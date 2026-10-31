# F554: independent actual-cycle and directed-square necessary-interface check

## Disposition and exact scope

**WRITTEN CONDITIONAL NECESSITIES SUPPORTED; INDEPENDENT FINITE SOURCE RETURNED, NOT RUN.** No actual eleven-row T2(11), complete exclusion of either T=13 or T=14, unrestricted nonexistence result, universal M=C, novelty, independent-family/human review, source equivalence, or kernel proof is claimed.

Mathematical findings against the supplied f489 candidate at its stated scope: **0 FATAL, 0 MAJOR, 0 MINOR identified.** This is not a finite-run PASS. The source below is unexecuted and could contain implementation defects; its prospective assertions and expected counts are not observed output.

Complete companion source: `local://f554-independent-finite-v1.py` (30,704 bytes reported by the write tool). Intended repository basename, if Main materializes it, is `f554-independent-finite-v1.py`. This body and the source are return artifacts, not repository changes. No attempt to bypass the repository read-only restriction was made.

The actual target is eleven permutation rows on the same eleven finite symbols. Every one of the 110 original directed linear adjacency events must occur once, and all 99 original directed linear distance-two events must be distinct. The conditional branch additionally assumes that the missing distance-two set M equals the actual last-to-first closing set C, and that distinct six-symbol odd-position supports B,D each occur three times. The accepted S2 interface supplies |B intersection D|=3 and its local T=13/14 table. Other tripled supports are not assumed absent.

The phrase “eleven distinct vertices” must refer to the eleven FINITE symbols of a row. The cycle used throughout the proof and checker is the augmented TWELVE-vertex cycle `(infinity,r1,...,r11)`. Squaring an eleven-cycle instead would introduce the wrong wrap events.

## 1. Read and method chronology

Before reading scientific bodies, I read the complete manifest, freeze receipt, dispatch receipt, parent-live-metadata supply, and all twelve listed permission/status controls, through their endings, with raw reads of at most twenty lines for the control traversal. A direct `agent://Main` PREBODY ACK was delivered before opening the literal packet. I subsequently read the complete packet in the ordered raw ranges 1–20, 21–40, ..., 561–580, 581–581, through S1 label543 and S2 label36. All derivation/source preparation followed that completed packet read.

Pinned metadata, attributed to the parent supply rather than a child-native hash calculation:

- manifest SHA256: `fdabbd8793a08655d65f14ab9d56cea52e0fb8b038197062ca15fdc8a542911c`;
- freeze-receipt SHA256: `aa80e29ea9e9ede3512c11845f2d98b69bb3c56a5aff6631edd7a74cbd60fa52`;
- literal-packet SHA256: `0493ce335c269f1b1b3e9cd445215b694af549bb03ff69cc1be667719a335f83`;
- S1: f489 `review-v1.md`, complete labels1–543, SHA256 `16940c11f15e2f931070ab94e0ee1e108ad1dfe2ec5bfe1c0effd5e7ea0eee83`;
- S2: `info-4-actual-tuscan11-overlap-budget-and-conditional-tripled-support-joint-cuts-parent-v1.md`, complete labels1–36, SHA256 `c82b00df7bb8fc2d3a8eb9cc3e2b841f4464314d6b471586c4a833e846c30c60`.

The supplied source metadata counts 542 LF characters for S1, while the packet displays labels through543; the coverage statement concerns those displayed labels, including the ending. I did not run a native clock, hash/reconstruction command, scientific executable, solver, CAS, build, test, linter, formatter, external-model CLI, or external source lookup. No linked earlier wave/code/report was followed. Held scientific episodes and all excluded consumers were not opened or imported.

This is a FINITE author-source duty. Source preparation includes fresh unexecuted fixture construction and a complete bounded cell-word enumeration, not a claim that only previously written code was copied. The written numerical example checks in Section7 concern the input's four explicitly displayed rows. No fresh private instance or unexecuted generated fixture is offered as evidence for a mathematical conclusion. These statements describe actual read/use and output boundaries, not cognitive isolation.

