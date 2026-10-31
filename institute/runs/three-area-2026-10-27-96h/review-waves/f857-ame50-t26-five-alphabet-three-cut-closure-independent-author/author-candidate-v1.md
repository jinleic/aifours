# Actual AME(4,6), N=50, t=26: the entire five-alphabet party is impossible

**Prospective GENERAL AUTHOR candidate; nonblind, same harness; separate parent disposition and independent scrutiny are required.** This is a written proof candidate, not a reviewed or formally verified theorem.

## 1. Exact statement and the new incompatibility

For every normalized complex pure tensor `ψ ∈ (C^6)^{⊗4}` in every fixed product orthonormal basis, suppose all three balanced flattenings of `U=6ψ` are unitary, exactly 50 entries of `U` are nonzero, and exactly 26 of those entries have modulus one. Let `E` be the other 24 nonzero entries and `Q_i` the actual set of symbols appearing in `E` at party `i`. The proposed conclusion is

```
                        |Q_i| ≠ 5  for every party i.                     (T)
```

All coefficients and phases are arbitrary complex numbers. Every word, alphabet, row, column and cut in the proof belongs to this **same** tensor and fixed basis. There is no assumption that an abstract support mask is unitary, no independent-cut witness, and no choice of different alphabets or coefficients in different cuts.

The decisive new observation is this. In the two high six-word slices of a putative five-symbol party, f841's same agreement coordinate gives two degree-three rows in either of the other two cuts. Those two rows are connected and together use **four** opposite physical pair values. Therefore the exact excess-four component classification forces them into the unique 4-by-4/12-entry component. The other high slice's two degree-three rows must lie in that very component, so their four opposite values are identical. Projecting that equality forces equality of the two high slices' physical partner alphabets, including the alphabet at the agreement coordinate. The latter equality is precisely what f841's actual closed-binary-box obstruction forbids. Below all three cuts are paid simultaneously, the relevant local statements are reconstructed rather than assumed, and the resulting complex contradiction is written out.

This excludes only the `q_i=5` stratum of this exact `N=50,t=26` branch. It does **not** exclude the remaining t26 strata, all N50 tensors, any other t, or establish a support minimum, construction, priority, novelty, family/human/kernel acceptance, or an independently realizable cut witness.

## 2. One physical P/E support and the low-excess cut interface

Let `P` be the 26 modulus-one words and `E` the remaining 24 words. A modulus-one entry exhausts its unitary row and column. In each of the six physical pair systems, the 26 `P` projections are distinct and disjoint from the `E` projections. Every other one of the 36 pair values is an `E` value; such a line has at least two `E` extensions, since an actual unitary line with only one nonzero has modulus one. Removing the `P` rows and columns in any cut leaves a 10-by-10 unitary support with 24 entries, no degree-one line, and total excess `24−2·10=4`.

For an `E`-used symbol `a` at party `i`, let `s_i(a)` count its `E` words and let `d_{ij}(a)` count its `E` partner symbols at another party `j`. Since exactly `6−d_{ij}(a)` `P` words have coordinate `a`, this degree is independent of `j`; call it `d_i(a)`. Put `h_i(a)=s_i(a)−2d_i(a)`. For each party,

```
       d_i(a) ≥ 2,       Σ_{a∈Q_i} d_i(a)=10,
       h_i(a) ≥ 0,       Σ_{a∈Q_i} h_i(a)=24−20=4.             (1)
```

Indeed, degree one at `a` fixes all three other coordinates and permits at most one distinct word, contrary to the at-least-two extensions of an `E` pair value. The inequalities for `h` follow by summing the line excesses. Thus `|Q_i|≤5`.

The following exact component interface will be used, including where a degree-two line lies; it is a consequence of actual unitarity, not merely graph feasibility.

**Component lemma.** Each residual cut is exactly one of

* two `3×3`-minus-one components plus two full `2×2` components; or
* one connected `4×4` component with 12 entries plus three full `2×2` components.

