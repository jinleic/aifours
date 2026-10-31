# Prime-power PSL₂ and eight actual cosets: a fresh conditional author reconstruction

**Status: UNADOPTED AUTHOR CANDIDATE.** Subject to the subgroup-classification import stated precisely below, the written argument proves the eight-actual-left-coset assertion for every `PSL₂(p^f)` with `f ≥ 2`. It proves the stronger three-proper-label property except at `q=4,9`, and handles those two values using actual coset intersections and capacity. It also reconstructs a conditional normal-extension consequence and necessary, not sufficient, 6+2 conditions. It does **not** prove unrestricted Sun8, the all-kernel normal-cut implication, or any original acceptance gate. Parent full reading, source checking and disposition, and disjoint mathematical review remain unpaid. There is no external-family, human, kernel, priority, novelty, or automatic previous-gate credit.

Native clock observed before creating this artifact: **2026-10-30T15:40:10-0700 PDT**. This is not an onset or completion time.

## 1. The objects and the conditional assertion

All indices below are finite. For a group `X`, let `B₇(X) ≤ r` mean that among any `r+1` pairwise-disjoint **actual left cosets** `xᵢUᵢ`, two subgroup indices have gcd at least 8. Different cosets may have the same subgroup, and indices may repeat. Let `J₇(X) ≤ s` mean that among any `s+1` proper subgroup **labels**, with repetitions allowed and no disjointness requirement, two indices have gcd at least 8. These are different assertions. If `J₇(X) ≤ 2`, any three disjoint actual cosets have the desired pair: a subgroup of index 1 has its sole coset equal to `X` and cannot coexist disjointly with another coset; otherwise all three labels are proper.

**Theorem, conditional on §2.** For every prime `p` and every `f ≥ 2`, putting `q=p^f` and `T=PSL₂(q)`, one has `B₇(T) ≤ 7`. More precisely:

* If `q` is neither 4 nor 9, `J₇(T) ≤ 2`, hence `B₇(T) ≤ 2`.
* If `q=4` or `q=9`, `B₇(T) ≤ 7`, but no finite `J₇(T)` bound holds. The latter statement follows by repeating one proper subgroup label of index 5 or 6; it is not a statement about infinitely many disjoint cosets.

Thus all four specified characteristics `p=2,3,5,7` are included, with no restriction to those four.

Two elementary facts will be used repeatedly. If `A,B ≤ X` have coprime finite indices, **every** left `A`-coset meets **every** left `B`-coset. Indeed, the map `X/(A∩B) → X/A × X/B`, `x(A∩B) ↦ (xA,xB)`, is injective. Its domain has cardinality divisible by both indices and at most their product, so coprimality forces equality and surjectivity. Consequently disjoint actual cosets cannot have coprime subgroup indices. Second, if `X` is finite and actual cosets are disjoint, `Σ 1/[X:Uᵢ] ≤ 1`; this counts the cosets themselves, including repetitions of a subgroup label.

## 2. Explicit external import and order arithmetic

The sole non-elementary premise is the following overinclusive consequence of Dickson's maximal-subgroup classification as stated in the frozen parent-read excerpts of M. Giudici, *Maximal subgroups of almost simple groups with socle PSL(2,q)*, arXiv:math/0703685v1, Theorems 2.1–2.2, and corroborated in the frozen excerpt of A. Beltrán and F. Viudez, arXiv:2607.09144v2, Theorem 3.2. The underlying named sources are <https://arxiv.org/pdf/math/0703685v1> and <https://arxiv.org/html/2607.09144v2#S3.Thmtheorem2>. The latter excerpt explicitly renders the relevant inequality signs that were lost in the Giudici PDF extraction. I did not follow these links or independently inspect the source: the theorem below is conditional on the stated classification premise and on the excerpts' fidelity.

Every proper subgroup of `T` is contained in a maximal one. For `q=2^f ≥ 4`, the maximal groups are among a Borel of order `q(q−1)`, dihedrals of orders `2(q−1), 2(q+1)`, and subfield groups of order `q₀(q₀²−1)` for `q=q₀^r`, `r` prime. For the argument I may harmlessly include `q₀=2` even when the actual maximality condition excludes it.

