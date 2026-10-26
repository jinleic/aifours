# Off-axis first profile: all96 positive two-edge-matching second cores v1

PhysicsRQLS10, same primary. Author-written CANDIDATE; no scientific program, arithmetic interpreter, enumeration, solver or CLI ran. Last actual working observation before this artifact:2026-10-24T05:08:40-07:00, not an exact creation timestamp.

## 1. Exact family and the actual new first block

First rho=(0,7,8,6,5,4,3,1,2), with H={4,5},J={3,6},U={1,7},V={2,8}, first D0=I and A0_JU=A0_JV=1,A0_UV=2. Its mixed block has rank3; none of it is replaced by the old axial rank1 data.

Take every genuine second core whose four pairs are rook-positive and whose odd off-diagonal graph A1 is a matching of two magnitude1 edges. This is the positive all-rook two-horizontal/two-vertical class. There are two raw source matchings and96 distinct literal tables. For example source horizontal pairs occupy rows1,2, each using column0 and one different nonzero column; the vertical pairs use the remaining two points in columns1,2. Source reflections/interchange exhaust the two raw cases. Every table is a literal PC P^T, with all independent complex D/E still unrestricted.

Every second pair tag is+1. Two second vertices joined by a unit A1 edge are parallel rook pairs with different omitted coordinate levels. Their even cross-entry is always-1: the two pair means in the varying coordinate overlap at one of their two points, giving raw cross sum-2 and pair-coordinate entry-1. Endpoint orientation changes the A1 sign but not this mean.

## 2. Complete first-order disposition

Let k be H's neighbour in the second matching and{i,j} the other two first vertical vertices. If k=J, then the opposite second edge U-V has magnitude1 and cannot cancel the first heavy2; all three B-triangle entries in L=A0+A1 remain nonzero. Hence leading rank>=3.

If k=U orV, let l be the other heavy first leaf, so the opposite second edge is J-l. If its sign is+1, that first light edge becomes2 and again the B triangle remains. Only

    A1_Jl=-1, A1_Hk=p, p=±1

can have leading rank2. L is exactly a star centred at k with leaf weights p on H,1 on J and2 on l. Its leading radical contains

    y=2e_J-e_l.

No physical phase or second mixed coordinate is chosen in this reduction.

## 3. Exact second Schur scalar for every critical input

The vector y has norm-square5. With the ACTUAL first O0=-I+A0,

    O0*y has J,l coordinates-3,+3 and k coordinate0,
    |O0*y|²=18.

For the positive second O1=-I+A1, its two active coordinates are-1,-1, so

    |O1*y|²=2.

Equivalently, on a leading radical with both D0=D1=I, O1*y=-O0*y-2y and the norm difference is4*y^T A0*y=-16. The regularity/even-inverse identity therefore gives the mixed Schur feedback

    [|O1*y|²-|O0*y|²]/128=-16/128=-1/8 (mod s).

It is essential that both actual mixed blocks are retained to obtain this difference; setting B0 or B1 to a flat surrogate would not justify it.

The direct y-y curvature has only the J-l off-diagonal contribution. First E0_Jl=-1, first O0_Jl=1, second O1_Jl=-1, and the genuine second pair mean E1_Jl=-1 from section1. Thus the direct off-diagonal numerator is

    E0_Jl*O1_Jl-O0_Jl*E1_Jl=2.

Its quadratic contribution on(2,-1) is2*2*(-1)*2/16=-1/2. Diagonal products cancel because both leaf tags are+1. Direct mixed skew terms vanish in any scalar quadratic. The total actual second Schur scalar is consequently

    -1/2-1/8=-5/8≠0 (mod7).

An additional odd pivot survives after the even5 and leading odd2 pivots. Therefore actual rank M>=8 for every critical case, and the general common-norm argument excludes every arbitrary complex coordinate-unit vector.

## 4. Count and exact scope

The three possible second matching supports give32 literal tables each. H-neighbour J contributes32 first-order closures. For H-neighbour U,V, the positive opposite-edge sign contributes16+16 first-order closures, while the negative sign contributes16+16 cases closed by the scalar above. Thus all96 are covered, disjointly64 at first order and32 at second order.

This is a written group/endpoint count, not an executed96-input experiment. It closes a whole positive-signature family for the genuinely different off-axis first rho. It does NOT claim the negative all-nonrook matching family closes: there D1=-I and the same scalar calculation cancels rather than giving-5/8. Those cases remain in the actual-rank7 remainder unless separately resolved.

The all5040-second-core off-axis orientation and unrestricted maximal1-RQLS10 remain UNKNOWN. No second-core count is a new primary problem or a global100-ray construction, and all claims here await their own actual reconstruction.
