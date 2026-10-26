# Literal preview synthesis outside PASSIVE HID: active unforced hidden blocks and a sharp rational family

Owner InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 14:44:21 PDT 2026**, an observation bound, not an invented exact completion clock. **ONE immutable WRITTEN OWNER-CANDIDATE; NOT yet freshly reviewed or parent-supported.** This is preview-source v9, not the parent-evidence erratum of the same number.

## 0. Exact improvement and non-promotion boundary

The supported v5 infinite theorem assumes a PASSIVELY mean-square-stable performance-hidden block. This source gives an exact infinite-horizon synthesis theorem on a DIFFERENT explicit class where that block can be unstable after K0, but an orthogonal set of fully PRICED hidden controls stabilizes it. The essential new representation is a control-orthogonal, EXOGENOUSLY UNFORCED hidden subsystem. Its stabilization costs exactly zero for EVERY zero-state input/output experiment, because the ACTUAL hidden state remains zero under the constructed homogeneous feedback, not because its control cost is discarded.

A multi-parameter rational plant family then has a completely explicit sharp attenuation threshold for ALL finite h>=0 and ALL gamma>0, with necessity against arbitrary admissible nonlinear/history controllers and an actual stationary current-state realizer. Its hidden passive HID test fails, while its actual actively stabilized diffusion remains nonzero. This is a proper domain extension, NOT a closure of disturbance-FORCED unstable hidden blocks or unavoidable visible noise.

Named imports for the general structural theorem:

- complete488LF `literal-preview-synthesis-consolidated-v4-positive-preview.md`, SHA256 `2def3e70fc69253fdda6428b36fe946d59986d9aae6d9f485f54b8131dd5ae43`: deterministic infinite-preview converse for ALL causal laws, stabilizable/detectable QARE criterion, stationary window completion and transversality;
- complete245LF `literal-preview-synthesis-consolidated-v5-visible-quotient.md`, SHA256 `0ecb7a5d574ad5a4c58b8c24037a5a384aaf6d20777ede08f747e133d9b9e3c7`: finite invariant quotient, projected H1/mean bridge and original-output completion;
- their actual297LF union review and the37LF current parent disposition `preview-positive-visible-quotient-union-parent-v1.md`, SHA256 `17897814a5b53e5aeea7dc577a20f25b75c320ba562e8e97aabe1b9737e20cff`, support ONLY their stated old domains. They do NOT independently review the new application below.

The sharp family proof in §§6–9 does not depend on solving a QARE or on unreviewed v6/v7/v8. It uses only the already supplied projected H1 mean-zero lemma and elementary output/ODE/Itô identities, all new identities displayed here. No old stochastic mean-square criterion is substituted for the printed objective. None of this is kernel-checked, executable-certified, configured-family/human/formal/novelty acceptance.

Current primary uses strict UNIFORM G1<gamma as its declared convention. A separate exact endpoint calibration in §9 distinguishes the pointwise-every-input strict reading; it does NOT silently change that frozen convention or retroactively extend old sources. This is NOT another Robin/example refinement.

## 1. Model, actual output square and finite quotient

Work on INFINITY with the original constant-data scalar-Brownian plant

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW, z=D0x+D1u,

zero initial state and negative input history for the gain test, any finite h>=0, and every progressive input with E integral|w|^2<infinity. Internal exponential mean-square stability is additionally required at w=0 from every square-integrable initial state and zero external-input history. Unknown controllers may be consistent, strongly well-posed nonanticipative nonlinear/history laws; the constructed law will use ONLY the original current state/current input window.

Let N1(f)=E(integral_0^infinity|f|^2)^(1/2). Uniform gain is sup_(N1(w)>0) N1(z)/N1(w). Controls have the frozen local PATHWISE L2 admissibility; no expected-L2 control condition is silently imposed on unknown laws.

Assume R=D1^T D1>0 and define

    K0=-R^(-1)D1^TD0, Abar=A+BK0, S=A0+B0K0,
    Dtilde=D0+D1K0, Q=Dtilde^TDtilde>=0,
    vtilde=R^(1/2)(u-K0x), Bcal=B R^(-1/2), B0cal=B0 R^(-1/2).

