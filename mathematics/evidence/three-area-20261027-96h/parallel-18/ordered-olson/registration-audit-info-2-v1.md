# Registration audit — info-2 printed entry versus registered septic target

Auditor **MathOlson-2-2**. Actual native `/bin/date` before this write: **Wed Oct 28 09:48:42 PDT 2026**.
This is a **DOCUMENTARY registration delta**, not a mathematical equivalence or a change to the registered target.

## Input bindings, actual order and notation

All frozen input SHA256s are bound here; actual live hashes of the listed source/receipt/status inputs matched their manifest pins.

| Input | LF | SHA256 |
|---|---:|---|
| S0 mandatory controls | 31 | `a7161aa016f59552d9ee823cd2e4205df74ef2308e6ad25c4ed18322d78e580b` |
| Audit release | complete | `efb045dc3b8e7dc9271ba5a16e3c3a2f17a0a2d1be364eba7e17f87e3113bef0` |
| Literal packet v1 | 300 | `41bfcab9dd1a784e76f7db022955b5bc2e45c105cffe76661720e502ceed2e47` |
| Mandatory erratum 1 | 201 | `4cbf03691952d0dd1d83d482b84540fa9c36138ad536b33a5a765b8ba6cf12c6` |
| Prior fidelity comparison | 98 | `ea05272f3c3e0727a89ab5a8a6e7c8be96fbe32e7df3d30d99f99cc3d4e794f9` |
| Erratum recheck | 53 | `7e257946afdd88878fc5a275475b962e80a72a85b289f264923324dbc6b592f6` |
| B6 return receipt | 36 | `47969285f7eeb80069b51dbe37fcab93b98a840e45f88a3340c2273d2124c435` |
| Erratum recheck return receipt | 23 | `6ef1631558ec85838b29dc089c19d09e7b58f850e7ed583b5e4015a6e44101e1` |
| Registered target text | 37 | `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad` |
| SPR post-v6 STOP, STATUS ONLY | 18 | `81804ea983f70b2bb307bc474a73059224f973d4ff0fdba22ea55c872bd230cd` |

S0 and the entire audit manifest were read FIRST. The required `registration-audit-info-2-prebody-ack-v1.json` was written at actual09:47:17 PDT BEFORE any listed body was reopened; its SHA256 is `312ef8c73e411df0b3c9d87d87e10c99b6770267ac6f13c1a72de82e5dffaa64`.
Then the complete literal packet, complete erratum and complete registered definition were read in that order; the two complete prior comparison outputs, two complete receipts and complete STOP status were also read as allowed context. No linked source, proof, old body or other lane file was opened.

**P** below means the literal packet `book-literal-info-2-v1.md`; **E** means its ADDITIVE erratum; **R** means the actual file `written-releases/info-2-septic-box-definitions-v1.md`. Line numbers after R are the file's actual lines, NOT the dossier line numbers embedded after `|`.
Where an erratum corrects a quotation, the corrected E lines control; original P bytes remain unchanged. The prior **EXACT_WITH_ERRATUM** verdict is a documentary fidelity boundary, not mathematical evidence.

Each numbered item is one grouped documentary comparison. A and B distinguish printed wording that is respectively **captured in part/as stated** and **not present as such** in the short registration; C records registration-only content; D names unresolved wording/equivalence questions. Where one side is absent, the nearest actual quotation is shown rather than fabricating a corresponding sentence. Categories can refer to different aspects of the same sentence; the counts below are item counts, not a claim of exhaustive mathematical equivalence.

# A. Printed wording captured in the registration

### A1. Title
**Print Chinese:** “区间系统的鲁棒严格正实综合” (P:28). **Print English:** “Robust Strictly Positive Real Synthesis for Interval Systems” (P:30,151).  
**Registration:** “区间系统的鲁棒严格正实综合” (R:7), and “Robust SPR synthesis for interval polynomial families of degree > 4” (R:5). The Chinese title wording is present; the added English degree formulation is addressed separately.

