# Hostile audit: B0S-CJ (SOURCE00 r2) and B0S-CJ''' (SOURCE01 r4)

I re-derived everything on paper from the inlined text. No computation, finite aid or earlier verdict serves as a premise. I did not recompute the SHA256 pins.

Notation used throughout:
- R = 2p − k + 2κ and Δ = p + κ − 1 − R.
- (H) is equivalent to p ≥ 3κ+2+Δ.
- R ≥ 4κ−4 is equivalent to p ≥ 3κ−3+Δ.

## Dispositions

| Item | Disposition | FATAL/MAJOR/MINOR |
|---|---|---|
| Lemma CJ (SOURCE00:48–62) | ACCEPT | 0/0/0 |
| Theorem B0S-CJ (SOURCE00:22–23, 66–71) | ACCEPT | 0/0/0 |
| Corollary 1 (SOURCE00:24, 72–76) | ACCEPT-WITH-FIXES | 0/0/1 |
| Corollary 2 (SOURCE00:25–30, 77–87) | ACCEPT-WITH-FIXES | 0/0/1 |
| Containment (SOURCE00:31–34) | ACCEPT | 0/0/0 |
| **SOURCE00 overall** | **ACCEPT-WITH-FIXES** | **0/0/2** |
| **Theorem B0S-CJ''' with its transferred items (SOURCE01)** | **ACCEPT-WITH-FIXES** | **0/0/2** (MINOR-2 also transfers) |
| Base as used (SOURCE02 Secs. 1–3; SOURCE03:72–113) | no new defect | — |

No proof step fails. Every repair below is a local justification or wording change.

## Findings

**MINOR-1 (SOURCE00:26–30, 109–110): the p ≤ 23 sentence is justified by a computation.**
- The text cites "a direct enumeration … (eval transcript)", while Remark (4) says no computation is used.
- Written replacement:
  - A violating triple satisfies 3κ+2+Δ ≤ p ≤ κ+5Δ−6, so 4Δ ≥ 2κ+8.
  - Together with Δ ≤ κ−1 this forces κ ≥ 6.
  - κ = 6 forces Δ = 5 and p = 25, which is not prime.
  - κ ≥ 7 forces Δ ≥ 6, hence p ≥ 21+2+6 = 29.
- Also state the two hidden inputs:
  - the import that RES_<(p) words with B = 0 satisfy the setting (odd blocks, κ ≥ 1, genuine empty runs; SOURCE08:13);
  - the fact that k ≤ p falls in the Δ ≤ 1 branch.

**MINOR-2 (SOURCE00:24, 73–74): Corollary 1 needs nonempty arcs.**
- The proof uses A3 ≠ ∅: "the last run of A2 is not the last run of O(A1)".
- For Δ ≥ 1, mass ≥ 1 forces each arc to be nonempty. The statement, however, is unrestricted.
- With empty arcs allowed and k = 1 (the word at SOURCE00:32), (3H) holds but no proper interval exists, so (2HA) fails. This case is degenerate.
- Repair: write "three nonempty consecutive arcs".

**MINOR-3 (SOURCE01:60, 52–54): wrong set in the |P| ≤ κ argument, and one omitted case.**
- "Φ ≥ 2|P|+2" applied to P only gives |P| ≤ 2κ−1. It should be applied to P′: 2|P′|+2 ≤ Φ(P′) ≤ 2κ, so |P′| ≤ κ−1 and |P| ≤ κ.
- Properness is immediate anyway from P ⊆ Z ⊊ [k].
- The +1/0/−1 trichotomy omits the case "t is adjacent on both sides to the same interval of P′". That case forces P′ = [k]∖{t}, so P = [k], which P ⊆ Z ⊊ [k] excludes. Add this clause.
- Codex raised the first point in passing (SOURCE06:70); r4 did not apply it.

**MINOR-4 (SOURCE01:14–15, 77–79 against SOURCE00:66): the Δ ≤ 0 branch does not transfer "verbatim".**
- The B0S-CJ proof disposes of Δ ≤ 0 by citing "Theorem B0S++", which assumes (H).
- Under (H''') this branch must instead be SIGMA-2P's Δ ≤ 0 argument (item 5) followed by the re-checked kill (item 6).
- Item 7 says the transferred results "use only C1, C2, (F1) and (F2)", omitting both.
- Repair: add one sentence to item 7.

**Notes (not counted):**
- SOURCE00:82–84: when x*+1 = a−1, "[x*+2, a−1]" denotes the whole cycle under the cyclic convention. Write "the part of O after x*+1".
- SOURCE00:106–107: the (29,7,6) argument should also dispose of |O| = 1 (there m(O) ≤ 1 < 11).
- SOURCE00:32: the example has R ≥ 2p and k = 1, so it lies before the trivial cut. After the cut, k ≥ 2κ+1 ≥ 3. For Δ ≤ 0, every proper interval is then heavy and admissible (take x = b+1), so (2HA) holds automatically. Say what the example is meant to illustrate.
- SOURCE01:14 and :77 cite r1, but the text actually read is r2 (SOURCE01:125).
- SOURCE01:1 says "(r3)"; SOURCE01:5 says "UNREVIEWED" and should say "r4 not re-reviewed".
- SOURCE01:64–68 is correct but unnecessary: (L3) is equivalent to δ_P ≤ R by parity (SOURCE03:77–78), and δ_P ≤ 4κ−4−ρ_P ≤ R.

