# 用分段线性时不变系统逼近时变系统的条件与方法

**As of 2026-10-14 (PT): the full book problem is not solved here.** Several exact known-system readings have complete classical answers; unrestricted blind recovery is nonidentifiable under the book's qualitative assumptions. This folder contains complete written proofs, primary-source checks and exact finite implementation evidence, not a claim of new mathematics or a Lean-kernel proof.

## 1. Source

- **Chinese title:** 用分段线性时不变系统逼近时变系统的条件与方法.
- **Author:** 高静怀 (西安交通大学电子与信息工程学院).
- **Book:** 《10000个科学难题·信息科学卷》, Science Press, 2011.
- **Pages:** book **467–469**, PDF **488–490**. Page map for this target: PDF = book +21.
- Original PDF: `/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`.
- Assignment-supplied SHA256: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (not independently rehashed by this worker).
- Read all three page images, copied to [`sources/`](sources/). The Chinese questions below were checked visually; formulas were not trusted to the garbled text layer in [`sources/book-excerpt.txt`](sources/book-excerpt.txt).

## 2. Problem

### Verbatim key questions and translation

Book p468, §3:

> 问题可表述为：①当时变系统的输入及系统函数满足哪些条件时，该系统可用分段线性时不变系统逼近？或可表述为时变系统输出的非平稳时间序列在何种条件下可用分段平稳时间序列来逼近？②如何实现有效分段？能否对精度进行估计？

**Translation:** Under what conditions on a time-varying system's input and system function can it be approximated by piecewise linear time-invariant systems? Alternatively, under what conditions can its nonstationary output time series be approximated by piecewise stationary time series? How can effective segmentation be carried out, and can the accuracy be estimated?

Book p468, §4, in full:

> （1）如果已知构成时变系统的入射在每个波阻抗界面上的子波的傅里叶振幅谱随频率缓变，而反射系数序列的傅里叶振幅谱随频率快变，能否从非平稳时间序列中把子波的振幅影响校正掉？
>
> （2）若地表处（对应于时变系统初始时刻）子波已知，该信息对把非平稳序列划分为逐段平稳序列有何帮助？
>
> （3）利用分段得到的逐段平稳序列能否近似估计介质中地层Q值？

**Translation:** (1) If the wavelet amplitude spectra at the interfaces vary slowly with frequency while the reflectivity amplitude spectrum varies rapidly, can the wavelet amplitude effect be corrected from the nonstationary series? (2) How does knowing the surface/initial-time wavelet help divide the record into successively stationary pieces? (3) Can the resulting pieces be used to estimate the strata's Q values approximately?

### Exact model and the ambiguity that must be retained

The book's equation(1) is

\[
 (T_wr)(t)=\int_I w(\tau,t-\tau)r(\tau)d\tau.
\]

Write \(w_\tau(u)=w(\tau,u)\). **Freezing the input index** produces
\(T_s r=\sum_jh_j*(r1_{I_j})\). **Freezing the output index** produces
\(\sum_j1_{J_j}(h_j*r)\). They are not the same operator. With white-noise input, exact input-piecewise LTI need not give exact within-piece stationary output; memory produces boundary transitions. Counterexample13 proves this, but does **not** refute an unspecified equivalence of arbitrary-accuracy approximation properties.

The book specifies neither a norm nor a statistical asymptotic regime. Its deterministic integral is not itself a stochastic stationarity definition; whiteness appears in its particular Q-model example, and the book warns that those assumptions may fail. We therefore fix, rather than conflate, the following readings.

