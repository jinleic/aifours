**Verdict: ACCEPT-WITH-FIXES.** There are 0 FATAL, 0 MAJOR and 7 MINOR findings. Every fix is a change of wording or citation. None alters the statement, the κ-range or the structure of any proof, so they can be recorded as binding readings instead of requiring a v2.

**Scope of this review.** I reviewed the candidate text as supplied, against the printed v5 interface (L38–48) and the parent verdict. I did not recompute any hash. I took Lemma W and Facts 2.1–2.2 in their printed form, since you stated the parent scope covers them.

## Step-by-step

**1. Encoding, fixed window and Lemma W hypotheses: correct.**
- **The reduction to (1) holds.**
  - F = 3p−2 = 2H + k, so k = p + 2κ holds without any assumption.
  - Fact 2.2 at R = p limits every run to at most one letter.
  - So exactly p runs are singletons (d = ±1) and 2κ runs are empty (d = 0).
- **The encoding is correct.**
  - Since p is odd, e is the inverse of the isomorphism 2Z/2pZ → Z_p. So e is additive and injective.
  - ψ(P) = −B + Σ_P e(θ_i) − Σ_P d_i = e(2u_P) − E(P).
  - Σα = e(Σθ) − D = −D, so ψ(P) + ψ(P^c) = −2B − D = −R ≡ p in C.
- **Every α_i is nonzero.** α_i is odd for singleton runs. For empty runs it is even and nonzero, because θ_i ≠ 0 (blocks are maximal) and e is injective.
- **FWIN is correct.**
  - E(P) and p − E(P) both lie in [0, p].
  - For κ+1 ≤ m ≤ (p+1)/2, both conditions of Fact 2.1 hold at E and at p−E: ⌈E/2⌉ ≥ 0 ≥ κ+1−m, and ⌊E/2⌋ ≤ (p−1)/2 ≤ p−m.
  - So I(P) = [−⌊(p−E)/2⌋, ⌊E/2⌋]. It has (p+1)/2 < p integers, so it does not wrap.
  - The map j ↦ 2j is a bijection from I(P) onto the even integers in [−(p−E), E].
  - For even t, t ≡ 2u_P (mod p) holds iff t ≡ e(2u_P) (mod 2p).
  - Then s = t − E ranges over [−p, 0]. Those are p+1 consecutive classes, and their complement is {1,…,p−1}.
  - I checked E = 0 and E = p by hand.
- **Lemma W's hypotheses are met.**
  - P is proper and nonempty, since m ≥ 2.
  - m is counted on the k-cycle of all runs, empty runs included.
  - Both γ endpoints come from Fact 2.1. Fact 2.2 is used only to get (1).

**2. CONNECT: correct, including complement patterns.**
- **Moves:** moving one boundary into a free adjacent site toggles exactly one run and keeps 2m boundaries.
- **Meet:** z = min(x,y) lies in L; I checked both the consecutive gaps and the wrap gap.
- **Descent:**
  - If the preceding gap of some i ∈ S equals 1, its predecessor is also in S. This holds in the wrap case too, using z ∈ L.
  - If no element of S could be decreased, every gap would equal 1, giving k = n and contradicting 2m < k.
- **Complements:**
  - Every pattern lifts into the same L.
  - P^c is the projection of (x_2,…,x_n, x_1+k), which lies in L. So P and P^c are connected.
- **Toggles:** an edge toggling each index follows from rotation invariance.
- **Sanity case (by hand, not relied on):** for k = 7 and m = 3, F_3 is a single 14-cycle.

**3. ILIFT and (5): correct.**
- **Uniqueness:** each edge difference lies in [−(p−2), p−2], which has 2p−3 integers, and is ≡ α_i (mod 2p). So h_i is unique and is the same in every layer, which makes the lift simultaneous automatically.
- **Properties:** h_i ≠ 0 and has the parity of α_i. Connectivity gives one constant c_m per layer.
- **The bound (5):** P^c ∈ F_m cancels c_m, so |Σ_P h − Σ_{P^c} h| = |N(P) − N(P^c)| ≤ p−2.
- **Existence:** h_i exists because some edge supplies it. The residues with no representative in the window (p and p±1) would already be a contradiction, so nothing is lost.

**4. LIGHT and SIGN: correct in all cases and at the boundary values.**
- **Weight bound:** S ≥ (k−2κ) + 4κ = k + 2κ, using |h_i| ≥ 2 (nonzero and even) on the 2κ empty runs.
- **Case 2:**
  - f = m0 − U0 lies in [1, m0).
  - Each boundary touches at most one flipped stretch, so exactly 2f boundaries disappear and p+1 sign changes remain.
  - The signed sum is at least S·U0/m0 ≥ 2U0 = p+1.
  - The case is vacuous at (5,1), where k = 7.
- **Case 3 with m0 ≥ 1:**
  - n − 2f ≥ p−2−2m0 ≥ p−2−2κ ≥ 1. This is exactly where κ ≤ (p−3)/2 is used, and the slack is exactly 1 at m0 = κ = (p−3)/2.
  - Flipping pairwise nonadjacent interior indices adds exactly 2f sign changes.
  - Since 1−2f/n ≥ 0 and (2f/n)·e_J ≤ 2κ, the signed sum is at least p−2+2m0.
