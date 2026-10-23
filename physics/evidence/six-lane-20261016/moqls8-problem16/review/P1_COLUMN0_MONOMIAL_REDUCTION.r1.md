# P1 column-0 monomial reduction r1 — mathematical candidate, NOT a production cutover

Status: exact proof candidate below, not independently reviewed. No strengthened CNF has been generated or
solved. Current signed-cube protocol, all old ledgers and the native lifecycle HOLD are unchanged. This note
proposes a DIFFERENT semantic cover, not a completion of the frozen Boolean16-cover ledger. Any use needs
parent approval/amendment, review and independently measured refutations. No novelty/priority claim.

Primary hypotheses are the QLS/MOQLS definitions in sources/2607.12933v2.raw.txt (195–225), row-0 standard
form, and the P1 templates already frozen in K5_COLUMN0_TEMPLATE_COVER.r1.md (1ae1c81d…d9a). The one-P4
bridge/parent conditional disposition supplies their connection to the original n8 target; this note assumes no
P4 property for squares2–5. Matched computational baseline: F_one P1-B1/B2/B3/B5 were UNKNOWN in the unchanged
900-s producer pass. Nothing here establishes a faster running time, a full QLS extension or a physical counterexample.

## 1. Exact local claim

Put row0 of each of five QLS in the standard basis. Restrict column0 to rows i=1..7 and coordinates c=1..7;
coordinate0 is absent since every other column0 vector is orthogonal to its common (0,0)=e0. Write U_s for the
resulting7×7 unitary support matrix. For fixed(i,c), at most one U_s has a nonzero entry: MOQLS orthogonality on
the two cells(0,c),(i,0) forbids two nonzero factors. Thus the five support matrices are entrywise disjoint.

Suppose U_1 has a P1 template: rows1,7 have support A={1,2,3}, row6 has support{2,3}, and rows2..5 have one of
B1..B6 on B={4,5,6,7}. Call U_s MONOMIAL if every column0 vector is a basis ray in the row0 frame, equivalently
U_s is a support permutation. This is a property of ONE COLUMN, not a claim that Q_s is a classical QLS.

**Claim:** at least one of U_2,U_3,U_4,U_5 is monomial. Stronger guaranteed lower bounds by B type are

| P1 type | support count of U_1 | minimum number of monomial U_2..U_5 proved here |
|---|---:|---:|
| B1 |12|1|
| B2 |14|1|
| B3 |16|2|
| B4 |18|3|
| B5 |17|2|
| B6 |20|4|

These are LOWER BOUNDS, not claimed exact optima for full MOQLS. The B1 bound1 is sharp for the stated LOCAL
unitary/disjointness hypotheses, as the explicit partial configuration in §3 shows.

## 2. Complete elementary proof

Each unitary has a nonzero in every row and column. Disjointness gives total support degree at most7 at each
row/column, so each individual degree is at most3. A singleton row/column of a unitary is an isolated1×1 block.

Rows1,7 of U_1 have degree3, so in every other U_s both rows are singleton B entries, using DISTINCT B coordinates.
Columns2,3 of U_1 have degree3, so in every other U_s both columns are singleton. Those two singleton columns
occupy two further isolated rows, neither1 nor7. Also neither is row6: U_1 uses(6,2),(6,3), so disjointness forbids
them in U_s. Removing these four isolated edges leaves a3×3 unitary R_s whose rows include6 and whose columns
are {1} plus two B coordinates. Its distinguished row6 and column1 each have degree at most2, because U_1
has degree2 at row6 and at column1 and the other three squares each need at least one entry there.

A3×3 unitary with those distinguished degrees is either monomial, K22 plus an isolated edge, or K33 minus the
single edge(6,1). Proof: if a degree1 exists, remove its isolated edge; the residual2×2 unitary is monomial or
dense. Otherwise every degree is at least2. Two zeros cannot share a row/column, and zeros in different rows
and columns would make those two degree2 rows overlap in exactly ONE nonzero coordinate, impossible for
orthogonal vectors. Hence there is exactly one zero, forced to be at(6,1) by both distinguished degree bounds.
This argument is valid over complex numbers; a single product of two nonzero entries cannot cancel.

Let X be the other squares with column1 degree2, and Y those with row6 degree2. Each set has size at most1:
U_1 contributes2, four other nonempty degrees contribute at least4, leaving only one extra degree out of7.
If U_s is nonmonomial but lies outside X∪Y, its R_s is K22 plus an isolated edge. Its distinguished row6 and
column1 both have degree1, so they must be that SAME isolated edge(6,1). At most one square can have this
edge by disjointness. Therefore the number of nonmonomial U_2..U_5 is at most |X|+|Y|+1 ≤3. This proves
at least one monomial column0 among the four others. In particular, this proof does NOT assert at least two.

