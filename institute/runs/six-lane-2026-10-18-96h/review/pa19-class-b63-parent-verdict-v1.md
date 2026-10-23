# PA19 ms09 class extension — accepted; b63 reduction partial; no count credit

Recorded 2026-10-21T09:27:41-0700 (`/bin/date`). **CLASS THEOREM CORRECTNESS_ACCEPTED; b63 REDUCTION ACCEPTED_AS_NECESSARY_PARTIAL_ONLY; NO WHOLE-CASE GAIN.** Governing: parent errata v1, v2, and v3 ([pa19-class-b63-parent-erratum-v3.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-class-b63-parent-erratum-v3.md)). Full bindings: [pa19-class-b63-parent-disposition-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-class-b63-parent-disposition-v1.json).

**Accepted — class theorem (H1∧H2 ⇒ no array):** all §1 general facts (171 = 5·21 + 3·22 agreement count, nine row patterns, five excess categories C3/C0/Q4/Q1/T2, I(r) = 7), Steps A–G, the symmetry group (relabelling P, S₃, the 3↔4 swap with both i values), Sections 3–4 including the unique perfect matching {e0v′, vv″} and the terminal contradiction in H_C for both i values. Verified twice by hand (parent check + both families). Covers only b65 among the 59 frozen-v10 rows — no duplicate credit (b65 separately excluded in v11).

**Accepted — 59 applicability decisions:** all 59 quoted entries, all 71 byte ranges (433-byte header, entry 70 ending at byte 4975, total 4977), all e values (H1 fails for exactly 55 cases, e ∈ [1,6]; among the four e = 7 cases only b65 satisfies H), all 59 V line numbers, and the Δ-selection of b63. Binding limits stand: hashes not recomputed by the family; membership proven, list completeness not.

**Accepted — b63 reduction at necessary scope only:** degrees (2,3,3,3,4), automorphism group exactly {id, 1↔2}, B1–B9 including the B9 terminal table (K_z = {z, e0, u1, va}, K′_A = {x, u2, vb, vc}, g's split {g, e0, vb}/{g, va, vc}), and the six exhaustive NECESSARY families (1–2 via G1; 3 via G2-C0; 4–5 via G2-Q1-(a); 6 via G2-Q1-(b)). None excluded, none realized: **no nonexistence claim**; b63/b66/b68 open as whole cases.

**Not accepted / permanent:** the original complete-nearest-case fallback stays UNFULFILLED (later F4/F5 leave families 1, 2, 3, 6 open); the three procedural/delivery MAJORs (pre-freeze derivation with outcome known; estimated 18:03:00 timestamp outside the observed 17:43:22–17:49:11 window; unmet fallback) are permanent, now independently confirmed by both families; "corroboration" for b59 is shared-provenance only; definition-to-encoder bridge is parent metadata, not theorem content.

**Count and status:** 128 (70 ms06 + 58 ms09, v11); PA(19,8,6) UNDECIDED. No novelty, human, Lean or runtime claim.

Verification: parent hand check + opaque 59-case byte/ID binding (`pa19-class-b63-source-byte-binding-v1.json`, 0 mismatches); first-family Codex (prior); second-family Claude 0F/0M math on (a), 0F/0M on (b), 0F/0M/2m on (c) with erratum v3 carrying both binding MINORs, the justification-gap repair and the nits; note binding re-verified (single complete assistant segment + trailing newline).
