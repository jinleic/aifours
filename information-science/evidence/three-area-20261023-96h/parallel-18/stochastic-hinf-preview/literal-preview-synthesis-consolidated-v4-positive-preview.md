# Literal stochastic synthesis — finite and infinite positive-preview realization on named matched/orthogonal classes

**InfoHinfPreview-2 / info-3. ONE immutable consolidated WRITTEN successor; OWNER CANDIDATE, not accepted.** Actual immediately preceding `/bin/date` observation: **Sun Oct 25 11:31:39 PDT 2026**, an observed precreation bound, not an invented exact creation time.

## 0. What is NEW, and the exact non-widened claim

This removes v3's h=0 restriction for its matched/orthogonal finite-horizon synthesis theorem. For EVERY prescribed finite T>h>=0 and gamma>0 on the exact constant-data class below, literal N1 feasibility over ALL nonlinear printed laws is equivalent to an explicit **2n-dimensional piecewise constant Hamiltonian graph condition at THAT SAME gamma**. A time/state/current-preview-window law is given explicitly. No extra controller memory is used. Necessity does not assume differentiability, linear optimality, stationarity, a smooth game value or a well-posed instantaneous adversarial feedback against a nonlinear law.

On the infinite horizon, with the ADDITIONAL actual-data assumptions that(Abar,B) is stabilizable and(Abar,Q^(1/2)) detectable, §10 proves a separate exact finite-dimensional algebraic Riccati feasibility criterion with a strict scalar margin at the prescribed gamma. Its printed stationary window law is internally exponentially mean-square stable. This infinite argument is integrated before the first source pin, not inferred from a horizon-uniform Volterra inverse.

This is still a CLASS theorem, not the original arbitrary-diffusion/rank-deficient N&S problem. Its complete original residual is in §13. The new proofs do not refine the Robin example and do not square the printed stochastic objective.

The primary102319 ACK preceded new work. After actual v80-B return, a LATER source-exposure ACK addendum was written BEFORE this new body, in `primary-continuation-20261025-102319-ack-addendum-1.json`. It discloses a newly read old deterministic-limit kernel lead and informal calculations, without backdating the original ACK or pretending the old mean-square theorem solves literal synthesis. V9/v10/v11 and HOLD remain binding. No scientific interpreter/eval/program, symbolic arithmetic, enumeration, ODE/ARE solve, determinant sampling, solver/replay, compilation, external-model CLI or nested agent was used. All identities are WRITTEN, not machine-checked.

Predecessors remain immutable:

- Supported expression-level family v2: SHA256 `d1e367cff5a4098c60bd0e44226eec72b7c91ce7a69c538c1b680fc043e22173`; not used as a mathematical lemma here.
- New v3 mean/H1/h0 synthesis candidate,385LF: SHA256 `331214d982b2926c2e37b79fb69851980ec3ff74b6c67f98d26a5322c92a6dfc`; not silently edited or treated as accepted. Its separate B=0 infinite-horizon claim is not a premise of either new finite/infinite proof here.
- Later read-only lead `information-science/stochastic-hinf-preview-control/work/theory.md`, SHA256 `78446859c16cad9a6ca26f580986fc84405a1301e61e7db1594f362b8e0ce806`: actual renewed reads COMPLETE RAW1–347 and509–554 only, not infinite-horizon348–508. Its mean-square F1 substitution, historical reviews and numerics are NOT imported as literal necessity. The deterministic kernel algebra needed here is rederived below, and its old converse is replaced by the new sample-and-hold argument.

## 1. Exact plant, criterion, information and algebraic domain

Use the actual book model

    dx=(A x+B u+C w(t-h))dt+(A0 x+B0 u)dW,
    z=D0 x+D1 u,

with real constant matrices, scalar Brownian W, zero initial data/negative input history, finite T>h>=0, and progressive disturbances with finite expected squared energy. Count input ONLY on[0,L], L=T-h, and output on[0,T]. Values outside the counted input window are zero as in the frozen precision convention; the law below explicitly ignores any uncounted tail. The literal criterion is

    G1(F)=sup_(w!=0) E||z_F,w||_L2(0,T) / E||w||_L2(0,L)
           < gamma.                                      (1)

Finite-horizon deterministic time dependence F_t is allowed by the frozen convention. The printed information is current x(t) and current window w(r),t-h<=r<=t; an energy-history or arbitrary-memory implementation is NOT granted. One fixed causal, event-local, strongly well-posed law is used consistently for all inputs, with zero response on zero data. Necessity may enlarge to consistent causal history laws; existence must actually supply the printed form.

Set

    R=D1^T D1>0,
    K0=-R^(-1)D1^T D0,
    Q=D0^T D0-D0^T D1 R^(-1)D1^T D0>=0,
    Abar=A+B K0,
    D=B R^(-1)B^T,
    v=u-K0 x.

Then exactly

    |z|^2=x^TQx+v^TRv.                                  (2)

The THEOREM domain is the following finite algebraic class:

    A0+B0K0=0,                                           (MATCH)
    B0R^(-1)B^T=0.                                       (ORTH)

