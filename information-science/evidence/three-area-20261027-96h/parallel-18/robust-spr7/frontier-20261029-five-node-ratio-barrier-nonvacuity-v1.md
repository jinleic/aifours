# The five-node geometric barriers are not sufficient

**Status: WRITTEN-checked-in-kernel finite example; not parent adoption.** The root-band and strict-ratio conditions in `frontier-20261029-strict-five-node-ratio-obstruction-v1.md` (SHA-256 `0884bd8e656abc589fd162d290ff9a5aa7d38031fb9b4a9ae5a6bb9b3bc80743`) are genuine restrictions, but they do **not** by themselves yield a negative certificate.

Use the actual full-width stable anchor box from `frontier-20261029-seven-dimensional-span-obstruction-open-v1.md`, with parity-corner numbering \((--),(-+),(+-),(++)=0,1,2,3\). The five increasing actual corner/squared-frequency pairs
\[
(0,1001/1000),\quad(3,2997/2000),\quad(2,999/10),\quad
(0,9999/100),\quad(0,101)
\]
have phase classes \((2,1,3,2,4)\). The required backward intervals occur in \(O_1\) and \(E_2\), and exact rational arithmetic gives the mandatory strict inequality \(r_2>r_3\).

Nevertheless, the source's positive-coefficient common numerator has strictly positive pairings with **all five** displayed actual atoms. Thus, for any positive weights on those atoms, the aggregate evaluated on that numerator is positive; its monomial coordinates cannot all be strictly negative. This finite contradiction requires no assumed optimization result. The whole anchor box's independent stability and all-frequency numerator checks are already pinned in the source.

The standalone rational checker `frontier-20261029-five-node-ratio-barrier-nonvacuity-independent-kernel-v1.py`, SHA-256 `bcddd91b0aafe1c04b3ed18eae3fe3e71990af5deaa75cb2cf22e83b0787374c`, reconstructs all 40 strict corner/marker signs, the five actual sign pairs, the exact ratio cross-product and all five positive test pairings. Receipt `frontier-20261029-five-node-ratio-barrier-nonvacuity-independent-result-v1.json`, SHA-256 `281d35b0facbeabc92bb9cb25ff3cc4373e037538e33301904fb90fc2c2c6d07`. Arithmetic uses `fractions.Fraction` on one Python Eval host; no formal proof, cross-vendor review, novelty clearance, or arbitrary-box conclusion is claimed.
