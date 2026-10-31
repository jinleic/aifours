# f204 independent same-harness scientific review

**Disposition: 0 FATAL / 0 MAJOR / 2 MINOR**: one minor written-reference/scope defect in the order-6 corollary, repaired explicitly below; one minor review-process clock-recording deviation, disclosed below. No scoped mathematical claim remains INCONCLUSIVE after the written reconstruction. **INCONCLUSIVE / OPEN outside those claims:** existence of T2(11), the free Z2 and Z3 cases, order-6 symmetry, and the asymmetric case; the allowed collision/capacity patterns are not shown realizable. No timed-out or unreviewed search is evidence of exclusion.

Native clock observed with `/bin/date` before writing this review: **2026-10-29T13:19:00-0700 PDT**. This is a pre-writing observation, not an asserted file-creation time.

## Frozen inputs, measurement, and actual read sequence

The first research artifact opened was the assigned manifest `review-waves/f204-tuscan-uniform-cyclic-compatibility-and-z4-exclusion/manifest-v1.json`. Its measured SHA-256 is `06b51d5ef37c070ecf1b55b5f9c56e8479e7fa756e8660c3301b2196ea005fed`, matching the assigned `06b51d5ef37c` prefix. Before opening any input body, I measured all three declared inputs by SHA-256 and `wc -c -l`; every result matched its manifest entry:

| Order | Manifest input, relative to `/Users/jinleic/repos/aifours/` | Measured SHA-256 | Bytes | LF | Raw windows actually displayed, inclusive |
|---|---|---|---:|---:|---|
| 1 | `institute/runs/three-area-2026-10-27-96h/dispositions/info-4-tuscan-odd-prime-symbol-asymmetry-and-orbit-counts-parent-v1.md` | `20b187f303624afe0423fb4042b34a028f4cbdd3cc5577759bb709765e42d5eb` | 5995 | 22 | 1–11, 12–22 |
| 2 | `information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261029-uniform-cyclic-compatibility-and-z4-exclusion-v1.md` | `cf82de4c647376a49d6e109eb6dfb98293863d959f77de2a15fd11be5b07eb9c` | 13973 | 120 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120 |
| 3 | `information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261029-uniform-cyclic-cycle-capacity-addendum-v1.md` | `fab5aeafd4ccdaae1ae7851557d5de107a0735bc44cea294217ba2bc81412540` | 4392 | 47 | 1–15, 16–30, 31–47 |

The displayed windows cover every declared line, including each final line, in manifest order, before mathematical reconstruction or controls. I did not open linked mathematical bodies, author code, sibling reviews, or held material. The main packet and addendum are the claims under review, not imported authorities.

## Per-claim verdicts

Counts in a row are findings against that row; the disposition counts each distinct finding once.

