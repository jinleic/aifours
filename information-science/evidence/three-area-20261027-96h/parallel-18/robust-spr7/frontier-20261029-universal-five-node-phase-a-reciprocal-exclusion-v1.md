# Phase A is excluded by a nonmonic reciprocal form of phase C

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:54:46 PDT 2026**. **WRITTEN theorem candidate**, importing same-host WRITTEN-checked-in-kernel integer evidence for phase C. Not parent-adopted, independently reviewed, formally verified or novelty-cleared.

## 1. Result

For every compact independent coefficient box of monic Hurwitz septics, no positive-weight direct all-eight-coordinate strictly negative aggregate with five distinct positive squared frequencies can have phase word **A = (2,1,3,2,4)**, even with additional zero and infinity atoms. Together with `frontier-20261029-universal-five-node-phase-c-exclusion-v1.md`, SHA-256 `8c0a03012e79fbdf4d713635bb03d448712e46510ea99bdfc722b01c449ef505`, this excludes two of the three direct five-node phase words in the named phase classification. **Phase B remains open** in its mixed-second-odd-band residual, and the original arbitrary-box common-numerator-or-counterexample problem remains open.

This transfer must not assume reciprocal denominators remain monic. We first extend the phase-C argument to an independent coefficient box with **variable positive leading coefficient**, and only then reverse coefficients.

## 2. Phase C with a positive leading interval

Let a compact independent septic coefficient box have all members Hurwitz and positive leading coefficient \(a_7\in[\underline a_7,\overline a_7]\), not necessarily fixed. Its pointwise odd envelopes have the form
\[
O_-(t)=\lambda_-(a-t)(d-t)(e-t),\quad
O_+(t)=\lambda_+(b-t)(c-t)(f-t),\quad
\lambda_-\ge\lambda_+>0. \tag{1}
\]
The scales are respectively the upper and lower leading endpoints. Independent intervals imply \(\Delta(t)=O_+(t)-O_-(t)\) has nonnegative coefficients in \(1,t,t^2,t^3\), hence is nondecreasing for \(t>0\). The usual real-part interlacing and the envelope ordering give the same root-band arrangement and phase-C placements. The direct eight-ray interpolation argument is unchanged: the ray weights use the actual \(O_i\), without requiring monic leading coefficient.

For the first-odd-band and boundary proof in the named phase-C packet, the formal \(O_-\) baseline and its pole term are multiplied by \(1/\lambda_-\). The node-2 correction for \(x=a\), \(y\in\{b,c\}\), is now
\[
D_y=\frac{B-y}{B-c}\frac{\Delta(B)}{\lambda_-\lambda_+(f-B)}. \tag{2}
\]
Because \(\Delta(A)>O_+(A)=\lambda_+(b-A)(c-A)(f-A)\) when \(a<A<b\), monotonicity gives
\[
D_y>\frac{(b-A)(y-A)}{\lambda_-}. \tag{3}
\]
This is exactly the bound required by the original tail proof after its baseline is scaled by \(1/\lambda_-\); the \(x=0\) pole and comparison scale the same way. At \(A=b\), the baseline first term is zero while the correction is positive. Thus the whole first-band/boundary part survives variable leading coefficients.

For the first-gap part, the three easy Vieta-vertex cases also survive: the all-positive case is immediate; the \((b,d)\) proof uses an \(O_-\) baseline and a positive opposite-sign correction; the \((c,e)\) proof uses an \(O_+\) baseline and a positive opposite-sign correction. Their baseline multipliers become \(1/\lambda_-\) or \(1/\lambda_+\).

