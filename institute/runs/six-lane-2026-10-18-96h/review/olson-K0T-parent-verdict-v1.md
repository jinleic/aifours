# Olson terminal kappa_hat=0 (K0T) — parent acceptance

Recorded 2026-10-20T03:24:11-0700 (`/bin/date`).

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, read with errata v1 (175557df97b387b8a3adc5330d5f01161b554fdad3c73798b32de36cdf56894a) and v2 (6896d0d5819655e4534487fa6965ff171e8ed0c689e1b2de1ae17957bd2d35bb). For every odd prime p (in particular p=5, 7 and p≥11) no length-(4p−2) avoider over D_(2p) has an admissible normal form with terminal k=p+1 and kappa_hat=0. Proof: NF gives F=k+2(p−1−kappa_hat)=3p−1 for the normalized avoider of the same length; Theorem P (length≤4p−1, F≥1, F+sum floor(n_t/2)≥3p−1) then yields an identity 2p-subword. Correct relative to Theorem P's literal statement (single-family Codex review "correct", recorded accepted at the K0*/RED verdict, relied on at the same threshold by accepted LOWER); P's proof was not re-reviewed here.

Codex gpt-6.1-sol/max **0F/0M/0m**; Claude claude-opus-5-5/max **0F/0M/4m** (P provenance, equivalent-restatement wording, verbatim frontier lines, p-range), all disposed by erratum v2. Both exit0 with expected model/effort and checked bindings. Parent derived the arithmetic and confirmed LOWER LF44/LF55–56.

**Frontier change:** for the terminal k=p+1 cell only, the "kappa_hat=0 open" listing in LOWER-K1 verdict LF9, K3 verdict LF13 and USK verdict LF13 is superseded; K2 verdict LF11 ("not settled here") is unaffected. Not settled: k≤p with kappa_hat=0 (ROT-KP is a structure theorem), nonterminal kappa=0, K0*/REFL residuals, other cells and full ordered Olson. No novelty, Lean, human-referee or runtime authority.

| Artifact | SHA256 |
|---|---|
| [olson-terminal-kappa0-parent-corollary-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-terminal-kappa0-parent-corollary-v1.md) | `18eee7e9224a13784c9e75faad16f0a1aff308b7304475800773d42ac34f7865` |
| [olson-terminal-kappa0-parent-corollary-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-terminal-kappa0-parent-corollary-erratum-v1.md) | `175557df97b387b8a3adc5330d5f01161b554fdad3c73798b32de36cdf56894a` |
| [olson-terminal-kappa0-parent-corollary-erratum-v2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-terminal-kappa0-parent-corollary-erratum-v2.md) | `6896d0d5819655e4534487fa6965ff171e8ed0c689e1b2de1ae17957bd2d35bb` |
| [olson-K0T-first-family-parent-disposition-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-first-family-parent-disposition-v1.json) | `efd89b10a4361a55ce5106091dc5b3330c9b7783f659d9fca9b02436f81c7114` |
| [olson-K0T-codex-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-codex-v1.prompt.receipt.json) | `d5e030d147a90d90ee2fee26f622fbac0a7c15f457838a835851a28072cd3cb6` |
| [olson-K0T-claude-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-claude-v1.prompt.receipt.json) | `25a686b7731b98b40eb682402d8866a16c2dafea800ff71af315868b29bc335f` |
| [olson-K0T-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-codex-v1.prompt.stdout.txt) | `9d463e8e01265889cb310868a6f8a145819086216aea30291baa5f7960716d6e` |
| [olson-K0T-claude-v1.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-claude-v1.prompt.note.md) | `d557d8bd717bbddca095e696c83bb83ecf83cb341f4dcc10c713572ff6bf94fc` |
