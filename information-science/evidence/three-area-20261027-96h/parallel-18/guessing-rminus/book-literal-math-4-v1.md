# B4r — literal book-entry transcription, math-4

## Source boundary and clocks

Transcriber: **InfoGuessingRminus-2**, slot info-5. Duty **B4r**, the separately frozen replacement. The held B4 output and its consumers are NONINPUT and were not opened. This packet is source-only transcription; no interpretation section is supplied.

- Frozen B4r release SHA256: `bfaf4b78151ce144f14a027c5a6c8e550b3e8f53db46eb7b2f893674a0cbadba`.
- Frozen base gate SHA256: `16441f4ed6394d93360d764ac553d99983eb989fb0253075f2fe69fe2ce84d0b`.
- Disclosure ACK: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/book-literal-math-4-prebody-ack-v1.json`, SHA256 `6a78d23d3fa0765d7158f4ddde8c1eeabdf1df3ed691adc0f2d62845e9d95cdc`, **19 LF / 3688 bytes**. Native clock before writing: **Wed Oct 28 09:39:43 PDT 2026**.
- Main explicitly gave **PROCEED** after that disclosure. The decision record was read before either image: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/duty-B4r-math-4-replacement-release-v1-disclosure-decision-v1.json`; its recorded observation is **2026-10-28T09:40:49-0700 PDT**. This is a disposition on disclosed contacts, not a clean-cognition certification.
- Native clock observed after decision and before writing this packet: **Wed Oct 28 09:41:13 PDT 2026**. Image display and a parallel metadata command occurred after the decision; the image displays' individual exact instants were not separately clocked. The metadata command returned **Wed Oct 28 09:40:56 PDT 2026**; its clock does not establish the ordering of those concurrent displays.
- Image 1: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/source-math-0082.png`, PDF page **82**, printed page **66**, SHA256 `d70fd92ab92e65b252e7088cdb2e4f76b940c96d76a98dc79832bab073e5c127`, **289795 bytes**.
- Image 2: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/source-math-0083.png`, PDF page **83**, printed page **67**, SHA256 `7b6ddcf090999f397e504181378d16759921438fc3f25028d9cffbec73abf70a`, **144070 bytes**.

Each image was displayed as a single-column page in a 1109×1568 viewer frame; the original is 1241×1754. Approximate coordinates below refer to the displayed frame, origin at upper left. Body-line identifiers B01 etc. are transcription locators counted from the first body line of each page, not printed line numbers. Formula lines, reference lines and credit lines have separate locators. Mathematical typography is encoded in LaTeX-style text. Reference superscripts and the question marks are retained.

**TRUNCATED: NO.** The entry continues from printed page 66 to the permitted page 67 and ends there with its five references and contributor/affiliation lines. The rest of page 67 is blank. No other page was opened.

## 1. Verbatim Chinese and other printed text

### Printed page 66 — PDF page 82

**[M66; running header; x≈150–805, y≈132–151]**

·66·　10000个科学难题　数学卷

**[Z01; entry title; x≈285–670, y≈263–294]**

关于正则半群的两个嵌入问题

**[Z01E; printed English title; x≈236–722, y≈318–341]**

Two Embedding Problems for Regular Semigroups

**[Z02; body B01–B03; x≈134–820, y≈393–471]**

正则半群是半群代数理论的主流研究领域, 从若干“(某种意义上) 更靠近群”的正则半群 (诸如逆半群, 完全正则半群等) 的研究入手开发正则半群的研究是当然的趋势. 下面的两个问题是遵循这一趋势于 2002 年被提出来的.

**[Z03; body B04–B09; x≈134–820, y≈479–646]**

令 $S$ 是一半群, $a\in S$. 称 $S$ 是一幺半群, 如果 $S$ 含恒等元; 称 $a$ 是 $S$ 的一个正则元, 如果 $S$ 的子集 $V(a)$ 非空, 其中, $V(a)=\{x\in S\mid axa=a,xax=x\}$, $V(a)$ 中的元素称为 $a$ 的逆元; 称 $S$ 是一正则 (逆) 半群, 如果关于任意 $a\in S$, $V(a)$ 非空 ($V(a)$ 是一单元集). $S$ 的所有幂等元形成的子集用 $E(S)$ 表示. 称 $E(S)$ 是一带, 如果 $E(S)$ 是 $S$ 的一个子半群; 称 $S$ 是一纯正半群, 如果 $E(S)$ 是一带; 称带 $E(S)$ 是一半格 (交换带)、正则带、正规带、半正规带, 如果它们分别满足

