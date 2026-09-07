#!/usr/bin/env python3
"""issues.json을 읽어 index.html 생성. 새 호는 issues.json에 항목 추가 후 이 스크립트 실행."""
import json, pathlib
root = pathlib.Path(__file__).parent
issues = json.loads((root / "issues.json").read_text(encoding="utf-8"))
issues.sort(key=lambda x: x["no"], reverse=True)

FIELDS = [("전체", "all"), ("유선", "유선"), ("무선", "무선"),
          ("SMB", "SMB"), ("모빌리티", "모빌리티"), ("보안", "보안")]
BEE = '<svg class="bee" viewBox="0 0 150 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="꿀벌 비비"><ellipse cx="78" cy="42" rx="26" ry="14" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(-25 78 42)"/><ellipse cx="112" cy="40" rx="22" ry="12" fill="#DDF3F7" stroke="#9FD6E2" stroke-width="1.5" transform="rotate(20 112 40)"/><ellipse cx="92" cy="76" rx="46" ry="30" fill="#FFD35C" stroke="#2B2A28" stroke-width="3"/><path d="M74 49 q -8 27 0 54 M96 46 q -8 30 0 60 M118 52 q -7 24 0 46" stroke="#2B2A28" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M138 76 l 10 0" stroke="#2B2A28" stroke-width="3" stroke-linecap="round"/><circle cx="52" cy="72" r="5" fill="#2B2A28"/><circle cx="54" cy="70" r="1.6" fill="#fff"/><path d="M46 84 q 6 5 12 0" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="62" cy="86" r="4" fill="#FF9FA8" opacity=".7"/><path d="M60 50 q -4 -14 -14 -18 M70 47 q 2 -14 -6 -22" stroke="#2B2A28" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="46" cy="32" r="3" fill="#2B2A28"/><circle cx="64" cy="25" r="3" fill="#2B2A28"/></svg>'

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
    '<link rel="stylesheet" href="style.css"></head><body><div class="mag">'
    '<header class="top"><div class="row"><span>U+ Enterprise혁신그룹 위클리</span><span>월·수·금</span></div>'
    '<div class="logo">꿀단지<span>.</span></div>'
    '<div class="tag">다섯 사업 꽃밭을 돌아가며, 비비🐝가 떠주는 주 3회 꿀 한 스푼</div>'
    '<div class="hero"><div class="bubble">지난 호 여기 다 있어. 위에서 사업별로 골라 봐. 최신이 맨 위야.</div>' + BEE + '</div></header>'
    '<main class="pad"><div class="nav">' + navs + '</div>'
    '<div class="list" id="list">' + cards + '</div>'
    '<div class="src">colophon · 콘텐츠는 Claude가 쓰고, 에디터가 검수하고, push하면 Vercel이 배포합니다. 새 호는 issues.json에 한 줄 추가로 올라와요.</div>'
    '</main></div><script>' + script + '</script></body></html>'
)
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html built with", len(issues), "issue(s)")
