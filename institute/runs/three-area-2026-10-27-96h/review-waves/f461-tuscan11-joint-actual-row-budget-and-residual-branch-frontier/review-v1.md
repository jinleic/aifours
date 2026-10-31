# Author candidate v1: joint cut restrictions for actual T2(11)

**Intended artifact:** `f461-tuscan11-joint-actual-row-budget-and-residual-branch-frontier/author-candidate-v1.md`

**Status:** AUTHOR CANDIDATE — complete written arguments, not independently reviewed or parent-adopted. No actual T2(11) witness or unrestricted nonexistence proof is claimed.

## 1. Results and relation to the original target

An actual T2(11) consists of eleven permutation rows on the same eleven symbols, with all 110 directed adjacency events distinct and all 99 original directed distance-two events distinct.

This manuscript establishes the following additional necessary conditions.

### Unconditional overlap-budget theorem

For every six-symbol set \(B\), let \(N_t(B)\) count the actual rows whose odd-position support intersects \(B\) in exactly \(t\) symbols. Let \(\mu_B\) count missing directed distance-two pairs internal to \(B\). Then

\[
\boxed{11N_6(B)+5N_5(B)+6N_1(B)\le 36-\mu_B.}
\]

Consequently:

- If three rows have odd-position support \(B\), every other support intersects \(B\) in **two, three, or four** symbols.
- If two rows have support \(B\), at most two rows in the entire array have supports intersecting \(B\) in one or five symbols.

The row-wise coefficients \(11,5,6\), and the zero lower bounds for intersection sizes two, three, and four, are sharp for actual eleven-symbol permutation rows.

### Additional results in the explicitly conditional \(M=C\) branch

Here \(M\) is the missing directed distance-two set and \(C\) is the actual set of last-to-first closing pairs. Equality \(M=C\) is an additional hypothesis, not a universal identity.

Suppose two distinct supports \(B,D\) each occur in three actual rows. Then:

1. Their intersection must have size exactly three:
   \[
   \boxed{|B\cap D|=3.}
   \]

2. Consider the three \(B\)-alternating augmented Hamilton cycles and the three \(D\)-alternating cycles. Let
   \[
   T=
   \sum_{\text{\(B\)-alternating }h}r_D(h)
   +
   \sum_{\text{\(D\)-alternating }h}r_B(h),
   \]
   where \(r_A(h)\) is the number of monochromatic \(A\)-runs on the cycle. Then
   \[
   \boxed{T\in\{13,14\}.}
   \]

3. Partition the twelve augmented vertices into
   \[
   I=B\cap D,\quad J=B\setminus D,\quad
   K=D\setminus B,\quad L=X\setminus(B\cup D).
   \]
   Each cell has three vertices. Among the five cycles outside the two alternating families, each cell has the following exact run-layout counts:

   | \(T\) | One run of length 3 | Runs of lengths \(2+1\) | Three singleton runs |
   |---|---:|---:|---:|
   | 13 | 1 | 4 | 0 |
   | 14 | 2 | 2 | 1 |

   The same row of this table applies to **all four cells**.

4. The six-symbol symmetric difference can occur as an odd-position support in at most one row:
   \[
   \boxed{k_{B\triangle D}\le1.}
   \]

5. If three distinct supports each occur three times, their pairwise intersections are three and their triple intersection is one or two.

These exclude additional whole actual-row branches. They do **not** exclude the branch with only one tripled support, all branches with multiplicities at most two, or the remaining configurations satisfying the conditions above.

## 2. Input audit, method boundary, and chronology

### 2.1 Frozen records

I read the complete manifest, freeze receipt, parent dispatch receipt, and parent live-metadata supply.

Assigned manifest SHA256:

`9b9f4c917cdd8585019865ad8eea424112bdf476b0bcd7e40b983bcb1ea3bc05`

Assigned receipt SHA256:

`b393d314e91fd36a80328df9ab9cf03fd91c1159fb6d2afa02fb9f472fc4c391`