**[Z04; displayed conditions F01–F04; x≈343–645, y≈672–779]**

$$
\begin{aligned}
&\forall e,f\in E(S),\quad ef=fe;\\
&\forall e,f,g\in E(S),\quad efege=efge;\\
&\forall e,f,g\in E(S),\quad efge=egfe;\\
&\forall e\in E(S),\quad eE(S)e\ \text{是正则带}.
\end{aligned}
$$

**[Z05; body B10–B11; x≈134–820, y≈806–858]**

众所周知, 逆半群恰是 $E(S)$ 为半格的半群, 因此逆半群是纯正的; 称 $S$ 的非零幂等元 $f$ 是本原的, 如果关于任意非零幂等元 $e$, $ef=fe=e\to e=f$.

**[Z06; body B12–B14; x≈134–820, y≈866–945]**

一正则半群称为完全单的, 如果它不含真理想, 而且含一本原幂等元; 称半群 $S$ 是局部逆的, 如果关于任意幂等元 $e$, $eSe$ 是逆子半群; 称正则半群 $S$ 是弱 $E$-酉的, 如果

**[Z07; displayed condition F05; x≈304–656, y≈955–979]**

$$
\forall e\in E(S),\quad \forall a\in S,\quad e\le a\to a\in E(S).
$$

**[Z08; body B15; x≈134–720, y≈996–1021]**

其中, “$\le$” 是正则半群 $S$ 上的自然偏序, 定义如下: 关于任意 $a,b\in S$,

**[Z09; displayed condition F06; x≈325–630, y≈1047–1072]**

$$
a\le b\leftrightarrow\exists e,f\in E(S),\quad a=eb=bf.
$$

**[Z10; body B16–B17; x≈134–820, y≈1096–1148]**

称一正则半群 $S$ 是局部 $r$-纯正的, 如果关于任意 $e\in E(S)$, $eSe$ 是以 $E(eSe)$ 为正则带的纯正 (幺) 半群. 称半群 $S$ 到半群 $T$ 的同态 $\phi$ 是幂等元分离的, 如果

**[Z11; displayed condition F07; x≈324–632, y≈1174–1200]**

$$
\forall e,f\in E(S),\quad \phi(e)=\phi(f)\to e=f.
$$

### Printed page 67 — PDF page 83

**[M67; running header; x≈152–805, y≈132–151]**

关于正则半群的两个嵌入问题　·67·

**[Z12; Fact 1, body B01–B02; x≈134–820, y≈190–240]**

**事实 1**$^{[1,2]}$　每一弱 $E$-酉局部逆半群可嵌入一“正规带经由完全单半群”的半直积.

**[Z13; Question 1, body B03–B04; x≈134–820, y≈248–297]**

**问题 1**$^{[2]}$　是否每一弱 $E$-酉局部 $r$-纯正半群可嵌入一“半正规带经由完全单半群”的半直积?

**[Z14; Fact 2, body B05–B06; x≈134–820, y≈307–356]**

**事实 2**$^{[2\sim5]}$　每一逆半群可嵌入一“半格经由群”的半直积的幂等元分离同态像.

**[Z15; Question 2, body B07; x≈172–675, y≈366–390]**

**问题 2**$^{[2]}$　推广事实 2 到正则半群的一个尽量大的子类中.

**[Z16; reference heading; x≈422–534, y≈416–441]**

参考文献

**[Z17; reference [1], reference line R01; x≈134–795, y≈462–484]**

[1]　Billhardt B, Hsieh S C. Weakly E-Unitary locally inverse semigroups. preprint

**[Z18; reference [2], reference lines R02–R03; x≈134–820, y≈488–538]**