For odd `q=p^f ≥ 5`, the maximal groups are among a Borel of order `q(q−1)/2`, dihedrals of orders `q−1,q+1`, subfield `PSL₂(q₀)` with `q=q₀^r` for odd prime `r`, subfield `PGL₂(q₀)` with `q=q₀²`, and `A₄,S₄,A₅`. For the exceptional entries, `A₄,S₄` are maximal only at prime `q`; a nonprime `q` has a maximal `A₅` only when `q=p²` and `p ≡ ±3 (mod 10)`. The actual small-`q` restrictions are material at `q=9`: the dihedral of order `q−1` requires `q≥13`, and the dihedral of order `q+1` excludes `q=7,9`. Hence at `q=9` the actual maximal indices are exactly `10` (Borel), `15` (`PGL₂(3)`), and `6` (`A₅`); there can be several conjugacy classes. At other values the inclusion of a nonmaximal dihedral only enlarges the list and is used as a divisibility overestimate.

The standard order identities follow directly by choosing a nonzero first column and a second column with determinant one: `|SL₂(q)|=q(q²−1)` and `|PSL₂(q)|=q(q²−1)/gcd(2,q−1)`. Also `|PGL₂(q₀)|=q₀(q₀²−1)` by dividing `|GL₂(q₀)|` by the nonzero scalars. In characteristic 2 the square map on the odd-order multiplicative group is bijective, so projective `GL₂` and `SL₂` have the same order and subfield order `q₀(q₀²−1)` as used above. A subgroup index is a multiple of the index of any maximal overgroup.

## 3. Two index divisors for every nonexceptional prime power

For each row below, every proper subgroup index is a multiple of at least one displayed integer, and both integers exceed 7:

| parameter | first divisor | second divisor |
|---|---:|---:|
| `q=8` | 9 | 28 |
| `q=2^f`, `f≥4` | `q+1` | 8 |
| `q=p^f` odd, `f≥2`, `q≠9` | `(q+1)/2` | `p²` |

The third row is a single all-exponent odd-characteristic argument; it does not require treating exponent 2 and the larger exponents as separate conclusions.

**Even characteristic.** The Borel and split-dihedral indices are `q+1` and `(q/2)(q+1)`. The other dihedral index is `(q/2)(q−1)`, divisible by 8 for `f≥4`. A subfield group for `q=q₀^r`, `q₀=2^d`, has index

`(q/q₀) · (q²−1)/(q₀²−1)`.

If `r=2`, this simplifies to `q₀(q+1)`. If `r` is an odd prime, its exact 2-adic valuation is `(r−1)d`. When `f=rd≥4`, this is at least 4: either `r≥5`, or `r=3` and `d≥2`. This proves the `f≥4` row. When `q=8`, the Borel and two dihedral indices are `9,36,28`; even if the excluded `q₀=2` subfield is overincluded, its index is `84`. Each is divisible by 9 or 28. At `q=4` neither proposed divisor argument gives the needed bound, so that case is treated separately.

**Odd characteristic, uniformly in `f`.** Since `f≥2` and `q≠9`, one has `q≥25`, so `A=(q+1)/2≥13`, and `B=p²≥9`. The Borel index is `2A`. Each dihedral order is prime to `p`, whereas the `p`-part of `|T|` is `p^f`, so its index is divisible by `B`. For a subfield `PSL₂(q₀)` with `q₀=p^d` and `q=q₀^r`, `r≥3` odd prime, the index has `p`-valuation `f−d=(r−1)d≥2`, so it is divisible by `B`. For a quadratic subfield, writing `q=q₀²`, its `PGL₂(q₀)` index is exactly

`[T:PGL₂(q₀)] = q₀(q+1)/2 = q₀A`,

which is divisible by `A` regardless of the size of its `p`-part. Finally, `A₄` and `S₄` do not occur as maximal groups for nonprime `q`. If an `A₅` occurs, then `q=p²` and `p≡±3 (mod 10)`; `p=3` is the separately excluded `q=9`, and `p=5` does not satisfy the congruence. Every remaining such prime is at least 7 and does not divide 60, so the `A₅` index is divisible by `p²`. This exhausts the imported list, including every `p,f` under the row's quantifiers.

For any three proper labels, assign each one either divisor from the appropriate row that divides its index. Two receive the same divisor, so their index gcd is at least that divisor and hence at least 8. This proves `J₇(T)≤2` and the direct actual-coset consequence for every nonexceptional `q`. No distinctness of labels, normality of subgroups, or disjointness of quotient shadows has been assumed.

## 4. Elementary group facts used in the two exceptions

For a finite field `F_q`, `q≥4`, let `U(s)=[[1,s],[0,1]]`, `L(s)=[[1,0],[s,1]]`, and `D(t)=diag(t,t⁻¹)`. The upper and lower unipotents generate `SL₂(q)`: row elimination reduces an invertible determinant-one matrix to a diagonal, and

`U(t)L(−t⁻¹)U(t) = [[0,t],[−t⁻¹,0]] = W(t)`, `W(t)W(−1)=D(t)`.

