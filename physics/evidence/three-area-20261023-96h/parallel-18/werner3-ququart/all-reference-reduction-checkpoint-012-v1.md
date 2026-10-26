# All-reference working checkpoint 012: one mixed lower pivot leaves five dimensions

Before-writing clock observed: `2026-10-23T18:05:39-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written algebra**. No scientific execution, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. This is a refinement within the same unfinished universal-reference candidate, not a new problem or an accepted theorem.

The input is checkpoint 011, SHA256 `cdb9b17897603fc454e94de069b0353d2bbd3094f8e2efcc9b832a54df4cee8f`: in real Schmidt coordinates, with `P=|eta><eta|`, `Q=I-P`, and `X_eta=M_eta^*(I)`, its hand-derived bound is

```
Q X_eta Q <= (17/8)Q.                       (12.1)
```

The source remains unreviewed. This checkpoint supplies a simpler general Kraus bound and uses the **joint** positivity of a six-dimensional lower subspace. It does not add dimensions merely because separate principal blocks are positive.

## 1. A full-space Kraus bound, with its actual tensor order

For a CP map `M(X)=sum_alpha K_alpha X K_alpha^dagger`, its reversed-input Choi matrix is

```
S=sum_alpha (K_alpha^dagger tensor I) F (K_alpha tensor I),
```

since this equals `sum_alpha (I tensor K_alpha)F(I tensor K_alpha^dagger)`. From `-I<=F<=I`,

```
-M^*(I) tensor I <= S <= M^*(I) tensor I.    (12.2)
```

Consequently (12.1) gives on the **entire** input-perpendicular space `eta^perp tensor C^16`, not just its antisymmetric part,

```
-(17/8)I <= S_eta <= (17/8)I.                (12.3)
```

The inequalities mean compressed quadratic forms on that space. They do not assert the same marginal bound in the reference direction, where it is false. Checkpoint 011's antisymmetric derivation remains valid, but (12.2) is enough for the use below.

## 2. The actual high-C direction in a nonzero-charge block

Fix `a!=b`, with spectators `{j,k}`. In the orthonormal computational coordinates of checkpoint 004,

```
Q_i=|i,i,a,b>, P_i=|a,b,i,i>,
R_l=|a,l,l,b>, T_l=|l,b,a,l>, l=j,k,
```

define the orthonormal high-C vectors

```
H_j=(Q_j+P_j-R_j-T_j)/2,
H_k=(Q_k+P_k-R_k-T_k)/2.
```

The printed physical C table gives exactly

```
C_B H_j=(9/4)H_j,
C_B H_k=(9/4)H_k.
```

The input-reference projection of `alpha_j H_j+alpha_k H_k` is

```
[(c_j alpha_j+c_k alpha_k)/2] eta_input tensor |a,b>_output.
```

Thus the subspace of these vectors satisfying `c_j alpha_j+c_k alpha_k=0` has dimension at least one and lies in `eta^perp tensor C^16`. Choose any normalized vector h in it. When `c_j^2+c_k^2>0` one explicit choice is

```
h=(c_k H_j-c_j H_k)/sqrt(c_j^2+c_k^2).
```

When both spectator amplitudes vanish, choose `h=H_j`; the formula with a zero denominator is not used. No kernel classification at that boundary is being inferred.

By (12.3), the high-C direction alone obeys

```
<h,(C_B-S_eta)h> >= 9/4-17/8=1/8,
<h,(3C_B+S_eta)h> >= 27/4-17/8=37/8.         (12.4)
```

## 3. Joint positivity with the five-dimensional skew subspace

Let A5 be the five-dimensional space from checkpoint 011,

```
sum_i u_i(Q_i-P_i)/sqrt(2)
+sum_(l=j,k) v_l(R_l-T_l)/sqrt(2),
c^T u=0.
```

It lies in `eta^perp tensor C^16` and has `C_B=(3/4)I`. Its vectors are globally antisymmetric under exchanging the entire input/output pairs. The vector h is globally symmetric, so `A5` and `span{h}` are orthogonal. They are distinct C eigenspaces. Therefore on their **whole direct sum** A6,

```
C_B >= (3/4)I,
S_eta >= -(17/8)I,
3C_B+S_eta >= (1/8)I.                       (12.5)
```

Equation (12.3) bounds the full compression, including all S cross terms between A5 and h. This is the reason six dimensions can be eliminated together. Separate diagonal-block bounds alone would not justify that operation.

## 4. Reference Schur correction and the five-dimensional residual

The block reference vector is `K=sum_i c_i Q_i`, with true lower diagonal `4d_ab>0`. Every vector of A5 and h is orthogonal to K. C acts on A5 by `3/4` and on h by `9/4`, so its pairing from K to **each** of these subspaces vanishes. The exact identity `D K=0` for `D=C_B-S_eta` then makes the lower reference coupling vanish on their direct sum as well.

Accordingly, after eliminating the actual positive K block, the principal form on A6 is still at least `I/8`. Remove this **six-dimensional** principal block by its exact Schur complement, retaining its cross terms with all remaining directions. Out of the eleven dimensions left after K, this leaves **five**.

Full lower positivity of the original nonzero-charge twelve-dimensional block is equivalent to nonnegativity of that resulting five-dimensional Schur form. Its sign is **unproved**. This is a different pivot order from the earlier R/T-first seven-dimensional representation and the skew-first six-dimensional representation; their old matrices are not being conflated.

For the upper form, (12.4) proves only the isolated high direction. It does not prove joint positivity with the old four-dimensional R/T pivot. The active upper residual is therefore still **seven-dimensional**, not six-dimensional by dimension counting.

## 5. Literal frontier

The same all-reference route still has exactly these unproved forms at this working boundary:

1. the nonzero-charge **upper seven-dimensional** residual;
2. the nonzero-charge **lower five-dimensional** residual from Section 4;
3. **both zero-charge nine-dimensional** residuals from checkpoint 010.

All nonzero two-site references remain quantified through their complete nonnegative Schmidt spectra, including zeros and repetitions. No universal-reference theorem, full W4 theorem, exact route failure, rank-two negative Werner witness, novelty verdict, independent acceptance, or kernel proof is claimed.