Parent-reported packet SHA256:

`c4db4d5a882fbdc088f93fe5c31ddf72ab9bb1e9b3b78cb8c52aceaa6b22a9e9`

The parent reports matching assigned hashes, byte counts, and LF counts. I did **not** independently execute hashing commands or reproduce the packet byte-equality check.

The parent supplied clock observations of **2026-10-30T11:43:56-0700 PDT** and **2026-10-30T11:59:20-0700 PDT**. These are parent-attributed metadata, not my native start, completion, arithmetic, or execution timestamps.

### 2.2 Controls before scientific body

Before reading the scientific packet, I read all ten listed permission/status controls in full:

- prospective author-method restoration;
- owner frontier-first addendum;
- L1 selected-diagnostic quarantine;
- privacy auxiliary-parameter quarantine;
- CORE auxiliary-operator quarantine;
- AME held-consumer quarantine;
- PH held-registration/report-consumer quarantine;
- F439, F444, and F448 selected-diagnostic quarantines.

Those records were used for status and permission boundaries only. Their held scientific episodes and consumers were not used.

### 2.3 Complete packet coverage

I read the ordered literal packet through its ending, packet lines 1–626, including:

- S1, source lines 1–29;
- S2, source labels 1–548;
- S3, source lines 1–25;
- S4, source lines 1–22.

The parent metadata reports 547 LF characters for S2, while the packet labels 548 logical source lines. My coverage statement is that I read through the displayed final label `S2|548`, not that I independently counted source bytes.

I use S2’s common-support conclusion only at the precise scope stated in S1: four shared-support rows are excluded; three shared-support rows remain live. S2’s final “closes the common-support family completely” sentence is not interpreted as excluding the remaining three-row branch.

### 2.4 Research chronology and execution

After the complete packet read, I developed fresh written joint-cut arguments. Public-source inspection and further written derivations were interleaved. The concrete row examples below were considered under this **GENERAL AUTHOR** permission, not under a WRITTEN-only review duty.

No scientific executable, solver, CAS, search campaign, test, build, linter, formatter, installation, remote scientific computation, or external-model CLI was run. All calculations below are displayed mathematical arguments, not machine output.

The active tool role forbids repository edits and restricts shell use. Repository materialization was therefore not attempted; this is the complete body for Main to materialize. No file-write or execution bypass was used.

No held scientific payload, linked held consumer, or sibling current scientific return was opened. This records the observable read frontier, not a cognitive-isolation certificate.

## 3. Actual rows, closing pairs, and singleton counts

Let \(S\) be the eleven-symbol set. For a row

\[
r=(r_1,\ldots,r_{11}),
\]

write

\[
O(r)=\{r_1,r_3,r_5,r_7,r_9,r_{11}\}.
\]

Adjoin the same vertex \(\infty\) to every actual row, obtaining its actual directed Hamilton cycle

\[
h_r=(\infty,r_1,\ldots,r_{11})
\]

on \(X=S\cup\{\infty\}\).

Adjacency exhaustion implies that every symbol is first in exactly one row and last in exactly one row. Thus the eleven \(h_r\) partition all directed edges of the complete loopless digraph on \(X\).

Let

\[
C=\{(r_{11},r_1):r\text{ is an actual row}\}.
\]

Its pairs are distinct. Let \(M\) be the eleven missing ordered distance-two pairs.

For \(A\subseteq S\), color \(A\) black and \(X\setminus A\) white. A cycle vertex is a singleton if both of its neighbors have the opposite color.

Define:

- \(w_A(r)\): the number of finite singleton vertices on \(h_r\);
- \(S_A(h_r)\): the number of singleton vertices including \(\infty\);
- \(W_A=\sum_r w_A(r)\);
- \(\mu_A=|M\cap A^2|\);
- \(\nu_A=|C\cap A^2|\).

The singleton status of \(\infty\) is exactly the event that the row starts and ends in \(A\). Therefore

\[
\sum_r S_A(h_r)=W_A+\nu_A. \tag{1}
\]

