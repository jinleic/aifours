# SPR7 — ALL-phase LINEAR contact escape, and large-delta exclusion INCLUDING h=U plus an OPEN region beyond it

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 08:28:43 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN NECESSARY-ESCAPE/PARTIAL-EMPTINESS CANDIDATE.** This no longer assumes bounded a or divides by U-h. It proves an all-phase uniform source-coefficient growth bound, forcing a to grow LINEARLY with delta on any surviving large-delta WIII branch. Combined with the actual source-phase guard it excludes an enlarged phase region, including h=U and an open region with h>U. No physical family or point is exhibited.

All-variable conventional exact proof only, including privately. No numeric/control trial, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FIVE owner findings/parentv37/current history permanent; fifth probe/consuming guidance ZERO credit. Qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded these proofs. Later body OUTSIDE v11-v29 snapshot; no old freeze widening.

## 0. Exact scope, source and constants

Retain ANY real phase shape U>0,U/(1+U)<V<1 and

`p0=U^2/(1+U)`, `q=V^2/(1-V)`,

`h=(q-p0)/(U+V)>0`, `r=p0+Uh>0`.

For delta>0 the strict target is

`d=U+delta`, `e=q+h delta`, `f=Uq+r delta`,

`D=delta(d+V)h`.

The proof uses the full qualified v11 actual inverse/width/word source SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, full v20 target chart SHA256 `530f87473ec31f592bc7b7ac46a9caf1b7292c1a1790314cca8d056506ae6fb7`, and COMPLETE new v30 physical source-phase guard k(a)>U and its width proof, SHA256 `b9401c9b459adf453d979f1dd264987ef636b6f7acf0a4d81a9dd419c2b46914`. Every new use requires fresh complete reconstruction, not acceptance by a hash or old verdict.

All conclusions concern ACTUAL admitted WIII points: q<a<e,0<b<p0,l,m>0; all original widths positive; C1 lag/C3 lag, inner-C2 lead, outer-C4 lead; full global pairings and ALL source/extra-zero guards. No hypothesis h<U is imposed here.

Define fixed positive phase constants

`E=q+h`, `F=Uq+r`, `J=(U+1)/r`,

`G=[(1+U+V)h+U+1]/r`,

`L=F E q/(Vh)`,

`M=(2L/h)(G+E/q^2)`.

First work on the symbolic domain

`delta>=delta_base=max{1,4p0/h}`.

These are uniform symbolic bounds, not values tried as individual parameters.

## 1. Sharper height bounds with UNBOUNDED a retained

For delta>=delta_base,

`e<=delta E`, `f<=delta F`, `f>=delta r`,

`d<=delta(U+1)`, `D>=delta^2h`.

Since a>q>r and q-r=Vh,

`a-r>=a(q-r)/q=a Vh/q`,

`da-f=U(a-q)+delta(a-r)>delta a Vh/q`.

The actual C1 lag ceiling therefore gives

`l<l_*<=delta L/a`. (LHEIGHT)

From original positive widths, with C0>0 and the exact M_source(x)=(D+d)x^2/f-2x+e,

`0<C0<l M_source(a)-m M_source(b)`.

The target bounds imply

`M_source(a)<=delta(G a^2+E)`,

`M_source(b)>=delta h/2` uniformly for ALL0<b<p0.

As a>q, E/a<=Ea/q^2. Hence

`m<l M_source(a)/M_source(b)<=delta M a`. (MHEIGHT)

These bounds allow a to grow with delta; they neither assume compact contacts nor hide a fixed-b lower bound.

## 2. ALL original source coefficients grow AT MOST LINEARLY in a

For a pal source at contact zeta,height eta, use the EXACT actual cubic coefficients

`A_U=[(zeta-e)^2+eta C_zeta]/D`,

`B_U=[f C_zeta+eta X_zeta^2/f]/D`,

`C_U=zeta^2 eta/f`,

`C_zeta=e-2zeta+d zeta^2/f`, `X_zeta=d zeta-f`.

### 2.1 C1 at contact a and height l

Since a<e<=delta E,

`C_a<=delta E+J a^2`,

`0<X_a<d a<=delta(U+1)a`,

`|a-e|<=delta E`.

Insert(LHEIGHT) and the target bounds. The coefficient estimates are

`A_U1<=A10=E^2/h+LE/(qh)+LJE/h`,

`B_U1<=B10+B11 a`,

`B10=FE/h`,

`B11=[FJE+L(U+1)^2/r]/h`,

`C_U1<=C11 a`, `C11=L/r`.

For the A estimate, l C_a/D<=LE/(a h)+LJa/(delta h), then a>=q and a/delta<E. For B, f C_a/D<=FE/h+FJa^2/(delta h), and a^2/delta<Ea; the height term is at most L(U+1)^2a/(rh). These are exact inequalities, not leading-order asymptotics.

### 2.2 C3 at contact b and height m

Set

`Cb=E+Jp0^2`, `Xb=(U+1)p0+F`.

Then C_b<=delta Cb, |X_b|<=delta Xb and |b-e|<=delta E. From(MHEIGHT),

`A_U3<=A30+A31 a`,

`A30=E^2/h`, `A31=M Cb/h`,

`B_U3<=B30+B31 a`,

`B30=F Cb/h`, `B31=M Xb^2/(rh)`,

`C_U3<=C31 a`, `C31=p0^2 M/r`.

All estimates are uniform over b approaching0.