A degree-two row in a connected component of order greater than two has a pair of twin columns with the same row neighborhood and degree at least three; distinct such rows have disjoint pairs. The transpose holds. On either side of the `4×4` component, the degree pattern is `3333` or `2244`; `2244` on one side forces `3333` on the other. Consequently a physical pair system contains either four degree-three values and no degree-four values, or two degree-four values and no degree-three values; all remaining values have degree two.

*Written derivation.* A support component of a square unitary is square, by comparing the numbers of orthonormal rows and columns. Two rows or columns cannot meet in exactly one nonzero. For a degree-two row, every row meeting one of its two columns meets both, so the columns are twins. If two degree-two rows had the same pair, their orthonormal vectors would span those two columns and force every other row to vanish there; the pair would be an isolated `2×2` component. Thus twin pairs in a larger component are disjoint.

If a connected component has order `m>2`, excess `e`, and `k` degree-two rows, then the other `m−k` rows contribute at least one each to the excess, while the disjoint twin pairs contribute at least `2k` to column excess. Hence

```
                  m−e ≤ k ≤ floor(e/2).                         (2)
```

Excess zero gives a full `2×2` component; excess one is impossible. Excess two has order three and is `3×3` minus one. For excess four, (2) gives `m≤6`. Order three cannot carry excess four. At order five there are one or two low rows. With one, the four other rows all have degree three; its twin columns have some high row avoiding both, which uses all three remaining columns and therefore meets a high row using the twins exactly once. With two, the two twin pairs use all column excess, so each twin column has degree three. Their two-high-row neighborhoods are two-subsets of three high rows; different subsets meet once, whereas equal subsets leave the third high row at most the one remaining column. Both cases contradict unitary support.

At order six, (2) and its transpose give exactly two degree-two lines on each side; all other lines have degree three. The two low columns have disjoint two-high-row neighborhoods `A,B`. A low row cannot meet a low column, since its twin columns are high. Each high twin column has two high-row neighbors and must meet either low column in zero or two rows, so those neighbors are `A` or `B`. If both twin pairs choose the same set, a row in the other set has at most one neighbor; if they choose different sets, the component disconnects. Thus a connected excess-four component has order four.

The only partitions of total excess four using positive component excesses are `4` and `2+2`, since excess one is impossible. Filling the remaining order with `2×2` blocks gives the two stated cut types. An order-four/12-entry side has degree partition `3333`, `2334`, or `2244`. For `2334`, the degree-two row has twin columns. If those columns have degree three, their neighbors are the low row, the degree-four row, and just one degree-three row; the other degree-three row has only two remaining columns. If the twins have degree four, the two remaining columns have degree two. The two degree-three rows must use different remaining columns, which then meet only in the degree-four row. Both are impossible. For `2244`, disjointness of the low-row pairs and fullness of the two high rows give degree three on every opposite column. This proves the interface.

When `d_i(a)=2` and `h_i(a)=1`, the five `a`-slice words are five vertices of a binary three-cube. For each axis, its two actual unitary rows have support sizes two and three in four complementary cells; they overlap and cannot overlap once, so the retained cube has at least two edges in each axis, at least six total. Deleting three cube vertices removes at least `9−2=7` of the twelve edges, because the cube is triangle-free and three vertices induce at most two edges. At most five remain. Thus

```
                   d_i(a)=2  implies  h_i(a)≠1.                 (3)
```

## 3. The entire q=5 party: eliminate the surplus-four alternative

Assume for contradiction that `|Q_D|=5`. Equation (1) makes all five D-degrees two. Each D-symbol slice is a subset of its actual binary three-cube, and by (3) its surplus is in `{0,2,3,4}`. The total surplus is four. Thus the only possibilities are one symbol of surplus four or two symbols of surplus two. We first exclude the former, including all alphabet boundary cases, rather than silently assuming the latter.

### 3.1 The full cube and its unique extra high-high incidences

Suppose `h_D(x)=4`. The `x` slice is the full cube

```
       {x} × H_A × H_B × H_C,          |H_A|=|H_B|=|H_C|=2.
```

Each other D-symbol has surplus zero and four E words. Every `j∈{A,B,C}` high symbol occurs four times with `x`; its `(D,j)` line has excess two. By (1), the two symbols in `H_j` each have surplus exactly two and all other j-symbols have surplus zero.

