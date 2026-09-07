# 각 호에 들어갈 원본 SVG 일러스트
ART = {}

ART["wire"] = ('해저케이블 단면과 용량 비교', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="해저케이블 단면도와 KT 용량 확대 계획 막대그래프">
<rect width="560" height="300" fill="#07213F" rx="14"/>
<text x="28" y="38" fill="#fff" font-family="Pretendard,sans-serif" font-size="15" font-weight="800">심해 케이블 단면 — 지름 약 2cm</text>
<circle cx="105" cy="150" r="66" fill="#010A16"/><circle cx="105" cy="150" r="54" fill="#8D96A3"/>
<circle cx="105" cy="150" r="40" fill="#0B1B2E"/><circle cx="105" cy="150" r="27" fill="#C8842A"/>
<circle cx="105" cy="150" r="15" fill="#F0F4F8"/>
<g fill="#0E4A80"><circle cx="100" cy="145" r="2.2"/><circle cx="110" cy="144" r="2.2"/><circle cx="113" cy="153" r="2.2"/><circle cx="105" cy="158" r="2.2"/><circle cx="97" cy="154" r="2.2"/></g>
<g font-family="Pretendard,sans-serif" font-size="11.5" fill="#BFD9F2">
<line x1="171" y1="105" x2="205" y2="105" stroke="#456B93"/><text x="212" y="109">폴리에틸렌 외피</text>
<line x1="160" y1="132" x2="205" y2="132" stroke="#456B93"/><text x="212" y="136">강선 외장 — 닻·저인망 방어</text>
<line x1="146" y1="159" x2="205" y2="159" stroke="#456B93"/><text x="212" y="163">구리관 — 중계기 전력</text>
<line x1="122" y1="186" x2="205" y2="186" stroke="#456B93"/><text x="212" y="190" fill="#FFD35C" font-weight="700">광섬유 — 머리카락 굵기</text>
<text x="212" y="214" fill="#8FA8C4">이 안으로 대륙 간 트래픽의 99%가 지나갑니다</text></g>
<g font-family="Pretendard,sans-serif"><text x="28" y="255" fill="#fff" font-size="13" font-weight="800">KT 해저케이블 용량 계획</text>
<rect x="28" y="266" width="86" height="16" fill="#5C7897"/><text x="122" y="279" fill="#BFD9F2" font-size="12">38Tbps 현재</text>
<rect x="222" y="266" width="290" height="16" fill="#FFD35C"/><text x="222" y="262" fill="#FFD35C" font-size="12" font-weight="700">128Tbps — 2031년 목표 (90Tbps 추가)</text></g></svg>''')

ART["security"] = ('과징금 상한 변화', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="개정 개인정보보호법 시행 전후 과징금과 통지 기준 비교">
<rect width="560" height="300" fill="#fff" rx="14" stroke="#EFE6D6"/>
<text x="26" y="36" font-family="Pretendard,sans-serif" font-size="15" font-weight="800" fill="#2B2A28">9월 11일, 이렇게 바뀝니다</text>
<g font-family="Pretendard,sans-serif" font-size="12" fill="#7A7570">
<text x="26" y="62">과징금 상한 (연매출 1조 기업 가정)</text></g>
<rect x="26" y="72" width="120" height="30" rx="6" fill="#E5E8EB"/><text x="34" y="92" font-family="Pretendard,sans-serif" font-size="13" font-weight="700" fill="#4E5968">종전 기준</text>
<rect x="26" y="110" width="480" height="30" rx="6" fill="#FF7AB6"/><text x="34" y="130" font-family="Pretendard,sans-serif" font-size="13" font-weight="800" fill="#fff">개정 — 매출액의 최대 10% · 최대 1,000억 원</text>
<line x1="26" y1="162" x2="534" y2="162" stroke="#EFE6D6"/>
<g font-family="Pretendard,sans-serif">
<text x="26" y="188" font-size="12" fill="#7A7570">통지 의무가 시작되는 시점</text>
<rect x="26" y="200" width="230" height="70" rx="10" fill="#F5F6F8"/>
<text x="42" y="224" font-size="13" font-weight="800" fill="#4E5968">종전</text><text x="42" y="246" font-size="12.5" fill="#7A7570">유출이 &#39;확인&#39;된 뒤</text><text x="42" y="263" font-size="12.5" fill="#7A7570">→ 조사할 시간이 있었음</text>
<rect x="278" y="200" width="228" height="70" rx="10" fill="#FFF3F9"/>
<text x="294" y="224" font-size="13" font-weight="800" fill="#8A1E5A">개정</text><text x="294" y="246" font-size="12.5" fill="#8A1E5A">유출 &#39;가능성&#39; 단계부터</text><text x="294" y="263" font-size="12.5" fill="#8A1E5A">→ 탐지 속도가 곧 법적 리스크</text></g></svg>''')

