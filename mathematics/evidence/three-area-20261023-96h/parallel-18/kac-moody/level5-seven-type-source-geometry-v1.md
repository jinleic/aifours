# Level-five seven-type classification: exact source cells for min(r,s)>=3

Owner MathKacMoody. Verbatim observed clock immediately before creation: **Sun Oct 25 03:57:03 PDT 2026** (`/bin/date`). NEW packet; no pinned original is edited.

**WRITTEN-checked-in-kernel, pending fresh reconstruction.** This packet begins the remaining-seven-type classification by determining actual primitive SOURCE dimensions throughout min(r,s)>=3, with explicit nonzero/independence witnesses for the entry-three relation images. It does NOT infer any of their original D3 map ranks. Integer/Fraction arithmetic occurred only in the owner's persistent eval kernel; no native scientific program, solver, scientific subprocess/background job, model CLI, network publication, nested agent or git operation was used. Metadata-only `/bin/date` and SHA-256 commands were used separately.

## 1. Fixed imports and precise scope

Retain the full complex Serre quotient of A(r,s), the original third row, l=sl3, V=ad(l), and the literal whole ideals

    T4=[V,[V,Q2]]+[V,Q3]+Q4,
    T5=[V,[V,[V,Q2]]]+[V,[V,Q3]]+[V,Q4]+Q5.

The named structural input is `level5-structural-interface-v1.md`, SHA256 `ef56a3c2406f80924ce7a1b5bb9e4ac904398088a1f06c4f68cb4833738bcc44`. Its finite-Levi, positive-presentation, actual-ideal and lowest-vector statements are imports. Its exact isotypic argument permits omitting Q5=154/154* ONLY from these eight selected types, not from the whole quotient. B4 is NOT needed for the character/source statements here. B4 is EXTRA if these primitive maps are used to conclude the whole B5 band.

The companion `level5-full-invariant-quotient-v1.md` proves a positive six-source determinant for the invariant primitive map at its own named imports. That is the new complete quotient verdict, not a premise for the nontrivial source dimensions computed here. The other seven map verdicts and general F5 remain open. H13 stays EXTRA for the optional A(2,1)/(1,2) band consequence.

## 2. Exact free source multiplicities

Let X,Y denote simple-root character variables ONLY in this section, and write

    chi=2+X+Y+XY+X^-1+Y^-1+(XY)^-1,
    Delta=(1-X^-1)(1-Y^-1)(1-X^-1Y^-1).

The free character is (chi^5-psi5(chi))/5. For a highest type L(p,q), its root-coordinate highest weight is lambda=((2p+q)/3,(p+2q)/3), and its multiplicity is the coefficient of X^lambda1 Y^lambda2 in the character times Delta. This is the standard finite Weyl coefficient formula, not a rank heuristic. Exact integer convolution gives:

|lowest full degree|type|multiplicity in V^tensor5|virtual multiplicity in psi5(V)|free L5 primitive multiplicity|
|---|---|---:|---:|---:|
|(2,2,5)|64=L(3,3)|94|-1|19|
|(3,2,5)|35=L(4,1)|100|0|20|
|(2,3,5)|35*=L(1,4)|100|0|20|
|(3,3,5)|27=L(2,2)|180|0|36|
|(4,3,5)|10=L(3,0)|100|0|20|
|(3,4,5)|10*=L(0,3)|100|0|20|
|(4,4,5)|8=L(1,1)|145|0|29|
|(5,5,5)|1|32|2|6|

In particular the Adams entry -1 for 64 is intentional: it is a virtual-character coefficient, not a negative ordinary multiplicity. These computations also give dim L2=28,L3=168,L4=1008,L5=6552. Source multiplicity means dimension of the simultaneous F1,F2-lowest space at the stated FULL degree, not the whole ordinary weight space.

## 3. Entry-three relation geometry: the only affected selected types

For min(r,s)>=3 there is no Q2 or Q3. An entry r=3 contributes

    Q4+ = L(5,2)=81,

and s=3 contributes its dual Q4-=L(2,5). Entry-four Q5 remains in the whole ideal but has no selected type. The elementary adjoint/Pieri rule is

    V tensor L(5,2)
      =L(6,3)+L(7,1)+L(4,4)+2L(5,2)+L(6,0)+L(3,3)+L(4,1).

The dimensions are 154+80+125+162+28+64+35=648. Consequently the source relation image [V,Q4+] can affect ONLY one copy of 64 and one copy of 35 among the eight selected types. For the dual relation, ONLY one copy of 64 and one copy of 35* can be affected. This gives upper bounds on image multiplicity; the explicit witnesses below establish equality and the independence needed when BOTH entries equal three. No tensor-domain multiplicity is silently identified with image rank.

