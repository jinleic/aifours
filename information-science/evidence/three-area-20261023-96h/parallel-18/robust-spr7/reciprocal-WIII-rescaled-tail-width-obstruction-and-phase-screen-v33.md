# SPR7 — the ENTIRE rescaled large-target WIII regime has a width obstruction: h>8 and new phase inequalities are NECESSARY for an unbounded tail

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 08:40:27 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN NECESSARY-TAIL/PARTIAL-BOUNDEDNESS CANDIDATE.** This analyzes the actual uncontrolled unbounded-a regime instead of assuming a bounded contact. For every fixed phase shape with h<=8 it proves an upper bound on delta exists; it also supplies a stronger explicit necessary phase inequality and limiting contact window. The bound here is NONCONSTRUCTIVE through a fully bounded rescaled-sequence contradiction, not a numerical cutoff or full physical attainment theorem.

All-variable exact conventional proof only, including privately. No parameter/control instance, selected sequence member, numeric trial, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. The hypothetical sequences below are universally quantified mathematical objects in a contradiction proof, not evaluated parameter scouts. All FIVE owner findings/parentv37/history permanent; fifth probe/consuming guidance ZERO credit. Qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded these later proofs. Outside the v11-v29 snapshot; no freeze widening.

## 0. Exact dependencies and hypotheses

Required ENTIRE sources: qualified supported v11 SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8` for actual source reconstruction/word/widths; new v20 SHA256 `530f87473ec31f592bc7b7ac46a9caf1b7292c1a1790314cca8d056506ae6fb7` for the real phase bijection; COMPLETE v30 SHA256 `b9401c9b459adf453d979f1dd264987ef636b6f7acf0a4d81a9dd419c2b46914` for k(a)>U; COMPLETE v32 SHA256 `2d6fdb4def333de1b26aaaa48145c92e465f842e46c9652e02e8b5724ff1292b` for ALL-phase height/coefficient/linear-contact bounds. No old verdict or hash substitutes for reconstruction. Ordinary compactness of bounded real sequences and continuous rational/polynomial limits are used with ALL bounds proved and degenerate limit faces retained.

Fix ANY phase shape U>0,U/(1+U)<V<1, and write

`K=V/(1-V)>U`, `p0=U^2/(1+U)`, `q=K^2/(1+K)`,

`h=(K-U)/(1+U)>0`, `r=p0+Uh=UK/(1+U)`, `H=1+h`.

Targets are d=U+delta,e=q+h delta,f=Uq+r delta,D=delta(d+V)h. All points considered are ACTUAL admitted WIII points, including every global pairing/source/width/contact guard, not arbitrary positive scalar factors.

## 1. Exact PHYSICAL target-component roots are rational in this chart

V20 gives rho1=p0,rho2=q. Their physical below-one branches are

`x2=1/(1+U)`, `y1=1/(1+K)`.

Reciprocity gives y2=1+U,x3=1+K. Since E_B has leading coefficient-(d+1) and constant1, its remaining root is

`x1=1/[H(d+1)]`,

and y3=H(d+1). Thus the ENTIRE actual components factor EXACTLY as

`E_B(t)=[1-H(d+1)t][1-(1+U)t][1-t/(1+K)]`,

`O_B(t)=(d+1)[1-(1+K)t][1-t/(1+U)][1-t/(H(d+1))]`.

Their strict order follows from d>U and K>U. These are TARGET component-wall formulas only: an ARBITRARY contact frequency t(v) still has its square-root inverse, so this does not retroactively claim v20 rationalized every physical contact.

In particular

`delta*x1=1/[H(1+(U+1)/delta)] ->1/H`

as delta grows, an exact identity with no root approximation or trial.

## 2. Assume an unbounded actual tail; ALL rescaled variables lie in explicit bounded sets

Suppose for contradiction that there are admitted WIII points at arbitrarily large delta for this FIXED shape. Choose an abstract sequence delta_n increasing without bound; NO member is instantiated or evaluated.

Use v32's proved finite phase constants c>0,L_phase,M_phase,Q0,Q1. After discarding only finitely many initial indices its bounds give

`a_n>c delta_n`, `a_n<q+h delta_n`,

`l_n<=delta_n L_phase/a_n`,

`m_n<=delta_n M_phase a_n`,

`0<Ai_n<=Q0+Q1 a_n` for ALL original source coefficients.

Define

`A_n=a_n/delta_n`, `L_n=l_n`, `M_n=m_n/delta_n^2`,

`b_n` as before, and `x_n=delta_n*t_outer,n` for the selected outer-C4 contact.

Then A_n is bounded below by c and above by h+q; L_n<=L_phase/c; M_n<=M_phase(h+q);0<b_n<p0. The actual outer contact has E_C4<0. The source coefficient bound forces

`t_outer,n>1/[4(Q0+Q1a_n)]`,

so

`x_n>1/[4(Q0+Q1(h+q))]>0`.

It also satisfies x_n<delta_n*x1,n, bounded above by1/H. Thus ALL FIVE rescaled coordinates have bounded subsequences, with positive lower bounds on A_n,x_n. No b lower bound, pal amplitude lower bound, individual width lower bound or strict limiting input is assumed.

Take a common convergent subsequence, denoting limits A,L,M,b,x. Then A>0,0<=b<=p0,L,M>=0 and0<x<=1/H. Passing the exact guard k(a)>U to leading scaled products gives

`A<=h-U`.

Thus existence of such a sequence already forces h>U. The lag height ceiling gives

`L<=r(h-A)/A`.

Every denominator here has a strictly positive proved limit, so these limit operations are ordinary continuous rational limits, not informal dominant balances.

## 3. Complete leading source coefficients on this bounded subsequence

Put

`gamma=A^2L/r>=0`,

`beta=(A^2+gamma)/h>0`,

`alpha=[(A-h)^2+gamma]/h=beta-2A+h`.

The exact pal inverse, after multiplying the stated coefficients by powers of delta, gives

C1: `A_U1 ->alpha`, `B_U1/delta ->beta`, `C_U1/delta ->gamma`.

For clarity this follows by a=a_n=delta_n A_n, f_n/delta_n->r, D_n/delta_n^2->h, and

`C_a/delta_n^2 ->A^2/r`, `X_a/delta_n^2 ->A`.

The two numerator terms for A_U1 have limits (A-h)^2 and LA^2/r; those for B_U1/delta have limits A^2 and LA^2/r. No floating asymptotics are used.

The lag height bound gives gamma<=A(h-A), hence

`beta<=A`. (BETABOUND)

Define

`j=(b-r)^2/(rh)>=0`, `k=b^2/r>=0`.

For C3 the ENTIRE corresponding scaled limits are

`A_U3/delta ->M`,

`B_U3/delta ->Mj`, `C_U3/delta ->Mk`.

They follow directly from C_b/delta->h and X_b/delta->b-r with m_n/delta_n^2->M. b=0 or p0 is retained, and no assertion that these limiting source polynomials are actual admitted original denominators is made.

## 4. The ENTIRE outer double-contact limit is forced, not guessed

For the actual C4 mixture at t=z/delta_n, the even/odd source components converge coefficientwise on bounded z to

`E_C4 ->1-M(1+j)z`,

`O_C4 ->alpha+1-(beta+gamma)z`.

The target satisfies E_B->1-Hz and t O_B->z. Therefore the physical C4 pairing and its derivative with respect to z converge to the quadratic

`Qout(z)=[1-Nz][1-Hz]+z[alpha+1-(beta+gamma)z]`,

`N=M(1+j)`.

Each actual selected outer contact satisfies pairing0 and its frequency derivative0. Hence

`Qout(x)=Qout'(x)=0`.

