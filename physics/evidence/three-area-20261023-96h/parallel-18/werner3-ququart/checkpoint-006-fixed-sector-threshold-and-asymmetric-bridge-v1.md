# Checkpoint 006 — exact fixed-sector threshold and the sharper W4 bridge

Before-creation clock observed: **2026-10-23T21:42:51Z**. Owner: physics-1 / PhysicsResearch96h. Status: **CANDIDATE written reconstruction**, no scientific program, CAS, finite replay or new GO. The global W4 question remains open.

This completes the symmetric-GS criterion on the **full eight-dimensional fixed subspace** for eta_t=(1,1,t,t), t>0. It does not silently include the other152 dimensions remaining outside that fixed subspace after checkpoints004/005. A separate direct diagonalization below sharpens the sufficient bridge to W4: the required two-site interval is actually **-3C_B <= S_eta <= C_B**, not necessarily the stronger symmetric interval. The old symmetric sufficient theorem remains valid; a symmetric-GS failure is not automatically failure of this sharper sufficient route.

## 1. Exact candidate conclusion on the fixed eight dimensions

Set s=t^2 and

`k=1/(1+2s)`, `l=s/(2+s)`, `p=kl`.

Then

`k+l=1-3p`, `0<p<=1/9`, `(k-l)^2=(1-p)(1-9p)`.

Define

`M(p)=-5292+118846p-296289p^2-442260p^3+882819p^4`.

There is a **unique** root p_* of M in (0,1/9). On the full fixed subspace the plus form C_B+S_eta is:

- positive definite for p>p_*;
- positive semidefinite with a one-dimensional kernel for p=p_*;
- of negative index exactly one for 0<p<p_*.

Together with checkpoint003's written minus proof, the fixed-subspace symmetric-GS criterion is therefore precisely **p>=p_***. All these new identities and the dependency on checkpoint002's physical table remain CANDIDATE until distinct reconstruction.

In t coordinates this is the reciprocal interval

`s_- <= t^2 <= s_+`,

`s_±=[1-5p_* ± sqrt((1-p_*)(1-9p_*))]/(4p_*)`, `s_- s_+=1`.

At t=0 the earlier hand -2 obstruction excludes symmetric GS; no singular basis substitution at t=0 is used here.

## 2. First exact Schur reduction

Use checkpoint002's complete eight-dimensional basis, remove its strictly positive z_minus scalar, and eliminate its positive2x2 reference block K2. The remaining five-vector form is then written in the basis

`(p_A,p_B,V_A,V_B,z)`,

`V_A=q_A+p_A/2`, `V_B=q_B+p_B/2`, `z=q_AB+q_BA`.

The V directions have zero C_B pairing with the two reference vectors. Define

`L=k+l`, `g=-2t/(1+s)`,

`d=(1-9p)/[3(1-p)]`, `e=8p/[3(1-p)]`.

The complete5x5 form has blocks

`[[T,E,-g*1], [E,J,g*1], [-g*1^T,g*1^T,2+3L]]`,

where 1=(1,1)^T and

`T=[[10l+11p,p],[p,10k+11p]]/[3(1-p)]`,

`E=[[1/3-dk,-e],[-e,1/3-dl]]`,

`J=[[17/6-(3+d)k,-e],[-e,17/6-(3+d)l]]`.

These are congruence/form matrices, not action matrices in a nonorthogonal basis. They follow by substituting V=q+p/2 into checkpoint002's displayed C5,S5,R,K2 and retaining the full Schur term `-2R^T K2^-1R`. In particular the p-z entry is **-g**, not the uncorrected 2g, and the z diagonal is **2+3L**, not 10+3L.

The first block is strictly positive because its diagonal entries are positive and

`det T=70p/[3(1-p)]>0`.

Its exact inverse is

`T^-1=(1/70)[[10/l+11,-1],[-1,10/k+11]]`.

Eliminating T leaves the3x3 form

`[[R,(g/7)v],[(g/7)v^T,Z]]`,

where

`v=(5+6k,5+6l)^T`, `Z=27/7-9p=9(3-7p)/7`,

`R_11=f(k)`, `R_22=f(l)`,

`R_12=R_21=-6p(5+39p)/[35(1-p)]`,

and

`f(x)=[196+86x+91x^2-684x^3+171x^4]/[70(1+x)^2]`.

For a hand reconstruction of the elimination, the first column of T^-1 E is

`[57k^2+16k+7, -3(1-k)(k+9)]^T/[70(1+k)]`;

the second is its k/l interchange. Substituting in `J-E^T T^-1E` gives f and the displayed off-diagonal. The two remaining contractions give Z and `(g/7)v`. These exact expressions use only `l=(1-k)/(1+3k)` and `g^2=8p/(1-p)`.

## 3. Second Schur reduction and hand polynomial certificates

Since Z>0, the remaining condition is positivity of the symmetric2x2 matrix

`H=R-alpha v v^T`,

`alpha=8p/[63(1-p)(3-7p)]`.

The following factorizations provide direct polynomial-identity certificates for its determinant; they are not finite-point checks. Put

`A=161+493p-171p^2-1539p^3`,

`B=-231+342p+513p^2`,

`C=-12p(5+39p)`, `D0=70(1-p)`, `Delta2=(1-p)(1-9p)`.

Then

`tr R=A/D0`, `(f(k)-f(l))/(k-l)=B/D0`, `R_12=C/D0`,

with the middle identity interpreted continuously at k=l. Also

`v_1^2+v_2^2=146-468p+324p^2`,

`(v_1^2-v_2^2)/(k-l)=96-108p`, `v_1 v_2=55-54p`.

