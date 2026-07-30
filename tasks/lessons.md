# Lessons

- waiting-room에서 확인된 225분은 과거 공개 일정으로 추정한 280분보다
  우선한다. 시간 프로필과 preflight를 함께 바꿔야 한다.
- Skills 업로드와 `.mcp.json` 저장은 capability activation 증거가 아니다.
  discovery, process start, tool list, 권한, 실제 호출을 따로 검증한다.
- G1은 대회 controller가 아니라 materialization custody 감사
  체크포인트다. Codex Goal과 같은 task를 동시에 drive하지 않는다.
- PowerShell `foreach (...) { ... } |`는 parser error를 반복시켰다.
  항상 `$rows`에 결과를 모은 뒤 별도 문장에서 파이프한다.
