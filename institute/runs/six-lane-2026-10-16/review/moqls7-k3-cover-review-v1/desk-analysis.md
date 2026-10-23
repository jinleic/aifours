# K3 cover / G6 / lex / AMENDMENT-4 — desk static analysis (M7K3CoverReviewDesk)

Written 2026-10-17 PT while the two CLI reviews ran. It is the desk's own static reading of the pinned snapshot
(`snapshot/`, manifest `836c336a…a47d`), and is separate from the reviewer notes. No solver, CNF generation, replay or
mathematical script was run. Desk byte facts come from reads and SHA-256 only (`snapshot/desk/cnf-static-excerpts.txt`).
This file gives no K3 or M(7) verdict.

## Byte-level facts (desk reads/hashes)
- The current files match all pinned hashes, including draft AMENDMENT-4 `d9794b9d…47d7ee`, which is unchanged.
- The CNF SHA-256 values match every metadata, screen and certificate receipt:
  - A_C311 `7fca33f1…2001`; A_C321 `d598507d…8388`; A_C411 `2b92f5b1…ddf2`.
  - B_C321 `8b7b8124…12c6`; lex A_C311 `059be616…8c4f`.
  - The cert_r2 copies are byte-identical to the explore copies.
- Headers agree with the metadata arithmetic:
  - A cubes: nv 96978, with 627398 + 88 = 627486 clauses (C321) or 627398 + 158 = 627556 (C311/C411).
  - B cubes: nv 461370, with 1629644 + 88 or + 158 clauses.
  - Lex: 96978 + 10535 = 107513 variables and 627556 + 31612 = 659168 clauses.
- Checker logs: 96978 variables with 627486 / 627556 clauses, then `s VERIFIED` (lines carry a leading CR).
- For each cube, the appended blocks of A and B are byte-identical (same SHA-256).
- Hand recomputation of the A_C321 tail:
  - Index of g_a((0,k),(1,0)) is 882(a−1) + 36k + 1, giving 37, 73, 109, 145, 181, 217 / 919… / 1801… .
  - g_3((1,0),(2,1)) = 2017.
  - The G6 pattern: 10 units with p-collinear t, 10 units with q-collinear t, 25 equality pairs, and 2 skipped t. Total 70 per singleton.
  - All of these match the bytes.
- The first lex comparator at line 627558 is the pair (7,13) = g_1((0,0),(2,1)) ↔ g_1((0,0),(3,1)) under rows (2,3).
  The last clause `-107513 -2646 1763` is the final pair of columns(4,5)+squares(2,3), with no new auxiliary.

## Q1 cover — SOUND
- S_a ⊆ {1..6}. Coordinate 0 is absent because (0,0) and (1,0) are collinear.
- S_a ≠ ∅ by unit norm in the row-0 ONB (at Boolean level, G3 with ℓ1 = column 0, ℓ2 = row 0).
- The S_a are pairwise disjoint by G5. The --sym units give S_1 ⊇ {1,2,3}.
- So S_1 = {1,2,3} ∪ X with |X| ≤ 1:
  - X = ∅: 6 assignments of type (1,1)+unused, plus 3 + 3 of type (2,1)/(1,2).
  - |X| = 1: 6 assignments.
  - Total 18 = 64 − 27 − 27 + 8. These are exactly the three 6-element orbits under S3(4,5,6) × ⟨swap 2,3⟩.
  - The 0-based `3 - a` swap in coverage() is correct.
- The residual operations fix row 0, rows 0/1, column 0 and columns 1–3. They therefore preserve:
  - the --sym units;
  - G1 by absence, G2/G3 on all lines, and G5;
  - every G4 constraint, with (square 1, row 0) mapped to itself.

## Q2 G6 — SOUND
- Same-ray: ψ_p = λψ_q with |λ| = 1. This holds for any field or phase.
- G1/G2 derivation, case by case:
  - t on row 0: both sides are 0, by the cube unit or G1.
  - t off row 0: the number of common row-0 neighbours of p and t equals g(q,t).
    - G2 with count 0 or 1 gives equality.
    - If p and t are collinear, count 1 is forbidden, so g(q,t) = 0.
- Clause level, encoder A:
  - h_r is forced to 0 for r ≠ q.
  - h_q ↔ g(t,q), or is absent when t is collinear with q.
  - The two G2 clause families then reduce as stated.
- Encoder B: counter2 is a full ≥1/≥2 equivalence, and the collinear `(-s1, s2)` branch forbids count 1.
- The wrapper's four None cases are correct. Skipping t ∈ {p,q} is correct: the diagonal is 1, and t = p is the existing unit g(p,q) = 1.
- Variable map:
  - A is asserted equal at runtime.
  - B's `gv` loop is the first allocation and is identical in order (squares, PTS lexicographic, non-collinear), so indices 1..2646 agree. This holds by static reading only.
- **MINOR (Q2/Q4).** AMENDMENT-2.r1.md:43-45 says the wrapper "reads each encoder's actual g-variable order" and "must confirm" agreement. For B the wrapper only checks `int(nv) >= len(vmap)` (k3_cubes.py:121). Fix: state that B equality rests on static reading of gram_encB.py:118-124, or add a runtime cross-check in a new wrapper version.
- **MINOR (wording).** G6-G2-DERIVATION.r1.md:5-6 says the cube fixes "all g(p,r)=0 for r in ell other than q". For r = (0,0) the predicate is absent by G1, not fixed by a cube unit.

