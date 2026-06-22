#!/usr/bin/env python3
"""VPS Monitor Server — Lightweight HTTP server exposing system metrics as JSON.
Designed for Surge Panel integration. Zero dependencies beyond Python stdlib."""

import json
import os
import socket
import subprocess
import time
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── Configuration ──────────────────────────────────────────────
HOST = "0.0.0.0"
PORT = 8765
ACCESS_TOKEN = os.environ.get("VPS_MONITOR_TOKEN", "changeme")
IP_CACHE_TTL = 3600  # refresh public IP/location every hour

# ── Cached external IP data ────────────────────────────────────
_ip_cache = {"data": None, "ts": 0}


def _get_ip_info():
    """Fetch public IP, ISP, location from ip-api.com (free, no key)."""
    now = time.time()
    if _ip_cache["data"] and (now - _ip_cache["ts"]) < IP_CACHE_TTL:
        return _ip_cache["data"]
    try:
        req = urllib.request.Request(
            "http://ip-api.com/json/?fields=16777215",
            headers={"User-Agent": "VPS-Monitor/1.0"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
            _ip_cache["data"] = {
                "public_ip": data.get("query", "N/A"),
                "isp": data.get("isp", "N/A"),
                "location": ", ".join(
                    filter(None, [data.get("city"), data.get("country")])
                ) or "N/A",
                "org": data.get("org", "N/A"),
            }
            _ip_cache["ts"] = now
    except Exception:
        _ip_cache["data"] = _ip_cache["data"] or {
            "public_ip": "N/A",
            "isp": "N/A",
            "location": "N/A",
            "org": "N/A",
        }
    return _ip_cache["data"]


def _read_proc(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError:
        return ""


def _get_memory():
    """Parse /proc/meminfo for memory stats (in MB)."""
    mem = _read_proc("/proc/meminfo")
    total = used = available = 0
    for line in mem.splitlines():
        if line.startswith("MemTotal:"):
            total = int(line.split()[1]) // 1024
        elif line.startswith("MemAvailable:"):
            available = int(line.split()[1]) // 1024
    used = total - available
    percent = round(used / total * 100, 1) if total else 0
    return {
        "total_mb": total,
        "used_mb": used,
        "free_mb": available,
        "percent": percent,
    }


def _get_cpu():
    """Parse /proc/stat + /proc/loadavg for CPU stats."""
    load = _read_proc("/proc/loadavg").split()[:3]
    cpu = {"load_1m": 0.0, "load_5m": 0.0, "load_15m": 0.0}
    if len(load) >= 3:
        cpu["load_1m"] = float(load[0])
        cpu["load_5m"] = float(load[1])
        cpu["load_15m"] = float(load[2])
    cpu["cores"] = os.cpu_count() or 1
    return cpu


def _get_disk():
    """Parse df output for disk stats (root partition, in GB)."""
    try:
        out = subprocess.check_output(
            ["df", "-B1", "/"], timeout=5, stderr=subprocess.DEVNULL
        ).decode()
        lines = out.strip().splitlines()
        if len(lines) >= 2:
            parts = lines[-1].split()
            if len(parts) >= 4:
                total = int(parts[1])
                used = int(parts[2])
                free = int(parts[3])
                return {
                    "total_gb": round(total / 1e9, 1),
                    "used_gb": round(used / 1e9, 1),
                    "free_gb": round(free / 1e9, 1),
                    "percent": round(used / total * 100, 1),
                }
    except Exception:
        pass
    return {"total_gb": 0, "used_gb": 0, "free_gb": 0, "percent": 0}


def _get_network():
    """Parse /proc/net/dev for total traffic + instant rates (in MB)."""
    net = _read_proc("/proc/net/dev")
    rx_total = tx_total = 0
    for line in net.splitlines():
        if ":" not in line or "lo" in line:
            continue
        parts = line.split()
        rx_total += int(parts[1]) if len(parts) > 1 else 0
        tx_total += int(parts[9]) if len(parts) > 9 else 0
    return {
        "rx_total_mb": round(rx_total / 1e6, 1),
        "tx_total_mb": round(tx_total / 1e6, 1),
    }


def _get_uptime():
    """Parse /proc/uptime."""
    uptime_secs = float(_read_proc("/proc/uptime").split()[0] or 0)
    days = int(uptime_secs // 86400)
    hours = int((uptime_secs % 86400) // 3600)
    minutes = int((uptime_secs % 3600) // 60)
    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    elif hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"


def get_status():
    """Main function: collect all system stats."""
    mem = _get_memory()
    cpu = _get_cpu()
    disk = _get_disk()
    net = _get_network()
    ip_info = _get_ip_info()
    uptime = _get_uptime()
    hostname = socket.gethostname()

    return {
        "hostname": hostname,
        "uptime": uptime,
        "timestamp": int(time.time()),
        "memory": mem,
        "cpu": cpu,
        "disk": disk,
        "network": net,
        "ip": ip_info,
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Token auth
        params = {}
        if "?" in self.path:
            query = self.path.split("?", 1)[1]
            for part in query.split("&"):
                if "=" in part:
                    k, v = part.split("=", 1)
                    params[k] = v
        token = params.get("token", "")
        if token != ACCESS_TOKEN:
            self.send_response(403)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Forbidden"}).encode())
            return

        status = get_status()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(status, ensure_ascii=False).encode())

    def log_message(self, fmt, *args):
        # Suppress default logging to avoid noise
        pass


def main():
    print(f"VPS Monitor Server starting on {HOST}:{PORT}")
    print(f"Access with ?token={ACCESS_TOKEN}")
    server = HTTPServer((HOST, PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()


if __name__ == "__main__":
    main()
