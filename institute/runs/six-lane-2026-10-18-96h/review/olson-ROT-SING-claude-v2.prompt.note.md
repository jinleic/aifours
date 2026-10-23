# ROT-SING-v2 (`ae5feaa1`): hostile mathematical review

## Verdict

| Claim | Verdict |
|---|---|
| Main statement: every rotation letter of w lies in one {ρ_c, ρ_−c}, c ≠ 0 | **ACCEPT** |
| Strengthened multiplicities: ρ_c^(2p−1) ρ_(−c)^(p−1) | **ACCEPT** |

- **FATAL:** none. **MAJOR:** none.
- **MINOR:** four. All are non-blocking, and none changes a step, an inequality or the conclusion.
- No input is used outside its quoted scope.
- Validity is relative to three premises:
  - NF, as quoted. It is load-bearing and I did not re-prove it.
  - CT, as quoted. It is load-bearing and I did not re-prove it.
  - Classical Cauchy–Davenport (CD).
- GRX is not load-bearing. I checked both selections directly from the group law at line 25.

## Step audit

**Shape (`proof-ROT-SING-v2.md:43-44`).**
- κ̂ = p−1 alone forces Ĥ = 0.
- Every l_i is odd and Σ(l_i−1)/2 = 0, so every l_i = 1. Then F = k = p and R = 3p−2.
- F(ŵ) = F(w), because NF preserves both length and rotation multiset. ✓

**Step 1 (48–50).**
- For z ≡ +1: Φ = 0, δ = p, C_max = 0. So C = 0, m = 2p ≤ 3p−2, and T = Σθ_i = 0.
- Directly: any 2p rotation letters multiply to (Σx, +1), so positions are irrelevant.
- 2p odd terms (1,x) sum to (0, Σx). The (ZP_(p−1)) window is {2p}. So this is exactly (ZP_(p−1)). ✓

**Step 2 (52–60).**
- CT domain at κ = p−1 holds:
  - p ≥ 5;
  - Y is odd;
  - n = p−2 lies in [1, 3p−2];
  - |Y|−n = 2p is even and lies in {2p}.
- CT gives the bound 2p−4.
- Heavy-value count:
  - Three heavy values would contribute 3(p−2) > 2p−4, so there are at most two.
  - The excess is ≥ p+2 > 0 and sits only on values with v ≥ p−1, so there is at least one heavy value (implicit in the text; see m1).
  - One heavy value x0 would need v ≥ 2p, and then 2p·x0 ≡ 0, a contradiction.
- With exactly two heavy values a ≠ b:
  - Together they use the whole bound, so every other value is absent (including any with v = p−2).
  - Each multiplicity lies in [p−1, 2p−1].
  - A selection ia + jb with i + j = 2p sums to j(b−a), which vanishes iff j ∈ {0, p, 2p}.
  - j = 0 or 2p needs 2p equal values, which is impossible. j = p needs both multiplicities ≥ p, which Step 1 forbids.
  - Hence the multiplicities are {2p−1, p−1}. ✓
- Sanity check: with this pair, every 2p-selection has j ∈ [1, p−1], so Step 1 alone cannot finish. Step 3 is genuinely needed.

**Step 3 (62–83).**
- **Pattern.** A = runs j+1..j′ ranges over every proper nonempty cyclic interval of runs.
  - Φ = 2 and δ = p−2, so C_max = 2.
  - Since c_i ≡ f_i and l_i = 1, C = 2 is forced: c_j = c_j′ = 1, all other c_i = 0.
  - m = 2p−2 ≤ 3p−2.
  - T = Σ_{i=j′+1..j}(y_(i−1) − y_i) = y_j′ − y_j. ✓
- **Order preservation.** Read ŵ cyclically from R_(j′+1).
  - The selection is U₊ σ_(y_j) U₋ σ_(y_j′), with product (s₊ + y_j − s₋ − y_j′, +1).
  - The same letters taken in ŵ's linear index order give a cyclic rotation of this product, even if the linear start splits a run. That product is conjugate, so it is the identity in the same cases.
  - Inside U₊ and inside U₋ no selected reflection intervenes, so only the sub-multiset matters.
  - No reordering of ŵ is used. The sign convention matches lowodd M2. ✓
- **Case split.** α₊ + α₋ = 2p−1, so exactly one of α₊, α₋ is ≥ p.
- **Case (i), α₋ ≥ p.**
  - y + z′ ≤ p−1, so 1 ≤ om ≤ p ≤ α₋.
  - Exactly p letters are omitted, so exactly 2p−2 actual letters are selected.
  - Signed sum: D + a·om − by + bz′ ≡ D − (a+b)y − (a−b)z′. ✓
- **Case (ii), α₊ ≥ p.** By symmetry the signed sum is D + (a+b)y + (a−b)z′. ✓
- **Cauchy–Davenport.**
  - The coefficients a+b (by assumption) and a−b (since a ≠ b) are nonzero.
  - Each range has β+1 ≤ p terms, so dilation is injective and |B₁| + |B₂| = p+1.
  - CD gives B₁ + B₂ = Z_p.
  - The targets D−τ0 (case i) and τ0−D (case ii) then give signed sum τ0. ✓