Both B and B0, and also A0, may be nonzero. ORTH separates useful drift/noise actuator directions in the performance metric; it is a condition on actual matrix data, not an assumed linear optimum.

For the broader necessary statement, replace MATCH/ORTH by the finite factorization condition

    [A0 B0]=Lambda[D0 D1] for some constant Lambda.       (NEO)

MATCH implies NEO with Lambda=B0R^(-1)D1^T. General noncancellable NEO data are NOT claimed sufficient.

## 2. The literal-to-mean necessary step, with H1 rather than N2 controls

Here is the complete operative bridge, independently of an objective replacement. A continuous local martingale M satisfies

    E sup_(t<=T)|M_t| <=8 E(trace[M]_T)^(1/2)

whenever the right side is finite. The needed nonsharp H1 fact follows by localization and the good-lambda bound

    P(M*>2lambda,S<=delta lambda)<=delta^2P(M*>lambda),
    S=(trace[M]_T)^(1/2).

Stop at first norm lambda, then stop the increment at additional quadratic variation delta^2 lambda^2. Conditional stopped Itô isometry and the weak L2 maximal inequality bound its probability of an increment lambda by delta^2. Integrating the good-lambda inequality gives `(1/2-delta^2)E M*<=E S/delta`; delta1/2 gives8. Apply to increasing norm/quadratic-variation stops, pass by monotone convergence, and dominate the localized martingales by the resulting integrable M*. Thus M is a true uniformly integrable martingale and E M_t=0. This constant is used ONLY for integrability, never as an attenuation loss.

Suppose NEO holds and one nonlinear law has G1(F)<=g<gamma. Test ANY deterministic w on the counted interval. Finite literal output gives

    E (integral|A0x+B0u|^2)^(1/2)
       <=||Lambda|| E||z|| <infinity.

Thus its diffusion integral has mean zero by the H1 argument. By(2), v is an L1(Omega;L2)-valued variable. Gronwall on

    x(t)=integral_0^t(Abar x+Bv+Cw(s-h))ds+M_t

gives E sup|x|<infinity. Fubini and Bochner Jensen therefore imply

    xbar'=Abar xbar+B vbar+Cw(t-h),  xbar(0)=0,
    ||(Q^(1/2)xbar,R^(1/2)vbar)||_L2(0,T)
        <=E||(Q^(1/2)x,R^(1/2)v)||_L2
         =E||z|| <=g||w||_L2(0,L).                      (3)

No N2(u) assumption was made, and the denominator is deterministic ONLY because this is a permitted deterministic test. Two deterministic inputs agreeing up to t give identical response histories under the same Brownian path/seed and fixed causal law; taking means preserves causality. Hence vbar=V(w) is ONE consistent deterministic causal control map. It need not be a printed state/window law and is NOT presented as one.

If zero response is interpreted first as zero OUTPUT, (2) and NEO make zero-data v and diffusion zero, then the zero-initial mean-free state equation forces x=u=0 as well. Thus restriction to an input prefix zero before s has the required zero state/control history. No controller reset is introduced.

The rest of the necessity proof uses ONLY this deterministic causal mean map, not a stochastic mean-square synthesis theorem.

## 3. Finite-dimensional deterministic preview equation at gamma

Define constant Hamiltonian matrices

    H0=[[Abar,-D],[-Q,-Abar^T]],
    Jgamma=[[0,gamma^(-2)CC^T],[0,0]],
    Hgamma=H0+Jgamma,
    Hh=exp(-hH0) Hgamma exp(hH0).                       (4)

Let E,F be the first block-column matrices of exp(-hH0):

    exp(-hH0)=[[E,*],[F,*]].

The preview Riccati is the PIECEWISE FINITE-DIMENSIONAL ODE

    -Pdot=Abar^TP+PAbar+Q-PDP+gamma^(-2)k(t)k(t)^T,
    P(T)=0,
    k(t)=(P(t)E-F)C  for 0<=t<=L,
    k(t)=0            for L<t<=T.                       (PRE)

The last window is plain LQ, not the preview Hamiltonian. On the early interval the expanded coefficients are

    Ah=Abar-gamma^(-2)E CC^T F^T,
    Qh=Q+gamma^(-2)F CC^T F^T,
    Mh=gamma^(-2)E CC^T E^T-D,
    -Pdot=Ah^TP+PAh+Qh+P Mh P.                         (5)

So there is no unknown future-P kernel in this deterministic equation. Symplecticity gives precisely the conjugation Hh in(4); it is NOT exp(-hHgamma) transport and is NOT applied after L.

Equivalently solve the explicit2n-dimensional graph flow

    [X;Y](t)=exp((t-T)H0)[I;0],              L<=t<=T,
    [X;Y](t)=exp((t-L)Hh) exp(-hH0)[I;0],    0<=t<=L.   (6)

The exact condition is

    det X(t) !=0 for EVERY t in the CLOSED[0,T].          (HAM-PRE)

