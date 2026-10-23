# PA19 production plan v1: remaining lane-original M2 frontier (frozen proposal)

Written after the `/bin/date` reading 2026-10-19T03:50:54-0700 by ContinuePA19b. The machine-readable companion is `review/production-plan-v1.json`; this note summarizes it, and the JSON is the authority.

This is a planning document. No native run happens without a per-run parent GO; the parent launches and audits every run. Estimates are extrapolations from the cited measured receipts and are not results. Nothing here closes a case or says anything about PA(19,8,6).

## 1. Frontier

- **Current frontier:** parent frontier v4, `RUN/review/pa19-parent-frontier-v4.json` (5bc07039…). It has **143 = 80 ms06 + 63 ms09** lane-original M2 cases.
- **In flight, not accepted:** run-006 (`ms06:b00295:direct`). Runner-level UNSAT, settled 03:42:18; parent audit pending. If accepted, the frontier becomes 142 = 79 + 63.
- **The 79 other ms06 cases:**
  - 73 have never been attempted directly;
  - 6 are known direct timeouts under old CaDiCaL at 300 s: b68, b73, b74, b77, b151, b162.
- **ms09:** all 63 cases are open over their full frozen extend_b lists, 493,426 placements in total. Only b4 has old interval records. No accepted interval exists for any open ms09 case.
- **Never used here:** accepted cases are never rerun, and M2H denominators are never merged into this frontier.

## 2. Framework: no new runner

There are two reviewed item families. Each run of either family is an **item-only delta**: only ITEMS and the docstring scope lines change.

| Family | Base runner | Review and execution basis |
|---|---|---|
| ms06 DIRECT whole case (`build_v2`) | v17 `96e179a4…7566` | Codex r8 ready, no findings; executed as runs 004–006 |
| ms09 PLACEMENT INTERVAL (`build_partbatch` over the frozen list) | v16 `0ef4cfdc…170e` | Codex r7 (v14) plus constant-only v15/v16 diffs; executed as run-003 |

