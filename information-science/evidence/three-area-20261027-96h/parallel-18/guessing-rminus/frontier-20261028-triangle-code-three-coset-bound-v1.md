# Three triangle-syndrome classes cannot beat the q=8 triangle code

**Status: WRITTEN with independently verified exact finite conflict witnesses; scientific review pending.** In the fixed factor-bit encoding of the standard q=8 R-minus triangle code `W0`, any original-FD-consistent support contained in the union of **three** triangle-syndrome classes has at most `2^20` words. Thus a q=8 fixed-point set strictly larger than the triangle code must meet **at least four** distinct syndrome classes.

This strengthens the two-class statement `frontier-20261028-triangle-code-two-coset-bound-v1.md` SHA-256 `deeb3b6722a5ee3c23f6c2957864e169a8ac0f10dc6910df1eab7681f5d868cd`. It is a fixed-label cardinality result, not a nonuniform entropy-gap exclusion or an unrestricted guessing-number bound.

## Conflict triangles tile three classes

The syndrome map is linear on `F_2^30`, has kernel `W0` of dimension 20, and each of its 1,024 fibers is a `W0` coset. Original-neighbour confusability is invariant under ambient bitwise translation. We prove that for every two distinct nonzero syndromes `s,t`, there are words `u,v` with syndromes `s,t` such that `0,u,v` are **pairwise confusable**. Translating these three words by each `x in W0` partitions the three classes into `2^20` disjoint conflict triangles, so any FD-consistent support contains at most one word per triangle.

For vertex `i`, let `A_i` be the three factor indices incident with `i`. If `s intersect A_i` and `t intersect A_i` are both nonempty and unequal, representatives `u,v` can both be chosen with all neighbour symbols at `i` equal to zero. Their symbols at `i` are precisely their respective three incident syndrome bits, hence are nonzero and distinct; `0,u,v` are pairwise confusable at `i`. The representatives exist because R-minus is `K4`-free: no factor triangle is entirely in `N(i)`, so for each factor at least one non-neighbour bit can be chosen freely to realize its required syndrome, while in an incident factor the bit at `i` realizes it.

Among the `binom(1023,2)=522,753` unordered nonzero syndrome pairs, the exact checker finds **522,231** covered by this one-vertex construction. For the remaining **522**, the pinned receipt supplies explicit 30-bit words `u,v`; an independent checker verifies their exact syndromes and checks directly from the original graph that each of `u`, `v`, and `u xor v` is a confusable difference. These are actual finite witnesses, not solver claims.

Any three distinct syndrome classes can be translated so that one has syndrome zero; the preceding result applies. The two-class and one-class cases follow by taking subsets of a three-class union or from the preceding packet. Thus any q=8 fixed-point support larger than `2^20` uses at least four classes.

## Exact evidence

Producer `frontier-20261028-syndrome-triple-cliques.py` SHA-256 `11eeeb0001a77b8f5b349064efad909e035107668a9f3060d32fe93ab48d8305`, receipt SHA-256 `a567094dd9a4f7fb9484c8a11a8c7bb2dc0476cb5e7f56499d3c1a6bb15b2004`, records all 522 exceptional witnesses. Separately written `frontier-20261028-syndrome-triple-independent.py` SHA-256 `3e08bef52c325d8d45bb9aedffc6bc3aef972e6e62e82fe051560d8bcc592a80`, receipt SHA-256 `6c254cb53fdbf004ac0c784fb3d5ee3398dacd9a5377a74e7ae972594f17f10b`, independently classifies all 522,753 syndrome pairs, verifies all 522 direct conflict triangles and all 100 factor-neighbour completion conditions, and rejects three intended-reason mutations. The local-construction and clique-factor implications are written mathematics, not proof-assistant formalization or independent scientific review.
