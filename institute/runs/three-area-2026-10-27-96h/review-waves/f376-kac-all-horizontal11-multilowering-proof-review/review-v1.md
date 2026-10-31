# f376 — Complete written review of Theorem B

**Disposition: SUPPORTED at the named displayed full-Cartan/f276/f306/f314 boundary.**

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

Theorem B reconstructs for **every positive integer \(r,s\)** and **every \(n\ge2\)**. This includes zero and negative \(h_3\)-weight, both complete positive seed modules, their whole ideal, the active \(n=2\) inverse-Gram contribution, and the author-supplied \((r,s,n)=(3,7,8)\) component. The proof does not require diagonalizability of \(\overline A_n\), a positive invariant form on the full nonsymmetrizable algebra, or directness of the two positive-seed contributions.

This is a complete direct-return body for parent materialization. **No repository review or process file was written.** The read-only role was not bypassed.

## 1. Binding, coverage, and exact scope

Run root:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`

Wave:

`review-waves/f376-kac-all-horizontal11-multilowering-proof-review/`

Bindings supplied by the frozen records and confirmed by the parent’s live metadata:

- Manifest SHA256: `bfec0a442f143f27d4eda6950b56dc4051b728455c5971a16e2e2fb884d57e1d`
- Freeze receipt SHA256: `6d7a793d143982d18c56fc1a88cc03c3c1275d751e976349ca538e72cf9779cf`
- Literal packet SHA256: `eac70fa9260600f89153dbc413b856df9c8eaa1de1be4ad5e51c0a1303bc67a8`

These are **parent-supplied bindings**, not child-executed hash checks.

The complete ordered packet, **LF1–1389**, was read raw in consecutively numbered windows of at most 20 LF before mathematical reconstruction. Coverage includes the complete S1 logical ending at line 790, complete S3 logical ending at line 457, and final S5 line 74. No packet elision remained unrecovered.

| Label | Frozen source relative to run root | SHA256 | Complete source coverage |
|---|---|---|---|
| S1 | `review-waves/f364-kac-next-serre-gap-multilowering-frontier/review-v1.md` | `af51a0025d41ddd0a62fd42b1be8b7f65d69601d253455ff0f8717fd26fa9d01` | Logical lines 1–790; 789 LF |
| S2 | `dispositions/math-3-upper-serre-gap-no-cancellation-and-actual-quotient-spectrum-parent-v1.md` | `7f95403e09074983f4d8326214c6ed1a3f6ea0c91ff91bc120b291bba639d3be` | Lines 1–39 |
| S3 | `review-waves/f359-kac-upper-serre-gap-no-cancellation-proof-review/review-v1.md` | `9cd74983dec5dd52b5940f92dc8be06611e210badf0fe71b6d19f1e8c391ebff` | Logical lines 1–457; 456 LF |
| S4 | `dispositions/math-3-actual-free-source-and-full-serre-ideal-at-displayed-presentation-parent-v1.md` | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` | Lines 1–27 |
| S5 | `written-releases/math-3-serre-family-definitions-v1.md` | `b415be711bf075210e2154db9812b024cb2282dfd38c3ae2fd9fb97315234030` | Lines 1–74 |

The scientific disposition here concerns **Theorem B**, its horizontal-\((1,1)\) consequences, and its supplied illustration. Reading the complete S1 does not constitute a separate disposition of Theorem A.

### Exact retained imports

1. **Displayed presentation and full Cartan.** S5 lines 16–38 and 66–70 specify the row-Cartan convention, full complex realization, and quotient by all positive and negative Serres. S4 lines 3, 7, 15, and 19 retain Cartan injection and root-character separation, including additional Cartan directions at singular parameters.

2. **Actual positive source and whole ideal.** S4 lines 7–10 and 19 supply
   \[
   \mathfrak n_+(T)=\mathfrak n_+^{\mathrm{Levi}}\ltimes L(V),
   \qquad T_n=L_n(V)\quad(n>0),
   \]
   the two complete lowest-seed Levi modules, their whole positive ideal, and
   \[
   J/K=P_+\oplus P_-
   \]
   with disjoint positive and negative support. This last statement—not positive degree counting alone—excludes extra positive relations from negative Serres.

3. **Actual contraction normalization.** S1 lines 156–165, 183–220 and S3 lines 114–139 retain the named f306 actual theta-dual/inverse-Gram/descended-bracket interface. The underlying f306 manuscripts were not newly opened or independently reconstructed in this assignment.

