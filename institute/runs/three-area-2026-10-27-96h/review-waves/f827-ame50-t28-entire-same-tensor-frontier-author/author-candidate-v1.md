# Actual AME(4,6), N=50, t=28: proposed whole-branch exclusion

**Status: prospective GENERAL AUTHOR candidate, NONBLIND, same harness; not an independent review or parent disposition.** The following is a proposed written proof, for arbitrary nonzero complex coefficients, that **no one normalized AME(4,6) tensor in one fixed local orthonormal product basis can have N=50 and t=28**. Here `U=6ψ`, `N` is the number of nonzero entries of `U`, and `t` is the number of entries of modulus one. The proof pays for the same 28 saturated words, 22 other words, six physical pair systems, three flattenings, all alphabet sizes, all surplus distributions, and arbitrary phases. It goes beyond a per-cut mask test. It is an exact-branch claim only: it neither excludes other t, proves a global N=50 exclusion, establishes a minimum, constructs an AME state, nor makes a novelty, priority, human, model-family, or formal-verification claim.

The proof uses the cut-alternative lemma stated by the parent disposition **S2** and reconstructed in the complete packet **S6**; §2 below gives the relevant written reconstruction, including the order-six/eight step. S2 mentions earlier f810/f811/f812 bodies that were not in this packet and were **not read**; their correctness or execution is not imported. If the reconstruction of the cut lemma is not accepted, the remaining same-tensor argument is an exact conditional exclusion **assuming that lemma**. No global t bound, no-OLS assertion, external enumeration, or other unprovided scientific body is needed.

## 1. Exact same-object bookkeeping

All six pair projections below refer to the same four physical parties. Let `P` be the 28 words at which `|U|=1`, and `E` the other 22 nonzero words. In each 36-by-36 balanced flattening `U` is unitary. A modulus-one entry exhausts its row and column, so every P word has a unique P pair value in each physical pair system, and no E word shares any such value. Removing the P rows and columns leaves an 8-by-8 unitary support with 22 entries, no degree-one line, and total excess `22−2·8=6`. Thus each physical pair system has exactly 28 P values and eight E values; each E value has at least two extensions. In particular all six projections and all subsequent sets are from this single P/E pair, never independent cut witnesses.

For each party i let `Q_i` be the set of symbols appearing in E, `q_i=|Q_i|`; for `x∈Q_i`, let `s_i(x)` be its number of E occurrences and `d_{ij}(x)` the number of its E partners in party j. The `6−d_{ij}(x)` other j-symbols are precisely the pair values occupied by P; since P is the same set, that number is independent of j. Write `d_i(x)` for the common value and put

    h_i(x) = s_i(x) − 2 d_i(x).

Every E pair line has at least two words, so `h_i(x)≥0`; summing over one pair system gives

    Σ_{x∈Q_i} d_i(x)=8,       Σ_{x∈Q_i} h_i(x)=22−16=6.          (1)

Also `d_i(x)≥2`: if it were one, all three other coordinates of every E word containing x would be fixed, giving at most one word although its E pair line has at least two. Therefore `q_i≤4`, and the eight E values in every pair give `q_i q_j≥8`. In particular, `q_i=2` forces all other q's to be four.

The same P set supplies a useful unrestricted moment identity. Let `n_k` count P words with exactly k coordinates in the respective Q alphabets. In party i, the number of such P incidences is `6q_i−8`; in pair ij it is `q_i q_j−8`. Counting P words, their incidences, and their pair incidences yields

    Σ_k n_k = 28,
    Σ_k k n_k = 6Σ_i q_i − 32,
    Σ_k C(k,2)n_k = Σ_{i<j}q_i q_j − 48,
    n_0+n_3+3n_4 = 12−6Σ_i q_i+Σ_{i<j}q_i q_j.                 (2)

The right side is `−6` for 3333 and `−3` for 3334. Consequently **at least two parties have q=4**: with no or one four and all q≥3 these are the only profiles; with a two, the other three are four. No other q, including 2444 or any high-surplus case, is omitted.

## 2. Cut lemma, and the boundary between masks and tensors

**Lemma.** Every cut of the actual N50/t28 tensor is either (F) two full 3-by-3 components and one full 2-by-2 component, or (B) one connected 4-by-4 component with 14 entries and two full 2-by-2 components. In B the two zero cells may initially share a row, share a column, or be disjoint. This is a necessary statement about each flattening, not an assertion that three chosen masks are jointly realizable.

