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

## 4. One-fixed-point involution obstruction at order 87

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

## Scope

The positive results in this directory are verified small-case certificates. The arguments above eliminate selected symmetry choices and justify exact encodings. They **do not construct LKTS(57) or LKTS(87)** and do not resolve the book's universal existence problem.
