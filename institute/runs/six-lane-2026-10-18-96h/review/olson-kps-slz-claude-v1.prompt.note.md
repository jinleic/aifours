# Referee report: ordered-Olson D₂ₚ candidates (import-Sp v1, KPS v4, SLZ-EXT v2)

**Basis.** I used only the embedded texts: no tools, search or delegation. I did not recompute any SHA-256. I only checked that the hashes the embedded documents cite for each other agree with the headers given, and they do.

**Summary: 0 FATAL, 0 MAJOR, 8 required MINOR, 2 editorial MINOR.** Every item is correct at its stated scope once the MINOR repairs are made. No repair changes a proof strategy.

---

## Verdicts

### (1) Import note — ACCEPT-WITH-FIXES

The logic is sound relative to the quoted Thm 3.1. The trust boundary needs three corrections.

- **Lemma SPLIT ✓.**
  - |y|_g + |z|_g is a positive integer congruent to |x|_g mod n, and |x|_g is the least positive member of that class.
  - Summing gives n‖M‖_g ≤ n‖M′‖_g. A positive multiple of n that is ≤ n equals n.
  - It silently needs x ≠ 0 (M-4).
- **Claim P ✓, including l = 0.**
  - Family A: 2g is even for every g. Its exponent is forced to n/2 − 1 = p − 1 ≥ 1 by |S| = p + 1, so lost exponent layout cannot remove it.
  - Family B: (p+1)g is even for every g, so any positive exponent on it is excluded.
  - l = 0 gives S = gᵖ(pg). Oddness forces g odd. g = p gives p^(p+1), which contains the proper zero-sum p·p. So g is a generator and the coefficient sum is p + p = 2p.
  - All quoted coefficient parities survive lost minus signs. The argument is robust to the PDF damage disclosed.
- **IDX1-odd(p+1) ✓.**
  - M′ has length p + 2, so (I1) gives a basis {a}.
  - M′ keeps odd terms of M, so a is odd.
  - If a = p, every nonzero term of M′ equals p, and p·p is a proper zero-sum. So a is a generator.
  - The least coefficients then sum to ord(a) = 2p, so ‖M′‖_a = 1, and SPLIT gives ‖M‖_a = 1.
  - The case split (splittable / unsplittable) is exhaustive by definition.
- **Equivalence with S(p) ✓.**
  - x = −σ(U) is odd, hence nonzero.
  - Minimality of Ux is argued correctly in both cases (zero-sum avoiding x, zero-sum containing x).
  - In the converse, |m|_g = 2p − Σ_U|·|_g.
- **Trust boundary.** It is accurate on the essentials:
  - Xia–Yuan's primary text was not read.
  - The statement comes only via an extracted restatement in Peng–Sun and a second-hand slide quote.
  - The n-hypotheses are unverified.
  - zbMATH is not used, and splitting monotonicity is proved rather than imported.

  It is inaccurate or incomplete in three places: M-1, M-2 and M-3.
- **Credit.** The note closes two gaps in the parent note's sketch:
  - Family B with l = 0 has no (1+n/2)g term.
  - The index-one basis element must be shown to be a generator, since the index is a minimum over generators.

### (2) Lemma FB-p — ACCEPT

- **(R) Realisation.**
  - From X_i ≥ p − n: for 1 ≤ n ≤ p − 1, W ≥ (n+1)X_i + n ≥ p + n(p−n) ≥ 2p − 1, with equality iff n ∈ {1, p−1}.
  - n = 1: W = 2p − 1, X_i = p − 1, the other p − 1 terms are units, and a_(h) = p. So Y′ = g^(p−1)(pg).
  - n = p − 1: forces X₁ = m = 1, and then heavies ≥ 3 give W ≥ 3p − 2.
  - n = p: every term is heavy, so W ≥ 3p.
  - Outside (X), a_(i) ≤ X_i, which is stronger than the filling condition.
  - The first occurrence of each heavy value is realised by strictly smaller terms.
  - An even s cannot be a singleton. s = 2 uses m ≥ 3 (or m = p when h = 0).
- **(Z) Shape of Z.**
  - In (X), sums of at least two terms from {1^(p−1), p} cover [2, 2p−1] except p, so z ∈ {g, pg}.
  - Outside (X), the cases are r = 1 or r ≥ W + 1, so s ≤ slack.
  - W ≥ L + 2h gives m − slack ≥ 2L − 2p + 1 + h = h + 1 at L = p, so m > s.
  - g^s z is a zero-sum of length s + 1, so s + 1 ≤ 2t by maximality.