[2]　M B Szendrei. Some open problems in the structure theory of regular semigroups.  
　　Semigroup Forum, 2002, 64: 213-223

**[Z19; reference [3], reference lines R04–R05; x≈134–820, y≈541–590]**

[3]　McAlister D B. Groups, semilattice and inverse semigroups. Trans Amer Math Soc,  
　　1974, 192: 227-244

**[Z20; reference [4], reference line R06; x≈134–820, y≈594–618]**

[4]　Lawson M V. Almost factorisable inverse semigroups. Glasgow Math J, 1994, 36: 97-111

**[Z21; reference [5], reference lines R07–R08; x≈134–820, y≈622–669]**

[5]　Lawson M V. Inverse Semigroups: The Theory of Partial Symmetries. Singapore: World  
　　Scientific, 1998

**[Z22; contributor line C01; x≈668–820, y≈697–723]**

撰稿人: 郭聿琦

**[Z23; affiliation line C02; x≈742–820, y≈727–750]**

西南大学

## 2. Sentence-aligned literal English rendering

The tags align to the source transcription above. Semicolon-separated printed clauses remain aligned to the source sentence. No mathematical implication is added to the source wording.

**[M66]** ·66·　10000 Scientific Problems　Mathematics Volume

**[Z01]** Two embedding problems concerning regular semigroups.

**[Z01E — English already printed]** Two Embedding Problems for Regular Semigroups

**[Z02a]** Regular semigroups are a mainstream research area of the algebraic theory of semigroups, and developing the study of regular semigroups by starting from the study of several regular semigroups “closer to groups (in a certain sense)” (such as inverse semigroups, completely regular semigroups, and so on) is a natural trend.

**[Z02b]** The two problems below were posed in 2002 in accordance with this trend.

**[Z03a]** Let S be a semigroup and $a\in S$.

**[Z03b]** S is called a monoid if S contains an identity element; a is called a regular element of S if the subset $V(a)$ of S is nonempty, where $V(a)=\{x\in S\mid axa=a,xax=x\}$, and the elements of $V(a)$ are called inverses of a; S is called a regular (inverse) semigroup if, for every $a\in S$, $V(a)$ is nonempty ($V(a)$ is a singleton set).

**[Z03c]** The subset formed by all idempotents of S is denoted by $E(S)$.

**[Z03d + Z04]** $E(S)$ is called a band if $E(S)$ is a subsemigroup of S; S is called an orthodox semigroup if $E(S)$ is a band; the band $E(S)$ is called a semilattice (commutative band), regular band, normal band, or seminormal band if they respectively satisfy

$$
\begin{aligned}
&\forall e,f\in E(S),\quad ef=fe;\\
&\forall e,f,g\in E(S),\quad efege=efge;\\
&\forall e,f,g\in E(S),\quad efge=egfe;\\
&\forall e\in E(S),\quad eE(S)e\ \text{is a regular band}.
\end{aligned}
$$

**[Z05a]** As is well known, inverse semigroups are exactly the semigroups for which $E(S)$ is a semilattice, and therefore inverse semigroups are orthodox;

**[Z05b]** a nonzero idempotent f of S is called primitive if, for every nonzero idempotent e, $ef=fe=e\to e=f$.

**[Z06a]** A regular semigroup is called completely simple if it has no proper ideal and contains a primitive idempotent; a semigroup S is called locally inverse if, for every idempotent e, $eSe$ is an inverse subsemigroup; a regular semigroup S is called weakly $E$-unitary if

**[Z07]**

$$
\forall e\in E(S),\quad \forall a\in S,\quad e\le a\to a\in E(S).
$$

**[Z08 + Z09]** Here “$\le$” is the natural partial order on the regular semigroup S, defined as follows: for every $a,b\in S$,

$$
a\le b\leftrightarrow\exists e,f\in E(S),\quad a=eb=bf.
$$

**[Z10a]** A regular semigroup S is called locally $r$-orthodox if, for every $e\in E(S)$, $eSe$ is an orthodox (monoid) semigroup whose $E(eSe)$ is a regular band.

**[Z10b + Z11]** A homomorphism $\phi$ from semigroup S to semigroup T is called idempotent-separating if

