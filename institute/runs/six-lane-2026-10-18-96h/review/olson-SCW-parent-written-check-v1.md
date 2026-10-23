# Olson SCW — parent written check v1 (not a verdict)

Recorded 2026-10-20T02:24:11-0700 (`/bin/date`). Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/proof-SCW-v1.md (6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650). Parent read LF1–386 and checked the following by hand; no computation over mathematical objects. Both-family review and parent verdict still required.

- Frame: N=4kappa−2, R=6kappa−4, H=3kappa−4 and F=10kappa−10; W_kappa=[2,R−2], W_(kappa+1)=[0,R−4]. SC0 is explicitly derived via the minimal zero-sum Y′z; (S′) is used at (p−1,kappa−1), not at terminal k=p+1.
- Label bounds: E≤2kappa−3+n−≤3kappa−4, m1≥5kappa/2. For a-label b≥3, m1−b≥kappa; for negative s-labels use u1≥m1+n+ and s≤n+. Thus u1≥|b|+4 uniformly. Density follows by the consecutive subset-sum interval argument.
- Lemma7: a minimal even-size representation of size≥R−2 misses at most two letters. The u1−2 or u1−4 unit-label counts give a zero-signed subset whenever both signs survive. At q=1, replacing one omitted odd label x≥3 by x positive unit labels lowers the representation size; at q=0 replace the two omitted labels by the stated unit-label set. These reproduce exactly the possible endpoint losses; no full-window premise.
- Lemma8: every exclusion interval has width≥B*−4. The parity-step complete residue system gives B*≤2p, the listed representative subintervals fit I*, and I* has length≤2kappa+2<2p.
- Lemma9: widened-window Delta lower bound≥(2kappa−1)−6≥1 at kappa≥4; upper bound<4p, so Delta=2p. Lemma10: B*≥R>p+4 makes the sum interval shorter than2p and its middle representative is present.
- Theta: 4kappa+4<2p, so congruent candidates within the allowed difference range coincide; empty-run theta is nonzero and even. The gap moves preserve m=kappa+1. The new P1/P2 pair has m=kappa,kappa+1,kappa+1 even at kappa4 (wrap separator kappa−3≥1), so f0=0 without the invalid old pair.
- Sorting: each alternating set has2kappa−1 runs, so kappa−1 remain after choosing the top kappa. Zero/one exception gives B*≤R−2/R−1. Two all-positive exceptional sets force nu0=0; two all-negative sets force Pi0=0, contradicting the lift margin and B*≤2p. Mixed signs force every unselected run empty, yielding B*≤4kappa−2<R. The nu0=0 cases use the nonzero-even theta fact correctly.
- Instances (4,13) and (5,17) match the general inequalities. No extension to general delta is established; LF343–348 states the exact shortfall in the minimal-representation argument.

No gap found in this parent check relative to the stated accepted imports. This is model-authored written mathematics, not human-referee or Lean verification, and not full ordered Olson.
