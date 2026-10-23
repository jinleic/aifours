**DISPOSITION: ACCEPT-WITH-FIXES** (advisory only; no gate or acceptance authority)

ROT-o2 (`proof-ROT-lowodd-v1.md:84-87`) holds as a universal statement on its exact scope. It has no finite premise and no circularity. GRX (`notes-GRX-v1.md:18-19`) is correct for the group law that its own proof fixes.

- **Severity:** no FATAL and no MAJOR finding. There are seven MINOR items, M1–M7; M1 and M2 are required corrections.
- **Robustness:** ROT-o2 uses GRX in only two places: PM*, and the all-plus conditions in K1/K2. I re-proved both without GRX, so even a defect in GRX could not reach ROT-o2.
- **Pins:** I audited the text as pasted. The SHA-256 pins were not verified (no execution).

## Premises imported but not stated

These come from `olson/proof-dihedral-partial.md` Sec. 0, cited at `notes-GRX-v1.md:9` and `proof-ROT-lowodd-v1.md:12`. That file was not provided.

- **Group law.** Elements are ρ_x = (+1,x) and σ_y = (−1,y) in Z_p ⋊ {±1}, with (ε,a)(ε′,a′) = (εε′, a+εa′).
  - Consequences: ρ_aσ_b = σ_{a+b}, σ_bρ_a = σ_{b−a}, σ_aσ_b = ρ_{a−b}.
  - A word u_1⋯u_n multiplies to (Πε_i, Σ_i ε_1⋯ε_{i−1}a_i).
  - This is exactly the contribution rule written at `notes-GRX-v1.md:31-32`.
- **"Identity 2p-subword".** 2p letters at increasing, not necessarily adjacent, positions, whose product in word order is 1. This is the reading used at `notes-GRX-v1.md:28` and in the pairs bound (`proof-ROT-lowodd-v1.md:5-6`).
- **EGZ for Z_p.** Permitted import.

## Q1 — GRX: both directions verified

1. **Only-if direction.**
   - An identity selection has an even number of reflections, because (ε,a) ↦ ε is a homomorphism. The proof uses this but never states it (`notes-GRX-v1.md:24`; M2).
   - Cut after S_k, so z_1 = +1.
   - A chosen rotation x in R_i contributes z_i·x.
   - The c_i chosen copies of σ_{y_i} are consecutive in the selection and are entered with sign z_i. They contribute z_iy_i − z_iy_i + ⋯ = z_iy_i·[c_i odd], whichever copies are chosen and in whatever order R_i sits.
   - For i < k we have z_{i+1} = z_i(−1)^{c_i}, and (−1)^C = +1. Hence [c_i odd] = f_i for every i, including i = k.
   - Therefore V = Σ_ch + Σ_{f_i=1} z_iy_i, where Σ_ch is the sum of the chosen elements of X^z (`:30`).
2. **Summation by parts** (`:33-34`). This is an identity over integer lifts, so no inverse of 2 mod p is needed.
   - z_if_i = (z_i − z_{i+1})/2, which lies in {0,±1}.
   - Reindex with z_{k+1} = z_1 and y_0 = y_k. Then Σθ_i = 0 exactly.
   - So Σz_iθ_i = T − (−T) = 2T, and V = Σ_ch − T(z).
3. **The set of realisable C** (`:35-39`).
   - c_i runs over f_i, f_i+2, …, l_i − [l_i ≢ f_i]. This set is nonempty because l_i ≥ 1, which is needed when f_i = 1.
   - A Minkowski sum of step-2 progressions is the step-2 progression from Φ to C_max.
   - Φ is even (sign changes around a cycle), and C_max ≡ Φ.
   - So every even C in [Φ, C_max] is realisable, for every z.
4. **If direction.**
   - If z_1 = −1, replace z by −z (`:40-41`). This leaves f, Φ, δ and C_max unchanged, sends X^z to −X^z, and gives T(−z) = Σ_{z_i=−1}θ_i = −T(z).
   - Choose the c_i as in item 3.
   - By induction the zone signs reproduce z, and the product is ρ_{Σ_ch−T} = 1.
