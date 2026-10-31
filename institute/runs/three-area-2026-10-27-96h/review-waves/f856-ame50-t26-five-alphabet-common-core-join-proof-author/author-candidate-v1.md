# Actual AME(4,6), N=50, t=26: entire five-symbol party obstruction

**Prospective author candidate; nonblind, same harness; no parent disposition or independent acceptance.** I reconstruct the parent common-core argument and its q=5 surplus input below, including the previously nontrivial surplus-four branch. The candidate is a written proof for arbitrary complex amplitudes and phases, not a computation. It concerns only the following exact implication.

Let one complex tensor `U` on four fixed six-symbol parties have all three 36-by-36 balanced flattenings unitary, exactly 50 nonzero entries, and exactly 26 entries of modulus one. Equivalently `U=6ψ` for one normalized AME(4,6) state expressed in the fixed product basis. For each party let `q_i` be the number of its symbols used by the remaining 24 nonzeros. **Claim:** `q_i≠5` for every party. All six pair systems, all components, and all phases below belong to that one tensor. This is not an exclusion of the whole t=26 branch, N=50, any other t, or a global minimum; no witness, priority, novelty, human/family/kernel verification, or adoption is claimed.

## 1. Actual-unitary bookkeeping and the needed cut lemma

Let `P` be the 26 modulus-one words and `E` the 24 other nonzero words. Every entry of a unitary has modulus at most one. A P entry exhausts its actual row and column, so in each of the six pair systems the 26 P projections are distinct, no E word shares one, and the other ten pair values are all E-used. Each such E value has at least two extensions: a residual row with just one nonzero would have an entry of modulus one. Thus deleting the P rows and columns in any cut leaves an actual 10-by-10 unitary with 24 entries and no degree-one line.

For an E-used symbol `z` at party i, let `d_ij(z)` be the number of E partners at party j and `s_i(z)` its E-word count. The number of P words containing z is `6−d_ij(z)`, independently of j, since the same P set supplies every other pair value; write the common degree as `d_i(z)`. Define `h_i(z)=s_i(z)−2d_i(z)`. Summing over the ten E pair values gives, for each party,

```text
    d_i(z) ≥ 2,       Σ_z d_i(z) = 10,
    h_i(z) ≥ 0,       Σ_z h_i(z) = 24−20 = 4.                 (1)
```

Indeed `h_i(z)` is the sum of `(multiplicity−2)` over its E pair values with any fixed partner party. If `d_i(z)=1`, independence of the degree from the partner fixes all three other coordinates of every word at z, leaving at most one E word although its pair line has at least two. Thus `q_i≤5`. Also `q_i≥2`: a sole E symbol would have degree ten, exceeding six physical symbols.

If `d_i(z)=2` and `h_i(z)=1`, the five E words at z lie in its binary three-cube. Along each axis the two actual row degrees are 2 and 3 and their supports must overlap at least twice, since a singleton overlap cannot be orthogonal. Therefore the five vertices induce at least six cube edges. Three deleted vertices induce at most two edges in the triangle-free cube, so delete at least `3·3−2=7` of its 12 edges, leaving at most five. Contradiction. Hence

```text
              d_i(z)=2  implies  h_i(z)≠1.                    (2)
```

We use the following cut classification and reconstruct it here rather than importing an unexamined source: the residual is either (I) two 3-by-3-minus-one components and two full 2-by-2 components, or (II) one connected 4-by-4 component with 12 entries and three full 2-by-2 components. In a 12-entry component, each side has degree pattern `3333` or `2244`; if one side is `2244` its opposite is `3333`. In particular, in any physical pair system either four E values have multiplicity three and all other E values have multiplicity two, or two have multiplicity four and all others multiplicity two. The two four-rows, when present, are in the unique 4-by-4 component and have the same four neighbors.