### A2. Printed contributor names
**Print Chinese:** “撰稿人：郁文生¹　王龙²” (P:141). **Print English:** “Contributors: Yu Wensheng¹ (郁文生), Wang Long² (王龙)” (P:258).  
**Registration:** “郁文生 (Yu Wensheng), 王龙 (Wang Long)” (R:7). The two names occur; the affiliation details are addressed in B.

### A3. Real-polynomial and Hurwitz symbols
**Print Chinese:** “\(\mathbf R\)表示实数域，记\(P^n\)为\(n\)阶实系数多项式集合，\(H^n\subset P^n\)是\(n\)阶实系数Hurwitz稳定多项式（仅具负实部的根）集合” (P:48, corrected E:135). **Print English:** “\(\mathbf R\) denotes the real-number field; write \(P^n\) for the set of nth-order real-coefficient polynomials, and \(H^n\subset P^n\) is the set of nth-order real-coefficient Hurwitz-stable polynomials (having only roots with negative real parts)” (E:143).  
**Registration:** “Let P^n be the real polynomials of order n and H^n ⊂ P^n the Hurwitz ones” (R:13). The symbol/order/real/Hurwitz wording is present; the explicit root parenthesis is separately B2.

### A4. Strict positive-real definition and real-frequency quantifier
**Print Chinese:** “\(p(s)\)称为是严格正实的，记为\(p(s)\in\mathrm{SPR}\)，是指\(b(s)\in P^n\)，\(a(s)\in H^n\)且对\(\forall\omega\in\mathbf R\)，\(\operatorname{Re}[p(j\omega)]>0\)” (P:52). **Print English:** “\(p(s)\) is called strictly positive real … \(b(s)\in P^n\), \(a(s)\in H^n\), and for \(\forall\omega\in\mathbf R\), \(\operatorname{Re}[p(j\omega)]>0\)” (P:175).  
**Registration:** “For b ∈ P^n and a ∈ H^n, b/a is strictly positive real (SPR) iff Re[b(jω)/a(jω)] > 0 for all real ω (Definition 1)” (R:13–15). This identifies common displayed clauses; the differing written formulation is not proved equivalent here.

### A5. Robust stability definition
**Print Chinese:** “一个多项式集合\(F\)称为是鲁棒稳定的，是指集合\(F\)中的每一个元均是Hurwitz稳定多项式” (P:54). **Print English:** “A polynomial set \(F\) is called robustly stable, meaning that every element in the set \(F\) is a Hurwitz-stable polynomial” (P:177).  
**Registration:** “A polynomial set F is robustly stable iff every member is Hurwitz (Definition 2)” (R:15).

### A6. A fixed numerator and every denominator in the general basic question
**Print Chinese:** “是否存在、如何找出一个（固定的）多项式\(b(s)\)，使对\(\forall a(s)\in F\)有\(b(s)/a(s)\)是严格正实的？” (P:58). **Print English:** “does there exist, and how does one find, a (fixed) polynomial \(b(s)\), such that for \(\forall a(s)\in F\), \(b(s)/a(s)\) is strictly positive real?” (P:181).  
**Registration:** “does there always exist one fixed polynomial b(s) such that b(s)/a(s) is SPR for every a(s) in the family?” (R:17–18). The fixed/each-denominator phrases are captured; the printed basic question's wider wording is B3.

### A7. Higher-than-four stable interval-set existence question
**Print Chinese:** “对于阶次大于4的稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数族？” (E:83). **Print English:** “For a stable interval-polynomial set of order greater than4, does there actually exist a polynomial which, together with that polynomial set, can be configured into a family of strictly positive real rational functions?” (E:91).  
**Registration:** “For a robustly stable interval polynomial family of order n > 4, does there always exist one fixed polynomial b(s) …” (R:17–18). The printed order range, stable interval-family and existence wording appear; D3/D4 retain the formulation boundary.

