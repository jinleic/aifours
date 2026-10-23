# Olson UFC — parent verdict v1

Recorded 2026-10-21T03:09:03-0700 (`/bin/date`). **CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Read proof-UFC-v1.md with the fixed-parameter finiteness clarification and parent erratum v1.

## Accepted statements

- **Theorem U0.** On T (prime p≥17, floor((p+7)/4)<kappa≤(p−3)/2), restricted to T0: kappa≤(3p+5)/8 for p≡1 mod4, kappa≤(3p+7)/8 for p≡3 mod4 (equivalently j≥2v−1 in the stated parameterisation). For every frame of every target NF (terminal k=p+1, kappa_hat=kappa, length4p−2 original-index identity-2p-subword avoider over D_(2p), SOME admissible NF, arbitrary extra-pair placement, genuine empty-run rule), Xi(S_ev)+Xi(S_od)≤−1. With accepted UMR's identity, **no such NF exists in T0.**
- **E0, ENV:** valid on all of T at their stated scopes (ENV's reverse bound uses the total identity explicitly).
- **U1:** every hypothetical surviving frame in T∖T0 induces data in R_U (a necessary relaxation; finite per fixed (kappa,p); no converse or existence).
- **Named cells:** (8,23), (9,23), (10,29) excluded (in T0). (10,23) not decided here; separately handled by FC1023 (pending its own second family).

## Open boundary

HIGH-COVER (Sec.5.4) is the first unproved uniform step of this method and is equivalent to nonexistence on T∖T0; it is not shown false, necessary or nonempty. The complementary strip j≤2v−2 remains OPEN. No other terminal k, inverse/assembly obligation or full ordered Olson is claimed.

## Verification

- Codex gpt-6.1-sol/max:0F/0M/0m. Receipt `18dd569edc89d9f4091991acb9c35507d1d84f8f701595279011454964bedd82`.
- Claude claude-opus-5-5/max no tools:0F/0M/1m (Sec.5.4 wording; erratum v1). Receipt `3ce6084ed55d457efe65ce5758a8818a5145f0f5e61a92351d74235f7b62d001`.
- Parent written check (0bc950ea8c165732115036c2281b91b1da558abd561c8d63ad8c2c7d9ff8e927) re-derived the counts, A5 constants, E0/ENV and residual before either review output.

Only accepted UMR at its literal scope is a premise; no FC717/FC19 lemma is used. Process qualifications: worker authored UMR/FC717/FC19; freeze preceded new derivation but strict preregistration is not certified; parent hint exposure recorded; two pre-creation wording replacements. Written/model correctness acceptance only; not Lean/kernel-verified or human peer-reviewed; no novelty/priority or runtime claim; no mathematical computation or enumeration used.

| Artifact | SHA256 |
|---|---|
| [UFC-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/UFC-scope-v1.md) | `ba2b5e7ae1aa61e7e31a1058ca51941a65b39704cac913bed71ef14dc3ccad23` |
| [proof-UFC-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/proof-UFC-v1.md) | `2d03076c9bbf1afa3d68e42bfc2fe9eeb4a62ee64b59e6c94c53f65a32b670c5` |
| [review-package-UFC-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/review-package-UFC-v1.md) | `6f2262d178dd0cc81a3650fc383379acc16a25fcab52777559a340d145064cae` |
| [review-excerpts-UFC-v1.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/review-excerpts-UFC-v1.json) | `6fe29f2d8aeb3c0addbfdd8170d713036993cd152f96eeee5686cbe409536259` |
| [olson-UFC-parent-scope-precision-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-scope-precision-v1.md) | `9b02608fdeb1054878867f1d9bd014cf5ec8084a91c8edc6a8fae5bc93dede17` |
| [olson-UFC-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-erratum-v1.md) | `b2719ef394c2920d144f39ff2b4a8752eab05161aa67226308309edaf88af40e` |
| [olson-UFC-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-written-check-v1.md) | `0bc950ea8c165732115036c2281b91b1da558abd561c8d63ad8c2c7d9ff8e927` |
| [olson-UFC-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-codex-v1.prompt.stdout.txt) | `ea3396b613438fee160ccaa18dfd691810341c26175015d886042f6119746755` |
| [olson-UFC-claude-v2.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-claude-v2.prompt.note.md) | `747b628067776c6a48d9c6287e852d1569cb651429aa97049c935aa198928f22` |
| [olson-UFC-review-freeze-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-review-freeze-v1.json) | `805aaaf70225376292b539d70ea982f1a29c5f2d9067a5f8b3e4a66ef16273ba` |
| [olson-UMR-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md) | `a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772` |
