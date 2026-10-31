# Actual AME(4,6), N=50, t=26: three profiles and a common-phase criterion

**Author candidate; nonblind, same harness; parent disposition and independent review are separate.** Throughout, one normalized complex tensor `ψ` is expressed in one fixed product orthonormal basis, `U=6ψ`, exactly 50 entries of `U` are nonzero, exactly 26 have modulus one, and each of its three 36-by-36 balanced flattenings is unitary. All statements quantify over arbitrary complex coefficients, not signs, equal nonzero moduli, or separate cut realizations. `P` denotes its 26 modulus-one words and `E` the other 24. We prove the necessary sorted E-alphabet profiles `3445`, `4444`, `4445`; the more precise five-alphabet restrictions below; and an exact same-object residual feasibility criterion. In particular, the six-word slices have missing-pair **distance exactly two**, strengthening the distance-two-or-three statement of packet S1 using a separate local three-cut argument. This candidate does **not** exclude the whole t26 branch, claim a global support minimum, construct an AME state, or establish novelty, priority, formal/human/family acceptance, or a parent decision.

## 1. Actual support, excess and binary-slice facts

All pair projections here and below are projections of the same `P,E⊂[6]^4`. A modulus-one entry of a unitary exhausts its row and its column. Consequently, in every physical party-pair system, the 26 P values are distinct; no E word has one of those values; the remaining ten values are E values; and each has at least two E extensions. The last assertion follows because a degree-one residual row or column has a unique entry of modulus one, already belonging to P. Deleting P rows and columns leaves a 10-by-10 unitary support with 24 entries and excess `24−2·10=4`.

Let `Q_i` be the set of E-used symbols at party `i`, `q_i=|Q_i|`, `s_i(a)` the number of E words at `a`, and `d_{ij}(a)` the number of E partners of `a` at party `j`. Every one of the six physical pairs `(a,b)` is either a P singleton or an E value, so the number of P words containing `a` is `6−d_{ij}(a)` for every `j≠i`. Thus the degrees agree: call the common value `d_i(a)`. Define `h_i(a)=s_i(a)−2d_i(a)`. Then, for each party,

```
      d_i(a) ≥ 2,       Σ_a d_i(a)=10,
      h_i(a) ≥ 0,       Σ_a h_i(a)=4.                         (1)
```

Indeed each E pair line has at least two words. If `d_i(a)=1`, all three other coordinates of a word at `a` are fixed, permitting at most one distinct word, a contradiction. In particular `2≤q_i≤5`; `q_i=1` is impossible since its sole degree would be 10, larger than a six-symbol partner alphabet.

If `d_i(a)=2` and `h_i(a)=1`, the five words at `a` form five vertices of a binary three-cube. For each axis, its two actual flattening rows have support sizes 2 and 3 in the four complementary cells; their overlap is nonempty and, by orthogonality, not a singleton. Thus the five vertices induce at least two edges along each axis, at least six total. Deleting the other three cube vertices removes at least `9−2=7` of the 12 edges, because the cube is triangle-free and three vertices induce at most two edges. At most five remain. Hence

```
                 h_i(a)=1  implies  d_i(a)≥3.                (2)
```

### Low-excess cut classification, reconstructed

A connected component of a unitary support is square: the restricted rows are orthonormal, so there cannot be more rows than columns, and the same argument for columns gives the reverse inequality. Two distinct rows or columns cannot have exactly one common nonzero. In a connected component of order greater than two, a degree-two row has two **twin** columns, with equal row neighborhoods of size at least three. If two degree-two rows shared that column pair, their orthonormal row vectors would span the two columns, forcing all other rows to vanish on them and isolating a 2-by-2 unitary block. Hence distinct low rows have disjoint twin pairs. Transpose throughout.

For a component of order `m`, excess `e`, and `k` degree-two rows, the other rows contribute at least one each to row excess, while the `k` disjoint twin pairs contribute at least `2k` to column excess. Thus

```
                  m−e ≤ k ≤ floor(e/2).                       (3)
```

