# Status and eligibility — 2026-10-14 (local PT)

## Selected question and explicit primary statement

Book bridge: Lou Senyue and Li Jinhua, 关于得到高维可积模型的一个新猜想,
《10000个科学难题·物理学卷》 (Science Press, 2009), pp. 350–351 (PDF pp. 383–384).
The chapter proposes replacing a spatial Hirota multiplier by an extra-dimensional,
supersymmetric or discrete one. The copied original excerpt is `source/problem.zh.txt`.

The exact selected question comes from **Jian-Yong Wang, Xiao-Yan Tang and Zu-Feng Liang**,
“Constructing (2+1)-dimensional N=1 supersymmetric integrable systems from the Hirota
formalism in the superspace,” *Chinese Physics B* **27** (2018), 040203,
DOI [10.1088/1674-1056/27/4/040203](https://doi.org/10.1088/1674-1056/27/4/040203).
[Publisher PDF](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/27/4/040203.pdf),
§4, p. 040203-9, proposes the unnumbered family

    (D_t+D_x^n)F·G=0,       S_y(D_t+D_x^n)F·G=0,       integer n≥2.

Two short verbatim extracts (each under 40 words):

> “it is difficult to prove the integrable property in the symmetry sense for n > 3, due to the difficulty in determining the function of integration.”

> “the integrability should be proved via other means, such as the criteria that the existence of three super-soliton solutions.”

**Approved bounded target:** for every integer n≥4, determine whether this paired system
admits a generic three-super-soliton family with independently chosen body wave numbers
and allowed F/G seed types, in the explicitly defined square-free exponential-body class
of RESULTS.md. This addresses the authors' suggested three-super-soliton criterion,
not their distinct conjecture about infinitely many generalized symmetries. The source
does not spell out “generic”; that quantifier and the ansatz are fixed explicitly here,
rather than silently treating any isolated exact solution as a full Hirota family.

**Why bounded:** a body projection retaining the external superspace coordinate theta
must turn any such supertau pair into a bosonic tau pair. An exact F–F–G obstruction has
already been certified in this workspace for every degree ≥4. The new obligation is
the precise Grassmann/projection bridge, including nilpotent corrections and parity,
plus an independent direct-differentiation replay. No growing-N symbolic search is needed.

Evidence label: **Certification**. A primary hypothesis is explicit, but first discovery
or exhaustive worldwide priority clearance is not claimed.

## Source definitions and current baseline

The 2018 paper, §2.1, p. 040203-2, defines even superfields F,G on (x,y,t,theta),
`theta²=0`, and `D_theta=partial_theta+theta partial_y`. Its super-Hirota operator is
`S_y P(F·G)=[(D_theta1−D_theta2)P(partial_x1−partial_x2,partial_t1−partial_t2)
F(1)G(2)]_{1=2}`. RESULTS.md uses this definition with left odd derivatives.
The paper proves symmetry results for n=2 and n=3, but asks about n>3. These are not
proofs of a generic unrestricted three-super-soliton ansatz for every n.

Its introduction, pp. 040203-1–2, explicitly writes the bosonic n=3 pair and credits
its N-soliton solutions, Bäcklund transformation and Lax representation to **Peng,
Zhang, Gegenhasi and Liu, PLA372 (2008)4197**, DOI10.1016/j.physleta.2008.01.090.
That is prior-art risk for the earlier cubic all-N project, not evidence about n≥4.
The earlier folders are preserved read-only; none of their historical-openness claims
is strengthened by this new selection.

## Critical 2026 comparison: not the same equation class

**Laurent Delisle and Amine Jaouadi**, “A Classification of Hirota-Integrable
Supersymmetric Bilinear KdV-Type Equations,” arXiv:[2609.14372v1](https://arxiv.org/abs/2609.14372v1),
13 September 2026, [full HTML](https://arxiv.org/html/2609.14372v1). This is a **preprint**;
no refereed publication status is inferred.

Definitions and results read: §II Eqs. (6)–(7); §III Eqs. (8), (11)–(15), (20)–(26);
§IV Grassmann compatibility decomposition; §V Eqs. (42)–(51); §VI conclusion.

- Its equation is the **single-tau** equation `S_x P(D_x,D_t)(tau·tau)=0`, with P
  assumed odd. It has no independent paired equation `P F·G=0` and no independent
  F/G seed amplitudes or F-only/G-only mixed pattern.
- Its dressed ansatz allows nilpotent pair corrections and modified odd phases;
  those corrections still have a conventional square-free exponential body.
  Our projection theorem allows arbitrary such nilpotent corrections rather than
  assuming the naive undressed ansatz.
- For `P=T+aX^5+bX^3+cX`, its §V excludes a nonzero fifth-order coefficient for
  unrestricted fermionic parameters in its own single-tau class. Its constrained
  “weak” solutions do not establish or refute the paired all-n statement here.
- Its higher-dimensional example Eq. (50) treats a cubic BLMP single-tau equation,
  not the paired n≥4 family. Its §VI asks whether the classification extends to
  supersymmetric mKdV-/sine-Gordon-/complex-type systems. Therefore no theorem in
  the inspected definitions/results directly settles this paired question.

This comparison is a statement about the inspected source's hypotheses, not a claim
that no related theorem or general hierarchy result exists elsewhere.

## Forward-citation screen and its limits

On 2026-10-14, a fresh [OpenAlex citing-works query](https://api.openalex.org/works?filter=cites:W2801150213&per_page=100)
for the 2018 paper returned **0 indexed citing works**. This is an indexing observation,
not evidence of zero literature activity or an exhaustive proof of openness.

The parent scout `ScoutLiLouQuestion` screened **14** OpenAlex citers of Li–Lou2008,
with an identical OpenCitations list reported by that scout. The following records its
actual depth. Rows marked scout-only were not independently promoted to full-text review.

| Citer | Depth used | Relevance / explicit resolution found |
|---|---|---|
| Wang–Lou–Qian2010, [10.1088/1674-1056/19/5/050202](https://doi.org/10.1088/1674-1056/19/5/050202) | Full text (earlier project and parent scout) | Supersymmetric n=2 example; asks for further checks, not n≥4 resolution |
| Wang–Tang–Liang2018, [10.1088/1674-1056/27/4/040203](https://doi.org/10.1088/1674-1056/27/4/040203) | Full definitions, n=2/3 results and §4 read here | Explicit hypothesis and proposed three-super-soliton criterion above |
| Wang–Yang–Tang–Chen2024, [10.1007/s11071-024-09511-0](https://doi.org/10.1007/s11071-024-09511-0) | Full public preprint in earlier project; scout checked journal reference list | F=G, n=5 bosonic equation has constrained three-/four-soliton families; not the generic paired all-n criterion |
| Wang–Yu–Lou2010, [10.1088/0253-6102/53/6/01](https://doi.org/10.1088/0253-6102/53/6/01) | Abstract | n=3 symmetry algebra only |
| Tang et al.2014, [10.1016/j.physleta.2014.03.040](https://doi.org/10.1016/j.physleta.2014.03.040) | Metadata; scope identified in 2018 primary introduction | Modified KdV/potential-BLMP n=3; no checked n≥4 theorem |
| Jing–Li2013, [10.1088/1674-1056/22/1/010303](https://doi.org/10.1088/1674-1056/22/1/010303) | Scout abstract only | Variable-coefficient nonlinear Schrödinger symmetry; no relevant resolution reported |
| Hu–Chen–Huang2010, [10.1088/1674-1056/19/8/080203](https://doi.org/10.1088/1674-1056/19/8/080203) | Scout abstract only | Baroclinic potential-vorticity equation |
| Zhang et al.2010, [10.1088/1674-1056/19/2/020201](https://doi.org/10.1088/1674-1056/19/2/020201) | Scout abstract only | Generalized KP equations from potential vorticity |
| Liu et al.2014, [10.1088/1674-1056/23/11/110203](https://doi.org/10.1088/1674-1056/23/11/110203) | Scout abstract only | Burgers residual-symmetry Bäcklund transformations |
| Wang et al.2014, [10.1088/1674-1056/23/1/010201](https://doi.org/10.1088/1674-1056/23/1/010201) | Scout abstract only | Blaszak–Marciniak lattice |
| Liu2010, [10.1088/1674-1056/19/8/080202](https://doi.org/10.1088/1674-1056/19/8/080202) | Scout abstract only | Generalized Kawahara approximate reductions |
| Xin–Chen–Wang2013, [10.1088/1674-1056/22/6/060201](https://doi.org/10.1088/1674-1056/22/6/060201) | Scout abstract only | Symmetry-preserving difference schemes |
| Wang–Li2009, [10.1088/1674-1056/18/6/001](https://doi.org/10.1088/1674-1056/18/6/001) | Scout abstract only | Coupled KP symmetries |
| Yang–Chen–Li2010, [10.1088/0253-6102/53/6/06](https://doi.org/10.1088/0253-6102/53/6/06) | Scout abstract only | Short-wave Camassa–Holm/DP approximations |

No explicitly settling source for the generic paired n≥4 three-super-soliton question
was identified among these checked materials. Hietarinta's older odd/even classifications
may overlap parts of the bosonic obstruction; no novelty is attributed to those classical
ingredients or to the elementary augmentation principle. The finite citation screen is
not an exhaustive priority determination.
