# Four distinct root scales in the explicit common numerator

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact leading-degree replay; not parent adoption.** Let \(b_R\) be the explicit determinant-constructed common numerator of the full-width stable septic family in `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`). As \(R\to\infty\), its seven roots split into four disjoint scales:

| Number | Root scale | Exact scaled limit |
|---:|---|---|
| 1 | \(R^2\) | \(\xi/R^2\to-1317/8425\) |
| 2 | \(R\) | \(\xi/R\to\pm i\sqrt{200/1317}\) |
| 2 | \(1\) | \(\xi\to\pm i\sqrt{1251/200}\) |
| 2 | \(1/R\) | \(R\xi\to(-1685\pm i\sqrt{2781935})/1668\) |

The fast root is eventually real and negative; the other six form three complex-conjugate pairs for sufficiently large \(R\). All finite-\(R\) roots lie in the open left half-plane because \(b_R\) is common SPR. The first, fast-scale necessity for **every** common numerator is established separately in `frontier-20261029-unbounded-common-numerator-fast-root-v1.md` (SHA-256 `5e66ad6170302407d1b4f4823852c446d4b49ba345fc684a7d8527da2d40403e`); the other three pairs' limits are for this **one** explicit numerator only.

## Proof from four exact scaled limits

The source's independent symbolic replay gives leading coefficient orders \((2,3,4,3,4,2,2,0)\) in ascending powers \(s^j\), with corresponding leading constants
\[
\left(\tfrac3{10},\tfrac3{10},\tfrac{1251}{8425},\tfrac{2002}{8425},
\tfrac8{337},\tfrac{2002}{8425},\tfrac{1317}{8425},1\right).
\]
The separate checker below verifies these exact degrees and constants. Coefficientwise, and hence uniformly on compact \(z\)-sets,
\[
\begin{aligned}
R^{-14}b_R(R^2z)&\to z^6(z+1317/8425),\\
R^{-8}b_R(Rz)&\to z^4((1317/8425)z^2+8/337),\\
R^{-4}b_R(z)&\to z^2((8/337)z^2+1251/8425),\\
R^{-2}b_R(z/R)&\to(1251/8425)z^2+(3/10)z+3/10.
\end{aligned}
\]
The nonzero roots of the latter three limiting polynomials are simple. Their squared imaginary limits and the slow quadratic's negative discriminant are checked exactly:
\[
\frac{(8/337)}{(1317/8425)}=\frac{200}{1317},\quad
\frac{(1251/8425)}{(8/337)}=\frac{1251}{200},\quad
\Delta_{\rm slow}=-\frac{14859}{168500}<0.
\]
Rouché's theorem on small disjoint circles around the nonzero simple limits yields respectively one, two, two and two roots at the four scales. These clusters are disjoint for large \(R\) and exhaust degree seven. The fast simple real limit gives an eventually real root by conjugation symmetry; the other simple limits are nonreal conjugates. The slow quadratic formula reduces exactly to the displayed \((-1685\pm i\sqrt{2781935})/1668\).

Independent leading-exponent checker `frontier-20261029-unbounded-numerator-multiscale-roots-independent-kernel-v1.py`, SHA-256 `bd1b03b3352fc3b8f44213ebb29f25be3c74e809553f6814a37dcc36dc8034bd`; receipt `frontier-20261029-unbounded-numerator-multiscale-roots-independent-result-v1.json`, SHA-256 `48747fb99105d92fe2df4eeec8dc6dec7406496315f86ab9dfb8ef344dcec45b`. The finite rational identities use exact `fractions.Fraction` on one Python Eval host; the Rouché root counts and asymptotic conclusions are written mathematics. No formal proof, cross-vendor review, novelty clearance, or arbitrary-box verdict is claimed.