Excess zero gives a full 2-by-2 component; excess one is impossible; excess two gives a 3-by-3 matrix with one zero. For excess three, order is at most four. If it were four, there would be one low row and three degree-three rows. Its twin columns both have degree three; one high row avoids both and would have to fit three nonzeros in the other two columns. Thus excess three is a full 3-by-3 component.

For excess four, order is at most six. At order five there are one or two low rows. With one, the four high rows all have degree three. The twins cannot have all four high rows as neighbors, since the other three columns would then have only four entries although each has degree at least two. A high row avoiding the twins uses all three other columns, and a high row using them uses exactly one of those columns: a forbidden singleton overlap. With two low rows, the four twin columns each have degree three and the remaining column degree two. Their two-high-row neighborhoods are two-subsets of three high rows; one-overlap is forbidden, so the subsets coincide and the remaining high row has at most one neighbor.

At order six, there are two low rows and two low columns, and every other line has degree three. The low columns have disjoint two-element neighborhoods `A,B` among the four high rows; low rows cannot meet them because their own two neighbors are high twin columns. Each twin pair's two high neighbors must be all of `A` or all of `B`, otherwise its column meets a low column once. If the two twin pairs choose the same set, the other two high rows have degree at most one; if they choose different sets, the component splits. Both are impossible. An order-three component cannot have excess four, so the positive-excess component partitions of the residual 10-by-10 support give exactly

* two 3-by-3-minus-one components and two full 2-by-2 components; or
* one connected 4-by-4, 12-entry component and three full 2-by-2 components.  

For the 12-entry component, each side's degree partition is `3333`, `2334`, or `2244`. The middle one is impossible: let the degree-two row have twin columns. If those columns have degree three, the degree-four row meets them, leaving one degree-three row avoiding both and unable to attain degree three. If the twins have degree four, the other two columns each have degree two; the two degree-three rows must use different ones, so those columns meet only in the degree-four row. If one side is `2244`, its two low rows have disjoint pairs and the two other rows are full, so the opposite side is `3333`. Consequently each physical pair system has either four E values of multiplicity three, or two of multiplicity four; all remaining E values have multiplicity two. The opposite pair system may have the other degree pattern in the same 12-entry component.

This is an actual-unitary argument, including the twin-pair step, not a classification of arbitrary graph masks. It reconstructs the precise t26 interface stated in packet S3. If any part of this reconstruction is not accepted, all uses below are conditional on that named per-cut interface **including** its stated degree alternatives and twin necessity; no linked but absent proof body is silently imported.

### A closed binary four-party box is impossible

Suppose two actual symbols are selected at each party and, in each of the three actual cuts, the four rows on one chosen side are supported entirely on the four selected opposite pair values. Those four globally orthonormal rows form a 4-by-4 unitary. Using the **same** entries in all cuts, the restricted tensor divided by two would be a normalized four-qubit pure state with every two-qubit marginal `I_4/4`. Such a state does not exist: for Pauli coefficients `a_R=tr(ρR)` and `A_r=Σ_{wt(R)=r}a_R²`, pairwise maximal mixing gives `A_1=A_2=0`. Each three-qubit marginal has purity `1/2`, so its weight-three Pauli sum is three; summing over the four triples gives `A_3=12`. Purity of `ρ` gives `A_4=16−1−12=3`. The positive spin flip `Y^{⊗4}\barρY^{⊗4}` has

```
        tr(ρ Y^{⊗4}\barρY^{⊗4}) = (1−A_3+A_4)/16 = −1/2,
```

contradicting positivity. The normalization and all three cuts are essential; this does not invoke a separately chosen four-qubit witness.

## 2. A surplus-four cube and the no-three-high lemma

Suppose `q_D=5` and `h_D(x)=4` for one D symbol. Then every D degree is two, all four remaining D surpluses vanish, and the eight E words at `x` are the full cube `H_A×H_B×H_C`, where each `H_j` has two symbols. Each high symbol in each `H_j` already participates in an E pair of multiplicity four, so it has surplus at least two; the total four forces exactly two at each high symbol and zero at every other symbol of that party.

