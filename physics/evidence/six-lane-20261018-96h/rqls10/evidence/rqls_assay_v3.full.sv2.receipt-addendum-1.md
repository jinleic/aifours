# Addendum 1 to evidence/rqls_assay_v3.full.sv2.receipt.md: structure of the calibration maximal solutions

Recorded 2026-10-19T00:42:34-0700. Post-hoc statistics read from the frozen JSONL (sha256 b69d610920c2b9e896b7ff8a979009c8dc80b1de2d46d323c98247131c67c55c);
no new search; numbers from |<q_p, q_p'>|^2 over all cell pairs of the saved (polished, maxdev <= 1.5e-15) vectors.

- v = 7, Cay(Z_7), seed 33 (49 rays): only three overlap values occur: 0 (441 pairs = the adjacent pairs),
  1/7 (441 pairs) and 2/7 (294 pairs). This is the value set of normalised character sums |Phi|^2/49 of a
  Fourier-permutation construction, consistent with a Huang-Li-type solution up to gauge (not proved here).
- v = 8, XOR, seeds 41 and 44 (64 rays each): 1312 orthogonal pairs (672 adjacent + 640 non-adjacent) and 44 further
  distinct overlap values, each attained by exactly 16 pairs; the two solutions have different overlap spectra, so
  they are not related by a unitary and relabelling-free gauge: the maximal solution set for B = XOR is at least
  one-dimensional modulo gauge (numerical observation). The 16-fold multiplicities suggest that RRR converged to
  configurations with a symmetry of order 16 (not analysed).
- Consequence for planning only: at v = 8 maximal 1-RQLS occur in continuous families that RRR reaches from random
  starts; nothing is implied for v = 10.
