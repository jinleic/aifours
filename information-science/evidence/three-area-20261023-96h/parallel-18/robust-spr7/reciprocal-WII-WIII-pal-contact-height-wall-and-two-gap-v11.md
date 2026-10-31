# SPR7 reciprocal W_II/W_III — diagonal palindromic-contact inverse, exact height wall, and a two-gap determinant representation

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 04:57:36 PDT 2026**. Owner InfoSPR7/info-2. **NEW COMPLETE WRITTEN THEOREM/REPRESENTATION CANDIDATE**, requiring its own fresh full-source/application gate. This is a NEW all-parameter representation, not another tiny-r W_I restriction, not a point, emptiness proof or original SPR7 verdict.

The v112-J review ACTUALLY RETURNED before the separate prospective primary ACK at04:46:05 (`primary-return-from-v112-J-exposure-ack-v1.json`, SHA256 `dc6682addec72cdf86412b2c901d23e40dfb4d9005f380c5fdef5218eb424e3d`), sent to Main BEFORE new primary source/math. No semigroup theorem is an SPR premise. The independently frozen v113 A/B gates are not read or inherited. All older sources remain immutable.

All derivations below use SYMBOLIC VARIABLES ONLY. No numerical parameter instance, approximate magnitude gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner written-exactness findings, v18's symbolic-only breach and every parent/author/reviewer finding remain permanent; withdrawn probes get ZERO credit. Written work is not formal/kernel/human/configured-family/executable/novelty acceptance.

## 0. Named inputs and exact delivered scope

Named reciprocal inputs, pinned by live metadata before this write:

- v5: `reciprocal-critical-cone-entire-inverse-and-positive-kernel-v5.md`, SHA256 `7a358b729dfff820eb18d8af9bd474e83592979f4a045ea212a09237bda7f70a`: actual reciprocal input decomposition, positive-kernel and first-critical interfaces.
- v9: `reciprocal-weak-quadratic-strict-transfer-entire-v9.md`, SHA256 `34d12a551f4255f9c647d1c643af3baae5fff805417896124b511e87723cc435`: needed ONLY for the converse passage from an arbitrary negative reciprocal input to a strict-cubic critical configuration.
- v10: `reciprocal-class-exact-three-word-reduction-v10.md`, SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`, with its mandatory erratum-1 SHA256 `cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`: exact four corners, determination/three-word/admission calculus. The erratum's d0<x1 condition is NOT called automatic.

The frozen even-Euler certificate and whole-even-profile obstruction remain the original qualified ancestry; their fixed-profile failures are NOT premises of an unrestricted negative conclusion here. Existing unrestricted numerators for the delivered literal profile/hybrid-obstruction boxes are not contradicted or promoted.

**New here.** For EVERY W_II/W_III strict-cubic configuration, with no smallness restriction:

1. The three target phase boundaries are roots of one explicit cubic A(v), with exact isolating intervals tied to f/d and e.
2. The two palindromic contact cubics directly recover all six original center/width coordinates. Width positivity becomes three strict linear inequalities in two contact heights.
3. A palindromic contact has an exact rational amplitude. It gives the precise C1 lead/lag height wall, and nonzero amplitude is equivalent to strict Hurwitz stability of that entire palindromic corner.
4. The two nonpalindromic corner inequalities are equivalent to ONE septic determinant inequality on ONLY TWO open gaps. The other target-component boundaries have AUTOMATIC strict margins. Whole-box admission still checks nonzero amplitudes at EVERY determinant zero, not only selected contacts.
5. These formulas yield an exact alternative representation of W_II/W_III. Neither set is decided. For fixed target and pal-contact locations, weak corner positivity is an intersection of explicit affine half-planes in the two heights.

## 1. Strict target and an explicit phase cubic

Retain the original reciprocal INPUT class: monic septic, A7=1, and the coefficients A_i,A_(7-i) vary INDEPENDENTLY in the SAME intervals [m_i-w_i,m_i+w_i], i=1,2,3. Widths w_i>0. This is a specified input subclass, not a universal restriction on the original problem.

Write the palindromic target

`B(s)=(s+1)s^3 T(s+1/s)`, `T(z)=z^3+d z^2+e z+f`,

where d,e,f>0 and D:=de-f>0. Thus T and B are strictly Hurwitz. Put t=omega^2, 0<t<1, u=omega-1/omega<0 and

`v=u^2=(1-t)^2/t`, `xi=(1-t)/(1+t)=sqrt(v/(v+4))`.

Then X=Re T(iu)=f-dv and W=Im T(iu)/u=e-v. Define

`A(v)=X^2-vXW-vW^2`

`=f^2-(2fd+fe+e^2)v+(d^2+f+de+2e)v^2-(d+1)v^3`. (A)

It has EXACTLY three distinct simple positive roots rho1<rho2<rho3, with

`0<rho1<f/d<rho2<e<rho3`.

**Proof.** A(0)=f^2>0. At v=f/d, X=0 and W=e-f/d=D/d>0, so A(f/d)=-(f/d)W^2<0. At v=e, W=0 and A(e)=(f-de)^2=D^2>0. Its leading coefficient is -(d+1)<0. There is a root in each of the three disjoint intervals; a cubic has only three roots counted with multiplicity, proving the assertion.

Direct evaluation of B(iomega) gives

`E_B=omega^3(omega X+uW)`, `O_B=omega^2(omega uW-X)`,

hence

`E_B(t) O_B(t)=-t^3 A(v)`. (EO)

The map v↦t is strictly decreasing and bijective from (0,infinity) to (0,1), with

`t(v)=(v+2-sqrt(v(v+4)))/2`.

Thus the target's four below-one cells, with their unique minimizing corners, are:

| v interval | t cell | corner |
|---|---|---|
| (0,rho1) | C3 cell (x2,1) | C3=(Eminus,Oplus) |
| (rho1,rho2) | C2 cell (y1,x2) | C2=(Eplus,Oplus) |
| (rho2,rho3) | C1 cell (x1,y1) | C1=(Eplus,Ominus) |
| (rho3,infinity) | C4 cell (0,x1) | C4=(Eminus,Ominus) |

This agrees with v10's cells but now supplies a polynomial isolator independent of the original input bands. A(v)<0 ONLY on the C2 and C4 intervals.

## 2. Diagonal palindromic-contact inverse and the exact amplitude wall

For a>0 and l>0, let the palindromic corner's real cubic pairing be

`phi_(a,l)(v)=(v-a)^2(v+l)`.

There is a UNIQUE monic cubic U(z)=z^3+A_U z^2+B_U z+C_U with

`Re[T(iu) conjugate U(iu)]=phi_(a,l)(v)`.

The exact inverse is

`C_U=a^2 l/f`,

`A_U=((a-e)^2+l(e-2a+d a^2/f))/D`,

`B_U=d A_U-e-l+2a`. (INV)

**Proof.** For general U the pairing coefficients are

`v^3+(d A_U-e-B_U)v^2+(-d C_U-f A_U+e B_U)v+f C_U`.

Equate these to v^3+(l-2a)v^2+(a^2-2al)v+a^2l. Solve the constant and quadratic equations, then the linear one; its remaining coefficient is D=de-f>0. This gives (INV) and uniqueness.

At the contact v=a, put

`kappa(a,l)=(a/D)[e-a+l(f-da)/f]`. (AMP)

Substitution of (INV), without division by a-e or f-da, gives

`Re U(iu)=kappa(a,l)(a-e)`,

`Im U(iu)/u=kappa(a,l)(f-da)/a`.

Therefore `U(iu)/T(iu)=i y`, with `kappa=y u`. Since u<0, the denominator LEADS B iff kappa<0 and LAGS iff kappa>0. This includes a=e or a=f/d without a removable-denominator mistake.

**Strict stability iff nonzero amplitude.** For all imaginary arguments Re(U/T)=phi/|T|^2≥0. The ratio is analytic in the closed right half-plane and tends uniformly to1 at infinity. The harmonic minimum principle gives strict positive real part inside; hence U has no right-half-plane zero. The ONLY possible imaginary zeros are at u^2=a, because phi is otherwise positive on v≥0 and U(0)=a^2l/f>0. At that contact U=0 iff kappa=0. Thus U is strictly Hurwitz IFF kappa!=0. The degree-seven palindromic corner is then strictly Hurwitz by the same reciprocal root map as for B. This is written ordinary positive-real/root-continuity reasoning, not a numerical root test.

For W_II/W_III, write

`phi1=(v-a)^2(v+l)`, `phi3=(v-b)^2(v+m)`,

with `a in(rho2,rho3)`, `b in(0,rho1)`, l,m>0. These are the EXACT forced forms of the two nonnegative monic cubic pairings, with their positive double contacts. The remaining real root is negative because the constant is positive.

For C3, b<rho1<f/d<e, so kappa(b,m)>0 AUTOMATICALLY. C3 therefore lags and is strict Hurwitz for every m>0. For C1, a>rho2>f/d:

- If a>=e, kappa(a,l)<0 for every l>0: C1 necessarily LEADS.
- If f/d<a<e, define `l_*(a)=f(e-a)/(da-f)>0`. C1 LEADS iff l>l_*(a), LAGS iff 0<l<l_*(a), and is not strictly Hurwitz at l=l_*(a).
- The height wall is strictly decreasing: `l_*'(a)=-fD/(da-f)^2<0`.