## Independent verification

### Base

- **Facts from P0:** n_E ≤ 2κ gives k ≤ p+2κ, R ≥ p and Δ ≤ κ−1.
- **Windows:** the window sum is ≥ min(R−2κ, (R−1)/2−κ), or ≥ R/2−1 when both terms are floors. So windows are nonempty for R ≥ 2κ+1, which is all that is needed.
- **C1(b):** gap(Q^c) = p − gap(Q).
- **C1(c):**
  - X lies in [U1+U2+2, 2p−L1−L2−2].
  - (A′) forces X ≥ U_Q+1; (B′) forces X ≤ p−L_Q−1.
  - Each closes using U_Q+L_Q ≥ 0, with negative endpoints and zero masses allowed.
- **Defects (from singleton gaps):** g(r_t)+1 ≤ x_t ≤ ⌊r_t/2⌋ forces r_t ≤ 2κ−2. Then r_t+δ_t ≤ 2κ−2, and r_t+δ_t is even and ≥ 2. For an empty defect, x_t ∈ [1−κ, −1] by genuineness.
- **Kill conditions:** the six inequalities (SOURCE03:74–75) are exactly x(P) ∈ [−g_m(R−ρ_P), g_m(ρ_P)].

### Lemma CJ

**Case |O| = 1:** J = c(S) + c(O) = c(S).

**Case |O| ≥ 2:**
- b+1 ≤ x ≤ a−2 keeps Y1, Y2 and every third part nonempty. This includes x = b+1, x = a−2, |O| = 2 and wrap-around.
- Pair sums when adding run i:

| Chain | Range of i | m(Q1∪Q2) | Second pair sum | Third pair sum |
|---|---|---|---|---|
| Chain 1 | i ≤ x | m([a,i]) ≥ m(S) | m([i,a−1]) ≥ m([x,a−1]) | R−r_i |
| Chain 2 | i ≥ x+1 | m([i,b]) ≥ m(S) | m([b+1,i]) ≥ m([b+1,x+1]) | R−r_i |

- All are ≥ 2Δ−1, so C2(b) gives c(Y1) ≤ c(S) and c(Y2) ≤ c(S).
- (A′) on Y2 = Y1^c ⊔ S gives c(Y1^c) = 0.
- Hence J = c(Y1) ≤ c(S) ≤ J.

**Checked separately:**
- Empty runs enter only as masses.
- (F2) needs R−r_t ≥ N₊−1 ≥ p−κ+Δ ≥ 2Δ−1, i.e. Δ ≤ p−κ+1. This holds because Δ ≤ κ−1 and 2κ ≤ p+2.
- The clause "m(O) ≥ 2Δ−1" in the definition of admissible is implied when |O| ≥ 2 and unused when |O| = 1.

### Theorem

1. S2 is a linear sub-arc of O(S1). So X = S1 ⊔ G and X^c = S2 ⊔ G′, where the gaps G and G′ may be empty.
2. (A′) and c ≥ 0 give c(X) ≥ J and c(X^c) ≥ J.
3. C1(b) then gives J ≥ 2J. Since J ≥ 0, J = 0 and Σw_t = p.
4. SOURCE02 Sec. 3 yields a proper P with x(P) ∈ I(P), and H0 turns it into an explicit identity 2p-subword.

### Corollaries and containment

**Corollary 2:**
- A minimal heavy S has at most 2Δ−1 nonempty runs (singletons included, since Δ ≥ 1).
- Hence m(O) ≥ p−κ+2−Δ, and this is ≥ 4Δ−3 if and only if p ≥ κ+5Δ−5.
- The x* argument then gives m([b+1, x*+1]) ≥ 2Δ−1. Existence of two such intervals starts from [k]∖{t}.

**Numerical shortcuts:**
- Under (H): p−κ−5Δ+5 ≥ 2κ+7−4Δ, so 4Δ ≤ 2κ+7 suffices.
- Under R ≥ 4κ−4: p−κ−5Δ+5 ≥ 2κ+2−4Δ, so 4Δ ≤ 2κ+2 suffices. This is sharp at R = 4κ−4.
- The cell (13,4,13,3,21) is genuine (R = p, Δ = κ−1, k = p+2κ). There 4Δ = 12 ≤ 15, but p = 13 < 14.
- So the +7 shortcut does not transfer, and the +2 shortcut does.

**Containment:** (D) implies (2HA) for Δ ≥ 1, as stated.

**Remark (3):**
- At (29,7,6) and (31,7,6), N₊ = R, so every nonempty run is a single ρ₁.
- The Codex witness checks: masses 11/11 at x₁ = 21 and x₂ = 1.
- I recounted the 12 triples with p ≤ 43 and the 43 triples with p ≤ 61 by hand.

