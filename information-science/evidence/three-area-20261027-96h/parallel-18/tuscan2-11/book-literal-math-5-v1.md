# B5 — Book-literal packet for mathematics, printed pages 64–65

## Scope, images and actual clocks

- Transcriber: **InfoRecursiveMDS18-2**, info-4. Duty **B5**; target lane **math-5**. No contact with MathShor-2 or any other lane owner.
- Duty release SHA256: `e972806ac3657f7118d4ccfc9e92a1dc049b7ebed86a1b4f0641ec3f7b6cb84e`.
- Frozen gate SHA256: `16441f4ed6394d93360d764ac553d99983eb989fb0253075f2fe69fe2ce84d0b`.
- Extraction receipt SHA256: `19156746c835ef8d8ad6e8b29490376fc69aea32c4b7a5f2ba94b733d071a392`.
- ONLY viewed images:
  - PDF page80 / printed64: `source-math-0080.png`, SHA256 `e2c67ba6010edeefb71e104b056d203f64060ba5fd059da273c918091ab5ed8f`,290613 bytes.
  - PDF page81 / printed65: `source-math-0081.png`, SHA256 `0bad7cfb52328592848919db2173184c5147339ca553600cb22362af688b61fc`,237291 bytes.
- Full image paths are in `institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/`. Both originals are1241×1754 pixels; the tool displayed1109×1568 previews.
- Native pre-image ACK clock: **Wed Oct 28 09:21:01 PDT 2026**. The ACK was written before either image was opened. Input hashes/bytes were verified as metadata at that observation.
- Native observation AFTER the image views and immediately before this packet write: **Wed Oct 28 09:27:07 PDT 2026**. Individual view instants were not separately clocked; they lie between those observations.
- Coordinates below use the DISPLAYED1109×1568 preview, origin at upper left, with approximate y-ranges. Both pages have one text column. Paragraph/formula IDs are editorial locators, not printed numbering.
- `⟦U1⟧`, `⟦U3⟧`, `⟦U4⟧` and the U2 notice are explicit transcription uncertainties, NOT printed text. No uncertain glyph has been silently repaired from another source. Printed reference markers are rendered as `[1]` etc.; displayed formulas use LaTeX-style text.

## Verbatim transcription

### Printed page 64 / PDF page 80

**[C64-H; header, y134–153]**

·64·　10000个科学难题　数学卷

**[C64-T; title, y256–285]**

关于有限码具有有限完备化的判定问题

**[C64-ET; printed English title, y305–356]**

The Decision Problem for A Finite Code Having

A Finite Completion

**[C64-P1; first body paragraph, y411–571]**

在 M.P.Schutzenberger 于1955开创的“变长度码理论”中[1]，除了“码交换等价于前缀码”的猜测及其局限于“有限极大”情形的猜测外（见文献[2]，[3]，也可参看我们⟦U1⟧于这里的一个有关的专门介绍），另一个主要的公开问题就是“有限码具有有限完备化的判定问题”. 这一问题的背景是，许多有关“编码过程优化”的问题都涉及码的一些极端性质，诸如“极大性”，“完备性”等；另外，这一问题与“有限极大码交换等价于有限极大前缀码”的猜测[3]也有密切的联系.

**[C64-P2; body, y584–659; C64-F1, y683–733]**

令 \(X\) 是一有限集，\(X^*\) 是由 \(X\) 生成的自由幺半群. 称 \(X^*\) 的元（子集）为 \(X\) 上的（半群）字（语言）；称自由幺半群 \(X^*\) 的幺元1为 \(X\) 上的空字；称 \(X\) 上一非空语言 \(C\) 为 \(X\) 上一（代数）码，如果

\[
\forall x_1,x_2,\cdots,x_m,y_1,y_2,\cdots,y_n\in C,
\]
\[
x_1x_2\cdots x_m=y_1y_2\cdots y_n\to m=n,\quad x_i=y_i,\quad i=1,2,\cdots,m;
\]

**[C64-P3; body, y749–772; C64-F2, y790–812]**

