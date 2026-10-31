# Actual-unitary support 50: the excess-five parity obstruction and per-cut refinements

**Status: NONBLIND GENERAL AUTHOR, same harness; proposed written reconstruction and additional candidate lemmas, not a review or a parent disposition.** Fix one normalized complex AME(4,6) state and one local orthonormal product basis. Put \(U=6\psi\), let \(N\) be its number of nonzero entries, and let \(t\) be the number of entries of \(U\) of modulus one. I propose the following necessary statements for the actual tensor, with arbitrary complex phases and moduli:

1. \(N=50,t=27\) is impossible. This exact branch needs only **one** genuine unitary flattening and does not use a global bound on \(t\), no-OLS, alphabet classification, another branch, or a computer calculation.
2. At \(N=50,t=26\), every balanced cut has either two \(3\times3\)-minus-one blocks and two full \(2\times2\) blocks, or one connected \(4\times4\), 12-entry block and three full \(2\times2\) blocks. The possible supports of that 12-entry block are made explicit below.
3. At \(N=50,t=28\), every balanced cut has either two full \(3\times3\) blocks and one full \(2\times2\) block, or one connected \(4\times4\), 14-entry block and two full \(2\times2\) blocks. The exclusion here of connected excess-six components of orders six and eight is an **additional, unreviewed proposed strengthening** of the packet's broader necessary alternatives, not an imported finding.

These are per-cut necessities for the same \(U\), **not** a classification of simultaneous cross-cut supports or complex phases, not an exclusion of either \(t=26\) or \(t=28\), and not a global support-50 witness, exact minimum, or novelty claim. The \(t=25\) branch and any global or conditional union are outside this reconstruction. All load-bearing claims below need an independent full read and disposition.

## 1. Actual unitary interface and where graph-only arguments stop

Every two-versus-two flattening of \(U\) is a \(36\times36\) unitary. A modulus-one entry exhausts its row and column. Hence its row and column are disjoint from those of every other such entry, and deleting all \(t\) saturated rows and columns leaves an \(n=36-t\) square unitary with \(N-t\) nonzeros. It has no singleton row or column: a singleton in a unitary has modulus one and would already have been deleted.

Take the bipartite support graph of this residual unitary. Each connected component is square, say order \(m\), since its block has orthonormal rows and orthonormal columns, giving both row count \(\le\) column count and the reverse. Every vertex has degree at least two. For a component define

\[
 e=|\text{edges}|-2m\ge0.
\]

The total residual excess is \(N+t-72\). Distinct rows cannot overlap in exactly one nonzero position, since their complex inner product would consist of one nonzero term. The same holds for distinct columns. These **no-one-overlap** statements are graph-level necessities; they do not by themselves encode all of unitarity.

In a connected component of order greater than two, a degree-two row at columns \(c,d\) makes \(c,d\) twins: any other row meets both or neither, so their row neighborhoods coincide. Each twin column has degree at least three. If its degree were two, the two columns restricted to their two common rows would be an orthonormal basis, forcing all other columns to vanish on those two rows and separating a full \(2\times2\) unitary block. Moreover, two degree-two rows have **disjoint** twin pairs. A one-column intersection violates no-one-overlap; if their two neighbors coincide, the two orthonormal rows span those two columns, forcing every other row to vanish there and separating a \(2\times2\) block. Transpose all these statements for degree-two columns. In particular, two low columns in a connected component have disjoint neighborhoods.

The disjointness assertion is a genuine-unitary step, not merely the no-one-overlap rule: the connected graph with row neighborhoods \(12,12,1234,1234\) has no one-overlap on either side, but is not a unitary support, because the first two rows would exhaust columns 1 and 2. This example also shows why a graph-only count may include masks forbidden by actual complex unitarity.

Write \(k\) for the number of degree-two rows. Since each other row contributes at least one to the excess, \(k\ge m-e\). The \(2k\) columns in their disjoint twin pairs have degree at least three, while there are at most \(e\) high columns. Consequently

\[
 2k\le e,\qquad m\le e+\lfloor e/2\rfloor\quad(m>2). \tag{1}
\]

The same inequalities hold with rows and columns exchanged. An order-two component is a full \(2\times2\) block with excess zero.

## 2. Low excess: complete arguments used by the parity step

From (1), excess one is impossible. An excess-two component has order three and eight entries, i.e. \(3\times3\) minus one entry. For excess three, the order is at most four. If it were four, both sides would have exactly one low line and three degree-three lines. The low row's twins each have degree three and meet precisely two of the three high rows, leaving a high row that avoids them and has at most two available columns. Thus an excess-three component is a full \(3\times3\) block.