5. **Every representation.**
   - The proof uses only that each S_i is constant and nonempty and that runs and blocks alternate cyclically.
   - It never uses y_{i−1} ≠ y_i, nor r_i ≥ 1. Empty runs still carry a sign z_i and a jump θ_i.
   - Hand checks under the law above:
     - σ_aσ_b: T = b−a, so the word is the identity iff a = b. Correct.
     - ρ_uσ_aρ_xσ_b: the product is ρ_{u+a−x−b}. GRX with z = (+,−) gives V = u−x−(b−a). They agree.
     - σ_aσ_bσ_aσ_b: the product is ρ_{2(a−b)}, and GRX gives T = θ_1+θ_3 = 2(b−a). They agree.
6. **Cyclic cut** (`:41-42`). In a cyclic shift of w, the chosen letters appear in a cyclically shifted order, and cyclic shifts of a product are conjugate. So the existence of an identity subword is invariant.
7. **Degenerate cases.**
   - F = 0 (`:20`): correct, since rotations commute.
   - R = 0: Σ_0(∅) = {0}, so the criterion becomes "C = 2p ∈ [Φ, C_max] and T(z) = 0".
   - k = 1: f_1 = 0 and θ_1 = 0, so T ≡ 0.
8. **Convention sensitivity (imported premise).**
   - Under the opposite law, (ε,a)(ε′,a′) = (εε′, ε′a+a′), we get V = Σ_ch + T(z). GRX then reads T(z) ∈ Σ_m(−X^z).
   - GRX must therefore name its law (M2).
   - ROT is unaffected: it only uses T = 0 patterns and the equality T̃ = T.
9. **Not audited and not load-bearing:**
   - the GR/GR0 specialisations (`:44-45`); the ±1 window formula itself is correct;
   - the controls (`:47-54`).

## Q2 — PM*: verified, in the right direction

Map each pattern z̃ of w̃ to the pattern z of w with z_j = z_{j+1} := z̃(m), where m is the merged run.

| quantity | w̃ | w |
|---|---|---|
| f at S_j | — | 0 |
| f at S_{j−1} | [z_{j−1} ≠ z̃(m)] | f_{j−1} |
| f at S′_{j+1} / S_{j+1} | [z̃(m) ≠ z_{j+2}] | f_{j+1} |
| δ-term of S_j | — | [l_j odd] = 0 |
| δ-term of S′_{j+1} / S_{j+1} | [l_{j+1}+l_j ≢ f_{j+1}] | [l_{j+1} ≢ f_{j+1}], equal since l_j is even |
| Φ, δ, F, R, C_max | equal | equal |
| X^z | z̃(m)(X_j+X_{j+1}) | z_jX_j + z_{j+1}X_{j+1}, equal |
| θ of merged run | y_{j−1}−y_{j+1} | θ_j+θ_{j+1}; both are in T iff z̃(m) = + |
| θ of R_{j+2} | y_{j+1}−y_{j+2} | θ_{j+2}, since S′_{j+1} keeps the value y_{j+1} |

Consequences:

- T̃(z̃) = T(z), so every condition of w̃ is also a condition of w.
- Hence "w̃ has an identity subword ⇒ w does", which is the same as "w avoids ⇒ w̃ avoids". This is the direction used at `:86`.
- The converse is neither claimed nor needed; w has extra patterns with f_j = 1.

Edge cases:

- **k = 2 → 1.** Here j−1 ≡ j+1, so θ̃ = 0 = θ_j+θ_{j+1}, and f_{j+1} = 0 = f̃.
- **j = k.** The merge wraps around the cut; GRX is cyclic, so this is fine.
- **Non-maximal representation.** If X_j = X_{j+1} = ∅ and y_{j−1} = y_{j+1}, the merged word's representation is not maximal; Q1 item 5 covers it.
- **Reflection values change.** PM* rewrites reflection values, so only rotation data transfers back to w, which is consistent with `:7-8`.

**Convention-free re-proof.** Take an identity selection of w̃ that uses c′ letters of S′_{j+1}.