## 4. Explicit Casimir-projected image witnesses

Use the zero-based basis from the companion invariant packet:

    b=(E12,E21,E23,E32,E13,E31,H1,H2),
    H1=diag(1,-1,0), H2=diag(0,1,-1), v=u5.

Take the actual free Serre generator, with an immaterial overall seed sign,

    q+=[v,[v,[v,u3]]].

It generates the full Q4+ relation module: E1v=-u3 in the positive matrix-label model, so q+ is the negative of the usual literal seed. Put

    t64=[u2,q+],          full degree (2,2,5),
    t35=[u4,q+],          full degree (3,2,5).

Let C be the finite-Levi quadratic Casimir acting on tensor/Lie polynomials,

    C=sum_i ad(b_i) ad(b^i),

with the TRACE-DUAL b^i. Its scalar on L(p,q) is

    c(p,q)=(2/3)(p^2+q^2+pq+3p+3q).

On the seven distinct simple types in V tensor Q4+ the possible scalars are precisely

    E={60,54,48,40,36,30,24}.

The duplicated 81 has the same scalar 40 and introduces no Jordan block, because finite sl3 modules are semisimple. Define the following explicit image vectors:

    U64+ = (1/34560) product_(e in E, e!=30)(C-e) t64,
    U35+ = (1/46080) product_(e in E, e!=24)(C-e) t35.     (4.1)

These are nonzero scalar multiples of the Casimir projectors onto the selected simple summands: the respective projector multipliers are -135 and 648. The images remain inside [V,Q4+] because that is a Levi submodule. Their weights are the lowest weights of 64 and 35, respectively; hence they are lowest vectors of those types. In addition, exact tensor arithmetic checked that both simple lowerings annihilate each vector and that their Casimir eigenvalues are 30 and 24.

For a completely finite nonzero check, read coefficients in the tensor embedding. The first two sorted nonzero coefficients are:

|vector|tensor word, zero-based|coefficient|
|---|---|---:|
|U64+|(0,1,5,5,5)|3|
|U64+|(0,5,1,5,5)|3|
|U35+|(0,1,3,5,5)|158|
|U35+|(0,1,5,3,5)|-168|

The normalizations in (4.1) are part of the definition, not fitted nonzero scalings. A pure-integer reconstruction may use 3C and denominators 25194240 and 33592320 instead, since there are six factors and 3^6=729. The resulting tensors have 217 and 378 nonzero coefficients, respectively.

## 5. Two entry-three 64 images are independent, not merely nonzero

Let sigma(x)=-J x^T J^-1, where J is the anti-diagonal permutation matrix. This is the finite diagram automorphism preserving the chosen Borel. It exchanges nodes 1,2 and sends the basis labels as follows:

    u0 -> -u2, u1 -> -u3, u2 -> -u0, u3 -> -u1,
    u4 -> -u4, u5 -> -u5, u6 -> u7, u7 -> u6.

It preserves C, sends Q4+ to Q4-, and preserves the full degree (2,2,5). Set

    U64- = sigma(U64+),     U35- = sigma(U35+).

Thus U64- is a 64-lowest vector in [V,Q4-], and U35- is a 35*-lowest vector there. On the TWO tensor coefficient rows (0,1,5,5,5) and (0,5,1,5,5), the two 64 vectors give

    [ 3   -87 ]
    [ 3   245 ],          determinant 996 != 0.          (5.1)

Therefore the two 64 relation images are independent in the free source. Their sum removes TWO copies of 64 when r=s=3. Nonzero images alone would NOT have proved that. The 35 and 35* images lie in different isotypic components and are automatically independent of one another and of 64.

Equations (4.1),(5.1), together with the domain multiplicity-one facts, now determine the selected actual ideal images exactly. This is a finite source-map rank result, not an original D3 rank result.

## 6. Exact actual source table throughout min(r,s)>=3

Write d_r=1 if r=3 and 0 otherwise, and d_s=1 if s=3 and 0 otherwise. For EVERY r,s>=3 the ACTUAL source-lowest dimensions are:

|full source degree|type|dim P5_(a,b)(r,s)|original D3 status|
|---|---|---:|---|
|(2,2,5)|64|19-d_r-d_s|OPEN off the classical diagonal|
|(3,2,5)|35|20-d_r|OPEN off the classical diagonal|
|(2,3,5)|35*|20-d_s|OPEN off the classical diagonal|
|(3,3,5)|27|36|OPEN off the classical diagonal|
|(4,3,5)|10|20|OPEN off the classical diagonal|
|(3,4,5)|10*|20|OPEN off the classical diagonal|
|(4,4,5)|8|29|OPEN off the classical diagonal|
|(5,5,5)|1|6|Injective by the companion six-source determinant|

