# B2 supplement 1 — PDF page 157 / printed page 141

## Source, boundary and clocks

- Sole image newly viewed for this supplement: `institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/source-math-0157.png`. Its SHA256, observed after the ACK, is `3ef412f284c1478ddb282ec2f53d1f13a207c28e827fca46f6b3df3dc890333b`; 362307 bytes. The viewer reported the original dimensions as 1241×1754 pixels.
- Frozen supplement release SHA256: `f021348aedcbbc245df5e3cc19a7d20a7511bb2f8ecb4895715bfd3f8663ab27`. Addendum gate SHA256: `e6abf489c5f9b9f7086d04eb59111c3f88c7c615eef03257848135fd1b92e0e1`.
- Actual pre-image ACK: `book-literal-math-2-supplement-1-prebody-ack-v1.json`, SHA256 `a9ba5d031f5ad016c591f07336f1d77bd6fdc74cb1b2ae013bde967282f1e13a`; prewrite `/bin/date`: **Wed Oct 28 09:39:08 PDT 2026**. ACK and image SHA were observed before viewing the image at **Wed Oct 28 09:39:26 PDT 2026**.
- Actual `/bin/date` immediately before this supplement packet write: **Wed Oct 28 09:40:25 PDT 2026**.
- **TRUNCATED: NO for the entry opening / the combined permitted two-page packet:** the title and opening are visible here; the previously returned page-158 packet includes the continuation and visible ending. **This supplement page by itself ends in an unfinished sentence, after the printed character “组”.** No text from another page is added here, and no page outside the two separately authorized page views was opened. The base packet remains immutable.
- The earlier base-page uncertainty marks, its exposure qualification and all process limitations remain as recorded in the base packet/ACK; this supplement does not silently correct them.

## Position and notation

The entry occupies one body column. B01–B27 below are editorial line labels counted down from its first body line, not printed line numbers. Approximate coordinates for uncertainties are normalized `(x/W,y/H)`, with origin at upper left; the body-line label and quoted word are the primary locator. Displayed mathematics is transcribed in LaTeX-style notation. `[U1]` and `[U2]` are editorial uncertainty markers, not printed glyphs.

## Verbatim printed title and Chinese body

### Header and title

[PDF157 / p141 / running header, upper left] 有限阿贝尔（Abel）群的 Davenport 常数

[PDF157 / p141 / running header, upper right] ·141·

[PDF157 / p141 / title] 有限阿贝尔（Abel）群的 Davenport 常数

[PDF157 / p141 / printed English subtitle] Davenport’s Constants for Finite Abelian Groups

### Body paragraphs

[CN-P1-S1 / PDF157 / p141 / column1 / B01–B03]
有限 Abel 群 \(G\) 的 Davenport 常数 \(D(G)\) 是具有下述性质的最小正整数 \(k\)：任何长为 \(k\) 的 \(G\) 中元序列 \(a_1,\cdots,a_k\) 都包含非空的零和子序列，即有 \(\{1,\cdots,k\}\) 的非空子集 \(I\) 使得 \(\sum_{i\in I}a_i=0\)。

[CN-P1-S2 / PDF157 / p141 / column1 / B03–B04]
如何根据 Abel 群 \(G\) 的结构决定出 Davenport 常数 \(D(G)\) 是组合数论中富有挑战性的著名难题。

[CN-P2-S1 / PDF157 / p141 / column1 / B05–B08]
设 \(G\) 为 \(n\) 阶加法 Abel 群，任给 \(a_1,\cdots,a_n\in G\)，由于 \(G\) 中只有 \(n\) 个不同元素，部分和

\[
s_0=0,\quad s_1=a_1,\quad s_2=a_1+a_2,\cdots,\quad s_n=a_1+\cdots+a_n
\]

中必有两个相等，即有 \(0\le i<j\le n\) 使得 \(0=s_j-s_i=a_{i+1}+\cdots+a_j\)。

