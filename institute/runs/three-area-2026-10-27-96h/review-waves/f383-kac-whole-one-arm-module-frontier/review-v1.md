# Whole one-arm finite-type Kac modules: complete \(b=1\) no-cancellation

**Materialization target:** `f383-kac-whole-one-arm-module-frontier/author-candidate-v1.md`

**Status: AUTHOR CANDIDATE — UNREVIEWED.** This is a complete written derivation, not parent adoption, independent-family verification, formal verification, or novelty certification. No scientific executable was run, and no repository file was written.

## 1. Result and exact target coverage

Use the displayed full-Cartan presentation
\[
A(r,s)=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-r&-s&2
\end{pmatrix},
\qquad
S=G_{\mathcal C}/J,
\]
where \(J\) contains **all positive and negative Serre relations**. Write
\[
E_i=\operatorname{ad}e_i,\qquad F_i=\operatorname{ad}f_i,
\qquad
\overline A_n=\overline\mu_n\overline{\mathcal C}_n.
\]

### Theorem

For
\[
\boxed{r\in\{1,2,3\},\qquad s>r,}
\]
the operator \(\overline A_n\) is invertible on **every entire actual component**
\[
\boxed{S_{(a,1,n)},\qquad a\ge1,\quad n\ge2.}
\]

The proof also covers \(a=0\). Empty components are included without asserting that they are nonzero.

There is **no positive-\(h_3\)-weight restriction**. In particular, the theorem covers
\[
2n-ra-s\le0
\]
and retains contributions from both arms and the mixed inverse-Gram block whenever they occur.

The mirrored statement exchanges nodes \(1,2\):
\[
\boxed{s\in\{1,2,3\},\quad r>s,\quad
\overline A_n\text{ invertible on every }S_{(1,b,n)},\ b\ge1,\ n\ge2.}
\]

Consequently, throughout these classes,
\[
\boxed{
\ker\overline{\mathcal C}_n=0,\qquad
\operatorname{im}\overline{\mathcal C}_n\cap\ker\overline\mu_n=0,\qquad
\ker\overline A_n^{\,k}=0\quad(k\ge1).
}
\]

At the retained f314 identification, this also gives the corresponding **full generalized-primary projected-seed equality**.

This closes the preferred one-arm class in the manifest, rather than another numerical case or a narrower defect strip. It does **not** establish whole-level \(B_8=0\), all horizontal degrees, or all-level \(J=\tau\).

---

## 2. Retained imports

The argument has the following explicit boundaries.

1. **Displayed presentation and full Cartan.** The row convention is
   \([h_p,e_i]=c_{pi}e_i\). Additional Cartan directions are not quotiented away.

2. **f276 actual-source/whole-ideal bridge**, at the adopted disposition
   `math-3-actual-free-source-and-full-serre-ideal-at-displayed-presentation-parent-v1.md`,
   SHA256
   `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e`.

   In particular, the actual positive source has the stated ordinary free-Lie model, both complete positive seed modules generate the whole positive ideal, and
   \[
   J/K=P_+\oplus P_-
   \]
   excludes additional positive relations from negative Serres. Positive-degree counting alone is not substituted for this bridge.

3. **f306 contraction normalization.** Actual theta-duals, the finite-Levi inverse Gram matrix, coevaluation, and the consuming bracket descend as stated.

4. **f314 generalized-primary interface.** Only for the final projected-seed corollary, retain
   \[
   E_0(\overline A_n|S_\alpha)
   \cong
   E_{n,\alpha}/\operatorname{im}(e_n\Phi_n)_\alpha,
   \]
   with the **whole two-seed ideal** and the **full generalized zero-primary space**.

5. **Finite-type facts already used in S3.** Ordinary finite-dimensional Chevalley–Serre theory, PBW for a finite-dimensional semisimple algebra, finite-dimensional \(\mathfrak{sl}_2\)-module decomposition, and a compact-averaged positive Hermitian form.

6. **The adopted horizontal-\((1,1)\) calculation**, S1 §B and its full derivations S2/S4, is used at precisely that slice. Its finite experiment and linked checker are not inputs here.

No invariant positive form on the whole nonsymmetrizable algebra is assumed. The contraction is never identified with a finite-type Casimir.

---

## 3. Exact whole-\(b=1\) module identification

Set
\[
v=e_2,\qquad
M=\bigoplus_{a,n\ge0}S_{(a,1,n)}.
\]

### 3.1 The acting finite-dimensional algebra

Nodes \(1,3\) have Cartan matrix
\[
\begin{pmatrix}2&-1\\-r&2\end{pmatrix},
\]
of type \(A_2,B_2,G_2\) for \(r=1,2,3\), respectively. Denote this finite-dimensional algebra by \(\mathfrak g_{13}\).

