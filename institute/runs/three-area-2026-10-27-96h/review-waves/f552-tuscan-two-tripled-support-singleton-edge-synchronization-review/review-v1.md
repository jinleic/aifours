# F552 WRITTEN review: two-tripled-support synchronization

**Disposition:** SUPPORTED at the frozen conditional scope.  
**Findings:** 0 FATAL / 0 MAJOR / 0 MINOR.  
**Scientific execution:** NOTRUN.

This is the complete review text for Main to materialize as this wave’s `review-v1.md`. Repository files were not edited under the read-only review boundary.

## 1. Scope and read record

The reviewed hypotheses are jointly:

1. Eleven actual permutation rows on the same eleven finite symbols form a T2(11): all 110 directed linear adjacency events are distinct, and all 99 directed linear distance-two events are distinct.
2. The missing finite distance-two set \(M\) equals the actual last-to-first closing set \(C\).
3. Two distinct six-symbol odd-position supports \(B,D\) each occur in three rows.

The conclusions below do **not** establish universal \(M=C\), existence of the surviving configurations, complete exclusion of either conditional branch, or unrestricted T2(11) nonexistence.

Before opening the mathematical packet, I completely read the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all twelve declared status-only controls, including their endings. I then sent the required direct administrative pre-body ACK to Main. After that ACK, I read the entire literal packet, physical LF 1–581, in ordered raw windows of at most twenty lines, through S1’s ending at source label 543 and S2’s ending at source label 36. Derivation began only after that complete read.

The supplied pins are:

- Manifest: `fb6a573e2bbb851918d336c9ba792a4dac2b86ef7533f09d9208976a62569de6`
- Freeze receipt: `437af07a81e378a8315096c738b970602b15e9695c9edad5222d2f8dcd80662b`
- Literal packet: `e3ff1fa41a370299e49ceaab9bf36d86df1faa2fb11cd3353f48ef1ec080f07c`
- S1, complete f489 candidate: `16940c11f15e2f931070ab94e0ee1e108ad1dfe2ec5bfe1c0effd5e7ea0eee83`
- S2, adopted conditional joint-cut disposition: `c82b00df7bb8fc2d3a8eb9cc3e2b841f4464314d6b471586c4a833e846c30c60`

Hashes, byte/LF counts, and the supplied native clock are attributed to the parent metadata records, not independently executed child observations. S1’s 542 LF characters versus 543 displayed source labels is explicit in the supplied records; all 543 displayed labels were read.

No new selected mathematical instance, scientific code, interpreter, solver, enumeration, replay, external CLI, public-source follow, sibling review, author code, or held mathematical payload was used. The concrete rows checked below are exactly the examples already supplied in S1. All quarantined episodes and their consumers remained NONINPUT.

## 2. Actual Hamilton cycles and square decomposition — SUPPORTED

**Source:** S1 LF 56–91.

For each actual row, retain the actual augmented cycle
\[
h_r=(\infty,r_1,\ldots,r_{11}).
\]

Adjacency exhaustion gives each symbol ten finite outgoing events. Across eleven rows, its outgoing-event count is eleven minus its last-column multiplicity, so that multiplicity is one. The incoming argument makes the first column a permutation. Consequently, the actual cycles partition all 132 directed edges on the twelve augmented vertices.

The finite square edges of those same cycles are exactly the 99 original distance-two events together with the eleven closing pairs \(r_{11}\to r_1\). Closing pairs are distinct because last-column symbols are distinct. Under \(M=C\), these finite square edges partition all 110 finite ordered pairs.

For any finite symbol, its missing outgoing distance-two count equals its penultimate-column multiplicity: last-column multiplicity is already one, leaving that identity directly from the number of eligible distance-two origins. The dual missing incoming count is its second-column multiplicity. Since \(M=C\) has indegree and outdegree one, both those columns are permutations. Hence the remaining square edges \(\infty\to r_2\) and \(r_{10}\to\infty\) also occur exactly once.

Thus both complete decompositions belong to the **same eleven actual Hamilton cycles**. The proof never substitutes arbitrary square-cycle covers for those Hamilton cycles.

## 3. Singleton saturation and the four cells — SUPPORTED

**Source:** S1 LF 93–168; exact relevant import scope: S2 LF 17–30.

