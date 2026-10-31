# A nontrivial open ratio-gap family: no corner numerator works

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** There is an explicit 14-dimensional open neighborhood of strictly Hurwitz septic boxes where every box meets the three five-node ratio-gap tests, **none of its four Kharitonov corner polynomials is a common numerator**, yet a fixed different numerator works for the whole neighborhood. The six-positive-frequency certificate lower bound is conditional on the named unreviewed phase-word and root-order imports. This is not an arbitrary-box verdict.

## Anchor box and actual corner failures

Take the exact box \(K\) in `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`, SHA-256 `a7ad2c77a2f155ef1b82e9d7e3eee73058a303547d0e9b7f600771f16b99f80f`, and shrink its seven intervals about their midpoints by \(\rho=3/4\). Call the resulting full-width box \(K_0\); its exact rational endpoints are pinned in the data below. Number its actual parity corners \(a_0,a_1,a_2,a_3\) in the usual \((--),(-+),(+-),(++)\) order.

The two exact negative pairings
\[
\begin{aligned}
P_{a_1,a_0}(170)=P_{a_0,a_1}(170)
&=-\frac{188879280277217053013556839729746763157}{3518437208883200000000},\\
P_{a_1,a_2}(10922)=P_{a_0,a_3}(10922)
&=-\frac{7696341619390490764159743262543762559389611711957}{87960930222080000000000}
\end{aligned}
\]
exclude, respectively, corner numerators \(a_0,a_1,a_2,a_3\). These are actual denominators and \(t=\omega^2\); the statement does **not** exclude other numerators inside the box.

A different monic numerator is common SPR for all of \(K_0\):
\[
(b_0,\ldots,b_7)=
\left(\frac{581401917}{10},\frac{520347753}{2},\frac{1443896043}{5},
\frac{42535235}{2},\frac{34705369}{10},\frac{73352}{5},\frac{1788}{5},1\right).
\]
Independent replay verified all 28 strict corner Hurwitz determinants and 480 strictly positive compactified pairing coefficients, with common margin
\[
\delta=\frac{5809199245066286683341672313993}
{12998370412496492886440804352000000}>0.
\]
Thus the anchor already has no negative atom certificate of **any** support; the ratio-gap result below is a structural property of a broader test, not a stronger conclusion for this particular box.

## Ratio gaps and their open persistence

For the four endpoint-root ratios \((U_1,L_2,U_2,L_3)\) defined in `frontier-20261028-five-node-ratio-gap-obstruction-v1.md`, rational exterior points \((40,120,142,6680)\) give bounds
\[
\left(\widehat U_1,\widehat L_2,\widehat U_2,\widehat L_3\right)=
\left(\frac{101990957442440301400}{21288358617298857197},
\frac{99175865247942046200}{8918703201862334771},
\frac{759748679403363934556}{14077069369018478077},
\frac{34370185261973656247824792}{37257624780294823334707}\right).
\]
The comparisons \(\widehat U_1<\widehat L_2\), \(\widehat U_1<\widehat L_3\), and \(\widehat U_2<\widehat L_3\) are strict. The root-side brackets are respectively \((40,41),(119,120),(142,143),(6679,6680)\), verified by 14 exact parity sign checks and stable-corner interlacing.

Now perturb all 14 endpoints independently by at most \(\varepsilon=10^{-20}\). The exact replay verifies:

* All 40 parity signs at the ordered markers \((9,61,120,254,6680)\) retain a strict margin, proving all-member Hurwitz stability by Hermite–Biehler.
* Four rational root-side guards and interval bounds on the four ratios retain all three strict comparisons, so the conditional six-positive-frequency lower bound continues to hold.
* The two displayed negative-pairing witnesses remain negative when both the selected denominator corner and the selected numerator corner are perturbed. This uses a direct bilinear coefficient perturbation bound, checked separately for all four corners.
* The fixed \(b\) remains common: \(14\varepsilon\sum|b_j|\le\delta\), so its normalized pairing loses at most \(\delta/2\) for any perturbed denominator. Thus these boxes do have an unrestricted numerator and no all-numerator negative certificate.

Anchor endpoints, ratios, four exact failures and positive leaves: `frontier-20261028-five-node-ratio-gap-no-corner-frozen-v1.json`, SHA-256 `ac46440c5a57f054eac084e9dce400428a4850149e2da4c01bd00044ff8572dd`. Open bounds: `frontier-20261028-five-node-ratio-gap-no-corner-open-frozen-v1.json`, SHA-256 `855dfd06e2a7c216c7f018a3a745bbdebab46143dde8511b41eceb5536f8b5ce`. Independent checker `frontier-20261028-five-node-ratio-gap-no-corner-open-independent-kernel-v1.py`, SHA-256 `b1dd98930508c9cb6c55bc12ffdadaeb5be0b76b14b9ccb6398e4d799a0ba274`; receipt `frontier-20261028-five-node-ratio-gap-no-corner-open-independent-result-v1.json`, SHA-256 `b66d51db320d3cb6042633991282896135d43289749df687246777d9e79a5de8`.

Finite arithmetic is exact integer/`fractions.Fraction` work on one Python Eval host. The root-band, ratio-gap and homotopy reasoning is written and depends on its stated unreviewed imports. No formal proof, cross-vendor review, novelty clearance, or universal arbitrary-box result is claimed.
