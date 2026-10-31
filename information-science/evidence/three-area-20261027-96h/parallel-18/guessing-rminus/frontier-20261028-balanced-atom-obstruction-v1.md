# A balanced-atom obstruction for arbitrary finite FD laws

**Status: WRITTEN conditional on the pinned original graph-FD inequality; review and novelty clearance pending.** Let `P` be any finite original-neighbour R-minus FD law with at least two positive-probability joint support words. Let `p_min` be the smallest positive word probability. If

\[
H(P)\le \frac{20}{3}h_2(p_{\min}),\tag{12}
\]

then `Delta=H(P)-(2/3)sum_i H(X_i)<=0`. In particular, no strict-gap law can have at most **eight** support words all having probability at least `1/10`. This covers a full positive-measure region of nonuniform six-, seven- and eight-word laws, but not arbitrarily skewed laws and not the unrestricted guessing-number problem.

## Proof

Suppose `Delta>0`. The conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` says every original coordinate is nonconstant. Every nonconstant coordinate has some value whose probability lies between `p_min` and `1-p_min`; merging its other values gives a binary variable with entropy at least `h_2(p_min)`. Thus each singleton entropy is at least `h_2(p_min)`, and strict balance implies `H(P)>(20/3)h_2(p_min)`, the negation of (12).

For the explicit region, `H(P)<=log2 8=3`, and `p_min>=1/10` implies `h_2(p_min)>=h_2(1/10)` because `p_min<=1/2`. The elementary exact integer comparison

\[
10^{20}>2^9 9^{18}
\]

is equivalent to `h_2(1/10)>9/20`; hence `(20/3)h_2(p_min)>3>=H(P)`. This rules out a strict gap. The integer comparison was checked directly in the kernel; the entropy argument is written mathematics and has not received independent scientific review or novelty clearance.
