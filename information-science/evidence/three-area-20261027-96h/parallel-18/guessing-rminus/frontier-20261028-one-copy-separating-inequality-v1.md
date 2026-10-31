# A verified one-copy inequality separates the all-order `F_n` source-core point

## Claim and scope

Let `X_1,...,X_10` be **any jointly distributed finite random variables**, not necessarily a guessing strategy. For a nonempty subset represented by a ten-bit mask `m`, write `h(m)=H(X_i: bit i-1 of m is 1)`. Then the following homogeneous information inequality holds:

```
L(h) = -h(579)-h(706)-h(728)-h(729)+2h(730)+h(731)+h(733)
       -h(737)+3h(739)-h(746)+h(762)-h(763)-h(764)+h(835)
       -h(962)-h(965)+h(966)+h(975)-h(976)+h(978)+h(980)
       -h(982)-h(991)-h(1000)+h(1002)-h(1003)+h(1004)
       -h(1010)+h(1011)-h(1013)+h(1014)+5h(1017)
       -4h(1019)+h(1020)-h(1021)-h(1022) >= 0.
```

An explicit rational point in the previously defined R-minus **partial source-certificate relaxation** satisfies every original Shannon/FD/symmetry condition and every disjoint original-block conditioned `F_n` for all positive n, yet has `L(h)=-1/276`. Therefore that restricted infinite `F_n` family does not imply this one-copy inequality within that relaxation. The point is not asserted entropic and is not a guessing strategy.

**This is not yet a new original guessing-number bound.** The inequality may be known, a consequence of other known information inequalities, or redundant in the full source-copy LP. Novelty and priority have not been investigated.

## 1. Finite copy construction and exact certificate

Write `a,...,j` for `X_1,...,X_10`, and introduce `b'0` as a fresh conditional copy of b over

```
Y = {a,d,e,f,g,h,i,j} = all originals except b,c.
```

That is, sample `b'0` from the conditional law of b given Y, independently of the original ten-variable tuple given Y. The construction is valid for every finite original distribution, including zero-probability conditioning values (choose any kernel there). It gives

```
H(S,b) = H(S,b'0)  for every S subset of Y,
I(b'0; a,b,c,d,e,f,g,h,i,j | Y) = 0.
```

The exact certificate `frontier-20261028-branch1-farkas-cut-result.json`, SHA256 `ae9d207260ef0855f84c9ab3ab6f7d62128562db5ad051a0337bf9ccac6e6498`, contains **48** explicitly listed signed rows and integer multipliers. Its row masks use the ten original bits above and bit 10 for `b'0`. Among them are **33 standard CMIs** with nonnegative multipliers and **15** of the displayed copy equalities with unrestricted multipliers. Dividing every multiplier by 276, the weighted sum has coefficient **zero on every entropy containing `b'0`** and is exactly the 36-term L displayed above.

Therefore the same finite joint extension witnesses L as a nonnegative sum of CMIs plus zero copy equalities. As the original marginal is preserved, L is nonnegative for the original variables. The proof does not use R-minus functional dependencies, graph symmetry, singleton caps, a guessed distribution or a numerical LP objective.

## 2. Exact separation of the restricted source-core relaxation

The point is `frontier-20261028-source-closure-primal-frozen.json`, SHA256 `97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec`. Its original ten-variable coordinates satisfy all original Shannon elemental inequalities, all graph FDs/caps and generator symmetries; its objective is exactly `1847/276`. Two differently structured integer scans checked its original coordinates against all **13,729,980** disjoint `A,B,C,D,Z` substitutions, modulo A/B swap, and **every** integer n>=1 in the universal `F_n` family. The independent scan receipt is `frontier-20261028-closure-primal-independent-result.json`, SHA256 `e93c5172db80982a6d012a8557a32938028662e77aeb29de70b2143aad77aa0b`.

The exact cut verifier evaluates the displayed L at those base coordinates as **`-1/276`**. Thus no derivation using only that relaxation’s checked original Shannon/FD/symmetry constraints and the stated disjoint-block `F_n` family can establish L>=0 on all points of the relaxation. This is a separation of a formal outer-relaxation point, not a counterexample to the true information inequality.

The earlier auxiliary values of this point cannot be extended to the publisher’s full branch cone: see `frontier-20261028-all-order-copy-obstruction-addendum-2-v1.md`, SHA256 `eab2a42b99840a6f6845da1256b207e6c60cae14ea2febd3fb961dc4dd453956`. More strongly, L(h)<0 itself proves that **no different b'0 one-copy Shannon extension can exist for this exact ten-variable base profile**. It does not exclude other feasible base profiles.

## 3. Reproducible verification and negative controls

- `frontier-20261028-branch1-farkas-cut.py`, SHA256 `9cd72ed64ebf0e238b2164c413ce54eb36b58767a3808e23914a23de8da1d333`, generated the proposal. The bounded HiGHS screen reported the fixed-base one-copy LP infeasible and returned a 48-row float ray; Z3 then supplied rational multipliers on that support. **Neither solver’s status is used as the mathematical proof.**
- `frontier-20261028-branch1-cut-independent.py`, SHA256 `8115b7648fbdbbac80b0a08c252a5f0060348f518b44a6992613f78531c2feb5`, imports neither generator nor optimizer. It reconstructs each CMI from its `(i,j,Z)` masks, checks all 15 copy equalities against the explicit conditional-copy identities, checks the multiplier signs, sums exact rational vectors, verifies all copy-containing coefficients cancel and checks the announced base vector and point value. Receipt `frontier-20261028-branch1-cut-independent-result.json` has SHA256 `1597bb44bea62b842c65a973ec08a4b8867af1a92a979225458e280464f3e915`.
- Two in-memory mutations were rejected for their intended reasons: a negative CMI multiplier as `NEGATIVE_INEQUALITY_WEIGHT`, and a modified CMI term as `INVALID_CMI_TERMS`. The input files were not changed. The exact checker’s observed completion clock was **Wed Oct 28 17:46:22 PDT 2026**.

The code, certificate and mathematical interpretation were produced in the same harness and have not received independent human, cross-model or formal review. The original graph is a previously visually transcribed source graph. The next substantive question is whether adding this exact valid L, and its graph-symmetry images, to the R-minus copy/FD relaxation yields a new coefficient certificate below `1847/276`. No such improvement is claimed in this packet.

**END.**