The runtime role permits returning source but forbids executing it. Therefore the independent finite program, every program control, its internal deadline, and its output are **NOT RUN / UNOBSERVED**. The literal prospective argv is:

`python3 -B -I f554-independent-finite-v1.py`

No elapsed-time or successful process-exit claim is made. The parent clock recorded in the metadata is a parent observation, not my observation.

## 2. Actual row-to-consumer boundary: where M=C is indispensable

Put X=S union {infinity}, |S|=11. An actual row r gives the single directed Hamilton cycle h=(infinity,r1,...,r11). The consumer is a directed successor map on the SAME twelve actual vertices, not an arbitrary permutation cover and not a cell word by itself.

Adjacency exhaustion implies each finite symbol occurs first and last exactly once: the number of outgoing original adjacency occurrences of x is 11 minus its last-column multiplicity and must equal ten; the incoming calculation is dual. Thus the eleven h cycles partition all 132 directed nonloop arcs on X.

For one row the finite arcs of h squared are EXACTLY the nine original events `(ri,r(i+2))`, i=1,...,9, together with `(r11,r1)`. Its two remaining square arcs are `(infinity,r2)` and `(r10,infinity)`. In particular, neither `(r10,r1)` nor `(r11,r2)` is a finite wrap event of this augmented square.

Across rows, M=C makes the 99 original distance-two arcs and eleven closing arcs a partition of the 110 finite ordered pairs. The number of missing outgoing distance-two arcs at x equals its penultimate-column multiplicity; the missing incoming count equals its second-column multiplicity. C has indegree and outdegree one, by first/last exhaustion, so M=C makes the second and penultimate columns permutations as well. The infinity square arcs consequently partition the remaining 22 arcs. This establishes the complete 132-arc square decomposition conditionally on M=C.

A square of a twelve-cycle has two derived six-cycle orbits. That is legitimate: Hamiltonicity is required of h, not of h squared. It is not legitimate to admit three four-cycles as h because they have the same local cell word. The returned checker has separate dispatch/validation for the actual Hamilton successor and its derived square successor.

No step imports this square partition when only original adjacency/distance-two injectivity is known. In the supplied S1 this boundary is explicit at labels71–91 and is consumed in labels191–207 and363 onward.

## 3. Reconstructing the local interface from the same cycles

Write I=B intersection D, J=B minus D, K=D minus B, L=X minus (B union D), with membership bits I=11,J=10,K=01,L=00. Each augmented cell has size three; the finite multiplicities are (3,3,3,2), with infinity in L.

For a six-cut A, the accepted finite-singleton identity plus M=C gives a total augmented singleton count36. Each A-alternating Hamilton cycle contributes12, so the three cycles with support A exhaust this count. Every other actual cycle therefore has no singleton for that cut. The three B-alternating and three D-alternating cycles are disjoint because a connected even cycle has a unique alternating bipartition up to complement. The five remaining actual cycles R have no singleton for either bit.

Let T be the sum of the other-cut run counts over the six alternating-family cycles. For a cell Q, let g,p,q count, across these same five residual cycles, layouts F=(one length3 run), P=(one length2 plus one singleton), Q=(three singleton runs). All six internal directed adjacency arcs of the cell occur in R, so

`g+p+q=5`, and `2g+p=6`.

A residual internal square arc cannot have a middle vertex outside its endpoint cell: such a middle vertex would be a singleton for a changed bit. Hence it comes from exactly one full length3 cell run. In a B-alternating cycle with j D-runs, each relevant D-color run contains both constituent cells and alternates their vertices. With three vertices in a cell, the number of its internal square arcs is 3−j; the D-family argument is symmetric. The square decomposition therefore gives

`6 = (18−T) + g`, so `g=T−12`, `p=30−2T`, `q=T−13`.

