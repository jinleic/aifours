# Primary-source reading notes

Checked 2026-10-14 (PT). Search snippets and search-engine-generated explanations are discovery aids, not evidence. In particular, one search response claimed a universal Gram-matrix necessity for LAD; Theorem 4A in ../proof.md disproves that unqualified claim. Another confused preservation of asymptotic properties with preservation of a finite-sample numerical estimate; that response was discarded.

## Original source and status-search scope

* Cui Hengjian, book pp. 408–409 / PDF pp. 424–425: local `book-excerpt.txt`, extracted with `pdftotext -layout`. The text says the error distribution satisfies “certain conditions” but does not specify them, and does not define selection or strong-consistency coupling. Its stated design repeats x_j at n+j. Page 409 explicitly describes the design as a point sequence and says progress beyond least squares had not been seen at the time of writing. This is evidence for the 2009 status, not for a 2026 absence of a solution.
* English searches included the exact title/phrases, Drygas/Chen/Cui, “consistency of M-estimates in linear models”, necessary/sufficient conditions, repeated/replicated/doubling sample size, and successors of Wang–Hu. Chinese searches included “样本量的增加”, “相合”, “崔恒建”, “M估计”, “充要条件”, “猜想”, “证明”, and “反例”. No opened primary source supplied a post-2009 resolution of the nested-design implication. This is a negative search finding, **not a proof that the problem remains open worldwide**.

## 1. Drygas (1976): weak least-squares necessity and sufficiency

