# UPAR2 v1: independent hostile written review (no tools used)

**Governing order.** I applied the navigation erratum v1 first and again last. Its two relocations are correct: bindings are in Sec.7, not Sec.8 (LF7), and R2/JUMP-COVER are in Sec.6, not Sec.7 (LF24/LF27). The remaining cross-references are correct (LF191 "Sec.0", LF209 "Sec.3"). The proof text is unchanged.

**Evidence rules.** Premises are only the accepted UMR/UPAR/UFC statements at their literal scopes, plus their errata and the cutoff binding. Hashes, statuses, the source-binding JSON, checkpoint counts and the Codex 0F/0M/1m count were treated as metadata only. Every step below was re-derived by hand from the pasted literal text.

## Counts

| Category | FATAL | MAJOR | MINOR |
|---|---|---|---|
| Proof (including the R2 residual) | 0 | 0 | 2 |
| Import / binding | 0 | 0 | 1 |
| Scope | 0 | 0 | 0 |
| Process | 0 | 0 | 1 |

- **No lemma fails.**
- **UPAR2-P (T2) holds**, conditional on the accepted premises.
- **UPAR2-R holds** as a one-way necessary relaxation.
- **JUMP-COVER remains the first unproved step.** Its full retained target is in §8.

## 1. Literal base

- **Window (W)**, from UMR LF161–165:
  - up = −2−ν0+x.
  - low = Π0+2−y−2p, with Π0 = B*−ν0 = R+e−ν and R−2p = −2d.
  - So low = e−2d+2−ν−y, which is exactly LF52.
- **Upper-type endpoints:**
  - On Q_r: M_r−q′ ≤ δ−R < 0 and ℓ_r−q ≥ 2 > ε, so x = ℓ_r−q.
  - On P_r: symmetrically, x = M_r−q′.
  - On G_r: x ≤ 1.
  - These give LF63 exactly.
- **Parity and cost.** UMR LF202 gives θ_i ≡ σ_i. Odd labels (LF88/101) give σ_i ≡ |L_i|. LF203 makes empty θ nonzero even. Together these give (Cost).
- **Identity.** UMR LF256–258 with h−κ = d gives Σ = e.
- **Balanced data.** floor((p+7)/4) = j+1, so κ ≥ j+2 and j ≥ d+2+ε. ℓ_j and M_j are as stated.

## 2. Lemma 1 (global P+ elimination): correct on all of T, both ε, every frame

Setup:
- B = S∖J_j, so |B| = h−j = j−ε.
- B lies below t_j = 1, so every empty run in B has a nonzero even θ ≤ 1, hence θ ≤ −2.
- The cap needs a ≤ δ+1. This holds because a ≤ L, and δ+1−L = 3j−2d−2ε+3 > 0.

Counting:
- **S:** the cap gives E(B) ≤ d+c−1, so l(B) ≥ j−ε−d−c+1.
- **S′:** the cap bounds negative empties by d+c−1. Since t_j(S′) ≤ −1, positive empties occupy ranks ≤ j−1. Also n(S′) ≤ λ. So λ ≥ j−ε−d−c+2.
- **Combine with (PB):** l(B)+λ ≤ a+z ≤ ν+z ≤ L = j−2d−2. This gives j−2ε+5 ≤ 2c ≤ a+2 ≤ j−2d−z, i.e. 2d+z+5 ≤ 2ε. That is impossible for d ≥ 2.

The contradiction survives with the tighter bound a+z as well (it gives 2d+5 ≤ 2ε). There is no unit-label, frame-selection or parameter cutoff.

**This lemma is load-bearing inside T2.** Take (81,181): d = 10, ε = 1, κ = 8d+1, p prime. UPAR's own threshold κ ≥ 7d+16−5ε = 81 does not exclude P+ there. Lemma 1 does.

## 3. Defect identity: exact, and (ID) is genuinely used inside

K, Q, X, Y partition the runs, so their letter sets partition the R letters.

**Letter algebra:**
- α′(K) = β(Q)+|A^c∩L(X∪Y)|.
- α(Q) = β′(K)+|A∩L(X∪Y)|.
- Hence zP+zQ = 2W+l(X)+l(Y).

