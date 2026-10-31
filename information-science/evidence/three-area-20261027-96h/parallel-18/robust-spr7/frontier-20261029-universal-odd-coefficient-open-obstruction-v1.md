# A necessary coefficient inequality for every common numerator

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact independent replay; not parent adoption.** For an explicit original-eligible, all-seven-width septic box, **every** common numerator must obey a simple strict halfspace inequality in two odd coefficients. This excludes every numerator whose odd coefficients stay inside the denominator box, even when its even coefficients are completely unrestricted. The box nevertheless has a separately checked unrestricted common numerator. The same conclusion holds throughout an explicit 14-dimensional open neighborhood.

## The actual box and unconditional necessary inequality

Use the stable box \(K\) of `frontier-20261029-seven-dimensional-span-obstruction-open-v1.md` (SHA-256 `5693a3a172c2d696471718084a755d4ce984cc3edf2fc1946b6e38ee1f9f561f`). Its boundary parity cubics are
\[
\begin{aligned}
E_-&=-\frac{1001}{1000}(t-1/20)(t-100)(t-101),&
E_+&=-(t-1)(t-3/2)(t-2000),\\
O_-&=-(t-1)(t-101)(t-2000),&
O_+&=-(t-3/2)(t-100)(t-2001),
\end{aligned}
\]
and its seven independent intervals are their midpoint-centered radial subbox at \(\rho=1-10^{-8}\). The actual endpoints are frozen in the cited record. In particular
\[
\overline a_3=\frac{81640399998301}{400000000},\quad
\underline a_5=\frac{840800000001}{400000000},\quad
\overline a_3-97\underline a_5=\frac{20699999551}{100000000}.
\]
The independent checker here replays all 28 positive corner Hurwitz determinants; Kharitonov's theorem implies all members Hurwitz. It also independently checks the source's exact unrestricted common numerator with four monomial Sturm chains, each having no positive root. Thus this is a real full-width stable box **with a solution**, not a putative counterexample.

**Theorem.** For every real degree-seven \(b(s)=\sum_{j=0}^7b_js^j\), if \(b/a\) is strictly positive real for every \(a\in K\), then \(b_7>0\) and
\[
\boxed{\quad b_3-97b_5>\frac{20699999551}{100000000}\,b_7.\quad}
\]
In monic normalization this implies \(b_3>\overline a_3\) **or** \(b_5<\underline a_5\), hence no common monic numerator can have both of these odd coefficients in their original denominator intervals. This holds with **no restriction whatsoever** on \(b_0,b_1,b_2,b_4,b_6\).

Consequently, choosing any actual denominator and rescaling its even and odd parts by arbitrary positive factors cannot solve this box: after monic normalization its odd part, including \(b_3,b_5\), is still that actual denominator's odd part. This is a substantially larger obstruction than excluding a fixed endpoint/derivative span. It does not exclude unrestricted numerator polynomials; indeed the independently replayed source numerator satisfies the inequality and works.

## Exact eight-atom proof

Number the actual parity corners \(0,1,2,3\) by \((--),(-+),(+-),(++)\). Use the eight actual corner/squared-frequency pairs
\[
\begin{array}{c|cccccccc}
\text{corner}&2&3&3&1&0&2&0&0\\
t&999/1000&2997/2000&3003/2000&1001/10&100899/1000&1998&1/3&4093/3.
\end{array}
\]
Their eight explicit positive integer weights are in `frontier-20261029-universal-simple-odd-halfspace-frozen-v1.json`. Direct signed monomial accumulation, without invoking any numerator basis, gives the exact aggregate coefficient vector
\[
C=c\left(0,0,0,1,0,-97,0,-\frac{20699999551}{100000000}\right),\qquad c>0.
\]
A common numerator makes every actual pairing positive, so \(C\cdot b>0\), which is exactly the displayed inequality. Since \(\overline a_3-97\underline a_5\) is the maximum of \(a_3-97a_5\) over the actual independent intervals, no monic \(b\) with those two coefficients in range can satisfy it.