Then P=YX^(-1). To check the conjugation algebra, the symplectic inverse of exp(-hH0) has bottom row[-F^T,E^T], so conjugating Jgamma adds blocks

    [[-gamma^(-2)E CC^TF^T,  gamma^(-2)E CC^TE^T],
     [-gamma^(-2)F CC^TF^T,  gamma^(-2)F CC^TE^T]],

exactly(5). The usual graph derivative gives PRE. Conversely bounded PRE gives a fundamental invertible X through X'=(Ah+MhP)X early and the corresponding H0 equation late, with Y=PX. Thus PRE boundedness and HAM-PRE are equivalent. The conserved relation X^TY=Y^TX makes P symmetric. This is an explicit finite-dimensional matrix-exponential/ODE condition at the prescribed gamma, not sampled determinants or an unexecuted claim of a numerical solve.

## 4. Operative K/M algebra, with all signs and boundaries

Put Phi(t,s)=exp((t-s)H0), with blocks Phi_ab. For t<=s,r<=min(t+h,T), define

    K(t,s)=(P(t)Phi11(t,s)-Phi21(t,s))C,
    m(t,s)=k(t)^T Phi11(t,s)C,
    M(t,s,r)=C^T Phi22(s,t)K(t,r)
                 +1_(r<s) C^T Phi21(s,r)C.             (7)

Let f(s)=w(s-h), the ACTUAL forcing signal, and define known-window quantities

    g(t)=integral_t^min(t+h,T) K(t,s)f(s)ds,
    mu(t)=integral_t^min(t+h,T) m(t,s)f(s)ds.             (8)

For t>L use k=m=0; all incoming terms then vanish because no counted w enters. The two auxiliary policies are

    v_star=-R^(-1)B^T(Px+g),
    w_star=gamma^(-2)(k^Tx+mu),    0<=t<=L.              (9)

Here f denotes delayed forcing and v the transformed control; they are not the same signal.

Write Acl=Abar-DP. The kernel identities are

    K(t,t)=PC,
    partial_t K=-Acl^T K-gamma^(-2)k m,                 (K)
    M(t,s,r)^T=M(t,r,s),
    M(t,t,r)=C^T K(t,r),
    M(t,s,t+h)=m(t,s)^T     when t+h<=T,                (MB)
    partial_t M=K(t,s)^T D K(t,r)
                      -gamma^(-2)m(t,s)^T m(t,r).     (MD)

They are rederived here, not inherited from an old stochastic theorem.

For K, differentiate Phi with H0. One obtains

    partial_t K=(Pdot+P Abar+Q)Phi11 C
                         +(Abar^T-PD)Phi21 C.

Subtract -Acl^TK. PRE makes the remaining coefficient `-gamma^(-2)kk^T Phi11 C=-gamma^(-2)k m`. K(t,t)=PC is immediate.

For M symmetry, the P-term is symmetric after exchanging s,r by the symplectic inverse. For r<s the remaining needed block identity is

    Phi22(s,t)Phi21(r,t)^T+Phi21(s,r)
        =Phi21(s,t)Phi22(r,t)^T.

Expand Phi(s,t)=Phi(s,r)Phi(r,t). The two residual brackets are `Phi11 Phi22^T-Phi12 Phi21^T=I` and `Phi21 Phi22^T-Phi22 Phi21^T=0`, exactly symplecticity. The diagonal follows from the second bracket. This proves symmetry, including the indicator term and its sign. The lower boundary is immediate from Phi22(t,t)=I. The upper boundary follows directly from

    M(t,s,t+h)=C^T Phi22(s,t)k=m(t,s)^T,

using Phi11(t,s)^T=Phi22(s,t); symmetry supplies the opposite order used for the incoming integral.

For MD, differentiate Phi22(s,t):

    partial_t Phi22(s,t)=Phi21(s,t)D+Phi22(s,t)Abar^T.

Using K gives the first coefficient `(Phi21(s,t)+Phi22(s,t)P)D K`, which is `K(t,s)^T D K` by the inverse blocks. The remaining coefficient is `-gamma^(-2)C^T Phi22(s,t)k m=-gamma^(-2)m(t,s)^T m(t,r)`. The indicator term has no t derivative. This checks every identity needed for the value calculation.

On the terminal plain-LQ window, its graph equation gives `P(t)Phi11(t,T)=Phi21(t,T)`, hence K(t,T)=0. In particular k(L)=0 when h>0, consistent with the no-new-input terminal window. No Dirichlet-like terminal change or extra tail input was inserted.

## 5. Exact deterministic preview squares

Consider the deterministic dynamics

    x'=Abar x+Bv+C f(t).

Define the purely auxiliary quadratic functional

    Vcal(t)=x^TPx+2x^Tg
       +integral integral f(s)^T M(t,s,r) f(r)dsdr,      (10)

over the current window[t,min(t+h,T)]. It is NOT an added controller state and no global positivity of Vcal on arbitrary window histories is assumed.

