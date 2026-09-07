/* 꿀단지 gate.js
   1) 첫 방문: 비밀번호 → 이름·소속팀 등록 → 입장.  재방문: 바로 입장 + "OO님 오셨어요"
   2) 회원·읽음·투표·피드백을 Supabase에 기록 (config.js에 키가 있을 때). 없으면 브라우저에만 저장.
   3) PWA: 홈 화면에 앱으로 설치 버튼. iOS는 안내 모달.
   주의: 정적 사이트라 비밀번호는 소스에서 보입니다. 외부인 실수 유입을 막는 문 정도예요. */
(function () {
  var CFG = window.KKULDANJI || {};
  var PASS = CFG.PASS || "8080";
  var KEY = "kkuldanji_member";
  var SB = CFG.SUPABASE_URL && CFG.SUPABASE_ANON_KEY ? { url: CFG.SUPABASE_URL.replace(/\/$/, ""), key: CFG.SUPABASE_ANON_KEY } : null;

  /* ---------- helpers ---------- */
  function uuid() { return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, function (c) { return (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16); }); }
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) { return null; } }
  function save(m) { try { localStorage.setItem(KEY, JSON.stringify(m)); } catch (e) {} }
  function meta(name) { var el = document.querySelector('meta[name="' + name + '"]'); return el ? el.content : ""; }
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function sb(table, row) {
    if (!SB) return Promise.resolve(null);
    return fetch(SB.url + "/rest/v1/" + table, {
      method: "POST",
      headers: { "Content-Type": "application/json", "apikey": SB.key, "Authorization": "Bearer " + SB.key, "Prefer": "return=minimal" },
      body: JSON.stringify(row)
    }).catch(function () { return null; });
  }

  function toast(html, ms) {
    var t = document.createElement("div"); t.className = "kk-toast"; t.innerHTML = html;
    document.body.appendChild(t);
    requestAnimationFrame(function () { t.classList.add("on"); });
    setTimeout(function () { t.classList.remove("on"); setTimeout(function () { t.remove(); }, 400); }, ms || 3200);
  }

  /* ---------- styles ---------- */
  var css = document.createElement("style");
  css.textContent =
    '#kk-gate{position:fixed;inset:0;z-index:9999;background:#9FE0EC;font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;overflow:auto}' +
    '#kk-gate .g-wrap{min-height:100%;display:flex;align-items:center;justify-content:center;padding:24px}' +
    '#kk-gate .g-card{background:#FFF8EC;border-radius:26px;padding:30px 26px 22px;width:100%;max-width:380px;text-align:center;box-shadow:0 14px 40px rgba(30,90,102,.18)}' +
    '#kk-gate .g-bee{width:120px;height:auto;display:block;margin:0 auto 4px}' +
    '#kk-gate .g-logo{font-size:40px;font-weight:900;letter-spacing:-.05em;color:#2B2A28;line-height:1}' +
    '#kk-gate .g-logo span{color:#FF7AB6}' +
    '#kk-gate .g-msg{font-size:15px;font-weight:600;color:#4E5968;margin:12px 0 16px;line-height:1.55}' +
    '#kk-gate .g-in,#kk-gate .g-sel{width:100%;border:2px solid #2B2A28;border-radius:14px;padding:12px 16px;font-size:16px;font-family:inherit;background:#fff;color:#2B2A28;outline:none;margin-bottom:8px;text-align:left}' +
    '#kk-gate .g-in.pw{text-align:center;letter-spacing:.3em}#kk-gate .g-in.pw::placeholder{letter-spacing:normal}' +
    '#kk-gate .g-in:focus,#kk-gate .g-sel:focus{border-color:#FF7AB6}' +
    '#kk-gate .g-sel{-webkit-appearance:none;appearance:none;background-image:linear-gradient(45deg,transparent 50%,#2B2A28 50%),linear-gradient(135deg,#2B2A28 50%,transparent 50%);background-position:calc(100% - 22px) 50%,calc(100% - 16px) 50%;background-size:6px 6px;background-repeat:no-repeat}' +
    '#kk-gate .g-btn{width:100%;margin-top:6px;border:0;border-radius:14px;background:#2B2A28;color:#fff;padding:13px;font-size:16px;font-weight:800;font-family:inherit;cursor:pointer}' +
    '#kk-gate .g-btn.sec{background:transparent;color:#2B2A28;border:2px solid #2B2A28;margin-top:8px}' +
    '#kk-gate .g-err{visibility:hidden;font-size:13.5px;color:#D6336C;font-weight:700;margin:8px 0 0}#kk-gate .g-err.show{visibility:visible}' +
    '#kk-gate .g-note{font-size:12px;color:#A39D95;margin:14px 0 0;line-height:1.5}' +
    '#kk-gate .shake{animation:kkshake .3s}@keyframes kkshake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}' +
    '#kk-gate .g-privacy{font-size:12px;color:#7A7570;text-align:left;background:#fff;border-radius:12px;padding:10px 12px;margin:4px 0 10px;line-height:1.55}' +
    '.kk-toast{position:fixed;left:50%;top:18px;transform:translate(-50%,-30px);opacity:0;background:#2B2A28;color:#fff;border-radius:999px;padding:11px 18px;font-size:14.5px;font-weight:700;z-index:9998;transition:.35s;box-shadow:0 8px 24px rgba(0,0,0,.18);font-family:"Pretendard Variable",Pretendard,sans-serif;max-width:92vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
    '.kk-toast.on{transform:translate(-50%,0);opacity:1}' +
    '.kk-install{position:fixed;left:12px;right:12px;bottom:14px;z-index:9997;background:#2B2A28;color:#fff;border-radius:18px;padding:12px 14px 12px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 10px 30px rgba(0,0,0,.22);font-family:"Pretendard Variable",Pretendard,sans-serif;max-width:600px;margin:0 auto}' +
    '.kk-install .t{flex:1;font-size:14px;line-height:1.45}.kk-install .t b{display:block;font-size:15px}' +
    '.kk-install button{border:0;border-radius:999px;padding:9px 14px;font-size:14px;font-weight:800;font-family:inherit;cursor:pointer;background:#FFD35C;color:#2B2A28;white-space:nowrap}' +
    '.kk-install .x{background:transparent;color:#9AA4B2;padding:6px 8px;font-size:18px;line-height:1}' +
    '.kk-modal{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.45);display:flex;align-items:flex-end;justify-content:center;font-family:"Pretendard Variable",Pretendard,sans-serif}' +
    '.kk-modal .m{background:#FFF8EC;border-radius:24px 24px 0 0;padding:24px 22px 30px;width:100%;max-width:600px}' +
    '.kk-modal h3{font-size:19px;font-weight:900;margin-bottom:12px}.kk-modal ol{padding-left:20px;font-size:15px;line-height:1.8;color:#4E5968}' +
    '.kk-modal button{width:100%;margin-top:16px;border:0;border-radius:14px;background:#2B2A28;color:#fff;padding:13px;font-size:15px;font-weight:800;font-family:inherit;cursor:pointer}' +
    '.vote a.voted{background:#2B2A28;color:#fff}.vote a.dim{opacity:.35;pointer-events:none}';
  document.documentElement.appendChild(css);

  var BEE = '<svg class="g-bee" viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="꿀벌 비비"><ellipse cx="78" cy="42" rx="26" ry="14" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(-25 78 42)"/><ellipse cx="112" cy="40" rx="22" ry="12" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(20 112 40)"/><ellipse cx="92" cy="76" rx="46" ry="30" fill="#FFD35C" stroke="#2B2A28" stroke-width="3"/><path d="M74 49 q -8 27 0 54 M96 46 q -8 30 0 60 M118 52 q -7 24 0 46" stroke="#2B2A28" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M138 76 l 10 0" stroke="#2B2A28" stroke-width="3" stroke-linecap="round"/><circle cx="52" cy="72" r="5" fill="#2B2A28"/><circle cx="54" cy="70" r="1.6" fill="#fff"/><path d="M46 84 q 6 5 12 0" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="62" cy="86" r="4" fill="#FF9FA8" opacity=".7"/><path d="M60 50 q -4 -14 -14 -18 M70 47 q 2 -14 -6 -22" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="46" cy="32" r="3" fill="#2B2A28"/><circle cx="64" cy="25" r="3" fill="#2B2A28"/></svg>';

  /* ---------- PWA install ---------- */
  var deferredPrompt = null;
  var isStandalone = window.matchMedia("(display-mode: standalone)").matches || window.navigator.standalone === true;
  var isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
  window.addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); deferredPrompt = e; });
  if ("serviceWorker" in navigator) { window.addEventListener("load", function () { navigator.serviceWorker.register("/sw.js").catch(function () {}); }); }

  function iosGuide() {
    var m = document.createElement("div"); m.className = "kk-modal";
    m.innerHTML = '<div class="m"><h3>📲 아이폰에서 앱으로 설치하기</h3><ol><li>사파리 하단 <b>공유</b> 버튼(네모에 화살표) 누르기</li><li>아래로 내려서 <b>홈 화면에 추가</b> 선택</li><li>오른쪽 위 <b>추가</b> 누르면 끝</li></ol><p style="font-size:13px;color:#7A7570;margin-top:10px">홈 화면에 꿀단지 아이콘이 생기고, 앱처럼 열려요. 크롬 말고 <b>사파리</b>에서 해야 해요.</p><button>알겠어요</button></div>';
    m.querySelector("button").onclick = function () { m.remove(); };
    m.addEventListener("click", function (e) { if (e.target === m) m.remove(); });
    document.body.appendChild(m);
  }
  function install() {
    if (deferredPrompt) { deferredPrompt.prompt(); deferredPrompt.userChoice.then(function (r) { if (r.outcome === "accepted") { toast("📲 설치됐어요. 홈 화면에서 만나요 🐝"); hideBanner(); } deferredPrompt = null; }); }
    else if (isIOS) iosGuide();
    else toast("브라우저 메뉴(⋮)에서 '앱 설치' 또는 '홈 화면에 추가'를 눌러주세요", 4200);
  }
  window.kkInstall = install;
  var banner = null;
  function hideBanner() { if (banner) { banner.remove(); banner = null; } try { localStorage.setItem("kk_install_dismiss", String(Date.now())); } catch (e) {} }
  function showBanner() {
    if (isStandalone || banner) return;
    var d = 0; try { d = +localStorage.getItem("kk_install_dismiss") || 0; } catch (e) {}
    if (Date.now() - d < 1000 * 60 * 60 * 24 * 7) return;
    banner = document.createElement("div"); banner.className = "kk-install";
    banner.innerHTML = '<div class="t"><b>📲 앱으로 설치하면 편해요</b>홈 화면에서 바로 열려요. 메일 링크 안 찾아도 돼요.</div><button class="go">설치</button><button class="x" aria-label="닫기">×</button>';
    banner.querySelector(".go").onclick = install;
    banner.querySelector(".x").onclick = hideBanner;
    document.body.appendChild(banner);
  }

  /* ---------- votes & feedback ---------- */
  function wireVotes(member) {
    var issue = meta("issue") || "";
    var links = document.querySelectorAll(".vote a");
    if (!links.length) return;
    var voted = ""; try { voted = localStorage.getItem("kk_vote_" + issue) || ""; } catch (e) {}
    links.forEach(function (a) {
      var choice = a.textContent.trim();
      if (voted) { a.classList.add(choice === voted ? "voted" : "dim"); }
      a.addEventListener("click", function (e) {
        e.preventDefault(); if (voted) return;
        var isDelete = /지워도/.test(choice); var reason = "";
        if (isDelete) { reason = prompt("알겠어요. 이유 한 줄만 남겨주세요 🐝"); if (reason === null) return; }
        voted = choice; try { localStorage.setItem("kk_vote_" + issue, choice); } catch (x) {}
        links.forEach(function (b) { b.classList.add(b === a ? "voted" : "dim"); });
        sb(isDelete ? "feedback" : "votes", { member_id: member.id, name: member.name, team: member.team, issue_no: issue ? +issue : null, choice: choice, reason: reason || null });
        toast(isDelete ? "알겠어요. 비비가 반성할게요 🐝" : "고마워요! 다음 호에 반영할게요 🐝");
      });
    });
  }

  /* ---------- entry ---------- */
  function enter(member, isNew) {
    var g = document.getElementById("kk-gate"); if (g) g.remove();
    document.documentElement.style.overflow = "";
    var issue = meta("issue") || "";
    sb("reads", { member_id: member.id, name: member.name, team: member.team, issue_no: issue ? +issue : null, path: location.pathname, is_new: !!isNew });
    toast(isNew ? "🐝 " + esc(member.name) + "님, 환영해요! 꿀단지에 처음 오셨네요" : "🐝 " + esc(member.name) + "님 오셨어요", isNew ? 4000 : 2800);
    setTimeout(showBanner, isNew ? 1800 : 6000);
    wireVotes(member);
  }

  var m = load();
  if (m && m.id && m.name) {
    if (document.body) enter(m, false); else document.addEventListener("DOMContentLoaded", function () { enter(m, false); });
    return;
  }

  /* ---------- gate UI (password → register) ---------- */
  var host = document.createElement("div"); host.id = "kk-gate";
  var teams = (CFG.TEAMS || ["기타"]).map(function (t) { return '<option value="' + esc(t) + '">' + esc(t) + "</option>"; }).join("");
  host.innerHTML =
    '<div class="g-wrap"><div class="g-card">' + BEE + '<div class="g-logo">꿀단지<span>.</span></div>' +
    '<div id="kk-step1"><p class="g-msg">여긴 사내용이야. 비밀번호 알려주면 열어줄게 🐝</p>' +
    '<input class="g-in pw" id="kk-pw" type="password" inputmode="numeric" autocomplete="off" placeholder="비밀번호" aria-label="비밀번호">' +
    '<button class="g-btn" id="kk-pwbtn">들어가기</button><p class="g-err" id="kk-pwerr">음… 그거 아닌데. 다시 🐝</p></div>' +
    '<div id="kk-step2" style="display:none"><p class="g-msg">처음 오셨네요! 누구신지만 알려주세요.<br>다음부턴 안 물어봐요 🐝</p>' +
    '<input class="g-in" id="kk-name" type="text" autocomplete="name" placeholder="이름 (예: 김민지)" maxlength="20" aria-label="이름">' +
    '<select class="g-sel" id="kk-team" aria-label="소속팀"><option value="">소속팀 선택</option>' + teams + '</select>' +
    '<div class="g-privacy">이름과 소속팀은 <b>누가 읽었는지</b> 알기 위해서만 써요. 어느 호를 읽었고 뭘 투표했는지가 같이 기록돼요. 그 외 용도로는 안 씁니다.</div>' +
    '<button class="g-btn" id="kk-regbtn">등록하고 들어가기</button><p class="g-err" id="kk-regerr">이름이랑 팀, 둘 다 필요해요 🐝</p></div>' +
    (isStandalone ? "" : '<button class="g-btn sec" id="kk-inst">📲 앱으로 설치하기</button>') +
    '<p class="g-note">U+ Enterprise혁신그룹 · 외부 공유 금지</p></div></div>';

  function mount() {
    document.documentElement.appendChild(host);
    document.documentElement.style.overflow = "hidden";
    var card = host.querySelector(".g-card");
    var pw = host.querySelector("#kk-pw"), pwerr = host.querySelector("#kk-pwerr");
    var s1 = host.querySelector("#kk-step1"), s2 = host.querySelector("#kk-step2");
    var name = host.querySelector("#kk-name"), team = host.querySelector("#kk-team"), regerr = host.querySelector("#kk-regerr");
    function shake() { card.classList.remove("shake"); void card.offsetWidth; card.classList.add("shake"); }
    function tryPw() {
      if (pw.value.trim() === PASS) { s1.style.display = "none"; s2.style.display = "block"; setTimeout(function () { name.focus(); }, 60); return; }
      pwerr.classList.add("show"); shake(); pw.value = ""; pw.focus();
    }
    function tryReg() {
      var n = name.value.trim(), t = team.value;
      if (n.length < 2 || !t) { regerr.classList.add("show"); shake(); return; }
      var mem = { id: uuid(), name: n, team: t, device: navigator.userAgent.slice(0, 80), joined: new Date().toISOString() };
      save(mem);
      sb("members", { id: mem.id, name: n, team: t, device: mem.device });
      enter(mem, true);
    }
    host.querySelector("#kk-pwbtn").onclick = tryPw;
    pw.addEventListener("keydown", function (e) { if (e.key === "Enter") tryPw(); });
    host.querySelector("#kk-regbtn").onclick = tryReg;
    name.addEventListener("keydown", function (e) { if (e.key === "Enter") tryReg(); });
    var inst = host.querySelector("#kk-inst"); if (inst) inst.onclick = install;
    setTimeout(function () { pw.focus(); }, 60);
  }
  if (document.body) mount(); else document.addEventListener("DOMContentLoaded", mount);
})();
