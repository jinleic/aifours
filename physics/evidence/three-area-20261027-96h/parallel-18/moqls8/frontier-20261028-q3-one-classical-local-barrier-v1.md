# Four-family q3: actual local support budget and one unresolved net

**WRITTEN local lemma; one bounded support computation UNKNOWN.** This concerns an actual order-8 four-MOQLS family with exactly one classical member L and three nonclassical members Q,R,S. It is not the different, previously considered five-family q3 question.

Independently normalize each member's actual first-row basis to the common label set `e_0,...,e_7`, and normalize the classical L symbol in first-row column j to j. At any off-first-row cell (i,j), the supports of Q,R,S all avoid j by their own column ONBs and also avoid L(i,j) by product orthogonality with the corresponding first-row classical-symbol partner. The two labels differ because L is Latin. Actual pair-product orthogonality between any two of Q,R,S, compared to the products at first-row cells, makes their three support sets pairwise disjoint. Therefore

`1 ≤ |S_Q|, |S_R|, |S_S| ≤ 4`, and `|S_Q|+|S_R|+|S_S| ≤ 6`.

The vectors and phases are arbitrary complex. In particular, if all three supports at a cell have size at least two, their sizes are exactly `(2,2,2)`; if one support has size four, the other two are singletons. These are necessary local consequences only, not a global no-q3 theorem or an existence claim.

For a concrete diagnostic, L is the first Latin square of the pinned source excerpt `frontier-20261028-source-wanless-max2-first-pair-v1.txt`, SHA256 710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd. The bounded Boolean relaxation `frontier-20261028-q3-one-classical-support-relaxation-v1.py`, SHA256 c28e362b472f9af136199cc54aa60a1d901e88f567526a493ff212cf6e73be00, retains nonempty/disjoint supports, coordinate coverage and same-line no-singleton intersections; it can additionally reject actual cross-member singleton-product collisions and odd two-axis phase cycles. Its first solver query timed out before any model or added cut. Receipt `frontier-20261028-q3-one-classical-support-relaxation-v1.json` SHA256 bd42f0f4049fa4098056ec159f83d46053a250d63c8f7c1c9a38e6c8a6af2cd: **UNKNOWN**, not SAT/UNSAT, no physical or support witness.

A separate known four-classical-family control checks all 4,096 original row/column and 24,576 pair-product Gram entries and the stated support necessary conditions, then rejects a duplicate-cell mutation. `frontier-20261028-q3-support-physical-control-v1.py` SHA256 44af562305bb1ce9839b3c76696957d28e64fa4844c2582d0d94bc7cd8481f14; receipt SHA256 48ca9a2bbd3a9cdf23e8bf4a9be3a69be3b54c90b6fe371af9a25620c7c9122f. This is not a q3 family.

**Exact remaining gap:** determine whether the local support budget, all three net-line ONBs, the three cross-member product ONBs and compatible complex amplitudes can coexist for any one-classical four-family. The two-classical q1/q2 catalogue-conditional candidates do not decide this q3 case, and the bounded failure is not an exclusion.
