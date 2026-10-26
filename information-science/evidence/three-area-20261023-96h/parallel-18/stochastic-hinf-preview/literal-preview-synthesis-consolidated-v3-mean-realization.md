# Literal stochastic preview synthesis — a mean-martingale necessity bridge and exact noise-erasing subclasses

**InfoHinfPreview-2, info-3. ONE immutable consolidated WRITTEN successor; CANDIDATE, not accepted.** Actual preceding `/bin/date` observation: **Sun Oct 25 10:50:11 PDT 2026**. This is an observation bound before creation, not a fabricated exact creation time.

## 0. Genuine advance, scope and frozen exposure

This manuscript does NOT refine the completed Robin/example endpoint. It addresses the next necessity/realization gap by a new representation:

1. A finite algebraic condition makes finite **literal N1 output** imply that the diffusion integral is a true H1 martingale. Bochner Jensen then gives an exact SAME-gamma deterministic-mean necessary problem for EVERY nonlinear admissible law. No N2 control hypothesis or squared stochastic-objective substitution is made.
2. For h=0 and a stated matched/orthogonal actuator class, a finite-dimensional Riccati/Hamiltonian condition is **necessary AND sufficient at the prescribed gamma**, with an explicit printed state-feedback realizer. Necessity covers arbitrary causal nonlinear histories, with no differentiability, stationarity, linear-optimality assumption or unproved Markovization. A sample-and-hold adversary proves the needed deterministic Riccati converse without assuming a feedback loop against a pathological nonlinear controller is well posed.
3. For B=0 and matched diffusion, positive preview is covered exactly: the sharp literal synthesis value is an uncontrolled deterministic convolution norm. Finite horizons have a finite-dimensional Riccati/Hamiltonian test on T-h; infinite horizons with A Hurwitz have a SAME-gamma finite-dimensional strict bounded-real LMI. The explicit law is static and of the printed information form, and on infinity internally exponentially mean-square stable.

These are consequential SUBCLASS theorems and a broader necessary bridge, NOT general stochastic preview N&S. The entire remaining general gap is in §11.

Mandatory v9 FIRST, v10 SECOND, v11 THIRD and HOLD were completely read, followed by common rules and the exact own assignment in `primary-continuation-20261025-102319-v1.json`, SHA256 `b4dce3ac050ee6688295eff9cbf3e2f3f6326f93e8f973db8374e752770e594b`. All active reviews, including actual v73-A, were returned before the separate exposure ACK `primary-continuation-20261025-102319-ack-v1.json` and before this new proofbody. Informal leads predating the ACK are disclosed there, not called preregistered. Complete414LF v2 and complete25LF parent boundary were read before new proof work. V11's withdrawal of that parent's printed09:46:30 clock remains binding; this successor does not backdate it.

The old414LF finite-rational-expression family, SHA256 `d1e367cff5a4098c60bd0e44226eec72b7c91ce7a69c538c1b680fc043e22173`, retains its actual v67-A/parent WRITTEN support only at its expression level. It is not used as a lemma below. Old four eval submissions remain preserved, unadmitted and at ZERO executable/certificate credit. **No scientific interpreter/eval/program, symbolic calculation, enumeration, solver, eigensolve, simulation, replay, compile, external-model CLI or nested agent was used here.** Only source/metadata reads, hashes, clocks and own-root writes occurred. All new identities below are WRITTEN, not WRITTEN_CHECKED_IN_KERNEL.

## 1. Actual model, information and literal criterion

Use the book's actual constant-matrix model, re-read in the images of printed pp674–676:

    dx=(A x+B u+C w(t-h))dt+(A0 x+B0 u)dW,
    z=D0 x+D1 u.

The book explicitly allows h>=0 and both finite/infinite horizons. Its controller is state/current-window `F(x(t),w(s):t-h<=s<=t)`. The frozen finite-horizon convention allows explicit deterministic time dependence F_t; it does NOT grant energy-history states or an arbitrary controller memory implementation. Initial state and negative-time input are zero. Disturbances are progressive with finite expected squared energy on the counted interval. For finite T>h, count input ONLY on[0,T-h] and output on[0,T]; on infinity count both to infinity. Testing deterministic inputs with zero uncounted tail is always allowed. Every explicit realizer below ignores any uncounted tail, so its existence statement adds no terminal-preview energy.

