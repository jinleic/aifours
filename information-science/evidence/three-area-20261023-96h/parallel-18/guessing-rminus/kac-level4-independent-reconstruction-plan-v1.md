# Prepare-only independent reconstruction of the64 Kac level-four certificates

Observed immediately before this plan: `2026-10-23T15:23:06-0700`. Reviewer: InfoGuessingRminus, temporary assignment under peer-review-wave-eighteen-v3.json. My sole primary problem remains info-5 R-minus. Its scientific HOLDs are unchanged.

**PREPARE ONLY. No consumer import, compilation, smoke, algebra execution or certificate replay has occurred.** Source reading, input-format parsing and metadata hashes are permitted. The output here is an independently derived consumer design/source and an admission proposal, not a claim that any of the64 certificates passed.

## 1. Exposure, pinned contract and exact scope

I read the full v3 common contract and detailed entry; the complete producer source (437lines); complete canonical model, certificate-to-band implication, full band manuscript, invariant bridge, quotient bridge, selection, free-character note; actual certificate field/minor/tensor examples; the settlement scope and historical quotient/lowering definitions. The producer was read for required exposure and format, not imported or executed. This is supplied-proof review, not blind or model-family-independent review.

Observed SHA-256 pins match the assignment:

- producer `small_row_level4_v1.py`: `af9e001f44c518eb56ffd7649926fe57625045a49c2ebd6b3954cbdb8a13874f`;
- `canonical-level4-model-v1.md`: `9ab6cbf7bd3b39e17714e64e314452362ba5525d6bb152a8e7e6d36f6acec18b`;
- `certificate-to-band-v1.md`: `c1a2efb271a44b76d8fcdf5dbb214f891e7f0b945f5088ee33d2b99bb122a3ca`;
- `level4-band-candidate-v1.md`: `8b2fd9b4f2b4935e703689efd227ee96392053696b3bdded3e91e5921a9dfb73`;
- settlement: `b654d5b7ac2e181042727e92b1bfb4f9d1723fe690ea7bdad20a974f2154c82e`.

The consumer must cover exactly16 cells (r,s independently1,2,3,4+variable) and exactly four degrees `(2,2,4),(3,2,4),(2,3,4),(3,3,4)` per cell. Category4 denotes4+X or4+Y, never just specialization4. It verifies the finite premises of the conditional band implication, not the historical lower-level theorem, the invariant-only theorem, formal proof or novelty.

## 2. Mathematically distinct representation and free-space reconstruction

Use the positive-lift basis

`B=(v,u,w,p,q,x,y,z)`

where `v=e3`, `u=[e1,v]`, `w=[e2,v]`, `p=[e1,w]`, `q=[e2,u]`, `x=[e1,p]`, `y=[e2,q]`, `z=[e1,y]`.

Its adjoint matrix realizations are

`(E31,-E32,E21,H1,-H2,-2E12,2E23,2E13)`

and degrees are `(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)` at level1. This is a different ordered/scaled basis from the producer. The serialized producer letters are converted by the explicit diagonal/permutation map

`0->-x/2, 1->y/2, 2->z/2, 3->w, 4->-u, 5->v, 6->p, 7->-q`.

The four Levi actions are derived using the matrix-unit rule `[Eij,Ekl]=delta(j,k)Eil-delta(l,i)Ekj`, not the producer's dense3x3 multiplication helper. The consumer checks the defining Levi/weight relations on all eight basis vectors. Tensor actions use first-order substitution in the dual-number tensor algebra, not the producer's position-replacement helper.

**Source:** enumerate the canonical symmetric-wedge images

`F((b_i b_j) tensor(b_k wedge b_l)) = [b_i,[b_j,[b_k,b_l]]] + [b_j,[b_i,[b_k,b_l]]]`, `i<=j,k<l`,

in every required weight, keeping their actual bracket trees. Do not infer completeness from a saved dimension. Compute the full primitive tensor space as the kernel of the reduced **unshuffle coproduct** on every tensor word in that weight. Verify all F-images are primitive, independent, and exhaust that kernel.