称 \(X\) 上一含于 \(X^+=X^*\backslash\{1\}\) 的非空语言 \(P\) 为 \(X\) 上一前缀码，如果

\[
\forall x,y\in P,\quad\forall z\in X^*,\quad y=xz\to z=1.
\]

**[C64-P4; body, y831–903; C64-F3, y913–934]**

后缀码是前缀码的对偶概念，显然，前、后缀码都是特殊的码. 关于 \(X\) 上任一字 \(x\) 和 \(X\) 的任一元素 \(a\)，用 \(x/a\) 表示 \(a\) 在 \(x\) 中出现的次数. 称 \(X\) 上两个字 \(x,y\) 是交换等价的，记为 \(x\approx y\)，如果

\[
\forall a\in X,\quad x/a=y/a.
\]

**[C64-P5; body, y948–971; C64-F4, y984–1006]**

称 \(X\) 上两个语言 \(A,B\) 是交换等价的，记为 \(A\approx B\)，如果存在双射 \(\sigma:A\to B\) 使得

\[
\forall x\in A,\quad x\approx\sigma(x).
\]

**[C64-P6; body, y1027–1051; C64-F5, y1071–1092]**

称 \(X\) 上一码 \(C\) 是完备的，如果

\[
\forall w\in X^*,\quad X^*wX^*\cap C^*\ne\Phi.
\]

The final printed glyph in C64-F5 is provisionally copied as \(\Phi\); see **U2**.

**[C64-P7; body, y1110–1163; C64-F6, y1180–1206]**

称 \(X\) 上一有限码 \(C\) 具有有限完备化，如果它能被嵌入一有限完备码. 称 \(X^*\) 上一语言 \(L\) 是正则的，如果 \(X^*\) 上下述等价关系 \(\sim_L\) 的指数有限：关于任意 \(x,y\in X^*\)，

\[
x\sim_L y\quad\Leftrightarrow\quad\forall u,v\in X^*,\quad uxv\in L\leftrightarrow uyv\in L.
\]

### Printed page 65 / PDF page 81

**[C65-H; running header, y134–153]**

关于有限码具有有限完备化的判定问题　·65·

**[C65-P1; continuation body, y194–214]**

显然，有限码是正则码.

**[C65-P2; body, y224–243]**

下面的事实指出，在一定条件下，码的极大性和完备性是一致的.

**[C65-FACT; y251–273]**

**事实** \(^{[1]}\)　正则码（特别地，有限码）是完备的当且仅当它是极大的.

**[C65-EX; example label and list, y280–390]**

**例** \(^{[3,4]}\)

(1) 任何有限前缀（后缀）码都具有有限前缀（后缀）完备化；

(2) \(\{a,b\}\) 上的有限码 \(\{aa,ba\}\) 具有有限完备化；

(3) \(\{a,b\}\) 上的有限码 \(\{aaaaa,aab,ba,b\}\) 不具有有限完备化.

**[C65-P3; body, y398–439; C65-F1, y469–495]**

推翻“码交换等价于前缀码”猜测的那个非极大有限码的反例是 \(\{a,b\}\) 上的有限码\(^{[3,5]}\)

\[
C=b\{1,a,a^7,a^{13},a^{14}\}\cup\{a^3,a^8\}b\{1,a^2,a^4,a^6\}\cup a^{11}b\{1,a,a^2\}.
\]

**[C65-Q1; first question, y519–542]**

**问题1**\(^{[3]}\)　上面的有限码 \(C\) 具有有限完备化（据事实1，即有限极大化）吗？

**[C65-P4; body after Question 1, y549–623]**

这一问题与“有限极大码交换等价于有限极大前缀码”的猜测联系在于，如果问题1的回答是正面的，那么“有限极大码交换等价于有限极大前缀码”的猜测就是错的.

**[C65-Q2; second question, y637–661]**

**问题2**\(^{[3]}\)　有限码具有有限完备化是可判定的吗？

**[C65-RH; reference heading, y689–711]**

参　考　文　献

**[C65-R1; y734–780; Latin accents uncertain, U3]**

