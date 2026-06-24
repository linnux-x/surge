---
name: surge-module-authoring
description: Create, edit, and debug Surge `.sgmodule` files — including Panel dashboards, Generic scripts, URL Rewrite, Host, MITM overrides, and parameter tables. Covers the module format, script integration, editable parameter UI via `#!arguments`, and the `{{{KEY}}}` placeholder system.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [surge, module, panel, script, configuration, networking]
    related_skills: [surge-ruleset-maintenance, github-repo-management]
---

# Surge Module Authoring

## Overview

A Surge module (`.sgmodule`) is a patch that overrides or appends to sections of the main profile. Modules let you toggle features, panels, and scripts independently without editing the main config.

This skill covers writing modules that use **Panels**, **Scripts**, and **Parameter Tables** — the three features that make modules interactive and user-configurable.

## Module Structure

A `.sgmodule` file is INI-format with metadata headers:

```ini
#!name=My Module
#!desc=What this module does
#!category=📊 ▸ Monitor
#!system=mac,ios          # optional: restrict to platforms
```

## Section Mapping

| Module Section | Behaviour |
|---|---|
| `[General]` | Override keys: `key = value`. Append: `key = %APPEND% value` |
| `[MITM]` | Override `hostname` with `%APPEND%` |
| `[Host]` | New lines insert at top |
| `[URL Rewrite]` | New lines insert at top |
| `[Script]` | Script definitions — referenced by name from Panel |
| `[Panel]` | Dashboard panels (iOS only) |
| `[Rule]` | Only `DIRECT` / `REJECT` / `REJECT-TINYGIF` policies allowed |

## Panel System (Dynamic Mode)

Panels display custom dashboards in Surge's policy-selection view. **Dynamic panels** use a script that runs on refresh or interval.

### Panel Section (no argument — argument goes on Script)

```ini
[Panel]
MyPanel = icon="server.rack",icon-color="#58A6FF",script-name=my-script,update-interval=30

[Script]
my-script = type=generic,timeout=10,script-path=https://raw.githubusercontent.com/...,argument=key1=val1&key2=val2
```

**CRITICAL**: The `argument=` field goes on the **`[Script]`** line, NOT the `[Panel]` line. Putting it on Panel breaks Surge's argument-edit UI.

### Panel Script Template (JavaScript)

**⚠️ CRITICAL**: `$httpClient.get()` uses a **callback pattern** `(error, response, data)`. `await $httpClient.get(url)` returns `undefined` in Surge's Panel script context — do NOT use async/await with `$httpClient`. Always use the callback pattern.

```javascript
// ✅ Correct callback pattern
var args = $argument || {};
// args.key1 -> "val1", args.key2 -> "val2"

$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({ title: "Error", content: "❌ " + error, style: "error" });
    return;
  }
  $done({
    title: "🖥 Panel Title",
    content: "Line 1\\nLine 2",
    icon: "server.rack",
    "icon-color": "#58A6FF",
  });
});
```

**🔴 DO NOT use async/await with `$httpClient.get()`** — this is a known pitfall:

```javascript
// ❌ WRONG — resp is undefined, crashes with "undefined is not an object"
var resp = await $httpClient.get(url);
if (resp.status !== 200) { ... }  // TypeError: undefined is not an object
```

If you need sequential HTTP calls, nest callbacks or use a promise wrapper (Surge runtime support for Promise varies):

```javascript
function httpGet(url) {
  return new Promise(function(resolve, reject) {
    $httpClient.get(url, function(error, resp, data) {
      if (error) { reject(error); return; }
      resolve({ status: resp.status, headers: resp.headers, body: data });
    });
  });
}

// Then use with async/await:
(async function() {
  try {
    var resp = await httpGet(url);
    // resp.status, resp.body work now
  } catch (e) { ... }
})();
```

### JS Engine Compatibility Notes

Surge's JavaScript runtime (JavaScriptCore) may lag behind modern JS engines. For maximum compatibility:

| Feature | Safe? | Alternative |
|---|---|---|
| `const` / `let` | ✅ Generally safe | `var` for maximum compatibility |
| Arrow functions `=>` | ⚠️ Most Surge versions support it | Use `function()` keywords |
| Template literals `` `...${var}` `` | ⚠️ Some older versions don't | String concatenation: `"text " + var` |
| `String.repeat(n)` | ⚠️ Not always available | `for` loop or `Array(n+1).join(char)` |
| `Object.fromEntries()` | ❌ Not available | Manual loop |
| `URLSearchParams` | ❌ Not available | Manual `.split('&')` parsing |
| Async/await | ⚠️ Available but `$httpClient` doesn't return promises | Use callback pattern (safe) |

