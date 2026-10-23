# D1-END — mandatory wording/self-containment erratum

Recorded 2026-10-21T07:46:23-0700 (`/bin/date`). Governs unchanged [proof-RPdelta1-boundary-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-RPdelta1-boundary-v1.md) — SHA256`6e7de9593cf5d8bf4ceeb853adf0e11487d63cf38a00cea39a91017c6754e74a`. Claude ACCEPT-WITH-FIXES 0F/0M/4m; all four are self-containment/wording, no statement/constant/range change.

1. **Sec.2 self-containment:** the fixed-window calculation, zero-increment criterion, CRT zero criterion and even-integer-test converse are re-derived here; no step of proof-RPdelta-two-neutral-v1.md is used (only V2NE binding1's e-definition and binding4's retained e0>z). Open Sec.2 with "Assume w avoids" (P0's avoider hypothesis). Rename the shifted integer s (collision with signs s_i).
2. **Case B justification:** same-parity nonadjacency follows from the parity argument of V2NE binding5 (stretch indices differ by a nonzero even residue mod 2m0; neighbours by±1), and no boundary is created — not from "m0>=m+1>=4".
3. **Case C citation:** replace the VL-binding5 citation with its generic one-line proof (a J-neighbour of i shares i's initial sign, hence lies in i's stretch; m0>=1 makes every stretch a proper interval); old boundaries are untouched; optionally record gamma=1 forces m0=m-1,f=1,n=2.
4. **Sec.4 ledger:** state the universe [2,p-1] explicitly (kappa<=p-1 from H>=0; kappa>=2 by the I.14 residual convention) so (3) is a literal set difference; note delta2's K2P+ band is empty at p=11.

Scope confirmed: accepted exactly at p>=7 prime, R=p+1 rotations in one nonzero pair, all-odd blocks, kappa=(p-3)/2, ANY B. NOT covered: p5/kappa1, other delta1 kappa, delta2 incl(2,2), R>=p+2, even blocks; REFL(p)/REFL-HI/RES-HI/INV*/ordered Olson remain open. Imports only W/Fact2.1 (V5 setting S), P0 (K0star-r2 L73-75, 879aeee7), CONNECT/LIGHT (VL), e-definition (V2NE binding1).
