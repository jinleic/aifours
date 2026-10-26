# Four-qubit low-noise majorization: consolidated written frontier and exact quartic noise elimination

Actual `/bin/date` observation preceding this manuscript: **Sun Oct 25 04:54:08 PDT 2026**. Owner PhysicsDepol4 / physics-2. **WRITTEN CANDIDATE at named inherited imports.** This is ONE consolidated manuscript, not a fourth stand-alone incremental note. It includes the complete new Pauli norm proof, signed-map route, actual witness budgets, corrected relaxed controls, and one new full-scope next attack: the exact physical quartic tradeoff in §6.

**Current scientific verdict:** low-noise k=2,3,4 are still OPEN; no actual physical counterexample is supplied. No unrestricted all-p composition is justified. All prior snapshots, reviews and park records remain unchanged.

## 1. Literal target, accepted boundary and assurance

For every four-qubit state rho and every physical replacement parameter0<=p<=4/3, the assigned target is

`lambda(D_p^tensor4(rho)) prec lambda(D_p^tensor4(|0000><0000|))`,

where `D_p(A)=(1-p)A+(p/2)Tr(A)I_2`. Each Ky-Fan comparison concerns ALL actual states, not independent compatible-looking marginal variables.

The parent's `priority-written-dispositions-v1.md` §3 supplies the recorded written-check boundary:

- every mixed/pure input, central k=6..10, every physical p;
- inherited all-state indices1,5,11..15 for every physical p;
- inherited full high-noise interval2/3<=p<=4/3;
- residual: **k=2,3,4 for0<p<2/3**.

Central source `proof-unrestricted-central-indices-v1.md` has SHA256 `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`. The old frozen U2/partial-channel proof and operative addendum retain SHA256 `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a` and `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`. Their certificates were NOT replayed here.

New same-target predecessors consolidated here:

- `low-noise-pair-norm-and-signed-map-v1.md`, SHA256 `5a067a6fb6c746ab0a47c20df2bc6b025986125dd18b2cda0ab045a82c896a83`;
- `low-noise-projector-overlap-budget-v1.md`, SHA256 `7ad282ae26ca9cf96153866e82cd5c16121ea395dfa329da6812d4ca8efc4bb4`.

Their actual review gates are separate; creating a consolidation does not accept unreturned reviews or upgrade either source. The earlier joint-Hessian gap in `joint-projector-Hessian-attack-v1.md` is NOT repaired by consolidation.

All work for this manuscript was WRITTEN reasoning and metadata only. No scientific eval/interpreter/arithmetic program, symbolic computation, enumeration, replay, solver, external-model CLI or nested agent was used. The pre-correction computations disclosed in `resume-computation-disclosure-v1.json` have no executable-verification or retroactive-admission credit. The rational relaxed points below are supplied with literal written formulas, not an accepted exhaustive LP optimum.

No formal/kernel, human, cross-vendor or novelty acceptance is asserted. Yuxuan Zhang's [author-hosted uniform-weight n=4 note](https://yuxuanzhang1995.github.io/agentic-research/songchen-n4/) has the matched complementary clipped-tail mechanism. Its displayed uniform-weight support remains ambiguous at the read interface. `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`, remains binding. There is no clean novelty/priority claim.

## 2. Actual-state/projector coordinates for the remaining channel gap

Use unnormalized identity factors:

`X_s(rho)=sum_(|I|=s) rho_I tensor I_(I^c)`,

`Z(rho)=sum_(i=1..4,a=x,y,z) sigma_a^(i)rho sigma_a^(i)`.

For ANY actual mixed/pure rho, ANY complex rank-k orthogonal projector Pi, k in{2,3,4}, put

`r=Tr(Pi rho)`, `d=1-r`,

`a=3k+1-Tr(Pi X1)`,

`b=3k+3-Tr(Pi X2)`,

`c=Tr(Pi X3)-(k+3)`.

Here a,b,d are nonnegative by the inherited U1/U2_k comparisons and0<=Pi<=I; c may have either sign. This lettering is local to the scalar criterion and is not a denominator coefficient convention.

