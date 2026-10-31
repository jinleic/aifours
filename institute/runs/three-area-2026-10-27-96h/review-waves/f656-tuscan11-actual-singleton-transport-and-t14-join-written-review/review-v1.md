# F656 written reconstruction — complete return for parent materialization

**Intended artifact:** `review-v1.md` in the assigned F656 wave.  
**Reviewer:** ReviewF656TuscanT14.  
**Status:** Unadopted same-harness written review; no repository files changed.

## Verdict and scope

**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The three proposed theorems and their stated consequences are **SUPPORTED at the explicitly conditional scope**:

1. One actual T2(11) on the same eleven finite symbols;
2. \(M=C\);
3. Two distinct odd-position supports, each occurring three times;
4. The adopted actual-cycle synchronization and square-budget interface in packet S2/S3.

The proof uses the same labeled connected twelve-cycles, their actual internal adjacency arcs, and their actual directed squares. I found no substitution of independently realizable cell schedules for that collection.

This does **not** construct or exclude the whole conditional collection, prove \(M=C\), or close unrestricted T2(11). The optional finite source and its alleged implementation properties were **not inspected or verified**.

## 1. Read boundary and provenance

Before opening the mathematical packet, I read:

- The complete manifest, LF1–163, bound in the supplied receipts to SHA  
  `2a2df85b8d1eac2a78ef33eea69922c6f0b78a882d26d7eb120d00bf02bc0068`;
- The complete freeze receipt, LF1–73, supplied SHA  
  `04007923bb5064912291614cab013c05ae0a0db85bc371b9032c6f6bafc286ea`;
- The complete parent metadata supply and actual dispatch receipt;
- All fifteen listed status-only controls, including their endings.

I then sent the required direct **PREBODY ACK** to `agent://Main`. Subsequently I read the entire literal packet, LF1–264, in ordered RAW windows of at most twenty LF, through the final S4|22. Its supplied packet SHA is:

`f9f03f917c9e295a253ca7c37882265343ffa97432f8995d5a2b455313835078`.

The packet contains complete S1 LF1–150, S2 LF1–54, S3 LF1–36, and S4 LF1–22. Mathematical reconstruction began only after that complete read.

**Administrative correction already sent to Main:** my ACK described the metadata endpoint as “LF1–179” without a separately observed LF count. That exact count is withdrawn. The actual read requests continued through LF161–180 and returned the closing brace before ACK; there was no unread metadata tail.

The hashes and clocks above are **parent-supplied observations**, not independently measured native metadata by this reviewer. I did not inspect author code, author runs, linked evidence, sibling reviews, held payloads, or their consumers. No scientific executable, CAS, interpreter, solver, test, formatter, or new selected mathematical diagnostic was used. The finite case distinctions below reconstruct the classes already expressly present in the literal proof.

## 2. Exact imported interface

I use the following adopted statements at their stated scope, rather than claiming a fresh review of their historical evidence chains.

| Import | Packet location | Scope retained |
|---|---|---|
| Actual augmented adjacency decomposition | S2|7–9 | Eleven connected twelve-cycles partition all 132 directed nonloop arcs. Their squares partition those arcs **only under \(M=C\)**. |
| Four cells and residual layouts | S2|11–29; S3|17–30 | Cells \(I,J,K,L\) have size three. Six alternating cycles leave the same five residual cycles. The synchronized T13/T14 layouts and full masks apply to those cycles. |
| Regular opposite joins | S2|19–24 | Each regular cycle has one join of each opposite kind, with endpoints in nontrivial runs. |
| Directed square budgets | S2|35–42 | Alternating families supply no opposite-cell square arcs. A regular join supplies two same-direction squares. T14’s exceptional cycle contributes three squares in each direction. |
| Physical vertex coupling | S2|44 | Singleton occurrences and full-run middle occurrences are coupled vertex by vertex on the same cycles; cell totals do not replace this condition. |
| Closing-pair reformulation | S4|9–11,16 | The derangement characterization is structural. It does not establish that all eleven closing pairs are missing. |

For a regular segment
\[
A_p\to A_x\to B_y\to B_q,
\]
the selected internal arcs are \(A_p\to A_x\) and \(B_y\to B_q\), and its opposite squares are
\[
A_p\to B_y,\qquad A_x\to B_q.
\]
Every extension argument below respects these directed positions.

