# Author candidate v1: joint directed-arc closure constraints for the conditional two-tripled-support T2(11) branch

**Intended artifact:** `f489-actual-tuscan11-conditional-two-tripled-support-residual-closure-frontier/author-candidate-v1.md`

**Status:** AUTHOR-WRITTEN CANDIDATE; not independently reviewed or parent-adopted. The two entire branches \(T=13\) and \(T=14\) are **not fully excluded**. No eleven-row witness is constructed.

The result is a stronger joint restriction on the **same five residual Hamilton cycles**, not a collection of independently feasible cell layouts. In particular:

- In the \(T=13\) branch, every residual cycle has exactly one adjacency joining \(I\) to \(L\) and exactly one joining \(J\) to \(K\).
- In the \(T=14\) branch, all four all-singleton cell layouts must occur in **one and the same residual cycle**. That cycle is an actual Hamilton cycle alternating across \(E=B\triangle D\).
- Consequently,
  \[
  \boxed{T=13\iff k_E=0,\qquad T=14\iff k_E=1}
  \]
  within the stated conditional branch.
- The remaining cycles admit only the synchronized full-run incidence patterns described below.
- Directed square-arc budgets impose additional orientation bounds. These exclude, in particular, the \(T=14\) subbranches in which either three-cycle alternating family has other-cut run sum nine.

These are conditional actual-row exclusions. They do not establish universal \(M=C\), unrestricted T2(11) nonexistence, or existence of the surviving configurations.

## 1. Scope, inputs, and execution status

The target remains eleven permutation rows on the same eleven symbols, with all \(110\) directed linear adjacency events distinct and all \(99\) original directed distance-two events distinct.

The hypotheses for the new conclusions are:

1. the rows form an actual T2(11);
2. the missing directed distance-two set \(M\) equals the actual last-to-first closing set \(C\);
3. two distinct six-symbol odd-position supports \(B,D\) each occur in three rows.

Other tripled supports are not assumed absent.

Before reading the mathematical packet, I read the complete manifest, freeze receipt, parent live-metadata supply, and all ten permission/status controls. I sent the direct pre-body ACK before opening the packet. I then read packet lines \(1\)–\(723\), in ordered exact ranges of at most twenty lines, through the endings of:

- S1, labels \(1\)–\(670\): the fresh, unreviewed f461 author body;
- S2, labels \(1\)–\(29\): the adopted singleton-budget disposition;
- S3, labels \(1\)–\(22\): the adjacency/closing-pair disposition.

The supplied manifest SHA256 is  
`3bc0d06fdc0864257dd8b29cc5f8460db5a062c621e74efa1e987f0571601c27`.

The supplied receipt SHA256 is  
`32977600b7e6d4dc7d4d13059454392a1cfba56896e646758a6ff9a01944a990`.

The parent-reported packet SHA256 is  
`aa26d027d985944b5d5e39fcdf92fed2195f8f3c09823407296b319a69b09817`.

The clock **2026-10-30T12:17:35-0700 PDT**, hash matches, byte counts, and LF counts are attributed to the parent’s metadata supply. I did not independently execute a clock, hashing command, or packet reconstruction. S1’s metadata records \(669\) LF characters while the literal packet displays source labels through \(670\); my coverage statement concerns those displayed labels.

After completing the packet, I developed the written arguments below, inspected the public actual-row definition cited in Section 10, and completed the derivations. The relevant S1 results are reconstructed below rather than accepted merely because they appear in that unreviewed input.

**Scientific execution: NOTRUN.** No executable calculation, solver, CAS, finite search, build, test, linter, formatter, installation, remote computation, or external-model CLI was run. No scientific program or machine output is omitted. The calculations below are written proofs and explicitly displayed one-row examples.

The runtime read-only boundary also prevented repository materialization; this is the complete body for Main to materialize. No execution or file-write bypass was used. Held scientific payloads and their excluded consumers were not opened. This is a factual read/use disclosure, not a cognitive-isolation certificate.

## 2. Actual Hamilton cycles and their squares

Let \(S\) be the eleven-symbol set and \(X=S\cup\{\infty\}\). An actual row
\[
r=(r_1,\ldots,r_{11})
\]
gives the actual directed Hamilton cycle
\[
h_r=(\infty,r_1,\ldots,r_{11}).
\]

Adjacency exhaustion forces each symbol to occur first exactly once and last exactly once. Indeed, a symbol has ten possible outgoing adjacency targets, and its number of outgoing adjacency occurrences is eleven minus its last-column multiplicity. The incoming argument is dual.

