# The bare Bose-lift PSD certificate is PSD-only at every finite level

Observed immediately before freezing: **2026-10-23T14:42:12-07:00**. Author PhysicsPPT44, physics-3. **CANDIDATE: complete written lemma, not independently reconstructed, formally checked, or priority-cleared.** No scientific executable was used.

This documents the cancelled N2 admission preparation and a stronger consequence found during its written continuation. It is an obstruction to one proposed witness-certificate mechanism, **not a proof that all 4 by 4 PPT states have Schmidt number at most two**.

## 1. Precisely which hierarchy is considered

Let physical systems A,B1,...,BN each have dimension d, and auxiliary systems A0,B10,...,BN0 each have dimension k. Assume k>=2 and N>=1 are finite. Set

`|phi_k> = (1/sqrt(k)) sum_{r=0}^{k-1} |r>_A0 |r>_B10`,
`Phi_k = |phi_k><phi_k|`.

For an arbitrary Hermitian `W in L(C^d_A tensor C^d_B)`, define

`K_N(W)=Phi_k(A0,B10) tensor W(A,B1) tensor I(B20,B2,...,BN0,BN)`,

with the tensor factors reordered as

`(A0,A) : (B10,B1) : ... : (BN0,BN)`.

Let P_N be the orthogonal projector onto the subspace invariant under all permutations of the **complete paired Bob systems** `(Bj0,Bj)`, i.e.

`P_N=(1/N!) sum_{pi in S_N} I_(A0,A) tensor U_pi`.

The proposed sufficient certificate is positivity of

`Q_N(W)=P_N K_N(W) P_N`

on its Bose-supported subspace `C^(kd) tensor Sym^N(C^(kd))`.

