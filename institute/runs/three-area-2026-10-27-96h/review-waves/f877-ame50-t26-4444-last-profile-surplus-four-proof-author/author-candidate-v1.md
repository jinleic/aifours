# The actual 4444, r=2 profile: surplus-four exclusion and a six-slice obstruction

**Prospective general-author candidate; nonblind, same harness; not a parent disposition.** This is a written argument about one actual tensor and its actual shared support. The S2 author candidate supplied the target and the A/B/C interface; the additional six-slice argument below strengthens that interface. No surviving support or phase solution is asserted to exist. All claims are restricted to the hypotheses immediately below.

## 1. Exact quantified statement

Let `ψ` be any normalized complex four-party state in one fixed local product basis of local size 6, and set `U=6ψ`. Suppose all three balanced 36-by-36 flattenings of this **same** array are unitary; its support consists of 26 modulus-one words `P` and 24 further nonzero words `E`; each E-used local alphabet `Q_i` has exactly four symbols; and exactly two P words are inside all four `Q_i`, with each other P word inside exactly two. In the packet notation this is the whole `(n_0,n_1,n_2,n_3,n_4)=(0,0,24,0,2)` or `r=2` profile. All E coefficients below are arbitrary nonzero complex numbers satisfying the actual unitarity equations; no uniform-modulus or sign ansatz is made.

For `a∈Q_i`, let `d_i(a)` be the number of E-neighbors of `a` in any other party, and let `h_i(a)=|{x∈E:x_i=a}|−2d_i(a)`. These definitions are justified in §2. Then, necessarily:

1. Every party has two degree-two symbols `D_i` and two degree-three symbols `T_i`. The two all-inside P words `w^0,w^1` differ in every coordinate and use precisely `D_i` at party `i`. For each `a∈Q_i` and `m∈{1,2,3,4}`, if `z_m(a)` counts P words containing `a` with `m` inside coordinates, the identities in §2 hold, including `z_4(a)=3−d_i(a)` and `z_2(a)=3`.
2. No symbol has `h_i(a)=4`. In particular the two proposed `h=4` degree cases are both excluded by the actual shared-support arguments in §4.
3. Before the additional obstruction in item 4, the exhaustive degree-labelled partitions of the four surplus units are **A**: two symbols with surplus 2; **B**: the two degree-three symbols have surpluses 3 and 1; or **C**: one degree-two symbol has surplus 2 and both degree-three symbols have surplus 1. In the hypothetical B case, every other party is C, the three C degree-two positive-surplus symbols have bits relative to `w^0,w^1` of both kinds, and there is at most one B party (§5).
4. In fact an actual degree-two, surplus-two E slice is a six-vertex binary cube with its two omitted vertices at Hamming distance exactly 2 (§6). Consequently **C is impossible and hence B is impossible** (§7). Thus all four parties necessarily have type A, with its two surplus-two symbols in any of the degree positions not ruled out by the next item. This strengthens the packet's stated A/B/C necessary list; it does not rule out the entire profile.
5. Define a graph on the four parties with edge `ij` precisely when the actual `ij` E-pair-line multiplicities are two 4's and eight 2's. At any party whose type A includes a degree-two surplus-two symbol, its graph degree is exactly one. Two disjoint graph edges are impossible. Therefore at least one party has **both** degree-three symbols of surplus 2 and both degree-two symbols of surplus 0. If exactly three parties have a degree-two surplus-two symbol, the graph is the star centered at the remaining party (§8).

Each conclusion is a necessity, not a realization or a global `t=26`/`N=50` exclusion. Items 3's B-conditional restrictions are retained explicitly even though item 4 subsequently excludes B.

## 2. Same-tensor incidence and per-symbol identities

In every physical pair system, a modulus-one entry of a unitary row and column is the sole entry in each. Thus the 26 P pair values are distinct, no E word has one of those values, and the other ten pair values are all used by E. Every such E line has at least two entries: a singleton unitary line would have a modulus-one entry. These statements also apply to the complementary pair system, i.e. the transpose of the same cut.

Fix `i` and `a∈Q_i`. In the `ij` pair system, the P words with `i` symbol `a` occupy distinct pair values, and each of the six pair values at `a` is either one of these P values or an E value. Therefore the number `d_i(a)` of E neighbors at `j` is `6−#{p∈P:p_i=a}`, independent of `j`. A degree-one E symbol would fix all three other coordinates and give at most one E word, contrary to the two-entry E-line rule. Hence `d_i(a)≥2`. Since there are ten E pair values and four E symbols,

