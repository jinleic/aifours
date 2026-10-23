VERDICT (STRUCTURAL REDUCTION ONLY): ACCEPT

References below are LF line numbers in [case-split-r1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/btd12-20-parent-inputs-v1/case-split-r1.md). The supplied SHA-256 matches.

- **Fatal:** No defect found in the mathematical reduction.
- **Major:** None in Lemma T, the abstract E0/E1 cover, or the stated Part D predicate. Completeness of the actual generated representative files remains unverified.
- **Minor:** The title and Part D heading overstate the established result (LF 1, 95). “Free” columns (LF 76) means zero columns of **A**; each still requires three entries of **D**. No complete nonexistence verdict is accepted.

**Part A is valid (LF 16–25).** Expanding the row product gives the stated coefficients \(1,2,2,4\); reduction modulo two forces even intersections of A-row supports. Distinct supports therefore meet in zero or two points. Equal supports remain separate rows with multiplicity. The column equation gives \(a_j=6-2d_j\in\{0,2,4,6\}\).

**The split-consistency argument is valid (LF 39–45).** Suppose two parts share exactly one point \(z\). They cannot belong to the same tetrad. Their tetrads intersect and hence are adjacent. Under the common-split hypothesis, their intersection is exactly the part containing \(z\) in each tetrad. Thus the two parts are equal, contradicting their one-point intersection. Consequently all parts are equal or disjoint and partition the support. Connectivity ensures every tetrad has a neighbour, except the explicitly handled singleton.

**The seven-point seed is forced (LF 46–52).** Different unordered splits can be labelled
\[
T=1234,\qquad T_1=12ab,\qquad T_2=13ad.
\]
The neighbours already share \(1\), so their required intersection of size two forces exactly one shared point outside \(T\). Their remaining outside points differ. Thus all seven displayed points are distinct. The seven nonzero sums listed in the document are indeed distinct weight-four words.

Here is an independent derivation of the code facts used afterward, without a length-24 theorem:

- The seven coordinate columns of the three seed generators are precisely the seven nonzero vectors of \(\mathbf F_2^3\). Every nonzero linear functional is one on four coordinates, giving a dimension-three code \(C_7\) with weights \(0,4\).
- Its dual consists of subsets whose coordinate labels sum to zero. The triples are exactly \(\{u,v,u+v\}\): seven triples, since the 21 unordered pairs each belong to one triple, with three pairs per triple. They form the Fano lines.
- The all-seven vector is in the dual. Therefore the seven complementary tetrads are also in the dual. Together with zero and all-seven, these give 16 words, exhausting the dimension-four dual. Its weight distribution is
  \[
  1+7z^3+7z^4+z^7.
  \]
  Its seven weight-four words are exactly \(C_7\setminus\{0\}\).

**The extension and induction are valid (LF 53–64).** For a Fano line \(L\) and a new coordinate \(y\), adjoin \(v=L\cup\{y\}\). This generator has even weight and is orthogonal to \(C_7\). The resulting length-eight code has dimension four, hence is self-dual.

Among the seven nonzero words of \(C_7\), precisely \(X\setminus L\) is disjoint from \(L\); the other six intersect it twice. Consequently the new coset has one weight-eight and seven weight-four words. The complete weight distribution is
\[
1+14z^4+z^8.
\]
Its tetrads are the seven old tetrads and the seven sets \(L'\cup\{y\}\). Labelling \(y=0\) identifies these with the affine planes of \(\mathbf F_2^3\). In-memory enumeration independently confirmed both distributions and all seven possible line extensions.

Connectivity permits an ordering starting with the connected seed. A later tetrad restricts to a dual word on the current support and meets an earlier tetrad twice. On seven points its restriction therefore has weight three or four: four stays inside \(C_7\); three introduces exactly one coordinate and produces the extension above. On eight points, self-duality and weights \(0,4,8\) force restriction weight four, leaving no room for another coordinate. Self-duality is proved only for this local eight-coordinate code, never presumed for the unknown full row code.

**E0/E1 is a complete mathematical cover (LF 69–81).** Different adjacency components have disjoint supports: a shared point would force intersection two and join them. In a pairable component, each row joins two distinct pair-vertices, so loops are impossible. Repeated rows give parallel edges; weighted vertex degrees are precisely the A-column multiplicities, hence \(2,4,6\).

For E0, twelve edges give degree sum 24, forcing \(n\ge4\); twenty columns force \(n\le10\). Each non-pairable component occupies seven or eight distinct columns, so at most two fit. Combining these with all pairable components and padding to twenty columns with zero A-columns proves coverage under row and column permutations. Uniqueness of representation is unnecessary. The counts 2069/1004, nauty invocations, and orbit implementation are not established by this argument (LF 82–93).

**Part D is exactly the completion predicate (LF 96–97).** Binary \(D\), supported off \(A\), with the stated margins makes \(M=A+2D\) have exactly four ones, three twos, and column sums six. Entrywise multiplication gives exactly the displayed integer pair equation, proving both necessity and sufficiency. The index \(i<k\) merely indexes unordered row pairs. No simplicity, column-distinctness, D-ordering, or D-orbit restriction appears. Paired columns coincide only in \(A\); their D-entries remain independent.

The solver statuses and unfinished certificates (LF 98–108) supply no verified nonexistence conclusion.