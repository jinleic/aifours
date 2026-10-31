# Exact common numerator for the difficult finite-node box

Owner InfoSPR7-2, info-2. Native clock observed before creation: **Thu Oct 29 15:35:34 PDT 2026**. **WRITTEN-checked-in-kernel exact rational candidate**, not parent-adopted, independently reviewed, formally verified or novelty-cleared. This is an all-frequency solution for the one explicit box below, not an arbitrary-box theorem. Its role is to settle the actual box behind the finite-node limitation and to exercise the all-candidate pole representation, not to claim that any fixed pole choice works universally.

## 1. The original eligible box and its numerator

In ascending coefficients \(a_0,\ldots,a_6\), with \(a_7=1\), take the independent intervals with lower and upper vectors
\[
\begin{aligned}
\ell={}&(1/2,\ 8066931430583/5000000,\ 2192672625039/2000000,\ 1212386815553/10000000,\\
&92232966209/2000000,\ 19302663807/10000000,\ 130713597/5000000),\\
u={}&(337520809988/78125,\ 8066933930583/5000000,\ 20431428914531/10000000,\ 3319907356313/10000000,\\
&92233966209/2000000,\ 19307663807/10000000,\ 133213597/5000000).
\end{aligned}
\]
Every width is strictly positive. The monic numerator with ascending coefficients
\[
 b=(20031739/80,\ 2570577219/2000,\ 103240501/400,\ 924507343/5000,\
15440477/2000,\ 4349847/2000,\ 31447/2000,\ 1) \tag{1}
\]
is common strictly positive real for **every** member and **every finite real frequency**, including zero. Thus this actual interval box is robustly Hurwitz and has a common exact-degree-seven numerator.

For reference, (1) is exactly
\[
\begin{aligned}
b(s)={}&\bigl(31447/2000+s\bigr)(s^2+1)(s^2+35)(s^2+455)\\
&+s\left[\tfrac{714279}{10000}(s^2+35)(s^2+455)
+\tfrac{898059}{5000}(s^2+1)(s^2+455)
+\tfrac{7164419}{5000}(s^2+1)(s^2+35)\right]. \tag{2}
\end{aligned}
\]
The three squared poles and all weights are positive rationals. The search used exact linear feasibility at finitely many nodes to propose these values, followed by exact whole-half-line certificates below; finite-grid feasibility by itself is not used to infer the result.

## 2. Uniform exact pairing certificate

For each of the four actual parity corners, form
\[
P_a(t)=E_a(t)E_b(t)+tO_a(t)O_b(t),\qquad
Q_a(u)=(1-u)^7P_a\!\left(\frac{u}{1-u}\right),\quad 0\le u\le1.
\]
The endpoints are included by polynomial continuation. The exhaustive dyadic Bernstein subdivision, all leaf intervals and exact minima are in `frontier-20261029-difficult-box-pole-synthesis-frozen-v1.json`, SHA-256 `1efd0db940af93860cd909b804bf421e60b7c20223ab0076d04a09e8c95724e5`. In corner order \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\), the four leaf counts are \(13,25,31,20\). Every degree-seven Bernstein coefficient on every leaf is strictly positive. Their global minimum is
\[
\Delta=\frac{8398254552985521971848465906907312923264484923271867}
{74828883831342229412028663435073690606383746200371200000000000}>10^{-13}. \tag{3}
\]
Because the Bernstein basis is nonnegative and sums to one, (3) implies
\[
P_a(t)/(1+t)^7\ge\Delta>10^{-13}
\]
for every corner and every \(t\ge0\). The pairing is affine in the independent coefficients, so the minimum at each fixed \(t\) occurs at one of these four actual corners. Therefore the same margin holds for the entire box.

As a separate arithmetic route on the same host, the exact Sturm sequences of the four compactified polynomials have variation counts \((3,3),(3,3),(3,3),(4,4)\) at \(u=0,1\), respectively, with both endpoint values positive. This establishes the same absence of interior roots; the Bernstein certificate additionally provides the quantitative uniform bound. These are same-host rational calculations, not independent-model or formal verification.

## 3. Stability without assuming a prior box result

The numerator in (2) is Hurwitz. Set \(H(s)=\prod_i(s^2+x_i)\), where \(x=(1,35,455)\). For \(\operatorname{Re}s>0\),
\[
\frac{b(s)}{H(s)}=c+ds+\sum_iw_i\frac{s}{s^2+x_i},
\quad
\frac{s}{s^2+x_i}=\frac12\left(\frac1{s-i\sqrt{x_i}}+\frac1{s+i\sqrt{x_i}}\right).
\]
All \(c,d,w_i>0\), and every displayed reciprocal has positive real part, so \(b/H\) has positive real part in the open right half-plane. There are no zeros there. On the imaginary axis away from the three zeros of \(H\), \(b/H\) has real part \(c>0\); at each zero of \(H\), the corresponding nonzero residue term in (2) makes \(b\ne0\). The origin is also nonzero. Hence \(b\) is strictly Hurwitz.

For any member \(a\), the positive pairing means \(\operatorname{Re}(a(i\omega)/b(i\omega))>0\) on the imaginary axis. The path \((1-\theta)b+\theta a\) therefore has no imaginary-axis root, and its leading coefficient stays one. It begins at the Hurwitz polynomial \(b\), so root continuity shows \(a\) is Hurwitz. This establishes the denominator hypothesis independently of the earlier finite-node packet. Dividing the positive pairing by \(|a(i\omega)|^2\) proves strict SPR of \(b/a\).

## 4. Explicit endpoint-neighborhood continuation

The same \(b\) works for **every** interval box whose 14 endpoints differ independently from the displayed endpoints by at most \(\varepsilon=10^{-21}\). Widths remain strictly positive and lower endpoints remain positive by the exact guards in the frozen certificate. For each new member \(a'\), clamp each nonleading coefficient into its old interval to obtain \(a\in K\), with \(|a'_j-a_j|\le\varepsilon\).

Let \(S=\sum_{j=0}^{7}b_j=1242874971/625\). Every monomial in the pairing difference has nonnegative degree \(r\le6\) in \(t\), and \(t^r\le(1+t)^7\) for \(t\ge0\). Hence
\[
\frac{|P_{a',b}(t)-P_{a,b}(t)|}{(1+t)^7}\le7\varepsilon S<\tfrac12\cdot10^{-13}.
\]
The last strict rational inequality follows from \(14\varepsilon S<10^{-13}\), explicitly checked in the frozen record. Thus the new box retains a strictly positive pairing at every finite frequency. The same homotopy from the fixed Hurwitz \(b\) proves that **every** new denominator is Hurwitz. This is a 14-endpoint-dimensional open neighborhood with one fixed numerator; the very small displayed radius is sufficient, not claimed optimal.

## 5. Limits

The one explicit box is the same literal input used in `frontier-20261029-five-node-two-triad-coupling-v1.md`, but the stability and positivity proof here does not assume any unreviewed claim in that packet. All 89 exact Bernstein leaves, the bound and perturbation guards were computed with integer and `fractions.Fraction` arithmetic in one Eval host. No separate checker or independent reviewer has replayed them. Formula (2), four-corner affine minimization, complex right-half-plane positivity and root homotopy are written deductions. No formal proof, arbitrary-box conclusion, global negative certificate or novelty claim is made. The unrestricted original septic synthesis-or-obstruction decision remains **OPEN**.
