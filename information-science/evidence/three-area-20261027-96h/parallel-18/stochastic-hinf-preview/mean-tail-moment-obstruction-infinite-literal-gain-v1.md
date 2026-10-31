# Finite all-matrix mean-tail conditions necessary for infinite literal feasibility

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:51:00 PDT 2026**. This is a class-level necessity/obstruction for a GIVEN law in the entire bound linear class. It does NOT solve the conditions for controller parameters, construct a diffusion-annihilating controller or use the stopped C1-C3/R4/v209 route. No new source or scientific execution.

## 1. Entire original plant/law and exact finite test

Fix arbitrary compatible real original matrices, positive dimensions, finite h>=0, zero state/history and ONE bound deterministic stationary linear preview law with K,L0,Lh,H in the supplied spaces. For the infinite comparison use canonical progressive globally E2 disturbances and the consistent local strong solution, with control E2 on every finite interval. Extra original global-control-energy/internal-stability eligibility is not inferred; the obstruction applies in particular to any law satisfying stronger eligibility.

Put

`P=A+BK`, `Q=A0+B0K`, `O=D0+D1K`,

`Rw=L0w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`.

Let Pi_+ be the REAL spectral projection of P onto the sum of its generalized eigenspaces with Re(lambda)>=0. It commutes with P. The complementary projection contains only strictly left-half-plane eigenvalues. This is the ordinary finite Jordan decomposition, not a performed spectral computation or a stability assumption.

Define the actual mean-tail matrix

`M_h = B L0 + exp(-Ph)(B Lh+C) + integral_0^h exp(-Pr) B H(r)dr`. (M)

At h=0 this is `B(L0+Lh)+C`, with no kernel, exactly the combined-tap convention.

**Theorem.** The following are equivalent:

1. The actual deterministic-input mean-output map is bounded from L2[0,infinity) to L2[0,infinity).
2. Its output belongs to L2 for EVERY compactly supported deterministic L2 input.
3. The FINITE matrix identities hold:

   **O P^j Pi_+ M_h=0 for j=0,...,n-1.**                     (C)

If (C) fails, there is an analytic family of ACTUAL compactly supported deterministic E2 disturbances with non-L2 mean output. Consequently the fixed law has **G_det,infinity=G_prog,infinity=infinity** at the ORIGINAL expected-path-norm criterion. Thus (C) is necessary for every finite prescribed-gamma infinite literal feasibility claim in the stated class.

When (C) holds, only the MEAN channel is proved bounded. It is NOT a sufficient stochastic literal-gain/synthesis condition, and no law is selected or constructed from it.

## 2. Paid actual expectation and complete head/tail formula

For any deterministic input, the bound original closed loop has E2 state/control on each finite interval by the permitted linear-SDE theorem and bounded preview operators. Hence its actual Itô integral has zero mean on each such interval, by simple-predictable approximation/isometry. The actual mean solves

`x_bar'=P x_bar+B Rv+C v(t-h)`, `z_bar=O x_bar+D1 Rv`.

This does not assume globally E2 control or a drift-only mean for an arbitrary nonintegrable local policy.

The mean output has direct atoms D1L0 at delay zero and D1Lh at delay h. Its ordinary kernel is

`k(t)=O exp(Pt)B L0`

`+ 1_(t>=h) O exp(P(t-h))(B Lh+C)`

`+ O integral_0^(min(h,t)) exp(P(t-r))B H(r)dr`

`+ 1_(0<=t<=h)D1 H(t)`.

This follows by the ordinary linear ODE formula and deterministic Fubini, with all finite-interval integrability paid by H in L2. For t>h its exact tail is simply

**k(t)=O exp(Pt) M_h.**                                      (T)

The head on [0,h] is L1 (bounded finite exponential factors and H in L2 on a finite interval). No physical regulated output is changed; the mean is used solely for a justified lower estimate on the original norm.

## 3. Sufficiency for the MEAN channel, with every nonstable mode included

By Cayley-Hamilton, (C) is equivalent to `O exp(Pt)Pi_+ M_h=0` for every t: powers of P at and above n reduce to the preceding n powers, and the exponential series converges on each compact interval. Conversely differentiation at zero gives the finite powers.