For each `j`, the two degree-four rows `(x,H_j)` in the actual `Dj | kl` cut are the two full rows of its 12-entry component. The opposite four pair values are exactly `H_k×H_l`, all of degree three. Hence every high-high pair in `AB`, `AC`, and `BC` has exactly two x-cube extensions and exactly one further E extension.

**No-three-high lemma.** No E word outside the x slice can be high at all three of A,B,C. If `t=(a,b,c)` at D-symbol `p≠x` were such a word, the p slice would have four words, two at each of its two partners in each coordinate. For each coordinate, compare the actual row `(p,t_j)` with the full cube row `(x,t_j)`. Their overlap cannot be one, so the second p-word in that row is also high in the other two coordinates. The three resulting mates are distinct: otherwise two outside-x words would share a high-high pair whose total multiplicity is already three, including the two cube words. Thus all four p-words are high-high-high, and each of their pair projections is bijective. They form a binary parity class: any two of the four triples agree in exactly one coordinate.

For such a triple write `z_t=U_{x,t} conjugate(U_{p,t})`, nonzero. The two-term orthogonality at the unique shared coordinate gives `z_t+z_{t'}=0` for every pair. Any triangle of these relations is impossible over `C`. Thus the lemma holds without an equal-modulus or real-phase assumption. In particular, the extra extension of each high-high pair uses a low symbol in the remaining party.

If another party `j` had five E symbols, all its degrees would be two. Each high j-symbol has six E occurrences, four already in the cube; its two neighbors at each remaining party are exactly the high sets. Its two outside-x occurrences would therefore be three-high, contradicting the lemma. No other party has five E symbols in this case. A party with two E symbols would have degrees summing to ten and hence each degree five; each of the other parties would have at least five E symbols, already impossible. Two parties with three E symbols cannot coexist, since their pair rectangle has at most nine cells but there are ten E pair values. Hence the remaining alphabet sizes are exactly `444` or `344`, in some party order.

### 3.2 The 444 case

Each high A symbol sees both high C symbols in the cube and a low C symbol in an extra high-AB extension; similarly in every direction. Its degree is at least three. As the two high and two low degrees at each party sum to ten, the high degrees are exactly three and the low degrees exactly two.

For high `a∈H_A`, let `f(a)` be its unique low C neighbor; for high `b∈H_B`, let `g(b)` be its unique low C neighbor. The outside extension of every high `(a,b)` has C low, so `f(a)=g(b)` for all four pairs. There is one common low C symbol `ℓ_C`; analogously there is a common low A symbol `ℓ_A`. In the actual AC graph, `ℓ_C` already meets both high A symbols and has degree two. The other low C symbol meets no high A symbol, since each has only the low neighbor `ℓ_C`, and it cannot meet `ℓ_A`, which already meets both high C symbols and has degree two. It has at most the one remaining low A neighbor, contradicting degree two.

### 3.3 The 344 case, including arbitrary complex phases

Let `Q_A=H_A∪{a_*}` and let B,C each have two high and two low symbols. The four extra extensions of the high BC values have A coordinate `a_*`. Thus each high B and C symbol has at least the two high A neighbors and `a_*`; their degrees are exactly three and their low symbols' degrees exactly two.

For `c∈H_C`, let `f(c)` be its unique low B neighbor; for `b∈H_B`, let `g(b)` be its unique low C neighbor. If both maps were constant, say `f≡β` and `g≡γ`, the other low B symbol would have no high C neighbor and, having degree two, would have to meet both low C symbols. But `γ` already meets both high B symbols and has degree two. Therefore at least one of the two maps is bijective.

Each high A symbol already sees both high B and both high C symbols. If `f` is bijective, the two extra high-AC extensions force both low B neighbors; if `g` is bijective, the two extra high-AB extensions force both low C neighbors. Thus both high A degrees are four. Equation (1) gives `d_A(a_*)=2`, and `h_A(a_*)=0` gives exactly four E words at `a_*`: precisely the four extra high-BC extensions.

