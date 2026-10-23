## Amendment GPS-1: global pair-structure condition for the all-P1 multisets (frozen after host clock read 2026-10-18T13:59:31-0700, BEFORE any probe)
* Purpose (parent 13:4x): a scientifically distinct reduction of the remaining cases, not more transport work. The open independent (M2) cases are only in ms06 (E2b = P1^2 P0^6, L=1) and ms09 (E3c = P1^3 P0^5, L=0). This amendment generalizes the two parent-accepted exact-case arguments: b3 (`review/pa19-ms09-b3-structural-parent-v1.md`) and b30/b44 (`review/pa19-b30-b44-parent-verdict-v1.md`). Both concern only the P1 size-2 blocks; the first-column enumerator (extend_b) never sees them, which is why b30/b44 had 2,858 and 547 placements and were still impossible.
* Setting: N=19, k=8, c0 P0 columns (4,3,3,3,3,3), m P1 columns (4,4,3,3,3,2), L = 171 - sum kappa (L1). Row r has P0-quad set T(r), t=|T(r)|. In P1 column j, e_j(r) = (size of r's block) - 3, which is +1, 0 or -1. l(r) = number of rows r agrees with nowhere. Write n2(r) = #{j: e_j(r) = -1} and n4(r) = #{j: e_j(r) = +1}.
* Lemma GPS (necessary condition). Any valid array of the case has the following:
  1. Row identity: r agrees with exactly 18 - l(r) rows, and a block of size s contributes s-1, so 16 + t + sum_j e_j = 18 - l(r). Hence n4 - n2 = 2 - l - t.
  2. Degree bounds: since 0 <= n4 <= m - n2, we get max(0, t+l-2) <= n2(r) <= floor((m-2+t+l)/2).
  3. Pair blocks: each P1 column has exactly one size-2 block, giving a set E of m row pairs. The pairs are DISTINCT, since two equal pairs would agree twice. For each {u,v} in E, T(u) and T(v) are disjoint, since u,v agree in their P1 column and so in no P0 column.
  4. L=1 only: L1 gives exactly one pair {x,y} agreeing nowhere, so l=1 exactly on x,y. T(x) and T(y) are disjoint and {x,y} is not in E.
  5. Consequence: a skeleton with no (E, {x,y}) satisfying (2)-(4) admits NO packing array. For ms09 this contains b3 (a t=5 row needs three partners with T empty, but t=0 rows have n2 <= 0) and the b30/b44 lemma (a t=4 row needs n2 = 2 distinct partners with T exactly the missing quad).
  6. Feasibility of GPS says nothing about existence. Proof: (1)-(4) are definition-level consequences of validity, L1 and the profiles, and (5) is their conjunction. No symbol placement, encoder or enumerator is a premise.
* Probe `src/gps_probe_v1.py` SHA `46b32d23d9beadd8179f800308808f34c2bb9838e6b4c458f0358c712b15f2bc` (pure Python, one lane metadata token, no solver, checker, CNF or native child; creation-only receipt `cycle2/gps1-probe-<stamp>.json`).
  * Rows are rebuilt from each skeleton: one row per edge, hyperedge or type, 4-deg private rows per quad, and the empty rows. The probe asserts 19 rows, quad degree <= 4, no two rows sharing two quads, and the exact all-P1 profile multiset.
  * Exhaustive search over m-subsets of T-disjoint candidate pairs, plus, for L=1, the leave pair, using the bounds of (2). Sound early exits: a row with lo > hi; required memberships > 2m; a row with fewer eligible partners than it needs.
  * Every reported witness is re-checked by a separate verifier function.
  * Inputs (read-only):
    * `skeletons/skeletons-ms06.json` 1c1253ab…9504, `skeletons/skeletons-ms09.json` 34a03106…2e68 (M1 lists);
    * `cycle2/skel-b/skeletons-b-ms06.json` 9ec0fd1d…0488, `cycle2/skel-b/skeletons-b-ms09.json` 7c46ebba…93d0 (independent lists, verdicts reported by b-index);
    * compare maps a_to_b;
    * `STATUS17.json` b7bb242b…c223 (M2 open tags at 02:48);
    * post-STATUS17 resolutions: ms06 b182/b201 (v6 M6 UNSAT checked) and ms09 b30/b44 (parent structural verdict).
* Controls, frozen with the probe:
  * C1: ms09 b3, b30 and b44 must be excluded.
  * C2 (positive semantic control): the known (13,5,4) SAT model `controls/c13skel/models/ms07_s00001.txt` (profiles (4,4,3,2)^3 (4,3,3,3)^2; L=0 and the same constant 2 = N-1-2k). It must be a valid array; its TRUE pair blocks must satisfy (2)-(4); the search must find its skeleton feasible.
  * C3: the M1 and independent lists must give identical verdicts under the a_to_b bijection.
  * C4: every witness is independently re-checked.
  * Limit: there is no semantic positive control for L=1, since the (13,5,4) L=1 analog is UNSAT.
* Stop rules:
  * If any control fails, the probe's exclusions are void and the failure is reported.
  * An excluded skeleton is a CANDIDATE structural exclusion only, never solver/DRAT-certified and never counted, until the written lemma and exact case data pass review and parent acceptance (the b30/b44 precedent).
  * No skeleton list, frozen contract or earlier record is modified. No native work follows from the probe without a separate GO.
* Result (ran 14:00:07-14:00:08, receipt `cycle2/gps1-probe-20261018T140007.json` SHA `67170e7b6934cf2e5594985922e8385f3c46f646714c862e3d6f94014fe52218`): all controls passed.
  * C1: b3, b30 and b44 excluded.
  * C2: the 13-row model is valid; its true pairs [[3,5],[2,4],[1,6]] satisfy (2)-(3) and its skeleton is feasible.
  * C3: the M1 and independent verdicts agree under the bijection, for ms06 and ms09.
  * C4: every witness passed the separate re-check.
  * GPS-1 excludes 44 of 482 ms06 skeletons (38 by exhaustive search, 6 for lack of partners) and 3 of 71 ms09 skeletons (exactly b3, b30, b44). EVERY excluded skeleton is already resolved; GPS-1 excludes NONE of the 86 open ms06 or 65 open ms09 M2 cases.
  * Open counts: ms06 88 open at STATUS17, now 86 after the v6 b182/b201 UNSAT checks (M1 tags s00178/s00182). ms09 67 open at STATUS17, now 65 after b30/b44.
  * Conclusion: the open cases survive the skeleton-level pair condition (their rows have t <= 3). A reduction must condition on deeper structure.

## Amendment GPS-1|C1: GPS-1 conditioned on the first P1 column (frozen after host clock read 2026-10-18T14:07:37-0700, BEFORE its probe)
* Representation: the frozen complete first-column lists `cycle2/m2part_drat/<case>/ext.json` (extend_b row order; orbit representatives under Aut(skeleton) x A/B swap). These are the same lists whose B100 intervals define the M9 route.
* Each placement (A1, B1, P1) fixes e1. The identity t + e1 + sum_{j>=2} e_j = 2 - l gives s(r) = 2 - l - t - e1 for the m' = m-1 remaining P1 columns, with |s| <= m'.
  * Pair blocks: n2'(r) is in [max(0,-s), floor((m'-s)/2)]. The remaining pair blocks are distinct and T-disjoint, and never two rows already together in A1, B1 or P1, since such rows would agree twice.
  * Counts: every remaining P1 column has exactly 8 rows at +1.
  * ms09 (L=0, m'=2): rows with s=2 are +1 in both columns, s=1 rows in exactly one, and s=0 rows lying in exactly one pair block are +1 in the other column. Feasible iff some x in [0,#(s=1)] gives #(s=2) + #(s=0 rows in P3 only) + x = 8.
  * ms06 (L=1, m'=1; only b68 and b73 have lists): choose a leave pair {x,y}, T-disjoint and not together in a column-1 block. Then e2 = s is forced: all e2 must lie in {-1,0,1}, exactly 8 rows must have e2 = +1, and exactly two rows must have e2 = -1, forming a T-disjoint pair that is not together in a column-1 block and is not {x,y}.
  * A placement failing this admits no array. Its whole orbit is excluded, since the condition is invariant under Aut(skeleton) and the A/B swap. The proof is the same definition-level argument as GPS (1)-(4), applied with e1 known.
* Probe `src/gps1c1_probe_v1.py` SHA `8e9eaa0ad560666974e4300c5fb007e3bb2b8888520fb2a5f8317bef4564c52c`. It imports `gps_probe_v1.rows_of` (46b32d23…f2bc) and reads the open flags from the GPS-1 receipt (67170e7b…2218). Pure Python, one metadata token, no solver; creation-only receipt `cycle2/gps1c1-probe-<stamp>.json`. Scope: every ms09 case with a list, plus ms06 b68/b73. Each placement is sanity-checked (sizes 4/4/2, disjoint, blocks T-disjoint).
* Controls:
  * C1: every placement of b30 and of b44 must be excluded (implied by GPS-1 at skeleton level).
  * C2: the 13-row SAT model with EACH of its three P1 columns taken as first column must be feasible.
  * C4: every ms09 witness is re-checked by explicit e-vector construction.
  * C6: every placement is a valid first column.
* Stop rules:
  * Any control failure voids the exclusions.
  * Excluded placements, intervals or cases are CANDIDATE structural exclusions, resting additionally on the parent-accepted completeness of each list. They are never counted, and never relabel or skip M9 records, until review and parent acceptance.
  * No native work.
* Result (ran 14:08:08-14:08:24, receipt `cycle2/gps1c1-probe-20261018T140808.json` SHA `d82ddf381c34348b1c4ae8b7a6956f8a6a6f0650c6ee947dd30e24beb0cc961d`): all controls passed.
  * Controls: every placement of b30 and of b44 excluded; the 13-row model is feasible with each P1 column taken as first; ms09 witnesses re-checked; all placements valid.
  * ms09, 65 open cases with lists: 118,102 of 493,802 placements excluded (23.9%). No open case is fully excluded. Only 16 of its 4,970 B100 intervals are entirely excluded, since the exclusions are spread across list order.
  * ms06 b68/b73: 8,636 of 11,574 placements excluded (74.6%). Neither case is fully excluded, and none of its 117 intervals is entirely excluded.

## Amendment GPS-2|C1 for ms06: forced second P1 column with its block partition (frozen after host clock read 2026-10-18T14:10:23-0700, BEFORE its probe)
* For ms06 (m=2, L=1), once the first column and the leave pair {x,y} are fixed, e2 = 2 - l - t - e1 is forced for every row. GPS-2|C1 adds the column-2 block partition to GPS-1|C1:
  * the 8 rows with e2=+1 split into two 4-blocks;
  * the 9 rows with e2=0 split into three triples;
  * the two rows with e2=-1 form the pair;
  * every block is pairwise T-disjoint, never holds two rows already together in an A1/B1/P1 block, and never holds both leave rows.
* Argument: rows sharing a column-2 block agree in column 2, hence in nothing else; the leave pair agrees nowhere. This is the definition-level argument of GPS (1)-(4). A placement with no passing leave pair admits no array, and its orbit is excluded.
* Probe `src/gps2c1_ms06_probe_v1.py` SHA `5029848a64d522448944502d0cd05ea75d69957f82b9b7536cdddbf96ac52d12`. It imports `gps1c1_probe_v1` (8e9eaa0a…c52c) and `gps_probe_v1` (46b32d23…f2bc) and reads the GPS-1|C1 receipt d82ddf38…961d. Scope: exactly ms06 b68 and b73. Exhaustive partition search; creation-only receipt `cycle2/gps2c1-ms06-probe-<stamp>.json`.
* Controls:
  * C1: monotone, i.e. every GPS-1|C1 exclusion stays excluded.
  * C2: partition unit control on the 13-row SAT model (its true second-P1-column blocks are compatible and split).
  * C4: every witness is re-checked as a full column-2 structure satisfying the row identity.
  * Limit: there is no L=1 semantic positive control.
* Stop rules: as for GPS-1|C1. Candidates only, list completeness required, no native work.
* Result (ran 14:10:48-14:10:52, receipt `cycle2/gps2c1-ms06-probe-20261018T141048.json` SHA `12b4320e3acdfd119516a505518357c9bd647f1ec5b19755196a0cf752b8bf57`): controls passed (monotone, 13-row partition unit control, every witness re-checked).
  * b68 (M1 s00134): 9,016 of 10,459 placements excluded (86.2%; GPS-1|C1 alone 7,806); 1,443 survive; 20 of 105 B100 intervals entirely excluded.
  * b73 (M1 s00115): 979 of 1,115 excluded (87.8%; GPS-1|C1 alone 830); 136 survive; 0 of 12 intervals entirely excluded.
  * Neither case is fully excluded.
* Reduction summary (candidates only; nothing counted or skipped). Re-batching only the surviving placements of the frozen lists would turn:
  * the 65 open ms09 cases (493,802 placements, 4,970 B100 intervals) into 375,700 placements in 3,791 B100 batches (-23.7%);
  * ms06 b68 into 15 batches instead of 105, and b73 into 2 instead of 12.
  * No open case is closed. This would need a new versioned contract and a parent GO, after the lemmas, the lists' completeness and the probe code are reviewed.
* Parent disposition (~14:1x): GPS-1, GPS-1|C1 and GPS-2|C1 remain frozen CANDIDATE necessary conditions only. None closes any of the 151 lane-original open M2 cases. Not authorized: re-batching, new lists (in particular the 84 listless open ms06 cases), native expansion, and any further 5 GiB enumeration. A compact-lemma review may follow later; no acceptance is inferred.
* List bindings (metadata only): `src/gps_list_binding_check_v1.py` SHA `5c965c1f0d9ceca623b47853442e94c74c1ca43a0e6aec4cec2141855897e3b3`, receipt `cycle2/gps-list-binding-20261018T141454.json` SHA `6e40783cce4ea392204741d2d26b68b83a724281b62a012ea97659c8525a40a9`. All 74 consumed lists match the frozen authorities in path, SHA, n, raw class assignments and automorphisms:
  * 70 ms09 lists against the M9 contract 072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8, phase file `cycle2/ms09-batch-denominators-v2-20261018T015110.json` d0d0d7fa9dae6ab263b05af800c0967916adf840c7583613d98c15d41d810d33;
  * ms06 b68/b73, used by both probes, against `cycle2/ms06-two-batch-denominators-20261018T024846.json` fc5b86191bb977f7f08fa1996a2011f9f086be6bcce954887146a3035476f83c, with their complete-denominator pin files verified.
  * List completeness remains the authorities' claim (helper generation receipts); it is not re-proven here.