Write

    N1(v)=E ||v||_L2(time),
    G1(F)=sup_(w!=0) N1(z_F,w)/N1(w).

One fixed nonanticipative, event-local, strongly well-posed law is used for ALL inputs; one may not choose an unrelated progressive open-loop control after seeing each entire deterministic input. Usual causality respects equality of input histories almost everywhere. Finite gain and zero response to zero data are required. Necessity below also holds for larger consistent causal history-law classes. Existence supplies only the displayed state laws, with no added memory.

All matrices are real and compatible; W is scalar standard Brownian motion. The same arguments extend to finitely many diffusion channels if each displayed diffusion factorization/cancellation condition is imposed channel by channel; no such extension is needed for the stated scalar-W theorem.

Assume throughout

    R=D1^T D1 >0,
    K0=-R^(-1) D1^T D0,
    Q=D0^T D0-D0^T D1 R^(-1)D1^T D0 >=0,
    Abar=A+B K0,
    v=u-K0 x.

Q is nonnegative because it is the Schur complement of a Gram matrix. Exact completion gives, for EVERY x,u,

    |z|^2=x^T Q x+v^T R v.                              (1)

Thus finite N1(z) implies E||v||_L2<infinity, but emphatically does NOT assert E||v||_L2^2<infinity.

## 2. An H1 lemma with a written proof, not a hidden mean-square assumption

**Lemma 1.** If a continuous local martingale M starts at zero and

    E S <infinity,  S=(trace[M]_T)^(1/2),

then M is a true uniformly integrable martingale on[0,T] and E sup|M|<=8 E S. In particular E M_t=0.

Here is the needed proof. Initially localize at increasing norm/quadratic-variation levels so the maximal function is integrable. For lambda>0, stop when |M| first reaches lambda. After that time, stop the increment when its additional quadratic variation reaches delta^2 lambda^2. Conditional Itô isometry and the weak L2 maximal inequality for that stopped increment give probability at most delta^2 of an increment of size lambda. On the event S<=delta lambda, the full relevant increment is not lost by this stopping. Hence

    P(M*>2lambda,S<=delta lambda)
        <=delta^2 P(M*>lambda),
    P(M*>2lambda)<=P(S>delta lambda)+delta^2P(M*>lambda),

where M*=sup_(t<=T)|M_t|. Integrating in lambda yields

    (1/2-delta^2) E M* <= E S/delta.

Take delta=1/2 to obtain E M*<=8 E S. Apply this to the norm/quadratic-variation stopped martingales; their quadratic variations are bounded by the original one. The stopping times increase to T since the original path is continuous with finite quadratic variation. Monotone convergence gives the same bound for M*. The localized martingales then converge at every time in L1, dominated by the integrable M*, so the martingale conditional-expectation identities pass to the limit. This proves the assertion. The weak L2 step itself follows by applying optional stopping to the nonnegative submartingale equal to the squared increment norm. No sharp BDG constant is claimed or needed.

The numerical8 here is only an integrability bound. It introduces NO factor8, sqrt8 or any other loss in the attenuation level below.

## 3. Noise-energy observability gives SAME-level deterministic-mean necessity

Consider the finite algebraic condition

    [A0  B0]=Lambda [D0  D1]                            (NEO)

for some constant matrix Lambda. Equivalently the kernel of[D0 D1] is contained in the kernel of[A0 B0]; this is a finite linear-system test. In particular NEO holds for arbitrary A0,B0 whenever the full performance Gram matrix is positive definite (equivalently R>0 and Q>0). It is not asserted for every plant.

**Theorem 2 — universal necessary bridge on the NEO domain.** Suppose NEO holds and one admissible nonlinear law has G1(F)<=g. For EVERY deterministic counted input w, there is a deterministic causal control map V:w↦vbar, with zero response to zero data, whose mean state obeys

    xbar'=Abar xbar+B vbar+C w(t-h),   xbar(0)=0,
    ||(Q^(1/2)xbar,R^(1/2)vbar)||_L2 <=g ||w||_L2.        (2)

