VERDICT: ACCEPT-WITH-FIXES

`r1 Ln` = SUPPORT_LOWER42.r1.md, `py Ln` = verify_lower42.py.

## FATAL

None found.

## MAJOR

**M1 [math] r1 L236–237: the "images of the written instance" claim is false, and the invariance claim is unproved.**
- **Why it is false.** Coordinate permutations and per-coordinate value swaps act on the subcube {0,1}^4 as S_4 ⋉ Z_2^4.
  - A permutation σ sends {u·x ≡ c} to {σu·x ≡ c}.
  - A swap at coordinate i sends it to {u·x ≡ c + u_i}.
  - So |U| is invariant, and the ten sets form two orbits: |U| = 4 (2 sets) and |U| = 3 (8 sets).
  - Only the odd code is an image of the written even code.
  - A second invariant also separates them: for |U| = 3 the coordinate outside U is free (N = N′ × {0,1}); for |U| = 4 no coordinate is free.
- **Invariance claim.** "Preserve … the congruences of Lemma 10" holds only up to sign, and the file gives no proof.
- **Consequence.** The written §4 covers 2 of the 10 sets. The eight |U| = 3 sets rest only on F2/F3, as L235–236 says. The theorem survives (see the verifier assessment below), but the file presents a false argument as an equivalent route.
- **Fix.** Replace L236–237 with (1) and (2) below.
  1. *Symmetry lemma.* A party permutation combined with coordinatewise value bijections:
     - maps lines to lines;
     - maps the three pairings onto the three pairings, possibly transposed;
     - maps 2×2 components to 2×2 components;
     - maps each Lemma-10 form to ± the form of the image block (a row or column swap gives −, by L136; a transpose gives +).
     
     So a vanishing signed sum of three forms, one per reshaping, maps to another vanishing signed sum of the same kind. Its right side is still (±1±1±1)π, which is odd.
  2. *Written |U| = 3 instance* (U = {1,2,3}, c = 0, in {4,5}^4). N = {4444, 4445, 4554, 4555, 5454, 5455, 5544, 5545}. I checked by hand that each reshaping has exactly two closed 2×2 blocks. The three blocks used are:
     - 12|34, rows (x1x2) ∈ {44, 55}, columns (x3x4) ∈ {44, 45}: φ₄₄₄₄ − φ₄₄₄₅ − φ₅₅₄₄ + φ₅₅₄₅ ≡ π.
     - 13|24, rows (x1x3) ∈ {44, 55}, columns (x2x4) ∈ {44, 45}: φ₄₄₄₄ − φ₄₄₄₅ − φ₅₄₅₄ + φ₅₄₅₅ ≡ π.
     - 14|23, rows (x1x4) ∈ {54, 55}, columns (x2x3) ∈ {45, 54}: φ₅₄₅₄ − φ₅₅₄₄ − φ₅₄₅₅ + φ₅₅₄₅ ≡ π.
     - (1) − (2) − (3) vanishes identically, while the right sides give −π ≢ 0.
  
  With L208–216, items (1) and (2) cover all ten sets in writing, and F2–F4 become cross-checks. The minimal alternative is to delete L236–237.

## MINOR

**[math: justification gaps; the conclusions are true]**
- **m1, r1 L93 and L98.** Lemma 7 uses Lemma 6 without citing it.
  - A one-row component has a single column only by Lemma 6.
  - In (a), "no row reaches a third column, so k_K = 2" needs |rows(K)| = |cols(K)|.
  - Fix: cite Lemma 6 in both places, and change "same two entries" to "same two columns".
- **m2, r1 L131 vs L211–216.** Lemma 10 defines φ_rc per reshaping, but §4 adds congruences from different reshapings as forms in φ_x. The coupling that makes this valid must be stated: U_π[r,c] = 6ψ_x, so φ_rc = arg ψ_x =: φ_x for every π. Fix: add this sentence after Lemma 10.
- **m3, r1 L201–203.** "Determined by the support" needs one line of justification. By Lemma 2(a), no row or column through a point of N contains an officer, so the components of B(U_π) that meet N are exactly the components of N's own support graph. This is what py L48–71 computes, with S = N and no officers.
- **m4, r1 L19–21.** The theorem does not say "orthonormal", but L34–35 needs each V_k to be unitary. Fix: "for all orthonormal bases {|e^{(k)}_x⟩} of C^6".
- **m5, r1 L202, L218; py L143–158.** F4 is logically redundant.
  - Components and block forms depend only on which coordinates are equal, and every coordinatewise injection preserves that.
  - A change of orientation only flips signs (L136).
  - Fix: state this invariance, and present F4 as a cross-check rather than writing "for every subcube" as if the proof depended on it.

