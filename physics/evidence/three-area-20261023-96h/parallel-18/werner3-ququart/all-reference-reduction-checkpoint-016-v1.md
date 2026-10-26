# All-reference working checkpoint 016: the reference-corrected lower Q/R/T block also closes

Before-writing clock observed: `2026-10-23T18:55:02-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written proof** within the same unfinished universal-reference W4 route. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used.

**Delta:** the actual lower reference Schur subtraction, followed by its Q-complement pivot, has a positive four-dimensional R/T Schur form. Its proof is an exact upper/lower Schur identity plus a four-column scalar likelihood-ratio estimate. The lower nonzero-charge twelve-block therefore reduces to **P4**, matching the upper four-dimensional residual. Neither resulting P4 sign is proved here.

## 1. Input and physical notation

Use the same physical table and coordinates as checkpoint 015 (SHA256 `c3f90d9adb871bfdf866f68764412e99b04a6c7e9b3a11c182053a44711e8ba5`). Put

```
D=C-S, L=3C+S=4C-D,
Tau=diag(tau_i), tau_a=tau_b=1/2, tau_j=tau_k=1,
f=Tau c, d=c^T Tau c=d_ab,
Q0=Tau-f f^T/d.
```

The Q-reference vector is `K=sum_i c_i Q_i`. D annihilates K and all its cross terms. The physical Q-complement has `Q0>=I/2` on `c^perp`. Write G for the four Q-complement-to-R/T cross columns of the upper form D. Their R columns are

```
G_Rl=-e_l/2+c_l Tau^(lb)c/(2d_lb),
```

with the T analogue using `Tau^(al),d_al`. Every column is orthogonal to c. All inverse pairings below use the exact inverse of Q0 on that complement, not an unconstrained inverse on its reference kernel.

Let R be the upper R/T Schur matrix from checkpoint 015. Its proved working bounds include

```
R>=I/18, max_r R_rr<=1,
max_r sum_(s!=r)|R_rs|<=11/18,
R<= (29/18)I.                               (16.1)
```

The additional diagonal upper bound follows directly from its formula: `R_Rl,Rl<=3/4+x_l^2/(16d_lb^2)<=1`, since `2d_lb=1+x_a+x_(other spectator)>=x_l`. The last bound in (16.1) is the Hermitian row-sum estimate, not a numerical eigenvalue computation.

## 2. Keep the actual reference correction

First take the Schur complement of C on its positive K block d, denoting the resulting form by `C_short`. Its Q-complement block is Q0. Its Q-to-R/T columns, denoted gC, are

```
(gC)_Rl=-e_l/2+c_l f/(2d),
(gC)_Tl=-e_l/2+c_l f/(2d).                   (16.2)
```

These columns also annihilate the c pairing. Because the lower K block is **4d**, and D has zero K row and column, the actual lower form after eliminating K is exactly

```
L_after_K=4 C_short-D.
```

In particular its Q-complement block is `3Q0` and its Q-to-R/T columns are `4gC-G`. None of the reference cross terms with other directions is silently discarded.

Eliminating **all four Q directions in C** is independent of eta and yields on R/T the fixed matrix

```
C_after_all_Q=(3/4)I_4.                     (16.3)
```

Indeed the raw C_QQ is Tau, and the Q-to-R_l and Q-to-T_l columns are both `-e_l/2`. Since `tau_l=1` for spectators, the correction is `1/4` on the corresponding R/T diagonal and same-spectator cross entry, giving diagonals `3/4` and zero off-diagonals.

Consequently, on the Q complement,

```
(C_short)_RT=(3/4)I+gC^* Q0^(-1)gC,
D_RT=R+G^*Q0^(-1)G.
```

Performing the **lower** Q-complement Schur operation gives the exact identity

```
L_RT_after_K,Q
=3I-R-(4/3)H^*Q0^(-1)H,
H=G-gC.                                    (16.4)
```

For clarity, the expansion uses the lower cross `4gC-G` and lower pivot `3Q0`:

```
4gC^*Q0^(-1)gC-G^*Q0^(-1)G
 -(1/3)(4gC-G)^*Q0^(-1)(4gC-G)
