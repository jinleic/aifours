# ALL complex Q0rays, ALL16diagonal entries: uniform strict non-separation of a genuinely coherent PPTrectangle

PhysicsPPT44-2. Actual `/bin/date` before this manuscript: **Sun Oct 25 13:32:33 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction and parent disposition pending.** This is written algebra and explicit finite rank-two moment control, NOTmachine verification. No NEWscientific program/eval/arithmetic interpreter/enumeration/symbolic computation/solver/replay/compile, nativeGO, nestedagentor externalCLI. HOLD/v9/v10/v11, original deadline and disclosed checkpoint013cadence miss remain unchanged.

The interface was frozen after disclosed informal written leads in `checkpoint-029-all-phi-full-D-coherent-rectangle-obstruction-lead-v1.json`, SHA-256 `ecac7bdff8f87da809d83bbd1054e11b238288e59613b2076dca7628a0e6f438`. It is not retroactive preregistration. The weaker phi+-only lead in checkpoint028is not edited or promoted as if it already contained these larger quantifiers.

## 1. Exact theorem, new geometry, and unchanged P44gap

Let Z=diag(1,i,-1,-i), X|j>=|j+1>, Phi_U=vec(U)/2, and

```
Q0=P(Phi_I)+P(Phi_Z), Q1=P(Phi_X)+P(Phi_ZX),
phi=alphaPhi_I+betaPhi_Z, |alpha|^2+|beta|^2=1,
Q_phi=P(phi)+Q1,
D=sum_(i,j=0)^3 d_ijP(ij), d_ijreal,
W=D-Q_phi.                                               (1)
```

Dhas ALLsixteen independent entries, not scalar/two-level/four-offset background. Generic alphabeta!=0is a genuinely non-MEray and gives nonuniform reduced Q_phi; hence it cannot be ANYpositive MEconic sum. The rank3CESrange also excludes a single localfilter orbit of the older <=3MEscalar class at the named range import in `nonME-three-ray-local-filter-escape-ADDENDUM-1-v1.md`, SHA-256 `dded6b0159c6a0155076f006cd18f0e8ba946ac39859f23b4981be0b3fcdd7a9`. The proof below does NOTimport the earlier scalar nonMEPTbound or transfer its conclusion to D.

**Theorem.** If W is nonnegative on EVERYcomplex Schmidt-rank<=2vector, then for every

```
1/2<=s<=2/3, 9/10<=t<=11/10,
```

the actual PPTfamily R(s,t)defined below satisfies

```
Tr[W R(s,t)]>67/9900,
Tr[W rho(s,t)]>67/89100, rho=R/TrR.                       (2)
```

This is uniform over ALLnormalized complex alpha,beta, including MEendpoints and zero entries of phi. It is a full-Dpair-family obstruction, NOTan unrestricted no-go, NOTa claim that R(s,t)has Schmidt number<=2, and NOTdecomposability of D-Q_phion all PPTstates. A different witness may still detect these states; the original full16entryD-(Q0+Q1)route remains open.

## 2. Actual eligible target and its needed moments

Use E_q e_r=|r,r-q>, F_(r,0)=1/2,F_(r,1)=i^r/2, B=F F*. The FULLtarget is

```
R0=F[1 s;s 1]F*, R1=tB,
R2=diag(y0,y1,y2,y3), R3=diag(z0,z1,z2,z3),
y0=y2=t^2/4,
y1=t^2/[4(1+s)]+s/2, y3=t^2/[4(1-s)]+s/2,
z0=z3=(1+s)^2/(4t), z1=z2=(1-s)^2/(4t),
R(s,t)=sum_q E_q Rq E_q*,
N(s,t)=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t.           (3)
```

Its complete four-complex-block PSD/PTproof, rank12/PTrank9, explicit Gaussian-rational rho(1/2,1)with integer real/imaginary entries divided by332, and failures of jointX/J/oldPTface invariance are in `coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md`, SHA-256 `f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37`, Section1. This is the named WRITTENPPTimport, not inherited independent acceptance. The inequality proof here only needs the directly displayed moments below; it does not depend on replaying a PPTchecker.

Write r=(r0,r1,r2,r3)=((1+s)/2,1/2,(1-s)/2,1/2). Split the actual diagonal cost into DISJOINTparts

```
C0=sum_j r_j d_jj+sum_j y_j d_(j,j-2),
C1=(t/2)sum_j d_(j+1,j)+sum_j z_j d_(j,j+1),
Tr(DR)=C0+C1.                                            (4)
```

Let x=2Re(alpha conjugate(beta)). The negative overlaps are

```
Tr[P(phi)R]=1+sx, Tr(Q1R)=2t.                            (5)
```

Product basis tests of Wforce every d_ij>=0since Q_phiis PSD. This is why the diagonal moment majorizations below have the stated direction.

## 3. Explicit TWO-atom SR2moment control for the whole q0/q2cost

Put v_j=(alpha+beta i^j)/2and a_j=|v_j|^2. Then a0+a2=a1+a3=1/2. Fix the RATIONALnumber c=81/400. On the whole state rectangle,