- **Case m0 = 0:** k − 2L0 = p−2 > 0, and S > k because κ ≥ 1. So the sum exceeds p−2.
- **Boundary values:** κ = 1, κ = (p−3)/2, p = 5 (κ = 1 only, with k = 7, L0 = 2, U0 = 3), and m = L0 or U0 (where 2m ≤ p+1 < k) all pass.
- **Membership:** the positive set has 2m sign changes with L0 ≤ m ≤ U0, so it lies in F_m.

**5. Avoidance notion: consistent, with one bridge left unstated (m1).**
- **Rotation invariance:** an identity product stays the identity under cyclic rotation, because g_1…g_n = 1 implies g_{j+1}…g_n g_1…g_j = 1 by conjugation.
- **Equivalence:** an identity 2p-subword of the cyclic word, read from any start, is therefore the same thing as an increasing-index identity 2p-subword of any linearisation.
- **Normalisation:** the normalising maps preserve this notion.
- **Same notion throughout:** the proof also needs "avoids" in Fact 2.2 to be exactly the negation of Lemma W's conclusion (ordered, exactly 2p letters). The candidate assumes this without saying so.

**6. Consistency with I.14: correct.**
- (p−3)/2 equals 1 at p = 5 and 2 at p = 7. So (5,2), (5,3) and (7,3) are **not** covered.
- At p = 7, κ = 2 was already excluded, and κ = 1 is not a residual cell.
- For p ≥ 11, ⌈(p+1)/4⌉ − 1 ≤ p/4 ≤ (p−3)/2. So the whole open band lies inside the theorem's range, and together with I.14 every κ in [2, p−1] is covered.
- Nothing from the FP-1 diversity statements or from R > p is used or claimed.

## Findings (all MINOR)

- **m1 (statement and §6).**
  - **Issue:** the conclusion is phrased for a linear word in increasing index order, but Lemma W and setting (S) are stated for the cyclic word. Also, "avoids" is never stated to be the same notion in Fact 2.2 and in Lemma W.
  - **Fix:** add the rotation-invariance sentence from item 5. State that "avoids" means the negation of Lemma W's conclusion, and cite where (S) defines it.
- **m2 (FWIN proof).**
  - **Issue:** the proof uses 0 ≤ E ≤ p without saying why.
  - **Fix:** add "since 0 ≤ A_P + B_{P^c} ≤ A + B = p".
- **m3 (CONNECT).**
  - **Issue:** "this preserves the preceding gap" is false as written; decreasing x_i lowers that gap by 1.
  - **Fix:** "keeps the preceding gap ≥ 1 and keeps x_i ≥ z_i".
- **m4 (§1 imports).**
  - **Issue:** the parent verdict accepts Lemma W and Facts 2.1–2.2 at "per-claim scopes as in the foundation review §C, with I.10/I.11", which the candidate does not cite. None of S1/m1–m7 touches these interfaces. The (S) normalisation is an accepted ingredient that is not listed, and A ≥ B is never used after it.
  - **Fix:** cite §C/I.10/I.11 and state that a pattern is any proper nonempty set of the k runs, empty runs included. List the normalisation as part of the setting, not as an interface.
- **m5 (SIGN, Case 3).**
  - **Issue:** the transfer of independence from LIGHT's augmented cycle back to the k-cycle is implicit.
  - **Fix:** add "indices of J that are adjacent in the k-cycle lie in one stretch interior, since stretch endpoints are excluded and m0 ≥ 1".
- **m6 (§§2, 4–5, notation).**
  - **Issue:** E names both E(P) and the marked set. F names the reflection count, the families F_m and the flipped set. FWIN says "its unique integer representative in [1,p−1]".
  - **Fix:** rename the marked set Z and the flipped set Φ. Write "its representative in [0,2p) lies in [1,p−1]".
- **m7 (SIGN, Case 2).**
  - **Issue:** same-parity stretches are nonadjacent only when 2m0 ≥ 4, which holds since m0 ≥ U0+1 ≥ 4 but is not stated. The count is exact because each boundary touches at most one flipped stretch, not because one stretch stays unflipped.
  - **Fix:** note m0 ≥ 4 and give that reason for "exactly 2f".

## Sketch check

No step is a sketch. FWIN, CONNECT, ILIFT, LIGHT and SIGN are complete proofs. m1, m2 and m5 each omit a single routine sentence, not an argument.

## Exact supported conclusion

**Theorem RP-LIFT holds as stated.** Let p ≥ 5 be prime and w a word of length 4p−2 over D_(2p) such that:
- its rotation letters lie in one pair {ρ_x, ρ_−x}, x ≠ 0, and exactly R = p letters are rotations;
- every maximal cyclic constant reflection block has odd length;
- 1 ≤ κ = p−1−Σ⌊l_i/2⌋ ≤ (p−3)/2.

Then w has 2p letters, in increasing index order (equivalently, in cyclic order from any start), whose product is the identity. This holds for every B, with no purity, B < κ or value hypothesis. Its only mathematical premises are Lemma W and Facts 2.1–2.2 of v5 at the parent-accepted scope, plus the (S) normalisation.

**Coverage.**
- In setting (S) at R = p, the band 2 ≤ κ < ⌈(p+1)/4⌉ is now excluded for every p ≥ 11. Together with I.14, every R = p cell with κ ≥ 2 is excluded for p ≥ 11.
- The open R = p cells are now exactly (5,2), (5,3) and (7,3). (5,2) and (7,3) are excluded only under the FP-1 diversity hypothesis, which does not count as coverage.
- Everything at R > p outside the accepted bands remains OPEN, as do REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and ordered Olson for D_(2p).
- No novelty is claimed.
