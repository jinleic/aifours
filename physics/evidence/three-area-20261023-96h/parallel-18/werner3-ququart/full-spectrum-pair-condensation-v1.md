# Full-spectrum upper-zero sign: exact edge-pair / four-row condensation

Observed clock before this packet: **Sun Oct 25 04:10:12 PDT 2026**, from `/bin/date`. Owner: PhysicsResearch96h, slot physics-1. Same primary problem and unchanged round deadline.

**Verdict: NOT_PROVED at the requested uniform-sign scope.** This packet gives a new **WRITTEN** arbitrary-spectrum identity: the actual full-Qraw p12 elimination reduces to six elementary positive two-by-two edge pivots and two positive four-dimensional row metrics. The final coupled six-dimensional sign remains unproved. This is not another selected-spectrum theorem or a replacement of Qraw by R0.

The parent withdrew the resumption context's automatic eval-arithmetic exception during this work. The mandatory `resumption-arithmetic-authority-addendum-v1.json` records every earlier scientific eval activity and the correction. None of those unadmitted finite observations is used as a premise below or claimed as accepted verification. No further scientific computation was performed after that correction. The derivation below is written algebra at named imports, not formal/kernel proof, independent reconstruction, cross-vendor review, or novelty clearance.

## 1. Named imports and exact scope

All paths in this section except RUN are relative to this owned root. RUN is `institute/runs/three-area-2026-10-23-96h/`.

- `generic-upper-zero-operator-checkpoint-001-v1.md`, SHA256 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`: G1-G12, including the exact filtered p operator, six-edge forcing and compatible-square identity. Its separate G13 is FALSE and is not imported.
- `generic-upper-zero-operator-checkpoint-001-ADDENDUM-1.md`, SHA256 `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`: preserves the G13 obstruction and distinguishes it from the actual target. No false sufficient estimate is reused here.
- `generic-upper-zero-operator-checkpoint-001-ADDENDUM-2.md`, SHA256 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`: F1-F5, with the ENTIRE commutator Gram S_c and the positive resolvent correction, not just its diagonal.
- `all-reference-four-residuals-v1.md`, SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`: the literal full q-plus raw matrix and physical p/q cross columns, especially its equations R5-R7. Its other three final signs are not premises.
- `all-reference-reduction-checkpoint-017-v1.md`, SHA256 `9bac932c40c58aced18ea14c54fd84334f889d9e21b1c102c18d7824b8b8a4a0`: the whole-operator Hodge bound B'>=2r P_a and strict positivity of the p12 quotient in the positive Schmidt interior. This is a p-principal result, not the full p/q sign.
- RUN/`wave-v24-werner-generic-parent-v1.md`, SHA256 `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`: written-supported operative identities and invalid-certificate scope only.
- RUN/`wave-v17-werner-parent-disposition-v1.md`, SHA256 `1b85107d54127373d0a05c0d73dff0e71a741ee83fd5151e52d1e291692c0184`: its generic incidence/raw identities and p-principal imports; its positive 1+3 comparison is not substituted for the present arbitrary-spectrum obligation.

The quantifiers throughout Sections 2-6 are ALL real c_i>0 with sum c_i^2=1 and ALL complex p/q test vectors. No symmetry of p, no reality of tests and no reference-family restriction is assumed. Real coefficient matrices below act by Hermitian forms over complex vectors.

## 2. A radical-free full joint matrix

Put

```
x_i=c_i^2, d_i=1-x_i, d_ij=(d_i+d_j)/2,
r=1/(sum_i 1/d_i), W=e3(d).
```

Index the p vector t by the TWELVE ordered pairs i!=j, and the q vector v by the SIX unordered pairs. Define the full matrix T by

```
T_ij=t_ij                    (i!=j),
T_ii=-(sum_(j!=i) x_j t_ij)/x_i,
Z_ij=c_i c_j T_ij.
```

Then Zc=0. Conversely every complex Zc=0 has exactly this chart on the positive interior. Thus t has all twelve p degrees of freedom. On the q side set

```
U_ij=sqrt(2)c_i c_j v_ij, U_ii=0, U^T=U.
```

This includes all six complex q directions. In particular the physical normalized q-plus coefficient is `q_ij=sqrt(2)c_i c_j d_ij v_ij`; no factor of two is absorbed into a redefined physical form.

Using the imported G9-G11 identities, the ENTIRE original joint form is

```
<Z,rho' Z>+2 Re<Z,h_c(U)>+Qraw(U)
 = t^dagger H t + 2 Re(t^dagger B v) + v^dagger A v.       (P1)