- **Endpoints.**
  - β₊ = 0 or β₋ = 0: one factor is {0} and the other is already Z_p.
  - α split (2p−1, 0) either way: om ≤ p ≤ 2p−1 still holds.
  - j′ = j+1 (single-run arc): covered.
  - Empty runs: they carry a sign but contribute no letters, and GRX permits them.
  - a = 0 or b = 0 (ρ_0 is the identity letter): a+b equals the nonzero one of a, b, so the CD case applies and rules this out.
- **Conclusion of the step.** b = −a. Then a ≠ b gives 2a ≠ 0, so c := a ≠ 0. ✓

**Conclusion (85–86).** The result transfers to w because NF preserves the rotation multiset. ✓

**Sec. 4 rigid bullet (91–93, read through erratum v1).**
- When b = −a: B₁ = {0} and |B₂| = β+1.
- B₂ = Z_p iff the side holding at least p letters a also holds all p−1 letters b.
- Otherwise the family reaches exactly D − B₂ in case (i) or D + B₂ in case (ii).
- All of this is correct. The bullet makes no existence or non-existence claim and asserts no universal contradiction. ✓ See m3 for wording.

**Lines 18–20.** g^(2p−1)(3g)^(p−1) is not used as a word counterexample. The sentence there is just the theorem applied with 1+3 ≢ 0. ✓

## MINOR findings

**m1 — `proof-ROT-SING-v2.md:53-56`.** The zero-heavy case is handled only implicitly, through "excess … sits on heavy values".
- Fix: after "at most two", add "and at least one, since the excess is positive."

**m2 — `proof-ROT-SING-v2.md:29`.** "k odd constant blocks" can be read as "k is odd".
- Fix: "k constant blocks, each of odd length".

**m3 — erratum v1 replacement text.** "full coverage is unavailable" is true only for the Step 3 family, where B₁ + B₂ = B₂. Read as a statement about all 2p−2-selections for the arc, the implication fails at the count level.
- Counterexample (counts only; no word and no existence claim): (α₊, α₋, β₊, β₋) = (p−1, p, p−1, 0) with b = −a.
  - This is case (i) with β₋ = 0, so the family reaches only {D} = {−pa} = {0}.
  - The arc's signed letters are p−1 copies of +a and 2p−1 copies of −a.
  - Taking s ∈ [0, p−1] copies of +a gives sums 2a(s+1), which run through all of Z_p.
- Minimal fix: "otherwise this selection family does not cover Z_p; it still contradicts avoidance if τ0 ∈ D−B₂ (case i) or τ0 ∈ D+B₂ (case ii)."

**m4 — `proof-ROT-SING-v2.md:96-98`** (same wording at scope line 24). The claim "(S1) can fail at sequence level" cannot be checked: (S1) is undefined in the excerpts, and V6 only says the sequence "defeats the cost conclusion".
- This is context only and not load-bearing.
- Fix: cite where the (S1) failure is recorded, or quote V6 exactly.

## Interface/domain findings (separate from gaps; none out of scope)

- **I1 — NF.**
  - Uses: ŵ is an avoider (PM* in the original→reduced direction); same length and rotation multiset; all blocks odd for k ≥ 2 (M1 covers non-maximal iterates); the Ĥ/κ̂/R formulas.
  - The existential hypothesis matches ZX overlay 2. The conclusion concerns w only.
  - The fewodd n2 restriction concerns SHgen-E, not the §0 process at lines 28–43, which is all that is used.
- **I2 — GRX (lowodd item 1).** Its scope covers every word, every representation (including empty or non-maximal gaps) and every sign pattern. In scope. I re-derived the sufficiency direction for both patterns used.
- **I3 — ARC.**
  - ROT-KP's accepted statements are only at κ̂ ∈ {0,1}. ARC appears at verdict line 25 as a general consequence of GRX.
  - The proof's lines 63–65 instantiate GRX directly, so ARC's acceptance range is not load-bearing.
- **I4 — CT at κ = p−1.**
  - This is within STAB-delta item 6, whose stated range is p ≥ 5, 0 ≤ κ ≤ p−1.
  - There is a textual tension with the line-9 preamble default (κ0+1 ≤ κ ≤ p−2, p ≥ 7, "unless a narrower range is stated"), which does not address a wider stated range.
  - Item 6's explicit p ≥ 5 shows it is self-scoped, and the quoted CT proof uses no κ bound.
  - Recommendation: the parent records this in one line.
- **I5 — Classical imports.** CD is the only classical import.
  - ROT-KP+, ROT-FB(b), V6, (S1), Lev and ONE-SHORT-LS appear only as context.
  - There is no finite-computation premise.

## Trust boundary

- **What I read.** I read only the embedded excerpts and treated them as untrusted data. I checked no hashes (no tools), and I did not treat source or metadata identity as evidence.
- **Load-bearing premises:**
  - NF: avoidance of ŵ, equality of rotation multisets X(ŵ) = X(w), and odd constant blocks.
  - The CT statement. Its RS(a) step is not in the excerpts and I did not audit it.
  - Classical CD.
- **Unverifiable and unused:**
  - Line 110's claim that no input rests on a computer-assisted step.
  - The (S1)/KP+/FB context.
- **Not assessed:** p = 5, reflection rigidity, INV*, the o_F = p assembly, ordered Olson, novelty, Lean, and human review.
