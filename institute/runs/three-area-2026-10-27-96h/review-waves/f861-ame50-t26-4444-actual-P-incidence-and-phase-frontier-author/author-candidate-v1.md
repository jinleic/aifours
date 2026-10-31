# Actual AME(4,6), N=50, t=26, q=4444: same-P incidence and common-phase frontier

**Prospective GENERAL AUTHOR candidate; nonblind, same harness; not a parent disposition.** Fix one normalized complex four-party tensor in one local product basis, put `U=6ψ`, and suppose its three 36-by-36 balanced flattenings are unitary, its support has 50 words, exactly 26 of them have modulus one, and the other 24 have E-alphabet sizes `(4,4,4,4)`. All statements below concern this one actual tensor, its same 26 P words, its same 24 E words, and arbitrary nonzero complex E amplitudes. They do not assume a q=5 party, a global support minimum, a global t bound, or a phase/sign ansatz.

**Results.** The three moment-possible P count profiles are `(0,2,18,6,0)`, `(0,1,21,3,1)`, and `(0,0,24,0,2)`, where the subscript counts coordinates in the actual E alphabets. The entire middle profile is impossible by the same-P argument in §3. The first profile has an additional explicit forbidden singleton class (§4). In the last profile every party has degree multiset `2,2,3,3`; its two all-inside P words pick exactly the two degree-two symbols at every party; and no party can concentrate all four surplus units on one symbol (§5). Thus several surplus distributions are excluded. If a surplus `(3,1)` occurs, §6 gives a further cross-party restriction using actual P words. Section 7 gives an exact parameterization of every surviving last-profile P incidence, and §8 gives an iff with one actual P/E support, one positive amplitude and one phase per E word, and the six physical pair systems coupled. No surviving profile, support, phase solution, or AME witness is asserted to exist.

## 1. Actual pair incidence and the cut interface

Write the parties as `I={1,2,3,4}`. Let `P` be the actual 26 modulus-one words and `E` the other 24 support words. In every physical pair system, a P entry exhausts its unitary row and column. Consequently the 26 P pair values are distinct, no E word has any of those values, and the complementary ten physical pair values occur in E. Each such E value has at least two extensions: a residual unitary row with only one entry would contain a modulus-one entry. These assertions apply also to the transposed pair system and to the **same** P and E.

Let `Q_i` be the four actual E-used symbols at party i and `O_i` its two unused symbols. For `a∈Q_i`, write `d_i(a)` for the number of its E neighbors in any one other party. This degree does not depend on the other party: the number of P words containing a is `6-d_i(a)` in each of the three pair projections. Let `s_i(a)` count its E words and put `h_i(a)=s_i(a)-2d_i(a)`. Then

```
 d_i(a)≥2,    Σ_{a∈Q_i}d_i(a)=10,
 h_i(a)≥0,    Σ_{a∈Q_i}h_i(a)=4.                         (1)
```

For `d_i(a)=1`, every other coordinate in its E slice is fixed, so there can be at most one distinct E word, contradicting the two-extension rule. With four used symbols, (1) gives exactly the degree multisets `4,2,2,2` and `3,3,2,2`.

We use the following actual-unitary cut lemma, whose proof is included here rather than importing a graph-only enumeration. On **either side** of any residual 10-by-10 cut, the ten E line multiplicities are either four 3's and six 2's, or two 4's and eight 2's. In the latter case the two degree-four rows have the same four complementary pair values, and each such complementary value has degree three. In particular a 3-line and a 4-line never coexist on the same side.

For completeness, here is the written reduction. A unitary support component is square; two rows or columns cannot overlap in exactly one entry. In a component of order above two, the two neighbors of a degree-two row are twin columns of degree at least three. Different degree-two rows meeting high rows have disjoint twin pairs: if two low rows shared their pair, those two orthonormal rows would exhaust both columns and isolate a 2-by-2 component. The transposed facts also hold. If a component has order `m`, excess `e_c` over `2m` entries, and `k` low rows, then `m-e_c≤k≤floor(e_c/2)`.

