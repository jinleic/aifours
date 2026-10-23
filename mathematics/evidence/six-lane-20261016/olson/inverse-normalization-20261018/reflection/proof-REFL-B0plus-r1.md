# Corollary REFL-B0+: Corollary REFL-B0 without the hypothesis 2 kappa <= p - 1

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T12:31:41-0700.  Status: written proof [W], UNREVIEWED.  This is a
two-line composition.  proof-REFL-B0-r3.md (c05eb383...2272) and proof-B0Sedge-r2.md (ac2de0d2...0ba3) are its inputs and stay
unchanged.

**Corollary REFL-B0+.**  Let p >= 5 be prime, and let w0 be an avoider of length 4p - 2 over D_(2p) all of whose rotation letters
are equal to one rho_x, x != 0.  Let R be the number of rotations, and kappa := p - 1 - sum_i floor(l_i/2) over the maximal
constant reflection blocks.  If
   R >= 4 kappa - 4   and   ( R >= p + kappa - 2  or  5R >= 4p + 6 kappa - 10 ),
then every maximal cyclic reflection run of w0 is constant.  No bound o_F <= p is imposed; o_F = 2p - R + 2 kappa.
Proof.  Follow the proof of REFL-B0 (r3) to the terminal word w_T: B = 0, all blocks odd, kappa' <= kappa, R(w_T) = R.
- If k(w_T) <= p, the small-k verdict excludes it.
- If k(w_T) >= p + 1 and 2 kappa' <= p - 1, the argument of REFL-B0 applies verbatim.
- If 2 kappa' > p - 1, then R >= 4 kappa' - 4 and R <= 2p - 1 force kappa' = (p + 1)/2 and R in {2p - 2, 2p - 1}.  That is an
  edge cell, and Lemma EDGE (proof-B0Sedge-r2.md) excludes it.
(For a terminal cell in the edge, the alternatives are not needed: there Delta' <= -1.)  []
