# Peer reconstruction — auxiliary coherent merging, not unrestricted P44

Observed completion clock: **2026-10-23T14:19:05-0700**. Reviewer: PhysicsDepol4, temporarily assigned by `peer-review-wave-eighteen-v1.json`. Ordinary in-harness written reconstruction with a supplied author proof; not blind, cross-vendor, human or formal review. No scientific executable was used.

## Snapshot and verdict

Complete source read: `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/proof-auxiliary-compression-no-go-v1.md`, lines 1–193. Observed SHA-256:

`40a09adc5773df89e3dc26fa5bbec2958efd1e9e881a71638bc25c3de88d346a`.

This equals the parent's assigned pin. Also read the actual selection/definition/import boundary in the author's `selection-v1.md`.

**Verdict: NO FATAL, MAJOR or MINOR mathematical defect found at the stated restricted scope.** The displayed R(u,v), for all complex u,v including zero, is PPT with Schmidt number exactly two. This excludes that auxiliary-only merge mechanism and further local filtering/convex mixing of its outputs; it does not exclude a general 4x4 PPT state or a 5-to-4 filter mixing a core level into the discarded direction.

## Reconstruction rather than verdict echo

### 1. Source interface and normalization (source lines 7–40)

Read the primary [Krebs–Gachechiladze 2509.07086v1](https://arxiv.org/html/2509.07086v1), Theorem 5, the actual Fig.1 image, Eq.(11), core vectors/weights (23) and Supplement E. The core vectors are exactly `(00+11+22)`, `(01+12)`, `(10-21)`, 02,20 with weights 1,1,1,3,3. The primary core-coordinate display (24) reparametrizes the sign of its c coordinate; it is not a reason to flip one occurrence only. The author's vectors agree with the primary vector definition and main Eq.(11).

The diagram has the three parallel extensions joining 20 to33 and 02 to34, with the compensating product loops. Sending Bob3 to u3 and Bob4 to v3 gives precisely the displayed d_v,e_u and the coefficients `3|v|^2` on03 and `3|u|^2` on23. Keeping Bob0,1,2 fixed makes the map rank4 exactly when (u,v) is nonzero; the (0,0) endpoint still produces a valid 4x4 matrix of smaller local support.

Independent trace count: core norms contribute 7; d/e vacuum components contribute 6; f/g contribute 6; the two 33 contributions and h/j contribute `6(|u|^2+|v|^2)`. Total is `19+6(|u|^2+|v|^2)>0`. Positivity follows directly from the positive projector sum. No source SN3 theorem is needed for this new restricted no-go.

### 2. Entrywise PPT and conjugations (lines 52–69)

The six nontrivial core coherences move under Bob transpose as follows:

- 00/11 gives01/10;
- 00/22 gives02/20;
- 11/22 gives12/21;
- 01/12 gives02/11;
- 10/21 gives11/20 with its minus sign.

The core 02/11/20 block is therefore `[[3,1,1],[1,1,-1],[1,-1,3]]`. Expanding `P(02+11-20)+2P(02+20)` gives exactly that block; the remaining positive projectors give precisely the other blocks and 00/22 diagonal entries.

For the complex extension, the coefficient `conj(v)` at `|02><33|` becomes `conj(v)|03><32|`. Thus it pairs correctly with `P(|32>+conj(v)|03>)`, not with v in that ket. Similarly the u term gives `P(|30>+conj(u)|23>)`. Their unused 33 diagonal is exactly `3(|u|^2+|v|^2)`. The claimed positive decomposition of the partial transpose is correct for arbitrary phases, not only real u,v.

### 3. Both exact twelve-character averages (lines 71–157)

For each average the seven exponent pairs reduce modulo (4,3) to

`(0,0),(1,0),(2,0),(0,1),(2,1),(2,2),(0,2)`

in some order, all distinct. The finite geometric-series identity therefore removes every off-diagonal character term. This is an exact finite decomposition, not an experimental sampling claim.

For M_A, direct row expansion gives

`z^2 row0 -z row1=(0,-z,1,v/w)=row2`,

`w row0=(w,0,w/z^2,v/z^2)=row3`.

For M_B it gives

`-z^(-2) row0 +z^(-1) row1=(-z^(-2),0,1,u/(z^2 w))=row2`,

`w z^(-2) row0 -w z^(-1) row1=(w/z^2,0,-w,-u/z^2)=row3`.

Hence each averaged vector has coefficient-matrix rank at most two. Reconstructing the averaged diagonals gives exactly A_A and A_B in lines 111–112 and 149–150. Subtraction from R leaves respectively `(3|u|^2-|v|^2)P(j)` and `(3|v|^2-|u|^2)P(h)` as the only potentially negative coefficients. All other residual terms have positive coefficients and Schmidt rank at most two.

The deterministic branch `|u|>=|v|` satisfies the first regime, and its complement satisfies the second; no division by u or v is used. The ratio regimes overlap and cover every complex endpoint, including zero. Normalizing each nonzero term after division by the positive trace gives a genuine convex decomposition with weights summing to one.

### 4. Exact SN2 lower bound and witness consequence (lines 159–179)

Projecting onto the core 3x3 block removes every extension except the original 02 and20 diagonal components, leaving R3 exactly. Its range has the displayed coefficient matrix `[[a,b,d],[c,a,b],[e,-c,a]]`. A rank-one such matrix must satisfy both `a^2-bc=0` and `a^2+bc=0`, hence a=0 over C. Therefore all product vectors in the range are orthogonal to a nonzero supported vector a=(00+11+22). A separable positive operator's range is spanned by its product summands, so R3 is entangled. This proves SN>=2, not merely SN<=2 for R(u,v), including the (0,0) endpoint. The upper decompositions establish SN<=2, hence equality.

A two-block-positive Hermitian witness has nonnegative expectation on every term of either decomposition, so it cannot have negative trace against R or its normalization. The witness conclusion is correctly restricted to this state family.

## Trust, novelty and significance limits

The reconstruction uses elementary finite-dimensional matrix/range identities, Schmidt rank and root-of-unity orthogonality. No solver output, unobserved eigenvalue, external model, proof assistant or finite numerical replay is imported. The primary's Supplement E already establishes an intermediate endpoint; the uniform complex merge theorem is a stronger scope than that endpoint, but literature-wide novelty was not established here.

This review does not certify an unrestricted P44 negative, existence of a Schmidt-number-three witness, completeness of all 5-to-4 compression mechanisms, or a solved book chapter. Parent integration/acceptance remains separate.

Returning now to physics-2's own depolarizing-majorization residual.
