# Referee report: exact-anchor Lemma U and corrected R1

## Verdicts

| Object | Verdict |
|---|---|
| **Lemma U**: anchor `3c8dbe62…`, rows in file order, normalised at row 0, columns in file order | **ACCEPT**. Computer-assisted, exact anchor only, and conditional on the integrity of the embedded records. |
| **Corrected R1**: base `eabe1fc4…` plus E1 `74bc52ca…` (Proposition, converse, Consequence 1) | **ACCEPT-WITH-FIXES**. The mathematics is correct given Lemma U. The fixes concern scope and record hygiene; none of them changes the Proposition. |

- **FATAL:** none.
- **MAJOR:** one (M1), in R1 Consequence 3, which is outside the core.
- **MINOR:** m1–m12, listed under the section they belong to.

Lemma U has no Lean or other formal proof and no human-checkable certificate. It stays a computer-assisted, exact-anchor result. R1's derivation from Lemma U is a short human proof, and I re-derived it. Both the beta route and the free one-row extension remain UNKNOWN. Nothing here bears on a seven-row DM over Z39, on CFR(6,39) or on six MOLS(39). I make no novelty assessment.

## 0. What I checked myself and what is recorded execution

**My proof audit (reading only):**
- the CRT/rainbow reduction;
- the gauge;
- the logic of all three programs;
- R1's proof.

**My hand arithmetic on the embedded bytes:**
- D0 mod 13 starts [0,1,12,0,0,10,3,10], which confirms the fact E1 relies on.
- Rows 1–5 of both parent representatives equal α and −α as computed from the raw anchor. I checked all 39 entries of each row.
- Spot checks only: D1−D0 is a permutation of Z39, and the fibre T01(0) = {0,15,16} is rainbow.
- The unit 14 satisfies 14 ≡ −1 (mod 3), 14 ≡ 1 (mod 13) and 14² = 196 ≡ 1 (mod 39).
- In the S4 table, the unknowns, ranks, dim V and m are mutually consistent.
- The parent's stdout is 123 bytes, which is exactly what `print(json.dumps(...))` of result.json's values produces.

**Recorded execution, which I did not reproduce:**
- Route 1 (S4a): its stdout `fd06bafb…` is not embedded, so I have only the worker's transcription in the S4 table.
- Route 2 (L1–L4): the index summary is embedded; the raw out.json files are not.
- Parent: result.json is embedded.

**Hashes:** I recomputed no SHA-256. I only checked that the hex strings agree across files, and they do:
- source → result → receipt → endpoints;
- input pins;
- representative digests;
- route 2 stdout = out_json in every run, as the code implies (it writes `txt+"\n"` and prints `txt`).

## 1. CRT/rainbow equivalence: no defect

- **DM criterion.** c ↦ D′x(c) − D′y(c) is a bijection onto Z39 if and only if its CRT image c ↦ (αx − αy, βx − βy) is a bijection onto Z3 × Z13. That holds exactly when every β-fibre Txy(t) has 3 columns and αx − αy takes all of Z3 on it.
- **Lifts.** For a fixed β, the 6-row DMs with row 0 equal to zero and mod-13 part β are exactly CRT(A, β) with A rainbow and A0 = 0.
- **Contrast criterion.** Three zero-sum elements of Z3 are either all equal or all distinct (if a+b+c = 0, then c = a ⇔ b = a). So on V = {fibre sums 0, A0 = 0}, A is rainbow if and only if every chosen contrast is nonzero.
- **What the programs build.** All three programs use all pairs x<y, including row 0, build fibres from mod-13 differences, and check fibre size 3.
- **Phrasing of the route.** It does not matter whether the route is phrased with D mod 13 or with D′ mod 13. Fibres depend only on row differences, and an unnormalised lift differs from a normalised one by a column function.

**m1.** R1's Setting says "every 6-row DM with skeleton β arises so". It should say "every 6-row DM E with E0 = 0 and E mod 13 = β". A general DM arises only after normalisation.

## 2. Gauge quotient: no defect

**Row constants.**
- Row constants e (with e0 = 0) lie in V, leave every contrast unchanged, and act freely.
- The map A ↦ A − (Ax(0))x picks a unique representative with column 0 equal to zero.
- So the gauge used by route 2 and the parent is data-independent and loses no class, and #lifts = 3⁵ · #gauged lifts holds for every input.

**Route 1's quotient.**
- Route 1 instead counts im F ≅ V/ker F. That quotient is data-dependent, and it equals V/constants only if rank F = dim V − 5.
- The parent's result alone settles this. If some non-constant N lay in ker F, then α + N would be rainbow and would lie in a third class: α + N ≡ −α would force F(N) = F(α) ≠ 0, a contradiction.
- Therefore "gauged dim 5, 2 rainbow" (parent) implies dim V = 10, ker F = constants, rank F = 5 and 2 of 243. That is every clause of Lemma U.