| Reading | Complete modelling choices and reason for them | Rival readings not silently substituted |
|---|---|---|
| **D: deterministic operator** | Known jointly measurable kernel; Banach-valued filters. Primary exact choice: \(B=L^1(\mathbb R)\), full-line output, \(L^1(I)\to L^1(\mathbb R)\) norm. This is exactly uniform accuracy over unit-mass inputs and exactly equals the essential supremum of column-filter errors. Compact input interval; also whole-line/half-line variants with finite or locally finite partitions. Step filters may be arbitrary centers, not just sampled originals. No extra causality/minimum-phase constraint is imposed by equation(1). \(L^p\), \(L^\infty\), Hilbert–Schmidt and weighted-envelope variants are separately stated. | Exact \(L^2\) or \(L^\infty\) operator closure for every bounded kernel; output truncation; causal/minimum-phase constrained filters; only sample-valued centers; model estimated from data. |
| **I: input-specific** | A fixed known \(r\in L^1(I)\). Weighted kernel error controls \(\|(T_w-T_s)r\|_1\). Also examine the literal weaker requirement of approximating only the one output in \(L^p\), \(1\le p<\infty\), allowing arbitrary \(L^1\) filters. This is justified by the book's explicit mention of the input, but its weakness is demonstrated rather than hidden. | Uniformly bounded gain, physical kernel fidelity, approximation for all possible inputs, or deconvolution when r is unknown. |
| **S: stochastic** | Gaussian white-noise driver with Lebesgue control measure. On a finite output window J, row filter \(g_t(u)=w(t-u,u)\). Output-frozen approximants are stationary Gaussian moving averages within each interval, with cross-piece dependence allowed. (i) Uniform same-driver RMS measures trace fidelity; (ii) uniform covariance metric including diagonal controls every variance and covariance, independently of representation; (iii) \(W_2\) on \(L^2(J)\) and covariance-operator norm control finite-window energy/law and linear measurements. Every metric and moment hypothesis is explicit in proof §7. | Independent blocks; strict stationarity for nonguassian noise from covariance alone; Hellinger distance; a fixed number of segments; enough observations per segment; infill-consistent estimation from one trace. |

For **known-system segmentation**, Theorem4 minimizes segment count for a supplied uniform-error feasibility criterion and gives the minimax-k dynamic program on a finite candidate grid. Continuous longest-prefix optimality is proved for reflexive filter spaces, with exact access to the interval-radius problem. No finite-query algorithm can certify every arbitrary continuous black-box function without a modulus. The finite-grid code is a scalar exact specialization, not an implementation of infinite-dimensional system identification.

For the book's constant-Q equations(2)–(4), finite-band propagation is treated as \(\widehat w_\tau=W_0e^{-\tau a}\), \(\operatorname{Re}a=\pi|f|/Q\). Band, source regularity and phase convention are required. The printed Hilbert-transform phase does not specify its regularization; identification with it is conditional on the explicit phase compatibility in Theorem9. Equation(5)'s Gabor factorization is separately bounded, never declared exact.

## 3. Status as of 2026-10-14

“SOLVED” in this table means **the stated formal reading**, not the full chapter or scientific novelty. “OPEN” means not resolved in this folder/search, not a proven absence of prior work.

| Reading or subreading | Verdict | Exact reason |
|---|---|---|
| D1: known kernel, finite-input uniform \(L^1\to L^1\) approximability; finite/locally finite infinite-horizon variants | **SOLVED-BY-PRIOR-WORK** | Dieudonné(1960) Theorem7.6.1 is read and re-proved; exact column norm identifies the operator problem. Necessary and sufficient: essential \(L^1\)-regulatedness; finite whole-line partitions additionally require limits at both infinities. |
| D2: requested broad collection of all \(L^p\)/\(L^\infty\) operator classes | **PARTIALLY-SOLVED** | Exact endpoint norms, Schur bounds, sharp envelope bounds and complete finite-energy \(L^2\) density theorem proved. No unrestricted operator-closure iff for every bounded \(L^2\) or \(L^\infty\) kernel is supplied. |
| D3: minimum segment count at tolerance and best error for k segments under known filter cost | **SOLVED-HERE**, classical certification | Greedy optimality and Bellman recurrence proved. Actual finite algorithm on candidate grid; continuous attainment/greedy theorem requires reflexive B. Not arbitrary-Banach continuous optimization or a statistical data-only method. |
| I1: fixed-input weighted kernel approximation | **SOLVED-HERE**, classical certification | Bochner integrability with weight \(|r|\) suffices, with constant-one error bound. No regulatedness needed. |
| I2: unrestricted output-only approximation for one fixed input | **SOLVED-HERE**, classical certification | Any nonzero r can approximate any prescribed \(L^p\) output, p<infinity, using at most three input pieces; filters can have diverging gain. Zero r permits only zero output. This proves the reading is too weak for physical identification. |
| I3: stable, faithful or blind input-specific recovery from a record | **PARTIALLY-SOLVED** | Exact ambiguity transformations rule out universal identification from the stated qualitative assumptions; no useful general positive recovery theorem is supplied. |
| S1: known row family, uniform same-driver RMS | **SOLVED-BY-PRIOR-WORK** | Regulated-function theorem plus Itô isometry gives an iff, sharp rates and optimal filter-cost segmentation. No novelty claimed. |
| S2: arbitrary-accuracy uniform covariance approximation, diagonal included, continuous within-piece stationary covariance | **SOLVED-HERE**, classical certification | Theorem12A proves iff row-regulatedness. Necessity uses covariance-induced mean-square distances, not a fixed coupling. No optimal segmentation claim in this metric. |
| S3: finite-energy Gaussian row family, \(W_2(L^2(J))\)/covariance-operator norm | **SOLVED-BY-PRIOR-WORK** | Bochner step density and Itô isometry approximate every such row family; Theorem12B. These weaker metrics do not enforce uniform accuracy. |
| S4: locally stationary triangular arrays with a Lipschitz rescaled transfer | **SOLVED-BY-PRIOR-WORK** for approximation | Ombao author preprint Theorem2.1 read; explicit no-overlap rate reproduced in Theorem18. Statistical adaptive-segmentation guarantees have different hypotheses. |
| Broad output-only segmentation and simultaneous wavelet/reflectivity/Q recovery as posed by the chapter | **PARTIALLY-SOLVED** | Missing identification/noise/regularity assumptions prevent a universal guarantee. Specific bare-assumption recovery assertions are refuted; conditional model-specific statistical problems are not fully settled here. |