In particular, **W_III requires rho2<a<e and 0<l<l_*(a)**. W_II requires the lead side of the wall; C3's lag is automatic. These are exact, all-parameter orientation/stability facts, not small-contact estimates.

## 3. All actual input coordinates from the two contact heights

Put

`Phi=(phi1+phi3)/2`, `Z=(phi3-phi1)/2=z2 v^2+z1 v+z0`.

The center inverse is the v5 monic pairing inverse, reproduced here:

`pi0=Phi(0)/f`,

`pi2=(coeff_v(Phi)+d*pi0+e*(e+coeff_v2(Phi)))/D`,

`pi1=d*pi2-e-coeff_v2(Phi)`,

`m1=pi2+1`, `m2=pi1+m1+2`, `m3=pi0+m1+m2-1`.

For widths define L=w1+w2+w3 and j0=-w1v-L, j1=w2-w1. Direct multiplication yields

`Z=X j0+vW j1`,

`z2=(d+1)w1-w2`, `z1=dL-(f+e)w1+e w2`, `z0=-fL`.

Thus the width inverse is especially short:

`L=-z0/f`, `N=z1-dL+e z2`,

`w1=N/D`, `w2=(d+1)N/D-z2`, `w3=L+z2-(d+2)N/D`. (WIDTH)

No rank or extra consistency condition is omitted: the determinant has nonzero factors f and D. In the contact parameters,

`2z2=m-l+2(a-b)`,

`2z1=b^2-a^2+2al-2bm`, `2z0=b^2m-a^2l`.

Consequently physical positive widths are EXACTLY

`L>0`, `max(0,D z2/(d+1))<N<D(L+z2)/(d+2)`. (CONE)

At fixed T,a,b these are strict LINEAR inequalities in l,m (split the max into two inequalities). They are not an independently chosen pointwise frequency rectangle: (WIDTH) reconstructs the original three INDEPENDENT paired coefficient intervals.

For clarity C1 and C3 recovered by these formulas are precisely the cubics U from (INV). The C1 original palindromic coefficients are (m1-w1,m2-w2,m3+w3); C3 uses (m1+w1,m2+w2,m3-w3). Their cubic difference is 2J(z), J=w1z^2+(w2-w1)z-L. The displayed Phi/Z center-width equations show equality of their pairings; the monic cubic pairing inverse is unique, so their actual polynomials agree. No second box convention is introduced.

## 4. A determinant identity with a physical positive width metric

Define the nonpalindromic width form

`K=X(j0+2j1)+W(2j0-vj1)`.

The four real cubic forms are phi1=Phi-Z, Phi+xi K, phi3=Phi+Z, Phi-xi K. Their actual t-pairings are those forms times (1+t)t^3, as in v5/v10.

Put

`H(v)=w1w2 v^2+[4w1w2+(w1+w2)w3]v+L^2`.

Every coefficient is POSITIVE when widths are positive. The exact identity is

`R(v):=(v+4)Phi(v)^2-v K(v)^2`

`      =(v+4)phi1(v)phi3(v)+4A(v)H(v)`. (DET)

**Direct derivation.** Expanding the two squares gives

`(v+4)Z^2-vK^2=4A(v)[j0^2-v j0j1-vj1^2]`.

