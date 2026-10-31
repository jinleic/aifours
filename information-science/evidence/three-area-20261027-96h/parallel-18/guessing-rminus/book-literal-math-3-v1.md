# B3 — literal book-entry transcription, math-3

## Source boundary and clocks

Transcriber: **InfoGuessingRminus-2**, slot info-5. Duty **B3**. This packet is source-only transcription from the TWO permitted images; no interpretation section is supplied.

- Frozen duty manifest SHA256: `3ad778a518dad5bfa5aacb87abd3f776eca5bd430af8823eddc012d803edcc17`.
- Frozen gate SHA256: `16441f4ed6394d93360d764ac553d99983eb989fb0253075f2fe69fe2ce84d0b`.
- Extraction receipt SHA256: `19156746c835ef8d8ad6e8b29490376fc69aea32c4b7a5f2ba94b733d071a392`.
- Pre-image ACK: `book-literal-math-3-prebody-ack-v1.json`, SHA256 `d11c631233b1654758d990754221fa693d1b287e93a923981e85174b161812ac`, **15 LF / 2799 bytes**.
- Native clock immediately before the ACK was written: **Wed Oct 28 09:19:57 PDT 2026**. S0, manifest and the listed administrative controls were read before that ACK; both image views were after it.
- Native clock observed after both image displays and before this transcription was written: **Wed Oct 28 09:22:58 PDT 2026**. Exact individual display instants were not separately clocked.
- Image 1: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/source-math-0242.png`, PDF page **242**, printed page **226**, SHA256 `6d3d0c803598270ec6bb4b8b493ce02f578d1f47d54f0b34443cd745aec466a6`, **301532 bytes**.
- Image 2: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/source-math-0243.png`, PDF page **243**, printed page **227**, SHA256 `c5f6b31ad405729db755b8e2ec37bf98794fc410d9d91490f2487295a376f718`, **102138 bytes**.

Each image was displayed as a single-column page in a 1109×1568 viewer frame; the original image is 1241×1754. Approximate coordinate ranges below refer to the DISPLAYED frame, with origin at its upper-left corner. They are visual locators, not measurements. Body-line labels B01 etc. are transcription locators, counted from the first Chinese body line on each page; the book does not print these line numbers. Reference lines and credit lines are labelled separately. Mathematical typography is represented in LaTeX-style text; printed wording, indices and equation numbers are retained.

**TRUNCATED: NO.** The entry continues from printed page 226 onto the permitted page 227 and ends there with references and the contributor/affiliation lines. The rest of the displayed page 227 is blank. No additional page was opened.

## 1. Verbatim Chinese and other printed text

### Printed page 226 — PDF page 242

**[M226; running header; x≈150–803, y≈133–150]**

·226·　10000个科学难题　数学卷

**[Z01; entry title, title lines 1–2; x≈173–780, y≈257–328]**

非可对称化的卡茨—穆迪 (Kac-Moody) 代数的  
定义关系问题

**[Z01E; printed English title, lines 1–2; x≈221–733, y≈356–412]**

Problem on Defining Relations of Non-symmetrizable  
Kac-Moody Algebras

**[Z02; body B01–B03; x≈134–820, y≈463–543]**

设 $A=(a_{ij})_{i,j=1}^{n}$ 是具有秩为 $\ell$ 的 $n\times n$ 复矩阵. 称 $A$ 为广义 Cartan 矩阵 (GCM), 如果 $A$ 满足以下三个条件: (i) $a_{ii}=2$, $i=1,\cdots,n$; (ii) 当 $i\ne j$ 时, $a_{ij}$ 是非正整数; (iii) 若 $a_{ij}=0$, 则 $a_{ji}=0$.

**[Z03; body B04–B06; x≈134–820, y≈550–629]**

设 $A$ 是一个 GCM. 令 $C=(c_{ij})$ 为任一个秩为 $n$ 的 $(2n-\ell)\times n$ 复矩阵, 其前 $n$ 行为矩阵 $A$. 定义一个李代数 $\tilde{\mathfrak g}(A)$ 如下: 它具有生成元 $e_i,f_i\ (i=1,\cdots,n)$, $h_p\ (p=1,\cdots,2n-\ell)$ 和定义关系:

**[Z04; displayed formula, body B07; x≈208–819, y≈654–677]**

$$
[e_i,f_j]=\delta_{ij}h_i,\quad [h_p,h_q]=0,\quad [h_p,e_i]=c_{pi}e_i,\quad [h_p,f_i]=-c_{pi}f_i,\qquad (1)
$$

**[Z05; body B08–B11; x≈134–820, y≈703–813]**

