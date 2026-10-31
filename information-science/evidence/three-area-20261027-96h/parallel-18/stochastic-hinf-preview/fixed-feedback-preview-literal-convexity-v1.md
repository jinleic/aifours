# A genuine common-law convexity block for literal preview synthesis

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:39:35 PDT 2026**. Continued standing-S1 analysis in the exact bound finite-horizon linear controller class. No new source or computation. The original-book images were separately admitted for literal source comparison only; their surrounding method discussion is NOT an input to this proof. The late-ACK PROCESS MINOR and all prior findings/STOP/HOLD/ZERO remain.

## 1. Entire matrix/controller scope and theorem

Fix ALL compatible real original matrices A,B,C,A0,B0,D0,D1, positive dimensions, finite T>h>=0, zero state/history and zero-extended canonical progressive E2 disturbances. Fix one feedback gain K. The remaining design parameter is

`R=(L0,Lh,H)`, with H in L2([0,h];R^(m x p)),

implemented by the ORIGINAL-information law `u=Kx+Rw`, where Rw has the two supplied endpoint taps and the supplied past/current window kernel. At h=0 combine the endpoints and omit H. No additional state, noise history or private randomization is allowed.

**Theorem.**

1. For this fixed K, the actual physical state, control and ORIGINAL output operators are affine in R, on the SAME progressive input and Brownian motion. A deterministic convex combination of feedforward parameters is one legal stationary controller, not an input-dependent selection of different controllers.
2. Consequently `R->G_prog(K,R)` and `R->G_det(K,R)` are convex (the inequality is valid in extended reals); both the uniform-strict and the all-input pointwise-strict literal feasible sets at a prescribed gamma are convex in R.
3. The conclusion extends to joint pairs (K,R) restricted to any affine feedback slice on which BK, B0K and D1K are all fixed. Feedback gains differing only in the simultaneous kernel of those three multiplication maps have exactly identical physical state/output operators for the same R.

The theorem does not assert convexity over arbitrary K, a numerical optimization method, attainment of an optimum or an unrestricted source-controller N&S criterion.

## 2. Actual-object coupling, every noise and preview term retained

For a fixed K the original closed-loop equation is

`dX=[P X+B Rw+C w(t-h)]dt+[Q X+B0 Rw]dW`,

`z=N X+D1 Rw`, `u=KX+Rw`,

with `P=A+BK`, `Q=A0+B0K`, `N=D0+D1K`. Each actual progressive E2 input has its unique strong nonexplosive E2 state/control/output by the permitted linear-SDE theorem and bounded preview operator. The two compared systems therefore share an actual probability space and well-posed caller, not just separate deterministic-input versions.

Let R1,R2 be ANY two design triples and lambda in [0,1] be a fixed deterministic design parameter. Define `Rlambda=lambda R1+(1-lambda)R2` componentwise, including its kernel. The kernel remains in L2 and uses exactly the same window. Let X1,X2 be the two actual solutions at a common arbitrary input w and Brownian path. The actual process

`Xlambda=lambda X1+(1-lambda)X2`

satisfies the original equation with Rlambda, because P,Q are fixed, BR and B0R depend linearly on R, and the two copies of the physical forcing Cw(t-h) have coefficients summing to one. Strong uniqueness identifies it with that law's actual state. Then

`ulambda=lambda u1+(1-lambda)u2`,

`zlambda=lambda z1+(1-lambda)z2`

hold for the SAME w and W. No copy of the controller sees an extra input, and the combined controller does not need to store either auxiliary solution: its implementation is just the displayed original law with K and Rlambda. This is the required forward actual-object caller. Conversely that law's unique solution must be the combined process, so the identity is not merely a candidate trajectory.

This covers every input, kernel, matrix rank/sign and lambda endpoint. It uses linearity of the actual linear SDE, not a state/output realization, probabilistic mixture or RMS objective.

## 3. The literal convexity and strictness conclusions

For every fixed nonzero admitted w, the pathwise triangle inequality followed by expectation gives