For completeness, the exact finite singleton identity can be reconstructed directly.

For one linear row, let \(q\) count black runs, \(s\) singleton black runs including boundaries, and \(t\) internal singleton white runs. The number \(d\) of original black-to-black distance-two events satisfies

\[
d=|A|-2q+s+t.
\]

Across all eleven rows, exhausted black-to-black adjacency gives

\[
\sum_r q=|A|(12-|A|).
\]

Distance-two injectivity gives

\[
\sum_r d=|A|(|A|-1)-\mu_A.
\]

Combining these equations yields

\[
\boxed{W_A=|A|(12-|A|)-\mu_A.} \tag{2}
\]

In particular, for \(|A|=6\),

\[
W_A=36-\mu_A\le36. \tag{3}
\]

The original distance-two events remain only \(r_i\to r_{i+2}\), \(1\le i\le9\). No uniqueness assumption has been inserted for augmented wrap events.

## 4. Sharp row-wise overlap bounds

### Lemma 1

Let \(r\) be any actual eleven-symbol permutation row and let \(D=O(r)\). For every six-symbol \(B\subseteq S\),

\[
w_B(r)\ge f(|B\cap D|),
\]

where

\[
\begin{array}{c|rrrrrr}
t&1&2&3&4&5&6\\ \hline
f(t)&6&0&0&0&5&11.
\end{array} \tag{4}
\]

Each entry is sharp at the individual-row level.

### Proof of the lower bounds

The cycle \(h_r\) alternates across the cut \(D\mid X\setminus D\), so all twelve vertices are singletons for that coloring.

If \(|B\cap D|=5\), the \(B\)-coloring is obtained by changing the colors of two finite vertices. A singleton status can change only at those two vertices and their cycle neighbors. This affects at most six vertices, and hence at most six finite vertices. At least

\[
11-6=5
\]

finite singletons remain.

If \(|B\cap D|=1\), consider \(X\setminus B\) instead of \(B\). Complementing the colors does not change singleton status. The cut \(X\setminus B\) differs from \(D\) exactly at \(\infty\) and the unique vertex in \(B\cap D\). Their closed neighborhoods affect at most six vertices, one of which is \(\infty\). At most five finite singleton statuses can therefore be lost, leaving at least

\[
11-5=6.
\]

If \(B=D\), all eleven finite vertices are singletons. For the remaining intersection sizes, nonnegativity supplies the stated lower bound. ∎

### Sharpness on full actual permutation rows

Take the actual row \(r=(1,2,\ldots,11)\), whose odd support is

\[
P=\{1,3,5,7,9,11\}.
\]

Direct run counts give:

| Cut \(B\) | \(|B\cap P|\) | \(w_B(r)\) |
|---|---:|---:|
| \(\{2,4,5,6,8,10\}\) | 1 | 6 |
| \(\{2,3,4,8,9,10\}\) | 2 | 0 |
| \(\{1,2,5,6,9,10\}\) | 3 | 0 |
| \(\{1,2,3,7,8,9\}\) | 4 | 0 |
| \(\{1,3,7,8,9,11\}\) | 5 | 5 |
| \(P\) | 6 | 11 |

For example, the intersection-five cut has singleton black runs at \(1,3,11\), and internal singleton white runs at \(2,10\), giving five. The intersection-one cut has three singleton black runs and three internal singleton white runs, giving six.

These are written counts in actual Hamiltonian rows. They establish sharpness of the row lemma, not existence of a compatible eleven-row array.

### Theorem 1: universal overlap budget

For every actual T2(11) and every six-symbol \(B\),

\[
\boxed{11N_6(B)+5N_5(B)+6N_1(B)\le36-\mu_B.} \tag{5}
\]

**Proof.** Sum Lemma 1 over the same eleven actual rows and apply (3). ∎

If \(N_6(B)=3\), only three units of finite singleton budget remain. Either an intersection-five row or an intersection-one row would exceed that remainder. Thus neither can occur.