This map is consistent across inputs and causal in the input w. It is a necessary mean-history problem, NOT by itself a printed state/window implementation.

**Proof.** For a deterministic input with finite output N1, NEO gives

    A0 x+B0 u=Lambda z,
    E (integral|A0 x+B0 u|^2)^(1/2)
        <=||Lambda|| N1(z)<infinity.

Lemma1 therefore makes its stochastic integral a true H1 martingale. Equation(1) makes v integrable as an L2-valued random variable. In transformed coordinates,

    x(t)=integral_0^t(Abar x+Bv+Cw(s-h))ds+M(t).

Pathwise Gronwall bounds sup|x| by a finite deterministic constant times `||v||_L2+||w||_L2+M*`. Its expectation is finite. Consequently all drift expectations may be interchanged with integration, E M=0, and the mean ODE in(2) follows.

The Hilbert-valued random variable `(Q^(1/2)x,R^(1/2)v)` has path norm exactly||z|| by(1), and is Bochner integrable. Convexity of the Hilbert norm gives

    ||(Q^(1/2)E x,R^(1/2)E v)||_L2
       <=E||(Q^(1/2)x,R^(1/2)v)||_L2
       =N1(z)<=g||w||_L2.

There is NO squaring of a random N1 denominator: deterministic test inputs have N1(w)=||w||_L2 exactly. Coupling two deterministic inputs that agree up to time t with the same Brownian path and using the fixed law's nonanticipativity/strong well-posedness gives identical response histories up to t. Taking means preserves that agreement, so V is causal. No linearity or differentiability of F was used. On an infinite horizon apply the mean argument on each finite interval and the Hilbert norm bound to increasing truncations; the same necessary bound follows for deterministic inputs and the full output. QED.

The existence of V is not the missing general controller-realization theorem. It can depend on past input information not recoverable from current x and the current preview window. The next sections close that direction only on explicitly stated subclasses.

## 4. A deterministic strict Riccati converse for ALL causal nonlinear controls

The following lemma is proved here to avoid importing an unproved assertion that nonlinear policies are no better than linear ones.

**Lemma 3.** Fix finite T>0, constant Abar,B,C,Q>=0,R>0 and prescribed gamma>0. If a causal deterministic control map V with zero response to zero data gives the zero-state system

    x'=Abar x+B V(w)+Cw,
    ||(Q^(1/2)x,R^(1/2)V(w))||_L2 <=g||w||_L2,
    g<gamma,                                               (3)

then the terminal Riccati equation

    -Pdot=Abar^T P+P Abar+Q
           +P(gamma^(-2) C C^T-B R^(-1)B^T)P,
    P(T)=0                                                 (RDE)

has a bounded symmetric solution on the CLOSED interval[0,T]. Conversely any such solution gives a state-feedback law with strict deterministic induced gain<gamma. No continuity, incremental Lipschitz bound, differentiability, stationarity, finite-dimensional realization or linearity of V is assumed.

### 4.1 Exact squares and positivity on a maximal existence interval

The finite-dimensional polynomial ODE has a unique local symmetric solution backward from T. On any compact part[s,T] of its maximal interval, direct differentiation gives, for arbitrary L2 controls and inputs,

    J_gamma := integral_s^T(x^TQx+v^TRv-gamma^2|w|^2)
      =a^T P(s)a
       +integral_s^T |R^(1/2)(v+R^(-1)B^TPx)|^2
       -gamma^2 integral_s^T |w-Hx|^2,
    H(t)=gamma^(-2) C^TP(t),   x(s)=a.                    (4)

The terminal term vanishes because P(T)=0. For w=0 choose the bounded linear feedback v=-R^(-1)B^TPx. Its cost J is nonnegative, whereas(4) is at most a^TP(s)a. Hence P(s)>=0 everywhere it exists. This argument requires no adversarial feedback loop and no dynamic-programming regularity theorem.

### 4.2 A uniform supply upper bound from the unknown nonlinear policy

Restrict V to inputs zero before s. Causality and zero response give a zero-initial-state map V_s on[s,T] with the SAME bound g. For an arbitrary initial a, use the SAME input-functional control v=V_s(w), without changing its dependence on w. Its state is exactly

    x(t)=x_zero(t)+exp(Abar(t-s))a.

