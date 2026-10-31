# SPR7 — the ENTIRE surviving inner limit is IMPOSSIBLE, including zero source amplitude: delta is BOUNDED at EVERY fixed phase shape

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 09:14:10 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN EXCLUSION/BOUNDEDNESS CANDIDATE.** V33 excluded h<=8 but left a possible h>8 rescaled tail. This packet excludes that ENTIRE remaining weak model, including the inner source-imaginary-zero case that cannot be divided away. Consequently no fixed-phase actual WIII tail has unbounded delta. This is NOT full WIII emptiness, not a uniform bound over varying phase shapes and not global physical attainment.

All-variable conventional exact proof only, privately too. No numeric/control instance, evaluated parameter/sequence member, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FIVE owner findings/parentv37/history permanent; fifth probe/consuming guidance ZERO credit. Qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded these later proofs. Outside v11-v29 snapshot; no old-source/freeze change.

## 0. Exact mathematical versus physical application scope

The proof is first an algebraic contradiction for the COMPLETE weak rescaled model. Its application to ACTUAL WIII requires ENTIRE v33, SHA256 `6eadd33525db09695cb268102ea3f6056de2d5ff2922d0e8640f6d6a191865e8`, and ENTIRE v34, SHA256 `2395569291feb3dde73c8fcc861bc83cad9969177383a1b88a4258f45fd5cf9d`, including all their operative v11/v20/v30/v32 sources/errata. No old verdict, hash or statement of compactness substitutes for those actual hypotheses/proofs. Both full mathematics AND dependency/application need a fresh complete gate.

V33/V34 show that ANY hypothetical unbounded actual tail at a FIXED phase shape has a subsequential weak model satisfying:

`U>0`, `K>U`, `h=(K-U)/(1+U)`, `p0=U^2/(1+U)`,

`r=p0+Uh`, `H=1+h`,

`0<=b<=p0`, `j=(b-r)^2/(rh)`, `k=b^2/r`,

`beta>0`, `N=beta+4(H-A)>beta`, `M=N/(1+j)>0`,

`Y=gamma/beta>U`,

`Y<=Y_*=[j+k+sqrt((j+k)^2+4k)]/2<=r/h`,

and a selected inner DOUBLE zero tau strictly in(1/(1+K),1/(1+U)) with nonnegative LEAD amplitude. The target/source quartic is the EXACT physical-t polynomial G4 of v34, not its compact determinant in v.

If h<=8, v33 already gives a contradiction. We therefore retain h>8 below. All source/pal/width boundary limits allowed by v33/v34 are STILL allowed: b may be0, a leading width may vanish, Y may equalY_* and the selected source amplitude may be0. The proof must handle them.

## 1. A boundary coordinate makes the ENTIRE inner zero equation exact

Write

`tau=1/(1+U+w)`, `R=1+U+w`,

so the strict inner phase cell gives

`0<w<K-U`.

Set

`z=Y-U>0`, `z_*=Y_*-U>=z`.

The selected nonnegative lead means Ctau-beta>=0, where C=beta+gamma=beta(1+Y). Thus

`w<=z<=z_*<=p0/h`. (STRIP)

Let

`f0(v)=v^2-(j+k)v-k`.

Its positive root is Y_* and its nonpositive root is -kappa, with kappa=k/Y_*>=0. Hence

`f0(v)=(v-Y_*)(v+kappa)`.

Define the strictly positive target factors

`At=R(1+K)-1`, `Bt=R(1+U)-1`,

`Dt=(K-U-w)Bt>0`.

The physical target quadratics at tau are EXACTLY

`Ebhat(tau)=-w At/[R^2(1+U)]`,

`Obhat(tau)=-Dt/[R^2(1+U)]`.

The source factors are

`Ctau-beta=beta(z-w)/R`,

`M-D0*tau+N*tau^2=M f0(U+w)/R^2`.

Substituting into the ENTIRE G4 zero equation gives

`beta*w*(z-w)*At=-M f0(U+w)*Dt`. (ZEROEQ)

No selected numerical frequency or approximation is used; these are algebraic identities at arbitrary symbolic w in the full cell.

## 2. NONZERO and ZERO source-amplitude cases give the SAME necessary lower bound

### 2.1 Strict lead amplitude: w<z

Using the exact factorization of f0,

`-f0(U+w)/(z-w)`

`=[(z_*-w)/(z-w)](U+w+kappa)>=U+w`.

Divide(ZEROEQ) by its strictly positive factors. It follows that

`beta/M >= (U+w)(K-U-w)Bt/(w At)`. (LOWER)

### 2.2 Zero lead amplitude: w=z

This case is NOT discarded or divided by z-w. (ZEROEQ) instead forces f0(Y)=0, hence Y=Y_* and z=z_*: it is precisely the allowed one-source-imaginary-pair limit.

The selected pairing has derivative0 too. Let

