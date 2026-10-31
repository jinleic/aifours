# NL242 rank-two eight-zero m=116 fibre (0,4,8): G3≠3 and G3=1 ⇒ H=0; seven residual class-count pairs

**Disposition: same-harness written support at the frozen f244 scope; the (0,4,8) case, m=116, rank two and the balanced target remain OPEN.** For a balanced f:F2^9→F2 with max|W_f|≤28, rank-two common polar, exactly eight Walsh zeros, m=116 and fibre pattern (e1,e2,e3)=(0,4,8) (up to permutation of the three nonzero fibres), writing u as 64 four-entry blocks over K=R⊕F2^2 and classifying blocks by the local Walsh types A_j, B, C_j, D_j, E, F, G_j, H, O:

1. z=64 and q|R=0 are DERIVED (even energy bound at m=116), sum of e_s is 12, and e1=0 forces exactly 16 A1 blocks and reduces the type list to C2, C3, D1, G2, G3, H, O.
2. Complete count equations: g2=2, c3=8−2g−2h, c2=2+2g−2h, d1=20−2g+2h, o=16+g+h (g=G3, h=H), nonnegative exactly for the eleven pairs with g+h≤4, h≤g+1; the U3-zero count is 20+3g and equals the number of positions where the eight-atom transform t3 is divisible by 3.
3. **g3≠3**: with 29 divisible positions the eight atoms have affine rank six with one relation of weight 4, 6 or 8; the sign-weight counts are (23,20), (17,26), (35,8) for even/odd syndrome, never 29.
4. **g3=1 ⇒ H=0**: 23 forces a weight-four relation with even syndrome, the zero-mod-3 set B0 (23 points) has every nontrivial Fourier coefficient of magnitude ≤15 (equality only at (0,1111)), so a hyperplane holds at most 19 points, excluding h≥2; h=1 forces H2=H* and an affine three-flat inside H* disjoint from B0, which the projection case analysis rules out.
5. Exactly seven class-count pairs (g,h) ∈ {(0,0),(0,1),(1,0),(2,0),(2,1),(2,2),(4,0)} survive as an integer relaxation; none is a spectrum, atom placement or Boolean function.

Native clock observed before composing: **2026-10-29T15:03:02-0700 PDT**; not a file-creation time.

## Not adopted

- Existence of any of the seven residual configurations; exclusion of the (0,4,8) case; any m=114/m=116/rank-two or global NL242 statement; the author's source attributions to other caller/phase dispositions (reviewer MINOR: those bodies were not inputs; the needed identities were derived directly from the Boolean assumptions and the expressly adopted T≠0 statement); author execution/history assertions; novelty.
- The withdrawn P1 roster, the period packet (f239) and CR7 are not used; the reviewer found no hidden dependence.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-rank2-eightzero-116-fibre-obstruction-v1.md, SHA-256 29a608826ee2c3dd80a3d47875ae10f720de4291375cc57473d36e8523c3b394, 174 LF; frozen manifest 5a4e50099914d5c175dcb8405fdffc1dcd3d47c8523dcd63558c517813c7c3ad (six-zero disposition scope-only, target). Parent relies on the reviewer receipt for the complete displays (raw windows through line 174).
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f244-nl242-rank2-eightzero-116-fibre-obstruction/review-v1.md, SHA-256 3c761fa2ff877be402f17212db02fea9e0a2f69dc48c563ec7bd71202a8dc4fe, 147 LF, **0F/0M/1m** (attribution) with INCONCLUSIVE status items; one disclosed ordering deviation (general memory read before the manifest; not a scientific input). Parent displayed every review line (raw windows 1-50, 51-110, 111-147).
- Reviewer-owned exact control (corrected run exit 0, 14:44:32-14:44:36 PDT; first run failed on int.bit_count and is disclosed): all 81 ternary blocks, four-atom flats, six eight-atom relation cases, all 63 Fourier coefficients and 126 hyperplanes of B0, all 620 affine three-flats of H*, all 256 rank-two phases, 11 raw vs 7 surviving pairs, and seven intended-reason negatives.
- Parent exact control (retained Python kernel, 2026-10-29T15:02:34-0700 PDT): relation sign-weight counts (23,20),(17,26),(35,8) with 29 absent; |B0|=23 with maximal nontrivial Fourier coefficient 15 at (0,1111) and hyperplane bound 19; the eleven nonnegative count pairs all give 64 blocks of total weight 116 and the stated seven survivors.
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification.