For0<p<2/3 let

`u=p/[2(1-p)] in(0,1)`, `a3=(1-p)^3 p/2>0`.

The first k product-reference eigenvalues sum to

`(1-p/2)^4+(k-1)(1-p/2)^3(p/2)`.

If G_k is the actual trace against Pi minus this sum, exact expansion of the channel gives

`G_k/a3=c-a u^2-b u-d/u`.                              (1)

Indeed the coefficients of X1,X2,X4 relative to X3 are respectively u²,u,1/u; the identity term cancels. Thus, with

`q(u)=a u^3+b u^2-c u+d`,                              (2)

one has `G_k=-(a3/u)q(u)`. A physical trace violation is exactly q(u)<0. Such a Pi need not already be identified as the leading spectral projector: its trace is a lower bound for the corresponding Ky-Fan sum.

The inherited high-noise endpoint p=2/3 gives, for every actual pair,

`q(1)=a+b-c+d>=0`.                                     (3)

Also q(0)=d>=0. Because q is continuous, nonnegativity for all0<u<1 is equivalent to nonnegativity on[0,1]. The map u↦p=2u/(1+2u) bijects the open intervals(0,1) and(0,2/3).

## 3. Complete all-complex paired-parity norm proof

For complex three-vectors v,w set

`A=(v dot sigma) tensor I + I tensor(w dot sigma)`.

Choose a real axis perpendicular to BOTH Re(v) and Im(v), and independently one perpendicular to Re(w),Im(w). Real rotations to the z-axis are implemented by physical single-qubit unitaries. In these independently rotated coordinates the two local matrices are

`[[0,alpha],[beta,0]]`, `[[0,gamma],[delta,0]]`,

with `|alpha|²+|beta|²=2||v||²` and `|gamma|²+|delta|²=2||w||²`.

In parity order(00,11;01,10),

`A=[[0,C],[D,0]]`,

`C=[[gamma,alpha],[beta,delta]]`,

`D=[[delta,alpha],[beta,gamma]]`.

Both blocks have Frobenius norm squared `2(||v||²+||w||²)`. Since `A^dagger A=diag(D^dagger D,C^dagger C)`,

`||A||_op²<=2(||v||²+||w||²)`.                         (P2)

No Hermiticity or real-coefficient assumption has been made.

For arbitrary complex coefficients w_i on four sites, apply P2 to pairs12 and34, then the triangle and two-term Cauchy inequalities:

`||sum_i wi dot sigma^(i)||`

` <=sqrt(2(||w1||²+||w2||²))+sqrt(2(||w3||²+||w4||²))`

` <=2sqrt(sum_i||wi||²)`.                               (P4)

For a pure psi, let V have the twelve columns sigma_a^(i)psi. Then Z=VV^dagger and

`||V||²=max_(||w||=1)||sum_(i,a) w_(i,a) sigma_a^(i)psi||²<=4`.

Consequently, for every pure rho, `0<=Z(rho)<=4I`; linearity and a pure-state decomposition extend this to EVERY mixed rho:

`Z(rho)<=4I_16`.                                       (Z1)

The physical product spectrum `(4,2,2,2,2,0,...,0)` makes the constant sharp. This proves only k=1 of the old sufficient Z-family. Its original channel k=1 consequence was already known and is not counted as an assigned-index closure.

The identity `Z=2X3-4rho` follows from `sum_a sigma_a A sigma_a=2Tr(A)I-A` on a qubit. Hence

`X3=2rho+Z/2<=2rho+2I`.                                (4)

For pure rho, rank-one interlacing gives lambda_j(X3)<=2 for j>=2. This is NOT a mixed-state assertion: the equal mixture of0000 and1000 has two X3 eigenvalues5/2.

P4's rotation can depend on ONE complex coefficient vector. Several complex vectors need not admit a common local perpendicular axis: `(1,i,0)` together with `(0,0,1)` already spans all three real axes. Therefore applying the same two-block argument to several orthonormal coefficient vectors would require a new proof; no top2,3,4 Gram sum follows automatically.