- **(B) Balance and room.**
  - r ≥ 2 because s₍₁₎ ≤ δ − 1.
  - y ≤ s₍ᵣ₎ − 1 ≤ slack − 1 < m.
  - y + r ≤ δ by the integer form in erratum O1.
  - σ(Z*) = 2p + n₊ − S(N), and |Z*| = p + 2t − (y + r).
  - |Z*| is even, so y + r is odd. W is odd and ≥ p.
  - If W ≥ p + 2, then |Z*| ≥ 2t + 2.
  - If W = p, either y + r ≤ p − 2, or y + r = p.
    - y + r = p forces S₍ᵣ₋₁₎ = (r−1)s₍ᵣ₎ = δ − 1 and (r−2)(s₍ᵣ₎−1) = 0.
    - r = 2 would give s = p − 1, which is even: impossible.
    - So r = p and every s = 1. Then gᵖ(−g)ᵖ is a 2p-zero-sum, which the hypothesis excludes.
  - Balance follows from 0 ≤ S(N) ≤ slack and 0 ≤ n₊ ≤ 2t ≤ 2p − 2.
- **Scope.** FB-p correctly avoids invoking FB, REALIZE or SC0 at L = p, which is outside their accepted scope (as the FB verdict warns). It re-derives what it needs.

### (3) Lemma ARC0 — ACCEPT

- **Filling for fixed e.**
  - The available sizes are m = |e| + 2j₀ + z, with 0 ≤ j₀ ≤ J and 0 ≤ z ≤ b.
  - Since b ≥ 1, consecutive blocks overlap, so the sizes fill [|e|, |e|+2J+b].
  - The signed value is ec = τ.
- **(X1).** [−U₋, U₊] contains exactly p integers, so some e has |e| ≤ p − 1. Then top ≥ |e| + 2κ̂ + 1 ≥ x + 1, so the window [x, min(top, 2p−2)] contains an even integer.
- **(X2) identity.** |e| + 2J = a − |e − e*| holds for both signs. With J = min(U₊−e, U₋) for e ≥ 0 and J = min(U₊, U₋+e) for e < 0, both reduce to min(2U₊−e, 2U₋+e).
- **(X2) nearest representative.**
  - The representatives e₁ and e₁ + p, and e*, all lie in a window of length 2p − 1.
  - The nearer representative is within p − 1 of e* (within (p−1)/2 if e* lies between them).
  - Hence top ≥ 2κ̂ + 1.
- **(X2) case split.** The four cases on |e| are exhaustive, since |e| ≤ max U± ≤ 2p − 1.
- **(X2) corner |e| = 2p − 1.** Here {U₊, U₋} = {2p−1, 0}. The other representative is e′ = ±(p−1) with J = 0, giving sizes [p−1, 2κ̂], which contains 2κ̂ ≥ p + 1.
- **ARC hypotheses.** m is even with 2κ̂ ≤ m ≤ 2p − 2, and m ≤ R holds automatically. Equivalently C = 2p − m ∈ [2, 2H+2].

### (4) Theorem ROT-KP+ — ACCEPT-WITH-FIXES; Corollary — ACCEPT

Both hold relative to Import S(p), at the range fixed by M-1.

- **Branches.**
  - κ̂ = 1: ROT-KP.
  - t ≤ κ̂ − 1, including t = 0: ROT-FB(b) at its accepted scope (every zero-sum has length ≤ 2κ̂ − 2).
  - t = κ̂:
    - Y′ has length p and is zero-sum-free. S(p) gives g = Y(c) with c ≠ 0.
    - (ZP) excludes length 2p, since 2κ̂ + 2 ≤ 2p.
    - All FB-p hypotheses hold, with 1 ≤ t ≤ p − 1.
- **Case (X).**
  - pg = Y(0). We have n₊ + q = 2κ̂ and n₊ + pq ≡ 0 (mod 2p).
  - q even gives n₊ = 0 (family X1). q odd gives n₊ = p and q = 2κ̂ − p ≥ 1 (family X2).
  - ARC0 applies, since 2κ̂ ≤ 2p − 2.
