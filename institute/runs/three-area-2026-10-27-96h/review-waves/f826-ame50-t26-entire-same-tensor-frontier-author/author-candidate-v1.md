# Actual N50/t26: common-tensor alphabet and phase obstructions

**Status: prospective GENERAL AUTHOR candidate, NONBLIND, same harness; parent disposition and independent review remain separate.** For one normalized complex AME(4,6) tensor in one fixed local orthonormal product basis, with support `N=50` and exactly `t=26` entries of `U=6ψ` of modulus one, I propose the following **necessary** restrictions, each using the SAME tensor and permitting arbitrary complex amplitudes and phases.

1. If `q_i` is the size of the E alphabet at party `i`, its sorted profile is **one of `3445`, `4444`, `4445`**. In particular no party has `q=2`, two parties cannot both have `q=3`, two cannot both have `q=5`, and `3444` is impossible.
2. If a party has `q=5`, all five of its E-degrees are two and its surplus vector is necessarily `(2,2,0,0,0)`, up to relabeling. Thus its two high symbols each occur six times. In each high-symbol binary three-cube the two missing vertices differ in **two or three coordinates**, and the set of coordinates in which they agree is identical for the two high symbols. Distance one is excluded, including with non-real phases.
3. Section 7 gives an exact residual criterion with one physical `P`, one physical `E`, a common positive amplitude per E word, a common phase per E word, all six pair systems, and all three actual cut masks. It includes an explicit integer-kernel obstruction for ALL two-term orthogonality equations and retains the coupled three-/four-term equations. It is not asserted to be solved.

No t26 witness or complete t26 exclusion is claimed. In particular none of this proves `N≥51`, an exact minimum, a global t bound, no-OLS, source identity, novelty, or publication priority. A 4-qubit contradiction used below is proved here and is not a claim about an independent cut witness.

## 1. Actual object and low-excess interface

Write the four parties as `A,B,C,D`, each with its actual six-symbol alphabet. `P` consists of the 26 nonzero entries of `U` of modulus one; `E` consists of its other 24 nonzeros. Every pair projection of `P` is injective and disjoint from the E pair values. Each of the six physical pair systems has exactly 26 singleton P values and ten E values; an E value has at least two E extensions. This follows because every 2-versus-2 flattening is a 36-by-36 unitary, and a modulus-one entry exhausts both its row and column. Pair values outside an E alphabet are still physical values and must be supplied by the SAME P set.

For an E-used symbol `x` at party `i`, let `d_i(x)` be the number of E partner symbols at any one other party, `s_i(x)` its E-word occurrence count, and `h_i(x)=s_i(x)-2d_i(x)`. The degree is independent of the partner: the number of P words containing `x` is `6-d_i(x)`. Thus, for each party,

    d_i(x) ≥ 2,       Σ_x d_i(x)=10,       h_i(x) ≥ 0,       Σ_x h_i(x)=4.       (1)

For `d=1`, all three other coordinates would be fixed and at most one E word could contain `x`, contrary to its E pair line having at least two entries. Consequently `q_i≤5`. Also `h=1` forces `d≥3`: if `d=2`, the five words of the slice are five vertices of a binary three-cube. In each of its three directions the size-2 and size-3 actual row supports must meet in at least two positions, because one-overlap is forbidden; hence the five vertices induce at least six cube edges. But three deleted cube vertices induce at most two edges and remove at least seven of the twelve, leaving at most five. This proves the assertion for arbitrary coefficients, not just support graphs.

We use the low-excess conclusion explicitly present, with written supporting arguments, in packet S1, S5 and S6: after deleting `P`, every cut has `n=10`, 24 edges, excess four, and is either two `3×3`-minus-one components plus two full `2×2` components, or one connected order-four, 12-entry component plus three full `2×2` components. A support component of a genuine unitary is square; two rows or columns cannot meet in exactly one nonzero. In a connected component of order above two, the neighbors of a degree-two row are twin columns of degree at least three, and different degree-two rows have disjoint twin pairs. If two such rows had the same pair, their two orthonormal rows would exhaust those columns and isolate a 2-by-2 block. The transposed statements also hold.

