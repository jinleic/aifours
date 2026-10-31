# ORIGINAL remaining seven maps: a full fixed-tensor walled-Brauer lowering operator

Owner MathKacMoody-2. Actual preceding `/bin/date`: **Mon Oct 26 07:24:17 PDT 2026**. NEW immutable exact WRITTEN representation, not a rank theorem, numerical certificate or scientific execution. No interpreter/Eval/CAS/calculator/program/enumeration/solver/replay/CLI/nested agent/GO was used. All formulas below follow from trace completeness/PBW/permutation identities in writing.

## 1. Actual original scope and held-lead chronology

The lead was already saved before v121-E intake in `peer-review-v121-E-primary-checkpoint-v1.json`, SHA256 `59b6088b04da5cc52e0b8f65f0126fd671365e76d9778783cd791749c4036e43`. It is not a new post-review discovery/preregistration. After that review ACTUALLY RETURNED, the NEW WHOLE primary ACK `primary-whole-resumption-after-v121-E-ack-v1.json`, SHA256 `221e8a49036494c11c25b5cb7ade05f3c504690f3739a740745450526b1d1735`, actual07:02:13, was WRITTEN and SENT before the present source/proof work. No live review is interleaved.

Retain original A(r,s)=[[2,-1,-1],[-1,2,-1],[-r,-s,2]], actual ORIGINAL third-row lowering, finite Levi sl3 on nodes1/2, V=ad(sl3), W=V*, and ALL seven nontrivial level-five primitive maps. The invariant type is separately supported at its exact prior imports; it is not re-opened or used to prove another type. The new model is a change of representation for the entire fixed free source, not an additional selected line or a nonzero determinant sampled at one parameter.

The COMPLETE380-LF row-one local source and its mandatory editorial overlay, COMPLETE333-LF nontrivial64/35 source/end, and COMPLETE266-LF structural interface/end were read after the earlier proper whole-primary ACK and before the held lead; they remain unchanged. Only their exact positive presentation/local row conventions are reused. No old unadmitted coefficient table or finite determinant is a correctness premise below.

## 2. Exact positive and negative local modules, with ORIGINAL r/s orientation

Let E=C3 with its compact-unitary form, E* its unitary linear dual. Identify End(E)=E tensor E*, and V=sl(E) with the orthogonal projection

    P(y)=y−Tr(y)I/3.

For traceless Hermitian X define the compressed left and dual-right partial actions

    A_X(y)=P(Xy), B_X(y)=−P(yX), y in V.                    (2.1)

They are Hermitian for the Hilbert-Schmidt form and equivariant vector operators. Individually they are NOT asserted representations after compression. Their sum and difference are EXACTLY

    A_X+B_X=ad_X,
    A_X−B_X=d_X, d_X(y)=Xy+yX−(2/3)Tr(Xy)I.                (2.2)

Set alpha=(r+s)/2,beta=(r−s)/2,kappa=2−r−s. The original local bracket is

    [w_x,u_y]=alpha[x,y]+beta*d(x,y)−Tr(xy)z0,
    [z0,u_y]=kappa*u_y.

With a trace-orthonormal Hermitian basis X of sl3, its finite part has the moment expression

    [w,u]=−sum_X w(Q_X u)X−w(u)z0,
    Q_X=alpha*ad_X−beta*d_X=s*A_X+r*B_X.                   (2.3)

To check the sign and r/s orientation, Tr(w[X,u])=−Tr([w,u]X), whereas Tr(w d_Xu)=Tr(d(w,u)X). Thus the leading minus gives precisely alpha commutator PLUS beta Jordan term. Since alpha−beta=s and alpha+beta=r, the actual row weights are **s on LEFT, r on DUAL-RIGHT**, not reversed. This holds for ALL original positive r,s, without changing the matrix to a symmetrizable row or importing a full-algebra invariant form.

At degree n the actual z0 action is n*kappa. The following operators keep this full level action by counting every later slot separately.

## 3. Exact fundamental permutation/contraction identities

Embed V^tensor n isometrically in(E tensor E*)^tensor n. Write P_global for the product of the n traceless projections. For distinct copies i,j let

- L_ij swap the two E factors;
- R_ij swap the two E* factors;
- K_(i,j*) contract E_i with E_j*, then reinsert the standard coevaluation;
- K_(i*,j) do the opposite cross contraction.