```
y0=y2=t^2/4>=c,
r0r2=(1-s^2)/4>=5/36>c^2,
4y1y3=t^4/[4(1-s^2)]+t^2s/(1-s^2)+s^2
      >=2187/10000+27/50+1/4
       =10087/10000>1.                                  (6)
```

All are written inequalities, not executed evaluations. In particular sqrt(y1y3)>1/2.

Construct nonnegative TWO-component real vectors

```
u0=(sqrt(r0),0),
u2=(c/sqrt(r0),sqrt(r2-c^2/r0)),
E=||sqrt(a0)u0+sqrt(a2)u2||^2>0,
T=(sqrt(a0)u0+sqrt(a2)u2)/sqrt(E),
u1=u3=T/sqrt2.                                         (7)
```

Thus ||u_j||^2=r_j, <u0,u2>=c, <u1,u3>=1/2. E>0because a0+a2=1/2and r0,r2>0. Choose phases tau_j=v_j/|v_j|when v_j!=0and arbitrary unit phases when v_j=0. Let sigma02and sigma13be any unit square roots of tau0tau2and tau1tau3. Put eta=sqrt(y1/y3)>0.

For EACHatom n=1,2, define an ACTUAL4by4coefficient matrix M_nwith entries

```
M_n(j,j)=tau_j u_j(n),
M_n(0,2)=M_n(2,0)=sigma02 sqrt(u0(n)u2(n)),
M_n(1,3)=sigma13 sqrt(eta u1(n)u3(n)),
M_n(3,1)=sigma13 sqrt(u1(n)u3(n)/eta),
all other entries zero.                                 (8)
```

Permuting rows/columns into0,2,1,3makes two2by2blocks. Each has determinant zero: its off-diagonal product equals its diagonal product, including arbitrary complex phases. Hence rankM_n<=2EXACTLY, even at zero components. This is a symbolic finite rank-two construction, not sampled vectors used to infer universal positivity.

Both matrices have ZEROQ1overlap. Their summed diagonal moments are exactly the target q0moments r_j. On q2they use c,cfor rows0,2and eta/2,1/(2eta)for rows1,3. These are at most y0,y2,y1,y3by(6). Therefore universal SR2nonnegativity of Wapplied to these two vectors gives

```
C0>=F_phi:=(sqrt(E)+sqrt(O))^2,
O=(sqrt(a1/2)+sqrt(a3/2))^2.                             (9)
```

Indeed the even diagonal contribution to the phi-overlap vector is sqrt(E)Tand the odd one is sqrt(O)T. Their squared summed norm is exactly F_phi. These controls DO NOTsum to R(s,t); their coherences differ. Only diagonal domination and the actual phi/Q1scores are used. No Schmidt-number upper bound for the target is inferred.

## 4. All-COMPLEXphi lower bound: a uniform q0surplus

Set y=2Im(alpha conjugate(beta)), so x^2+y^2<=1and

```
a0=(1+x)/4, a2=(1-x)/4,
a1=(1+y)/4, a3=(1-y)/4,
E=(1+sx)/4+(c/2)sqrt(1-x^2),
O=(1+sqrt(1-y^2))/4 >=(1+|x|)/4.                         (10)
```

Thus F_phi-(1+sx)is at least

```
H_s(x)=[sqrt((1+sx)/4+(c/2)sqrt(1-x^2))
              +sqrt((1+|x|)/4)]^2-(1+sx).               (11)
```

On EACHof[-1,0]and[0,1], this is concave. The first radicand is concave, the second is affine and positive on each half; the function E+O+2sqrt(EO)is jointly concave and increasing in both arguments. Its geometric-mean concavity follows directly by squaring the two-point inequality, whose difference is a nonnegative multiple of `(sqrt(E1O2)-sqrt(E2O1))^2`. Subtracting a linear function preserves concavity. Consequently the minimum is at x=-1,0or1, not at an unexamined complex phase.

The endpoint values are

```
H_s(1)=sqrt((1+s)/2)-(1+3s)/4,
H_s(-1)=sqrt((1-s)/2)-(1-3s)/4,
H_s(0)=sqrt(281/800)-319/800.                            (12)
```

The first decreases on our s-interval, with minimum

```
delta=sqrt(5/6)-3/4>0.                                  (13)
```

The second is larger than1/6since s>=1/2and sqrt((1-s)/2)>=sqrt(1/6)>1/3. The third is also larger than1/6: sqrt(281/800)>7/12, so H_s(0)>443/2400>1/6. Finally delta<1/6because5/6<(11/12)^2. Thus ALLcomplex alpha,beta, not only phi+, satisfy

```
C0 >= 1+sx+delta.                                       (14)
```

There is no division by a possibly zero v_jand no missing Bloch-sphere boundary.

## 5. Actual complex rank-two q1tests and weighted q1/q3cost

Define indices modulo4:

```
delta_j=d_(j+1,j)-1/2,
beta_j=d_(j,j+1),
gE=sqrt(beta0beta2), gO=sqrt(beta1beta3).
```