For later use, the degree pattern of a 12-entry order-four component is as follows. On a side it is either `3333` or `2244`; a `2334` side is impossible. Indeed a degree-two row has twins. If their degree is three, the degree-four row meets them and one degree-three row avoids them, leaving that row only two columns. If their degree is four, the two degree-three rows use distinct remaining columns, otherwise one remaining column has degree one; the two remaining columns then overlap only in the degree-four row. If a side is `2244`, its two low rows have disjoint pairs and the two other rows are full, so the opposite side is `3333`. Thus every physical pair system has either four E values of multiplicity three or two E values of multiplicity four, all other E values having multiplicity two. This also proves that in a component containing degree-four rows there are exactly two, with the same four opposite neighbors, and the opposite degrees are all three.

## 2. A self-contained obstruction to an isolated binary four-party block

**Lemma.** There is no normalized pure four-qubit state whose every two-qubit marginal is `I_4/4`.

Let `a_P=tr(ρP)` for the tensor-product Pauli matrices, and let `A_r` be the sum of `a_P²` over the Pauli strings of weight `r`. Pairwise maximal mixing gives `A_1=A_2=0` and `A_0=1`. For any three parties, complementary Schmidt spectra give purity `1/2`, since the remaining one-qubit marginal is `I_2/2`. The three-party Pauli expansion therefore gives `1/8(1+Σ_{weight 3 on this triple}a_P²)=1/2`, so that sum is three. Summing over the four triples yields `A_3=12`. Purity of the four-qubit state gives `Σ_r A_r=16`, hence `A_4=3`.

The spin-flipped density `\widetildeρ=Y^{⊗4}\overlineρY^{⊗4}` is positive and maps a Pauli string of weight `r` to `(-1)^r` times that string. Therefore

    tr(ρ \widetildeρ) = (1 - A_3 + A_4)/16 = -1/2,

contradicting positivity. No external nonexistence theorem or phase restriction is used.

In applications, it suffices to find two symbols at each party such that, in every actual cut, the four rows with the two chosen symbols on one side have all their support in the four chosen opposite pair values. Those four globally orthonormal rows form a 4-by-4 unitary, whose columns are exhausted. The SAME 16-entry subtensor divided by two is then the forbidden normalized four-qubit state. It is important that all three cuts and all the same entries are used.

## 3. A modulus-eight slice cannot meet a high-high-high word

Suppose `q_D=5` and some D symbol `x` has `h_D(x)=4`. By (1), `d_D(x)=2`, `s_D(x)=8`, and the actual slice is the complete binary cube

    E_x = {x} × H_A × H_B × H_C,       |H_A|=|H_B|=|H_C|=2.              (2)

For any other party `j`, each value in `H_j` forms with `x` an E pair of multiplicity four, so its surplus is at least two. Since the total surplus at `j` is four, those two symbols have surplus exactly two each and all other symbols at `j` have surplus zero. In the cut `Dj | kl`, the two full rows `(x,H_j)` lie in the same 12-entry order-four component. Its opposite pair values are exactly `H_k×H_l`, each of multiplicity three. Hence in each of the three systems `AB,AC,BC`, the four high-high pair values have multiplicity exactly three, with the x-cube providing two occurrences and exactly one further actual E word at each value.

**No-three-high lemma.** No E word outside `E_x` uses high symbols from all three of `H_A,H_B,H_C`.

Suppose such a word has D coordinate `x'≠x`. Since `q_D=5`, every D degree is two; `h_D(x')=0`, so its slice has exactly four words and every line `(x',j)` has two. For each of the three other parties, compare the row `(x,j)` with `(x',j)` through the given word. A singleton overlap is impossible, so the second word in the latter row also has all three coordinates high. These three mates are distinct: otherwise two outside words would share a high-high pair, which already has the two x-cube extensions and has total multiplicity three. Thus all four words of the `x'` slice are high-high-high, and each of their three pair projections is bijective. A binary set of four triples with all pair projections bijective is a parity class. Any two of its four triples agree in exactly one coordinate.

For each of those four triples `t`, put `z_t=U_(x,t) conjugate(U_(x',t))`, which is nonzero. Orthogonality of rows `(x,j)` and `(x',j)` at the one coordinate shared by a pair `t,t'` gives `z_t+z_t'=0`. The three edges of any triangle in this four-vertex agreement graph imply `z_t=0`, contradiction. This argument retains unrestricted complex phases and magnitudes.

