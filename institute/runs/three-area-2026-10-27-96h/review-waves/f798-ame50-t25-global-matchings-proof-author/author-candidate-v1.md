# N=50, t=25: proposed same-complex-tensor exclusion

**Status: NONBLIND GENERAL AUTHOR reconstruction, not a parent disposition or independently reviewed result.** The exact claim is that there is no normalized complex AME(4,6) tensor in any one local orthonormal product basis whose support has exactly 50 entries and whose scaled tensor `U=6ψ` has exactly 25 entries of modulus one. Every support and multiplicity below refers to that **same U** in all three balanced cuts and all six physical pair systems. Amplitudes are arbitrary nonzero complex numbers; no equal-modulus residual, phase, classical-array, or independent-cut assumption is made.

This is a proposed complete written proof of this **one** exact branch. It does not use a global t bound, no-OLS, a historical computer-assisted count, or a claimed global witness. It neither excludes support 50 at other t nor proves a new minimum, existence, novelty, or priority. The first independent full read, mathematical scrutiny, and disposition remain the parent's. I identify no omitted case in the argument below; that is an author assessment, not an independent verification.

## 1. Actual unitarity and the excess-three block

AME makes each of the three two-versus-two flattenings of `U` a 36×36 unitary. Let `P` be its 25 entries of modulus one, and `E` its other 25 nonzero entries. A modulus-one entry exhausts its row and column in every cut. Thus no other nonzero shares any of its six physical pair values, and P is injective on every pair projection. In a cut, delete its 25 P rows and 25 P columns. The remaining 11×11 matrix is unitary, with exactly 25 nonzero E entries. It has no degree-one row or column: its sole entry would have modulus one and would instead be in P. Consequently, in each physical pair system, a pair value is either a singleton P value or an E value with at least two E extensions; there are exactly 11 E values.

We derive the needed component restriction directly, including arbitrary complex phases. A connected bipartite support component of the residual matrix is square: its block has orthonormal rows and orthonormal columns, giving both inequalities between its row and column counts. Two rows or two columns cannot have exactly one common nonzero position, since their inner product there would be a single nonzero complex term.

For a component of order `m` define its excess `e_c=edges−2m`. Every line has degree at least two, so `e_c≥0`, and the total excess is `25−2·11=3`. An order-two component is a full 2×2 block. If `m>2`, each degree-two row has two columns with identical row neighborhoods: every other row meets either both or neither. Their common degree is at least three, since degree two would isolate a 2×2 unitary block. Distinct degree-two rows have disjoint column pairs: one common position is forbidden, while sharing both columns makes those two rows a 2×2 unitary and isolates that block. There are at least `m−e_c` degree-two rows and at most `e_c` columns of degree at least three. Hence

`m ≤ e_c + floor(e_c/2)` for every component of order greater than two.                         (1)

This rules out positive excess one and rules out a component of order greater than two with excess zero. A positive excess-three component has order at most four. If its order were four, it would have at least one degree-two row and at most one, because two disjoint twin pairs would require four high columns but there are at most three. Its other three rows therefore all have degree three. The twin columns are both high; each has degree exactly three because the whole column excess is three. They meet the degree-two row and the same two of the other three rows. The remaining degree-three row avoids both twins and has at most the other two columns available, a contradiction. The excess-three component therefore has order three, and its nine edges fill the 3×3 block.

Since excess one is impossible, the entire excess three cannot split into positive components. Thus **each cut consists of one full 3×3 component and four full 2×2 components**. In each physical pair system exactly three E values have multiplicity three; call them high pair values. The other eight E values have multiplicity two. In a given cut, its three high rows and three high columns form the complete 3×3 block. In particular, for every actual E word, its value in one pair is high if and only if its value in the complementary pair is high; and **all nine high-row/high-column combinations are actual E words** of U.

## 2. Common incidence degrees and a five-cube obstruction

