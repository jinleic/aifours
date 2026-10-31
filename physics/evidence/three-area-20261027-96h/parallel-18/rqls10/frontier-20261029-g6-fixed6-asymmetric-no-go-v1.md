# Six exact spoke rays suffice to forbid any 6D complement of this graph

**WRITTEN + EXACT-ALGEBRAIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 01:59:41 PDT 2026. This further strengthens `frontier-20261029-g6-fixed12-asymmetric-no-go-v1.md`, SHA-256 `ba2c1bedd66be0dd13bc100f5166b0f1ee4c6ca50c9b3ee4d03dd791fde42336`. It is a two-configuration obstruction, not a general G6 or 1RQLS10 no-go.

## Exact scope

Use the same G6 graph, generators R,S and the two 12-spoke configurations generated from xA or xB in the fixed12 packet. Fix **only** the six rays on the edges

`(2,14), (4,10), (5,13), (5,14), (8,10), (9,10)`.

For either xA or xB, these six rays are distinct and locally orthogonal where their edges meet. **No assignment of rays to the remaining 39 edges gives an ONB at each G6 vertex.** This exclusion does not assume symmetry or distinctness of the remaining rays and holds under a common unitary transformation of all six fixed rays. An open neighborhood of each labeled six-ray tuple is also excluded by the compactness argument at the end of the fixed12 packet; no radius is computed.

## Linear forcing

In C6, if five known incident-neighbor rays are linearly independent, the target ray is uniquely forced to their common 1D orthogonal complement. The exact replay certifies every following step for both xA and xB; each parenthesized list consists only of previously fixed or forced edge rays.

| Forced edge | Five orthogonal-neighbor witnesses |
|---|---|
| `(5,10)` | `(4,10), (5,13), (5,14), (8,10), (9,10)` |
| `(2,10)` | `(2,14), (4,10), (5,10), (8,10), (9,10)` |
| `(3,10)` | `(2,10), (4,10), (5,10), (8,10), (9,10)` |
| `(2,5)` | `(2,10), (2,14), (5,10), (5,13), (5,14)` |
| `(3,5)` | `(2,5), (3,10), (5,10), (5,13), (5,14)` |
| `(4,5)` | `(2,5), (3,5), (4,10), (5,10), (5,13)` |

All six forced rays match the ones in the fixed12/fixed21 configurations. At this point exactly three of their 12 spokes, `(2,8)`, `(2,9)` and `(2,13)`, remain unforced.

## Three more rays forced by a rank-one positive pencil

For each of those three edges, the four already known incident-neighbor rays leave a 2D orthogonal complement. Let `B1,B2,B3` be the exact bases produced by the replay, in the displayed edge order. Writing the first missing ray as `B1 z`, the requirement that the other two be orthogonal to it forces their projective representatives to be `B2 A12 conjugate(z)` and `B3 A13 conjugate(z)`, with the nonsingular 2×2 maps `A1j=J (B1† Bj)^T` and `J=[[0,-1],[1,0]]`.

The last two rays must also be orthogonal. For the stated bases, write their inner product as `z† H z` and set `H1=(H+H†)/2`, `H2=(H-H†)/(2i)`. Orthogonality implies both `z†H1z=0` and `z†H2z=0`. Exact computation gives

- for xA: `det(H1+lambda H2) = -16 - 32 sqrt(2) lambda - 32 lambda²`, and take `lambda=-sqrt(2)/2`;
- for xB: `det(H1+lambda H2) = -16 + 32 sqrt(2) lambda - 32 lambda²`, and take `lambda=+sqrt(2)/2`.

At the respective lambda the Hermitian pencil has determinant 0 and diagonal entries `18-6sqrt(6)` and `18+6sqrt(6)` in some order. Both are positive, so it is positive semidefinite of rank 1. Since its expectation on z is zero, z must lie in its **unique** 1D kernel. The replay checks that this forces exactly the three original missing spoke rays. Any purported completion therefore contains the entire 12-spoke configuration, which the fixed12 and fixed21 packets exclude without assuming symmetry.

## Exact evidence and limitations

`frontier-20261029-g6-fixed6-forces12-v1.py` SHA-256 `e522251d23ef4bccb48e54626124c145c072bb8a35b90a19bd2a8ff93a8e88cb` checks the original graph, both exact radical seeds, six incidence-consistent forcing steps and nullities, both nonsingular 2D transfer maps, each Hermitian pencil and its rank-one kernel, and all forced-ray matches. Output `frontier-20261029-g6-fixed6-forces12-v1.json` SHA-256 `1b152a0182ffe172966812d8e6fb623c1651eee56a7f2742c5742ac68c5ecc93` records **PASS** at 01:59:41 PDT. All exact radical arithmetic and pivot inverses are defined and checked in the replay; numerical searches only suggested the six-ray subset.

The chain depends on the fixed G6 graph and the two displayed ray tuples up to common unitary, not arbitrary six-ray partial assignments. Other complements, other 4D cores, and the full 1RQLS10 problem remain open. The linear forcing, positive-pencil argument and both imported downstream certificates need independent written and exact review; no formal-kernel or novelty claim is made.