For a finite colored set of size \(b\), a row with \(q\) black runs, \(s\) singleton black runs, and \(t\) internal singleton white runs has
\[
d=b-2q+s+t
\]
black-to-black distance-two events. A black run contributes its length minus two, corrected by one when its length is one; each internal singleton white run supplies one additional event between consecutive black runs.

Adjacency exhaustion gives \(\sum q=b(12-b)\), while distance-two injectivity gives \(\sum d=b(b-1)-\mu_A\). Therefore the finite singleton total is
\[
W_A=b(12-b)-\mu_A.
\]
Infinity contributes once exactly when both finite row endpoints lie in \(A\), adding \(\nu_A\). Under \(M=C\), \(\mu_A=\nu_A\), so the augmented singleton total is \(b(12-b)\).

A six-cut therefore has total 36. Three alternating cycles contribute all 36 singletons, forcing every other actual cycle to have none for that cut. The two alternating families are disjoint because a connected Hamilton cycle has only one alternating bipartition, up to complement, and the distinct finite supports cannot be complementary augmented cuts.

The intersection exclusion is valid:

- Distinct six-subsets of eleven symbols have intersection between one and five.
- At intersection five, the two cuts differ at two vertices. Changing those vertices affects singleton status only there and at their neighbors, at most six vertices. A cycle alternating for one cut retains singletons for the other, contrary to saturation.
- Intersection one reduces to the same argument by complementing the augmented \(D\)-cut.
- At intersection four, cells \(I,L\) have size four and \(J,K\) size two. In a \(B\)-alternating cycle, the absence of \(D\)-singletons forces the two \(D\)-runs to be \(IKI\), and the complementary runs to be \(LJL\). Thus neither alternating family uses a \(J\)-\(K\) edge.
- All eight directed \(J\)-\(K\) arcs would then have to occur in the residual cycles. A residual \(J\)-\(K\) adjacency forces an internal neighbor at both endpoints, consuming the unique two-vertex run in each cell. Two joins in one Hamilton cycle would close a four-vertex component. Moreover, each join consumes a directed internal \(J\)-arc, of which only two exist across the decomposition. The required eight joins are impossible.
- Intersection two reduces to intersection four by complementing the cut, without asserting that the complement is an original odd-position support.

Hence \(|B\cap D|=3\), all four cells have size three, and the residual set is the same five actual Hamilton cycles.

## 4. Uniform local ledgers and \(T\in\{13,14\}\) — SUPPORTED

**Source:** S1 LF 170–225.

For a cell \(Q\), its five residual layouts are precisely a full three-run, a pair plus singleton, or three singletons. Every internal adjacency arc belongs to the residual cycles because either alternating family changes one of the cell’s membership bits. Thus
\[
g_Q+p_Q+q_Q=5,\qquad 2g_Q+p_Q=6.
\]

A residual square edge with both endpoints in \(Q\) cannot have its middle vertex outside \(Q\): any bit changed on leaving \(Q\) would make that middle vertex a singleton for that bit. Therefore residual internal square arcs correspond exactly to full three-runs, one per run.

In a \(B\)-alternating cycle with \(j\) \(D\)-runs of either color, every such run has length at least two and contains both relevant cells. The three vertices of any particular cell therefore contribute \(3-j\) internal square arcs. The dual statement holds for the other family. Complete square-arc exhaustion gives
\[
6=(18-T)+g_Q,\qquad g_Q=T-12.
\]

Nonnegative layout counts initially allow \(g_Q=1,2,3\). The value three would partition all six internal directed arcs into three Hamilton paths on the cell. With the candidate’s path named \(a,b,c\), a path starting at \(b\) must use \(b,a,c\), leaving \(c\to a,c\to b\), which cannot form the third path. Hence three is impossible.

The exact alternatives are consequently
\[
T=13:\ (g_Q,p_Q,q_Q)=(1,4,0),\qquad
T=14:\ (g_Q,p_Q,q_Q)=(2,2,1)
\]
for every cell. This reconstructs the relevant imported table rather than treating an earlier unreviewed body as proof.

## 5. Joint diagonal saturation and singleton synchronization — SUPPORTED

**Source:** S1 LF 227–302.

A residual diagonal adjacency changes both membership bits. Avoiding a singleton for either bit forces each endpoint’s other neighbor into its own cell. Each endpoint therefore belongs to its cell’s unique nontrivial run. Two joins between the same opposite-cell pair would join both ends of those runs into a proper closed component, contrary to Hamiltonicity. Thus each residual cycle has capacity at most one \(I\)-\(L\) join and at most one \(J\)-\(K\) join.