`J(w)=beta*w*(z-w)*At+M f0(U+w)*Dt`.

It is a nonzero positive scalar multiple (with a minus sign) of G4(1/R). At a zero, the derivative of that scalar does not contribute; G4'=0 therefore gives J'=0. At w=z=z_* this becomes

`beta*w*At=M f0'(Y_*)*Dt`.

But f0'(Y_*)=Y_*+kappa>=U+w. Therefore the SAME bound(LOWER) holds.

This explicitly covers a vanishing source value and any higher pairing multiplicity. It does not assume the limiting source strict or overlook its axis-zero case.

## 3. The target-root geometry makes that lower bound TOO LARGE

The exact identity

`K Bt-U At=(R-1)(K-U)>0`

gives Bt/At>U/K. Thus(LOWER), with U+w>U, implies

`beta/M > U^2(K-U-w)/(K w)`.

By(STRIP), w<=p0/h=U^2/(K-U). The right side, a decreasing function of w, is at least

`[(K-U)^2-U^2]/K=K-2U`.

Hence EVERY possible weak selected contact in the model would require

`beta/M>K-2U`. (TOOLARGE)

This inequality holds in BOTH amplitude cases and does not require a positive lower bound on b or on the leading third width.

## 4. The forced outer contact makes the same ratio TOO SMALL

The COMPLETE outer rescaling of v33 gives M=N/(1+j), N>beta. Therefore

`beta/M=beta(1+j)/N<1+j`.

As0<=b<=p0<r,

`j=(r-b)^2/(rh)<=r/h`.

Consequently

`beta/M<1+U+p0/h`. (TOOSMALL)

But K-U=(1+U)h. With h>8,

`K-2U=(1+U)(h-1)+1`

`>(1+U)(1+1/h)>1+U+p0/h`.

Here h-1>1+1/h follows from h^2-2h-1>0, and p0<U<1+U. These are uniform symbolic inequalities on the derived whole regime h>8, not a numeric parameter check.

(TOOLARGE) and(TOOSMALL) contradict each other. Thus the ENTIRE surviving h>8 weak model is EMPTY. Together with v33's h<=8 width contradiction, there is NO weak rescaled model for ANY fixed phase shape.

## 5. Exact ACTUAL conclusion: fixed-phase depth boundedness, not WIII emptiness

Suppose actual admitted WIII points at a fixed real phase shape U,V had unbounded delta. V33 supplied explicit bounds on ALL rescaled variables and permitted every relevant limit face; v34 supplied the full inner polynomial/source strip and proved its selected contact could not escape to target walls. The resulting model has now been contradicted in ALL h-regimes and BOTH source-amplitude cases.

Therefore for EVERY fixed real phase shape U,V,

**the set of deltas of ACTUAL admitted WIII points is BOUNDED ABOVE.**

The bound is NONCONSTRUCTIVE here: no explicit numerical or symbolic cutoff function is computed. V31/v32 retain their separate explicit bounds where applicable. V30's strictly stronger lower threshold remains, so every fixed-phase actual WIII problem is confined to a finite depth interval if nonempty.

This does NOT make the remaining full physical set compact/admissibly closed, prove attainment, or empty a finite depth interval. Phase U,V may still vary toward their own boundaries and the bound need not be uniform over them. b0, individual-width0, pal/source walls and phase-shape escapes remain genuine separate issues. WI/WII_strict and the original nonreciprocal universal problem remain OPEN.

## 6. Consequence for the just-supplied CONDITIONAL germ route — no history rewrite

The complete v35 theorem, SHA256 `f36ed8832abd394ad09090b41f57cfff4ca1d7ec6d00a7b0c67e84d2d2e3a17e`, proved a conditional full finite-epsilon bridge from a STRICT model point and explicit nonzero derivative; it DID NOT assert such a point existed.

Its strict prerequisite is a SUBSET of the weak model excluded here. Hence the prerequisite is now proved EMPTY at this author-WRITTEN level. The conditional theorem remains logically valid but cannot produce a physical counterexample by this route. No old source is edited and no actual family claim is retracted, because none was made. This is a new prospective mathematical route exclusion, not an execution/process absolution.

The next work must change representation or attack the remaining finite-depth/phase-shape system, not keep searching this contradicted fixed-phase large-depth model or report another timeout as progress.

## 7. Assurance and remaining original task

This is genuine full closure of the fixed-phase unbounded-depth route, not a narrower sampled instance or just the old target screen. The zero-amplitude derivative case was proved separately, so the conclusion does not rely on an illicit nonzero-source division. Full mathematics and actual dependency/application remain fresh-review candidates at their exact stated quantifiers.

No actual tuple, physical feasibility, full WIII/global emptiness, global attainment, strict perturbation, unrestricted SPR7 resolution, finite executable certificate or novelty. WRITTEN only; no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/parent acceptance. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30mincadence; no GO/early park/source cutover/round closeout, primary active.