There is a nonzero `t` with `t²≠1`, since a degree-two polynomial has at most two roots and `q−1≥3`. The commutator `D(t)U(s)D(t)⁻¹U(s)⁻¹` is `U((t²−1)s)`; the analogous lower commutator gives all `L(s)` because `t⁻²−1≠0`. Therefore `SL₂(q)` and its quotient `PSL₂(q)` are perfect. A perfect group has no nontrivial solvable quotient. In particular it has no subgroup of index 2, 3, or 4: the nontrivial transitive coset action would map it to a solvable `S_k`, `k≤4`. For solvability use `S₄ ▹ A₄ ▹ V₄ ▹ 1` with abelian successive quotients.

We also give the small-group fact needed below without importing an `A₅` subgroup table. `A₅` is simple. Its conjugacy-class sizes are `1,15,20,12,12`: the 15 double transpositions and 20 three-cycles each form one `A₅` class, while the 24 five-cycles split into two classes of 12. This follows because an `S₅` class splits in its index-two subgroup `A₅` exactly when its centralizer contains no odd permutation; the centralizer of a five-cycle is its cyclic group, while the other two types have an odd centralizer element. A normal subgroup's order is 1 plus a subcollection of `15,20,12,12`. The possible cardinalities are `1,13,16,21,25,28,33,36,40,45,48,60`, and none except 1 and 60 divides 60. Since `A₅` is nonabelian, its derived subgroup is nontrivial normal, so it is perfect as well. Simplicity also excludes proper subgroups of indices 2, 3 and 4: the induced nontrivial action on at most four points would be faithful, but `60>|S₄|=24`. We will use these facts for an arbitrary subgroup isomorphic to `A₅`, not just for one chosen copy.

## 5. The actual-coset packing for `q=4`

Let `T=PSL₂(4)`, with `|T|=60`. A proper subgroup index divides 60; perfectness removes 2, 3 and 4, so the only possible indices are

`5, 6, 10, 12, 15, 20, 30, 60`.

This is an overinclusive list; existence of every entry is not needed. Suppose a pairwise-disjoint family has every pair of index gcds at most 7.

If some index is 5, the coprime-index lemma forbids 6 and 12. Every other label is 5 or belongs to `{10,15,20,30,60}`. Among the non-5 labels at most one lies in `{10,20,30,60}`, since any two share 10, and at most one is 15. Density permits at most five index-5 cosets. Thus the entire family has at most seven members.

Now suppose there is no index 5. Among the indices other than 6, there are at most three labels: at most one from `{10,20,30,60}`, at most one 12 and at most one 15. Six index-6 cosets fill the group, and more than six violate density. An eight-family would therefore have exactly five index-6 cosets and three others, namely 12, 15 and one member `n` of the four-number set. Since `gcd(15,n)≤7`, `n` is 10 or 20. Its density is at least

`5/6 + 1/12 + 1/15 + 1/20 = 31/30 > 1`,

contradiction. This proves `B₇(PSL₂(4))≤7` for actual disjoint cosets. A Borel has index 5, so repetition of that subgroup label proves that no finite `J₇` bound exists.

## 6. The actual-coset packing for `q=9`

Let `G=PSL₂(9)`, of order 360. We first derive a convenient faithful action, rather than assume an isomorphism to a named permutation group.

### 6.1. The six-point action from any index-six subgroup

The classification premise gives maximal `A₅` subgroups of index 6. Conversely, every subgroup `H` of index 6 is one: a maximal overgroup has index dividing 6, and the list `6,10,15` forces that index to be 6, hence it equals `H`.

Such an `H` is not normal in `G`: otherwise `G/H` has order 6. Every group of order 6 has a normal Sylow-3 subgroup, because the number of such subgroups divides 2 and is 1 modulo 3, and hence has a quotient of order 2; it is not perfect. This contradicts perfectness of `G`. The kernel of the action on `G/H` is the core of `H`, a normal subgroup of `H`; by simplicity of `H≅A₅`, it is either 1 or `H`. It cannot be `H` because `H` is not normal. Thus the degree-six action is faithful. Its image is perfect and so has trivial sign, hence lies in `A₆`. Both have order 360, so the image is all of `A₆`. In particular this action is 2-transitive: any map between two ordered pairs of distinct points extends to a permutation, and if that permutation is odd, interchange two of the four unused points to make it even.