Since coefficient convergence is on a FIXED finite-degree polynomial, derivative convergence is automatic and no unproved exchange of a continuum limit/minimum is being used.

The possible upper endpoint is excluded EXACTLY:

`Qout(1/H)=[(alpha+1)H-(beta+gamma)]/H^2`

`=(A-H)^2/H^2>0`,

because A<=h-U<H. Thus0<x<1/H. Constant Qout(0)=1 excludes a degree-drop double-zero artifact. Consequently

`Qout(z)=(1-zeta z)^2`, `zeta=1/x>H`.

Coefficient comparison gives

`N=alpha-h+2zeta=beta-2A+2zeta`,

`zeta^2=NH-(beta+gamma)`.

Using beta h-gamma=A^2 yields

`(zeta-H)^2=(A-H)^2`.

A<H and zeta>H select the UNIQUE permitted branch

`zeta=2H-A`,

`N=beta+4(H-A)>0`. (OUTERFORCED)

Thus M=N/(1+j)>0 is inferred; it was not smuggled in as a strict limiting height hypothesis. The other algebraic branch zeta=A would lie OUTSIDE the actual outer cell and is excluded by the actual phase filter.

## 5. Positive original width w3 gives a STRICT quadratic obstruction

The original width is2w3=actual C1 middle coefficient minus actual C3 middle coefficient. From the limits just proved,

`lim 2w3,n/delta_n=beta+gamma-M(2+j+k)>=0`.

Only NONNEGATIVITY is inferred from strict finite widths. The leading width is permitted to vanish; it is not falsely assumed positive.

Use(OUTERFORCED) to obtain

`zeta^2<=N R(b)`,

