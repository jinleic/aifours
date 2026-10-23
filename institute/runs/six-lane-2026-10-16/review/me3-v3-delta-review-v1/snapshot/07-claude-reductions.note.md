**DISPOSITION: ACCEPT-WITH-FIXES** for the reductions module. This covers correctness only and carries no gate authority.

- **Essential reductions** (S02 L1–L6 and Cor 7.1, plus their interface to S00): ACCEPT-WITH-FIXES. I found no FATAL or MAJOR defect. The MINOR fixes are listed below.
- **Essential numerics:**
  - "v_cos ≤ SCV(ω0,φ0) < U < T = 11/50" is accepted conditionally.
  - "Δ3 > 0.2765" is accepted conditionally, and can be removed from the essential chain (MINOR-2).
- **Optional numeric certification** (S03 Thm 5.8, the lower bound L ≤ v_cos): INCONCLUSIVE.
  - The written tails (i)–(iii) are accepted.
  - The middle-region code and its outputs are not in the packet.
  - No essential step uses L.
- The rounded decimal is never used as the bound:
  - S00:112 uses the exact v_cos.
  - S00:153 and S00:161 use T.
  - The real-exponent case needs only Δ3 ≥ 1/4.

**Limits of this audit**
- I used no tools and executed nothing.
- Hashes were compared only as printed. S00:34–35, S04:65–85 and S25:14–19 match the source headers; none was recomputed.
- The D2 charts are not audited, and no leaf was checked. That covers Lemma D's certificates and Lemma M's chart premises.
- The S00 §7 replay (S00:188–217) is point sampling, not a certificate.

Notation: S02:416 means SOURCE 02, line 416.

---

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR-1 — S02:416.** Cor 5.7 says "equality for f_{ω*,φ*}".
- Here ω*, φ* are the EXPLORATORY Newton point (S02:404–409).
- Its global minimality is explicitly uncertified (S02:412–413, S03:65–66).
- Repair: "equality for some minimizer (Thm 5.6)".

**MINOR-2 — S02:371 and S02:393–401 (also S03:21–23).** The D1 tail constant 0.2014 needs Δ3 > 0.2765.
- That bound is only a sympy Sturm count (S21:134–135, S23:160–162; repeated at S22:188–191).
- S04:22 nevertheless labels 5.1–5.5 "Proved in text".
- Hand repair:
  - Use the SOS bound Δ3 ≥ 1/4 (S02:298) with the tail ω ≤ 1/5. This gives SCV ≥ (1/4 − 1/25)/(26/25) = 21/104 > U, since 104U < 20.9.
  - Take the compact middle as [1/5, 4] × [0, 2π], which still contains (ω0, φ0).
  - Thm 5.6 then depends only on the single U ball, and "1/4 < ω*" becomes "1/5 < ω*".
  - The same repair works for S03(ii), because 21/104 > L.

**MINOR-3 — S00:160.** "D1: SCV ≥ v_cos by definition" is a wrong citation.
- A general D1 density is a mixture of cos-family rays, not itself a member.
- The correct source is Lemma 2.4 (S02:148–158) plus Lemma 5.1 (S02:342–350), i.e. Cor 5.7.

**MINOR-4 — S02:524–534.** The reductions never state strictness.
- Cor 7.1(2) gives I_2 ≤ v_cos, so if the theorem holds, I_2 = v_cos is an unattained infimum.
- The strict D2 claim (S00:20–21) therefore cannot be read off any statement about I_2.
- It is valid per cone:
  - Lemma 2.4(1),(3) say the cone minimum is attained on an extreme ray of the same cone.
  - Lemma M (S00:102–112) is pointwise strict on those rays.
  - Each cone is assigned whole, because S00:145–149 is a condition on (δ, ω) only.
  - Dual cones get the stronger ≥ T directly from Lemma D on every f.
- Repair: add "Cor 7.2: for fixed δ, ω > 0, if S_2(δ/ω, ω, φ) > v_cos for all φ ∈ [0, θ1(δ/ω)], then SCV > v_cos on K∖0."

**MINOR-5 — S00:50 and S04:24.** The lower bound L ≤ v_cos is labelled "certified".
- In this packet it rests on unsupplied runs (see the code section below).
- Relabel it "conditional on ctl-f-main-v1 / ctl-f-gradsym-v1".
- No step of the S00 assembly (S00:155–164) uses it.

