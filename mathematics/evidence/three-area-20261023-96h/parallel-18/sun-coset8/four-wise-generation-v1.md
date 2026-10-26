# Four-wise generation: written closure of the finite R4 image v1

Observed before creation: `2026-10-23T14:29:59-0700` (`/bin/date`). **CANDIDATE, written only; not unrestricted Sun8, not formal or novelty acceptance.** This manuscript consumes the complete R4/finite-image reduction in `four-overgroup-residual-v1.md`, SHA256 `d588fe306856763d5a48ae71d4504a10c3430124c3c258c823944fb448057eee`, and closes its exact residual. It does not claim a previous peer review covers that additional source or this manuscript.

## 1. Exact statement and input boundary

**Theorem G4 (relative to the explicit earlier interfaces).** No P7 configuration has an index-seven subgroup containing four of its subgroup vertices. Consequently every FOUR of U_1,...,U_8 generate G, and the same is true after inversion U_i↦g_iU_i g_i^{-1}.

P7 retains arbitrary pairwise-coprime positive cofactors in n_i=7r_i. The preceding R4 manuscript proves that an index-seven overgroup W containing four vertices would produce an actual finite quotient Q with:

- Q≤S7 faithfully and transitively, |Q| dividing1008;
- H=W/core(W), a point stabilizer of index7;
- four distinct disjoint H-cosets, six disjoint cosets of index7 in total, and two further disjoint cosets of indices7·2^a and7·3^b, a,b positive;
- the other two index-seven subgroups K,L each have an orbit of size3 on Q/H;
- the complement T of the four occupied point-image values is a three-element set. The two K/L-cosets have that same T as their point-image set, and every remaining coset is contained in the complement of the six index-seven cosets.

The earlier manuscript's exact added imports remain: internal all-group Sun5, Zhu Sun3/4, Margolis–Schnabel Prop4.5 and TheoremB at length≤4. They are not re-proved here. The elementary finite permutation/group geometry below is written out; no classification database or executable check is used.

## 2. Seven triples and transitive block stabilizers force a Fano plane

We first prove the small incidence lemma needed to analyze Q without classifying transitive degree-seven groups.

**Lemma F.** Suppose a group Q acts transitively on seven points Ω and on a collection B of seven DISTINCT three-element subsets (blocks). Suppose each block's set stabilizer acts transitively on its three points. Then B is a2-(7,3,1) design (a Fano plane).

**Proof.** Double counting incidences shows every point lies in exactly3 blocks: there are7·3=21 incidences and Q is point-transitive. Pick a block B0. Its stabilizer acts transitively on three points, so some stabilizer element induces a3-cycle there. As a permutation of the other four points its order has3-part at most3 and2-part at most4. Raising to the appropriate2-power gives an element σ of order3 which still induces a3-cycle on B0. It has either one3-cycle (B0) and four fixed points, or two3-cycles (B0 and a disjoint triple C) and a fixed point g.

### 2.1 One3-cycle and four fixed points

Write F=Ω\B0, |F|=4. A σ-invariant three-subset is B0 itself or one of the four triples contained in F. The number of fixed blocks is congruent to7 modulo3, so is1 or4.

If it is1, only B0 is fixed; the other six blocks form two orbits of size3. Membership of a fixed point f∈F is constant on either orbit. Because f lies in exactly3 blocks, it belongs to exactly one of these two block orbits. Thus the F-parts of the two orbits partition F. Every nonfixed block has at least one B0-point and at most two F-points; the two F-parts must therefore each have size2. The blocks are B0 and the three translates of a single B0-point joined to one fixed pair, together with the three translates joined to the other fixed pair. A point of B0 then has co-degree1 with each of the other six points. A fixed point f has co-degree3 with its fixed-pair partner, co-degree1 with each B0-point, and co-degree0 with the other two fixed points. These different co-degree profiles contradict point transitivity.

