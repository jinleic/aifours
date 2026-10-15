# An average-optimal policy need not exist in a four-state blind POMDP

Date: 2026-10-14 (America/Los_Angeles).
Evidence: classical written proof; not kernel-checked. This is a counterexample to an unrestricted optimizer-existence reading, not a new general POMDP synthesis method. Novelty is unestablished.

## 1. Exact claim and expected-average convention

The theorem below is self-contained. Its relation to the book's article 部分可观马尔可夫决策过程的性能优化 (汪德新, 曹希仁), pp. 653–655 (PDF 674–676), is conditional on the **expected-average, unrestricted-policy reading** documented in §7. It does not address a model with an additional communicating, unichain, ergodicity or mixing hypothesis.

For the usual expected-average reading, write

\[
 J(\pi)=\lim_{T\to\infty}\mathbb E^\pi\!\left[
 T^{-1}\sum_{t=0}^{T-1}r(X_t,A_t)\right].
\]

In this example the sample averages converge almost surely for every policy; bounded convergence makes the expected-average and expected-liminf-average criteria identical. The theorem optimizes their **expectations**, not an unspecified ordering of random sample-path limits.

**Theorem.** There is a four-state, two-action, one-observation POMDP, with rational transition probabilities and rewards in {0,1}, starting from a known state, such that

\[
 \sup_\pi J(\pi)=1,
 \qquad J(\pi)<1\quad\text{for every policy }\pi.
\]

An admissible behavioral policy is a sequence of probability kernels \(\pi_t(\cdot\mid h_t)\) on {W,C}, where \(h_t\) is its observation/action history. Policies can be time-dependent and have unbounded memory. We also allow mixtures using private randomness independent of plant noise. All these policies have a well-defined expected average reward here. For every positive epsilon an explicit finite-memory deterministic policy is epsilon-optimal.

## 2. The model

States are B (not ready), G (ready), H (successful absorption), and L (failed absorption). Actions are W (wait) and C (commit). Initial state: B. Every state emits the same observation. Fix q in (0,1), with q = 1/2 for the rational example.

| Current state | W transition | C transition | Reward for either action |
|---|---|---|---|
| B | q B + (1−q) G | L | 0 |
| G | G | H | 0 |
| H | H | H | 1 |
| L | L | L | 0 |

Rewards are received before the state transition. Even if rewards are additionally observed, the argument is unchanged: every reward before the first C is zero, and the state after C is absorbing and uncontrollable.

## 3. Reduction of every admissible policy to its first commit time

Before the first C the only possible observable history is \(h_t^W\): t W actions, constant observations, and zero rewards if rewards are observed. Put \(p_t=\pi_t(C\mid h_t^W)\). For a behavioral policy each \(p_t\) is a fixed number. If N is the number of W actions before the first C, the chain rule gives the joint probabilities

\[
 \mathbb P(N=n)=p_n\prod_{t<n}(1-p_t),\qquad
 \mathbb P(N=n,X_n=B)=q^n p_n\prod_{t<n}(1-p_t).
\]

Consequently

\[
 \mathbb P(N=n,H\text{ is reached})=(1-q^n)\mathbb P(N=n).
\]

These identities do not condition on null events. They remain valid after integrating over a private policy seed independent of plant noise, so they include arbitrary mixtures and correlated private randomization. Equivalently one can presample all private random choices; before commit, N then depends only on those choices, not on the hidden waiting-transition coins.

If N = infinity, every action is W, so rewards are zero forever, regardless of the hidden readiness state. Once C occurs the state is H or L and no later action can change it.

For every sample path, the time-average reward therefore converges to the indicator of eventual H absorption. Bounded convergence gives, for every policy,

\[
 J(\pi)=\mathbb E[(1-q^N)\mathbf1_{\{N<\infty\}}]
       =\sum_{n=0}^\infty \mathbb P(N=n)(1-q^n).
\]

## 4. Nonattainment and approximating policies

The exact gap is

\[
 1-J(\pi)=\mathbb P(N=\infty)
   +\sum_{n=0}^\infty \mathbb P(N=n)q^n.
\]

If P(N = infinity) is positive the gap is positive. Otherwise the countable probabilities P(N=n) sum to one, so some finite n has positive probability, and its strictly positive summand makes the gap positive. This also covers distributions with infinite expected N and arbitrarily heavy tails. Therefore no admissible policy attains reward one.

The deterministic policy W^n C followed by arbitrary actions has

\[
 J_n=1-q^n\longrightarrow1.
\]

Hence the supremum is one. For q = 1/2 and epsilon>0, choose the least nonnegative n with 2^(−n) <= epsilon (n=0 suffices when epsilon≥1). A counter with n+1 states implements this policy, with no observation of the hidden state.

There is an explicit improvement map, not just nonattainment. If P(N < infinity) > 0, replace N by N+1 (and leave infinity unchanged). The improvement is

\[
 (1-q)\,\mathbb E[q^N\mathbf1_{\{N<\infty\}}]>0.
\]

This new stopping rule is implementable using the same private seed and an extra initial W. If N is infinity almost surely, W C already gives positive reward 1−q.

## 5. Checks against common escape routes

### Unlimited memory and randomness do not repair nonattainment

Section 3 covered every private random first commit time, not just constant or finite-memory controllers. A distribution supported at very large finite times still has E[q^N; N < infinity] > 0. Placing all mass at infinity makes the reward zero, not one.

### The limit exists

The average reward converges on each path to zero or one; expectation converges by bounded convergence. Replacing the ordinary expected limit by expected liminf, expected limsup, liminf expected reward, or limsup expected reward does not alter the result.

