# All-reference working checkpoint 018: the lower zero-sector p pivot is strictly positive

Before-writing clock observed: `2026-10-23T19:19:33-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written proof**. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. This remains one component of the same unfinished universal-reference W4 route.

**Delta:** after its **actual positive reference-block Schur subtraction**, the entire twelve-dimensional lower p principal block is strictly positive for every reference, including sparse spectra. A trace bound for a compressed CP Choi projection and an explicit weighted diagonal-dominance estimate are enough. The lower zero block can therefore use a p-first pivot and reduce to **q-plus6**, matching the upper six-dimensional residual. The two q-plus6 Schur matrices are different and neither sign is proved here.

## 1. Actual restricted map and notation

Use checkpoint 017 (SHA256 `9bac932c40c58aced18ea14c54fd84334f889d9e21b1c102c18d7824b8b8a4a0`) only for its Section 1-2 interface:

```
Bdiag(X)=Tr(X)I-diag(X)+X/4,
P=cc^T, Q=I-P, x_i=c_i^2, sum x_i=1,
X0=diag(x_i),
A0=I-X0+P/4>=I/4.
```

The real normalized c is the Schmidt coefficient vector, and all sector test vectors may be complex. The ordinary Choi matrix of Bdiag is a rank-thirteen orthoprojection Pi. The CP peeling map Mdiag has an ordinary Choi matrix `J_M` which is an orthoprojection of rank four. Its input-c compression is A0. Set

```
C=Jhat(Bdiag), S=Jhat(Mdiag), D=C-S,
L=3C+S=4C-D.
```

D has zero rows and columns on the reference subspace `P_input tensor C^4_output`. This follows from the actual peeling identity and reality of c, not an assumed matrix sign.

This proof does **not** require checkpoint 017's PPT conclusion or its inverse/Hodge estimate. The shared projection interface is not independent verification; this is a second author argument for a different sign.

## 2. A compressed-CP trace bound for S

Let `Qref=Q_input tensor I_output` and

```
J_Q=Qref J_M Qref>=0.
```

As `J_M` is a rank-four orthoprojection,

```
Tr J_Q=4-Tr A0=4-13/4=3/4.                  (18.1)
```

Since Q is real, its input partial transpose is unchanged and

```
J_Q^Gamma=Qref S Qref=:S_Q.
```

For any positive operator Y on a bipartite space,

```
Y^Gamma>=-(Tr Y/2)I.                        (18.2)
```

To see this, write a positive sum of unnormalized pure projectors. A pure projector's partial transpose has possible negative eigenvalues `-s_i s_j`, where s_i are its Schmidt coefficients; `s_i s_j<=(s_i^2+s_j^2)/2<=||v||^2/2`. Sum the resulting operator inequalities. No finite point evaluation or numerical spectrum is involved.

Equations (18.1)-(18.2) give the universal bound

```
S_Q>=-(3/8)I_Qref.                          (18.3)
```

This is only the reference-perpendicular compression, not a global bound on S.

## 3. Keep the C reference correction explicit

Relative to the reference subspace and its orthogonal complement, write

```
C=[[A0,V],[V^dagger,C_Q]],
T=V^dagger A0^(-1)V,
C_short=C_Q-T.
```

The physical p C table consists of scalar `1/4` on `|ii>` and reverse-pair blocks `[[1,1/4],[1/4,1]]` off the diagonal. Hence

```
C>=I/4,
C_short>=I_Qref/4,                          (18.4)
```

the second by minimizing the C quadratic form over reference vectors. The reference and complement are orthogonal, so their combined norm is at least the norm of the fixed complement vector.

Because D has zero reference row/column, the lower reference block is exactly **4A0**, and its true Schur form on the complement is

```
L_after_reference
=3C_Q+S_Q-4T
=3C_short+S_Q-T.                            (18.5)
```

The correction T is not deleted. The next section proves `T<(3/8)I`, precisely enough for (18.3)-(18.5).

## 4. Exact variance matrix for the C reference coupling

Squaring the physical p C table and compressing its input on c gives

```
C2_ref=(17/16)I-(3/2)X0+P/2.
```

For a direct entry check: its diagonal output entry i is `17/16-x_i`; its off-diagonal entry i,j is `c_i c_j/2`. These follow from the off-pair squared block `[[17/16,1/2],[1/2,17/16]]` and diagonal scalar `1/16`.

Thus the exact coupling variance is

```
VV^dagger=C2_ref-A0^2
=I/16+X0/2-X0^2-P/16+(X0 P+P X0)/4.        (18.6)
```

Put `theta=3/8` and

```
M=theta A0-VV^dagger.
```

The entries obtained by expanding (18.6) are

```
M_ii=(16x_i^2-23x_i+10)/32,
M_ij=c_i c_j[5/32-(x_i+x_j)/4], i!=j.       (18.7)
```

We will prove M strictly positive without discarding its rank-one cross terms.

## 5. Weighted strict diagonal dominance of M

For an active index `c_i>0`, use the positive row weight c_i. The relevant row margin is

```
M_ii-sum_(j!=i)(c_j/c_i)|M_ij|
=M_ii-sum_(j!=i)x_j|5/32-(x_i+x_j)/4|.      (18.8)
```

If `x_i<1/2`, the absolute coefficient is at most `5/32`, since `0<=x_i+x_j<=1`. Therefore the margin is at least

```
[16x_i^2-18x_i+5]/32
=[(2x_i-1)(8x_i-5)]/32>0.                   (18.9)
```

Both factors are negative on this interval.

If `x_i>=1/2`, then `1/2<=x_i+x_j<=1`, so the absolute coefficient is at most `3/32`. The margin is now at least

```
[16x_i^2-20x_i+7]/32
=[16(x_i-5/8)^2+3/4]/32>0.                  (18.10)
```

This covers `x_i=1/2` without an equality gap. Congruence by the diagonal of the positive active c_i therefore makes the active block strictly diagonally dominant with positive diagonal. For inactive `c_i=0`, all its off-diagonal M entries vanish and `M_ii=5/16>0`. Hence

```
M>0 for EVERY normalized nonnegative c.     (18.11)
```

This is an operator sign statement, not a numerical eigenvalue bound copied from a nonorthonormal coordinate matrix.

## 6. Strict bound on the reference correction

Equation (18.11) says

```
VV^dagger < (3/8) A0.
```

After the positive A0 congruence, the nonzero eigenvalues of `A0^(-1/2)VV^dagger A0^(-1/2)` are those of `T=V^dagger A0^(-1)V`. Thus

```
T < (3/8) I_Qref.                          (18.12)
```

Equivalently its operator norm is strictly below `3/8` at every fixed reference. No numerical uniform gap over the reference simplex is asserted or needed.

Combining (18.3), (18.4), (18.5), and (18.12) gives

```
L_after_reference
>= (3/4)I-(3/8)I-T
=(3/8)I-T>0.                               (18.13)
```

This proves strict positivity of the actual twelve-dimensional lower p principal block **after** the reference correction, for all reference spectra. The full p-only lower block is also positive because its reference block `4A0` is positive. No q coupling has been ignored in the eventual full-block equivalence below.

## 7. The exact new lower zero-sector residual

In the full zero-charge lower matrix:

1. eliminate the true four-dimensional reference block;
2. remove the reducing positive q-minus6 block;
3. eliminate the actual p12 principal block (18.13), carrying all p/q-plus cross terms.

The remaining exact Schur matrix is lower q-plus6. Unlike the upper p pivot, this lower p pivot is strictly positive even at sparse references, so no boundary inverse is being silently substituted.

The lower q-plus6 sign is **unproved**. The upper q-plus6 from checkpoint 017 is a different Schur form, and its sparse-boundary interpretation still requires full physical continuity if a proof is supplied on the interior.

## 8. Literal remaining all-reference frontier

The working reduction packet now has exactly these still-unproved forms:

1. upper nonzero-charge P4;
2. lower nonzero-charge P4;
3. upper zero-charge q-plus6;
4. lower zero-charge q-plus6.

The claimed scalar/two-dimensional/four-dimensional phase closures and these principal-pivot reductions remain written candidates pending actual independent reconstruction. No full universal-reference theorem, unrestricted W4 theorem, exact route failure, rank-two Werner witness, novelty certification, independent acceptance, or formal/kernel verification is claimed. No output from either held polynomial proposal or the finite-reference assay is an input to this proof.
