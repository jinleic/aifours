# All-reference working checkpoint 010: both zero-sector residuals reduce from twelve to nine

Before-writing clock observed: `2026-10-23T17:47:13-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written algebra**, within the same unfinished all-reference W4 route. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. This does not prove the remaining nine-dimensional forms positive.

**Delta:** a three-dimensional skew-matrix subspace has a uniformly positive principal form **after** the required reference and symmetric-q Schur operations, for **both** asymmetric signs. Thus its actual Schur elimination, retaining all cross terms, replaces each zero-charge twelve-dimensional residual by a nine-dimensional residual. The lower reference subtraction is not omitted.

## 1. Raw interfaces and order of operations

Use the zero-charge physical table in checkpoint 002 (SHA256 `3940d80c695b96272b59cb3c10c98ccadde720f63dc93152155be4f4b17fdea1`) and the q pivots in checkpoint 003 (SHA256 `77b39b558944fa8e4892f92020421bc7d458bf170da2691f9e9fd75f9b3af006`). Both remain unreviewed working sources; no inherited acceptance is claimed.

Normalize the real Schmidt vector `c=(c_1,...,c_4)^T`, `c_i>=0`, `c^T c=1`; write `x_i=c_i^2`, `d_i=1-x_i`, and `d_ab=(d_a+d_b)/2`. The zero-charge coordinates are

```
p(i,j)=|i,i,j,j>,                 16 coordinates,
q(a,b)=|a,b,b,a>, a!=b,           12 coordinates.
```

The p coefficient matrix is `Z=(z_ij)`. After separating the known reference directions `eta_input tensor |j,j>_output`, the p quotient is

```
c^T Z=0,                        complex dimension 12.
```

The antisymmetric q directions are reducing and already have positive pivots. In the six normalized symmetric q coordinates

```
q_+(a,b)=[q(a,b)+q(b,a)]/sqrt(2), a<b,
```

the upper pivot `Q_up` satisfies `Q_up>=I/2`. For the lower sign, first eliminate the **actual positive reference block** using its full inverse; the resulting symmetric-q pivot satisfies `Q_low>=I/4`. These are the exact pivots being used here. Positivity of the remaining p forms is not presumed.

For the upper p form on the quotient the earlier table reads

```
D_pp(Z)=sum_(i!=j)|z_ij|^2
        +sum_i [r/d_i^2-x_i/d_i]|z_ii|^2
        +sum_(i!=j) [r/(d_i d_j)] conjugate(z_ij) z_ji,
```

where `D=C-S`, and the expression is interpreted by its regular full-inverse version at a product vertex. The upper coupling functional to an ordered q direction is

```
G_ab(Z)=-(z_ba+z_ab)/2
        -[x_a z_ab+x_b z_ba+c_a c_b(z_aa+z_bb)]/(4d_ab).
                                                        (10.1)
```

It satisfies `G_ab=G_ba`. The normalized symmetric-q coupling is consequently `sqrt(2)G_ab`, not `G_ab`.

The C coupling from the reference block to `(Z,q_+)` is recorded by

```
g(Z,q_+)=Z c/4-diag(c)diag(Z)-(W_q+W_q^T)c/2,
```

with `W_q` denoting the corresponding off-diagonal q-coordinate matrix. Only its value at `q_+=0` is needed below.

## 2. The three-dimensional skew subspace

Inside the p quotient consider

```
Kspace={K: K^T=-K, K c=0}.
```

Since c is real, `Kc=0` also gives `c^T K=0`, so these vectors genuinely belong to the same p quotient. This is a **complex** skew-transpose condition, not a restriction to real coefficients or a skew-Hermitian condition.

Every such K has a unique parametrization

```
K_ab=epsilon_abkl (c_k v_l-c_l v_k),
```

where `{k,l}` is the complementary pair in increasing order, the Levi-Civita sign uses the ordered pair `a<b`, and `v` ranges over `c^T v=0`. This is the Hodge dual of `c wedge v`. The map is injective and has a three-dimensional image, hence gives precisely `Kspace`. Its norms are

```
sum_(a<b)|K_ab|^2=||v||^2,
||K||_HS^2=2||v||^2.                         (10.2)
```

These identities also hold for complex v by the complex Lagrange identity with real c.

## 3. A regular weighted-wedge estimate

Let

```
u=sum_i d_i x_i=1-sum_i x_i^2=2e_2(x),
W=e_3(d)=1+u-e_3(x).
```

The elementary symmetric identity

```
e_2(x)=sum_(i<j)x_i x_j(x_i+x_j)+3e_3(x)
```

uses `sum x_i=1`, so `e_3(x)<=e_2(x)/3=u/6`. Cauchy-Schwarz gives `0<=u<=3/4`. It follows that

```
W>=1+5u/6,
u/W<=6/13.                                  (10.3)
```

The last function increases in u, and at `u=3/4` it equals `(3/4)/(13/8)=6/13`.

The potentially singular ratio in the raw table has the regular expression

```
r/(d_a d_b)=d_k d_l/W,
```

where `{k,l}` is the complement of `{a,b}`. Thus it is never necessary to substitute an infinite `x_i/d_i` in the skew calculation, whose diagonal coefficients vanish anyway.

Under the parametrization (10.2),

```
Tweight=sum_(a<b)d_k d_l |K_ab|^2
       =sum_(i<j)d_i d_j |c_i v_j-c_j v_i|^2
       =u sum_i d_i |v_i|^2-|sum_i d_i c_i v_i|^2
       <=u ||v||^2.                          (10.4)