## 3. Claim-level disposition

| Claim | Author LF | Disposition |
|---|---:|---|
| Singleton transport by budget saturation | S1|27–33 | **SUPPORTED** |
| Two-full, grouped zero-full, and split zero-full cell-word grammar | S1|35–44 | **SUPPORTED** |
| T14 opposite joins are 2:2 | S1|46–89 | **SUPPORTED** |
| \(x=y,\ u=v,\ x+u=7\); exclusion of family sums \((7,7)\) | S1|48–50,91 | **SUPPORTED** |
| T14 same-row sign and mask correlations | S1|93–101 | **SUPPORTED** |
| T13 missing square and unique grouped bridge | S1|103–117 | **SUPPORTED** |
| Complete T13 four-case table and low-row full-cell conclusion | S1|119–132 | **SUPPORTED** |
| T13 full-pattern and grouped-sign consequences | S1|134–136 | **SUPPORTED** |
| Optional checker implementation, fixtures, termination and outputs | S1|138–142 | **INCONCLUSIVE / NOT AUDITED**, as required by this written-review assignment |
| Actual eleven-row realization or whole-case exclusion | S1|144–150 | **NOT ESTABLISHED**, consistently with the candidate |

## 4. Singleton transport and actual cell-word grammar

### 4.1 The centered-square accounting is exhaustive

Fix opposite cells \(A,B\), with other opposite pair \(C,D\).

An \(A\to B\) square centered in \(A\) must pass through an actual \(A\to B\) adjacency, and is the first square of its regular join segment. A square centered in \(B\) is the second square of that segment.

Any other such square is centered in \(C\) or \(D\). Both neighbors of its middle vertex are outside that vertex’s own cell, so that occurrence is a singleton cell-run. One singleton occurrence has only one ordered predecessor-successor pair, hence centers at most one opposite-cell square.

The required counts are:

| Branch | Opposite squares per pair on regular cycles | Join-supplied squares | Singleton-centered remainder | Total over both pairs | Available singleton occurrences |
|---|---:|---:|---:|---:|---:|
| T13 | 18 | \(5\cdot2=10\) | 8 | 16 | \(4\cdot4=16\) |
| T14 | \(18-6=12\) | \(4\cdot2=8\) | 4 | 8 | \(4\cdot2=8\) |

Distinctness is inherited from the actual square decomposition. Thus the map from required centered squares to singleton occurrences is injective between sets of equal size and is therefore bijective.

A singleton in \(A\) cannot have an \(A\)-neighbor. Its centered opposite pair consequently cannot be \(A,B\); it must be \(C,D\). This proves Theorem 1 in both branches.

### 4.2 The physical gap grammar follows

Contract the two opposite joins into directed blocks with cell words \(A\cdots A B\cdots B\) and \(C\cdots C D\cdots D\). Their lengths are respectively:

- \((6,6)\) for four full cells;
- \((5,5)\) for two full cells;
- \((4,4)\) for zero full cells.

There is one nontrivial run per cell; all remaining vertices are the singleton occurrences in the two cyclic gaps.

Starting after the \(B\)-end of the first block, the singleton-neighbor law forces the recurrence
\[
B,S,A,\operatorname{opp}(S),B,S,\ldots .
\]
The terminal block starts at \(C\). Therefore:

- A gap of one or three singletons is impossible;
- A gap of two has word \(D,A\);
- A gap of four has word \(C,A,D,B\).

The reverse gap has the corresponding symmetric rule.

For a two-full row, its two singletons must consequently occupy one gap together. Their centered squares point opposite the corresponding joins.

For a zero-full row, the four singletons are either:

- **Grouped:** all four in one gap, giving one centered square in each direction of each opposite pair; or
- **Split:** two in each gap, giving two centered squares opposite each corresponding join.

This is a statement about actual consecutive vertices, not independently assigned singleton contributions.

## 5. Complete T14 2:2 reconstruction

### 5.1 The exceptional cycle gives coupled matchings

For one opposite pair let \(F:A\to B\) and \(G:B\to A\) be the square matchings of the exceptional cycle \(h\).

