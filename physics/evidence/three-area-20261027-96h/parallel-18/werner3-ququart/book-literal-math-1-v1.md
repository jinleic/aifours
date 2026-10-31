# B1 — Math-1 Book-Literal Packet

## Source and Actual Clocks

- Duty: B1. Transcriber: PhysicsResearch96h-2 / physics-1.
- Frozen duty SHA256: `9b89d77f707fee2c9aefbf4e62387b9d98c331c6e0d3763fcbf3d1b74c056964`.
- Pre-body ACK: `book-literal-math-1-prebody-ack-v1.json`, SHA256 `01f09d9c5da867d8f83130c3d63b0afa49b0e6c34d268747f4547ed48c5a2e8a`.
- Actual native clock immediately before ACK: **Wed Oct 28 09:21:30 PDT 2026**.
- Actual native clock immediately before this packet: **Wed Oct 28 09:30:13 PDT 2026**.
- The two images were viewed only after the ACK was saved/sent. The first image was viewed again to inspect its glyphs. Individual image-view wall clocks were not separately observed.
- PDF-page labels560–561 are the duty's labels. The images visibly carry printed pages544–545.
- First image: `source-math-0560.png`, SHA256 `13a5ddd85e134412599d837e8663490b73cbd6842a70291257cf7edd7e7a5bd5`, expected318084 bytes; hash matched.
- Second image: `source-math-0561.png`, SHA256 `45f5a2b379799bba1c6523f87113371a4e23da5169c55207621f7091ac13159a`, expected86147 bytes; hash matched.
- **TRUNCATED: NO.** The listed images visibly contain the title, body, references and contributor/affiliation ending.
- `⟦U1⟧` and `⟦U2⟧` below mark two localized uncertain two-glyph spans. They are not text supplied from context. Locations are recorded below; no proposed replacement is inserted.

## Verbatim Chinese Transcription

**[H544 — printed p544, running header]**

· 544 ·　10000 个科学难题　数学卷

**[T1 — printed p544, upper title]**

位相型分布的最小表示

**[T2 — printed p544, upper English title as printed]**

Minimal Representation of Phase-Type Distribution

**[C01 — printed p544, upper body, first sentence]**

位相型分布理论是研究随机服务系统的一个主要数学工具.

**[C02 — printed p544, upper body, following sentence]**

位相型分布或 PH-分布 (phase-type distribution) 是一个有限状态马氏过程吸收时间的分布.

**[C03 — printed p544, upper body, chain and generator lead-in]**

具体地, 对于一个状态空间为 \(\{1,2,\cdots,m,m+1\}\) 连续时间马尔可夫链 \(\{X(t),\ t\geqslant0\}\), 状态 \(m+1\) 为吸收态, 而其他状态均为瞬态, 无穷小生成元为

**[F01 — printed p544, upper-middle displayed matrix]**

\[
\begin{pmatrix}
T & -Te\\
0 & 0
\end{pmatrix},
\]

**[C04 — printed p544, middle body, immediately below F01]**

其中 \(e\) 是以 1 为元素的 \(m\) 维列向量, 初始分布为 \((\alpha,\alpha_{m+1})\), 这里 \(\alpha=(\alpha_1,\cdots,\alpha_m)\).

**[C05 — printed p544, middle body, absorption-time lead-in]**

令 \(\xi\) 表示该马氏链状态 \(m+1\) 的吸收时间, 即

**[F02 — printed p544, middle displayed absorption time]**

\[
\xi=\inf\{t\geqslant0\mid X(t)=m+1\},
\]

**[C06 — printed p544, middle body, distribution and terminology]**

则 \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e,\ x\geqslant0\). 将 \(\xi\) 称为 PH-分布, 记 \((\alpha,T)\) 为 \(\xi\) 的一个 PH-表示, 称状态 \(\{1,2,\cdots,m,m+1\}\) 为该 PH-表示的位相.

**[C07 — printed p544, middle body, weak-convergence sentence]**

人们已经证明了在弱收敛拓扑下, 由所有 PH-分布组成的集合是定义在 \([0,\infty)\) 上全体概率分布组成的空间上的一个稠密子集 (见文献 [3]).

**[C08 — printed p544, middle-lower body, approximation sentence]**

