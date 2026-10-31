# F553 written review: conditional T2(11) joint-cycle constraints

**Verdict: SUPPORTED at the stated conditional scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The new diagonal-join saturation, common-cycle synchronization, full-run incidence restrictions, directed square-arc budgets, vertexwise identities, and exclusion of the \(T=14\) run-sum-\(9\) subbranches follow from the stated hypotheses. They do **not** exclude either complete \(T=13\) or \(T=14\) branch, construct an eleven-row array, or resolve unrestricted T2(11).

This is the complete review body for parent materialization. No repository file was written.

## 1. Reviewed inputs and process boundary

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f553-tuscan-three-cut-square-arc-budget-and-vertex-coupling-review/`

Supplied pins:

- Manifest: `7263cc75ac8337659da112422ed2cc00854a62b99c9ddfc871f4482d9a65fd62`
- Freeze receipt: `ce6d787ffdc84f6b927f61d75dbf623bc0ab9d3864f93f55d2487dcb0157bd7b`
- Literal packet: `e3ff1fa41a370299e49ceaab9bf36d86df1faa2fb11cd3353f48ef1ec080f07c`

The manifest, freeze receipt, parent metadata supply, parent dispatch receipt, and all twelve listed status-only controls were read completely before the direct administrative pre-body ACK to `agent://Main`. The write tool reported delivery. Only afterward was the mathematical packet opened.

The complete packet was read in ordered raw windows of at most twenty lines: packet lines 1–581, including both source endings. This covers:

- **S1:** displayed source labels 1–543, the f489 author candidate at  
  `review-waves/f489-actual-tuscan11-conditional-two-tripled-support-residual-closure-frontier/review-v1.md`  
  SHA `16940c11f15e2f931070ab94e0ee1e108ad1dfe2ec5bfe1c0effd5e7ea0eee83`.
- **S2:** displayed source labels 1–36, the named parent disposition at  
  `dispositions/info-4-actual-tuscan11-overlap-budget-and-conditional-tripled-support-joint-cuts-parent-v1.md`  
  SHA `c82b00df7bb8fc2d3a8eb9cc3e2b841f4464314d6b471586c4a833e846c30c60`.

The distinction between S1’s **542 LF characters** and **543 displayed source lines** is retained.

Hashes, byte counts, LF counts, freeze equality, and clock observations are attributed to the supplied parent metadata. No child-native hash, clock, or packet reconstruction was executed.

**Scientific execution: NOTRUN.** No code, CAS, interpreter, enumeration, solver, replay, build, test, linter, formatter, external CLI, or additional source access was used. No additional concrete row, cycle, or parameter instance was selected. The four examples inspected below are precisely the examples already printed in S1.

All listed quarantined episodes and their proof, method, selection, planning, reporting, and confidence consumers remain **HELD/ZERO/NONINPUT**. No excluded links, sibling review bodies, held payloads, or author code were opened. This is an access/use account, not a cognitive-isolation certificate.

## 2. Claim-by-claim disposition

Line references below are **source labels**, not packet physical line numbers.

| Claim | Disposition | Source |
|---|---|---|
| Actual-row Hamilton decomposition and, under \(M=C\), complete square decomposition | **SUPPORTED** | S1:56–91 |
| Singleton identity and saturation by three alternating cycles | **SUPPORTED** | S1:93–129 |
| Two distinct tripled supports have intersection three | **SUPPORTED** | S1:131–160 |
| Uniform residual cell tables and \(T\in\{13,14\}\) | **SUPPORTED** | S1:170–223 |
| Each \(T=13\) residual cycle has one join of each opposite-cell kind | **SUPPORTED** | S1:227–261 |
| The \(T=14\) all-singleton layouts coincide in one actual \(E\)-alternating cycle | **SUPPORTED** | S1:263–286 |
| Exact \(E\)-support multiplicity: zero for \(T=13\), one for \(T=14\) | **SUPPORTED** | S1:288–302 |
| Synchronized full-cell patterns on the same residual cycles | **SUPPORTED** | S1:304–357 |
| Directed opposite-cell square budgets and orientation bounds | **SUPPORTED** | S1:359–394 |
| Physical-vertex singleton/middle-run identity | **SUPPORTED** | S1:396–408 |
| Alternating-family orientation ledger and run-sum exclusions | **SUPPORTED** | S1:410–464 |
| Four displayed individual-row realizations | **SUPPORTED only as individual-row checks** | S1:466–506 |
| Hamilton-and-square formulation is equivalent to the stated conditional actual-row formulation | **SUPPORTED** | S1:510–521 |
| Existence or exclusion of all surviving compatible collections | **INCONCLUSIVE; explicitly unproved** | S1:523–543 |

