---
name: surge-module-development
description: >-
  Use when developing Surge `.sgmodule` files with Panel scripts,
  editable parameters, HTTP API integration, and VPS monitoring panels.
  Covers module metadata, the `#!arguments` parameter system, Panel JS
  patterns, Surge script HTTP client quirks, and routing pitfalls.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [surge, panel, module, sgmodule, javascript, vps-monitor]
    related_skills: [surge-ruleset-maintenance, systematic-debugging]
---

# Surge Module Development

## Overview

Develop Surge `.sgmodule` files — self-contained configuration patches
that override or augment the main profile. Modules can add Panel
dashboards, Script-driven data fetches, URL/Host rewrite rules, and
editable user parameters.

This skill focuses on **script-driven Panel modules** (the most complex
case), but the principles apply to any module type.

## Quick Reference — Module Anatomy

```ini
#!name=Module Name
#!desc=Short description
#!category=📊 ▸ Monitor
#!arguments=KEY1:default1,KEY2:default2

[General]
key = value

[Panel]
PanelName = icon="sf-symbol",icon-color="#HEX",script-name=my-script

[Rule]
RULE-TYPE,value,POLICY

[Script]
my-script = type=generic,timeout=10,script-path=https://raw.githubusercontent.com/org/repo/COMMIT_HASH/path.js,argument=key1={{{KEY1}}}&key2={{{KEY2}}}
```

Note: no `update-interval` → manual refresh only. Add `update-interval=N` if auto-refresh is desired.

## Editable Parameters (`#!arguments`)

### Syntax

```
#!arguments=KEY:default_value,KEY2:default_value2
#!arguments-desc=[Description]\n\nitem 1\n\nitem 2
```

- **Colon** (`:`) separates key from default value
- **Comma** (`,`) separates key-value pairs
- Each key becomes a **placeholder** `{{{KEY}}}` in the module content
- Surge replaces placeholders with user input at install time

### CRITICAL: Default value restrictions

Default values MUST NOT contain:
- `:` — conflicts with the KEY:value separator
- `,` — conflicts with the pair separator
- `&` — may be misinterpreted as query-string separator

✅ `SERVER:server_address`
✅ `TOKEN:access_token`
❌ `SERVER:http://1.2.3.4:8765` — colon in URL breaks parsing

Put the **real format in `#!arguments-desc`** as instructional text.

### Placeholder syntax

Use **`{{{KEY}}}`** (triple curly braces), NOT `%KEY%`:

```ini
argument=server={{{SERVER}}}&token={{{TOKEN}}}
```

`{{{KEY}}}` substitution works in **any module field**, not just
`argument=`. This includes `script-path=`:

```ini
# ✅ Works: Surge substitutes the IP into script-path
vps-panel = type=generic,timeout=10,script-path=http://{{{SERVER}}}:8765/panel.js

# ✅ Also works in argument= as expected
my-script = type=generic,timeout=10,script-path=https://...,argument=host={{{HOST}}}
```

This is useful when you want the user to configure only an IP via
long-press, without exposing secrets in the GitHub repo or dealing
with `#!arguments` parsing issues in the JS.

### `#!arguments-desc` newlines

Write `\n` as literal backslash-n (0x5C 0x6E), NOT as real newlines.
Surge interprets `\n` as line breaks in the parameter UI:

```ini
#!arguments-desc=[设置]\n\n① SERVER: VPS 地址\n   例: http://1.2.3.4:8765
```

## Module Sections

### `[General]`

Supports **override** and **append** (`%APPEND%`):

```ini
[General]
skip-proxy = %APPEND% 45.94.40.38
```

The module can add to `skip-proxy` — this is checked **before the rule
engine** by Surge and is the most reliable way to ensure DIRECT routing.

### `[Panel]`

```ini
[Panel]
PanelName = icon="sf-symbol",icon-color="#HEX",script-name=script-ref,update-interval=N
```

- `icon`: any valid SF Symbol name
- `icon-color`: HEX color for the icon
- `script-name`: must match the name in `[Script]` section
- `update-interval`: seconds between auto-refreshes (triggers when user
  opens the policy selection view; minimum practical value is 1)
  **Many users prefer manual refresh** — omit `update-interval` entirely
  and the panel only refreshes when tapped.
