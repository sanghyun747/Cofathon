# Cofathon Track 2 TODO

## 동기화

- [x] 원격 main 기반 격리 worktree 생성
- [x] 이관 범위와 제외 기준 확정
- [x] 문서·contest-kit·고유 스크린샷 반영
- [x] contest-kit compile/test/preflight 검증
- [x] stale timing·secret·중복 파일 검사
- [x] commit과 origin push
- [x] 노트북용 pull/restart 경로 확인

## 과제 공개 후

- [ ] `docs/KNOWN_UNKNOWNS.md` P0 채우기
- [ ] task contract 고정
- [ ] 실제 input/output validator 구현
- [ ] Browser Preview smoke 구현
- [ ] baseline/candidate/champion ledger 연결
- [ ] submission freeze와 receipt 검증

## Review

- 브랜치: `cofathon-track2-sync-20260730`
- `python -m compileall -q contest-kit\scripts contest-kit\tests`: PASS
- `python -m unittest discover -s contest-kit\tests -v`: 4/4 PASS
- `python contest-kit\scripts\preflight.py`: PASS, phase total 225
- 결정적 ZIP: 두 빌드 SHA-256
  `7f6d6cf46fa3fc7cf5db939bd533a9d177a7b0c5432652c6b28a1c9b33cb7735`
- secret pattern: no matches
- 스크린샷: 고유 해시 5개, 중복 대기실 이미지 제외
- WSL 교차 검증은 이 Windows 호스트에 WSL 배포판이 없어 실행하지 못함
- 원격 main에 포함된 content checkpoint:
  `d781fd7031fe0d96755e1fa03096bfbd612f19d2`
- 새 shallow clone의 HEAD가 위 커밋과 일치했고 같은 preflight와 4/4
  tests가 다시 PASS했다.
- G1 annotated tag가 원격에 게시됐고 peeled commit이
  `2894c968ffd1686f3a26576b4efbaf0fb7c38080`임을 `ls-remote`로 확인했다.