Proof. A support component of an actual unitary is square, since its rows are orthonormal within its columns and its columns are orthonormal within its rows. Distinct rows or columns cannot meet in exactly one nonzero. In a component of order greater than two, if a degree-two row uses columns c,c', every other row uses both or neither: orthogonality makes c,c' twins. Their common degree is at least three, for degree two would isolate an actual 2-by-2 unitary. Distinct degree-two rows have disjoint twin pairs: if they shared one column they would share both, and their two orthonormal row vectors would exhaust those two columns and isolate a 2-by-2 block. The transposed statements also hold.

For a component of order m and excess `e=#entries−2m`, let k be its degree-two rows. The other `m−k` rows contribute at least one to the excess, while the k disjoint twin column pairs contribute at least `2k`. Thus `m−e≤k≤floor(e/2)`. A zero-excess component is a full 2-by-2 block; excess one is impossible. Excess two has order at most three and is 3-by-3 minus one. Excess three has order at most four. At order four there is one low row and three degree-three rows; its twins both have degree three, so one high row avoids them and cannot place three entries in the two remaining columns. Hence excess three is a full 3-by-3 block.

For excess four, order is at most six. At order five, k is one or two. If k=1, the four high rows have degree three. The twin columns cannot meet all four high rows because then the other three columns would contain only four entries, less than their required six. A high row avoiding the twins uses all three other columns and meets any high row using the twins in exactly one column, impossible. If k=2, both twin pairs have degree three and the fifth column degree two. Each pair's high-neighbor set is a two-subset of the three high rows; distinct such subsets would intersect once, so the two sets coincide and the remaining high row has degree at most one. At order six there are exactly two low rows and two low columns and every other line has degree three. Low rows cannot meet low columns. The two low columns have disjoint two-element high-row neighborhoods A,B which partition the four high rows. Each low-row twin pair has two high neighbors and, to avoid a one-overlap with the low columns, must choose A or B. Equal choices leave the other two high rows with degree one; different choices disconnect the component. Thus an excess-four component has order four (order three cannot hold ten entries).

The residual excess is four. Its positive-component excesses are therefore either `2+2` or `4`; components of excess one do not exist, and the remaining order is filled by full 2-by-2 components. This gives I or II. At order four with 12 entries, the only possible row degree partitions are `3333`, `2334`, `2244`. In `2334`, the degree-two row has twins of equal degree three or four. If degree three, the full row meets both and one degree-three row avoids both, impossible. If degree four, the other two columns have degree two; each degree-three row must use a different one, so those two columns overlap only in the full row, impossible. In `2244`, the two low rows' twin pairs are disjoint; each column meets the two full rows and exactly one low row, giving opposite pattern `3333`. The stated per-pair alternatives and full-row equality follow. In I, the two degree-three rows in each 3-by-3-minus-one component have the identical full three-column neighborhood.

## 2. The actual closed-box obstruction

Suppose two actual symbols are chosen at each of the four parties and, in every cut, the four rows on one side of the corresponding binary box have **all** their actual support in the four opposite box pair values. Their restrictions are 4-by-4 unitaries: the original four rows are orthonormal and a square row-isometry is unitary. The same restricted tensor divided by 2 is normalized and has every two-party marginal `I_4/4`.

No such pure four-qubit state exists. Write `ρ` for it and `A_r=Σ_{wt(R)=r}(tr ρR)^2` over Pauli strings. Two-party maximal mixing gives `A_1=A_2=0`, `A_0=1`. Every three-party marginal has purity 1/2, by complementary spectra and the remaining one-party marginal `I_2/2`; its weight-three Pauli square sum is therefore three. Summing over the four triples yields `A_3=12`. Global purity gives `A_4=16−1−12=3`. But the spin flip `ρ̃=Y^{⊗4} conjugate(ρ) Y^{⊗4}` is positive and flips a weight-r Pauli coefficient by `(-1)^r`, hence

```text
    tr(ρρ̃) = (1−12+3)/16 = −1/2 < 0,
```