A useful consequence is that the twelve extra incidences of the three high-high pair systems occur at twelve distinct E words, each high at exactly two of A,B,C: every high-high pair has precisely one outside-x extension, and a three-high word is impossible. The other four outside-x words have at most one high coordinate.

## 4. No two E alphabets have size five

If two parties have `q=5`, each used symbol has degree two. On either party the surplus partition is `(4)` or `(2,2)`, because a part one is forbidden by Section 1. If D has surplus `(4)` and another party `j` also has `q=5`, the two `H_j` symbols have surplus two and degree two. Their already-present x-cube neighbors at both other parties exhaust their two neighbors there. Each has six total E occurrences, four in the x-cube, so its other two words are three-high, contradicting Section 3. Thus both five-symbol parties would have surplus `(2,2)`.

Call their two high symbols `a_0,a_1` and `b_0,b_1`. The only positive-surplus pair values lie in this high-by-high square. Each row and column of its weighted excess matrix sums to two; a line contributes one for multiplicity three or two for multiplicity four. Hence, up to labels, either all four high pairs have multiplicity three, or the two diagonal high pairs have multiplicity four.

* **Four threes.** Each high `a` has six E occurrences and exactly two neighbors in each other party; similarly each high `b`. At a high pair `(a,b)`, three distinct complementary pairs must lie in the product of two two-element neighbor-set intersections. Their product has size at least three, so both intersections have size two: the two relevant neighbor sets agree. Applying this to all four high pairs gives common two-symbol alphabets `K,L` for the other parties. All twelve words with high `a` lie in `{a_0,a_1}×{b_0,b_1}×K×L`. They exhaust the six E occurrences of each high `a` and each high `b`.
* **Two fours.** The two high diagonal rows are full rows of the same order-four/12-entry component and have the same four complementary pair neighbors. The four extensions of either high pair use a `2×2` rectangle because each high symbol has degree two. Thus both high `a` symbols, and both high `b` symbols, have common neighbor alphabets `K,L`. Their four already-present occurrences per high symbol occupy eight words of the component. Each high `a` has two further occurrences and, since its K/L degrees are already exhausted, these four words all lie in the remaining four component positions. The same argument for the high `b` symbols shows that these very four words also have high `b`. Again all twelve words with high `a` lie in the same binary four-party box.

In either case, for every cut, the four rows involving a high `a` symbol have support only on the four complementary values in that box, and all four row values occur because the high `a` symbols have degree two in every partner. Their actual row orthonormality makes each of the three restrictions a 4-by-4 unitary. Section 2 is a contradiction. Therefore **at most one party has `q=5`**.

## 5. The actual P set excludes `q=2` and `3444`

If a party has `q=2`, (1) and the ten E values in each pair force every other party to have `q=5` and each `2×5` pair rectangle to be full. Each of the two used symbols then occurs in exactly `6-5=1` P word. Such a word must use the unique outside-E symbol at each of the three other parties. The two P words consequently have the same pair value at any two of those parties, contradicting injectivity of the SAME P projection. Hence `q_i≥3`. Two `q=3` parties cannot coexist because their pair rectangle has only nine cells for ten E values.

For the P moment calculation, let `n_k` be the number of P words with exactly `k` coordinates in the respective E alphabets. Since P and E pair values partition all 36 physical cells,

    Σ n_k=26,
    Σ k n_k=6 Σ_i q_i-40,
    Σ binom(k,2)n_k=Σ_{i<j}q_i q_j-60.                                  (3)

For `3444`, these give `n_0+n_3+3n_4=0`, and hence `n_0=n_3=n_4=0`, `n_2=24`, `n_1=2`. Let A have three E symbols and B,C,D four. The number of P incidences in the A E alphabet is eight. Exactly two P cells of each of AB, AC, AD lie in the corresponding E-alphabet rectangles, so six of those eight incidences are in two-inside P words. Both single-inside P words therefore have their sole inside coordinate at A.

Fix any E-used B symbol `b`, of degree `d`. Each of the three actual A-outside symbols pairs with `b` in a unique P word. Those three words cannot be single-inside and cannot have three inside coordinates, so each has B inside and **exactly one** of C,D inside. There are exactly `4-d` such P cells with C inside and exactly `4-d` with D inside. Thus `3=2(4-d)`, impossible. This is a same-P incidence contradiction, not an independent pair completion.