### A8. Printed alternative question mentions necessity and sufficiency
**Print Chinese:** “或者大于4阶的区间多项式集的鲁棒稳定性是否也是其可鲁棒严格正实综合的充分必要条件？” (E:109). **Print English:** “Or is robust stability of an interval-polynomial set of order greater than4 also a necessary and sufficient condition for it to be robustly strictly positive real synthesizable?” (E:117).  
**Registration:** “is robust stability of an order-n (n > 4) interval family necessary and sufficient for robust SPR synthesizability?” (R:19–20). The same named question terms occur; R's “Equivalently” is separately D3.

### A9. Printed conjectural answer / numerical-example wording
**Print Chinese:** “从计算的大量数值例子来看……尚未发现反例，因此，我们推测该问题可能会有正面肯定的答案” (P:116). **Print English:** “Judging from the large number of numerical examples computed … no counterexample has yet been found; therefore, we conjecture that this problem may have a positively affirmative answer” (P:233).  
**Registration:** “The authors conjecture yes (no counterexample in their numerical examples)” (R:20). This is a comparison of printed/registered wording only, not an independent status or numerical verification.

### A10. Printed necessity wording
**Print Chinese:** “多项式集\(F\)的鲁棒稳定性是……\(b(s)/a(s)\)严格正实的必要条件” (P:60). **Print English:** “robust stability of the polynomial set \(F\) is a necessary condition for the existence of a (fixed) polynomial \(b(s)\) …” (P:183).  
**Registration:** “Necessity is immediate; the open part is sufficiency” (R:21). The word “necessity” is present in both; the additional registration wording is C7/D7, not proved here.

# B. Printed content absent as such from the registration

### B1. Preliminary numerator order \(m\)
**Print Chinese:** “在下述定义中，\(b(s)\in P^m\)，\(a(s)\in P^n\)，\(p(s)=b(s)/a(s)\)是有理函数” (P:50). **Print English:** “In the definitions below, \(b(s)\in P^m\), \(a(s)\in P^n\), and \(p(s)=b(s)/a(s)\) is a rational function” (P:173).  
**Registration:** “For b ∈ P^n and a ∈ H^n … (Definition 1)” (R:13–15). The earlier **P^m** clause is not quoted in R. It is NOT reconciled with the separately printed P^n definition.

### B2. Explicit root clause in the definition of \(H^n\)
**Print Chinese:** “Hurwitz稳定多项式（仅具负实部的根）集合” (E:135). **Print English:** “Hurwitz-stable polynomials (having only roots with negative real parts)” (E:143).  
**Registration:** “H^n ⊂ P^n the Hurwitz ones” (R:13). R does not reproduce the parenthetical root clause; no inference about its meaning is made here.

### B3. General basic question's full frame and “how to find”
**Print Chinese:** “给定一个\(n\)阶多项式集\(F\)，是否存在、如何找出一个（固定的）多项式\(b(s)\)……” (P:58). **Print English:** “Given an nth-order polynomial set \(F\), does there exist, and how does one find, a (fixed) polynomial \(b(s)\) …?” (P:181).  
**Registration:** “For a robustly stable interval polynomial family of order n > 4, does there always exist …” (R:17–18). The separately printed general F frame and express “how does one find” question are not fully quoted in that R question.

### B4. Separate robust-SPR-region characterization question
**Print Chinese:** “给定\(a(s)\in H^n\)，如何找出所有的\(b(s)\)，使\(p(s)=b(s)/a(s)\in\mathrm{SPR}\)？” (P:64). **Print English:** “Given \(a(s)\in H^n\), how does one find all \(b(s)\) such that \(p(s)=b(s)/a(s)\in\mathrm{SPR}\)?” (P:187).  
**Registration:** “Question. For a robustly stable interval polynomial family …” (R:17–20). R does not separately quote the all-numerators region question.

### B5. Explicit coefficient-expression question
**Print Chinese:** “给出\(b(s)\)的基于\(a(s)\)的系数的显式表达条件是文献[4]提出的一个问题” (P:70). **Print English:** “giving explicit expression conditions for \(b(s)\) based on the coefficients of \(a(s)\) is a problem raised in reference[4]” (P:191).  
**Registration:** “one fixed polynomial b(s)” (R:18); no corresponding explicit-expression question/reference[4] is quoted.

