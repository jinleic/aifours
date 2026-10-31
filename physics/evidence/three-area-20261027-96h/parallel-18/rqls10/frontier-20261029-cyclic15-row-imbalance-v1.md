# An all-phase spectral imbalance forced by cyclic 6D incidence

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:30:13 PDT 2026. This is a necessary condition for the unitary-cyclic-equivariant G6 problem of `frontier-20261029-cyclic15-unrestricted-multiplicity-v1.md` SHA-256 `128c8d68c92ef4db22169b0376e7a97758efa4ef18cdb086ecf4914de5482de7`. It imposes no number-field, rationality or phase restriction, but does not exclude all cyclic solutions.

## General row inequality

Let `zeta=exp(2 pi i/15)`, and let j,k index two U eigenvectors with eigenvalue exponents a_j,a_k. For the basis `v_d,U^(-d)v_d`, d=2,5,7, write `p_dj=|<e_j,v_d>|²` and `q_j=p_2j+p_7j=1/2-p_5j`. Orthogonality of its j-th and k-th rows, the triangle inequality and Cauchy–Schwarz imply

`|1+zeta^(5 Delta)|² (1/2-q_j)(1/2-q_k) <= M_Delta² q_j q_k`,

where `Delta=a_k-a_j (mod 15)` and

`M_Delta=max(|1+zeta^(2 Delta)|, |1+zeta^(7 Delta)|)`.

Indeed the left side is the squared magnitude of the d=5 contribution; the other two contributions have total magnitude at most `M_Delta [sqrt(p_2j p_2k)+sqrt(p_7j p_7k)] <= M_Delta sqrt(q_j q_k)`. Also `1/6<=q_j<=1/2`, because each of the three U^5 eigenspaces receives v5 population exactly 1/3.

## Explicit imbalance for a 2D U^5 eigenspace

Suppose one U^5 eigenspace is 2-dimensional, with U-exponents differing by `Delta=3` or `12` modulo 15. Its v5 populations sum to 1/3, so `q_j+q_k=2/3`. Here `|1+zeta^(5 Delta)|²=4` and both d=2,7 coefficients have squared magnitude

`K=(3-sqrt(5))/2`.

The general inequality becomes

`(4-K)(q_j-1/3)² + (K-1)/9 >= 0`,

or explicitly

`|q_j-1/3| >= (1/3) sqrt((3sqrt(5)-5)/10)`.

The same bound holds for q_k and, equivalently, for the deviation of either v5 population from 1/6. Thus one of the two v5 populations is at most `1/6-delta` and the other at least `1/6+delta`, with `delta=(1/3)sqrt((3sqrt(5)-5)/10)>0`. Equal or nearly equal populations in such an eigenspace cannot occur in any cyclic lift, even over arbitrary real fields. The statement remains valid for any eigenbasis of U, including degenerate eigenspaces.

## Scope

This gives a continuous all-variable restriction, not a no-go for all spectra. It does not cover noncyclic realizations and does not imply that an imbalanced population pattern has a compatible Gram matrix. The row inequality, exponent caller, and earlier irreducibility reduction need independent written review; no formal or novelty claim is made.
