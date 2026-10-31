# A simple two-atom obstruction to choosing the numerator from the family

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This gives an explicit strictly Hurwitz-stable, full seven-dimensional septic interval box \(K\) with an explicit common SPR numerator, but **no monic common SPR numerator inside \(K\)**. The obstruction persists throughout a nonempty 14-dimensional endpoint neighborhood and even forces an explicit positive coefficient distance from each perturbed box. It is not a counterexample to unrestricted common SPR.

## The box and an unrestricted common numerator

Set
\[
\begin{aligned}
L(s)&=(s+200)^5\left(s^2+\tfrac1{10}s+1\right),\\
U(s)&=(s+200)^5\left(s^2+\tfrac15s+4\right),\\
V(s)&=(s+200)^5\left(s^2+\tfrac1{10}s+4\right).
\end{aligned}
\]
For each \(j=0,\ldots,6\), independently choose \(a_j\) between the coefficient of \(s^j\) in \(L\) and that in \(U\), with \(a_7=1\). All seven intervals have positive width; \(L,V\in K\). An exact monic common numerator for the whole independent coefficient box is
\[
b_\star(s)=(s+200)^5\left(s^2+10s+\tfrac52\right).
\]
The independent checker verified all 28 leading Hurwitz determinants of the four actual parity corners. The classical Kharitonov theorem proves all-member stability. It also checked 96 strictly positive compactified Bernstein coefficients for the four corner pairings, establishing
\[
\frac{P_{a,b_\star}(t)}{(1+t)^7}\ge1\quad(a\in K,\ t\ge0).
\]
Affine minimization over the actual parity corners extends the pairing bound to the entire box. In particular \(b_\star/a\) is strictly positive real for every \(a\in K\).

## Two positive atoms exclude every numerator inside \(K\)

For monic \(b\), put
\[
F(b)=P_{L,b}(2)+P_{V,b}(3).
\]
The two denominators are actual box members, the two frequencies have \(t=\omega^2>0\), and both weights are one. Its coefficient signs in \((b_0,\ldots,b_7)\) are
\[
(-,+,-,-,+,+,-,-).
\]
Thus the maximum of \(F\) over the **entire** independent numerator box is attained at the mixed coefficient vertex with sides
\[
(\ell_0,h_1,\ell_2,\ell_3,h_4,h_5,\ell_6),
\]
and direct exact evaluation yields
\[
\max_{b\in K}F(b)=-\frac{8792741287791347797871307}{100}<0.
\]
Any common SPR numerator would make both summands strictly positive. Therefore no monic \(b\in K\) works. The known external \(b_\star\) instead satisfies
\[
F(b_\star)=\frac{819468836482544090601311}{2}>0.
\]
The mixed coefficient signs show that this is **not** a negative-coordinate certificate against unrestricted numerators.

## Open neighborhood and explicit distance

Perturb each of the 14 endpoints of \(K\) independently by at most \(\varepsilon=10^{-14}\), keeping the leading coefficient one; call the resulting box \(K'\). Every \(K'\) remains strictly Hurwitz and has the same common numerator \(b_\star\). Moreover every monic common numerator \(b\) for \(K'\) obeys
\[
\operatorname{dist}_\infty((b_0,\ldots,b_6),K')>8{,}000{,}000{,}000.
\]
The distance is in coefficient coordinates and depends on monic normalization; no scale-invariant numerical claim is intended.

For the anchor, let \(C_0,\ldots,C_7\) be the two-atom coefficient vector and put
\[
M=\frac{8792741287791347797871307}{100},\qquad
T=\sum_{j=0}^6|C_j|=9775780490882,\qquad d=8{,}000{,}000{,}000.
\]
Enlarging every anchor coefficient interval by \(d\) on each side changes the affine maximum to \(-M+dT=-M_d\), where
\[
M_d=\frac{972116895085747797871307}{100}>0.
\]
For \(K'\), project the two original atom denominators coefficientwise into \(K'\); they move by at most \(\varepsilon\). A numerator within distance \(d\) of \(K'\) is likewise within \(\varepsilon\) of the anchor's \(d\)-expanded box. The direct monomial triangle bound for this two-atom functional gives perturbation at most \(\varepsilon L_d\), where
\[
L_d=154188131857745,\qquad 2\varepsilon L_d\le M_d.
\]
Hence its two-atom sum is strictly negative, contradicting common SPR. The checker also establishes that the perturbed intervals remain positive-width, and that
\[
14\varepsilon\sum_{j=0}^7|b_{\star,j}|\le1,
\qquad \sum_{j=0}^7|b_{\star,j}|=\frac{8858170827027}{2}.
\]
For any perturbed denominator and the straight path back to its coefficientwise projection in \(K\), the normalized pairing can therefore decrease by at most \(7\varepsilon\sum|b_{\star,j}|\le1/2\). It stays positive at every frequency, excludes imaginary-axis crossings, and homotopy preserves Hurwitz stability and common SPR. This proves the entire endpoint neighborhood, not just sampled boxes.

## Evidence and limitations

Anchor inputs and dyadic leaves: `frontier-20261028-lifted-simple-no-family-frozen-v1.json`, SHA-256 `64a15a865f342f47beb94146503f67ee235acf53f15b905bb95e7c0427908800`. Open-separation constants: `frontier-20261028-lifted-simple-open-separation-frozen-v1.json`, SHA-256 `ac3dfb6ddae33393572ceba011db84913dc6df3f4323081dba5b754b1d3f4efc`. The independent checker `frontier-20261028-lifted-simple-open-separation-independent-kernel-v1.py`, SHA-256 `aaa5cffb1cc232b4d385e8e405fa54ed2cbfcf2091a41be71a0635e7b60d2eb3`, expands the factors afresh, verifies all anchor minors and pairing leaves, maximizes the two-atom form over the **full** coefficient box, and recomputes the seven robust inequalities. Receipt: `frontier-20261028-lifted-simple-open-separation-independent-result-v1.json`, SHA-256 `5cca34072827c53c32ce5dfd7b38e4f323c5677bf315ae0e00eebdb8368a8e30`.

The finite identities use exact integers and `fractions.Fraction` on one Python Eval host; Kharitonov, affine minimization, and homotopy are named written imports or deductions. No formal proof, cross-vendor review, novelty clearance, universal positive conclusion, or unrestricted negative certificate is claimed.
