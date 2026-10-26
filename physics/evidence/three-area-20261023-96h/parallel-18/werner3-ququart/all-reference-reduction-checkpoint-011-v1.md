# All-reference working checkpoint 011: unitary ordinary Choi matrix and a strict lower skew pivot

Before-writing clock observed: `2026-10-23T17:57:02-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written algebra**. No scientific execution, numerical evaluation, import, compilation, solver, independent model CLI, or proof assistant was used. This is another working leaf of the same unfinished all-reference W4 route.

**Delta:** the special local dimension four makes the ordinary Choi matrix of `B=Lambda tensor Lambda` a Hermitian unitary. This gives an explicit isometric Kraus-space representation of the conditional CP map and a uniform bound on its input marginal perpendicular to the reference. A general antisymmetric-tensor estimate then proves a positive lower pivot on five dimensions of every nonzero-charge block. The exact lower residual there becomes **six-dimensional**, rather than seven-dimensional. The corresponding upper pivot is not proved by this argument.

## 1. Conventions and the ordinary/co-Choi distinction

Keep `Lambda(X)=Tr(X)I-X/2` on `M_4`, and `B=Lambda tensor Lambda` on `M_16`. The normalized Schmidt reference is

```
eta=sum_i c_i |i,i>, c_i>=0, sum_i c_i^2=1,
P=|eta><eta|, Q=I-P,
Rho1=diag(c_i^2) tensor I,
Rho2=I tensor diag(c_i^2), H=Rho1+Rho2.
```

All matrix entries are real in this Schmidt coordinate system; vector tests remain complex. Define

```
A=B(P)=I-H/2+P/4,
L_i=B(|i><eta|),
M_eta(E_ij)=L_i A^(-1)L_j^dagger.
```

For a map `E`, the **ordinary** Choi convention is

```
J(E)=sum_ij E_ij tensor E(E_ij).
```

The reversed-input co-Choi convention in the W4 route is `Jhat(E)=J(E)^Gamma`, with partial transpose on the entire sixteen-dimensional input. Thus `C_B=Jhat(B)` and `S_eta=Jhat(M_eta)`. An ordinary Choi identity is not by itself a complete-copositivity conclusion.

## 2. The dimension-four reflection and the exact Kraus-space representation

Let `Omega_4=sum_i |i,i>` be unnormalized. The one-site ordinary Choi matrix is

```
U4=I-|Omega_4><Omega_4|/2.
```

Because `(|Omega_4><Omega_4|)^2=4|Omega_4><Omega_4|`, one has `U4^2=I` and `U4^dagger=U4`. Consequently

```
U=J(B)=(I-P_Omega,13/2)(I-P_Omega,24/2)
```

is a real Hermitian unitary on input/output space. The factors commute because they act on disjoint pairs. Its partial transpose is the already used

```
U^Gamma=C_B=(I-F_13/2)(I-F_24/2)>0.
```

For an auxiliary output vector v, define the matrix `T_v` by its input columns

```
T_v |i>=L_i v.
```

With column vectorization `|T_v>>=sum_i |i>_input tensor T_v|i>_output`, expansion of the two local reflections gives

```
|T_v>>=U(|eta>_input tensor |v>_output).      (11.1)
```

This identity holds for entangled eta and v, not only product vectors. In explicit Schmidt coordinates, if `V=(v_ab)` and `C=diag(c_i)`, its matrix form is

```
T_v=|v><eta|-(V C tensor I+I tensor V^T C)/2
    +Tr(CV) I/4.
