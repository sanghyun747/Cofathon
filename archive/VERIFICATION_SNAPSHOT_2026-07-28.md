# Cofathon Track 2 Preparation Verification

> 보관용 검증 스냅샷입니다. 당시 280분 프로필과 과거 agent-loop
> `1ef52bc...` observer를 검증한 기록이며, 현재 225분 kit 또는 G1
> 체크포인트의 검증 결과로 해석하면 안 됩니다.

Date: 2026-07-28 KST

## Reviewed artifacts

| Artifact | SHA-256 |
|---|---|
| `COFATHON_TRACK2_PREPARATION_2026-07-28.md` | `1da562fd923955fab267d04e202ce56069ba58603d1bccdc92aea77bf0b00c50` |
| `HACKATHON_AND_DOMAIN_EVIDENCE_2024_2026.md` | `03164a20559be59a0ccc51f19c22062a1c4900e425c07bb97428a8c9f28f02f6` |
| `contest-kit/contest_profile.json` | `9656be4b1a13187e0c8ec5e4a60c15eb10fc18860d1bedaac759174a682f5cd2` |

## Local contest-kit verification

- Python: 3.12.10.
- `python -m compileall -q scripts tests`: exit 0.
- `python -m unittest discover -s tests -v`: 4/4 PASS.
- `python scripts/preflight.py`: PASS, zero findings, phase total 280.
- `init_work.py`: required working tree created; a human edit survived a
  second initialization.
- Two separate deterministic builds were byte-identical:
  `e03fd7bf80de752865f54e24d24e31e08af4ae5d05fb2f64239095436192c52e`
  (9,445 bytes, 14 files).

## Fixed agent-loop verification

- Source code was exported from fixed commit
  `1ef52bc1aa3429a3e7650bafb50690536dd9f023`; the dirty live checkout was not
  switched or modified.
- Focused fixed-source tests:
  `test_goal_monitor.py` + `test_process_liveness.py`: 17/17 PASS.
- Run 01 used Codex CLI 0.145.0 and was correctly classified `UNVERIFIED`.
  The provider had added `cache_write_input_tokens` to terminal usage while the
  frozen parser accepts the exact earlier four-field contract. The valid
  no-veto model response and the failed receipt are preserved; this run is not
  counted as a review pass.
- Run 02 used the preserved compatible Codex CLI 0.144.6 with actual
  `gpt-5.6-terra`, high reasoning, ephemeral/read-only mode, disabled tools,
  and the same evidence hash.

Run 02 acceptance:

- `execution_status`: `VERIFIED`
- evidence bundle SHA-256:
  `cf81a312a41b19b6662659339644771187bab93baea0f774175ce445f748b65b`
- `unresolved_veto_ids`: `[]`
- tool calls: 0
- write side effects: 0
- external side effects: 0
- recommendation: `NO_VETO_BUT_NOT_COMPLETION_AUTHORITY`
- receipt SHA-256:
  `5025ff73c3c7793e5bc0783dd3a8b31f8d0a14261a2a537eddb7809218e63e73`

The CLI emitted a model-cache compatibility warning on stderr, but returned
exit 0 and a schema-valid provider receipt. It did not affect the accepted
verdict.

## Claim ceiling

- The observer reviewed only the embedded evidence and could not browse source
  URLs.
- The model-version source in the receipt is the requested versioned identifier
  plus provider execution receipt, not hardware-level attestation.
- The observer has no completion authority.
- Exact Track 2 weights and hidden task remain unknown until the 11:00 briefing.
- The D-1 full 280-minute mock remains a participant readiness gate and is not
  represented as completed.
- The broader Outcome Engine V2 R5 and provider/model superiority remain
  unfinished/unmeasurable and are not on the contest critical path.