For L2 input, the moving integrals are absolutely continuous. Away from the irrelevant endpoints, their derivatives have incoming f(t+h)=w(t), outgoing f(t), and kernel derivatives. In detail

    gdot=k w-K(t,t)f(t)+integral partial_tK f,
    Ndot=2w^Tmu-2f(t)^T integral M(t,t,r)f(r)dr
                       +integral integral f^T partial_tM f,

where N is the double-integral term and the incoming terms are zero after L. Differentiating x^TPx+2x^Tg and adding the running supply makes the outgoing-forcing terms cancel by K(t,t)=PC and M(t,t,r)=C^TK(t,r). Complete the v-square and w-square. The x-x remainder is PRE, the x-window remainder is K, and the window-window remainder is MD. Thus exactly

    dVcal/dt+x^TQx+v^TRv-gamma^2|w|^2
      =|R^(1/2)(v-v_star)|^2
                          -gamma^2|w-w_star|^2,         (11)

with the w term counted only through L. There is no Brownian term: this is a DETERMINISTIC algebraic identity, applied to the mean auxiliary problem or to a diffusion-free realized path.

At T, Vcal=0. At a starting time s with initial state a and ZERO initial preview forcing window (equivalently w zero before s), Vcal(s)=a^TP(s)a. Hence

    J_gamma=a^TP(s)a+integral_s^T|R^(1/2)(v-v_star)|^2
                        -gamma^2 integral_s^L|w-w_star|^2. (12)

If s>=L there is no remaining disturbance integral. No positivity of a general window value is needed.

## 6. Converse for ANY nonlinear causal mean control, not an assumed optimum

**Lemma.** If one consistent deterministic causal map V has zero-state gain at most g<gamma for the delayed system in §5, with input counted[0,L] and output[0,T], then PRE is bounded on the CLOSED[0,T].

First PRE has local backward solutions. Its terminal window is ordinary LQ. On any existence interval choose zero forcing/history and v=v_star=-R^(-1)B^TPx. The nonnegative cost in(12) is at most a^TP(s)a; therefore P(s)>=0. On the plain-LQ terminal window one may also choose v=0 to upper bound P by the finite homogeneous cost, so the solution extends across the whole[L,T]. Early PRE is the constant-coefficient polynomial Riccati(5); it can fail to continue only by unbounded norm.

Restrict V to an input zero before s<L, giving V_s and the SAME zero-state gain g. For arbitrary initial a, use the SAME input-functional v=V_s(w), not a purported printed controller initialized with new memory. Its state is its zero-state response plus exp(Abar(t-s))a. If W=||w||_L2(s,L), X=|a|, and M0 uniformly bounds the homogeneous output, then

    J_gamma<=(gW+M0X)^2-gamma^2W^2
             <=-(d/2)W^2+C0X^2,
    d=gamma^2-g^2>0, C0=M0^2(1+2g^2/d).                (13)

Also the R-control term gives `||V_s(w)||<=gW/sqrt(lambda_min(R))`. Variation of constants therefore gives

    ||x||_H1(s,T)<=K_T(W+X),                            (14)

uniformly in s and independently of P, since delayed input has the SAME L2 norm W. No continuity or incremental Lipschitz property of V is needed.

On a compact Riccati existence interval[s,T], the coefficients k,K,m and their relevant derivatives are bounded. Express the auxiliary input in current-input coordinates:

    w_star(t)=H(t)x(t)+integral_max(s,t-h)^t J(t,r)w(r)dr,
    H=gamma^(-2)k^T,
    J(t,r)=gamma^(-2)m(t,r+h),     s<=t<=L.             (15)

All integral endpoints carry ordinary L2 boundary values; there is no direct pointwise w(t) term in w_star itself. Differentiation of the moving integral puts w(t),w(t-h) only in its L2 derivative. Consequently

    ||w_star||_H1(s,L)<=C_P(W+X).                       (16)

Construct a finite partition of[s,L] recursively and take

    w(t)=w_star(t_k),  t_k<=t<t_(k+1).                 (17)

Each sample uses only x(t_k) and ALREADY known past input integrals. A finite prefix can be extended by zero to evaluate the causal map V_s; its control/state are finite by the gain and ODE bounds. Thus the construction is well defined without an instantaneous adversarial feedback-loop assumption. The H1 sampling inequality and(16) give

    ||w-w_star||_L2(s,L)<=max_mesh*C_P(W+X).

Choose the finite mesh to make this at most epsilon(W+X), with `2gamma^2 epsilon^2<=d/4`. No response convergence as partitions change is used; every constructed input individually is admissible. Equation(12), discarding its nonnegative control square, and(13) imply

    0<=a^TP(s)a<=-(d/4)W^2+(C0+d/4)X^2
                  <=(C0+d/4)|a|^2.                    (18)

The FINAL bound is independent of s,P and any potential escape point. P>=0 and this uniform bound exclude finite escape for the polynomial early ODE, so PRE extends to0. This proves necessity for ALL causal nonlinear maps using only strict gain and causality, not a quadratic value ansatz, linear optimality, differentiability or extra controller information.

Together with §2, NEO and literal feasibility imply PRE/HAM-PRE for arbitrary finite h. This broader statement is only NECESSARY when MATCH/ORTH do not hold.

