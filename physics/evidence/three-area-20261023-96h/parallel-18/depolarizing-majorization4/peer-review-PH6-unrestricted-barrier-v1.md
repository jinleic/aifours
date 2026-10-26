# Hostile written reconstruction — unrestricted six-state PH barrier

Observed review clock: **2026-10-23T14:29:56-0700**. Reviewer PhysicsDepol4, under the parent's bounded review assignment. This is an ordinary in-harness reconstruction with the supplied proof, not blind, cross-vendor, human or kernel verification. No mathematical program, solver, numerical root calculation or executable replay was run.

## Pin, read scope and verdict

Complete reviewed source: `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/proof-unrestricted-six-state-barrier-v1.md`, **all lines 1–195**.

Observed SHA-256: **`8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`**, equal to the parent's assigned pin. Also read the actual slot selection and the upper constructions described below.

**Verdict: no FATAL, MAJOR or MINOR mathematical defect found.** The argument excludes every PH representation with at most six transient states when `beta^2>1/2`, without an initial constant-diagonal/topology/irreducibility assumption. Together with the displayed inherited upper construction it proves the stated iff. At equality it derives, rather than assumes, the diagonal and cycle rigidity. The exact-order-seven bridge is valid on `1/2<beta^2<=53/96`, at the declared G7 construction dependency. Parent acceptance and novelty remain separate.

## 1. Geometric-mean symmetrization (source lines 30–59)

For a real Metzler X, the off-diagonal products X_ij X_ji are nonnegative, so the symmetric S has real entries. Its diagonal is unchanged. For the quadratic trace both matrices give

`sum_i X_ii^2 +sum_(i!=j) X_ij X_ji`.

For the cubic trace, grouping closed walks by their number of distinct vertices gives:

- one vertex: `sum_i X_ii^3`;
- two vertices: `3 sum_(i<j)(X_ii+X_jj) X_ij X_ji`;
- three vertices: `3 sum_(i<j<k)(A_ijk+B_ijk)`.

The first two groups agree exactly for X and S, even when diagonal entries are negative. For each triple, S gives `6sqrt(A_ijk B_ijk)`, while X gives `3(A_ijk+B_ijk)`. AM–GM proves the claimed direction. This does not require X to be entrywise nonnegative after centering, nor positive reverse-edge products, irreducibility, or any missing-cycle assumption.

## 2. Sharp symmetric trace-zero cubic bound (lines 61–82)

If tau2=0, S is zero and the comparison gives tau3>=0. Otherwise, normalize its real eigenvalues to zero sum and squared sum one. The sphere/hyperplane intersection is compact. The two constraint gradients are independent there: dependence would make all eigenvalues equal, inconsistent with zero sum and norm one. Lagrange multipliers consequently put all eigenvalues among the at most two roots of a quadratic.

For k negative values and n-k positive values, the two constraints yield exactly

`r_minus=-sqrt((n-k)/(nk))`, `r_plus=sqrt(k/(n(n-k)))`.

The cubic sum is `(2k-n)/sqrt(nk(n-k))`. The minimum is negative and therefore occurs for k<=n/2; its squared magnitude is `[n^2/(k(n-k))-4]/n`, maximized at k=1. The n=2 case gives zero on both sides and is consistent. Thus the sharp constant is `(n-2)/sqrt(n(n-1))`, and at n=6 it is **4/sqrt(30)**. A diagonal matrix with the displayed one-negative/five-positive eigenvalues attains it, so this is sharp even within Metzler matrices.

Combining this real-symmetric bound with the explicitly checked trace comparison proves Lemma M. No claim that a general Metzler matrix has real eigenvalues is needed.

## 3. Characteristic binding, trimming and the hidden mode (lines 84–102)

The numerator K is a nonzero constant, so the displayed denominator is reduced and has degree five. A finite PH transfer has denominator dividing det(sI-T), including when T is defective or the realization is nonminimal. Therefore order below five is impossible.

For order five, shifting by c gives spectral trace -4d and squared trace `4(d^2-b^2)`. Nonnegative reverse-edge products and Cauchy on the five real diagonal entries give

`4(d^2-b^2)>=sum_i X_ii^2>=16d^2/5`,

hence beta^2<=1/5. This is a topology-unrestricted lower bound.

For order six, the remaining monic factor is necessarily s+u with u real; Hurwitz stability forces u>0. If any state were unreachable from alpha's positive support, removing the unreachable states would preserve the transfer. There are no transitions from a reachable state into an unreachable one; the restricted block therefore remains a stable PH subgenerator with the same exits. Its order would be at most five, impossible in the analyzed beta^2>=1/2 region. Thus every state is reachable.

Every state also reaches a positive exit: otherwise the finite reachable no-exit subgraph would contain a final conservative class, forcing eigenvalue zero and contradicting Hurwitz stability. For fixed t0>0, `alpha exp(Tt0)` and `exp(Tt0)w` are therefore positive on each irreducible block. For a dominant diagonal block B of abscissa rho, paths staying in B give a nonnegative lower contribution. Positive left/right Perron vectors then give a constant L>0 with

`f(t+2t0)>=L exp(rho t)`.

For completeness this lower bound does not require an unproved asymptotic observability assertion: the positive restricted row/column dominate positive multiples of the left/right Perron vectors componentwise, and their product through exp(Bt) is exactly a positive constant times exp(rho t).

The target inverse transform has positive leading residue `K/(d^2+b^2)^2` at -c and only degree-one polynomial times exp(-at) from the repeated nonreal poles. Thus rho cannot exceed -c. Since -c is an actual pole/eigenvalue, rho=-c, so **u>=c**. This handles reducibility and canceled subordinate modes; it does not falsely require every eigenvalue to be visible as a pole.