这说明对给定任何一个定义在 \([0,\infty)\) 上的概率分布函数, 我们都可以构造一个 PH-分布使之很好地近似这个给定的概率分布函数.

**[C09 — printed p544, lower body, model sentence; U1 unresolved]**

而由 PH-分布描述的随机模型如排队系统、库存系统、可靠性系统, 其重要⟦U1⟧指标往往能精确地给出.

**[C10 — printed p544, lower body, following sentence]**

这使分析和优化该模型成为可能 (见文献 [1]).

**[C11 — printed p544, lower body, representation/order sentence; U2 unresolved]**

然而, PH-分布的 PH-表示是不唯一的, 对 PH-表示 \((\alpha,T)\), 其阶数 \(m\) 在分析和应用模型时至关重要, 阶数小的表示在人们⟦U2⟧系统以及数值计算时有许多方便之处.

**[C12 — printed p544, lower body, stated question and identity lead-in]**

因此人们关注 PH-分布的最小表示: 即对给定 PH-分布 \((\alpha,T)\) 怎样找到其具有最小阶数的 PH-表示 \((\hat\alpha,\hat T)\), 使对任何 \(x\geqslant0\),

**[F03 — printed p544, lower displayed identity]**

\[
1-\alpha\exp(Tx)e=1-\hat\alpha\exp(\hat T x)e.
\]

**[C13 — printed p544, bottom body, first sentence]**

当 \(T\) 具有一些特殊结构时, 如 \(T\) 为上三角或下三角, 这类问题已经解决, 见文献 [2] 与 [4].

**[C14 — printed p544, bottom body, final sentence]**

但对一般 PH-分布 \((\alpha,T)\), 如何找其最小表示是几十年来人们关注的一个公开问题.

**[H545 — printed p545, running header]**

位相型分布的最小表示　· 545 ·

**[R0 — printed p545, upper heading]**

参 考 文 献

**[R1 — printed p545, upper reference block, entry1]**

[1] Asmussen S. Applied Probability and Queues. New York: Wiley, 1987

**[R2 — printed p545, upper reference block, entry2]**

[2] He Q M, Zhang H Q. An algorithm for computing minimal coxian representations. INFORMS Journal on Computing, 2008, 20: 179-190

**[R3 — printed p545, upper reference block, entry3]**

[3] Neuts M F. Matrix-Geometric Solutions in Stochastic Models: An Algorithmic Approach. Baltimore: The Johns Hopkins University Press, 1981

**[R4 — printed p545, upper reference block, entry4]**

[4] O’ Cinneide C. Characterization of phase-type distributions. Stochastic Models, 1990, 6: 1-57

**[A01 — printed p545, upper-middle contributor line below references]**

撰稿人：何启明　张汉勤

**[A02 — printed p545, upper-middle affiliation line]**

中国科学院数学与系统科学研究院

## Sentence-Aligned Literal English Rendering

**[H544 / p544 running header]** ·544·　10,000 Scientific Difficult Problems　Mathematics Volume

**[T1 / p544 upper title]** Minimal Representation of Phase-Type Distribution.

**[T2 / p544 printed English title]** Minimal Representation of Phase-Type Distribution

**[C01 / p544 upper body]** Phase-type distribution theory is a main mathematical tool for studying stochastic service systems.

**[C02 / p544 upper body]** A phase-type distribution, or PH-distribution (phase-type distribution), is the distribution of the absorption time of a finite-state Markov process.

**[C03 / p544 upper body]** Specifically, for a continuous-time Markov chain \(\{X(t),\ t\geqslant0\}\) with state space \(\{1,2,\cdots,m,m+1\}\), state \(m+1\) is an absorbing state, whereas all the other states are transient states; the infinitesimal generator is

**[F01 / p544 upper-middle display]**

\[
\begin{pmatrix}
T & -Te\\
0 & 0
\end{pmatrix},
\]

**[C04 / p544 middle body]** where \(e\) is an \(m\)-dimensional column vector whose elements are 1, the initial distribution is \((\alpha,\alpha_{m+1})\), and here \(\alpha=(\alpha_1,\cdots,\alpha_m)\).

**[C05 / p544 middle body]** Let \(\xi\) denote the absorption time of state \(m+1\) of this Markov chain, that is,

**[F02 / p544 middle display]**

\[
\xi=\inf\{t\geqslant0\mid X(t)=m+1\},
\]