Nonnegativity gives g=1,2,3. The case g=3 would partition all six directed arcs on three vertices into three length2 directed Hamilton paths. Each vertex would start and end once. Fix one path a,b,c. The path starting b must end c (it cannot end a, since b,c,a repeats b→c), hence it is b,a,c; the two unused arcs both start c, not a path. Thus g=3 is impossible. The exact local alternatives are T13:(F,P,Q)=(1,4,0) and T14:(2,2,1), uniformly in all four cells.

This reconstructs the relevant S2 table; it does not re-audit the unrelated unconditional overlap minimum table in S2 labels7–13.

## 4. Joint Hamilton and diagonal constraints

A diagonal adjacency joins I,L or J,K and changes both bits. At either endpoint, avoiding a singleton in both bits forces the other neighbor into the endpoint's own cell. Therefore diagonal endpoints belong to nontrivial runs. A size3 cell has at most one nontrivial run in a cycle. Two joins between the same opposite-cell pair would close those two runs into a component containing at most six vertices, contradicting the actual twelve-vertex Hamilton cycle. Thus each residual cycle has capacity one for each opposite pair.

In a B-alternating cycle let x,y count I→L,L→I. Cell indegree/outdegree balance gives J→K=x and K→J=y, and x+y equals the other-cut run count j. In a D-alternating cycle the corresponding J,K directions are reversed. Thus either undirected opposite pair receives T adjacency occurrences from the six alternating cycles. Of its eighteen possible directed arcs, exactly 18−T must occur across R.

For T13, demand5 equals total capacity5. Every residual cycle has exactly one join of each opposite kind. For T14, demand4. If the unique all-singleton slots of I and L differed, at most three slots could join I,L, impossible. They therefore coincide; likewise J,K. In a cycle where both I,L are all-singleton, all six vertices of I union L have neighbors in J union K, accounting for all twelve edges. It alternates across E=J union K. Diagonal neighbors are absent, so J,K are all-singleton there too. All four unique all-singleton layouts therefore occupy one common actual Hamilton cycle hE. The other four residual cycles each have both diagonal joins.

At hE each cell singleton must change different bits on its two incident edges. This fixes one of the two cyclic orientations I–J–L–K–I, repeated three times on the cell projection, while hE itself remains connected on twelve distinct vertices. The finite odd support is E because infinity belongs to L. Every other residual cycle has E-preserving diagonals; the B,D families cannot have this distinct alternating cut. Hence kE=0 for T13 and kE=1 for T14, exactly as claimed, not just kE≤1.

For a regular residual cycle, joining the nontrivial runs across each diagonal creates one I/L block and one J/K block. Every remaining cell-singleton vertex has both edges crossing E. The two gaps between opposite-E blocks therefore have even length and equal numbers of singleton vertices on the two E sides. If f is the number of full cells, this gives

`#full in {I,L} = #full in {J,K}`.

The allowed full-cell sets are empty, all four cells, or one of the four edges IJ,JL,LK,KI. In particular, f is0,2,4, and a size2 full set is adjacent, not opposite. There are 4−f cell-singleton vertices, E adjacency-cross count6−f, E-singleton count4−f, and E square-cross count4 in such a cycle. The last equality also follows from the cyclic identity `square-cross=2*adjacency-cross−2*singleton`.

Summing full-cell incidence gives precisely:

- T13: full-count sequences `(4,0,0,0,0)` or `(2,2,0,0,0)`. In the second case the size2 sets are complementary edges.
- T14 outside hE: `(4,4,0,0)`, `(4,2,2,0)`, or `(2,2,2,2)`. The middle case again uses complementary edges. In the last case the four cell-square edge multiplicities are `(x,2−x,x,2−x)`, x=0,1,2.

These prove restrictions on simultaneous same-cycle layouts, not sufficiency for any labeled five-cycle collection.

## 5. Exact directed-square orientation bounds and normalization

Let x,y count I→L,L→I over the B family, and u,v the same directions over the D family. Then x+y+u+v=T. Their directed residual adjacency counts are

`aIL=9−x−u`, `aLI=9−y−v`, `aJK=9−x−v`, `aKJ=9−y−u`.

