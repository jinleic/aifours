# Original k3: an all-physical-p spin-flip coupling of the actual input and rank-three projector

Owner PhysicsDepol4-2, physics-2. Actual native clock before this candidate: **Thu Oct 29 13:52:50 PDT 2026**. This is a new immutable candidate, not an edit of packet 186 or a transfer of its pending f224 review.

**NEW AUTHOR-WRITTEN CANDIDATE, unreviewed and not adopted.** The all-variable inequality below is unconditional for every actual density, actual rank-three complex orthogonal projector, and physical p, but its right-hand side can be negative. It does **not** settle global k3. The state-dependent uniform-over-projectors criterion is likewise sufficient, not claimed for every state. The exact example at p=9/16 is one pure input, not an all-density theorem at that parameter or at p=4/3.

This route uses the actual spin-flip geometry of the SAME input/projector, including an exact constraint coupling the projector's one-body and three-body Pauli budgets. It does not assume R positivity, the one-erasure conjecture, equality packet 183, a prior held mathematical result, or the acceptance of packet 186. The matched public clipped-tail claim of Yuxuan Zhang remains attributed, with its exact uniform subset-weight support/priority boundary unresolved; no novelty clearance is claimed.

## 1. Definitions and exact universal inequality

Let rho be any four-qubit density and Q any orthogonal rank-three projector. Put

`Phi_p(X)=(1-p)X+(p/2)Tr(X)I`, `Lambda_p=Phi_p^tensor4`, `s=1-p`, `t=|s|`,

`epsilon=sign(s)` for t>0, and `Gamma(X)=Y^tensor4 X^T Y^tensor4`.

Write `rho~=Gamma(rho)`, `Q~=Gamma(Q)`, `kappa=Tr(Q Q~)`,

`q=Tr(Q rho)`, `q_tilde=Tr(Q rho~)=Tr(Q~ rho)`,

`d(rho)=(1/2)||rho-rho~||_1`.

For each phase-free Pauli string P define the actual real coefficients `a_P=Tr(rho P)`, `b_P=Tr(Q P)`, and

`A_j=sum_(wt P=j) a_P^2`, `B_j=sum_(wt P=j) b_P^2`,

`S=A_1`, `x=B_1`, `E_t=A_2+t^4 A_4`.

Let `r_1<=r_2<=r_3<=r_4` be the local Bloch radii of this rho and put

`L=r_1+r_2+3r_3+3r_4`, `m=min(L,sqrt(Sx))`.

The product-reference top-three sum is `R3(t)=[3+8t+6t^2-t^4]/16`. The central claim is

`16[R3(t)-Tr(Q Lambda_p(rho))]`

`>= t[8+6t-t^3 -(1-t^2)m -8t^2 epsilon(q-q_tilde) -t sqrt(E_t(15+8kappa))]`. (1)

At t=0 the channel output is I/16 and both sides are zero; epsilon need not be defined there. No upper bound on epsilon(q-q_tilde) has been substituted in (1): it is the exact signed overlap of the same rho and Q at the same p.

### Universal state-dependent all-Q envelope

The same objects satisfy

`0<=kappa<=3`, `x<=min(20,24-8kappa)`,

`|q-q_tilde|<=min(d(rho),sqrt(3-kappa))`. (2)

Define, for `0<=k<=3`,

`F_t(rho,k)=(1-t^2) min(L,sqrt(S min(20,24-8k)))`

`  +8t^2 min(d(rho),sqrt(3-k)) +t sqrt(E_t(15+8k))`,

`M_t(rho)=max_(0<=k<=3) F_t(rho,k)`. (3)

This maximum exists by continuity. Equations (1)–(2) imply, for every physical p,

`K3(Lambda_p(rho)) <= [3+t M_t(rho)]/16`,

`16[R3(t)-K3(Lambda_p(rho))] >= t[8+6t-t^3-M_t(rho)]`. (4)

Consequently `M_t(rho)<=8+6t-t^3` is a sufficient condition for original k3 for this same possibly mixed input and every actual Q. A k maximizing (3) is a scalar relaxation, not asserted to be realized by a physical rank-three projector.

## 2. Exact physical-projector identities

Gamma is implemented by the antiunitary `Theta=Y^tensor4 K`, with `Theta^2=1`, and sends a weight-j Pauli to `(-1)^j P`. The projector Q~ is an actual rank-three projector. Since products of PSD operators have nonnegative real trace, `0<=kappa<=3`.

Pauli Parseval gives

`B_0=9`, `sum_(j=0)^4 B_j=16Tr(Q^2)=48`,

`16kappa=sum_(j=0)^4 (-1)^j B_j`.

Adding and subtracting these equalities gives the exact, SAME-Q constraints