This statement concerns expectation-type criteria. The limiting random payoff is \(\eta=\mathbf1_H\); \(E\eta=P(\eta=1)=J(\pi)\). In contrast, \(\operatorname{ess\,inf}\eta=0\) for every policy, so every policy is optimal under the almost-surely guaranteed-average criterion. Also \(\operatorname{ess\,sup}\eta=1\) is attained by W C. These are different objectives, not alternate interpretations silently covered by the theorem.

### Belief states do not manufacture an optimizer

After n W actions, the probability of G is 1−q^n. This converges to one but never equals one at any finite n. A policy that waits for belief exactly one waits forever and receives zero. A belief representation is sufficient information, but it cannot make a missing maximizing policy exist.

### Full observation is a decisive positive control

If readiness is observed, W until G and then C reaches H almost surely. The readiness time is finite almost surely, so its finite random delay contributes zero to the limiting average and reward one is attained. This change of observation model removes the obstruction; it is not an admissible fix inside the blind model.

### Randomized stationary policies can approximate but not attain

If each precommit action is C with a fixed probability c in (0,1], then P(N=n)=c(1−c)^n and

\[
 J(c)=1-\frac{c}{1-q(1-c)}.
\]

For q=1/2 this is (1−c)/(1+c), tending to one as c decreases to zero. At c=0 the policy never commits and has reward zero. Thus J is not upper semicontinuous at zero: \(\lim_{c\downarrow0}J(c)=1>J(0)=0\). Compactness of the policy parameter interval therefore does not yield a maximizer by the extreme-value theorem.

Nonattainment already holds within randomized memoryless policies (the displayed c family), hence within randomized k-state controllers for every fixed k≥1. It also holds among deterministic open-loop and deterministic belief-stationary policies: the precommit beliefs after different numbers of W actions are distinct, so each W^n C is implementable in those classes. These are nonattainment statements about this instance, not memory bounds for general POMDPs.

By contrast, stationary deterministic memoryless policies both earn zero. A **time-homogeneous** deterministic controller with at most k memory states, a fixed initial memory state and no separate clock, on constant observations, either first commits by step k−1 or never commits: repeating a precommit memory state would repeat W forever. Hence its maximum is \(1-q^{k-1}\), attained by the k-state counter W^(k−1) C. A time-dependent controller supplied an external clock is not in this finite class.

## 6. What this settles, and what it does not

No map, computable or not, assigns an expected-average-optimal policy to **every** finite POMDP: some inputs have no admissible maximizing output. This is a complete negative answer to the universal optimizer-existence reading, already within finite rational models. It is not an undecidability proof.

Not settled: deciding whether a given finite rational POMDP has an optimizer; constructing one when it exists; existence under communicating, unichain, ergodic or mixing hypotheses; general continuous-state optimization; or the book's broader methodological request. A selector allowed to return “no optimizer” is a different problem. No novelty claim is made.

Chatterjee–Saona–Ziliotto, arXiv:1904.13360v2 (2022), Theorem 2.9 establishes finite-memory epsilon-optimal strategies for finite POMDPs, for the expected liminf-average criterion. Definition 3.1 and Corollary 3.2 concern their promise approximation decision problem; §3.1 attributes its undecidability lower bound to earlier work and adds the recursively enumerable upper bound. These locators and statements were checked directly against the primary HTML by this package's author; the no-tools referee did not independently fetch them. They are cited primary results, not theorems proved here. Our example is consistent with their epsilon-optimality result: epsilon-optimal finite-memory policies exist here, but epsilon>0 cannot in general be replaced by zero.

## 7. Relation to the printed question

The package's author read all three article page images, including its signed end and reference list, and the front matter/thematic table of contents. These inspected sources present separately signed articles and state no shared POMDP assumptions. No communicating, unichain, ergodic or mixing restriction appears in the three-page POMDP article. This is a source-local observation, not a claim about its cited papers or every page of the volume.

Book p.654, policy information:

> 基于在时刻t已有信息（包括输出历史及行动历史），我们可以选择一个行动

“Based on information available at time t (including output and action histories), we can choose an action.”

Book p.654, general policy class:

> 在最一般的情况下，一个POMDP系统的策略是关于整个系统输出历史和行动历史的一个函数。

“In the most general case, a POMDP policy is a function of the entire output and action histories.”

The optimizer request is posed before the article subsequently discusses restrictions to smaller policy subspaces. Its general-history formulation does not restrict the requested optimizer to deterministic current-output policies. Reading “function” deterministically already includes every W^n C and suffices for nonattainment; allowing distribution-valued policies gives the larger class proved in §3.

The displayed formula is

\[
 \eta^u(x)=\lim_{T\to\infty}\frac1T
 \left\{\sum_{t=0}^{T-1}f(X_t,u_t)\mid X_0=x\right\}.
\]

The braces condition on the initial state but show **no expectation symbol**. The prose continues:

> 则我们希望解决的问题是如何选取最优的策略u使得上式取得最大值。

“We wish to solve how to select an optimal policy u making the expression above attain its maximum.”

The expected-average convention is the standard numeric reading adopted here, **not a verbatim repair of the printed formula**. Under that convention, the quoted general-history policy class, and without extra recurrence restrictions, the universal request presupposes an optimizer that need not exist, as the theorem proves. Under a pathwise worst-case reading, the same counterexample does not refute existence (§5). Under a methodological reading, the result identifies a necessary scope correction rather than a full optimization theory.