| Claim | F / M / m / INCONCLUSIVE | Review conclusion |
|---|---|---|
| Decomposition–cut correspondence and the four-vertex coincidence criterion | 0 / 0 / 0 / no | Exact, including the reverse implication and all cuts in the distinguished orbit. |
| Semiregularity for an arbitrary T2(11) extension; cyclic stabilizer normal form | 0 / 0 / 0 / no | Correct, conditional only on expressly adopted f175 Theorem A for semiregularity. |
| D1 type partition, distinct aligned middles, and sufficiency of compatibility | 0 / 0 / 0 / no | Exact for actual cycle orbits with their actual stabilizers; no marginal-only relaxation. |
| Z2 collision categories, directed partial matching, and excess bound | 0 / 0 / 0 / no | Categories and `D≤16`, hence circular excess `≤32`, follow. |
| Z3 forbidden orbit triple, two possible repeated types, and excess | 0 / 0 / 0 / no | Circular excess and missing-pair count belong to `{0,3,6}`; realizability is not claimed. |
| Z4 coincidence elimination and consequent 2-perfection | 0 / 0 / 0 / no | Each of the three transition systems traps a cycle in four vertices. |
| General free even-cyclic, odd-orbit-count 2-perfect obstruction | 0 / 0 / 0 / no | The periodic jump-sum and parity contradiction reconstruct as stated. |
| Exclusion of free Z4 and `|Aut(D)|∈{1,2,3,6}` | 0 / 0 / 0 / no | Correct at the named f175 and elementary group/Sylow imports; does not exclude order 6. |
| Order-6 implication of 2-perfection | 0 / 0 / 1 / no | Correct, but the packet cites its (1), stated only for cyclic orders 2, 3, 4; a full order-6 group can be noncyclic. The direct group-orbit argument below closes the reference/scope gap. |
| General stabilizer displacement and free Z2 cycle capacity | 0 / 0 / 0 / no | `2a+f=11`, `a≥1`, `f∈{1,3,5,7,9}`. |
| Free Z3 cycle capacity and equality structure | 0 / 0 / 0 / no | `3a+f=11`, `(a,f)=(2,5)` or `(3,2)`; if `a=2`, both base cycles saturate every orbit with complementary internal types. |
| Free Z4 cycle capacity before imposing T2 | 0 / 0 / 0 / no | `4a+2b+c=11`, `a∈{1,2}`, `c` odd; this is separate from the T2 exclusion. |
| Unrestricted existence and realizability of residual cases | 0 / 0 / 0 / yes | Not proved or disproved by the packets or by this review. |
| Review process: native clock before first control-script write | 0 / 0 / 1 / no | First control script was created without an earlier independently sampled native clock; execution and review clocks were sampled as detailed below. No creation time is asserted. |

## Independent written reconstruction

### 1. Cuts, coincidences, and automorphisms

A directed Hamiltonian decomposition of the 12-vertex complete loopless digraph has 11 cycles. Remove a vertex `u` from each cycle. The resulting 11 rows are permutations of the other 11 vertices, and their adjacent pairs are exactly the 110 ordered pairs avoiding `u`, once each. Conversely, in a T1(11) array all 110 ordered pairs occur once. Each symbol has ten incoming and ten outgoing events among its eleven row occurrences, so it starts exactly one row and ends exactly one. Adjoining `u` before the start and after the end of every row therefore recovers all 22 arcs incident with `u` exactly once as well as the other arcs. This gives the claimed decomposition–cut correspondence.

A cyclic two-step event `(x,y,z)` has distinct vertices. Two different events with the same ordered endpoints cannot have the same middle: the arc `x→y` has a unique successor in its unique decomposition cycle. Thus two coincident events have exactly the four vertices `{x,y,y',z}`. The event survives the cut at `v` exactly when `v` is none of its three vertices.

Let a free cyclic subgroup preserve the decomposition and let `O` be the orbit of `u`. All cuts at vertices of `O` are isomorphic. If the cut at `u` is T2, so are those at every `v∈O`; therefore no such `v` can be omitted from both of two coincident triples, i.e. `O⊆{x,y,y',z}`. Conversely, this containment for every coincidence prevents a repeated distance-two pair at the particular cut `u`. Both directions are necessary: cyclic 2-perfection is not assumed.

For an arbitrary T2(11) cut, an automorphism fixing `u` permutes the other vertices and preserves the cut row set. The expressly adopted f175 Theorem A makes that symbol automorphism trivial, hence it fixes all 12 vertices. Therefore every nonidentity decomposition automorphism acts without fixed vertices, and every subgroup action is free. This application uses the adopted theorem, not the linked proof or finite checks in its disposition.

### 2. Actual cycle orbits and exact compatibility

Write the free action as `(t,a)↦(t+1,a)` on `Z_q×{0,…,r−1}`, `qr=12`, with `O=Z_q×{0}`. The type of an ordered pair `((t,a),(t+d,b))` is `(a,b,d)`, excluding `(a,a,0)`. It is exactly one orbit of `q` actual ordered pairs; there are `132/q` types. For a middle `(t+h,c)`, its aligned middle is `(h,c)`. Translation fixes both the type and aligned middle, while different aligned middles give different actual triples over each given endpoint pair.

