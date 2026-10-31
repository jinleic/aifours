# Overlap checks for the five-variable family separator

**Additive scope clarification.** This concerns `frontier-20261028-fivevar-family-separation-v1.md` (SHA-256 `82a56e0c8775eca1e37f547be4e4b519ce9a56cd42f882f6af412e4b367a8774`). Its original conclusion was explicitly restricted to disjoint block substitutions. The source inequalities and new gluing inequality remain pending independent scientific review and novelty clearance.

The pinned five-variable separating polymatroid `frontier-20261028-fivevar-family-separator-witness-v2.json` (SHA-256 `84ac1e3c87db445e0c4b3d4eb9388c58f040591cd8ca6b799c93630e3ac187f4`) satisfies the previously named `F_n` family under **all** nonempty `A,B,C,D` subsets and any `Z` subset of its five variables, including overlaps, for every positive integer `n`. Two differently batched exact scans each checked `15,252,992` substitutions modulo `A/B` exchange, using respectively quadratic-vertex and first-difference minimization; both have minimum twice-slack zero.

However, the same point does **not** satisfy every overlapping substitution of the pinned Csirmaz–Csirmaz (2026) Theorem 2. An exact counterexample in the five-bit mask convention of the predecessor is

```
A=1, B=4, C=16, D=8, Z=16, W=0, k=7.
```

Here `C` and `Z` coincide. In the source theorem's notation `g=I(A;B|Z)=2758`, `[ACBD]+Zterm=-2758`, and `Cterm=422`; the exact slack is `2758+7*(-2758)+21*422=-7686`. Thus the predecessor's separation must **not** be generalized from its stated disjoint Csirmaz substitutions to overlapping ones, or to the full literature. The failure does not affect the universal `Psi` proof, its Shannon-cone separator, the original disjoint comparison, or the source-LP no-improvement result.

## Evidence

* Overlapping `F_n` scan `frontier-20261028-fivevar-separator-overlap-fn-scan.py` SHA-256 `48ceb1cb4caf60d5129e2453cd627681fcf533727876e592794a6c6278642f9f`, receipt SHA-256 `e75089ea9fdd8ada256a473af3a60f503a882eff06bfc35255b78dc8b83862fb`.
* Independent-structure replay `frontier-20261028-fivevar-separator-overlap-fn-independent.py` SHA-256 `c6c9a08d5a1e7ddb139633ac2829a3e57048c6420334dfb138b4f2702cac7318`, receipt SHA-256 `96f0be7a26992bf36b116a8eb85f417002bd6cfc2fb0d2ac2e1effb54735ecc9`.
* Overlapping source-Theorem-2 scan `frontier-20261028-fivevar-separator-overlap-source2-scan.py` SHA-256 `3a5aa31ad79c2fe81738d6b22896c6f7fb118e11c32bbe1dd8c26225528c104d`, receipt SHA-256 `40b15796782c6c0fadaf61b4e6db4fa95f5d384803332cb756c0319f7a08e3ce`. It stopped at the displayed exact violation; it is not an exhaustive nonviolation result.

No original guessing-number bound, entropy realization, cross-model review or novelty clearance follows.
