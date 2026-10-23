# PA19 ms09: empty-pair and forced-pair exclusions accepted

Recorded at 2026-10-19T16:09:27-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** TheoremsA/B and the fixed-profile skeleton exclusions b59,b67,b69,b70 are accepted as written mathematics. **PA(19,8,6) stays UNDECIDED.** No solver/Lean/human/novelty claim. No complete skeleton-list coverage or global nonexistence claim.

## Exact statements

For a 19x8 array over six symbols with at most one agreement per pair, five columns have profile(4,3,3,3,3,3) and three have profile(4,4,3,3,3,2). Q_c denotes each first-five column's quad, T(r)={c:r in Q_c}, and e counts rows with T empty.

- **TheoremA:** e=8 or9 is impossible. Exact pair saturation gives 5 Phi_5(e)+Phi_6(2e)+Phi_9(e)<=binom(e,2); the respective lower bounds29 and38 exceed28 and36.
- **TheoremB:** e=7 and two rows whose T-sets have size3 and whose two-element complements are not listed skeleton types is impossible. Each is forced into two pair blocks; their T-sets intersect, so those four pair blocks are distinct, but only three exist.
- F1-F5, Lemmas1-6 and the stated rescue implications are accepted at their literal conditions, read through all three parent errata. No unproved diagnostic compatibility or realization is accepted.

## Exact case binding

Skeleton file: `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json`; SHA256 `7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0`. Byte ranges are zero-based half-open.

| Case | Byte range | Entry SHA256 | Current delta |
|---|---|---|---|
| b59 | [3934, 4011] | `16beca8ac7fb52c0a0bef63d2c644ed1ec0669f2166e367c2fb9e409b1a2677d` | New current closure |
| b67 | [4594, 4684] | `6c0454e38f9b2ab0eed47be262eb4b9f227dbbaa084c1d4c1bde467bf8de9248` | New current closure |
| b69 | [4775, 4870] | `4b8864a4da6d996cfcf6e72a0d9db3861e1d8fef849c9d203165cbb6ddea38a2` | New current closure |
| b70 | [4872, 4975] | `77a101369c6d7058e7ea7333388eb036c2f98f5326df4bb465c9d82acaf5f662` | Previously closed; no count gain |

b59 satisfies TheoremB; b67,b69,b70 satisfy TheoremA. Parent read the proof in full, independently checked the saturation, balancing, excess/rescue and four-versus-three pair argument, and verified all14 raw source excerpts and both document pins. Each current b_index's skeleton_types/empty is JSON-equal to the exact skeleton bytes. b70 is absent from frontier-v9's unresolved list and already in its closure history. The aliases are not the identity. The original-frontier counts151 and current pre-verdict132 are not conflated.

## Independent reviews and text of record

- [Codex gpt-6.1-sol/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-structural-codex-v1.prompt.stdout.txt) `030746ef16283d3a6a112cb396c938c882f847317f1abc0bf820f0cac3d4a289`: every theorem/case ACCEPT; packet ACCEPT-WITH-FIXES,0F/0M/2m; fixes in parent erratumv2.
- [Claude claude-opus-5-5/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-structural-claude-v2.prompt.note.md) `9ca23df8e4b3ae867fcfbfb1472856fc983ff11df3552560d02a10c3428e5b70`: every theorem/case ACCEPT;0F/0M/6m; fixes/boundaries in parent erratumv3.
- [Proof](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/notes/ms09-empty-pair-and-pair-demand-proof-v1.md) `43dd4c42b151716e5b5ab0be6c50a576aa100380be42460a9e8eb345705cc439`; [manifest](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/review/ms09-structural-route-excerpt-manifest-v1.json) `40a6ac089ec74a35a25f8e644f713857aeeb9e3d92e9a760e3528d5412b46fb6`.
- Mandatory [erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-structural-parent-erratum-v1.md) `b93c2b54f9b8ab6b9ecbce5acbfab7ecb72cba39d6354aa2e4cf91e2e99b2086`, [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-structural-parent-erratum-v2.md) `9acdd422964ab00568ecf6bfd8facc5ead787d17a6acb0bb3f35f789cb6808bb`, [v3](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-structural-parent-erratum-v3.md) `f25d73aff8bfceb7dda264e3a56401e6905082e430c15c09b430fec44daaf899`.

## Authorized ledger consequence

The parent may remove exactly b59,b67,b69 from frontier-v9 (ms06=70,ms09=62,total132), producing ms06=70,ms09=59,total129. This is a whole fixed-skeleton mathematical closure, independent of placement-list/interval enumeration. b70 contributes no new closure. All historical solver UNKNOWNs, receipts, intervals and STOP/HOLD records remain unchanged; measured M2H views remain separate. Runtime remains HOLD.
