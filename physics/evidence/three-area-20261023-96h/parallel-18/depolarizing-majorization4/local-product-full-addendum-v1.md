# Full majorization in the explicit near-product neighborhood

Observed before creation: **2026-10-23T14:21:23-0700**. PhysicsDepol4. Status: **CANDIDATE, written only**. This resumes the same primary problem after the assigned bounded P44 review. No scientific executable was run. Read together with `local-product-stability-v1.md`, SHA-256 `1bd4b2aeb2d031be09e5c9da192b8d624da8808074ddadbf37ab30f1e34d73a6`; that central-index snapshot remains unchanged.

## 1. Stronger local conclusion, same restricted input class

The earlier local snapshot established only central indices. This addendum supplies the missing local subset-size bounds, so that its neighborhood now satisfies **complete** four-qubit depolarizing-output majorization for every physical replacement p:

`G(psi)>=1-1/900000000` implies `lambda(D_p^tensor4(psi)) prec lambda(D_p^tensor4(0000))` for all `0<=p<=4/3`.

This is still an input-restricted theorem, **not** an unrestricted solution. No use of the earlier exact LP certificates is required.

Use the closest-product coordinates and notation of the preceding snapshot: `psi=sqrt(1-s^2)|0000>+s phi`, no weight-zero/one component in phi, weight-sector norms a,b,e with a+b+e=1, and `0<s<=1/30000`. This coordinate representation applies to every state in the claimed neighborhood, by closest-product stationarity.

## 2. The remaining X_2 indices k=2,3,4,5

Use the exact same twice-conjugated expansion from the preceding snapshot,

`X_2(psi) ~ T_2+s^2 D+R`, `||R||<=200s^3`,

with the four spectral clusters of T_2 ordered as 6,3,1,0. Let alpha be the second-order correction to its top eigenvalue, and J the four-dimensional second-order block on H_1.

The vacuum compression of Phi_2(|phi><phi|) is a: for a basis input of weight two, exactly one two-qubit subset retains all zero bits, and at weights three/four none does. Therefore

`alpha =a-6+a/5 =6a/5-6`.

On H_1,

`J=P_1 Phi_2(|phi><phi|)P_1-3I +(1/3)M^dagger M`.

There is no coupling to H_0 at first order. The trace of the compressed Phi_2 term is `6a+3b`: subtract the vacuum a from the previously counted top-five value 7a+3b. Since `||M||_F^2=2a`,

`Tr J=20a/3+3b-12`, and `J>=-3I`.

Hence, for `1<=m<=4`,

`K_m(J)<=Tr J+3(4-m)=20a/3+3b-3m`.

The second-order correction of K_(1+m) is consequently at most

`alpha+K_m(J) <=118a/15+3b-6-3m <=28/15-3m <=-17/15`.

The remainder changes this Ky-Fan sum by at most `5*200s^3<=s^2/30`. Thus

`K_(1+m)(X_2(psi)) <=K_(1+m)(T_2)-s^2`, `1<=m<=4`.

Together with the earlier central bounds, termwise X_2<=6I at k=1, and the trace bound at k>=11, this proves `X_2(psi) prec T_2` at every index throughout the stated neighborhood.

## 3. A compatible weight-two Gram estimate needed for X_3

Write the six weight-two coefficients as c_ij=c_ji, c_ii=0, and let F be the symmetric 4x4 matrix with those entries. Then `||F||_F^2=2a`. Put `Gamma=F F^dagger` and `s_i=Gamma_ii`, so `sum_i s_i=2a`.

Let M again be the four-by-four H_1-to-H_3 matrix, with `M_(ri)=c_([4] minus {r,i})` when r!=i and zero diagonal. Directly comparing its two nonzero summands at each off-diagonal entry shows

`Gamma+M^dagger M=aI+2 offdiag(Gamma)`.                              (2)

For example, at distinct i,j the remaining indices are k,l. Both off-diagonal sums equal `c_ik conjugate(c_jk)+c_il conjugate(c_jl)`; at the diagonal the incident and nonincident pair squares sum to a. This verifies (2) for arbitrary complex coefficients, not only real c.

We need the elementary norm estimate

`lambda_max(2 offdiag(Gamma))<=sqrt(6)a <(5/2)a`.                    (3)

Here is a complete derivation. Let H be the real nonnegative symmetric matrix of entrywise moduli |F_ij|. For any complex unit vectors x,y, `|x^dagger F y|<=|x|^T H |y|`; and absolute values in a Rayleigh quotient show `||H||=lambda_max(H)`. Since H is a real symmetric traceless 4x4 matrix with `Tr H^2=2a`, Cauchy on its other three eigenvalues yields

`lambda_max(H)^2 <=(3/4)Tr H^2=3a/2`.

Thus `||Gamma||=||F||^2<=3a/2` and `Tr Gamma^2<=||Gamma|| Tr Gamma<=3a^2`. Also `sum_i s_i^2>=(2a)^2/4=a^2`. Therefore

`Tr[(2 offdiag(Gamma))^2]=4(Tr Gamma^2-sum_i s_i^2)<=8a^2`.

This matrix is Hermitian and traceless. Applying the same four-dimensional trace-zero eigenvalue bound gives (3). If a=0 all matrices vanish and the non-strict version is immediate. No unconstrained Pauli-Gram majorization theorem is assumed; the complementary-pair structure of M is used explicitly.

