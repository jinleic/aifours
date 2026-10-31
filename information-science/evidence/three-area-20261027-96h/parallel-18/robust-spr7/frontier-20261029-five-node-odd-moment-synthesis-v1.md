# Eliminating the odd numerator: exact five-node inequalities for septic synthesis

Owner InfoSPR7-2, info-2. Native clock observed before writing: **Thu Oct 29 15:46:44 PDT 2026**. **WRITTEN universal coupling theorem candidate**, not parent-adopted, independently reviewed, formally verified or novelty-cleared. It treats all actual box members and all numerator coefficients; no fixed numerator profile or earlier unreviewed theorem is assumed. The original all-box existence-or-obstruction verdict remains open.

## 1. Exact original-target reduction

Let \(K\) be any nonempty bounded closed independent monic real septic coefficient box, with degenerate intervals allowed, whose members are all strictly Hurwitz. Let \([\underline o_j,\overline o_j]\) be the range of the \(j\)-th positive root of actual odd parity parts; the three compact bands are strictly ordered and separated. For \(e=(e_0,e_2,e_4)\), put
\[
F_e(t)=e_0-e_2t+e_4t^2-t^3.
\]
Define the open root-gap polyhedron \(\mathcal P_K\subset\mathbb R^3\) by
\[
e_0>0,\quad F_e(\underline o_1)<0,\quad F_e(\overline o_1)<0,\quad
F_e(\underline o_2)>0,\quad F_e(\overline o_2)>0,\quad F_e(\underline o_3)<0. \tag{1}
\]
These are six linear strict inequalities in \(e\).

The box has one original exact-degree-seven common SPR numerator **if and only if** there exists \(e\in\mathcal P_K\) satisfying **every** inequality of the following two forms. All denominators \(a_i\) are independently chosen actual members of \(K\), and \(E_i=E_{a_i}(t_i)\), \(O_i=O_{a_i}(t_i)\).

