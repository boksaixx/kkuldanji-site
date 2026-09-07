#!/usr/bin/env python3
"""issues.json을 읽어 index.html 생성. 새 호는 issues.json에 항목 추가 후 이 스크립트 실행."""
import json, pathlib
root = pathlib.Path(__file__).parent
issues = json.loads((root / "issues.json").read_text(encoding="utf-8"))
issues.sort(key=lambda x: x["no"], reverse=True)

FIELDS = [("전체", "all"), ("유선", "유선"), ("무선", "무선"),
          ("SMB", "SMB"), ("모빌리티", "모빌리티"), ("보안", "보안"), ("AI", "AI")]
BEE = '<svg class="bee" viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="꿀벌 비비"><ellipse cx="78" cy="42" rx="26" ry="14" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(-25 78 42)"/><ellipse cx="112" cy="40" rx="22" ry="12" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(20 112 40)"/><ellipse cx="92" cy="76" rx="46" ry="30" fill="#FFD35C" stroke="#2B2A28" stroke-width="3"/><path d="M74 49 q -8 27 0 54 M96 46 q -8 30 0 60 M118 52 q -7 24 0 46" stroke="#2B2A28" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M138 76 l 10 0" stroke="#2B2A28" stroke-width="3" stroke-linecap="round"/><circle cx="52" cy="72" r="5" fill="#2B2A28"/><circle cx="54" cy="70" r="1.6" fill="#fff"/><path d="M46 84 q 6 5 12 0" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="62" cy="86" r="4" fill="#FF9FA8" opacity=".7"/><path d="M60 50 q -4 -14 -14 -18 M70 47 q 2 -14 -6 -22" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="46" cy="32" r="3" fill="#2B2A28"/><circle cx="64" cy="25" r="3" fill="#2B2A28"/></svg>'

ABOUT = """<section class="about">
<h2>🐝 꿀단지가 뭔가요?</h2>
<p><b>꿀단지</b>는 U+ Enterprise혁신그룹이 만드는 사내 뉴스레터예요. 여섯 개 사업 영역을 <b>꽃밭</b>이라고 부르고, 그 꽃밭을 돌아다니며 뉴스를 물어오는 꿀벌이 <b>비비</b>예요. 비비가 모아온 걸 에디터가 다듬어서 한 스푼씩 떠 담는 곳, 그래서 꿀단지입니다.</p>
<p>세상에 뉴스 요약은 많아요. 꿀단지가 다른 건 <b>"그래서 우리 사업엔 무슨 뜻인가"</b>까지 간다는 점이에요. 경쟁사 발표를 그대로 옮기는 대신 속뜻을 번역하고, 매 호 끝에는 회의에서 그대로 써먹을 수 있는 한마디를 남겨요.</p>
<div class="who2"><div class="ic"><svg viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="비비"><ellipse cx="78" cy="42" rx="26" ry="14" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(-25 78 42)"/><ellipse cx="112" cy="40" rx="22" ry="12" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(20 112 40)"/><ellipse cx="92" cy="76" rx="46" ry="30" fill="#FFD35C" stroke="#2B2A28" stroke-width="3"/><path d="M74 49 q -8 27 0 54 M96 46 q -8 30 0 60 M118 52 q -7 24 0 46" stroke="#2B2A28" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M138 76 l 10 0" stroke="#2B2A28" stroke-width="3" stroke-linecap="round"/><circle cx="52" cy="72" r="5" fill="#2B2A28"/><circle cx="54" cy="70" r="1.6" fill="#fff"/><path d="M46 84 q 6 5 12 0" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="62" cy="86" r="4" fill="#FF9FA8" opacity=".7"/><path d="M60 50 q -4 -14 -14 -18 M70 47 q 2 -14 -6 -22" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="46" cy="32" r="3" fill="#2B2A28"/><circle cx="64" cy="25" r="3" fill="#2B2A28"/></svg></div>
<div><h3>비비 — 꿀벌</h3><p>B2B의 그 '비'예요. 여섯 꽃밭을 날아다니며 뉴스를 모아오고, 경쟁사 발표를 반말로 번역해요. 짧고 솔직하고 가끔 뼈가 있어요.</p></div></div>
<div class="who2"><div class="ic"><div class="av2">P</div></div>
<div><h3>에디터 P — 사람</h3><p>비비가 물어온 걸 다듬고, 우리 사업 관점에서 해석을 붙여요. 존댓말을 쓰고 가끔 TMI를 흘려요. 틀리면 다음 호에서 정정합니다.</p></div></div>
<div class="fields"><span>🌊 유선</span><span>📡 무선</span><span>🏪 SMB</span><span>🚗 모빌리티</span><span>🔐 보안</span><span>🤖 AI</span></div>
<div class="rule">📌 <b>세 가지 약속</b><br>① 최근 3일 이내 뉴스만 다뤄요. 오래된 건 배경 설명에만 씁니다.<br>② 새 소식이 없는 날은 "오늘은 조용했어요" 한 줄만 보내요. 억지로 안 채웁니다.<br>③ 사내 수치는 지어내지 않아요. 확인이 필요한 건 그렇다고 적습니다.</div>
</section>
<div class="secline">지난 호 — 최신순</div>"""

nav_items = []
for name, key in FIELDS:
    on = " on" if name == "전체" else ""
    nav_items.append('<a href="#" data-f="%s" class="filt%s">%s</a>' % (key, on, name))
navs = "".join(nav_items)

cards = ""
for it in issues:
    cards += (
        '<a class="item" href="%s" data-field="%s">'
        '<div class="meta"><span class="no">No.%s</span><span>%s %s</span><span>·</span><span>%s (%s)</span></div>'
        '<h3>%s</h3><p>%s</p></a>\n'
        % (it["file"], it["field"], it["no"], it["emoji"], it["field"],
           it["date"], it["dow"], it["title"], it["dek"])
    )

script = (
    "const filt=document.querySelectorAll('.filt'),items=document.querySelectorAll('.item');"
    "filt.forEach(b=>b.addEventListener('click',e=>{e.preventDefault();"
    "filt.forEach(x=>x.classList.remove('on'));b.classList.add('on');"
    "const f=b.dataset.f;items.forEach(it=>{it.style.display="
    "(f==='all'||it.dataset.field===f)?'block':'none';});}));"
)

html = (
    '<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    '<title>꿀단지. — U+ Enterprise혁신그룹 위클리</title>'
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">'
    '<link rel="stylesheet" href="style.css"><script src="gate.js"></script></head><body><div class="mag">'
    '<header class="top"><div class="row"><span>U+ Enterprise혁신그룹 위클리</span><span>월·수·금</span></div>'
    '<div class="logo">꿀단지<span>.</span></div>'
    '<div class="tag">다섯 사업 꽃밭을 돌아가며, 비비🐝가 떠주는 주 3회 꿀 한 스푼</div>'
    '<div class="hero"><div class="bubble">지난 호 여기 다 있어. 위에서 사업별로 골라 봐. 최신이 맨 위야.</div>' + BEE + '</div></header>'
    '<main class="pad">' + ABOUT + '<div class="nav">' + navs + '</div>'
    '<div class="list" id="list">' + cards + '</div>'
    '<div class="src">colophon · 콘텐츠는 Claude가 쓰고, 에디터가 검수하고, push하면 Vercel이 배포합니다. 새 호는 issues.json에 한 줄 추가로 올라와요.</div>'
    '</main></div><script>' + script + '</script></body></html>'
)
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html built with", len(issues), "issue(s)")