Let M0 be any uniform bound, for s∈[0,T], on the L2 norm of `Q^(1/2)exp(Abar(t-s))a` divided by|a|. For example `sqrt(T)||Q^(1/2)||exp(||Abar||T)` works. Therefore, writing W=||w||_L2, X=|a| and d=gamma^2-g^2>0,

    J_gamma <=(gW+M0 X)^2-gamma^2 W^2
             <=-(d/2)W^2+C0 X^2,
    C0=M0^2(1+2g^2/d).                                    (5)

Also(3) implies `||V_s(w)||_L2<=gW/sqrt(lambda_min(R))`. The state ODE then gives a uniform Sobolev bound

    ||x||_H1(s,T)<=K_T(W+X),                              (6)

where K_T depends on fixed plant/T/g/R but NOT on s,P or any regularity of V. This uses the ordinary variation-of-constants and derivative estimates, not an incremental bound on V.

### 4.3 A finite sample-and-hold adversary avoids a hidden well-posedness assumption

An arbitrary nonlinear V need not remain well posed in an instantaneous feedback loop w=Hx. We do NOT assume that loop exists. On a finite partition s=t0<...<tN=T define recursively

    w(t)=H(t_k)x(t_k),   t_k<=t<t_(k+1).                 (7)

At each step, previous input segments determine the state x(t_k); causality determines the control on the next segment independently of any later extension. Each finite prefix can be extended by zero and is an admissible L2 input to V. Its response has finite L2 control and continuous state by(3). Induction therefore defines the finite partition input, with finite values/energy, without a fixed-point or policy-continuity assumption.

H is C1 on the fixed compact interval[s,T]. The elementary Sobolev sampling estimate gives

    ||w-Hx||_L2 <=c_H max_mesh ||x||_H1.

Indeed on one cell use `|x(t)-x(t_k)|^2<=mesh*integral_cell|x'|^2`; the variation of H is bounded by its C1 norm. Summing also bounds sampled state values by the L2 and derivative norms. Together with(6), choosing the finite mesh small enough gives, for ANY chosen epsilon>0,

    ||w-Hx||_L2<=epsilon(W+X).                           (8)

No response convergence as the mesh changes is asserted or needed. No partition was executed/enumerated by a program.

### 4.4 No finite-time Riccati blow-up is compatible with strict gain

For the input(7), the nonnegative control square in(4) and(8) give

    J_gamma>=a^TP(s)a-2gamma^2 epsilon^2(W^2+X^2).

Choose epsilon so `2gamma^2 epsilon^2<=d/4`. Combine with(5):

    a^TP(s)a<=-(d/4)W^2+(C0+d/4)X^2
              <=(C0+d/4)|a|^2.                         (9)

Thus `0<=P(s)<=(C0+d/4)I` uniformly on its entire maximal backward interval. The sampling constant may depend on that compact interval, but the FINAL bound does not. A finite-dimensional polynomial ODE cannot have a finite escape endpoint while its solution remains in a bounded set; its derivative is also bounded there. It therefore extends to and through any proposed endpoint before0, and to0 itself. This proves the converse. It uses only the original strict gap d, not an assumed optimal policy or a policy linearization.

### 4.5 Bounded RDE gives a UNIFORM STRICT gain at this SAME gamma

Set v=-R^(-1)B^TPx and a=0. Identity(4) becomes

    ||(Q^(1/2)x,R^(1/2)v)||_L2^2
        =gamma^2||w||_L2^2-gamma^2||r||_L2^2,
    r=w-Hx.                                               (10)

Let Acl=Abar-BR^(-1)B^TP. Since w=r+Hx, the state satisfies

    x'=(Acl+CH)x+Cr,  x(0)=0.

All coefficients are bounded on[0,T]. If `K=sup||Acl+CH||`, Young's convolution estimate gives

    ||x||_L2<=||C|| T exp(KT)||r||_L2,
    ||w||_L2<=M||r||_L2,
    M=1+||H||_infinity ||C|| T exp(KT)>=1.                (11)

Substituting in(10) gives gain at most

    gamma sqrt(1-M^(-2)) < gamma.                         (12)

