# Design notes — why the institute looks like this

The owner asked on 2026-10-14 for an institute that takes the problems of 《10000个科学难题》 one
at a time: identify the problem, check the state of the art, spend a bounded quota on it, record the
result, then move on. These notes record the evidence and the decisions behind that shape. The
operating contract is `../README.md`, and the code is `../ri.py`.

## What came before

- **The v1 research institute** (2026-09-08 → 2026-09-20; archive in
  `~/jinleic-workspace/research-institute/`). It was a portfolio governor of about 12.5k lines with
  a launchd driver, a ranking formula, leases, receipts and settlement.
  - Of its 34 runs, 27% were operational failures.
  - In late runs only about 4% of wall time was compute; the rest was ceremony.
  - All 9 reviewed continue/pause decisions said "pause", so the driver starved itself and sat
    idle for 6 days.
  - It had no intake stage and no "already solved elsewhere" outcome.
  - Lesson: build the smallest loop that records an outcome for every visit.
- **The ai4s sessions** (now `../{mathematics,physics,information-science}/`) had strong
  verification habits: verbatim statements, independent checkers, hostile cross-vendor referees,
  Lean. Their weaknesses:
  - selection in batches of five, with no persistent queue and no per-problem quota;
  - the literature gate sometimes ran after the proofs, so SO(5) was proved and only then found to
    be pre-2009.

## Decisions

- **The cheapest gate runs first; "already solved" is a normal outcome.**
  - identify (no web, page images) → sota (web) → attack → replay → review → novelty.
  - Identify closes an article only when no question can be made precise. Famous problems still get
    a literature check, which is how Vaught's 2026 claimed counterexample was found.
- **Per-question verdicts.** One article can hold a settled question next to an open one (量子信道:
  additivity was refuted by Hastings 2009, while capacities remain open). Sota screens up to five
  questions and picks the attack target.
- **"Solved elsewhere" needs evidence.** The verdict stands only with an opened, peer-reviewed source
  that matches the exact question; otherwise it becomes a claim. The runner applies this check, not
  the model.
- **A frozen contract.** The target, the literature status and the acceptance criteria are hashed
  when an attack starts, including a requeued attack. The review judges against the contract.
  `solved`/`refuted` need a clean accept, headline scope and the referee confirming the question is
  settled.
- **A post-acceptance novelty search** addresses the SO(5) failure: prior art phrased in another
  convention. In the smoke test it turned a correct binary-codes result into Reproduction (Cordero
  2019).
- **One actor and one cross-vendor referee, not HMZ RLAR.** The codex actor runs in a sandbox. RLAR's
  reviewer must answer done:false on open problems, so all five ai4s runs stopped at the budget,
  with 0–3 reviews per hour at $17–28/h.
- **An append-only record.** `problems/<id>/record.json` logs attempts, outcomes and grants. The
  current stage is derived by folding pure decisions over that log; it is never stored. Evidence is
  never rewritten: `attack-e<epoch>/` accumulates.
- **Typed status; stop, don't poison.**
  - Only a usable artifact, or a stage running out of quota, changes a record.
  - Any other failure is retried once and then stops the run, leaving the problem open. A usage
    limit, auth failure or full subscription window therefore cannot cascade into 50 bogus outcomes.
- **Isolation.**
  - Executor work dirs live outside every repository, so no AGENTS.md/CLAUDE.md is loaded.
  - Claude runs `--safe-mode --restricted --strict-mcp-config` with an exact tool list, checked
    against the init event.
  - Codex runs with `--ignore-user-config --ignore-rules` and drops the user config's MCP servers,
    memories and auto-allow rules.
  - The sota and novelty stages have web but no shell. The attack has a shell but no web or network.
  - Claim replay uses a deny-IPC `sandbox-exec` profile. It was canary-tested: network, outside
    writes, `launchctl`, `osascript` and reading `~/.codex/auth.json` are all blocked.
- **ai4s coordination.**
  - `ai4s-owned.json` lists the 34 articles with a dossier or a cited solution.
  - A live guard skips any article an ai4s dossier names, without writing a record.
  - Inference-only judgments ("too hard") stay eligible.
- **Not campaign.py.** Visits are bounded screening records. A problem that deserves a long
  preregistered program graduates to a dossier or a campaign.

## How it was checked

| Check | Result |
|---|---|
| Codex independent design opinion and hostile spec review | adopted: SOTA-before-attack, frozen contract, per-problem budget; declined: v1-style launch machinery |
| Three spec critics (research quality, ops robustness, simplicity/policy) | per-question verdicts, image-first identify, novelty stage, typed status, process-tree watchdog, archive integrity |
| `/simplify` (reuse, simplification, efficiency, altitude) | stage table plus fold, contract as attack precondition, symlink-safe capped copies, plus 9 incidental bugs fixed |
| Live executor probes | the exact claude/codex flags; config bleed and `/tmp` write-root hazards found and closed |
| Contract tests (`tests/test_ri.py`, no model calls) | 33 pass |
| Live smoke test and blind calibration | [smoke-2026-10-14.md](smoke-2026-10-14.md): 4/4 visits, 6/6 calibration |

## Known limits

- A search miss is a dated result, and paywalled sources remain access holes.
- At most five precise questions per article are screened per visit.
- The referee cannot run code. Replay proves repeatability; the attack must ship an independent
  check and a negative control.
- `accept-with-fixes` is recorded as `unverified`. A `requeue --stage attack` continues from the
  previous deliverables with the referee's fixes in its prompt.