If there are4 fixed blocks, they are B0 and three of the four triples of F. One F-point lies in all three of these F-triples, and the other three F-points each lie in exactly two. The three remaining blocks form one σ-orbit. A fixed point belongs to either all three or none of that orbit; a point already lying in two fixed blocks cannot obtain exactly one further incidence. Contradiction.

Thus σ cannot have just one3-cycle.

### 2.2 Two3-cycles and one fixed point

Now σ has cycles B0,C and fixed point g. Its only invariant triples are B0 and C, and the fixed-block count is1 modulo3. Therefore only B0 is fixed; the other six blocks form two3-orbits. Since g lies in exactly3 blocks and not B0, exactly one orbit consists of blocks through g.

Let a∈{0,1,2} be the number of B0-points in a block through g, and b the number in a block of the other orbit. The two cycles imply uniform incidence within B0 and C. Each B0-point lies once in B0 and a+b times in the other two orbits, hence a+b=2.

- a=2,b=0 is impossible: the second orbit would have to consist of the single subset C rather than three distinct blocks.
- a=0,b=2 gives g co-degree2 with each C-point and0 with each B0-point. A B0-point has co-degree2 with the other two B0-points (one occurrence from B0 and one from the orbit of all three B0-pairs), co-degree1 with two distinct C-points and0 with g and the third C-point. The profiles {2,2,2,0,0,0} and {2,2,1,1,0,0} differ, contradicting point transitivity.
- Therefore a=b=1. The three blocks through g each contain one B0-point and one C-point, permuted cyclically. Thus g has co-degree1 with every other point. By point transitivity every point has co-degree1 with every other point.

This is exactly the required design property. QED.

## 3. Applying Lemma F to the actual index-seven subgroup K

Let Ω=Q/H. The subgroup K has index7 and an orbit B0 of size3. Its set stabilizer S=Stab_Q(B0) contains K, so [Q:S] divides7. The index cannot be1 because a transitive group cannot preserve a proper three-element subset of Ω. Thus [Q:S]=7, S=K, and the orbit of B0 consists of exactly seven blocks. Their stabilizers are conjugates of K and act transitively on the corresponding triples. LemmaF applies and yields a Q-invariant Fano plane F on Ω.

In particular Q embeds in Aut(F). This is not an assumption that Q was simple or a pre-selected finite group.

## 4. Elementary automorphism facts and the exact image Q

### 4.1 The Fano plane has the binary-vector model and168 automorphisms

For completeness, every2-(7,3,1) design has the standard unique form. Label the three lines through point1 as123,145,167. The line through2,4 must have its third point among6,7; interchange6,7 to make it246. Pair uniqueness then forces257,347,356 as the remaining lines. These seven triples use every pair once.

Identify points1,2,4 with independent e1,e2,e3 in F_2^3; points3,5,6,7 are e1+e2,e1+e3,e2+e3,e1+e2+e3. The displayed lines are exactly triples {x,y,x+y} of nonzero vectors. A permutation preserving lines is determined by the images of the independent ordered triple1,2,4. There are7·6·4=168 possible independent ordered images, and each extends to a unique invertible linear map preserving all lines. Hence Aut(F)=GL(3,2), of order168.

Every such automorphism is an EVEN permutation of the seven points. Gaussian elimination over F2 expresses every invertible matrix as elementary coordinate-addition matrices (a coordinate interchange is a product of three additions). A coordinate addition fixes the three nonzero vectors with the added coordinate zero and swaps the remaining four in two transpositions. These generators are even, so Aut(F)≤A7.

### 4.2 The exceptional indices force Q=Aut(F)

Since Q≤Aut(F), |Q| divides168. The residual indices7·2^a and7·3^b, with a,b positive, both divide |Q|. Thus42 divides |Q|, and the only possibilities are42,84,168.

For |Q|=42, the number of Sylow7-subgroups divides6 and is1 modulo7, hence is1. For |Q|=84 it divides12 and is1 modulo7, again hence1. In either case Q normalizes its Sylow7-subgroup P.

