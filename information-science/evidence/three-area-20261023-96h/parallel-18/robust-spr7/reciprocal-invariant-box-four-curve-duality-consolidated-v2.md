# SPR7 — reciprocal input boxes: unrestricted synthesis is a four-curve cubic cone; any obstruction needs at least three frequencies

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 17:35:39 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL representation**,not a constructed counterexample or accepted theorem. Exact symbolic polynomial/rational/convex geometry only;no scientific calculator/interpreter/eval/program/CAS/LP/enumeration/optimizer/replay or solver.

This is ONE consolidation of the complete163LF reciprocal-v1 representation (SHA256 `1b970fbba16ce4563ee4e6b959c9b5ce99f33c6e55aee0de6eb96b099f03f11d`) with a stronger FOUR-Kharitonov-curve formulation and the NEW rigorous at-least-THREE-frequency barrier. The old bytes stay immutable. No pending direct-DEFECT/Pick/Hermite theorem is needed. The two permanent PRIVATE WRITTEN approximate-probe findings,including v2 SHA256 `d712cd64a2a2e77628a466e6be524f868131827f37b7a767ed92bf9b9e446301`,retain ZERO credit;this derivation consumes none. All earlier histories/HOLD/v9/v10/v11 and cutoff/deadline remain.

## 0. Exact input subclass and what is NOT claimed

K is the ORIGINAL independent monic septic coefficient box with A7=1 and A_i,A_(7-i) independently in the SAME[ell_i,u_i] for i1,2,3. ALL original members are assumed strictly Hurwitz. The six coefficients are NOT individually constrained to be palindromic. This is an explicit INPUT subclass,not a silent universal reduction.

Within it,ANY unrestricted exact-degree7 common-SPR numerator exists IFF the four-curve compact cubic cone below is strictly feasible. If infeasible,it has a positive annihilation on at most FIVE reciprocal constraint orbits;ANY such annihilation requires at least THREE DISTINCT compact frequency values. No particular inputs,frequencies,weights,positive numerator or finite certificate are supplied. A genuine negative base could be enlarged to ALL SEVEN positive widths,but no base has been constructed.

## 1. Exact unrestricted-target symmetrization and cubic coordinates

Define `Ra(s)=s^7 a(1/s)`. The paired intervals and A7=1 give RK=K. For any common target B,its leading coefficient and B(0) are positive by the large-frequency limit and frequency0. For omega>0,

`(RB)(i*omega)/a(i*omega)=conjugate[B(i/omega)/(Ra)(i/omega)]`.

Thus RB is also common SPR,with positive0/infinity endpoints. The real palindromic average `(B+RB)/2` is common and remains exact degree7. Conversely a palindromic solution is unrestricted. THIS is why no target is lost;it is not another unproved profile-union ansatz.

Every palindromic degree<=7 B has unique coordinates

`B=(s+1)s^3 T(z)`, `z=s+s^-1`,

`T=tau3*z^3+tau2*z^2+tau1*z+tau0`.

Exact degree7 AND positive leading coefficient mean tau3>0;its constant equals tau3. Positive scaling sets tau3=1,leaving three variables. In that exact-degree case,B Hurwitz iff T Hurwitz:for every root z0,the quadratic roots s,1/s have the same real-part sign,and `Re z0=Re s*(1+|s|^-2)`;the extra root is-1. This equivalence is NOT claimed at a degree drop.

## 2. Preserve original uncertainties,then reuse the actual four-corner pattern

Put `m_i=(ell_i+u_i)/2`,`w_i=(u_i-ell_i)/2`;let M_i,D_i be the mean/half-difference of A_i,A_(7-i). Their EXACT independent domains are

`|M_i-m_i|+|D_i|<=w_i`.

They are three coupled diamonds,NOT free P/Q rectangles. Direct polynomial expansion is

`a=(s+1)s^3 P(z)+(s-1)s^3 Q(z)`,

`P=z³+(M1-1)z²+(M2-M1-2)z+(M3-M1-M2+1)`,

`Q=D1*z²+(D1+D2)z+(D3-D1+D2)`.

For example,the Q basis coefficient rows at s6,...,s1 are `(1,-1,2,-2,1,-1)`,`(0,1,-1,1,-1,0)`,`(0,0,1,-1,0,0)`;substitution gives D1,D2,D3,-D3,-D2,-D1 exactly. No scientific arithmetic program checked this.

