# An external q=8 word forces at least 68 deletions from the triangle code

**Status: WRITTEN with independently replayed exact generator/projection counts; scientific review pending.** Fix the component-bit encoding of the standard ten-triangle R-minus code `W0` over a common eight-symbol alphabet. It has `|W0|=2^20=1,048,576` words. Every word `w` outside `W0` conflicts, in the original-neighbour guessing confusability graph, with at least **68 distinct** words of `W0`.

Consequently, any original-FD-consistent q=8 support containing a word outside `W0` must omit at least 68 `W0` words. The code is maximal: it cannot be enlarged by adding even one word. In particular, any q=8 fixed-point set strictly larger than `2^20` must remove at least 68 old words **and add at least 69 new words**, in this fixed alphabet labeling. These are finite-support trade constraints, not a proof that such a replacement is impossible or a numerical improvement on the inherited unrestricted bound.

Together with the global product-support theorem `frontier-20261028-triangle-code-global-obstruction-v1.md` SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`, this also means that any q=8 **positive-gap law**, whether uniform or not, must use an outside word and omit at least 68 `W0` words. Both statements require the fixed factor-bit correspondence of the alphabet; they make no claim about edit distance after choosing different labelings.

## Proof

Each of the ten listed triangle factors supplies an XOR-zero triple, and each vertex participates in exactly three factors, giving its three-bit q=8 symbol. R-minus is `K4`-free. Thus for every vertex `i`, no factor triangle is contained entirely in `N(i)`: such a triangle together with `i` would be a `K4`. In a binary XOR-zero triple, any one or two selected bits range freely and uniformly. Therefore every tuple of all `3 deg(i)` neighbour bits occurs among `W0` words, and each such neighbour fiber has exactly

\[
2^{20-3\deg(i)}
\]

words. The degree is 6 at vertices 1 and 8 and 5 at the other eight vertices, so the fiber sizes are respectively 4 and 32.

Since `w` is not a codeword, at least one factor triangle `T` has nonzero XOR syndrome. For each `i in T`, consider the `W0` fiber matching `w` on `N(i)`. The other two vertices of `T` lie in `N(i)`, so in every word of that fiber the parity constraint forces the factor bit at `i` to disagree with `w`. Thus all words in the fiber conflict with `w` at vertex `i`.

The three fibers for vertices of `T` are pairwise disjoint. If `i,j in T` are distinct, then they are neighbours; a word in the fiber for `i` agrees with `w` at `j`, while a word in the fiber for `j` disagrees with `w` at `j`. Each triangle contains at most one of the degree-six vertices 1 and 8, since those two are not adjacent. The three disjoint fibers therefore contain at least `4+32+32=68` old words (or 96 if all three degrees are five). Every FD-consistent support containing `w` must exclude all of them.

If a q=8 fixed-point set has more than `2^20` words, it contains an outside word, so the preceding argument removes at least 68 old words; strict cardinality then requires at least 69 outside words. This does not multiply the 68 bound by the number of added words, since different outside words' conflict sets may overlap.

## Exact evidence

`frontier-20261028-triangle-neighbor-fibers-check.py` SHA-256 `7a4cd6c06084282cfc940bd20ce14e145c4d61c1cf3ac9cfdc8b1f8f68e8e168`, receipt SHA-256 `09165f77dc480be2463290cb532da5d8fed04a366404f86a3edb6327af1156a7`, builds the 20-bit triangle generator and checks the 10 neighbour projection ranks by exact binary Gaussian elimination. Independent factorwise projection checker `frontier-20261028-triangle-neighbor-fibers-independent.py` SHA-256 `f73c2d55434abbb54f21a7d6ec25eeb7fa6d2d907864adbb0a001fbafaad65bc`, receipt SHA-256 `9000c1afc5dc4c9cb0986b15596d23ff8120b56edb0831709be663757e950e5f`, independently checks all per-factor projection sizes, all ten fiber counts and all ten triangle bounds. The checks include intended invalid-rank/added-K4-edge controls. The conflict-set argument above is written mathematics, not a proof-assistant formalization or an independent scientific review.
