# Candidate exclusion of the entire (4,4,4,4) residual profile at support 46

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 20:04:55 PDT 2026`; not an exact completion time. **WRITTEN normal-form argument plus exact finite-enumeration candidate**, not independently accepted, formally verified, or novelty-cleared. It is conditional on `frontier-20261028-n46-residual-no-hamming1-v1.md`, SHA-256 `98bb82499cda7135db96de89b6a7fb9901274c892af3fd125ac7a9d446992b0d`, and the pinned residual/lower-bound prerequisites named there. The no-OLS(6) theorem is inherited. This is not by itself a global ≥47 proof.

## 1. Normal form for all four-valued residual alphabets

Assume the conditional N=46, t=26, n=10 case and residual alphabets `(4,4,4,4)`. Let P be the 26 maximal entries and E the remaining 20 positions. Every E coordinate-pair projection has ten values, each with exactly two E extensions. Let d_i(a) be the number of E partner symbols of local symbol a at any other party; this number is independent of the partner because the other `6−d_i(a)` pair values are occupied by distinct maximal P words. The incidence lemma gives d≥2, and the four d values at each party sum to 10. The only degree multisets are

`X=(2,2,2,4)` and `Y=(2,2,3,3)`.                                  (1)

Let n_k count P words with k active coordinates. Their total active and pair-active incidences are 56 and 36, and |P|=26. Solving the resulting integer equations gives exactly

`(n_0,n_1,n_2,n_3,n_4)=(0,2,18,6,0),(0,1,21,3,1),(0,0,24,0,2)`.

In particular there are at most two singleton-active P words. For a local active symbol a, if s,q,h count P words using a with respectively one, three, or four active coordinates, comparison of its `6−d_i(a)` P occurrences with their other-active incidences gives

`s−q−2h=2d_i(a)−6`.                                                (2)

A degree-4 symbol requires s≥2. Singleton-active words at different parties are distinct, so at most **one** party can have type X; all others have type Y. The cases are therefore all Y, or exactly one X.

The no-Hamming-one dependency says any four-point E fiber is one of the two binary parity subsets, hence its projection onto any pair of the other coordinates is the full 2×2 rectangle. A six-point E fiber has three local values in each other coordinate, each appearing twice. It is pair-injective on those three coordinates: otherwise two words in the fiber would differ only in the remaining fourth coordinate. A type-X eight-point fiber is likewise pair-injective; each of its three pair projections is a 2-regular graph on 4+4 vertices.

## 2. Incidence normalization and parity of projections

Choose a party A of type Y in the all-Y case, or the unique X party in the one-X case. Number its low-degree symbols first. For any other party j, the A–j E-pair incidence graph has row degrees equal to A's d sequence and column degrees equal to j's d sequence. It may be enumerated by its four row subsets:

- Y–Y: 34 labeled graphs. Permuting A's two low and two high symbols and independently permuting the corresponding classes of one partner B gives five orbits.
- X–Y: 15 labeled graphs. Permuting A's three low symbols and B's two low and two high symbols gives two orbits.

After normalizing the A–B graph to an orbit representative, both other graphs A–C and A–D may be arbitrary labeled graphs. C and D have the same type Y; swapping the parties is a symmetry, so their graph-list indices may be ordered C≤D. This gives `5·34·35/2=2,975` all-Y incidence patterns and `2·15·16/2=240` one-X patterns.

In any of BC,BD,CD, every E pair value has total multiplicity exactly two. Within each A fiber, pair projection is injective, by the no-Hamming-one property. Therefore the F₂ XOR of the four projected incidence sets must vanish. Each pair cell can occur in at most all four fibers; under XOR zero, excluding a cell occurring four times is equivalent to exact total multiplicity 0 or 2. These are necessary support conditions, not phase assumptions.

## 3. All-Y finite exclusion

A has two low four-point fibers, each one of two binary parity sets, and two high six-point fibers. Up to relabeling the three symbols used in each coordinate, a high fiber is a six-word subset of a 3×3×3 cube with each local symbol occurring twice and every two-coordinate projection injective. There are exactly 144. The first checker obtains them by balanced six-subset enumeration; the second independently constructs them as partial Latin tables: choose the missing matching in the first pair and assign the third symbols with row/column injectivity. Both record 144.

For each of the 2,975 incidence patterns and each high-fiber pair, the two low projections and two high projections must satisfy the XOR and no-fourfold-overlap condition of §2. Exactly **10** high-fiber projection pairs survive. Both parity choices on each low fiber produce **40** complete 20-point support candidates. These 40 form a conservative superset: the first program reports that 30 also have a distance-one pair **across** A fibers, but it retains them rather than silently pruning. Every one of the 40 has two rows or columns with exactly one shared nonzero position in **each** of the three 2|2 cuts. Such an overlap cannot occur in a unitary.

## 4. One-X finite exclusion

A has three low parity fibers and one high eight-point fiber. For a pair among B,C,D, the high-fiber projection is the XOR of the three low 2×2 rectangles, because its projection is injective and the global multiplicity is even. It must be a 2-regular 4×4 graph, since every symbol of that coordinate occurs twice in the high fiber. No pair cell may appear in all three low rectangles and the high projection.

Among the 240 normalized incidence patterns, exactly **10** have three admissible high pair graphs. In each case the three graphs admit exactly eight candidate B,C,D triples, but those triples cover only six distinct pairs in each projection, so they cannot form the required pair-injective eight-word high fiber. The independent replay instead performs an exact triangle-edge-cover search and finds no cover for all 10 graph triples. Thus the one-X case is excluded.

## 5. Exact implementations and review boundary

First implementation `frontier-20261028-n46-4444-noh1-enum-v1.py`, SHA-256 `96c519e0169380d333fd7a1414925e0decca2335c6cdf0ac4846c377e7d4ee4c`; receipt `frontier-20261028-n46-4444-noh1-enum-v1.json`, SHA-256 `45e5a0fbdb0b13dcd3f26905dde807b7067dc6ada115a965ed2e81cd66dbd21e`. Its receipt includes all 40 all-Y supports and explicit unique-overlap witnesses in all three cuts, plus all 10 one-X triangle sets.

Independent implementation `frontier-20261028-n46-4444-noh1-latin-replay-v1.py`, SHA-256 `eb413c112a0398500f9642b9f39fb5ef20079f95aa09da29c95c27d298025425`; receipt SHA-256 `50a20186279163febfd47f586c37172d90ecd751a9cad19ddac4b7e7497ddd13`. It generates six-point fibers as partial Latin tables and uses direct edge-set multiplicity checks and an independent exact triangle-cover recursion; its counts match exactly.

Both implementations are same-harness exact controls, not independent human/model reviews or formal certificates. A reviewer should reconstruct the no-distance-one prerequisite, the at-most-one-X deduction, the five/two incidence orbit normalizations, the pair-projection XOR/cap completeness, and every reported overlap/triangle obstruction. The first checker intentionally covers distance-one supersets across fibers; only the within-fiber no-distance-one deductions are used to generate the normal form. No global lower-bound upgrade is accepted by this packet alone.