Because \(h\) is a connected twelve-cycle with cell word \(A,C,B,D\) repeated three times, \(GF\) is the action of \(h^4\) on \(A\), hence a three-cycle. Normalize \(F\) by writing \(B_i=F(A_i)\). The reverse matching \(G\) is then one of the two three-cycles on these indices.

This is stronger than two arbitrary independent matchings. Connectedness of the original \(h\) is load-bearing.

### 5.2 A 3:1 split forces two transitive tournaments

Suppose three regular joins point \(A\to B\), and the fourth points \(B\to A\).

The three high joins supply six distinct \(A\to B\) squares. They avoid \(F\), so they are exactly the six off-diagonal matrix entries.

For each high join, its two entries use different source rows and different target columns. Each source index occurs twice among the six entries. Thus the three selected \(A\)-internal arcs have undirected incidence two at each vertex. With no loops, their underlying unordered edges are exactly the three different pairs. They form a tournament. The same holds in \(B\).

Neither tournament can be cyclic:

- In \(A\), extending a high selected arc to its full run requires a preceding internal edge. In a cyclic tournament that edge is already selected in another high row.
- In \(B\), the corresponding required following edge is likewise already used elsewhere.

A cyclic tournament therefore prevents every high row from being full in that cell. The single low row cannot supply the required two full runs. Both tournaments must be transitive.

### 5.3 All four partitions are covered

The pair using source rows 1 and 2 can only be \((12,21)\), \((12,23)\), or \((13,21)\). Enforcing the remaining row-pair and column-pair requirements gives exactly these four partitions:

1. \((12,21),(13,31),(23,32)\);
2. \((12,21),(13,32),(23,31)\);
3. \((12,23),(13,31),(21,32)\);
4. \((13,21),(12,31),(23,32)\).

The first is the reciprocal partition. Every high adjacency is then \(A_i\to B_i\). Adjacency uniqueness forces the three chosen indices to be distinct. Each selected \(A\)-internal arc points into its chosen index, producing indegree one at every vertex—a cyclic tournament, already excluded.

The other three partitions are equivalent by a common permutation of the \(A\)- and \(B\)-indices. Such relabeling conjugates \(G\); it does not require fixing one orientation of \(G\). Both orientations are checked below.

Use the author’s canonical partition
\[
Q_0=(12,21),\quad Q_1=(13,32),\quad Q_2=(23,31).
\]

Its two orientations per pair are exactly the supplied four-vertex segments. Choices 1 for both \(Q_1,Q_2\) repeat \(A_3\to B_3\), independently of \(Q_0\).

The remaining mixed choices have the stated obstructions:

| Choices | Cyclic tournament |
|---|---|
| \(010\) | \(A\) |
| \(110\) | \(B\) |
| \(001\) | \(B\) |
| \(101\) | \(A\) |

Only \(000\) and \(100\) remain. Swapping indices 1 and 2 exchanges these and interchanges \(Q_1,Q_2\). Thus no orientation class is omitted by taking the author’s \(000\) segments:
\[
r_0:A_2A_1B_1B_2,\quad
r_1:A_3A_1B_2B_3,\quad
r_2:A_3A_2B_1B_3.
\]

### 5.4 Physical full runs force the low segment

The selected high \(A\)-edges are \(21,31,32\); the remaining edges are \(12,13,23\).

- \(r_0\) cannot be \(A\)-full: its preceding edge \(32\) is selected in \(r_2\).
- If the low selected edge is \(13\), the low row cannot be full, and only \(r_1\) can be full.
- If it is \(23\), the low row cannot be full, and only \(r_2\) can be full.

Both alternatives contradict two full runs. The low selected edge must be \(12\).

Likewise, the high \(B\)-edges are \(12,23,13\), leaving \(21,31,32\).

- \(r_0\) cannot be \(B\)-full because its following edge \(23\) is selected in \(r_1\).
- Low edge \(31\) leaves only \(r_2\) possibly full.
- Low edge \(32\) leaves only \(r_1\) possibly full.

The low selected \(B\)-edge must be \(21\). The actual low segment is therefore
\[
B_2\to B_1\to A_1\to A_2.
\]

Its reverse squares are \(B_2\to A_1\) and \(B_1\to A_2\).

