# Documentary registration audit — math-1 PH minimum representation

Auditor **PhysicsRQLS10-2**, physics-5. Actual native `/bin/date` immediately before writing: **Wed Oct 28 09:47:07 PDT 2026**.

**This is a literal registration delta only. No mathematical reasoning, proof, equivalence argument, status/novelty assessment or target revision was performed.** Section A records the limited wording actually shared, not a certification that the lane's target is the whole printed question. Section D explicitly leaves every identified equivalence question unproved. “Absent” below means **not stated in the one frozen 17-LF registration text**, not that something is false or absent from all other records.

## Frozen source chain, pins and actual reads

- S0: `S0-carry-and-resumption-v1.md`, SHA256 **a7161aa016f59552d9ee823cd2e4205df74ef2308e6ad25c4ed18322d78e580b**, 31 LF, read ENTIRELY FIRST.
- Manifest: `registration-audit-math-1-release-v1.json`, SHA256 **cdc0d1e2abf0d3f2604e1c736ddf0f01bb1719870b467fd586452e2efca0fcb6**, read ENTIRELY before any listed body; live hash matched.
- Pre-body ACK: `registration-audit-math-1-prebody-ack-v1.json`, SHA256 **e341f54668ffff5d25baaece7f12af70a5dfaf995c1e3bb4c34597414b4f2399**, **14 LF / 3196 bytes**, written at native preclock09:46:13, pinned09:46:31. It records actual prior B1 same-document/image exposure and prior lane/transcriber contacts, with no clean-cognition claim. No listed body or registration comparison was opened/begun under THIS duty before the ACK.
- Printed literal packet `P`: `physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/book-literal-math-1-v1.md`, SHA256 **83d0f5e8e134c7c6b836737e2914f4ad7e63f7043c55c5015be7d1e89ae00a6e**, 253 LF. Read RAW1–60/61–120/121–180/181–240/241–253 through ending.
- Mandatory additive erratum `E`: `.../werner3-ququart/book-literal-math-1-v1-erratum-1.md`, SHA256 **206f2c7e47aeb98745114a215869082c17ae80955144c3d6a86cb27a3e011582**, 39 LF, read fully BEFORE the registration. U1/U2 are applied as E states; original P remains immutable. E preserves the semantic **AMBIGUOUS** qualification on its literal U2 wording.
- Own B1 comparison `F`: `.../rqls10/book-literal-math-1-comparison-v1.md`, SHA256 **57d5873cd271f942c8f1a09a07291636f796f9463e62afa1535c32bf3b488925**, 44 LF, read completely. Own additive recheck `F2`: `.../rqls10/book-literal-math-1-erratum-1-recheck-v1.md`, SHA256 **6178acb39fca9564f5a67809a01ddaac5e8769da857e30b314f07c783c5c05f2**, 27 LF, read completely. F2's EXACT_WITH_ERRATUM is documentary-fidelity status at its precise two-image cut, not a mathematical or source-history theorem.
- Literal transcriber return receipt `T`: `source-screens/book-literal-20261028/duty-B1-math-1-return-receipt-v1.json`, SHA256 **f9388fe700814d83d20be407643059129b0dbc2fe2227fbb6b9d1d7b422f8e11**, 36 LF, read fully. Recheck receipt `T2`: `.../comparison-B1-math-1-erratum-1-recheck-return-receipt-v1.json`, SHA256 **0efff3a7789221a6cc56b745cd7046aba7b4eacd9a998250c6e6def7a54b50cf**, 23 LF, read fully. These are status/receipt evidence, not a new independent documentary comparison.
- Registered target `R`: `institute/runs/three-area-2026-10-27-96h/written-releases/math-1-ph-order-definitions-v1.md`, SHA256 **a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85**, 17 LF, read RAW1–17 through ending. Its lines7–14 carry literal selection-line prefixes; citations below use the ACTUAL file LF and preserve those prefixes where helpful. The linked selection body was NOT opened.
- Status-only control `Q`: `institute/runs/three-area-2026-10-27-96h/phase-type-whole-mixed-packet-noninput-addendum-2.json`, SHA256 **95b678bf4a4a4bba0480238891d3295aa8950beaad0fb4576e75cdba23174007**, 28 LF, read fully. Both whole mixed artifacts and all consumers remain HELD/ZERO/NONINPUT; none was opened.

All above input hashes were observed matching at09:46:36. No image/page, source, selection, proof, other lane, external reference or unlisted review body was opened in this audit. P/E/F/F2/T/T2 are documentary inputs, not a proof release. The print quotes below reproduce P's Chinese and sentence-aligned English, with E applied where indicated; they do not silently resolve E's ambiguity.

## A. Printed statements / terms captured literally by registration

### A1 — PH representation and minimum-order terminology (wording overlap only)

