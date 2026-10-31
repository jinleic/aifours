# NL242 rank-two eight-zero case: even-half period obstruction (CR7-conditional and unconditional bounds)

**Disposition: same-harness written support at the frozen f239 scope; no rank-two, m=114, m=116 or global NL242 exclusion.** For a balanced f:F2^9->F2 with max|W_f|<=28, exactly eight Walsh zeros, rank-two common polar B (so z=64, q^{-1}(0)=R, Z=W a linear 3-space inside R), normalized odd phase and the period subgroup G={r in W : k(a+r)=k(a) mod 8 for all a in K}:

1. **Unconditional:** G != {0} implies D>=16, m>=108+D/2>=116, D=0 (mod 4), phi=1 on H, E+D<=28, E=244-2m, and the pair identities 5N12=4N0+3N4 and N0(K)+2b=160. Hence m<=114 or D<=12 forces G={0}.
2. **Conditional on CR7** (every sign function on F2^7 has a Walsh coefficient of magnitude >=16; equivalently covering radius of RM(1,7) <=56): D=16 is impossible, so G != {0} implies D>=20 and m>=118; thus m<=116 or D<=16 forces G={0}. CR7 is a classical, source-unverified import, not adopted as proved here; the parent's bounded read of the 2026 RM(1,9) paper (source-screens/nl242-current-paper-balanced-status-parent-v1.json) only confirms that it attributes RM(1,7)=56 to classical papers and leaves balanced 242 OPEN.

Native clock observed before composing: **2026-10-29T14:47:42-0700 PDT**; not a file-creation time.

## Adopted statements

Items 1-2 exactly as reconstructed in the review's §§1-4: full 512-frequency correlation identity C(b)=0 for b != 0; the eight-dimensional (u,v) transform with Parseval 64m / 64(256-m); the common quadratic polar via e2(a)=binom(N(a),2) mod 2; the pointwise odd decomposition k=g(12h-7)-8delta; the z=64 energy argument; the RM(5,8) minimum-weight equality case giving an affine 3-flat; normalization of rho by a translation; the mod-8 flip formula with tau^r=0 and the affine phi forcing phi=1; and the CR7 reduction through the 7-flat restriction with coefficients of magnitude 4 or 12 only.

## Not adopted

- CR7 itself; any claim about the cited 1980/1996 proofs or the 2026 citation.
- The unreviewed predecessor packet (all-ranks parity, 5ddc9432): displayed as input, not a premise.
- Any exclusion of m=114, m=116, nonzero-G cases with D>=20, trivial-G targets, or a balanced witness; the target's formal pair multiset is arithmetic only, not a spectrum.
- Novelty or literature status.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/successor-20261029-rank2-eightzero-phase-kernel-obstruction-v1.md, SHA-256 cf1eaaf9c8c3d26225ee33b4794d211d8f641e7646cc89fa72409cf03fbd660f, 142 LF; frozen manifest 070b3f297fb9a0a07c65a8f528c896058dae9541ade7c7eb2b2eafe21df58822 (four inputs: two adopted four-zero dispositions scope-only, the unreviewed predecessor, the target). Parent relies on the reviewer's receipt for the complete source displays (raw 15-line windows, all endings).
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f239-nl242-rank2-eightzero-even-period-obstruction/review-v1.md, SHA-256 d5939717d29660e14655d1140887ce05c204993f3ea6956518206b6a722e5ec1, 140 LF, **0F/0M/0m with one INCONCLUSIVE (CR7 source verification)**; parent displayed every review line (raw windows 1-15, 16-70, 71-130, 131-175; file ends inside the last window).
- Reviewer-owned controls: 18/18 checks (exit 0, 120 s cap) with six intended-reason negatives; two earlier failed runs (syntax error; missing int.bit_count) disclosed, not counted.
- Parent exact control (retained Python kernel, 2026-10-29T14:47:12-0700 PDT): odd-half Parseval identity 8(m-60)=6n1+5n3+3n5 over all count tuples; pair-equation reduction 5N12=4N0+3N4; E=244-2m; D>=16 from N0(K)+2b=160; the CR7 example sign (-1)^(x1x2+x3x4+x5x6) has seven-dimensional Walsh maximum exactly 16 (illustrates the equivalence, not the universal bound).
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification. No held, withdrawn roster, f161/f162 or author PASS material used.