## 7. Strict SAME-gamma deterministic realization and the Volterra inverse

Suppose PRE is bounded. Use v=v_star in(9) from zero state/history. Its dynamics are a finite-time linear ODE with a known moving-window input integral. All coefficients are bounded and it is strongly well posed. Identity(12) becomes

    ||(Q^(1/2)x,R^(1/2)v)||_L2(0,T)^2
        =gamma^2||w||_L2(0,L)^2
                 -gamma^2||w-w_star||_L2(0,L)^2.        (19)

To obtain UNIFORM STRICT gain at gamma, not merely <=gamma, write w_star=mathcal D w under this realized controller. It is a bounded STRICT Volterra operator on[0,L]. Here is the operative estimate: bounded K gives `|g(t)|<=c integral_0^t|w(r)|dr`. The state ODE `x'=(Abar-DP)x-Dg+Cw(t-h)` and Gronwall give `|x(t)|<=c_T integral_0^t|w(r)|dr`; zero negative input was used. Formula(15) therefore gives

    |(mathcal D w)(t)|<=c_D integral_0^t|w(r)|dr.        (20)

There is no direct feedthrough of current w, despite the available current preview. Iterating(20) and using Young's inequality proves

    ||mathcal D^n|| <=(c_D L)^n/n!.

Thus the operator series `sum_(n>=0) mathcal D^n` converges in norm, is the TWO-SIDED bounded inverse of I-mathcal D, and has norm at most exp(c_D L). It remains causal. In particular

    ||w||<=M||w-w_star||,  M=exp(c_D L)>=1.             (21)

Substitution in(19) gives induced gain at most

    gamma*sqrt(1-M^(-2)) <gamma.                        (22)

If c_D=0 the bound is0. No numerical inverse, stationary limit, compactness argument or unstated gamma-epsilon criterion is used. This is a finite-horizon strictness proof at the prescribed gamma itself.

## 8. Actual stochastic realization uses EXACTLY the printed window

Define, with zero extension outside the counted interval,

    g(t)=integral_max(0,t-h)^min(t,L) K(t,r+h)w(r)dr,
    u(t)=K0 x(t)-R^(-1)B^T(P(t)x(t)+g(t)).              (23)

Every input value used lies in the current printed window[t-h,t]. There is no stored input-energy state, remote past outside that window, future Brownian information or auxiliary controller-memory implementation. Kernels and time are deterministic design data.

Under MATCH/ORTH the ACTUAL diffusion is exactly

    A0x+B0u=(A0+B0K0)x
                -B0R^(-1)B^T(Px+g)=0.

Thus for EVERY progressive disturbance the actual state solves the deterministic ODE of §5 path by path. Each counted sample input is L2 almost surely. Equations(19)–(22) apply to each path with the SAME deterministic constant below gamma, and(2) identifies the actual output norm. Taking expectations preserves BOTH literal N1 norms. Strong existence/uniqueness, causality, event locality and zero response follow from the bounded linear finite-time construction. No N2 transfer theorem or probability constant is needed in this sufficient direction.

## 9. Exact finite-horizon N&S theorem, with actual nonzero channels

**Theorem.** Fix ANY real constant plant data, finite T>h>=0 and gamma>0 satisfying R>0, MATCH and ORTH. Then the following are equivalent:

1. There is a printed state/current-window law with literal gain G1<gamma.
2. There is even a consistent causal nonlinear history law with literal gain G1<gamma.
3. PRE at that SAME gamma is bounded on the CLOSED[0,T].
4. The explicit2n-dimensional HAM-PRE condition(6) holds on the CLOSED[0,T].

The realizer is(23). Necessity is the H1/Jensen step plus the sample-and-hold converse; sufficiency is actual diffusion cancellation plus the strict Volterra inverse. A mean-history law is never passed off as an implementation.

The class genuinely permits nonzero drift and diffusion actuation and nonzero state-dependent noise. For example

    B=(b,0), B0=(0,beta), A=a, A0=alpha, C=c,
    D0=(d,0,alpha/beta)^T,
    D1=[[0,0],[1,0],[0,1]],

with b,beta,alpha nonzero gives R=I, K0=(0,-alpha/beta)^T, Q=d^2, Abar=a and MATCH/ORTH. The controller's second component cancels alpha*x noise, while the first controls the drift and includes the actual preview integral. The n-dimensional theorem, not this illustration, is the result. No numerical coefficient or finite witness was sought.

For h=0, E=I,F=0, g=0 and PRE/HAM-PRE reduce EXACTLY to the v3 finite-horizon theorem. For B=0, v_star=0 and(23) is static u=K0x, agreeing with v3's positive-preview sharp-convolution result. The theorem is finite-horizon attenuation; it does NOT assert infinite-horizon internal stability of this horizon-dependent law.

**Broader necessary corollary.** Under R>0 and NEO, without MATCH/ORTH, any literal-feasible law must satisfy the SAME finite-dimensional PRE/HAM-PRE test. For Q>0,R>0, the full performance Gram matrix is positive definite, so NEO holds for arbitrary A0,B0. This necessary result is not sufficient for arbitrary noncancellable multiplicative noise.

