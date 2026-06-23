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

    // Pad label to 6 visual cells so data after it starts at same column
    function padLabel(s) {
      var w = 0, a = s.split("");
      for (var i = 0; i < a.length; i++) w += a[i].charCodeAt(0) > 127 ? 2 : 1;
      while (w < 6) { s += " "; w++; }
      return s;
    }

    var c = "";
    c += "🧠 " + padLabel("内存") + info.memory.percent + "% " + memUsedG + "G/" + memTotalG + "G\n";
    c += "🖥 " + padLabel("CPU") + cpuPct + "% " + info.cpu.load_1m + "/" + info.cpu.cores + "核\n";
    c += "💾 " + padLabel("硬盘") + info.disk.percent + "% " + info.disk.used_gb + "G/" + info.disk.total_gb + "G\n";
    c += "📡 " + padLabel("流量") + "⬆" + txGb + "G ⬇" + rxGb + "G\n";
    c += "🌐 " + padLabel("IP") + info.ip.public_ip + "\n";
    c += "📍 " + padLabel("位置") + info.ip.location + "\n";
    c += "🏢 " + padLabel("ISP") + info.ip.isp + "\n";
    c += "⏱ " + padLabel("运行") + info.uptime;
    
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