Let `Pmid=z³+pi2*z²+pi1*z+pi0`,with `pi2=m1-1`,`pi1=m2-m1-2`,`pi0=m3-m1-m2+1`,and define the SINGLE width polynomial

`J(z)=w1*z²+(w2-w1)z-(w1+w2+w3)`.

At each positive frequency,original independent parity-block values fill the actual E/O rectangle;its vertices are EXACTLY C1=(Eplus,Ominus),C2=(Eplus,Oplus),C3=(Eminus,Oplus),C4=(Eminus,Ominus). This is the same existing original-box convention,not a second corner convention.

For this reciprocal INPUT,these actual corner polynomials have `(P,Q)` data

`C1:(Pmid-J,0)`, `C3:(Pmid+J,0)`,

`C2:(Pmid,-J(-z))`, `C4:(Pmid,+J(-z))`.

Indeed C1 uses M=(ell1,ell2,u3),C3=(u1,u2,ell3);C2 has M=m,D=(-w1,+w2,+w3),and C4 opposite D. Thus C1,C3 are palindromic and RC2=C4. Every original frequency value is in the rectangle's convex hull,so testing these FOUR actual corners for a fixed numerator is EXACT;no free coefficient/root enlargement is made.

## 3. Four real affine loss curves and rational compact frequency

For omega>0 put `z=i*u`,`u=omega-1/omega`,`r=(i*omega-1)/(i*omega+1)`. The corner quotient is T/(P+rQ). Its denominator is nonzero by actual Hurwitz,and the sign of its real part is the sign of

`Phi=Re[T*conjugate(P+rQ)]`.

On this imaginary z,J(-z)=conjugate(J). Hence the four Phi values are

`Phi0-Z`, `Phi0-Y`, `Phi0+Z`, `Phi0+Y`,

`Phi0=Re[T*conjugate(Pmid)]`,

`Z=Re[T*conjugate(J)]`, `Y=Re[T*conjugate(r*conjugate(J))]`.

Their minimum is Phi0-max(|Z|,|Y|). This also proves the previous three-diamond support formula collapses to this ONE maximum;we reuse actual four corners rather than enumerate unrelated endpoint combinations.

Reciprocity of B and K permits0<omega<=1. Set

`t=omega²`, `xi=(1-t)/(1+t)` in[0,1), `delta=1-xi²`,

`v=u²=4xi²/delta`, `u/(omega+1/omega)=-xi`.

Let `X=tau0-tau2*v`,`W=tau1-tau3*v`,and `j0(v)=-w1*v-(w1+w2+w3)`,`j1=w2-w1`,so J(iu)=j0+i*u*j1. Exact real multiplication gives

`Phi0=X*(pi0-pi2*v)+v*W*(pi1-v)`,

`Z=X*j0+v*W*j1`,

`Y=-xi*K`, `K=X*(j0+2*j1)+W*(2*j0-v*j1)`.

For Y,use conjugate(r)=(u-2i)/(omega+1/omega) and multiply by J. These identities are symbolic integer/rational algebra;no numeric angle or square-root estimate is consumed.

Define their polynomial extensions

`Fhat=delta³*Phi0(4xi²/delta)`,

`Jhat=delta³*Z(4xi²/delta)`,

`Khat=xi*delta³*K(4xi²/delta)`.

Fhat,Jhat are even of degree<=6;Khat is odd of degree<=7. They are linear in tau. At xi1,Fhat=64*tau3,Jhat=Khat=0. The EXACT unrestricted existence criterion in this INPUT class is

`Fhat-Jhat>0`, `Fhat+Jhat>0`,

`Fhat+Khat>0`, `Fhat-Khat>0`,for EVERY xi in[0,1].           (FOUR)

The four inequalities correspond C1,C3,C2,C4 respectively. The xi1 constraints enforce exact degree/positive leading coefficient. At frequency0 and infinity,B/a tends to tau3>0;they are not silently divided out of the Laurent formula. FOUR is a strict CONVEX feasibility system in four homogeneous taus,or three after scaling;no uniqueness/strong-convexity assertion is made.

## 4. Compact cone dual and exact lift to unrestricted actual atoms

Let S in R4 consist of the tau coefficient vectors of the four polynomials in FOUR as xi ranges[0,1]. It is compact. If0 is outside conv(S),its closest point V0 satisfies `V dot V0>=||V0||²>0` for all V in S,giving a successful tau. If0 is in conv(S),no strict target can exist. Caratheodory in R4 gives

`sum_(j=1..m) lambda_j V_j=0`, `lambda_j>=0`,

