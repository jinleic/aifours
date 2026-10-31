# The ineligible phase example violates common root-band ordering

**Status: WRITTEN-checked-in-kernel finite addendum; not parent adoption.** In `frontier-20261029-individually-stable-five-atom-negative-ineligible-v1.md` (SHA-256 `1ffd658f3d38e80d0aa086857e5fd0c043a16a44883962b7051975354b9fac51`), let \(a_{\min}(s)=(s+12587/10000)^7\) and \(a_{\max}(s)=(s+11597/2500)^7\). Their first positive odd/even roots satisfy the **opposite** of the globally separated-box ordering:
\[
O_1(a_{\min})<\frac12<E_1(a_{\max}).
\]
Indeed \(O_{a_{\min}}(0)>0\) while \(O_{a_{\min}}(1/2)<0\), so an odd root occurs before \(1/2\). For \(E_{a_{\max}}\), the four exact cubic Bernstein coefficients on \([0,1/2]\) are strictly positive, so its first even root is after \(1/2\). The independent checker `frontier-20261029-ineligible-phase-root-band-independent-kernel-v1.py`, SHA-256 `40c90cc63a760d65d9fdc0a26c8c6d12a994a65f73457c8f531b584b5b6f398e`, verifies these statements by rational arithmetic.

Thus the earlier five-negative-atom construction, although its **sampled phase classes** obey \(q_i\le q_j+1\) and its ratio condition holds, does **not** enjoy the common root-band hypothesis of a stable independent box. This is a precise failure of that hypothesis, not an original counterexample. It complements the previously checked negative Hurwitz minors of its convex and interval hulls. No formal proof, cross-vendor review, novelty clearance or arbitrary-box verdict is claimed.
