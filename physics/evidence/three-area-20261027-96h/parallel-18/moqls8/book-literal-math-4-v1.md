# B4 — math-4 book-literal transcription

## Documentary header and source boundary

- Transcriber: **PhysicsMOQLS8-2**,slot physics-4;duty **B4**,lane math-4.
- Frozen duty: `institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/duty-B4-math-4-release-v1.json`,SHA256 **5353096bb38cf66a685184ada9c64110ac71e7df8df3880dc4bc9ef318d96565**.
- Gate: `book-literal-transcription-gate-v1.json`,SHA256 **16441f4ed6394d93360d764ac553d99983eb989fb0253075f2fe69fe2ce84d0b**;complete354LF read.
- Extraction receipt: `book-literal-extraction-receipt-v1.json`,SHA256 **19156746c835ef8d8ad6e8b29490376fc69aea32c4b7a5f2ba94b733d071a392**;complete87LF read.
- Actual PRE-IMAGE ACK: `book-literal-math-4-prebody-ack-v1.json`,SHA256 **6fbf3b2cf4a0ab10636f825c4680ce59c2a96fedeba84dc4c03183fdac1e4cf8**,24LF/4731B;native prewrite **Wed Oct 28 09:22:59 PDT 2026**,postpin **09:23:44 PDT**. It disclosed historical prior-round math-4/v145-B contact and held image access pending a prospective recipient decision;that ACK is unchanged.
- Prospective recipient qualification,read COMPLETE before either image: `institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/duty-B4-math-4-release-v1-addendum-1-recipient-disclosure.json`,SHA256 **9f8405bee940fec184bdfb63c4fd0e14d6d82ca8399b622d347c3fdd8b9f616f**. Main expressly authorized source-only transcription with the disclosed contact carried forward and third-owner documentary comparison required. This is not a clean-cognition certificate or a STOP waiver.
- Native observation AFTER the qualification read and BEFORE image viewing: **Wed Oct 28 09:24:51 PDT 2026**. Native observation BEFORE this packet write: **Wed Oct 28 09:32:08 PDT 2026**. No separate per-image wall clock was observed;none is invented.
- **TRUNCATED: NO.** The permitted second page contains the end of the entry,its five printed references,and the contributor/affiliation;the remaining page is blank.

|Permitted source image|PDF page|Printed page|Original pixel size|SHA256|
|---|---|---|---|---|
|`source-math-0082.png`|82|66|1241×1754|d70fd92ab92e65b252e7088cdb2e4f76b940c96d76a98dc79832bab073e5c127|
|`source-math-0083.png`|83|67|1241×1754|7b6ddcf090999f397e504181378d16759921438fc3f25028d9cffbec73abf70a|

Both PNG pins matched the duty before viewing. ONLY these two images were viewed;each was re-viewed for glyph/reference legibility. No PDF,OCR,text extraction,other page,web,reference source,lane proof body or quarantined CLI payload was opened. MathSemigroup-2 and all other lane owners were not contacted.

## Location key

The entry is single-column on both pages. The following VISUAL line labels are introduced only to locate the transcription;they are not printed line numbers.

- Printed p66: T1=Chinese title,T2=printed English title;B01–B17=text lines from the opening paragraph to the last prose line;F01–F07=displayed formula lines,numbered top to bottom. B01–B03 are the opening paragraph;B04–B09 the first definitions paragraph;F01–F04 the four band conditions;B10–B11 the inverse/primitive paragraph;B12–B14 the completely-simple/local-inverse/weak-E paragraph;F05 its implication;B15 the natural-order introduction;F06 its formula;B16–B17 the last definitions paragraph;F07 its implication.
- Printed p67: B01–B02=Fact1,B03–B04=Question1,B05–B06=Fact2,B07=Question2;RH=reference heading;R01–R08=the eight printed reference lines;A01–A02=contributor/affiliation. The running page header is not counted as entry text.
- Paragraph line wraps are rejoined below;wording,punctuation,order and printed mathematical content are retained. Displayed mathematics is rendered in LaTeX-style text.

## Verbatim Chinese and printed English transcription

### CN-66-T1 — printed p66,column1,title line T1

关于正则半群的两个嵌入问题