4. **Generalized-zero-primary quotient interface.** S1 lines 156–165 and S3 lines 168–198 retain the named f314 identification
   \[
   E_0(\overline A_n|S_\alpha)
   \cong E_{n,\alpha}/\operatorname{im}(e_n\Phi_n)_\alpha,
   \]
   where \(\Phi_n\) spans the whole two-seed ideal and \(E_{n,\alpha}\) is the full free-source generalized zero-primary space.

5. **Ordinary free-Lie construction.** The characteristic-zero free-Lie tensor embedding is the named classical import in S4. No preliminary-\(G_{\mathcal C}\) positive-freeness or PBW theorem is substituted for it.

The source/full-ideal and contraction bridges remain exact-scope imports. This review does not newly authenticate the original book/source chain or independently reprove their underlying manuscripts. S2’s reported finite execution and linked certificates are not premises of the proof below and were not opened.

## 2. Whole-two-seed quotient basis for every \(n\) — SUPPORTED

**Candidate references: S1 lines 307–378. Supporting interface: S3 lines 206–301; S4 lines 7–10 and 19.**

Set
\[
t_0=e_3,\qquad
X_i=(\operatorname{ad}t_0)^ie_1,\qquad
Y_j=(\operatorname{ad}t_0)^je_2.
\]

Let \(F\) be the ordinary free Lie algebra on \(t_0,e_1,e_2\). Its elimination presentation is
\[
F\cong
\mathbb Ct_0\ltimes
\operatorname{Lie}\langle X_i,Y_j:i,j\ge0\rangle,
\]
with derivation
\[
DX_i=X_{i+1},\qquad DY_j=Y_{j+1}.
\]

Indeed, the homomorphism sending each eliminated letter to its indicated iterated adjoint, and the reverse homomorphism fixing \(t_0,X_0,Y_0\), are inverse on the generators.

Horizontal bidegree \((1,1)\) contains exactly one \(X\)-letter and one \(Y\)-letter. Hence
\[
F_{(1,1,n)}
=\operatorname{span}\{Z_{i,j}=[X_i,Y_j]:i+j=n\},
\]
with these \(n+1\) vectors independent by the ordinary free-Lie embedding.

### Matching the actual source

This free presentation is not asserted to equal the actual positive source globally. On the component in question, the comparison is nevertheless an isomorphism.

Eliminating \(u_0\) in the imported actual \(L(V)\), the entire charge-\((1,1)\), level-\(n\) roster is:

- \((\operatorname{ad}u_0)^{n-1}u_3\);
- \((\operatorname{ad}u_0)^{n-1}u_4\);
- the brackets
  \[
  [(\operatorname{ad}u_0)^pu_1,
    (\operatorname{ad}u_0)^qu_2],
  \qquad p+q=n-2.
  \]

For \(n\ge2\), there are \(2+(n-1)=n+1\) independent vectors. At \(n=1\), the first two give dimension two. At \(n=0\), both sources have the one-dimensional Levi component generated by \([e_1,e_2]\).

Thus the natural surjection
\[
\pi:F\longrightarrow\mathfrak n_+(T)
\]
has
\[
(\ker\pi)_{(1,1,n)}=0
\]
for every relevant \(n\).

### Imposing both complete seed modules

Let \(H\) be the ideal of \(F\) generated by
\[
X_{r+1},\qquad Y_{s+1}.
\]

At the named source boundary, these raw seeds are lowest vectors for the finite Levi action. Their complete cyclic modules are spanned by positive Levi raising words. Therefore the positive ideal generated by the raw seeds contains both complete modules. Conversely, the \(L(V)\)-ideal generated by the complete modules is positive-Levi stable and contains the raw seeds. Consequently,
\[
\pi(H)=I,\qquad \pi^{-1}(I)=H+\ker\pi.
\]

The component comparison gives
\[
S_{(1,1,n)}
\cong F_{(1,1,n)}/H_{(1,1,n)}.
\]

In the eliminated alphabet, \(H\) is precisely the derivation-stable ideal generated by
\[
X_i\quad(i>r),\qquad Y_j\quad(j>s).
\]
Repeated \(t_0\)-adjoints produce every invalid letter from the two raw seeds. Conversely, the ideal of those invalid letters is shift-stable and contains both raw seeds.

The quotient of this eliminated free Lie algebra is therefore free on the surviving letters, with truncated shift. It introduces no relation among brackets of surviving letters. This yields the actual quotient basis
\[
\boxed{
Z_{i,j},\qquad
0\le i\le r,\quad0\le j\le s,\quad i+j=n.
}
\]

Equivalently, with \(z_i=Z_{i,n-i}\),
\[
\boxed{
\max(0,n-s)\le i\le\min(r,n).
}
\]

For \(2\le n\le r+s\),
\[
\dim S_{(1,1,n)}
=\min(r,n)-\max(0,n-s)+1.
\]
For \(n>r+s\), the component is zero.

