# Four genuinely independent cyclic background levels: all-PPT obstruction through exact mixed-state Schmidt-two replacement

Actual `/bin/date` before writing: **Sun Oct 25 12:02:05 PDT 2026**. PhysicsPPT44-2. **AUTHOR-WRITTEN CANDIDATE; cross-domain reconstruction and parent disposition pending.** Continued original P44primary. No scientific interpreter/eval/arithmetic program, enumeration, solver, replay or compile; metadata/source/clock/hashonly. HOLD and v9/v10/v11remainbinding; checkpoint013's earlier cadence deviation is not cured.

## 1. A genuinely broader positive geometry and exact theorem

Indices are modulo4. Use Z|j>=i^j|j>, X|j>=|j+1>and the full orthonormal Weyl Bell basis

```
Phi_pq=vec(Z^pX^q)/2, p,q=0,1,2,3.
```

Let

```
H_q=sum_(r)P(r,r-q),
Q_q^+=P(Phi_0q)+P(Phi_1q),
Q_q^-=P(Phi_2q)+P(Phi_3q), H_q=Q_q^++Q_q^-,
Q=Q_0^++Q_1^+.
```

The witness class in this theorem is

```
D=sum_(q=0)^3 d_q H_q,
W=D-Q, all FOURd_q>=0 independent.                      (1)
```

This is not merely the accepted two-level class: d0need not equal d1and d2need not equal d3. For d0,d1<1and d2,d3>0it has four negative eigenvalues; Qrank4cannot be a three-term conic sum. The accepted strict two-positive/non-CCPheadroom at aH+bL-Qpersists under sufficiently small four-offset perturbations by compactness/uniform strict positivity and openness of negative PTspectrum. Thus genuine non-two-level members exist; no certified numerical perturbation is claimed or needed here. This distinguishes the new literal class without claiming escape from the decomposable cone whose membership is the conclusion.

The named headroom input is Section5of `anisotropic-Weyl-positive-background-consolidated-v1.md`, SHA-256 `fa39d6a671455eec40a7f05b0c48ec80cd3b63f0b395920609de8611a8d64d3c`, at the actual accepted `ppt-anisotropic-background-parent-v1.md` boundary. The non-detection proof below does not need that nonemptiness input; it only prevents treating the enlarged class as an empty formal extension.

**Theorem.** Every universally COMPLEXrank-two-nonnegative W in(1)is nonnegative on EVERY4 by4PPTstate. Equivalently it is decomposable at the named finite-dimensional cone-duality boundary below. No symmetry of the original tested state is assumed; the lossless symmetries belong to W.

A consequence for the FULL16-entry diagonal route is that any actual negative PPTtarget must break joint cyclic translation X tensorX. Breaking only the stronger J=(X tensorI)SWAPsymmetry is not enough.

The proof directly settles the whole four-offset class and the complete mixed uniform-high-noise state cone. It does not infer the mixed case by composing the earlier equal-coherence/noise and unequal-low-only closures. It uses a new exact rank-two frame and an objective-preserving PPTreplacement. Older frozen packets remain unchanged and are not retroactively broadened.

## 2. Full-complex witness criterion is retained, not replaced by symmetry controls

For strictly positive d_q, let alpha_ij=d_(i-j). For EVERYcomplex4 by2isometry S define

```
A_j=S*diag(alpha_0j,...,alpha_3j)S,
V_j=[(1/2)S*U_a e_j]_a, U_a in{I,Z,X,ZX},
G_D(S)=sum_j V_j* A_j^(-1)V_j.
```

Then W is two-block-positive iff G_D(S)<=I4for EVERYsuch S. Indeed C=SZhas positive energy E=sum z_j*A_jz_jand negative-overlap vector h=sum V_j*z_j. The exact whitened norm is lambda_max(G_D); if g>1an eigenvector choice z_j=A_j^-1V_jvproduces E=g,h=gvand negative expectation g-g^2. This includes all complex planes and rank-one Cby extension, with no real/sample substitution.

The proof below assumes actual universal two-positivity in this sense, not that a finite selection passed. At zero coefficients it uses the definition directly, or the usual D+epsilonIregularization; no singular inverse is inserted. Its obstruction also does not require solving the full positivity parameter region.

