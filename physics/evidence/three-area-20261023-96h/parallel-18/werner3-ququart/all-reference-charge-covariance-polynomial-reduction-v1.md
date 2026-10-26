# Exact proposed universal charge-covariance certificate: a degree-seven four-matrix

Before-writing clock observed: `2026-10-23T18:38:31-07:00` (`/bin/date -Iseconds`).

Status: **UNEXECUTED PROPOSAL / CANDIDATE exact reduction**, not an admission or a positive certificate. No scientific program, import, compilation, syntax test, numerical evaluation, solver, or replay has been performed. This is within the same all-reference W4 obligation; it is not a new fixed-reference sampling batch.

## 1. Scientific consequence and non-consequence

In one generic nonzero-charge twelve-dimensional upper block, take the principal space `(Q_perp,R2,R3,T2,T3)`, of dimension seven, leaving out P4. The Q block is already exactly positive on its three-dimensional complement. This proposal asks whether its **entire four-dimensional R/T Schur matrix** has a universal ordered-cone coefficient certificate.

A successful certificate would prove this joint seven-dimensional principal block strictly positive throughout the positive reference interior. It would allow its exact Schur elimination from the upper block, leaving an **upper four-dimensional** P residual instead of the active upper seven-dimensional representation. That remaining P sign would still need proof. Zero-charge signs and the lower form would not be settled. A failed coefficient ansatz is not a negative route direction or a W4 witness.

All probability vectors remain quantified. Boundary nonnegativity of the physical principal matrix would follow by continuity; any later closed-simplex proof of the whole upper block must extend its full physical matrix, not divide by a boundary-degenerate amplitude chart.

## 2. Raw and covariance interfaces

Use checkpoint 013 (SHA256 `cf4734d64a507777c28042cf2ec7ba39bd8181c59c29f164e025bbc61e4ef9a1`) and its raw checkpoint-004 source. Set the charged labels `a=0,b=1`, spectators `j=2,k=3`, and the R/T order

```
R2, R3, T2, T3.
```

After the positive diagonal amplitude congruence of checkpoint 013, the Q block is `L(tau x)`, where `tau_i=1/2` on i=0,1 and one otherwise. Its cross columns have zero sum. For such columns g,h the exact inverse pairing is

```
g^* L(tau x)^+ h=sum_i conjugate(g_i)h_i/(tau_i x_i).
```

This is the Q elimination being used. It is not the earlier R/T-first upper-seven matrix.

## 3. Homogeneous variables and linear column numerators

Use formal nonnegative variables `p0,p1,p2,p3`, not all zero, and set

```
S=p0+p1+p2+p3, x_i=p_i/S,
D_uv=2S-p_u-p_v,
W3=S^3+2S e2(p)-e3(p),
B2=S^2-2S(p0+p1)+p0p1-p2p3.
```

Then `d_uv=D_uv/(2S)`, `W=W3/S^3`, and `beta=S B2/(4W3)`. All `D_uv,S,W3` are strictly positive on the nonzero closed orthant; indeed `D_uv>=S` and `W3>=S^3`.

For a column r define its spectator label `l(r)` and partner `b(r)` as

```
r:       R2 R3 T2 T3
l(r):     2  3  2  3
b(r):     1  1  0  0
u_r=D_(l(r),b(r)).
```

The scaled Q-cross entries have the exact form

```
g_(i,r)=x_i H_(i,r)/(2u_r),
H_(i,r)=-delta_(i,l(r)) u_r
        +p_(l(r))[2-delta_(i,l(r))-delta_(i,b(r))]. (15.1)
```

For example `g_(i,R2)=-x2 delta_i2/2+x_i x2 tau_i^(21)/(2d_21)`, and inserting `d_21=D_21/(2S)` gives (15.1). Define the degree-three polynomial

```
Gamma_rs=sum_i omega_i p_i H_(i,r)H_(i,s),
omega_0=omega_1=2, omega_2=omega_3=1.
```

The exact Q Schur subtraction is consequently

```
Gamma_rs/(4S u_r u_s).                     (15.2)
```

## 4. A small denominator-clearing congruence

