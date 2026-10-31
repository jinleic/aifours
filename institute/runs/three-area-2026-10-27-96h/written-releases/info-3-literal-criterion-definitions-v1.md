# Source-bound original definitions — info-3

Literal canonical-dossier statement of the printed problem, /Users/jinleic/repos/aifours/information-science/stochastic-hinf-preview-control/README.md SHA256 bacb92ff14af3757ffb6e78f11a72fb479460546f3c7a288455c810cf856d1e7, LF1-19 (prefix = source line number):

1| # Stochastic H∞ preview control (随机系统 H∞ 预演控制)
2| 
3| Book: 《10000个科学难题·信息科学卷》 (Science Press, 2011), pp. 674–676 (PDF pp. 695–697), problem by
4| 张焕水 (Zhang Huanshui) and 王宏霞 (Wang Hongxia). Page images: [`sources/book/`](sources/book/).
5| Work done 2026-10-14 (PT).
6| 
7| ## 1. The problem as printed
8| 
9| The system is
10| 
11|     dx(t) = [A x(t) + B u(t) + C w(t−h)] dt + [A0 x(t) + B0 u(t)] dW(t),    z(t) = D0 x(t) + D1 u(t),
12| 
13| where W is a Brownian motion and h ≥ 0 is the preview length. For a given γ > 0, find a full-information
14| controller u(t) = F(x(t), w(s) | t−h ≤ s ≤ t) such that
15| 
16|     E‖z‖_{L2[a,b]} / E‖w‖_{L2[a,b−h]} < γ,    with ‖f‖_{L2[a,b]} := (∫_a^b f(t)ᵀf(t) dt)^{1/2}.
17| 
18| Both the finite horizon (a, b bounded) and the infinite horizon (b → ∞) are asked for. The book asks
19| for necessary and sufficient (N&S) solvability conditions and the controller.

The criterion is the PRINTED expectation of pathwise L2 norms (an L1(Omega;L2) ratio), NOT the mean-square/RMS Hilbert replacement. Adaptedness, zero initial state, disturbance window/zero-extension, strictness and the controller information pattern are INTERPRETATIONS to be stated explicitly, never silently imposed.

## Provenance and limits

The quoted lines are the 2026-10-14 canonical dossier transcription of book pp.674–676 (page images exist; not re-read by Main). An earlier scout display past LF19 incidentally included the dossier's later theorem opening; that material is NOT supplied and is NONINPUT here. This packet certifies no book-image equivalence or result.