Two adjacent q1coordinate kets span only SR<=2vectors. Their actual2by2block has diagonals delta_j,delta_(j+1)and off-diagonal modulus sqrt2/4. Therefore

```
delta_j>0, delta_jdelta_(j+1)>=1/8.                      (15)
```

The following additional ACTUALrank-two tests are independent of phi. Fix j, let k=j-2,r=k-1,l=k+1,A_k=I-i^(-k)Z, and take arbitrary complex z,w with w!=0:

```
M=X[A_k+(z-2)E_jj+sqrt2(wE_rl+w^(-1)E_lr)].               (16)
```

Before the invertible X, the kcoordinate is zero, the jcoordinate is z, and the r/lblock has diagonal product2and off-diagonal product2, hence rank1. Thus rankM<=2. It has only q1/q3entries, so its phi-overlap is ZEROfor every alpha,beta. The two normalized Q1overlaps have equal modulus |z+2|/2, giving Q1score |z+2|^2/2. Its exact Wexpectation is

```
delta_j|z|^2-2Re(z)+2(delta_(j-1)+delta_(j+1))
             +2(beta_(j+2)|w|^2+beta_j|w|^(-2)).
```

Minimizing over the phase/modulus of zand over |w|forces

```
delta_j[2(delta_(j-1)+delta_(j+1))
                       +4sqrt(beta_jbeta_(j+2))]>=1.     (17)
```

Zero betaentries are included by the infimum over finite w; if the infimum were negative, a finite actual wwould already violate positivity. No full-Q0+Q1positivity assumption or backwards restriction transfer has been made.

Put E0=delta0+delta2,O0=delta1+delta3,p=sqrt(E0O0). Equation(15)implies E0O0>=1/2. Summing the reciprocal lower bounds from(17)gives

```
E0(O0+2gE)>=1, O0(E0+2gO)>=1.                            (18)
```

The actual q3weights in(3)have equal opposite geometric means, so weighted AMGMgives

```
C1>=t+(t/2)(E0+O0)+a(gE+gO),
a=(1-s^2)/(2t)>=a_min=25/99.                            (19)
```

If p>=1, C1>=2t. If1/sqrt2<=p<1, (18)and E0+O0>=2pproduce

```
C1>=t+t p+a(1/p-p)
   >=t+(t-a_min)p+a_min/p
   >=t+(t+a_min)/sqrt2.                                 (20)
```

The last function increases on this p-interval because its derivative is at least `t-3a_min>=9/10-25/33=47/330>0`. The same final bound holds when p>=1: sqrt2-1>1/3and t>=9/10imply `t(sqrt2-1)>3/10>a_min`, so2t>t+(t+a_min)/sqrt2. This proves(20)for ALLcases, without claiming these necessary tests are a sufficient universal positivity certificate.

## 6. Combine disjoint resources: explicit rational strictly positive margin

Using(4),(5),(14),(20),

```
Tr[(D-Q_phi)R]>=delta+(t+a_min)/sqrt2-t.
```

This decreases with t, so the minimum is at t=11/10. The elementary WRITTENbounds sqrt(5/6)>91/100and1/sqrt2>7/10yield

```
Tr[(D-Q_phi)R]
 >4/25+35/198-33/100
 =(1584+1750-3267)/9900=67/9900>0.                        (21)
```

No floating-point or kernel check is used. Both radical inequalities follow by squaring positive rationals.

For normalization, on the full rectangle,

```
N<2+11/5+2/3+11/5+5/3=131/15<9,
```

because the fourth term in(3)is at most1089/500<11/5and the last at most130/81<5/3. Dividing(21)proves the second bound in(2).

## 7. Exact scope and replacement of this failed separator branch

The entire arbitrary complex Q0raypluswholeQ1negative geometry with ALLsixteen diagonal background entries is now blocked on this genuine two-parameter coherent PPTrectangle at the WRITTENscope above. This is stronger than a scalar class closure or an isolated rational PPTcontrol. The concrete integer/332state lies inside the rectangle and cannot be certified by ANYWof(1), even though its Schmidt number is NOTestablished here.

The old fixed-Qscalar and arbitrary<=3MEscalar barriers are NOTbeing transferred. The proof is new direct rank-two moment control plus exact complex necessary tests for the actual family. It does not prove all D-Q_phidecomposable, cover arbitrary off-diagonal positive backgrounds, exclude other actual PPTinputs, or settle unrestricted P44. The original fullD-(Q0+Q1)with all four negative rays remains genuinely outside this theorem and remains a live primary route; no scalar/two-level reset is authorized.

The first remaining primary gap is still an actual explicit rational PPTstate with a universally COMPLEXSR2nonnegative negative separator, or an unrestricted no-go. No such Schmidt3pair, machine certificate, symmetric-extension obstruction, formal/kernel, human/vendor/family, novelty/SOTAor stronger acceptance is claimed. This source only establishes the displayed exact pair-family obstruction, pending separate reconstruction; nativeN4status and old21table stronger gates remain unchanged. No new scienceGOor deadline reset.
