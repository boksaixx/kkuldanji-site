# 꿀단지. — U+ Enterprise혁신그룹 위클리

정적 뉴스레터 사이트. **콘텐츠는 Claude(구독)로 만들고, GitHub에 올리면 Vercel이 자동 배포**합니다. API 크레딧 안 씁니다.

## 구조
```
index.html        ← 자동 생성. 손대지 마세요 (build_index.py가 만듦)
issues.json       ← 호 목록(메타데이터). 새 호는 여기에 항목 하나 추가
issues/           ← 실제 뉴스레터 HTML 파일들
  001-2026-09-02-wire.html
style.css         ← 공통 디자인
build_index.py    ← issues.json → index.html
vercel.json       ← 배포 설정
```

## 새 호 발행하는 법 (매주 월·수·금)
1. Claude에게: "이번 주 <사업> 꽃밭 만들어줘" → 완성된 HTML을 받는다
2. 그 파일을 `issues/` 에 저장 (예: `002-2026-09-04-security.html`)
   - 파일명 규칙: `번호-날짜-사업영문.html`
3. `issues.json` 맨 위에 항목 하나 추가:
   ```json
   {
     "no": 2, "field": "보안", "emoji": "🔐",
     "date": "2026-09-04", "dow": "금",
     "file": "issues/002-2026-09-04-security.html",
     "title": "제목", "dek": "한 줄 설명"
   }
   ```
4. `python build_index.py` 실행 (index.html 갱신)
5. GitHub에 커밋·푸시 → **Vercel이 30초 안에 자동 배포**

> build_index.py를 못 돌리는 환경이면, 그 단계도 Claude에게 맡기세요. issues.json만 주면 새 index.html을 만들어 드립니다.

## Vercel 최초 연결 (한 번만)
1. vercel.com 로그인 → **Add New → Project**
2. 이 GitHub 리포 **Import**
3. Framework Preset: **Other**, 나머지 기본값 → **Deploy**
4. 끝. 이후 main 브랜치에 푸시할 때마다 자동 배포됩니다.

사업 5개(유선·무선·SMB·모빌리티·보안)는 상단 필터 버튼으로 걸러 볼 수 있습니다.
