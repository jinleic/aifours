# Joint-projector Hessian attempt — exact coupled conditions, uniform-transfer gap

Observed activation clock: **2026-10-24T03:27:56-0700**. Observed settlement clock preceding this freeze: **2026-10-24T03:32:49-0700**. PhysicsDepol4, same physics-2 primary. The first new logical input was announced to Main before work: necessary **joint** second variations on the actual complex Grassmannian, with P(t)^2=P(t) exactly, rather than a fixed-P compression or Schmidt reduction. No scientific program, arithmetic interpreter, numerical search, CLI or nested agent was used.

**Outcome:** the new coupled necessary resolvent inequality below is derived. Its natural Pauli-direction summation is an exact covariance identity and does not prove the required bound. The first unproved uniform transfer is frozen in §5. No low-noise index, all-projector Schur domination or eligible channel witness is established; the full target is not declared exhausted.

## 1. Operative boundary and literal objective

Read the actual parent's `physics-structural-frontiers-parent-v1.md` §3 and its complete untruncated coverage paragraph. The supported predecessor is source `projector-dual-and-offrange-control-v1.md`, SHA `653860e76b6de6b4994920d98817dd04588381a8dedbbfc98ee2c84abbb24159`, with actual different-domain return SHA `6f91d1053bebc5e270d38e121da8b8efabdf13539db5ab02dfea1157c6b8d682`, already read completely/hash-matched. It establishes the exact dual, fixed-P off-range control and Schur equivalence only. It does not rule out an in-range representative of a **jointly global** optimum.

Let Phi=Phi_3 be the physical unnormalized sum of the four erase-and-reinsert-identity maps. For fixed k in{2,3,4}, put

`beta=max_(rank-k orthogonal P, ||psi||=1) <psi|Phi(P)|psi>`.

Compactness gives a joint maximizing pair. Product-star controls give beta>=c:=k+3. The desired sufficient U3 theorem is beta<=c. Nothing below assumes that inequality or assumes psi belongs to Ran(P).

For a maximizing pair set

`rho=|psi><psi|`, `H=Phi(P)`, `A=Phi(rho)`.

Fixing P makes psi a top eigenvector of H: `H psi=beta psi`. Fixing rho makes P a top-k spectral projector of A, so `[A,P]=0`, including when eigenvalues tie at the boundary. These are joint optimality facts, not consequences asserted for an arbitrary fixed projector.

## 2. Exact actual-projector and state tangent curves

Write Q=I-P. For an arbitrary **complex** linear map X:Ran(P)->Ran(Q), use the anti-Hermitian generator

`K_X=[[0,-X^dagger],[X,0]]` on Ran(P)+Ran(Q),

and `P(t)=exp(tK_X)P exp(-tK_X)` for real t. This is an actual rank-k orthogonal projector at every t, not a first-order arbitrary marginal tuple. Its first two derivatives are

`L_X=P'(0)=[[0,X^dagger],[X,0]]`,

`P''(0)=[[-2X^dagger X,0],[0,2XX^dagger]]`.                        (1)

For arbitrary complex v orthogonal to psi take the normalized state curve

`psi(t)=(psi+t v)/sqrt(1+t^2 ||v||^2)`.

The objective `f(t)=<psi(t)|Phi(P(t))|psi(t)>` has zero first derivative by the two optimality relations above. Its second-order coefficient is

`<v|(H-beta I)|v> +2Re<v|Phi(L_X)|psi>`

` -Tr_P(A_P X^dagger X)+Tr_Q(A_Q XX^dagger)`,

where A_P=PAP and A_Q=QAQ. Since the pair is a global maximum, this coefficient is nonpositive. Define

`E(X)=Tr_P(A_P X^dagger X)-Tr_Q(A_Q XX^dagger)>=0`.

Its nonnegativity is also immediate in an A eigenbasis: it is the sum of `(alpha_a-alpha_b)|X_ba|^2` over occupied a and unoccupied b, with every gap nonnegative. Hence the genuinely coupled necessary inequality is

`<v|(beta I-H)|v>+E(X) >=2Re<v|Phi(L_X)|psi>`                      (2)

for every complex X and every complex v perpendicular to psi. Varying the actual projector and state independently with these velocities is legitimate; no unproved invariance of H on Ran(P) is used.

## 3. What the mixed Hessian actually controls

Let S=I-rho and put

`B_psi=S(beta I-H)S` on psi-perp, `T_X=S Phi(L_X)psi`.

B_psi is positive semidefinite because beta is the top eigenvalue of H. Minimizing the left-minus-right side of (2) over v gives the exact pair of conditions

`T_X in Ran(B_psi)`,

`<T_X|B_psi^(+) T_X> <=E(X)` for every X.                          (3)

The pseudoinverse is on psi-perp. If T_X had a component along ker(B_psi), scaling v in that component would violate (2). Under the range condition, completing the square yields precisely (3), including degenerate top eigenvalues. This derives a **coupled resolvent bound**, not just first-order commutativity.

The map X->T_X is real-linear, not generally complex-linear, because L_X contains both X and X^dagger. Inequality (2) is a real quadratic-form condition with arbitrary complex variables; no complex-linearity shortcut is taken when deriving (3).

