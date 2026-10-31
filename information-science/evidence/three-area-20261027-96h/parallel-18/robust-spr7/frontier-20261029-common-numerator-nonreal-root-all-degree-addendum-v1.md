# All-degree extension of the nonreal-root obstruction

**Status: WRITTEN; author candidate, not parent adoption.** The odd-degree construction in `frontier-20261029-common-numerator-nonreal-root-obstruction-v1.md` extends verbatim to **every integer \(n\ge4\)**. Let \(m=\lfloor n/2\rfloor\), \(d=1/(10n)\), \(\eta=1/(100n^2)\), and
\[
a_n(s)=(s+1)^{n-2m}\bigl((s+\eta)^2+1\bigr)^m.
\]
There is an explicit full-width strictly stable monic degree-\(n\) interval box, centered at \(a_n\), for which \(a_n\) is a common SPR numerator but **every** common exact-degree-\(n\) real numerator has at least \(m-1\) nonreal conjugate root pairs, counted with multiplicity.

The phase increment proof is unchanged. The optional linear factor has nonnegative phase increment; the \(m\) lightly damped quadratic factors force \(\Delta\theta_{a_n}>m\pi-4m/(5n)\). Any common numerator with at most \(m-2\) nonreal pairs has phase increment below \((m-2)\pi+nd/(1-d)\). Strict SPR forces its phase increment above \((m-1)\pi-4m/(5n)\), impossible because the two rational error bounds sum to less than one and \(\pi>3\).

For the box, the even case simply drops the factor \((1+t)\) from both \(|a_n(i\sqrt t)|^2\) and the compactification denominator \((1+t)^n\). The same lower bound \(\delta_n=(\eta^2/5)^m\), coefficient sum \(S_n\), and positive independent radius
\[
r_n=\min\!\left(\tfrac12\min_{j<n}[s^j]a_n,\ \frac{\delta_n}{4n(1+S_n)}\right)
\]
prove all-member stability and common numerator \(a_n\) by the pairing estimate and homotopy in the original packet.

This addendum proves a structural restriction for a constructed family; it does not say that every robust box requires nonreal roots, nor does it preclude unrestricted synthesis. The underlying septic rational identities are checked in the original packet; the all-degree extension is written mathematics, not formal or cross-vendor verification, novelty clearance, or an arbitrary-box verdict.