```

The right side is obtained directly by expanding both Bell-projector factors, so the transpose and tensor order are fixed. Since U is unitary and eta is normalized, `v -> |T_v>>` is an isometry. Equivalently,

```
sum_i L_i^dagger L_i=I_16.
```

Taking real Kraus vectors `v_alpha=A^(-1/2)e_alpha` gives the exact ordinary Choi identity

```
J(M_eta)=U(P tensor A^(-1))U.                (11.2)
```

In particular its nonzero eigenvalues equal those of `A^(-1)`, and `Tr J(M_eta)=Tr A^(-1)`. These are exact identities, not eigenvalue assays.

The input compression of U on eta is A:

```
(<eta| tensor I)U(|eta> tensor I)=A.
```

Therefore `||A||<=1`; its positivity and lower bound are proved next. No global positivity of U is asserted: U has negative eigenspaces.

## 3. A regular inverse inequality for every reference

Let `Red(X)=Tr(X)I-X`. Its reversed-input Choi matrix is `I-F>=0`, so `Red tensor Red` is completely copositive and hence positive. Applied to P, this yields

```
I-H+P>=0.                                  (11.3)
```

Thus

```
A-(I/2-P/4)=(I-H+P)/2>=0,
A>=I/2-P/4>=I/4.
```

Together with the compression norm bound in Section 2,

```
I/4<=A<=I,
A^(-1)<=2I+2P.                             (11.4)
```

The inverse inequality uses the inverse of `I/2-P/4`, which is `2I+2P`. It contains no vanishing Schmidt-coordinate denominators and includes every zero or repeated Schmidt amplitude.

## 4. Input-marginal bound on eta-perpendicular vectors

Define the CP, trace-preserving map

```
E_eta(X)=Tr_output[U(P tensor X)U].
```

Equation (11.2) gives `E_eta(A^(-1))=(M_eta^*(I))^T`. All matrices here are real and Hermitian, so write this marginal as `X_eta=M_eta^*(I)`.

Two direct partial-trace identities will suffice. For one local reflection, tracing the output of `U4(rho tensor I)U4` gives `3rho+Tr(rho)I/4`. Applying this local identity twice to the possibly entangled input P proves

```
E_eta(I)=9P+3H/4+I/16.                      (11.5)
```

For the second identity take `v=eta` in (11.1). The matrix `T_eta` is real symmetric and equals

```
T_eta=P-H/2+I/4=A-3Q/4.
```

Its input marginal is therefore

```
E_eta(P)=T_eta^2.                            (11.6)
```

Positivity of E and (11.4) give

```
X_eta<=2E_eta(I)+2E_eta(P).
```

Compress to `eta^perp`. Equation (11.3) gives `Q H Q<=Q`; also

```
Q T_eta^2 Q=Q(A-3I/4)^2 Q<=Q/4,
```

because `spec(A)` lies in `[1/4,1]`. Substituting (11.5)-(11.6) now gives the uniform estimate

```
Q X_eta Q
<=2(3Q/4+Q/16)+2(Q/4)
=(17/8)Q.                                  (11.7)
```

The large P term in (11.5) vanishes only because this is a genuine Q compression. No claim `X_eta<=17I/8` on the entire input space is made.

## 5. General antisymmetric-tensor estimate for a CP map

This step is an elementary Kraus inequality, not a Werner-specific imported theorem. Let `M(X)=sum_alpha K_alpha X K_alpha^dagger`, put `X0=sum_alpha K_alpha^dagger K_alpha=M^*(I)`, and let F exchange the entire input/output spaces of the same dimension. Its reversed-input Choi matrix is

```
S=sum_alpha (K_alpha^dagger tensor K_alpha)F.
```

For an antisymmetric vector psi with `F psi=-psi`, the two expectations of `K^dagger tensor K` and `K tensor K^dagger` agree by conjugating with F. Furthermore

```
-(K^dagger K tensor I+I tensor K^dagger K)
<=K^dagger tensor K+K tensor K^dagger
<=K^dagger K tensor I+I tensor K^dagger K,
```

by expanding `(K tensor I +/- I tensor K)^dagger(K tensor I +/- I tensor K)>=0`. Summing gives, on antisymmetric vectors,

```
-(1/2)(X0 tensor I+I tensor X0)
<=S<= (1/2)(X0 tensor I+I tensor X0),         (11.8)
```

where the inequalities mean compressed quadratic forms on that subspace.

Now restrict to

```
A_skew = wedge^2(eta^perp).
```

Both tensor factors then lie in Q. For `M=M_eta`, equation (11.7) and (11.8) show

```
-(17/8)I<=S_eta|A_skew<=(17/8)I.             (11.9)
```

This is **not** strong enough to prove the required upper form, since `C_B` equals only `3I/4` there. Its role is the lower form.

## 6. Strict lower pivot and the reference subtraction

Write `F_global=F_13 F_24`. On its antisymmetric eigenspace the two commuting local swaps have opposite signs, so

```
C_B|wedge^2(C^16)=(3/4)I.
```

Combining with (11.9) gives

```
(3C_B+S_eta)|A_skew >=(1/8)I.               (11.10)
```

This remains true after the required lower reference Schur operation. Here are the explicit reasons, rather than an instruction to discard a reference direction.

The ordinary Choi remainder from (11.2) is

```
J(B-M_eta)=U-U(P tensor A^(-1))U.
```

Its rows and columns on `P_input tensor I_output` vanish because the compression of U there is A. Partial transpose on the input preserves this zero-row/column property for the real projector P. Hence `D=C_B-S_eta` annihilates every `eta_input tensor z_output`.

Every vector in `A_skew` is orthogonal to that reference subspace. Since C acts on such a vector as `3/4` times the vector, its C pairing with the reference subspace also vanishes. As `3C+S=4C-D`, the lower reference pairing with `A_skew` is zero. Therefore the actual positive reference-block Schur subtraction does not change the principal form (11.10). It still changes other blocks and cannot be deleted globally.

## 7. Consequence in a nonzero-charge twelve-dimensional block

Use the full physical table and coordinates in checkpoint 004 (SHA256 `98e0d5f820e1b9aeabe9b88410afc6c3d1771feaffb2dfa7fe1798812c649d72`):

```
Q_i=|i,i,a,b>, P_i=|a,b,i,i>, i=1,...,4,
R_j=|a,j,j,b>, T_j=|j,b,a,j>, j outside {a,b}.
```

Within this block, global antisymmetric vectors are

```
sum_i u_i(Q_i-P_i)/sqrt(2)
+sum_(j outside {a,b}) v_j(R_j-T_j)/sqrt(2).
```

The additional condition `c^T u=0` is precisely orthogonality to the block's reference vector `sum_i c_i Q_i`. Antisymmetry then gives orthogonality in the other tensor factor too, so these vectors lie in `A_skew`. Their dimension is `3+2=5`.

The lower form has its true positive reference block `4d_ab`. Eliminate that block first. On the displayed five-dimensional subspace its principal form is still at least `I/8`, by Section 6. Its exact Schur elimination, retaining all cross terms with the complement, leaves a **six-dimensional** form out of the remaining eleven dimensions.

Thus full lower positivity of each nonzero-charge twelve-dimensional block is equivalent to positivity of this new six-dimensional Schur residual. That residual's sign is unproved here. The earlier R/T-first lower seven-dimensional representation remains preserved, but this is a different legitimate pivot order, not an identification of its entries with the new form.

For the **upper** form (11.9) gives no positive pivot on these five dimensions. Its earlier seven-dimensional residual remains the active upper obligation.

## 8. Classical peeling source boundary

During this written work the following primary source was read: Yu Yang, Denny H. Leung, Wai-Shing Tang, *All 2-positive linear maps from M3 to M3 are decomposable*, arXiv:1603.03534v1, posted 11 March 2016:

- <https://arxiv.org/abs/1603.03534>
- <https://arxiv.org/pdf/1603.03534>
- <https://arxiv.org/html/1603.03534>

Actual read scope includes the definitions, Theorem 2.7 and its full block-matrix proof, Corollary 2.10, Theorem 2.11, Example 2.12, and Theorem 3.2. The PDF retrieval returned through page 9; no full-paper absence claim is made about unread later sections. The ordinary CP peeling and zero reference row/column are classical, **not a novelty claim** here. Theorem 2.7 guarantees a `(k-1)`-positive trivial-lifting remainder after peeling a k-positive map; for k=2 that is only positivity, not the complete copositivity still sought here. Theorem 3.2 is specifically `M3 -> M3`, not this `M16 -> M16` situation.

The HTML rendering's displayed 2026 typesetting date is not being treated as a new release; the arXiv v1 header is 2016. A separate broad exact-phrase search for a unitary-Choi/2-positive result returned no directly applicable theorem in the inspected hits, which is not evidence of novelty or nonexistence. No imported peeling statement supplies the missing upper or lower residual signs.

## 9. Literal frontier and status

At this working-candidate boundary the all-reference route still has:

1. the **seven-dimensional upper** nonzero-charge residual;
2. the **six-dimensional lower** nonzero-charge residual in Section 7;
3. **both nine-dimensional zero-charge residuals** from checkpoint 010 (SHA256 `987e2964ded5422944a39095b6112598496a91a44ac06e44afbf7afbc93374f4`).

The full four-dimensional phase blocks retain checkpoint 009's hand closure. Every reference is still quantified, including zeros and repeated amplitudes. No complete universal-reference theorem, full W4 proof, exact negative route direction, exact rank-two Werner witness, novelty certification, separate mathematical acceptance, or kernel proof is claimed.