For completeness, here is the reconstruction from S2/S6. In an actual unitary support each connected component is square; distinct rows or columns cannot meet in precisely one nonzero. In a component of order `m>2`, a degree-two row has two twin columns of equal neighborhood and degree at least three, and distinct degree-two rows have disjoint pairs. Equal pairs would isolate a 2-by-2 unitary, not merely a graph component; transpose the facts for columns. If component excess is e and there are k degree-two rows, then `k≥m−e` and `2k≤e`, so `m≤e+floor(e/2)`. Excess one is impossible; excess two is 3-by-3 minus one; excess three is full 3-by-3 (at order four the unique low row has twin columns of degree three, leaving a high row with at most two neighbors).

For excess four, order five is impossible: with one low row, its twins leave a degree-three high row avoiding them; that row uses all three other columns and meets a high row using the twins exactly once. With two low rows, the two twin pairs have degree three and their two-element high-row neighborhoods, subsets of three high rows, must coincide, leaving the third high row at most one column. At order six there are two low rows and columns and all other lines have degree three. The disjoint neighborhoods A,B of the low columns partition the high rows; each low-row twin pair has high neighborhood A or B. Equal choices leave rows of degree one, while different choices disconnect the component. Thus an excess-four component has order four.

For excess six and order six, exhaust k=0,1,2,3 low rows. For k=3, the three twin-pair high neighborhoods are two-subsets of three high rows; no one-overlap forces them all equal, leaving a high row empty. For k=2, twin-pair degrees are either (3,3) or (4,3). In the first case their two-subsets of four high rows must be disjoint; the other two columns have degrees two and four, and a row from each subset meets exactly in the degree-four column. In the second, the two remaining low columns have disjoint high-row neighborhoods A,B; a degree-four twin column has three high neighbors and meets one of A,B once. Both are impossible. For k=1, transpose the already excluded k=2,3 cases: there is at most one low column, so the low row's twin columns have degree three. Their two high neighbors have identical neighborhoods and, since at most one high row has degree four, both have degree three; their sole other common column cannot meet another row without a one-overlap, isolating a 3-by-3 component. For k=0, transpose to exclude low columns: the support is cubic. Repeated three-neighborhoods force an isolated K3,3; if all are distinct, each row meets exactly three other rows twice and two rows not at all, but its complementary three columns are unique, forcing those two disjoint rows to repeat a neighborhood.

For order eight/excess six there are two or three low lines on each side. If there are three low rows, their three twin pairs have degree three and the other two columns are low. Their disjoint high-row neighborhoods A,B use four of five high rows; each twin's two high neighbors must be A or B, leaving the fifth high row empty. Transpose to exclude three low columns. With two low rows and columns, all other lines are cubic. Let A,B be the disjoint two-high-row neighborhoods of the low columns and Z the two remaining high rows. A twin pair must use A, B, or Z. At least one pair uses Z, since Z rows need degree three and only two other high columns remain; both pairs cannot use Z. If the other uses A, both B rows must use both remaining high columns. The Z rows require a common one of those columns to avoid a one-overlap with their twins, making that column's degree at least four. Contradiction.

The positive component-excess partitions of six are `6`, `4+2`, `3+3`, `2+2+2`. The last requires order at least nine. The `4+2` components have orders four and three, leaving one unfillable residual order. The `3+3` case is F. A single excess-six component must have even order, at most eight; order two has zero excess, and orders six/eight are excluded, giving B.

## 3. An actual three-bit slice: all degree-two surplus cases

Fix a physical party i and an E-used symbol x with `d_i(x)=2`. Its neighbors in each of the other three parties form a two-symbol alphabet. Thus the x-slice is a subset of the actual binary three-cube, with exactly `4+h_i(x)` vertices and `0≤h_i(x)≤4`. For each of its three axes, the two rows `(x,0),(x,1)` of the corresponding actual flattening have norm one and are orthogonal. This uses **all three cuts of the same U**, not an abstract graph.

First `h_i(x)≠1`. Five retained cube vertices have at most five cube edges: deleting three removes at least `3·3−2=7` of the 12 edges. But on each axis the two actual row supports have sizes two and three, overlap at least once, and cannot overlap exactly once, so they overlap at least twice. The three axes would give at least six retained cube edges.