**Excess four, order five.** There are one or two low rows. With one, all four high rows have degree three. The low-row twins have common degree three or four, because degree five twice would already use six excess units. Some high row avoids the twins and hence uses all other three columns. Any high row meeting the twins has exactly one remaining neighbor and therefore overlaps that avoiding row once, impossible. With two low rows, their four twin columns all have degree three: raising either equal-degree pair to degree four would require at least six column-excess units. Each pair consists of its low row and a two-subset of the three high rows. Two such subsets must intersect and cannot intersect once, so they are equal. The third high row can meet only the fifth column, contradicting minimum degree two.

**Excess four, order six.** There are exactly two low rows and, by transposition, two low columns; all other lines have degree three. The four twin columns are all the high columns. The two low columns avoid the low rows and have disjoint two-element neighborhoods \(A,B\), partitioning the four high rows. Each twin column has two high-row neighbors and meets either low column in zero or two positions, so its high neighborhood is exactly \(A\) or \(B\). If the twin pairs choose the same neighborhood, the other two high rows have only one neighbor. If they choose different neighborhoods, the support splits into two components. Both contradict the hypotheses.

**Excess five, order five.** If either side has a low line, transpose so that there are one or two low rows. With one, the other row degrees are \(3,3,3,4\). The twins have degree three or four, so at least one high row avoids them and uses all three remaining columns. At least two other high rows meet the twins; each must use at least two of those other three columns to avoid a one-overlap with the avoiding row, so each has degree at least four. Only one such row is available. With two low rows, all four twin columns have degree three, because even one degree-four twin pair would use at least six column-excess units. Their two high-neighborhoods are two-subsets of the three high rows; as above, they must coincide and leave the third high row at most one column.

If neither side has a low line, all five rows and columns have degree three. Each row omits two columns and each column is omitted by two rows. Distinct rows meet in at least one column and cannot meet in exactly one, so their two-column omission sets must intersect. Fix one row omitting \(u,v\). Among the other four rows, at most one also omits \(u\) and at most one also omits \(v\), yet all four omission sets must meet \(\{u,v\}\). Contradiction.

**Excess five, order seven.** Both sides have exactly two low lines and five degree-three lines. The two low columns avoid the low rows and have disjoint two-subsets \(A,B\) of the five high rows as neighborhoods. Each of the four twin columns of the low rows has two high-row neighbors, meeting each of \(A,B\) in zero or two positions, so it chooses exactly \(A\) or \(B\). The fifth high row outside \(A\cup B\) meets neither low column nor any twin column, leaving only one other column available. This contradicts minimum degree two.

These arguments reconstruct the packet's stated order-five/order-six excess-four and order-five/order-seven excess-five exclusions. They use complex unitarity only through the square-block, no-one-overlap, and genuine-unitary twin/isolation facts spelled out above; no phase choice is made.

## 3. Standalone \(N=50,t=27\)

Here \(n=9\), the residual has 23 entries, and the total excess is \(5\). Every positive component has excess at least two. The only possible positive-excess partitions are \(5\) and \(3+2\).

For \(3+2\), both positive components have order three, by Section 2. All other components have order two, so the total order is even, not nine. For a single excess-five component, (1) bounds its order by seven, and the remaining order is a sum of twos; therefore its order is odd. Order one is excluded by minimum degree, order three can have at most nine entries and hence excess at most three, and orders five and seven were excluded in Section 2. This exhausts all possibilities. Thus the asserted single-cut residual cannot be unitary, proving the exact \(N=50,t=27\) contradiction without any assumption about other possible \(t\) values.

## 4. \(t=26\): necessary alternatives and the 12-entry mask

Here \(n=10\), the residual has 24 entries, and the total excess is four. The positive-excess partition is either \(2+2\) or \(4\). In the first case the two positive components are \(3\times3\) minus one entry, and the remaining order gives two \(2\times2\) blocks. In the second, a positive component has order at most six; orders five and six are impossible by Section 2, while order three has excess at most three. It is therefore a connected order-four, 12-entry component, with three \(2\times2\) blocks.

The following is a further necessary support classification for that order-four block. Let \(k\) be its number of low rows. By the twin bound \(k\le2\).

* If \(k=0\), all rows have degree three.
* If \(k=1\), the row degrees are \(2,3,3,4\). The two twin columns have degree three or four. If degree three, the degree-four row meets them and one of the degree-three rows avoids them, leaving that row only two possible columns. If degree four, all three high rows meet them. The two degree-three rows each use one of the other columns and the degree-four row uses both; minimum column degree forces the two degree-three rows to choose different other columns. Those columns then overlap in exactly the degree-four row. Both cases are impossible.
* If \(k=2\), the other two rows have degree four. The disjoint twin pairs fill the four columns, so every column has degree three.