When in doubt, use `var`, `function()`, and `+` string concatenation.

### Error State (Callback Pattern)

Always handle errors in panel scripts — Surge panels silently fail otherwise:

```javascript
$httpClient.get(url, function(error, response, data) {
  // 1. Network-level error (timeout, DNS, unreachable)
  if (error) {
    $done({
      title: "VPS Monitor",
      content: "❌ 网络错误: " + error,
      style: "error",
    });
    return;
  }
  
  // 2. HTTP-level error (non-200 status)
  if (!response || response.status !== 200) {
    var code = response ? response.status : "无响应";
    $done({
      title: "VPS Monitor",
      content: "❌ 连接失败 (" + code + ")\\n请检查配置",
      style: "error",
    });
    return;
  }
  
  // 3. Parse error (malformed JSON)
  try {
    var info = JSON.parse(data);
    // ... use info ...
    $done({
      title: "🖥 " + info.hostname,
      content: "🧠 内存: " + info.memory.percent + "%",
      icon: "server.rack",
      "icon-color": "#58A6FF",
    });
  } catch (e) {
    $done({
      title: "VPS Monitor",
      content: "❌ 解析错误: " + e.message,
      style: "error",
    });
  }
});
```

Style values: `info` (default, icon shown), `good`, `alert`, `error`.
When `style` is omitted and `icon` is set, the icon color controls appearance.

## Parameter Tables (`#!arguments`)

Surge Mac 5.5.0+ / iOS 5.10.0+ lets you declare **user-editable parameters** that show a form when the module is installed or long-pressed.

### Two Syntax Formats

There are TWO documented syntaxes. **Both appear in real-world modules:**

| Syntax | Format | Placeholder | Notes |
|--------|--------|-------------|-------|
| **Colon (legacy)** | `#!arguments=KEY:val,KEY2:val2` | `{{{KEY}}}` | Widely used in community modules |
| **Query-string (official)** | `#!arguments=KEY=val&KEY2=val2` | `%KEY%` | Per official Surge manual |

The official Surge manual (manual.nssurge.com) documents the **query-string format** with `%KEY%` substitution. Many popular community modules (e.g., Script-Hub) use the colon format. When in doubt, prefer the official query-string format for newer Surge versions.

### Placeholder Format

| Syntax | Placeholder | Example |
|--------|-------------|---------|
| Query-string (official) | `%HOST%` | `argument=host=%HOST%` |
| Colon (legacy) | `{{{HOST}}}` | `argument=host={{{HOST}}}` |

### Description (shown in the edit UI)

```
#!arguments-desc=[Setup]\\n\\n❶ HOST: Server address\\n\\n❷ PORT: Port number
```

Use literal `\\n` (backslash + n) for newlines. NOT actual newline characters.

### Full Example (query-string format, official)

```ini
#!name=Example Module
#!desc=Shows parameter editing
#!arguments=HOST=example.com&PORT=8080
#!arguments-desc=[Setup]\\n\\n❶ HOST: Server hostname\\n\\n❷ PORT: TCP port

[Panel]
Example = icon=\"gearshape\",script-name=example

[Script]
example = type=generic,script-path=https://...,argument=host=%HOST%&port=%PORT%
```

### Full Example (colon format, legacy)

```ini
#!name=Example Module
#!desc=Shows parameter editing
#!arguments=HOST:example.com,PORT:8080
#!arguments-desc=[Setup]\\n\\n❶ HOST: Server hostname\\n\\n❷ PORT: TCP port

[Panel]
Example = icon=\"gearshape\",script-name=example

[Script]
example = type=generic,script-path=https://...,argument=host={{{HOST}}}&port={{{PORT}}}
```

### How Surge Processes Arguments

1. User installs module → Surge reads `#!arguments` → shows edit UI with fields
2. User fills in values → Surge replaces `%KEY%` or `{{{KEY}}}` everywhere in the module
3. The final `argument=` becomes e.g. `host=actual.value&port=1234`
4. The panel script receives `$argument = {host: \"actual.value\", port: \"1234\"}`

### Critical Pitfall: Special Characters in Default Values (Colon Format)

When using the colon format (`KEY:value`), the `:` is the key-value separator. **Default values must NOT contain `:` or `,`** — these characters confuse the parser and cause Surge to reject the module as invalid.

**WRONG** — causes "无效的模块" (invalid module):
```ini
#!arguments=SERVER:http://1.2.3.4:8765
# The `:` in \"http://\" and \"1.2.3.4:8765\" breaks parsing
```

