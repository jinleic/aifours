<!-- Parent capture 2026-10-18T00:49:51-07:00 of read-only scout Ph3Priority (bounded screen; access holes listed; a miss is not novelty). Commissioned after the freeze, before any worker result; it covers the untrusted candidate construction class. -->

**NONE-FOUND-IN-SCOPE.** I found no source, current to 2026-10-18, that proves or disproves Commault–Mocanu 2003 Conjecture 1 in continuous time. I also found no earlier construction equivalent to an all-n order-n* representation. This is a bounded search with access holes, so it is not a priority claim. No prior equivalent turned up, so there was nothing to escalate to the parent mid-run.

## Target as frozen (checked against the pinned PDF)
- **Eq. 42:** q(s)=(1+s/c)(1+s/(a+ib))(1+s/(a−ib)) and f̃=1/q.
- **Theorem 14 (Commault–Chemla 1996):** order 3 exists iff b ≤ (a−c)/√3. The PDF states the hypothesis as a,b,c ≥ 0.
- **p.13:** "Conjecture 1: There exists a representation of order n_min for such a distribution. In Mocanu (1999) it is only proved that we can obtain a representation of order (n_min + 1)."
- **Proposition 1 (p.6)** supplies the contract's lower-bound step: "For any irreducible positive realization… the eigenvalue of A with maximal real part is the pole of maximal real part."
- **Current state:** the lower bound is n* (Theorem 6). The best upper bound reported is n*+1, from Mocanu's 1999 thesis, which I could not read. n* is known to be attained only when n*=3.

## Q1. Latest continuous-time results