- For \(GF=(123)\), \(G\) contains \(B_1\to A_2\);
- For \(GF=(132)\), \(G\) contains \(B_2\to A_1\).

Either orientation repeats an actual square already supplied by \(h\). Thus 3:1 is impossible. Exchanging \(A,B\) excludes 1:3. The imported bounds leave exactly **2:2**.

## 6. T14 family totals and synchronized signs

### 6.1 Family totals

Each of the four residual directional counts
\[
9-x-u,\quad9-y-v,\quad9-x-v,\quad9-y-u
\]
is now two. Hence
\[
x+u=y+v=x+v=y+u=7,
\]
so
\[
x=y,\qquad u=v,\qquad x+u=7.
\]

Both family sums are even. The previously permitted \((6,8),(7,7),(8,6)\) reduce to **\((6,8),(8,6)\)**.

### 6.2 The three full-count patterns

Each opposite direction needs exactly two singleton-centered regular squares after subtracting its two joins and \(h\).

- **\((4,4,0,0)\):** grouped/grouped supplies \(2,2\); split/split supplies \(2,2\) only with opposite join signs; grouped/split supplies \(3,1\) or \(1,3\), impossible. In the split/split case the four-full rows also have opposite signs by the 2:2 join margin.

- **\((4,2,2,0)\):** if the zero-full row is grouped, the two two-full rows must have opposite join signs, and the four-full and zero-full rows must have opposite signs. If the zero-full row is split, both two-full joins point opposite its join, while the four-full join has its sign.

- **\((2,2,2,2)\):** the gap grammar makes the full mask either \(\{J,L\}\) or \(\{I,K\}\) when \(s=t\), and either \(\{I,J\}\) or \(\{L,K\}\) when \(s\ne t\). The two 2:2 sign margins imply
  \[
  n_{++}=n_{--},\qquad n_{+-}=n_{-+}.
  \]
  Combining this with opposite-mask multiplicities gives the claimed
  \[
  (n_{++},n_{--},n_{+-},n_{-+})=(x,x,2-x,2-x).
  \]

These statements retain the same named physical rows for both opposite pairs. They do not establish compatible vertex labels.

## 7. Complete T13 4:1 reconstruction

### 7.1 The sole missing high-direction square

There are five selected internal edges in each cell, one per join row, and one additional edge in the cell’s unique full run.

Let \(\ell\) be the low row’s selected edge and \(e\) the additional edge. The four high selected edges contribute eight squares. Each vertex’s square-source count is its undirected incidence among those four edges, at most three.

If \(\ell,e\) were reversals of the same unordered edge, the third vertex would retain all four incidences, impossible. Thus they occupy different unordered pairs and share exactly one vertex \(z_A\). The high source degrees are two at \(z_A\), three elsewhere. The target argument similarly identifies \(z_B\). The unique missing high-direction entry is therefore \(z_A\to z_B\).

### 7.2 The bridge must be a high grouped zero-full row

The square \(z_A\to t\to z_B\) cannot be centered in \(A\) or \(B\); otherwise it would belong to a high join’s two supplied squares.

If it were in the low segment
\[
B_p\to B_y\to A_x\to A_q,
\]
the incident-edge conditions force \(z_A=A_q,\ z_B=B_p\). This closes the five-cycle
\[
B_p\to B_y\to A_x\to A_q\to t\to B_p,
\]
contradicting the connected twelve-cycle. The bridge is high.

In that high row, both selected internal edges omit \(z_A,z_B\). These third vertices must be singleton runs, as must \(t\). The row therefore has zero full cells, and its three consecutive singleton occurrences force the grouped four-singleton grammar.

Exactly two high \(A\)-edges omit \(z_A\), and exactly two high \(B\)-edges omit \(z_B\). If two rows belonged to both sets, their selected edges would be reversals on both sides and their two square pairs would coincide. Their intersection is consequently exactly the unique bridge row.

### 7.3 Exhaustiveness of the four-case table

Normalize the bridge as
\[
r_0:A_2A_1B_2B_1,
\]
with \(z_A=A_3,z_B=B_3\). Its squares are 11 and 22; entry 33 is missing.

The other \(A_3\)-omitting high edge is \(12\), defining \(r_1\). The other \(B_3\)-omitting high edge is \(12\), defining the distinct row \(r_2\).