**RIGHT** — use a clean placeholder:
```ini
#!arguments=SERVER:server_address
```

The query-string format (`KEY=value`) does NOT have this `:` conflict, making it safer for values containing URLs or ports.

### Critical Pitfall: Placeholder Substitution May Fail Silently

In some Surge configurations or versions, `{{{KEY}}}` or `%KEY%` substitution silently fails. The module loads but `$argument` is undefined or has default values.

**Symptoms of failed substitution:**
- Panel shows `token: changeme` despite user setting TOKEN in module UI
- Panel connects to `127.0.0.1` despite user setting SERVER
- The JS fallback value is used instead of the user's configured value

**Root cause is not always identifiable.** Substitution may fail due to version edge cases, encoding issues, or module syntax quirks. After 2-3 failed attempts at fixing the syntax, switch strategies instead of iterating on more variations.

**Debugging**: Add the actual variable value to the error display:

```javascript
if (!response || response.status !== 200) {
  $done({
    title: \"VPS Monitor\",
    content: \"❌ HTTP \" + code + \"\\nserver: \" + API_BASE + \"\\ntoken: \" + TOKEN,
    ...
  });
}
```

This reveals whether substitution happened:
- `token: changeme` → substitution failed (JS default was never overridden)
- `token: {{{TOKEN}}}` → placeholder literal not replaced
- `token: FHR2uZ...` → substitution worked

### Pitfall: GitHub raw CDN Cache

After pushing module changes to `main`, `raw.githubusercontent.com` CDN caches for up to 5 minutes (max-age=300). If a user installs during this window, they get the **old** version — and if the old version had a syntax error, they see \"无效的模块\" even though your latest code is correct.

**Workaround**: Use a specific commit hash URL for immediate validation:

```
https://raw.githubusercontent.com/user/repo/COMMIT_HASH/Module/Module.sgmodule
```

The commit-specific URL bypasses the CDN cache. Once 5 minutes pass, `main` branch URL also reflects the latest content.

### Pitfall: `#!arguments-desc` Newline Encoding

The `#!arguments-desc` field renders newlines in the parameter edit UI. The file must contain **literal `\\n`** (two bytes: backslash 0x5C + n 0x6E) — NOT actual newline characters.

Verify with xxd:
```
5c 6e 5c 6e  →  \\n\\n  ✅  Surge renders two line breaks
0a 0a        →  (actual newlines) ❌  Surge shows no breaks
```

## Alternative: Service-Hosted Panel JS (`/panel.js`)

When `#!arguments` substitution fails and the root cause cannot be identified, the most reliable alternative is to **serve the panel script directly from the backend service** that the panel monitors. This approach was proven in a real VPS Monitor implementation after `{{{KEY}}}` substitution repeatedly failed across multiple syntax variations.

### How it works

1. The backend service (e.g., a Python HTTP server) exposes a `/panel.js` endpoint
2. The endpoint generates JavaScript with the correct URL and auth token baked in
3. The Surge module points `script-path` directly to this endpoint
4. No `#!arguments` needed — no substitution to fail, no CDN cache to worry about

### Module side

```ini
#!name=My Service Monitor
#!desc=Monitor status

[Panel]
Status = icon=\"server.rack\",icon-color=\"#58A6FF\",script-name=status-panel

[Rule]
# Ensure panel traffic goes DIRECT (important if the VPS is also the proxy)
DEST-PORT,8765,DIRECT

[Script]
status-panel = type=generic,timeout=10,script-path=http://service-host:8765/panel.js
```

### Backend side (Python)

```python
PANEL_JS_TEMPLATE = \"\"\"// Panel Script (auto-generated)
var API_BASE = \"http://service-host:{PORT}\";
var TOKEN = \"{TOKEN}\";
var url = API_BASE + \"/status?token=\" + TOKEN;
// ... rest of panel JS (formatting, error handling) ...
\"\"\"

def _build_panel_js():
    return (PANEL_JS_TEMPLATE
            .replace(\"{PORT}\", str(PORT))
            .replace(\"{TOKEN}\", ACCESS_TOKEN))

# In HTTP handler:
path = self.path.split(\"?\", 1)[0]
if path == \"/panel.js\":
    js = _build_panel_js()
    self.send_response(200)
    self.send_header(\"Content-Type\", \"application/javascript; charset=utf-8\")
    self.send_header(\"Cache-Control\", \"no-cache\")
    self.end_headers()
    self.wfile.write(js.encode(\"utf-8\"))
    return
```

