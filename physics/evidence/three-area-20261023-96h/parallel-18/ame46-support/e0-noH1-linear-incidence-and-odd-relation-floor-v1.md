# e0/no-Hamming1 support dichotomy: an EXPLICIT3-row odd certificate OR linear block incidence with at least SEVEN odd coefficient blocks

Owner PhysicsAME46-2 / physics-6. Actual `/bin/date` immediately before this NEW write: **Mon Oct 26 08:22:42 PDT 2026**. Precreation observation only.

**NEW COMPLETE WRITTEN SUPPORT/INTEGER-RELATION THEOREM CANDIDATE, UNREVIEWED.** This is a uniform geometric dichotomy for simultaneous e0 support predicates, followed by an exact necessary classification of the SMALLEST surviving odd-integer-relation incidence pattern. It does NOT produce an odd integer relation in the remaining linear class, prove GLOBAL-ODD, assert phase feasibility, construct a tensor or settle support48/50/minimum. No mod2 condition is promoted to an integer certificate.

## 0. Original-primary order and immutable sources

Current work follows actualv121FRETURN and the separately WRITTEN/SENT07:12:45whole-primaryACK before source/reasoning, SHA256 `2905623b9bcb3a543d84bbc914324d12b712d0efadcf3e6fc880e14d5b54e835`. The new complete dichotomy/floor was saved in checkpoint58 at08:21:28. All old GLOBAL-ODD/support48/support49/excess and current core/surgery leads remain exposed, not reclassified as future-gate preregistration.

The earlier100LF `e0-six-site-three-rectangle-odd-relation-v1.md`, SHA256 `ff0b111cc462c997e5afdc1a69f33bdb7e9063155133e1a2350ee4b5fd4da4ae`, is an immutable UNREVIEWED predecessor. Its exact local certificate is reproduced below rather than implicitly adopted. No historical I48/J49/lower48/native theorem, component catalogue or computational phase result is a premise of this source.

## 1. EXACT support input, no hypothetical state silently assumed

Let T,N be a literal flagged support on physical product-basis coordinates, satisfying the simultaneous e0 support predicate:

- each physical pair line has either ONE T site and ZERO N, or ZERO T and EXACTLY TWO N;
- in EACH of the THREE complementary cuts the N graph is a disjoint union of actual K2,2 blocks on the SAME N sites;
- no TWO N sites differ in just ONE physical coordinate.

The predicate does NOT assert that phases/amplitudes realizing an AME tensor exist. Every hypothetical actual e0/no-Hamming1 AME support satisfies it, but the theorem can examine a support before assigning phases.

Index N globally. Give every block its checkerboard integer row with plus on one diagonal and minus on the other; B is the resulting three-cut phase matrix. Each row has four±1 entries and each site column belongs to EXACTLY THREE block rows, one per cut. Complex phase realizability would require `B*theta=pi*1 mod2pi`. Blocks within ONE cut are disjoint.

**Theorem LI.** For every such literal support, EXACTLY one of these geometric cases occurs:

1. Two blocks from DIFFERENT cuts share at least TWO N sites. Then the support contains an EXPLICIT three-row odd-INTEGER certificate as in §2, ruling out every complex realization.
2. Every different-cut block pair intersects in at most ONE site. The three-cut incidence is LINEAR. For ANY exact integer z with `B^Tz=0` and ODD sum, the number b of ODD entries of z is at least7. If b=7, the odd-block incidence graph is EXACTLY the graph in §4, with cut class sizes3,2,2 and fourteen selected N sites.

Case2 permits the possibility of NO odd integer relation and does NOT establish feasibility or nonexistence. The two cases are a support partition, not a partition into known feasible/infeasible states.

## 2. Every NONLINEAR block intersection yields the literal three-rectangle odd certificate

No-Hamming1 implies the two physical row labels of ANY block differ in BOTH row-party coordinates: otherwise sites in one column would be Hamming1. The same holds for column labels. Therefore within a block an adjacent corner pair differs in exactly TWO physical coordinates, and an opposite-corner pair differs in ALL FOUR.

Take two sites shared by blocks from DIFFERENT cuts. They cannot be adjacent in one block: in another cut, adjacency would preserve a DIFFERENT coordinate pair and hence preserve at least THREE coordinates together, giving Hamming distance<=1; opposite corners would have distance4 instead of2. Both are impossible. Thus the two sites are opposite corners in BOTH blocks and differ in all four coordinates.

Relabel their actual values x=0000,y=1111 and name the two cuts12|34,13|24. Their blocks force

    u=0011,v=1100,s=0101,t=1010,
    R12=[[x,u],[v,y]], R13=[[x,s],[t,y]].

In cut14|23, the four u,s,t,v already give two nonzeros in each selected row and column. The support predicate's exact-two lines therefore makes the third block ACTUAL:

    R14=[[u,s],[t,v]].

On columns(x,y,u,v,s,t), the signed rows are

    b12=(1,1,-1,-1,0,0),
    b13=(1,1,0,0,-1,-1),
    b14=(0,0,1,1,-1,-1).

The exact INTEGER relation is `b12-b13+b14=0`, with coefficient vector(1,-1,1) of ODD sum1. Extend it by0 on all other rows/sites. Reversing row orientation only reverses the corresponding coefficient; the sum remains odd because there are THREE nonzero±1 coefficients.

Consequently no complex phase solution can exist in case1. This is not a mod2 failure substituted for cancellation: each signed site coefficient cancels EXACTLY in Z. Alternatively the three row-orthogonality equations force simultaneously `u*bar(t)=s*bar(v)` and its negative, a contradiction for six nonzero entries. All literal positions, cuts and cross terms are retained.

