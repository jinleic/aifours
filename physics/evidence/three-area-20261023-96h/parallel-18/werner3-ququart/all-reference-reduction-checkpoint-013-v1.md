# All-reference working checkpoint 013: rational probability charts and covariance Laplacians

Before-writing clock observed: `2026-10-23T18:20:03-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED exact representation**, not a positivity proof of the remaining forms. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. The universal-reference target is unchanged.

The new representation removes every Schmidt square root from the raw charge and zero-sector tables by positive diagonal congruence. The reference kernels become constant coordinate directions. It also supplies an explicit rational nine-plus-three chart for the zero-sector p quotient. These facts make a complete symbolic certificate a precise finite algebraic obligation rather than a sampling problem, but no such certificate is claimed or executed here.

## 1. Common notation and the domain of the chart

Let `c_i>0`, `x_i=c_i^2`, `sum x_i=1`, and

```
d_i=1-x_i, d_ij=1-(x_i+x_j)/2,
W=e_3(d)=1+2e_2(x)-e_3(x)>0.
```

The raw physical matrices are those in checkpoint 004 (SHA256 `98e0d5f820e1b9aeabe9b88410afc6c3d1771feaffb2dfa7fe1798812c649d72`) and checkpoint 002 (SHA256 `3940d80c695b96272b59cb3c10c98ccadde720f63dc93152155be4f4b17fdea1`), with the regular inverse from checkpoint 005 (SHA256 `6cfa523879ded76992804f916ba9afb00075b98b972199026512c298b2d7c00c`). These are unreviewed working sources, not imported acceptances.

Every congruence below is invertible on the full positive interior. No eigenvalue bound in an orthonormal physical basis is transferred unchanged to its nonorthonormal coordinate Gram matrix. Matrix signs and exact Schur equivalences are preserved by congruence. The physical matrices themselves are continuous at all boundary spectra because `A_eta>=I/4`; a proof over the entire interior would extend positivity to every zero or repeated Schmidt amplitude. The charts are not evaluated by dividing by a zero amplitude, and the all-reference quantifier is not being reduced to the interior without that extension.

## 2. Nonzero-charge block: one diagonal congruence removes all roots

Fix `a!=b`, with spectators `{j,k}`. Retain the physical basis `Q_i,P_i,R_j,R_k,T_j,T_k` from checkpoint 004. Apply the diagonal congruence which multiplies each `Q_i` and `P_i` by `c_i`, and multiplies `R_l,T_l` by `c_l`.

Put

```
tau_i=1-(delta_ia+delta_ib)/2,
w_i=tau_i x_i, d=d_ab=sum_i w_i,
sigma_i=1-2delta_ia-2delta_ib,
T=x_a+x_b, m=x_a x_b, n=x_j x_k.
```

For any positive weight vector w define the covariance Laplacian

```
L(w)=diag(w)-w w^T/(sum_i w_i).
```

It is positive semidefinite, with constant kernel `1`, and depends rationally on w. Write `w^(uv)_i=[1-(delta_iu+delta_iv)/2]x_i`.

In the congruent matrices, denoted by bars, the **whole Q part of the upper form** `D=C-S` becomes

```
Dbar_QQ=L(w),
Dbar_Q,Pi=kappa_i L(x)e_i,
Dbar_Q,Rl=-L(w^(lb))e_l,
Dbar_Q,Tl=-L(w^(al))e_l.                     (13.1)
```

The regular coefficients are

```
kappa_a=-d_b(d_j+d_k)/(2W),
kappa_b=-d_a(d_j+d_k)/(2W),
kappa_j= d_k(d_a+d_b)/(2W),
kappa_k= d_j(d_a+d_b)/(2W).
```

For example `Dbar_Q,Rl` has entries

```
-x_l delta_il/2+x_i x_l tau_i^(lb)/(2d_lb),
```

which is exactly `-L(w^(lb))e_l` since `w_l^(lb)=x_l/2`. The Q-reference kernel is now simply `1_Q`, independent of the reference angles. No generic mixed-input inverse term was discarded.

For completeness the remaining congruent entries are rational as well:

```
Cbar_QQ=Cbar_PP=diag(w),
Cbar_Q,Pi=(sigma_i x_i/4)e_i,
Cbar_Q,Rl=Cbar_Q,Tl=Cbar_P,Rl=Cbar_P,Tl=-(x_l/2)e_l,
Cbar_(R,T)=[[diag(x_j,x_k),diag(x_j,x_k)/4],
           [diag(x_j,x_k)/4,diag(x_j,x_k)]].