[CN-P2-S2 / PDF157 / p141 / column1 / B08–B09]
因此 \(D(G)\) 存在而且 \(D(G)\le |G|\)。

[CN-P3-S1 / PDF157 / p141 / column1 / B10–B12]
Davenport 常数起源于 H. Davenport 在1966年的一项工作；对于理想类群为有限 Abel 群 \(G\) 的代数数域 \(K\)，其整数环中不可约元的素理想因子总个数的最大值就是 Davenport 常数 \(D(G)\)。

[CN-P4-S1 / PDF157 / p141 / column1 / B13]
对于 \(n\) 阶加法循环群 \(\mathbf Z_n=\mathbf Z/n\mathbf Z\)，易见 \(D(\mathbf Z_n)=n\)。

[CN-P4-S2 / PDF157 / p141 / column1 / B13–B15]
Olson 证明了 \(D(\mathbf Z_n\oplus\mathbf Z_n)=2n-1\)，并猜测 \(G\) 为 \(r\) 个 \(\mathbf Z_n\) 的直和时 \(D(G)=1+r(n-1)\)；这个困难的猜测至今仍未解决且进展甚微。

[CN-P4-S3 / PDF157 / p141 / column1 / B15–B17]
阶大于1的有限 Abel 群 \(G\) 在同构的意义下可唯一地表成 \(\mathbf Z_{n_1}\oplus\cdots\oplus\mathbf Z_{n_r}\) 的形式，其中 \(1<n_1\mid n_2\mid\cdots\mid n_r\)，\(r(G)=r\) 与 \(\exp(G)=n_r\) 分别叫做 \(G\) 的秩与幂指数，我们还定义 \(d^*(G)=\sum_{i=1}^{r}(n_i-1)\)。

[CN-P4-S4 / PDF157 / p141 / column1 / B17–B22]
对于 Abel \(p\) 群 \(G\)，1969年 Olson 用群环工具证明了 \(D(G)=1+d^*(G)\)；1992年 A. Geroldinger 与 R. Schnei-  
der 指出有无穷多个秩为4的有限 Abel 群 \(G\) 适合 \(D(G)>1+d^*(G)\)；1969年 P. van Emde Boas 与 D. Kruyswijk 证明对阶大于1的有限 Abel 群 \(G\) 有不等式 \(D(G)\le\exp(G)(1+\ln(|G|/\exp(G)))\)；1994年 W. R. Alford，A. Granville 与 C. Pomer-  
ance 利用这个结果证明有无穷多个 Carmichael 伪素数。

[CN-P5-S1 / PDF157 / p141 / column1 / B23–B25]
零和方面的第一个重要结果是 P. Erdös[U1]，A. Ginzburgh[U2] 与 A. Ziv 在1961年建立的下述著名的 EGZ 定理：长为 \(2n-1\) 的 \(\mathbf Z_n\) 中元序列 \(a_1,\cdots,a_{2n-1}\) 必包含长为 \(n\) 的零和子列。

[CN-P5-S2 / PDF157 / p141 / column1 / B25–B26]
高维东证明了 Caro 的下述猜想：对于有限 Abel 群 \(G\)，\(D(G)+|G|-1\) 是最小的正整数 \(k\) 使得长为 \(k\) 的 \(G\) 中元序列必有长为 \(|G|\) 的零和子列。

[CN-P5-S3 / PDF157 / p141 / column1 / B26–B27]
考虑到 \(D(\mathbf Z_n)=n\)，这个结果蕴涵着 EGZ 定理。

[CN-P5-S4 / PDF157 / p141 / column1 / B27 / page end]
2007年 C. Reiher 通过综合运用代数与组

[Page boundary: the printed sentence is unfinished on this image. The character “组” above is the last visible character.]

No separate reference list, contributor name, or affiliation is printed within this page's visible portion of the entry. The separately returned base page contains the visible later ending; it is not reproduced or changed here.