## Q3 lex — SOUND
- Generators match AMENDMENT-3: 7 for C311, 7 for C321, 8 for C411 (22 in total). Each is a product of commuting transpositions, hence an involution.
- They preserve the base (G1–G5, the G4 set with (1,row0) fixed), the signed 18 units, and G6.
- C411 column (3,4) moves the base --sym unit g_1(p,(0,3)) to g_1(p,(0,4)), which is a C411 cube unit. Invariance therefore holds for the base+cube solution set, not for the base CNF alone.
- Convention: perm[v] = idx(σ·pred v). The comparator uses Y = X∘σ, which is the pattern of σ⁻¹C, so it lies in the orbit for any σ. Involution is not even needed.
- Comparator: e_1 ≡ true, e_{i+1} ⇐ e_i ∧ (x_i = y_i), and e_i → (¬x_i ∨ y_i).
  - Satisfiable iff X ≤lex Y, with e = 1 up to the first difference and 0 after.
  - At a first difference with x = 1, y = 0, the forced chain violates the clause.
  - This holds when pairs share variables. Skipping v with perm[v] = v is harmless, and fresh auxiliaries start at old nv + 1.
- Counts: 1386 moved predicates gives 3·1386 − 2 = 4156; 2226 gives 6676; total 31612 clauses and 10535 auxiliaries. These match the metadata and header.
- Coverage: the lex-minimal member of the H-orbit of any actual configuration in the cube satisfies X* ≤ X*∘h for every h ∈ H, simultaneously for all generators. Base auxiliaries are definitional or existential, so they are reconstructible. No invariance is assumed.
- **MINOR (Q3/Q4).** AMENDMENT-3.r1.md:45-46 requires binding the "original cube CNF SHA, metadata, …". The lex metadata (k3_lex.py:121-125) and AMENDMENT-3.bindings.r1.json bind the source cube CNF SHA but not the source cube metadata SHA (`3b2ab04f…`). The values cross-check, so this is a binding gap, not a soundness gap.
- **MINOR (doc).** AMENDMENT-3.r1.md:25 should define T(X)_v = X_{T(v)}, matching the code. This is harmless for involutions, and for orbit coverage in general.

## Q4 composition — SOUND, with the binding notes above
- In both wrappers the base or cube text is copied unchanged. Only units, G6, or comparator clauses are appended, and the headers are recomputed.
- Certificate driver r2 regenerates with the frozen wrapper and asserts `sha(cnf) == screen["cnf_sha256"]` (k3_cube_certify_r2.py:45-46). The receipts bind the CNF, metadata, screen, code pins and logs.
- No four-square lemma is used. LEMMAS W is the three-square bound.
- **MINOR (citation).** AMENDMENT-2.r1.md:5 cites the G4 bridge as `GRAM-ENCODING.r1.md`, whose G4 text cites K1 §8. That dependency error was corrected in GRAM-ENCODING.r2.md:52-65 and LEMMAS.md:69-78. Cite r2/LEMMAS in any revision.
- K1 and K2 dependence is explicit in AMENDMENT-2.r1.md:5-6 and in the receipts' scope.

## Q5 draft AMENDMENT-4 — mathematically SOUND in principle; REQUIRES FIXES before any freeze
These conclusions are conditional on accepted A/C321 and A/C411 certificates and on G4 (K1 accepted, K2 pending).

- Transport for a row frame ℓ:
  - Use ρ: ℓ ↦ 0, row(p) ↦ 1, and κ: col(p) ↦ 0.
  - Columns: N_a ↦ {1..4} and the singletons ↦ 5, 6 for C411; or N_a ↦ {1,2,3}, N_b ↦ {4,5}, N_c ↦ {6} for C321.
  - Squares: a ↦ 1, b ↦ 2, c ↦ 3.
- For a column frame, transpose first.
- The image is again a minimal heavy triple and satisfies the exact 18 units. It also satisfies the --sym units, because columns 1–3 are contained in the image of N_a. It satisfies every G4 constraint and G6.
- So every own row/column (ℓ, p) obeys w_a ≤ 3 and ¬(w_a ≥ 3 ∧ w_b ≥ 2). Every heavy occurrence in such a frame is (3,1,1).
- Cut count: 588 (ℓ,p) pairs × (3·15 + 6·20·3) = 26460 + 211680 = 238140 clauses, with no auxiliaries.
  - They are distinct: 4 or 5 points on ℓ determine ℓ.
  - The overlapping (R,T) cases are implied by G5.
- The cuts are invariant under every row/column/square permutation and under transposition, so they are compatible with the AMENDMENT-3 lex group.
- Fixes needed (all MINOR, wording/conditions):
  1. State the G4 ⇒ K1 (accepted) + K2 (pending) dependency explicitly. AMENDMENT-4.md:28 says only "surviving heavy K3 configuration".
  2. Write the transport maps explicitly, including the square relabelling of b and c (AMENDMENT-4.md:18-23).
  3. Restrict L33 ("Every heavy occurrence is therefore type (3,1,1)") and the title's "all-frame" to own row/column frames. G4 heaviness in arbitrary ONBs is not covered.
  4. Require parent-accepted certificates, not just producer receipts, for any final use (AMENDMENT-4.md:3-4, 50-51).
  5. Name the base instance for the cut screen (original C311 or the C311-lex CNF; AMENDMENT-4.md:61), and note that the cuts are H-invariant.
  6. Restate that the cut CNF needs its own regenerated DRAT certificate and reviewed composition. The old cube proofs certify nothing about the strengthened CNF (AMENDMENT-4.md:61-63 already says this).