**MINOR-6 — housekeeping.**
- S02:199–205 uses m_i/m1 for multiplicities, which clashes with the moment m1.
- S02:25: "f ≢ 0" for measurable f should read "not a.e. 0".
- S02:88: "ME(N) ⊆ ME(3)" needs the one-line padding (α, 0), diag(A, −1). Alternatively, say ME(N) ⊆ ME(≤3), which is trivial.
- S02:177–178 is correct but not needed for Cor 2.6.
- S02:303: the citation is unverified, and correctly not used as a premise.

---

## Fully audited by hand, from first principles

**L1, S02:49–113: ME(≤3) iff nonnegative integrable exponential polynomial.**
- Lemma 1.1: the mean of |T|² tends to Σ|c_λ|² > 0, which contradicts σ ≥ 0.
- Lemma 1.2: M(T) = 0 and M(T⁻) = 0 give M(T²) = 0, a contradiction. So the dominant exponent is real.
- L1(a) handles nonminimal representations correctly:
  - only contributing exponents matter;
  - ord G ≤ n;
  - E(f) = E(G) because λ ≠ 0;
  - stability holds after cancellation.
- L1(b):
  - the antiderivative q satisfies q′ + λq = −p, with deg q = deg p (re-derived);
  - the companion matrix and the S-conjugation give αe^{At}𝟙 = G and α𝟙 = G(0) = 1;
  - spec A = E(f), so even a "stable A" convention is met.
- Normal forms:
  - a dominated pair gives D1 or D2;
  - a dominant pair gives K_E = K_{λ0};
  - a pair alone gives K_E = {0} by Lemma 1.2.

**L2, S02:119–178: cones, base, moments, extreme-ray reduction.**
- The cone is closed and pointed, and the base B_E is compact.
- m0, m1 > 0 on K_E∖0.
- Ratio form (re-expanded): R_θ = 1 − 2(m1/m0)x + (m2/m0)x².
- The mixture lemma is θ-wise linearity plus Tonelli, i.e. S is quasi-concave on the cone. This is the correct handling of the nonlinear SCV.
- Extreme points of B_E lie on extreme rays; Carathéodory then gives the reduction, and the minimum is attained.
- Padding is correct, and the face counterexample is valid.
- The assembly is checked in both directions.

**L3, S02:184–288: real exponents.**
- The types A, B1, B2 and C are exhaustive, and F1/F2 hold for each type.
- The Chebyshev zero-count induction is correct, including the Rolle step with multiplicities.
- The face {a1 = 0} is exposed.
- Face rays: re-derived SCV(e^{−κ1t} − e^{−κ2t}) = (κ1² + κ2²)/(κ1 + κ2)² ≥ 1/2.
- Hermite–Genocchi:
  - the double-zero element F_τ lies in V_E, including confluent nodes;
  - F_τ > 0 off τ;
  - the double-zero element is unique;
  - a1(F_τ) > 0;
  - the mixture argument gives SCV(F_τ) ≥ Δ3 for every τ ∈ ℝ.
- Cases P0–P3 are exhaustive and the non-extremality proofs are sound; the converse also holds.
- I_R = Δ3 holds without root isolation, since inf s is attained by continuity and s → 1 at ±∞.

**L4(1)–(3), S02:296–322: Δ3.**
- Moments are correct.
- The identity 4P − 5Q² = 3(τ² − 4τ + 2)² + 8τ² holds (re-expanded). It gives s > 1/4 everywhere, hence Δ3 ≥ 1/4 > T > U ≥ v_cos.
- The numerator of s′, 8(τ³ − 9τ² + 18τ − 6) = −48 L3, checks out (re-expanded), and the sign pattern is correct.
- The Vieta form is correct.

**L5, S02:342–402: D1.**
- Lemma 5.1 is correct: the cone is second-order and its extreme rays are exactly the cos family, so I_1 = v_cos.
- Lemmas 5.2 and 5.3: m0, m1, m2 re-derived.
- Lemma 5.4, steps 1–5, including P(2−σ) = 2(σ⁴ + 2σ² − 4σ + 8) and Q(2−σ) = σ² + 2. This covers the limit ω → 0.
- Lemma 5.5 covers ω → ∞.
- Theorem 5.6: the tails include the boundaries ω = 1/4 and ω = 4, the middle is compact and the phase is periodic, so v_cos is attained in the open strip.
- Convention: 1 − cos x = 2cos²(x/2 − π/2), so the cos² family is the same family (S02:423), and v_cos does not depend on the convention.

