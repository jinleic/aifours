# Hostile referee report: Olson delta package

All results below were re-derived by hand. I used no tools and no computation. Every delta file was treated as untrusted. I accepted a cross-import between delta files only after re-checking the proof it cites:
- LS-II′ is used by LS-small and LS-lin.
- Lemma CT and the greedy step (C) of LS+2 are used by CTgen and LS-lin.
- The corrected AP′ in erratum-1-delta is used by LS-small.

**Bottom line: there is no FATAL and no MAJOR finding in any of the six claims.** Every theorem statement holds at its stated scope. The repairs are MINOR: wording, explicit hypothesis checks, citations, and two scope remarks in LS-lin.

| # | File | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|---|
| 1 | addendum-1 (LS-II′) | ACCEPT-WITH-FIXES | 0/0/3 |
| 2 | LS-small v1 + erratum-1-delta | ACCEPT-WITH-FIXES (erratum D1, D2: ACCEPT) | 0/0/4 |
| 3 | BASE1 v1 | ACCEPT-WITH-FIXES | 0/0/3 |
| 4 | LS+2 v1 | ACCEPT-WITH-FIXES | 0/0/3 |
| 5 | LS-lin v1 | ACCEPT-WITH-FIXES | 0/0/4 |
| 6 | CTgen v1 | ACCEPT | 0/0/1 (editorial) |
| — | credit addendum | no mathematical content; context only | — |

## (1) LS-II′: proof-LS-caseII-v2-addendum-1.md

**Checks (all pass):**
- **Steps 1–4 of v2 are free of H′ and SH.** They use only CF (F), the case (II) data and Lemma AP.
  - Step 1 under R6: t runs over the K+1 residues of [δ0−s, v1] ⊂ [1, p−2]; δ0−s ≥ 1 because s ≤ δ0−1. So the e-term progression lies in an arc of size 2e−2 = 2n with n = e−1, and 3n < p. Hence μ1 = ±1.
  - Step 2: W = 1^{e−1} gives 3e−3 ≥ δ0, so μ1 ≠ 1.
  - Step 3: v1 ≤ p−e; (R) holds; every negative term has c′ = 2ν−1 ∈ [3, 2e−5].
  - Step 4: the first bad prefix has sum in (0, δ0), which falls in the gap of (R).
- **(a)** g(−g) is a zero-sum. Removing it from a T of length 2p+2 would leave a zero-sum of length 2p, which is in the window. So every T containing both has length ≥ 2p+4, and the result stays long. A T1 without g lies in (−g)^{v1}R′, of length ≤ r ≤ p−2.
- **(b)** c′ is odd, so each step c′+1 is even and ≤ 2e−4. The new length is ≥ 2p+2−(2e−4) = 2κ+6 > 2κ+2. It is therefore in the window (excluded) or ≥ 2p+2. The process terminates because length decreases.
- **(c)** a′ ≥ 2p+2−s ≥ 2p−e+4 > 2e−5 ≥ c′, so no negative term survives. Then |W2| ≥ |T2|−M ≥ δ0+2, against Step 4's |W2| ≤ (δ0−1)/3.
- **Edge cases:** e = 2 gives R′ = ∅. e = 3 has no negatives because [3, 2e−5] is empty. p = 7 has 3e = p−1.

**MINOR findings:**
- **m1.1 (b), wording.** "e consecutive even values … cannot land below without landing in it" is not the operative reason. Replace it with the direct bound L−(c′+1) ≥ 2κ+6.
- **m1.2 (c), citation.** The bound s ≤ e−2 is the (II) clause of the accepted dichotomy (verdict item 6), so it is legitimate. However, erratum-2 R8's note that it is "not used" is now stale.
  - Either cite the dichotomy clause,
  - or use s ≤ δ0−1 ≤ 2e−4 instead, which gives a′ ≥ 2p−2e+6 > 2e−5.