Proof: subtract the exact selected image multiplicities established in §§3-5 from the free table. Q5 can neither add another selected image nor change their intersection, by isotypic semisimplicity. This proves the ACTUAL table, not just a domain-derived lower bound.

In particular the 64 source is 19-dimensional if both entries are >=4, 18-dimensional if exactly one is 3, and 17-dimensional at (3,3). The other seven sources do not disappear in these cells. Thus there is no source-vanishing shortcut for the residual F5 obligations.

## 7. Exact corresponding target sizes, without confusing highest multiplicity with weight dimension

At r,s>=3 the whole target ideal at level4 is exactly d_r Q4+ + d_s Q4-, a direct sum of different 81 types. Therefore the ACTUAL ordinary target weight dimensions at full degree (a,b,4) are the following free dimensions minus the two displayed corrections:

|source pair (a,b)|free target dim|subtract d_r times|subtract d_s times|
|---|---:|---:|---:|
|(2,2)|25|2|2|
|(3,2)|36|3|2|
|(2,3)|36|2|3|
|(3,3)|65|3|3|
|(4,3)|65|3|3|
|(3,4)|65|3|3|
|(4,4)|84|3|3|
|(5,5)|65|3|3|

The free target character is (chi^4-(psi2 chi)^2)/4. The two corrections are ordinary weight multiplicities in L(5,2) and its dual. They were evaluated exactly from the finite Weyl formula; they are not selected-highest multiplicities. For the invariant source, whole-W equivariance further restricts its image to the unchanged eight-dimensional adjoint-highest multiplicity space; that was crucial to the companion theorem. No corresponding eight-target assertion is transferred to the other seven types.

## 8. The entry-two boundary: honest bounds, not invented actual image ranks

For min(r,s)>=2, entry two contributes Q3+=35 or Q3-=35*. Its source ideal is an image of V tensor V tensor Q3; entry three contributes V tensor Q4 as above. The exact DOMAIN multiplicities for the eight types, in the fixed table order, are:

|relation-domain|64|35|35*|27|10|10*|8|1|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|V^tensor2 tensor Q3+|6|9|2|6|4|1|2|0|
|V^tensor2 tensor Q3-|6|2|9|6|1|4|2|0|
|V tensor Q4+|1|1|0|0|0|0|0|0|
|V tensor Q4-|1|0|1|0|0|0|0|0|

Consequently, if m is the free source row, an explicit safe lower bound is

    dim P_type >= max(0, m_type
       -1_(r=2) A_type -1_(s=2) Adual_type
       -1_(r=3) B_type -1_(s=3) Bdual_type).

Examples with no entry-three term: at r=2,s>=4 the lower bounds are (13,11,18,30,16,19,27,6); at r=s=2 they are (7,9,9,24,15,15,25,6). These are NOT equality claims. The two iterated-bracket maps have Jacobi/overlap kernels, and their intersections with other relation images must be proved before subtracting exact ranks. Invariant multiplicity remains exactly six throughout min(r,s)>=2 because all these relation domains have zero invariant; the companion theorem proves its original lowering injective.

On the row-one axes, the already supported invariant source dimension two and its D3 injectivity remain in force, but this packet does NOT classify the other seven quadratic-ideal source images. At (1,1) all cases are classical. No old level-four dimension or H13 receipt is substituted for an uncomputed level-five source or map.

## 9. Exact remaining work and assurance

This packet has classified actual sources in all cells with min(r,s)>=3 and given explicit relation-domain bounds at the entry-two boundary. The next mathematical gap is NOT another character count: it is original D3 injectivity on these nonzero actual primitive spaces (and exact source/target relation-image control for entries one or two), with the original live parameter restriction ar+bs>=10. A free-space minor cannot certify a relation-affected target without an actual quotient argument.

The arithmetic checks are recorded in `level5-seven-type-source-arithmetic-v1.json`: exact free character coefficients; complete V tensor81 decomposition; exact Casimir-projected coefficient witnesses; the two-by-two determinant; actual target weight multiplicities; and domain multiplicities used only as bounds. These are finite in-kernel arithmetic results at the stated written imports, not formal/kernel verification, independent-vendor/human review, novel-theorem clearance or parent acceptance. General F5, all seven original map verdicts, B4/H13 authentication, outside-band (4,4,6), and the broad book problem remain unproved here. The global scientific-launch HOLD and all parent evidence errata remain binding.