In the cut `Dk | ij`, the two rows `(x,k)` for `k∈H_k` are degree four. They belong to the same 12-entry component and have common opposite neighbors `H_i×H_j`, each of degree three. Therefore each high-high pair in `AB`, `AC`, or `BC` has precisely the two x-cube extensions plus one further E extension.

**No-three-high.** No E word outside the x slice is high in all three of A,B,C. Otherwise let its D symbol be `p≠x`. Since `h_D(p)=0` and `d_D(p)=2`, that slice has four words, with exactly two at each of its six D/partner pair values. Comparing each row `(p,j_high)` with `(x,j_high)` shows that the other word in the row is high in both remaining coordinates: a singleton overlap is impossible. These three mates are distinct, because two outside-x words cannot share a high-high pair that already has two x-cube extensions and total multiplicity three. Thus all four p-slice words are high-high-high; no pair of them repeats a two-coordinate projection. They are a binary parity class, and any two agree in exactly one coordinate. For each triple `t`, put `z_t=U_{x,t}\overline{U_{p,t}}≠0`. For each pair `t,t'`, orthogonality at their common coordinate gives `z_t+z_{t'}=0`. The three edges of a triangle give a contradiction over the complex numbers. Hence the twelve outside-x extensions of the high-high pairs are twelve distinct words, each high in exactly two of A,B,C.

## 3. At most one five-symbol E alphabet

At a five-symbol party all degrees equal two by (1). By (2) and total surplus four, its surplus vector is, up to permutation, either `(4,0,0,0,0)` or `(2,2,0,0,0)`.

If D has the first vector and another party `j` also has `q_j=5`, each of the two high symbols at j has degree two, surplus two, and six occurrences. Four of its occurrences are already in the x-cube; its two neighbors at each other party are consequently exhausted by that cube. Its two remaining words are outside x and high at all three of A,B,C, contrary to §2. Thus two five-symbol parties would both have surplus `(2,2,0,0,0)`.

Name their high symbols `a_0,a_1` and `b_0,b_1`. Label every high-high pair by its E multiplicity minus two, taking absent pairs to have label zero. Low symbols cannot touch a positive label, and the two row and column sums are two. Since a line has multiplicity at most four, up to relabeling the only weighted matrices are all ones, or diagonal twos and off-diagonal zeros.

* **Four multiplicity-three pairs.** Each high symbol has two neighbors at each remaining party. Three distinct complementary extensions at a high-high pair lie in the product of two intersections of two-element neighbor sets. Their product has size at least three, so both intersections have size two. Across the four pairs, all high A and high B symbols share the same two-symbol alphabets `K,L` at the remaining parties. All twelve words at high A and all twelve at high B are in that binary box.
* **Two multiplicity-four pairs.** They are the two full rows of the same 12-entry component and share four complementary pair values. The four extensions of either pair form a `2×2` rectangle because each participating high symbol has degree two. Hence the two rectangles, and their partner alphabets `K,L`, agree. Each high A has two further words; they use `K,L`, so their rows meet the two full rows and are the component's two remaining rows. The same argument for high B shows those same four words also have high B.

In either case, for each cut choose the side containing A. Its four rows `(a_high, partner-in-box)` are E rows, occur, and have all their support inside the four opposite box values. The common binary-box lemma contradicts the actual three-cut unitary. Thus **at most one `q_i` is five**.

## 4. Actual P rules out q=2, two q=3, and profile 3444

If `q_A=2`, its two E degrees sum to ten, so each is five, and every other party has at least five E symbols and hence exactly five. Each A E symbol occurs in `6−5=1` P word. These two P words must both use the unique outside-E symbol at B, C, and D, giving the same BC projection, contrary to P injectivity. Thus `q_i≥3`. Two q=3 parties are impossible because ten distinct E pair values cannot fit in a 3-by-3 rectangle.

