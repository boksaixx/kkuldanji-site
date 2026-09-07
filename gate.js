/* 꿀단지. 간단 접근 게이트
   주의: 정적 사이트라 소스 보기로 우회 가능합니다. 외부인 실수 유입을 막는 문 정도로만 쓰세요.
   진짜 접근 통제가 필요하면 Vercel 프로젝트 설정의 Password Protection(유료) 또는 사내망 배포를 쓰세요. */
(function () {
  var PASS = "8080";
  var KEY = "kkuldanji_ok";
  try { if (sessionStorage.getItem(KEY) === "1") return; } catch (e) {}

  var host = document.createElement("div");
  host.id = "kkuldanji-gate";
  host.innerHTML =
    '<div class="g-wrap"><div class="g-card">' +
    '<svg class="g-bee" viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="꿀벌 비비">' +
    '<ellipse cx="78" cy="42" rx="26" ry="14" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(-25 78 42)"/>' +
    '<ellipse cx="112" cy="40" rx="22" ry="12" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(20 112 40)"/>' +
    '<ellipse cx="92" cy="76" rx="46" ry="30" fill="#FFD35C" stroke="#2B2A28" stroke-width="3"/>' +
    '<path d="M74 49 q -8 27 0 54 M96 46 q -8 30 0 60 M118 52 q -7 24 0 46" stroke="#2B2A28" stroke-width="7" fill="none" stroke-linecap="round"/>' +
    '<path d="M138 76 l 10 0" stroke="#2B2A28" stroke-width="3" stroke-linecap="round"/>' +
    '<circle cx="52" cy="72" r="5" fill="#2B2A28"/><circle cx="54" cy="70" r="1.6" fill="#fff"/>' +
    '<path d="M46 84 q 6 5 12 0" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/>' +
    '<circle cx="62" cy="86" r="4" fill="#FF9FA8" opacity=".7"/>' +
    '<path d="M60 50 q -4 -14 -14 -18 M70 47 q 2 -14 -6 -22" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/>' +
    '<circle cx="46" cy="32" r="3" fill="#2B2A28"/><circle cx="64" cy="25" r="3" fill="#2B2A28"/></svg>' +
    '<div class="g-logo">꿀단지<span>.</span></div>' +
    '<p class="g-msg">여긴 사내용이야. 비밀번호 알려주면 열어줄게 🐝</p>' +
    '<input class="g-in" id="g-in" type="password" inputmode="numeric" autocomplete="off" placeholder="비밀번호" aria-label="비밀번호">' +
    '<button class="g-btn" id="g-btn">들어가기</button>' +
    '<p class="g-err" id="g-err">음… 그거 아닌데. 다시 🐝</p>' +
    '<p class="g-note">U+ Enterprise혁신그룹 · 외부 공유 금지</p>' +
    '</div></div>';

  var css = document.createElement("style");
  css.textContent =
    '#kkuldanji-gate{position:fixed;inset:0;z-index:9999;background:#9FE0EC;' +
    'font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif}' +
    '#kkuldanji-gate .g-wrap{height:100%;display:flex;align-items:center;justify-content:center;padding:24px}' +
    '#kkuldanji-gate .g-card{background:#FFF8EC;border-radius:26px;padding:34px 28px 26px;width:100%;max-width:360px;text-align:center;box-shadow:0 14px 40px rgba(30,90,102,.18)}' +
    '#kkuldanji-gate .g-bee{width:132px;height:auto;display:block;margin:0 auto 6px}' +
    '#kkuldanji-gate .g-logo{font-size:42px;font-weight:900;letter-spacing:-.05em;color:#2B2A28;line-height:1}' +
    '#kkuldanji-gate .g-logo span{color:#FF7AB6}' +
    '#kkuldanji-gate .g-msg{font-size:15px;font-weight:600;color:#4E5968;margin:12px 0 18px;line-height:1.5}' +
    '#kkuldanji-gate .g-in{width:100%;border:2px solid #2B2A28;border-radius:14px;padding:13px 16px;font-size:17px;' +
    'font-family:inherit;text-align:center;letter-spacing:.3em;background:#fff;color:#2B2A28;outline:none}' +
    '#kkuldanji-gate .g-in::placeholder{letter-spacing:normal;color:#A39D95}' +
    '#kkuldanji-gate .g-in:focus{border-color:#FF7AB6}' +
    '#kkuldanji-gate .g-btn{width:100%;margin-top:10px;border:0;border-radius:14px;background:#2B2A28;color:#fff;' +
    'padding:13px;font-size:16px;font-weight:800;font-family:inherit;cursor:pointer}' +
    '#kkuldanji-gate .g-btn:active{transform:scale(.99)}' +
    '#kkuldanji-gate .g-err{visibility:hidden;font-size:13.5px;color:#D6336C;font-weight:700;margin:10px 0 0}' +
    '#kkuldanji-gate .g-err.show{visibility:visible}' +
    '#kkuldanji-gate .g-note{font-size:12px;color:#A39D95;margin:16px 0 0}' +
    '#kkuldanji-gate .shake{animation:kkshake .3s}' +
    '@keyframes kkshake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}';

  document.documentElement.appendChild(css);
  document.documentElement.appendChild(host);
  document.documentElement.style.overflow = "hidden";

  var input = host.querySelector("#g-in");
  var btn = host.querySelector("#g-btn");
  var err = host.querySelector("#g-err");
  var card = host.querySelector(".g-card");

  function open() {
    try { sessionStorage.setItem(KEY, "1"); } catch (e) {}
    host.remove(); css.remove();
    document.documentElement.style.overflow = "";
  }
  function tryOpen() {
    if (input.value.trim() === PASS) { open(); return; }
    err.classList.add("show");
    card.classList.remove("shake"); void card.offsetWidth; card.classList.add("shake");
    input.value = ""; input.focus();
  }
  btn.addEventListener("click", tryOpen);
  input.addEventListener("keydown", function (e) { if (e.key === "Enter") tryOpen(); });
  setTimeout(function () { input.focus(); }, 60);
})();