- **m1.3 Statement.** Write "case (II) w.r.t. g = g0 of DGM-p". Also state that "LS-counterexample" means an odd Y with |Y| = p+2κ+1, (ZP_κ) and a long zero-sum.

**Observation (optional, no change required).** Step 3, Step 4 and parts (b)–(c) are dispensable. After (a):
- a T1 without −g lies in g^M R′, of length ≤ M+s ≤ (2p−δ0)+(δ0−1) = 2p−1;
- a T1 without g has length ≤ r.

So Steps 1–2 plus (a) already prove LS-II′. This is the unconditional analogue of Codex's R8 alternative.

**Scope:** p ≥ 7 prime and κ0+1 ≤ κ ≤ p−2. A threshold LS-counterexample with g = g0 is not in case (II).

**Import closure:**
- Imports: CF(a)(b) [V1], DGM-p [V5], ROW plus the LS-threshold dichotomy [V6], AP with R6 [V8], and v2 Steps 1–4 (re-checked).
- Not used: H′, SH, S1-sharp, RED,

index-one.
- **Consequence (with RED):** every threshold counterexample lies in case (I), i.e. δ0 ≤ e−2 and all U-multiplicities are ≤ p−2e+1. This is not LS.

## (2) LS-small: proof-LS-caseI-smalldelta-v1.md + erratum-1-delta-APprime.md

**Checks (all pass):**
- **(A)** ρ ≥ 1 gives |W|+2ρ ≥ 3 ≥ δ0. ρ = 0 gives |W| ≥ 2, since μ ≢ 0. The upper bound is r+2e−2 = p+δ0−1 ≤ 2p.
- **(B)**
  - r ≥ (p+1)/2 is equivalent to 4e ≤ p+1+2δ0.
  - σ(U) ≢ 0 because U is zero-sum-free.
  - Minimality, including the complement case: a proper zero-sum containing −σ(U) has a nonempty zero-sum complement inside U.
  - The length r+1 ≥ (p+3)/2 = ⌊p/2⌋+2, with n = p ≥ 3 and ord(a) = p.
  - The coefficient of −σ(U) is ≥ 1, so S ≤ p−1.
- **(C)** f(k) = −k²+(r+1)k+r is concave with f(1) = f(r) = 2r ≥ p+1.
- **(D)**
  - The points ρa⁻¹ (ρ = 1..e−1) avoid [1, S], so they lie in [S+1, p−1], an arc of size ≤ 2e−2−δ0 ≤ 2n+1 with n = e−2.
  - AP′ is valid under the D1 proof:
    - (i) d ≥ l gives an empty intersection.
    - (ii) both summands are < 2l−p ≤ 4n+2−p < n.
    - (iii) d ≤ n+1.
    - Lifting: the next point lies in [α−n−1, α+3n+1]. L+p is excluded by p > 3n+1 and L−p by l+n < p. Then nd ≤ 2n, so d ≤ 2.
  - Exclusions: a⁻¹ ∈ {1, 2} would put ρ = 1 inside [1, S]. a⁻¹ = −2 needs S ≤ p−2e+1 < r ≤ S.
- **(E)** |W\*| ≥ 3, so s\* ∈ [1, p−1]. Then j ≡ s\* forces j ≥ s\*, so |W\*| ≥ δ0+2s\* > s\* ≥ |W\*|, a contradiction.
- **Corollary.** κ0+1 ≤ p−e is equivalent to p ≥ 3e+1, since 3e is not prime. The resulting ranges are exact:
  - e = 2: p ≥ 7. Case (I) is empty here because it needs δ0 ≤ 0.
  - e = 3: p ≥ 11, with δ0 = 1 and 12 ≤ p+3.
  - e = 4: p ≥ 13, with δ0 ≤ 2 and 16 ≤ p+1+2δ0.