**Target:** independently construct standard Lyndon bracket trees of length3 in the new alphabet; verify independence and equality with the primitive-tensor coproduct kernel. This is not the producer's all-right-normed-word generation.

Classical import: in characteristic zero the primitive elements of T(V) with its usual coproduct are precisely the free Lie algebra. A PBW proof identifies the enveloping coalgebra with the symmetric coalgebra on the Lie algebra; only linear symmetric tensors are primitive in characteristic zero. This gives exact completeness from the coproduct equations, not a count-only Witt inference. The canonical model's written F-isomorphism is read for context, but the consumer's whole-space check does not simply trust it.

## 3. Whole actual ideals, independently generated

For each q=1,2,3 and j=1,2 form the literal original generator `(ad v)^q(E_j v)`. Check it is nonzero and killed by both Levi lowerings. Generate its positive-Levi orbit under E1,E2. Because the seed is a lowest-weight vector, PBW reordering proves its full Levi span equals this positive orbit.

Only weights with a,b<=3 are required. This truncation is exact: E1/E2 only increase a or b, all V-leaf degrees are nonnegative, and every bracket in the required ideal formulas only adds them. An orbit exceeding the required box cannot contribute back to any source, target or lowered-parent degree. There is no truncation by sampled tensor rank or arbitrary total height.

Generate literal complete spaces independently from the graded ideal theorem:

`T3=[V,Q2]+Q3`,

`T4=[V,[V,Q2]]+[V,Q3]+Q4`.

Both inclusions are justified: these terms lie in the generated ideal; conversely a free Lie ideal generated in levels2..4 has, through level4, only these brackets. A `[L2,Q2]` term is already in `[V,[V,Q2]]` by Jacobi. All appropriate original modules from BOTH rows are included. Do not reuse the producer's recursive E1/E2-plus-V ideal routine.

For every serialized ideal basis, verify its tensors are in the independently reconstructed whole free space, are independent, and have exactly the same span as these complete T3/T4 spaces. This is not merely verification that selected supplied rows vanish. Check Levi-lowering stability into both degree parents and D3 stability into the actual target ideal, coefficient by coefficient on the entire open parameter cell.

## 4. Whole quotient-lowest completeness without free-lowest lifting as a computational premise

For the full independently reconstructed source basis B4, form the simultaneous map

`B4 -> (L4_parent1/T4_parent1) direct-sum (L4_parent2/T4_parent2)`

using the actual F1/F2 actions and independently reconstructed parent ideals. Its kernel is the full preimage of the simultaneous quotient-lowest space. Subtract dim(T4) after verifying T4 is killed in both quotient targets. This computes the actual quotient-lowest dimension **directly**, rather than repeating the producer's free-primitives-then-reduce selection.

Check every supplied primitive representative lies in the source, has both quotient lowerings zero (and verify its claimed free-lowest property), is independent modulo T4, and collectively has exactly this independently computed full dimension. Thus no primitive can be missing even if a free-lowest lifting argument were misapplied. The classical semisimplicity lifting statement remains valid written context, not an unchecked numerical substitution.

## 5. Actual original-row D3 via bracket recursion

Derive the leaf actor table from the positive lifts and `[f3,e3]=-h3`, `[f3,e1]=[f3,e2]=0`:

`Dv=-h3`, `Du=-r e1`, `Dw=-s e2`, `Dp=-s[e1,e2]`, `Dq=r[e1,e2]`, `Dx=Dy=Dz=0`.

Retain h3 as an independent actor, including A(1,1). Its action on full positive degree(a,b,k) is `2k-ra-sb`; never replace it by a Levi-Cartan linear combination.

Compute D3 of the canonical F bracket trees by the **recursive derivation rule**. A level-zero actor on the left acts on the other Lie factor; on the right it acts with the opposite sign. A non-leaf derivative is a genuine positive tensor polynomial. This differs from the producer's associative actor-to-the-right deletion algorithm. Extend linearly using independently solved F-coordinates of each supplied source tensor. Keep all constant,r,s coefficients before substituting1/2/3 or4+X/4+Y.

Independently check terminal-actor cancellation on every supplied/source-ideal tensor: first-order substitute each actor's scalar leaf functional in the dual-number tensor algebra and require the first variation to vanish. The check is performed; the argument is not used to silently discard an actor.