The important new `h=2` restriction is stronger. The six vertices are the cube minus two words. Those two omitted words must differ in **exactly two** of the three remaining coordinates:

* If they differ in one coordinate, an entire 2-point fiber of the other two coordinates is absent. The 2-by-2 table of squared moduli on those two coordinates has both row sums and column sums one, so opposite cell sums agree. The opposite fiber would also be absent, contradicting six nonzeros.
* If they differ in all three, relabel them 000 and 111. Write the six nonzero coefficients at 001,010,011,100,101,110 as `a,b,c,d,e,f`. The three actual row inner products give

      a conj(e) = −b conj(f),
      a conj(c) = −d conj(f),
      b conj(c) = −d conj(e).

  Multiplying the first and third equations and dividing by the second gives `b conj(e)=−b conj(e)`, impossible.

Distance two is not excluded merely by this local argument. For example, the six slice entries `(000,001,010,011,100,101,110,111)=(0,1/√2,−1/√2,0,1/2,1/2,1/2,−1/2)` have unit row norms and zero row inner products along all three axes. This is only an illustrative 2-by-2-by-2 slice, not a whole AME tensor or a three-cut completion.

If `h=2`, call the two omitted cube words H. In the axis on which they agree, the two x-rows have degrees 2 and 4; on either other axis they have degrees 3 and 3, overlap in two columns, and have different neighborhoods. In case F, the latter two rows would have to be in the same full 3-by-3 component and hence have identical neighborhoods. Thus **every cut is B**. In each cut the two x-rows lie in the 4-by-4 component: degree 4 forces this in the first case, while the intersecting degree-3 rows force it in the second. Their union has all four complementary columns, so the two missing cube words are exactly the two internal zero cells of that component. The same two actual four-coordinate words H therefore are the internal holes in **all three** cuts. They agree in exactly the two physical coordinates i and the shared cube axis.

If `h=3`, the slice has seven vertices. In every cut its two x-rows have degrees 3 and 4 and overlap in three of the four complementary columns, so every cut is B and the single omitted cube word is an internal 4-by-4 zero in every cut. If `h=4`, the slice has all eight vertices, and every cut is B because its two x-rows have degree four. These statements retain every allowed arbitrary complex phase; `h=0` is not discarded.

## 4. Two q=4 parties force one closed eight-word subsystem

For q=4, (1) and `d≥2` force `d=2` at all four symbols. Each h is in `{0,2,3,4}` and their sum is six. The only possibilities before further restrictions are `(4,2,0,0)`, `(3,3,0,0)`, and `(2,2,2,0)`. The last is impossible: two different h=2 symbols in the **same** party would each supply two internal holes in every B cut, but the two hole sets have different values in that party and cannot be the same two cells. Call the surviving profiles type X=`(4,2,0,0)` and type Y=`(3,3,0,0)`; the two positive-h symbols are called high, the other two low.

Each X party supplies its common two-word H by its h=2 slice. Each Y party supplies the same kind of H: its two h=3 slices supply distinct internal holes in every cut, exhausting both holes. If several q=4 parties occur, these are the **same actual two words**, since each cut has only two internal holes.

Take any two q=4 parties A,B, whose existence follows from (2). In their pair graph, label each E edge by its surplus `multiplicity−2`. Each vertex has exactly two neighbors and incident surplus sum h. In every pair system the cut lemma bounds an E-line multiplicity by four, so an edge surplus is in `{0,1,2}`. With rows/columns ordered by the two high symbols, the complete high-high edge set and its surpluses are, up to relabeling,

    X / X:  [ 2  2 ]     X / Y:  [ 2  2 ]     Y / Y:  [ 2  1 ]
            [ 2  0 ]             [ 1  1 ]             [ 1  2 ].     (3)

The X row order is h=4,h=2; Y has two h=3 symbols. Here is why no edge is being assumed. For Y, its two incident weights are 1 and 2, so neither neighbor can have h=0; with only two high symbols opposite, it meets both. An X h=4 vertex likewise has two weight-2 edges and must meet both opposite high symbols. This gives X/Y and Y/Y. For X/X, the h=4 vertices give the three weight-2 edges shown. The two h=2 symbols each force the same H; hence H agrees in both their A and B coordinates. In the actual AB cut the two holes are in their common row of the 4-by-4 component, so the h=2/h=2 pair is an E value of multiplicity two: the displayed zero-weight edge. All high degrees are now full. Consequently **there are no high-low E edges**, and the two low symbols on each side form a complete low-low K2,2 of multiplicity-two pair values.