The two D neighbors of `a_*` partition those four BC cells into two pairs, each at a low D symbol `p`, with two further p-words at one common high A symbol. A diagonal pair would exhaust p's B and C neighbor sets with their high symbols, so the other two p-words would be three-high, impossible. If the pair has fixed high B and both high C values, the two other words have high A and both high C values and must use their unique low B neighbors. Since p has only two B neighbors, `f` must be constant. The transposed same-C case forces `g` constant. Thus both maps bijective is impossible.

It remains to exclude exactly one constant map. By interchanging B and C, take `f≡β` and `g` bijective. Both pairs in the `a_*` partition have fixed B. Write their D symbols `p_b`, one for each high B value `b`. The other two p_b-words have B=`β`, both high C values, and one high A value `a_b`. The two `a_b` are distinct: otherwise a high AC pair would have two outside-x extensions. In the actual `DB | AC` cut, the row `(p_b,β)` has exactly the two columns `(a_b,c)` for `c∈H_C`.

A high B symbol has degree three, surplus two, and hence eight E occurrences. Four are in the x cube and two are the `a_*` words at `p_b`. Its other two are the outside-x extensions of the high AB pairs and have C=`g(b)` and both high A values. They share a third D neighbor `r_b`: they are neither at x nor at p_b, and b has only three D neighbors. Thus in the actual `DC | AB` cut the row `(r_b,g(b))` has exactly the two columns `(a,b)` for `a∈H_A`.

Label the high alphabets by bits and put `Q_{abc}=U_{x,a,b,c}`, all nonzero. Orthogonality of each just-described two-term row to **both** full cube rows gives, for every `a,b`,

```
 Q_{a,0,0} Q_{a,1,1} = Q_{a,0,1} Q_{a,1,0},
 Q_{0,b,0} Q_{1,b,1} = Q_{1,b,0} Q_{0,b,1}.                 (4)
```

These are determinants of actual row restrictions; no phase identification between different words is assumed. Define `r_a=Q_{a,1,0}/Q_{a,0,0}` and `s_b=Q_{0,b,1}/Q_{0,b,0}`. Equations (4) give `Q_{a,1,c}=r_a Q_{a,0,c}` and `Q_{a,b,1}=s_b Q_{a,b,0}`. Computing `Q_{a,1,1}` in both orders gives `s_0=s_1`. Hence the actual full rows `(x,c=0)` and `(x,c=1)` in `DC | AB` are nonzero proportional on their whole common four-column support, contradicting unitary orthogonality. All divisions are by nonzero cube entries. The case with `g` constant and `f` bijective is the transpose. This exhausts 344 and proves that the surplus-four alternative is impossible.

## 4. The two six-word slices: agreement, components, and partner alphabets

The only remaining possibility has distinct D symbols `x,y` with surplus two and three other D symbols with surplus zero. Each high symbol has exactly six E words and exactly two physical partner symbols at each of the other three parties.

A six-word slice is its binary three-cube minus two distinct vertices. Those missing vertices differ in exactly two coordinates. If they differ in only one coordinate, form the `2×2` table of squared moduli summed over that coordinate. The other two actual cuts give every row and column of this table sum one, so opposite entries agree. The empty fiber forces the opposite fiber empty, contradicting six retained vertices. If they differ in all three, label the missing vertices `000,111` and the six nonzero entries at `001,010,011,100,101,110` by `a,b,c,d,e,f`. The three actual row orthogonalities are

```
       a conjugate(e) = −b conjugate(f),
       a conjugate(c) = −d conjugate(f),
       b conjugate(c) = −d conjugate(e).                         (5)
```

Multiplying the first and third and dividing by the second gives `b conjugate(e)=−b conjugate(e)`, impossible. All six entries are nonzero. Thus each slice has exactly one agreement coordinate.

In its agreement coordinate, a high slice has row multiplicities `4,2`; in each differing coordinate it has multiplicities `3,3`. If x's agreement coordinate were a differing coordinate for y, that physical pair system would contain a degree-four value and degree-three values, forbidden by the component lemma. Therefore both high slices have the same agreement coordinate `J`; name the other two `K,L`.