| Source (date/version) | Quote ≤40 words | What it covers |
|---|---|---|
| Liu–Yao–Zhang, [arXiv:2409.12673](https://arxiv.org/abs/2409.12673) v2 (2025-02-15); AAP 2025, doi:10.1017/apr.2024.72. Hanqin Zhang co-wrote the book chapter. | "roots of the denominator polynomial are not real while keeping the numerator polynomial to be constant/linear, the minimal PH representation problem becomes much more complicated"; "the current state of affairs is far from solving the minimal PH representation problem." | An iff condition only for order = algebraic degree. Here that means n*=3, which is already known. |
| Benvenuti 2022 survey ([IRIS preprint](https://iris.uniroma1.it/retrieve/e383532e-e8ef-15e8-e053-a505fe0a3de9/Benvenuti_preprint_Minimal_2022.pdf.pdf)) | "The case of third-order transfer functions with a pair of complex poles is open as well." | This sentence is about **discrete time** (H(z), §3.1). The continuous-time §9 lists only real-pole results. Commault–Mocanu 2003 is not cited. |
| Taghavian–Sjölund, [arXiv:2502.21102](https://arxiv.org/abs/2502.21102) (2025) | "all third-order systems with complex conjugate poles, where: (i) the pole angles are rational multiples of π and (ii) the pole magnitudes are large enough" | Discrete time only. In the continuous-time shift limit the normalized pole angles go to 0, so this does not apply [INFERENCE]. |
| Sun–Yu–Wang, ICNSC 2007 (continuous time) | "provide conditions for these systems to have positive realizations of the same order" | Order 3 only. |
| Sun–Yu–Yu–Wang, POSTA 2006 (LNCIS 341:327–334) | Survey's description: sufficient conditions for a (minimal) third-order realization | Third-order realizations; it cites Karpelevich, so it is likely discrete-time [INFERENCE; full text unread]. |
| O'Cinneide, [2017 Neuts lecture slides](https://higherlogicdownload.s3.amazonaws.com/INFORMS/50069173-2ea8-479b-baa7-2071ed7cd5dc/UploadedImages/2017-Marcel_Neuts_Lecture_.pdf) | "The only distribution represented by G is the exponential distribution of rate λ." | The circulant "canonical core" for a real pole −λ plus a complex pole ζ is a device in the characterization proof, not an order-n* representation of this transform. The conjectures slide cites Commault–Mocanu 2003 but gives no status for Conjecture 1. |

I scanned the OpenAlex citer titles for Commault–Mocanu 2003 (55), Commault–Chemla 1996 (28), Mocanu–Commault 1999 (45) and He–Zhang 2005 (25), and read the closest items above. None addresses Conjecture 1.

## Q2. Do any theorems cover this family or the one-cycle form?

| Result | What it gives for this family | Proves Conjecture 1? |
|---|---|---|
| Commault–Chemla 1996 / Theorem 14 | n*=3 only | No |
| Theorem 6 (Dmitriev–Dynkin; O'Cinneide 1991) | Lower bound n ≥ n* | Lower bound only |
| Mocanu–Commault 1999 mixture of monocyclic Erlangs; Mocanu thesis | n*+1 | No |
| He–Zhang 2005 ([author copy](https://www.engineering.uwaterloo.ca/~q7he/Z_PDF_PS_Published/2005_SM_Unicyclic_HE_Zhang.pdf)): "a counterexample to the conjecture that every PH-representation has an equivalent unicyclic representation of the same order… the conjecture holds if the order… is 3." The general case uses a nonlinear program. | Order 3 only | No |
| Benvenuti–Farina–Anderson 1999; Czaja–Jaming–Matolcsi 2008, Thm 2.2: "If all c_j s are sufficiently small then H(z) admits a positive realization of dimension N"; Benvenuti 2020b Thm 11 (polygon plus residue condition) | Discrete time. The condition requires a small complex residue, which this family violates (derivation below). | No [INFERENCE] |
| Kim 2013 (MPE, continuous time, multiple complex poles): "A sufficient condition… is analyzed" | Sparse realizations, no minimality claim (abstract only) | No |
| Liu Zhaobo, Zenodo 2026 | Discrete-time complexity (∃ℝ) | No |

**Why the discrete-time results don't transfer.** A Metzler A has A+λI ≥ 0 for large λ. So the continuous-time minimal dimension equals the discrete-time minimal dimension of H(z−λ) for large λ, and residues are unchanged by the shift.

For this family h(0)=h′(0)=0, which forces 2|R| = r₁·√(1+((a−c)/b)²) > r₁. Here r₁ is the residue at the real pole and R the residue at the complex pole. Any residue-dominance hypothesis therefore fails [my INFERENCE]. The survey's rendering of Theorem 11 is garbled, so its exact right-hand side is unverified.

**The one-cycle construction.** After time reversal (eq. 33), the candidate (entry at state 1, single cycle, exits on states 3..n) becomes a unicyclic-type form. O'Cinneide's unicyclic generator is a forward chain whose last state feeds back and is the only exit state; the reversed candidate is that form with feedback to state 1 only [INFERENCE]. So the structural class is known, but I found no theorem giving order n* in that class for this family. I also found nothing using three adjustable diagonals plus n−3 equal diagonals.

## Q3. BuTools and other software
BuTools master [d4be9d1](https://github.com/ghorvath78/butools/commit/d4be9d1dcd80f028731193cc63003acabc554007) (2016-09-08):
- **`MonocyclicPHFromME`.** It calls `TransformToMonocyclic`, which picks the block size with `while evalimag / evalues[i].real >= 1.0 / math.tan(math.pi/n): n += 1`. That measures |Im|/|Re| from the origin, not from −c. The docstring says "Note that M>N if there are complex eigenvalues." `ExtendToMarkovian` then appends an Erlang tail. No minimality claim is made.
- **What that means here [INFERENCE from the code, not run].** The feedback-Erlang block's dominant eigenvalue is −(a − b·tan(π/n)), which dominates −c whenever n < n*. That branch therefore cannot produce a valid representation (Proposition 1). On valid branches the size is 1 + n + tail ≥ n*+1. So the routine never returns n* when n* ≥ 4.
- **`PHFromME`.** The BuTools paper ([horv19z](http://webspn.hit.bme.hu/~telek/cikkek/horv19z.pdf)) says it works "by applying elementary similarity transformations iteratively (note however, that this function is not able to increase the order…)". The underlying `FindMarkovianRepresentation` is greedy: "If not found, the closest one is returned."
- **Other routines.** `MinimalRepFromME` gives the minimal ME representation (not Markovian), and `CanonicalFromPH3` only accepts PH(3) inputs.
- **Horváth–Telek, ValueTools 2014:** "The minimal Markovian representation of PH distributions is an open research problem… We report examples when the obtained representation is larger than the minimal."
- I did not inspect matrixdist, PhaseTypeR, mapfit, jPhase, LINE or KPC-Toolbox.

## Q4. DataCite, Zenodo and arXiv
- **Liu Zhaobo**, 10.5281/zenodo.23272770 (registered 2026-10-10T02:16:26Z): "computational complexity of minimal positive realization for discrete-time linear systems". Not this problem.
- **Nowicki and "Eve Artificial Hyperintelligence"**, SERAPHIEL, 10.5281/zenodo.23042990 (2026-09-29T17:54:02Z): positive-semidefinite matrix realizations, a different notion.
- **Named families.** A topic-filtered query for Kirtchakov, Raval, Ferudun, Gippini, Sadhu, Vos, Long, Nowicki and Liu found nothing else on PH or positive realization. Ferudun's 2026-10-15 to 10-18 records are unrelated.
- **Recent "phase-type" titles** on DataCite: none on minimal order.
- **arXiv API** searches returned irrelevant results, which is a gap in the search, not a negative finding.

## Access holes
- Mocanu 1999 thesis: [theses.fr 1999INPG0103](https://theses.fr/api/v1/theses/these/1999INPG0103) marks it "accessible": "non".
- Paywalled or not parsed:
  - Commault's POSTA 2003 chapter (Springer, pp. 281–288; the preview PDF did not parse).
  - The Sun et al. 2006 POSTA chapter.
  - Wang et al., ACC 2004.
  - O'Cinneide 1999.
  - The original Benvenuti 2020b paper.
  - Kim 2012/2013 (HTTP 403).
  - Horváth–Telek 2014 (HTTP 403).
  - Pulungan 2011 (HTTP 403).
- Commault–Mocanu 2003 citers I did not read:
  - arXiv:1911.12826 ("…Minimal Representations").
  - The SIMAX 2024 substochastic inverse eigenvalue paper.
  - Bull. Math. Biol. 2024.
  - Liu–Yao–Zhang, EJC 2023: two distinct poles must both be real, so it doesn't cover this family [INFERENCE].
- Not searched: Google Scholar, CNKI, He's 2014 book.

## Significance
If the untrusted candidate is correct and new, it would settle a published 2003 conjecture for one three-pole, constant-numerator family and give its exact PH order n*. That is a modest specialist result. The book's general question on minimal PH representations stays open, as does Problem 5 (degree-2 numerator).

I wrote no files and ran no code or CLIs.