Thus the eleven actual cycles partition all directed edges of the complete loopless digraph on \(X\).

The finite edges of their squares \(h_r^2\) consist of:

- the \(99\) original linear distance-two events;
- the eleven closing pairs \(r_{11}\to r_1\).

Under the additional hypothesis \(M=C\), these partition all \(110\) finite ordered pairs.

The remaining square edges are
\[
\infty\to r_2,\qquad r_{10}\to\infty.
\]
For a finite symbol, its number of missing outgoing distance-two targets equals its penultimate-column multiplicity; the missing incoming count equals its second-column multiplicity. Since \(C\) has indegree and outdegree one, \(M=C\) makes both those columns permutations.

Consequently,
\[
\boxed{\{h_r^2:r\text{ an actual row}\}
\text{ partitions every directed edge on }X.}
\tag{1}
\]

The cycles \(h_r\) remain Hamilton cycles throughout. Their squares, each comprising two six-cycles, are used only as consequences of the actual rows.

## 3. Reconstructing saturation and the four three-vertex cells

For a finite set \(A\subseteq S\), put \(b=|A|\). In one linear row, let \(q\) count black runs, \(s\) singleton black runs including boundary runs, and \(t\) internal singleton white runs. Its original black-to-black distance-two count is
\[
d=b-2q+s+t.
\]

Adjacency exhaustion gives
\[
\sum_r q=b(12-b).
\]
If \(\mu_A=|M\cap A^2|\), distance-two injectivity gives
\[
\sum_r d=b(b-1)-\mu_A.
\]
Hence the total number of finite singleton vertices is
\[
W_A=b(12-b)-\mu_A.
\]

The added vertex \(\infty\) is a singleton precisely when both row endpoints lie in \(A\). Writing \(\nu_A=|C\cap A^2|\), the total including \(\infty\) is therefore
\[
W_A+\nu_A.
\]
Under \(M=C\),
\[
\boxed{\sum_r S_A(h_r)=b(12-b).}
\tag{2}
\]

Complementing a coloring preserves singleton status, so this also treats cuts whose named side contains \(\infty\).

For a six-plus-six cut the budget is \(36\). Each alternating cycle contributes twelve. Therefore three alternating cycles saturate the budget:

> Every other actual Hamilton cycle has no singleton for that cut.

Let \(\mathcal A_B,\mathcal A_D\) be the two three-cycle alternating families. They are disjoint: a connected Hamilton cycle has a unique alternating bipartition, up to complement, and the distinct finite supports \(B,D\) cannot be complements on \(X\).

### Intersection reconstruction

If \(|B\cap D|=5\), the two colorings differ at two vertices. Changing those colors can affect singleton status only at those vertices and their neighbors, at most six vertices. A \(B\)-alternating cycle therefore retains at least six \(D\)-singletons, contradicting saturation for \(D\).

If the intersection has size one, complement the \(D\)-cut; the same two-change argument applies.

If the intersection has size four, define
\[
I=B\cap D,\quad J=B\setminus D,\quad
K=D\setminus B,\quad L=X\setminus(B\cup D).
\]
Then \(|I|=|L|=4\) and \(|J|=|K|=2\).

In a \(B\)-alternating cycle, every \(D\)-run has length at least two. Its six \(D\)-vertices comprise four \(I\)-vertices and two \(K\)-vertices. There can be neither one run of length six nor three runs of length two, since either would contain three vertices of each \(B\)-color. The two runs must consequently be
\[
I\,K\,I,\qquad I\,K\,I.
\]
The complementary runs are \(L\,J\,L\). In particular, these cycles have no \(J\)-\(K\) adjacency. The same is true of the \(D\)-alternating family.

All eight directed \(J\)-\(K\) arcs would therefore have to occur in the five remaining cycles. At a \(J\)-\(K\) adjacency in one of those cycles, avoiding singletons for both cuts forces the other neighbor of its \(J\)-endpoint into \(J\), and the other neighbor of its \(K\)-endpoint into \(K\).

Thus the adjacency joins the unique two-vertex \(J\)-run to the unique two-vertex \(K\)-run. There can be at most one such join in a Hamilton cycle; a second would close a four-vertex component. Each join consumes an internal directed \(J\)-arc, of which only two exist across the decomposition. Eight required joins are impossible.

