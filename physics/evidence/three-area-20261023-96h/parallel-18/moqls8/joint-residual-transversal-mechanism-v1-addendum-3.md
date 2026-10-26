# Joint residual addendum 3: written survivor reduction and a large-component block barrier

Observed clock before this packet: **2026-10-25T04:16:23-0700 PDT**. Owner PhysicsMOQLS8. NEW additive, **AUTHOR-WRITTEN CANDIDATE ONLY**. This was derived by written reasoning after Main withdrew the eval exception. No arithmetic interpreter, enumeration program, symbolic/numerical computation, solver, replay or scientific process was used for this packet. Read addendum1 WITH mandatory assurance addendum2; the seven earlier eval cells remain disclosed and unadmitted, not verification for this work.

The four stratum exclusions and the projection definitions below refer to addendum1's WRITTEN proofs, not to its108-tuple computational table. Neither this packet nor those proofs have been independently reconstructed. No proof-kernel or novelty claim.

## 1. Written completeness of the two remaining stratum barriers

This section obtains the remaining parameter patterns by ordinary case analysis; it does NOT use an interpreter verdict. Write a_s, f_s, r_s, b_s, d and c as in addendum1. Its written lemmas give:

- 12<=a_s<=14, sum a_s<=38;
- a12 forces f4 or5; a13 forces f2..5; a14 forces f1..5;
- c<=d=38-sum a_s;
- c>=f_s(f_t+f_u-8) whenever positive;
- f>=4 with a13 or14 is excluded by the four per-stratum proofs;
- a14/f3 is excluded by the additional constant-aware proof;
- all-three-a12 is excluded by its separate written proof.

The arithmetic in those proofs is directly visible. For example the delicate six-space contradiction is

`(1/3)^2+[(11/2)-(1/3)]^2/10 = (40+961)/360 =1001/360 >990/360=11/4.`

The fourteen-cell contradiction is

`(7/16)^2+[(77/16)-(7/16)]^2/9 = (441+4900)/2304 =5341/2304 >5337/2304=593/256.`

The a14/f3 (or a13/f3 with d1) contradiction is

`(2/5)^2+[(11/2)-(2/5)]^2/10 =2761/1000 >2750/1000=11/4.`

These are displayed written rational identities, not a new run or an attestation of the prior eval cells.

### 1.1 Remaining f5/r3/b7

The selected a is12. It cannot have another a12 member:

- if the third span is14, then d=0; f5 plus the other a12 member's f>=4 forces at least one triple cell, impossible;
- if the third span is13, then d=1 and its f>=2; f5 plus f>=4 forces c>=2, impossible;
- if the third span is12, then d=2 and the third f>=4, again impossible (or use the all-a12 exclusion).

Thus both other spans are13, d=c=0. Their f-values can only be2 or3, because the a13/f4,f5 strata are already excluded. If both are3, the selected member's nine-point compression has

`tau=99/32`, `sigma<=1385/1024`, `rank>=9801/1385>7`

(the last strict inequality is `9801>7*1385=9695`). This contradicts b7. Consequently the ONLY remaining joint patterns are

`(a,f)=(12,5),(13,2),(13,2)`

or

`(a,f)=(12,5),(13,2),(13,3)`,

both with c=d=0. They are unexcluded necessary patterns, not physical constructions.

### 1.2 Remaining f4/r4/b8

Again the selected a is12. There are four possible other-span patterns.

**Other spans14,12.** Here d=c=0. The other a12 member cannot have f5, since its fixed count plus the selected f4 exceeds8. It therefore has f4. The a14 member cannot have f>=4 by the four-stratum proof, nor f3 by its displayed constant-aware contradiction. Hence its f is1 or2. Remaining patterns: (14,1),(12,4),(12,4) or (14,2),(12,4),(12,4), c0.

**Other spans13,13.** Here d=c=0. Each f is2 or3 after the a13 exclusions. Thus (f_t,f_u) is (2,2), (2,3) or (3,3). The present compression inequality does not exclude these for selected b8.

**Other spans13,12.** Here d=1. The other a12 member cannot have f5: f4+f5 would force c>=f_(a13)>=2>1. Hence it has f4. The a13 member has f2 or3. For f2, c0 or1 is not excluded. For f3, c0 is excluded by selecting that a13 member and applying the displayed 2761/1000>11/4 contradiction with m=b+d=11; c1 is not excluded.

**Other spans12,12.** Excluded by the written all-a12 theorem.

This recovers precisely EIGHT unordered joint parameter cases for the f4/b8 residual, counting the c0 and c1 versions separately, without using the108-tuple table as evidence. No line equations or unknown full mates are eliminated by this parameter list.

## 2. New complex uncertainty lemma: an actual zero-matching4 block is globally isolated

**Lemma Z4 (AUTHOR-WRITTEN).** Suppose the full physical two-sided degree3 bound holds in two ACTUAL selected-square line frames E,F, and their transition has a zero-matching4 block on a coordinate four-space A. Then EVERY actual selected-square vector is either wholly in A or wholly in A-perp. Thus A is an actual global coordinate component, of dimension4.

This statement does NOT require a small projector span. It is stronger than merely saying the original two bases preserve A. Its proof retains complex phases.

**Proof.** Relabel the four F vectors so that their E transition on A has its only zeros on the diagonal: U_ii=0, U_ij!=0 for i!=j.