Since Dtilde^TD1=0,

    |z|^2=x^TQx+|vtilde|^2,
    vtilde=R^(-1/2)D1^Tz.                              (1)

Let U=intersection_(j=0)^(n-1)ker(Q Abar^j), the largest Abar-invariant subspace in kerQ. Choose orthonormal visible rows pi and hidden columns Z, x=pi^Ty+Zq. Put

    Av=pi Abar pi^T, Qv=pi Q pi^T,
    AU=Z^T Abar Z, SU=Z^T S Z, Cv=pi C.

Then pi Abar Z=0, Dtilde Z=0, Q=pi^TQv pi. The visible pair(Av,Qv^(1/2)) is observable by maximality of U, exactly as in v5. For the new theorem take visible and hidden dimensions positive; zero-dimensional reductions are already covered by the old theorems.

## 2. The entire NEW actual-data domain

Supply an orthonormal control split [L N], so L^TL=I,N^TN=I,L^TN=0,LL^T+NN^T=I, and vtilde=L a+N b. Require ALL these finite equalities:

    pi S=0,
    pi Bcal N=0, pi B0cal N=0,                         (visible isolation)
    Z^T Abar pi^T=0, Z^T S pi^T=0, Z^T C=0,
    Z^T Bcal L=0, Z^T B0cal L=0.                      (hidden unforced)

Define

    Bv=pi Bcal L, B0v=pi B0cal L,
    BU=Z^T Bcal N, B0U=Z^T B0cal N.

Also assume B0v Bv^T=0 and(Av,Bv) stabilizable. These are the visible orthogonality and stabilizability conditions; detectability is supplied by the actual maximal quotient.

The ACTUAL equations and output square, for EVERY control law, are now exactly

    dy=(Av y+Bv a+Cv w(t-h))dt+B0v a dW,
    dq=(AU q+BU b)dt+(SU q+B0U b)dW,
    |z|^2=y^TQv y+|a|^2+|b|^2.                        (2)

"Unforced" means no direct exogenous w, visible state or visible control in the hidden equation. An arbitrary unknown law may still feed w into b; I do NOT claim q is autonomous for every law. The construction below chooses b=Kq, making it genuinely autonomous.

Finally the PLANT DOMAIN includes the explicit active-hidden certificate

    exists X=X^T>0,Y:
      [[AU X+BU Y+X AU^T+Y^T BU^T, (SU X+B0U Y)^T],
       [SU X+B0U Y,                       -X]]<0.     (AH)

This is a finite-dimensional LMI, not an assumed necessary condition for all original nonlinear/history stabilization OUTSIDE this class. With H=X^(-1),K=Y X^(-1), its Schur complement and congruence by H give exactly

    (AU+BUK)^TH+H(AU+BUK)
                  +(SU+B0UK)^TH(SU+B0UK)<0.          (3)

Conversely any such explicit H/K certificate gives X=H^(-1),Y=KX and(AH). No mean-square state estimate is used to infer integrability of an UNKNOWN unpriced hidden diffusion or to prove a nonlinear-to-linear stabilization theorem.

## 3. Exact finite-dimensional N&S condition ON that domain

Set Dv=Bv Bv^T and

    Hv=[[Av,-Dv],[-Qv,-Av^T]],
    [E;F]=exp(-h Hv)[I;0].

**Theorem.** For every plant in §2's ENTIRE stated domain and gamma>0, original literal strict UNIFORM G1<gamma synthesis with full-state internal exponential mean-square stability is equivalent to

    exists rho>gamma^(-2), P=P^T>=0,
    k=(PE-F)Cv,
    Av^TP+PAv+Qv-PDvP+rho*k*k^T=0.                    (AQARE)

This is a finite-dimensional Riccati-type condition with a strict scalar margin, not asserted convex. The hidden certificate is a DOMAIN premise; do not read the theorem as an unrestricted iff "AH and AQARE" for arbitrary plants. The theorem extends outside PASSIVE HID specifically when active hidden stabilization has no zero-state input/output price.

## 4. All-causal necessity without taking the hidden mean

Suppose an arbitrary original feasible law has uniform gain at most g<gamma. For each deterministic finite-energy input, (1) controls E||a||_L2 and E||b||_L2 by N1(z). Therefore

    E(integral|B0v a|^2)^(1/2)<infinity.