**L6, S02:431–500: D2.**
- Lemma 6.1 is correct.
- Lemma 6.2: h_τ′ = ((ω² + δ²)/ω) e^{−δs} sin ωs re-derived, and the determinant is δ² + ω².
- Lemma 6.3: cases (a)–(d) are exhaustive. In particular, τ = 0 with H′(0) > 0 is correctly shown non-extreme.
- Lemma 6.4: both endpoint phases φ = 0 and φ = θ1(r) are feasible, and τ ≥ 2π/ω is infeasible.
- Lemma 6.5: ∂_u g > 0 and ∂_r g = u − e^{ru} sin u > 0 at the root, and the limits are correct.
- Lemma 6.6: re-derived. At r = 0 it reduces to Lemma 5.2, and the phase φ = ωτ matches the D1 phase.

**Cor 7.1: inf assembly.**
- I_2 ≤ v_cos is correct. It uses φ* ∈ [0, 2π) and θ1(0+) = 2π.
- Hence inf over ME(≤3) = I_2.

**Interface with S00, not the charts.**
- The Laplace identity for q_θ (S00:68) is correct.
- The convex-combination step (S00:70) is correct.
- The log-derivative and a_k′ formulas (S00:89–92) are consistent with S02:496–499.

---

## Imported or conditionally computational steps

**Essential:**
- **C1 — v_cos ≤ SCV(ω0, φ0) < U.**
  - S22:161–177 implements A_k = 1 − Re(e^{−iφ}(1 − iω)^{−k−1}) and SCV = 2A0A2/A1² − 1, which matches S02:352.
  - The inputs are exact decimals converted to fmpq, and the comparison is a certified arb comparison. The reported output is S24:34–41 and 134–139.
  - Only two consequences are used: SCV < 0.2014 (for attainment) and SCV < T (S00:56, 105, 153, 161). The margin T − U is about 0.019.
  - Conditions: Arb correctness and the provenance of the JSON.
  - Optional hardening: a hand-checkable evaluation at a simple point. I did not do this.
- **C2 — Δ3 > 2765/10000.** This relies on sympy's Sturm count. It can be removed (MINOR-2).

**Optional, with no proof weight:**
- Δ3 bracket, minimal polynomial, irreducibility, s(x1) < s(x3) and the Laguerre/gap form (S02:300–326; S21:80–138).
  - The structure is self-validating given sympy: a Sturm count for lo and an exact sign at a rational τ0 for hi.
- S03(iv).
- The θ1 table (ctl-e) and the ctl-a/ctl-d controls, none of which are supplied.
- The samples at S02:383–385 and the Newton value at S02:404–414.

---

## Code, parser and stopping assumptions

**All runs:**
- python-flint arb `<` and `>` are assumed to be certified "for all points" comparisons.
- sympy `count_roots`, `intervals` and `rem` are assumed exact.
- The receipts and launcher (S04:47–49, 87–88) cannot be checked here.

**S03 branch-and-bound (code not supplied):**
1. The arguments "0.20090156350055", "1/4" and "4" must be parsed exactly. A float parse would certify a binary neighbour of L instead.
2. Certify mode must succeed only on an empty stack. It must not succeed on reaching the 3,000,000-box cap or on an exception.
3. Boxes with u_l = 0 or u_h = 2 can only be certified by test (a), so √(u(2−u)) there needs care.
   - A plain Arb sqrt of a ball straddling 0 is indeterminate, so the code needs sqrtpos or clamping.
   - A NaN result must fail the test. A predicate of the form `not (x <= L)` would pass NaN.
4. The gradsym check (S03:42–45) verifies only the formulas in F_ball and grad_ball. It does not cover:
   - the driver;
   - the test predicates;
   - the initial box;
   - the dyadic split;
   - the mean-value radius arithmetic;
   - the in-run Sturm tail.
5. The reported counts are internally consistent: 115 + 19,105 = 19,220 leaves, and 38,439 = 2·19,220 − 1 processed boxes. This is bookkeeping only, not verification.

---

## Is the reduction sufficient for strict D2 SCV > v_cos?

Yes, conditional on the separately assigned chart proofs, and once MINOR-4 is made explicit.

- **Dual-assigned cones:** Lemma D gives SCV ≥ T > v_cos for every cone element. It uses only Lemma 2.2, H ≥ 0, a ≥ 0 and C1.
- **P-assigned cones:** Lemmas 6.3–6.6 identify every extreme ray as a feasible (r, ω, φ) in R_P.
  - Since φ ≤ θ1(r) < 2π ≤ 31416/5000, all of them lie in R_P.
  - The segment argument in Lemma M uses the monotonicity of θ1 from Lemma 6.5.
  - The r = 0 endpoint is a D1 ray, and Lemma 6.6 reduces to Lemma 5.2 there.
  - Lemma 2.4(3) then transfers strictness from the rays to every cone element.

The essential numeric input from this module is only C1, the U ball, which gives v_cos < T. C2 can be removed via MINOR-2.