contradicting positivity. This proof assumes neither real coefficients nor any phase relation between different actual words.

## 3. Entire q=5 surplus distribution, including h=4

Suppose `q_D=5`. Equation (1) forces all five degrees to be two. By (2), the nonnegative surplus partition of four is only `(4,0,0,0,0)` or `(2,2,0,0,0)`. We exclude the first, without assuming a separately selected cut mask or the full F826 profile theorem.

### 3a. Consequences of an h=4 cube

Assume a D symbol x has `h_D(x)=4`. Its E slice is the full cube `{x}×H_A×H_B×H_C`, with each `H_j` of size two. At each other party, each symbol in `H_j` has an E pair with x of multiplicity four, hence surplus at least two. Equation (1) forces both high symbols to have surplus exactly two and all other symbols there surplus zero.

In the `Dj | kl` cut, the two degree-four rows at x are the full rows of its unique 12-entry component. Its four opposite columns are exactly `H_k×H_l`, and all four have degree three. Thus every high-high pair at A,B, at A,C, and at B,C has exactly the two x-cube extensions and **one** additional E extension.

**No-three-high lemma.** No E word outside the x slice is high at all three of A,B,C. Suppose one has D coordinate `p≠x`. Since `d_D(p)=2,h_D(p)=0`, its slice has four words and each of its pair lines has exactly two. Compare the actual rows `(x,j)` and `(p,j)` for each j at the alleged high triple. The x row is full on the high complementary square, so singleton-overlap prohibition forces the other p word on that line also to be high in the two remaining coordinates. These three mates are distinct: otherwise two outside-x words would share a high-high pair whose unique extra extension was already used. They exhaust the p slice. Its four high triples have injective projections on every two coordinates, hence form a binary parity class; any two agree in exactly one coordinate. Put `z_t=U_{x,t} conjugate(U_{p,t})≠0`. Comparing the two actual rows at that common coordinate gives `z_t+z_{t'}=0` for every pair of triples. Three such equations on a triangle force `z_t=0`, contradiction. In particular, each high-high pair's unique outside-x extension has a low third coordinate.

### 3b. At most one five-symbol party, including both high-high patterns

First, a second five-symbol party is impossible if D has the h=4 cube. Its two high symbols have degree two, surplus two, and six E occurrences each. Four occurrences are already in the cube, whose two high alphabets at the other parties exhaust that symbol's degree-two neighbor sets. Its two remaining occurrences would be outside x and high in all three of A,B,C, contrary to the lemma. The same reasoning applies with the parties interchanged.

It remains to rule out two q=5 parties each having surplus `(2,2,0,0,0)`. Call their high symbols `a_0,a_1` and `b_0,b_1`. On each actual high-high pair put weight `multiplicity−2`, with weight zero for an absent or degree-two pair. Positive weights can touch only high symbols. Their two row and column sums are two and each weight is at most two. Up to relabeling the only matrices are all ones or diagonal twos.

* **Four threes.** Each high symbol has only two neighbors at each remaining party. A high-high pair has three distinct complementary extensions, so the product of the two intersections of the participating symbols' two-element neighbor sets has at least three cells. Both intersections must have size two. Across the four high-high pairs, all high symbols consequently share the same two actual alphabets K,L at the other parties. Both B neighbors of each high A symbol are the two high B symbols, so all twelve high-A words lie in the one binary box `{a_0,a_1}×{b_0,b_1}×K×L`.
* **Two fours.** The two high-high degree-four rows are full rows of the same actual 12-entry component and share its four complementary columns. Each set of four extensions is a product of intersections of two-element neighbor sets, hence a full 2-by-2 product; all four high symbols share the actual alphabets K,L. Each high A symbol has two further E words, all with complementary values in `K×L`; the four such words meet the same component and exhaust its four entries outside the two full rows. The same is true of the four further high-B words. They are therefore the **same** four words, and all twelve high-A words lie in the same binary box.

