# All-reference working checkpoint 019: exact boundary kernels and the upper zero Schur range condition

Before-writing clock observed: `2026-10-23T19:35:06-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written boundary analysis**. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. This does not prove the remaining zero-six sign.

**Delta:** the extra kernel of the upper p-only block at sparse references is identified, and the actual q-plus coupling is proved orthogonal to it. Hence the upper zero-six residual can be defined by a mathematical Moore-Penrose inverse on the **entire closed reference simplex**, with the exact generalized-Schur range condition already supplied. No floating-point pseudoinverse or deletion of an unsupported zero pivot is permitted.

## 1. Fixed interface

Use the explicit p operators and q-plus columns in `all-reference-four-residuals-v1.md` (SHA256 `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`). In particular

```
c_i>=0, c^T c=1, P=cc^T, Q=I-P,
rho=Jhat(Bdiag-Mdiag)>=0,
Pref=P_input tensor I_output,
H_ab=|[v_ab f_ab^T/d_ab-F_ab]/sqrt(2)>>,
F_ab=|a><b|+|b><a|,
v_ab=F_ab c, f_ab=Tau^(ab)c.
```

Column vectorization uses output rows and input columns. Every H_ab annihilates c as a matrix, so it is orthogonal to the four reference-kernel directions. All vectors and the operator rho remain complex-linear; the Schmidt coordinate c is real.

Checkpoint 017 (SHA256 `9bac932c40c58aced18ea14c54fd84334f889d9e21b1c102c18d7824b8b8a4a0`) proved the whole p-only upper block positive. This leaf supplies its exact kernel and the additional coupling conditions, rather than assuming strictness at rank-two boundary references.

## 2. Kernel for nonproduct references

Suppose at least two c_i are nonzero, so every `d_i=1-c_i^2` is positive. Apply checkpoint 017's real invertible output filter `D0=diag(d_i)`. Its proof gave

```
rho'=B0'+r(P_s-P_a)
     =[B0'-2rP_a]+r(Q tensor Q)>=0,
B0'>=2rP_a,
```

where B0' is block diagonal by output row i, with block

```
d_i^2[Q-|q_i><q_i|/d_i], q_i=Qe_i.
```

Inside `Q_input tensor C4_output`, any zero vector of rho' must therefore have the form `v_input tensor c_output`, with `v orthogonal c`. It lies in the kernel precisely when B0' kills it, namely

```
c_i v is proportional to q_i for every active c_i. (19.1)
```

The converse is also exact: such a vector is killed by B0' and by both P_s,P_a because its output is c, so rho' kills it.

If at least three c_i are nonzero, choose two active i,j with another active label remaining. Then

```
||q_i||^2||q_j||^2-|<q_i,q_j>|^2
=1-x_i-x_j>0.
```

Condition (19.1) forces v=0. Thus for Schmidt rank three or four the kernel of rho is **exactly** the four reference directions, and its p12 quotient is strictly positive.

If the support is exactly `{a,b}`, put

```
v=c_b e_a-c_a e_b,
u=D0 c=x_b c_a e_a+x_a c_b e_b.
```

The common line of q_a,q_b is `span{v}`. Undoing the output filter shows that the single extra p-quotient kernel direction is

```
k_ab=|v>_input tensor |u>_output,
```

or the matrix `u v^T`. It is nonzero because both active coefficients are positive. Together with the four reference directions this is the full rho kernel. No normalization of u is silently assumed.

## 3. The q-plus coupling is orthogonal to the rank-two extra kernel

For the active pair a,b, `d_ab=1/2` and `f_ab=c/2`, so the matrix of H_ab is

```
[v_ab c^T-F_ab]/sqrt(2)
=[(c_a e_a-c_b e_b)v^T]/sqrt(2).
```

Its output factor is orthogonal to u:

```
<u,c_a e_a-c_b e_b>
=x_b x_a-x_a x_b=0.
```

Hence `<k_ab,H_ab>=0`.

For a pair containing exactly one active label and one inactive label t, the matrix H applied to v has output only in the inactive direction `e_t`. It is therefore orthogonal to u, whose support is active. This follows directly because `F_pair v` is inactive and `v_pair=F_pair c` is inactive. For a pair containing no active label, `F_pair v=0` and `f_pair^T v=c^T v=0`, so the output vanishes altogether.

These three cases cover all six q-plus columns. Thus each is orthogonal to the extra rank-two p kernel, not just to Pref.

## 4. Product reference: exact p block and range

Let `c=e_a`. The restricted peeling map on input `e_a^perp` is explicitly

```
Phi(X)=Tr(X)I-diag(X).
```

The ordinary and reversed-input Choi matrices are then the same classical projector

```
rho=sum_(i!=a, j!=i)|i,j><i,j|.
```

It has rank nine. Besides Pref, its p-quotient kernel consists exactly of `|i,i>`, `i!=a` (three dimensions).

If a q-plus pair contains the active label a and another label b, its H matrix is `-|a><b|/sqrt(2)`. If it contains no active label it is `-F_pair/sqrt(2)`. All are off-diagonal matrices, so they are orthogonal to every additional `|i,i>` kernel vector. This is an exact range check, not a numerical near-zero threshold.

## 5. Closed-simplex generalized Schur form

For Schmidt rank at least three, the range condition is automatic from strict positivity on the p quotient and `Pref Hq=0`. Sections 3-4 prove the missing conditions at ranks two and one. Hence on **every** normalized nonnegative spectrum,

```
ran(Hq) subset ran(rho).                    (19.2)
```

It is therefore legitimate to define the exact upper residual everywhere by

```
Z_up_closed=(5/4)I6-Tq-Hq^*rho^+Hq,          (19.3)
```

where `rho^+` is the mathematical Moore-Penrose inverse of the explicitly given finite matrix. The standard generalized Schur criterion says that the full p/q-plus upper block is positive if and only if (19.3) is positive, because rho is positive and (19.2) is already established. The reducing q-minus block retains its previous positive bound.

On the positive interior, (19.3) agrees exactly with the earlier `rho+Pref` inverse formula. At sparse spectra this formulation uses the proved range condition and all additional kernel directions; it does not invert a zero pivot or replace a small coefficient by a tolerance.

No continuity of the pseudoinverse expression itself across a rank drop is asserted. Independently, positivity of the full physical block would still extend by ordinary physical continuity if proved on the whole interior. These are two distinct valid formulations, not an interchange of a limit with a singular inverse.

## 6. Remaining scope

The still-unproved signs remain both charge-P4 forms and both zero-q-plus6 forms. This leaf only completes the upper boundary-kernel/range interface. No positivity proof of Z_up_closed, negative asymmetric route direction, rank-two Werner witness, full all-reference theorem, unrestricted W4 theorem, novelty verdict, independent acceptance, or formal/kernel verification is claimed.
