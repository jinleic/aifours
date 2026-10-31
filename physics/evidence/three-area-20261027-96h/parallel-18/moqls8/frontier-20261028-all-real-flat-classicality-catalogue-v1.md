# Conditional all-real-flat four-MOQLS(8) classicality: the last net obstruction

**Status: WRITTEN + independently checked finite-data candidate, pending mathematical review and catalogue-source authentication.** Let **Hcat** be the explicit external premise that every ordinary triple of order-8 MOLS, regarded as a five-class strength-two orthogonal array up to paratopy, is equivalent to one of the 39 triples in the two pinned local catalogue snapshots listed in `frontier-20261028-wanless-q1-species-reduction-v1.md` (SHA256 2f78091f08eb4c4fcf48cac7a29a7f1b559dd58aab000534b6a8e5e05541d73d). Hcat is NOT proved by this packet or its programs. Under Hcat and the explicitly named prior written real-flat input below:

1. Any actual ordinary four-MOQLS(8) with three classical members and a fourth real-flat member has all four members classical.
2. Any actual ordinary four-MOQLS(8) in which all four members are real-flat is classical memberwise.

Real-flat means that, for each member separately, one global output frame exists in which every cell ray has real ±1/sqrt(8) coordinates up to cell phase. The frames may differ among members; all eight rows, all eight columns, and all six original pair-product ONBs are required. This is not an unrestricted four-family theorem or an M(8) bound. A non-real-flat member, a nonclassical actual four-family outside this subclass, A10/A11, formal proof, family/human review and novelty remain untouched.

## 1. Inputs and the reduction to a finite net question

The named written input is `frontier-20261028-flat-real-q1-reduction-v1.md` (SHA256 d7f90ef8420ab431be46dc3753338cc92d425231aa1cc4a691532de2eb88c0d1), including its predecessor `frontier-20261028-flat-real-four-family-heavy-rigidity-v1.md` (SHA256 c19176626318f4ad2da6b597b5f32013d34d99cf3e4b871b744a69b20fad7568). Its precise claims used here are: (a) relative to any actual first-row ONB, real-flat entries are light first-row basis rays or heavy four-coordinate affine-plane rays, each nonzero squared coefficient 1/4; (b) an all-real-flat four-family has at most one nonclassical member. These are ordinary-written author candidates, not assumed independently reviewed. Claim 1 uses only (a); claim 2 additionally uses (b).

For three classical companions their row, column and three symbol classes form a five-net. As detailed in the species-reduction packet, the selected Q is an ONB on every line of all five classes: same-mate-symbol product orthogonality proves this for each of the three symbol classes. Thus any two net classes can serve as rows and columns without altering Q's real-flatness or memberwise classicality. Normalize each of the other three class symbols by its intersection with the chosen first row, so all three first rows equal 0,1,...,7.

For any non-first-row cell, orthogonality to its same-column first-row partner and its three same-mate-symbol first-row partners makes its Q ray avoid four distinct first-row labels: its column label and its three normalized companion labels. A heavy ray has exactly four nonzero coordinates, so its support is the complement of those four labels. Both the support and its complement must be affine two-planes in the first-row Walsh labeling. Enumerate all 30 affine-plane structures on the eight first-row labels. A cell satisfying this necessary condition is called eligible; the selected first row contains no heavy cell.

Every net line containing a heavy ray contains at least four heavy rays: on any axis in that ray's support no light basis ray may occur, and the ONB resolution of identity gives four 1/4 contributions. Iteratively remove eligible cells belonging to a net line with fewer than four eligible cells. An actual heavy set survives every removal. A zero resulting 4-core makes Q classical. Moreover, if a net line contains exactly four heavy entries, their four support sets are **identical**: on any coordinate used by one of them, the four required 1/4 contributions can only come from all four heavy entries.

The pinned 23,400-context screen and separate independent checker detailed in the species-reduction packet prove the following finite statements about the local snapshots: for 38 listed species an ordered pair of classes has zero core in all 30 affine structures; for remaining zero-based maximal species 22, in orientation (0,1), only structures 2 and 5 have nonzero core, and each has 32 eligible cells equal to its entire core. The 38-species implication uses only the zero-core condition, and Hcat supplies coverage of actual triples. What follows eliminates both exceptional structures by actual ONB support constraints; it does not assume the core is an actual family.

## 2. Explicit exceptional net

Use cell x=8i+j with row/column indices 0,...,7. The first rows have already been symbol-normalized. The three catalogue matrices are:

```text
L1          L2          L3
01234567    01234567    01234567
10325476    23017654    32106745
23017654    45760132    67543201
32106745    76452310    45760132
45760132    32106745    54671023
54671023    10325476    76452310
67543201    54671023    10325476
76452310    67543201    23017654
```

They are individually Latin and pairwise orthogonal; both independently checked scripts test these properties directly from the pinned source. Geometry 2 maps labels 0,...,7 to `[0,1,2,3,4,6,5,7]`; geometry 5 maps them to `[0,1,2,3,4,7,6,5]`. Addition in these coordinates is bitwise XOR. In the following eligible-cell boards, `#` denotes an eligible cell and `.` an ineligible one; rows are in order 0 through 7:

