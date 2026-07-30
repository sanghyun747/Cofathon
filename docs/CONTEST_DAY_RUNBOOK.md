# Cofathon Track 2 · 225분 운영표

## 시작 전

- 공식 과제문, 채점 기준, 제출 규격을 원문 그대로 확보합니다.
- `work/problem.md`에 사용자, 입력, 출력, 성공 조건, 금지 조건을 씁니다.
- `docs/KNOWN_UNKNOWNS.md`의 P0 항목부터 확인합니다.
- extension은 기본 일정에 포함하지 않습니다.

## 225분

| 분 | 할 일 | 통과 조건 |
|---:|---|---|
| 0~10 | 과제·평가·제출 계약 고정 | task contract와 non-goal이 적힘 |
| 10~15 | Python/Node/Codex/port/upload smoke, G1 go/no-go | 개발 서버와 최소 테스트가 실행됨 |
| 15~55 | 가장 얇은 end-to-end vertical slice | 실제 입력 하나가 실제 출력 하나로 이어짐 |
| 55~135 | 핵심 기획전 자동화·데이터 흐름 | 주 경로와 evaluator가 통과 |
| 135~175 | 브라우저 UI, 수정 흐름, 오류 처리 | Preview에서 사용자가 완주 가능 |
| 175~195 | 회귀·edge·fallback·시간 확인 | champion이 baseline 이상이며 회귀 통과 |
| 195~207 | champion 고정, 제출물 생성, receipt | 제출 후보와 해시가 고정됨 |
| 207~215 | fresh 재실행 또는 선택적 G1 감사 | 새 프로세스 검증 통과 |
| 215~225 | 제출, 미리보기, acknowledgement 보존 | 제출 완료가 화면·receipt로 확인됨 |

두 번 연속 개선이 없으면 새 접근을 멈추고 champion을 보존합니다.
100분 이후 새 모델 계열, 175분 이후 새 기능을 기본적으로 시작하지
않습니다.

## G1 go/no-go

최대 3분 동안 다음만 확인합니다.

1. 고정 G1 커밋 또는 tag를 가져올 수 있음
2. `agent-loop-v3 --help`가 실행됨
3. synthetic contract의 `initialize`, `status`, `audit`가 실행됨

모두 통과할 때만 vertical slice에서 `audit --stage pre_completion`,
최종 freeze에서 새 프로세스로 `audit --stage complete`를 사용합니다.
하나라도 실패하면 설치·포팅을 중단하고 contest-kit 검증으로 돌아갑니다.

## task harness가 측정할 사실

- 입력·출력 schema와 필수 필드
- 핵심 사용자 흐름 성공/실패
- 재고·중복·프로모션·상품 제약
- 결정적 회귀 fixture
- 처리시간과 오류율
- baseline, candidate, champion 비교
- 제출 파일 존재, 해시, 재실행 결과, acknowledgement

실제 과제 데이터가 공개되기 전에는 metric 이름을 확정하지 않습니다.

## 제출 후 3분 질문 준비

`work/decisions.md`에 아래 여섯 줄을 유지합니다.

```text
문제:
사용자:
입력→처리→출력:
핵심 선택과 이유:
검증 결과:
한계와 다음 개선:
```

답변은 코드 생성 과정을 나열하기보다 요구 해석, 선택의 근거, 실제
검증 결과, 알고 있는 한계를 중심으로 합니다.