### Dated search log

All searches below were performed **2026-10-14**. See [`sources/references.md`](sources/references.md) for URLs, exact versions and access failures.

1. Exact Chinese title and English time-varying/piecewise-LTI/operator-norm variants: no exact full-chapter resolution located; this is **not evidence of openness**.
2. Dieudonné + Banach-valued regulated functions: found a scanned primary book; checked theorem, proof, endpoints and Banach completeness at printed pp139–140. Core uniform-filter characterization predates the2011 book by decades.
3. Priestley1965, Dahlhaus1997, Adak1998, Ombao2001, Davis2006: checked original abstracts/records and available primary manuscripts. Recovered Adak's1995 Stanford scan and Ombao's1999 UCL PostScript rather than treating search summaries as evidence. Read Dahlhaus's2012 primary author review when the original1997 PDF was blocked.
4. Margrave2011 and the book's2001 Gabor source: read primary2011 abstract and primary2001 derivation. Whiteness, minimum phase, smoothing bias, nonuniqueness and approximate factorization are essential caveats.
5. Broader segmentation/prior-art checks: Ohlsson–Ljung–Boyd2010 convex ARX segmentation; recent Tang–Kirch–Lee–Meyer arXiv2303.11561 spectral posterior guarantees. These have substantive model assumptions and do not resolve blind factor separation.
6. Access limits preserved: full Priestley1965, Dahlhaus1997, Adak1998 final version, Ombao2001 final version and Margrave2011 final proof texts were not all obtainable. Their unread proof-level details are **[UNVERIFIED]**, never used as load-bearing imported theorems.

## 4. State of the art

This is a checked baseline map, not a claim that one method is best in every metric.

