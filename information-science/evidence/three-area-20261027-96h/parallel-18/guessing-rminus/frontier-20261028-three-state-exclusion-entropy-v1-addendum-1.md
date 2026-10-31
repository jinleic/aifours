# Addendum: the one-hot entropy upper bound

**Status: WRITTEN, review pending.** In the notation of `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7`, one also has, for every joint conditioning variable `A`,

\[
\sum_{j=0}^2 H(S_j\mid A)\le2H(S\mid A).\tag{33}
\]

Together with the previous KL lower bound this gives the conditional sandwich `5H(S|A)/3 <= sum_j H(S_j|A) <= 2H(S|A)` for any distribution supported on at most three labelled states.

## Elementary proof

Fix a conditional probability vector `(p_0,p_1,p_2)`. With `f(x)=-x log x` and `g(x)=f(x)-f(1-x)`, the claimed upper bound is equivalent to `sum_i g(p_i)>=0`. The function `g` is antisymmetric about `1/2`, satisfies `g(0)=g(1/2)=0`, and has

\[
g''(x)=\frac{2x-1}{x(1-x)}\le0\quad(0<x<1/2).
\]

Hence `g>=0` and is concave on `[0,1/2]`. If all `p_i<=1/2`, the sum is nonnegative termwise. Otherwise exactly one, say `p_0`, exceeds `1/2`. Since `p_1+p_2=1-p_0<1/2`, antisymmetry gives

\[
\sum_i g(p_i)=g(p_1)+g(p_2)-g(p_1+p_2)\ge0.
\]

The last inequality follows from concavity and `g(0)=0`. Boundary values follow by continuity; average the fixed-condition inequality over `A`. The bound is not asserted sharp for exactly three positive probabilities, and does not resolve the guessing-number problem.
