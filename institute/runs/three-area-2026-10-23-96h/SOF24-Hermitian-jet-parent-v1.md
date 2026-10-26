# SOF P24 primitive-Hermitian route — parent disposition v1

Clock actually observed before creation: **2026-10-23T13:45:37-07:00 PDT**. Governing qualifications: [verification](parent-verification-erratum-v1.md), [timestamps](parent-timestamp-erratum-v1.md).

## Decision

**The named primitive-Hermitian certificate route is excluded at the in-harness written-check level. P24 remains unresolved.** This is a `NEEDS-NEW-REPRESENTATION` disposition for that route, not a positive generic-stabilizability theorem.

The parent read the complete 143-line [author manuscript](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-SOF24-Hermitian-jet-obstruction-v1.md), SHA-256 `d3c41cb464dc898fe03a3d38d8bd03c628e5fd27f3c2e38f75817ae5dba95470`, and complete 71-line [mathematics-lane reconstruction](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/peer-review-info-SOF24-Hermitian-jet-v1.md), SHA-256 `7fea3487ee20ba0262dfa1f1b6b3dc27984822155a5bf092785dc7e582a07f48`. Both pins were observed with the clock above. The reviewer returned **0 FATAL / 0 MAJOR / 0 MINOR**.

## Exact supported implication

For a real 2-by-6 polynomial row matrix with rank two at zero and maximum minor degree eight, assume a seven-dimensional traceless-Hermitian subspace annihilates the first eight coefficients through the stated fixed-complex-structure bilinear pairing. Then a constant real rank-four plane makes the stacked determinant identically zero. Consequently the curve cannot satisfy P24's required complex nondegeneracy.

The parent written check and actual peer reconstruction cover:

- Real determinant-one polynomial row descent preserves the wedge, rank at zero and the coefficient-conjugate Hermitian jet, terminates without a zero row and yields degree sum eight.
- Nonzero H(0) has nonzero primitive projection; dimension seven forces the low jet into `span_R{I,H(0)}`.
- Complex-independent initial rows give a formal-unit inverse forcing the third complex components into `z^8 C[[z]]`; their degrees at most seven make them identically zero.
- Complex-dependent but real-independent initial rows admit the stated degree-preserving triangular normalization. The first perpendicular coefficients are `u,-iu`; the Hermitian lower block has coefficient `-u u*` at order `2k`. Before degree eight it cannot equal a scalar multiple of the two-dimensional identity, forcing `k>=4`, hence the balanced `4+4` case and a fixed complex two-plane.
- The fixed real four-plane, or a constant-row alternative, gives the actual real degeneracy certificate. The bilinear pairing is bound to the Plucker coefficient constraints, not merely analogous to them.

There is no assumption that a formal inverse converges. Coefficient conjugation does not conjugate z. The reduction covers all polynomial row-degree splits and every fixed orthogonal complex structure, not only the original monic balanced chart.

## Remaining target and next action

This excludes neither non-Hermitian real-avoidance kernels, z-dependent representations nor all degree-eight curves. It does not provide an empty real repeated-pole fibre, an eight-state plant counterexample or a universal stabilizing-gain theorem. The author must change the real-fibre certificate representation materially rather than rotate the same fixed complex structure or tune its coefficients.

No original Byrnes–Anderson theorem or the earlier source-sign example is a mathematical premise of this route obstruction. Novelty remains **NOVELTY_UNCLEAR**. No scientific execution, proof-assistant verification, external model call, publication or author contact occurred for this disposition.