| Result | Hypotheses / limitation | Primary link and exact location | Read? |
|---|---|---|---|
| Regulated iff uniform step limit | Compact interval, Banach target, pointwise endpoint convention | [Dieudonné1960 scan](http://absinthe.tuxfamily.net/openmathdep/analysis_real/Foundations_of_Modern_Analysis-Dieudonne.pdf), §7.6, Thm7.6.1, p139 | **Original theorem and full proof**; saved images |
| Evolutionary spectra and one-realization estimation | Conditions on nonstationary spectral structure; not all processes | [Priestley1965 DOI](https://doi.org/10.1111/j.2517-6161.1965.tb01488.x) | Primary abstract only; full proof **[UNVERIFIED]** |
| Local stationarity/infill, minimum-distance and block-Whittle estimation | Triangular array and smooth/summable transfer; model identifiability | [Dahlhaus1997 DOI](https://doi.org/10.1214/aos/1034276620); [author2012 review](https://arxiv.org/abs/1109.4174), pp2–13,29–34 | 1997 abstract; relevant2012 primary sections |
| Piecewise-stationary approximation and binary-tree pruning |1995 manuscript Eq9 strong block approximation; pruning within prescribed tree/cost | [Adak1995 TR478](https://purl.stanford.edu/yq814sc0753), Thm3.1 pp8–9, Thm4.1 p11; [1998 DOI](https://doi.org/10.1080/01621459.1998.10473808) | Original1995 theorem/proof images; final1998 differences **[UNVERIFIED]** |
| Auto-SLEX, O((M/T)^2) average coupled approximation | Lipschitz rescaled transfer; fixed-segmentation spectral consistency is not adaptive-BBA consistency | [Ombao1999 author preprint](https://sites.uclouvain.be/IAP-Stat-Phase-V-VI/ISBApub/dp1999/dp9908.ps), Thm2.1 and appendix; §5 Remark6; [2001 DOI](https://doi.org/10.1198/016214501753168244) | Relevant primary preprint theorem/proof and caveat |
| Auto-PARM and relative breakpoint consistency | Piecewise AR, **known true break count** for Prop1; finite separation/order bounds; GA not exact global certificate | [Davis et al.2006 author PDF](https://www-stat.ucdavis.edu/~tcmlee/PDFfiles/2006jasa.pdf), §2.2 Prop1 | Primary proposition, assumptions, limitations |
| Gabor deconvolution | White reflectivity, minimum-phase source/attenuation; approximate factorization and biased smoothing | [Margrave2011 DOI](https://doi.org/10.1190/1.3560167); [2001 primary report](https://www.crewes.org/Documents/ResearchReports/2001/2001-18.pdf), Eqs29–38 | 2011 abstract;2001 derivation |
| Convex sum-of-norms ARX segmentation | Specified regressors/model, regularization parameter; not minimum count at a deterministic kernel tolerance | [Ohlsson et al.2010 author PDF](https://web.stanford.edu/~boyd/papers/pdf/l1_seg.pdf), §2 | Primary method and derivation |
| Bayesian dynamic-Whittle spectral inference | Smooth locally stationary model, spectrum bounded away from zero, specified prior and bandwidth conditions | [Tang et al., arXiv2303.11561](https://arxiv.org/abs/2303.11561), AssumptionsA.1–A.3, Thm3.2 | Primary statement and assumptions; full proof not replayed |

**Verified prior-art caution:** Adak's strong displayed rate follows from its stated blockwise approximation hypothesis, not from generic Lipschitz variation alone. Ombao's known-family approximation rate is separately reproduced with all constants in Theorem18. The final versions of the1998/2001 papers must not be silently equated with their earlier author manuscripts.

## 5. Results

All theorem numbers refer to [`proof.md`](proof.md). **PROVED** here means a complete classical written argument, not Lean certification; independent model review is not human peer review. Novelty is a separate column.

| Claim | Status | FRONTIER label | Novelty / scope |
|---|---|---|---|
| Exact \(L^1\to L^1\) column norm; exact \(L^\infty\to L^\infty\) row norm; Schur \(A^{1/p}D^{1-1/p}\) | **PROVED**, Thm1 | Certification | Classical. Columns alone do not control other norms. |
| Essential-regulated iff; finite versus locally finite infinite horizons | **PROVED**, Thm2–3/Cor2A | Certification; Reproduction of classical core | Dieudonné primary verified; no discovery. |
| Greedy minimal segment count; minimax-k Bellman recurrence | **PROVED**, Thm4 | Certification | Classical hereditary-interval argument; exact-cost access and stated center-attainment hypotheses. |
| Sharp midpoint \(LT/(2k)\), arbitrary-Banach BV \(V/(2k)\), matching affine lower bound | **PROVED**, Thm5 | Certification | No novelty claimed. Arbitrary center filters are essential. |
| Weighted fixed-input density; three-piece output-only approximation | **PROVED**, Thm6–7 | Certification | Elementary; three-piece construction may have exploding gain, not physical inversion. |
| Finite-energy \(L^2\) operator and exact white-noise energy error | **PROVED**, Thm8 | Certification | Hilbert–Schmidt/Itô facts, not exact unrestricted \(L^2\) closure. |
| Constant-Q finite-band O(1/k) bounds, exponential-tail improvement, matching order; explicit \(L^1\) Sobolev constant | **PROVED**, Thm9 | Certification | Conditional on source, band and phase conventions; no blanket physical-model claim. |
| Direct Gabor factorization remainder: variation plus window commutator | **PROVED**, Thm10 | Certification | Classical estimate; not exact Eq5 or an inverse stability theorem. |
| Covariance-operator and finite-window Wasserstein bounds | **PROVED**, Thm11 | Certification | Standard factorization/coupling inequalities. |
| Uniform RMS iff row regulated; uniform covariance iff row regulated; all finite-energy rows approximable in weaker metrics | **PROVED**, Thm12/12A/12B | Certification | Classical deductions; novelty unestablished; exact metrics differ. |
| Exact input-piecewise LTI implies exact output-piecewise stationarity | **REFUTED**, C13 | Certification | Boundary-memory counterexample; no assertion that the book claimed exact class equality. |
| Input-column regulatedness necessary for a stationary output law; row regulatedness necessary in weak W2/operator metric | **REFUTED**, C14 | Certification | Separate examples; **not** a refutation of uniform covariance necessity. |
| Qualitative slow/fast amplitudes uniquely separate; initial wavelet alone identifies future kernel or bounds segment count | **REFUTED**, Prop15–16 | Certification | Explicit spectral/product and time-dependent scale ambiguities. |
| Conditional average inverse-Q recovery and \(2\delta/(\pi\Delta f\Delta\tau)\) error bound | **PROVED**, Prop17 | Certification | White within-block spectra and positive continuous representatives; no observed-data error guarantee. |
| Locally stationary spectral freezing RMS \(D/T+Lh/2\) | **PROVED**, Thm18 | Reproduction | Explicit no-overlap version of Ombao prior art, not discovery. |
| Finite scalar-grid greedy/DP implementation and counterexample/Q arithmetic | **COMPUTED+VERIFIED** | Certification |1,092 sequences;3,276 greedy and6,015 DP comparisons; rational arithmetic. This does not certify the general mathematical proofs. |
| General blind, finite-record physically constrained segmentation/recovery | **OPEN** in this work; bare-assumption universal identification refuted | No positive certification | No general resolution located; additional hypotheses must be chosen and justified. |

### Exact computational evidence

Executed once:

```sh
python3 -B information-science/piecewise-lti-approximation/work/verify_exact.py information-science/piecewise-lti-approximation/evidence/exact-checks.json
```

[`evidence/exact-checks.json`](evidence/exact-checks.json) records **PASS**, Python3.14.3, source hashes, command arguments and elapsed time. It compares independent exhaustive enumeration of all partitions with both algorithms for every sequence of length1–6 over {-1,0,1}. Counterexample13's variance is exactly7/4 at t=1/4 and13/4 at t=3/4; the Q-bound worst-case rational error equals its bound. No floating-point observation carries a proof claim. There are no third-party Python dependencies; [`work/requirements.txt`](work/requirements.txt) records that fact.

### Explicit answers to the extension questions

1. **Amplitude correction:** not uniquely from slow/fast descriptions alone, even with a normalization. Prop15 supplies nonconstant smooth factorizations of exactly the same observed amplitude. Margrave's whiteness/minimum-phase assumptions are genuinely extra.
2. **Known surface wavelet:** fixes the initial condition but supplies no time-modulus or later identifiability by itself (Prop16). With a known propagation law/Q/phase, it fixes the family and enables Thm9's constructive bounds.
3. **Q estimation:** possible conditionally in the ideal white-reflectivity frozen-block model; spectral log-ratio slopes recover **average inverse Q**, with Prop17's explicit error propagation. Colored reflectivity is exactly confounded with attenuation. No confidence guarantee from a single finite trace follows without a spectral-estimation error model.

## 6. Independent review

Requested hostile referee: **Codex `gpt-6.1-sol`, reasoning `max`, read-only, ephemeral**. The actual runtime header confirmed that model/effort/sandbox; no external posting or contact was performed. First pass completed with exit0 in approximately498 seconds and read the book images and the immutable initial proof snapshot. Prompt and exact invocation/hashes are in [`evidence/referee-prompt.txt`](evidence/referee-prompt.txt), [`evidence/referee-receipt.json`](evidence/referee-receipt.json); report is [`evidence/codex-referee.md`](evidence/codex-referee.md).

First review: **no fatal defect**, one major and four minor findings. Every finding received a disposition:

| Finding | Disposition |
|---|---|
|1 Major: the input-sign example only defeats input-column regulatedness; it does not defeat output-row necessity in a uniform covariance metric | **Fixed.** Split the two counterexamples and metrics. Added a full covariance-characterization proof (Thm12A) and separate weak-metric density theorem (Thm12B). In particular, uniform covariance approximation is not dismissed. |
|2 Minor: exact model-class separation does not refute the book's unspecified approximation equivalence | **Fixed.** C13 now makes only the exact-class/boundary-memory statement and explicitly preserves the approximation question. |
|3 Minor: chosen phase b not automatically the book's Hilbert-transform phase | **Fixed.** Added explicit phase-compatibility condition and conjugate-frequency extension; Gabor identification made conditional. |
|4 Minor: spectral point values require representatives | **Fixed.** Prop17 now assumes positive continuous representatives and pointwise model identities on the measurement band. |
|5 Minor: Dieudonné precise attribution unsupported in first review's allowed sources | **Resolved with primary evidence.** Downloaded/read the original1960 p139 theorem and complete proof and p140; saved images and detailed source ledger. No longer an unverified attribution. |

The first pass's proof hash was `9c0b6cd736ec6e816ece695ff68c24d7712226cf3fe05d520107331774a1f55d` before and after review. The final proof intentionally differs because the above fixes and prior-art reproduction were added.

**Second pass completed:** same actual model/effort/read-only sandbox, exit0, approximately242 seconds. [`evidence/codex-referee2.md`](evidence/codex-referee2.md) states **“The central revised statements survive. No fatal or major defect found”**, confirms all five earlier findings resolved, checks Thm12A's diagonal/Fubini/translation/representation argument, Thm12B, and Thm18, and finds no inflation in the per-reading/book-level verdicts. The sole new minor finding was an unspecified observation index set in Thm18: **fixed** by requiring \(T\in\mathbb N\), exactly \(t=0,\ldots,T-1\), and \(M\ge1\). The author also clarified full-line white-noise/zero-extension conventions for finite input domains. These local clarifications and this disposition paragraph were made after the second review, whose proof snapshot hash is `073ce68ab6974d007ffae7ab192191564d65a1d75ef565fbcee7af72b6b8e91e`; they were not presented as a third model-reviewed snapshot. [`evidence/referee2-receipt.json`](evidence/referee2-receipt.json) binds the reviewed proof and README. No unresolved fatal or major finding remains.

## 7. Book-level verdict

**The full chapter, including its three seismic inverse-problem extensions, is not completely resolved here.** The known-kernel uniform \(L^1\) approximation question has a complete classical answer: essential Banach-valued regulatedness, with tail limits exactly when a globally finite partition is required. Fixed-input output-only approximation and the stated Gaussian covariance/coupling/finite-window metrics also receive complete, explicitly conditional characterizations or density theorems. These are not new scientific solutions of the whole book problem: changing the metric changes the answer, input and output segmentation differ, and oracle approximation is not blind estimation. Under the chapter's bare qualitative information, unique amplitude correction, future-kernel identification from one initial wavelet, and unrestricted Q recovery are impossible; conditional statistical recovery remains a model-specific task. The truthful portfolio count is **zero newly fully resolved book questions**, with useful classical certification, explicit obstructions and a precise map of the missing assumptions.

## 8. Next steps

1. For an actual seismic-recovery theorem, first fix the admissible propagation/phase model, reflectivity distribution or calibration, noise class, physical filter constraints, measurement band and statistical loss. The existing gauge ambiguities must be broken by those assumptions, not by tuning a segmentation algorithm.
2. If the scientific objective is uniform approximation of a known physical kernel, supply its frequency band, source spectrum and phase convention; apply the exact \(L^1\) criterion or the declared Schur/envelope bounds. Continuous optimal segmentation beyond the stated reflexive/cost-access setting is not claimed here.
3. For a literature-complete historical account, obtain the inaccessible final versions of the named1965/1997/1998/2001/2011 papers and compare against the explicitly identified primary manuscripts. No new search run is justified merely to claim novelty for these classical results.
4. Parent verification: replay `work/verify_exact.py` on a copy; read the final proof and second referee dispositions. There are no Lean files or hidden numerical certificates. Do not promote `PROVED` here to kernel-verified or human-refereed mathematics.
