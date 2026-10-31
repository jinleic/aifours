# The Vieta-face obstruction box has an explicit common numerator

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:13:02 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational certificates**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This strengthens the exact proof-route barrier in `frontier-20261029-pattern-c-entire-vieta-face-failure-v1.md`, SHA-256 `6ab23593f984a52e0585cb0c3d53edb629a2b2f891047f8eedabf73598b5bbf9`: the displayed actual box **does have** an unrestricted common numerator, even though its entire \(x_2=c\) Vieta face is obstructed.

## 1. Explicit numerator and whole-half-line certificate

Use the exact interval box in the named face packet. The monic numerator with ascending coefficients
\[
b=(932/5,\ 8611/25,\ 11883/25,\ 34049/100,\ 2097/10,\ 962/25,\ 233/25,\ 1) \tag{1}
\]
is strictly positive real against every member at every finite real frequency. Explicitly, let
\[
H(s)=(s^2+1/2)(s^2+2)(s^2+20).
\]
Then
\[
b(s)=(233/25+s)H(s)+s\left[\frac{157}{25}(s^2+2)(s^2+20)
+\frac{353}{50}(s^2+1/2)(s^2+20)
+\frac{66}{25}(s^2+1/2)(s^2+2)\right]. \tag{2}
\]
All three squared poles and all four displayed positive weights are rational.

For each actual parity corner \(a\), put
\[
P_a(t)=E_a(t)E_b(t)+tO_a(t)O_b(t),\qquad
Q_a(x)=(1-x)^7P_a\!\left(\frac{x}{1-x}\right).
\]
The four exact compactified Bernstein certificates are frozen in `frontier-20261029-pattern-c-face-box-common-numerator-frozen-v1.json`, SHA-256 `f4e659dccdd7eabb572b94881d9133b47a86bcd7bbc9bc80a15493e706da06af`. Their dyadic leaves cover \([0,1]\), with counts \((12,12,20,11)\), and all **440** displayed degree-seven Bernstein coefficients are strictly positive. Their exact minimum is
\[
\Delta=\frac{8116034505056821580897239201}{346623210999906476971754782720000000}>10^{-9}. \tag{3}
\]
The compactification is applied **implicitly and exactly**: if \(P(t)=\sum_{i=0}^7p_it^i\), then the degree-seven Bernstein coefficients of \(Q\) are \(p_i/\binom7i\), since \(Q(x)=\sum_i p_i x^i(1-x)^{7-i}\). Subdivision is exact `fractions.Fraction` arithmetic. Thus \(P_a(t)/(1+t)^7\ge\Delta\) for each corner and all \(t\ge0\); affine coefficient minimization extends this to every box member.

As a separate same-host rational check, raw-polynomial Sturm chains for all four corners have variation pairs \((3,3)\) at \(0,+\infty\), and both endpoint/leading signs are positive. They therefore have no positive roots. This is not an independent-model review or a formal proof.

## 2. Stability and the real obstruction scope

For \(\operatorname{Re}s>0\), each \(s/(s^2+x_j)\) is the average of reciprocals of \(s\mp i\sqrt{x_j}\), both with positive real part. Equation (2) makes \(b/H\) strictly positive real in that half-plane, so \(b\) has no right-half-plane zero. On the imaginary axis, the positive constant in \(b/H\) excludes zeros away from the three roots of \(H\), and the corresponding strictly positive residue excludes a zero at each of those roots; the origin is nonzero. Thus \(b\) is Hurwitz. The positive pairing gives \(\operatorname{Re}(a(i\omega)/b(i\omega))>0\); the monic path from \(b\) to each \(a\) has no imaginary-axis root, so every denominator is Hurwitz by root continuity. Division by \(|a(i\omega)|^2\) gives the claimed strict positivity of \(b/a\).

The named face packet's five-atom zero-odd measure remains a valid, **nonvacuous restriction** on every common monic numerator. Let \(x_2\) be the middle positive root of its even part after normalizing the positive \(s^6\) coefficient to one. Denote the first odd band's upper endpoint by \(b_{\rm band}=21/20\) and the second band's lower endpoint by \(c=221/20\). Its pairing on the \(x_2=b_{\rm band}\) face is everywhere strictly below 750, and on the \(x_2=c\) face everywhere strictly below \(-1/60\); these follow from the exact four-vertex sums in the named packet and the rational comparisons in the frozen analysis. Multi-affinity then forces
\[
x_2<c-\frac{10}{45001}. \tag{4}
\]
Indeed writing \(\theta=(x_2-b_{\rm band})/(c-b_{\rm band})\), the weighted pairing is less than \(750(1-\theta)-\theta/60\); a common numerator requires it positive. The explicit numerator (1) has even roots \((1/2,2,20)\) and satisfies (4). Thus the face failure cannot be dismissed by saying the box itself has no common numerator, but it does not refute unrestricted synthesis.

## 3. An explicit common-numerator neighborhood

The same numerator works for every interval box whose 14 nonleading endpoints independently differ from those of the face box by at most \(\epsilon=10^{-14}\). All widths and lower endpoints remain positive. Clamp any new coefficient vector to the old box, changing each nonleading coefficient by at most \(\epsilon\). With \(S=\sum_j b_j=32103/20\), every corresponding pairing perturbation satisfies
\[
\frac{|P_{a',b}(t)-P_{a,b}(t)|}{(1+t)^7}\le7\epsilon S<\frac12\,10^{-9}.
\]
The strict rational guard \(14\epsilon S<10^{-9}\) is in the frozen record. Thus the fixed \(b\) retains a positive uniform pairing margin, and the same homotopy proves every new denominator Hurwitz. This is a 14-endpoint-dimensional open positive family. The atom/face obstruction and bound (4) are asserted for the original box only, not automatically for every perturbed box.

## 4. Assurance and process correction

All 55 dyadic leaves, 440 positive Bernstein coefficients, the minimum, pole data and guards were computed exactly using integers/`fractions.Fraction` in one Python Eval host; the separate Sturm calculation used the same host. The pole positivity, homotopy, Vieta root bound and perturbation deductions are written mathematics. A mistakenly issued checker-coverage alert was explicitly withdrawn in `owner-halfline-checker-coverage-fault-erratum-v1.json`, SHA-256 `499602399e38f475688b8ad4d0f56d1a3cb5c63debc54db7581941e9e0509df3`; its false blanket hold must not be propagated. The separate second-band proof errata remain binding. No independent scientific review, formal verification, parent adoption or novelty clearance occurred. The original arbitrary septic-box synthesis-or-obstruction verdict remains **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
