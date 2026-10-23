# Review: combined BOTTOM unit (P LF34–203 + C LF15–117)

## Counts

**FATAL 0 · MAJOR 0 · MINOR 2.** There are also some uncounted editorial notes.

I found no mathematical error in the load-bearing chain. Theorem BOTTOM and Corollary BOTTOM follow at exactly the stated scope from the accepted interfaces:

- NF (existential)
- GRX, if direction
- RS(b), at the R5 scope
- UH-A, at its literal antecedent
- classical Cauchy–Davenport (CD)

The proof uses no RUH3/RUH2/KP3/KP4/R7, UH-L/SH/MW/PH, or multiset-only premise. This is a reviewer finding on the written candidate. It is not acceptance.

## Claim-wise verdicts

**1. SR window (P LF36–41): correct.**
- Every block is odd, so the GRX parity count is #{f_i=0} = 2e−2m. That gives C_max = 2p−2e+2m.
- Since p−e = e−1, this becomes j∈[m,m+e−1]∩[1,p].
- R_i sits between S_(i−1) and S_i, so T_GRX = Σ_{i∉P}θ_i = Σ_P τ_i, using Στ=0.
- j=e is admissible for every proper nonempty P.

**2. Pairing, Lemma P, Lemma U, (W), c-range (P LF43–56): correct.**
- Lemma P: Σmin(q,v_x) ≥ 2q, and the offset-q pairing gives p−1 unequal pairs when μ ≤ p−1. RS(b) with K=p−1 then hits all p residues at n=p−1, j=e.
- Lemma U: two classes would need at least 2p > R letters.
- a=0: two of the p+1 values y_i coincide. The arc between them has m=1 and T=0, and p−1 zero rotations hit that target.
- A′ ≤ κ: use all-plus at j=e−1, n=p+1.
- UH-A at κ=(p−1)/2 (inside its literal range) gives c ≥ 3. R gives c ≤ p−1.
- (W) comes from the multiplicities A−d and A′+d. The threshold λ=c−1 matches UH erratum v1.

**3. MW/(CW)/escape classification (P LF60–70): correct.**
- K_j = 2j−2. Index j is counted iff e−g/2 ≤ j ≤ e+g/2.
- Even g with r+1 ≤ m ≤ e−r: w0+q = p, which is impossible.
- Odd g: w0+q = p−1.
- For m ≤ k0: ⌊e/2⌋+⌊(e−1)/2⌋ = e−1, so m+r ≤ e.

**4. Lemma C, including g=1 (P LF72–88): correct.** This is the odd-g equality case.
- g ≥ 3:
  - If any ω had |I∪(I+ω)| ≥ g+2, then w0−1 further CD steps would reach p.
  - The growth of a q-interval under a shift v is min(q,p−q,v,p−v).
  - Here q=g ≥ 3 and p−q ≥ e ≥ 6, so v=±1 and ω=±2a.
- g=1:
  - The set {0,u,v,u+v} plus p−4 further steps would reach p, so all differences are ±u.
  - β = p−2−δ ≥ c−1 ≥ 1, which forces u=±2a.
- Equality:
  - For each counted j, w0 = β+δ ≤ n ≤ φ, so (y,w) ranges freely over [0,β]×[0,δ].
  - The normalized sums p−j−y+w fill [p−e−r−β, p−e+r+δ], which is p−1 integers.
  - The missing residue t gives 2t ≡ g+2δ ≡ D_z/(2a). The conclusion 2Σ_P H_i = D0 follows.

**5. Local transport (P LF90–92): correct.**

**6. Section 3 / (LB) (P LF94–103): correct.**
- Toggling an empty run leaves d unchanged. The result stays proper and nonempty because m ≥ r+2 ≥ 2.
- For odd e, m+r ≤ e−1 always holds.
- For even e, the only exception is (k0, e−1). There, m′=m and m′=m−1 are both low critical, so every empty run must be flat.
- (LB) with ℓ=e−1 at m=k0: an odd g ≤ e−2 means g ≤ e−3, so m+r ≤ e−1.

**7. Anchor lemma and the m=k0 path (P LF105–117): correct.**
- I traced the path step by step:
  - The additions N−1 down to 2k0 extend the interval through 0; run 2k0−1 separates it from {2k0−2}.
  - Remove 0.
  - Each "add 2j−1, remove 2j" pair slides one singleton by one place.
  - Adding 2k0−1 merges into the long interval.
  - The endpoint is P0^c, and m=k0 at every step.
