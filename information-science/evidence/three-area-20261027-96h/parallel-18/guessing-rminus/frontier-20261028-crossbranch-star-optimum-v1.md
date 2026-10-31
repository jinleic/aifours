# Exact optimum with both first-copy cross branches

**Status: WRITTEN with independently checked exact rational primal and matching published dual.** This is a separately scoped strengthening of `frontier-20261028-crossbranch12-optimum-v1.md` (SHA-256 `2155646388beb18738c608f3f7aedc9e86606fcd17fba27a433e28e4725d1693`). It does not change that frozen packet or the publisher-LP packet under review. It is not an entropic realization or a new guessing-number bound.

## LP being strengthened

Use `X=(a,b,c,d,e,f,g,h,i,j)`, `U=b'0`, `V=(d'1,e'1,g'2)` and `W=(f'3,g'3,h'4)`, with all original caps, FDs, graph symmetries and five source copy protocols as in the two predecessor packets. The LP contains:

* all elemental Shannon inequalities on **both** 14-variable sets `(X,U,V)` and `(X,U,W)`;
* the source-copy equalities for the copies occurring in each set;
* `I(U;V'|X)=0` for all seven nonempty subtuples `V'` of `V`, and `I(U;W'|X)=0` for all seven nonempty subtuples `W'` of `W`;
* one **shared entire 11-variable entropy profile** for `(X,U)` between the two sets.

For an actual entropy law these pairwise conditional-independence requirements can be achieved by sampling the source copy branches independently given the full original vector `X`, preserving each branch marginal. The LP omits Shannon inequalities whose variable sets mix `V` and `W`, and does not impose their mutual independence; it is not the all-17-variable Shannon/copy LP. Its coordinate count is `2(2^14-1)-(2^11-1)=30,719` nonempty entropies.

## Exact primal, dual, and all-order family

The common original profile has all singleton values 1 and `h(X)=1847/276`. The first 14-variable exact primal is `frontier-20261028-crossbranch12-exact-candidate.json`, SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739`. Its entire 2,047-coordinate nonempty `(X,U)` profile is fixed in the second 14-variable exact primal `frontier-20261028-crossbranch13-fixed-u-exact-candidate.json`, SHA-256 `9744448c5473f3781ef616d46c5615dff649c0f4581dcf7f9bbd4b5c25ee9ce1`.

Separate exact independent checkers validate every `372,750` elemental Shannon row in each 14-variable system; all `899` and `1,539` source copy equalities respectively (including 257 duplicated branch-1 equalities); the seven cross-independence equations in each; original caps, FDs and all eight graph symmetries; and all `1,052` and `1,491` source rows applicable to the respective systems. The combined checker binds the **same** 2,047 shared coordinates, checks every one of the `1,920` source rows exactly tight, and revalidates the published signed dual at `1847/276`. Hence the primal and dual match and the star LP optimum is exactly `1847/276`.

The same original profile also passes the previously pinned exact all-positive-order family `F_n` for all `13,729,980` pairwise-disjoint original-variable block substitutions modulo `A/B` exchange. Therefore adding that entire stated family to this star LP still leaves optimum `1847/276`. No conclusion is made for overlapping substitutions or other non-Shannon/copy families.

As in the predecessors, only the old 4,397-coordinate file's **original-variable** projection is fixed. The new cross12 candidate differs on 247 of 1,372 overlapping old auxiliary values, and the new cross13 values differ on 460 of 2,002. No claim is made that the old auxiliary assignment extends; earlier nonextension findings retain their specified scope.

## Evidence

* Cross12 producer SHA-256 `544f598dae4ddd529f2635c74be4caa2827a1feaaea617f4712a8b6e8633a7d8`; independent checker `frontier-20261028-crossbranch12-independent-check.py` SHA-256 `1249cc1692dcc8d76b62094d3c5ef66f274dda899632f9090195d543a962b2a5`, receipt SHA-256 `371ed6d0da680cdbacf36704f61f7d1888b800a5489470c9c36512811df9a86e`.
* Cross13 producer `frontier-20261028-crossbranch13-fixed-u-exact.py` SHA-256 `b6ccbe358dccb745a3105bb0354c5e194361cb6e6fbb5cc7a5906f16f90e4967`; independent checker `frontier-20261028-crossbranch13-independent-check.py` SHA-256 `e692f6ed3a366f194b6c629c0490d4a8f93be096adc7333087aac060ffdaffd8`, receipt SHA-256 `e182255f7fab8835a8703e1e6efa33a662cc6f7906f661bb4dc2aa771f0b2112`. The checker binds the shared first-copy profile to the exact cross12 candidate and rejects six intended mutations.
* Combined checker `frontier-20261028-crossbranch-star-combined-check.py` SHA-256 `48edd0c9d80da68e58427f12fe4af65dad2520a15a00ad28b7af8272095034e2`; receipt SHA-256 `96a28c2502d5ea7571a1dd52ad19e9e6c1fb82ba33d3399f48f1302b7648f5e9`. It rechecks exact source row values, both cross-independence families, all shared/profile hashes, the published dual and the `F_n` base receipt. Its in-memory controls reject changes to the original joint entropy and to one cross-only coordinate in each 14-variable system.

The numerical IPM outputs were only proposals; exact affine reconstruction and separate integer/Fraction checks establish the stated primal. No cross-model review, proof-assistant formalization or novelty clearance was performed. Constraints mixing the branch-2 and branch-3 auxiliaries, other copies, and a genuine positive-gap FD law remain open.
