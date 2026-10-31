# A two-heavy-atom obstruction for arbitrary FD laws

**Status: WRITTEN, conditional on the pinned exact conditioned graph-FD inequality; scientific review and novelty clearance pending.** Let a finite original-neighbour R-minus FD law have joint support of size `m>=3`. Pick two distinct support words `u,v`, with probabilities `p_u,p_v`, and set `epsilon=1-p_u-p_v<=1/2`. If

\[
2h_2(p_v)\ge 1+5h_2(\epsilon)+\epsilon\log_2(m-2),\tag{11}
\]

then its balance gap `Delta=H(X_V)-(2/3)sum_i H(X_i)` is nonpositive. Here `h_2` is binary entropy and the tail term is interpreted as zero when `epsilon=0`. Thus any strict-gap law must violate (11) for **every** pair of support words.

A concrete sufficient condition is: if `m<=1026`, the two words together carry at least `99%` of the probability, and each has probability at least `2/5`, then `Delta<=0`. This applies to arbitrary alphabets and probabilities, not just group or uniform laws. It does not give a global guessing-number bound.

## Proof

The pinned conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` implies that `Delta>0` requires `2I(X_i;X_j)<H(X_i)` for every distinct pair of coordinates.

Two distinct support words differ in at least two coordinates: if only coordinate `i` differed, all its original neighbours would agree and the FD at `i` would be violated. Choose any two differing coordinates `i,j`. Let `B` be the indicator of the event `X_V=v`. From either `X_i` or `X_j`, one can predict `B` correctly on the two heavy words, so the prediction error is at most `epsilon`. For a binary variable this implies

\[
H(B\mid X_i),\ H(B\mid X_j)\le h_2(\epsilon).
\]

Indeed, given a decoder and its binary error indicator, `B` is determined; the error indicator has entropy at most `h_2(epsilon)`. The Shannon identity

\[
I(X_i;X_j)\ge H(B)-H(B\mid X_i)-H(B\mid X_j)
\]

then yields `I(X_i;X_j)>=h_2(p_v)-2h_2(epsilon)`. On the other hand, conditioning on whether the support word is in `{u,v}` gives

\[
H(X_i)\le H(X_V)\le 1+h_2(\epsilon)+\epsilon\log_2(m-2).
\]

Condition (11) implies `2I(X_i;X_j)>=H(X_i)`, contradicting the strict-gap consequence of the conditioned inequality.

For the stated numerical region, both heavy probabilities at least `2/5` imply `p_v` lies in `[2/5,3/5]`, so concavity gives `h_2(p_v)>=4/5`. For `epsilon<=1/100`, monotonicity gives `h_2(epsilon)<9/100`: indeed `log2 100<7` and `(1+1/99)^99<3<4`, so `100 h_2(1/100)<7+2=9`. Also `log2(m-2)<=10` for `m<=1026`. Thus the left side of (11) is at least `8/5`, while the right side is less than `1+45/100+10/100=31/20`, and (11) holds.

Only the stated graph-FD inequality, elementary Shannon identities and entropy concavity are imported. No proof-assistant formalization, scientific review, or novelty claim is made.
