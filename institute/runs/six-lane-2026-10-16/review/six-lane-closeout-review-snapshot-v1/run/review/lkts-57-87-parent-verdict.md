# LKTS(57) and LKTS(87): independently verified existence certificates

## Result

**Large sets of Kirkman triple systems of orders 57 and 87 exist.** Each certificate is an explicit labelled list. LKTS(57) has 55 resolved STS(57) with 28 classes of 19 triples; LKTS(87) has 85 resolved STS(87) with 43 classes of 29 triples. In each, every class partitions the points, every pair occurs exactly once per constituent, and the constituents together contain every 3-subset exactly once.

Chen Wang, [arXiv:2607.21521v1 §4](https://arxiv.org/html/2607.21521v1#S4) (23 July 2026; still the only version when the parent re-opened the abstract page on 2026-10-16), states that LKTS(v) is known for every admissible v<200 "with the two possible exceptions being 57 and 87", and names direct construction of these two as a natural short-term objective. **Combined with the constructions summarized in that source, these certificates leave no admissible order below 200 open.** This combined statement inherits Wang's literature summary at uneven evidence levels (see the priority audit; order 147 rests on a Xu–Ji 2021 family whose body could not be opened, and 93/177 rest on Wang's own unrefereed preprint).

The book's question asks for **every** admissible order. It remains open.

## Evidence

| Gate | LKTS(57) | LKTS(87) |
|---|---|---|
| Raw certificate SHA-256 | `09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09` | `65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e` |
| Parent stdlib checker (strict parser; explicit triple-universe equality) | PASS, `lkts57-parent-verification-v1.json` | PASS, `lkts87-parent-verification-v1.json` |
| Cross-vendor Codex `gpt-6.1-sol` (max), own in-memory verifier | RESULT: VALID; 30,856 lines accounted; 22 parser corruptions rejected; `lkts57-codex-verification.md` | RESULT: VALID; 109,736 lines accounted; 5 corruptions rejected for intended reasons; `lkts87-codex-verification.md` |
| Third implementation (Claude Opus 5.5 max, prompt-only; written from the definition alone; same-vendor) | Parent-executed: VALID under `python3` and `python3 -O`; wrong hash, wrong order and all 8 mutations rejected for the intended invariant | Same: VALID; all 10 negative cases rejected for the intended invariant |
| Parent mutation controls | 8 rejected; LKTS(9), two LKTS(15) positive controls pass | 8 rejected |
| Other checkers | Prior dossier checker PASS (parent-run); worker Python and C checkers PASS | Prior dossier checker, worker Python and C checkers PASS (worker receipts) |
| Compact seed → exact bytes | Byte-identical; regenerated file re-verified | Byte-identical; regenerated file re-verified |
| Construction action | G513=(Z19⋊Z9)×Z3; constituent orbits 19+9+9+9+9 | G903=Z43⋊Z21 on {∞}∪Z43×{0,1}; constituent orbits 43+21+21 |
| Bound receipts | `lkts57-independent-verification-receipt.json` | `lkts87-independent-verification-receipt.json` |

Seed replay: `lkts-both-seed-replay-v1/parent-replay.json`. Action audits: `lkts57-action-parent-check.json`, `lkts87-action-parent-check.json`. The groups act on the underlying block sets; chosen resolutions are transported by coset representatives and are **not** globally invariant. Validity of the raw certificates depends on no solver output, symmetry lemma or orbit-forcing argument.

## Priority and significance

A bounded primary-source audit (`lkts57-87-priority-audit.md`) located no earlier construction or announcement of either order, and no earlier claim of the complete spectrum below 200. It checked every listed recursive family for applicability (tripling, products, Wang–Shi q^n+2, Xu–Ji, Liu–Lei, Tan–Zhou, Wang 7q+2, Ji, Yuan–Kang, Zhou–Chang) and confirmed none reaches 57 or 87. It separates related known objects: OLKTS(57), OLKTS(87), LKTS(171) and LKTS(261). Residual risk: the 12-week window since Wang, paywalled bodies, and unindexed venues. **A search miss is not proof of novelty.**

Method calibration: prescribed automorphism groups with Kramer–Mesner exact cover and per-base resolution SAT is an established design-theory technique. Wang himself suggested "direct computer search, preferably with a prescribed automorphism group". The new ingredients are the specific groups, elementary automorphism lemmas that force the orbit structures, and an orientation congruence used to prune resolution models. **Significance: potentially substantive specialist result** — it settles the two explicitly named smallest open cases. It is not a new general method or a solution of the universal problem.

**FRONTIER:** DELIVERY-READY for external expert review, with NOVELTY-UNCLEAR priority. Under the six-lane contract's breakthrough gate, this is a complete solution of an explicitly stated open finite target with independent parent verification, cross-vendor review and a primary-source comparison. It has no human peer review, publication or Lean-kernel proof.

## Remaining work

- Optional Lean kernel existence theorem (`lkts57-kernel/`, running).
- Third verifier complete: `lkts-claude-verifier-v1/checker.py` (SHA-256 `2bfbc1f8…6d1`), execution receipt `lkts-claude-verifier-v1/parent-execution.json`.
- Worker generalization attempt for v=2q+1, q≡7 (mod 12); finite samples are not a uniform theorem.