```
Σ_{a∈Q_i} d_i(a)=10,
Σ_{a∈Q_i} h_i(a)=24−2·10=4,
h_i(a)=Σ_{b: (a,b) is an E value} (multiplicity(a,b)−2)≥0.
```

Here the final expression is valid in every `ij` system and will be used repeatedly. For `z_m(a)` as in the theorem, an E neighbor at `j` is in `Q_j`, and exactly `4−d_i(a)` values `(a,b)` with `b∈Q_j` are P values. Counting P words and their inside neighbors gives

```
Σ_m z_m(a) = 6−d_i(a),
Σ_m (m−1)z_m(a) = 3(4−d_i(a)),
z_1(a)−z_3(a)−2z_4(a) = 2(d_i(a)−3).             (1)
```

Under the specified profile `z_1=z_3=0`; solving the first two equations gives

```
z_4(a)=3−d_i(a),       z_2(a)=3.                     (2)
```

As `d_i(a)≥2`, nonnegative `z_4` gives `d_i(a)≤3`; the degree sum forces the multiset `2,2,3,3`. Every degree-two symbol occurs once in the two all-inside words and every degree-three symbol occurs zero times. Therefore the two all-inside words differ at every party and their symbols are exactly `D_i`. In fact for each `j≠i` every `a∈Q_i` occurs in exactly one P word whose inside coordinates are exactly `i,j`: among the `4−d_i(a)` inside P neighbors at `j`, `z_4(a)` are supplied by the all-inside words, leaving one.

## 3. Actual-unitary cut lemma and binary-slice parity

We reconstruct the cut fact used below. Deleting the 26 saturated P rows and columns of a flattening leaves a 10-by-10 unitary with 24 entries, minimum line multiplicity 2 and excess 4 over two entries per row. Each connected support component is square. Distinct rows or columns cannot meet in exactly one nonzero position.

For a component of order `m>2`, a degree-two row has two **twin columns**: every other row meeting either must meet both, and each twin has degree at least 3. If they had only the low row and one other row in their common support, those two orthonormal columns would exhaust those rows and isolate a 2-by-2 block. Two degree-two rows have disjoint twin pairs: one shared column gives singleton overlap, while a shared pair forms an isolated 2-by-2 block. If the component's excess is `e` and its number of degree-two rows is `k`, counting row excess and the column excess of the `2k` twin columns yields

```
m−e ≤ k ≤ floor(e/2),   hence m ≤ e+floor(e/2).     (3)
```

The same facts hold with rows and columns interchanged. An excess-zero component is a 2-by-2 block; excess one is impossible; and an excess-two component is a 3-by-3 block with one zero. Since the total excess is 4, the only alternatives are two excess-two components plus two 2-by-2 blocks, or one excess-four component plus excess-zero blocks. In the latter case (3) gives `m≤6`. Orders 5 and 6 cannot occur:

* For `m=5,k=1`, the other four rows have degree 3. If some but not all meet the low row's twins, a row avoiding the twins uses all three remaining columns and meets a row using them in exactly one column. If all four use the twins, those rows have only four entries among the other three columns, fewer than their required six. For `m=5,k=2`, the four twin columns each have degree 3 and exhaust the excess, so the fifth column has degree 2. The two twin pairs choose two-element subsets of the three high rows. Different subsets intersect once, violating column orthogonality; equal subsets leave the third high row with at most one neighbor.
* For `m=6`, necessarily `k=2`, all four high rows have degree 3, all four twin columns have degree 3, and the two remaining degree-two columns have disjoint supports partitioning the four high rows. Each twin column's two high neighbors must be one whole part of that partition, otherwise it meets a low column once. If the twin pairs choose the same part the other high rows have too few neighbors; if they choose different parts the component splits.

Thus the single excess-four component has order 4 and 12 entries. On either side its degree partition is one of `3333`, `2334`, `2244`. The middle partition is impossible: the degree-two row's twins of degree 3 leave a high row unable to reach degree 3 outside them; if they have degree 4, the two other columns have degree 2 and both meet the degree-four row, forcing either a singleton overlap or an isolated 2-by-2 component. In the `2244` case the two low rows have disjoint neighbor pairs and the two full rows share all four opposite columns, each of which has degree 3. Consequently **every physical pair side** has either four 3-lines and six 2-lines, or two 4-lines and eight 2-lines; a 3-line and a 4-line never occur on that side. On a side with two 4-lines, their opposite side has four 3-lines and six 2-lines, and the two full rows have the same four opposite values.