`E||zlambda(w)|| <= lambda E||z1(w)||+(1-lambda)E||z2(w)||`.

The denominator is the SAME E||w|| in all three systems. Dividing and taking the common progressive E2 supremum yields

`G_prog(K,Rlambda)<=lambda G_prog(K,R1)+(1-lambda)G_prog(K,R2)`.

At lambda=0 or 1 the conclusion is the corresponding identity, without interpreting a zero times an infinite value. The same proof with deterministic inputs gives the G_det inequality.

If both endpoint laws have uniform gain strictly below gamma, their convex combination does too. If instead both satisfy the ratio<gamma separately for EVERY admitted w, their weighted inequality is still strict for each such input, including all interior lambda; endpoints are the given laws. Thus pointwise-strict feasibility is also convex. This does not assert equivalence between pointwise and uniform strictness at a nonattained endpoint.

The current author-only bound `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302`, additionally asserts finiteness/continuity on this whole class. If using that UNREVIEWED import, the objective is a finite continuous convex functional and the uniform-strict feasible set is open as well as convex. The self-contained convexity proof above does not require adoption of that separate bound or a new scientific program.

## 4. Exact feedback equivalence slice, all degeneracies

Suppose K1,K2 satisfy

`B(K1-K2)=0`, `B0(K1-K2)=0`, `D1(K1-K2)=0`.                   (E)

Then their P,Q,N are identical. With the same R, the actual state equations and original output equations are identical and uniqueness gives exactly the same state/output for every input. Controls may differ by `(K1-K2)X`, but that difference is annihilated by every physical channel B,B0,D1. Every law still has the required E2/local pathwise admissibility.

More generally keep any fixed triple (BK,B0K,D1K) and allow K to vary on its affine fiber while R varies freely. The same proof as section 2 applies because P,Q,N remain fixed. The resulting actual original output is affine in R and independent of the invisible feedback directions; hence both gain objectives and strict feasible sets have the asserted joint convexity on that slice. No full-rank/inverse or quotient-source theorem is assumed, and zero/null fibers are included.

## 5. The unpaid identity for arbitrary feedback averaging

For arbitrary different feedbacks, the standard averaging step must NOT be silently reused. Let `Kbar=lambda K1+(1-lambda)K2`, `Xbar=lambda X1+(1-lambda)X2`, and similarly combine feedforward operators. Then

`lambda K1X1+(1-lambda)K2X2 - Kbar Xbar`

`=lambda(1-lambda)(K1-K2)(X1-X2)`.

Unless its physical B/B0/D1 images vanish, this is an extra term in the original drift, diffusion and/or output caller. Thus the combined trajectory need not be the actual trajectory for the averaged gain Kbar. Condition (E) pays this step; absent it, no convexity theorem over arbitrary feedbacks is proved here. This is an exact failed implication, not a physical counterexample to every possible alternative convex parameterization.

A random or disturbance-dependent lambda is not the fixed deterministic controller parameter used in the theorem. Nor is a policy that stores and simulates both states the original bound law; no such augmentation is proposed or authorized.

## 6. What changes for the original problem and what remains

The result identifies a real convex common-policy block of the literal synthesis problem, preserving the whole progressive input domain and all state/control-noise couplings, plus an exact algebraic feedback-equivalence fiber. It is more than a per-input trajectory or coordinate encoding: every feasible convex combination is one actual original-information controller valid for every input.

What remains OPEN is finding an original-domain necessary-and-sufficient condition over the full feedback/nonlinear controller class, evaluating the literal norm sharply, controller/source equivalence, and the infinite-horizon task. Convexity within this stated class does not promote the two-endpoint/L2-kernel subclass to the book's general F. No solver, controller search, chosen state/control probe, external source, model CLI or held guide is used; only the supplied definitions, actual linear-SDE uniqueness/linearity, ordinary norm inequalities and elementary matrix identities. All process/source/STOP/HOLD/ZERO/N4/aux214 limitations persist, with no review/adoption, formal/kernel, executable, human/configured-family or novelty claim.