## Sentence-aligned literal English

The statements and historical/priority wording below are translations of the dated printed text, not present-day status findings.

[EN-title ↔ Chinese title] Davenport constants of finite Abelian (Abel) groups. The book itself prints the English subtitle “Davenport’s Constants for Finite Abelian Groups”.

[EN-P1-S1 ↔ CN-P1-S1 / B01–B03]
The Davenport constant \(D(G)\) of a finite Abel group \(G\) is the smallest positive integer \(k\) having the following property: every sequence \(a_1,\cdots,a_k\) of elements in \(G\) of length \(k\) contains a nonempty zero-sum subsequence, that is, there is a nonempty subset \(I\) of \(\{1,\cdots,k\}\) such that \(\sum_{i\in I}a_i=0\).

[EN-P1-S2 ↔ CN-P1-S2 / B03–B04]
How to determine the Davenport constant \(D(G)\) from the structure of the Abel group \(G\) is a famous challenging difficult problem in combinatorial number theory.

[EN-P2-S1 ↔ CN-P2-S1 / B05–B08]
Let \(G\) be an additive Abel group of order \(n\), and let \(a_1,\cdots,a_n\in G\) be given arbitrarily. Since \(G\) has only \(n\) distinct elements, among the partial sums

\[
s_0=0,\quad s_1=a_1,\quad s_2=a_1+a_2,\cdots,\quad s_n=a_1+\cdots+a_n
\]

there must be two equal ones, that is, there exist \(0\le i<j\le n\) such that \(0=s_j-s_i=a_{i+1}+\cdots+a_j\).

[EN-P2-S2 ↔ CN-P2-S2 / B08–B09]
Therefore \(D(G)\) exists and \(D(G)\le |G|\).

[EN-P3-S1 ↔ CN-P3-S1 / B10–B12]
The Davenport constant originated in a work of H. Davenport in 1966; for an algebraic number field \(K\) whose ideal class group is the finite Abel group \(G\), the maximum total number of prime ideal factors of an irreducible element in its ring of integers is the Davenport constant \(D(G)\).

[EN-P4-S1 ↔ CN-P4-S1 / B13]
For the additive cyclic group \(\mathbf Z_n=\mathbf Z/n\mathbf Z\) of order \(n\), it is easy to see that \(D(\mathbf Z_n)=n\).

