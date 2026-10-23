# Minimal phase-type order, one complex pair: pre-freeze screen

Parent capture 2026-10-18T00:23:54-07:00. Mathematics lane1 successor after Tan–Zhou section4(3), not a seventh problem. The source book's BROAD minimal-PH question is not claimed solved by selecting this special family.

## Parent primary reading and corrections

- Parent read the rendered mathematics-volume book pages544–545 (PDF560–561), stored in `phase-type-complex3-intake-v1/images/`. The chapter is *Minimal Representation of Phase-Type Distribution*, Qi-Ming He and Hanqin Zhang. **The open statement is on book page544**, not545 as the scout report says;545 contains references/authors. It asks generally for minimum-order PH representations. This target is a precise published special family, not the entire book question.
- Parent read the rendered Commault–Mocanu2003 PDF page13 (printed577). Equation42 is q(s)=(1+s/c)(1+s/(a+ib))(1+s/(a-ib)); Conjecture1 says a representation of order n_min exists for this distribution. Theorem14 covers order3 iff b≤(a−c)/sqrt(3). The paper reports n_min+1 from Mocanu1999, whose thesis was not read.
- The primary PDF is pinned as `phase-type-complex3-intake-v1/commault-mocanu-2003.pdf`, SHA256 `8db1e4aa330a9d9989cb91498524d9cb0c41a95aa636906ed6e42391d5d70cfb`, from https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf. The mathematics book SHA is in `fetch.json` and books/README.md.
- The scout's cycle/jet construction is an **untrusted candidate**, not evidence or a result. Its simplicity raises prior-art risk. Benvenuti2022's quoted third-order open statement concerns discrete time and must not be represented as direct continuous-time open attestation.
- Pre-freeze verdict: **OPEN-IN-SCOPE / HEADROOM-UNKNOWN**, with elevated folklore/access-hole risk. Primary-source availability is sufficient for a bounded exact attempt; post-result priority screen must include the uninspected BuTools toolbox and inaccessible theses before any novelty claim.
- This intake rendered images with default inherited TMPDIR instead of explicitly setting the owned tmp directory; no temp artifact was observed. The commands' output paths were fresh and confined to the intake dir. Future compiler/render/checker commands must set owned TMPDIR.

## Read-only scout report, verbatim (its proposals remain unreviewed)

**Pick: Commault–Mocanu (2003) Conjecture 1, the minimal phase-type order for distributions with one real pole and one complex pair.** This is the smallest complex-pole case of He & Zhang's book question (book pp. 544–545). No resolution turned up in a bounded search on 2026-10-17/18. That is a search miss, not proof the problem is open.

My own hand derivation suggests an explicit n-state cycle may prove the conjecture for every n. I ran no code and nobody has reviewed it, so it is [INFERENCE]. If it holds, the target is very tractable. It also means someone may already have the result unpublished or unindexed, and it caps the significance at a modest specialist result.

The two alternates are Sun's disjoint-coset conjecture at k = 5 and the order-3 matrix-exponential minimal-cv conjecture. Both are much less certain. The existing dossiers (Kac–Moody, Shor, Artin, semigroup, M-estimator) offer no complete finite case that is eligible and doable in about 18 hours.

## Ranking

| # | Target | What it would settle | Tractable in 18h? | Prior-art kill status |
|---|---|---|---|---|
| **1 (pick)** | Commault–Mocanu Conjecture 1 | The whole 2003 conjecture | High [INFERENCE] | None found; elevated folklore risk |
| 2 | Sun disjoint-coset conjecture, first open group case k = 5 | One new case of a $200 prize conjecture | Uncertain | None found; heavy 2026 Zenodo activity on "Sun's conjectures" |
| 3 | Order-3 matrix-exponential (ME(3)) minimal-cv conjecture | A long-standing numerical conjecture, proved rigorously | Low–moderate | None found; active 2026 group |

## #1 (pick): Commault–Mocanu Conjecture 1