- `argument=` goes on the `[Script]` line, **NOT** on the `[Panel]` line

### `[Rule]` (in modules)

Module rules are inserted at the TOP of the user's existing rules.
Only DIRECT, REJECT, and REJECT-TINYGIF policies are allowed:

```ini
[Rule]
DEST-PORT,8765,DIRECT
```

### `[Script]`

```ini
[Script]
panel-script = type=generic,timeout=10,script-path=https://github.com/raw/...,argument=key1={{{KEY1}}}
```

- `type=generic` for panel scripts
- `argument=` — placed HERE, not on the `[Panel]` line
- `script-path` — use `raw.githubusercontent.com/org/repo/branch/path`
  for hosted scripts; Surge caches the script content

## Panel JavaScript Patterns

### $httpClient.get() — ALWAYS use callback pattern

Surge's JS runtime does NOT support `async/await` with `$httpClient`.
`await $httpClient.get(url)` returns `undefined`.

✅ **Correct pattern**:

```javascript
$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({ title: "...", content: "❌ " + error, style: "error" });
    return;
  }
  if (!response || response.status !== 200) {
    $done({ title: "...", content: "❌ HTTP " + response.status, style: "error" });
    return;
  }
  // data = response body string
  var info = JSON.parse(data);
  $done({ title: "🖥 " + info.hostname, content: formattedContent });
});
```

❌ **Does NOT work**:
```javascript
var resp = await $httpClient.get(url);   // resp is undefined
```

### JS Compatibility — Surge uses an older JS engine

| Modern JS | ✅ Surge-safe equivalent |
|---|---|
| `const` / `let` | `var` |
| `` `template ${var}` `` | `"string " + var` |
| `"str".repeat(n)` | `for (var i=0; i<n; i++) s += "x"` |
| `async/await` | callback pattern |
| `arrow functions` | Use with caution — `function(){}` is safer |

### Accessing `$argument`

`$argument` is a parsed object, NOT a raw string:

```javascript
var server = $argument ? $argument.server || "http://127.0.0.1:8765" : "http://127.0.0.1:8765";
var token  = $argument ? $argument.token  || "changeme"              : "changeme";
```

### Error output — show the REAL error

Display the actual error message for diagnostics:

```javascript
if (error) {
  // Show the raw error, NOT a generic "网络错误"
  $done({ content: "❌ " + error });
}
```

## Routing: Making Panel Script Traffic Go DIRECT

When a Surge panel script makes `$httpClient.get("http://VPS_IP:PORT")`,
the request goes through Surge's routing engine. If the user's config
sends that traffic through a proxy, the connection fails because the
monitor port is not a proxy port.

**Double-lock approach** (use BOTH):

```ini
[General]
# Layer 1: Network-level bypass (checked before rules)
skip-proxy = %APPEND% VPS_IP_ADDRESS

[Rule]
# Layer 2: Rule-level fallback
DEST-PORT,MONITOR_PORT,DIRECT
```

`skip-proxy` is the stronger mechanism — it tells Surge to never proxy
traffic to that IP, regardless of rules. `DEST-PORT` adds a rule-level
safety net.

## GitHub CDN Cache Behavior

- `raw.githubusercontent.com/<ref>/main/` has `max-age=300` (5 min cache)
- After pushing changes, the `main` branch URL may serve stale content
- **In practice, the CDN can cache for much longer than 5 minutes** —
  after many pushes to the same file, edge nodes may serve versions that
  are **weeks old** even though `git show HEAD:path` shows correct code
- **Workaround: ALWAYS use a specific commit hash URL** as the primary
  `script-path` in production modules:
  `raw.githubusercontent.com/org/repo/<commit-hash>/path`
- The commit hash URL bypasses CDN caching completely — the correct
  version is always served immediately after push
- When you update the JS, also update the module's `script-path` to
  point to the new commit hash
- The `main` branch CDN resolves independently per-request, not per-file
- Module script URLs (`script-path=`) also go through CDN; force refresh
  by reinstalling the module

## Panel Content Formatting Best Practices

When building numeric dashboard panels (monitoring, status, metrics),
follow these **user-validated** layout rules after iterative refinement:

### Column layout strategy