[1] Schutzenberger M P. Une theorie algebrique du codage, Seminaire Dubreil-Pisot 1955-
56. expose No. 15 (1955)

**[C65-R2; y787–832; Latin accents uncertain, U3; one letter uncertain, U4]**

[2] Perrin D, Schutzenberger M P. Un probleme elementaire de la theorie de l'information.
Colloques intern⟦U4⟧t. CNRS 276, Cachan 1977, 249-260

**[C65-R3; y840–884]**

[3] Bruyere V, Latteux M. Variable-Length Maximal Codes. Automata, Languages and
Programming (paderborn, 1996). Berlin: Springer-Verlag, 1996, 24-47

**[C65-R4; y893–915]**

[4] Restivo A. On codes having no finite completions. Discrete Math, 1977, 17: 309-316

**[C65-R5; y920–965]**

[5] Shor P. A counterexample to the triangle conjecture. J Combin Theor Ser A, 1983, 38:
110-112

**[C65-A; contributor line, y993–1017]**

撰稿人：郭聿琦　刘　云

**[C65-AFF; affiliation, y1025–1046]**

西南大学

## Sentence-aligned literal English rendering

The identifiers refer to the Chinese paragraph/formula units above. Sentences within a paragraph are rendered in their printed order. Bibliographic strings C65-R1–R5 are retained above as printed-language strings, not corrected or replaced by other citations.

**[E64-T ↔ C64-T]** The decision problem for a finite code having a finite completion.

**[E64-ET ↔ C64-ET]** The printed English title is: “The Decision Problem for A Finite Code Having / A Finite Completion”.

**[E64-P1.s1 ↔ C64-P1, sentence 1]** In the “variable-length code theory” initiated by M.P.Schutzenberger in1955[1], besides the conjecture that “codes are exchange-equivalent to prefix codes” and the conjecture restricted to the “finite maximal” case (see references[2],[3]; one may also consult our ⟦U1: unclear printed glyph⟧ here, a related special introduction), another main open question is “the decision problem for a finite code having a finite completion”.

**[E64-P1.s2 ↔ C64-P1, sentence 2]** The background of this question is that many questions concerning “optimization of the coding process” involve some extremal properties of codes, such as “maximality”, “completeness”, and so on; in addition, this question also has a close connection with the conjecture[3] that “finite maximal codes are exchange-equivalent to finite maximal prefix codes”.

**[E64-P2.s1 ↔ C64-P2, sentence 1]** Let X be a finite set, and X* the free monoid generated by X.

**[E64-P2.s2 ↔ C64-P2, remaining semicolon-linked sentence and C64-F1]** The elements (subsets) of X* are called (semigroup) words (languages) over X; the identity1 of the free monoid X* is called the empty word over X; a nonempty language C over X is called an (algebraic) code over X if, for all x1,…,xm,y1,…,yn in C, equality of the two printed concatenations implies m=n and xi=yi for i=1,2,…,m.

**[E64-P3 ↔ C64-P3/C64-F2]** A nonempty language P over X contained in X+=X*\{1} is called a prefix code over X if, for all x,y in P and all z in X*, y=xz implies z=1.

**[E64-P4.s1 ↔ C64-P4, sentence 1]** Suffix code is the dual concept of prefix code; evidently, prefix and suffix codes are both special codes.

**[E64-P4.s2 ↔ C64-P4, sentence 2]** For an arbitrary word x over X and an arbitrary element a of X, x/a denotes the number of occurrences of a in x.

**[E64-P4.s3 ↔ C64-P4/C64-F3]** Two words x,y over X are called exchange-equivalent, denoted x≈y, if for all a in X, x/a=y/a.

**[E64-P5 ↔ C64-P5/C64-F4]** Two languages A,B over X are called exchange-equivalent, denoted A≈B, if there exists a bijection σ:A→B such that, for all x in A, x≈σ(x).

**[E64-P6 ↔ C64-P6/C64-F5]** A code C over X is called complete if, for all w in X*, X*wX*∩C*≠Φ. The final printed glyph is retained provisionally as Φ; U2 is unresolved.