- **Why ms09 uses v16, not v17.** v17 replaced the partbatch generation and the ms09 skeleton. Running ms09 on v17 would revert that change, which is not item-only.
- **Why ms09 is not run directly.** Measured: the old ms09 b2 direct attempt was UNKNOWN at 477.6 s with a 1.19 GB proof.
- **Items per run: at most 3.** The prestart chunk fit is 2,960 + n × 2,450 + 180 s ≤ 10,800 s. Three items need 10,310 s; four would need 12,760 s and are refused.
- **No mixed-family runs.** Each runner has one skeleton constant and one generation path.
- **Latest runner start** (from the runner's own settle-by check against `owned_compute_settled_by` 2026-10-22T21:56:33-07:00):
  - 3-item runs: 2026-10-22T19:01:43;
  - 2-item runs: 19:42:33;
  - 1-item runs: 20:23:23.

## 3. Measured receipts used

All paths and SHA-256s are in the JSON.

- **ms06 direct, old CaDiCaL 300 s.** These are the first 33 cases of the hard queue in file order (`cycle2/m2-jobs-hard-direct.txt` 21fdc72f…).
  - 27 were solver-UNSAT: solve p50 37.6 s, max 223.5 s; proof p50 88.9 MB, mean 146.8 MB, max 505.9 MB.
  - 6 timed out, leaving partial proofs of 562–717 MB at 300 s.
- **Solve rate by |Aut(types)|:**

  | |Aut| | Solved / measured |
  |---|---|
  | 1 | 8/8 |
  | 2 | 13/15 |
  | ≥ 4 | 6/10 |

  M1 hard-direct times do not predict M2 outcomes: the M2 timeouts had M1 times anywhere from 39 to 2,140 s.
- **kissat 4.0.4 versus old CaDiCaL on the same 6 ms06 CNFs:** solve time ×0.80–1.26, proof size ×0.83–1.14. kissat writes proof at 2.0–2.4 MB/s.
- **kissat `--seed=1` is deterministic:** the same CNF gives a byte-identical proof. Examples: b5 [200..299] gives 478,666,919 B in both v6 and run-003; b70 [0..24] gives 4,634,811 B in both the calibration run and run-003.
- **ms09 partbatch, same-case B100 measurements (kissat):**
  - easy cases b9, b13, b20, b31, b55: solve 0.026–0.042 s per placement, check 0.015–0.076 s per placement, proof 57–97 KB per placement;
  - hard cases: b4 at 1.34 s and 3.41 MB per placement; closed b5 at 0.99–2.09 s and 2.3–5.2 MB per placement;
  - **57 of the 63 open ms09 cases have no same-case M2 measurement.**
- **Run wall times:** run-003 610 s, run-004 177 s, run-005 822 s. Controls take about 3 s.

## 4. Disk is the binding constraint

- **Budget:**
  - the per-lane new-disk ceiling is 10,737,418,240 B (`RUN/contract-v1.json`);
  - after run-006 the lane uses 1,983,483,904 B (du);
  - that leaves 8.75 GB.
- **GO accounting rule:** used + the run's worst-case retained reservation must stay ≤ the ceiling.
  - One item reserves about 1.305 GB; a 3-item run about 4.09 GB.
  - So 3-item runs need used ≤ about 6.65 GB, 2-item runs ≤ 7.94 GB, and 1-item runs ≤ 9.26 GB.
- **Dominant risk:** an UNKNOWN by timeout or proof cap keeps its partial proof, up to 1,258,291,200 B.
- **Projections by family** (planning extrapolations, JSON `estimates_planning_only`):

  | Class (never-attempted cases) | Expected closures | Expected bytes | Bytes per closure |
  |---|---|---|---|
  | ms06 \|Aut\|=1 (19) | 19 | 2.79 GB | 147 MB |
  | ms06 \|Aut\|=2 (28) | 24.3 | 8.79 GB | 362 MB |
  | ms06 \|Aut\|≥4 (26) | 15.6 | 15.4 GB | 987 MB |

  - For ms06, timeout waste dominates the cost from |Aut|=2 upward.
  - All ms09, if every case is easy: 28–48 GB of proofs and 21,000–55,000 s of solve plus check. If b4, b6 and b7 are hard they add 7.4–16.3 GB.
- **What fits:** a greedy order by expected bytes per closure, keeping one item's reservation as headroom, fits about **42 closures** (19 ms06 \|Aut\|=1 and 23 small ms09 cases). That would take the frontier from 143 to about 101, if the measured averages hold.

## 5. Order rules (frozen)

- **R0.** Never rerun an accepted case or interval, and never count M2H. Each item maps to exactly one lane-original case (ms06 whole case) or one exact [lo..hi] of one frozen ms09 list.
- **R1.** Work in order of expected bytes per closure:
  1. small-n ms09 cases whose measurement came back easy;
  2. ms06 \|Aut\|=1 never-attempted cases, in hard-queue file order;
  3. larger easy ms09 cases and ms06 \|Aut\|=2 cases;
  4. ms06 \|Aut\|≥4 and hard ms09 cases last.
- **R2.** Every unmeasured ms09 case starts with its B100 [0..99] measurement item.
  - The rest of its list becomes one item if the same-case rate predicts solve ≤ 200 s and proof ≤ 0.5 GB; otherwise it is split into equal chunks that meet both bounds.
  - This applies only if the b9 whole-list item (W1-R1) lands within 2× of its linear prediction for both solve time and proof size. If it does not, items stay at B100.
- **R3.** ms09 cases measured hard are deferred: B100 solve > 0.5 s per placement or proof > 1 MB per placement. b4 qualifies, at a predicted 1.74 GB.
  - b6 and b7 are not measured first. Like the measured-hard b4 and b5 they have 2 types and ≤ 2 empty rows. This is a structural hypothesis, not a measurement.
- **R4.** ms06 cases that end UNKNOWN are not retried directly. They join the 6 known timeouts for the Level-D/E split route, which is outside this plan (decision D3).
- **R5.** Runs alternate families (ms09, ms06, ms09, …) so ms09 measurements arrive early.
- **R6.** Stop proposing runs when the disk rule cannot admit even a 1-item run. Report what remains as UNDECIDED.

## 6. Wave 1 (frozen, CNFs pinned)

- **Pins:** `evidence/probes/production-wave1-pins-v1.json` (b8822c2c…). It was produced by `code/probe_production_wave1_pins_v1.py` (7e1f878a…), with a receipt recording PID 71187.
- **Checks passed:** every item is open in frontier v4; skeleton fields and list pins are equal; every ms06 item has never been attempted; the \|Aut\|-then-file-order rule reproduces the frozen ms06 list.

| Run | Family | Items | Reservation |
|---|---|---|---|
| W1-R1 | ms09 / v16 | b9 [0..814] (whole list, scaling test), b25 [0..99], b69 [0..99] | 4,093,264,344 B |
| W1-R2 | ms06 / v17 | b88, b89, b186 (direct) | 4,090,126,920 B |
| W1-R3 | ms09 / v16 | b10 [0..99], b67 [0..99], b11 [0..99] | 4,092,208,545 B |
| W1-R4 | ms06 / v17 | b154, b168, b169 | 4,090,113,891 B |
| W1-R5 | ms09 / v16 | b8 [0..99], b49 [0..99], b61 [0..99] | 4,092,208,647 B |
| W1-R6 | ms06 / v17 | b282, b299, b269 | 4,090,113,891 B |

- **Expected Wave 1 disk** (planning): about 1.5 GB. This is about 1.3 GB for the ms06 items plus 0.15–0.25 GB for ms09 if those cases are easy. Each hard B100 would add 0.23–0.52 GB, and each ms06 timeout 1.26 GB.
- **Expected native wall per run:** about 5–25 min for ms06 runs, about 1–5 min for easy ms09 runs.
- **Wave 2** is rule-based (R1–R6). Its items are pinned only after the parent accepts Wave 1.

## 7. STOP registry (current)

- **Inherited registry:** `evidence/inherited-stop-registry-v1.json` (ee370929…).
  - Its 9 live cycle2-root markers are preserved and pinned byte-for-byte by every runner.
  - The retired m2k3-HALT item (ms09 b5 [200..299]) is now parent-closed by run-003.
- **Binding items and how each is handled:**
  - F-A: the file transport checks that consumed bytes equal file bytes.
  - F-D: the parent's provenanced drat-trim build a46c0c71 replays every proof.
  - lrat-check: not used.
  - Disk floor: enforced by every admission gate.
- **New-round marker scan** (LANE/control and RUN/control) at 03:43:49: none.
- **Duplicate-literal disclosure** (`RUN/review/pa19-duplicate-literal-disclosure-v1.json`): no soundness effect.

## 8. Structural work

**No ms06 structural elimination is proposed.**
- GPS-1 excludes none of the open ms06 cases (67170e7b…).
- GPS-2|C1 leaves 1,443 of 10,459 b68 first-column placements feasible (12b4320e…). Block-level necessary conditions alone did not eliminate that case.
- GPS-1|C1 would prune 118,092 of the 493,426 open ms09 placements, about 24% (d82ddf38…). But applied GPS coverage is INCONCLUSIVE, and contiguous items cannot skip placements without an item-format change, so this is not used.

Any future elimination or pruning that shrinks the universe will be submitted as a standalone exact proof, with exact skeleton and list bindings, before it is used.

## 9. Parent decisions needed

- **D1 Disk ceiling.** About 42 closures fit within 10 GiB. The whole frontier needs roughly 30–50 GB for ms09 plus about 27 GB for ms06 direct attempts, including timeout waste.
- **D2 Optional constants-only variant:** PROOF_CAP about 0.6 GB and SOLVER_SECONDS 300.
  - All 27 measured solved ms06 directs fit (maximum 506 MB proof, 223 s solve).
  - It halves the timeout waste and the per-item reservation.
  - It needs one focused review, as v15 and v16 did.
- **D3 Split route** for ms06 timeouts (census `evidence/probes/ms06-split-census-v1.json`, c08cee17…). This is a generation change and needs review; disk per sub-case is unmeasured.
- **D4 ms09 GPS pruning** needs an accepted applied-coverage proof and an item format for placement subsets. Not proposed now.