其中 $\delta_{ij}$ 为 Kronecker 记号 (即当 $i=j$ 时, $\delta_{ij}=1$, 否则为 $0$), $i,j=1,\cdots,n$; $p,q=1,\cdots,2n-\ell$. 令 $\mathfrak h$ 为由 $h_p\ (p=1,\cdots,2n-\ell)$ 张成的空间, 并令 $\mathfrak r$ 为与 $\mathfrak h$ 具有平凡交的 $\tilde{\mathfrak g}(A)$ 的极大理想, 则 $\mathfrak g(A)=\tilde{\mathfrak g}(A)/\mathfrak r$ 就是著名的 Kac-Moody 代数. 李代数的生成元与定义关系是李代数结构理论的第一个基本问题. 文献 [1] 证明了:

**[Z06; Theorem 1, body B12–B13; x≈134–820, y≈819–872]**

**定理 1**　当 $A$ 可对称化 (即存在 $n\times n$ 可逆对角矩阵 $D$, 使 $DA$ 为对称矩阵) 时, $\mathfrak r$ 由 $(\operatorname{ad}e_i)^{1-a_{ij}}e_j$, $(\operatorname{ad}f_i)^{1-a_{ij}}f_j\ (1\le i\ne j\le n)$ 生成.

**[Z07; body B14; x≈173–452, y≈879–901]**

定理 1 说明关系 (1) 和下述关系

**[Z08; displayed formula, body B15; x≈250–820, y≈923–949]**

$$
(\operatorname{ad}e_i)^{1-a_{ij}}e_j=0,\quad (\operatorname{ad}f_i)^{1-a_{ij}}f_j=0,\quad 1\le i\ne j\le n\qquad (2)
$$

**[Z09; body B16–B17; x≈134–820, y≈973–1023]**

是可对称化 Kac-Moody 代数 $\mathfrak g(A)$ 的定义关系. 关系 (1) 和 (2) 称为 Serre 关系. 一个自然的猜想是

**[Z10; Conjecture 1, body B18–B19; x≈134–820, y≈1032–1083]**

**猜想 1**　对任意广义 Cartan 矩阵 $A$, Serre 关系是 Kac-Moody 代数 $\mathfrak g(A)$ 的定义关系.

**[Z11; body B20–B23; x≈134–820, y≈1090–1203; paragraph continues onto printed page 227]**

与猜想密切相关的猜想是: “任意 Kac-Moody 代数的可积最高权表示不可约”, 或等价地, “Kac-Moody 代数的范畴 $\mathcal O$ 的可积表示完全可约”. 因此, 具有 40 年历史的猜想 1 是 Kac-Moody 代数的结构和表示理论中未解决的重要问题. 当 $A$ 是可对称化 GCM 时, 这一猜想已经解决, 即前面的定理 1, 主要工具是用到了 Kac-Moody

### Printed page 227 — PDF page 243

**[M227; running header; x≈153–804, y≈132–151]**

非可对称化的卡茨—穆迪 (Kac-Moody) 代数的定义关系问题　·227·

**[Z12; body B01–B02; x≈134–820, y≈158–211; continuation of Z11]**

代数 $\mathfrak g(A)$ 具有的非退化对称不变双线性型 $(\cdot,\cdot)$. 但当 $A$ 不可对称化时, 由于 $\mathfrak g(A)$ 不存在这样的双线性型, 这一问题至今还没有什么进展.

**[Z13; reference heading; x≈423–533, y≈271–295]**

参考文献

**[Z14; reference [1], reference lines R01–R02; x≈134–820, y≈317–365]**

[1]　Humphreys J E. Introduction to Lie Algebras and Representations. Berlin-Heidelberg-  
　　New York: Springer-Verlag, 1972

**[Z15; reference [2], reference lines R03–R04; x≈134–820, y≈370–418]**

[2]　Kac V G. Infinite Dimensional Lie Algebras. 3rd Ed. Cambridge: Cambridge University  
　　Press, 1990

**[Z16; reference [3], reference line R05; x≈134–739, y≈424–446]**

[3]　苏育才, 卢才辉, 崔一敏. 有限维半单李代数简明教程. 北京: 科学出版社, 2008

**[Z17; contributor line C01; x≈666–820, y≈475–501]**

撰稿人: 苏育才

**[Z18; affiliation line C02; x≈666–820, y≈505–528]**

中国科学技术大学

## 2. Sentence-aligned literal English rendering

The tags below align to the quoted source above; a paragraph containing several sentences is divided into suffixes a, b, etc. An interrupted sentence retains its cross-formula or cross-page alignment.

**[M226]** ·226·　10000 Scientific Problems　Mathematics Volume

