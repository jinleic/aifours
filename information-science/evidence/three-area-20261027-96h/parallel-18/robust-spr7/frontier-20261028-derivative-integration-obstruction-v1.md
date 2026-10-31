# A prescribed derivative-family numerator need not lift by integration

**Status: WRITTEN-checked-in-kernel for the explicit example; author candidate, not parent adoption.** This closes a tempting but invalid route from the sixth-order result to the original septic problem. It is not a counterexample to septic SPR synthesis: the box below has a different explicit common numerator.

## The derivative reduction and its limitation

For every all-member-Hurwitz monic septic interval box, the normalized derivative \(q=p'/7\) ranges over a monic sextic interval box: its coefficients are \(q_k=(k+1)p_{k+1}/7\), independently for \(k=0,\ldots,5\). Every such derivative is Hurwitz by the Gauss–Lucas theorem, since the convex hull of strictly left-half-plane roots stays strictly left. Thus the sextic derivative box is robustly Hurwitz.

However, even if one has a common sextic SPR numerator \(c\) for that derivative box, it is **false** that some integration constant \(\beta\) necessarily makes
\[
b_\beta(s)=\beta+7\int_0^s c(z)\,dz
\]
a common septic SPR numerator. The following exact full-width box disproves that implication for a specified valid \(c\).

## Exact counterexample to the integration implication

Let \(p_*(s)=(s+1)^7\), and let all seven lower coefficients vary independently by \(\pm10^{-6}\), with leading coefficient one. All seven widths are positive. The whole box is Hurwitz and has the common numerator \(p_*\): \(|p_*(i\sqrt t)|^2=(1+t)^7\), \(\sum|p_{*,j}|=128\), and the coefficient perturbation bound gives
\[
P_{p,p_*}(t)/(1+t)^7\ge1-128\cdot7\cdot10^{-6}=15611/15625>0.
\]
The same positivity throughout the homotopy to \(p_*\) excludes imaginary-axis crossings and establishes all-member stability.

The derivative center is \(q_*=(s+1)^6\). Choose
\[
c(s)=(s+1)^6+2,
\quad(c_0,\ldots,c_6)=(3,6,15,20,15,6,1).
\]
Its center pairing is
\[
H(t)=3-24t+45t^2+18t^3+15t^4+6t^5+t^6,
\quad H(t)/(1+t)^6\ge5/1024.
\]
This can be read from the exact four-leaf certificate. It also has an elementary sign proof: the quadratic part is \(45(t-1/5)(t-1/3)\); outside \([1/5,1/3]\) it is nonnegative. On \([1/5,7/30]\) it is at least \(-3/20\), while \(18t^3+15t^4\ge21/125>3/20\). On \([7/30,1/3]\) it is at least \(-1/5\), while \(18t^3\ge343/1500>1/5\).

For the entire derivative box, the coefficient \(\ell^1\)-deviation from \(q_*\) is at most \(3\cdot10^{-6}\), and \(\sum|c_j|=66\). Thus the compactified pairing remains at least
\[
5/1024-66\cdot3\cdot10^{-6}=74957/16000000>0.
\]
Every derivative denominator is Hurwitz, as just proved, so this **particular** \(c\) is a common sextic SPR numerator.

Integration gives
\[
b_\beta(s)=\beta+21s+21s^2+35s^3+35s^4+21s^5+7s^6+s^7.
\]
At the central septic \(p_*\), exact pairings at two positive squared frequencies are
\[
P_{p_*,b_\beta}(1)=8(\beta+1),\qquad
P_{p_*,b_\beta}(1/2)=-\frac{13}{8}\beta-\frac{2421}{128}.
\]
Strict positivity would require simultaneously \(\beta>-1\) and \(\beta<-2421/208\), impossible even for an arbitrary real \(\beta\). Since the center is a member of the full box, this prescribed \(c\) cannot be integrated into a common septic numerator.

The obstruction is **not** to all choices of \(c\): \(q_*\) itself is also a common numerator for the small derivative box by the same perturbation bound, and its integral with \(\beta=1\) is \(p_*\), the common numerator already exhibited for the septic box. No statement is made about integrating some other numerator for an arbitrary box.

## Evidence and imports

Frozen endpoints, derivative intervals, exact line tests and complete center/corner Bernstein leaves: `frontier-20261028-derivative-lift-box-obstruction-frozen-v1.json`, SHA-256 `46d821081629ba035892b827c0bcd9d62580304d0843d30a4012d76f02e5c9ef`. Independent standalone checker `frontier-20261028-derivative-lift-independent-kernel-v1.py`, SHA-256 `2d4fd2346b20b024533fea65444a60ce09ba99420e8bb31d4d199a95b0bfc720`, reconstructs the two binomial centers, all 28 septic and 24 derivative-corner Hurwitz minors, every Bernstein coefficient, both margins, the two exact frequency inequalities, and the different-numerator positive control. Receipt `frontier-20261028-derivative-lift-independent-result-v1.json`, SHA-256 `425c24130cda9424fb3477b0c0564f32ecb68f402f75329283912320da53c1ab`.

The first producer invocation encountered a helper-name `TypeError`; its failed step was corrected and resumed, and the frozen output was subsequently independently replayed. The general derivative-stability reduction imports Gauss–Lucas and the written perturbation/homotopy lemma; the cited finite calculations use exact rational arithmetic on one host. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
