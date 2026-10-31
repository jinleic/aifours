## D1 [DEPENDENCY (input only where used)] /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-two-row-completion-v8.md
SHA256 a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb
LF1-134 COMPLETE
D1|1|# Definition-first common selection VIII: sentinel completion, exact affine D2 coupling for the last two rows, and a Hamilton parity obstruction
D1|2|
D1|3|Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:17:54 PDT 2026**.
D1|4|
D1|5|**NEW author-WRITTEN, unreviewed completion bridge.** This is universally quantified over actual partial row systems, not a chosen numerical state or support stratum. At original order11 it applies to EVERY nine-row subsystem of a putative original array. It gives exact distance-two constraints on the remaining two cycle covers as affine equations over the two-element field, while retaining the indispensable Hamilton-cycle realization conditions. A parity obstruction and a missing-pair capacity obstruction follow. No original table or all-array contradiction is delivered.
D1|6|
D1|7|## 0. Inputs and separation
D1|8|
D1|9|Only the current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), the prospective controls/pre-body ACK, and named elementary facts are inputs. Needed facts: actual permutation-row counting, directed graph degrees/paths, alternating cycles in a degree-two bipartite graph, elementary binary equations, and signs of finite permutations. Proofs are below.
D1|10|
D1|11|No old turn/converse/support/Latin-sign theorem, source, private type8 or author/reviewer material is imported. The sentinel graph is defined afresh directly from literal rows; it is NOT an old split/turn construction. The Olson packet remains review-only. Prior exposure survives without a clean-cognition or independent-reconstruction claim.
D1|12|
D1|13|No interpreter/calculator/Eval/CAS, row/graph enumeration, selected numeric/control/boundary probe, program, solver, replay, modelCLI or new GO. Component orientations below are mathematical variables for ALL possibilities, not an executed branch search.
D1|14|
D1|15|## 1. Exact full-array sentinel equivalence
D1|16|
D1|17|Let X have n≥3 symbols, and adjoin a NEW formal vertex ∞ not in X. For a genuine linear row
D1|18|
D1|19|`a1,…,a_n`,
D1|20|
D1|21|form the directed cycle
D1|22|
D1|23|`∞→a1→a2→…→a_n→∞`.
D1|24|
D1|25|This is a Hamilton cycle on N=n+1 vertices. The sentinel is bookkeeping only: no original row is given wraparound events.
D1|26|
D1|27|### Lemma 1 — whole-array forward/converse
D1|28|
D1|29|An original n-row array is equivalent to a decomposition of the complete loopless directed graph on X∪{∞} into n Hamilton cycles, with the extra condition that all directed two-step paths whose THREE vertices lie in X have distinct ordered outer pairs across the cycles.
D1|30|
D1|31|**Proof.** In an original array each symbol is first once and last once: n occurrences minus n−1 outgoing/incoming adjacency events leaves one terminal/initial occurrence respectively. Thus the n augmented cycles use each ∞→x arc and x→∞ arc once, as well as each x→y adjacency arc once. They decompose the complete directed graph.
D1|32|
D1|33|Conversely, deleting ∞ from each Hamilton cycle gives n actual linear permutations of X. Every x→y arc with x,y∈X is used exactly once, proving original adjacency coverage. The extra two-step condition applies precisely to the internal consecutive triples of those linear rows. It deliberately ignores paths using ∞ in ANY of their three positions. Hence it is exactly original distance-two noncollision, not a stronger cyclic requirement. ∎
D1|34|
D1|35|This equivalence by itself is a representation. The following completion results supply additional common-selection constraints and exact remaining realization gaps.
D1|36|
D1|37|## 2. Arbitrary n−2-row partial system and residual degree-two graph
D1|38|
D1|39|Take ANY n−2 actual rows with pairwise distinct distance1 and distance2 events at the respective distances. A full extension must have distinct starting symbols and distinct ending symbols among these rows, by the endpoint count above. If either fails, there is no extension.
D1|40|
D1|41|Assume these distinctness conditions. Their augmented cycles are edge-disjoint in the complete directed graph on N vertices. Delete those n−2 cycles; call the residual directed graph D.
D1|42|
D1|43|Every vertex has indegree2 and outdegree2 in D, since the complete graph degree is n and n−2 Hamilton cycles have been removed. D is loopless and has no parallel directed arcs. A two-row adjacency completion is precisely a partition of D into TWO Hamilton cycles. This degree-two conclusion is derived for the augmented residual, not imposed on an original missing-distance2 graph.
D1|44|
D1|45|Construct the bipartite graph B with a left and right copy of every vertex in X∪{∞}; the directed arc u→v in D becomes the edge u_L v_R. All degrees are2. Consequently each connected component of B is an even cycle, with exactly TWO alternating edge-colourings by colours0,1.
D1|46|
D1|47|Choose a reference alternating colouring τ(e) symbolically on each component. If B has c components, every proper two-colouring of its edges is
D1|48|
D1|49|`χ(e)=τ(e) xor x_j`, where e belongs to component j, with `x_j∈{0,1}`.
D1|50|
D1|51|Each colour has one incoming/outgoing arc at every vertex, so it is a permutation/cycle cover. It need NOT be a Hamilton cycle; that condition is retained below.
D1|52|
D1|53|## 3. Distance-two restrictions become exact affine equations
D1|54|
D1|55|Let U be the set of ordered outer pairs already used at distance2 by the n−2 fixed rows. These are `(n−2)^2` distinct pairs. For each distinct a,c∈X, consider ALL residual two-step paths
D1|56|
D1|57|`a→b→c`, with b∈X,
D1|58|
D1|59|whose arcs lie in D. There are at most two such paths, because D has outdegree2 at a. In a proper colour splitting, such a path is an added original D2 event exactly when its two arcs have the SAME colour.
D1|60|
D1|61|### Lemma 2 — exact local constraints for both added rows
D1|62|
D1|63|All distance2 noncollision requirements for the two added cycle covers, relative to U, hold exactly under the following constraints:
D1|64|
D1|65|1. If (a,c)∈U, EVERY available path a→b→c must have its two arcs differently coloured.
D1|66|2. If (a,c)∉U and there are TWO available paths, it is necessary and sufficient that the two arcs of EITHER ONE of them be differently coloured. Then the other path is differently coloured as well.
D1|67|3. If (a,c)∉U and there is only one available path (or none), there is no extra distance2 constraint for that outer pair.
D1|68|
D1|69|**Proof.** A used outer pair allows no new occurrence, giving1.
D1|70|
D1|71|For2, let the two paths have distinct middles b,d. The outgoing arcs a→b,a→d have opposite colours, and the incoming arcs b→c,d→c have opposite colours. If the first path's colours are u,v, the second path's are 1−u,1−v. Thus both paths are monochromatic exactly when u=v; in that case they lie in different colours and duplicate the outer pair across the two added rows. Otherwise neither is monochromatic, and there is no new event. This proves both necessity and sufficiency.
D1|72|
D1|73|For3, one available path can occur in at most one colour, so an unused pair cannot be duplicated. These are all paths and all distinct original outer pairs, proving the complete claim. ∎
D1|74|
D1|75|For each required differently-coloured pair of arcs e,f, the component variables satisfy
D1|76|
D1|77|`x_j xor x_k = 1 xor τ(e) xor τ(f)`.                              (D2-XOR)
D1|78|
D1|79|So the exact original D2 coupling of the TWO cycle covers is an affine binary system, not an unverified packet/row-margin assumption. If j=k, a right side1 is an immediate contradiction and right side0 is a tautology. For different components, the labelled constraint graph is consistent exactly when its edge labels xor to0 on every cycle: necessity follows by cancelling each variable twice; conversely, assign one variable per connected component and propagate labels along a path, with cycle consistency making the result path-independent. This is a written equivalence, not an executed linear solver.
D1|80|
D1|81|Diagonal outer pairs a=c are not silently admitted as valid row triples. Hamilton cycles of length N≥4 below exclude every repeated vertex in a linear row. One may additionally impose opposite colours on all such original-symbol two-step returns as an early necessary condition; Lemma2 addresses exactly the distinct outer-pair D2 requirement from the literal definition, with Hamilton realization still explicit.
D1|82|
D1|83|## 4. A genuine missing-pair capacity obstruction
D1|84|
D1|85|Let T be the set of UNUSED outer pairs (a,c)∉U with TWO residual internal-middle paths. Under Lemma2 neither path may be monochromatic, so every pair in T is missing from the final original D2 event set.
D1|86|
D1|87|A complete original array has exactly n missing directed pairs: n(n−1) possible pairs minus n(n−2) distinct D2 events. Therefore
D1|88|
D1|89|`|T|≤n`                                                          (CAP)
D1|90|
D1|91|is necessary for extension. More than n such double-path unused pairs is an exact no-extension certificate, independent of whether the affine system can be solved or the cycle covers made Hamilton.
D1|92|
D1|93|No particular partial row system or outer pair is chosen or counted here. This is a universal implication for EVERY admissible partial system and hence for every n−2-row deletion of a hypothetical original array.
D1|94|
D1|95|## 5. Hamilton realization is NOT removed: an independent parity obstruction
D1|96|
D1|97|Let B's c alternating-cycle components have lengths `2l_1,…,2l_c`. Then `Σ_j l_j=N`. Splitting B into two perfect matchings gives permutations P,Q on the N augmented vertices. On component j their relative permutation is a cycle of length l_j, up to inversion/conjugation, so
D1|98|
D1|99|`sgn(P)sgn(Q)=Π_j (-1)^(l_j−1)=(-1)^(N−c)`.
D1|100|
D1|101|For completeness, following first a Q matching edge and then a reversed P matching edge runs once around the component's l_j left vertices. Hence the relative bijection on those vertices is one l_j-cycle. This proves the sign factor directly, without a Latin-square sign theorem.
D1|102|
D1|103|If BOTH P and Q were Hamilton cycles on N vertices, each would have sign `(-1)^(N−1)`, so their product would be+1. Thus
D1|104|
D1|105|`N−c is EVEN`                                                    (HP)
D1|106|
D1|107|is necessary, independent of every component orientation variable.
D1|108|
D1|109|At original n=11 (N=12), B must have an EVEN number of components. An odd component count is a rigorous two-row noncompletion certificate. It is not a contradiction for all original arrays: any genuine two-row remainder already obeys it.
D1|110|
D1|111|This parity condition is NOT sufficient for Hamiltonicity. Nor are affine D2 consistency or the degree equations. They remain necessary constraints alongside the actual requirement that both permutations be single N-cycles.
D1|112|
D1|113|## 6. Complete forward/converse two-row caller
D1|114|
D1|115|Given the fixed n−2 partial rows, a full original extension exists IF AND ONLY IF:
D1|116|- their starting symbols and ending symbols are separately distinct;
D1|117|- some component orientation vector x in §2 satisfies every (D2-XOR) equation;
D1|118|- BOTH resulting colour permutations are Hamilton cycles of length N.
D1|119|
D1|120|**Forward:** an original completion supplies exactly those two cycles, their proper colouring, component vector and D2 constraints.
D1|121|
D1|122|**Converse:** such a vector partitions every residual arc once into the two actual Hamilton cycles. Delete ∞ from them. The result is two actual linear permutation rows; with the fixed rows their adjacencies cover every directed original pair exactly once, and Lemma2 checks every distinct outer-pair D2 event, with no sentinel-wrap event included. Hamiltonicity rules out repeated-symbol rows and diagonal two-step returns. Thus the same constructed rows satisfy the literal original definition.
D1|123|
D1|124|(CAP) and (HP) are proved necessary certificates for this exact caller, not substitutes for its remaining Hamilton conditions.
D1|125|
D1|126|## 7. Original target and next genuine gap
D1|127|
D1|128|This applies without assuming any maximal cross-layer overlap, any old support census or a selected construction family. It exposes a concrete common-row selection interface after an arbitrary n−2-row partial system: local D2 coupling is affine, but the two single-cycle conditions are still global.
D1|129|
D1|130|No nine-row input at n=11 is supplied or evaluated, and no proof is given that every possible such input violates (CAP), (HP), affine consistency or Hamiltonicity. Thus the original problem is still OPEN. Conversely no satisfiable local system is promoted to an actual completion without both Hamilton-cycle witnesses.
D1|131|
D1|132|**Next admitted mathematical step:** retain this exact residual common-row system and determine whether stronger universal Hamilton/affine compatibility or an original all-row extension theorem follows. A degree-two cycle cover or a feasible fractional mixture alone does not pay that step. No old theorem/source, solver or selected probe is requested by implication.
D1|133|
D1|134|All prior exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Author-written, unreviewed, same harness; no parent adoption, formal/kernel, executable, human, configured-family, priority or novelty claim. Deadline unchanged.

