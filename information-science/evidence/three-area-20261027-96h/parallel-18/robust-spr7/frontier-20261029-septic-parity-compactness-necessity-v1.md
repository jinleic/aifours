# A fixed-odd noncompact septic family with no common numerator

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel finite stability evidence; not parent adoption.** This sharpens `frontier-20261029-one-parity-compactness-necessity-v1.md` from cubics to the actual septic degree. It is a necessary boundary on the positive fixed-parity theorem, **not an admissible original finite-width box**.

Let
\[
\begin{aligned}
O(t)&=-(t-1)(t-4)(t-9),\\
E_A(t)&=-(t-1/2)(t-2)(t-6),\\
E_B(t)&=-(t-3/4)(t-3)(t-7),
\end{aligned}
\]
and for every \(N>0\) define the monic septics by
\[
a_{A,N}(i\sqrt t)=NE_A(t)+i\sqrt t\,O(t),\qquad
a_{B,N}(i\sqrt t)=NE_B(t)+i\sqrt t\,O(t).
\]
All members have **exactly the same odd part** \(O\).

Their even and odd positive roots strictly alternate: for \(A\), \(1/2<1<2<4<6<9\); for \(B\), \(3/4<1<3<4<7<9\). Thus no polynomial on either positive \(N\)-ray has an imaginary-axis zero, including at zero and infinity. At \(N=1\) the independent exact checker verifies the seven strictly positive Hurwitz minors of each polynomial. Keeping the monic leading coefficient fixed while varying \(N\) through \((0,\infty)\), axis avoidance and root continuity therefore prove **all** ray members Hurwitz.

Suppose some real septic \(b\) were common to both rays. Evaluating at zero forces \(b_0>0\). For every \(t\in(1/2,3/4)\), one has \(E_A(t)<0<E_B(t)\). The two pairings are
\[
P_{a_{A,N},b}=NE_AE_b+tOO_b,\qquad
P_{a_{B,N},b}=NE_BE_b+tOO_b.
\]
Strict positivity for every \(N>0\) requires \(E_b(t)=0\): either nonzero sign makes one pairing tend to \(-\infty\). Since this is true throughout a nonempty open interval, \(E_b\) is the zero polynomial, contradicting \(b_0>0\). Hence there is **no** common numerator at all.

For any \(0<N_{\min}\le N\le N_{\max}<\infty\), the union of the two ray segments is compact and the fixed-odd theorem does give a common numerator. The example therefore isolates compactness, rather than stability, the parity condition, or degree, as essential. It does not yield an eligible finite-width interval-box counterexample.

Frozen exact factorizations and reference determinants `frontier-20261029-septic-parity-compactness-frozen-v1.json`, SHA-256 `23f31c32eee919cd958bf6e58d640123f029e086390f81d63f1457544928e2c9`; standalone exact checker `frontier-20261029-septic-parity-compactness-independent-kernel-v1.py`, SHA-256 `73b1f0a30b273f4c3ef39ffd6feb6d458da18fb02b272263e16bc4cb04e50890`; receipt `frontier-20261029-septic-parity-compactness-independent-result-v1.json`, SHA-256 `4d3746cecfdef342e5a6d8b53129f7114e438b2d13591bea24cd09d479e53fd2`. The all-\(N\) homotopy and interval-of-opposite-signs arguments are written, and finite arithmetic uses exact `fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, or original-box verdict is claimed.