## 6. Quotient normalization and why a raw minor is not enough

A selected tensor-coordinate minor would be unsound on arbitrary lifts modulo T3. Therefore independently transform the COMPLETE reconstructed target ideal to the serialized alphabet, compute its full lexicographic RREF, and use its annihilating free-coordinate projection. A quotient has the unique representative whose pivot coordinates are zero. Reconstruct every raw affine image by this projection and compare **exactly** with the supplied quotient_affine_images. Also check the supplied images lie in full L3.

The normal-form coordinates must agree with the packet interface; this is a shared serialization convention, NOT reuse of the producer's raw generator or ideal helper. All raw spaces, ideals, quotient kernels and D3 operations are independently generated first. Faithfulness of the quotient projection makes the selected coordinate minor a valid injectivity witness.

Build the selected matrix from these reconstructed images in the exact stated row/column order. Compute its full bivariate determinant by fraction-free **Bareiss elimination with checked polynomial exact division**, not the producer's recursive Laplace expansion. Compare the entire polynomial, not evaluations. Then verify orientation±1, every oriented coefficient nonnegative, and the constant strictly positive. Empty source uses determinant1. Fixed parameter rows must have no spurious X/Y dependence.

## 7. Definition-first consumer controls and strict parsing

The future one-shot must invoke the actual consumer paths on copied in-memory mutants, without changing any frozen author input:

- perturb one coefficient of a source primitive tensor: fail the primitive-coproduct/Lie membership gate;
- remove a genuine source/target ideal basis row: fail whole-ideal span coverage, not just a status flag;
- alter a nonzero affine image component: fail the reconstructed ORIGINAL-row quotient-image equality;
- transpose the actual r,s row in the reconstruction while keeping the off-diagonal cell: fail actual original-row ideal stability/image validation;
- alter determinant coefficient, and separately flip orientation: fail determinant identity and positivity gates respectively;
- missing degree, missing cell, duplicated degree/cell: fail the real exhaustive64-record coverage gate;
- truncated/malformed JSON: fail the real strict parser, with duplicate keys and unsupported fields refused.

A mutation that unexpectedly validates or fails for an unrelated exception is a failed control, not PASS. No assert-only gate is allowed; every gate raises an explicit typed error with a named reason. No optimization/debug assumption may disable validation.

## 8. Bounded runtime preparation, NOT admission

Prepare one stdlib-only process/thread; no children, network, external library, producer import, configuration or dependency changes. Request an internal cooperative bound no greater than600seconds. Signals set a cooperative stop flag; finite loops/linear and polynomial elimination check it, and the consumer writes an INCOMPLETE/ERROR settlement rather than a false success. Outputs use a freshly exclusive directory under this info-5 root only. Record source/interpreter pins, all64 certificate hashes plus launch/settlement metadata, observed start/end, PID/PGID, elapsed time and honest RSS metadata.

Memory is bounded by degree<=4 tensor supports (at most8^4 words), small canonical weight spaces, a single cell's reconstructed ideals, and selected minors of size at most8 for these input claims. Cache immutable free-space data once; release per-cell record contexts. Any larger/different claimed dimension is rejected, not used to enlarge the run. Resource estimates remain proposals until parent audit/fresh aggregate observations.

## 9. Independence and limits

Achieved design independence: different positive-lift basis; coproduct-kernel completeness; canonical symmetric-wedge source and Lyndon target; literal Q-module/T3/T4 generation rather than producer ideal recursion; direct quotient-lowest kernel rather than producer free-primitive selection; recursive original-row bracket lowering rather than associative deletion; Bareiss rather than Laplace determinant; and real strict consumer mutation paths.

Not achieved: blindness to producer source, different model/vendor, a formal kernel, new classical PBW/Levi proofs, or independent acceptance of the inherited lower-level band/invariant theorem. The exact positive elimination, full-realization convention and ideal/Levi interpretation are shared mathematical definitions/imports that were read, not hidden independence claims. Future success verifies only the64 finite certificate premises; stage3 written import composition remains separate.
