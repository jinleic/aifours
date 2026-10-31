# Exact synthesis for an oscillatory anisotropic septic box

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This new full seven-dimensional interval box was generated from an oscillatory-centered anisotropic family without imposing the five-contact conditions. Its stability and a common degree-seven numerator are certified for all members and all real frequencies. It is not a universal answer to the original problem.

For \(a(s)=s^7+\sum_{j=0}^6a_js^j\), independently let \(a_j\in[\ell_j,h_j]\), with
\[
\begin{array}{c|rr}
j&\ell_j&h_j\\\hline
0&9515838999074276501/104857600000&5335914536004123499/52428800000\\
1&2154858820764754563/20971520000&592168602467245437/5242880000\\
2&5319261176108667111/419430400000&5530382378297732889/419430400000\\
3&538260731369513903/209715200000&161810287126486097/52428800000\\
4&5462065913599479/52428800000&24153390342400521/209715200000\\
5&212625960095989/20971520000&17772401504011/1310720000\\
6&3426410887489/209715200000&1030037112511/52428800000
\end{array}
\]
All seven widths are positive. The numerator with ascending coefficients
\[
(b_0,\ldots,b_7)=
\left(\frac{581401917}{10},\frac{520347753}{2},\frac{1443896043}{5},
\frac{42535235}{2},\frac{34705369}{10},\frac{73352}{5},\frac{1788}{5},1\right)
\]
is common strictly positive real for the whole box. Consequently it also works for every subbox.

## Exact verification

The independent checker reconstructed the four actual Kharitonov parity corners and verified all **28** leading Hurwitz determinants strictly positive by integer Bareiss elimination. The classical Kharitonov theorem then proves every polynomial in the independent coefficient box strictly Hurwitz.

For each corner it independently constructed \(P_{a,b}(t)=E_aE_b+tO_aO_b\), compactified \(t=x/(1-x)\), and checked strict positivity on a dyadic partition of \(x\in[0,1]\). The respective corners required 128, 160, 136 and 120 strictly positive Bernstein coefficients. Their common exact lower bound is
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge
\delta=\frac{8935551948234464603794129462286704554333771}
{11909882842232846221218111260111887400960000000}>0.
\]
The pairing is affine in the independently varying coefficients, and at each frequency its minimum is attained at one of the four actual parity corners. The same bound therefore holds for every member, including the endpoints \(t=0\) and \(t=\infty\). With
\[
S=1+\sum_{j=0}^6 h_j=\frac{96939671769615629267}{419430400000},
\]
we have \(|a(i\omega)|^2\le S^2(1+\omega^2)^7\) and hence the explicit uniform bound
\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge \frac{\delta}{S^2}>0.
\]

The exact search originally required rescaling both numerator coordinates and frequency rows; an integer-simplex solution on 161 sample rows was then simplified to the displayed tenths. Only the subsequently replayed full-half-line Bernstein certificate establishes the claim. Frozen endpoints: `frontier-20261028-sturm-band-strict-certificate-case-00-v1.json`, SHA-256 `9234459cf1cf113dbb4ea823f6197deac094fef1da38494593ae9a66547732e1`. Frozen simplified numerator and frequency leaves: `frontier-20261028-sturm-band-case-00-simple-frozen-v1.json`, SHA-256 `fb469c9df3aff1b7150191ecddc0e52f7dbec3248ff57ffec9c32d1db0f315c9`. Independent checker: `frontier-20261028-sturm-band-case-00-independent-kernel-v1.py`, SHA-256 `cb26b32e4dc22dadcac9d5bfcced563af18f61a1936f3ebd317838063bacad4f`; receipt: `frontier-20261028-sturm-band-case-00-independent-result-v1.json`, SHA-256 `f9cdd256a1249f8c841af2e2478b28918733911b7834ba80426fa85e3fcf5c33`.

The finite arithmetic used integers and `fractions.Fraction` in one Python Eval host. Kharitonov and the affine/compactification arguments are named written imports or deductions. This is not formal verification, cross-vendor review, novelty clearance, an arbitrary-box theorem, or a negative certificate.
