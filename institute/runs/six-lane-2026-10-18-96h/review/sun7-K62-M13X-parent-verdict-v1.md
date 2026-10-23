# Sun K6.2*: orientations (1,3) and (3,1) are excluded

Recorded at 2026-10-19T13:44:59-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Written proof relative to accepted original-scope E1, LFC/INV/E6/E7/R0, VFC, E3 (including Z11(a) under alpha_(d i*)=1), E3-C2/DG for alpha*, and M13-A's accepted DG*/C2* for alpha at (1,3). **Computer-assisted Sun(5)/Sun(6) remain transitive imports**, not newly replayed here. This excludes a full named regime, not all K6.2*, K7 or Sun(7).

## Exact accepted result

In any group with finite-index subgroups, no configuration of class K6.2* has (alpha_(d i*),alpha*_(d i*)) equal to **(1,3) or (3,1)**. Every admissible5-marker placement (d,i*,t,some p in O minus {t},or absent), arbitrary exponents and w-cofactors are covered. E3 provides e_d>=4,e*=2 and the3-marker t in O with f_t>=2,f*=1. For (3,1), apply the (1,3) theorem to the ACTUAL inverted configuration; no unproved matrix symmetry.

The supporting Lemmas1/1'/2, PropositionSG, R4S, DEG, CIS/EQS, P2-P4, BUD, T16, ONE, TRI, FB and DEEP are accepted at their printed M13 scopes with the errata below. In particular **SG is i*-free**: for both families z and every nonempty R subset O, T_z({d} union R)=lcm(n_d,n_R)*2^s, s>=0; hence gcd(n_v,T_z(V minus {v,i*}))=6 for every v in O including t and a5-marked p. This record does not grant SG or these conclusions outside M13.

## Evidence and mandatory reading order

- [Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed/K62-M13X-v1.md) `b86bb186e425ea5ac69a51d85ad5f56cfc1abd2a08c66c169fd54de074262db9` (332lines); [scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed/K62-M13X-SCOPE-v1.md) `072c509805f89b8cfff7f57c97ff4508f1a7aca6925977fb341198881497bf01`; [package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed/review-package-M13X-v1.md) `a87ccfcf21b5035bb7b137fbf16bff9d252c96c3af6bc5841f4431415f60df47`; [manifest](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed/review-excerpts-M13X-v1.json) `c3e0851d1e801fc69c99271a69247cc03b2f8522c7c1c38308cea6d364b6b056`.
- [Original review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-review-freeze-v1.json) `471cb6714f1673bd5c7ab5018a02c1f7d6c1b2456b57e2e1021556f79ff20641`; [corrected Claude freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-claude-v2-freeze-v1.json) `06892ba8c26ad6f2a799d99a8d4d36fe590f1ac5bfd0dc4bdbeb8c1a973792db`.
- Read [parent erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-parent-erratum-v1.md) `f8dc60cd085a89cc079e07df68d3606f6b52e343e0099dbde18b59d4348cb440`, then [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-parent-erratum-v2.md) `56f88d7c2ce742b3af071f9cba680cec6081c11ec5ee6957aa49f4f456b70874`. Only diagnostic pointers and interface wording/bookkeeping change.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-codex-v1.prompt.stdout.txt) `9bf84a110b060e1a399d1f91e14f2eea8c72b1f97aae64d38ca25a6efa9b72aa`: gpt-6.1-sol/max/read-only, every mathematical claim ACCEPT, packet0F/0M/2MINOR fixed in v1.
- [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-claude-v2.prompt.note.md) `b2cab1e5a7585277a2422e4f96f3a6d35e127f081d78b1c6ffab9cbaf1173175`: claude-opus-5-5/max/no tools, every mathematical claim ACCEPT,0F/0M/4MINOR fixed in v2. No reviewer report is a mathematical premise.

## Parent independent checks

The freeze records the whole-proof read and verification of36ranges from20hash-pinned sources. For SG the parent independently re-derived the step gcd6 for e=t/e!=t, the k<=3 measure bound, the exact ordered product equality if k=3, and #both=#neither>=1 from two half-sized d-fibre supports omitting their own fibre. Thus k is1or2. Row certificates use the O/d support only, with i* weight0; the opposite-family light-fibre bound gives11/12<=5/6, impossible. CIS uses own-family subset granularity and5/6 saturation, forcing two disjoint2/6 pieces into a1/2 piece.

The parent also checked P3's t-first prime-to6 induction; both-family C2 budget; the T16 and ONE counts; the exhaustive FB endpoint cases and their k=2 product equalities/fifth-vertex contradiction; and the final diamond complement. FB supplies each family's DG/DG* four-subset hypothesis BEFORE applying it. No numerical computation, scientific probe or Lean replay.

## Scope and next boundary

This passes the full M13 written-correctness gate at the declared imported trust. It does not accept MK/R2MIX/M3R merely by attribution (their needed steps are re-proved), nor prove orientation(1,1), fullK6.2*, K7 or Sun(7). The fullK6.2* uniform proof has its own pending second-family review. This is a specialist regime exclusion, not a certified novelty, matched-SOTA, publication-ready, Lean or human-referee result.
