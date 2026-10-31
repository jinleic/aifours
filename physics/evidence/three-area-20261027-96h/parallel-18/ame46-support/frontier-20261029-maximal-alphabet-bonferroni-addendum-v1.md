# Additive simplification: a Bonferroni bound for the local alphabets of maximal coefficients

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 09:55:17 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed or adopted. This is an elementary Bonferroni/second-moment bound, not a claimed new method. It strictly simplifies the earlier proof `frontier-20261029-maximal-four-alphabet-theorem-v1.md`, SHA-256 `d73b3808b455eefec56f4dc3049c85118da9a9045ae2c3189ad21e21be52583b`, without editing or withdrawing its valid longer argument.

## 1. General bound

Let ψ be a normalized complex AME(4,6) state in any product basis. Let P be all t coefficient positions of modulus1/6. At each party i choose any set H_i of h_i basis symbols **absent from every P word**, and define `J(x)=#{i:x_i∈H_i}`.

All six two-party marginals of the same state are `I_36/36`, so for `p(x)=|ψ_x|²`,

`E[J]=Σ_i h_i/6`,  `E[C(J,2)]=Σ_{i<j}h_i h_j/36`.

For every support word x,

`J(x)−C(J(x),2) ≤ 1_{x∉P}`.                                     (B)

Indeed at a P word J=0; at any other word the left side is `0,1,1,0,−2` for J=0,1,2,3,4, at most1. Summing (B) against p and using that each P word has probability1/36 gives

`6Σ_i h_i−Σ_{i<j}h_i h_j ≤ 36−t`,

or

**`t ≤ 36−6Σ_i h_i+Σ_{i<j}h_i h_j`.**                           (T)

This uses the six given marginals of one state. It imports neither no-OLS(6), no-Hamming-one, fixed support size nor residual block assumptions.

## 2. Immediate consequences for the original support problem

- If maximal positions use at most4 symbols at **every** party, take h=(2,2,2,2): `t≤12`. This proves the preceding four-alphabet theorem in one inequality and makes its longer full-symbol case split unnecessary.
- If maximal positions use at most5 symbols at every party, take h=(1,1,1,1): `t≤18`.
- If at least two parties each omit a symbol from P, take h=(1,1,0,0): `t≤25`. Hence t≥26 forces at least three parties to use **all six symbols in P**.
- If at least three parties omit a symbol from P, take h=(1,1,1,0): `t≤21`. Hence t≥22 forces at least two parties to use all six symbols in P.
- If two parties omit2 symbols from P and the other two omit1, take h=(2,2,1,1): `t≤13`. Thus a58-term zero-excess search with t=14 cannot fix that maximal-alphabet pattern.

The standard row count `N≥72−t` then gives restricted-basis lower bounds: if P uses≤4 symbols at each party, N≥60; if P uses≤5 at each party, N≥54. These are restricted maximal-alphabet statements, not universal support minima. In particular an unrestricted state may use all six symbols in P, and no global lower-bound upgrade follows.

## 3. Equality pattern

If equality holds in (T), every positive-probability word outside P must satisfy `J∈{1,2}`; otherwise the pointwise slack in (B) is positive. At h=(2,2,2,2), t=12, the remaining probability is24/36 and `E[J]=48/36`; hence every nonmaximal word has exactly two H coordinates. This explains the two-active-party sector pattern in the known60-term construction as a forced equality condition, rather than an arbitrary ansatz.

At h=(1,1,1,1), t=18, the nonmaximal probability is18/36; exactly12/36 lies at J=1 and6/36 at J=2. These are necessary mass conditions, not a witness or existence result.

## 4. Scope and evidence

All numerical values above are integer arithmetic in (T). The preceding Fraction control (`frontier-20261029-maximal-four-alphabet-controls-v1.json`, SHA-256 `bbb6db689e5229435b5c3387c8c35bc1a99a072fc95e3c774923c0b6907563da`) remains a correct control of its longer proof; it is not needed for this short argument. No priority, exact global minimum, human review, independent-model-family review or formal proof is claimed.