Both seed ideals and their overlap have been imposed simultaneously. No subtraction of separate seed ranks or directness assumption is used. Exclusion of additional negative-Serre consequences is specifically conditional on the named full-ideal import.

## 3. Actual lowerings and all consuming targets — SUPPORTED

**Candidate references: S1 lines 388–504.**

All operators below are actual adjoint operators on \(S\). They are not artificially extended endomorphisms of a positive free Lie algebra.

Write
\[
E=E_3,\qquad F=F_3.
\]
Since \(X_0,Y_0\) have respective \(h_3\)-weights \(-r,-s\), the actual \(\mathfrak{sl}_2\) commutator identities give
\[
EX_i=X_{i+1},\qquad FX_i=i(r-i+1)X_{i-1},
\]
\[
EY_j=Y_{j+1},\qquad FY_j=j(s-j+1)Y_{j-1}.
\]
The endpoint conventions agree with the actual Serre truncations.

For the finite-node lowerings,
\[
F_1X_0=-h_1,\quad F_1X_1=-e_3,\quad
F_1X_i=0\ (i\ge2),\quad F_1Y_j=0,
\]
and
\[
F_2Y_0=-h_2,\quad F_2Y_1=-e_3,\quad
F_2Y_j=0\ (j\ge2),\quad F_2X_i=0.
\]

Because \(Y_j\) has \(h_1\)-weight \(-j-1\), and \(X_i\) has \(h_2\)-weight \(-i-1\), derivation gives
\[
F_1Z_{i,j}=
\begin{cases}
(j+1)Y_j,&i=0,\\
-Y_{j+1},&i=1,\\
0,&i\ge2,
\end{cases}
\]
\[
F_2Z_{i,j}=
\begin{cases}
-(i+1)X_i,&j=0,\\
X_{i+1},&j=1,\\
0,&j\ge2.
\end{cases}
\]

### Commutator order and coefficient tables

Retaining the named actual-dual convention,
\[
W_0=F_3,\qquad
W_1=[F_3,F_1],\qquad
W_2=[F_3,F_2].
\]
In particular, changing \(W_1\) to \([F_1,F_3]\), or \(W_2\) to \([F_2,F_3]\), would reverse the needed signs.

Direct expansion gives
\[
\boxed{
W_1Z_{i,j}=
\begin{cases}
j(s-j+1)Y_{j-1},&i=0,\\
[2j-s-r(j+1)]Y_j,&i=1,\\
2(r-1)Y_{j+1},&i=2,\\
0,&i\ge3,
\end{cases}}
\]
and
\[
\boxed{
W_2Z_{i,j}=
\begin{cases}
-i(r-i+1)X_{i-1},&j=0,\\
[r+s(i+1)-2i]X_i,&j=1,\\
-2(s-1)X_{i+1},&j=2,\\
0,&j\ge3.
\end{cases}}
\]

For example, the \(i=1\) coefficient in \(W_1\) is
\[
-(j+1)(s-j)-r(j+1)+j(s-j+1)
=2j-s-r(j+1),
\]
which checks the sign and both parameter contributions.

### Complete target audit

For \(n\ge2\):

| Operator | Actual target |
|---|---|
| \(W_0\) | \(S_{(1,1,n-1)}\) |
| \(W_1\) | \(S_{(0,1,n-1)}=\mathbb CY_{n-1}\) if \(n-1\le s\), otherwise zero |
| \(W_2\) | \(S_{(1,0,n-1)}=\mathbb CX_{n-1}\) if \(n-1\le r\), otherwise zero |
| \(W_3,W_4\) | \(S_{(0,0,n-1)}\): \(\mathbb Ce_3\) at \(n=2\), zero for \(n\ge3\) |
| \(W_5,W_6,W_7\) | Mixed-sign root degrees, hence zero |

Thus no higher-charge term is silently discarded. The pure-simple target of \(W_3,W_4\) is exactly why \(n=2\) requires separate treatment.

For \(n\ge3\), the entire descended inverse-Gram sum is
\[
\overline A_n
=E_3F_3+\operatorname{ad}(u_1)W_1+
                 \operatorname{ad}(u_2)W_2.
\]

Here
\[
u_1=-X_1,\qquad u_2=-Y_1.
\]
The consuming bracket map therefore sends
\[
[u_1,Y_{n-1}]=-z_1,\qquad
[u_2,X_{n-1}]=z_{n-1}.
\]

Set
\[
a_i=i(r-i+1),\qquad
b_i=(n-i)(s-n+i+1),\qquad B=E_3F_3.
\]
Then
\[
Bz_i=a_iz_{i-1}+(a_i+b_i)z_i+b_iz_{i+1}.
\]