- Let c_j be the largest even number ≤ min(l_j, c′), and let c_{j+1} = c′ − c_j.
- Then c_{j+1} ≤ l_{j+1}: either c′ ≤ l_j + l_{j+1}, or c_{j+1} ∈ {0,1}.
- Cut w immediately after S_{j+1}. The selection in w̃ reads ⋯A B σ_{y_{j+1}}^{c′}, and its lift to w reads ⋯A σ_{y_j}^{c_j} B σ_{y_{j+1}}^{c_{j+1}}.
- σ_{y_j}^{c_j} is consecutive in the lift and equals 1. Also σ^{c′} = σ^{c_{j+1}} because c_j is even. So the two products are equal.

**Iteration** (`:40-41`).

- Parities are preserved, so o is invariant, and k decreases by 1 at each step.
- The process ends with k = o when o ≥ 1, or with a single even block when o = 0.

**M1 (required).** `:12-13` defines blocks as maximal, and PM* (`:31`) and K2 (`:66`, "k = 2") are worded in that vocabulary. From the second merge on, the representation may be non-maximal. None of the proofs of PM*, K1 or K2 uses maximality. The fix is to state all three for any cyclic constant-block representation, with runs allowed to be empty and adjacent blocks allowed to share a value. Maximality is then needed only to define o.

## Q3 — (D), Z1, Z2: verified; no hidden inverse theorem

- **(D)** (`:16`).
  - Among the n partial sums, either one is zero or two are equal. Either way there is a consecutive zero-sum block.
  - Z_2×Z_p ≅ Z_{2p} because p is odd.
- **Z1** (`:20-22`).
  - Zero-sum-freeness depends only on the multiset, so every ordering is zero-sum-free. In each ordering the n−1 partial sums are distinct and nonzero, so they are exactly Z_n∖{0}.
  - Swapping a_1 and a_2 changes only S_1. The new S_1 = a_2 must be the one remaining value, which is a_1.
  - Any pair can be placed first; this needs n ≥ 3. So all terms are equal.
  - The multiples g, 2g, …, (n−1)g are all nonzero, so ord g = n.
  - Notation: at `:21`, "s_1 = s_2" means terms, not partial sums (M5).
- **Z2** (`:22-27`).
  - S_i has first coordinate i mod 2. So S_2, …, S_{2p−2} are p−1 distinct nonzero elements of the (p−1)-set {(0,y) : y ≠ 0}, and therefore exhaust it.
  - Swapping positions 2j and 2j+1 (with 2j+1 ≤ 2p−2) changes only S_{2j}. The new value must be the same element, so a_{2j} = a_{2j+1}.
  - Positions 2 and 3 exist when p ≥ 3, and any pair can be moved there. So all terms are equal.
  - g = (1,0) is excluded because gg would be a zero-sum.
  - g = (1,c) with c ≠ 0 generates only because p is prime. This is used tacitly at `:75`.
- **Boundary.** The hypothesis p ≥ 5 is never used. Every inequality below also holds at p = 3, where K2's t ≥ 2 branch is vacuous (M7, harmless).
- **Lengths at which Z1/Z2 are applied.**
  - Z1 is applied only at length exactly 2p−1 (`:52`, `:58`).
  - Z2 is applied only at length exactly 2p−2, with every first coordinate equal to 1 (`:74`).
  - The first-coordinate condition rules out the other extremal shape, g^{n−3}(2g), because 2g has first coordinate 0.

## Q4 — K1 and K2: every branch and endpoint checked

**EGZ used twice** (`:46`, `:67`, `:86`).

- Suppose R ≥ 3p−1. EGZ on any 2p−1 rotation values gives p of them summing to 0.
- The remaining R−p ≥ 2p−1 values give another p summing to 0.
- These 2p rotations have product ρ_0 in any order.
- Hence an avoider has R ≤ 3p−2, F ≥ p, and F ≥ 1.

**(∗) and (∗∗) are elementary.**

- Only z ≡ + is used, so T = 0.
- Choose an even c_i ≤ l_i − [l_i odd] in each block. Then every zone sign is + and the product is ρ_Σ.
- Through the CRT encoding (`:14-15`), this is exactly the zero-sum condition on Y. It does not depend on the sign convention.

**K1** (`:45-61`):

