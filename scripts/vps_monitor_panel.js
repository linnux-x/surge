// VPS Monitor Panel — Surge Panel Script
// Fetches system stats from VPS monitor server and displays in Surge panel.
//
// Configuration: edit the API_BASE and TOKEN below, OR set module arguments:
//   arg1 = server URL (e.g. http://1.2.3.4:8765)
//   arg2 = access token

const API_BASE = $argument ? $argument.server || "http://127.0.0.1:8765" : "http://127.0.0.1:8765";
const TOKEN = $argument ? $argument.token || "changeme" : "changeme";

(async () => {
  try {
    const url = `${API_BASE}/status?token=${TOKEN}`;
    const resp = await $httpClient.get(url);
    if (resp.status !== 200) {
      $done({
        title: "VPS Monitor",
        content: `❌ 连接失败 (${resp.status})\n请检查服务器和 Token`,
        style: "error",
      });
      return;
    }

    const data = JSON.parse(resp.body);

    // ── Build progress bars ──────────────────────────────────
    const memBar = bar(data.memory.percent, 10);
    const cpuBar = bar(data.cpu.load_1m / data.cpu.cores * 100, 10);
    const diskBar = bar(data.disk.percent, 10);

    // ── Format lines ─────────────────────────────────────────
    const memLine = `🧠 内存    ${memBar}  ${data.memory.used_mb}MB / ${data.memory.total_mb}MB (${data.memory.percent}%)`;
    const cpuLine = `🖥  CPU     ${cpuBar}  负载 ${data.cpu.load_1m} / ${data.cpu.cores}核`;
    const diskLine = `💾 硬盘    ${diskBar}  ${data.disk.used_gb}G / ${data.disk.total_gb}G (${data.disk.percent}%)`;
    const netLine = `📡 流量    ⬆${data.network.tx_total_mb}MB ⬇${data.network.rx_total_mb}MB`;
    const ipLine = `🌐 IP      ${data.ip.public_ip}`;
    const locLine = `📍 位置    ${data.ip.location}`;
    const ispLine = `🏢 ISP     ${data.ip.isp}`;
    const uptimeLine = `⏱ 运行    ${data.uptime}`;

    const content = [
      memLine,
      cpuLine,
      diskLine,
      netLine,
      ipLine,
      locLine,
      ispLine,
      uptimeLine,
    ].join("\n");

    $done({
      title: `🖥 ${data.hostname}`,
      content: content,
      icon: "server.rack",
      "icon-color": "#58A6FF",
    });
  } catch (e) {
    $done({
      title: "VPS Monitor",
      content: `❌ 错误: ${e.message || e}`,
      style: "error",
    });
  }
})();

// ── Helper: generate a text progress bar ──────────────────────
function bar(percent, width) {
  const filled = Math.round((Math.min(percent, 100) / 100) * width);
  const empty = width - filled;
  const fillChar = "█";
  const emptyChar = "░";
  return fillChar.repeat(filled) + emptyChar.repeat(empty);
}
