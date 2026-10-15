# Primary sources and reading ledger

Search/read date: **2026-10-14 (PT)**. A search result is a lead, not evidence. “Read” below identifies the actual version and sections examined; it does not claim a complete audit of every proof in a paper. Source PDF downloads and conversion commands are recorded in `../evidence/source-receipt.json`; heavy originals remain in `../../../scratch/ai4s-piecewise-lti-approximation/`.

## Book

- 高静怀，《用分段线性时不变系统逼近时变系统的条件与方法》，《10000个科学难题·信息科学卷》，科学出版社，2011，书页467–469，PDF页488–490. Author affiliation printed on p469: 西安交通大学电子与信息工程学院.
- Local original: `/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`.
- Supplied SHA-256: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (source pin supplied by the assignment, not independently rehashed in this worker).
- Read all three images `page-0488.png`–`page-0490.png`. §3 and all three §4 questions transcribed visually in README. `book-excerpt.txt` is the uncorrected extraction, including garbled formulas. Formula evidence comes from images, not the text layer.
- Equations: (1) input-indexed time-varying convolution; (2) propagation integral; (3) `alpha_Q(tau,f)=exp[-pi f tau/Q+i H(pi f tau/Q)]`; (4) Fourier trace model; (5) **approximate**, not exact, Gabor factorization; (6) STFT definition. The printed (3) has no absolute-value bars on f. Positive-frequency/conjugate-extension conventions are therefore stated explicitly in proof §6.

## 1. Regulated functions: primary theorem verified

J. Dieudonné, *Foundations of Modern Analysis*, Academic Press, **1960**, Chapter VII §6, **Theorem (7.6.1), p139**, and p140.

- Primary-text scan (mirror): <http://absinthe.tuxfamily.net/openmathdep/analysis_real/Foundations_of_Modern_Analysis-Dieudonne.pdf>.
- HTTPS failed with certificate-hostname mismatch; HTTP successfully delivered the actual scanned 379-page book, 17,909,883 bytes.
- **Read** the original theorem and complete proof on printed p139 (PDF156), plus p140 (PDF157) including the bounded-variation exercise. Saved theorem images: `dieudonne-theorem-156.png`, `dieudonne-theorem-157.png`.
- Exact result: for a compact interval and **any Banach target**, regulatedness is equivalent to uniform approximation by finite interval-step functions. Step values at partition points may differ from neighboring interval values. The original theorem is pointwise; proof Theorem 2 supplies the essential-norm/operator adaptation.
- What it does not prove directly: arbitrary Lp operator-norm closure, inverse identification, data-driven segmentation, or stochastic stationarity.

## 2. Priestley (1965): primary abstract only

M. B. Priestley, “Evolutionary Spectra and Non-Stationary Processes,” *JRSS B* **27(2), 204–229** (1965), DOI <https://doi.org/10.1111/j.2517-6161.1965.tb01488.x>.

- **Read** publisher-deposited Crossref abstract through DOI. It describes local-energy evolutionary spectra and estimation from one realization **under conditions**.
- Full-text attempts: Wiley DOI page and OUP PDF returned HTTP403; JSTOR <https://www.jstor.org/stable/pdf/2984191.pdf> returned a client challenge. **Full proof text not read [UNVERIFIED]**.
- The spectral representation and distinction from infill asymptotics were additionally read in the primary author review Dahlhaus (2012), pp2–3. We do not attribute any general segmentation iff or optimal finite segmentation theorem to Priestley1965.
- Some downstream bibliographies misprint this reference as volume28 pp228–240; the DOI metadata gives the citation above.

## 3. Dahlhaus (1997), with the author's later full review

R. Dahlhaus, “Fitting Time Series Models to Nonstationary Processes,” *Annals of Statistics* **25(1), 1–37** (1997), DOI <https://doi.org/10.1214/aos/1034276620>.

- **Read** publisher-deposited abstract: minimum-distance estimation, evolutionary representation, misspecification, time-varying AR coefficients.
- Original1997 PDF: Heidelberg <https://archiv.ub.uni-heidelberg.de/volltextserver/21356/1/beitrag.04.pdf> gave an Anubis challenge; Project Euclid PDF gave an access challenge. **Original theorem/proof text not read [UNVERIFIED]**.
- **Read primary author review**: R. Dahlhaus, *Locally Stationary Processes*, arXiv <https://arxiv.org/abs/1109.4174>, full PDF <https://arxiv.org/pdf/1109.4174>, v2 header **3 February2012**. Local text: `dahlhaus2012-extracted.txt`.
- Examined pp2–9: infill asymptotics, triangular arrays, frozen stationary approximants, local bias/variance, segment-length trade-off; pp11–13: retrospective description of1997 block-Whittle results; pp29–34: Assumption4.1, coefficient summability/BV, strengthened O(1/T) approximation and smoothness, equations(62)–(79), Theorem4.3 spectral uniqueness.
- In particular, (79) approximates `A_{t,T}` by `A(t/T,frequency)` at the **same rescaled time**. It is not the stronger assertion that a whole window of width T^-alpha is O(T^-1)-close to one fixed center for arbitrary smooth A.
- These models already make stationary local approximation precise. They do not identify the seismic source/reflectivity factors or make every nonstationary process locally stationary.