Neither alternating family contributes opposite-cell square arcs, because its square preserves its own bit. All nine square arcs in each directed opposite-cell direction must be residual. A residual diagonal square event has exactly one of two forms: it uses a diagonal adjacency with an internal edge before/after, or it is centered at a singleton cell vertex with its two bit changes different. Every diagonal adjacency contributes two square events of its own direction.

For T13 this gives `9=2a+z` in either direction, with a+a'=5 and nonnegative z,z'. Consequently a,a' lie in[1,4]. For T14, hE already contributes three square arcs in each directed opposite-cell direction, so regular cycles satisfy `6=2a+z`, a+a'=4, giving a,a' in[1,3]. This applies separately to both opposite pairs.

Therefore, for EACH of the four cross sums c in `{x+u,x+v,y+u,y+v}`, the exact common interval is

`T−8 ≤ c ≤ 8`.

Equivalently,

`2T−16 ≤ 2c ≤ 16`,

or

`max(x,y)+max(u,v) ≤ 8`,

or

`abs(x−y)+abs(u−v) ≤ 16−T`.

This states the requested 2T−16 form with its factor of two explicit. The supplied packet defines no separate undoubled cross quantity with lower bound2T−16; assigning that lower bound to c itself would not be the S1 inequality. The independent source checks equivalence of all four displayed normalizations rather than silently changing variables.

Each other-cut run number is1,2,3. If a three-cycle family has run sum9, each member has run number3; every other-cut run then has length2, forcing its I,L directional contribution to be (3,0) or(0,3). Its family maximum is at least6. For T14 the other family sums5, with directional maximum at least3. This contradicts the upper bound8. Thus the only T14 run-sum pairs are `(6,8),(7,7),(8,6)`. This excludes (9,5),(5,9), not the whole T14 branch.

If the six run numbers are1,1,3,3,3,3, both run-one members cannot be in the same family (that would give5+9). Each family therefore has multiset1,3,3 and sum7. Its directional totals must be3,4 in some order, since both maxima are at least4 and their sum is at most8.

For T13, a family summing9 is not excluded: the bound forces its directions3,6 and the other family's directions2,2. No contradiction is inferred.

## 6. Vertex bookkeeping consumes the SAME five physical cycles

Fix a vertex z in a cell. Across R it has exactly two internal incoming and two internal outgoing adjacency events, because all six cell-internal directed arcs are used once. A vertex has both neighbors internal exactly when it is the middle of a full length3 run. If m(z) counts those middle occurrences, inclusion-exclusion makes the number of occurrences with at least one internal neighbor `2+2−m(z)`. There are five occurrences total, so its cell-singleton count is exactly `1+m(z)`.

For T14, hE contributes one singleton occurrence for every vertex. On the SAME four regular cycles the singleton count is consequently m(z). Neither cell-total equality nor ledger values computed from a relabeled/different cycle collection suffice for this vertexwise identity.

The returned source calculates internal arcs, middle positions and singleton positions directly from the actual cyclic rows; a binding check prevents mixing packets from different row collections. Its fresh T13/T14 fixture constructors partition the internal arcs only. They are not claimed to partition the global cross-cell adjacency or square arcs.

## 7. Written checks of the four source-explicit actual rows

Use I={1,2,3}, J={4,5,6}, K={7,8,9}, L={infinity,10,11}. The following numbers are written consequences of the input's displayed rows and cyclic cell words; they are NOT machine output. The directed vector order is IL,LI,JK,KJ. All four augmented rows have twelve distinct vertices, hence are actual Hamilton cycles.

| Source row | Full-cell count | Diagonal adjacency vector | Diagonal square vector | E adjacency-cross | E singletons | E square-cross |
|---|---:|---|---|---:|---:|---:|
| `(10,11,1,2,3,4,5,6,7,8,9)` |4| (0,1,1,0) | (0,2,2,0) |2|0|4|
| `(10,1,2,3,7,11,4,5,6,8,9)` |2| (0,1,1,0) | (1,2,2,1) |4|2|4|
| `(10,4,3,7,11,5,6,8,9,1,2)` |0| (1,0,1,0) | (3,1,3,1) |6|4|4|
| `(4,1,7,10,5,2,8,11,6,3,9)` |0, all Q| (0,0,0,0) | (3,3,3,3) |12|12|0|

