# B6 — Literal Book Transcription: info-2

## Scope, Source Pins and Actual Clocks

Transcriber: **MathSun8-2 / math-6**. Duty **B6**, source-only transcription of the entry **区间系统的鲁棒严格正实综合**, printed pp.680–682, PDF pp.701–703. **Nothing beyond transcription, literal translation and a printed-text inventory was done.** No interpretation, reformulation, proof, solution idea, example, other source/page or owner contact was used. This packet is not a research result or a later lane release and lifts no STOP/HOLD/ZERO.

- Duty manifest SHA256: `6bc99d52700e6de10ac79c19b139e6a8387cb52961374b6867d0f8235b230346`.
- Frozen gate SHA256: `16441f4ed6394d93360d764ac553d99983eb989fb0253075f2fe69fe2ce84d0b`.
- Extraction receipt SHA256: `19156746c835ef8d8ad6e8b29490376fc69aea32c4b7a5f2ba94b733d071a392`.
- Pre-image ACK: `book-literal-info-2-prebody-ack-v1.json`, SHA256 `38fe359650abb75a425bfe512ae6f6c0c8d3f99ebc86b44f9a515d5b36a0d9af`,16LF/3330B. S0 and the ENTIRE82LF manifest were read before that ACK; NO image was opened before it. The listed gate, receipt and four lane-control records were read as administrative/status controls only; no links, proof bodies or other pages were opened.

|Printed/PDF page|Only viewed literal source image|SHA256|Manifest bytes|Native clock immediately before view|
|---|---|---|---|---|
|680 /701|`source-info-0701.png`|`b1cc2c660fb5cbcb9c9af44dac43bd150fe51b3b935aab95df82a1552b550b60`|397304|Wed Oct 28 09:22:09 PDT 2026|
|681 /702|`source-info-0702.png`|`dff777370aeb6847303c23e72b5814f3d5eeb10decb8e211d2e7b9d39543f13f`|508668|Wed Oct 28 09:22:53 PDT 2026|
|682 /703|`source-info-0703.png`|`0f8a90aa11836f595a8e37ca9b57baee63b0e3884ceb19562059b1b76f7b08ed`|328609|Wed Oct 28 09:23:41 PDT 2026|

