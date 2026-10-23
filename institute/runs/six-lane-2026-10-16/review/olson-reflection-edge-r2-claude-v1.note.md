# Hostile audit: Lemma EDGE r2, extended B0S-CJ''', extended REFL-B0

`SS:LL` means SOURCE SS at LF line LL. This was a static reading only. I did not recompute the hashes.

## Verdicts

| Object | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|
| Lemma EDGE (00) | **ACCEPT-WITH-FIXES** | 0 / 0 / 5 |
| B0S-CJ'''' (CJ''' under R ≥ 4κ−4 alone, 00:16–18) | **ACCEPT-WITH-FIXES**, conditional on EDGE | 0 / 0 / 1 |
| REFL-B0 without 2κ ≤ p−1 (00:19–20) | **ACCEPT-WITH-FIXES**, conditional on EDGE; the argument is valid but only sketched | 0 / 0 / 3 |

I found no counterexample. I re-derived every kill from the six H0 inequalities. All findings are presentation or citation gaps, and each has a repair in §6.

## 1. Imported versus new

**Imported and accepted.** I checked how each is applied, not its proof:
- the H0 instance and the kill test (02:24–43, 03:35–37);
- P0;
- Lemma C1 (03:69–78);
- the equivalence of the six conditions (02:72–77);
- the Case II construction (02:93–113);
- CJ''' at its overlay scope (04:13);
- RED's process, K0*, K1* and the small-k verdict;
- REFL-B0's monotonicity κ' ≤ κ with R' = R (06:37–45, reviewed at 07:17–51 and 08:29–53).

**New and audited here:**
- the claim that CJ''' items 2–5 and Case II hold without 2κ ≤ p−1 (00:28, 00:68–73);
- facts (F2)–(F4);
- kill conditions (K1)–(K3);
- Steps 1–5;
- the reduction to edge cells (00:17–18);
- the REFL-B0 transfer (00:19–20).

## 2. Imported inequalities in the edge cells, without 2κ ≤ p−1

In the edge cells, κ = (p+1)/2, R ∈ {2p−2, 2p−1}, k = 3p+1−R ∈ {p+3, p+2}, Δ ≤ (3−p)/2 ≤ −1, and 4κ−4 = 2p−2. So R = 2p−2 lies exactly on the boundary R = 4κ−4.

- **Windows (01:29–30, 03:59–61).**
  - These need R ≥ 2κ+1 = p+2, which holds.
  - The cap p−1 in g₁ is inactive because E ≤ R ≤ 2p−1 (03:56). That uses the trivial cut, not 2κ ≤ p−1.
