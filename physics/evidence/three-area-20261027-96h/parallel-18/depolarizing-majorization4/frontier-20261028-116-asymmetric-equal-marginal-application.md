# An asymmetric GME application of the equal-marginal k3 candidate

**CONDITIONAL WRITTEN APPLICATION, NOT ADOPTED.** If the complete unreviewed result `frontier-20261028-114-equal-marginal-k3.md`, SHA256 `78dce15eedb3a2102d32802cb965538193a3719043dffe353016f10637f8ad72`, is valid, then it establishes the original k3 comparison for the actual pure GME state below at every physical noise and every complex rank-three test projector. This note shows explicitly that the state is outside several named earlier input families; it does **not** prove exclusion from every prior regional certificate, novelty, global k3, or stronger-family/human/formal acceptance.

## 1. Exact input and application of the stated region

Consider

\[
|\psi\rangle=(|0001\rangle+|0010\rangle+|1100\rangle)/\sqrt3,
\quad\rho=|\psi\rangle\langle\psi|.
\]

Its four exact local marginals are `diag(2/3,1/3)`, so all local Bloch radii are `r=1/3` and all local axes are nondegenerate. None of the three support strings has its bitwise complement in the support, hence the exact four-site spin-flip overlap is `C=0`. Thus

\[
16r^2+8C=16/9<256/39.
\]

The 114 all-noise original k3 assertion applies conditionally. Independently, direct Pauli arithmetic gives `Tr F(rho)^2=160/9<880/39`, agreeing with its frame criterion. The seven bipartition Schmidt ranks are `2,2,2,2,2,3,3`, so psi is genuinely four-partite entangled and is not biseparable.

## 2. Precise comparisons with older named families

* **Not a local-unitary image of a product-Pauli parity eigenstate.** If psi were an eigenstate of `tensor_i(n_i dot sigma)`, invariance under that operator would make each nondegenerate local marginal commute with its local factor. Each `n_i` would therefore be parallel to the unique local Z axis, so psi would have definite computational parity. Its support instead contains both odd-weight `0001,0010` and even-weight `1100`. This also rules out the earlier paired-parity code family, whose states have a product-Pauli parity symmetry. For a pure density, belonging to the convex hull of such pure images would require being one of them.
* **Not an LU image of a permutation-symmetric pure state.** A symmetric pure state has the same spectrum, hence purity, for every two-party marginal, and local unitaries and party permutations preserve this equality. Here the exact `(1,2)` marginal has spectrum `(2/3,1/3,0,0)` and purity `5/9`, while the `(1,3)` marginal has spectrum `(1/3,1/3,1/3,0)` and purity `1/3`. The same pure-state convex-hull observation applies.
* **Not a local-unitary image of a vacuum-plus-single-excitation state.** Across any bipartition A|B such a state is a sum of at most the two product tensors `|0_A> tensor (c0|0_B>+sum_B c_i|e_i>)` and `(sum_A c_i|e_i>) tensor |0_B>`, hence has Schmidt rank at most two. The actual `(1,3)|(2,4)` cut of psi has Schmidt rank three.
* **Outside the cited old `G>=124/125` near-product region.** Across the `(1,2)|(3,4)` cut, the largest squared Schmidt coefficient is `2/3`; a fully product vector is a special case of a product vector across this cut, so the actual maximal fully product overlap `G<=2/3<124/125`.

These are exact exclusions of the specifically named BISEP/PAR/paired-parity/symmetric/general-W/near-product classes. Other old F2/Schur/covariance or regional sufficient tests are **not assessed** here; this is not a claim that the state escaped every prior accepted region.

## 3. Executed exact physical evidence

`frontier-20261028-115-asymmetric-equal-marginal-check.py`, SHA256 `ffc16f7b089684123c08ea65ebd05ea3c46ba1a033fc8220968009640d33ed3c`, ran with `python3 -B` and single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational arithmetic checks rho purity, all four local marginals, `C=0`, all seven cut ranks, the two explicit two-party marginals and their purities, `Tr F^2=160/9`, and the actual frame-condition inequality. Exact sequential and independently assembled Pauli channels agree at `p=2/3` and `4/3`; exact LDL certifies `lambda1<3/25`, and inertia `(15,1,0)` certifies `lambda2<9/100`. Thus actual top3 `<3/10<32/81`, with certified gap `77/810`; one same actual rank-three projector and its reflected partner have exact output trace `64/243` at both p. The two finite noise checks do not themselves establish all-p coverage. Native checker-pin clock `Wed Oct 28 21:19:16 PDT 2026`.

The 114 whole proof and this exact application require independent written review. All previous source, process and quarantine qualifications remain unchanged.