If \(N_6(B)=2\), then

\[
5N_5(B)+6N_1(B)\le14-\mu_B\le14,
\]

so \(N_5(B)+N_1(B)\le2\).

No equality \(M=C\) has been used.

## 5. What the additional hypothesis \(M=C\) supplies

Under \(M=C\), equations (1) and (2) give, for every \(A\subseteq S\),

\[
\boxed{\sum_r S_A(h_r)=|A|(12-|A|).} \tag{6}
\]

For a six-symbol cut,

\[
\sum_r S_A(h_r)=36. \tag{7}
\]

A cycle alternating across this cut contributes twelve, not eleven, to (7). Hence three alternating cycles use the entire budget:

> **Saturation principle.** Under \(M=C\), if three actual rows have odd support \(A\), all other eight actual Hamilton cycles have no singleton vertices for this cut, including \(\infty\).

This is a statement about the same actual Hamilton cycles, not independent cycle covers.

There is also an exact square-decomposition interpretation. Under \(M=C\), the squares \(h_r^2\) partition all directed edges on \(X\). The finite square edges comprise the original distance-two events together with \(C=M\). The remaining square edges are \(\infty\to r_2\) and \(r_{10}\to\infty\).

Indeed, missing outdegree at a finite symbol equals its penultimate-column multiplicity; missing indegree equals its second-column multiplicity. Since \(C\) has indegree and outdegree one, those two columns are permutations when \(M=C\).

Each \(h_r^2\) consists of two six-cycles. These are auxiliary consequences of the actual rows; they are not substituted for the original Hamilton cycles in the arguments below.

## 6. Two tripled supports cannot intersect in two or four symbols

### Theorem 2

Suppose an actual T2(11) satisfies \(M=C\), and distinct supports \(B,D\) each occur three times. Then

\[
\boxed{|B\cap D|=3.} \tag{8}
\]

### Proof

Intersection sizes one and five are excluded by Theorem 1.

Suppose first that \(|B\cap D|=4\). Put

\[
I=B\cap D,\quad J=B\setminus D,\quad
K=D\setminus B,\quad L=X\setminus(B\cup D).
\]

Then

\[
|I|=|L|=4,\qquad |J|=|K|=2.
\]

The three \(B\)-alternating cycles and three \(D\)-alternating cycles are disjoint families. A Hamilton cycle has only one bipartition across which it alternates, up to complement; \(B,D\subseteq S\) are distinct and cannot be complements on \(X\).

Consider a \(B\)-alternating cycle. By saturation, it has no \(D\)-singletons. Its \(D\)-runs therefore all have length at least two.

There are six \(D\)-vertices, consisting of four vertices of \(I\) and two of \(K\). A single \(D\)-run of length six would contain three of each \(B\)-color, which is impossible. Three \(D\)-runs would all have length two, again containing three of each \(B\)-color.

There must consequently be two \(D\)-runs. To contain four \(I\)-vertices and two \(K\)-vertices while alternating in \(B\)-color, both must have form

\[
I\,K\,I.
\]

The complementary runs similarly have form

\[
L\,J\,L.
\]

In particular, this cycle has no adjacency between \(J\) and \(K\). The same argument with \(B,D\) interchanged applies to every \(D\)-alternating cycle.

Thus all eight ordered adjacency pairs between the two-element sets \(J,K\) must occur in the remaining five cycles. Each of those cycles has no singleton for either cut.

In such a remaining cycle, a \(J\)-vertex adjacent to a \(K\)-vertex must have its other neighbor in \(J\): avoiding a \(B\)-singleton requires that neighbor to lie in \(B\), and avoiding a \(D\)-singleton requires it to lie outside \(D\). Their intersection is \(J\). Similarly, the other neighbor of the \(K\)-vertex must lie in \(K\).

Hence any \(J\)-\(K\) adjacency forces a consecutive path through both vertices of \(J\) and both vertices of \(K\).