The only additional check is the hard \((y,z)=(c,d)\) vertex in the first-gap theorem. Write its unit-leading-endpoint pairing as \(S_0=S_++S_-\), where \(S_+\) is the sum of the first two \(O_+\) node contributions and \(S_-\) the last two \(O_-\) contributions. The eight positive-polynomial certificates imported by the named gap theorem give \(S_0>0\). In fact \(S_+>0\) separately. For a four-node ray, write \(w_i=e_m(\widehat u_i)\), \(m=0,1,2,3\), and for the first-root vertex \(x\in\{0,a\}\) define
\[
h(t)=\frac{d-t}{u_3-t}\frac{e-t}{u_4-t}\frac1{f-t}. \tag{4}
\]
Each positive factor in (4) increases on \([u_1,u_2]\), because \(u_2<u_3<d\), \(u_4<e<f\). The two \(O_+\) terms are
\[
S_+=\frac{w_2(u_2-x)h(u_2)-w_1(u_1-x)h(u_1)}{u_2-u_1}. \tag{5}
\]
Let \(A=e_{m-1}(u_3,u_4)\), \(B=e_m(u_3,u_4)\), with \(e_{-1}=0\). Then
\[
w_2(u_2-x)-w_1(u_1-x)=(u_2-u_1)(xA+B)\ge0, \tag{6}
\]
and the strict increase of \(h\) makes (5) strictly positive, including \(x=0,m=3\). Hence, for the actual scales,
\[
S=\frac{S_0}{\lambda_-}+
\left(\frac1{\lambda_+}-\frac1{\lambda_-}\right)S_+>0. \tag{7}
\]
Thus the phase-C exclusion extends to every independent all-Hurwitz septic box with positive variable leading coefficient. This is a written extension; the previously frozen eight unit-scale hard-vertex polynomials are not being presented as a new independent computation.

## 3. Coefficient reversal preserves the actual box

For an original monic denominator \(a(s)=\sum_{j=0}^7a_js^j\) and any test numerator \(b\), define
\[
a^*(s)=s^7a(1/s),\quad b^*(s)=s^7b(1/s). \tag{8}
\]
Do **not** divide \(a^*\) by its varying leading coefficient. Its coefficients are the original independent intervals in reverse order; its constant coefficient is 1 and its leading coefficient ranges over the original positive \(a_0\) interval. Reciprocating each root preserves the open left half-plane.

If \(P_{a,b}(t)=E_a(t)E_b(t)+tO_a(t)O_b(t)\), then for every \(t>0\)
\[
P_{a^*,b^*}(1/t)=t^{-7}P_{a,b}(t),\qquad
\frac{P_{a^*,b^*}(1/t)}{(1+1/t)^7}
=\frac{P_{a,b}(t)}{(1+t)^7}. \tag{9}
\]
Thus compactified finite atom weights remain positive and unchanged; zero and infinity swap. Reversing \(b\)'s coefficient order reverses the eight aggregate coordinates, so strict negativity of all eight survives. The parity signs transform as \((E,O)\mapsto(-O,-E)\), in reversed frequency order. In particular
\[
(--),(-+),(+-),(--),(++)
\longmapsto
(--),(++),(+-),(-+),(++), \tag{10}
\]
which is exactly phase A to phase C. The variable-leading phase-C theorem therefore contradicts any phase-A certificate.

## 4. Nonvacuity and assurance

`frontier-20261029-phase-a-reciprocal-example-frozen-v1.json`, SHA-256 `af44672dcbe49ecf969ac2c336fa61854a860d67d278e7f4a4410c906393c257`, contains an actual full-width monic septic box, five actual members with the phase-A signs in (10), and five exact checks of (9). Its 128 endpoint polynomials have all 896 leading Hurwitz minors positive in exact integer arithmetic; the classical Kharitonov theorem is explicitly imported to infer whole-box stability. The integer-scaled minor minima are not common unscaled stability margins.

The reciprocal identity, endpoint-scale extension, ray argument and phase mapping are written mathematics. The example's finite determinant and rational checks were performed on one Python Eval host; the inherited hard-vertex polynomial expansion is also same-host. No independent review, formal proof, parent adoption or novelty clearance occurred. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