In a \(B\)-alternating cycle, cell indegree/outdegree balance makes the directed \(J\)-\(K\) counts equal to the corresponding directed \(I\)-\(L\) counts. Their sum is the other-cut run number. The analogous statement for the \(D\)-alternating family gives exactly \(T\) adjacency occurrences between each opposite-cell pair across the six alternating cycles. Since each pair has eighteen possible directed arcs, its residual demand is \(18-T\).

### \(T=13\)

Demand is five and capacity is one in each of the same five residual cycles. Therefore **every residual cycle has exactly one join of each opposite-cell kind**.

### \(T=14\)

Demand is four. If the all-singleton cycles for \(I\) and \(L\) differed, both cycles would be unavailable for an \(I\)-\(L\) join, leaving capacity at most three. Therefore those slots coincide. The same holds for \(J,K\).

In the common \(I,L\) all-singleton cycle, every vertex of \(I\cup L\) has both neighbors in \(J\cup K\): same-cell neighbors are excluded by the layout, and diagonal neighbors would force a nontrivial cell run. These six vertices therefore supply twelve cross-cut edges, exhausting all edges of the cycle. The entire cycle alternates across \(E=J\cup K\), making \(J,K\) all-singleton there too.

Thus **all four all-singleton slots occur in one and the same residual cycle**. Each of the other four residual cycles has exactly one join of each opposite-cell kind.

At an all-singleton cell vertex, its two neighbors must change different individual bits; otherwise the vertex would be a singleton for one original cut. Following these forced cell transitions gives one orientation of \(I-J-L-K-I\), repeated three times. Connectedness comes from the retained actual Hamilton cycle—not from the projected cell word. A disconnected three-component cover is not admitted.

Finally, infinity lies in \(L\), so this actual \(E\)-alternating cycle has finite odd support exactly \(E\). All regular residual cycles contain diagonal edges, and the other alternating families have different connected bipartitions. Therefore, within the frozen conditional domain,
\[
T=13\iff k_E=0,\qquad T=14\iff k_E=1.
\]

## 6. Synchronized full-run incidence patterns — SUPPORTED

**Source:** S1 LF 304–357.

In a regular residual cycle, the unique diagonal join of each opposite-cell pair connects its two nontrivial cell runs into one block. There are exactly two such blocks, on opposite \(E\)-sides. Every remaining vertex is a singleton cell vertex, and its incident edges cross \(E\).

Each of the two gaps between the blocks consequently alternates across \(E\). Its endpoint blocks have opposite colors, so each gap contains an even number of singleton vertices, with equal numbers on the two sides. Hence the number of full cells in \(\{I,L\}\) equals that in \(\{J,K\}\), and \(f(h)\) is \(0,2\), or \(4\). If two cells are full, they form an edge, not a diagonal, of the cell square.

The simultaneous incidence totals then give exactly the stated necessary patterns:

- For \(T=13\), total full-cell incidence is four:
  \[
  (4,0,0,0,0)\quad\text{or}\quad(2,2,0,0,0).
  \]
  In the latter case, each cell occurs once, so the two edges form an opposite-edge matching.
- For \(T=14\), total full-cell incidence on the four regular cycles is eight:
  \[
  (4,4,0,0),\quad(4,2,2,0),\quad(2,2,2,2).
  \]
  The middle case again leaves an opposite-edge matching. In the last case, incidence two at every cell forces cyclic edge multiplicities
  \[
  (x,2-x,x,2-x),\qquad x\in\{0,1,2\}.
  \]

These are constraints on the same residual cycles; no independent-table feasibility is substituted.

## 7. Directed square arcs, endpoint identities, and run-sum exclusions — SUPPORTED

**Source:** S1 LF 359–464.

Neither alternating family contributes an opposite-cell square arc, because its square preserves the corresponding alternating bit. All nine arcs in each directed opposite-cell direction therefore belong to the residual cycles.

A directed diagonal square event has precisely the candidate’s two forms: a diagonal adjacency together with an internal edge, or two different one-bit changes through a singleton cell vertex. Each diagonal adjacency contributes exactly two square arcs in its direction. Thus
\[
9=2a+u,\qquad 9=2a'+u'.
\]