For a degree-two E symbol the slice lies in a binary 3-cube and has `4+h` vertices. If `h=1`, its five vertices have at least one edge in every coordinate direction by pigeonhole; no row overlap can be a singleton, so they have at least two edges in each direction. But deleting three vertices from the 12-edge cube removes at least `9−2=7` edges (three cube vertices induce at most two edges), leaving at most five. If `h=3`, seven cube vertices yield one 4-line and one 3-line in the same pair side. Both cases are impossible. Together with `Σh=4` this gives

```
d_i(a)=2  ⇒  h_i(a)∈{0,2,4}.                        (4)
```

## 4. Excluding surplus four in both degree cases

Suppose first `d_i(a)=3,h_i(a)=4`. The `a` slice has ten words. In each `ij` system its three lines must have multiplicities `4,4,2`: the cut lemma forbids mixing a 3-line with a 4-line. Let the two 4-lines share the actual set `S` of four complementary `(k,l)` values, and call the two words on the remaining line `(a,b_low,x_1,y_1)` and `(a,b_low,x_2,y_2)`. In the `ik` system the `a` slice also has line multiplicities `4,4,2`; all are even. For any fixed `k` value, the two full `ij` lines contribute twice the number of elements of `S` with that `k` value, hence an even number. The two low-line words must contribute an even number as well, so `x_1=x_2`. The identical argument using `il` gives `y_1=y_2`, contradicting distinct support words. The actual common core and all three pair systems are essential here.

Now suppose `d_i(a)=2,h_i(a)=4`. Its eight distinct E words are the full cube

```
{a} × H_j × H_k × H_l,       |H_j|=|H_k|=|H_l|=2.    (5)
```

The two `(a,b)` lines at each other party are 4-lines. Each high symbol `b∈H_j` receives surplus at least 2 from its `(a,b)` line; the total at party `j` is 4, so both symbols of `H_j` have surplus exactly 2 and all other `j` symbols have surplus 0. In the `il|jk` cut the two full `(a,x_l)` lines have common opposite support `H_j×H_k`; by the cut lemma each of those four high-high pair values has total multiplicity 3. Thus each of the twelve high-high values in the three pairs `jk,jl,kl` has exactly **one** E extension outside the `a` slice.

There is no outside-`a` E word high in all three other coordinates. Indeed `h_i(a)=4` leaves `h_i(p)=0` for every `p≠a`. For any such actual symbol `p` and any of its E neighbors, its corresponding pair line has exactly two entries. This does **not** say the whole `p` slice has four entries: `p` may have degree 3 and its slice then has six. If an outside word `(p,x_j,x_k,x_l)` were high in all three coordinates, compare its `pj` line with the full `aj` line. Their overlap contains the word's complementary pair; because singleton overlap is impossible and the `pj` line has exactly two entries, its other word is high in the other two coordinates as well. The analogous `pk` and `pl` lines give three mates. Each mate differs from the original in both of the two coordinates not held fixed, since otherwise their shared high-high pair would have two outside extensions. Hence the mates are distinct and the four high triples form one binary parity class.

Any two of these four triples agree in exactly one coordinate. For each such pair `x,y`, actual row orthogonality of the corresponding `a` and `p` lines has exactly the two terms

```
z_x+z_y=0,  where z_x=U_(a,x) conjugate(U_(p,x)) ≠ 0.   (6)
```

Three vertices form a triangle in this agreement graph, and (6) on its three edges is impossible. This uses only the two entries on each relevant `p` line, not a four-entry assumption for the whole slice.

The twelve outside-`a` extensions of the high-high pair values are therefore twelve distinct words, each high in exactly two coordinates. Each high symbol occurs four times in the cube and in four of these distinct outside words. Its surplus is 2, so `2d+2≥8`; by §2 its degree is exactly 3, and all eight of its occurrences are already accounted for. Thus `H_j=T_j` for `j,k,l`, and the remaining `24−8−12=4` E words use only `D_j×D_k×D_l` in these three coordinates. Label the two degree-two symbols at each party by whether they belong to `w^0` or `w^1`. Two equal bits would give one of the P pair values from that same all-inside word, which E cannot use. Three binary bits cannot be pairwise different. This contradiction excludes the degree-two case too. Hence

```
h_i(a) ≤ 3 for every actual symbol.                  (7)
```

