# Information-science volume: catalog of difficult problems and 6-hour selection (2026-10-15 PT)

Volume: 《10000个科学难题·信息科学卷》, Science Press 2011, ISBN 978-7-03-031911-1.
This is a selection stage only. No attack was made beyond five feasibility probes of at most 5 minutes each.
The machine-readable version is [`catalog.json`](catalog.json). Page images and transcriptions for the top three are under [`sources/`](sources/), and the probe scripts and outputs under [`probes/`](probes/).

**Recommendation #1: `info-p0403-q9bal242`.** Does a balanced 9-variable Boolean function with nonlinearity 242 exist? The book (p.403) poses it as the smallest case of "for odd n ≥ 9 the maximum nonlinearity of balanced functions is unknown", together with the construction question for odd n. On 2026-10-13, two unrefereed preprints both listed it as open, and one of them (arXiv:2610.17871) claims the covering radius of RM(1,9) is 242. If that claim holds, a single balanced 242 function would settle the balanced maximum at n = 9 exactly.
**Alternates:** #2 `info-p0399`, the APN-permutation problem for n = 8 (close one of the two residual linear-self-equivalence classes). #3 `info-p0403-q8bal118`, a machine audit of the 2026-10-13 claimed proof that 118 is impossible. #3 is a verification task and is flagged for the parent to decide.

---

## (a) Method, inputs, query log

**Inputs (read-only).**
- Book PDF: `/Users/jinleic/repos/aifours/books/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`. Its sha256 per `books/README.md` is `9b3f16ee…27db`. PDF page = book page + 21.
- Inventory: `research-institute/explorer/inventory/info.json` lists 328 articles: 32 in 科普篇 (popular science) and 296 in 专题篇 (topical).
- Skip list: `ai4s-owned.json` has 10 information-science ids: info-p0409, 0452, 0467, 0539, 0542, 0631, 0674, 0680, 0712, 0880. The dossiers listed in `information-science/README.md` add info-p0446, 0635, 0653 and 0731, so 14 ids are skipped.
- Prior screens: the crosswalk has 28 information-science entries; 11 are too-hard and 5 ill-posed, and all of those verdicts are inference-only. Also used: `information-science/README.md` and `evidence/information-science-more-20261014/Screen*.md`.
- Standards followed: `explorer/prompts/sota.md` and `docs/knowledge-system/FRONTIER_METHOD.md` §§1–2.

**Method.**
1. Listed all 328 articles.
2. Dropped the popular-science section. It poses no precise questions, which matches the earlier category-level exclusion.
3. Ran a keyword scan of the text layer (猜想 / 公开问题 / 公开难题 / 悬而未决 / 是否存在 / 能否 plus about 70 domain terms). Hits concentrate in the cryptography and complexity block, PDF pp. 401–568.
4. Read candidate statements from **page images**, because the text layer garbles Latin letters, digits and formulas. Pages read as images at 100–300 dpi (PDF pages): 420 (APN, formula zoomed at 300 dpi), 424–426 (nonlinearity), 413–416 (lattices, decoding), 439 (network information theory), 444–445 (information flow), 545–550 (complexity, SAT), 685–686 (flatness), 707–708 (LTV stability). The other cryptography and complexity articles (PDF 401–419, 421–434, 537–568) were checked through their Chinese text layer only. Their questions are standard flagship problems.
5. Checked status in primary sources. The read-only scout `BooleanSOTA` covered APN and nonlinearity. Every source cited below was opened unless marked [UNVERIFIED].
6. Ran five feasibility probes (≤5 min each): an exact MILP and a plain C DFS on the RSBF class; two Lemma 6 checks for the 2026-10-13 claim; and a re-check of Kavut–Yücel's printed nl-242 truth tables. See [`probes/probe-results.txt`](probes/probe-results.txt).

