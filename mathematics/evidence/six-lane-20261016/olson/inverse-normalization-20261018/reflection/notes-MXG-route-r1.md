# Route note: RES_<(p) with k <= p and B >= 1 via a G-adaptation of the accepted Theorem M chain (plan, not a proof)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T04:37:35-0700.  Status: [I] plan with on-paper checks; NOT a written
proof.  Recorded so that the route is not lost while Main's current priority (B = 0, k >= p + 1) is worked on.

Source chain (RGR, parent-accepted Theorem M): ../../inverse-parity/mixdef-low/c2/proof-MIX-low-partial-r2.md Secs. 1-5 (Lemma S,
K, Phi, G, AV, Theorem MIX-R), c2/proof-Rstar-r4.md Secs. 0-6 (Fact F, KL, W, B1, A, G1, KS, AC, ZP, C), c2/proof-R4-closure-r1.md
Sec. 1 (Lemma R4).  Setting there: pure aligned / pure anti / (1,1)-pair runs, all nonempty.

G-setting: all blocks odd, runs pure aligned (d >= 1), pure anti (d = -c), or EMPTY (d = 0, genuine: x_t != 0), k <= p,
A >= B >= 1, g := kappa - B >= 1, A <= 2p - 1.  Empty runs act like pairs in every window (d = 0) but cost no B and have
phi_t = -x_t != 0; an empty defect has phi in [1, g - 1], bh = -2 phi <= -2.

Checks done on paper (to be written out in full):
* Lemma S, Lemma K (+ Corollary), Lemma KL: proofs verbatim (interval masses stay in [-B, D + B]; only window algebra used).
* NEW Lemma GIANT: a run with d = 2p - 1 forces all other runs anti or empty, >= 2g empty runs, all of them defects
  (L_t = p - 1); KL on S = all empty runs (c >= 2g + 1, BH < 0) kills.  This replaces Fact F(a) "d <= 2p - 2", whose RGR proof
  used nonempty runs.
* MIX-R with empty defects: L_Z gains + n_EZ (empty defects), but delta >= 2 n_EZ keeps BH(P*) <= B; with Phi even the
  residual is R*_G = {Phi(Z0) <= 2g} and {|Y_al| + |Y_E| + a_Z <= 1} (Y_E = empty non-defects, blockers counted in exc).
* W, B1 (a' = 0 case via GIANT), ZP, C, G1: verbatim or with one-line changes.
* NEW Lemma SPLIT: for a set C of cheap runs with complement nonempty and E = its empty defects, alternate inside the
  maximal blocks of C \ E and add E to both halves: c(U*), c(V*) >= floor((|C| + |E|)/2) (each block's two classes differ by at
  most 1 after subtracting endpoint adjacencies to E; empty defects have phi >= 1), BH(U*) + BH(V*) = BH(C) + BH(E).
  This replaces the cardinality-balanced split in Theorem A, KS and AC, where the counts carry -n_EZ.
* Theorem A, KS, AC with SPLIT: counts #cheap + n_EZ >= 2g + 2 and BH(U*) + BH(V*) <= 2B + 1 (using R*_G).
* Lemma R4: verbatim (empty defects are free with d = 0).
Expected consequence if every step survives the written check and review: no avoider in RES_<(p) with k <= p and B >= 1;
with Theorem B0S (B = 0), RES_<(p) contains no avoider with k <= p.  Planned aid: lift-sampled replay of every elimination.