In either case, for every cut the four rows formed by a high A symbol and one of its two partner symbols occur and are supported only on the four opposite box values. The isolation of E pair values from P ensures no hidden P entry on those rows. Section 2 is a contradiction. Therefore at most one party has q=5.

### 3c. The remaining alphabets in the h=4 branch

No party has q=2. Indeed its two degrees sum to ten and each is at most five, because every partner has q≤5; both degrees are five, so all other parties have q=5. Each of the two used symbols then occurs in exactly one P word. Each such word must use the unique outside-E symbol at each other party, so the two P words repeat a physical pair value, contrary to P injectivity. Two q=3 parties are impossible because their 3-by-3 rectangle cannot contain ten distinct E pair values. Together with §3b, an h=4 q=5 party D leaves, up to permutation of A,B,C, only other-alphabet cases `444` or `344`.

**Case 444.** Each high symbol has the two cube neighbors at each other party and, by the unique outside-x extension of a high-high pair, at least one low neighbor. Both high symbols have degree at least three; the two low symbols have degree at least two and the degree sum is ten. Therefore both high degrees are three and both low degrees two. For high `a∈H_A`, let `f(a)` be its unique low C neighbor; for high `b∈H_B`, let `g(b)` be its unique low C neighbor. The outside extension of every high AB pair shows `f(a)=g(b)` for all four choices, yielding a common low C neighbor `ℓ_C`; cyclically there is a common low A neighbor `ℓ_A` of both high C symbols. The other low C symbol meets no high A symbol, and it cannot meet `ℓ_A`, whose two high-C neighbors exhaust its degree. Only one other low A symbol remains, contradicting degree two.

**Case 344.** Let `Q_A=H_A∪{a_*}` and B,C have two high and two low symbols each. The four high BC pairs have outside-x extensions at `a_*`. Each high B or C symbol therefore has degree at least three and, as in the 444 case, exactly three; each low B or C degree is two. Let `f:H_C→(low B)` give the unique low-B neighbor of high c, and `g:H_B→(low C)` the unique low-C neighbor of high b.

Both f and g cannot be constant. If f is constant at β, the other low B symbol has no high-C neighbor and must meet both low C symbols. If g is constant at γ, γ already meets both high B symbols and has degree two, so it cannot meet that other low B symbol. Thus at least one of f,g is bijective. Each high A symbol then has both high and both low neighbors in the corresponding B or C party, so its degree is four. Equation (1) gives `d_A(a_*)=2`, and its surplus is zero; its entire four-word slice is exactly the four outside-x extensions of the high BC pairs.

Those four cells are partitioned into two degree-two `(D,a_*)` rows, at distinct D symbols `p≠x`. Each such p has a four-word zero-surplus slice: two words at `a_*` and two at one high A symbol. If a row's two high-BC cells are diagonal, its B and C neighbor alphabets are already the two high alphabets, forcing its remaining two words to be three-high, forbidden. If its two cells share B and differ in C, each high C value must appear once again in the p slice, and the two remaining words have high A and high C; no-three-high forces their B values to be `f(c)`. Since p has only one further B neighbor, f is constant. A same-C pair analogously forces g constant. Consequently both f and g bijective is impossible.

It remains to exclude exactly one constant. By symmetry take `f(c)=β` constant and g bijective. Every row in the `a_*` partition must pair the two cells at one fixed high B symbol b; call its D symbol `p_b`. The other two `p_b` words have B=β, both high C values, and one high A value `a_b`. The `a_b` are distinct: otherwise a high AC pair would have two outside-x extensions. They therefore exhaust `H_A`.