**Query log (all on 2026-10-15 PT).** Web search returns leads only; anything cited was then opened.
- "balanced Boolean function 8 variables nonlinearity 118 existence open problem". This found arXiv:2610.17897 (submitted 2026-10-13).
- "APN permutation dimension 8 nonexistence linear self-equivalence Beierle Brinkmann Leander".
- "APN permutation even dimension 8 new result 2025 2026 arXiv" (past year). This found 2508.04644, 2606.11967 and 2609.05917; the last uses a different notion of APN on Z_n and is irrelevant.
- **zh:** "9元平衡布尔函数 非线性度 242 存在性"; "偶数元 APN 置换 存在性 8元 公开问题 进展"; "九元 平衡布尔函数 最大非线性度 奇数元 平衡函数 非线性度 超过 bent 级联界". Chinese sources were reachable, but every result led to English primary papers. No Chinese-language resolution was found.
- "12-variable 1-resilient … Zhang Xiao conjecture …".
- "balanced Boolean function 9 variables nonlinearity 242 Walsh spectrum zero open problem 2023 2024 2025". This found arXiv:2610.17871 (submitted 2026-10-13).
- "APN permutations dimension 8 linear self-equivalence remaining cases settled …". This found ePrint 2026/1012 and repeated 2606.11967.
- Scout queries: BBL plus follow-ups, quadratic-APN databases, Kavut–Yücel, the AMC 2020 table, the Zhang–Xiao 2009/2010 papers and Zhang–Pasalic 2017.
- **openai/math.**
  - Local corpus (`math/lean/docs` 235 files, `math/preprints` 722 dirs): grep for APN, almost perfect nonlinear, nonlinearity of balanced/resilient, resilient Boolean, bent concatenation, Patterson–Wiedemann and covering radius. No hits on cryptographic Boolean functions. The only hits are unrelated Boolean-analysis families (119, 132, 192, 284) and lattice "covering radius".
  - Remote `openai/math` `CONTENTS.md` at HEAD `1581d4cbdd69` (377 families): 0 hits.
  - Article authors' later work: 张卫国 (Weiguo Zhang): Zhang–Pasalic 2017, opened by the scout. 林东岱 (Dongdai Lin): no later APN-permutation result found [search-dated].

## (b) Catalog of difficult problems in the volume

Budget classes: **6h-scoped**, **multi-day** or **not-boundable**. Plausibility is [INFERENCE]. Status was checked 2026-10-15; "opened" means the source was actually read this round. Pages are given as book pages (PDF pages).