**[Z01]** Problem on the defining relations of non-symmetrizable Kac-Moody algebras.

**[Z01E — English already printed]** Problem on Defining Relations of Non-symmetrizable Kac-Moody Algebras

**[Z02a]** Let $A=(a_{ij})_{i,j=1}^{n}$ be an $n\times n$ complex matrix of rank $\ell$.

**[Z02b]** A is called a generalized Cartan matrix (GCM) if A satisfies the following three conditions: (i) $a_{ii}=2$, $i=1,\cdots,n$; (ii) when $i\ne j$, $a_{ij}$ is a nonpositive integer; (iii) if $a_{ij}=0$, then $a_{ji}=0$.

**[Z03a]** Let A be a GCM.

**[Z03b]** Let $C=(c_{ij})$ be any $(2n-\ell)\times n$ complex matrix of rank n whose first n rows are the matrix A.

**[Z03c]** Define a Lie algebra $\tilde{\mathfrak g}(A)$ as follows: it has generators $e_i,f_i\ (i=1,\cdots,n)$, $h_p\ (p=1,\cdots,2n-\ell)$ and defining relations:

**[Z04 — formula (1)]**

$$
[e_i,f_j]=\delta_{ij}h_i,\quad [h_p,h_q]=0,\quad [h_p,e_i]=c_{pi}e_i,\quad [h_p,f_i]=-c_{pi}f_i,\qquad (1)
$$

**[Z05a]** Here $\delta_{ij}$ is the Kronecker symbol (that is, when $i=j$, $\delta_{ij}=1$, and otherwise it is 0), $i,j=1,\cdots,n$; $p,q=1,\cdots,2n-\ell$.

**[Z05b]** Let $\mathfrak h$ be the space spanned by $h_p\ (p=1,\cdots,2n-\ell)$, and let $\mathfrak r$ be the maximal ideal of $\tilde{\mathfrak g}(A)$ having trivial intersection with $\mathfrak h$; then $\mathfrak g(A)=\tilde{\mathfrak g}(A)/\mathfrak r$ is the well-known Kac-Moody algebra.

**[Z05c]** The generators and defining relations of a Lie algebra are the first basic problem of the structural theory of Lie algebras.

**[Z05d]** Reference [1] proved:

**[Z06]** **Theorem 1.** When A is symmetrizable (that is, there exists an $n\times n$ invertible diagonal matrix D such that DA is a symmetric matrix), $\mathfrak r$ is generated by $(\operatorname{ad}e_i)^{1-a_{ij}}e_j$, $(\operatorname{ad}f_i)^{1-a_{ij}}f_j\ (1\le i\ne j\le n)$.

**[Z07 + Z08 + Z09a — one sentence interrupted by the displayed formula]** Theorem 1 explains that relations (1) and the following relations

$$
(\operatorname{ad}e_i)^{1-a_{ij}}e_j=0,\quad (\operatorname{ad}f_i)^{1-a_{ij}}f_j=0,\quad 1\le i\ne j\le n\qquad (2)
$$

are the defining relations of the symmetrizable Kac-Moody algebra $\mathfrak g(A)$.

**[Z09b]** Relations (1) and (2) are called the Serre relations.

**[Z09c]** A natural conjecture is

**[Z10]** **Conjecture 1.** For any generalized Cartan matrix A, the Serre relations are the defining relations of the Kac-Moody algebra $\mathfrak g(A)$.

**[Z11a]** A conjecture closely related to the conjecture is: “An integrable highest-weight representation of any Kac-Moody algebra is irreducible”, or equivalently, “The integrable representations of category $\mathcal O$ of a Kac-Moody algebra are completely reducible”.

**[Z11b]** Therefore, Conjecture 1, which has a history of 40 years, is an important unresolved problem in the structure and representation theory of Kac-Moody algebras.

**[Z11c + Z12a — one sentence crossing the page boundary]** When A is a symmetrizable GCM, this conjecture has already been solved, namely Theorem 1 above; the main tool used was the nondegenerate symmetric invariant bilinear form $(\cdot,\cdot)$ possessed by the Kac-Moody algebra $\mathfrak g(A)$.

**[M227]** Problem on the defining relations of non-symmetrizable Kac-Moody algebras　·227·

**[Z12b]** But when A is not symmetrizable, because $\mathfrak g(A)$ does not have such a bilinear form, there has still not been much progress on this problem to this day.

**[Z13]** References

**[Z14 — already printed in English]** [1] Humphreys J E. Introduction to Lie Algebras and Representations. Berlin-Heidelberg-New York: Springer-Verlag, 1972

