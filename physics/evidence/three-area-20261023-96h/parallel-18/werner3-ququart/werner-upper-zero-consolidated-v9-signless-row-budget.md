# Werner upper zero — GLOBAL signless-row inverse budget and exact negative-edge frontier

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Immediately preceding actual `/bin/date`: **Sun Oct 25 17:00:59 PDT 2026**, precreation observation only. Same ENTIRE all-positive-spectrum full complex mixed9/p12q6 target, not a selected-spectrum replacement. All new mathematics is WRITTEN, not checked-in-kernel.

The complete serial v93-B/v93b privacy review was ACTUALLY RETURNED to Main before primary checkpoint019 and BEFORE this primary reading/derivation resumed. Its return does not confer any physics acceptance. No scientific interpreter, calculator/eval, symbolic/numerical program, enumeration, solver/replay, test/build, scientific CLI, new GO or nested agent. HOLD v2 and additive v9/v10/v11 histories, original October27 cutoff/deadline and all existing process findings remain.

## 1. Exact consumed input and unchanged full target

The COMPLETE211LF `werner-upper-zero-consolidated-v7-full-raw-ground-state.md`, SHA256 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`, supplies the ACTUAL full-raw kernel/masses and exact common-q6 completion. The COMPLETE180LF `werner-upper-zero-consolidated-v8-signed-row-metrics.md`, SHA256 `f970e53b71dba7c5c4cd28e32144d51ce37021447c135a1bf6b51ee713449d1d`, supplies the actual row form and shows why its bare post-budget diagonal cannot be presumed positive. Both bodies were actually read completely after the serial-review RETURN and before this successor.

The raw import union remains: generic G1–G12 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`; FALSE-G13 addendum1 `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`; ENTIRE raw Gram addendum2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`; physical kernel/Schur P4/P10 `1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`, NOT P11; literal four residuals `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`; original v24 operative-identity support `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`. No region theorem, unadmitted arithmetic or external theorem is a premise of the NEW row inequalities here. Ordinary imports: elementary Hermitian finite-matrix algebra, positive-operator inverse order, complex square expansions and the harmonic/arithmetic mean inequality.

For ALL ci>0, sum ci^2=1, put xi=ci^2, di=1-xi, r=(sum1/di)^(-1). Every test Z is COMPLEX with Zc=0. The ACTUAL full-raw residual is

```
Praw(Z)=sum_i sum_(j<t;j,t!=i) omega_(i;jt)|ct Zij-cj Zit|^2
        +r sum_ij conj(Zij)Zji
        -sum_(i<j)|di Zij+dj Zji|^2/(4gF_ij),
omega_(i;jt)=di(di^2+dj dt)/[(di+dj)(di+dt)].             (SR1)
```

Here gF is the actual v7 mass, including all commutator row sums, not only a correction diagonal. The original E_full equals Praw PLUS the minimum of the TWO actual compatible q6-square sums in v7 GFR11. They retain ONE common symmetric six-edge vector with varying beta centers. Neither that minimum nor negative terms below are suppressed.

## 2. NEW global quantitative row-weight lower bound

Fix row i and write a=di in(0,1). For any two other indices j,t put b=dj, s=dt, h=dl, so a+b+s+h=3 and all four values lie in(0,1). Set S=b+s and P=bs. Then

```
2-a<S<2,  P>S-1,
omega=a(a^2+P)/(a^2+aS+P).
```

For fixed S the last expression increases strictly with P, its derivative being a^2 S/(a^2+aS+P)^2. Substitution P=S-1 gives

```
omega >= a/(1+a) * (a^2+S-1)/(a+S-1).
```

The right side increases with S, with derivative a^2(1-a)/[(1+a)(a+S-1)^2]. Thus the following is GLOBAL, not a reference-family estimate:

```
omega_(i;jt) >= m(a):=a(1-a+a^2)/(1+a).                 (SR2)
```

The boundary value is attained by the appropriate two-support limit b=1,s=1-a,h=1. Interior inequalities are strict. Meanwhile sum_other d=3-a and the harmonic/arithmetic mean inequality give

```
r <= r_max(a):=a(3-a)/(3+8a).                           (SR3)
```

Define

```
P(a)=3-13a+21a^2-8a^3,
rho(a)=a^2 P(a)/[(1+a)(3+8a)(2-a)].
```

Direct clearing of positive factors yields

```
m(a)-2r_max(a)/(2-a)=rho(a).                            (SR4)
```

Crucially P(a)>0 on[0,1], with an exact short proof. If a<=1/2 put v=1/2-a; then

```
P(a)=3/4-2v+9v^2+8v^3
    =9(v-1/9)^2+23/36+8v^3>0.
