# A stable septic box whose common numerator must leave the family

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** There is a strictly Hurwitz-stable seven-dimensional septic interval box \(K\) for which **no monic common SPR numerator belongs to \(K\)**. Nevertheless, an explicit monic numerator outside \(K\) does work. Thus selecting the common numerator from the denominator family is not a valid general proof strategy. This is a genuine obstruction to that restricted strategy, **not** a negative answer to the original unrestricted problem.

## Box and three-atom certificate

Use the exact interval box \(K\) and the four actual parity corners in `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`. Write them \(a_{--},a_{-+},a_{+-},a_{++}\). For a real monic septic numerator \(b\), put
\[
F(b)=10^{12}P_{a_{-+},b}(32503/265)
+53P_{a_{+-},b}(262119/25)
+14P_{a_{++},b}(262123/21).
\]
All three weights are strictly positive, all three denominators are actual members of \(K\), and the three arguments are \(t=\omega^2>0\). The function \(F\) is affine in the seven free coefficients of a monic \(b\). Exact coefficient accumulation gives coordinate signs
\[
(C_0,\ldots,C_7):\quad (+,+,-,-,+,-,+,-).
\]
Consequently the maximum over the **full** independent numerator box is attained at the mixed vertex with sides
\[
(h_0,h_1,\ell_2,\ell_3,h_4,\ell_5,h_6),
\]
not necessarily at one of its four parity corners. Direct rational evaluation gives
\[
\max_{b\in K}F(b)=
-\frac{2267533640364343317259095319125151909302637034028471098859237860674482800551913}
{12981592480036971812065388789760000000000000000000000}<0.
\]
If \(b\) were common SPR for \(K\), every pairing on the three atoms would be strictly positive, so \(F(b)>0\), a contradiction. Hence no \(b\in K\) can be common SPR. Since a common exact-degree-seven numerator has positive leading coefficient, the same conclusion applies after the usual positive monic normalization.

## Scope and independent replay

The independently checked unrestricted numerator in the cited synthesis packet satisfies
\[
F(b)=\frac{2712053100045033634150247580676752869065227161332998192217264803047281}
{77376320839148591828736000000000000000000}>0,
\]
and is common SPR for all of \(K\). The coefficient sums above are mixed in sign, so the three-atom functional is **not** a strict negative-coordinate certificate excluding all positive numerators. The unrestricted decision remains open.

The independent checker reconstructed all four denominator corners, verified their **28 strict Hurwitz determinants**, accumulated the three pairing rows by a direct even-monomial convolution, maximized the affine form over the full coefficient box using its coordinate signs, and checked both displayed exact values. The full-family stability uses the classical Kharitonov theorem; the known unrestricted numerator's separate all-frequency certificate is in the cited synthesis packet.

Frozen exact box, atoms, weights and values: `frontier-20261028-sturm-band-full-box-obstruction-frozen-v1.json`, SHA-256 `5bc88140adab434f8cfb59a32640e49af34483bad6c0ae1da7c50b8f172fee92`. Independent checker `frontier-20261028-sturm-band-full-box-obstruction-independent-kernel-v1.py`, SHA-256 `70aa62831f0b47a9f6f493bb898a2f0aa494e85f2bb811714c0d566d0dcf5134`; receipt `frontier-20261028-sturm-band-full-box-obstruction-independent-result-v1.json`, SHA-256 `681f70f70a28e75902d27a7fe17ab9c2a263a7acc9ec3fe575f9c37fb98f30b0`.

An earlier two-atom calculation established only a four-corner-hull obstruction but was incorrectly labeled box-wide. Its additive correction is `frontier-20261028-sturm-band-box-numerator-obstruction-erratum-v1.md`, SHA-256 `c2a4c9fa944cd83c3b9512d99add6d319f8293caed2013d414ddf504d2381641`. The three-atom certificate above is a **separate, directly maximized** proof over all coefficients; it does not rely on the withdrawn inference.

All finite arithmetic was exact integer/`fractions.Fraction` work on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, unrestricted negative certificate, or universal positive theorem is claimed.