**Sum via (ID):**
- e = Θ(K)+Θ(X)+Θ(Q)+Θ(Y)+2ν+2d.
- Substitute the definitions of sP, sQ and C, using |X|+|Y| = 2h−2r−1 and h = κ+d.
- Result: e = (4r−2κ−4d+2)−2W−sP−sQ−C, i.e. F−e = 2W+sP+sQ+C.

**Nonnegativity of each term:**
- sP: the P_(r+1) endpoint is 2(r+1)−2d−2−ν−zP.
- sQ: the Q_r endpoint.
- C: (Cost) applies because every θ in X is ≤ θ_u ≤ −1 (UPAR LF270) and every θ in Y is ≤ t_r(S′) ≤ −1 (UPAR LF77–78, since 2r > κ).

## 4. Lemmas 2 and 3: correct; the predecessor deficits are the right ones

**Lemma 2.**
- 2r−3n ≤ Θ ≤ 2κ−2r−ν−q, so 3n ≥ 2b+ν+q.
- n ≤ l = a+q−2α ≤ ν+q.
- Therefore n ≥ b.

**Lemma 3(a)** uses QQ-mixed at level r with the predecessor deficits z0+zQ, not zP+zQ.
- Lemma 2 applies to whichever predecessor has threshold −1, so both orientations are covered.
- e ≤ κ−r−d−b = (κ−3b−2d)/2, so κ ≥ 3b+2d+2e.

**Lemma 3(b):**
- QQ-1 gives e+ν+E ≤ κ−3b.
- For Q: 2r−3(a−zQ+2w) ≤ 2κ−2r−ν−zQ−sQ. Using ν ≥ a and zQ ≥ w, this gives a+w ≥ b+sQ/2.
- (Defect) gives 2w+sQ ≤ F−e.
- So a ≥ 2d−1+e/2+sQ, and therefore κ ≥ 3b+2d−1+3e/2.

## 5. Zero exits (F = 0): correct

**(Z) consequences.**
- F = 0 forces e = W = sP = sQ = C = 0. Unit labels and ν = a are therefore derived, not assumed.
- W = 0 makes K (and I) pure A^c and Q pure A.
- C = 0 forces θ = |L_i|−2 on every tail run, so tails are empty runs with θ = −2 or singletons with θ = −1.
- With 2r−A0 = 4d−2 = 2b:
  - zP ≥ z0+b, or z0+b+1 if I is strong.
  - β(I) ≥ a+b when I has threshold −1.
  - a ≥ b+2zQ when Q has threshold −1.
- |X| = (κ−1)/2 and |Y| = (κ+1)/2.

**Lemma 4 (arbitrary independent singleton extension).**
- Q∪{v} ⊂ S′ is an independent, non-top set of central size r+1, so (W) applies.
- At that level ℓ = A0 and M = κ+1, with q = zQ+1.
- Under zQ ≤ (κ−8d+3)/4: the entry A0−zQ−1 is ≥ 3(κ−1)/4 > 1, and the entry zQ−3κ−2d+4 is ≤ (−11κ−16d+19)/4 < 0.
- So the upper bound is A0−a−zQ−3, which is 2 below the actual sum.

**Lemma 5, both orientations.** With E dropped and e = 0, C0 = (κ−4d+1)/2.
- **I strong, Q at −1:**
  - zQ ≤ (κ−8d+3)/6, which is ≤ the Lemma 4 bound (or already impossible).
  - X is all empty, since θ ≤ θ_u ≤ −2 and slack is zero.
  - zP = α′(K) ≥ z0+b+1 ≥ 1, so some A^c letter lies outside K.
  - That letter cannot be in Q or X, so it must be in Y. This contradicts Lemma 4.
- **I at −1, Q strong:**
  - a ≤ (κ−8d+3)/4, which is ≤ δ+1 (the gap is (7κ+1)/4).
  - Y consists of (κ+1)/2 negative empty runs.
  - The cap then gives κ+1 ≤ 2d+a ≤ (κ+3)/4, which is impossible.

**Lemma 6 (both predecessors at −1).**
- zP ≥ z0+b ≥ 2a+2b ≥ 4b+4zQ = 8d−4+4zQ.
- zP ≤ M_(r+1)−2 = κ−1, so zQ ≤ (κ−8d+3)/4, so β(Y) = 0 by Lemma 4.
- Then zP = |A^c∩L(X)| ≤ |X| = (κ−1)/2.
- Therefore κ ≥ 16d−7+8zQ.

