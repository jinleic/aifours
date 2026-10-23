# info-1 PA(19,8,6) — 96-hour continuation lane

Frozen after `/bin/date` read 2026-10-18T23:20:20-0700, before any new search. Owner: ContinuePA19 (this lane path only). Parent declared identity: openai-codex/gpt-6-astra per parent `review/parent-identity-correction-v2.json` (no independent runtime receipt). Run contract: `RUN/contract-v1.json` (55baff0c…cffaa); worker contract `RUN/control/worker-contract-v1.md`; resource stability rule `RUN/control/resource-stability-addendum-v2.json` (monitor `resource-observer-live-v3.jsonl`).

## Target (unchanged)

Decide whether a 19×8 array over {0,…,5} exists in which any two rows agree in at most one column (A_6(8,7) ≥ 19). Eighteen rows are known (CPro1; parent lower-bound check only). Nineteen is the counting upper bound. A complete exclusion plus a verified 18-row construction would give optimum 18. A verified 19×8 witness would give optimum 19.

## Status at freeze: UNDECIDED

No witness and no nonexistence proof. Layers stay separate and are never fused.

- **M1 (primary pipeline):** complete candidate 5,577 A2 skeleton cases + 486 E0 graphs (old record). It is not parent-final; bridge-desk residuals F-A to F-E remain.
- **Lane-original independent M2:** 151 cases UNDECIDED, frozen exactly in `evidence/probes/frontier-v1.json` (0e7e4370…6a46):
  - ms06 (E2b): 86 skeleton cases. Only b68/b73 have incomplete M2 split lists. v6 direct attempts b74, b151 and b295 are UNKNOWN.
  - ms09 (E3c): 65 skeleton cases, each with a complete frozen extend_b first-P1 placement list. 4,995 pending plus 7 reserved B100 intervals in the frozen v6 M9 contract (072a6172…14a8).
  - Derivation: STATUS17 open list of 155, minus ms06 b182/b201 (v6 validated UNSAT) and ms09 b30/b44 (parent structural verdict 0e56374c…). The probe asserts the counts 86 and 65.
- **Measured M2H views, kept separate:** v6_3 inventory 3/5,424 (49972a35…5118) and v6_4 inventory 1/5,424 (e5242b5a…37d5). Neither is merged with the other or with the 151.
- **Accepted written results, at their scope only:** ms09 b3, b30 and b44 structural exclusions; GPS1/GPS2 written necessity and abstract transport. GPS applied list and orbit coverage is INCONCLUSIVE and no GPS pruning count is accepted. Prior GPS written exclusions do NOT imply applied computational coverage.
- **Not redone here:** the 2,976 stored-proof replay and the 737 effective explicit-floor passes.

## Inherited STOP/HALT registry

`evidence/inherited-stop-registry-v1.json` (ee370929…9873) classifies every live, retired and fixture marker. The raw probe inventory is `evidence/probes/stop-inventory-raw-v1.json` (83eef3eb…e659). All markers are preserved, and no old driver is restarted.

- **Disk/deadline/CPU stops from the closed round:** STOP-hard12 and STOP-m2r12 (watchdog4 disk floor, 13:58:01), STOP-K1 (17:20 deadline), STOP-m2skel9 and STOP-m2partbatch5 (CPU). The parent STOP-RESOLVE was already released.
- **Permanent defects of superseded routes:** STOP-m2skel8 (rev-8 verdict parsing), STOP-hard10/STOP-m2r10 (rev-10 escape paths), STOP-m2skel7 (lratstrict-only acceptance withdrawn).
- **Unresolved items binding any new run:**
  - the m2k3-HALT supervisor-race veto, whose cause is inferred and not reproduced;
  - F-A, CNF delivery with drat-trim early-EOF false VERIFIED;
  - F-D, a single unprovenanced drat-trim binary;
  - lrat-check unsoundness;
  - the disk-floor breaches of unidentified cause.

## Initial scientific plan (frozen; native work only after an item-specific parent GO)

1. **Decisive bounded pilot (proposal to parent):** close ms09 cases with the smallest exact remaining cover.
   - b70 (ms09_s00070): its only interval [0..24]. An earlier calibration record is count=false.
   - b5 (ms09_s00022): [200..299] (new attempt; the old UNKNOWN is preserved) and [300..350]. [0..99] and [100..199] are already v6 measured-validated.
   - Method: the unchanged independent encoder `encode_skel_b.build_partbatch` with the pinned lists. Kissat 4.0.4 `--seed=1`, native limit 600 s. drat-trim with native limit 1200 s.
   - New file-based transport in this lane: exact CNF and binary DRAT bytes are retained and SHA-pinned, so an independently built checker can replay them later.
   - Owned SIGTERM-only settlement. Details are in the GO request under `review/`.
2. **Structural route (written, no native):** look for definition-level counting lemmas beyond GPS that cut whole ms09/ms06 skeleton cases, as b3/b30/b44 did. Candidates: P0-triple empty-partner demand, P1-quad T-disjoint capacity, and pair-block demand. Evaluation uses frozen ≤300 s stdlib probes over the pinned skeleton lists. Any exclusion is checked against the exact skeleton bytes and is counted separately from solver results.
3. **Production estimate for the remaining ms09 cover.** It uses existing calibration and v6 timing receipts only. It is a planning figure, never an accepted quantity.

## Acceptance (from the frozen info-1 contract)

- **New exclusion:** an exact case or subfamily identity, an exact bridge to the frozen skeleton/list/encoder bytes, complete interval coverage, checked UNSAT per interval (or parent-accepted written proof), independent parent replay and hostile review.
- **SAT:** an explicit 19×8 matrix verified by the parent and two verifiers.
- An optimum-18 claim requires every residual case plus the known 18-row construction.
- Insufficient: timeouts, unchecked solver assertions, restricted families or model acceptance.
