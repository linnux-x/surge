# VPS Monitor — Reference Implementation

A concrete working example of a Surge Panel module that fetches and
displays VPS system stats. Updated to reflect the **final production
layout** after iterative user refinement.

## Architecture

```
[VPS]                                    [User iPhone / Mac]
  │                                          │
  │  vps_monitor.py                          │  Surge
  │  Port 8765, token auth                   │    │
  │  GET /status?token=xxx → JSON            │    │
  │                                          │    ├─ Module installs (sgmodule)
  │  ┌─ memory: {total_mb, used_mb, percent} │    │  $httpClient.get() callback
  │  ├─ cpu: {load_1m, load_5m, cores}       │    │  → DIRECT (skip-proxy + DEST-PORT)
  │  ├─ disk: {total_gb, used_gb, percent}   │    │  → displays in Surge UI
  │  ├─ network: {tx_total_mb, rx_total_mb}  │    │
  │  ├─ ip: {public_ip, isp, location}       │    ▼
  │  └─ uptime, hostname                     │  [Dashboard Panel]
  │                                          │  🖥 linnux
  │  └─ systemd service (auto-start)         │  🧠 内存  69.3% 2.6G/3.8G
  └──────────────────────────────────────────┘  🖥 CPU     4% 0.07/2核
```

## Final Optimized Display

After multiple rounds of user feedback, the panel settled on this
**fully left-aligned, column-gapped** layout:

```
🧠 内存  69.6% 2.6G/3.8G
🖥 CPU    6% 0.11/2核
💾 硬盘  18.8% 7.9G/42.2G
📡 流量  ⬆91.4G ⬇103.1G
🌐 IP    45.94.40.38
📍 位置  Tokyo, Japan
🏢 ISP   xTom Japan Corporation
⏱ 运行  13d 23h 30m
```

Key formatting decisions (each was user-validated):

| Decision | Why |
|---|---|
| **No progress bars** | Cleaner, less visual noise |
| **Traffic in GB** | MB values like 93548.6MB are too long |
| **Memory also in GB** | Consistent with traffic/disk |
| **Left-aligned labels** | Labels start at same column |
| **Left-aligned data after label** | All data starts at same column |
| **Unicode-aware label padding (6 visual cells)** | Chinese chars (2 cells/char) and ASCII (1 cell) need different padding |
| **All emojis followed by 1 space** | Emojis render consistently in Surge; no width hack needed |
| **Single `\n` spacing** | Double blank lines between rows felt too tall |

## Port Pattern: CRITICAL `#!arguments` Trap

**Problem**: `#!arguments=KEY:value` uses `:` as the key-value separator.
If the default value contains `:` (e.g. `45.94.40.38:8765`), Surge's
parser interprets `45.94.40.38` as the value and discards `8765` as
garbage → the module gets a bare IP with no port → connection refused.

**Fix**: Hardcode port 8765 in the JavaScript. `#!arguments` only passes
the IP address (no port, no scheme):

```javascript
// ✅ CORRECT — port is hardcoded
var PORT = 8765;
if ($argument.server) {
    API_BASE = "http://" + $argument.server + ":" + PORT;
}

// ❌ WRONG — server comes as "45.94.40.38" (port eaten by #!arguments parser)
//    even if user typed "45.94.40.38:8765"
```

```ini
# Module: #!arguments takes bare IP only
#!arguments=SERVER:server_address,TOKEN:access_token
```

The user types just `45.94.40.38` in the SERVER field — no colon, no
port, no scheme.

## Security: Public Repo Credential Protection

**Problem**: Hardcoding real IP and token in the Panel JS means they're
pushed to a public GitHub repo, visible to anyone.

**Two solutions, depending on Surge version compatibility:**

### Option A: `#!arguments` (recommended when it works)

1. **JS defaults = safe placeholders** (not real credentials):
   ```javascript
   var API_BASE = "http://127.0.0.1:8765";  // safe placeholder
   var TOKEN = "changeme";                    // safe placeholder
   ```

2. **Real values via `#!arguments`** — user long-presses the module in
   Surge and fills in SERVER/IP and TOKEN:
   ```javascript
   if ($argument.server) {
     API_BASE = "http://" + $argument.server + ":8765";
   }
   if ($argument.token) TOKEN = $argument.token;
   ```
   Note: port is hardcoded in JS (not in the argument) to avoid the
   `:` conflict in `#!arguments=KEY:default` syntax.