Writing
\[
W_1z_i=\ell_iY_{n-1},\qquad
W_2z_i=\kappa_iX_{n-1},
\]
the only potentially nonzero coefficients are
\[
\ell_0=n(s-n+1),\quad
\ell_1=2n-2-s-rn,\quad
\ell_2=2(r-1),
\]
\[
\kappa_n=-n(r-n+1),\quad
\kappa_{n-1}=r+sn-2n+2,\quad
\kappa_{n-2}=-2(s-1).
\]

Consequently,
\[
\boxed{
\overline A_nz_i=Bz_i-\ell_i z_1+\kappa_i z_{n-1}.
}
\]
Only existing quotient coordinates are used.

## 4. Diagonal-only rows and their positivity — SUPPORTED

**Candidate references: S1 lines 506–525.**

Use the matrix convention that the \(i\)-th column is the image of \(z_i\).

For \(n\ge3\), the marked indices \(1\) and \(n-1\) are distinct.

### Row \(1\)

The vector \(z_1\) exists exactly when \(n\le s+1\). Its only possible off-diagonal entries from \(B\) are:

- column \(0\): \(B_{1,0}=n(s-n+1)=\ell_0\);
- column \(2\): \(B_{1,2}=2(r-1)=\ell_2\).

The correction \(-\ell_i z_1\) cancels both. The surviving diagonal is
\[
\boxed{
\lambda_1=(n+1)r+n(s-n+1).
}
\]
Its existence condition gives \(s-n+1\ge0\), so \(\lambda_1>0\).

### Row \(n-1\)

This row exists exactly when \(n\le r+1\). Its only possible off-diagonal entries are:

- column \(n\): \(n(r-n+1)\), cancelled by \(\kappa_n\);
- column \(n-2\): \(2(s-1)\), cancelled by \(\kappa_{n-2}\).

The surviving diagonal is
\[
\boxed{
\lambda_2=(n+1)s+n(r-n+1)>0.
}
\]

The cancellations remain valid at omitted endpoints: absent rows or columns are not added to the quotient, and the relevant boundary coefficients vanish where appropriate.

These are cancellations of entries inside the derived operator. They do not exhibit a bracket-cancellation tensor.

## 5. Auxiliary metric, exact \(EF\)-kernel, and principal block — SUPPORTED

**Candidate references: S1 lines 527–583.**

Give the actual string-sector basis the positive diagonal Hermitian metric
\[
\boxed{
\|Z_{i,j}\|^2
=\frac{i!\,r!}{(r-i)!}\,
 \frac{j!\,s!}{(s-j)!},
}
\]
with distinct pairs orthogonal.

All factorials are defined on the surviving index rectangle. The norm ratios are
\[
\frac{\|Z_{i+1,j}\|^2}{\|Z_{i,j}\|^2}
=(i+1)(r-i),
\]
\[
\frac{\|Z_{i,j+1}\|^2}{\|Z_{i,j}\|^2}
=(j+1)(s-j).
\]
These are exactly the reverse coefficients in \(F_3\). Across adjacent sector levels,
\[
E_3^*=F_3,\qquad
B=E_3F_3=F_3^*F_3\ge0.
\]

This is an explicitly constructed metric on this sector. It is not asserted to be an invariant positive form for the whole algebra.

### Exact kernel

Assume \(r\le s\); exchanging the two arms handles the other orientation.

If \(n\le r\), the equation
\[
F_3\sum_i c_i z_i=0
\]
is precisely
\[
(i+1)(r-i)c_{i+1}
+(n-i)(s-n+i+1)c_i=0,
\qquad 0\le i\le n-1.
\]
Every multiplier displayed is positive. Hence the solution space has dimension one, and every nonzero solution has every coordinate nonzero. Explicitly,
\[
c_i=(-1)^i\binom ni
\frac{(s-n+i)!}{(s-n)!}
\frac{(r-i)!}{r!}\,c_0.
\]

If \(r<n\le s\), the rightmost target coordinate has coefficient
\[
(n-r)(s-n+r+1)c_r.
\]
Its positive multiplier forces \(c_r=0\), and the remaining recurrence forces every coefficient to vanish.

If \(s<n\le r+s\), put \(L=n-s>0\). The leftmost target coordinate has coefficient
\[
L(r-L+1)c_L.
\]
Again its multiplier is positive, and the recurrence forces every coefficient to vanish.

Thus, on nonzero components,
\[
\boxed{
\dim\ker B=\dim\ker F_3=
\begin{cases}
1,&n\le\min(r,s),\\
0,&n>\min(r,s).
\end{cases}}
\]
In the one-dimensional-kernel case, a nonzero kernel vector has no zero coordinate.