**MINOR findings:**
- **m2.1 (D).** State AP′'s hypotheses in the text: n = e−2 ≥ 1, and 3n+2 = 3e−4 < p from 3e ≤ p−1. Note also that l = 0 is covered by case (i).
- **m2.2 (D).** The exclusion of a⁻¹ ∈ {1, 2} needs S ≥ 2. This holds because S ≥ r ≥ 4; say so.
- **m2.3 Dependencies.** Cite the following:
  - the parent verdict ca6e4ca7;
  - erratum-2, which is mandatory: R4 for (L), and R6 through LS-II′ Step 1;
  - D1 for AP′. The original AP′ case (ii) "n ≤ 2l−p" and its terse lifting are superseded by D1.
- **m2.4 Scope remark.** "p−κ ≥ 5 open" is superseded by LS-lin and BASE1+. This is editorial.

**Erratum-1-delta:** D1 and D2 are both ACCEPT.

**Scope:**
- Prop I-small holds exactly as stated.
- LS(p, p−2) holds for every prime p ≥ 7.
- LS(p, p−3) holds for every prime p ≥ 11.
- LS(p, p−4) holds for every prime p ≥ 13.

**Import closure:** RED, CF, DGM-p, the dichotomy, index-one (n = p), LS-II′ (accepted in (1)) and AP′ via D1.

## (3) BASE1: proof-STAB-base-p1mod3-v1.md

**Parameters** (p ≡ 1 mod 6):
- κ = c = (2p+1)/3, odd
- δ = (p+2)/3, odd and ≥ 3
- l = (2p+4)/3, even
- D = 2δ−2 (equality)
- base = 2
- m ≥ p+1

**Checks (all pass):**
- **S1–S3.** S3 applies accepted S1-sharp at κ0, the top of its lower range with no length bound, to T itself.
- **S4.** Index-one applies with n = 2p and |Q| ≥ p+2. Orders 1 and p would give even terms. Order 2 would force |Q| ≤ 2.
- **S5 (MC).** Exactly the two pairs (Q, ∅) and (∅, Q′) are excluded.
- **S6.** Valid at these values:
  - m ≥ p+1 ≥ D+2, and l ≥ 6.
  - b0 ≤ m because 3−|S_Q| ≤ 2δ.
  - |Z0| = 1 uses D = 2δ−2 and gives |S_Q| ≤ 0, a contradiction.
  - |Z0| ≥ 2 gives m ≤ (p+3δ)/2 − 3, a contradiction.
- **S7.** The argument ends at l ≤ D, but here l = D+2. Also r ≤ D < m, s ≤ D+1 < m, and A_W ≤ 2p+D < 4p.
- **S8.** Generic; no value-specific input.
- **S9′.**
  - X = t′−2 ≥ 0, so t′ ≥ 2.
  - |R_high| ≤ 1 would give l ≤ b_min ≤ (2p+1)/3 < l, so |R_high| ≥ 2.
  - t′ odd would give X ≥ t′−1, so t′ is even.
  - t′ = 2 gives R = (3g)^{(2p−2)/3}.
  - t′ ≥ 4 forces two highs equal to (t′+1)g and every low term equal to 3g. Then (8c) and b_min ≤ c give t′ = (2p−2)/3, n3 = 0 and b_min = c.
- **S10.**
  - Case 1: k ≤ (2p+1)/9 and i ≤ t′, so W ⊆ Q′. MC gives i+k ≤ 1, so b = 3 and Y = E2.
  - Case 2: every term of S_Q has mass ≥ c−1, which equals mass(S_Q), so S_Q = {cg} and Y = E3.
- **Corollary.**
  - SLZ3 is used only to bound |T|.
  - E2·g: M = p+4 and W = 1^{e−1}; at δ0 = p−4 this is forbidden.
  - E2·y: W = 1^{p+ρ−μ}{μ}; both branches satisfy ≥ p−3 and ≤ 2p.
  - E3·g gives g^{2p}.
  - E3·y is handled by the ν-window argument.
