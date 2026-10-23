<!-- Parent capture 2026-10-18T01:37:23-07:00 of Ph3PostPriority; unverified scout report except separately recorded parent primary checks. -->

NONE-FOUND-IN-SCOPE

I found no source that proves or disproves Commault–Mocanu 2003 Conjecture 1 for all a>c>0, b>0 in continuous time. This is a bounded search with access holes, so a miss is not evidence of novelty. Nothing equivalent turned up, so there was nothing to escalate mid-run. Three partial overlaps matter for the write-up:

- **The eigenvalue-placement step is already published.** Verbeken–Ginis (arXiv 2606.10143, 2026) characterise all spectra of n-cycle-with-loops matrices. Their angle reduction is identical to the candidate's: Σθ=2π, ∏sin(θ+φ)=sinⁿφ, m=−β·cot θ. They have no input/exit vectors and no transfer function, so the exit-positivity step is not covered.
- **One boundary line follows from a 1999/2004 discrete-time example** (my derivation). For b=a−c (β=1, n*=4), a standard shift turns Benvenuti–Farina's realization of 1/((z−1)(z²+1)) by the 4-cycle into an order-4 realization of the target. The candidate's construction reduces to exactly this case.
- **The only continuous-time order-m construction I found excludes this whole family.** Kim–Ryou 2012 build order-m realizations only when the complex residue is small, and every member of this family violates that condition.

## Evidence by question

**Q1. Is the construction, or an equivalent, already known?**