```

The remaining S entries are

```
Sbar_PP=[m/(4d)](e_a+e_b)(e_a+e_b)^T,
Sbar_P,Rl=[x_a x_l/(4d_al)](e_a+e_l),
Sbar_P,Tl=[x_b x_l/(4d_bl)](e_b+e_l),
Sbar_(R,T)=[[0,Bbar],[Bbar,0]],

Bbar=[[x_j beta, x_j x_k/(4d_jk)],
      [x_j x_k/(4d_jk), x_k beta]],
beta=(1-2T+m-n)/(4W).
```

Together with (13.1) and `Sbar_Q*=Cbar_Q*-Dbar_Q*`, these specify the entire twelve-dimensional table without a square root.

### Exact Q-first inverse rule

If `sum_i g_i=sum_i h_i=0`, then

```
g^* L(w)^+ h=sum_i conjugate(g_i)h_i/w_i.    (13.2)
```

Indeed `q_i=h_i/w_i+constant` solves `L(w)q=h`, and the constant drops from pairing with g. Every cross column in (13.1) has zero coordinate sum. Thus eliminating the rank-three Q block is completely explicit: subtract the Gram matrix `sum_i conjugate(g_i)h_i/w_i` from the remaining eight-dimensional block.

This is an alternate exact eight-dimensional representation, not a claim improving the currently active upper seven-dimensional residual. Its usefulness is that only positive weights and rational covariance columns occur; no angular square-root basis or numerical pseudoinverse is needed.

## 3. Zero-charge block: rational raw entries

For the zero-charge physical basis multiply **both** `p(i,j)` and `q(i,j)` by `c_i c_j` (with `i!=j` for q). The four p-reference kernel directions become the constant-column vectors `1_(column j)`.

Let `G` be the inverse block on the diagonal two-site basis `|ii>`, and define

```
H0=diag(c) G diag(c).
```

It has the regular rational entries

```
(H0)_ii=x_i[product_(l!=i)d_l
           +sum_(l<t, l,t!=i)d_l d_t]/W,
(H0)_ij=-x_i x_j d_k d_l/W, i!=j,
```

where `{k,l}` complements `{i,j}`. Set

```
t_i^j=x_i[(1-delta_ij)e_j+(delta_ij/4)1].
```

The full congruent p-p S table is exactly

```
Sbar_(p(i,j),p(k,l))=(t_k^j)^T H0 t_i^l.     (13.3)
```

To check the factors directly, the old vector `W_k^j` satisfies

```
c_k c_j W_k^j=diag(c)t_k^j.
```

Multiplying the analogous identity for `W_i^l` supplies precisely the product of the two congruence factors `c_i c_j c_k c_l` in (13.3).

The C p-p diagonal entries are `x_i x_j` for `i!=j`, and `x_i^2/4` for `i=j`. Its only further p-p entries are the reverse-pair off-diagonals `x_i x_j/4` for `i!=j`.

The p-q entries simplify to

```
Cbar_(p(i,j),q(a,b))
=-(x_a x_b/2)[delta_ib delta_ja+delta_ia delta_jb],

Sbar_(p(i,j),q(a,b))
=-[x_i x_a x_b tau_i^(ab)/(2d_ab)]
  [delta_ja+delta_jb].                       (13.4)