For the remaining profile calculation, let `n_k` count P words with exactly `k` coordinates in the corresponding E alphabets. The count of P incidences at party i within Q_i is `6q_i−10`, and the number within the pair rectangle Q_i×Q_j is `q_iq_j−10`. Thus

```
 Σ_k n_k = 26,
 Σ_k k n_k = 6 Σ_i q_i − 40,
 Σ_k C(k,2)n_k = Σ_{i<j} q_iq_j − 60.                         (4)
```

For `3444` these yield `n_0+n_3+3n_4=0`; hence `(n_0,n_1,n_2,n_3,n_4)=(0,2,24,0,0)`. Let A be the q=3 party and B,C,D the q=4 parties. The A E alphabet has eight P incidences. Exactly two P values lie in each of the AB, AC, AD E rectangles, so six of the eight incidences belong to two-inside words. The two single-inside P words therefore both have their sole inside coordinate at A.

Fix a B E symbol `b` of degree d. Each of the three A-outside values pairs with b in a P word. None of these three is single-inside; each has B inside and exactly one of C,D inside. There are `4−d` P values with b and a C-inside symbol, and `4−d` with b and a D-inside symbol. Thus `3=2(4−d)`, impossible. This is a contradiction in the **same 26 P words**, not in independently completed pair systems.

Together with §3, the only sorted profiles are `3445`, `4444`, `4445`. Solving (4) and nonnegativity gives the following necessary, not claimed realizable, P profiles:

| sorted q | possible `(n_0,n_1,n_2,n_3,n_4)` |
|---|---|
| 3445 | `(0,1,20,5,0)`, `(0,0,23,2,1)` |
| 4444 | `(0,2,18,6,0)`, `(0,1,21,3,1)`, `(0,0,24,0,2)` |
| 4445 | `(0,2,12,12,0)`, `(0,1,15,9,1)`, `(0,0,18,6,2)` |

## 5. Every five-symbol party has exactly two surplus-two symbols

Assume instead the surplus-four cube of §2. By §4 the other alphabets are either `444` or `344`. The two high symbols at each other party have surplus two and all low symbols surplus zero.

### Other alphabets 444

For each high symbol of any of A,B,C, the outside-x extension of a high-high pair forces a low neighbor in the remaining party. Thus each high degree is at least three. Since the four degrees sum to ten and both low degrees are at least two, the high degrees are exactly three and the low degrees exactly two. For `a∈H_A`, let `f(a)` be its unique low C neighbor, and for `b∈H_B`, let `g(b)` be its unique low C neighbor. Every high AB pair has an outside-x extension with C low, so `f(a)=g(b)` for all four choices. Denote this common low symbol by `ℓ_C`; the analogous `ℓ_A,ℓ_B` exist in the other directions. The low C symbol `ℓ_C` is adjacent to both high A symbols and has degree two. The other low C symbol has no high A neighbor, because each high A symbol's sole low C neighbor is `ℓ_C`; nor can it meet `ℓ_A`, because `ℓ_A` already has both high C neighbors and degree two. It has at most one remaining low A neighbor, contradiction.

### Other alphabets 344: both-constant and both-bijective subcases

Let `Q_A=H_A∪{a_*}` and let B,C each have two high and two low symbols. The four high BC pairs have their four outside-x extensions at A=`a_*`. Each high B or C symbol is therefore adjacent to both high A symbols and to `a_*`; it has degree three, while each low B or C symbol has degree two.

For high `c∈H_C`, let `f(c)` be its unique low B neighbor; for high `b∈H_B`, let `g(b)` be its unique low C neighbor. If both maps were constant, with values `β` and `γ`, then β would already meet both high C symbols and the other low B symbol would have to meet both low C symbols. But γ already meets both high B symbols and has degree two, contradiction. Each map is a map between two-element sets, so at least one is bijective.

Every high A symbol meets both high B and both high C symbols in the cube. For each high c its outside-x high-AC extension uses B=`f(c)`, and for each high b its outside-x high-AB extension uses C=`g(b)`. A bijective f or g therefore forces **each** high A degree to be four. By (1), `d_A(a_*)=2`; its surplus is zero, so its entire four-word slice is exactly the four outside-x extensions at the high BC pairs.