### CN-66-T2 — printed p66,column1,title line T2

Two Embedding Problems for Regular Semigroups

### CN-66-P1 — printed p66,column1,B01–B03

正则半群是半群代数理论的主流研究领域，从若干“（某种意义上）更靠近群”的正则半群（诸如逆半群，完全正则半群等）的研究入手开发正则半群的研究是当然的趋势。下面的两个问题是遵循这一趋势于2002年被提出来的。

### CN-66-P2 — printed p66,column1,B04–B09,F01–F04

令\(S\)是一半群，\(a\in S\)。称\(S\)是一幺半群，如果\(S\)含恒等元；称\(a\)是\(S\)的一个正则元，如果\(S\)的子集\(V(a)\)非空，其中，\(V(a)=\{x\in S\mid axa=a,xax=x\}\)，\(V(a)\)中的元素称为\(a\)的逆元；称\(S\)是一正则（逆）半群，如果关于任意\(a\in S\)，\(V(a)\)非空（\(V(a)\)是一单元集）。\(S\)的所有幂等元形成的子集用\(E(S)\)表示。称\(E(S)\)是一带，如果\(E(S)\)是\(S\)的一个子半群；称\(S\)是一纯正半群，如果\(E(S)\)是一带；称带\(E(S)\)是一半格（交换带）、正则带、正规带、半正规带，如果它们分别满足

\[
\forall e,f\in E(S),\quad ef=fe;
\]
\[
\forall e,f,g\in E(S),\quad efege=efge;
\]
\[
\forall e,f,g\in E(S),\quad efge=egfe;
\]
\[
\forall e\in E(S),\quad eE(S)e\text{ 是正则带}.
\]

### CN-66-P3 — printed p66,column1,B10–B11

众所周知，逆半群恰是\(E(S)\)为半格的半群，因此逆半群是纯正的；称\(S\)的非零幂等元\(f\)是本原的，如果关于任意非零幂等元\(e\)，\(ef=fe=e\rightarrow e=f\)。

### CN-66-P4 — printed p66,column1,B12–B14,F05

一正则半群称为完全单的，如果它不含真理想，而且含一本原幂等元；称半群\(S\)是局部逆的，如果关于任意幂等元\(e\)，\(eSe\)是逆子半群；称正则半群\(S\)是弱\(E\)-酉的，如果

\[
\forall e\in E(S),\quad\forall a\in S,\quad e\leqslant a\rightarrow a\in E(S).
\]

### CN-66-P5 — printed p66,column1,B15,F06

其中，“\(\leqslant\)”是正则半群\(S\)上的自然偏序，定义如下：关于任意\(a,b\in S\)，

\[
a\leqslant b\leftrightarrow\exists e,f\in E(S),\quad a=eb=bf.
\]

### CN-66-P6 — printed p66,column1,B16–B17,F07

称一正则半群\(S\)是局部\(r\)-纯正的，如果关于任意\(e\in E(S)\)，\(eSe\)是以\(E(eSe)\)为正则带的纯正（幺）半群。称半群\(S\)到半群\(T\)的同态\(\phi\)是幂等元分离的，如果

\[
\forall e,f\in E(S),\quad\phi(e)=\phi(f)\rightarrow e=f.
\]

### CN-67-F1 — printed p67,column1,B01–B02

**事实\(1^{[1,2]}\)**　每一弱\(E\)-酉局部逆半群可嵌入一“正规带经由完全单半群”的半直积。

### CN-67-Q1 — printed p67,column1,B03–B04

**问题\(1^{[2]}\)**　是否每一弱\(E\)-酉局部\(r\)-纯正半群可嵌入一“半正规带经由完全单半群”的半直积？

### CN-67-F2 — printed p67,column1,B05–B06

**事实\(2^{[2\sim5]}\)**　每一逆半群可嵌入一“半格经由群”的半直积的幂等元分离同态像。

### CN-67-Q2 — printed p67,column1,B07

**问题\(2^{[2]}\)**　推广事实2到正则半群的一个尽量大的子类中。

### CN-67-RH — printed p67,column1,RH

参考文献

### CN-67-R1 — printed p67,column1,R01

