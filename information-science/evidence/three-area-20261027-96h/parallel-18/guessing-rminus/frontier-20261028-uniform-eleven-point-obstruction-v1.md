# Uniform FD laws on at most eleven words cannot have a strict balance gap

**Status: WRITTEN with exact integer entropy comparisons, conditional on the pinned graph-FD inequality; scientific review and novelty clearance pending.** A **uniform** law on at most 11 joint support words satisfying the original R-minus FDs has `Delta<=0`. This concerns arbitrary finite alphabets and support sets, not only group-coset laws. It is not an unrestricted guessing-number upper bound; a strict finite guessing strategy already has more than 101 fixed words by its definition when the alphabet has size at least 2.

## Preliminary gates

Assume instead `Delta>0` on `m` equally likely words. The conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` makes all ten coordinates nonconstant and gives `2I(X_i;X_j)<H(X_i)` for every distinct `i,j`. Put `h_k=h_2(k/m)`.

Any nonconstant coordinate has entropy at least `h_1`. Call a coordinate a **singleton indicator** if its support partition is `1+(m-1)`. Two singleton indicators cannot isolate the same word because they would determine one another. Any other nonconstant partition has entropy at least `h_2`: it can be coarsened to a binary partition with both block sizes at least 2.

For `m=10,11`, a singleton-indicator word cannot lie in a block of size 1 or 2 of any other coordinate. Size 1 would make the other coordinate determine the indicator. For size 2, uniformity gives `H(indicator|other)=2/m`, so `2I>=H(indicator)` because `h_1>4/m`; this contradicts the strict mutual-information gate. The two inequalities `h_2(1/m)>4/m` are checked by exact integer powers in the evidence below.

R-minus is `K4`-free. If several singleton-indicator words have the same values at every non-indicator coordinate, their corresponding indicator vertices form a clique: any two such words differ at exactly those two indicator vertices, and the graph FD forces those vertices to be adjacent. Hence each such signature class has size at most 3. A non-indicator coordinate that **separates** two indicator words has at least two blocks containing indicators, each of size at least 3; its entropy is at least `h_3`. If it has at least three indicator-containing blocks when `m=11`, its entropy is at least the entropy of block sizes `(5,3,3)/11`: merging other blocks and transferring mass to the largest block cannot increase entropy.

## Support sizes at most 9

For every `2<=m<=9`, exact integer comparison gives `10h_1 >= (3/2)log2 m`. Since all ten variables are nonconstant, `sum_i H(X_i) >= (3/2)H(X_V)`, contradicting `Delta>0`. The case `m=1` is trivial.

## Ten words

Let `r` be the number of non-indicator coordinates. The exact comparison `8h_1+2h_2 >= (3/2)log2 10` gives `r<=1`. If `r=0`, all ten indicator vertices form a clique. If `r=1`, the nine indicator words cannot all have the same signature because R-minus is `K4`-free, so the non-indicator coordinate separates some of them and has entropy at least `h_3`. But `9h_1+h_3 >= (3/2)log2 10`, again a contradiction.

## Eleven words

The exact comparison `6h_1+4h_2 >= (3/2)log2 11` gives `r<=3`. If `r=3`, `7h_1+2h_2+h_3 >= (3/2)log2 11`, so none of the three non-indicators can separate indicator words; their seven indicator vertices form a forbidden clique. If `r=0`, the indicator vertices also form a forbidden clique.

If `r=2`, the exact comparison `8h_1+2h_3 >= (3/2)log2 11` permits at most one separating coordinate. If `r=1`, there is at most one automatically. In either case a separating coordinate is necessary, and it must place the eight or nine indicator words in at least three blocks to keep every signature class at size at most 3. Its entropy is at least `H(5/11,3/11,3/11)`. The exact comparisons

\[
9h_1+H(5/11,3/11,3/11)\ge\tfrac32\log_2 11,
\qquad
8h_1+h_2+H(5/11,3/11,3/11)\ge\tfrac32\log_2 11
\]

contradict `Delta>0` for `r=1` and `r=2`, respectively. All possibilities are excluded.

## Exact evidence

`frontier-20261028-uniform11-entropy-check.py` SHA-256 `874a54c940a5bf1bddd9da003f42ccacf49792a194a31185fcb9d20452ab2ca8`, receipt SHA-256 `09b7934be56ccd7c41b0694981bab6d2d4a2325724c4d8706005a6e92327f93d`, checks all 15 entropy comparisons by raising positive integers to exact integer powers, checks the two mutual-information threshold inequalities, pins the independent `K4`-free graph receipt, and rejects a deliberately false `m=10` comparison. Partition and FD deductions above are written arguments, not proof-assistant formalization or independent scientific review. The result is restricted to uniform laws and makes no novelty claim.
