# Balanced B: an exact FOUR-simplex feedback fiber, five coefficient equations and a full dual

Owner MathResearch96h-2 / original math-1. Actual `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:59:12 PDT 2026**. **WRITTEN AUTHOR-CANDIDATE, UNREVIEWED.** All algebra/proofs are conventional exact WRITTEN symbols/fractions/integer products; no scientific interpreter/calculator/eval/CAS/program/enumeration/LP/solver/replay/checker/test/build/CLI/nested agent/new GO. No machine/kernel verification.

## 1. Scope: FULL arbitrary balanced B, not a fixed-holding cone

Fix c,d>0,a=c+d,b²=8d²/9 and `D5(s)=(s+c)((s+a)²+b²)²`, K=D5(0)>0. The original question remains actual PH7 existence at this target, NOT_PROVED/minimum{7,8}. This packet gives an exact fiber representation for EVERY literal balanced3+3 B, with arbitrary actual principal matrices, boundary supports, holdings and feedback. It neither fixes the outer data nor proves all fibers empty/nonempty.

The named global connection to the original problem is the COMPLETE266LF `PH7-standalone-global-ordered-A-or-balanced-B-equivalence-v1.md`, SHA256 `3815c4d699735797090dbd974f522828363c02931b604d8f36af438f00d7ffc6`, NEW UNREVIEWED. Original coverage by ordered A union B remains at the parent's recorded conditional boundary until that full proof passes its own gate. The local balanced-fiber theorem below is independently proved for its printed literal class; it does not infer a global normal form from the ancestor's title/hash.

The separate141LF PH3-renewal/complex-double-contact candidate, SHA256 `6171627f20c035ef7e9cb99c35e46a2bef05d2bd4b47451fc71119abbe4fed24`, is NOT a correctness premise here. Its pruning, strict recycling and complex contacts remain their own gate. This new fiber has no essential-channel/co-reachability assumption beyond the exact physical conditions printed below; it also retains degenerate B cases that another valid proof may send to A.

## 2. Actual OUTER data and automatic real-hidden quadratic

Choose real3×3 Hurwitz Metzler A,F with

    b0=−A1>=0,
    alpha>=0,alpha1=1,
    alpha b0=0, L_R=alpha A b0>0;
    t,omega>=0,
    t^T omega=0, L_S=t^T F omega>0,
    h=−F1−omega>=0.                              (OUTER)

These are actual upstream/input and downstream/exit data. No off-diagonal polynomial factors or path weights are selected separately. The positive L_R,L_S, together with the zero earlier terms, give exact shortest pre/post distances TWO each. For example alpha A b0 has no signed diagonal contribution because alpha_i b0_i=0; it is the actual positive one-transition path sum followed by the center edge. Likewise t^T F omega is the actual center/S/exit two-edge path sum. Hurwitz A and b0=−A1 give `(−A)^−1 b0=1`.

Define

    a_R(s)=det(sI−A), a_S(s)=det(sI−F),
    U(s)=adj(sI−A)b0,
    V(s)^T=t^T adj(sI−F),
    N_R(s)=alpha U(s), N_S(s)=V(s)^T omega.

The high-s expansions `N_R/a_R=alpha(sI−A)^−1 b0` and `N_S/a_S=t^T(sI−F)^−1 omega` give exact degrees ONE, with leading coefficients L_R,L_S. Constants are

    N_R(0)=a_R(0)>0,
    N_S(0)=a_S(0) gamma>0,
    gamma=t^T(−F)^−1 omega>0.

Positivity of gamma follows from the actual two-edge positive path ensured by L_S>0. Thus N_R,N_S are linear with both coefficients strictly positive, no separate discriminant/root test. Necessarily retain the leading target normalization

    L_R L_S=K.                                    (LEAD)

Set `Q=N_R N_S/K=(s+x)(s+y)`, where `x=N_R(0)/L_R>0`, `y=N_S(0)/L_S>0`; x=y is allowed. Q is AUTOMATICALLY real monic Hurwitz. It is defined from the actual outer matrices and boundaries, not an independent quadratic. No claim Q|a_R or Q|a_S.

## 3. Trace fixes the center holding — it is NOT another free routing variable

Let `A_hold=−trA`, `F_hold=−trF`, and p_Q=x+y. In a full characteristic D5Q the coefficient of s6 is c+4a+p_Q. The off-diagonal feedback in the literal matrix below contributes only degrees<=5. Therefore the only possible center holding is

    lambda=c+4a+p_Q−A_hold−F_hold.                 (TRACE)

Require `lambda>=t^T1`; since t is nonzero by L_S>0, this also gives lambda>0. Put `r0=lambda−t^T1>=0`. There is no hidden independent adjustment of lambda after the fiber is solved.

For fixed outer data satisfying(OUTER)/(LEAD)/(TRACE), every admissible literal feedback has

    r>=0, r^T1=r0,
    f>=0,D>=0, f+D1=h,                             (BUDGET)

and assembles the actual matrix/input/exit

    T=[ A       b0      0
        r^T    −lambda  t^T
        D       f       F ],
    alpha_full=(alpha,0,0), omega_full=(0,0,omega)^T.

The row ties give EXACTLY `omega_full=−T1>=0`; alpha_full is a probability row. All fifteen feedback coordinates r_i,f_j,D_ji are preserved. In particular f+D1=h is THREE separate post-row budgets, not a single aggregate mass constraint. These budgets must not be dropped to obtain an easier nonnegative cone.

## 4. Full common-matrix polynomial identity and exact fiber iff

Solve the first/last resolvent blocks for the same T. For generic s,

    y_R=(sI−A)^−1 b0*y_center,
    y_S=(sI−F)^−1[(D(sI−A)^−1 b0+f)y_center+omega].

The center feedback scalar is `s+lambda−r^T(sI−A)^−1 b0−t^T(sI−F)^−1 f−t^T(sI−F)^−1D(sI−A)^−1 b0`. Multiplying by a_R a_S gives the entire characteristic

    P7=(s+lambda)a_R a_S−a_S r^T U−a_R V^T f−V^T D U,

and the actual adjugate numerator is N_R N_S. Clearing denominators makes these polynomial identities valid at ALL principal/hidden coincidences. Define the fixed residual

    R_poly=(s+lambda)a_R a_S−D5 Q.

**Fiber theorem.** A literal balanced PH realization exists at THESE fixed outer data iff there are feedback entries satisfying(BUDGET) and the ENTIRE identity

    R_poly=sum_i r_i a_S U_i
           +sum_j f_j a_R V_j
           +sum_(j,i) D_ji V_j U_i.                (FIBER)

Necessity follows from the actual full characteristic and target numerator. Conversely, (BUDGET) gives the actual row/input/exit ties and Metzler matrix. (FIBER) makes its characteristic D5Q, Hurwitz because c,a,x,y>0 and b>0. Its ACTUAL numerator is `N_R N_S=KQ` by(LEAD) and the physical definition of Q. The transfer is exactly K/D5 after cancellation. The distance TWO+TWO conditions were already physical in(OUTER). This proves sufficiency at every boundary allowed by zero r/f/D coordinates or repeated x=y, not a spectrum-only certificate.

Every actual literal B realization supplies its own outer data satisfying these conditions; every successful fiber constructs a literal B pair. No selected holding graph, single initial/exit or independently assigned two linear factors has narrowed the ENTIRE class.

## 5. EXACT four-simplex membership, not a fifteen-generator cone relaxation

For polynomials write conv for their finite convex hull. Define the fixed compact convex set

    C=r0*conv{a_S U_1,a_S U_2,a_S U_3}
      +sum_(j=1..3) h_j*
          conv{a_R V_j,V_j U_1,V_j U_2,V_j U_3}.    (FOUR)

Multiplication by a zero budget means the singleton{0}; there is no excluded zero-budget case. Then the fiber theorem is EXACTLY

    R_poly in C.                                  (MEMBER)

Indeed r/r0 gives the first simplex weights when r0>0. In post row j, f_j/h_j is the direct-center vertex weight and D_ji/h_j are the three R-destination weights. They sum1 by(BUDGET). Conversely any such barycentric representation recovers nonnegative r,f,D with ALL four budgets. Zero-budget rows are forced zero, with arbitrary unused barycentric weights; no division by0 is needed.

Thus the entire physical routing fiber is a Minkowski sum of FOUR actual finite simplices, with15 displayed vertices across the four groups. It is not the cone generated by those polynomials without budgets, not four separately realizable cut matrices, and not a claim that arbitrary outer choices are possible.

## 6. Why only FIVE coefficient equations remain — none silently discarded

U_i,V_j have degree<=2. Therefore a_S U_i and a_R V_j have degree<=5, V_j U_i degree<=4. The s7 terms in R_poly cancel by monicity, and(TRACE) removes s6. Consequently R_poly and every element of C have degree<=5.

The CONSTANT comparison is AUTOMATIC from the exact physical budgets, not an optional check. At0, `U_i(0)=a_R(0)` for every i. Write `v0^T=t^T(−F)^−1`, so V_j(0)=a_S(0)v0_j. Every vertex in post row j has the SAME constant a_R(0)a_S(0)v0_j, while every first-group vertex has constant a_R(0)a_S(0). Hence all C has constant

    a_R(0)a_S(0)[r0+v0^T h]
      =a_R(0)a_S(0)[lambda−t^T1
          +t^T(−F)^−1(−F1−omega)]
      =a_R(0)a_S(0)(lambda−gamma).

Meanwhile Q(0)=N_R(0)N_S(0)/K=a_R(0)a_S(0)gamma/K, and D5(0)=K, so R_poly(0) is EXACTLY the same number. This proves the redundancy at all budgets, including zeros.

Let pi retain the coefficients of s,s²,s³,s4,s5 as a vector in R5. Full(MEMBER) is therefore equivalent to the FIVE-dimensional membership `pi(R_poly) in pi(C)`: the constant and two higher obligations were derived separately, not ignored. No claim that the outer matrix/data search itself has only five scalar unknowns.

## 7. COMPLETE dual support-function criterion, with its sufficiency proved

For EVERY real linear functional ell on these FIVE coefficients, define

    H_C(ell)=r0*max_i ell(pi(a_S U_i))
      +sum_j h_j*max{ell(pi(a_R V_j)),
                    ell(pi(V_j U_1)),ell(pi(V_j U_2)),
                    ell(pi(V_j U_3))}.

Then the exact fiber iff is equivalently

    ell(pi(R_poly))<=H_C(ell) for EVERY ell.         (DUAL)

Necessity is direct: maximize separately on each simplex and add the maxima. For sufficiency, pi(C) is nonempty compact convex. If z=pi(R_poly) lay outside, let y be its closest point in pi(C). With ell(w)=(z−y)·w, minimal distance along every segment y→q gives `(z−y)·(q−y)<=0` for every q∈pi(C). Thus `ell(z)=ell(y)+||z−y||²>sup ell(pi(C))`, contradicting(DUAL). This proves completeness, not just a one-sided certificate. No dual/LP algorithm or finite functional sample has been run.

A universal B exclusion would need such a separating functional for EVERY admissible outer data set, or another proof of empty membership. A single selected functional/data case is not a global contradiction. A witness must give actual outer matrices plus a COMMON full polynomial barycentric representation, not different routings at different coefficients/values of s.

## 8. Exact positive-real sharp routing bounds, at ALL symbolic s>=0

A useful necessary family follows directly from budgets, without pretending pointwise extrema settle polynomial membership. For real s>=0 put

    u(s)=(sI−A)^−1 b0,
    v(s)^T=t^T(sI−F)^−1,
    u_min=min_i u_i, u_max=max_i u_i.

Every u_i is a normalized first-hit transform starting at phase i, because b0=−A1 and A is transient. Thus 0<u_i<=1, with STRICT u_i<1 for s>0 (the first holding time is positive); v_j>=0. The actual return numerator is

    B_return(s)=r^T u+v^T f+v^T D u.

For each post row j its budget h_j can route either directly to center (value1) or to an R state (value u_i). The first group routes its r0 among u_i. Therefore EVERY full feedback satisfies

    u_min(s)[r0+v(s)^T h]
      <=B_return(s)
      <=r0*u_max(s)+v(s)^T h.                      (REAL)

At a SINGLE symbolic real evaluation these bounds are sharp over the budget polytope: put r and every D-row mass at a minimum-state for the lower bound; put r at a maximum-state and all post return budgets in f for the upper. Different s may choose different extreme states/routings, so attaining these separate evaluations is NOT a common polynomial witness. At s=0 both bounds reduce to lambda−gamma, agreeing with §6.

For a target solution the SAME B_return must be

    s+lambda−D5(s)Q(s)/(a_R(s)a_S(s)).

Substituting this in(REAL) gives an exact necessary ALL-real-s constraint on arbitrary actual outer data. No chosen s/c/d/holding instance, numeric parameter probe, approximate magnitude claim or interpreter check is used. No inference to infeasibility follows merely from displaying the inequalities.

## 9. Exact remaining gap, ancestry and permanent process limits

The new mathematical representation is ENTIRE balanced B as an arbitrary-outer-data search with its center holding fixed by TRACE and its feedback a compact FOUR-simplex membership/complete dual in five coefficient coordinates. It retains every actual PH input/exit/row tie and all15 feedback variables. This is distinct from the ordered-A TEN cone/fiber and from the separate essential-B PH3 renewal/contact theorem. It does NOT replace them by a free positive polynomial, independent block spectrum, equal-modulus/rate ansatz or selected numerical LP experiment.

**Still unresolved:** whether some actual outer data satisfy all these exact conditions at8/9, or whether ALL corresponding four-simplex fibers can be excluded. Arbitrary ordered A also remains open. No B-emptiness, original8/9 PH7 witness/min8, maximal band, numerical-bound/upper change, executable/formal/kernel/human/configured-family/novelty/SOTA/priority acceptance. Global A/B coverage must still receive its OWN full266LF proof gate; this local iff does not retroactively accept that source or its historical NR-DOM/NR-SHARED ancestry.

All substantial proof material here was saved completely in checkpoint076 before this manuscript, not claimed a future preregistered discovery. It follows ACTUALv119RETURN→NEWwholeprimaryACKWRITTEN/SENT before primary work. Permanent NEWcadence071to072FULL33m29s/firstlate30m36s/parentv32, distinctprematureturnendv21 and ALL older exactness/cadence/opaque/documentary/importpin/ZEROwithdrawnprobe/guidance findings remain. No processcure/cleanthought-runtime-access-countcensus/falsity-execution-from-process inference.

Only ordinary finite matrix/resolvent/adjugate algebra, positivity of transient finite CTMCs and an explicitly proved compact finite-convex separation are used for the local fiber. No unsupplied load-bearing specialized lemma/new historical numerical theorem is hidden. This complete candidate needs its OWN ENTIRE mathematical AND dependency/application gate before parent adoption. Same18/exclusiveOWN/HOLD/October27sciencecutoff11:05:38/deadline12:35:38/<=30minsubstantivecheckpoints/noearlyfinalpark or96-hour closeout. Sources/gates are immutable; no Git/deletion/publication/newGO.
