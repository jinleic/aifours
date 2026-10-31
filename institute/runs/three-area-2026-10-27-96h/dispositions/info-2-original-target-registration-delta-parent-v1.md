# info-2 original-target registration delta — parent documentary disposition

Parent observation before writing: **2026-10-28T09:53:10-0700 PDT**. Documentary only: no mathematical reasoning, equivalence argument, status/novelty assessment or target revision was performed by Main or by any owner in this chain.

## Complete actual reads and bindings

Main read the complete 252-LF registration audit (raw 1–60, 61–125, 126–190, 191–252 through ending) and lines 29–37 of the registered definition text to verify the truncation finding below. Main did NOT read the literal packet, erratum, comparison or recheck bodies, or any book image for this lane; fidelity status is taken from the frozen receipts and the auditor's bound reads.

| Record | LF | SHA-256 |
|---|---:|---|
| Registration audit (MathOlson-2-2, math-2) | 252 | `0ffbf2687013eebc2a600b44202902c2d8ace34c05ce1ffe228154887cf59344` |
| Literal packet v1 (MathSun8-2, math-6; immutable) | 300 | `41bfcab9dd1a784e76f7db022955b5bc2e45c105cffe76661720e502ceed2e47` |
| Erratum-1 (eight corrections: 严格 ×3, 族 ×2, 可, three lexical) | 201 | `4cbf03691952d0dd1d83d482b84540fa9c36138ad536b33a5a765b8ba6cf12c6` |
| Fidelity comparison (MathOlson-2-2) | 98 | `ea05272f3c3e0727a89ab5a8a6e7c8be96fbe32e7df3d30d99f99cc3d4e794f9` |
| Fidelity recheck: EXACT_WITH_ERRATUM | 53 | `7e257946afdd88878fc5a275475b962e80a72a85b289f264923324dbc6b592f6` |
| Registered target definition text (lane S1) | 37 | `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad` |

Source: printed entry 区间系统的鲁棒严格正实综合 (郁文生, 王龙), information-science volume printed pp. 680–682 (PDF 701–703), transcribed under the [book-literal gate](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/book-literal-20261028/book-literal-transcription-gate-v1.json).

## Documentary finding

1. **The registered info-2 target is a single-order specialization with added conventions.** The print asks, for stable interval-polynomial sets of order greater than 4, whether a polynomial exists that forms a strictly positive real rational family with the set, or equivalently whether robust stability is necessary and sufficient for robust SPR synthesizability; it also poses a separate region question (given \(a\in H^n\), find all \(b\)) and an explicit-coefficient-expression question, and records a general "given an \(n\)-th order set \(F\), does there exist and how does one find" frame (audit A6–A8, B3–B5). The registration specializes to \(n=7\), a monic closed coefficient box (degenerate intervals allowed), a common real numerator of exact degree seven, strict positivity at every finite real \(\omega\) including zero, and an explicit counterexample alternative; it adds a separately labelled uncertain-leading-coefficient variant, "necessity is immediate; the open part is sufficiency", and external provenance (Wang–Yu ACC 2001 / arXiv math/0202242, 2026 announcements for \(n=5,6\)) (audit C1–C8). The registration itself states that the book text does not say "monic".
2. **Twenty-two printed items are absent from the registration as such** (audit B1–B22), including the preliminary \(b(s)\in P^m\) clause (unreconciled with the printed \(P^n\) definition), the explicit root clause of \(H^n\), the segment/polytope families, the even/odd-term and \(n\le3\), \(n\le4\) historical statements, the Anderson/Betser–Zeheb history, the fourth-order history and reference [10], the continuous/discrete/D-SPR remark, references [1]–[10] and affiliations.
3. **Eight interfaces are EQUIVALENCE_NOT_ESTABLISHED** (audit D1–D8): order \(>4\) versus \(n=7\)/\(n\ge5\); \(b\in P^n\) versus "exact degree"; the printed family formulation versus the registration's "Equivalently"; interval set versus monic closed box and leading-coefficient variant; negative-real-part roots versus "strictly Hurwitz"; every real \(\omega\) versus "finite … including zero"; necessity sentence versus "open part is sufficiency"; printed references versus the registration's external provenance. Main does not bridge any of them.
4. **Documentary defect in the frozen registration text.** Line 31 of the registered definition text ("**Fully solved means:** for every n ≥ 5, either a proof that every robustly Hurwitz monic box of") ends mid-sentence; verified by Main at the file (lines 29–37). The frozen S1 release is not edited; the defect is recorded here and the completion of that sentence is NOT inferred. Any later lane release must either supply the complete sentence from its original dossier source under a pin or treat the "fully solved" criterion as unstated.
5. **Consequence for reporting.** info-2 results in this run and the prior round are results about the registered \(n=7\) monic closed-box specialization under the registered conventions; the printed question for all orders greater than 4 (and the separate region and explicit-expression questions) is the original target and is not addressed by those results. Report wording must carry the specialization and the registration defect explicitly.

## What this does not do

No STOP is lifted (the post-v6 method-separation hold, the stopped Wang–Yu statement audit and all consumers persist). The registration text is not changed. No mathematical content of the print is adopted as a theorem or hypothesis. The lane owner (InfoSPR7-2) has not been contacted.

## Assurance boundary

Same-harness documentary chain: transcriber (math-6), comparer/auditor (math-2; same auditor as the fidelity comparison, disclosed), parent read of the audit and of the registration lines 29–37 only. Not human, formal, novelty or source-wide verification; the three book pages are the only printed source read.