1. **Emoji column** — all emojis followed by exactly **1 space**. Do NOT
   try to compensate for narrow emojis (🖥, 💾) with extra spaces; in
   Surge's rendering, emojis all take the same visual width.
2. **Label column** — pad to a fixed visual-cell width using a
   Unicode-aware function. Chinese chars are 2 cells, ASCII is 1 cell:
   ```javascript
   function padLabel(s) {
     var w = 0;
     for (var i = 0; i < s.length; i++)
       w += s.charCodeAt(i) > 127 ? 2 : 1;
     while (w < 6) { s += " "; w++; }
     return s;
   }
   ```
3. **Data column** — left-align everything after the padded label. Do
   NOT right-align percentages to make detail data align — the resulting
   variable whitespace looks worse than natural left-alignment.
4. **Unit conversion** — for monitoring panels, convert MB to GB
   (`value / 1024`) to keep values short and readable.
5. **No progress bars** — text-only is cleaner. The █░ characters add
   visual noise without actionable information.
6. **Single `\n` spacing** — double `\n\n` (blank line) between every row
   is too much vertical space in Surge's compact panel display. Single
   `\n` keeps everything readable.

### Final format template

```javascript
var c = "";
c += "🧠 " + padLabel("内存") + memoryPercent + "% " + memUsedG + "G/" + memTotalG + "G\n";
c += "🖥 " + padLabel("CPU")  + cpuPct + "% " + load + "/" + cores + "核\n";
c += "💾 " + padLabel("硬盘") + diskPercent + "% " + diskUsed + "G/" + diskTotal + "G\n";
c += "📡 " + padLabel("流量") + "⬆" + txGb + "G ⬇" + rxGb + "G\n";
c += "🌐 " + padLabel("IP")   + publicIp + "\n";
c += "📍 " + padLabel("位置") + location + "\n";
c += "🏢 " + padLabel("ISP")  + isp + "\n";
c += "⏱ " + padLabel("运行") + uptime;
```

### Common layout pitfalls

- **Don't pad labels by character count** (`s.length`) — "内存" is 2 JS
  chars but 4 visual cells. Use the Unicode-aware `padLabel()` above.
- **Don't right-align percentages** — the detail column won't align
  perfectly with non-percentage rows (traffic, IP, location) anyway.
  Left-align everything for consistent appearance.
- **Don't add extra space after narrow emojis** — in Surge, emoji widths
  are uniform. Extra spaces just push the label column off.
- **Don't forget unit conversion** — 93548.6MB wraps lines in the panel.
  Always show large values in GB with 1 decimal.

## Common Pitfalls

1. **`#!arguments` default values with `:` or `,`**. These break the
   KEY:value parser. Use clean placeholder defaults like `server_address`
   and describe the real format in `#!arguments-desc`.
2. **`async/await` with `$httpClient`**. NOT supported. Use callback
   pattern `function(error, response, data){}`.
3. **`argument=` on `[Panel]` line**. Must be on `[Script]` line.
4. **Template literals / `const` / `let` / `String.repeat()`**. Surge's
   JS engine may not support these. Use `var`, `+` concatenation,
   traditional `for` loops.
5. **Proxy routing for script HTTP requests**. Script-initiated HTTP
   goes through Surge's routing. Monitor-only ports need explicit
   DIRECT treatment via `skip-proxy %APPEND%` and/or `DEST-PORT`.
6. **CDN cache on installation**. If the module fails after a recent
   push, use a commit-hash URL instead of `main` branch.
7. **Module `[Rule]` only supports internal policies**. DIRECT, REJECT,
   REJECT-TINYGIF only — no proxy policies.
8. **`#!arguments-desc` newline format**. Must be literal `\n`
   (backslash + n), not real newlines.
9. **Not showing the real HTTP error**. Always include `error` or
   `response.status` in failure output for diagnostics.
