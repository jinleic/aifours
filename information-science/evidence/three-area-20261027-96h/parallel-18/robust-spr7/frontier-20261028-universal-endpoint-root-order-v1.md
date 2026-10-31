# Universal endpoint-root order and forced maximal contact pattern

**Status: WRITTEN; author candidate, not parent adoption.** This structural result applies to every strictly Hurwitz-stable independent monic septic coefficient box. It is not a universal common-SPR theorem or a negative certificate.

Let \(E_-,E_+,O_-,O_+\) be the actual parity endpoints, with the lower/upper labels denoting their pointwise order for \(t>0\). Write their simple positive roots as \(e_i^-,e_i^+,o_i^-,o_i^+\), \(1\le i\le3\). If at least one even and at least one odd coefficient width are nonzero, then necessarily
\[
0<e_1^-<e_1^+<o_1^-<o_1^+
<e_2^+<e_2^-<o_2^+<o_2^-
<e_3^-<e_3^+<o_3^-<o_3^+.
\]
If a whole parity group has zero width, its corresponding \(+\) and \(-\) roots coincide; the strict inequalities between the six even/odd root bands remain. Conversely, positivity of the leading even endpoint coefficient, simple positive endpoint roots, and the displayed chain with only those within-parity equalities allowed are sufficient for strict Hurwitz stability of the entire coefficient box.

## Proof

The parity differences are pointwise nonnegative polynomials with nonnegative coefficients:
\[
E_+(t)-E_-(t)=\Delta a_0+\Delta a_2t+\Delta a_4t^2+\Delta a_6t^3,\qquad
O_+(t)-O_-(t)=\Delta a_1+\Delta a_3t+\Delta a_5t^2.
\]
Each is strictly positive for \(t>0\) whenever its parity group has a nonzero width. Every actual corner \((E_\pm,O_\pm)\) is Hurwitz. By odd-degree Hermite–Biehler, its roots interlace as
\[
0<e_1<o_1<e_2<o_2<e_3<o_3.
\]
All four combinations therefore give disjoint ordered even/odd bands. Compare \(E_-\) and \(E_+\) using the common odd endpoint \(O_-\). In the first, second and third even bands, the sign of \(E_+\) before its own root is respectively \(+,-,+\), and after it is \(-,+,-\). At each \(E_-\) root, \(E_+>0\). Hence
\[
e_1^-<e_1^+,\quad e_2^+<e_2^-,\quad e_3^-<e_3^+.
\]
The same argument, with the common even endpoint \(E_-\), gives
\[
o_1^-<o_1^+,\quad o_2^+<o_2^-,\quad o_3^-<o_3^+.
\]
Combining these orders with the six-band separation yields the stated twelve-root chain. If a parity group is degenerate its two endpoint polynomials, and therefore their roots, are identical.

For the converse, the chain implies Hermite–Biehler interlacing for all four actual parity corners. Their positive endpoint coefficients follow from their positive roots and positive leading magnitudes. At every \(t>0\), the ranges \([E_-(t),E_+(t)]\) and \([O_-(t),O_+(t)]\) can simultaneously contain zero only if \(t\) belongs to both an even and an odd root band; the chain excludes that. At \(t=0\), the constant coefficient is positive. Thus the connected coefficient box has no imaginary-axis crossing. Since one corner is Hurwitz, homotopy proves that every member is Hurwitz. This argument uses the actual independent parity ranges, not an artificial hull of different coefficients.

## Forced five-contact structure

Consider a boundary limit of strictly stable boxes whose four parity endpoint cubics retain simple positive roots and nondegenerate parity widths. Suppose the five *successive* even/odd band separations all close, at distinct values \(t_1<t_2<t_3<t_4<t_5\). Continuity of the chain forces the five contacts
\[
(e_1^+,o_1^-)=t_1,\quad(o_1^+,e_2^+)=t_2,\quad
(e_2^-,o_2^+)=t_3,\quad(o_2^-,e_3^-)=t_4,\quad
(e_3^+,o_3^-)=t_5.
\]
The remaining outer roots are \(e_1^-=u<t_1\) and \(o_3^+=v>t_5\). Hence the endpoint root allocations are forced:
\[
E_-:\ (u,t_3,t_4),\quad E_+:\ (t_1,t_2,t_5),\qquad
O_-:\ (t_1,t_4,t_5),\quad O_+:\ (t_2,t_3,v).
\]
The chain is weak across the five closed separations but remains strict inside each parity band because the relevant endpoint difference is strictly positive at positive roots. Therefore the five-contact pattern studied in `frontier-20261028-five-contact-all-admissible-nodes-v1.md` is not an arbitrary choice of endpoint allocation: it is the only possible allocation under these hypotheses. In particular that theorem covers **all** such coefficient-admissible five-contact boxes whose first four contact values are proportional to \((1,2,3,6)\), not merely one of several possible endpoint assignments. It still does not cover arbitrary contact ratios or arbitrary stable boxes.

The proof imports the classical odd-degree Hermite–Biehler criterion and otherwise uses pointwise parity ordering and connected homotopy. No numerical search, formal verification, cross-vendor review, or novelty clearance is claimed.