## 4. Adak (1998): exact earlier manuscript read, final paper not conflated

S. Adak, “Time-Dependent Spectral Analysis of Nonstationary Time Series,” *JASA* **93(444), 1488–1501** (1998), DOI <https://doi.org/10.1080/01621459.1998.10473808>.

- **Final1998 article:** DOI metadata read; publisher fulltext/abstract page returned403. Final-version proof details **[UNVERIFIED]**.
- **Primary author manuscript read:** Stanford Technical Report478, **May1995**, same title. Repository <https://purl.stanford.edu/yq814sc0753>; PDF <https://stacks.stanford.edu/file/yq814sc0753/yq814sc0753_EFS-NSF-478.pdf>.
- Read image pages corresponding to printed pp1,3–12; especially Definition3.1 on p6, Theorem3.1 and proof pp8–9, tree segmentation/pruning pp10–11 and Theorem4.1. Saved important images `adak-08.png`, `adak-10.png`–`adak-13.png`.
- Theorem3.1's displayed mean-square error bound is obtained by white-noise isometry from its equation(9), a uniform O(N^-1) transfer approximation to the chosen **blockwise fixed** transfer values. We checked that implication. We do **not** infer this strong rate from ordinary Lipschitz local stationarity alone, and do not certify every step connecting the manuscript's special Definition3.1 to equation(9).
- Theorem4.1 is optimal pruning **within the specified binary tree for its stated cost**. It is not a universally minimal segment count for arbitrary interval cuts in operator norm. The empirical/data-driven method must be distinguished from an oracle known-kernel partition.
- Later Ombao author manuscript explicitly discusses limitations of Adak's adaptive-segmentation consistency theory. That is a dated source comparison, not proof of an unresolved2026 problem.

## 5. Ombao et al. (2001): author preprint recovered and read

H. C. Ombao, J. A. Raz, R. von Sachs, B. A. Malow, “Automatic Statistical Analysis of Bivariate Nonstationary Time Series,” *JASA* **96(454), 543–560** (2001), DOI <https://doi.org/10.1198/016214501753168244>.

- Final bibliographic identity verified at institutional record <https://research.dial.uclouvain.be/entities/publication/efc8c96a-be65-4cff-b8c5-4f0de3c80f67>; the record has no attached full text. Publisher final PDF inaccessible. **Final-version differences [UNVERIFIED]**.
- **Primary author preprint read:** **11 May1999**, UCL discussion paper DP9908. Archival index <https://sites.uclouvain.be/IAP-Stat-Phase-V-VI/ISBApub/ISBAdp.html>; linked original <https://sites.uclouvain.be/IAP-Stat-Phase-V-VI/ISBApub/dp1999/dp9908.ps>. Converted with Ghostscript SAFER; extracted text `ombao1999.txt` is saved locally.
- Read §2, Theorem2.1 (printed p6) and complete appendix derivation pp26–27: Lipschitz rescaled transfer, block maximum length M, average coupled MSE O((M/T)^2); ordinary piecewise stationary is included as the no-overlap case. The order is reproduced directly in proof Theorem18, with an explicit constant and the O(1/T) representation discrepancy kept.
- Read §5, Theorem5.1 and Remarks(1)–(6), printed pp14–15: smoothed SLEX periodogram bias/variance under second-order smoothness, M→infinity, M/T→0, frequency bandwidth→0 and M*bandwidth→infinity.
- Crucial scope: Remark(6) explicitly says consistency has been proved **given a fixed segmentation**, and the BBA-selected segmentation case is not established there. We do not turn that1999 caveat into a claim about all later literature.
- Search-lead correction: a search summary mislabeled **DP0141** as this paper. Opening it showed it is **Guo–Dai–Ombao–von Sachs, Smoothing Spline ANOVA** (2001 manuscript). It is not the2001 JASA paper above.
- Related2002 SLEX model: DOI <https://doi.org/10.1023/A:1016130108440>; primary publisher abstract read, full PDF inaccessible. It asserts asymptotic mean-square equivalence of its SLEX and Dahlhaus models, not equality of every finite trace or kernel. No unexamined theorem is imported.