## 4. Centered spectrum, traces and the sign of h (lines 104–136)

From `6mu=c+4a+u`, h=mu-a gives

`u=c+2d+6h`; hence u>=c yields `h>=-d/3`.

The centered eigenvalues are exactly

`d+h`, `-d-5h`, and `h+ib,h-ib` each twice.

Their powers give, without a diagonalizability assumption,

`tau2=2d^2+12dh+30h^2-4b^2 =12dh+30h^2-4Delta`,

`tau3=-12d^2h-72dh^2-120h^3-12hb^2 =-12h(d^2+6dh+10h^2+b^2)`.

For `-d/3<=h<0`, the factor `2d+5h>=d/3>0`, so `6h(2d+5h)<0`; subtracting 4Delta cannot restore nonnegativity. This contradicts the exact nonnegative expression for tau2 of a real Metzler matrix. Thus h>=0, and Delta>0 forces h>0. The proof does not assume centered diagonal entries vanish here.

## 5. Cubic obstruction and full polynomial expansion (lines 138–169)

For h>0 and Delta>=0, R is positive and tau3 is negative. Lemma M requires

`12hR<=(4/sqrt(30))tau2^(3/2)`.

In particular tau2>0. Squaring positive quantities is legitimate and yields

`tau2^3>=270h^2 R^2`.

Set `tau20=6h(2d+5h)` and `R0=(3/2)d^2+6dh+10h^2`. Then tau2<=tau20 and R>=R0. I reconstructed identity (7) by the following coefficient expansion:

| monomial | coefficient in 5 R0^2 | coefficient in 4h(2d+5h)^3 | difference |
|---|---:|---:|---:|
| d^4 | 45/4 | 0 | 45/4 |
| d^3 h | 90 | 32 | 58 |
| d^2 h^2 | 330 | 240 | 90 |
| d h^3 | 600 | 600 | 0 |
| h^4 | 500 | 500 | 0 |

Since tau20^3=216h^3(2d+5h)^3, multiplication by 54h^2 gives exactly

`270h^2 R0^2-tau20^3 =54h^2[(45/4)d^4+58d^3h+90d^2h^2] >0`.

The strict sign uses only d,h>0. Thus `tau2^3<=tau20^3<270h^2R0^2<=270h^2R^2`, the required contradiction. This is a symbolic reconstruction, not finite-value testing. It rules out h>0 at both Delta>0 and Delta=0.

## 6. Equality rigidity (lines 171–179)

At Delta=0, the sign argument has h>=0 and the cubic argument forbids h>0. Therefore h=0, mu=a, u=c+2d and tau2=0. The formula

`tau2=sum_i X_ii^2+sum_(i!=j)X_ij X_ji`

then forces all centered diagonal entries zero and every reverse-edge product zero. This is precisely where constant holding rates are **concluded**, not imported as an ansatz. X is now entrywise nonnegative. With tau3=0, its nonnegative closed-walk sum forbids every positive directed triangle; the two-cycle statement already came from tau2. The equal-rate anchor's four/six feedback cycles are consistent, not an extra premise.

## 7. The iff and minimum-seven composition (lines 15–28,181–187)

Observed inherited pins:

- `manuscript-repeated-pole-PH-v2.md`: `b92639157d0e90530d1237d336f781c6707b01c2846801cfad8fcf5ef1f204f2`; read its explicit five-/six-state constructions, lines 94–147.
- `proof-H12-seven-state-extension-v1.md`: `59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`; read all 170 lines.
- Read the operative actual G7 disposition `institute/runs/three-area-2026-10-23-96h/G7-and-reference-regions-parent-v1.md`, lines 5–13, which records its separate reconstruction and supported upper7 scope. The original G7 freeze's candidate label is historical, not silently rewritten.

The T6 coefficients `A=d^2-2b^2`, `B=b^2(2d^2-b^2)`, `C=d^2b^4` are nonnegative on beta^2<=1/2, with B,C>0. Its real canceled mode is -(c+2d), its initial row `(d,a,0,...)/(c+2d)` is positive and sums to one, and its transfer numerator cancels exactly that factor. Thus PH order at most six exists throughout the claimed lower-parameter range. The new lower proof excludes every N<=6 above that range, proving the iff, not only the failure of this companion.

G7 gives a genuine PH representation on beta^2 in[1/2,53/96]: the pinned polynomial has nonnegative feedback coefficients, its generator shifts to the explicitly stable seven-eigenvalue list, the three initial weights normalize via `(lambda+3d/4)(lambda+2d/3)=u1u2`, and both hidden factors cancel with a nonnegative input row. This is an actual transfer construction, not spectral feasibility alone. Combining that upper7 with the newly reconstructed unrestricted N<=6 exclusion gives **minimum exactly seven on 1/2<beta^2<=53/96**. The strict lower endpoint is correct; at equality the explicit six-state representation exists and the five-state trace obstruction applies.

No PH-existence characterization is needed for this finite-band composition. It does not determine minimum order beyond 53/96, certify the general book problem, or establish priority. The matrix-moment mechanism may have classical equivalents; this correctness review makes no novelty claim.

## Evidence boundary and return

Actual work: full pinned new-source read, selection/import read, observed metadata pins, written trace/triangle/polynomial reconstruction, positivity/trimming and strict-endpoint checks, and reading the actual upper matrices/operative G7 review disposition. No unadmitted execution or formal verification occurred. Parent acceptance remains its own gate.

The bounded PH review is complete. The reviewer resumes the one owned four-qubit majorization problem.