`B_1+B_3=24-8kappa`, `B_2+B_4=15+8kappa`. (5)

All B_j are nonnegative, so `x=B_1<=24-8kappa`. Also `x<=20`: independently align the four actual one-body trace vectors of Q with local Z axes, and denote the diagonal of that rotated Q by z_x. The set `0<=z_x<=1`, `sum z_x=3` is a hypersimplex whose vertices choose three distinct computational strings. The squared norm of the four Z traces is convex in z, so its maximum occurs at a vertex. For three strings a,b,c it equals

`36-4[d(a,b)+d(a,c)+d(b,c)]<=20`,

because at least two coordinates vary and every varying coordinate contributes two to the distance sum. This gives the first part of (2) for every complex Q, without replacing it by a diagonal projector.

For the overlap bound, rho-rho~ is traceless Hermitian. For `0<=Q<=I`, the positive spectral part of rho-rho~ bounds `|Tr Q(rho-rho~)|` by `d(rho)`. On the other hand, `D=Q-Q~` is Hermitian and Theta D Theta^-1=-D, so its spectrum is symmetric under lambda↦-lambda. Since

`Tr(D^2)=6-2kappa`, `||D||_op^2<=Tr(D^2)/2=3-kappa`.

Using `q-q_tilde=Tr[rho(Q-Q~)]` proves the second part of (2). For a pure state `rho=psi psi^dag`, `d(rho)=sqrt(1-C)`, `C=|<psi|Theta psi>|^2`, by the two nonzero eigenvalues ±sqrt(1-C) of the difference of pure projectors.

## 3. Proof of the all-variable gap inequality

Let `c_j=sum_(wt P=j) a_P b_P`. Pauli orthogonality and the local channel eigenvalues give

`16Tr(Q Lambda_p(rho))=3+s c_1+s^2 c_2+s^3 c_3+s^4 c_4`. (6)

Because Gamma reverses odd Pauli weights,

`c_1+c_3=8(q-q_tilde)`. (7)

Thus the odd contribution in (6) is **exactly**

`s c_1+s^3 c_3 = s(1-t^2)c_1+8s^3(q-q_tilde)`. (8)

Cauchy–Schwarz gives `|c_1|<=sqrt(Sx)`. Also c_1 is the expectation in Q of the actual commuting local Bloch Hamiltonian of rho. Its top-three eigenvalue sum is L, and the bottom-three sum is -L; hence `|c_1|<=L` and `epsilon c_1<=m`.

For the even contribution, using (5) in one weighted Cauchy–Schwarz inequality,

`c_2+t^2 c_4 <= sqrt[(A_2+t^4 A_4)(B_2+B_4)]`

`=sqrt(E_t(15+8kappa))`. (9)

Insert (8)–(9) into (6), use `s=epsilon t`, and subtract the exact product-reference polynomial. This proves (1) for t>0. It directly includes negative shrinkage without reflecting either the input or the projector. Bounds (2), monotonicity in x of sqrt(Sx), and maximization over the actual projector's possible kappa prove (3)–(4).

No step assumes individual Pauli-sector overlaps are independently realizable: the budget relations and the parity identity are simultaneously satisfied by the same actual Q/rho pair. Conversely, the scalar maximization over k is a relaxation, and may return a negative or weak gap; it is not an equality characterization of physical projectors.

## 4. Exact strict certificate beyond packet 186's own optimized criterion

Use the actual pure state

`psi=(3|0000>+|0011>+|0101>+|1110>)/sqrt(12)`, `rho=psi psi^dag`. (10)

Every local marginal is diagonal; the four radii are `(5/6,2/3,2/3,2/3)`. Direct Pauli evaluation gives

`S=73/36`, `L=35/6`, `C=0`, `d(rho)=1`,

`A_2=145/36`, `A_3=215/36`, `A_4=107/36`.

All seven nontrivial bipartitions have a nonzero 2×2 coefficient minor: determinant 3 before the common normalization, i.e. determinant 1/4 after normalization. Hence psi is genuinely four-party entangled.

Take the physical parameter `p=9/16`, so `t=7/16`. It lies outside f200's adopted all-density window. Put

`T=8+6t-t^3=43177/4096`, `E=E_t=1084403/262144`,

`u=L^2/S=1225/73`, `k_0=(24-u)/8=527/584`.

We bound (3) for **every** k in [0,3], using no numerical optimization.

### Case 0<=k<=k_0

Here `min(L,sqrt(S min(20,24-8k)))<=L`, `min(1,sqrt(3-k))<=1`, and the even term is nondecreasing. Since `15+8k_0=39-u`,

`F_t(rho,k) <= (1-t^2)L+8t^2+t sqrt(E(39-u))`