**[Z15 — already printed in English]** [2] Kac V G. Infinite Dimensional Lie Algebras. 3rd Ed. Cambridge: Cambridge University Press, 1990

**[Z16]** [3] Su Yucai, Lu Caihui, Cui Yimin. A Concise Course on Finite-Dimensional Semisimple Lie Algebras. Beijing: Science Press, 2008

**[Z17]** Contributor: Su Yucai

**[Z18]** University of Science and Technology of China

## 3. Inventory of printed definitions, symbols, parameters, quantifiers and stated questions

Every quotation in this inventory is from the tagged transcription above; locations are the corresponding page/line coordinates. “No separate definition printed” records only the absence of a definition in the two displayed pages, without supplying one.

| Item | Exact printed text / formula | Printed location |
|---|---|---|
| Entry question/title | “非可对称化的卡茨—穆迪 (Kac-Moody) 代数的定义关系问题” | Z01; p226 title |
| Printed English title | “Problem on Defining Relations of Non-symmetrizable Kac-Moody Algebras” | Z01E; p226 |
| Matrix A, entries and index notation | “$A=(a_{ij})_{i,j=1}^{n}$” | Z02; p226 B01 |
| Rank and dimensions of A; scalars | “具有秩为 $\ell$ 的 $n\times n$ 复矩阵” | Z02; p226 B01 |
| Generalized Cartan matrix; abbreviation | “称 $A$ 为广义 Cartan 矩阵 (GCM), 如果 $A$ 满足以下三个条件” | Z02; p226 B01–B03 |
| Condition (i), value and index range | “(i) $a_{ii}=2$, $i=1,\cdots,n$” | Z02; p226 B02 |
| Condition (ii), off-diagonal condition | “(ii) 当 $i\ne j$ 时, $a_{ij}$ 是非正整数” | Z02; p226 B02–B03 |
| Condition (iii), implication | “(iii) 若 $a_{ij}=0$, 则 $a_{ji}=0$” | Z02; p226 B03 |
| Hypothesis on A in the construction | “设 $A$ 是一个 GCM” | Z03; p226 B04 |
| C, its entries, arbitrary choice, rank and dimensions | “令 $C=(c_{ij})$ 为任一个秩为 $n$ 的 $(2n-\ell)\times n$ 复矩阵” | Z03; p226 B04 |
| First rows of C | “其前 $n$ 行为矩阵 $A$” | Z03; p226 B04–B05 |
| Defined Lie algebra | “定义一个李代数 $\tilde{\mathfrak g}(A)$ 如下” | Z03; p226 B05 |
| Generators e and f and their ranges | “生成元 $e_i,f_i\ (i=1,\cdots,n)$” | Z03; p226 B05 |
| Generators h and their range | “$h_p\ (p=1,\cdots,2n-\ell)$” | Z03; p226 B05–B06 |
| Relation (1), first bracket | “$[e_i,f_j]=\delta_{ij}h_i$” | Z04; p226 B07 |
| Relation (1), second bracket | “$[h_p,h_q]=0$” | Z04; p226 B07 |
| Relation (1), third bracket and coefficient | “$[h_p,e_i]=c_{pi}e_i$” | Z04; p226 B07 |
| Relation (1), fourth bracket and minus sign | “$[h_p,f_i]=-c_{pi}f_i$” | Z04; p226 B07 |
| Kronecker symbol; two cases | “$\delta_{ij}$ 为 Kronecker 记号 (即当 $i=j$ 时, $\delta_{ij}=1$, 否则为 $0$)” | Z05; p226 B08 |
| Relation index ranges | “$i,j=1,\cdots,n$; $p,q=1,\cdots,2n-\ell$” | Z05; p226 B08–B09 |
| Space h and its spanning elements | “令 $\mathfrak h$ 为由 $h_p\ (p=1,\cdots,2n-\ell)$ 张成的空间” | Z05; p226 B09 |
| Ideal r, trivial intersection and maximality wording | “并令 $\mathfrak r$ 为与 $\mathfrak h$ 具有平凡交的 $\tilde{\mathfrak g}(A)$ 的极大理想” | Z05; p226 B09–B10 |
| Quotient and Kac-Moody algebra | “$\mathfrak g(A)=\tilde{\mathfrak g}(A)/\mathfrak r$ 就是著名的 Kac-Moody 代数” | Z05; p226 B10 |
| Stated basic problem | “李代数的生成元与定义关系是李代数结构理论的第一个基本问题” | Z05; p226 B10–B11 |
| Printed theorem attribution | “文献 [1] 证明了” | Z05; p226 B11 |
| Symmetrizability, D, dimensions and invertibility | “当 $A$ 可对称化 (即存在 $n\times n$ 可逆对角矩阵 $D$, 使 $DA$ 为对称矩阵)” | Z06; p226 B12 |
| Theorem 1 ideal generators and exponent | “$\mathfrak r$ 由 $(\operatorname{ad}e_i)^{1-a_{ij}}e_j$, $(\operatorname{ad}f_i)^{1-a_{ij}}f_j\ (1\le i\ne j\le n)$ 生成” | Z06; p226 B13 |
| Notation ad | “$\operatorname{ad}e_i$”, “$\operatorname{ad}f_i$”; no separate definition printed | Z06, Z08; p226 B13, B15 |
| Relation (2), e expression | “$(\operatorname{ad}e_i)^{1-a_{ij}}e_j=0$” | Z08; p226 B15 |
| Relation (2), f expression | “$(\operatorname{ad}f_i)^{1-a_{ij}}f_j=0$” | Z08; p226 B15 |
| Relation (2), complete printed index condition | “$1\le i\ne j\le n$” | Z08; p226 B15 |
| Symmetrizable defining-relations statement | “定理 1 说明关系 (1) 和下述关系” … “是可对称化 Kac-Moody 代数 $\mathfrak g(A)$ 的定义关系” | Z07–Z09; p226 B14–B16 |
| Name Serre relations | “关系 (1) 和 (2) 称为 Serre 关系” | Z09; p226 B16 |
| Introduction of conjecture | “一个自然的猜想是” | Z09; p226 B16–B17 |
| Conjecture 1, complete quantifier and claim | “对任意广义 Cartan 矩阵 $A$, Serre 关系是 Kac-Moody 代数 $\mathfrak g(A)$ 的定义关系” | Z10; p226 B18–B19 |
| Related conjecture; quantifier and highest-weight representations | “任意 Kac-Moody 代数的可积最高权表示不可约” | Z11; p226 B20 |
| Printed equivalence wording | “或等价地” | Z11; p226 B21 |
| Category symbol and second related conjecture | “Kac-Moody 代数的范畴 $\mathcal O$ 的可积表示完全可约”; no separate definition of $\mathcal O$ or “可积” printed | Z11; p226 B21 |
| Printed time parameter | “具有 40 年历史的猜想 1” | Z11; p226 B21–B22 |
| Printed symmetrizable hypothesis | “当 $A$ 是可对称化 GCM 时” | Z11; p226 B22–B23 |
| Bilinear-form symbol and printed adjectives | “非退化对称不变双线性型 $(\cdot,\cdot)$” | Z12; p227 B01 |
| Printed nonsymmetrizable condition and sentence | “但当 $A$ 不可对称化时, 由于 $\mathfrak g(A)$ 不存在这样的双线性型, 这一问题至今还没有什么进展” | Z12; p227 B01–B02 |
| Printed references | Complete [1], [2], [3] strings as transcribed at Z14–Z16 | p227 R01–R05 |
| Contributor and affiliation | “撰稿人: 苏育才”; “中国科学技术大学” | Z17–Z18; p227 C01–C02 |

