# Werner upper zero-six — all-spectrum nonsymmetric output-c forcing and the unclosed mixed residual

Actual `/bin/date` observation immediately before this manuscript: **Sun Oct 25 11:04:42 PDT 2026**. PhysicsResearch96h-2, physics-1. New immutable consolidated successor under `primary-continuation-20261025-102319-v1.json`; separate exposure ACK preceded this body. All predecessor/source bytes remain unchanged.

**NEW WRITTEN PARTIAL FORCING CANDIDATE:** for every positive normalized four-Schmidt spectrum and every complex w with c^T w=0, the actual FULL-q upper-zero energy at the nonsymmetric p test Z=cw^T obeys

```
E_full,c(cw^T)>=(3/4)e3(x)||w||^2,  x_i=c_i^2.             (1)
```

ALL six complex q directions are minimized, and the full original raw correction is retained. This is actual p/q forcing domination on an intrinsic three-dimensional nonsymmetric part of the mixed9 complement, NOT p-only positivity or a selected-spectrum calculation.

**Priority boundary:** (1) is NOT yet the requested mixed9 Schur certificate. In particular it does not bound the subtraction from coupling to the old skew block. Section7 retains the ENTIRE full complex mixed9 residual and states the first unproved corrected-block comparison. Two individually positive compressions are NOT promoted to a positive sum block.

All arithmetic/inequalities below are WRITTEN. No scientific interpreter/eval/program/symbolic calculation/enumeration/solver/replay/compile, new GO, nested agent or model CLI was used. Metadata/source/date/hash operations only. Mandatory v9/v10/v11/HOLD and the parent skew sign-case addendum remain binding. No earlier unadmitted output is a premise.

## 1. Exact full target and named input boundary

The original primary is unrestricted complex rank<=2 three-copy ququart Werner nonnegativity. This is still only the upper-zero leaf of a sufficient co-Choi reference route; full p12/P11, F_up,F_low,Z_low, route composition and W4 eligibility remain separate.

Use

```
c_i>0, sum_i c_i^2=1,
x_i=c_i^2, d_i=1-x_i, D=diag(d_i),
d_ij=(d_i+d_j)/2, Q=I-cc^T,
r=(sum_i1/d_i)^(-1).
```

On H={Z:Zc=0}, retain the ACTUAL operator and six-edge forcing

```
rho'Z=B'Z+rQZ^TQ,
B'Z=D^2Z-D diag(Z_ii)Q,
j_ij(Z)=[d_i(1+d_i)Z_ij+d_j(1+d_j)Z_ji
              +c_i c_j(d_i Z_ii+d_j Z_jj)]/(d_i+d_j).
```

For every complex symmetric zero-diagonal U, F_ij=d_ij U_ij are the six unnormalized physical edge entries. The exact full joint and its minimum are

```
J_full(Z,U)=<Z,rho'Z>-sqrt(2)Re(j^dagger F)
                            +(1/2)F^dagger K_full F,
E_full,c(Z)=min_U J_full(Z,U).
```

K_full is the original full raw kernel, with diagonal `3-2d_ij d_kl/e3(d)` and shared-edge entry `-c_j c_t/(2d_jt)`; disjoint entries are zero. Its coefficients are not replaced by a sampled/diagonal kernel or the old R0 kernel.

Named imports only at their actual written scopes:

- Generic G1-G12 variance/coupling identities: SHA256 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`.
- Full raw correction addendum2, including ALL commutator Gram cross terms: SHA256 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`.
- Literal raw physical matrix definitions: SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`.
- Existing all-spectrum skew-forcing theorem: `werner-upper-zero-consolidated-v2-skew-forcing.md`, SHA256 `3021af178709baa457a97918d5d790e5daeaa7a2bb342cf1097f596294771fc3`,369LF, fully reread before this push.
- Its parent support: RUN/`werner-skew-forcing-parent-v1.md`, SHA256 `0c5880b836423d286a8ef4afe9787f04435de4e7d53fbd8343e09a1bb0e082d0`, read with mandatory `werner-skew-forcing-parent-addendum-1.md`, SHA256 `76fd90f801598c328c42328e9e28d2ec488822fad88671aef02a02168056d597`. ONLY negative mu uses the min(N0,N1) substitution; positive mu uses the direct1/32 bound. V11's original-parent-clock withdrawal remains.

The new proof does not use the inverse-free/polynomial successor, the false global G13 assertion, bare-lift contractivity or p-only H>0 as a forcing certificate. The auxiliary Cauchy-kernel route recorded in the current checkpoint is NOT an input to this simpler output-c forcing proof.

## 2. Keep the exact compatible squares and ENTIRE raw correction

For positive c define

```
g_ij=d_ij-(d_i-d_j)^2/4>0,
m_ij=x_i x_j g_ij,
T_ij=Z_ij/(c_i c_j),
z_ij=U_ij/(c_i c_j), z_ij=z_ji, z_ii=0,
e_ij=c_i c_j(d_i Z_ij+d_j Z_ji),
a_ij=e_ij/(sqrt(2)m_ij).
```

Use the actual weighted directed-row difference form

```
Gamma(V)=sum_i sum_(j<t; j,t!=i)
                 (d_i x_i x_j x_t/2)|V_ij-V_it|^2.