`< (1-t^2)L+8t^2+t(48/5) =26747/2560 =: U_0`,

because `(48/5)^2-E(39-u)=58990999/239206400>0`.

### Case k_0<=k<=2

Now `24-8k<=u<20`. Put `y=24-8k`, so `8<=y<=u`. Since d=1,

`F_t(rho,k) <= (1-t^2)sqrt(Sy)+8t^2+t sqrt(E(39-y))`.

The nonconstant expression is concave and has its unconstrained maximum at

`y_0=39(1-t^2)^2 S/[(1-t^2)^2 S+t^2 E]`.

Here `y_0-u=79223837221/10373979995>0`, so the expression is increasing on [8,u] and is at most its value at u, which is strictly below U_0.

### Case 2<=k<=3

Here `min(20,24-8k)<=8`, `min(1,sqrt(3-k))<=1`, and `15+8k<=39`. Thus

`F_t(rho,k) <= (1-t^2)sqrt(8S)+8t^2+t sqrt(39E)`

`< (1-t^2)(81/20)+8t^2+t(51/4)=53167/5120=:U_2`.

Both square comparisons are exact: `(81/20)^2-8S=649/3600>0`, `(51/4)^2-39E=323067/262144>0`. Also `U_2<U_0` and

`T-U_0=1909/20480>0`.

Therefore the new all-Q inequality establishes the strict original comparison

`R3(7/16)-K3(Lambda_(9/16)(rho)) > 13363/5242880`. (11)

This is an exact all-projector statement for the state in (10) at this one physical p. It is not an all-density result at p=9/16.

For contrast, packet 186's optimized **sufficient** criterion fails for the same state and t. Indeed, with `H=A_2+t^2 A_3+t^4 A_4=12456587/2359296`, its optimizer has `x_0-u=412938801007/44654331921>0`, and

`H(39-u)-[(T-L)/t]^2=2129511149/1406533632>0`.

Both T-L and t are positive, so 186's relaxed upper-bound bracket is negative. This compares the exact stated certificates; it does not say the physical k3 inequality fails or that no earlier different proof covers this state. The named f172 pure classes P/U/H/D also fail for the same reason as in 186; at this t the D failure is exactly `39(15-S)-(5+(8-L)/t)^2=717713/1764>0`, while `4S+8C=73/9>64/9`. The rank-one density is therefore outside their fixed-p finite convex hull. No exhaustive prior-region comparison is claimed.

## 5. A common actual complex projector and channel check

For the very same rho and p=9/16, take the actual complex orthogonal rank-three projector onto

`|0000>`, `|0101>`, and `(|0011>+i|1111>)/sqrt(2)`.

Exact matrix/Pauli arithmetic gives

`(B_0,B_1,B_2,B_3,B_4)=(9,6,12,10,11)`, `kappa=1`, `q-q_tilde=1/2`.

The signed same-Q estimate (1) itself gives a strictly positive gap: `6S<(7/2)^2` and `23E<(49/5)^2`, whence its bracket is strictly larger than

`T-(1-t^2)(7/2)-4t^2-t(49/5)=54437/20480`.

So the actual fixed-Q gap is larger than `381059/5242880`. Direct exact application of the original channel yields

`Tr(Q Lambda_(9/16)(rho))=639301/2097152`,

`R3=498847/1048576`, and the actual same-Q gap `358393/2097152`.

The displayed Q is not asserted to be the top-three output projector. The global all-Q bound (11) comes from the separate uniform argument in §4. The same input/projector is also checked at p=2/3 and p=4/3; those are two fixed-object checks, not p=4/3 all-density claims.

## 6. Finite-check scope and review boundary

`frontier-20261029-189-spinflip-budget-exact-check-v1.py`, SHA256 `53fd25928caddf068ea9970bb21832d8c777b314a2fd34ae7d79226a3716c050`, ran once with `python3 -B`, exit 0. It uses only exact standard-library integer/Fraction Gaussian-pair arithmetic and checks the stated Pauli norms, both Q projectors, their exact spin flips/parity budgets and q differences, direct matrix-unit channel traces versus the Pauli expansion at p=9/16,2/3,4/3, intended wrong-transpose detection for the complex Q, and the rational inequalities used in §4. It checks these **two finite Q instances only**. The full all-variable result rests on §§1–3 and needs disjoint written review.

At inputs failing the state-dependent criterion, especially genuinely entangled inputs at intermediate noise, original global k3 remains open. Parent f200's adopted all-density window and its P1 manifest-order MINOR remain unchanged. f224 review of 186 has been dispatched but its verdict is not assumed. No human, independent-model-family, formal/kernel, novelty, source-priority, continuous-service, or historical-process repair is claimed.