## 10. Infinite positive preview with nonzero B: an exact algebraic criterion on an S/D class

This section is an additional NEW argument, integrated in the unpublished draft BEFORE its first hash/return. It does not read or import the old mean-square source's infinite-horizon348–508, renewal/SFDE theorem, Krein–Rutman premise or numerical limits.

Retain R>0, MATCH, ORTH and constant data. Assume additionally:

    (Abar,B) is stabilizable,
    (Abar,Q^(1/2)) is detectable.                       (SD)

These are the usual finite-dimensional conditions: the first supplies a constant F0 with Abar+BF0 Hurwitz; the second excludes every Abar eigenvector of nonnegative real part annihilated by Q^(1/2). Equivalently they have the finite PBH rank tests. They are stated DOMAIN restrictions, not asserted consequences for arbitrary stochastic plants.

Fix ANY finite h>=0 and the prescribed gamma>0. In the following criterion E,F remain the first block column of exp(-hH0), using the ACTUAL Abar,Q,D; they do not depend on the scalar margin:

    There exist a real scalar rho>gamma^(-2) and P=P^T>=0
    such that, with k=(PE-F)C,

    Abar^TP+PAbar+Q-PDP+rho*k*k^T=0.                    (ARE-PRE)

This is a FINITE-DIMENSIONAL algebraic Riccati-type feasibility condition, including one strict scalar inequality. It is not claimed convex or a general stochastic LMI. Writing eta=rho^(-1/2), the scalar inequality means eta<gamma EXACTLY; it is the strict-level quantifier, not a fixed-factor loss or a different requested objective.

**Infinite-horizon theorem.** On R>0/MATCH/ORTH/SD, a printed state/current-window law with G1<gamma and internal exponential mean-square stability exists IF AND ONLY IF ARE-PRE is feasible. In fact even a gain-feasible consistent causal nonlinear history law already implies ARE-PRE on this data domain. An explicit admissible realizer is given below.

### 10.1 Necessity: uniform finite values from a nonlinear literal-feasible law

Suppose a law has literal gain at most g<gamma. MATCH gives NEO, so the H1/Jensen argument, on each finite interval and then increasing output truncations, gives ONE deterministic causal mean map with

    ||(Q^(1/2)xbar,R^(1/2)vbar)||_L2(0,infinity)
        <=g||w||_L2(0,infinity)

for every deterministic compactly supported input. No state/window realization of that mean map is assumed. Choose eta with g<eta<gamma, and apply the already PROVED finite converse at eta for every finite terminal T. The input is genuinely stopped at T-h; output up to T is bounded by the full infinite output. Nothing is reset.

To make the no-blowup bound UNIFORM in T, use stabilizability in(SD). For an artificial initial state a, take the zero-initial mean control plus F0*xi, where

    xi'=(Abar+BF0)xi, xi(s)=a.

The actual deterministic state is exactly x_zero+xi. The homogeneous performance pair is(Q^(1/2)xi,R^(1/2)F0xi), whose L2 norm on the WHOLE future half-line is at most M_infinity|a|, uniformly in s,T. Thus(13)–(18) hold with this M_infinity and d=eta^2-g^2. The sampling constants may depend on the individual finite T, but their FINAL matrix bound does not. Consequently the finite terminal initial matrices P_T(0) at eta are uniformly bounded and nonnegative.

For the limit argument, their game-value monotonicity is established rather than assumed. On a fixed finite interval, the known linear v_star and the equation w=w_star from arbitrary a and zero history have a unique solution: the finite Volterra inverse of §7 solves its affine right-hand side. Call the pair(v_degree,w_degree). Then(12) gives

    J(v_degree,w_degree;a)=a^TP_T(0)a.

For this FIXED deterministic input w_degree, put p=P_T*x_degree+g_degree. Direct differentiation using K and PRE gives

    p'=-Abar^Tp-Qx_degree+k(w_degree-w_star)
       =-Abar^Tp-Qx_degree,
    p(T)=0,  B^Tp+R*v_degree=0.

For any other L2 control, integration by parts on p^T*delta_x cancels the first variation. Therefore

    J(v,w_degree;a)-J(v_degree,w_degree;a)
       =integral(delta_x^TQ delta_x+delta_v^TR delta_v)>=0.

So a^TP_T(0)a is a lower-game value sup_w inf_v J: it is attained from below by w_degree, and v_star's(12) bounds the infimum for EVERY w from above by the same number. This is a calculation for fixed known linear extremals, not an assumption that the unknown nonlinear law is optimal.

If T2>T1, extend a T1 counted input by zero to the T2 counted interval. For any longer control, its restricted T1 cost is at least the shorter control infimum, and its remaining output cost is nonnegative. The input penalty is unchanged. Taking infima and then suprema proves

    P_T2(0)>=P_T1(0).

