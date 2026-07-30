# 과제 공개 후 확인할 미확인 항목

## P0: 구현 전에 고정

- [ ] 전체 과제문
- [ ] 채점 항목, 가중치, hidden/real-time 평가 방식
- [ ] 실격·금지 조건과 AI 도구 사용 범위
- [ ] 제출물 형식, 필수 파일, entrypoint, 제출 버튼의 실제 동작
- [ ] 입력 데이터 위치·schema·크기·예시
- [ ] 기대 출력 schema와 오류 형식
- [ ] 필수 사용자 흐름과 acceptance example
- [ ] 실행 환경의 Python/Node 버전
- [ ] 허용 포트, 시작 명령, Browser Preview 경로
- [ ] 패키지 설치, 인터넷, subprocess, 파일 지속성 제한

## P1: 첫 vertical slice 전 확인

- [ ] 평가 호출 횟수·속도 제한·비용
- [ ] 재고, 가격, 프로모션, 중복, 개인정보 제약
- [ ] seed·시간·메모리 제한
- [ ] 제출 후 수정 또는 재제출 가능 여부
- [ ] extension 조건

## Skills

- [ ] 어떤 AI가 업로드한 skill을 소비하는가
- [ ] 자동 discovery 또는 reload가 필요한가
- [ ] root `SKILL.md` 외 필수 manifest가 있는가
- [ ] 포함 스크립트 실행 권한과 cwd는 무엇인가

## MCP

- [ ] 지원 transport와 정확한 `.mcp.json` schema
- [ ] server command 실행 권한
- [ ] tool list를 확인하는 화면 또는 명령
- [ ] secret/env 주입 방법
- [ ] 변경 후 reload 필요 여부와 오류 로그 위치

## 제출 직전

- [ ] fresh process에서 시작 가능
- [ ] Preview에서 핵심 흐름 완주
- [ ] 테스트/validator exit 0
- [ ] champion과 제출 파일 해시 일치
- [ ] secret·cache·불필요한 대용량 파일 없음
- [ ] 제출 acknowledgement 보존
- [ ] 3분 답변용 결정·검증·한계 메모 준비
