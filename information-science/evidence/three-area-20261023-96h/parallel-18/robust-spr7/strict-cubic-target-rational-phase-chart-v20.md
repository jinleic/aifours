# SPR7 — a complete rational phase-root chart for EVERY strict cubic target, with a root-free W_III target screen

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:07:47 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN REPRESENTATION THEOREM CANDIDATE.** This rationalizes the ENTIRE strict-cubic target phase domain; it does not impose rational-root or small-parameter hypotheses on the original target. No physical obstruction point, emptiness of the full systems or universal SPR7 result is claimed.

Only SYMBOLIC variables and exact algebra/inequalities, privately too. No numerical target sample or decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner exactness/v18 process findings and every old history remain permanent/ZERO probes. Frozen sources/reviews/gates unchanged.

## 0. Named inputs and exact result

Use the complete v11 phase-cubic identity `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, and, ONLY for the W_III screen, v16 `reciprocal-WIII-positive-width-lower-bounds-and-guarded-target-slices-v16.md`, SHA256 `850f35ab4b266e21ab5cf13a0c8885a1cd918f0899a432ae73ecae027ed369da`. All original reciprocal v5/v9/v10+erratum and ordinary-written assurance remain.

**Theorem.** Strict cubic targets T=z^3+d z^2+e z+f with d,e,f>0,de>f are in BIJECTION with the real parameter domain

`d>u>0`, `u/(1+u)<v<1`.

Every target coefficient and EVERY positive root of its phase cubic is an explicit RATIONAL function of d,u,v. The parameters u,v are arbitrary REAL variables; requiring them rational would be an EXTRA restriction, and is not done here.

This removes cubic-root selectors from the exact target/word systems. It is not a time/frequency normalization of the original interval box and changes no coefficient-independence assumption.

## 1. Forward construction — all signs and phase roots explicit

For the displayed parameter domain put

`p=u^2/(1+u)`, `q=v^2/(1-v)`,

`h=(q-p)/(u+v)=(v-u+uv)/[(1-v)(1+u)]>0`.

Define

`e=p+(d+v)h`,

`f=d p+u(d+v)h`,

`D=de-f=(d-u)(d+v)h>0`. (TARGET)

All d,e,f are positive; hence T is strictly Hurwitz by the ordinary cubic criterion. Also

`e-p=(d+v)h`, `e-q=(d-u)h`,

`f-dp=u(e-p)>0`, `dq-f=v(e-q)>0`.

Therefore

`0<p<f/d<q<e`.

For the phase cubic A(w)=(f-dw)^2-w(f-dw)(e-w)-w(e-w)^2, the identities

`u^2-pu-p=0`, `v^2+qv-q=0`

give A(p)=A(q)=0. V11's sign/root proof then identifies

`rho1=p`, `rho2=q`,

`rho3=f^2/[(d+1)pq]>e`. (ROOTS)

The third formula follows from the cubic constant/leading coefficients, so it too is rational. Positivity/root ordering and simplicity are inherited from the same strict cubic sign proof, not guessed after computing roots. No additional root must be selected or tested numerically.

## 2. Every strict cubic target has these UNIQUE coordinates

Start with ANY d,e,f>0,D=de-f>0. Let rho1<rho2<rho3 be its three simple phase roots. V11 proves

`0<rho1<f/d<rho2<e<rho3`.

Define the positive ratios

`u=(f-d rho1)/(e-rho1)`,

`v=(d rho2-f)/(e-rho2)`.

At A(rho1)=0 and A(rho2)=0 they satisfy

`u^2-rho1 u-rho1=0`, `v^2+rho2 v-rho2=0`.

Thus rho1=u^2/(1+u) and rho2=v^2/(1-v), with u>0 and0<v<1. Since rho2>rho1,

`rho2-rho1=(u+v)(v-u+uv)/[(1-v)(1+u)]>0`,

so v>u/(1+u). The identity D=(d-u)(e-rho1)>0 gives d>u. Subtracting the two exact equations for f gives

`e=rho1+(d+v)(rho2-rho1)/(u+v)`,

`f=d rho1+u(d+v)(rho2-rho1)/(u+v)`.

These are exactly(TARGET). Both u,v were uniquely determined by the original target/ordered roots, and the forward construction recovers those same roots. Hence the map is a true bijection on the whole real strict-cubic domain, not a selected rational phase-root subfamily.

## 3. W_III's target screen is now a rational inequality without root variables

V16 proves the necessary bound

`e-a>epsilon_T=D(e-rho1)^2/[d(e-rho1)^2+D e(e+1)]`

for every W_III point, whereas a>rho2 gives e-a<e-rho2. Therefore epsilon_T>=e-rho2 excludes W_III.

Using(TARGET), set r1=e-rho1=(d+v)h and r2=e-rho2=(d-u)h. Then D=(d+v)r2. All denominators are positive, so

`epsilon_T>=r2`

`IFF v r1^2>=D e(e+1)`

`IFF v(d+v)h>=(d-u)e(e+1)`. (SCREEN)

Consequently EVERY W_III target must satisfy the STRICT rational inequality

`(d-u)e(e+1)>v(d+v)h`.

Here e,h are the explicit rational functions above. Denominator clearing uses only positive factors (1-v),(1+u),(u+v), so this is an ordinary finite polynomial screen if desired; no unresolved cubic-root comparison remains. It is a sufficient exclusion screen, not a proof of W_III feasibility on the opposite side.

The explicit polynomial region already excluded by v19 is a coefficient-only sufficient subset of this screen. The current chart does not erase that theorem or claim a new full decision.

### 3a. EVERY fixed phase shape has one positive-root target threshold

Fix u>0 and u/(1+u)<v<1. Then p,q,h are fixed positive quantities; let delta=d-u>0. Since q=p+(u+v)h, the target coefficient is e=q+h delta. The necessary W_III screen becomes

`G(delta):=h^2 delta^3+h(2q+1)delta^2+[q(q+1)-v h]delta-v h(u+v)>0`. (THRESH)

EVERY nonconstant coefficient of G is strictly positive. Indeed h=(q-p)/(u+v)<q/(u+v), so v h<q and C:=q(q+1)-v h>q^2>0. Thus G is strictly increasing on delta>=0, G(0)<0 and G tends to infinity. There is EXACTLY ONE positive zero delta_*(u,v).

Consequently W_III has NO point with this phase shape for

`0<d-u<=delta_*(u,v)`.

Every W_III point must have d-u>delta_*. This is a uniform forbidden initial segment for EVERY phase shape, not an ad-hoc numerical near-boundary condition. It is still only a necessary target screen: the opposite segment is NOT declared feasible.

The threshold has explicit positive RATIONAL brackets in u,v. Put

`F=v h(u+v)`, `C=q(q+1)-v h`, `U=F/C`,

`L=F/[C+h(2q+1)U+h^2 U^2]`.

Then `0<L<delta_*<U`. The upper bound follows by substituting U into G; the positive higher-degree terms make G(U)>0. For the lower bound use F=delta_*[C+h(2q+1)delta_*+h^2 delta_*^2] and delta_*<U. No numerical root or bracket is evaluated. The exact root is selected unambiguously by a cubic with positive derivative; alternatively (THRESH)>0 itself is the root-free rational test.

## 4. Exact contact-coordinate intervals, retaining ALL original geometry

For W_III, pal contacts can now be written

`b=theta*p`, `a=q+eta*(d-u)h`, `0<theta<1`, `0<eta<1`.

A nonpal inner contact is r=p+xi*(q-p),0<xi<1, and an outer contact is s=rho3+tau,tau>0. These are RATIONAL functions of the real chart variables. V16's exact guards further restrict eta,xi,tau, without imposing arbitrary caps or dropping the source-amplitude faces. W_II uses a in(q,rho3), not the W_III restriction a<e; its entire target domain is still the same d,u,v chart.

Original physical half-frequency t(w)=(w+2-sqrt(w(w+4)))/2 remains the exact decreasing reciprocal conversion. The chart rationalizes phase roots and input/height algebra, NOT that final positive square-root frequency map. It does not change the original denominator polynomial or the independent coefficient intervals. Square roots can be kept by exact positive-root equations in any later finite semialgebraic formulation.

## 5. Distinct boundary mechanisms are now explicit

The chart identifies different potential degenerations instead of calling all of them 'small Hurwitz determinant':

- d-u→0 with h bounded away from0 makes rho2 approach e while rho1 can remain separate; this is the side controlled by the W_III screen near that boundary.
- h→0, equivalently v→u/(1+u), makes rho1,rho2,e coalesce while d-u may stay positive. It is a DIFFERENT target-phase collision and is not excluded merely by the first boundary's argument.
- u→0 can drive f and rho1 to0.
- v→1 or unbounded d can produce unbounded target coefficients/phase ranges.

These are mathematical boundary descriptions with the other variables appropriately controlled, not evaluated limit families, numerical viability evidence or a proof that each boundary is realized by a physical obstruction. They are not all silently compactified away.

The next exact task is to combine(SCREEN), the signed-amplitude/positive-width cone, and the positive-factor coefficient equations in this rational target chart. Physical feasibility of W_I/W_II_strict/W_III and the original general-box SPR7 question remain OPEN. No actual tuple, scientific execution/new GO, formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, source cutover, nineteenth owner, deadline reset or round closeout. Same science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence; written work remains active.
