# Written multiplicity barriers for the genuinely surviving four cells

Observed immediately before creation: **2026-10-23T14:31:51-07:00**. Written research under the parent's explicit assay HOLD. No syntax compilation, import, enumeration or mathematical executable has been run. The frozen proposed source remains unchanged; this note does not authorize or claim a control replay.

## 1. What this proves, and what it does not

The absence/detection of the invariant line does NOT imply that the other four primitive spaces vanish under small-row Serre relations. Here are exact representation-theoretic lower bounds for their surviving multiplicities, useful as nonvacuity/rejection controls for any future actual-quotient reconstruction.

At the four residual degrees in order

    (2,2,4), (3,2,4), (2,3,4), (3,3,4),

the lowest Levi weights correspond to simple types

    N = (L(2,2), L(3,0), L(0,3), V).

Write n_N for their FREE multiplicities in L4(V). The bounds below are stated in terms of n_N and do NOT depend on trusting an old finite-rank computation. The historical values(7,6,6,8) are merely a clearly labelled specialization if their independent source is imported; a new admitted reconstruction should obtain its own n_N.

## 2. One row2 leaves at most one removed copy in each of only two types

For r=2,s>=3, Q2=0 and T4=[V,L(4,1)]+Q4. Any Q4 summand has type81 and no matching lowest line in these four degrees. The exact elementary tensor rule gives

    V⊗L(4,1) = L(5,2)⊕L(6,0)⊕L(3,3)
               ⊕2L(4,1)⊕L(2,2)⊕L(3,0).

Thus the multiplicities removed from the four types by the actual bracket IMAGE are bounded ABOVE by(1,1,0,0). Complete reducibility gives the exact inequalities

    dim P_actual >= (n_27-1, n_10-1, n_10*, n_8).    (2.1)

I do NOT infer equality of the image with the tensor product from these characters; a possible bracket kernel only strengthens the lower bounds. For s=2,r>=3 exchange10 and10*. When r=s=2, the corresponding upper bounds add, giving

    dim P_actual >= (n_27-2, n_10-1, n_10*-1, n_8).  (2.2)

For the historical free multiplicities, these become(6,5,6,8) in(2.1) and(5,5,5,8) in(2.2). They show that row2 does not eliminate the remaining four-cell problem. In particular the entire free adjoint multiplicity survives, as proved more strongly in quotient-bridge-addendum-v1.md.

## 3. One row1: a forced55-dimensional syzygy, not generic rank

Take r=1,s>=4, so the only low relation module is R=M1=L(3,0)⊆L2(V), of dimension10. The exact source ideal is

    T4=[V,[V,R]].

Let f:V⊗V⊗R→L4(V) be the bracket map

    f(v⊗w⊗z)=[v,[w,z]].

Its image is exactly T4. The tensor inclusion R⊗R→V⊗V⊗R obtained by expanding the FIRST R as its degree-two tensor is injective. For r0,s0∈R, Jacobi gives

    f(r0⊗s0)=[r0,s0],

where the first tensor factor r0 is understood through that inclusion. Therefore the whole Sym2R is in ker f:

    f(r0⊗s0+s0⊗r0)=[r0,s0]+[s0,r0]=0.

This is an actual55-dimensional Levi-stable kernel, not a parameter heuristic. Consequently T4 is a quotient of

    (V⊗V⊗R)/Sym2R.                               (3.1)

The other kernel constituents, if any, are NOT assumed absent. In particular neither a dimension subtraction suggesting equality nor a generic-rank assumption is used.

## 4. Explicit multiplicity arithmetic in(3.1)

Use the previously derived

    V⊗V=1⊕2V⊕10⊕10*⊕27.

The multiplicities of(27,10,10*,8) in V⊗V⊗R are(5,4,2,4). Here is the complete small calculation, exposing the finite representation imports:

| First factor in V⊗V | Multiplicities after tensoring R=10, in order(27,10,10*,8) |
|---|---|
|1|(0,1,0,0)|
|2V|(2,2,0,2)|
|10|(1,0,1,0)|
|10*|(1,0,0,1)|
|27|(1,1,1,1)|
|Total|(5,4,2,4)|

The rows use V⊗10=35⊕27⊕10⊕8,

    10⊗10=L(6,0)⊕L(4,1)⊕L(2,2)⊕L(0,3),
    10*⊗10=1⊕8⊕27⊕L(3,3),

and elementary Pieri for27⊗10. To verify the four entries of that last row explicitly, identify27 with the GL3 partition(4,2,0) and10 with Sym3(C3). The target SU3 types27,10,10*,8 correspond at total partition size9 to

    (5,3,1), (5,2,2), (4,4,1), (4,3,2).

Each contains(4,2,0) with a horizontal3-strip, hence occurs exactly once by Pieri. There is no multiplicity ambiguity or numerical fit.

Finally,

    Sym2(10)=L(6,0)⊕L(2,2),

of dimensions28+27=55. This follows from the same10⊗10 decomposition: the factors with even Pieri index belong to the symmetric square, while the others belong to the alternating square. The55-dimensional known kernel in §3 therefore removes one27 and none of the other three listed types from the tensor-domain bound. Hence the multiplicities of T4 in those four types are bounded ABOVE by

    (4,4,2,4).

The actual quotient primitive spaces must consequently satisfy

    dim P_actual >= (n_27-4, n_10-4, n_10*-2, n_8-4) (4.1)

when r=1,s>=4. With the clearly conditional historical values this is(3,2,4,4). For s=1,r>=4 it is(3,4,2,4), by duality. Thus a proposed small-row argument claiming that a single quadratic relation kills ALL nontrivial lowest spaces is mathematically impossible. The surviving couplings must actually be detected.

## 5. Classical diagonal positive boundary and exact scope

At r=s=1 the actual affine A2 Serre quotient is the classical loop algebra with its full central/degree realization retained; every positive fixed level is adjoint V as a Levi module. Thus at level4 the three27/10/10* primitive cells vanish and the adjoint primitive cell is one-dimensional and detected. At r=s=2 or3, classical symmetrizable Gabber–Kac guarantees injectivity after the ACTUAL appropriate quotient, not necessarily a preselected free-space minor. These are classical positive boundaries, not this round's discoveries or substitutes for the off-diagonal proof.

Equations(2.1),(2.2),(4.1) are genuine written rejection controls for future certificates. They do not by themselves prove D3 injectivity. The missing ingredient remains original-row coupling on these nonzero multiplicity spaces, with correct source AND target ideals. Any future executable calculation of those maps is still separately gated by exact parent GO.