## 3. Lossless Bell dephasing and a permitted antiunitary symmetry

W is invariant under the LOCALunitaries V tensor conjugate(V), V=X^kZ^n. Conjugation by Zmultiplies Phi_pqby i^qand conjugation by Xby i^(-p), so their16joint characters are distinct. Twirling any PPTdensity matrix over this finite group is PPT, preserves Tr(Wrho), and gives a Bell-diagonal state

```
rho=sum_(p,q)r_pqP(Phi_pq), r_pq>=0.                    (2)
```

The background(1)is invariant because jointXshifts both product indices and keeps their difference, while diagonalZonly adds phases. No original state symmetry is assumed.

There is one additional real-linear symmetry. Let Kdenote GLOBALcomplex conjugation in the computational basis and set

```
Theta=(Z tensorI)K.
```

It sends Phi_pqto Phi_(1-p,q), since Xis real. Consequently Theta W Theta^-1=W. This operation is NOTasserted to be a physical completely-positive quantum channel; it is used only as a positivity/PPT-preserving mathematical symmetry. Full complex conjugation preserves PSD and PPT, and the subsequent local unitary does too.

The expectation is preserved exactly: invariance implies `(Z* tensorI)W(Z tensorI)=conjugate(W)`, so

```
Tr(W Theta rho Theta^-1)
 =Tr(conjugate(W) conjugate(rho))
 =conjugate(Tr(Wrho))=Tr(Wrho).
```

The final equality uses Hermiticity. Averaging the Bell-diagonal state with its Thetaimage therefore gives, still without loss of objective,

```
rho=sum_(q=0)^3[x_q Q_q^++y_q Q_q^-], x_q,y_q>=0.         (3)
```

This allows arbitrary low-sector coherent differences, not just diagonal low noise. No claim of Schmidt monotonicity under a partial/nonpositive transpose has been made.

## 4. Exact PPTcriterion for the FULL eight-coefficient state

Put

```
S_q=x_q+y_q, Delta_q=x_q-y_q.
```

The product diagonals in sector qare S_q/2. Replacing Q_q^-=H_q-Q_q^+, write(3)as sum_q y_qH_q+Delta_q Q_q^+. The signed Delta_qare real and may be negative.

After Bob transpose, total-index sectors tauare invariant. For tau=0and2, reordering to difference0then difference2gives diagonal blocks(S0/2)I2and(S2/2)I2. Their off-diagonal blocks are, respectively,

```
K_even=[(1-i)Delta1 I2+(1+i)Delta3 T]/4,
K_even T,
T=[0,1;1,0].                                          (4)
```

For tau=1and3, the same statement holds with diagonals S1/2,S3/2and

```
K_odd=[(1+i)Delta0 I2+(1-i)Delta2 T]/4,
K_odd T.                                              (5)
```

These follow by applying each normalized projector directly:

```
(Q_q^+)^Gamma|r,s>
 =(1/4)(1+i^(s-r+q))|s+q,r-q>.
```

There are no other PTentries. Since T=T*=T^-1and the two coefficients in each Kdiffer by a pure ifactor,

```
K_even K_even*=(Delta1^2+Delta3^2)I2/8,
K_odd K_odd*=(Delta0^2+Delta2^2)I2/8.                    (6)
```

Equivalently diagonalizing Tproduces two ordinary2 by2blocks with the same off-diagonal modulus. This gives the COMPLETEPPTcriterion, including zero diagonals:

```
2 S0 S2>=Delta1^2+Delta3^2,
2 S1 S3>=Delta0^2+Delta2^2.                             (7)
```

If a diagonal factor is zero the right side must be zero, so no hidden Schur inverse or nondegenerate branch is required.

## 5. Objective-preserving low-coherence replacement — not a physical monotonicity claim

Replace only the two low sectors in(3)by

```
rho'=x0Q_0^++y0Q_0^-+x1Q_1^++y1Q_1^-
                        +(S2/2)H2+(S3/2)H3.            (8)
```

