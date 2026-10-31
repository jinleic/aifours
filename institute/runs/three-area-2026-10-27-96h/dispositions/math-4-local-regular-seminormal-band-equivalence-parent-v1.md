# Locally regular bands and the seminormal identity

**Disposition: same-harness written support for the corrected composite, conditional on the named classical free-band input.** For every nonempty band B, the following are equivalent:

1. Every local monoid `eBe` satisfies the regular-band identity `xyxzx=xyzx`.
2. B satisfies `abcda=abcacda` for all a,b,c,d (the candidate's stated seminormal convention).

This identifies the two varieties at these **displayed identities**. It does not establish an embedding, a canonical SEP/R/L construction, the printed Q1/Q2 interfaces, the historical terminology's provenance, novelty, a human or independent-model-family review, or a formal/kernel proof.

Native clock observed before composing: **2026-10-29T07:17:56-0700 PDT**; not a file-creation time.

## Parent reconstruction and correction

For `2⇒1`, e is the identity of `eBe`, which is closed and idempotent. Substitute local elements x,y,z for a,b,d and e for c in `abcda=abcacda`: the result is `xyzx=xyxzx`.

For the other direction the proof uses the all-band content absorption `XYZ=XZ` whenever `cont(Y)⊆cont(X)=cont(Z)`. The original source's statement that `X(XY)X=X` alone forces X and XY to have the same R-coordinate is false as a rationale: every pair in a rectangular band satisfies that equation. The [additive erratum](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-local-seminormal-band-content-rationale-erratum-v1.md) supplies the missing idempotence equation `X(XY)=(XX)Y=XY`. By the named Green–Rees content/D-class theorem, X, XY and Z lie in the same rectangular D-class, so `X(XY)Z=XZ`; the preceding equation turns its left side into XYZ. The [cited source](https://www-users.york.ac.uk/~varg1/2023_11_08_York_Semigroups_Computing_in_Free_Bands-corrected.pdf) also states the exact content rewrite on slide 18. Parent read that statement; neither the original Green–Rees proof nor the complete rewriting-system theorem was re-proved here. The original LF26 finding remains a historical MINOR, not a counterexample to the corrected composite.

Use the regular identity in two actual local monoids: first `e=c`, with local elements `cac,cbc,cdac` and common contexts `ab` / `da`; second `e=bc`, with `(bc)a(bc),(bc)(ac)(bc),(bc)d(bc)` and contexts `a` / `da`. Every e is idempotent in a band and every displayed element is literally of the form eue. The first local equality reduces by the stated square and content rewrites to `abcacda=abcacbcda`; the second reduces to `abcda=abcacbcda`. Transitivity yields the displayed seminormal identity. The 21 square contractions and two content steps are separately enumerated in the review; no cancellation, global regularity or identity outside the local monoid is assumed.

## Evidence and chronology

Parent read the complete [erratum](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-local-seminormal-band-content-rationale-erratum-v1.md), SHA-256 `dfedbf04821a2e60259e2d34631f336178ed73f867e79373d888926f4cb1262a`, before the complete 118-LF [candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-20261028-local-regular-seminormal-equivalence-v1.md), SHA-256 `bf7af7afe0440fda2774231c99577fa1d36ebf4b12f70628eddc380a162663ee`, and read the author's 57-LF replay as text only. Parent read the complete 196-LF [f144 review](../review-waves/f144-band-local-regular-seminormal-equivalence/review-v1.md), SHA-256 `768eee97386e4c933f3a968829b9437b27998c169cbca3969616f91801ae80b9`, and [manifest-v2](../review-waves/f144-band-local-regular-seminormal-equivalence/manifest-v2.json), SHA-256 `843b051c235415a7e5faed2cd9a36e59737770a1c6b05acafc4c2c5b11a46344`.

The reviewer read the original under v1 **before the erratum existed**, identified the rationale defect independently, then read the erratum and reassessed, and later read the corrected composite in declared order. This chronology is not a retroactive before-source receipt. The reviewer found 0 FATAL / 0 MAJOR and one historical MINOR repaired by the additive correction. Its own controls checked every literal transition and enumerated 698,603 labeled bands through order six; the [assurance receipt](../review-waves/f144-band-local-regular-seminormal-equivalence/reviewer-f144-assurance-v1.json), SHA-256 `e9c2091901908b3d7bb1e9dcd8df47341f7002736bbb4b4c2664fcfb69c07b8a`, binds the inputs and finite examples. Those bounded checks do not establish the universal theorem.

The review preserved its failed first mutation and invalid first enumeration tally; only corrected controls are used. Optional square-only searches were INCONCLUSIVE, not a disproof of the classical-import argument. The reviewer disclosed scratch files and compiled executables under `/tmp/f144-build/`, outside its assigned directory; they were not deleted. No historical held outcome is rehabilitated.