This is the bare Bose-extension objective compression in Chen–Collins–Fawzi, [arXiv:2505.22100v1](https://arxiv.org/html/2505.22100v1), Lemma4/Eqs.(7)–(10), Definition6/Eq.(13), Proposition1/Eq.(14). The normalized auxiliary projector and the whole-paired-Bob permutation convention above are important. The corresponding raw primary HTML is retained with SHA-256 `c83cb1cc76311cc6bc41c41dfe0074a4d87732fcabbcdf466cead1a841c727f4`.

No PPT constraints are added to the primal extension here. A dual certificate with extra partially transposed positive terms is not the same condition and is not excluded by this lemma.

## 2. Theorem

**For every finite N>=1, k>=2, and d>=1,**

`Q_N(W)>=0   if and only if   W>=0`.

Thus the bare finite-level PSD certificate cannot certify a non-PSD k-block-positive witness. In particular it cannot supply a negative separator for any positive density matrix, whether PPT or NPT.

The N2 instance previously proposed for P44 has Bose support dimension `8*binom(9,2)=288`. Raising it to N3 would give dimension `8*binom(10,3)=960`, but **the same obstruction still applies**. Increasing the finite level of this exact PSD test is not a scientifically justified substitute.

## 3. Explicit negative direction for every non-PSD W

Take arbitrary nonzero vectors

`psi in C^d_A tensor C^d_B`, `v in C^d`.

For each j=1,...,N define Xi_j as follows:

- Alice's auxiliary is `|0>_A0`;
- Bob j's auxiliary is `|0>_Bj0` and the physical state on A,Bj is psi;
- every other Bob l has auxiliary `|1>_Bl0` and physical vector v.

Tensor factors are placed in the fixed order from Section1. Set

`Xi_N = sum_{j=1}^N Xi_j`.

Because every spectator Bob uses the same v, any permutation of the complete paired Bob systems merely permutes the N summands. Therefore

`P_N Xi_N=Xi_N`.

For different j, the full auxiliary label strings have their unique Bob-auxiliary zero in different positions. They are orthogonal. Consequently

`||Xi_N||^2=N ||psi||^2 ||v||^(2N-2)`.

Now contract the normalized Bell bra on A0,B10. The term Xi_1 has auxiliary pair00 and survives with factor `1/sqrt(k)`. Each term Xi_j with j!=1 has pair01 and vanishes. Hence

`(<phi_k|_(A0,B10) tensor I) Xi_N`
` = (1/sqrt(k)) psi_(A,B1) tensor (|1> tensor v)_(B2) tensor ... tensor (|1> tensor v)_(BN)`.

This identity is exact for arbitrary complex psi,v. For N=1 the spectator product is the scalar1, so the same argument applies.

It follows immediately that

`<Xi_N|Q_N(W)|Xi_N>`
` =<Xi_N|K_N(W)|Xi_N>`
` =(1/k) <psi|W|psi> ||v||^(2N-2)`.

If W has any negative expectation direction psi, the displayed Bose-supported vector has negative expectation against Q_N(W). Thus positivity of Q_N(W) implies every expectation of W is nonnegative, which is exactly W>=0.

Conversely, if W>=0, then K_N(W) is a tensor product of positive operators, hence positive. Orthogonal compression preserves positivity. This proves both implications.

### Quantitative form and consistency check

For unit psi,v, the normalized vector `Xi_N/sqrt(N)` has expectation

`<psi|W|psi>/(kN)`.

In particular, if `lambda_min(W)<0`, the minimum of the bare Bose-extension objective is at most `lambda_min(W)/(kN)<0` at **every finite N**. No matrix diagonalization or finite numerical sample is needed to establish this statement.

The sufficiency direction W>=0 is an immediate positive anchor: a positive tensor followed by a compression is positive. The necessity direction uses the explicit contraction above, rather than a guessed Schur-block computation.

## 4. Why this does not contradict the source's limiting hierarchy

The source's auxiliary lift tests only the **sign** of its separable minimum; its Remark5 explicitly warns that the lifted and original optimization values differ. Even when W is strictly positive on normalized Schmidt-rank-k vectors, the lifted operator Phi_k tensor W has zero expectation on auxiliary-orthogonal product vectors. Its separable minimum can therefore be zero rather than strictly positive.

Accordingly, finite Bose-extension minima may remain negative and approach zero from below. The explicit `1/(kN)` negative direction is consistent with such asymptotic convergence. This lemma does **not** claim that the source's limiting separability theorem is false, that all its symmetry reductions are useless, or that PPT-strengthened/differently normalized certificates fail.

Auxiliary unitary twirling cannot remove this negative expectation from an equivalent symmetry reduction: K_N and P_N are invariant under the corresponding joint auxiliary action, so twirling a feasible negative test state preserves its objective and Bose support. The obstruction concerns the underlying cone, not one basis or solver implementation.

## 5. Consequence for the admitted preparation

Parent approved **preparation only**, never execution, of the N2 screen for one rational mixed-kernel state `R_x/49`, x=(1,1,1,1), together with known-SN4 and separable controls. The preparation is frozen as

`admission-preparation-kbp2-N2-v1.json`, status `WITHDRAWN_ANALYTICALLY_VACUOUS_BEFORE_EXECUTION`.

That JSON's shorthand `braPhi2` denotes the normalized vector bra `<phi_2|`, not a bra of the projector Phi2; Section1 here fixes the notation explicitly. Its N2 identity is correct and is a special case of this theorem. Its description of N3 as a different test needing analysis is now strengthened: **N3 with the same bare PSD condition is also vacuous**, by the present all-finite-N proof.

No scientific script was created or run, no solver invoked, and no GO consumed. A numerical negative output from an optimization over this supposed witness cone would indicate approximation error or an encoding defect, not a valid Schmidt-number separator.

The precise remaining witness-method input would have to change the certificate cone — for example by genuinely analyzing additional PPT constraints or an appropriate normalization/quotient — rather than merely increasing N or switching to another target matrix. Such a change is a new mathematical obligation and a materially different experiment; none is silently authorized here.

## 6. Evidence labels

- **Correctness:** author-written universal proof; separate reconstruction and parent acceptance pending.
- **Source trust:** raw primary theorem/definition scope read and pinned; no unsupported claim that the paper asserts finite sign completeness.
- **Scope:** all finite bare Bose-lift PSD levels defined above. Not unrestricted P44, not a no-go for every SDP hierarchy or all two-positive maps.
- **Execution/formal verification:** none. Root-of-unity results in the earlier compression packets are unrelated to this proof.
- **Novelty/significance:** priority unclear. The operational value is eliminating an entire proposed assay family before any scientific execution, not a claim of solving P44 or a book chapter.