$$
\forall e,f\in E(S),\quad \phi(e)=\phi(f)\to e=f.
$$

**[M67]** Two embedding problems concerning regular semigroups　·67·

**[Z12]** **Fact 1**$^{[1,2]}$. Every weakly $E$-unitary locally inverse semigroup can be embedded in a “normal band by a completely simple semigroup” semidirect product.

**[Z13]** **Question 1**$^{[2]}$. Can every weakly $E$-unitary locally $r$-orthodox semigroup be embedded in a “seminormal band by a completely simple semigroup” semidirect product?

**[Z14]** **Fact 2**$^{[2\sim5]}$. Every inverse semigroup can be embedded in an idempotent-separating homomorphic image of a “semilattice by a group” semidirect product.

**[Z15]** **Question 2**$^{[2]}$. Extend Fact 2 to as large a subclass of regular semigroups as possible.

**[Z16]** References

**[Z17–Z21 — English already printed]** The five reference entries are transcribed at Z17–Z21 above.

**[Z22]** Contributor: Guo Yuqi

**[Z23]** Southwest University

## 3. Inventory of printed definitions, symbols, parameters, quantifiers and questions

Each quotation below is from the tagged text above. A statement that no separate definition is printed does not supply one.

| Item | Exact printed text / formula | Location |
|---|---|---|
| Title | “关于正则半群的两个嵌入问题” | Z01; p66 title |
| Printed English title | “Two Embedding Problems for Regular Semigroups” | Z01E; p66 |
| Stated research setting and examples | “正则半群是半群代数理论的主流研究领域” … “逆半群, 完全正则半群等” | Z02; p66 B01–B03 |
| Printed year | “于 2002 年被提出来的” | Z02; p66 B03 |
| Semigroup and element | “令 $S$ 是一半群, $a\in S$” | Z03; p66 B04 |
| Monoid | “称 $S$ 是一幺半群, 如果 $S$ 含恒等元” | Z03; p66 B04 |
| Regular element and set $V(a)$ | “称 $a$ 是 $S$ 的一个正则元, 如果 $S$ 的子集 $V(a)$ 非空, 其中, $V(a)=\{x\in S\mid axa=a,xax=x\}$” | Z03; p66 B04–B05 |
| Inverse element | “$V(a)$ 中的元素称为 $a$ 的逆元” | Z03; p66 B05–B06 |
| Regular/inverse semigroup and quantifier | “称 $S$ 是一正则 (逆) 半群, 如果关于任意 $a\in S$, $V(a)$ 非空 ($V(a)$ 是一单元集)” | Z03; p66 B06–B07 |
| Idempotent set | “$S$ 的所有幂等元形成的子集用 $E(S)$ 表示” | Z03; p66 B07 |
| Band | “称 $E(S)$ 是一带, 如果 $E(S)$ 是 $S$ 的一个子半群” | Z03; p66 B07–B08 |
| Orthodox semigroup | “称 $S$ 是一纯正半群, 如果 $E(S)$ 是一带” | Z03; p66 B08 |
| Four named kinds of band | “一半格 (交换带)、正则带、正规带、半正规带” | Z03; p66 B08–B09 |
| Semilattice condition | “$\forall e,f\in E(S),\ ef=fe$” | Z04; p66 F01 |
| Regular-band condition | “$\forall e,f,g\in E(S),\ efege=efge$” | Z04; p66 F02 |
| Normal-band condition | “$\forall e,f,g\in E(S),\ efge=egfe$” | Z04; p66 F03 |
| Seminormal-band condition | “$\forall e\in E(S),\ eE(S)e$ 是正则带” | Z04; p66 F04 |
| Printed inverse/semilattice statement | “逆半群恰是 $E(S)$ 为半格的半群, 因此逆半群是纯正的” | Z05; p66 B10 |
| Nonzero primitive idempotent and quantifier | “称 $S$ 的非零幂等元 $f$ 是本原的, 如果关于任意非零幂等元 $e$, $ef=fe=e\to e=f$” | Z05; p66 B10–B11 |
| Completely simple | “一正则半群称为完全单的, 如果它不含真理想, 而且含一本原幂等元” | Z06; p66 B12 |
| Locally inverse | “称半群 $S$ 是局部逆的, 如果关于任意幂等元 $e$, $eSe$ 是逆子半群” | Z06; p66 B12–B13 |
| Weakly $E$-unitary | “称正则半群 $S$ 是弱 $E$-酉的, 如果” … “$\forall e\in E(S),\ \forall a\in S,\ e\le a\to a\in E(S)$” | Z06–Z07; p66 B13–B14, F05 |
| Natural partial order and both quantifiers | “其中, ‘$\le$’ 是正则半群 $S$ 上的自然偏序, 定义如下: 关于任意 $a,b\in S$” | Z08; p66 B15 |
| Natural-order formula | “$a\le b\leftrightarrow\exists e,f\in E(S),\ a=eb=bf$” | Z09; p66 F06 |
| Locally $r$-orthodox | “称一正则半群 $S$ 是局部 $r$-纯正的, 如果关于任意 $e\in E(S)$, $eSe$ 是以 $E(eSe)$ 为正则带的纯正 (幺) 半群” | Z10; p66 B16–B17 |
| Idempotent-separating homomorphism | “称半群 $S$ 到半群 $T$ 的同态 $\phi$ 是幂等元分离的, 如果” … “$\forall e,f\in E(S),\ \phi(e)=\phi(f)\to e=f$” | Z10–Z11; p66 B17, F07 |
| Fact 1, quantifier and printed cited scope | “每一弱 $E$-酉局部逆半群可嵌入一‘正规带经由完全单半群’的半直积” | Z12; p67 B01–B02; $^{[1,2]}$ |
| Question 1, full printed question | “是否每一弱 $E$-酉局部 $r$-纯正半群可嵌入一‘半正规带经由完全单半群’的半直积?” | Z13; p67 B03–B04; $^{[2]}$ |
| Fact 2, full printed statement | “每一逆半群可嵌入一‘半格经由群’的半直积的幂等元分离同态像” | Z14; p67 B05–B06; $^{[2\sim5]}$ |
| Question 2, complete printed wording | “推广事实 2 到正则半群的一个尽量大的子类中” | Z15; p67 B07; $^{[2]}$ |
| Extension/semidirect product, embedded image | “经由”, “半直积”, “幂等元分离同态像”; no separate definition of those expressions printed on these pages beyond Z10–Z11 | Z12–Z14; p67 |
| References and names | Complete [1]–[5] as quoted at Z17–Z21 | p67 R01–R08 |
| Contributor and affiliation | “撰稿人: 郭聿琦”; “西南大学” | Z22–Z23; p67 C01–C02 |