## 5. Exhaustive initial surplus classes and B's cross-party consequence

Each party has two degree-two and two degree-three symbols. By (4), (7), nonnegativity and `Σh=4`, the only degree-labelled surplus types are:

* **A:** exactly two symbols have `h=2` and the other two have `h=0`, with arbitrary degree positions;
* **B:** both degree-two symbols have `h=0`, and the degree-three symbols have `h=3,1`;
* **C:** one degree-two symbol has `h=2`, the other has `h=0`, and both degree-three symbols have `h=1`.

For B at party `i`, write `c,t∈T_i` for its surplus-3 and surplus-1 symbols. Every `ij` side must be of the four-3-line kind: the alternative has only even contributions to each symbol's surplus. The 3 surplus edges at `c` meet three distinct positive-surplus symbols at `j`; only type C has three such symbols. Denote its degree-two surplus-2 symbol by `b_j`. The four 3-lines on `ij` form simple edges; `c` meets all three positive symbols, so the fourth edge, from `t`, must meet `b_j`. In particular every `(t,b_j)` line has three E words. Every other party is C, and there can be at most one B.

If the three `b_j` had the same bit relative to the actual `w^0,w^1`, every pair of them would be a P pair value and no E word could contain two. The three `(t,b_j)` E lines would then be disjoint and have 9 words in total, but the entire `t` slice has `2·3+1=7`. Therefore the three bits contain both values, necessarily in a 2-versus-1 distribution. These are genuine shared-P and shared-E necessary restrictions under the hypothetical B premise; they do not establish that B exists.

## 6. A six-vertex binary slice has two missing vertices at distance two

This step uses the actual complex coefficients, not a phase ansatz. Let `a` be any E symbol with `d_i(a)=2,h_i(a)=2`. Its six words are six distinct vertices of a binary 3-cube on the two actual E-neighbors in each of the other three parties. Each of the six nonempty `(a,bit)` pair lines, in each direction, has squared norm 1: it is a row of an actual unitary flattening and contains no P entry. Distinct such lines in the same direction are orthogonal.

If the two absent cube vertices have Hamming distance 1, relabel the three local bits so the missing vertices are `000,001`. The `(a, first bit=1)` line contains `100,101,110,111`; the `(a, second bit=0)` line contains only `100,101`. Both lines have squared norm 1, but the first has the latter's two nonzero terms plus the two nonzero terms at `110,111`, contradiction.

If the absent vertices have Hamming distance 3, relabel bits so they are `000,111` and write the six **actual nonzero** coefficients

```
A=U_(a,001), B=U_(a,010), C=U_(a,011),
D=U_(a,100), E=U_(a,101), F=U_(a,110).
```

The row overlaps in the three actual pair systems each have exactly two terms. Their orthogonality gives

```
A conjugate(E) + B conjugate(F) = 0,
A conjugate(C) + D conjugate(F) = 0,
B conjugate(C) + D conjugate(E) = 0.                   (8)
```

Multiplying the first and third equations after moving one term on each side and cancelling the nonzero factor `B conjugate(E)` gives `A conjugate(C)=D conjugate(F)`, contradicting the second equation. Thus distance 3 is impossible. Distance 0 is impossible because there are two distinct absent vertices. The only remaining distance is 2.

Consequently exactly one other coordinate is equal in the two missing vertices. In that direction the two actual pair-line multiplicities of `a` are `2,4`; in each of the other two they are `3,3`. This is a **necessary** slice property, not a claim that every distance-two slice extends to a tensor.

## 7. Excluding C and B, without a global phase claim

Suppose a party `i` is type C and let `a∈D_i` be its surplus-two symbol. A degree-three symbol at that party has odd surplus 1. Therefore none of the three `ij` pair sides can be of the two-4-line kind, since in such a side every symbol's surplus is a sum of 0's and 2's. All three sides must have four 3-lines and six 2-lines. Since the slice of `a` has six words and two neighbors in each direction, its pair lines are `3,3` in **every** direction. This contradicts the exactly-one `2,4` direction proved in §6. Hence type C cannot occur.

By §5, a B party forces each of the other three parties to be C. Thus B is impossible as well, and every party has type A. The contradiction in §6 is a specific, explicitly displayed set of three actual two-term orthogonality equations. It is not an assertion that a separate local phase check solves the remaining global phase system, nor a global exclusion of `r=2`.

## 8. A further global necessary restriction among the surviving A types

