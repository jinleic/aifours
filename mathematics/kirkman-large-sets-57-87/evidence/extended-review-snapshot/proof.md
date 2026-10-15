# Proven reductions and obstructions — not solutions of LKTS(57) or LKTS(87)

These arguments concern explicitly restricted automorphism models. None rules out an unrestricted LKTS. No novelty is claimed. All point actions below act on block sets; where resolution invariance is needed it is stated.

## 1. Cyclic transversal criterion

Let n be coprime to 6, v=n+2, and X=Z_n∪{u,w}. Translation fixes u,w. Every orbit on unordered triples has length n. Indeed, a stabilizer is a subgroup of Z_n acting faithfully on a triple: a nonidentity translation fixes no finite point, whereas every triple contains at least one finite point. Thus its order divides both n and 6, so is 1.

Consequently there are `binom(n+2,3)/n=(n+2)(n+1)/6` triple orbits. If a KTS(v) B contains exactly one representative of every orbit, its n translates are pairwise disjoint and cover all triples, with the translated resolutions. Conversely, a large set which is a single free translation orbit of a base KTS has this transversal property.

The pair {u,w} belongs to one block `{u,w,x}` of B. Translating B makes x=0 without loss of generality. For each infinity u, the other `(n−1)/2` blocks through u have the form `{u,a,b}` and use every nonzero finite point once. The translation orbit of such a block is determined by the unsigned nonzero difference `{b−a,a−b}`. Transversality therefore makes those differences occur exactly once. In a resolution, the unique class containing `{u,w,0}` is class 0, and every other class can be labelled by the unsigned difference of its u-block. This proves the class labelling in `work/search_cyclic.py` is lossless within the cyclic model.

In the multiplier model, multiplication by a unit a fixes both infinities and sends a class labelled d to the class labelled `min(ad mod n,−ad mod n)`. Exact-cover rows are full orbits of (block,class) placements. A repeated pair, triple-orbit, or (class,point) column within a row makes that row impossible. Choosing disjoint rows covering all columns is exactly an invariant resolved transversal KTS, not a relaxation.

## 2. Negation fixing both infinities is impossible

Suppose n>1 is odd and the base transversal STS is invariant under `x↦−x`, fixing u,w. For a block `{u,a,b}`, negation preserves its translation orbit (the unsigned difference is unchanged). Transversality forces the negated block to equal the original block. Neither a nor b is 0, because `{u,w,0}` already covers {u,0}. Thus b=−a. The blocks through u consequently contain *all* pairs `{a,−a}` of nonzero finite points. The identical argument for w repeats every such finite pair, contrary to the STS property. Hence this symmetry is impossible even without resolvability.

## 3. The seven-point fixed-subsystem obstruction

Let a multiplier automorphism of a cyclic transversal STS fix exactly m finite points, where m divides n. Its fixed set is `H∪{u,w}`, where H is the subgroup of Z_n of size m. For any pair of fixed points, uniqueness of its completing block forces its third point to be fixed. Thus the fixed set carries an STS(m+2). Its blocks are still transverse to H-translation orbits, because H-translates are also Z_n-translates. When m is coprime to 6, counting as in §1 gives a cyclic large set of **STS**(m+2); no resolvability of this subsystem is asserted.

There is no such cyclic transversal STS on Z_5∪{u,w}. Normalize `{u,w,0}`. The u-blocks must pair {1,2,3,4}, with the two distinct unsigned differences 1 and 2. Its three perfect matchings are:

1. `{1,2},{3,4}`: differences 1,1;
2. `{1,3},{2,4}`: differences 2,2;
3. `{1,4},{2,3}`: differences 2,1.

Only the third is possible. The w-blocks are forced to use the same matching, repeating finite pairs. Contradiction.

Therefore any proposed multiplier group with an element having exactly five fixed finite points is impossible. This proves, for example:

- n=55, multiplier 21: `gcd(21−1,55)=5`, impossible.
- n=85, multiplier 16: `gcd(16−1,85)=5`, impossible.
- n=85, multiplier 4: its square is 16, so also impossible.

This explains a genuine obstruction in the `multiplier87-a4` search independently of trusting the solver's INFEASIBLE result.

## 4. Classical reverse-STS corollary at order 87

