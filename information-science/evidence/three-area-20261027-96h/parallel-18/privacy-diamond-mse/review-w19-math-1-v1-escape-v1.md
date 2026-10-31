# w19 phase-type density boundary and bounded-rate escape — complete written review

Reviewer **InfoResearch96h-2**, info-1. Author **MathResearch96h-2**, math-1. Actual native prewrite clock: **Tue Oct 27 15:11:53 PDT 2026**. The first returned native observation around this duty was **15:09:47 PDT**; that date command was briefly tool-backgrounded for the incoming dispatch and its actual completed output arrived automatically. No timer, sleep, polling or persistent-work proxy was launched.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE. 0 FATAL / 0 MAJOR / 0 MINOR.** The exact density-sign threshold, entire closed non-PH side and fixed-order/BOUNDED-holding-rate escape theorem are SUPPORTED in writing. The positive-density PH-existence converse, exact finite minimum orders and unbounded-rate fixed-order closure remain unpaid. The boundary calculation is a definition-side REPRODUCTION/reconstruction, not a new proof of the full minimum-order function or a novel PH-existence theorem.

## 1. Complete frozen reads, pins and exposure

Read the manifest completely first, raw LF1–34: SHA256 `9d948609a7958aad57d03c93286fb01833ba95afa652473680f3d22a5694bcf6`, 34LF/2452B.

The SINGLE part was pin-matched and read **raw LF1–329 COMPLETELY through S3|79 END**: `packet-part-1-v1.md`, SHA256 `4d655b3d653e2d04504f9a2f4c0b51d2ea3e9a33924428f02d0db3ddac3b5e44`, 329LF/32359B. It includes ALL:

- **S1 CONTEXT:**43LF controls/literal-transform definition packet, pin `89fedee56db112d2fc29b1762dc18fbc58092dffabb130e9001e14a853eb5c2c`.
- **S2 AUTHOR v1:**195LF, pin `a763a08228625177d05f98cbc18f0deddba9cdfa609c83eb983e7f5a588d0adb`.
- **S3 AUTHOR escape:**79LF, pin `81a8d0ed5ca045fabb0e7f0ea0c0dcedcca7fb817085c155415b45d734b75655`.

All references below are the OUTER S1/S2/S3 labels in this supplied part. No old PH manuscript/addendum, L6/G7/U6/672 union, primary comparison, old proof/review/park/checkpoint, held v260 material or author contact was opened. The author ACK chronology/old-intake statements and original source/book provenance are not independently authenticated by linked-file reads.

**Exposure/contact:** this continuing owner has inherited prior cross-domain review/contact history. An exhaustive predecessor/current-author or PH-specific contact census is not supplied and was not recovered from prohibited history. No blindness, configured-family independence or unaffected-cognition certificate is claimed. Current reconstruction uses only the displayed transform, PH definition and elementary calculus/matrix arguments; no earlier threshold verdict, positive-realization theorem, selected parameter, old matrix ansatz or confidence guide is a premise. My own info-1 source line stays paused for this bounded review.

No scientific interpreter/calculator/CAS/Eval, numerical root, selected state/time/rank probe, enumeration, replay, outside mathematical source or nested/model-CLI review was used. Only this requested review output is written. Same-harness written support is not formal/kernel, human, executable, novelty or parent adoption.

## 2. Literal target and gate decisions

The supplied transform is

`H(s)=K/[(s+c)((s+a)^2+b^2)^2]`, `K=c(a^2+b^2)^2`,

with ALL `a>c>0`, `b>0`, `d=a-c`, `r=d/b`, `beta=1/r`. A PH representation uses ANY finite dimension, real Hurwitz Metzler T, literal exit `omega=-T1>=0` and a probability row alpha, matching `alpha(sI-T)^(-1)omega`. Topology, reducibility, holding-rate uniformity, latent canceled modes and input/exit supports are not restricted.

