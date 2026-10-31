# Addendum 1 to the edge-defect theorem: the twin edge 6--7

**Status: WRITTEN-checked-in-kernel (exact transported identity).** This is an additive companion to `frontier-20261028-edge-defect-theorem-v1.md` (SHA-256 `74f1b87077ae8d918d2eabee4f0f576e176f1aa25ec77a44faf4f5a874958c69`); that packet is unchanged.

R-minus has a second ten-triangle decomposition, the image of the first under the graph automorphism `g=(1,2,7,6,5,4,3,8,10,9)` (one-based images):

`127, 156, 134, 2-7-10, 239, 7-8-10, 569, 689, 4-5-10, 348`.

Its unique uncovered graph edge is `6--7`. The four automorphisms outside the factor-preserving subgroup all map edge `3--4` to edge `6--7`.

Transporting every row of the pinned edge-defect certificate `frontier-20261028-edge-defect-dual-v1.json` (SHA-256 `09750933bddc4e47a25e94d1e11882f0742bdcc8cf0ab0f841836ec9ead3dc39`) by `g` gives the exact identity, for every R-minus FD law,

`3 Delta = H(X6 | X1,X5,X8,X9) + H(X7 | X1,X2,X8,X10) - (108 nonnegative transported CMI terms)`,

and since `N(6)={1,5,7,8,9}` and `N(7)={1,2,6,8,10}`,

`3 Delta <= I(X6;X7 | X1,X5,X8,X9) + I(X6;X7 | X1,X2,X8,X10)`.

Together with the original theorem, a strict-gain law must carry conditional information across **both** non-decomposition edges `3--4` and `6--7`:

`3 Delta <= min{ I(X3;X4|X1,2,8,9)+I(X3;X4|X1,5,8,10), I(X6;X7|X1,5,8,9)+I(X6;X7|X1,2,8,10) }`.

Checker `frontier-20261029-edge-defect-twin-check.py` (SHA-256 `39e2f4944476041da9e3e6820d4edeca14a3ba7892e40aa1ffd42f1cec72caee`) verifies that `g` preserves all 26 edges, that the image is a ten-triangle decomposition with uncovered edge exactly `6--7`, that every transported FD row is the FD row of the second decomposition, every CMI sign, and the identity on all 1,023 coordinates; controls (identity map, non-automorphism, changed target) are rejected. Receipt `frontier-20261029-edge-defect-twin-check-result.json`, SHA-256 `5d1ea6f9a1e30eee1457f6af11d301ddb2e9149df66c6ba7e8f8cd1c0cb2350a`.

At the publisher LP point `h*` both edge terms equal `61/69`, far above `3 Delta = 7/92`, so this structural inequality is not the binding constraint of the copy LP. No numerical bound improvement, novelty or formal verification is claimed.
