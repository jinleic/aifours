# A constructive high-gain criterion for five-contact septic families

**Status: WRITTEN sufficient theorem; one exact instantiated family was independently replayed, while a bounded exploratory screen is not a general proof.** This is a method for a structured continuous subfamily, not an arbitrary-box verdict or a novelty claim.

## Boundary geometry

Let an independent monic septic boundary box have parity endpoints
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-t_3)(t-t_4),&
E_+&=-(t-t_1)(t-t_2)(t-t_5),\\
O_-&=-(t-t_1)(t-t_4)(t-t_5),&
O_+&=-(t-t_2)(t-t_3)(t-v),
\end{aligned}
\]
with
\[
0<u<t_1<t_2<t_3<t_4<t_5<v,\quad\lambda>0,
\]
and assume the resulting independent coefficient intervals all have positive lower endpoints and positive widths. The actual corner contacts are at \((2,t_1),(3,t_2),(1,t_3),(0,t_4),(2,t_5)\), using the usual corner order. Every radial subbox \(K_\rho\) centered at the interval midpoint is strictly Hurwitz for \(0\le\rho<1\): the five markers have alternating parity signs and the center has interlacing parity roots; a reference Routh check or Hermite–Biehler establishes its stability. The boundary itself contains imaginary-axis roots.

## Checkable sufficient condition

For an arbitrary coefficient vector \(b\), each contact pairing vanishes automatically. Its derivative at the contact is a linear form in \(b\). Suppose the resulting five tangent equations determine uniquely the coefficients \(b_1,\ldots,b_5\) when \(b_0,b_6,b_7\) are specified. Let \(u,v\) be the two solutions specified by
\[
(u_0,u_6,u_7)=(1,0,1),\qquad
(v_0,v_6,v_7)=(0,1,0).
\]
Assume

1. \(v_j>0\) for \(j=1,\ldots,6\); and
2. for each actual boundary corner \(a_i\), the exact polynomial quotient
\[
Q_i(t)=\frac{P_{a_i,v}(t)}{t\prod_{\tau\in T_i}(t-\tau)^2}
\]
is strictly positive on \([0,\infty)\). Here \(T_i\) is that corner's contact set; polynomial divisibility follows from \(v_0=0\) and the tangent equations.

Then a single monic numerator \(b_x=u+xv\) works for every \(0\le\rho<1\) once \(x>0\) is sufficiently large. This is an all-frequency conclusion for the stated family.

**Proof.** Define the polynomial
\[
R_i(t)=\frac{P_{a_i,u}(t)}{\prod_{\tau\in T_i}(t-\tau)^2}.
\]
It satisfies \(R_i(0)>0\), since all boundary constant coefficients and \(u_0\) are positive, and its leading coefficient is positive, since \(u_7=a_{i,7}=1\). Therefore it is positive near zero and for sufficiently large \(t\). On the remaining compact positive interval, \(tQ_i(t)>0\); one sufficiently large \(x\) makes
\[
R_i(t)+x\,tQ_i(t)>0\quad(t\ge0)
\]
for every corner. Equivalently, one may take \(x\) larger than the finite maximum of \(-R_i(t)/(tQ_i(t))\) over the regions where \(R_i<0\), and also larger than every \(-u_j/v_j\), \(j=1,\ldots,6\). Thus every coefficient of \(b_x\) is positive and every boundary pairing is nonnegative, vanishing only at that corner's contacts.

No positive \(t\) is a contact of all four corners; averaging the four boundary denominators therefore gives a strictly positive center pairing at each finite positive \(t\). It is also strict at zero and at infinity. Every radial-box pairing is an affine combination of the center and a boundary-corner pairing, and the minimum over independent coefficients is attained at the four actual corners. Hence all pairings are strict for \(\rho<1\); the denominators are Hurwitz by the preceding marker argument. This constructs \(b_x\) without assuming the original problem's conclusion.

## Exact instantiated family and bounded evidence

For the separately replayed five-contact family with \((u,t_1,\ldots,t_5,v)=(1/2,1,2,3,6,8,11)\) and \(\lambda=989/855\), all four \(Q_i\) are strictly positive. Exact tangent-preserving coefficient inequalities admit \(x=116\); the resulting explicit numerator and all-frequency boundary/center proofs are in `frontier-20261028-five-contact-all-eligible-scales-v1.md`, SHA-256 `fa380afca2f7ac0529275b1b03d5c84453dd36d4c8940fd6d61d65ec08eda2d6`, with independent receipt SHA-256 `4fbafafd696f5c6e40eb4b60c26b5c074691278bfc377b04a5abae6defe69a2b`.

A separate bounded exact exploratory screen tested the same high-gain residual conditions on 436 rational designs generated from integer root nodes up to 21; it reported 436 positive cases and no inconclusive or negative case. This is **not** a proof that the two hypotheses follow from root order or coefficient-width constraints. The screen producer is `frontier-20261028-five-contact-high-gain-hypothesis-kernel-v1.py`, and no universal theorem is inferred from its census. The sufficient theorem itself uses only its explicitly stated positive-residual hypotheses, elementary continuity, and parity root geometry; its universal quantification is written rather than machine-checked or formally verified.