### 2.3 Every ACTUAL original corner, not merely the pal cubic coefficients

The largest of the three original paired septic coefficients for U is C_U+B_U+2A_U+3. Therefore define

`Q0=max{3+2A10+B10,3+2A30+B30}`,

`Q1=max{B11+C11,2A31+B31+C31}`.

Both are positive finite continuous phase functions and Q0>=3. Every one of the six original coefficients of C1,C3 and their ACTUAL mixtures C2,C4 obeys

`0<Ai<=Q0+Q1 a`. (LINEARQ)

This is a NEW ALL-phase coefficient bound. It does not assert a itself is bounded. V31 used h<U to bound a first; here that restriction has been removed and the growth rate is controlled explicitly.

## 3. All-phase necessary LINEAR escape of the pal contact

Set

`S=F+E+2(U+1)+3`,

`delta0=max{delta_base,8S/(h+1)^2}`.

The actual target even polynomial is

`E_B(t)=1-(e+d+3)t+(f+e+2d+3)t^2-(d+1)t^3`.

For delta>=delta0 it is at most-1/2 at t_test=2/[delta(h+1)], exactly as the direct bound

`E_B(t_test)<=-1+4S/[delta(h+1)^2]`

shows. Thus the target's entire outer C4 cell lies below t_test.

Let Q(a)=Q0+Q1a. By(LINEARQ), for0<t<=1/[4Q(a)] the ACTUAL C4 even component obeys

`E_C4(t)>=1-Q(a)(t+t^3)>=1/2>0`.

A selected outer-C4 LEAD contact instead requires E_C4=-y sqrt(t)O_B<0. Therefore an actual WIII point with delta>=delta0 must have

`delta<8[Q0+Q1a]/(h+1)`. (ESCAPE)

Otherwise t_test<=1/[4Q(a)] and the entire outer cell has the wrong source-even sign.

If additionally delta>=16Q0/(h+1), (ESCAPE) forces

`a>c delta`, `c=(h+1)/(16Q1)>0`. (LINEAR_ESCAPE)

This is uniform over ALL source heights, b, positive width ratios and determinant/source admission branches. It is a NECESSARY escape rate, NOT an actual unbounded physical family or asymptotic solution.

## 4. Combine with the physical source-phase guard: an ENLARGED tail-exclusion domain

V30's exact guard k(a)>U is

`(a-q)(a+U^2)<delta[(h-U)a+Ur]`. (PHASEGUARD)

Define the exact phase function

`sigma=c/2-(h-U)`.

Suppose sigma>0. For delta>=2q/c, (LINEAR_ESCAPE) gives a>2q, so

`a^2/2<(a-q)(a+U^2)`.

Using(PHASEGUARD), dividing by delta a, and a>c delta yields

`c/2 < a/(2delta) < h-U+Ur/a < h-U+Ur/(c delta)`.

Therefore EVERY such WIII point must satisfy

`delta<Ur/(c sigma)`.

Thus the finite explicit bound

`delta_upper_extended=max{delta0,16Q0/(h+1),2q/c,Ur/(c sigma)}`

proves:

**For EVERY fixed phase shape with sigma>0, WIII is EMPTY for EVERY delta>=delta_upper_extended, uniformly over ALL original contacts/heights/positive widths.**

The quantities are fully specified (piecewise) rational functions of the REAL phase parameters. No rational-valued instance, numerical certificate or feasible family is asserted.

## 5. Why this strictly extends the phase domain of v31

All h<=U satisfy sigma>=c/2>0, so the new tail theorem covers the ENTIRE CLOSED wedge h<=U, including the formerly uncovered equality h=U. No denominator U-h appears in any constant.

It also covers an OPEN region with h>U: every phase shape on h=U is interior to the original phase chart, all constants Q0,Q1,c are continuous there and c>0. Hence sigma>0 persists in an open neighborhood across that locus. This is a symbolic continuity argument, not a selected numerical instance.

The complete v31 proof SHA256 `847613138d4e7080fb11fcf0cad3dc2b7161b050a52ed69eaa55bb8e642e549c` gave a different explicit tail bound on h<U. The present theorem EXTENDS ITS DOMAIN and supplies the new ALL-phase linear-escape lemma; its explicit upper bound need not be numerically smaller than v31's at every old phase shape. Both bounds may be retained where both apply. No old source or claim is overwritten.

In the remaining phase region sigma<=0 the tail exclusion is NOT proved. The all-phase necessary escape(ESCAPE)/(LINEAR_ESCAPE) still applies and forces any sufficiently large-delta physical WIII point to have a growing at least linearly. Such growth and the full contact/width/source equations must be analyzed, not assumed achievable.

## 6. Residual and assurance

Combined with v30, every phase shape in sigma>0 has an exact necessary target slab delta_new<delta<delta_upper_extended (and may use the smaller v31 bound when applicable). Neither slab nonemptiness nor emptiness is asserted. Outside sigma>0 the remaining large-delta system is constrained by a>c delta but still OPEN. WI/WII_strict, distinct source/pal/width/target boundaries and original universal nonreciprocal SPR7 remain OPEN.

The new proof is a uniform actual-coefficient-growth and opposite-tail result, not a repetition of tiny-r or fixed-target compactness, not an arbitrary frequency rectangle, and not parameter-scanning progress. No actual tuple, feasibility, global full emptiness, attainment, strict perturbation or finite certificate. WRITTEN only; no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty/parent acceptance. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30mincadence, no GO/early park/round closeout; primary active.
