# Actual 4444 surplus and F-edge elimination — author candidate

**Status and exact scope.** This is a nonblind, same-harness written reconstruction, not a review disposition or an acceptance. For every single complex tensor `U:[6]^4→C` whose three balanced 36-by-36 flattenings are unitary, whose support has exactly 50 words, exactly 26 of these have modulus one, and whose remaining 24 words use exactly four symbols at each party, the following necessary conditions hold: each party has two surplus-two symbols of degree three and two surplus-zero symbols of degree two; in every physical pair system the four high/high values have multiplicity three and every other E value has multiplicity two. Equivalently, the F-edge set defined below is empty. All moduli and phases are arbitrary; the *same* tensor and its actual words are used in every cut. This is an implication under the assumed tensor, not an assertion that it exists. It does not exclude the remaining all-T 4444 branch, any other alphabet profile or t value, N=50 globally, or establish a global minimum.

The proof below reconstructs the load-bearing genuine-unitary component interface rather than using an unprovided enumeration. No linked, absent proof body is imported. If that reconstruction is not accepted, the precise conditional import is the actual-unitary component/twin and T/F mask interface in §2, including its full-row and sparse-row assertions; no larger theorem is imported. All conclusions remain author-candidate claims pending independent checks and parent disposition.

## 1. Actual support, degrees, and elementary orthogonality

Write `P={w:|U_w|=1}` and `E={w:0<|U_w|<1}`; thus `|P|=26`, `|E|=24`. A unit entry of any flattening exhausts its row and column. Therefore the P projections are injective in each of the six physical pair systems, and each physical pair value is either one of 26 isolated P values or one of the remaining ten E values. Deleting those P rows and columns gives a 10-by-10 unitary support with exactly 24 E entries. Every E line has at least two entries: a one-entry unitary line would be a modulus-one word, contrary to its belonging to E. Distinct rows, or distinct columns, cannot have exactly one common nonzero; that lone nonzero product could not sum to zero.

For an E-used symbol x at party i, let `d_i(x)` be the number of its distinct E-neighbors at any particular other party, `s_i(x)` the number of E words containing x, and `h_i(x)=s_i(x)-2d_i(x)`. The degree does not depend on the other party: the number of P words at x is `6-d_i(x)` in every pair projection. Each neighbor line contributes at least two words, so h is a nonnegative integer. If `d_i(x)=1`, all three other coordinates in every E word at x are fixed, yielding at most one distinct word, impossible. Thus, with four used symbols at i,

```
 d_i(x)≥2,      Σ_x d_i(x)=10,      h_i(x)≥0,      Σ_x h_i(x)=4.    (1)
```

The only degree multisets are `4,2,2,2` and `3,3,2,2`.

A degree-two, surplus-one symbol cannot occur. Its five E words lie in a binary 3-cube, with both values actually used in each direction. For each direction, the two corresponding pair rows contain respectively two and three words; among the four possible complementary positions they overlap at least once, hence at least twice by orthogonality. Thus the five vertices induce at least six cube edges, counting the three directions. But three deleted cube vertices induce at most two edges, so they remove at least `9-2=7` of the 12 edges, leaving at most five. Consequently

```
                 h_i(x)=1  ⇒  d_i(x)≥3.                              (2)
```

## 2. Reconstructed actual-unitary component and T/F masks

A connected support component of a unitary is square: its rectangular submatrix has orthonormal rows and orthonormal columns, giving both inequalities between its row and column counts. In a component of order greater than two, the two columns adjacent to a degree-two row are twins: a row meeting just one would overlap it once. These columns have degree at least three. If their only two neighboring rows were degree two, those two orthonormal rows would span the two columns and isolate a 2-by-2 component. Similarly, two distinct degree-two rows in a larger component cannot share a neighbor: they would have the same two neighbors, and actual orthonormality would isolate that 2-by-2 block. These claims also hold with rows and columns interchanged; the isolation step is genuinely unitary, not merely a graph no-singleton condition.