This sets Delta2=Delta3=0while keeping ALLproduct diagonals, the trace and the highQoverlap unchanged. It is PSD. It is also PPTby(7), because dropping those squares only weakens the inequalities.

Consequently

```
Tr(Wrho')=Tr(Wrho).                                    (9)
```

No quantum channel or global Schmidt-number monotonicity is inferred from this replacement. It is a specifically constructed PPTstate with the SAMEobjective for the witness class(1). The next section proves that rho'has Schmidt number<=2by a complete new explicit identity. That suffices for the obstruction; SN(rho)itself is not claimed<=2.

## 6. Complete mixed six-coefficient PPTstate theorem

Consider any nonzero operator

```
R=x0Q_0^++y0Q_0^-+x1Q_1^++y1Q_1^-+z0H2+z1H3,
all coefficients>=0.                                  (10)
```

It is PSD. Its exact PPTconditions, from(7), are

```
4 S0 z0>=Delta1^2,
4 S1 z1>=Delta0^2.                                     (11)
```

We prove EVERYsuch PPToperator has Schmidt number<=2after normalization.

If S0=0, (11)forces Delta1=0, so x1=y1and R is product-diagonal. The S1=0case is symmetric. Both zero also give a product-diagonal operator. These cases include all endpoints without division.

Now suppose S0,S1>0. Define the LARGER quadratic roots

```
A0=[S0+sqrt(S0^2-Delta0^2)]/2>=S0/2>0,
A1=[S1+sqrt(S1^2-Delta1^2)]/2>=S1/2>0,
a=sqrt(A0), h=sqrt(A1),
b=Delta0/(2a), g=Delta1/(2h), u=h/a>0.                  (12)
```

All roots are real: S_q^2-Delta_q^2=4x_qy_q>=0. The signed real b,gmay be zero or negative. The root identities give

```
a^2+b^2=S0, 2ab=Delta0,
g^2+h^2=S1, 2gh=Delta1.                                (13)
```

Use the literal matrix

```
C=[a   b/u  0   g ]
  [h   b    0   ug]
  [0   g    a   b/u]
  [0   ug   h   b ].                                   (14)
```

Its second row is utimes its first and its fourth row utimes its third. The first and third rows are independent because a>0, so rank(C)=2over the full complex field.

Apply the SAMEsixteen LOCALunitary operations

```
C_(n,e,k)=X^k Z^e (Z^n C Z^(-n)) X^(-k),
n=0,1,2,3, e=0,1, k=0,1.                              (15)
```

Here is a full symbolic accounting, not a finite computed table.

First naveraging removes every cross group between the four distinct difference sectors. In difference0the remaining diagonal vector is(a,b,a,b), hence its Weyl coefficients are(a+b)/2on Iand(a-b)/2on Z^2. In difference1the vector is(g,h,g,h), with coefficients(g+h)/2on Xand(g-h)/2on Z^2X. Difference2has only ug(E13+E31); difference3only(b/u)(E01+E23).

LeftZaveraging e0,1pairs the phase indices0/1and2/3. JointXaveraging k0,1then cancels the remaining cross terms between phase indices0and2(and1and3), because their conjugation characters differ by-1. Thus the high terms become exactly

```
[(a+b)^2/2]Q_0^++[(a-b)^2/2]Q_0^-
 +[(g+h)^2/2]Q_1^++[(g-h)^2/2]Q_1^-,
```

which equals the high part of(10)by(13). The low opposite-position cross terms cancel under leftZas before (phases i,-ior1,-1), and jointXfills all four positions in each low sector. The resulting low coefficients are

```
z0'=(ug)^2/2=Delta1^2/(8A0),
z1'=(b/u)^2/2=Delta0^2/(8A1).                           (16)
```

Therefore the FULLoperator identity is

```
R'=(1/16)sum_(n,e,k)P(vec C_(n,e,k))
   =high part of(10)+z0'H2+z1'H3.                       (17)
```

Every one of the sixteen vectors has rank2and the same finite norm. From A0>=S0/2and A1>=S1/2,

```
z0'<=Delta1^2/(4S0)<=z0,
z1'<=Delta0^2/(4S1)<=z1,                                (18)
```