The projected H1 lemma makes the visible local martingale true mean-zero on every finite prefix. Gronwall gives finite visible first moments. The original hidden state need NOT have a mean. Taking ONLY visible/control means yields

    ybar'=Av ybar+Bv abar+Cv w(t-h),
    ||(Qv^(1/2)ybar,abar,bbar)||_L2<=N1(z)<=g||w||_L2.

The inequality is Bochner Jensen applied to the actual output square, not an exchange of N1 with N2. Deleting the NONNEGATIVE bbar cost leaves a deterministic visible map of gain<=g. Consistent strong causality across deterministic input prefixes supplies ONE causal mean map, even if the original a used all hidden/Brownian histories. It is not called a printed controller implementation.

The named v4 deterministic infinite-preview converse applies to(Av,Bv,Cv,Qv,I), using visible stabilizability and the observable quotient. It gives(AQARE). Neither passive hidden stability nor expected control L2 was used in this necessity direction.

## 5. Actual original-window sufficiency and full internal stability

Given(AH)/(AQARE), choose K,H as above, eta=rho^(-1/2)<gamma, and define

    Kh(tau)=[P,-I]exp(-tau Hv)[Cv;0], 0<=tau<=h,
    gwin(t)=integral_0^h Kh(tau)w(t-h+tau)dtau,
    a_star=-Bv^T(P*pi*x+gwin), b_star=K Z^T x,
    u=K0x+R^(-1/2)(L a_star+N b_star).                 (4)

This is a stationary deterministic law of the ACTUAL current x and current window[t-h,t], with zero negative history. No remote-memory state, energy budget, reset, new Brownian information or separate controller state is inserted.

By B0v Bv^T=0 its VISIBLE diffusion is exactly zero. The named v4 realization/transversality theorem gives Av-DvP Hurwitz and the pathwise visible attenuation<=eta for every L2 sample input.

The ACTUAL hidden closed loop is

    dq=(AU+BUK)q dt+(SU+B0UK)q dW.

For the gain experiment q(0)=0, strong uniqueness gives q(t)=0 and b_star(t)=0 for EVERY progressive w. Hence the actual full output energy is EXACTLY the visible energy in(2), with no omitted priced hidden term. The pathwise bound implies N1(z)<=eta N1(w)<gamma N1(w). Stable visible/window convolutions give finite expected state/control energy for expected-L2 inputs; hidden state is identically zero. Thus this really is an admissible original implementation.

For arbitrary initial x and w=0, the visible state is the deterministic stable equation y'=(Av-DvP)y; the hidden homogeneous SDE has the strict quadratic certificate(3). Itô and norm equivalence give E|q(t)|^2<=M_U exp(-lambda_U t)E|q(0)|^2. Combining the two orthogonal blocks proves full original internal exponential mean-square stability. This is not inferred from zero-state gain.

The quadratic Itô expectation needs no fourth moments: on finite intervals the constructed linear SDE has E sup|q|^2 and E integral|hidden_diffusion|^2 finite. The expected square-root bracket of its storage martingale is bounded by their square-root product times2||H||. The same H1 mean-zero lemma and localization justify(3)'s expected estimate. No integrability assertion about UNKNOWN nonlinear hidden controls is smuggled in.

## 6. A rational-parameter family STRICTLY outside passive HID

Take ANY positive rational a,b,c,d,sigmaV, ANY finite real h>=0, and the original actual plant

    dy=(-a*y+b*u1+c*w(t-h))dt+sigmaV*u2 dW,
    dq=(q+u3)dt+(q+u3/4)dW,
    z=(d*y,u1,u2,u3).                                  (5)

All constant matrices are rational:

    A=diag(-a,1), B=[[b,0,0],[0,0,1]], C=(c,0)^T,
    A0=diag(0,1), B0=[[0,sigmaV,0],[0,0,1/4]],
    D0=[[d,0],[0,0],[0,0],[0,0]],
    D1=[[0,0,0],[1,0,0],[0,1,0],[0,0,1]].

R=I3,K0=0,Q=diag(d^2,0), U=span(e2), pi=(1,0),Z=e2. Choose L=(e1,e2),N=e3. The visible actuator pair is Bv=(b,0),B0v=(0,sigmaV), so their product is0. Hidden is unforced by w,y,a. ALL three controls are fully priced.

