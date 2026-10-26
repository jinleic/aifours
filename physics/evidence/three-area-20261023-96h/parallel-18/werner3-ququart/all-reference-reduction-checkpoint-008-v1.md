# All-reference working checkpoint 008: a strict two-dimensional pivot inside the four-dimensional block

Clock observed immediately before writing: `2026-10-23T17:26:18-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written algebra**. No scientific execution, numerical evaluation, import, compilation, solver, or independent review was used for this checkpoint. This is a representation of the same universal reference obligation, not a smaller angular target or a claim of closing it. In particular, the remaining full four-dimensional determinant is still unproved.

## 1. Source boundary

This checkpoint uses the four-dimensional raw physical matrices in `all-reference-reduction-checkpoint-001-v1.md` (SHA256 `1e1e076bb8ec3b47853877c5cddd39dd37dc0915d8c9d87c4ef18596533a2326`), the bounds `1/12 <= E_ij <= 1/4` in checkpoint 006 (SHA256 `162c2094f006dc5c261678df6fa5fb6a21f9327bc3f83cbe5d3b794c82ff25aa`), and the strictly positive interior principal three-minors in checkpoint 007 (SHA256 `d643f18eed205db95a77de6622b8b59d9badb8040ceda1b028d4bbccdf5f5362`). Those sources are themselves unreviewed working candidates; this checkpoint does not upgrade them.

The four distinct labels are `a,b,c,d`. The reference is normalized with positive real Schmidt amplitudes `c_a,c_b,c_c,c_d`; write `x_i=c_i^2`, with sum `x_i=1`. Strict positivity is imposed only while using an invertible filter. Section 7 explains the boundary issue; no division by a zero Schmidt amplitude is permitted.

In the ordered computational basis

```
P1 = |a,c,b,d>,  P2 = |b,d,a,c>,
P3 = |a,d,b,c>,  P4 = |b,c,a,d>,
```

the original matrices are

```
C4 = [[1,   1/4, -1/2, -1/2],
      [1/4, 1,   -1/2, -1/2],
      [-1/2,-1/2,1,    1/4 ],
      [-1/2,-1/2,1/4,  1   ]],

S4 = [[0,     -e,  x_a/(4 d_ab), x_c/(4 d_cd)],
      [-e,     0,  x_d/(4 d_cd), x_b/(4 d_ab)],
      [x_a/(4 d_ab), x_d/(4 d_cd), 0, -f],
      [x_c/(4 d_cd), x_b/(4 d_ab),-f,  0]],
```

where `d_ij=1-(x_i+x_j)/2`, `e=E_ac`, and `f=E_ad`. The target here is `M4=C4-S4 >= 0`.

## 2. A determinant-one filter, without an irrational witness requirement

Set

```
g = c_a c_b c_c c_d > 0,
D = diag(c_b c_d, c_a c_c, c_b c_c, c_a c_d),
r = c_b/c_a,  s = c_d/c_c.
```

Define the congruent matrices

```
Ctilde = D C4 D/g,
Stilde = D S4 D/g,
Mtilde = Ctilde-Stilde.
```

Equivalently the diagonal filter is `D/sqrt(g)`, with entries

```
sqrt(r s), 1/sqrt(r s), sqrt(r/s), sqrt(s/r).
```

Its determinant is one: `det(D)=g^2`, so `det(D/sqrt(g))=1`. Hence `det(Mtilde)=det(M4)` exactly. Although the normalized description uses square roots, the unnormalized filter `D` has polynomial amplitude entries. With rational amplitudes, a rational negative vector can therefore be lifted without introducing irrational physical coordinates; Section 6 makes the scaling explicit.

Introduce

```
H_r=(r+r^(-1))/2,  L_r=(r-r^(-1))/2,
H_s=(s+s^(-1))/2,  L_s=(s-s^(-1))/2,
h1=H_r H_s+L_r L_s,
h2=H_r H_s-L_r L_s,
l1=L_r H_s+H_r L_s,
l2=L_r H_s-H_r L_s.
```

Thus `H_r,H_s>=1`, `H_r^2-L_r^2=H_s^2-L_s^2=1`, and

```
h1=(rs+(rs)^(-1))/2 >= 1,
h2=(r/s+s/r)/2 >= 1.
```

Also set

```
k = c_a c_b/(4 d_ab),
l = c_c c_d/(4 d_cd).
```

These are nonnegative and at most `1/4`. For example, with `T=x_a+x_b`,

```
k <= T/[4(2-T)] <= 1/4.
```

More precisely, `k=T/[4(2-T)H_r]` and `l=(1-T)/[4(1+T)H_s]`. The filtered off-diagonal entries of `S4` on edges `(1,3),(2,4)` both become `k`; those on `(1,4),(2,3)` both become `l`. The opposite entries remain `-e,-f`.

## 3. Explicit parity blocks

Use the orthonormal basis, in this order,

```
u1+ = (P1+P2)/sqrt(2),  u2+ = (P3+P4)/sqrt(2),
u1- = (P1-P2)/sqrt(2),  u2- = (P3-P4)/sqrt(2).
```

Write `O` for this real orthogonal change of basis. Direct addition of the displayed entries gives

```
O^T Ctilde O = [[P, R], [R^T, N]],
O^T Stilde O = [[U, 0], [0, V]],
```

with

```
P = [[h1+1/4, -(H_r+H_s)/2],
     [-(H_r+H_s)/2, h2+1/4]],

