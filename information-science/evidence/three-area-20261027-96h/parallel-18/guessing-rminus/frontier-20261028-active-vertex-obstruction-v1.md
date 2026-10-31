# A strict-gap law needs a non-3-colorable active subgraph

**Status: WRITTEN with independently checked finite graph census; review and novelty clearance pending.** For any finite original-neighbour R-minus FD law, let `S={v:H(X_v)>0}`. If the induced graph `R-minus[S]` is 3-colorable, then

\[
H(X_V)\le\frac23\sum_vH(X_v).
\]

Consequently every strictly positive balance-gap FD law has **at least six nonconstant vertices**. If it has exactly six, the active set must be one of

```
{1,2,3,4,8,9}       {1,2,6,7,8,10}
{1,3,4,5,8,10}      {1,5,6,7,8,9}
```

Each is an induced five-wheel. This restriction is independent of joint-support size, and does not by itself prove or disprove strict gain on any of these active sets.

## Proof

The argument works for any finite loop-free directed dependency graph, using a proper 3-coloring of the underlying undirected graph induced by its nonconstant vertices. Outside `S` every coordinate is constant on the positive-probability support. For two distinct support words `x,y`, their difference set `D` is contained in `S`. If `v` lies in `D`, some neighbour of `v` must also lie in `D`; otherwise the FD at `v` would map equal neighbour values to unequal own values. Thus `D` contains a graph edge and, under a proper 3-coloring, meets at least two color classes.

Let `Y_1,Y_2,Y_3` be the tuples of coordinates in the three classes. Any two `Y`'s jointly distinguish all support words, hence determine the entire joint vector. The three pairwise entropy-subadditivity inequalities give `2 sum_r H(Y_r)>=3H(X_V)`, and `sum_r H(Y_r)<=sum_v H(X_v)`. This proves the bound.

The independent exact checker `frontier-20261028-sparse-coloring-independent.py` SHA-256 `f9060fbf1d3036ee69999512ce872c3db0a669e772d440cd0794c6b07e30bb46` and receipt SHA-256 `5994e7fbec78f4fa864e713438e28d9676a107bf4a5e66df9044fe3103863eb4` replay all **848** induced subgraphs on at most six vertices and find exactly the four non-3-colorable vertex sets listed above, all of size six. Its pinned source census is SHA-256 `75884fb96097853126b328c6308c822a8439bee05c0e94c083e91320e4c3062f`, containing the explicit graph-neighbour lists. This is a combinatorial/entropy obstruction only, not an unrestricted guessing-number upper bound or novelty claim.