- **Endpoints p = 7 and p = 13** are consistent (15 ≡ 1 mod 14, 27 ≡ 1 mod 26).

**MINOR findings:**
- **m3.1 (Cor., E3 bullet).** The parenthetical only covers the top end of the window. Add: "if ν_y = 1 the window contains 4 ∈ Φ (p ≥ 7); if ν_y ≥ 2 it does not contain 1".
- **m3.2 (S6/S7).** Replace "all hold here" with the explicit numeric checks: m ≥ D+2, l ≥ 2, D = 2δ−2, and l = D+2.
- **m3.3 (Sec. 0 sharpness).** This statement is unused by the proof. Either cite F1 via the S1-sharp verdict and F2 via erratum 1, or give the two-line CF check:
  - E2: 3w ≤ p−4 < δ0 = p−3.
  - E3: the ν-sums are 1, 2, 3, none of which is in Φ.

**Scope:** exactly p ≡ 1 (mod 3) prime ≥ 7 and κ = (2p+1)/3.
- The Theorem is STAB(p, κ) in the R3 wording.
- The Corollary is LS+(p, κ), which implies LS(p, κ).

**Import closure:** S1-sharp at κ0, index-one (n = 2p), SLZ3 (|T| only) and CF. The steps S5–S8 are re-derived here, not imported. The first p ≡ 2 (mod 3) cell is not covered.

## (4) LS+2: proof-LSplus-e2-v1.md

**Checks (all pass):**
- **Lemma CT.**
  - An S with σ_p(S) = σ_p(Y) makes Y−S a zero-sum with even length in the window; it is nonempty.
  - RS(a) then gives T−n+1 ≤ p−1.
- **Step 0.**
  - SLZ3 needs ⌊2p/3⌋+1 ≤ p−2, i.e. p ≥ 7. It gives |T| ≤ 3p−5.
  - Cut Y to length 3p−4.
- **Step 1.** The excess Σ max(0, v_x−(p−2)) is ≥ p, and the case split is exhaustive.
- **Step 2.**
  - {v0, v1} = {p−1, 2p−3}.
  - j0 ≥ 1 would give a zero-sum of length 2p−2.
  - So α = 0. Then j = 0, and i is even with i ≤ 2p−4.
- **Step 3.**
  - The involution is excluded by its (2p−2)-fold power.
  - (A) holds.
  - (B) length ≥ p−2 ≥ (p+3)/2.
  - (C) 2r ≥ 2p−6 ≥ p+1.
  - (D) a⁻¹ ∈ {−1, −2}.
  - (E):
    - a = −1 gives 2p−s.
    - a = −1/2 gives ≤ 2p for even s and ≤ p for odd s.
- **Sec. 4** checks out, including the M ≤ 2p−1 condition.
- **p = 7** is tight in (B) and in (C).

**MINOR findings:**
- **m4.1 Dependencies.** RS(a) is now parent-accepted (verdict ca6e4ca7 item 4; any prime, 1 ≤ n ≤ |S|). Replace the "model review" citation, and read CF through erratum-2 R4.
- **m4.2 Step 0.** Cite SLZ3's lower range (p ≥ 7) as well.
- **m4.3 Steps 1 and 3(B).** State that the excess > 0 forces some v ≥ p−1, and that the −σ(U) coefficient ≥ 1 gives S ≤ p−1.

**Scope:** LS+(p, p−2), and hence LS(p, p−2), for every prime p ≥ 7. Lemma CT holds at its stated scope. STAB(p, p−2) is not claimed.

**Import closure:** RS(a), CF, SLZ3 (|T| only) and index-one (n = p).

## (5) LS-lin: proof-LS-lin-v1.md

**Checks (all pass):**
- **Step 1** goes through via LS-II′ and dichotomy (I).
- **Step 2.** (F\*) holds.
- **Step 3.** The core construction holds:
  - |Z0| ≤ e−3.
  - U′ is zero-sum-free by maximality.
  - (F′) holds via W′ ∪ Z0.