### B6. Real-root and Sturm wording
**Print Chinese:** “传递函数严格正实性的判定，本质上可以化为多项式实根的判定问题” and “古典Sturm组方法……对文字（符号）系数的多项式建立判别系统是没有效率的[5]” (P:72,74). **Print English:** “can essentially be reduced to the determination of real roots of polynomials” and “the classical Sturm-group method … is not efficient … with literal (symbolic) coefficients[5]” (P:193,195).  
**Registration:** “SPR means strict positivity of Re(b/a) at every real ω” (R:26–27). The two printed real-root/Sturm sentences are not present as such.

### B7. Complete discrimination-system statements
**Print Chinese:** “1996年，由杨路等建立的多项式完全判别系统……” and “文献[6]借此给出了传递函数鲁棒严格正实域的描述……” (P:76,78). **Print English:** “the complete polynomial discrimination system established by Yang Lu and others” and “Reference[6] used this to give a description …” (P:197,199).  
**Registration:** “Formalization used here. Following the authors' own papers …” (R:23–24). These printed [5]/[6] descriptions are not reproduced in R.

### B8. Three named polynomial-set families
**Print Chinese:** “稳定的多项式线段集、或稳定的区间多项式集、或稳定的凸多面体多项式集” (P:80). **Print English:** “a stable polynomial-segment set, or a stable interval-polynomial set, or a stable convex-polytope polynomial set” (P:201).  
**Registration:** “an interval family is a monic box of closed coefficient intervals” (R:25). The segment/polytope alternatives are not separately listed in R.

### B9. Even/odd-term historical statement
**Print Chinese:** “当\(F\)的元具有相同的偶次（或奇次）项时，这样的多项式\(b(s)\)是存在的[3,4,7]” (P:84). **Print English:** “When the elements of \(F\) have identical even-degree (or odd-degree) terms, such a polynomial \(b(s)\) exists[3,4,7]” (P:205).  
**Registration:** “one common real numerator … for EVERY member” (R:33). R does not quote that even/odd-term condition or its printed citations.

### B10. Printed low-order \(n\leq3\) sentence
**Print Chinese:** “当\(F\)为低阶的（\(n\leqslant3\)）稳定的区间多项式集时[3,4,7]，这样的多项式\(b(s)\)是存在的” (E:161). **Print English:** “When \(F\) is a stable interval-polynomial set of low order (\(n\leqslant3\))[3,4,7], such a polynomial \(b(s)\) exists” (E:169).  
**Registration:** “Slot specialization … n=7” (R:33). The printed n≤3 statement is not reproduced there.

### B11. Anderson/Betser–Zeheb history and formula references
**Print Chinese:** “Anderson等[9]……给出了使上述问题存在解的一组条件[即文献[9]中的式（58）～式（60）]” (corrected E:187); “1993年，Betser和Zeheb举出反例说明，文献[9]中给出的仅是一个充分性的条件” (P:90). **Print English:** “Anderson and others[9] … [namely formulas(58) through(60) in reference[9]]” (E:195); “Betser and Zeheb gave a counterexample showing … only a sufficient condition” (P:211).  
**Registration:** “For a robustly stable interval polynomial family of order n > 4 …” (R:17–20). These named historical clauses/formula numbers are not present in that target text.

### B12. Printed fourth-order historical question
**Print Chinese:** “即使对于4次稳定的区间多项式集，究竟是否存在一个多项式，使其与该多项式集合配置成严格正实的有理函数族？” (E:57). **Print English:** “even for fourth-degree stable interval-polynomial sets, did there actually exist a polynomial … configured into a family of strictly positive real rational functions?” (E:65).  
**Registration:** “order n > 4” (R:17) and “n=7” (R:33). The printed fourth-order question is not separately stated.