```

Here every entry of H, B, A is a rational function of x, with no square roots. Explicitly, if i,j,t are distinct,

```
H_(ij,ij)=d_i^2 x_i x_j+(r-d_i x_i)x_j^2,
H_(ij,it)=(r-d_i x_i)x_j x_t,
H_(ij,ji)=r x_i x_j,
```

and the other entries are zero apart from the symmetric counterparts. The entries of B are

```
B_(ij,{i,j})=-d_i x_i x_j(1+d_i-x_j)/2,
B_(ij,{i,t})= d_i x_i x_j x_t/2,
B_(ij,e)=0 if e is not incident to i.                       (P2)
```

For complementary pairs {i,j}, {k,l},

```
A_({i,j},{i,j})=x_i x_j d_ij^2(3-2d_ij d_kl/W),
A_({i,j},{i,t})=-x_i x_j x_t d_ij d_it/(2d_jt),
A_(e,f)=0 if e,f are disjoint.                              (P3)
```

Every shared-edge cross term is present in (P3).

For a direct derivation of H, the diagonal part of the swap form is `sum_i |sum_(j!=i)x_j t_ij|^2`, and its off-diagonal part is `sum_(i!=j)x_i x_j conj(t_ij)t_ji`. The row-variance form is

```
2 Gamma(T)
 =sum_i d_i x_i [d_i sum_(j!=i)x_j |t_ij|^2
                         -|sum_(j!=i)x_j t_ij|^2].
```

Adding r times the swap gives exactly H. Likewise G11 with the displayed sqrt(2) choice gives the cross terms

```
-2 Re Gamma(T,v)
-Re sum_(i<j) x_i x_j conj(d_i t_ij+d_j t_ji) v_ij,
```

which expand to (P2). Finally (P3) follows directly from the literal physical raw q matrix `(5/4)I-Tq`, whose diagonal is `3/2-d_ij d_kl/W` and whose shared-edge entry is `-c_j c_t/(4d_jt)`.

Thus A is the full raw block, not the stronger R0 block. In the earlier compatible-square coordinates it is exactly `M+C^dagger C+2S_c`. This equality retains the full S_c, including its commutator cross terms, rather than assuming that S_c is diagonal.

## 3. The actual full raw kernel is also Stieltjes

Let W_e be the positive diagonal edge matrix with entries `c_i c_j d_ij`. Then

```
A=W_e K_full W_e,
K_full=2[(5/4)I-Tq].                                       (P4)
```

Its diagonal is `3-2d_ij d_kl/W`, and its shared-edge entries are `-c_j c_t/(2d_jt)`. Hence it is a real symmetric matrix with nonpositive off-diagonal entries. The imported full remainder identity Qraw>=R0 gives

```
K_full>=K_c>=I.
```

Consequently K_full is positive Stieltjes, and K_full^(-1) is entrywise nonnegative. This is a written operator deduction from the actual raw kernel, not an entrywise-order claim about the RESOLVENT DIFFERENCE in F5. In particular neither `K_full^(-1)>=K_c^(-1)` entrywise nor any sign of their entrywise difference is asserted.

These facts alone do not prove the full p forcing comparison. In the present coordinates that comparison is exactly `H-B A^(-1)B^dagger>=0`, not positivity of A alone.

## 4. Six positive edge-pair pivots and a four-row update

For each unordered pair {i,j}, introduce the positive two-by-two metric on `(t_ij,t_ji)`

```
E_ij=x_i x_j [[d_i^2,r],[r,d_j^2]],
Delta_ij=d_i^2 d_j^2-r^2.
```

Let E_0 be their direct sum. These are genuinely positive pivots for EVERY positive spectrum: since

```
1/r>1/d_i+1/d_j,
r<d_i d_j/(d_i+d_j)<=d_i d_j,
```

where `d_i+d_j>=1`, we have Delta_ij>0. Their exact inverses are

```
E_ij^(-1)=[[d_j^2,-r],[-r,d_i^2]]/(x_i x_j Delta_ij).       (P5)
```

Define a twelve-by-four row-sum matrix V, a signed four-diagonal S_row, a four-by-six R and a positive four-diagonal K_row by

```
V_(ij,k)=delta_ik x_j,
S_row=diag(r-d_i x_i),
R_(i,{i,j})=x_j, with other entries zero,
K_row=diag(d_i x_i/2).
```

Define L_0, twelve-by-six, by the single nonzero entry in each ordered row

```
(L_0)_(ij,{i,j})=d_i x_i x_j(1+d_i)/2.
```

Then the full identities are

```
H=E_0+V S_row V^dagger,
B=-L_0+V K_row R.                                          (P6)
```

This follows entry by entry from (P2) and the displayed H. No sign is assigned to S_row; its negative diagonal entries must remain. In particular replacing this signed update by zero would not be a valid bound.

Set

```
G=V^dagger E_0^(-1)V.
```

V has rank four (its columns have disjoint nonempty ordered-row supports), so G is strictly positive. Its explicit entries are

```
G_ii=sum_(j!=i) x_j d_j^2/(x_i Delta_ij),
G_ij=-r/Delta_ij, i!=j.                                    (P7)
```

Thus G is another positive Stieltjes four-matrix, with entrywise nonnegative inverse. Define the row core

```
N_row=G^(-1)+S_row.                                        (P8)
```

N_row is strictly positive. Here is the exact reason, avoiding any false assertion that S_row>=0: for fixed `u=V^dagger t`, minimization of `t^dagger E_0 t` gives `u^dagger G^(-1)u`. Therefore

```
min_(V^dagger t=u) t^dagger H t =u^dagger N_row u.
```

The imported p-only Hodge result says H>0 on the full p12 interior chart. Since V^dagger is onto, every nonzero u has a nonzero constrained minimizer. Its H energy is strictly positive, proving N_row>0. This imports ONLY the established p principal sign, not the unproved joint p/q sign. No entrywise inverse sign is asserted for N_row.

## 5. Exact condensation of the original target to the four-row core

Define the following fixed-size rational matrices:

```
Y=V^dagger E_0^(-1)L_0,                 size4x6,
D_q=A-L_0^dagger E_0^(-1)L_0,          size6x6,
F=G^(-1)Y-K_row R,                     size4x6.
```

For fixed u=V^dagger t and v, completing the E_0 square in (P1) gives

```
min_(V^dagger t=u) Joint(t,v)
 =v^dagger D_q v
  +(u-Yv)^dagger G^(-1)(u-Yv)
  +u^dagger S_row u
  +2 Re(u^dagger K_row Rv).