Let L be the words with A low. Equation (3) makes this exactly the words with B low. Each of the four low-low AB pair values has two extensions, so `|L|=8`. In the actual AB cut these four low rows are the two external 2-by-2 components. For X/Y and Y/Y, all four high rows have degree 3 or 4 and must be the 4-by-4 rows. For X/X, the three degree-four high rows and the h=2/h=2 row containing the two actual holes are the 4-by-4 rows. Thus the remaining four low rows are external in every case, including the degree-two row inside the X/X core.

This detail is essential: a generic degree-two row of a 14-entry block need not be an external block. Here its location follows from the actual common holes, not from its degree alone. The four complementary pair values attached to the four L rows are therefore all degree-two columns in those two external blocks and have no E outside L. In every other pair system, at least one coordinate belongs to A or B; an L pair value contains a low A or B symbol, has multiplicity two because that symbol has h=0, and all its extensions lie in L. P cannot share an E pair value. Hence **in every one of the six physical pair systems L has exactly four values, each with exactly two extensions, and no P or E outside L shares those values**.

For a symbol x appearing in L, let `s_L(x)` count its occurrences and `d^L_{ij}(x)` its number of L partners at j. The two-extension statement gives `s_L(x)=2d^L_{ij}(x)` for every j; write the common value as `d^L_i(x)`. It is at least two: degree one would fix all three other coordinates and allow at most one distinct word. Since each pair has four values, `Σ_x d^L_i(x)=4`, giving at most two symbols per party. One symbol is impossible, because every symbol of another party would then have at most one partner in this party, contrary to `d^L≥2`. Thus each party has exactly two L symbols, each pair projection is the complete 2-by-2 set, and each of its four values occurs twice. Moreover the actual 4-by-4 matrix induced by L in every cut is unitary: every one of its rows and columns is an entire actual U line. Its degree-two support consists of two 2-by-2 blocks, since two rows of a longer 2-regular cycle would overlap in exactly one position.

The last conclusion is an actual closed-subtensor statement, not a choice of four new independent alphabets or of independent 2-by-2 witnesses.

## 5. No arbitrary-complex eight-word closed subtensor of that kind

Identify the two L symbols at each party with bits. Its indicator `f` on `{±1}^4` has size eight and every two-coordinate marginal equal to two. Let `g=2f−1` and `χ_S=∏_{i∈S}x_i`. Its Fourier coefficients of degrees 0,1,2 vanish, hence

    g = χ_{1234}(a_0+a_1x_1+a_2x_2+a_3x_3+a_4x_4).

Because `g²=1` pointwise, comparison of the characters `x_i` and `x_i x_j` gives `a_0a_i=0` and `a_i a_j=0` for i≠j; the constant coefficient gives `a_0²+Σ_i a_i²=1`. Thus exactly one coefficient is ±1. Up to physical party and bit relabeling, L is either the even-parity support on all four bits or the even-parity support on three bits times a free fourth bit. This is a complete classification, not an assertion that arbitrary pair-balanced supports have independently selected cuts.

For the three-bit case write the words `(a,b,a⊕b,d)` and let `r_ab` be the ratio of the **unit phases** of the d=1 and d=0 coefficients. The actual 2-by-2 row orthogonalities in cuts AB|CD and AC|BD give

    r_00=−r_11,    r_01=−r_10,    r_00=−r_10,

hence `r_00=r_01`. Orthogonality of the rows `(a=0,d=0)` and `(a=0,d=1)` in AD|BC instead gives `r_00=−r_01`. Contradiction. Only phases are divided; arbitrary positive moduli cancel in the two-term orthogonality equations.

For the four-bit case label a word by its first three bits abc, with fourth bit `a⊕b⊕c`, and write its unit phase as `z_abc`. The 2-by-2 squares in AB|CD at a⊕b=0, AC|BD at a⊕c=0, and AD|BC at a⊕d=1 respectively give

    z_000 z_111 = − z_001 z_110,
    z_000 z_111 = − z_010 z_101,
    z_001 z_110 = − z_010 z_101.