### B13. Printed historical lack-of-proof/counterexample wording and later reference
**Print Chinese:** “理论上不能正面证明这一结论……也从未发现有反例……” (P:94); “文献[10]……给出了4次区间稳定多项式集……正面肯定的答案” (P:96). **Print English:** “this conclusion could not be positively proved … no counterexample … had ever been found” (P:215); “reference[10] … gave a positively affirmative answer … fourth-degree” (P:217).  
**Registration:** “The authors conjecture yes (no counterexample in their numerical examples)” (R:20). R does not reproduce this separate historical fourth-order narrative. No current-status inference is drawn.

### B14. Arbitrary-order segment and \(n\leq4\) interval wording
**Print Chinese:** “任意阶多项式线段或低阶（\(n\leqslant4\)）区间多项式的鲁棒稳定性，是实现其鲁棒严格正实综合的充分必要条件” (P:98). **Print English:** “robust stability of polynomial segments of arbitrary order or low-order (\(n\leqslant4\)) interval polynomials is a necessary and sufficient condition …” (P:219).  
**Registration:** “order n > 4” and “n=7” (R:17,33). The printed segment/low-order statement is not quoted in R.

### B15. Continuous/discrete/D-SPR wording
**Print Chinese:** “针对连续时间系统……可以直接推广到离散时间系统、甚至D-SPR的情形[3]” (P:100). **Print English:** “concern continuous-time systems … extended directly to discrete-time systems, and even to the D-SPR situation[3]” (P:221).  
**Registration:** “SPR means strict positivity of Re(b/a) at every real ω” (R:26–27). The printed continuous/discrete/D-SPR sentence is absent as such.

### B16. Distinction from convex-polytope sets
**Print Chinese:** “多项式线段和区间多项式……与凸多面体多项式集……有内在的本质不同” (P:102). **Print English:** “an inherent essential difference between … polynomial segments and interval polynomials and … convex-polytope polynomial sets” (P:223).  
**Registration:** “an interval family is a monic box of closed coefficient intervals” (R:25). R does not quote this printed contrast.

### B17. Introductory context, uncertainty and earlier analysis
**Print Chinese:** “传递函数的严格正实性……在绝对稳定性与超稳定性理论、二次优化控制及自适应系统理论等领域中起着十分重要的作用” (P:32); “因实际系统中总存在有不确定性……” (P:34); “文献[1]、[2]……‘八顶点检验定理’” (P:38). **Print English:** “strict positive realness … plays a very important role … absolute stability and hyperstability …” (P:155); “uncertainty always exists” (P:157); “eight-vertex test theorem” (P:161).  
**Registration:** “Problem as posed (book p. 682)” (R:11). These contextual statements and [1]/[2] wording are not reproduced in R.

### B18. LMI explanation and definition-variation context
**Print Chinese:** “对鲁棒严格正实综合问题，通过正实引理……基于矩阵不等式的正实性条件[3]” (E:17); “不同的文献采用了稍有不同的定义[3]” (P:44). **Print English:** “through the positive-real lemma … matrix-inequality-based positive-realness conditions” (E:25); “different references have adopted slightly different definitions[3]” (P:167).  
**Registration:** “Formalization used here …” (R:23). Those printed explanatory sentences are not quoted in the registration.

### B19. Printed references [1]–[5]
**Print:** “参考文献” (P:118; English “References,” P:235). Printed entries include “On robust nonlinear stability of interval control systems” [1] (P:120/237); “区间有理函数严格正实性的有限检验” [2] / “A finite test of strict positive realness of interval rational functions” (P:122/239); “系统鲁棒严格正实综合与鲁棒稳定性分析” [3] / “System robust strictly positive real synthesis and robust-stability analysis” (P:124/241); “Robust analysis of strictly positive real function set” [4] (P:126/243); “非线性代数方程组与机器证明” [5] / “Nonlinear algebraic equation systems and machine proof” (P:128/245). English-language titles [1]/[4] are printed in English; a non-existent Chinese title is not supplied here.  
**Registration:** “Following the authors' own papers (Wang & Yu, ACC 2001, arXiv:math/0202242 …)” (R:23–24). The printed [1]–[5] list is not reproduced in R.