These conditions are uniform over every joint maximizing pair at each of the three ranks. They are not asserted for all projectors without their maximizing state/stationarity hypotheses.

## 4. Natural Pauli directions: exact saturation, not the needed upper bound

The first attempted use of (3) was to sum the physical local-Pauli tangent directions. This can be evaluated completely in writing and exposes why that summation does not close the target.

Let U be any one of the twelve Hermitian single-qubit Pauli matrices, with U^2=I. Phi is covariant under physical local unitaries. The simultaneous local-unitary orbit of P and psi therefore keeps the objective constant. Its projector velocity is `i[U,P]=L_X` with X=iQUP, and its phase-adjusted state velocity is

`v_U=i(U-<psi|U|psi>)psi`.

Covariance gives `Phi(i[U,P])=i[U,H]`. Applying this to the eigenvector psi and projecting to psi-perp proves

`T_X=B_psi v_U`.

The actual tangent energy can also be computed using [A,P]=0:

`E(iQUP)=beta-Tr[A U P U] =<v_U|B_psi|v_U>`.                      (4)

Thus (3) is saturated along these simultaneous symmetry directions. Their nontrivial mixed terms are already fixed by covariance; they do not furnish a free inequality at the desired constant c.

For transparency, define the Pauli sum `Z(Y)=sum_U UYU`. The exact identities on arbitrary operators are

`Z(Y)=2Phi(Y)-4Y`,

`Phi^2=2Phi+2Phi_2`,                                              (5)

where Phi_2 is the six two-qubit-marginal map. In (5), each single-site erase map squares to twice itself and distinct erasures commute; the six double erasures are exactly Phi_2.

Put `t2=Tr[P Phi_2(rho)]`. Self-adjointness and (5) give

`Tr(AH)=Tr[P Phi^2(rho)]=2beta+2t2`.

Summing (4) over the twelve Pauli matrices gives

`sum_U E(iQUP)=12beta-Tr[A Z(P)]`

`                =16beta-2Tr(AH)=12beta-4t2`.                      (6)

Summing the state-side quantities gives the same identity:

`sum_U <v_U|B_psi|v_U> =Tr[(beta I-H)Z(rho)]`

`                         =12beta-4t2`.

All conjugations, factors of two and traces are explicit; no arithmetic code or finite-point evaluation is used. The inherited U2 bound at k2,3,4 gives t2<=3k+3 at its existing trust level. This makes the right side of (6) **positive** when beta>k+3; it does not contradict that hypothetical inequality. Merely using E>=0 gives t2<=3beta, the wrong direction for an upper bound on beta.

This diagnoses the exact failure of this **particular summation**, not impossibility of all uses of the Hessian. No symmetry identity is counted as a new low-noise bound.

## 5. First unproved uniform transfer to the target Schur blocks

The original all-projector target uses the decomposition Ran(P)+Ran(Q), with

`A_H=P H P`, `B_H=P H Q`, `C_H=Q H Q`, `D_c=cQ-C_H`, c=k+3.

It requires

`D_c>=0`, `Ran(B_H^dagger) subset Ran(D_c)`,

`cP-A_H >=B_H D_c^(+) B_H^dagger`.                                (7)

The new necessary inequality (3) instead concerns beta I-H on **psi-perp**, driven by the spectral gaps of A=Phi(rho). These are different subspaces, different right-hand sides and a different scalar: psi need not lie in Ran(P), and beta>=c is the unknown maximum, not a known upper bound.

One cannot replace beta by c in (3). If a counterexample maximum had beta>c, then on psi-perp the c-gap would be `B_psi-(beta-c)I`; positivity of B_psi alone does not imply positivity after that subtraction. Nor does its range condition automatically become the range condition in (7). Assuming such a replacement would simply assume away the desired contradiction.

**First new unproved step:** derive from the actual coupled projector identities plus (2)/(3) a nonperturbative implication that excludes beta>c, or directly controls all three conditions (7). No bound established here performs that transfer. In particular, the Pauli-direction sum (6) only reproduces covariance and cannot be promoted to (7). The genuinely non-symmetry Grassmannian directions remain unbounded by a proved target-constant estimate.

This is the exact current blocker of this bounded attempt. It is not a claim that (7) is false, that every joint optimum is off-range, that all second-order methods are exhausted, or that the unrestricted scientific target is exhausted. No new compression-only countercontrol, restricted input region, or ordinary-Schmidt surrogate was substituted for the target.

## 6. Retained channel and assurance boundaries

The actual all-p channel residual remains k2,3,4 for0<p<2/3 at the parent's central/high-noise boundary. If the U3 sufficient bound ever fails, an actual original-channel counterexample must still meet the SAME-projector condition

`delta3>u^2 d1+u d2+d4/u`, `u=p/[2(1-p)]`,

with exact positive rho, orthogonal projector and physical p. Nothing in this Hessian attempt produces such a witness.

The public Zhang claim's matching clipping mechanism, under-specified uniform support and unresolved priority remain unchanged. This note contains classical variational machinery applied explicitly, not a novelty claim. Parent and separate reconstruction would be required before treating any new identity packet as supported; no scientific, formal/kernel, human or outside-model verification occurred.
