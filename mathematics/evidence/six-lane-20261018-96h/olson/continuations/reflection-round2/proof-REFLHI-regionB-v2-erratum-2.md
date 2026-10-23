# Erratum 2 to proof-REFLHI-regionB-v2.md (35948d69955ab44faa6464741a2190c97d528218334101b8fc02674422640af3); overlay

Written after host clock 2026-10-19T06:51:44-0700 by OlsonReflectionSuccessor.  Erratum 1 (94a018c5...43e3) stays in force.
It also applies to the addendum B' (4a5b0057...dcc5, with its erratum-1 fa4c249e...6943).  It adopts, for this separate file,
the clipped-gain wording raised by the parent's Codex corollary review of v5 (MINOR; RUN/review/
olson-REFLHI-v5-corollaries-codex-v1.prompt.stdout.txt 7cf9cc10...): Lemma SEG guarantees |U| - 1 >= min(p - 1, 2t, b' - 1),
not the uncapped min(2t, b' - 1).

e2 (Sec. 2, "Segments ... rate 2 ... rate 1", and the "Units" paragraph).  Read every guaranteed segment gain as the clipped
quantity min(p - 1, 2t, b' - 1).  The clipping never binds in Theorem B or Theorem B': units are added one at a time only while
the certified total gain is below Pi_need <= (p - delta)/2 <= (p - 1)/2, so before the last added unit every segment has
2t <= Pi_need - 1, and after it 2t <= Pi_need + 1 <= (p + 1)/2 <= p - 1 (p >= 3).  Hence each rate-2 unit still adds >= 2 and
each rate-1 unit >= 1 to the certified gain until the target is reached, and the bounds sum t <= max(ceil(G_need/2),
G_need - W2/2) are unchanged.  The phrases "W2" and "W1" denote uncapped CAPACITIES; only their use as upper limits on the
number of available units is needed.
No statement or range changes.