For a symbol `x` appearing in E at party `i`, write `d_i(x)` for its number of distinct E partners at any one other party and `s_i(x)` for its number of E occurrences. This degree is the same for all three partner parties: `6−d_i(x)` is the number of P words containing x, because every pair cell is either a singleton P value or an E value and P is pair-injective. Put `h_i(x)=s_i(x)−2d_i(x)`. For every partner, `h_i(x)` counts the high pair values incident to x. Consequently

`d_i(x)≥2,    Σ_x d_i(x)=11,    h_i(x)≥0,    Σ_x h_i(x)=3`.                          (2)

Indeed, degree one would fix the x-word's symbol at all three other parties, allowing at most one distinct E word, contrary to the minimum E pair multiplicity two.

We also need `h_i(x)=1 ⇒ d_i(x)≥3`. If instead `d=2,h=1`, the five words containing x lie in a binary 3-cube, with two allowed symbols at each other party. In each direction their two actual pair rows have sizes two and three among the four possible complementary pairs. These two supports meet, and row orthogonality prevents exactly one common position, so there are at least two retained cube edges in each of the three directions, at least six in total. But the three omitted vertices induce at most two edges in the bipartite cube; deleting them removes at least `3·3−2=7` of its 12 edges. The five retained vertices induce at most five edges. This contradiction proves

`h_i(x)=1 ⇒ d_i(x)≥3`.                                                                  (3)

## 3. Excluding concentrated excess using the same U

At each party the positive `h` values must partition three as `(3)`, `(2,1)`, or `(1,1,1)`. We exclude the first two, using complete 3×3 blocks of different cuts of the same tensor.

**A single `h=3`.** Suppose A has symbol a with `h_A(a)=3`. All three high AB values contain a, and their B symbols are distinct. Since `Σ h_B=3`, B has exactly three high symbols, each with h=1. The same holds for C and D; in particular the high CD values form a matching `(c_j,d_j)`, `j=1,2,3`, between their three high symbols. Write the high AB values `(a,b_i)`, `i=1,2,3`. The full AB|CD block contains all nine actual words `(a,b_i,c_j,d_j)`. In the AC|BD cut, all three rows `(a,c_j)` are high. Their BD-neighbor sets include the disjoint three-element sets `{(b_i,d_j): i=1,2,3}`. But the full 3×3 AC|BD block requires every high AC row to have the same three BD neighbors. Contradiction. Thus no party has `(3)`.

**Two parties of type `(2,1)`.** Suppose A and C have h=2 symbols a and c. Their three distinct high AC edges have endpoint-degree sequences `(2,1)` on both sides, so the edge `(a,c)` must occur: otherwise a would need two neighbors among the single other high C symbol. Let B,D be the remaining parties. There are two high AB values `(a,b_1),(a,b_2)` and two high CD values `(c,d_1),(c,d_2)`. The full AB|CD block contains the four distinct words `(a,b_i,c,d_j)`, `i,j∈{1,2}`. All share the high AC value `(a,c)`, whose actual multiplicity is only three. Contradiction.

**One party of type `(2,1)`.** If A alone had this type, each of B,C,D would be `(1,1,1)`, since `(3)` and a second `(2,1)` are impossible. Let a be A's h=2 symbol. Its two high AB values are `(a,b_1),(a,b_2)` and its two high AC values are `(a,c_1),(a,c_2)`. The high CD matching sends `c_j` to distinct `d_j` for j=1,2. The AB|CD block contains `(a,b_i,c_j,d_j)` for all i,j=1,2. Therefore the high AC rows `(a,c_1),(a,c_2)` have at least four distinct BD neighbors jointly, although the AC|BD full block says they share one three-element neighbor set. Contradiction.

Every party consequently has three h=1 **high symbols**, and every other E-used symbol is low with h=0. A high pair value has one high endpoint in each of its parties, and the three such values form a perfect matching between the two three-symbol high sets.

## 4. Actual P moments force alphabet 4444

