# A strict mixed-operator inequality and a pointwise separation example

**Status: WRITTEN deduction from the SPR-preserving operator theorem, with an exact finite example independently replayed on one host; author candidate, not parent adoption.** This is a necessary inequality for a common numerator, not an unrestricted septic verdict.

For real same-degree \(a,b\), fix \(t=\omega^2\ge0\) and put
\[
\begin{aligned}
P_0(t)&=\operatorname{Re}[b(i\omega)\overline{a(i\omega)}],\\
P_1(t)&=\operatorname{Re}[b'(i\omega)\overline{a(i\omega)}+b(i\omega)\overline{a'(i\omega)}],\\
P_2(t)&=\operatorname{Re}[b'(i\omega)\overline{a'(i\omega)}].
\end{aligned}
\]
If \(b/a\) is SPR, the preceding operator theorem gives, for every \(h\ge0\),
\[
P_h(t)=P_0(t)+hP_1(t)+h^2P_2(t)>0.
\]
In particular \(P_0,P_2>0\), and minimizing the quadratic over \(h\ge0\) yields the additional strict necessary condition
\[
P_1(t)>-2\sqrt{P_0(t)P_2(t)}.
\]
Each \(P_i\) is linear in the coefficients of \(b\). When \(P_1<0\), the equivalent squared form is \(P_1^2<4P_0P_2\). Testing only the original and derivative inequalities at a given frequency does not in general enforce this mixed inequality.

For an exact pointwise example, take
\[
a=(s+1)^7,\qquad
b=(s+17)(s+1)(s+16)(s+21)(s+9)(s+28)(s+7).
\]
Both polynomials and their derivatives and \(I+D\) transforms are Hurwitz. At \(t=2\), exact arithmetic gives
\[
P_0=312440490>0,\quad P_1=-1221017976,\quad
P_2=54687150>0,\quad P_{h=1}=-853890336<0.
\]
Equivalently the three real-part ratios at that frequency are
\[
\operatorname{Re}(b/a)=3857290/27>0,\quad
\operatorname{Re}(b'/a')=32150/21>0,\quad
\operatorname{Re}((b+b')/(a+a'))=-1756976/99<0.
\]
Thus an operator row can reject a candidate that passes both endpoint tests **at this one frequency**. By the preservation theorem, this particular \(b/a\) cannot be SPR on the entire imaginary axis. The example is not a stable interval-box counterexample and does not claim that the two endpoint tests hold at other frequencies.

Frozen factor lists, polynomial coefficients, quadratic and ratios: `frontier-20261028-spr-operator-point-obstruction-frozen-v1.json`, SHA-256 `7c11c8486c61f362e23e68119c8040a265bb2081e998af416fef73ed27b36f34`. Standalone checker `frontier-20261028-spr-operator-point-independent-kernel-v1.py`, SHA-256 `cb0bdddb3da45413f462c180c3ece522542a4554cf5afa7a67c91e910eaef371`, rebuilds both factorizations, checks 40 positive Hurwitz minors for the six relevant polynomials, and directly recomputes all pairings and ratios. Receipt `frontier-20261028-spr-operator-point-independent-result-v1.json` has SHA-256 `0b1313b962f10dc0e60452af85c59d008c85dde2b60f84f0cb5877e94014a4d9`. The general operator theorem is written mathematics, not independently formalized or novelty-cleared.