For a component of order m, write `e_c=number of entries−2m` and let k be its degree-two row count. The other `m-k` rows each contribute at least one to excess, and the k disjoint twin-column pairs each contribute at least two to column excess. Therefore

```
                  m−e_c ≤ k ≤ floor(e_c/2).                            (3)
```

Excess zero gives a full 2-by-2 component: all rows and columns have degree two, and (3) rules out a larger connected component. Excess one is impossible. For excess two, (3) gives order at most three; the only positive possibility is order three, with degree sequence `2,3,3` on each side, hence a full 3-by-3 with the low-row/low-column intersection deleted. For excess three, order is at most four. Order four would have one low row and three degree-three rows. Each high row must use both of the low row's twins, because avoiding them leaves only two columns; the twins would then each have degree four, already contributing four column-excess units. Hence excess three is a full 3-by-3.

For excess four, (3) gives `m≤6`. At order five, k is one or two. With k=1 the four high rows have degree three. Some high row avoids the twin columns, since otherwise both twins have degree five and already use six excess units; at least one high row uses them, since their degree is at least three. The avoiding row uses all three other columns and meets a using row exactly once. With k=2 the four twin columns each have degree three and the fifth column degree two, exhausting the four excess units. Each twin pair's two high neighbors form a two-subset of the three high rows. Distinct two-subsets overlap in exactly one high row, so singleton column overlap forces the subsets to coincide. The remaining high row could then use only the fifth column, impossible.

At order six, k=2 and, by transposition, there are two low columns; every other row and column has degree three. The two low columns have disjoint two-subsets of the four high rows: singleton intersection is forbidden, while identical subsets would isolate an actual 2-by-2 unitary. Thus they partition the high rows into two pairs. Each of the two twin-column pairs must take one whole high-row pair, since meeting either low column once is forbidden. If both choose the same pair, the other two high rows have at most one neighbor; if they choose different pairs, the component disconnects. Thus order six is also impossible. An excess-four component has order four.

The total cut excess is four. Positive components must therefore be either two excess-two components or one excess-four component, the rest being 2-by-2. Consequently each actual cut has exactly one of:

* **X:** two 3-by-3-minus-one components and two full 2-by-2 components;
* **Y:** one connected 4-by-4, 12-entry component and three full 2-by-2 components.

On either side of the Y component the only degree partitions are `3333`, `2334`, `2244`. The middle partition cannot occur. Its unique low row has twin columns. If they have degree three, the degree-four row and one degree-three row use them, leaving the other degree-three row to fit in only two columns. If they have degree four, the two remaining degree-two columns are both used by the full row; the two degree-three rows must use different remaining columns, making those columns overlap exactly once. If one side is `2244`, its degree-two rows have disjoint twin pairs and its two degree-four rows are full; every column on the opposite side has degree three. Thus each physical pair system is exactly

* **T:** four lines of multiplicity three and six of multiplicity two; or
* **F:** two lines of multiplicity four and eight of multiplicity two.

Complementary systems are T/T, F/T or T/F, never F/F. In an F/T cut, the two F rows are full on the same four T-high columns, and the other two rows of that 4-by-4 component are degree-two rows whose disjoint two-element supports partition those columns. In a T/T cut, X has two separate high 2-by-2 rectangles; Y has the 4-by-4 high block with one zero in every row and column. These statements refer to the actual component of the actual flattening, not independently chosen masks.

## 3. Six-word binary slice and complex phases

Suppose `d_i(x)=2,h_i(x)=2`. Its six distinct E words occupy six vertices of its actual binary 3-cube. The missing pair cannot have Hamming distance one: summing `|U|²` over the remaining coordinate gives a 2-by-2 nonnegative table whose row and column sums are all one, so one zero cell forces the opposite cell to be zero as well, while distance-one deletion empties only one cell.

Nor can the missing pair have distance three. Relabel the missing vertices 000 and 111, and put nonzero entries `a,b,c,d,e,f` at 001,010,011,100,101,110. Actual row orthogonality in the three directions gives

