<!-- Parent capture 2026-10-18T02:30:11-07:00 of read-only scout ME3SuccessorScreen (25m52s). Its hand derivations (H1-H4, Delta_3, P-tilde, D) are UNTRUSTED. A search miss is not novelty. -->

## Parent primary checks before freeze (2026-10-18T02:30:11-07:00)

- HSTZ 2016 (https://math.bme.hu/~safaro/cikkek/osafarepew.pdf, fetched 2026-10-18): abstract, verbatim: "there is a long standing conjecture that for the first non-trivial order, which is order 3, the cv cannot be less than 0.200902 but the proof of this conjecture is still missing". Section 2: "No analytic results are available for the minimal value of cv in the class ME(n) for any n ≥ 3." Definitions 1, 2 and 5 match the screen: the order is at most n, X is continuous, and cv = m2*m0/m1^2 - 1 (a squared CV). The paper also states that the contributing eigenvalues always include a dominant real eigenvalue ([6], [8]).
- Battagliola–Peralta arXiv:2609.14612 (abstract, 2026-09-13) covers only common-damping harmonic densities. The non-common-damping case (D2) is outside its scope.
- **Convention pin** (parent mpmath, 30 digits, numerical aid only):
  - Reading HSTZ eq. (4) literally as e^(-t) cos^2(1.03593 t - 0.337037) gives SCV 1.5757070, which is wrong.
  - e^(-t)(1 - cos(1.03593 t - 0.337037)) gives 0.2009015635020.
  - A Newton stationary point at (ω, φ) = (1.0359329551, 0.3370382424) gives 0.2009015635005570, with 1/SCV = 4.977562059, matching the printed 4.9776/4.97756.
  - The minimum over the cos^2 family equals the minimum over the 1 - cos family, by reparametrizing frequency and phase. The table's ω is therefore the imaginary part of the complex pole in the 1 - cos form.
- No literal decimal enters the contract. The target constant is v_cos, defined as a minimum.

## Verdicts

- **ME(3) minimum-SCV conjecture (Horváth–Sáfár–Telek–Zámbó, HSTZ 2016): OPEN-IN-SCOPE. Headroom is plausible but unproven.** I found no proof and no counterexample in any source up to 2026-10-18. The 2026 Battagliola–Peralta papers settle only subclasses, and say so explicitly. The hard part that remains is one sub-case, real pole strictly dominant over the complex pair (D2 below), which I could not resolve on paper.
- **Commault–Mocanu 2003 (CM2003) Problem 5: KNOWN-SOLVED. Do not nominate.**
- This is not a problem from the mathematics book. The only phase-type entry in the inventory is the minimal-PH chapter (`math.json` ~line 3277; book p.544, which I checked in the rendered image). That page can serve only as a thematic bridge.

## Contract-ready statement

- **Class.** ME(3) is every law on [0,∞) whose CDF is F(t) = Pr(X<t) = 1 − α·e^{At}·1, with α a real 1×3 row vector, A a real 3×3 matrix, and F a valid continuous CDF. Its density f(t) = α·e^{At}·(−A)·1 is ≥ 0. This follows HSTZ Definitions 1–2 ("representation of order at most n"). Equivalently, ME(3) is the set of laws whose Laplace transform is rational with denominator degree ≤ 3.
- **Objective.** SCV(f) = m0·m2/m1² − 1, where m_k = ∫ t^k f. This is HSTZ Definition 5, which they call "cv".
- **Constant.** v_cos = min over ω>0 and φ of SCV(e^{−t}(1 − cos(ωt − φ))).
- **Target.** Prove SCV(X) ≥ v_cos for every X in ME(3). Alternatively, give an explicit ME(3) density with certified f ≥ 0 on all of [0,∞) and certified SCV < v_cos.
- **Not gates:** the common-damping case only, the real-pole cases only, finite scans, and extensions to higher order.
- **Use v_cos, never the decimal.** The conjectured minimiser itself does not satisfy "≥ 0.200902" literally:
  - Éltető–Rácz–Telek 2006 (ERT) and Buchholz–Horváth–Telek 2011 (HBT) both print 1/min = 4.97756. That puts the minimum in (0.2009014, 0.2009018], so 0.200902 is a rounded-up value.
  - My hand evaluation at the published optimum gives 0.200901 (UNTRUSTED).

## Definitions, quantifiers and admissible cases

**0.200902 is CV², not CV.**
- HSTZ Definition 5 uses m0·m2/m1² − 1.
- The 2009 moments paper (Horváth–Rácz–Telek, ASMTA 2009) reports "n2 = 1.200902", where n2 = 1 + SCV.
- The plain coefficient of variation is about 0.44822.

**Pinning the optimiser.** HSTZ eq. (4) read literally, with Table 2's (1.03593, 0.337037), does not reproduce the value: I get about 1.58 by hand.
- The invariant form, from HBT 2011 §3.1, is u·e^{−at}(1 + cos(ωt + φ)) with "a = 1, φ = −3.47863, ω = 1.03593".
- Equivalently, f*(t) ∝ e^{−t}(1 − cos(ωt − 0.337037)), with poles −1 and −1 ± 1.03593i and zeros at ωt ≡ 0.337037.
- The text extraction of HSTZ (4) is garbled. The parent should render HSTZ pp.4 and 8 to confirm the convention.

**Admissible cases.** The classes are from ASMTA 2009 §3 and Kolossváry–Telek 2011.

| Class | Poles | Density shape |
|---|---|---|
| A | three distinct real | sum of three real exponentials |
| B | one double real pole plus one simple real pole | |
| C | one triple real pole | |
| D1 | real pole λ1 and complex pair with equal real part | a₁·e^{−λ1 t} + a₂·cos(ωt + φ)·e^{−λc t}, λ1 = λc |
| D2 | real pole strictly dominant, λ1 < λc | same form |

- A complex pair cannot be dominant: f ≥ 0 forces a real dominant pole (the "λ1 ≤ λc" condition in ASMTA 2009 Theorem 5).
- Lower orders are included by "at most n"; ME(2) = PH(2), so their SCV is ≥ 1/2.
- An atom at 0 is excluded by "continuous", and it could only raise SCV: (1 + SCV_c)/(1 − p) − 1. This is my derivation.
- f ≥ 0 has to be checked; there is no sign structure on α or A. ∫f = 1 is irrelevant because SCV is scale-invariant. The mean is automatically finite and positive.
- The accepted phase-type theorem (CM2003 Conjecture 1) does **not** cover ME: the D1 optimum has common real part and zeros on (0,∞), so it is not PH of any order.

## Status evidence

All quotes are 40 words or fewer.

| Source (date) | Quote | Bearing |
|---|---|---|
| [ERT 2006 slides](https://webspn.hit.bme.hu/~telek/cikkek/elte05h.pdf) (Madrid, Jul 2006) | Table row "3 \| 0.276583 \| 3.61556 \| 0.200902 \| 4.97756" | Origin of the numbers. The complex search assumed a common real part. Identical real eigenvalues are only asserted ("similar to the PH distributions"). |
| [ASMTA 2009](https://webspn.hit.bme.hu/~telek/cikkek/horv09c.pdf) (LNCS 5513:174–188) | "the outer borders in Figure 1 are the borders of the whole ME(3) class, but we cannot prove it" | Gives n2 = 1.200902. The abstract says the bounds rest on "unproved conjectures". |
| [HBT 2011](https://webspn.hit.bme.hu/~telek/cikkek/buch10c.pdf) (Int. J. Performability Eng. 7(5):441–454) | "there is no proof or counter example (an ME with lower scv) is available up to now which verify or destroy this conjecture" | Lists 0.276583 (real poles) and 0.200902 (complex). |
| [HSTZ 2016](https://math.bme.hu/~safaro/cikkek/osafarepew.pdf) (EPEW, LNCS 9951:18–31) | "the cv cannot be less than 0.200902 but the proof of this conjecture is still missing" | Also: "No analytic results are available for the minimal value of cv in the class ME(n) for any n ≥ 3." |
| [Horváth–Scarpa–Telek 2016 chapter](https://webspn.hit.bme.hu/~telek/cikkek/horv16h.pdf) | "minimal squared coefficient of variation among the order three PH and ME distributions are 1/3 and 0.200902" | States the value as fact without proof. This is a phrasing hazard, not a proof. |
| [Horváth–Horváth–Telek arXiv:1901.08627](https://arxiv.org/abs/1901.08627) (2019; Stoch. Models 2020) | "only conjectures are available for N ≥ 3" | |
| [Almousa–Telek 2021](https://real.mtak.hu/125732/1/AMI_53_from5to19.pdf) (Ann. Math. Inform. 53, online 2021-05-18) | "not proved even for the smallest non-obvious case, N = 3" | Also: "its solution is an open problem currently." |
| [Mészáros–Telek 2022](https://webspn.hit.bme.hu/~telek/cikkek/mesz20a.pdf) (PEIS 36(4)) | "the order N ME distribution with minimal SCV is not known for N > 2" | |
| [Battagliola–Peralta arXiv:2608.29143v1](https://arxiv.org/abs/2608.29143) (2026-08-29) | "We do not claim optimality … over kernels with several distinct or complex poles" | Covers only the single repeated real pole class, e^{−λu}·a(λu)². At order 3 its optimum is 0.276583. |
| [Battagliola–Peralta arXiv:2609.14612v1](https://arxiv.org/abs/2609.14612) (2026-09-13) | "The enlargement leaves the infimum unchanged from that of the classical cosine-squared construction." | Common damping only (Def. 2.1). Leaves a 2-parameter numerical search; no certified order-3 value. |

- Battagliola–Peralta arXiv:2604.26304 (2026-04-29) is asymptotic only.
- Peralta's other 2026 preprints (2603.28047, 2605.15395 and others) are unrelated.
- **Competitor risk is high.** Peralta has resolved several open questions in exactly this area during 2026. Re-screen at freeze and again after any result.

## Best matched prior work

- **Common damping (D1).** Battagliola–Peralta 2609 reduce it exactly to the cos² family, with a 2-parameter search and no certified value.
- **Triple real pole (C).** Battagliola–Peralta 2608 with m = 1 give the minimum Δ₃ = (x₃−x₂)²/(4x₂x₃) over the zeros of the Laguerre polynomial L₃. I computed Δ₃ = 0.276583 by hand.
- **Nonnegativity tests for ME(3).** ASMTA 2009 Theorems 1–5 and Kolossváry–Telek 2011 ([kolo11a](https://webspn.hit.bme.hu/~telek/cikkek/kolo11a.pdf)) give explicit or partly explicit tests.
- **Touching heuristic.** The ERT 2006 slides observe that the minimiser touches zero. They give no proof.

## Headroom and new representation (all UNTRUSTED hand derivations)

**H1. Reduction to extreme rays.** For fixed poles Λ and centre θ, R_θ(f) = ∫(t−θ)²f / (θ²∫f) is a ratio of linear functionals. Its minimum over the compact slice {f ≥ 0, ∫f = 1} is therefore attained at an extreme ray. This is Battagliola–Peralta Prop. 2.2 / Cor. 3.4 extended to non-common damping.

**H2. Real poles (A/B/C) look short.**
- The extreme ray with a double zero at τ is V·(t−τ)²·∫_Δ e^{−(t−τ)⟨u,λ⟩} du. This is the Hermite–Genocchi formula, and it is valid for repeated poles too.
- That is a nonnegative mixture of kernels e^{−μt}(t−τ)², so a ratio lemma gives SCV ≥ Δ₃ = 0.276583 for every real-pole ME(3).
- The boundary extreme rays have SCV ≥ 1/3.
- This would prove the HBT "real poles, order 3" entry. It is a subclass milestone, **not** the gate.

**H3. Laplace-domain dual.** Let q(t) = (t−1)² − ρ, Q(s) = (2 − 2s + (1−ρ)s²)/s³, κ = 1 − ρ, and A₀ = κλ² − 2λ + 2.
- **D1** holds iff |Q(λ−iω)| ≤ Q(λ) for all λ, ω > 0.
- Equivalently P̃(λ,W) ≥ 0 for λ, W = ω² > 0, where
  P̃(λ,W) = A₀²(3λ⁴ + 3λ²W + W²) + λ⁶(−2κ²λ² + 4κλ + 4κ − 4 − κ²W).
- The exact κ_cos is the value at which the following has a double root λ* > 0:
  D(λ,κ) = 3A₀⁴ + 16(κλ + κ − 1)λ²A₀² − 2κ²λ⁴A₀² − κ⁴λ⁸ (degree 7 in λ).
- So v_cos = (1 − κ)/κ is algebraic, a root of the discriminant of D in λ. I have not computed the minimal polynomial.
- Hand checks at κ = 0.832708, λ* = 2.7105, ω* = 2.8079:
  - Q(λ*) = 0.135420 and |Q| = 0.135423, with arg = 0.3364 ≈ φ.
  - The W-vertex is 7.8849, against ω*² = 7.8845.
  - D(λ*, κ) ≈ −0.03, where the individual terms are about 1.8e3.
- **D2** holds iff Q(λ₁+δ−iω)/Q(λ₁) lies in conv{e^{(−δ+iω)t} : t ∈ [0,∞]}, the convex hull of a log-spiral.

**H4. D2 is the crux.**
- **Parameters:** three transcendental ones, δ/λ₁, ω/λ₁ and t*·λ₁, with t* ∈ [0, t₁(δ,ω)]; t₁ is the chord-tangency point of the hull.
- **Tight point:** one, on the δ = 0 boundary.
- **Local checks at the optimum:**
  - In the primal form, d ln(1+SCV)/dδ = +0.17.
  - In the dual form, Re(Q′/Q) = −0.1745, against the required ≤ −0.1198.
  - Both are locally consistent with the conjecture.
- **Tails:**
  - ω→0 gives a double real pole with Δ₃ slack.
  - ω→∞ and δ→∞ send SCV → 1.
  - t* = 0 is the CM2003 Eq. 42 family, whose minimum is 1/4 at δ = 0.
- No known analytic positivity theorem covers D2. A full proof needs either a new comparison lemma in δ or a certified interval branch-and-bound with analytic tails and a local lemma at the interface. Feasibility within the run is UNKNOWN; do not assume it is tractable.

## Controls and hazards

Every claimed proof or counterexample must reproduce these. The values marked as mine are hand derivations, not literature figures.

| Control | Expected value | Source |
|---|---|---|
| PH(3) | ≥ 1/3 | Aldous–Shepp |
| Real poles | 0.276583 | ERT/HBT table; Battagliola–Peralta 2608 m = 1 |
| f(0) = 0 subfamily (constant numerator) | ≥ 1/4 | my derivation |
| Atom at 0 | raises SCV | my derivation |
| Literal HSTZ eq. (4) with Table 2 values | about 1.58, so must be rejected | my derivation |

Any counterexample must also certify nonnegativity everywhere, including the tail of the dominant term and a neighbourhood of the touching point.

## Significance

The three axes are separate.
- **Correctness of the value:** numerically robust. It appears in sources from 2006, 2009, 2011 and 2016, and my hand check at the published optimum reproduces it.
- **Status:** open in every primary source I found.
- **Significance:** a proof would be the first exact minimum SCV for ME(n) with n ≥ 3, settling a 2006 conjecture at its first nontrivial order. That is a specialist result, with use in numerical inverse Laplace transforms.

## First obligation and stop rule

**First obligation.**
1. Compute κ_cos exactly from D(λ, κ): find the root and an isolating interval.
2. Certify P̃ ≥ 0 on the open quadrant (D1) with an exact certificate.
3. Cross-check the primal SCV at the optimum to at least 12 digits.
4. In the same chunk, write H1 and H2 and the local D2 lemma at the interface.

The gate is the global D2 bound.

**Stop rule.** Stop immediately on any of:
- a priority hit, especially new Peralta or Battagliola work;
- a certified counterexample (then switch to disproof verification);
- v_cos differing from the 0.20090144–0.20090185 band implied by the published 4.97756, which would mean a convention error.

If D2 cannot be covered by written boxes plus tail lemmas by the parent's checkpoint (about 6 worker-hours), stop and report D1 and the real-pole results as **partial, not gate**.

## CM2003 Problem 5

- **Statement** (printed p.577): "Consider a PH-distribution whose Laplace transform is f̃(s) = p(s)/q(s), where p(s) has degree two and q(s) degree three. Under which conditions (besides condition (43)) has this distribution an order 3 representation?"
- **It is decided by two prior results:**
  - He–Zhang 2005: every PH(3) distribution has an order-3 unicyclic representation.
  - [Horváth–Telek 2007](https://webspn.hit.bme.hu/~telek/cikkek/horv07b.pdf), EPEW, LNCS 4748. Their explicit canonical transformation works from any representation: "If the procedure exits with one of the error messages then the input does not represent a PH(3) distribution." Its checks are a₂² − 3a₁ ≥ 0, which is equivalent to (43), plus f(0), the γ₂ ≤ γ_u bound and π₃ ≥ 0.
- **General case:** [Liu–Yao–Zhang](https://arxiv.org/abs/2409.12673) (Adv. Appl. Probab. 2025) give an iff condition for order equal to algebraic degree, via a nonconvex quadratic program.
- CM2003 itself says the discrete-time version was solved by Anderson et al. 1996.

## Gaps and search log

**Not read:**
- Bladt–Nielsen 2017 book, ME chapter.
- Horváth–Telek 2024 Wiley book, Ch. 4 (paywalled; it cites HSTZ).
- Fackrell 2003 thesis and Bean–Fackrell–Taylor 2008.
- Google Scholar, CNKI and MathSciNet were not searched.

**Searched, nothing relevant beyond the sources above:**
- OpenAlex citers of HSTZ (15) and ASMTA 2009 (8), by title.
- OpenAlex full-text search for "0.200902" (6 hits).
- arXiv API: subject queries, the newest October 2026 entries, and Peralta/Battagliola author listings.
- DataCite, three queries.
- Telek's publication list (updated Nov 2025).

I wrote no files and ran no code. All numbers labelled hand or UNTRUSTED come from paper derivations only.

**Local files:**
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/phase-type-complex3-intake-v1/commault-mocanu-2003.pdf` (p.13 holds Problem 5)
- `…/phase-type-complex3-intake-v1/images/book-560.png` (book p.544)
- `…/screening/math-1-phase-type-complex3-screen-v1.md` (the earlier light screen; its alternate #3 is this target)
- `/Users/jinleic/jinleic-workspace/research-institute/explorer/inventory/math.json` (~line 3277)
