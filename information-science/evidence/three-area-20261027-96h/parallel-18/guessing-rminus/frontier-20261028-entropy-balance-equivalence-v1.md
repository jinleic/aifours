# Strict guessing gain is equivalent to a positive entropy-balance gap

**Status: WRITTEN with exact incidence-matrix checking.** This is a reduction of the original unrestricted R-minus problem, not a strict-gain law and not a proof that no such law exists. The necessary type-class and total-decoder construction is written out below; no formal proof, cross-model review or novelty clearance has been performed.

## The equivalence

For any finite joint law satisfying all original-neighbour R-minus FDs, define

\[
\Delta(X)=H(X_V)-\frac23\sum_{v=1}^{10}H(X_v).
\]

Then the following are equivalent:

1. The unrestricted guessing number of the original R-minus graph is strictly greater than `20/3`.
2. Some finite-alphabet original-graph FD law has `Delta(X)>0`.

Since the explicit ten-triangle code attains `20/3`, the original equality question is consequently equivalent to the **unrestricted graph-FD entropy inequality** `H(X_V) <= (2/3) sum_v H(X_v)`. This equivalence does not assert that inequality is true.

The direction 1 implies 2 is immediate. If a finite alphabet of size `q` has more than `q^(20/3)` fixed words, take the uniform law on those words. Each singleton entropy is at most `log q`, while the joint entropy is `log |W|`; hence `Delta>0`.

The converse uses the special invertible triangle cover. Let `A` be the `10 x 10` matrix whose rows are vertices and whose columns are the ten triangles in the preceding packet. Each row has three ones, so `A 1=3 1`, and exact integer/Fraction elimination gives `det A=3`. The triangles are

```
123  145  167  239  2,7,10  389  4,5,10  4,8,10  569  678
```

Every triangle `t` supplies a valid independent binary FD factor: on its three vertices put a uniform XOR-zero triple and at other vertices put constant zero. Its joint entropy is two bits, its three active singleton entropies are one bit, and its `Delta` is zero. All decoders use original neighbours and are total on the full binary domain.

Suppose a finite FD law `P` has `Delta(P)>0`, with singleton entropy vector `h` in bits. We may assume `P` rational: a sufficiently close rational law on the same finite support preserves all FDs and preserves the strict gap by entropy continuity. Choose an integer `C` larger than every component of `A^{-1}h` and define the positive real vector

\[
\lambda=C\mathbf1-A^{-1}h,\qquad A\lambda=3C\mathbf1-h.
\]

Choose a positive rational vector `lambda_tilde` with `|lambda_tilde_t-lambda_t|<eta`, where `eta<Delta(P)/40`. Take `k` independent copies of `P` and `k lambda_tilde_t` copies of the triangle-`t` factor, with `k` chosen to make every multiplicity integral. This product is another original-graph FD law `P'`. Its singleton entropies differ from the common target `3kC` by at most `3k eta`; each vertex belongs to exactly three chosen triangles. Triangle factors have zero balance gap, so `Delta(P')=k Delta(P)` exactly. Hence

\[
\begin{aligned}
H(P')-\frac{20}{3}\max_v H(P'_v)
&=\Delta(P')-\frac23\sum_v\bigl(\max_uH(P'_u)-H(P'_v)\bigr)\\
&\ge k\bigl(\Delta(P)-40\eta\bigr)>0.
\end{aligned}
\]

Thus `P'` has a strict entropy ratio above `20/3` and rational probabilities.

## From the law to an actual finite guessing strategy

For a positive integer `n` divisible by all probability denominators, take all length-`n` sequences of joint support words having empirical distribution exactly `P'`. Each vertex's projected sequence lies in its own marginal type class. Let the common new alphabet size be the maximum of the ten marginal type-class sizes; inject each vertex's type class into that alphabet, padding unused labels.

A decoder first interprets valid neighbour labels as their neighbour sequences, applies the original coordinatewise FD decoder at every position, and returns the injected label of the resulting own sequence when it is in the vertex's type class; otherwise it returns a fixed default label. This defines a full-domain original-neighbour decoder. Every joint type sequence is a fixed word, and the encodings are injective, so the count is at least the joint type-class size. Standard elementary type-class bounds, for example `(n+1)^-|support| 2^(nH(P')) <= |T(P')| <= 2^(nH(P'))`, and the corresponding marginal bounds give

\[
\lim_{n\to\infty}\frac{\log |T(P')|}{\log \max_v |T(P'_v)|}
=\frac{H(P')}{\max_v H(P'_v)}>20/3.
\]

For sufficiently large admissible finite `n`, the constructed alphabet and full decoders therefore give a strict guessing-number gain. This proves 2 implies 1.

## The two exact certificate identities narrow the search

The single-diamond certificate in `frontier-20261028-single-diamond-defect-gate-v1.md` (SHA-256 `2ea2c5c414dc0a88dcecfe9da1423d4117bb06cc8420b01965d8f2e4604c4011`) gives, for every original FD law,

\[
\Delta(X)=-\sum_{i=1}^{62}a_i\,\overline{I_i}-\tfrac13\overline{J_1}.
\]

Consequently the original strict-gain problem is also equivalent to finding a finite original FD law for which `average_G J_1 + 3 sum_i a_i average_G I_i < 0`. A negative averaged Ingleton defect alone is not enough: the four-word example in that packet has negative averaged defect but negative `Delta`. The representable-rank proof establishes `Delta<=0` for every uniform affine finite-field rank law; it does not establish it for general FD distributions.

## Exact matrix evidence

`frontier-20261028-triangle-balance-matrix.py` SHA-256 `93272bffe6c0dc724cddb849790c8e6879940445125306888b91424fdd734cc8`; receipt SHA-256 `5bb5fc9254e205cf5f7b1cabb8373c1aebcfad546d7e49261441b8e5bd188796`. It independently checks all chosen triangle edges and vertex multiplicities, computes the determinant and full inverse using `Fraction`, and verifies `A A^-1=I` exactly. The receipt includes the matrix and inverse.

This result converts the unrestricted task into an entropy-balance search and provides a rigorous route from any strict witness back to finite full-neighbour decoders. It does not by itself decide whether a positive-gap FD law exists.