```
 a·conj(e) = −b·conj(f),
 a·conj(c) = −d·conj(f),
 b·conj(c) = −d·conj(e).                                              (4)
```

Multiplying the first and third equations and dividing by the second yields `b·conj(e)=−b·conj(e)`, impossible for nonzero entries over C. Hence the missing vertices have distance exactly two. In the one coordinate on which they agree, the two line multiplicities are 4 and 2; in each other coordinate they are 3 and 3. In particular a degree-two/surplus-two symbol has **exactly one F incident pair system**, and its other two incident systems are T.

We also use the following direct binary-box obstruction. If two actual symbols are selected at each party and, in each balanced cut, all four selected rows are supported on the four selected columns, the common 16-entry subtensor divided by two would be a normalized pure four-qubit state with all two-party marginals `I/4`. Let `A_r` be the sum of squared Pauli expectations of weight r. The two-body marginals give `A_1=A_2=0`; purity `1/2` of each complementary three-party marginal gives `A_3=12`; global purity gives `A_4=3`. The spin-flipped density is positive, but

```
 tr(ρ Y^⊗4 conjugate(ρ) Y^⊗4)=(1−A_3+A_4)/16=−1/2,                 (5)
```

contradicting nonnegativity of the trace of a product of positive semidefinite matrices. This uses the *same* subtensor in all three cuts, not equal moduli, real phases, or a separately realizable mask.

## 4. Every surplus partition, including degree-three/four concentration

The positive partitions of total surplus four are `4`, `3+1`, `2+2`, `2+1+1`, `1+1+1+1`. The last is impossible by (2), since at most two degrees can be at least three. For `2+1+1`, the two surplus-one symbols must be the two degree-three symbols and the surplus-two symbol must have degree two. Because an F system contributes even excess at each endpoint, any party with an odd surplus entry has all three incident systems T. This contradicts the one-F consequence of §3.

For `3+1`, every incident system is again T. The surplus-three symbol must meet three **distinct** positive-surplus symbols at each opposite party, since each T line contributes only one excess. The only surplus partitions with at least three positive parts are the two just excluded. Hence only `4` and `2+2` remain.

It remains essential not to assume the surplus-four symbol has degree two. Suppose party A has `h_A(a)=4`, with arbitrary allowed `d_A(a)`. A T system at A would put its four multiplicity-three lines at `(a,b)` with four distinct opposite symbols b, forcing all four opposite surpluses positive. That is impossible. Hence AB, AC and AD are F. Another surplus-four party cannot be F-adjacent to A: both multiplicity-four values would need the same unique surplus-positive endpoint at each side, producing the same pair value twice. Thus B,C,D each have partition `2+2`. Write their two surplus-two symbols as `H_B,H_C,H_D`, and call them high; their other symbols are low.

The AB F rows are `(a,b)` for both `b∈H_B`; its complementary CD side is T and its four high lines are `H_C×H_D`. The F/T full-row interface gives all eight actual words

```
                  {a} × H_B × H_C × H_D.                              (6)
```

The same conclusion holds in each cut. Each high/high pair among B,C,D has multiplicity three, so, after its two occurrences in (6), it has exactly one extension outside A=a.

**No outside-a word is high in all B,C,D.** Let such a word have A symbol p. All other A surpluses are zero, so every actual `(p,b)` E line has exactly two words. Compare this line against `(a,b)`: the first word overlaps the full high CD row, and orthogonality forces its unique mate to overlap it too. Doing this at its B, C and D coordinates gives three distinct mates: if two mates coincided, they and the starting word would give two outside-a extensions of one high/high pair. On the binary triple they are the three two-bit flips, so the four triples form a parity class, with each pair agreeing in exactly one coordinate. Set `z_t=U_(a,t)·conj(U_(p,t))`, all nonzero. At the shared coordinate the actual two-overlap orthogonality equation is `z_t+z_t'=0`. A triangle of these equations implies a nonzero z equals its own negative, impossible over C.