3. **Module defaults are also placeholders**:
   ```ini
   #!arguments=SERVER:server_address,TOKEN:access_token
   ```

### Option B: Self-host `/panel.js` (fallback when `#!arguments` fails)

When `#!arguments` doesn't work on your Surge version (panel loads but
`$argument` is undefined → connection refused), serve the panel JS
directly from the monitoring server:

**Server side** (`vps_monitor.py`):

```python
# Template with placeholders for .replace() (NOT .format() — JS uses {})
PANEL_JS_TEMPLATE = """var API_BASE = "http://{IP}:{PORT}";
var TOKEN=*** url = API_BASE + "/status?token=" + TOKEN;
// ... full panel JS ...
"""

def _build_panel_js():
    return (PANEL_JS_TEMPLATE
            .replace("{IP}", PUBLIC_IP)
            .replace("{PORT}", str(PORT))
            .replace("{TOKEN}", ACCESS_TOKEN))

# In do_GET handler — route BEFORE auth check
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        # 1. No-auth endpoints first
        if path == "/panel.js":
            js = _build_panel_js()
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
            return
        # 2. Auth-gated endpoints
        # ... token check, /status route ...
```

**Module side** (`VPS-Monitor.sgmodule`) — no `#!arguments`, no `argument=`:
```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态
#!category=📊 ▸ Monitor

[General]
skip-proxy = %APPEND% 45.94.40.38

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel,update-interval=30

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=http://45.94.40.38:8765/panel.js
```

The tradeoff: users must manually configure the module after install,
but credentials never leave their device's Surge config (Option A).
Alternatively, Option B eliminates all manual config at the cost of
exposing the IP/port in the module (which is already public).

## Panel Script: `scripts/vps_monitor_panel.js`

### Complete, production-verified code:

```javascript
// VPS Monitor Panel — Surge Panel Script
// Uses callback pattern for Surge $httpClient API.
//
// Configure via module #!arguments:
// long-press module → edit SERVER (IP only, e.g. 45.94.40.38) and TOKEN.
// Port 8765 is fixed in the script (avoids : conflict in #!arguments).

var API_BASE = "http://127.0.0.1:8765";
var TOKEN = "changeme";

if (typeof $argument !== "undefined" && $argument) {
  if ($argument.server) {
    API_BASE = "http://" + $argument.server + ":8765";
  }
  if ($argument.token) TOKEN = $argument.token;
}

var url = API_BASE + "/status?token=" + TOKEN;

$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({ title: "VPS Monitor", content: "❌ " + error,
            icon: "server.rack", "icon-color": "#FF453A" });
    return;
  }
  if (!response || response.status !== 200) {
    var code = response ? response.status : "null";
    $done({ title: "VPS Monitor",
            content: "❌ HTTP " + code + "\\nserver: " + API_BASE,
            icon: "server.rack", "icon-color": "#FF453A" });
    return;
  }
  try {
    var info = JSON.parse(data);

    var cpuPct = Math.min(Math.round(
      info.cpu.load_1m / info.cpu.cores * 100), 100);
    var memUsedG = (info.memory.used_mb / 1024).toFixed(1);
    var memTotalG = (info.memory.total_mb / 1024).toFixed(1);
    var txGb = (info.network.tx_total_mb / 1024).toFixed(1);
    var rxGb = (info.network.rx_total_mb / 1024).toFixed(1);

    // Unicode-aware pad: Chinese chars = 2 cells, ASCII = 1 cell
    function padLabel(s) {
      var w = 0;
      for (var i = 0; i < s.length; i++)
        w += s.charCodeAt(i) > 127 ? 2 : 1;
      while (w < 6) { s += " "; w++; }
      return s;
    }

    var c = "";
    c += "🧠 " + padLabel("内存") + info.memory.percent + "% "
      + memUsedG + "G/" + memTotalG + "G\\n";
    c += "🖥 " + padLabel("CPU") + cpuPct + "% "
      + info.cpu.load_1m + "/" + info.cpu.cores + "核\\n";
    c += "💾 " + padLabel("硬盘") + info.disk.percent + "% "
      + info.disk.used_gb + "G/" + info.disk.total_gb + "G\\n";
    c += "📡 " + padLabel("流量") + "⬆" + txGb + "G ⬇" + rxGb + "G\\n";
    c += "🌐 " + padLabel("IP") + info.ip.public_ip + "\\n";
    c += "📍 " + padLabel("位置") + info.ip.location + "\\n";
    c += "🏢 " + padLabel("ISP") + info.ip.isp + "\\n";
    c += "⏱ " + padLabel("运行") + info.uptime;

    $done({
      title: "🖥 " + info.hostname,
      content: c,
      icon: "server.rack",
      "icon-color": "#58A6FF",
    });
  } catch (e) {
    $done({ title: "VPS Monitor",
            content: "❌ 解析失败: " + e.message,
            icon: "server.rack", "icon-color": "#FF453A" });
  }
});
```

