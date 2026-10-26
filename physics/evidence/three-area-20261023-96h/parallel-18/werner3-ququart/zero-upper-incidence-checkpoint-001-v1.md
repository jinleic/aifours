# Single active residual: upper zero-six via weighted edge incidence

Actual clock observed before writing: **2026-10-24T03:43:46-07:00**, `/bin/date -Iseconds`. Author: PhysicsResearch96h.

Status: **NEW CANDIDATE written identities and reduction**, not a proof of the final residual sign. No scientific execution, arithmetic interpreter, import, compile/syntax check, test, enumeration, solver, native launch, model CLI or nested agent was used.

## 1. Freeze the one target and its first new logical input

The next same-primary obligation was ACKed to Main **before this attack**: pursue only

```
Z_up(c) >= 0 for every normalized nonnegative Schmidt spectrum
and every complex six-dimensional q-plus test vector.
```

The other three final signs are not being attacked or supplied here. A negative value would refute this sufficient co-Choi route, not automatically refute W4.

The first new logical input is the invertible edge rescaling

```
U_ab=q_ab/d_ab, U_aa=0, U^T=U,
b=Uc,
```

followed by an exact incidence-image/kernel decomposition. Because `d_ab>=1/2`, the rescaling itself loses no spectrum or complex test direction, even on a sparse face. The component inverses used later in this file are explicitly confined to the positive interior.

The actual parent disposition was fully read, including its untruncated defect-history clause:

`../../../../../institute/runs/three-area-2026-10-23-96h/werner-four-residuals-parent-v1.md`, observed SHA256 **`a8594c2bc9248212bdc942c22e9c56ed62afd0f4c2d1cf1b0a4b6b0ae58d80fb`**.

It supports component reductions only at the stated in-harness written level. Original015's MAJOR history and mandatory ADDENDUM1 remain operative. Neither a final sign, novelty, formal verification, nor a new execution permission follows. The zero branch used below is the actual017–019 branch, not the defective old charge formula.

The literal residual definitions are `all-reference-four-residuals-v1.md`, SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`, with the closed-simplex upper range interface in019, SHA256 `1dc5a4991660666e8aaf9381ff0d5ce3b85740b2863fa6dde0970156849ac130`.

## 2. Exact coupling normal form in the new edge variables

Use `c_i>=0`, `sum c_i^2=1`, `x_i=c_i^2`, `X=diag(x_i)`,

```
P=cc^T, Q=I-P,
D=I-X=diag(d_i), d_i=1-x_i,
E=I-X/2=(I+D)/2,
d_ab=1-(x_a+x_b)/2.
```

The normalized q-plus coefficient on edge a,b is q_ab, so `||q||^2=sum_(a<b)|q_ab|^2`. The matrix U above is complex symmetric, not necessarily Hermitian. No restriction to real test vectors is made.

For an edge put

```
F_ab=|a><b|+|b><a|,
v_ab=F_ab c,
f_ab=c-(c_a e_a+c_b e_b)/2.
```

The actual upper p/q-plus column is

```
H_ab=vec[(v_ab f_ab^T/d_ab-F_ab)/sqrt(2)].
```

Let H(q) be the 4-by-4 matrix whose column vectorization is `Hq q`. Then summing these six columns gives the exact new identity

```
H(q)=[b c^T-(1/2)diag(c_i b_i)-E U]/sqrt(2)
    =-[E U+(1/2)diag(c_i b_i)]Q/sqrt(2).       (I1)
```

Here `diag(c_i b_i)` is linear in the possibly complex b, not an absolute-square diagonal.

For a direct derivation, define the weighted edge matrix U, and note

```
sum_(a<b) q_ab v_ab/d_ab = Uc=b,
sum_(a<b) q_ab v_ab(c_a e_a+c_b e_b)^T/d_ab
 =diag(c_i b_i)+U X,