- **Setup.**
  - F ≤ 2p−1, since σ_y^{2p} = 1. Put s = R−(2p−1), so s ∈ [0, p−1] and F = 2p−1−s.
  - F′ ≤ 2p−2, so the forbidden range starts at 2p−F′ ≥ 2. The empty selection is never in the forbidden range.
  - The lower end 2p−F′ is s+1 when s is odd and s+2 when s is even. In the even case, s+1 is odd and so irrelevant. This gives (∗).
- **s = 0.** Y is zero-sum-free, so Z1 applies.
- **Loop for s ≥ 1.**
  - Each pass starts with a remainder of at least (2p−1+s)−(s−1) = 2p elements.
  - (D) gives a zero-sum U with |U| ≤ 2p, hence |U| ≤ s by (∗).
  - Then |Z∪U| ≤ 2s−1 ≤ 2p−3, hence |Z∪U| ≤ s.
  - |Z| strictly increases and is bounded by s, so the loop exits within s passes, with |Z| = s.
  - Zero-sums have even length, so odd s is impossible.
- **s even, s ≥ 2.**
  - Any nonempty zero-sum U′ inside Y′ would give |Z∪U′| ∈ [s+2, 2s] ⊆ [s+1, 2p−2]. That is forbidden, so Y′ is zero-sum-free.
  - Z1 then gives Y′ = g^{2p−1}.
  - For h ∈ Z: a_h is odd, and e_h ≤ 2p−1 copies of g are available. So h·g^{e_h} is a zero-sum of length at most 2p, hence of length at most s. The case h = g would give length 2p and is an immediate contradiction.
  - Cumulative lengths L_i: L_1 ≤ s and L_s ≥ 2s. The least i with L_i ≥ s+1 has i ≥ 2 and L_i ≤ 2s ≤ 2p−2.
  - That step uses L_i − i ≤ 2s−2 ≤ 2p−4 copies of g, and its sum is i·2p·g = 0. Its length lies in [s+1, 2s], contradicting (∗).
  - Endpoint s = p−1 gives 2s = 2p−2, which is fine.
- **The example at `:62`.** Correct by the same elementary criterion, but not used.

**K2** (`:66-80`):

- **Pairs bound.** There are (l_1−1)/2 + (l_2−1)/2 = (F−2)/2 disjoint adjacent σσ pairs, so F ≤ 2p. The symbol H is never defined (M5).
- **Range of t.** F is even and F ≥ p, so F ≥ p+1. Hence t ∈ [0, (p−1)/2] and R = 2p−2+2t.
- **(∗∗).** No zero-sum has length in [2t+2, 2p]. So every zero-sum of length at most 2p has length at most 2t.
- **Loop.** Each pass gives |Z∪U| ≤ 4t−2 ≤ 2p−4. The loop exits at |Z| = 2t, using parity. For t = 0 there is no pass.
- **Y′.** Any U′ would give a forbidden length in [2t+2, 4t] ⊆ [2t+2, 2p−2], so Y′ is zero-sum-free. Z2 gives Y′ = g^{2p−2}.
- **At most one g in Z.** Two copies would give g^{2p}, a zero-sum of length 2p ∈ [2t+2, 2p].
- **Terms h ≠ g.** There are at least 2t−1 of them.
  - For each, a_h ∈ [3, 2p−1] and e_h ∈ [1, 2p−3], both odd.
  - At most 2p−3 ≤ 2p−2 copies of g are needed, so h·g^{e_h} is available. It is a zero-sum of length 1+e_h ≤ 2p−2, which gives e_h ≤ 2t−1.
- **t = 0.** Y = g^{2p−2}.
- **t = 1.** e_h = 1, so h = −g.
- **t ≥ 2** (only possible when p ≥ 5).
  - There are at least 3 such h, and L_q ≥ 4t−2 ≥ 2t+2.
  - Take the least i ≥ 2 with L_i ≥ 2t+2. Each increment 1+e_h is even, so L_{i−1} ≤ 2t and L_i ≤ 4t ≤ 2p−2.
  - The parity step is not stated at `:79` (M3). Without it, L_i ≤ 4t+1 is still within range.
  - The step uses at most 4t−2 ≤ 2p−4 copies of g, which gives the contradiction.
  - Endpoint t = (p−1)/2 gives 4t = 2p−2, which is fine.