```

To check the constrained square without an unstated inverse formula, its minimizer is

```
t=E_0^(-1)L_0 v
  +E_0^(-1)V G^(-1)(u-Yv).
```

It satisfies V^dagger t=u, and the residual is E_0-orthogonal to ker(V^dagger), so it is the unique constrained minimizer. Expanding the displayed energy, the u pivot is exactly N_row>0 and its forcing is Fv. Eliminating u therefore proves the FULL identity

```
Z_hat
 =D_q+Y^dagger G^(-1)Y-F^dagger N_row^(-1)F
 =A-B^dagger H^(-1)B.                                      (P9)
```

All inverses in the first expression are six elementary two-by-two edge inverses and the positive FOUR-dimensional matrices G and N_row. There is no eight- or twelve-dimensional inverse, no singular signed S_row inverse, and no discarded q direction or cross term.

Moreover, because H>0 and A>0, ordinary Schur equivalence gives

```
E_full,c(Z)>=0 for EVERY Zc=0
  iff H-B A^(-1)B^dagger>=0
  iff Z_hat>=0.                                            (P10)
```

At the original physical normalization,

```
Z_hat=2 W_e Z_up W_e.
```

Thus this condensation is exactly the original full-Qraw generic upper-zero problem. It is NOT G13, not the false bare dual lift, not a dropped-compatibility estimate, not the stronger R0 comparison, and not a selected-family substitute.

## 6. Exact remaining sign and scientific verdict

The first unproved input after the present written identities is

```
D_q+Y^dagger G^(-1)Y
 >=F^dagger [G^(-1)+diag(r-d_i x_i)]^(-1)F
for EVERY x_i>0, sum_i x_i=1.                              (P11)
```

All symbols in (P11) are explicitly defined in Sections 2-5. Positivity of E_0, G, N_row, A, and of the known resolvent correction does NOT by itself establish (P11). The left difference D_q is not labeled positive, and no inverse-order comparison is made across signed row updates. This is the precise remaining coupled matrix inequality, not a hidden scalar step.

Uniform sign verdicts:

- Full-spectrum E_full>=0 / generic Z_up: **NOT_PROVED; no exact falsifying spectrum delivered.**
- The other three final signs F_up, F_low, Z_low: **NOT_PROVED.** Their literal definitions remain the canonical four-residual source; finite in-kernel observations before the authority correction do not settle them and are not admitted as verification.
- Stronger arbitrary-spectrum R0 comparison: **NOT_PROVED**, not an imported premise.
- G13 and bare dual lift: **FALSE CERTIFICATES**, as already supported in v24. They were not reused to infer any actual target sign.
- Full asymmetric co-Choi route and unrestricted rank<=2 W4: **NOT_PROVED**. A negative route Schur form, if later supplied, would still not automatically be a rank-two Werner coefficient witness.

The coordinate charts divide by positive c_i or x_i. No sparse-boundary inverse, pseudoinverse-continuity claim or new endpoint theorem is asserted. Only a uniform interior proof of the full physical joint PSD would permit the existing physical-continuity/range interface to be used.

This is a parkable new representation at the same unrestricted obligation, not an exhausted-problem declaration or a 96-hour closeout. The next mathematical action is a written proof or exact separating test for (P11), with the complete A from (P3), followed by the other three canonical signs if the upper sign closes. No computation is authorized by that next-action description; the corrected HOLD requires a separate named GO for any new arithmetic execution.