```text
geometry 2   geometry 5
........     ........
########     ########
....####     ####....
####....     ....####
....####     ####....
####....     ....####
....####     ####....
####....     ....####
```

In either board, row-class eligible counts are `[0,8,4,4,4,4,4,4]`; every line in each of the column, L1, L2 and L3 classes contains exactly four eligible cells. If any one eligible cell is heavy, every eligible cell on every incident four-eligible line is heavy. Those forcing lines connect the entire eligible board. For direct inspection, the following line chains start from cell (1,0), and each named line has exactly four eligible cells, meets the preceding union, and adds cells until all 32 eligible cells are included. Write Rk for row k, Ck for column k and L1=k for the L1-symbol-k line:

```text
geometry 2: C0, R3, R5, R7, L1=0, R4, R6, C4, R2, C2, C3, C5, C6, C7
geometry 5: C0, R2, R4, R6, L1=0, R5, R7, C4, R3, C2, C3, C5, C6, C7
```

Each four-eligible line gives a reversible all-or-none implication, so connectivity forces all 32 eligible cells heavy from **any** heavy starting cell, not only the displayed root. The explicit 31-edge forcing trees in the certificate give a second, machine-checkable presentation of the same connectivity. Therefore row 2 has exactly its four eligible cells heavy. By the four-heavy ONB lemma their supports must agree.

For geometry 2 the row-2 eligible cells are (2,4),(2,5),(2,6),(2,7). The forbidden-label sets at its first two cells are respectively `{0,3,4,7}` and `{1,2,5,6}`. Their supports are their distinct complements, so equality is impossible. For geometry 5 the row-2 eligible cells are (2,0),(2,1),(2,2),(2,3); the forbidden sets at its first two cells are `{0,2,4,6}` and `{1,3,5,7}`, again yielding distinct complementary supports. Thus neither of the only two nonzero-core cases admits even one heavy ray. All 30 structures force Q classical for species 22.

Combining the exceptional contradiction with the 38-species finite result proves claim 1 under Hcat and input (a). For claim 2, input (b) leaves at most one nonclassical member in any all-real-flat four-family; if one exists its three companions are classical, so claim 1 makes it classical too. Independent unitaries may identify each member's common ray basis separately, giving a classical four-family. No inference that every complex QLS is real-flat is made.

## 3. Finite certificate, checks and exact remaining obligations

- Exceptional producer `frontier-20261028-exceptional-net-support-certificate-v1.py`: SHA256 a091faa224c4191a280aa436faceb5f6acf194b1ce593b8c14408c43423e9870. Certificate `frontier-20261028-exceptional-net-support-certificate-v1.json`: 3b0d3e0cda916f6f7f313b5bd147ed9e4961584afee87c3baedb88eae393b14e. It records the actual normalized matrices, all eligible cells, all line counts, both 31-edge forcing trees and the unequal support witnesses.
- Independent finite verifier `frontier-20261028-exceptional-net-support-check-v1.py`: 298f02ff8440da2140e7f0fb45156eccd4cdb280b15bc897ab0790163d912c70; receipt `frontier-20261028-exceptional-net-support-check-receipt-v1.json`: ccaf9b88e232beccfdf62d58917be2726fdbd5ed43e1d228392b0339d7dec01a. It reconstructs the three actual source squares, independently recalculates all 30 cores, checks both spanning trees and both support clashes, and rejects mutations removing a tree edge, using a wrong line, repeating a support witness, omitting one geometry, and altering a net label. It does not prove Hcat or the written real-flat input.
- The two shorter chains printed in §2 were separately checked by `frontier-20261028-exceptional-line-chain-check-v1.py` SHA256 cc6d1bcd7ab8a46a6656e6951ed71dd99e19e36277726899053637c15da08c66; receipt `frontier-20261028-exceptional-line-chain-check-receipt-v1.json` SHA256 52b52659a8ae9227b87be0a1d63d43db9f7d0a990df228ed07cac45850e9e607. Each listed line has four eligible cells, overlaps the running union and adds cells; omission of the last line is rejected.
- The species-reduction packet pins the two local catalogue snapshots, the complete 39 × 20 × 30 screen, the separately reconstructed Steiner-plane/core checker and the 38-orientation selection. Its maximal snapshot is reader-paged with blank-separator normalization; the pinned local bytes are not asserted to equal the original HTTP bytes. Latin/orthogonality verification does not itself prove source fidelity or species completeness.
- Hcat is motivated by Ian Wanless's [MOLS catalogue](https://users.monash.edu.au/~iwanless/data/MOLS/) reporting 38 maximal and one nonmaximal species, with [format documentation](https://users.monash.edu.au/~iwanless/data/LSformat.html); [Egan–Wanless](https://arxiv.org/html/1406.3681) supplies the paratopy convention. These sources are not an independently replayed classification or novelty certificate. Correct matching of all source species to the pinned parsed triples remains a named assumption.

A disjoint reviewer should reconstruct (i) the real-flat input and all-variable five-line reorientation, (ii) the 30-structure coverage and the catalogue-to-snapshot boundary, (iii) both programs' complete context coverage and finite evidence, and (iv) the exceptional all-or-none support contradiction. No held result, previous solver UNKNOWN, numerical local minimum, or selected quantum witness is used as an input.
