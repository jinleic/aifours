# An all-physical-parameter k3 gap inequality coupling one actual density and one actual rank-three projector

Owner PhysicsDepol4-2, physics-2. Actual native clock observed before the paired exact checker was prepared: **Thu Oct 29 13:42:19 PDT 2026**. This is an observation preceding composition, not an asserted file-creation time.

**NEW AUTHOR-WRITTEN CANDIDATE, not yet independently reviewed or adopted.** The inequality in §1 is unconditional and quantifies over every actual mixed input, every actual complex rank-three projector, and every physical p. Its right-hand side may be negative; it is **not** a global k3 proof. The pure-input sufficient criterion and exact physical example are consequences. They do not assert an all-density theorem at p=4/3.

This packet derives everything from the channel definition, Pauli orthogonality, Cauchy–Schwarz, elementary convexity and the finite Ky Fan principle. It does not use the conjectural R positivity, the one-erasure conjecture, equality packet 183, or a previously held result. Zhang's public four-qubit clipping mechanism remains explicitly attributed; this direct Pauli-budget calculation is not claimed to establish novelty or to settle the source's underdefined exact uniform-subset-weight scope.

## 1. Literal unconditional inequality

Let `rho` be any four-qubit density, `Q` any complex orthogonal rank-three projector, and `0<=p<=4/3`. Set

`Lambda_p=Phi_p^tensor4`, `Phi_p(X)=(1-p)X+(p/2)Tr(X)I`, `s=1-p`, `t=|s|`.

For every phase-free four-qubit Pauli string P let

`a_P=Tr(rho P)`, `b_P=Tr(Q P)`, and `A_j=sum_(wt(P)=j) a_P^2`.

The coefficients are real. Let `r_i` be the local Bloch lengths of this same rho, ordered as `r_1<=r_2<=r_3<=r_4`, and put

`S=A_1=sum r_i^2`, `L=r_1+r_2+3r_3+3r_4`,

`H_t=A_2+t^2 A_3+t^4 A_4`,

`x(Q)=sum_(wt(P)=1) b_P^2`.

With `R3(t)=[3+8t+6t^2-t^4]/16` the product-reference top-three sum, the claimed inequality is

`16 [R3(t)-Tr(Q Lambda_p(rho))]`

`>= t [8+6t-t^3 - min(L,sqrt(S x(Q))) - t sqrt(H_t (39-x(Q)))]`.  (1)

All square roots are nonnegative and finite. At t=0 both sides vanish. This is a same-rho, same-Q, same-p inequality: none of the moment budgets or marginals comes from an independently chosen state or projector.

### Exact uniform-in-Q corollary

If S>0 set

`u=L^2/S`, `x0=39S/(S+t^2 H_t)`, `x_*=min(u,x0)`,

`B_t(rho)=sqrt(S x_*)+t sqrt(H_t(39-x_*))`.  (2)

If S=0 define `B_t(rho)=t sqrt(39 H_t)`. Then for the **same actual mixed rho** and every physical p,

`K3(Lambda_p(rho)) <= [3+t B_t(rho)]/16`,

`16 [R3(t)-K3(Lambda_p(rho))] >= t[8+6t-t^3-B_t(rho)]`.  (3)

Consequently, for t>0, the explicit state-dependent condition

`B_t(rho)<=8+6t-t^3`  (4)

is sufficient for original k3 at that p, with strict inequality implying a strict gap. It is an input-and-parameter criterion, **not** a claim that all rho satisfy it. It applies to mixed rho as written, without treating a mixed spin-flip overlap as a pure-state invariant or picking a decomposition.

## 2. Proof of (1): one shared projector budget

Pauli orthogonality gives `Tr(PP')=16 delta_(P,P')`. Since Q is a rank-three orthogonal projector,

`sum_P b_P^2=16 Tr(Q^2)=48`, `b_I=Tr Q=3`,

so the SAME Q satisfies

`sum_(wt(P)>=2) b_P^2=39-x(Q)`.  (5)

