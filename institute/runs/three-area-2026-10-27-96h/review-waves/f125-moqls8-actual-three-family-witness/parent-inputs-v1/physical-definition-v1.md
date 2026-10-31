# Physical acceptance definition for the claimed three-family witness

Verify three actual quantum Latin squares of order8, all in the SAME physical cell coordinates. Every row and every column of each square must be an orthonormal basis of C^8. For every distinct pair of members, the64 same-cell tensor products must be an orthonormal basis of C^8 tensor C^8. All64x64 Gram entries, not only norms or edge constraints, must be checked.

The JSON quantum member has64 integer numerator vectors of length8 (row-major), each divided by the square root of its corresponding positive integer denominator_squared. The two classical members are8x8 label matrices with labels0..7 representing the eight standard basis vectors. Strictly reject malformed dimensions, nonintegers, duplicate/missing coordinates or invalid normalizers. Every necessary physical condition must be checked from the frozen witness alone, not a source catalog or solver.

Classicality is memberwise: one global output orthonormal frame with arbitrary per-cell phases. A pair of vectors in one member whose squared overlap lies strictly between0 and1 is sufficient to certify nonclassicality invariant under allowed phases, row/column permutations and a global member unitary. Verify the stated8 mixed cells relative to the supplied basis separately; mixed count alone is not a proof of nonclassicality.

Primary source is Ball and Simoens arXiv:2607.12933v2, Introduction definition of M(n), Table2, and Sections2.2/2.3. It defines a nonclassical SET (at least one nonclassical member is enough); the physical source correspondence and CURRENT/PRIORITY comparison still require a separate source audit, not the finite verifier. The registered original target is a FOUR-family alternative, so three families do not close it. No novelty or M(8) promotion follows automatically from a local PASS.

Independence: no author checker/producer code is supplied in this frozen verifier snapshot. Same-harness separate implementations only; no independent-vendor/human/formal protocol is authorized or claimed. Preserve failures and fixtures; no deletion.
