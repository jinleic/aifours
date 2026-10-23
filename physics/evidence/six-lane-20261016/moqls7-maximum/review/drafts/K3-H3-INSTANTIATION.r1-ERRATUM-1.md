# Erratum 1 to K3-H3-INSTANTIATION.r1 (phys-2, lane moqls7-maximum)

Written 2026-10-18 from 08:04:12 PDT (host clock) at the parent's request. It corrects one sentence of
`review/K3-H3-INSTANTIATION.r1.md` (c3d8c05db226781de915d7a98ee84eae16cb7392e7aef2fc4a37b897dfd65cdc), which stays
frozen and unchanged. Source of the finding: Codex review `R/m7-h3-instantiation-codex-v1.note.md`
(2cdda1de5736dbf743b3f148de7b8d3a540f73440aaf8679eac8783a757d7190), ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 1 MINOR.
`R/` = `institute/runs/six-lane-2026-10-16/review/`.

No encoder, CNF, run or status changes. No claim.

## E1. H3 r1 §4, lines 119–122 (encoder B degenerate branches)

r1 says: "s2 = None (one item) would make lines 151 and 155 malformed".

That is wrong for line 155. With a single item, `counter2` returns s2 = None. The non-collinear branch then reaches
lines 154–155, which deliberately emit `B.clause(-s1, gpq)`, a valid clause (exactly one common neighbour forces
g(p,q)). Only the collinear branch at line 151, `B.clause(-s1, s2)`, would contain None.

**Corrected reading:** "With one item, the collinear branch at line 151 would emit None; the non-collinear branch at
lines 154–155 correctly handles this case. Neither occurs in production, where G2 lists have five or six items."

The rest of r1 §4 stands, including the unreachability of every degenerate branch by F3.
