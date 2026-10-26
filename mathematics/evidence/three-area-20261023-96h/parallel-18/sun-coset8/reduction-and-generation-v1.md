# Sun(8): prime-seven reduction and five-wise generation — candidate v1

Observed before creation: `2026-10-23T14:10:01-0700` (`/bin/date`). **CANDIDATE; single-author written mathematics, no executable scientific check, no formal or novelty acceptance.** Full Sun8 is NOT proved. Scope and source freeze: `selection-v1.md`.

## 1. Exact imports and target

Write Sun(k) for: every k pairwise disjoint left cosets of finite-index subgroups of an arbitrary group have a pair of indices with gcd at least k. The target is Sun(8), without normality, solvability, valuation, cofactor or finite-original-group restrictions.

Imports are only:

- **S7:** the literal arbitrary-group Sun(7) statement accepted internally by `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, read with final reportv17 and its mandatory delivery erratum and ledger errata15/16. Recorded SHA256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. This is an explicitly trusted internal written interface, not a formal or human/priority certification. No historical solver execution or seven-coset component is generalized.
- **Z3/Z4:** Zhu, IJMM3(2008),197–206, Theorem1.1, <https://arxiv.org/html/0807.2207v1>: arbitrary-group Sun(3) and Sun(4).
- Elementary finite-index subgroup facts, proved below where load-bearing; in particular coprime-index cosets must intersect. No Margolis–Schnabel five-tuple lemma, no G-to-Z transfer, no computation and no minimal-order assumption is used.

## 2. Finite-core bridge and coprime-index lemma

For the original eight finite-index subgroups U_i of arbitrary G, let N be the intersection of their cores. Each core is the kernel of the finite permutation action on G/U_i and has finite index. Thus N is normal, finite-index and contained in every U_i. Each g_i U_i is the full preimage of its quotient coset. Quotienting by N preserves all eight indices, every subgroup-intersection index and pairwise disjointness. It is therefore enough to work with finite G; this is a reduction, not an added hypothesis.

For finite-index H,K with coprime indices a,b, pass to their common finite core if necessary. The intersection index I=[G:H∩K] is a multiple of lcm(a,b)=ab. The product formula gives |HK|/|G|=I/(ab), while HK⊆G. Hence I=ab and HK=G. Consequently every left H-coset meets every left K-coset: xH∩yK is nonempty iff x^{-1}y∈HK (inverse signs inside H,K do not alter the product-set criterion).

The same argument applies inside any subgroup and to any translated intersection with a fixed left coset of that subgroup.

## 3. Exhaustive new eight-coset reduction

**Theorem R8 (relative to S7).** Any counterexample to Sun(8) has

    n_i=[G:U_i]=7 r_i  (1≤i≤8),
    gcd(r_i,r_j)=1  (i≠j).

Equivalently every one of its28 pairwise index gcds is exactly7. No restriction on the r_i beyond the DERIVED pairwise coprimality is imposed: arbitrary prime factors, powers and one cofactor divisible by7 remain allowed.

**Proof.** In a counterexample all pairwise gcds are at most7; the coprime-index lemma excludes gcd1. By S7, each seven-element subfamily has a pair of gcd at least7, hence exactly7. Let A={i:7 divides n_i}. The gcd-seven pairs are precisely the pairs inside A. Every seven-subset must contain at least two elements of A, so |A|≥3: if |A|≤2, delete one member of A (or any vertex when A is empty) to leave at most one.

Assume A is proper and choose j outside A. For each i∈A, gcd(n_i,n_j)>1, and its prime factors cannot include7 because j∉A or exceed7 because the gcd is at most7. Therefore each i∈A has some prime in {2,3,5} dividing both n_i and n_j. No prime from {2,3,5} can divide two different A-indices: their gcd would be at least14. Their nonempty supports in {2,3,5} are thus disjoint. It follows that |A|≤3. Since |A|≥3, equality holds and those three supports are the three singleton primes2,3,5, in some order.

Every outside index must share a prime with each of the three A-indices, so EVERY outside index is divisible by2·3·5=30. There are five outside vertices; two of their indices have gcd at least30, contradiction. Hence A is all eight vertices. Every pair then has gcd7. Dividing every index by7 gives the stated cofactor coprimality. QED.

**Exact remaining obligation P7.** Prove that no arbitrary group has eight pairwise disjoint left cosets with indices 7r_1,...,7r_8 and pairwise coprime positive r_i; or exhibit a genuine exact group/coset realization. R8 plus P7 gives the entire target. Conversely any such realization is a Sun8 counterexample. Thus this is an exact residual, not an ansatz or a local index-pattern counterexample.

## 4. Fibre mechanism for an index-seven overgroup

The following results hold directly for P7 and use only elementary facts plus Z3/Z4; they do not import S7 again.

Suppose W≤G has index7. Put t_i=[U_i:U_i∩W]. The coset g_iU_i meets exactly t_i left W-cosets, where 1≤t_i≤7. Its nonempty intersection with any such W-coset, translated into W, is a left coset of U_i∩W of index

    λ_i=[W:W∩U_i]=r_i t_i.

Indeed [G:W∩U_i]=[G:U_i]t_i=7r_i t_i, and division by [G:W]=7 proves the formula. The t_i cosets are distinct because representatives g_i u and g_i u' lie in the same W-coset iff u'^{-1}u∈U_i∩W. All fibre pieces are disjoint whenever their original cosets are disjoint.

If U_b≤W then t_b=1, and its original coset occupies exactly one W-coset. Such baseline cosets for different b occupy DIFFERENT W-cosets: if two shared a W-coset, the corresponding indices inside W would be r_b,r_c, which are coprime, forcing intersection.

For an outlier i and baseline b, sharing b's occupied W-coset requires

    gcd(r_b, r_i t_i)=gcd(r_b,t_i)>1.

Since the r_b are pairwise coprime, at most ω(t_i) baseline cells can be met, where ω(t) is the number of distinct prime factors (ω(1)=0). This is a necessary condition only, not a realization criterion.

## 5. Five-common-overgroup exclusion

**Theorem G5.** In P7, no index-seven subgroup W contains five of the U_i. In particular, in any hypothetical Sun8 counterexample, **every five of U_1,...,U_8 generate G**.

**Proof.** Suppose W contains U_1,...,U_5. Their five original cosets occupy five distinct W-cosets. Call the other two W-cosets holes. The remaining three subgroups/cosets are called outliers; they need not actually lie outside W, and t=1 is allowed.

Each outlier meets t cells, at most ω(t) baseline cells and at most two holes. Therefore t≤2+ω(t). For 1≤t≤7, this forces t∈{1,2,3}: at t=4,5,6,7 the right sides are3,3,4,3 respectively. If t=1, the outlier lies in a hole because it has gcd1 with each baseline fibre. If t=3, some baseline cofactor is divisible by3, and the outlier meets that baseline cell and BOTH holes. This baseline3-carrier is unique, and no outlier cofactor is divisible by3.

### 5.1 No outlier can have t=3

If a t=3 outlier coexists with a t=1 outlier, their fibre indices 3r_i and r_j are coprime (the factor3 belongs to a baseline cofactor). The t=3 outlier meets both holes, leaving no possible hole for the t=1 outlier. Thus no t=1 is then possible.

For a t=3 outlier i and t=2 outlier j, their fibre indices 3r_i and2r_j have gcd1 unless2 divides r_i; the factor3 cannot divide r_j. If the gcd were1, j could meet neither hole, but could meet at most one baseline cell (the unique possible2-carrier), fewer than its required two cells. Hence every t=3 outlier coexisting with a t=2 one must have even r_i.

There are three outliers. If exactly one has t=3 and the other two have t=2, the t=3 cofactor is even. No baseline cofactor is then even. Each t=2 outlier meets both holes. In either hole the three fibre indices are 3r_i,2r_j,2r_k; their pairwise gcds are exactly2. Z3 forbids these three disjoint fibre cosets.

If exactly two have t=3 and the third t=2, both t=3 cofactors would have to be even, contradicting cofactor coprimality.

If all three have t=3, they all meet the baseline3-carrier cell. In that W-coset the baseline piece together with the three outlier pieces has indices r_b,3r_i,3r_j,3r_k, whose pairwise gcds are exactly3. Z4 forbids four such disjoint cosets. This exhausts the possibilities, so all outliers have t∈{1,2}.

### 5.2 A baseline cofactor is even

There is at most one such baseline b, and all three outlier cofactors are odd. Each t=2 outlier may meet only the two holes and b's baseline cell. Each t=1 outlier is in a hole and has gcd1 with every other outlier's fibre index; it therefore reserves that hole exclusively.

- Three t=1 outliers cannot fit in two holes.
- Two t=1 outliers reserve both holes, leaving a t=2 outlier only one possible cell.
- One t=1 outlier reserves one hole. Both t=2 outliers must then meet the other hole and b's cell. In b's cell the baseline and two outliers have all pairwise fibre gcds2, contrary to Z3.
- With no t=1 outlier, all three have t=2 and require six incidences in the three available cells. Each hole holds at most two outliers by Z3 (their fibre indices have pairwise gcd2), and b's cell holds at most one outlier by Z3 including the baseline piece. Capacity is at most2+2+1=5<6.

Every case is impossible.

### 5.3 No baseline cofactor is even

Every t=2 outlier must meet both holes, since it cannot share a baseline cell. Every t=1 outlier is in a hole.

- Three t=1 outliers have pairwise coprime fibre indices and cannot fit in two holes.
- Two t=1 outliers plus one t=2 outlier require BOTH t=1 cofactors to be even to coexist with the t=2 piece (which meets both holes). At most one cofactor is even, contradiction.
- One t=1 outlier plus two t=2 outliers requires the t=1 cofactor to be even. The other two cofactors are odd. In its hole the three fibre indices have all pairwise gcds exactly2, contradicting Z3.
- Three t=2 outliers meet each hole and have pairwise fibre gcds exactly2 (at most one cofactor is even), again contradicting Z3.

This finishes the exclusion of W. Finally, the subgroup generated by any five U_i has finite index dividing all five n_i. Their common gcd is7, so that index is1 or7. The index-seven possibility was just excluded; hence the generated subgroup is G. QED.

## 6. Consequences in both orientations

Inversion sends g_iU_i to g_i^{-1}U_i^* with U_i^*=g_iU_i g_i^{-1}; these are again disjoint LEFT cosets of the same indices. Therefore R8/P7 and G5 apply to both the original subgroups and U_i^*. A hypothetical counterexample must satisfy five-wise generation in BOTH orientations. This does not assert a common conjugating element or normality.

**No normal vertex.** If some U_v is normal, every product U_vU_j is a subgroup. Put α_vj=[G:U_v∩U_j]/(7r_vr_j), a positive integer. Product sizes give |U_vU_j|/|G|=α_vj/7. Disjointness excludes U_vU_j=G, so 1≤α_vj≤6. Since U_vU_j is a subgroup, 7/α_vj is an integer; primality forces α_vj=1 for all j≠v. Passing to G/U_v, every other subgroup image has index7. Their quotient cosets remain disjoint: whenever two quotient cosets overlap, their pieces in a common U_v-coset have coprime indices r_i,r_j inside U_v, forcing an original intersection. The seven quotient cosets of index7 are therefore disjoint and cover the quotient. But the nonempty image of g_vU_v is disjoint from all of them, contradiction. Thus every U_i (and equivalently every conjugate U_i^*) is nonnormal. This is a re-derived elementary corollary consistent with the classical all-α-one obstruction, not a novelty claim.

## 7. Exact boundary and next structural obligation

The full theorem is still missing: **P7 has not been excluded**. The new necessary obstruction is an eight-vertex, uniform-prime-seven geometry, with arbitrary pairwise-coprime private cofactors, no normal subgroup vertex, and every five subgroup vertices generating G in both orientations. Neither a local index pattern nor a symmetric matrix of intersection labels realizes that geometry.

The next bounded written attack is to determine whether the actual subgroup-product intersection identities force an index-seven common overgroup for five vertices, or otherwise contradict the fibre packing of P7. G5 alone does NOT prove such an overgroup exists. An alternative proof of P7 would also close R8. No numerical/solver implication, no finite-order coverage and no discovery/priority assertion is claimed.

## 8. Verification needed at these pinned bytes

Independent written reconstruction should check R8's A7-incidence argument; the left-coset orientation of the fibre formula; the complete t=3 and t=1/2 case partitions; and the generated-subgroup index bridge. The parent and a separate in-harness agent have not yet reviewed this snapshot. There has been no scientific execution, no historical checker replay, no modelCLI and no Lean/kernel or human review.
