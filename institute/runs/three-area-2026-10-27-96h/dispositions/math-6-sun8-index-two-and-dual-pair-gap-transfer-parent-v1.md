# Parent disposition - index-two Sun8 transfer, dual pair-gap transfer and conditional solvable closure (f16)

Observed native clock before writing: **2026-10-28T17:26:25-0700 PDT**. Same-harness written support; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-c2-normal-transfer-v1.md` (MathSun8-2) | `3bda86f96f33089da3f0c7ab5d6550e21d018cfc78ece70240a5c4fc54dbb063` | 93 | raw 1-93 through ending |
| Candidate `frontier-20261028-dual-k-fibre-transfer-v1.md` (MathSun8-2) | `1c4631d57fb6c118d1d1859f9cfb33fae521433a65cfea74e4a2f41de14d1b67` | 91 | raw 1-91 through ending |
| Review `frontier-review-f16-sun-c2-and-dual-k-v1.md` (PhysicsPPT44-2) | `44cd1e9b36b6737a26c05044295c2f6e2f60a0320869e1bae9c878a7caac8235` | 137 | raw 1-137 through ending |
| Assignment `review-waves/f16-sun-c2-and-dual-k/assignment-v1.json` | `855a0903dd3eedfac635c88b61111ab76d7340de550dbfdeb7bc320df23efa09` | 27 | frozen before dispatch |
| Sun7 import: prior-round written-composition parent verdict (2026-10-20) | `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2` | 63 | pinned as the statement-level import; composition not re-reviewed |

## Adopted statements (exact scope)

1. **Index-two transfer.** For every group G and normal N of index 2: Sun8(N) and Sun7(G) imply Sun8(G). Main reconstructed by hand: a_i in {1,2}; at least two proper labels (else Sun8(N) on a common fibre); proper pairs have gcd(b_i,b_j) <= 3; Sun7 forces at least three seven-divisible original indices, at most one proper; no-proper-seven case: two odd full seven-labels V, W force 3 and 5 to divide every proper b, so two proper b have gcd >= 15 > 3; one-proper-seven case (A): all full seven-labels odd, a second proper B has 15 | b_B with 3 | V, 5 | W, exactly two proper labels, a third full F is not seven-divisible and must satisfy 3 | n_F and 5 | n_F, contradicting 15 | n_B = 2b_B.
2. **Dual pair-gap transfer.** For every integer k >= 2, every group G and every normal N: if every two disjoint finite-index left cosets of N have index gcd >= k (pair-gap k) and Sun_k(G/N), then Sun_k(G). Proof reconstructed: meeting quotient images would give two disjoint actual N-fibres with gcd >= k; so the quotient cosets are pairwise disjoint and Sun_k(G/N) applies to them; a_i | n_i. Sufficient kernel conditions: every pair of finite subgroup indices has gcd 1 or >= k; in particular every prime dividing any finite subgroup index is >= k (finite p-groups with p >= 11 for k = 8; trivial N vacuously).
3. **Conditional solvable closure.** Assuming the universal Sun7 statement (prior-round written composition, import) and the prior-round p = 5, 7 and p > 7 kernel transfers at their stated scopes (reconstructed by the reviewer in the return, read by Main), together with the adopted index-three and index-two theorems: if N is normal in G, Sun8(N) and G/N is finite solvable, then Sun8(G); every finite solvable group, and by the finite-core reduction every solvable group, satisfies Sun8; a minimum-order finite counterexample to Sun8 (if any) is perfect.

## Parent verification

Main hand-verified items 1 and 2 completely and the derived-series/prime-order refinement, the finite-core reduction (cores of the eight subgroups have finite index; images of the same cosets in G/K stay disjoint with the same indices) and the perfectness argument in item 3. The reviewer's independent squarefree-support check (zero models) and D22/A5 actual-coset enumerations are supplementary. Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m.

## Not established

Unrestricted Sun8; Sun7 (import); any nonsolvable/perfect quotient case beyond the separately reviewed kernel-prime transfers; novelty (NR). The A5 and GL(3,2) finite enumerations are instances, not theorems. Historical quarantines for this slot remain historical records.