Combining this with Section 4 gives the three sorted profiles stated at the start. For completeness, the possible `(n_0,n_1,n_2,n_3,n_4)` forced by (3) and nonnegativity are:

| sorted q | all moment-possible P profiles |
|---|---|
| 3445 | `(0,1,20,5,0)`, `(0,0,23,2,1)` |
| 4444 | `(0,2,18,6,0)`, `(0,1,21,3,1)`, `(0,0,24,0,2)` |
| 4445 | `(0,2,12,12,0)`, `(0,1,15,9,1)`, `(0,0,18,6,2)` |

These are necessary moment profiles, not claimed realizations or a replacement for individual P cells.

## 6. The surviving five-symbol party cannot have surplus four

Assume `q_D=5` and `h_D(x)=4`, with the cube and no-three-high lemma of Section 3. By Section 5 the other sorted alphabets are either `444` or `344`. In either case every high-high pair at the other three parties has its unique outside-x extension at a **low** symbol of the third party.

### Other alphabets 444

Each high symbol at A,B,C has a high-high pair with each symbol of another high alphabet, so the unique outside extension forces at least one low neighbor in the remaining party. Its degree is at least three. Since each of the four used degrees is at least two and totals ten, both high symbols have degree three and both low symbols have degree two.

For a high symbol `a∈H_A`, let its unique low C neighbor be `f(a)`; for `b∈H_B` let its unique low C neighbor be `g(b)`. Every high `(a,b)` pair has an outside-x extension with C low, so `f(a)=g(b)` for all four choices. Consequently all high A and B symbols have the same low C neighbor `ℓ_C`. The same conclusion holds in every direction. For the pair of parties A,C, the low symbol `ℓ_C` is adjacent to both high A symbols and has degree two, so it has no low A neighbor. The other low C symbol has no high A neighbor, because each high A symbol has the unique low neighbor `ℓ_C`. It also cannot be adjacent to `ℓ_A`, which is already adjacent to both high C symbols and has degree two. It has at most the one remaining low A neighbor, contrary to degree two. Thus `4445` with surplus four is impossible.

### Other alphabets 344

Let `|A_E|=3`, `|B_E|=|C_E|=4`; write the unique low A symbol as `a_*`. The four high-high BC pair values each have an outside-x extension, necessarily with A coordinate `a_*`. Thus each high B symbol is adjacent to both high A symbols and to `a_*`, so it has degree three; the two low B symbols have degree two. The same holds for C.

For `c∈H_C`, let `f(c)` be its unique low B neighbor; for `b∈H_B`, let `g(b)` be its unique low C neighbor. Each high AC pair has its outside extension at B=`f(c)`, and each high AB pair has its outside extension at C=`g(b)`. Both maps cannot be constant: if `f` is constant at low B symbol `β`, then `β` has both high C neighbors and is degree two; the other low B symbol has no high C neighbor and must meet both low C symbols. If also `g` is constant at low C symbol `γ`, then `γ` already has both high B neighbors and degree two, a contradiction.

At least one of `f,g` is therefore bijective. Each high A symbol has the two high B and two high C neighbors from the cube, and if `f` is bijective it also has both low B neighbors; if `g` is bijective it has both low C neighbors. Hence each high A degree is four. Equation (1) gives `d_A(a_*)=2`, `h_A(a_*)=0`, so its entire E slice consists of exactly the four outside-x words at the four high BC pair values.

In the `DA | BC` component, those four BC cells are partitioned into two supports of degree-two rows `(p,a_*)`, with `p≠x`. Each `p` has four E words, exactly two at A=`a_*` and two at one high A symbol. If the two BC cells in one row are diagonal, both B and C neighbor sets of `p` are exactly the high pairs; its other two words would be three-high, impossible. If the two cells have the same B and different C, the other two words must have C high and B=`f(c)`; the two B-neighbor limit forces `f` constant. Likewise a same-C pair forces `g` constant. Therefore if both maps are bijective there is no possible partition.