## Explicit open persistence

Independently perturb each of the 14 endpoints by less than \(\epsilon=10^{-2000}\), retain monicity, and recompute the **perturbed** actual corners. Let \(r_i\) be the monomial pairing row at the same eight fixed frequencies, and form a \(7\times8\) matrix whose rows are
\[
(r_{i0})_i,(r_{i1})_i,(r_{i2})_i,(r_{i4})_i,(r_{i6})_i,
(r_{i5}+97r_{i3})_i,
(r_{i7}+(\overline a'_3-97\underline a'_5)r_{i3})_i.
\]
At the anchor its eight signed \(7\times7\) cofactors are strictly positive after a common orientation and proportional to the displayed atom weights; the checker also verifies that the corresponding weighted \(b_3\) coefficient is strictly positive. These cofactors give a nullvector, so the new atom sum has precisely the desired halfspace form, with the new box's own endpoints.

For the quantitative stability of these signs, a common denominator for the anchor matrix and its augmented \(8\times8\) matrix is
\(D=27993600000000000000000000000000000<10^{35}\). Thus every nonzero anchor \(7\times7\) cofactor has absolute value at least \(D^{-7}\), and the nonzero augmented determinant has absolute value at least \(D^{-8}\). For all such endpoint perturbations, each entry of either matrix has magnitude below \(10^{40}\) and changes by less than \(10^{38}\epsilon\): actual coefficients are below \(10^{10}+1\), all \(t<2000\), and the endpoint threshold changes by at most \(98\epsilon\). The Leibniz/telescoping determinant bounds
\[
7!\,7\,10^{40\cdot6+38}\epsilon<\tfrac12D^{-7},\qquad
8!\,8\,10^{40\cdot7+38}\epsilon<\tfrac12D^{-8}
\]
are independently checked exactly. All eight cofactor signs and the positive \(b_3\) scale therefore persist. Widths remain positive. The prior independently replayed open box result already covers radius \(10^{-370}\), including preservation of the same unrestricted numerator and all-member Hurwitz stability; this smaller neighborhood is contained in it. Hence every nearby box has both an unrestricted solution and the stated necessary halfspace, while its entire original odd-coefficient projection remains forbidden.

## Evidence and scope

Anchor inputs and positive weights: `frontier-20261029-universal-simple-odd-halfspace-frozen-v1.json`, SHA-256 `3891b2e8ee1e2405573dc0aaf9f1194a8909948988e3e24e2e20a14790a5e8bf`. Independent direct monomial/Hurwitz/Sturm replay: `frontier-20261029-universal-simple-odd-halfspace-independent-kernel-v1.py`, SHA-256 `d7209489226c03614e6ce03d544bc0399d0aab04a4379079d1b04a3415f1680c`; receipt `frontier-20261029-universal-simple-odd-halfspace-independent-result-v1.json`, SHA-256 `53f27f8fa292d74c30538bd41231ebe4d03ea89b125f5d00b58e704eed723052`. Open data `frontier-20261029-universal-odd-halfspace-open-frozen-v1.json`, SHA-256 `4ad166dcebd90a1ed2ad5fbf16e0a54d83448dd56255f970abf768fdeb58c672`; open cofactor/perturbation replay `frontier-20261029-universal-odd-halfspace-open-independent-kernel-v1.py`, SHA-256 `07505b78f1e16015646b1e09252ebcf32ae094578170289542acf2092bd0aaf4`; receipt `frontier-20261029-universal-odd-halfspace-open-independent-result-v1.json`, SHA-256 `e7e692fe7321f2f8e9163db8bd157543e249f6042db6193bcd13a89db5b429ea`.

The separate replays use exact integer/`fractions.Fraction` arithmetic on one Python Eval host. Kharitonov, the determinant perturbation estimate and homotopy are written mathematics. No formal proof, cross-vendor review, novelty clearance, strict-negative-coordinate certificate, or universal arbitrary-box verdict is asserted.
