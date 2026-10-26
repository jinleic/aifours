# Low-noise resumption: a uniform Pauli norm bound and a signed-map obstruction

Observed clock preceding this packet: **Sun Oct 25 04:16:46 PDT 2026**, actual `/bin/date` output. Owner PhysicsDepol4, slot physics-2. This is a NEW packet; no predecessor is edited.

**Verdict:** the assigned unrestricted low-noise inequalities at **k=2,3,4 remain OPEN**. There is no exact physical counterexample and therefore no composition into an unrestricted all-p theorem. A new elementary, all-complex written proof below establishes the k=1 Pauli-Gram norm bound that the old Z-route left uncertified. It does **not** establish the required k=2,3,4 sums. A different sufficient signed-map route is isolated, and explicit rational relaxed controls show that neither its plain twirled-PPT version nor adding the new scalar norm cut closes the channel gap.

## 1. Assurance, parent correction and imports

Every new mathematical claim in this packet is **WRITTEN**, not proof-assistant/kernel verified, human reviewed, cross-vendor reviewed or parent accepted. No new result inherits the central packet's separate review.

The resumption assignment and checkpoint026 incorrectly said exact scientific eval arithmetic was automatically exempt from HOLD v2. Main withdrew that exception during this work. **No scientific computation has been made after the correction.** Before it, two exact Fraction active-constraint enumerations were performed in eval, and a third cell failed immediately while importing unavailable sympy. The complete disclosure, observed outputs and chronology limits are in `resume-computation-disclosure-v1.json`. Those enumerations have **NO automatic scientific/verification credit**. No optimum/completeness claim below relies on accepting them. The rational feasible points in §§5–6 are instead supplied with a short, written reconstruction. Their computational discovery provenance is not hidden. There was no native solver, external-model CLI, subprocess, background scientific job, installation or retry.

Named inherited boundaries:

- `proof-unrestricted-central-indices-v1.md`, SHA256 `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23`, and run-root `priority-written-dispositions-v1.md` §3: all-state central k=6..10 for every physical p, at the parent's recorded written-check boundary.
- The frozen partial package and operative addendum named there: U2 at k=2,3,4 and the all-input high-noise interval. Its old rational certificates are imports, **not replayed here**.
- `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/zlemma-route/FROZEN_STATEMENTS.md` §1: the sufficient Z inequalities, including its previously unclosed k=1 complex local-Hamiltonian norm statement. §2 describes the old PPT obstruction. This packet does not convert those old numerical observations into proofs.
- `residual-low-noise-witness-profile-v1.md`: the exact same-state/same-projector noise eligibility identity used in §6.
- `source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`: binding prior-overlap qualification.

In particular, Yuxuan Zhang's [author-hosted n=4 uniform-weight note](https://yuxuanzhang1995.github.io/agentic-research/songchen-n4/) has the matched complementary clipped-tail mechanism. The exact uniform-weight support remains ambiguous at the read interface. The present elementary norm argument and signed-map reduction do not restore a clean novelty or priority claim, resolve that ambiguity, or certify a full public solution.

## 2. An exact two-qubit complex-coefficient norm lemma

For complex three-vectors u,v, let

`A=(u dot sigma) tensor I_2 + I_2 tensor (v dot sigma)`.

**Lemma P2 (WRITTEN, unrestricted complex coefficients).**

`||A||_op^2 <= 2(||u||_2^2+||v||_2^2)`.                 (P2)

Here coefficient norms use complex absolute squares. No Hermiticity of A is assumed.

*Proof.* For u, choose a real unit vector orthogonal to BOTH Re(u) and Im(u). Such a vector exists in R^3, including the cases of dependent or zero real/imaginary parts. A real rotation sending it to the z-axis is implemented by a single-qubit unitary. Consequently u dot sigma is unitarily similar to an off-diagonal matrix

`[[0,alpha],[beta,0]]`, with `|alpha|^2+|beta|^2=2||u||_2^2`.

The same independent construction for v gives entries gamma,delta and preserves its coefficient norm. These are similarities of the actual operators; no nonunitary change of basis or Schmidt-spectrum substitution is used.