**[C06, sentence1 / p544 middle body]** then \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e,\ x\geqslant0\).

**[C06, sentence2 / p544 middle body]** Call \(\xi\) a PH-distribution, denote \((\alpha,T)\) as a PH-representation of \(\xi\), and call the states \(\{1,2,\cdots,m,m+1\}\) the phases of this PH-representation.

**[C07 / p544 middle body]** It has already been proved that, under the topology of weak convergence, the set consisting of all PH-distributions is a dense subset in the space consisting of all probability distributions defined on \([0,\infty)\) (see reference [3]).

**[C08 / p544 middle-lower body]** This says that, for any given probability distribution function defined on \([0,\infty)\), we can construct a PH-distribution to approximate this given probability distribution function very well.

**[C09 / p544 lower body]** For stochastic models described by PH-distributions, such as queueing systems, inventory systems and reliability systems, their important ⟦U1⟧ indicators can often be given exactly. **AMBIGUOUS at the unresolved glyph span U1; no replacement is supplied.**

**[C10 / p544 lower body]** This makes analysis and optimization of the model possible (see reference [1]).

**[C11 / p544 lower body]** However, the PH-representation of a PH-distribution is not unique; for a PH-representation \((\alpha,T)\), its order \(m\) is of vital importance when analyzing and applying models, and representations of small order have many conveniences when people ⟦U2⟧ systems and carry out numerical computation. **AMBIGUOUS at the unresolved glyph span U2; no replacement is supplied.**

**[C12 / p544 lower body]** Therefore people are concerned with the minimal representation of a PH-distribution: that is, for a given PH-distribution \((\alpha,T)\), how to find its PH-representation \((\hat\alpha,\hat T)\) having the smallest order, so that for every \(x\geqslant0\),

**[F03 / p544 lower display]**

\[
1-\alpha\exp(Tx)e=1-\hat\alpha\exp(\hat T x)e.
\]

**[C13 / p544 bottom body]** When \(T\) has some special structures, such as \(T\) being upper triangular or lower triangular, this kind of problem has already been solved; see references [2] and [4].

**[C14 / p544 bottom body]** But for a general PH-distribution \((\alpha,T)\), how to find its minimal representation is an open problem that people have been concerned with for several decades.

**[H545 / p545 running header]** Minimal Representation of Phase-Type Distribution　·545·

**[R0 / p545 upper heading]** References.

**[R1 / p545 reference1; printed English retained]** [1] Asmussen S. Applied Probability and Queues. New York: Wiley, 1987

**[R2 / p545 reference2; printed English retained]** [2] He Q M, Zhang H Q. An algorithm for computing minimal coxian representations. INFORMS Journal on Computing, 2008, 20: 179-190

**[R3 / p545 reference3; printed English retained]** [3] Neuts M F. Matrix-Geometric Solutions in Stochastic Models: An Algorithmic Approach. Baltimore: The Johns Hopkins University Press, 1981

**[R4 / p545 reference4; printed English retained]** [4] O’ Cinneide C. Characterization of phase-type distributions. Stochastic Models, 1990, 6: 1-57

**[A01 / p545 contributor line]** Contributors: He Qiming; Zhang Hanqin.

**[A02 / p545 affiliation line]** Academy of Mathematics and Systems Science, Chinese Academy of Sciences.

## Printed Definition, Symbol, Parameter and Quantifier Inventory

The entries below quote the printed text/formulas above; no additional conditions or definitions are supplied.

