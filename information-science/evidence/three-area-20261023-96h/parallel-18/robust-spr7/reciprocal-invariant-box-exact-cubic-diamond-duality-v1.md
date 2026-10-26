# SPR7 — exact reciprocal symmetrization,three diamond uncertainties and a compact four-dimensional dual

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 17:25:34 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN representation candidate**,not yet reviewed/adopted. It is a realization/front-end representation for the SAME original unrestricted degree7 problem,not another profile-only obstruction. No actual bad box or finite witness is supplied.

The later second PRIVATE WRITTEN approximate-binomial scout was wholly withdrawn in `owner-written-exact-arithmetic-erratum-v2.json`,SHA256 `d712cd64a2a2e77628a466e6be524f868131827f37b7a767ed92bf9b9e446301`,actual17:17:28. This paper is a NEW exact symbolic derivation independent of that ZERO-credit scout;no trial magnitudes or feasibility inference are consumed. Earlier findings/HOLD/v9/v10/v11 and October27 cutoff/deadline remain. No calculator/interpreter/eval/program/CAS/LP/enumeration,optimizer,replay or solver was used.

## 0. Scope: a genuine input subclass,NOT a target-profile restriction

Consider ORIGINAL independent monic septic boxes with A7=1 and,for i=1,2,3,the TWO independent coefficients A_i,A_(7-i) in the SAME interval[ell_i,u_i]. Assume every original member is strictly Hurwitz. This is an explicitly stated INPUT subclass;it is not silently imposed on an arbitrary box.

Within this class,existence of ANY unrestricted common real exact-degree7 SPR numerator is EXACTLY equivalent to a four-coefficient cubic T passing the explicit compact convex positivity system below. Positive scale removes one target degree of freedom. This reduction loses NO numerator by a profile assumption:reciprocal averaging proves the existence equivalence.

The exact dual alternative is a positive annihilation using at most FIVE compact constraint vectors,each liftable to at most TWO ACTUAL original frequency/corner atoms. It is an existential theorem,not a constructed/admitted finite certificate;no rational frequency/weight existence is inferred. If a genuine negative base box is later constructed,compact Hurwitz openness extends it to a box with ALL SEVEN positive widths.

Neither the pending163LF direct-DEFECT v4 nor the218LF boundary/sharpness v3,other new Hermite/Pick sources,old profile computations or external reviews are correctness inputs here. Classical inputs are elementary polynomial expansion/real reciprocity,strict SPR linearity,the previously reconstructed monic-Hurwitz homotopy,compact strict separation and Caratheodory in R4;their application is given explicitly.

## 1. Exact reciprocal averaging of EVERY successful numerator

Write `Ra(s)=s^7 a(1/s)`. Because A7=1 and paired intervals coincide,R maps K BIJECTIVELY to K. If B is ANY real exact-degree7 common SPR numerator,its leading coefficient and B(0) are positive. Then RB has the same positivity at its constant/leading endpoints. For omega>0,

`(RB)(i*omega)/a(i*omega)`

`=conjugate[B(i/omega)/(Ra)(i/omega)]`.

It has positive real part because Ra is an ORIGINAL member. Thus RB is also common SPR,including frequency0 and the positive infinity limit. By linearity,Bpal=(B+RB)/2 is common SPR,palindromic,RBpal=Bpal,and STILL exact degree7 with positive leading coefficient.

Conversely every palindromic common numerator is an unrestricted one. Hence arbitrary common-numerator existence is equivalent to palindromic existence. No assumption that a itself is palindromic is made:its SIX original coefficients vary independently.

Every palindromic degree<=7 B has a UNIQUE representation

`B(s)=(s+1)s^3 T(z)`, `z=s+s^-1`,

`T(z)=tau3*z^3+tau2*z^2+tau1*z+tau0`.

It has exact degree7 AND positive leading coefficient precisely when tau3>0;its constant coefficient is the SAME tau3. Positive scaling then makes tau3=1,leaving THREE free target coefficients. In this EXACT-degree case,B Hurwitz iff T Hurwitz:each root z0 gives quadratic roots s,1/s,and `Re(z0)=Re(s)*(1+|s|^-2)`;the extra root is-1. This equivalence is NOT asserted at tau3=0,where a degree drop introduces zero/infinity defects. Common SPR already forces Hurwitz by the monic segment argument,so this is not an extra ansatz or an unproved numerical filter.

## 2. Preserve all original coefficient independence as THREE diamonds

Put

`M_i=(A_i+A_(7-i))/2`, `D_i=(A_i-A_(7-i))/2`,

