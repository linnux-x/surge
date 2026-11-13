/**
 * Looking Glass · Surge 参考路由面板（仅 Surge）
 *
 * 显示公共探针到代理入口、落地 IP 的参考路径：IP、位置、AS。
 *
 * Surge 脚本只能发 HTTP 请求，设备本身做不了 traceroute，所以借 Globalping（https://globalping.io）
 * 的公共探针跑 mtr，分两段：
 *   第一段  本地 → 入口  从跟本地出口同城、同运营商的探针出发（找不到同城就用同运营商的）
 *   第二段  入口 → 落地  从跟入口同城、同网络的探针出发
 * 没有中转（入口就是落地）时只有一段：本地 → 落地。
 *
 * 要知道的限制：
 *   - 路径是「同城同网的探针」看到的，不是本机发出的包，不能据此判断本机真实路径或是否经过某条专线
 *   - 入口到落地走专线（IPLC/IEPL）时，公网追踪看不到专线，第二段只是公网的近似
 *   - 入口和落地的 IP 会发给 Globalping 作为追踪目标；本机 IP 不会发给它
 *   - 每次刷新用 1～2 次 Globalping 免费额度（不登录每小时 250 次），面板默认不自动刷新
 *
 * 每跳的位置用平安的 IP 接口查（走 DIRECT），AS 号来自 mtr，AS 名称用 Surge 自带的库本地查。
 * 延迟取每跳的最小值。骨干网路由器的位置以 IP 库为准，电信国际等骨干 IP 偶尔会被定位到海外别处。
 *
 * 参数（模块里填）：
 *   Proxy   落地 IP 走哪个策略或策略组查；默认「跟随规则」
 *   Probe   第一段的探针，默认「自动」；也可以手填 Globalping 的位置写法，如 Nanjing+AS4134
 *   MaskIP  本地、入口、落地 IP 打码，默认 true（中间路由器的 IP 不打码）
 */

