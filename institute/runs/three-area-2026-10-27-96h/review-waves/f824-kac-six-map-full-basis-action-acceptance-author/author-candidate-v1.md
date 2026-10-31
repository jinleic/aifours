# F824 — exact actual-quotient join and grade-four union, conditional on the six full data comparisons

**Status: NONBLIND GENERAL-AUTHOR CANDIDATE; NOT a parent disposition.** This note gives an exact, finite construction of each *actual* simultaneous-lowest quotient and its actual third lowering, proves a full-rank/grade-four-radical equivalence at the named imports, checks the Jacobi table and the whole 81-dimensional relation, and reconstructs the whole-grade-three and 13-type union arguments. The parent reports an exact raw-token transport check and a separate six-polynomial arithmetic replay. They are valuable **reported** evidence for the emitted pencils; neither pays the missing comparison of all six emitted lowest tensors and full image columns with the actual construction. Those complete tensors and columns are not in the F824 packet. I did not open the linked but unlisted dossier bodies. Consequently the unconditional actual grade-four theorem is **not established by this note**.

## 1. Quantifiers and load-bearing imports

Let

\[
A(3,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-3&-s&2\end{pmatrix},\qquad s\in\mathbb Z,\ s\ge4,
\]

and let \(\mathcal C\) be **any full complex Cartan realization**, including extra directions. In the preliminary Chevalley algebra \(G_{\mathcal C}\), let \(J\) be the **whole ideal of both signs of all Serre relations**, let \(\tau\) be the maximal ideal disjoint from the whole Cartan, and put \(S=G_{\mathcal C}/J\), \(R=\tau/J\). Write \(S_{a,b,n}\) for root degree \((a,b,n)\), and \(S_n=\oplus_{a,b\ge0}S_{a,b,n}\). Let \(E_i=\operatorname{ad}e_i\), \(F_i=\operatorname{ad}f_i\).

The following are explicit mathematical imports, not consequences of a receipt or an original-book identity:

* **SRC.** Packet S9's actual ordinary-free-Lie/tensor-embedding source, its eight-letter Levi action, whole-Cartan injection and root grading, and its bridge for the whole positive-and-negative Serre ideal at the displayed presentation. In particular, the actual positive grade-four quotient is the ordinary free Lie-four module modulo the complete grade-four relation, not a selected model quotient; grade three is free for this parameter range. Use characteristic zero and the standard finite-dimensional \(\mathfrak{sl}_3\) complete-reducibility and Weyl-character facts.
* **G2.** The complete actual grade-two radical exclusion used by S10's grade-three argument. Section 5 reconstructs its consequence **G3:** \(R\cap S_3=0\), at SRC and G2. Independently, the packet's parent dispositions also name the entire G3 import. We do not infer G3 from a finite sample or from a chosen grade-three component.
* **ISO.** The earlier exclusions of the **whole** \(L_{\rm low}(5,2)\) and \(L_{\rm low}(3,3)\) isotypics from \(R\), including all multiplicity-space combinations. The relevant earlier proof is not a body input here, so this is an import, not a new independent verification.
* **TRIV.** Packet S8's exclusion of the **entire** actual grade-four singlet isotypic from \(R\). Its separate selected 100-dimensional submodule cannot replace an entire-isotypic statement.
* **CA-join and CA-arithmetic.** The six complete emitted lowest-basis/action identities and the selected determinant identities stated precisely in §§6–7. S5 and S6 report transport and replay respectively; their results are not the full basis/action comparison and are not independently re-executed here.

Full-Cartan injection matters twice: it prevents an extra Cartan direction from being silently killed, and the linearly independent simple roots of a full realization separate the root degrees used in the ideal argument. Nothing in this note authenticates the original printed source or upgrades another presentation to this one.

## 2. Written check of the eight-letter Jacobi action

Use the **distinct** ordinary tensor letters

\[
(x,a,b,c,d,e,f,g)=(e_3,E_1x,E_2x,E_1E_2x,E_2E_1x,-\tfrac12E_1^2E_2x,\tfrac12E_2^2E_1x,E_1f).
\]

Their horizontal degrees are `(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)` in this order. These are not products or entries in an 8-by-8 or 3-by-3 matrix model. The imported Levi table is

```
          x  a  b   c   d   e   f   g
E1        a  0  c  -2e -e   0   g   0
E2        b  d  0   f  2f  -g   0   0
F1        0  x  0  2b   b  -c   0   f
F2        0  0  x   a  2a   0   d  -e
```

Directly taking `E1 E2 - E2 E1` on **all eight** columns gives

```
E12 = [E1,E2]:   x    a    b    c    d    e  f  g
                 c-d  -e   -f   -g   g    0  0  0.
```

For example, on `c` the two terms are `g` and `2g`, while on `d` they are `2g` and `g`; this checks the mixed-zero-weight signs, not merely the outer letters. Chevalley commutators and Jacobi give, for general formal \(r,s\),

\[
[F_3,(x,a,b,c,d,e,f,g)]=(-h_3,-re_1,-se_2,-s[e_1,e_2],r[e_1,e_2],0,0,0).
\]

Here `[F3,u]` denotes the action of the third lowering on the letter. Indeed \([f_3,e_i]=0\) for \(i=1,2\), so the `c,d` entries follow immediately from their definitions; the last three vanish by the two fixed \(A_2\) Serres. Thus, writing \(D_u\) for the adjoint action of \([f_3,u]\) on another letter of horizontal degree \((i,j)\), at \(r=3\) one has

\[
D_x=(3i+sj-2)I,\quad D_a=-3E_1,\quad D_b=-sE_2,\quad
D_c=-sE_{12},\quad D_d=3E_{12},\quad D_e=D_f=D_g=0. \tag{1}
\]

For an ordered length-four word \(u_1u_2u_3u_4\), its degree-three output is the sum over **all** \(i<j\): delete \(u_i\), replace \(u_j\) by \(D_{u_i}u_j\), and retain all remaining positions in their original order. Extend linearly. This is not a vacuum assumption: after commuting each degree-zero operator to the right, the residual coefficient of each such operator is the noncommutative deletion derivation of the original tensor with respect to its corresponding letter. That derivation sends its letter to the central scalar 1 and all other letters to 0, and it annihilates every Lie bracket of length at least two because the resulting scalar commutators vanish. Thus all right tails cancel separately on **every genuine Lie tensor**. Equation (1) is an exact affine map \(D(t)=D_0+tD_1\), \(t=s-4\), on the whole free Lie-four space. It need not preserve \(F_1/F_2\)-lowestness in its grade-three target.

## 3. The complete 81-dimensional relation, not one selected seed

Put \(q_k=(\operatorname{ad}x)^k a\) and \(q=q_3\). In the ordinary tensor algebra,

\[
q=x^3a-3x^2ax+3xax^2-ax^3\ne0. \tag{2}
\]

The four words are distinct. Since \(F_1x=0,F_1a=x,F_2x=F_2a=0\), both Levi lowerings kill q. It has grade four, horizontal degree \((1,0)\), and lowest label \((2,5)\). The finite-dimensional Levi module is semisimple; a nonzero lowest vector of this label generates one irreducible *diagonal* copy, even if the surrounding free module has equivalent copies. Weyl's dimension formula gives

\[
\dim U(\mathfrak{sl}_3)q=(2+1)(5+1)(2+5+2)/2=81. \tag{3}
\]

The actual third lowering kills this **whole** copy. To see the nontrivial seed calculation, for general r the derivation rule and \([-h_3,z]=(ri+sj-2n)z\) on grade-\(n\), degree-\((i,j)\) vectors give successively

\[
F_3q_1=2(r-1)a,\qquad F_3q_2=3(r-2)q_1,\qquad F_3q_3=4(r-3)q_2. \tag{4}
\]

Thus \(F_3q=0\) at \(r=3\). Because \([F_3,E_1]=[F_3,E_2]=0\), it also kills every raising translate. The sign of the seed in S9 is opposite to (2), which does not change its span.

SRC identifies this whole cyclic module as the entire actual grade-four relation: the other positive Serre seed begins at grade \(s+1\ge5\), positive outer letters strictly raise grade, and the imported whole-ideal bridge rules out extra effects from negative Serres. The 81-dimensional computation alone would **not** prove that last bridge. Since (4) annihilates the whole relation, (1) descends independently of the representative to the actual, free grade-three target.

For a horizontal degree \(w=(a,b)\), define the actual relation space explicitly by

\[
\mathcal Q_w=\operatorname{span}_{\mathbb Q}\{E_{i_1}\cdots E_{i_m}q:
\#\{i_k=1\}=a-1,\ \#\{i_k=2\}=b\}, \tag{5}
\]

with zero space if a count is negative. The order of every word in \(1,2\) is included. PBW triangular spanning and the lowest property show that (5) is the **whole** weight space of the cyclic module, including all commutator-generated translates; it is not 81 independent copies of the seed and not merely one translate at each weight.

## 4. All 13 lowest types, independently enumerated

The eight-letter horizontal character is \(H=(1+X)(1+Y)(1+XY)\). The ordinary free-Lie-four character and lowest Weyl denominator are

\[
C_4=\frac{H^4-H(X^2,Y^2)^2}{4},\qquad
\Delta=(1-X)(1-Y)(1-XY)=1-X-Y+X^2Y+XY^2-X^2Y^2. \tag{6}
\]

The lowest label at horizontal degree \((a,b)\) is \((4-2a+b,4+a-2b)\). Its two nonnegativity inequalities imply \(0\le a,b\le4\), and enumeration gives exactly the 13 positions below. To make the coefficient check reproducible without relying on the reported table, set

\[
N(a,b)=\sum_k\binom4k\binom4{a-k}\binom4{b-k},\quad
N_2(a,b)=\begin{cases}\sum_k\binom2k\binom2{a/2-k}\binom2{b/2-k},&a,b\text{ even},\\0,&\text{otherwise},\end{cases}
\]

where out-of-range binomials and negative-index coefficients are zero. In the table, `dN=[X^aY^b] ΔH^4`, `dN2=[X^aY^b] ΔH(X²,Y²)²`, and the free lowest multiplicity is `(dN-dN2)/4`:

| (a,b) | label | dN | dN2 | free | actual | whole-type disposition |
|---|---|---:|---:|---:|---:|---|
| (0,0) | (4,4) | 1 | 1 | 0 | 0 | absent |
| (0,1) | (5,2) | 3 | -1 | 1 | 1 | ISO |
| (0,2) | (6,0) | 2 | 2 | 0 | 0 | absent |
| (1,0) | (2,5) | 3 | -1 | 1 | 0 | complete 81 relation |
| (1,1) | (3,3) | 12 | 0 | 3 | 3 | ISO, all three copies |
| (1,2) | (4,1) | 15 | -1 | 4 | 4 | map A |
| (2,0) | (0,6) | 2 | 2 | 0 | 0 | absent |
| (2,1) | (1,4) | 15 | -1 | 4 | 4 | map B |
| (2,2) | (2,2) | 33 | 5 | 7 | 7 | map C |
| (2,3) | (3,0) | 20 | -4 | 6 | 6 | map D |
| (3,2) | (0,3) | 20 | -4 | 6 | 6 | map E |
| (3,3) | (1,1) | 32 | 0 | 8 | 8 | map F |
| (4,4) | (0,0) | 8 | 4 | 1 | 1 | TRIV, entire singlet |

The actual column follows from removing the one whole \((2,5)\) copy, not from subtracting a single root-weight vector. As a consistency check, free dimension `(8^4-8^2)/4=1008`, and

`81 + 3·64 + 4·35 + 4·35 + 7·27 + 6·10 + 6·10 + 8·8 + 1 = 927 = 1008-81`.

This is a character/decomposition check, **not** a map-rank check. Absence of a lowest type does not mean its horizontal root space has no raised vectors. ISO and TRIV must eliminate whole isotypics: a diagonal copy in two equivalent summands can avoid any one selected summand.

## 5. Check of the whole grade-three import at SRC and G2

This section specializes the packet S10 construction to \(r=3,s\ge4\). There is no grade-three relation by §3/SRC, so \(S_3=\operatorname{Lie}_3(V)\), \(S_2=\Lambda^2V\). Its complete character is

\[
3L(1,1)\oplus L(0,3)\oplus L(3,0)\oplus2L(2,2)\oplus L(1,4)\oplus L(4,1),\quad \dim=168. \tag{7}
\]

For transparency, the standard identity \(\operatorname{Lie}_3(V)=(V\otimes\Lambda^2V)/j(\Lambda^3V)\) has \(j(v\wedge w\wedge z)=v\otimes(w\wedge z)+w\otimes(z\wedge v)+z\otimes(v\wedge w)\); wedge projection sends \(j\) to three times the identity. Equation (7) is the full multiplicity statement used below.

Let \(q_0=[x,a]\), \(q'_0=[x,b]\), and

\[
Q_1=E_2q_0,\quad Q_2=E_2^2q_0,\quad Q_3=E_1E_2q_0,\quad Q_4=E_1E_2^2q_0.
\]

The explicit lowest vectors on one side are

\[
\begin{aligned}
T_{35,r}&=[x,q_0],\\
T_{27,r}&=3[b,q_0]-[x,Q_1],\\
T_{10,r}&=[c,q_0]-2[d,q_0]+[a,Q_1]-[x,Q_3],\\
T_{8,r}&=[x,Q_4]-2[a,Q_2]-4[b,Q_3]+4[d,Q_1]-12[f,q_0].
\end{aligned} \tag{8}
\]

Their other-side partners are obtained by the **formal simultaneous source substitution**
`(x,a,b,c,d,e,f,g;r,s) -> (x,b,a,d,c,-f,-e,g;s,r)`, not by claiming an automorphism of a fixed nonsymmetric Cartan matrix. Put `A=[x,c]`, `B=[x,d]`, `C=[a,b]`. Formula (1) gives

\[
\begin{aligned}
F_3T_{35,r}&=3q_0,&F_3T_{35,s}&=3(s-2)q'_0,\\
F_3T_{27,r}&=(-3-4s)B+(4s-13)C,&
F_3T_{27,s}&=(-6-3s)A+(5s-14)C.
\end{aligned} \tag{9}
\]

The three displayed exterior pairs are independent, and the two unique A/B coefficients are nonzero; hence the **entire double 27 multiplicity space** is separated. For the two 10s, using `(A_r,B_r,C_r)=([c,a],[d,a],[x,e])` and `(A_s,B_s,C_s)=([d,b],[c,b],-[x,f])`, the respective images are

\[
(-7-2s,\ 2s-1,\ 15+2s),\qquad(-4-3s,\ 8-s,\ 7s). \tag{10}
\]

Each triple consists of independent exterior pairs and has a nonzero first coefficient.

For the third adjoint let \(Y=A-B-C\), \(Y_1=E_1Y\), \(Y_2=E_2Y\), \(Y_3=E_1E_2Y\), and \(Z=[x,Y_3]-2[a,Y_2]-[b,Y_1]+[d,Y]\). The table gives the lowering identities needed to make all vectors in (8), their primed partners, and Z lowest. For instance, the `T8,r` F1 terms cancel using `F1 Q3=Q1`, `F1 Q4=2Q2`; its F2 terms cancel using `F2 Q1=3q0`, `F2 Q2=4Q1`, `F2 Q4=4Q3`. The same direct table check applies to Z.

In exterior coordinates `(P,Q,U,T)=([x,g],[a,f],[b,e],[c,d])`, their third-lowering columns, before specializing r, are

\[
\begin{aligned}
v_r&=(16r+8s-12,\ 28r+8s-24,\ -4r-8s,\ 12r+8s-8),\\
v_s&=(8r+16s-12,\ 8r+4s,\ 24-8r-28s,\ 8-8r-12s),\\
v_Z&=(6-7r-5s,\ 4s-r,\ 6-5r-4s,\ 2-3r-2s).
\end{aligned} \tag{11}
\]

The identity \(v_Z=-v_r/4+3(r+s-1)(-1,2,-2,0)\) and column operations give the `(P,Q,T)` determinant

\[
18(r+s-1)(8r+12s-8)(16r+8s-12)
=18(s+2)(16+12s)(36+8s)>0. \tag{12}
\]

Thus all three adjoint images are independent. Together with (7), (9)–(12) establish the complete lowest multiplicity-space injections in grade three, not only one copy of each repeated type. Since R is an ideal and G2 says \(R\cap S_2=0\), a nonzero finite-dimensional Levi submodule of \(R\cap S_3\) would contain a lowest vector killed by \(F_3\), contradicting those injections. Hence **G3** holds at SRC and G2. This does not claim injectivity on all raised grade-three root vectors.

## 6. Exact, data-independent construction of the six missing joins

This section defines the actual quantities without assuming any producer's basis, and makes the remaining comparison finite and exact.

For each weight \(w=(a,b)\), take all right-nested length-four brackets of the eight letters whose horizontal degrees sum to w; view them as ordinary tensor-word columns. Jacobi makes their span \(U_w\) the entire free Lie-four weight space. Order bracket columns lexicographically by the displayed letter order and choose a rational basis by greedy independence. Construct \(\mathcal Q_w\) from **all** words in (5), again choosing a rational independent basis. Extend that basis to a basis of \(U_w\) by greedy columns, and call the added columns \(B_w\). This is a deterministic definition after fixing the order; no producer code, sample rank, or selected representation is involved.

For \(i=1,2\), take \(Q_i\) to be an independent matrix of **all** relation columns in \(\mathcal Q_{w-\mathbf e_i}\), with an empty matrix for a negative weight. Form the two block matrices, in the complete target tensor-word coordinates,

\[
A_w=\begin{pmatrix}F_1B_w&-Q_1&0\\F_2B_w&0&-Q_2\end{pmatrix},\qquad
H_w(t)=\begin{pmatrix}F_1B_w&-Q_1&0\\F_2B_w&0&-Q_2\\D(t)B_w&0&0\end{pmatrix}. \tag{13}
\]

Each \(Q_i\) has independent columns and the two relation blocks occupy disjoint summands. Therefore projection of \(\ker A_w\) onto the \(B_w\)-coordinates is injective and its image is **exactly** the full simultaneous \(F_1,F_2\)-lowest space in the actual quotient. Projection of \(\ker H_w(t)\) is exactly its \(F_3\)-kernel. No identification of a root-space kernel with R is used. The first columns of H represent actual quotient coordinates; the extra columns only certify descent of both Levi lowerings modulo their **whole** relation spaces.

For the six weights the following sizes follow from (6) and (5). In this range the relative \((2,5)\)-character has coefficient `min(a-1,b)+1`, because the first numerator corrections occur outside the displayed weights. The `H columns` count includes both relation-coordinate blocks.

| w | dim free root | dim Q_w | dim B_w | dim Q_1 | dim Q_2 | H columns | dim ker A_w |
|---|---:|---:|---:|---:|---:|---:|---:|
| (1,2) | 10 | 1 | 9 | 0 | 1 | 10 | 4 |
| (2,1) | 10 | 2 | 8 | 1 | 1 | 10 | 4 |
| (2,2) | 25 | 2 | 23 | 1 | 2 | 26 | 7 |
| (2,3) | 36 | 2 | 34 | 1 | 2 | 37 | 6 |
| (3,2) | 36 | 3 | 33 | 2 | 2 | 37 | 6 |
| (3,3) | 65 | 3 | 62 | 2 | 3 | 67 | 8 |

Consequently, for a real formal t, actual-lowest injectivity is exactly

\[
\operatorname{rank}H_w(t)=\#\text{columns of }H_w(t). \tag{14}
\]

Equivalently, the explicitly defined polynomial \(C_w(t)\), the **sum of squares of every maximal column minor** of \(H_w(t)\), is positive at t. This is a finite exact construction, not a claim that we have evaluated its many minors. Its real-parameter interpretation is only formal; the actual Serre interpretation is at integers \(t=s-4\ge0\).

Let \(\ell_{w,1},\ldots,\ell_{w,m}\) and \(A_{w,0},A_{w,1}\) denote the *actual emitted tensors and full column families*, in their emitted order, for the corresponding six dossiers. The remaining CA-join can be paid, for each w, by the following **complete** exact comparisons:

1. Check every \(\ell_{w,j}\) is a genuine length-four Lie tensor in \(U_w\), with the stated weight, not merely an arbitrary associative tensor. Include all tensor-word coefficients.
2. Check `rank([Q_i | F_i ell_1 | ... | F_i ell_m]) = rank(Q_i)` for **both** i, using the whole relation bases in (5).
3. Check `rank([Q_w | ell_1 | ... | ell_m]) = dim(Q_w)+m`. Together with the independently reconstructed multiplicity in §4, this proves that their classes are a basis of the **entire** actual lowest space, including diagonal combinations.
4. Compute (1) coefficientwise on every \(\ell_{w,j}\) and compare **every** grade-three tensor-word coefficient, separately for constant and t terms, with the corresponding columns of \(A_{w,0}\) and \(A_{w,1}\). Check the complete selected row labels/order and normalization against the exact columns. The relation vanishing in §3 makes this comparison independent of the chosen lift.
5. Check the selected determinant polynomial against the six full coefficient lists in §7 by exact arithmetic, with the signed multiplier. This is separate from (1)–(4): a positive minor of unrelated columns, a good ratio, a lost-copy control, or two sample ranks cannot prove actual basis/action completeness.

All six sets of emitted lowest tensors and both full column families are absent from this packet. Thus I cannot perform checks 1–4 here. S6 reports a separate replay of check 5 against its inputs, not these actual-source checks.

## 7. Exact reported arithmetic, transport, and their limits

The following are the **full** reported positive coefficient lists, in increasing powers of `t=s-4`, for `P_w(t)=epsilon_w det M_w(t)`; M has the selected rows in the given order. In S6 the first three row matrices are reported compared with their full columns; the last three are reconstructed from row labels and full columns, not separately emitted matrices.

| w | m | selected tensor-word rows | epsilon | reported coefficients of P_w |
|---|---:|---|---:|---|
| (1,2) | 4 | xxf, xbc, xbd, xcb | +1 | 1157976, 1072872, 344952, 42552, 1296 |
| (2,1) | 4 | xxe, xac, xad, xca | -1 | 864 |
| (2,2) | 7 | xxg, xaf, xbe, xcc, xcd, xdc, xdd | -1 | 1319983104, 2642613760, 1856734208, 644346112, 122319616, 12723200, 658432, 12288 |
| (2,3) | 6 | xcf, xdf, xfc, xgb, abf, bcc | -1 | 3697490645581824, 3484683925438464, 1255344568418304, 217464747687936, 18189659013120, 589934886912 |
| (3,2) | 6 | xag, xce, xde, xec, xga, abe | -1 | 1880785008, 2390437656, 1211796288, 312420240, 43069320, 2997648, 81648 |
| (3,3) | 8 | xcg, xdg, xef, xfe, xgc, xgd, abg, acf | +1 | 13068287740523588400, 15710405256803970000, 8217192601033146720, 2444563237731287760, 452540115016407360, 53319016237430160, 3889462476079440, 159225675739200, 2752864380000 |

If those are the actual determinant coefficients, every P has positive constant and all other coefficients nonnegative, so \(P_w(t)>0\) for every real \(t\ge0\). This is a uniform symbolic sign argument, not finite interpolation or a large-tail inference. The sole selected matrix fully displayed in the present packet is the `(2,1)` pencil:

```
[ 27+3t   54+6t   40+4t   -10-t ]
[ 15+2t   15+2t   53+6t      -2 ]
[  -3-t     6+t  -36-5t    -6-t ]
[-19-3t  -34-6t  -36-4t     6+t ]
```

For this displayed matrix, independently in writing, adding row 1 to row 4 gives `4(2,5,1,-1)`. Eliminate the last column with that row and expand: its determinant is `-4 det N`, with

```
N = [   t+7     t+4    3t+30 ]
    [ 2t+11    2t+5    6t+51 ]
    [-3t-15  -4t-24   -6t-42 ] .
```

Apply `C3 <- C3-3 C1`, `C1 <- C1-C2`, `R2 <- R2-2 R1`: the determinant becomes that of

```
[   3      t+4       9 ]
[   0       -3       0 ]
[ t+9  -4(t+6)  3(t+1) ] ,
```

which is `216`. The pencil determinant is therefore identically `-864`, and its stated multiplier gives `+864`. This written calculation does **not** show the pencil is the actual F3 action on a complete actual basis.

S4–S5 report that retained raw stdout copies matched their originals byte-for-byte and that a literal-preserving `json(parse_int=str,parse_float=str)` comparison recovered the first semantic object and all 18 last JSONL records exactly. S6 reports `REPLAY_COMPLETE` for all six determinant vectors, 12 sample ranks and 24 reason controls, with explicitly limited scope. I did not rerun or independently inspect those sources, raw artifacts, or dossier bodies; the record does not separately display a numeric exit or timing, which I do not invent. The earlier F807 zero-exit/nonpass-status design flaw remains a real evidence-control finding, not a demonstration that its reported complete result was wrong.

There is an additional exact binding to settle: S1 pins the full `(3,3)` dossier `weight-3-3.json` as SHA-256 `0541d5f39b67eb5db10b4316ebdfc014cdf78747efe293e8bb3fd9e5f069d092`, while S6 says its replay input was `weight-3-3-compact.json` SHA-256 `757dc7ca0390aa9bd658e1ed888b1b710a9755887833653f94d3670097ebd3c7`. The packet does not display their complete fieldwise equivalence or its binding to the raw record. This is an **unpaid join**, not an assertion that either file is corrupted or inconsistent. The actual tensor/action comparison and exact arithmetic must refer to the same fully bound data, including the compact/full relationship if both are used.

## 8. Conditional uniform theorem and exact residual equivalence

Fix any integer \(s\ge4\) and any full complex Cartan realization. Assume SRC, G2, ISO and TRIV as in §1. Sections 2–5 then give the stated relation, full 13-type inventory and G3 at those imports. Under precisely these imports,

\[
R\cap S_4=0
\quad\Longleftrightarrow\quad
\operatorname{rank}H_w(s-4)=\#\operatorname{columns}H_w
\ \text{for all six }w\text{ in §6}. \tag{15}
\]

Equivalently all six explicitly defined \(C_w(s-4)\) are positive. The implication from right to left is the complete union: a nonzero \(R\cap S_4\) contains a nonzero irreducible Levi submodule and hence a lowest vector in one of §4's types. The absent/removed types cannot occur, ISO disposes of both full prior isotypics and TRIV of the entire singlet. The vector must therefore lie in one of the six entire lowest spaces. Ideal stability gives \(F_3v\in R\cap S_3=0\), contradicting (14).

For the reverse implication, suppose an actual homogeneous lowest vector v is killed by all three simple lowerings. Its positive-simple-adjoint span is stable under every simple lowering by Jacobi, is stable under the whole Cartan, and all its roots have third grade at least four. It is therefore an ideal with zero Cartan intersection. By full-Cartan injection, its inverse image in \(G_{\mathcal C}\) is Cartan-disjoint and lies in \(\tau\); thus \(v\in R\). If \(R\cap S_4=0\), each of the six lowest \(F_3\)-kernels is zero, giving the left-to-right direction. This is the S8 homogeneous-lowest criterion reconstructed in the scope needed here; no equality \(J=\tau\) is assumed.

If, **in addition**, the six complete CA-join comparisons in §6 and the six determinant identities in §7 hold for the same exactly bound records, their positive polynomials prove all six ranks for every real formal \(t\ge0\). Hence at every integer \(s\ge4\), every full complex Cartan realization, and the whole both-sign Serre ideal,

\[
R\cap S_4=0,\qquad J_{(a,b,4)}=\tau_{(a,b,4)}\quad\text{for all }a,b\ge0. \tag{16}
\]

Equation (16) is **conditional** on the stated imports and unpaid CA-join; it is not an unconditional adoption. The known ten-dimensional \(F_3\) kernel on the full `(2,2,4)` root space is compatible: that space has dimension 23 whereas its simultaneous-lowest space has dimension 7, and neither the full root-space kernel nor its arbitrary vectors are identified with R.

## 9. Provenance, exact unpaid steps, and exclusions

Before any packet body or body mathematics, I read the complete F824 manifest, freeze receipt, final binding, live metadata, actual dispatch receipt and all 24 named controls for status/permissions only, and sent Main the direct prebody ACK saved as `prebody-ack-v1.md`. I then read the sole part serially as raw windows `1–20, 21–40, ..., 941–960, 961–971`, through its ending. No clipping or recovery event was observed in this pass. I used only the ten complete bodies rendered in that packet as scientific inputs; the packet and source hashes are parent-supplied administrative bindings, not my source-identity or unobservable-cognition certificate.

The exact next mathematical payment is the six complete steps 1–5 in §6, including full tensor/Lie membership, both whole-relation lowering tests, quotient independence/completeness, both full F3 coefficient families, and exact row/determinant binding; also bind the `(3,3)` compact/full record if both are consumed. A separately assigned verifier must be complete, exclusively created and UNRUN until the parent fully reads it and separately authorizes the specific execution. Nothing in this author note supplies such a GO or asserts a sibling's verifier or result. Parent disposition and required independent scrutiny remain separate.

I performed written derivations only: no scientific child, compile, test, solver, CAS, external CLI, old producer/checker, unlisted source, network, Git, installation or deletion. All held episodes and **all** their consumers remain NONINPUT; F775 lost science/code/output are noninput and its supervisor loss remains NO VERDICT. No claim is made for r=1 or r=2, other grades, global \(J=\tau\), source identity, novelty, human review, independent model family, proof kernel, or any automatic gate/parent acceptance.