```

If a>=1/2 put v=a-1/2 in[0,1/2]; then

```
P(a)=3/4+2v+9v^2-8v^3 >=3/4+2v+5v^2>0.
```

Combining gives the NEW uniform-in-other-coordinates strengthening

```
omega_(i;jt) >= 2r/(2-a)+rho(a),  rho(a)>0.              (SR5)
```

This is stronger than v8's omega>r and pays a precisely matched inverse-diagonal metric below. No scalar spot check or floating approximation enters the proof.

## 3. NEW exact signless identity and full inverse-diagonal domination

Still fix row i. Let cR=(cj)_(j!=i), so |cR|^2=a, and put

```
u=cR/sqrt(a),  P_u=uu^dagger,  Q_u=I-P_u,
yj=xj/a,  sum_(j!=i)yj=1,
D_R=diag_(j!=i)(dj)=I-a diag(y).
```

There are THREE remaining coordinates. The Hermitian matrix

```
S_u=I-2diag(y)+P_u
   =sum_(j<t;j,t!=i) (ut e_j+uj e_t)(ut e_j+uj e_t)^dagger             (SR6)
```

is a positive signless weighted triangle Gram. With all three uj>0 it is STRICTLY positive: a zero test would have z_j/uj=-z_t/ut on all three edges, and the odd cycle forces every entry0. This argument uses full complex tests.

Set

```
L_i = [2/(2-a)] Q_u + [1/(1-a)] P_u,
L_i^(-1)=(1-a/2)I-(a/2)P_u.
```

The EXACT identity

```
D_R-L_i^(-1)=(a/2)S_u >=0                              (SR7)
```

and positive Hermitian inverse order therefore give

```
D_R^(-1) <= L_i,
C_i:=L_i-D_R^(-1)>=0.                                  (SR8)
```

C_i is strictly positive in the full interior. This is Loewner inverse order between the displayed POSITIVE operators, not entrywise inverse order, not inversion of a signed diagonal, and not Sherman–Morrison with an assumed positive bare pivot. It bypasses exactly the v8 RFR9 obstruction rather than denying it. In particular it also implies the compression bound

```
Q_u D_R^(-1) Q_u <= [2/(2-a)] Q_u,
```

but the FULL operator inequality(SR8), including the common cR direction, is what is used.

## 4. A GLOBAL positive row-budget theorem

For row off-diagonal vector z=(Zij)_(j!=i), the actual constraint fixes Zii=-(sum cj zj)/ci. Let

```
R_i(z)=sum_(j<t;j,t!=i) omega_(i;jt)|ct zj-cj zt|^2
       +(r/xi)|sum_(j!=i)cj zj|^2,
N_i=R_i-r a D_R^(-1)
```

where the last line denotes Hermitian row matrices. Write v_jt=ct e_j-cj e_t. The weighted Lagrange identity is

```
sum_(j<t) v_jt v_jt^dagger =a I-cR cR^dagger=a Q_u.
```

Using the ACTUAL varying omega weights and(SR8) gives the EXACT decomposition

```
N_i =sum_(j<t) [omega_(i;jt)-2r/(2-a)] v_jt v_jt^dagger
      +r a C_i.                                        (SR9)
```

Every coefficient in its first sum is at least rho(a)>0 by(SR5), and C_i>=0. Consequently, for EVERY positive four-spectrum and EVERY complex row,

```
R_i(z) >= r di sum_(j!=i)|Zij|^2/dj,                    (SR10)
N_i >=a rho(a) Q_u+r a C_i>0                            (interior).
```

The strict statement follows from C_i>0; it is not a claim of a uniform margin up to sparse boundary. This theorem is not one of the previously unproved row M_i signs: it is a NEW globally proved baseline budget. It retains the exact positive and negative rank-one effects from v8 through the whole row variance/common-direction identity, rather than dropping the negative update or presuming the bare diagonal positive.

## 5. Exact full-raw decomposition isolates all remaining negative edge coefficients

Define for each edge

```
q_ij=di dj/(4gF_ij),
kappa_ij=r-q_ij,
s_ij(Z)=sqrt(di/dj) Zij+sqrt(dj/di) Zji.
```

Subtract the six reciprocal row budgets in(SR10) from(SR1), pairing rows i and j. Exact expansion gives

```
Praw(Z)=sum_i z_i^dagger N_i z_i
        +sum_(i<j) kappa_ij |s_ij(Z)|^2.                (SR11)