**Citation:** H. Drygas, *Weak and strong consistency of the least squares estimators in regression models*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 34, 119–127. DOI [10.1007/BF00535679](https://doi.org/10.1007/BF00535679).

**Actually opened:** publisher page and complete public PDF, saved as `drygas-1976.pdf` / `.txt`.

**Load-bearing text:** introduction and Theorem 3.1, printed pp. 119–121, local text lines 16–31, 36–38, 75–94, 122–147. With zero-mean square-integrable errors and covariance matrices bounded above and uniformly positive below, weak consistency for all estimable components is equivalent to divergence of the smallest positive design eigenvalue. For i.i.d. errors with finite nonzero variance and eventually full-rank fixed design, this becomes lambda_min(S_n)->infinity. It is not restricted to normal errors. The paper treats nested rows x_1,x_2,...; it does not prove strong consistency for arbitrary sliding repeated-design arrays.

## 2. Lai–Robbins–Wei (1978): strong least-squares sufficiency

**Citation:** T. L. Lai, H. Robbins, C. Z. Wei, *Strong consistency of least squares estimates in multiple regression*, PNAS 75(7), 3034–3036. DOI [10.1073/pnas.75.7.3034](https://doi.org/10.1073/pnas.75.7.3034).

**Actually opened:** [PMC primary page](https://pmc.ncbi.nlm.nih.gov/articles/PMC392707/) and its scanned first page, saved as `lai-robbins-wei-1978-page3034.png`. The PDF endpoint returned an HTML download interstitial, so no full-PDF reading is claimed.

**Theorem 1, visually read on p. 3034:** independent errors, E epsilon_i=0, uniformly bounded second moments, and (X_n'X_n)^(-1)->0 imply b_n->beta with probability one. The design entries are fixed x_ij (row and coordinate indices), not an unrestricted n-dependent triangular design. The main text explicitly says the result needs only uniformly bounded second moments. With i.i.d. finite nonzero variance, Drygas plus this theorem gives the familiar nested-design LSE equivalence between Gram divergence, weak consistency, and strong consistency. Our strong counterexample changes the *coupling and nonnested repeated arrays*, not this theorem.

## 3. Zhao–Rao–Chen (1993): convex M weak sufficiency

**Citation:** L. C. Zhao, C. Radhakrishna Rao, X. R. Chen, *A Note on the Consistency of M-Estimates in Linear Models*, in *Stochastic Processes*, pp. 359–367. DOI [10.1007/978-1-4615-7909-0_41](https://doi.org/10.1007/978-1-4615-7909-0_41).

**Actually opened:** publisher abstract and public two-page preview, saved as `zhao-rao-chen-1993-preview.pdf` / `.txt`. Full chapter download returned an HTML access page, preserved as `zhao-rao-chen-1993-access-denied.html`.

**Verified scope:** weak consistency under S_n^(-1)->0 for convex rho satisfying additional regularity assumptions. Preview p. 360 says earlier estimating-equation conditions excluded LAD; its result covers important special cases; necessity in its general setting was open. A later visual rendering recovered formulas omitted by text extraction: A2 is E psi(e_1)=0, |E psi(e_1+u)|>=c_0|u|, and E psi^2(e_1+u)<=c_1 for |u|<Delta; A3 is S_n^(-1)->0. See `zhao-rao-chen-1993-preview-page2.png` and the exact transcription `zhao-rao-chen-1993-assumptions.txt`. The formal theorem statement/proof on the following pages is still unavailable, so no further unobserved qualifications or universal applicability are assumed.

## 4. Pollard (1991): LAD asymptotic normality under diffuse leverage

**Citation:** D. Pollard, *Asymptotics for least absolute deviation regression estimators*, Econometric Theory 7, 186–199. DOI [10.1017/S0266466600004394](https://doi.org/10.1017/S0266466600004394).

**Actually opened:** author-hosted public PDF [HTTP URL](http://www.stat.yale.edu/~pollard/Papers/Pollard91ET.pdf), saved as `pollard-1991-author.pdf`. It is a scan: text extraction is empty. Rendered and visually read printed pp. 186–189 in `pollard-page-01.png` through `pollard-page-04.png`. HTTPS on the author host failed certificate verification; the publisher endpoint returned an HTML challenge, preserved as `pollard-1991-publisher-access.html`. No TLS-verification bypass was used.

**Exact Theorem 1, printed p. 189:** i.i.d. errors with median zero and a continuous positive density f near zero; deterministic design with S_n=V_n^2 eventually positive definite; max_i ||V_n^(-1)x_i||->0. Then 2 f(0) V_n(beta_hat_n-beta_0) converges in law to N(0,I_p). This yields weak consistency for the nested design. Indeed, choose a fixed full-rank prefix S_m: tr(S_n^(-1)S_m)<=m d_n->0, so S_n^(-1)->0. This last implication is our elementary linear-algebra deduction, not a quotation.

**Convexity lemma, p. 187:** pointwise-in-probability convergence of finite convex random functions on an open convex domain to a finite deterministic function implies compact-uniform convergence in probability. This does not say that convergence of minimizers alone implies objective convergence or stability under addition.

## 5. Zhao (2002), Wang–Hu (2015/2016): modern sufficient conditions

**Citations:**

* L. C. Zhao, *Strong consistency of M-estimates in linear models*, Science in China Series A 45, 1420–1427. Opened publisher record at DOI [10.1007/BF02880036](https://doi.org/10.1007/BF02880036). Its abstract describes weaker moment conditions; the exact theorem below is quoted from Wang–Hu's Theorem A, not independently checked against the full 2002 paper. Note: the Metrika reference links a different DOI, BF02879979; that conflicting metadata was not silently substituted.
* X. Wang and S. Hu, *A note on the strong consistency of M-estimates in linear models*, [arXiv:1505.07178](https://arxiv.org/abs/1505.07178), 2015; Metrika 79, 265–266 (2016), DOI [10.1007/s00184-015-0554-8](https://doi.org/10.1007/s00184-015-0554-8). Opened arXiv full text and journal landing page. Saved full preprint `wang-hu-2015.pdf` / `.txt`. The journal article is two pages; the preprint is eight pages, so no claim of byte-identical versions is made.

**Definitions:** a nonmonotone convex rho, a subgradient selection psi between left/right derivatives, S_n=sum x_i x_i', full rank at some fixed n_0, and d_n=max_i x_i'S_n^(-1)x_i.

**Verified preprint Theorem 1:** for i.i.d. errors, assume positive constants Delta,C_0,C_1 such that

1. psi(u+h)-psi(u)<=C_0 for every u and 0<h<Delta;
2. E psi(epsilon)=0 (ordinary finite expectation), and |E psi(epsilon+u)|>=C_1 |u| for |u|<Delta;
3. d_n=O(n^(-1)).

Then beta_hat_n->beta_0 almost surely. There is no additional q>1 score moment in this theorem. This is not “no moment assumptions”: condition E psi=0 still entails integrability in the usual interpretation.

**Theorem A as reported there:** d_n=O(n^(-delta)), 0<delta<=1, with the same score conditions; require E|psi|^(1/delta)<infinity for delta<1, or E|psi|^q<infinity for some q>1 for delta=1. The new theorem improves the delta=1 moment condition.

**LAD specialization:** psi=sign with a suitable value at zero satisfies bounded score increments. A median-zero density bounded below near zero gives the stated local identification. Thus d_n=O(1/n) is an explicit strong-consistency sufficient condition for regular LAD. These are sufficient conditions, not a characterization. The sparse design in Theorem 3 has d_n=1/floor(log_4 n), so it does not meet this leverage rate.

**Replication:** at even prefixes of the interleaved R design, S_{2n}=2S_n and d_{2n}=d_n/2. Hence these fixed-design sufficient regimes remain valid for R; existence of an arbitrary consistent estimator does not imply these hypotheses. S must not be treated as a fixed interleaved design for strong convergence.

## 6. Important identified papers whose full theorems were not accessible

These records prevent an overclaim that no necessary/sufficient-condition literature exists. Their formulas are not guessed from titles or search-generated summaries.

* X. R. Chen and Y. H. Wu (1988), *Strong consistency of M-estimates in linear models*, DOI [10.1016/0047-259X(88)90120-0](https://doi.org/10.1016/0047-259X(88)90120-0). Crossref primary metadata opened; publisher full/abstract endpoints returned 403. Exact hypotheses/results beyond the title: **[UNVERIFIED in this session]**.
* Z. D. Bai and Y. Wu (1997), *On necessary conditions for the weak consistency of minimum L1-norm estimates in linear models*, DOI [10.1016/S0167-7152(96)00182-4](https://doi.org/10.1016/S0167-7152(96)00182-4). Crossref and the publisher's public article API opened; these provided metadata but not the theorem. Search-generated claims about an L1 design criterion and error-law assumptions remain **[UNVERIFIED]**, and are not used as a proved necessity theorem.
* A. Berlinet, F. Liese, I. Vajda (2000), *Necessary and sufficient conditions for consistency of M-estimates in regression models with general errors*, DOI [10.1016/S0378-3758(99)00218-9](https://doi.org/10.1016/S0378-3758(99)00218-9). Crossref, publisher API, and [Liese's own bibliography](https://www.math.uni-rostock.de/~liese/Papers.pdf), item 48, opened. Full text unavailable via publisher (403) and attempted CiteSeer route. Whether its conditions imply the book's duplication conjecture is **[UNVERIFIED]**; no resolution is inferred from its title.
* X. Deng, Y. Wu, W. Wang, X. Wang (2023), *Asymptotic properties of M estimators in classical linear models with phi-mixing random errors*, DOI [10.1080/00949655.2023.2220157](https://doi.org/10.1080/00949655.2023.2220157). Primary metadata opened, no abstract supplied. Its title concerns dependent errors; no implication for the iid replication conjecture is asserted.

## Synthesis and precise limit of this literature check

The strongest directly read general-convex strong theorem here is Wang–Hu's explicit leverage/identification theorem, not a claim to the globally latest result. Classical weak LSE is characterized; regular LAD has powerful asymptotic and sufficient-consistency theorems; unrestricted convex losses and arbitrary atoms/support/selection are different. The self-contained bounded-Gram examples in proof.md demonstrate why the LSE criterion cannot simply be promoted to a universal necessary condition. A comprehensive necessity characterization and the book's nested weak transfer were not established by this search.
