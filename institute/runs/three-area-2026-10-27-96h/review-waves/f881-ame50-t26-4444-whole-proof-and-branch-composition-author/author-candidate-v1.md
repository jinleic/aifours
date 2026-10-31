# One-tensor 4444 obstruction and conditional exact-t26 composition

**Status: prospective, nonblind, same-harness AUTHOR proof candidate, not an acceptance.** This is an independent written reconstruction and audit of the entire f860 argument in packet source S2, not a use of f879, f880, a sibling return, or an unpublished review. The proposed direct result is the following.

> **4444 statement.** There is no normalized complex pure state \(\psi\in(\mathbb C^6)^{\otimes4}\), in a fixed product orthonormal basis, whose three balanced \(36\times36\) flattenings of \(U=6\psi\) are unitary, which has exactly \(50\) nonzero coefficients, exactly \(26\) modulus-one coefficients of \(U\), and exactly four symbols used by the remaining \(24\) coefficients at each party.

All amplitudes not fixed to zero are arbitrary complex numbers: no reality, equal-modulus, phase, linearity, symmetry, independent-cut-realizability, or particular degree-pattern assumption is made. Every object and all six pair projections below come from **one and the same tensor**. The proof purports to cover all surplus partitions, all allowed cut components, both parity cases and every single-F arrangement. The separate, explicitly conditional composition with the parent-adopted q=4444-only statement is in §8. If any independently reviewed local cut derivation in §2 is not accepted, the 4444 result is conditional on the complete actual-unitary interface explicitly stated there, not on an absent graph enumeration.

## 1. The actual support and its common degree data

Name the parties \(A,B,C,D\). Let \(P\) be the actual 26 modulus-one words and \(E\) the remaining actual 24 nonzero words. A modulus-one entry in a unitary exhausts its row and column. Hence, for **each** physical pair \(ij\), the 26 projections of \(P\) are distinct and disjoint from the \(E\) projections. The other ten pair values are all used by \(E\); each has at least two extensions, since a residual unitary line with a single nonzero would have modulus one. These are statements about all six pair systems of the same \(P,E\), not six separately chosen masks.

For an E-used symbol \(x\) at party \(i\), put \(d_i(x)=|\{y:(x,y)\in\pi_{ij}E\}|\). It is independent of \(j\ne i\): exactly \(6-d_i(x)\) words of \(P\) contain \(x\). Let \(s_i(x)\) count E words containing \(x\), and define

\[
 h_i(x)=s_i(x)-2d_i(x)
       =\sum_{y:(x,y)\in\pi_{ij}E}(m_{ij}(x,y)-2)\ge0,
 \quad \sum_x d_i(x)=10,\quad \sum_x h_i(x)=4. \tag{1}
\]

Here \(m_{ij}(x,y)\) is its actual E multiplicity; the identity holds for every other party \(j\). If \(d_i(x)=1\), independence of degree fixes one symbol in each of the other three parties, leaving at most one distinct E word, contrary to the two-extension rule. Thus all four E-used symbols have degree at least two. The only sorted degree multisets are \(2224\) and \(2233\).

For a degree-two symbol, the other three E alphabets in its slice have size two. If its surplus were one, the slice would be five vertices of a binary 3-cube. For each direction, the two unitary rows at its two symbols have nonempty supports and cannot overlap in just one position; hence the five vertices induce at least two edges in each of the three directions, at least six total. Three deleted cube vertices induce at most two edges, so they remove at least \(9-2=7\) of the twelve cube edges, leaving at most five. Therefore

\[
 h_i(x)=1\ \Longrightarrow\ d_i(x)\ge3. \tag{2}
\]

This uses actual orthogonality, and a singleton overlap is impossible for arbitrary nonzero complex entries.

## 2. Complete low-excess cut reconstruction

After deleting the isolated P rows and columns, each balanced cut is an actual \(10\times10\) unitary with 24 nonzeros. All its row and column degrees are at least two, and its excess over twice the order is four. A connected support component is square: the block's rows and columns are both orthonormal, so the two dimensions bound each other. Distinct rows, and distinct columns, never have exactly one common nonzero.

