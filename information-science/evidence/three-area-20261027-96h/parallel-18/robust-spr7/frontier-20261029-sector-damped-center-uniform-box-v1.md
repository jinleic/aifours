# Uniform interval-box synthesis around sector-damped complex centers

**Status: WRITTEN; author candidate, not parent adoption.** The all-degree theorem in `frontier-20261029-real-rooted-center-uniform-box-theorem-v1.md` extends beyond real-rooted centers. In particular it covers full-dimensional boxes around centers with arbitrarily many nonreal conjugate root pairs. It is not an arbitrary-box theorem.

Let \(a\) be monic real degree \(n\), with all real roots \(-\alpha\), \(\alpha\ge c>0\), and each nonreal conjugate pair \(-\alpha\pm i\beta\) satisfying
\[
\alpha^2-\beta^2\ge c^2.
\]
For any \(0\le r<1\), independently vary its nonleading coefficient \(a_j\) by at most \(r c^{n-j}\). Then every resulting polynomial is strictly Hurwitz and the fixed numerator \(a\) is common SPR. With \(B=a(c)/c^n>0\), the same explicit ratio bound holds:
\[
\operatorname{Re}\frac{a(i\omega)}{p(i\omega)}
\ge\frac{1-r}{(B+nr)^2}>0.
\]
The universal threshold \(r<1\) remains sharp because the all-real center \((s+c)^n\) is included and its constant-coefficient lower endpoint is zero at \(r=1\).

**Proof.** After the scaling \(s=cz\), each real factor has squared imaginary-axis modulus at least \(1+t\). Each conjugate pair gives
\[
\left|\left(i\sqrt t+\frac\alpha c\right)^2+\left(\frac\beta c\right)^2\right|^2
=t^2+2\frac{\alpha^2-\beta^2}{c^2}t
+\frac{(\alpha^2+\beta^2)^2}{c^4}\ge(1+t)^2.
\]
Therefore the scaled center satisfies \(|A(i\sqrt t)|^2\ge(1+t)^n\). The geometric-sum Cauchy–Schwarz argument and homotopy in the cited theorem depend only on this modulus bound, not on individual real roots, and apply unchanged. ∎

For instance, \(a(s)=(s+1)((s+2)^2+1)^3\), \(c=1\), has six nonreal roots and satisfies the hypothesis; every independent coefficient box of scaled radius \(r<1\) centered there has \(a\) as a common numerator. This illustrates compatibility with the separate result that some boxes require nonreal numerator roots.

The proof is written mathematics using factorwise modulus comparison, the cited Cauchy–Schwarz lemma and homotopy. No formal proof, cross-vendor review, novelty clearance, universal arbitrary-box conclusion, or unrestricted negative certificate is claimed.
