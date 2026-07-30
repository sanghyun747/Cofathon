# Olive Better MD Automation MVP

운영자가 웰니스 기획 요청을 입력하면 공개 검색 근거, 안전 상품, 대표 배너와
고객 화면 구성을 자동으로 만들고 검토·수정·발행하는 MVP입니다. 고객은 발행본만
조회하며 상세·좋아요·모의 구매 반응을 남길 수 있고, 이 반응은 다음 초안의 상품
점수와 영역 순서에 다시 반영됩니다.

## 빠른 실행

```bash
npm test
npm start
```

- 운영자: `http://127.0.0.1:5173`
- 고객: `http://127.0.0.1:5173/customer.html`

외부 LLM 연결 없이 기능 데모를 실행하려면 명시적으로 데모 모드를 켭니다.

```powershell
$env:OLIVE_MVP_DEMO_MODE='1'
npm start
```

운영 환경에서는 서버 프로세스에 `OPENAI_API_KEY`와 필요 시
`OPENAI_BASE_URL`, `OPENAI_MODEL`을 설정합니다. 키 값은 브라우저나 저장소에
넣지 않습니다. 연결 실패나 잘못된 응답은 발행 가능한 성공으로 처리하지 않습니다.

상품 데이터의 출처와 한계는 [`data/PRODUCT_DATA_PROVENANCE.md`](data/PRODUCT_DATA_PROVENANCE.md)에
기록했습니다.