For completeness `0<=x(Q)<=20`. Rotate the local Bloch axes of Q so each one-body trace vector points along its local Z axis (zero vectors permit any axis). These rotations preserve x. Writing `q_z=<z|Q|z>`, one has `0<=q_z<=1`, `sum_z q_z=3`. The resulting sum of four squared local-Z traces is a convex function of q, whose maximum over this hypersimplex occurs at a vertex: exactly three distinct z have q_z=1. For such a vertex let z,z',z'' be the selected strings. Their sign vectors satisfy

`x=36-4[d(z,z')+d(z,z'')+d(z',z'')]`.

At least two coordinates vary among three distinct binary strings, and each varying coordinate contributes two to the sum of pairwise Hamming distances. Hence that distance sum is at least four, proving `x<=20`. This argument covers non-diagonal complex Q via its actual diagonal in the locally rotated basis; it does not replace Q by an independent test object.

The single-site channel sends each nonidentity Pauli to s times itself. Thus

`16 Tr(Q Lambda_p(rho))=3+sum_(j=1)^4 s^j sum_(wt(P)=j) a_P b_P`.  (6)

For the weight-one term, Cauchy–Schwarz yields

`|sum_(wt(P)=1) a_P b_P|<=sqrt(S x)`.

It also equals `Tr(Q H)` for the actual commuting local Hamiltonian `H=sum_i r_i n_i dot sigma_i`. Its spectrum is invariant under global sign reversal, so the absolute value is at most its top-three eigenvalue sum. Ordering the radii yields the three largest eigenvalues `sum r_i`, `sum r_i-2r_1`, `sum r_i-2r_2`. Their sum is exactly L. Thus the weight-one contribution in (6) is bounded by `t min(L,sqrt(Sx))`.

For weights 2–4, one application of Cauchy–Schwarz, retaining the actual signed channel powers, gives

`|sum_(j=2)^4 s^j sum_(wt(P)=j) a_P b_P|`

`<= t^2 [sum_(j=2)^4 t^(2j-4) A_j]^(1/2) [sum_(wt(P)>=2) b_P^2]^(1/2)`

`=t^2 sqrt(H_t(39-x))`.

Together with (6) and the exact reference polynomial, this proves (1), also for negative shrinkage s<0 without reflecting or changing either Q or rho. At p=1 the output is I/16 directly.

## 3. Proof of the optimizer in (2)

Assume S>0. By Cauchy–Schwarz on `(r_1,r_2,r_3,r_4)` against `(1,1,3,3)`,

`u=L^2/S<=20<39`.

For `0<=x<=u`, `min(L,sqrt(Sx))=sqrt(Sx)`. The function

`f(x)=sqrt(Sx)+t sqrt(H_t(39-x))`

is concave and reaches its unconstrained maximum at `x0=39S/(S+t^2 H_t)`; this remains valid when H_t=0, with x0=39. Its maximum on `[0,u]` is f(min(u,x0)). For `x>=u`, the first term is L and the second is nonincreasing, so no larger value is obtained beyond u. Thus f(x_*) bounds the bracket for every actual projector, even if the maximizing relaxed x_* is not itself realizable by a rank-three projector. When S=0, L=0 and the maximum is at x=0. This proves (2)–(4); no optimizer is asserted to be a physical projector.

The new estimate also retains the earlier D_p comparison: for any density, Parseval gives `A_2+A_3+A_4=16Tr(rho^2)-1-S<=15-S`, so `H_t<=15-S` for 0<=t<=1. Hence `B_t<=L+t sqrt(39(15-S))` and `8+6t-t^3>=8+5t`. Therefore the earlier pure-state criterion `8-L>=t(sqrt(39(15-S))-5)` implies (4). This is an implication between sufficient tests, not an assertion that either test characterizes all feasible states.

## 4. Exact genuinely entangled state beyond the named f172 hull at p=2/3 and p=4/3

Consider the normalized, physical pure state

`psi=(3|0000>+|0011>+|0101>+|1110>)/sqrt(12)`, `rho=psi psi^dag`.  (7)

Its support contains no two strings at Hamming distance one, so each one-site marginal is diagonal. Their actual Bloch radii, in site order, are `(5/6,2/3,2/3,2/3)`. Direct Pauli calculation gives

`S=73/36`, `L=35/6`, `C=|<psi|Y^tensor4 conjugate(psi)>|^2=0`,

