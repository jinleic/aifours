# SPR7 W_III — positive-height/total-width LOWER bounds, an explicit C1 location exclusion, and uniformly guarded fixed-(T,b) slices

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:43:19 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL THEOREM CANDIDATE.** This strengthens v15 from fixed(T,a,b) to fixed(T,b), permitting EVERY C1 pal-contact position a and ALL admissible heights. No small-contact or numerical cutoff is assumed.

Only SYMBOLIC variables, exact fractions and integer-product identities, including privately. No numerical instance/scout, decimal magnitude gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner written-exactness/v18 findings and every old history remain permanent/ZERO probe credit. No frozen source, review or gate is modified or inherited.

## 0. Exact inputs and additive boundary refinement

Use the complete new v11 packet `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, and v15 `reciprocal-WIII-bounded-height-and-uniform-frequency-guards-v15.md`, SHA256 `f7e29b89749e5ee233f0c48c5f7bc6fbc7e19bd8829894d517760e2fc3c47901`. Their complete named v5/v9/v10+erratum interfaces and original scope remain. No positive tuple or emptiness of the general word systems is claimed.

V15 conservatively left height/width collapses uncontrolled in its bounded closure. The NEW argument here excludes l→0 and L=w1+w2+w3→0 even while a varies in the whole W_III lag cell at fixed(T,b). It does NOT exclude m→0, individual width collapse or source-amplitude walls, and it does not backdate this stronger result into v15 or a live gate.

Fix a strictly Hurwitz target T=z^3+d z^2+e z+f, d,e,f>0,D=de-f>0, with phase roots0<rho1<f/d<rho2<e<rho3. Fix ONLY b in(0,rho1). Quantify over EVERY W_III a, l,m and positive widths:

`rho2<a<e`, `0<l<l_*(a)=f(e-a)/(da-f)`, `m>0`.

## 1. A strict lower bound from the ACTUAL width sum

Define

`C(v)=e-2v+d v^2/f=(d/f)(v-f/d)^2+D/d>0`,

`M(v)=C(v)+D v^2/f=(D+d)v^2/f-2v+e>0`.

For the actual height inverse put C0=(a-b)(2e-a-b)>0. The formulas of v11 give

`2(z1+e z2)=C0+l(2a-e)+m(e-2b)`,

`2fL=a^2l-b^2m`, `w1=(z1-dL+e z2)/D`.

Since w2,w3>0, w1<L. Substitution gives the exact strict inequality

`C0<l M(a)-m M(b)`. (LOW)

In particular

`l>C0/M(a)>0`,

`q:=m/l<M(a)/M(b)<a^2/b^2`. (RATIO)

For the last strict inequality, multiply by b^2M(b)>0. Its numerator is

`a^2M(b)-b^2M(a)`

`=(a-b)[e(a+b)-2ab]>0`,

because a>b and e>a, so e(a+b)-2ab=a(e-b)+b(e-a)>0. This proof uses actual w1<L, not an arbitrary independent height cap or a source stability sample.

It also gives

`L=l(a^2-b^2q)/(2f)`

` > l (a-b)[e(a+b)-2ab]/(2f M(b))>0`. (LLOW)

Thus neither l nor the total paired-width sum can approach zero in a fixed slice whose other parameters stay fixed. The uniform version allowing all a follows next.

## 2. A height-free necessary exclusion on the C1 contact position

For a positive l satisfying both(LOW) and the strict lag wall, necessarily

`C0(da-f)<f(e-a)M(a)`.

The difference factors EXACTLY as

`f(e-a)M(a)-C0(da-f)`

`=D(e-a)a(a+1)-(da-f)(e-b)^2`. (LOC)

**Derivation.** Write q0=e-a and r0=e-b, so C0=r0^2-q0^2. Then fM(a)=Da^2+fC(a). Direct expansion gives q0 fC(a)+q0^2(da-f)=a q0D. Adding Da^2q0 and subtracting r0^2(da-f) gives(LOC).

Hence EVERY W_III point satisfies the STRICT target/contact-only condition

`D(e-a)a(a+1)>(da-f)(e-b)^2`. (NEC)

Using a(a+1)<=e(e+1) and da-f=D-d(e-a), it follows that

`e-a>epsilon_b:=D(e-b)^2/[d(e-b)^2+D e(e+1)]>0`.

The expression is increasing in(e-b)^2, so b<rho1 gives the target-only bound

`e-a>epsilon_T:=D(e-rho1)^2/[d(e-rho1)^2+D e(e+1)]>0`. (EGAP)

Thus the C1 lag contact CANNOT drift to v=e even when a,b and heights vary at FIXED T. If epsilon_T>=e-rho2, the ENTIRE W_III slice at that T is EMPTY. No claim that this exclusion applies to every target is made; it is an exact symbolic necessary region.

## 3. Explicit lower/upper bounds uniform over ALL a at fixed(T,b)

On rho2<=a<=e define the fixed positive constants

`Cmin=(rho2-b)(2e-rho2-b)>0`,

`Mmax=(D+d)e^2/f+e>0`,

`l_lo=Cmin/Mmax>0`.

Since C0 is increasing in a on this interval and M(a)<=Mmax, (LOW) gives l>l_lo.

Put

`Fmin=(rho2-b)rho2(e-b)>0`,

`L_lo=l_lo Fmin/[2f M(b)]>0`.

Because (a-b)[e(a+b)-2ab]>=Fmin, (LLOW) gives L>L_lo UNIFORMLY over ALL a, heights and points in the fixed(T,b) slice.

For upper bounds use the strictly decreasing wall l_*(a):

`l_hi=l_*(rho2)=f(e-rho2)/(d rho2-f)>0`,

`m_hi=e^2 l_hi/b^2`, `L_hi=e^2 l_hi/(2f)`.

Then

`l_lo<l<l_hi`, `0<m<m_hi`,

`L_lo<L<L_hi`, `0<w_i<L_hi`. (UNIFORM)

These remain valid on the nonnegative-width closure with non-strict outer inequalities. They do not give a positive lower bound for EACH individual width or for m.

Substituting a<=e, l<=l_hi, m<=m_hi and w_i<=L_hi into v15's coefficient formulas gives an explicit fixed(T,b) norm bound ||R||_1<=M_R and hence EVERY positive nonpal contact v<1+M_R. For completeness one may take

`P2_hi=(l_hi+m_hi)/2+e+b`,

`P1_hi=(e^2+b^2)/2+e l_hi+b m_hi`, `P0_hi=e^2 l_hi`,

`P_hi=1+P2_hi+P1_hi+P0_hi`,

`K_hi=(6d+4f+4e+4)L_hi`, `M_R=5P_hi^2+K_hi^2`.

Thus v15's outer-frequency/no-parameter-upper-escape bounds now hold uniformly while the C1 pal contact a varies, not just at a fixed a. The same quotient-cubic/factor bounds there apply with these constants.

## 4. Quantitative component-zero margin lemma — no strict denominator assumption needed

This lemma uses the ORIGINAL independent coefficient intervals, not a substituted frequency rectangle.

Let t0>0 be ANY simple positive zero of E_B OR O_B. Define

`mu0=min(1,t0,t0^2)>0`.

All pairings P_(a,B)(t) are nonnegative on t>=0, by the global corner inequalities and coefficient linearity. At t0 choose the nonzero-multiplier coefficient block to minimize the pairing, giving p_min>=0. Vary the OTHER independent block between its actual extrema, retaining that minimizing block fixed. This yields TWO actual denominator members with the SAME pairing value p_min at t0.

- If E_B(t0)=0, their derivative difference is Delta_E(t0)E_B'(t0). The paired-width structure gives Delta_E(t0)=2t0(w1t0^2+w3t0+w2)>=2t0 mu0 L_lo.
- If O_B(t0)=0, their derivative difference is t0 Delta_O(t0)O_B'(t0), with Delta_O(t0)=2(w2t0^2+w3t0+w1)>=2mu0 L_lo.

Thus in either case the magnitude is at least the fixed positive number

`c_*=2t0 mu0 L_lo * |B_component'(t0)|>0`.

