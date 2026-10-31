# Common SPR numerators for compact odd-degree families with one fixed parity

**Status: WRITTEN theorem with WRITTEN-checked-in-kernel septic examples; author candidate, not a parent adoption.** This is a general positive result for a genuine restricted subfamily, including degree seven. It does **not** resolve boxes in which both parity components vary. No novelty claim is made.

## Theorem

Let \(m\ge1\), and let \(\mathcal A\) be a compact set of real monic strictly Hurwitz polynomials of degree \(2m+1\). Write
\[
p(s)=E_p(-s^2)+sO_p(-s^2).
\]
If either all \(E_p\) are the same polynomial or all \(O_p\) are the same polynomial, there is one real polynomial \(b\) of **exactly** degree \(2m+1\) such that
\[
\operatorname{Re}\frac{b(i\omega)}{p(i\omega)}>0
\quad\text{for every }p\in\mathcal A\text{ and every }\omega\in\mathbb R.
\]
This includes every all-member-stable septic interval box with all four even coefficients fixed or with all three variable odd coefficients fixed. Compactness matters: it supplies uniform strict margins over the family.

For \(t=\omega^2\), put \(P_{p,b}(t)=F_b(t)E_p(t)+tG_b(t)O_p(t)\), where \(b(s)=F_b(-s^2)+sG_b(-s^2)\). Its sign is the sign of the real part because the stable denominator is nonzero on the imaginary axis.

## Construction and proof

The Hermite–Biehler criterion for a monic Hurwitz polynomial of odd degree gives simple positive roots
\[
0<\alpha_1<\beta_1<\alpha_2<\beta_2<\cdots<\alpha_m<\beta_m,
\]
where the \(\alpha_i\) are roots of \(E_p\) and the \(\beta_i\) are roots of \(O_p\). Both parity polynomials are positive at zero and have degree \(m\), with leading terms \((-1)^m a_{2m}t^m\) and \((-1)^m t^m\), respectively. Thus at these roots
\[
-E_p'(\alpha_i)O_p(\alpha_i)>0,\qquad
E_p(\beta_i)O_p'(\beta_i)>0.
\]
These strict signs are uniform over a compact family when the indicated roots are fixed.

### Fixed odd component

Suppose \(O_p=O\) for all \(p\), and let \(\beta_1\) be its smallest root. Choose any \(\zeta\in(0,\beta_1)\), define
\[
F(t)=(t-\zeta)O'(t),\qquad b_\varepsilon(s)=\varepsilon F(-s^2)+sO(-s^2).
\]
The numerator is monic of exact degree \(2m+1\), and its pairing is
\[
P_{p,b_\varepsilon}(t)=tO(t)^2+\varepsilon F(t)E_p(t).
\]
At every \(\beta_i\), \(F(\beta_i)E_p(\beta_i)>0\) uniformly. At \(t=0\), \(F(0)=-\zeta O'(0)>0\) because \(O'(0)=-a_3<0\), and \(E_p(0)>0\) uniformly. By uniform continuity, the second term is strictly positive on common neighborhoods of zero and all \(\beta_i\).

Outside these neighborhoods on a fixed compact half-interval, \(tO(t)^2\) has a strictly positive minimum and \(F E_p\) is uniformly bounded. For sufficiently large \(t\), the leading terms of \(F\) and \(E_p\) have the same sign uniformly, so \(F E_p>0\). One sufficiently small positive \(\varepsilon\) therefore makes the pairing strictly positive for the entire half-line and all \(p\in\mathcal A\).

### Fixed even component

Suppose \(E_p=E\) for all \(p\), with roots \(\alpha_i\). Choose
\[
0<\eta<\min_i\frac{|E'(\alpha_i)|}{\alpha_i^m},\qquad
G_\eta(t)=-E'(t)+\eta(-1)^m t^m,
\]
and put
\[
b_{\varepsilon,\eta}(s)=E(-s^2)+\varepsilon sG_\eta(-s^2).
\]
Its leading coefficient is \(\varepsilon\eta>0\), so its degree is exactly \(2m+1\). The pairing is
\[
P_{p,b_{\varepsilon,\eta}}(t)=E(t)^2+\varepsilon tG_\eta(t)O_p(t).
\]
The choice of \(\eta\) preserves the sign of \(-E'(\alpha_i)\), so \(G_\eta(\alpha_i)O_p(\alpha_i)>0\) uniformly. Common neighborhoods of the roots therefore have positive second term, and \(E(0)^2>0\). Outside those neighborhoods on a fixed compact interval, \(E^2\) has a positive minimum and \(tG_\eta O_p\) is uniformly bounded. At sufficiently large \(t\), the leading terms of \(G_\eta\) and every \(O_p\) have the same sign uniformly. Choosing one sufficiently small \(\varepsilon>0\) proves strict positivity everywhere. Dividing by its positive leading coefficient makes the numerator monic if wanted.

The proof uses only the named Hermite–Biehler interlacing theorem, continuity/compactness, and elementary polynomial signs. It applies to compact stable sets, not merely boxes. The degree-one case is elementary but is not needed for the septic application.

## Exact septic examples

Both examples are subboxes of the independently checked five-contact family at scale \(\rho=1/2\); their nonfixed parity coefficients retain nonzero interval widths. Four-corner values below include repetitions from the fixed parity. All coefficients are ascending.

| Fixed parity | Parameters | One exact numerator | Lower bound for \(P/(1+t)^7\) |
|---|---|---|---|
| odd | \(\zeta=1/2,\ \varepsilon=1/10\) | \((123/40,57,77/10,123/2,13/4,31/2,3/10,1)\) | \(162214533/481036337152\) |
| even | \(\eta=1/10000,\ \varepsilon=1/10\) | \((2509/190,1977/760,1977/76,1979/900,1979/180,461/1425,922/855,1/100000)\) | \(1/100000\) |

The odd example's fixed \(O\) is strictly positive on \([0,1]\), so \(\zeta=1/2\) lies before its first root. The even example's exact half-line pairing certificate independently establishes its chosen parameters work; the example does not substitute for the general written proof.

Frozen endpoints, pairing polynomials, leaves and margins: `frontier-20261028-fixed-parity-septic-examples-frozen-v1.json`, SHA-256 `bd032a29ef541d3e628209814ba8a8bdd79ec2a786d7b15c076d64e57319736b`. Standalone independent checker `frontier-20261028-fixed-parity-independent-replay-kernel-v1.py`, SHA-256 `591a6f4621097ba54abf02924be10f06d71c543b07d2fb26c82f57317e505161`, reconstructs both formulas, subbox inclusions, 56 rational corner Hurwitz minors, every Bernstein leaf, the fixed-\(O\) sign check and the two margins, and rejects a corrupted leaf. Receipt `frontier-20261028-fixed-parity-independent-replay-result-v1.json`, SHA-256 `37ce59a986848ab13c4f86161ba9fa064cd4be13eca0e390f70d0e97fe4d529e`.

As context only, the publicly available [sixth-order interval SPR preprint](https://arxiv.org/html/2609.26541v1) states a fixed-even sextic construction and an unrestricted sextic existence result; this packet does not import those results or claim this odd-degree observation is novel. The general theorem above is a written argument, not a machine-checked universal quantification, formal proof, cross-vendor review, or unrestricted septic verdict.
