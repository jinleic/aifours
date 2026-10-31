# Exact min-cut oracle for the seven residual distance-six cases

**Status: WRITTEN with eight independently verified integer flow/cut certificates; scientific review pending.** The seven unexcluded six-factor two-syndrome cases in `frontier-20261028-two-syndrome-distance5-v1.md` SHA-256 `606e74ea5d7ede9580c217091e240663641d23d43141ac9db49c5b753b0a38df` have an exact reduction from the **joint support-and-weight** search to a finite-dimensional outer weight search with a polynomial-time min-cut inner oracle. This is an actionable reformulation, not a proof of gain or no-gain.

## The oracle

Fix one residual six-factor set `J`, condition on all other factor tuples, and translate the affine syndrome offset to zero. The reduced block has 18 component bits. Its two allowed syndrome classes are `C` and `d+C`, where `C` is the six-triangle XOR code of dimension 12 and each class has `4^6=4096` words. Each class is internally FD-consistent: any nonzero difference in `C` activates at least two vertices of some selected triangle, so every differing vertex has a differing original neighbour.

Build a bipartite graph with one vertex per word in each class, joining cross-class words exactly when they are original-neighbour confusable. Thus original-FD supports in the two-class block are exactly its independent sets. For any nonnegative integer vertex-symbol weights `t[i,a]`, define

\[
w_t(x)=\prod_i t[i,x_i]^2,\qquad
D(t)=\prod_i\bigg(\sum_a t[i,a]^3\bigg)^2.
\]

Let `M(t)` be the maximum `sum_{x in W} w_t(x)` over bipartite independent sets. Compute it exactly as `total_weight - mincut`: connect the source to each left word with capacity `w_t`, each right word to the sink with capacity `w_t`, and every cross-conflict edge left-to-right with a capacity exceeding total finite weight. A minimum cut selects a minimum-weight vertex cover, whose complement is a maximum-weight independent support.

By the pinned Gibbs/integer criterion `frontier-20261028-balance-polynomial-equivalence-v1.md` SHA-256 `70e90a3236d735d74dbd71f68577f97f778e98eafdc49137e30aa4fe36178ec1`, the reduced two-class block has a positive-gap FD law **if and only if** there are integer weights with every row nonzero and

\[
M(t)^3>D(t).\tag{24}
\]

The outer weights remain unbounded and nonlinear; finitely many failed choices do not prove impossibility. Conversely any strict result in (24) gives an explicit reduced FD law. Setting the four other factor components to constants embeds it into the original q=8 graph; the pinned entropy-balancing/type-class reduction would turn its positive gap into a strict unrestricted guessing-number gain. If an original two-syndrome q=8 law with the same difference set has positive gap, conditioning on the other fixed-parity factor tuples produces a positive reduced fiber, as in the distance-five packet. Thus the oracle covers the intended two-class case without requiring uniformity.

## Scope and exact checks

The seven six-factor sets form four orbits under factor-preserving graph automorphisms, with representatives

```text
{1,2,5,6,8,9}     {1,3,4,6,7,10}
{2,3,4,6,7,10}    {2,3,5,6,9,10}
```

Their cross degrees are respectively `60,72,68,74`, so the bipartite graphs have `245,760` to `303,104` conflict edges. `frontier-20261028-sixfactor-residual-orbits-check.py` SHA-256 `96edc2b3887d1d57dcec71cbd946fb56aab41e83085196e2531cc0b9b4558c66`, receipt SHA-256 `ba3ce740c83ba989871e3d3f5bbc57deee864df3c4a9426bc8b93c7cf713e8e4`, checks the orbit coverage.

The exact integer-flow producer `frontier-20261028-two-coset-flow-search.js` SHA-256 `5896325278407560d44d92e5bd5ae72eee54e1c3213bd2e60cf8e0150e373737`, receipt SHA-256 `5c81fde2f95ace2debec5024e8e6f0f47b96e85c72d6e0ff15bf5f1d7036ca13`, saves eight explicit flow, cut and support certificates. Separately written `frontier-20261028-two-coset-flow-independent.py` SHA-256 `73fd66f6e41d8f2a07283ae1cef7b6a312b3b96c68e8c062e193eed458dffa3c`, receipt SHA-256 `7c24b822f0a2b61e98aad9e44c993276cb08f9ad80f0156e3ccd3d603a38d922`, rebuilds each graph, checks code linearity, independent-set support, every positive flow edge/capacity, vertex flow conservation, exact flow=cut, polynomial comparison, and a removed-flow control. None of these eight weights gives a strict witness.

A further 400 selected weights were processed by `frontier-20261028-two-coset-flow-batch.js` SHA-256 `ffa922fafe9cf0c7f91aa69134140a7d6da6928d88587d2365de9b56dbed3097`, receipt SHA-256 `0aac744999c8b4b072b4005a1656010d5e20090d1483ce39999d853c2ebea567`; the implementation checks integer flow conservation and equal cut values internally, but those 400 compact results have not all been independently replayed. No strict witness was found. This is not a global outer-weight bound, independent scientific review, proof-assistant formalization or novelty claim.