Passive HID is IMPOSSIBLE: AU=SU=1 gives AU^TH+H AU+SU^TH SU=3H>0 for every scalar H>0. Yet K=-3,H=1 gives

    AU+BUK=-2, SU+B0UK=1/4,
    -4+1/16=-63/16<0.

Equivalently X=1,Y=-3 in(AH) gives the exact2x2 matrix[[-4,1/4],[1/4,-1]], whose Schur complement is-63/16. This is hand rational algebra, NOT an executed finite witness.

Full MATCH fails since S=A0 is nonzero. Full ORTH also fails: B0 B^T=[[0,0],[0,1/4]]. Global NEO fails at x=e2,u=0: z=0 while full diffusion=e2. Therefore the example is not secretly inside v4 or v5's passive-HID infinite domain. Its hidden diffusion remains nonzero under active feedback for nonzero hidden initial state.

## 7. An explicit sharp same-gamma stationary original controller

Define positive exact quantities

    p=d^2/a, k=b*d^2/a, lambda=a+b*k=(a^2+b^2*d^2)/a,
    gstar^2=c^2*d^2/(a^2+b^2*d^2).                     (6)

The SQUARED threshold is rational for every rational parameter tuple; no matrix solve, limiting decimal or unknown spectral number enters it. The actual stationary current-state law is simply

    u1=-k*y, u2=0, u3=-3*q.                            (7)

It ignores the available preview, which is permitted for every h. For zero initial state, q=0 identically; visible y'=-lambda*y+c*f, f=w(t-h), and |z|^2=(d^2+k^2)y^2. Direct differentiation, using p*lambda=d^2+k^2, gives the PATHWISE identity

    d(p*y^2)/dt+|z|^2-gstar^2*f^2
                    =-gstar^2*(f-(lambda/c)y)^2.       (8)

This proves G1<=gstar by integration and expectation; no stochastic mean-square supply is substituted for the literal objective. For every L2 sample input y,y' lie in L2, so (y^2)'=2yy' is L1, y^2 has a limit, and that limit must be0. Thus(8) also gives the exact infinite energy identity with its remainder retained.

At w=0 but arbitrary square-integrable initial state, E y(t)^2=e^(-2lambda t)E y(0)^2 and E q(t)^2=e^(-63t/16)E q(0)^2. Hence the full original state is internally exponentially mean-square stable with constant1 and exponent min(2lambda,63/16). Active hidden cost is REAL for nonzero initial q; it disappears in the gain test ONLY because the unforced hidden state has zero initial condition.

## 8. Necessity against EVERY admissible nonlinear/history controller

Let ANY original law for(5) have finite uniform gain bounded by g. Test the deterministic input w_L=1_[0,L], L>0. Then N1(w_L)=sqrt(L) and N1(z_L)<=g sqrt(L). In particular E||u2||_L2<=g sqrt(L), so sigmaV*u2 has H1 integrability. The visible martingale is true mean-zero, without needing a hidden-state mean or N2(u). Put ybar=E y, vbar=E u1. Jensen gives

    ||(d*ybar,vbar)||_L2<=g sqrt(L), ||vbar||_L2<=g sqrt(L),
    ybar'=-a*ybar+b*vbar+c*1_[h,h+L].                  (9)

The stable scalar convolution, from zero visible initial state, gives the uniform-in-time bound

    |ybar(t)|<=(b*g+c)*sqrt(L/(2a)).                  (10)

Integrate(9) over[h,h+L], retaining BOTH boundary states, including any legitimate preview pre-action:

    cL=ybar(h+L)-ybar(h)+integral_(h)^(h+L)(a*ybar-b*vbar).

Cauchy–Schwarz with the actual output weights gives

    |integral(a*ybar-b*vbar)|
       <=sqrt(L)*sqrt(a^2/d^2+b^2)*||(d*ybar,vbar)||_L2
       <=sqrt(a^2/d^2+b^2)*g*L.

Using(10), dividing by L and letting L tend to infinity yields

    c<=sqrt(a^2/d^2+b^2)*g, hence g>=gstar.            (11)

