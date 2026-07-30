# 웹 IDE, Skills, MCP 사용 안내

## 화면별 역할

| 화면 | 하는 일 | 성공 판정 |
|---|---|---|
| Explorer | 앱·하네스 파일 생성, 저장, 업로드 | 저장 후 파일이 다시 열리고 내용이 유지됨 |
| Terminal | 앱 서버, 테스트, CLI 실행 | 명령 종료 코드와 출력이 기대값과 일치 |
| Browser Preview | 지정 포트와 경로의 웹 앱 확인 | 실제 사용자 흐름과 오류 처리가 브라우저에서 동작 |
| 내장 AI 채팅 | 과제 해석·코드 요청·검토 보조 | 코드와 검증 결과로 확인 |
| Skills | AI에 반복 가능한 지침·워크플로를 제공 | 특정 AI가 skill을 발견·선택·적용했음을 별도 확인 |
| MCP | AI가 외부 도구 서버의 tool을 호출하도록 연결 | 서버 시작, tool 발견, 권한, 실제 호출까지 확인 |

사전 체험의 Preview 예시는 포트 `3000`, 경로 `/`입니다. 실제 과제의
포트나 entrypoint라는 뜻은 아닙니다.

## Skills 화면은 무엇인가

Skills는 라이브러리 설치 화면이 아니라 AI가 따를 작업 지침 묶음을
등록하는 화면입니다. 업로드하는 폴더의 루트에 `SKILL.md`가 있어야
한다는 것까지만 스크린샷으로 확인됐습니다.

아직 모르는 사항:

- 내장 AI 채팅, Claude Code, Codex 중 누가 해당 skill을 읽는지
- 업로드 직후 자동 발견되는지, reload가 필요한지
- 함께 들어 있는 스크립트를 실행할 권한과 working directory
- 여러 skill이 충돌할 때 우선순위

허용 정책과 시간이 충분할 때의 최소 확인 순서:

1. 부작용 없는 작은 skill 폴더를 업로드합니다.
2. Skills 목록에 나타나는지 확인합니다.
3. 사용할 AI에게 skill 이름을 명시해 작은 marker 작업을 요청합니다.
4. 응답 문구가 아니라 실제 생성 파일·명령 로그로 적용 여부를 확인합니다.
5. 실패하거나 2~3분 안에 원인이 드러나지 않으면 사용하지 않습니다.

현재 데스크탑의 AGENTS 정책은 built-in `.system` skill만 허용합니다.
노트북에서도 해당 정책을 먼저 확인해야 하며, 정책을 명시적으로
바꾸지 않는 한 custom agent-loop skill을 업로드하지 않습니다.

## MCP 화면은 무엇인가

MCP는 AI와 도구 서버 사이의 통신 설정입니다. 화면의 `.mcp.json`은
다음 최상위 구조를 보여 줍니다.

```json
{
  "mcpServers": {}
}
```

일반적인 로컬 명령형 서버는 다음과 비슷하지만, 정확한 필드와 transport는
플랫폼 문서를 확인해야 합니다.

```json
{
  "mcpServers": {
    "example": {
      "command": "실행파일",
      "args": ["서버 스크립트 경로"]
    }
  }
}
```

`저장` 성공은 JSON이 보존됐다는 뜻일 뿐 다음을 증명하지 않습니다.

- 서버 프로세스가 실제로 시작됨
- AI가 tool 목록을 발견함
- 인증과 권한이 통과함
- harmless read-only tool 호출이 성공함
- 실패 로그를 참가자가 볼 수 있음
- working directory와 환경변수가 올바름

MCP를 사용하려면 위 항목을 순서대로 smoke해야 합니다. API key나
토큰을 `.mcp.json`에 직접 적지 말고, 플랫폼이 제공하는 secret/env
주입 방식이 확인된 경우에만 사용합니다.

현재 데스크탑 정책의 MCP allowlist는 `agent-browser`와
`cloakbrowser`뿐입니다. 행사 UI가 더 많은 MCP를 기술적으로 받아도
로컬 정책과는 별개입니다.

## 실전 권장 결론

- Explorer에 Linux 호환 mini task harness와 앱 파일을 올립니다.
- Codex Goal 하나만 구현을 지휘하게 합니다.
- Terminal에서 테스트와 서버를 실행합니다.
- Browser Preview에서 실제 입력→출력 흐름을 확인합니다.
- Skills는 정책과 소비 주체가 확인될 때만 사용합니다.
- MCP는 필수인 사전 검증 도구가 있을 때만 연결합니다.
- agent-loop를 MCP로 감싸지 않습니다. CLI/스크립트로만 조건부 사용합니다.
