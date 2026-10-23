DISPOSITION: ACCEPT-WITH-FIXES
F1 GR->WAS->HW both directions: VERIFIED
F2 Lemma H incl. empty/full and the 07:39 correction: VERIFIED
F3 OR/M0 avoidance transfers: VERIFIED-WITH-FIXES
F4 EGZ application: VERIFIED-WITH-FIXES
F5 gap Theorem P: VERIFIED
F6 marked formulation and Doubling Lemma: VERIFIED-WITH-FIXES
F7 Davenport-alpha: VERIFIED-WITH-FIXES
F8 DR-Res deletion and inherited inequalities: VERIFIED-WITH-FIXES
F9 DR, DR' and the use of INV_Res: VERIFIED
INV*-SEPARATE: YES
CIRCULARITY: NONE
FINITE-PREMISE: NONE

## FATAL
none

## MAJOR
none

## MINOR

**m1 (F4) olson/proof-dihedral-partial.md:L27-28.**
- *Problem.* Lemma EGZ is stated with no derivation. Its gloss "2p rotations with zero sum" does not follow from EGZ at n = 2p, which needs 4p - 1 terms.
- *Correct derivation.*
  - Apply classical EGZ with n = p to the R >= 3p - 1 >= 2p - 1 rotation values. This gives p values with sum 0 mod p.
  - The remaining R - p >= 2p - 1 values contain another p with sum 0 mod p.
  - The 2p chosen letters, taken in increasing index order, contain no reflection. Their ordered product is therefore rho_(sum) = rho_0.
- *Other occurrence.* The same import with n = p, used once, appears at L59 (a gap with >= 2p - 1 rotations).
- *Uses.* Every use satisfies R >= 3p - 1:
  - olson/proof-DR.md:L26-27 (R = 4p - 1);
  - olson/proof-INV-reduction.md:L21-23 (F in {0, 1} gives R >= 4p - 2);
  - (E).
- *Fix.* Add the one-sentence derivation.

**m2 (F6) olson/proof-dihedral-partial.md:L20-25.**
- *(a) Encoding.* The single-mark encoding is not literally olson/proof-theoremP.md Steps 1-4, which use pair marks and leave singletons unselected. It is their variant with x_r in place of x_pi. I checked that it holds:
  - the identity c_t x [m XOR u_t] = x m - x u_t holds (u_t = 0 gives x m; u_t = 1 gives -x(1 - m));
  - the cyclic summation by parts sum_t (u_(t+1) - u_t) y_t = sum_t u_t (y_(t-1) - y_t) holds, with no boundary term because u = 0 at the fixed gap;
  - the bijection is a valid count: 2^(F-1) * 2^R = number of selections with an even number of reflections.
- *(b) Product formula.* "The ordered product is rho_V" holds only in the linear order that starts with the fixed gap. In the original order the product is a conjugate, rho_(+-V).
- *Fix.* State "identity iff V = 0", which is order-independent, and cite "the single-mark variant of Steps 1-4".

**m3 (F6) olson/proof-dihedral-partial.md:L45.**
- *Problem.* "One of them is the fixed gap" must read "a P-gap, e.g. t_0, is the fixed gap".
- *What goes wrong otherwise.* Suppose an M-gap t* were fixed to colour 0. U's parameter point would then be the complementary colouring: M-gaps Plus, all other gaps Minus, marks complemented. Then "Minus(U u V) = Minus(V) u M-gaps" (L54-55) is not a parameter point of that frame.
- *With t_0 fixed.* U, V and U u V all have colour 0 at t_0, and L41-57 is correct (checked below).
- *Also note.* "2j+1 distinct ... gaps" (L34) is what supplies:
  - F >= 2j + 1;
  - the 2j distinct reflections f_(t_0), ..., f_(t_0+2j-1) of U.

**m4 (F7) olson/proof-dihedral-partial.md:L61-70.**
- *Missing hypothesis N <= 4p - 1.* Sec. 0 (L12) fixes no length.
  - Davenport only yields a nonempty zero-sum item subset with size ≡ 0 mod 2p.
  - The conclusion "below 4p, i.e. 2p" needs total item size <= N <= 4p - 1. For N >= 4p the argument does not exclude size 4p.
  - L72 ("R = 4p-2") also presupposes N = 4p - 1.