10. **`#!arguments` default values limited → use JS-side fallback**.
    Since `#!arguments` defaults cannot contain `:` (URLs), `,`, or `&`,
    real defaults live in the Panel JS. Two patterns depending on repo
    visibility:

    **Private repo / acceptable risk**: hardcode real credentials in JS,
    `#!arguments` acts as override only:
    ```javascript
    var API_BASE = "http://1.2.3.4:8765";  // real default in JS
    var TOKEN = "actual-token-here";
    if ($argument.server) API_BASE = $argument.server;
    if ($argument.token) TOKEN = $argument.token;
    ```

    **Public repo (security)**: use only placeholder defaults in JS too.
    User MUST configure via `#!arguments` long-press:
    ```javascript
    var API_BASE = "http://127.0.0.1:8765";  // safe placeholder
    var TOKEN = "changeme";
    if ($argument.server) API_BASE = "http://" + $argument.server + ":8765";
    if ($argument.token) TOKEN = $argument.token;
    ```
    Note the port is hardcoded in JS (see pitfall #11).

    Meanwhile `#!arguments` keeps clean placeholders:
    ```ini
    #!arguments=SERVER:server_address,TOKEN:access_token
    ```
11. **Panel `update-interval` only fires when the policy view is open**.
    The panel does NOT auto-refresh in the background — it only refreshes
    when the user is looking at the policy selection view.
    Some users prefer **manual refresh only** (no `update-interval` at
    all) — the panel refreshes when tapped. Respect this preference when
    the user asks for it.
12. **`#!arguments` / `{{{KEY}}}` substitution may break silently on some Surge versions.**  
    Even when all syntax rules are followed (no `:`/`,`/`&` in defaults,  
    `{{{KEY}}}` placeholders used, `argument=` on `[Script]` line), the  
    parameter substitution can fail silently. This affects `{{{KEY}}}`  
    in BOTH `argument=` AND `script-path=` fields — the module loads,  
    the panel appears, but `$argument` values are `undefined` (falls  
    through to JS defaults) or `script-path` remains the literal  
    `{{{KEY}}}` string. Result: connection to `127.0.0.1` (JS default)  
    or a broken URL, giving "connection refused".  

    **Diagnosis**: Add the suspected variable to the error output to  
    confirm what Surge actually passed:

    ```javascript
    // In the HTTP error handler:
    $done({
      title: "VPS Monitor",
      content: "❌ HTTP " + code + "\\nserver: " + API_BASE + "\\ntoken: " + TOKEN
    });
    ```
    If `token:` shows your JS default (e.g. `changeme`) instead of the  
    user-entered value, `#!arguments` substitution is failing — switch  
    to self-hosting `/panel.js`.

    **Root cause**: Confirmed on multiple iterations — even with  
    perfectly clean defaults (`server_address`, `access_token`), certain  
    Surge versions/device configs do not inject `$argument` reliably.  
    Not a syntax error; a runtime gap.

    **Reliable fallback**: Self-host the panel JS (see section below).  
    When the JS is served dynamically from your server, no `#!arguments`  
    is needed — the module is a static pointer with zero user-editable  
    fields.
13. **`skip-proxy` in public repos exposes your server IP.** If your
    module is in a public GitHub repo and you use `skip-proxy = %APPEND%
    1.2.3.4`, that IP is visible to everyone. Mitigation: rely on the
    `[Rule] DEST-PORT` directive instead, which doesn't need the IP, or
    use the `{{{SERVER}}}` placeholder in `script-path` so the user
    configures the IP locally.
14. **`#!arguments-desc` helps users set up correctly.** Use it to
    explain what format each argument expects and provide setup
    instructions visible during module installation.
    Even when all syntax rules are followed (no `:`/`,`/`&` in defaults,
    `{{{KEY}}}` placeholders used, `argument=` on `[Script]` line), the
    parameter substitution can fail silently. Symptoms: the module loads,
    the panel appears, but `$argument` contains `undefined` or wrong
    values → connection refused. This appears to be a Surge version
    compatibility issue. If this happens after ruling out all syntax
    errors, the **reliable fallback is to self-host the panel JS** (see
    section below).

## Self-Hosting Surge Panel Scripts (Bypasses `#!arguments`)

When `#!arguments` is unreliable for your Surge version, serve the
panel script directly from your API server instead of GitHub.

### Architecture

```ini
# Module: point script-path at your server
[Script]
vps-panel = type=generic,timeout=10,script-path=http://YOUR_IP:PORT/panel.js
```

Your server generates the JS **dynamically** with the correct endpoint
URL and auth token baked in:

```python
PANEL_JS_TEMPLATE = """\
var API_BASE = "http://{IP}:{PORT}";
var TOKEN = "{TOK...";
var url = API_BASE + "/status?token=" + TOKEN;
// ... rest of panel script ...
"""

def _build_panel_js():
    return (PANEL_JS_TEMPLATE
            .replace("{IP}", ip)
            .replace("{PORT}", str(PORT))
            .replace("{TOKEN}", ACCESS_TOKEN))
```

**CRITICAL**: Use `.replace()` not `.format()` — the JS template
contains `{}` (object literals, function bodies) that Python
`str.format()` will misinterpret as format placeholders.

### Key design decisions

- **`/panel.js` endpoint does NOT require auth** — it only generates JS
  code, no sensitive data. The `/status` (data) endpoint still requires
  the token.
- **Route `/panel.js` BEFORE the auth check** in your HTTP handler.
- **No `#!arguments` in the module** — remove the `#!arguments=` line
  entirely and the `argument=` from the `[Script]` line. The module
  becomes a simple reference with no user-editable parameters.
- **GitHub has zero secrets** — the module only contains the public
  server IP and port, which are already reachable.
- **No CDN cache issues** — JS is served fresh each time. Set
  `Cache-Control: no-cache` to prevent stale script caching.

### Router order in your HTTP server

```python
def do_GET(self):
    path = self.path.split("?", 1)[0]

    # 1. Unauthenticated endpoints FIRST
    if path == "/panel.js":
        serve_panel_js()
        return

    # 2. Authenticated endpoints AFTER
    token = parse_token(self.path)
    if token != ACCESS_TOKEN:
        send_403()
        return

    if path == "/status":
        serve_status()
        return
```

### When to use this pattern

| Situation | Recommended approach |
|---|---|
| `#!arguments` works fine | Use `#!arguments` + GitHub-hosted JS |
| `#!arguments` gives connection errors | Self-host `/panel.js` |
| Public GitHub repo (secrets concern) | Self-host `/panel.js` OR `#!arguments` with placeholder defaults |
| Private repo | Hardcode in JS directly |

### `{{{SERVER}}}` in `script-path` + self-hosted `/panel.js`

When `#!arguments` works for simple fields (no `:`, `,` in defaults) but
you want to avoid exposing the IP/token in your GitHub repo, try this
hybrid:

```ini
# Module — no secrets, user fills IP on install
#!name=VPS Monitor
#!desc=实时查看 VPS 状态。长按编辑 SERVER 填入 IP
#!arguments=SERVER:server_address

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=http://{{{SERVER}}}:8765/panel.js
```

The user long-presses the module and fills in JUST the IP (e.g.
`45.94.40.38`). Surge substitutes `{{{SERVER}}}` in `script-path=`,
making the final URL `http://45.94.40.38:8765/panel.js`.

**⚠️ Caveat**: `{{{KEY}}}` in `script-path` can also fail on some Surge
versions (same silent-substitution bug as `argument=`). If the panel
cannot connect, verify by checking whether the module loaded the URL
correctly. If it fails, fall back to the full self-hosting approach
below (no `#!arguments`, no `{{{KEY}}}` — just a static script-path).

**Advantages over plain self-hosting:**
- ✅ No IP hardcoded in module (public GitHub)
- ✅ No `#!arguments` parsing needed in JS (avoids Surge version bugs)
- ✅ JS served fresh each time (no CDN cache issues)
- ✅ `/panel.js` endpoint handles the complexity (generates JS with
  correct IP, port, and token baked in)

### Security: `skip-proxy` and public repos

`skip-proxy = %APPEND% YOUR_VPS_IP` exposes your server's public IP in
the GitHub repo. This is visible to anyone who views the module file.

**Mitigations:**
1. **Rely on `DEST-PORT` rule** instead (no IP needed):
   ```ini
   [Rule]
   DEST-PORT,8765,DIRECT
   ```
   Surge evaluates module `[Rule]` sections and applies DIRECT routing
   for the monitor port. This is sufficient for VPS Monitor traffic.
2. **Use a domain name** instead of raw IP if you have one.
3. **If you MUST use `skip-proxy`**, generate the module locally with
   the real IP and don't commit to a public repo.
