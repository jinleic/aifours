# Mathematics volume — hard-problem catalog and 6-hour selection (2026-10-15 PT)

Volume: 《10000个科学难题·数学卷》 (Science Press 2009, ISBN 978-7-03-024267-9), 250 articles
(inventory `math.json`). Selection only: no attack was run beyond the ≤5-minute feasibility probes
described in §c.1. Prepared by the MathHardScreen agent; deadline 03:40 PT.

**Recommendation #1: `math-p0039`** — the nonexistence of non-Desarguesian flag-transitive
projective planes explicitly discussed in the article, formalized using Kantor and Thas–Zagier.
The six-hour visit permits a four-hour attack on a longer computed range past n < 2×10¹¹.
A finite range is partial progress; sampled cross-checks do not independently certify the whole range.

## a. Method, inputs, dated query log

**Inputs.**

- Book PDF `books/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf`. SHA-256 `3c69cf2c…2901`
  matches `books/README.md`. PDF page = book page + 16.
- Inventory `research-institute/explorer/inventory/math.json` (250 ids).
- Skip list: `ai4s-owned.json` (14 math ids) plus four articles whose exact titles appear in aifours
  dossier READMEs (p0061, p0064, p0081, p0141). These 18 are listed in `catalog.json` →
  `skipped_owned_or_dossier`.
- Prior screening: `aifours/mathematics/README.md` and `ai4s-crosswalk-20261014.json`.
- openai/math: the local clone `jinleic-workspace/math` (adc7f1241), grepping `lean/docs/*.md` titles
  and preprint `.tex`, plus the remote preprint listing from the GitHub API on 2026-10-15 (749
  entries, 27 newer than the local clone).

**Procedure.**

1. Listed all 250 articles and marked the skips.
2. Skimmed the text layer of about 45 candidate articles across the whole volume (logic, algebra,
   number theory, geometry, analysis, dynamics, combinatorics, complexity and optimization).
3. Read page images for the top candidates. Each top-3 quote below was checked against the PDF page
   image.
4. Checked status in primary sources: arXiv API, author and journal pages, plus two read-only scouts
   (`FoulkesLCCScout`, `FlagPlaneScout`) whose opened URLs and quotes are recorded below.
5. Ran two short compile-and-run feasibility probes for #1.

**Runtime note.** `/Users/jinleic/jinleic-workspace/scratch` (including `ai4s-venv`) disappeared
between 02:27 and 02:31 PT. It was not used, restored or touched. The probes used system `clang` in
`/tmp/ai4s-hard/math/probe/`.

**Query log (2026-10-15 PT; a search miss is a dated result, not proof of openness).**

| Topic | Queries / sources | Result |
|---|---|---|
| Flag-transitive planes | web: "Thas Zagier … flag-transitive verified n"; "flag-transitive … nonexistence verified computer order 10^12/10^13/10^14 special primes"; zh: "旗传递射影平面 非Desargues 存在性 Cayley图 二面体群 直径 李才恒"; zh: "非Desargues 旗传递 射影平面 不存在性 猜想 计算机验证 阶 n^2+n+1 素数"; arXiv API all:"flag-transitive" AND all:"projective plane" (25 newest); arXiv API "cyclotomic difference set" / "Gauss period" + "projective plane" (newest 2015); Semantic Scholar lists of all 25 papers citing Thas–Zagier (DOI 10.4171/JEMS/107; newest 2026) and all 24 citing Li 2005; scout FlagPlaneScout (2 searches) | Opened: Thas–Zagier JEMS 2008 (full text), Xia arXiv 1707.05486v7 (full text, Jan 2023; EJC doi 10.1016/j.ejc.2023.103687), Li PAMS 2005 abstract. **No extension of the n < 2×10¹¹ range found**, including among the citing papers. Chinese queries returned only English-language sources. |
| Prime power conjecture (planar difference sets) | arXiv API all:"planar difference set" OR all:"prime power conjecture"; scout | Opened: Baumert–Gordon math/0304502 (cyclic, n ≤ 2×10⁹); **Gordon arXiv 2007.07292 (2020): PPC true up to 2·10¹⁰** (the scout missed this); Peluse, Math. Ann. 2021 (asymptotic). |
| Covering systems / Herzog–Schönheim | zh: "Herzog-Schönheim 猜想 群 陪集 不相交覆盖 指标 两两互异 进展"; scout searches | Opened: Margolis–Schnabel arXiv 1803.03569 ("order smaller than 1440"), Garonzi–Margolis arXiv 2509.25118. Scout-opened: BBMST (616000), Hough–Nielsen, Mian–Siddique arXiv 2607.25628 (Lean, odd-covering lcm > 10000), Erdős problems #2 and #7. |
| Foulkes, list colouring | scout FoulkesLCCScout (arXiv, EJC, author pages) | Foulkes: a ≥ 6 open in the literature; Müller–Neunhöffer 2005 checked n+m ≤ 17. openai/math **claims a = 6** and b ≥ a(a−1). LCC: K₁₀ settled computationally (Schauz 2017); K₁₆ "completely out of reach". |
| Self-avoiding walks | scout | Couronné (J. Stat. Phys. 2025): μ₂ ≤ 2.662342426 after one week with 32 GB. |
| Hajós | web "Hajós cycle decomposition … verified" | Opened arXiv 1705.08724: verified up to 12 vertices. |
| openai/math | grep `lean/docs` and preprint `.tex` for flag-transitive / Desarguesian / special prime / Gaussian period / planar difference set / prime power conjecture / Herzog / Schönheim / covering system / odd covering / minimum modulus; remote listing | **No hit on any top-3 topic.** The only matches were unrelated: Boone–Higman ("Higman") and Lech's conjecture ("Herzog" as an author name). Claims noted for other book problems: Foulkes a=6 (210), Hilbert's 16th uniform bound, off-diagonal Ramsey, circulant Hadamard (179), Hadwiger counterexample, Turing-degree rigidity (241), Brennan (072), Koebe (071), Rokhlin (145), finitistic dimension (198), Auslander–Reiten (199), and Ryser's *covering* conjecture (not the Latin-square one). |

## b. Catalog of difficult problems

Columns: id · zh title · authors · book (PDF) pages · question · status (dated 2026-10-15) and key
source · budget class · plausibility for 6 h. "[INFERENCE …]" marks statuses from prior knowledge
that were not re-opened this round. Those are leads only and do not count as checks. The 18
owned/dossier articles are excluded, as are 97 articles that pose programmes or directions rather
than recognized hard precise questions (numerical methods, statistics, modelling, symbolic-computation
programmes) or specialist questions not re-read. All of them are listed in `catalog.json`.