Order the two-qubit basis by even parity `(00,11)` followed by odd parity `(01,10)`. In that order A has the form

`A=[[0,C],[D,0]]`,

where

`C=[[gamma,alpha],[beta,delta]]`,

`D=[[delta,alpha],[beta,gamma]]`.

Both blocks have squared Frobenius norm

`F=|alpha|^2+|beta|^2+|gamma|^2+|delta|^2`

` =2(||u||_2^2+||v||_2^2)`.

Since `A^dagger A=diag(D^dagger D,C^dagger C)`,

`||A||_op^2=max(||C||_op^2,||D||_op^2)<=F`.

This proves P2 by the operator-norm/Frobenius-norm inequality on two literal two-by-two blocks. All coefficients may be complex. ∎

## 3. Four-qubit consequence: the formerly uncertified k=1 Z bound

For arbitrary complex w=(w1,w2,w3,w4), define

`L_w=sum_(i=1)^4 wi dot sigma^(i)`,

`S12=||w1||^2+||w2||^2`, `S34=||w3||^2+||w4||^2`.

Apply P2 on physical pairs12 and34, then the triangle and two-term Cauchy inequalities:

`||L_w|| <=sqrt(2S12)+sqrt(2S34)`

`          <=2sqrt(S12+S34)`.

Thus

`||L_w||_op^2<=4 sum_i ||wi||^2`.                         (P4)

For a pure state psi, let V have the twelve columns `sigma_a^(i)psi`. Then

`Z(psi)=V V^dagger`,

`||V||_op^2=max_(||w||=1) ||L_w psi||^2<=4`.

It follows that

**Theorem Z1 (WRITTEN).** For EVERY mixed or pure four-qubit state rho,

`0<=Z(rho)=sum_(i,a) sigma_a^(i)rho sigma_a^(i)<=4I_16`.     (Z1)

The mixed case follows by linearity and a pure-state convex decomposition. Sharpness is witnessed by a physical product state: `Z(0000)` has eigenvalues `(4,2,2,2,2,0,...,0)`.

This closes only **k=1** of the old sufficient Z family. It is a real unrestricted auxiliary statement, but the original channel k=1 comparison was already known; it is NOT a new solution of any assigned low-noise index.

Using `X3=2rho+Z/2`, Z1 gives the all-state operator inequality

`X3(rho)<=2rho+2I`.                                      (N)

For PURE rho, rank-one interlacing implies `lambda_j(X3)<=2` for j>=2, while `lambda_1<=4`. This pure-state spectral statement is not asserted for mixed inputs. For example, the equal mixture of0000 and1000 has two X3 eigenvalues5/2, so extending the second-eigenvalue cap to mixed states would be false.

Neither (N) nor its pure-state interlacing consequence gives the required sums5,6,7 at k=2,3,4. In particular, replacing the unknown whole spectrum by its largest-eigenvalue cap is not a majorization proof.

The pair proof cannot simply be applied to several complex coefficient vectors with one common rotation: at a given physical site the real and imaginary parts of several vectors can span R^3. For example the local coefficients `(1,i,0)` and `(0,0,1)` have no common real perpendicular axis. This identifies a missing step in that proposed extension; it is not a claim that all multi-vector arguments fail.

## 4. A different sufficient route through a positive signed two-body map

For all four-qubit states define

`B(rho)=I-X1(rho)+X2(rho)`.

Global spin-flip inclusion-exclusion gives exactly

`B=X3-rho+tilde(rho)`.

The reduction estimate `X3>=2rho` yields

`B>=rho+tilde(rho)>=0`, `Tr B=8`.

For each k in{2,3,4}, the new sufficient obligation is

`K_k(B(rho))<=k+2` for every rho.                          (SB_k)

If SB_k were proved, positivity of tilde(rho), Ky-Fan subadditivity and `K_k(rho)<=1` would give

`K_k(X3)=K_k(B+rho-tilde(rho))`

`       <=K_k(B+rho)<=K_k(B)+1<=k+3`.

The inherited U2_k bound and the common-order channel bridge would then prove that same index for every physical p. This is a genuine sufficient route to the original target, not a replacement target declared solved.