## 4. X_3 effective spectral blocks

Let Psi_3(rho)=X_3(rho). Its product reference T_3 is 4 on H_0, 1 on H_1, and 0 on `H_2 direct_sum H_3 direct_sum H_4`. Expand

`X_3(psi)=T_3+s sqrt(1-s^2) C_3+s^2 B_3`,

where `B_3=Psi_3(|phi><phi|)-T_3` and C_3 is the vacuum cross term. Since each of the four marginal terms is bounded by I, `||B_3||<=4`.

The first-order C_3 couples only the positive support L=H_0+H_1 to its kernel. More explicitly:

- its H_0 column into H_2 is 2c;
- its H_0 column into H_3 is the weight-three coefficient vector q, with `||q||^2=b`;
- its H_1-to-H_3 block is M;
- its H_1-to-H_4 row is the four weight-three amplitudes in complementary order, denoted h^dagger, with `||h||^2=b`.

The first item has factor two because a weight-two support lies in exactly two three-qubit marginal subsets. A weight-three support lies in exactly one. No weight-four coefficient survives a three-qubit vacuum cross term. These statements also show there are no first-order within-support or within-kernel blocks.

The same commutator elimination used in the preceding snapshot applies, with eigenvalue gaps four and one. The second-order top eigenvalue correction is

`beta=-4+(4a+b)/4=-4+a+b/4`,

because the vacuum compression of Psi_3(|phi><phi|) is zero. The second-order H_1 block is

`L_1=Gamma-I+M^dagger M+h h^dagger`

`   =(a-1)I+2 offdiag(Gamma)+h h^dagger`.                           (4)

Indeed, the H_1 compression of Psi_3(|phi><phi|) is exactly Gamma, the one-particle reduction of the weight-two coefficient array. Cross terms between different input Hamming weights have nonzero charge and vanish in a fixed-weight compression.

Its trace and operator lower bound are

`Tr L_1=4a+b-4`, `L_1>=-I`.

For m=2,3 this gives

`beta+K_m(L_1) <=(-4+a+b/4)+(4a+b-m)`

`                  =5a+(5/4)b-4-m <=1-m <=-1`.                    (5)

For m=1, instead use (3) in (4):

`beta+lambda_max(L_1) <=(-4+a+b/4)+(a-1)+(5/2)a+b`

`                         =(9/2)a+(5/4)b-5 <=-1/2`.                (6)

Thus the second-order corrections to the three nontrivial sums K_2,K_3,K_4 are all uniformly negative, by at least one half.

## 5. Explicit remainder for X_3 at the same radius

The off-diagonal block of C_3 between L and its kernel has squared Frobenius norm `6a+2b<=6`. Hence `||C_3||<=sqrt(6)<3`. The first anti-Hermitian elimination generator S_3 has

`||S_3||_F^2=2((4a+b)/16+2a+b)=(9/2)a+(17/8)b<=9/2`,

so `||S_3||<3`. The effective second-order matrix has norm at most `4+3*3=13`.

For `s<=1/1000`, the first exponential conjugation has remainder at most

`(144+54+24)exp(6s)s^3+3s^3 <=300s^3`.

The terms are respectively the third-order tail from T_3, the second-order tail from sC_3, the first-order tail from s^2B_3, and the normalization square-root remainder. This follows by the same displayed commutator-series bound as before, not an asymptotic assertion without constants.

The second anti-Hermitian generator T_3' has norm at most `4*13=52` by the Frobenius/gap argument in the preceding snapshot. Its additional remainder is at most

`(21632+1352) exp(104s^2)s^4 <=45968s^4 <=46s^3`.

Thus the exact twice-conjugated X_3 is its block-diagonal second-order approximation plus a remainder of norm at most `400s^3`. Its clusters stay ordered because `26s^2<1`. The error in each of K_2,K_3,K_4 is at most `1600s^3`.

For `s<=1/30000`, this is at most `(4/75)s^2`. Combining with (5)–(6) proves

`K_k(X_3(psi)) <=K_k(T_3)-(2/5)s^2`, `k=2,3,4`,

since `1/2-4/75=67/150>2/5`. At k=1, X_3<=4I; at k>=5 the trace bound eight is the target. Hence `X_3(psi) prec T_3` at every index.

## 6. Completion of the restricted theorem and remaining global obstacle

Sections 2–5 and the prior central snapshot establish the full subset-size majorizations `X_2 prec T_2` and `X_3 prec T_3` in this input neighborhood. X_0,X_1,X_4 have elementary universal bounds. Their product references share Hamming order, and the depolarizing expansion has nonnegative coefficients for q=min(p,2-p) in [0,1]. Therefore the common-order/Ky-Fan argument proves full output majorization for every physical p; spin flip handles p>1.

This gives a second actual input region, near arbitrary products, beyond the moment region. It is not a silent restriction of the assigned target: **the unrestricted target remains open in this work**. A remaining pure counterexample must lie outside both (i) `3R+2C_spinflip<=157/36` and (ii) `G>=1-1/900000000`. At k=6 the stronger moment exclusion is `10R+4C_spinflip<=74/3`; its complement is still a substantial region.

The next missing ingredient is a nonperturbative compatibility inequality for that intermediate-entanglement region, not another moment restatement or an unconstrained PPT solve. Candidate correctness still requires separate written reconstruction and parent acceptance. No kernel, human, external-model, numerical or novelty acceptance is implied.