## D2 [DEPENDENCY (input only where used)] /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-affine-hamilton-cuts-v9.md
SHA256 141812a7a8eeebc90c3da035ae1d9b9f3612898d843fa861209ae6e528f55324
LF1-101 COMPLETE
D2|1|# Definition-first common selection IX: stronger missing-pair capacity and exact Hamilton cut coupling after affine D2 closure
D2|2|
D2|3|Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:21:58 PDT 2026**.
D2|4|
D2|5|**NEW author-WRITTEN, unreviewed necessary/sufficient completion certificates.** These apply to ANY actual n−2-row partial system at the original n=11, not a maximal-overlap or selected support family. They retain all original actual-row quantifiers. No original partial input or witness is supplied, and no all-array contradiction is claimed.
D2|6|
D2|7|## 0. Source and imports
D2|8|
D2|9|Same admitted S1 definition-first actual-row line; the only external problem source is literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37. This continues the fully proved own `prerequisite-two-row-completion-v8.md`, SHA256 `a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb`.
D2|10|
D2|11|Imports are the v8 sentinel equivalence, degree-two residual/component parametrization and exact D2-XOR lemma, plus elementary finite counting, binary equations and permutation-cycle connectivity. No old proof/turn/Latin-sign/support/source, held/ZERO guide, private method or Olson review input. Prior exposure is not certified absent.
D2|12|
D2|13|No row/graph enumeration, scientific execution, arithmetic interpreter, calculator/CAS, selected numeric/control/boundary probe, solver, modelCLI or new GO. Universal cut families and affine variables below are mathematical quantifiers, not an executed cut-generation or search procedure.
D2|14|
D2|15|## 1. Setting and a stronger capacity obstruction
D2|16|
D2|17|Use v8's arbitrary fixed n−2 actual rows and augmented residual graph D on X∪{∞}, with all degrees2. The fixed rows have separately distinct starting and ending symbols; otherwise no extension is possible. Let U be their `(n−2)^2` already-used directed D2 outer pairs.
D2|18|
D2|19|Among the UNUSED distinct outer pairs in X, define Z_j for j=0,1,2 according to whether exactly j residual paths a→b→c with b∈X are available. There are at most two paths, and the sets partition the unused pairs. Their total size is
D2|20|
D2|21|`|Z_0|+|Z_1|+|Z_2|=n(n−1)−(n−2)^2=3n−4`.
D2|22|
D2|23|**Proposition 1 — strengthened mandatory missing set.** In any two-row extension, EVERY pair in `Z_0∪Z_2` is absent from the final D2 event set. Consequently
D2|24|
D2|25|`|Z_0|+|Z_2|≤n`, equivalently `|Z_1|≥2n−4`.                      (RES)
D2|26|
D2|27|**Proof.** A pair in Z_0 has no path from which to create a new event and was unused before. A pair in Z_2 cannot be created by either path: by v8 Lemma2, the two paths are simultaneously monochromatic or simultaneously nonmonochromatic under any proper two-colouring; the first alternative would duplicate the pair, so both must be nonmonochromatic. Thus every pair in Z_0 or Z_2 is among the n final missing directed pairs. Equivalently the last two actual rows must obtain all their2(n−2) distinct new D2 events from Z_1. ∎
D2|28|
D2|29|This strengthens v8's bound on Z_2 alone; it does not edit or invalidate that weaker necessary bound. No specific outer-pair count is asserted for an unprovided nine-row input.
D2|30|
D2|31|## 2. Hamiltonicity is exactly a simultaneous two-colour cut condition
D2|32|
D2|33|For a nonempty proper vertex subset A⊂X∪{∞}, write δ⁺(A) for the directed residual arcs leaving A.
D2|34|
D2|35|A proper two-colouring χ gives one outgoing/incoming edge of each colour at each vertex, hence two permutation cycle covers P,Q. Such a permutation cover is a single Hamilton cycle exactly when it has an edge leaving every nonempty proper A: if it has multiple cycles, one cycle's vertex set is closed; conversely a closed proper set cannot occur in one full Hamilton cycle.
D2|36|
D2|37|Therefore BOTH P and Q are Hamilton exactly when
D2|38|
D2|39|> δ⁺(A) contains both colours for EVERY nonempty proper A.          (HCUT)
D2|40|
D2|41|This is not just degree balance. In particular a cut with zero or one outgoing residual arc precludes any two-row extension.
D2|42|
D2|43|With v8's component variables, `χ(e)=τ(e) xor x_j`, each HCUT is a not-all-equal constraint on the actual outgoing-arc colour literals. A two-arc cut gives the exact extra affine equation χ(e) xor χ(f)=1. Larger cuts are NOT replaced by an unjustified binary equation.
D2|44|
D2|45|**Complete caller.** A two-row original extension exists iff there is one SAME component vector satisfying every v8 D2-XOR equation AND every HCUT. Forward is immediate from the two actual augmented Hamilton cycles. Conversely proper colouring plus HCUT makes both cycles Hamilton; deleting ∞ gives the actual rows, and D2-XOR checks every original outer pair. No sentinel event is counted as an original event.
D2|46|
D2|47|## 3. What affine closure proves about each cut — exactly
D2|48|
D2|49|Start with the D2-XOR equations. One may additionally include all mandatory two-arc HCUT equations. If they are inconsistent, there is no extension.
D2|50|
D2|51|A consistent system of equations `x_j xor x_k=b_jk` partitions its variables into connected constraint classes. Choose one free bit y_C per class. Within it,
D2|52|
D2|53|`x_j = y_C xor d_j`,
D2|54|
D2|55|where d_j is fixed by any path from a reference variable; cycle consistency makes d_j well-defined. Thus every residual arc has colour
D2|56|
D2|57|`χ(e)=y_(C(e)) xor s_e`,
D2|58|
D2|59|where s_e is its fixed reference parity. Different classes' free bits are independent for THIS affine system. No independence after imposing HCUT is claimed.
D2|60|
D2|61|### Lemma 2 — exact universal cut-safety criterion
D2|62|
D2|63|For any fixed cut δ⁺(A), the following are equivalent:
D2|64|1. EVERY solution of this affine system gives both colours on that cut.
D2|65|2. The cut contains two arcs e,f in the SAME constraint class with fixed opposite parities `s_e xor s_f=1`.
D2|66|
D2|67|**Proof.** Such a pair always differs in colour, proving2→1. If no such pair exists, all cut arcs belonging to any one class have the same s_e. Choose that class's free bit to cancel this parity. These choices are independent between classes, so one affine solution makes ALL cut arcs colour0; global complementation gives colour1. Thus1 fails. Empty and single-arc cuts also fail1 and have no such opposite pair, so the equivalence covers them. ∎
D2|68|
D2|69|This is an exact statement about EVERY affine solution, not the stronger and unproved claim that failure of2 excludes SOME Hamilton solution.
D2|70|
D2|71|### Corollary 3 — robust completion certificate
D2|72|
D2|73|If the affine system is consistent and EVERY nonempty proper cut has a pair as in Lemma2(2), then EVERY affine solution gives two Hamilton cycles and hence an original two-row extension.
D2|74|
D2|75|**Proof.** Lemma2 supplies HCUT simultaneously for each solution; v8's exact caller supplies the actual original rows. The existence of an affine solution is already included in the stated premise and follows from cycle consistency of its labelled constraint graph. ∎
D2|76|
D2|77|This is a genuine realization direction: once those universal cut certificates and the affine consistency premise are proved for a given actual partial system, no separate favourable cycle-cover-to-row assertion is needed. No such partial system is constructed here.
D2|78|
D2|79|## 4. Forced monochromatic cuts are unconditional noncompletion certificates
D2|80|
D2|81|**Proposition 4.** If for some nonempty proper A all arcs of δ⁺(A) are in ONE affine constraint class and have the SAME fixed parity, that cut is monochromatic in EVERY affine solution. Thus no original two-row extension exists. A zero-arc cut is likewise impossible.
D2|82|
D2|83|**Proof.** All those arc colours are the identical expression y_C xor s. No assignment can put both colours on the cut, so HCUT fails. ∎
D2|84|
D2|85|This condition is stronger than merely observing that one affine solution makes a cut monochromatic. If the cut uses several independent classes but has no forced opposite pair, Lemma2 shows a bad affine solution exists; it does NOT show no good solution exists. The remaining not-all-equal constraints may couple those classes and still admit a Hamilton solution. That quantifier boundary is essential.
D2|86|
D2|87|**Additional affine closure.** In particular a two-arc cut whose two arcs are forced equal contradicts its mandatory opposite-colour equation. More generally, adding ALL two-arc cut equations preserves an exact necessary system. It cannot justify discarding larger-cut constraints that are not thereby made universally safe.
D2|88|
D2|89|## 5. Exact original scope and remaining selection issue
D2|90|
D2|91|For every hypothetical original eleven-row array, EVERY choice of nine of its rows must yield a residual satisfying (RES), the affine constraints, the parity necessary condition of v8 and an actual common solution of HCUT. The results do not assert that some such choice necessarily violates one of them.
D2|92|
D2|93|We now have:
D2|94|- a stronger all-variable forced-missing capacity obstruction;
D2|95|- an exact affine-plus-cut completion equivalence;
D2|96|- a robust positive completion certificate (Corollary3);
D2|97|- a robust negative completion certificate (Proposition4).
D2|98|
D2|99|**Still unproved:** for an arbitrary original partial system, whether its remaining higher-arity cut constraints have a joint solution, or a universal reason why some unavoidable residual violates them. A feasible affine system or one nice colouring is not enough. No input-clean argument currently supplies a nine-row partial system meeting the positive certificate, and no all-array obstruction is claimed.
D2|100|
D2|101|The route remains the literal original problem, not a promise to solve a smaller fixed-state instance. No computational cut/row search, modelCLI or new source is admitted. Old source/method/exposure STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP remain. Same-harness author-written, unreviewed; no Main adoption, kernel/formal, executable, human, configured-family, source-openness, priority or novelty gate. Deadline unchanged.