For a cycle `C`, its stabilizer `K` embeds faithfully in the cyclic rotation group of the 12-cycle: a rotation fixing one vertex is the identity. If `s=|K|`, the rotation subgroup is generated by an advance of `L=12/s` positions. There is a corresponding `k∈K` with `x_{j+L}=k x_j`. The first `L` vertices are representatives of distinct `K`-orbits. Conversely, extending any such list with that shift produces an actual Hamiltonian cycle; when applying the reduction, `K` and `L` must be the cycle's actual stabilizer and period. A cycle described more than once is not selected more than once.

For each selected orbit, the first `L` arcs supply its representative D1 types. Each representative arc has `q` translates, distributed among the `q/s` actual cycles, and these translates exhaust its pair type. A repeated type within or between selected representatives means an actual repeated arc after a suitable translation; no repetition means the translated arcs are disjoint. Therefore the representative D1 types partition all `132/q` types if and only if the expanded actual cycles cover each directed arc once. In particular, this partition also yields the correct number of cycles, since `sum L=132/q` implies `sum(q/s)=11`.

Under D1 exactness, the same D2 type and same aligned middle cannot occur twice: translating both occurrences onto the same endpoints and middle repeats the same directed first arc. For every pair of distinct aligned middles of one type `(a,b,d)`, the cut criterion becomes

`O ⊆ {(0,a),(d,b),m,m'}`.

Translation preserves `O`, so this is exactly the four-vertex condition for all corresponding actual coincident pairs. It must be checked for every pair of middles, including pairs produced within one cycle orbit and across different orbits. Conversely, the D1 partition makes a genuine decomposition and the compatibility condition makes its cut T2. Types with zero, one, or more compatible D2 occurrences are all allowed. The reduction neither assumes a D2 type partition nor discards the actual cycles or their cut position.

### 3. Z2 collision restrictions and excess

Let `O={u,v}`. If both endpoints of a repeated pair are outside `O`, compatibility forces its two distinct middles to be exactly `u,v`; a third middle would make a pair of triples missing one of `u,v`. If two such repeated pairs shared a source but had different targets, the single arc `x→u` would have two successors; sharing a target but having different sources would give the single arc `u→z` two predecessors. Thus these repeated actual ordered pairs form a directed partial matching on ten outside vertices. There are at most ten pairs, or five free Z2 pair types.

If exactly one endpoint is in `O`, any repeated pair must have the other orbit point as a middle, and there can be at most one other middle. For a repeated type starting in `O`, fix its source to `u` by translation: the unique successor of `u→v` fixes the outside target. Thus at most one such type starts in `O`; the unique predecessor of `u→v` gives at most one ending in `O`. If both endpoints lie in `O`, there is one directed pair type, with at most ten distinct outside middles.

For each of the 66 pair types let `μ` be its multiplicity. There are 132 actual cyclic events, so `sum μ=66`. Consequently `D=sum max(μ−1,0)` is also the number of absent types. The four categories give `D≤5+1+1+9=16`. Each type has two actual pairs, so both the cyclic excess and number of missing actual pairs equal `2D≤32`. These are necessary restrictions, not a construction or an exclusion of Z2.

### 4. Z3 collision restrictions and excess

For any three-point vertex orbit, an all-orbit triple has the form `(x,g^a x,g^{2a}x)` with `a=1` or `2`. Its translate by `g^a` contains the same directed second arc, now followed by `x`. Unique predecessor and successor in the decomposition then force a directed 3-cycle, impossible inside a Hamiltonian 12-cycle. Thus no such triple occurs, and this reasoning applies to every three-point orbit, not just `O`.