Each pair `(p,a_*)` has exactly two E extensions. Thus the four high-BC cells are partitioned into two pairs, one for each of two D symbols `p≠x`. Every such p has four E words and exactly two A neighbors: `a_*` and one high A symbol. If its two BC cells are diagonal, its two B and two C neighbors are both the respective high sets, so its other two words would be three-high, contradicting §2. If the cells share B and differ in C, the two remaining words have high A and high C; their B values are `f(c)`. The two-neighbor limit at B then forces f constant. If they share C instead, the symmetric argument forces g constant. Hence both maps bijective is impossible.

### Exactly one constant map: the complex-ratio obstruction

By symmetry take `f(c)=β` constant and `g` bijective. Every pair in the `a_*` partition must share its high B value b. Write its D symbol as `p_b`. The other two words of the `p_b` slice have B=`β`, both high C values, and one common high A value `a_b`. The two `a_b` are distinct, because otherwise a high AC pair would have two outside-x extensions. In the actual `DB|AC` cut, the two rows `(p_b,β)` each use the two columns with one fixed high A value and both high C values.

For each high B symbol b, its degree is three and surplus two, so it has eight E occurrences. Four are in the x-cube and two are the `a_*` words at `p_b`. The two remaining words are the outside-x extensions of the two high AB pairs; both have C=`g(b)`. They use a common third D neighbor `r_b`: it cannot be x or `p_b`, because both have only high C neighbors, and b has only three D neighbors. Thus in the `DC|AB` cut the row `(r_b,g(b))` has the two columns with fixed b and both high A values. All these are rows of the actual 12-entry components, not selected independent matrices.

Write `Q_{abc}=U_{x,a,b,c}` for the full high cube, with binary labels. Orthogonality of the just-described two-term rows against **both** full cube rows gives the determinants, for every `a,b`,

```
 Q_{a,1,0}/Q_{a,0,0} = Q_{a,1,1}/Q_{a,0,1},
 Q_{0,b,1}/Q_{0,b,0} = Q_{1,b,1}/Q_{1,b,0}.                 (5)
```

All denominators are nonzero. Set `Q_{a,1,c}=r_a Q_{a,0,c}` and `Q_{a,b,1}=s_b Q_{a,b,0}`. The two computations of `Q_{a,1,1}` give `s_0=s_1`. Thus the actual full rows `(x,c=0)` and `(x,c=1)` in `DC|AB` are nonzero proportional on all four columns, contradicting their orthogonality. No real-phase or equal-modulus assumption was made. The case g constant and f bijective is the transposed argument.

All subcases have been exhausted. Therefore whenever some party has `q=5`, its degree vector is `(2,2,2,2,2)`, its surplus vector is `(2,2,0,0,0)`, and each of its two high symbols has exactly six E words.

## 6. Exact missing-pair distance and cross-cut synchronization

First prove a local statement independent of any t28 exclusion. Fix an E symbol `x` of degree two and surplus two at any party. Its six words are a binary three-cube with two distinct vertices deleted, and the two rows at x in each of the three cuts are actual unit vectors and mutually orthogonal.

* If the deleted vertices differ in just one coordinate, fix the other two coordinates and sum squared moduli over that coordinate. The resulting 2-by-2 table has all row sums and column sums one. Opposite table entries agree, so an empty fiber forces its opposite fiber empty too, contradicting six nonzeros.
* If they differ in all three coordinates, relabel the deleted vertices `000,111` and write the six nonzero coefficients at `001,010,011,100,101,110` as `a,b,c,d,e,f`. The three actual row orthogonalities are

```
        a conj(e)=−b conj(f),    a conj(c)=−d conj(f),
        b conj(c)=−d conj(e).                                  (6)
```

Multiplying the first and third and dividing by the second gives `b conj(e)=−b conj(e)`, impossible. All six divisions/cancellations are legitimate because the indicated entries are nonzero.