Excess zero gives a full 2-by-2 block; excess one is impossible; excess two gives a 3-by-3 block with one zero. A positive excess-four component has order at most six. At order five, one low row leaves four degree-three rows; unless all four use its twins, a high row avoiding the twins meets one using them exactly once; if all use them the other three columns receive only four entries, below their required six. With two low rows, their four twin columns have degree three and the fifth degree two. Their two-high-row neighborhoods are two-subsets of three high rows; singleton overlap forces them equal, leaving one high row with at most one neighbor. At order six, two low rows and two low columns remain, all other lines have degree three. The two low columns partition the four high rows into two pairs. Each high twin-column pair must use one whole pair, else it overlaps a low column once; choosing the same pair leaves the other high rows too small, choosing different pairs splits the component. Thus a connected excess-four component has order four. The total excess is four, so the residual support consists either of two excess-two 3-by-3-minus-one components plus two 2-by-2 blocks, or one order-four/12-entry component plus three 2-by-2 blocks.

For the latter, the only possible degree partitions on a side are `3333`, `2334`, `2244`. The middle one is impossible: its low row has twin columns. Twins of degree three leave a degree-three row avoiding them and unable to fit in the other two columns. Twins of degree four force the other two columns to have degree two and to overlap in exactly the degree-four row. With `2244`, the low rows have disjoint pairs, the other rows are full, and every opposite column has degree three. This proves the stated multiplicity alternatives and common-neighbor conclusion. These are necessary facts for a genuine unitary, not independent choices of six masks.

Finally, if `d_i(a)=2`, then `h_i(a)≠1`: five words in a binary three-cube would give at least two overlap edges in each direction by actual row orthogonality, but five cube vertices induce at most five edges. Also `h_i(a)≠3`: its seven words would give one 3-line and one 4-line in a single physical pair system, contrary to the just-proved cut lemma. Thus

```
        d_i(a)=2  ⇒  h_i(a)∈{0,2,4}.                       (2)
```

The five-cube-vertex count uses that the three deleted cube vertices induce at most two edges, so they remove at least seven of the twelve cube edges.

## 2. The three actual P moment profiles and symbol identities

For `k=0,...,4`, let `n_k` count P words with exactly k coordinates in the corresponding `Q_i`. In a pair system the inside/inside, inside/outside, outside/inside, and outside/outside P cell counts are respectively `6,8,8,4`. The first two moments therefore give

```
 Σ n_k=26,     Σ k n_k=56,     Σ C(k,2)n_k=36.
```

Solving them yields `n_1=2-3n_0-n_4`, `n_3=6-n_0-3n_4`, and `n_2=18+3n_0+3n_4`. Nonnegativity forces `n_0=0`. Writing `r=n_4∈{0,1,2}`, the three profiles are precisely

```
 r=0: (0,2,18,6,0);   r=1: (0,1,21,3,1);
 r=2: (0,0,24,0,2).                                      (3)
```

For each party let `u_i` be the number of single-inside P words whose inside coordinate is i, and `v_i` the number of triple-inside P words missing i. The six inside/inside pair-cell counts and fourteen inside incidences at i give the stronger **partywise** identities

```
 u_i+v_i=2-r,     Σ_i u_i=2-r,     Σ_i v_i=6-3r.          (4)
```

For example, if `p_ij` counts P words inside exactly i and j, then `p_ij=6-r-v_k-v_l` for `{i,j,k,l}=I`. Substituting these in the 14 i-inside incidences gives (4). These are equations for the same words, not separate pairwise completions.

There is also a per-symbol identity. Let `z_m(a)` count the P words containing `a∈Q_i` and having m inside coordinates. In each of the other three parties exactly `4-d_i(a)` Q symbols give P values with a. Thus

```
 Σ_{m=1}^4 z_m(a)=6-d_i(a),
 z_2(a)+2z_3(a)+3z_4(a)=3(4-d_i(a)),
 z_1(a)-z_3(a)-2z_4(a)=2(d_i(a)-3).                     (5)
```