Thus every high/high BC pair has its one outside-a extension low at D, and analogously for the other pairs. Every high B symbol has both high D neighbors from (6) and at least one low D neighbor; similarly at every other party. Both highs at each of B,C,D have degree at least three, so (1) forces their degrees to be three and both low degrees to be two. In the BC high 2-by-2 square, let `λ_b` be high b's unique low D neighbor and `μ_c` high c's unique low D neighbor. The outside-a extension of `(b,c)` forces `λ_b=μ_c`; all four equal a single low D symbol `ℓ_D`. Likewise the extra extensions of the CD high square force a single low B symbol `ℓ_B` adjacent to both high D symbols. The other low D symbol cannot meet either high B, because their only low D neighbor is `ℓ_D`; it cannot meet `ℓ_B`, whose degree two is already exhausted by the two high D neighbors. It has at most the other low B as neighbor, contradicting degree two. This rules out surplus four even when its A degree is three or four.

Therefore every party has exactly two surplus-two high symbols and two surplus-zero lows. In a T pair system the four excess-one edges are necessarily the complete `H_i×H_j` square. In an F system the two excess-two edges form a matching between the high sets. These conclusions exhaust all surplus and degree branches; no extra partition has been assumed away.

## 5. Two F edges cannot occur

Complementary F edges are impossible by §2, so two F edges would meet. Suppose AB and AC are F. Their actual full-row components contain eight all-high words each. Relabel each high alphabet so that the matched pairs are `a=b` and `a=c`. For fixed high `(a,d)` their union contains exactly three words: the assignments with `b=a` or `c=a`. Thus all four high AD pairs have multiplicity at least three, forcing AD to be T. The complements BD and CD of AC and AB are T. **No assignment to BC is needed here**: it may be T or F until the following contradiction.

For fixed high d, the union has six words and has already supplied three occurrences at each high pair `(d,a)`, `(d,b)` and `(d,c)`; each is a T line of multiplicity three. Since all three D-incident systems are T, §3 excludes degree two for either surplus-two D symbol. The degree sum (1) makes both high D degrees three. Its eight-word E slice therefore needs two further words. None may have high A, B, or C, since the respective high pair lines are saturated. Yet d already meets both high symbols at each of A,B,C and, having degree three, has only one low neighbor in each. There is at most one distinct all-low triple. Contradiction. Hence there is **at most one** F edge.

## 6. Exactly one F edge: every sparse-row arrangement

Assume AB is the only F edge. Label its full F rows `(a_0,b_0),(a_1,b_1)`; the other two rows in the 12-entry component are `r,r'`. The complementary high columns are the four pairs of binary high C,D symbols, and `r,r'` partition those columns into two two-element supports. Both high symbols at each of C and D have degree three: all incident systems are T, so §3 rules out degree two, and (1) forces equality.

The partition into two supports is either an axis partition or the two complementary diagonals. An axis partition is impossible. For example, if each support fixes C and varies D, a sparse row containing high A would add two words to a high AC line already supplied two by its full F row, exceeding the T multiplicity three; the same holds for high B. Both sparse rows would be low/low. Each high D sees both rows and already has the two high A and two high B neighbors. Since its degree is three, the two low A coordinates must agree and the two low B coordinates must agree, so the rows are identical. The other axis is symmetric. Therefore the supports are complementary diagonals, each containing one entry at each high C and each high D.

Two sparse rows cannot share a high A symbol, or a high B symbol: each high C would then give two sparse occurrences in addition to the two full-row occurrences on a multiplicity-three high line. If both sparse rows have low A coordinates, those coordinates agree, because a high C sees both high A symbols and has degree three; similarly for low B. Classify a sparse AB row as follows, where `α,α'` and `β,β'` denote low A and B symbols:

```
 X = high/high, necessarily off the F matching;
 Y = high A/low B;   Z = low A/high B;   W = low/low.
```

The following is the complete unordered-pair analysis. Each claimed singleton overlap is between actual rows of a balanced flattening. The full-row core guarantees that a row containing one of the selected high pairs has *no unlisted high-CD entry* beyond those exhibited.

