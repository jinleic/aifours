# Persistent co-Choi kernel and an explicit open nonuniform reference region

Before-creation clock observed: **2026-10-23T13:39:27-07:00**. Status: **CANDIDATE written proof**, pending independent reconstruction. This is the single next primary packet requested by the parent. The persistent-kernel idea was a parent-suggested lead; all contractions and constants below are independently derived here. No scientific program, point evaluation, symbolic engine, replay, model CLI or formal verification was performed.

## 1. Exact result, normalization and limits

Let `B=C^4⊗C^4`, dimension16, and define

`Lambda_B=(Tr(.)I-./2)⊗(Tr(.)I-./2)`.

For a nonzero complex reference eta in B put

`A_eta=Lambda_B(|eta><eta|)`,

`L_i(eta)=Lambda_B(|i><eta|)`,

`M_eta(|i><j|)=L_i A_eta^(-1)L_j†`,

`C_B=Jhat(Lambda_B)`, `S_eta=Jhat(M_eta)`,

with `Jhat(E)=Σ_(i,j)|j><i|⊗E(|i><j|)`. All maps and kernels are on the fixed physical input/output spaces; no coordinate-dependent eigenvector is silently held fixed.

Scaling eta by any nonzero complex scalar leaves M_eta and S_eta unchanged: A scales by the squared modulus and L_i by the conjugate scalar. For norm estimates **eta is normalized to norm one**. Let

`eta0=Phi4=(|00>+|11>+|22>+|33>)/2`,

`P_eta=|eta><eta|⊗I_B`,

`rho=1/207424`.

### Theorem PK: universal persistent reference kernel

For every nonzero complex eta and every z in B,

**`(C_B-S_eta)(eta⊗z)=0`.**

This asserts a contained kernel for arbitrary eta, not that it is always the whole kernel and not that either co-Choi sign is always positive.

### Theorem OR: an explicit sufficient open angular region

If eta has unit norm and

**`||eta-eta0||<rho`,**

then

`C_B+S_eta >= (1/32)I`,

`C_B-S_eta >= (13/96)(I-P_eta)`,

`ker(C_B-S_eta)=ran P_eta=span{eta}_input⊗B_output`.

The same holds around any locally-unitarily equivalent maximally entangled reference, with the same radius. In particular a sufficient condition stated purely in the normalized Schmidt coefficients sigma1,...,sigma4 is

**`Σ_i (sigma_i-1/2)^2 < 1/(207424)^2`.**

This is a tiny, conservative sufficient region, **not the sharp angular criterion**, and it is not claimed necessary. It supplies actual nonuniform reference rays, not just local-unitary images of equal Schmidt coefficients. Generic two-planes remain outside the reference-ray approach; unrestricted W4 stays NOT PROVED.

## 2. Persistent identity with the complex conjugations explicit

The local map and its tensor square preserve adjoints. With eta=Σ_i eta_i|i>, linearity gives

`Σ_i eta_i L_i=Lambda_B(Σ_i eta_i |i><eta|)=Lambda_B(|eta><eta|)=A_eta`.

The coefficients here are eta_i, **not** their conjugates. The conjugation is already present in the bra of L_i. On a reference input,

`S_eta(eta⊗z)`

`=Σ_(i,j) eta_i |j>⊗L_i A_eta^(-1)L_j† z`

`=Σ_j |j>⊗L_j†z`.

On the other hand,

`C_B(eta⊗z)=Σ_j |j>⊗Lambda_B(|eta><j|)z`

`=Σ_j |j>⊗Lambda_B(|j><eta|)†z`

`=Σ_j |j>⊗L_j†z`.

This proves PK for arbitrary complex eta in any fixed basis, including zeros in its Schmidt spectrum. A_eta is always invertible: it is a compression of the positive swap product R_B, whose least eigenvalue is1/4, giving `A_eta>=||eta||^2 I/4`.

M_eta is completely positive because its ordinary Choi matrix is the block Gram matrix `L_i A_eta^(-1)L_j†`. Consequently S_eta is Hermitian, even though it need not be PSD. Thus D_eta=C_B-S_eta is Hermitian and PK implies **both** `D_eta P_eta=0` and `P_eta D_eta=0` for unit eta.

The generic algebraic identity itself is not presented as a priority discovery. Its usefulness is that it tracks the required zero modes exactly while the Schmidt angles change.

## 3. Fixed positive gaps at the uniform reference

