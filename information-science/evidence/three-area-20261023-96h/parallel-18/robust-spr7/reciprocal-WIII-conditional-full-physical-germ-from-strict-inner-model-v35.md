# SPR7 — CONDITIONAL full physical germ theorem: a STRICT leading-quartic point with ONE explicit nonzero derivative would give genuine unrestricted septic counterexamples

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 09:03:11 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL-SUFFICIENCY BRIDGE CANDIDATE.** This proves the formerly missing finite-epsilon/global-positivity/all-source-Hurwitz bridge under EXPLICIT strict model and Jacobian hypotheses. NO leading model point satisfying them is exhibited. Consequently NO actual counterexample, feasibility or original SPR7 resolution is claimed. The hard remaining prerequisite is the existence of that strict finite model point; the theorem is not allowed to stand in for it.

All-variable exact conventional proof only, including privately. No numeric/control instance, evaluated parameter/sequence member, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FIVE owner findings/parentv37/history permanent; fifth probe/consuming guidance ZERO credit. Qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded these later proofs. Outside v11-v29 snapshot; no frozen-source/gate widening.

## 0. Exact source dependencies and mathematical imports

Use COMPLETE v34 inner model SHA256 `2395569291feb3dde73c8fcc861bc83cad9969177383a1b88a4258f45fd5cf9d`, COMPLETE v33 rescaling SHA256 `6eadd33525db09695cb268102ea3f6056de2d5ff2922d0e8640f6d6a191865e8` and every operative v11/v20/v30/v32 source/erratum named there. The unrestricted-dual conclusion additionally requires FULL B5 `reciprocal-critical-cone-entire-inverse-and-positive-kernel-v5.md`, SHA256 `7a358b729dfff820eb18d8af9bd474e83592979f4a045ea212a09237bda7f70a`, FULL B10 `reciprocal-class-exact-three-word-reduction-v10.md`, SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`, and its mandatory erratum SHA256 `cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`. No headline or old verdict substitutes for reconstruction/application.

Ordinary imports: real analytic implicit-function theorem at a PROVED nonzero Jacobian; local polynomial-root continuity/Rouche root counting on bounded isolating disks (including a degree-dropping coefficient limit), and simple-root analytic continuation; reciprocal root map; ordinary cubic/quartic Hurwitz criteria; minimum principle; polynomial division with a nonzero constant term; openness of strict Hurwitz stability on a COMPACT coefficient box. Specialized source-root, full-frequency and rank/application bridges are supplied below. This is conventional WRITTEN, not a formal proof.

## 1. EXACT unexhibited model hypotheses

Fix real U>0,K>U and define

`V=K/(1+K)`, `p0=U^2/(1+U)`, `q=K^2/(1+K)`,

`h=(K-U)/(1+U)>0`, `r=p0+Uh`, `H=1+h`.

Suppose there exist REAL A,b,beta,tau,s,lambda satisfying EVERY condition below:

- `0<A<h-U`, `0<b<p0`, `beta<A`;
- `Y=h-A^2/beta` is defined and `U<Y<Y_*(b)`, where j=(b-r)^2/(rh),k=b^2/r,Y_*=[j+k+sqrt((j+k)^2+4k)]/2;
- beta>0, `gamma=h beta-A^2>0`, `C=beta+gamma`;
- `zeta=2H-A`, `N=beta+4(H-A)`, `M=N/(1+j)`, `D0=M(2+j+k)`;
- `rho=C-D0>0` (STRICT leading original third width);
- `tau in(1/(1+K),1/(1+U))`, `C tau-beta>0` (STRICT selected inner LEAD);
- `s>0`, `lambda>0`, and the ENTIRE identity

`G4(t)=zeta^2(t-tau)^2[(t-s)^2+lambda t]`,

where

`G4=t(Ct-beta)(-t^2+Jt*t-H)+(M-D0*t+Nt^2)(Ht^2-Jt*t+1)`,

`Jt=r+h+2`;

- the explicit reduced derivative defined next satisfies `Dcal(tau)!=0`.

The factor identity includes its constant M=zeta^2tau^2s^2 and ALL coefficients, not only a selected zero. lambda>0 makes the residual quadratic STRICTLY positive on the entire positive half-line. No actual tuple satisfying these hypotheses is delivered here; no claim that their domain is nonempty is made.

To define the derivative, hold U,K,A,b fixed, put Pj=1/(1+j),Dh=(2+j+k)/(1+j), and vary beta with C=Hbeta-A^2,N=beta+4(H-A),M=N Pj,D0=N Dh. Then

`Dcal(t)=dG4/d beta`

`=t(Ht-1)(-t^2+Jt*t-H)+(t^2-Dh*t+Pj)(Ht^2-Jt*t+1)`.

The apparent degree-four terms cancel; this is an explicit degree-at-most-three polynomial. Its NONZERO value at tau is a stated prerequisite, NOT assumed generically or asserted verified at an unknown point.

## 2. Exact original finite-epsilon parameterization

Set epsilon>0, delta=1/epsilon and the EXACT target

`d=U+1/epsilon`, `e=q+h/epsilon`, `f=Uq+r/epsilon`.

Choose a=A/epsilon,b as fixed, l=L(beta), m=M/epsilon^2, where

`L(beta)=r(hbeta-A^2)/A^2`.

Construct the two ACTUAL pal cubics by the entire v11 inverse and the original interval centers/widths by its diagonal inverse. This is the original monic-degree7/constant1 coefficient system, not a limiting polynomial or a shifted frequency rectangle.

For epsilon>0 all coefficients are explicit rational functions. After the normalizations used below they extend real-analytically to epsilon=0 near the stated tuple: denominators include r+Uq epsilon,1+(U+V)epsilon and fixed positive phase/contact quantities, none zero there. All apparent singular powers are removed by the displayed physical frequency/coefficient scalings.

The four unknown branch coordinates will be beta,M,x,tau, with A,b,U,K fixed. At epsilon=0 the outer contact is x=1/zeta, the inner contact tau is the prescribed one.

## 3. The outer two equations have an AUTOMATIC nonzero Jacobian

Let P4(t;epsilon) be the ACTUAL physical C4 pairing. Define

`Fout(epsilon,beta,M,x)=P4(epsilon*x;epsilon)`.

It extends analytically and at epsilon0 equals

`Qout(x)=(1-M(1+j)x)(1-Hx)+x[alpha+1-(beta+gamma)x]`,

`alpha=beta-2A+h`.

At the model point it is(1-zeta*x)^2. The equations Fout=0,partial_xFout=0 have Jacobian in(M,x) with determinant

`[-(1+j)x(1-Hx)]*[2zeta^2]!=0`,

because0<x=1/zeta<1/H. Thus the analytic IFT gives UNIQUE local functions M(epsilon,beta),x(epsilon,beta). At epsilon0 they are exactly

`M(0,beta)=[beta+4(H-A)]/(1+j)`,

`x(0,beta)=1/zeta`.

No generic root/rank assumption is being imported here.

## 4. The inner two equations require precisely the explicit Dcal prerequisite

Let P2 be the ACTUAL physical C2 pairing and define

`Fin(epsilon,beta,t)=epsilon^2 P2(t;epsilon)`

using the just-constructed outer branch. It extends analytically and at0 equals t G4(t;beta).

At the model inner contact G4=G4'=0, while

`G4''(tau)=2zeta^2[(tau-s)^2+lambda*tau]>0`.

The Jacobian of(Fin,partial_tFin) with respect to(beta,t) has determinant

`tau^2 Dcal(tau) G4''(tau)!=0`.

The IFT therefore supplies beta(epsilon),tau(epsilon), hence M(epsilon),x(epsilon), satisfying BOTH exact double-contact systems for every sufficiently small epsilon. Their initial values are the given model tuple. This is conditional on its nonzero Dcal; no point/nonsingularity has been proved to exist.

## 5. Full ALL-frequency positivity persists — not merely positivity at a finite set

The exact C4 double contact at t=epsilon*x corresponds by ACTUAL reversal to a C2 double contact at

`R_epsilon=1/[epsilon*x(epsilon)]`.

It is distinct from tau(epsilon) for small epsilon. P2 is a monic degree-seven polynomial in physical t with constant1. Exact division yields

`P2=(t-tau_epsilon)^2(t-R_epsilon)^2 Q_epsilon(t)`

with Q_epsilon MONIC cubic and

`Q_epsilon(0)=epsilon^2 x(epsilon)^2/tau_epsilon^2>0`.

Its coefficients extend continuously/analytically to epsilon0. To see this without division by an unbounded root, multiply P2 by epsilon^2x^2 and divide by

`(t-tau_epsilon)^2(epsilon*x*t-1)^2`,

whose constant is tau_epsilon^2>0. Low-coefficient polynomial division gives the cubic coefficients analytically; exact contact divisibility supplies consistency of the higher coefficients. At the limit,

`Q_0(t)=t[(t-s)^2+lambda t]`.

Now lambda>0 makes the bracket positive for EVERY t>=0 and its constant s^2>0. Hence Q_epsilon(t)>0 for ALL t>0 when epsilon is sufficiently small:

- near0, its constant is positive and its linear coefficient tends s^2>0; choose a fixed small symbolic interval so the positive linear term dominates any bounded negative quadratic coefficient;
- on a fixed compact middle interval Q_0 has a strictly positive minimum, preserved by coefficient convergence;
- for large t the monic cubic term dominates the uniformly bounded lower coefficients.

These three ranges cover the ENTIRE positive half-line. This is a full proof, not an inference from a grid or isolated contact continuity.

Thus P2>=0 with ONLY the two stated double roots; C4 is globally nonnegative by reversal. Both pal pairings are globally nonnegative by their exact(v-a)^2(v+l),(v-b)^2(v+m) formulas. Endpoints/frequency1/constants remain the actual original ones. No extra unweighted positive zero has been omitted; Q_epsilon is strictly positive.

## 6. ALL original source corners and the WHOLE independent box are strictly Hurwitz

### 6.1 Actual widths and pal corners

The three paired widths have leading positive coefficients

`2epsilon*w1 ->M>0`,

`2epsilon*w2 ->N-beta=4(H-A)>0`,

`2epsilon*w3 ->rho>0`.

Hence all original intervals are nondegenerate for small positive epsilon. beta<A means

`L(beta)<r(h-A)/A`,

the strict limit of the original C1 lag-height ceiling, so the finite C1 corner stays strictly below that ceiling and is strictly Hurwitz/lagging by the full pal amplitude theorem. Fixed b>0 and m>0 make C3 strictly Hurwitz/lagging. No m0/pal-wall limit is called admitted.

### 6.2 The nonpal source has four bounded, one slow and two FAST strict-left roots

The reduced quartic

`ared=N s^4+C s^3+D0 s^2+beta s+M`

is STRICTLY HURWITZ: its coefficients are positive and its third Hurwitz determinant equals

`M beta^2[(j+k)Y+k-Y^2]>0`

by Y<Y_*. The second determinant is then positive because beta*Delta2=Delta3+C^2M>0; the other quartic conditions follow.

For the exact finite source a2,

`epsilon*a2(s;epsilon) ->s*ared(s)`

coefficientwise. Four roots stay near the strict quartic roots. The simple root at0 continues as

`s_slow(epsilon)=-epsilon/M+O(epsilon^2)<0`.

For the remaining pair put eta=sqrt(epsilon),z=eta*s. The exact coefficient expansions give

`eta^7 a2(z/eta;eta^2)`

`=z^5(z^2+N)+eta*z^4[(alpha+1)z^2+C]+O(eta^2)`.

The two nonzero leading roots z0=+/-i sqrt(N) are simple. Their analytic first corrections are

`z1=-[(alpha+1)N-C]/(2N)`.

The outer identity gives

`(alpha+1)N-C=(N-zeta)^2>0`.

Indeed leading width rho>0 gives zeta^2<NR(b), with R(b)<h<zeta, so N>zeta. Therefore both fast roots have real part tending the STRICT negative number z1 after dividing z=z0+eta*z1+O(eta^2) by eta. All seven source roots are left for sufficiently small positive epsilon. This is an exact analytic perturbation proof, not a numerical root plot or an assumption that a degree-dropped limit preserves stability.

C4 is the exact reversal of C2 and hence also strict.

### 6.3 Whole ORIGINAL box, without assuming corner stability is sufficient by itself

Every original member has globally weak nonnegative ratio a/B because its pairing is affine in independent coefficients and all four minimizing actual corner pairings are nonnegative. The minimum principle excludes right-half-plane member roots. Any member imaginary root would give a zero minimizing corner; actual positive parity variation excludes target-component-wall zeros by the derivative argument, and elsewhere the unique minimizing actual corner would share that source zero. All four corners were just proved strict, impossible. Monic degree7/constant1 prevent degree/origin escape for any member. Thus EVERY denominator of the ORIGINAL independent box is strictly Hurwitz.

## 7. Actual word, unrestricted dual and exact conditional conclusion

The contacts stay in their correct actual target cells. For C1, a=A/epsilon has q<a<e and the strict lag height side; b remains in(0,p0). The inner contact tau stays inside(y1,x2) and Ctau-beta>0 keeps its actual C2 LEAD sign. The outer contact epsilon*x stays below actual x1 because x0=1/zeta<1/H; its source even value tends1-N/zeta<0, hence it remains C4 LEADING. All selected sources are nonzero by strict source stability.

There are therefore four distinct actual reciprocal contact orbits with physical word

`C4 lead, C1 lag, C2 lead, C3 lag`.

Only NOW, AFTER full original Hurwitz/all-zero admission, invoke the FULL B5/B10 rank-three positive-kernel and reciprocal lift. It gives an actual positive annihilation of ALL eight unrestricted real numerator coefficients. A single unrestricted strict-SPR numerator would make every positive weighted contact term strictly positive, contradiction.

**Conditional theorem proved:** For EVERY real model tuple satisfying EVERY strict hypothesis and Dcal(tau)!=0 in Section1, there exists epsilon0>0 such that EVERY0<epsilon<epsilon0 on the analytic branch supplies a genuine original-class monic septic robustly Hurwitz interval box with NO unrestricted common exact-degree7 SPR numerator. Its six paired widths are positive; ALL SEVEN widths can also be made positive by the exact containment argument below.

For each resulting fixed epsilon-box, the original denominator coefficient rectangle is COMPACT and every member is strictly Hurwitz. Continuity of roots and a finite neighborhood subcover therefore give a positive constant-coefficient enlargement margin. Choose a real eta>0 small enough, with eta<1, and independently enlarge the formerly fixed constant1 to[1-eta,1+eta]. Every denominator in this new full SEVEN-dimensional coefficient rectangle remains strictly Hurwitz. All six old intervals already have positive width, and the seventh now does too.

The enlarged box contains the entire original negative box, so a common unrestricted SPR numerator for it would also work for the old box, impossible. Thus the conditional construction can deliver an actual original independent box with ALL SEVEN positive coefficient widths; its final enlarged input need not stay reciprocal. No rational eta or numerical enlargement is claimed, and no existence is asserted without the unexhibited strict model prerequisite.

**What is NOT proved:** there exists EVEN ONE such leading model tuple. Its coefficient identities, strict widths/quarter-root strip/inner LEAD and nonzero Dcal are an unexhibited finite real prerequisite. No actual family, original counterexample or universal failure follows UNTIL that prerequisite is established and the whole union/application is freshly reviewed. No rational tuple, executable finite certificate or novelty clearance is provided.

## 8. Residual and assurance

The finite-epsilon/whole-frequency/source-Hurwitz/positive-dual bridge is now supplied CONDITIONALLY rather than left as an unmentioned IFT slogan. The real remaining problem is the existence or impossibility of the strict leading finite quartic model and explicit derivative hypothesis, plus the other finite target slabs/WI/WII alternatives. No weaker target problem replaces the original question.

WRITTEN only; no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty/parent acceptance, no actual tuple/feasibility/global empty/attainment/round closeout. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30mincadence; no GO/early park/source cutover, primary active.
