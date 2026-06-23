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
    
    // Progress bars
    function bar(pct, w) {
      var f = Math.round((Math.min(pct, 100) / 100) * w);
      var e = w - f;
      var s = "";
      for (var i = 0; i < f; i++) s += "█";
      for (var i = 0; i < e; i++) s += "░";
      return s;
    }
    
    var cpuPct = Math.min(Math.round(info.cpu.load_1m / info.cpu.cores * 100), 100);
    
    var c = "";
    c += "🧠 内存    " + bar(info.memory.percent, 10) + "  " + info.memory.used_mb + "MB/" + info.memory.total_mb + "MB (" + info.memory.percent + "%)\n";
    c += "🖥  CPU     " + bar(cpuPct, 10) + "  负载 " + info.cpu.load_1m + "/" + info.cpu.cores + "核\n";
    c += "💾 硬盘    " + bar(info.disk.percent, 10) + "  " + info.disk.used_gb + "G/" + info.disk.total_gb + "G (" + info.disk.percent + "%)\n";
    c += "📡 流量    ⬆" + info.network.tx_total_mb + "MB ⬇" + info.network.rx_total_mb + "MB\n";
    c += "🌐 IP      " + info.ip.public_ip + "\n";
    c += "📍 位置    " + info.ip.location + "\n";
    c += "🏢 ISP     " + info.ip.isp + "\n";
    c += "⏱ 运行    " + info.uptime;
    
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
