# Quantitative source-independent high-privacy rigidity

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:48:58 PDT 2026`.

## 1. Uniform explicit modulus

For 0<epsilon<=1/4, let X have ANY original all-Borel, all-event, full closed l1-unit-diamond-private law with finite first moment. Put

    Z=epsilon X,  Lambda(dz)=(1/4)e^(-||z||_1)dz,
    V=E||Z||_1,  D=V-2e^(-epsilon) >=0.                                 (1)

There is a UNIVERSAL finite constant C, independent of the law and epsilon, for which the written claim is

    W1_l1(Law(Z),Lambda) <= C[D^(1/3)+D+epsilon],                        (2)
    TV(Law(Z),Lambda) <= C sqrt[D^(1/3)+D+epsilon].                      (3)

The l1-ground W1 and Euclidean-ground W1 are equivalent. This applies to arbitrary laws, not only an optimizer or a staircase. In particular if `V<=2+delta`, delta>=0, it yields rates `W1=O((delta+epsilon)^(1/3))` and `TV=O((delta+epsilon)^(1/6))` as delta+epsilon->0.

For finite J, set `U=E|Z|^2` and `E2=U-4+8(1-e^(-epsilon))>=0`. A second source-independent inequality is

    D <= sqrt(2 E2)+2(1-e^(-epsilon)).                                   (4)

Thus if `U<=4+delta_J`, delta_J>=0, every all-law original-J nearopt has

    W1=O((delta_J+epsilon)^(1/6)),
    TV=O((delta_J+epsilon)^(1/12)).                                      (5)

Constants are universal. These rates are not claimed sharp. They give an independent quantitative route to W1/TV, not formal verification or automatic adoption of any earlier limiting candidate.

## 2. One-dimensional conditional stability lemma

Let Y be ANY real-valued random variable with a density and finite E|Y| whose scaled privacy satisfies `P(Y in A)<=e^(|h|+epsilon)P(Y in A+h)` for every real h and Borel A. Set `p+=P(Y>0)`, `p-=1-p+`. Group privacy implies for every t>=0

    P(Y>t)>=e^(-t-epsilon)p+,    P(Y<-t)>=e^(-t-epsilon)p-.

Let the two nonnegative differences be Delta_+(t), Delta_-(t), and set

    E=integral_0^infinity(Delta_++Delta_-)dt = E|Y|-e^(-epsilon)>=0.      (6)

For delta in (0,1/4), choose t in [delta,2delta] with `Delta_+(t)+Delta_-(t)<=E/delta`. The masses of (0,t] and [-t,0), denoted A+ and A-, differ by at most the privacy factor `e^(t+epsilon)`. Since

    A++A- <= 1-e^(-t-epsilon),
    A+-A- = (p+-p-)(1-e^(-t-epsilon))-(Delta_+-Delta_-),

and `1-e^(-t-epsilon)>=delta/2`, it follows that

    |p+-p-| <= C[delta+epsilon+E/delta^2].                               (7)

Choose delta=E^(1/3) when E is small, then use the trivial bound 1 when E is large (and the limiting argument if E=0). This proves `|p+-p-|<=C(E^(1/3)+epsilon)`.

The 1D W1 tail formula, decomposition into Delta_± and the two signs, then gives

    W1(Law(Y),standard two-sided Laplace)
      <= E+(1-e^(-epsilon))+|p+-p-|
      <= C(E^(1/3)+E+epsilon).                                           (8)

No assumption of symmetry is used.

## 3. Conditional tensorization without independence

Original full-D privacy gives a bounded all-point density f for Z. For each coordinate and every h, its pointwise ratio is at most `e^(|h|+epsilon)`. For almost every z2, normalize f(.,z2) to obtain the conditional law of Z1 given Z2=z2; it satisfies precisely the 1D condition of §2. The Z2 marginal also satisfies it. The mean of the conditional deficits E is `E|Z1|-e^(-epsilon)`, and the marginal deficit is `E|Z2|-e^(-epsilon)`.

Couple conditionals to an independent 1D Laplace, then couple the second coordinate to its 1D Laplace; the l1 cost is at most the sum of these two W1 costs. Jensen's inequality for x^(1/3) and (8) give (2), because the two average deficits are nonnegative and sum to D. This is a coupling argument, not a presumption that the original law is independent.

For (3), the full-shift density ratio also gives

    ||f(.-h)-f||_1 <= e^(||h||_1+epsilon)-1.

Convolve with a fixed smooth kernel scaled to delta D. The density's mollification error is O(delta+epsilon), as is Lambda's; the L1 difference of the two mollifications is at most `C W1/delta` by the coupling in §3 and the L1 gradient norm of the kernel. Choosing `delta=sqrt(W1)` when W1<1 and using TV<=1 otherwise gives (3).

## 4. From a J gap to a first-norm gap

For each coordinate, `S_i(t)=P(|Z_i|>t)>=e^(-t-epsilon)`. Put

    T_i=integral_0^infinity 2t |S_i(t)-e^(-t)|dt.

Since the difference above the lower exponential envelope is nonnegative,

    sum_i T_i <= U+4-8e^(-epsilon)=E2.                                   (9)

For nonnegative variables, monotone 1D quantile coupling gives

    W2^2(Law(|Z_i|),Exp(1)) <= T_i,

because `(a-b)^2<=|a^2-b^2|` and the corresponding W1 tail integral is T_i. Therefore `|E|Z_i|-1|<=sqrt(T_i)`, and summing proves (4). If `U<=4+delta_J`, then `E2<=delta_J+8epsilon`; combining (2)–(4) gives (5).

## 5. Status

The proof is WRITTEN from original event privacy and standard 1D transport, conditional distributions and mollification; it imports NO LAW642, MDA, PMLR or prior research result. No numerical, formal, cross-model, independent review, novelty or parent-acceptance claim is made. A disjoint review should check the small-interval sign argument (7), conditional all-shift inheritance, measurability of the 1D coupling, (9), and the smoothing inequality. Constants are unspecified but universal; no sharpness is asserted.