[1] Billhardt B, Hsieh S C. Weakly E-Unitary locally inverse semigroups. preprint

### CN-67-R2 — printed p67,column1,R02–R03

[2] M B Szendrei. Some open problems in the structure theory of regular semigroups. Semigroup Forum, 2002, 64: 213-223

### CN-67-R3 — printed p67,column1,R04–R05

[3] McAlister D B. Groups, semilattice and inverse semigroups. Trans Amer Math Soc, 1974, 192: 227-244

### CN-67-R4 — printed p67,column1,R06

[4] Lawson M V. Almost factorisable inverse semigroups. Glasgow Math J, 1994, 36: 97-111

### CN-67-R5 — printed p67,column1,R07–R08

[5] Lawson M V. Inverse Semigroups: The Theory of Partial Symmetries. Singapore: World Scientific, 1998

### CN-67-A — printed p67,column1,A01–A02,lower-right contributor block

撰稿人：郭聿琦

西南大学

## Sentence-aligned literal English rendering

Sentence numbers below follow the printed Chinese full stops/question mark within each CN block;semicolons are retained within their printed sentence. The printed English reference entries are unchanged,not bibliographically corrected.

### EN-66-T1 / EN-66-T2 — aligned to CN-66-T1 / CN-66-T2

Two Embedding Problems for Regular Semigroups

The printed English title is: Two Embedding Problems for Regular Semigroups

### EN-66-P1-S1 — aligned to CN-66-P1,sentence1

Regular semigroups are the mainstream research field of semigroup algebra theory;it is a natural trend to develop the study of regular semigroups by starting from the study of some regular semigroups that are “closer to groups (in some sense)” (such as inverse semigroups,completely regular semigroups,and so on).

### EN-66-P1-S2 — aligned to CN-66-P1,sentence2

The following two problems were put forward in2002 following this trend.

### EN-66-P2-S1 — aligned to CN-66-P2,sentence1

Let \(S\) be a semigroup,and \(a\in S\).

### EN-66-P2-S2 — aligned to CN-66-P2,sentence2

\(S\) is called a monoid if \(S\) contains an identity element;\(a\) is called a regular element of \(S\) if the subset \(V(a)\) of \(S\) is nonempty,where \(V(a)=\{x\in S\mid axa=a,xax=x\}\),and the elements in \(V(a)\) are called inverses of \(a\);\(S\) is called a regular (inverse) semigroup if,for any \(a\in S\),\(V(a)\) is nonempty (\(V(a)\) is a singleton).

### EN-66-P2-S3 — aligned to CN-66-P2,sentence3

The subset formed by all idempotents of \(S\) is denoted by \(E(S)\).

### EN-66-P2-S4 — aligned to CN-66-P2,sentence4 and F01–F04

\(E(S)\) is called a band if \(E(S)\) is a subsemigroup of \(S\);\(S\) is called an orthodox semigroup if \(E(S)\) is a band;the band \(E(S)\) is called a semilattice (commutative band),a regular band,a normal band,and a seminormal band if they respectively satisfy

\[
\forall e,f\in E(S),\quad ef=fe;
\]
\[
\forall e,f,g\in E(S),\quad efege=efge;
\]
\[
\forall e,f,g\in E(S),\quad efge=egfe;
\]
\[
\forall e\in E(S),\quad eE(S)e\text{ is a regular band}.
\]

### EN-66-P3-S1 — aligned to CN-66-P3

As is well known,inverse semigroups are precisely the semigroups for which \(E(S)\) is a semilattice,and therefore inverse semigroups are orthodox;a nonzero idempotent \(f\) of \(S\) is called primitive if,for any nonzero idempotent \(e\),\(ef=fe=e\rightarrow e=f\).

### EN-66-P4-S1 — aligned to CN-66-P4 and F05

A regular semigroup is called completely simple if it contains no proper ideal and contains a primitive idempotent;a semigroup \(S\) is called locally inverse if,for any idempotent \(e\),\(eSe\) is an inverse subsemigroup;a regular semigroup \(S\) is called weakly \(E\)-unitary if

\[
\forall e\in E(S),\quad\forall a\in S,\quad e\leqslant a\rightarrow a\in E(S).
\]

