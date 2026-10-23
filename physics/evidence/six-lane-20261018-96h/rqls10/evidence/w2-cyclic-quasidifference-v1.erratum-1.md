# Erratum 1 to evidence/w2-cyclic-quasidifference-v1.md (sha256 7f224d30da658d69f4371226505cdefd4fdd13eec700c5f7ded9538bd865875a)

Recorded 2026-10-18T23:39:03-0700. Prompted by the parent's scope note (IRC, after reading W2). The original file is unchanged.

**Withdrawn.** In Lemma 5's consequences, the sentence "... and no maximal Z_7 + 3 configuration is a continuous
deformation of a classical one" is withdrawn. It does not follow. The ansatz only requires U q_p to be *parallel* to
q_(g.p), so a classical Z_7 + 3 configuration (vectors = computational basis rays, U = shift on the seven finite
symbol vectors) admits U = shift (+) diag(omega^m1, omega^m2, omega^m3) with distinct 7th roots on the three fixed
basis rays e_1, e_2, e_3. Then the eigen-multiplicities are already (2,2,2,1,1,1,1), E_mk = span(f_mk, e_k), the
corner vector of every cell with classical symbol inf_k is e_k in E_mk, and each mate class of the corner collapses to
a single ray (consistent with Lemma 5's labelling, with the corner rays not distinct). Such classical points lie in the
closure of the forced-form ansatz, and nothing in W2 excludes maximal configurations near them.

**Unchanged.** "The classical situation with U = shift (+) I_3 (multiplicities (4,1,1,1,1,1,1)) is never maximal" is
correct for that U. Lemmas 1-7 and Proposition 4 are unaffected.

**Consequence for the plan.** Classical Parker-type points with a forced-form U are a legitimate initialisation for
the numerical assay: a local tangent-space (Jacobian kernel modulo gauge and representative phases) computation at
those points, followed by continuation along any excess kernel direction while monitoring corner/orbit ray
separation. This is added to the W4 assay design (v2) and is not excluded by any lemma.