Its map into \(S\) is injective: a kernel would be an ideal of the finite-dimensional simple algebra, and cannot be the whole algebra because the retained full-Cartan injection keeps \(h_1,h_3\) nonzero.

The space \(M\) is a \(\mathfrak g_{13}\)-module, with
\[
F_1v=F_3v=0,\qquad h_1v=-v,\qquad h_3v=-sv.
\]
Every positive Lie word containing exactly one \(e_2\) can, by Jacobi, be written as a sum of positive \(\mathfrak g_{13}\)-words acting on \(v\). Thus \(M\) is cyclic.

Actual simple local nilpotence, finite Weyl conjugacy and finite-type PBW put this cyclic module in a finite-dimensional \(\mathfrak g_{13}\)-module. Therefore \(M\) itself is finite-dimensional.

### 3.2 The complete positive ideal, not a character guess

Linearize the positive presentation at \(e_2\)-count at most one. This is a calculation of that homogeneous slice, **not** a replacement of the original quotient by a truncated algebra.

The \(b=0\) presentation is the finite-type positive algebra \(\mathfrak n_{13}^+\). At \(b=1\), the module presentation is
\[
\boxed{
M\cong
U(\mathfrak n_{13}^+)v\Big/
\left(
U(\mathfrak n_{13}^+)E_1^2v+
U(\mathfrak n_{13}^+)E_3^{s+1}v
\right).
}
\]

Here:

- the entire \(b=0\) seed and all its \(b=1\) adjoint descendants are precisely the operator relations of \(\mathfrak g_{13}\);
- \(E_1^2v=0\) is the repeated-node-1 relation;
- \(E_3^{s+1}v=0\) is the second raw seed, with its entire module closure;
- positive seeds with at least two \(e_2\)'s cannot contribute to this positive homogeneous slice;
- exclusion of additional negative-Serre consequences is **the named f276 whole-ideal bridge**.

One can obtain the displayed module presentation by constructing the semidirect positive algebra with its abelian \(b=1\) linearization; the maps in both directions fix \(e_1,e_3,v\). Thus it retains the full relevant seed closure, not separate seed-rank subtraction.

Equivalently,
\[
\boxed{M\cong L^{(13)}(1,s)}
\]
as the finite-dimensional irreducible **lowest-weight** module of labels \((1,s)\).

For completeness, irreducibility also follows from finite-dimensional complete reducibility: the cyclic vector \(v\) is a joint lowest vector of fixed labels \((1,s)\). Its nonzero projections into irreducible summands all have those same labels; the module generated by the diagonal vector is one irreducible copy.

### 3.3 Exact low-grade PBW model

Let \(t=e_3\), and introduce finite-type positive root vectors
\[
z=[e_1,t],\qquad d=[t,z],\qquad
p=[t,d],\qquad q=[z,d].
\]
Use the corresponding capital letters \(T,Z,D,P,Q\) for their adjoint actions.

The nilradical \(\mathfrak n\) of the node-1 parabolic in \(\mathfrak g_{13}\), graded by \(\alpha_3\)-coefficient, is:

| \(r\) | \(\mathfrak n_1\) | \(\mathfrak n_2\) | \(\mathfrak n_3\) |
|---|---|---|---|
| 1 | \(\mathbb Ct\oplus\mathbb Cz\) | \(0\) | \(0\) |
| 2 | \(\mathbb Ct\oplus\mathbb Cz\) | \(\mathbb Cd\) | \(0\) |
| 3 | \(\mathbb Ct\oplus\mathbb Cz\) | \(\mathbb Cd\) | \(\mathbb Cp\oplus\mathbb Cq\) |

The relevant brackets are
\[
[T,Z]=D,\qquad [T,D]=P,\qquad [Z,D]=Q.
\]
For \(r=1\), \(D=P=Q=0\). For \(r=2\), \(P=Q=0\). For \(r=3\), \(P,Q\) commute with this nilradical.

Write \(e=E_1\). Since \(E_1^2v=0\), PBW gives
\[
\boxed{M_n\cong U(\mathfrak n)_n\otimes\operatorname{span}\{v,ev\}
\quad\text{for }n\le s.}
\]
There is no omitted relation at those grades: the remaining seed has grade \(s+1\), and its positive closure cannot decrease that grade.

The hypothesis \(s>r\) is crucial:
\[
r+1\le s.
\]
Thus **every exceptional low grade requiring a correction calculation is in this exact, untruncated PBW model**. Higher grades will be handled on the actual finite quotient, without a freeness claim.

---

## 4. Every lowering target and its consuming Gram coefficient