**[verifier]**
- **v1, py L110–117.** `verify_combination` repeats the same summation as py L101–105 on the same data, and the parity test is vacuous: 1 + e1 + e2 is always odd. It is not an independent check. Correctness is unaffected.
- **v2, py L165–167.** If F2 or F3 fails for any set, `F3_obstruction` is None and the loop raises TypeError after the JSON has been written. The exit status is still 1, so r1 L243 holds, but the per-set report aborts. Fix: iterate over `... or []`.
- **v3, py L161.** The JSON records the Python version, so byte-identical replay is meaningful only under Python 3.9.6.
- **v4, py L14–15.** The unknowns are real phases. Change "no real or complex solution" to "no assignment of phases".

**[editorial]**
- **e1, r1 L223.** φ is reused for the 4-qubit state after serving as the phase symbol. Rename the state.
- **e2, r1 L12–13, L149.** Tarry is cited only through a secondary source. Add primary or modern references (Tarry 1900–01; Stinson, J. Combin. Theory Ser. A 36 (1984)).
- **e3, r1 L159–161, L235–236.** Update the dependence statements after the M1 fix.

## What is established

- **Main result.** Every AME(4,6) state has at least 42 nonzero coefficients in every orthonormal product basis, conditional only on Tarry's theorem for t = 36.
  - This is a partial result. It says nothing about 59 versus 60 or about the true minimum.
  - Novelty is not assessed.
- **Checked line by line, with no gap beyond those listed above:**
  - §0: the reduction by local unitaries, and AME ⇔ all three reshapings unitary.
  - Lemmas 1–6.
  - Lemma 7(a): e_K = 0 ⇔ K is a 2×2 block with 4 entries.
  - Lemma 7(b): e_K = 1 forces cols(K) = C0, k_K = 3, two equal 2-supports, and a column with a single entry. By 2(b) that entry is classical, and 2(a) then contradicts r0 having three entries.
  - Lemma 7(c).
  - Lemma 8: |D| = d_{i,a}, d ≠ 1, Σd = h, and N ⊆ ΠV_i.
  - Lemmas 9 and 10.
  - The case split for s ≤ 41 is complete:
    - t = 31: odd count of rows to be paired;
    - t = 33, 34: |V_i| = 1, so |N| ≤ 1, against ≥ 2;
    - t = 35: d = 1;
    - t = 36: a pair of orthogonal Latin squares of order 6;
    - t = 32: e ≠ 1, then Step 1 ({4} profile impossible), Step 2 (uniform marginals), giving an OA(8,4,2,2).
  - Fourier classification: five characters survive, their ten pairwise sums are distinct and nonzero, and Parseval gives exactly the ten parity sets.
  - Even-code obstruction: blocks recomputed, and (1) − (2) + (3) ≡ 0 identically.
- **Generality.**
  - Lemma 10 uses only orthogonality of two rows of a 2×2 unitary block.
  - Magnitudes are free except |ψ_x| = 1/6 on T, and phases are arbitrary.
  - The support structure is derived (Lemma 8, §3), never assumed.
  - No real-only, ansatz, canonical-basis or symmetry assumption enters the main chain. The only symmetry claim is M1, and the main chain does not use it.
- **Verifier logic.**
  - Blocks are the components of N's support graph, which are the non-classical components (m3).
  - The sign pattern at py L89 matches Lemma 10 with r = rs[0], c = cs[0].
  - Variables are keyed by the point x, so phases are shared across reshapings (m2).
  - The search takes one block per reshaping with ±1 signs and checks for a zero sum.
  - So a reported success does imply 0 ≡ odd·π. Independently of the replay, all ten sets are obstructed: the even code (written), the odd code (one value swap), the |U| = 3 representative in M1(2), plus the symmetry lemma.
- **By-product (the §2 arguments for t ≥ 33 do not use s ≤ 41).**
  - No AME(4,6) state has t ∈ {33, 34, 35}, so with Tarry, t ≤ 32.
  - e = 0 forces t to be even.

## Imports/trust limits

- **Imported:** only Tarry's theorem (no pair of orthogonal Latin squares of order 6), for case t = 36, via Pandya L42–46, refs [7–9].
- **Not used:**
  - Pandya's code bound (≤ 34 codewords, ref [32]);
  - nonexistence of AME(4,2) (the remark at L220–227 is optional, and its derivation is correct);
  - any SAT result (L257–258).
- **Taken on trust:** I did not execute F1–F4. The replay status, exit code, byte identity and all SHA-256 values (r1 L3–4, L7–8, L241–246) are accepted as reported.
  - F1 duplicates the written classification.
  - Until M1 is fixed, the eight |U| = 3 sets formally rest on F2/F3. Here they are confirmed by a hand-checked representative plus symmetry, not by an exhaustive run.
- **Context only:** Pandya's 38 ≤ s_min ≤ 60 (L504–520).