### B20. Printed references [6]–[10]
**Print:** “Complete characterization of strictly positive real regions and robust strictly positive real synthesis method” [6] (P:130/247); “Designing strictly positive real transfer function families…” [7] (P:132/249); “Classification of units in \(H_\infty\) and an alternative proof of Kharitonov’s theorem” [8] (P:134/251); “Robust strict positive realness:Character-ization and construction” [9] (P:136–137/253–254); “Anderson’s claim on fourth-order SPR synthesis is true” [10] (P:139/256). These titles are printed in English; the English rendering repeats them, so no printed Chinese counterpart is invented.  
**Registration:** “Wang & Yu, ACC 2001, arXiv:math/0202242” (R:23–24). R does not reproduce the full printed [6]–[10] list; no identification/equivalence between its source reference and any numbered entry is asserted.

### B21. Contributor affiliations
**Print Chinese:** “1　华东师范大学软件学院” and “2　北京大学工学院” (P:143,145). **Print English:** “School of Software, East China Normal University” and “College of Engineering, Peking University” (P:260,262).  
**Registration:** “郁文生 (Yu Wensheng), 王龙 (Wang Long)” (R:7). R names the contributors but does not quote the two printed affiliations.

### B22. Printed definition-variation and challenge wording
**Print Chinese:** “不同的文献采用了稍有不同的定义[3]” (P:44); “如下区间系统的鲁棒严格正实综合问题仍是理论上尚未解决的具有挑战性的公开问题[3,4,7,9]” (P:110). **Print English:** “different references have adopted slightly different definitions[3]” (P:167); “remains a challenging open problem not yet solved theoretically[3,4,7,9]” (P:227).  
**Registration:** “The authors conjecture yes … Necessity is immediate; the open part is sufficiency” (R:20–21). The printed definition-variation clause and full cited challenge sentence are not reproduced verbatim; no current-open/closed status is assessed.

# C. Registered restrictions, conventions and added wording not printed as such

### C1. Single registered order and exact counterexample alternative
**Print Chinese:** “对于阶次大于4的稳定的区间多项式集……” (E:83). **Print English:** “For a stable interval-polynomial set of order greater than4 …” (E:91).  
**Registration:** “Slot specialization … n=7 … or one genuine robustly Hurwitz monic septic box with no such numerator” (R:33). The explicit single-order specialization and this counterexample-object formulation are not printed as those words in the entry. No equivalence/inequivalence is argued.

### C2. Monic coefficient-box representation
**Print Chinese:** “稳定的区间多项式集” (E:83). **Print English:** “a stable interval-polynomial set” (E:91).  
**Registration:** “K = {s^n + Σ a_i s^{n−i}, a_i ∈ [a_i^−, a_i^+]} … an interval family is a **monic** box of closed coefficient intervals” (R:24–25). The printed main question does not display this monic coefficient-box formula. R itself states “The book text itself does not say ‘monic’” (R:27).

### C3. Closed/degenerate interval convention
**Print Chinese:** “区间多项式集” (E:83). **Print English:** “interval-polynomial set” (E:91).  
**Registration:** “closed coefficient intervals (degenerate intervals allowed)” (R:25–26). Those explicit conventions are not spelled out in the printed question quotation.

### C4. Exact-degree and common real numerator phrasing
**Print Chinese:** “\(b(s)\in P^n\)” (P:52) and “存在一个多项式” (E:83). **Print English:** “\(b(s)\in P^n\)” (P:175) and “there actually exist a polynomial” (E:91).  
**Registration:** “the numerator has **exact degree n**” (R:26), and “one common real numerator of EXACT degree seven” (R:33). The literal words “exact degree”/“degree seven” are explicit in R, not in those printed quotations; the relationship to P^n is D2.

### C5. Explicit finite-frequency/zero wording
**Print Chinese:** “对\(\forall\omega\in\mathbf R\)，\(\operatorname{Re}[p(j\omega)]>0\)” (P:52). **Print English:** “for \(\forall\omega\in\mathbf R\), \(\operatorname{Re}[p(j\omega)]>0\)” (P:175).  
**Registration:** “at EVERY finite real w including zero, for EVERY member” (R:33). The words “finite … including zero” are explicit in R, not spelled out in the printed clause. No frequency-domain equivalence proof is supplied here.