- *Corrected statement.* "Let N <= 4p - 1, F >= 2, and I pairwise non-adjacent ...".
- *Missing frame.* Rotate so that the linear word starts at a gap outside I. Such a gap exists because |I| <= floor(F/2) < F. Then no bracket wraps, and each chosen bracket is a consecutive factor sigma_(y_(t-1)) sigma_(y_t) = (y_(t-1) - y_t, +1).
- *Effect.* The only use (olson/proof-INV-reduction.md:L23, L33-35) has N = 4p - 1 and says so, so no conclusion changes.

**m5 (F3) olson/inverse-run-count/proof-RUNS.md:L375 and olson/inverse-parity/proof-PAR-Kplus-partial-r2.md:L35.**
- *L35 wording.* The transfer uses H/HW in the necessity direction for w and the sufficiency direction for w~. L35 names only "Lemma H applied to w~".
- *L375 wording.* L375 writes the empty-pattern condition as "min(A,B) <= kappa". That equals the exact condition 0 notin I(empty) (mod p) only under A, B <= 2p - 1 (olson/inverse-parity/proof-PAR-K0.md:L23-24); the counterexample to the unrestricted form is at K0 L26-28.
- *Why it is harmless.*
  - I(empty) depends only on (p, A, B, H), and OR keeps all of these.
  - A, B <= 2p - 1 holds for the avoider w.
- *Fix.* Write "the P = empty conditions of w and w~ concern the same interval I(empty)". (K0 L31 is accurate for uses of the min-form; Lemma OR uses the exact form, r2 L34.)

**m6 (F8) olson/proof-INV-reduction.md:L24-25.**
- *Problem.* "Each pair adjacent in the selection" can fail in the original linear order. Example: a constant reflection run of length 2 split 1 + 1 across the end of the word. Its floor(2/2) = 1 pair is necessarily {last letter, first letter}.
- *Repair.* Either rotate cyclically first (L11; olson/proof-dihedral-partial.md:L14-15), or note directly: all other pairs are consecutive letters, so the product is sigma_y * 1 * sigma_y = 1.
- *Effect.* The conclusion is unchanged.

## Answers

**Q1 (F1).**