1. **W/W:** both low coordinates agree, so the rows coincide.
2. **Y/Y:** the high A symbols differ and the low B coordinate is the same β. For the two complementary diagonals choose c,c' so that their sparse entries have the same high D value d. The AC rows `(a_0,c)` and `(a_1,c')` have full-row entries at B=`b_0` and B=`b_1` respectively and one sparse entry each at `(β,d)`. Their unique common entry is `(β,d)`. **Z/Z** is symmetric.
3. **X/X:** both off-matching high/high rows occur. For each high a,c, the full row contributes two entries and its X row one, exhausting the T multiplicity three; the same is true for each high a,d. Together with the four AB high rows, the same binary box is closed in all three cuts, contradicting (5).
4. **X/Y:** sharing high A is already impossible. Otherwise relabel as `(a_0,b_1),(a_1,β)`. An AC row at `a_0` has two full entries with B=`b_0` and one sparse entry with B=`b_1`; a row at `a_1` has both high-D entries with B=`b_1` and one with B=`β`. Their unique overlap is the X-row entry with B=`b_1`. Both high AC lines are saturated at three. **X/Z** is symmetric.
5. **Y/W:** the low B coordinates agree, giving `(a_0,β),(α,β)`. For high c, the `(β,c)` BC row has exactly the two sparse high-D entries, since β has surplus zero. Compare it with a high `(b_0,c')` row. The latter has both high-D entries at A=`a_0`; its third entry must have low D, since neither sparse AB row uses b_0 and all high-CD entries lie in the displayed core. Exactly one entry overlaps. **Z/W** is symmetric.
6. **Y/Z:** if their high symbols are matched, relabel the rows `(a_0,β),(α,b_0)`. Compare `(a_0,c)` with `(α,c')` in AC. The former has the two full `(b_0,d)` entries and one `(β,d)` sparse entry. The latter has its one sparse `(b_0,d)` entry and, since α has surplus zero and no other sparse AB row uses it, its only other entry has low D. The overlap is exactly one. If their high symbols are crossed, this particular singleton argument does not apply.

Up to interchanging the matched labels, the only residual row pairs are consequently

```
 I:  (a_0,b_1), (α,β);           II:  (a_0,β), (α,b_1).              (7)
```

These are residual cases of the preceding argument, not claimed unitary realizations.

### 6a. Actual degrees in both residual cases

In either (7), α and β occur in exactly one sparse row, which contains one word at each high C and each high D. If `d_A(α)=2`, both C-neighbors and both D-neighbors would be high, and all its `s_A(α)=4` words would have high C,D. The actual F/T component contains exactly two such words at α, contradiction. Thus `d_A(α)≥3`; similarly `d_B(β)≥3`.

The high `a_1` appears in no sparse row. Its full F row contributes four words and uses both high C and both high D symbols. If it had degree two, all its `s_A(a_1)=6` words would have high C,D, but the component has only those four. Hence `d_A(a_1)≥3`; similarly `d_B(b_0)≥3`. Since all degrees are at least two and sum to ten, the exact assignments, including the previously unnamed low neighbors, are forced:

```
 A: d(a_0), d(a_1), d(α), d(α') = 2,3,3,2;
 B: d(b_0), d(b_1), d(β), d(β') = 3,2,3,2.                         (8)
```

### 6b. Four distinct contexts and the matching contradiction

Fix high c at C. Its degree-three, surplus-two slice has eight words. The two high D lines are T lines of multiplicity three, hence contain six words; its only low D neighbor accounts for the remaining two. The full rows contribute two of the six at each of `a_0,a_1` and at each of `b_0,b_1`. Either residual pair (7) contributes one further at each of `a_0,α,b_1,β`. Thus the two low-D words must use A symbols `a_1,α` once each and B symbols `b_0,β` once each. Their AB pairs are exactly one of the two matchings

```
 M_0={(a_1,b_0),(α,β)},       M_1={(a_1,β),(α,b_0)}.                 (9)
```

The same argument, interchanging C and D, applies at each high D symbol. These give four distinct contexts: two high-C/low-D and two low-C/high-D contexts. They cannot refer to the same word. Every AB pair in (9), once present, is non-F and therefore has E multiplicity exactly two.

In case I, `(α,β)` is the W sparse row and already has its two high-CD words. Thus no context can use `M_0`; all four would use `M_1`, giving four distinct E words on `(a_1,β)`, a contradiction.

In case II, each of `M_0,M_1` can occur in at most two contexts by the multiplicity-two bound, and all four contexts must choose one. Hence each occurs exactly twice. In particular all four AB pairs in (9) occur. Now `b_0` has A neighbors `a_0,a_1,α`; β has `a_0,a_1,α`; and `b_1` has `a_1,α`. These exhaust their degrees in (8). The remaining A symbol `α'` can meet only `β'`, contradicting its degree two. Both residual sparse-row cases are impossible. There is therefore **no F pair system**.

Since each high has surplus two, §3 now forbids degree two at every high. Equation (1) forces both highs at every party to have degree three and both lows degree two. Every pair is T and its four multiplicity-three lines are exactly its complete high/high square. This proves the stated necessary conclusion, and stops before the all-T component synchronization or parity analysis.

## 7. Explicit gap and import accounting

The detailed reconstruction identifies no unresolved gap in the displayed §§1–4 implication to F-free surplus/degree data. In particular it supplies the assignments often omitted in compressed summaries: BC need not be assigned in the two-F argument; in the single-F cases the sparse supports must be diagonal, each possible unordered X/Y/Z/W pair is accounted for, the third high `(b_0,c')` entry in Y/W is at **low D** because of actual core membership, and the four matching contexts are disjoint. The two remaining cases (7) are not silently dropped. This is my author analysis, not a claim that an independent reviewer has cleared it.

The unprovided linked source bodies and historical computations in the packet are not premises. The actual-unitary component lemma is written out in §2, and the binary-box obstruction is written out in §3. If either displayed derivation is not accepted, the conclusion is conditional on that explicitly named interface/obstruction, not on an unspecified theorem. The f861 erratum was read first; its `b_i` symbol versus `v_i` triple-count correction applies to f861, which is nonblind context, not an adopted theorem. Neither f861's residual feasibility nor the parent dispositions supplies an additional premise here. Nothing above establishes the subsequent all-T contradiction, a family/human/formal verdict, publication priority, or a global AME theorem.

## 8. Complete read and process declaration

Before any packet-body reading or task mathematical reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent-live metadata supply, actual dispatch receipt, and all 22 listed status/permission controls, then wrote `prebody-ack-v1.md` and sent a direct prebody ACK to Main. Initial non-raw administrative displays elided JSON blocks; complete raw rereads recovered those blocks before the ACKs. Controls were not mathematical inputs. The owned-directory listing showed both candidate and prebody output names absent before writing; the write interface did not expose an atomic exclusive-create flag, so no stronger OS-level exclusivity is claimed.

After both acknowledgments I read the sole packet part serially in raw windows `1–20, 21–40, …, 401–420, 421–434`, including its ending; every display was below 30,000 bytes and no packet clipping was observed. The rendered bodies were S1 original LF 1–3, S2 LF 1–182, S3 LF 1–172, S4 LF 1–22, and S5 LF 1–33, all complete and in that order. The parent-supplied packet SHA-256 is `7628f3d1d1bb7ee9a8c0d8d30c79c817701c10be2f32fcc8d3fbfc9c34e85dc1`; exact original paths and source pins are in the frozen manifest. Administrative bindings are not independently recomputed hashes, source-identity certification, mathematical verification, or cognition certificates.

No links, held episode or held proof/method/planning/selection/verification/reporting/confidence/downstream consumer was opened or used. No peer science was requested or read. No network, external model, scientific execution/evaluation, test, solver, compilation, child subprocess, build, lint, formatter, Git or deletion was used. No verifier was prepared, so there is no prepared code hash or computational verification. Apart from the recovered administrative display elisions and the atomic-create limitation disclosed above, no process deviation is known. Any correction must be a new additive file, not an edit of this candidate.