| Gate | Literal location | Decision |
|---|---|---|
| Inverse transform, normalization and analytic formula | S2 LF45–71 | SUPPORTED |
| ALL extrema and unique global density threshold | S2 LF73–136 | SUPPORTED |
| No finite PH at/beyond the touching boundary | S2 LF138–166 | SUPPORTED for ALL finite orders/topologies |
| Compact bounded-order/bounded-rate limits, possibly non-Hurwitz | S3 LF11–63 | SUPPORTED |
| Original existence/minimum-order caller | S2 LF168–185; S3 LF65–71 | Correctly limited; positive PH existence and unrestricted rate/order conclusions not supplied |

## 3. Inverse Laplace formula and all-variable algebra

For real s sufficiently positive, subtracting the elementary transforms of `e^(-at)sin(bt)` and `e^(-at)bt cos(bt)` gives

`b/J - b((s+a)^2-b^2)/J^2 = 2b^3/J^2`,

where `J=(s+a)^2+b^2`. Thus convolution with `e^(-ct)` yields exactly

`f(t)=K e^(-ct) F_r(bt)/(2b^4)`,

`F_r(x)=integral_0^x e^(-ru)(sin u-u cos u)du`.

The b-power is correct: the convolution contributes the change of variable `u -> bu` in addition to the inverse quadratic-square factor. Since `|F_r(x)|` is bounded by the finite integral of `e^(-ru)(1+u)`, f is continuous, bounded and absolutely integrable for every permitted parameter. Its signed integral is `H(0)=1`; no positivity is inferred from that normalization.

Put `R=1+r^2` and

`A_r(x)=[Rx+r(r^2+3)]sin x+[2-rRx]cos x`.

Differentiation gives

`A_r'(x)=[r^2-1+rRx]sin x+[Rx+2r]cos x`,

so `rA_r-A_r'=R^2(sin x-x cos x)`. Together with the forced initial value `A_r(0)=2`, this proves

`F_r(x)=[2-e^(-rx)A_r(x)]/R^2`.

This is a complete variable identity/initial-condition check, not a finite selected-value verification of an inferred formula.

## 4. ALL extrema and the exact threshold — no first-minimum shortcut

Let `g(x)=sin x-x cos x`; then `g'(x)=x sin x`. It is strictly increasing and positive on `(0,pi)`. On EACH `(n pi,(n+1)pi)`, n>=1, the sign of sin x is constant, so g is strictly monotone. Its signs at the left endpoint and half-period are opposite; there is exactly one zero `x_n` in `(n pi,n pi+pi/2)`, and these exhaust all positive zeros. At those zeros,

`sin x_n=x_n cos x_n`, `cos x_n=(-1)^n/sqrt(1+x_n^2)`.

Substituting this exact root identity into A_r, its middle coefficients combine as `r(r^2+3)-rR=2r`. Consequently

`F_r(x_n)=[2-(-1)^n W_r(x_n)]/R^2`,

`W_r(x)=e^(-rx)[(1+r^2)x^2+2rx+2]/sqrt(1+x^2)`.

The odd-index roots are positive local maxima; even-index roots are ALL positive local minima. The first minimum is `xi=x_2`, the unique `tan xi=xi` root in the specified interval. This identification is derived from the complete critical-point pattern, not chosen as a diagnostic time.

For fixed x>0, differentiating the full expression gives

`partial_r W_r(x)=-(1+r^2)x^3 e^(-rx)/sqrt(1+x^2)<0`.

At the symbolic derivative-regime boundary `r=1/xi`,

`W_(1/xi)(xi)=(xi^2+5)/(e sqrt(1+xi^2))>xi/e>2`.

The first strict inequality is the displayed positive polynomial difference `9xi^2+25`; the second follows from `xi>2pi` and ordinary exact elementary bounds `e<3<pi`. These are literal analytic bounds, not a numerical approximation or selected physical parameter trial. Exponential decay makes W tend to zero as r tends to infinity. Continuity and strict r-monotonicity therefore yield a UNIQUE positive threshold root r_star, with `r_star xi>1`.

The x derivative is also correct:

`partial_x W_r(x)=-e^(-rx)x^2 Q_r(x)/(1+x^2)^(3/2)`,