Let `q_i` be the number of E-used symbols at party i. By (2)–(3), the three high symbols have degree at least three and any additional symbol has degree at least two. Hence `3≤q_i≤4`. Two size-three alphabets cannot coexist, because their pair has 11 distinct E values but only nine possible cells. Therefore the only profiles, up to party permutation, are 3444 and 4444.

The same actual P set rules out 3444. Let `n_k` be the number of P words with exactly k coordinates in their parties' E alphabets. In party i, each E-alphabet symbol has `6−d_i(x)` P occurrences, so the total is `6q_i−11`. In parties i,j, among the `q_i q_j` cells with both coordinates in the E alphabets, exactly 11 are E cells and all others are singleton P cells. Therefore

```
Σ n_k                 = 25,
Σ k n_k               = 6 Σ_i q_i − 44,
Σ binom(k,2) n_k      = Σ_{i<j} q_i q_j − 66,
n_0 + n_3 + 3 n_4    = 25 − Σ k n_k + Σ binom(k,2)n_k.
```

For 3444 these last two moments are `46` and `18`, making the nonnegative left side `25−46+18=−3`. Thus every `q_i=4`. For 4444 the same moments are 52 and 30, and the corresponding left side is 3; this is a necessary P constraint, not a construction. Equation (2) now forces the three high degrees to be exactly 3 and the sole low degree exactly 2 in every party. Therefore every high symbol has `s=2·3+1=7` E occurrences, and the unique low symbol has `s=2·2=4`.

## 5. Cross-cut matching consistency

Use local relabeling of the three high symbols at each party so that the high matchings AB, AC and AD are equality on `{0,1,2}`. Denote the other high matchings by bijections `β:B→C`, `γ:B→D`, and `δ:C→D`. Because all nine high AB/CD combinations are actual words, E contains

`(x,x,y,δ(y))` for all `x,y∈{0,1,2}`.                                               (4)

For these words, high AC iff high BD says `x=y` iff `δ(y)=γ(x)`, giving `δ=γ`. High AD iff high BC says `x=δ(y)` iff `y=β(x)`, giving `β=δ⁻¹`. The complete high AC/BD block also contains `(x,y,x,γ(y))` for every x,y. On these words high AD iff high BC says `x=γ(y)` iff `x=β(y)`, giving `γ=β`. Consequently `β=γ=δ=π`, where `π²=id`. A permutation of three labels with square identity is either the identity or one transposition, up to a simultaneous relabeling.

Writing A,B,C,D in that order, the three complete high blocks are the actual nine-word sets

```
X_AB = {(a,a,c,π(c)) : a,c∈{0,1,2}},
X_AC = {(a,b,a,π(b)) : a,b∈{0,1,2}},
X_AD = {(a,b,π(b),a) : a,b∈{0,1,2}}.                                                (5)
```

They are sets of words of the same E, not three independently specified supports. Their pairwise intersections are respectively

```
X_AB ∩ X_AC = {(a,a,a,π(a))},
X_AB ∩ X_AD = {(a,a,π(a),a)},
X_AC ∩ X_AD = {(a,π(a),a,a)}.                                                           (6)
```

Each has three words. Their triple intersection is exactly `{(a,a,a,a): π(a)=a}`. Every high label at every party occurs three times in each set of (5), once in each pairwise intersection, and once in the triple intersection exactly when its label is fixed by π. Thus it has

`6 + 1_{π(label)=label}` occurrences in the union `X=X_AB∪X_AC∪X_AD`.                (7)

All counts here are counts of distinct actual tensor support words; the formulas include the π-permutation of the relevant label in (6).

## 6. Both permutation classes and actual low-cell multiplicities

**Identity.** There are three triple-intersection words, so `|X|=27−9+3=21`. Equation (7) gives seven occurrences in X for each high symbol, exhausting its total s=7. The four remaining E words must use the unique low symbol at all four parties. Only one quadruple has those coordinates, contradicting distinct support words.

**A transposition.** Relabel so that `π` swaps 0 and 1 and fixes 2. Now `|X|=27−9+1=19`. Every fixed high symbol 2 has all seven occurrences in X; every high symbol 0 or 1 has six in X and therefore exactly one E occurrence outside X. There are six outside words.