const GP_API = 'https://api.globalping.io/v1/measurements';
const GP_HEADERS = { 'Content-Type': 'application/json', Accept: 'application/json', 'User-Agent': 'surge-route-trace/1.0' };
const JSON_HEADERS = { Accept: 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' };
const TITLE = 'Looking Glass';
const ICON = 'point.3.connected.trianglepath.dotted';
const ERROR_COLOR = '#FF3B30';
const STARTED = Date.now();
const DEADLINE = 52000; // 模块的脚本超时是 60 秒，留几秒把结果交出去
const FOLLOW_RULES = '跟随规则';
const AUTO = '自动';

// 运营商 → 骨干网 AS
const ISP_ASN = [
  [/电信/, 4134],
  [/联通/, 4837],
  [/移动|铁通/, 9808],
  [/腾讯/, 45090],
  [/阿里/, 37963],
  [/华为/, 55990],
];

// 省份 → 省会英文名；再加几个有探针的城市。Globalping 的城市名用英文
const PROVINCE_CAPITAL = {
  北京: 'Beijing', 天津: 'Tianjin', 上海: 'Shanghai', 重庆: 'Chongqing', 河北: 'Shijiazhuang', 山西: 'Taiyuan',
  内蒙古: 'Hohhot', 辽宁: 'Shenyang', 吉林: 'Changchun', 黑龙江: 'Harbin', 江苏: 'Nanjing', 浙江: 'Hangzhou',
  安徽: 'Hefei', 福建: 'Fuzhou', 江西: 'Nanchang', 山东: 'Jinan', 河南: 'Zhengzhou', 湖北: 'Wuhan', 湖南: 'Changsha',
  广东: 'Guangzhou', 广西: 'Nanning', 海南: 'Haikou', 四川: 'Chengdu', 贵州: 'Guiyang', 云南: 'Kunming', 西藏: 'Lhasa',
  陕西: "Xi'an", 甘肃: 'Lanzhou', 青海: 'Xining', 宁夏: 'Yinchuan', 新疆: 'Urumqi', 香港: 'Hong Kong', 澳门: 'Macau',
  台湾: 'Taipei',
};
const CITY_EN = {
  苏州: 'Suzhou', 无锡: 'Wuxi', 常州: 'Changzhou', 南通: 'Nantong', 宁波: 'Ningbo', 温州: 'Wenzhou', 金华: 'Jinhua',
  深圳: 'Shenzhen', 东莞: 'Dongguan', 佛山: 'Foshan', 厦门: 'Xiamen', 青岛: 'Qingdao', 大连: 'Dalian', 荆州: 'Jingzhou',
  十堰: 'Shiyan', 宜昌: 'Yichang', 洛阳: 'Luoyang', 绵阳: 'Mianyang',
};
// 省会没有探针时，再试一下旁边的大城市（如安徽的探针少，就近用南京、上海）
const NEARBY = {
  安徽: ['Nanjing', 'Shanghai'], 江西: ['Wuhan', 'Changsha'], 河北: ['Beijing', 'Tianjin'], 山西: ['Beijing'],
  浙江: ['Shanghai'], 江苏: ['Shanghai'], 广西: ['Guangzhou'], 海南: ['Guangzhou'], 贵州: ['Chengdu'], 重庆: ['Chengdu'],
  湖南: ['Wuhan'], 福建: ['Guangzhou', 'Shanghai'], 山东: ['Beijing', 'Shanghai'], 河南: ['Wuhan', 'Beijing'],
};

// ───────────────────────────── 参数 ─────────────────────────────

function readArgs(input) {
  const text = String(input || '');
  const keys = ['MaskIP', 'Probe', 'Proxy'];
  const marker = new RegExp(`(?:^|&)(${keys.join('|')})=`, 'g');
  const marks = [];
  for (let m = marker.exec(text); m; m = marker.exec(text)) marks.push({ key: m[1], start: m.index, end: marker.lastIndex });
  const args = {};
  marks.forEach((mark, i) => {
    args[mark.key] = text.slice(mark.end, i + 1 < marks.length ? marks[i + 1].start : text.length).trim();
  });
  const clean = value => (/^\{\{\{.*\}\}\}$/.test(value || '') ? '' : value || '');
  const proxy = clean(args.Proxy);
  const probe = clean(args.Probe);
  return {
    policy: proxy === FOLLOW_RULES ? '' : proxy,
    probe: probe === AUTO ? '' : probe,
    maskIP: !/^(false|0|no|off)$/i.test(clean(args.MaskIP)),
  };
}

// ───────────────────────────── 网络 ─────────────────────────────

function http(method, url, opts = {}) {
  return new Promise(resolve => {
    const options = { url, headers: opts.headers || JSON_HEADERS, timeout: Math.max(1, Math.min(opts.timeout || 8, timeLeft() / 1000)), 'auto-cookie': false };
    if (opts.body !== undefined) options.body = opts.body;
    if (opts.policy) options.policy = opts.policy;
    const send = method === 'POST' ? $httpClient.post : $httpClient.get;
    send.call($httpClient, options, (error, response, body) => {
      if (error) resolve({ ok: false, status: 0, body: '', error: String((error && error.message) || error) });
      else resolve({ ok: true, status: Number(response && (response.status || response.statusCode)) || 0, body: String(body || '') });
    });
  });
}

function parseJSON(text) {
  try {
    return JSON.parse(text);
  } catch {
    return null;
  }
}

const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
const timeLeft = () => DEADLINE - (Date.now() - STARTED);
const isIPv4 = ip => /^(?:\d{1,3}\.){3}\d{1,3}$/.test(ip) && ip.split('.').every(part => Number(part) <= 255);

// 平安的 IP 归属：不传 IP 查本机出口，传了查那个 IP。固定走 DIRECT。查不到返回 null
async function pinganInfo(ip) {
  const url = 'https://rmb.pingan.com.cn/itam/mas/linden/ip/request' + (ip ? `?ip=${encodeURIComponent(ip)}` : '');
  const res = await http('GET', url, { timeout: 5, policy: 'DIRECT' });
  const data = res.ok && res.status === 200 ? (parseJSON(res.body) || {}).data : null;
  if (!data || typeof data !== 'object') return null;
  const strip = value => String(value || '').trim().replace(/(省|市|特别行政区|壮族自治区|回族自治区|维吾尔自治区|自治区)$/, '');
  return {
    ip: String(data.ip || ip || ''),
    code: String(data.countryIsoCode || '').toUpperCase(),
    country: String(data.country || '').trim(),
    region: strip(data.region),
    city: strip(data.city),
    isp: String(data.isp || '').trim().replace(/^中国(?=.)/, ''),
  };
}

// 落地 IP，以及刚才那次查询走的策略和入口地址（从 Surge 最近的请求里找）
async function landingAndEntrance(policy) {
  const res = await http('GET', 'https://my.ippure.com/v1/info', { timeout: 8, policy });
  const data = res.ok && res.status === 200 ? parseJSON(res.body) : null;
  if (!data || !data.ip) throw new Error(`落地 IP 没查到（${res.ok ? `HTTP ${res.status}` : res.error}）`);
  if (!isIPv4(String(data.ip))) throw new Error('当前落地为 IPv6；本模块暂只支持 IPv4 参考追踪');
  const route = await new Promise(resolve => {
    let settled = false;
    const finish = value => {
      if (!settled) {
        settled = true;
        resolve(value);
      }
    };
    setTimeout(() => finish({}), 2000);
    try {
      $httpAPI('GET', '/v1/requests/recent', null, out => {
        const hit = ((out && out.requests) || []).slice(0, 50).find(req => String(req.URL || '').startsWith('https://my.ippure.com/v1/info'));
        const remote = hit ? String(hit.remoteAddress || '') : '';
        finish({
          policy: hit ? String(hit.policyName || '') : '',
          entrance: /\(Proxy\)/.test(remote) ? remote.replace(/\s*\(Proxy\)\s*/, '').trim() : '',
        });
      });
    } catch {
      finish({});
    }
  });
  const entrance = (String(route.entrance || '').match(/^\d{1,3}(?:\.\d{1,3}){3}/) || [])[0] || '';
  return { landing: String(data.ip), policy: route.policy || '', entrance: isIPv4(entrance) && entrance !== data.ip ? entrance : '' };
}

// ───────────────────────────── 探针 ─────────────────────────────

function ispASN(isp) {
  const hit = ISP_ASN.find(([pattern]) => pattern.test(isp || ''));
  return hit ? hit[1] : 0;
}

// 按「同城同网 → 省会同网 → 邻近城市同网 → 同网 → 同城 → 同国」的顺序列出候选探针位置
function probeCandidates(info, asn) {
  const list = [];
  const add = value => value && !list.includes(value) && list.push(value);
  if (!info) return ['China'];
  const cities = [CITY_EN[info.city], PROVINCE_CAPITAL[info.city], PROVINCE_CAPITAL[info.region], ...(NEARBY[info.region] || [])].filter(Boolean);
  const country = info.code && info.code !== 'CN' ? info.code : 'China';
  if (asn) cities.forEach(city => add(`${city}+AS${asn}`));
  if (asn) add(`${country}+AS${asn}`);
  cities.slice(0, 1).forEach(city => add(city));
  add(country);
  return list;
}

// 建一次 mtr；找不到合适探针（422）就换下一个位置。返回 { id, magic } 或 { error }
async function startMtr(target, candidates) {
  let last = '';
  for (const magic of candidates) {
    if (timeLeft() < 14000) return { error: '选点超时，请手填 Probe 后重试' };
    const body = JSON.stringify({
      type: 'mtr',
      target,
      locations: [{ magic, limit: 1 }],
      measurementOptions: { packets: 3, protocol: 'ICMP', ipVersion: 4 },
    });
    const res = await http('POST', GP_API, { headers: GP_HEADERS, body, timeout: 8 });
    const data = res.ok ? parseJSON(res.body) : null;
    if (res.ok && res.status === 202 && data && data.id) return { id: data.id, magic };
    if (res.ok && res.status === 429) return { error: 'Globalping 本小时的免费额度用完了' };
    last = res.ok ? `HTTP ${res.status}` : res.error;
    if (!(res.ok && res.status === 422)) break;
  }
  return { error: `Globalping 建测失败（${last || '没有合适的探针'}）` };
}

async function waitMtr(id) {
  while (timeLeft() > 12000) {
    await wait(1200);
    const res = await http('GET', `${GP_API}/${id}`, { headers: GP_HEADERS, timeout: 5 });
    const data = res.ok && res.status === 200 ? parseJSON(res.body) : null;
    if (data && data.status !== 'in-progress') {
      const first = (data.results || [])[0];
      if (!first || !first.result || first.result.status !== 'finished') return { error: '探针没有跑完这次追踪' };
      return { probe: first.probe || {}, hops: first.result.hops || [] };
    }
  }
  return { error: '追踪超时' };
}

async function trace(target, candidates) {
  const started = await startMtr(target, candidates);
  if (started.error) return started;
  return waitMtr(started.id);
}

// ───────────────────────────── 每跳 ─────────────────────────────

// 只按地址范围判断私有/共享地址；公网地址可能被云厂商内部复用，但不能仅凭位置库断言。
function isPrivate(ip) {
  const p = ip.split('.').map(Number);
  return p[0] === 10 || p[0] === 127 || (p[0] === 172 && p[1] >= 16 && p[1] <= 31) || (p[0] === 192 && p[1] === 168) || (p[0] === 100 && p[1] >= 64 && p[1] <= 127);
}

// 同时最多 6 个请求，免得超过 Surge 每个脚本 20 个并发的上限
async function lookupAll(ips) {
  const out = {};
  const queue = ips.slice();
  const worker = async () => {
    while (queue.length && timeLeft() > 2000) {
      const ip = queue.shift();
      out[ip] = await pinganInfo(ip);
    }
  };
  await Promise.all(Array.from({ length: Math.min(6, queue.length) }, worker));
  return out;
}

function flag(code) {
  if (!/^[A-Z]{2}$/.test(code)) return '';
  if (code === 'TW') return '🌏'; // 国行 iPhone 画不出 🇹🇼
  return String.fromCodePoint(...[...code].map(char => 127397 + char.charCodeAt(0)));
}

// 港澳台单独带旗帜；平安对它们有时给 CN 加「中国香港」这样的地区名
const SAR = { 香港: 'HK', 澳门: 'MO', 台湾: 'TW' };

function placeOf(info, ip) {
  if (info) {
    const names = [info.city, info.region, info.country].map(name => String(name || '').replace(/^中国(?=.)/, ''));
    const sar = names.find(name => SAR[name]);
    if (sar) return `${flag(SAR[sar])} ${sar}`;
    if (info.code === 'CN') return names[0] || names[1] || '中国';
    return [flag(info.code), names[2], names[0] && names[0] !== names[2] ? names[0] : ''].filter(Boolean).join(' ');
  }
  try {
    const code = String($utils.geoip(ip) || '').toUpperCase();
    return code ? `${flag(code)} ${code}`.trim() : '';
  } catch {
    return '';
  }
}

function asName(asn, ip) {
  try {
    return String($utils.ipaso(ip) || '').trim();
  } catch {
    return '';
  }
}

function hopASN(hop, ip) {
  const fromMtr = Array.isArray(hop.asn) ? Number(hop.asn[0]) : 0;
  if (fromMtr) return fromMtr;
  try {
    return Number($utils.ipasn(ip)) || 0;
  } catch {
    return 0;
  }
}

function maskIP(ip) {
  const parts = ip.split('.');
  return parts.length === 4 ? `${parts[0]}.${parts[1]}.••.${parts[3]}` : ip;
}

// 一段的每一跳一行；连续不回应的跳并成一行。AS 名称收集起来放到面板最后
function renderLeg(result, geo, asNames, show, endpoints) {
  const lines = [];
  let silent = [];
  const flush = () => {
    if (!silent.length) return;
    lines.push(`${silent.length > 1 ? `${silent[0]}–${silent[silent.length - 1]}` : silent[0]}  *`);
    silent = [];
  };
  result.hops.forEach((hop, index) => {
    const no = index + 1;
    const ip = String(hop.resolvedAddress || '');
    if (!isIPv4(ip)) {
      silent.push(no);
      return;
    }
    flush();
    // 用最小延迟：中间路由器对 ICMP 限速，平均值常被拉高到几百毫秒，最小值更接近这一跳的真实延迟
    const best = hop.stats && typeof hop.stats.min === 'number' ? hop.stats.min : hop.stats && hop.stats.avg;
    const avg = typeof best === 'number' ? `${Math.round(best)}ms` : '';
    if (isPrivate(ip)) {
      lines.push(`${no}  ${ip}  内网  ${avg}`.trim());
      return;
    }
    const asn = hopASN(hop, ip);
    if (asn && !asNames[asn]) asNames[asn] = asName(asn, ip);
    const shownIP = endpoints.includes(ip) ? show(ip) : ip;
    lines.push([`${no}`, shownIP, placeOf(geo[ip], ip), asn ? `AS${asn}` : '', avg].filter(Boolean).join('  '));
  });
  flush();
  return lines;
}

function probeLabel(probe) {
  return [probe.city, probe.asn ? `AS${probe.asn}` : ''].filter(Boolean).join(' ');
}

// ───────────────────────────── 入口 ─────────────────────────────

(async () => {
  const cfg = readArgs(typeof $argument === 'string' ? $argument : '');
  const show = ip => (cfg.maskIP ? maskIP(ip) : ip);
  try {
    const [local, exit] = await Promise.all([pinganInfo(), landingAndEntrance(cfg.policy)]);
    if (local && local.ip === exit.landing) throw new Error('落地 IP 就是本地出口：这次查询没有经过代理');

    const firstTarget = exit.entrance || exit.landing;
    const firstProbes = cfg.probe ? [cfg.probe] : probeCandidates(local, local ? ispASN(local.isp) : 0);
    let secondProbes = [];
    let entranceInfo = null;
    if (exit.entrance) {
      entranceInfo = await pinganInfo(exit.entrance);
      let asn = 0;
      try {
        asn = Number($utils.ipasn(exit.entrance)) || 0;
      } catch {}
      secondProbes = probeCandidates(entranceInfo, asn || (entranceInfo ? ispASN(entranceInfo.isp) : 0));
    }

    const [legA, legB] = await Promise.all([
      trace(firstTarget, firstProbes),
      exit.entrance ? trace(exit.landing, secondProbes) : Promise.resolve(null),
    ]);

    const ips = [];
    [legA, legB].forEach(leg => {
      if (!leg || leg.error) return;
      leg.hops.forEach(hop => {
        const ip = String(hop.resolvedAddress || '');
        if (isIPv4(ip) && !isPrivate(ip) && !ips.includes(ip)) ips.push(ip);
      });
    });
    const geo = await lookupAll(ips);
    const asNames = {};
    const endpoints = [exit.entrance, exit.landing].filter(Boolean);

    const lines = ['公共探针参考路径，与本机实际路径可能不同'];
    const where = info => (info ? [info.city || info.region, info.isp].filter(Boolean).join(' ') : '');
    lines.push(`本地 ${local ? `${show(local.ip)} ${where(local)}` : '没查到'}`);
    if (!exit.entrance) lines.push('未识别独立入口，仅测到落地的参考路径');
    if (exit.entrance) lines.push(`入口 ${show(exit.entrance)} ${where(entranceInfo)}`.trim());
    lines.push(`落地 ${show(exit.landing)}${exit.policy ? ` · 策略 ${exit.policy === 'DIRECT' ? '直连' : exit.policy}` : ''}`);

    const section = (title, leg) => {
      lines.push('');
      if (leg.error) {
        lines.push(`${title}：${leg.error}`);
        return;
      }
      lines.push(`${title} · 探针 ${probeLabel(leg.probe)}`);
      lines.push(...renderLeg(leg, geo, asNames, show, endpoints));
    };
    section(exit.entrance ? '① 本地附近探针 → 入口' : '本地附近探针 → 落地', legA);
    if (legB) section('② 入口附近探针 → 落地', legB);
    if (legB && !legB.error) lines.push('（第二段是公网路径，入口到落地走专线时看不到）');

    const legend = Object.keys(asNames)
      .filter(asn => asNames[asn])
      .map(asn => `AS${asn} ${asNames[asn]}`);
    if (legend.length) lines.push('', ...legend);

    const hopCount = [legA, legB].filter(leg => leg && !leg.error).reduce((sum, leg) => sum + leg.hops.length, 0);
    const failed = [legA, legB].some(leg => leg && leg.error);
    $done({
      title: `${TITLE} · ${exit.entrance ? '2 段' : '1 段'} · ${hopCount} 跳`,
      content: lines.join('\n'),
      icon: ICON,
      'icon-color': failed ? '#FF9F0A' : '#34C759',
    });
  } catch (error) {
    const message = String((error && error.message) || error).slice(0, 120);
    console.log(`路由追踪失败：${message}`);
    $done({ title: TITLE, content: message, icon: 'exclamationmark.triangle.fill', 'icon-color': ERROR_COLOR });
  }
})();
