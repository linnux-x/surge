# VPS Monitor — Complete Reference

Surge Panel + Python backend that monitors VPS system metrics (CPU, memory, disk, network, uptime).

## Architecture

```
Surge iOS (Panel)                VPS (Python)
      │                              │
      ├── install module ──────────► GitHub (no secrets)
      │                              │
      ├── fetch panel.js ──────────► HTTP server :8765/panel.js
      │                              │  └── returns JS with token baked in
      │                              │
      └── request /status?token=xx─► HTTP server :8765/status
                                       └── returns JSON metrics
```

Two connection methods supported:
1. **`#!arguments` mode**: JS from GitHub, user fills IP + Token in module UI
2. **`/panel.js` mode**: JS from VPS directly, install-and-refresh (no config)

## Backend: vps_monitor.py

Zero-dependency Python HTTP server using only stdlib (`http.server`, `json`, `os`, `subprocess`).

### Key design decisions

- **Token from environment variable**: `ACCESS_TOKEN = os.environ.get("VPS_MONITOR_TOKEN", "changeme")`
- **DEST-PORT rule**: Surge module includes `DEST-PORT,8765,DIRECT` to ensure the panel connects directly (not through the proxy tunnel), preventing proxy loops since the VPS is also the proxy server
- **/panel.js endpoint**: No auth required (generates JS, not sensitive data). Bakes correct IP and token into the JavaScript at request time
- **/status endpoint**: Token-auth required via `?token=` query parameter. Returns JSON with hostname, uptime, memory, CPU, disk, network, IP location

### Security considerations

- **HTTP not HTTPS**: All traffic is plaintext. Token and metrics visible on the network.
- **Token in URL query parameter**: Visible in server access logs. Prefer `Authorization: Bearer <token>` header for production use.
- **Binding to 0.0.0.0**: Server listens on all interfaces. For better security, bind to `127.0.0.1` and put behind a reverse proxy (Caddy, Nginx) with HTTPS.
- **Running as root**: Creates a dedicated `vpsmon` system user and run the service under that user.

## Panel JS Format

```
🧠 内存    74.2%  2.8G/3.8G
🖥 CPU     4%    0.08/2核
💾 硬盘    18.8%  7.9G/42.2G
📡 流量    ⬆91.6G ⬇103.2G
🌐 IP      45.94.40.38
📍 位置    Tokyo, Japan
🏢 ISP     xTom Japan Corporation
⏱ 运行    14d 1h 27m
```

Formatting rules:
- Labels padded to 6 visual cells (via `padLabel()` Unicode-aware function)
- 2 spaces between percentage and detail data
- Emoji + 1 space before label
- Traffic displayed in GB (÷1024 from server's MB values)
- Memory also converted to GB for consistency

## Module: VPS-Monitor.sgmodule

Two configurations:

### Mode 1: `#!arguments` (user fills IP + Token)

```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态。长按编辑填写 IP 和 Token
#!arguments=SERVER=vps_ip&TOKEN=access_token

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,
  script-path=https://raw.githubusercontent.com/linnux-x/surge/HASH/scripts/vps_monitor_panel.js,
  argument=server=%SERVER%&token=%TOKEN%
```

### Mode 2: `/panel.js` (install and refresh, no config)

```ini
#!name=VPS Monitor
#!desc=实时查看 VPS 状态

[Panel]
VPS-Status = icon="server.rack",icon-color="#58A6FF",script-name=vps-panel

[Rule]
DEST-PORT,8765,DIRECT

[Script]
vps-panel = type=generic,timeout=10,script-path=http://riven.linnux.cc:8765/panel.js
```

## Troubleshooting: `#!arguments` substitution fails

**Symptom**: Panel shows `token: changeme` despite user setting TOKEN. Or connects to `127.0.0.1` despite setting SERVER.

**Root cause**: Unknown. May be a Surge version issue, module syntax quirk, or encoding problem. After 2-3 syntax variations, switch to `/panel.js` mode instead.

**Debug steps**:
1. Add the token value to the error display to see what's actually passed:
   ```javascript
   $done({ content: "...server: " + API_BASE + "\\ntoken: " + TOKEN });
   ```
2. Read the result:
   - `token: changeme` → substitution never happened (JS default)
   - `token: {{{TOKEN}}}` → placeholder was not replaced (literal)
   - `token: FHR2uZ...` → substitution works, check other issues

## Files

| File | Purpose |
|------|---------|
| `scripts/vps_monitor.py` | Python HTTP server (port 8765) |
| `scripts/vps_monitor_panel.js` | Surge Panel JS (GitHub-hosted, with argument parsing) |
| `Module/VPS-Monitor.sgmodule` | Surge module (points to GitHub JS or /panel.js) |