The deleted vertices are distinct, so their distance is **exactly two**. This reconstructs the local h=2 observation available in packet S2 without assuming any t28 cut mask or t28 conclusion. It is a necessary local fact, not a whole-t26 exclusion.

Now let `x,x'` be the two high D symbols of a q=5 party. For any one of A,B,C, the two line multiplicities within either six-word slice are `(4,2)` if the two deleted vertices agree in that coordinate, and `(3,3)` if they differ. The per-pair classification in §1 permits either two multiplicity-four values or four multiplicity-three values, but not a mixture. Thus the two high slices have the same set of agreement coordinates. By the local argument this set is a **single** common coordinate `J`; call the other two coordinates `K,L`.

In the `DJ|KL` cut, the two degree-four rows belong to the same 12-entry component, so their opposite four neighbors coincide. Therefore `x` and `x'` have the same actual two-symbol alphabets at both K and L. Each slice also has a degree-two row at J which overlaps its own full row and hence lies in that component. The two degree-two rows are distinct and have disjoint twin pairs. Their supports on the common K-by-L square are complementary diagonals. Equivalently, after identifying the actual K,L alphabets, **the two missing K,L pairs are complementary diagonals**.

The two two-symbol neighbor alphabets at J cannot be equal: if they were, both entire six-word slices would lie in one binary four-party box, and all four rows on the side containing the high D symbols would be supported inside the selected opposite pair values in each of the three cuts. The closed-box lemma would contradict unitarity. Write each J alphabet as `{F_x,S_x}`, where F labels its degree-four row and S its degree-two row, and similarly for `x'`. If their intersection consists of exactly one symbol, it cannot be `F_x=S_{x'}` or `S_x=F_{x'}`. For instance, in the first case, fix any K symbol and compare the two E rows `(x,K)` and `(x',K)`: their only common J symbol is that crossed value, and the sparse diagonal has exactly one L entry at that K, producing one forbidden overlap. Thus a one-symbol intersection is either `F_x=F_{x'}` or `S_x=S_{x'}`. In particular, if `q_J=3`, the two distinct two-subsets must intersect once, in one of these same-role ways. No equality of phases between slices is assumed.

## 7. Exact SAME-P/E, positive-amplitude and common-phase iff

The following is an exact equivalence for this one N50/t26 branch. The structural requirements are **necessary filters**, not a claim that any support passes them.

Choose a single pair of actual sets `P,E⊂[6]^4` with `|P|=26`, `|E|=24`. Require in each of the six physical pair systems that P has 26 distinct values, the E projection is the complementary ten values, and each E value has at least two extensions. Require in every actual balanced cut one of the support-component forms in §1, including the genuine-unitary degree alternatives, and the alphabet, degree, surplus, P-moment, and high-slice restrictions proved in §§1–6. These are all conditions on the **same** P and E, including the same underlying symbols and actual projected word sets.

Assign one real variable `x_w>0` to each `w∈E`, shared by every cut, and impose for every E pair value p in all six systems

```
                Σ_{w : w_pair=p} x_w = 1.                      (7)
```

Each such sum has at least two positive terms, so `x_w<1`. For every unordered pair `p≠p'` of E pair values in each of the six systems, let `I(p,p')` be their common complementary pair values. Forbid `|I|=1`. For `I={r,s}`, write `u=(p,r), v=(p',r), w=(p,s), z=(p',s)` and impose

```
          x_u x_v = x_w x_z,
          M_(p,p') = e_u−e_v−e_w+e_z.                          (8)
```

Stack **all** these integer rows, including the rows arising in transposed physical pair systems, in a matrix `M` with 24 columns; do not replace repeated occurrences in distinct cuts by independent word variables. In particular a common phase solution requires

```
          for every y∈ker_Z(M^T),  Σ_i y_i is even.            (9)
```

