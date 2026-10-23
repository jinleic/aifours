# Hostile audit: PA19 necessary conditions GPS‑1, GPS‑1|C1 (ms09, ms06), GPS‑2|C1, and the orbit bridges

## Scope and assumptions

**What was done.**
- I read S00–S04 statically. Nothing was executed, and no SHA256 was recomputed.
- I compared only the cross‑reference strings, and all agree:
  - S00:11, S00:48 and S00:70 match the S02, S03 and S04 header SHAs.
  - S03:34 and S04:27 match S00:31.
  - S04:28 matches S00:58.
- S00 line numbers are snapshot LF (original line = LF + 1001).
- No count, percentage, survivor, interval, orbit or list‑completeness result is accepted (S00:31‑38, 58‑61, 77‑89).

**Assumptions.**
- **(A1)** Two distinct rows agree in at most one column. Profiles are exactly P0 = (4,3,3,3,3,3) and P1 = (4,4,3,3,3,2), with N = 19 and k = 8. For ms09 (c0, m, L) = (5, 3, 0); for ms06 (c0, m, L) = (6, 2, 1).
- **(A2)** T(r) is the set of P0 columns whose unique 4‑block contains r. Every quad has exactly 4 rows (S02:51).
- **(A3)** A placement (A1, B1, P1) is the two 4‑blocks and the 2‑block of one P1 column, indexed in the same labeling as T.

## Verdicts

| Item | Verdict | Findings |
|---|---|---|
| GPS‑1 | **ACCEPT** | m1, m2 |
| GPS‑1\|C1 ms09 | **AWF** | M1; m1, m3 |
| GPS‑1\|C1 ms06 | **ACCEPT** | m1, m3, m4 |
| GPS‑2\|C1 (per‑placement necessity) | **ACCEPT** | m3, m5, m6 |
| Orbit invariance | **AWF** as mathematics; **INCONCLUSIVE** as a bridge to the frozen lists | M2 |
| Probes generally | n/a | m7 |

No FATAL finding.

## Checks

### GPS‑1

**Row identity.** Under (A1), the sets of rows that r agrees with in different columns are disjoint. So Σ_c(|block_c(r)| − 1) = 18 − l(r).
- P0 columns give 2c0 + t, and P1 columns give 2m + Σe_j.
- Since 2k = 16, t + Σe_j = 2 − l and n4 − n2 = 2 − l − t (S00:5). ✓
- From n4 ≥ 0 and n2 + n4 ≤ m, the interval at S00:6 follows. ✓ The bound n2 ≤ m is implied, so `min(m,·)` (S02:58) is redundant but harmless.

**Tabulated (lo, hi) for n2:**

| Case | t = 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| ms09 | (0,0) | (0,1) | (0,1) | (1,2) | (2,2) | (3,3) |
| ms06 non‑leave | (0,0) | (0,0) | (0,1) | (1,1) | (2,2) | infeasible |
| ms06 leave | (0,0) | (0,1) | (1,1) | (2,2) | infeasible | infeasible |

- The b3 and b30/b44 reductions (S00:9) follow from the ms09 row and agree with S01:9‑11.
- **Pair blocks.** E has exactly m pairs (one per P1 column), pairwise distinct, each T‑disjoint (S00:7). ✓
- **L = 1.** The 170 agreeing pairs are distinct, so exactly one pair agrees nowhere. Then l = 1 exactly on x and y, T(x) ∩ T(y) = ∅, and {x, y} ∉ E (S00:8). ✓
- **Column totals add nothing at skeleton level.** Σ(n4 − n2) = 38 − 2L − 4c0 = 6m in both cases.
- No over‑strong clause found. Exclusion is one‑directional (S00:10).

### GPS‑1|C1, ms09

**Pair‑block memberships.** Here s = 2 − t − e1 ∈ [−2, 2]. The n2′ bounds give:
- s ∈ {1, 2}: no pair block;
- s = 0: at most one;
- s = −1: exactly one;
- s = −2: both.

S03:63 matches.

**+1 allocation.** From e2 + e3 = s:
- s = 2 gives (+1, +1);
- s = 1 gives exactly one free +1;
- s = 0 gives +1 in the column opposite its pair block, else (0, 0);
- s ≤ −1 is never +1.

**Count equations.** Let a_k = #{s = k}. Let x be the number of s = 1 rows at +1 in column 2. Let y2 and y3 be the numbers of s = 0 rows in P2 and in P3.
- column 2: a₂ + x + y3 = 8
- column 3: a₂ + (a₁ − x) + y2 = 8

Both equations are necessary.

**Why column 3 follows from column 2.**
- Σs = 38 − 0 − 20 − 6 = 12 = 2a₂ + a₁ − a₋₁ − 2a₋₂.
- |P2| + |P3| = 4 = 2a₋₂ + a₋₁ + y2 + y3.
- Hence 2a₂ + a₁ + y2 + y3 = 16, so column 2 ⇔ column 3.

The README's "iff" is therefore true, but only of this relaxation, and only through an identity it never states. The (13,5,4) control shares Σs = 12.

### GPS‑1|C1, ms06

Fixing the leave pair forces e2 = 2 − l − t − e1. All conditions at S00:46 are necessary:
- every e2 lies in {−1, 0, 1};
- exactly two rows have e2 = −1, and they form a T‑disjoint pair that is not together in A1, B1 or P1 and is not {x, y};
- the leave pair is T‑disjoint and not together in a column‑1 block.