For any two index-six subgroups `H,K` that are **not** conjugate, every left `H`-coset meets every left `K`-coset. To prove this, let `H` act on the six left cosets of `K`. There is no fixed point: a fixed coset would give `H≤xKx⁻¹`, and equality of the subgroup orders would make them conjugate. An orbit has size 1 or at least 5, because a point stabilizer is a subgroup of `H≅A₅` and there are no proper indices 2, 3, 4. With six points and no singleton, the action is transitive. Hence `G=HK`, and for arbitrary `g,h∈G`, `g⁻¹h∈HK` implies `gH∩hK≠∅`. Therefore all index-six subgroups underlying one disjoint coset family lie in a single conjugacy class.

Fix one such class and identify `G` with `A₆` by the action just derived. Its subgroups are the stabilizers `G_x` of the six points. Every actual left coset of a subgroup in this class has the form

`C(x,y) = {g∈G : g(x)=y}`.

Indeed, if `K=G_x`, a coset `gK` is exactly `C(x,g(x))`. Two distinct cells `C(x,y),C(x',y')` are disjoint exactly when `x=x'` or `y=y'`. If neither coordinate agrees, 2-transitivity gives an element in both; in fact their intersection has 12 elements, since four points remain to be bijected and exactly half of the `4!` completions are even. Equal first coordinates and unequal second coordinates are incompatible, as are unequal first coordinates and equal second coordinates, because permutations are bijective.

Consequently any pairwise-disjoint collection of at least three such cells lies in one row `x=constant` or one column `y=constant`: after two cells in one row, any cell outside it would need both of their different second coordinates to be disjoint from both; the column case is symmetric. For either a fixed input or a fixed output, the six cells partition `G`. Thus five disjoint index-six cosets have as their complement the sixth cell, itself an actual left coset `D=tK` of an index-six subgroup `K`. This is a statement about the actual sets, not just their sizes or index labels.

If two further actual cosets `aU` and `bV` are disjoint from those five, both are contained in `D`. Then `U,V≤K`: for example `a∈tK` and `aU⊆tK` imply `U≤K`. Translating both by the **same** `t⁻¹` gives disjoint actual `K`-cosets. Their original indices are `6[K:U]` and `6[K:V]`; the assumed original-index gcd at most 7 forces `gcd([K:U],[K:V])=1`. The coprime-index lemma contradicts their disjointness. Hence five index-six cosets can be accompanied by at most one further coset; six index-six cosets already fill `G` by density.

### 6.2. Counting all the other subgroup labels

Every proper subgroup index greater than 6 is divisible by at least one of `10,15,36`. Indeed, choose a maximal overgroup. If its index is 10 or 15 the claim is immediate. Otherwise it is an index-six `A₅`. If the subgroup index `n=6m` is not divisible by 10 or 15, then `5∤m`; also `m>1` and `m` divides 60. Thus `m∈{2,3,4,6,12}`. The elementary `A₅` fact above excludes 2, 3 and 4, leaving `n=36` or `72`. This argument includes subgroups inside any conjugacy class and does not assert that each candidate index actually occurs.

In a low-gcd family at most one label can be assigned to each of the divisors 10, 15 and 36, because two indices sharing any one of them would have gcd at least 8. There are therefore at most three labels of index greater than 6. The maximal-index list excludes proper indices below 6. If there are at most four index-six cosets, the family has at most seven cosets in total; if there are five or six, §6.1 gives at most six. This proves `B₇(PSL₂(9))≤7`. Repeating one index-six `A₅` as a proper label gives arbitrarily many labels with pairwise gcd 6, so no finite `J₇` bound holds.

## 7. Normal cuts: what follows, and what does not

For arbitrary `G`, normal `N`, `Q=G/N`, and an actual finite-index coset `Cᵢ=gᵢUᵢ`, put

`aᵢ=[Q:π(Uᵢ)]`, `bᵢ=[N:N∩Uᵢ]`, `nᵢ=[G:Uᵢ]=aᵢbᵢ`.

The index formula follows from `Uᵢ≤NUᵢ≤G`, `NUᵢ/N≅π(Uᵢ)` and `[NUᵢ:Uᵢ]=[N:N∩Uᵢ]`. Its quotient image is the actual left coset `π(gᵢ)π(Uᵢ)`. If several images contain the same quotient point `π(t)`, choose `xᵢ∈Cᵢ∩tN`. Then

`t⁻¹(Cᵢ∩tN)=(t⁻¹xᵢ)(Uᵢ∩N)`

is an actual left `N`-coset of index `bᵢ`. The same `t⁻¹` is used for all labels, so disjointness is preserved. Right translation instead would conjugate the slice subgroups; it must not be mixed with this left-translation formula.