[EN-P4-S2 ↔ CN-P4-S2 / B13–B15]
Olson proved \(D(\mathbf Z_n\oplus\mathbf Z_n)=2n-1\), and conjectured that \(D(G)=1+r(n-1)\) when \(G\) is the direct sum of \(r\) copies of \(\mathbf Z_n\); this difficult conjecture remains unsolved to date and has seen very little progress. [This is the book's printed wording.]

[EN-P4-S3 ↔ CN-P4-S3 / B15–B17]
A finite Abel group \(G\) of order greater than1 can, in the sense of isomorphism, be uniquely expressed in the form \(\mathbf Z_{n_1}\oplus\cdots\oplus\mathbf Z_{n_r}\), where \(1<n_1\mid n_2\mid\cdots\mid n_r\); \(r(G)=r\) and \(\exp(G)=n_r\) are respectively called the rank and exponent of \(G\), and we also define \(d^*(G)=\sum_{i=1}^{r}(n_i-1)\).

[EN-P4-S4 ↔ CN-P4-S4 / B17–B22]
For an Abel \(p\)-group \(G\), in1969 Olson proved \(D(G)=1+d^*(G)\) using group-ring tools; in1992 A. Geroldinger and R. Schneider indicated that there are infinitely many finite Abel groups \(G\) of rank4 for which \(D(G)>1+d^*(G)\); in1969 P. van Emde Boas and D. Kruyswijk proved that finite Abel groups \(G\) of order greater than1 obey the inequality \(D(G)\le\exp(G)(1+\ln(|G|/\exp(G)))\); in1994 W. R. Alford, A. Granville and C. Pomerance used this result to prove that there are infinitely many Carmichael pseudoprimes. [The printed page breaks Schneider and Pomerance across lines as shown in the Chinese transcription.]

[EN-P5-S1 ↔ CN-P5-S1 / B23–B25]
The first important result in the area of zero sums is the following famous EGZ theorem established by P. Erdös[U1], A. Ginzburgh[U2] and A. Ziv in1961: a sequence \(a_1,\cdots,a_{2n-1}\) of elements in \(\mathbf Z_n\) of length \(2n-1\) must contain a zero-sum subsequence of length \(n\).

[EN-P5-S2 ↔ CN-P5-S2 / B25–B26]
高维东 proved the following conjecture of Caro: for a finite Abel group \(G\), \(D(G)+|G|-1\) is the smallest positive integer \(k\) such that a sequence of elements in \(G\) of length \(k\) must have a zero-sum subsequence of length \(|G|\).

[EN-P5-S3 ↔ CN-P5-S3 / B26–B27]
Considering \(D(\mathbf Z_n)=n\), this result implies the EGZ theorem.

[EN-P5-S4 ↔ CN-P5-S4 / B27 / page end]
In2007 C. Reiher, by comprehensively applying algebra and “组” … [sentence cut at the page boundary; no completion is supplied here].

## Quoted printed-definition, symbol, parameter and quantifier inventory

|Source position|Printed wording or notation, quoted from this page|
|---|---|
|Title|“有限阿贝尔（Abel）群的 Davenport 常数”; “Davenport’s Constants for Finite Abelian Groups”|
|B01–B03, definition and parameters|“有限 Abel 群 \(G\) 的 Davenport 常数 \(D(G)\) 是具有下述性质的最小正整数 \(k\)”|
|B02–B03, universal and nonempty quantifiers|“任何长为 \(k\) 的 \(G\) 中元序列 \(a_1,\cdots,a_k\) 都包含非空的零和子序列”|
|B02–B03, subset definition wording|“即有 \(\{1,\cdots,k\}\) 的非空子集 \(I\) 使得 \(\sum_{i\in I}a_i=0\)”|
|B03–B04, explicit question|“如何根据 Abel 群 \(G\) 的结构决定出 Davenport 常数 \(D(G)\) 是组合数论中富有挑战性的著名难题”|
|B05, group order and arbitrary inputs|“设 \(G\) 为 \(n\) 阶加法 Abel 群，任给 \(a_1,\cdots,a_n\in G\)”；“\(G\) 中只有 \(n\) 个不同元素”|
|B06–B07, defined partial sums|“部分和 \(s_0=0,\ s_1=a_1,\ s_2=a_1+a_2,\cdots,\ s_n=a_1+\cdots+a_n\)”|
|B08, equality/indices|“中必有两个相等，即有 \(0\le i<j\le n\) 使得 \(0=s_j-s_i=a_{i+1}+\cdots+a_j\)”|
|B08–B09, printed bound|“\(D(G)\) 存在而且 \(D(G)\le\lvert G\rvert\)”|
|B10–B12, number-field wording|“对于理想类群为有限 Abel 群 \(G\) 的代数数域 \(K\)，其整数环中不可约元的素理想因子总个数的最大值就是 Davenport 常数 \(D(G)\)”|
|B13, cyclic-group notation and statement|“\(n\) 阶加法循环群 \(\mathbf Z_n=\mathbf Z/n\mathbf Z\)”；“\(D(\mathbf Z_n)=n\)”|
|B13–B14, printed two-summand expression|“\(D(\mathbf Z_n\oplus\mathbf Z_n)=2n-1\)”|
|B14–B15, explicit conjecture|“猜测 \(G\) 为 \(r\) 个 \(\mathbf Z_n\) 的直和时 \(D(G)=1+r(n-1)\)”；“这个困难的猜测至今仍未解决且进展甚微”|
|B15–B16, finite group and uniqueness wording|“阶大于1的有限 Abel 群 \(G\) 在同构的意义下可唯一地表成 \(\mathbf Z_{n_1}\oplus\cdots\oplus\mathbf Z_{n_r}\) 的形式”|
|B16–B17, divisibility and named parameters|“其中 \(1<n_1\mid n_2\mid\cdots\mid n_r\)，\(r(G)=r\) 与 \(\exp(G)=n_r\) 分别叫做 \(G\) 的秩与幂指数”|
|B17, further definition|“我们还定义 \(d^*(G)=\sum_{i=1}^{r}(n_i-1)\)”|
|B17–B18, group type and equality|“对于 Abel \(p\) 群 \(G\)，1969年 Olson 用群环工具证明了 \(D(G)=1+d^*(G)\)”|
|B18–B19, infinite-family wording|“有无穷多个秩为4的有限 Abel 群 \(G\) 适合 \(D(G)>1+d^*(G)\)”|
|B19–B21, inequality and domain|“对阶大于1的有限 Abel 群 \(G\) 有不等式 \(D(G)\le\exp(G)(1+\ln(|G|/\exp(G)))\)”|
|B21–B22, printed numerical-family claim|“证明有无穷多个 Carmichael 伪素数”|
|B23–B25, named theorem and quantified conclusion|“长为 \(2n-1\) 的 \(\mathbf Z_n\) 中元序列 \(a_1,\cdots,a_{2n-1}\) 必包含长为 \(n\) 的零和子列”|
|B25–B26, named conjecture and minimization|“对于有限 Abel 群 \(G\)，\(D(G)+|G|-1\) 是最小的正整数 \(k\) 使得长为 \(k\) 的 \(G\) 中元序列必有长为 \(|G|\) 的零和子列”|
|B26–B27, printed implication wording|“考虑到 \(D(\mathbf Z_n)=n\)，这个结果蕴涵着 EGZ 定理”|
|B27, cut wording|“2007年 C. Reiher 通过综合运用代数与组”|
|Mathematical signs appearing in these quotations|“\(\in\)”, “\(\sum_{i\in I}\)”, “\(\sum_{i=1}^{r}\)”, “\(\le\)”, “\(<\)”, “\(>\)”, “\(\mid\)”, “\(\oplus\)”, “\(|G|\)”, “\(\cdots\)” and “\(\ln\)”|

This inventory repeats the page's printed statements and definitions without adding a domain, selected input, missing continuation, proof or present-day status conclusion.

## Uncertain glyphs and page-boundary text

- **U1 — AMBIGUOUS diacritic:** in B23 “P. Erdös”, the o-accent is provisionally transcribed as “ö”; “ö/ő” is not resolved. Approximate normalized box: x0.38–0.47, y0.675–0.690; use B23 and the author token as the primary locator.
- **U2 — AMBIGUOUS final letter:** in B23 the name is provisionally transcribed “Ginzburgh”; the apparent final **h** is not resolved with certainty against “Ginzburg”. Approximate normalized box: x0.46–0.56, y0.675–0.690; use B23 and the name token as the primary locator. Neither spelling is supplied or corrected from the base page, memory or another source.
- The end of B27 is a **page cut, not an illegible glyph**: the visible sentence ends at “组” here. No completion is invented in this supplement. The title and opening of the entry are visible on this page.

## Action statement

Nothing beyond direct viewing of the one newly released image, literal transcription, sentence-aligned English rendering, quoted printed-text inventory, uncertainty/truncation reporting and required metadata was done. No proof or interpretation, selected example, status/priority/novelty determination, mathematical source comparison, external source, held review/guide or owner contact was used. The historical claims and conjecture descriptions above are the book's text, not current scientific findings. This source-only supplement is not admitted as a lane input except by a later separately frozen release.
