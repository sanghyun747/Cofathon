# Cofathon Track 2: Olive Young AI Engineer Preparation

> 보관용 스냅샷입니다. 이 문서의 280분·11:30~16:10 가정은 이후
> waiting-room 화면에서 확인한 225분과 충돌합니다. 실제 운영에는
> 상위 디렉터리의 `README.md`와 `docs/CONTEST_DAY_RUNBOOK.md`를 사용하세요.

Date: 2026-07-28 KST
Event: 2026-07-30, PUBG Seongsu
Build window: 11:30-16:10, 280 minutes

## Executive decision

The winning posture is not “use the largest model” or “generate the most code.”
It is:

1. define the Olive Young business objective and data contract correctly;
2. produce a working baseline early;
3. improve it against a reproducible evaluator;
4. preserve the best known result and recover from failure;
5. make the AI steering, engineering decisions, limitations, and business impact
   explainable.

This follows the event's working-output and real-time Probe format and Olive
Young's disclosed Cofa-Probe evaluation model. The four preparation axes are:

- Technique: executable output, maintainability, scalability, and security.
- Intent: objective/constraint definition, decomposition, delegation, and
  validation loops.
- Cognition: understanding and explaining the structure, behavior, trade-offs,
  and risks.
- Communication: eliciting requirements, prioritizing, and redefining the
  problem clearly.

The exact Cofathon weights and hidden task are not public. The four axes are a
high-confidence preparation proxy because Olive Young's AI-First recruitment
uses the same Cofa-Probe concept, real-domain task, web IDE/real API environment,
and end-to-end activity capture.

Official references:

- [Cofathon event](https://cofathon.getcofa.com/#tracks)
- [Olive Young AI-First Track and four-axis evaluation](https://career.oliveyoung.tech/)

## What the last two years show

The normalized evidence is in
[`HACKATHON_AND_DOMAIN_EVIDENCE_2024_2026.md`](HACKATHON_AND_DOMAIN_EVIDENCE_2024_2026.md).
The actionable findings are:

1. Completion is a differentiator. Microsoft's 2025 AI Agents Hackathon had
   18,000+ registrations but 570 submissions; AWS PartyRock had 7,650
   registrants and 1,200+ submissions. These ratios are not directly comparable
   to an onsite finalist event, but they show that a complete, valid delivery is
   rarer than registration or ideation.
2. Real business workflow wins over generic chat. The Microsoft overall winner
   joined supply-chain data, news, tools, an agent backend, SQL, and an analyst
   UI. Meta's winner embedded AI in frontline triage rather than presenting an
   isolated model.
3. Automated scoring needs a human-readable defense. AWS LLM League used an
   LLM judge and later a 40% LLM / 40% expert / 20% audience final. A correct
   answer was misclassified in the final, demonstrating the need for invariant
   tests and a clear explanation rather than blind score chasing.
4. Late scope expansion is dangerous. In Olive Young's own two-hour GenAI
   hackathon, some teams could not finish service integration or recommendation
   logic and had to narrow the demo or hardcode a path.
5. Olive Young rewards explicit quality criteria. Its production AI records
   repeatedly define a baseline, a task-specific evaluator, edge cases,
   operational constraints, and human review.
6. The closest short-format analogue, Useful Agents 2025, put 30% on task
   completion/benchmarks and 30% on UX, ahead of 20% each for technical novelty
   and presentation. A reproducible baseline, success metric, and usable path
   therefore deserve the first hours, not the last.
7. Iteration must be bounded. ARC Prize 2025 disclosed a refinement harness
   moving a baseline from 31% at $0.81/task to 54% at $31/task—about 38 times
   the cost. This supports the two-non-improvement stop rule and champion
   preservation below; it does not prove that the same score/cost curve applies
   to Cofathon.

## Most likely problem families

These are evidence-based hypotheses, not leaked tasks.

| Priority | Problem family | Why it is likely | Minimum credible solution |
|---|---|---|---|
| 1 | Recommendation/search/ranking | The AI-First role centers on candidate retrieval, serving, offline evaluation, online simulation, A/B testing, and monitoring | Deterministic baseline, chronological validation, ranking metric, cold-start fallback, inventory/business constraints |
| 2 | Review/catalog/content intelligence | Olive Young has public systems for review themes, review tagging, image validation, and catalog operations | Schema-bound output, edge-case set, deterministic settings, confidence/fallback, latency/cost record |
| 3 | Customer/promotion/CRM | Membership, promotion, consent, and real-time campaign data are core omnichannel assets | Freshness and consent constraints, segment baseline, bounded retry, no duplicate action |
| 4 | Inventory/logistics/operations | Public work covers Kafka OMS, inventory, MFC, allocation, address validation, and delivery | Idempotency, missing/out-of-order data handling, simulator or rule baseline, operational KPI |
| 5 | Global commerce | 150+ countries, multilingual product/customer context, address and market differences | Locale-aware validation, terminology normalization, graceful unsupported-country fallback |
| 6 | AI operations/back office | Olive Young's AI-DLC trials included incident/compensation orchestration and legacy modernization | AS-IS/TO-BE boundary, audit trail, human approval, safe partial automation |

## Recommendation-track playbook

### First 15 minutes

Write the following before choosing a model:

- Query: user, keyword, item, brand, basket, or context?
- Value: item, category, theme, content, or action?
- Label/objective: click, purchase, co-view, similarity, relevance, or business
  utility?
- Unit of evaluation: event, user, session, query, item, or time window?
- Hard constraints: inventory, eligibility, duplicate suppression, price,
  promotion, locale, privacy.
- Offline metric and business proxy.
- Data split and leakage risks.

Olive Young's ItemLM account explicitly frames recommendation as
`Query × Value → Label` and identifies label design, quantitative validation,
and cold start as the central problems.

### Baseline ladder

Use the first working option that fits the provided data:

1. global or segment popularity with deterministic tie-breaking;
2. item-item co-occurrence or co-visitation;
3. metadata/ingredient/attribute TF-IDF or one-hot cosine similarity;
4. simple candidate retrieval plus lightweight reranking;
5. embedding or learned ranker only if the evaluator and time budget justify it.

Do not start with fine-tuning. A simple baseline makes later claims measurable
and guarantees a fallback.

### Evaluation defaults

- Use a chronological or leave-last-interaction split when timestamps exist.
- Report at least one ranking metric: Recall@K, NDCG@K, MRR@K, or MAP@K as
  appropriate.
- Add catalog coverage and duplicate/invalid-item rate.
- Add cold-start slices for new users, new items, and missing attributes.
- Measure p50/p95 latency or total batch wall time and peak memory.
- Validate inventory/eligibility/locale constraints separately from ranking.
- Record score, wall time, configuration, seed, and artifact hash for every
  accepted experiment.

### Senior-level risks to state explicitly

- exposure and click bias;
- leakage from future interactions;
- popularity feedback loops;
- missing attributes and new products;
- stale inventory/promotion state;
- low diversity or category collapse;
- privacy and unnecessary PII;
- offline metric not equaling CTR/CVR or margin;
- model/API timeout and malformed output.

## Agent-loop contest profile

Use the existing agent-loop as a bounded controller and evidence ledger, not as
an opaque autonomous black box.

### Allowed reliance

- plan/task/checkpoint/evidence state;
- exact task and gate transitions;
- preserving the best accepted artifact;
- deterministic local oracles;
- pause/resume/steer and explicit limitations;
- fresh read-only completion audit when the environment supports it.

The local agent-loop basis audited for this preparation is the fixed code
commit `1ef52bc1aa3429a3e7650bafb50690536dd9f023`, with the Windows liveness
checkpoint tag
`checkpoint/outcome-engine-v2-r5-windows-liveness-final-20260727`. Its
read-only goal monitor is suitable for an auxiliary veto review. The current
live checkout is intentionally not used because it contains later, moving work.
The observer can say that no supported veto remains in a supplied evidence
bundle; it cannot authorize completion.

### Do not put on the critical path

- unfinished Outcome Engine V2 R5 claims;
- unmeasured provider/model superiority;
- a new credential or provider integration;
- multiple heavy workers;
- a long self-hosting or external certification run;
- assumptions that the Probe environment exposes local process or filesystem
  features not confirmed at 11:00.

The broader Outcome Engine V2 R5 campaign is not represented as complete:
commit-point reconciliation, a crash matrix, three self-host work items,
G0-G8, clean final reproduction, and external certification remain outside the
trusted contest path. Model/provider superiority is also `NOT_MEASURABLE`.

### Contest policy

- One active heavy worker. A second process is allowed only for a bounded
  evaluator.
- Human steering gates at minute 15, baseline pass, champion selection, and
  final freeze.
- Preserve `champion/` separately from `candidate/`.
- Two consecutive non-improving experiments force a new hypothesis or rollback.
- No new model family after minute 180.
- No new feature after minute 225.
- Champion freeze at minute 250.
- Submission bundle must be reproducible by minute 270.
- The final 10 minutes are submission buffer, not development time.
- If agent-loop cannot run inside Probe, retain the same files and gates
  manually; do not spend contest time porting the controller.

## Exact 280-minute timeline

| Clock | Minutes | Goal | Exit gate |
|---|---:|---|---|
| 11:30-11:45 | 15 | Intake, data/API inspection, business objective, metric, NFR, non-goals | `problem.md` and acceptance criteria frozen |
| 11:45-12:15 | 30 | Smallest end-to-end baseline | One valid output and local evaluator PASS |
| 12:15-13:30 | 75 | Complete vertical slice, API/CLI integration, error handling | Working result with baseline receipt |
| 13:30-14:30 | 60 | Highest-value measured improvement | Champion beats baseline on same evaluator |
| 14:30-15:15 | 45 | Cold start, malformed input, timeout, latency, security | Robustness matrix and fallback PASS |
| 15:15-15:40 | 25 | Remove unstable scope, regression, explanation artifacts | Feature freeze and champion selected |
| 15:40-16:00 | 20 | Clean run, package, hashes, debate card | Fresh reproduction and bundle PASS |
| 16:00-16:10 | 10 | Upload, verify acknowledgement, preserve receipt | Submission confirmed |

If a working baseline is not ready by 12:15, stop architecture expansion and
use the simplest deterministic path. If no measured improvement exists by
14:30, ship the baseline plus robustness and explanation rather than a fragile
candidate.

## Harness structure to bring

The portable starter kit in `contest-kit/` is intentionally standard-library
only and Probe-schema agnostic:

```text
contest-kit/
  README.md
  contest_profile.json
  task_contract.template.json
  run-receipt.template.json
  templates/
    problem.md
    data-audit.md
    experiment.md
    decision.md
    risk-register.md
    debate-card.md
  scripts/
    init_work.py
    preflight.py
    build_bundle.py
  tests/
    test_contest_kit.py
```

The kit is not a hidden-task solver. It supplies:

- fixed timeboxes and stop rules;
- a task and acceptance contract;
- an idempotent working-directory initializer that preserves human edits;
- traceable experiments and decisions;
- secret scanning and deterministic bundle creation;
- a fast fallback if agent-loop cannot run in the hosted IDE.

### Files to produce during the event

```text
work/
  problem.md
  data-audit.md
  baseline/
  candidate/
  champion/
  experiments.jsonl
  decisions.md
  risks.md
  test-results/
  run-receipt.json
  debate-card.md
  submission/
```

### Required run receipt fields

- task and configuration version;
- source/data hashes where permitted;
- exact command and exit code;
- metric name, value, split, seed, and sample count;
- wall time and peak memory if available;
- accepted champion hash;
- failed checks and known limitations;
- secret scan and submission acknowledgement.

## 11:00 scoring-rule adaptation

At the opening, transcribe the official criteria verbatim. Do not reinterpret
them immediately. Then update only the weights and exit gates:

| Official emphasis | Immediate response |
|---|---|
| Correctness/hidden score | Narrow scope, lock evaluator, prioritize data leakage and invalid output checks |
| Latency/cost | Add caching/batching, use smaller deterministic baseline, measure p95 and total cost |
| Robustness/security | Allocate the 14:30 block early; add malformed/empty/timeout/injection tests |
| Business impact | Tie the metric to CTR/CVR/VOC/lead time/operational hours; keep a simple end-user flow |
| AI Native/process | Make steering, rejected alternatives, verification, and human decisions explicit |
| Creativity/novelty | Keep baseline; spend only one bounded improvement block on differentiation |

Do not rewrite the whole harness after the opening. The official page already
permits a local harness; its purpose is to absorb rule changes through config.

## D-2, D-1, and event-day checklist

### D-2 — 2026-07-28

- [ ] Read the Cofathon and Olive Young AI-First pages once end to end.
- [ ] Memorize the four axes and their evidence.
- [ ] Run `python scripts/preflight.py` from `contest-kit/`.
- [ ] Build and inspect the deterministic upload ZIP.
- [ ] Practice one recommendation baseline and evaluator on a small public or
      synthetic dataset.
- [ ] Practice explaining Query, Value, Label, split, metric, and cold start in
      under 90 seconds.
- [ ] Run a 45-minute micro-drill: intake 5, baseline 10, one improvement 15,
      hardening 8, package 5, upload simulation 2.
- [ ] Verify laptop power, charger, network fallback, browser, editor, Git,
      Python, and Korean/English keyboard input.
- [ ] Keep API keys outside the bundle and prepare only environment-variable
      names, never plaintext secrets.

### D-1 — 2026-07-29

- [ ] Run one full 280-minute mock under the exact timeline.
- [ ] Use a synthetic commerce task if no suitable public dataset is ready:
      rank eligible items for sessions with stock, locale, and duplicate
      constraints; inject unseen users/items and malformed rows.
- [ ] Inject one malformed-data failure, one evaluator mismatch, and one
      timeout/API failure.
- [ ] Require a fresh environment run of the champion and bundle.
- [ ] Rehearse the debate card with no slides.
- [ ] Fix only P0/P1 failures after the mock; no new framework.
- [ ] Rebuild the ZIP and verify its SHA-256.
- [ ] Sleep; do not spend the submission buffer in advance through fatigue.

### Event arrival

- [ ] Arrive with charger, mouse, hotspot, ID/invitation, and the verified ZIP.
- [ ] Check internet, power, browser download/upload, terminal, Python version,
      writable path, and available disk/memory.
- [ ] Confirm whether external network, packages, Git, subprocesses, and
      environment variables are allowed.
- [ ] Confirm whether Probe records harness-originated AI calls and where scores,
      logs, and submission receipts appear.
- [ ] Do not start a heavy process until resource limits are known.

### 16:00 submission gate

- [ ] Champion, not latest candidate, is packaged.
- [ ] One clean run passes.
- [ ] Required filename/schema/entrypoint is exact.
- [ ] No `.env`, tokens, credentials, personal data, caches, virtualenv, model
      weights, or unnecessary logs are included.
- [ ] Upload completes and acknowledgement is visible.
- [ ] Receipt/screenshot/hash is preserved if rules permit.

## Debate card

Prepare direct answers to:

1. Who is the user, what is the loss, and why is this metric a valid proxy?
2. What was the trivial baseline and how much did the champion improve?
3. How did you prevent temporal leakage, exposure bias, or invalid labels?
4. What happens for a new user/item or missing attributes?
5. What happens when the model/API is slow, unavailable, or returns bad output?
6. Why this model, architecture, and threshold under a 280-minute constraint?
7. What did AI propose incorrectly, and how did you detect and correct it?
8. Which data was deliberately not stored or used?
9. What is the first production experiment: A/B test, online simulator, or
   shadow traffic?
10. What is still unproven?

## Go/no-go definition

Ready means:

- a valid upload bundle exists and passes preflight;
- one 280-minute mock finishes with at least 10 minutes submission reserve;
- champion recovery succeeds after a forced failure;
- the evaluator is deterministic on repeated runs;
- the four-axis evidence can be shown from artifacts;
- every metric claim has a split, sample count, and reproducible command;
- the debate card can be answered without relying on AI.

Anything less is `NOT_READY`, even if a visually impressive demo exists.