**Print — Chinese (P LF68, LF90 and LF92):** “记 \((\alpha,T)\) 为 \(\xi\) 的一个 PH-表示”; “对给定 PH-分布 \((\alpha,T)\) 怎样找到其具有最小阶数的 PH-表示 \((\hat\alpha,\hat T)\), 使对任何 \(x\geqslant0\),” followed by P LF94–100's displayed equality.

**Print — literal English (P LF176, LF187–193):** “denote \((\alpha,T)\) as a PH-representation of \(\xi\)” and “for a given PH-distribution \((\alpha,T)\), how to find its PH-representation \((\hat\alpha,\hat T)\) having the smallest order, so that for every \(x\geqslant0\),” followed by the displayed equality.

**Registration — actual file LF10:** “Determine its exact minimum continuous-time PH order wherever it is PH, and distinguish non-PH parameters. A representation(alpha,T) uses …”.

**Documentary classification:** the PH-representation pair and minimum PH-order language are present in both. R addresses the PARTICULAR registered expression and adds conditions; it does **not literally reproduce** the print's entire universal question or equality. Whether these differently stated tasks/formulas correspond is left to D1–D3, not asserted here.

## B. Printed content absent from the registration text

### B1 — Motivation, stochastic model and literal chain construction

**Print — Chinese (P LF32–44, LF46–64):** “位相型分布理论是研究随机服务系统的一个主要数学工具”; “位相型分布或 PH-分布 … 是一个有限状态马氏过程吸收时间的分布”; the following sentence gives the continuous-time chain, state set, absorbing/transient statuses and generator, and LF56–64 gives \(e\), initial distribution and absorption time.

**Print — literal English (P LF146–173):** “Phase-type distribution theory is a main mathematical tool for studying stochastic service systems”; “A phase-type distribution … is the distribution of the absorption time of a finite-state Markov process,” followed by the specified chain/generator, vector, initial distribution and absorption-time wording.

**Registration — R LF6–10:** “For every a>c>0,b>0 …”; “A representation(alpha,T) uses arbitrary real Hurwitz Metzler T with T1<=0 and alpha>=0,alpha1=1 …”. The registration has no literal chain state set, absorbing/transient description, displayed block generator, initial mass \(\alpha_{m+1}\), or absorption-time definition. Its different representation conditions are separately inventoried in C2; no equivalence is inferred.

### B2 — Printed distribution and phase terminology

**Print — Chinese (P LF68):** “则 \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e,\ x\geqslant0\). 将 \(\xi\) 称为 PH-分布, 记 \((\alpha,T)\) 为 \(\xi\) 的一个 PH-表示, 称状态 \(\{1,2,\cdots,m,m+1\}\) 为该 PH-表示的位相.”

**Print — literal English (P LF174–176):** “then \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e,\ x\geqslant0\)” and “call the states \(\{1,2,\cdots,m,m+1\}\) the phases of this PH-representation.”

**Registration — R LF10:** “must match the exact transform alpha(sI-T)^(-1)(-T1).” The printed cumulative-distribution expression, named absorption variable, phase-set wording and its \(x\)-domain do not occur literally in R. No implication between the printed expression and registered transform is claimed; see D2.

### B3 — Weak-convergence, approximation and application context

**Print — Chinese (P LF72, LF76, LF84; E LF17):** “在弱收敛拓扑下, 由所有 PH-分布组成的集合是定义在 \([0,\infty)\) 上全体概率分布组成的空间上的一个稠密子集 (见文献 [3])”; “对给定任何一个 … 概率分布函数, 我们都可以构造一个 PH-分布使之很好地近似”; corrected E wording names “排队系统、库存系统、可靠性系统” and “重要权重指标”; P LF84 adds “这使分析和优化该模型成为可能 (见文献 [1]).”

**Print — literal English (P LF178–180, LF183; E LF21):** “under the topology of weak convergence … a dense subset”; “for any given probability distribution function … we can construct a PH-distribution to approximate … very well”; corrected “queueing systems, inventory systems and reliability systems … important weight indices”; “This makes analysis and optimization of the model possible (see reference [1]).”

**Registration — R LF6–12:** specifies the single transform family and its minimum-order/residual tasks; it does not state the printed density, general approximation, application examples, indices or reference [1]/[3] statements. This is a documentary absence, not a judgment about those statements.

### B4 — Nonuniqueness and the printed general question/equality

**Print — Chinese (E LF29; P LF90–100, LF108):** “PH-分布的 PH-表示是不唯一的”; the print asks “对给定 PH-分布 \((\alpha,T)\) 怎样找到其具有最小阶数的 PH-表示 \((\hat\alpha,\hat T)\), 使对任何 \(x\geqslant0\)” and displays \(1-\alpha\exp(Tx)e=1-\hat\alpha\exp(\hat T x)e\); it ends “但对一般 PH-分布 \((\alpha,T)\), 如何找其最小表示…”.

