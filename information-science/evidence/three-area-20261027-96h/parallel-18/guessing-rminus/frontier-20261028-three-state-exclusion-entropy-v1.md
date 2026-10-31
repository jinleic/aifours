# A one-hot entropy inequality for three syndrome states

**Status: WRITTEN, elementary KL proof; review pending.** If `S` takes at most three labelled values and `S_j=1{S=j}`, then for every random variable `A` jointly distributed with `S`,

\[
3\sum_{j=0}^2 H(S_j\mid A)\ge5H(S\mid A).\tag{29}
\]

This is stronger than the `3 sum H(S_j|A)>= (9/2)H(S|A)` obtained by pairwise Shannon subadditivity. It uses one-hot **mutual exclusion**, which the synthetic polymatroid in `frontier-20261028-three-syndrome-indicator-obstruction-v1.md` SHA-256 `789cc5d89adab8c4bea659837012a93380466f8dd3dd6d4b7d1143103214b6ac` does not satisfy. This inequality is an input toward the three-syndrome case, not by itself a proof of `Delta<=0` or a new unrestricted guessing bound.

## Proof

Fix `A=a` and write `p_j=P(S=j|A=a)`. Use natural logarithms and `f(x)=-x log x`, with the usual zero convention. Let `H=H(S|A=a)=sum_j f(p_j)` and `N=sum_j f(1-p_j)`. Then

\[
\sum_j H(S_j|A=a)=H+N.\tag{30}
\]

Any pair of indicators determines the three-state value of `S`, so

\[
\sum_{j<k}I(S_j;S_k|A=a)=2N-H.\tag{31}
\]

Since distinct indicators cannot simultaneously be one, the KL expression for mutual information gives, for each distinct `j,k`,

\[
I(S_j;S_k|A=a)\ge p_j\log\frac1{1-p_k},
\qquad
I(S_j;S_k|A=a)\ge p_k\log\frac1{1-p_j}.
\]

Average these two bounds and sum the three pairs. The right side is

\[
\tfrac12\sum_k(1-p_k)\log\frac1{1-p_k}=N/2.
\]

Thus `2N-H>=N/2`, so `N>=2H/3`; (30) gives `3 sum H(S_j|A=a)>=5H`. Boundary probabilities follow by continuity. Averaging over `a` proves (29) in any log base. No independence assumption on `A` is used.

For the guessing problem, if a law has three syndrome values, each indicator split has fibers of one or two syndrome values. Subject to review of the two-syndrome theorem, its four conditional entropy gates remain valid, and (29) may be imposed after conditioning on **any** subset of original vertex variables. The proof does not assert the constant `5/3` is sharp, nor does it claim formal verification or novelty.