## 6. Davis–Lee–Rodriguez-Yam (2006): primary proposition and limits read

R. A. Davis, T. C. M. Lee, G. A. Rodriguez-Yam, “Structural Break Estimation for Nonstationary Time Series Models,” *JASA* **101(473), 223–239** (2006), DOI <https://doi.org/10.1198/016214505000000745>.

- **Read primary author-hosted PDF** <https://www-stat.ucdavis.edu/~tcmlee/PDFfiles/2006jasa.pdf>. Local text `davis2006-extracted.txt`.
- Read introduction, §2.2 **Proposition1** (printed p225), genetic-search description, and appendix context.
- Proposition1 establishes almost-sure consistency of relative break locations **when the true number of breaks is known**, under the specified segmented AR model, segment separation and bounded AR-order search. The following paragraph explicitly says a proof of consistency for estimated unknown break count is not supplied in this paper.
- The genetic algorithm is a practical optimizer of MDL, not a certified exact optimizer of every instance. Neither Proposition1 nor the simulations solve unconstrained blind segmentation for arbitrary time-varying kernels.

## 7. Margrave et al. (2011), with the book's original2001 source

G. F. Margrave, M. P. Lamoureux, D. C. Henley, “Gabor deconvolution: Estimating reflectivity by nonstationary deconvolution of seismic data,” *Geophysics* **76(3), W15–W30** (2011), DOI <https://doi.org/10.1190/1.3560167>.

- **Read primary publisher-deposited abstract**: explicitly assumes statistically white reflectivity, minimum-phase source and attenuation; Gabor factorization is approximate; smoothing estimates wavelet/attenuation magnitude; phases are then assigned by minimum phase. The2011 full article was not retrieved: detailed theorem/proof claims **[UNVERIFIED]**.
- **Read primary antecedent used by the book**: G. F. Margrave & M. P. Lamoureux, *Gabor deconvolution*, CREWES Research Report13 (2001), <https://www.crewes.org/Documents/ResearchReports/2001/2001-18.pdf>. Local extraction `margrave2001-extracted.txt`; original PDF in scratch.
- Read introduction and the nonstationary model/factorization/deconvolution derivation, PDF pp11–15, equations(29)–(38). It explicitly calls spectral factorization inherently nonunique, notes smoothing bias, and explains division by exponentially small attenuation factors/noise. It gives an asymptotic factorization rather than an arbitrary-kernel segmentation iff.
- These assumptions cannot be silently generalized to the book's unrestricted §3 or to §4's mere “slow”/“fast” amplitude descriptions. Our Gabor remainder (proof Theorem10) is a separate elementary bound, not an attribution to the2011 article.

## 8. Other checked baselines

- H. Ohlsson, L. Ljung, S. Boyd, “Segmentation of ARX-models using sum-of-norms regularization,” *Automatica* (2010), DOI <https://doi.org/10.1016/j.automatica.2010.03.013>. **Read primary author PDF**, especially §§2,3,5: <https://web.stanford.edu/~boyd/papers/pdf/l1_seg.pdf>. Convex penalized ARX regression and sparse parameter changes; known model regressors/tuning parameter; no general waveform-factor identifiability theorem. Penalized optimum differs from minimum number of segments under a deterministic tolerance.
- Y. Tang, C. Kirch, J. E. Lee, R. Meyer, *Bayesian nonparametric spectral analysis of locally stationary processes*, first arXiv posting **21 March2023**, <https://arxiv.org/abs/2303.11561>, full primary manuscript <https://arxiv.org/pdf/2303.11561>. **Read** §§1–3, Assumptions A.1–A.3 and Theorem3.2. It proves posterior sup-norm consistency and L2 contraction under its smooth locally stationary model, positive spectral lower bound and specified prior. Local extraction `tang-et-al-extracted.txt`. A search hit points to a2025 journal DOI, but its final publication/version is **[UNVERIFIED]** here and is not needed for the claim.
- This recent result confirms that spectral inference with guarantees is a developed field, not an untouched general problem. It does not recover the two factors of a single blind seismic convolution or supply a representation-invariant necessary-and-sufficient approximation theorem for all Gaussian covariances.

## Search conclusion

No exact, unrestricted resolution of the entire book question, including its three inverse-problem extensions, was located. This is a bounded literature-search outcome, **not proof that the question is open**. Known-kernel approximation has classical complete answers after a norm and segmentation convention are fixed; statistical and seismic inverse tasks require additional hypotheses that the book does not fix. No claim of new scientific discovery is made.