### Alternative: Self-Hosted Panel JS (no `#!arguments`)

If `#!arguments` is unreliable on your Surge version, the server
generates the JS dynamically with values baked in. The JS is simpler
(no `$argument` parsing needed):

```javascript
// Auto-generated by vps_monitor.py /panel.js endpoint
// Values (IP, token) are baked in at generation time.

var API_BASE = "http://45.94.40.38:8765";
var TOKEN=*** url = API_BASE + "/status?token=" + TOKEN;

$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({ title: "VPS Monitor", content: "❌ " + error,
            icon: "server.rack", "icon-color": "#FF453A" });
    return;
  }
  if (!response || response.status !== 200) {
    var code = response ? response.status : "null";
    $done({ title: "VPS Monitor",
            content: "❌ HTTP " + code + "\\nserver: " + API_BASE,
            icon: "server.rack", "icon-color": "#FF453A" });
    return;
  }
  try {
    var info = JSON.parse(data);
    // … same padLabel() and formatting code as above …
    $done({ title: "🖥 " + info.hostname, content: c,
            icon: "server.rack", "icon-color": "#58A6FF" });
  } catch (e) {
    $done({ title: "VPS Monitor",
            content: "❌ 解析失败: " + e.message,
            icon: "server.rack", "icon-color": "#FF453A" });
  }
});
```

The module points directly to the server endpoint — no `argument=` line:

```ini
[Script]
vps-panel = type=generic,timeout=10,script-path=http://45.94.40.38:8765/panel.js
```

See the "Self-Hosting Surge Panel Scripts" section in the parent skill
(`surge-module-development`) for full server-side implementation details.

```javascript
function padLabel(s) {
  var w = 0;
  for (var i = 0; i < s.length; i++)
    w += s.charCodeAt(i) > 127 ? 2 : 1;
  while (w < 6) { s += " "; w++; }
  return s;
}
```

This is the critical function for column alignment. It pads each label to
exactly **6 visual cells**:
- "内存" (4 cells, 2 Chinese chars) → "内存  " (6 cells)
- "CPU" (3 cells, 3 ASCII) → "CPU   " (6 cells)
- "IP" (2 cells) → "IP    " (6 cells)

## Module: `Module/VPS-Monitor.sgmodule`

Three variants — choose based on your Surge version's `#!arguments`
compatibility:

### Option A: With `#!arguments` (GitHub-hosted JS)

```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态：内存 CPU 硬盘 流量 IP
#!category=📊 ▸ Monitor
#!arguments=SERVER:server_address,TOKEN:access_token

[General]
skip-proxy = %APPEND% 45.94.40.38

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel,update-interval=30

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=https://raw.githubusercontent.com/linnux-x/surge/main/scripts/vps_monitor_panel.js,argument=server={{{SERVER}}}&token={{{TOKEN}}}
```

### Option B: Pure Self-Hosting (no `#!arguments`, no `{{{KEY}}}` — static `script-path`)

**Use when**: `#!arguments` AND `{{{KEY}}}` in `script-path` both fail on
your Surge version (confirmed by `token: changeme` in error output — see
diagnosis section below). The module is a simple static pointer to your
server, which dynamically generates the panel JS with correct values.

**Module** (`VPS-Monitor.sgmodule`) — on GitHub, zero secrets, zero
configurable fields:

```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态：内存 CPU 硬盘 流量 IP
#!category=📊 ▸ Monitor

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel

[Rule]
# 端口级规则确保 VPS Monitor 直连
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=http://riven.linnux.cc:8765/panel.js
```

Key points:
- **No `#!arguments=`** — no editable parameters.
- **No `argument=`** on `[Script]` — values are baked into the JS.
- **No `skip-proxy`** — `DEST-PORT` alone is sufficient.
- **No `update-interval`** — manual tap refresh.
- **Domain name instead of raw IP** (`riven.linnux.cc` → resolves to the
  VPS). This is cleaner than exposing a raw IP in the module.
