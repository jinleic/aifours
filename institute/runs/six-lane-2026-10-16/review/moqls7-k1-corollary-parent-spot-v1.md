# Parent spot check: K1 ⇒ no MCPQLS(7), no maximal-cardinality 2-RQLS(7)

Recorded 2026-10-17T22:42:49-07:00 (host clock). Parent in-memory computation against the pinned lane file
`physics/evidence/six-lane-20261016/moqls7-maximum/evidence/nets7_classes.json` (sha256 `78d1728f9096afff9d23650f88808f9d7888b4cc380141f68b31578a26ec0d67`, the hash printed in K1-THEOREM.r1 §3 and verified by M7K1Verify route 1).

## Bridge checked

- The pandiagonal 4-net of order 7 (rows, columns, slope +1 diagonals, slope −1 diagonals) was built on points 7x+y with classes `x = c`, `y = c`, `y − x = c`, `y + x = c`.
- The shear (x, y) ↦ (x, y + x) is an affine collineation of AG(2,7). Applied to the pandiagonal net's 28 lines it gives exactly the 28 lines of the slope set {∞, 0, 1, 2}: **set equality holds**.
- That slope-{∞,0,1,2} net equals, line for line, the lane's **class 5** net (origin "desarguesian-harmonic"), and differs from class 6. The slope-{∞,0,1,3} net equals class 6 (equianharmonic). So the lane's class labels match the source nets.

## Consequence (conditional on acceptance of Theorem K1)

- A pandiagonal QLS(7) (Huang–Li arXiv:2606.27758v1: main diagonal, anti-diagonal and all broken diagonals in both directions are transversals) is an ONB-assignment on the pandiagonal 4-net, hence on class 5 after the shear. K1's class-5 clause says every such assignment is classical (uses 7 rays), i.e. cardinality 7. Hence **no MCPQLS(7)** (cardinality 49) exists.
- By Zhang–Cao arXiv:2608.29201v2 Lemma 2.2, a 2-RQLS(7) is a QLS(7) orthogonal to two classical QLS(7); a non-classical one would be a K1 triple. Hence **every 2-RQLS(7) is classical and no maximal-cardinality 2-RQLS(7)** exists.
- Both instances are listed as undetermined in those 2026 preprints (Huang–Li §5; Zhang–Cao §5). The parent read both passages in the arXiv PDFs on 2026-10-17 PDT.

## Limits

- This is a bridge check, not an acceptance of K1. K1's acceptance rests on the five parent routes (all PASS), the two hostile reviews (both ACCEPT-WITH-FIXES) and the pending delta check of r3.
- "Cardinality 7 ⇔ classical" for a single square: every row is an ONB of 7 rays; if the square uses only 7 rays overall they form that ONB, and a global unitary sends them to the standard basis. Not re-proved beyond this remark.
- No priority claim: the scout screen was bounded (NONE-FOUND-IN-SCOPE, [transcription](moqls7-k1-priority-scout-v1.md)).