The component root is simple because the FIXED target B is strictly Hurwitz and has strictly interlacing components. At least one of the two pairing derivatives therefore has magnitude at least c_*/2.

Suppose ALL original pairing second derivatives are bounded in magnitude by M2_*>0 on[t0/2,3t0/2]. Choose

`h_*=min(t0/2,c_*/(2M2_*))>0`.

For the member whose derivative has the indicated magnitude, move by h_* in the OPPOSITE derivative direction. Taylor's theorem and nonnegativity there give

`p_min>=|P'(t0)|h_*-(M2_*/2)h_*^2>=c_*h_*/4>0`. (MARGIN)

This gives a STRICT margin for ALL original pairings at t0, uniformly over the entire fixed(T,b) slice. It does NOT require individual widths bounded below, a uniformly strict denominator Hurwitz margin or a nonzero corner-amplitude assumption. At least one paired width remains positive through L_lo, so BOTH parity blocks still vary independently. Exact source-pairing nonnegativity and target-component simplicity are the key hypotheses.

## 5. Explicit source/pairing derivative bound and uniform target-wall guards

All quantities below depend ONLY on fixed T,b. From the actual center inverse, use

`C0_hi=P0_hi/f`,

`C2_hi=[P1_hi+d C0_hi+e(e+P2_hi)]/D`,