- **Step 4.**
  - The index-one length condition is equivalent to p ≥ 4e−3.
  - δ′+E′ ≤ 2e−2.
  - |V| ≥ s−E′.
  - The greedy argument applies.
- **Step 5.**
  - All signed representatives lie in [−(2e−3), 2e−5], so every difference lies in [−(6e−11), 6e−13]. Since p ≥ 6e−10, each difference is 0.
  - At ρ = e−1 the positive range is empty, so x̃ < 0. Then (e−1)|x̃| ≤ 2e−3 gives a = −1.
  - It follows that δ′+E′ ≤ e−1.
- **Step 6.**
  - Every positive z̃ is ≤ 2e−6.
  - (6a) The first crossing is ≤ 3e−8, the residual is in [0, 2e−7], and the count gives ≥ e+1 > δ0.
  - (6b) The first crossing is ≥ −(4e−6), and |W| ≥ p−5e+9 ≥ δ0, which is equivalent to p ≥ 6e−11.
- **Step 7.**
  - ρ = 0 is excluded.
  - σ̃ ≥ 0 gives a bound ≤ 3e−7.
  - σ̃ ≤ −1 forces Z″ to violate (F\*).
- **Z0 ≠ ∅ is possible only for e ≥ 5:** a nonempty Z0 needs ≥ 2 terms, and |Z0| ≤ δ0−1. The cases e = 3 (p = 11), e = 4 (p = 17) and e = 5 (p = 23) all pass.

