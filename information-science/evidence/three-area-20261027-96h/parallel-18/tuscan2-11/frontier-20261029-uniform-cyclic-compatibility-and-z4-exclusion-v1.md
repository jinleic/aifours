# Uniform Z₂/Z₃/Z₄ orbit compatibility and a written Z₄ exclusion for T2(11) extensions

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 10:02:35 PDT 2026**.

**NEW author-WRITTEN candidate; not reviewed or adopted.** The existence/equivalence statements below apply to **every** free cyclic action of order 2, 3 or 4, with the actual Hamiltonian cycles and cut point retained. The Z₄ exclusion is a proposed written theorem, not an executed search. No solver, program, arithmetic kernel, finite enumeration, external model, protected review or old certificate is used in this packet. No formal/kernel, independent-model, human, novelty or parent-adoption claim.

**Named imports:** the definition of linear T1/T2 arrays; elementary finite cyclic-group and permutation facts; and, ONLY for the final application to every automorphism of an arbitrary T2(11), parent-adopted f175 Theorem A: every T1(p), p odd prime, has trivial symbol-automorphism group. Its parent disposition is `institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-prime-symbol-asymmetry-and-orbit-counts-parent-v1.md`, SHA-256 `20b187f303624afe0423fb4042b34a028f4cbdd3cc5577759bb709765e42d5eb` (same-harness written scope). The final group-order corollary additionally names Sylow's theorem. Neither the odd-order f187 candidate/review, the Z₄ timed-out search, the six/twelve exact-cover packet, nor either (6,3,2) SAT/DRAT receipt is an input.

## 1. Original objects, free actions, and the exact cut criterion

A directed Hamiltonian decomposition D of K₁₂* is a set of eleven directed 12-cycles in which every ordered pair of distinct vertices occurs once as a directed arc. Cutting every cycle immediately after a vertex u gives eleven permutation rows on the other eleven vertices, with each adjacent ordered pair occurring once: a T1(11) array A_u. Conversely, every T1(11) array determines D by adjoining u to each row. A_u is T2 exactly when all its linear distance-two pairs are distinct.

A cyclic **two-step event** of D is a triple (x,y,z) of consecutive vertices in one cycle. Every such triple has three distinct vertices. If two distinct events have the same ordered endpoints (x,z), then their middles y,y' differ: otherwise the same directed arc x→y would occur twice. Thus the union {x,y,y',z} has exactly four vertices. Call this pair of events a coincidence.

Suppose g∈Aut(D) has order q∈{2,3,4} and acts freely on the twelve vertices. Let O={u,gu,…,g^(q−1)u}. D-invariance sends A_u isomorphically to A_v for every v∈O. A cyclic two-step triple belongs to A_v precisely when it avoids v. Consequently the following is an **if and only if**, not just a necessary counting condition:

> A_u is T2  ⇔  every pair of distinct cyclic two-step events with the same ordered endpoints has O⊆{x,y,y',z}.  (1)

The forward implication uses invariance to obtain T2 at every v∈O; for the reverse, take v=u. No global 2-perfection is assumed.

For the application to an arbitrary T2(11), a nonidentity automorphism fixing u would restrict to a symbol automorphism of the cut T1(11), so the named f175 Theorem A makes it trivial. Thus every automorphism acts freely; any subgroup C_q may be put in the form above. This application does not require that the full automorphism group equal C_q.

## 2. A uniform, exact orbit-and-compatibility reduction

Set r=12/q. Relabel the free action as V=Z_q×{0,…,r−1}, with g(t,a)=(t+1,a), and choose u=(0,0). The entire distinguished orbit is O=Z_q×{0}. For ordered endpoints x=(t,a), z=(t+d,b), define their pair type

λ(x,z)=(a,b,d), with (a,b,d)≠(a,a,0).                    (2)

All ordered pairs with a fixed type form exactly one g-orbit of size q; there are 132/q types. If the middle is y=(t+h,c), its **aligned middle** is m=(h,c). Distinct middle labels for the same λ are precisely the distinct events over each aligned actual endpoint pair. The first endpoint, second endpoint and middle must be distinct.

Let K≤⟨g⟩ be the stabilizer of a directed Hamiltonian cycle C; its action on the twelve vertices is faithful and by cyclic rotations. Write s=|K| and L=12/s. There is a generator k of K that advances C by L positions. Taking positions x₀,…,x_{L−1} as representatives gives

x_{j+L}=k x_j; the x₀,…,x_{L−1} lie in distinct K-orbits.  (3)

Conversely, a sequence of L representatives of distinct K-orbits, extended by (3), is an actual directed Hamiltonian cycle. Include s=1, k=id, L=12. Different choices may describe the same cycle orbit; duplicates are harmless only if not selected twice.

For a candidate cycle orbit, retain its L **D1 types**, and for each of its first L cyclic triples retain (D2 type, aligned middle). Then:

1. The selected D1 type sets must partition all 132/q types. D1 types within a candidate cannot repeat. Indeed, equal types are translates of the same actual arc; if the corresponding translates are distinct cycle orbits this repeats an arc, while within the same cycle orbit the only stabilizer rotations preserving a representative class are multiples of L. Conversely, each selected type supplies all q actual arcs once.
2. For each D2 type λ, collect all aligned middles produced by all selected cycle orbits. D1 exactness prevents a repeated aligned middle for one λ: it would repeat the same actual first arc and successor. For **every pair** m≠m' in that collection, require

   O⊆{(0,a),(d,b),m,m'},  where λ=(a,b,d).                (4)

   This is exactly (1) after translating the first endpoint to (0,a). No requirement is imposed that each D2 type occur, or occur exactly once.

Conditions 1–2 are **sufficient as well as necessary**: expand every selected candidate to its full g-orbit of cycles; condition 1 gives an actual Hamiltonian decomposition, and condition 2 gives T2 at u by (1). They are a finite exact-cover-plus-local-compatibility problem on actual cycles, not a relaxation of row realizability. All candidate transversals and all middle choices are retained; no claim is made that a search of this problem has been run or finished here.

## 3. Sharpening for q=2 and q=3

Let O be the distinguished orbit. For a D2 pair type, its multiplicity is the number of aligned middles in §2. The following structural restrictions use actual D1 arc uniqueness and (1).

### q=2: exact collision categories and a partial matching

O={u,v}. For any repeated D2 pair:

- If both endpoints lie outside O, its two middles are exactly u and v. No third middle is possible. Such repeated pairs form a directed **partial matching** on V\O: each outside vertex occurs at most once as source and at most once as target. Otherwise two coincidences from the same source would force different successors after the same arc x→u; two into the same target would force different predecessors before the same arc u→z. The matching is g-invariant, so it contains at most ten ordered pairs, i.e. at most five pair types.
- If exactly one endpoint lies in O, the other point of O must be a middle. Multiplicity is at most two: any two other middles outside O would give a coincidence missing the second orbit point. At most one repeated type can start in O, because the arc u→v has one successor; similarly at most one repeated type can end in O, because that arc has one predecessor. This is a type-orbit statement, not a claim that the corresponding concrete source/target is fixed by g.
- If both endpoints lie in O, they are u and v in one order and every middle is outside O. There is one pair type of this form; each of its two ordered pairs may have up to ten distinct middles. No pairing or extra bound on those ten middles is assumed.

The full cycle system has 132 two-step events. If μ_λ is the multiplicity of each actual pair of type λ, let D=Σ_λ max(μ_λ−1,0). Then Σ_λ μ_λ=66, so D also equals the number of missing pair types. The restrictions above give

0≤D≤5+1+1+(10−1)=16; cyclic excess and missing pairs are both 2D≤32.   (5)

The matching and the named type restrictions are stronger than the scalar bound. They do not decide the q=2 class.

### q=3: only two possible repeated type-orbits

No cyclic triple can have all three vertices in O. For such a triple (x,g^a x,g^(2a)x), a∈{1,2}, translating by g^a produces the triple (g^a x,g^(2a)x,x). The shared directed arc g^a x→g^(2a)x belongs to a unique cycle, forcing that cycle to close after three vertices, contrary to Hamiltonicity on twelve vertices.

Thus in any coincidence, neither both endpoints nor neither endpoint can lie in O: in the first case (1) requires the third O-vertex as a middle, giving a prohibited all-O triple; in the second, two middles cannot cover all three O-vertices. Exactly one endpoint lies in O, and the two middles are the other two O-vertices. Every repeated type therefore has multiplicity exactly two.

There is at most **one** repeated type directed O→V\O. Indeed, fixing x∈O, both possible within-O first arcs x→gx and x→g²x force their successor to be the common target z. A second repeated pair from x would give one of those arcs a different successor. Translating by g identifies all sources in O, giving at most one entire pair type. The reversed predecessor argument gives at most one repeated type directed V\O→O.

Hence the circular two-step excess and number of missing ordered pairs are equal and belong to

**{0,3,6}.**                                                  (6)

Equivalently at least 126 of the 132 distinct directed pairs occur at distance two. This leaves the q=3 class open; the allowed coincidence patterns are not asserted realizable.

## 4. q=4 forces 2-perfection, without computation

For q=4, every coincidence has its entire four-vertex set equal to O. Label O by Z₄ and translate the first endpoint to 0. The second endpoint d is 1, 2 or 3; the middles must be the other two vertices. The two required triples, and the resulting step-type transitions, are:

| d | two triples inside O | forced successive step types |
|---|---|---|
| 1 | (0,2,1), (0,3,1) | 2→3 and 3→2 |
| 2 | (0,1,2), (0,3,2) | 1→1 and 3→3 |
| 3 | (0,1,3), (0,2,3) | 1→2 and 2→1 |

Translate both triples by every element of Z₄. Because each directed arc occurs in exactly one cycle and has exactly one successor in that cycle, every arc of either named step type is forced to be followed by an arc of one of those same two step types. Each such arc and successor remains inside O. Starting with any one of them, its Hamiltonian cycle can never leave the four-point set O, contradiction.

Therefore no coincidence exists. Since 132 cyclic two-step events have distinct ordered endpoints among exactly 132 possible directed pairs, **D is 2-perfect**. This conclusion covers all free Z₄-invariant extensions satisfying T2 at u, including cases that were UNKNOWN in earlier searches.

## 5. Written obstruction to free even-cyclic symmetry of a 2-perfect decomposition

**Lemma.** Let q≥2 be even and r≥1 be odd, with m=qr≥3. No 2-perfect directed Hamiltonian decomposition of K_m* is invariant under a free C_q action with r vertex orbits.

**Proof.** Label the points Z_q×{0,…,r−1} with g acting by +1 on the first coordinate. The pair types are (a,b,d), omitting only (a,a,0). Each type has q actual directed pairs. Since both D1 and D2 events are exact, over all cycle-orbit representatives the first L events of §2 contain each type exactly once at each distance.

For one cycle orbit and its period L, let δ_j∈Z_q be the coordinate increment of the directed arc from position j to j+1. The rotation relation x_{j+L}=g^t x_j implies δ_{j+L}=δ_j. The increment of a two-step pair is δ_j+δ_{j+1}; so, over one period,

Σ_{j=0}^{L−1} increment₂(j)=2Σ_{j=0}^{L−1} δ_j  (mod q).    (7)

Summing (7) over all cycle orbits equates the sum S of the increments of **all D2 types** with twice the sum of **all D1 types**, namely 2S. The type sets are the same at the two distances, so

S = r²·Σ_{d=0}^{q−1} d ≡ r²·(q/2) ≡ q/2  (mod q).           (8)

The excluded diagonal types have increment 0. Since q is even and r is odd, q/2 is nonzero modulo q, but 2S=0. This contradicts S=2S. ∎

For q=4,r=3, §§4–5 imply that **no free Z₄ action can preserve the circular extension of any T2(11)**. This is an all-variable written exclusion of that entire class; it is independent of the earlier 1,200-second UNKNOWN search and of the unreviewed order-6/order-12 computations.

## 6. Consequence and exact remaining gap

For an arbitrary T2(11), f175 Theorem A makes Aut(D) free on 12 points, hence its order divides 12. A subgroup Z₂×Z₂ cannot act on the eleven directed Hamiltonian cycles: a cycle stabilizer embeds faithfully into the cyclic rotation group of the cycle, so its orbit under that subgroup has size 2 or 4; eleven cannot be their sum. The q=4 theorem excludes a cyclic subgroup of order 4. By **Sylow's theorem** a group whose order is divisible by 4 contains a subgroup of order 4, which must be one of those two groups. Therefore the proposed WRITTEN consequence at the named f175/Sylow imports is

**|Aut(D)| ∈ {1,2,3,6}.**                                   (9)

If the order is 6, condition (1) forces D to be 2-perfect because a coincidence has only four vertices; no order-6 exclusion is asserted here. Orders 2 and 3 retain the exact compatibility conditions and stronger collision constraints in §§2–3. In particular the trivial-group case, which includes arbitrary asymmetric arrays, is the unrestricted original problem.

**No T2(11) witness or universal no-go is supplied.** The original existence question remains OPEN. No conclusion is taken from a timeout, an incomplete proof stream, an unreviewed computation, f187, or any held material. This new packet has not undergone a parent or peer review.
