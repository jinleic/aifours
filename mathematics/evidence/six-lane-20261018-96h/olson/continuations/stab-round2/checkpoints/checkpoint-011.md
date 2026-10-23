# Checkpoint 011 (Slice A, OlsonSTABSuccessor) -- BASE2 slice result

Written after /bin/date 2026-10-19T07:54:34-0700.  Written work only; no computation, model call or launch.  Shell use: /bin/date, shasum,
one read-only diff between my own v1/v2; v2 created with exclusive creation.
- NEW candidate [W, unreviewed]: proof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 (v1 16fda0d6c38df327fbfd2a180b2b378fed7ded9c5bfae60b8cec13a13296c302 never sent;
  v2 changes only one attribution sentence in Sec. 3, verified by diff).
  - Lemma L1: at a BASE2 cell the shortest long zero-sum has length exactly 2p + 2 (accepted SLZ3), so a threshold counterexample has
    W* <= U with sigma(W*) = -1 and |W*| >= delta0 + 2.
  - Lemma B2-1: at EVERY BASE2 cell (p = 6m - 1 prime, kappa = 4m), delta0 = 1 is impossible (complement symmetry of the subset-sum set
    forces A <= {0} u [sigma, p - 1]; then the subset sums of Z* = -W* are trapped in J = [6m - B, B]; t = 3 and two extremal triples,
    each with no admissible extension).
  - Theorem B2-17: LS(17, 12).  Theorem B2-23: LS(23, 16).  Both new LS cells relative to the accepted coverage (S1, S2 of the scope).
- S3 (all BASE2 cells) NOT proved; exact residual: 2 <= delta0 <= 2m - 3 with 2 <= delta' <= m - 3 or delta0 >= 6.
- Next: parked pending parent instruction/review; candidate next lever is to replace the delta0 <= 5 single-term exclusions by a
  Z0 first-crossing argument valid for larger delta0.