The following are actual low **E** pair values, not merely cells assumed to be available. Their unique occurrences in X, obtained directly from (5), are

| Pair value | Unique word in X |
|---|---|
| `(A0,B1)` | `(0,1,0,0)` |
| `(A0,C1)` | `(0,0,1,0)` |
| `(A0,D1)` | `(0,0,0,1)` |

Each pair value is non-high because the A-to-other high matching is equality; since its displayed word exists, it is an E pair value, and by Section 1 its total actual E multiplicity is exactly two. Each therefore needs one more occurrence outside X. A0 has only one such occurrence, so all three missing extensions must be the single actual word `(0,1,1,1)`. By interchanging 0 and 1, the only remaining occurrence of A1 is `(1,0,0,0)`.

Those two distinct words use and exhaust the one outside-X occurrence of each of labels 0 and 1 at **every** party. All occurrences of label 2 were already exhausted in X. The other four outside-X E words would therefore have to use the unique low symbol at all four parties; only one such word exists. This contradiction excludes the transposition as well. The two involution classes exhaust the matching possibilities, proving the proposed exact N=50,t=25 exclusion, subject to independent scrutiny.

## 7. Coverage and verification boundary

After Main's direct notice that the actual dispatch receipt had been finalized, I read the complete dispatch receipt, 246-LF manifest, 227-LF freeze receipt, 199-LF final binding, 240-LF prepared metadata, and all 22 manifest-listed controls through their endings. Controls were used for status/permissions only. I sent Main a direct PREBODY ACK naming those controls and the ordered parts before reading any packet body. I then read part 01 serially, raw, LF 1–433 in consecutive windows of at most 20 LF, followed by part 02 serially, raw, LF 1–138 in consecutive windows of at most 20 LF, including their endings and long lines, before mathematical work or comparison. This covers all six declared complete bodies: S1 1–161, S2 1–29, S3 1–29, S4 1–31, S5 1–161, S6 1–132. I did not open the outgoing source paths.

Parent-declared source pins, not independently rehashed by this child: S1 `3752d4b981b70d4626dbda6a87644044332ffd2e431a624f753fcccf9257d4f9`; S2 `ccbadbf970b31c199b08f8adeeca03e489f345052d204b31a6192af69aa1e6f0`; S3 `ceadc652cbdcfc957d9ca64ab97cd6e0e8c7faa0826356dc03de8d60f093957a`; S4 `69f2bff74957951086b6481b2c553e6ab2d2c59f6ea2fd7d369c4c4acefaf8b0`; S5 `ac4f6284549678e0e0430242baed238230680b74a0f1facbd8e8e1cd99691181`; S6 `c852a533a2e26cd2b7bcf37f38827c63511544d7b5d1a9e98b5454ac7b7f2b3a`. The parent freeze/binding reports literal roundtrip and matching hashes; that is not this child's independent source-identity verification. The parent-supplied packet pins are part 01 `3fa85011e561ba4636b2bf957258792ac51f4ebbc549d323b0c7bb8e6426b425` and part 02 `10f367294d61b46e5d746b2b3bfabab782803d2e506f69609b4b6c39cd58402a`.

One initial administrative manifest read mistyped the home path and returned not found with no bytes; I promptly disclosed it to Main, then completed the correct manifest read before the PREBODY ACK. Main confirmed that this empty path error alone is not a process violation. No prior body access was claimed. This is a nonblind reconstruction of the supplied candidate and associated complete packet, not a claim of cognitive isolation. All genuine held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remain NONINPUT.

No scientific code or new source was prepared, run, imported or compiled. No solver, test, build, linter, formatter, external CLI, network, Git, install, deletion, old code, unlisted scientific source, sibling return, or outgoing source link was used. No human, model-family, formal/kernel, global enumeration, phase-realizability, or parent-adoption result is asserted. The exact proof needs a separate independent full review and parent disposition; global and other-t questions remain outside this artifact.