```

Here `0<=d_i<=1`; the equality is the weighted complex Lagrange identity. In particular `Tweight>=0`.

## 4. Upper form after the symmetric-q Schur operation

For a skew K the raw p form simplifies exactly to

```
D_pp(K)=2[||v||^2-Tweight/W]
       >=(14/13)||v||^2,                     (10.5)
```

by (10.3)-(10.4). No constraint involving diagonal p entries has been silently dropped: those entries are zero for K.

Equation (10.1) gives

```
G_ab(K)=-(x_a-x_b)K_ab/(4d_ab).
```

Let `h` be the normalized six-dimensional q coupling column for this fixed K. Its squared norm is

```
||h||^2=sum_(a<b)(x_a-x_b)^2 |K_ab|^2/(8d_ab^2).
```

Because `Q_up>=I/2`, the actual q Schur subtraction is at most

```
h^* Q_up^(-1)h
<=2||h||^2
=sum_(a<b)[(x_a-x_b)/(d_a+d_b)]^2 |K_ab|^2
<=sum_(a<b)|K_ab|^2=||v||^2.                 (10.6)
```

The last inequality uses `|x_a-x_b|=|d_a-d_b|<=d_a+d_b`; the denominator is at least one. Combining (10.5)-(10.6), the resulting twelve-dimensional p residual has on `Kspace` the principal bound

```
D_zero,p-after-q(K)>=(1/13)||v||^2
                    =(1/26)||K||_HS^2.      (10.7)
```

Thus this three-dimensional principal pivot is strictly positive uniformly, including at boundary references. Cross terms with its nine-dimensional orthogonal complement remain and must be included in its subsequent Schur complement.

## 5. Lower form: the reference correction vanishes on this subspace, not globally

For `Z=K` and `q_+=0`, the reference pairing is

```
g(K,0)=K c/4-diag(c)diag(K)=0.
```

Accordingly the true lower reference Schur subtraction changes neither the K principal block nor its K-to-q coupling. This conclusion is specific to `Kspace`; it is not permission to delete the reference block for a general p vector.

On the skew p coordinates the C table gives

```
C_pp(K)=(3/4)||K||_HS^2=(3/2)||v||^2.
```

Since `3C+S=4C-D`, (10.5)'s exact first expression, rather than its lower bound, gives the lower p principal form

```
(3C+S)_pp(K)
=6||v||^2-2[||v||^2-Tweight/W]
=4||v||^2+2Tweight/W
>=4||v||^2.                                 (10.8)
```

Also `C_pq(K)=-(K_ba+K_ab)/2=0`. Thus the lower normalized K-to-q coupling is `-h`, the opposite of the upper coupling, and has exactly the same norm.

The already reference-corrected lower symmetric-q pivot obeys `Q_low>=I/4`. Its actual Schur subtraction is therefore at most

```
h^* Q_low^(-1)h<=4||h||^2<=2||v||^2,        (10.9)
```

by the same denominator estimate as (10.6). Equations (10.8)-(10.9) prove, on the twelve-dimensional lower p residual,

```
L_zero,p-after-reference-and-q(K)
>=2||v||^2=||K||_HS^2.                      (10.10)
```

This is a genuine positive principal pivot **after** both required operations.

## 6. Exact resulting residuals, not a positivity conclusion

The p quotient has physical Hilbert-Schmidt dimension twelve. Its subspace `Kspace` has dimension three, with the strictly positive principal bounds (10.7) and (10.10). Choose its orthogonal complement in that same quotient, of dimension nine, and perform the exact Schur complement on the K pivot, retaining every K/complement cross term.

- The full zero-charge **upper** positivity question is equivalent to nonnegativity of the resulting **nine-dimensional** Schur form.
- The full zero-charge **lower** positivity question is equivalent to nonnegativity of its own **nine-dimensional** Schur form, after the actual reference and q eliminations specified above.

Neither nine-dimensional Schur form has been proved nonnegative here. The two signs have different pivots and cross terms; they are not being identified.

This is a reduction valid for every normalized nonnegative Schmidt reference, including zeros and repetitions, not a positive neighborhood or a paired-spectrum restriction. Product-vertex expressions are read through the regular `d_k d_l/W` formula, not divergent q symbols.

## 7. Literal remaining frontier

Combining this working leaf with the complete four-block hand proof in checkpoint 009 (SHA256 `49ec952c85f567fae0a5145fb71a5e516bc9dd6ddef710c992f59bb6045bb48e`), the same unfinished universal-reference candidate now has these unproved obligations:

1. both seven-dimensional nonzero-charge residuals;
2. both nine-dimensional zero-charge residuals obtained in Section 6.

No all-reference theorem, full W4 theorem, exact negative route direction, exact rank-two Werner witness, novelty finding, independent acceptance, or kernel proof is claimed. The fixed-reference assay remains finite evidence and supplies no inequality used in this hand derivation. The pending four-polynomial assay remains an author-requested HOLD, not an executed or successful certificate.
