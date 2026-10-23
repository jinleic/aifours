# Exact mathematical-physics replacement screen — 2026-10-16 PT

Read-only scout report; eligibility/tractability are provisional. No 2024–2026 explicit primary attestation was found for its strongest proposal.

I'm proposing one strongest target, the 3-colourability of random 5-regular graphs, and one alternative. Neither is from the depolarizing/code/majorization family.

**Summary**
- **Strongest target:** show that a uniformly random 5-regular graph has chromatic number exactly 3 with probability → 1. Díaz, Kaporis, Kemkes, Kirousis, Pérez and Wormald (J. Graph Theory 2009) proved this conditionally, assuming a "Maximum Hypothesis" about a finite optimisation problem. Certifying that hypothesis would settle a named open case; a certified violation would refute the published hypothesis and leave the case open.
- **Physics link:** the question is the zero-temperature 3-state Potts antiferromagnet on the random regular graph. Its book chapter is p0422, the constraint-satisfaction chapter. This is the same article as the earlier random-SAT lane, but the question is a yes/no chromatic number, not better threshold digits.
- **Status:** the latest explicit "open/conditional" statements I could read are from 2013–2022. I found no 2024–2026 primary statement either way.
- **Crowding:** EulerSolve posted a note dated 17 Oct 2026 that uses the same technique on a closely related problem, random lifts of K₅. Scoop risk is high.
- **Alternative:** chromatic number 4 for random 7-regular graphs. The attestation is weaker and the supporting evidence is my own hand arithmetic.
- No files were created or edited, and nothing was computed except by hand.

**Files read**
- `institute/runs/six-lane-2026-10-16/screening/fresh-physics-screen.md`, `outcomes.md`, `screening/parent-primary-leads.json`, `screening/sof-prior-art-collapse.md` (this one requires the EulerSolve screen).
- `physics/README.md`, `physics/PHYSICS_RESELECTION.md`.
- `physics/evidence/physics-hard-20261015/catalog.md` and `catalog.json` (the p0073/p0457/p0488/p0352 dispositions).
- `physics/evidence/physics-hard-20261015/sources/phys-p0422/excerpt.txt:40-54,168-178`: the spin-glass mapping, the interval-arithmetic sentence, and Challenge 5.
- Book PDF pages 108–115, 490–491 and 521–523 (the p0073, p0457, p0488 and p0489 chapters).
- Grep of the repo and the six-lane screens: this target has not been screened before.

**How it fits:** the round's physics slots are all quantum-information work. This target belongs to chapter p0422 but is a different, exact question. No repository folder exists for it yet.

## Strongest target: χ(G(n,5)) = 3, via the Maximum Hypothesis

**What exactly is to be proved.** Show that lim P[χ(G_{n,5}) = 3] = 1 for the uniform simple 5-regular graph on n vertices (n even). The lower bound of 3 is trivial.

The sufficient finite statement is Hypothesis 1.1 of Díaz et al.:
- **The function.** F(n₁,…,n₄) is defined on {n ≥ 0 : n₁+n₂, n₃+n₄, n₁+n₃, n₂+n₄ ≤ 1/3, n₁+n₂+n₃+n₄ ≥ 1/3}. It must have a unique global maximum at (1/9, 1/9, 1/9, 1/9).
- **The inner maximisation.** F(n) is the maximum of F̂(d) = ∏(C(5;s)/dˢ)^{dˢ} · ∏ m^{m/2} over d ≥ 0, subject to Σₛ d^{ij}_s = n^{ij} and the pairing condition m^{ij}_{r,t} = m^{i+r,j+t}_{−r,−t}. Here s runs over the 36 nonnegative integer 2×2 matrices with entry sum 5 and every row and column sum ≥ 1. Indices are mod 3 and r, t ∈ {±1}.
- **A cleaner form (their Lemma 5.3).** Maximise ∏(√m/λ)^m over a 13-dimensional polytope. Here λ solves λ∂Φ/∂λ = m, with Φ = (x+y+z+w)⁵ − (x+y)⁵ − (x+z)⁵ − (y+w)⁵ − (z+w)⁵ + x⁵ + y⁵ + z⁵ + w⁵.
- **Centre values, checked by hand.** λ = 8100^{−1/5} and F(centre) = 5^{5/2}·25/24 ≈ 58.2309.

