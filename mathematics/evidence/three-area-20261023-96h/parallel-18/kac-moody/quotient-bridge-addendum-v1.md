# Addendum v1 — exact level-three targets and which level-four cells really change

Observed immediately before creation: **2026-10-23T14:11:01-07:00**. New immutable research snapshot. This extends, not edits, invariant-bridge-v1.md (SHA25626485dba4591ca16c8d5dfa66b5793bae5f28635c54be2938e7f50ab6f343a2c). Status remains author-written CANDIDATE/PARTIAL; no execution or independent acceptance is claimed.

## 1. A syzygy-free pair of level-three submodules

Retain g=sl3, V=ad(g), Λ2V=M0⊕M1⊕M2 with M0=V, M1=L(3,0), M2=L(0,3). The free degree-three exact sequence and j,b are as in the main candidate. In fact

    b: V⊗(M1⊕M2) → L3(V)

is injective, not merely injective on its two adjoint copies.

Here is a complete finite-Levi proof. The exterior cube has decomposition

    Λ3V = 1 ⊕ V ⊕ L(3,0) ⊕ L(0,3) ⊕ L(2,2).       (1.1)

To prove this without a tensor-product table, construct the following nonzero simple submodules:

- The invariant Cartan3-form tr(x[y,z]), transferred by the trace form, gives1.
- The explicitly computed lowest vector Z in main-candidate(5.1) gives V.
- The vector E13∧E12∧E23 is highest of weight(2,2), giving dimension27.
- The vector Y=E13∧E12∧(2H1+H2) is highest of weight(3,0), giving dimension10. Both raisings kill it: the E1 term repeats E12, while E2(2H1+H2)=0 and its other nonzero term repeats E13.
- The Dynkin-diagram automorphism gives its dual10.

These five types are distinct. Complete reducibility makes their sum direct, and1+8+10+10+27=56=dimΛ3V proves exhaustion.

Let δ0=(id⊗[-,-]_matrix)j, whose second factor detects projection onto M0. This map is nonzero on EVERY simple summand of(1.1):

- On1, j is injective and the only invariant in V⊗Λ2V lies in V⊗M0, so the projection cannot vanish.
- On V, the explicit nonzero expression is main-candidate(5.2).
- On the27 highest vector, δ0(E13∧E12∧E23)=E13⊗E13, nonzero.
- On Y, direct commutators give

      δ0Y = -3 E13⊗E12 +3 E12⊗E13 !=0.

- The dual10 is nonzero by the same automorphism.

Since each summand is simple, δ0 is injective on each; the distinct images have distinct simple types and hence direct sum. Therefore δ0 is injective on Λ3V. It follows that j(Λ3V) has zero intersection with V⊗(M1⊕M2). Exactness of the degree-three sequence proves the asserted bracket injection.

Set A_i=[V,Mi]. Then

    A1 ≅ V⊗M1 = L(4,1)⊕L(2,2)⊕L(3,0)⊕V,
    A2 ≅ V⊗M2 = L(1,4)⊕L(2,2)⊕L(0,3)⊕V,           (1.2)

and A1∩A2=0. These tensor products follow from the elementary sl3 adjoint tensor rule (or its six Weyl-character terms); their dimensions are35+27+10+8=80. The kernel j(Λ3V) projects isomorphically onto V⊗M0 minus one adjoint copy: V⊗M0 has decomposition1⊕2V⊕M1⊕M2⊕27, while(1.1) removes one of each displayed type. Consequently

    L3(V) ≅ V ⊕ A1 ⊕ A2,                          (1.3)

as a finite-Levi module. This is an isomorphism of modules, not a chosen canonical splitting.

## 2. Actual S3 for every small-row regime

The quadratic relation for r=1 kills M1, hence its degree-three ideal is A1; similarly s=1 kills A2. The cubic relation for r=2 generates the unique35 in A1, because its lowest vector is[v,[v,E1v]]=[v,t1]. Likewise s=2 kills the35* in A2. These are distinct simple constituents; the two row conditions cannot conflict within the same row.

Define

    B1(r) = 0                                  if r=1,
            V⊕L(3,0)⊕L(2,2)                   if r=2,
            V⊕L(3,0)⊕L(2,2)⊕L(4,1)           if r>=3,

