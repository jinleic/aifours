# RQLS10 WH5⊗C2 — parent verdict v1

Recorded 2026-10-21T04:42:37-0700 (`/bin/date`). **CORRECTNESS_ACCEPTED_SCOPED_PARTIAL (restricted ansatz only).**

## Accepted statements (all inside (H) only)

- Theorem1: (H)⟺120 real equations (R1),(R2) across β_Z,β_X,β_T with couples M_Z,M_X,M_T; counts, no rank claim.
- Lemma2: X_r^*X_r=I/2; flat-plane reformulation.
- Theorem3: same-orbit rays distinct; cross-orbit equality↔identical25-ray sets; 30 forced cross-orbit zeros; maximal cardinality⟺120 strict inequations.
- Theorems4–5: unique antiunitary couple maps A,B,C with A_(s→r)=−A_(r→s); (H)⟺flat P with (F),(O); every solution X₀₀=V/√2, X_r∈{AVJ,BVJ,CVJ}/√2, any isometry V with VV^*=P (V-independence proof recorded in erratum v2).
- Theorem6/Lemma7/Corollary8: triangle Kramers condition Θ²V=−V; WH-type triangle maps (all three) excluded.
- Lemma10/Corollary11: the unit vectors unbiased to β_Z,β_X,β_T are exactly the unimodular multiples of ψ^k_m,k∈{1,2,3}; flat planes containing one are MUB-pair planes; orthogonal span(u,W_wu) flat planes likewise (orthogonality essential).
- Proposition12/Theorem13/Corollary14: couple partners of MUB-pair planes are MUB-pair; no three representative planes are MUB-pair; hence in EVERY (H)-solution of ANY cardinality no representative plane is a MUB-pair plane, no representative plane contains a vector unbiased to all three bases, and no orthogonal span(u,W_wu) occurs. Import-free (Haagerup/Chebnotarev not used).
- Section9: exact remaining system P1–P4 (P1–P4⟺(H)+100 distinct rays).

**Open:** non-MUB-pair flat-plane classification (C1)–(C3); any witness; any ansatz-wide no-go; **unrestricted maximal-cardinality1-RQLS(10) remains OPEN/UNKNOWN** (Zhang–Cao v2 still lists v=10 among its 17 exceptions). No cardinality of (H)-solutions is determined.

## Verification

- Codex gpt-6.1-sol/max read-only:0F/0M/1m (interface scope propagation, disposed by v1 errata chain). Receipt `0a604eeb0b2d971b373410cf58d537d041c5952115b1550b6f34a13e285aba33`.
- Claude claude-opus-5-5/max no tools:0F/0M/6m (wording/summaries, disposed by erratum v2). Receipt `0b520f9a64edac0f802408babe6357d521a4db381088f031893534711438d2dc`.
- Parent written check (6abf006ab3369d36e5235a4f73787063c141b1afdfb161be30e434adc5d449a6) re-derived the chain, including frame-invariance under conj(detU) and the odd-5-cycle intensity argument.

Process: single-author lane worker, scope frozen before derivation; historical float probes explicitly non-premises. Written/model acceptance only: no Lean/kernel, human review, novelty/first or runtime claim; no computation used for this acceptance.

| Artifact | SHA256 |
|---|---|
| [01-wh5-c2-exact-system-v1.md](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10/continuations/wh5-c2-written/01-wh5-c2-exact-system-v1.md) | `aa90e2eb1fd9e44e1a49dbff89e42a7805960a19d546d84882764045dfd1a6af` |
| [01-wh5-c2-exact-system-v1.erratum-1.md](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10/continuations/wh5-c2-written/01-wh5-c2-exact-system-v1.erratum-1.md) | `bd804ee1420ba0be15c8da78412e930aab648b6ad3486dbac67495be2ed43452` |
| [rqls10-WH5C2-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-parent-erratum-v1.md) | `b2288fa267ad8002b414bc45d69e9ea7ce07650241a7ebef0a4e3fde9e944f33` |
| [rqls10-WH5C2-parent-erratum-v2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-parent-erratum-v2.md) | `686fa062154e2b62608e8678a80e90739b06b465d5f2500368b69b05ffe816da` |
| [rqls10-WH5C2-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-parent-written-check-v1.md) | `6abf006ab3369d36e5235a4f73787063c141b1afdfb161be30e434adc5d449a6` |
| [rqls10-WH5C2-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-codex-v1.prompt.stdout.txt) | `b8b5f294b0b0d607c451ab42d4ffa95fde6cc209280f0895eb59a470845f334f` |
| [rqls10-WH5C2-claude-v2.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-claude-v2.prompt.note.md) | `2db0a58596b24026dc43ea03f1338f6a441000864f98e0fd9e14a0f0cb0c23b3` |
| [rqls10-WH5C2-review-freeze-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-WH5C2-review-freeze-v1.json) | `262f7c07753a15d032fe885a1be3f73c2d8e420af5e5a75e9f31f599a517e9f0` |