### C6. Leading-coefficient variant and external outcome label
**Print Chinese:** “稳定的区间多项式集” (E:83). **Print English:** “a stable interval-polynomial set” (E:91).  
**Registration:** “boxes with an uncertain leading coefficient are treated as a separately labelled variant (Prop. E in [`work/theory.md`](work/theory.md), outcome O6)” (R:28–29). That variant label/path/outcome is not printed in the supplied entry; the linked file was NOT opened.

### C7. “Immediate” necessity and singled-out remaining part
**Print Chinese:** “鲁棒稳定性是……严格正实的必要条件” (P:60), and the printed alternative asks “是否也是……充分必要条件？” (E:109). **Print English:** “robust stability … is a necessary condition” (P:183), and “is … also a necessary and sufficient condition?” (E:117).  
**Registration:** “Necessity is immediate; the open part is sufficiency” (R:21). The exact “immediate/open part” formulation is R wording; this audit does not establish it by an argument or make a current-status judgment.

### C8. External formalization provenance / later announcements
**Print Chinese:** the entry's numbered source list includes [6] “Wang L, Yu W S. Complete characterization …” and [10] “Yu W S, Wang L. Anderson’s claim …” (P:130,139; printed in English). **Print English:** the same printed entries are repeated at P:247,256.  
**Registration:** “Following the authors' own papers (Wang & Yu, ACC 2001, arXiv:math/0202242 …) and the 2026 announcements for n = 5, 6” (R:23–25). That exact named provenance and 2026-announcement wording is absent from the printed entry; no identification of cited works is attempted.

### C9. Truncated “fully solved means” registration line
**Print Chinese:** “究竟是否存在一个多项式……” and “或者……是否也是……充分必要条件？” (E:83,109). **Print English:** “does there actually exist a polynomial …?” and “Or is … a necessary and sufficient condition …?” (E:91,117).  
**Registration:** “**Fully solved means:** for every n ≥ 5, either a proof that every robustly Hurwitz monic box of” (R:31). The supplied line ENDS there. Its unfinished continuation is not supplied; this audit does not infer what the missing alternative or remaining words say.

# D. Wording whose equivalence to the print is **EQUIVALENCE_NOT_ESTABLISHED**

No mathematical argument is offered in this section. These are comparisons requiring a separate authorized semantic/equivalence gate, not findings that the two statements are necessarily equivalent or inequivalent.

### D1. Printed “order greater than4” versus registered n=7 / n≥5
**Print Chinese:** “阶次大于4” (E:83). **Print English:** “order greater than4” (E:91).  
**Registration:** “order n > 4” (R:17), “for every n ≥ 5” (R:31, incomplete), and separately “n=7” (R:33). **EQUIVALENCE_NOT_ESTABLISHED** for the full printed question versus the single-slot specialization or unfinished “fully solved” line.

### D2. Printed \(b(s)\in P^n\) versus “exact degree”
**Print Chinese:** “记\(P^n\)为\(n\)阶实系数多项式集合” (P:48, corrected E:135) and “\(b(s)\in P^n\)” (P:52). **Print English:** “the set of nth-order real-coefficient polynomials” (E:143) and “\(b(s)\in P^n\)” (P:175).  
**Registration:** “numerator has exact degree n” (R:26), “EXACT degree seven” (R:33). **EQUIVALENCE_NOT_ESTABLISHED**; the earlier P^m wording at P:50 is preserved separately in B1.

### D3. Printed family formulation versus registered “Equivalently”
**Print Chinese:** “存在一个多项式，使其与该多项式集合配置成严格正实的有理函数族？” (E:83); “或者……是否也是其可鲁棒严格正实综合的充分必要条件？” (E:109). **Print English:** “exist a polynomial … configured into a family of strictly positive real rational functions?” (E:91); “Or is … a necessary and sufficient condition …?” (E:117).  
**Registration:** “one fixed polynomial b(s) such that b(s)/a(s) is SPR for every a(s) in the family? **Equivalently:** …” (R:18–20). **EQUIVALENCE_NOT_ESTABLISHED** between these displayed question formulations; no implication or quantifier conversion is argued.