**Exact statement.** Take a > c > 0 and b > 0, and the Laplace transform f̃(s) = [(1+s/c)(1+s/(a+ib))(1+s/(a−ib))]⁻¹. A PH representation (α, T) of order n has:
- α ≥ 0 with α·1 = 1;
- T an n×n matrix with nonnegative off-diagonal entries, T·1 ≤ 0, T nonsingular;
- f̃(s) = α(sI−T)⁻¹(−T·1).

Claim: such a representation exists with order n_min = min{n ≥ 3 : b ≤ (a−c)·cot(π/n)} = ⌈π / arctan((a−c)/b)⌉. A counterexample would be explicit (a, b, c) together with a proof that order n_min is impossible.

**Open attestation.**
- Commault & Mocanu, Int. J. Control 76(6):566–580 (2003), DOI 10.1080/0020717031000114986, §6; [author copy](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf), PDF p. 13: "Conjecture 1: There exists a representation of order n_min for such a distribution. In Mocanu (1999) it is only proved that we can obtain a representation of order (n_min + 1)."
- Book p. 545 (PDF p. 561): "但对一般 PH- 分布 (α, T ), 如何找其最小表示是几十年来人们关注的一个公开问题." ("For a general PH distribution, how to find its minimal representation has been an open problem of interest for decades.")
- Benvenuti, Automatica 143 (2022), [preprint](https://iris.uniroma1.it/retrieve/e383532e-e8ef-15e8-e053-a505fe0a3de9/Benvenuti_preprint_Minimal_2022.pdf): "The case of third-order transfer functions with a pair of complex poles is open as well." This is stated for discrete time; the survey's continuous-time section lists only real-pole results.
- [Pulungan 2011](https://pulungan.staff.ugm.ac.id/pubs/P-SEAMS-11.pdf): "For the general phase-type distributions, the problem is still open."

**Baseline.**
- Lower bound n ≥ n_min: Theorem 6 of the 2003 paper (Dmitriev–Dynkin 1945; O'Cinneide 1991).
- n_min = 3 is solved: Commault–Chemla 1996 give order 3 exactly when b ≤ (a−c)/√3.
- Order n_min + 1 is reported from Mocanu's 1999 thesis (not read).
- The Mocanu–Commault 1999 mixture-of-monocyclic-Erlang construction is sparse but not minimal.
- He–Zhang 2005 handles unicyclic forms at order 3 only.

**Already tried.** Nothing in the repo; this was only screen candidate T2 in `fresh-mathematics-screen.md`. In the literature, the monocyclic, Coxian and unicyclic routes, and Benvenuti's 2020 polygon-plus-residue bound (discrete time; [INFERENCE] it does not cover this all-pole case).

**New representation (first bounded attempt, [INFERENCE]).**
1. Rescale time so a − c = 1 and set x = s + a. Then f̃ ∝ 1/((x−1)(x²+β²)) with β = b/(a−c), so **c drops out**.
2. Find an n×n matrix M with nonnegative off-diagonal entries, α = e₁ and t ≥ 0 such that α(xI−M)⁻¹t is proportional to that function. Then T = M − aI, rescaled by diag(−T⁻¹t) (Theorem 4 of the 2003 paper), is an order-n PH representation for every c > 0.
3. For M, use an n-cycle with diagonal entries m_i = −β·cot θ_i and positive cycle weights. With φ = arctan β, the spectrum is right iff Σθ_i = 2π and ∏ sin(θ_i+φ) = sinⁿφ.
4. Set θ₄ = … = θ_n = ψ := π − 2φ, which puts those diagonal entries at m* = (1−β²)/2. An intermediate-value argument then fixes θ₁, θ₂, θ₃.
5. The exits sit on states 3..n and are Taylor coefficients at m* of h(m) = 1/((1−m)(m²+β²)). Their sign is the sign of cos(ψ/2) − cos((k+3/2)ψ), which is ≥ 0 for every derivative order k ≤ n−4, because ψ < 2π/(n−1).

For n = 4 there is a closed form: diagonal (0, 0, r, −r) with r = √(1−β²), weights with product β², and t = (0, 0, t₃, t₃(1−r)/w₃). On the boundary β = cot(π/n) the uniform cycle works, matching the screen's lead of "exits from two states".

**Hand spot checks only:**
- β = 0.8, n = 4: the characteristic-polynomial identity holds.
- β = 1.2, n = 5: the intermediate-value condition changes sign (+0.438 vs −1.94).
- β = 1.5, n = 6: h, h′ and h″ are all positive at m*.

**Controls and falsification.**
- Exact symbolic check of the n = 4 family as a polynomial identity in β, plus positivity of every entry.
- For n = 5..12 and several β per band (including both ends): certified root-finding for θ₁–θ₃, then exact or interval verification of the Laplace-transform identity and of the PH constraints.
- Negative controls: β just above cot(π/n) must come out infeasible; a perturbed exit rate must give a transform mismatch; a wrong node ordering must produce a negative exit.
- Two independent CLI reviews of the derivative-sign lemma.
- Compute fits easily: one core, under 1 GiB, kilobyte-sized witnesses, no SAT.

**Three axes, kept separate.**
- *Correctness:* unverified hand derivation; the reviews above are the gate.
- *Novelty:* no earlier equivalent found in the bounded screen. The construction's simplicity raises the chance it is folklore or unindexed.
- *Significance:* if correct and new, it fully answers an explicit 2003 conjecture and gives the exact PH order of this family. That is a modest specialist result, not a major one.

**Kill-check log (2026-10-17/18).**

| Source checked | Result |
|---|---|
| OpenAlex works citing the 2003 paper (55), Commault–Chemla 1996 (28), Mocanu–Commault 1999 (45), He–Zhang 2005 (25); closest abstracts read | None addresses Conjecture 1 (He–Zhang is about unicyclic forms) |
| OpenAlex full-text search "Commault + conjecture + phase-type" | 3 unrelated hits |
| DataCite and Zenodo | Zhaobo Liu's 2026-10-10 note on the complexity of minimal positive realization, and the "SERAPHIEL" note (Nowicki with an AI co-author); neither covers it |
| EulerSolve listing (316 papers), openai/math local and remote (719 manuscripts), arXiv API | No hit |
| Benvenuti publication list to 2024, Matolcsi list, O'Cinneide 2017 slides, Dagstuhl 2008 | Nothing settling it |

**Access holes:** He–Zhang 2005 full text; Commault's 2003 POSTA chapter; Mocanu's 1999 thesis; Benvenuti 2020b full text; Chinese literature (CNKI) and Google Scholar; the BuTools toolbox was not inspected. Repeat this screen after any result.

**Contract-ready text (same format as `math-1-tz43-contract.json`).**
- *Target:* prove, for all a > c > 0 and b > 0, that the PH order of f̃ equals n_min. Import the lower bound from Theorem 6. Equivalently, for each n ≥ 4 and β ∈ (cot(π/(n−1)), cot(π/n)], build an order-n representation; or disprove at explicit (a, b, c).
- *Acceptance:* a written all-n proof; parent exact and interval checks plus controls; hostile reviews from both CLI families; a post-result priority audit.
- *Partial results are labelled as such:* n = 4 alone, or finite (n, β) instances.

## #2: Sun's disjoint-coset conjecture, k = 5 for groups

- **Statement:** any 5 pairwise disjoint left cosets of finite-index subgroups contain a pair whose indices have gcd ≥ 5; or one explicit finite counterexample.
- **Attestation:** book p. 106, `/tmp/math10000_full.txt:3938-3940`: "孙智伟的下述猜想远未解决" ("Sun's following conjecture is far from solved").
  - [Sun's 2018 survey](http://maths.nju.edu.cn/~zwsun/CoverGroupCoset.pdf): Zhu "proved the conjecture for k = 3,4 via several sophisticated lemmas."
  - [Prize Problem Ledger PPL 057](https://prizeproblems.org/problems/057/), checked 2026-07-27: $200, open since 2004.
- **Baseline:** Zhu 2008 for groups with k = 3, 4 (arXiv:0807.2207); O'Bryant 2007 for the integers with k ≤ 20; Fornal–Sun arXiv:2607.24655 (2026) gives an asymptotic bound for the integers only.
- **Representation ([INFERENCE], mine):** pass to a finite quotient. A counterexample must fall in one of two cases:
  - all five indices even, pairwise gcds in {2, 4}, at most one divisible by 3 and at most one divisible by 8;
  - at least four odd indices, all divisible by 3 with pairwise gcd 3, and at most one even index.
  Then search permutation groups and attempt a minimal-counterexample argument.
- **Controls:** reproduce k = 3, 4 and the integer cases by brute force.
- **Risks:** the proof idea is unclear and a counterexample is unlikely. GAP availability and disk use are not checked.

## #3: ME(3) minimal coefficient of variation

- **Statement:** the infimum of cv = m₂m₀/m₁² − 1 over order-3 matrix-exponential densities equals the e^{−t}cos² optimum (≈ 0.20090), or there is an ME(3) density below it.
- **Attestation:** [Horváth–Sáfár–Telek–Zámbó 2016](https://math.bme.hu/~safaro/cikkek/osafarepew.pdf): "the cv cannot be less than 0.200902 but the proof of this conjecture is still missing."
- **Baseline:** PH(n) minimum is 1/n; ME(2) = PH(2); numerical results up to order 47; Battagliola–Peralta 2026 (arXiv:2608.29143, 2609.14612) work on subclasses.
- **Method:** pole-type split, touching-point reduction, then interval branch-and-bound.
- **Risks:** a hard semi-infinite global optimization with an active competitor group. It shares an author community with the pick; the status check was lighter (a web search and the two 2026 Battagliola–Peralta abstracts).

## Not eligible

| Dossier | Why not |
|---|---|
| Kac–Moody | Only height extensions remain, which is a numerical gap; an all-height proof needs a new idea; the next candidate degree (4,4,6) has free-Lie dimension 15000, and no defect is expected |
| Shor Q1 | Needs an all-n impossibility proof or n ≥ 1320 |
| Artin Gröbner–Shirshov, other questions | Under-specified and literature-heavy |
| Regular semigroup P1 | Theorem X closed the finite route; the three-D-class search needs paywalled criteria |
| M-estimator | Cui's intended conditions are unspecified |
| Semifilter, dendriform, inverse optimization, Seymour | Answered or claimed elsewhere |
| Herzog–Schönheim, prime-power conjecture, Hajós | Range extensions only |

None of the three candidates overlaps MOQLS7/8, PA19 or CFR(6,21).

## Files
- `institute/runs/six-lane-2026-10-16/screening/fresh-mathematics-screen.md:17-25` — screen T2: the Commault–Mocanu lead and its named prior-art checks.
- `/tmp/math10000_full.txt:18679-18713` — He & Zhang book text. This is a temporary dump; the canonical source is `books/`, PDF pp. 560–561.
- `mathematics/evidence/mathematics-hard-20261015/catalog.md:199` — marks the general p.544 question "not-boundable".
- `mathematics/evidence/mathematics-more-20261014/discrete-screen.md` — Sun conjecture nomination 2.
- `mathematics/kac-moody-serre-relations/README.md:218-238`
- `mathematics/shor-code-finite-completion/README.md`
- `mathematics/regular-semigroup-embedding/README.md:284,385-402`
- `mathematics/artin-group-grobner-shirshov/README.md:104-114`
- `institute/runs/six-lane-2026-10-16/screening/math-1-tz43-contract.json` — contract template.

All paths are under `/Users/jinleic/repos/aifours/` except `/tmp`. I wrote no files and ran nothing.