For M=1 the bound is0. Thus no unproved strictness at the boundary gamma, compactness assertion or gamma-epsilon replacement is hidden in the sufficient direction. This completes Lemma3.

## 5. Exact finite-dimensional Hamiltonian form

For the RDE of Lemma3 put

    M_gamma=gamma^(-2)CC^T-BR^(-1)B^T,
    H_gamma=[[Abar,M_gamma],[-Q,-Abar^T]],
    [X_gamma(t);Y_gamma(t)]
       =exp((t-T)H_gamma)[I;0].                           (13)

Then a bounded terminal RDE solution exists on[0,T] IF AND ONLY IF

    det X_gamma(t) !=0 for EVERY t in the CLOSED[0,T].    (HAM)

When it exists, `P=Y_gamma X_gamma^(-1)`. To verify this, differentiating the block flow gives X'=Abar X+M_gamma Y, Y'=-QX-Abar^TY and hence the RDE for YX^-1. The conserved identity X^TY=Y^TX makes P symmetric. Conversely a bounded RDE solution makes X solve the fundamental equation X'=(Abar+M_gamma P)X with terminal I, so X is invertible; Y=PX then obeys precisely the displayed Hamiltonian flow. This proves both directions without a guessed determinant computation.

HAM is a finite-dimensional constant-matrix exponential condition at the actual gamma, not a controller-existence restatement. It is NOT claimed to be a finite list of sampled-time determinant checks, an executed test, or a finite LMI for every general plant.

## 6. SAME-gamma stochastic N&S and PRINTED realization at h=0

**Theorem 4.** Fix finite T>0, h=0, gamma>0, R>0 and actual constant plant data satisfying

    A0+B0 K0=0,                                          (MATCH)
    B0 R^(-1) B^T=0.                                     (ORTH)

Then the following are equivalent:

- Some admissible printed state/current-input law has literal G1(F)<gamma.
- Some consistent causal nonlinear history law has literal G1(F)<gamma.
- RDE at THIS gamma is bounded on[0,T].
- HAM at THIS gamma holds on the closed interval.

An explicit printed realizer is

    u(t)=(K0-R^(-1)B^TP_gamma(t)) x(t).                  (14)

It uses state and deterministic time only, hence certainly the allowed information. The theorem is finite-horizon attenuation; no separate infinite-horizon stability assertion is attached to this time-varying law.

**Necessity.** MATCH implies NEO with the explicit factor

    Lambda=B0 R^(-1)D1^T,
    Lambda D1=B0,   Lambda D0=-B0K0=A0.

So Theorem2 converts ANY feasible nonlinear history law to a deterministic causal map satisfying(3) for some g<gamma. Lemma3 supplies RDE; §5 supplies HAM. This never assumes that the mean-history map itself is printed-realizable.

**Sufficiency and realization.** For(14), transformed v=-R^(-1)B^TPx and actual diffusion is

    A0x+B0u=(A0+B0K0)x-B0R^(-1)B^TPx=0

by MATCH and ORTH. Thus the ACTUAL stochastic plant, for every progressive input, has the pathwise ordinary dynamics used in Lemma3. Each sample input is L2 on the finite interval. Equations(10)–(12) apply SAMPLE BY SAMPLE, with one deterministic constant below gamma. Taking expectation preserves N1 on BOTH sides and gives strict literal gain<gamma. The bounded linear state law is strongly well posed, causal, event-local and zero on zero data. There is no stochastic N2 equivalence premise, extra energy state or unproved realization direction. This proves all equivalences.

ORTH allows genuinely effective drift and diffusion actuators in different cost-orthogonal directions. For example, with real constants b,alpha,beta nonzero and arbitrary a,c,d, take

    n=1,m=2,p=3,
    B=(b,0), B0=(0,beta), A=a, A0=alpha, C=c,
    D0=(d,0,alpha/beta)^T,
    D1=[[0,0],[1,0],[0,1]].

Then R=I, K0=(0,-alpha/beta)^T, Q=d^2, Abar=a, MATCH/ORTH hold, and both actuation matrices and A0 are nonzero. The exact scalar criterion is

    -Pdot=2aP+d^2+(gamma^(-2)c^2-b^2)P^2, P(T)=0,