### D4. Printed interval set versus monic closed box and leading-coefficient variant
**Print Chinese:** “稳定的区间多项式集” (E:83). **Print English:** “a stable interval-polynomial set” (E:91).  
**Registration:** “monic box of closed coefficient intervals (degenerate intervals allowed)” and “uncertain leading coefficient … separately labelled variant” (R:25–29). **EQUIVALENCE_NOT_ESTABLISHED** between those descriptions, including their domain boundaries.

### D5. Printed negative-real-part roots versus “strictly Hurwitz”
**Print Chinese:** “Hurwitz稳定多项式（仅具负实部的根）” (E:135). **Print English:** “Hurwitz-stable polynomials (having only roots with negative real parts)” (E:143).  
**Registration:** “every member strictly Hurwitz” (R:33). **EQUIVALENCE_NOT_ESTABLISHED** as a documentary comparison; no root or stability argument is made.

### D6. Printed every-real-frequency clause versus added words finite/zero
**Print Chinese:** “对\(\forall\omega\in\mathbf R\)，\(\operatorname{Re}[p(j\omega)]>0\)” (P:52). **Print English:** “for \(\forall\omega\in\mathbf R\), \(\operatorname{Re}[p(j\omega)]>0\)” (P:175).  
**Registration:** “strict Re(b(jw)/a(jw))>0 at EVERY finite real w including zero, for EVERY member” (R:33). **EQUIVALENCE_NOT_ESTABLISHED** beyond identifying those literal phrases; no added frequency convention is inferred from the printed text.

### D7. Printed necessity sentence plus question versus “open part is sufficiency”
**Print Chinese:** “鲁棒稳定性是……必要条件” (P:60); “是否也是……充分必要条件？” (E:109). **Print English:** “robust stability … is a necessary condition” (P:183); “is … also a necessary and sufficient condition?” (E:117).  
**Registration:** “Necessity is immediate; the open part is sufficiency” (R:21). **EQUIVALENCE_NOT_ESTABLISHED** for that reformulation; no proof or current-state inference is supplied.

### D8. Printed source references versus registration's external provenance
**Print Chinese:** “参考文献” (P:118); the numbered [10] title “Anderson’s claim on fourth-order SPR synthesis is true” is itself printed in English (P:139). **Print English:** “References” (P:235) and the same [10] title (P:256).  
**Registration:** “Wang & Yu, ACC 2001, arXiv:math/0202242” (R:23–24). **EQUIVALENCE_NOT_ESTABLISHED** as to bibliographic identity, version, formalization or any underlying results; no other source was opened.

## Counts and interpretation boundary

| Section | Grouped items |
|---|---:|
| A — printed wording captured in part/as stated | 10 |
| B — printed content absent from the registration as such | 22 |
| C — registration-only wording/conventions/restrictions | 9 |
| D — EQUIVALENCE_NOT_ESTABLISHED | 8 |

Counts refer to the explicitly numbered GROUPS, not atomic subclauses or a mathematical verdict. Overlap is intentional where one sentence has both common words and an unestablished relationship.
The **TRUNCATED: NO** flag concerns the printed three-page entry; it does NOT fill the unfinished registered line R:31.

**No mathematical reasoning, equivalence argument, proof, source-status/novelty judgment, source lookup, lane-owner/transcriber contact or computation was performed.** No registration or frozen source is edited. The SPR post-v6 STOP was read as STATUS ONLY: its entire held branch/consumers remain NONINPUT and it does not authorize any scientific route.
All S0 STOP/HOLD/ZERO, parent L1, scientific HOLDv2, N4 UNKNOWN historical child exit UNESTABLISHED, auxiliary214 STOP and the deadline persist. This audit does not admit the printed packet as a research input or modify the lane's target.

**END OF COMPLETE INFO-2 DOCUMENTARY REGISTRATION AUDIT.**