### EN-66-P5-S1 — aligned to CN-66-P5 and F06

Here,“\(\leqslant\)” is the natural partial order on the regular semigroup \(S\),defined as follows:for any \(a,b\in S\),

\[
a\leqslant b\leftrightarrow\exists e,f\in E(S),\quad a=eb=bf.
\]

### EN-66-P6-S1 — aligned to CN-66-P6,sentence1

A regular semigroup \(S\) is called locally \(r\)-orthodox if,for any \(e\in E(S)\),\(eSe\) is an orthodox (monoid) semigroup whose \(E(eSe)\) is a regular band.

### EN-66-P6-S2 — aligned to CN-66-P6,sentence2 and F07

A homomorphism \(\phi\) from a semigroup \(S\) to a semigroup \(T\) is called idempotent-separating if

\[
\forall e,f\in E(S),\quad\phi(e)=\phi(f)\rightarrow e=f.
\]

### EN-67-F1-S1 — aligned to CN-67-F1

**Fact\(1^{[1,2]}\).** Every weakly \(E\)-unitary locally inverse semigroup can be embedded into a semidirect product of “a normal band via a completely simple semigroup”.

### EN-67-Q1-S1 — aligned to CN-67-Q1

**Question\(1^{[2]}\).** Can every weakly \(E\)-unitary locally \(r\)-orthodox semigroup be embedded into a semidirect product of “a seminormal band via a completely simple semigroup”?

### EN-67-F2-S1 — aligned to CN-67-F2

**Fact\(2^{[2\sim5]}\).** Every inverse semigroup can be embedded into an idempotent-separating homomorphic image of a semidirect product of “a semilattice via a group”.

### EN-67-Q2-S1 — aligned to CN-67-Q2

**Question\(2^{[2]}\).** Extend Fact2 to a subclass of regular semigroups as large as possible.

### EN-67-RH and EN-67-R1–R5 — aligned to CN-67-RH and CN-67-R1–R5

参考文献 → References.

[1] Billhardt B, Hsieh S C. Weakly E-Unitary locally inverse semigroups. preprint

[2] M B Szendrei. Some open problems in the structure theory of regular semigroups. Semigroup Forum, 2002, 64: 213-223

[3] McAlister D B. Groups, semilattice and inverse semigroups. Trans Amer Math Soc, 1974, 192: 227-244

[4] Lawson M V. Almost factorisable inverse semigroups. Glasgow Math J, 1994, 36: 97-111

[5] Lawson M V. Inverse Semigroups: The Theory of Partial Symmetries. Singapore: World Scientific, 1998

### EN-67-A — aligned to CN-67-A

Contributor: 郭聿琦

Southwest University

## Printed-definition inventory — quotations only

The following entries quote the printed definitions/clauses;the locators refer to the verbatim blocks above. No extra definition or equivalence is supplied.