- **Case (N), weights and E.**
  - n₋ ≥ 1, since otherwise 2tg = 0 with 1 ≤ t ≤ p − 1.
  - e′ ≤ p − 1 − n₊ ≤ p − 2, and e′ is even, so e′ ≤ p − 3.
  - s_i ≤ p − 1 − e′, and s_i is odd, so s_i ≤ p − 2. The weights are canonical, with no ρ₀.
  - E = e′ + n₊ − n₋ ≤ p − 1 − n₋.
- **Case (N), (H).** n₊ ≤ p − 1 gives E ≤ 2H.
- **Case (N), (K) with η = 1.**
  - If n₊ ≤ 2κ̂ − 2, KETA gives η + a_max ≤ p − 1.
  - If n₊ = 2κ̂ − 1, then n₋ = 1, s₁ = 2κ̂ − 1 ≥ 3 is the only heavy, and e′ = 0.
  - So g^(p+2κ̂−1) ⊆ Y. (ZP) forbids g^(2p), so 2κ̂ ≤ p, and parity gives 2κ̂ ≤ p − 1.
- **Case (N), (K) with η ≥ 2.** This branch is correct but needs M-5.
- **Caller scope.**
  - The ROT-KP verdict (m5/m6) establishes that SHgen has no hidden k ≤ p − 1 restriction. SHgen-E base words keep k = p and o_F(u°) ≤ p, and the (K) equality case is allowed.
  - That this discharge does not depend on κ̂ is exactly what the FB verdict accepted when it closed R1 for ROT-FB(b) at κ̂ ≥ 2.
  - §4 cites this correctly; §1 does not (M-6).
- **Corollary.**
  - The split k = 1 / 2 ≤ k ≤ p − 1 / k = p is exhaustive under k ≤ o ≤ p.
  - κ̂ ≤ κ(w) ≤ ⌊2p/3⌋ supplies S1-sharp. Restricted REFL applies at o ≤ p.
  - The ledger is that of the accepted KP corollary: Case 1 uses o ≤ p ≤ 2p − 3, and Cases 2 and 3 preserve both bounds.

### (5) Lemma SLZ — ACCEPT-WITH-FIXES

- **(S1) for T − d.** T − d satisfies (S1_κ) because its zero-sums are proper zero-sums of T. Hence t_d ≤ κ.
- **t_d ≥ 1.** This holds by Davenport (|T − d| ≥ 2p + 1), independently of L.
- **FB instantiation when L ≥ p + 1.**
  - κ′ = t_d ≤ p − 2, and k′ = 2p − L ∈ [1, p−1].
  - The Setting fact gives m − slack ≥ 2L − 2p + 1 + h ≥ 3.
- **d = (2p − W)g.** σ(T−d) = σ(C) + σ(Z₀) = Wg.
- **Descent dU.**
  - The negative part N is nonempty.
  - dU is a zero-sum of length N_T − s − 1. It omits s + 1 ≥ 2 terms, so it is proper and not long, and its length is ≤ 2κ.
- **Bounds.**
  - s ≤ 2p − 1 − L = 2p − N_T + 2t_d gives 2N_T ≤ 2(p+κ+t_d) + 1, so N_T ≤ p + κ + t_d.
  - L ≤ p is equivalent to N_T ≤ p + 1 + 2t_d.
  - Both bounds are ≤ thr, since t_d ≤ κ.
- **Required fix.** The shared instantiation lacks t₀ ≤ p − 1 (M-7). It is satisfied at this call site.

### (6) Lemma EXT — ACCEPT-WITH-FIXES

- **t₀ = 0 (SC0).**
  - SC0 applies since L ≥ p + 1.
  - Every zero-sum contains y, and its coefficient sum lies in [1, 4p−2] ∩ 2pℤ = {2p}.
  - Its length is 2p − (c−1) − mass ≤ 2p, so (ZP) excludes it.
- **Step 1.**
  - Positive coefficients total at most W + n₊ + c ≤ 4p − 2; negatives total at least −n₊ > −2p. So σ_g ∈ {0, 2p}.
  - The identity |S| = σ_g + f(S_N) − mass₊ holds, since the number of positive terms is σ_g + S(S_N) − mass₊.
- **Step 2.** The arithmetic is correct and uses |Y₁| ≥ p + 2κ.
- **Step 3, descent.**
  - D(S*) ≥ 2 gives c ≤ 2t₀ − 1.
  - The modified sequence keeps σ_g = 2p.
  - Each removal lowers D by s + 1 ≤ 2p − 2κ.
  - The stopping set has length in [2κ+2, 2p], contradicting (ZP).