`m_i=(ell_i+u_i)/2`, `w_i=(u_i-ell_i)/2`.

The original two interval constraints are EXACTLY

`|M_i-m_i|+|D_i|<=w_i`,for each i.                         (DIAMOND)

Indeed the inverse coefficients are M_i+D_i,M_i-D_i,and max(|x+y|,|x-y|)=|x|+|y|. The three diamonds remain independent;P and Q below do NOT become independent coefficient rectangles.

Direct coefficient expansion gives

`a(s)=(s+1)s^3 P(z)+(s-1)s^3 Q(z)`,

`P=z^3+(M1-1)z^2+(M2-M1-2)z+(M3-M1-M2+1)`,

`Q=D1*z^2+(D1+D2)z+(D3-D1+D2)`.

For an explicit check,the Q basis contributions `(s-1)s^3 z^2`, `(s-1)s^3 z`, `(s-1)s^3` have coefficient rows respectively `(1,-1,2,-2,1,-1)`, `(0,1,-1,1,-1,0)`, `(0,0,1,-1,0,0)` at s6,...,s1. Substitution gives `(D1,D2,D3,-D3,-D2,-D1)`. The P expansion supplies the matching averaged coefficients M1,M2,M3,M3,M2,M1 and the endpoint1s. This is symbolic integer algebra,not machine verification.

Let `Pmid=z^3+pi2*z^2+pi1*z+pi0`,where

`pi2=m1-1`, `pi1=m2-m1-2`, `pi0=m3-m1-m2+1`.

Its M partials are `A=(z²-z-1,z-1,1)`;Q's D partials are `C=(z²+z-1,z+1,1)`.

## 3. Exact affine support and no lost frequency endpoints

For omega>0 set `z=i*u`, `u=omega-1/omega`, `r=(i*omega-1)/(i*omega+1)`. Then

`B/a=T(z)/(P(z)+rQ(z))`.

The denominator is nonzero because the ORIGINAL a is Hurwitz. Strict positivity is equivalent to

`Phi=Re[T(z)*conjugate(P(z)+rQ(z))]>0`.

Define `Phi0=Re[T*conjugate(Pmid)]`, `alpha_i=Re[T*conjugate(A_i)]`, `beta_i=Re[T*conjugate(r*C_i)]`. DIAMOND's exact affine support gives

`min_(a in K) Phi=Phi0-sum_i w_i*max(|alpha_i|,|beta_i|)`.    (SUPPORT)

Each maximizing diamond vertex corresponds to an ACTUAL original coefficient corner;no enlarged reciprocal box or free-root tuple is used. This is simply the duality of a real two-dimensional l1 ball and l-infinity support,derived independently for each actual pair.

Reciprocity permits restricting omega to(0,1]:for palindromic B,the condition for a at1/omega is conjugate to that for Ra at omega,and Ra ranges through exactly K. Frequency0/infinity are covered directly by B(0)=leading(B)=tau3>0,not by dividing the Laurent formula at s0.

## 4. Rational compact parameter and explicit degree<=7 scalar polynomials

Set `t=omega²`, `xi=(1-t)/(1+t)` on0<t<=1,so0<=xi<1,and `delta=1-xi²`. Also

`v=u²=4xi²/delta`, `u/(omega+1/omega)=-xi`.

Write `X=tau0-tau2*v`, `W=tau1-tau3*v`,so T(iu)=X+i*u*W. Exact multiplication gives

`Phi0(v)=X*(pi0-pi2*v)+v*W*(pi1-v)`,

`alpha1=-(v+1)X-vW`, `alpha2=-X+vW`, `alpha3=X`,

`beta_i=-xi*G_i(v)`,where

`G1=-(v+3)X-(v+2)W`, `G2=-X+(v+2)W`, `G3=X+2W`.

For clarity,beta follows from `conjugate(r)=(u-2i)/(omega+1/omega)`;multiplication by conjugate(C_i) gives the displayed real parts. No square-root approximation or numeric angle is used.

Define the polynomial extensions

`Fhat(xi)=delta^3*Phi0(4xi²/delta)`,

`Ahat_i(xi)=delta^3*alpha_i(4xi²/delta)`,

`Bhat_i(xi)=xi*delta^3*G_i(4xi²/delta)`.

Fhat,Ahat are even polynomials of degree<=6;Bhat odd polynomials of degree<=7. Every coefficient is LINEAR in the four taus. The apparent delta denominators cancel because Phi0 has degree<=3 in v and alpha_i,G_i degree<=2. At xi1,