- The path needs N ≥ 2k0+2, i.e. e ≥ 4. It never uses m=e.
- A removal can raise d by at most A′ ≤ e−1 < 2ℓ.
- The "avoiding sets are low" margin is 2ℓ−2e+3+2δ ≥ 1 for ℓ ∈ {e, e−1}.

**8. Missing sets (P LF119–124): correct.** The general bounds on |J| are kept. Full G is substituted only for b ≤ n ≤ A, and the A+1 rule yields M∪{0}.

**9. Lemma ME (P LF126–150): correct.** I re-derived:
- J(Y) is admissible and free for m ≤ M0.
- |F(Y)| = min(e, m+μ) ≥ μ+1.
- D ≤ max(3μ+ε−e, c−2) ≤ 2e−2.
- D ≥ L−c−1, using 2M0 ≤ e+2.
- Prefix additivity holds, with k6 ≤ M0 and h0 ≤ M0.
- The bounds E ≤ ⌈c/2⌉−1 and E+C_E ≤ e+ε−1 hold in all three sign cases.

**10. Theorem E0 (P LF152–203): correct, subject to MINOR-1.**
- The c-range partition is exhaustive:
  - odd e (ℓ=e): Case A for c ≤ e−1, Case C for c ≥ e;
  - even e (ℓ=e−1): Case A for c ≤ e−2, Case B for c=e−1, Case C for c ≥ e.
- Case A:
  - α(S) ≤ ⌊(c+1)/2⌋, so c is odd, |S|=c+1, every component is an even path, Q=∅ and E=c+1.
  - RS(b) with K=c+1 then puts c+1 residues in M, but |M| ≤ c.
- Case B (c=e−1, even e):
  - An independent k0-set would be an all-empty escape with g=e−1 whose own runs are isolated, so they are not flat.
  - Hence α(S)=e/2, |S|=e, Q=∅, and |M| ≥ e > c.
- Case C:
  - The (POS) identity checks out.
  - (α): the bound c+k0 ≤ p−1+ε contradicts c+k0 ≥ ℓ+2k0 ≥ 2e.
  - (β): |Q| ≤ c−e+1 < c+3−e.
  - (γ): both subcases close.

**11. C's restatements and (LEN) (C LF25–33): correct and faithful.** Σ(L_i−2) = R−2N = −4.

**12. Minimal interior g (C LF35–73): correct.**
- Step (1), every singleton is signed −a. This step does not use minimality:
  - A signed-a singleton flip gives g−1. That hits (W) when g=1, or the even window [r+1,e−r] otherwise.
  - A signed-3a singleton flip keeps g, and the result is low critical while containing −3a. That is impossible for p ≥ 5.
  - A signed-−a singleton flip gives 2r+2, whose forbidden window is exactly [r+2,e−r−1].
- Step (2), endpoints and singleton counts:
  - A strictly interior m is impossible.
  - At the lower endpoint, singletons are isolated, so s1 ≤ 2m−1 = g+2.
  - At the upper endpoint, singletons are flat, so s1 ≤ N−4m+s_sign1 ≤ N−2m−1 = g.
  - (LEN) then gives L_i ≤ g for every run. g=1 dies outright.
- Step (3), pure-a flip:
  - There are at least g+2 pure signed-a runs, none of them singletons, each with 2 ≤ L ≤ g. The flip gives g′ = g−L.
  - Even g′: L is odd ≥ 3, and the even window covers [r+1,e−r].
  - Odd g′: [r+1,e−r] ⊆ [r′+2,e−r′−1], so the pure-a flip stays interior with a strictly smaller g′.
- The minimum is taken over all interior patterns, not only m ≤ k0. This is legitimate, and it is what keeps the pure-a flip inside the class.
- Only e=g+2 odd survives. Since (IC) forces g ≤ e−2, every interior pattern has the (TOP) parameters.

**13. Caps and long run (C LF75–98): correct.**
- (EV) at m=k0: even g is killed by MW, and odd g ≤ e−3 would be interior.
- (OD) at k0=(e+1)/2: 2m−1 = e.
- (LR) uses only d_h and the m=k0 path. For ℓ ≥ e−2 the removal gain is less than 2ℓ when e ≥ 4.
- An escape exists, because ℓ=e would force L_h ≥ p+1+δ > p−2.

