# 최종목표(Final Goal)

노트북과 데스크탑에서 동일한 Cofathon Track 2 준비 상태를 유지하고,
225분 안에 검증 가능한 웰니스 상품 기획전 자동화 MVP를 제출한다.

## 지금 하고있는 일(Current Focus)

- [x] waiting-room과 IDE 사전 체험 화면의 확정 사실 기록
- [x] 280분 contest-kit을 225분 + 제출 후 3분 구조로 수정
- [x] Skills와 MCP의 역할·미확인 경계 문서화
- [x] agent-loop G1의 정확한 태그·커밋과 사용 한계 기록
- [x] 원격 main과 G1 tag에 게시하고 clean clone에서 재검증
- [ ] 과제 공개 후 `docs/KNOWN_UNKNOWNS.md` P0 채우기
- [ ] 실제 schema와 rubric에 맞춰 validator/evaluator 연결
- [ ] thin vertical slice를 먼저 완성하고 champion 고정
- [ ] 제출 후 3분 질문에 직접 답할 결정·검증 메모 유지

구조:

- `docs/`: 당일 운영과 도구 해설
- `contest-kit/`: 225분 mini task harness
- `research/`: 외부 공개 근거
- `archive/`: 현재 계획으로 사용하지 않는 과거 스냅샷
- `screenshots/`: 환경 사실 근거

## 대화 요약(Ping-Pong Summary)

- 사용자: Cofathon Track 2 올리브영 AI 엔지니어 대회를 위해 최근
  2년 기록, agent-loop, Goal, task harness 준비를 요청했다.
- 에이전트: 공개 근거와 로컬 agent-loop를 감사하고, Goal을 유일한
  컨트롤러, harness를 사실 측정 계층, G1을 선택적 frozen audit로
  분리했다.
- 사용자: 대회 화면을 제공하고 MCP·Skills 페이지의 사용법까지
  설명해 달라고 했다.
- 에이전트: 225분, 제출 후 3분, IDE·Preview·Skills·MCP 화면을
  확정 사실과 미확인 사항으로 분리했다.
- 사용자: 노트북에서도 작업할 수 있도록 Cofathon 자료를
  `sanghyun747/laptop-desktop`에 기록해 달라고 했다.
- 에이전트: 기존 dirty 작업 트리를 보존하고 원격 main 기반 별도
  브랜치에서 선별 자료와 225분 kit를 준비해 main에 push했고,
  content checkpoint `d781fd7031fe0d96755e1fa03096bfbd612f19d2`의
  clean clone에서 동일한 검증 결과를 확인했다.

## 참조(References)

- `../README.md`
- `../docs/CONTEST_DAY_RUNBOOK.md`
- `../docs/ENVIRONMENT_AND_TOOLING.md`
- `../docs/KNOWN_UNKNOWNS.md`
- `../MANIFEST.md`
- `2026-07-30.md`
- `chat/2026-07-30.md`
