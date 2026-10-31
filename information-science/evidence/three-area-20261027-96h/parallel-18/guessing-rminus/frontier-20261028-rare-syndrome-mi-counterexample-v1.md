# The tempting syndrome-information lower bound is false

**Status: WRITTEN with exact fiber and integer-margin checks; scientific review pending.** The syndrome inequality `frontier-20261028-syndrome-entropy-gate-v1.md` SHA-256 `2efc6640f4551bcad35ea3678737aa0242e0d85921846134166b9c7f59a98b81` would imply `Delta<=0` if every q=8 graph-FD law obeyed `sum_i I(X_i;S)>=(3/2)H(S)`. That proposed lower bound is **false**, even for an explicit finite original-neighbour R-minus FD law. This is a counterexample to a proof route, **not** a strict-gap law: the law below in fact has `Delta<0`.

## The law

Use the standard 2^20-word triangle code `W0` in its fixed q=8 bit labeling. Let `w` be the word obtained from zero by flipping the factor-1 bit at vertex 1. By the sharp trade result `frontier-20261028-triangle-trade-sharpness-v1.md` SHA-256 `69d2df12669da61f3b5e07f1a58318079b75de9e565cec55fd638c0e9c08130f`, exactly 68 old codewords conflict with `w`; remove all of them. The remaining `M=2^20-68=1,048,508` old words together with `w` form an original-FD-consistent support. Give `w` probability `p=2^-128` and, conditional on not choosing `w`, choose an old word uniformly.

The ten-bit syndrome `S` is zero on old words and has the single nonzero factor-1 syndrome on `w`, so it is equivalent to the binary outsider indicator. Every symbol of each old singleton marginal has probability greater than `1/9`: the uniform old code had `2^17` instances of each symbol, and at most 68 were removed. The exact fiber/marginal checker below verifies the counts.

## Failure of the proposed lower bound

Use natural logarithms. Let `q_i` be the old conditional probability of `w_i`, and let `P_i` be the mixture singleton marginal. Relative-entropy convexity gives

\[
I(X_i;S)=(1-p)D(P_i^0\Vert P_i)+pD(\delta_{w_i}\Vert P_i)
\le-\log(1-p)-p\log q_i < 5p,
\]

using `q_i>1/9`, `-log(1-p)<=2p` for `p<=1/2` and `log 9<3`. Thus `sum_i I(X_i;S)<50p`. Meanwhile `H(S)>=p log(1/p)=128(log 2)p>64p`, so

\[
\frac{\sum_i I(X_i;S)}{H(S)}<\frac{25}{32}<\frac32.
\]

For the same fixed support with outsider probability tending to zero, the ratio tends to zero. Therefore the syndrome-information lower bound cannot be used without additional hypotheses, although the always-valid inequality from the cited syndrome packet remains true.

## The law does not have a strict gap

Let `P_old` be uniform on the `M` remaining old words, and `U8` the uniform singleton law. Since `2^20=8^(20/3)`,

\[
\Delta(P_{\rm old})=\log(M/2^{20})+\frac23\sum_i D(P_i^0\Vert U8).
\]

Each singleton probability differs from `1/8` by at most `68/M`, and `D(q||U8)<=8 sum_a(q(a)-1/8)^2`. Hence

\[
\Delta(P_{\rm old})\le-\frac{68}{2^{20}}+\frac{1280}{3}\left(\frac{68}{M}\right)^2
<-\frac{68}{2\cdot2^{20}},
\]

where the last comparison is checked by integers. Entropy concavity and the disjoint-support mixture identity give `Delta(P)<=(1-p)Delta(P_old)+h(p)`. For `p=2^-128`, `h(p)<130p<68/(4*2^20)`, while `1-p>1/2`; the exact checked margins show `Delta(P)<0`.

## Exact evidence

`frontier-20261028-rare-syndrome-counterexample-check.py` SHA-256 `262081a2b13a22dcbb09054531ef40334d80f1f9a7a93b477f2141587cc75a7c`, receipt SHA-256 `88781d264e4b4666f3d92747f5ba2203a8f05796e9ecac307e7424f73c846e0f`, constructs and checks the three disjoint fibers, their 68 words, and all old singleton marginal counts. `frontier-20261028-rare-syndrome-gap-check.py` SHA-256 `371d0656fa6faca4eac2e97154387cded7499fa492c70e06ce9abaab896403cb`, receipt SHA-256 `392f9a64e8a9da10c5c7bfac89159c74ff8335cb609d3dec19c041acb0e0e30e`, checks the coarse old-gap and mixture margins using integers. Their mutation controls check a missing fiber word and an overly large outsider weight. The entropy estimates and FD-support argument are written, not proof-assistant formalization or independent scientific review.