**[E64-P7.s1 ↔ C64-P7, sentence 1]** A finite code C over X is said to have a finite completion if it can be embedded in a finite complete code.

**[E64-P7.s2 ↔ C64-P7/C64-F6]** A language L over X* is called regular if the following equivalence relation ~L on X* has finite index: for arbitrary x,y in X*, x~L y if and only if, for all u,v in X*, uxv∈L if and only if uyv∈L.

**[E65-P1 ↔ C65-P1]** Evidently, finite codes are regular codes.

**[E65-P2 ↔ C65-P2]** The following fact points out that, under certain conditions, maximality and completeness of a code coincide.

**[E65-FACT ↔ C65-FACT]** Fact[1]. A regular code (in particular, a finite code) is complete if and only if it is maximal.

**[E65-EX.label ↔ C65-EX]** Examples[3,4].

**[E65-EX.1 ↔ C65-EX(1)]** Every finite prefix (suffix) code has a finite prefix (suffix) completion;

**[E65-EX.2 ↔ C65-EX(2)]** The finite code {aa,ba} over {a,b} has a finite completion;

**[E65-EX.3 ↔ C65-EX(3)]** The finite code {aaaaa,aab,ba,b} over {a,b} does not have a finite completion.

**[E65-P3 ↔ C65-P3/C65-F1]** The counterexample of a nonmaximal finite code that overturns the conjecture “codes are exchange-equivalent to prefix codes” is the finite code[3,5] over {a,b} displayed as C in C65-F1.

**[E65-Q1 ↔ C65-Q1]** Question1[3]. Does the above finite code C have a finite completion (according to Fact1, that is, a finite maximalization)?

**[E65-P4 ↔ C65-P4]** The connection of this question with the conjecture “finite maximal codes are exchange-equivalent to finite maximal prefix codes” is that, if the answer to Question1 is positive, then the conjecture “finite maximal codes are exchange-equivalent to finite maximal prefix codes” is wrong.

**[E65-Q2 ↔ C65-Q2]** Question2[3]. Is it decidable whether a finite code has a finite completion?

**[E65-RH ↔ C65-RH]** References. The five printed reference strings are reproduced at C65-R1–R5, with uncertainties U3/U4 retained.

**[E65-A ↔ C65-A]** Contributors: Guo Yuqi; Liu Yun.

**[E65-AFF ↔ C65-AFF]** Southwest University.

## Printed-definition, symbol, parameter and quantifier inventory

Only quoted printed material is inventoried below; no additional definition or interpretation is supplied.

| ID / source coordinates | Printed quotation |
|---|---|
| D1 / C64-P2 | “令 X 是一有限集，X* 是由 X 生成的自由幺半群.” |
| D2 / C64-P2 | “称 X* 的元（子集）为 X 上的（半群）字（语言）” |
| D3 / C64-P2 | “称自由幺半群 X* 的幺元1为 X 上的空字” |
| D4 / C64-P2/F1 | “称 X 上一非空语言 C 为 X 上一（代数）码，如果” followed by `∀x1,x2,…,xm,y1,y2,…,yn∈C`, `x1x2…xm=y1y2…yn → m=n, xi=yi, i=1,2,…,m`. |
| D5 / C64-P3 | “X⁺=X*\{1}”; “称 X 上一含于 X⁺=X*\{1} 的非空语言 P 为 X 上一前缀码，如果” |
| D6 / C64-F2 | `∀x,y∈P, ∀z∈X*, y=xz → z=1`. |
| D7 / C64-P4 | “后缀码是前缀码的对偶概念，显然，前、后缀码都是特殊的码.” |
| D8 / C64-P4 | “关于 X 上任一字 x 和 X 的任一元素 a，用 x/a 表示 a 在 x 中出现的次数.” |
| D9 / C64-P4/F3 | “称 X 上两个字 x,y 是交换等价的，记为 x≈y，如果”; `∀a∈X, x/a=y/a`. |
| D10 / C64-P5/F4 | “称 X 上两个语言 A,B 是交换等价的，记为 A≈B，如果存在双射 σ:A→B 使得”; `∀x∈A, x≈σ(x)`. |
| D11 / C64-P6/F5 | “称 X 上一码 C 是完备的，如果”; `∀w∈X*, X*wX*∩C*≠Φ` (final glyph U2). |
| D12 / C64-P7 | “称 X 上一有限码 C 具有有限完备化，如果它能被嵌入一有限完备码.” |
| D13 / C64-P7/F6 | “称 X* 上一语言 L 是正则的，如果 X* 上下述等价关系 ~L 的指数有限：关于任意 x,y∈X*”; `x~L y ⇔ ∀u,v∈X*, uxv∈L ↔ uyv∈L`. |
| D14 / C65-P1/FACT | “显然，有限码是正则码.”; “正则码（特别地，有限码）是完备的当且仅当它是极大的.” |
| D15 / C65-EX | “任何有限前缀（后缀）码”; `{a,b}`, `{aa,ba}`, `{aaaaa,aab,ba,b}` and the completion assertions copied in full at C65-EX. |
| D16 / C65-F1 | `C=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11 b{1,a,a^2}`. |
| Q1 / C65-Q1 | “上面的有限码 C 具有有限完备化（据事实1，即有限极大化）吗？” |
| Q2 / C65-Q2 | “有限码具有有限完备化是可判定的吗？” |
| Printed conjecture wording / C64-P1, C65-P3/P4 | “码交换等价于前缀码”; “有限极大码交换等价于有限极大前缀码”. |