In a coincidence, neither endpoint being in `O` leaves only two middles to cover three orbit vertices. Both endpoints in `O` require the remaining point as a middle, creating a forbidden all-`O` triple. Exactly one endpoint is therefore in `O`, and the two middles are the two remaining orbit vertices. A third middle would form a pair omitting an orbit point, so the multiplicity is exactly two.

Fix a repeated pair from `x∈O` to an outside target. Both within-orbit first arcs from `x` must have that same target as their successor, so there is at most one target for fixed `x`; translation identifies the three sources. Hence at most one repeated type is directed out of `O`. The predecessor argument yields at most one directed into `O`. Each repeated type contributes exactly three excess actual events. Since total cyclic events and possible ordered pairs are both 132, excess equals the number of missing pairs and is `0`, `3`, or `6`. Thus at least 126 distinct cyclic distance-two pairs occur. Nothing in this argument asserts that any of the three values is realizable.

### 5. Z4 forces 2-perfection

A coincidence has four distinct vertices and must contain all four points of `O`, so its vertices are exactly `O`. Identify them with `Z4`, set the first endpoint to `0`, and write its second endpoint `d`. The two middles are the remaining two points. Translating the required triples through all four group elements and using unique successors of actual arcs gives these forced transitions of nonzero step types:

| `d` | Two triples based at 0 | Forced step transitions |
|---:|---|---|
| 1 | `(0,2,1)`, `(0,3,1)` | `2→3`, `3→2` |
| 2 | `(0,1,2)`, `(0,3,2)` | `1→1`, `3→3` |
| 3 | `(0,1,3)`, `(0,2,3)` | `1→2`, `2→1` |

In each row, every translated arc of either named step type has its next arc forced to another named step type, still entirely inside the four vertices of `O`. Starting at any such arc, its unique cycle cannot leave `O`; a finite four-vertex walk must repeat before visiting all 12 vertices. This contradicts Hamiltonicity. Hence no coincidence exists. The 132 cyclic two-step events have 132 distinct ordered endpoints among 132 possibilities, giving a 2-perfect decomposition.

### 6. Even cyclic symmetry and the jump-sum obstruction

For a free `C_q` action on `m=qr≥3` vertices, with even `q` and odd `r`, use the same pair types and actual cycle-orbit periods `L=m/s`. D1 and D2 exactness in a 2-perfect decomposition make both representative type collections the complete pair-type set. For a period of one representative let `δ_j` be the first-coordinate increment of its `j`th arc. Its stabilizer shift is a fixed group translation, hence `δ_{j+L}=δ_j`. The distance-two increment at `j` is `δ_j+δ_{j+1}`. Summing cyclically over one period and then all cycle-orbit representatives gives `S=2S (mod q)`, where `S` is the sum of increments of all pair types.

The excluded diagonal types have increment zero, so

`S = r² sum_{d=0}^{q−1} d = r² q(q−1)/2 ≡ q/2 (mod q)`.

The last equality uses even `q` and odd `r`. Thus `S` is nonzero, whereas `2S=0`, contradicting `S=2S`. The periodic last-to-first term is essential. For `q=4,r=3`, this obstruction contradicts the 2-perfection forced in the preceding section, excluding every free Z4-invariant circular extension with a T2 cut. It does not use any search result.

### 7. Full automorphism order and the order-6 reference repair

By semiregularity, the full group order divides 12. A subgroup `Z2×Z2` cannot act on the 11 Hamiltonian cycles: a cycle stabilizer embeds in its cyclic rotation group, so it cannot be the whole Klein group. Every cycle orbit under the subgroup has size 2 or 4, and such sizes cannot sum to 11. A cyclic subgroup of order 4 is excluded above. If the group order were divisible by 4, Sylow's theorem gives a subgroup of order 4, necessarily cyclic or Klein; both possibilities are excluded. The remaining divisors of 12 are `{1,2,3,6}`.