ART["mobility"] = ('V2X 도로 구조', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="차량 센서가 못 보는 사각지대를 도로 인프라가 먼저 감지하는 V2X 구조">
<rect width="560" height="300" fill="#F5F6F8" rx="14"/>
<text x="26" y="34" font-family="Pretendard,sans-serif" font-size="15" font-weight="800" fill="#2B2A28">차가 못 보는 걸 도로가 먼저 봅니다</text>
<rect x="0" y="150" width="560" height="90" fill="#4E5968"/>
<g stroke="#fff" stroke-width="3" stroke-dasharray="26 20"><line x1="0" y1="195" x2="560" y2="195"/></g>
<rect x="70" y="163" width="66" height="30" rx="7" fill="#3182F6"/><circle cx="86" cy="196" r="7" fill="#2B2A28"/><circle cx="120" cy="196" r="7" fill="#2B2A28"/>
<path d="M136 178 L 250 160 L 250 196 Z" fill="#3182F6" opacity=".18"/>
<text x="150" y="152" font-family="Pretendard,sans-serif" font-size="11.5" fill="#3182F6" font-weight="700">차량 센서 시야</text>
<rect x="380" y="205" width="66" height="30" rx="7" fill="#FF7AB6"/><circle cx="396" cy="238" r="7" fill="#2B2A28"/><circle cx="430" cy="238" r="7" fill="#2B2A28"/>
<text x="368" y="262" font-family="Pretendard,sans-serif" font-size="11.5" fill="#8A1E5A" font-weight="700">사각지대의 차량</text>
<line x1="470" y1="60" x2="470" y2="150" stroke="#2B2A28" stroke-width="5"/><rect x="452" y="46" width="36" height="20" rx="4" fill="#2B2A28"/>
<g fill="none" stroke="#0E9F6E" stroke-width="2.5"><path d="M446 70 q -16 12 0 24" opacity=".9"/><path d="M436 62 q -24 20 0 40" opacity=".6"/><path d="M426 54 q -32 28 0 56" opacity=".35"/></g>
<text x="336" y="42" font-family="Pretendard,sans-serif" font-size="12" fill="#0E9F6E" font-weight="800">노변기지국(RSU)이 둘 다 보고 있음</text>
<rect x="26" y="60" width="200" height="62" rx="10" fill="#fff"/>
<text x="42" y="86" font-family="Pretendard,sans-serif" font-size="26" font-weight="900" fill="#FF7AB6">20%</text>
<text x="42" y="106" font-family="Pretendard,sans-serif" font-size="11.5" fill="#7A7570">세종-대전 V2X 구간 5년간</text>
<text x="42" y="120" font-family="Pretendard,sans-serif" font-size="11.5" fill="#7A7570">사고·사상자 감소</text></svg>''')

ART["wireless"] = ('개별 구축 vs 공유형', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="공장별 개별 코어 구축과 산단 공유형 코어 구조 비교">
<rect width="560" height="300" fill="#fff" rx="14" stroke="#EFE6D6"/>
<text x="26" y="34" font-family="Pretendard,sans-serif" font-size="15" font-weight="800" fill="#2B2A28">같은 5G를 까는 두 가지 방법</text>
<g font-family="Pretendard,sans-serif">
<text x="26" y="62" font-size="12.5" font-weight="700" fill="#7A7570">지금까지 — 공장마다 코어까지 따로</text>
<g fill="#E5E8EB" stroke="#C9CED4"><rect x="26" y="74" width="72" height="56" rx="8"/><rect x="112" y="74" width="72" height="56" rx="8"/><rect x="198" y="74" width="72" height="56" rx="8"/></g>
<g font-size="10.5" fill="#4E5968" text-anchor="middle"><text x="62" y="96">코어+DU</text><text x="62" y="112">공장 A</text><text x="148" y="96">코어+DU</text><text x="148" y="112">공장 B</text><text x="234" y="96">코어+DU</text><text x="234" y="112">공장 C</text></g>
<text x="288" y="106" font-size="12" fill="#8A3A00" font-weight="700">중소기업엔 진입장벽</text>
<line x1="26" y1="150" x2="534" y2="150" stroke="#EFE6D6"/>
<text x="26" y="178" font-size="12.5" font-weight="700" fill="#1F5A33">창원 방식 — 코어는 하나, 공장엔 DU만</text>
<rect x="212" y="192" width="132" height="40" rx="10" fill="#0E9F6E"/><text x="278" y="217" font-size="12.5" fill="#fff" font-weight="800" text-anchor="middle">공유 코어망 1개</text>
<g fill="#CFF3DA" stroke="#0E9F6E"><rect x="40" y="256" width="82" height="34" rx="8"/><rect x="146" y="256" width="82" height="34" rx="8"/><rect x="252" y="256" width="82" height="34" rx="8"/><rect x="358" y="256" width="82" height="34" rx="8"/><rect x="452" y="256" width="70" height="34" rx="8"/></g>
<g font-size="10.5" fill="#1F5A33" text-anchor="middle" font-weight="700"><text x="81" y="278">DU</text><text x="187" y="278">DU</text><text x="293" y="278">DU</text><text x="399" y="278">DU</text><text x="487" y="278">DU…</text></g>
<g stroke="#0E9F6E" stroke-width="1.6" opacity=".55"><path d="M278 232 L 81 256"/><path d="M278 232 L 187 256"/><path d="M278 232 L 293 256"/><path d="M278 232 L 399 256"/><path d="M278 232 L 487 256"/></g>
<text x="366" y="217" font-size="12" fill="#1F5A33" font-weight="700">구축·운용비 하락</text></g></svg>''')