## 4. Positive signed map: a sufficient route, not an established theorem

Global spin flip `tilde(rho)=sigma_y^tensor4 rho^T sigma_y^tensor4` is positive. Inclusion-exclusion gives

`tilde(rho)=I-X1+X2-X3+rho`.

Define

`B(rho)=I-X1+X2=X3-rho+tilde(rho)`.

The universal reduction estimate `X3>=2rho` gives `B>=rho+tilde(rho)>=0`, and Tr B=8. A sufficient target is

`K_k(B)<=k+2`, k=2,3,4.                                (SB)

Indeed `X3=B+rho-tilde(rho)` and Ky-Fan subadditivity give `K_k(X3)<=K_k(B)+1<=k+3`. With the inherited U2 bounds this would close the corresponding channel index for every physical p. The product B spectrum is `(3,1 repeated5,0 repeated10)`, so SB's constants are sharp.

None of SB2,SB3,SB4 is proved or physically refuted here. A physical failure of this SUFFICIENT signed-map theorem would still not automatically violate the original channel.

## 5. Actual overlap budgets retained in the consolidated interface

From(4), `Tr(Pi X3)<=2r+2k`. Consequently

`k2: c<=1-2d`, `k3: c<=2-2d`.

For k4 the trace bound Tr X3=8 gives the sharper c<=1. Substituting these into(1), and using `2+1/u=2/p`, gives

`k2: G_2/a3<=1-[a u²+b u+(2/p)d]`,

`k3: G_3/a3<=2-[a u²+b u+(2/p)d]`,

`k4: G_4/a3<=1-[a u²+b u+d/u]`.

A STRICT actual violation therefore requires respectively

`a u²+b u+(2/p)d<1`, hence d<p/2 at k2;

`a u²+b u+(2/p)d<2`, hence d<p at k3;

`a u²+b u+d/u<1`, hence d<u at k4.

These are universal actual-state/projector restrictions at the Z1/U2 imports, not a claim that the true leading projector always has excluded low overlap. At d=0 they still leave the central compatibility difficulty. Small d does not justify replacing Pi by a projector containing psi without tracking the changed trace.

## 6. NEW exact noise-elimination theorem: one quartic physical tradeoff

This section eliminates the remaining channel parameter u EXACTLY for each actual pair. It does not assume the stronger sufficient inequality c<=0.

### Scalar theorem

Let a,b,d>=0, c real, and suppose a+b-c+d>=0. For q in(2), the condition `q(u)>=0 for every u in[0,1]` has the following complete case split:

1. If c<=0, it holds automatically.
2. If c>0 and c>=3a+2b, it holds automatically from the endpoint assumption.
3. If0<c<3a+2b and a=0, then b>0 and it holds IFF

`4bd-c²>=0`.                                           (Q)

4. If0<c<3a+2b and a>0, it holds IFF

`D(a,b,c,d):=27a²d²+18abcd+4b³d-b²c²-4ac³>=0`.           (D)

D is a homogeneous QUARTIC polynomial in the four physical deficit/excess variables. This is an exact written scalar decision theorem, not a claim that all actual pairs satisfy its nontrivial interior condition.

### Proof, including all degenerate cases

If c<=0, every coefficient of q is nonnegative. If c>0 and c>=3a+2b, then

`q'(u)=3au²+2bu-c<=3a+2b-c<=0`

on[0,1]. Its minimum is q(1), nonnegative by hypothesis. This covers a=b=0 as well; no division by either coefficient is needed in the endpoint case. Equality c=3a+2b belongs to this endpoint case.

It remains to consider0<c<3a+2b. Then q'(0)<0 and q'(1)>0, while `q''(u)=6au+2b>=0`. The derivative has exactly one zero s in(0,1), the unique minimum.

If a=0, necessarily b>0, s=c/(2b), and `q(s)=d-c²/(4b)`. This is equivalent to(Q).

If a>0, set