bounded on[0,T], with printed realizer `u1=-bPx,u2=-alpha*x/beta`. This is a structural illustration of the n-dimensional theorem, not a new endpoint example offered instead of synthesis.

**Broader necessary conclusion.** Even without MATCH/ORTH, if NEO holds and h=0, literal feasibility implies RDE/HAM by Theorem2 and Lemma3. In particular this necessary condition applies to arbitrary A0,B0 whenever Q>0,R>0. It is NOT sufficient for those general noises, because the explicit feedback need not erase them.

## 7. Positive-preview sharp synthesis for the matched B=0 class

There is an exact positive-preview result, not only a no-preview boundary theorem.

**Theorem 5.** Suppose B=0, R>0 and MATCH holds. Let h>=0 and T>h be finite, and put L=T-h. Define the deterministic Volterra operator

    (G_L w)(s)=Q^(1/2) integral_0^s exp(A(s-r))Cw(r)dr,
    0<=s<=L,
    m_L=||G_L||_(L2->L2).                                (15)

Then the INFIMUM literal gain over every admissible printed law, or even every consistent causal nonlinear history law, is EXACTLY m_L, and is ATTAINED by the static printed law

    u=K0x.                                               (16)

Consequently literal strict synthesis at the prescribed gamma is equivalent to the B=0 RDE/HAM on the CLOSED interval[0,L]. The test uses Abar=A and terminal P(L)=0, at gamma itself.

**Necessity, including all preview pre-action.** MATCH gives NEO. For any controller with finite gain and any deterministic input, Theorem2 gives

    xbar'=A xbar+Cw(t-h),

because B=0. Hence the mean state is zero before h and equals the deterministic convolution in(15), shifted by h, afterwards. The mean control cannot change it. Jensen and the nonnegative R-control term give N1(z)>=||G_Lw||. Taking the deterministic-input supremum gives G1(F)>=m_L. Controls before h have NOT been reset or forbidden; they may create random state but cannot change this mean, because their diffusion is H1. A law of infinite gain already satisfies the lower bound trivially.

**Sufficiency.** For(16), v=0, diffusion=0 by MATCH, and the actual pathwise output norm is exactly||G_Lw||, with the same h-shift. Therefore `N1(z)<=m_L N1(w)` for ALL progressive inputs, with no additional input information or energy. Deterministic inputs approach the norm, so the achieved gain is exactly m_L. This proves both the sharp value and its printed realization.

Finally m_L<gamma is equivalent to the B=0 RDE test: apply Lemma3 with the zero deterministic control map for necessity, and its strict Volterra inverse argument for sufficiency. HAM is §5 with terminal time L. No unspecified optimization over controllers or quadratic-objective surrogate remains in this subclass criterion.

## 8. Infinite positive preview: an exact SAME-gamma LMI on that class

Now suppose B=0, R>0, MATCH and A Hurwitz, and fix any finite h>=0. Define G_infinity by the convolution in(15) on[0,infinity), and let m_infinity be its deterministic L2 operator norm. Exponential decay makes this norm finite.

The same mean lower bound, first on finite output intervals and then by monotone convergence, gives `G1(F)>=m_infinity` for EVERY controller. The static law(16) gives pathwise `||z||<=m_infinity||w||` and hence equality of the optimal literal gain with m_infinity. The delay is a pure time shift on the infinite interval and changes neither bound. The law's zero-input dynamics are dx=A x dt, so it is internally exponentially mean-square stable. This conclusion includes arbitrary positive preview and all progressive finite-expected-energy disturbances.

**Theorem 6.** On this class the following are equivalent at the SAME prescribed gamma>0:

- Literal G1<gamma synthesis, with the static realizer(16).
- m_infinity<gamma.
- A symmetric P>0 exists such that the FINITE-DIMENSIONAL LMI

        [[A^TP+PA+Q,  PC],
         [C^TP,       -gamma^2 I]] <0.                  (LMI)

Here is a proof of the LMI equivalence, rather than an unexamined stochastic bounded-real import.