Intersection two reduces to intersection four by complementing the \(D\)-cut. Therefore
\[
\boxed{|B\cap D|=3.}
\tag{3}
\]

Henceforth \(I,J,K,L\) all have size three. Let \(\mathcal R\) be the same five actual cycles outside the two alternating families.

Record the four cells by their \(B,D\) membership bits:
\[
I=11,\quad J=10,\quad K=01,\quad L=00.
\]
Call a cross-cell adjacency **diagonal** if it joins \(I,L\) or \(J,K\), changing both bits. Other cross-cell adjacencies change one bit.

Every cycle of \(\mathcal R\) has no singleton for either bit.

## 4. A directed-square reconstruction of the two local ledgers

Define
\[
T=\sum_{h\in\mathcal A_B}r_D(h)
 +\sum_{h\in\mathcal A_D}r_B(h),
\]
where \(r_A\) counts runs of one color on the cycle.

For one cell \(Q\), let \(g_Q,p_Q,q_Q\) count its layouts across \(\mathcal R\):

- one full run of length three;
- a pair run and one singleton;
- three singleton runs.

All six internal directed adjacency arcs of \(Q\) occur in \(\mathcal R\), because an alternating-family edge cannot stay inside a cell. Thus
\[
g_Q+p_Q+q_Q=5,\qquad 2g_Q+p_Q=6.
\tag{4}
\]

There is also an exact square-arc count.

In a residual cycle, a square edge with both endpoints in \(Q\) must have its middle vertex in \(Q\): otherwise that middle vertex would be a singleton for a changed bit. Thus residual internal square arcs of \(Q\) correspond exactly to its full three-vertex runs, one per run.

Now take \(h\in\mathcal A_B\), with \(r_D(h)=j\). Each \(D\)-run has length at least two and alternates between \(I,K\), or between \(J,L\). Each of its \(j\) runs of either \(D\)-color contains both relevant cells. The square arcs internal to any one cell consequently number
\[
3-j.
\]
The analogous statement holds in \(\mathcal A_D\).

By the complete square decomposition (1),
\[
6=(18-T)+g_Q,
\]
so
\[
\boxed{g_Q=T-12\quad\text{for every cell }Q.}
\tag{5}
\]

Equations (4) give \(p_Q=6-2g_Q\) and \(q_Q=g_Q-1\), initially allowing \(g_Q=1,2,3\).

The value three is impossible: it would partition the complete directed graph on three vertices into three directed Hamilton paths. Incoming and outgoing degrees would force each vertex to start one path and end one path. Naming one path \(a,b,c\), the path starting at \(b\) must then be \(b,a,c\); the remaining arcs \(c\to a,c\to b\) do not form a path.

Thus the reconstructed alternatives are exactly
\[
\begin{array}{c|ccc}
T&g_Q&p_Q&q_Q\\ \hline
13&1&4&0\\
14&2&2&1.
\end{array}
\tag{6}
\]

No acceptance of S1’s unreviewed conclusion is needed for this reconstruction.

## 5. New joint diagonal-adjacency saturation

### Lemma: residual capacity is one per opposite-cell pair per cycle

A diagonal adjacency in a residual cycle forces the other neighbor of each endpoint into that endpoint’s own cell. Both endpoints therefore belong to nontrivial cell runs.

By (6), each cell has at most one nontrivial run in a residual cycle. Two diagonal joins between the same opposite-cell pair would connect both ends of those two runs and close a component, contradicting Hamiltonicity.

Therefore
\[
\boxed{\text{Each }h\in\mathcal R
\text{ has at most one }I\text{-}L\text{ join
and at most one }J\text{-}K\text{ join.}}
\tag{7}
\]

### Lemma: each opposite-cell pair needs \(18-T\) residual joins

For a \(B\)-alternating cycle, let \(a\) count \(I\to L\) and \(b\) count \(L\to I\). Cell indegree/outdegree balance forces the counts of \(J\to K\) and \(K\to J\) to be \(a,b\), respectively. All \(D\)-crossing edges are diagonal, so
\[
r_D(h)=a+b.
\]
Thus each undirected opposite-cell pair receives exactly \(r_D(h)\) directed adjacency occurrences in that cycle. The \(D\)-alternating argument is identical.

There are eighteen possible directed arcs between either opposite-cell pair. Hence
\[
\boxed{\text{Residual joins between either opposite-cell pair}=18-T.}
\tag{8}
\]

### Theorem A: exact \(T=13\) joins