- **C2(a) (01:31–39).**
  - Two small parts: the criterion is m₁+m₂ ≥ 4κ−4−R, and the right side is ≤ 0. The value −2 is attained at R = 2p−2 by two parts of mass 0. That is allowed, since (A') only needs ≥ −2.
  - One small part needs R ≥ 2κ−2.
  - Three small parts need R ≥ 3κ−2 = (3p−1)/2.
  - All hold.
- **C2(b) (01:40–47).** Since 2Δ−1 ≤ −3, every split qualifies.
  - One small pair sum: ⌈s/2⌉ ≥ 0 ≥ Δ.
  - Two small pair sums: 3R+m_b ≥ 2p+4κ−4 = 4p−2, which holds.
  - Three small pair sums need R ≤ 3κ. That happens only at (5,3,8), (5,3,9) and (7,4,12), and there 2R−3κ ≥ p−2.
- **C1(c) and SIGMA-2P.**
  - C1(c) needs only nonempty windows.
  - SIGMA-2P for Δ ≤ 0 (01:48, 03:89–90) uses only C2(b) and C1(b), C1(c).
  - So J = 0 and Σbh = 2p−R ∈ {1, 2}.

**Where 2κ ≤ p−1 is actually used.**
1. Case I (U1)/(L1), through "Φ ≤ 4κ ≤ 2p" (01:62, 03:106).
2. CJ (F2) (05:39–40), which is used only when Δ ≥ 1.
3. The B0S++ Corollary (03:25–26), which is used only when Δ = 1.

In the edge cells only use 1 is live, and that is exactly the step EDGE replaces.

**Case II (00:68–73, checked against 02:93–113 with x_t := w_t).** The generic relations re-derive: δ_Z = 2κ−|Z|+s, |Z| ≤ κ−m_Z, s ≤ g_Z−2m_Z, δ_Z−ρ_Z ≥ 4m_Z, and 2 ≤ d ≤ g_Z ≤ κ−1.
- (L3): δ_P ≤ 2κ−2 = p−1 ≤ R−1.
- (U1):
  - for W = {y}, the left side is ≤ −2m_Z+r_y+3 ≤ r_y+1 ≤ 2p;
  - otherwise it is ≤ 3κ−7 < 2p.
- (L1): the left side is ≤ 4κ−4 = 2p−2 < 2p.
- (L2):
  - for W = {y}, it needs R ≥ 4κ−5;
  - otherwise it needs 2p−2 ≤ 2R−p−3, i.e. 2R ≥ 3p+1.
  - The second is an equality at p = 5, R = 8, which is permitted.
  - That branch cannot occur at p = 5 anyway: there d = 2, every y ∈ F has r_y+1 ≥ 2, so W = {y}.
- |F| ≥ d/2 is equivalent to k ≥ 2+2|Z|−ρ_Z. This holds because 2+2|Z| ≤ 2κ < k.
- Properness (02:106–107) is generic.

## 3. The new mathematics

**(F2)–(F4).**
- (F2): g(0) = −κ, and g(R) = p−1 because R−κ ≥ (3p−5)/2 > p−1.
  - So gap({t}) = [1−κ, 0], which has κ < p elements.
  - Genuineness (u_t ≢ 0) then gives x_t ∈ [1−κ, −1] and bh ≤ −2.
- (F3): for a defect, x_t ≤ ⌊r_t/2⌋ and x_t ≥ g(r_t)+1 force g(r_t) = r_t−κ.
  - So c_t = 2(r_t−x_t) is even and lies in [2, 2κ−2].
  - Equality c_t = 2κ−2 holds iff x_t = r_t−κ+1.
  - The derivation valid here is 03:99–102 (see E3).
- (F4): the trichotomy misses one case (see E1).

**(K1)–(K3).** Write x = (ρ−δ)/2. The six H0 inequalities x ≤ p−m, x ≤ ρ+m−κ−1, x ≤ ⌊ρ/2⌋ and their three mirrors are exactly (U1)–(L3) (02:74–77). Parity facts used below: δ ≡ ρ, bh ≡ r, and Φ is even.

- **(K1).**
  - δ ≥ 0 on Z gives (U3). (U1) and (L1) are both bounded by Φ ≤ 2p.
  - (L2): Φ−4m ≤ 2p−4 ≤ 2R−p−3, using m ≥ 1.
  - (L3): if ρ = 0, then δ ≤ 2p−2 = R−[R odd], with equality allowed. If ρ ≥ 1, then δ ≤ 2p−3 ≤ R−1.
  - Properness holds because P ⊆ Z ⊊ [k].
- **(K2).**
  - m = 2 requires the two defects to be non-adjacent.
  - With Φ = 2p+2, (U1) becomes δ ≥ 1 and (L1) becomes ρ ≥ 1.
  - The case δ = 0 is exactly the FM obstruction, which Step 3 closes.
  - (L2): 2p−6 ≤ 2R−p−3.
- **(K3).**
  - δ_P = p−1−bh_y can be negative. Condition (b) is exactly δ_P ≥ 0.
  - Φ = p+3+r_y−bh_y.
  - (U2) ⇔ (a), (U3) ⇔ (b), and (U1) ⇔ (c). Note (3p−5)/2 is an integer.
  - (L1) holds because x_y ≥ (r_y+1)/2 ≥ 1.
  - (L2) is automatic: a violation forces r_y ≥ 2p+1 > R, because R−p+2 ≥ p.
  - (L3): δ ≤ p−2 ≤ R−1.

**Step 1.**
- P' is nonempty, because a singleton has Φ = c+2 ≤ 2κ. Also P' ≠ Z.
- For t ∈ Z∖P', maximality and evenness give Φ(P'∪{t}) ≥ 2κ+2.
- The increment is at most c_t+2 ≤ 2κ, so Φ(P'∪{t}) ≤ 4κ. If it is ≤ 4κ−2, then (K1) kills.
- If it equals 4κ, then Φ(P') = 2κ, c_t = 2κ−2, and the increment is of type +1, so t is not adjacent to P'.
- Replacing an end defect e of an interval of P':
  - If e's interval has ≥ 2 runs, removing e does not split it, and t stays non-adjacent. So Φ(P'') = 4κ−c_e ∈ [2κ+2, 4κ−2], and (K1) kills.
  - If e is a singleton, Φ(P'') = 4κ−2−c_e ∈ [2κ+2, 4κ−4] unless c_e = 2κ−2, so (K1) kills otherwise.
  - Hence P' = {e}.
- The claim at 00:86 that each other singleton is inclusion-maximal is true but unproved (see E2).
- Conclusion: the defects are pairwise non-adjacent, all have c = p−1, and Φ(Z) = 2κ|Z|, so |Z| ≥ 2.

**Step 2.**
- For a pair of defects, δ = 2p−2−ρ and Φ = 2p+2.
- (K2) fails only if ρ = 0 or ρ ≥ 2p−2. The latter means r_s = r_t = p−1.
- A mixed EB–FM pair, or any defect with 0 < r < p−1, has 1 ≤ ρ ≤ 2p−3, so it kills.

**Step 3 (FM).**
- |Z|(p−1) ≤ R ≤ 2p−1 forces |Z| = 2.
- Then Σ_Y bh = 2p−R ≤ 2. But |Y| = k−2 ≥ p, and every non-defect has bh ≥ 1. Contradiction.

**Step 4.**
- g₃(0) = 2−κ, using κ ≥ 3. g₃(R) = p−3.
- So I(P) = [3−p, 2−κ], and x(P)+p = 2−κ is its top endpoint.
- x(P) itself violates (L1), since 3p+3 > 2p. So the shift by p is essential. It is legitimate under the residue-class kill test (02:42–43).

**Step 5.**
- By (F2), every run of Y is nonempty.
- N₊ = 3p−1−R and Σ_Y bh = 4p−2−R.
- There is at most one common neighbour y₀: two would need k | 4, but k ≥ 7.
- **The point that makes the step work:** conditions (a), (b), (c) depend on y alone. So every y ≠ y₀, being non-adjacent to some t_i, violates one of them.
- The resulting bounds:
  - not (a) gives bh ≥ r+2, by parity;
  - not (b) gives bh ≥ p;
  - not (c) gives bh ≥ 3p−3−r. The stated bound 3p−4−r is weaker but still valid.
  - So bh ≥ r+2 when r ≤ p−2, and bh ≥ p−3 for a big run.
- At most two runs are big, because 3(p−1) > 2p−1.
- A big y₀ is counted once, in e, using only bh ≥ 1. This is conservative.
- Upper bound: M_S ≤ R−(N₊−|S|) ≤ p−1+|S|. This uses that Z has mass 0 and that every run of Y∖S is nonempty.
- Lower bound from the bh budget: M_S ≥ 2p−2|S|+b(p−3)+e. I re-derived the algebra.
- Combining them gives 2e ≥ p+1+b(p−6).
  - For b = 0, 1, 2 this forces p ≤ 1, 7/2, 13/3 respectively.
  - Each contradicts p ≥ 5, for both e = 0 and e = 1.

**Semantics.**
- Patterns are sets of cyclically indexed runs, and m counts cyclic intervals.
- Every kill is H0's increasing-index identity subword.
- No unordered product is used, and no census is a premise. The finite aid at 00:126 is labelled as a non-premise.

## 4. Corollary: R ≥ 4κ−4 alone

- R ≥ 2p is killed by ρ₁^{2p}, so R ≤ 2p−1.
- 2κ > p−1 with both sides even gives 2κ ≥ p+1. Also 4κ−4 ≤ 2p−1 gives 2κ ≤ p+1.
- So exactly two cells per prime remain: 2κ = p+1 and R ∈ {2p−2, 2p−1}. That gives 32 cells for p ≤ 61, matching 01:88.
- Both cells have Δ ≤ −1, so there the theorem says that no avoider exists. The other parts are unaffected:
  - Corollary 1 is purely combinatorial.
  - The shortcut 4Δ ≤ 2κ+2 (01:19–20) uses only R ≥ 4κ−4.
  - The Containment remark is unchanged.

## 5. REFL-B0 transfer

- The terminal word w_T has:
  - B = 0, all blocks odd, and genuine empty runs;
  - R(w_T) = R and 2 ≤ κ' ≤ κ;
  - k' = 2p−R+2κ'.
- No assumption on the block parities or o_F of w₀ is used.
- After deleting 2κ ≤ p−1, we still have R ≥ 4κ−4 ≥ 4κ'−4.
  - If 2κ' ≥ p+1, then R ≤ 2p−1 puts w_T in an edge cell, and EDGE excludes it.
  - Otherwise 06:46–50 apply verbatim, since both comparisons are monotone in κ'.
- **New initial cells:** κ(w₀) = (p+1)/2 with R ∈ {2p−2, 2p−1}.
  - Here o_F(w₀) = 3p+1−R ∈ {p+3, p+2} > p, so these cells lie entirely outside fewodd.
  - Both OR alternatives hold automatically: R ≥ (3p−3)/2, and 5R ≥ 10p−10 ≥ 7p−7.
  - If κ' < κ, then k' ≤ p+1 and Δ' ≤ (1−p)/2. So only κ' = κ ever reaches EDGE.
- **The first OR branch is redundant.**
  - R ≥ p+κ−2 implies 5R ≥ 4p+6κ−10, because κ ≤ p−1 (08:111–113). This does not depend on 2κ ≤ p−1.
  - Keeping or dropping the branch leaves the hypothesis set unchanged.
  - The extension adds no new restriction: there is no all-odd or o_F ≤ p assumption, all other R hypotheses are kept, and the rotations remain equal and non-identity.

## 6. Findings

**EDGE**
- **E1 MINOR (00:34–36).** The (F4) trichotomy omits a fourth case: t adjacent on both sides to the same interval.
  - That case would mean P∪{t} = [k]. It is impossible because P∪{t} ⊆ Z ⊊ [k] (00:67).
  - This is the same gap as overlay correction 3 (04:32).
  - *Repair:* add that sentence.
- **E2 MINOR (00:86).** "{t} is also inclusion-maximal" is asserted without proof.
  - *Repair:* c_t = 2κ−2 gives Φ({t}) = 2κ, and for t' ∈ Z∖{t}, Φ({t,t'}) ≥ c_t+c_{t'}+2 ≥ 2κ+2. Monotonicity (00:35–36) extends this to all supersets.
  - Alternatively, two adjacent extreme defects have Φ = 4κ−2, and (K1) kills directly.
- **E3 MINOR (00:32; also 00:8 and 00:68).** The defect bound is attributed to B0S-r4 (2.1).
  - That derivation (02:57–66) uses prefix lifts justified by facts that assume k ≤ p (02:38–40).
  - Those facts fail in the edge cells. At (p, κ, R, k) = (7, 4, 13, 9), p < 2κ+1 and R < p+2κ.
  - *Repair:* cite 03:99–102, where x_t := w_t lies in the singleton gap. Cite Case II as used through 03:96–103.
- **E4 MINOR (00:14).** The setting omits several standing assumptions:
  - F, R ≥ 1;
  - the normalisation to ρ₁;
  - genuine empty runs, which are used at 00:31;
  - the trivial cut R ≤ 2p−1, used at 00:17, 00:30 and 00:113.
  - *Repair:* "setting of 04:8, after the trivial cut."
- **E5 MINOR (00:28).** "Use only R ≥ 4κ−4 and R ≥ p" omits R ≤ 2p−1 (03:56), κ ≥ 1, and avoidance.
  - *Repair:* add these, together with the list of uses of 2κ ≤ p−1 from §2.
- *Notes, no change required:*
  - The bounds at 00:109–110 have slack.
  - At 00:126–127 the tuple order (κ, k, R) is not declared and E15b is not pinned. It is not a premise.
  - The label '''' at 00:16 does not match ''' in the title at 00:1.

**Extended CJ**
- **C1 MINOR (00:16–18).** *Repair:*
  - State that the theorem is read through 04:
    - "nonempty" in Corollary 1;
    - only the first two sentences of Corollary 2, with the shortcut 4Δ ≤ 2κ+2;
    - the p ≤ 23 claim is not extended.
  - Record that the new range is exactly two cells per prime, each with Δ ≤ −1.
  - The wording that keeps 2κ ≤ p−1 (01:16, 01:21–22, 01:86–88, 04:13, 04:41) can be superseded only by a new parent overlay.

**Extended REFL-B0**
- **R1 MINOR (00:19–20).** The transfer exists only as a parenthetical. *Repair, as r4 of 06:*
  - Delete "2κ ≤ p−1" at 06:17.
  - At 06:47, write: "R ≥ 4κ'−4, so B0S-CJ'''' applies; 2κ' ≥ p+1 is an edge cell, excluded by EDGE."
  - Update the import paraphrase at 06:30–33.
- **R2 MINOR (06:55–61).** Remark (1) becomes stale. *Repair:*
  - At p = 7, κ = 4 is now covered for R ∈ {12, 13}.
  - κ ≥ 5 is excluded because 4κ−4 > 2p−1, not because of 2κ ≤ p−1.
  - List the new cells and their o_F values.
- **R3 MINOR (06:42–43, 06:63–64; see 07:5–6 and 08:105–139).** r3 still carries the r2-review MINORs that were never applied:
  - PM0 is still said to append to "an odd one";
  - Remark (3) still says P3 changes R, κ and B;
  - Claude's m1 and m3–m7.
  - They do not affect the proof. *Repair:* fold them into the revision.

**Scope.** These are partial results on the B = 0, equal-rotation slice only. Nothing here claims full REFL(p), INV*(p), ordered Olson, or novelty.