```

The generic identities give B' energy2Gamma(T), the cross

```
-sqrt(2)Re Gamma(T,z)
-(1/sqrt(2))Re sum_(i<j)conj(e_ij)z_ij,
```

and R0 energy `Gamma(z)/2+sum m_ij|z_ij|^2/2`. Completing these actual terms gives the exact FULL identity

```
J_full(Z,U)=R_c(Z)
   +(1/2)Gamma(z-sqrt(2)T)
   +(1/2)sum_(i<j)m_ij|z_ij-a_ij|^2
   +(Qraw(U)-R0(U)),                                    (2)

R_c(Z)=<Z,(B'/2+rF_Q)Z>
        -sum_(i<j)|d_i Z_ij+d_j Z_ji|^2/(4g_ij),
F_Q Z=QZ^TQ.
```

The full raw remainder in(2) is the imported NONNEGATIVE exact Gram, not its diagonal or a zero substitute. Both compatible-square centers remain; none is asserted to vanish independently of the other. The global assertion R_c(Z)>=0 on all H is FALSE and is not revived. Only its new intrinsic output-c restriction is proved below.

## 3. A uniform compressed inverse bound: QD^-1Q<=2Q

For every complex w with c^T w=0,

```
sum_i |w_i|^2/d_i <=2||w||^2.                            (3)
```

This is a compression inequality, NOT D^-1<=2I on the full four-space.

If all x_i<=1/2, every d_i>=1/2 and the assertion is immediate. Otherwise exactly one x_i exceeds1/2. Relabel it x1=A>1/2, put s=1-A, and let w_weak=(w2,w3,w4). The actual complex constraint and Cauchy give

```
|w1|^2<=s||w_weak||^2/A.
```

The positive coefficient of |w1|^2 in `<w,(D^-1-2I)w>` is `(2A-1)/s`. Each weak x_j<=s, and the real function `(1-2t)/(1-t)` decreases on[0,1), so its NEGATIVE coefficient has magnitude at least

```
(1-2s)/(1-s)=(2A-1)/A.
```

Thus the sole positive contribution is at most `(2A-1)||w_weak||^2/A`, and the three negative contributions have at least that total magnitude. This proves(3), with all complex phases and the full dominant/non-dominant simplex covered. No symmetric-spectrum hypothesis or numerical grid is used.

## 4. One exact edge scalar inequality

For a=d_i,b=d_j, S=a+b is in[1,2]. Since `4g_ij=2S-(a-b)^2`,

```
1/(4g_ij) <= S/(8ab).                                   (4)
```

All denominators are positive. To check the direction, multiply through: it becomes

```
8ab <=S[2S-(a-b)^2]
     =8ab+(a-b)^2(2-S),
```

which is exact. This is an entire physical two-variable inequality, not a value at one spectrum.

## 5. The new nonsymmetric output-c forcing bound

Let Z=cw^T with c^T w=0, w arbitrary COMPLEX. Then Zc=0 and `QZ^TQ=0`. In particular no skew-Hermitian or transpose-symmetric assumption is made; nonzero Z here is generally nonsymmetric. Also `||Z||_HS^2=||w||^2`.

Define two scalar spectral moments, distinct from the old skew-subspace labels:

```
A_x=sum_i x_i d_i^2,
B_x=sum_i x_i d_i.
```

The actual p energy is

```
<Z,rho'Z>=<Z,B'Z>
         =A_x||w||^2-sum_i d_i x_i|w_i|^2.               (5)
```

The mass subtraction in(2) is

```
M_c(w)=sum_(i<j)|d_i c_i w_j+d_j c_j w_i|^2/(4g_ij).
```

Apply(4) to this WHOLE nonnegative edge square, retaining its cross term. The resulting Hermitian edge Gram has diagonal entry, at coordinate i,

```
sum_(j!=i)(d_i+d_j)d_j x_j/(8d_i)
 =B_x/8+A_x/(8d_i)-x_i d_i/4,
```

and off-diagonal entry `c_i c_j(d_i+d_j)/8`. On c^T w=0 its entire off-diagonal quadratic is EXACTLY

```
-sum_i x_i d_i|w_i|^2/4,
```

because the full rank-two expression factors through c^T w and its conjugate. Therefore

```
M_c(w)<=sum_i[B_x/8+A_x/(8d_i)-x_i d_i/2]|w_i|^2.         (6)
```

No individual complex cross term was discarded by sign; it was summed using the actual orthogonality constraint.

Combining(5),(6) in the actual remainder R_c gives

```
R_c(cw^T)
 >=[(4A_x-B_x)||w||^2-A_x<w,D^-1w>]/8
 >=(2A_x-B_x)||w||^2/8,                                 (7)
```

where the second line is exactly the compressed estimate(3), with A_x>0. Finally,

```
2A_x-B_x
 =1-3sum_i x_i^2+2sum_i x_i^3
 =6e3(x),                                               (8)
```

by sum x_i=1 and the elementary symmetric identities for the second/third power sums. Thus

```
R_c(cw^T)>=(3/4)e3(x)||w||^2.                            (9)
```

For positive four-Schmidt spectra e3(x)>0, but this margin is SPECTRUM-DEPENDENT and can tend to zero at a sparse face. No uniform positive lower bound on e3(x) is asserted.

Inserting(9) in the exact full identity(2) proves the actual joint certificate

```
J_full(cw^T,U)>=(3/4)e3(x)||w||^2
   +(1/2)Gamma(z-sqrt(2)T)
   +(1/2)sum m_ij|z_ij-a_ij|^2
   +(Qraw(U)-R0(U)) >=0                                 (10)
```

for ALL complex symmetric zero-diagonal U. Minimization over this ENTIRE complex q6 gives(1). This is genuine forcing domination on the output-c compression, not only its p principal energy. It even uses the stronger R0 energy inside the exact completion, while the original FULL raw correction stays explicitly present and nonnegative. The false GLOBAL R_c>=0 assertion is not an input: the restriction(9) has a new complete written proof.

## 6. Actual complementary structure and output-c mixed coupling

Let H={Zc=0}, let A=range(P_a) with `P_a Z=Q(Z-Z^T)Q/2`, and set

```
C={cw^T:c^T w=0},
T={Sigma:Sigma^T=Sigma, Sigma c=0}.
```

These are mutually orthogonal complex spaces of dimensions3,3,6. Thus `H=A directsum C directsum T`, and the previous nine-dimensional complement is `S=C directsum T`. In particular S is NOT the transpose-symmetric space; the output-c part is essential.

The older supported theorem gives E_AA>=I_A/40 for `E=rho'-J_c^dagger K_full^-1J_c`; the NEW result gives

```
E_CC >=(3/4)e3(x) I_C.                                  (11)
```

This does NOT establish their combined block positivity. For the actual C vector, the forcing simplifies to

```
j_ij(cw^T)=c_i(1+d_i-d_j)w_j+c_j(1+d_j-d_i)w_i.
```

The actual mixed A/C block remains

```
E_AC w
 =[(QD^2c)w^T-w(QD^2c)^T]/2
   -J_A^dagger K_full^-1 j(cw^T),
J_A^dagger F=Q[D+D^2,U_F]Q/4,
(U_F)_ij=F_ij/d_ij, (U_F)_ii=0.                         (12)
```

The factor1/4 follows from HS pairing counting each skew edge twice. Both terms in(12) are retained; neither is assumed zero or controlled merely by(11). The output-c contribution cannot be dropped by pretending that S is symmetric. No huge coefficient generation or boundary inverse was used.

## 7. ENTIRE exact remaining mixed9 Schur obligation

Order S as C directsum T. With all actual blocks of E, the FULL original residual is still

```
R9 = [[E_CC,E_CT],[E_TC,E_TT]]
      -[E_CA;E_TA] E_AA^-1 [E_AC,E_AT] >=0               (13)
```

on ALL complex S and for EVERY positive normalized c. In particular the corrected corner

```
E_CC-E_CA E_AA^-1 E_AC >=0                               (14)
```

has NOT been proved by(11). The genuinely mixed A/C subtraction may consume the new margin; no estimate paying it, nor the remaining T coupling in(13), is supplied. Positive compressions on A and C do not justify an elimination of C AFTER A, and no six-dimensional remaining-residual claim is made.

This is the first unproved comparison after the new output-c certificate. The active target remains the ENTIRE(13), not just(14). All K_full coefficients and original raw remainder remain. The inverse-free/polynomial presentation and its unreviewed acceptance boundary are untouched. No exact negative actual full-target residual is delivered, and a failed sufficient lower budget would not be such a direction.

## 8. Scope, limits and continuation

**Delivered new written component:** all-spectrum/all-complex output-c p3/q6 forcing domination with explicit `(3/4)e3(x)` margin and a full positive completion. The proof covers all positive spectra by the actual compressed inverse estimate, not selected symmetric cases or coefficient positivity on samples. No all-H G13 premise, bare lift or p-only positivity is revived.

**Not delivered:** domination of the genuine corrected A/C block(14), the whole mixed9 form(13), full p12/P11, a negative actual route spectrum, the other three canonical leaves, full asymmetric-route composition or unrestricted complex rank<=2 W4. This partial certificate is not reported as completing the present mixed9 assignment or as reducing its original scope.

**Single remaining task:** use the actual forcing/resolvent in(12) and the new positive C budget to dominate ALL blocks of(13), or provide an exact negative actual residual and its distinct W4 eligibility boundary. No separate-component positivity shortcut is permitted. The auxiliary raw-kernel budget in the current checkpoint remains an unapplied route ingredient, not a certificate for(13).

This manuscript is an AUTHOR-WRITTEN candidate pending independent reconstruction; no parent/formal/kernel/human/cross-vendor/executable-certificate/novelty acceptance is claimed. All mathematical identities here were derived in writing, not evaluated by any scientific interpreter. All previous process findings and original October27 cutoff/deadline remain unchanged; this is not a96-hour closeout or an assertion of mathematical exhaustion.