A degree-four symbol must have `z_1=2` and `z_2=z_3=z_4=0`. In the r=0 case the converse holds if both singleton P words use the same symbol a: for degree two, (5) and the word count would force a negative `z_2`; for degree three the same is true. Hence a degree-four symbol occurs iff both singleton words are at the same party and the same actual symbol. At most one party can then have degree four. If the two singletons are at distinct parties, or at distinct symbols of one party, all four degree multisets are `2,2,3,3`.

## 3. Complete exclusion of the r=1 P count class

Suppose r=1. There is only one singleton P word. Therefore no symbol can have degree four, and each party has two degree-two and two degree-three E symbols. Let `w*` be the one all-inside P word. If `w*_i` had degree three, (5) with `z_4(w*_i)=1` would require at least two singleton P words at that symbol. Thus `w*_i` has degree two at every party. Let `v_i` be the **other** degree-two symbol at i.

Let h be the inside party of the unique singleton. By (4), `v_h=0` and `v_j=1` for `j≠h` (here `v_j` is the triple count, not the symbol just named; below call the symbol `b_j` to avoid ambiguity). Write `b_j` for the degree-two symbol distinct from `w*_j`. The three triple-inside P words are `T_j`, `j≠h`, where `T_j` misses j. For each `j≠h`, (5) at `b_j` gives exactly two triple occurrences because `z_1=z_4=0`; the only two triple words containing j are therefore both at `b_j`. At h, (5) gives `z_3(b_h)=2+z_1(b_h)≥2`. Choose two distinct triple words `T_j,T_k` containing `b_h`. They also both contain the fourth party `l`, and by the preceding sentence both have symbol `b_l` there. Their `(h,l)` P projections coincide, contradicting actual P injectivity. Thus **all** of r=1 is excluded; no E phase, independent pair completion, or q=5 premise was used.

## 4. A forbidden class within r=0

Assume r=0, both singleton P words have inside party i, and they use the two **different degree-two** symbols `a_0,a_1` of that party. Let `D_j` and `T_j` be respectively the two degree-two and two degree-three symbols at each other party j. No other party has a singleton, so (5) says its triple P words can use only `D_j`, not `T_j`. By (4), there are two triple words missing each j≠i and none missing i.

For either `a_b`, (5) gives exactly three triple P words. They must miss the three other parties one each. Indeed, if two missed the same j and the third missed k≠j, all three would contain the remaining party l, use its two-symbol `D_l`, and have the same i symbol; two would repeat an `(i,l)` P value. Hence, for every j≠i, the two triples at `a_b` containing j use both symbols of `D_j`. Since `d_i(a_b)=2`, exactly two Q_j cells at `a_b` are P cells; these are all of `D_j`. Consequently its two E neighbors at j are exactly `T_j`.

For each of the three cuts `ij|kl`, the four actual E rows `(a_b,t)`, `b=0,1`, `t∈T_j`, are supported wholly on the four columns `T_k×T_l`. They form a 4-by-4 unitary, simultaneously for all cuts of the **same** binary subtensor. This is impossible. To see the binary obstruction directly, normalize that subtensor by 2 and let `A_s` be the sum of squared Pauli coefficients of weight s. Its two-party marginals are maximally mixed, so `A_1=A_2=0`. Each three-party marginal has purity 1/2, giving `A_3=12`; global purity gives `A_4=3`. Positivity of the spin flip would require `(1-A_3+A_4)/16≥0`, but it equals `-1/2`. Thus this specified r=0 singleton/degree class is excluded. The other r=0 singleton placements and surplus classes are **not** excluded by this paragraph.

## 5. The r=2 all-inside words and exclusion of surplus four

In r=2, `n_1=n_3=0`. Equation (5) gives `z_4(a)=3-d_i(a)`. Hence every party has `D_i={d_i=2}` and `T_i={d_i=3}`, both of size two. The two all-inside P words `w^0,w^1` use every symbol of `D_i` exactly once: `D_i={w_i^0,w_i^1}`. In particular `w_i^0≠w_i^1` for every i. Every other P word has exactly two inside coordinates.