**LMI sufficiency.** Strict negativity persists with the SAME P when gamma is replaced by some eta<gamma sufficiently close. Schur complement gives

    A^TP+PA+Q+eta^(-2)PCC^TP<0.

Along the deterministic pathwise state equation, storage differentiation/completion gives the ordinary energy bound `||G_infinity w||<=eta||w||`; integrate first on finite intervals, discard the nonnegative terminal storage, and pass to infinity. Thus m_infinity<=eta<gamma. This applies pathwise under(16), so preserves the literal criterion exactly.

**LMI necessity.** Suppose m_infinity<gamma. Since A is Hurwitz, the deterministic state convolution w↦x also has a finite L2 norm m_x. Choose eta with m_infinity<eta<gamma and epsilon>0 small enough that

    m_infinity^2+epsilon*m_x^2<eta^2.

Put Q_epsilon=Q+epsilon I. Its uncontrolled zero-state gain is uniformly less than eta on EVERY finite horizon. The finite B=0 RDE at eta with Q_epsilon therefore exists on every horizon tau by Lemma3. The uniform supply bound in(5)–(9) uses a constant M0 bounding the homogeneous output `Q_epsilon^(1/2)exp(At)a` on[0,infinity); A Hurwitz makes this bound finite independently of tau. Hence these terminal Riccati initial values P_tau(0) are uniformly bounded.

For clarity, they are also the exact uncontrolled deterministic max-game values. Completion(4), now with B=0 and no control, bounds every supply by a^TP_tau(0)a. Equality is achieved by the bounded linear input feedback `w=eta^(-2)C^TP_tau(t)x`; its deterministic linear ODE is well posed on the finite interval, giving an ordinary L2 input. Extending a shorter-horizon input by zero only adds nonnegative later Q_epsilon output cost. Therefore P_tau(0) is monotone nondecreasing with tau and has a finite limit P_infinity.

The time-homogeneous Riccati flow has P_tau(0)=S(tau), where

    S'=A^TS+SA+Q_epsilon+eta^(-2)SCC^TS, S(0)=0.

Continuity of this finite-dimensional flow implies its monotone bounded limit is an equilibrium: for every fixed r, S(tau+r)=Flow_r(S(tau)) and both limits agree, so Flow_r(P_infinity)=P_infinity. Consequently

    A^TP_infinity+P_infinity A+Q+epsilon I
       +eta^(-2)P_infinity CC^TP_infinity=0.              (17)

The zero input is an allowed competitor in the max-game. Thus P_infinity dominates the strictly positive homogeneous Gramian with Q_epsilon, and P_infinity>0. Evaluating its Schur expression at gamma gives

    A^TP_infinity+P_infinity A+Q
       +gamma^(-2)P_infinity CC^TP_infinity
      =-epsilon I-(eta^(-2)-gamma^(-2))
                    P_infinity CC^TP_infinity <0.

The Schur complement is exactly LMI. This proves its necessity, including the strict prescribed level, with no numerical ARE computation or stochastic mean-square replacement.

If desired, ordinary Fourier Plancherel identifies m_infinity with the stable transfer norm of `Q^(1/2)(sI-A)^(-1)C`; that identification is not needed for the proved LMI equivalence. No A-unstable infinite-horizon synthesis assertion is made here.

## 9. Why this is not the forbidden reformulation or an assumed linear optimum

- Theorem2 ALONE is a lower problem on deterministic mean histories and is labelled only necessary. No claim is made that its control map is a printed controller.
- Lemma3 proves the finite-horizon nonlinear-to-Riccati implication using only causal consistency, a strict gain and finite-dimensional state estimates. It does not assume a differentiable tangent, a linear optimal controller, a quadratic value-function ansatz, a smooth Isaacs solution, policy compactness, or a well-posed instantaneous adversarial feedback against an arbitrary nonlinear law.
- Theorem4's actual realizer is state-only. Its Brownian coefficient is checked to vanish algebraically; the literal gain then follows pathwise at the SAME gamma with a UNIFORM STRICT buffer. It is not an enlarged-memory implementation.
- Theorem5/6 realizer is static. The lower bound includes all preview pre-action and arbitrary nonlinear causal histories, so the exact value is not obtained by restricting an optimization to linear laws.
- The required special conditions are on the ACTUAL plant matrices. They are not assumptions that the desired arbitrary-plant controller happens to be linear, stationary, smooth or optimal.
- None of these statements says N1 and N2 are generally equivalent. The previous separated families are outside any attempted universal objective substitution; here diffusion vanishes only under the explicitly constructed laws, while necessity is independently derived from literal N1.