`Fhat(1)=64*tau3`, `Ahat_i(1)=Bhat_i(1)=0`.

Thus unrestricted common-SPR existence in this INPUT class is EXACTLY feasibility of

`Fhat(xi)>sum_i w_i*max(|Ahat_i(xi)|,|Bhat_i(xi)|)`

`for EVERY xi in[0,1]`.                                   (COMPACT)

The xi1 constraint forces tau3>0,so no separate fictitious degree drop is admitted. These are strict inequalities defining a CONVEX target set,not a claim of strict convexity or uniqueness. After tau3=1 they involve only three real variables.

## 5. Complete compact positive-cone alternative and its actual lift

For each xi in[0,1],choose independently for each pair one of Ahat_i,Bhat_i and a sign sigma_i in{+1,-1}. The scalar polynomial

`Fhat-sum_i w_i*sigma_i*Z_i`

is linear in tau=(tau3,tau2,tau1,tau0);call its coefficient vector V. COMPACT is equivalent to V dot tau>0 for ALL such choices/xi. Their set S in R4 is compact:it is a finite union of continuous polynomial images of[0,1].

If0 is NOT in conv(S),the closest point V0 of the compact convex hull to0 satisfies V dot V0>=||V0||²>0 for every V in S. Thus tau=V0 is a strict common target. If0 IS in conv(S),no tau can be positive on all S. By Caratheodory in R4,that alternative has an annihilation

`sum_(j=1..m) lambda_j V_j=0`, `lambda_j>=0`,

`sum lambda_j=1`, `m<=5`.                                  (DUAL)

This is a theoretical finite bound,NOT a supplied witness. Neither rational xi_j nor rational lambda_j is guaranteed by this abstract argument.

Each chosen diamond/sign branch is an ACTUAL corner a_j. For t=(1-xi)/(1+xi)>0,its scalar functional is EXACTLY

`64/(1+t)^7 * P_(a_j,B)(t)` on palindromic B.

Indeed `P_(a,B)(t)=(1+t)t³*Phi`,while `delta=4t/(1+t)²`. To lift DUAL to arbitrary B,apply each evaluation to `(B+RB)/2`. Real reciprocity gives

`P_(a,RB)(t)=t^7*P_(Ra,B)(1/t)`.

Hence the lifted functional is a POSITIVE multiple of the TWO ACTUAL atoms

`P_(a,B)(t)` and `t^7*P_(Ra,B)(1/t)`.

At xi1,t0,the functional is64 times the palindromic constant/leading tau3;its lift is `32*(B(0)+leading(B))`,the genuine positive0/infinity endpoint pair for this actual input. Thus DUAL annihilates ALL eight arbitrary target coefficients after lifting,and contradicts a strict unrestricted common numerator. At most five reciprocal constraint orbits,each at most two atoms,suffice here;no minimality or executed finite verification is claimed.

## 6. Why this can address ALL SEVEN widths,without claiming an example

Suppose a specific reciprocal base box with six positive coefficient widths is later PROVED robustly Hurwitz and common-SPR-infeasible. Compactness of that base box inside the OPEN Hurwitz set gives a uniform coefficient neighborhood remaining Hurwitz. Enlarging only A7 from1 to[1-epsilon,1+epsilon] for sufficiently small positive rational epsilon therefore gives an ORIGINAL independent box with ALL SEVEN positive widths,still robustly Hurwitz. It contains the base family,so no common numerator can appear by enlargement.

This is conditional monotonicity/openness,not an evaluated epsilon or a constructed box. Conversely,a positive synthesis theorem confined to this symmetric input class would NOT settle the arbitrary original interval box. The reduction is a legitimate negative-realization route precisely because it loses no target within that input class.

## 7. Exact remaining gap and assurance

One still needs ACTUAL rational interval endpoints satisfying full robust Hurwitz plus an explicit exact DUAL,OR a proof COMPACT always feasible for such original inputs. No box,taus,frequencies,weights,mutation/replay certificate or feasibility conclusion has been selected. The withdrawn approximate scout supplies NONE of them.

This complete exact reciprocal/cubic/diamond/compact-dual representation is a separate NEW WRITTEN candidate,not accepted by the pending direct-DEFECT v4 gate or any earlier even-profile/root-transport verdict. No formal/kernel/human/configured-family/executable/triple-finite/novelty gate is conferred. No native science/GO,calculator/CAS/program/LP/solver/replay,CLI/nested agents,source/shared edits,publication/Git/deletion/config changes or deadline reset occurred. Same original primary continues at an actual input/Hurwitz/finite-dual realization or general global-attainment gap.
