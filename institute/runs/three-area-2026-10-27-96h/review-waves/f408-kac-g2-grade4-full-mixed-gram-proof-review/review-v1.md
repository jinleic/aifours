# f408 WRITTEN review — \(G_2\), grade four, full mixed-Gram block

**Disposition:** **SUPPORTED at the assigned conditional scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

For every integer \(s\ge4\), at \(r=3\), I reconstruct the complete grade-four node-1 decomposition, the four-dimensional previously undetected multiplicity space, every contributing actual lowering, the full mixed inverse-Gram consumption, the displayed matrix \(K_4\), and
\[
\det K_4=256(s^3+13s^2+48s+18)>0.
\]
The remaining detected summands are also invertible. Thus the assigned calculation supports invertibility on every actual \(S_{(a,1,4)}\), including its empty components, **conditional on the named source/whole-ideal and contraction interfaces**.

This is a written review, not parent adoption of the whole f383 candidate. It does not dispose of the other verification slices or establish the original target globally.

## 1. Binding, reading, and method

### Frozen bindings

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f408-kac-g2-grade4-full-mixed-gram-proof-review/`

The supplied bindings are:

- Manifest: `ea85c53387a59db0b6568deaf8b86ce03e228e4feff0653a8894d6f00bf564ea`
- Freeze receipt: `209a57c49fbfccd3272b6853cf89f74db91b729e35d42bbe01caf99fde757d70`
- Literal packet: `fbc0bff9b9df7a864e7dd5f71953cf099d87cc911f2f21852848d8172cf6ea5f`

These are supplied bindings corroborated by the **parent’s** metadata record. I did not execute a hashing command.

I read the complete manifest, freeze receipt, dispatch receipt, all seven status-only controls, and the parent live-metadata record before the mathematical packet. I sent the required administrative pre-body ACK to Main before opening that packet. I then read packet lines 1–1157 sequentially, raw, in windows of at most 20 lines, through the final `S3|74` ending.

The packet contains:

- **S1:** f383 `review-v1.md`, SHA256  
  `c8f654d88661a9c11475fb33bd5d5f3837f31819ecff691350b86e189aaf5d40`, through `S1|1034`.
- **S2:** `math-3-finite-type-two-lowering-strip-and-complete-horizontal11-parent-v1.md`, SHA256  
  `e28d6f6a237da33908080f8f1c56a6c79cce941f1aad97bc9df2be4365fec792`, complete 47-line body.
- **S3:** `math-3-serre-family-definitions-v1.md`, SHA256  
  `b415be711bf075210e2154db9812b024cb2282dfd38c3ae2fd9fb97315234030`, complete 74-line body.

All source-line anchors below refer to those literal `S1`, `S2`, and `S3` labels, not packet physical-line numbers.

### Method boundary

All reconstruction below is symbolic written algebra with the integer parameter \(s\ge4\). No new selected mathematical instance, scientific code, interpreter, CAS, enumeration, solver, or replay was used. I did not open current siblings, prior reviewer bodies, linked checkers, author code, or held mathematical payloads.

S2 contains historical finite-experiment descriptions and links; these were read as part of the mandatory complete packet but are **not premises** of this reconstruction.

The observation `2026-10-30T10:41:03-0700 PDT` and the pin/byte/LF statements belong to the parent’s live-metadata supply. They are not my native start, completion, or elapsed-time observations. The cutoff remains `2026-10-31T21:23:27Z`.

Repository materialization was not attempted under this read-only role. This is the complete review body for parent materialization, not a reference to an earlier message.

## 2. Exact mathematical scope and imports

The presentation is
\[
A(3,s)=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-3&-s&2
\end{pmatrix},
\qquad S=G_{\mathcal C}/J,
\]
with the book’s full Cartan realization and **all positive and negative Serre relations** in \(J\).

The assigned universal statement is:
\[
s\in\mathbb Z,\quad s\ge4
\quad\Longrightarrow\quad
\overline A_4
\text{ is invertible on every }S_{(a,1,4)},\ a\ge0.
\]
It entails the candidate’s \(a\ge1\) assertion at this grade, without asserting that every component is nonzero.

The following remain named imports rather than independently reconstructed manuscripts:

1. **f276 actual-source/whole-ideal bridge**, at the stated disposition SHA256  
   `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e`.  
   Its use is precisely the ordinary positive-source model and exclusion of additional positive relations from negative Serres, including the stated \(J/K=P_+\oplus P_-\) boundary. Positive degree counting alone would not establish this.
2. **f306 contraction interface:** actual theta-duals, normalized finite-Levi inverse Gram, coevaluation, and the consuming bracket.
3. **f314 generalized-primary interface:** needed only for the corresponding projected-seed corollary, with the whole two-seed ideal and full generalized zero-primary space.
4. Ordinary finite-type Chevalley–Serre, PBW, and finite-dimensional \(\mathfrak{sl}_2\) representation theory.
5. S2’s adopted actual horizontal-\((1,1)\) source/basis result. I also reconstruct the required grade-four horizontal matrix below; its earlier finite corroboration is not used.

**Anchors:** S1 LF 67–99, 129–197; S2 LF 19–39; S3 LF 19–38, 62–74.

## 3. Whole grade-four source and decomposition

### 3.1 Why no relevant Serre closure is omitted

Put
\[
v=e_2,\qquad w=E_1v,\qquad
M=\bigoplus_{a,n\ge0}S_{(a,1,n)}.
\]
Nodes 1 and 3 form finite type \(G_2\). The positive presentation linearized at exactly one \(e_2\) gives
\[
M\cong
U(\mathfrak n_{13}^{+})v/
\left(
U(\mathfrak n_{13}^{+})E_1^2v+
U(\mathfrak n_{13}^{+})E_3^{s+1}v
\right).
\]

The relevant positive Serres are accounted for as follows:

- The \(e_2\)-count-zero Serres give the acting finite-type algebra.
- \(E_1^2v\) is the \(e_2\)-count-one node-1 relation.
- \(E_3^{s+1}v\), with its entire positive closure, is the other \(e_2\)-count-one relation.
- The remaining positive seeds have at least two \(e_2\)’s and cannot contribute to this positive homogeneous slice.
- Exclusion of extra relations coming from the negative ideal is exactly the f276 import, not an independent conclusion from this list.

Define root vectors
\[
t=e_3,\quad z=[e_1,t],\quad d=[t,z],\quad
p=[t,d],\quad q=[z,d],
\]
and their adjoint actions \(T,Z,D,P,Q\).

For the node-1 parabolic nilradical,
\[
\mathfrak n_1=\langle t,z\rangle,\qquad
\mathfrak n_2=\langle d\rangle,\qquad
\mathfrak n_3=\langle p,q\rangle.
\]
The nonzero nilradical brackets are
\[
[T,Z]=D,\qquad [T,D]=P,\qquad [Z,D]=Q;
\]
\(P,Q\) commute with this nilradical.

Ordering the nilradical before \(E_1\), and imposing \(E_1^2v=0\), gives
\[
M_n\cong U(\mathfrak n)_n\otimes\langle v,w\rangle
\qquad(n\le s).
\]
The remaining seed starts at grade \(s+1\), and its positive closure cannot lower the grade. Since \(s\ge4\), this is the exact grade-four source, including the boundary \(s=4\).

**Status: SUPPORTED, conditional on f276.**  
**Anchors:** S1 LF 103–197.

### 3.2 Complete node-1 decomposition

Write \(V_k\) for the node-1 irreducible of lowest weight \(-k\). Then
\[
\mathfrak n_1\simeq V_1,\qquad
\mathfrak n_2\simeq V_0,\qquad
\mathfrak n_3\simeq V_1,\qquad
\langle v,w\rangle\simeq V_1.
\]

Equivariant PBW symmetrization gives
\[
M_4\simeq
\left(
\operatorname{Sym}^4V_1
\oplus\operatorname{Sym}^2V_1
\oplus V_0
\oplus(V_1\otimes V_1)
\right)\otimes V_1.
\]
Its four contributions are
\[
(V_5\oplus V_3)
\oplus(V_3\oplus V_1)
\oplus V_1
\oplus(V_3\oplus V_1\oplus V_1).
\]
Therefore
\[
\boxed{M_4\simeq V_5\oplus3V_3\oplus4V_1.}
\]

The dimension is \(6+12+8=26\).

On \(S_{(a,1,4)}\), the node-1 weight is \(2a-5\). Thus the horizontal-\((1,1)\) slice has weight \(-3\), which occurs in \(V_5\) and \(V_3\), but not \(V_1\). It detects exactly the \(V_5\oplus3V_3\) multiplicity operators and misses the four \(V_1\)’s.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 363–412.

### 3.3 Complete basis for the missed multiplicity space

Set
\[
L=Tw-Zv.
\]
With \(e=E_1\) and \(g=F_1\), the relations
\[
gT= Tg,\quad [g,Z]=T,\quad gw=v,\quad gv=0
\]
give \(gL=0\). Similarly, \([e,T]=Z\), \([e,Z]=0\), and \(ew=0\) give \(eL=0\).

Consider
\[
A=DTL,\qquad B=D^2v,\qquad C=PL,\qquad
H=(TQ-ZP)v.
\]
Each has degree \((2,1,4)\), hence node-1 weight \(-1\). Each is killed by \(g\); for \(H\),
\[
gH=TPv-TPv=0.
\]

Their PBW independence can be seen explicitly. With the root order \(T,Z,D,P,Q\),
\[
\begin{aligned}
A&=(T^2D-2TP)w-TZDv+TQv+ZPv,\\
B&=D^2v,\\
C&=TPw-ZPv,\\
H&=TQv-ZPv.
\end{aligned}
\]
Successive coefficients of \(T^2Dw\), \(D^2v\), \(TPw\), and \(TQv\) force every linear dependence coefficient to vanish.

The decomposition above shows that the kernel of \(g\) at weight \(-1\) has dimension four: precisely one lowest vector from each \(V_1\), with none from \(V_5\) or \(V_3\). Hence these vectors exhaust the missing multiplicity space.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 479–488, 685–698.

## 4. Normalized Gram, actual duals, and the full consuming operator

### 4.1 Mixed Gram normalization

Use the candidate’s normalized level-one letters \(u_0,\ldots,u_7\). In the finite Levi module generated by \(u_0=e_3\), normalize its contravariant form by \((u_0,u_0)=1\), with \(E_i^*=F_i\) for \(i=1,2\).

For the two zero-horizontal-weight letters,
\[
u_3=E_1E_2u_0,\qquad u_4=E_2E_1u_0,
\]
the actual Levi lowerings are
\[
F_1u_3=2u_2,\quad F_1u_4=u_2,\qquad
F_2u_3=u_1,\quad F_2u_4=2u_1.
\]
Consequently,
\[
(u_3,u_3)=2,\qquad
(u_3,u_4)=1,\qquad
(u_4,u_4)=2.
\]
The normalized extremal letters have norm one; for example,
\[
u_5=-\tfrac12E_1u_3,\qquad F_1u_5=-u_3
\]
gives \((u_5,u_5)=1\). The \(u_6,u_7\) normalization works similarly.

Thus
\[
G_{\{3,4\}}=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{\{3,4\}}^{-1}
=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]
and all singleton inverse-Gram entries are \(+1\).

This is the finite-Levi normalization used by f306, not a positive invariant form on the whole nonsymmetrizable algebra.

### 4.2 Actual dual operators and consuming formula

Put
\[
f=F_3,\qquad g=F_1,\qquad R=F_2.
\]
The actual reversed-order theta-duals are
\[
\begin{aligned}
W_0&=f,&W_1&=[f,g],&W_2&=[f,R],\\
W_3&=[W_2,g],&W_4&=[W_1,R],&
W_5&=-\tfrac12[W_3,g].
\end{aligned}
\]

On \(b=1,n=4\), \(W_6,W_7\) have negative \(b\) and positive third degree, so triangular support makes their targets zero. All remaining terms must be retained:
\[
\begin{aligned}
\overline A_4={}&A^0+\operatorname{ad}(u_2)W_2\\
&+\frac13\left[
\operatorname{ad}(u_3)(2W_3-W_4)
+\operatorname{ad}(u_4)(-W_3+2W_4)
\right]
+\operatorname{ad}(u_5)W_5,\\
A^0={}&Tf+ZW_1.
\end{aligned}
\]
The letters consume the lowerings through
\[
u_2=-Tv,\quad u_3=-Zv-Tw,\quad
u_4=-Zv,\quad u_5=Zw.
\]

In particular, the mixed terms are neither diagonal-only nor replaceable by separate seed ranks.

**Status: SUPPORTED at the f306 interface.**  
**Anchors:** S1 LF 201–279.

### 4.3 Equivariance, including terms active only after raising

The relevant node-1 tables are
\[
\begin{array}{c|rrrrrr}
i&0&1&2&3&4&5\\ \hline
eu_i&u_1&0&u_3&-2u_5&-u_5&0\\
[e,W_i]&0&-W_0&0&-2W_2&-W_2&W_3\\
gu_i&0&u_0&0&2u_2&u_2&-u_3\\
[g,W_i]&-W_1&0&-W_3&2W_5&W_5&0.
\end{array}
\]
The \(e\)-commutator of the \(u_2W_2\) term is \(u_3W_2\); that of the mixed block is
\[
-u_3W_2-u_5W_3;
\]
that of \(u_5W_5\) is \(u_5W_3\). They cancel. The \(g\)-commutators cancel in the same way. The \(A^0\) pair is separately equivariant.

Therefore the **full** operator commutes with node-1 \(\mathfrak{sl}_2\). Although \(W_5X=0\) for the four lowest vectors below, it cannot be deleted on their whole \(V_1\) isotypic component. Indeed, when \(W_2X=c_Xq\),
\[
W_5(eX)=-W_3X=c_Xp.
\]
Its contribution after raising is included by the full equivariance identity.

This verifies the consuming-side integration needed to pass from a lowest multiplicity matrix to all its raised vectors.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 281–305.

## 5. Actual \(F_3,F_1,F_2\) reconstruction

### 5.1 Root identities

The identities used here follow from the displayed Cartan convention and Jacobi:
\[
\begin{gathered}
[f,T]=-H_3,\quad [f,Z]=-3e,\quad
[f,D]=4Z,\quad [f,P]=3D,\quad [f,Q]=0,\\
[g,T]=0,\quad[g,Z]=T,\quad[g,D]=[g,P]=0,\quad[g,Q]=P.
\end{gathered}
\]
Also
\[
fv=fw=0,\qquad gv=0,\quad gw=v,\qquad
fL=(s+6)w.
\]
For example,
\[
f(Tw)=(s+3)w,\qquad f(Zv)=-3w,
\]
so \(fL=(s+6)w\).

Write \(k=s+6\).

### 5.2 Complete simple-lowering table

Applying those identities gives
\[
\begin{array}{c|l|l}
X&fX&gfX\\ \hline
A&4ZTL+(s+1)DL+kDTw&4T^2L+kDTv\\
B&8ZDv-4Qv&8TDv-4Pv\\
C&3DL+kPw&kPv\\
H&(s+3)Qv+3Pw-3ZDv&kPv-3TDv.
\end{array}
\]

For instance,
\[
fA=4ZTL+D\bigl((s+1)L+kTw\bigr),
\]
and
\[
fB=4(ZD+DZ)v=8ZDv-4Qv.
\]
For \(H\), the term \(-3ePv\) from \(f(ZPv)\) must retain
\[
ePv=Qv+Pw;
\]
this produces the stated \(Qv\) and \(Pw\) coefficients.

Because \(gX=0\) for all four columns,
\[
W_1X=-gfX.
\]

**Status: SUPPORTED.**  
**Anchors:** S1 LF 512–527, 700–719.

### 5.3 The actual \(F_2\) action

\(R=F_2\) commutes with \(E_1,E_3\), and
\[
Rv=-h_2,\qquad Rw=-e_1.
\]
Thus the applicable rule is
\[
R(Uv)=-Uh_2,
\]
not an auxiliary adjoint chosen on \(M\).

For a positive \(\mathfrak g_{13}\)-root vector of degree \((a,n)\),
\[
[h_2,x]=-(a+n)x.
\]
The required complete intermediate reductions are
\[
\begin{array}{c|c}
Y&RY\\ \hline
L&3z\\
TL&3d\\
T^2L&3p\\
DL&-3q\\
ZTL&3q\\
DTw&-q\\
DTv&p\\
TDv&-3p\\
ZDv&-3q\\
Pv&-4p\\
Pw&q\\
Qv&-5q.
\end{array}
\]
The distinct values of \(R(DTv)\) and \(R(TDv)\) retain the noncommutativity \([T,D]=P\).

These imply
\[
\begin{array}{c|rrrr}
X&A&B&C&H\\ \hline
RfX/q&3-4s&-4&s-3&-(5s+3)\\
RgfX/p&s+18&-8&-4s-24&-4s-15.
\end{array}
\]

All four \(RX\) vanish. Directly,
\[
RA=3[d,d]=0,\quad RB=0,\quad
RC=3[p,z]=0,
\]
and
\[
RH=-5[t,q]+4[z,p]=0.
\]
This also agrees with the absence of grade-four positive roots in \(\mathfrak g_{13}\).

### 5.4 Retaining the \(W_1R\) term correctly

The operator identity is always
\[
W_4=[W_1,R]=W_1R-RW_1.
\]
Here \(RX=0\) is proved on the grade-four source, so
\[
W_4X=RgfX.
\]
This is a legitimate domain-specific zero, not deletion of \(W_1R\) as an operator.

The distinction matters already in the packet’s generic grade-three \(G_2\) family:
\[
x=-DL,\qquad y=Pw-Qv.
\]
The same actual rules give
\[
Rx=3q,\qquad Ry=6q,\qquad W_1q=3d.
\]
Hence \(W_1Rx=9d\) and \(W_1Ry=18d\), which must be added to
\[
Rgf x=3(s+2)d,\qquad Rgf y=-9d.
\]
This recovers
\[
W_4x=3(s+5)d,\qquad W_4y=9d.
\]
Thus the source’s caution about \(W_1F_2\) is correct; it cannot be generalized away from the particular grade-four vanishing just established.

### 5.5 Complete surviving dual-lowering table

Set \(W_2X=c_Xq\), \(W_4X=d_Xp\). Since \(RX=gX=0\),
\[
W_2X=-RfX,\qquad
W_3X=-gW_2X=-c_Xp,\qquad
W_5X=\tfrac12gW_3X=0.
\]
Therefore
\[
\boxed{
\begin{array}{c|rrrr}
X&A&B&C&H\\ \hline
c_X&4s-3&4&3-s&5s+3\\
d_X&s+18&-8&-4s-24&-4s-15.
\end{array}}
\]
Together with \(W_0X=fX\), \(W_1X=-gfX\), and the triangular-support zeros for \(W_6,W_7\), this accounts for every lowering in the consuming formula.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 490–510, 622–643, 746–778.

## 6. Two-term matrix and full mixed-Gram consumption

### 6.1 Reconstruction of \(A^0\)

Using \(A^0X=TfX-ZgfX\), the complete columns are
\[
\begin{aligned}
A^0A&=(2s+11)A+(s+6)B+(2s+7)C-(s+6)H,\\
A^0B&=8B-4H,\\
A^0C&=3A+(s+9)C,\\
A^0H&=-3B+3C+(s+3)H.
\end{aligned}
\]

One useful noncommutative reduction for the first column is
\[
TDTw-ZDTv=A+B+C-H.
\]
Together with \(TDL=A+C\), this yields the stated first column without commuting \(T,D,Z\) illegally.

Hence, in \((A,B,C,H)\),
\[
\boxed{
A^0=
\begin{pmatrix}
2s+11&0&3&0\\
s+6&8&0&-3\\
2s+7&0&s+9&3\\
-(s+6)&-4&0&s+3
\end{pmatrix}.}
\]

**Status: SUPPORTED.**  
**Anchors:** S1 LF 721–744.

### 6.2 Actual consuming brackets

Since \(p,q\) commute with the nilradical,
\[
[u_2,q]=TQv,
\]
and
\[
[u_3,p]=TPw+ZPv,\qquad
[u_4,p]=ZPv.
\]

For a column with
\[
W_2X=cq,\quad W_3X=-cp,\quad W_4X=dp,\quad W_5X=0,
\]
the full correction is therefore
\[
\begin{aligned}
(\overline A_4-A^0)X
={}&cTQv\\
&+\frac13\left[
(-2c-d)(TPw+ZPv)+(c+2d)ZPv
\right]\\
={}&-\frac{2c+d}{3}(TPw-ZPv)+c(TQv-ZPv).
\end{aligned}
\]
Thus
\[
\boxed{(\overline A_4-A^0)X=-\frac{2c+d}{3}C+cH.}
\]

This calculation explicitly consumes the second-arm lowering and **both** mixed inverse-Gram columns.

Substituting the four pairs gives
\[
\begin{aligned}
\Delta A&=-(3s+4)C+(4s-3)H,\\
\Delta B&=4H,\\
\Delta C&=(2s+6)C+(3-s)H,\\
\Delta H&=(3-2s)C+(5s+3)H.
\end{aligned}
\]

Adding these to the preceding columns gives exactly
\[
\boxed{
K_4=
\begin{pmatrix}
2s+11&0&3&0\\
s+6&8&0&-3\\
3-s&0&3s+15&6-2s\\
3s-9&0&3-s&6s+6
\end{pmatrix}.}
\]

**Status: SUPPORTED.**  
**Anchors:** S1 LF 780–810.

## 7. Exact determinant and the missing \(V_1\) isotypic component

The \(B\)-column is \((0,8,0,0)^T\), so
\[
\det K_4
=8\det
\begin{pmatrix}
2s+11&3&0\\
3-s&3s+15&6-2s\\
3s-9&3-s&6s+6
\end{pmatrix}.
\]
Let \(u=s-3\), retaining the entire symbolic family. The smaller determinant is
\[
\begin{aligned}
&(2u+17)\bigl((3u+24)(6u+24)-2u^2\bigr)+72u\\
&=(2u+17)(16u^2+216u+576)+72u\\
&=32u^3+704u^2+4896u+9792\\
&=32(s^3+13s^2+48s+18).
\end{aligned}
\]
Consequently,
\[
\boxed{\det K_4=256(s^3+13s^2+48s+18)>0\qquad(s\ge4).}
\]

This proves invertibility of the multiplicity operator. Node-1 equivariance makes its action on \(4V_1\) the identity on \(V_1\) tensored with this multiplicity operator. Thus the **whole eight-dimensional missing isotypic component** is covered, not merely its four lowest vectors.

No positive-real-spectrum assertion for \(K_4\) is used or established here.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 814–842.

## 8. Independent reconstruction of the remaining detected block

Use S2’s actual basis
\[
\zeta_i=[X_i,Y_{4-i}],\qquad
X_i=T^ie_1,\quad Y_j=T^jv,\qquad i=0,1,2,3.
\]
Here \(X_4=0\) and \(s\ge4\), so these are precisely the four horizontal-\((1,1,4)\) basis vectors.

Let \(\eta_i=[X_i,Y_{3-i}]\). The string identities give
\[
f\zeta_i
=i(4-i)\eta_{i-1}+(4-i)(s-3+i)\eta_i,
\qquad
T\eta_i=\zeta_i+\zeta_{i+1}.
\]
Thus
\[
Tf=
\begin{pmatrix}
4(s-3)&3&0&0\\
4(s-3)&3s-3&4&0\\
0&3(s-2)&2s+2&3\\
0&0&2(s-1)&s+3
\end{pmatrix}.
\]

For the first-arm dual,
\[
g\zeta_0=5Y_4,\qquad g\zeta_1=-Y_4,\qquad
g\zeta_2=g\zeta_3=0.
\]
Using \(W_1=fg-gf\),
\[
W_1\zeta_i=\alpha_iY_3,\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\bigl(4(s-3),-s-6,4,0\bigr).
\]
Since \(u_1=z=-X_1\),
\[
[u_1,Y_3]=-\zeta_1.
\]

For the second arm, \(R\zeta_i=0\), while
\[
R\eta_0=R\eta_1=0,\qquad
R\eta_2=X_3,\qquad R\eta_3=-4X_3.
\]
It follows that
\[
W_2\zeta_i=\beta_iX_3,\qquad
(\beta_0,\beta_1,\beta_2,\beta_3)
=\bigl(0,0,-2(s-1),4s-3\bigr).
\]
Also \([u_2,X_3]=\zeta_3\).

The mixed \(W_3,W_4\) targets at this horizontal degree have \(a=0,n=3\), hence are zero; the remaining higher-horizontal targets are likewise absent. Adding the two actual rank-one corrections to \(Tf\) gives
\[
\boxed{
D_4=
\begin{pmatrix}
4(s-3)&3&0&0\\
0&4s+3&0&0\\
0&3(s-2)&2s+2&3\\
0&0&0&5s
\end{pmatrix}.}
\]
Its determinant is
\[
4(s-3)(4s+3)(2s+2)(5s)>0
\qquad(s\ge4).
\]

This verifies the candidate’s displayed detected matrix. By the detection lemma and equivariance, it covers the whole \(V_5\oplus3V_3\) component.

Together with \(K_4\), this exhausts \(M_4\). More explicitly, the weight dimensions for \(a=0,\ldots,5\) are
\[
1,\ 4,\ 8,\ 8,\ 4,\ 1;
\]
other \(a\ge0\) components are zero. Hence every \(a\) in the assigned universal statement is covered.

**Status: SUPPORTED.**  
**Anchors:** S1 LF 394–412, 844–859; S2 LF 21–35.

## 9. Author’s nonvacuous \(B_2\) example, compared as written

This comparison concerns the example already selected and stated by the author; it is not a newly selected diagnostic.

For the packet’s generic \(B_2\) family \(r=2,s\ge3\), \(d\) is central in the parabolic nilradical and
\[
x=-DL
\]
is its missing grade-three \(V_0\). The actual identities give
\[
fx=-2ZL-(s+4)Dw,\qquad
gfx=-2TL-(s+4)Dv.
\]
Consequently,
\[
A^0x=(s+6)x.
\]
Moreover,
\[
Rx=0,\qquad W_2x=W_3x=W_5x=0,\qquad
W_4x=3(s+2)d.
\]
Because \(2u_4-u_3=L\) and \([L,d]=x\), the full mixed correction is \((s+2)x\). Therefore
\[
\overline A_3x=(2s+8)x.
\]

The packet’s horizontal block is
\[
\begin{pmatrix}
3(s-2)&2&0\\
0&3s+2&0\\
0&0&4s
\end{pmatrix}.
\]
The decomposition \(V_4\oplus2V_2\oplus V_0\) shows that raising the three horizontal weight-\(-2\) basis vectors gives an independent three-dimensional weight-zero space; \(x\) supplies the independent \(V_0\).

Accordingly, the author’s stated
\[
(r,s,a,b,n)=(2,3,2,1,3)
\]
component has dimension four, third weight \(-1\), and the stated blocks
\[
\begin{pmatrix}3&2&0\\0&11&0\\0&0&12\end{pmatrix},
\qquad (14).
\]
Its listed eigenvalues \(3,11,12,14\) agree with the written generic formulas. This is a valid nonvacuity comparison outside the older positive-third-weight strip; it is not executed finite evidence.

**Status: SUPPORTED as the author’s stated comparison.**  
**Anchors:** S1 LF 531–586, 934–961.

## 10. Claimwise disposition and limits

| Claim | Disposition | Exact boundary |
|---|---|---|
| Grade-four source has no omitted relevant Serre closure | **SUPPORTED, conditional** | Full positive closure plus named f276 negative-ideal/source bridge; \(r=3,\ s\ge4\) |
| \(M_4=V_5\oplus3V_3\oplus4V_1\) | **SUPPORTED** | Equivariant PBW at grade \(4\le s\) |
| Horizontal weight \(-3\) misses precisely four \(V_1\)’s | **SUPPORTED** | Complete node-1 decomposition |
| \(A,B,C,H\) form the entire missing lowest multiplicity basis | **SUPPORTED** | Explicit PBW independence and dimension four |
| Normalized mixed inverse Gram and consuming formula | **SUPPORTED at named interface** | Finite-Levi normalization/f306, not a whole-algebra positive form |
| Actual \(f,g,R\) and \(W_2,W_3,W_4,W_5\) tables | **SUPPORTED** | Entire symbolic family; full \(W_1R\) retained before its grade-four vanishing |
| Displayed \(A^0\), correction columns, and \(K_4\) | **SUPPORTED** | Ordered basis \((A,B,C,H)\) |
| \(\det K_4=256(s^3+13s^2+48s+18)>0\) | **SUPPORTED** | Every integer \(s\ge4\) |
| Remaining detected matrix \(D_4\) | **SUPPORTED** | Actual horizontal basis, then node-1 saturation |
| Invertibility on every \(S_{(a,1,4)}\) | **SUPPORTED, conditional** | \(r=3,\ s\ge4,\ a\ge0\), including zero spaces |
| Author’s stated \(B_2\) nonvacuity example | **SUPPORTED as written** | Comparison above; not a new experiment |
| Positive real spectrum of the new \(K_4\) block | **NOT ESTABLISHED OR REQUIRED** | Nonzero determinant is sufficient |
| Whole f383 one-arm theorem at all other grades and parameters | **NOT DISPOSED BY THIS SLICE** | Other assigned gates and parent assembly remain separate |
| Global \(J=\tau\), whole-level \(B_8=0\), novelty, original-source authenticity | **NOT ESTABLISHED** | No such extension follows from this review |

For the assigned components, invertibility gives
\[
\ker\overline{\mathcal C}_4=0,\qquad
\operatorname{im}\overline{\mathcal C}_4\cap\ker\overline\mu_4=0,
\qquad
\ker\overline A_4^{\,k}=0\quad(k\ge1).
\]
The projected-seed equality follows **only through the named f314 identification**, retaining the complete two-seed ideal and full generalized primary. This review does not independently reconstruct that interface or certify a global radical equality.

There is no missing mathematical step within the assigned grade-four reconstruction once its explicitly allowed imports are retained. The underlying f276/f306/f314 manuscripts remain imports, not newly verified results.

No finite-slice code or argv is supplied because this assignment is **WRITTEN**, not FINITE; no executable was generated or run. Parent execution or independent-family verification must not be inferred from this return.

**Overall correctness:** correct at the assigned conditional scope.

**Explanation:** The complete symbolic reconstruction agrees with the candidate’s grade-four basis, actual lowerings, mixed-Gram consumption, full matrix, determinant, and detected-block coverage. No defect was found in this slice; whole-candidate adoption and broader claims require their separate gates and parent disposition.

**Confidence:** 0.97.