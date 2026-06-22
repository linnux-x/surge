// VPS Monitor Panel — Surge Panel Script
// Fetches system stats from VPS monitor server and displays in Surge panel.
// Uses callback pattern ($httpClient.get does not support await in Surge).

var API_BASE = "http://127.0.0.1:8765";
var TOKEN = "changeme";

if (typeof $argument !== "undefined" && $argument) {
  if ($argument.server) API_BASE = $argument.server;
  if ($argument.token) TOKEN = $argument.token;
}

var url = API_BASE + "/status?token=" + TOKEN;

$httpClient.get(url, function(error, response, data) {
  if (error) {
    $done({
      title: "VPS Monitor",
      content: "❌ 网络错误: " + error,
      style: "error"
    });
    return;
  }
  
  if (!response || response.status !== 200) {
    var code = response ? response.status : "无响应";
    $done({
      title: "VPS Monitor",
      content: "❌ 连接失败 (" + code + ")\n请检查 server 和 token",
      style: "error"
    });
    return;
  }
  
  try {
    var info = JSON.parse(data);
    
    // Progress bars
    var memBar   = bar(info.memory.percent, 10);
    var cpuPct   = Math.min(Math.round(info.cpu.load_1m / info.cpu.cores * 100), 100);
    var cpuBar   = bar(cpuPct, 10);
    var diskBar  = bar(info.disk.percent, 10);
    
    var content =
      "🧠 内存    " + memBar  + "  " + info.memory.used_mb + "MB / " + info.memory.total_mb + "MB (" + info.memory.percent + "%)" + "\n" +
      "🖥  CPU     " + cpuBar  + "  负载 " + info.cpu.load_1m + " / " + info.cpu.cores + "核" + "\n" +
      "💾 硬盘    " + diskBar + "  " + info.disk.used_gb + "G / " + info.disk.total_gb + "G (" + info.disk.percent + "%)" + "\n" +
      "📡 流量    ⬆" + info.network.tx_total_mb + "MB ⬇" + info.network.rx_total_mb + "MB" + "\n" +
      "🌐 IP      " + info.ip.public_ip + "\n" +
      "📍 位置    " + info.ip.location + "\n" +
      "🏢 ISP     " + info.ip.isp + "\n" +
      "⏱ 运行    " + info.uptime;
    
    $done({
      title: "🖥 " + info.hostname,
      content: content,
      icon: "server.rack",
      "icon-color": "#58A6FF"
    });
  } catch (e) {
    $done({
      title: "VPS Monitor",
      content: "❌ 解析错误: " + e.message,
      style: "error"
    });
  }
});

// Helper: text progress bar
function bar(percent, width) {
  var filled = Math.round((Math.min(percent, 100) / 100) * width);
  var empty = width - filled;
  var s = "";
  for (var i = 0; i < filled; i++) s += "█";
  for (var i = 0; i < empty; i++) s += "░";
  return s;
}