**MINOR findings:**
- **m5.1 Sec. 0 combination.** As written, it literally includes κ = p−1 (outside LS's scope) and cells with κ ≤ κ0. Restrict it to "prime p ≥ 7, κ0+1 ≤ κ ≤ p−2, p−κ ≤ (p+10)/6". This is an unscoped statement, not a false one.
- **m5.2 Sec. 2 "exactly open" is inaccurate.**
  - BASE1+ covers LS at κ = (2p+1)/3 for p ≡ 1 (mod 3), because LS+ ⇒ LS.
  - Its e = (p−1)/3 lies inside the claimed open band for every such p ≥ 19, e.g. (19, 13), (31, 21), (37, 25).
  - Repair: add "except the BASE1 cells".
- **m5.3 Step 4.** Spell out four facts: U′ ≠ ∅, σ(U′) ≢ 0, minimality via the complement, and S′ ≤ p−1.
- **m5.4 (6a)/(6b).** "Integer sum" means the signed-representative sum; the μ-sum is only congruent to it. Reword.

**Scope:** LS(p, κ) for κ0+1 ≤ κ ≤ p−2, e ≥ 3 and p ≥ 6e−10. Note that e = 4 needs p ≥ 17; the cell (13, 9) comes from LS-small.

**Import closure:** RED, CF, DGM-p, ROW plus the dichotomy, LS-II′ (accepted in (1)), index-one (n = p) and the LS+2 greedy step (re-checked).

## (6) CTgen: lemma-CTgen-v1.md

**Verdict: ACCEPT.**

**Checks (all pass):**
- **Counts.**
  - n = N−2κ−2 ≥ 1.
  - N−n = 2κ+2 is even and lies in the window.
  - Σ min(n, v_x) ≤ p+n−2 < N, which is equivalent to κ > (p−4)/2.
- **Involution step.**
  - |W| ≤ N−v_p ≤ 2κ+1 < 2p, where W is the non-p part of T.
  - |T| is even, and |T|−2p ∈ [2, m].
  - Deleting an even number of copies of p leaves a zero-sum of length exactly 2p, which (ZP_κ) excludes.
- **At N = 3κ+2:** v_g ≥ κ+1 > p−e.
- **R12 hypotheses hold:** r+2e−2 ≤ 2p and K = p−3e+2 ≥ 3. This supplies a hypothesis; it is not an LS+ step.

**MINOR finding:**
- **m6.1 (editorial).** Say that |T| is even, and rename W to avoid clashing with CF's notation.

**Scope:** p ≥ 5, (p−3)/2 ≤ κ ≤ p−1, N ≥ 2κ+3.

**Import closure:** Lemma CT (accepted in (4)), which rests on RS(a).

## Credit addendum

None of its [INFERENCE] items is a premise of anything accepted above. Its inferred "LS(p, p−2) for p ≥ 5" reaches p = 5, where κ = 3 = κ0; that cell belongs to S1-sharp, not to the delta package. No novelty assessment was made.

## Cross-cutting audit

- **Occurrence semantics.** Every extraction stays within the available counts:
  - g^{c′} with c′ ≤ a′;
  - x0^i x1^j with i ≤ v0 and j ≤ v1;
  - g^i(3g)^k ⊆ Q′;
  - 1^{p+ρ−μ} with exponent ≤ p−1 (when μ = 1, the new copy supplies the p-th 1);
  - deleting copies of p up to m.
- **Representatives and wrap-around.** These were checked in four places:
  - CF μ ∈ [1, p−1];
  - least coefficients in [1, 2p−1];
  - the lifting in AP (R6) and AP′ (D1);
  - LS-lin's no-wrap condition p > 6e−11.
- **Parity.** These were checked in four places:
  - the even steps in LS-II′ (b);
  - the parity of t′ in S9′;
  - the even i in LS+2 Step 2;
  - the even deletion in CTgen.
- **κ0 floors.**
  - p ≡ 1 (mod 3): κ0+1 = (2p+1)/3 and e_max = (p−1)/3.
  - p ≡ 2 (mod 3): κ0+1 = (2p+2)/3 and e_max = (p−2)/3.
  - In both cases 3e ≤ p−1, which is what AP, AP′ and LS-II′ use.
- **Endpoints:**
  - p = 7, κ = 5: LS, LS+ and STAB all hold.
  - p = 11:
    - κ = 8 (e = 3): LS holds; LS+ is open.
    - κ = 9: LS and LS+ hold.
  - p = 13:
    - κ = 9: LS (LS-small), LS+ and STAB (BASE1) hold.
    - κ = 10: LS only.
    - κ = 11: LS and LS+ hold.
- **Import literals.**

  | Import | How its literal hypothesis is met |
  |---|---|
  | Index-one | Length ≥ ⌊n/2⌋+2 was verified in each of the four uses. |
  | SLZ3 | Used for |T| only, and its range was checked. |
  | S1-sharp | Applied at κ0 only. |
  | RED | Range 0 ≤ κ ≤ p−2. |
  | CF | M ≤ 2p−1 was checked before each use of (F). |
  | DGM-p | Range (p−3)/2 ≤ κ. |
  | Dichotomy | Threshold length with g = g0. |
  | RS(a) | 1 ≤ n ≤ |S|. |
  | EGZ | Not used. |

## Exactly proved cells

Sequence level only, relative to the imports above:
- **LS(p, κ)** for κ0+1 ≤ κ ≤ p−2 in three families:
  - every cell with e ≤ 4;
  - every cell with e ≤ (p+10)/6;
  - κ = (2p+1)/3 when p ≡ 1 (mod 3).
  - The smallest open cells are (17, 12), (19, 14), (23, 16) and (23, 17).
- **LS+(p, κ)** at κ = p−2 for every prime p ≥ 7, and at κ = (2p+1)/3 for every prime p ≡ 1 (mod 3), p ≥ 7.
- **STAB(p, (2p+1)/3)** for every prime p ≡ 1 (mod 3), p ≥ 7.
- **Structural results:** LS-II′, Prop I-small, Lemma CT and CTgen.

## Not concluded

- Full LS.
- LS+ outside the two families above.
- STAB outside the BASE1 cells, because TR is open.
- INV\*.
- Ordered Olson.
