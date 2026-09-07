# 꿀단지. — U+ Enterprise혁신그룹 위클리

정적 뉴스레터 사이트 + 앱(PWA). **콘텐츠는 Claude(구독)로 만들고, GitHub에 올리면 Vercel이 자동 배포**합니다. API 크레딧 안 씁니다.

## 이 사이트가 하는 일

| 기능 | 동작 |
|---|---|
| 🔒 첫 방문 | 비밀번호(기본 `8080`) → 이름·소속팀 등록 → 입장 |
| 🐝 재방문 | 아무것도 안 묻고 바로 입장, 상단에 "OO님 오셨어요" |
| 📲 앱 설치 | 첫 화면·목록 페이지에 설치 버튼. 홈 화면에 아이콘 생기고 앱처럼 열림. 아이폰은 안내 모달 |
| 📊 기록 | 누가 가입했는지 · 누가 어느 호를 읽었는지 · 투표 · "지워도 돼요" 사유 → **Supabase** |
| 🗳️ 투표 | 각 호 하단 "다음 호 뭘로" 버튼이 실제로 집계됨 (1인 1표) |

## 최초 설정 (한 번만, 20분)

### 1. Supabase (등록·읽음 기록 저장소)
1. supabase.com 가입 → **New project** (무료 플랜이면 충분)
2. 프로젝트 열리면 왼쪽 **SQL Editor** → 이 리포의 `supabase.sql` 내용 전체 붙여넣기 → **Run**
3. 왼쪽 **Settings → API** 에서 두 값 복사:
   - `Project URL` (예: https://abcdefgh.supabase.co)
   - `anon public` 키
4. 이 리포의 `config.js` 열어서 두 값 채우기:
   ```js
   SUPABASE_URL: "https://abcdefgh.supabase.co",
   SUPABASE_ANON_KEY: "eyJhbGciOi...",
   ```
   > anon 키는 **공개용**이라 소스에 넣어도 됩니다. `supabase.sql`의 RLS 설정으로 브라우저는 "쓰기만" 되고 읽기는 대시보드에서만 됩니다.

5. 소속팀 목록도 `config.js`의 `TEAMS`에서 손보세요.

### 2. GitHub → Vercel
1. 이 폴더 전체를 GitHub 리포에 올리기 (`issues/`, `icons/` 폴더 포함)
2. vercel.com → GitHub 로그인 → **Add New → Project** → 리포 Import → Framework **Other** → **Deploy**
3. 나온 주소(예: `kkuldanji.vercel.app`)가 사이트이자 앱 설치 주소

> PWA는 https에서만 설치돼요. Vercel은 기본 https라 추가 설정 없음.

## 기록 보는 법
Supabase 대시보드 → **Table Editor**:
- `v_readers` — 누가 가입했고 몇 호를 읽었는지, 마지막 접속
- `v_issue_stats` — 호별 순 독자 수·열람 수
- `v_vote_results` — 호별 투표 결과
- `feedback` — "지워도 돼요" 누른 사람과 사유

전무 보고용 숫자는 여기서 바로 뽑으면 됩니다.

## 매주 발행 (5분)
1. Claude에게: **"오늘 AI랑 보안 꽃밭 만들어줘"** (2~3개 한 번에)
2. 받은 HTML을 `issues/`에 추가, `issues.json`에 항목 추가 (기존 호는 그대로 — 계속 쌓임)
3. 커밋·푸시 → Vercel이 30초 안에 배포. 앱으로 설치한 사람도 다음 열 때 새 호가 보여요

## 꽃밭 6개와 리듬
유선 🌊 · 무선 📡 · SMB 🏪 · 모빌리티 🚗 · 보안 🔐 · AI 🤖
월·수·금 하루 2~3호. 최근 3일 이내 뉴스만. 없으면 "조용했어요" 한 줄.

## 파일 구조
```
index.html            ← 자동 생성 (build_index.py). 손대지 않음
issues.json           ← 호 목록. 새 호는 여기 한 줄 추가
issues/               ← 호별 HTML (계속 쌓임)
config.js             ← 비밀번호 · Supabase 키 · 팀 목록  ← 유일하게 손볼 파일
gate.js               ← 비밀번호·등록·환영·설치·기록 로직
sw.js, manifest.webmanifest, icons/  ← 앱(PWA) 구성
supabase.sql          ← DB 스키마. Supabase에 한 번 실행
style.css             ← 디자인
tools/                ← 호 생성 템플릿 (Claude가 참고)
```

## 알아둘 것
- **비밀번호는 소스에서 보입니다.** 외부인 실수 유입을 막는 문이지 보안이 아니에요. 실제 운영 땐 리포를 Private으로 두거나 Vercel Password Protection(Pro)을 쓰세요.
- 등록 정보는 사용자 브라우저(localStorage)에도 저장돼요. 브라우저 데이터를 지우면 다시 등록 화면이 나오고, 그 사람은 DB에 새 행으로 잡힙니다(이름·팀으로 합쳐 보면 됨).
- 비밀번호 변경: `config.js`의 `PASS`.