**Conditional bridge.** If `B₇(N)≤5` and `J₇(Q)≤2`, then `B₇(G)≤7`. Otherwise take eight disjoint actual cosets with all original-index gcds at most 7. At most two `aᵢ` exceed 1: any three proper quotient subgroup labels would give a gcd at least 8 dividing the corresponding original-index gcd. Thus at least six quotient images are all of `Q`. Slice those six over one common quotient point; their actual `N`-cosets are disjoint and their pairwise index gcds divide the original ones, contradicting `B₇(N)≤5`. This applies in particular to the nonexceptional prime-power quotients from §3, but it assumes the stronger kernel bound 5.

**Necessary 6+2 structure under the original kernel bound.** Suppose instead `B₇(N)≤7`, `J₇(Q)≤2`, and an actual bad eight-family exists. As above at most two quotient images are proper. With zero or one proper image all eight images share a quotient point, yielding eight bad slices in `N`; therefore exactly two are proper and six are all of `Q`. The two proper actual image cosets must be disjoint, for otherwise a common point again yields eight bad slices. Label them 7 and 8 and set

`d=gcd(a₇,a₈)`, `e=gcd(b₇,b₈)`.

The coprime-index lemma on the disjoint quotient cosets gives `d≥2`; the original low-gcd hypothesis gives `d≤7`. For each of the six full-image labels `j`, slice separately over a point of image 7 and over a point of image 8. Disjointness of the corresponding kernel slices gives `2≤gcd(bⱼ,b₇)≤7` and `2≤gcd(bⱼ,b₈)≤7`. Moreover `d·e` divides `gcd(a₇b₇,a₈b₈)≤7`, so either `e=1` with `2≤d≤7`, or `(d,e)∈{(2,2),(2,3),(3,2)}`. The fibre for the first proper image need not be the fibre for the second; no simultaneous intersection or Helly conclusion is claimed.

These are necessary constraints on an assumed actual counterconfiguration, not an existence construction or a sufficiency/closure theorem. The unpaid mathematical step is to exclude or realize an actual eight-family with `B₇(N)≤7`, these 6+2 conditions, genuine quotient incidences, compatible subgroup slices and all original gcds at most 7. The hypotheses `B₇(N)≤7` and `B₇(Q)≤7` alone are not shown to imply `B₇(G)≤7`. For `q=4,9`, `J₇(Q)≤2` fails, so neither the bridge nor the 6+2 assertion is asserted from those quotient results. Other finite simple groups and unrestricted Sun8 remain outside this proof.

## 8. Provenance, methods, and unpaid checks

I first read the complete f667 manifest, freeze receipt, parent metadata, actual dispatch and every manifest-listed status control through its ending, and sent Main a direct pre-body ACK recorded in `prebody-ack-v1.json`. Only afterward I read the entire frozen literal packet, in order, raw windows of at most 20 LF: `1–20, 21–40, …, 261–280, 281–295`, including its ending. The live child metadata hash of the packet was `565792f5263384ab12c6ecf73cbdf2732621578b1cda4ea617c890981049046b`; manifest and freeze hashes matched the supplied pins. All derivation in this document followed that reading. The prior f642 candidate is part of the packet, so this is a nonblind alternative author reconstruction, not a claim that the author was uninfluenced by it or a cognition certificate. The packet's earlier author chronology and parent source readings are historical reports, not actions by this author.

The prospective author-selected representation in §6 is the six-coset action of `G` on `G/H`, derived here from an arbitrary index-six `A₅` and then identified with `A₆` by the elementary faithful-action/order argument. The uniform odd-characteristic divisor choice in §3 is likewise an all-variable written reconstruction. The separately treated numerical field sizes `4,8,9` and the small-group labels are already present in the frozen packet; no additional concrete field example or experimental case was selected. No stopped f653/f654/f659/f660/f662 scientific episode, history or consumer was read or used, and status controls were not treated as mathematical inputs. No sibling source, old author code, source link, external model or scientific program was read or run. **Child scientific execution: NOT RUN**; no solver, enumeration, CAS, test or numerical experiment was executed. All formulas and small arithmetic above are written proof steps, not machine-check results.

The complete source list is the literal packet's S1–S7 and the classification references quoted in §2; I followed no source links. In particular, the `A₅` classification and the `q=9` small-`q` maximal list remain explicit imports, not newly proved classifications. The parent must fully read this body and independently check the exact classification-source restrictions and excerpt fidelity, the all-prime-power divisor argument, the `A₅`/`A₆` reconstruction, all actual-coset orientation and complement claims, and the normal-cut hypotheses before any adoption. No proof of global Sun8, the original normal-extension closure, novelty, formal correctness, a human check, or independent-model-family verification is claimed.
