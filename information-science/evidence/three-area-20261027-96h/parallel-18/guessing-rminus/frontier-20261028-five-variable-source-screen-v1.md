# 2026 five-variable source families versus one exact R-minus relaxation point

**Result.** For the exact original-variable entropy profile in `frontier-20261028-separator-bound-primal.json`, SHA256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`, two separately structured exact integer scans evaluated **both** infinite five-variable inequality families stated in Csirmaz and Csirmaz (2026), including an additional conditioning block W. Every substitution of pairwise disjoint original-variable blocks `A,B,C,D,Z,W` passed every finite staircase in Theorem 1 and every positive integer parameter in Theorem 2.

The point has objective `1847/276` and is feasible for the documented **partial source-certificate relaxation**. **It is not known to extend to the full three-branch source LP or to an actual distribution.** Thus this result does not show that either family cannot improve the full LP, does not settle the guessing number, and does not assert source novelty or independent proof of the published theorem.

## 1. Source, visual formula and exact scope

[Csirmaz and Csirmaz, “Information Inequalities for Five Random Variables,” *Computation* 14 (2026), 42](https://doi.org/10.3390/computation14020042), published 2 February 2026, supplies two proved infinite families via copy constructions, while stating a separate completeness conjecture. The locally fetched PDF `frontier-20261028-csirmaz-2026-five-variable.pdf` has SHA256 `401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6`. Theorems 1 and 2 were visually inspected on p17 and p19, not accepted solely from text extraction.

**Extraction warning.** The raw PDF text reader displaced the fraction in theorem 2: the actual image p19 equation (43) has `I(A;B|Z)` with coefficient **1**, and `k(k-1)/2` multiplies **C**. The code uses the visually observed formula below, not the mispositioned extracted text. The p19 PNG SHA256 is `03d53eb23677941a00571089020d2cdd73e471aabd8ca0beb0afa295f3d9f2d5`; p17 is `8698e00bdb0e08bc83ad4527827968f2cba4b7f13ac8785557d5c9db09e1e176`.

For any five finite-valued tuple variables A,B,C,D,Z, abbreviate

```
[ABCD] = -I(A;B)+I(A;B|C)+I(A;B|D)+I(C;D),
Zterm = I(A;Z|B)+I(B;Z|A),
Cterm = I(A;C|B)+I(B;C|A),
Dterm = I(A;D|B)+I(B;D|A).
```

For a finite downward-closed set `S` of nonnegative lattice pairs, put

```
(alpha,beta,gamma) = sum_((i,j) in S) binom(i+j,i) * (1,i,j).
```

The source’s Theorem 1 states

```
I(A;B|Z) + alpha([ABCD]+Zterm) + beta Cterm + gamma Dterm >= 0.
```

The source’s Theorem 2, visually read at equation (43), states for each positive integer k

```
I(A;B|Z) + k([ACBD]+Zterm) + k(k-1) Cterm/2 >= 0.
```

For any finite distribution, the required source `n`-copy exists for a sufficiently large n: sample copies of the tuple `(C,D)` conditionally independently over `(A,B)`, and couple Z independently over `(A,B)` with its original `(A,B,Z)` marginal. This recoupling need **not** preserve the original joint `(C,D,Z)` law, but every displayed expression uses only the `(A,B,C,D)` and `(A,B,Z)` marginals, which are preserved. Thus the source theorems apply to the original entropy expression. Conditional versions follow by applying them for each value of W and averaging. This explains the caller; the complete source proof itself has **not** been independently reviewed here.

## 2. Exact all-generation scan, not just a finite n sample

At the pinned rational base profile, with all quantities interpreted conditionally on W, put

```
g = I(A;B|Z,W),
v = [ABCD]|W + Zterm|W,
c = Cterm|W,   d = Dterm|W.
```

The profile passes all original Shannon inequalities, so `g,c,d>=0`. Every Theorem 1 staircase evaluates as

```
g + sum_((i,j) in S) binom(i+j,i) * (v+i*c+j*d).
```

If v>=0 all such values are nonnegative. If v<0 and c,d>0, the set of negative cells `v+i*c+j*d<0` is finite and downward closed. Including **all** negative cells yields the exact minimum over every finite downward-closed S; adding any nonnegative cell cannot improve it. If c=0 or d=0 and v<0, arbitrarily many negative cells lie on an axis, so a sufficiently long finite axis staircase would violate the inequality.

Two separately structured implementations scan all **47,534,520** substitutions modulo A/B swap with nonempty A,B,C,D and optional Z,W, all six pairwise disjoint. They use integer entropy numerators at scale 25944. Exactly **248** substitutions have v<0, representing **34** distinct `(g,v,c,d)` profiles. In every one the negative-cell minimization is finite and its exact minimal value is nonnegative; the smallest is zero. Thus all finite source staircases pass at this point. Empty A/B/C/D cases reduce to nonnegative Shannon expressions.

For Theorem 2, `[ACBD]` is not symmetric under A/B swap, so **both orders** were checked. For fixed blocks, put `b=[ACBD]|W+Zterm|W`. The exact value at parameter k is

```
g + k*b + k(k-1)*cterm/2.
```

For `cterm=0`, a negative b would eventually violate it; otherwise it is a convex quadratic, and its minimum over positive integers is achieved at the integers adjacent to the real vertex, clipped to k>=1. Both independent scans find no negative value for **any positive k**. This is a proof of the finite point test, not a proof that all real entropy vectors or the original optimization satisfy the candidate’s equality.

The total substitution count is checked independently by inclusion–exclusion:

```
[7^10 - 4*6^10 + 6*5^10 - 4*4^10 + 3^10] / 2 = 47,534,520.
```

## 3. Exact evidence and limitations

- Producer `frontier-20261028-conditioned-five-variable-full-scan.py`, SHA256 `df3a5a7f1c6467ea8cc4c48cf4d068f54ccecc877b4eba4eef7c5e933df33863`; receipt SHA256 `f2bbd6793dd6c0772c6832f2463c56d7aa90e61218b4e26ad7aca20c377c85bb`. Its original syntax failure was repaired before this successful run; no failed output was presented as a result.
- Independently structured scanner `frontier-20261028-conditioned-five-variable-independent.py`, SHA256 `d3e144e4c33448124561e0d7717fe5a0e1c2c3bcc9ec9178b2c10b0095c8c131`; receipt SHA256 `77c7f21e5ed3759360bbde9ff03abe9fd4038397a408407604a15a2bf5e64acd`. It uses a different base-7 enumeration split and quadratic-vertex test. Both return 248 negative-inner assignments, 34 distinct profiles, zero staircase violations, and zero Theorem 2 violations. The second run completed at **Wed Oct 28 18:05:12 PDT 2026**.
- The base point was separately checked against all original elemental Shannon rows, all graph FDs/symmetry and every disjoint conditioned four-variable `F_n`: `frontier-20261028-separator-primal-independent-result.json`, SHA256 `dac76b954fbd166eac73ce461d2bca641420991ebceb721093f49db6df54284d`.

Both scanners share the same point and source interpretation and were written in the same harness; they are not independent human or cross-model reviews. Pairwise-overlapping blocks/functions, other inequalities and other relaxation points are not exhausted. A bounded overlapping sample found no violation but is not an exhaustive result. The full-source optimal-face model hit its numerical time limit, so no exact full-source primal or new upper dual is claimed. No conclusion about worldwide prior art or original-target resolution follows.

**END.**
