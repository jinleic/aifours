# An exactly eligible three-contact septic-box family and a bounded certificate search

**Status: WRITTEN-checked-in-kernel; new author candidate, not a parent adoption.** This gives a genuinely different, anisotropic test family with three simultaneous imaginary-axis contacts at its stability boundary. It does **not** settle the original unrestricted degree-seven SPR question. In particular the bounded finite-grid search below found neither an unrestricted common numerator nor a no-go certificate for its selected box.

## Family and exact stability threshold

Write coefficient vectors in ascending order and let

\[
a_0(s)=(s+1)\prod_{v\in\{2,4,8\}}((s+1)^2+v^2)
=5525+8555s+4893s^2+2219s^3+455s^4+105s^5+7s^6+s^7.
\]
Let the independent positive coefficient halfwidths be

\[
 h=\left(\frac{33060833}{6723},2718,\frac{104393}{1245},
 \frac{172}{15},\frac{104393}{18225},\frac{106}{15},
 \frac{1530997}{1512675}\right).
\]
For \(\rho\ge0\), let \(K_\rho\) be the monic septic box with \(a_j\in[a_{0,j}-\rho h_j,a_{0,j}+\rho h_j]\), independently for \(j=0,\ldots,6\). All seven halfwidths are strictly between zero and the corresponding center coefficients.

**Claim.** Every polynomial in \(K_\rho\) is strictly Hurwitz for every \(0\le\rho<1\). For every \(\rho\ge1\), \(K_\rho\) is ineligible: it contains a polynomial with a purely imaginary root. Thus this family has an exact robust-stability threshold, not just a numerical bracket.

For \(t=\omega^2\), write \(a(i\omega)=E_a(t)+i\omega O_a(t)\). At \(\rho=1\), independent coefficient variation gives the following exact interval bounds; the entries are \((E_{\min},E_{\max};O_{\min},O_{\max})\):

| \(t\) | \(E\) interval | \(O\) interval |
|---|---|---|
| \(3\) | \([-10496,0]\) | \([0,5632]\) |
| \(17/2\) | \([-85655718239/6050700,-1247832784/1512675]\) | \([-799249/120,-1001/120]\) |
| \(15\) | \([0,21760]\) | \([-8960,0]\) |
| \(30\) | \([29371810/747,89005280/747]\) | \([63,18907]\) |
| \(65\) | \([-625040,0]\) | \([0,66640]\) |

For \(\rho<1\), the zero endpoints at \(3,15,65\) become strict with the signs of the center, while the strict endpoints at \(17/2,30\) stay strict. At zero both parity polynomials are positive; both have negative leading cubic coefficients for every member. The signs at \(0,3,17/2,15,30,65,\infty\) are therefore, respectively,

\[
(+,+),(-,+),(-,-),(+,-),(+,+),(-,+),(-,-).
\]
Each parity cubic consequently has exactly three positive roots, with the \(E\) roots in \((0,3),(17/2,15),(30,65)\) and the \(O\) roots in \((3,17/2),(15,30),(65,\infty)\). They are disjoint, so no member has an imaginary-axis root. The coefficient box is connected and homotopic to the explicitly Hurwitz center; monicity and bounded coefficients preclude an escape through infinity. The right-half-plane root count is therefore constant and zero. This proves all-member stability without relying on the four-corner theorem.

At \(\rho=1\), actual corner \((E_+,O_-)\) has both parity components zero at \(t=3\) and \(t=65\); actual corner \((E_-,O_+)\) has both zero at \(t=15\). These correspond to three imaginary-axis pairs. Every larger nested box contains those same boundary polynomials.

## Finite-grid search, and what it does not show

Select the actual all-member-stable box \(K_{999/1000}\). Its midpoint numerator \(b=a_0\) fails: at actual corner \((E_+,O_-)\) and \(t=49/15\),

\[
P_{a,b}(t)=\operatorname{Re}[b(i\sqrt t)a(-i\sqrt t)]
=-\frac{8371280460790839296}{79769970703125}<0.
\]
This is a restriction on that numerator only; it is not a restriction on all numerators.

A six-round rational frequency-exchange search started with the three target contacts and added exact failing dyadic-compactification frequencies from the candidate grid-dual polynomials. In the sixth round, its 19 finite \(t\)-values, all four actual corners, and the common infinity atom give 77 atoms. Exact rational simplex primal and dual witnesses agree at the **positive** normalized max-min value

\[
\frac{1230651043686817380174876345053234800010680171867467398526440548593}
 {96062364978167213753671332026894190360690257482834890224879352952067387392}.
\]
The frozen dual has all eight coefficients positive and has strictly positive pairing at every tested atom. Hence **no nonpositive-coordinate atom certificate supported on that particular grid exists**. This does not exclude certificates using other frequencies. The sixth candidate failed at additional exact frequencies; these were generated after the final optimization and were not part of the 77-atom claim. No full-halfline positive numerator was established by these six rounds.

## Evidence and boundary

- Frozen family, markers, exact search trajectory, eight-atom primal support and positive grid dual: `frontier-20261028-three-gap-family-and-grid-frozen-v1.json`, SHA-256 `6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9`.
- Design producer `frontier-20261028-three-gap-simultaneous-design-kernel-v1.py`, SHA-256 `f59bebd4c72ff69d7b8a762ece899c821f1653c9815f1ab0941a69d6439af23a`. The bounded design tried 33 selected triples before this feasible candidate; it is not an exhaustive impossibility claim about the others.
- Exact search producer `frontier-20261028-three-gap-certificate-search-kernel-v1.py`, SHA-256 `1cce4a6577b9924a14e5492c216c79a2cd8cd3d62a21b6125ac20b3b00f93e0f`; it uses the already-loaded rational simplex and pairing helpers, with no native optimizer.
- Standalone frozen-input replay `frontier-20261028-three-gap-independent-replay-kernel-v1.py`, SHA-256 `e17f8ca64fddaef20844232c78ef3a8f246c9d738c88a4867ac5f25e8edada8d`. It recomputes the center factorization, all marker bounds, three actual boundary zeroes, 28 positive rational Hurwitz minors at \(999/1000\), midpoint failure, all 77 dual inequalities, eight-atom primal sum and objective, and rejects corrupted marker and weight controls. Receipt `frontier-20261028-three-gap-independent-replay-result-v1.json`, SHA-256 `76b4e454df53a4190454e0f37da1ec765696cd8a532544618909c6057996f9d7`.

The stability proof imports elementary real-polynomial root continuity, sign-change/root-count facts, and preservation of the right-half-plane root count under a compact monic homotopy with no imaginary roots. Exact checks use Python `fractions.Fraction` and integers. This is not a formal proof, independent-model review, novelty clearance, or a verdict for arbitrary interval families.