It remains to exclude exactly one constant map. By symmetry suppose `f(c)=β` is constant and `g` is bijective. Every row of the `a_*` partition must pair the two cells at a fixed B value. Let its two D values be `p_b`, one for each high `b`. The other two words in the `p_b` slice have B=`β`, both high C values, and a common high A symbol `a_b`. The `a_b` are distinct: otherwise a high AC pair would have two outside-x extensions. Thus in the `DB | AC` high component, the two low rows `(p_b,β)` pair AC columns at fixed A, varying C. In the `DC | AB` high component, the two low rows have distinct low C values `g(b)` and pair AB columns at fixed B, varying A.

Write `Q_{abc}=U_(x,a,b,c)` on the high cube, with all indices binary and all entries nonzero. Orthogonality of each low row against **both** full high rows gives the two determinant identities

    Q_{a,1,0}/Q_{a,0,0} = Q_{a,1,1}/Q_{a,0,1}     for each a,
    Q_{0,b,1}/Q_{0,b,0} = Q_{1,b,1}/Q_{1,b,0}     for each b.             (4)

The first ratio is independent of `c`, the second independent of `a`. Commuting the two ratios gives the second ratio independent of `b` as well: explicitly, if `Q_{a,1,c}=r_a Q_{a,0,c}` and `Q_{a,b,1}=s_b Q_{a,b,0}`, then the two evaluations of `Q_{a,1,1}` imply `s_0=s_1`. The two high rows `(x,c=0)` and `(x,c=1)` of the actual `DC | AB` cut are consequently nonzero proportional vectors on their entire four-column supports, contradicting orthogonality. All divisions are legitimate because the x-cube is full. The case `g` constant and `f` bijective is the transposed argument.

This exhausts `3445` and `4445`; therefore a q=5 party has surplus exactly `(2,2,0,0,0)`.

## 6a. Distance and cross-cut synchronization of its two six-word slices

Let the two high D symbols be `x,x'`. Each has degree two and surplus two, so its six E words are six distinct vertices of its own binary cube, equivalently the complete cube with two distinct vertices deleted. In any physical system `Dj`, the two lines at a fixed high D symbol have multiplicities `(4,2)` if the two deleted vertices agree in coordinate `j`, and `(3,3)` if they differ. By the complete per-pair degree alternatives in Section 1, the two high D symbols must show the **same** alternative in every party `j`. Thus the set `T` of coordinates on which the deleted vertices agree is common to both symbols.

If `|T|=2`, take the two corresponding cuts. In each, the two degree-four rows lie in one 12-entry block and share all four opposite pair values. One cut therefore identifies the two high D symbols' two-neighbor alphabets at the other two parties; the second identifies the remaining alphabet. Both six-word slices lie in one common binary four-party box. For each cut, all four rows `(D high symbol, j neighbor)` occur and are supported on the four complementary box values. As in Section 2 they form a 4-by-4 unitary, contradicting the four-qubit lemma. The deleted vertices are distinct, so `|T|=3` is impossible. Hence `|T|≤1`, i.e. distance two or three, synchronized between the two high slices. This proof does not assume the two slice phases agree or restrict them to signs.

## 7. Exact common-support, common-amplitude, common-phase residual

The following formulation is an equivalence for the **single** N50/t26 branch, not an assertion that the residual is feasible. It also makes the new alphabet obstructions usable without replacing the problem by separately realized cut graphs.

Choose actual word sets `P,E⊂[6]^4` with `|P|=26`, `|E|=24`. Require, for all six physical party pairs, that the 26 P projections are distinct and disjoint from the ten E projections, that every other physical pair value has at least two E extensions, and that the three bipartite E support graphs have the actual t26 component alternatives and genuine-unitary necessary order-four masks of Section 1. Require the q/profile, degree, surplus, P-moment and high-slice restrictions above. All these conditions refer to the same two word sets. A high slice's deleted vertices and all Hamming comparisons are relative to its own actual two-element partner alphabets.

Give each `w∈E` a **single** variable `x_w>0`. For every physical pair value `p` used by E, impose

    Σ_{w: w_pair=p} x_w = 1.                                             (5)

Since each such line has at least two positive terms, automatically `x_w<1`. For every unordered pair `p≠p'` of E values in each of the six pair systems, let `I(p,p')` be the set of complementary pair values `r` for which both words `(p,r),(p',r)` are in E. A valid mask has `|I|=0,2,3,4`, never one. For `|I|=2`, with common complementary values `r,s`, put

    u=(p,r), v=(p',r), w=(p,s), z=(p',s),
    x_u x_v = x_w x_z,                                                   (6)