### Remaining principal block

Let \(J_{\mathrm{mark}}\) be the existing members of \(\{1,n-1\}\), and let \(T\) be the remaining actual indices.

If \(n>\min(r,s)\), \(B\) is already positive definite.

If \(n\le\min(r,s)\), both marked indices exist. No nonzero vector in \(\ker B\) can be supported on \(T\), because every nonzero kernel vector has every coordinate nonzero.

For a vector supported on \(T\), its quadratic form under the weighted principal block \(B_{TT}\) equals its quadratic form under \(B\). Therefore
\[
\boxed{B_{TT}\text{ is positive definite}.}
\]
This includes the usual empty-block convention.

Ordering marked coordinates first gives the actual block-triangular matrix
\[
\boxed{
\overline A_n=
\begin{pmatrix}
\operatorname{diag}(\lambda_j:j\in J_{\mathrm{mark}})&0\\
C&B_{TT}
\end{pmatrix}.
}
\]

The marked diagonals are positive, and \(B_{TT}\) has positive real spectrum. The characteristic polynomial factors through these diagonal blocks. Consequently every eigenvalue of \(\overline A_n\) is positive real and \(\overline A_n\) is invertible.

This conclusion is valid without diagonalizing the full matrix. Repeated eigenvalues across blocks do not invalidate it.

## 6. Independent reconstruction of the full \(n=2\) block — SUPPORTED

**Candidate references: S1 lines 585–652.**

At \(n=2\), retain the ordered possible basis
\[
z_0=Z_{0,2},\qquad z_1=Z_{1,1},\qquad z_2=Z_{2,0}.
\]
The coordinate \(z_0\) is absent if \(s=1\); \(z_2\) is absent if \(r=1\).

The actual duals give
\[
w_3=[f_1,[f_2,f_3]],\qquad
W_3=W_2F_1-F_1W_2,
\]
\[
w_4=[f_2,[f_1,f_3]],\qquad
W_4=W_1F_2-F_2W_1.
\]
These signs follow directly from \(\operatorname{ad}[x,y]=[\operatorname{ad}x,\operatorname{ad}y]\) and the already fixed \(W_1,W_2\) order.

The preceding actual identities give
\[
W_2Y_2=2(s-1)e_3,\qquad
W_1X_2=2(r-1)e_3.
\]
Combining these with the \(F_1,F_2,W_1,W_2\) tables yields the entire scalar table:
\[
\boxed{
\begin{array}{c|ccc}
&z_0&z_1&z_2\\ \hline
W_3/e_3&4(s-1)&r&-2(r-1)\\
W_4/e_3&2(s-1)&-s&-4(r-1)
\end{array}}
\]

For example,
\[
W_3z_0
=W_2(3Y_2)-F_1(-2(s-1)X_1)
=4(s-1)e_3,
\]
and
\[
W_4z_1
=W_1X_2-F_2((2-s-2r)Y_1)
=-s\,e_3.
\]
The other entries follow from the same displayed actual identities.

The normalized positive letters satisfy
\[
u_3=-Z_{0,1},\qquad u_4=Z_{1,0}.
\]
Hence
\[
[u_3,e_3]=z_0+z_1,\qquad
[u_4,e_3]=-z_1-z_2.
\]

