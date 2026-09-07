import pathlib, sys, json
sys.path.insert(0,'/tmp')
from art import ART
root = pathlib.Path("/home/claude/site")
BEE = open('/tmp/bee.txt').read().strip()
MINI = '<svg class="k" viewBox="0 0 34 24"><ellipse cx="18" cy="13" rx="13" ry="8" fill="#FFD35C" stroke="#2B2A28" stroke-width="1.5"/><path d="M14 6 v14 M20 5 v16" stroke="#2B2A28" stroke-width="2.5"/><circle cx="8" cy="12" r="1.8" fill="#2B2A28"/></svg>'

INTRO = ('<div class="note">🐝 <b>처음 오셨나요?</b> 꿀단지는 Enterprise혁신그룹 사내 뉴스레터예요. '
 '여섯 사업 영역을 <b>꽃밭</b>이라 부르고, 그 꽃밭을 돌며 뉴스를 물어오는 꿀벌이 <b>비비</b>예요. '
 'B2B의 그 비. 어려운 말 안 쓰고, 재미없으면 짧게 끝내요. <a href="../index.html">지난 호 보기 →</a></div>')

def bee(t): return '<div class="bee-say">%s<p>%s</p></div>' % (MINI, t)

def quiz(q, opts, ans_idx, expl):
    btns = "".join('<button data-i="%d">%s</button>' % (i, o) for i, o in enumerate(opts))
    return ('<div class="quiz" data-ans="%d"><div class="t">🐝 비비 퀴즈</div><div class="q">%s</div>'
            '<div class="opts">%s</div><div class="ans">%s</div></div>') % (ans_idx, q, btns, expl)

QUIZ_JS = """<script>
document.querySelectorAll('.quiz').forEach(function(z){var a=+z.dataset.ans,done=false;
z.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){if(done)return;done=true;
z.querySelectorAll('button').forEach(function(x){x.classList.add(+x.dataset.i===a?'ok':'no');});
z.querySelector('.ans').classList.add('show');});});});
</script>"""

def build(d):
    lbl, svg = ART[d["art"]]
    fig = '<figure class="fig"><div class="lbl">%s</div>%s<figcaption>%s</figcaption></figure>' % (lbl, svg, d["fig_cap"])
    tr = '<h2>🎤 발표 그대로 vs 비비 번역</h2><div class="chat">%s</div>' % "".join(
        '<div class="msg kt">%s</div><div class="msg kb">%s</div>' % (a,b) for a,b in d["translation"])
    us = '<div class="us">%s</div>' % "".join('<div><span>%d</span><div>%s</div></div>' % (i+1, x) for i, x in enumerate(d["us"]))
    evs = "".join('<div class="r"><div class="d">%s<small>%s</small></div><div><div class="t">%s<span class="tagb">%s</span></div><div class="m">%s <b>비비:</b> %s</div></div></div>' % (e[0],e[1],e[2],d["field"],e[3],e[4]) for e in d["events"])
    srcs = " · ".join('<a href="%s">%s</a>' % (u,t) for t,u in d["sources"])
    tldr = '<div class="tldr"><div class="t">⏱ 30초만 있으면</div><ol>%s</ol></div>' % "".join("<li>%s</li>" % x for x in d["tldr"])
    story = '<div class="story">%s</div>' % "".join(d["story"])
    return """<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>꿀단지. No.%(no)s · %(field)s — %(title_plain)s</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="../style.css"><link rel="manifest" href="/manifest.webmanifest"><meta name="theme-color" content="#9FE0EC"><link rel="apple-touch-icon" href="/icons/apple-touch-icon.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="default"><meta name="apple-mobile-web-app-title" content="꿀단지"><link rel="icon" href="/icons/icon-192.png"><meta name="issue" content="%(no)s"><script src="/config.js"></script><script src="/gate.js"></script></head><body><div class="mag">
<header class="top"><div class="row"><a href="../index.html">← 지난 호 전체</a><span>No.%(no)s · %(datelabel)s · %(readtime)s</span></div>
<div class="logo">꿀단지<span>.</span></div><div class="tag">여섯 꽃밭을 돌아가며 꿀 한 스푼 · 오늘 꽃밭: %(field)s %(emoji)s</div>
<div class="hero"><div class="bubble">%(hello)s</div>%(BEE)s</div></header>
<main class="pad">
<h1>%(title)s</h1><p class="dek">%(dek)s</p>
%(INTRO)s
%(tldr)s
<section class="letter"><div class="who"><div class="av">P</div><div><b>에디터 P</b><small>Enterprise혁신그룹</small></div></div>%(letter)s</section>
%(story)s
%(fig)s
%(tr)s
%(quiz)s
<h2>🙋 이게 우리랑 무슨 상관?</h2>
<p class="ps" style="margin-bottom:6px">딱 세 개만.</p>
%(us)s
%(bee_close)s
<h2>💬 회의에서 써먹을 한마디</h2>
<div class="copy">%(quote)s<small>%(quote_note)s</small></div>
<h2>🎪 갈 만한 데</h2><div class="ev">%(evs)s</div>
<h2>🗳️ 다음 호, 뭘로 할까요</h2>
<div class="vote">%(votes)s<a href="#">🗑️ 그냥 지워도 돼요</a></div>
<p class="ps">마지막 거 누르면 진짜로 안 보내요. 대신 이유 한 줄만. 비비가 봐요.</p>
<section class="letter" style="margin-top:30px"><div class="who"><div class="av">P</div><div><b>에디터 P의 마무리</b><small>퇴근 30분 전</small></div></div>%(outro)s</section>
<div class="src">공개된 뉴스와 정부 자료로 만들었어요. 사내 숫자는 지어내지 않아요. 틀리면 다음 호에서 고칩니다.<br>출처: %(srcs)s</div>
</main></div>%(QUIZ_JS)s</body></html>""" % dict(d, BEE=BEE, INTRO=INTRO, tldr=tldr, story=story, fig=fig, tr=tr, us=us, evs=evs, srcs=srcs, QUIZ_JS=QUIZ_JS,
    quiz=d["quiz"], bee_close=bee(d["bee_close"]),
    letter="".join("<p>%s</p>" % x for x in d["letter"]),
    outro="".join("<p>%s</p>" % x for x in d["outro"]),
    votes="".join('<a href="#">%s</a>' % v for v in d["vote"]))