**Minor scope/reference finding.** The packet then says its criterion (1) forces 2-perfection when the full group has order 6. But (1) was stated with `O` the orbit of a cyclic group of order `2`, `3`, or `4`; an order-6 group may be noncyclic. The conclusion is nevertheless correct by the same direct argument at the necessary generality: choose the full automorphism-group orbit of `u`. Semiregularity makes this orbit contain six vertices, and invariance makes each of its cuts T2. Any coincidence would have to contain all six vertices, but has exactly four. Hence there are no coincidences and the decomposition is 2-perfect. This supplies the missing scope extension; it does not exclude any order-6 group.

### 8. Independent reconstruction of cycle-capacity addendum

If an element `h` of order `s` stabilizes a directed 12-cycle, its action on that cycle is a faithful rotation of order `s`, hence its displacement is `k·12/s` with `gcd(k,s)=1`. For `s=2` this is 6; for `s=3` it is 4 or 8. In particular `x→hx` cannot be a cycle arc. This is a statement about the actual permutation cycle, not an abstract count of types.

For free Z2 there are six point-orbits. Every arc `x→gx` must occur in the decomposition, but cannot occur in a `g`-fixed cycle, so at least one orbit of two cycles is present. Writing its count as `a` and the fixed-cycle count as `f` gives `2a+f=11`, `a≥1`, and the listed odd possibilities `f=1,3,5,7,9`.

For free Z3 there are four point-orbits and two internal directed arc types in each, hence eight internal types in total. A fixed cycle contains no internal arc, because the relevant rotation displacement is 4 or 8. A non-fixed cycle contains at most one internal arc in each three-point orbit: two distinct internal arcs either share a tail or a head, form an impossible directed 2-cycle, or form a prohibited three-consecutive-vertex path through the orbit. The full orbit of that actual cycle covers the complete type of each such arc and therefore at most four internal types. At least two free cycle-orbits are needed. Since `3a+f=11`, only `(a,f)=(2,5)` and `(3,2)` remain. When `a=2`, their combined capacity is exactly eight, so each base cycle has one internal arc in each of the four orbits, and uniqueness of D1 arcs makes their two types complementary in every orbit.

For free Z4, `g²` is an involution. A cycle stabilized by it has `x` and `g²x` six positions apart and cannot contain `x→g²x`; such arcs must nevertheless be covered. Every nontrivial subgroup of Z4 contains `g²`, so a cycle containing one of those arcs has trivial Z4 stabilizer and lies in a four-cycle orbit. If `a,b,c` count cycle orbits of sizes 4, 2, 1, respectively, then `4a+2b+c=11`, `a≥1`, hence `a∈{1,2}` and `c` is odd. This is a necessary pre-T2 capacity constraint; the separate written Z4 exclusion applies after imposing T2.

## Independent bounded controls and receipts

These scripts were written independently in this wave directory; they do not read, run, import, or compile author code. They are finite diagnostics, not a formal proof and not an order-12 global decomposition enumeration. The subprocess runner imposed a 115-second cap per run; neither cap was reached. Clocks below are direct `/bin/date` observations, not creation-time assertions.