```

For q-q, the C diagonal is `x_a x_b`, the reverse C entry is `x_a x_b/4`, the S diagonal is zero, and the reverse S entry is `x_a x_b E_ab`. For distinct `a,b,t`, the nonzero chain entries are

```
Sbar_(q(a,b),q(b,t))=x_a x_b x_t/(4d_at),
Sbar_(q(a,b),q(t,a))=x_a x_b x_t/(4d_bt).
```

These specify all entries together with symmetric counterparts. Hence the entire zero-charge table is rational in the four probabilities.

The actual lower reference block, in the constant-column reference basis just described, is

```
4diag(x_i d_i)+x x^T>0                      (13.5)
```

on the interior. This follows by congruencing the old `4G^(-1)` reference block by `diag(c)`. It is not omitted or replaced by deleting four coordinates. The equality (13.5) is for that reference block, not for the whole lower form.

## 4. A rational nine-plus-three chart for the p quotient

Write the physical p coefficient matrix as

```
Z=diag(c) U diag(c).
```

The physical reference-orthogonality condition `c^T Z=0` becomes

```
x^T U=0.                                    (13.6)
```

Every U satisfying (13.6) has the unique decomposition

```
U=V+(Vx)1^T-1(Vx)^T+K,
V^T=V, x^T Vx=0,
K^T=-K, Kx=0.                               (13.7)
```

Indeed `V=(U+U^T)/2`. If `J=(U-U^T)/2`, condition (13.6) gives `Jx=Vx` and `x^T Vx=0`; subtracting `(Vx)1^T-1(Vx)^T` leaves exactly a skew K with `Kx=0`, since `1^T x=1`.

The symmetric V space has dimension nine. A single interior rational chart takes its three diagonal entries `V_11,V_22,V_33` and six off-diagonals freely and sets

```
V_44=-[sum_(i=1..3)x_i^2 V_ii
       +2sum_(1<=i<j<=4)x_i x_j V_ij]/x_4^2.
```

This denominator is positive on the full interior. The skew K space has dimension three, with the rational parametrization

```
K=star(x wedge z), sum_i z_i=0.
```

Choose `z=e_1-e_4,e_2-e_4,e_3-e_4` for a basis. The only kernel of `z -> star(x wedge z)` is `span{x}`, which does not meet `sum z_i=0` except at zero because `sum x_i=1`.

After physical congruence this K space is exactly the skew subspace of checkpoint 010: `diag(c)Kdiag(c)` is skew and annihilates c. Thus checkpoint 010's proven-positive **physical** K pivots apply, with their actual coordinate Gram matrices, and give a rational exact Schur form on the nine V coordinates in (13.7). The same statement holds for each sign with its own preceding q and reference operations. No common upper/lower Schur matrix is presumed.

Equations (13.3)-(13.7) therefore provide a square-root-free specification of both still-unproved nine-dimensional residuals. This is not a numerical implementation, a determinant evaluation, or a positive coefficient certificate.

## 5. Literal frontier and a source-status caution

The unproved universal-reference forms remain:

1. upper nonzero-charge seven-dimensional residual;
2. lower nonzero-charge five-dimensional residual from checkpoint 012;
3. both zero-charge nine-dimensional residuals, now with the explicit rational chart above.

All are over the entire positive probability simplex, with the stated physical continuity extension required for a full closed-simplex proof. No smaller paired spectrum or neighborhood replaces that obligation.

The complete statement of Fraser-Huber-Pozsgay-Vona's primary Theorem A was also reread at <https://arxiv.org/pdf/2607.24309> (arXiv:2607.24309v1): it is an all-rank two-factor partial-trace inequality, with rank-at-most-r and no normality assumption. It supplies no automatic complete-copositivity conclusion for these conditional remainders. Its published/imported two-copy scope is not being relabeled as the present three-copy advance. No unread source corollary or novelty-absence claim is inferred from that bounded reread.

No full all-reference theorem, unrestricted W4 theorem, exact route failure, admissible rank-two negative Werner witness, novelty certification, independent acceptance, or kernel proof is claimed. The pending four-polynomial request remains author-requested HOLD; no new execution is proposed or presumed by this representation.