using the actual PPTconditions(11). Hence

```
R=R'+(z0-z0')H2+(z1-z1')H3                              (19)
```

is an explicit conic sum of sixteen rank-two projectors plus at most eight product projectors, ALLwith nonnegative coefficients. Normalizing by the positive trace gives a convex Schmidt-rank-at-most-two decomposition. If a coefficient in(18)vanishes, the corresponding product terms are omitted. The matrices remain rank2when Delta0orDelta1is zero; no inverse of those quantities occurred. This proves the entire theorem, including arbitrary signs of the coherent differences and every zero-weight boundary.

Explicit convex weights are available without another check. Let `N=2(S0+S1)+2(ug)^2+2(b/u)^2`, the squared norm of every matrix in(15), and `T_R=2(S0+S1)+4z0+4z1=TrR`. Each normalized rank-two vector has weight `N/(16T_R)`. Each of the four product positions in H2has weight `(z0-z0')/T_R`, and each of the four in H3has weight `(z1-z1')/T_R`. Their sum is exactly1by(16)and(19), and every weight is nonnegative; N>0in the current S0,S1>0case.

This contains the earlier unequal-low-only family as a corner, but no previous unreviewed decomposition is a premise. It directly proves the MIXEDuniform-high-noise case, rather than assuming the older closures glue.

## 7. Whole four-offset witness obstruction and decomposability boundary

Starting with ANYPPTdensity matrix, Section3produces the Bellpair form(3)with the SAMEWexpectation. Section5produces the PPTstate(8), again with the SAMEexpectation. By the complete theorem in Section6, (8)has Schmidt number<=2. Therefore actual universal rank-two positivity of Wgives

```
Tr(Wrho)=Tr(Wrho')>=0 for EVERYPPT rho.                  (20)
```

This is the full unrestricted-tested-state theorem for ALLfour independent background levels(1), not only a theorem about selected controls.

If the map-language conclusion “decomposable”is desired, use the named finite-dimensional cone-duality import: the dual of the PPTcone is PSD+Gamma(PSD). The latter sum is closed here: for any convergent sequence P_n+Q_n^Gamma, the PSDtraces sum to the bounded trace of that sequence, bounding each P_n,Q_n; compact subsequences give PSDlimits. PSDself-duality, self-adjointness of Gammaand the finite-dimensional bipolar theorem therefore supply W=P+Q^Gamma. This is an EXISTENTIALdecomposition, not a displayed P,Qmatrix formula or executable SDPcertificate. Equation(20)already proves the physical non-detection claim independently of that terminology.

## 8. Consequence for the FULL16-entry diagonal route and exact remaining primary step

Let Dnow have arbitrary sixteen diagonal entries. If the ACTUALtested PPTstate is invariant under joint cyclic translation X tensorX, averaging W(D)over those four local conjugations preserves two-block positivity and the target expectation, and reduces Dto the four-offset form(1). Equation(20)therefore excludes every such target.

The actual-target hypothesis is essential. For a nonsymmetric Dand a non-translation-invariant state, shifting the state would change the objective and is NOTlicensed. Thus the full arbitrary-D/G_D/four-complex-PPT-block residual remains open; no all-Ddecomposability or P44no-go is asserted. Any successful target in that route must now break joint cyclic translation, not merely J. The minimal-coherence asymmetric ratio ttargets and mixed but uniform high-noise targets are genuinely settled at this new boundary if reconstructed.

Remaining science must retain actual coordinate asymmetry, the same sixteen Dentries, all four coupled complex PTblocks and the ENTIREall-plane Gram condition, or use an essentially different negative/positive geometry. The full P44state with a sound universal negative separator remains missing. Non-diagonal completions and other negative spaces are not covered by this theorem.

All statements are author-WRITTEN candidates until genuine cross-domain reconstruction/parent pass. No SOTA/novelty, formal/kernel, scientific execution, human/cross-vendor or publication gate is claimed. Older frozen sources, old21tableunreconstructed status, N4historicalUNKNOWN/oldexit and cutoff/deadline remain unchanged. Currentprimarycontinues; no newGO is requested.
