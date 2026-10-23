# Olson FC19 — parent verdict v1

Recorded 2026-10-20T19:59:43-0700 (`/bin/date`). **CORRECTNESS_ACCEPTED_SCOPED (two terminal cells).** Read proof-FC19-v1.md with worker process erratum1 and parent erratum v1.

## Accepted statements

For (kappa,p)=(7,19) [FC19(a)] and (8,19) [FC19(b)]: no word of length74 over D_38 without an identity38-subword in increasing original index order has SOME admissible NF with terminal k=20 and kappa_hat=kappa. Extra reflection pairs may lie anywhere in the odd blocks; every empty NF run separates different reflection values; no o_F, nonempty-run, rotation-pair or rigidity hypothesis is imposed. Each part is proved independently and covers EVERY frame, including RES, with no UB, saturation, Lemma15–20 or FC717 premise.

- WC719: level-5 upper windows (ell,M)=(6,4), G/Q/P top-five types and empty-run counting give Xi_ev+Xi_od≤−1.
- WC819: level-5 and level-6 windows, six exhaustive classes C1–C6, the lower-window Lemma4.2 and the five swapped subsets of Lemma4.6 give Xi_ev+Xi_od≤−1.
- Accepted UMR-F and Lemma14 (verdict a2535971…) supply the frame data and identity Xi_ev+Xi_od=e≥0, used only after each count.

## Composed p19 terminal statement (union of separately accepted scopes; no new mathematics)

For p=19, terminal k=20, full existential NF antecedent; NF/GRX range0≤kappa_hat≤18:

| kappa_hat | accepted scope | verdict |
|---|---|---|
| 0 | K0T | [olson-K0T-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K0T-parent-verdict-v1.md) |
| 1 | LOWER-K1 (p≥11) | [olson-LOWER-K1-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-LOWER-K1-parent-verdict-v1.md) |
| 2 | K2 (p≥11) | [olson-K2-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K2-parent-verdict-v1.md) |
| 3 | K3 (p≥13) | [olson-K3-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-K3-parent-verdict-v1.md) |
| 4 | USK, 3≤kappa_hat≤floor((p−1)/4)=4 | [olson-USK-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-USK-parent-verdict-v1.md) |
| 5 | FCW, p=4·5−1 | [olson-FCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FCW-parent-verdict-v1.md) |
| 6 | TCW, p=4·6−5 | [olson-TCW-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-verdict-v1.md) |
| 7 | FC19(a) | [olson-FC19-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-verdict-v1.md) |
| 8 | FC19(b) | [olson-FC19-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-verdict-v1.md) |
| 9–17 | upper-half composite [(p−1)/2,p−2] | [olson-BOTTOM-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-BOTTOM-parent-verdict-v1.md) |
| 18 | PP1-EXCL (kappa_hat=p−1) | [olson-PP1-EXCL-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-PP1-EXCL-parent-verdict-v1.md) |

Hence **every terminal k=20 cell at p=19 is excluded**. With the separately accepted p7, p11, p13 and p17 unions, every terminal k=p+1 cell is excluded for p∈{7,11,13,17,19}. For p≥23 the cells floor((p+7)/4)<kappa_hat≤(p−3)/2 remain OPEN. Other k, nonterminal/inverse/assembly obligations and full ordered Olson remain OPEN.

## Verification

- Codex gpt-6.1-sol/max read-only:0F/0M/0m for each cell. Receipt `83377fbb91bc9c6deba8ed06c2e18e1c09a46aeebb8021792dd2d2d98f3bda1a`.
- Claude claude-opus-5-5/max no tools:0F/0M/1m (input wording; parent erratum v1); every branch re-derived. Receipt `182137ba0ca9d2fa58a7b01b46fd61a7096be85c360dad31fe90f8d64e5f2de3`.
- Parent written check (af0695519e0be30528a594a9b220e1d29bb26a5565f876a70cdf338e04e55ff8) re-derived both counts before the second review.

Process qualifications: worker authored UMR and FC717 and disclosed pre-freeze unwritten attempts/exposure; freeze precedes new written derivation but strict preregistration is not certified; process erratum1 and pre-creation wording replacements are disclosed. The parent's untrusted half-level hint was recorded before assignment. Written/model correctness acceptance only: not Lean/kernel-verified or human peer-reviewed; no novelty/priority or runtime claim; no mathematical computation or enumeration was used.

| Artifact | SHA256 |
|---|---|
| [FC19-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/FC19-scope-v1.md) | `889acf673aed2005ee3ab412d5d82050c7026d053e54844574a000619eee3c05` |
| [proof-FC19-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/proof-FC19-v1.md) | `10cc94b0210274167b1aa124e2a977b1b94c65275c153cd8a4492564e1bdb57b` |
| [erratum-1-process-wording-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/erratum-1-process-wording-v1.md) | `6642ac5fe622fc0007164cae223bc9448ee8c0e06e615c663527700ccbfda528` |
| [review-package-FC19-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/review-package-FC19-v1.md) | `4b9f60eef1f544f724cb02b5fee79dd24e95fc65938c4e425f6e3a33053f0246` |
| [review-excerpts-FC19-v1.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/review-excerpts-FC19-v1.json) | `d41ff0561aeea19b9e0935e58446c80303c8aed0f23b39e3b82fdc14bcc0ba21` |
| [olson-FC19-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-erratum-v1.md) | `930380257c675c31e32715bef5233ec6acdb192e836c4ab2f141021cd0ac4a65` |
| [olson-FC19-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-written-check-v1.md) | `af0695519e0be30528a594a9b220e1d29bb26a5565f876a70cdf338e04e55ff8` |
| [olson-FC19-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-codex-v1.prompt.stdout.txt) | `e419e7c5f763e11575345dc9b6a205b00a3a6fc9114a4355ff291b450f2aad3c` |
| [olson-FC19-claude-v1.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-claude-v1.prompt.note.md) | `532ea86d7d47bc8a96a3ab439acc7ca2a72246eb6453d083994502d9c3cbed3d` |
| [olson-FC19-review-freeze-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-review-freeze-v1.json) | `9c3b28b1b40df0acf8c7f7bf12d048d169564a1a207fa3c25fa48783b8c8e802` |
| [olson-UMR-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md) | `a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772` |