For \(T=13\), \(a+a'=5\); nonnegativity gives \(1\le a,a'\le4\). For \(T=14\), the actual common alternating cycle contributes three square arcs in each opposite direction. Removing it gives
\[
6=2a+u_{\rm reg},\quad 6=2a'+u'_{\rm reg},\quad a+a'=4,
\]
and therefore \(1\le a,a'\le3\). The same reasoning applies to \(J,K\).

For a fixed cell vertex, there are exactly two internal incoming and two internal outgoing adjacency occurrences across the five residual cycles. Their intersection consists precisely of occurrences where that vertex is the middle of a full cell run. Inclusion-exclusion therefore gives \(4-m_x\) occurrences with an internal neighbor, leaving exactly \(1+m_x\) singleton-cell occurrences. In \(T=14\), one is in the common alternating cycle, leaving \(m_x\) in the regular cycles.

The orientation ledger also follows from actual cell balance. With the candidate’s \(x,y,u,v\),
\[
a_{IL}=9-x-u,\quad a_{LI}=9-y-v,\quad
a_{JK}=9-x-v,\quad a_{KJ}=9-y-u.
\]
The established residual bounds place all four cross sums in \([T-8,8]\), equivalently giving
\[
\max(x,y)+\max(u,v)\le8
\]
together with the fixed total.

If one family in \(T=14\) has other-cut run sum nine, each of its three run numbers is three. Its directed diagonal contributions are therefore three in one direction or three in the other, giving a family maximum at least six. The other family has total five and maximum at least three, contradicting the bound eight. Hence the stated surviving family-sum possibilities are exactly
\[
(6,8),\ (7,7),\ (8,6).
\]

The two further consequences are valid:

- For run multiset \(1,1,3,3,3,3\), putting both run-one cycles in one family would create the excluded \(5,9\) allocation. Each family must instead total seven, and the maximum bound forces directed totals \(3,4\).
- In \(T=13\), a family totaling nine has directed totals divisible by three. The same maximum bound forces totals \(3,6\) for that family and \(2,2\) for the other. This is not a contradiction, as the candidate states.

## 8. Supplied actual-row examples — SUPPORTED at individual-row scope

**Source:** S1 LF 466–506.

The supplied rows contain each finite symbol exactly once. Their augmented cell sequences have the stated properties:

- The \(f=4\) example has four full runs \(L^3I^3J^3K^3\).
- The \(f=2\) example has full \(I,J\) runs, pair-plus-singleton \(K,L\) layouts, and the displayed cyclic cell word.
- The \(f=0\) example has one pair and one singleton in every cell; its four singleton vertices lie in the displayed alternating gap.
- In each regular example there is exactly one diagonal join of each opposite-cell kind, and every singleton cell vertex has neighboring cells differing in different bits, so neither original cut has a singleton.
- The supplied common-cycle example has cell sequence \(LJIK\) repeated three times and odd-position support \(J\cup K\).

These checks support only the stated individual Hamilton-row nonvacuity. They do not establish compatible residual collections, either complete decomposition, or a T2(11).

## 9. Residual problem and assurance boundary — SUPPORTED

**Source:** S1 LF 508–543; S2 LF 36.

The final compatibility requirement retains actual Hamilton cycles on the same twelve vertices and requires both complete directed decompositions. Removing infinity then yields distinct original adjacency and distance-two events; the finite square partition identifies the closing pairs with the missing distance-two set. The converse is supplied by the reconstruction in Section 2 above. Thus the formulation does not weaken the problem to unrelated covers or independently realizable shadows.

The first unproved step remains exactly the simultaneous exclusion or realization of labeled Hamilton collections satisfying these synchronized templates and both decompositions. Neither entire \(T=13\) nor entire \(T=14\) branch is closed. Relevant \(M\ne C\) cases and cases without two distinct tripled supports remain outside this argument.

S2 was used only at its explicit adopted scope. Its linked historical reviews, finite source, and execution receipt were not opened or replayed, and their existence was not substituted for the reconstructions above. The public definition cited by S1 was not followed; this review evaluates the explicitly frozen actual-row target, not source equivalence or literature status.

## Overall verdict

**Overall correctness: correct.** No mathematical defect was found in the frozen candidate: the diagonal saturation, common-cycle synchronization, exact \(k_E\) alternatives, and subsequent necessary arc/incidence restrictions follow for the same actual cycles under all three stated hypotheses. This is same-harness written support only, not parent adoption, independent-family or human review, kernel verification, novelty certification, or closure of the original problem.

**Confidence: 0.98.**