sum_(a<b)q_ab F_ab = U-(XU+UX)/2.
```

Insert `f_ab=c-(c_a e_a+c_b e_b)/2`; the UX terms cancel, leaving (I1). Multiplication by c verifies `H(q)c=0` exactly. This retains all six edges and all their cross terms; it is not a diagonal/principal compression.

## 3. An explicit four-plus-two incidence chart

On the positive c interior set

```
W=diag(c) U diag(c), r_i=c_i b_i, Rsum=sum_i r_i.
```

Then W is symmetric with zero diagonal and its row sums are r_i. An explicit right inverse of those four row-sum constraints is

```
W_b,ij=(r_i+r_j)/2-Rsum/6, i!=j,
W_b,ii=0.                                    (I2)
```

Indeed its row sum is `r_i+Rsum/2-Rsum/2=r_i`. Thus `W_C=W-W_b` has zero row sums. Every such symmetric zero-diagonal four-matrix has exactly the two-parameter form

```
W_C,12=alpha, W_C,13=beta, W_C,14=-alpha-beta,
W_C,23=-alpha-beta, W_C,24=beta, W_C,34=alpha.   (I3)
```

Conversely (I3) has all row sums zero. The image part and this kernel are orthogonal in the ordinary unweighted edge inner product of W; that does **not** make them orthogonal in the original q energy, whose weights include `d_ij^2/(x_i x_j)`. The corresponding U parts divide the off-diagonal entries by `c_i c_j`, only on this declared positive-interior chart.

Therefore the six-dimensional test family splits as four incidence coordinates b plus two cycle coordinates alpha,beta. The **mixed incidence/cycle terms are not zeroed**. Proving only the cycle restriction would not prove the target sign.

## 4. The filtered p operator and its exact kernel frame

Use the supported p principal component, with standard column vectorization (output rows/input columns):

```
rho=Jhat(Bdiag-Mdiag),
Bdiag(Y)=Tr(Y)I-diag(Y)+Y/4.
```

On the positive interior, rho is positive and strictly positive on `Q_input tensor C4_output`. Its kernel is the four-dimensional reference input P. The real output filter gives

```
rho'=(I tensor D)rho(I tensor D)
     =B'+r(P_s-P_a),
r=1/Y, Y=sum_i 1/d_i,
B'=sum_i d_i^2[Q-q_i q_i^T/d_i]_input tensor |i><i|_output,
q_i=Qe_i,
```

where P_s,P_a are the symmetric/antisymmetric projectors on `Q tensor Q`. The established whole-operator bound is `B'>=2r P_a`, not an assertion inferred from one restricted quadratic form.

Work on the twelve-dimensional space `H=Q_input tensor C4_output`. The four vectors

```
t_i=|q_i>_input tensor |i>_output/sqrt(d_i)
```

are orthonormal, span the kernel T of B' inside H, and form an isometry matrix Tmat with four columns. Let `P_B=I_H-Tmat Tmat^dagger`; its range B has dimension eight. B' is strictly positive on B, with its actual row-block metric retained.

The antisymmetric projector annihilates every t_i, since projection to `Q tensor Q` makes t_i proportional to `q_i tensor q_i`. Thus `P_a Tmat=0`.

## 5. A new explicit Gram matrix and its determinant

The positive kernel-frame Gram of the symmetric projector is

```
N=Tmat^dagger P_s Tmat,
N_ij=Q_ij^2/sqrt(d_i d_j).
```

Let

```
M=Q circ Q=diag(1-2x_i)+x x^T.
```

The circle denotes entrywise product of the real Q, not an operator square. Its diagonal is d_i^2 and its off-diagonal entries are x_i x_j. Then

```
N=diag(d_i^(-1/2)) M diag(d_i^(-1/2)),
det M=2[e3(x)-4e4(x)].                       (I4)
```

Here is a full symbolic determinant expansion. Multilinearity with the rank-one x x^T term gives

```
det M=product_i(1-2x_i)
      +sum_i x_i^2 product_(j!=i)(1-2x_j).
```

The first term is `-1+4e2-8e3+16e4`. In the second,

```
sum_i x_i^2 e2(x excluding i)=e3-4e4,
sum_i x_i^2 e3(x excluding i)=e4,
p2=1-2e2, p3=1-3e2+3e3.
```

It therefore equals `-p2+2p3+4e3-24e4=1-4e2+10e3-24e4`. Adding proves (I4) for the entire normalized domain. No division by `1-2x_i`, finite-value interpolation, or arithmetic program is used.

For positive x, `e3=e4 sum_i1/x_i>=16e4`, so `det M>=24e4>0`; M is positive as the Schur product of a positive Q with itself. Thus N is strictly positive and