| id | zh title (authors) | pages | question (one line) | status · key source | budget · plausibility |
|---|---|---|---|---|---|
| **info-p0403-q9bal242** | 弹性布尔函数的非线性度的紧上界 (张卫国, 肖国镇) | 403–405 (424–426) | Is there a balanced f: F₂⁹→F₂ with nl ≥ 242 (max\|W\| ≤ 28, W(0)=0)? The balanced maximum is 240, 242 or 244. | **open** · [LXW 2026 OP1](https://arxiv.org/abs/2610.17897), [WLW 2026 §6](https://arxiv.org/abs/2610.17871), [Kavut–Yücel 2010](https://arxiv.org/abs/0808.0684), [2025 survey](https://arxiv.org/abs/2504.17666) | **6h-scoped** · low (find) / high (local-neighbourhood certificates) / medium (small-class maxima) |
| **info-p0399** | 偶数变元APN置换的存在性 (林东岱) | 399 (420) | Does an APN permutation of F_{2^n} exist for even n ≥ 8 (first case n=8)? | **open** · [BBL 2021](https://arxiv.org/abs/2003.12006) Thm 4; [2508.04644](https://arxiv.org/abs/2508.04644v2); [2606.11967](https://arxiv.org/abs/2606.11967) | full problem not-boundable; **6h-scoped** sub-case (BBL classes 22/30) · low |
| **info-p0403-q8bal118** | same article | 403 (424) | Can a balanced 8-variable function reach nl 118? | **claimed** (answer no) · [LXW 2026](https://arxiv.org/abs/2610.17897), unrefereed. We found a counting slip in Lemma 6; our probes indicate the lemma still holds (see #3) | 6h-scoped, **verification only** · high |
| info-p0403-q10bal494 | same | 403 (424) | Can a balanced 10-variable function reach nl 494? | open · [LXW 2026 OP3](https://arxiv.org/abs/2610.17897) | not-boundable (needs a new reduction) · very low |
| info-p0403-q11bal | same | 403 (424) | Is there a balanced 11-variable function with nl > 992 (non-PW)? | open · [AMC 2020 Table 1](https://doi.org/10.3934/amc.2020010) (opened by scout): no balanced value listed; unbalanced 994/996 known ([KY](https://arxiv.org/abs/0808.0684)) | multi-day (~48 h symmetric-class search) · very low |
| info-p0403-zx | same, p.404 | 404 (425) | Zhang–Xiao conjecture N_f ≤ 2^{n−1}−2^{n/2−1}−2^{⌊n/4⌋+m−1} for m-resilient f; the first test case is (12,1), bound 2008, and only 2012 would refute it | open · [Zhang–Xiao 2009](https://arxiv.org/abs/0905.0794), [Zhang–Pasalic 2017](https://web.xidian.edu.cn/wgzhang/files/InfSci2017.pdf) (both opened by scout; the published hypotheses differ from the book's) | not-boundable · very low |
| info-p0403-resgeneral | same | 403 (424) | Tight upper bound on the nonlinearity of m-resilient functions for all (n, m) | open (umbrella question) · as above | not-boundable |
| info-p0380 | 安全方案中的单向函数 (王天择) | 380–381 (401–402) | Do one-way functions exist? | open · [Clay: P vs NP "Unsolved"](https://www.claymath.org/millennium/p-vs-np/) (related) | not-boundable |
| info-p0382 | 密码学中的整数分解问题 (赵岩) | 382–383 | Is integer factoring classically polynomial? | open · standard; no row-specific source opened | not-boundable |
| info-p0384 | RSA问题 (冯登国) | 384–385 | Is the RSA problem equivalent to factoring? | open · [UNVERIFIED] Boneh–Venkatesan 1998, Aggarwal–Maurer 2009 | not-boundable |
| info-p0386 | 安全方案中的离散对数问题 (张旭升) | 386–388 | Is there a polynomial-time algorithm for DLP / ECDLP? | open · standard | not-boundable |
| info-p0389 | Diffie-Hellman问题 (张旭升) | 389–391 | Is CDH/DDH equivalent to DL in general groups? | open · [UNVERIFIED] Maurer–Wolf | not-boundable |
| info-p0392 | 格约化问题 (史涛) | 392–393 (413–414) | Is approximate SVP with factor n^δ hard even quantumly, and at least as hard as factoring? | open · book pp.392–393 states these as 猜想/公开问题 | not-boundable |
| info-p0394 | 纠错码的译码问题 (张寅) | 394–395 (415–416) | Average-case complexity of decoding random linear codes | open · standard | not-boundable |
| info-p0396 | 多项式分层 (李振琦) | 396–398 | Is PH infinite? | open · Clay (related) | not-boundable |
| info-p0516 | Mu-演算模型检测复杂度 (林惠民) | 516–517 (537–538) | Is μ-calculus model checking (parity games) in P? | open (quasi-polynomial since 2017) · [Jurdziński–Lazić](https://arxiv.org/abs/1702.05051) | not-boundable |
| info-p0518 | BQP类的大小 (刘田) | 518–520 | How BQP relates to BPP, NP and PH | open · [UNVERIFIED] Raz–Tal 2018 oracle separation | not-boundable |
| info-p0521 | 约束求解与优化 (季晓慧 et al.) | 521–523 | CSP dichotomy; random-CSP thresholds | partially solved: dichotomy proved · [Zhuk](https://arxiv.org/abs/1704.01914) (opened in the 2026-10-14 round) | not-boundable (the remainder is research directions) |
| info-p0524 | 计算复杂性若干未解决问题 (李昂生, 朱洪) | 524–526 (545–547) | L vs P; P vs PSPACE; NP vs PSPACE; P vs NP; Berman–Hartmanis isomorphism under P≠NP; Karp vs Cook reductions; P=BPP; RL=L | open · Clay (related); the article itself says new mathematics is needed | not-boundable |
| info-p0527 | 逻辑公式可满足性问题 (赵希顺, 李初民) | 527–529 (548–550) | Smallest a with 3-SAT in O(aⁿ) (book: 1.324); is UNIQUE-SAT D^P-complete? | open (base improved to ≈1.307 [UNVERIFIED] PPSZ line) | not-boundable |
| info-p0530 | Unique Games猜想 (张鹏) | 530–532 | Is Unique Games NP-hard? | open; 2-to-2 theorem proved with imperfect completeness · [KMS ECCC TR18-006](https://eccc.weizmann.ac.il/report/2018/006/) | not-boundable |
| info-p0533 | Tarski指数函数问题 (詹乃军) | 533–535 | Is Th(ℝ, +, ·, exp) decidable? | open (decidable assuming Schanuel [UNVERIFIED] Macintyre–Wilkie 1996) | not-boundable |
| info-p0545 | 非阿贝尔群上的隐子群问题 (孙晓明) | 545–547 | Efficient quantum algorithms for non-abelian HSP | open · [Kuperberg](https://arxiv.org/abs/quant-ph/0302112) (dihedral case subexponential only) | not-boundable |
| info-p0417 | 网络信息论 (尹长川 et al.) | 417–419 (438–440) | Capacity of the 3-node Gaussian relay channel and the 2-user Gaussian interference channel | open ("open for thirty years"; within one bit) · [Etkin–Tse–Wang](https://arxiv.org/abs/cs/0702045) | not-boundable |
| info-p0664 | 微分平坦系统的判定 (霍伟) | 664–666 (685–687) | A general method to decide flatness and find flat outputs | open · book p.665; known only for special classes | not-boundable |
| info-p0686 | 线性时变系统的渐近稳定性 (张龙, 谭峰, 段广仁) | 686–688 (707–709) | Practical necessary and sufficient conditions for asymptotic stability of x′=A(t)x | open, not precise · book pp.686–687 | not-boundable |

Not precise enough to catalog as difficult problems, though each was checked: info-p0400, 0406, 0411 (quantum and NIZK protocol design), 0423 (information-flow maximization), 0425, 0455, 0464 (iterative decoding), 0536 (DNA-computing detection), and the device, optics and metrology articles. Already settled with citations and skipped: info-p0539, info-p0542. AI4S dossiers skipped: the other 12 ids in the skip list.

## (c) Top three candidates for a 6-hour run

### #1 `info-p0403-q9bal242`: a balanced 9-variable Boolean function with nonlinearity 242

**Book (p.403, PDF 424; verbatim from the page image):**
> 当n为奇数且n≤7时，布尔函数的最大非线性度是2^{n−1}−2^{(n−1)/2}，并且可以是平衡的；当n为奇数且n≥9时，n元平衡布尔函数的最大非线性度还不知道。……如何构造非线性度严格大于2^{n−1}−2^{(n−1)/2}的奇数个变元的非Patterson-Wiedemann型平衡布尔函数也是目前颇受关注的问题。

*Translation:* For odd n ≤ 7 the maximum nonlinearity of Boolean functions is 2^{n−1}−2^{(n−1)/2}, and it can be attained by balanced functions. For odd n ≥ 9 the maximum nonlinearity of balanced n-variable functions is unknown. … How to construct odd-variable balanced functions that are not of Patterson–Wiedemann type and have nonlinearity strictly greater than 2^{n−1}−2^{(n−1)/2} is also a problem of much current interest.

**Formal statement.**
- Notation: for f: F₂⁹→F₂, let W_f(a) = Σ_x (−1)^{f(x)⊕a·x}, so nl(f) = 256 − max_a |W_f(a)|/2. f is balanced iff W_f(0) = 0.
- **Q:** is there an f with W_f(0)=0 and max_a |W_f(a)| ≤ 28?
- Facts used:
  - For balanced f every W_f(a) ≡ 0 (mod 4) (elementary weight-parity argument), so nl is even and NLB₉ ∈ {240, 242, 244}.
  - NLB₉ ≥ 240 is known. NLB₉ ≤ 244 follows from the covering-radius bound, which KY attribute to Helleseth–Kløve–Mykkeltveit 1978 and Hou 1997 (KY refs [8], [9]; primary [UNVERIFIED]). NLB₉ ≤ 242 holds if the unrefereed WLW 2026 claim is right.
  - The value 9 is the book's own smallest odd case; [ASSUMPTION] that n = 9 is the intended first instance.
- **Solved (positive, n=9 existence only):** an indexed 512-bit table with weight 256 and max|W| ≤ 28, its bit order and SHA-256, checked by FWHT and independent direct character sums. This does not prove optimality or a general odd-n construction; the claimed universal upper bound 242 is unrefereed.
- **Solved (negative):** a proof that none exists. That is out of 6-hour scope.
- **6-hour checkable advance:** a positive, or certified exact statements of the form "class C (orbit count k) has max nl = x overall and has no balanced f with nl ≥ 242", for invariant classes not previously enumerated exhaustively.

**Baseline (SOTA, sources opened).**
- Best known balanced value: 240. The [AMC 2020 Table 1](https://doi.org/10.3934/amc.2020010) "balanced" row has no entry above the bent-concatenation bound for n = 9 (opened by scout). [LXW arXiv:2610.17897](https://arxiv.org/abs/2610.17897) lists "Open problem 1. Does there exist a 9-variable balanced Boolean function with nonlinearity 242?". [WLW arXiv:2610.17871](https://arxiv.org/abs/2610.17871) §6 says "it is still an open problem to determine whether there exists a balanced 9-variable Boolean function with nonlinearity 242".
- Unbalanced 242: [Kavut–Yücel, Inf. Comput. 2010 / arXiv:0808.0684](https://arxiv.org/abs/0808.0684) found it in the 3-RSBF, 3-DSBF and permutation-invariant classes. Their words: "there is no zero value in the Walsh spectra of these functions; hence, none of them can be linearly transformed to 9-variable balanced functions with nonlinearity 242." The whole 2⁶⁰ RSBF class has been exhaustively searched (max 241). Their 30 permutation classes, including subsets "as small as 2⁷⁴", were searched **heuristically only**; they write that exhaustive search of the 2⁷⁴ subset "may be possible".
- Covering radius of RM(1,9): **claimed** to be 242 by WLW 2026, unrefereed.
- 2025 survey, [arXiv:2504.17666](https://arxiv.org/abs/2504.17666) (PDF read): its review of 9-variable results reports balanced functions only up to nl 240 (Carlet et al., evolutionary search on RSBFs), and unbalanced 241/242 (Kavut et al.). No balanced value above 240 appears.
- Re-checked here ([`probes/ky242_check.py`](probes/ky242_check.py)): the three nl-242 truth tables printed by KY (two 3-DSBFs and one 3-RSBF) have nl = 242, even weight (250, 250, 242), all W ≡ 0 (mod 4) and **zero Walsh zeros**. This confirms the obstruction stated above, and the tables can serve as positive controls and seeds.

**Attack plan.** The run is capped at 4 threads, 4 GB RAM and 1 GB disk; this plan stays within them.
1. *Prior-art pass (≤20 min).* Open the Kavut–Maitra(–Yücel) ePrints 2007/308, 2007/309 and 2007/321, which are [UNVERIFIED] now, and any later exhaustive class results. Drop any class that has already been enumerated.
2. *Exact local balancing around nl-242 seeds (≈1.5 h, kissat plus z3/numpy).*
   - Seeds: KY's printed tables (re-checked here) and further nl-242 functions from step 4.
   - Use only radii r ≥ |W_g(0)|/2: start at 6 for weight-250 seeds and at 14 for the weight-242 seed. Smaller radii are vacuous. Flipping S changes W(a) by −2·Σ_{x∈S}(−1)^{g(x)⊕a·x}. Report each seed's forced minimum alongside each radius.
   - Encoding: 512 flip variables, a cardinality bound on |S|, and 512 two-sided ±1-coefficient sum constraints.
   - Output: a find, or certified statements "no balanced nl ≥ 242 function within distance r of g". These are new, bounded and checkable.
3. *Exact class enumeration, only where feasible (≈2 h, 2 threads, C via clang).*
   - Method: orbit-bit DFS with the exact per-a remaining-mass bound |partial W(a)| − Σ_unassigned |c_O(a)| > T, with W(0)=0 for the balanced case.
   - Calibration from the probes:
     - generic MILP (HiGHS) failed on the RSBF facts in 70 s;
     - a plain C DFS on the 60-orbit RSBF class extrapolates to about 10⁷ CPU-seconds ([`probes/probe-results.txt`](probes/probe-results.txt) §4).
   - Before any exact enumeration, reject classes containing an affine conjugate of the nine-cycle shift: their functions are affine-equivalent to the already excluded RSBF class. In particular the proposed F₈* plus Frobenius example is not a new target. Enumerate only feasible, genuinely unscreened classes of ≲45 orbits.
   - Alternatively, first build a meet-in-the-middle / Kavut-style enumerator, and accept it only if it reproduces the RSBF facts (max 241, nothing ≥ 242) within 1 h.
   - Record the exact maximum nl per class, overall and balanced. A class reaching nl ≥ 243 would also refute WLW.
4. *Parallel heuristic (1 thread).*
   - Steepest descent / annealing in KY's rich classes (3-DSBF 2¹⁰⁴, 3-RSBF 2¹⁷⁶, and the 2⁷⁴ subsets), with cost Σ_a max(0,|W(a)|−28)² + λ·W(0)².
   - KY found nl 242 in 36 of 100 short 3-DSBF runs, so step 2 receives a supply of seeds.
   - A heuristic failure is never reported as nonexistence.

**Deliverable, verifier and controls.**
- **Deliverable:** either a balanced nl-242 truth table (hex), or certified negative statements: (i) per seed and radius, "no balanced nl ≥ 242 within distance r"; (ii) per small class, generators, orbit count, exact max nl overall and balanced, node counts, runtime and replay command.
- **Verifier:**
  - positive: an independent FWHT in numpy plus a second implementation;
  - per-class negatives: a separate encoding (a kissat cardinality CNF reporting UNSAT, or a differently written enumerator) must agree.
- **Negative control:** the RSBF facts above; a nl ≥ 240 balanced query must be satisfiable at once (the probe confirms this); a deliberately corrupted orbit table must be rejected by the FWHT check.
  - Agreement between solvers on one encoding is not independent certification. Audit mathematical-to-CNF correspondence with planted solvable cases and direct Walsh checks. Any unchecked UNSAT remains unchecked; an exact maximum requires an attaining witness. A heuristic may search for any zero Walsh coefficient and then add the corresponding linear function to balance without changing nonlinearity.
- **Kill criteria:**
  - If no enumerator reproduces the RSBF control within 1 h, exact mode is limited to classes of ≤45 orbits and the limit is reported.
  - Stop exhaustive mode on any class whose projected node count exceeds the remaining budget.
  - Never present a heuristic non-find as a result.

**Risks.**
1. Small classes may contain no nl-242 function at all, so excluding them has limited value. Mitigation: favour the local-neighbourhood certificates (step 2) and subclasses of rich classes.
2. Replication: unopened Kavut–Maitra papers may already have enumerated some classes; step 1 checks this.
3. The balanced maximum may simply be 240. LXW 2026 shows that at n=8 the balanced maximum stops short of the Seberry bound, and an analogous gap at n=9 would make every positive search futile [INFERENCE]. Negative certificates remain valid either way.
4. The upper bound of 242 rests on an unrefereed preprint. A positive find stands on its own regardless.

**openai/math:** no matching family, locally or remotely (§a).

**Plausibility [INFERENCE]:** finding a balanced 242 is low (≲5%). Certified local-neighbourhood statements are high. Certified exact maxima for small classes never enumerated before are medium, though of modest value.

### #2 `info-p0399`: APN permutations in dimension 8, residual linear-self-equivalence classes

**Book (p.399, PDF 420; verbatim):**
> 设映射φ:F_{2^n}→F_{2^n}为置换。如果对任意非零α，β∈F_{2^n}，方程φ(x+α)+φ(x)=β在有限域F_{2^n}上至多存在两个解，则称φ是一个APN置换。……当n=4时，已经证明不存在APN置换；当n=6时，在CCZ等价意义下仅找到一个APN置换。然而，当n为大于等于8的偶数时，是否存在APN置换还是一个公开难题。

*Translation:* Let φ be a permutation of F_{2^n}. If for all nonzero α (and all β) the equation φ(x+α)+φ(x)=β has at most two solutions, φ is an APN permutation. … For n=4 none exists; for n=6 only one is known up to CCZ-equivalence. For even n ≥ 8, whether APN permutations exist is still an open problem.

The printed definition quantifies over nonzero α and β. For a permutation the case β = 0 is vacuous, so this is the standard definition. The page also prints Hou's result as "Σ a_i x" with the exponent missing; the transcription in [`sources/info-p0399/excerpt.txt`](sources/info-p0399/excerpt.txt) keeps the misprint.

**Formal statement.**
- **Book question:** is there a bijection F: F₂⁸→F₂⁸ with |{x : F(x⊕a)⊕F(x)=b}| ≤ 2 for all a≠0 and all b?
- **6-hour sub-question.** BBL's own open problem is to "settle the cases described in Theorem 4". Here: is there an APN permutation G with G∘A = A∘G for either
  - **(Q22)** A = Comp(X⁴+X³+X²+X+1)⊕Comp(X⁴+X³+X²+X+1), of order 5, with 51 free orbits; or
  - **(Q30)** A = I₂⊕Comp(X²+1)³, an involution with 32 fixed points? Here G|Fix(A) must be an APN permutation of F₂⁵.
- [ASSUMPTION, to be checked in the run] Q22 is equivalent to asking for APN permutation polynomials Σ a_i x^i over F₂₅₆ with every i ≡ 1 (mod 5), via A = multiplication by a primitive 5th root of unity.
- **Solved:** an explicit table (positive), or a certified UNSAT for Q22 or Q30.

**Baseline (sources opened).**
- [Beierle–Brinkmann–Leander, IEEE TIT 2021 / arXiv:2003.12006](https://arxiv.org/abs/2003.12006): of 32 LE-automorphism classes for n=8, 15 are excluded by Propositions 4/5 and 15 by exhaustive search. Theorem 4 leaves Q22 and Q30. "We did not find any APN permutation by letting the algorithm run for at least 128 CPU days for each of those cases." The full classification is conditional on their Conjecture 1.
- [arXiv:2508.04644v2](https://arxiv.org/abs/2508.04644v2) (2025/26): 3,775,599 inequivalent quadratic APN functions in dimension 8. Per the scout, the text says none is CCZ-equivalent to a permutation.
- [Calderini–Sala–Villa](https://arxiv.org/abs/1511.08101): no quadratic APN permutation exists in even dimension.
- [Kuznetsov, arXiv:2606.11967](https://arxiv.org/abs/2606.11967) (unrefereed; PDF read): quadratic APN functions exist in the class-22 commutant subspace V_A. Remark 2 argues that the BBL2021 tree search "can miss globally valid solutions by early pruning". That remark concerns the earlier search for *quadratic* APN functions with self-equivalences, not BBL's exclusions of permutations. Treat it as a lead for re-checking, not a refutation. The paper's §D also states that existence of APN permutations in dimension 8 "remains open".
- [Baudrin–Canteaut–Perrin, ePrint 2026/1012](https://eprint.iacr.org/2026/1012): most sporadic APN functions in dimensions 6 and 8 are not CCZ-equivalent to an affinely self-equivalent function. This weakens how much an LE-symmetric search says about the full problem.

**Attack plan.**
1. A SAT/XOR encoding, run with kissat and cadical:
   - variables: output bits on orbit representatives (Q22: 408 variables);
   - APN constraint: G(x)⊕G(y)⊕G(z)⊕G(x⊕y⊕z) ≠ 0 for every orbit of 2-flats;
   - bijectivity;
   - symmetry breaking by the centralizer of A;
   - cube-and-conquer on 4 threads.
2. Calibration: recover Dillon's permutation for n=6 in its BBL class, and re-derive UNSAT for one BBL-closed n=8 class.
3. Main run on Q30, using the Fix(A) reduction to the APN permutations of F₂⁵, or on Q22.

**Deliverable, verifier and controls.**
- **Deliverable:** an APN permutation, or an UNSAT certificate.
- **Verifier:** an independent DDT and bijectivity checker; for UNSAT, an independently checked DRAT/LRAT proof. **Resource flag:** proof files may exceed the 1 GB disk cap. Fallback: check online, or require agreement of two encodings and two solvers, which is weaker.
- **Negative control:** a relaxed instance (differential uniformity ≤ 4) must be satisfiable; the n=8 closed-class control must come out UNSAT.
- **Kill:** if the closed-class control is not solved within 1 h, stop the UNSAT attempt.

**Plausibility [INFERENCE]:** closing a class is low; finding an APN permutation is very low.

### #3 `info-p0403-q8bal118`: audit of the claimed resolution "NLB₈ = 116"

**Book (p.403; verbatim):**
> Seberry等[2]曾给出具有偶数个变元的n元平衡布尔函数非线性度的一个上界2^{n−1}−2^{n/2−1}−2，但至今没人证明这个界是紧的。n≥8时，这个界是否能达到至今还不知道。8元(10元)平衡布尔函数的非线性度能否达到118(494)是目前受到关注的公开问题。

*Translation:* Seberry et al. gave the upper bound 2^{n−1}−2^{n/2−1}−2 for balanced functions in an even number n of variables, but nobody has proved it tight. For n ≥ 8 it is unknown whether it is attained. Whether balanced 8-variable (10-variable) functions can reach nonlinearity 118 (494) is an open problem of current interest.

**Formal statement.** Is there an f: F₂⁸→F₂ with W_f(0)=0 and max_a |W_f(a)| ≤ 20?

**Status: claimed "no".**
- Source: [Lou–Xu–Wang, arXiv:2610.17897](https://arxiv.org/abs/2610.17897), submitted 2026-10-13, unrefereed, 17 pages, pen-and-paper. Its proof reduces the question to Lemma 6: a 6-variable function at distance 4–6 from a bent function has nl ≤ 26.
- **Our check (2026-10-15):** in the wt(h)=5 case the paper writes Σ_ω C(N(ω),2) = C(5,2)·32 = 320.
  - For x≠y, the number of ω with φ_x(ω)=φ_y(ω)=1 is (28+28−32)/2 = 12, so the sum is 120.
  - The printed contradiction "192 < 320" therefore does not follow. With N ≤ 3 everywhere, the first two moments are satisfiable, e.g. counts (n₀,n₁,n₂,n₃) = (10,2,18,34).
  - Equivalent test (derived here): nl(f₁⊕1_S) ≥ 27 ⇔ N(ω) ≤ 3 for all ω.
  - Probe 2: 3753 random Maiorana–McFarland bent f₁ gave no counterexample in 240 s.
  - Probe 5: 3101 samples, each classified by an EA invariant (the rad-histogram of second derivatives). All **4 distinct invariant classes** were hit: 41 quadratic, plus 1421, 822 and 817 in the three cubic classes. The exhaustive 5-subset DFS found **0 counterexamples** in every class.
  - Conclusion: 6-variable bent functions form exactly 4 EA classes (Rothaus 1976, the book's ref. [1]; classical, primary not opened). Under that count, Lemma 6 holds for every bent f₁, and the counting slip is harmless. This is a probe result and has not been independently replayed. The wt 4 and wt 6 cases follow from the paper's own parity argument, which we re-derived.

**6-hour plan.**
1. Re-run the Lemma 6 check as a certificate: open Rothaus 1976 (or a modern classification) for the 4 representatives, use two independent implementations, and cover wt 4–6.
2. Machine-check every remaining finite identity and table, which is where any residual risk now lies: Proposition 1 (polar-rank-6 quadratic form), Table 1, Lemmas 3–5.
3. Optionally, do the same for the companion RM(1,9) claim ([2610.17871](https://arxiv.org/abs/2610.17871)). Its proof reduces to the Brier–Langevin classification of cubic forms in 9 variables, which is computable. That claim also bounds #1.

**Deliverable, verifier and controls.**
- **Deliverable:** a verification certificate or an erratum.
- **Verifier:** two independent implementations.
- **Negative control:** flipping one bit of a bent function must give nl 27, and the reformulated test must agree with a direct FWHT on random samples.

**Plausibility:** high for a full Lemma 6 certificate (the probe essentially shows it holds); medium for a full-proof audit in 6 h. Novelty value is now lower, because the one gap we found looks harmless.

**Flag:** this is verification of a claim. It does **not** meet criteria 2 and 3 as written (the status is "claimed", and the task is not an advance on an open question).

## (d) Recommendation #1 and rationale (FRONTIER §1)

**Recommend `info-p0403-q9bal242`.**

It meets the four criteria:
1. **Book-posed and precise.** The quote is from p.403. n=9 is the smallest instance and has an exact target value.
2. **Open on 2026-10-15.** Both 2026-10-13 preprints (opened) say it is open, and no resolution turned up in English, Chinese or openai/math searches.
3. **Named baseline and a 6-hour checkable advance.** The best known balanced value is 240; KY's unbalanced 242 functions have no Walsh zeros, and KY searched only heuristically. A truth table can be checked in milliseconds, and per-class exact maxima can be replayed independently.
4. **Not owned or attacked by AI4S.** The 2026-10-14 "too hard" verdict was inference-only, and the article id is not in `ai4s-owned.json`.

Value against plausibility:
- **Claim:** a balanced nl-242 function exists, or, per class, it does not.
- **Missing ingredient:** decidable searches, not new mathematics: exact neighbourhoods of known nl-242 functions, exhaustively enumerated small symmetry classes, and heuristic search in rich classes.
- **Decision value.** A find would answer a question listed as open by both 2026-10-13 preprints. Given WLW's claim, it would fix NLB₉ = 242 exactly and answer the book's odd-n construction question at n=9. The negative certificates are new, bounded and replayable statements that sharpen where a balanced 242 cannot lie. They are modest but real.
- **Honest caveat.** By the n=8 analogy, the balanced maximum at n=9 may be 240. If so, no 6-hour search can produce the positive find, and the expected yield is the negative certificates.

Why not the others as #1:
- **#2** has the larger prize but lower plausibility per 6 hours. Over 128 CPU-days per residual class have already failed, certificates may exceed the 1 GB cap, and the 2026 results weaken the relevance of LE-symmetric searches.
- **#3** is the most likely to produce a definite outcome. Our probes already indicate that the one gap we found (Lemma 6) is harmless, so the remaining value is a full audit of a 2-day-old claim. That is verification, not an advance, and is offered only as a parent decision.

## Notes for the parent
- `/Users/jinleic/jinleic-workspace/scratch/` (including `ai4s-venv`) disappeared between 02:27 and 02:31 PT. Probe 1 ran from it before it vanished; probes 2–5 used `/usr/bin/python3` or clang. Nothing was restored or recreated.
- Resources: #1 and #3 fit within 4 threads, 4 GB and 1 GB disk (SAT and enumeration logs are small). #2 may need more than 1 GB of disk for DRAT/LRAT proofs (flagged above). The research-explorer venv has numpy, z3, sympy and networkx but no scipy or numba; kissat 4.0.4, cadical 3.0.1 and clang are on PATH.
- During screening, one read-only `git ls-remote https://github.com/openai/math HEAD` was run to date the remote corpus. It touched no repository.
- Two unrefereed claims dated 2026-10-13 (LXW, WLW) bear directly on info-p0403. Any run on #1 or #3 should re-open them, in case of v2 revisions.