**Open attestations (verbatim, ≤40 words each)**
- Díaz et al., §1: "the main outstanding open question on the chromatic number of low-degree random regular graphs as follows: is the chromatic number of a 5-regular graph a.a.s. 3?" Theorem 1.1: "Under the Maximum Hypothesis, the chromatic number of G_{n,5} is a.a.s. 3." ([J. Graph Theory 61 (2009) 157–191, DOI 10.1002/jgt.20369](https://doi.org/10.1002/jgt.20369). I read the author preprint via the [Wayback snapshot of 2021-03-15](https://web.archive.org/web/20210315161735/https://users.monash.edu.au/~nwormald/papers/3col.pdf), §§1, 5.1 and 7.)
- Coja-Oghlan, Efthymiou and Hetterich, [arXiv:1308.4287v1](https://arxiv.org/abs/1308.4287) (2013-08-20), §1.3; the JCTB version has DOI 10.1016/j.jctb.2015.09.006: "proved that if a certain four-dimensional optimization problem … attains its maximum at a particular point, then χ(G(n,5)) = 3 w.h.p. Thus, determining χ(G(n,5)) remains an open problem."
- Kang and McDiarmid, [survey draft of 2014-05-13](https://staff.fnwi.uva.nl/j.r.kang/colrgsurvey.pdf), §4: "The conjecture that χ(G_{n,5}) = 3 a.a.s. remains open, but there is some positive evidence for it in [30]."
- Ayre, Coja-Oghlan and Greenhill, [arXiv:1812.09691v4](https://arxiv.org/abs/1812.09691v4) (2021-10-19), §1.1; Combinatorica 42 (2022): the result holds "if a certain optimisation problem attains its maximum at a specific point, for which they provided numerical evidence."

**Status checks and access holes**
- OpenCitations lists 4 citing records and OpenAlex lists 5. The newest is the 2021 Ayre–Coja-Oghlan–Greenhill paper, and none resolves the question.
- Semantic Scholar shows "cited by 11", but I could not list those citations.
- arXiv metadata search for "5-regular" with "colourable/colorable" (56 hits) and "5-regular chromatic" (0 hits) turned up no 3-colourability result.
- The ESA 2005 abstract (LNCS 3669, 215–225) claims 3-colourability "with positive probability". Its body is paywalled and its references include the L-BFGS-B optimiser. The 2009 journal version made the result conditional.
- Zdeborová and Krzakala (2007) cite the 2005 reports as "rigorous results". That citation predates the conditional journal version.
- Not read: the journal body, and the Kemkes–Wormald technical report CORR 2005-22 (its text could not be extracted).

**Prior-art and corpus checks**
- None of the known results covers d = 5:
  - Kemkes–Pérez-Giménez–Wormald (2010) gives only the window {3,4} at d = 5.
  - Coja-Oghlan–Efthymiou–Hetterich applies only for large k.
  - Ayre–Coja-Oghlan–Greenhill gives d₃ = 6, so 3-colourability fails only from d = 6.
  - G(n,4) is already solved by Shi–Wormald.
- EulerSolve's [opg-37656](https://eulersolve.org/papers/opg-37656/) (dated 17 Oct 2026) covers random lifts of K₅, a different degree-4 model. Its text never mentions G(n,5).
- The remote openai/math `CONTENTS.md` has no hit for this problem. Its family 229 is related context only: it claims non-reconstruction for the three-state symmetric channel exactly at the Kesten–Stigum point, which is the regime of 3-colourings on the 4-ary tree. It is an unreviewed AI claim and does not imply colourability.

**Matched baseline**
- Proven: χ(G_{n,5}) ∈ {3,4} a.a.s. (Shi–Wormald 2007, as restated in Díaz et al. §1).
- Conditional: χ = 3 under the hypothesis (Díaz et al. 2009). Their evidence was a 200-step-per-dimension grid that skipped a boundary layer of width 1/1000, a 1/8000 rescan near the centre, and an inner Newton maximisation that relied on "numerically confirmed" concavity.
- Physics: the cavity method predicts 3-colourable. Zdeborová–Krzakala ([arXiv:0704.1269](https://arxiv.org/abs/0704.1269), §III) say 5-regular graphs are "exactly critical since c^reg_RS(3) = 5".

**Book connection (related, not verbatim).** Article p0422, book pp. 422–427 (PDF pp. 455–460), maps CSPs to spin glasses (`excerpt.txt:40-54`). Two passages ask for exactly this kind of computer-assisted proof:
- §4: "许多分析及数学物理中的数值模拟方案通过一些技巧(如区间代数法等)都能够给出一些严格的上下限" ("many numerical schemes in analysis and mathematical physics can give rigorous upper and lower bounds through techniques such as interval arithmetic").
- Challenge 5, p. 426: "…必将极大程度增进对 K-SAT 问题的满足/不满足相变点和其他相变点的上下限的严格计算" ("…would greatly advance the rigorous computation of upper and lower bounds on the SAT/UNSAT and other transition points of K-SAT").

**Why this is a real open claim and not a toy.** It is the original question for random 5-regular graphs. The hypothesis is the only missing step in a refereed conditional proof.

**Endpoints**
- **Positive:** an outward-rounded interval certificate that the maximum is unique at the centre, plus an audit of Díaz et al.'s Lemmas 5.1–5.10 and §6 (the case n ≢ 0 mod 6). This gives χ(G_{n,5}) = 3.
- **Negative:** an explicit rational feasible d with F̂(d) > 5^{5/2}·25/24, certified by interval arithmetic. That refutes the hypothesis, kills this route, leaves the case open, and leaves the ESA 2005 claim unsupported.

**Independent verifier plan**
- Two separately written evaluators: one using the original 324-variable primal form, one using the dual λ-system with Φ.
- Exact anchors to reproduce: |S| = 36, λ*, b_s = C(5;s)/8100, F(centre), and the constant 3¹³5¹³/(7⁶11⁴79²√221) for E[Y²]/(EY)². Also recompute the Lemma 5.8 determinant, because PDF extraction lost its signs.
- The certificate itself: a box log over a fundamental domain of the order-72 symmetry group, plus a ball around the centre on which concavity is certified. A separate checker replays it.
- Negative controls:
  - the ordinary (not locally rainbow) colouring analogue must show a non-central global maximum, as the paper reports;
  - removing one inclusion–exclusion term from Φ, or setting d = 6, must break the result;
  - ±1-ulp perturbations.
- Cross-vendor Codex review of the reduction lemmas.

**First bounded experiment**
1. Reproduce the anchors above.
2. Audit the 2009 concavity assumption: check the slice Hessian of ln G̃ (the per-factor function the paper assumed concave), including the skipped 1/1000 boundary layer.
3. Run a multistart search over the full 13-dimensional polytope without assuming concavity.

What the outcome would change:
- A certified violator refutes the hypothesis.
- A concavity failure alone makes the published numerical evidence unsound.
- Clean results, with a margin of about 0.4% away from the centre (the paper reports values ≤ 58 there, against 58.2309), justify starting the rigorous branch-and-bound.

**Reductions that make it tractable [INFERENCE]**
- The objective separates into 9 copies of one 4-variable function ψ(μ) = Σ μ(½ ln μ − ln λ(μ)), linked only by linear constraints.
- Homogeneity of Φ gives λ(cμ) = c^{1/5}λ(μ), hence ψ(cμ) = cψ(μ) + (3/10)(Σμ)·c ln c. So ψ is convex in the radial direction, which is why the outer 4-dimensional problem is non-concave and needs branch-and-bound.
- The symmetry group is AGL(1,3)² ⋊ Z₂, of order 72.
- The work is bounded but not easy: the log singularities at the boundary and the local ball around the centre need care.

**Main risks**
- **Novelty:** the EulerSolve group is working on adjacent problems. Credit for the reduction belongs to Díaz et al., so a positive result completes a conditional proof rather than standing alone.
- **Correctness:** the optimisation is nested; parts of the source used Maple, some calculations were omitted, and I have not read the journal body.
- **Preference not met:** I found no 2024–2026 primary attestation.

## Alternative: χ(G(n,7)) = 4

**What exactly is to be proved.** Show that lim P[χ(G_{n,7}) = 4] = 1.

The sufficient finite statement [INFERENCE: the proof's other step should hold unchanged, pending audit]:
- φ(M) = −¼ Σ m ln m + (7/2) ln(½ + Σ m²/16), the Achlioptas–Naor function in Kemkes–Pérez-Giménez–Wormald eq. (3.8), must have a unique global maximum on the 4×4 doubly stochastic matrices at J/4.
- Then their §3 argument applies. Its local condition k² − 2k − d + 2 = 3 > 0 holds.

**Open attestations**
- Kemkes–Pérez-Giménez–Wormald [arXiv:0812.2937](https://arxiv.org/abs/0812.2937) (Advances in Mathematics 2010), Theorem 1, leaves χ ∈ {4,5} for d = 7–9.
- Their §3 uses the global bound only under the condition "if d < d_{k−1} := 2(k − 1) log(k − 1)", which is about 6.59 for k = 4.
- Ayre–Coja-Oghlan–Greenhill, Table 1: the second-moment method reaches d = 6 for q = 4, and the lower bound starts at d₄ = 10. Physics predicts 4 for d ≤ 9.
- There is no explicit "open" sentence specifically about d = 7. Shi–Wormald's {4,5} wording comes only from a search snippet; the PDF would not extract.

**Status.** EulerSolve and openai/math have no hit. Prior art and recent work: none found.

**Hand check, not a certificate [INFERENCE]**
- At d = 7 the centre wins on all three symmetric families I tried. The smallest gap is about 0.0025, at t = 0.1 along (1−t)J/4 + tI.
- At d = 8 the point t = ½ gives −0.90774, which beats the centre's −0.91516. So this route cannot reach d = 8.

**Endpoints**
- **Positive:** a 9-dimensional interval certificate, giving χ(G_{n,7}) = 4.
- **Negative:** a certified point that beats the centre. That kills only this route, not the question.

**Verifier plan.** The same two-implementation and replay design as for the main target. As a control, the verifier must reproduce the d = 8 failure.

**First bounded experiment.** A global numerical search over the 4×4 doubly stochastic matrices at d = 7 and d = 7.5.

**Book connection.** The same p0422 Challenge 5.

**Main risks**
- Hidden prior art, for example small-k remarks in Achlioptas–Naor or the Kemkes thesis.
- Possible errors in my hand arithmetic.
- Modest significance.

## Screened and rejected

| Lead | Reason |
|---|---|
| Spin-2 AKLT spectral gap on the square lattice | Open, but not bounded. The 2026 activity ([2605.12184v3](https://arxiv.org/abs/2605.12184v3), [2609.27993v1](https://arxiv.org/abs/2609.27993v1)) is hexagonal-lattice only. |
| Smale's 6th problem, five planar bodies | Claimed for all positive masses by [2610.13100](https://arxiv.org/abs/2610.13100) and [2610.16107](https://arxiv.org/abs/2610.16107) (Oct 2026). |
| Classifying 4×4 Yang–Baxter solutions | Completed ([2411.18685](https://arxiv.org/abs/2411.18685), v6 dated 2026-06-24). |
| Sign alternation of Ising Ursell functions | Proven (Shlosman 1986, restated as eq. (6) of [2207.12247](https://arxiv.org/abs/2207.12247)). |
| Spin-one Haldane gap | Claimed by openai/math family 268. |
| Book chapters p0073 (Lieb/Nagaoka ferromagnetism), p0457 (spin liquids), p0488/p0489/p0491 (3D exact solutions, topological order, quantum chaos), tetrahedron equation | No primary-source finite open target with a checkable endpoint found. |