For `z∈{x,y}`, write the actual two-symbol J alphabet as `{F_z,S_z}`: `F_z` is its degree-four row and `S_z` its degree-two row. Let the two K and L alphabets of z be `K_z,L_z`. The F row occupies all four cells of `K_z×L_z`; the S row occupies two diagonally opposite cells, because the missing pair differs in both K and L.

### 4.1 The `DJ | KL` cut

The two degree-four rows `(x,F_x)` and `(y,F_y)` are full rows of the unique `4×4`/12-entry component, so their four physical column sets coincide:

```
          K_x × L_x = K_y × L_y,     hence K_x=K_y=:K, L_x=L_y=:L.  (6)
```

Each degree-two row `(z,S_z)` meets its own full row, hence belongs to the same component. The two low rows have disjoint twin pairs. Their supports are therefore the two complementary diagonals of the common `K×L` square. The 12 high-slice words are exactly the 12 entries in this component; its DJ degrees are `2244`, its KL degrees are `3333`, and the other three components are full `2×2` blocks. In particular, no low-D E word shares one of these four actual KL pair values.

### 4.2 The `DK | JL` and `DL | JK` cuts force the missing equality

This step does **not** assume the J alphabets coincide. For a fixed high `z`, the two actual rows `(z,k)`, `k∈K_z`, both have degree three. They share the two columns `{F_z}×L_z`, so they are in one connected component. Their union of opposite column values is exactly

```
                         {F_z,S_z} × L_z.                       (7)
```

It has four values: the F row supplies both L values and the sparse diagonal supplies both S/L values across the two K rows. Neither `3×3`-minus-one component can contain this connected union of four columns. Therefore the `DK` cut has the `4×4`/12-entry type. Its other three components are `2×2`, so the two degree-three rows of the other high symbol must also be in that **same** 4-by-4 component. Their four-column union is the entire same column side. Thus

```
      {F_x,S_x} × L_x = {F_y,S_y} × L_y,
      {F_x,S_x} = {F_y,S_y} =: J,       L_x=L_y.              (8)
```

The equality of physical J alphabets is forced, not a relabeling and not a consequence of comparing independently completed cuts. Repeating the same argument in `DL | JK` gives the same equality of J alphabets and equality of the physical K alphabets. Together with (6), every high slice uses the **same** `J,K,L` binary alphabets in all three cuts. Equations (6)–(8) also prove that the central 12 entries in each of the three cuts are exactly the same 12 physical high-D words.

For completeness, the exact component degrees in both `DK` and `DL` are as follows. The high-D side is `3333`. If `F_x=F_y` (and hence `S_x=S_y`), the opposite side is `2244`: at a fixed opposite K or L value, the common F symbol receives two entries from each high slice, while the common S symbol receives one from each. If `F_x=S_y` (and `S_x=F_y`), the opposite side is `3333`: each opposite value receives two entries from one F row and one from the other S row. Both role assignments, including the crossed one, are covered. In either case the remaining three components are `2×2`; no additional phase or equal-modulus premise has been used.

## 5. The actual common box gives an exact complex contradiction

The equality (8) is incompatible with the f841 observation that these J alphabets cannot coincide. For a self-contained contradiction, consider the actual restriction of `U` to

```
                     {x,y} × J × K × L.                         (9)
```

In each of the three cuts, take the four rows containing one of `x,y` and one of the two selected symbols of the other party on that side. They all occur as E rows. Since each high D symbol has exactly these two partners at each other party, every E entry in these rows lies in (9); no P entry can share an E pair value. Thus the four actual globally orthonormal rows are supported entirely on the four selected opposite pair values. Their restriction is a `4×4` unitary in each cut. This is the **same** restricted tensor and the **same** entries in all three cuts, with 12 nonzero entries, not three independent witnesses.