The prerequisite is the explicit d=4 GS proof, SHA `684ec10f7b7ab25bf0331fdbe9f660ffbfc195c37581addd36d14cf1228debb5`, and its dimension-universal/equality companions. These have ordinary in-harness written reconstructions; they are not formal/kernel theorems. This section extracts **written gap bounds**, not numerical eigenvalue estimates.

Because scaling does not change S, `S_eta0=S_Omega4`. From the complete Bell-contraction decomposition:

### 3.1 Minus complement gap

- On K-perp the smallest positive minus scalar is1/6.
- On the two-dimensional identity block, the physical action has eigenvalues0,1 (action matrix `[[0,-1/4],[0,1]]`), with the zero exactly the reference direction. Its nonorthogonal coordinates do not change its eigenvalues.
- On each traceless block the f_minus eigenvalue is1. The remaining rank-two positive matrix has trace7/3 and product of its two nonzero eigenvalues4/9. Hence its smaller positive eigenvalue is at least `(4/9)/(7/3)=4/21>1/6`.

The complete minus kernel is exactly ran P_eta0. Therefore

**`D_eta0>= (1/6)(I-P_eta0)`**, and

**`B_eta0:=D_eta0+P_eta0>=I/6`.**

For the rank-two traceless matrix, the product4/9 follows by summing its three 2×2 principal minors `2/9,1/18,1/6`; its trace is `1/6+11/6+1/3=7/3`. These are hand identities, not fitted eigenvalues.

### 3.2 Plus gap

- On K-perp the smallest plus scalar is1/3.
- On the identity block, the physical action has trace4 and determinant1/4. Both eigenvalues are positive. The smaller is at least determinant/trace=1/16.
- On each traceless block the f_minus eigenvalue is1/2. The positive 3×3 block has trace25/6 and determinant19/24. If its eigenvalues are lambda1<=lambda2<=lambda3, then `lambda2 lambda3<=(trace/2)^2`; hence `lambda1>=4det/trace^2=114/625>1/16`.

Thus

**`H_eta0:=C_B+S_eta0>=I/16`.**

The identity-block trace/determinant refer to its actual operator, not to the uncorrected nonorthogonal quadratic-form matrix. Its action matrix is `[[5/2,-7/4],[-2,3/2]]`, so those invariants are immediate.

## 4. Explicit Lipschitz bounds — no spectral computation

Let eta and eta0 both have norm one and let `epsilon=||eta-eta0||`. The physical swap product has norm `||R_B||=(3/2)^2=9/4` and minimum eigenvalue1/4. Its reference compressions and mixed compressions imply

`||A_eta^(-1)||<=4`, `||A_eta0^(-1)||<=4`,

`||A_eta-A_eta0||<=(9/2)epsilon`,

`||L_i(eta)||<=9/4`, `||L_i(eta0)||<=9/4`,

`||L_i(eta)-L_i(eta0)||<=(9/4)epsilon`.

The A difference follows by changing one reference vector at a time in the two-sided compression. The inverse identity gives

`||A_eta^(-1)-A_eta0^(-1)||<=4·(9epsilon/2)·4=72epsilon`.

For every matrix-unit block of M, add and subtract one factor at a time. Its difference is at most

`(9/4)^2 (4+72+4)epsilon =405epsilon`.

The two terms with inverse bound four account for the left and right L changes; the middle inverse difference accounts for72. The co-Choi input reversal does not alter the maximum block norm.

A16×16 matrix of operator blocks, each of norm at most b, has norm at most16b: apply the triangle inequality to each row and Cauchy–Schwarz to the16 input block norms. Therefore

**`||S_eta-S_eta0||<=6480epsilon`.**

For the moving orthogonal projection,

`||P_eta-P_eta0||<=2epsilon`,

by expanding the difference of the two unit rank-one projectors. Consequently

`||H_eta-H_eta0||<=6480epsilon`,

`||B_eta-B_eta0||<=6482epsilon`,

where `H_eta=C_B+S_eta` and **`B_eta=D_eta+P_eta` uses the moving projection**, not P_eta0. This is what prevents the exact zero modes from being perturbed as if their subspace were fixed.

## 5. Positivity on the moving complement

Choose epsilon<rho=`1/(32·6482)`. Then

`||H_eta-H_eta0||<1/32`,

`||B_eta-B_eta0||<1/32`.

Section3 gives

`H_eta >= I/16-I/32=I/32`,

`B_eta >= I/6-I/32=(13/96)I`.

By PK and Hermiticity, P_eta exactly reduces D_eta: it vanishes on ran P_eta and has no cross terms with its orthogonal complement. B_eta acts as identity on ran P_eta and as D_eta on the complement. Thus the B bound proves

