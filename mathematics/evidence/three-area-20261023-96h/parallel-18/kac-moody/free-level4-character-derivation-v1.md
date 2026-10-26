# A short written derivation of all five relevant free level-four multiplicities

Observed immediately before creation: **2026-10-23T14:34:42-07:00**. Written reasoning only, during explicit scientific-assay HOLD and an assigned Sun-review hash clarification. No mathematical execution, import, smoke check or syntax compilation occurred.

## 1. Result and exact significance

For V=ad(sl3), the multiplicities in L4(V) of

    (1, L(2,2), L(3,0), L(0,3), V)

are EXACTLY

    (1,7,6,6,8).

This derivation requires no historical tensor-rank/checker output. It supplies a second written proof of the unique invariant multiplicity and independently derives the free primitive dimensions relevant to the all-r,s band. It does NOT detect the actual omitted lowering, prove its injectivity, or solve the remaining actual small-row quotient couplings. Classical PBW/Witt, Pieri and finite-Levi complete reducibility remain explicit imports; no novelty is claimed for these representation identities.

## 2. The simplifying character identity

For any characteristic-zero finite-dimensional representation V with character χ,

    χ_Sym2V=(χ²+ψ2χ)/2,
    χ_Λ2V=(χ²-ψ2χ)/2.

The degree-four Witt character is

    χ_L4V=(χ⁴-(ψ2χ)²)/4.

Therefore

    χ_L4V = χ_(Sym2V tensor Λ2V).                   (2.1)

Both sides are finite-dimensional semisimple sl3 representations. Their equal characters imply an isomorphism AS LEVI MODULES,

    L4(V) ≅ Sym2(V) tensor Λ2(V).                   (2.2)

There is no assertion that a chosen symmetric-times-alternating bracket is a canonical isomorphism of Lie algebras, nor that the original-row lowering is transported by(2.2). The identity is used only to compute multiplicities. It also gives dimension36*28=1008 immediately.

## 3. The complete small tensor calculation

The written decompositions already justified in the invariant candidate are

    Sym2 V = 1 ⊕ V ⊕ 27,
    Λ2 V   = V ⊕ 10 ⊕ 10*,

where27=L(2,2),10=L(3,0),10*=L(0,3). Distribute their tensor product. The required multiplicities are listed in the table; ALL nine tensor factors are accounted for (the first three are combined into one row).

| Product contribution | Multiplicities in order(1,27,10,10*,V) |
|---|---|
|1 tensor(V⊕10⊕10*)|(0,0,1,1,1)|
|V tensor V|(1,1,1,1,2)|
|V tensor10|(0,1,1,0,1)|
|V tensor10*|(0,1,0,1,1)|
|27 tensor V|(0,2,1,1,1)|
|27 tensor10|(0,1,1,1,1)|
|27 tensor10*|(0,1,1,1,1)|
|TOTAL|(1,7,6,6,8)|

The first three nontrivial factors use

    V tensor V = 1 ⊕ 2V ⊕10⊕10*⊕27,
    V tensor10 = L(4,1)⊕27⊕10⊕V,
    V tensor10* = L(1,4)⊕27⊕10*⊕V.

For27 tensor V, apply the elementary adjoint tensor rule, obtained by tensoring with3 then3* and subtracting the original module:

    27 tensor V = L(3,3)⊕L(4,1)⊕L(1,4)
                  ⊕2L(2,2)⊕L(3,0)⊕L(0,3)⊕V.

Its dimensions64+35+35+54+10+10+8=216=27*8 verify exhaustion once the Pieri summands are obtained. For27 tensor10, identify27 with GL3 partition(4,2,0) and use multiplication by Sym3(C3). The four target types27,10,10*,V correspond at total size9 respectively to

    (5,3,1), (5,2,2), (4,4,1), (4,3,2).

Each differs from(4,2,0) by a horizontal3-strip, so each occurs once by Pieri. No trivial summand occurs since27 is not10*. Duality gives the final table row. The invariant contribution occurs ONLY in V tensor V, and there once. Thus the table proves every stated multiplicity, not just a numerical dimension check.

## 4. Translation to full-degree primitive counts

At level4 the Levi weight of full degree(a,b,4) is

    (2a-b-4,-a+2b-4).

The lowest weights of27,10,10*,V are(-2,-2),(0,-3),(-3,0),(-1,-1), respectively. Solving the two linear weight equations yields exactly

    (a,b)=(2,2),(3,2),(2,3),(3,3).

In each irreducible finite-Levi module the simultaneous F1,F2 kernel is its unique lowest line. Consequently the FREE primitive dimensions in those four full degrees are7,6,6,8. The invariant lowest line is at(4,4,4). This distinguishes lowest-vector multiplicities from ordinary zero-weight dimensions.

The numerical lower bounds in primitive-multiplicity-controls-v1.md are therefore no longer conditional on importing the historical free-rank counts: substituting this written character theorem gives exact lower bounds(6,5,6,8) for one row2/other>=3, (5,5,5,8) for both rows2, and(3,2,4,4) for row1/other>=4, with dual exchange in the opposite orientation. These remain LOWER bounds, not unproved equalities of relation-image ranks.

The actual quotient map still has to be analyzed. The proposed one-shot assay remains NOT ADMITTED and unexecuted; this representation-character identity supplies no permission to run it and no all-parameter rank conclusion.
