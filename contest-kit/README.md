# Cofathon Contest Kit

This is a small, standard-library-only starter harness for the confirmed
225-minute Cofathon task window. A separate three-minute question follows
submission and affects evaluation.

It does not solve the hidden task and does not assume an undocumented Probe API.
It provides fixed timeboxes, task/evidence templates, a secret-aware preflight,
and deterministic ZIP creation.

## Before the event

```powershell
python scripts/preflight.py
python scripts/init_work.py --output ..\work
python scripts/build_bundle.py --output ..\cofathon-contest-kit.zip
python -m unittest discover -s tests -v
```

Linux/macOS:

```bash
python3 scripts/preflight.py
python3 scripts/init_work.py --output ../work
python3 scripts/build_bundle.py --output ../cofathon-contest-kit.zip
python3 -m unittest discover -s tests -v
```

## At task admission

1. Copy official criteria verbatim into a new `work/problem.md`.
2. Confirm environment/network/package/subprocess/secret rules.
3. Change weights or exit criteria in `contest_profile.json` only if necessary.
4. Do not add a new framework before inspecting the actual repository and data.

## At task start

Initialize a writable directory with `scripts/init_work.py`. It is idempotent
and will not overwrite files you already edited. Create the baseline before
starting model or architecture expansion. Preserve the accepted result under
`champion/`; never overwrite it with an unverified candidate.

The base schedule does not assume that an optional extension will be granted.
Keep the final 10 minutes for submission and keep a short decision record ready
for the three-minute post-submission question.

## Agent-loop integration

Use Codex Goal as the only controller. When the hosted Linux environment passes
a bounded smoke test for the pinned G1 runtime, map the templates to its task,
gate, candidate, limitation, and deliverable records. Use G1 only as a
pre-completion/final frozen audit, not as another live controller.

When it does not support agent-loop, use these files manually. Do not spend
contest time installing or porting the full controller.

The harness intentionally keeps human gates at:

- task/metric freeze;
- baseline acceptance;
- champion promotion;
- final feature freeze and submission.