`C1_hi=d C2_hi+e+P2_hi`.

Then |m1|<=C2_hi+1, |m2|<=C1_hi+C2_hi+3 and |m3|<=C0_hi+2C2_hi+C1_hi+3. Put these three upper bounds equal to M1_hi,M2_hi,M3_hi, and set

`A_hi=2+2 sum_(j=1)^3(Mj_hi+L_hi)`.

Every original denominator has coefficient absolute-sum at most A_hi. The target B has positive coefficients and

`B_hi=B(1)=2(8+4d+2e+f)`.

The coefficient absolute-sum of each degree<=7 pairing is at most A_hi B_hi, by multiplication/triangle inequalities on its even/odd components. Hence on[t0/2,3t0/2] one may use the explicit second-derivative bound

`M2_*=42(1+3t0/2)^5 A_hi B_hi`.

This completes every constant in(MARGIN), with no evaluator, sampled bound or uncomputed minimization.

For i=1,2,3 let t_i=t(rho_i) in(0,1), and use(MARGIN) to obtain epsilon_i>0 at that target-component root. Divide by its positive pairing scale to put

`nu_i=epsilon_i/[(1+t_i)t_i^3]>0`.

Both palindromic forms satisfy phi1(rho_i),phi3(rho_i)>=nu_i UNIFORMLY over a and heights. Therefore

`|a-rho_i|>=sqrt(nu_i/(rho_i+l_hi))>0`,

because phi1(rho_i)=(rho_i-a)^2(rho_i+l) and l<=l_hi. In particular C1 also stays uniformly AWAY FROM rho2, not merely below e-epsilon_T. No target-wall collision is possible.

Moreover

`R(rho_i)=(rho_i+4)phi1(rho_i)phi3(rho_i)>=(rho_i+4)nu_i^2`.

With V_hi=1+M_R+rho3 and derivative bound |R'|<=7M_R V_hi^6 on[0,V_hi], every positive R root v0 has the uniform guard

`|v0-rho_i|>=(rho_i+4)nu_i^2/[7M_R V_hi^6]>0`.

This includes every selected, unselected and higher-multiplicity contact. All source correlations and actual phase walls are retained. Neither target-wall guards nor outer-frequency bounds are numerical searches.

## 6. Exact boundary inventory after this stronger result

At FIXED T,b the complete W_III finite system now has:

- C1 a in a compact guarded subinterval of(rho2,e), from(EGAP)/(MARGIN);
- l bounded BOTH above and away from0;
- total paired width L bounded BOTH above and away from0;
- bounded m, original coefficients and positive-factor coordinates;
- all nonpal frequencies bounded and separated from every target component wall.

STILL OPEN and NOT waived:

- m→0, where the C3 palindromic corner can lose its frequency1 Hurwitz margin;
- individual w_i→0 while L stays positive;
- C1 or nonpal denominator amplitudes→0 inside their proper cells;
- variation of T or b, where these fixed-slice constants need not stay uniform.

Those actual source/admission boundary faces still prevent an automatic global attainment or universal answer. The theorem supplies a larger guarded domain and a genuine contact-location exclusion, not a solved W_III feasibility problem. The original reciprocal union (including W_I/W_II) and universal general-box SPR7 remain OPEN. No formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, new GO, source cutover, nineteenth owner, deadline reset or round closeout. Original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence remain binding; work is active.