**Structural sanity checks.**
- For each pair 1≤x<y, Σt Exy − Σt E0y + Σt E0x = 0 identically. These are 10 independent relations among the 195 fibre equations.
- Hence rank ≤ 185 and gauged dim ≥ 5 for any input of this shape. Route 1 and the parent both report exactly these extremal values.
- Negation is a fixed-point-free involution on rainbow classes, since F(−A) = −F(A) ≠ F(A). So every class count is even and contains ±α. The reported 2 and 4 both comply.

**m2.** The S4 column header says "mod constants", but the probe reports `rainbow_points_mod_kernel`. The two are equal only because functional rank = m in every row; S4 should say so.

## 3. Enumerators on the pinned inputs

The anchor meets every precondition: it is a DM, all fibres have size 3, 39 = 3·13, the gauged dimension is 5 (within the parent's cap of 6), and the m ≤ MMAX gate was passed (a count was produced).

**Route 1 (`probe_mod3_lift_v1.py`)**
- Sparse forward elimination followed by back-substitution gives a reduced row echelon form (RREF), and the nullspace basis taken from the free columns is correct.
- The column echelon of F over that basis picks a basis of im F. The map z ↦ Σ zᵢF(bᵢ) is a bijection from GF(3)^5 onto im F, so counting images with all coordinates nonzero counts the rainbow classes exactly.
- There is no pruning, and the full enumeration is 243 points.
- The budget check (`tot & 4095`) cannot fire below 4096 points. An early budget stop produces no count, never a wrong count.

**m3.** Route 1 never builds a lift and re-checks it against the definition. Together with its unembedded stdout, this makes route 1 corroboration only, not a basis for acceptance.

**Route 2 (`lift_route2.py`)**

Every pruning step is a necessary condition:
- **Domain filter.** A value w is removed only if it would repeat a difference already present in the fibre.
- **Linear layer.** It holds only the fibre-sum equations and the branching decisions. I checked `lin_add_equation`, `lin_assign` and `_subst`:
  - the GF(3) inverses are right (a⁻¹ = a);
  - pivots never appear in free parts;
  - assigned cells are always eliminated;
  - a contradiction is raised exactly when the system plus the decisions is inconsistent;
  - only values the system determines are forced.
- **`fibre_ok`.** It re-checks every fibre touched by a changed cell.
- **Empty domain.** A cell with no remaining value ends the branch.

Exhaustiveness and leaf checks:
- Each branch tries the chosen cell's whole filtered domain, and `list(vals)`/`copy_rows` keep branches from sharing state. So every gauged lift is reached exactly once.
- Each leaf is a full array that is re-checked by `is_lift`, which is the definition. Duplicate leaves raise an error.

Status integrity:
- COMPLETE is set only when the search returns without the budget exception.
- A failure at the root produces no leaves and then fails the T/−T self-test with INTERNAL_ERROR. It never yields an empty COMPLETE.

Controls:
- L3 (Singer k8) found 4 classes, two of them "other". It is the real power test: the engine is not biased toward ±T.

**m4.** The comparison against pure DFS (L2 vs L1) checks the linear propagator only on DM21; the anchor is out of reach for pure DFS. This is mitigated by my code audit and by the parent run.

**m5.** The Singer generator is copied between routes 1 and 2. The L3 agreement is therefore engine-independent but not input-independent. That is acceptable for a control.

**Parent dense (`parent_dense_lift_v1.py`)**
- It sets up 190 gauged cells and 195 equations and runs a full Gauss–Jordan elimination.
- The parametrisation x_p = −Σ eq[j][c]·x_c over all 3^|free| free assignments visits every gauged solution exactly once.
- Acceptance is the literal definition: each fibre's differences must be {0,1,2}.
- Soundness does not depend on the RREF. Completeness does; that elimination is standard, and route 2's search independently corroborates it.

## 4. Parent control

**What is solid:**
- The code is independent: no worker imports, and it is a dense method rather than a sparse or search method.
- The run is supervised and SETTLED, with rc 0, no trips and no remaining descendant processes.
- `source_sha256` is computed by the running file itself and equals the pinned `94dff08b…`, and the input pin is the anchor.
- The printed representatives are ±α (my hand check), and their digests equal route 2's L4 digests.

**Its limits.** It is a scope-restricted confirmation check, not a general solver:
- It stops with `ENUMERATION_SCOPE_EXCEEDED` above 6 free variables.
- It raises an error unless the result is exactly 2 classes, 486 lifts, dimension 5, and the set {T, −T}.
- The expectation gate sits after a deterministic computation, so it cannot bias the reported values.

**m6.** The DM3 positive control is degenerate (q = 1, k = 2: one fibre, no relations). Both mutations are rejected by elementary necessity: changing one cell of a rainbow triple in Z3 always creates a collision, and changing one entry of a DM row always breaks a bijection. These controls only show the checkers are not vacuous. The substantive engine controls are route 2's L1–L3.

**m7.** A run that disagreed would have left only a traceback and a nonzero return code, with no record of the disagreeing numbers. For future runs: write the record first, then gate.

**m8.** Route 2's child launch identities were registered after completion. This weakens pre-registration for L1–L4. My verdict does not depend on it, because the parent's own supervised run reproduces the anchor result.

## 5. Exact-anchor count: accepted

The accepted result is for the anchor (`3c8dbe62…`, rows in file order, normalised at row 0, columns in file order):
- dim V(β) = 10;
- ker F = the row constants;
- exactly 2 of the 243 classes are rainbow, namely ±α;
- there are 486 lifts.

**Evidence:**
- two independent complete enumerations whose embedded records agree down to the representative digests (route 2 L4 and the parent);
- route 1, recorded but not visible to me.

**No negative-count inference.** "No third class" rests on complete enumerations: route 2's COMPLETE status, the parent's full 243-vector loop, and route 1's full 243-point loop. It does not rest on absence within a time budget.

**Not promoted.** This audit does not promote the other S4 rows (DM21/33/51, P21, Singer). DM21 and Singer-k8 agree with route 2 only in their role as engine controls.

## 6. Corrected R1

**Re-derivation**
1. Let D*′ = D* − D*0. D*′ is still a DM, and its rows 0–5 form a 6-row DM with skeleton β.
2. By Lemma U, the mod-3 part of rows 0–5 is εα + e. The sign ε is unique, because F(−α) ≠ F(α).
3. With μ ≡ ε (mod 3) and μ ≡ 1 (mod 13), we get μD*′x = D′x + rx, where each rx ∈ {0,13,26} is constant along the row.
4. Then Dx − f = D′x − μD*′6 = μ(D*x − D*6) − rx. This is a bijection because μ is a unit.
5. So f = μ(D*6 − D*0) + D0, and [D; f] is a DM.

**Converse:** D* = [D; f] gives β6 = (f − D0) mod 13, with ε = 1, e = 0 and μ = 1, and the map returns f.

**E1 is correct.** The proof gives g = μD0, and g ≡ D0 (mod 13), which is nonzero (column 1 has D0 = 1). The original clause is what one gets for the normalised anchor [D′; f] with g = 0, so the base error is a D/D′ conflation.

**Imports (exact list)**
- R1 uses only the class statement of Lemma U (it does not need dim V or rank F).
- It also uses three invariances of the DM property: under column translation, under adding a constant to a row, and under multiplying by a unit.
- It uses the CRT.
- It uses nothing from T2/T6, G6/C3/C2 or the S4 rows other than the anchor.

**Scope**
- The labelled anchor, together with any 7-row DM D* whose columns are identified with C and whose six old rows, in anchor order and normalised at the first, have skeleton β.
- Permuting the rows of D* is free, so this is exactly the beta route's hypothesis.
- The result is an existence equivalence with explicit maps in both directions (D* ↦ f maps onto the set of extensions). Both questions remain UNKNOWN.

**M1 (MAJOR, Consequence 3; does not affect the core).**
- The claim "genuinely wider" is not established. An extra sign pair ±α′ only means the route also covers extensions of CRT(α′, β), which may be equivalent to CRT(α, β); E2 itself says this was "not examined". No extension is exhibited.
- "6-row lift space" is the wrong description: the Singer objects have 8 and 7 rows.
- "It is not [wider]" for DM21/33/51 and P21 rests on unaudited route-1 rows and on an unstated per-object analogue of R1.
- **Fix:** restrict Consequence 3 to the anchor, or downgrade it to "potentially wider; unreviewed single-producer observations".

**m9.** The base file still shows the withdrawn clause and the wrong converse (β6 = f mod 13). Every citation of the base file should be paired with E1, or both should be replaced by a consolidated v2. Any positive control built under Consequence 4 must use β6 = (f − D0) mod 13.

**m10.** E1 calls the original clause "false as stated". What is actually shown is that the clause is unsupported: the proof yields g = μD0. Because the existence of any D* is open, the universally quantified clause cannot be refuted; it is vacuously true if no D* exists. The withdrawal is still correct.

**m11.** R1's status and provenance lines are stale: "single-producer", "second route being prepared", "UNREVIEWED". They should cite route 2 L4 and the parent control, and include the two-line derivation from §2.

**m12.** Consequence 1's imported statuses (UNKNOWN at 270–282 s; the COMPLETE negatives as "special cases") were not reviewed here and are not needed for R1. "Special cases" must not be read as transferring those negatives to the beta route, since the D* ↦ f map does not track equivariance.

Consequence 2 is labelled as a heuristic. I reproduce its order of magnitude (≈0.9 expected β-solutions). Its claim "strictly looser" is unproven but harmless.

## 7. Citable scope

> Computer-assisted, exact anchor only: the rainbow mod-3 lifts of the anchor's mod-13 skeleton are exactly ±α + row constants (2 classes, 486 lifts). Given that, a human proof shows that one-row extensions of the exact anchor exist if and only if beta-route extensions of its skeleton exist; both are UNKNOWN. There is no formal (Lean) proof and no certificate. No statement is made about other DMs, CFR(6,39) or six MOLS(39), and the non-anchor S4 rows are not promoted.

**Optional strengthening, not required for these verdicts:** a small certificate would let a tiny independent checker, or Lean, re-verify Lemma U without trusting any of the three programs. It would contain:
- the 5 gauged basis vectors;
- an echelon witness that the rank is 185;
- for each of the 241 non-rainbow points, one fibre where it fails.