**14. Final contradictions (C LF100–117): correct.** I checked these by substituting into the displayed inequalities, with no enumeration.
- Even e: L_h ≥ p−1+δ > p−2.
- Odd e: s1 ≥ p−1+δ, but at (TOP) s1 ≤ β ≤ w0 = e < 2e−2.
- p=11 (e=6, k0=4, interior g ∈ {1,3}): L_h ≥ 10+δ > 9.
- p=13 (e=7, (TOP) g=5, m=4): L_h ≥ 10+δ, so s1 ≥ 12+δ > w0 = 7.

**15. Theorem and Corollary BOTTOM (C LF17–23, 116–117): correct at the stated scope.** They depend only on the accepted interfaces listed above, which are recorded as accepted in the supplied verdicts. UH-A removes c ≤ 2 and R removes c ≥ p. No unresolved load-bearing dependency remains.

## Findings

**MINOR-1. Exposition in E0 Case C(γ), P LF179–181 with LF197–199.**
- **Step:** P chooses "the 1st, 3rd, 5th, … available runs" without saying which direction to count. LF197–199 then claims that neither y nor the run before y is in I. That claim holds only when counting in path order (h removed) from each cluster's first run. Counted from the other end, index l−1 lands in I for both an odd start-end cluster and an even inner cluster.
- **What breaks without the fix:** y would join that run's interval, so m(P′)=m(P). (LB) would then give only |Q|−1 ≤ c−E+1, which is not a contradiction.
- **Consequence:** none once the direction is fixed. The (POS) counts do not depend on direction, and I is the prover's free choice.
- **Repair:** add one phrase at LF180: "counted in path order from each cluster's first run."

**MINOR-2. Process/scope wording in P.**
- **Step:** P's frozen text at LF3–4, LF31, LF239–243 and LF247–249 says the cell is "not a bottom-cell closure", is "restricted exclusions", and that no contradiction is claimed. Only the package (LF11–13), C (LF9–10) and the residual ledger (LF20–22) supersede this.
- **Consequence:** none mathematical. Someone citing P alone would record the cell as open, or would treat Theorem BOTTLE and §7 as non-vacuous.
- **Repair:** any record should cite Theorem BOTTOM with its proof as P LF34–203 + C LF25–117. It should mark P LF3–4, LF31 and §§7–8 as historical.

**Editorial (uncounted).** Several symbols are overloaded:
- P names both the file and a run set.
- δ is both the GRX parity count and R−A−A′.
- H is both e−1 and the per-run H_i.
- L is both an endpoint in ME and a run length.

Each use is local to its section, and I found no resulting ambiguity.

## Checked non-issues

- **Anchor clause at ℓ=e−2.** The "avoiding sets are low" clause (P LF112–113) fails at ℓ=e−2 when δ=0, because the margin there is 2δ−1. C LF89–94 correctly takes only L_h ≥ 2ℓ+δ. Future reuse at ℓ=e−2 must not import that clause.
- **g=e omitted.** "Low critical" excludes g=e. This is harmless, because no use needs it.
- **p ≥ 11 is the scope, not a requirement.** The steps need only p ≥ 5, e ≥ 4 and e ≥ 3. I make no claim about p=7.
- **No circularity.** E0 uses only P §§1–2. C uses E0 only through (LEN).
- **c = p−1 (b=0) works.** B=∅, M = Z_p∖{0} and |X| = 0.

## Errata applied

- UH erratum v1: λ = c−1 matches (W).
- UH errata v1/v2 and v3 OB2: the filler and free-length rules are respected at P LF122–124 and in ME's B0.
- UH v3 item 1: the "nonempty" wording appears at P LF113.
- UH v3 item 4: work on the NF word, as P does.
- RS R5: every call uses an integer K ∈ {p−1, w0, b, c+1, e} and nonzero terms.
- lowodd M2: the group law is fixed at P LF36.
- ZX: the NF is existential and κ is integral.

## Separation of concerns

- **Correctness:** no error found.
- **Completeness:** the argument is exhaustive over c ∈ [3,p−1], both parities of e, g=1, and every interior m. It is scoped to this terminal NF cell only.
- **Process:** MINOR-2. I did not re-check hashes; those are parent-checked metadata, not proof acceptance.
- **Priority/novelty:** none is claimed and none was assessed.
- **Computation:** the candidate uses none and none is needed. My checks were by hand.

This is a reviewer's recommendation only. The exact combined claim is correct after the MINOR-1 wording fix. It is not acceptance, not UH-EXCL, not ordered Olson, and not a runtime approval. The parent owns the verdict, and no retry is requested.
