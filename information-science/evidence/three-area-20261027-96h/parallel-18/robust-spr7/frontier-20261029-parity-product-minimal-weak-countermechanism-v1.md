# A minimal weak obstruction for a stable independent-parity product

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:05:51 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational certificate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is **not** an original interval-box counterexample: its independent coefficient hull is explicitly unstable.

## 1. Result and relation to the target

A compact convex family of monic strictly Hurwitz septics can have **independently chosen even and odd component families**, globally separated even/odd root bands, and still admit a strict weak odd-cancellation/eight-Vieta-vertex obstruction supported on exactly five positive frequencies plus infinity. This is the minimum six-location frontier of `frontier-20261029-vieta-weak-obstruction-six-support-v1.md` and explicitly realizes the phase word \((2,1,3,2,4)\). Its two-circuit structure is that of `frontier-20261029-minimal-weak-circuit-pair-v1.md`, SHA-256 `9993e2e0bf89bf36a3dfc4efc42b98f466c138e6fd6f952a55c854400d4a1282`.

Thus neither compact convex stability, separated bands, parity-component independence, nor the exact two-circuit phase geometry alone can exclude this minimum weak obstruction. A successful proof for the original problem must use the stronger **coefficient-by-coefficient box structure within the two parity components**, or a different hypothesis that fails here. The example's actual coefficient hull contains an unstable polynomial, so it neither proves nor disproves the original seven-width interval-box question.

## 2. Explicit stable parity-product family

For independent real parameters
\[
1\le\lambda\le3000,\qquad 2\le v\le16/5,\qquad 9/10\le o\le13/10,
\]
put
\[
E_{\lambda,v}(t)=-\lambda(t-1/2)(t-v)(t-5),\qquad
O_o(t)=-(t-o)(t-9/2)(t-7),
\]
and define the monic septic \(a_{\lambda,v,o}\) by
\(a(i\sqrt t)=E_{\lambda,v}(t)+i\sqrt t\,O_o(t)\).
Every member is strictly Hurwitz by the standard Hermite–Biehler interlacing criterion: the roots satisfy
\[
1/2<o<v<9/2<5<7.
\]
The entire even component set and odd component set are chosen independently. The family is also convex: with \(w=\lambda v\), the even polynomials are affine in \((\lambda,w)\), and their parameter set is the convex polygon \(1\le\lambda\le3000\), \(2\lambda\le w\le(16/5)\lambda\); the odd polynomial is affine in \(o\). The product is compact.

The global odd bands are \([9/10,13/10]\), \(\{9/2\}\), \(\{7\}\). Any common monic septic SPR numerator has even part \(F(t)=\prod_{j=1}^3(x_j-t)\), after normalizing its positive \(s^6\) coefficient to one, with
\[
x_1\in(0,9/10),\qquad x_2\in(13/10,9/2),\qquad x_3\in(9/2,7). \tag{1}
\]
Indeed a common numerator is Hurwitz by the same axis-positive homotopy used in `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`; at the actual odd-root bands the even pairing forces signs \(-,+,-\), while at zero it is positive. The three strict sign changes force the listed simple roots. Multi-affinity in \((x_1,x_2,x_3)\) represents \(F\) coefficientwise as a convex combination of the eight vertex cubics formed by the closed endpoints in (1).

## 3. Five actual members and an exact weak certificate

Use the five actual members with \((\lambda,v,o)\) and squared frequencies
\[
\begin{array}{c|ccc|c}
i&\lambda_i&v_i&o_i&t_i\\\hline
1&1&16/5&9/10&1\\
2&1&16/5&13/10&121/100\\
3&3000&2&9/10&9/4\\
4&3000&16/5&9/10&49/16\\
5&1&2&9/10&121/25.
\end{array} \tag{2}
\]
Their \((E_i(t_i),O_i(t_i))\) sign classes are \((2,1,3,2,4)\) under the convention in the imported minimum-support theorem. The even-root reversal is at nodes 3–4 and the odd-root reversal at nodes 1–2.