For each high b, its two high-AB pairs have outside-x extensions at C=`g(b)`. Their D values are neither x nor `p_b`; since b has exactly three D neighbors, both use its unique third neighbor `r_b`. Because `r_b≠x`, its D surplus is zero, so the actual `(r_b,g(b))` line has exactly the two words with that fixed b and both high A values. In the actual DB cut, the row `(p_b,β)` has exactly the two columns at fixed `a_b` and both high C values. Orthogonality of that row to **both** full x/B rows, and of `(r_b,g(b))` to **both** full x/C rows, yields the following determinant identities for the nonzero cube coefficients `Q_{abc}=U_{x,a,b,c}`:

```text
    Q_{a,1,0}/Q_{a,0,0} = Q_{a,1,1}/Q_{a,0,1}   for each a,
    Q_{0,b,1}/Q_{0,b,0} = Q_{1,b,1}/Q_{1,b,0}   for each b.  (3)
```

All divisions are legitimate. Write `Q_{a,1,c}=r_a Q_{a,0,c}` and `Q_{a,b,1}=s_b Q_{a,b,0}`. Computing `Q_{a,1,1}` in the two orders gives `s_0=s_1`; thus the two nonzero full actual rows `(x,C=0)` and `(x,C=1)` of the DC cut are proportional on their entire supports, contradicting their orthogonality. The case g constant and f bijective is the transposed argument. This exhausts 344 and 444, and therefore excludes h=4.

Consequently, for **every** q=5 party D, all five degrees are two and precisely two symbols `x,x'` have surplus two; the other three have surplus zero. Each high slice has six E words. This reconstructs the load-bearing F826/F841 assertion rather than assuming only selected alphabet cases.

## 4. Six-slice geometry and synchronized unique agreement

For either high D symbol, its six words occupy a binary three-cube minus two distinct vertices. Actual norms and row orthogonality apply separately to its two rows on each of the three other axes.

If the deleted vertices have distance one, sum squared moduli over that differing coordinate. On the other two coordinates the resulting 2-by-2 nonnegative table has every row and every column sum one. Opposite entries agree, so the missing two-point fiber forces the opposite fiber empty too, contrary to exactly two missing words.

If their distance is three, relabel the missing vertices 000 and 111 and let the six retained coefficients at `001,010,011,100,101,110` be `a,b,c,d,e,f`. The three actual row orthogonalities give

```text
    a conjugate(e)=−b conjugate(f),
    a conjugate(c)=−d conjugate(f),
    b conjugate(c)=−d conjugate(e).                            (4)
```

Multiplying the first and third and dividing by the second gives `b conjugate(e)=−b conjugate(e)`, impossible since all six entries are nonzero. Thus the distance is **exactly two**. The remaining distance-zero case is impossible because the missing vertices are distinct. This is a genuine three-cut, arbitrary-complex argument; no t=28 global conclusion is used.

For an axis on which the two deleted vertices agree, the two rows at that high D symbol have multiplicities `(4,2)`; on an axis where they differ they have `(3,3)`. The two high symbols contribute distinct rows in each pair system. Section 1 permits either the global multiplicity-four alternative or the multiplicity-three alternative, never both. Therefore the agreement axes for x and x' coincide. Since each missing pair has distance two, there is exactly one common agreement axis; call it A, with the other parties B,C. This also covers the absence of any second agreement axis and the previously possible distance-three boundary.

## 5. Join the actual high slices, not independent cut masks

For `u∈{x,x'}`, write its actual two-element neighbor alphabets as `A_u,B_u,C_u`. Since its missing pair agrees in A and differs in B,C, the rows `(u,A_u)` have degrees four and two. Write `F_u` and `S_u` for their A values. The degree-four row has exactly the product `B_u×C_u` as its E neighborhood; the degree-two row uses the complementary diagonal to the deleted pair in that product.

**DA cut.** Both high symbols supply a distinct degree-four row, and §1 puts both full rows in the same unique order-four component. Its four columns are therefore simultaneously `B_x×C_x` and `B_{x'}×C_{x'}`. Equality of nonempty Cartesian products implies

```text
                 B_x=B_{x'}=:B_0,    C_x=C_{x'}=:C_0.          (5)
```

