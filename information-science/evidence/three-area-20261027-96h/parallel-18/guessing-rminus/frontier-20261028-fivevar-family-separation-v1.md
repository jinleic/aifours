# Five-variable gluing inequality versus two pinned infinite families

**Status: WRITTEN with two independent-structure exact checks; source-theorem and scientific review pending.** This is a restricted algebraic separation, not a novelty claim, not an entropic construction, and not an improved R-minus guessing-number bound. The universal five-variable inequality `Psi>=0` is stated and proved in `frontier-20261028-five-variable-gluing-inequality-v1.md` (SHA-256 `ef9cb87907bd255d75f4154a11fe5471072e8959e622376bea6469ad60462df4`).

## Exact separating polymatroid

Order variable bits as `C,R,H,P,Q`, least to most significant. The following **integer** values define a five-variable polymatroid `r`, with `r(empty)=0`:

```
 0–7:      0 25867 22526 38376 23164 35407 35673 38376
 8–15: 18392 32016 31378 44525 41556 41556 44525 44525
16–23: 20406 35196 29735 44525 32493 44525 41822 44525
24–31: 32438 38376 38587 44525 44525 44525 44525 44525
```

It satisfies all 85 five-variable elemental Shannon inequalities, but the 15-term gluing inequality has `Psi(r)=-9329`. In addition, it satisfies:

* every `F_n` from `frontier-20261028-all-order-copy-obstruction-v1.md`, under all **480 ordered** disjoint block substitutions on these five variables with four nonempty roles and optional disjoint conditioning, for every positive integer `n`;
* both pinned Csirmaz–Csirmaz (2026) five-variable Theorems 1 and 2 under all **600 ordered** disjoint substitutions of nonempty `A,B,C,D` and optional disjoint `Z,W`, for every finite downward-closed staircase in Theorem 1 and every positive integer parameter in Theorem 2.

The source formulas and their stated interpretation are in `frontier-20261028-five-variable-source-screen-v1.md` (SHA-256 `e8d1910e7cd2024b5a03c9cc6688fcf529ea3d75345b95033e3c801b1ec4e9cd`); its pinned publisher PDF has SHA-256 `401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6`. The source theorem proof has not been independently reviewed here.

Consequently `Psi` cannot be a finite nonnegative conic combination of elemental Shannon inequalities and **those specified disjoint-substitution instances** of the three named infinite families: every such combination is nonnegative at `r`, whereas `Psi(r)<0`. This does **not** rule out derivation using overlapping/identified blocks, other information inequalities, other published families, or a different source theorem. It is not evidence of full literature novelty.

The all-parameter checks are exact, not finite parameter samples. For `F_n` and Theorem 2 the verifier checks the integer quadratic minimum, including the zero-leading-coefficient/unbounded-slope cases. For Theorem 1, it sums every negative lattice cell in the finite downward-closed order ideal; when a positive coefficient vanishes it checks the unbounded-axis case. The point has 16 negative-inner Theorem 1 substitutions; both verifier implementations give minimum zero over all allowed staircases and all positive parameters.

## Original source-LP base does not violate these disjoint `Psi` cuts

For the independently verified exact source/star LP original profile `aadf8410...b651`, two differently structured exact scans checked **all 67,609,080** pairwise-disjoint nonempty five-block substitutions with an optional disjoint conditioning block; the minimum `Psi` slack is zero. Therefore adding *all of those particular original-variable `Psi` instances* to the specified exact source/star LP does not reduce its `1847/276` optimum: its pinned primal remains feasible, while the publisher dual remains an upper bound. This is conditional on the written `Psi` validity proof, whose independent scientific review is pending, and does not cover overlapping substitutions or other inequalities.

## Evidence

* Separating vector `frontier-20261028-fivevar-family-separator-witness-v2.json` SHA-256 `84ac1e3c87db445e0c4b3d4eb9388c58f040591cd8ca6b799c93630e3ac187f4`.
* First exact family checker `frontier-20261028-fivevar-family-separator-check-v2.py` SHA-256 `8f70f6e56a526b050465349413a89f30465fda92cc8cf0687b228c4d6efe7d6a`; receipt SHA-256 `9fe3ec5b0f312a840f04d828b14988004e104a573e82f53ed159bbe54fca37d5`.
* Independent-structure family checker `frontier-20261028-fivevar-family-separator-independent.py` SHA-256 `00f78f69da821259316318aa1f6ceae45c1d3c3207ed179c89c371819fb872fd`; receipt SHA-256 `763f993b4ef64ab90d89ede3da7f7f3750c8a8b350f3a1f55def1f8234381507`. It uses nested disjoint subsets, first-difference minimization and diagonal lattice-cell sums instead of the producer's digit enumeration and quadratic formulas; it rejects two targeted point mutations.
* Original-profile exhaustive `Psi` scanner SHA-256 `ad7db6225292c269a66fcdfb36af7a217d505beadc10879048fd876fdf4ee405`, receipt `ee7ba6ae9a27526ac7559780a2c054ef07c49c5695adbb5af898fe71f7181108`; independently structured replay SHA-256 `cbc5996822c7873a04e41d28e22f15ab21259df3b1bde71d7ac944d0d235eb59`, receipt `f5d7da891b0dc6268e33fe71de98dacf24345d37b4426d526cdcd4247ee7800d`.
* The matching source/star primal and publisher dual are bound by `frontier-20261028-crossbranch-all-cuts-combined-check-result.json`, SHA-256 `e5bc0967f9e7ae84722a6fa9346c4a8fb1afa3d109a8041b89dc52a81ce39377`.

A preliminary earlier ray failed two all-order source checks and was replaced by the pinned vector above; it is not used as a separation witness. No cross-model review, proof-assistant formalization or broad SOTA/novelty audit has been performed.