`sum lambda_j=1`, `m<=5`.                                 (DUAL)

No actual such data or rational-frequency/weight guarantee is claimed. This is a proved theoretical alternative,NOT an executed/admitted finite witness.

For xi<1,t=(1-xi)/(1+xi),each corner functional equals

`64/(1+t)^7 * P_(a,B)(t)` on palindromic B.

Indeed `P_(a,B)=(1+t)t³*Phi` and delta=4t/(1+t)². Apply each functional to the palindromic projection `(B+RB)/2` of an ARBITRARY real degree<=7 B. The exact reversal identity

`P_(a,RB)(t)=t^7*P_(Ra,B)(1/t)`

lifts it to a POSITIVE combination of ACTUAL a,t and Ra,1/t atoms. At xi1,the lift is `32*(B(0)+leading(B))`,the genuine0/infinity endpoint pair since A7=1. Thus any actual DUAL would annihilate all eight unrestricted target coefficients and obstruct every strict target,not merely palindromic ones. At most five reciprocal constraint orbits,each at most two actual atoms,suffice;no optimal atom count or verification is asserted.

## 5. NEW uniform barrier: an obstruction cannot use only one or two frequencies

At a finite xi<1 put `D=P+rQ=a+i*c`,`b=u*c`,with u=omega-1/omega and v=u². Apart from the positive frequency factor delta³,the tau-vector is

`(-v*b,-v*a,b,a)` in order(tau3,tau2,tau1,tau0).              (VECTOR)

Positive sums of corner values AT ONE frequency are actual original-member values after normalization,because K is convex and evaluation is affine. The same frequency factor is common and positive,so it can be absorbed into those weights.

Suppose a nonzero DUAL used at most TWO DISTINCT finite frequencies v1!=v2. Let a1,b1 and a2,b2 be the positive-weight aggregate values at the two groups. The tau0/tau2 equations give

`a1+a2=0`, `v1*a1+v2*a2=0`,hence a1=a2=0.

The tau1/tau3 equations similarly give b1=b2=0. If v>0,u!=0,an aggregate a=b0 implies D0 for a normalized ACTUAL member,hence an imaginary-axis denominator zero:impossible.

If one group has v0/omega1,the same a0 conclusion is impossible. There a=Re(P+iQ)=P(0)>0:the palindromic averaged original member is in K,its cubic P is Hurwitz by §1's root map,and its constant is positive. This argument uses the REAL original convex box,not a free P/Q uncertainty.

A group at xi1 is the pure POSITIVE tau3-axis vector64. With at most one other finite frequency,tau0/tau1 force its a=b0,again impossible (or a>0 at v0). A single frequency alone is excluded by the same actual zero/endpoint positivity. Multiple corners at one frequency do not evade this grouping argument.

Consequently ANY actual positive annihilation needs at least THREE DISTINCT reciprocal frequency values. Together with DUAL's upper bound,a negative instance has a certificate with three to five distinct frequency groups and at most five total corner-orbits. This is an exact search barrier,not a supplied negative instance,an exhaustive search or a scientific execution count.

## 6. Honest full-width consequence and remaining mathematical task

If a specific base with all six paired widths positive were later proved robustly Hurwitz and FOUR-infeasible,compactness of K inside the OPEN Hurwitz set permits a sufficiently small positive rational enlargement A7 in[1-epsilon,1+epsilon] preserving all-member Hurwitz. The enlarged ORIGINAL independent box has ALL SEVEN positive widths,and common infeasibility persists by containment. No such base,epsilon or witness is supplied.

The task is therefore ACTUAL interval endpoints/full Hurwitz plus a three-to-five-frequency exact DUAL,OR a positivity/synthesis theorem for FOUR. A positive theorem limited to this symmetric INPUT subclass would not prove arbitrary SPR7 universality. This representation does not close general bad-infimum>1 attainment or other primary regimes;it is a correlation-preserving exact route to a genuine unrestricted counterexample,not replacement of the original question by a profile subproblem.

All new symmetrization,coefficient identities,four-corner support,compact polynomial conversion,DUAL/lift and frequency lower-bound proofs need a fresh complete scope/application reconstruction before promotion. No old source hash/reviewer headline,pending v4 result,formal/kernel/human/configured-family/executable/triple-finite/novelty gate or approximate scout is used as acceptance. Original process findings/HOLD/cutoff/deadline remain;no GO/native science/program/LP/replay/solver/CLI/nested agent,shared/source edit,publication/Git/deletion/config change or parked round closeout occurred.