```
det N=2(e3-4e4)/product_i d_i.                (I5)
```

At rank three the same determinant is positive by e4=0,e3>0. At ranks two/one the determinant is zero, consistent with the separately supported sparse-kernel analysis. No N inverse is asserted at those rank drops.

## 6. Short the symmetric projector: the cycle space appears exactly

The operator `P_s Tmat N^(-1) Tmat^dagger P_s` is an orthoprojection inside the six-dimensional range of P_s: it is the Gram projector of `P_s Tmat`, whose column Gram is N. Therefore

```
P_C=P_s-P_s Tmat N^(-1) Tmat^dagger P_s        (I6)
```

is the orthoprojection onto

```
C={vec(U): U^T=U, Uc=0, diag(U)=0}.
```

The reason for the last constraint is exact: for a symmetric matrix on `Q tensor Q`, pairing with t_i is its ith diagonal entry divided by sqrt(d_i). This is precisely the two-dimensional incidence kernel in (I3), in physical matrix coordinates. Its dimension is `6-4=2`. This is not a claim that the weighted q quadratic form is block diagonal in that splitting.

The T4 block of rho' is rN. Its exact Schur complement on B is consequently

```
A8=B'|B+r P_C-r P_a.                         (I7)
```

Only P_s couples to T; B' and P_a do not. The positive symmetric-projector Schur term in (I7) is the actual shorted orthoprojection (I6), not a guessed projector. Moreover

```
A8 >=(1/2)B'|B+r P_C>0,
```

since `B'>=2rP_a`. Thus the new operator is a well-defined positive inverse object on B throughout the positive interior.

## 7. Exact inverse energy: incidence controls the first term only

Put `h=vec(D H(q))`, the actual filtered coupling. Its T coordinates are

```
eta=Tmat^dagger h,
eta_i=sqrt(d_i)c_i b_i/(2sqrt(2)).             (I8)
```

Indeed H(q)c=0 and its diagonal entry from (I1) is `c_i b_i/(2sqrt(2))`; the output filter multiplies it by d_i. Thus eta depends **only** on the four incidence coordinates b.

Let

```
h_B=P_B h,
zeta=h_B-P_B P_s Tmat N^(-1)eta.
```

The exact block inverse/Schur identity for rho' in `T direct-sum B` gives

```
h^dagger(rho'|H)^(-1)h
=(1/r) eta^dagger N^(-1)eta
 +zeta^dagger A8^(-1)zeta.                   (I9)
```

All normalization factors, including the q-plus sqrt(2), are included in eta and h. No extra factor is silently absorbed into A8.

The local filter preserves the inverse energy, so the left side is exactly the original `q^dagger Hq^dagger(rho+Pref)^(-1)Hq q` on the positive interior. For an incidence-kernel test b=0, eta vanishes and only the second term remains. For a general test, zeta and the raw q energy both contain the cycle/image coupling. Dropping those cross terms is not justified.

## 8. The one full residual obligation after this checkpoint

Define the raw q energy from the literal six-by-six matrix Tq in the canonical specification:

```
Qraw(U)=q^dagger[(5/4)I6-Tq]q,
q_ab=d_ab U_ab.
```

The SAME full upper-zero target is now the exact coupled inequality

```
Qraw(U)
 -(1/r) eta(U)^dagger N^(-1)eta(U)
 -zeta(U)^dagger A8^(-1)zeta(U) >=0           (I10)
```

for every complex symmetric zero-diagonal U and every positive-interior c. Its closed-simplex version is the original mathematical Moore-Penrose residual with the established range condition; proving the whole interior physical block would also extend positivity by ordinary physical continuity.

**I10 is still UNPROVED.** Neither positivity of N/A8, the two-dimensional cycle projector, nor the fact that the first cost depends only on b proves it. This checkpoint supplies a nontrivial exact coupling normal form, a determinant, and a structured inverse-energy split; it does not replace the full sign by a cycle-only or diagonal-only problem. The three other final residual signs are not analyzed here. No negative route direction, W4 witness, full all-reference theorem, novelty certification, independent review or formal verification of these new identities is claimed.

All existing execution HOLDs remain in force. The two complete but unused polynomial proposals are not imported, run, repurposed or treated as permission for any calculation.