|ID|Printed item|Exact printed quotation/formula|Locator|
|---|---|---|---|
|D01|Initial semigroup and element|“令\(S\)是一半群，\(a\in S\)。”|CN-66-P2,B04|
|D02|Monoid|“称\(S\)是一幺半群，如果\(S\)含恒等元”|CN-66-P2,B04|
|D03|Regular element|“称\(a\)是\(S\)的一个正则元，如果\(S\)的子集\(V(a)\)非空”|CN-66-P2,B04–B05|
|D04|\(V(a)\)|\(V(a)=\{x\in S\mid axa=a,xax=x\}\)|CN-66-P2,B05|
|D05|Inverse of an element|“\(V(a)\)中的元素称为\(a\)的逆元”|CN-66-P2,B05–B06|
|D06|Regular/inverse semigroup|“称\(S\)是一正则（逆）半群，如果关于任意\(a\in S\)，\(V(a)\)非空（\(V(a)\)是一单元集）。”|CN-66-P2,B06–B07|
|D07|\(E(S)\)|“\(S\)的所有幂等元形成的子集用\(E(S)\)表示。”|CN-66-P2,B07|
|D08|Band|“称\(E(S)\)是一带，如果\(E(S)\)是\(S\)的一个子半群”|CN-66-P2,B07–B08|
|D09|Orthodox semigroup|“称\(S\)是一纯正半群，如果\(E(S)\)是一带”|CN-66-P2,B08|
|D10|Ordered list of band names|“一半格（交换带）、正则带、正规带、半正规带，如果它们分别满足”|CN-66-P2,B09|
|D11|First printed band condition|\(\forall e,f\in E(S),\ ef=fe\)|CN-66-P2,F01|
|D12|Second printed band condition|\(\forall e,f,g\in E(S),\ efege=efge\)|CN-66-P2,F02|
|D13|Third printed band condition|\(\forall e,f,g\in E(S),\ efge=egfe\)|CN-66-P2,F03|
|D14|Fourth printed band condition|“\(\forall e\in E(S),\ eE(S)e\)是正则带。”|CN-66-P2,F04|
|D15|Printed inverse-semigroup sentence|“逆半群恰是\(E(S)\)为半格的半群，因此逆半群是纯正的”|CN-66-P3,B10|
|D16|Primitive idempotent|“称\(S\)的非零幂等元\(f\)是本原的，如果关于任意非零幂等元\(e\)，\(ef=fe=e\rightarrow e=f\)。”|CN-66-P3,B10–B11|
|D17|Completely simple|“一正则半群称为完全单的，如果它不含真理想，而且含一本原幂等元”|CN-66-P4,B12|
|D18|Locally inverse|“称半群\(S\)是局部逆的，如果关于任意幂等元\(e\)，\(eSe\)是逆子半群”|CN-66-P4,B12–B13|
|D19|Weakly \(E\)-unitary|“称正则半群\(S\)是弱\(E\)-酉的，如果”及\(\forall e\in E(S),\ \forall a\in S,\ e\leqslant a\rightarrow a\in E(S)\)|CN-66-P4,B13–B14,F05|
|D20|Natural partial order|“其中，‘\(\leqslant\)’是正则半群\(S\)上的自然偏序，定义如下：关于任意\(a,b\in S\)，”及\(a\leqslant b\leftrightarrow\exists e,f\in E(S),\ a=eb=bf\)|CN-66-P5,B15,F06|
|D21|Locally \(r\)-orthodox|“称一正则半群\(S\)是局部\(r\)-纯正的，如果关于任意\(e\in E(S)\)，\(eSe\)是以\(E(eSe)\)为正则带的纯正（幺）半群。”|CN-66-P6,B16–B17|
|D22|Idempotent-separating homomorphism|“称半群\(S\)到半群\(T\)的同态\(\phi\)是幂等元分离的，如果”及\(\forall e,f\in E(S),\ \phi(e)=\phi(f)\rightarrow e=f\)|CN-66-P6,B17,F07|

## Printed-symbol,parameter and quantifier inventory

