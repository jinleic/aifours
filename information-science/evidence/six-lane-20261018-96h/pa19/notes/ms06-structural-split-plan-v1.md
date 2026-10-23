# ms06 structural split plan v1: leave pair and pair blocks (PA19 96 h lane)

Written after the `/bin/date` reading 2026-10-19T02:09:12-0700 by ContinuePA19b, the lane successor of ContinuePA19. This is a planning note: it records exact definitions, a soundness argument and two proposed experiments. It closes nothing, excludes nothing and makes no PA(19,8,6) claim. Every count below is either taken from a pinned record (and cited) or labelled as a hand derivation. The ~566M figure is a planning alarm, not a lower bound.

## 0. Scope

- **Target.** The 86 lane-original M2-undecided ms06 cases (E2b), frozen in `evidence/probes/frontier-v1.json` (0e7e4370…6a46).
- **Problem with the inherited route.** The first-P1 placement route used for ms09 (extend_b lists, then `build_partbatch` batches) has, for ms06, a class-assignment DP upper bound of 566,411,546 raw assignments over the 86 cases (`evidence/probes/ms06-dp-v1.json` 8c2c44b2…7ae4). That bound ignores pairwise disjointness, so it is not a list size or a lower bound. The two lists that exist (b68, b73) hold 10,459 and 1,115 orbit placements (checkpoint 003). The route is not plausible for 86 cases in this round.
- **This plan.** Split each case by a much coarser global structure, namely its pair blocks and its leave pair. GPS-1 already proves that structure necessary. The base formula stays the frozen M2 direct CNF (`encode_skel_b.build_v2`), the same formula behind the v6 direct attempts, and each sub-case only appends a few clauses.
- **Not claimed.** No case is closed or excluded by this note. A split denominator is not coverage, and a planning estimate is not a result.

## 1. Setting and exact definitions

**Case.** The case b is skeleton b of `cycle2/skel-b/skeletons-b-ms06.json` (9ec0fd1d…0488) in the old lane. It has:
- N = 19 rows, K = 8 columns and Q = 6 symbols;
- c0 = 6 P0 columns with profile (4,3,3,3,3,3), indexed 0..5;
- m = 2 P1 columns with profile (4,4,3,3,3,2), indexed 6 and 7 in `build_v2`;
- L = 1. Counting gives 6·21 + 2·22 = 170 = C(19,2) − 1 agreeing pairs.

**Rows (member order of `build_v2`, identical to GPS `rows_of`).**
- First the listed types, in file order; each is a set T ⊆ {0..5} with |T| ≥ 2.
- Then, for each v = 0..5, the 4 − deg(v) private rows with T = {v}.
- Then the `empty` rows with T = ∅.

Write T(r) for the P0-quad set of row r and t(r) = |T(r)|. The **class** of r is T(r). Only private rows and empty rows can share a class, because two rows with the same T of size ≥ 2 would agree twice.

**Arrays.** An array X is valid for case b if it is a 19×8 array over {0..5} with:
- any two rows agreeing in at most one column;
- the column profiles above;
- X[r][v] = 0 exactly when v ∈ T(r), for P0 columns v.

In `build_v2` the P1 labels are sorted by count, so labels 0 and 1 are the two quads, labels 2, 3 and 4 the triples, and **label 5 the pair**. The cell variable is v(r,c,s) = 1 + 48r + 6c + s.

**Pair blocks and leave pair.**
- P_c(X) = {r : X[r][c] = 5} for c ∈ {6, 7}. These are the pair blocks, and E(X) = {P_6(X), P_7(X)} is unordered.
- D(X) is the unique pair of rows agreeing in no column. It is unique because L = 1.
- The **key** of X is κ(X) = (E(X), D(X)).

**Row identity.** Validity gives t(r) + e_6(r) + e_7(r) = 2 − l(r). Here e_c(r) = (block size) − 3 ∈ {+1, 0, −1} and l(r) = [r ∈ D(X)]. With n2(r) the number of pair blocks containing r and n4(r) the number of P1 quads containing r:
- n4 − n2 = 2 − l − t;
- max(0, t + l − 2) ≤ n2(r) ≤ min(2, ⌊(t + l)/2⌋).

**GPS-1 (written necessity, accepted at its scope in the lane README).** κ(X) satisfies:
- P1: the two pairs of E are distinct and each is T-disjoint;
- P2: every row satisfies the n2 bounds with l(r) = [r ∈ D];
- P3: D is T-disjoint and D ∉ E.

Call any (E, D) satisfying P1–P3 a GPS-1 key of b. K_raw(b) denotes the set of all of them. All 86 open cases are GPS-1 feasible (old receipt `cycle2/gps1-probe-20261018T140007.json` 67170e7b…2218: `m2_open_now_gps_excluded` = []). Only existence of a witness was recorded there; K_raw(b) itself has never been enumerated.