Each degree-two `(u,S_u)` row overlaps its own full row and hence belongs to that same component. The four `(u,A_u)` rows are distinct and exhaust its four rows. The two low rows have disjoint twin pairs, so their two retained diagonals in `B_0×C_0` are complementary. No degree-two row is presumed external merely because of its degree.

**DB cut.** At a fixed u, the two `(u,B_u)` rows have degree three, intersect in exactly two actual AC columns, and have different neighborhoods: each misses the one vertex at A=`S_u` with that B coordinate. They belong to the same connected component because they intersect. They cannot be in a 2-by-2 component, nor can they be the degree-three rows of a 3-by-3-minus-one component, where such rows have identical neighborhoods. Thus they lie in the unique order-four component. Their union has all four columns of `A_u×C_u`, so this is the component's entire column set. The same reasoning for x' puts its two distinct rows in that **same** unique component and gives

```text
              A_x×C_x = A_{x'}×C_{x'},  hence A_x=A_{x'}=:A_0.  (6)
```

This product equality uses actual nonempty factor sets, not merely equal cardinalities. Its two x rows and two x' rows are four distinct rows and exhaust the component. The analogous DC argument uses the two degree-three C rows, whose neighborhoods overlap in two and differ; it puts all four `D_0×C_0` rows in that cut's unique order-four component and exhausts its four `A_0×B_0` columns. Here `D_0={x,x'}`. No assumption is made about whether the high A roles `F_x,F_{x'}` coincide; both the equal-role and crossed-role possibilities are covered by (5)–(6).

## 6. Same 12-word tensor, complete closure in all cuts, and contradiction

All twelve high-D E words are precisely the two six-word slices, hence lie in `D_0×A_0×B_0×C_0`. In the DA cut its four selected rows are the four component rows and its four selected columns are all of `B_0×C_0`; in DB they are the four component rows and all of `A_0×C_0`; in DC they are the four component rows and all of `A_0×B_0`. Every selected row is an E-used pair value. Therefore no P entry can share it, and no off-core E entry can occur on it: each is already a row of the actual connected component with its complete four-column set. The same conclusion also exhausts the corresponding columns by unitarity. Thus off-core P/E words, other symbols, and possible additional components cannot change any of the three 4-by-4 restrictions.

The restrictions are three reshapes of the **same** 16-entry subtensor, with exactly twelve nonzero E entries, and each is a unitary. Dividing that single subtensor by 2 gives the forbidden normalized four-qubit state of §2. This contradiction excludes every q=5 party under the stated exact N=50/t=26 hypotheses. Neither equality of high-slice amplitudes nor a special phase pattern is assumed. Individual local six-slices are not claimed to be AME states.

## 7. Parent-line audit, dependencies, and limits