N = [[h1-1/4, -(H_r-H_s)/2],
     [-(H_r-H_s)/2, h2-1/4]],

R = [[l1, -(L_r-L_s)/2],
     [-(L_r+L_s)/2, l2]],

U = [[-e, k+l], [k+l, -f]],
V = [[ e, k-l], [k-l,  f]].
```

Only this filtered four-dimensional `S` block is being split by the simultaneous-exchange parity. No global parity symmetry of `S_eta` on all 256 dimensions is asserted. The `C` cross block `R` is generally nonzero and cannot be discarded.

## 4. The minus-parity pivot is uniformly positive

First,

```
N-(3/4)I = [[h1-1, -(H_r-H_s)/2],
            [-(H_r-H_s)/2, h2-1]].
```

Both diagonal entries are nonnegative. Its determinant is

```
(H_r H_s-1)^2-L_r^2 L_s^2-(H_r-H_s)^2/4
= (H_r-H_s)^2-(H_r-H_s)^2/4
= 3(H_r-H_s)^2/4 >= 0.
```

The middle equality follows by inserting `L_r^2=H_r^2-1` and `L_s^2=H_s^2-1`. Thus `N >= (3/4)I` for every positive `r,s`, not just near equal Schmidt coefficients.

Next, `0<=e,f<=1/4` and `|k-l|<=1/4`. The maximum absolute row sum of `V` is at most `1/2`, so its Hermitian operator norm is at most `1/2`. This does **not** assert that `V` is positive semidefinite. Consequently the actual pivot

```
H = N-V >= (1/4)I
```

is strictly positive for every interior reference.

The analogous negative-parity pivot of `3 C4+S4` is `3N+V >= (7/4)I`, but that observation alone does not prove the lower form. The previously written conditional trace argument remains the stated lower-four-block route once the upper block is proved.

## 5. Exact residual: one two-dimensional Schur determinant

The actual upper block is congruent to

```
[[P-U, R], [R^T, H]],  H=N-V>0.
```

Hence its remaining Schur matrix is exactly

```
Q = P-U-R H^(-1) R^T.                         (8.1)
```

There is no endpoint-singular or approximate inverse in (8.1) while the amplitudes are positive: `H >= I/4`.

The determinant identity is

```
det(M4) = det(H) det(Q).                       (8.2)
```

The filter has determinant one and `O` is orthogonal, so no extra sign or scaling factor is suppressed in (8.2).

Checkpoint 007's strict interior leading three-minor gives at least three positive eigenvalues of `M4`. Congruence preserves inertia, and eliminating the positive two-dimensional `H` leaves at least one positive eigenvalue of the two-dimensional `Q`. Therefore, at this working-candidate boundary,

```
M4 >= 0  <=>  Q >= 0  <=>  det(Q) >= 0,
```

and strict positivity is equivalent to `det(Q)>0`. The determinant in (8.1) has **not** been proved nonnegative. This is a transparent positive-pivot representation of the same missing full determinant, not its solution.

## 6. Exact route-failure lift, if a negative residual is subsequently found

For any vector `z` with `z^* Q z<0`, put

```
w = -H^(-1) R^T z.
```

Then `(z,w)^* [[P-U,R],[R^T,H]] (z,w)=z^*Qz`. The physical four-block vector

```
y = (D/sqrt(g)) O (z,w)
```

has `y^* M4 y<0`. Equivalently use `O0=sqrt(2)O`, whose entries are `0,+1,-1`, and take

```
y0 = D O0 (z,w),
y0^* M4 y0 = 2g z^*Qz < 0.
```

For rational positive amplitudes all displayed matrices `P,N,R,U,V,H,Q` are rational, and an exact rational negative direction, if present, gives rational `w,y0`. No such negative direction has been found here. Even a genuine negative direction would disprove only this co-Choi sufficient route, not supply a rank-two negative W4 coefficient operator.

## 7. Boundary and literal frontier

The invertible filter is used only when all four Schmidt amplitudes are positive. It is not evaluated at a zero amplitude. A proof of the remaining determinant on that interior would extend the original physical `M4` to every normalized nonnegative reference by continuity, using the already regular full inverse and `A_eta>=I/4`. The singular filter is not the continuity argument.

The universal target remains **both** `C_B-S_eta>=0` and `3C_B+S_eta>=0` for all nonzero two-site references. The current literal unproved obligations are unchanged:

1. the full four-dimensional upper determinant, now equivalently (8.1)'s two-dimensional Schur determinant; the four-dimensional lower form remains conditional on that upper result via the recorded trace argument;
2. both seven-dimensional residuals of the nonzero-charge twelve-dimensional blocks;
3. both twelve-dimensional residuals of the zero-charge block.

The seven fixed-reference exact-assay passes remain finite evidence only. The separately proposed polynomial coefficient assay has not been executed by this worker and is not an input to any identity or inequality in this checkpoint. No new scientific-execution permission is inferred.