`Delta=b²+3ac`, `R=sqrt(Delta)`, `s=(R-b)/(3a)`.

Since c>0, R>b and s>0. The strict interior hypothesis implies `Delta<(b+3a)²`, hence s<1. At the critical point `c=3as²+2bs`, so

`q(s)=d-s²(2as+b)`.

Substitute s and expand its nonnegative subtraction term:

`s²(2as+b)=(R-b)²(2R+b)/(27a²)`

` =[2R³-3bR²+b³]/(27a²)`

` =[2Delta^(3/2)-2b³-9abc]/(27a²)`.

Thus q(s)>=0 is equivalent to

`L:=27a²d+2b³+9abc >= 2Delta^(3/2)`.

Both sides are nonnegative because a,b,c,d are nonnegative in this case. Squaring is therefore reversible; it introduces no extraneous negative branch. Direct written expansion gives

`L²-4Delta³`

` =729a^4 d²+486a³bcd+108a²b³d-27a²b²c²-108a³c³`

` =27a² D(a,b,c,d)`.

Because27a²>0, this has the sign of D. Hence q(s)>=0 iff(D). No derivative root, square root or coefficient sign is asserted from an arithmetic program. This completes all cases. ∎

### Exact equivalence to the original missing channel indices

For EVERY actual rho,Pi, the endpoint hypothesis is already(3). Equations(1)–(2) and the bijection between u and p show that the index-k channel inequality for this SAME pair at ALL0<p<2/3 is equivalent to the scalar theorem's case condition. Thus the full target at each k is exactly:

> For EVERY actual state and complex rank-k orthogonal projector whose coordinates satisfy0<c<3a+2b, prove(D) if a>0 and(Q) if a=0; or give an actual physical pair violating that condition.

This is the ONE consolidated next attack. It is not a narrowed input region, a frequency sample, a rank-matched relaxation or a surrogate norm statement. The outside cases are already settled analytically by c<=0 or the inherited endpoint.

Pure states suffice for proving the channel comparison, by its original linear/Ky-Fan convexity. This does NOT assert that the quartic D itself is convex or that its feasible set is convex. A proposed proof may check the exact predicate on all pure inputs and then extend the original channel inequalities by convex decomposition, rather than incorrectly extending a nonlinear quartic directly.

### Exact physical counterexample interface, if the quartic fails

If an ACTUAL pair satisfies the interior hypotheses and D<0 with a>0, then its q(s)<0 at the exact s above. The exact physical parameter

`p_star=2s/(1+2s)`

lies strictly between0 and2/3 and has `G_k>0`. Therefore that actual Pi is an original-channel counterexample witness without a numerical eigensolver or approximate spectral-ordering assertion.

If a=0,b>0 and4bd<c² in the interior case, take `s=c/(2b)` and `p_star=c/(b+c)`. Again q(s)<0 and the actual trace violates the correct product-reference sum.

No actual pair with either strict failure is supplied here. Rational matrix entries for rho and Pi would give rational a,b,c,d and a rational quartic sign test; the a>0 critical noise can be algebraic. This is a certificate FORMAT, not an executed calculation, a finite search bound or a found witness. A relaxed four-number tuple is not an actual pair.

## 7. Literal relaxed controls and why they are not counterexamples

For clarity, the consolidated controls are the CORRECTED k2 point and the k3,k4 points, not the original k2 point that violated the new norm cut.

The permutation-twirled PPT relaxation uses x=(x0,...,x4), d_s=(81,108,54,12,1), constraints

`0<=x_s<=1`, `0<=(Hx)_t<=1`, `sum_s d_s x_s=16k`,

with

`16H=[[1,4,6,4,1],`

`     [3,8,6,0,-1],`

`     [9,12,-2,-4,1],`

`     [27,0,-18,8,-1],`

`     [81,-108,54,-12,1]]`.

Its subset-size objectives are `t_j=(1/16)sum_s d_s x_s 2^j binom(s,j)`. The following are literal feasible rational controls:

| k | x | Hx |
|---|---|---|
|2| `(49/297,10/297,1/9,2/3,1)` | `(86/297,8/297,0,14/33,6/11)` |
|3| `(25/81,1/27,1/9,1,1)` | `(31/81,1/18,0,5/6,1)` |
|4| `(7/27,1/9,1/3,1,1)` | `(13/27,1/6,0,1/2,1)` |

All entries lie in[0,1]. Their weighted vectors d_s x_s are `(147/11,40/11,6,8,1)`, `(25,4,6,12,1)`, `(21,12,18,12,1)`, summing to32,48,64. Multiplication by the displayed integer matrix16H gives the stated Hx table. For k2, its alternative construction is the convex combination with weights7/11 and4/11 of `(5/21,0,1/21,16/21,1)` and the ACTUAL product-star point `(1/27,5/54,2/9,1/2,1)`; their H-images are respectively `(2/7,0,0,2/3,6/7)` and `(8/27,2/27,0,0,0)`.

The final objectives are

| k | t1 | t2 | t3 | t4 | a | b | c | d |
|---|---|---|---|---|---|---|---|---|
|2|60/11|9|6|1|17/11|0|1|0|
|3|7|12|8|1|3|0|2|0|
|4|11|15|8|1|2|0|1|0|

They saturate their rank-matched U2 bounds t2=3k+3. Their scalar Z traces `2t3-4t4` are8,12,12, at most4k, so the new Z1 scalar cut does NOT exclude these corrected controls. At p=1/2 their relaxed channel gaps are27/1408,5/128,1/64, respectively.

They also fall in the interior branch of §6 and give quartic values respectively−68/11,−96,−8. This is consistent with their relaxed channel violations. It is NOT evidence that an actual rho/Pi violates the physical quartic: the relaxation has not supplied `omega=bar(rho) tensor Pi`, purity/actual projection structure or the required nonlinear compatibility.

In particular, adding(D) to an optimization before proving it for actual pairs would merely impose the desired original-channel conclusion in that branch. It is not an independent certificate. The next attack must derive the physical quartic from real state/projector structure, or realize a strict failure by a valid actual pair; it cannot declare an existing relaxed tuple to be the state.

## 8. Per-index verdicts and the exact common frontier

| index | current actual verdict | exact remaining consolidated condition |
|---|---|---|
|k2| **OPEN** for0<p<2/3; inherited high-noise result unchanged | for every actual pure rho and rank2 Pi in the interior branch, prove(D)/(Q), or supply an actual strict failure; sufficient stronger route `K2(X3)<=5` also remains open |
|k3| **OPEN** for0<p<2/3; inherited high-noise result unchanged | same full physical predicate at rank3; sufficient stronger route `K3(X3)<=6` remains open |
|k4| **OPEN** for0<p<2/3; inherited high-noise result unchanged | same full physical predicate at rank4; sufficient stronger route `K4(X3)<=7` remains open |

The new exact scalar theorem removes the noise quantifier; it does NOT remove the actual-state/projector quantifiers. No actual strict failure has been found. It also shows why solving the original channel problem need not require the stronger universal c<=0 theorem: a positive excess can be compensated by d and the other same-projector deficits. For example the elementary implication d>=c>=0 already makes `q(u)=a u³+b u²+c(1-u)+(d-c)>=0` on[0,1], without asserting such values are realized by any particular state.

The old scalar clipping proof's all-state central contribution, new Z1, signed-map route and overlap budgets are all retained at their exact scope, not counted as several solved problems. Ordinary two-ququart Schmidt reduction is not revived; fixed-P compression cannot discard the off-range block; and the old joint-Hessian's beta-gap is not replaced by the target constant.

**Parkable state:** one consolidated manuscript with one exact full-scope next attack, complete per-index OPEN verdicts and an exact physical witness format if that attack fails. A later substantive development should supersede/consolidate this manuscript rather than append a volume-only fourth incremental note. HOLD/v7, Zhang attribution, inherited certificate boundaries and independent review gates remain unchanged.