`D_eta >= (13/96)(I-P_eta)`,

with exact kernel ran P_eta. Together with H_eta this proves OR, including both numerical constants and the rotating zero-mode claim. No continuity assertion has been used in place of an explicit error bound.

## 6. Phase, local-unitary and Schmidt-coefficient formulations

A global phase of eta changes neither A, M, S nor P, so the ball may equivalently be taken after a phase choice. For a local unitary `W=U2⊗U3`, covariance of Lambda_B gives

`S_(W eta)=(W⊗W)S_eta(W†⊗W†)`,

and the same conjugation leaves C_B unchanged. It also transports P_eta to P_(W eta). Therefore the gaps and radius are unchanged around any local-unitary image of eta0.

Write a normalized reference in a Schmidt basis as `eta=Σ_i sigma_i |ii>`, with sigma_i>=0 and `Σsigma_i^2=1`. Comparing it with eta0 in that basis gives exactly

`||eta-eta0||^2=Σ_i(sigma_i-1/2)^2`.

This proves the sufficient angular condition in Section1. No assumption of equal Schmidt coefficients or real entries in the original basis is imposed: the real diagonal form is obtained by the standard Schmidt decomposition and the already proved covariance. A proof that this is the minimal distance over the entire orbit is unnecessary for this sufficient implication.

### A literal nonuniform reference in the open region

Take e=1/1000000 and

`eta_e=[|00>+|11>+|22>+(1+e)|33>]/sqrt(3+(1+e)^2)`.

For v=(1,1,1,1+e), v0=(1,1,1,1), the triangle inequality and `||v0||=2` give

`||v/||v||-v0/2||<=| ||v||-2 |/2+||v-v0||/2<=e`.

Since e<1/207424, OR applies. The Schmidt coefficients are genuinely unequal, so this is not a local-unitary rephrasing of the uniform theorem. The small radius is intentionally conservative and no optimality is claimed.

## 7. Consequence for reference-ray Werner operators and strict new coverage

The switched-complement bridge requires only `-C_B<=S_eta<=C_B`, while the strictness/equality argument requires the strict plus sign and exact minus kernel. OR supplies all three. Therefore for any finite first-site space and rank-at-most-two complex C with a range ray `a⊗eta` satisfying the sufficient angular condition,

`q3(C)>=0`,

with nonzero equality cases exactly `P_E⊗|eta><w|` as in the prior equality proof. The co-range statement is the adjoint version. This application uses no partial-trace rank assumption and no inference from a co-Choi negative direction to an admissible rank-two witness.

For a strict comparison with the earlier equal-Schmidt-ray family, replace Phi4 in both u and v of the checkpoint001 separation example by eta_e; retain the two GHZ-type second rays x,y. Each resulting range/co-range has only its one biseparable ray across1:23, and that ray has unequal Schmidt coefficients. Across cuts2:13 and3:12, every combination with a nonzero reference coefficient has Schmidt rank4: its four independent first-site-zero (or shifted-first-site) components cannot be canceled by the GHZ-type terms. With reference coefficient zero, the GHZ ray has rank3. Thus neither plane contains a biseparable ray on those cuts either. The new operator is not covered by simply choosing a different equal-Schmidt reference or rotating a degenerate SVD. Its old local-support/product-code exclusions continue to hold for the same reason.

This establishes a genuine sufficient nonuniform family. It does not claim that every nonuniform reference works, or that a generic two-plane contains a ray in this tube. The exact nonuniform negative examples in the angle-obstruction packet remain valid and lie outside this guaranteed small region.

## 8. Provenance, prior art and the remaining angular problem

The persistent identity is a general co-Choi/Schur algebra calculation and the openness principle is finite-dimensional perturbation theory. They are not counted as independent discoveries. The mathematical delta is a **checkable nonuniform sufficient region** derived from the previously written-checked GS4 gaps and their minimal reference kernel. Wu–Zou's fully-product-ray argument does not automatically supply it: its product-reference minus kernel has additional zero directions, whereas the minimal GS4 kernel is load-bearing here. The inspected primary papers do not state this exact tube, but the existing bounded screen does not certify novelty or priority.

The exact global set of Schmidt spectra satisfying symmetric GS is still unresolved. A sharp characterization must contain the product and uniform rank-three/full-rank positive points and exclude the explicit near-balanced rank-two perturbations. This packet intentionally freezes **one sufficient angular condition**, not a claim that the tiny radius is the true boundary. No further scientific execution is admitted; the author pauses new candidate generation for this packet's independent check as requested.