The bracket is exactly w1w2 v^2+[4w1w2+(w1+w2)w3]v+L^2=H(v). Since phi1phi3=Phi^2-Z^2, (DET) follows.

**Independent original-corner derivation.** Write P_j for the four actual corner t-pairings. Expanding the rectangle gives

`P2 P4-P1 P3=-t Delta_E Delta_O E_B O_B`.

Here Delta_E=2t(w1t^2+w3t+w2), Delta_O=2(w2t^2+w3t+w1). The product of the two parenthetical width quadratics is t^2H(v), by v=t+t^-1-2; (EO) supplies E_B O_B=-t^3A(v). Also (1+t)^2/t=v+4. Dividing by t^7 yields exactly (DET). This checks the sign and normalization through actual original corners, not an unrelated scalar polynomial.

The physical H family is narrower than arbitrary positive quadratics. If p=w1w2, s=w1+w2 and h=w3, its coefficients satisfy

`H2=p`, `H1=4p+s h`, `H0=(s+h)^2`,

and

`disc(H)=(s^2-4p)(h^2-4p)=(w1-w2)^2(w3^2-4w1w2)`.

Given H2>0,H1,H0, possible positive widths are recovered by L>0, L^2=H0, s(L-s)=H1-4H2, 0<s<L, s^2>=4H2, followed by w3=L-s and w1,w2 as the positive roots of z^2-sz+H2. This is a finite algebraic inverse with at most two s choices and two w1/w2 assignments, coalescing at equalities. It is NOT license to replace H by an arbitrary positive polynomial; in this chart (WIDTH) already fixes the correct widths.

## 5. EXACT two-gap positivity and amplitude admission

Since a and b lie in disjoint proper cells, phi1 and phi3 are nonnegative on v≥0 and never vanish together. Hence Phi>0 everywhere on v≥0. Therefore

`Phi+xi K>=0 AND Phi-xi K>=0 IFF R>=0`.

On A>=0, (DET) makes R>0: if A>0, H>0; at A=0 the two palindromic factors are strictly positive because a,b are not any rho_i. Thus the ENTIRE nonpalindromic positivity question is ONLY

`R(v)>=0 on (rho1,rho2) AND on (rho3,infinity)`. (GAPS)

Equivalently, on either gap,

`Lambda(v):=(v+4)(v-a)^2(v-b)^2(v+l)(v+m)/[-4A(v)H(v)] >=1`.

Lambda tends to infinity at each finite gap endpoint. On the outer gap it also tends to infinity as v→infinity, since its numerator has degree7 and denominator degree5 with positive leading magnitude. At FIXED target/contact/height parameters, both frequency-gap minima are therefore attained; no infimum-at-infinity surrogate is inserted. This is a written frequency-compactness consequence, not an evaluated optimum, global parameter-compactness theorem or arbitrary-box bad-infimum attainment result.

At the target-component roots rho_i, R>0 and phi1,phi3>0, so ALL four actual pairings have STRICT positive margins. The v10 component-zero guard is automatic in this representation, not dropped.

For explicit nonpalindromic amplitudes, write Pmid(iu)=p0-p2v+i u(p1-v), with p_i=pi_i, and use the SAME j0,j1 as above. For sigma=+1 at C2 and sigma=-1 at C4, define

`A_sigma=p0-p2v+sigma*xi*(j0+2j1)`,

`B_sigma=v*(p1-v)+sigma*xi*(2j0-vj1)`.

These are Re D_sigma and u Im D_sigma for D_sigma=Pmid+r0Q_sigma, with actual a_sigma=(s+1)s^3D_sigma at the frequency. At a contact R(v)=0, the appropriate corner satisfies X A_sigma+W B_sigma=0. Its exact amplitude is

`kappa_sigma(v)=[(v-e)A_sigma+X B_sigma]/[(v-e)^2+X^2]`. (AMP2)

The denominator is NEVER zero because X(e)=f-de is nonzero. Contact gives (A_sigma,B_sigma)=kappa_sigma(v)(v-e,X); hence kappa_sigma=y u again. Corner nonvanishing is exactly kappa_sigma!=0, lead is kappa_sigma<0 and lag kappa_sigma>0.

