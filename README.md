# Cofathon Track 2 · 올리브영 AI 엔지니어

노트북과 데스크탑에서 같은 준비 상태를 이어가기 위한 인수인계
디렉터리입니다. 공식 과제가 공개되면 이 문서보다 공식 과제문,
채점 기준, 제출 규격이 우선합니다.

## 현재 확정된 사실

- 과제명: `건강한 아름다움을 위한 웰니스 상품 기획전 자동화 MVP`
- 작업 시간: 225분
- 제출 후 3분 확인 문제가 이어지며 답변도 평가에 반영됨
- 필요 시 연장 가능하다고 표시되지만 기본 일정에는 연장을 포함하지 않음
- 웹 IDE에 Explorer, 편집기, Terminal, Browser Preview, 내장 AI 채팅이 있음
- Terminal에는 Claude Code·Codex 같은 CLI가 미리 준비돼 있음
- Skills 폴더 업로드와 `.mcp.json` 편집 화면이 있음
- 세션 활동 기록과 카메라 확인 동의가 필요함

근거 화면은 [`screenshots/`](screenshots/)에 고유 이미지 5장만 보관했습니다.
대기실 중복 이미지는 SHA-256이 같아 제외했습니다.

## 권장 운영 구조

| 역할 | 담당 |
|---|---|
| Codex Goal | 유일한 구현 컨트롤러. 과제·제약·검증 조건과 남은 작업을 유지 |
| 실제 앱/MVP | 웰니스 기획전 자동화의 입력→처리→출력 사용자 흐름 |
| task harness | 스키마·기능·제약·회귀·실행시간을 사실로 측정 |
| 선택적 agent-loop G1 | 고정된 결과와 원장을 두 번 이하로 감사 |
| 사람 | 요구 해석, champion 승인, 제출, 제출 후 3분 답변 |

기본값은 `Goal + mini task harness + Terminal + Browser Preview`입니다.
Skills나 MCP는 화면에 존재한다는 이유만으로 사용하지 않습니다.

## agent-loop G1 사용 경계

- 체크포인트 태그:
  `checkpoint/b1-g1-materialization-custody-20260728`
- peeled commit:
  `2894c968ffd1686f3a26576b4efbaf0fb7c38080`
- 해당 커밋은 원격
  `b1-role-harness-superiority-20260727` 브랜치의 조상입니다.
- G1은 전체 대회 자동화 완성이 아니라, 정상 materialization
  process lifecycle/start 증거가 빠진 결과를 fresh audit가 잘못
  승인하던 P0를 막은 감사 체크포인트입니다.
- 웹 IDE 입장 후 최대 3분 smoke가 모두 통과할 때만 사용합니다.
- 사용 시점은 vertical slice의 `pre_completion` 감사와 최종 freeze의
  `complete` 감사, 최대 두 번입니다.
- Codex Goal과 `agent-loop-goal drive`를 동시에 실행하지 않습니다.
- 현재 개발 중인 dirty G2 작업 트리를 대회에 업로드하지 않습니다.
- G1 설치기는 PowerShell 중심이므로 Linux형 웹 IDE에서 포팅에 시간을
  쓰지 않습니다. 실패하면 즉시 mini harness로 돌아갑니다.

## 노트북에서 시작

```powershell
git clone https://github.com/sanghyun747/Cofathon.git
cd Cofathon
python contest-kit\scripts\preflight.py
python -m unittest discover -s contest-kit\tests -v
```

이미 clone했다면 먼저 현재 변경을 확인한 뒤 pull하세요.

```powershell
git status
git pull --ff-only
```

실전 작업 디렉터리 초기화:

```powershell
python contest-kit\scripts\init_work.py --output work
```

Linux 웹 IDE에서는 `python` 대신 필요하면 `python3`를 사용합니다.

## 파일 안내

- [`docs/CONTEST_DAY_RUNBOOK.md`](docs/CONTEST_DAY_RUNBOOK.md):
  225분 실행 순서와 제출 후 3분 대응
- [`docs/ENVIRONMENT_AND_TOOLING.md`](docs/ENVIRONMENT_AND_TOOLING.md):
  Explorer·Terminal·Preview·Skills·MCP의 의미와 smoke 방법
- [`docs/KNOWN_UNKNOWNS.md`](docs/KNOWN_UNKNOWNS.md):
  과제 공개 직후 받아 적을 미확인 항목
- [`contest-kit/`](contest-kit/): 표준 라이브러리 기반 225분 mini task harness
- [`research/`](research/): 2024~2026 해커톤·올리브영 공개 근거 조사
- [`archive/`](archive/): 280분 가정을 사용했던 과거 준비·검증 스냅샷
- [`screenshots/`](screenshots/): 웹 IDE 사전 체험 화면
- [`memory/MEMORY.md`](memory/MEMORY.md): 노트북 재개용 중요 기억

## 아직 확정되지 않은 것

실제 입력 데이터와 스키마, 채점 가중치·실격 조건, 제출물 형식과
entrypoint, 패키지 설치·네트워크·저장 지속성, Skills를 소비하는 AI,
MCP transport·환경변수·reload 방식은 아직 확인되지 않았습니다.
과제 시작 후 [`docs/KNOWN_UNKNOWNS.md`](docs/KNOWN_UNKNOWNS.md)를 먼저
채운 뒤 Goal과 validator를 고정합니다.