**Consequence used later.** Given (E, D), every row's n2 and l are fixed, so its P1-quad degree n4(r) = 2 − l − t + n2 is fixed as well. This is a possible later strengthening; v1 does not use it.

## 2. Split levels and class-level signatures

For a GPS-1 key k = (E, D) with E = {{p, p'}, {q, q'}} and D = {x, y}, define three class-level signatures, each a sorted multiset of classes:
- **Level E:** σ_E(k) = {{T(p), T(p')}, {T(q), T(q')}};
- **Level D:** σ_D(k) = {T(x), T(y)};
- **Level ED:** σ_ED(k) = (σ_E(k), σ_D(k)).

**Aut(types)** is the set of permutations α of the P0 columns {0..5} that preserve the type multiset, computed by brute force over 6! exactly as in extend_b and `ms06-dp-v1`. α acts on classes by T ↦ α(T). Private classes keep their sizes because degrees are preserved, and the empty class maps to itself.

**Sub-case set.** S_ℓ(b) is the set of Aut(types)-orbit representatives (canonical minimum) of {σ_ℓ(k) : k ∈ K_raw(b)}.

**Sub-case formula.** F_b ∧ Φ_s for each s ∈ S_ℓ(b), where:
- F_b = `build_v2(6, types_b, empty_b, [[4,4,3,3,3,2]]*2)`. This is byte-for-byte the CNF of the direct attempts; for example, v6 b74 is a95aafdd…f193 (8,793,188 B) and v6 b151 is 063cbc49…eb08 (8,788,845 B).
- Φ_s is defined in section 4.

## 3. Soundness

**Theorem.** Fix b and a level ℓ. Suppose S_ℓ(b) contains the orbit representative of every realizable signature, i.e. the census is exhaustive. If F_b ∧ Φ_s is UNSAT for every s ∈ S_ℓ(b), then no valid array exists for case b.

**Proof.**
1. **Setup.** Suppose X is valid for b. By GPS-1, κ(X) ∈ K_raw(b). Choose α ∈ Aut(types) whose image of σ_ℓ(κ(X)) is the representative s* ∈ S_ℓ(b).
2. **Lift.** Lift α to g = (α, π). Here π is any row bijection with T(π r) = α(T(r)); it exists because α preserves the type multiset and the private-class sizes. Then Y = g·X (permute the P0 columns by α and the rows by π) is valid for b with the same membership, and σ_ℓ(κ(Y)) = s*.
3. **Normal form.** Let H be the group of symmetries that `build_v2` breaks: symbol relabelings preserving the column profiles, the swap of the two identical P1 columns, and transpositions of consecutive rows with identical T and |T| ≤ 1. Its docstring states that the lex-least element Y′ of the H-orbit of Y satisfies every clause of F_b, with the auxiliary variables at their defined values. This is the same encoder trust that every M2 direct UNSAT (e.g. b182, b201) relies on.
4. **H keeps the signature.** Every element of H fixes σ_ℓ:
   - a profile-preserving relabeling fixes label 5, the unique count-2 label, so it fixes both pair blocks, and it never changes which rows agree;
   - the P1 swap exchanges P_6 and P_7, and E is unordered;
   - row transpositions stay inside classes.

   Hence σ_ℓ(κ(Y′)) = s*.
5. **Conclusion.** Y′ satisfies Φ_{s*}: set the selector according to which column carries which class pair (section 4), and the leave clause holds by its true U literal. So F_b ∧ Φ_{s*} is SAT, a contradiction. ∎

**Why class level and not row level.** `build_v2` already uses H's row transpositions: rows of one class are lex-ordered. Choosing one row-level representative per orbit of the class-permutation group would use that symmetry a second time. That is unsound in general, because the normal form need not put the leave or pair row at the chosen position. Class-level signatures are invariant under H, so only Aut(types) (unused by `build_v2`) is spent on the reduction. The σ-swap is handled by keeping E unordered and adding one selector.

**Trust base.**
1. GPS-1 necessity (written).
2. The `build_v2` normal-form claim and encoding correctness, which every M2 direct result already relies on.
3. Census exhaustiveness and orbit correctness. This is new; it needs two enumerators and an independent parent replay.
4. Per-sub-case UNSAT checked by DRAT (drat-trim) with file transport.

The F-A and F-D items in the lane README stay binding for item 4.

## 4. Exact sub-case clauses Φ_s