### Advantages over `#!arguments`

| Factor | `#!arguments` | `/panel.js` |
|--------|---------------|-------------|
| GitHub secrets | Placeholders only | Zero secrets on GitHub |
| User setup | Must fill in fields | Install and refresh |
| Reliability | Substitution can fail silently | Always works |
| Token rotation | User must re-enter and reinstall | Just restart the service |
| CDN cache | Must use commit hashes | Direct HTTP, no cache |

### When to use each

- **Use `#!arguments` when**: You need user-configurable parameters, the Surge version is known to support substitution, and you have verified it works end-to-end.
- **Use `/panel.js` when**: The panel script needs secrets (tokens, passwords) and you control the backend, OR when `#!arguments` substitution fails for unknown reasons.

### Hybrid Fallback Strategy

For maximum reliability, support BOTH methods simultaneously:

1. Module uses `#!arguments` with safe defaults + `argument=` pointing to GitHub-hosted JS
2. The GitHub JS accepts `$argument.server` and `$argument.token` with safe fallback defaults
3. The backend also serves `/panel.js` with the token baked in
4. If `#!arguments` works → user configures parameters normally
5. If `#!arguments` fails → user switches the module's `script-path` to the `/panel.js` URL

## Generic Scripts

Scripts in modules can do more than panels:

```ini
[Script]
my-script = type=generic,timeout=10,script-path=...,argument=...
panel-script = type=generic,timeout=10,script-path=...,argument=...
```

The `type=generic` is correct for both standalone scripts AND panel-updating scripts. Surge differentiates them by context: when a Panel references `script-name=panel-script`, Surge knows to call it with panel parameters.

## Surge JS Runtime API

### Available Globals

- `$httpClient.get(url, callback)` / `$httpClient.post(url, body, callback)`
  
  **Callback signature**: `callback(error, response, data)`
  - `error`: string or `undefined`. Set when network fails (timeout, DNS, unreachable).
  - `response`: object `{status: number, headers: object}` or `undefined` on network failure.
  - `data`: string — the response body. Passed as a **third parameter**, NOT as `response.body`.

  **⚠️ DO NOT use `await`** — `await $httpClient.get(url)` returns `undefined`. Always use the callback pattern.

- `$notification.post(title, subtitle, body)`
- `$notification.post(title, subtitle, body)`
- `$persistentStore.read(key)` / `$persistentStore.write(key, value)`
- `$done(response)` — complete the script; for panels, pass `{title, content, style?, icon?, icon-color?}`
- `$argument` — the parsed argument object (from `argument=key=val&key2=val2`)
- `$trigger` — context: `"button"` or `"auto-interval"`
- `$env` — metadata about the current environment

### Timeout

Set `timeout=` on the Script line (default 5s, Surge Mac 5s max per script). For network requests that may be slow, set `timeout=10` or higher.

## VPS Monitor — Concrete Reference

See `references/surge-vps-monitor-pattern.md` for the complete VPS Monitor implementation pattern: Python HTTP server collecting system metrics + Surge Panel JS displaying formatted progress bars + sgmodule with editable SERVER/TOKEN parameters.

## Module Distribution

Host the `.sgmodule` file and any referenced `.js` scripts on a public URL (GitHub raw is standard). The module URL is what users install in Surge:

```
https://raw.githubusercontent.com/user/repo/main/Module/MyModule.sgmodule
```

Scripts referenced via `script-path=` must also be publicly accessible URLs — typically also GitHub raw.

## Validation Checklist

- [ ] Metadata headers present: `#!name`, `#!desc`, `#!category`
- [ ] `#!arguments` format: `KEY:val,KEY2:val2` (colon) OR `KEY=val&KEY2=val2` (query-string)
- [ ] Placeholders match the syntax: `{{{KEY}}}` (colon) or `%KEY%` (query-string)
- [ ] If `#!arguments` substitution fails after 2-3 attempts, switch to service-hosted `/panel.js` pattern
- [ ] `argument=` is on the `[Script]` line, NOT the `[Panel]` line
- [ ] `script-name=` in Panel matches a `[Script]` line name
- [ ] Panel scripts handle errors with `style: "error"` in `$done()`
- [ ] If using `icon` and `icon-color` on Panel, they are SF Symbol names and valid hex colors
- [ ] `#!system` is set if the module uses iOS-only features (like Panel)
- [ ] All `script-path` URLs are valid and publicly accessible
- [ ] `update-interval` is reasonable (30-60s for monitoring, 1-5s for node switching)
