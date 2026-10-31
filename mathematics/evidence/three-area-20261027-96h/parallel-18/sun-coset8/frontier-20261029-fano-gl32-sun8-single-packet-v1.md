# Sun8 in GL3(2)=PSL3(2): one complete Fano-plane packet

Actual `/bin/date` immediately before this new body: **Thu Oct 29 09:30:00 PDT 2026**. Owner: **MathSun8-2**, math-6. **WRITTEN, with separate author-run exact finite corroboration; UNREVIEWED, UNADOPTED.**

## 0. Exact statement and provenance

**Theorem.** If G=GL3(F2) and g_i H_i, 1≤i≤8, are nonempty pairwise-disjoint left cosets of arbitrary subgroups, then some pair of subgroup indices has gcd at least 8. Subgroups may repeat. No covering, maximality, stabilizer or common-conjugacy-class hypothesis is imposed.

This is the eight-coset Sun8 statement for this one group. It implies absence of an eight-disjoint-coset family with all 28 pairwise index gcds exactly 7. It does not exclude seven distinct index-7 subgroups, seven gcd-7 indices or seven disjoint cosets: all exist. No assertion about all finite simple groups or arbitrary groups follows.

Read the complete mandatory overlays first, in this order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA256 `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json`, SHA256 `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json`, SHA256 `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. Relative filenames are in the owner's exclusive new-window root.

The owner's wide-search preview frontier `frontier-20261028-sun-wide-search-preview-frontier-v1.json`, SHA256 `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6`, is cited status-only. Displayed snippets stay NONINPUT; none is used, reconstructed or searched for. Prior owner GL3(2) candidates include `frontier-20261028-gl32-sun8-geometric-v1.md`, SHA256 `d7c18486c27d7f50d792d57c6ed493f4ceb19c4a8df0c2ff041a59e3ff1c4da0`, and `frontier-20261028-gl32-sun8-v1.md`, SHA256 `f54d7aa6fecce85a311d6314a656abc284f18bf958064254946e702f7a0f0823`. This packet consolidates that known author context into one standalone obligation; it is not a new group-family count and transfers no old verdict.

Only elementary finite-group facts and linear algebra over F2 are used below, including Lagrange, Sylow/orbit-stabilizer, coset actions and the elementary rational/Jordan canonical forms of 3×3 matrices. Simplicity is proved in §2, not imported from CFSG. No Sun7, R8, descent, maximal-subgroup classification, alternating-group result or Lie-type packet is a premise. The proof does not depend on a computer check.

## 1. Two elementary coset lemmas

**Coprime indices.** For U,V≤F in a finite group, let a=[F:U], b=[F:V], c=[F:U∩V]. The integer c is divisible by both a,b and is at most ab, since |UV|≤|F|. If gcd(a,b)=1 this forces c=ab and UV=F. For any x,y, factor x^{-1}y=uv with u∈U,v∈V; then xu=yv^{-1} lies in xU∩yV. Hence disjoint cosets have index gcd at least 2, with no normality assumption.

**Subcosets.** If yK⊆xL, then x^{-1}y∈L and K≤L, and x^{-1}yK is a coset of K inside L. If [F:L]=7 and [F:K]=7a, then [L:K]=a. The same left translation preserves disjointness of multiple subcosets.

## 2. The group and its minimal index

The group order is (8−1)(8−2)(8−4)=168. Since F2^×={1}, every invertible matrix has determinant 1 and the center is trivial. Thus GL3(2)=SL3(2)=PSL3(2).

For completeness its elementary conjugacy-class sizes, obtained from the 3×3 canonical forms, are:

| Type | Order | Centralizer size | Class size | Number of classes |
|---|---:|---:|---:|---:|
| identity | 1 | 168 | 1 | 1 |
| unipotent J2+J1 | 2 | 8 | 21 | 1 |
| unipotent J3 | 4 | 4 | 42 | 1 |
| irreducible quadratic x²+x+1 plus a fixed line | 3 | 3 | 56 | 1 |
| irreducible cubic | 7 | 7 | 24 | 2 |

Here the two cubics are x³+x+1 and x³+x²+1. An irreducible block has centralizer the multiplicative group of its field; J3 has invertible centralizer {I+aN+bN²:a,b∈F2}. The involutions are precisely the transvections I+vf with v≠0, f≠0 and f(v)=0, where f is a covector: there are 7·3=21, and they are conjugate by choosing an adapted basis. The displayed sizes sum to 168 and exhaust the canonical forms of invertible 3×3 matrices.

A normal subgroup is a union of entire classes and its order divides 168. If it avoids the odd-sized involution class, its order is odd; every nontrivial such union has order at least 25, larger than the largest odd divisor 21. If it contains that class, its order is 22 plus a subset sum of 42,56,24,24. A proper even divisor of 168 at least 22 is 24,28,42,56 or 84, requiring a subset sum 2,6,20,34 or 62; none occurs. Thus G is simple.

A proper subgroup of index m≤6 would give an injective coset action of G into S_m, impossible since 7 divides 168 but not m!. Therefore every proper subgroup has index at least 7.

Let V=F2^3, Ω=V∖{0}; regard Ω as the seven points of the Fano plane. A line is the three nonzero vectors in a two-dimensional subspace. There are seven lines, three through each point, and four not through each point. Every two distinct lines meet in one point. Three noncollinear points form a basis.

## 3. All index-7 subgroups and cosets

An index-7 subgroup H has order 24. It cannot be transitive on Ω since 7∤24. If it fixes a point p, it equals the point stabilizer G_p, whose order is 168/7=24. Otherwise its orbit partition is 4+3 or 3+2+2: orbit sizes divide 24 and there is no fixed point or 7-orbit. A preserved two-set {u,v} forces H to fix u+v, contradicting the no-fixed-point assumption; alternatively its setwise stabilizer has order 8. Thus only 4+3 remains. If the three-orbit is a triangle/basis, its setwise stabilizer has order 3!=6, too small. Hence the three-orbit is a line L, and H is the full line stabilizer G_L, also order 24.

The point and line stabilizers are different subgroups: a point stabilizer has point orbits of sizes 1 and 6, so cannot preserve a three-point line. They give the complete two classes of index-7 subgroups, seven of each.

For p,q∈Ω and lines L,M, put

P(p,q)={g:g(p)=q},    E(L,M)={g:g(L)=M}.

These are exactly the index-7 cosets, 49 point events and 49 line events. No point event equals a line event, because equality of left cosets would imply equality of their underlying subgroups.

**Disjointness rules.** Distinct point events are disjoint precisely when they have the same source and different targets, or the same target and different sources. For two distinct sources and two distinct targets, the prescribed two-point bijection extends to an invertible linear map: each distinct nonzero pair is independent. The same rule holds for two line events by duality. For a mixed pair, P(p,q) and E(L,M) meet if and only if the incidence statements p∈L and q∈M agree. If they disagree intersection is impossible. If they agree, choose adapted bases: a basis starting with p and a second vector in L for an incident pair; or p plus a basis of L for a nonincident pair. Mapping one such basis to another gives an invertible map satisfying both requirements.

A pairwise-disjoint family of three or more point events has a common source or common target. If two share a source and have different targets, any event disjoint from both must share the same source; it cannot share both different targets. The common-target case is symmetric. The identical assertion holds for line events.

## 4. Six-coset complement lemma, with every mixed case

**Lemma.** The complement of any six pairwise-disjoint index-7 cosets in G is another index-7 coset.

Let a of the six be point events and b be line events. The automorphism θ(g)=(g^{-1})^T exchanges point and line events (identifying a line with the kernel of a nonzero covector). Hence assume a≥b. Inversion g↦g^{-1} exchanges sources and targets of both types and preserves disjointness and the left-coset property, since (xH)^{-1}=x^{-1}(xHx^{-1}). Since a≥3, the point-event star rule lets us assume that the a point events are P(p,q), q∈Q, for one p and |Q|=a.

The mixed disjointness rule says that a line event E(L,M) disjoint from all of these must satisfy exactly one of:

- p∈L and Q∩M=∅;
- p∉L and Q⊆M.

The possible pairs (a,b) are (6,0), (5,1), (4,2), (3,3).

**(6,0).** The complement is P(p,q_0) for the unique point q_0 outside Q.

**(5,1).** Impossible: the first alternative permits at most four targets outside M, and the second at most the three points of M.

**(4,2).** Only the first alternative is possible. Both line events have target M=Ω∖Q, which must be a line, and distinct source lines through p. There are exactly three lines through p. The set {g:g(p)∈M} is the disjoint union of E(L_j,M) over those three source lines: g^{-1}(M) is the unique line through p mapped to M. The two present events occupy two summands; together with the point events, they leave the third E(L_0,M) as complement.

**(3,3), Q a line.** No line is disjoint from Q, so only the second alternative occurs. All three line events have target Q and distinct source lines not through p. There are four such source lines. The point events occupy exactly those g for which g^{-1}(Q) passes through p. The three line events occupy three of the four other possibilities. The complement is E(L_0,Q) for the fourth source line not through p.

**(3,3), Q a triangle.** The second alternative is impossible. Write Q={u,v,w}, a basis of V. The unique line disjoint from Q is M={u+v,u+w,v+w}; the only other point outside Q is s=u+v+w. To check uniqueness, any line in {u+v,u+w,v+w,s} containing s and another point has third point in Q, while the first three sum to zero. Thus every line event has target M and a source line through p. The three distinct source lines are all three lines through p, so their union is {g:g(p)∈M}. Adding the point events {g:g(p)∈Q} leaves precisely P(p,s).

These cases exhaust all possibilities; undoing θ and inversion takes an index-7 coset to another such coset. The lemma follows. □

## 5. Proof of Sun8

Suppose eight disjoint cosets have all pairwise index gcds at most 7. Every index is at least 7 by §2.

If no index is 7, every index divides 168 and exceeds 7, so belongs to this complete divisor list:

8, 12, 14, 21, 24, 28, 42, 56, 84, 168.

It is not necessary to decide which of these are realized by subgroups. Partition the list into four classes:

{8,24,168}; {12,84}; {14,28,42,56}; {21}.

Two indices in the same class, including a repeated index, have gcd at least 8. A family with all pairwise gcds at most 7 can therefore use at most four indices, not eight. Thus at least one index is 7.

By the coprime-index lemma, every other coset must then have index divisible by 7. Write the eight indices as 7a_i. Since all pairwise gcds are exactly 7, the a_i are pairwise coprime divisors of 24=2^3·3. At most two of them exceed 1; arbitrarily many units are permitted. Hence at least six cosets have index 7. Seven such disjoint cosets would already occupy 7·24=168 elements, leaving no room for an eighth. There are exactly six.

Their complement is xL for an index-7 subgroup L by §4. The other two cosets lie inside xL and, after the same left translation, become disjoint cosets inside L with indices a,b. But gcd(a,b)=1, contradicting the coprime-index lemma inside L. The theorem follows. □

**Seven-coset boundary.** The seven cosets of a point stabilizer partition G with every index 7 and every pairwise gcd 7. Seven distinct stabilizers also give a partition by the events P(p,q_0) with q_0 fixed. In a valid proof, these boundaries are not suppressed by cofactor counting.

## 6. Separate exact finite corroboration

Checker: `frontier-20261029-small-simple-sun8-check-v1.py`, SHA256 `7e36d8e9d55fdfee253cd82a7c3ed8de4cc6b9fd0d89e1bb480d4891cc7e772d`, 287 LF / 12782 bytes. Receipt: `frontier-20261029-small-simple-sun8-check-receipt-v1.json`, SHA256 `4ffb680ef6e14673f7c9e491e0acee94f191cc379dd37d27680b38ab3e2c7cb5`. The single completed run lay between native observations 09:24:08 and 09:25:39 PDT, using existing NumPy and exact integer permutation/matrix arithmetic in the author's Python eval kernel.

The script builds all invertible binary 3×3 matrices as their faithful permutations on V∖{0}. It enumerates 168 elements, 15 subgroup conjugacy classes and all 179 subgroups. The proper indices are exactly 7,8,14,21,24,28,42,56,84,168. It constructs 98 actual index-7 cosets, not just index values. It checks all 1568 unordered six-families of disjoint such cosets; each complement is another index-7 coset. Each representative order-24 stabilizer has 30 subgroups; all 27 pairs with coprime proper indices have actual product equal to the full stabilizer, checked for both stabilizer classes.

The only feasible eight-index multisets under the elementary gcd and size constraints are (7,7,7,7,7,7,14,21), (7,7,7,7,7,7,21,28) and (7,7,7,7,7,7,21,56). Together with the six-complement and stabilizer-product checks, this gives the same exclusion as the written theorem. It does not presuppose the Fano classification or mixed-case proof in §§3–4.

Enumeration completeness is by induction on a generating list. Starting with the trivial subgroup, join each known conjugacy-class representative to each cyclic subgroup not already contained in it; compute the generated finite monoid/subgroup and insert every conjugate when new. Every subgroup generated by g_1,…,g_r is reached up to conjugacy by iterating this operation. All actual conjugates are expanded; each stored subgroup is checked for identity, inverse and multiplication closure. The routine therefore does not assume a published subgroup lattice.

This is a **reduction-based exhaustive check**, not a direct scan of all eight-coset subsets. It uses exactly the two elementary lemmas of §1 to exclude coprime-index pairs and to move the last two cosets inside the checked stabilizer. The one completed checker is author-run corroboration, not independent-family verification. The receipt is not a second checker.

Positive controls: the seven index-7 cosets form an actual partition, and eight cosets of an index-8 subgroup form an accepted family at gcd cap 8. Mutations reject a duplicated coset for `COSET_OVERLAP`, a wrong index for `SIZE_INDEX_MISMATCH` and that eight-coset family at cap 7 for `INDEX_GCD_EXCEEDS_CAP`. The two earlier generic 6746-coset searches timed out at 600 and 900 seconds and supplied no exclusion evidence. The new index-multiset-first representation replaces them; their timeouts are not counted as successful verification.

## 7. Review obligations and nonclaims

A reviewer should check the elementary simplicity argument, every order-24 subgroup case, the point/line/mixed disjointness rules, all four splits of six cosets (including both (3,3) subcases), the divisor-class argument, repeated unit cofactors and the exact two-coset application inside L. The finite checker is separate corroboration; the written proof does not need it. No isomorphism with PSL2(7) is required for the theorem about GL3(2); identifying another group with this one remains an explicit additional input whenever used.

No Lean/kernel proof, independent-model-family/human review, priority search, mathematical novelty clearance, parent adoption, all-simple-group or arbitrary-group Sun8 result is claimed. The 09:18 cadence PROCESS MAJOR and all earlier findings/quarantines remain permanent; frozen sources and reviews remain unchanged. In particular this author packet does not promote the unfrozen conditional assembly.