For \(T=13\), equation (8) requires five joins for each opposite-cell pair. Equation (7) provides capacity five over the same five cycles. Therefore every residual cycle has exactly one join of each kind.

This rules out every \(T=13\) assignment of the input’s local cell ledgers in which any residual cycle lacks either diagonal join.

### Theorem B: synchronized \(T=14\) all-singleton layouts

For \(T=14\), each cell has one all-singleton cycle. Suppose the all-singleton cycles for \(I\) and \(L\) were different. A diagonal join requires both cells to have nontrivial runs, leaving only three possible cycles, whereas (8) requires four joins. Therefore their all-singleton cycles coincide. The same holds for \(J,K\).

In the common all-singleton cycle of \(I,L\), all six vertices in \(I\cup L\) have both neighbors in \(J\cup K\). Same-cell neighbors are absent, and diagonal neighbors would force nontrivial runs. These six vertices account for twelve cross-cut incidences, exhausting the twelve cycle edges. The cycle therefore alternates between \(I\cup L\) and \(J\cup K\).

It follows that \(J,K\) are also all-singleton there. Thus:

\[
\boxed{\text{All four }q_Q=1\text{ layouts occur in one common cycle }h_E.}
\tag{9}
\]

This cycle alternates across
\[
E=J\cup K=B\triangle D.
\]
Because it has no \(B\)- or \(D\)-singleton, its cell sequence follows one of the two directed orientations of
\[
I-J-L-K-I,
\]
three times. It is the original twelve-vertex Hamilton cycle, not three disconnected four-cycles.

The other four residual cycles each have exactly one join between each opposite-cell pair, again by (7)–(8).

### Exact symmetric-difference multiplicity

Since \(\infty\in L\), the finite odd-position support of \(h_E\) is exactly \(E\).

In \(T=13\), every residual cycle has diagonal edges and therefore cannot alternate across \(E\). The two other alternating families cannot alternate across this distinct cut either.

In \(T=14\), the common all-singleton cycle is \(E\)-alternating, while every other residual cycle has diagonal edges.

Consequently,
\[
\boxed{k_E=0\text{ in }T=13,\qquad k_E=1\text{ in }T=14.}
\tag{10}
\]

This strengthens S1’s upper bound \(k_E\le1\).

## 6. New synchronized full-run incidence patterns

Call the five \(T=13\) residual cycles, or the four \(T=14\) residual cycles other than \(h_E\), **regular residual cycles**.

Every cell in a regular residual cycle has exactly one nontrivial run, and each opposite-cell pair has exactly one diagonal join. Joining the two nontrivial runs across that diagonal produces:

- one contiguous block in \(I\cup L\);
- one contiguous block in \(J\cup K\).

Everything outside those two blocks is a singleton cell vertex. At such a vertex the two neighboring cells differ in different bits, so both incident edges cross the \(E\)-cut.

The two gaps between the blocks therefore consist of alternating \(E\)-colors. Their endpoint blocks have opposite \(E\)-colors, so each gap contains an **even** number of singleton vertices, equally many from each \(E\)-side.