The first two imply the two right-hand products are equal, contradicting the third. These are phase identities, not the generally false equality of unnormalized complex products with unequal magnitudes.

Both possible supports are impossible. Section 4 therefore contradicts the actual tensor, and §1 guarantees the two q=4 parties required by §4. Subject to review of the stated cut lemma and the written derivations, **the entire exact N=50,t=28 branch is excluded**, not just a selected alphabet or independent-cut instance.

## 6. Explicit single-cut realizability is not AME realizability

The two necessary per-cut masks are locally realizable; the contradiction above is genuinely simultaneous. Let `H_2=(1/√2)[[1,1],[1,−1]]`, let `F_3` be the normalized 3-by-3 Fourier unitary, and define

    M = 1/(5√3) · [[ 0, 5, 5, 5],
                    [−5, 0, 5,−5],
                    [−7, 1,−4, 3],
                    [ 1, 7,−3,−4]].

The rows of M have squared numerator norm 75 and pairwise numerator inner product zero. It is orthogonal and has exactly the two disjoint zero cells shown. For a same-row-zero representative use

    R = [[ 1/√2,       1/√2,       0,    0],
         [ 1/(3√2),   −1/(3√2),   −2/3, −2/3],
         [−2/(3√2),    2/(3√2),    1/3, −2/3],
         [−2/(3√2),    2/(3√2),   −2/3,  1/3]].

Its first row is orthogonal to the remaining three; those three are obtained by a 3-by-3 orthogonal Householder matrix applied to the orthonormal basis `(1,−1,0,0)/√2,(0,0,1,0),(0,0,0,1)`. The transpose has same-column zeros. Thus `I_28 ⊕ F_3 ⊕ F_3 ⊕ H_2` is a 36-by-36 unitary with the F mask, while `I_28 ⊕ M ⊕ H_2 ⊕ H_2` and its R replacements realize all B zero-mask types. Each has exactly 28 modulus-one entries and 50 nonzeros. These are **one-cut matrices only**. Reshaping one into a four-party tensor does not establish the other two flattenings are unitary, and the above argument proposes that none can be a whole AME tensor with these counts.

## 7. Source and process declaration

Before any packet-body reading or mathematical reasoning I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all 22 listed controls through their endings; controls were status/permission only. I wrote the direct `prebody-ack-v1.md` first. I then read the one ordered packet serially in raw windows `1–20, 21–40, …, 381–400, 401–408`, including all endings; each window was below 30,000 displayed bytes. No clipping or recovery of packet content was needed. An initial attempted read of 181–200 used a mistyped path and returned only `not found`; I immediately read that window at the correct path before continuing. No packet body or mathematical reasoning preceded the acknowledgment.

Parent-declared packet metadata: 75,271 bytes, 408 LF, SHA-256 `39fcfcdd588d30595023a246084e3b021da5b2d94be5841e2f35bd1451fb404d`. Its complete source bodies and parent-declared SHA-256 pins are:

| ID | Original LF | Parent-declared SHA-256 |
|---|---:|---|
| S1 | 1–33 | `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336` |
| S2 | 1–23 | `f84c4b2eba89f99b693fa1c9fdfd5b4ef90eb5e6f7d9c5a99ca7373cc11fd0dc` |
| S3 | 1–21 | `85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9` |
| S4 | 1–34 | `876bf145aca1439a6854d2008c82f0afd16d5d0181782bcf675ff41818119057` |
| S5 | 1–161 | `3752d4b981b70d4626dbda6a87644044332ffd2e431a624f753fcccf9257d4f9` |
| S6 | 1–110 | `61dfb5205f9b6bf2022c17d6149f1926571c48d24307556f67a7f2201b684197` |

These are supplied metadata, not my independent hashes, original-source identity certification, or correctness evidence. I did not follow packet/control links, open unlisted science, inspect held episode bodies or any of their consumers, use sibling outputs, network, external model, scientific execution, code, subprocesses, solvers, tests, compilation, build, lint, formatter, Git, or deletion. No executable was prepared and there is no code hash or computational verification. The concrete matrices and identities are written derivations, not claims of a run. All genuinely held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remain NONINPUT. The parent must independently read and dispose of this proposed proof; later corrections must be new additive files, not edits to these bytes.