S2:17–30 supplies the named, previously scoped conditional base. The relevant base mathematics is also reconstructed below rather than treating S2’s review or finite-execution reports as fresh verification. The universal overlap-minimum classification in S2:7–13 is not needed for the new argument and was not independently re-enumerated.

## 3. Reconstruction

### 3.1 Actual rows, closing arcs, and square transport

Let \(S\) contain eleven symbols and \(X=S\cup\{\infty\}\). For each actual permutation row
\[
r=(r_1,\ldots,r_{11}),
\]
retain the actual Hamilton cycle
\[
h_r=(\infty,r_1,\ldots,r_{11}).
\]

For a finite symbol \(z\), its original outgoing adjacency count is eleven minus its last-column multiplicity. Adjacency exhaustion gives ten outgoing targets, so that multiplicity is one. The incoming argument makes the first column a permutation.

Consequently, the original 110 finite adjacency arcs, the eleven arcs \(\infty\to r_1\), and the eleven arcs \(r_{11}\to\infty\) partition all 132 directed edges on \(X\).

The square of an actual row cycle has exactly these arcs:
\[
\infty\to r_2,\qquad
r_i\to r_{i+2}\ (1\le i\le9),\qquad
r_{10}\to\infty,\qquad
r_{11}\to r_1.
\]
Thus its finite arcs are the **original linear distance-two events plus the actual closing pair**, not a replacement cyclic distance-two condition.

Because first and last columns are permutations, \(C\) has indegree and outdegree one. For a finite symbol, the missing outgoing original distance-two count is its penultimate-column multiplicity; the missing incoming count is its second-column multiplicity. Under \(M=C\), both multiplicities are one.

Therefore the finite square arcs partition all 110 finite ordered pairs, while the second and penultimate columns supply all 22 infinity-incident square arcs exactly once. This proves S1’s complete square decomposition.

The fact that each \(h_r^2\) is two six-cycles causes no substitution: the objects being assembled remain the same eleven actual twelve-vertex Hamilton cycles.

### 3.2 Singleton budget and saturation

For a finite black set \(A\), \(|A|=b\), a linear row with \(q\) black runs, \(s\) singleton black runs, and \(t\) internal singleton white runs has
\[
d=b-2q+s+t
\]
original black-to-black distance-two events. A black run of length \(\ell\) contributes \(\max(\ell-2,0)\); each internal singleton white run contributes one further event.

Across eleven rows,
\[
\sum q=b(12-b),\qquad
\sum d=b(b-1)-\mu_A.
\]
Hence the finite singleton total is
\[
W_A=b(12-b)-\mu_A.
\]
Infinity is singleton exactly when the row’s two endpoints belong to \(A\), contributing \(\nu_A=|C\cap A^2|\). Under \(M=C\),
\[
\sum_r S_A(h_r)=b(12-b).
\]

For a balanced six-cut, this is 36. Three alternating Hamilton cycles contribute all 36 singletons, so every other actual cycle has none for that cut.

