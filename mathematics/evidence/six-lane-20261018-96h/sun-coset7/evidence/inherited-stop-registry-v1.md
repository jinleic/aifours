# Inherited STOP / HOLD / OPEN registry, math-1 sun-coset7 (96-hour continuation), v1

- Written: `/bin/date` read immediately before this exclusive write: 2026-10-18T23:19:02-0700.
- Scope: inventory only. No old file was modified; every old path below was read, not written.
- Pins re-hashed at 2026-10-18 23:01-23:04 PDT (`shasum -a 256`), all equal to the pins in the new run's
  `inputs/prior-evidence-manifest-v1.json` and in LANE-SUMMARY-v3 section 1.

## 1. Target (unchanged)

Sun 2006 Conjecture 1.2 at k = 7 for EVERY group: seven pairwise disjoint LEFT cosets of finite-index subgroups
(subgroups possibly equal, no cover assumption) force gcd([G:U_i],[G:U_j]) >= 7 for some i < j.
Old binding contract: `institute/runs/six-lane-2026-10-16/screening/math-1-sun-coset7-contract.json`
(frozen 2026-10-18T13:01:42-07:00; its cutoffs are STALE and are not used).

## 2. Class ledger inherited from the closed round

| class | inherited status | controlling record (sha256) |
|---|---|---|
| K5.2* (incl. D2') | EXCLUDED, computer-assisted, CORRECTNESS-ACCEPTED; permanent process MAJOR F-1 | sun-coset7-stageB-classes-parent-verdict-v1.md fd14952c...3c13f |
| KII | EXCLUDED, same verdict and same F-1 | same |
| K5.3 | OPEN (NOT PROMOTED). Held for terminal-stop/publication defect of checker v1; repair checker_v2 frozen, runtime NOT_STARTED in the old round | sun-coset7-stageA-parent-hold-verdict-v1.md 10cefa4b...0ec1 |
| K7 | OPEN. Accepted written sub-results only (structure, BLOCK/PAIR, Q5+, unmarked) | verdicts 2154c317..., cc214b58..., 38ec128d..., 463e0a45... |
| K6.2* | OPEN. No accepted sub-result beyond the README class definition | written verdict 73a25ba6... |
| K6.3 | OPEN. Partial D3 only (C cap E empty and >= 4 alpha_di = 2) | written verdict 73a25ba6... |

## 3. Inherited STOP / HOLD / NOT_STARTED items

| item | kind | inherited state | disposition in this round |
|---|---|---|---|
| StageA checker v1 terminal-stop/publication defect (Codex MAJOR, note 81ab8c60...) | correctness/safety defect of the CHECKER publication path, not of the mathematics | repair checker_v2 5b285da4... frozen; controls + positive replay NOT_STARTED | Parent-owned. Parent IRC (this round): parent ran the frozen 9 v2 controls, 7 v1 sensitivity runs and positive v2 replay under its own review output `RUN/review/sun7-stageA-v2-qualification-v1/`; reported all as frozen, positive normal exit 0, COMPLETE_VALID, no marker. Parent audit and NEW K5.3 disposition PENDING. This lane launched nothing for StageA and does not count K5.3 as promoted. |
| Old resource HOLD (free disk 4,384,600,064 B at 16:39:56 PDT) | closed-round disk stop | expired with the old round | Not a correctness defect. Fresh disk at 23:03:40 PDT: 198,766,800,896 B (statvfs). |
| `RESULT-v2-HOLD.json` (7da8d5a1...) | worker HOLD receipt | preserved | read-only record; superseded only by parent's new outputs |
| F-1 late CERT-FORMAT / RPLP freeze | permanent process MAJOR | permanent | retained verbatim; no new result relabels it |
| v1 defect history (C1-C5 false PASS on v1) | permanent | permanent | retained; parent reports v1 sensitivity reproduced it |
| Stage C NO-GO (5cd8a2b6...) | parent NO-GO | engine v4, admission_v2, stageC_launch_v4, smoke_v4_v2, terminal_probe_v1 frozen NOT_STARTED | NOT restarted. Any K62/K63/K7 computation needs a new frozen spec, certificate format, independent checker and item-specific parent GO (F-4). |
| K7-enumeration-spec-v1 (e5aa176b...) | spec with superseded family convention | never executed | not used (X1 convention required) |
| FH (L5 with L6 subgroup source, 7-piece use) | UNUSED rule | UNUSED | still unused as an executable rule. NOTE: the new Lemma LFC of this round applies L5 only with H = U_v, where every fibre holds at most six pieces; no Sun(7), no least-order frame. |
| Old wrappers / launcher v2 process-cap deviation | disclosed deviations | permanent | retained |

No FIFO, STOP-file or CANCELLED marker exists in the old lane or in the old StageA/StageB review directories
(`find ... -iname '*stop*' -o -iname '*hold*' -o -iname '*cancel*' -o -type p` returned only RESULT-v2-HOLD.json).

## 4. What remains OPEN at the start of this round

K7, K6.2*, K6.3 (written frontier as in LANE-SUMMARY-v3 section 3), and K5.3 pending the parent disposition.
No Sun(7) theorem, counterexample or novelty claim is inherited.