Thus any phase-realizable support in the no-Hamming1 class must have LINEAR different-cut block incidence. This is stronger than merely prohibiting a repeated diagonal mate at one vertex.

## 3. EXACT integer relation implies a SIMPLE4-regular tripartite graph

Assume the incidence is linear and take ANY z in the INTEGER kernel of B^T with odd total. Mark precisely the block rows whose z coefficient is ODD. Let b be their number. Since the sum of integer coefficients is odd, b is ODD and nonzero.

At each N site there are exactly three incident block rows. Modulo2 all checkerboard signs become1. Exact cancellation in `B^Tz=0` therefore says the number of marked incident blocks is0 or2, never1 or3.

Make a graph with the b MARKED BLOCKS as vertices. Each site incident to TWO marked blocks is one edge between them. Its endpoints have different cut types because each site belongs to only one block per cut. Every marked block contains four DISTINCT sites, each yielding one such edge, so the graph is4-REGULAR. Linear incidence implies that two marked blocks share at most one site, so the graph is SIMPLE, without parallel edges or loops. Its cut types give a proper TRIPARTITION.

This construction uses the parity of an ALREADY EXACT integer relation, only in the necessary direction. It does NOT conclude that an even-incidence marked set lifts to an integer z. Unmarked/even-coefficient rows may themselves have NONZERO even coefficients in the original relation; they are not deleted from the integer problem by this graph construction.

If marked blocks occupied just TWO cuts, the4-regular bipartite graph would have equal class sizes (count its edges from both sides), making b EVEN. Thus an ODD relation must use ALL THREE cut classes in its odd-coefficient set.

## 4. Sharp smallest possible odd count and its COMPLETE seven-vertex incidence

A simple4-regular graph requires at least5 vertices; hence b=1,3 are impossible. For b=5, any nonempty cut class has size at most b-4=1, because a vertex needs FOUR neighbours OUTSIDE its own class. Three such classes cannot contain5 vertices. Thus b5 is impossible too, proving

    b>=7.                                              (Floor)

At b7 each cut class has size at most3 and all three are nonempty. Up to permutation the only partitions are3,3,1 or3,2,2.

For a general tripartite4-regular graph with class sizes a,b,c, edge counting gives

    E_AB=2(a+b-c), E_AC=2(a+c-b), E_BC=2(b+c-a).

At3,3,1 this would require E_AB=10 edges between two3-sets, exceeding the simple capacity9. Thus the ONLY seven-vertex partition is3,2,2.

Every vertex in the3-class has exactly FOUR outside vertices available, so it is adjacent to ALL of them. These twelve edges form K3,4. Each vertex in the two2-classes then has degree3 from the3-class and needs ONE further neighbour in the other2-class. Those TWO additional edges are a PERFECT MATCHING. This completely determines the uncoloured/cut-partition incidence type, with all physical site/phase data still to be supplied.

The graph has `4*7/2=14` edges, hence FOURTEEN distinct actual N sites incident to two odd blocks. At an exact50 E0 support those are14 of28 N sites. The seven odd blocks have cut multiplicities3,2,2; the other sites have0 odd incidents. This is an exact structural floor, not a numerical graph enumeration or an asserted realizable support.

## 5. What remains genuinely unproved

The smallest unexcluded ODD-relation candidate in a LINEAR no-Hamming1 support is therefore a seven-block3/2/2 structure on fourteen actual sites. Larger odd-block structures also remain. To turn any of them into an exclusion one must produce an ACTUAL integer z satisfying all signed B columns (including nonzero even coefficients if necessary), with the genuine global support/physical coordinate assignments; a mod2 incidence graph alone is insufficient.

Conversely, failure to find such a z or existence of the simple graph does not establish a complex phase solution. The same physical sites must satisfy every pair coverage, officer placement, exact2/K2 closure and signed integer condition. No arbitrary cubic/4-regular graph is promoted to an admissible quantum support.

GLOBAL-ODD on every remaining support, the no-doubled-fibre E0 class, the coupled six-fibre complementary slices, E4 A/A-transpose/twoD2 and the full support50/minimum/upper witness remain OPEN at their exact scopes. This local dichotomy/floor neither accepts I48+J49 numerically nor supplies a new18x24/21x28 support matrix/tensor. Numerical48..60 and all historical NOT_RECONSTRUCTED/NOT_REPLAYED assurance cuts remain unchanged.

## 6. Assurance and continuation

All specialized facts are proved here from the actual simultaneous support predicate, physical Hamming distances, the explicit six-site integer certificate and elementary finite graph/edge counting. No native replay, external classification, historical numerical bound, positive-part shortcut, phase alphabet, arbitrary mode alignment or parameter trial is an input. This is exact WRITTEN conventional mathematics, not a scientific interpreter/kernel/finite-witness run.

All old proof/ACK/checkpoint bytes remain, including the separate cp55 false quarter-row inference withdrawal, unconsumed here. Both old AME pre-ACK majors, v100-E written-exactness ZEROcredit, originalv107read-order/prospectivecorrection, FULL06:05:05..06:57:52cadence MAJOR, characterized unadmitted cells and all parent/owner/reviewer findings remain. No processPASS/retropreregistration/falseblind/global hidden-cognition/runtime/cadence census/execution-or-falsity-from-process inference.

No decimals/new numeric parameter trials/scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO; exact source-symbolic/fraction/integer-product writing only. ExclusiveOWN/immutable sources/noGit/deletion/publication. Own ENTIRE mathematical AND dependency/application gate needed, not formal/kernel/configured-family/human/executable/novelty acceptance. Same18/HOLD/October27sciencecutoff11:05:38/deadline12:35:38/substantiveactivecheckpoints<=30min. Incremental ACTIVE original research, NOT an early final-park or96-hour closeout.
