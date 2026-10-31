# Right-half-plane shifts are valid, but add no new strict boundary cone

**Status: WRITTEN theorem with WRITTEN-checked-in-kernel finite row identities; author candidate, not parent adoption.** Shifted rows may accelerate a finite search, but this packet does not report a negative certificate or an unrestricted septic verdict.

## Validity and Poisson representation

If \(a\) is real Hurwitz and \(b/a\) is SPR of equal degree, the harmonic minimum principle gives \(\operatorname{Re}[b(z)/a(z)]>0\) throughout the closed right half-plane. Thus for every \(r\ge0\), \(b(s+r)/a(s+r)\) is also SPR. This shift can be composed with the previously proved derivative and reciprocal operators.

For a fixed Hurwitz \(a\), write
\[
L_{r,\omega}(b)=\operatorname{Re}[b(r+i\omega)\overline{a(r+i\omega)}].
\]
For \(r>0\), the Poisson formula for the bounded harmonic real part of the proper rational function \(b/a\) gives the **linear-functional** identity
\[
L_{r,\omega}(b)=\int_{-\infty}^{\infty}
\frac{|a(r+i\omega)|^2}{\pi|a(i\xi)|^2}
\frac{r}{r^2+(\omega-\xi)^2}\,L_{0,\xi}(b)\,d\xi.
\]
The kernel is strictly positive and independent of \(b\). The integral converges for every degree-\(\le n\) basis polynomial: at large \(|\xi|\), its integrand is \(O(|\xi|^{j-n-2})\) for basis coefficient \(b_j\). Thus each shifted coefficient vector is a positive conic integral of boundary coefficient vectors for the **same actual denominator**.

Consequently, if a finite nonnegative combination of shifted and boundary rows has all coefficient sums **strictly** negative, positive finite Riemann-sum approximations to the displayed integrals yield a finite pure-boundary strict certificate for the same actual denominators: choose the approximation error below the smallest strict coordinate margin. For real coefficients the \(\pm\xi\) rows agree, so the boundary can be parametrized by \(t=\xi^2\ge0\). If the original data are rational, rational sampling frequencies and positive rational weights can be chosen by density. This approximation statement does **not** automatically preserve a weak certificate with zero coordinates. The same identity applies after a previously allowed fixed differential operator, relative to that transformed actual denominator.

Thus shifted rows are mathematically valid finite-search cuts, but their mere introduction does not prove a new strict global obstruction beyond boundary rows. In particular it does not turn a failed finite grid into a proof.

## Bounded exact check

One asymmetric septic box was checked at its four actual parity corners, shifts \(r\in\{0,1,10\}\), derivative orders \(k=0,1,2\), \(h\in\{0,1\}\), and a finite rational frequency grid. The initial and second exact minimax solves used 576 and 864 rows; both margins were positive, and the corresponding candidate numerators failed at additional original frequencies. No full-halfline numerator or negative certificate was obtained. Separately, 4,608 target-box shifted unit-coefficient values were recomputed by independent polynomial shifting, recursive differentiation and direct parity pairing; another 4,608 were checked on a different box.

Search data `frontier-20261028-shifted-operator-hybrid-search-results-v1.json` has SHA-256 `646739ed798f7adc7397c2e9a4dce3681753cd6a023c17f1a87574708d4821ea`; producer `frontier-20261028-shifted-operator-hybrid-search-kernel-v1.py` has SHA-256 `0cabb4d8c2eb5a120969304074c671377f4da6f36849d5be50794a92dd59a55c`. All-member stability of the searched interval box follows from the four-corner Hurwitz check together with the named Kharitonov interval theorem; no independent all-frequency SPR claim is made.

The Poisson/approximation argument is written mathematics, and the indicated finite identities use exact rational arithmetic on one Python Eval host. No formal verification, cross-vendor review, novelty clearance or universal septic conclusion is claimed.