Let \(f(h)\) count full three-vertex cell runs in a regular residual cycle. The number of singleton cell vertices is \(4-f(h)\). Equal singleton counts on the two \(E\)-sides imply
\[
\boxed{\#\text{ full cells in }\{I,L\}
=\#\text{ full cells in }\{J,K\}.}
\tag{11}
\]
In particular,
\[
\boxed{f(h)\in\{0,2,4\}.}
\tag{12}
\]

When \(f(h)=2\), the two full cells must be adjacent in the cell square, not opposite.

### \(T=13\)

Every cell is full once, so \(\sum_{h\in\mathcal R}f(h)=4\). The only possibilities, up to row order, are
\[
\boxed{(4,0,0,0,0)\quad\text{or}\quad(2,2,0,0,0).}
\tag{13}
\]

In the second case, the two full-cell sets partition the four cells into opposite edges of the cell square.

### \(T=14\)

Among the four regular residual cycles, every cell is full twice. Hence
\[
\boxed{(f(h))=(4,4,0,0),\quad(4,2,2,0),\quad\text{or }(2,2,2,2).}
\tag{14}
\]

In the middle case, the two two-cell sets again form an opposite-edge matching.

In the last case, regard each full-cell set as an edge of the cell square. Each cell has incidence two. The four cyclic edge multiplicities are therefore
\[
(x,\,2-x,\,x,\,2-x),\qquad x\in\{0,1,2\}.
\tag{15}
\]

These restrictions concern simultaneous layouts on the same cycles. They are stronger than four separate copies of the local table (6).

## 7. Directed square-arc and endpoint constraints

Let \(a\) count residual adjacency arcs \(I\to L\), and let \(a'\) count \(L\to I\).

Neither alternating family can contribute a square arc between opposite cells: a \(B\)-alternating cycle’s square preserves \(B\), and a \(D\)-alternating cycle’s square preserves \(D\). All nine square arcs in each directed opposite-cell direction must therefore occur in \(\mathcal R\).

In a residual cycle a directed diagonal square event has exactly two possible forms:

1. a diagonal adjacency, with an internal cell edge before or after it;
2. two different one-bit changes at a singleton cell vertex.

Every diagonal adjacency \(I\to L\) contributes exactly two square arcs \(I\to L\). Thus
\[
9=2a+u,\qquad 9=2a'+u',
\tag{16}
\]
where \(u,u'\) count the appropriately oriented singleton events centered in \(J\) or \(K\).

For \(T=13\), \(a+a'=5\). Nonnegativity in both equations yields
\[
\boxed{1\le a,a'\le4.}
\tag{17}
\]

For \(T=14\), the cycle \(h_E\) contributes three square arcs in each directed opposite-cell direction. Removing that contribution gives
\[
6=2a+u_{\rm reg},\qquad
6=2a'+u'_{\rm reg},\qquad a+a'=4,
\]
and therefore
\[
\boxed{1\le a,a'\le3.}
\tag{18}
\]

The same bounds hold for the two \(J,K\) directions. In particular, neither opposite-cell pair can have every residual join oriented the same way.

### Vertexwise endpoint identity

For \(x\) in a cell, let \(m_x\) count full residual cell runs in which \(x\) is the middle vertex.

Across the five residual cycles, \(x\) has exactly two internal incoming and two internal outgoing adjacency occurrences. Its number of occurrences with at least one internal neighbor is therefore \(4-m_x\). Hence its singleton-cell occurrences number
\[
\boxed{1+m_x.}
\tag{19}
\]

For \(T=14\), one of these is in \(h_E\); among the four regular residual cycles the count is exactly \(m_x\).

Thus full-run middle choices and singleton endpoint choices cannot be assigned independently.

### Alternating-family orientation ledger

Let \(x,y\) be the totals of \(I\to L,L\to I\) in \(\mathcal A_B\), and \(u,v\) the corresponding totals in \(\mathcal A_D\). Cell balance gives
\[
\begin{aligned}
a_{IL}&=9-x-u,&a_{LI}&=9-y-v,\\
a_{JK}&=9-x-v,&a_{KJ}&=9-y-u,
\end{aligned}
\]
with
\[
x+y+u+v=T.
\]

Equations (17)–(18) imply that all four cross sums
\[
x+u,\quad x+v,\quad y+u,\quad y+v
\]
lie in
\[
\boxed{[T-8,\,8].}
\tag{20}
\]
Equivalently, one useful bound is
\[
\boxed{\max(x,y)+\max(u,v)\le8.}
\tag{21}
\]

### Explicitly excluded \(T=14\) subbranches

Suppose all three \(B\)-alternating cycles have \(r_D=3\). Every \(D\)-run then has length two. Their cell words follow
\[
I\,K\,J\,L
\quad\text{or its reverse, repeated three times.}
\]
Each such cycle contributes either \((3,0)\) or \((0,3)\) to its two directed \(I,L\) counts.

Consequently \(x+y=9\) and \(\max(x,y)\ge6\). In \(T=14\), the other family has \(u+v=5\), so \(\max(u,v)\ge3\), contradicting (21).

Therefore
\[
\boxed{
T=14\Longrightarrow
\left(\sum_{\mathcal A_B}r_D,\sum_{\mathcal A_D}r_B\right)
\in\{(6,8),(7,7),(8,6)\}.
}
\tag{22}
\]

This fully excludes the nested run-sum branches \((9,5)\) and \((5,9)\).

As another consequence, if the six other-cut run numbers in \(T=14\) are \(1,1,3,3,3,3\), the two run-one cycles must belong to different alternating families. Each family then has run multiset \(1,3,3\), and its directed diagonal totals must be \(3,4\) in some order.

For comparison, \(T=13\) does not give the same exclusion. If one family has run sum nine, (21) forces its directed totals to be \(3,6\), while the other family’s totals are \(2,2\). This is a restriction, not a contradiction.

## 8. Physical one-row nonvacuity checks

Use the same actual symbol cells
\[
I=\{1,2,3\},\quad J=\{4,5,6\},\quad
K=\{7,8,9\},\quad L=\{\infty,10,11\}.
\]

The following are full eleven-symbol permutation rows. Their augmented cycles give individual realizations of the regular-cycle structures:

| \(f(h)\) | Actual row |
|---|---|
| 4 | \((10,11,1,2,3,4,5,6,7,8,9)\) |
| 2 | \((10,1,2,3,7,11,4,5,6,8,9)\) |
| 0 | \((10,4,3,7,11,5,6,8,9,1,2)\) |

The first has cyclic cell runs \(L^3I^3J^3K^3\).

The second has cyclic cell word
\[
L\,L\,I\,I\,I\,K\,L\,J\,J\,J\,K\,K.
\]
Its singleton \(K,L\) vertices have neighbors in different one-bit directions.

For the third, starting its augmented cycle at symbol \(1\) gives cell word
\[
I\,I\,L\,L\,J\,I\,K\,L\,J\,J\,K\,K.
\]
Its four singleton cells occur along a four-singleton gap. In each example there is one \(I,L\) diagonal join, one \(J,K\) diagonal join, and no singleton for either original cut.

An actual row realizing the common all-singleton structure is
\[
(4,1,7,10,5,2,8,11,6,3,9).
\]
Its augmented cell sequence is
\[
L\,J\,I\,K\,L\,J\,I\,K\,L\,J\,I\,K,
\]
and its odd-position support is exactly \(J\cup K\).

These are written checks of individual actual Hamilton rows. They do **not** establish five jointly compatible residual cycles, six compatible alternating cycles, or a T2(11). No disconnected cycle cover is offered as a witness, and no unrelated-order example is used to establish order-eleven nonvacuity.

## 9. Exact residual problem and unpaid step

A surviving actual conditional candidate must now realize simultaneously:

1. the same twelve vertices and the same two three-cycle alternating families;
2. the \(T=13\) structure (13), or the \(T=14\) common \(E\)-alternating cycle and structure (14)–(15);
3. all internal cell arcs exactly once;
4. one join for each opposite-cell pair in every regular residual cycle;
5. the directed orientation restrictions (16)–(22);
6. the vertexwise endpoint identities (19);
7. all \(132\) directed adjacency arcs exactly once across the actual Hamilton cycles;
8. all \(132\) directed square arcs exactly once across those same cycles.

Conversely, actual Hamilton cycles satisfying the two complete decompositions, with \(\infty\) removed, yield distinct original adjacency and distance-two events; the finite square decomposition makes their closing pairs precisely the missing distance-two pairs. Thus the final Hamilton-and-square compatibility requirement is an exact conditional formulation, not a replacement by independent cycle covers.

The **first unproved step** is to exclude or realize the remaining labeled Hamilton collections within these synchronized templates while enforcing both decompositions. In particular, I have not proved incompatible:

- the \(T=13\) patterns \((4,0,0,0,0)\) and \((2,2,0,0,0)\);
- the surviving \(T=14\) patterns (14), together with one actual common \(E\)-alternating cycle;
- the alternating-family run-sum allocations remaining after (22).

No full \(T=13\) or \(T=14\) exclusion follows merely from the necessary conditions displayed here.

For the unrestricted original problem, branches with \(M\ne C\), one tripled support, or no tripled support remain outside this conditional argument.

## 10. Attribution and final disposition

The inspected actual-row definition is Christopher D. Rosin, *Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems*, arXiv:2505.23881v1, Table 6:

https://arxiv.org/html/2505.23881v1#A1.T6

It specifies exactly one linear adjacency row for each ordered distinct pair and at most one linear distance-two row. I inspected the opening material and the exact definition passage, not the full paper. No current-literature completeness, novelty, or priority claim is made.

**Completed deliverable:** a self-contained author-written reconstruction of the conditional two-support ledger, followed by new common-cycle diagonal saturation, all-singleton synchronization, full-run incidence restrictions, directed square-arc bounds, endpoint identities, and explicit exclusion of the \(T=14\) run-sum-\(9\) subbranches.

**Original-target status:** NOT_PROVED. No eleven-row witness, full conditional branch closure, unrestricted no-go, independent-family review, human review, parent mathematical acceptance, or formal/kernel verification is claimed.