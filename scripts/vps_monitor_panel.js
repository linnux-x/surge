// VPS Monitor Panel — Surge Panel Script
// Uses callback pattern for Surge $httpClient API.

// Default: connect to VPS at public IP. Override via #!arguments SERVER + TOKEN.
// SERVER can be "host:port" (auto-prepends http://) or full "http://host:port".
var API_BASE = "http://45.94.40.38:8765";
var TOKEN = "FHR2uZWirs6O6L74XDHb4BaWdvSxPs3q";

if (typeof $argument !== "undefined" && $argument) {
  if ($argument.server) {
    API_BASE = $argument.server;
    // Prepend http:// if missing (bare host:port from #!arguments)
    if (API_BASE.indexOf("http://") !== 0 && API_BASE.indexOf("https://") !== 0) {
      API_BASE = "http://" + API_BASE;
    }
  }
  if ($argument.token) TOKEN = $argument.token;
}

var url = API_BASE + "/status?token=" + TOKEN;

$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({
      title: "VPS Monitor",
      content: "❌ " + error,
      icon: "server.rack",
      "icon-color": "#FF453A"
    });
    return;
  }
  
  if (!response || response.status !== 200) {
    var code = response ? response.status : "null";
    $done({
      title: "VPS Monitor",
      content: "❌ HTTP " + code + "\nserver: " + API_BASE,
      icon: "server.rack",
      "icon-color": "#FF453A"
    });
    return;
  }
  
  try {
    var info = JSON.parse(data);
    
    var cpuPct = Math.min(Math.round(info.cpu.load_1m / info.cpu.cores * 100), 100);
    var memUsedG = (info.memory.used_mb / 1024).toFixed(1);
    var memTotalG = (info.memory.total_mb / 1024).toFixed(1);
    var txGb = (info.network.tx_total_mb / 1024).toFixed(1);
    var rxGb = (info.network.rx_total_mb / 1024).toFixed(1);

    // Pad label to 4 cells; right-align percentage to 5 chars for column alignment
    function l(s) { while (s.length < 4) s += " "; return s; }
    function r(s, w) { s = String(s); while (s.length < w) s = " " + s; return s; }

    var c = "";
    c += "🧠 " + l("内存") + r(info.memory.percent + "%", 5) + "  " + memUsedG + "G/" + memTotalG + "G\n\n";
    c += "🖥  " + l("CPU") + r(cpuPct + "%", 5) + "  " + info.cpu.load_1m + "/" + info.cpu.cores + "核\n\n";
    c += "💾  " + l("硬盘") + r(info.disk.percent + "%", 5) + "  " + info.disk.used_gb + "G/" + info.disk.total_gb + "G\n\n";
    c += "📡 " + l("流量") + "⬆" + txGb + "G ⬇" + rxGb + "G\n\n";
    c += "🌐 " + l("IP") + info.ip.public_ip + "\n\n";
    c += "📍 " + l("位置") + info.ip.location + "\n\n";
    c += "🏢 " + l("ISP") + info.ip.isp + "\n\n";
    c += "⏱ " + l("运行") + info.uptime;
    
    $done({
      title: "🖥 " + info.hostname,
      content: c,
      icon: "server.rack",
      "icon-color": "#58A6FF"
    });
  } catch (e) {
    $done({
      title: "VPS Monitor",
      content: "❌ 解析失败: " + e.message,
      icon: "server.rack",
      "icon-color": "#FF453A"
    });
  }
});