Necessity follows by pairing `y` with `Mθ=(1/2)·1` over `R/Z`. Conversely, (9) is sufficient for this two-term phase subsystem: an integral Smith normal form makes each nonzero diagonal multiplication a surjection of `R/Z`, while each zero row tests precisely an integral left-kernel parity relation. A mod-two dependency alone is not necessarily an integral dependency.

Finally require a **single** phase vector `θ∈(R/Z)^24` satisfying the two-term equations `Mθ=(1/2)·1` and, simultaneously for every overlap of size three or four in every physical pair system,

```
  Σ_{r∈I(p,p')} sqrt(x_(p,r) x_(p',r))
       exp(2πi(θ_(p,r)−θ_(p',r))) = 0.                        (10)
```

No equation is needed for zero overlap. A polygon inequality for the term lengths is only a necessary relaxation of (10), and (9) is not a substitute for the coupled higher-overlap equations.

**Proof of iff.** An actual tensor supplies P,E, the common squared moduli and phases, (7) from row norms, (8)–(10) from orthogonality, and all listed necessary filters by §§1–6. Conversely suppose one physical P,E and one simultaneous solution exist. Put `U_w=1` on P, `U_w=sqrt(x_w) exp(2πiθ_w)` on E, and zero elsewhere. Each P row and column is an isolated unit entry in every cut. Equation (7) makes each E row a unit vector, (8) and the two-term phase equation make every two-overlap inner product zero, and (10) handles the remaining overlaps; no singleton remains. Thus each square flattening has orthonormal rows and is unitary. Summing (7) over one physical pair system gives `Σ_E x_w=10`, hence `Σ|U_w|²=26+10=36`, so `ψ=U/6` is normalized. The support has exactly 50 entries and precisely the 26 P entries have modulus one. This establishes the asserted equivalence; it does not solve the residual feasibility problem.

## 8. Coverage, process, imports, and limits

Before the first mathematical packet read or task-specific mathematical reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all 23 manifest-listed status-only controls. The first non-raw displays of administrative JSON had elided blocks; these were recovered by full raw reads before the exclusive local `prebody-ack-v1.md` and before direct delivery of the prebody acknowledgment to Main. Only after both acknowledgments did I read the one literal packet part serially in raw windows `1–20, 21–40, …, 381–400, 401–407`, including the ending. Each displayed window was below 30,000 bytes; no packet clipping was observed and no packet recovery was needed. The part contains complete bodies S1 original LF 1–163, S2 LF 1–145, S3 LF 1–33, S4 LF 1–23, and S5 LF 1–21. Parent-declared part SHA-256 is `89b5515fbb78cf530d1803446872aa09663d4f6cb88589e5dee5e3117ec42c9e`; it and the per-source pins in the manifest are supplied metadata, not independently recomputed hashes or source-identity certification.

S1 and S2 are earlier, nonblind author candidates and are **not** accepted merely by being packet inputs. S3 states the t26 cut interface, which is independently reconstructed in §1; S2's local h=2 argument is independently reconstructed in §6. S4/S5 are complete background inputs, not premises for a t26 global theorem. References within those sources to their former packets, low-excess source bodies, historical executions, global t bounds, no-OLS, and other linked artifacts do not authorize reading or importing them. No missing older body is treated as an independently proved load-bearing premise; if the written §1 reconstruction is disputed, the precise conditional import is the actual-unitary t26 component/twin/degree interface named there, not an unqualified global result. All genuine held episodes and all proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT.

No packet/control link was followed, no sibling science was read, and no network, external model, scientific eval, code execution, subprocess, test, solver, compilation, build, lint, formatter, Git or deletion was used. No executable was prepared, so there is no code hash or computational verification. The first unsolved exact question is whether **one** actual P/E incidence and **one** simultaneous positive-amplitude/common-phase solution of (7)–(10) exist. The three profiles and the sharper q5 geometry are necessary, not existence claims. This artifact is a candidate for separate parent scrutiny; no family/human/formal acceptance, t26 whole exclusion, global minimum, or publication-priority assertion is made. Any correction must be additive rather than changing these bytes.