*(a) Completeness.*
1. Take an identity 2p-subword. Rotate w cyclically to R_1 S_1 ... R_k S_k. This is allowed because the product becomes a conjugate (olson/proof-theoremP.md:L14-15). A run that wraps around the end becomes contiguous (olson/proof-GR.md:L60-61).
2. By (v,e)(v',e') = (v + ev', ee'), letter j contributes (prefix sign) * v_j. The e-coordinate is (-1)^C, so an identity selection has C even (L113 fix).
3. Set z_i = (-1)^(#selected reflections before R_i).
   - The c_i letters of the constant run S_i contribute z_i y_i (1 - 1 + ...) = z_i y_i [c_i odd].
   - z_(i+1) = z_i (-1)^(c_i), and this closes cyclically because C is even, so c_i ≡ f_i (L38-41).
   - The rotations of R_i contribute z_i n_i, which gives L43-44.
4. Summation by parts (L45-46):
   - if f_i = 1 then z_i = (z_i - z_(i+1))/2; otherwise (z_i - z_(i+1))/2 = 0;
   - reindex sum z_(i+1) y_i = sum z_i y_(i-1), using z_(k+1) = z_1 and y_0 := y_k;
   - so sum_(f_i=1) z_i y_i = -tau(z) and V = t - tau(z) (L49).

*(a) Realisability.*
- Given z, c_i ≡ f_i with 0 <= c_i <= l_i, and A+- <= E+-, choose those letters.
- The realised pattern is z_1 z and the product is (z_1 V(z), +1).
- Ach(-z) = -Ach(z) and tau(-z) = -tau(z), because f, Phi and delta are invariant and E+- swap. So the single global sign is immaterial (L59-60).

*(a) Realisable C (L51-53).*
- Per run, c_i ranges over f_i, f_i + 2, ..., l_i - [l_i ≢ f_i]. This range is nonempty: for f = 1 with l even, l >= 2.
- Summing gives every even number in [Phi, C_max], and C_max ≡ Phi ≡ 0.

*(a) Elimination (L54-57).* t is even because A+ + A- = 2p - C is even. With A+- = (2p - C +- t)/2 there are three lower bounds (Phi, 2p + t - 2E+, 2p - t - 2E-) and two upper bounds (C_max, 2p - |t|). The six pairwise conditions are:

| Pair | Equivalent condition |
|---|---|
| Phi <= C_max | always true |
| Phi <= 2p - \|t\| | \|t\| <= s1 |
| 2p + t - 2E+ <= C_max | t <= 2E+ - s0 |
| 2p - t - 2E- <= C_max | t >= s0 - 2E- |
| 2p + t - 2E+ <= 2p - \|t\| | t + \|t\| <= 2E+, i.e. t <= E+ |
| 2p - t - 2E- <= 2p - \|t\| | \|t\| - t <= 2E-, i.e. t >= -E- |

All five bounds are even, so an even C exists iff these hold. This is exactly L27.

*(a) k = 1.* f_1 = 0, Phi = 0, and tau = -2^(-1) z_1 (y_1 - y_1) = 0.

*(a) Hand check.* p = 5, w = rho_1^3 sigma_0^5 rho_1^5 sigma_4^5, select rho_1^3 sigma_0 rho_1^5 sigma_4.
- Direct product: (3,+)(0,-)(5,+)(4,-) = (3 - 5 - 4, +) = (4, +).
- GR: z = (+,-), t = 3 - 5 = -2, tau = -2^(-1)[(0 - 4) - (4 - 0)] = 4, V = -6 ≡ 4. The two agree.

*(b) WAS.*
- With P = {z_i = +1}: sum z_i theta_i = 2 sum_P theta, because sum theta = 0. Hence tau(z_P) = sum_P theta (olson/repr-WAS.md:L20-22).
- Negating GR quantifier by quantifier gives L16-18.
- No step uses N. The hypotheses are F, R >= 1 and x = 1 with y correspondingly normalised (L153-157).

*(c) HW.*
- *Per-run C_max* (f = 0 / f = 1): l = 1: 0/1; l = 2: 2/1; l = 3: 2/3; l = 4: 4/3. These equal 2 floor(l/2) and 1 + 2 floor((l-1)/2).
- floor((l-1)/2) = floor(l/2) - [l even], so h = H - #{f_j = 1, l_j even} (README L25, L31-32).
- floor(U/2) = g_P(E+) because floor is monotone and s1 and s0 are even.
- ceil(L/2) = -g_P(E-) by ceil(-x/2) = -floor(x/2), for either parity of E+-.
- Because 2 is invertible mod p: t ≡ tau iff t/2 ≡ sum_P phi.
- *Complement* (L36): P^c has the same f, m and h, and E+(P^c) = E-(P).
- *Empty pattern:* m = 0, h = H, E+ = B, E- = A, and g_0(E) = min(p, E - kappa - 1, floor(E/2)) since H - p = -kappa - 1.
- *Full pattern:* P = [k] gives -I(empty), with phi(empty) = phi([k]) = 0, so it is the same condition.
- *k = 1:* only these two patterns occur.
- *Example* (same word as (a), P = {1}): Ach = 2Z ∩ [max(-8, -10, -5), min(8, 6, 3)] = {-4, -2, 0, 2}, so the half window is [-2, 1]. From HW: g(5) = min(4, 5, 2) = 2 and g(3) = min(4, 3, 1) = 1. The two agree.

*(d) Directions.*
- GR "<=" (realisability) gives HW "=>" (avoider => every phi(P) ∉ I(P) mod p). Equivalently: one hit window => solvable.
- GR "=>" (completeness) gives HW "<=" (all windows avoided => avoider).
- Both directions are proved.

**Q2 (F2).**

*lambda(Q) for proper Q.*
- delta = beta + (o_F - (2m - beta)), so C_max/2 = c = H + m - beta = p - 1 - kappa + m - beta.
- E+(Q) = D_Q + B.
- g_Q(E+) = min(p - m, D_Q + B - kappa + m - beta - 1, floor((D_Q + B)/2)) = lambda(Q) - 1.
- E-(Q) = R - E+(Q) = E+(Q^c), and Q^c has the same m and beta. So -g_Q(E-) = 1 - lambda(Q^c).
- This is I(Q) at K0 L20, which is identical to HW. I(empty) at L22-23 and its negative for [k] (L40-41) also check.

*07:39 correction (L23-31): exactly right.*
- The endpoints lie in [-p, p]. g_0 <= p, and g_0(E) >= min(p, -kappa - 1, 0) >= H - p >= -p.
- If A, B <= 2p - 1, then floor(E/2) <= p - 1, so I(empty) ⊆ [-(p-1), p-1]. Its only possible multiple of p is 0.
- 0 ∈ I(empty) iff g_0(A), g_0(B) >= 0 iff A, B >= kappa + 1. This argument also covers an empty interval.
- If kappa < 0 (H >= p), both g_0 values are >= 0 and min(A, B) <= kappa is false, so the two sides still agree. This is also just p pairs sigma_y sigma_y.

*Counterexample to the uncorrected form* (p = 5, rho_1^10 sigma_0^8): k = 1, H = 4, kappa = 0, B = 0. I(empty) = [-min(5, 9, 5), min(5, -1, 0)] = [-5, -1], which contains -5 ≡ 0, and indeed rho_1^10 = rho_10 = 1. The uncorrected form wrongly calls it an avoider.

*Control.* rho_1^9 sigma_y^9 gives I(empty) = [-4, -1], an avoider. Directly: c is even in [2, 8] and 10 - c ≢ 0 mod 5.

*Remaining items.* "Every avoider has A, B <= 2p - 1" is correct: rho_(+-1)^(2p) = rho_(+-2p) = 1. OR keeps A and B; M0 lowers both by 1.

**Q3 (F3).**

*Lemma OR.*
- w~ is RGR of length 4p - 2 with:
  - F, R, A, B unchanged;
  - all o_F reflection runs odd and constant (they take the value y of the odd run);
  - nonempty rotation runs (every segment contains a rotation run);
  - o_F >= 1 (assembly Fact Z(iii), R/olson-runs-assembly-proof-v4.md:L80, L84-85).
- So H/HW apply to w~.
- For a pattern Q~ of w~, the segment union Q of w has:
  - its even interior runs not as boundaries;
  - every boundary odd, so beta = 0;
  - the same m, E+- = D_Q + B, h = H and kappa.
- phi of each block telescopes to (y_start - y_end)/2 at the two odd boundary runs, whose y values are kept.
- The empty pattern has the same I(empty).
- So: w avoids ⇒ (HW "=>" on w) all of w's windows are avoided, including these ⇒ (HW "<=" on w~) w~ avoids.

*Lemma M0.*
- w' is RGR of length 4p - 2: r_t - 2 >= 1, and S_j stays constant.
- For every P, including empty: E+-' = E+- - 1, h' = h + 1, and m and beta are unchanged. So
  g'(E-1) = min(p - m, E + m + h - p, floor((E-1)/2)) <= g(E),
  i.e. each I'(P) ⊆ I(P) with phi fixed.
- Before the step E+- >= 1, since a_t and b_t each feed one side, so E+-' >= 0.
- The same two directions as OR are used.

*Assembly.* R/olson-runs-assembly-proof-v4.md:L53-56 and L87-97 describe both transfers and their direction requirements correctly. L95 additionally keeps D and kappa - B.

**Q4.**

*(a) EGZ.* Correct via two applications of EGZ with n = p (m1). Each use checks:
- olson/proof-DR.md:L26-27 (F = 0, R = 4p - 1);
- olson/proof-INV-reduction.md:L21-23 (F = 0, 1);
- condition (E).

*(b) Gap Theorem P.*
- *Normalisation.* For w = UV with VU ending in a reflection, a subword S_V S_U of VU with product 1 gives S_U S_V = s_U (s_V s_U) s_U^(-1) = 1 in the original order.
- *Step 1:* M = F - 1 + sum floor(n_t/2) >= 3p - 2.
- *Step 2:* u_(t+1) = u_t XOR [f_t selected] and m_pi = [pi selected] XOR u_t. The map is injective and 0 maps to the empty selection.
- *Step 3:* the colour changes form a closed walk, so their number is even.
- *Step 4:* the prefix parity is u_t, which gives c_t; also (c_t - c_(t+1))/2 = u_(t+1) - u_t, the boundary terms vanish (u_1 = u_(F+1) = 0), and V is linear with beta_t (L70-71).
- *Step 5:* Z has degree 2, deg Q <= 3p - 3 < M, and the box lemma holds (a monomial of degree < M misses a variable). The point 0 contributes +1, so a nonzero point exists.
- *Step 6:* the selection size is even, ≡ 0 mod p, and <= 4p - 1, so it is 2p.
- *Hypotheses.* Since sum floor(n_t/2) <= R/2 and N <= 4p - 1, the hypothesis forces F >= 2p - 1. So F = 0 (empty sum) and F = 1 (1 + floor((N-1)/2) <= 2p) are vacuous, and the omission of F >= 1 at olson/proof-dihedral-partial.md:L30-31 needs no fix.

*(c) Marked formulation.* Bijection, value and size are correct in the frame of the fixed gap (m2).

*(d) Doubling Lemma.*
- |U| = 2j + sum n_M + |K| = p.
- U's colouring is M-gaps Minus with P-gap neighbours; its marks are K and it has 2j reflections, so its value is sum_M beta + sum_K x = 0.
- V-family parameters: M = (F - 2j - 1) + (R - p + 2j) = 3p - 2.
- V never uses U's letters: U's reflections lie between frozen Plus gaps, and U's rotations have frozen mark 0 in Plus gaps.
- The box lemma gives a nonzero point; injectivity gives |V| >= 1; |V| <= 3p - 1. So |V| ∈ {p, 2p}.
- For the union U u V:
  - at the two stretch ends the colours are V's on one side and Plus on the other;
  - marks = marked(V) u K, value = 0 + 0, size 2p, with an even number of reflections.
- This requires the fixed gap to be a P-gap (m3).
- *Case j = 0.* Here the fixed gap is t_0 itself. The two uses check:
  - olson/proof-DR.md:L37-40: >= p equal rho_(+-1) in a rotation run, which is a gap; N = 4p - 1, F >= 1.
  - olson/proof-INV-reduction.md:L26 (D0).

*(e) Davenport-alpha.*
- F >= 2 is needed because otherwise f_(t-1) = f_t.
- Non-adjacency makes the bracket reflections distinct and the Minus gaps isolated.
- Bracket value: in the marked formula, the unselected rotations of a Minus gap carry mark 1, so beta_t + sum_(X_t) x = y_(t-1) - y_t. Directly, (a,-)(b,-) = (a - b, +).
- "Any subset of items is a valid selection with item-sum (size, value)" is right in a frame starting outside I (m4).
- The group is Z_(2p) + Z_p ≅ Z_p + Z_(2p), with p | 2p. D = p + 2p - 1 = 3p - 1 (Olson 1969; van Emde Boas–Kruyswijk), which is a correct classical import.
- "Below 4p" needs N <= 4p - 1, and this is not stated in the lemma (m4).

**Q5 (F8).**

*Reductions.* F = 0 gives EGZ, R = 0 gives sigma_y^(2p) = 1, and F = 1 gives R = 4p - 2, hence EGZ.

*Inherited conditions for w:*
- (E) by EGZ.
- (P) by gap Theorem P: each S_i yields one gap with n = r_i and l_i - 1 empty gaps, so the gap sum is sum floor(r_i/2).
- (V) by Davenport-alpha:
  - take gaps (g1,g2), (g3,g4), ... of each run: floor(l_j/2) gaps, |I| = H;
  - they are separated within a run by unchosen gaps and across runs by nonempty rotation gaps (also for k = 1);
  - this gives H items (2, 0) and R rotation items, sizes < 4p;
  - so R + H >= 3p - 1 would make w solvable.
- (Pairs) by p pairs sigma_y sigma_y (m6).
- (D0) by Doubling with j = 0.

*Monotonicity under an in-run deletion.* R, F + sum floor(r_i/2), R + H, H, a_i and b_i are all non-increasing.
- An in-run deletion removes a letter from a run of length >= 2. No run vanishes or merges, so w' ∈ RGR_(4p-2)(p) with the same 2k runs and F, R >= 1.
- w' is an order-preserving subsequence of w, so every 2p-subword of w' is a 2p-subword of w in the same order.
- A wrapping cyclic run stays wrapping, so the cyclic structure is unaffected.

*Rest of Theorem DR (olson/proof-DR.md:L25-40).*
- 4p - 1 is odd while 2k is even, so some run has length >= 2.
- Two runs of length >= 2 give contradictory parities.
- So |X| = 4p - 2k >= 2p. If X is a reflection run, sigma_y^(2p) = 1. If X is a rotation run, it contains >= p equal letters, and Doubling with j = 0 applies.

**Q6 (F9).**

*What INV_Res(p) must supply.* For every inherited avoider in RGR_(4p-2)(p) with F, R >= 1, here applied to in-run deletions: k <= p and all runs odd.

*Order of use.*
1. RUNS on one in-run deletion gives k <= p. k is common to all in-run deletions.
2. PAR, whose hypothesis includes k <= p, is then applied to the deletions from X and Y (olson/proof-INV-reduction.md:L45-48).

*Corollaries D and E.*
- R/olson-runs-assembly-proof-v4.md:L202-203 supplies exactly this statement, conditional on Theorem C, which was not audited here. PAR's Theorem P hypotheses (L84-90) match.
- Corollary E (L204-205) follows from Corollary D by Theorem DR-Res.

*Why DR' still needs INV*(p).* An arbitrary length-(4p-1) avoider is forced into RGR only through INV* applied to all of its deletions. Nothing inlined touches non-RGR words, except sufficient tools that cover no full class. Both halves remain open (obligations-after-PAR.md:L54-56; invstar/results.md:L69-71).

*DR' (a).* A forbidden rotation pair, or a rho_0, survives the deletion of any third letter (4p - 1 >= 3), so the deletion is not RGR.

*DR' (b).* Adjacent unequal reflections stay cyclically adjacent after deleting j ∉ {i, i+1}. Merging only enlarges the run containing them, which is then non-constant. Both (a) and (b) are correct.

**Q7.**
- *Circularity: none.*
  - Gap Theorem P (self-contained Chevalley–Warning) is unrelated to PAR's Theorem P, which takes (P) only as a hypothesis.
  - GR is self-contained; WAS depends only on GR; HW and H depend only on WAS and GR.
  - INV_Res is a hypothesis of DR-Res, and RUNS and PAR do not use DR-Res.
- *Finite computations: none used as premises.* proof-PAR-K0.md:L45-46, proof-GR.md Sec. 5, repr-WAS.md Secs. 2-4, proof-INV-reduction.md Sec. 3, proof-DR.md:L60-67 and the [C] labels are all aids; every step has a written proof.
- *Unstated hypotheses:* only m3 (fixed P-gap) and m4 (N <= 4p - 1, frame).

## FULLY CHECKED vs IMPORTED

FULLY CHECKED (line by line):
- proof-GR.md L11-61, L110-113, together with Cor. GR-W;
- repr-WAS.md L7-33, L151-157;
- inverse-run-count/README.md L17-36;
- proof-PAR-K0.md L7-44, L48-53, including (V) <=> kappa <= o_F - 1 and (P) <=> R + o_R >= 2p;
- proof-RUNS.md L9-21, L56-63, L364-375, L400-414;
- proof-PAR-Kplus-partial-r2.md L13-42;
- proof-theoremP.md L8-93;
- proof-dihedral-partial.md L9-73 (Sec. 0-4);
- proof-INV-reduction.md L9-48;
- proof-DR.md L9-58;
- assembly L39-56, L77-104 (Facts Z, T, K), L194-209.

IMPORTED OR HYPOTHESIS-MATCHED ONLY:
- Imported: classical EGZ (n = p) and D(Z_p + Z_2p) = 3p - 1.
- Matched only against their use in Corollaries D and E: Theorem C, (GC), U2-U8, U10, PAR's Theorem P and Theorem M.
- Read, not audited: the INV* status files.
- Not used and not checked: Theorem R, Corollary R', T0, and all finite sections.

## Conclusion

**Endorsed (every prime p >= 5, with m1-m6 applied):**
- GR, WAS, HW and H are exact two-way criteria for RGR words with F, R >= 1 of any length. H's kappa-identities are for N = 4p - 2.
- OR and M0 preserve avoidance.
- EGZ, gap Theorem P, Doubling and Davenport-alpha hold as used.
- INV_Res(p) => RGR-LONG(p) (DR-Res).
- INV*(p) + RGR-LONG(p) => OO(p) (DR').

**Open:**
- INV*(p), both halves; OO(p) is therefore not established.
- Parent acceptance of (GC) and U2-U10, which this audit did not review.
- p = 3.

**Correctness versus novelty.** This audit addresses correctness only. GR, WAS, HW and H are elementary bookkeeping of ordered products in D_2p. Gap Theorem P and Doubling are Chevalley–Warning box arguments of a standard type. EGZ and the Davenport constant are classical imports. No novelty, significance or priority is assessed or claimed.