**Print — literal English (E LF33; P LF187–193, LF197):** “the PH-representation of a PH-distribution is not unique”; “for a given PH-distribution … how to find its PH-representation … having the smallest order, so that for every \(x\geqslant0\)” followed by that displayed equality; “for a general PH-distribution … how to find its minimal representation…”.

**Registration — R LF6–10:** “For every a>c>0,b>0 … Determine its exact minimum continuous-time PH order wherever it is PH, and distinguish non-PH parameters.” R does not literally state the printed general-input question, its explicit new hatted pair, or the equality for every \(x\geqslant0\), nor the nonuniqueness sentence. This records a difference in wording and scope, not a conclusion that a special-family question answers or cannot answer the general one. E's separate “人们分布系统” wording remains explicitly ambiguous; its meaning is not repaired here.

### B5 — Printed special-structure sentence and references/contributors

**Print — Chinese (P LF104, LF108, LF112–136):** “当 \(T\) 具有一些特殊结构时, 如 \(T\) 为上三角或下三角, 这类问题已经解决, 见文献 [2] 与 [4]”; the entry gives references [1]–[4], “撰稿人：何启明　张汉勤” and “中国科学院数学与系统科学研究院”.

**Print — literal English (P LF195–211):** “When \(T\) has some special structures, such as \(T\) being upper triangular or lower triangular, this kind of problem has already been solved; see references [2] and [4]”; the printed references and contributor/affiliation lines follow.

**Registration — R LF10–12:** “All topologies, reducible/irreducible cases, nonuniform holding rates and latent canceled modes are included”; “Uniform-diagonal or companion-only results are partial…”. It does not reproduce the print's upper-/lower-triangular sentence, bibliographic entries or contributor/affiliation lines. No claim that these different labels describe equivalent classes is made.

## C. Registration content not stated in the print

### C1 — The actual parameterized transform family and quantifiers

**Print — Chinese (P LF90–100, LF108):** “对给定 PH-分布 \((\alpha,T)\) 怎样找到其具有最小阶数的 PH-表示…” with the displayed \(x\)-domain equality; “但对一般 PH-分布 \((\alpha,T)\), 如何找其最小表示…”.

**Print — literal English (P LF187–193, LF197):** “for a given PH-distribution … how to find its PH-representation … having the smallest order” with the displayed equality; “for a general PH-distribution … how to find its minimal representation…”.

**Registration — R LF6–9 (selection prefixes7–10):** “For every a>c>0,b>0, put d=a-c,beta=b/d and \(H_{(1,2)}(s)=c(a^2+b^2)^2/[(s+c)((s+a)^2+b^2)^2]\).” R LF10 adds “wherever it is PH, and distinguish non-PH parameters.”

The named \(a,b,c,d,\beta,s\) family, the inequalities and the explicit transform are not printed in P/E. The print describes a given/general PH distribution, whereas R expressly asks about PH and non-PH parameters in its named family. This is an additional registered special-family task, not an equivalence conclusion.

### C2 — Explicit representation constraints and transform matching

**Print — Chinese (P LF40–68):** the finite-state absorbing/transient chain with generator \(\begin{pmatrix}T&-Te\\0&0\end{pmatrix}\), initial distribution \((\alpha,\alpha_{m+1})\), and \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e\), \(x\geqslant0\).

**Print — literal English (P LF150–176):** “continuous-time Markov chain … state \(m+1\) is an absorbing state … all the other states are transient states; the infinitesimal generator is” the displayed block matrix; “the initial distribution is \((\alpha,\alpha_{m+1})\)” and the displayed distribution formula.

**Registration — R LF10:** “A representation(alpha,T) uses arbitrary real Hurwitz Metzler T with T1<=0 and alpha>=0,alpha1=1, and must match the exact transform alpha(sI-T)^(-1)(-T1).”

The explicit words/conditions **real**, **Hurwitz**, **Metzler**, \(T1\le0\), \(\alpha\ge0\), \(\alpha1=1\), and the resolvent-transform matching expression are not literally printed in P/E. In particular, retain the print's \(\alpha_{m+1}\) term and R's \(\alpha1=1\) verbatim; do not silently substitute either for the other. Their relationship is D3, not an established mismatch or equivalence theorem.

### C3 — Explicit topology and mode coverage

**Print — Chinese (P LF40, LF104):** the printed setup describes the finite chain and says “当 \(T\) 具有一些特殊结构时, 如 \(T\) 为上三角或下三角…”.

**Print — literal English (P LF150, LF195):** the chain setup and “When \(T\) has some special structures, such as \(T\) being upper triangular or lower triangular…”.

**Registration — R LF10:** “All topologies, reducible/irreducible cases, nonuniform holding rates and latent canceled modes are included.”

