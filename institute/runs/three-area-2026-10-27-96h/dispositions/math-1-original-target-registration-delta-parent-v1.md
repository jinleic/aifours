# math-1 original-target registration delta — parent documentary disposition

Parent observation before writing: **2026-10-28T09:49:53-0700 PDT**. Documentary only: no mathematical reasoning, equivalence argument, status/novelty assessment or target revision was performed by Main or by any owner in this chain.

## Complete actual reads and bindings

Main read the complete 162-LF registration audit (raw 1–60, 61–120, 121–162 through ending) and had earlier read the complete 17-LF registered definition text. Main did NOT read the literal packet body, the erratum body, the comparison or recheck bodies, or any book image for this lane; their fidelity status is taken from the frozen receipts and the auditor's bound reads.

| Record | LF | SHA-256 |
|---|---:|---|
| Registration audit (PhysicsRQLS10-2, physics-5) | 162 | `bdba139290540cafe8065b2206e3cc79334c5fa46f2700df99fccd3b3fdec033` |
| Literal packet v1 (PhysicsResearch96h-2, physics-1; immutable) | 253 | `83d0f5e8e134c7c6b836737e2914f4ad7e63f7043c55c5015be7d1e89ae00a6e` |
| Erratum-1 (U1/U2 resolved from the 300-dpi re-render) | 39 | `206f2c7e47aeb98745114a215869082c17ae80955144c3d6a86cb27a3e011582` |
| Fidelity comparison (PhysicsRQLS10-2) | 44 | `57d5873cd271f942c8f1a09a07291636f796f9463e62afa1535c32bf3b488925` |
| Fidelity recheck: EXACT_WITH_ERRATUM | 27 | `6178acb39fca9564f5a67809a01ddaac5e8769da857e30b314f07c783c5c05f2` |
| Registered target definition text (lane S1) | 17 | `a4db7478cf384fabdddccede032efe2cd1f33d12ad3e771788e58d5596682e85` |

Source: printed entry 位相型分布的最小表示 (何启明, 张汉勤), mathematics volume printed pp. 544–545 (PDF 560–561), transcribed under the [book-literal gate](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/book-literal-transcription-gate-v1.json) and its [300-dpi addendum](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/book-literal-transcription-gate-v1-addendum-2-math-1-hires-p560.json).

## Documentary finding

1. **The registered math-1 target is a parameterized special family, not the printed question.** The print asks, for a given/general PH distribution \((\alpha,T)\), how to find a PH representation of smallest order with the same distribution for every \(x\ge 0\); it notes that the problem is already solved when \(T\) has special structure (upper or lower triangular; references [2], [4]). The registration asks for the exact minimum PH order of one explicit transform family \(H_{(1,2)}(s)\) over \(a>c>0,\ b>0\), with explicit representation conditions (real Hurwitz Metzler \(T\), \(T\mathbf{1}\le 0\), \(\alpha\ge 0\), \(\alpha\mathbf{1}=1\), resolvent-transform matching) and a numerical residual obligation (\(\beta^2\in(1/2,53/96]\): PH6 construction or PH6 impossibility, G7). None of the family, the conditions or the residual is printed (audit C1–C4); the printed chain model, CDF, nonuniqueness sentence, general question, special-structure sentence and references are absent from the registration (audit B1–B5).
2. **Three interfaces are EQUIVALENCE_NOT_ESTABLISHED** (audit D1–D3): general/given input versus the registered family; the printed equality for every \(x\ge0\) versus the registered transform matching; the printed absorbing-chain convention with initial component \(\alpha_{m+1}\) versus the registered class with \(\alpha\mathbf{1}=1\). Main does not bridge any of them here.
3. **Consequence for reporting.** Every math-1 result in this run and in the prior round (including the accepted special-family minimum-order theorem recorded in the mathematics index) is a result about the registered family. The printed original problem — minimal PH representation for a general PH distribution — is not addressed by those results and remains the original target. Report wording for math-1 must state the registered family and this delta explicitly; "original target" may not be used for the family without the qualification.
4. **The erratum's U2 printed phrase (人们分布系统) remains literally transcribed and semantically ambiguous; it is not repaired or interpreted.

## What this does not do

No STOP is lifted (the NR-NEXT-CONTACT-ZERO source/proof/method STOP and the whole-mixed-packet NONINPUT hold persist). The registration text is not changed; any re-registration of the printed general question would be a new, separately frozen lane release. No mathematical content of the print is adopted as a theorem or hypothesis. The lane owner (MathResearch96h-2) has not been contacted; this disposition and the literal packet chain are to be delivered to the owner as status/input only through a separately frozen release after its current review duty returns.

## Assurance boundary

Same-harness documentary chain: transcriber (physics-1), comparer/auditor (physics-5), parent read of the audit and the registration text. Not human, formal, novelty or source-wide verification; the two book pages are the only printed source read.