The \(B\)- and \(D\)-alternating families are disjoint: a connected even Hamilton cycle has only one alternating bipartition up to complementation, and the two distinct finite six-supports cannot be complementary cuts on \(X\). Their union therefore has six cycles, leaving the same five-cycle set \(\mathcal R\) throughout the proof.

### 3.3 Intersection three

For overlap five, the two balanced colorings differ at two vertices. Only those vertices and their neighbors can change singleton status, so a \(B\)-alternating cycle retains at least six \(D\)-singletons. This contradicts \(D\)-saturation. Overlap one reduces to this by complementing the **cut**, without asserting that the complement is a finite odd-position support.

For overlap four, the cells have sizes
\[
|I|=|L|=4,\qquad |J|=|K|=2.
\]
In a \(B\)-alternating cycle, all \(D\)-runs have length at least two. The \(D\)-side contains four \(I\)-vertices and two \(K\)-vertices. One run cannot accommodate the imbalance, and three length-two runs would be balanced. Thus its two runs are \(IKI\) and \(IKI\); the complementary runs are \(LJL\) and \(LJL\). There is no \(J\)-\(K\) adjacency. The \(D\)-alternating family gives the same absence.

All eight directed \(J\)-\(K\) arcs must then occur in \(\mathcal R\). A residual diagonal join forces each endpoint’s other neighbor into its own cell. Such a join uses the unique two-vertex run of each size-two cell; two joins in one cycle would close a proper component. Moreover, each join consumes an internal directed \(J\)-arc, of which only two exist across the decomposition. Eight joins are impossible.

Overlap two reduces to overlap four by cut complementation. Since distinct six-subsets of eleven symbols have overlap between one and five, only
\[
|B\cap D|=3
\]
remains. Thus all four cells have size three.

### 3.4 The residual cell tables

For one cell \(Q\), classify its layout in each of the five residual cycles as full, pair-plus-singleton, or all-singleton. With counts \(g_Q,p_Q,q_Q\),
\[
g_Q+p_Q+q_Q=5,\qquad 2g_Q+p_Q=6.
\]
The second equation counts all six directed internal adjacency arcs of \(Q\); none can occur in either alternating family.

A residual square arc internal to \(Q\) cannot have its middle vertex outside \(Q\), because that vertex would then be singleton for a changed membership bit. It therefore corresponds exactly to a full three-vertex cell run.

In a \(B\)-alternating cycle with \(j=r_D(h)\), every \(D\)-run has length at least two and contains both relevant cells. For each cell, summing “number of its vertices in the run minus one” gives \(3-j\) internal square arcs. The same argument applies to the other family.

The complete square decomposition consequently gives, for every cell,
\[
6=(18-T)+g_Q,\qquad g_Q=T-12.
\]
Together with the adjacency equations,
\[
p_Q=6-2g_Q,\qquad q_Q=g_Q-1,
\]
so initially \(g_Q\in\{1,2,3\}\).

The value three would decompose the six directed arcs on three vertices into three spanning directed paths. As in S1’s displayed argument, after naming one path \(a,b,c\), degree accounting gives one start and one end per vertex. The path starting at \(b\) is forced to be \(b,a,c\); the remaining arcs \(c\to a,c\to b\) cannot form the third path.

Thus \(g_Q=1\) or \(2\), uniformly over the four cells:
\[
T=13:\ (g_Q,p_Q,q_Q)=(1,4,0),
\qquad
T=14:\ (g_Q,p_Q,q_Q)=(2,2,1).
\]

### 3.5 Diagonal capacity and common-cycle synchronization

A residual diagonal adjacency changes both bits. Avoiding singleton status forces each endpoint’s other neighbor into its own cell. Every size-three cell has at most one nontrivial run. Two joins between the same opposite-cell pair would join both ends of those runs and close a proper component.

Hence each residual cycle has capacity at most one \(I\)-\(L\) join and one \(J\)-\(K\) join.

