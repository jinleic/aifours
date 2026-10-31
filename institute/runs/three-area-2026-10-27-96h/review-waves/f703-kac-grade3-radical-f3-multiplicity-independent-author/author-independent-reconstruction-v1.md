# Grade-three radical: nonblind independent reconstruction at the actual source

**AUTHOR RECONSTRUCTION; UNADOPTED.** This is a same-harness, nonblind reconstruction of the supplied f696 candidate, with the named source interfaces imported at their stated scopes. It is not an independent-model-family review, a kernel proof, or a parent disposition. The native clock observed before this file was created was 2026-10-30T16:44:13-0700 PDT; that observation is not an asserted completion time.

## 1. Quantifiers, objects, and imports

Fix
\[
 A(r,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-r&-s&2\end{pmatrix},\quad
 r\in\{1,2,3\},\quad s\in\mathbb Z,\quad s>r,
\]
and **every** full complex Cartan realization of it as in packet S2. In the preliminary Chevalley algebra let \(\tau\) be its maximal ideal disjoint from the full Cartan, and let \(J\) be the ideal of **both signs of all** Serre relations. Write \(S=G_{\mathcal C}/J\), \(\mathcal R=\tau/J\), and
\(S_n=\bigoplus_{a,b\geq0} S_{(a,b,n)}\).

The reconstructed conditional result is
\[
 \mathcal R\cap S_3=0,\qquad
 J_{(a,b,3)}=\tau_{(a,b,3)}\quad\text{for all }a,b\geq0.
\]
It is conditional on the following actual, not merely model, imports from the full packet:

* S3: full-Cartan injection; the actual positive piece as the ordinary free Lie algebra on the eight-dimensional Levi module after the fixed Serres; the positive/negative whole-Serre-ideal bridge; and \(J\subseteq\tau\). Its named classical import is the characteristic-zero tensor embedding/free-Lie theorem.
* S4: for this exact parameter domain and actual whole-Serre quotient, \(\mathcal R\cap S_2=0\), including every root component. The eight-channel normalization is also an S4 interface. Neither fact is re-proved here as a claim about the preliminary algebra.
* Finite-dimensional \(\mathfrak{sl}_3\) semisimplicity and the Weyl character formula are used explicitly. S5 is an adopted second-arm interface, not an assumption that the whole grade-three result already holds.

S2's larger family and level-four obligation, sourcebook authentication, higher grades, and global \(J=\tau\) are not established. No conclusion follows merely from a contraction spectrum.

## 2. Actual letters, complete quotient, and characters

Let \(E_i=\operatorname{ad}e_i\), \(F_i=\operatorname{ad}f_i\), and write
\[
 (x,a,b,c,d,e,f,g)=(u_0,u_1,u_2,u_3,u_4,u_5,u_6,u_7),
\]
where \(x=e_3\), \(a=E_1x\), \(b=E_2x\), \(c=E_1E_2x\), \(d=E_2E_1x\), \(e=-\tfrac12E_1^2E_2x\), \(f=\tfrac12E_2^2E_1x\), and \(g=E_1f\). These are letters of \(V=L_{\rm low}(1,1)\), not matrix products. Their horizontal degrees are respectively
\((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)\).
The source table, which fixes all signs, is
\[
\begin{array}{c|rrrrrrrr}
 &x&a&b&c&d&e&f&g\\\hline
 E_1&a&0&c&-2e&-e&0&g&0\\
 E_2&b&d&0&f&2f&-g&0&0\\
 F_1&0&x&0&2b&b&-c&0&f\\
 F_2&0&0&x&a&2a&0&d&-e
\end{array}.
\]

Set \(q=[x,a]\), \(q'=[x,b]\), and \(Q=U(\mathfrak{sl}_3)q\cong L_{\rm low}(0,3)\). The ordinary free-Lie description in S3 gives, with the entire indicated cyclic modules imposed,
\[
\begin{array}{c|l}
(r,s)&S_3\\\hline
r=3&\operatorname{Lie}_3(V)\\
r=2&\operatorname{Lie}_3(V)/U(\mathfrak{sl}_3)[x,q]\\
r=1,\ s\ge3&\operatorname{Lie}_3(V)/[V,Q]\\
(1,2)&\operatorname{Lie}_3(V)/([V,Q]+U(\mathfrak{sl}_3)[x,q']).
\end{array}
\]
For \(r=1\), \(S_2=\Lambda^2V/Q\); for \(r=2,3\), \(S_2=\Lambda^2V\). Here \([V,Q]\) is the bracket with **all ten dimensions** of \(Q\). This is the actual quotient because the imported bridge excludes further positive consequences of the negative Serres.

The decomposition follows from
\[
\begin{aligned}
\Lambda^2V&=L(0,3)\oplus L(3,0)\oplus L(1,1),\\
\Lambda^3V&=L(0,0)\oplus L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus L(2,2),\\
V\otimes L(0,3)&=L(1,4)\oplus L(2,2)\oplus L(0,3)\oplus L(1,1),\\
V\otimes V&=L(0,0)\oplus2L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus L(2,2).
\end{aligned}
\]
Indeed \(\operatorname{Lie}_3(V)=(V\otimes\Lambda^2V)/j(\Lambda^3V)\), with
\(j(v\wedge w\wedge z)=v\otimes(w\wedge z)+w\otimes(z\wedge v)+z\otimes(v\wedge w)\). The wedge projection takes \(j\) to three times the identity, so it is injective. The character identities can be obtained from the eight weights of \(V\), exterior-power generating functions, and the Weyl formula. Thus the free module is
\[
3L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus2L(2,2)\oplus L(1,4)\oplus L(4,1),
\quad \dim=168.
\]

For the whole \([V,Q]\) claim, define
\(Q_1=E_2q\), \(Q_2=E_2^2q\), \(Q_3=E_1E_2q\), \(Q_4=E_1E_2^2q\). From the table,
\[
\begin{aligned}
Q_1&=[b,a]+[x,d],&Q_2&=2([b,d]+[x,f]),\\
Q_3&=[c,a]+[a,d]-[x,e],&
Q_4&=2([x,g]+[a,f]-[b,e]+[c,d]).
\end{aligned}
\]
Their nonzero lowerings are \(F_1Q_3=Q_1\), \(F_1Q_4=2Q_2\), \(F_2Q_1=3q\), \(F_2Q_2=4Q_1\), \(F_2Q_4=4Q_3\). Put
\[
\begin{aligned}
T_{35,r}&=[x,q],\\
T_{27,r}&=3[b,q]-[x,Q_1],\\
T_{10,r}&=[c,q]-2[d,q]+[a,Q_1]-[x,Q_3],\\
T_{8,r}&=[x,Q_4]-2[a,Q_2]-4[b,Q_3]+4[d,Q_1]-12[f,q].
\end{aligned}
\]
The lowering table makes these lowest of types \((1,4),(2,2),(0,3),(1,1)\), respectively. Their nonzero free-Lie words containing \([x,[x,a]]\), \([x,[x,d]]\), \([x,[x,e]]\), and \([x,[x,g]]\), respectively, establish nonvanishing: the indicated letter is unique to that term. The tensor embedding makes the nonzero assertion literal. Since the four types occur once in \(V\otimes Q\), the bracket map is injective, and \([V,Q]\) has dimension \(35+27+10+8=80\). The other seed \([x,q']\) is a nonzero lowest vector of type \((4,1)\); this type is absent from \([V,Q]\), so the two **whole** modules have zero intersection, including at \((1,2)\).

Consequently the actual decomposition and dimensions are
\[
\begin{array}{c|l|r}
(r,s)&S_3&\dim\\\hline
(1,2)&2L(1,1)\oplus L(3,0)\oplus L(2,2)&53\\
1,\ s\ge3&2L(1,1)\oplus L(3,0)\oplus L(2,2)\oplus L(4,1)&88\\
2,\ s\ge3&3L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus2L(2,2)\oplus L(4,1)&133\\
3,\ s\ge4&3L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus2L(2,2)\oplus L(1,4)\oplus L(4,1)&168.
\end{array}
\]

## 3. Exact all-root weight table, including overlaps

The following is a table of \(d(a,b)=\dim S_{(a,b,3)}\), not a table of nonoverlapping lowest-weight labels. In each displayed matrix rows are \(a=0,\ldots,6\) and columns are \(b=0,\ldots,6\); all other \(a,b\ge0\) give zero.
\[
\begin{array}{c|c}
(r,s)&(d(a,b))_{a,b=0}^6\\\hline
(1,2)&\begin{pmatrix}
0&0&0&0&0&0&0\\
0&1&2&1&0&0&0\\
0&1&5&5&1&0&0\\
0&1&5&8&5&1&0\\
0&0&2&5&5&2&0\\
0&0&0&1&1&1&0\\
0&0&0&0&0&0&0
\end{pmatrix}\\[3ex]
1,\ s\ge3&\begin{pmatrix}
0&1&1&0&0&0&0\\
0&2&4&2&0&0&0\\
0&2&7&7&2&0&0\\
0&2&7&10&7&2&0\\
0&1&4&7&7&4&1\\
0&0&1&2&2&2&1\\
0&0&0&0&0&0&0
\end{pmatrix}\\[3ex]
2,\ s\ge3&\begin{pmatrix}
0&1&1&0&0&0&0\\
0&3&5&3&0&0&0\\
0&4&11&11&4&0&0\\
0&3&11&16&11&3&0\\
0&1&5&11&11&5&1\\
0&0&1&3&4&3&1\\
0&0&0&0&0&0&0
\end{pmatrix}\\[3ex]
3,\ s\ge4&\begin{pmatrix}
0&1&1&0&0&0&0\\
1&4&6&4&1&0&0\\
1&6&13&13&6&1&0\\
0&4&13&18&13&4&0\\
0&1&6&13&13&6&1\\
0&0&1&4&6&4&1\\
0&0&0&0&1&1&0
\end{pmatrix}.
\end{array}
\]
A compact reproducible derivation is as follows. Let horizontal variables be \(X,Y\) and
\[
H=(1+X)(1+Y)(1+XY),\quad
P_{p,q}=\frac{1-X^{p+1}-Y^{q+1}+X^{p+q+2}Y^{q+1}+X^{p+1}Y^{p+q+2}-(XY)^{p+q+2}}
{(1-X)(1-Y)(1-XY)}.
\]
The quotient is a polynomial; \(P_{p,q}\) records all relative weights above the lowest weight of \(L(p,q)\). In particular
\(P_{0,3}=\sum_{k=0}^3\sum_{j=0}^{3-k}X^kY^{j+k}\).
The four characters, in the order of the table, are
\[
\begin{aligned}
&\tfrac13\{H^3-H(X^3,Y^3)\}-HX P_{0,3}-Y P_{4,1},\\
&\tfrac13\{H^3-H(X^3,Y^3)\}-HX P_{0,3},\\
&\tfrac13\{H^3-H(X^3,Y^3)\}-X P_{1,4},\\
&\tfrac13\{H^3-H(X^3,Y^3)\}.
\end{aligned}
\]
Thus every entry is a coefficient of the **actual quotient**, with overlaps added before subtraction of whole disjoint relation modules. Evaluation at \(X=Y=1\) gives 53, 88, 133, 168. In particular no component is counted twice merely because distinct irreducibles contain the same root weight.

## 4. Deriving actual \(F_3\) on all words

Let \(E_{12}=[E_1,E_2]\) and \(D_i=\operatorname{ad}(F_3u_i)|_V\). Chevalley brackets give
\[
 F_3(x,a,b,c,d,e,f,g)=(-h_3,-re_1,-se_2,-s[e_1,e_2],r[e_1,e_2],0,0,0).
\]
Thus on a letter of horizontal degree \((i,j)\),
\[
D_0=(ri+sj-2)I,\quad D_1=-rE_1,\quad D_2=-sE_2,\quad
D_3=-sE_{12},\quad D_4=rE_{12},\quad D_5=D_6=D_7=0.
\]
The needed commutator table begins
\(E_{12}(x,a,b,c,d,e,f,g)=(c-d,-e,-f,-g,g,0,0,0)\).
For any letters \(u,v,w\), with \(D_u\) extended linearly,
\[
F_3[u,v]=D_uv-D_vu,\quad
F_3[u,[v,w]]=[D_uv,w]+[v,D_uw]+[u,D_vw-D_wv].
\]
These are derivation identities in the actual quotient, not an inference from a matrix multiplication model. In particular the following intermediate values follow directly:
\[
\begin{array}{c|ccccc}
 &q&Q_1&Q_2&Q_3&Q_4\\\hline
F_3&2(r-1)a&2(r-1)d&4(r-1)f&-2(r-1)e&4(r-1)g
\end{array}.
\]
For \(r=1\), \(F_3Q=0\) because \([F_3,E_1]=[F_3,E_2]=0\), and \(F_3[V,Q]\subseteq Q\) by the derivation rule. The grade-three seeds at \(r=2\) and \(s=2\) have zero \(F_3\)-image; commutation with the raising operators gives zero on their entire cyclic modules. This explicitly agrees with descent to the displayed actual quotient; the whole-ideal bridge is still the import proving that this is the whole quotient.

## 5. Complete lowest multiplicity spaces

For primed formulas use the formal source relabeling
\[
(x',a',b',c',d',e',f',g')=(x,b,a,d,c,-f,-e,g),\quad
(E'_1,E'_2;r',s')=(E_2,E_1;s,r).
\]
This is a substitution in the displayed universal letter/action formulas, **not** an automorphism of the fixed nonsymmetric \(A(r,s)\). It supplies the other-side vectors \(T_{35,s}=[x,q']\), \(T_{27,s}=3[a,q']-[x,E_1q']\), and the primed versions \(T_{10,s},T_{8,s}\).

### 5.1 The two 35s and two 27s

The derivation rule immediately gives
\[
F_3T_{35,r}=3(r-2)q,\qquad F_3T_{35,s}=3(s-2)q'.
\]
The first module survives only at \(r=3\), and the second only at \(s>2\). Their images are nonzero in the corresponding actual \(S_2\).

Put \(A=[x,c]\), \(B=[x,d]\), \(C=[a,b]\). Direct derivation gives
\[
\begin{aligned}
F_3T_{27,r}&=(6-3r-4s)B+(2-5r+4s)C,\\
F_3T_{27,s}&=(6-4r-3s)A+(5s-4r-2)C.
\end{aligned}
\]
For example, \(F_3[b,q]=-s(B-C)-2(r-1)C\) and
\(F_3[x,Q_1]=(r+s-4)(B-C)+2(r-1)B\), which yields the first line. Both displayed \(A\)- and \(B\)-coefficients are strictly negative for the entire domain. For \(r=2,3\) there is no degree-two relation, so the two images are independent. For \(r=1\), \(T_{27,r}\in[V,Q]\), and the **entire** relation at this weight is \(\langle Q_1\rangle=\langle B-C\rangle\); the nonzero \(A\)-coefficient leaves the other image nonzero. This covers the complete surviving 27 multiplicity space.

### 5.2 Both 10s

Let \((A_r,B_r,C_r)=([c,a],[d,a],[x,e])\). The image is
\[
F_3T_{10,r}=(2-3r-2s)A_r+(2-r+2s)B_r+(-6+7r+2s)C_r.
\]
To reconstruct it, use \(Q_3=A_r-B_r-C_r\): its total coefficient before collecting the extra exterior pairs is \(4-5r-2s\); the extra coefficients on \((A_r,B_r,C_r)\) are \((2,-6,2)(r-1)\). For \(r=2,3\) its first coefficient is nonzero and there is no degree-two quotient.

For the primed vector the target pairs are
\((A_s,B_s,C_s)=([d,b],[c,b],-[x,f])\), and
\[
F_3T_{10,s}=(2-3s-2r)A_s+(2-s+2r)B_s+(-6+7s+2r)C_s.
\]
At \(r=1\), the whole degree-two relation at this weight is
\(\langle Q_2\rangle=\langle A_s+C_s\rangle\). Its \(A_s\) and \(C_s\) coefficients differ by \(8-10s-4r\ne0\). Thus this image is nonzero in the actual quotient, including \((1,2)\). Each surviving 10 occurs once.

### 5.3 All three possible adjoints and an exact determinant

Define
\[
Y=A-B-C,\quad Y_1=E_1Y,\quad Y_2=E_2Y,\quad Y_3=E_1E_2Y,
\quad Z=[x,Y_3]-2[a,Y_2]-[b,Y_1]+[d,Y].
\]
The action table gives \(F_1Y=F_2Y=0\),
\(F_1Y_1=Y\), \(F_2Y_2=Y\), \(F_1Y_3=2Y_2\), \(F_2Y_3=Y_1\), and the cross lowerings zero; substitution shows \(F_1Z=F_2Z=0\).

Write the unquotiented weight-\((2,2)\) exterior basis as
\[
P=[x,g],\quad Q=[a,f],\quad U=[b,e],\quad T=[c,d].
\]
The independent derivation uses
\[
\begin{aligned}
Q_4&=2(P+Q-U+T),\\
Y_1&=-[a,d]-[x,e],&Y_2&=[b,c]-[x,f],\\
Y_3&=-P-Q-2U,&E_2E_1Y&=P-2Q-U,\\
F_3Y&=(3r+2s-2)c-(2r+3s-2)d,\\
F_3Y_1&=(2-4r-s)e,&F_3Y_2&=(2-r-4s)f,&F_3Y_3&=(2-r-4s)g.
\end{aligned}
\]
For \(T_{8,r}\), use also \(E_2Q_3=E_{12}Q_1=Q_4/2\). Its image before expanding \(Q_4\) is
\[
(6r+4s-4)Q_4+4(r-1)P+16(r-1)Q+8(r-1)U.
\]
The formal swap sends \((P,Q,U,T)\) to \((P,-U,-Q,-T)\). The resulting complete coordinate vectors are
\[
\begin{aligned}
v_r=F_3T_{8,r}&=(16r+8s-12,\ 28r+8s-24,\ -4r-8s,\ 12r+8s-8),\\
v_s=F_3T_{8,s}&=(8r+16s-12,\ 8r+4s,\ 24-8r-28s,\ 8-8r-12s),\\
v_Z=F_3Z&=(6-7r-5s,\ 4s-r,\ 6-5r-4s,\ 2-3r-2s).
\end{aligned}
\]
The indicated \((P,Q,T)\)-minor is exactly
\[
\det(v_r,v_s,v_Z)_{P,Q,T}
=18(r+s-1)(8r+12s-8)(16r+8s-12)>0.
\]
For a transparent factorization, set \(\rho=r-1\), \(\sigma=s-1\),
\(C_0=12\rho+8\sigma+12\), \(D_0=8\rho+12\sigma+12\). One has
\(v_Z=-v_r/4+3(\rho+\sigma+1)(-1,2,-2,0)\). After this column operation the three-row determinant is \(6D_0(C_0+4\rho)\), producing the displayed product. Each factor is positive throughout the stated domain.

For \(r=2,3\), the three images are independent in the full exterior square; since the free decomposition has exactly three adjoints, their preimages span the **whole** lowest multiplicity space. For \(r=1\), the entire relation in this target weight is \(\langle Q_4\rangle\), and
\(v_r=(2+4s)Q_4\). The nonzero determinant proves that the classes of \(v_s,v_Z\) are independent modulo that whole line. The source vector \(T_{8,r}\) is killed by \([V,Q]\); hence these are the two surviving adjoints. The extra relation at \((1,2)\) is a disjoint \(L(4,1)\), so removes no adjoint. This is a rank statement on the **entire** multiplicity space, not on a preferred copy.

## 6. Ideal-stability proof, not a contraction argument

The imported S4 theorem gives \(\mathcal R\cap S_2=0\). Because \(\mathcal R\) is an ideal in the actual \(S\),
\[
 F_3(\mathcal R\cap S_3)\subseteq\mathcal R\cap S_2=0.
\]
The full Cartan separates root degrees, and \(\mathcal R\cap S_3\) is a finite-dimensional \(\mathfrak{sl}_3\)-submodule. By complete reducibility, a nonzero such submodule contains a nonzero lowest vector in one of the listed isotypic multiplicity spaces. Section 5 establishes that actual \(F_3\) is injective on **each whole** such space, including the double 27 and triple/two adjoints. This contradicts its vanishing on \(\mathcal R\cap S_3\). Hence \(\mathcal R\cap S_3=0\), and the root-graded equality \(J_{(a,b,3)}=\tau_{(a,b,3)}\) follows for every \(a,b\ge0\). Nothing here asserts that \(F_3\) is injective on all raised vectors or that the full contraction is invertible.

## 7. All eight contraction channels and the two 35 eigenvalues

This section is separate from the ideal proof. Put \(W_0=F_3\), \(W_1=[F_3,F_1]\), \(W_2=[F_3,F_2]\), \(W_3=[W_2,F_1]\), \(W_4=[W_1,F_2]\), \(W_5=-\tfrac12[W_3,F_1]\), \(W_6=\tfrac12[W_4,F_2]\), \(W_7=[W_6,F_1]\). On **every** actual \(z\in S_3\), the full coevaluation and its consuming bracket are
\[
\begin{aligned}
\overline A_3z={}&[x,W_0z]+[a,W_1z]+[b,W_2z]\\
&+\tfrac13\{[c,(2W_3-W_4)z]+[d,(-W_3+2W_4)z]\}\\
&+[e,W_5z]+[f,W_6z]+[g,W_7z].
\end{aligned}
\]
For the contravariant form normalized by \(\langle x,x\rangle=1\), the action table gives unit norm for \(x,a,b,e,f,g\) and the \((c,d)\) block \(\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)\); hence the displayed inverse block is \(\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)\). The Chevalley anti-involution identifies the \(W_i\) with the dual negative letters: \([E_j,\sigma(v)]=-\sigma(F_jv)\). The complete coevaluation is therefore Levi invariant; the consuming bracket is Levi-equivariant by Jacobi. This argument includes \(W_5,W_6,W_7\) and the mixed block on every raised vector.

On either 35 lowest vector \(T_{35,*}\), \(F_1T=F_2T=0\), and its \(F_3\)-image is a scalar multiple of the corresponding lowest \(q\) or \(q'\). Thus \(W_1T=W_2T=0\), and induction through the nested commutators yields \(W_3T=\cdots=W_7T=0\). The complete formula therefore gives \(3(r-2)T_{35,r}\) and \(3(s-2)T_{35,s}\); equivariance transports these scalars across the respective surviving irreducibles. It does **not** make the seven channels vanish on their raised vectors. Spectra and invertibility on the other isotypic pieces remain uncomputed and unpaid.

## 8. Access record and assurance ceiling

* Before body access, read the complete manifest, freeze receipt, final binding, parent-prepared metadata, actual dispatch, all 21 listed permission/quarantine controls, and the prospective multipart policy. Sent Main a direct pre-body ACK before any part access or derivation. All held episodes and all their consumers are noninput; status-only controls were not used as scientific sources.
* Read the sole part serially as raw windows 1–20, 21–40, ..., 461–480, 481–490, through its end. These render complete S1 LF1–286, S2 LF1–74, S3 LF1–27, S4 LF1–44, and S5 LF1–37. No part body was accessed in parallel. Outgoing links, sibling proofs, held history/methods, and old code were not followed or opened.
* The three assigned manifest/freeze/final-binding SHA256s independently observed were respectively `949e932dea176915486c23d548a50129ba11a26496d3470b3ec08f5d8439d1ae`, `40d6dfb23be7ceaca3d6e5c3ae0f1e7929e4af97fa102e51c0d86c019cfcc049`, and `00f804d3cd535bde1145fa18cdd2757e551d76cfb75b6e9a46956e63e5c910e1`. After reading, packet metadata was 490 LF, 47,657 bytes and SHA256 `f988c1d717274b1fbbf77692eb928221bd2d155ff3a6c5f94d40e08ee0eb16d4`, matching the frozen packet. These are metadata observations, not scientific verification.
* The displayed mathematical reconstruction is written/manual. Scientific child code, tests, builds, linters, formatters, external models, installations, Git and paid/heavy jobs were not run. The file is a prospective candidate for complete parent reading and separate disposition; no parent acceptance, cross-family/human/kernel verification, original-source identity, novelty, or automatic old-gate clearance is asserted. Access history is not a certificate about unobservable cognition.