## 4. Illegible or uncertain glyphs and ambiguity record

No content glyph was judged illegible in the two displayed permitted images. The natural-order symbol is encoded as $\le$ at Z07–Z09; the homomorphism symbol is encoded as $\phi$ at Z10–Z11, and the reference range at Z14 as $[2\sim5]$. These are typography encodings, not additional definitions.

The expressions “正规带经由完全单半群”, “半正规带经由完全单半群” and “半格经由群” are quoted exactly as printed. Their English renderings retain the word “by”; no choice of an action, convention, multiplication order, or additional definition is supplied. No source sentence is resolved by a proof or by comparison with another source.

## 5. Completion and scope statement

**TRUNCATED: NO.** Both listed pages visibly contain the entry's title, printed English title, body, definitions and displayed formulae, Facts 1–2, Questions 1–2, five references, contributor and affiliation. No neighbouring page, reference target, web source, held B4 output, lane proof, withdrawn material or quarantined review was opened.

**Nothing beyond transcription was done:** visual copying, literal translation, quoted printed-definition/symbol/parameter/quantifier/question inventory and documentary coordinates only. No interpretation, reformulation, proof, solution idea, selected example, scientific computation, source-status/priority/novelty assessment or contact with MathSemigroup-2, PhysicsMOQLS8-2 or another owner. No STOP is lifted, no mathematical verdict is issued, and this source packet becomes a lane input only through a later separately frozen release.

**END OF B4r LITERAL SOURCE PACKET.**