Applying the same reasoning after transposition gives exactly these **necessary** patterns, up to row and column permutations: (i) each side has degree \((3,3,3,3)\), so the four zeros form a permutation; (ii) rows have degrees \((2,2,4,4)\) and columns have degrees \((3,3,3,3)\), with the two low rows supported on disjoint column pairs; or (iii) the transpose of (ii). This description is not a claim of simultaneous three-cut realizability.

## 5. Additional candidate lemma: excess six cannot have order six or eight

The packet's \(t=28\) discussion leaves these two orders as possibilities. The following proposed direct argument removes them under the actual-unitary hypotheses; it has **not** been independently checked.

### 5a. Order six

Suppose a connected order-six component has excess six, hence 18 entries. Let \(k\) be its number of low rows. The disjoint-twin bound gives \(k\le3\).

* **\(k=3\).** The other three rows have degree four. The six twin columns exhaust all columns and all have degree three. Each contains its low row and a two-subset of the three high rows. Any two such high-neighborhoods belonging to different low rows intersect and cannot meet once, so they coincide. The remaining high row has no neighbor, a contradiction.
* **\(k=2\).** The four twin columns occur as two equal-degree pairs. Each has degree at least three, and total column excess is six. Thus their pair-degrees are either \((3,3)\) and \((3,3)\), or \((4,4)\) and \((3,3)\).
  * In the first case, the two twin-pair high-neighborhoods are two-subsets of the four high rows. They cannot meet once. If equal, the other two high rows have only the two remaining columns available, contrary to degree at least three. Hence they are disjoint sets \(A,B\) partitioning the high rows. Each of the two remaining columns meets each of \(A,B\) in zero or two positions; these columns have total degree six, so their degrees must be two and four, not three and three. The degree-four column contains all four high rows and the degree-two column contains just \(A\) or just \(B\). A row in \(A\) and a row in \(B\) then meet in exactly the degree-four column, contradiction.
  * In the second case the two remaining columns have degree two. They avoid the low rows and have disjoint two-subset neighborhoods \(A,B\) partitioning the four high rows. A degree-four twin column contains its low row and three high rows. Any three-subset of \(A\cup B\) meets one of \(A,B\) once, violating no-one-overlap with that low column.
* **\(k=1\).** The five high-row degrees are \(3,3,3,3,4\). By transposing the already excluded \(k=2,3\) cases, the number of low columns is zero or one. Consequently the twin columns of the low row both have degree three: when there are no low columns all six columns have degree three, and when there is one low column there is only one degree-four column. Let \(x,y\) be the two high rows meeting those twins. Any other column meets a twin in zero or two places and avoids the low row, so it contains both \(x,y\) or neither; their row neighborhoods are identical. Their degrees are equal, and there is only one degree-four high row, so both have degree three. They share precisely one additional column. No other row can meet that additional column without overlapping one of \(x,y\) exactly once. The low row, \(x,y\), the twins and this additional column therefore form a separate \(3\times3\) component, contradiction.
* **\(k=0\).** All rows have degree three. The preceding cases, transposed, exclude low columns, so all columns also have degree three. Two distinct rows cannot have the same three-column neighborhood: the three columns have three incidences left after those two rows, and every other row meets the neighborhood in zero, two, or three positions. The only possibility is one more identical row, after which those three rows and columns form a separate \(K_{3,3}\) component. Thus all row neighborhoods are distinct. For any fixed row, its three columns contribute six intersections with the other five rows. No-one-overlap and distinctness permit only zero or two intersections, so exactly three other rows meet it twice and two are disjoint. But a three-subset of six columns has only one disjoint three-subset, so those two disjoint rows have identical neighborhoods, contradiction.

All low-row cases are exhausted, excluding connected order six with excess six.

### 5b. Order eight

Suppose a connected order-eight component has excess six, hence 22 entries. There are at least two and at most three low rows, and the same is true for low columns.

If there are three low rows, their six twin columns have degree at least three and use all six units of column excess. They therefore have degree three, and the remaining two columns have degree two. Those low columns avoid the low rows and have disjoint two-element neighborhoods \(A,B\) among the five high rows. Each twin column has two high-row neighbors and intersects each of \(A,B\) in zero or two positions; it must therefore choose all of \(A\) or all of \(B\), since only one high row lies outside their union. That remaining high row has no neighbor at all, contradiction. The transposed case of three low columns is likewise impossible.

