/**
 * t.me 链接跳转到 Telegram 客户端（Surge http-request 脚本，直接返回 302）
 *
 * 基于 Yu9191/Rewrite 的 TgRedirect.js 改写（上游 sha256 b1cc4e493b988393…，2026-11-11）。
 * 版权归原作者，不适用本仓库的 MIT 许可证。
 *
 * 相对上游的改动：
 *   - 保留链接里的查询参数：机器人的 ?start=、小程序的 ?startapp=、评论 ?comment=、话题 ?thread= 等
 *     上游都会丢掉，点开只到对话首页
 *   - 补上上游没处理的链接：私有频道消息 t.me/c/…、话题里的消息、动态、小程序、分组文件夹 addlist、
 *     表情包 addemoji、代理 proxy / socks、主题、壁纸、语言包、账单、助推、手机号 t.me/+86… 等
 *   - 不认识的路径（t.me/iv 即时预览、不像用户名的短路径）原样放行，不再硬转成 resolve
 *   - 只转浏览器的页面访问（GET 且 Accept 含 text/html）；应用抓链接预览、脚本和接口请求不受影响
 *   - 只支持 Surge，去掉 Quantumult X 分支
 *
 * 参数：client=Telegram / Swiftgram / Turrit / iMe / Nicegram / Lingogram，
 *       或直接写 scheme：tg / sg / turrit / ime / ng / lingo（也可以只写值，不带 client=）
 */

const CLIENTS = { telegram: 'tg', swiftgram: 'sg', turrit: 'turrit', ime: 'ime', nicegram: 'ng', lingogram: 'lingo' };

// 第一段是这些词时，后面一段是它的参数：t.me/addlist/<slug> → scheme://addlist?slug=<slug>
const WITH_VALUE = {
  joinchat: ['join', 'invite'],
  addstickers: ['addstickers', 'set'],
  addemoji: ['addemoji', 'set'],
  addlist: ['addlist', 'slug'],
  addtheme: ['addtheme', 'slug'],
  bg: ['bg', 'slug'],
  setlanguage: ['setlanguage', 'lang'],
  login: ['login', 'code'],
  invoice: ['invoice', 'slug'],
  giftcode: ['giftcode', 'slug'],
  m: ['message', 'slug'],
  contact: ['contact', 'token'],
  nft: ['nft', 'slug'],
};

// 这些词的参数都在查询串里，原样带过去：t.me/proxy?server=… → scheme://proxy?server=…
const QUERY_ONLY = ['proxy', 'socks', 'confirmphone'];

function readScheme(argument) {
  let text = String(argument || '').trim().replace(/^["']|["']$/g, '');
  const named = text.match(/(?:^|&)client=([^&]*)/i);
  if (named) text = named[1];
  else if (text.includes('=')) text = '';
  text = text.trim().replace(/^["']|["']$/g, '');
  if (/^\{\{\{.*\}\}\}$/.test(text)) text = '';
  const name = text.toLowerCase();
  if (Object.prototype.hasOwnProperty.call(CLIENTS, name)) return CLIENTS[name];
  return ['tg', 'sg', 'turrit', 'ime', 'ng', 'lingo'].includes(name) ? name : 'tg';
}

function decode(text) {
  try {
    return decodeURIComponent(text);
  } catch {
    return text;
  }
}

// 把 t.me 后面的路径和查询串换成客户端链接里 scheme:// 之后的部分；不认识的返回空串
function convert(path, query) {
  const segs = path.split('/').filter(Boolean).map(decode);
  if (segs[0] === 's' && segs[1]) segs.shift(); // t.me/s/<频道> 是网页预览，按频道处理
  const [first, second, third, fourth] = segs;
  if (!first || segs.some(seg => /[\u0000-\u001f\u007f/]/.test(seg))) return '';

  const isNumber = value => /^\d+$/.test(value || '');
  const make = (host, params) => {
    const own = Object.keys(params).map(key => `${key}=${encodeURIComponent(params[key])}`);
    // 路径已确定的目标字段优先，避免查询串再次指定 domain/post 等改变目标。
    const extra = query.split('&').filter(part => part && !Object.prototype.hasOwnProperty.call(params, decode(part.split('=')[0])));
    return `${host}?${own.concat(extra).join('&')}`;
  };

  if (first[0] === '+') {
    const rest = first.slice(1);
    if (!rest) return '';
    return /^\d{5,}$/.test(rest) ? make('resolve', { phone: rest }) : make('join', { invite: rest });
  }
  if (first[0] === '$') return first.length > 1 ? make('invoice', { slug: first.slice(1) }) : '';

  const key = first.toLowerCase();
  if (Object.prototype.hasOwnProperty.call(WITH_VALUE, key)) return second ? make(WITH_VALUE[key][0], { [WITH_VALUE[key][1]]: second }) : '';
  if (QUERY_ONLY.includes(key)) return query ? make(key, {}) : '';
  if (key === 'share') return /(?:^|&)url=/.test(query) ? make('msg_url', {}) : '';
  if (key === 'boost') {
    if (second) return make('boost', { domain: second });
    const channel = (query.match(/(?:^|&)c=(\d+)/) || [])[1];
    return channel ? `boost?channel=${channel}` : '';
  }
  if (key === 'c') {
    if (!isNumber(second)) return '';
    if (isNumber(third) && isNumber(fourth)) return make('privatepost', { channel: second, thread: third, post: fourth });
    if (isNumber(third)) return make('privatepost', { channel: second, post: third });
    return make('privatepost', { channel: second });
  }

  // 剩下的按用户名处理。用户名是字母开头、4 到 32 位的字母数字下划线；不像用户名的（iv、dl 等）放行
  if (!/^[A-Za-z][A-Za-z0-9_]{3,31}$/.test(first)) return '';
  if (!second) return make('resolve', { domain: first });
  if (second === 's' && isNumber(third)) return make('resolve', { domain: first, story: third });
  if (isNumber(second) && isNumber(third)) return make('resolve', { domain: first, thread: second, post: third });
  if (isNumber(second)) return make('resolve', { domain: first, post: second });
  return make('resolve', { domain: first, appname: second });
}

function isPageVisit(request) {
  if (String(request.method || 'GET').toUpperCase() !== 'GET') return false;
  const headers = request.headers || {};
  const name = Object.keys(headers).find(key => key.toLowerCase() === 'accept');
  return !name || String(headers[name]).includes('text/html');
}

(function () {
  if (typeof $request === 'undefined' || !$request.url || !isPageVisit($request)) return $done({});
  const match = String($request.url).match(/^https?:\/\/t\.me\/([^?#]+)(?:\?([^#]*))?/i);
  const target = match ? convert(match[1], match[2] || '') : '';
  if (!target) return $done({});
  const scheme = readScheme(typeof $argument === 'undefined' ? '' : $argument);
  $done({ response: { status: 302, headers: { Location: `${scheme}://${target}` }, body: '' } });
})();