### Strengthened version: R ≥ 4κ−4 and 2κ ≤ p−1 ("small" means mass ≤ 2κ)

**C2(a):**
- Two small: the sum is exactly R−2κ−⌈T/2⌉, which is ≥ −2 if and only if m1+m2 ≥ 4κ−4−R.
- At R = 4κ−4 with m1 = m2 = 0 the sum is exactly −2, so it passes with zero slack.
- At R = 4κ−5 the sum is −3, which matches the boundary stated in SOURCE01 Sec. 2.
- One small requires R ≥ 4κ+2, and then the sum is ≥ κ.
- Three small: R−3κ ≥ −2, from R ≥ 4κ−4 when κ ≥ 2 and from R ≥ 5 when κ = 1.

**C2(b):**
- Two small sharing m_b: the sum is ⌊(3R+m_b)/2⌋−2κ. It is ≥ p−2 if and only if 3R+m_b ≥ 2p+4κ−4.
  - This follows from R ≥ p and R ≥ 4κ−4.
  - It holds without the 2Δ−1 threshold.
- One small: R−κ−1+⌈s/2⌉ (all parity cases checked).
- Three small: 2R−3κ ≥ p−2 for κ ≥ 2; impossible when κ = 1.

**Increment lemma:**
- Φ(P′) ≤ 2κ by parity, and r_t+δ_t ≤ 2κ−2.
- For Δm = +1, 0, −1 the bounds are (Φ ≤ 4κ, m ≥ 2), (Φ ≤ 4κ−2, m ≥ 1) and (Φ ≤ 4κ−4, m ≥ 1).
- Hence δ_P ≤ 4κ−4−ρ_P and Φ−4m ≤ 4κ−6.

**Case I (κ ≥ 2, since κ = 1 has no defects):**
- U1 and L1: Φ ≤ 4κ ≤ 2p−2.
- L2: follows from R ≥ 3κ−2.
- L3: δ_P ≤ 4κ−4 ≤ R. The equality case ρ_P = 0, δ_P = R = 4κ−4 passes because R is even.
- U2 and U3: by construction.

**Case II (κ ≥ 3):**
- L3: δ_P ≤ 2κ−2 ≤ R−1.
- U1: the left side is ≤ r_y+1 ≤ 2p when W = {y}, and ≤ 3κ−7 otherwise.
- L1: the left side is ≤ 4κ−4 < 2p.
- L2: when W = {y} it needs r_y ≤ R ≤ 2R−4κ+5, i.e. R ≥ 4κ−5; otherwise it needs R ≥ 3κ−1.
- |F| ≥ d/2: follows from k ≥ 2κ+1.

**Edge cells:**
- Under 4κ−4 ≤ R ≤ 2p−1, 2κ ≤ p−1 fails exactly when κ = (p+1)/2 and R ∈ {2p−2, 2p−1}. These cells have k = p+3 or p+2, and Δ ≤ −1.
- Every check survives there except Case I's U1 and L1. These fail only when Φ = 2p+2 together with δ_P = 0 (for U1) or ρ_P = 0 (for L1).
- The exclusion is therefore correct. There are 32 edge cells for p ≤ 61 (two per prime, 16 primes).

**Coverage counts (not premises):**
- The total of 224 equals Σ(p−3)/2 over primes 5 ≤ p ≤ 61, in closed form.
- I spot-checked per-prime totals of 4, 7, 14, 22 at p = 5, 7, 13, 19, with 0, 0, 1, 2 failures respectively.

## Audited / imported boundary

**Audited here, in writing:**
- SOURCE02 Secs. 1–3 under both (H) and (H''').
- SOURCE03:72–113, as used with x_t = w_t.
- All of SOURCE00 Secs. 0–3, plus the arithmetic in Remarks (2)–(3).
- SOURCE01 Secs. 0–2, and the closed-form parts of Sec. 3.
- The algebraic specialisation from the GRX statement to the H0 instance (SOURCE03:28–33).

**Imported, with exact scope:**
1. **Lemma H0, one instance:** B = 0, β = 0, proper P, m ≥ 1, solvable direction only. Here I(P) = [−g_m(R−E), g_m(E)] (SOURCE02:35–37). It is parent-accepted (SOURCE03:25–26). The proof of GRX itself (SOURCE05:22–42) was not re-audited.
2. **P0** (SOURCE04:73–75), which rests on Theorem P (not supplied): e_R ≤ e_F+2κ, with empty runs counted as even. It is used only in the form n_E ≤ 2κ.
3. **Definition of RES_<(p)** (from RED, not supplied): used only for SOURCE00:26–27. B0S itself appears only in the containment remarks.

**Not claimed or still open:**
- R ≤ 4κ−5.
- The edge cells.
- Δ ≥ 2 words without (2HA): every word at (29,7,6), and some words at (13,4,13,3,21).
- B ≥ 1 with k ≥ p+1.
- General REFL, INV*(p), ordered Olson, and novelty.

The finite aids (SOURCE02:124–128; SOURCE01:89–94) and the parameter transcripts (SOURCE00:110; SOURCE01:104) can be deleted without affecting any proof, once MINOR-1's written argument replaces the transcript.