`Q_r(x)=r(1+r^2)x^2-(1-r^2)x+r(r^2+3)`.

Its decisive decomposition

`Q_r(x)=x[(rx-1)+r^2(rx+1)]+r(r^2+3)>0` when `rx>=1`

shows W decreases strictly on ALL `x>=xi` whenever `r>=r_star`. Thus EVERY later even-root value of W is smaller than its first-minimum value. This is the load-bearing global comparison a single extremum evaluation would not supply.

For `r>r_star`, every minimum is positive; all maxima are positive, initial increase is positive and monotonicity covers every intervening interval, proving f positive at every positive time. At equality the first minimum is zero and all later ones positive; no other positive-time zero exists. Since

`F_r''(xi)=e^(-r xi)xi sin xi>0`,

the touching zero is exactly quadratic. The positive analytic prefactor and the nonzero scaling b preserve its order at `t=xi/b`. For `r<r_star`, the exact first-minimum value is negative by strict r-monotonicity, proving the other sign direction.

The origin itself has f(0)=0 as allowed by the nonnegative statement; the strict statement is correctly only for t>0. All r,c,b remain coupled to the original parameters. The additional whole-range r>=1 derivative argument proves `r_star<1`; its stated symbolic location and the density-side placement of the critical ratio do not determine its PH order.

## 5. ALL finite PH topologies have strictly positive density on positive times

**S2 LF142–154: SUPPORTED.** For any finite PH pair choose symbolic `q>0` at least the largest holding rate. Then `M=T+qI>=0` entrywise and

`alpha e^(Tt)omega=e^(-qt) sum_(k>=0) t^k alpha M^k omega/k!`.

Every coefficient is nonnegative. Hurwitz stability and the ACTUAL row tie give

`integral_0^infinity alpha e^(Tt)omega dt=alpha(-T)^(-1)(-T1)=alpha1=1`.

Therefore at least one coefficient is strictly positive, and that one term makes the density positive for EVERY t>0. Reducible graphs, zero coordinates and canceled modes are included; there is no irreducible-only positivity assumption or fixed holding rate imposed on T.

Laplace uniqueness for integrable continuous densities identifies any exact PH representation with f. Both negativity below r_star and the interior zero at equality contradict this PH positivity. Thus no finite PH of ANY order exists for `r<=r_star`, equivalently `beta>=1/r_star`.

The converse remains deliberately absent: a positive normalized rational density need not be granted a PH realization without the exact positive-realization/PH-characterization theorem or construction and all its antecedents. The packet does not import such a theorem from memory, old comparisons or a supplied baseline label.

## 6. Fixed-order bounded-rate escape, including a non-Hurwitz limit

### 6.1 Correct compactness hypotheses (S3 LF11–27)

Fix the stated ARBITRARY symbolic c,b,M>0 and integer n>=1. Negating the theorem yields parameters r_j approaching r_star from above with actual exact PH representations of order at most n and every holding at most M. A subsequence has one dimension m<=n.

Metzlerness and `T_j1<=0` imply that every nonnegative off-diagonal row sum is at most `-T_j,ii<=M`. Thus all generator entries lie in a common bounded cube. Probability rows lie in the closed finite-dimensional simplex. A subsequence converges to `alpha_0,T_0`, and the row-tied exits converge to `omega_0=-T_01`. All Metzler/nonnegative/substochastic inequalities are closed.

The candidate correctly DOES NOT infer that T_0 is Hurwitz. Zero modes, closed/inaccessible classes and zero exits are explicitly permitted in the limit. No unprovided PH-class closure theorem is hiding in this step.

### 6.2 Positive-real resolvents use the SAME limit data (S3 LF31–42)

`P_0=I+T_0/M` is entrywise nonnegative and has row sums at most one. For EVERY real s>0,

`(sI-T_0)^(-1)=(s+M)^(-1) sum_(k>=0)[M/(s+M)]^k P_0^k`.