The complete charge-\((1,1)\) Gram block and inverse are
\[
G_{34}=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{34}^{-1}
=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
Therefore the entire mixed-charge contribution is
\[
H=
\frac13\left\{
\operatorname{ad}(u_3)(2W_3-W_4)
+\operatorname{ad}(u_4)(-W_3+2W_4)
\right\}.
\]

Substituting the table and consuming brackets gives
\[
H=
\begin{pmatrix}
2(s-1)&(2r+s)/3&0\\
2(s-1)&r+s&2(r-1)\\
0&(r+2s)/3&2(r-1)
\end{pmatrix}.
\]

Separately, the \(W_0,W_1,W_2\) contribution is
\[
D=
\begin{pmatrix}
2(s-1)&r&0\\
-2(s-1)&4(r+s)-4&-2(r-1)\\
0&s&2(r-1)
\end{pmatrix}.
\]

Adding the complete contributions gives exactly
\[
\boxed{
\overline A_2=D+H=
\begin{pmatrix}
4(s-1)&(5r+s)/3&0\\
0&5(r+s)-4&0\\
0&(r+5s)/3&4(r-1)
\end{pmatrix}.
}
\]

Absent endpoint rows **and columns** must be omitted. They do not represent zero eigenvalues. Every surviving diagonal is positive:

- \(5(r+s)-4\ge6\);
- \(4(s-1)>0\) whenever \(z_0\) exists;
- \(4(r-1)>0\) whenever \(z_2\) exists.

Ordering the central coordinate first makes this block triangular, proving invertibility and positive spectrum for every \(r,s\ge1\).

### Required \(r=s=1\) corner

Only \(z_1\) survives. Its contributions are:

- \(E_3F_3\): scalar \(2\);
- the \(W_1,W_2\) terms together: scalar \(2\);
- the full \(W_3,W_4\) inverse-Gram term: scalar \(2\).

Thus
\[
\boxed{\overline A_2=(6).}
\]

Dropping the mixed Gram block would give the incorrect scalar \(4\).

All calculations here take place in the actual quotient, where Cartan and level-zero targets are defined. No free-positive \(f_3\) endomorphism with an incorrect codomain is introduced.

## 7. Supplied \((3,7,8)\) component — SUPPORTED as a written claim

**Candidate references: S1 lines 675–730.**

This instance was prescribed by the manifest and supplied by the author; it was not independently selected by this reviewer.

For \(r=3,s=7,n=8\), the proved actual quotient basis is
\[
Z_{1,7},\quad Z_{2,6},\quad Z_{3,5}.
\]

The universal coefficients give
\[
(a_1,a_2,a_3)=(3,4,3),\qquad
(b_1,b_2,b_3)=(7,12,15),
\]
and therefore
\[
E_3F_3=
\begin{pmatrix}
10&4&0\\
7&16&3\\
0&12&18
\end{pmatrix}.
\]

The \(W_1\) coefficients are
\[
W_1Z_{1,7}=-17Y_7,\qquad
W_1Z_{2,6}=4Y_7,\qquad
W_1Z_{3,5}=0.
\]
Since \([u_1,Y_7]=-Z_{1,7}\),
\[
\operatorname{ad}(u_1)W_1=
\begin{pmatrix}
17&-4&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

This verifies an **actual nonzero correction**, not merely a surviving target. The \(W_2\) target would be \(X_7\), which is zero because \(r=3\); the other targets vanish as previously audited. Hence
\[
\boxed{
\overline A_8=
\begin{pmatrix}
27&0&0\\
7&16&3\\
0&12&18
\end{pmatrix}.
}
\]

Its characteristic polynomial is
\[
(x-27)\bigl((x-16)(x-18)-36\bigr)
=(x-27)(x^2-34x+252),
\]
with eigenvalues
\[
\boxed{27,\quad17+\sqrt{37},\quad17-\sqrt{37}.}
\]
All are positive.

Both raw seeds \(X_4,Y_8\), their complete Levi modules, and their whole ideal are included through the all-\(n\) quotient proof. This is written verification of the supplied component, **not** an executed finite certificate, whole-level-eight computation, or proof of global \(B_8=0\).

## 8. No cancellation and full generalized-zero absence — SUPPORTED

**Candidate references: S1 lines 104–124 and 732–764. Named interface: S1 lines 156–165; S3 lines 168–198.**

The preceding arguments prove invertibility of
\[
\overline A_n=\overline\mu_n\overline{\mathcal C}_n
\]
on every \(S_{(1,1,n)}\), \(n\ge2\), including the zero-space cases.

If \(\overline{\mathcal C}_nx=0\), then \(\overline A_nx=0\), so \(x=0\). Therefore
\[
\boxed{\ker\overline{\mathcal C}_n=0}
\]
on this class.

If
\[
y=\overline{\mathcal C}_nx,\qquad \overline\mu_ny=0,
\]
then \(\overline A_nx=0\), so \(x=y=0\). Thus
\[
\boxed{
\operatorname{im}\overline{\mathcal C}_n
\cap\ker\overline\mu_n=0.
}
\]

Invertibility also gives
\[
\boxed{\ker\overline A_n^{\,k}=0\qquad(k\ge1).}
\]
Accordingly, the entire quotient generalized zero-primary space vanishes, not just its ordinary kernel.

At the retained f314 interface,
\[
E_0(\overline A_n|S_\alpha)
\cong
E_{n,\alpha}/\operatorname{im}(e_n\Phi_n)_\alpha,
\]
this yields
\[
\boxed{
\operatorname{im}(e_n\Phi_n)_\alpha=E_{n,\alpha},
\qquad \alpha=(1,1,n),\ n\ge2.
}
\]

This uses the whole two-seed ideal and the full generalized zero-primary space. It neither replaces generalized primary by ordinary kernel nor assumes the two seed images are disjoint.

If all three original \(F_1,F_2,F_3\) kill \(x\), every iterated negative-generator commutator \(W_j\) kills \(x\). Thus \(\overline{\mathcal C}_nx=0\), and \(x=0\) in the reviewed class.

Conversely, \(F_3\) alone does have the one-dimensional kernel proved above when \(n\le\min(r,s)\). Such vectors cannot be coevaluation-singular. The distinctions among \(F_3\)-singularity, simultaneous original-lowering singularity, bracket cancellation, and generalized zero-primary obstruction are preserved.

## 9. Per-claim disposition

| Claim | Verdict | Exact source LF / reconstruction |
|---|---|---|
| Full row-Cartan convention, including singular realizations | **SUPPORTED**, at the displayed-presentation boundary | S5 16–38, 66–70; S4 3, 7, 15, 19 |
| Actual source comparison for every horizontal-\((1,1)\) level | **SUPPORTED**, at the named f276 boundary | S1 311–347; §2 above |
| Both complete seed modules and the entire mixed ideal are imposed | **SUPPORTED** | S1 349–378; S3 244–301; S4 9–10 |
| No hidden additional positive relation from negative Serres | **SUPPORTED**, specifically conditional on the full-ideal import | S1 357–361; S4 9, 19 |
| Actual quotient basis, dimension, and \(n>r+s\) zero-space claim | **SUPPORTED for all stated parameters** | S1 75–93, 363–378; §2 |
| Actual \(F_1,F_2,F_3\) formulas | **SUPPORTED** | S1 411–444; §3 |
| \(W_1,W_2\) order, signs, full coefficient tables, and consuming brackets | **SUPPORTED** | S1 446–504; §3 |
| Every other \(W_j\) target and the \(n=2\) exception | **SUPPORTED** | S1 388–408, 585–595; §§3, 6 |
| Diagonal-only rows, existence conditions, and positive diagonals | **SUPPORTED** | S1 506–525; §4 |
| Auxiliary positive metric, \(E_3^*=F_3\), and exact \(EF\)-kernel | **SUPPORTED** | S1 527–566; §5 |
| Positive remaining principal block and triangular spectrum, without diagonalizability | **SUPPORTED** | S1 568–583; §5 |
| Full \(n=2\) \(W_3,W_4\) table and inverse-Gram consumption | **SUPPORTED** | S1 585–626; §6 |
| Full \(A_2\), endpoint omissions, and scalar \(6\) at \(r=s=1\) | **SUPPORTED** | S1 628–652; §6 |
| Supplied \((3,7,8)\) component, nonzero correction, and spectrum | **SUPPORTED as written verification of the supplied claim** | S1 675–730; §7 |
| Invertibility for all \(r,s\ge1,n\ge2\), including nonpositive \(h_3\)-weight | **SUPPORTED** | S1 68–102; §§2–6 |
| No cancellation, coevaluation injectivity, and absence of every generalized-zero chain in this class | **SUPPORTED** | S1 104–124, 732–764; §8 |
| Full projected-seed generalized-primary equality | **SUPPORTED at the named f314 interface** | S1 156–165; S3 168–198; §8 |
| Unrestricted other horizontal coefficients, whole-level-eight conclusions, global \(B_8=0\), all-level \(J=\tau\) | **INCONCLUSIVE / NOT ESTABLISHED BY THIS REVIEW** | Explicit limitations at S1 766–774 |
| Original-book/source authentication, novelty, human or formal/kernel acceptance | **INCONCLUSIVE / OUTSIDE THIS REVIEW** | S1 772; S4 27 |

**REFUTED claims: none within the reviewed scope.**

## 10. Methods and assurance ceiling

- The complete manifest, receipt, and all seven status/permission controls were read before the direct administrative pre-body ACK and before packet access.
- Complete packet reading preceded mathematical derivation.
- The explicitly authorized earlier review S3 was read as a frozen input. No unlisted prior review, current sibling outcome, author code, linked finite certificate, held payload, or quarantined consumer was opened.
- The general author’s permission to use fresh examples was not treated as a violation and did not widen this written reviewer’s method.
- No scientific executable, interpreter, CAS, solver, enumeration, replay, new selected instance, build, test, lint, formatter, external-model CLI, installation, paid/heavy/remote job, or external mutation was used.
- The special \(n=2,r=s=1\) corner and \((3,7,8)\) illustration were audited because they were expressly assigned.
- The runtime identity is `anthropic/claude-fable-5-1`, as supplied by the runtime context, not independently measured.
- The parent supplied a metadata observation at **2026-10-30T09:54:48-0700 PDT** and a fresh actual parent clock observation at **2026-10-30T10:00:14-0700 PDT**. Neither is claimed as child-native start, private derivation, or completion time.
- A substantive written checkpoint was delivered to Main. No child-native timing or continuous-supervision certificate is asserted.
- No review file persistence, scientific execution, original-source authentication, independent-model-family review, human review, formal/kernel verification, or novelty certification is claimed.

## 11. Overall verdict

**overall_correctness: correct**

**explanation:** At the named displayed full-Cartan/f276/f306/f314 boundaries, Theorem B proves invertibility and positive real spectrum on every actual horizontal-\((1,1,n)\) component for all \(r,s\ge1\) and \(n\ge2\). The complete two-seed quotient basis, actual lowering signs, marked-row cancellation, auxiliary-metric principal-block argument, active \(n=2\) Gram corner, and supplied level-eight component reconstruct without a diagonalizability assumption. The result does not establish whole-level-eight or all-level acceptance.

**confidence: 0.98**

---

## Materialization target: `f376-kac-all-horizontal11-multilowering-proof-review/reviewer-process-v1.md`

# f376 — Reviewer process and metadata record

**Role:** WRITTEN review of f364 Theorem B, all \(r,s\ge1\), all \(n\ge2\).

**Delivery:** Complete direct-return review body supplied for parent materialization. No filesystem write was attempted or claimed; no alternate-path or shell-writing bypass was used.

## Binding

- Manifest SHA256: `bfec0a442f143f27d4eda6950b56dc4051b728455c5971a16e2e2fb884d57e1d`
- Receipt SHA256: `6d7a793d143982d18c56fc1a88cc03c3c1275d751e976349ca538e72cf9779cf`
- Packet SHA256: `eac70fa9260600f89153dbc413b856df9c8eaa1de1be4ad5e51c0a1303bc67a8`

Bindings, byte counts, LF counts, and live matching were supplied by the parent metadata record. They are not reviewer-native hash execution.

## Observed read and ACK chronology

1. Read the mandatory memory summary and procedural written-acceptance/snapshot-review skills. They were not used as mathematical premises.
2. Read the complete manifest and freeze receipt.
3. Read all seven named status/permission controls, including the separately recovered endings of the selected-diagnostic quarantine and duty-reporting control:
   - frontier-first owner direction;
   - L1 selected-diagnostic quarantine;
   - written-duty execution/reporting deviations;
   - prospective author-method restoration;
   - held compression-claim consumer quarantine;
   - CORE-GRAM auxiliary-operator quarantine;
   - privacy auxiliary-parameter quarantine.
4. Delivered a direct administrative pre-body ACK committing to exact-scope imports, NONINPUT treatment of held material, complete raw packet reading, written-only methods, and direct-return delivery under the read-only role.
5. Read the ordered packet LF1–1389 raw in consecutively numbered windows of no more than 20 LF. Complete coverage included S1 logical line 790, S3 logical line 457, and S5 final line 74.
6. During packet reading, received and read the complete parent live metadata supply. Its observation was **2026-10-30T09:54:48-0700 PDT**.
7. Began mathematical reconstruction only after complete packet reading.
8. Delivered a substantive checkpoint to Main reporting completed reconstruction of:
   - the all-\(n\) actual whole-two-seed quotient basis;
   - \(F_1,F_2,F_3\), \(W_1,W_2\), and all target spaces;
   - diagonal-only row cancellations;
   - the positive auxiliary metric, exact kernel, principal block, and triangular spectrum;
   - the complete \(n=2\) mixed Gram block and scalar \(6\);
   - the supplied \((3,7,8)\) matrix and spectrum.
9. Received the fresh parent observation **2026-10-30T10:00:14-0700 PDT**, explicitly supplied as the parent’s actual clock observation.
10. Completed the self-contained written review with **0 FATAL / 0 MAJOR / 0 MINOR** findings.

The two parent clocks are metadata observations only. No child-native start, derivation, completion, execution, or elapsed-time measurement is invented.

## Method and exposure boundary

No scientific code or executable was generated or run. No CAS, solver, enumeration, certificate replay, build, test, lint, formatter, newly selected mathematical probe, scientific network source, external-model CLI, or paid/heavy/remote job was used.

Only the manifest-authorized sources were mathematical inputs. The expressly supplied earlier review S3 was read; no current sibling outcome or unlisted prior review was read. Held material and its proof, method, selection, planning, or confidence consumers remained NONINPUT. Linked author code and finite certificates were not opened.

The general author’s supplied examples were permitted under its own scope. Reviewing the expressly assigned \(r=s=1,n=2\) corner and \((3,7,8)\) component did not authorize the reviewer to choose new probes.

No frozen source, historical record, provider, credential, infrastructure, or external publication was changed. No deletion, commit, or push occurred.

**Scientific result:** Theorem B is supported for its entire quantified horizontal-\((1,1)\) class at the named conditional interfaces. Whole-level-eight, all-level, original-source-authentication, novelty, human, independent-family, and formal/kernel gates remain unpaid.