For the product state, B has spectrum `(3,1 repeated5,0 repeated10)`, so the constants in SB_k are sharp. But **none of SB_2, SB_3, SB_4 is proved or physically refuted here**. Z1 alone does not imply them.

## 5. Literal rational controls for the signed-map relaxation

The inherited local-unitary twirled PPT relaxation can additionally be permutation-twirled. Write its five real variables as x_s=16c_s, s=0..4, with

`d=(81,108,54,12,1)`.

Its constraints are

`0<=x_s<=1`, `0<=y_t<=1`, `d dot x=16k`,

where y=Hx and

`16H=[[1,4,6,4,1],`

`     [3,8,6,0,-1],`

`     [9,12,-2,-4,1],`

`     [27,0,-18,8,-1],`

`     [81,-108,54,-12,1]]`.

Equivalently, entry16H_(t,s) is the coefficient of z^s in `(1+z)^(4-t)(3-z)^t`. With `E_S` as in the inherited proof, these constraints make `omega=sum_S (x_|S|/16)E_S` positive, satisfy its cap and trace, and make both PPT inequalities hold. They do **not** make omega a product `bar(rho) tensor Pi` with one pure rho and an actual rank-k projector.

For any subset-size map Phi_j, its relaxed objective is

`t_j=(1/16)sum_s d_s x_s 2^j binom(s,j)`.

Thus t0=k; the signed-map objective is `k-t1+t2`; and the spin-flip objective is `sflip=(1/16)sum_s (-1)^s d_s x_s`.

The following THREE controls require no exhaustive optimization claim:

| rank k | x=(x0,x1,x2,x3,x4) | y=Hx |
|---|---|---|
|2| `(5/21,0,1/21,16/21,1)` | `(2/7,0,0,2/3,6/7)` |
|3| `(25/81,1/27,1/9,1,1)` | `(31/81,1/18,0,5/6,1)` |
|4| `(7/27,1/9,1/3,1,1)` | `(13/27,1/6,0,1/2,1)` |

Their weighted-coordinate vectors d_s x_s are respectively

`(135/7,0,18/7,64/7,1)`, `(25,4,6,12,1)`, `(21,12,18,12,1)`.

These sum to32,48,64. All displayed x,y coordinates lie in[0,1]. This proves feasibility directly. For clarity, multiplying the integer matrix16H by the integer-numerator versions of these x vectors gives respectively

`(96,0,0,224,288)/21`,

`(496,72,0,1080,1296)/81`,

`(208,72,0,216,432)/27`.

Dividing each by16 gives exactly the tabled y. These are written rational calculations on the displayed formulas, not a claim of replaying or accepting the prior enumeration.

The objectives are

| k | t1 | t2 | t3 | t4 | sflip | B objective | desired SB_k |
|---|---|---|---|---|---|---|---|
|2|32/7|9|46/7|1|6/7|45/7|4|
|3|7|12|8|1|1|8|5|
|4|11|15|8|1|1|8|6|

In particular, each control already saturates its **rank-matched U2 bound**, t2=3k+3. It is not enough to append that bound to this relaxed optimization. These points also satisfy the scalar expectations `B>=rho+tilde(rho)` and `X3>=2rho`; this does not assert the full underlying physical operator constraints for a nonexistent rho.

The k2 control violates the new Z1 rank-matched scalar cut `2t3-4t4<=4k`; it must NOT be retained unchanged after adding Z1. Section6 repairs that relaxed control by a convex mixture, rather than silently ignoring the new cut.

## 6. Even the new norm cut leaves exact low-noise relaxed violations

The actual product-star rank-two projector gives the feasible point

`x_star=(1/27,5/54,2/9,1/2,1)`,

`Hx_star=(8/27,2/27,0,0,0)`.

For it `(t1,t2,t3,t4,sflip)=(7,9,5,1,0)`; equivalently its weighted coordinates are `(3,10,12,6,1)`.

Mix the k2 control of §5 with x_star, with weights7/11 and4/11. The result is

`x_2^new=(49/297,10/297,1/9,2/3,1)`,