## 6. T2 assembly, parity rounding, containment, the seven cells

**F = 0** forces κ odd and κ ≥ 16d−7, which exceeds 8d+1 for d ≥ 2. Lemma 3 alone would only give κ ≥ 8d−4 or 8d−3 here. So odd κ ∈ {8d−3, 8d−1, 8d+1} depend on Lemmas 4–6; among the named cells, these are (13,29) at r = 8 and (17,37) at r = 10.

**F > 0** gives b ≥ 2d with b ≡ κ (mod 2).

| κ parity | b bound | Both predecessors −1 | Mixed predecessors | T2 contradiction |
|---|---|---|---|---|
| even | b ≥ 2d | κ ≥ 8d−1, rounded to ≥ 8d | κ ≥ 8d | contradicts κ ≤ 8d−2 |
| odd | b ≥ 2d+1 | κ ≥ 8d+2, rounded to ≥ 8d+3 | κ ≥ 8d+3 | contradicts κ ≤ 8d+1 |

**Equivalences.** κ ≤ 8d−2 ⟺ 9κ ≤ 4p+2, and κ ≤ 8d+1 ⟺ 9κ ≤ 4p+5. Both correct.

**Containment of old T_PAR.**
- κ ≤ 4d implies κ ≤ 8d−2.
- (10,23): d = 2, 10 ≤ 14.
- (13,31): d = 3, 13 ≤ 25.
- Strictness: (16,37) has d = 3 and 16 ≤ 22 but 16 > 12 = 4d. All seven named cells lie in T2∖T_PAR.

**The seven named cells** (each checked by hand for membership in T, d, the cutoff, length 4p−2, D_2p and k = p+1):

| (κ,p) | d | κ parity | T2 cutoff | Holds |
|---|---|---|---|---|
| (13,29) | 2 | odd | 17 | yes |
| (14,31) | 2 | even | 14 | yes |
| (17,37) | 2 | odd | 17 | yes |
| (16,37) | 3 | even | 22 | yes |
| (17,41) | 4 | odd | 33 | yes |
| (18,43) | 4 | even | 30 | yes |
| (20,47) | 4 | even | 30 | yes |

## 7. Findings, with exact lines

**Proof MINOR-1** — `proof-UPAR2-v1.md:154`
- The text says "Q's negative threshold makes every Y theta<=-2". A merely negative threshold gives only θ ≤ −1.
- The step needs the strong threshold t_r(S′) ≤ −2 fixed at LF152 ("Q strong"). With that reading the step is valid.
- Wording only.

**Proof MINOR-2** — notation collisions inside the R2 definition
- R2(1) (LF198–202) keeps the literal R_PAR text, where (CM)/(DM) use b = h−|Q| (UPAR LF216) and ENV uses C(S) (UPAR LF225).
- LF209 then defines b = 2r−κ and C = tail slack "exactly as in Sec.3".
- UFC's bottom sets K_r and F_r coexist with UPAR2's K = J_(r+1)(S) and defect F.
- Lemma labels also collide:
  - LF116 "(Lemma2)" (the new count) versus LF68 "(UPAR Lemma2)" (the cap).
  - LF214 "(Lemma5)" (zero exit) versus "Lemma5" in UPAR verdict LF9 / erratum item 3 (QQ-1/QQ-mixed). Both appear within R2.
- No test is wrong, but anyone instantiating R2 must disambiguate. A renaming erratum is advisable.

**Import MINOR-1** — Sec.7 table versus the pins and the packet
- LF244 lists the UPAR primary as 66-122, 146-155, 216-275. The packet also contains UPAR 18-29, 35-64 and 157-175; the package acknowledges only 35-64 and 157-175.
- LF245 gives the UMR verdict as 1-26, but authority LF33–37 and scope LF36 pin 1-38.
- LF249 gives the UFC verdict as 5-14, but authority LF51–55 and scope LF43 pin 1-36. Lines 1–4, which in sibling verdicts carry the status line, are absent.
- UFC erratum LF3 names a co-governing "fixed-parameter finiteness clarification" (9b02608f…) that is not in the packet.
- Every statement UPAR2 actually uses is pasted literally:
  - frame and labels: UMR 49-56, 88-118
  - Θ = U′ and centrality: UMR 18-28, 238-239, 252-253, with erratum v1
  - windows: UMR 64-68, 137-139, 161-165
  - parity: UMR 201-209
  - identity: UMR 252-258
  - UB / Lemma 20 including the 320–321 boundary: UMR 266-274, 300-302, 315-324
  - cap, PB, QQ and LJ: UPAR 102-122, 146-155, 266-273
  - UFC cutoffs (+5/+7): UFC 23-27, verdict LF7, binding LF5
  - E0 and ENV: UFC 200-225