## 4. Illegible or uncertain glyphs and ambiguity record

No illegible or uncertain content glyph requiring a substitute or unresolved reading was identified in the two permitted displayed images. The printed blackletter Lie-algebra/space/ideal letters are encoded as $\mathfrak g$, $\mathfrak h$, $\mathfrak r$; the printed rank letter is encoded as $\ell$, and the category letter as $\mathcal O$. This records typographic encoding only. The inventory leaves notation without a separately printed definition undefined; no missing definition has been supplied.

No source sentence has been resolved by interpretation or comparison with another source. No additional AMBIGUOUS sentence is asserted by this transcription.

## 5. Completion and scope statement

**TRUNCATED: NO.** The two listed pages contain the entry's visible title, printed English title, body, both numbered displayed relations, Theorem 1, Conjecture 1 and related quoted conjectures, all three references, contributor and affiliation. The source paragraph crossing the page boundary is tagged at Z11/Z12 and sentence-aligned above. No neighbouring page, bibliography target, web source, proof body, held material or review payload was opened.

**Nothing beyond transcription was done:** visual copying, literal translation, printed-definition/symbol/parameter/quantifier/question inventory and documentary coordinates only. No interpretation, reformulation, proof, solution idea, selected example, scientific computation, source-status/priority/novelty assessment or contact with MathKacMoody-2 or another owner. No STOP is lifted, no mathematical verdict is issued, and this source packet is not admitted for lane research until Main freezes a later separate release.

**END OF B3 LITERAL SOURCE PACKET.**
