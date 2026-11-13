/**
 * Reddit 自动翻译（Surge http-request 脚本）
 *
 * 给 Reddit App 的 GraphQL 请求加上 x-reddit-translations 请求头，打开 App 自带的翻译。
 *
 * 基于 RavelloH 的 gist 68ed0626dae69a1ce7c8ad6887087ea1 中的 main.js 改写
 * （上游提交 c008127260bc，sha256 1d3ea8c1046be208…，2026-11-11），经 fmz200/wool_scripts 的
 * RedditTranslation.module 引用。版权归原作者，不适用本仓库的 MIT 许可证。
 *
 * 相对上游的改动：
 *   - 目标语言改为模块参数 Lang，默认 zh-hans（简体），可填 zh-hant（繁体）等
 *   - 删除旧请求头时不区分大小写（上游只删两种写法）
 */

const DEFAULT_LANG = 'zh-hans';

function readLang(argument) {
  const text = String(argument || '').trim().replace(/^["']|["']$/g, '');
  const value = ((text.match(/(?:^|&)Lang=([^&]*)/i) || [])[1] || '').trim();
  return /^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$/.test(value) ? value.toLowerCase() : DEFAULT_LANG;
}

(function () {
  if (typeof $request === 'undefined' || !/^https?:\/\/gql(-fed)?\.reddit\.com(?::\d+)?(?:[/?#]|$)/i.test(String($request.url || ''))) return $done({});
  const headers = { ...$request.headers };
  Object.keys(headers)
    .filter(name => name.toLowerCase() === 'x-reddit-translations')
    .forEach(name => delete headers[name]);
  headers['x-reddit-translations'] = `enabled, seo, ${readLang(typeof $argument === 'undefined' ? '' : $argument)}`;
  $done({ headers });
})();