`Hx_2^new=(86/297,8/297,0,14/33,6/11)`.

Convexity proves feasibility. Its weighted coordinates are `(147/11,40/11,6,8,1)`, summing to32. Its objectives are

`(t1,t2,t3,t4,sflip)=(60/11,9,6,1,6/11)`.

It now SATURATES the Z1 scalar cut: `2t3-4t4=8=4k`.

Keep the k3 and k4 controls of §5. They have `2t3-4t4=12`, which equals4k at k3 and is below4k at k4. Thus all three final relaxed controls satisfy the new norm cut.

For the same-projector noise variables

`d1=3k+1-t1`, `d2=3k+3-t2`, `d4=1-t4`,

`delta3=t3-(k+3)`, `u=p/[2(1-p)]`,

the final controls give

| k | d1 | d2 | d4 | delta3 |
|---|---|---|---|---|
|2|17/11|0|0|1|
|3|3|0|0|2|
|4|2|0|0|1|

The exact channel-relaxation gap, with a3=`(1-p)^3 p/2`, is

`a3[delta3-u^2 d1-u d2-d4/u]`.

At the rational physical parameter **p=1/2**, one has u=1/2 and a3=1/32. The relaxed gaps are therefore exactly

- k2: `(1/32)(1-17/44)=27/1408>0`;
- k3: `(1/32)(2-3/4)=5/128>0`;
- k4: `(1/32)(1-2/4)=1/64>0`.

More generally these same controls violate the relaxation whenever, respectively, `u^2<11/17`, `u^2<2/3`, `u^2<1/2`. Each is a nonempty low-noise interval inside0<p<2/3. No root approximation is needed.

**These are NOT physical counterexample states.** No factorization of omega as `bar(rho) tensor Pi`, no density-matrix amplitudes and no actual rank-k projector are supplied. The controls prove a limitation of the specified relaxed route, not falsity of SB_k, U3_k or the channel conjecture. They do not prove that every conceivable use of the central operator bound is insufficient. In particular they do not impose all nonlinear actual-state/projector compatibility, nor a simultaneous system involving all other projector ranks.

## 7. Per-index written verdicts and parkable frontier

| index | actual all-input/all-p result of this resumption | exact unresolved obligation | route verdict |
|---|---|---|---|
|k=2| **OPEN** on0<p<2/3; inherited high-noise result unchanged | prove `K2(X3)<=5`, or a direct channel bound, or supply an actual exact state/projector/noise counterexample | new uniform Z1 is true as WRITTEN; signed-map/PPT-plus-norm-cut route is still loose by the explicit27/1408 relaxed gap at p1/2 |
|k=3| **OPEN** on0<p<2/3; inherited high-noise result unchanged | prove `K3(X3)<=6`, or a direct channel bound, or an actual exact counterexample | same relaxed route is loose by5/128 at p1/2 |
|k=4| **OPEN** on0<p<2/3; inherited high-noise result unchanged | prove `K4(X3)<=7`, or a direct channel bound, or an actual exact counterexample | same relaxed route is loose by1/64 at p1/2 |

The new sufficient SB_k obligations are4,5,6 for the positive signed map B. They are NOT necessary conditions for the original channel conjecture, and a physical failure of SB_k alone would not be a channel counterexample.

The first remaining nontrivial step for the pair-norm route is a multi-vector estimate controlling the top2,3,4 Pauli-Gram singular values, not another k1 operator-norm estimate. For the signed-map route, an additional actual-state/projector compatibility inequality must exclude the literal rational controls above; adding only the already-known rank-matched U2 bound and the new scalar Z1 cut does not do so.

The former joint-Grassmannian-Hessian gap is not silently repaired. This packet changes representation and supplies a new uniform auxiliary lemma plus exact method controls, but does not transfer that old beta-gap Hessian to the target constant.

There is no unrestricted composition because three required low-noise indices remain unproved. Zhang attribution, novelty UNCLEAR, inherited verification boundaries and the corrected global HOLD all remain binding. New mathematics is **WRITTEN**, not WRITTEN_CHECKED_IN_KERNEL or a scientific certificate accepted from the pre-correction eval output.