=-(4/3)(G-gC)^*Q0^(-1)(G-gC).
```

Thus (16.4) is not a claim that upper and lower share the same Schur matrix.

## 3. Bound the exact correction by a scalar variance inequality

The R_l column of H is

```
H_Rl=(c_l/2)[Tau^(lb)c/d_lb-Tau c/d],        (16.5)
```

and its T_l column replaces `(lb)` by `(al)`. The `-e_l/2` terms cancel. This cancellation is exact and does not depend on equal Schmidt coefficients.

Introduce the probability distribution and likelihood ratio

```
pi_i=tau_i x_i/d,
ell_i=tau_i^(lb)/tau_i,
mu=sum_i pi_i ell_i=d_lb/d.
```

Every likelihood ratio lies in `[1/2,2]`; the two thinning patterns differ only in which labels receive the factor one-half. The exact covariance inverse pairing from checkpoint 013 gives

```
H_Rl^*Q0^(-1)H_Rl
=[x_l/(4d)] Var_pi(ell)/mu^2.                (16.6)
```

To verify the normalization, its direct expanded expression is

```
(x_l/4)sum_i [x_i/tau_i]
 [tau_i^(lb)/d_lb-tau_i/d]^2.
```

Inserting `pi_i=tau_i x_i/d` reduces this precisely to (16.6), including the factor d. The T column has the same bound.

For any scalar random variable `ell in[m,M]` with positive mean mu,

```
E ell^2 <=(M+m)mu-Mm,
E ell^2/mu^2 <=(M+m)^2/(4Mm).
```

The first follows from `(ell-m)(M-ell)>=0`; the second follows by completing the square

```
[(M+m)^2/(4Mm)]mu^2-(M+m)mu+Mm
=[(M+m)mu-2Mm]^2/(4Mm)>=0.
```

At `m=1/2,M=2`, this gives `Var(ell)/mu^2<=9/16`. Therefore each R_l or T_l diagonal of the positive Gram matrix in (16.4) is at most `9x_l/(64d)`. Summing its four diagonals,

```
Tr[H^*Q0^(-1)H]
<=9(x_j+x_k)/(32d)
<=9/32,                                     (16.7)
```

because `d=(1+V)/2` and `V/d=2V/(1+V)<=1`. As that Gram matrix is positive, its operator norm is at most its trace; hence

```
0<=H^*Q0^(-1)H<=(9/32)I.                   (16.8)
```

The probability proof permits zero pi weights. The original physical columns and Q-complement inverse are continuous and uniformly bounded, so the bound includes zero or repeated Schmidt amplitudes; no zero-amplitude congruence inverse is evaluated there.

## 4. Positive lower Schur pivot and the P4 residual

Combining (16.1), (16.4), and (16.8) yields

```
L_RT_after_K,Q
>= [3-29/18-(4/3)(9/32)]I
=(73/72)I>0.                                (16.9)
```

Thus the correct order is:

1. eliminate the genuine positive lower K block `4d`;
2. eliminate its three-dimensional Q-complement block `3Q0`;
3. eliminate the resulting strictly positive four-dimensional R/T Schur block (16.9).

The actual remainder is **four-dimensional P4**, with every P cross term carried through all three operations. Full lower positivity is equivalent to that P4 Schur sign. No P variable was set to zero in obtaining this equivalence.

The bound `73/72` is for the R/T Schur form after the preceding two operations, not an asserted lower eigenvalue bound on the entire seven-dimensional joint pivot before those cross terms are eliminated.

## 5. Literal frontier and evidence boundary

The same all-reference target now has only these still-unproved forms in the working reduction packet:

1. **upper nonzero-charge P4** after checkpoint 015's positive joint Q/R/T pivot;
2. **lower nonzero-charge P4** after the actual reference correction and positive pivots proved here;
3. **both zero-charge nine-dimensional** residuals from checkpoint 010, with checkpoint 013's rational chart.

The upper and lower P4 matrices are different exact Schur complements and are not being identified. All reference spectra remain quantified. The full four-dimensional phase blocks have their earlier hand closure, but the complete universal-reference route and unrestricted W4 remain unproved.

No scientific execution or result from either polynomial request was used. Both requests remain author-requested HOLD pending any separate parent decision; no rerun, extra control, proof promotion, novelty certification, independent acceptance, or formal/kernel verification is inferred.
