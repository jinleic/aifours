# PA(19,8,6) lane info-1: final lane summary

Written after `/bin/date` read 2026-10-18T16:41:29-0700. This is a new file: no receipt is overwritten and nothing is deleted. Earlier summaries are interim checkpoints.

## 1. Status

- **PA(19,8,6) is UNDECIDED.** No 19-row array was found, and there is no nonexistence proof.
- The info-1 gate is not reached.
- No native work has run in this lane since 2026-10-18T13:30:46-0700, and none is planned.

## 2. Lane-original frontier (separate from §3)

Sources: `STATUS17.json` (b7bb242bb0304ba5d0a10b8d0b113f34813244f9be74134ec91b067d0acfc223, 02:48) plus the later records named below.

- **Cover:** A1 = ms00 E0 (486 quad graphs) and A2 = ms01-ms09 (5,577 skeleton cases). The global cover/bridge audit is still pending.
- **M1:** E0 486/486; A2 5,577/5,577.
- **M2:** E0 486/486. A2 has 5,426 resolved:
  - 5,421 solver-checked at STATUS17;
  - ms06 b182 and b201 UNSAT checked under v6 (`cycle2/m2skel_drat/ms06_b00182_v6.json`, `ms06_b00201_v6.json`);
  - parent structural verdicts for ms09 b3, b30 and b44.
- **151 lane-original M2 cases are UNDECIDED:**
  - ms06: 86. Its v6 attempts b74, b151 and b295 ended UNKNOWN.
  - ms09: 65. b5 is partial: [0..99] and [100..199] UNSAT under v6, [200..299] UNKNOWN, [300..350] not attempted.
- M6/M9 stay PARKED.

## 3. Measured independent M2H coverage (receipt-level; the two inventories are NOT merged)

- **v6_3 inventory:** `cycle2/m2h-inventory-20261018T120437-1792350277375607000.json` (49972a359fbaa64cc3b43acb8f2e2e912d9305d540682568284c1cedd1eb5118). 3 of 5,424 cases covered: ms01 b45, b236, b685. Parent pilot GO e074541bd8edd8183e4820e065e34ee9ed3dc74dcf182c7eb2936ad422b41562.
- **v6_4 isolated inventory:** `cycle2/m2h-inventory-20261018T133100-1792355460018218000.json` (e5242b5aad81f9974147e7a79f9e65a918bd324b8487df7f59075a86ba3237d5). 1 of 5,424 covered: ms01 b957, through its four split intervals. Parent audit 4e120c1a17850ac62271388843c9505b659bdb9a01658575db36a0bb6c1794d6 accepted it at exact scope only.
- **Outside M2H:** 82 ms01-ms08 cases; ms09 and E0 are not in M2H.
- **Limits:**
  - native stdout, CNF and proof payloads are not retained, so qualification rests on receipts, not on a replay of proof bytes;
  - the consumer shell exit codes are not retained;
  - resource guards are sampled;
  - the data census assumes a 600 s TTL and no other-lane writer adding more than 256 MiB within 600 s;
  - the v6_4 run's stop_reason is null (README addendum).

## 4. GPS conditions

Parent verdict `review/pa19-gps-written-parent-verdict-v1.md`, SHA ff0954eefe72d237eb190ed0fa50a1eeb194c3b5ef1f6eeff041076b2436546e.

**ACCEPTED as written necessity and abstract symmetry, with the parent's overlay:**
1. GPS1;
2. GPS1 conditioned on a PARTIAL 4/4/2 first-column placement;
3. the ms09 relaxation R09, whose "iff" concerns only the e-value relaxation;
4. ms06 conditioned necessity;
5. ms06 GPS2 conditioned necessity;
6. abstract symmetry transport under T(σr) = π(T(r)), the A/B swap, and the ms09 column exchange (P2, P3, x) -> (P3, P2, b - x).

The texts are README lines 1002-1090 (parent excerpt 4f73cddb564cc835391ebcc1137532c753e6b7c892a5f77a05299549c27678b5) and `cycle2/gps-proof-addendum-v1.md` (dec91dbfeacbf39be9f180400cd1f93c12432dffc2151402c8dbb13e8d89c14f). The column-swap supplement `cycle2/gps-proof-addendum-v1-colswap-supplement.md` (88ae07466f1e402ccecd3a7ce06d55a796ef4d448f993869d825df0fa4f2fedd) is not separately reviewed.

**UNRESOLVED application gap (INCONCLUSIVE):**
- whether ext-list row labels match rows_of(sk)[i];
- whether every extend_b generator satisfies the transport equation;
- list completeness and orbit coverage;
- exhaustive exclusion search;
- all numeric exclusion counts.