For the f4 row the full-run middle vertices are2,5,8,10; there are no cell-singletons. For f2 the middle vertices are2,5 and the cell-singletons7,11. For f0 there are no full-run middles and the cell-singletons are3,4,7,11. In the hE row every vertex is cell-singleton. Every row has no B-singleton or D-singleton, directly from the displayed cyclic cell words.

These individual rows illustrate the cases and the directed middle/endpoint contributions. They do not form an eleven-row array, and their per-vertex counts must not be inserted into the five-cycle identity as though the internal arc partition had been established.

## 8. Complete prospective finite protocol; execution status NOT RUN

The full source attachment is self-contained, standard-library-only and deterministic. It reads no file, creates no subprocess, uses no network/randomness, and writes no evidence file. Its only normal I/O is final stdout. It enforces an internal cooperative55-second bound and exits unsuccessfully with FAILED_OR_INCOMPLETE on an invariant or deadline failure. No full9! or11! labeled permutation campaign, joint-array solver, or hidden background work is present.

The exact experiment domain and dispatch are:

1. Enumerate every cell word beginning at infinity in L, with remaining counts3,3,3,2: `11!/(3!3!3!2!)=92,400` words. Lift each to an actual eleven-finite-symbol permutation. Build and validate the connected twelve-vertex successor, its actual directed arcs and its square FIRST; only then project to cell metrics. One deterministic lift represents a cell word, not all labeled cycles.
2. On rows with no B/D singleton, compute F/P/Q layouts, all directed diagonal adjacency and square counts, E directed cross counts, and E singleton counts from these same actual cyclic rows. Check diagonal capacity, internal-square/full-run identity, and directed centered-singleton identity.
3. Collect physical layout signatures and all regular full-cell masks. Enumerate q-slot assignments over exactly5^4=625 possibilities. The opposite-pair capacity restriction leaves25; requiring the q-masks actually present on no-B/D-singleton Hamilton words leaves5, namely a single common slot. These are prospective assertions, not observed counts.
4. Enumerate regular full-mask schedules from the masks arising in the physical-word domain. This is a necessary projection: it does NOT enforce cross-row vertex arc compatibility.
5. Collect actual B-alternating and D-alternating physical row types with no other-cut singleton; enumerate triples of those types to check the exact orientation/cross-bound equivalences and surviving family run-sum pairs. A product of row types is not a compatible alternating family.
6. Independently enumerate all216 ordered triples of three-vertex directed Hamilton paths for the no-three-path-cover lemma.
7. Construct small physical five-row internal-arc fixtures for the vertex ledger. Validate the full vertex conditions from those rows and deliberately mix a foreign relabeled middle ledger only as a negative control. Their global cross-cell arcs are expressly uncertified.

The prospective schedule counts can also be obtained by the following complete written counting, independently of any execution:

- T13: choose the one full-all slot in5 ways, or choose two slots and a complementary-edge matching: `C(5,2)*2*2=40`. Total45 ordered mask schedules.
- T14 regular slots: full-count4,4,0,0 gives6; full-count4,2,2,0 gives `4*3*2*2=48`; four size2 edges give6+24+6=36 for edge multiplicity parameter0,1,2. Total90. Choosing the hE position among five yields450 projected schedules.

These counts concern cell-incidence schedules only. No number counts realizable labeled five-cycle decompositions or actual T2(11) arrays.

### Intended-reason mutation coverage

**Every entry below is NOT RUN.** “Designed” is not “passed.” The program's prospective output distinguishes failure, lack of a physical fixture, interface-only discrimination and full intended-reason discrimination.