There can be at most one \(J\)-\(K\) adjacency in that Hamilton cycle. A second would close a four-vertex cycle, contradicting Hamiltonicity on twelve vertices.

Moreover, each such adjacency consumes one of the two directed internal \(J\)-arcs. Actual adjacency exhaustion therefore permits at most two \(J\)-\(K\) adjacencies over all remaining cycles, whereas eight are required. This is a contradiction.

If \(|B\cap D|=2\), complement the \(D\)-cut on \(X\). Its alternating family and singleton statuses are unchanged, while its intersection with \(B\) becomes four. The same argument applies. This complementation is only a relabeling of a cut, not an assertion that a support containing \(\infty\) is an original odd-position support.

The only remaining intersection size is three. ∎

## 7. A three-cut ledger for the surviving pair branch

Assume henceforth the hypotheses of Theorem 2. Thus all four cells

\[
I,\ J,\ K,\ L
\]

have size three.

Let \(\mathcal A_B,\mathcal A_D\) be the two three-cycle alternating families, and let \(\mathcal R\) be the other five actual Hamilton cycles.

Set

\[
E=B\triangle D=J\cup K.
\]

This is another six-symbol subset of \(S\).

Define

\[
T=
\sum_{h\in\mathcal A_B}r_D(h)
+
\sum_{h\in\mathcal A_D}r_B(h). \tag{9}
\]

### Lemma 2: contribution of the six alternating cycles

For \(h\in\mathcal A_B\),

\[
S_E(h)=12-4r_D(h). \tag{10}
\]

The analogous identity holds for \(h\in\mathcal A_D\).

**Proof.** Along a \(B\)-alternating cycle, the \(B\)-color changes at every edge. Since \(E\) is the exclusive-or of the \(B,D\) colors, an \(E\)-singleton occurs precisely when neither incident edge changes \(D\)-color.

The cycle has no \(D\)-singleton. All its \(2r_D(h)\) monochromatic \(D\)-runs have length at least two. The number of vertices internal to these runs is therefore

\[
12-2\bigl(2r_D(h)\bigr)=12-4r_D(h).
\]

These are exactly its \(E\)-singletons. ∎

Consequently,

\[
\sum_{h\in\mathcal A_B\cup\mathcal A_D}S_E(h)=72-4T. \tag{11}
\]

### Lemma 3: singleton interpretation on the remaining five cycles

For \(h\in\mathcal R\), an \(E\)-singleton is exactly a vertex that has neither cycle neighbor in its own cell \(I,J,K,L\).

**Proof.** Record each vertex by its two membership bits for \(B,D\). For either incident edge, record which bits change.

Since the vertex is not a singleton for \(B\) or \(D\), the change sets on its two incident edges are disjoint.

If one neighbor is in the same cell, that edge changes neither bit, so the vertex is not an \(E\)-singleton.

If neither neighbor is in the same cell, both change sets are nonempty. Two disjoint nonempty subsets of the two-bit set must be the two different singletons. Both edges therefore change exclusive-or color, making the vertex an \(E\)-singleton. ∎

For one three-vertex cell on a Hamilton cycle, its possible layouts are:

- one run of length three;
- one run of length two and one singleton;
- three singleton runs.

Let \(a\) count internal cell adjacency edges and let \(g\) indicate the first layout. Its number \(s\) of singleton cell vertices satisfies

\[
s=3-2a+g. \tag{12}
\]

This follows from the respective triples

\[
(a,g,s)=(2,1,0),\ (1,0,1),\ (0,0,3).
\]

The six cycles in the alternating families use no internal cell adjacency: every edge changes at least one of the two cut colors. All

\[
4\cdot3\cdot2=24
\]

directed internal cell arcs therefore occur in \(\mathcal R\).

Let \(G\) count full three-vertex cell runs over its five cycles and four cells. Summing (12), using Lemma 3, gives

\[
\sum_{h\in\mathcal R}S_E(h)
=5\cdot4\cdot3-2\cdot24+G
=12+G. \tag{13}
\]

