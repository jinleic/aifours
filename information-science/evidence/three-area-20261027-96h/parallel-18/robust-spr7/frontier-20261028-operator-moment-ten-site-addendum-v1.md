# Ten-site extension of the all-\(h\) operator separator

**Status: WRITTEN-checked-in-kernel; additive to the seven-site packet, not parent adoption.** For the same exactly stable asymmetric septic box, add the actual-corner sites \((0,1021/3),(2,231/25),(3,235/21)\) to the seven sites in `frontier-20261028-operator-moment-seven-site-obstruction-v1.md`. These were selected because the earlier seven-site separator fails the original pairing at those points; its finite-site positivity is not global.

The new positive coefficient vector
\[
(b_0,\ldots,b_7)=\left(\frac{91}{10000},\frac{27965499039}{10000},
\frac{10733007319}{10000},\frac{2978813209}{10000},
\frac{25201549}{625},\frac{26269981}{10000},\frac{764987}{5000},1\right)
\]
has \(P_0>0,P_1>0,P_2>0\) at all ten sites, using the quadratic notation of the seven-site packet. Therefore it separates **every** nonzero nonnegative mixture of \(I+hD\) rows with arbitrary \(h\ge0\) and derivative rows supported on those ten sites. The minimum of the 30 unnormalized quadratic coefficients is exactly
\[
663186658288071524098503711/6553600000000000000000>0.
\]
The moment-cone decomposition and its finite-atom interpretation are unchanged. No conclusion is made about any other frequency, derivative order, or box, and neither this vector nor the earlier seven-site vector is claimed globally SPR.

Frozen vector, ten exact coefficient triples, box endpoints and root bands: `frontier-20261028-operator-moment-ten-site-dual-frozen-v1.json`, SHA-256 `0e2ebc6bd3d330cc0a678de65d66682d4040aa1035dd9934a7c99b7a994e968f`. Independent checker `frontier-20261028-operator-moment-ten-site-dual-independent-kernel-v1.py`, SHA-256 `19279bc42cd4cf7638fe7af4e0824b76aecf98d54a30161d06d5d8c4b471724a`, checks 28 positive original corner Hurwitz minors, 12 root brackets and six separated bands, all 30 quadratic coefficients and a corrupt-coefficient control. Receipt `frontier-20261028-operator-moment-ten-site-dual-independent-result-v1.json` has SHA-256 `7f9443fb456440000c18812cd0ef01e54e74f29cbf4b1e38ae2e6de1fd2978be`.

The general operator-preservation and all-member stability arguments remain written proofs; these finite identities were replayed with exact rational arithmetic on one Python Eval host. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