| Mutation | Physical/control construction and intended reason | Unpaid limitation |
|---|---|---|
| Admit a disconnected permutation cover as h | Split the supplied hE vertex sequence into three directed four-cycles. Degree-only mutant accepts; actual Hamilton consumer must reject DISCONNECTED_SUCCESSOR. | It is a negative input, never a witness. The legitimate square's two six-cycles remain allowed. |
| Reverse C² direction | Use backwards two-step arcs on supplied f2 row; independent linear-row event formula must reject C2_EVENT_SET. | NOT RUN. |
| Use eleven-cycle wrap instead of augmented wrap | Compare the wrong cyclic-eleven square against nine original events plus closing and infinity arcs; reject C2_EVENT_SET. | NOT RUN. |
| Give cells independent T14 all-singleton slots | Select individually valid Hamilton rows from physical signatures, locally meeting every F/P/Q column but lacking the required diagonal joins. Correct necessary-interface consumer rejects OPPOSITE_JOIN_BUDGET; per-cell-only mutant accepts. | If the intended physical fixture is absent, output NOTTESTED rather than claiming discrimination. No global decomposition claim. |
| Allow any even full-cell pair instead of E-side balance | The mask interface rejects the two opposite-pair masks6,9 with FULL_CELL_E_SIDE_BALANCE; an even-cardinality-only mutant accepts. | This is explicitly INTERFACE_ONLY. A physical regular-row mutant is NOTTESTED: such a row is exactly what the theorem rules out. |
| Drop M=C while importing the complete actual square partition | The full actual-array validator checks original events and M=C before importing the partition. | Scientific discrimination is explicitly NOTTESTED: no actual eleven-row T2(11) with M≠C is supplied. A flag-only/fake-ledger case is not counted. |
| Take vertex singletons and middles from different cycles | Two actual internal-arc-cover fixtures, related by within-cell relabeling, have separately valid ledgers. Mixing them must reject VERTEX_LEDGER_CYCLE_IDENTITY; cell-total-only checking misses the per-vertex mismatch. | NOT RUN. No arbitrary exception counts; the exact reason is required. |

There is no observed output, stdout/stderr file, native elapsed time, exit code, own-source hash, or successful control count to cite. Main must pin and inspect the returned source before deciding whether to execute it once under the already stated finite allowance. This return does not execute it or grant itself an execution exemption.

## 9. Consumer/scope audit and exact unpaid scientific step

The critical consuming boundaries have been read in the complete packet and reconstructed above:

- original linear row -> augmented Hamilton successor: requires all eleven distinct finite vertices and one connected twelve-cycle;
- actual h -> h squared: preserves direction and uses the augmented wrap, not an eleven-cycle wrap;
- M=C -> complete square decomposition: retains its conditional guard;
- all six alternating families -> residual internal-square count: same vertices, same arc universe, not separate shadow ledgers;
- per-cell F/P/Q -> diagonal capacity/synchronization: enforced on the same five cycles;
- directed square counts -> orientation ledger: direction and family-specific J/K reversal retained;
- cell-internal adjacency partition -> per-vertex singles/middles: both ledgers consume the identical actual row collection;
- physical row types -> mask/type schedules: output labeled NECESSARY ONLY, never promoted to a labeled compatible array.

The first unproved scientific step is still simultaneous LABELED Hamilton-and-square compatibility. One must either construct eleven actual augmented Hamilton cycles partitioning all132 adjacency arcs and all132 square arcs, with the stipulated two three-cycle alternating families, or exclude every such collection in the remaining templates. For T13 both full-count patterns remain; for T14 the three regular full-count patterns with one hE and family run-sum allocations6+8,7+7,8+6 remain. Cell-word support, mask schedule counts, physical single-row examples, and internal-arc-only fixtures do not close this gap.

For the unrestricted original problem, M≠C branches, a single tripled support, and multiplicity-at-most-two cases remain outside this conditional result. No new public source was consulted; the supplied paper link is not re-certified, and no present-literature or priority claim follows.

**Overall mathematical assessment:** the stated f489 conditional necessities are supported by written reconstruction, with no identified F/M/m defect. **Independent finite verification:** NOT RUN, source supplied in full. **Original-target status:** NOT PROVED.