The full \(E\)-singleton budget is 36. Equations (11) and (13) imply

\[
36=(72-4T)+(12+G),
\]

or

\[
\boxed{G=4T-48.} \tag{14}
\]

This couples three cuts on the same eleven actual Hamilton cycles.

## 8. The three-vertex path obstruction and exact frontier

For one cell, let \(g,p,q\) count its three layouts across \(\mathcal R\), in the order used above. Since all six directed internal arcs of that cell occur in these five cycles,

\[
g+p+q=5,\qquad 2g+p=6. \tag{15}
\]

Thus

\[
p=6-2g,\qquad q=g-1,
\]

and initially \(1\le g\le3\).

### Lemma 4

The complete loopless directed graph on three vertices cannot be partitioned into three directed Hamilton paths.

**Proof.** If such paths existed, incoming and outgoing counts would force each vertex to start exactly one path and end exactly one path.

Name one path \(a,b,c\). The path starting at \(b\) cannot use \(b\to c\), already used, so it must be \(b,a,c\). The two remaining arcs are \(c\to a\) and \(c\to b\), which cannot form a directed two-edge path. ∎

If \(g=3\), the three full cell runs would be exactly such a partition: they would use all six internal cell arcs. Therefore

\[
g\in\{1,2\}
\]

for every cell.

There are four cells, so \(4\le G\le8\). Equation (14) makes \(G\) a multiple of four. Consequently,

\[
G\in\{4,8\},\qquad T\in\{13,14\}. \tag{16}
\]

If \(G=4\), every cell has \(g=1\); if \(G=8\), every cell has \(g=2\). Equation (15) supplies the complete table.

### Theorem 3

Under the hypotheses of Theorem 2,

\[
\boxed{T\in\{13,14\},}
\]

and the exact cell-layout table in Section 1 holds.

Thus all pair branches with \(T\le12\) or \(T\ge15\) are impossible, as are nonuniform mixtures of the two cell-layout rows.

The proof uses directed adjacency exhaustion and the Hamiltonicity of the original cycles. In particular, the three-vertex path obstruction would not be available from a freely chosen disconnected cycle cover.

## 9. Symmetric-difference and three-support consequences

### Corollary 3.1

Under the hypotheses of Theorem 2,

\[
\boxed{k_{B\triangle D}\le1.}
\]

**Proof.** From (11) and the full singleton budget, the five remaining cycles have total \(E\)-singleton count

\[
36-(72-4T)=4T-36,
\]

which is 16 or 20.

Every cycle alternating across \(E\) contributes twelve. Such a cycle belongs to neither \(\mathcal A_B\) nor \(\mathcal A_D\), since these are distinct cuts of a connected Hamilton cycle. Two \(E\)-alternating cycles would require 24, exceeding either available total. ∎

### Corollary 3.2

Suppose three distinct supports \(B,D,F\) each occur three times in an actual T2(11) with \(M=C\). Then

\[
|B\cap D|=|B\cap F|=|D\cap F|=3
\]

and

\[
\boxed{|B\cap D\cap F|\in\{1,2\}.}
\]

**Proof.** Pairwise intersections follow from Theorem 2. Put \(t=|B\cap D\cap F|\). Inclusion-exclusion gives

\[
|B\cup D\cup F|=18-9+t=9+t\le11,
\]

so \(t\le2\).

If \(t=0\), the three elements of \(F\cap B\) exhaust \(B\setminus D\), and its three elements in \(D\) exhaust \(D\setminus B\). Hence \(F=B\triangle D\), contradicting Corollary 3.1 because \(F\) occurs three times. ∎

These conditions do not prove that a three-tripled-support configuration with triple intersection one or two is realizable.

## 10. Nonvacuity and limits of the examples

The sharpness table in Section 4 consists of full actual permutation rows and shows that the new universal overlap coefficients are not artifacts of an unattainable binary-word bound.

