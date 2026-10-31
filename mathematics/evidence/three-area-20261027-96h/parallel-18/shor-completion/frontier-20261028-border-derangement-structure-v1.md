# Shor completion: two forced permutations on the new border heads

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:59:17 PDT 2026**.
**WRITTEN all-order structure of the actual border factorization; no construction, complete no-go, novelty clearance or formal review.**

## 1. Statement

Let D be any finite UD factor-complete extension of the literal Shor S, and take its actual direct border factorization `P+Q=Z_n`, `n>=26`, with

    A={0,3,8,11} subset P,       {0,1,7,13,14} subset Q.

The same-D factorization is proved from actual words in `frontier-20261028-six-head-border-factorization-v1.md`; it is also a known prior theorem. Let `E=P\A` and `m=|E|`. There exist two UNIQUE permutations

    pi_4, pi_10 : E -> E,

both without fixed points, such that for every `x in E`

    x-pi_4(x)+4 in Q,       x-pi_10(x)+10 in Q.                (1)

Uniqueness means that these are the unique sources supplied by the SAME direct tiling, not a choice among arbitrary matching models. The individual Q-elements in (1) for different x need not be distinct; no such assertion is made.

In particular, when `|P|=8`, E has four elements and each permutation has cycle type either a four-cycle or two disjoint transpositions. These two cases are a complete structural split for the as-yet-unresolved eight-head border branch. The previously written `|P|>=8` bound does not prove that branch feasible.

Summing (1) as multisets in Z_n also gives

    sum_x (x-pi_4(x)+4) = 4m,
    sum_x (x-pi_10(x)+10) = 10m.                               (2)

These are identities, not a claim that Q has m new distinct elements.

## 2. Proof for offset4

Fix `x in E`. In a representation of target `x+4`, each old source `a in A` and the source x itself would require the following forbidden Q-element:

| source in P | candidate in Q | directness collision with an old Q-anchor |
|---|---|---|
| 0 | x+4 | (x+4)+3=7+x |
| 3 | x+1 | (x+1)+0=1+x |
| 8 | x-4 | (x-4)+11=7+x |
| 11 | x-7 | (x-7)+8=1+x |
| x | 4 | 4+0=1+3 |

In each equality the two P-elements are distinct, since x lies outside A. Coverage and directness therefore give exactly one source `y in E\{x}`, defining `pi_4(x)=y` and forcing `x-y+4 in Q`.

If two distinct x,x' had the same image y, their forced Q-elements `x-y+4` and `x'-y+4` would be distinct, and

    (x-y+4)+x' = (x'-y+4)+x

would contradict directness. Thus pi_4 is injective; E is finite, so it is a permutation. It has no fixed point by construction.

## 3. Proof for offset10

For target `x+10`, the analogous old and self-source candidates are all forbidden:

| source in P | candidate in Q | directness collision |
|---|---|---|
| 0 | x+10 | (x+10)+3=13+x |
| 3 | x+7 | (x+7)+0=7+x |
| 8 | x+2 | (x+2)+11=13+x |
| 11 | x-1 | (x-1)+8=7+x |
| x | 10 | 10+0=7+3 |

The unique remaining source defines pi_10. The same collision as in §2 proves injectivity, hence pi_10 is a derangement permutation. Formula (2) follows by cancellation over the finite permutation sums.

These implications depend only on the actual direct tiling and old anchors. They do not resolve how pi_4 and pi_10 may coexist with the remaining old-tail anchors, the full one-b layer, multi-b atoms, or factor-completeness.

## 4. Status

All claims here are written elementary equalities; they have not received a separate peer, human, formal/kernel, independent-family or novelty review. The 4-cycle / paired-transposition split covers every hypothetical eight-head border but neither branch is proven realizable or impossible by this packet. The original finite UD factor-completion/noncompletion question remains OPEN.

**END OF BORDER DERANGEMENT STRUCTURE.**