- So this finding is non-load-bearing. The omitted lines simply cannot be confirmed free of further qualifications.

**Process MINOR-1** — "independently derived" after exposure
- Locations: LF257–258 ("The stronger bounds here were independently derived") and cp-01 LF9 ("Independently derived predecessor bounds … kappa<=6d-4").
- cp-01 LF4 records that the unaccepted reviewer note LF1–210 was read first. The 6d−4 route is that note's own lead (authority LF103).
- The accurate wording is "re-derived after exposure". The note body is not pasted, so overlap beyond the three-lead preview cannot be assessed.
- No novelty claim is made and all steps are re-derived here, so this is non-load-bearing.

**Uncounted qualifications**
- **Lemma 2's "stronger" label** (LF110, package LF22). n ≥ b follows from UPAR's own 3n ≥ 4r−2κ+ν+q (LF151/153) combined with n ≤ ν+q. It is stronger only than a parameter-only weakening, not than UPAR's count.
- **LF100's tail-negativity claim** omits its inherited justification. The justification is valid (§3).
- **Derivation order.** The core results in cp-01/cp-02 were derived before the literal primary ranges were read (cp-02 LF20, then cp-03 LF15). This is consistent with scope LF77, and the final text matches the literal sources.
- **Addendum route.** The (13,29), r = 8 route it discloses (zP ≥ z0+3 plus singleton extension) is exactly the d = 2, b = 3 instance of (Z) and Lemmas 4–6. It is disclosed, and no preregistration is required.
- **Checkpoint gaps.** Recomputed as 511, 1128, 212, 402, 1048, 311 and 424 s, all under 1200 s. These are records only.

**Scope.** No overclaim found. Full T, other k, full ordered Olson, existence/converse, novelty, human review, Lean and runtime are all explicitly excluded.

## 8. Failing lemmas and the full retained target

No UPAR2 lemma fails. **JUMP-COVER** is unproved and is equivalent to nonexistence on T∖T2. It is not a proved reduction in difficulty.

**Parameter range.** T∖T2 = {even κ with 9κ ≥ 4p+4} ∪ {odd κ with 9κ ≥ 4p+7}, for both p ≡ 1 and p ≡ 3 (mod 4), unbounded.

**Retained data.**
- **All R_PAR baseline tests:**
  - labels and partition, all-run parity, |θ| < 2p, max|c| ≤ p−6, the reservoir
  - all central mixed windows, ID, E0
  - B-bound / ENV / CM / DM and the cap
  - exact UB failure, with both Lemma 20 one-way clauses including the "no run of S′∖P_(S′) is empty" boundary
- **LJ only:**
  - first unique P exit at r+1, with max(j, ⌈(κ+2d−1)/2⌉) ≤ r ≤ κ−d−1
  - θ_u ≤ −1 and β(u) ≥ 2κ+4d−2
  - at least one predecessor exactly −1
  - all QQ-1 / QQ-mixed inequalities
- **New tests:**
  - (Defect), n ≥ b, Lemma 3(a)/(b)
  - if F = 0: both predecessors −1, (Z), β(Y) = 0, zP ≥ 8d−4+4zQ, zP ≤ (κ−1)/2, κ ≥ 16d−7+8zQ
  - if F > 0: both orientations with all defect tests

Finiteness holds per fixed (κ,p) only.

## 9. Limits of this review

- UMR-F/UMR-P and UPAR-R's exhaustive P+/LJ dichotomy were taken as accepted premises. The relevant UPAR sections are not pasted beyond the listed ranges, so I did not re-derive them.
- This is a written, model-only check. It is not a human, Lean or runtime certification, and it makes no novelty claim.