We now show that no `h_i(a)=4` is possible in r=2. If `d_i(a)=3`, the cut lemma forces, in each `ij` system, two E lines `(a,b)` of multiplicity four and one of multiplicity two. For a fixed j, the two full rows have the same set S of four opposite `(k,l)` cells. Let the two words in the remaining `(a,b_low)` line have projections `(k_1,l_1),(k_2,l_2)`. Every `(a,k)` line has even multiplicity, 2 or 4. Its contribution from the two full rows is twice the number of S cells with that k; the number of the two low-row words with that k is therefore even. Since there are two, `k_1=k_2`. The same argument at l gives `l_1=l_2`, contradicting distinct words. This part needs no q=5 assumption.

It remains to rule out `d_i(a)=2,h_i(a)=4`. Its E slice consists of all eight words of a binary cube, `a×H_j×H_k×H_l`. Each symbol in each `H` has surplus exactly two, and all other symbols at those parties have surplus zero. The cut lemma says that every high-high value in `jk`, `jl`, and `kl` has multiplicity three: the cube supplies two extensions and there is exactly one outside-a extension.

There is no outside-a E word high in all three coordinates. Indeed any other i symbol p has `h_i(p)=0`, so each `(p,j)` E line has exactly two words, regardless of whether `d_i(p)=2` or 3. If one p word were high-high-high, comparing its three p-lines with the corresponding full a-lines forces, by no singleton overlap, one more high-high-high word in each line. The three mates are distinct because a high-high pair has only one outside-a extension. The four high triples form a binary parity class. For `z_x=U_{a,x} overline(U_{p,x})≠0`, every pair of its four triples agrees in one coordinate; actual row orthogonality gives `z_x+z_y=0` on every edge, impossible on a triangle.

Thus the twelve outside-a extensions of the twelve high-high pair values are twelve distinct words, each high in exactly two coordinates. Each high symbol has its four cube occurrences plus four distinct outside occurrences. Since its surplus is two, `2d+2≥8`, and the r=2 degree bound forces `d=3`. Thus `H_j=T_j` at each of the other three parties. The 12 outside words together with the cube exhaust all eight occurrences of every high symbol. The remaining four of the 24 E words would therefore use only the three degree-two alphabets `D_j,D_k,D_l`. But for any such word, its bit relative to `w^0,w^1` at each of these three parties would have to differ pairwise: equal bits give the P pair value of `w^0` or `w^1`. Three binary bits cannot be pairwise different. Contradiction. Hence

```
                    r=2  ⇒  h_i(a)≤3 for every i,a.       (6)
```

Combining (2), (6), and total surplus four, the only possible ordered-by-degree patterns at any party are:

* **A:** two symbols have surplus two and the others zero, in any degree positions;
* **B:** the two degree-three symbols have surpluses three and one; the degree-two symbols have zero;
* **C:** one degree-two symbol has surplus two, both degree-three symbols have surplus one, and the other degree-two symbol has zero.

These are necessary classes, not claimed realizations.

## 6. Cross-party consequence of a `(3,1)` surplus

Still in r=2, suppose party i is type B. Let c and t be its surplus-three and surplus-one symbols. Every pair system incident to i must have four multiplicity-three values, since a two-four system gives only even symbol surpluses. Its four surplus edges are simple. The three E neighbors of c must be three different positive-surplus symbols at the opposite party; therefore each of the other three parties must be type C, the only pattern above with three positive symbols. In each such party j, write `b_j∈D_j` for the surplus-two symbol. The three surplus edges at c meet all three positive symbols; the remaining surplus edge, at t, must meet `b_j`. Hence `(t,b_j)` is an E value of multiplicity three, for each j≠i.

All six pair systems are consequently four-three systems, since each of the other three parties has odd symbol surplus too. Moreover the three `b_j` cannot all have the same bit relative to the two actual P words `w^0,w^1`. If they did, any pair `b_j,b_k` would be a P value and no E word could contain both. The three disjoint `(t,b_j)` lines would then contain nine E words at t, but `s_i(t)=2·3+1=7`. Thus their bits are distributed two of one kind and one of the other. In particular at most one party can be type B. This is a same-P and same-E consequence; it is not an assertion that the remaining type-C configurations or their phases exist.

## 7. Exact P incidence parameterization for r=2