For any pair `ij` whose line side is of type `2244`, each 4-line contributes surplus 2 at each endpoint. Since every party is now type A, the two 4-lines use both positive-surplus symbols at each end, each exactly once; their high-value edges form a perfect matching. On a `3333` pair side, each positive-surplus symbol meets exactly two 3-lines, so the four high-value edges form the complete bipartite graph on the two positive-surplus symbols at each end. These are only line-multiplicity necessities on the same E support.

Form the graph `G` on the four parties with edge `ij` when the `ij` side has two 4-lines. If a party `i` has a degree-two positive-surplus symbol, the six-slice lemma gives exactly one direction where that symbol has a 4-line. Every edge incident to `i` must contain a 4-line at that symbol, because its two positive-surplus symbols each have surplus exactly 2 and the two 4-lines cannot both be assigned to one symbol. Thus `deg_G(i)=1`.

If `ij` is an edge and `kl` is its complementary pair, the opposite side of the same unitary cut has four 3-lines by §3; hence `kl` is not an edge. Thus `G` has no disjoint edges. If all four parties had a degree-two positive-surplus symbol, every vertex would have graph degree one, producing two disjoint edges. At least one party instead has no positive-surplus degree-two symbol. Since it is type A, its two degree-three symbols both have surplus 2. If exactly three parties have a positive-surplus degree-two symbol, they cannot be adjacent to one another: such an edge would force the third's degree-one edge to be disjoint. All three therefore connect to the fourth party, and `G` is precisely that star.

The surviving per-party A placements are degree-two/degree-two, degree-two/degree-three, and degree-three/degree-three, subject to the global restriction just proved. Nothing here establishes simultaneous feasibility of any placement, a common E support, positive amplitudes or phases.

## 9. Input, process and result boundaries

Before mathematical body reading or task-specific reasoning I read in full the F877 manifest, freeze receipt, final pre-dispatch binding, parent live metadata and actual-dispatch receipt, and the 22 controls listed in the manifest, as status/permissions only. They comprise the author-scope restoration, owner addendum 2, L1/privacy/Gram/AME/PH quarantine records, the F439/F444/F448/F508/F513/F586/F602/F596/F653/F654/F659/F660/F662 status-only quarantine controls, and the occupancy-omission and prerun-design-correction controls. I then created `prebody-ack-v1.md` and sent the direct prebody ACK to Main, both before the body. Initial non-raw administrative displays omitted blocks; complete raw displays recovered the manifest, receipt, binding, metadata and dispatch receipt before the ACK. The metadata path was initially mistyped as `/Users/jinic/...` and returned not found; the designated `/Users/jinleic/...` path was then read in full. The initial wave listing showed neither output file. The write interface did not expose an atomic exclusive-create flag, so no stronger atomicity claim is made.

Only after both acknowledgements I read the one complete literal part in serial raw windows `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–248`, including the ending. Displays were below 30,000 bytes; no packet clipping was observed, so no packet clipping recovery was required. The packet renders S1 LF 1–3 (the notation erratum), S2 LF 1–172, S3 LF 1–22 and S4 LF 1–33 completely. The parent-supplied part pin is SHA-256 `09b46473ab0743a1cba2578e16716adc88e70441d976ac9682bd3a1f1aba413a`; source paths and pins are those in `manifest-v1.json` and the packet headings. These are parent-supplied administrative bindings, not independently recomputed hashes, correctness certificates or source-identity certification. The read is nonblind: the assignment and S2 supplied the intended cases and earlier claims. S1 corrects S2's notation collision, not its mathematics.

The basic incidence, cut classification, cube, complex-line and surplus arguments used here are written out above; no missing source body is silently imported as a theorem. S2 is an earlier author candidate, while S3/S4 are scoped parent dispositions; their linked underlying sources were not opened and their broader claims are not needed by this proof. Status controls are not mathematical inputs. No held episode or held proof/method/selection/planning/verification/reporting/confidence/downstream consumer, sibling science, unlisted linked body, network, external model, code execution, test, scientific evaluation, solver, child subprocess, compilation, Git or deletion was used. No verifier was prepared, so there is no code hash or computational verification.

This is an author candidate for separate parent disposition. It claims no independent-family, human, formal or kernel acceptance, publication priority, witness, exact feasible support classification, global t26/N50 theorem or global phase impossibility. The all-A common-support/common-amplitude/common-phase question remains open within this argument. Any later correction must be additive, not an edit of this candidate.
