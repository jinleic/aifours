# Exact polynomial barrier for five-word FD supports

**Status: WRITTEN corollary; scientific review pending.** Assume the five-point theorem `frontier-20261028-five-point-k4free-bound-v1.md` SHA-256 `7f2103f8f47ea57830836a5e7e8887577fef8876b1af8b2ca7f51075ae3b7ca0`. Let `W` be any set of at most five original R-minus FD-consistent words, on any finite vertex alphabets, and let `t[v,a]` be arbitrary nonnegative real weights. Then

\[
\left(\sum_{w\in W}\prod_{v=1}^{10}t[v,w_v]^2\right)^3
\le\prod_{v=1}^{10}\left(\sum_a t[v,a]^3\right)^2.
\]

This includes all nonnegative integer weights in the strict-gain criterion of `frontier-20261028-balance-polynomial-equivalence-v1.md` SHA-256 `70e90a3236d735d74dbd71f68577f97f778e98eafdc49137e30aa4fe36178ec1`. Hence any positive polynomial witness must have at least six support words. It does not rule out such a witness on six or more words.

If any entire vertex weight row vanishes, both sides are zero. Otherwise normalize `Q_v(a)=t[v,a]^3/sum_b t[v,b]^3` and let

\[
S=\sum_{w\in W}\prod_v Q_v(w_v)^{2/3}.
\]

The Gibbs variational identity gives `log S = max_P [H(P)+(2/3) sum_v E_P log Q_v(X_v)]`, where `P` ranges over laws supported on `W` and the zero cases are interpreted by continuity. Every such law obeys `H(P)<= (2/3) sum_v H(P_v)` by the five-point theorem. Gibbs' inequality gives `E_P log Q_v <= -H(P_v)`. Thus every expression inside the maximum is nonpositive, so `S<=1`. Clearing the row normalizations and cubing yields the displayed inequality. The zero-`S` case is immediate.

This is conditional on the written five-point theorem and inherits its graph/FD scope and review status; it is not a global polynomial impossibility result.
