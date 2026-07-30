# Wins

## 2026-07-30 · 225분 contest-kit 검증

- `contest_profile.json`, `preflight.py`, 단위 테스트를 함께 225분으로
  바꿔 stale 280분 계약이 남지 않게 했다.
- `python -m unittest discover -s contest-kit\tests -v`가 4/4 PASS했다.
- `python contest-kit\scripts\preflight.py`가 phase total 225로 PASS했다.
- 두 번 생성한 ZIP의 SHA-256이
  `7f6d6cf46fa3fc7cf5db939bd533a9d177a7b0c5432652c6b28a1c9b33cb7735`
  로 일치해 bundle 결정성을 재현했다.
- 고유 스크린샷 5장의 해시를 manifest와 다시 대조했다.

## 2026-07-30 · 원격 인계 재현

- 원격 main을 새 shallow clone한 HEAD가 source commit
  `d781fd7031fe0d96755e1fa03096bfbd612f19d2`와 일치했다.
- clean clone에서 preflight와 4/4 tests가 다시 PASS했다.
- 원격 annotated G1 tag의 peeled commit을 `git ls-remote`로 확인했다.