**Variables of F_b.**
- Cells: v(r,c,s) = 1 + 48r + 6c + s, giving 912 variables.
- Leave variables: in `build_v2` order, the i-th pair of `combinations(range(19), 2)` gets U(i) = 913 + 49i, followed by its 48 witnesses a = U(i) + 1 + 6c + s. Each witness has the clauses (¬a ∨ v(r,c,s)) and (¬a ∨ v(r′,c,s)), and the pair has the clause (a_1 ∨ … ∨ a_48 ∨ U(i)).
- In every model U is exact. A true agreement forbids U only through the per-row totalizer count, and validity fixes that count at the true number of non-agreeing partners.

Let rows(C) be the rows of class C, and let nv_b and m_b be the variable and clause counts of F_b.

**Level E,** s = {{A1, A2}, {B1, B2}}. A1 ≠ A2 and B1 ≠ B2 always hold: pair rows are T-disjoint, two rows of one private class share their quad, and empty rows have n2 = 0.
- If {A1, A2} = {B1, B2}, append (∨_{r∈A1} v(r,6,5)), (∨_{r∈A2} v(r,6,5)), (∨_{r∈A1} v(r,7,5)) and (∨_{r∈A2} v(r,7,5)).
- Otherwise use the selector z = nv_b + 1 and append:
  - (¬z ∨ ∨_{A1} v(r,6,5)), (¬z ∨ ∨_{A2} v(r,6,5)), (¬z ∨ ∨_{B1} v(r,7,5)), (¬z ∨ ∨_{B2} v(r,7,5));
  - (z ∨ ∨_{B1} v(r,6,5)), (z ∨ ∨_{B2} v(r,6,5)), (z ∨ ∨_{A1} v(r,7,5)), (z ∨ ∨_{A2} v(r,7,5)).

  F_b allows exactly two rows with label 5 per P1 column (the at-most-n clauses of all labels sum to 19). So these clauses force one row from each named class.

**Level D,** s = {X1, X2}. Append the single clause (∨ U(x,y) over x ∈ rows(X1), y ∈ rows(X2), x ≠ y).

**Level ED.** Append both groups.

**Serialization.** The header is `p cnf (nv_b + [selector]) (m_b + |Φ_s|)`, followed by the F_b clauses in `build_v2` order and then Φ_s in the order above. The result is byte-identical to `cnf_bytes(nv', cl + Φ_s)`. Experiment 1 checks this, the U numbering and the witness clauses against the actual clause list.

## 5. Coverage bookkeeping and audit (for later production, not now)

- The denominator of case b at level ℓ is |S_ℓ(b)|, frozen by an accepted census replay.
- Case b closes only if all of the following hold:
  - every s ∈ S_ℓ(b) is checked UNSAT (or refined, below);
  - the census is replayed by an independently written enumerator;
  - the parent raw audit passes.
- No partial cover gives any case or PA(19,8,6) verdict.
- **Adaptive refinement.** An UNKNOWN Level-E node s_E may be replaced by all Level-ED signatures (s_E, d) that occur in the census with first component s_E. This is complete by the same theorem, restricted to arrays with σ_E = s_E. The bookkeeping is a tree whose leaves must all be UNSAT.

## 6. Hand illustration (b73; hand derivation, to be confirmed by experiment 1)

b73 (ms06_s00115) has types {0,4}, {1,5}, {2,5}, {3,5}, {4,5}, no empty rows, private classes {0},{1},{2},{3} of size 3 and {4} of size 2, no t ≥ 3 rows, and |Aut| = 6 (matching `ms06-dp-v1`).
- The only T-disjoint type pairs are {0,4}–{1,5}, {0,4}–{2,5} and {0,4}–{3,5}. Since n2 ≤ 1 for t = 2, at most one pair block is type–type.
- So every GPS-1 key has a pair block containing a private row. A private row needs l = 1 to have n2 = 1, so at least one leave row is a private row lying in a pair block.
- A rough hand count gives about 36 + ~140 Level-E signatures, roughly 30–40 Aut-orbits. Compare the 1,115 first-P1 orbit placements of b73.

These are planning magnitudes only. Experiment 1 replaces them with exact counts.

## 7. Prioritisation context (pinned records only; these are solver behaviour, not certificates)

For the open ms06 cases, the records show:
- **Solved, not counted.** b144, b156, b177, b187, b189 and b202 were solved UNSAT by CaDiCaL 3.0.1 under rev-15 staged transport in 26.65, 12.27, 134.5, 23.65, 108.41 and 123.92 s. They are not counted (F-A class transport).
- **Checker refused.** v6 b295: the solver printed `s UNSATISFIABLE` within 300 s, but the checker was refused at STOP-K1.
- **Direct timeouts at 300 s:** rev-15 b68, b73, b77, b162 and v6 b74, b151.
- **Never attempted.** The other 73 open cases have no direct `build_v2` attempt on record.

