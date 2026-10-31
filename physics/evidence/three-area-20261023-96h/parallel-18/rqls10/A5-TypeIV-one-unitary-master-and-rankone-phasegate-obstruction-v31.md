# RQLS10 v31 — ENTIRE TypeIV one-unitary/full-resolution master, and no rankONE covariant phase-gate solution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 08:50:09 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite representation/unitary/association-algebra/PSD proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/full-witness acceptance.

This is a new representation of the actual remaining ordinary irreducible10 geometry, not another orientation of the closed4-sector model. It retains a FULL arbitrary allowed resolution and maximal-ray conditions, and records a complete failure of the first natural low-rank construction inside this master.

## 1. Exact TypeIV model and one-unitary iff statement

The physical representation is the natural permutation representation on the ten duads, U(g)e_a=e_(ga), which decomposes as1+4+5 (TypeIV ofv29). By unitary equivalence this is the ENTIRE ordinary TypeIV case, not a coordinate ansatz within that irreducible decomposition. Simultaneous A5 row/column covariance is still an explicit hypothesis, NOT WLOG for the original problem. No covariance of the third resolution is imposed.

Fix a reference duad a0, with stabilizer H=S3. Its ten column-duad orbits have sizes1(diagonal),3(disjoint),6(intersecting). Let

    V0 be ANY unitary in Comm(U(H)),
    V_a=U(g_a) V0 U(g_a)^dagger,
    q_(a,b)=V_a e_b,                              (MASTER)

where g_a is ANY even permutation taking a0 to a. Since V0 commutes with H, V_a is independent of this choice. Each row is automatically an ONB and the entire array is exactly vector-equivariant under simultaneous A5.

The S3 restriction of the physical permutation representation is

    trivial multiplicity3,
    sign multiplicity1,
    standard2 multiplicity3.

Consequently the COMPLETE parameter unitary is one element of

    U(3) directsum U(1) directsum (I2 tensor U(3)),

in the corresponding isotypic decomposition. This has19 real parameters before its irrelevant common phase, not a collection of one hundred unconstrained vector guesses.

The exact remaining conditions are:

**COLUMN** for EVERY b and EVERY a!=c,

    e_b^dagger V_a^dagger V_c e_b=0.

**RESOLUTION** choose ANY Latin square L on the SAME ten-by-ten cell labels with ten symbols. For EVERY two distinct cells(a,b),(c,d) with L(a,b)=L(c,d), require

    e_b^dagger V_a^dagger V_c e_d=0.

The ten cells of each L-symbol are then a genuine row-and-column transversal ONB; L is not presumed cyclic, covariant or a selected group table.

**MAXIMALITY** for EVERY two distinct cells(a,b),(c,d), require

    |e_b^dagger V_a^dagger V_c e_d|<1.

Since all vectors have norm1, this is EXACTLY distinctness of the one hundred complex projective rays, not an ansatz or a weaker nonzero determinant. These three literal conditions together with MASTER are an iff master for TypeIV maximal1-RQLS10.

## 2. Why this covers EVERY projectively equivariant TypeIV array

The ordinary full-array trace theoremv29 forces BOTH diagonal and disjoint-cell stabilizer characters to be+1 in TypeIV. For the reference row, the diagonal ray is H-fixed and each disjoint-column ray has trivial character on its order2 point stabilizer. Thus their phases can be chosen so H acts EXACTLY by permutation on those1+3 row vectors. On the remaining six columns H acts FREELY; choose one representative vector and transport it by H, giving an unambiguous exact vector-permutation action there as well. There is no hidden point-stabilizer phase left on a free orbit.

The matrix V0 whose ten columns are these reference-row ONB vectors is unitary and intertwines the reference physical U(H) with its ten-column permutation action, which are the SAME representation. Hence V0 commutes with U(H). Covariance transports this row to every other row; the above phase choices yield exactly MASTER at the ray level. This proves NECESSITY, not just one convenient construction.

Conversely, any V0 in that commutant gives the stated row ONBs/covariance. COLUMN then makes all columns ONBs; RESOLUTION supplies the full literal third context partition; MAXIMALITY supplies all hundred distinct rays. This proves SUFFICIENCY with no executable or inferred Latin completion. No actual V0,L satisfying all three conditions is supplied here.

## 3. ENTIRE rankONE covariant phase-gate family

A natural first construction is to let the seed differ from a scalar only on ONE invariant ray:

    V0=I+(u-1)|v><v|,   |u|=1, ||v||=1,
    [|v><v|,U(H)]=0.                              (PHASE1)

Global scalar multiples are irrelevant. This is the entire rank(V0-lambda I)<=1 family of unitary seeds for some unit lambda, including the scalar case. Covariance gives

    v_a=U(g_a)v,
    V_a=I+(u-1)|v_a><v_a|,
    q_(a,b)=e_b+(u-1)v_a (v_a)_b^*.