The run-number values used in Section 7 are also individually realizable on full actual rows. For \(r=(1,\ldots,11)\) and \(B=O(r)\), the following cuts \(D\) all have \(|B\cap D|=3\) and no \(D\)-singleton on the augmented cycle:

| \(D\) | \(r_D(h_r)\) | \(S_{B\triangle D}(h_r)\) |
|---|---:|---:|
| \(\{1,2,3,4,5,6\}\) | 1 | 8 |
| \(\{1,2,3,4,7,8\}\) | 2 | 4 |
| \(\{1,2,5,6,9,10\}\) | 3 | 0 |

These directly illustrate \(12-4r_D\).

Both remaining three-vertex cell ledgers are locally nonempty:

- For \(g=1,p=4,q=0\), a full path \(a,b,c\) uses \(ab,bc\), and four pair runs can use \(ac,ba,ca,cb\).
- For \(g=2,p=2,q=1\), full paths \(a,b,c\) and \(b,a,c\) use four arcs; pair runs can use \(ca,cb\), with one additional all-singleton layout.

These specify only internal cell layouts. They are **not** five jointly compatible Hamilton cycles or a T2(11) witness.

As a separate general-interface control, \(M=C\) is genuinely realizable at another order. The four rows

\[
(0,1,3,2),\quad
(1,2,0,3),\quad
(2,3,1,0),\quad
(3,0,2,1)
\]

form an actual T2(4) with \(M=C\). They are the translates modulo four of the first row. Its adjacency differences are \(1,2,3\), so translation exhausts all twelve directed adjacency pairs. Its distance-two differences are \(3,1\), so translation produces eight distinct distance-two pairs. The missing difference-two pairs are exactly the closing pairs.

This is a written exact check, not executed output. It does not establish nonvacuity of the unresolved \(M=C\), three-common-support branch at order eleven.

## 11. Public attribution and verification status

The inspected definition in Christopher D. Rosin, *Using Reasoning Models to Generate Search Heuristics that Solve Open Instances of Combinatorial Design Problems*, arXiv:2505.23881v1, Table 6, matches the actual-row target used here:

[https://arxiv.org/html/2505.23881v1#A1.T6](https://arxiv.org/html/2505.23881v1#A1.T6)

I inspected the opening portion of that paper and the specific definition passage, not its entire text.

A public copy of Etzion–Golomb–Taylor’s 1989 *Tuscan-K Squares* was located at:

[https://etzion.net.technion.ac.il/files/2016/02/P12.pdf](https://etzion.net.technion.ac.il/files/2016/02/P12.pdf)

The reader reported incomplete text extraction on all eleven pages. I did not obtain a readable full-paper inspection, and no theorem from that unread paper is used here.

The new arguments above were derived from the frozen actual-row definitions and singleton identity. This does not establish novelty, priority, independence from all known Tuscan invariants, or a complete current-literature status assessment.

**Verification status:** author-written proof only. No independent review, finite replay, parent mathematical adoption, human review, cross-family review, or formal/kernel verification is claimed. Earlier reviews of the input identities do not review these new joint-cut arguments.

## 12. Exact remaining original-target obligations

No eleven-row witness has been constructed, and unrestricted T2(11) nonexistence has not been proved.

The surviving cases include:

- configurations with no support occurring three times, subject to the new universal overlap inequality;
- configurations with one tripled support and all other supports intersecting it in two, three, or four symbols;
- under \(M=C\), the still-unexcluded eight-cycle residual branches for a single tripled support;
- under \(M=C\), multiple tripled supports satisfying the intersection, \(T\)-ledger, cell-layout, and symmetric-difference restrictions above;
- all relevant \(M\ne C\) branches, to which the conditional zero-singleton and four-cell arguments have not been exported.

The exact unpaid step for a full no-go is to exclude every remaining compatible collection of actual Hamilton cycles while retaining the original adjacency and distance-two conditions. The alternative is an explicit eleven-row array with all 110 adjacency and 99 distance-two events independently checked.

This manuscript supplies new whole-class necessary conditions and branch exclusions, not completion of either obligation.