In a component of order \(m>2\), a degree-two row's two columns have identical row neighborhoods, because any row meeting exactly one would overlap it once. Both columns have degree at least three, for otherwise the component would be an isolated \(2\times2\) block. Different degree-two rows have disjoint column pairs: if they share a column they share both, and their two orthonormal row vectors span those two columns, forcing every other row to be zero there. The transposed statements hold. If the component has excess \(e\) and \(k\) degree-two rows, the other rows contribute at least one excess apiece and the \(2k\) disjoint twin columns each contribute at least one, so

\[
 m-e\le k\le\lfloor e/2\rfloor. \tag{3}
\]

An excess-zero component is \(2\times2\): if its order were greater than two, (3) would be impossible. Excess one is impossible. Excess two has order three and is the \(3\times3\) support with one zero; its zero is at the intersection of its unique degree-two row and column. For excess three, (3) allows orders three and four. At order four there is one degree-two row and three degree-three rows. Its twin columns have equal degree, necessarily three because degree four for both would use four excess units. One high row avoids both twins and cannot fit its three nonzeros in the two remaining columns. Thus excess three is the full \(3\times3\).

For excess four, (3) gives order at most six. Order five has one or two degree-two rows. With one, the other four rows all have degree three; not all can use both twin columns, since that would give each twin degree five and already six column excess units. A row avoiding the twins then uses all three other columns and overlaps a row using the twins in exactly one position. With two low rows, their four twin columns each have degree three and the fifth column degree two. The high-row parts of the two twin pairs are two-subsets of the three high rows. Intersection one violates column orthogonality; intersection two leaves the third high row with at most the fifth column. At order six there are exactly two low rows and two low columns; every other line has degree three. The two low columns, which meet only high rows, have disjoint two-element neighborhoods partitioning the four high rows: intersection one is forbidden and identical neighborhoods would isolate a \(2\times2\) block. Each high twin-column pair must take one whole part of this partition, else it meets a low column exactly once. Taking the same part twice leaves the other two rows of degree at most two; taking different parts disconnects the component. Hence excess-four components have order four.

The total excess four is consequently either \(2+2\) or \(4\): an excess-three component cannot be accompanied by excess one. The zero-excess blocks fill the remaining order. Thus every actual cut has exactly one of

* **X:** two \(3\times3\)-minus-one components and two \(2\times2\) blocks;
* **Y:** one connected \(4\times4\), 12-entry component and three \(2\times2\) blocks.

On either side of Y, the only partitions of 12 into four degrees between two and four are \(3333,2334,2244\). For \(2334\), the unique low row has twins of equal degree. If those columns have degree three, one degree-three row avoids both and has only two other places. If they have degree four, the two remaining degree-two columns intersect only in the full row. Both possibilities violate unitarity. For \(2244\), the low rows have disjoint twin pairs and the other two rows are full, giving opposite degrees \(3333\). If both sides are \(3333\), the core is all 16 positions except one zero in each row and column.

Therefore every physical pair system has exactly one of the following types:

* **T:** four multiplicity-three values and six multiplicity-two values;
* **F:** two multiplicity-four values and eight multiplicity-two values.

Complementary systems are T/T, F/T or T/F, never F/F. In F/T, the two F rows are full on the four T-high columns; the other two core rows have disjoint two-element supports partitioning those columns. In T/T, X has two complete high-by-high \(2\times2\) rectangles, whereas Y has the \(4\times4\) high block with one zero per row and column. These component, degree and mask statements together are the **named actual-unitary cut interface** if §2 itself is treated as a conditional import. No conclusion here depends on an unprovided finite run or on sufficiency of these necessary masks.

## 3. Two phase-valid local lemmas

**A degree-two, surplus-two symbol has exactly one incident F pair.** Its slice has six distinct vertices of its actual binary cube. If the two omitted vertices differ in one coordinate, sum squared moduli over that coordinate. The resulting \(2\times2\) table on the two agreeing coordinates has every row and column sum one, because all four corresponding pair lines are actual unitary rows. An empty cell then forces its opposite cell empty, impossible with only those two omitted vertices. If the omitted vertices differ in all three coordinates, relabel them \(000,111\) and denote the six nonzero entries at \(001,010,011,100,101,110\) by \(a,b,c,d,e,f\). Orthogonality in the three coordinate directions is

\[
 a\overline e=-b\overline f,\qquad
 a\overline c=-d\overline f,\qquad
 b\overline c=-d\overline e.
\]

