# Checkpoint 13: RP-2NE accepted, D1-END packaged, new science parked

Recorded after /bin/date observation 2026-10-19T09:08:20-0700.  OlsonReflectionSuccessor.  No scientific computation,
probe, test/build, solver or model call.  Packaging checks only inspect raw source pins/ranges/UTF-8 byte counts.

## Accepted input update

RP-2NE verdict read in full and SHA verified:
RUN/review/olson-RP2NE-parent-verdict-v1.md,
320d817a4b24d2c39f04806ce84ab1977fd68f5869b8c7be0da5184d166d2eab (all five binding readings apply).
Accepted ranges unchanged: delta1,2<=kappa<=(p-5)/2; delta2,3<=kappa<=(p-5)/2.  No upper boundary or delta2,kappa2 accepted.
RPdelta's corrected second-family packet remains independent, parent-controlled after eligibility09:30PT.

## Authorised new upper boundary (CANDIDATE, not accepted)

scope-RPdelta1-boundary-v1.md: 9137410530bb8ef109dbc10987d615661252fa9bb232c60ecd8e9d25ce2df6e1 (frozen before proof).
proof-RPdelta1-boundary-v1.md: 6e7de9593cf5d8bf4ceeb853adf0e11487d63cf38a00cea39a91017c6754e74a.
D1-END: p>=7, length4p-2, rotations in one nonzero pair, R=p+1, all maximal constant blocks odd,
kappa=(p-3)/2 => identity2p-subword, ANY B/no purity.  Retains marked e0>z (e0-z>=p-5>=2), with z<=1.
New calculation: M=p-1 even>=6, k=2M-2, sole layer L=U=M/2, CONNECT2m<k; LIGHT n>=2f allows equality n=2f.  SIGN CaseC
has nonnegative coefficient 1-gamma, but even at gamma=1, 2m0-z>=1 gives the needed strict signed-sum bound.  All four
cases and exact CRT/floor endpoints rechecked; no unaccepted zero-sign lemma used.

## Frozen short endpoint packet (delivered)

review-package-D1END-v1.md: b3e764cc5e70b402225c2f4870753762dfc29af1202fbd01a6c1f816fec4d0b2.
review-excerpts-D1END-v1.json: 64f4d4f58e84fb074b83e5c3fc197ad2a37b5b142b2ec6237e48a85a7e944e62.
12 excerpts/9sources, every pin/range matches. 32231excerpt+8554package+3163JSON=43948 UTF-8 bytes.
Only full proof + exact genericCONNECT/LIGHT/P0/W/Fact2.1 statements and acceptance authorities.  No pending B/SEG-k or
RPdelta proof used in its middle-ledger comparison.  If endpoint accepted, delta1 p>=11 remaining middle points are
{(p-1)/2,(p+1)/2}, plus top{p-3,p-2,p-1}; p7 remains{3,4,5,6}.  Delta2 unchanged: {2} plus middle[(p-3)/2,(p+1)/2]
plus top[p-4,p-1] for p>=11.  These are conditional numerical ledgers, not realizability or avoider existence claims.

Parent requested park after package: PARKED, no new reflection science.  Independent delta2,kappa2 has not been frozen
as a candidate in this slice and remains unclaimed in both accepted RP-2NE and the new endpoint packet.  The older unsent
Zsign addendum stays outside every current review.  Full REFL/INV*/Olson open.