and make an integer row `e_u-e_v-e_w+e_z`. Stack ALL such cut-indexed rows, including rows from transposed physical pair systems, into `M`; do not deduplicate across cuts as a substitute for the actual equations. All variables refer to the same 24 words.

The following integer condition is necessary for the common complex phases:

    for every y∈ker_Z(M^T),        Σ_i y_i is even.                       (7)

Indeed, for phases `z_w=exp(2πiθ_w)`, the two-term orthogonality equations are precisely `Mθ=(1/2)·1` in `(R/Z)^m`. Conversely, (7) is sufficient for THESE two-term phase equations: integral Smith normal form reduces nonzero diagonal equations to multiplication maps on `R/Z`, all of which are surjective, and zero diagonal rows impose precisely the integral left-kernel parity conditions. A mod-two dependency alone is not in general an integral dependency. Equation (7) by itself is not sufficient for a tensor.

After imposing (6) and (7), require one common `θ∈(R/Z)^24` satisfying `Mθ=(1/2)1` and, for every `|I(p,p')|=3` or `4`, the actual coupled complex equation

    Σ_{r∈I(p,p')} sqrt(x_(p,r) x_(p',r))
       exp(2πi(θ_(p,r)-θ_(p',r))) = 0.                                  (8)

In particular the largest of the three/four positive term lengths cannot exceed the sum of the others; this polygon inequality is only a necessary relaxation. Conditions (5)–(8) keep the same amplitudes and phases through all six systems; phases at different occurrences of a word are not separate choices.

**Equivalence proof.** An actual tensor provides all of these data. Conversely, given actual P,E and a simultaneous solution, set `U_w=1` for `w∈P`, `U_w=sqrt(x_w) exp(2πiθ_w)` for `w∈E`, and zero elsewhere. P rows and columns are isolated in every cut, (5) gives all row norms, and (6)–(8), including the zero-overlap cases, give every required E row inner product. Each square 36-by-36 flattening is unitary. Moreover `Σ_E x_w=10` by summing any one physical pair system, so `Σ|U_w|²=26+10=36`, and `ψ=U/6` is normalized with exactly the stipulated support and t. Thus the unresolved first step is the existence or impossibility of one actual P/E incidence and one simultaneous continuous solution of this displayed system. No finite search, independent-cut phase witness, or solution of (7)–(8) is claimed.

## 8. Source coverage and process boundary

Before reading a mathematical body I read the complete manifest, freeze receipt, final binding, parent live metadata, actual dispatch receipt, and all 22 manifest-listed controls through their endings; `prebody-ack-v1.md` was then written. Initially collapsed administrative displays were recovered with raw reads; the large dispatch receipt was additionally reread in raw windows. Controls were status/permission only, not mathematical inputs. After the acknowledgement, the **one** literal part was read serially in raw windows `1–20, 21–40, …, 381–400, 401–408`, including the ending and long lines, before reasoning. Every displayed packet window was below 30,000 bytes and no packet clipping was observed. The part renders S1–S6 completely, respectively original LF `1–33, 1–23, 1–21, 1–34, 1–161, 1–110`. Parent-supplied part SHA-256 is `39fcfcdd588d30595023a246084e3b021da5b2d94be5841e2f35bd1451fb404d`; source hashes and exact original paths are in `manifest-v1.json`. I did not independently rehash or open the outgoing source files, and the binding is not source-identity certification.

The t26 component alternatives and low-excess proof bodies are explicitly present in S1/S5/S6 and are used at their stated scope. The present argument does not use the linked but unprovided global `t≤28`, no-OLS, previous support-union bodies, finite source/results, or t22/t28 theorems as premises; any future composition needing them must name and import their missing load-bearing bodies conditionally. All genuine held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remain NONINPUT; no linked scientific source, held body, old code or sibling output was opened. No network, external model, scientific code, child subprocess, scientific eval, test, solver, compilation, build, lint or formatter was used. No code was prepared or hashed. No family, human, formal/kernel, independent-review, parent-adoption or priority assurance is asserted. Corrections, if needed, must be additive and never overwrite this candidate.
