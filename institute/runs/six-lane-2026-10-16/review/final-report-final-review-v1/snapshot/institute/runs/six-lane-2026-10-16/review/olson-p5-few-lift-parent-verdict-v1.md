# Olson: p=5 lift of INV*-FEW and OLSON-FEW — parent verdict v1

Recorded at 2026-10-18T10:45:38-07:00.

**CORRECTNESS-ACCEPTED at the restricted scopes below.** This closes the earlier Claude M1 on the p=5 consequences, not unrestricted INV*(5) or ordered Olson. The p=5 input C5 is computer-assisted finite exact; no Lean proof or novelty claim is made.

## Accepted statements
Let p≥5 be prime. Define o_F on the maximal cyclic constant reflection blocks (split a reflection run whenever its value changes).

1. Every length-(4p−2) avoider over D_2p with o_F≤4 has all rotations in one nonzero pair {ρ_c,ρ_−c} and every maximal cyclic reflection run constant (INV*).
2. Every word of length 4p−1 over D_2p with o_F≤4 has an increasing-index identity 2p-subword (OLSON-FEW).
3. The previously accepted alternative bound 5·o_F≤2p+4 is unchanged. These bounds may be combined by **OR**, not by an added hypothesis.

The new content is p=5, o_F=4. For p≥7 and for o_F≤3 the preceding verdict already applies. The number of odd constant blocks is not the number of reflection runs.

## Text and evidence
- Text of record: [proof-FEW-p5-lift-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-FEW-p5-lift-v3.md), SHA256 `aa2fb35092e8eb7621772428925898f5f000584cd9ff069004afc8e353bcb9cb`, read through the mandatory wording overlay below.
- [C5 / ROT-o4 at p=5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-p5o4-parent-verdict-v1.md), SHA256 `92d35e67b811ffefdb6eb802fb428cf1e098f20ffe87b0aa12205fb0f5d78db0`.
- [Existing few-odd verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-fewodd-parent-verdict-v1.md) and [part(b) addendum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-fewodd-parent-verdict-v1-addendum-1.md) retain their accepted imports and limitations.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5-few-lift-v3-codex-v1.note.md), SHA256 `827085f7f02c8e40ad1c17a9c89b2dd186250730f4a3e44c2df40f082cd4fc32`: ACCEPT, 0 FATAL / 0 MAJOR / 0 MINOR; former M1 discharged.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5-few-lift-v3-claude-v1.note.md), SHA256 `6ca1e28a49b4410311ce30c3e93f10f4ade7597b6c1098914fe9e5e2fc33ca88`: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 5 MINOR, citations and wording only. It independently checked parity changes, cyclic boundaries, every call and its scope.
- [Review snapshot](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5-few-lift-v3-review-v1/manifest.json), SHA256 `fe783bad04f3bb56f38140d5a7eeffd3a0a39bf3a9bc2ca790e262e238eadb8e`: exact inputs to both reviews.

## Parent derivation and scope checks
C5 supplies the o_F=4 rotation case at p=5 without assuming constant reflection runs. ROT-o2/o3 supply the smaller cases; o_F=0 is impossible. REFL-few-odd applies to the same length18 word because o_F≤4≤5, yielding INV*.

For a length19 word without an identity10-subword, every deletion also avoids. With at most two rotations, F≥17 and F−o_F is even and ≥14, yielding at least seven disjoint equal-reflection pairs. Five pairs suffice in a cyclic frame; conjugation returns the identity to original index order. Otherwise deleting one rotation cannot increase o_F: the only change is one fusion, dropping the odd-block count by zero or two. Two separate deletions leave a third, nonzero rotation in common, identifying their nonzero ±pairs. Every original rotation is in one deletion, and any adjacent unequal reflections persist after deleting a rotation. Thus the original word is RGR and the accepted RGR-LONG(5) applies. The optional odd-block deletion case lowers o_F by one and also stays within scope. No deletion from an even reflection block is used.

Parent read and checked the lift §§3–4 against INV*-FEW v3 and OLSON-FEW v3, in addition to both independent reviews. The original C5 computation and accepted theorem statements remain imports here; this is a proof-composition check, not a new finite replay.

## Mandatory wording overlay (Claude MINOR1–5)
This overlay changes no theorem, proof step, call or bound; the source remains immutable.

1. At lift lines54/57, ROT-o3-v4 and ROT-o4-v4 are **errata successors not pinned by the cited older parent verdict**. Acceptance here imports the scoped statements of the parent verdict, not an inferred acceptance of those whole v4 files. For the ROT-o4 statement at line84 cite the o3o4 verdict line9.
2. In the search table, INV*-FEW line146 belongs to row1 (a diff copy of its statement at line22), not row3 (the exclusion text). Search tables are corroborating metadata, not premises.
3. For lines157–161 use the accepted REFL/K0*/small-k verdict statements for prime scope; for line166 use EGZ and lowodd verdict lines9/32; for line193 use the explicit fusion derivation rather than the absent review quote; for line236 use the complete-claim Claude A1 reduction. No unseen source or search supplies a new hypothesis.
4. At lines206–207 explicitly insert the common-rotation argument: a third rotation x3 lies in both deletion words; its value t≠0 forces {±c1}={±t}={±c2}. Every original rotation belongs to one of the two deletion words.
5. Replace the awaiting-Codex-only status with: **both CLI reviews above are complete; this parent verdict decides acceptance**.

## Provenance and navigation notes
- The worker's lift v1 contained an invented hash suffix and an unperformed-search claim; both were caught before submission. v2's search coverage description was also repaired before submission. Neither earlier version is evidence for this acceptance; v3 and its pinned reviewed inputs govern. The failed drafts remain preserved.
- The former C5 verdict's relative RESULT-v1 link mistakenly included an extra `review/` segment. The correct target is [/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5o4-parent-replay-v1/RESULT-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5o4-parent-replay-v1/RESULT-v1.json), SHA256 `d823a969064fbf473ea9ab8288b487dbd75c3b68608e857fb3ae6aa7e9efddf1`; its [addendum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5o4-parent-replay-v1/ADDENDUM-v1.json) supplies provenance and fresh rerun evidence. This corrects navigation, not the accepted computation.
- The p5 worker result note's errata successor is [/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-o4-p5-finite-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-o4-p5-finite-v3.md), SHA256 `3a2acf7bd7edae272410f3a7816a0c7b49ba596519fda1ada5465c07a6a0e5c9`. Its downstream lift is accepted only through the scope and overlay here.

**Still open:** avoiders and length-(4p−1) words outside both stated odd-block bounds; full INV*(p); ordered Olson over D_2p and over arbitrary finite groups. The historical D10 census is unused.
