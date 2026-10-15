# Scalar benchmarks for the printed stochastic norm (deterministic disturbances)

Date: 2026-10-14 (America/Los_Angeles). Status: analytic certification of a restricted subclass. An independent no-tools hostile review (Claude Opus 5.5, effort max) returned `PASS_RESTRICTED_SCOPE_MINOR_REVISIONS`. Its required revisions are applied below; see [Review record](#review-record). These results concern **deterministic disturbances** and an **inert control**. They are not a synthesis result, do not cover adapted disturbances, and do not resolve the book problem. No novelty is claimed.

The stronger original-model result, a constant-matrix finite-horizon solvability separation valid for all adapted disturbances with an effective control, is the worker's Theorem L2 in [`../../stochastic-hinf-preview-control/work/literal_continuation.md`](../../stochastic-hinf-preview-control/work/literal_continuation.md). The parent's exact-arithmetic replay of its inequalities is in [`preview-separation.json`](preview-separation.json) and [`preview-separation-b0-nonzero.json`](preview-separation-b0-nonzero.json).

## Contract

Consider constant coefficients

\[
dx(t)=(a x(t)+w(t-h))dt+\sigma x(t)dW(t),\qquad x(0)=0,\quad z=(x,u),
\]

with B=B0=0, D0=(1,0)^T and D1=(0,1)^T. This is the book's **delayed-disturbance model**: the plant is driven by w(t-h), and the counted disturbance window is [0,T-h]. Then D1^T D1=1, the control enters neither drift nor diffusion, and ||z||^2=||x||^2+||u||^2 pathwise. Hence u=0 is pathwise optimal for both output functionals, under every controller class, including preview controllers. The subclass therefore tests only the norm functional, not synthesis. Under this delayed model, the response on [h,T] to a deterministic disturbance on [0,T-h] has the same law as the undelayed response on [0,T-h]. The finite-horizon results below are stated for the active horizon T after this shift. They do not apply verbatim to a look-ahead model in which the plant is driven by w(t).

For deterministic disturbances define

\[
g_1(T)=\sup_{0\ne w\in L^2(0,T)}
 \frac{E\|x_w\|_{L^2(0,T)}}{\|w\|_{L^2(0,T)}},\qquad
g_2(T)=\sup_w\frac{(E\|x_w\|_{L^2(0,T)}^2)^{1/2}}{\|w\|_{L^2(0,T)}}.
\]

The printed book criterion uses g1; its mean-square replacement uses g2.

## Theorem F: strict finite-horizon norm separation

For every finite T>0, every real a and every nonzero sigma,

\[
0<g_1(T)<g_2(T)<\infty.
\]

**Proof.** Write

\[
(\mathcal T w)(t)=\int_0^t\Phi(t,s)w(s)ds,\quad
\Phi(t,s)=\exp((a-\sigma^2/2)(t-s)+\sigma(W_t-W_s)).
\]

Ito's product rule gives d(Psi^{-1}x)=Psi^{-1}w dt for Psi(t)=Phi(t,0), so this is the strong solution. Since E Phi(t,s)^2=exp((2a+sigma^2)(t-s)), the operator from deterministic L2(0,T) into L2(Omega;L2(0,T)) is Hilbert-Schmidt, hence compact, and g2(T)<infinity. The functional f(v)=E||v||L2 is 1-Lipschitz in that Hilbert norm. A maximizing sequence on the unit sphere has a weakly convergent subsequence whose images converge strongly, so the g1 supremum is attained at some w*. The unit input has a positive response on (0,T], so g1>0 and w*≠0. Homogeneity then forces ||w*||=1. Positivity of Phi gives |T w|<=T|w| pathwise, so a nonnegative maximizer can be chosen.

For nonnegative nonzero w*, Y=||T w*||L2 is not almost surely constant. Since w* lies in L1(0,T), Y is a continuous functional of the Brownian path in the uniform topology. Along W_t=k t, the kernel is exp((a-sigma^2/2+sigma k)(t-s)). For every t after the essential infimum of supp w*, the inner integral is strictly increasing in sigma k. Two such paths therefore have different Y values, and uniform balls around them have positive Wiener measure. Since E Y^2<infinity, strict Cauchy-Schwarz at the maximizer gives

\[
g_1=EY<(EY^2)^{1/2}=\|\mathcal T w^*\|_{L^2(\Omega;L^2)}\le g_2. \qquad\text{QED}
\]

**Consequence.** For **every** gamma in (g1(T),g2(T)), u=0 satisfies the printed criterion and every controller fails the mean-square criterion, for deterministic disturbances in this subclass. This holds under both strict and non-strict conventions.

### Mean-square operator used by the computational check

Let c=2a+sigma^2. For s<=r<=t, E[Phi(t,s)Phi(t,r)]=exp(a(r-s)+c(t-r)). Hence g2(T)^2 is the largest eigenvalue of the positive compact integral operator with kernel

\[
K_T(s,r)=e^{a|s-r|}\int_{\max(s,r)}^T e^{c(t-\max(s,r))}dt.
\]

The independent moment equations are m'=a m+w and p'=c p+2w m, with zero initial data; the output energy is the integral of p.

## Theorem I: infinite-horizon deterministic-input gain

On [0,infinity), with the same deterministic-input gains: if c=2a+sigma^2<0, then

\[
g_1(\infty)=g_2(\infty)=\sqrt{\frac{2}{a(2a+\sigma^2)}}.
\]

If c>=0, both gains are infinite. This includes the sigma=0 specialization. The c>=0 branch is an **open-loop statement**: with an inert control, that plant is not mean-square stabilizable and lies outside any internally-stable infinite-horizon problem.

**Upper bound for c<0.** Necessarily a<0. If w is supported in [0,S], then p(t)=p(S)exp(c(t-S)) for t>=S, so p vanishes at infinity. Integrating p'=c p+2wm gives

\[
E\int_0^\infty x^2dt=-\frac2c\int_0^\infty w(t)m(t)dt
 \le \frac{2}{a c}\|w\|_2^2,
\]

by Cauchy-Schwarz and Young's inequality ||m||2<=||w||2/|a|. For general w in L2, let w_n=w 1_[0,n]. By causality the response to w_n agrees with the response to w on [0,n]. Thus, for every finite R and every n>=R, E int_0^R x_w^2 <= (2/(ac))||w||^2. Monotone convergence in R gives the same bound on [0,infinity). Jensen then gives g1<=g2<=sqrt(2/(ac)).

**Lower bound, including instability.** Fix L>0 and apply w=1 on [0,N L], zero afterward. On block j, let x_j^0 be the zero-start response to unit input driven only by that block's Brownian increments, and Y_j=int_0^L(x_j^0)^2dt. The Y_j form one fixed independent identically distributed sequence, independent of N, with finite mean. On block j the actual state equals a nonnegative carried term plus x_j^0, so it is at least x_j^0>=0. Hence

\[
\frac{E\|x\|_{L^2(0,\infty)}}{\sqrt{NL}}
 \ge E\sqrt{\frac1{NL}\sum_{j=1}^N Y_j}.
\]

The strong law and Fatou give liminf at least sqrt(E Y_1/L), even if the left side is infinite. For unit input, m(t)=(exp(a t)-1)/a when a!=0 and m(t)=t when a=0, and p(t)=2 int_0^t exp(c(t-s))m(s)ds>=0. If c<0, p tends to 2/(ac), so E Y_1/L tends to 2/(ac). If c>=0 and a<0, m tends to 1/|a| and p grows linearly or exponentially. If a>=0, p(t)>=t^2. In both c>=0 cases E Y_1/L tends to infinity. QED

## Horizon corollary (from review R8)

In this subclass, g1(T) is nondecreasing in T, and the block construction uses only finite horizons. For c<0 this gives

\[
\lim_{T\to\infty}g_1(T)\ge g_2(\infty)\ge g_2(T),
\]

so g2(T)-g1(T) tends to zero. Moreover neither infinite-horizon supremum is attained: Plancherel gives ||m||^2<||w||^2/a^2 strictly for every nonzero deterministic L2 input. Therefore, with the same convention for both criteria, **no gamma separates the two deterministic-input criteria at T=infinity**. Theorem F is finite-horizon only.

## Adapted disturbances change the gains (remark)

The theorems above exclude adapted disturbances. Parent-checked example: for c<0 and adapted mean-square inputs, apply Ito to P x^2:

\[
x^2-\gamma^2w^2+\frac{d}{dt}E[Px^2]
 =(1+cP+P^2/\gamma^2)x^2-\gamma^2(w-Px/\gamma^2)^2
\]

in expectation. Some P>0 makes the first coefficient nonpositive iff gamma>=2/|c|. Conversely, feedback w=kappa x+v with kappa increasing to |c|/2 drives the closed loop to mean-square resonance, and the squared ratio tends to 4/c^2. Thus the adapted infinite-horizon mean-square gain is 2/|c|, which strictly exceeds sqrt(2/(ac)) whenever sigma!=0. The reviewer also derived, without parent verification, that the adapted first-moment gain is at least 2/|c| (R6) and that adapted finite-horizon mean-square gains strictly exceed g2(T) (R7).

## Scope and unresolved obligations

- Theorems F and I keep the book's printed norm and constant matrices. They restrict disturbances to deterministic inputs and use an uncontrolled scalar channel with a regular dummy control.
- g1(T) is bracketed by strict inequalities, not computed. No synthesis formula follows.
- The infinite-horizon value is exact only for this inert subclass. It is not the stochastic H-infinity norm with adapted disturbances; see the remark.
- Adapted random inputs, nontrivial optimal controllers and arbitrary-dimensional synthesis remain unresolved. Expected squared-norm bounds do not, by Jensen alone, imply E||z||<=gamma E||w|| when w is random, because the denominator changes too.

## Computational check

[`check_scalar_literal_norm.py`](check_scalar_literal_norm.py) compares the kernel and moment-ODE representations of mean-square energy at 128, 256 and 512 Gauss-Legendre nodes, checks the Cameron-Martin path monotonicity used in Theorem F, and checks monotone unit-input block averages for four drift regimes. Output: [`scalar-literal-norm-check.json`](scalar-literal-norm-check.json); receipt: [`scalar-check-receipt.json`](scalar-check-receipt.json). These are numerical identity checks, not part of the proofs.

## Review record

- Prompt: [`scalar-referee.prompt.txt`](scalar-referee.prompt.txt), embedding the pre-revision text (sha256 7adbfefd917cb89dbb16d6d6e8f9250e14474b0038785833a0ddbc77035c2f1a).
- Command: `claude --model claude-opus-5-5 --effort max --safe-mode --no-chrome --tools "" --permission-mode dontAsk --no-session-persistence --output-format json -p <prompt>`. The init event and modelUsage both report claude-opus-5-5; the run took 797 s.
- Raw events: [`scalar-referee.events.json`](scalar-referee.events.json); extracted reply: [`scalar-referee.result.md`](scalar-referee.result.md).
- Dispositions: R3 (circular extension wording) fixed with causality and monotone convergence; R9 (preview model) fixed by stating the delayed model; R8 added as the horizon corollary; R11 "some gamma", the title and the computational-check reference fixed; c>=0 labelled open-loop; R5 checked by the parent and recorded as a remark; R6 and R7 recorded as unverified reviewer derivations; R10 and R12 retained as scope statements. R1, R2 and R4 verified the load-bearing steps with no change required.