Divide this restricted tensor by two and call the resulting pure four-qubit state `φ`. A `4×4` unitary restriction in each cut gives all two-qubit reduced states `I_4/4`; the state is normalized. This is impossible over the complex numbers. For the Pauli strings `R`, define `a_R=tr(ρR)` for `ρ=|φ⟩⟨φ|`, and let `A_r=Σ_{wt(R)=r} a_R²`. Pairwise maximal mixing gives `A_1=A_2=0`. The complementary one-qubit state is `I_2/2`, so each three-qubit marginal has purity `1/2`. Its Pauli expansion gives a weight-three sum of `3`; summing over the four triples gives `A_3=12`. Purity of ρ gives `1+A_3+A_4=16`, hence `A_4=3`. The spin-flipped operator `\widetildeρ=Y^{⊗4}\overlineρY^{⊗4}` is positive, while the Pauli expansion yields the exact identity

```
 tr(ρ \widetildeρ) = (1−A_3+A_4)/16
                     = (1−12+3)/16 = −1/2.                     (10)
```

The trace of a product of positive semidefinite operators is nonnegative. Equation (10) is the contradiction. Thus the two six-word high slices cannot exist. Together with §3, the entire possible five-symbol E-alphabet party is excluded, proving the candidate statement (T), subject to ordinary review of the written derivation.

## 6. Inputs, coverage, conditionality, and limits

Before any mathematical body or task-specific mathematical reasoning, I read the manifest, freeze receipt, final pre-dispatch binding, parent metadata supply, actual dispatch receipt, and all 23 listed status-only controls. Initial non-raw administrative displays with elisions were recovered by complete raw reads before acknowledgement. The exclusive new local `prebody-ack-v1.md` was written after confirming the filename absent from the owned directory, and a direct acknowledgement was delivered to Main before the packet was opened. Controls supplied permissions/status only and were not mathematical inputs. The required workspace memory summary and written-math protocol were consulted administratively. No previous mathematical exposure to this wave is known from this task context; no claim about private cognition is made.

After both acknowledgements I read the single literal packet part serially in raw windows `1–20, 21–40, …, 561–580, 581–589`, including the ending. Each display was below 30,000 bytes; no packet clipping was observed and no clipped portion required recovery. The complete rendered input bodies were S1 f841 LF 1–203, S2 f826 LF 1–163, S3 f827 LF 1–145, S4 parent disposition LF 1–33, and S5 parent disposition LF 1–23. The parent-declared part SHA-256 is `0ead5e6ebcda91b845f3f13380d3c940d0c87e1f6245e49fc67a19a090e78549`; the five parent-declared source pins are, in order, `3788449b5decefd62ee107a01410e1572e3c089a9ff8a40ac659e2b51205c912`, `b826085181355b587d96df2825c7ef5fb1b9ffc13ff9531818f640d39a392fa8`, `c78020e48e7ca16159cf74debcb25cc2b747be06b4c371230142298c1ea95814`, `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336`, and `f84c4b2eba89f99b693fa1c9fdfd5b4ef90eb5e6f7d9c5a99ca7373cc11fd0dc`. These are supplied metadata, not independent source-identity certification or an independently recomputed hash.

S1 and S2 are prior nonblind author candidates, not automatically accepted premises. This candidate reconstructs the precise actual t26 low-excess component/twin/degree interface, the surplus-four exclusion, six-slice distance and synchronization, and the closed-box obstruction in §§2–5. If the component reconstruction is not accepted, the result is conditional on precisely that named per-cut actual-unitary interface, including its `3333`/`2244` alternatives and twin-pair necessity; it is not conditional on an unstated global theorem. No absent linked proof body is silently imported. S3–S5 provide context only: their t28/other-t conclusions and historical computations are not premises of (T). All genuinely held episodes and all their proof, method, planning, selection, verification, reporting, confidence and downstream consumers remain NONINPUT.

No packet or control link, sibling author output, parent q5 candidate, unlisted source, network, external model, scientific code or evaluation, subprocess, solver, test, compilation, build, lint, formatter, Git or deletion was used. No executable was prepared, so no code hash or computational verification is claimed. The q5 conclusion is a proposed written result for separate parent disposition; it does not assert that any remaining profile is realizable or that all of t26/N50 is excluded. Any correction must be additive and must not modify these candidate bytes.