Under (C), (T)'s only remaining observable tail is `O exp(Pt)(I-Pi_+)M_h`. The finite Jordan form makes this a finite sum of polynomial times exponentially decaying terms, hence L1 on [h,infinity). The head is already L1, and the direct atoms are bounded shifts. Young's elementary L1-kernel/L2 estimate proves a finite mean-operator norm. This gives 3->1->2, including arbitrary repeated/nilpotent eigenvalues, singular channels and Pi_+=0.

No claim that the INTERNAL state is stable follows. Nonstable state components may be unobservable in this mean output, and Q/B0 noise may affect actual fluctuations even when the mean is bounded.

## 4. Failure supplies an ACTUAL all-variable deterministic obstruction

If (C) fails, choose any j and a real nonzero input direction e with `O P^j Pi_+ M_h e!=0`. Such a direction exists by finite linear algebra. Consider the whole symbolic pulse family

`v_epsilon(s)=(1/epsilon)e 1_[0,epsilon](s)`, `epsilon>0`.

Each input is deterministic, canonical-progressive and globally E2 with finite positive norm. No pulse width, state or control is chosen for a numerical diagnostic.

For t>h+epsilon all direct/finite-window head output has ended. The ACTUAL mean tail is

`z_bar_epsilon(t)=O exp(Pt) J_epsilon M_h e`,

`J_epsilon=(1/epsilon) integral_0^epsilon exp(-Ps)ds`.

The matrix J_epsilon commutes with P and Pi_+, and tends to I as epsilon decreases to zero. Thus

`O P^j Pi_+ J_epsilon M_h e -> O P^j Pi_+ M_h e !=0`.

For ALL sufficiently small positive epsilon the observed nonstable component is nonzero. It is a finite nonzero exponential polynomial with eigenvalues of real part >=0, so is not L2 on the half-line. The ordinary finite-Jordan fact used here follows by grouping the greatest exponential growth/degree and using the positive long-time mean square of a nonzero finite trigonometric sum; decaying lower groups cannot cancel it. The stable component is L2 and cannot cancel this non-L2 component. Hence z_bar_epsilon is not L2, proving 2->3 by contraposition.

For every finite prefix the actual output satisfies `E||z_epsilon||_[0,t]>=||z_bar_epsilon||_[0,t]` by the expectation triangle inequality. Let t grow and apply monotone convergence to the ORIGINAL path norms. The right side diverges, so `E||z_epsilon||_[0,infinity)=infinity`. The disturbance denominator is finite and positive, giving an actual infinite literal ratio. This pays the physical caller rather than inferring an output from a formal pole or a mean relaxation.

## 5. Scope, degeneracies and why this is not controller construction

The finite test includes all closed-right-half-plane eigenvalues, not merely positive real eigenvalues; imaginary-axis/Jordan terms are covered. For n=1 only j=0 is needed; for Pi_+=0 the conditions are vacuous and only mean boundedness follows. If O or M_h vanish the observable tail vanishes directly. h=0 and every singular/rank-deficient matrix case use the displayed exact formulas; no inverse or controllability hypothesis is inserted.

For fixed K the conditions are affine equalities in the ALREADY GIVEN feedforward coefficients/kernel. This paper only tests necessity and proves failure causes infinite gain. It does NOT solve those equalities, choose gains to cancel modes, propose an implementation or authorize the stopped realization/diffusion-annihilating controller branch. In particular bounded mean is not silently promoted to a stochastic N&S criterion; Q remains completely unrestricted and untested by this mean condition.

The result supplies an original-object infinite-horizon obstruction over the entire bound matrix/law class. It does not certify book admissibility, globally E2 control, internal EMS, arbitrary nonlinear full-information policies, a sharp finite gain or general prescribed-gamma synthesis. Source comparison confirms displayed formulas only; all additional domain choices remain explicit.

Named facts and uses: allowed finite-prefix linear-SDE well-posedness/isometry zero mean; ordinary matrix-exponential ODE formula and deterministic Fubini; finite real Jordan spectral decomposition/Cayley-Hamilton; L1-kernel Young bound and the stated elementary exponential-polynomial L2 criterion; prefix norm monotonicity and expectation triangle inequality. No Riccati/storage/Gramian, stochastic-flow/dual guide, old packet, new source, scientific interpreter/CAS/enumeration/solver, selected diagnostic/model CLI/nested agent occurred. All old process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP, source-render/copyright and parent physics-2 L1 quarantine controls persist; written only, no parent/peer/formal/kernel/executable/human/configured-family/novelty acceptance.
