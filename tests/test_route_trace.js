// Run with: node tests/test_route_trace.js (no network, no Surge required).
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../Module/route-trace.js'), 'utf8');

async function run(mode) {
  const calls = [];
  let starts = 0;
  let finish;
  const done = new Promise(resolve => { finish = resolve; });
  const context = {
    console: { log() {} },
    setTimeout: (fn) => { queueMicrotask(fn); return 1; },
    $argument: 'MaskIP=true&Probe=Nanjing+AS4134&Proxy=A&B=C',
    $httpAPI: (method, url, body, cb) => cb({ requests: [{
      URL: 'https://my.ippure.com/v1/info', policyName: 'A&B=C', remoteAddress: '203.0.113.9 (Proxy)',
    }] }),
    $utils: { ipasn: () => 4134, ipaso: () => 'Example network', geoip: () => 'CN' },
    $done: value => finish(value),
  };
  function request(options, cb) {
    calls.push(options);
    let status = 200, body;
    const host = new URL(options.url).hostname;
    if (host === 'my.ippure.com') {
      body = { ip: mode === 'direct' ? '192.0.2.3' : mode === 'ipv6' ? '2001:db8::1' : '198.51.100.7' };
    } else if (host === 'rmb.pingan.com.cn') {
      body = { data: { ip: '192.0.2.3', countryIsoCode: 'CN', country: '中国', region: '江苏省', city: '南京市', isp: '电信' } };
    } else if (options.body) {
      starts++;
      if (mode === 'limited') { status = 429; body = {}; }
      else { status = 202; body = { id: String(starts) }; }
    } else {
      body = { status: 'finished', results: [{ probe: { city: 'Nanjing', asn: 4134 }, result: { status: 'finished', hops: [
        { resolvedAddress: null }, { resolvedAddress: null },
        { resolvedAddress: '11.0.0.1', asn: [749], stats: { min: 4, avg: 500 } },
        { resolvedAddress: '198.51.100.7', asn: [4134], stats: { min: 20 } },
      ] } }] };
    }
    cb(null, { status }, JSON.stringify(body));
  }
  context.$httpClient = { get: request, post: request };
  vm.runInNewContext(source, context);
  const result = await done;
  return { result, calls };
}

(async () => {
  const helpers = source.slice(0, source.lastIndexOf('(async () => {'));
  vm.runInNewContext(helpers + `
    assert.equal(isPrivate('11.0.0.1'), false);
    assert.equal(isPrivate('9.0.0.1'), false);
    assert.equal(isPrivate('172.20.0.1'), true);
    assert.equal(isIPv4('999.1.2.3'), false);
    assert.equal(readArgs('MaskIP=false&Probe=自动&Proxy=A&B=C').policy, 'A&B=C');
    assert.equal(placeOf({code:'CN',city:'',region:'中国香港',country:'中国'}, '203.0.113.1'), '🇭🇰 香港');
  `, { assert });
  const normal = await run('normal');
  assert.match(normal.result.content, /公共探针参考路径/);
  assert.match(normal.result.content, /1–2  \*/);
  assert.match(normal.result.content, /11\.0\.0\.1.*4ms/);
  assert.ok(!normal.result.content.includes('198.51.100.7'));
  assert.match(normal.result.content, /198\.51\.••\.7/);
  assert.equal(normal.calls.filter(c => c.body).length, 2);
  assert.ok(normal.calls.filter(c => c.body).every(c => !('ipVersion' in JSON.parse(c.body).measurementOptions)));
  for (const [mode, message] of [['direct', /没有经过代理/], ['ipv6', /暂只支持 IPv4/]]) {
    const outcome = await run(mode);
    assert.match(outcome.result.content, message);
    assert.equal(outcome.calls.filter(c => c.body).length, 0);
  }
  assert.match((await run('limited')).result.content, /免费额度用完/);
  process.stdout.write('RouteTrace: address classification, masking, routing, API errors and direct/IPv6 checks passed\n');
})().catch(error => { console.error(error); process.exitCode = 1; });