1. `reviewer-control-v1.py`, SHA-256 `806863004aa7833036a15e9b4c313db82f652b38ae4ee174638943296712089b`; start **2026-10-29T13:17:43-0700 PDT**, end **2026-10-29T13:17:45-0700 PDT**, exit **0**.
   - For each of `q=2,3,4` at 12 vertices, independently enumerated all 5,940 endpoint/four-distinct-vertex coincidence candidates and compared orbit containment with the direct cuts. Compatible pair counts were 540, 108, and 12 respectively. Exhausting all middle subsets of each endpoint pair gave Z2 maximum repeated multiplicities 2, 2, 10 for zero, one, two endpoints in `O`; Z3, after excluding the explicitly forbidden all-orbit triples, had maximum 2 only for one endpoint in `O`; Z4 had maximum 2 only for two endpoints in `O`.
   - Intended-reason negative fixtures deliberately omit one orbit point for each `q` and exhibit the duplicate pair at that omitted cut: 3/3 detected. For Z3, all six ordered orbit triples give the translated-arc closure. For Z4, all three transition tables force four-point closure; removing one translated successor constraint produces an incomplete forced system, a 3/3 negative for using the full translation closure.
   - Independently enumerated the 15 pairs of internal arcs on three vertices: 6 share a tail or head, 3 form a 2-cycle, 6 are three-vertex paths. Checked the order-2 and order-3 fixed-cycle displacements, all listed nonnegative capacity equations, 6,604 periodic jump identities and 16 even-`q`/odd-`r` residue cases. The intended unwrapped-period negative `q=4`, increments `(1,0)` yields unwrapped sum 1 rather than the claimed periodic value 2.
   - Exhausted single Hamiltonian cycle orbits on smaller vertex sets: `n=8,q=2` had 2,544 orbits (1,488 D1-unique; 1,008 compatible and 480 incompatible); `n=9,q=3` had 13,464 (3,492 D1-unique; 576 compatible and 2,916 incompatible); `n=8,q=4` had 1,276 (188 D1-unique; 32 compatible and 156 incompatible). For each orbit the script compared type uniqueness with actual arc uniqueness, and for D1-unique cases compared local compatibility with the actual cuts. The first-180-orbit cross-orbit sample had **zero** D1-disjoint pairs for the first two settings, so that sample alone provides no cross-orbit evidence there; the separate control below addresses this. For the third it checked 260 D1-disjoint pairs, 16 compatible.
2. `reviewer-control-pairs-v1.py`, SHA-256 `6b3f85214904b213e8c39ead93a03ca1c190da0fb117f122f50eee2d5a541594`; start and end both **2026-10-29T13:18:13-0700 PDT** at the displayed clock resolution, exit **0**. It independently generated actual smaller cycle orbits, checked disjoint D1 type sets against concrete arc uniqueness, and compared all orbit cuts against merged aligned-middle compatibility. It stopped only after at least 25 positive and 25 intended negative D1-disjoint two-orbit families per setting: `n=8,q=2`, 25 positive / 122 negative after 754 candidate pairs scanned; `n=9,q=3`, 25 / 258 after 1,998; `n=8,q=4`, 25 / 331 after 14,303. This is a bounded witness sample, not an enumeration of every pair or a full decomposition search.

## Imports, limits, and deviations

**Imported premises:** the pinned disposition's expressly adopted definition of T1/T2 and Theorem A, used only to pass from an arbitrary T2(11) cut to semiregularity; elementary finite group/cycle/permutation facts and Sylow's theorem. The mathematical statements in the two target packets were reconstructed rather than imported. Neither linked f175 bodies nor other material mentioned in any packet supplied evidence. In particular, no author PASS/receipt, solver UNKNOWN, timeout, author program, floating search, web source, other model/API, sibling review, or held mathematical payload was used.

**Remaining gap:** the written exclusion concerns free Z4 only. The residual Z2/Z3 compatibility problems, possible order-6 2-perfect decompositions, and asymmetric decompositions are not resolved. This review supplies no T2(11) witness and no universal nonexistence proof.

**Process deviation:** I created and made a small pre-run correction to `reviewer-control-v1.py` before independently observing a native `/bin/date` clock. The first subsequently observed clock for that script was the execution-start clock above; it is not a script-creation time. The second script was written after the first run's recorded end clock, and the review after the expressly recorded pre-review clock. This clock-recording lapse is counted as one minor process finding. There were no input-hash mismatches, incomplete source windows, pre-read mathematical controls, author-code executions, or control timeouts.

This is **same-harness review only**: it is not human review, independent-model-family review, formal/kernel verification, or novelty/priority verification.