The two required numerator identities, obtainable by ordinary multiplication, are

`A^2-B^2 Delta2-4C^2`

`=140(1-p)[-196+5878p-6741p^2-14013p^3]`,

and

`A(146-468p+324p^2)-B(96-108p)Delta2-4C(55-54p)`

`=14(1-p)[3263-16002p+30537p^2]`.

Consequently

`det R=[-196+5878p-6741p^2-14013p^3]/[140(1-p)]`,

`v^T adj(R) v=[3263-16002p+30537p^2]/10`.

The rank-one determinant identity `det(R-alpha vv^T)=det R-alpha v^T adj(R)v` now gives

**`det H=M(p)/[1260(1-p)(3-7p)]`.**

For an independently short coefficient reconstruction of M, it is exactly

`9(3-7p)[-196+5878p-6741p^2-14013p^3]`

`-16p[3263-16002p+30537p^2]`.

No division by det R is used, so this identity remains valid when R is singular.

## 4. Positive trace, unique crossing and inertia

The trace condition cannot be dropped without proof. Here it is uniformly positive. On 0<=p<=1/9,

`A>=161-171/81-1539/729=1411/9`,

so `tr R>=1411/630`. The denominator in alpha decreases while p increases; hence `0<=alpha<=1/140`. The squared norm of v is at most146. Therefore

`tr H=tr R-alpha||v||^2 >=1411/630-146/140=377/315>0`.

Thus this real symmetric2x2 H is positive semidefinite **iff det H>=0**; when det H<0 it has exactly one negative direction.

For the quartic,

`M(0)=-5292<0`, `M(1/9)=34048/9>0`,

and

`M'(p)=118846-592578p-1326780p^2+3531276p^3`

`>=118846-592578/9-1326780/81=36624>0`.

The intermediate value theorem and this strict derivative bound prove the unique root and every stated sign. At the root H has one zero and one positive eigenvalue. All Schur-eliminated blocks and the z_minus scalar are strictly positive, so the fixed-space inertia is transported without any omitted zero mode. Checkpoint003's two exact minus reference kernels are a different sign and do not create a plus zero here.

## 5. Strict improvement over the earlier principal test

A simple exact comparison is t=1/3, so s=1/9 and p=9/209<1/20. Direct integer evaluation gives

`M(1/20)=-22429981/160000<0`.

Since M is increasing, M(9/209)<0. The full fixed plus form therefore has a negative direction at this angle. Yet checkpoint001's p_A,q_A principal quartic passes:

`Q(1/9)=40702/6561>0`,

where `Q(s)=112s^4+316s^3+331s^2+96s-9`.

The new full fixed criterion is genuinely stronger than that principal necessary test. This is an exact co-Choi obstruction, **not** a rank-two Werner witness. It neither proves W4 false nor excludes a different sufficient bridge.

## 6. Exact asymmetric bridge from the already displayed one-site matrices

This deduction is independent of the new five-dimensional formulas. In the v2 switched-complement bridge, let C0,S0 be the one-site co-Choi pair for the first-site ray |0>. On |00>, their normalized generalized eigenvalue is1. On each span{|0a>,|a0>} they are

`C0=[[1,-1/2],[-1/2,1]]`, `S0=[[1,-1/2],[-1/2,0]]`,

so

`det(S0-lambda C0)=-(1/4)(1-lambda)(1+3lambda)`.

On Q tensor Q they are `I-F/2` and `F/2`, whose normalized eigenvalues are likewise1 and-1/3 on the symmetric and antisymmetric parts. Therefore for dim H1>=2,

**`spec(C0^-1/2 S0 C0^-1/2)={1,-1/3}`**,

with multiplicities `n(n+1)/2` and `n(n-1)/2` when n=dim H1. Both eigenvalues occur. For n=1 only1 occurs.

For any two-site reference put `T_B=C_B^-1/2 S_eta C_B^-1/2`. The co-Choi matrix of the full switched-complement map is congruent to

`I-T0 tensor T_B`.

Because T0 and T_B are Hermitian, its eigenvalues are `1-t0*t_B`. For n>=2 it is positive semidefinite **iff**

`t_B<=1` and `t_B>=-3` for every eigenvalue t_B,

or equivalently

**`C_B-S_eta>=0` and `3C_B+S_eta>=0`.**

This is an exact necessary-and-sufficient criterion for this **complete-copositivity sufficient route**, not a claim that complete copositivity is necessary for the underlying rank-two Werner inequality. If these two inequalities hold, the same square completion in v2 proves q3(C)>=0 for arbitrary covectors and rank<=2 operators whose range contains `a tensor eta` (and for the adjoint co-range class). No factorization of the other ray is imposed. No equality classification is extended here.

The old symmetric interval `-C_B<=S_eta<=C_B` is stronger and remains a valid sufficient premise. In particular the new negative fixed plus directions below p_* only obstruct symmetric GS; they do **not** themselves obstruct `3C_B+S_eta>=0`. This distinction may be consequential for returning the angular calculation to W4 rather than treating a stronger auxiliary criterion as the physical target.

## 7. Remaining single W4 obligation

The dimensional residual is **160 total, including the fixed eight**, not160 plus8. Outside those eight there are152 nontrivial-complement dimensions still to reconstruct. The symmetric fixed minus sign is checkpoint003's candidate; its symmetric plus interval is now the explicit quartic above. A globally sufficient W4 route could instead use the weaker lower bound3C_B+S_eta together with the same upper bound. Neither the remaining sectors nor that global asymmetric domination has been proved here. The old full-book boundary, source/novelty uncertainty, and ban on new scientific execution are unchanged.