* S1 lines 3, 6: the claim is the exact q=5 implication above. Sections 3–4 independently reconstruct both surplus branches, the genuine-unitary six-slice lemma, and synchronization. F826's weaker distance-two-or-three result is strengthened by the separate local calculation in (4); no t=28 total-count assertion is used.
* S1 line 8: §1 derives both residual component forms, the order-four degree alternatives, and identity of degree-three neighborhoods in the 3-by-3-minus-one component. The genuinely unitary twin-pair fact is essential; no graph-only replacement is made.
* S1 lines 11 and 13: equations (5) and (6) prove the product equalities, the unique 4-core membership, actual alphabet equality, and all rows' presence. The missing `A_x=A_{x'}` conclusion does not follow from DA alone; DB supplies it.
* S1 line 15: §6 explicitly discharges four-row and four-column exhaustion in **all three** actual cuts, including the DA degree-two rows, and rules out hidden P or E leakage. The resulting tensor is one common object, not independently constructed unitaries.
* S1 line 17: §2 derives normalization and the unrestricted-complex spin-flip contradiction. S1 line 20's qualification remains: this artifact is an author candidate, not a parent disposition or independent gate. The argument needs no global t bound, no-OLS theorem, or external enumeration.

The S1 parent note and F841/F826/F827 are nonblind candidate inputs, not accepted merely by inclusion. The written arguments above reconstruct every load-bearing statement used here, including the low-excess classification, so **no absent linked mathematical body is imported as an unconditional premise**. If independent scrutiny disputes §1's reconstruction, the exact conditional fallback is the per-cut actual-unitary component/twin/degree interface stated at the start of §1; if it disputes §3, the distinct fallback is the full q=5 surplus `(2,2,0,0,0)` assertion, not merely selected 3445 or 4445 instances. The references to older packets, no-OLS, global bounds, source code and execution receipts inside the literal sources are not authorization to open or use those absent bodies. Dispositions S5 and S6 are background only; no old finite run is treated as evidence for this proof. No implication about q=3/4 profiles or the entire t=26/N=50 branch is claimed here.

## 8. Complete source and process declaration

Before any packet body or mathematical reasoning I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and all 23 manifest-listed status-only controls. Initial non-raw administrative JSON displays had elisions; the affected manifest, freeze receipt, final binding, and metadata supply were reread completely as raw before acknowledgement. I then created the previously absent `prebody-ack-v1.md` and delivered a direct prebody acknowledgement to Main, both before reading any packet body. My prior task exposure was the assignment's own description and those administrative/process inputs. Controls were used only for status and permissions, not as mathematical premises.

Thereafter I read both literal parts completely, in order and through their endings, in raw windows of at most 20 LF: part 1 `1–20, 21–40, …, 561–580, 581–586`; part 2 `1–20, 21–29`. Each individual display was below 30,000 bytes. No packet clipping was observed and no packet clipping recovery was needed. The parent-supplied part pins are part 1, 98,523 bytes, 586 LF, SHA-256 `0cd2d962f8a1ff0675fc9861b8b19a3c3dbec1a985ce99ec111ea3e07c6c18b1`, and part 2, 5,810 bytes, 29 LF, SHA-256 `74923c936df979c758bc0c39148a22a4b5a6f775c0892eb7cb1b42a1a88500d4`. Complete rendered bodies and parent-supplied original pins were:

| ID | Original source, complete LF | Parent-supplied SHA-256 |
|---|---|---|
| S1 | parent q5 common-core candidate, 1–20 | `eedcb1df68e7682342150b044013729404d8ae1414257f73cc66acfa94352882` |
| S2 | f841 t26 three-alphabet author candidate, 1–203 | `3788449b5decefd62ee107a01410e1572e3c089a9ff8a40ac659e2b51205c912` |
| S3 | f826 t26 entire-same-tensor author candidate, 1–163 | `b826085181355b587d96df2825c7ef5fb1b9ffc13ff9531818f640d39a392fa8` |
| S4 | f827 t28 entire-same-tensor author candidate, 1–145 | `c78020e48e7ca16159cf74debcb25cc2b747be06b4c371230142298c1ea95814` |
| S5 | t25/t27 exclusion and excess-frontier parent disposition, 1–33 | `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336` |
| S6 | unitary-excess6 and t28-cut parent disposition, 1–23 | `f84c4b2eba89f99b693fa1c9fdfd5b4ef90eb5e6f7d9c5a99ca7373cc11fd0dc` |

The pins and roundtrip are supplied administrative metadata, not my own hash calculation or a source-identity/correctness certificate. No genuine held episode or any of its proof/method/planning/selection/verification/reporting/confidence/downstream consumers was opened or used. No packet link, unlisted source, sibling scientific output, network, external model, scientific eval, code execution, child subprocess, solver, test, compilation, build, lint, formatter, Git or deletion was used. No executable was prepared; there is no code hash or computational verification. Mathematical corrections, if any, require a new additive artifact, not an edit to this frozen candidate.