**Candidate figures only, NOT accepted:**
- GPS1 excludes 44 ms06 and 3 ms09 skeletons, all already resolved.
- GPS1|C1 excludes 118,102 of 493,802 open ms09 placements, and 8,636 of 11,574 for ms06 b68/b73.
- GPS2|C1 excludes 9,016 of 10,459 placements for b68 and 979 of 1,115 for b73.
- No case is closed. No re-batching follows.

**Sparse or vacuous controls (none is a premise or an independent certificate):**
- the GPS2|C1 monotone control is vacuous for b68, because the prior excluded-index list was omitted above 2,000 entries;
- C4 re-checks feasible witnesses only, not exclusions;
- the 13-row reference check compares the sorted t multiset, not the full T;
- the GPS2 unit control covers only 4-blocks with an empty leave;
- there is no L=1 semantic positive control;
- the same-lane cross-check (`cycle2/gps-crosscheck-20261018T141846.json`, 7e44f9f52979353166c349915e894937a592c00c1a2855fbf4add7d1b7d9a6b9; 508,966 placements, 0 disagreements) is auxiliary;
- the list-binding check (`cycle2/gps-list-binding-20261018T141454.json`, 6e40783cce4ea392204741d2d26b68b83a724281b62a012ea97659c8525a40a9) is metadata only.

## 5. Unreviewed written triple-layer/Gram results (separate from GPS; NOT reviewed, NOT accepted)

- `cycle2/triple-layer-gram-note-v1.md` (4a68eeef659a05f925d12b0da2221501cc71ed52d4427c0e83483ddb0ee427bc):
  - the Gram identity M M^T = 7I + J - A_leave, verified from incidence;
  - Lemma TG: the triple Gram equals L_QP + L_lv + J - diag(1 + 6 n2 - 3 l), which is PSD;
  - C1 reformulation, C2 expansion bound and C3 connectivity, all for ms09; heuristic C4; and the exact obstruction to a uniform proof.
- `cycle2/triple-layer-gram-note-v2.md` (cd4cac0d33da60fbaf0cda196e12be474453154dde5388758da6e2bca3bf4f4e): C2' (unified bound) and C3' (ms06 connectivity). Its C5 is withdrawn in v3.
- `cycle2/triple-layer-gram-note-v3.md` (48b0c495fe7dfb4af24223fd5bd7b0e103f4eb1ad2064878dc8984348e49871c): erratum showing C5 is vacuous, since incidence counting already gives q_AB <= 4 + N2; and C2*, a Cauchy-Schwarz sharpening.
- `cycle2/triple-layer-gram-note-v4.md` (0f40bbad7ccf5453e6ce2f6b905be07a04a9eb484965f27ba1d7514525eaca48): Lemma Q2P, two-quad pigeonhole on triples.
  - ms09: q_j <= 2 N2_j - 1, so N2(A_j ∪ B_j) >= 1 and Σ_{A_j ∪ B_j} (t - 2 n2) <= 4.
  - ms06: q + ℓ <= 1 + 2 N2 - Lv.
  - Tight by hand on the real (13,5,4) model: q = 8, N2 = 4.
- None was evaluated on any configuration. There is no uniform obstruction and no closure.

## 6. Disk floor (exact parent-monitor observations; cause UNIDENTIFIED)

| Time (-0700) | Free (B) | Note |
|---|---|---|
| 14:07:50 | 11,985,104,896 | below the 12e9 floor |
| 14:08:01 | 12,577,251,328 | back above |
| 14:19:51 | 11,953,606,656 | below (`df` at 14:19:49 read 11,960,438,784) |
| 14:20:31 | 12,336,631,808 | back above |
| 15:20:14 | 12,261,830,656 | last sample at or above 12e9 |
| 15:20:24 | 11,763,953,664 | below, and continuously below since |
| 16:40:38 | 4,382,003,200 | latest observation |

- This lane had no native job during any breach. No floor stop of a lane native job occurred.
- No cleanup and no deletion was done.
- My earlier statements attributing the drops to a particular writer are withdrawn.
- Earlier events, both already recorded: the 07:04 parent-observed floor event, and the 09:25:51 global SIGTERM, cause unknown, after which the lane harness was re-armed.

## 7. Processes at 16:40:43

- Only the passive monitors are running: rss_watchdog4 (pid 60597), checkpoint_clock (60600) and stop_k1_timer (60602), which writes `cycle2/STOP-K1` at 17:20.
- Tokens t0, t1 and bigmem are unheld. There are no HALT or STOP flags.
- No new launch is permitted; free space is below the floor.

## 8. Irreducible next steps (none authorized)

1. Closing the 151 lane-original M2 cases needs full-constraint solving with checked proofs, or a new global argument. GPS, TG and Q2P are relaxations.
2. The applied GPS bridge (row-order map, generator transport, list completeness) must be verified before any reviewed exclusion search.
3. Measured M2H coverage still lacks about 5,573 items, roughly 43 h at about 28 s per item.
