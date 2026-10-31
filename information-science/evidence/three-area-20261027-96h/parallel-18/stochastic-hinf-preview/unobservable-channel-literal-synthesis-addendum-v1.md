# Finite matrix conditions extend the exact literal synthesis class

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:14:24 PDT 2026**. This append-only continuation extends `noise-only-actuation-literal-synthesis-v1.md`, SHA-256 `204345d091c0c22f08984e72abe9bc0f601dfe2cf0ef55b411923e1fb4da06ea`, by a new actual-state coupling argument. No new source, program, numerical probe, replaced performance output, storage/Gramian or controller realization is used. The earlier late-ACK PROCESS MINOR and all source/process limitations persist.

## 1. All-matrix statement, including nonzero B and A0

Keep arbitrary positive dimensions, finite T>h>=0, S=T-h, zero initial state/history, zero-extended canonical progressive E2 disturbances and the exact bound deterministic stationary linear full-information preview controller class. Now use the ORIGINAL plant

`dx=[Ax+Bu+Cw(t-h)]dt+[A0x+B0u]dW`, `z=D0x`,

where A,B,C,A0,B0,D0 are arbitrary real compatible matrices satisfying only

**D0 A^j B=0 and D0 A^j A0=0, for j=0,...,n-1.**               (U)

D1 remains zero. B and A0 need not themselves be zero; B0 is completely unrestricted. There is no invertible coordinate transformation, rank condition, positivity assumption or added state feedback premise.

Let V_A and sigma be exactly the original-output deterministic convolution operator/norm in the preceding theorem:

`(V_A v)(r)=D0 integral_0^r exp(A(r-s)) C v(s)ds`, `r in [0,S]`.

**Theorem.** Under (U), for every prescribed gamma>0, both pointwise-strict and uniform-strict literal feasibility in the bound controller class hold iff gamma>sigma. The same explicit original-information controller u=0 attains `inf_F G_prog=inf_F G_det=sigma`. At A=0 this is the explicit condition `gamma>2(T-h)||D0C||/pi`.

These are sufficient structural hypotheses for this synthesis theorem, not necessary hypotheses for all original solvable plants. No failure of (U) is asserted to imply infeasibility.

## 2. Why the finite conditions cover the whole original dynamic channel

The ordinary Cayley-Hamilton identity says that, for the characteristic polynomial `p_A(lambda)=lambda^n+sum_(j=0)^(n-1) alpha_j lambda^j`,

`A^n=-sum_(j=0)^(n-1) alpha_j A^j`.

Multiplying and iterating shows that (U) annihilates D0 A^j B and D0 A^j A0 for every integer j>=0, not just the displayed finite list. Conversely vanishing for all j implies the displayed list. This also makes `D0 exp(At)B=D0 exp(At)A0=0` for every t by the uniformly convergent exponential series on compact intervals. The proof below uses a finite actual-state stack instead of any stochastic-convolution/change-of-measure theorem.

The subspace `N=intersection_(j=0)^(n-1) ker(D0 A^j)` is A-invariant by the same identity, and (U) is equivalently `range(B)+range(A0) subset N`. This describes the condition only; no reduced plant or altered output criterion is substituted into the problem.

## 3. Actual-state stack pays both required callers

For the ORIGINAL actual solution X define actual linear functions

`Y_j=D0 A^j X`, `j=0,...,n-1`.

This is an internal proof device, not a new physical state/controller or a new performance output. The criterion remains exactly `z=Y_0=D0X`, with its original norm and expectation. Define fixed matrices `C_j=D0 A^j C` and `G_j=D0 A^j B0`.

Multiplication of the original SDE by each constant matrix D0 A^j, with (U), gives for j<n-1

`dY_j=[Y_(j+1)+C_j w(t-h)]dt+G_j u dW`,

and for the last index

`dY_(n-1)=[-sum_j alpha_j Y_j+C_(n-1)w(t-h)]dt+G_(n-1)u dW`.  (3)

There is no term from Bu or A0X left in these equations. They are exact identities for the original process, including the n=1 case (only the last equation). They require no inverse stack map and remain true when D0 or the stack is singular/zero.

Every bound controller is finite-horizon E2-admissible: substituting its K and bounded preview feedforward operator into the full original plant gives constant linear drift A+BK, diffusion A0+B0K and progressive E2 forcing. The permitted linear-SDE existence/uniqueness estimate, or the explicit isometry/integral-inequality bound in the current robustness addendum, gives E2 state/control/output and strong nonexplosive well-posedness. Thus the stochastic integrals in (3) have zero mean, paid by E2 rather than assumed for merely local controls.

For a deterministic v, taking expectations in the finite stack yields the deterministic companion-block linear ODE with forcing C_j v(t-h), independent of the chosen law. Its zero-start solution is exactly the stack obtained from `dot x_bar=A x_bar+C v(t-h)`. In particular,

`E z_t=D0 integral_0^t exp(A(t-s)) C v(s-h)ds`.

The original-output norm inequality therefore gives `E||z||>=||V_A v||` for every law and every deterministic v. Taking the full deterministic supremum gives **G_prog(F)>=G_det(F)>=sigma**.

For the explicit u=0, the stochastic terms in the finite stack (3) vanish IDENTICALLY. The stack is then the ordinary pathwise linear ODE driven by the actual possibly random input w, so its first component is the deterministic convolution V_A applied to each input path, after the original h time shift. The original state may still be stochastic in its unobservable components; no assertion of a deterministic whole state is needed.

Consequently `||z(omega)||<=sigma||w(omega)||` almost surely and u=0 attains both gain infima. This pays the upper actual caller without deriving a universal stochastic pathwise solution map or importing a state-noise cancellation guide.

## 4. Strict endpoint, all degeneracies and remaining boundary

The deterministic kernel V_A is exactly the same finite-horizon compact operator as in the preceding proof. Its norm is finite and, if positive, attained by an actual deterministic L2 input. That proof explicitly pays compactness, its norm-attaining caller, the pointwise-strict endpoint, and the A=0 closed form without any new source. Thus no law can meet pointwise strictness at gamma=sigma>0, while u=0 works with a common margin for gamma>sigma. If sigma=0 the given gamma is positive and u=0 works directly.

All ranks of B,A0,C,D0, all kernel dimensions, n=1, zero matrices, arbitrary B0 and unstable A over a finite horizon are included. The argument uses each of the n finite channel identities; it does not assert that checking only j=0 would suffice when n>1. The choice of horizon/controller quantifiers is unchanged and no infinite-horizon stability claim is made.

This removes the earlier theorem's B=A0=0 restriction by exact finite structural conditions, while retaining the original output and proving both common-law callers. It does NOT solve the general original problem when control drift or state noise can affect the observed dynamic channel, nor when D1 is nonzero, nor for nonlinear/non-E2 legal controllers. The prescribed matrix conditions are not promoted to a universal N&S test or a global obstruction.

New ordinary import: the exact Cayley-Hamilton identity stated above. Other facts are precisely the already admitted linear-SDE/isometry/standard L2 facts used in the earlier theorem, with all relevant E2 assumptions checked. No other source, scientific execution, external model, selected state, performance-output replacement, storage/Gramian or stopped realization method is used. All STOP/HOLD/ZERO/history and NR-SOURCE limits persist; this is written only, not peer/parent accepted, formal/kernel, human/configured-family, executable or novelty certified.
