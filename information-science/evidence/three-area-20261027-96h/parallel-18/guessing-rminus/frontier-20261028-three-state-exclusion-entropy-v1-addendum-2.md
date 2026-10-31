# Addendum: explicit KL decomposition

For the lower bound in `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7`, the step `I(S_j;S_k)>=p_j log(1/(1-p_k))` follows from the **full KL chain rule**, not from dropping arbitrary signed terms in a pointwise expansion. Since `S_j=1` forces `S_k=0`,

\[
I(S_j;S_k)=p_jD(\delta_0\Vert P_{S_k})+(1-p_j)D(P_{S_k\mid S_j=0}\Vert P_{S_k})
\ge p_j\log\frac1{1-p_k}.
\]

The second KL divergence is nonnegative; exchange `j,k` for the other displayed bound. Apply this argument in each conditioning fiber, with zero-probability cases by continuity. This adds proof detail without changing the theorem, coefficients or the independent upper-bound addendum.