## D3 [DEPENDENCY (input only where used)] /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-cycle-parity-cut-duality-v10.md
SHA256 a10074fff184f4978f19dc1bbda523c1f00b68214284d872497edb09c77f53d7
LF1-108 COMPLETE
D3|1|# Definition-first common selection X: Hamilton cycle parity couples affine classes; exact dual certificates for safe cuts
D3|2|
D3|3|Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:25:04 PDT 2026**.
D3|4|
D3|5|**NEW author-WRITTEN, unreviewed conditional completion result.** It adds a genuinely global cycle-sign equation to the two-row D2 affine system and identifies the precise cut-safety certificate after that higher-order coupling. It does not assume that pairwise affine classes stay independent once the new equation is imposed. No original row input, original witness or universal obstruction is supplied.
D3|6|
D3|7|## 0. Inputs and setting
D3|8|
D3|9|Only the current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), controls/pre-body ACK, and elementary binary linear algebra/permutation signs are inputs.
D3|10|
D3|11|Own input-clean proofs used:
D3|12|- v8 `prerequisite-two-row-completion-v8.md`, SHA256 `a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb`;
D3|13|- v9 `prerequisite-affine-hamilton-cuts-v9.md`, SHA256 `141812a7a8eeebc90c3da035ae1d9b9f3612898d843fa861209ae6e528f55324`.
D3|14|
D3|15|They concern ANY actual n−2-row partial system whose separate starts/ends are distinct. Its sentinel residual is a directed graph D on N=n+1 vertices with all indegrees/outdegrees2. Its bipartite representation has c cycle components of lengths2l_j, with Σl_j=N. Reference alternating arc colours τ and component variables x_j determine two cycle covers P(x),Q(x). The original distance2 restrictions give v8's exact D2-XOR equations; mandatory two-arc Hamilton cuts may also be added as in v9.
D3|16|
D3|17|No old turn/Latin/sign/support theorem, stopped method/source, held/ZERO/review body or private type8 guide is input. Prior exposures persist; the Olson packet is review-only. No scientific execution, calculator/Eval/CAS, selected numeric/control/boundary probe, row/cut enumeration, solver, modelCLI or GO.
D3|18|
D3|19|## 1. Individual Hamilton parity is an extra affine equation
D3|20|
D3|21|Let P0=P(0) be the reference colour0 matching permutation. Define b∈{0,1} by
D3|22|
D3|23|`(-1)^b = (-1)^(N−1) sgn(P0)`.
D3|24|
D3|25|### Lemma 1
D3|26|
D3|27|`sgn(P(x)) = sgn(P0) (-1)^(Σ_j (l_j−1)x_j)`.
D3|28|
D3|29|Thus P(x) being a Hamilton cycle requires
D3|30|
D3|31|`Σ_(j:l_j even) x_j = b` over F2.                                (HP1)
D3|32|
D3|33|Both P(x),Q(x) can have Hamilton parity only if the number e of even l_j is even; when e is even the SAME equation (HP1) enforces the necessary sign for both covers.
D3|34|
D3|35|**Proof.** Switching one component replaces one alternating matching by the other. Following one and reversing the other gives a single l_j-cycle on its left vertices, so the sign changes by (-1)^(l_j−1). Different components involve disjoint vertex sets, and their factors multiply, giving the formula. A Hamilton cycle has sign (-1)^(N−1), yielding HP1.
D3|36|
D3|37|Q(x)=P(x xor1) as a matching choice; its sign differs by `(-1)^(Σ_j(l_j−1))=(-1)^e`. Hence if e is odd the two signs are opposite and cannot both equal the Hamilton sign. If e is even, enforcing HP1 pays the sign requirement for both. Also `Σ(l_j−1)=N−c`, so this includes v8's parity obstruction exactly. ∎
D3|38|
D3|39|This is still only a NECESSARY cycle-sign equation. It is not a claim that a correctly signed cycle cover is Hamilton.
D3|40|
D3|41|## 2. Exact interaction with D2 parity closure
D3|42|
D3|43|Suppose the pairwise D2/two-arc-cut system is consistent. As in v9, write `x_j=y_(C(j)) xor d_j`, with one free bit per constraint class.
D3|44|
D3|45|Let A be the set of classes containing an ODD number of even-l_j components, and put
D3|46|
D3|47|`b' = b xor Σ_(j:l_j even) d_j`.
D3|48|
D3|49|Then HP1 becomes exactly
D3|50|
D3|51|`Σ_(C∈A) y_C = b'`.                                             (HP2)
D3|52|
D3|53|Consequences, all without a chosen state:
D3|54|- If A is empty and b'=1, no original two-row completion is possible, even if all D2-XOR equations are consistent.
D3|55|- If A is empty and b'=0, this particular sign condition is automatic.
D3|56|- Otherwise it is a new global affine relation among the indicated free class bits. It is not replaced by fictitious independent choices for those classes.
D3|57|
D3|58|When the relation has two class variables it is a new pairwise parity edge and may merge classes. In general it is higher-arity. The all-solutions cut criterion of v9 was explicitly for a PAIRWISE-XOR system with independent class flips; it must not be used unchanged after an arbitrary higher-arity HP2 relation. The next section gives the correct general criterion.
D3|59|
D3|60|## 3. Exact cut-safety dual for the full affine system
D3|61|
D3|62|Collect D2-XOR, mandatory two-arc cut equations and HP1 into one affine system
D3|63|
D3|64|`M x = q` over F2.                                               (AFF)
D3|65|
D3|66|If it is inconsistent, the original completion is impossible. Assume it is consistent. No Gaussian elimination or state enumeration is performed; the following is an elementary theorem about every such system.
D3|67|
D3|68|For a nonempty proper A⊂X∪{∞}, let its outgoing residual arcs be e. Each χ(e)=τ(e) xor x_(j(e)). Fix one outgoing arc e0 if the cut is nonempty. The condition that the cut is MONOCHROMATIC is precisely
D3|69|
D3|70|`χ(e) xor χ(e0)=0` for all other outgoing e,
D3|71|
D3|72|which is another linear system `L_A x=t_A`. It does not require deciding whether that common colour is0 or1. For an empty outgoing cut, the monochromatic obstruction is automatic.
D3|73|
D3|74|### Theorem 2 — exact universal Hamilton-cut certificate
D3|75|
D3|76|Every solution of (AFF) puts BOTH colours on a given nonempty cut iff the augmented system
D3|77|
D3|78|`M x=q`, `L_A x=t_A`
D3|79|
D3|80|is inconsistent. Equivalently there exist coefficient row vectors u,v over F2 such that
D3|81|
D3|82|`u M + v L_A = 0`, but `u q + v t_A = 1`.                        (DUAL)
D3|83|
D3|84|**Proof.** A solution of the augmented system is exactly an affine-feasible colouring with that cut monochromatic. Its absence is exactly the claimed universal cut safety.
D3|85|
D3|86|Any certificate DUAL makes a solution impossible by taking that linear combination of its equations. Conversely, if the augmented right side lies outside the image of its linear map, choose a basis of the image, extend it by that right side and then to a full basis. Define a linear functional that vanishes on the image basis and is1 on that right side. It annihilates all coefficient columns but not the right side, producing u,v. This is elementary finite-dimensional linear algebra, not an executed solver. ∎
D3|87|
D3|88|Thus universal safe-cut certificates need not be just a forced-opposite pair of arcs after HP2 couples several classes: a combination of several parity equations can certify that a monochromatic cut is impossible. Conversely the existence of ONE monochromatic affine-feasible colouring does NOT show that every colouring fails Hamiltonicity.
D3|89|
D3|90|## 4. Full original realization and obstruction callers
D3|91|
D3|92|**Robust positive caller.** If (AFF) is consistent and for EVERY nonempty proper vertex subset A the cut is nonempty and has a DUAL certificate, then EVERY solution of (AFF) supplies two Hamilton cycles. Deleting the sentinel gives the exact two original rows, with all D2 restrictions paid by the same affine vector. Together with the fixed n−2 rows this is an original array.
D3|93|
D3|94|**Proof.** Theorem2 makes every cut bichromatic for each solution. A permutation cycle cover with an outgoing edge of each colour from every proper subset has one cycle in each colour. The v8 forward/converse then checks all original row, adjacency and internal-distance2 conditions without wraparound. ∎
D3|95|
D3|96|**Negative callers.** Inconsistency of AFF (including the HP2 contradiction of §2), a zero outgoing cut, or a cut forced monochromatic in every affine solution excludes a completion. A DUAL certificate for cut safety is a POSITIVE ingredient for realizing rows, not a nonexistence certificate for the original array; the direction must not be reversed.
D3|97|
D3|98|**Remaining non-robust case.** If some cuts have no universal safety certificate, the original problem may still have a solution: one common vector could satisfy ALL not-all-equal cut clauses even though other affine vectors fail individual cuts. No implication from per-cut existence to simultaneous existence is asserted. The exact general caller remains one vector satisfying both affine constraints and every HCUT.
D3|99|
D3|100|## 5. Original scope and next gap
D3|101|
D3|102|The result applies to every permissible n−2-row partial system; at original order11 that means every nine-row deletion of a hypothetical full array. No particular partial system, cut, sign or numeric coefficient was selected or evaluated. It sharpens the missing common-selection premise without assuming a maximal-overlap triangle or a special support class.
D3|103|
D3|104|No admissible nine-row input meeting the positive caller is supplied, and no argument forces a negative caller for every possible input. Original Tuscan-2(11) remains OPEN. No construction, universal no-go, support promotion, book/current-openness or novelty certification is inferred.
D3|105|
D3|106|**Next genuine mathematical obligation:** find an all-variable reason for one common affine/cut solution (or unavoidable contradictory cut), not independent favourable choices for cuts, cycle signs or D2 paths. The global row selection/purity gap from v6/v7 remains a separate upstream obligation. These conditional criteria are not silently substituted for its solution.
D3|107|
D3|108|All exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Author-written, unreviewed, no Main adoption or stronger verification gate. Full-window standing direction and original deadline unchanged.