The following describes **all** r=2 P sets with the actual pair-injectivity rules, before choosing E or phases. Choose the four actual `Q_i` and two-element `O_i`, and choose `w^0,w^1∈∏Q_i` with `w_i^0≠w_i^1` for every i. For each unordered pair `ij`, with complement `kl`, choose a bijection `f_ij:Q_i→Q_j` and a bijection `g_ij:Q_i→O_k×O_l` (order i<j only for notation). Form four words `P_ij` by putting the Q coordinates at `a,f_ij(a)` and the O coordinates at `g_ij(a)`.

Require (i) `f_ij(w_i^b)≠w_j^b` for b=0,1; and (ii) for every i, a∈Q_i, and j≠i, if k,l are the remaining two parties, the unique `P_ik` word with i symbol a and the unique `P_il` word with i symbol a use the two **different** values of `O_j`. Then

```
              P={w^0,w^1} ∪ ⋃_{i<j} P_ij              (7)
```

has 26 distinct words and injective projections in every physical pair. Conversely every actual r=2 P set has exactly this form. Indeed, for each `ij` the four `P_ij` words cover the four `O_k×O_l` values; (5) says each Q_i symbol occurs once in this layer, and similarly for Q_j, so f and g are bijections. Conditions (i) and (ii) are respectively the inside/inside and inside/outside collision exclusions. Outside/outside cells are covered by g, while the two all-inside words are injective because all their coordinates differ. These cases exhaust all pair cell types.

There is a further convenient same-P consequence. Label each O alphabet by bits. Fix i and, for each j≠i, define a bit function `b_ij(a)` as the j-outside bit of whichever of the two layers `P_ik,P_il` is selected by a fixed ordering of k,l. The other layer uses its complement by (ii). For each `ij`, the two outside bits of `P_ij` are fixed complements of the corresponding two b-functions, and g is a bijection. Hence for each i, any two of its three b-functions give all four binary pairs as a varies through Q_i. Their three-bit values form one parity class: writing the third bit as a function of the first two, balance in both directions forces it to be their XOR plus a constant. In particular any two distinct Q_i symbols differ in exactly two of these three bits. This is a restriction on one common P set, not a construction of E.

## 8. Exact shared-support and common-phase criterion

The following iff makes the unresolved frontier explicit without pretending that separate pair completions or independent phase solutions form a tensor. It also applies to r=0; for r=2, (7) can be used as the exhaustive P generator.

Choose one `Q_i⊂[6]` of size four, put `O_i=[6]\Q_i`, and choose one `P⊂[6]^4` with 26 distinct words, the appropriate r=0 or r=2 profile from (3), and injective projection in all six pair systems. Require every physical pair value outside `Q_i×Q_j` to be a P value. Let `F_ij=[6]^2\π_ij(P)`; these are ten inside/inside values. Choose one set `E⊂∏Q_i` of 24 distinct words with `π_ij(E)=F_ij` in every physical pair and at least two E extensions at each F value. The r=0 singleton exclusion, the r=2 degree/surplus restrictions, and §6 are necessary filters on these same words. They may be imposed to shrink the finite support domain; none is claimed sufficient.

For each `w∈E` choose one **shared** `x_w>0`. For each of the six physical pair systems and each E pair value p impose

```
                    Σ_{w: π(w)=p} x_w = 1.                (8)
```