Multiplying the first and third equations and dividing by the second gives \(b\overline e=-b\overline e\), impossible. The omitted vertices thus differ in exactly two coordinates. The multiplicity pattern is \((4,2)\) in their common coordinate and \((3,3)\) in the other two. By §2, the first physical pair is F and the other two are T. Division is legal because all six actual E amplitudes are nonzero.

**No closed binary box.** Suppose two actual symbols at each party give four pair rows on one side of each balanced cut, all supported on the four selected pair values on the opposite side. The same \(4\times4\) restrictions are unitary in all three cuts; the common four-qubit subtensor divided by two is normalized and has all two-qubit marginals \(I/4\). Let \(A_r\) be the sum of squares of its weight-\(r\) Pauli expectations. Then \(A_1=A_2=0\). Each three-qubit marginal has purity \(1/2\), so its weight-three sum is three and \(A_3=12\); global purity gives \(A_4=3\). The spin-flipped density \(Y^{\otimes4}\bar\rho Y^{\otimes4}\) is positive, but

\[
 \operatorname{tr}(\rho Y^{\otimes4}\bar\rho Y^{\otimes4})
 =\frac{1-A_3+A_4}{16}=-\frac12,
\]

contrary to nonnegativity of the trace product of two positive matrices. This proof also allows arbitrary complex entries and uses one common box, not three unrelated unitary completions.

## 4. Every surplus partition, including all degrees

The partitions of total surplus four are \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\). Equation (2) excludes the last, since at most two symbols have degree at least three. In \((2,1,1)\), the two surplus-one symbols must be the two degree-three symbols and the surplus-two symbol has degree two. A party with an odd surplus is incident only to T systems: F's pair excesses are all even. But §3 requires exactly one F pair at that degree-two, surplus-two symbol. Thus \((2,1,1)\) is impossible.

A \((3,1)\) party is also incident only to T systems. Its surplus-three symbol must meet three **distinct** positive-surplus symbols at every other party, because each T excess edge contributes one. Every partition with at least three positive parts has just been excluded. Thus only \((4)\) and \((2,2)\) remain.

Suppose party A has its entire surplus at \(a\). A T system incident to A would have all four positive edges at \(a\), forcing four surplus-one symbols at the opposite party. Hence AB, AC and AD are F. Two \((4)\) parties cannot be joined by F: both distinct multiplicity-four edges would have to be the same pair of their unique positive-surplus symbols. Therefore B,C,D each have two surplus-two symbols, their high sets \(H_B,H_C,H_D\). Every pair between those parties is T, and its four positive edges are exactly the complete high-by-high square. In the AB|CD cut the two F rows are \((a,b)\), \(b\in H_B\), and the four high CD columns are \(H_C\times H_D\). The F/T core therefore contains the full eight-word cube

\[
 \{a\}\times H_B\times H_C\times H_D. \tag{4}
\]