- **Step 3, validity.**
  - |U(N₁)| = 2p − c − A(H*) + S(N₁) ≥ (2p + 2κ + 1 − c − A − |H*|)/2 ≥ 3.
  - This uses A + |H*| ≤ e′ + 2h ≤ 2e′ ≤ 2(p−2), and 0 ≤ |U(N₁)| ≤ |U*| as required.
- **Required fix.** M-7 applies here too (t₀ ≤ κ ≤ p − 2 holds at this call site).

### (7) Corollary PROP — ACCEPT-WITH-FIXES

- Case 1 gives L ≥ p + 1 from t₀ ≤ κ.
- Case 2 gives L ≥ p + 2 from t₀ ≤ κ − 1.
- (ZP) is hereditary.
- Each induction step keeps length ≥ thr, so L ≥ p + 1 holds for the new longest zero-sum.
- The base case fails at κ = 0 (M-8).

### (8) Corollary RED — ACCEPT-WITH-FIXES

- **Minimal counterexample.**
  - If R₀ > thr, every Y − x satisfies (S1), so every long zero-sum contains every term.
  - Then T = Y is the unique long zero-sum, and SLZ gives R₀ ≤ thr: a contradiction.
- **Length-thr dichotomy.** This follows from PROP case 2, and inherits M-8.
- **Shrink step.** It is under-stated (E-2).

---

## Findings

### FATAL — none

### MAJOR — none

### MINOR (required)

- **M-1 — import §1 (and KPS v4 header/§0/§6).**
  - Problem: Import S(p) is stated "for every prime p ≥ 5". But §2 makes it conditional on n = 2p lying in Thm 3.1's unverified n-range, and §5 says "(n = 2p within the range of (I2))".
  - Repair: state it as "for every prime p ≥ 5 with 2p in the n-range of (I2) (lane uses p ≥ 7)". Have KPS v4's "relative to Import S(p)" carry this proviso.
- **M-2 — import §2, last sentences of the trust boundary.**
  - Problem: "n ≥ 14 for the lane's applications; p = 5 covered only if Thm 3.1 includes n = 10" singles out n = 10. Nothing recorded supports n ≥ 14 either: the Peng–Sun hypothesis is not quoted, and the slide-25 quote is unqualified and second-hand.
  - Repair: record the n-hypothesis printed in Peng–Sun Thm 1.3 (the parent read it). Otherwise, state that the n-range is unverified for every n.
- **M-3 — import §0, §2, §4 heading.**
  - Problem: "the only property of (I2) used" understates what is used. Claim P also needs:
    - (i) the two families exhaust *all* unsplittable minimal zero-sums of length ⌊n/2⌋+1 at n = 2p;
    - (ii) Xia–Yuan's "unsplittable" coincides with §0's definition.

    The source of (ii) is not recorded.
  - Repair: list (i) and (ii) as trust items. Record that the definition comes from Peng–Sun §1 (parent-read), and that Xia–Yuan's own definition was not read.
- **M-4 — import §3, Lemma SPLIT.**
  - Problem: |x|_g is undefined for x = 0, and (0) is a minimal zero-sum.
  - Repair: add "M has no zero term (automatic if |M| ≥ 2)".
- **M-5 — KPS §4 (K), branch η ≥ 2.**
  - Problem: the inequality E ≥ (a_max−1) + 2(η−1) is load-bearing.
    - KETA as accepted gives only η + a_max ≤ E + 2 ≤ p when n₊ = 2κ̂ − 1, one more than (K) allows.
    - η and a_max are defined nowhere in the embedded sources.
    - "Otherwise η ≥ 1" and "s₁ is the only heavy" presuppose that η counts heavy letters of both signs.
  - Repair: state the SHgen v3/KETA definitions with a citation: η = number of letters with |b| ≥ 3 relative to c, and a_max = largest |b|. If a_max is instead the largest positive weight, the bounds only improve. Then add the one-line derivation: the a_max letter contributes a_max − 1 to E, and each other heavy contributes at least 2.
- **M-6 — KPS §1 import line.**
  - Problem: "SHgen/SHgen-E with the ROT-ZR caller discharge and restricted REFL for o_F(u°) ≤ k ≤ p" is wrong. The ROT-ZR discharge is accepted only for k ≤ p − 1 (ROT-ZR verdict; FB erratum R1).
  - Repair: cite the ROT-ZR discharge for k ≤ p − 1 only. For k = p, cite the ROT-KP verdict m5/m6 with ZX overlay 4/V3, extended to κ̂ ≥ 2 by the FB verdict's R1 closure, as §4 already does.
