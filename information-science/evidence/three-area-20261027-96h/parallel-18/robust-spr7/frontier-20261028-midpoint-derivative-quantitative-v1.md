# Quantitative negative coefficient in the midpoint-derivative basis

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For every box \(K'\) in the endpoint neighborhood of `frontier-20261028-midpoint-derivative-cone-open-obstruction-v1.md`, let \(m'\) be its monic midpoint. Every monic common SPR numerator has a unique expansion
\[
b=\sum_{k=0}^7c_kD^km',\qquad c_0=1,
\]
and at least one coefficient satisfies
\[
\boxed{\quad c_k<-1/160\quad\text{for some }1\le k\le7.\quad}
\]
The basis is triangular because \(\deg D^km'=7-k\). The bound depends on the monic normalization and the variable's scale. A common unrestricted numerator does exist for every such box, by the referenced neighborhood theorem.

For the four positive atoms of the preceding cone packet, write \(S'_k=-F_{K'}(D^km')>0\). Common SPR gives
\[
0<F_{K'}(b)=-S'_0-\sum_{k=1}^7c_kS'_k.
\]
If all \(c_k\ge-1/160\), the right-hand side is at most
\(-S'_0+(1/160)\sum_{k=1}^7S'_k\), which is strictly negative. The needed strict inequality follows from the previously pinned anchor sums \(S_k\), perturbation bounds \(A_k\) and \(\varepsilon=10^{-14}\):
\[
S_0-\varepsilon A_0>\frac1{160}\sum_{k=1}^7(S_k+\varepsilon A_k).
\]
The independent checker recomputed this exact inequality together with the anchor and neighborhood calculations. It does not assert an all-numerator negative certificate; the negative coefficient is a necessary condition on numerators which may nevertheless exist.

Frozen input: `frontier-20261028-midpoint-derivative-quantitative-frozen-v1.json`, SHA-256 `fe4b1db0b849ef6b59714ec732a4294e51c3e97dbed4a5a0f8293f384a3055e8`. Independent checker `frontier-20261028-midpoint-derivative-quantitative-independent-kernel-v1.py`, SHA-256 `ad8de8db4c8826289e3452a7ac053f4b9cce2f5eee04102572d0911fe03276f5`; receipt `frontier-20261028-midpoint-derivative-quantitative-independent-result-v1.json`, SHA-256 `0dd2114272c6bd8b0e251ac4180a285dfb156b001c85149ea126be149b737a1f`. The preceding cone theorem is SHA-256 `042cf303f487563577553675d8b5b35301fe91c763658155ffee8ece27df74e4`.

All finite arithmetic used integers and `fractions.Fraction` on one Python Eval host. The basis and inequality deductions are written mathematics; no formal verification, cross-vendor review, novelty clearance or universal arbitrary-box verdict is claimed.