**Five finite nodes.** For any \(0<t_1<\cdots<t_5\) whose five nonzero \(O_i\) signs alternate, let
\(H_5(t)=\prod_{i=1}^5(t-t_i)\). Require
\[
\sum_{i=1}^5
\frac{E_i F_e(t_i)}{t_i|O_i|\,|H_5'(t_i)|}>0. \tag{2}
\]

**Four finite nodes plus infinity.** For any \(0<t_1<\cdots<t_4\) with nonzero odd signs \((- ,+,-,+)\), let \(H_4(t)=\prod_{i=1}^4(t-t_i)\). Require
\[
\sum_{i=1}^4
\frac{E_i F_e(t_i)}{t_i|O_i|\,|H_4'(t_i)|}>0. \tag{3}
\]
Each condition is an affine strict inequality in the **same three** variables \(e\). Every nontrivial node configuration in (2) or (3) has a backward crossing within an actual global odd-root band, proved in §5. Thus this result eliminates the four unknown odd-numerator coefficients and arbitrary-size dual measures without assuming any selected profile. It does **not** show that the resulting three-dimensional convex intersection is nonempty.

## 2. The root-gap polyhedron is necessary

Write \(a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t)\). By Hermite–Biehler, each \(E_a\) and \(O_a\) has three simple positive roots in alternating order. Because the parity coefficient boxes are independent, their root extrema can be combined into actual members; compactness then gives strict global separation between successive even and odd root bands.

If a common numerator \(b\) exists, \(b_7>0\), since \(b/a\to b_7\) at infinity and the numerator has exact degree seven. For any fixed \(a\in K\), the path \((1-\theta)a+\theta b\) is imaginary-axis-zero-free and keeps positive leading coefficient; root continuity implies \(b\) is Hurwitz. In particular \(b_6>0\), so normalize \(b_6=1\) and write \(E_b=F_e\).

At an actual root of the \(j\)-th odd component, \(P_{a,b}=E_aF_e>0\). For every actual even component the sign of \(E_a\) there is \((-1)^j\), because of the global band order. The \(j\)-th odd root varies continuously over a connected coefficient box and therefore fills its entire closed band. Thus \(F_e\) has signs \(-,+,-\) on the three odd bands and \(F_e(0)>0\), yielding (1). Conversely, (1) is precisely the condition that the three roots of \(F_e\) lie in the three gaps before and between these odd bands: the sign changes force three roots in disjoint intervals, and cubic degree excludes extras.

## 3. Eliminating the odd coefficients exactly

For an actual member and \(t=\omega^2\), define the normalized pairing
\[
\frac{P_{a,b}(t)}{(1+t)^7}=g_e(a,t)+z\cdot v(a,t),\qquad
z=(b_1,b_3,b_5,b_7),
\]
where
\[
g_e(a,t)=\frac{E_a(t)F_e(t)}{(1+t)^7},\qquad
v_r(a,t)=\frac{tO_a(t)(-t)^r}{(1+t)^7},\quad0\le r\le3. \tag{4}
\]
On compactifying \(t\in[0,\infty]\), \(g_e(a,\infty)=0\) and \(v(a,\infty)=(0,0,0,1)\); at zero, \(g_e(a,0)=a_0e_0\) and \(v(a,0)=0\). At each finite \(t\), both components are affine in \(a\), so four actual parity corners suffice for minimizing the pairing. Let \(S\) be their compact union of normalized rows, and set
\[
M_e=\min\left\{\int g_e\,d\mu:\ \mu\text{ a probability measure on }S,\quad \int v\,d\mu=0\right\}. \tag{5}
\]
The feasible measure set is nonempty (a zero-frequency row has \(v=0\)), compact, and the minimum exists.

There is a real \(z\) and \(\delta>0\) with \(g_e+z\cdot v\ge\delta\) on all of \(S\) **if and only if** \(M_e>0\). The forward direction follows by integration. For the reverse direction, the compact convex hull of the points \((v,g_e)\in\mathbb R^5\) is disjoint from the closed ray \(\{(0,s):s\le0\}\). Strict separation yields \((h,\lambda)\) with \(h\cdot v+\lambda g_e>0\) on the hull and \(\lambda\ge0\). If \(\lambda=0\), adding a sufficiently small positive coefficient of \(g_e\) preserves strictness because the hull is compact. Divide by \(\lambda>0\). The infinity row forces \(z_3=b_7>0\), so the resulting polynomial has exact degree seven. The four-corner reduction then gives the original strict finite-frequency condition for every member.

A minimizing measure in (5) can be taken to have **at most five atoms**. First, ordinary Carathéodory represents the minimizing point \((0,M_e)\) by at most six rows in \(\mathbb R^5\). If six have positive weights, their six vectors \((1,v_i)\in\mathbb R^5\) are linearly dependent. Perturb the six weights in either direction along a nonzero dependence. Both directions remain feasible for small perturbations, so minimality forces the derivative of the \(g_e\)-objective to vanish. Continue until one weight is zero. This retains \(\int v=0\), total mass one, and the minimum. Repeating yields at most five atoms.

## 4. Classification of the at-most-five-atom minimizer

Take \(e\in\mathcal P_K\). Any row with \(v=0\) has positive \(g_e\): at zero this is \(a_0e_0>0\); at \(t>0\), \(v=0\) means \(O_a(t)=0\), and (1) gives the same strict sign for \(F_e(t)\) as every \(E_a(t)\). If a nonpositive-cost odd-canceling measure contained such a row, remove it and renormalize the remaining positive mass; the remaining measure has the same odd cancellation and nonpositive cost. Thus a failure \(M_e\le0\) has a minimizing witness with no zero-\(v\) row.

Merge atoms at the same positive finite frequency by weighted averaging of their denominators. The average is an actual member of the convex box, and (4) is affine in the denominator. If merging makes \(O_i=0\), it is a zero-\(v\) row and may be discarded as above. Hence assume all remaining finite nodes are distinct and \(t_iO_i\ne0\). The infinity row, if used, has \(v=(0,0,0,1)\), \(g_e=0\).

Without infinity, fewer than five finite nodes cannot cancel the four odd moments: the corresponding Vandermonde columns \((1,-t_i,t_i^2,-t_i^3)^T\) are independent. For exactly five nodes, put \(H_5(t)=\prod_{i=1}^5(t-t_i)\). The one-dimensional Vandermonde kernel is
\[
\bigl(1/H_5'(t_1),\ldots,1/H_5'(t_5)\bigr),
\]
whose signs alternate \((+,-,+,-,+)\). Positive atom weights are therefore possible exactly when the \(O_i\) signs alternate, starting with either sign. Apart from a common positive factor, the positive weights are
\[
\mu_i=\frac{(1+t_i)^7}{t_i|O_i|\,|H_5'(t_i)|}.
\]
Their \(g_e\)-sum has the sign of (2).

With a positive infinity atom, fewer than four finite nodes cannot cancel the first three odd moments. Exactly four finite nodes have kernel \(1/H_4'(t_i)\) for those first three moments. The fourth finite moment equals minus its common multiplier, so a nonnegative infinity weight forces that multiplier to be positive. Thus the \(O_i\) signs are exactly \((- ,+,-,+)\), the positive finite weights are proportional to the same absolute-value formula, the infinity atom has zero \(g_e\)-cost, and the cost sign is (3).

Therefore every possible nonpositive minimum is detected by (2) or (3). Conversely every node configuration there supplies a positive odd-canceling measure with cost equal, up to a positive normalization, to the displayed left side. Compactness is essential: if all these inequalities and the zero-row signs are strict, the minimizing witness cannot have cost zero, so \(M_e>0\) and an odd polynomial \(z\) exists. This completes the if-and-only-if statement.

## 5. Why only reversed odd bands can appear

For each finite node, let \(k_i\in\{0,1,2,3\}\) count the odd roots of its actual member below \(t_i\); its odd sign is \((-1)^{k_i}\). In a five-node circuit the signs alternate four times. If the \(k_i\) never decreased, the four changes would require at least four increments, impossible because \(k_i\le3\). In a four-plus-infinity circuit, the signs are \((- ,+,-,+)\); the first count is at least one, so three nondecreasing sign changes again force a count at least four. Thus a decrease occurs in either case.

If the earlier member has already passed its \(j\)-th odd root but the later member has not, both increasing node frequencies, and their whole intervening interval, lie in the global \(j\)-th odd-root band. Therefore every nontrivial circuit in (2) or (3) requires a backward crossing in some odd band. This is a restriction on all candidate projection obstructions, not a claim that every such crossing is realizable or yields a counterexample.

## 6. Assurance and remaining original problem

Named standard imports: odd-degree Hermite–Biehler; compactness and strict finite-dimensional convex separation; ordinary Carathéodory; Vandermonde interpolation and root continuity. The coefficient projection, support reduction, exact denominators in (2)–(3), endpoint accounting, and reversed-band deductions are written explicitly above. No numerical sampling, solver, previous unreviewed result, historical held body or external model is a premise. Parent-classified incidental source-display exposure remains recorded in `owner-incidental-held-source-search-display-v1.json`; no clean-cognition claim is made.

The **exact remaining universal question** is whether every eligible \(K\) admits one \(e\in\mathcal P_K\) satisfying all the explicit five-node and four-plus-infinity affine inequalities simultaneously, or whether some eligible box has no such \(e\). The theorem resolves neither alternative. It is not a formal proof, independent review, novelty clearance or an original-box verdict.