and B2(s) by exchanging the two highest-weight coordinates. Then the EXACT actual quotient is

    S3(r,s) ≅ V ⊕ B1(r) ⊕ B2(s).                 (2.1)

No third-leading relation of higher level can affect it. Thus its dimensions, derived from the written decompositions rather than computed ranks, are

| Row categories, up to exchange | dim S3 |
|---|---:|
|1,1|8|
|1,2|53|
|1,>=3|88|
|2,2|98|
|2,>=3|133|
|>=3,>=3|168|

These presentation dimensions are NOT a new discovery of alpha3<=3 equality; that equality is the historical baseline. They identify precisely the target one must use in the unsolved level-four couplings.

## 3. Entry3 does not alter any residual interior primitive space

When r,s>=3, Q2=Q3=0. Hence T3=0 and T4=Q4. Each summand of Q4 is simple of dimension81, with lowest full degree(1,0,4) or(0,1,4). Its simultaneous F1,F2-kernel is exactly its displayed lowest line. Therefore its intersection with the free primitive space in each of

    (2,2,4), (3,2,4), (2,3,4), (3,3,4), (4,4,4)

is zero. By the exact lifting formula main-candidate(2.3), all these quotient primitive spaces are canonically represented by the unchanged free primitive spaces, and the target is the unchanged L3(V).

Thus the missing regimes r=3,s>=3 or s=3,r>=3 DO NOT require a new quotient-matrix construction at those five degrees. They require a valid nonvanishing proof for the same free affine maps at the new boundary. The old minor positivity only at r=4+x,s=4+y does not supply this boundary proof automatically. This is a precise reduction, not a claim that its missing nonvanishing has now been checked.

## 4. The adjoint primitive cell is unchanged already for r,s>=2

Suppose r,s>=2. Then Q2=0. T3=Q3 is a sum of L(4,1),L(1,4), while T4=[V,Q3]+Q4.

There is NO adjoint constituent in T4. For Q4 this follows from its81-dimensional simple types. For[V,Q3] it follows from

    Hom_g(V,V⊗L(4,1)) ≅ Hom_g(V⊗V,L(4,1))=0,

and the dual case, using main-candidate(3.1). So the adjoint-isotypic part of S4 is unchanged from free L4(V), including its lowest multiplicity space at(3,3,4).

Moreover the full W-action of this adjoint-isotypic part cannot have an image in T3: W⊗V≅V⊗V has types1,V,M1,M2,27, none of type35 or35*. Consequently the image of its free original-row D is disjoint from T3. Hence

> For r,s>=2, injectivity at the adjoint primitive cell(3,3,4) in the ACTUAL quotient is equivalent to injectivity of the unchanged free-space original-row map at those parameters.

This is an equivalence of the required quotient question, not generic rank or finite-field reasoning. It supplies no unproved nonvanishing.

## 5. Which one-row2 cells still require a quotient

For r=2,s>=3, Q3=L(4,1). The elementary adjoint tensor decomposition is

    V⊗L(4,1) = L(5,2)⊕L(6,0)⊕L(3,3)
               ⊕2L(4,1)⊕L(2,2)⊕L(3,0).          (5.1)

The dimensions81+28+64+70+27+10=280 check the complete tensor-product dimension8*35; the types are obtained by adding adjoint weights with the standard boundary cancellations. In particular neither V nor L(0,3) occurs. Q4, if s=3, still has no matching lowest primitive in the four residual cells.

Therefore for r=2,s>=3 the primitive cells(3,3,4) [adjoint] and(2,3,4) [L(0,3)] have unchanged source multiplicity spaces. Their W-images have no L(4,1) constituent: the first uses V⊗V; the second uses V⊗L(0,3)=L(1,4)⊕27⊕L(0,3)⊕V. So their target quotient cannot erase a nonzero D-image. Only the cells(2,2,4) [27] and(3,2,4) [L(3,0)] can require a genuine quotient adjustment in this one-row2 regime. The exchanged statement holds for s=2,r>=3.

This reduces, but does not settle, the remaining all-parameter proof. In regimes with a row1 the quadratic descendants in T4 MUST still be included explicitly. No free-rank computation is substituted for them. No checker or Lean execution has been admitted or run.