Every w_L has finite expected squared energy. This is a written limiting argument, not a program or an uncounted infinite-energy test input. No restriction to linear, stationary, Markov or differentiable unknown controllers was used. The particular law(7) attains uniform induced gain gstar by(8)/(11).

Consequently, for the ENTIRE rational-parameter family(5), all finite h>=0,

    strict UNIFORM G1<gamma synthesis with full internal EMS
       IFF gamma^2>c^2*d^2/(a^2+b^2*d^2).             (12)

This is a genuine N&S result at the original current-state/window information class; the necessity allowed even more history, and the sufficiency actually realizes the printed information. It is not a numerical example or a mean-square substitute theorem.

## 9. The literal pointwise-strict endpoint is DIFFERENT on this family

For clarity, consider ALSO the distinct interpretation "for EVERY nonzero admissible w, N1(z)/N1(w)<gamma", without requiring that their SUPREMUM be strictly below gamma. This paragraph does NOT replace the frozen primary uniform convention.

For law(7), on every nonzero L2 sample path the remainder in(8) is POSITIVE. If f-(lambda/c)y=0 almost everywhere, then y'=0 and y(0)=0 imply y=f=0. Therefore for any nonzero input in norm,

    ||z||_L2<gstar*||w||_L2

on the positive-probability event ||w||>0, with equality0 only on its complement. Both norms are integrable. Their nonnegative gap has positive expectation, so N1(z)/N1(w)<gstar for EVERY nonzero admissible input. Yet its supremum is gstar by §8.

If the pointwise-strict property held at gamma<gstar, it would imply the non-strict uniform bound G1<=gamma, contradicting(11). Thus the EXACT classification for this alternative reading on(5) is

    pointwise-every-input strict synthesis
       IFF gamma^2>=c^2*d^2/(a^2+b^2*d^2).            (13)

The endpoint gamma=gstar is feasible for(13) but NOT(12). This is a quantified concrete warning against silently identifying the two readings of a printed ratio. It is NOT a claim that N1=RMS generally, a new Robin separation, a finite-horizon endpoint theorem or a blanket interpretation of the book's missing supremum symbol.

## 10. Imports, remaining original gap and exact gate

For the structural theorem §§1–5, the nontrivial named import is the exact deterministic infinite-preview machinery in v4 and the projected integrability/quotient lemma in v5. All NEW control-block decompositions, priced hidden-cost handling, LMI congruence, actual window realizer and internal-stability proof are supplied. For the rational family §§6–9, no QARE solution or unused transitive theorem is asserted: the full same-gamma result follows directly from the displayed output square, H1 mean bridge, stable convolution, elementary Cauchy–Schwarz and pathwise identity. Ordinary finite-dimensional linear-SDE well-posedness, Itô/localization and positive-definite norm equivalence are the remaining standard imports.

This new source requires its OWN complete fresh reconstruction, including all new applications and any exact import UNION, before promotion. Old v4/v5 union support does not certify it; v6/v7/v8 are separate candidates, NOT correctness inputs. The exposure in addendum6 and checkpoints14/15 predates this source and is not relabeled preregistration. No earlier pinned file is edited.

ENTIRE residual remains: generic genuinely visible autonomous noise/pi S!=0; projected drift/noise actuator directions failing QORTH; disturbance-FORCED unstable hidden blocks and their prescribed-gamma cost tradeoffs; arbitrary hidden stabilization without the supplied active linear certificate; rank-deficient R/unpenalized-control integrability; removal of visible stabilizability; full arbitrary-plant finite/infinite N&S and original stationary finite-book syntax. The new structural result closes only the EXOGENOUSLY UNFORCED active-hidden subdomain. The pointwise endpoint classification closes only the explicit family, not arbitrary data.

Everything here is WRITTEN. No scientific interpreter/eval/program/CAS/enumeration/solver/Riccati/LMI routine/replay/simulation/compile/CLI/nested agent or new GO occurred. Rational signs and identities were HAND derived, NOT kernel-verified; old unadmitted evals retain zero credit. All earlier owner/parent process findings, v9/v10/v11/HOLD, original October27 cutoff/deadline and exclusive owner root remain. No novelty/priority, formal/human/configured-family/executable acceptance, full-book solution, continuous18-way activity or round completion is claimed.