Use the normalized eight letters
\[
\begin{aligned}
u_0&=e_3,&u_1&=E_1e_3,&u_2&=E_2e_3,\\
u_3&=E_1E_2e_3,&u_4&=E_2E_1e_3,\\
u_5&=-\tfrac12E_1^2E_2e_3,&
u_6&=\tfrac12E_2^2E_1e_3,&u_7&=E_1u_6.
\end{aligned}
\]

Their horizontal charges are
\[
(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2).
\]

All singleton Gram entries are one. The only nonsingleton block is
\[
G_{\{3,4\}}=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{\{3,4\}}^{-1}
=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

Set
\[
f=F_3,\qquad g=F_1,\qquad R=F_2.
\]
The actual theta-dual operators are
\[
\begin{aligned}
W_0&=f,&W_1&=[f,g],&W_2&=[f,R],\\
W_3&=[W_2,g],&W_4&=[W_1,R],&
W_5&=-\tfrac12[W_3,g],\\
W_6&=\tfrac12[W_4,R],&
W_7&=[W_6,g].
\end{aligned}
\]
In particular, the order in \(W_1=[F_3,F_1]\) is retained.

On \(S_{(a,1,n)}\), \(n\ge2\), the targets are exactly:

| Operator | Target |
|---|---|
| \(W_0\) | \(M_{(a,n-1)}\) |
| \(W_1\) | \(M_{(a-1,n-1)}\) |
| \(W_2\) | \((\mathfrak g_{13})_{(a,n-1)}\) |
| \(W_3,W_4\) | \((\mathfrak g_{13})_{(a-1,n-1)}\) |
| \(W_5\) | \((\mathfrak g_{13})_{(a-2,n-1)}\) |
| \(W_6,W_7\) | Negative \(b\), positive \(n-1\): zero by triangular support |

A negative \(a\)-coordinate likewise gives zero. Since \(n-1\ge1\), no final target in this table is silently identified with Cartan.

The full consuming operator is therefore
\[
\boxed{
\begin{aligned}
\overline A_n={}&A^0+\operatorname{ad}(u_2)W_2\\
&+\frac13\left\{
\operatorname{ad}(u_3)(2W_3-W_4)
+\operatorname{ad}(u_4)(-W_3+2W_4)
\right\}
+\operatorname{ad}(u_5)W_5,
\\
A^0={}&Tf+ZW_1.
\end{aligned}}
\]

No mixed-Gram coefficient has been discarded.

On the \(b=1\) module,
\[
u_2=-Tv,\qquad
u_3=-Z v-T ev,\qquad
u_4=-Zv,\qquad
u_5=Zev.
\]

### 4.1 Node-1 equivariance, including the \(W_5\) term

The above full expression commutes with \(E_1,F_1,h_1\). This follows from invariant coevaluation, but the coefficients can also be checked directly:

| \(i\) | \(E_1u_i\) | \([E_1,W_i]\) |
|---|---|---|
| 0 | \(u_1\) | \(0\) |
| 1 | \(0\) | \(-W_0\) |
| 2 | \(u_3\) | \(0\) |
| 3 | \(-2u_5\) | \(-2W_2\) |
| 4 | \(-u_5\) | \(-W_2\) |
| 5 | \(0\) | \(W_3\) |

The \(F_1\) table is
\[
\begin{array}{c|rrrrrr}
i&0&1&2&3&4&5\\ \hline
F_1u_i&0&u_0&0&2u_2&u_2&-u_3\\
[F_1,W_i]&-W_1&0&-W_3&2W_5&W_5&0.
\end{array}
\]

Substitution makes both commutators with \(\overline A_n\) vanish. In particular, the singleton coefficient \(+1\) of \(u_5W_5\) is required.

Thus computations on an entire node-1 multiplicity space determine its raised vectors as well. Terms such as \(W_5\), which vanish on a lowest vector but can become active after raising, are retained by this exact intertwining identity—not dropped.

---

## 5. The high-grade two-term operator is positive on the actual module

The largest \(\alpha_3\)-coefficient of a positive root of \(\mathfrak g_{13}\) is \(r\), for \(r=1,2,3\). Consequently, when
\[
n\ge r+2,
\]
all targets of \(W_2,\ldots,W_5\) vanish, and
\[
\boxed{\overline A_n=A^0=E_3F_3+[E_1,E_3][F_3,F_1].}
\]

Choose a compact-averaged positive Hermitian form on the **finite-dimensional module \(M\)**. The finite-type Chevalley normalization gives
\[
T^*=f,\qquad Z^*=W_1,
\]
including the unequal root lengths. Hence
\[
\langle x,A^0x\rangle=\|fx\|^2+\|W_1x\|^2.
\]

It remains to prove that the joint kernel has no vector of positive grade.

Let
\[
K=\ker f\cap\ker W_1.
\]
The commutators
\[
[E_1,f]=0,\quad [E_1,W_1]=-f,\quad
[F_1,f]=-W_1,\quad [F_1,W_1]=0
\]
make \(K\) a node-1 \(\mathfrak{sl}_2\)-submodule, preserving \(n\).

If \(K\cap M_n\ne0\), it contains a nonzero node-1 lowest vector \(y\). Then
\[
F_1y=F_3y=0.
\]
In the irreducible lowest-weight module \(M\), the joint simple-lowering kernel is \(\mathbb Cv\), at grade zero. One can also see uniqueness directly: with the compact form, such a \(y\) at another weight is orthogonal to \(v\) and to every nonconstant positive word applied to \(v\), contradicting cyclicity.

Therefore
\[
K\cap M_n=0\qquad(n>0).
\]
It follows that
\[
\boxed{A^0\text{ is positive definite on every }M_n,\ n>0.}
\]

This proves all grades \(n\ge r+2\), without requiring \(2n-ra-s>0\).

This is **not** an identification of the original contraction with a Casimir. It is positivity of its explicitly derived two surviving terms on a finite auxiliary module.

---

## 6. Exact coverage of the exceptional low grades

Write \(V_k\) for the node-1 irreducible \(\mathfrak{sl}_2\)-module with lowest weight \(-k\).

PBW symmetrization is node-1 equivariant. The exact low-grade model therefore gives:

| Case | Exact node-1 decomposition |
|---|---|
| \(r=1,n=2\) | \(V_3\oplus V_1\) |
| \(r=2,3,n=2\) | \(V_3\oplus2V_1\) |
| \(r=2,n=3\) | \(V_4\oplus2V_2\oplus V_0\) |
| \(r=3,n=3\) | \(V_4\oplus3V_2\oplus2V_0\) |
| \(r=3,n=4\) | \(V_5\oplus3V_3\oplus4V_1\) |

For example,
\[
\mathfrak n_1=V_1,\qquad
\mathfrak n_2=V_0,\qquad
\mathfrak n_3=V_1
\]
where those spaces exist. At \(r=3,n=4\), the PBW contributions are
\[
\left(
\operatorname{Sym}^4V_1
\oplus\operatorname{Sym}^2V_1
\oplus V_0
\oplus(V_1\otimes V_1)
\right)\otimes V_1,
\]
giving the last row.

### Detection lemma

If an operator commutes with \(\mathfrak{sl}_2\), then on an isotypic component it has the form
\[
I_{V_k}\otimes B_k.
\]
Its restriction to any weight occurring in \(V_k\) contains the same multiplicity operator \(B_k\). Thus invertibility at that weight detects all such isotypic components.

Here
\[
h_1|S_{(a,1,n)}=2a-1-n.
\]
The horizontal-\((1,1)\) slice has weight \(1-n\). It detects:

- every summand at \(n=2\);
- every \(V_4,V_2\) summand at \(n=3\), missing only the \(V_0\)'s;
- every \(V_5,V_3\) summand at \(r=3,n=4\), missing only the four \(V_1\)'s.

These decompositions are a **coverage argument**, not the no-cancellation proof. The missing multiplicity operators are computed below from the actual consuming formula.

---

## 7. Grade two: complete mixed Gram, then node-1 saturation

Use the actual horizontal-\((1,1)\) basis
\[
z_i=[X_i,Y_{2-i}],
\quad
X_i=E_3^ie_1,\quad Y_j=E_3^je_2.
\]

The full exceptional lowering table is
\[
\begin{array}{c|ccc}
&z_0&z_1&z_2\\ \hline
W_3/e_3&4(s-1)&r&-2(r-1)\\
W_4/e_3&2(s-1)&-s&-4(r-1).
\end{array}
\]
The consuming brackets are
\[
[u_3,e_3]=z_0+z_1,\qquad
[u_4,e_3]=-z_1-z_2.
\]

The \(W_0,W_1,W_2\) contribution is
\[
\begin{pmatrix}
2(s-1)&r&0\\
-2(s-1)&4(r+s)-4&-2(r-1)\\
0&s&2(r-1)
\end{pmatrix},
\]
and the complete mixed inverse-Gram contribution is
\[
\begin{pmatrix}
2(s-1)&(2r+s)/3&0\\
2(s-1)&r+s&2(r-1)\\
0&(r+2s)/3&2(r-1)
\end{pmatrix}.
\]

Their sum is
\[
\boxed{
\overline A_2=
\begin{pmatrix}
4(s-1)&(5r+s)/3&0\\
0&5(r+s)-4&0\\
0&(r+5s)/3&4(r-1)
\end{pmatrix}.
}
\]
For \(r=1\), omit row and column \(2\). Here \(s>r\), so \(z_0\) exists.

Every surviving diagonal is positive. The detection lemma and the grade-two decomposition show that **the entire \(M_2\)** is invertible—not merely its \(a=1\) weight space.

This uses the previously adopted horizontal calculation to prove new node-1-saturated components; it does not count a reproof of that old slice as the new result.

---

## 8. Universal identities for the remaining finite calculations

All products below are compositions of actual adjoint operators.

Define
\[
\boxed{L=Tev-Zv=2u_4-u_3.}
\]
Then
\[
gL=eL=0,\qquad
fL=(s+2r)ev,\qquad
RL=3z.
\]

The last identity uses the actual \(f_2\)-action, not an auxiliary adjoint:
\[
R(Uv)=-U h_2
\quad(U\in U(\mathfrak n_{13}^+)),
\]
because \(F_2\) commutes with \(E_1,E_3\).

In particular,
\[
Rv=-h_2,\qquad R(ev)=-e_1,
\]
and
\[
R(Tv)=-t,\quad R(Zv)=-2z,\quad
R(Dv)=-3d,\quad R(Pv)=-4p,\quad R(Qv)=-5q.
\]
The coefficients follow from
\[
[h_2,x]=-(a+n)x
\]
for a positive \(\mathfrak g_{13}\)-root vector of degree \((a,n)\).

The required root commutators are
\[
\begin{aligned}
[f_3,z]&=-r e_1,&
[f_3,d]&=2(r-1)z,\\
[f_1,z]&=t,&[f_1,d]&=0.
\end{aligned}
\]
For \(r=3\), additionally,
\[
[f_3,p]=3d,\quad [f_3,q]=0,\quad
[f_1,p]=0,\quad[f_1,q]=p,\quad
W_1q=3d.
\]

These identities, together with the displayed full Gram formula, are the finite algebraic source for all matrices below. They specify the inputs and calculations; none is reported as program output.

---

## 9. Type \(B_2\), grade three: the missing \(V_0\)

Here \(r=2,\ s\ge3\). The only isotypic component not detected at \(a=1\) is the single \(V_0\), spanned by
\[
\boxed{x=-DL=[L,d].}
\]
It is nonzero by the exact grade-three PBW model.

Since \(gx=0\),
\[
W_1x=-gf x.
\]
The actual lowerings are
\[
fx=-2ZL-(s+4)Dev,\qquad
gf x=-2TL-(s+4)Dv.
\]
Because \(d\) is central in this nilradical,
\[
A^0x=(s+6)x.
\]

On this vector,
\[
W_2x=W_3x=W_5x=0,
\qquad
W_4x=3(s+2)d.
\]
For instance, \(Rx=0\), and
\[
W_4x=Rgf x
=-2R(TL)-(s+4)R(Dv)
=3(s+2)d.
\]

The full mixed-Gram term is
\[
\frac13\operatorname{ad}(2u_4-u_3)W_4x
=(s+2)x.
\]
Thus
\[
\boxed{\overline A_3x=(2s+8)x.}
\]

The remaining summands \(V_4\oplus2V_2\) are detected by the old horizontal slice. Its actual grade-three matrix, in \(z_0,z_1,z_2\), is
\[
\begin{pmatrix}
3(s-2)&2&0\\
0&3s+2&0\\
0&0&4s
\end{pmatrix},
\]
which is invertible for \(s\ge3\).

Therefore the entire \(M_3\) is invertible for type \(B_2\).

---

## 10. Type \(G_2\), grade three: the two missing \(V_0\)'s

Here \(r=3,\ s\ge4\). A basis of the two-dimensional node-1-trivial space is
\[
\boxed{x=-DL,\qquad y=Pev-Qv.}
\]
Both are nonzero and independent by PBW.

Put \(k=s+6\). Directly,
\[
\begin{array}{c|cc}
&fx&gf x\\ \hline
x&-4ZL-kDev&-4TL-kDv\\
y&3Dev&3Dv
\end{array}
\]
where the first column is interpreted as \(f\) applied to the indicated row vector.

Consequently,
\[
A^0x=(s+10)x-(s+6)y,\qquad
A^0y=-3x+3y,
\]
so
\[
A^0=
\begin{pmatrix}
s+10&-3\\
-(s+6)&3
\end{pmatrix}.
\]

The full actual lowering calculation is
\[
Rx=3q,\qquad Ry=6q,
\]
\[
W_2x=W_2y=W_3x=W_3y=W_5x=W_5y=0,
\]
and
\[
\boxed{W_4x=3(s+5)d,\qquad W_4y=9d.}
\]

The \(W_1R\) part of \(W_4=[W_1,R]\) is essential here:
\[
\begin{aligned}
W_4x&=W_1(3q)+Rgf x
=9d+3(s+2)d,\\
W_4y&=W_1(6q)+Rgf y
=18d-9d.
\end{aligned}
\]
It must not be dropped merely because \(R\) vanished in the preceding \(B_2\) calculation.

The correction matrix is therefore
\[
\overline A_3-A^0=
\begin{pmatrix}
s+5&3\\
0&0
\end{pmatrix},
\]
giving
\[
\boxed{
\overline A_3\big|_{\operatorname{span}\{x,y\}}
=
\begin{pmatrix}
2s+15&0\\
-(s+6)&3
\end{pmatrix}.
}
\]
Its determinant is \(3(2s+15)>0\).

The detected \(V_4\oplus3V_2\) part has horizontal matrix
\[
\begin{pmatrix}
3(s-2)&3&0&0\\
0&3s+6&0&0\\
0&0&4s+3&0\\
0&0&s&3
\end{pmatrix},
\]
again invertible.

This proves invertibility on the entire type-\(G_2\) grade-three module.

---

## 11. Type \(G_2\), grade four: the four missing \(V_1\)'s

This is the remaining case. Let \(r=3,\ s\ge4\).

### 11.1 Complete lowest multiplicity basis

The node-1-lowest space of the four \(V_1\)'s has basis
\[
\boxed{
A=DTL,\qquad
B=D^2v,\qquad
C=PL,\qquad
H=(TQ-ZP)v.
}
\]
Each has \(h_1\)-weight \(-1\) and is killed by \(g=F_1\).

They are independent by PBW. For example, their ordered leading terms distinguish the \(T^2D\,ev\), \(D^2v\), \(TP\,ev\), and \(TQv\) contributions. The decomposition in §6 shows that these four vectors exhaust the missing multiplicity space.

### 11.2 Actual simple-lowering table

Put \(k=s+6\). The exact table is
\[
\begin{array}{c|l|l}
X&fX&gfX\\ \hline
A&
4ZTL+(s+1)DL+kDTev&
4T^2L+kDTv\\
B&
8ZDv-4Qv&
8TDv-4Pv\\
C&
3DL+kPev&
kPv\\
H&
(s+3)Qv+3Pev-3ZDv&
kPv-3TDv
\end{array}
\]

Since \(gX=0\), one has \(W_1X=-gfX\). Applying \(T\) and \(Z\) gives
\[
\boxed{
A^0=
\begin{pmatrix}
2s+11&0&3&0\\
s+6&8&0&-3\\
2s+7&0&s+9&3\\
-(s+6)&-4&0&s+3
\end{pmatrix}
}
\]
in the ordered basis \((A,B,C,H)\).

For example,
\[
\begin{aligned}
A^0A
&=T\bigl(4ZTL+(s+1)DL+kDTev\bigr)
 -Z\bigl(4T^2L+kDTv\bigr)\\
&=(2s+11)A+kB+(2s+7)C-kH.
\end{aligned}
\]
The noncommutative relations \([T,Z]=D\), \([T,D]=P\), \([Z,D]=Q\) are retained in this simplification.

### 11.3 Every surviving correction

There is no positive \(\mathfrak g_{13}\)-root of grade four, so \(RX=0\) here. Write
\[
W_2X=c_Xq,\qquad W_4X=d_Xp.
\]
Then
\[
W_2X=-RfX,\qquad W_4X=RgfX.
\]
The complete coefficients are
\[
\boxed{
\begin{array}{c|rrrr}
X&A&B&C&H\\ \hline
c_X&4s-3&4&3-s&5s+3\\
d_X&s+18&-8&-4s-24&-4s-15.
\end{array}}
\]

Also,
\[
W_3X=-c_Xp,\qquad W_5X=0.
\]
The latter agrees both with its target degree and with
\(W_5X=\tfrac12gW_3X\), since \(gp=0\).

For transparency, the target computations use
\[
RfA=(3-4s)q,\quad RfB=-4q,\quad
RfC=(s-3)q,\quad RfH=-(5s+3)q,
\]
and the displayed \(gfX\) table gives the \(d_X\) row.

Now consume these lowerings with the **full inverse Gram block**. The needed brackets are
\[
[u_2,q]=TQv,
\]
\[
[u_3,p]=TPev+ZPv,\qquad [u_4,p]=ZPv.
\]
Consequently, if \(W_2X=cq,\ W_3X=-cp,\ W_4X=dp\), then
\[
\boxed{
(\overline A_4-A^0)X
=-\frac{2c+d}{3}\,C+cH.
}
\]

This identity includes the second arm and both mixed-Gram columns. It is not a rank or character calculation.

### 11.4 Full matrix and determinant

Adding these corrections gives
\[
\boxed{
K_4=
\overline A_4\big|_{\operatorname{span}\{A,B,C,H\}}
=
\begin{pmatrix}
2s+11&0&3&0\\
s+6&8&0&-3\\
3-s&0&3s+15&6-2s\\
3s-9&0&3-s&6s+6
\end{pmatrix}.
}
\]

The \(B\)-column has only its diagonal entry \(8\). Removing that row and column leaves
\[
\begin{pmatrix}
2s+11&3&0\\
3-s&3s+15&6-2s\\
3s-9&3-s&6s+6
\end{pmatrix}.
\]
Set \(u=s-3\). Its determinant is
\[
\begin{aligned}
&(2u+17)
\left((3u+24)(6u+24)-2u^2\right)+72u\\
&\hspace{1cm}
=(2u+17)(16u^2+216u+576)+72u\\
&\hspace{1cm}
=32\bigl(s^3+13s^2+48s+18\bigr).
\end{aligned}
\]
Thus
\[
\boxed{
\det K_4=
256\bigl(s^3+13s^2+48s+18\bigr)>0
\qquad(s\ge4).
}
\]

No assertion that all eigenvalues of this new block are positive real is needed. Its nonzero determinant proves the required invertibility.

The detected \(V_5\oplus3V_3\) part has horizontal matrix
\[
\begin{pmatrix}
4(s-3)&3&0&0\\
0&4s+3&0&0\\
0&3(s-2)&2s+2&3\\
0&0&0&5s
\end{pmatrix},
\]
whose diagonal-block eigenvalues are
\[
4(s-3),\quad4s+3,\quad2s+2,\quad5s.
\]
They are positive for \(s\ge4\).

Therefore the entire type-\(G_2\) grade-four module is invertible.

---

## 12. Assembly of the theorem

The cases are exhaustive:

- \(r=1\): grade two is covered by §7; every \(n\ge3\) by §5.
- \(r=2\): grades two and three are covered by §§7 and 9; every \(n\ge4\) by §5.
- \(r=3\): grades two, three and four are covered by §§7, 10 and 11; every \(n\ge5\) by §5.

All exceptional calculations occur at \(n\le r+1\le s\), where their full PBW source is exact. All subsequent grades are handled on the **actual finite module**, including the seed relation and its entire closure.

The operator preserves each actual root component. Invertibility on \(M_n\) therefore proves invertibility on every \(S_{(a,1,n)}\).

Node exchange proves the mirrored theorem. The contraction is basis-independent inverse-Gram coevaluation, so the exchange does not depend on retaining the same signed normalized-letter basis. ∎

---

## 13. Consequences and relation to the original problem

### 13.1 Coevaluation and generalized primary

Since
\[
\overline A_n=\overline\mu_n\overline{\mathcal C}_n
\]
is invertible, \(\overline{\mathcal C}_n\) is injective.

If \(y=\overline{\mathcal C}_nx\) and \(\overline\mu_ny=0\), then
\(\overline A_nx=0\), hence \(x=y=0\). Thus
\[
\operatorname{im}\overline{\mathcal C}_n\cap\ker\overline\mu_n=0.
\]
Invertibility also excludes every generalized-zero chain.

At the named f314 interface,
\[
\boxed{
\operatorname{im}(e_n\Phi_n)_\alpha=E_{n,\alpha}
}
\]
for the theorem's root components. This retains the whole two-seed ideal and full generalized primary.

If all three original \(F_1,F_2,F_3\) kill \(x\), every \(W_i\) kills \(x\), so \(x=0\) in these classes. No simultaneous-lowering counterexample is produced.

### 13.2 A separate scoped radical corollary

At f276's retained definition of \(\tau\), \(J\subseteq\tau\), and
\[
\mathcal R=\tau/J
\]
is a Cartan-disjoint ideal of \(S\).

The intersection \(\mathcal R\cap M\) is a \(\mathfrak g_{13}\)-submodule. Since \(M\) is irreducible, it is either \(0\) or \(M\). The latter is impossible:
\[
v=e_2\in\mathcal R
\quad\Longrightarrow\quad
[f_2,v]=-h_2\in\mathcal R,
\]
contradicting Cartan disjointness.

Hence
\[
\boxed{\mathcal R\cap M=0.}
\]
In particular, the actual original-radical equality
\[
\boxed{J_\alpha=\tau_\alpha}
\]
holds on this whole \(b=1\) module, and on its mirrored class, at the same displayed-presentation/f276 boundary.

This corollary is logically distinct from contraction no-cancellation: irreducibility alone did not establish the new contraction matrices.

### 13.3 An explicitly nonvacuous new component

Take
\[
(r,s,a,b,n)=(2,3,2,1,3).
\]
Then
\[
\alpha(h_3)=6-4-3=-1.
\]
It lies outside the old arbitrary-horizontal positive-weight strip.

The entire actual component has dimension four. A basis is obtained from
\[
E_1z_0,\ E_1z_1,\ E_1z_2,\ x,
\]
where the \(z_i\) are the horizontal-\((1,1,3)\) basis and \(x=-DL\). In this decomposition its operator is block diagonal with blocks
\[
\begin{pmatrix}
3&2&0\\
0&11&0\\
0&0&12
\end{pmatrix}
\quad\text{and}\quad(14).
\]
Thus its eigenvalues are \(3,11,12,14\).

This is an exact **written consequence** of the source model and matrices above, not observed execution.

---

## 14. Unpaid gates and limits

The result is complete for the theorem's quantified one-arm class, subject to its named imports. The following are not established:

1. A corresponding contraction theorem for both horizontal coefficients at least two.
2. Equal parameters by this argument, or unequal short-arm parameter at least four.
3. Entire-level-eight contraction, \(B_8=0\), or all-level \(J=\tau\).
4. Independent reconstruction of the underlying f276/f306/f314 manuscripts beyond the imports stated here.
5. Original-book authenticity or a new current-status/novelty audit.
6. Disjoint scientific review, independent-model-family review, human review, formal/kernel checking, or executable finite corroboration of these new matrices.

No proof of positive real spectrum is claimed for the new \(G_2\) grade-four multiplicity block; only its explicitly sufficient invertibility is proved.

---

## 15. Source, calculation and process provenance

### Frozen bindings

The user and parent metadata supplied:

- Manifest SHA256:  
  `8bd88e9ea143279cc3df276644c07cd7cf2f59d17665413133d68775768e4076`
- Freeze-receipt SHA256:  
  `380a5cb634e60f1d0f3f53a58cb7415ed321d9e91bfc3ec425721bf212945fae`
- Literal-packet SHA256:  
  `9b6933fba7be2d7a8dc74069f1035e7d900c02747c7b506749f8e2b6342ff15f`

These are supplied bindings, **not child-executed hash observations**.

### Read chronology

1. Read the mandatory memory summary and research-orchestration skill as procedural context, not mathematical premises.
2. Read the complete manifest and receipt; recovered the clipped research-task text raw.
3. Read all seven named status/permission controls through their endings **before scientific packet access**.
4. Read the complete ordered packet raw, sequentially, in requested windows:
   \(1\!-\!310\), \(311\!-\!630\), \(631\!-\!950\), \(951\!-\!1270\),
   \(1271\!-\!1590\), \(1591\!-\!1910\), and \(1911\!-\!2153\),
   through the final `S4|832` ending.
5. Read this wave's parent metadata and dispatch receipt.
6. During derivation, read the complete 27-line f276 disposition and complete 74-line displayed source-definitions release to clarify the named presentation/whole-ideal boundary. No underlying held source was followed.
7. Inspected process-list metadata while locating the parent communication route. No current sibling scientific body or result was opened or used.

The initial substantive route was whole-module identification plus high-grade joint-kernel positivity. The exceptional cases were then closed in order: node-1 saturation at grade two, the \(B_2\) grade-three singlet, the \(G_2\) grade-three singlets, and the \(G_2\) grade-four multiplicity block.

### Clock attribution and checkpoints

Actual parent-supplied observations were:

- `2026-10-30T10:18:22-0700 PDT`, in the live metadata;
- `2026-10-30T10:23:44-0700 PDT`, supplied by Main;
- `2026-10-30T10:31:58-0700 PDT`, supplied by Main.

Substantive checkpoints were sent to Main during the derivation and final assembly. These clocks are **parent observations**, not child-native start, derivation, completion, or elapsed-time measurements. No unobserved timing certificate is asserted.

### Calculation and execution distinction

All new calculations in this submission are **written exact algebra**, with symbolic integer parameter \(s\). Their full finite source consists of:

- the actual module presentation in §3;
- the finite root-vector definitions and commutators;
- the actual normal-ordering rule \(R(Uv)=-Uh_2\);
- every surviving lowering target and inverse-Gram coefficient in §4;
- the complete exceptional tables and resulting matrices in §§7–11.

No executable code was generated or run. Accordingly, there is no program argv, observed stdout, solver status, or executable experiment result to report. The displayed matrices and determinants must not be relabeled as executed checks.

No build, test, lint, formatter, CAS, solver, enumeration, certificate replay, external-model CLI, paid/heavy/remote job, installation, deletion, credential/provider change, commit, push, or publication was performed. No repository or frozen file was changed; this full body is returned for parent materialization.

**Requested scientific disposition:** disjoint reconstruction of the exact module identification, the complete consuming Gram expression, and especially the \(B_2/G_2\) low-grade multiplicity matrices, followed by a separately recorded parent decision. **No acceptance is self-granted.**