A vector w in A with ONE E-coordinate has exactly THREE F-coordinates. If w has exactly TWO E-coordinates i,j, its F coefficients at indices i,j are both nonzero: each contains a single nonzero product involving the other E-coordinate.

Let k,l be the complementary indices. The restrictions of F_k,F_l to the E-coordinate pair {i,j} are nonzero, orthogonal two-vectors. Indeed their full inner product has terms ONLY at i,j: at k or l one of the two factors vanishes. Hence these restrictions are linearly independent over C. A nonzero w supported on {i,j} cannot be orthogonal to BOTH restrictions. At least one of its F coefficients k,l is nonzero. Therefore any two-E-coordinate w in A has AT LEAST THREE F-coordinates.

Now let v be an actual selected-square vector with nonzero A and A-perp parts. Its E support has at most3, so its A part has one or two E-coordinates. By the preceding paragraph the A part already occupies at least3 F-coordinates. Its nonzero A-perp part contributes at least one additional F-coordinate, since F preserves A. This gives F support at least4, contradicting the physical bound in the actual F frame.

Thus no actual vector crosses A. Since the original zero-matching block connects all four A coordinates, A is exactly a global connected component. QED.

**Important scope.** The lemma uses the degree bound in BOTH actual frames. It does not assert this for arbitrary external bases or a projection of other members. It is compatible with the quaternion r4 control: that control's zero-matching blocks already live in its actual isolated four-space.

## 3. New consequence: full3 blocks also cannot lie in a component of dimension>=5

**Lemma F3 (AUTHOR-WRITTEN).** In the same full physical setting, an actual full3 transition block can belong only to a global component of dimension3 or4. In particular an irreducible component of dimension>=5 has, in EVERY pair of actual line frames, only singleton, full2 and one-zero3 blocks; neither a full3 nor a zero-matching4 block occurs.

**Proof.** The zero-matching4 part follows from Z4. Suppose an E-to-F transition has a full3 block on A, and suppose the global component containing it has dimension>=5.

There must be an actual vector v crossing A. One E-coordinate in A would expand into all3 F-coordinates in A and at least one outside, impossible. Thus v has exactly TWO E-coordinates in A and exactly ONE outside, say e. Its A part has at least2 F-coordinates: otherwise it would be an F-axis, but every F-axis of the full3 block has three E-coordinates. Its outside E-axis must therefore have only one F-coordinate, or v would have F support>=4. Hence e is also an F-axis, up to phase.

Choose an ACTUAL line basis G containing v. In the E-to-G transition the block containing its three-coordinate support is either a3-block or a zero-matching4 block. The latter is globally isolated by Z4 and would force the entire component containing v and A to have dimension4, contrary to the assumption. Thus G has a3-block on B+{e}, where B is the two-coordinate part of A used by v. Let c be the third A coordinate.

Every other G vector has E support disjoint from B+{e}. Any such vector using c together with an outside coordinate would have one E-coordinate in A and hence at least3 F-coordinates there plus a nonzero outside coefficient, impossible. Consequently G contains the pure c-axis as a singleton.

Both F and G now preserve the four-space V=A+Ce. On V, F is a full3 block plus singleton e; G is a connected3-block on B+e plus singleton c. Their transition on V is CONNECTED: the G c-axis overlaps all three F A-rays, joining those rays; a G mixed vector with nonzero e and A parts joins the F e-axis to the same component. Its S3 block must therefore be zero-matching4. Applying Z4 in these actual F,G frames makes V globally isolated, again forcing the original component dimension4. Contradiction. QED.

No statement here excludes arbitrary three- or four-dimensional components. No real form is assumed. The conclusion is a representation restriction on larger components, not a classicality theorem.

## 4. What this adds to the two live residuals

For a13/f2, its residual dimension6 has span11. It cannot split into3+3 components: the imported local bounds would give span at least6+6=12. Thus it is an irreducible SIX-space. By F3, ALL its actual line transitions now have only singleton/full2/one-zero3 blocks.

For a13/f3, the residual five-space is irreducible (a two-component is prohibited); the same restriction applies.

For a14/f1, its seven-space has span13 and cannot split into3+4 (that would give span at least6+8=14). It is irreducible, with the same restriction. For a14/f2, the residual six-space has span12 and could be irreducible6 OR3+3; the latter is NOT excluded or relabeled as a six-component by this packet.

In particular BOTH remaining f5/b7 joint patterns necessarily involve an irreducible six-space b11, and possibly a second six-space b11 or a five-space b10. All these larger components are now restricted to the one-zero3/two/singleton transition representation.

The exact missing bridge is still substantial: absence of full3/zero4 blocks does NOT prove that all actual vectors share one coordinate two-space B with at most one fixed B-ray per outside coordinate. Such uniqueness and global channel coverage must be proved before invoking the existing channel lemma. Different overlapping one-zero3 blocks can a priori use different B-pairs or different factors at the same outside axis. The current proof does not classify or exclude that gluing.

Thus the remaining f5/b7 and f4/b8 strata remain OPEN. The new contribution is the complex Z4/F3 uncertainty reduction and the explicit written first-unproved step, not another enumeration. No catalogue result, native UNKNOWN, A10/A11 or full-family conclusion is altered.

## 5. Review boundary

Required hostile reconstruction: the complex two-coordinate support argument in Z4; F3's use of actual G frames and its connected F-to-G four-block; all component-partition alternatives when applying it. These statements were not part of v28-B's pinned source and have no inherited review verdict. A10/A11 are assessed separately without claiming old proof-stream replay or a blanket scientific launch exception.
