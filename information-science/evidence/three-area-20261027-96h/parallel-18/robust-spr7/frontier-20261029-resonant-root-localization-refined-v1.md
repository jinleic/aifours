# Two numerator roots within \(101/1000\) of a narrow resonant segment

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For every stable box in the explicit 14-endpoint neighborhood of `frontier-20261029-resonant-root-localization-open-v1.md`, every common exact-degree-seven numerator has at least two upper-half-plane roots, counted with multiplicity, within distance
\[
\boxed{\frac{101}{1000}}
\]
of the segment \(i[24/25,26/25]\), plus their conjugates. The fixed unrestricted common numerator continues to work. This strengthens the earlier \(91/500\) localization and concerns literal numerator roots, regardless of cancellation.

For the actual retained denominator \(a=(s+1)((s+1/100)^2+1)^3\), let \(\omega_-=24/25\), \(\omega_+=26/25\), \(\Delta=2/25\), and \(A=10001/10000\). Set
\[
q_- =\frac{2\eta\omega_-}{A-\omega_-^2},\quad
q_+=\frac{2\eta\omega_+}{\omega_+^2-A},\quad
z=\frac{\omega_+-\omega_-}{1+\omega_+\omega_-},\quad\eta=1/100,
\]
\[
 e=\left(q_- -\frac{q_-^3}{3}+\frac{q_-^5}{5}\right)
 +\left(q_+ -\frac{q_+^3}{3}+\frac{q_+^5}{5}\right),\qquad
 g=z-\frac{z^3}{3}.
\]
All three arguments lie in \((0,1)\), so alternating arctangent bounds give a quadratic phase deficit less than \(e\), and the real linear factor contributes phase rise greater than \(g\). Therefore
\[
\Delta\theta_a>3\pi-3e+g.
\]
The conjugate-aware criterion supplies the two possible upper phase budgets for a common numerator with zero or one upper root inside the \(R\)-neighborhood. With \(R=101/1000\) and the rational lower bound \(\pi_L=281476/89625<\pi\), the exact checker verifies
\[
\begin{aligned}
2\pi_L&>3e-g+3\Delta/R+4\Delta/(2\omega_-),\\
\pi_L&>3e-g+2\Delta/R+3\Delta/(2\omega_-).
\end{aligned}
\]
Both cases contradict the required common-SPR phase increment. In particular, two upper roots satisfy the weaker rectangular bounds
\[
-\frac{101}{1000}<\operatorname{Re}z<0,\qquad
\frac{859}{1000}<\operatorname{Im}z<\frac{1141}{1000},
\]
with their conjugates reflected below the real axis.

Frozen rational bounds: `frontier-20261029-resonant-root-localization-refined-frozen-v1.json`, SHA-256 `bc2b46631b9000c93fc550edf30f543373e7e2eaa8a712e08aa6694d70d31638`. Independent checker `frontier-20261029-resonant-root-localization-refined-independent-kernel-v1.py`, SHA-256 `aab765d69348ef330d6610574046a25416c60e99773e36a110574429fa354ea5`; receipt `frontier-20261029-resonant-root-localization-refined-independent-result-v1.json`, SHA-256 `f0ced692b20f1fcad6d75626749f93738e18f3aaa604c4e291a5427e545d6554`. The open-box theorem is SHA-256 `9370d7664752dc3cc60b9aa83c2272cd5e8aef656a403add09de991532158b58`.

The finite inequalities use exact integers and `fractions.Fraction` on one Python Eval host; the alternating-series, phase and rootwise estimates are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