The records come from the v6 contract rows `cycle2/m2-ms06-initial-v6-contract-20261018T075542.json` (dc343809…2413) and the frontier v6 attempt pins. Suggested tiers, each needing its own item GO:
- **Tier 0:** direct re-solve under the file transport of the pilot runner for the 7 cases with solver-UNSAT history.
- **Tier 1:** first direct attempts for the 73 never-attempted cases.
- **Tier 2:** this split, for the six timeouts and any Tier-1 timeouts.

Tiers 0 and 1 need only a runner variant whose item builds F_b instead of a partbatch.

## 8. Experiment 1 (proposed; frozen source, NOT run)

- **Source:** `code/probe_ms06_split_census_v1.py`, sha256 fb9e516456139592c147176b684ca3291c686ff468b21463a614b9ad88be8b05. It was compiled in memory for syntax only and never executed. It is stdlib Python with an in-process import of the vendored encoder (d0002e60…), and its only child process is `/bin/date`.
- **Pinned inputs:**
  - skeletons-b-ms06 (9ec0fd1d…);
  - frontier-v1 (0e7e4370…);
  - ms06-dp-v1 (8c2c44b2…);
  - the GPS-1 receipt (67170e7b…);
  - the v6 ms06 contract (dc343809…), plus the direct-attempt records it and the frontier pin;
  - the vendored encoder.
- **Computes:**
  - for all 86 cases: K_raw(b) by enumerator A (D first) and enumerator B (E first), which must be equal; signature and orbit counts at levels E, D and ED, with Aut-closure and union-find consistency checks; |Aut| against `ms06-dp-v1`; the old GPS-1 witness ∈ K_raw(b); frontier fields against the skeleton file;
  - for one pilot case: the fewest Level-E orbits among the direct-timeout cases {68, 73, 77, 162, 74, 151}, ties to the smaller b.
- **Pilot-case checks:**
  - it rebuilds F_b and compares the digest with the case's direct-attempt record;
  - it checks the U numbering and the witness clauses, and the serialization;
  - it pins in memory the sub-case CNF digests, headers and appended clauses for every Level-E and Level-D representative. Nothing but the JSON is written.
- **Bounds:** self budget 280 s with no output when exceeded; receipt with PID written before any work; admission requires fresh free space ≥ 12.2e9 + 16 MiB and no STOP/HALT/SAT-candidate marker; output created exclusively at `evidence/probes/ms06-split-census-v1.json`.
- **Run command once the parent decides:** `cwd LANE; env -u PYTHONOPTIMIZE TMPDIR=LANE/tmp PYTHONDONTWRITEBYTECODE=1 <python3.14 Cellar file> -B code/probe_ms06_split_census_v1.py LANE/evidence/probes/ms06-split-census-v1.json`, with tool timeout 0.
- **Use of the result:** planning only. Per-case orbit counts replace the 566M alarm with the actual number of sub-cases at each level. Any `all_ok = false` is a defect to fix in a v2 source, not a result.

## 9. Experiment 2 (design only; needs a new reviewed runner version and a parent item GO)

- **Items:** the first three Level-E sub-cases, in canonical order, of the experiment-1 pilot case, with CNF digests pinned by experiment 1.
- **Method:** the same as the pilot runner (kissat 4.0.4 `--seed=1` with a 600 s native limit, drat-trim with a 1200 s limit, file transport with retained CNF and DRAT, the same-binary controls), one child at a time.
- **Worst case:** 3 × 1,800 s within one 10,800 s chunk.
- **Runner change:** a new runner version replaces the partbatch item builder with "F_b + Φ_s", checked against the pinned digests. It needs a hostile review (Codex) before any GO.
- **Risk:** proofs from 600 s kissat runs on these formulas may exceed the 1.2 GiB per-item proof cap. The v6 b74/b151 CaDiCaL proof streams at 300 s were 0.68/0.60 GB raw. A cap hit is fail-closed UNKNOWN.
- **Decision rule (planning):**
  - if at least 2 of the 3 are checked UNSAT, request a GO for the rest of the case's Level-E set;
  - if all 3 time out, request one Level-ED refinement of the cheapest node before anything else.

## 10. Risks and open points

- The sub-case hardness is unknown. Pair blocks plus the leave pair may not make the formulas easy, and a Level-ED blow-up is possible for cases with many types (up to 9 types, |Aut| = 1–72).
- The class-level leave clause is a disjunction, not a unit. A Level-ED representative with large classes gives clauses of up to about 16 U literals.
- The n4 consequence of section 1 and the triple-layer Gram corollaries (old lane notes) are candidate written strengthenings; none is used in v1.
- Inherited unresolved binding items still apply: the m2k3 race (an ms09 item), F-A, F-D, the lrat-check unsoundness (lrat is never used here) and the disk-floor breaches.