For the finite, **uncompactified** pairings use the strictly positive rational weights
\[
\begin{aligned}
(w_1,\ldots,w_5)=(&19375/14553,\ 212500000000000/130197894099273,\ 1280000/139908951,\\
&838860800000/71185421760453,\ 7769775390625/731375270700921).
\end{aligned} \tag{3}
\]
The atom at compactified infinity has weight **4**. Exact arithmetic gives the four odd identities
\[
\sum_{i=1}^5w_i\,t_iO_i(t_i)(-t_i)^r+4\mathbf1_{r=3}=0,\quad r=0,1,2,3. \tag{4}
\]
These weights are also generated without solving anything: for \(X=\{1,2,3,5\}\), \(Y=\{1,2,4,5\}\), and \(H_X=\prod_{i\in X}(t-t_i)\), \(H_Y=\prod_{i\in Y}(t-t_i)\), take
\[
w_i=\frac{\mathbf1_{i\in X}}{t_iO_i(t_i)H_X'(t_i)}+
\frac{3\mathbf1_{i\in Y}}{t_iO_i(t_i)H_Y'(t_i)}.
\]
The first and second terms are the two positive odd circuits, with infinity masses 1 and 3. Thus the repeated finite nodes 3–4 are the only differing finite support points. To write this in the predecessor's compactified form, give finite atom \(i\) weight \(w_i(1+t_i)^7\), give infinity weight 4, and divide all six weights by their positive total.

For verification, direct exact substitution gives
\[
\begin{aligned}
(E_i(t_i))&=(-22/5,-5354891/1000000,28875/8,-1048575/512,30814/15625),\\
(O_i(t_i))&=(-21/10,1714419/1000000,-4617/320,-250677/20480,90423/31250).
\end{aligned} \tag{5}
\]
Order the eight vertices lexicographically by \(x_1\in(0,9/10)\), \(x_2\in(13/10,9/2)\), \(x_3\in(9/2,7)\), choosing each listed endpoint. With
\(D=638987565352683834577824534>0\), the eight exact even sums are
\[
\sum_iw_iE_i(t_i)\prod_j(x_j-t_i)=D^{-1}(N_1,\ldots,N_8),\tag{6}
\]
where
\[
\begin{aligned}
(N_1,\ldots,N_8)=(&-12323336377952387826014540025,\ -102764438991337963638224643525,\\
&-23764920059851235569791573625,\ -32703657311334710369617381125,\\
&-22761911636408616783862260990,\ -100914002204037204632434633215,\\
&-51977353405500518139726507550,\ -74801917287603566073995450175).
\end{aligned}
\]
Every entry is strictly negative. Equations (2)–(6) were computed exactly using Python `fractions.Fraction` and integer arithmetic in one Eval kernel; no floating point was used in this certificate.

## 4. Contradiction and the exact box barrier

Suppose a common exact-degree numerator \(b\) exists. Its leading coefficient \(b_7\) is strictly positive by the finite-frequency positivity and degree-seven limit, and its even part is as in (1). Each of its five finite pairings and the compactified infinity pairing \(b_7\) is strictly positive. Weighting these pairings by (3) and 4 therefore gives a strictly positive total. By the four identities (4), all odd coefficients cancel. By (6) and the convex-combination representation of the even part, the same total is strictly negative. Contradiction. Thus the displayed independent-parity product has no common numerator.

This is not an eligible independent coefficient box. Take member 4 and replace only its \(s^6\) coefficient \(3000\) by \(1\), leaving all other coefficients unchanged. The resulting monic polynomial lies in the componentwise coefficient hull of the family: the value 1 is attained by member 1. Its second Hurwitz determinant is
\[
a_6a_5-a_4=1\cdot(62/5)-26100=-130438/5<0,
\]
since member 4 has \(a_5=62/5\) and \(a_4=3000(1/2+16/5+5)=26100\). Hence that hull is not all-Hurwitz, and any independent coefficient box containing the family is ineligible. The countermechanism cannot be used as an original-box no-go.

## 5. Remaining gap and assurance

The arithmetic in (3)–(6) and the displayed determinant were checked using exact integers/`fractions.Fraction` on one Python Eval host; interlacing, parity-product convexity, Vieta interpolation and the homotopy contradiction are written deductions and named classical imports. This is author work, not a separate replay or formal/kernel proof. Parent-classified incidental source-display exposure is disclosed in `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made. The original universal interval-box synthesis-or-obstruction verdict remains **OPEN**.