Σe2 = 38 − 2 − 24 − 6 = 6, so "#(+1) = 8" and "#0 = 9" follow from "#(−1) = 2". This is redundant but consistent.

### GPS‑2|C1

Rows sharing any column‑2 block agree there, and therefore nowhere else. So every block is pairwise T‑disjoint, contains no two rows together in A1, B1 or P1, and never contains both leave rows. The block sizes are forced by e2 (S00:65‑68).
- This holds for every completion. Column‑1 triples, P0 triples and symbols stay free, so it is a relaxation.
- GPS‑2|C1 ⇒ GPS‑1|C1 ⇒ GPS‑1, since {P1, P2(, P3)} plus the leave pair is a GPS‑1 witness.
- So S00:50 and S00:72 are implications, not independent tests.

### Orbit invariance

**The group.** Let G = {(σ, π) : T(σr) = π(T(r)) for all r} × ⟨A/B swap⟩, with σ acting on rows and π on P0 columns.

**The argument.** For any valid array M with skeleton T, form gM by moving rows by σ, moving P0 columns by π, and swapping the two column‑1 4‑block symbols.
- gM is valid, with the same profiles, L and T.
- It maps the P1 column ρ to gρ.
- So "no array has ρ as a P1 column" transfers to every gρ.

**Consequences.**
- No predicate invariance is needed, so the argument also covers the probes' internal WLOG choices.
- Transpositions of rows with equal T lie in G (π = id).
- Per‑placement necessity never uses which P1 column is "first", so no P1‑column symmetry is needed.
- The argument fails for row maps that preserve only t, or a class label coarser than T. The claims at S00:47 and S00:69 therefore hold only for subgroups of G.

## Findings

### MAJOR

**M1 — GPS‑1|C1 ms09: the written test differs from the implemented test.** There are three distinct formulations:
- **README** (S00:45): only the column‑2 equation. It never defines P2/P3, and says "Feasible iff" without quantifier or scope.
- **Probe** (S03:71‑84): tests column 2 only, under the WLOG r0 ∈ P2. That WLOG rests on the unproved remark "column 3 then has 8 automatically" (S03:14).
- **Verifier** (`verify_L0`, S03:123): tests both equations.

These coincide only through the identity above. Without it, the written lemma does not cover the probe's exclusions, because the WLOG needs column 2 / column 3 symmetry. Necessity itself is unaffected. The probe's test can also be shown necessary directly, by labeling the two remaining columns so that r0 ∈ P2.

*Fix:*
1. Define P2 and P3 as the pair blocks of the two remaining columns.
2. State both equations and the identity.
3. Rewrite the claim as: "R_C1(ρ) holds iff there exist distinct P2, P3 satisfying S00:43 and x ∈ [0, a₁] satisfying both equations."
4. Document the r0 WLOG.

**M2 — orbit bridge undefined.** S00:41, S00:47 and S00:69 invoke "Aut(skeleton)" with no definition or proof. The probes pair T in `rows_of` order (S03:165, S04:122) with ext.json row indices. The only check on that pairing is the sanity filter S03:50‑54.

*Fix:*
1. Define G as above.
2. Insert the solution‑set argument.
3. For each consumed list, verify that ext row i has T = rows_of(sk)[i], or is related to it by a recorded map in G.
4. Verify that every recorded generator satisfies T∘σ = π∘T.

S00:86‑89 binds metadata only and does not establish this.

### MINOR

- **m1 — notation clashes.**
  - "s" means block size at S00:5 and the residual at S00:42.
  - "L1" labels an equation (S00:3, S00:8) alongside the case L = 1.
  - "P1" is a column type, the column‑1 pair (S00:42) and a condition name (S02:14).
  - "P3" is the column‑3 pair (S00:45) and the leave condition (S02:16).

  Rename them.
- **m2 — S00:9 and S00:10 wording.** At S00:9, write "E, and {x, y} only when L = 1". At S00:10, item (5) is the contrapositive of the conjunction, not the conjunction itself.
- **m3 — S00:47 and S00:69 cite "GPS (1)‑(4)".** In fact S00:44 uses the P1 profile count (two 4‑blocks, one 2‑block), and S00:68 uses co‑membership in 3‑ and 4‑blocks. State both premises explicitly.
- **m4 — S00:46 wording.** Quantify as "there exists {x, y}". Note that the 8‑count follows from the 2‑count.
- **m5 — the monotone control (S00:72, S00:77) is vacuous for b68.** S03:180 stores excluded indices only when there are at most 2000. The record gives 7,806 for b68 (S00:78), so S04:121 receives ∅. This is not a premise, because monotonicity holds by construction (S04:62‑67 includes every test in S03:94‑100). Say so, or store the full index list.
- **m6 — the controls are aids, not proof.**
  - C2 searches the T derived from the model and compares the reference skeleton only by sorted t (S02:150‑153).
  - The GPS‑2 unit control uses leave = () and splits only 4‑blocks (S04:103‑105).
  - There is no L = 1 positive control at all (S00:26, S00:75).
- **m7 — C4 re‑checks only feasible witnesses** (S00:14, S00:52, S00:74). Exclusions, the only load‑bearing output, have no independent checker.

## Remaining unverified

- List completeness.
- The ext.json row order and automorphism generators, checked against G.
- Exhaustiveness and correctness of every exclusion search (S02:77‑110, S03:57‑102, S04:44‑73).
- The b3 parent record (cited at S00:2, not supplied).
- All counts.
- The unpinned import `m2_supervised_runtime_v6_3` (S02:29).