`R(b)=(h+r-1-2b)/(1+j)`.

The identity hj-k=r-2b gives

`R(b)=h-(1+k)/(1+j)<h`.

Since zeta^2>0 and N>0, R(b)>0. Together with beta<=A,

`zeta^2<=NR(b)<Nh<=h[4H-3A]`.

The STRICT middle inequality persists even when b=0, L is on its wall or the leading width vanishes; its gap is positive at every finite fixed phase and0<=b<=p0.

Therefore EVERY unbounded admitted WIII tail would require

`F_h(A)=A^2-(h+4)A+4(h+1)<0`. (WIDTHOBSTRUCTION)

The discriminant is EXACTLY h(h-8). Thus:

- If0<h<=8, F_h is nonnegative for EVERY real A; at h=8 it is(A-6)^2. Contradiction in ALL cases.
- If h>8, the limit must satisfy

`A_-(h)<A<A_+(h)`,

`A_+/-=(h+4 +/-sqrt(h(h-8)))/2`.

In particular A_->4, since (h-4)^2-h(h-8)=16 and h-4>0. Along with A<=h-U, a necessary phase condition is

`h-U>A_-(h)>4`.

No equality branch is silently included here; the derived inequality is STRICT.

## 6. A sharper explicit necessary phase inequality, with equality LIMIT faces retained

For b in[0,p0], let

`D_b=(1+k)/(1+j)=h(r+b^2)/[rh+(r-b)^2]`.

Its derivative has sign of

`g(b)=r+b(h+r-1)-b^2`.

This concave quadratic is positive at both endpoints:

`g(0)=r>0`,

`g(p0)=h[U(1+p0)+p0]>0`.

Hence D_b increases strictly, R(b)=h-D_b decreases, and

`R(b)<=R0=h-h/(h+r)`.

The leading width condition and beta<=A consequently imply

`(2H-A)^2<=R0(4H-3A)`.

Here R0>0 is necessary. The discriminant of this last quadratic in A is R0(9R0-8H). Thus an unbounded tail NECESSARILY satisfies

`9R0>=8H`, equivalently

`Psi=h^2+hr-17h-8r>=0`. (PHASESCREEN)

This is NONSTRICT: at equality the limit may simultaneously have b=0, pal-height wall and leading-width collapse. Those degeneracies were allowed by the compactness hypotheses; no exclusion of this equality case is claimed. The earlier strict(WIDTHOBSTRUCTION) remains valid because R(b)<h even there.

## 7. Exact boundedness conclusions — NOT global attainment or a numerical cutoff

For EVERY FIXED real phase shape, if admitted WIII points had unbounded delta, all the necessary conditions just proved would hold:

`h>U`, `h>8`, `Psi>=0`, `h-U>A_-(h)`,

and a common rescaled limit A would satisfy BOTH quadratic width inequalities with the exact forced outer branch.

Therefore for every fixed phase shape violating ANY of these necessary conditions, the set of deltas of actual admitted WIII points is BOUNDED ABOVE. In particular:

- ALL shapes0<h<=8 have some finite upper delta bound, with h=8 INCLUDED.
- ALL shapes with h-U<=4 have some finite upper delta bound.
- More generally Psi<0 or, for h>8, h-U<=A_-(h), gives the same conclusion.

This bound is NONCONSTRUCTIVE in this packet: boundedness follows from the fully justified no-unbounded-sequence contradiction. It is not an explicit computed cutoff. It is also NOT attainment of the remaining physical parameter space, not a statement that its closure is admissible, and not a strict-source point obtained from a formal limit. V31/v32's explicit bounds remain separately valid where applicable and need not be numerically dominated by this argument.

The remaining large-delta regime is thus narrower: h>8 and a genuine anisotropic a/delta contact window, the phase(PHASESCREEN) and cap h-U>A_- must all survive. Those necessary conditions do not establish a family or feasibility. The full inner/global/source/width equations still have to be solved or contradicted.

## 8. Residual and assurance

This is new actual source/target rescaling, exact physical component factorization, a forced outer-contact square, and an original-width obstruction that rules out whole far-target phase regimes. It does not repeat a fixed-T bound or use an arbitrary band/profile as an original box. All zero-width/pal/phase-wall limit possibilities were retained until an explicit algebraic contradiction removed particular ones.

Still OPEN: the remaining finite target slabs, the surviving unbounded-target phase region, WI/WII_strict, distinct source/pal/width/target faces and original universal nonreciprocal SPR7. No actual tuple, feasibility, full WIII/global emptiness, global attainment, strict perturbation, executable certificate or novelty. WRITTEN only; no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/parent acceptance. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30mincadence; no GO/early park/source cutover/round closeout, primary active.
