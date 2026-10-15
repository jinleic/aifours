I screened all 13 assigned chapters. None of their questions is solved outright by what I found, but two questions look closable with modest work. Neither has novelty cleared, and every proof below is my own derivation that nobody has reviewed. No files were written and no git commands, tests or model CLIs were run. I worked from `/tmp/math10000_full.txt` (book page + 16 = PDF page) and read each chapter's open-question sentences directly.

## Ranked proposals

### #1 GS chapter 问题 3, the trialgebra half (book p83, `/tmp/math10000_full.txt:3203-3204`)

**Exact question:** 「问题 3 分别找出自由 dendriform dialgebra 和 trialgebra 的 Gröbner–Shirshov 基.」 (Find the Gröbner–Shirshov bases of the free dendriform dialgebra and of the free dendriform trialgebra.) The seven trialgebra axioms are at `:3196-3201`.

**Status:**
- The dialgebra half is solved: Chen–Wang 2010 ([arXiv:1009.0185](https://arxiv.org/abs/1009.0185)), with a shorter basis in Madariaga 2013 ([arXiv:1304.5184](https://arxiv.org/abs/1304.5184)).
- I found no Gröbner–Shirshov basis for the free dendriform trialgebra:
  - zbMATH "dendriform trialgebra Shirshov" returns 0 results.
  - zbMATH "tridendriform Gröbner" finds only Zhang–Gao 2019 (Rota–Baxter family algebras; it builds free *commutative* tridendriform family algebras) and a 2012 proceedings volume.
  - Madariaga's paper mentions trialgebras only in passing.
  - [arXiv:2608.19572](https://arxiv.org/abs/2608.19572) (Aug 2026) covers only the two-operation ("disuccessor") case.
- A search miss does not prove the result is unpublished.

**Proof path (my derivation, unreviewed):**
1. Treat the free trialgebra as a nonsymmetric operad with 7 quadratic relations. Choose a path-lexicographic order in which left combs beat right combs and ≻ is the largest operation.
2. The leading terms are then:
   - the 3 left combs with outer ≺: (x≺y)≺z, (x≻y)≺z, (x·y)≺z;
   - the 3 left combs with outer ·: (x≻y)·z, (x≺y)·z, (x·y)·z;
   - and (x≻y)≻z from the third relation.
3. The surviving normal forms are trees in which every node with a non-leaf left child is ≻, and that child is ≺ or ·. Their counting series satisfies $F=x+3xF+2xF^2$, giving 1, 3, 11, 45, 197, 903.
4. These are exactly the little Schröder numbers, which are the dimensions of the free trialgebra (Loday–Ronco 2004, planar rooted trees). Normal forms always span, so equal counts in every arity make them a basis, and the 7 relations form a quadratic Gröbner basis.
5. Two built-in checks:
   - Negative control: choosing a different leading term for the third relation gives 47 normal forms in arity 4 instead of 45, so that choice fails.
   - Positive control: the same method on the dialgebra reproduces the Catalan numbers.
6. Transfer the operad basis to the free trialgebra on a set X using the Bokut–Chen–Huang composition lemma ([arXiv:1005.0118](https://arxiv.org/abs/1005.0118)), as Madariaga did for the dialgebra.

**To verify:**
- Confirm the chosen order is admissible.
- Reduce all arity-4 overlaps explicitly.
- Brute-force the ranks in arity ≤ 6.

**Novelty risk:** the operad-level basis may already be folklore. Check Loday–Ronco 2004, Vallette 2008, and Bremner–Dotsenko 2016 (I could not access the last).

### #2 Prodinger 问题 2 and 问题 3 (book p62, `:2503`, `:2505-2506`)

**Exact questions:**
- 「问题 2 寻找另外的 L ∈ LDF_{X*} (LDSF_{X*}), 使得 R_{X*} = R_L.」 (Find other left-divisible filters or semifilters L for which R_L is exactly the class of regular languages.)
- 「问题 3 令 L1, L2 ∈ LDF_{X*} (LDSF_{X*}). 给出 R_{L1} = R_{L2} 的一个充分必要条件.」 (Give a necessary and sufficient condition for R_{L1} = R_{L2}.)
- Definitions are at `:2457-2495`. Fact 1 (`:2500`, Guo–Wang–Li 1983) says the cofinite filter gives exactly the regular languages.

**Reformulation:** let V = {complements of members of L}. Then:
- L is a semifilter exactly when V is closed under symmetric difference and under left quotients.
- L is a filter exactly when V is also closed under taking subsets.
- x R(T,L) y exactly when x⁻¹T Δ y⁻¹T ∈ V.

**Claimed answers (my derivation, unreviewed):**
- **Decomposition theorem.** R_L consists of the regular languages plus finite mod-2 sums of products R·a·B, where R is regular, a is a letter, B ∈ V, and concatenation counts factorizations mod 2.
  - Proof idea: take a representative x_i for each class and track the error F_x = x⁻¹T Δ x_{[x]}⁻¹T. It satisfies F_{xa} = e([x],a) Δ a⁻¹F_x with each e(i,a) ∈ V, which yields T = T′ + Σ L_i·a·e(i,a).
  - The converse inclusion uses x⁻¹(R·a·B) = (x⁻¹R)·a·B + (a finite sum of quotients of B, all in V).
  - Fact 1 is the special case V = finite sets.
- **Problem 2.**
  - For semifilters: R_L = Reg exactly when every member of L is regular. The largest such semifilter is Reg itself, so a language is regular iff it has finitely many left quotients modulo regular languages.
  - For filters: exactly when L ⊆ CX*, i.e. every member is cofinite. Any infinite complement would contain a non-regular subset.
- **Problem 3.** R_{L1} = R_{L2} exactly when V_{L1} ⊆ R_{L2} and V_{L2} ⊆ R_{L1}. This follows from V ⊆ R_V, monotonicity, and R applied to R_V giving back R_V.
- **Side remark on 问题 4 (general semigroups):** for S = (ℤ,+), the cofinite filter is left-divisible and T = ℕ falls in a single class, yet T is not regular. So Fact 1 fails for general semigroups.

**Lean:** feasible. The cached Mathlib has `Language.IsRegular` and `MyhillNerode.lean` with `leftQuotient`. One extra lemma is needed: a mod-2 product of regular languages is regular.

**Novelty risk is high:**
- The problem's own authors published Guo–Wang–Shum 2010, whose title is literally "characterizing and generalizing regular languages by semifilters". It is blocked (HTTP 403 plus captcha).
- Their 2024 Springer monograph, chapter 3, cites Prodinger 1980 and the 1983 paper (paywalled).
- Guo–Wang–Shum 2017 says it answers "a question proposed in Prodinger 1980"; which question is not identified.

## Not ranked: open with an explicit object, but no credible full-proof path

**Finite-completion 问题 1 (p65, `:2592-2594`):** does Shor's code C = b{1,a,a⁷,a¹³,a¹⁴} ∪ {a³,a⁸}b{1,a²,a⁴,a⁶} ∪ a¹¹b{1,a,a²} have a finite completion?

- **Status:** open.
  - Cordero's 2019 [slides](http://www.normalesup.org/~cordero/Presentations/2019/GdR_IM.pdf) say: "We do not know if it is included in a finite maximal code." Any completion must contain aⁿ with 330 | n, and no factorization of that form is known. Paper: [HAL](https://hal.science/hal-03682699).
  - De Felice 2022 ([arXiv:2202.09675](https://arxiv.org/abs/2202.09675)) calls the triangle conjecture open in general.
  - Cordero 2023 ([arXiv:2301.13566](https://arxiv.org/abs/2301.13566)) proves it only for special n (in particular n < 36).
- **Why it matters:** C has 16 words of maximum length 15. A completion would refute the triangle, factorization and commutative-equivalence conjectures.
- **My refinement (unreviewed):** doubling the a-exponents of the a^k b words creates a clash (2·3 = 6 = 7−1), which forces |L| even. That gives 660 | n and n ≥ 1320.
- **Bounded assay only:** run SAT/exact-cover for factorizations of ℤ_n extending ({0,3,8,11}, {0,1,7,13,14}) for n = 1320, 1980, …. A negative answer would need an argument covering all n, and I know of none.

## Exclusion log

| Chapter / question (line) | Status | Primary source |
|---|---|---|
| Brown p37: are all noetherian Hopf algebras AS-Gorenstein? (`:1635`) | Open | [Brown, arXiv:2605.00774](https://arxiv.org/abs/2605.00774) (May 2026: "remains open after 30 years") |
| Cayley p39 P1, P2 (`:1700`, `:1706`) | Research programmes, not precise | — |
| Cayley P3 (`:1714`) | Literal text is defective: Cay(D₂ₚ, involutions) is bipartite, so its diameter cannot be 2. The intended content is the flag-transitive projective plane conjecture, which is open | [Li 2005 abstract](https://www.ams.org/proc/2005-133-01/S0002-9939-04-07549-5/home.html); [Xia, arXiv:1707.05486](https://arxiv.org/abs/1707.05486) |
| Ramras p49, three questions (`:2039`, `:2053`, `:2055`) | Open; Artin–Tate–Van den Bergh settle dimension ≤ 4 | [Rogalski, arXiv:2307.03174](https://arxiv.org/abs/2307.03174) |
| Smashing p51 (`:2113`) | Open-ended "which categories" question. [INFERENCE] the stable homotopy category fails, since the telescope conjecture is false | [BHLS, arXiv:2310.17459](https://arxiv.org/abs/2310.17459) |
| Codes p60, Conjecture 2 (`:2420`) | Open | [De Felice, arXiv:1611.04580](https://arxiv.org/abs/1611.04580) |
| Codes p60 问题 (`:2423`) | Vague; de Luca 1998 (TCS 204) gives a two-letter reformulation | — |
| Finite completion p65 问题 2: decidability (`:2598`) | Open; partial results only for special n | De Felice 2022; Cordero 2023 Cor. 6.3 |
| Semigroup p62 问题 4, 5 (`:2507`, `:2520`) | Vague programmes | — |
| Fitting p72 (`:2877`) | Open per the book. Robinson 2019 treats metanilpotent groups only; [INFERENCE] the general case is still open | [Crossref record](https://api.crossref.org/works/10.1515/jgth-2018-0210) |
| Smash product semiprimeness p74 (`:2914`) | Open | [Lomp survey, arXiv:1401.1049](https://arxiv.org/abs/1401.1049) |
| Pieri p76 (`:2980-2984`) | Vague; largely addressed by later work | [Lassalle–Schlosser, math/0402127](https://arxiv.org/abs/math/0402127); [BHMPS, arXiv:2307.06517](https://arxiv.org/abs/2307.06517) |
| GS 问题 1 (`:3158`) | Largely solved: Yunus–Gao–Obul 2015 covers all Dynkin types (Algebra Colloq. 22:495), plus E₆, D₄, G₂ papers. B_n and F₄ explicit bases not verified | — |
| GS 问题 2 (`:3176`) | The 3-generator Sklyanin algebra F is handled by [Iyudu–Shkarin, arXiv:1601.00564](https://arxiv.org/abs/1601.00564). Q_{n,m}(E,η) for all n, m is broad and open | — |
| GS 问题 4 (`:3205`) | Solved | [Bokut–Chen–Deng, arXiv:0908.2281](https://arxiv.org/abs/0908.2281); [Chen–Mo, arXiv:1005.2717](https://arxiv.org/abs/1005.2717); Gubarev–Kolesnikov 2013 |
| Witt p224, Aut Wₙ (`:7871`) | Solved: Aut Wₙ ≅ Aut K[x₁,…,xₙ] in characteristic 0 | [Bavula, arXiv:1304.3836](https://arxiv.org/abs/1304.3836); [Kraft–Regeta, arXiv:1402.5012](https://arxiv.org/abs/1402.5012) |
| Rota–Baxter pp492–493 (1)–(3) (`:17063`, `:17073`, `:17082`) | Not precisely posed | — |

## Source-access blockers
- **Semifilter literature (needed to clear #2):**
  - Guo–Wang–Shum 2010 survey: HTTP 403 plus captcha.
  - Guo–Liu–Wang 2024 monograph: paywalled.
  - Guo–Wang–Li 1983: not online.
  - Prodinger 1980: image-only PDF and ScienceDirect 403; I read the zbMATH review instead.
  - Wang–Guo–Xu 2011: 403; zbMATH review read.
  - Guo–Wang–Shum 2017: zbMATH summary only.
- **Li 2005 PAMS:** 403, so I could not confirm which graph invariant P3 intends.
- **Robinson 2019:** blocked by the publisher's bot wall.
- **Kourovka notebook:** a grep of the PDF returned nothing, so it is unchecked.
- **Not opened:** Lam 1997, Restivo–Salemi–Sportelli 1989, Zhang–Shum 2017, and Bremner–Dotsenko 2016.

## Corpus overlaps
- **Local `math/` clone:** no overlap. Grep of `lean/docs` found nothing; grep of `preprints` found only false positives such as "raising operator" or "finite completion" used in other senses.
- **Remote openai/math:** the 7 newer families (027, 066, 075, 103, 137, 195, 301) are unrelated, and the remote `preprints/` directory names show no related titles.