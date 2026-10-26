# Werner upper zero — GLOBAL positive nonanchor pivots and a legal one-scalar row gate

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Actual preceding `/bin/date`: **Sun Oct 25 18:27:20 PDT 2026**, precreation observation only. Same ENTIRE all-positive-spectrum full complex p12/q6 task. No scientific interpreter/eval/calculator/program/CAS, enumeration, solver/replay, test/build, scientific CLI, nested agent or GO. Exact symbolic/rational WRITTEN reasoning only, including private scoping; NOT checked-in-kernel.

OWN private-written-exactness major `70c38388c31b1a3d58520be8d00e6a57335a6c3423a533d2d1a6f8258fe48deb`, own earlier cadence finding, zero-credit old arithmetic and all parent/owner/HOLD histories remain. Correct math does not clear process. This new body follows the ACTUAL v103-B RETURN; no primary work during its live review is claimed or performed. Original October27 cutoff/deadline unchanged.

## 1. Exact inputs and what is being attacked

Consume actual-raw v7 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`, whole signed-row v8 `f970e53b71dba7c5c4cd28e32144d51ce37021447c135a1bf6b51ee713449d1d`, global row-budget v9 `1a41695f8bbde665338e4daca4fdba41713472cdb20d9490ac78add2a277b616`, full-mass v10 `8fd87df6cd19dfc1ddd3205ee59ebc090cddb2c962ef337abcf87a2b75350938`, and maximal-anchor v11 `ed3358376965bd005bc3ef8f76ce13560c2296a81d559eb43fef7995ed3f1485` at their complete named generic G1-G12/false-G13-correction/ENTIRE raw-Gram/physical P4-P10/literal residual/v24 union. NOT false G13, bare dual lift, unproved P11, private approximate guidance or external science.

All ci>0, sum ci^2=1, xi=ci^2, di=1-xi, r=(sum1/di)^(-1), and Z is COMPLEX with Zc=0. The ORIGINAL full E_full retains the entire common-q6 compatibility minimum as in v11 AT9. This paper investigates an EXPLICITLY STRONGER SUFFICIENT row route to standalone Praw. It is not asserted necessary for the original target, and a negative lower-row scalar would not be a negative E_full witness.

For row i put a=di, xi=1-a and cR=(cj)_(j!=i). Its actual row form is

```
R_i(z)=sum_(j<t;j,t!=i)omega_(i;jt)|ct zj-cj zt|^2
       +(r/xi)|sum cj zj|^2.
```

Let

```
q_ij=di*dj/(4gF_ij), kappa_ij=r-q_ij,
B_ij=di^2/(4gF_ij)+|kappa_ij|di/dj
    =(a/dj)max(r,2q_ij-r).
```

The v8 pair-Cauchy bound is Praw>=sum_i z_i^dagger M_i z_i, with M_i=R_i-diag(B_ij). No sign of all M_i has yet been proved. V8 correctly rejected positivity of its different bare D_i^0-diag B; that obstruction is NOT contradicted here.

## 2. A legal diagonal-plus-positive-rank-one LOWER metric

V9 proved globally

```
omega_(i;jt)>=m(a):=a(1-a+a^2)/(1+a),
m(a)>=2r/(2-a)+rho(a), rho(a)>0.
```

The weighted Lagrange identity gives

```
R_i>=a*m(a) I +sigma_i cR cR^dagger,
sigma_i=r/xi-m(a)>0.                                    (LR1)
```

Here positivity of sigma is not guessed. Concentrating the three other x values in the exact harmonic bound gives

```
r>=a*xi/[1+2a*xi].
```

Writing H=a*xi,

```
sigma_i>= a/(1+2H)-a(1-H)/(1+a)
        =a[a^2+2H^2]/[(1+a)(1+2H)]>0.                   (LR2)
```

Thus define the ACTUAL-budget lower row matrix

```
K_i=diag_(j!=i) A_ij +sigma_i cR cR^dagger,
A_ij=a*m(a)-B_ij,
M_i>=K_i.                                               (LR3)
```

Unlike the old invalid pivot, this uses the full row variance lower bound and retains a proved POSITIVE rank-one term. Bare A values are not all presumed positive.

## 3. NEW GLOBAL theorem: every NONANCHOR bare A is strictly positive

Choose an index0 with maximal x0. V11 proves kappa_i0>0 for every i!=0; all edges incident to ANY maximum are positive. For the anchor row0, all budgets are baseline B_0j=r*d0/dj, hence M_0=N_0>0 already by v9. Only a nonanchor row i needs the following analysis. Its remaining columns are0,j,k, with x0>=xj,xk and a=x0+xj+xk.

Each nonanchor remaining xj<a/2, because x0>=xj and the third positive coordinate is retained. Consider its actual edge sign.

### 3.1 Nonnegative kappa: direct strict baseline bound

If kappa_ij>=0, then B_ij=r*a/dj. Since dj=1-xj>=1-a/2,

```
A_ij/a=m(a)-r/dj>=m(a)-2r/(2-a)>=rho(a)>0.              (LR4)
```

The strict positive interior is retained even if the edge coefficient itself is0.

### 3.2 Negative kappa: use the COUPLED pair harmonic bound

If kappa_ij<0, v11 gives xi+xj<1/2. Thus a>1/2 and, writing b=dj and S=a+b, one has3/2<S<2. V10's ACTUAL gF>dij gives

```
q_ij<ab/[2(a+b)],
B_ij/a=(2q_ij-r)/b < a/(a+b)-r/b.                       (LR5)
```

Do NOT insert a fixed-row harmonic endpoint independently of the other x values. Keep the fixed PAIR coupled. With T=2-S=xi+xj, the complementary d values have sum1+T and product at least T. Their reciprocal sum is therefore at most(1+T)/T, giving

```
r>=r_pair=ab*T/[ab(1+T)+T(a+b)].                        (LR6)
```

Consequently

```
a/(a+b)-r/b <=F(a,b)
 :=a^2*b*(3-a-b)/[(a+b) W0],