The normalizer of a7-cycle in S7 has order42: identify Ω with F7 and P with translations; its normalizer is exactly the affine maps x↦a x+b, with7 choices of b and6 choices of a. Its intersection with A7 has order21. Indeed translations are even, whereas x↦−x fixes0 and swaps the six nonzero residues in three pairs, so is odd; the sign homomorphism on that normalizer is nontrivial. As Q≤A7, a Q normalizing P has order at most21. This excludes42 and84.

Therefore |Q|=168 and Q=Aut(F). In particular the exceptional index7·3^b has b=1. No database/classification theorem has been used.

## 5. The two other index-seven cosets are line-map cosets in this SAME plane

The second index-seven subgroup L also has an orbit of size3 on Ω. Its stabilizer of that triple contains L and, just as in section3, is L itself. In the full Fano automorphism group, three-subsets have two orbits: the seven lines and the28 noncollinear triples. The latter orbit is transitive because ordered independent triples are transitive under GL(3,2); its stabilizer has order168/28=6. Since L has order24, its3-orbit triple cannot be noncollinear. Thus L is the set stabilizer of a line of the SAME Fano plane F. The same conclusion already holds for K.

Fix the natural base point a=H∈Ω. Four H-cosets are exactly the four sets of elements q with q(a) equal to one of four distinct points. Let T be the complementary three points. A coset gK of a line stabilizer has point-image set g(K·a). Its orbit size is3, so a lies on the line stabilized by K; gK sends that line onto the line g(K·a). Being disjoint from the four H-cosets forces its point-image triple to be exactly T. Hence T is a Fano line. The same holds for g'L.

Consequently the two extra index-seven cosets have the form

    {q∈Q : q(L_1)=T},       {q∈Q : q(L_2)=T},

for two lines L_1,L_2 THROUGH a. If L_1=L_2 these cosets coincide, impossible. Hence they are two different lines among the three through a.

For any q with q(a)∈T, the preimage q^{-1}(T) is a line through a, and is uniquely one of those three. Thus all elements not in the four H-cosets partition into exactly THREE line-map cosets, one for each line through a. The two displayed cosets occupy two of them. The complement of all SIX index-seven cosets is exactly the remaining line-map coset

    xJ={q∈Q : q(L_3)=T},

where J=Stab_Q(L_3) has index7.

## 6. Final contradiction inside the remaining line coset

Both exceptional cosets must lie entirely inside xJ, because they are disjoint from all six ordinary index-seven cosets. If gV⊆xJ, then g∈xJ and left translation shows V⊆J. Therefore the two exceptional pieces, translated into J, are full left cosets of subgroups of J having indices

    [J:V_A]=2^a,         [J:V_B]=3^b.

These indices are coprime. By the elementary coprime-index intersection lemma they cannot be disjoint. This contradicts the original P7 configuration and closes the finite R4 image.

Hence an index-seven overgroup containing four original subgroup vertices is impossible. The subgroup generated by any four U_i has finite index dividing their common index gcd7, so its index is1 or7. The index-seven option was just excluded. Every four therefore generate G. Applying the same proof to inverted left cosets proves the second orientation. QED, at the declared imported interfaces.

## 7. Remaining unrestricted obstruction and verification

The actual Sun8/P7 target is still NOT proved. It remains possible only in a hypothetical configuration whose every four subgroup vertices generate the entire group (in both orientations), with no subnormal vertex; a minimal finite example also has O_{7′}(G)=1. The argument does not show that such a configuration exists, nor that a four-vertex proper join must occur. The remaining bridge is exactly to force an excluded join or otherwise contradict this unrestricted all-joins-full geometry.

Independent reconstruction is particularly needed for LemmaF's order-three cases, the use of MSB only on cells of size≤4 in the consumed R4 source, the quotient overlap bridge, the Sylow/normalizer exclusion, and the final Fano complement argument. No finite point evaluation, solver, enumeration, kernel or modelCLI has checked this snapshot. Correctness, import trust, scope, novelty and significance remain separate; all new snapshots are immutable candidates pending actual peer and parent checks.