Those exact topology, reducibility, holding-rate and cancellation terms are not stated in P/E. No assertion is made about whether the printed general wording includes or excludes any of them mathematically.

### C4 — Numerical-interval PH6/PH7 residual and named G7

**Print — Chinese (P LF90–108):** “对给定 PH-分布 … 怎样找到其具有最小阶数的 PH-表示” and the general-question sentence.

**Print — literal English (P LF187–197):** “for a given PH-distribution … how to find its PH-representation … having the smallest order” and “for a general PH-distribution … how to find its minimal representation…”.

**Registration — R LF12:** “for beta^2 in(1/2,53/96], either construct an actual PH6 representation for a nonempty specified parameter range (then minimum6 follows), or prove a topology-unrestricted PH6 impossibility on a nonempty specified subrange (then minimum7 follows from G7). Uniform-diagonal or companion-only results are partial…”.

The named interval, PH6/PH7 outcomes, G7, nonempty-subrange alternatives and exclusion of uniform-diagonal/companion-only partial results as substitutes are registered content absent from P/E. They are quoted as the target's words only; no underlying G7 result, implication, bound or existence assertion is checked or adopted here.

## D. Wording requiring a mathematical equivalence argument

### D1 — Given/general printed input versus the registered family

**Print — Chinese (P LF90, LF108):** “对给定 PH-分布 \((\alpha,T)\)” and “对一般 PH-分布 \((\alpha,T)\)”.

**Print — literal English (P LF187, LF197):** “for a given PH-distribution \((\alpha,T)\)” and “for a general PH-distribution \((\alpha,T)\)”.

**Registration — R LF6–10:** “For every a>c>0,b>0 … \(H_{(1,2)}(s)=\cdots\)” and “Determine its exact minimum continuous-time PH order wherever it is PH, and distinguish non-PH parameters.”

**EQUIVALENCE_NOT_ESTABLISHED:** no proof or assertion that the parameterized registered task and the printed given/general task are equivalent, exhaustive, or mutually sufficient. Their distinct written quantifiers/inputs are quoted above; this audit does not attempt to bridge them.

### D2 — Printed equality for every x versus registered transform equality

**Print — Chinese (P LF90–100):** “使对任何 \(x\geqslant0\),” with \(1-\alpha\exp(Tx)e=1-\hat\alpha\exp(\hat T x)e\).

**Print — literal English (P LF187–193):** “so that for every \(x\geqslant0\),” followed by that equality.

**Registration — R LF10:** “must match the exact transform alpha(sI-T)^(-1)(-T1).”

**EQUIVALENCE_NOT_ESTABLISHED:** the print states an \(x\)-domain equality between two pairs; R states a transform-matching condition for the registered family. No transform/uniqueness/conversion argument, domain extension or missing normalization is supplied here.

### D3 — Printed absorbing-chain convention versus registered representation class

**Print — Chinese (P LF40–68):** “状态 \(m+1\) 为吸收态, 而其他状态均为瞬态”, “初始分布为 \((\alpha,\alpha_{m+1})\)” and the printed generator/distribution expressions.

**Print — literal English (P LF150–176):** “state \(m+1\) is an absorbing state, whereas all the other states are transient states” and “the initial distribution is \((\alpha,\alpha_{m+1})\)”, with the displayed expressions.

**Registration — R LF10:** “arbitrary real Hurwitz Metzler T with T1<=0 and alpha>=0,alpha1=1”.

**EQUIVALENCE_NOT_ESTABLISHED:** no argument equating the stated classes, order convention, treatment of the initial absorbing-state component or constraints. Their exact textual distinctions are retained in B1/B2/C2. In particular, neither the presence nor absence of an atom is inferred by this documentary audit.

## Count and non-effect

| Section | Count | Unit of count |
|---|---:|---|
| A | **1** | Captured literal terminology item, with its restricted-scope qualification. |
| B | **5** | Grouped printed-content items absent as literal text in R. |
| C | **4** | Grouped registration-content items absent as literal text in P/E. |
| D | **3** | Distinct wording/equivalence interfaces marked EQUIVALENCE_NOT_ESTABLISHED. |

These are grouped documentary items, not counts of all individual sentences or independent theorems. The same wording can legitimately appear in B/C and D because “not stated literally” and “equivalence not established” are different observations. No inference is made from the counts.

This audit does not change R or any frozen source, determine equivalence, validate G7, authenticate unseen book pages, assess scientific status/novelty, or authorize further lane work. All own RQLS/xs4/w96/L1 and math-1 whole-mixed-packet STOP/HOLD/ZERO controls, N4 UNKNOWN/historical child exit unestablished, auxiliary214 STOP and the global source pause persist. Same-harness documentary comparison only; no formal/kernel, executable, human or configured-family gate passed.

**END REGISTRATION AUDIT — A1 / B5 / C4 / D3.**