| id | 题目 | authors | book (PDF) pp. | question | status (2026-10-15) · key source | budget | 6h plausibility |
|---|---|---|---|---|---|---|---|
| `math-p0001` | 奥特 (Vaught) 猜想与拓扑奥特猜想 | 高速 | 1-2 (17-18) | Does every countable complete first-order theory have either ≤ℵ0 or 2^ℵ0 countable models (and the Polish-group-action analogue)? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0003` | 超紧基数典型内模型问题 | 冯琦 | 3-4 (19-20) | Construct a canonical (fine-structural) inner model with a supercompact cardinal. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0005` | 递归可枚举度中的格嵌入问题和双量词理论可判定性问题 | 杨跃 | 5-6 (21-22) | Which finite lattices embed into the c.e. Turing degrees preserving 0 and 1? Is the two-quantifier theory decidable? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0007` | 高层有限波雷尔 (Borel) 等价关系中的两个问题 | 高速 | 7-8 (23-24) | Problems on hyperfinite / treeable countable Borel equivalence relations posed in the article. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0010` | r = rω ? 及 s = sω ? | 张树果 | 10-10 (26-26) | Are the reaping/splitting numbers equal to their σ-versions? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0011` | 连续统势确定问题 | 冯琦 | 11-12 (27-28) | Settle the value of 2^ℵ0 (CH program). | not a ZFC question; open program [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0013` | 奇异基数问题 | 冯琦 | 13-14 (29-30) | Determine the possible behaviour of 2^κ at singular κ. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0015` | 萨克斯 (Sacks) 关于波斯特 (Post) 问题的度不变解问题和马丁 (Martin) 猜想 | 杨跃 | 15-16 (31-32) | Is there a degree-invariant solution to Post's problem; is Martin's conjecture true? | open (partial results) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0017` | 图灵 (Turing) 等价问题 | 高速 | 17-18 (33-34) | Is Turing equivalence a universal countable Borel equivalence relation? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0019` | 图灵 (Turing) 度的自同构问题 | 杨跃 | 19-20 (35-36) | Is the structure of the Turing degrees rigid? | claimed (openai/math family 241) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/241.md) | not-boundable | — |
| `math-p0021` | 是否存在一个稳定的一阶完全理论，它有大于一的有穷多个可数模型 | 史念东 | 21-22 (37-38) | Is there a stable complete theory with n countable models, 1<n<ℵ0 (Lachlan)? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0023` | Cherlin-Zilber 猜想 | 庞炜恩 | 23-23 (39-39) | Is every simple group of finite Morley rank an algebraic group over an algebraically closed field? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0024` | 带指数函数的实数理论的可判定性问题 | 庞炜恩 | 24-25 (40-41) | Is Th(ℝ, +, ·, exp) decidable (Tarski)? | open; decidable conditional on Schanuel (Macintyre–Wilkie) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0026` | Shelah 唯一性猜想 | 庞炜恩 | 26-26 (42-42) | As posed in the article (model theory). | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0028` | 3-Calabi-Yau 代数的分类 | 章璞 | 28-29 (44-45) | Classify 3-CY algebras. | open program [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0035` | 布如意 (Broué) 交换亏群猜想 | 张继平 | 35-36 (51-52) | Is a block with abelian defect group derived equivalent to its Brauer correspondent? | open in general; many cases known [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0039` | 凯莱 (Cayley) 图和相关的问题 | 李才恒 | 39–40 (55–56) | The geometric conjecture explicitly discussed in the article: every finite flag-transitive projective plane is Desarguesian. The printed Cayley-graph formulation is inconsistent; see §c.1. | No later range extension located in the dated screen; baseline n < 2×10¹¹, [Thas–Zagier](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.4171/JEMS/107/fulltext.pdf); [Xia](https://arxiv.org/abs/1707.05486) | 6h-scoped visit, including ≤4h attack | A production range extension looks plausible [INFERENCE]; independent exhaustive certification is not promised |
| `math-p0041` | 福克斯 (Foulkes) 猜想 | 王立中 | 41-42 (57-58) | For a ≤ b, is h_a[h_b] contained in h_b[h_a] (plethysm)? | open in literature for a ≥ 6; openai/math claims a = 6 (all b ≥ 6) and every b ≥ a(a−1); computationally checked up to n+m ≤ 17 (Müller–Neunhöffer 2005) · [opened](https://arxiv.org/abs/1509.03944); [opened](http://www.math.rwth-aachen.de/~Max.Neunhoeffer/Publications/pdf/foulkes.pdf); [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/210.md) | multi-day (~72 h) | low |
| `math-p0043` | 戈伦斯坦 (Gorenstein) 对称猜想 | 陈小伍, 章璞 | 43-44 (59-60) | Is the injective dimension of an Artin algebra as left module equal to that as right module? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0045` | 卡普兰斯基 (Kaplansky) 第六猜想 | 陈惠香 | 45-46 (61-62) | Does the dimension of every simple module of a semisimple Hopf algebra divide dim H? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0047` | 中山 (Nakayama) 猜想和广义中山 (Nakayama) 猜想 | 郭晋云 | 47-48 (63-64) | As stated (homological conjectures for Artin algebras). | open; openai/math claims Auslander–Reiten (199) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/199.md) | not-boundable | — |
| `math-p0053` | 巴斯–奎伦 (Bass-Quillen) 猜想 | 丁南庆 | 53-54 (69-70) | Are f.g. projective modules over R[x1..xn] extended from regular R? | open in general [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0057` | 非交换曲面的分类 | 吴泉水, 张坚 | 57-58 (73-74) | Artin's conjecture on noncommutative projective surfaces. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0059` | 关于码交换等价于前缀码的猜测 | 郭聿琦 | 59-60 (75-76) | Is every finite maximal code commutatively equivalent to a prefix code (Perrin–Schützenberger)? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0068` | 广义倾斜模中的两个猜想 | 叶郁, 章璞 | 68-69 (84-85) | Wakamatsu-tilting-type conjectures as stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0070` | 考克斯特群的胞腔 | 时俭益 | 70-71 (86-87) | Lusztig's conjectures on cells of affine Weyl groups (e.g. left-connectedness of left cells). | open in general [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | multi-day (~100 h) | low |
| `math-p0072` | 满足正规子群极小条件的可解群的 Fitting子群是否是幂零的？ | 刘合国 | 72-73 (88-89) | As titled. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0074` | 模代数 smash 积的半素性 | 朱胜林 | 74-75 (90-91) | Is A#H semiprime for semiprime H-module algebra A, semisimple H? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0078` | 稳定等价猜想 | 张英伯 | 78-80 (94-96) | Do stably equivalent Artin algebras have the same number of non-projective simples (Auslander–Reiten)? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0087` | 有限维数猜想 | 黄兆泳 | 87-88 (103-104) | Is findim of every Artin algebra finite? | claimed (openai/math family 198) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/198.md) | not-boundable | — |
| `math-p0089` | ABC 猜测 | 袁平之 | 89-90 (105-106) | As stated. | open (Mochizuki claim not accepted) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0091` | 巴斯 (Bass) 猜想和索尔 (Soule) 猜想 | 秦厚荣 | 91-92 (107-108) | Finite generation of K-groups of regular finitely generated rings; Soulé's conjecture. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0093` | Lichtenbaum 猜想 | 秦厚荣 | 93-94 (109-110) | Special values of zeta functions via motivic cohomology. | open in general [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0095` | 里德–所罗门 (Reed-Solomon) 码的译码问题 | 万大庆 | 95-97 (111-113) | Q1: is MLD for standard RS codes polynomial/NP-hard? Q2: compute error distance in polynomial time? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0098` | 沙努尔 (Schanuel) 猜想 | 姚家燕 | 98-100 (114-116) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0101` | 哥德巴赫 (Goldbach) 猜想 | 贾朝华 | 101-103 (117-119) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0104` | 关于不同模覆盖系的厄尔多斯 (Erdös) 问题 | 孙智伟 | 104-106 (120-122) | Min-modulus problem; odd covering (Erdős–Selfridge); Herzog–Schönheim (disjoint coset partitions have a repeated index); Sun's gcd conjecture. | min-modulus answered negatively (Hough 2015; bound 616000 BBMST; record 42); odd covering open; HS open, verified for \|G\| < 1440 (2019; unchanged in 2025) · [opened](https://arxiv.org/abs/1811.03547); [opened](https://arxiv.org/abs/1703.02133); [opened](https://arxiv.org/abs/2607.25628); [opened](https://www.erdosproblems.com/2); [opened](https://www.erdosproblems.com/7); [opened](https://arxiv.org/abs/1803.03569); [opened](https://arxiv.org/abs/2509.25118) | 6h-scoped (~6 h) | low–medium (HS range extension; needs GAP SmallGroups); low (min modulus 43) |
| `math-p0107` | 关于倒数和发散序列的厄尔多斯–图兰 (Erdös-Turán) 猜想 | 孙智伟, 潘颢 | 107-108 (123-124) | If Σ1/a diverges, does A contain arbitrarily long APs? | open (k=3 known, Bloom–Sisask) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15]; openai/math title 159 suggests overlap, not compared · — | not-boundable | — |
| `math-p0112` | 关于有限域上代数曲线点数的 Drinfeld-Vladt 界 | 冯克勤 | 112-113 (128-129) | Determine A(q), in particular for non-square q. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0114` | 朗兰兹 (Langlands) 纲领 | 叶扬波, 刘建亚 | 114-121 (130-137) | As stated. | open programme · — | not-boundable | — |
| `math-p0122` | 类数 1 实二次域的高斯猜想 | 冯克勤 | 122-123 (138-139) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0124` | 黎曼 (Riemann)zeta 函数在奇正整数点处值的超越性 | 姚家燕 | 124-125 (140-141) | Are ζ(2k+1) transcendental (irrational)? | open beyond ζ(3) irrational [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0126` | 黎曼 (Riemann) 猜想 | 贾朝华 | 126-128 (142-144) | As stated. | open · — | not-boundable | — |
| `math-p0129` | 欧拉常数的超越性 | 姚家燕 | 129-130 (145-146) | Is γ transcendental (irrational)? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0131` | 椭圆曲线的 BSD 猜想 | 冯克勤 | 131-132 (147-148) | As stated. | open; remote openai/math has partial BSD-formula preprints (Oct 2026, not compared) · — | not-boundable | — |
| `math-p0133` | 希尔伯特第九问题：高斯二次互反律如何推广 | 冯克勤 | 133-135 (149-151) | General reciprocity laws. | open programme [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0136` | 希尔伯特第十二问题：构作数域的最大阿贝尔扩域 | 冯克勤 | 136-137 (152-153) | Explicit class field theory for number fields. | open in general [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0138` | 岩泽 (Iwasawa) 理论的主猜想 | 欧阳毅 | 138-140 (154-156) | As stated in generality. | proved in many cases; general open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0148` | 格里菲思 (Griffiths) 问题 | 陈伯勇 | 148-148 (164-164) | As stated. | openai/math title 050 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0149` | 哈茨霍恩 (Hartshorne) 猜想 | 谈胜利 | 149-151 (165-167) | Smooth X^n ⊂ P^N with n > 2N/3 is a complete intersection? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0152` | 饭高 (Iitaka) 猜想：Cn,m | 陈猛 | 152-153 (168-169) | Subadditivity of Kodaira dimension. | open in general; openai/math title 033 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0154` | 长田 (Nagata) 猜想 | 杨劲根 | 154-155 (170-171) | As stated. | open; openai/math title 039 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0158` | Tate 猜想 | 扶磊 | 158-159 (174-175) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0162` | 格拉腾迪克 (Grothendieck) 标准猜想 | 扶磊 | 162-163 (178-179) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0166` | 局部上同调模的相伴素理想的有限性问题 | 唐忠明 | 166-167 (182-183) | Huneke's question. | false in general (Singh, Katzman); open for regular rings in some settings [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0172` | 奇点解消 | 杨劲根 | 172-173 (188-189) | In positive characteristic, dimension ≥ 4. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0179` | 雅可比猜想 | 余解台 | 179-180 (195-196) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0181` | 霍普夫 (Hopf) 猜想 | 忻元龙 | 181-183 (197-199) | Does S²×S² admit positive sectional curvature? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0191` | 六维球面上复结构的存在性问题 | 唐梓洲 | 191-191 (207-207) | Does S^6 admit an integrable complex structure? | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0192` | 曲面到四维欧氏空间的等距浸入的存在性 | 唐梓洲 | 192-192 (208-208) | As posed. | openai/math title 333 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0193` | 3 维流形上 tight 切触结构的分类 | 丁帆 | 193-194 (209-210) | As posed. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0195` | 4 维光滑庞加莱 (Poincaré) 猜想 | 丁帆 | 195-195 (211-211) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0196` | 波雷尔 (Borel) 猜想: 非球面性闭流形之间的同伦等价必同伦于一个同胚 | 郁国樑, 徐胜芝 | 196-197 (212-213) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0198` | 11/8 猜想 | 方复全 | 198-199 (214-215) | As stated. | open (10/8+4 known) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0200` | Kashaev-Murakami-Murakami 体积猜想 | 罗锋 | 200-201 (216-217) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0202` | 瑟斯顿 (Thurston) 有效纤维化猜想 | 罗锋 | 202-202 (218-218) | As stated. | solved (Agol 2013) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0203` | Virtual Haken 猜想 | 雷逢春 | 203-204 (219-220) | As stated. | solved (Agol 2013) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0205` | 仿射平坦流形的陈猜想 | 于立 | 205-206 (221-222) | Euler characteristic vanishes. | open in general (special affine case known) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0215` | 纽结的交叉点数的计算和可加性 | 杨志青 | 215-216 (231-232) | Is c(K#K') = c(K)+c(K')? | open (Lackenby lower bound) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | multi-day (~48 h) | very low |
| `math-p0217` | 纽结的解结数的计算和可加性 | 杨志青 | 217-218 (233-234) | Determine u(K); is u additive; is u(K1#…#Kn) ≥ n? | additivity answered negatively (Brittenham–Hermiller, arXiv 2506.24088, not re-opened) [UNVERIFIED]; u ≥ n open · — | multi-day (~48 h) | low |
| `math-p0222` | osp 型李超代数的特征标问题 | 苏育才 | 222-223 (238-239) | As posed. | solved (Gruson–Serganova; parent-opened 2026-10-14) · — | not-boundable | — |
| `math-p0238` | 齐性爱因斯坦 (Einstein) 流形 | 邓少强, 侯自新 | 238-240 (254-256) | As posed. | Alekseevskii conjecture solved (Böhm–Lafuente; parent-opened 2026-10-14) · — | not-boundable | — |
| `math-p0241` | 有理顶点算子代数的分类 | 姜翠波 | 241-242 (257-258) | As posed. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0249` | 3n + 1 猜想与复解析方法 | 李玉华 | 249-250 (265-266) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0251` | 布洛克 (Bloch) 常数 | 刘劲松 | 251-251 (267-267) | Determine B (conjectured Ahlfors–Grunsky value). | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0252` | 博克纳–里斯 (Bochner-Riesz) 乘子问题 | 杨大春 | 252-254 (268-270) | As stated (n ≥ 3). | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0255` | 布伦南 (Brennan) 猜测 | 伍胜健 | 255-256 (271-272) | As stated. | claimed (openai/math family 072) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/072.md) | not-boundable | — |
| `math-p0257` | 傅里叶 (Fourier) 变换的限制性问题 | 杨大春 | 257-259 (273-275) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0262` | 挂谷 (Kakeya) 问题 | 杨大春 | 262-264 (278-280) | As stated. | solved in R^3 (Wang–Zahl 2025) [UNVERIFIED]; open n ≥ 4 · — | not-boundable | — |
| `math-p0265` | Koebe 问题 | 贺正需 | 265-265 (281-281) | As stated. | claimed (openai/math family 071) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/071.md) | not-boundable | — |
| `math-p0266` | 庞加莱 (Poincaré) 圆盘上调和映射的舍恩 (Schoen) 猜想 | 漆毅, 李忠 | 266-267 (282-283) | As stated. | solved (Marković) [UNVERIFIED] · — | not-boundable | — |
| `math-p0272` | 斯梅尔 (Smale) 均值猜想 | 王跃飞 | 272-273 (288-289) | Constant K = 1 or (d−1)/d. | open (degree-5 computer proof by Crane reported) [UNVERIFIED] · — | multi-day (~72 h) | low |
| `math-p0274` | 双曲猜想 | 王跃飞, 崔贵珍 | 274-275 (290-291) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0276` | 双线性希尔伯特 (Hilbert) 变换的 Lp 有界性 | 颜立新 | 276-277 (292-293) | Range below 2/3. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0280` | 亚纯函数与其导函数有公共的波雷尔 (Borel) 方向吗？ | 张广远 | 280-282 (296-298) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0284` | 阿诺德 (Arnold) 猜想 | 刘春根 | 284-286 (300-302) | As posed. | openai/math title 347 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0289` | 菲尔斯滕贝格 (Fürstenberg) 猜想 | 黄文, 叶向东 | 289-290 (305-306) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0291` | 埃农 (Hénon) 映射族中奇异吸引子的存在性问题 | 王兰宇 | 291-292 (307-308) | Existence for classical parameters. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0293` | 希尔伯特 (Hilbert) 第 16 问题 | 李承治 | 293-294 (309-310) | Is H(n) finite; determine H(n). | claimed: openai/math preprint 'Uniform bounds for planar polynomial limit cycles' (2026-09-24) claims uniform finiteness · [opened](/Users/jinleic/jinleic-workspace/math/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/) | not-boundable | — |
| `math-p0295` | Palis 猜测 | 文兰 | 295-296 (311-312) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0297` | 罗林 (Rohlin) 问题 | 邵松, 叶向东 | 297-298 (313-314) | As stated. | claimed (openai/math family 145) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/145.md) | not-boundable | — |
| `math-p0301` | 魏因施泰因 (Weinstein) 猜想 | 蒋美跃 | 301-303 (317-319) | Higher dimensions. | dim 3 solved (Taubes); higher open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0307` | 关于闸轨道多重性的塞弗特 (Seifert) 猜想 | 张端智 | 307-309 (323-325) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0312` | 紧流形上的闭测地线猜想 | 龙以明 | 312-314 (328-330) | As posed. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0315` | 弱 Pinsker 猜想 | 黄文, 叶向东 | 315-316 (331-332) | As stated. | solved (Austin 2018) [UNVERIFIED] · — | not-boundable | — |
| `math-p0317` | 天体力学中的中心构型有限性猜想 | 孙善忠 | 317-319 (333-335) | Finitely many CCs for every positive mass vector, n ≥ 5? | open for n ≥ 5 (n=4 Hampton–Moeckel; n=5 generic Albouy–Kaloshin) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | multi-day (~100 h) | low |
| `math-p0320` | 波利亚 (Pólya) 猜测 | 戴求亿 | 320-321 (336-337) | λ_k ≥ 4πk/\|Ω\| for all domains. | open in general (balls proved 2023) [UNVERIFIED] · — | not-boundable | — |
| `math-p0327` | 不可压缩纳维耶–斯托克斯 (Navier-Stokes) 方程 | 何成 | 327-329 (343-345) | As stated. | open · — | not-boundable | — |
| `math-p0336` | 非线性椭圆方程中的 De Giorgi及吉本斯 (Gibbons) 猜想 | 魏军城 | 336-338 (352-354) | As stated. | De Giorgi: solved n ≤ 8 (with conditions), counterexample n ≥ 9 [UNVERIFIED] · — | not-boundable | — |
| `math-p0381` | 量子杨–米尔斯 (Yang-Mills) 千禧问题 | 王世坤, 吴可 | 381-383 (397-399) | As stated. | open · — | not-boundable | — |
| `math-p0386` | 彭罗斯 (Penrose) 猜想 | 白姗, 刘润球 | 386-387 (402-403) | As stated. | openai/math title 260 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0395` | 宇宙监督假设 | 白姗, 刘润球 | 395-396 (411-412) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0397` | 亨特 (Hunt) 假设与 Getoor 猜测 | 应坚刚 | 397-398 (413-414) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0410` | 最热点猜测 | 陈振庆 | 410-412 (426-428) | As stated. | openai/math title 369 (planar simply connected) suggests overlap; high-dimensional counterexamples reported · — | not-boundable | — |
| `math-p0413` | 阿达马 (Hadamard) 矩阵存在性 | 葛根年, 向青, 殷剑兴 | 413-414 (429-430) | Hadamard conjecture; smallest open order 668; circulant Hadamard conjecture. | Hadamard conjecture open (668 open [INFERENCE]); circulant conjecture claimed by openai/math (179) · [opened](/Users/jinleic/jinleic-workspace/math/lean/docs/179.md) | multi-day (~200 h) | very low |
| `math-p0415` | Hadwiger 猜想 | 许宝刚 | 415-416 (431-432) | As stated. | claimed false (openai/math preprint, Sep 2026) · — | not-boundable | — |
| `math-p0419` | 韦斯 (Weiss) 有限局部本原图猜想 | 冯衍全 | 419-420 (435-436) | Vertex stabilizers bounded by a function of valency. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0421` | 并闭集猜想 | 王军 | 421-421 (437-437) | As stated. | open (constant ≈0.38 known) [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0422` | 独立系的 Chvátal 猜想 | 王毅 | 422-423 (438-439) | As stated. | open; unrefereed 2026 claims (README) · — | not-boundable | — |
| `math-p0424` | 非素数幂阶射影平面的存在性 | 葛根年 | 424-424 (440-440) | Does a projective plane of non-prime-power order exist? (Sub-question: cyclic/abelian planar difference sets — prime power conjecture.) | open; PPC for abelian planar difference sets verified for n ≤ 2×10^10 (Gordon 2020); cyclic n ≤ 2×10^9 (Baumert–Gordon); PG(2,12) open · [opened](https://arxiv.org/abs/math/0304502); [opened](https://arxiv.org/abs/2007.07292); [opened](https://arxiv.org/abs/2003.04929) | 6h-scoped (~6 h) | medium-low (range extension beyond 2×10^10) |
| `math-p0425` | 经典拉姆齐 (Ramsey) 函数的估值 | 李雨生 | 425-427 (441-443) | Improve asymptotic bounds on r(n,n) and r(m,n). | open; diagonal upper bound improved (Campos–Griffiths–Morris–Sahasrabudhe 2023) [UNVERIFIED]; off-diagonal claimed by openai/math · [opened](/Users/jinleic/jinleic-workspace/math/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/) | not-boundable | — |
| `math-p0430` | 拉丁方的横截问题 | 李学良 | 430-431 (446-447) | Every odd-order Latin square has a transversal; every Latin square has a partial transversal of size n−1. | open (Brualdi–Stein asymptotically, Montgomery 2023 [UNVERIFIED]) · — | not-boundable | — |
| `math-p0432` | 列表染色猜想 | 许宝刚 | 432-433 (448-449) | χ_l(L(G)) = χ(L(G)) for all G; Gravier–Maffray for claw-free graphs. | open; K_{p+1} proved (Schauz 2014); K_10 by computation (Schauz 2017, [INFERENCE]); K_16 open and 'out of reach' · [opened](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v21i3p43); [opened](https://arxiv.org/abs/1705.00484) | multi-day (~500 h) | very low |
| `math-p0438` | 双圈覆盖猜想 | 张存铨 | 438-439 (454-455) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0440` | 凸多边形与厄尔多斯 -Szekeres(Erdös-Szekeres) 问题 | 李学良 | 440-441 (456-457) | f(n) = 2^{n−2}+1; determine g(6). | f(n) open (f(6)=17 known); g(6)=30 solved (Heule–Scheucher 2024) [UNVERIFIED] · — | multi-day (~10000 h) | very low |
| `math-p0442` | 图的 Pfaffian 定向 | 张福基 | 442-443 (458-459) | Characterize/recognize Pfaffian (non-bipartite) graphs efficiently. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0444` | 图的重构猜想 | 洪渊 | 444-445 (460-461) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | multi-day (~1000 h) | very low |
| `math-p0446` | 整数流猜想 | 范更华 | 446-447 (462-463) | Tutte's 5-, 4-, 3-flow conjectures. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0448` | 子图覆盖问题 | 范更华 | 448-449 (464-465) | Gallai path decomposition; Hajós cycle decomposition; Fulkerson's conjecture. | all three open; Hajós verified up to 12 vertices (2017) · [opened](https://arxiv.org/abs/1705.08724) | multi-day (~48 h) | low |
| `math-p0450` | 自回避行走的计数问题 | 陈永川, Richard P. Stanley | 450-452 (466-468) | Exact c_n, connective constants, exponents γ, ν, SLE_{8/3} limit. | open; rigorous μ₂ ≤ 2.662342426 (Couronné 2025) · [opened](https://link.springer.com/article/10.1007/s10955-025-03542-6) | multi-day (~170 h) | low |
| `math-p0453` | P=NP? | 高小山, 朱洪 | 453-455 (469-471) | As stated. | open · — | not-boundable | — |
| `math-p0456` | 单向函数的存在性 | 邓映蒲 | 456-456 (472-472) | As stated. | open · — | not-boundable | — |
| `math-p0460` | 大数分解是否有多项式算法? | 冯克勤 | 460-462 (476-478) | As stated. | open · — | not-boundable | — |
| `math-p0463` | 离散对数求解问题 | 龚贤 | 463-465 (479-481) | Polynomial-time DLP algorithm? | open · — | not-boundable | — |
| `math-p0466` | 多变元公钥密码中 MQ 问题是否存在有效算法? | 刘卓军 | 466-468 (482-484) | Efficient algorithm for multivariate quadratic systems? | open · — | not-boundable | — |
| `math-p0469` | “最小秩”问题是否存在有效算法? | 刘卓军 | 469-470 (485-486) | Efficient algorithm? | open · — | not-boundable | — |
| `math-p0482` | 平面向量场不变曲线次数的庞加莱 (Poincaré) 问题 | 冯如勇 | 482-484 (498-500) | Bound the degree of invariant algebraic curves of planar vector fields. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0485` | 微分代数簇的不可缩分解 | 高小山 | 485-486 (501-502) | Decide inclusion of components algorithmically. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0494` | 阿蒂亚 (Atiyah) 猜想 | 李洪波 | 494-494 (510-510) | As stated (n points). | n ≤ 4 known; n=5 claim unverified (README) · — | not-boundable | — |
| `math-p0525` | 推广的 Lax 猜想：双曲锥能表示为半定锥的一个截面 | 修乃华 | 525-526 (541-542) | Every hyperbolicity cone is spectrahedral? | open; openai/math title 095 suggests overlap (not compared) · — | not-boundable | — |
| `math-p0529` | 最小阻力凸体问题 | 戴彧虹 | 529-531 (545-547) | Structure of minimizers. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0532` | 是否存在求解性线性规划的强多项式时间算法? | 张树中, 何斯迈 | 532-534 (548-550) | As stated. | open · — | not-boundable | — |
| `math-p0539` | k- 服务器猜想 | 徐寅峰 | 539-540 (555-556) | Deterministic ratio k. | deterministic open; randomized version refuted 2023 [UNVERIFIED] · — | not-boundable | — |
| `math-p0541` | 是否存在求解装箱问题的绝对近似算法 | 张国川 | 541-542 (557-558) | As stated. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |
| `math-p0544` | 位相型分布的最小表示 | 何启明, 张汉勤 | 544-545 (560-561) | Determine minimal order of a PH representation. | open [INFERENCE: status from prior knowledge, not re-opened 2026-10-15] · — | not-boundable | — |

Skipped (owned by AI4S dossiers or settled with citation): `math-p0009`, `math-p0030`, `math-p0061`, `math-p0064`, `math-p0066`, `math-p0081`, `math-p0109`, `math-p0141`, `math-p0165`, `math-p0226`, `math-p0408`, `math-p0417`, `math-p0428`, `math-p0436`, `math-p0521`, `math-p0527`, `math-p0535`, `math-p0537`.

## c. Top 3 candidates for a 6-hour run

### c.1 #1 — `math-p0039` Problem 3: flag-transitive projective planes (凯莱 (Cayley) 图和相关的问题, 李才恒; book p. 39, PDF p. 55)

**Verbatim (checked against the page image of PDF p. 55):**

> 最后, 令 G 是阶为 2p 的二面体群, 其中 p = n² + n + 1 是素数. 假定 n > 8, S 是由 G 中 n+1 个共轭对合组成的集合, 令 Cay(p)=Cay(G, S), 那么 Cay(p) 的直径至多为 3, 并且直径为 3 的图 Cay(p) 的存在性等价于 n 阶非 -Desarguesian 旗传递射影平面的存在性, 参见文献 [2]∼[4]. 后者是几何学中的一个重要问题, 其不存在性是几何学中一个著名的猜想. 因此, 我们提出
> **问题 3** 证明对于所有的素数 p = n²+n+1 使得 n > 8, 图 Cay(p) 的直径等于 2.

**Translation.** "Finally, let G be the dihedral group of order 2p, where p = n²+n+1 is prime.
Assume n > 8, let S be a set of n+1 conjugate involutions of G, and put Cay(p) = Cay(G, S). Then
Cay(p) has diameter at most 3. The existence of a diameter-3 graph Cay(p) is equivalent to the
existence of a non-Desarguesian flag-transitive projective plane of order n [2–4]. The latter is an
important problem in geometry, and its non-existence is a famous conjecture. We therefore propose
**Problem 3**: prove that for every prime p = n²+n+1 with n > 8, the graph Cay(p) has diameter 2."

**Precision caveat (accepted with disclosure after parent review).** The printed reflection-generated
Cayley graph is bipartite with parts of size p and valency n+1 < p, so diameter two is impossible.
Its stated equivalence is also incomplete because S is unspecified: an ordinary Singer difference
set can give diameter three for a Desarguesian plane. There is no unique correction of the printed
Problem 3. We select the geometric conjecture explicitly stated in its preceding paragraph, not a
silent repair of the literal claim. Its precise reduction is credited to Kantor and Thas–Zagier.

**Formal geometric statement (Kantor and Thas–Zagier Prop. 2.1 / Thm 2.4).** For every integer
n > 8 such that p = n²+n+1 is prime, let
D = {x ∈ F_p^× : x^{n+1} = 1}, the subgroup of order n+1. Then D is **not** a planar difference
set: there is some η ∈ F_p^× with t(η) := #{(x, y) ∈ D² : x − y = η} ≠ 1.

By Kantor's theorem and Thas–Zagier Thm 1.1/2.4, this is equivalent to the Higman–McLaughlin (1961)
conjecture that every finite flag-transitive projective plane is Desarguesian. (Orders 2 and 8 are
the planes that are both Desarguesian and "special".) *Solved* means a proof for all n > 8. The
6-hour deliverable is the finite statement **S(N)**: no n with 8 < n < N gives a special prime.
Together with Thm 1.1, S(N) means there is no non-Desarguesian flag-transitive projective plane of
order less than N.

**Status: open on 2026-10-15.** The SOTA baseline is
[Thas–Zagier, JEMS 10 (2008) 173–190](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.4171/JEMS/107/fulltext.pdf)
(full text opened). Quotes:

- "Continuing the search up to 2 × 10¹¹, now with n restricted to the congruence class 8 (mod 24),
  led to no further solutions (computation time roughly 3 days), verifying the non-existence of
  non-Desarguesian flag-transitive projective planes for n < 2 × 10¹¹, or p < 4 × 10²²."
- The filter is "a prime p = n²+n+1 can only be special if 2 ∈ D_n, i.e., if 2^{n+1} ≡ 1 (mod p)".
- The congruence n ≡ 8 (mod 24) is necessary. Feit proved 8 | n, and n ≡ 2 (mod 3) because
  n³ ≡ n^{n+1} ≡ 1 (mod p).
- An earlier run over all even n < 5×10⁹ found exactly the survivors 2, 8, 24, 90, 512, 134217728 and
  297474474.
- Feit (1990) had n > 14,400,008.

[Xia, arXiv 1707.05486v7 (Jan 2023)](https://arxiv.org/abs/1707.05486) (full text opened) adds
necessary conditions in characteristic 3 but cites only Feit's range and reports no new computation.
No later extension was found by any of these checks:

- the arXiv API (newest 25 "flag-transitive" + "projective plane" records);
- a Semantic Scholar scan of all 25 papers citing Thas–Zagier (newest 2026; none extends the
  range);
- web searches, including two in Chinese;
- the scout.

The openai/math corpus has no hit, locally or in the remote listing.

**Feasibility probes (≤ 5 min each; not an attack).** These use 128-bit Montgomery exponentiation
for the 2-test. Code and logs are in `sources/math-p0039/`: `feasibility-probe-sp.c`
(single-thread), `feasibility-probe-sp2.c` (4 threads), `feasibility-probe-sp3.c` (sieve plus
2-test) and `feasibility-probe-output.txt`.

- *Control:* all even n < 3×10⁸ produced exactly {2, 8, 24, 90, 512, 134217728, 297474474}, which is
  Thas–Zagier's published list restricted to that range. 1.5×10⁸ tests took 11.3 s on 4 threads.
- *Rate without the sieve:* 8.66×10⁶ tests/s on 4 threads at n ≈ 2×10¹¹.
- *Rate with the sieve:* dropping n whose p has a prime factor ≤ 10⁶ leaves 13.7% of n ≡ 8 (mod 24).
  The predicted fraction ∏_{q≡1 (3), q≤10⁶}(1−2/q) = 0.1366 matches. Throughput was 5.3×10⁷ class
  members/s on 4 threads at n ≈ 2×10¹¹.
- *Projection [INFERENCE]:* a 2.5-hour production cap at the probed rate covers about 4.8×10¹¹
  class members, or Δn ≈ 1.1×10¹³. This is not a runtime or result guarantee. Report N only as
  the endpoint of the last gap-free audited block.
- *Resources:* 4 threads, < 100 MB RAM and < 50 MB disk. This fits the institute caps of 4 threads,
  4 GB and 1 GB.

**Attack plan (ordered).**

1. *(30 min) Harden the engine.*
   - Add a segmented sieve on n ≡ 8 (mod 24) that drops n when p has a prime factor q ≤ 10⁶ with
     **q < p** (the roots of x²+x+1 mod q for q ≡ 1 mod 3). This is sound because a special p must be
     prime. The prototype is `feasibility-probe-sp3.c`.
   - Keep the Montgomery 2-test.
   - Write a per-block log: range, class count, number sieved, number tested, survivors and a
     checksum.
2. *(20 min) Controls.*
   - (a) Replicate Thas–Zagier's run over all even n < 5×10⁹ with no sieve and no mod-24
     restriction. It must output exactly the 7 survivors (≈ 3 min).
   - (b) Replicate the mod-24 run up to 2×10¹¹ with the sieve off (≈ 8.3×10⁹ tests, ≈ 16 min). The
     2-test survivors must be exactly 8, 512 and 134217728. Then rerun with the sieve on: it must
     remove 134217728, whose p = 2593·71119·97685839, and keep 8 and 512 (guard q < p).
3. *(≤2.5 h) Main run* on [2×10¹¹, N), starting at 2×10¹¹ inclusive, with checkpoints per block.
4. *(20 min) Survivors.* For each 2-test survivor, check p with BPSW/Miller–Rabin. Then check
   Feit's condition d^{n+1} ≡ 1 (mod p) for every prime d | n (proved elementarily by K. Thas 2003,
   as cited by Thas–Zagier). A survivor that passes everything is reported as an *unresolved
   candidate* with no claim. The O(n) difference-set test is infeasible at n ~ 10¹².
5. *(20 min)* Independent cross-checks and write-up, within the four-hour attack ceiling.

**Deliverable.** S(N), with these targets:

- success threshold N ≥ 2×10¹² (10× the 2008 bound);
- expected N ≈ 10¹³–2×10¹³ by the sieve probe.

It comes with the code, block logs, control outputs and a survivor table with elimination reasons.

**Independent verifier.** A second implementation in Python with arbitrary-precision `pow`, no
Montgomery and no sieve. It re-checks:

1. every survivor, plus a random sample of sieve certificates (q | p);
2. at least 10⁶ uniformly random n from each block of length 10¹²;
3. one contiguous sub-range of at least 10⁸ class members, matching the C logs hash for hash.

Parent-review requirements override the exploratory verification plan above: compare full arbitrary-
precision residues and actual sieve divisors at main-range modulus sizes, not just survivor flags.
Contiguous comparison hashes must cover decisions and residues. Declare every imported theorem,
including Kantor's reliance on the classification of finite simple groups and Feit's divisibility
condition. A probable-prime pass does not eliminate a survivor. Label a production-only extended
range separately from the independently checked subsets; do not call the whole range independently
certified.

**Negative controls.**

1. Mutating the exponent (2ⁿ or 3^{n+1}) or the modulus (n²+n+3) on the control range must change or
   remove the known survivors. This shows the test is not vacuous.
2. The sieve must keep n = 8 and n = 512 (p prime) and remove 134217728.
3. Coverage audit: per-block counts must equal the arithmetic count of n ≡ 8 (mod 24) in the block.

**Kill criteria.**

- A mismatch in control (a) or (b) means no main run.
- If hardened throughput is below 2×10⁶ tests/s on 4 threads, stop at the reached N (it must be at
  least 4×10¹¹) and report the result as weak.
- Any verifier disagreement invalidates the block.
- An unresolved survivor is reported, never claimed.

**Risks.**

1. The scientific value is a finite-range extension, not a theorem; the chance of a counterexample is
   about 0.
2. The run relies on Feit's 8 | n, as Thas–Zagier did. Removing that dependence means covering
   n ≡ 2 (mod 6), which costs 4× per unit of range.
3. Theorem 1.1 rests on Kantor's theorem, which uses CFSG. This is standard.
4. The literal book formulation is inconsistent; see the caveat above.

**Plausibility [INFERENCE].**

- N ≥ 2×10¹²: high.
- Counterexample: about 0.

### c.2 #2 — `math-p0424` (sub-question): prime power conjecture for abelian planar difference sets (非素数幂阶射影平面的存在性, 葛根年; book p. 424, PDF p. 440)

**Verbatim (page image checked):**

> 已经证明：当 n 为素数幂时, PG(2, n) 都存在. 而对所有非素数幂的 n > 1, 尚未发现一个 PG(2, n) 存在的例子. …
> **问题** 对于非素数幂 n, 是否存在 n 阶射影平面？ … **射影平面猜想** 存在 PG(2, n) 当且仅当 n 为素数幂.

**Translation.** "It is proved that PG(2,n) exists whenever n is a prime power, and for no
non-prime-power n > 1 has a PG(2,n) been found. **Problem:** for non-prime-power n, does a
projective plane of order n exist? **Projective-plane conjecture:** a PG(2,n) exists iff n is a
prime power."

**Formal sub-question [ASSUMPTION: we restrict to planes with an abelian point-regular group; the
book does not mention difference sets].** For every integer n ≥ 2 that is not a prime power, no
abelian group of order v = n²+n+1 contains a (v, n+1, 1) difference set. This is the prime power
conjecture (PPC). *Solved* means a proof for all n. The full book question also covers planes with
no regular abelian group, such as the order-12 plane, which is not boundable.

**SOTA.**

- [Gordon, arXiv 2007.07292 (2020)](https://arxiv.org/abs/2007.07292) (abstract opened): "a
  computer search was able to show that the Prime Power Conjecture is true up to order 2·10¹⁰".
- Cyclic case up to 2×10⁹: [Baumert–Gordon](https://arxiv.org/abs/math/0304502) (opened).
- [Peluse, Math. Ann. 380 (2021)](https://arxiv.org/abs/2003.04929) (opened): the number of n ≤ N
  with a perfect difference set in Z/(n²+n+1) is asymptotically N/log N.
- No later computation was found. The openai/math corpus has no hit.

**Angle.**

- Re-implement Gordon's test cascade: Bruck–Ryser–Chowla; Hall's first multiplier theorem;
  Arasu's multiplier argument as generalized by Gordon (2020); the known small-divisor exclusions.
- Run it on (2×10¹⁰, N) with N ≥ 4×10¹⁰ as the target.
- Deliverable: per-n elimination certificates (test name and witness prime/order) and a survivor
  list, expected to be empty.

**Verifier.** An independent second implementation, plus a re-run that reproduces "no survivors"
for n ≤ 10⁸.

**Negative control.** Every prime-power n in the range must pass all tests, because Singer
difference sets exist. Eliminating any prime power proves a test is unsound.

**Kill criteria.**

- More than 10⁻⁶ of n left unresolved by the cheap tests.
- Throughput below 2×10⁶ n/s on 4 threads.
- Gordon's 2020 full text (only the abstract was opened) not obtainable in the first 30 minutes.

**Risks.** The extension is incremental (about 2×) over a 2020 baseline, and Peluse already proves
the asymptotic statement. Per-n factorization of v ≈ n² may dominate the cost. The test details
depend on an unread full text.

**Plausibility [INFERENCE]:** medium-low.

**Resources:** fits the caps.

### c.3 #3 — `math-p0104`: Herzog–Schönheim conjecture / Erdős covering systems (关于不同模覆盖系的厄尔多斯 (Erdös) 问题, 孙智伟; book pp. 104–106, PDF pp. 120–122)

**Verbatim (page images checked):**

> 关于不同模覆盖系的最小模, 目前最好的纪录是可取 n1 = 40 (P. Nielsen, 2008). 关于不同模覆盖的另一个著名难题是下述 Erdös-Selfridge 猜想：模都大于 1 的不同模覆盖系必有偶数模.
>
> 1974 年 Herzog 与 Schönheim 提出下述猜想：如果群 G 的有限个左陪集 a1G1, ···, akGk (k > 1) 构成 G 的不相交覆盖, 则诸指标 n1=[G:G1], ···, nk=[G:Gk] 不可能两两互异.

**Translation.**

- "For the least modulus of a covering system with distinct moduli, the best record is n₁ = 40
  (Nielsen 2008). Another famous problem is the Erdős–Selfridge conjecture: a covering system with
  distinct moduli, all > 1, must have an even modulus."
- "In 1974 Herzog and Schönheim conjectured: if finitely many left cosets a₁G₁, …, a_kG_k (k > 1)
  of a group G partition G, then the indices [G:G₁], …, [G:G_k] cannot be pairwise distinct."

**Formal statement (Herzog–Schönheim).** For every group G and every partition of G into k > 1 left
cosets of finite-index subgroups, two of the indices coincide. Taking the normal core of ∩Gᵢ reduces
this to finite groups [INFERENCE: standard]. *Solved* means a proof for all groups.

**SOTA.**

- [Margolis–Schnabel, arXiv 1803.03569](https://arxiv.org/abs/1803.03569) (opened; Beitr. Algebra
  Geom. 60 (2019)): "holds for any group G of order smaller than 1440".
- [Garonzi–Margolis, arXiv 2509.25118 (2025)](https://arxiv.org/abs/2509.25118) (opened): simple and
  symmetric groups. The scout quotes its introduction as still giving the bound 1440.
- Covering systems:
  - minimum-modulus record 42 (Owens 2014, per [Erdős #2](https://www.erdosproblems.com/2),
    scout-opened);
  - upper bound 616000 ([BBMST](https://arxiv.org/abs/1811.03547), scout-opened);
  - odd covering open; a Lean proof gives lcm > 10000
    ([Mian–Siddique, arXiv 2607.25628](https://arxiv.org/abs/2607.25628), Jul 2026, scout-opened).
- The book's "record 40" is outdated.
- The openai/math corpus has no hit.

**Angles.**

- **(A)** Extend Herzog–Schönheim to all groups of order 1440 ≤ |G| < N, starting with |G| = 1440.
  Re-implement the Margolis–Schnabel reduction: distinct-index multisets with Σ1/nᵢ = 1 and
  nᵢ | |G|, then index realizability and coset-packing feasibility.
  - Needs GAP with SmallGroups, which is **not installed**. The install footprint is likely
    > 1 GB [INFERENCE], so this is a **resource exception** to the 1 GB disk cap.
- **(B)** No dependencies: construct a distinct covering system with minimum modulus ≥ 43, beating
  the 12-year-old record of 42.

**Verifier.**

- (A): an independent SAT/ILP check of the residual coset-packing cases.
- (B): an independent covering checker that sieves over a CRT-structured residue tree.

**Negative controls.**

- (A): the pipeline must find genuine repeated-index coset partitions (for example in S₃ and A₄) and
  must reproduce the Margolis–Schnabel conclusion on sampled orders below 1440.
- (B): the checker must reject the 42-system with one residue class deleted.

**Kill criteria.**

- (A): GAP is not usable within 30 minutes, or the order-1440 candidate multisets exceed 10⁷.
- (B): rebuilding a known 42-construction takes more than 3 h.

**Risks.** Margolis–Schnabel stopping at 1440 suggests the case count blows up there. Angle (B) has
low plausibility.

**Plausibility [INFERENCE].**

- (A): low–medium, if GAP is available.
- (B): low.

## d. Recommendation

**#1 = `math-p0039` Problem 3, a finite-range extension of the non-existence of non-Desarguesian
flag-transitive projective planes past n < 2×10¹¹.**

Ranking by FRONTIER §1 (scientific value × plausibility per 6 h):

- **#1.**
  - *Value.* Modest but genuine: the baseline has not moved in 18 years and concerns a 65-year-old
    named conjecture that the book poses explicitly.
  - *Plausibility.* High. The pipeline already reproduced the published control list in a probe and
    projects to a 10×–100× extension within the caps (sieve probe: 5.3×10⁷ class members/s on 4
    threads).
  - *Checkability.* The result is fully checkable: deterministic logs, a published control and an
    independent re-check.
- **#2.**
  - *Value.* Lower: about a 2× extension of a 2020 baseline, already covered asymptotically by
    Peluse.
  - *Readiness.* The test suite still has to be rebuilt from a full text that was not opened.
- **#3.**
  - *Value.* Higher in principle.
  - *Plausibility.* Depends on a GAP install that breaks the disk cap (A), or is low (B).

None of the three is expected to settle a conjecture. The volume's recognized hard problems are
either flagships with no bounded plan, claimed by the openai/math corpus (Foulkes a = 6, Hilbert's
16th, off-diagonal Ramsey, circulant Hadamard, Hadwiger, Koebe, Brennan, Rokhlin, Turing-degree
rigidity, finitistic dimension, Auslander–Reiten), or multi-day searches: self-avoiding-walk
μ-bounds, Foulkes (7,11), K₁₆ list colouring, Hajós n = 13, Hadamard order 668 and Erdős–Szekeres
f(7).

**Decisions for the parent.**

1. Accept the formalization of Problem 3, since the book's literal "diameter 2" is impossible.
2. Accept Feit's 8 | n, as Thas–Zagier did, or spend 4× on n ≡ 2 (mod 6).
3. Frame success as "S(N), N ≥ 2×10¹²", not as a theorem.
4. #3 angle A needs a GAP install that exceeds the 1 GB disk cap. Allow it or drop angle A.
