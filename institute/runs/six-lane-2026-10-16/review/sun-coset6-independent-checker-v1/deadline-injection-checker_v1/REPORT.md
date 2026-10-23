# Independent checker report (checker_v1, standard library, one process)

- Verdict: **PASS** (failures 0, incomplete parts 0)
- Checker: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-independent-checker-v1/checker_v1.py` sha256 `5c25199b6de969c84c9521b9960a02d297d6cbacacea6c5e9e8f82695737874e`
- Elapsed: 1000033.1 s (one process, no numpy)

## Inputs (sha256)

- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/run.json` 6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754 (2853 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/orbits.jsonl.gz` a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49 (407387 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/rlp_duals.json` bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef (106879 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/survivors.json` 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 (2 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-run.sha256` f69b8b2288a2cb4285eba8f39a45510e2aa456b725b08fb7cc6358245790bf73 (974 bytes)
- orbits.jsonl (uncompressed) f4f69363a1a602ec56f3a957566e566d2f03f988792a8d04565d2cce31976579; equals run.json field: True

## Per type

| type | leaves (mine) | leaves (run.json) | hash match | edge-DFS = primary | orbit lines | orbits (run.json) | coverage ok | verified | failed | incomplete |
|---|---|---|---|---|---|---|---|---|---|---|
| `(None, 0, None)` | 64940 | 64940 | True | True | 478 | 478 | True | 0 | 0 | 478 |
| `(None, 0, 0)` | 92937 | 92937 | True | True | 2268 | 2268 | True | 0 | 0 | 2268 |
| `(0, 1, None)` | 137789 | 137789 | True | True | 2964 | 2964 | True | 0 | 0 | 2964 |
| `(0, 1, 0)` | 200741 | 200741 | True | True | 4466 | 4466 | True | 0 | 0 | 4466 |
| `(0, 1, 1)` | 222701 | 222701 | True | True | 16414 | 16414 | True | 0 | 0 | 16414 |
| `(0, 2, None)` | 211192 | 211192 | True | True | 4344 | 4344 | True | 0 | 0 | 4344 |
| `(0, 2, 0)` | 307224 | 307224 | True | True | 6475 | 6475 | True | 0 | 0 | 6475 |
| `(0, 2, 1)` | 337507 | 337507 | True | True | 23715 | 23715 | True | 0 | 0 | 23715 |

Engine `code` field (informational; CERT-FORMAT says not to rely on it): lines whose `code` lies in the stabiliser orbit of `rep`, per type: {'(None, 0, None)': 478, '(None, 0, 0)': 402, '(0, 1, None)': 402, '(0, 1, 0)': 408, '(0, 1, 1)': 315, '(0, 2, None)': 402, '(0, 2, 0)': 408, '(0, 2, 1)': 315}; sampled lines whose `code` lies in the full S6 orbit of `rep`: {'(None, 0, None)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(None, 0, 0)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 1, None)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 1, 0)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 1, 1)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 2, None)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 2, 0)': {'sampled': 200, 'code_in_S6_orbit': 200}, '(0, 2, 1)': {'sampled': 200, 'code_in_S6_orbit': 200}}.

## Per rule (all types)

| rule | lines | verified | failed | incomplete |
|---|---|---|---|---|
| K | 55159 | 0 | 0 | 55159 |
| RLP | 5513 | 0 | 0 | 5513 |
| PB | 55 | 0 | 0 | 55 |
| FH5 | 134 | 0 | 0 | 134 |
| N26 | 108 | 0 | 0 | 108 |
| RPLP | 155 | 0 | 0 | 155 |

## Global

- lines_parsed: 61124
- lines_malformed: 0
- survive_lines: 0
- survivors_json_empty: True
- total_orbits_match: True
- rlp_dual_entries: 1346
- rlp_keys_checked: 0
- rlp_keys_passed: 0
- rlp_keys_failed: 0
- rlp_dual_entries_unused: 1346
- leaves_total_mine: 1575031
- manifest_lists_input_hashes: {'run.json': True, 'orbits.jsonl.gz': True, 'rlp_duals.json': True, 'survivors.json': True}
- FH5: {'lines': 0, 'nodes': 0, 'max_seconds': 0.0, 'engine_counts_equal_full_space': 0, 'full_space_sum_per_placement': 0}
- q statistics: {'RLP_q_vectors_checked': 0, 'RPLP_R_entries': 0, 'RPLP_P_entries': 0}
- types cover: {'placements': 91, 'placements_per_type': {'(None, 0, None)': 1, '(None, 0, 0)': 6, '(0, 1, None)': 6, '(0, 1, 0)': 6, '(0, 1, 1)': 30, '(0, 2, None)': 6, '(0, 2, 0)': 6, '(0, 2, 1)': 30}, 'stabiliser_sizes': {'(None, 0, None)': 720, '(None, 0, 0)': 120, '(0, 1, None)': 120, '(0, 1, 0)': 120, '(0, 1, 1)': 24, '(0, 2, None)': 120, '(0, 2, 0)': 120, '(0, 2, 1)': 24}, 'each_placement_maps_to_exactly_one_type': True}

## Method (what a PASS means)

- **Types.** A placement is (E2 vertex or none, class c2 in {1,2}, E3 vertex or none): 1 + 6 + 6*2 + 6*2*6 = 91
  placements.  Coverage proof: no markers -> (None,0,None); only E3 at x -> any permutation with x->0 gives
  (None,0,0); only E2 at x with class c -> x->0 gives (0,c,None); E2 and E3 both at x -> x->0 gives (0,c,0);
  E2 at x, E3 at y != x -> x->0, y->1 gives (0,c,1).  Presence of each marker, the class and coincidence are
  S6-invariant, so the image type is unique.  Relabelling the six subgroups by a permutation maps a configuration
  to a configuration, so every pattern is equivalent to one with a type's placement.  The stabiliser of a type's
  placement is exactly {p : p(e2)=e2 if present, p(e3)=e3 if present} (E2 and E3 are different markers and are never
  exchanged); sizes 720, 120 (x5), 24 (x2).  `check_types_cover` re-verifies all of this by brute force over S6.
- **Universe.** Primary enumeration: vertex-by-vertex stars, every star in {1..4}^c tried, a triangle tested exactly
  when its last edge is assigned.  Cross-check: an edge-by-edge depth-first enumeration with the scalar T test
  (must give the identical sorted list), plus random and one-edge-neighbour spot checks.  The sorted list is hashed as
  specified and compared with run.json.
- **Orbits.** For each line the checker computes the full stabiliser orbit of `rep` itself; the orbits must be pairwise
  disjoint and their union must equal the leaf set exactly (set equality, not only counts/hash); `rep` must be a
  T-consistent leaf of the line's type.  Every rule is checked on `rep`; a certificate for `rep` transfers to its orbit
  because each rule is label-equivariant and the stabiliser fixes the markers.
- **Rules.** K, RLP (all 31 non-empty supports with every hereditary sub-test, exact Fractions, every admissible q,
  key recomputed), PB/Ppair (grid rounding lo = u*ceil(L/u), hi = u*floor(min/u) then the K2 decrement), FH5
  (exhaustive search over the whole assignment space for all 7 E5 placements; pruning only on rejections that persist),
  N26 (safe form: every admissible tau of every neighbour triple has no prime factor >= 5, and if v = E3 none is
  divisible by 3 and tau_max < 3 tau_min; the '3 | tau_min' alternative is never accepted), RPLP (columns rebuilt:
  every non-empty A closed under the ordered forced pairs, every S subset of A that is empty, a singleton or
  hereditary-allowed; per-q certificate count exact; R keys recomputed).  Any SURVIVE line, malformed line, unknown
  rule, duplicate JSON key, non-string rational or sign violation is a failure.

## Observations on the texts (no effect on this verdict unless stated)

1. CERT-FORMAT-k6-v1 N26 and rules-k6-v3 L11(4) allow '3 | tau_min' as an alternative; that direction is wrong
   (it forces 3 | tau).  Unreachable here because tau_min is a power of 2 under alpha_jk in {2,4}; fixed in
   CERT-FORMAT-k6-v2 / erratum v2 F1.  This checker uses the safe test.
2. CERT-FORMAT-k6-v1 PB wording ('ceil(...) rounded up to a multiple of u') is ambiguous; the integer-ceiling reading
   would be unsound.  This checker uses grid rounding (as in CERT-FORMAT-k6-v2 / erratum v2 F3).
3. The engine `code` field is not, in general, a labelling in the stabiliser orbit of `rep` (counts above); it is in
   the full S6 orbit on every sampled line, i.e. it appears to carry the markers elsewhere.  Coverage here is
   established from `rep` only, as CERT-FORMAT section 3 prescribes.
4. The PB precondition 'every pair has lo <= hi' is not needed for soundness (it is enforced anyway).
5. E5 enters only FH5; for K, P, RLP and RPLP E5-independence is a written argument (alpha, q <= 4 and the gcd
   table involve no factor 5).  For N26 this checker removes the dependence mechanically (prime-support test on
   every admissible tau).
6. What a PASS supports (wording from the delta reviews): no minimal-order Sun(6) counterexample carries a Core5(6)
   configuration, conditional on the written rule proofs, the imports (Zhu k <= 4, accepted Sun(5)), and R1(6).
   This report is a certificate check only; it makes no theorem or novelty claim.