Let `R(x)` be the actual four-dimensional R/T Schur matrix after the Q elimination. Multiply it on both sides by `diag(u_r)`, and then by the positive scalar

```
L0=4S W3 D_23.
```

The resulting symmetric integer polynomial matrix

```
P(p)=L0 diag(u_r) R(p/S) diag(u_r)           (15.3)
```

has homogeneous degree **seven**, not degree thirteen: using a column-specific congruence avoids squaring a product of all four mixed denominators.

It is completely specified as follows. Start with `P_rs=-W3 D_23 Gamma_rs` for every pair. Add the C contribution:

- if `r=s`, add `4W3 D_23 u_r^2 p_(l(r))`;
- if r,s are opposite R/T types with the same spectator, add `W3 D_23 u_r u_s p_(l(r))`;
- otherwise add zero.

Subtract the S contribution:

- if r,s are opposite R/T types with the same spectator, subtract `S D_23 u_r u_s p_(l(r)) B2`;
- if r,s are opposite R/T types with different spectators, subtract `2W3 u_r u_s p2p3`;
- otherwise subtract zero.

Every term has degree seven. These are exactly the old C/S R/T entries and (15.2), without a new reference, an omitted inverse correction, or an assumed sign.

## 5. Hand calibration, not a universal identity proof

At `p0=p1=p2=p3=1`, one has `S=4`, `u_r=D_23=6`, `W3=108`, and `L0=10368`. The calibrated polynomial matrix is

```
P(1,1,1,1)=
[[68040, 6480, -648,     0],
 [ 6480,68040,    0,  -648],
 [ -648,    0,68040,  6480],
 [    0, -648, 6480,68040]].                 (15.4)
```

For a transparent derivation, the physical R/T Schur matrix before the amplitude and denominator congruences diagonalizes in the four normalized Hadamard sign vectors with eigenvalues

```
19/24, 47/72, 29/36, 2/3
```

for signs `++++`, `+-+-`, `++--`, `+--+`, respectively. The combined scale from that physical matrix to (15.4) is `93312`. Equivalently (15.4) is the sum of outer products of the four unnormalized sign vectors with coefficients `18468,15228,18792,15552` in that order.

Its leading determinants are therefore

```
a,
a^2-b^2,
a(a^2-b^2-c^2),
73872*60912*75168*62208,
```

where `a=68040,b=6480,c=648`. These exact products serve as a known-point calibration only. Agreement there cannot establish the polynomial identity (15.3), which still requires the displayed symbolic derivation and a separate raw reconstruction before acceptance.

## 6. Fixed proposed coefficient experiment

A proposed standalone integer-polynomial source will:

1. build exactly P from Section 4;
2. perform symbolic cancellation, 2x2 determinant-sign and ordered-gap controls, and compare all sixteen entries and four leading minors at the single hand calibration (15.4);
3. calculate the four leading determinants, of degrees `7,14,21,28`;
4. for every one of the twenty-four variable orderings, substitute ordered gaps so the ordered probabilities are `g0+g1+g2+g3`, `g1+g2+g3`, `g2+g3`, `g3`;
5. require every resulting coefficient nonnegative and the pure `g3^(7k)` coefficient positive;
6. preserve complete exact coefficient arrays, or stop at the first negative coefficient with an **INCONCLUSIVE_ANSATZ_NOT_ROUTE_FAILURE** status.

A full pass would be an exact certificate candidate for this printed component matrix on the whole interior, using Sylvester's criterion and the positive factors in (15.3). It would **not** be independent verification of the physical table, the remaining upper P4 form, either zero9 form, the lower5 form, or W4. A time/resource/stop gate yields UNKNOWN, not mathematical exhaustion. There is no automatic second algorithm, rerun, reference sweep, or follow-on experiment.

Requested prospective envelope: one local CPU process, internal monotonic deadline at most180 seconds, cooperative RSS guard512MiB, tool timeout0, private owned lane output and TMPDIR, no subprocess/network/model access. This text is **not GO**. The complete successor source and request must be frozen and read by the parent, with fresh resources and exact launch/settlement admission, before any import, syntax/compile check, or execution. The old four-polynomial proposal remains separately HOLD and is not revived.