For the remaining table bounds, a nonmonomial7×7 unitary has at least9 support entries: a nontrivial unitary
component has at least two rows of degree≥2 (one degree≥2 row cannot coexist with six isolated1×1 blocks).
Thus, if k of the other four are nonmonomial and U_1 has m entries, their disjoint supports use at least
m+4×7+2k ≤49 entries. Combine k≤floor((21−m)/2) with k≤3. Substituting m=12,14,16,18,17,20 gives the table.

## 3. Sharp local B1 configuration, not a full5-MOQLS(8)

All five row0 frames are e0..e7 and all column0 vectors at row0 are e0. Below, row labels are1..7 and an integer
means the corresponding standard basis vector. Let h(a,b)=(e_a+e_b)/sqrt2 and k(a,b)=(e_a−e_b)/sqrt2.

- Q1 column0: ((e1/sqrt2)+(e2+e3)/2), 7, 6, 5, 4, k(2,3), ((e1/sqrt2)−(e2+e3)/2).
- Q2 column0: 4, 1, 3, 2, h(5,6), k(5,6), 7.
- Q3 column0: 5, 3, h(1,7), k(1,7), 2, 4, 6.
- Q4 column0: 6, 2, 5, 3, 1, 7, 4.
- Q5 column0: 7, h(4,6), 2, k(4,6), 3, 1, 5.

Each is an orthonormal basis, and their supports are disjoint at every off-row0 position(i,c). Only Q4 is
monomial among Q2..Q5. Thus a proposed LOCAL bound of at least TWO others would be false. The15 specified
cells (row0∪column0) give a valid partial configuration; the other49 cells are UNSPECIFIED. This is neither a
Boolean model of the full F_one CNF nor a nonclassical5-MOQLS(8) counterexample.

Q2 row2 has A-profile100 (L1 index1 in the frozen little-endian convention), and row3 has A-profile001 (L2
index4). The partial configuration therefore lies in the signed cube P1-B1.L1.001.L2.004, but does NOT satisfy
or refute its full-CNF completion problem. It shows exactly where a solely local argument cannot exclude that
leaf. A separate exact Q(sqrt2) checker/controls may verify this finite witness; no such run is claimed by this freeze.

## 4. Proposed six-case semantic cover for the four hard P1 templates

This is a proposal only; current requirement remains all16 exact F_one closures under its signed-cover route.
For s=2..5 let M_s mean that Q_s column0 is monomial. Residual coordinate permutations in B must be paired
with the same common column/reference relabelling and a standardizing permutation unitary, then square
relabelled by s→sigma(s+2)−2 for s2..5. This retains SB2 at(1,0). Q1 is fixed as a LABEL; its support sets, not
its actual vectors, are preserved. Common row re-sorting of rows2..7 imposes ROWLEX again, using the same
support-mask comparator as the accepted template normalization. Column0, row0 and row1 stay distinguished.
Monomial-column status is invariant under these permutations/re-sortings.

The following support stabilizer subgroups suffice (not a claim that these are the full stabilizers):
- B1: Sym(B), restoring the four singleton B rows by their common row permutation; transitive on B.
- B2: generators(4 5),(6 7); (6 7) is paired with row swap(2 3), while(4 5) preserves the two equal support rows.
  The B orbits are{4,5},{6,7}.
- B3: generators(4 5),(6 7),(4 6)(5 7); the last is paired with row swaps(2 4)(3 5). This is transitive on B.
- B5: generator(5 6) preserves every Q1 column0 support set; the orbits are{4},{5,6},{7}.

Thus a genuine configuration may be normalized into at least one of these restricted cases:

| source template | proposed extra property | number of cases |
|---|---|---:|
| P1-B1 | M2 |1|
| P1-B2 | M2 or M4 |2|
| P1-B3 | M2 |1|
| P1-B5 | M2 or M3 |2|

For B5, the lower bound2 ensures a monomial square has row1 label outside the singleton orbit{7}; hence one
can choose orbit{4} or{5,6}, not an omitted seventh case. For B1/B3 transitivity sends any available monomial
square's row1 label to4. For B2 choose its orbit representative4 or6. After each transformation the original
nonclassical five-square set remains such, Q1's chosen weight3 witness persists, the SAME P1 support template
persists, and the accepted canonical-auxiliary-extension argument applies to F_one. No full-CNF automorphism
on arbitrary Boolean assignments is claimed. This is a SEMANTIC cover, not a Boolean8-sign partition.

If later approved, one can impose M_s with126 negative binary clauses:
for i=2..7 and1≤c<d≤7, NOT g_s((0,c),(i,0)) OR NOT g_s((0,d),(i,0)). Existing SB2 already makes row1 a
basis ray, and QLS/G3 nonemptiness gives exactly one coordinate in every other row. These constrain only
column0, not the whole square; no K4/global-classical assumption is introduced. There are no new variables.
A source leaf5740268clauses plus126 would have5740394clauses. No such formula/encoding has been generated,
no runtime forecast is asserted, and no old-F/c112/producer proof is imported by this proposed route.