The swaps are Hermitian unitaries, commute with one another, and their product is the WHOLE-copy swap. Each K is positive semidefinite and satisfies K²=3K. Partial swaps/contractions need not preserve the individual V factors; EVERY formula below is compressed by P_global, not silently restricted as if they did.

Trace completeness, `sum_X X tensor X = swap−I/3` on E tensor E, gives

    sum A_i(X)A_j(X)=P_global(L_ij−I/3)P_global,
    sum A_i(X)B_j(X)=P_global(−K_(i,j*)+I/3)P_global,
    sum B_i(X)B_j(X)=P_global(R_ij−I/3)P_global,
    sum B_i(X)A_j(X)=P_global(−K_(i*,j)+I/3)P_global.         (3.1)

These are exact DIFFERENT-copy compression identities; no illegal same-copy product Q(X)Q(Y)=Q(XY) is used. Since total rho_j=A_j+B_j preserves V_j, the scalar thirds cancel in each row:

    sum Q_i(X)rho_j(X)
      =P_global[s*(L_ij−K_(i,j*))
                    +r*(R_ij−K_(i*,j))]P_global.            (3.2)

This is the normalized walled-Brauer form of the ORIGINAL local coupling, with no unspecified Clebsch channel.

Define the Hermitian ordered-pair operator

    M_ij=−kappa I−sum Q_i(X)rho_j(X)
      =P_global{s*(I−L_ij+K_(i,j*))
                +r*(I−R_ij+K_(i*,j))−2I}P_global.          (3.3)

The two row pieces I−swap+K are positive semidefinite in the ambient unitary tensor space. Their compression remains positive. This gives the exact coarse bound M_ij>=−2I, but NOT positivity of every pair/channel, and certainly not a free degree-five rank verdict.

As a normalization/control consequence on a source antisymmetric under the WHOLE-copy swap i,j, R_ij x=−L_ij x in the ambient space. Therefore

    <x,M_ij x> >=[2min(r,s)−2]||x||².                       (3.4)

This is a whole-pair quadratic inequality, not a finite parameter trial. It does NOT say a sum with later noncommuting front permutations is positive. At min(r,s)=1 the actual quadratic Serre kernels must remain; no false strictly-positive bound is asserted there.

## 4. The COMPLETE coherent derivative on a free Lie tensor

Let f in L_n(V) be embedded by PBW in V^tensor n. Let T_i move WHOLE slot i to the front and leave all other old slots in order, T_1=I. For a natural-dual basis u_a,w_a define

    mathcalD_n f=sum_a u_a tensor D_(w_a)f.

The EXACT ORIGINAL coherent lowering is

    mathcalD_n f =sum_(1<=i<j<=n) T_i M_ij f.                (4.1)

The target is V tensor L_(n−1)(V), included in the same n-fold ambient tensor. This specifies EVERY source and EVERY output coefficient, not a selected block.

Proof: apply the original commutator derivation to a tensor word. For each i<j, deleting old slot i and replacing old slot j by the finite local action gives the coupling−Q_i*rho_j; the central contraction contributes−kappa. Coherent insertion restores the dual-contracted old i at the FIRST slot, hence T_i. Summing all ordered pairs gives(4.1). Far-right degree-zero remnants cancel on a homogeneous Lie polynomial: for each scalar coordinate they are the ordinary derivation sending generators to scalars, which kills every bracket of degree>=2. This cancellation is not an assumed associative negative representation. Central action on each later slot is retained, so a degree-k subbracket receives k*kappa rather than one kappa.

For n5 the original remaining maps are therefore controlled by the completely explicit ten-pair, fixed-tensor affine pencil

    mathcalD_5(r,s)=r*B5+s*A5−2G5,
    A5=sum_i<j T_i P_global(I−L_ij+K_(i,j*))P_global,
    B5=sum_i<j T_i P_global(I−R_ij+K_(i*,j))P_global,
    G5=sum_i<j T_i.                                         (4.2)

A5/B5 are NOT declared Hermitian/positive merely because the unpermuted row pieces are positive. T_i matters. Treating(4.2) as a positive convex combination without controlling those permutations would solve the wrong operator.

## 5. Entire-source Young geometry, with no five-block independence assumption

Classical PBW/Witt gives the degree-five Lie-operad Frobenius character(p1^5−p5)/5. Under Schur-Weyl the multiplicity of a partition lambda of5 is(dim Specht_lambda−chi_lambda(5cycle))/5. The exact seven-partition values are:

|partition|Specht dimension|5-cycle character|Lie multiplicity|
|---|---:|---:|---:|
|(5)|1|1|0|
|(4,1)|4|−1|1|
|(3,2)|5|0|1|
|(3,1,1)|6|1|1|
|(2,2,1)|5|0|1|
|(2,1,1,1)|4|−1|1|
|(1,1,1,1,1)|1|1|0|

The five surviving Specht dimensions4+5+6+5+4=24=(5−1)! exhaust the multilinear Lie source. Thus, as a GL(V) functor,

    L5(V)=S41(V)+S32(V)+S311(V)+S221(V)+S2111(V),             (5.1)

each once. This is an ENTIRE source representation, not a guess from dimensions of a particular sl3 primitive type. It can be defined by the usual finite Young idempotents and the degree-five Dynkin image without a numerical basis search.

The walled-Brauer pair couplings in(4.2) need not commute with the central S5 Young projectors. Hence one must keep ALL off-diagonal Young components of A5/B5; five independently checked diagonal blocks would NOT be a whole-source proof. Formula(5.1) supplies a complete fixed source geometry while explicitly preserving that coupling risk.

## 6. Actual quotient return, especially the entire r,s>=4 quadrant

For ALL parameters retain the literal WHOLE Serre ideals

    T4=adV²Q2+adV Q3+Q4,
    T5=adV³Q2+adV²Q3+adV Q4+Q5.

The original-row derivative sends T5 into T4; the tensor operator(4.1) must therefore be tested on ACTUAL quotients, not arbitrary free representatives with target relations forgotten. At small rows this target-leak/lift issue remains and is not cured by a walled-Brauer rewriting.

In the ENTIRE quadrant r,s>=4 there is a clean exact specialization. Q2/Q3/Q4 are absent, so T4=0. T5 is only the entry4 modules Q5=154/154star, absent from all eight selected primitive types. Finite sl3 semisimplicity therefore identifies each selected source isotypic component with its entire free component, while the WHOLE target is literally free L4(V). For any actual F1/F2-lowest source, D3 zero implies EVERY W derivative zero by negative-Levi generation/Jacobi; conversely that includes f3.

Consequently on EACH of the seven remaining nontrivial primitive types, for EVERY r,s>=4,

    ACTUAL original map kernel = FREE coherent kernel
       of(4.2) on the ENTIRE selected lowest source.           (6.1)

This is an equality at the actual ideals, not a source count or an invariant-target detector transfer. No original Q5 is removed from a claimed whole quotient; it is omitted only after the selected-isotypic argument. At entries1/2/3 one must return to the full quotient or the exact finite-Levi correction packets.

The seven source degrees remain(2,2,5),(3,2,5),(2,3,5),(3,3,5),(4,3,5),(3,4,5),(4,4,5). Their targets are the corresponding ACTUAL original degrees with last coordinate4. The invariant degree(5,5,5) stays separately settled at its named old gate; no eight-target adjoint identification is transferred to a nontrivial type.

## 7. Consequential replacement and exact remaining obligation

This representation replaces a large parameter-dependent Chevalley/tensor expansion by a fixed unitary diagram algebra with ten ordered pairs, two positive unpermuted row pieces, explicit central term and ALL source Young components. It establishes every operator coefficient/normalization and the exact actual-kernel interpretation; it does NOT establish injectivity of the affine five-source-Young operator or of a remaining full primitive map.

The next valid step is a complete coupled Young/diagram positivity or detector theorem for(4.2), or an actual nonzero quotient kernel, at the full original source. A diagonal-rank control, one Young summand, copied invariant determinant, unpermuted pair positivity or an invented Casimir-only scalar is insufficient. The lower-pair form theorem in the finite-Levi companion gives further intermediate-channel control but does not remove these front-permutation/higher-hook couplings.

All original r1 four separate families/r2/r3/grade4/general-aJ3M_R/import gaps, general F5/B5/Serre, H13EXTRA/old19/B4/H223/F64 and outside-band(4,4,6) boundaries remain. No blanket family/grade3 adoption, novelty or source-count promotion follows. ALL old parent/owner freeze/ACK/source/35star/cadence/admission findings, including my v114 observed36:10/6:10 PROCESS MAJOR, remain permanent. Same18/original cutoff/deadline/<=30min substantive checkpoints/HOLD/exclusive own-root new-file rules persist; no scientific execution, new GO, shared/frozen edit, config/Git/deletion/publication or early park/round closeout.
