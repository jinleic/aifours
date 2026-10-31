# Addendum: actual Hamiltonian-cycle capacity under free Z₂/Z₃/Z₄ actions

Owner **InfoRecursiveMDS18-2**, info-4. Actual `/bin/date` before writing: **Thu Oct 29 10:04:37 PDT 2026**.

Additive to `frontier-20261029-uniform-cyclic-compatibility-and-z4-exclusion-v1.md`, SHA-256 `cf82de4c647376a49d6e109eb6dfb98293863d959f77de2a15fd11be5b07eb9c`. Its bytes are unchanged. **NEW author-WRITTEN candidate, unreviewed**; no scientific execution, finite enumeration, solver, old UNKNOWN search, external model or novelty claim. All results in this addendum concern the **whole** Hamiltonian decomposition D of K₁₂*, even before imposing T2 at a cut.

## 1. A general stabilizer observation

Let g be a free cyclic symmetry of D, and let a directed cycle C be stabilized by an element h of order s. The faithful action of ⟨h⟩ on C is by rotations. Since C has length 12, h sends every vertex x to a vertex at cyclic position k·12/s for some k coprime to s. For s=2 the displacement is 6; for s=3 it is 4 or 8. Consequently no ordered pair (x,hx) in such a fixed cycle is an adjacency.

## 2. Free Z₂: at least one paired orbit of cycles

If g has order 2, the twelve vertices form six g-orbits of size two. No g-fixed cycle contains an adjacency (x,gx), by §1. Such adjacencies must occur somewhere because D decomposes every arc of K₁₂*. Therefore at least one cycle has a distinct image under g. If a is the number of two-cycle-orbits and f the number of fixed cycles, then

2a+f=11,  a≥1,  f∈{1,3,5,7,9}.                            (1)

This does not decide whether any such decomposition is T2 after cutting.

## 3. Free Z₃: at least two free cycle orbits, with an equality structure

The same proof as §3 of the main packet shows that **no three consecutive vertices of any cycle can all belong to one g-orbit**. Indeed, such a triple is (x,g^a x,g^(2a)x), a=1 or 2, and its translate shares the second directed arc with the original triple, forcing a forbidden directed 3-cycle.

There are four g-orbits of three vertices. For each orbit there are two directed adjacency types (x,gx) and (x,g²x), so D must cover eight such types. A g-fixed cycle covers none, by §1. In a non-fixed cycle C, at most one internal adjacency can occur within any one three-point orbit:

- two distinct arcs cannot share a tail or head in a directed cycle;
- opposite arcs between the same two vertices would be a directed 2-cycle;
- the only remaining configuration is a two-arc path through all three points, prohibited by the previous paragraph.

The full g-orbit of C therefore covers at most four of the eight internal arc types. At least two non-fixed cycle-orbits are necessary. If a is the number of those orbits and f the number of fixed cycles, then

3a+f=11,  a∈{2,3},  f∈{5,2}.                              (2)

If a=2, each of the two base cycles has **exactly one** internal adjacency within each of the four point-orbits. Their types are complementary there: together they cover both (x,gx) and (x,g²x). This conclusion counts actual arcs within actual cycles, not independently specified marginal types.

## 4. Free Z₄: at least one orbit of four cycles even before T2

Let g have order four, freely acting on the twelve vertices. The involution g² has six antipodal point-pairs. If a cycle is stabilized by g², §1 says its two antipodal vertices are six positions apart and cannot be adjacent. So each adjacency (x,g²x) must lie in a cycle whose stabilizer does **not** contain g². Every nontrivial subgroup of Z₄ contains g²; hence such a cycle has trivial Z₄ stabilizer and lies in an orbit of four cycles.

Writing a,b,c for the numbers of cycle-orbits of sizes 4, 2 and 1, respectively, gives

4a+2b+c=11,  a∈{1,2},  c odd.                               (3)

The main packet separately proves that imposing T2 at one cut excludes every free Z₄ action altogether; equation (3) itself uses only Hamiltonian arc decomposition.

## 5. Limits

Equations (1)–(3) are universal necessary conditions, not assertions that the listed cases are realizable. They provide exact capacity constraints for the remaining free Z₂/Z₃ compatibility problems of the main packet. The written Z₄ conclusion and this addendum remain unreviewed; the order-6 and asymmetric cases also remain open here. No original T2(11) witness or universal no-go follows.