- **M-7 — SLZ-EXT §1, FB instantiation.**
  - Problem: the hypothesis t₀ ≤ p − 1 is omitted. (S′) needs κ′ < p, and FB's balance uses n₊ ≤ 2t < 2p; the FB verdict lists t ≤ κ < p as essential.
  - As written the instantiation is false. Take Y₁ = g^(3p+1):
    - Z₀ = g^(2p), so t₀ = p.
    - The complement g^(p+1) is zero-sum-free, with L = p + 1 and W = p + 1.
    - N = ∅, so S(N) = 0 ≠ n₊ = 2p.
  - Repair: add "t₀ ≤ p − 1". Note at both call sites that it holds: t_d ≤ κ ≤ p − 2 in SLZ, and t₀ ≤ κ ≤ p − 2 in EXT.
- **M-8 — SLZ-EXT §0 and §4, PROP case 2 and RED clause 2 at κ = 0.**
  - Problem: with nonempty zero-sums, "no zero-sum of length 2κ = 0" does not give t₀ ≤ κ − 1. Then L = p and EXT does not apply.
  - The statements remain true: (ZP₀) implies (S1₀) by Davenport, since any nonempty zero-sum contains a minimal one of length in [2, 2p].
  - Repair: restrict case 2 to κ ≥ 1 and dispose of κ = 0 by Davenport. RED's clause 2 is then vacuous at κ = 0.

### MINOR (editorial)

- **E-1 — SLZ-EXT §2–§3, notation.**
  - Problem: N denotes both |T| and the negative part of Z₀ in the same paragraph ("N is nonempty", "length N − s − 1"). S(N₁) denotes both a sum of the s_i and a sequence.
  - Repair: rename, e.g. N_T for |T| and S^(N₁) for the sequence.
- **E-2 — SLZ-EXT §4, RED last sentence.**
  - Problem: the descent from length > thr + 1 down to thr + 1 is not spelled out.
  - Repair: add "by PROP case 1, every one-term deletion of a counterexample of length ≥ thr + 1 is again a counterexample; iterate".

### Optional

- **O-1 (import §4).** gᵖ(pg) is splittable: pg = g + (p−1)g yields the minimal zero-sum g^(p+1)((p−1)g). So Claim P can be stated as "no all-odd unsplittable minimal zero-sum of length p + 1 exists". This uses only the quoted classification, without the elided conditions or "ind ≥ 2".
- **O-2 (FB-p (R)).** Record a_(h) = p in the n = 1 case, and use the unified bound W ≥ p + n(p−n).
- **O-3 (FB-p (B)).** Make two points explicit after "exactly as in Lemma FB":
  - y < m uses m ≥ slack + 1 + h, not FB's m ≥ slack + 3;
  - the argument is a re-derivation, because FB's own scope requires L ≥ p + 1.
- **O-4 (ARC0).** Note that R = a + b = p + 2κ̂, so k = p is implicit, and that m ≤ R holds automatically.
- **O-5 (RED).** PROP alone already yields the reduction, so the SLZ paragraph is not needed for RED.

---

## Steps needing more than the embedded imports

1. **Claim P** needs three things beyond the embedded quote, all declared trust items rather than logical gaps:
   - exhaustiveness of Thm 3.1 at n = 2p;
   - its n-range;
   - the definition of "unsplittable".
2. **ROT-KP+ (K), η ≥ 2** needs the SHgen/KETA definitions of η and a_max (M-5).
3. **The SHgen/SHgen-E call at k = p, κ̂ ≥ 2** is available only as accepted-scope statements: ROT-KP verdict m5/m6 and FB verdict R1. SHgen's internals and REFL condition (d) cannot be checked here. They are used at their recorded scope, so this is no gap.
4. **SLZ/EXT** use ZSTRUCT and the Setting fact in (S′) for κ′ ≤ p − 1. These enter via FB §1 "verdict overlay 5"; the BAL-full verdict is not embedded. They are within accepted scope once M-7 is applied.
5. **KPS** uses GRX (ZP), DAV, R = p + 2κ̂ and the normal-form facts, which are embedded by reference only.

No finite probe or parent control is used as a premise anywhere in the three candidates.
