# Addendum 001: inherited simple-pole falsifier and repeated-pole distinction

Before-creation clock observed: **2026-10-23T13:09:24-07:00**. This is a numbered addendum to the immutable `proof-repeated-pole-PH-v1.md`, SHA256 `ae4d983da5de5f897b262c92dd7594aac1905e2cdfcc6b6f8b5cb9e43b89bb6f`. It implements the parent's explicit comparison requirement without changing the pinned original. No scientific execution occurred.

## 1. Required baseline substitution

Substitute r=q=1 in Theorem A. Then L=ceil(q/r)=1, N_0=3, and its exact-degree criterion is

    beta <= 1/sqrt(2L+1)=1/sqrt3=cot(pi/3).

This exactly reproduces the classical order3 threshold for H_{1,1} and the n*=3 case of the already internally accepted simple-pole all-n statement. It is a **known-achievable positive control and a free falsifier**, not a new scientific result. The threshold endpoint is included in both statements.

The lower-bound argument likewise specializes correctly: the sole irreducible three-state block has shifted spectrum0,-d+ib,-d-ib; its trace-square inequality is 2(d^2-b^2)>=4d^2/3, hence b^2<=d^2/3. The upper-bound construction at equality is the familiar three-state cycle (the shifted nonnegative spectrum is gamma,-d/3+ib,-d/3-ib with gamma=2d/3); no discrepancy or new simple-pole claim remains.

## 2. Why the degree5 threshold is not cot(pi/5)

H_{1,1} has three distinct simple poles: one real pole and one conjugate pair. The old all-n minimum n*=min{n>=3:beta<=cot(pi/n)} concerns representations of that SAME three-pole transform, possibly with additional hidden eigenvalues. Its cyclic spectral-angle bound only needs to accommodate one conjugate pair.

H_{1,2} is different: it has one real pole and a conjugate pair EACH OF MULTIPLICITY TWO. An order5 representation has no room for hidden eigenvalues. Its characteristic polynomial is exactly the degree5 denominator. Every irreducible Metzler diagonal block requires a real algebraically simple Perron eigenvalue; because only one real eigenvalue is available, all five eigenvalues lie in one irreducible block. Thus this block must accommodate TWO repeated nonreal pairs simultaneously. Its shifted trace-square obstruction is

    4(d^2-b^2)>=16d^2/5,

which forces beta<=1/sqrt5. This multiplicity/trace obstruction is stronger than the generic single-pair angle bound for a five-state generator. There is no reason to substitute n5 into the old three-simple-pole formula and expect an exact threshold for this new transform.

The general Theorem A makes the distinction structural: with r real-pole occurrences, there are exactly r irreducible blocks at algebraic degree; q conjugate-pair occurrences must be distributed among them, forcing at least ceil(q/r) pairs in one block. Its criterion depends on that occupancy, not just the total state dimension.

Therefore the degree5 threshold1/sqrt5 and the old simple-pole cot(pi/n) pattern are not contradictory. A naive extension of the old single-monocycle construction also cannot represent a repeated nonreal pole: its logarithmic-derivative sum has a strictly nonzero imaginary part at every nonreal root, as proved in the original manuscript §8. The new multiple-feedback construction explicitly changes the representation rather than pretending multiplicity is free.

## 3. Delta and verification wording

The inherited r=q=1 case earns no new-coverage or priority credit. The scoped delta is repeated nonreal poles, the exact all-(r,q) algebraic-degree criterion at the named classical theorem import, and an actual super-degree minimum6 interval for H_{1,2}. The subsequent PH-existence-threshold and order-blowup manuscripts are separate candidates, not consequences already accepted by the earlier order5/6 peer review.

The preceding comparisons are written symbolic substitutions and matrix reasoning, not numerical assays. No new Lean/kernel, cross-vendor or human acceptance is claimed. Correctness review and novelty comparison remain distinct.