The printed index/symbol occurrences are retained: X,X*,X⁺,1,C,P,L,A,B,σ,~L,≈,x,y,z,a,w,u,v, x1,…,xm, y1,…,yn, m,n,i, the membership/equality/implication signs, intersection and Φ-shaped final glyph, and the literal powers/concatenations in C65-F1. No separate parameter domains, conventions or consequences are added where the page supplies none.

## Uncertain glyphs and unresolved typography

| Marker | Image/page/position in the displayed1109×1568 preview | Literal uncertainty |
|---|---|---|
| U1 | source-math-0080.png, printed64, C64-P1, third text line around y476, immediately after “我们” and before “于这里” | One glyph is not reliably resolved between a 刊-/行-shaped reading. It is left as `⟦U1⟧`, not supplied from another text. The corresponding English clause retains the same gap. |
| U2 | source-math-0080.png, printed64, C64-F5, final glyph around y1078 | The glyph is Φ-shaped; the exact typeform is uncertain. It is provisionally copied as `\Phi`. No meaning or alternate notation is assigned. |
| U3 | source-math-0081.png, printed65, C65-R1/R2, y740–821 | Fine Latin diacritics in the author/French strings are not reliably resolved at the displayed scale. Visible base letters are copied, without silently supplying/correcting accents from bibliographic knowledge. |
| U4 | source-math-0081.png, printed65, C65-R2 second line around y820, `Colloques intern…t.` | One letter appears a-/e-shaped. It is left as `⟦U4⟧`; the word is not normalized to a presumed bibliographic spelling. |

**AMBIGUOUS typography retained:** C65-FACT shows “事实” with reference `[1]`; C65-Q1 says “据事实1”. Both strings are copied without resolving the relation of that numeral to the reference marker. No substantive ambiguity has been resolved into a reformulation.

## Truncation and source-only statement

**TRUNCATED: NO.** The listed images show the entry's title on printed64 and its ending references/contributor/affiliation on printed65, followed by blank page space. No other page was opened or extension attempted.

**Nothing beyond the authorized literal transcription, literal English rendering, quoted printed-definition inventory and source/uncertainty metadata was done.** Printed examples, conjecture/status words and bibliography are copied as source text only: no example was tested, no proof or solution idea developed, no interpretation/status/priority/novelty judgment made. No other source, old proof/held body, CLI payload, OCR/text extraction, scientific computation or lane-owner contact was used. All STOP/HOLD/ZERO, L1, scientific HOLDv2, N4 UNKNOWN/historical child exit UNESTABLISHED and auxiliary214 STOP persist. This packet is not yet an admitted mathematical input to math-5; that requires a later separately frozen lane release.
