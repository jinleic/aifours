# F844: the entire r=2 two-copy lowest pencil has a constant minor

**Prospective GENERAL AUTHOR candidate, conditional on the explicit interfaces below; written reconstruction, not a parent disposition or an independent-family, human, formal/kernel, source-authentication, priority, or novelty claim.** This is a nonblind reconstruction of the packet's F831 formulas, together with an explicit constant equivalence to the different F832 output pencil. No scientific code was prepared or executed.

## 1. Exact statement and conditional inputs

For every integer \(s\ge3\), every full complex Cartan realization of
\[
 A(2,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-2&-s&2\end{pmatrix},
\]
let \(G\) be the preliminary Chevalley algebra at the displayed presentation, \(J\) the **whole ideal of both signs of all Serre relations**, \(S=G/J\), \(\tau\) the maximal ideal disjoint from the **whole** Cartan, and \(\mathcal R=\tau/J\). Denote \(S_{a,b,n}\) by the root \(a\alpha_1+b\alpha_2+n\alpha_3\), and put \(E_i=\operatorname{ad}e_i\), \(F_i=\operatorname{ad}f_i\). Lowest means the simultaneous \(F_1,F_2\) kernel in the **entire** indicated quotient, not a chosen summand.

**Candidate theorem.** Subject to the interfaces in the next paragraph, the whole grade-four \(L_{\mathrm{low}}(1,4)\) lowest multiplicity space is two-dimensional and actual \(F_3\) is injective on it, for every such \(s\). Consequently
\[
 (\mathcal R\cap S_4)_{L_{\mathrm{low}}(1,4)\text{-isotypic}}=0
 \qquad(s\in\mathbb Z,\ s\ge3). \tag{1}
\]
This includes every diagonal mixture of the two equivalent copies. It is not a claim about the entire grade-four radical, another isotypic type, higher grades, or global \(J=\tau\).

The load-bearing **conditional imports** are: (i) packet S7's ordinary free-Lie source on the actual eight-letter Levi module, the whole positive- and negative-Serre ideal bridge, root grading, and full-Cartan injection for this exact displayed presentation; and (ii) packet S10's \(\mathcal R\cap S_3=0\), itself conditional on the same source bridge and the entire-grade-two radical-zero interface in S9. The underlying operative presentation/bridge and grade-two proof bodies linked by these dispositions were not supplied as literal packet bodies; their conclusions are **not independently re-established here**. We also use characteristic-zero free-Lie tensor embedding and multigraded Witt dimensions, standard finite-dimensional \(\mathfrak{sl}_3\) complete reducibility/Pieri rules, and elementary finite-dimensional \(\mathfrak{sl}_2\) theory. The needed lowest ideal criterion is proved below. We do not assume preliminary-\(G\) PBW independence, a global Serre equality, or sourcebook identity.

## 2. Actual free object and the whole first relation

All brackets in Sections 2–6 are in the ordinary free Lie algebra \(L(V)\), embedded in the tensor algebra by concatenation, **not** products of adjoint matrices. The actual eight-letter Levi module has degrees
\[
\begin{array}{c|cccccccc}
 &x&a&b&c&d&e&f&g\\\hline
(i,j)&(0,0)&(1,0)&(0,1)&(1,1)&(1,1)&(2,1)&(1,2)&(2,2).
\end{array}
\]
The complete given Levi table is
\[
\begin{array}{c|rrrrrrrr}
 &x&a&b&c&d&e&f&g\\\hline
 E_1&a&0&c&-2e&-e&0&g&0\\
 E_2&b&d&0&f&2f&-g&0&0\\
 F_1&0&x&0&2b&b&-c&0&f\\
 F_2&0&0&x&a&2a&0&d&-e
\end{array}. \tag{2}
\]
Set
\[
 q=[x,a],\qquad h=[x,q],\qquad W=U(\mathfrak{sl}_3)h,\qquad A=[V,W].
\]
The tensor word \(xxa\) shows \(h\ne0\). Both \(F_1,F_2\) kill it, and its lowest labels are \((1,4)\); hence \(W\cong L_{\mathrm{low}}(1,4)\). The imported whole-ideal bridge identifies \(W\) with the entire grade-three first relation and \(A\) with the entire grade-four first-seed consequence.

For later use, the whole-module upper bound follows from the Pieri rules, not from a selected bracket:
\[
 V\otimes W\cong L(2,5)\oplus L(3,3)\oplus L(0,6)
 \oplus2L(1,4)\oplus L(2,2)\oplus L(0,3). \tag{3}
\]
Indeed \(V=\mathbf3\otimes\overline{\mathbf3}-\mathbf1\), and \(L(1,4)\otimes\mathbf3=L(2,4)\oplus L(0,5)\oplus L(1,3)\). The potential \(L(0,6)\) does not occur in \(L_4(V)\): its lowest root position is \((2,0)\), whose free piece has multidegree \(x^2a^2\), Witt dimension one and basis \([a,[x,[x,a]]] = [a,a_2]\). But \(F_1[a,a_2]=[x,a_2]=a_3\ne0\). Thus its entire lowest kernel is zero. The image \(A\) has no such summand.

## 3. Complete ten-dimensional free root and all four free lowest vectors

Write \(a_i=(\operatorname{ad}x)^i a\), and similarly \(b_i,c_i,d_i,e_i\). In \(L_4(V)_{2,1}\), use the ordered ten vectors
\[
\begin{gathered}
 N=e_3,\quad U_i=[a_i,c_{2-i}],\quad V_i=[a_i,d_{2-i}]\quad(i=0,1,2),\\
 X_0=[q,[a,b]],\quad X_1=[a,[q,b]],\quad X_2=[a,[a,b_1]].
\end{gathered} \tag{4}
\]
They are a **whole basis**. Their four distinct letter-multidegree blocks are \(x^3e,x^2ac,x^2ad,xa^2b\), with Witt dimensions \(1,3,3,3\). In tensor words \(N\) has nonzero \(xxxe\); \(xxca,xxac,xacx\) successively separate \(U_0,U_2,U_1\), and the analogous words with \(d\) separate \(V_0,V_2,V_1\). For \(X_0,X_2,X_1\), the successive pivots are \(xaab,aabx,axab\). This also accounts for every free root vector, not just the displayed four lowest ones.

Put
\[
 v=\alpha N+\sum_{i=0}^2u_iU_i+\sum_{i=0}^2v_iV_i+kX_0+\ell X_1+mX_2.
\]
The complete \(F_1v\) coefficients, in the independent basis
\((c_3,d_3,[a,b_2],[q,b_1],[a_2,b])\), and the complete \(F_2v\) coefficient on \([a,a_2]\), are
\[
\begin{array}{l}
-\alpha+u_0,\quad v_0,\quad 2u_0+v_0+2m,\\
2u_1+v_1+k+\ell+m,\quad 2u_2+v_2+\ell;\\
u_0-u_2+2v_0-2v_2-\ell.
\end{array} \tag{5}
\]
For example, \(F_1U_0=c_3+2[a,b_2]\), \(F_1X_2=2[a,b_2]+[q,b_1]\), \(F_2U_0=[a,a_2]\), \(F_2V_2=-2[a,a_2]\), and \(F_2X_1=-[a,a_2]\); the rest follow from (2) and Leibniz. The three mixed \(F_1\)-basis vectors are independent in multidegree \(x^2ab\), e.g. by tensor words \(xxba,xxab,xaxb\); the other two basis vectors have distinct multidegrees. Solving all six equations gives
\[
\alpha=u_0,\quad v_0=0,\quad m=-u_0,\quad
\ell=-u_0-3u_2,\quad v_2=u_0+u_2,\quad
k=2u_0+3u_2-2u_1-v_1. \tag{6}
\]
Thus the **whole** free lowest space has exactly the following four independent vectors:
\[
\begin{aligned}
 w_0&=N+U_0+V_2+2X_0-X_1-X_2,\\
 w_1&=U_1-2X_0,\\
 w_2&=U_2+V_2+3X_0-3X_1,\\
 w_3&=V_1-X_0.
\end{aligned} \tag{7}
\]
Their grade-four position \((2,1)\) has lowest labels \((4-2\cdot2+1,4+2-2)=(1,4)\).

## 4. Reconstructing both complete relation copies and the quotient

Set \(h_1=E_1h\), \(h_2=E_2h\), \(h_{12}=E_1E_2h\), \(h_{21}=E_2E_1h\). Directly from (2),
\[
\begin{aligned}
 h_1&=[a,q],\\
 h_2&=d_2-2[q,b]-[a,b_1],\\
 h_{12}&=2[a,d_1]+[q,d]-e_2-2[q,c]-[a,[a,b]]-[a,c_1],\\
 h_{21}&=[a,d_1]-[q,d]-[a,[a,b]].
\end{aligned} \tag{8}
\]
Define actual brackets in \(A\):
\[
\begin{aligned}
 z_1&=[x,h_{12}]-2[a,h_2]-4[b,h_1]+4[d,h],\\
 z_2&=[x,h_{21}]-[a,h_2]-5[b,h_1]+2[c,h]+[d,h].
\end{aligned} \tag{9}
\]
Their complete free-basis expansions, obtained by applying \([x,[u,v]]=[[x,u],v]+[u,[x,v]]\), are
\[
\begin{aligned}
 z_1&=-N-U_0-3U_1-2U_2+3V_1-3V_2-5X_0+7X_1+X_2\\
    &=-w_0-3w_1-2w_2+3w_3,\\
 z_2&=-2U_2-2V_2-6X_0+6X_1=-2w_2. 
\end{aligned} \tag{10}
\]
For an explicit check, \([b,h_1]=X_0-X_1\), and
\([x,h_{12}]=2V_0+3V_1+V_2-N-2U_2-3U_1-U_0-X_0-X_1-X_2\).
Equations (7),(10) show that both \(z_i\) are lowest and independent. Since (3) bounds the **whole** \(L(1,4)\) multiplicity of \(A\) by two, they exhaust its entire lowest relation space.

This also gives the complete first-relation root dimension, without identifying a map rank with a character. The nonzero vector \([x,h]\) is lowest of type \(L(2,5)\), and \([x,h_2]-4[b,h]\) is lowest of type \(L(3,3)\); their respective nonzero tensor words are \(xxxa\) and \(xxxd\). At \((2,1)\), the first contributes two dimensions and the second one. For lowest labels \((p,q)=(2,5)\), the two vectors \(E_1E_2v,E_2E_1v\) are independent because their two lowerings have coefficient determinant \((p+1)(q+1)-pq=8\); PBW spanning bounds that displacement by two. The \(L(3,3)\) contribution is a single nonzero \(E_1\) step. Both \(L(1,4)\) relations contribute one each, and the remaining possible types in (3) contribute nothing at this position, with \(L(0,6)\) absent by Section 2. Therefore
\[
 \dim A_{2,1}=2+1+2=5. \tag{11}
\]
Let
\[
 P=(L_4(V)/A)_{2,1},\quad
 K=\ker F_1\cap\ker F_2\text{ on }P,\quad
 T=(L_3(V)/W)_{2,1}. \tag{12}
\]
The finite-dimensional Levi module has a stable complement to \(A\); consequently the free-to-quotient map is surjective on the **whole** lowest kernel, not merely on selected copies. From (7),(10),
\[
 \dim P=5,\qquad K=\operatorname{span}\{\bar w_1,\bar w_3\},
 \qquad\dim K=2. \tag{13}
\]
The two displayed vectors form a basis of the entire lowest subspace \(K\), not a basis of the five-dimensional whole root space \(P\).

## 5. Target basis, actual descent, and every minor

Introduce free grade-three vectors
\[
 A_0=[a,c_1],\ B_0=[q,c],\ C_0=[a,d_1],\ D_0=[q,d],\ E_0=e_2,\ R_0=[a,[a,b]]. \tag{14}
\]
The separated letter-multidegree dimensions are \(2,2,1,1\), and tensor words \(xca,xac\), respectively their \(d\)-analogues, separate each pair; hence these six vectors form the whole free target root space. By (8),
\[
 h_{12}=2C_0+D_0-E_0-2B_0-R_0-A_0,\qquad
 h_{21}=C_0-D_0-R_0. \tag{15}
\]
These two vectors are independent, and PBW spanning of the \(W\) weight after one \(E_1\) and one \(E_2\) bounds its dimension by two. Thus they are the whole \(W_{2,1}\). Reducing by them yields
\[
 R_0=E_0+2B_0+A_0-3D_0,\qquad C_0=D_0+R_0,
\quad (\bar A_0,\bar B_0,\bar D_0,\bar E_0)\text{ a basis of }T,\quad \dim T=4. \tag{16}
\]

Now derive the actual \(F_3\) operation rather than substituting a model matrix. For a letter \(u\), let \(D_u=\operatorname{ad}[f_3,u]\). The Chevalley brackets and (2) give
\[
 D_x|_{L(V)_{i,j,n}}=2i+sj-2n,\quad
 D_a=-2E_1,\ D_b=-sE_2,\ D_c=-s[E_1,E_2],\ D_d=2[E_1,E_2],\ D_e=D_f=D_g=0. \tag{17}
\]
Here the \(D_x\) eigenvalue is the **whole word's** grade \(n\) and horizontal degree \((i,j)\); on a single letter it reduces to \(2i+sj-2\). For a degree-one \(u\), degree-one \(v\), and \(w\) of positive degree at least two,
\[
 \delta_s[u,v]=D_uv-D_vu,\qquad
 \delta_s[u,w]=D_uw+[u,\delta_sw],\quad \delta_s=F_3. \tag{18}
\]
In particular \(\delta_s q=2a\) and \(\delta_s h=-2q+[x,2a]=0\). Since \([F_3,E_1]=[F_3,E_2]=0\), \(\delta_sW=0\); and for every \(u\in V,w\in W\), \(\delta_s[u,w]=D_uw\in W\). Thus the **entire** \(A=[V,W]\) descends into the **entire** target relation \(W\), uniformly in \(s\); this is the actual induced \(P\to T\), not a projected surrogate.

The elementary letter identities are
\[
 \delta_s c_1=2sc-sd,\qquad \delta_s d_1=-2c+(s+2)d,
 \qquad \delta_s[a,b]=-2c+sd. \tag{19}
\]
For example, \(D_xc=sc\) and \([E_1,E_2]x=c-d\), giving the first. Using \(\delta_sq=2a\), (19), and the derivation rule,
\[
\begin{aligned}
 \delta_s U_1&=2A_0+2sB_0-sD_0,\\
 \delta_s V_1&=2C_0-2B_0+(s+2)D_0,\\
 \delta_s X_0&=2R_0-2B_0+sD_0.
\end{aligned} \tag{20}
\]
Consequently
\[
 \delta_sw_1=2A_0+(2s+4)B_0-3sD_0-4R_0,\qquad
 \delta_sw_3=2(C_0+D_0-R_0). \tag{21}
\]
In the full source basis (13) and target basis (16), (21) reduces to
\[
 M(s)=\begin{pmatrix}
 -2&0\\ 2s-4&0\\ 12-3s&4\\ -4&0
 \end{pmatrix},\qquad
 M(3+t)=\begin{pmatrix}
 -2&0\\ 2t+2&0\\ 3-3t&4\\ -4&0
 \end{pmatrix}. \tag{22}
\]
The six ordered \(2\times2\) minors, using row order \(12,13,14,23,24,34\), are exactly
\[
 (0,-8,0,8s-16,0,16)=(0,-8,0,8t+8,0,16). \tag{23}
\]
The constant \(-8\) proves rank two over every scalar specialization, hence every integral \(s\ge3\). It detects every diagonal mixture in the two-dimensional \(K\). The formulas make no assertion that \(F_3\) is Levi-equivariant under \(F_1,F_2\).

## 6. The actual s=3 second seed and whole-root check

For \(s\ge4\) the second Serre seed begins in grade \(s+1\ge5\), so the grade-four source is exactly the first-only quotient. At \(s=3\), the entire additional relation is the cyclic module
\[
 k=b_3=(\operatorname{ad}x)^3b,\qquad B=U(\mathfrak{sl}_3)k\cong L(5,2).
\]
The word \(xxxb\) shows \(k\ne0\), and both lowerings kill it. Its type is absent from (3), so semisimplicity gives \(A\cap B=0\). Its entire \((2,1)\) weight is the single line \(\mathbb C E_1^2k\), with
\[
 F_1E_1^2k=2(5-1)E_1k=8E_1k\ne0. \tag{24}
\]
In particular that line is not a lowest vector in \(P\). More importantly, a Levi-stable complement to \(B\) shows that quotienting by the whole simple module creates no new lowest vectors of type \(L(1,4)\): the images of \(\bar w_1,\bar w_3\) remain an entire basis. This semisimplicity argument, not just nonlowestness of the one line, proves completeness of the boundary quotient.

For actual descent, (17),(18) give
\[
 \delta_sb_1=2(s-1)b,\quad
 \delta_sb_2=3(s-2)b_1,\quad
 \delta_sk=4(s-3)b_2. \tag{25}
\]
At \(s=3\), \(\delta_3k=0\), hence \(\delta_3B=0\) by commutation with the Levi raisings. Thus (22) is indeed the same actual lowest map after quotienting by **both** seed modules. Equation (23) gives rank two at the boundary as well as in the first-only pencil.

There is also an independent whole-root consistency argument. Both signs of the Serre relations make actual \(E_3,F_3\) locally nilpotent on generators, hence on finite Lie words. For a homogeneous vector, the \(\mathfrak{sl}_2\) PBW spanning order gives a finite-dimensional generated module. On every finite-dimensional \(\mathfrak{sl}_2\) module, lowering is onto a negative weight. The \(H_3\) weight of \(S_{2,1,3}\) is \(2-s<0\), so the actual whole-root map \(F_3:S_{2,1,4}\to S_{2,1,3}\) is onto. Its source/target dimensions, from Sections 4–5 and the boundary line, are
\[
\begin{array}{c|ccc}
 &\dim S_{2,1,4}&\dim S_{2,1,3}&\dim\ker F_3\\\hline
 s=3&4&4&0\\
 s\ge4&5&4&1.
\end{array} \tag{26}
\]
In particular at \(s=3\) the induced map is an isomorphism, and the kernel of the **first-only** \(P\to T\) is exactly \(\mathbb C E_1^2k\). Its intersection with \(K\) is zero. At \(s\ge4\), the one-dimensional whole-root kernel is disjoint from \(K\) by (23); it is **not** thereby identified with the radical.

## 7. Reconciliation with F832's different-basis output

Packet S5/S6 report an actual prior parent-run stdout with a different two-column pencil. The numeric process exit was **not separately shown**, and I did not read or execute its linked operative code. Its reported columns, with \(t=s-3\), are
\[
\begin{aligned}
 a(t)&=(-10-2t,-3-t,7+3t,-(1+t)/2)^T,\\
 b(t)&=(40+8t,12+4t,-36-12t,-2+2t)^T.
\end{aligned} \tag{27}
\]
Writing \(M_{832}=[a\ b]\), I obtain the following **explicit constant rational pencil equivalence** by direct multiplication:
\[
 M_{832}(t)=P\,M(3+t)\,Q,\quad
 P=\begin{pmatrix}
 2&-1&0&1\\
 1&-\tfrac12&0&0\\
 -8&-\tfrac32&-2&0\\
 -3&-\tfrac74&-1&0
 \end{pmatrix},\qquad
 Q=\begin{pmatrix}1&-4\\0&1\end{pmatrix},\qquad
 \det P=\det Q=1. \tag{28}
\]
For a transparent check, if \(u(t),v\) are the two columns in (22), then \(Pu(t)=a(t)\), \(Pv=(0,0,-8,-4)^T\), and \(b(t)=-4a(t)+Pv\). The identity is an exhibited algebraic equivalence between the reported polynomial matrices; it does **not** identify the actual private basis vectors selected by the F832 program or claim its matrix is literally (22).

Independently expanding (27) gives its ordered minors
\[
 (0,80+16t,40+8t,24+8t,12+4t,-32-16t). \tag{29}
\]
In particular \(\Delta_{13}-2\Delta_{23}=32\), so their monic gcd in \(\mathbb Q[t]\) is 1 and there is no common zero. This reconciles the packet's reported gcd and empty exceptional set with (23), despite the individual minors and the matrices being different. Equation (28), not an unaudited program, is the written basis for the comparison; it does not independently certify the prior run, its mutations, or its source bridge.

## 8. Full-Cartan ideal criterion and conclusion

Let \(v\in S_{2,1,4}\) be an actual homogeneous simultaneous \(F_1,F_2\)-lowest vector. If \(v\in\mathcal R\), then \(F_3v\in\mathcal R\cap S_3=0\) by the named entire-grade-three import. Conversely suppose \(F_3v=0\). Let \(I_+\) be the span of \(v\) and every iterated positive-simple adjoint. Root homogeneity makes it stable under the **whole** Cartan; it is stable under all positive generators by construction. Induction on word length using
\[
 [f_i,[e_j,w]]=-\delta_{ij}[h_i,w]+[e_j,[f_i,w]] \tag{30}
\]
shows stability under every negative generator as well. Hence \(I_+\) is an ideal. All its roots have \(\alpha_3\)-coefficient at least four, so it has zero intersection with the whole Cartan. The imported full-Cartan injection makes its inverse image in \(G\) Cartan-disjoint, hence contained in \(\tau\). Therefore
\[
 v\in\mathcal R\quad\Longleftrightarrow\quad F_3v=0
 \qquad\text{for every actual homogeneous simultaneous lowest }v. \tag{31}
\]
The forward implication alone plus (23) excludes the entire lowest intersection with \(\mathcal R\); the converse is recorded for exactness, not applied to arbitrary root-kernel vectors. Since \(\mathcal R\cap S_4\) is a finite-dimensional Levi submodule, any nonzero intersection with the whole \(L(1,4)\) isotypic would have a nonzero lowest vector, including in a diagonal copy. Equations (23)–(25) rule this out for every integer \(s\ge3\), proving (1) at precisely the named imports.

No claim is made about the six-copy \(L(2,2)\) lowest map, other grade-four types, the whole grade-four radical, higher grades, all parameters, an actual sourcebook identity, or global \(J=\tau\). No independent-family/human/formal acceptance or publication priority is implied. Parent disposition and separate disjoint scientific scrutiny remain outstanding.

## 9. Complete read and process declaration

Before any mathematical body or mathematical reasoning, I read the full manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and all **24** manifest-listed status/permission controls. I wrote the new `prebody-ack-v1.md` and sent the required direct prebody ACK to `Main` before packet access. The initial non-raw administrative displays elided portions; the full administrative files were subsequently displayed raw before the ACK. An attempted raw metadata read had a mistyped home directory and failed; it was retried at the actual manifest path. The general memory summary had long-line display truncation and was not a mathematical source. Administrative/control material supplied no mathematical premise. Parent pins and roundtrip statements below are parent-reported metadata, not independently recomputed hashes or correctness certificates.

After the ACK and before mathematical reasoning, I read packet part 01 **serially**, raw windows LF 1–20, 21–40, ..., 1001–1020, 1021–1026, including its ending; then part 02 serially in raw windows LF 1–20 and 21–29, including its ending. Every window was at most 20 LF and below 30,000 displayed bytes; no packet clipping or clipping recovery was observed. Parent-supplied part SHA-256 values are `4391ab1156e4c36c8c66630878ba565a1e2f790637c3f99c31946619ce335f69` and `41cf7da8240ee153107e8217052b00a803fa932cc388d54184c12bd539221269`. They render all complete original bodies below. Paths are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`:

| ID | Complete literal body | LF | Parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f831-kac-r2-cofinite-lowest-ideal-proof-author/author-candidate-v1.md` | 246 | `3332c813487588ff2bcffcc0268ad2182e820e5f01651c846e084b6b97613438` |
| S2 | `review-waves/f830-kac-r2-whole-relation-multiplicity-proof-author/author-candidate-v1.md` | 258 | `61ce48fdcdb1b4148ab4a796a8ffbfcab44142eb0acc4cb86baba6b3effe4902` |
| S3 | `review-waves/f832-kac-r2-complete-lowest-symbolic-finite-author/parent-prerun-boundary-target-and-exit-design-major-v1.md` | 9 | `9d6aef9a198ce129a3d7789c6fe1cf38d78079dde06bb21f18a6fc49883036d3` |
| S4 | `review-waves/f832-kac-r2-complete-lowest-symbolic-finite-author/author-candidate-v1.md` | 158 | `6ac724bb25d31cced0827cf1daaf196e52d553e841590a66036ae32218faacf9` |
| S5 | `review-waves/f832-kac-r2-complete-lowest-symbolic-finite-author/parent-r2-v2-run-v1-receipt.json` | 199 | `a06dfb524ee2594e45b654b829fb0dd0a3220230792ae7e08be03a0724d1d081` |
| S6 | `review-waves/f832-kac-r2-complete-lowest-symbolic-finite-author/parent-r2-v2-run-v1-complete-stdout.json` | 1 | `0cd7c841375a634d1528138071d9698c1095b336f5ed5f064876df75eb8a18ed` |
| S7 | `dispositions/math-3-actual-free-source-and-full-serre-ideal-at-displayed-presentation-parent-v1.md` | 27 | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` |
| S8 | `dispositions/math-3-actual-third-grade-three-entire-radical-exclusion-parent-v1-erratum-1.md` | 5 | `9648a8ab70aa62355e52e5c7cc8ad5ebb584876bc1d5ad7e3b883b40f78799e5` |
| S9 | `dispositions/math-3-kac-actual-entire-third-grade-two-and-all-grade-boundary-parent-v1.md` | 44 | `6f5b9994bd27198b06f0a9e1e7294712e35fbdce47ab07d9ca51aa3f58f90629` |
| S10 | `dispositions/math-3-actual-third-grade-three-entire-radical-exclusion-parent-v1.md` | 37 | `b703063027085eb004407d51a9a55941c2fbf02d5f3ccf851ab502a1af7f500d` |
| S11 | `dispositions/math-3-grade4-entire-singlet-selected-submodule-and-lowest-ideal-criterion-parent-v1.md` | 23 | `c75905ed6751ee0af9d77042adbcf0eb35947bacecbfa95411f5a4699547c7db` |

No unlisted source or code, sibling source, historical held episode, or held proof/method/planning/selection/verification/reporting/confidence/downstream consumer was opened. There was no network, child subprocess, scientific execution, eval, solver, test, compile, build, linter, formatter, Git, or deletion. No code was prepared, so no prepared-code hash exists. These process declarations do not certify unobservable cognition.