This converges in the row-sum operator norm because `||P_0||<=1` and its scalar ratio is less than one. It proves invertibility at each positive s despite a possibly singular T_0 at zero. The same bound applies to all T_j. Continuity of inversion at this fixed positive-real point and the rational target formula give

`alpha_0(sI-T_0)^(-1)omega_0=H_(r_star)(s)`.

The single matrix/row subsequence converges independently of s; applying the continuous evaluation at arbitrary s proves the identity for ALL s>0 with the SAME limit data. No incompatible s-dependent limiting realization is selected.

### 6.3 The singular limit still cannot touch zero (S3 LF46–63)

Uniformization with P_0 gives `e^(T_0t)>=0` with row sums at most one. Also each exit coordinate lies between zero and M, so `g_0(t)=alpha_0 e^(T_0t)omega_0` is continuous and bounded between zero and M. Its positive-real Laplace transform is the above resolvent; exponential damping legitimizes the integral even without Hurwitz stability.

That transform is the nonzero H_(r_star), so g_0 is not identically zero. In its nonnegative series using `T_0+MI>=0`, some coefficient must therefore be strictly positive. Hence `g_0(t)>0` for EVERY t>0, exactly as in the finite-PH argument but without using an integral-at-zero normalization or assuming transience of the limit.

The density f_star constructed in S2 is bounded and continuous and has the SAME positive-real Laplace transform. Uniqueness of Laplace transforms for continuous functions of exponential order forces `g_0=f_star`, contradicting `f_star(xi/b)=0` at a positive time. This proves the asserted excluded neighbourhood for each fixed c,b,n,M.

The claimed equivalent rate-escape statement is correctly conditional: a fixed-order sequence, IF one exists, cannot have a uniform bound on maximum holdings as the boundary is approached. It neither asserts that such PH representations exist nor proves divergence of minimum orders; unbounded-rate limits remain outside this compactness argument.

## 7. Boundary reproduction and exact original-problem effect

The existence/density-boundary calculation should be booked as a **definition-side reproduction/reconstruction of the density sign and necessary-PH boundary**, not as a newly solved minimum-order region, novel threshold or new positive-PH existence theorem. The present packet supplies no earlier baseline proof/statement with which to certify historical formula identity, and I did not reopen one. If the parent's inherited boundary is already supported, this repeat derivation does not count as an additional scientific discovery or an independent-family verification of it.

In particular “PH existence boundary” must not be read here as an IF-AND-ONLY-IF PH theorem: S2 proves the non-PH side and density positivity on the other side, but explicitly leaves positive-density PH existence NR. It also does not pay the exact order decision at the critical ratio or the PH6/G7 sentence preserved from a historical selection. Those older claims remain at their safe final-report scopes, not new premises of these proofs.

The bounded-rate escape theorem is a distinct exact conditional obstruction on ALL topologies with BOTH an order ceiling and a holding-rate ceiling. It is NOT an unrestricted fixed-order impossibility region: taking rates arbitrarily large is precisely the unpaid case. No global rate normalization, hidden-fast-state closure, divergence-of-orders result or positive-side actual alpha,T construction is supplied.

## 8. Final separate verdicts and unchanged limits

- Inverse density/normalization and universal analytic identities: SUPPORTED.
- Complete extrema classification, unique implicit r_star and all-time strict/nonnegative sign criteria: SUPPORTED.
- Closed-side all-finite-order PH exclusion, including the touching zero and canceled/reducible modes: SUPPORTED.
- Near-boundary fixed-order bounded-holding escape with the potentially non-Hurwitz limit: SUPPORTED.
- Original-object caller/non-converses: correctly limited; original whole minimum-order function, positive-side existence and unbounded-rate closure remain open.

**0 FATAL / 0 MAJOR / 0 MINOR at the entire frozen scope.** No stronger assurance, source/book authenticity, novelty or original PH-order completion is inferred. All previous v260/exposed-consumer and other STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit unestablished and auxiliary214 STOP remain. A correct current reproduction/compactness proof is not a historical provenance or cognition cure.

**END COMPLETE w19 REVIEW — manifest, sole part and all three source endings read; no author contact or other mathematical source.**