## 10. Sources, imports and actual verification boundary

Actual book images re-read: `information-science/stochastic-hinf-preview-control/sources/book/pdfpage-0695.png`,0696,0697, printed pp674–676. They confirm the constant matrices, current preview-window information, h NONNEGATIVE, expectation outside the path norm, and separate finite/infinite questions. No terminal-state penalty was inserted; RDE has terminal0 because this target has none.

The locally retained Wang2014 printed p102 was also read: its displayed quadratic expectation and terminal penalty are a DIFFERENT objective/information discussion, and NO theorem from that page is used as literal synthesis. The book's Tadmor–Mirkin2005 and Kojima–Ishijima2006 deterministic-preview citations were observed. A bounded source check read the [KTH Tadmor differential-games abstract](https://www.math.kth.se/optsyst/seminars/tadmor.html) and the [author publication listing](https://aerospace.technion.ac.il/person/leonid-mirkin/); neither is a read of the full deterministic positive-preview N&S proof. That theorem is therefore NOT imported to fill the remaining positive-preview realization gap. Search/access limitations are not treated as evidence of novelty or absence of an existing theorem.

Named ordinary imports: construction/localization of Brownian Itô integrals, stopped Itô isometry and optional stopping for the squared increment norm; Bochner expectation/Jensen and Fubini; finite-dimensional spectral square roots, Gronwall, Sobolev sampling, Young convolution bounds and matrix-ODE existence/uniqueness/continuation; Hurwitz exponential decay. The needed H1 estimate, deterministic strict Riccati converse, Hamiltonian equivalence and strict LMI argument have their operative proofs above. Fourier Plancherel is named only for the optional frequency interpretation. No uncertain preview-Riccati literature theorem or sharp probability-transfer constant is hidden in a necessity or realization direction.

All new claims are owner-WRITTEN CANDIDATES pending fresh full-body reconstruction and parent import disposition. No interpreter arithmetic, symbolic matrix calculation, finite partition execution, determinant sampling, LMI solve, numerical RDE/ARE, simulation or certificate replay was performed. No formal/kernel/human/configured-family/executable/novelty acceptance is claimed. Prior process findings stay permanent. This packet makes no continuous18-way runtime or96-hour completion claim.

## 11. ENTIRE original residual and first unproved next bridge

The original target remains arbitrary constant A,B,C,A0,B0,D0,D1, prescribed gamma, arbitrary finite positive preview/horizon or infinity, and the full printed law class.

The following are STILL OPEN here:

1. For general noise not controlled by output (NEO fails), finite N1 output alone has not been shown to justify the deterministic-mean martingale step. Additional state/control coercivity may restore it, but no such universal condition is proved.
2. Even on NEO data, the deterministic mean-history map has NOT generally been converted into an admissible state/current-window stochastic controller. Theorem4 closes this only for h=0 plus MATCH/ORTH; Theorem5/6 close arbitrary h only for B=0 plus MATCH (and A Hurwitz on infinity).
3. Genuine h>0 with nonzero drift control B, arbitrary noncancellable multiplicative noise, rank-deficient R, and the general infinite-horizon internal-stabilization/necessity direction remain unclosed. A known deterministic preview theorem may aid the matched/orthogonal subclass, but its exact all-causal quantifiers and printed-window realization need an ACTUAL source-body check or a new proof; the abstract/listing is not that check.
4. The attained subclass values, finite Riccati/Hamiltonian tests and infinite B=0 LMI are NOT a general stochastic LMI criterion, a universal stationary/linear-feedback optimality theorem, a same-level N1/N2 equivalence, or a full-book solution. No novelty/priority claim is made.

The next genuinely general obligation is a same-level NECESSITY-and-realization representation for the missing plant/information classes, not another refinement of the already supported finite-expression separating family. The unchanged October27 science cutoff/deadline and HOLD remain binding.