The rank-one projector commutes with H iff its line carries a one-dimensional H character: trivial or sign. We handle BOTH, not merely H-fixed vectors.

### 3.1 Sign line: four immediate repeated column rays

The sign subspace of the ten-duad permutation representation is one-dimensional and lies entirely on the six-element intersecting-duad orbit. It has zero coordinates at the fixed diagonal and at the three disjoint columns, since those point stabilizers contain an odd S3 element acting as-1 on that line. Thus for EACH fixed column b, v_a has zero b-coordinate for row a=b and for the three rows disjoint from b. All FOUR corresponding q_(a,b) equal e_b. The column cannot be an ONB, irrespective of u. This excludes the entire sign-line branch.

### 3.2 Trivial line: exact three-entry orbit form

An H-fixed vector has entries A0 at the reference duad, B0 at its three disjoint duads, C0 at its six intersecting duads. Therefore its orbit vectors satisfy

    (v_a)_b=A0 if a=b,
             B0 if a,b disjoint,
             C0 if a,b intersect but differ,
    |A0|^2+3|B0|^2+6|C0|^2=1.

Put C=|C0|^2. If C=0, the six intersecting rows in a fixed column all give q_(a,b)=e_b, so a column ONB is impossible. If u=1, every row seed is scalar identity and columns repeat as well. Hence any hypothetical solution in this branch has C>0 and s=|u-1|^2>0, with s<=4.

Let P be the Petersen adjacency matrix on the duads (disjointness), J the all-ones matrix. The matrix with orbit vectors v_a as its columns is

    N=A0 I+B0 P+C0(J-I-P).

It lies in the real symmetric three-class association algebra. Explicitly P^2=2I-P+J and PJ=JP=3J: adjacent(disjoint) duads have no common neighbor, distinct intersecting duads have exactlyONE. Thus this algebra is commutative and closed under conjugate transpose. Its Gram N^dagger N has diagonal1 and REAL constants g_dis,g_int on the two offdiagonal relations. Their being real follows from Hermiticity in the linearly independent REAL symmetric basis I,P,J; no real-phase restriction on A0,B0,C0 was assumed.

## 4. Column orthogonality gives a sharp contradiction for the ENTIRE trivial-line phase family

Fix column b. For any two row duads a,c intersecting b, their b-coordinates in v_a,v_c are BOTH C0. Direct inner product expansion of the two PHASE1 column vectors gives

    <q_(a,b),q_(c,b)>
       =1+(u-1)C+(conj(u)-1)C+s C <v_a,v_c>
       =1-s C+s C g_relation,

because (u-1)+(conj(u)-1)=-s. The set of six row duads intersecting b contains BOTH relation types: for b={1,2}, choose {1,3},{2,4} for disjoint rows and {1,3},{1,4} for intersecting rows. Thus COLUMN orthogonality forces

    g_dis=g_int=g=1-1/(s C).

The full ten-vector Gram is now

    N^dagger N=(1-g)I+gJ.

Positive semidefiniteness gives1+9g>=0, i.e. g>=-1/9. Therefore

    s C>=9/10.

But normalization gives C<=1/6 and |u-1|^2<=4, so

    s C<=2/3<9/10,

an exact contradiction(20<27). Every zero/degenerate case was handled above. This excludes ALL choices of three complex amplitudes and ALL unit phases u, not just reflections or a particular equal-amplitude vector.

Together with the sign-line branch, NO rankONE commuting phase-gate seed PHASE1 produces even a QLS10 in TypeIV. Any actual TypeIV solution must satisfy

    rank(V0-lambda I)>=2 for EVERY unit scalar lambda.

This is a necessary mixing-rank condition inside the COMPLETE one-unitary master, not an arbitrary sparsity no-go or a statement about all group-covariant arrays.

## 5. Exact remaining geometry and scope

The original dense TypeIV task is now concrete: solve the full U(3)/U(1)/U(3) commutant-unitary COLUMN equations, an ACTUAL allowed Latin resolution L and the hundred-ray MAXIMALITY inequalities. RankONE scalar perturbations are closed; rankTWO or genuinely multiblock seeds remain open. The original degree-of-freedom count does not itself prove existence/nonexistence. No additional validation, execution or current-priority claim is inferred.

The entire master/application proof and BOTH rank-one character branches require a full gate; an isolated PSD bound or checking only a real reflection does not accept this theorem. Named inputs are the complete v29 ordinary TypeIV trace/stabilizer fact and the literal S3 permutation decomposition, elementary finite-group phase transport, exact unitary rank-one update algebra, and the printed Petersen association identity. No Pauli/600-cell/graph-classifier output is an operative premise.

Mixed TypeI and TypeII/III also remain open inside the A5 model. Outside A5 covariance the original intrinsic10/4+6/5+5 branches remain OPEN. No A5-WLOG,100-ray witness, unrestrictedno-go or formal/kernel/family/human/novelty/current-openness/finitewitness-gate promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines remain. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early pending-review park.