`(A_0,A_1,A_2,A_3,A_4)=(1,73/36,145/36,215/36,107/36)`.  (8)

C=0 because no support string is the bit complement of another. At `t=1/3`, including both physical parameters p=2/3 and p=4/3,

`H_t=13787/2916`, `u=1225/73`, `x0=2075463/67004>u`,

`H_t(39-u)=11181257/106434<121`.

Thus `B_t=L+(1/3)sqrt(H_t(39-u))<35/6+11/3=19/2`. Since `8+6t-t^3=269/27`, the all-projector result (3) gives the **strict original-channel certificate**

`K3(Lambda_p(rho)) < 37/96 = 32/81-25/2592`, for p in `{2/3,4/3}`.  (9)

Here 32/81 is the exact product-reference top-three sum. This is a result for the displayed input and **every** rank-three Q at each of the two displayed physical parameters; it is not an all-input statement at either parameter.

### The same explicit input and projector at both parameters

For the actual rank-three projector

`Q=|0000><0000|+|0011><0011|+|0101><0101|`,

`x(Q)=12`, and all other projector Pauli weight-norm squares are `(b_0^2, b_2^2, b_3^2, b_4^2)=(9,6,12,9)`. Direct exact channel evaluation gives

| p | Tr(Q Lambda_p(rho)) | R3 | actual same-Q gap |
|---|---:|---:|---:|
| 2/3 | 5/18 | 32/81 | 19/162 |
| 4/3 | 41/324 | 32/81 | 29/108 |

No optimality of this Q is claimed. The general inequality (1) itself certifies a weaker positive gap for this same Q without diagonalizing the output: `Sx=73/3<25` and `H_t(39-x)=13787/108<144`, hence the bracket is larger than `269/27-5-4=26/27`, and the gap exceeds `13/648` at both p. This checks the same actual rho/Q/p interface rather than an incompatible marginal tuple.

### Exact comparison with named earlier criteria

For state (7), at t=1/3:

- it is not P or U because it is genuinely four-party entangled and has nonzero one-site Bloch radii;
- H's required moment condition fails: `4S+8C=73/9>64/9`;
- D_p fails since `delta=8-L=13/6`, and

  `39(15-S)-(5+delta/t)^2=1121/3>0`.

  Both sides compared under the square root are nonnegative, so the D_p inequality fails strictly.
- the earlier pure-state full-output-purity test in packet 39 also fails:

  `39(S+t^2 H_t)-(8+6t-t^3)^2=680/2187>0`.

Because a rank-one density in a convex hull of pure states can only be a mixture of its own ray, rho is outside the **named** fixed-p f172 hull `P union U union D_p union H`. This is not an exhaustive exclusion of every historical region, candidate, or prior source.

Every one of the seven nontrivial bipartitions has a nonzero 2-by-2 coefficient minor: for all seven cuts the checker records an unnormalized determinant 3, hence the normalized determinant is 1/4. Thus the state is genuinely four-party entangled. It is also outside the near-product condition `G>=124/125`, since any product overlap is at most the largest eigenvalue `5/6` of a one-site marginal. These facts do not imply that every other earlier sufficient condition fails.

## 5. Actual finite checks and exact limits

The independent-to-the-paper finite checker in this same owner root is `frontier-20261029-185-weight-budget-physical-check-v1.py`. Its final corrected run uses only Python integers and fractions.Fraction; it checks the displayed real Pauli expectations over all 256 strings, all seven cut minors, the Q coefficient budgets, the stated rational strict comparisons, and the two same-Q channel traces. The first development run stopped at an incorrectly anticipated Q weight-norm vector; the actual diagonal calculation gave `(9,12,6,12,9)`. The assertion was corrected before the final run. The final run exited 0. Both observations are retained; the failed initial assertion is not presented as a successful check.

These are finite checks for (7) and the displayed Q only. The all-variable statement is the written proof in §§1–3, which needs a separate full-scope mathematical review. The example is not a counterexample to original k3. The difference from the f172 hull is a specifically proved comparison at the stated two p values, not a novelty/priority assertion. Parent f200's 1/142 all-density disposition, its disclosed P1 manifest-order MINOR, the previous owner cadence PROCESS MAJORs, all frozen errata and all historical quarantine records remain unchanged.