- **`script-path` is static** — no `{{{KEY}}}` placeholders that might
  fail to substitute.

**Server** (`vps_monitor.py`) — `/panel.js` endpoint generates JS with
the correct IP and token baked in:

```python
# Template: use .replace() NOT .format() — JS uses {}
PANEL_JS_TEMPLATE = """var API_BASE = "http://riven.linnux.cc:8765";
var TOKEN = "{TOKEN}";
var url = API_BASE + "/status?token=" + TOKEN;
// ... full panel JS (padLabel, formatting) ...
"""

def _build_panel_js():
    return PANEL_JS_TEMPLATE.replace("{TOKEN}", ACCESS_TOKEN)

# Route BEFORE auth check
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/panel.js":  # 1. No-auth first
            js = _build_panel_js()
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
            return
        # 2. Token auth for /status
        ...
```

**User flow**: Install module → tap to refresh → works instantly.
No long-press editing, no fields to fill.

### When `#!arguments` Fails — Diagnosis

If you suspect `#!arguments` substitution is not working:

1. **Add the token to error output**:
   ```javascript
   if (!response || response.status !== 200) {
     $done({
       content: "❌ HTTP " + code + "\\nserver: " + API_BASE + "\\ntoken: " + TOKEN
     });
   }
   ```
2. **Read the panel error**: if `token: changeme` appears (your JS
   default), `$argument.token` is `undefined` — substitution failed.
   If `token: {{{TOKEN}}}` appears, the placeholder wasn't replaced at
   all.
3. **Escalate**: Switch to Option B (pure self-hosting, no placeholders).

When `#!arguments` works for simple fields but you want:
- ✅ No IP/token in GitHub repo
- ✅ No CDN cache issues
- ✅ No `#!arguments` parsing bugs
- ✅ User configures only IP via long-press

**Module** (`VPS-Monitor.sgmodule`) — on GitHub, no secrets:

```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态。长按编辑 SERVER 填入 VPS IP
#!category=📊 ▸ Monitor
#!arguments=SERVER:server_address

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=http://{{{SERVER}}}:8765/panel.js
```

Note: no `skip-proxy` (avoids hardcoded IP), no `argument=` (JS comes
from `/panel.js` with values baked in), no `update-interval` (manual
refresh only unless user wants auto).

**Server** (`vps_monitor.py`) — generates JS with real IP and token:

```python
PANEL_JS_TEMPLATE = """// VPS Monitor Panel — Surge Panel Script (auto-generated)
var API_BASE = "http://{IP}:{PORT}";
var TOKEN = "{TOKEN}";
var url = API_BASE + "/status?token=" + TOKEN;

$httpClient.get(url, function(error, response, data) {
  // ... full panel formatting code ...
});
"""

def _build_panel_js():
    return (PANEL_JS_TEMPLATE
            .replace("{IP}", PUBLIC_IP)
            .replace("{PORT}", str(PORT))
            .replace("{TOKEN}", ACCESS_TOKEN))

# In do_GET — route BEFORE auth
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/panel.js":                # 1. No-auth first
            js = _build_panel_js()
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
            return
        # 2. Token check for /status
        ...
```

**User flow**:
1. Install module from GitHub
2. Long-press → edit SERVER → type `45.94.40.38` (just IP, no port)
3. Tap panel to refresh → Surge fetches JS from `http://45.94.40.38:8765/panel.js`
4. Server generates JS with correct IP and token → panel displays data

## Server: `scripts/vps_monitor.py`

Zero-dependency Python HTTP server using only stdlib. Collects 6 metrics:

| Metric | Source | Method |
|---|---|---|
| Memory | `/proc/meminfo` | Parse MemTotal, MemAvailable → MB + % |
| CPU | `/proc/loadavg` + `os.cpu_count()` | Load averages + core count |
| Disk | `df -B1 /` | Parse total, used, free → GB + % |
| Network | `/proc/net/dev` | Sum rx/tx bytes (excluding lo) → MB |
| IP/ISP | ip-api.com | Public IP, ISP, location (cached 1h) |
| Uptime | `/proc/uptime` | Days/hours/minutes format |

### Verification Commands

```bash
# Test server locally with token
curl -s "http://127.0.0.1:8765/status?token=your-token" | python3 -m json.tool

# Auth rejection without token
curl -s http://127.0.0.1:8765/status     # → {"error": "Forbidden"}

# Check systemd
systemctl status vps-monitor
journalctl -u vps-monitor -n 20 --no-pager
```
