# r=2: whole grade-four relations, boundary root dimensions, and a new tenth-dimensional relation

**GENERAL AUTHOR CANDIDATE; conditional, nonblind, unadopted.** This is a written reconstruction of the f809 claims at the exact original quotient and a further explicit lowest-vector calculation. It requires a complete parent read and a separate independent disposition. It is not a family, human, formal/kernel, source-identity, publication-priority, or novelty claim.

## 1. Exact objects, quantifiers, and imports

For **every** integer \(s\ge3\), put
\[
 A(2,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-2&-s&2\end{pmatrix}.
\]
For **every full complex Cartan realization**, including additional Cartan directions when present, let \(G\) be the preliminary Chevalley algebra, \(J\) the **whole ideal of both signs of every Serre relation**, \(\tau\) the maximal ideal disjoint from the whole Cartan, \(S=G/J\), and \(\mathcal R=\tau/J\). Write \(S_{a,b,n}\) for the **entire** homogeneous root component and \(E_i=\operatorname{ad}e_i\), \(F_i=\operatorname{ad}f_i\). A lowest multiplicity space is the entire simultaneous \(F_1,F_2\) kernel, including every copy and every diagonal mixture. For a grade-four lowest position \((a,b)\), its labels are \((p,q)=(4-2a+b,4+a-2b)\).

The explicit conditional imports are: S7's actual ordinary-free-Lie source, both-sign whole-ideal bridge, full-Cartan injection and root grading at its displayed-presentation interface; the entire grade-three statement \(\mathcal R\cap S_3=0\); S5's free grade-four character; and ordinary characteristic-zero free-Lie tensor embedding, finite-dimensional \(\mathfrak{sl}_3\) semisimplicity and finite-dimensional \(\mathfrak{sl}_2\) theory. S8 reconstructs the grade-three statement conditional on its own **entire grade-two radical-zero** interface; the underlying grade-two proof is not present in this packet and remains a named conditional import. Likewise S7 refers to the underlying operative Chevalley-presentation/bridge bodies, which were not supplied as literal bodies here; its scope is imported, not independently re-established from those missing bodies. No preliminary-\(G\) PBW basis, global \(J=\tau\), or held output is assumed.

At those imports, the main conclusions are:

* The **entire first-seed grade-four relation**, including all copies, is
  \[
  A=[V,W]\cong L(2,5)\oplus L(3,3)\oplus2L(1,4)
       \oplus L(2,2)\oplus L(0,3). \tag{1}
  \]
  In particular f809's first-relation multiplicities **2 and 1** for \(L(1,4)\) and \(L(2,2)\) are reconstructed. The last \(L(0,3)\) summand is an additional written calculation: f809 had left its multiplicity undetermined.
* At \(s=3\), the entire second-seed relation is one \(L(5,2)\), and it has **zero intersection with the whole** \(A\). At \(s\ge4\), that seed contributes nothing in grade four. Consequently the entire actual lowest multiplicities at \((2,1)\) and \((2,2)\) are respectively **2 and 6** for every \(s\ge3\).
* Actual \(F_3:S_{2,1,4}\to S_{2,1,3}\) is onto: its dimensions are \(4\to4\) at \(s=3\) and \(5\to4\) at \(s\ge4\). Thus it is an isomorphism at \(s=3\), and the **whole** \(L(1,4)\) isotypic at this boundary has zero intersection with \(\mathcal R\). For \(s\ge4\) its whole root kernel has dimension 1; this only bounds the \(L(1,4)\) radical multiplicity by 1.
* Actual \(F_3:S_{2,2,4}\to S_{2,2,3}\) is onto: its dimensions are \(16\to11\) at \(s=3\), and \(18\to11\) at \(s\ge4\). Its root kernel dimensions are respectively **5 and 7**. At \(s=3\), at most five of the six actual \(L(2,2)\) copies can be radical. No root kernel is identified with the radical.

## 2. Actual first seed and lowering table

All following brackets are in the ordinary free Lie algebra on the actual eight-dimensional Levi module \(V\), or its tensor embedding, **not** matrix products. Use the ordered letters \(x,a,b,c,d,e,f,g\), of horizontal degrees
\[
(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2).
\]
Their table is
\[
\begin{array}{c|rrrrrrrr}
 &x&a&b&c&d&e&f&g\\\hline
E_1&a&0&c&-2e&-e&0&g&0\\
E_2&b&d&0&f&2f&-g&0&0\\
F_1&0&x&0&2b&b&-c&0&f\\
F_2&0&0&x&a&2a&0&d&-e
\end{array}. \tag{2}
\]
Put
\[
 q=[x,a],\qquad h=[x,q],\qquad W=U(\mathfrak{sl}_3)h.
\]
Here \(h\ne0\) by the tensor word \(xxa\); \(F_1h=F_2h=0\) and \((H_1,H_2)h=(-1,-4)h\). Finite-dimensional Levi semisimplicity gives \(W\cong L(1,4)\). The imported whole-ideal bridge identifies the entire first-seed grade-four relation with \(A=[V,W]\).

Set
\[
\begin{gathered}
 h_1=E_1h,\quad h_2=E_2h,\quad h_{22}=E_2^2h,\quad
 h_{12}=E_1E_2h,\quad h_{21}=E_2E_1h,\\
 h_A=E_1E_2^2h,\quad h_B=E_2E_1E_2h.
\end{gathered}
\]
The Chevalley commutators \([F_i,E_j]=-\delta_{ij}H_i\) give the complete table needed below:
\[
\begin{array}{c|cc}
 &F_1&F_2\\\hline
h&0&0\\
h_1&h&0\\
h_2&0&4h\\
h_{22}&0&6h_2\\
h_{12}&2h_2&4h_1\\
h_{21}&h_2&5h_1\\
h_A&3h_{22}&6h_{12}\\
h_B&2h_{22}&3h_{12}+4h_{21}
\end{array}. \tag{3}
\]
For example, \(H_2h_{12}=-3h_{12}\), giving the last entry. Directly, \(h_1=[a,q]\ne0\), and
\[
 h_2=[b,q]+[x,[b,a]+[x,d]]\ne0
\]
has coefficient 1 at \(xxd\). If \(\alpha h_{12}+\beta h_{21}=0\), applying the two lowerings gives \(2\alpha+\beta=4\alpha+5\beta=0\), whose determinant is 6. Thus those two vectors are independent. The two \(F_2\)-images of \(h_A,h_B\) are likewise independent; PBW spanning at their respective displacement weights bounds each corresponding \(W\) weight space by two. In particular these are the **whole** relevant two-dimensional spaces.

The tensor-product upper bound itself can be recovered without assuming a bracket rank. Since \(V=\mathbf3\otimes\overline{\mathbf3}-\mathbf1\), the two Pieri rules give
\[
\begin{aligned}
L(1,4)\otimes\mathbf3&=L(2,4)\oplus L(0,5)\oplus L(1,3),\\
L(p,q)\otimes\overline{\mathbf3}&=L(p,q+1)\oplus L(p+1,q-1)\oplus L(p-1,q),
\end{aligned}
\]
with negative labels omitted. Hence
\[
 V\otimes W\cong L(2,5)\oplus L(3,3)\oplus L(0,6)
  \oplus2L(1,4)\oplus L(2,2)\oplus L(0,3). \tag{4}
\]
S5's complete free grade-four character has no \(L(0,6)\). Thus that summand is in the kernel of the equivariant bracket map, while (4) bounds every remaining image multiplicity.

## 3. f809's three vectors and all-copy multiplicities

Define
\[
\begin{aligned}
 z_1&=[x,h_{12}]-2[a,h_2]-4[b,h_1]+4[d,h],\\
 z_2&=[x,h_{21}]-[a,h_2]-5[b,h_1]+2[c,h]+[d,h],\\
 z_{27}&=4[x,h_A]-3[x,h_B]-6[a,h_{22}]-15[b,h_{12}]
       +12[b,h_{21}]+18[d,h_2]-72[f,h].
\end{aligned} \tag{5}
\]
They belong to the actual free-word relation \(A\). Using (2)–(3), the first two are killed by both lowerings: for \(F_1z_1\) the paired coefficients are \(2-2\) and \(-4+4\); for \(F_2z_1\) they are \(4-4\) and \(-8+8\). For \(z_2\) the corresponding pairs are \(1-1,-5+4+1\), and \(5-5,-4+2+2\). For the third vector the complete cancellations are
\[
\begin{aligned}
F_1z_{27}&=(12-6-6)[x,h_{22}]+(-30+12+18)[b,h_2]=0,\\
F_2z_{27}&=(24-9-15)[x,h_{12}]+(-12+12)[x,h_{21}]\\
 &\quad+(-36+36)[a,h_2]+(-60+60)[b,h_1]+(72-72)[d,h]=0.
\end{aligned} \tag{6}
\]
The tensor coefficient of \(xxxe\) in \(z_1\) is \(-1\): \(E_1E_2a=-e\). On the other hand \(z_2\) contains no letter \(e\), and its coefficient at \(cxxa\) is 2. Indeed \(h_1=[a,q]\), \(h_2\) is displayed above, and
\(h_{21}=[d,q]+[a,[b,a]+[x,d]]\), so no other term of \(z_2\) contains \(c\). Thus \(z_1,z_2\) are independent **actual free words**, not projections of one copy.

Moreover \(E_1E_2^2a=2g\) and \(E_2E_1E_2a=g\); consequently the coefficient of \(xxxg\) in \(z_{27}\) is \(4\cdot2-3\cdot1=5\). The other outer bracket letters cannot produce that word. Thus \(z_{27}\ne0\). Their horizontal degrees are \((2,1),(2,1),(2,2)\), with lowest labels \((1,4),(1,4),(2,2)\). Complete reducibility plus the **whole** source bounds in (4) prove exactly two and one respective relation copies.

Also, \([x,h]\) is a nonzero lowest \(L(2,5)\) vector, with coefficient 1 at \(xxxa\), and
\[
 z_{64}=[x,h_2]-4[b,h]
\]
is a nonzero lowest \(L(3,3)\) vector, with coefficient 1 at \(xxxd\). Its \(F_1\) image is zero and its \(F_2\) image is \(4[x,h]-4[x,h]\). Thus each of these source types also survives once.

## 4. New explicit \(L(0,3)\) relation and the complete first image

This section pays the first-relation case that f809 explicitly left unknown. Put
\[
 k=E_1h_{12}=E_1^2E_2h,\quad t_1=E_1h_A,\quad t_2=E_1h_B.
\]
Since \(E_1q=0\), also \(E_1^2h=0\); the \(A_2\) Serre relation gives \(E_1h_{21}=k/2\). Applying the Chevalley commutators to (3) yields
\[
\begin{array}{c|cc}
 &F_1&F_2\\\hline
 k&2h_{12}&0\\
 t_1&4h_A&6k\\
 t_2&2h_A+h_B&5k
\end{array}. \tag{7}
\]
Now form the following actual bracket sum in \([V,W]\):
\[
\begin{aligned}
 z_{10}={}&2[x,t_1]-3[x,t_2]-2[a,h_A]+3[a,h_B]+3[b,k]\\
 &-5[c,h_{12}]+4[c,h_{21}]+4[d,h_{12}]-8[d,h_{21}]\\
 &-6[e,h_2]+24[f,h_1]-24[g,h].
\end{aligned} \tag{8}
\]
Its horizontal degree is \((3,2)\), hence its lowest labels, if annihilated, are \((0,3)\). Equations (2), (3), (7) give the following complete coefficient cancellations, using the indicated bracket terms as a spanning list:
\[
\begin{array}{c|l}
F_1z_{10}&
\begin{array}{l}
[x,h_A]:8-6-2;\ [x,h_B]:-3+3;\ [a,h_{22}]:-6+6;\\
[b,h_{12}]:6-10+4;\ [b,h_{21}]:8-8;\\
[c,h_2]:-10+4+6;\ [d,h_2]:8-8;\ [f,h]:24-24
\end{array}\\\hline
F_2z_{10}&
\begin{array}{l}
[x,k]:12-15+3;\ [a,h_{12}]:-12+9-5+8;\\
[a,h_{21}]:12+4-16;\ [c,h_1]:-20+20;\\
[d,h_1]:16-40+24;\ [e,h]:-24+24
\end{array}
\end{array}. \tag{9}
\]
Every displayed coefficient is zero, so both lowerings annihilate \(z_{10}\). Its nonvanishing is not inferred from the character: in the ordinary tensor embedding the coefficient at the single word \(gxxa\) is
\[
 \underbrace{4}_{-2[a,h_A]}\;\underbrace{-3}_{3[a,h_B]}\;
 \underbrace{-24}_{-24[g,h]}=-23\ne0. \tag{10}
\]
Indeed the coefficients of \(gxx\) in \(h_A,h_B\) are 2 and 1, respectively, and that of \(xxa\) in \(h\) is 1; all other outer bracket letters begin or end their terms with a letter incompatible with \(gxxa\).

Therefore the unique possible \(L(0,3)\) source copy in (4) survives. Along with §3 and the absence of \(L(0,6)\) from the free target, this proves (1), not merely bounds. In fact the kernel of the entire map \(V\otimes W\to L_4(V)\) is exactly its single \(L(0,6)\) summand. Its dimension is 28; the source dimension is \(8\cdot35=280\), and the whole first-relation image has dimension
\[
81+64+2\cdot35+27+10=252. \tag{11}
\]
This is a new **written** conclusion requiring separate review; no calculation program or finite verifier was run.

## 5. Second seed, complete character, and boundary dimensions

At \(s=3\), the second seed is the nonzero lowest free word \((\operatorname{ad}x)^3b\), whose lowest labels are \((5,2)\), and its entire grade-four contribution is the one cyclic simple module \(B\cong L(5,2)\), of dimension 81. At \(s\ge4\) its seed degree is at least five. None of the types in (1) is \(L(5,2)\); by finite-dimensional Levi semisimplicity, \(A\cap B=0\) at \(s=3\). This proves disjointness of the **whole modules**, not just of the two named weights.

S5 gives the free lowest multiplicities below, in the listed dominant positions, by the ordinary free-Lie character and the lowest Weyl denominator. Subtracting (1) and, only at \(s=3\), the disjoint second seed gives every actual grade-four lowest multiplicity:
\[
\begin{array}{c|c|r|r|r}
(a,b)&(p,q)&\text{free}&s=3&s\ge4\\\hline
(0,0)&(4,4)&0&0&0\\
(0,1)&(5,2)&1&0&1\\
(0,2)&(6,0)&0&0&0\\
(1,0)&(2,5)&1&0&0\\
(1,1)&(3,3)&3&2&2\\
(1,2)&(4,1)&4&4&4\\
(2,0)&(0,6)&0&0&0\\
(2,1)&(1,4)&4&2&2\\
(2,2)&(2,2)&7&6&6\\
(2,3)&(3,0)&6&6&6\\
(3,2)&(0,3)&6&5&5\\
(3,3)&(1,1)&8&8&8\\
(4,4)&(0,0)&1&1&1
\end{array}. \tag{12}
\]
The two requested entries are therefore \(2,6\), including the boundary. The complete actual grade-four dimension is \(1008-252-81=675\) for \(s=3\), and \(1008-252=756\) for \(s\ge4\). These are module/character dimensions, **not** ranks of \(F_3\).

For the root dimensions, the free grade-four dimensions at \((2,1),(2,2)\) are 10 and 25; the free grade-three dimensions there are 6 and 13. For example, with \(H=(1+X)(1+Y)(1+XY)\),
\[
\begin{aligned}
[X^2Y]H^3&=18,&[X^2Y^2]H^3&=39,\\
[X^2Y]H^4&=40,&[X^2Y^2]H^4&=106,\\
[X^2Y^2]H(X^2,Y^2)^2&=6.
\end{aligned}
\]
The Witt formulas yield the four stated dimensions; the grade-three correction \(H(X^3,Y^3)\) contributes zero at both weights.

At \((2,1)\), the whole first relation contributes \(2+1+2=5\), from \(L(2,5),L(3,3),2L(1,4)\), respectively. At \((2,2)\), its contributions are \(2+2+2+1=7\), from those types and \(L(2,2)\). The new \(L(0,3)\) summand starts at \((3,2)\) and contributes to neither. At \(s=3\), the second seed adds 1 and 2 at these two weights. In grade three, \(W\) contributes 2 at each, as proved in §2. Thus
\[
\begin{array}{c|cc|cc}
 &\dim S_{2,1,4}&\dim S_{2,1,3}&\dim S_{2,2,4}&\dim S_{2,2,3}\\\hline
s=3&4&4&16&11\\
s\ge4&5&4&18&11
\end{array}. \tag{13}
\]
For clarity, these weight contributions can be checked without counting a character as a map rank. If \(v\) is a lowest \(L(p,q)\) vector with \(p,q>0\), the two vectors \(E_1E_2v,E_2E_1v\) are independent: lowering them gives determinant \((p+1)(q+1)-pq=p+q+1\). PBW bounds that weight by two. At displacement \((1,2)\), the two vectors \(E_1E_2^2v,E_2E_1E_2v\) are independent when \(q>1\), since their \(F_2\) images are \(2(q-1)E_1E_2v\) and \((q-1)E_1E_2v+qE_2E_1v\); PBW again bounds the weight by two. The analogous statement with arms interchanged covers displacement \((2,1)\) of the second \(L(5,2)\). The one-string contributions are nonzero by their positive string labels.

## 6. Actual sl2 surjectivity and the whole boundary isotypic

This step uses the actual map, not a character inference. The adjoints \(E_3,F_3,H_3\) form \(\mathfrak{sl}_2\) on \(S\). Both signs of the Serre relations give local nilpotence of \(E_3,F_3\) on same-sign simple generators; the Chevalley relations give it on opposite-sign generators and on **all** full-Cartan directions. The derivation rule extends local nilpotence to every finite Lie word. For a homogeneous vector, \(\mathfrak{sl}_2\) PBW ordering expresses its generated module using \(F_3^iH_3^jE_3^k\); local nilpotence makes the relevant \(k\) and, for each \(k\), the relevant \(i\) finite, while \(H_3\) is scalar on each homogeneous vector. Hence the generated module is finite-dimensional. In a finite-dimensional \(\mathfrak{sl}_2\) module, lowering is onto any negative weight. Because \(H_3\) has weight \(2n-2a-sb\) on \(S_{a,b,n}\), and \(E_3,F_3\) preserve \((a,b)\),
\[
 2n-2a-sb<0\quad\Longrightarrow\quad
 F_3:S_{a,b,n+1}\twoheadrightarrow S_{a,b,n}. \tag{14}
\]
At \(n=3\), the target weights for \((2,1)\) and \((2,2)\) are \(2-s\) and \(2-2s\), both negative for every \(s\ge3\). Combining the actual surjections with (13) gives
\[
\begin{array}{c|cc}
 &\dim\ker(F_3:S_{2,1,4}\to S_{2,1,3})&
  \dim\ker(F_3:S_{2,2,4}\to S_{2,2,3})\\\hline
 s=3&0&5\\
 s\ge4&1&7
\end{array}. \tag{15}
\]
At \(s=3\), the first map is an isomorphism. Since \(\mathcal R\) is an ideal and the entire-grade-three import says \(\mathcal R\cap S_3=0\), it follows that \(\mathcal R\cap S_{2,1,4}=0\). The grade-four radical is a finite-dimensional Levi submodule; any nonzero intersection with the whole \(L(1,4)\) isotypic contains a nonzero lowest vector at \((2,1)\), impossible by the preceding actual root-space result. This excludes the **whole isotypic**, including all diagonal copies. At \((2,2)\), the radical's lowest space lies inside the five-dimensional root kernel at \(s=3\), giving only the stated upper bound 5 of the six copies.

The converse \(v\in\mathcal R\) iff \(F_3v=0\) is available under S6 only after \(v\) is an actual homogeneous **simultaneous** \(F_1,F_2\)-lowest vector. It is not applied to an arbitrary root-kernel vector. No claim is made that a nonzero radical vector exists, that the \(L(2,2)\) bound is sharp, or that the \(s\ge4\) lowest map has full rank.

## 7. Limits and complete read declaration

The asserted new \(L(0,3)\) vector and resulting complete first-relation image are manual author claims, not independently reviewed or adopted. This note does not evaluate f809's affine-pencil minors, prove an all-\(s\) \(L(1,4)\) radical exclusion, determine the other complete lowest \(F_3\) maps, settle all of the grade-four radical, or establish anything at higher grades or globally. Its conclusions depend on the actual-source/whole-ideal/full-Cartan bridge and entire-grade-three input as named in §1. Status-only controls are not mathematical inputs; source links did not authorize any other body.

Before any packet body or mathematical reasoning, I read the manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all **23** listed status-only controls, then exclusively wrote `prebody-ack-v1.md`. The administrative dispatch receipt initially displayed several long lines clipped; I recovered the complete raw line 59 and all clipped task/assignment lines 72–73, 89–90, 106–107, 123–124, 140–141, 157–158 and 174–175 before the acknowledgment. The general memory summary itself was displayed with long-line truncation and was not a mathematical source. Parent-supplied hashes below are metadata; I did not independently rehash the originals.

After the acknowledgment I read packet part 1 **serially** in raw windows 1–20, 21–40, …, 741–760, 761–766 through its ending, then part 2 serially in raw windows 1–20, 21–40, …, 301–320 through its ending, all before mathematical reasoning. Every display was below 30,000 bytes and every window at most 20 LF. No packet body clipping or packet-read failure was observed. The parts' supplied pins are `2b7181938ed545680b14a72caf223cc16ed489792a3efcf123ee53805beebfb0` and `d699d9b99288ab19d4958d18526f76903aa098f60bc0f1d35fd45989d20da96e`, respectively. They render every complete literal body listed below, including its ending; paths are relative to `institute/runs/three-area-2026-10-27-96h/`:

| ID | Complete literal source body | LF | Parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f809-kac-small-r-grade4-whole-overlap-frontier-author/author-candidate-v1.md` | 1–203 | `a47c4500fc61da5150dd40f914230b70407442c630efbad41b4ab672f059c37b` |
| S2 | `review-waves/f773-kac-grade4-singlet-and-lowest-ideal-proof-author/author-independent-singlet-ideal-and-overlap-v1.md` | 1–212 | `f71ca32c5404742c0bc8c54ed2848020632032e0d6bd8a5142ac55092eff7883` |
| S3 | `review-waves/f757-kac-grade4-complete-lowest-map-frontier-author/author-complete-lowest-map-frontier-v1.md` | 1–231 | `490561e0239e568534190175fc2c889887390ded133fe1b9dd6c0804a5a8d8fb` |
| S4 | `review-waves/f757-kac-grade4-complete-lowest-map-frontier-author/author-complete-lowest-map-frontier-v1-addendum-1.md` | 1–15 | `6c8f33ad9fce860868482e06ff821baac8cf1381900941436e795cb487aea5eb` |
| S5 | `dispositions/math-3-actual-grade4-complete-character-and-root-kernel-ten-parent-v1.md` | 1–25 | `f8cf56158c127497bdd75487b9dbc99d26e5e32a8fadcbbd818b663f4049d889` |
| S6 | `dispositions/math-3-grade4-entire-singlet-selected-submodule-and-lowest-ideal-criterion-parent-v1.md` | 1–23 | `c75905ed6751ee0af9d77042adbcf0eb35947bacecbfa95411f5a4699547c7db` |
| S7 | `dispositions/math-3-actual-free-source-and-full-serre-ideal-at-displayed-presentation-parent-v1.md` | 1–27 | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` |
| S8 | `review-waves/f703-kac-grade3-radical-f3-multiplicity-independent-author/author-independent-reconstruction-v1.md` | 1–314 | `f856b62e2f8261ff0c272ccff33431cdbd014aa4ef7a6f27aca6f445c288ab5e` |

No unlisted mathematical source, genuine held episode or its proof/method/planning/selection/verification/reporting/confidence/downstream consumers, sibling mathematical return, or old code was opened. No network, child process, scientific execution, tests, compilation, solver, external-model call, Git, deletion, build, formatter, or linter was used. No verifier code was prepared, so there is no prepared-code hash. The ordered-read and access statements do not certify unobservable cognition. Parent disposition and separate review remain outstanding.