Together with the uniform bound this gives a finite nonnegative limit P_eta. Time-homogeneity makes S(T)=P_T(0) solve the plain-LQ forward Riccati up to duration h and the AUTONOMOUS forward version of(5), at eta, after h. Local existence and continuity of the finite-dimensional polynomial flow in a neighbourhood of this bounded limit give, for every sufficiently small fixed r>=0,

    Flow_r(P_eta)=lim_(T->infinity) S(T+r)=P_eta

Differentiating this local fixed-point identity at r=0 makes P_eta an equilibrium; the constant equilibrium then extends for all r. Thus no global-flow existence at an untested limit point is assumed, and

    Abar^TP_eta+P_eta Abar+Q-P_eta D P_eta
          +eta^(-2)(P_eta E-F)CC^T(P_eta E-F)^T=0.

With rho=eta^(-2)>gamma^(-2), this is ARE-PRE. No numerical convergence, stationary-policy assumption on the unknown controller, stochastic ARE theorem or uniform finite inverse was used.

### 10.2 Detectability gives actual closed-loop stability

Take ANY P>=0 solving ARE-PRE and let Acl=Abar-DP. Its exact Lyapunov identity is

    Acl^TP+PAcl+Q+PDP+rho*k*k^T=0.                      (24)

If Acl had an eigenvector a with Re(lambda)>=0, evaluation on that complex vector would make every term nonnegative. Hence Q^(1/2)a=0 and B^TPa=0 (as well as k^Ta=0). Thus DPa=0 and Acl*a=Abar*a. Detectability in(SD) rules out this nonstable Abar eigenvector. Therefore Acl is Hurwitz. This needs neither P>0 nor an unproved general stochastic stabilizing-solution theorem.

### 10.3 A stationary printed controller and transversality, not an infinite inverse assumption

Define lag kernels for0<=tau<=h:

    K_h(tau)=[P,-I]exp(-tau H0)[C;0],
    k=K_h(h),
    m_h(tau)=k^T[exp(-tau H0)]11*C.

The realizer is

    g(t)=integral_0^h K_h(tau)w(t-h+tau)dtau,
    u(t)=K0x(t)-R^(-1)B^T(Px(t)+g(t)).                 (25)

It uses ONLY current state and[t-h,t] input, with zero negative history. MATCH/ORTH make actual diffusion zero. Its state matrix is the just-proved Hurwitz Acl. The finite-window kernel maps L2 inputs to L2 g, and the stable state convolution maps the delayed input and g to L2 x. Thus all realized state/control/performance signals are square integrable path by path for every L2 sample input.

The stationary versions of K,M satisfy precisely §4's identities with gamma^(-2) replaced by rho, because ARE-PRE supplies the x-x identity. The window functional Vcal has the bound

    |Vcal(t)|<=c*(|x(t)|^2+integral_(t-h)^t|w(r)|^2dr).

For each L2 sample input the sliding window energy tends to0. Stable convolution of an L2 forcing tends to0 pointwise, by approximation with compactly supported inputs and the exponentially decaying L2 kernel. Hence x(t)->0 and Vcal(t)->0. This is an actual transversality proof for the REALIZED law, not global positivity of a window value.

With eta=rho^(-1/2), the stationary identity integrates on[0,S] as

    integral_0^S(|z|^2-eta^2|w|^2)
       =-Vcal(S)-eta^2 integral_0^S|w-w_star|^2,

since Vcal(0)=0. All L2 terms converge, and the proved transversality gives

    ||z||_L2(0,infinity)<=eta||w||_L2(0,infinity)

PATH BY PATH. Taking expectations gives literal gain at most eta<gamma. With w=0 and zero input history, g=0 and dx=Acl*x dt, so arbitrary initial states decay exponentially in mean square. This proves the prescribed-level performance AND internal stability, without an unproved infinite-horizon inverse bound, worst-loop SFDE spectral theorem or stochastic norm replacement.

The infinite criterion is therefore exact on its stated class. No claim is made outside(SD), for rank-deficient R, or for noise not canceled by MATCH/ORTH.

## 11. Source/representation audit and what was NOT assumed

The original book pp674–676 were actually read; h is nonnegative, matrices constant, the expectation is OUTSIDE the pathwise time norm, input ends at T-h, and the law has current state/current preview window. No terminal-state penalty was added, so P(T)=0. Explicit finite-horizon time dependence follows the frozen interpretation, not a new stationarity assumption.

The old scoped mean-square substitute's deterministic-limit algebra was a LATER supplied lead, pinned/covered in §0 and the exposure addendum. Every operative K/M sign, symmetry, boundary, derivative and completion identity needed for this theorem has been rederived in §§4–5. The old stochastic necessity, stochastic advanced-P equation, historical computations, renewal/SFDE theorem and external review headlines are NOT premises. In the deterministic auxiliary case H0 is constant, which is WHY the finite graph test is valid; this is not claimed for the general stochastic Riccati equation.