| Source (date, version) | Quote (≤40 words) | Bearing on the target |
|---|---|---|
| Verbeken & Ginis, [arXiv:2606.10143](https://arxiv.org/abs/2606.10143), v1 2026-06-08; read v2 2026-09-14 | "For every n≥3, we determine the union of the spectra of row-stochastic matrices supported on a directed n-cycle with self-loops and strictly positive cycle edges." Cor. 8.3: "If ω > d cot(π/n), then c_min(ν) = +∞." | Eq. (2.4) α(u)=a−b·cot u and (2.5) log(sin M/sin(M−u)) match the candidate's angle conditions with λ=iβ, M=π−φ, k=1. M−I is diagonally similar to their ring generator with rates 1−mᵢ (my derivation). They state: "the reconstruction does not prescribe the rest of the spectrum." A search found no transfer-function, exit-vector or phase-type content. |
| Vagenende et al., [arXiv:2605.06743](https://arxiv.org/abs/2605.06743), 2026-05-07 | the 4-cycle spectral region is "exactly and explicitly determined" | Same angle mechanism for n=4. Spectral only. |
| Kim & Ryou, ICINCO 2012, [PDF](https://www.scitepress.org/Papers/2012/39814/39814.pdf), doi:10.5220/0003981405660569 | "an efficient and general algorithm of positive realization for positive continuous-time linear systems in the case of transfer function with (multiple) real or complex poles." Also: "Some of theorems in paper were only mentioned without detail proof" | Thms 3.1–3.2: order m under an angle condition (extraction garbled; it looks like the order-m sector) plus \|β₁\| ≤ β₀/2. For this family f(0)=f′(0)=0 forces \|β₁\| = (R/2)√(1+((a−c)/b)²) > R/2, so the condition fails for every member (my derivation). |
| Horváth & Telek, [arXiv:1502.00521](https://arxiv.org/abs/1502.00521) v1, 2015 | "each pair of complex conjugate eigenvalues is represented with at least 3 phases" | Feedback-Erlang block length ⌈2π/(π−2·arctan(b/(a−c)))⌉ equals n* (for n*≥3), plus a separate block for −c, plus an Erlang tail. Total ≥ n*+1 (inference). |
| Kim 2016, JKSIAM 20(3):225–242, [record](https://koreascience.or.kr/article/JAKO201628663266949.page) | "Our objective is to find an HFCB representation with possibly lower order, including all the eigenvalues of the original generator." | Numerical nonlinear program. HFCB (hypo-feedback-Coxian block) appears to be the candidate's structural class (inferred from the name). **Full text unread.** |
| Taghavian & Sjölund, [arXiv:2502.21102](https://arxiv.org/abs/2502.21102) v3, 2025-09-03 | "all third-order systems with complex conjugate poles, where: (i) the pole angles are rational multiples of π and (ii) the pole magnitudes are large enough" | Discrete time. After the continuous→discrete shift the pole angle tends to 0, so their dimension m grows without bound. Does not cover the target (inference). |
| Benvenuti–Farina tutorial, IEEE TAC 2004, [author copy](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf), Ex. 7 | "all the 4–th roots of unity must belong to the spectrum of the matrix A₊ of any positive realization" | Discrete H=1/((z−1)(z²+1)), realized by the 4-cycle with b=e₁, c=(0,0,1,1). Gives the β=1 boundary line above. |
| Pulungan 2011, [PDF](https://pulungan.staff.ugm.ac.id/pubs/P-SEAMS-11.pdf) | "For the general phase-type distributions, the problem is still open." | Status as of 2011. |
| Johnson–Paparella, [arXiv:1611.06970](https://arxiv.org/abs/1611.06970); Chruściński et al., J. Phys. A 2026, doi:10.1088/1751-8121/ae58d2 | Karpelevič arcs "realized by a single, somewhat simple, parametrized stochastic matrix" | Single-eigenvalue (spectral) results only. |
| Mocanu 1999 thesis, [HAL tel-05023365](https://hal.science/tel-05023365v1) (online 2025-04-07, flagged open access) | "the definition of a class of representations with a reduced number of parameters and the proof that any phase-type distribution accepts such a representation" | The abstract makes no minimality claim. The PDF route returned HTML to my fetcher. |

**Q2. Commault's POSTA chapter and O'Cinneide 1999**

- **Commault 2004.** Exact title "Linear Positive Systems and Phase-type Representations", LNCIS 294, pp. 281–288, doi:[10.1007/978-3-540-44928-7_38](https://link.springer.com/chapter/10.1007/978-3-540-44928-7_38). The Springer page shows "First Online: 01 January 2004" and "Published: 30 April 2004".
  - Abstract: "The representation problem which consists of finding a Markov chain associated with some phase-type distribution is a positive realization problem. It turns out that this realization problem may be seen as concerning a large class of positive problems."
  - The abstract does not mention Conjecture 1. I could not read the full text, so whether the chapter restates it is unverified.
  - Crossref deposits no reference list. Its six OpenAlex citers (He–Zhang 2005/2006, ICNSC 2007, 2008, 2018) do not resolve the conjecture, judging by titles; He–Zhang 2005 was read.
- **O'Cinneide 1999.** Stochastic Models 15(4):731–757, doi:10.1080/15326349908807560. Abstract ([Pollett UQ page](https://people.smp.uq.edu.au/PhilipPollett/papers/colm.html)): "The paper describes some conjectures concerning these distributions. Some partial proofs and other evidence are offered in support of the conjectures." I found no lawful full text.
  - Secondhand, via [He–Zhang 2005](https://www.engineering.uwaterloo.ca/~q7he/Z_PDF_PS_Published/2005_SM_Unicyclic_HE_Zhang.pdf): "Conjecture 4 in O'Cinneide states 'Every phase-type distribution of order m has a unicyclic representation of order m.' Next, we present a counterexample." He–Zhang show it is false at order 6 and true at order 3.
  - Commault–Mocanu 2003 calls the paper "complementary" and does not attribute Conjecture 1 to it.
  - O'Cinneide 1999 predates 2003, so it cannot list this conjecture or its resolution. Whether it poses an equivalent question is unverified.

**Q3. Benvenuti & Farina 1999** (SCL 36(4):261–266, doi:10.1016/S0167-6911(98)00098-X; ScienceDirect returned 403, so I relied on two later papers by the same author)

- **It is discrete-time.** The tutorial says: "It has been shown (see [119]) that for any m, the minimal positive realization of H(z; m) is of dimension N(m) = 2^{m+1}". Here H(z;m)=1/((z−1)(z^{2^m}+1)).
- The 2022 survey adds: "the same result has been proved for a transfer function with three positive real poles in (Benvenuti & Farina, 1999)".
- The mechanisms are dominant poles on the unit circle and zero impulse-response samples. The survey notes that results relying on non-negative-matrix properties "cannot be directly extended to the continuous-time case."
- **It does not give the exact minimal dimension for this family.** Only its m=1 member maps, after the shift, onto the β=1 boundary line.

**Q4. Later citers of Commault–Mocanu 2003.** None states or solves Conjecture 1.

- **Maia, [arXiv:1911.12826](https://arxiv.org/abs/1911.12826) v1.** The paper cites it only once: "the lower bound 14 was presented before using a completely different approach in [11]". The paper works with acyclic generalised Cox structures and moment matching.
- **SIMAX 2024**, doi:10.1137/23m1547305 (read [arXiv:2409.09034](https://arxiv.org/abs/2409.09034) v1). Quote: "even the simple case in which the elements are real and distinct is still challenging, see, e.g., [8, 19]." It is discrete-time with real, distinct eigenvalues; the complex case is left as future work.
- **Bull. Math. Biol. 87:11** (online 2024-12-03; read [arXiv:2311.03593](https://arxiv.org/abs/2311.03593) v2). It cites the paper for definitions and for "Proposition 2. A multi-exponential phase-type distribution with N exponentials can be represented by a Markov chain model of order N". Real eigenvalues only.

## Equivalence table

Target: c(a²+b²)/((s+c)((s+a)²+b²)), a>c>0, b>0, all n*≥4, continuous time.

| Result | Hypotheses | Conclusion | Covers target? |
|---|---|---|---|
| Thm 14 of CM2003 (Commault–Chemla 1996) | eq. 42, a,b,c ≥ 0 | order 3 iff b ≤ (a−c)/√3 | n*=3 only |
| Thm 6 (Dmitriev–Dynkin) | any PH generator | b/(a−c) ≤ cot(π/n) | lower bound only |
| Mocanu 1999 | this family | order n*+1 | no |
| Horváth–Telek 2015 | dominant-eigenvalue and positive-density conditions | feedback-Erlang blocks + Erlang tail | no (≥ n*+1) |
| Kim–Ryou 2012 | sector condition and \|β₁\| ≤ β₀/2 | order m | no (residue condition always fails) |
| Verbeken–Ginis 2026 | one eigenvalue; n-cycle with loops | realizable iff ω ≤ d·cot(π/n) | spectral step only |
| Tutorial Ex. 7 / BF1999 with m=1 (discrete) | poles {1, ±i}, constant numerator | minimal dimension 4 | only the line b=a−c (my derivation) |
| Discrete polygon results (Benvenuti–Farina–Anderson 1999, Nagy–Matolcsi–Szilvási 2007, Czaja–Jaming–Matolcsi 2008, Benvenuti 2020b) | polygon plus small residue | dimension N | no |
| He–Zhang 2005 | PH order 3 | unicyclic of order 3 | n*=3 only |
| Kim 2016 | any PH representation | numerical HFCB | unknown (unread) |

## What is new compared with the pre-result screen
1. The Verbeken–Ginis overlap on the spectral step.
2. Kim–Ryou 2012, and the proof that its residue condition always fails.
3. The β=1 boundary line obtained by shifting the discrete-time example.
4. Mocanu's thesis is now listed as open access on HAL.
5. The text of O'Cinneide's Conjecture 4.
6. The POSTA chapter's title and abstract.
7. All three Q4 citers read.
8. Topic sweeps of DataCite and arXiv found only unrelated items (arXiv 2609.14623; Zenodo 23217139).

## Access holes
- Full text of the POSTA chapter: the Springer preview would not parse and its .pdf variant returned 404; DBLP showed a bot wall; the Google Books API returned 429.
- O'Cinneide 1999: Taylor & Francis paywall.
- Benvenuti & Farina 1999 primary text: ScienceDirect returned 403.
- Mocanu thesis PDF: HAL returned HTML instead of the PDF.
- Kim 2016 full text: three koreascience fetches aborted, and the KSIAM S3 issue link returned 404.
- Kim 2013 (MPE) and Kim 2015 (AAA): Hindawi/Wiley returned 403.
- Kim 2012 (SCL): no abstract available.
- Published versions of the SIMAX and Bull. Math. Biol. papers: I read the arXiv versions.
- The 2024 Wiley book "Phase Type Distributions": 403.
- I did not compare Verbeken–Ginis v1 against v2.
- CNKI and Google Scholar were not searched.

The write-up should cite Verbeken–Ginis for the eigenvalue step and the 2004 tutorial's Example 7 for the β=1 case. The remaining candidate contribution is exit-coefficient positivity at m* for interior parameters; I found no source for it. I wrote no files and ran no code.