In a \(B\)-alternating cycle, write its \(I\to L,L\to I\) counts as \(a,b\). Cell balance makes its \(J\to K,K\to J\) counts \(a,b\). All \(D\)-crossing edges are diagonal, so
\[
r_D(h)=a+b.
\]
The analogous statement holds for the other family. Each opposite-cell pair therefore has exactly
\[
18-T
\]
joins remaining in \(\mathcal R\).

For \(T=13\), five required joins saturate five-cycle capacity for each pair. Every residual cycle has exactly one join of each kind.

For \(T=14\), each cell has one all-singleton occurrence. If the all-singleton occurrences of \(I\) and \(L\) were in different cycles, at most three cycles could contain an \(I\)-\(L\) join, contrary to four required joins. They coincide.

In that common cycle, all six vertices of \(I\cup L\) have both neighbors in \(J\cup K\): same-cell adjacency is absent, and diagonal adjacency would force nontrivial runs. These vertices account for twelve cross-cut incidences, exhausting the twelve edges. The cycle alternates across
\[
E=J\cup K=B\triangle D.
\]
Consequently \(J,K\) are also all-singleton in the same cycle \(h_E\).

Avoiding \(B\)- and \(D\)-singletons forces consecutive cell transitions to change different bits. The cell walk therefore follows one orientation of
\[
I-J-L-K-I
\]
three times. Hamiltonicity is retained from the original cycle; this is not an assertion that three disconnected four-cycles suffice.

The other four residual cycles each carry one join of each opposite-cell kind.

Since \(\infty\in L\), the alternating side not containing infinity is exactly the finite support \(E\). In \(T=13\), every residual cycle has an \(E\)-monochromatic diagonal edge, while neither original alternating family can also alternate across this distinct cut. In \(T=14\), only \(h_E\) can alternate across \(E\). Therefore
\[
k_E=0\quad(T=13),\qquad k_E=1\quad(T=14).
\]
Because these are the only two values of \(T\), the stated equivalences follow.

### 3.6 Full-run incidence on the same cycles

In a regular residual cycle, the unique diagonal joins combine the nontrivial runs into one \(I\cup L\) block and one \(J\cup K\) block. Every remaining vertex is a singleton of its cell.

At a singleton cell vertex, its neighbors must differ from it in different single bits. Both incident edges therefore cross \(E\). The two gaps between the opposite-\(E\)-colored blocks consequently contain even numbers of singleton vertices, with equal numbers from each \(E\)-side.

Each non-full cell contributes exactly one such singleton. Thus the numbers of full cells in the two opposite-cell pairs are equal:
\[
\#\text{full cells in }\{I,L\}
=
\#\text{full cells in }\{J,K\}.
\]
It follows that \(f(h)\in\{0,2,4\}\); when \(f(h)=2\), the full cells are adjacent, not opposite, in the cell square.

For \(T=13\), the total number of full-cell occurrences is four, yielding exactly
\[
(4,0,0,0,0),\qquad (2,2,0,0,0).
\]
In the second pattern, each cell occurs once, so the two selected edges form an opposite-edge matching.

For \(T=14\), exclude \(h_E\), which has no full cell. Each cell is full twice among the four regular cycles. Their total is eight, giving
\[
(4,4,0,0),\qquad (4,2,2,0),\qquad (2,2,2,2).
\]
The middle pattern again leaves an opposite-edge matching. In the last pattern, degree two at each cell forces cyclic edge multiplicities
\[
(x,2-x,x,2-x),\qquad x\in\{0,1,2\}.
\]

These deductions retain the common residual-cycle indices. They do not combine four unrelated local ledgers.

### 3.7 Directed square budgets

Neither alternating family supplies an opposite-cell square arc: its square preserves its alternating bit. Hence all nine square arcs in each directed opposite-cell direction must occur in \(\mathcal R\).

A two-step residual path between opposite cells has exactly two possible cell types:

1. an internal edge and a diagonal adjacency, in either order;
2. two distinct one-bit changes, with a singleton cell vertex in the middle.