|Printed material|Exact occurrence/quotation|Locator|
|---|---|---|
|\(S,a\)|“\(S\)是一半群，\(a\in S\)”|CN-66-P2|
|\(x,V(a),\{\ \},\in,\mid\)|\(V(a)=\{x\in S\mid axa=a,xax=x\}\)|CN-66-P2|
|Products \(axa,xax\) and equality|\(axa=a,xax=x\)|CN-66-P2|
|“任意” for regular/inverse clause|“关于任意\(a\in S\)”|CN-66-P2|
|\(E(S)\)|“所有幂等元形成的子集”|CN-66-P2|
|\(e,f,\forall\)|\(\forall e,f\in E(S),\ ef=fe\)|CN-66-P2,F01|
|\(g\) and products \(efege,efge\)|\(\forall e,f,g\in E(S),\ efege=efge\)|CN-66-P2,F02|
|Product \(egfe\)|\(\forall e,f,g\in E(S),\ efge=egfe\)|CN-66-P2,F03|
|\(eE(S)e\)|\(\forall e\in E(S),\ eE(S)e\)|CN-66-P2,F04|
|Nonzero qualifications|“非零幂等元\(f\)”；“任意非零幂等元\(e\)”|CN-66-P3|
|\(\rightarrow\),products \(ef,fe\)|\(ef=fe=e\rightarrow e=f\)|CN-66-P3|
|\(eSe\)|“关于任意幂等元\(e\)，\(eSe\)是逆子半群”|CN-66-P4|
|\(E\) in printed name|“弱\(E\)-酉”|CN-66-P4;CN-67-F1,Q1|
|\(\forall e\in E(S),\forall a\in S\)|\(\forall e\in E(S),\ \forall a\in S,\ e\leqslant a\rightarrow a\in E(S)\)|CN-66-P4,F05|
|\(\leqslant\)|“自然偏序”及\(e\leqslant a\)、\(a\leqslant b\)|CN-66-P4,P5|
|\(b,\leftrightarrow,\exists\)|“关于任意\(a,b\in S\)”及\(a\leqslant b\leftrightarrow\exists e,f\in E(S)\)|CN-66-P5|
|Products \(eb,bf\)|\(a=eb=bf\)|CN-66-P5,F06|
|\(r\) in printed name|“局部\(r\)-纯正”|CN-66-P6;CN-67-Q1|
|\(E(eSe)\)|“以\(E(eSe)\)为正则带”|CN-66-P6|
|\(T,\phi\)|“半群\(S\)到半群\(T\)的同态\(\phi\)”|CN-66-P6|
|Images \(\phi(e),\phi(f)\)|\(\phi(e)=\phi(f)\rightarrow e=f\)|CN-66-P6,F07|
|“每一” in Fact1|“每一弱\(E\)-酉局部逆半群”|CN-67-F1|
|“是否每一” in Question1|“是否每一弱\(E\)-酉局部\(r\)-纯正半群”|CN-67-Q1|
|“每一” in Fact2|“每一逆半群”|CN-67-F2|
|Question2 qualifier|“一个尽量大的子类”|CN-67-Q2|
|Printed date in prose|“于2002年被提出来的”|CN-66-P1|
|Fact/question/citation numbers|“事实1”\(^{[1,2]}\)；“问题1”\(^{[2]}\)；“事实2”\(^{[2\sim5]}\)；“问题2”\(^{[2]}\)|CN-67-F1,Q1,F2,Q2|
|Printed bibliography numbers|[1]–[5]；2002,64:213-223；1974,192:227-244；1994,36:97-111；1998|CN-67-R1–R5|

## Printed stated facts and questions — exact quotation inventory

- **Fact1:**“每一弱\(E\)-酉局部逆半群可嵌入一‘正规带经由完全单半群’的半直积。” [CN-67-F1]
- **Question1:**“是否每一弱\(E\)-酉局部\(r\)-纯正半群可嵌入一‘半正规带经由完全单半群’的半直积？” [CN-67-Q1]
- **Fact2:**“每一逆半群可嵌入一‘半格经由群’的半直积的幂等元分离同态像。” [CN-67-F2]
- **Question2:**“推广事实2到正则半群的一个尽量大的子类中。” [CN-67-Q2]

## Glyph and literal-ambiguity record

- **Illegible/uncertain glyphs:**none identified after viewing and re-viewing ONLY the two permitted images. The opening paragraph is transcribed as printed with“开发” and“当然”;reference[3] is transcribed with singular“semilattice”. No external reference was used to alter these strings.
- **AMBIGUOUS — retained,not resolved:**“正规带经由完全单半群” [p67,column1,B01–B02];“半正规带经由完全单半群” [p67,column1,B03–B04];“半格经由群” [p67,column1,B05–B06]. The English retains“via”;no formal expansion is added.
- **AMBIGUOUS — retained,not resolved:**“一个尽量大的子类” [p67,column1,B07]. The English retains“a subclass ... as large as possible”.

## Completion and non-interpretation statement

**TRUNCATED: NO.** The complete entry is visible on PDF82–83/printed66–67,ending with references[1]–[5] and the printed contributor/affiliation on p67. No additional page was viewed or sought.

Nothing beyond literal transcription,literal sentence-aligned translation,printed-item inventory and the documentary source/position/uncertainty records was done. There is NO interpretation,reformulation,proof,solution idea,status/priority/novelty assessment,other-source consultation or contact with MathSemigroup-2/other lane owners. No research conclusion or STOP clearance is claimed. The disclosed recipient history and prospective addendum remain attached;third-owner documentary comparison is required by that addendum. This packet is not itself a lane proof input until a later separately frozen release.