W0=ab(3-a-b)+(2-a-b)(a+b)>0.                            (LR7)
```

### 3.3 Exact monotonicity, not an optimizer assertion

For fixed a in(1/2,1), F increases strictly with b on3/2<=a+b<=1+a. Set

```
S=a+b, T=2-S, H=3-S,
W0=abH+TS.
```

The sign of partial_b F is the sign of

```
D=b S^2+H T S(a-b)-a b^2 H^2.                           (LR8)
```

This follows by differentiating bH/(S W0); its numerator is

```
(aH-bS)W0-bHS[aH-ab+T-S],
```

which expands exactly to(LR8).

If a>=b, then

```
D=b[S^2-abH^2]+HTS(a-b)>0,
```

because ab<=S^2/4 and H<=3/2. If a<b, let delta=b-a<=2-S=T and b>=S/2. The same bounds give

```
D>=S[(S^2/2)(1-H^2/4)-H T^2]
 >=S[63/128-3/8]=15S/128>0.                             (LR9)
```

Here S>=3/2,T<=1/2,H<=3/2; every bound is an exact rational inequality. No program, root finder or numerical maximization is used.

Thus F(a,b)<=F(a,1). Direct algebra yields

```
m(a)-F(a,1)
 =a(1-a)[1-2a^2(1-a)]
       /[(1+a)(1+2a(1-a))]>0.                           (LR10)
```

The bracket is positive since a>1/2 and a^2<1: it exceeds1-2(1-a)=2a-1. Combining(LR5)-(LR10) proves A_ij>0 also for EVERY actual negative nonanchor edge.

Therefore, for EACH nonanchor row i, BOTH nonanchor columns j,k have strictly positive A_ij,A_ik. Only its column0 can have a nonpositive bare A. This theorem retains actual full masses in the budget; replacing them by the simpler pair bound is used only in the indicated upper estimate.

## 4. Exact ONE-scalar gate with legitimate positive pivots

For fixed nonanchor row i write

```
p=x0>0, u=xj>0, v=xk>0,
A0=A_i0 (not presumed positive), Aj=A_ij>0, Ak=A_ik>0,
sigma=sigma_i>0,
V=u/Aj+v/Ak.
```

The tail2x2 block diag(Aj,Ak)+sigma*c_tail*c_tail^dagger is genuinely positive. Its elementary rank-one inverse is legitimate because Aj,Ak>0 have been PROVED. Schur elimination gives EXACTLY

```
K_i>=0 iff
Phi_i:=A0+sigma*p/[1+sigma V]>=0.                        (LR11)
```

No inverse of A0 or of an indefinite bare diagonal occurs. If A0>=0, this condition is automatically strict. If A0<0, (LR11) is an unproved explicit scalar comparison, not an already established certificate.

Thus Phi_i>=0 for all three nonanchor rows would prove M_i>=0, then Praw>=0, then the ORIGINAL full E_full>=0. This is ONLY a sufficient route. Conversely Phi_i<0 would defeat this uniform-minimum-omega lower metric, not necessarily M_i, Praw or E_full. The actual q6 compatible minimum must remain if this stronger estimate fails.

The fully equivalent original frontier is STILL the anchored at-most3-edge Gram of v11, with its entire positive L_+=N+C_comp+positive edge forms. The present scalar row gates do not replace that target or transfer a sign to the other three canonical operators.

## 5. Remaining gap and exact assurance

NEW GLOBAL WRITTEN progress: a legal positive-rank-one lower row metric; a coupled pair-harmonic estimate; exact derivative factorization proving the negative-branch budget bound; strict positivity of BOTH nonanchor bare pivots in every nonanchor row; and a valid ONE-scalar Schur gate instead of the known false all-bare-positive pivot.

Still UNPROVED: Phi_i>=0 uniformly when A_i0<0; all M_i signs; standalone Praw globally; the actual anchored-triangle deficit Gram; full generic E_full/Z_up; other three canonical signs and W4. No exact full-target separator or physical Werner witness. Central-region and boundary-collar candidates do not silently cover the remaining simplex.

Next genuine action: prove or exactly reject(LR11) using the ACTUAL r/gF/coefficient coupling. A rejected lower-row test demands return to the ENTIRE original Gram/q6 interface, not suppression of a warning or a false full-target claim. All source bytes remain unchanged; full source-union reconstruction/parent disposition is needed before promotion. No formal/kernel/human/configured-family/executable/triple-witness/novelty acceptance or permission to park. Original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 unchanged.