**Corollary at its full proved strength:** no STS(87), on any labelled point set, admits an involutory automorphism with exactly one fixed point. This is the classical reverse-Steiner-triple-system necessary condition, not a new exclusion limited to our cyclic search. The Doyen–Rosa line is recorded by [Doyen1972, DOI10.1016/0012-365X(72)90038-6](https://doi.org/10.1016/0012-365X(72)90038-6) and [Rosa1972, DOI10.1016/0012-365X(72)90061-1](https://doi.org/10.1016/0012-365X(72)90061-1) (metadata opened); the spectrum is explicitly stated in the opened Hartman–Hoffman primary abstract cited below. A self-contained proof of the needed necessity follows.

Suppose an STS(v) has an involutory automorphism with exactly one fixed point 0 and m=(v−1)/2 transposed point-pairs. Every transposed pair completes with 0, so these are exactly the blocks through 0. Every remaining block contains points from three distinct transposition pairs, and it is paired with its image.

Label the two points in each transposition pair by bits 0,1. An orbit of two remaining blocks determines a triangle on three pair-indices. Label each of its edges by the xor of the endpoint bits in one representative block; complementing all three bits leaves those edge labels unchanged. A triangle has 0 or 2 edges labelled 1.

For every two pair-indices, their four point-pairs form two involution-orbits, one of xor 0 and one of xor 1. The STS property covers both exactly once. Thus across all triangle orbits the number of edges labelled 1 is `binom(m,2)`. Since each triangle contributes an even number, `binom(m,2)` must be even, equivalently m≡0 or 1 modulo 4.

For v=87, m=43 and `binom(43,2)=903` is odd. Contradiction. In particular, the symmetry `x↦−x` on Z_85 swapping u,w (one fixed point) cannot stabilize a base STS(87), regardless of how it acts on the resolution. For v=15 the same obstruction has m=7 and binom(7,2)=21; for v=57, m=28 and 378 is even, so this test gives no obstruction.

This necessary condition agrees with the known reverse-STS spectrum stated by Hartman and Hoffman, *Steiner Triple Systems with an Involution*, DOI [10.1016/S0195-6698(87)80045-8](https://doi.org/10.1016/S0195-6698(87)80045-8). The primary author's page, opened 2026-10-14, states existence iff v≡1,3,9,19 mod24 for the one-fixed-point case: https://research.ibm.com/publications/steiner-triple-systems-with-an-involution . The elementary necessity argument above does not rely on that existence theorem.

## 5. The three 19-cycles action at order 57

Consider C_19 acting freely on three point-orbits of size 19. Suppose it acts on a resolved LKTS(57), preserving the set of KTS constituents and their chosen resolutions. Let f be the number of constituents fixed by C_19. The other constituent orbits have size 19, so `55−f` is divisible by 19: f∈{17,36,55}.

A fixed constituent has 28 parallel classes. Their C_19-orbits have sizes 1 or 19, hence at least 9 classes are fixed. An invariant parallel class consists of 19 blocks. No triple can be fixed by a nonidentity element of C_19, so that class is a single block orbit. To cover each of the three point-orbits once, its seed block must contain exactly one point in each orbit. It therefore consumes 19 transversal triples.

There are exactly `19^3=6859` transversal triples in all. Disjointness of the KTSs gives `19·9·f≤6859`, hence `f≤floor(19^2/9)=40`. Therefore **f is 17 or 36, never 55**. A search forcing all 55 constituents and their resolutions to be C_19-invariant is impossible. A valid C_19-invariant LKTS would need either (i) 36 fixed constituents and one free orbit of 19, or (ii) 17 fixed constituents and two free orbits of 19.

This proof assumes invariant chosen resolutions of fixed constituents. A block-set automorphism need not preserve a chosen resolution; the stronger unrestricted claim is not made.

## 6. A fixed-class obstruction to order-four multipliers

Suppose a point permutation g has only cycles of lengths 1 and 4 and preserves a parallel class P. The block of P through any g-fixed point must be fixed setwise. Its other two points cannot be in a length-4 point orbit: a setwise fixed triple through a fixed point can only permute its other two points in cycles of length at most 2. Thus every fixed point lies in an all-fixed triple of P. The number of fixed points must be divisible by 3.

In the cyclic base setting, a multiplier fixing both infinities fixes the block `{0,u,w}`, hence fixes its unique parallel class whenever the resolution is invariant. Multiplication by 12 on Z_55 has 11 fixed finite points and eleven 4-cycles (it is 2 mod5 and 1 mod11). Including u,w gives 13 fixed points, not divisible by 3. Therefore the order-four multiplier-12 model for LKTS(57) is impossible. Similarly multiplication by 52 on Z_85 is 2 mod5 and 1 mod17: it has 17 fixed finite points and seventeen 4-cycles. Its 19 fixed points also contradict divisibility by 3. This excludes that order-four model for LKTS(87), not the order-two multipliers 34 and 69, respectively.

## 7. Fixed-point divisibility for an invariant KTS resolution

**Lemma.** Let an involution preserve both the blocks and a chosen resolution of a KTS(v), and have f≥1 fixed points. If c parallel classes are fixed, then

`2cf = f(f−1)+(v−f) = f²−2f+v`.

In particular, **f divides v**.

**Proof.** The fixed points carry an STS(f), because the completing third point of any fixed pair is fixed. There are f(f−1)/6 wholly fixed blocks. Every transposition pair `{x,g(x)}` completes with a fixed point, giving exactly (v−f)/2 other setwise fixed blocks. These are all the fixed blocks, since an invariant triple has either three fixed points or one fixed point and a transposition pair. Every fixed block lies in a fixed parallel class: the resolution partitions the block set and is invariant. Conversely, in a fixed parallel class the unique block through any fixed point is fixed. Counting fixed-point incidences over fixed blocks gives `cf = 3f(f−1)/6+(v−f)/2`. Rearranging proves the identity and divisibility. This argument includes f=1 and does **not** assume that arbitrary block-set automorphisms preserve some resolution. ∎

This divisibility conclusion is not established from block-set invariance alone.

For the previously unresolved involution searches:

- multiplication by 34 on Z_55 fixes 11 finite points and both infinities, so f=13; 13 does not divide 57;
- multiplication by 69 on Z_85 fixes 17 finite points and both infinities, so f=19; 19 does not divide 87.

Thus both invariant-resolution models are impossible **by this proof**, even though the bounded CP-SAT runs returned UNKNOWN. The solver result is not retrospectively changed to INFEASIBLE.

If f=1, the formula gives c=(v−1)/2: all parallel classes must be fixed. Thus the reflection encoding with negation swapping the infinities captures every resolution invariant under that reflection, not merely a selection of its possible class actions. Requiring such an invariant resolution remains a restriction on the original LKTS problem.

## 8. All nonidentity scalar multipliers are excluded at 57 and 87

Here "multiplier" means `x↦a x` on Z_n with both infinities individually fixed, preserving the base KTS **and its chosen resolution** in a cyclic-transversal large set.

For n=55, the Chinese remainder isomorphism gives `U(55)≅U(5)×U(11)`, of order 40 and exponent 20. Its nontrivial involutions are 21,34,54, with respectively 7,13,3 fixed points on the full 57-point set. Section 7 excludes 21 and 34 since neither 7 nor 13 divides 57. Section 2 excludes 54=−1. Every even-order multiplier has one of these as a power, and is therefore excluded.

The only possible nontrivial odd order is 5. Such a multiplier is 1 modulo 5 and has order 5 modulo 11. It fixes exactly five finite points and the two infinities; all other point cycles have length 5. The unique block `{r,u,w}` through the infinity pair is setwise fixed, so its parallel class is fixed. This uses no normalization of r. A block through a fixed point in this fixed class must be setwise fixed. Its two other points cannot move in a 5-cycle, so all its points are fixed. Consequently the seven fixed points would be partitioned into triples, impossible. This excludes all remaining nonidentity multipliers modulo 55.

For n=85, `|U(85)|=4·16=64`, so every nonidentity multiplier has even order. The nontrivial involutions are 16,69,84, with respectively 7,19,3 fixed points on the full 87-point set. Section 7 excludes 16 and 69 since neither 7 nor 19 divides 87; Section 2 excludes 84=−1. Their powers exclude every nonidentity multiplier.

**Conclusion:** the multiplier-invariant-resolution cyclic ansatz has no solution at either target. This does not exclude a base KTS with only identity multiplier, a multiplier preserving its blocks but not an invariant chosen resolution, a reflection swapping the infinities at 57, or any noncyclic LKTS. Finite arithmetic is independently reproducible with `python3 work/screen_symmetries.py`; the mathematical proof is the argument above, not a solver timeout.

## Scope

The positive results in this directory are verified small-case certificates. The arguments above eliminate selected symmetry choices and justify exact encodings. They **do not construct LKTS(57) or LKTS(87)** and do not resolve the book's universal existence problem.