Every x is then less than one. For distinct E pair values p,p' in a physical pair system let `I(p,p')` be their common complementary pair values. Forbid `|I|=1`. If `I={r,s}`, put `u=(p,r), v=(p',r), w=(p,s), z=(p',s)` and require

```
 x_u x_v = x_w x_z,          M_(p,p')=e_u-e_v-e_w+e_z.  (9)
```

Stack these integer rows from **all six** physical pair systems into one matrix M with the same 24 word columns. A necessary and sufficient condition for the two-term **phase subsystem alone** is

```
       for every y∈ker_Z(M^T),       Σ_j y_j is even.     (10)
```

Necessity follows by pairing the equations `Mθ=(1/2)1` in `R/Z` with y. For sufficiency, integral Smith normal form makes each nonzero diagonal multiplication surjective on `R/Z`; the zero rows are exactly an integral left-kernel basis and require the displayed even sums. A mod-two dependency need not be an integral dependency. Reversing a row only changes its sign and does not change its RHS modulo one or the parity condition.

Finally require one `θ∈(R/Z)^24` satisfying `Mθ=(1/2)1` and, simultaneously for **every** `|I(p,p')|≥3` in every pair system,

```
 Σ_{r∈I(p,p')} sqrt(x_(p,r)x_(p',r))
                 exp(2πi(θ_(p,r)-θ_(p',r))) = 0.       (11)
```

The cut lemma bounds actual overlap sizes by four, but writing `≥3` makes the iff independent of using that bound as a shortcut. No equation is needed at zero overlap. Polygon inequalities and (10) alone are only necessary relaxations; the same θ must solve (11) too.

**Proof of iff.** An actual tensor supplies P, E, x and θ, the six norm equations and all overlap equations. Conversely, given one such support and simultaneous solution, set `U_w=1` for w∈P, `U_w=sqrt(x_w)exp(2πiθ_w)` for w∈E, and zero otherwise. Every P row and column is isolated by the physical P projections. Equation (8) normalizes E rows, (9) plus the two-term phases makes their two-overlap inner products vanish, and (11) handles the remaining nonempty overlaps. The three square flattenings are unitary. Summing one pair system's ten E-row norms gives `Σ_E x_w=10`, so `Σ|U_w|²=26+10=36` and `ψ=U/6` is normalized with exactly 50 nonzeros and exactly 26 modulus-one entries. Thus the criterion is necessary and sufficient **for this scoped branch**, but its residual joint feasibility has not been decided here.

## 9. Coverage, conditional boundaries, and status

Before any packet-body read or task-specific mathematical reasoning I read the manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all 22 manifest-listed status-only controls. Initial non-raw administrative displays elided blocks; complete raw displays recovered them before I created `prebody-ack-v1.md` and sent the direct prebody acknowledgement to Main. The status controls were not mathematical inputs. The output names were absent in the initial owned-directory listing; the write interface does not expose an OS-level exclusive-create flag, so no stronger atomic-creation guarantee is claimed.

Only after both acknowledgements I read the single literal packet part in order, raw windows `1–20, 21–40, …, 401–420, 421–438`, including the ending. Every display was below 30,000 bytes; no packet clipping was observed and no packet clipping recovery was needed. The packet completely renders S1 original LF 1–203, S2 1–163, S3 1–33, and S4 1–21. Parent-supplied packet SHA-256 is `ff860db56e111022deb9aa77ee2d7187a0bbaa248aaa4500804352cd340bc220`; S1–S4 source pins and exact paths are in the frozen manifest. These are supplied administrative bindings, not independently recomputed hashes or source-identity certification.

S1 and S2 are earlier nonblind author candidates, not automatically accepted. S3 supplies the scoped low-excess t26 interface; the needed cut and degree facts are reconstructed in §1. S4 is background for the integer-kernel formulation; §8 reconstructs its actual t26 use. No absent linked source, q=5 theorem, prior global t bound, no-OLS result, historical executable, sibling science, held episode, or held proof/method/selection/planning/verification/reporting/confidence/downstream consumer was opened or used. If §1's written cut reconstruction is not accepted, the surplus conclusions depending on it are conditional on the explicit actual-unitary multiplicity/common-neighbor lemma stated there; the same-P r=1 exclusion and the r=0 singleton-class exclusion use only the basic actual-unitarity/pair-injectivity facts and the displayed binary-box proof. No unlisted missing body is silently treated as proved.

No network, external model, scientific eval, code execution, test, solver, child subprocess, compilation, build, lint, formatter, Git or deletion was used. No verifier was prepared, so there is no code hash or computational verification. No complete r=0 or r=2 exclusion, support witness, global-minimum theorem, human/family/formal acceptance, publication priority, or parent adoption is claimed. The remaining exact question is whether one of the surviving actual P/E supports admits the common positive-amplitude and common-phase system (8)–(11). Any correction must be additive, not an edit of this candidate.
