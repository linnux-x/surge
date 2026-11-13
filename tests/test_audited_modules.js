// node tests/test_audited_modules.js — synthetic data only; never makes network requests.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const crypto = require('node:crypto');
const load = name => fs.readFileSync(path.join(__dirname, '../Module', name), 'utf8');

async function execute(name, input = {}, respond = () => { throw new Error('Unexpected HTTP request'); }) {
  const notices = [], logs = [], calls = [], storage = { ...(input.storage || {}) };
  let completed = 0, complete;
  const result = new Promise(resolve => { complete = resolve; });
  const request = (opts, cb) => { calls.push(opts); respond(opts, cb, calls.length); };
  const context = {
    console: { log: (...args) => logs.push(args.join(' ')) },
    setTimeout: (fn, ms) => setTimeout(fn, Math.min(ms, 5)), clearTimeout,
    $environment: { 'surge-version': '6.11.0' },
    $persistentStore: { read: k => storage[k] || null, write: (v, k) => { storage[k] = v; return true; } },
    $notification: { post: (...args) => notices.push(args) },
    $httpClient: { get: request, post: request },
    $done: value => { completed++; complete(value); },
    ...input,
  };
  delete context.storage;
  vm.runInNewContext(load(name), context, { timeout: 1000 });
  let watchdog;
  const output = await Promise.race([result, new Promise((_, reject) => { watchdog = setTimeout(() => reject(new Error(name + ' did not finish')), 1000); })]).finally(() => clearTimeout(watchdog));
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(completed, 1, name + ' must call $done once');
  return { output, context, calls, storage, notices, logs };
}
const htmlRequest = url => ({ url, method: 'GET', headers: { Accept: 'text/html' } });
async function telegram() {
  const cases = [
    ['https://t.me/samplebot?start=abc', 'tg://resolve?domain=samplebot&start=abc'],
    ['https://t.me/samplebot?domain=other&start=abc', 'tg://resolve?domain=samplebot&start=abc'],
    ['https://t.me/channel/10?post=20&comment=3', 'tg://resolve?domain=channel&post=10&comment=3'],
    ['https://t.me/c/123/5/9', 'tg://privatepost?channel=123&thread=5&post=9'],
    ['https://t.me/s/channel/8', 'tg://resolve?domain=channel&post=8'],
    ['https://t.me/joinchat/abcd', 'tg://join?invite=abcd'],
    ['https://t.me/constructor', 'tg://resolve?domain=constructor'],
    ['https://t.me/addlist/folder', 'tg://addlist?slug=folder'],
    ['https://t.me/botname/app?startapp=x', 'tg://resolve?domain=botname&appname=app&startapp=x'],
    ['https://t.me/proxy?server=example.com&port=443', 'tg://proxy?server=example.com&port=443'],
  ];
  for (const [url, expected] of cases) {
    const r = await execute('TgRedirect.js', { $request: htmlRequest(url) });
    assert.equal(r.output.response.headers.Location, expected);
  }
  for (const url of ['https://t.me.evil.example/channel', 'https://t.me/iv?url=foo', 'https://t.me/%00channel']) {
    assert.equal(Object.keys((await execute('TgRedirect.js', { $request: htmlRequest(url) })).output).length, 0);
  }
  const fallback = await execute('TgRedirect.js', { $argument: 'client=javascript', $request: htmlRequest('https://t.me/channel') });
  assert.match(fallback.output.response.headers.Location, /^tg:/);
  const swift = await execute('TgRedirect.js', { $argument: 'client=Swiftgram', $request: htmlRequest('https://t.me/channel') });
  assert.match(swift.output.response.headers.Location, /^sg:/);
  const post = await execute('TgRedirect.js', { $request: { ...htmlRequest('https://t.me/channel'), method: 'POST' } });
  assert.equal(Object.keys(post.output).length, 0);
}
async function reddit() {
  const headers = { 'X-REDDIT-TRANSLATIONS': 'old', 'x-reddit-translations': 'old2', Authorization: 'synthetic' };
  const r = await execute('RedditTranslation.js', { $request: { url: 'https://gql-fed.reddit.com/', headers }, $argument: 'Lang=zh-hant' });
  assert.equal(r.output.headers['x-reddit-translations'], 'enabled, seo, zh-hant');
  assert.equal(Object.keys(r.output.headers).filter(k => k.toLowerCase() === 'x-reddit-translations').length, 1);
  assert.equal(r.output.headers.Authorization, 'synthetic');
  assert.equal(headers['X-REDDIT-TRANSLATIONS'], 'old');
  for (const url of ['https://gql.reddit.com.evil.example/', 'https://example.com/']) {
    const other = await execute('RedditTranslation.js', { $request: { url, headers } });
    assert.equal(Object.keys(other.output).length, 0);
  }
  const fallback = await execute('RedditTranslation.js', { $request: { url: 'https://gql.reddit.com/' }, $argument: 'Lang=\r\ninjected' });
  assert.equal(fallback.output.headers['x-reddit-translations'], 'enabled, seo, zh-hans');
}
const cookie = 'c_mmbDevId=dev%2Btest&credential=fake%3Dvalue';
const jd = { url: 'https://in.m.jd.com/product/graphext/123.html', headers: {} };
async function prices() {
  const capture = await execute('jd_price.js', { $request: { url: 'https://apapia-sqk-weblogic.manmanbuy.com/baoliao/center/menu', body: cookie } });
  assert.equal(capture.storage.manmanbuy_val, cookie);
  assert.ok(!JSON.stringify([...capture.notices, ...capture.logs]).includes('fake'));
  const invalid = await execute('jd_price.js', { $request: { url: 'https://apapia-sqk-weblogic.manmanbuy.com/baoliao/center/menu', body: '' }, storage: { manmanbuy_val: cookie } });
  assert.equal(invalid.storage.manmanbuy_val, cookie);
  const fixtures = [
    { ok: 1, result: { url: 'https://item.jd.com/123.html', spbh: 'abc' } },
    { ok: 1, result: { trend: 'synthetic' } },
    { ok: 1, remark: { ListPriceDetail: [{ Name: '历史最低价', Price: '<script>alert(1)</script>', Date: '2026-01-01', Difference: 2 }] } },
  ];
  const r = await execute('jd_price.js', { $request: jd, $response: { body: '<HTML><BODY class="page">original</BODY></HTML>' }, storage: { manmanbuy_val: cookie } }, (opts, cb, i) => cb(null, { status: 200 }, JSON.stringify(fixtures[i - 1])));
  assert.equal(r.calls.length, 3);
  assert.match(r.output.body, /&lt;script&gt;/);
  assert.match(r.output.body, /<BODY class="page"><div/);
  for (const opts of r.calls) {
    const params = Object.fromEntries(new URLSearchParams(opts.body));
    const canonical = Object.keys(params).filter(k => params[k] !== '' && k.toLowerCase() !== 'token').sort().map(k => k.toUpperCase() + params[k].toUpperCase()).join('');
    const key = '3E41D1331F5DDAFCD0A38FE2D52FF66F';
    assert.equal(params.token, crypto.createHash('md5').update(encodeURIComponent(key + canonical + key)).digest('hex').toUpperCase());
    assert.equal(params.credential, 'fake=value');
    assert.equal(params.c_mmbDevId, 'dev+test');
  }
  vm.runInNewContext('intCryptoJS(); if(md5("abc") !== "900150983cd24fb0d6963f7d28e17f72") throw new Error("MD5 mismatch");', r.context);
  const v2 = await execute('jd_price.js', { $request: jd, $response: { body: '<body>original</body>' }, storage: { manmanbuy_val: cookie, mmb_v: 'V2' } },
    (opts, cb, i) => cb(null, { status: 200 }, JSON.stringify(i === 1 ? { ok: 1, result: { link: 'https://item.jd.com/123.html', stteId: 'synthetic' } } : fixtures[i - 2])));
  assert.equal(v2.calls.length, 4);
  assert.equal(new URLSearchParams(v2.calls[1].body).get('stteId'), 'synthetic');
  for (const [status, body] of [[500, '{}'], [200, 'not json'], [200, '{"ok":1}']]) {
    const fail = await execute('jd_price.js', { $request: jd, $response: { body: '<body>original</body>' }, storage: { manmanbuy_val: cookie } }, (opts, cb) => cb(null, { status }, body));
    assert.match(fail.output.body, /original/);
    assert.ok(!fail.output.body.includes('undefined'));
  }
  const timed = await execute('jd_price.js', { $request: jd, $response: { body: '<body>original</body>' }, storage: { manmanbuy_val: cookie } }, () => {});
  assert.match(timed.output.body, /超时/);
}
async function firewall() {
  const config = { $argument: 'tokens=pgnfw_synthetic@0' };
  const reply = { enabled: true, currentIp: '192.0.2.3', limit: 5, whitelist: [{ ip: '192.0.2.0/24', slot: 0 }] };
  const r = await execute('po0-firewall-whitelist.js', config, (opts, cb) => cb(null, { status: 200 }, JSON.stringify(reply)));
  assert.match(r.output.title, /1\/1/);
  assert.equal(r.calls[0].policy, 'DIRECT');
  assert.equal(r.calls[0]['auto-redirect'], false);
  assert.match(r.calls[0].url, /slot=0$/);
  for (const token of ['pgnfw_synthetic@-1', 'pgnfw_synthetic@2abc', 'pgnfw_synthetic@']) {
    const invalid = await execute('po0-firewall-whitelist.js', { $argument: 'tokens=' + token });
    assert.equal(invalid.calls.length, 0);
    assert.match(invalid.output.content, /格式无效/);
  }
  const malformed = await execute('po0-firewall-whitelist.js', { $argument: 'tokens=%broken', storage: { po0fw_tokens: 'pgnfw_synthetic' } });
  assert.equal(malformed.calls.length, 0);
  const notOK = await execute('po0-firewall-whitelist.js', config, (opts, cb) => cb(null, { status: 401 }, JSON.stringify(reply)));
  assert.match(notOK.output.content, /HTTP 401/);
  assert.equal(notOK.calls.length, 1);
  const retry = await execute('po0-firewall-whitelist.js', config, (opts, cb) => cb('failed https://example.com/pgnfw_synthetic/add'));
  assert.equal(retry.calls.length, 3);
  assert.ok(!JSON.stringify([retry.output, retry.notices]).includes('pgnfw_synthetic'));
}
(async () => {
  await telegram(); await reddit(); await prices(); await firewall();
  process.stdout.write('Audited modules: Telegram, Reddit, JD signatures/HTML/errors, po0 routing/slots/errors passed\n');
})().catch(error => { console.error(error); process.exitCode = 1; });