- **Unstated corollary.** The argument also shows F ∈ {2p, 2p−2}, and X = c^{2p−2} when t = 0.

## Q5 — ROT-o2: exact scope

- **o = 0 is impossible.** EGZ gives F ≥ 1. PM* reduces to one even block, and K1 then forces F = 2p−1, which is odd. This step is only implicit at `:85-87` (M4).
- **o = 1.** R = F = 2p−1, and all rotations equal some c ≠ 0. The example at `:62` shows this case is nonempty.
- **o = 2.** K2 applies to the possibly non-maximal reduced word, once M1 is fixed. The rotations lie in {c, −c} with c ≠ 0.
- **Scope covered.** Any number of even blocks, empty runs, and non-constant reflection runs.
- **Counting of o.** o is counted cyclically (`notes-GRX-v1.md:10`).
  - A linear count is never smaller, since merging the first and last blocks never increases the number of odd blocks. So the statement also holds under a linear reading.
  - This is not the same as "at most 2 reflection runs". For example, a single run σ_aσ_bσ_c with distinct values has o = 3 and is excluded.
- **Not inferred** (consistent with `:7-8` and `:88-89`):
  - anything about reflection values;
  - o ≥ 3;
  - existence of avoiders with o = 2;
  - ordered Olson.
- **Remark at `:89`.** The parenthetical is garbled. In fact o ≡ R (mod 2) always holds (M6).

## Q6 — Severity

- **FATAL:** none.
- **MAJOR:** none.
- **Counterexamples:** none found. Cases stress-tested:
  - s odd, and h = g;
  - t = 0, 1, (p−1)/2;
  - the k = 2 merge;
  - empty runs with equal neighbouring blocks;
  - the j = k wrap;
  - R = 0 and F = 0;
  - cyclic versus linear counting of o;
  - the opposite group-law convention.
- **MINOR:**
  - **M1 (required).** Restate PM*, K1 and K2 for arbitrary representations: `proof-ROT-lowodd-v1.md:12-13, 31-33, 66, 86`.
  - **M2 (required for GRX as a standalone lemma).**
    - Name the group law and note the T ↦ −T flip under the opposite law (`notes-GRX-v1.md:9, 31-32`).
    - State that identity selections have an even number of reflections (`:24`).
  - **M3.** State the parity of 1+e_h (`:78-79`).
  - **M4.** Spell out why o = 0 is impossible, and optionally record F ∈ {2p−2, 2p} (`:85-87`).
  - **M5. Notation:**
    - l_i is reused for cumulative lengths (`:59-60, 78`);
    - s_i means terms, not partial sums (`:21, 26`);
    - "sigma" also denotes a sum (`notes-GRX-v1.md:34`);
    - H is never defined (`:67`);
    - "only pattern" should read "only pattern up to global sign" (`:47`).
  - **M6.** Fix the parenthetical at `:89`.
  - **M7.** p ≥ 5 is never used (`:1, 84`); harmless.
- **Circularity:** none.
- **Finite premises:** none. The claim at `:6` is confirmed, and I did not rely on `notes-GRX-v1.md:47-54`.

## Checked versus imported

**Fully checked here:**
- (D), Z1, Z2;
- the CRT encoding;
- the double EGZ step;
- the pairs bound;
- GRX: both directions, all parities, which C are realisable, the global sign, the cyclic cut, F = 0, R = 0, k = 1, and every representation;
- PM*, with two independent proofs, and its iteration;
- K1 for all s;
- K2 for all t;
- ROT-o2 for o = 0, 1, 2;
- the example at `:62`.

**Imported:**
- EGZ for Z_p;
- the group law and the meaning of "identity 2p-subword", from proof-dihedral-partial Sec. 0.

**Not checked, and not load-bearing:**
- GRX's relation to GR/GR0 (`notes-GRX-v1.md:3-5, 44-45`);
- the review statuses (`proof-ROT-lowodd-v1.md:4-5`);
- the controls (`notes-GRX-v1.md:47-54`);
- the meaning of ROT(p), INV*(p) and OB1.