For an adjacency \(I\to L\), the other neighbor of each endpoint is internal to that endpoint’s cell. The adjacency therefore supplies exactly two \(I\to L\) square arcs. No such event is counted twice by two diagonal adjacencies.

Writing \(a,a'\) for residual \(I\to L,L\to I\) adjacency counts gives
\[
9=2a+u,\qquad 9=2a'+u',
\]
with nonnegative singleton-event counts.

For \(T=13\), \(a+a'=5\), so
\[
1\le a,a'\le4.
\]

For \(T=14\), the actual common cycle \(h_E\) contributes three square arcs in **each** directed opposite-cell direction. Removing that contribution gives
\[
6=2a+u_{\rm reg},\qquad
6=2a'+u'_{\rm reg},\qquad
a+a'=4,
\]
and therefore
\[
1\le a,a'\le3.
\]
The same reasoning applies to \(J,K\).

The count includes infinity as a physical vertex of \(L\). Its square arcs are justified by the complete square decomposition, not silently identified with original linear distance-two events.

### 3.8 Physical-vertex identity

Fix an actual vertex \(z\) of a cell. Across the five residual cycles, it receives exactly two internal incoming and two internal outgoing adjacency arcs.

The intersection of those occurrence sets consists precisely of full cell runs having \(z\) as middle vertex. If their number is \(m_z\), inclusion–exclusion gives
\[
\#\{\text{occurrences with an internal neighbor}\}=4-m_z.
\]
Among five occurrences, the remaining singleton-cell occurrences therefore number
\[
1+m_z.
\]

For \(T=14\), exactly one is the occurrence in \(h_E\). Among the four regular cycles the count is consequently \(m_z\).

This is vertexwise, including for \(z=\infty\). It does not permit middle choices and singleton choices to be reassigned independently after aggregation by cell.

### 3.9 Alternating-family orientation and run-sum exclusions

Let \(x,y\) be the total \(I\to L,L\to I\) counts in \(\mathcal A_B\), and \(u,v\) the corresponding totals in \(\mathcal A_D\).

Cell balance in the two respective alternating bipartitions gives
\[
\begin{aligned}
a_{IL}&=9-x-u,&a_{LI}&=9-y-v,\\
a_{JK}&=9-x-v,&a_{KJ}&=9-y-u,
\end{aligned}
\qquad x+y+u+v=T.
\]
In particular, the \(J,K\) correspondence is reversed for the \(D\)-alternating family, as S1 correctly records.

The residual orientation bounds imply that all four cross sums
\[
x+u,\quad x+v,\quad y+u,\quad y+v
\]
lie in \([T-8,8]\). Their largest is
\[
\max(x,y)+\max(u,v),
\]
which must be at most eight.

If one three-cycle family has other-cut run sum nine, all three run numbers are three. Each other-cut run then has length two, and the cell word follows the printed four-cell orientation or its reverse. Each cycle contributes either \((3,0)\) or \((0,3)\) to its directed \(I,L\) totals. The family’s larger directed total is therefore at least six.

For \(T=14\), the other family has total five and hence larger directed total at least three. Their sum exceeds eight, a contradiction. Thus \((9,5)\) and \((5,9)\) are excluded. Since each family contains three run numbers between one and three, the remaining sum pairs are exactly the necessary alternatives
\[
(6,8),\qquad(7,7),\qquad(8,6).
\]
No existence of those alternatives follows.

The two additional consequences also follow:

- For the printed multiset \(1,1,3,3,3,3\), placing both run-one cycles in one family would give the excluded \((5,9)\) allocation. Each family instead has \(1,3,3\), total seven. Each larger directed total is at least four; their sum is at most eight, forcing directed totals \(3,4\) in each family.
- For \(T=13\), a run-sum-nine family has larger directed total at least six, and the other family, of total four, has larger directed total at least two. The bound forces equality: totals \(3,6\) and \(2,2\). This is not a contradiction.

### 3.10 Printed physical examples

Only the four rows explicitly supplied in S1:468–504 were inspected.

- The \(f=4\) row gives \(L^3I^3J^3K^3\), with diagonal joins \(11\to1\) and \(6\to7\).
- The \(f=2\) row gives the printed word \(LLIIIKLJJJKK\). Its singleton vertices \(7\in K\) and \(11\in L\) have neighbors differing in distinct single bits. Its diagonal joins are \(10\to1\) and \(6\to8\).
- The \(f=0\) row gives the printed cyclic word \(IILLJIKLJJKK\). Its four singleton vertices form the stated gap, and its diagonal joins are \(2\to\infty\) and \(6\to8\).
- The final row has cell word \(LJIK\) repeated three times, no diagonal adjacency, and finite odd-position support \(J\cup K\).

Each is a permutation row with the asserted individual augmented-cycle structure. None establishes compatibility with the other rows or with an eleven-row Hamilton-and-square decomposition. S1 preserves that limitation.

## 4. Consumer and scope audit

The load-bearing transitions are correctly consumed:

1. **Actual rows → square decomposition.**  
   S1:71–91 separately accounts for original linear distance-two events, closing pairs, and infinity-incident square arcs. The complete decomposition is then used in the internal-cell ledger at S1:191–208 and the opposite-cell budgets at S1:363–391.

2. **Five-cycle local table → synchronized structures.**  
   S1:229–286 applies capacities on the same \(\mathcal R\), producing exact joins and the common \(h_E\), rather than promoting independent cell fixtures.

3. **Common \(h_E\) → four regular cycles.**  
   Its three square arcs per directed opposite-cell direction are explicitly removed in S1:383–391. Its one singleton occurrence per physical vertex is separately removed in S1:406.

4. **Directed bounds → family exclusions.**  
   The four direction-specific residual counts feed the cross-sum bound and only then the run-sum exclusions at S1:412–460. Direction reversal in the second alternating family is retained.

5. **Vertex identity → final compatibility obligation.**  
   S1:398–408 concerns each actual vertex. S1:517 requires those identities in the surviving labeled collection; it does not substitute a cell-total condition.

6. **One-row examples → no global witness claim.**  
   S1:506 explicitly prevents their promotion to five compatible residual cycles, six compatible alternating cycles, or an actual T2(11).

7. **Necessary constraints → exact remaining problem.**  
   S1:510–529 retains both complete decompositions across the same actual Hamilton cycles. It expressly leaves their simultaneous realization or exclusion unpaid.

Conversely, eleven actual Hamilton cycles partitioning both directed edges and directed square edges yield the required original linear adjacency and distance-two injectivity after removing infinity. The finite square partition splits into the 99 original distance-two events and eleven closing arcs, making the latter precisely the missing set. The conditional formulation therefore does not lose the actual-row requirement.

## 5. Acceptance boundary

Supported under the explicit hypotheses:

- an actual T2(11);
- \(M=C\);
- two distinct tripled six-symbol odd-position supports;

are the synchronized \(T=13,14\) structures, their directed budgets, their vertexwise coupling, and the stated nested run-sum exclusions.

Still **INCONCLUSIVE**:

- realization or exclusion of all surviving \(T=13\) collections;
- realization or exclusion of all surviving \(T=14\) collections;
- universal \(M=C\);
- branches with one or no tripled support;
- unrestricted T2(11) existence or nonexistence.

No independent-family, human, kernel/formal, novelty, priority, current-literature-completeness, or external-source-equivalence certification is supplied by this review.

**Overall correctness:** correct at the frozen conditional scope.

**Explanation:** The new claims follow from the actual Hamilton and square decompositions with the same residual-cycle and physical-vertex indices retained. The manuscript correctly stops at necessary constraints and explicitly leaves complete conditional compatibility and the unrestricted original target unproved.

**Confidence:** 0.96.