1. **Name and distribution definition — C02:** “位相型分布或 PH-分布 (phase-type distribution) 是一个有限状态马氏过程吸收时间的分布.”
2. **State space and process — C03:** “状态空间为 \(\{1,2,\cdots,m,m+1\}\) 连续时间马尔可夫链 \(\{X(t),\ t\geqslant0\}\)”. Printed symbols/indices: \(m,m+1,X(t),t\geqslant0\).
3. **Absorbing/transient states — C03:** “状态 \(m+1\) 为吸收态, 而其他状态均为瞬态”.
4. **Generator and its printed symbols — C03/F01:** “无穷小生成元为” \(\begin{pmatrix}T&-Te\\0&0\end{pmatrix}\). Printed symbols: \(T,e,0\).
5. **Vector e and dimension m — C04:** “\(e\) 是以 1 为元素的 \(m\) 维列向量”.
6. **Initial distribution and alpha entries — C04:** “初始分布为 \((\alpha,\alpha_{m+1})\), 这里 \(\alpha=(\alpha_1,\cdots,\alpha_m)\)”.
7. **Absorption-time variable and defining formula — C05/F02:** “令 \(\xi\) 表示该马氏链状态 \(m+1\) 的吸收时间, 即” \(\xi=\inf\{t\geqslant0\mid X(t)=m+1\}\).
8. **Printed distribution formula and x domain — C06:** \(\Pr(\xi\leqslant x)=1-\alpha\exp(Tx)e,\ x\geqslant0\). Printed symbols/operations: \(\Pr,\xi,x,\alpha,\exp,T,e\).
9. **PH-representation and phases — C06:** “记 \((\alpha,T)\) 为 \(\xi\) 的一个 PH-表示, 称状态 \(\{1,2,\cdots,m,m+1\}\) 为该 PH-表示的位相”.
10. **Printed topology/set quantifiers — C07:** “在弱收敛拓扑下”, “所有 PH-分布”, “定义在 \([0,\infty)\) 上全体概率分布”, “一个稠密子集”.
11. **Printed approximation quantifier — C08:** “对给定任何一个定义在 \([0,\infty)\) 上的概率分布函数, 我们都可以构造一个 PH-分布”.
12. **Order m and nonuniqueness — C11:** “PH-分布的 PH-表示是不唯一的”, “对 PH-表示 \((\alpha,T)\), 其阶数 \(m\)”. The later U2 text remains unresolved as recorded below.
13. **Explicit printed question, new pair and universal equality — C12/F03:** “对给定 PH-分布 \((\alpha,T)\) 怎样找到其具有最小阶数的 PH-表示 \((\hat\alpha,\hat T)\), 使对任何 \(x\geqslant0\)” and \(1-\alpha\exp(Tx)e=1-\hat\alpha\exp(\hat T x)e\).
14. **Printed special structures — C13:** “\(T\) 为上三角或下三角”.
15. **Explicit general-question wording — C14:** “但对一般 PH-分布 \((\alpha,T)\), 如何找其最小表示是几十年来人们关注的一个公开问题.” This is a quotation of the page, not an assessment beyond transcription.
16. **Printed bibliographic labels and identities — R0–R4/A01–A02:** labels [1]–[4], the four printed references, “撰稿人：何启明　张汉勤”, and “中国科学院数学与系统科学研究院” are transcribed above.

## Uncertain Glyphs and Unresolved Sentences

Coordinates refer approximately to the **original1241×1754 image**, not the displayed rescaling. The textual anchors identify the spans; no reading is supplied from context.

- **U1 — p544 / C09:** two glyphs after “其重要” and before “指标”, in the line beginning “由 PH-分布描述的随机模型”. Approximate original-pixel bounding box **x830–895, y975–1015**. Unresolved; no proposed replacement.
- **U2 — p544 / C11:** two glyphs after “在人们” and before “系统以及数值计算时”, in the line beginning “要, 阶数小的表示”. Approximate original-pixel bounding box **x355–430, y1070–1115**. Unresolved; no proposed replacement.
- **AMBIGUOUS, quoted without resolution:** “其重要⟦U1⟧指标往往能精确地给出.”
- **AMBIGUOUS, quoted without resolution:** “阶数小的表示在人们⟦U2⟧系统以及数值计算时有许多方便之处.”

No formula glyph or other text was completed from mathematical knowledge or another source. The two uncertain spans remain explicit gaps in the literal text.

## Truncation and Activity Statement

**TRUNCATED: NO.** The entry begins with its title on printed p544 and visibly ends with references and contributor/affiliation on printed p545. No additional page was opened to extend it.

Nothing beyond transcription, sentence-aligned literal translation and printed-definition/symbol/quantifier inventory was done. No interpretation, reformulation, proof, solution idea, status/priority/novelty assessment, source-equivalence conclusion or contact with MathResearch96h-2 or any other lane owner was performed. No bibliography or reference was opened. Only the two listed page images were used for the text; unresolved glyphs were not improvised.

This is source-only work. It lifts no STOP/HOLD/ZERO boundary and is not a research result, proof acceptance or openness certification. Any future use as a mathematical input requires a later separately frozen lane release.
