# Olson FC1023 — parent verdict v1

Recorded 2026-10-20T22:22:15-0700 (`/bin/date`). **CORRECTNESS_ACCEPTED_SCOPED (single terminal cell).** Read proof-FC1023-v1.md with parent erratum v1.

## Accepted statement

No word of length90 over D_46 without an identity46-subword in increasing original index order has SOME admissible NF with terminal k=24 and kappa_hat=10. Extra reflection pairs arbitrary in the odd blocks; genuine empty-run rule; no o_F/nonempty-run/rotation-pair/rigidity premise. EVERY frame is covered, including all cases any candidate R23 description would select, with no UB/RES/saturation/giant-pair/Lemma20-converse/UFC premise.

Method: WC1023 proves Xi(S_ev)+Xi(S_od)≤−1 from the reduced data using the all-run parity theta_i≡|L_i| mod2 (literal UMR Lemma10 with odd labels), signed run costs, upper windows at levels6/7 only, the positive-P6 whole-pair case, five exhaustive classes, mass coupling and the deduced ≥26-letter seventh run. Accepted UMR-F/Lemmas0–13 supply the data; the total identity enters only at the final contradiction.

## Composed consequence (union of separately accepted scopes; no new mathematics)

For p=23, terminal k=24, NF/GRX range0≤kappa_hat≤22: kappa_hat0..3 (K0T; K1,K2,K3),4 (USK),5 (FCW p=4·5−1),6 (TCW p=4·6−5),7 (SCW p=4·7−3),8,9 (FC19-style adjacent-level counts are NOT claimed here; these two cells are covered by the UFC candidate T0, which is NOT yet accepted), **10 (FC1023, this verdict)**, and the upper-half composite [(p−1)/2,p−2]=11..21 with p−1=22 by PP1-EXCL. **Because the UFC T0 subrange (covering kappa_hat 8 and 9 at p=23) is still an unaccepted candidate, the full p=23 terminal row is NOT yet closed; after UFC acceptance it would close.** No other k, nonterminal/inverse/assembly obligations or full ordered Olson are claimed.

## Verification

- Codex gpt-6.1-sol/max read-only:0F/0M/0m, every lemma re-derived. Receipt `62ac9bccf0abe0dab44a3d37d65f38d9f5276e1f01efcea4b79ed2b04bb5d308`.
- Parent written check (c3c100d6340c01986094afc0a2a6647d88dfd81f5af246c31fada2df0996667d) re-derived all sections before reading any review output.
- Second family (Claude) queued; this verdict requires it and remains provisional until then, per the two-family rule. No frontier promotion before that review.

Process qualifications: single-author worker with full UMR/FC717/FC19/UFC exposure disclosed; freeze preceded new derivation but strict preregistration is not certified; three pre-creation wording changes and unused post-freeze routes disclosed in checkpoints. Written/model correctness acceptance only; not Lean/kernel-verified or human peer-reviewed; no novelty/priority or runtime claim; no mathematical computation or enumeration was used.

| Artifact | SHA256 |
|---|---|
| [FC1023-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-10-23/FC1023-scope-v1.md) | `190f9656606750f184963724d211bfaaf7165b05e7dc16c3fe5d78397d3cdf1e` |
| [proof-FC1023-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-10-23/proof-FC1023-v1.md) | `7795fdbddaa8afa177332687ecbc8f15483a0f330a30fba57e140343a513e130` |
| [review-package-FC1023-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-10-23/review-package-FC1023-v1.md) | `1814245f9e1dff845d3f6d37fbd3d5cefd799a24b06c3d24cf9f22c048ed816f` |
| [review-excerpts-FC1023-v1.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-10-23/review-excerpts-FC1023-v1.json) | `a8f834b122a5cd0dc1e2fd0e9819ba741a12fa3dd6d2007c9c7980d548232f36` |
| [olson-FC1023-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-erratum-v1.md) | `9966046795690fd9087de61bd9165f9c0726bb9ab4664b897a16193d2eb57f98` |
| [olson-FC1023-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-written-check-v1.md) | `c3c100d6340c01986094afc0a2a6647d88dfd81f5af246c31fada2df0996667d` |
| [olson-FC1023-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-codex-v1.prompt.stdout.txt) | `17d0d86dfd419c5734e5f1c3cacfe57e3cb1a7a3cd11bc7be12d992fd1c9837b` |
| [olson-FC1023-review-freeze-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-review-freeze-v1.json) | `bfd54c2356b0c3a827b0cffec9aa776be9642392b57a3e96082b84c28c40e610` |
| [olson-UMR-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md) | `a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772` |