Hence there are exactly two low rows and two low columns; all other lines have degree three. Let \(A,B\) be the disjoint two-high-row neighborhoods of the two low columns, and let \(Z\) be the remaining two high rows. The four twin columns of the two low rows each contain their low row and exactly two high rows. Since they meet the low columns in zero or two positions, their high neighborhood is exactly \(A\), \(B\), or \(Z\). Each row of \(Z\) has degree three but can use only the four twin columns and two other high columns; therefore at least one twin pair has high neighborhood \(Z\). The other twin pair cannot also choose \(Z\), as that would already give each \(Z\)-row degree four. Suppose it chooses \(A\); the case \(B\) is symmetric. Each \(B\)-row already meets its low column and must meet both remaining high columns to reach degree three. Each \(Z\)-row meets the \(Z\)-twin pair and needs one further neighbor, and no-one-overlap with either twin column forces those two \(Z\)-rows to use the same remaining high column. But each remaining high column has degree three and already contains both \(B\)-rows, leaving only one place. Contradiction.

Thus neither order six nor order eight can occur for a connected excess-six component of an actual unitary.

## 6. \(t=28\): resulting necessary per-cut alternatives

Here \(n=8\), the residual has 22 entries, and total excess is six. The positive component partitions are \(6\), \(4+2\), \(3+3\), and \(2+2+2\). Three excess-two components already require order nine. For \(4+2\), the excess-two component has order three and Section 2 forces the excess-four component to have order four; their total order is seven, which cannot be completed to eight using order-two components. For \(3+3\), the two full order-three components leave one full order-two block.

For a single excess-six component, the remaining order is a sum of twos, so its order is even and at most eight. Order two has zero excess, while orders six and eight are excluded by Section 5. It must therefore have order four and 14 entries, leaving two full order-two blocks. This gives the two alternatives in the opening claim.

The 14-entry block has precisely two zeros. Thus, up to row and column permutations, the two zeros either share a row, share a column, or lie in different rows and columns. The corresponding block degree multisets on the two sides are respectively \((2,4,4,4)/(3,3,4,4)\), its transpose, or \((3,3,4,4)/(3,3,4,4)\). These are necessary masks, not a claim that all three cut masks, complex amplitudes, and pair incidences can be jointly realized by one tensor.

## 7. Coverage, provenance, and boundaries

Main directly confirmed the actual dispatch receipt and authorized starting the controls. I read that receipt, the entire manifest, freeze receipt, final pre-dispatch binding, prepared metadata, and all 22 manifest-listed status/permission controls through their endings. I sent Main the direct PREBODY ACK naming those controls and the ordered packet counts **before** reading packet bodies. Thereafter I read packet part 01 serially as RAW LF 1–20, 21–40, ..., 401–420, 421–433, followed by part 02 as RAW LF 1–20, 21–40, ..., 101–120, 121–138, through the endings, including long lines, before mathematical work or comparison. No sequence deviation is known. The packet renders complete bodies S1–S6, respectively 161, 29, 29, 31, 161, and 132 original LF. In particular S1 is the nonblind prior candidate proposing the parity proof; this is a reconstruction in view of that candidate, not a blind or independent-model-family result.

The parent-supplied manifest declares source-body SHA-256 pins, in that order: `3752d4b981b70d4626dbda6a87644044332ffd2e431a624f753fcccf9257d4f9`, `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0`, `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a`, `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0`, `ac4f6284549678e0e0430242baed238230680b74a0f1facbd8e8e1cd99691181`, and `c852a533a2e26cd2b7bcf37f38827c63511544d7b5d1a9e98b5454ac7b7f2b3a`. The declared packet hashes are `3fa85011e561ba4636b2bf957258792ac51f4ebbc549d323b0c7bb8e6426b425` and `10f367294d61b46e5d746b2b3bfabab782803d2e506f69609b4b6c39cd58402a`. The parent metadata reports its roundtrip and binding matches. I did not open or independently rehash outgoing original source paths, so these administrative pins are not a source-identity or correctness certification.

All genuine held episodes **and every consumer** remain NONINPUT; controls were used for status/permissions only. No old code, unlisted scientific source, outgoing source link, sibling proof, network, Git, install, deletion, scientific child execution, solver, test, compiler, build, or external-model CLI was used. No executable source was prepared. In particular, the new excess-six order-six/eight arguments have not been tested or independently reviewed. This is not human, family, formal/kernel, parent-adoption, phase-feasibility, global-existence, or novelty evidence. If any step is found faulty, preserve these bytes and record a separate correction rather than silently rewriting this candidate.
