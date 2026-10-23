# Olson BOTTOM — the κ_hat=(p−1)/2 cell accepted; terminal upper half complete

Recorded 2026-10-19T22:28:09-0700 (`/bin/date`).

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Under the full existential admissible-NF/word antecedent, for every prime p≥11, terminal k=p+1, κ_hat=(p−1)/2 (e=(p+1)/2) and every 3≤c≤p−1, no avoider exists (Theorem BOTTOM; P §§1–5 + C). Imports: NF, GRX if-direction, RS(b) (integer K), classical CD, and UH-A at its literal antecedent for c≥3. With Theorem R excluding c≥p, **the whole specified bottom cell of the upper half is empty**.

Codexgpt-6.1-sol/max0F/0M/0m; Claudeclaude-opus-5-5/max0F/0M/2m disposed by parent erratum v1. Completed exit0 and bindings checked.

**Composed consequence (union of separately accepted scopes, no new mathematics):** for every prime p≥7, no avoider of length 4p−2 over D_(2p) has an admissible NF with terminal k=p+1 and κ_hat in the upper half [(p−1)/2, p−2]:
- κ̂=p−2: accepted terminal k=p+1, κ̂=p−2 exclusion;
- κ̂=p−3: KP3-EXCL (bb9d8a27);
- κ̂=p−4: KP4-A (p≥11, 5b56b367) + R7 (p=7, b83058b2);
- (p+1)/2≤κ̂≤p−5: Corollary U (8242b90b, imports UH-A);
- κ̂=(p−1)/2: this verdict.
Each cell carries its own imports (UH-A where used); historical computer-assisted records unchanged. Not claimed: the lower half (κ̂<(p−1)/2; LOWER candidate covers only κ̂=1 and is under review), other terminal k, multiset-only statements, full ordered Olson, novelty, human or Lean verification.

| Artifact | SHA256 |
|---|---|
| [proof-BOTTOM-parity-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-bottom-cell/proof-BOTTOM-parity-v1.md) | `b648411f7ed7b2b17fdd9bcc4a51f2df24ca7a1540eb88cd4c7fbd2e6080a9f3` |
| [proof-BOTTOM-close-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-bottom-cell/proof-BOTTOM-close-v1.md) | `e9e1b55315bbe4cc24b50da7c600f6c8af09626b7a4ead6731a171b775521817` |
| [review-package-BOTTOM-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-bottom-cell/review-package-BOTTOM-v1.md) | `3cfd96abd75bf93ff14e37e0a68910ed83afe141d1e0d6c08d152b9eb1d4b789` |
| [olson-BOTTOM-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-erratum-v1.md) | `a92cc68de543f681b9d9cfc59459e15d3cb82728412bf319c2a345cbf1d9209a` |
| [olson-BOTTOM-parent-written-check-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-written-check-v1.json) | `b610fab2b91560ebf0a891f395ac509d7b248c280649bb10d002c7bba44adee6` |
| [olson-BOTTOM-codex-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-codex-v1.prompt.receipt.json) | `7491801c27191fa79fc2e8f6da6ae0924c2ac77a1cbf294d4cb6a70aec317610` |
| [olson-BOTTOM-claude-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-claude-v1.prompt.receipt.json) | `9ea4e954298aabb04dab972cafa6e1e5fa78de836df09205e649b1b68e412cc0` |
| [olson-BOTTOM-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-codex-v1.prompt.stdout.txt) | `ef5ea0140f08bc501fdedc7fb8bdc9382c291e800b93f0fe4ab61fcb4b7a7a61` |
| [olson-BOTTOM-claude-v1.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-claude-v1.prompt.note.md) | `e110ce1994a5306a86e7e91730dce3b8d5b3dabffede4042eb3ab74041feff60` |