The remaining six entries have precisely the two supplied partitions:
\[
(12,23),(21,32),(13,31),
\]
or
\[
(13,21),(12,31),(23,32).
\]
The \(r_1,r_2\) selected edges force their orientations. The final pair has two orientations. This gives exactly X1, X2, Y1, Y2.

### 7.4 Reconstruction of every full-cell conclusion

For a high row, an \(A\)-full extension precedes its selected \(A\)-edge and a \(B\)-full extension follows its selected \(B\)-edge. For the low row these roles reverse. This directionality is essential.

The remaining internal edges after the four high selections give:

| Case | Remaining \(A\)-edges | Remaining \(B\)-edges | Forced conclusion |
|---|---|---|---|
| X1 | \(13,32\) | \(31,32\) | Low \(A\) uses \(13\) with extension \(32\), hence is full. Low \(B\) cannot be full; its full run is in \(r_1\) or \(r_3\). |
| X2 | \(31,32\) | \(13,32\) | The \(A\)-extra is \(31\) in \(r_1\), leaving low selected \(32\), nonfull. Low \(B\) selects \(32\) with preceding \(13\), hence is full. |
| Y1 | \(13,23\) | \(13,32\) | Low \(A\) is nonfull; its full run is in \(r_2\) or \(r_3\). Low \(B\) selects \(32\) with preceding \(13\), hence is full. |
| Y2 | \(13,32\) | \(13,23\) | Low \(A\) selects \(13\) with following \(32\), hence is full. The \(B\)-extra is \(23\) in \(r_2\), leaving low selected \(13\), nonfull. |

In particular, every apparent extension of the bridge in \(A\) or \(B\) is forbidden by its established singleton vertices. This is needed to force the table; an internal-edge ledger without that physical constraint would be insufficient.

Every case has **exactly one of \(A,B\) full in the low row**. Its full count is therefore two, and its other full cell belongs to the other opposite pair.

These are necessary configurations, not certified realizations.

## 8. T13 consequences

In the \((4,0,0,0,0)\) pattern, no two-full row exists. The forced low row therefore rules out either extreme 4:1 orientation. The imported positive directional bounds leave 2:3 or 3:2 for each opposite pair.

In \((2,2,0,0,0)\), a 4:1 split instead forces its low row to be one of the two two-full rows and its bridge to be a grouped zero-full row. This does not exclude that pattern.

For the additional sign identity in \((4,0,0,0,0)\):

- A four-full row contributes square-direction difference \(2s_F\);
- A split zero-full row contributes \(2s-2s=0\);
- A grouped zero-full row contributes \(2s\).

Equality of the nine squares in each direction gives
\[
s_F+\sum_{\text{grouped rows}}s=0.
\]
The number of grouped rows is therefore odd: one or three. Both opposite pairs use the same grouped/split classification of the four physical zero-full rows.

## 9. Unpaid interfaces and non-acceptances

The following remain unpaid, and this review supplies no substitute:

1. **T14:** simultaneous labeled compatibility of all eleven cycles, both complete arc decompositions, surviving family sums \((6,8),(8,6)\), and all three full-count patterns.
2. **T13:** simultaneous compatibility of both opposite-pair constraints, their physical masks, bridge rows, internal edges, and all remaining adjacency and square arcs.
3. **Other original branches:** \(M\ne C\), fewer tripled supports, and every original-row case outside the stated assumptions.
4. **Optional source:** implementation completeness, fixtures, resource behavior, and any execution result. No code/run was inspected; none supports this verdict.
5. **Original target:** an actual eleven-row witness with all 110 adjacency and 99 linear distance-two events verified, or a contradiction covering every original branch.

In particular, a zero count for a necessary local relaxation would not itself establish full-array nonexistence. The candidate expressly preserves that distinction.

## Final verdict fields

**Findings:** None.

**Overall correctness:** correct, at the stated conditional written-theorem scope.

**Explanation:** The singleton budget, exhaustive T14 matching/orientation argument, physical full-run obstruction, and complete T13 bridge/table argument reconstruct from the frozen imports on the same actual cycles. No full-array realization, global exclusion, \(M=C\) theorem, source-code verification, novelty, independent-family, human, or kernel conclusion follows.

**Confidence:** 0.97.