All image SHA256s matched the manifest before viewing. Image directory: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/`.

Actual native wake: **Wed Oct 28 09:19:07 PDT 2026**. Native pre-ACK clock: **Wed Oct 28 09:20:18 PDT 2026**; ACK pin clock: **Wed Oct 28 09:21:03 PDT 2026**. Actual native prewrite clock for THIS packet: **Wed Oct 28 09:25:59 PDT 2026**. These are observed clocks, not inferred image-exposure completion times. A later return pins completed bytes.

Coordinate convention: all pages are single-column. Positions below are approximate normalized full-page image coordinates, origin upper left, x increasing rightward and y downward; a y interval identifies the printed visual-line band. These are documentary positions, not computed pixel measurements. Paragraphs are marked P and sentences S for English alignment; these labels are NOT printed in the book. Physical line wrapping and interword spacing are reflowed; source words, sentence punctuation, citation numbers and formulas are retained. The printed line-end hyphen in reference[9] is retained below.

## Verbatim Chinese Transcription and Printed English Text

### Printed Page 680 / PDF Page 701

**[C680-T; column1, x29–72%, y17–20%]** 区间系统的鲁棒严格正实综合

**[C680-ET; column1, x18–84%, y21–24%]** Robust Strictly Positive Real Synthesis for Interval Systems

**[C680-P1-S1; column1, x13–88%, y26–33%]** 传递函数的严格正实性（strictly positive realness，SPR）是系统的一种重要性能，在绝对稳定性与超稳定性理论、二次优化控制及自适应系统理论等领域中起着十分重要的作用。

**[C680-P1-S2; column1, x13–88%, y31–35%]** 因实际系统中总存在有不确定性，研究系统的鲁棒严格正实性尤为有意义。

**[C680-P1-S3; column1, x13–88%, y33–37%]** 20世纪90年代以来，受鲁棒稳定性分析中参数化方法的刺激，系统鲁棒严格正实性的研究得到了广泛的关注和发展。

**[C680-P2-S1; column1, x13–88%, y37–42%]** 早期得到的多数结果是属于鲁棒严格正实分析的，系统鲁棒严格正实分析方面的最好结果是由文献[1]、[2]几乎同时独立得到的“八顶点检验定理”。

**[C680-P3-S1; column1, x13–88%, y42–51%]** 对鲁棒正实综合问题，通过正实引理，可以给出传递函数的基于矩阵不等式的正实性条件[3]，但用该方法进行鲁棒正实综合时，需引进较多的变元，得到的矩阵不等式的阶次较高，并且所得条件是用矩阵不等式的可解性来表述的，而这一点在理论上未有完整的结果。

**[C680-P4-S1; column1, x13–88%, y51–53%]** 首先给出相关的定义、记号及基本问题的描述。

**[C680-P4-S2; column1, x13–88%, y53–56%]** 由于严格正实性源于控制理论的多个领域，不同的文献采用了稍有不同的定义[3]。

**[C680-P4-S3; column1, x13–88%, y54–56%]** 本文采用如下定义。

**[C680-P5-S1; column1, x13–88%, y56–60%]** \(\mathbf R\)表示实数域，记\(P^n\)为\(n\)阶实系数多项式集合，\(H^n\subset P^n\)是\(n\)阶实系数Hurwitz稳定多项式（仅具有负实部的根）集合。

**[C680-P5-S2; column1, x13–88%, y58–63%]** 在下述定义中，\(b(s)\in P^m\)，\(a(s)\in P^n\)，\(p(s)=b(s)/a(s)\)是有理函数。

**[C680-D1; column1, x13–88%, y63–67%]** **定义1** \(p(s)\)称为是严格正实的，记为\(p(s)\in\mathrm{SPR}\)，是指\(b(s)\in P^n\)，\(a(s)\in H^n\)且对\(\forall\omega\in\mathbf R\)，\(\operatorname{Re}[p(j\omega)]>0\)。

**[C680-D2; column1, x13–88%, y67–72%]** **定义2** 一个多项式集合\(F\)称为是鲁棒稳定的，是指集合\(F\)中的每一个元均是Hurwitz稳定多项式。

**[C680-P6-S1; column1, x17–75%, y72–74%]** 鲁棒正实综合问题的基本提法如下。

**[C680-Q1; column1, x13–88%, y74–79%]** **鲁棒严格正实综合基本问题** 给定一个\(n\)阶多项式集\(F\)，是否存在、如何找出一个（固定的）多项式\(b(s)\)，使对\(\forall a(s)\in F\)有\(b(s)/a(s)\)是严格正实的？

**[C680-P7-S1; column1, x13–88%, y79–85%]** 从严格正实性的定义容易知道，多项式集\(F\)的鲁棒稳定性是存在一个（固定的）多项式\(b(s)\)，使对\(\forall a(s)\in F\)，\(b(s)/a(s)\)严格正实的必要条件。

**[C680-P7-S2; column1, x13–88%, y83–85%]** 另外，考虑如下问题。

**[C680-Q2; column1, x13–88%, y85–91%]** **鲁棒严格正实域刻画问题** 给定\(a(s)\in H^n\)，如何找出所有的\(b(s)\)，使\(p(s)=\dfrac{b(s)}{a(s)}\in\mathrm{SPR}\)？

### Printed Page 681 / PDF Page 702

**[C681-P1-S1; column1, x13–88%, y12–15%]** 该问题对鲁棒严格正实的分析与综合是有意义的。

**[C681-P1-S2; column1, x13–88%, y13–17%]** 特别，给出\(b(s)\)的基于\(a(s)\)的系数的显式表达条件是文献[4]提出的一个问题。

**[C681-P2-S1; column1, x13–88%, y17–19%]** 传递函数严格正实性的判定，本质上可以化为多项式实根的判定问题。

**[C681-P2-S2; column1, x13–88%, y19–24%]** 古典Sturm组方法虽然也可用于判定多项式实根的分布，但是对文字（符号）系数的多项式建立判别系统是没有效率的[5]。

**[C681-P3-S1; column1, x13–88%, y24–28%]** 1996年，由杨路等建立的多项式完全判别系统可以给出一组由多项式系数构成的显式表达式来判定多项式根的状况[5]。

**[C681-P3-S2; column1, x13–88%, y26–32%]** 文献[6]借此给出了传递函数鲁棒严格正实域的描述，从而理论上完整解决了上面的鲁棒严格正实域刻画问题。

**[C681-P4-S1; column1, x13–88%, y33–40%]** 对于鲁棒严格正实综合问题，当所给定的多项式集合是稳定的多项式线段集、或稳定的区间多项式集、或稳定的凸多面体多项式集时，由于这些集合在鲁棒稳定性理论中具有的特殊重要性及严格正实性本身的特点，受到了研究者的充分重视。

**[C681-P4-S2; column1, x13–88%, y40–42%]** 这方面已有结果总结如下。

**[C681-P5-S1; column1, x13–88%, y42–51%]** 当\(F\)的元具有相同的偶次（或奇次）项时，这样的多项式\(b(s)\)是存在的[3,4,7]，这一结果最先由Hollot等[7]于1989年针对区间多项式集而得到，1990年又被推广至更为一般的结果，与文献[7]完全相同的结果于1997年又被Patel和Datta重新得到[8]。

**[C681-P6-S1; column1, x13–88%, y51–55%]** 当\(F\)为低阶的（\(n\leqslant3\)）稳定的区间多项式集时[3,4,7]，这样的多项式\(b(s)\)也是存在的。

**[C681-P6-S2; column1, x13–88%, y53–62%]** 应该提及的是，Anderson等[9]于1990年利用线性规划的方法，给出了使上述问题存在解的一组条件[即文献[9]中的式（58）～式（60）]，并认为，对任给的4次区间多项式集，该组条件总是可以满足的，因而认为，上述问题对4次区间多项式集也就完全解决了。

**[C681-P6-S3; column1, x13–88%, y60–64%]** 但是，1993年，Betser和Zeheb举出反例说明，文献[9]中给出的仅是一个充分性的条件。

**[C681-P6-S4; column1, x13–88%, y64–68%]** 当时，即使对于4次稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数？

**[C681-P6-S5; column1, x13–88%, y67–72%]** 一方面，理论上不能正面证明这一结论，另一方面，也从未发现有反例说明结论不成立，因而成为鲁棒严格正实综合领域著名的公开问题[3,4,7,9]。

**[C681-P6-S6; column1, x13–88%, y71–76%]** 后来，文献[10]利用针对稳定多项式线段鲁棒严格正实综合的技巧，给出了4次区间稳定多项式集鲁棒严格正实综合正面肯定的答案。

**[C681-P7-S1; column1, x13–88%, y76–83%]** 上述结果表明，任意阶多项式线段或低阶（\(n\leqslant4\)）区间多项式的鲁棒稳定性，是实现其鲁棒严格正实综合的充分必要条件，换句话说，鲁棒稳定性与鲁棒严格正实可综合性在某些情况下是等价的，这是具有深刻科学内涵的结论。

**[C681-P8-S1; column1, x13–88%, y83–87%]** 上述所有这些结果均是针对连续时间系统而言的，这些结果可以直接推广到离散时间系统、甚至D-SPR的情形[3]。

**[C681-P9-S1; column1, x13–88%, y87–92%]** 此外，一些存在结果表明多项式线段和区间多项式鲁棒严格正实综合与凸多面体多项式集的鲁棒严格正实综合是有内在的本质不同。

**[C681-P9-S2a; column1, x13–88%, y90–92%; CONTINUES at C682-P1-S2b]** 因此，对高阶区间

### Printed Page 682 / PDF Page 703

**[C682-P1-S2b; column1, x13–88%, y12–15%; CONTINUATION of C681-P9-S2a]** 多项式集的鲁棒严格正实综合就尤为重要。

**[C682-P1-S3; column1, x13–88%, y14–17%]** 如下区间系统的鲁棒严格正实综合问题仍是理论上尚未解决的具有挑战性的公开问题[3,4,7,9]。

**[C682-Q3-S1; column1, x13–88%, y17–24%]** **区间系统的鲁棒严格正实综合问题** 对于阶次大于4的稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数？

**[C682-Q3-S2; column1, x13–88%, y22–26%]** 或者大于4阶的区间多项式集的鲁棒稳定性是否也是其鲁棒严格正实综合的充分必要条件？

**[C682-P2-S1; column1, x13–88%, y26–31%]** 从计算的大量数值例子来看，给定稳定的区间多项式集，这样的多项式都可以找到，尚未发现反例，因此，我们推测该问题可能会有正面肯定的答案。

**[C682-RH; column1, x44–57%, y33–35%]** 参考文献

**[C682-R1; column1, x13–88%, y37–41%]** [1] Chapellat H, Dahleh M, Bhattacharyya S P. On robust nonlinear stability of interval control systems. IEEE Trans. on Automat. Contr., 1991, AC-36:59—69.

**[C682-R2; column1, x13–88%, y41–44%]** [2] 王龙, 黄琳. 区间有理函数严格正实性的有限检验. 科学通报, 1991, 36:262—264.

**[C682-R3; column1, x13–88%, y43–46%]** [3] 郁文生. 系统鲁棒严格正实综合与鲁棒稳定性分析[博士学位论文]. 北京:北京大学, 1998.

**[C682-R4; column1, x13–88%, y45–51%]** [4] Huang L, Hollot C V, Xu Z L. Robust analysis of strictly positive real function set. Preprints of Proceedings of the Second Japan-China Joint Symposium on Systems Control Theory and its Applications, 1990:210—220.

**[C682-R5; column1, x13–88%, y51–55%]** [5] 杨路, 张景中, 侯晓荣. 非线性代数方程组与机器证明（非线性科学丛书）. 上海:上海科学教育出版社, 1996.

**[C682-R6; column1, x13–88%, y55–61%]** [6] Wang L, Yu W S. Complete characterization of strictly positive real regions and robust strictly positive real synthesis method. Science in China Series E:Technological Sciences, 2000, 43:97—112.

**[C682-R7; column1, x13–88%, y61–67%]** [7] Hollot C V, Huang L, Xu Z L. Designing strictly positive real transfer function families:A necessary and sufficient condition for low degree and structured families//Proceedings of Mathematical Theory of Network and Systems, Boston, 1989:215—227.

**[C682-R8; column1, x13–88%, y67–71%]** [8] Patel V V, Datta K B. Classification of units in \(H_\infty\) and an alternative proof of Kharitonov’s theorem. IEEE Trans. on Circuits Syst. ;Part I, 1997, CAS-44:454—458.

**[C682-R9; column1, x13–88%, y71–75%]** [9] Anderson B D O, Dasgupta S, Khargonekar P, et al. Robust strict positive realness:Character-
ization and construction. IEEE Trans. on Circuits Syst., 1990, CAS-37:869—876.

**[C682-R10; column1, x13–88%, y75–79%]** [10] Yu W S, Wang L. Anderson’s claim on fourth-order SPR synthesis is true. IEEE Trans. on Circuits Syst. ;Part I, 2001, CAS-48:506—509.

**[C682-A; column1, x58–88%, y84–87%]** 撰稿人：郁文生¹　王龙²

**[C682-A1; column1, x61–88%, y87–89%]** 1　华东师范大学软件学院

**[C682-A2; column1, x68–88%, y89–92%]** 2　北京大学工学院

## Sentence-Aligned Literal English Rendering

The following is solely the literal rendering of the printed text above. Matching C/E identifiers give the alignment; the cross-page sentence is aligned as one joined sentence. The English words already printed in the entry and references are retained as printed, not independently supplied claims.

**[E680-T ↔ C680-T]** Robust Strictly Positive Real Synthesis for Interval Systems.

**[E680-ET ↔ C680-ET]** Robust Strictly Positive Real Synthesis for Interval Systems.

**[E680-P1-S1]** Strict positive realness (strictly positive realness, SPR) of a transfer function is an important performance property of a system, and plays a very important role in such fields as the theories of absolute stability and hyperstability, quadratic optimization control, and adaptive-system theory.

**[E680-P1-S2]** Because uncertainty always exists in actual systems, studying the robust strict positive realness of systems is especially meaningful.

**[E680-P1-S3]** Since the 1990s, stimulated by parameterization methods in robust-stability analysis, research on the robust strict positive realness of systems has received extensive attention and development.

**[E680-P2-S1]** Most results obtained in the early period belong to robust strict-positive-real analysis; the best result in the analysis of system robust strict positive realness is the “eight-vertex test theorem” obtained almost simultaneously and independently in references[1] and[2].

**[E680-P3-S1]** For the robust positive-real synthesis problem, through the positive-real lemma one can give matrix-inequality-based positive-realness conditions for transfer functions[3], but using that method for robust positive-real synthesis requires introducing more variables, the resulting matrix inequalities have higher order, and the obtained conditions are expressed by the solvability of matrix inequalities, for which there are not yet complete theoretical results.

**[E680-P4-S1]** First, the related definitions, notation and description of the basic problem are given.

**[E680-P4-S2]** Because strict positive realness originates in several fields of control theory, different references have adopted slightly different definitions[3].

**[E680-P4-S3]** This article adopts the following definitions.

**[E680-P5-S1]** \(\mathbf R\) denotes the real-number field; write \(P^n\) for the set of nth-order real-coefficient polynomials, and \(H^n\subset P^n\) is the set of nth-order real-coefficient Hurwitz-stable polynomials (having only roots with negative real parts).

**[E680-P5-S2]** In the definitions below, \(b(s)\in P^m\), \(a(s)\in P^n\), and \(p(s)=b(s)/a(s)\) is a rational function.

**[E680-D1]** **Definition1.** \(p(s)\) is called strictly positive real, written \(p(s)\in\mathrm{SPR}\), meaning that \(b(s)\in P^n\), \(a(s)\in H^n\), and for \(\forall\omega\in\mathbf R\), \(\operatorname{Re}[p(j\omega)]>0\).

**[E680-D2]** **Definition2.** A polynomial set \(F\) is called robustly stable, meaning that every element in the set \(F\) is a Hurwitz-stable polynomial.

**[E680-P6-S1]** The basic formulation of the robust positive-real synthesis problem is as follows.

**[E680-Q1]** **Basic problem of robust strictly positive real synthesis.** Given an nth-order polynomial set \(F\), does there exist, and how does one find, a (fixed) polynomial \(b(s)\), such that for \(\forall a(s)\in F\), \(b(s)/a(s)\) is strictly positive real?

**[E680-P7-S1]** From the definition of strict positive realness it is easy to know that robust stability of the polynomial set \(F\) is a necessary condition for the existence of a (fixed) polynomial \(b(s)\) making \(b(s)/a(s)\) strictly positive real for \(\forall a(s)\in F\).

**[E680-P7-S2]** In addition, consider the following problem.

**[E680-Q2]** **Problem of characterizing the robust strictly positive real region.** Given \(a(s)\in H^n\), how does one find all \(b(s)\) such that \(p(s)=\dfrac{b(s)}{a(s)}\in\mathrm{SPR}\)?

**[E681-P1-S1]** This problem is meaningful for the analysis and synthesis of robust strict positive realness.

**[E681-P1-S2]** In particular, giving explicit expression conditions for \(b(s)\) based on the coefficients of \(a(s)\) is a problem raised in reference[4].

**[E681-P2-S1]** The determination of strict positive realness of a transfer function can essentially be reduced to the determination of real roots of polynomials.

**[E681-P2-S2]** Although the classical Sturm-group method can also be used to determine the distribution of real roots of polynomials, it is not efficient for establishing a discrimination system for polynomials with literal (symbolic) coefficients[5].

**[E681-P3-S1]** In1996, the complete polynomial discrimination system established by Yang Lu and others could provide a group of explicit expressions composed of polynomial coefficients to determine the situation of polynomial roots[5].

**[E681-P3-S2]** Reference[6] used this to give a description of transfer-function robust strictly positive real regions, thereby completely solving theoretically the above problem of characterizing the robust strictly positive real region.

**[E681-P4-S1]** For the robust strictly positive real synthesis problem, when the given polynomial set is a stable polynomial-segment set, or a stable interval-polynomial set, or a stable convex-polytope polynomial set, these sets’ special importance in robust-stability theory and the characteristics of strict positive realness itself have attracted researchers’ full attention.

**[E681-P4-S2]** Existing results in this respect are summarized below.

**[E681-P5-S1]** When the elements of \(F\) have identical even-degree (or odd-degree) terms, such a polynomial \(b(s)\) exists[3,4,7]; this result was first obtained by Hollot and others[7] in1989 for interval-polynomial sets, was extended in1990 to a more general result, and a result completely identical to reference[7] was obtained again in1997 by Patel and Datta[8].

**[E681-P6-S1]** When \(F\) is a stable interval-polynomial set of low order (\(n\leqslant3\))[3,4,7], such a polynomial \(b(s)\) also exists.

**[E681-P6-S2]** It should be mentioned that Anderson and others[9] in1990 used a linear-programming method to give a group of conditions for the above problem to have a solution [namely formulas(58) through(60) in reference[9]], and believed that, for any given fourth-degree interval-polynomial set, that group of conditions could always be satisfied, and therefore believed that the above problem had also been completely solved for fourth-degree interval-polynomial sets.

**[E681-P6-S3]** However, in1993, Betser and Zeheb gave a counterexample showing that what reference[9] gave was only a sufficient condition.

**[E681-P6-S4]** At that time, even for fourth-degree stable interval-polynomial sets, did there actually exist a polynomial which, together with that polynomial set, could be configured into strictly positive real rational functions?

**[E681-P6-S5]** On the one hand, this conclusion could not be positively proved theoretically, and on the other hand, no counterexample showing that the conclusion failed had ever been found; it therefore became a famous open problem in the field of robust strictly positive real synthesis[3,4,7,9].

**[E681-P6-S6]** Later, reference[10], using techniques for robust strictly positive real synthesis of stable polynomial segments, gave a positively affirmative answer for robust strictly positive real synthesis of fourth-degree interval-stable polynomial sets.

**[E681-P7-S1]** The above results show that robust stability of polynomial segments of arbitrary order or low-order (\(n\leqslant4\)) interval polynomials is a necessary and sufficient condition for realizing their robust strictly positive real synthesis; in other words, robust stability and robust strict-positive-real synthesizability are equivalent in certain situations, a conclusion with profound scientific implications.

**[E681-P8-S1]** All these results above concern continuous-time systems; these results can be extended directly to discrete-time systems, and even to the D-SPR situation[3].

**[E681-P9-S1]** In addition, some existence results show an inherent essential difference between robust strictly positive real synthesis of polynomial segments and interval polynomials and robust strictly positive real synthesis of convex-polytope polynomial sets.

**[E681-P9-S2a + E682-P1-S2b]** Therefore, robust strictly positive real synthesis of high-order interval-polynomial sets is especially important.

**[E682-P1-S3]** The following robust strictly positive real synthesis problem for interval systems remains a challenging open problem not yet solved theoretically[3,4,7,9].

**[E682-Q3-S1]** **Problem of robust strictly positive real synthesis for interval systems.** For a stable interval-polynomial set of order greater than4, does there actually exist a polynomial which, together with that polynomial set, can be configured into strictly positive real rational functions?

**[E682-Q3-S2]** Or is robust stability of an interval-polynomial set of order greater than4 also a necessary and sufficient condition for its robust strictly positive real synthesis?

**[E682-P2-S1]** Judging from the large number of numerical examples computed, for given stable interval-polynomial sets such polynomials can all be found, and no counterexample has yet been found; therefore, we conjecture that this problem may have a positively affirmative answer.

**[E682-RH]** References.

**[E682-R1]** [1] Chapellat H, Dahleh M, Bhattacharyya S P. On robust nonlinear stability of interval control systems. IEEE Trans. on Automat. Contr., 1991, AC-36:59—69.

**[E682-R2]** [2] Wang Long, Huang Lin. A finite test of strict positive realness of interval rational functions. Science Bulletin, 1991, 36:262—264.

**[E682-R3]** [3] Yu Wensheng. System robust strictly positive real synthesis and robust-stability analysis [doctoral degree dissertation]. Beijing:Peking University, 1998.

**[E682-R4]** [4] Huang L, Hollot C V, Xu Z L. Robust analysis of strictly positive real function set. Preprints of Proceedings of the Second Japan-China Joint Symposium on Systems Control Theory and its Applications, 1990:210—220.

**[E682-R5]** [5] Yang Lu, Zhang Jingzhong, Hou Xiaorong. Nonlinear algebraic equation systems and machine proof (Nonlinear Science Series). Shanghai:Shanghai Scientific and Technical Education Publishing House, 1996.

**[E682-R6]** [6] Wang L, Yu W S. Complete characterization of strictly positive real regions and robust strictly positive real synthesis method. Science in China Series E:Technological Sciences, 2000, 43:97—112.

**[E682-R7]** [7] Hollot C V, Huang L, Xu Z L. Designing strictly positive real transfer function families:A necessary and sufficient condition for low degree and structured families//Proceedings of Mathematical Theory of Network and Systems, Boston, 1989:215—227.

**[E682-R8]** [8] Patel V V, Datta K B. Classification of units in \(H_\infty\) and an alternative proof of Kharitonov’s theorem. IEEE Trans. on Circuits Syst. ;Part I, 1997, CAS-44:454—458.

**[E682-R9]** [9] Anderson B D O, Dasgupta S, Khargonekar P, et al. Robust strict positive realness:Character-
ization and construction. IEEE Trans. on Circuits Syst., 1990, CAS-37:869—876.

**[E682-R10]** [10] Yu W S, Wang L. Anderson’s claim on fourth-order SPR synthesis is true. IEEE Trans. on Circuits Syst. ;Part I, 2001, CAS-48:506—509.

**[E682-A]** Contributors: Yu Wensheng¹ (郁文生), Wang Long² (王龙).

**[E682-A1]** 1　School of Software, East China Normal University.

**[E682-A2]** 2　College of Engineering, Peking University.

## Printed Definition, Symbol, Parameter and Quantifier Inventory

This inventory QUOTES the printed text above; it adds no definition, inference, coefficient convention or reformulation.

1. **Name and abbreviation:** C680-P1-S1 prints “严格正实性（strictly positive realness，SPR）”; C680-D1 prints “\(p(s)\in\mathrm{SPR}\)”.
2. **Real-number field:** C680-P5-S1 prints “\(\mathbf R\)表示实数域”.
3. **Polynomial-set symbol and order parameter:** C680-P5-S1 prints “记\(P^n\)为\(n\)阶实系数多项式集合”. The printed symbols are \(P^n\) and \(n\).
4. **Stable polynomial-set symbol, containment and root clause:** C680-P5-S1 prints “\(H^n\subset P^n\)是\(n\)阶实系数Hurwitz稳定多项式（仅具有负实部的根）集合”.
5. **Numerator, denominator, argument and other order parameter:** C680-P5-S2 prints “\(b(s)\in P^m\)，\(a(s)\in P^n\)，\(p(s)=b(s)/a(s)\)是有理函数”. The printed symbols here are \(b(s),a(s),p(s),s,m,n,P^m,P^n\).
6. **Definition1, in full:** “\(p(s)\)称为是严格正实的，记为\(p(s)\in\mathrm{SPR}\)，是指\(b(s)\in P^n\)，\(a(s)\in H^n\)且对\(\forall\omega\in\mathbf R\)，\(\operatorname{Re}[p(j\omega)]>0\)。” The quoted clause contains the printed symbols \(\forall,\omega,j,\operatorname{Re},>,0\) and retains the printed \(P^n\) in this definition. It is not replaced by the preceding \(P^m\).
7. **Definition2 and its element quantifier, in full:** “一个多项式集合\(F\)称为是鲁棒稳定的，是指集合\(F\)中的每一个元均是Hurwitz稳定多项式。”
8. **Basic synthesis question and fixed/universal quantifiers, in full:** C680-Q1 prints “给定一个\(n\)阶多项式集\(F\)，是否存在、如何找出一个（固定的）多项式\(b(s)\)，使对\(\forall a(s)\in F\)有\(b(s)/a(s)\)是严格正实的？”
9. **Printed necessary-condition sentence and repeated quantifier:** C680-P7-S1 prints “多项式集\(F\)的鲁棒稳定性是存在一个（固定的）多项式\(b(s)\)，使对\(\forall a(s)\in F\)，\(b(s)/a(s)\)严格正实的必要条件”.
10. **Region-characterization question and all-numerators quantifier, in full:** C680-Q2 prints “给定\(a(s)\in H^n\)，如何找出所有的\(b(s)\)，使\(p(s)=\dfrac{b(s)}{a(s)}\in\mathrm{SPR}\)？”
11. **Printed coefficient-dependence wording:** C681-P1-S2 prints “给出\(b(s)\)的基于\(a(s)\)的系数的显式表达条件”.
12. **Printed polynomial-family phrases:** C681-P4-S1 prints “稳定的多项式线段集、或稳定的区间多项式集、或稳定的凸多面体多项式集”; C681-P9-S1 repeats “多项式线段和区间多项式” and “凸多面体多项式集”.
13. **Parity-condition quantifier:** C681-P5-S1 prints “当\(F\)的元具有相同的偶次（或奇次）项时，这样的多项式\(b(s)\)是存在的”.
14. **First printed low-order bound:** C681-P6-S1 prints “当\(F\)为低阶的（\(n\leqslant3\)）稳定的区间多项式集时[3,4,7]，这样的多项式\(b(s)\)也是存在的”.
15. **Referenced formula numbers, not reproduced formulas:** C681-P6-S2 prints “[即文献[9]中的式（58）～式（60）]”. No formulas from that cited source are supplied here.
16. **Fourth-degree/any-given wording:** C681-P6-S2 prints “对任给的4次区间多项式集，该组条件总是可以满足的”; C681-P6-S4 prints the question “即使对于4次稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数？”
17. **Arbitrary-order and second low-order bound:** C681-P7-S1 prints “任意阶多项式线段或低阶（\(n\leqslant4\)）区间多项式的鲁棒稳定性，是实现其鲁棒严格正实综合的充分必要条件”.
18. **Printed time-system and additional abbreviation wording:** C681-P8-S1 prints “连续时间系统” and “离散时间系统、甚至D-SPR的情形[3]”. This is the printed occurrence of D-SPR.
19. **Final named question, existence quantifier and order range, in full:** C682-Q3-S1 prints “对于阶次大于4的稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数？”
20. **Final alternative question, in full:** C682-Q3-S2 prints “或者大于4阶的区间多项式集的鲁棒稳定性是否也是其鲁棒严格正实综合的充分必要条件？”
21. **Printed conjectural wording:** C682-P2-S1 prints “因此，我们推测该问题可能会有正面肯定的答案”.
22. **Other printed mathematical notation in references:** C682-R8 prints \(H_\infty\); the same reference prints “Kharitonov’s theorem”. The body prints “Sturm组方法”, “正实引理”, “八顶点检验定理” and “多项式完全判别系统” at C681-P2-S2, C680-P3-S1, C680-P2-S1 and C681-P3-S1 respectively. These are quoted names/notation only, not supplied theorem statements or imported proof tools.
23. **Printed contributors and affiliation markers:** C682-A/A1/A2 print “郁文生¹　王龙²”, “1　华东师范大学软件学院”, “2　北京大学工学院”. The complete printed references[1]–[10] are transcribed and aligned above.

## Illegible or Uncertain Glyphs and Ambiguous Sentences

No illegible or uncertain glyph is declared after direct viewing of the three listed images. No sentence is silently resolved by adding a missing hypothesis or mathematical definition. The expression in C680-P5-S2 is transcribed as \(b(s)\in P^m\), while Definition1 is transcribed as \(b(s)\in P^n\), exactly as displayed; no reconciliation is attempted. The printed term “Sturm组方法” is rendered literally as “Sturm-group method”, without expanding it into an unprinted definition. These are transcription choices, not mathematical interpretations.

## Truncation Flag and Source-Only Completion

**TRUNCATED: NO.** The entry visibly ends on printed p.682 with the contributor line and both numbered affiliations; no continuation beyond the three listed images is visible. No extra page was sought or viewed.

**Nothing beyond transcription was done.** The only primary problem text viewed was in the three manifest-listed images. No mathematical reasoning, proof, solution idea, numerical example, status/priority/novelty assessment, source search, owner contact, scientific execution or selected check was performed. Every STOP/HOLD/ZERO, the L1 recipient frontier, scientific HOLDv2, N4 UNKNOWN and auxiliary214 STOP remains unchanged. This packet becomes an admitted lane input only through a later separately frozen release.