```

For example the |Zij|^2 coefficient in the last term is `r di/dj-di^2/(4gF_ij)`, and its cross coefficient is `2r-di dj/(2gF_ij)`, exactly the original swap-minus-edge coefficients. The identity is over ALL complex Zc=0 and uses the ACTUAL full masses.

Thus the original full target is equivalently

```
E_full,c(Z)=sum_i z_i^dagger N_i z_i
       +sum_(i<j) kappa_ij |s_ij(Z)|^2
       +min_(ONE common symmetric complex z6)
             {the TWO compatibility sums in v7 GFR11}.  (SR12)
```

This is a genuine new representation of the full original problem. The baseline row matrices are now globally positive. Only the explicitly negative-kappa edges, where present, and their payment by the positive row surplus plus actual compatible q6 minimum remain. Their pair forms are not independently zeroed, and the old false constant-half G13 is not an input.

In particular define the explicit semialgebraic region

```
Gamma={x_i>0,sum xi=1 : 4r gF_ij>=di dj for ALL six edges}.
```

On Gamma, (SR11) proves Praw>0 for every nonzero Zc=0, and hence the ACTUAL E_full>0/generic Z_up>0 there. This is not a selected one-parameter family. Gamma contains a nonempty open interior neighbourhood of the uniform spectrum: at xi=1/4, the actual values are `r=3/16`, `gF=15/16`, `q=3/20`, and `kappa=3/80>0` on every edge. These values follow directly from the displayed actual K_full row sums; they are WRITTEN, not replayed computations.

## 6. Exact negative-coefficient control: Gamma is NOT silently the whole simplex

At the positive interior spectrum

```
x=(7/10,1/10,1/10,1/10),
d=(3/10,9/10,9/10,9/10), W=729/500, r=3/20,
```

consider an edge between two of the three small x values. Its actual dij=9/10, complementary dkl=3/5, and K_full diagonal is

```
3-2(9/10)(3/5)/(729/500)=61/27.
```

The shared-edge ratios in the mass formula are2 because di=dj. The total outside x mass is4/5, so

```
gF=(81/100)(61/27)-(9/20)(8/5)=111/100,
q=(81/100)/(444/100)=27/148,
kappa=3/20-27/148=-6/185<0.                             (SR13)
```

This is an exact WRITTEN countercontrol to dropping all negative-kappa terms. It is NOT a negative N_i, NOT a negative Praw, NOT a negative E_full or Z_up, and NOT a physical Werner witness. In this spectrum the negative edges form the triangle among the three small coordinates, but no claim that this is the universal negative-edge pattern is made. No finite enumeration or program was launched.

## 7. Exact frontier and assurance

NEW GLOBAL WRITTEN theorems: the sharp-in-other-coordinates omega lower bound(SR2), the quantitative strengthened harmonic comparison(SR5), the full signless inverse metric(SR7)–(SR8), and the actual row-budget PSD theorem(SR9)–(SR10). NEW EXACT full-raw representation(SR11)–(SR12) isolates negative edge coefficients while retaining the ENTIRE compatible q6 minimization. A genuine multidimensional region Gamma is settled; the explicit interior control(SR13) prevents pretending Gamma is all spectra.

Still NOT_PROVED: payment of the negative-kappa pair forms by the global positive N_i plus actual compatible q6 minimum for EVERY positive spectrum; standalone Praw sign globally; full generic E_full/Z_up; the other three canonical F_up/F_low/Z_low signs; whole co-Choi route and unrestricted rank<=2 W4. No exact full-target falsifying spectrum is delivered. No sparse-boundary inverse or endpoint extension is evaluated here.

The next genuine attack is on the negative-edge operator in(SR12), not another bare diagonal, independent-center or scalar-margin shortcut. No source is edited, and no related review transfers adoption. Theorems here require a complete joint-source written reconstruction and parent disposition before promotion. No formal/kernel/human/configured-family/executable/triple-witness/novelty acceptance, scientific GO or park follows. Continue the same all-spectrum target under science cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38-07:00.