The bibliographic follow-up resolved [Tadmor–Mirkin2005 PartI, DOI10.1109/TAC.2004.840460](https://doi.org/10.1109/TAC.2004.840460) and [Kojima–Ishijima2006, DOI10.1109/TAC.2006.886485](https://doi.org/10.1109/TAC.2006.886485) through exact-title Crossref metadata. The old source catalog's Tadmor DOI was explicitly UNVERIFIED and is not adopted. The linked publisher PartI PDF returned HTTP418; OpenAlex reported closed/no OA location. These access/metadata observations are not full theorem-body reading or proof that no source is accessible elsewhere. NO deterministic preview theorem was imported from an abstract or listing to fill a realization gap; the finite bridge is proved above.

Ordinary named imports: Brownian Itô construction/localization, stopped isometry/weak L2 maximal inequality, Bochner Jensen/Fubini, Gronwall, finite-dimensional matrix ODE continuation, symplectic matrix identities, Sobolev sampling, Young convolution, Hurwitz exponential decay and the usual finite-dimensional stabilizability/detectability equivalences. Their operative nontrivial uses are displayed, including the H1 good-lambda argument, finite Volterra inverse, uniform finite-value limit and infinite transversality proof. The criteria contain finite-dimensional matrix exponentials/ODEs or algebraic Riccati feasibility, not an unknown controller-existence oracle. HAM-PRE is an all-time graph condition, NOT sampled determinant checks or an executed certificate.

Not assumed: linear/nonlinear policy optimality equivalence, differentiability of the candidate controller, stationarity, a Markovization of energy-history control, a smooth Isaacs value, a nonlinear adversarial feedback-loop existence theorem, an accepted old stochastic necessity theorem, or an objective N1/N2 replacement. No scientific code or replay ran. Written mathematics is not formal/kernel proof or independent-family/human/executable/novelty acceptance.

## 12. Status of preceding results and review gates

The385LF v3 stays frozen at its delivered owner-candidate scope. The new full finite-positive-preview and infinite(SD) theorems are NOT automatically accepted by a review frozen against v3 or its h0 source; they require actual reading/reconstruction of THIS complete source, its later exposure and every new kernel/converse/inverse/value-limit/transversality step. The infinite section was integrated while v4 was still an unpublished, unpinned draft; no earlier frozen file was edited or review chronology backdated.

A LATER exposure occurred after both finite and infinite v4 arguments had been drafted but BEFORE its first hash/return: the COMPLETE227LF actual v82-B review of V3, `physics/evidence/three-area-20261023-96h/parallel-18/werner3-ququart/peer-review-preview-literal-mean-realization-v3.md`, SHA256 `064722e5df35eb63dc32ea9295e7cba36326686bfba3df2ea7de2f7193e80b93`, was read RAW1–120/121–227. It reports0F/0M/0m at V3's exact h0/B=0 subclass scope, not the new v4 claims. Its local-flow explanation motivated explicitly stating the small-r continuation qualification above before the first v4 freeze. No V3 source was edited, no parent disposition is inferred, and this exposure is not backdated into either earlier proof or ACK.

V3's separate B=0, A Hurwitz infinite-horizon LMI remains that separate candidate domain. The nonzero-B infinite(SD) result above has its OWN new proof and does not inherit acceptance from that special case. The older v2 expression-level separation remains separately supported, without expanded digits or executable credit. These domains must not be silently unioned into an unrestricted arbitrary-diffusion theorem.

## 13. ENTIRE original residual and first unproved general step

The registered primary is STILL arbitrary constant A,B,C,A0,B0,D0,D1, prescribed gamma, finite and infinite horizons, and the printed controller information.

What is NOW proved only as an owner-WRITTEN CANDIDATE is exact finite-horizon synthesis for ALL h>=0 on R>0/MATCH/ORTH, an exact infinite-horizon algebraic criterion and printed internally stable realizer on that class with(SD), and a broader finite-dimensional necessary finite-horizon test on NEO data. The positive-preview nonzero-B realization gap is closed ONLY on those explicitly named plant domains.

STILL OPEN here:

- Arbitrary noncancellable multiplicative noise, including NEO data where(23) does not erase diffusion. PRE is then only a mean lower test, not a general sufficient stochastic criterion.
- Plants failing NEO, where finite literal output has not generally been shown to force a true diffusion martingale, and rank-deficient R/unpenalized control directions.
- General infinite-horizon necessity, realization and internal stabilization OUTSIDE the stated matched/orthogonal(SD) class, including removal of those extra S/D assumptions, remain unclosed. Finite graph existence or its inverse alone does not supply an infinite result; §10 required a separate uniform-value and transversality proof.
- Full arbitrary-plant literal N&S synthesis, globally optimal nonlinear laws and novelty/priority. No part of the current subclass theorem is a book-problem cutover or an unqualified N1/N2 equivalence.

The next genuinely general step must handle the remaining noncancellable-noise, rank-deficient or outside-SD infinite-realization obstruction while retaining prescribed gamma and actual information. Another Robin endpoint refinement is not that step. Fresh full-body same-harness review/parent import disposition and every stronger human/configured-family/formal/executable/novelty gate remain separate and unperformed for this source. Original October27 cutoff/deadline, v1–v11 and scientific HOLD are unchanged; this packet does not complete the96-hour round.
