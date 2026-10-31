# A common septic numerator may require at least four nonreal roots

**Status: WRITTEN candidate, with an explicit WRITTEN-checked-in-kernel box; author result, not parent adoption.** There is a full seven-dimensional strictly Hurwitz-stable monic septic interval box with a common SPR numerator, for which **every** common numerator has at least two nonreal conjugate root pairs. Thus neither real-rooted numerators nor numerators with only one nonreal pair suffice in general. The same phenomenon extends to arbitrarily high odd degree. This is a genuine root-geometry obstruction to a restricted synthesis strategy, not an unrestricted negative certificate.

## An explicit septic box

Let
\[
a(s)=(s+1)\left((s+\tfrac1{100})^2+1\right)^3
=s^7+\sum_{j=0}^6a_js^j.
\]
Choose each \(p_j\) independently from \([a_j-10^{-16},a_j+10^{-16}]\), with \(p_7=1\). All seven widths are positive. This box is strictly Hurwitz and the fixed numerator \(b=a\) is common SPR for it. Nevertheless any common exact-degree-seven real numerator has **at least four nonreal roots counted with multiplicity**.

For the positive synthesis, put \(t=\omega^2\), \(A=10001/10000\), and \(c=1/20000\). Exact rational calculation gives
\[
(t-A)^2+\frac{t}{2500}-c(1+t)^2>0\quad(t\ge0),
\]
because its leading coefficient is positive and its discriminant is \(-399999999/500000000000<0\). Hence
\[
\frac{|a(i\omega)|^2}{(1+\omega^2)^7}\ge c^3=\frac1{8000000000000}=:\delta>0.
\]
Let \(S=\sum_{j=0}^7|a_j|=8243632180601/500000000000\). Any box member and the straight coefficient path back to \(a\) move each of the seven nonleading coefficients by at most \(r=10^{-16}\), so
\[
\frac{|P_{p,a}(t)-|a(i\sqrt t)|^2|}{(1+t)^7}\le7rS\le\delta/2.
\]
The pairing stays positive along that path; in particular it excludes imaginary-axis roots. Since \(a\) is Hurwitz, homotopy proves every box member Hurwitz and \(a/p\) is strictly positive real. All lower endpoints stay positive.

## Root-count obstruction by phase variation

Suppose \(b/p\) is common SPR; in particular \(b/a\) is SPR. After positive leading-coefficient normalization, \(b\) is Hurwitz: the segment \((1-\tau)a+\tau b\) has positive real ratio to \(a\) on the imaginary axis, hence no imaginary-axis zeros, and stays monic. Let \(\theta_a,\theta_b\) be their continuous unwrapped phases on \(\omega\ge0\), with phase zero at \(\omega=0\). The continuous difference cannot leave \((-\pi/2,\pi/2)\), so for any \(0<\omega_-<\omega_+\),
\[
\Delta\theta_b>\Delta\theta_a-\pi.
\]

Take \(\omega_-=9/10\), \(\omega_+=11/10\). Each quadratic factor has positive imaginary part. Its phase moves from less than \(\arctan(180/1901)\) to more than \(\pi-\arctan(220/2099)\). Using \(\arctan x<x\) for \(x>0\),
\[
\frac{180}{1901}+\frac{220}{2099}
=\frac{796040}{3990199}<\frac14.
\]
The linear factor's phase is increasing, so \(\Delta\theta_a>3\pi-3/4\), and consequently
\[
\Delta\theta_b>2\pi-3/4.\tag{1}
\]

If \(b\) had at most one nonreal conjugate pair, that pair contributes a phase increase strictly less than \(\pi\). Each of the other at least five roots is real and negative; for any real-negative-root factor \(s+r\),
\[
\frac{d}{d\log\omega}\arg(r+i\omega)
=\frac{\omega r}{r^2+\omega^2}\le\frac12.
\]
There are at most seven such factors. With zero conjugate pairs,
\[
\Delta\theta_b<\frac72\log(11/9)<\frac79<1;
\]
with exactly one pair,
\[
\Delta\theta_b<\pi+\frac52\log(11/9)<\pi+\frac59.
\]
Both contradict (1), since \(\pi>3\). Thus at least two conjugate pairs are necessary. Multiplicity is included, and the proof makes no assumption that \(b\) is a particular polynomial form.

## General odd-degree version

For every \(n=2m+1\ge5\), put
\[
d=\frac1{10n},\quad \eta=\frac1{100n^2},\quad
 a_n(s)=(s+1)\bigl((s+\eta)^2+1\bigr)^m.
\]
There is a full-width strictly stable interval neighborhood of \(a_n\), with common numerator \(a_n\), such that every common numerator has at least \(m-1\) nonreal conjugate pairs. For the phase proof use \(\omega_\pm=1\pm d\). The absolute real part of each quadratic at either endpoint is at least \(d\), and its imaginary part is at most \(4\eta\). Hence each quadratic's phase rise exceeds \(\pi-8\eta/d=\pi-4/(5n)\). The increasing linear factor gives
\[
\Delta\theta_{a_n}>m\pi-\frac{4m}{5n},\qquad
\Delta\theta_b>(m-1)\pi-\frac{4m}{5n}.
\]
With at most \(m-2\) nonreal pairs, the same rootwise bounds give
\[
\Delta\theta_b<(m-2)\pi+\frac n2\log\frac{1+d}{1-d}
<(m-2)\pi+\frac{nd}{1-d}.
\]
The two error terms sum to less than one for \(n\ge5\), so \(\pi>3\) yields a contradiction.

An explicit neighborhood is obtained without a numerical search. For \(0<\eta\le1/10\) and \(t\ge0\),
\[
\frac{(t-(1+\eta^2))^2+4\eta^2t}{(1+t)^2}\ge\frac{\eta^2}{5}.
\]
For \(t\le1/2\), the square term gives at least \(1/9\); for \(1/2\le t\le2\), the \(4\eta^2t\) term gives at least \(2\eta^2/9\); for \(t\ge2\), the square term gives at least \(4/81\). Put \(\delta_n=(\eta^2/5)^m\), \(S_n=\sum|[s^j]a_n|\), and choose each nonleading coefficient radius
\[
r_n=\min\!\left(\frac12\min_{j<n}[s^j]a_n,\ \frac{\delta_n}{4n(1+S_n)}\right)>0.
\]
The same normalized pairing estimate and homotopy prove stability and common numerator \(a_n\) throughout that independent full-width box.

## Evidence and limits

Frozen septic coefficients, safety constants and exact phase deficits: `frontier-20261029-four-nonreal-roots-box-frozen-v1.json`, SHA-256 `58b4dade994bc008bdda290c11e8c3d352be9d2fe5379cc1911417678f42ae15`. Independent checker `frontier-20261029-four-nonreal-roots-box-independent-kernel-v1.py`, SHA-256 `440967fa07788603e25c360b72c9dacc6f6b3776c0c9bdbac2564487ed6cd8c6`; receipt `frontier-20261029-four-nonreal-roots-box-independent-result-v1.json`, SHA-256 `cc8926df50f39e3b9170281347222864dffc20eb608e0724f80ea3e23c94742c`.

The specific rational identities were checked with exact integers and `fractions.Fraction` on one Python Eval host. Root factorization, phase unwrapping, elementary inequalities, and the general-degree argument are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