ART["smb"] = ('지원사업 흐름', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="소상공인 지원 예산 규모와 사장님이 겪는 병목 구조">
<rect width="560" height="300" fill="#fff" rx="14" stroke="#EFE6D6"/>
<text x="26" y="34" font-family="Pretendard,sans-serif" font-size="15" font-weight="800" fill="#2B2A28">돈은 풀렸는데, 여기서 막힙니다</text>
<g font-family="Pretendard,sans-serif">
<rect x="26" y="56" width="150" height="86" rx="12" fill="#FFF3E0"/>
<text x="101" y="88" font-size="24" font-weight="900" fill="#8A5A00" text-anchor="middle">5.4조</text>
<text x="101" y="108" font-size="11.5" fill="#8A5A00" text-anchor="middle">2026 소상공인 예산</text>
<text x="101" y="126" font-size="11.5" fill="#8A5A00" text-anchor="middle">(역대 최대)</text>
<path d="M186 99 L 214 99" stroke="#C9CED4" stroke-width="2.5" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#C9CED4"/></marker></defs>
<rect x="222" y="56" width="150" height="86" rx="12" fill="#FFF8E1"/>
<text x="297" y="88" font-size="24" font-weight="900" fill="#8A5A00" text-anchor="middle">144억</text>
<text x="297" y="108" font-size="11.5" fill="#8A5A00" text-anchor="middle">AI·디지털 전환</text>
<text x="297" y="126" font-size="11.5" fill="#8A5A00" text-anchor="middle">지원사업</text>
<path d="M382 99 L 410 99" stroke="#C9CED4" stroke-width="2.5" marker-end="url(#a)"/>
<rect x="418" y="56" width="116" height="86" rx="12" fill="#FFF3F9" stroke="#FFB6D9" stroke-dasharray="5 4"/>
<text x="476" y="90" font-size="30" text-anchor="middle">🤔</text>
<text x="476" y="116" font-size="11.5" fill="#8A1E5A" text-anchor="middle" font-weight="700">"어디서부터</text>
<text x="476" y="132" font-size="11.5" fill="#8A1E5A" text-anchor="middle" font-weight="700">시작하죠?"</text>
<line x1="26" y1="170" x2="534" y2="170" stroke="#EFE6D6"/>
<text x="26" y="198" font-size="12.5" fill="#7A7570">지원 한도 (2026년 확대분)</text>
<rect x="26" y="212" width="96" height="26" rx="6" fill="#FFD35C"/><text x="132" y="230" font-size="12.5" fill="#4E5968">운전자금 최대 2억</text>
<rect x="26" y="248" width="380" height="26" rx="6" fill="#FFB48A"/><text x="416" y="266" font-size="12.5" fill="#4E5968">시설자금 최대 10억</text>
</g></svg>''')

ART["ai"] = ('도입률과 내재화율의 간격', '''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="생성형 AI 도입률 61%와 조직 내재화 6.7% 격차 그래프">
<rect width="560" height="300" fill="#fff" rx="14" stroke="#EFE6D6"/>
<text x="26" y="34" font-family="Pretendard,sans-serif" font-size="15" font-weight="800" fill="#2B2A28">도입은 했는데, 조직에 남지 않았습니다</text>
<g font-family="Pretendard,sans-serif">
<text x="26" y="66" font-size="12.5" fill="#7A7570">생성형 AI 도입률</text>
<rect x="26" y="76" width="310" height="38" rx="8" fill="#FFD35C"/>
<text x="42" y="102" font-size="20" font-weight="900" fill="#2B2A28">61%</text>
<text x="348" y="101" font-size="12" fill="#A39D95">300여 개 기업 HRD 담당자 조사</text>
<text x="26" y="150" font-size="12.5" fill="#7A7570">실제 조직적 내재화</text>
<rect x="26" y="160" width="34" height="38" rx="8" fill="#FF7AB6"/>
<text x="72" y="186" font-size="20" font-weight="900" fill="#FF7AB6">6.7%</text>
<g stroke="#D6336C" stroke-width="1.6" stroke-dasharray="5 5"><line x1="60" y1="150" x2="60" y2="206"/><line x1="336" y1="70" x2="336" y2="206"/></g>
<path d="M66 212 L 330 212" stroke="#D6336C" stroke-width="1.6"/>
<path d="M66 212 l 7 -5 v10 z M330 212 l -7 -5 v10 z" fill="#D6336C"/>
<text x="198" y="232" font-size="12.5" font-weight="800" fill="#D6336C" text-anchor="middle">이 간격이 시장입니다</text>
<line x1="26" y1="252" x2="534" y2="252" stroke="#EFE6D6"/>
<text x="26" y="276" font-size="12" fill="#7A7570">Gartner 전망 · 기업 앱의 AI 에이전트 통합 비율</text>
<text x="392" y="276" font-size="12" fill="#4E5968" font-weight="700">2025년 5% 미만 → 2026년 40%</text>
</g></svg>''')