With positive widths, C2 is the unique minimizer on the inner gap and C4 on the outer gap. Indeed E_B,O_B are both negative in the C2 cell, both positive in C4, and the original independent coefficient extrema are strict. Thus every R zero belongs to the indicated minimizing corner, not an arbitrary choice of sign branch.

**Whole-box admission condition:** require kappa_+(v)!=0 at EVERY inner-gap zero of R, and kappa_-(v)!=0 at EVERY outer-gap zero. With the C1 height wall avoided, the palindromic corners are already strictly Hurwitz by Section2. The ratio a/B for any original member is analytic on the right half-plane, tends to1, and has nonnegative boundary real part by the four corner inequalities. The minimum principle excludes right-half-plane zeros. A finite imaginary zero forces a minimum pairing zero; the target components there are nonzero and the minimizing original corner is unique, so its actual values would vanish, contrary to the amplitude condition. At0 every member has constant1. Hence EVERY original member is strictly Hurwitz. This is the complete v10 admission argument, with its component-zero margin supplied automatically and nonzero corner condition retained at ALL zeros, not only selected ones.

## 6. Equivalent W_II/W_III systems and the remaining task

Start with d,e,f>0,D>0; choose a in(rho2,rho3), b in(0,rho1), l,m>0; construct centers/widths using Section3. Impose (CONE), the appropriate C1 height-wall side, (GAPS), and the ALL-zero amplitude admission of Section5. Then:

- **W_II:** C1 is on the LEAD side. Select two DISTINCT inner-gap zeros v_s<v_r of R, with kappa_+(v_r)>0 (C2 lag at the earlier frequency r=t(v_r)) and kappa_+(v_s)<0 (C2 lead at the later frequency s=t(v_s)). The four contacts in frequency order are C1 lead, C2 lag, C2 lead, C3 lag.
- **W_III:** C1 is on the LAG side, hence rho2<a<e and l<l_*(a). Select an inner-gap zero v_r and an outer-gap zero v_d, with kappa_+(v_r)<0 and kappa_-(v_d)<0. The four contacts in frequency order are C4 lead, C1 lag, C2 lead, C3 lag.

Every selected R zero is at least double by global nonnegativity; no exact-multiplicity-two or no-extra-contact assumption is inserted. The target cells force the frequency ordering. Ordinary unwrapped phase on the now-admitted Hurwitz box recovers the precise actual band-orientation chains of v10; no independent unattained band tuple is substituted.

Conversely EVERY actual W_II/W_III point yields exactly these data and inequalities: its palindromic cubic forms have the displayed double-root shapes, Section2 recovers their amplitudes, (WIDTH) uniquely recovers the actual intervals, and the original pairings give (DET)/(GAPS) plus all nonzero amplitudes. Thus this is an EXACT reparametrization, not merely necessary filters.

At the v5/v10 positive-kernel interface, either system's actual four alternating contacts yields a positive annihilation on reciprocal orbits, hence an obstruction to EVERY unrestricted numerator. A point would be an actual reciprocal counterexample and could be enlarged to rational endpoints/all seven positive widths by strict-Hurwitz openness, as in v10. NO such point is supplied. The converse reduction from a negative reciprocal input to these sets still imports v5 first-critical plus v9 and also retains W_I; W_I has NOT been eliminated here.

**Height-plane geometry.** For fixed T,a,b, Phi,Z, the original centers, widths and K are affine in l,m. Therefore (CONE), the height wall and EVERY weak corner inequality Phi±xi K>=0 are affine half-plane constraints in the TWO heights. Their intersection is convex. This is a whole-frequency intersection, NOT a finite LP computation or a proof of feasibility. Contact/nonzero-amplitude requirements and varying T,a,b remain additional genuine geometry.

**Exact residual.** Decide the two explicit gap-minimum systems, with their positive-width cone and nonzero amplitude filters, or supply a uniform contradiction. A new representation is now available: the scalar septic determinant R, physical quadratic H, exact two-height wall and affine height-plane envelope. No W_II/W_III point or emptiness, reciprocal-class answer, general-box answer, novel/SOTA/formal/kernel/family/human/executable acceptance, scientific GO or round closeout is claimed. The original full SPR7 target, eighteen owners, cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 remain unchanged.