Each high-high pair among B,C,D has total multiplicity three, so it has exactly one extension outside \(a\). There can be no outside-\(a\) word high at all three parties. Indeed, if \((p,b,c,d)\) is such a word, \(h_A(p)=0\) makes each \((p,b),(p,c),(p,d)\) line have exactly two words. Comparing it with the corresponding full \(a\)-line forces the other word on each line to be high in the remaining coordinates. These three mates are distinct, since a high-high pair has only one outside-\(a\) extension. The four triples form a binary parity class: every two agree in exactly one coordinate. Write \(z_t=U_{a,t}\overline{U_{p,t}}\ne0\). The actual row inner product at the common coordinate of each pair is exactly \(z_t+z_{t'}=0\); three of these equations on a triangle are inconsistent over \(\mathbb C\).

Thus each high BC pair's unique outside extension is low at D, and similarly cyclically. Each high symbol meets both high symbols and at least one low symbol at each other party; its degree is at least three. Since the four degrees sum to ten, both highs have degree three and both lows degree two. Each high B has a unique low D neighbor, and each high C has a unique low D neighbor. The outside extensions of all four high BC pairs force these neighbors to be one common low D symbol \(\ell_D\). Similarly both high D symbols share one low B neighbor \(\ell_B\). The other low D symbol meets no high B, and cannot meet \(\ell_B\), whose degree two is already used by both high D symbols. It has at most the other low B as a neighbor, contradicting degree two. This excludes \((4)\) without assuming \(d_A(a)=2\); the degree-three and degree-four possibilities are included.

Consequently every party has exactly two high symbols of surplus two and two low symbols of surplus zero. Equation (1) now gives the following precise incidence. In a T pair the four multiplicity-three values are **all** high-by-high pairs. In an F pair the two multiplicity-four values form a matching between the high sets. All other E pair values in that system have multiplicity two.

## 5. Exhaustive elimination of F pairs

Any F edge forces its complementary edge to be T. Its F/T core contains eight all-high words: the two matched high values at the F side extend to all four high values at the opposite side.

### 5.1 Two F edges cannot coexist

Two distinct F edges must be adjacent. Suppose AB and AC are F. Their forced all-high boxes have union consisting, for every fixed high \((a,d)\), of the three words where B matches A or C matches A. Thus each of the four high AD pair values has at least three extensions. AD cannot be F, since F has only two multiplicity-four values and every other value has multiplicity two; hence AD is T. The complementary edges BD and CD are T as well.

For a fixed high D symbol, the union has six words and uses all three allowed occurrences of its pair with **each** high A, high B and high C symbol. Since all D-incident pairs are T, §3 excludes degree two for either high D symbol. Their degree sum forces both degrees to be three, so each has \(2\cdot3+2=8\) E words. Its remaining two words must be low at A,B,C, but it has only one low neighbor at each of those parties. At most one such triple exists. Contradiction; at most one F edge can occur.

### 5.2 The one-F case, with all sparse-row cases

Suppose AB is the only F pair. Label its two full rows \((a_0,b_0),(a_1,b_1)\), and let the two high C and D alphabets be binary. Both high symbols at C and D have degree three by §3 and the degree sum. Let \(r,r'\) be the other two AB rows in the 12-entry core. Their two-element supports partition the four high CD columns.

An axis partition is impossible. For example, if each support fixes C and varies D, a sparse row containing high A would add two entries to a high AC line already containing the two full-row entries, exceeding its T multiplicity three. The same holds for high B, so both sparse rows are low/low. Each high D sees both rows and already has both high A and high B neighbors. Its degree three permits only one low A and one low B neighbor, so the two rows would be identical. The other axis is symmetric. Thus the supports are the two complementary **diagonals**. Each high C or high D occurs once in each sparse row.

Classify a sparse row as X = high A/high B (necessarily off the F matching), Y = high A/low B, Z = low A/high B, W = low/low. No two sparse rows can share a high A or a high B: a high C line would then have its two full-row entries plus both sparse entries. If both use low A, those two low A symbols agree, since each high C already has both high A neighbors and degree three; likewise for low B. These facts and actual row orthogonality exhaust all unordered type pairs:

* **W/W:** the two low A coordinates and two low B coordinates agree, making the rows identical.
* **Y/Y:** after relabeling the rows are \((a_0,\beta),(a_1,\beta)\), with low \(\beta\). Choose high \(c,c'\) so the complementary diagonals have the same D value. The AC rows \((a_0,c),(a_1,c')\) overlap exactly once, at \((\beta,d)\); their full-row B values differ. **Z/Z** is symmetric.
* **X/X:** the rows are the two off-matching high/high values. Every high AB row is supported on high CD, and every high AC and AD row has exactly its two full-row entries plus one sparse entry, exhausting its T multiplicity. All three cuts close on the same binary box, impossible by §3.
* **X/Y:** sharing a high A was excluded. Otherwise the rows may be written \((a_0,b_1),(a_1,\beta)\). An AC row at \(a_0\) has full-row B value \(b_0\) at both high D values and a sparse \(b_1\) entry; one at \(a_1\) has full-row B value \(b_1\) at both high D values and a sparse low-\(\beta\) entry. These saturated T rows overlap exactly once. **X/Z** is symmetric.
* **Y/W:** the low B symbols must agree, so the rows are \((a_0,\beta),(\alpha,\beta)\). For high \(c\), the BC row \((\beta,c)\) has exactly the two sparse entries, with complementary high D values. Compare it with any \((b_0,c')\) row. The full row supplies one common \((a_0,d)\) entry. Its only third entry must have low D: any entry with both C,D high lies in the displayed core, whose two sparse rows have B=\(\beta\), not \(b_0\). Hence the overlap is exactly one. **Z/W** is symmetric.
* **Y/Z, matched:** the rows are \((a_0,\beta),(\alpha,b_0)\). An AC row \((a_0,c)\) has the full \(b_0\) pair at high D plus one \(\beta\) entry. An AC row \((\alpha,c')\) has one \((b_0,d)\) high-D entry and, by the same core exhaustion, its other entry at low D. They overlap exactly once. **Y/Z, crossed** remains.

The two residual arrangements, after relabeling, are therefore

\[
 \mathrm I:\ (a_0,b_1),(\alpha,\beta),\qquad
 \mathrm{II}:\ (a_0,\beta),(\alpha,b_1), \tag{5}
\]

with \(\alpha,\beta\) low. In either case \(\alpha\) appears in exactly one sparse row, whose diagonal meets both high C and both high D values. If \(d_A(\alpha)=2\), all four E words at \(\alpha\) would use high C,D, but the core has only two. Thus \(d_A(\alpha)\ge3\), and similarly \(d_B(\beta)\ge3\). If high \(a_1\) had degree two, its six E words would all use the two high C and two high D values already seen in its full row, yet that full row is its only row in the core and supplies only four. Thus \(d_A(a_1)\ge3\), and similarly \(d_B(b_0)\ge3\). The sums of the four degrees force, including the other low symbols \(\alpha',\beta'\),

\[
 \begin{array}{c|cccc}
 A&a_0&a_1&\alpha&\alpha'\\\hline d&2&3&3&2\end{array}
 \qquad
 \begin{array}{c|cccc}
 B&b_0&b_1&\beta&\beta'\\\hline d&3&2&3&2.
 \end{array} \tag{6}
\]

Fix a high C symbol. Its eight-word slice has six words at high D: four full-row entries and one in each sparse row. Its two remaining words share its unique low D neighbor. In either arrangement (5), the high-D six have A multiplicities \((a_0,a_1,\alpha)=(3,2,1)\) and B multiplicities \((b_0,b_1,\beta)=(2,3,1)\). The T multiplicities for high/high pairs are three and low/high pairs two. Therefore the two low-D words must be one of the two matchings

\[
 M_0=\{(a_1,b_0),(\alpha,\beta)\},\qquad
 M_1=\{(a_1,\beta),(\alpha,b_0)\}. \tag{7}
\]

The same statement holds with C,D interchanged. These are four distinct pair contexts: two high-C/low-D and two low-C/high-D. Every AB value in (7) is non-F and has multiplicity exactly two. In case I, \((\alpha,\beta)\) already has its two core entries, so no context can use \(M_0\). Four \(M_1\) contexts would give four distinct extensions of \((a_1,\beta)\), contradiction. In case II, each matching can occur at most twice, hence each occurs exactly twice. Then \(b_0\) and \(\beta\) have the three A-neighbors \(a_0,a_1,\alpha\), while \(b_1\) has the two A-neighbors \(a_1,\alpha\). Their degrees in (6) are exhausted. The remaining A symbol \(\alpha'\) can meet only \(\beta'\), contradicting \(d_A(\alpha')=2\). Thus no F pair exists. The entire pair-type list, including both axes, both residual arrangements and their symmetric counterparts, has been covered.

## 6. One common high support and exhaustive parity classification

With no F pair, §3 implies that no high symbol has degree two. The degree sum makes both highs degree three and both lows degree two at each party; high symbols occur in eight E words and low symbols in four. Write

\[
 \Omega=E\cap(H_A\times H_B\times H_C\times H_D). \tag{8}
\]

In a T/T cut X, the two high \(2\times2\) rectangles contain eight words of this **same** \(\Omega\); in a T/T cut Y, the high core contains twelve. Therefore all three cuts have the same type. If they were Y, the four omitted all-high words would project bijectively to every coordinate pair, since in every physical pair system each high row or column has one missing high position. Label them by their first two bits \((x,y)\). Bijectivity against both first and second coordinates forces each of the third and fourth bits to be \(x\oplus y\) plus a constant. Their joint projection has only two values, not four. So all cuts are X and \(|\Omega|=8\).

In every physical pair projection, each of the four high pair values occurs exactly twice in \(\Omega\). Put signs \(x_i\in\{\pm1\}\) on the high alphabets and \(F(x)=2\mathbf1_\Omega(x)-1\). Its Fourier coefficients of degrees zero, one and two vanish. Thus

\[
 F(x)=x_Ax_Bx_Cx_D\left(c_0+c_Ax_A+c_Bx_B+c_Cx_C+c_Dx_D\right).
\]

The coefficients are real. Since \(F^2=1\), the degree-one and degree-two coefficients of the bracket's square give \(c_0c_i=0\) and \(c_ic_j=0\) for \(i\ne j\). Exactly one coefficient is nonzero, of magnitude one. Up to party permutation and independent high-bit relabelings, \(\Omega\) is either a three-bit parity cylinder or a four-bit parity class. Both signs and all permutations are included.

### 6.1 Three-bit parity cylinder

Take \(\Omega=\{a\oplus b\oplus c=0\}\), with D free. In the AD|BC cut, the two high rows \((a,d_0),(a,d_1)\) with fixed high \(a\) occupy the same two high BC columns, differing in both B and C. They are the two high rows of one X component. Let its common low BC column be \(s_a\). If either coordinate of \(s_a\) were high, its two entries would add two to a high AB or AC pair already having two \(\Omega\) entries, contradicting T multiplicity three. Hence \(s_a=(\beta_a,\gamma_a)\) is low/low.

For fixed high \(a\), its four \(\Omega\) words plus the two words at \(s_a\) exhaust its two high-D pair lines. They also exhaust its pair lines to \(\beta_a\) and \(\gamma_a\), each of multiplicity two. Since \(a\) has degree three at each other party, its remaining two words have high B,C and a common low D neighbor \(\delta_a\). The pair row \((a,\delta_a)\) is a low AD row in a high X component. The two high BC columns it meets differ in both coordinates. Thus the low D symbol \(\delta_0\) has both high B and both high C as neighbors and, because its degree is two, all four of its E words have high B,C.

Every high BC pair has two \(\Omega\) extensions and exactly one further extension, and those four extra words are precisely the two low AD rows \((a_0,\delta_0),(a_1,\delta_1)\). The four words at \(\delta_0\) must therefore use both rows, so \(\delta_0=\delta_1=\delta\). Every high B symbol already meets both high D symbols via \(\Omega\) and \(\delta\) via these rows, exhausting its degree three. The other low D symbol \(\delta'\) can meet no high B, and its degree two forces it to meet both low B symbols. But \(\beta_a\) already meets both high D symbols in the two words at \(s_a\), exhausting its degree two. Contradiction, independently of component ordering and phases.

### 6.2 Four-bit parity class

For a four-bit parity class, the two high pair values on each side of either X component differ in **both** coordinates. Consider any pair \(ij\), its complementary pair \(kl\), and the two low \(ij\) rows of the X components. Suppose one row has low i-symbol \(\alpha\). Its two high \(kl\) columns use both high k symbols and both high l symbols. As \(\alpha\) has degree two and surplus zero, all its four E words have high k,l. Every high \(kl\) value already has two \(\Omega\) extensions and allows exactly one more; the four extra words are exactly the two low ij rows. Hence **both** low rows have i-coordinate \(\alpha\). The analogous statement holds for a low j-coordinate. A low row cannot be high/high, since every high/high T value has multiplicity three. It cannot be low/low, since the two rows would then have the same two low coordinates and be identical. Consequently the two rows have exactly one of the star forms

\[
 \{\alpha\}\times H_j\qquad\text{or}\qquad H_i\times\{\beta\}. \tag{9}
\]

If the first form holds, all four \(\alpha\)-words have j,k,l high. For either other party \(m\), the two pair rows \((\alpha,m)\), \(m\in H_m\), each have multiplicity two and are supported entirely on high complementary pair values. They are therefore the two low rows of the high X components in the \(im\) cut: every high complementary pair has only its one non-\(\Omega\) slot. Thus a star placing its low endpoint at i forces **every** pair incident to i to place its low endpoint at i, with the same low symbol.

Every one of the six edges has exactly one star endpoint. If AB places it at A, propagation places both AC and AD at A. Edge BC must place it at B or C. The first choice would force AB to place it at B, the second would force AC to place it at C. Both contradict the already fixed endpoints. This rules out the four-bit class. Together with §6.1 it finishes the proposed 4444 contradiction for one actual complex tensor.

## 7. Audit and boundary of the 4444 candidate

The reconstruction in §§1–6 addresses every load-bearing stage of S2: all actual cut components and T/F masks; all five surplus partitions; surplus-four at degrees two, three or four; impossibility of multiple F edges; all ten unordered pairs of sparse-row types, with both surviving patterns resolved; synchronization of the same high words across all cuts; the complete Fourier classification; and both low-incidence parity contradictions. The local complex equations use actual pair-row orthogonality or positive unitary norms; no assertion that supports alone admit a unitary is used. The boxed obstruction is proved by positive density matrices, not a real-phase specialization. This is an author's written reconstruction, **not** a parent disposition or independent-family, human, formal or kernel review.

The S1 notation erratum and S3's separate same-P/phase-frontier candidate were read as packet sources but are not imported as proof of the 4444 contradiction. S5's t25/t27 disposition is likewise not an input to the 4444 proof or to §8. Source links within all packet bodies are not authorization to read the linked files and were not opened. No statement about N=50 at another t, a global minimum, publication priority, novelty or a construction follows from §§1–6.

## 8. Separately conditional composition: exactly N=50, t=26

**Named import Q (not reproved here):** the separately adopted scoped statement in packet S4, `physics-6-actual-AME50-t26-entire-q5-exclusion-and-4444-frontier-parent-v1.md`, parent-supplied SHA-256 `67e216de5e5878d13448c261c3ec87ca4e000a9df235f878093bd246043e8321`: for every one normalized complex AME(4,6) tensor in one fixed product basis with \(N=50\) and \(t=26\) for \(U=6\psi\), each residual E alphabet has size four. S4 states this adoption, but the full bodies underlying its q5 and alphabet-profile reduction are not in this packet; its linked sources are not opened. Therefore Q is an explicit conditional import, not an independently established consequence of this candidate.

Assume Q and assume the written proof in §§1–6 is valid, including the reconstructed actual-unitary interface. Any such exact \(N=50,t=26\) tensor would satisfy Q and hence have q=4444; §§1–6 would then contradict its existence. **Conditional conclusion:** no normalized complex AME(4,6) tensor in a fixed product basis has exactly \(N=50,t=26\). This composition does not extend to other t, a global N=50 exclusion, minimum 51, a witness, independent-family review, or any priority assertion. Parent must separately disposition the 4444 proof, Q's import boundary, and this composition.

## 9. Complete reads and process declarations

Before packet-body reading or task-specific mathematical reasoning I read the entire manifest, freeze receipt, final pre-dispatch binding, parent-live metadata supply, actual-dispatch receipt, and each of the 22 manifest-listed status/permission controls through its ending. Initial non-raw administrative displays collapsed blocks; complete raw displays recovered them before I wrote `prebody-ack-v1.md` and sent a direct prebody acknowledgment to Main. Status-only controls were not mathematical inputs. The initial sole-owner directory listing contained neither new output name; the write interface did not expose an OS-level exclusive-create option, so atomic exclusive creation is not independently certified.

Only after both acknowledgments I read the sole packet part completely **in order**, using raw windows `1–20, 21–40, …, 401–420, 421–434`, including its actual ending. Each display was below 30,000 bytes; no packet clipping was observed and no clipped packet portion required recovery. The part contains complete rendered bodies S1 LF 1–3, S2 LF 1–182, S3 LF 1–172, S4 LF 1–22 and S5 LF 1–33, in that order. Parent-supplied part SHA-256 is `7628f3d1d1bb7ee9a8c0d8d30c79c817701c10be2f32fcc8d3fbfc9c34e85dc1`; the five original paths, source pins, sizes and terminal-LF flags are in the frozen manifest. I did not independently recompute hashes or open the original linked source files; supplied metadata is not correctness or source-identity certification.

All genuine held episodes and all proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT. No packet/status link, sibling science, network, external model, code execution, scientific evaluation, test, solver, child subprocess, compilation, build, lint, formatter, Git or deletion was used. No verifier was prepared and there is no code hash or computational verification. No process deviation beyond recovered administrative display elisions is known; neither unobservable cognitive isolation nor any parent/family/human/formal acceptance is asserted. Any correction is to be an additive new file, not an edit of this candidate.
