# Sun8: sparse-quotient fibre bridge for normal extensions, and PSL2(F_p) quotients

**Disposition: same-harness written support at the frozen f242 scope; no unrestricted Sun8 claim.** Definitions: B_T(X)<=r means every r+1 pairwise-disjoint actual LEFT cosets of finite-index subgroups of X contain a pair whose indices have gcd>T; J_T(X)<=s means any s+1 proper finite-index subgroups (labels, repetitions allowed, no disjointness) contain a pair with index gcd>T (s=0: no proper finite-index subgroup).

1. **Bridge.** For every group G and normal subgroup N, B_T(N)<=r and J_T(G/N)<=s imply B_T(G)<=r+s. No splitting, finiteness of G, normality of the U_i or quotient Helly property is used. With T=7, r=5, s=2: B_7(N)<=5 and J_7(G/N)<=2 imply Sun8(G) (every eight disjoint left cosets of finite-index subgroups contain a pair of indices with gcd>=8).
2. **PSL2 quotients.** For every prime p>7, J_7(PSL_2(F_p))<=2: every proper subgroup of index prime to p lies in a point stabilizer (index p+1), so among any three proper labels two indices share p or share p+1. Reconstructed from elementary 2x2 matrices (Borel stabilizers, unipotent generation via W(a)=U(a)L(-1/a)U(a)) plus ordinary Sylow; no subgroup classification.
3. **Applications (conditional).** Any extension (split or not, finite or not) with quotient PSL_2(F_p), p>7, and kernel with B_7(N)<=5 satisfies Sun8; the adopted f151 criterion gives B_7(A8)<=5 (k=0, mu(A8)>=8), so A8-kernel/PSL_2(p)-quotient extensions satisfy Sun8 conditional on f151; (Q,+) has no proper finite-index subgroup, so Q x PSL_2(F_p) is an infinite example.
4. **Non-implication.** J_7<=2 (hence B_7<=2) does not imply 3-Helly for finite-index left cosets: E(inf,inf), E(0,0), E(1,z) with z a nonsquare pairwise intersect with empty triple intersection; their indices are p+1>7, so this is not a low-gcd counterconfiguration.

Native clock observed before composing: **2026-10-29T14:50:16-0700 PDT**; not a file-creation time.

## Not adopted

- Any statement that arbitrary kernels satisfy B_7<=5 or arbitrary quotients have finite J_7 (repeating a subgroup of index<=7 defeats every finite J_7 bound); the unrestricted Sun8 problem remains OPEN.
- f184/f188 (characteristic-7 and other simple-group packets), the conditional assembly, and the Helly-Ramsey bridge (f243, separately dispositioned).
- Author provenance/history assertions (INCONCLUSIVE in the review), novelty, source/book equivalence.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261029-sparse-quotient-fibre-bridge-v1.txt, SHA-256 406c41136f828891b76b61d0a75b406544d363c65035f4411e324e13ee84bc69, 175 LF; dispatched manifest-v2 c6d2665185d1c81bd82d84cb9e845792ea3f5aaa76aabb4bf75726eee1804cb8 (five inputs: f151 disposition scope-only, three mandatory alternating overlays, target; v1 never dispatched). Parent relies on the reviewer receipt for the complete source and overlay displays.
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f242-sun8-sparse-quotient-fibre-bridge/review-v1.md, SHA-256 5859a8e8597f964ed1dec3ba1282b8991c526fb238a4dd86a99582761f30a4e8, 113 LF, **0F/0M/0m** with two provenance INCONCLUSIVE rows; parent displayed every review line (raw windows 1-15, 16-70, 71-113).
- Reviewer-owned exact controls (exit 0, 120 s cap, native clocks): S4/A4 fibre-translation identity with two orientation negatives; PSL_2(F_11), PSL_2(F_13) orders 660/1092, unipotent generation, stabilizer indices 12/14, Helly-failure triple with nonsquare z=2 and square-replacement positive; proper subgroups of index 110/156 as intended negatives to the oversimplified p+1 rule; repetition checks for s=0..10.
- Parent exact control (retained Python kernel, 2026-10-29T14:48:49-0700 PDT): independent enumeration of PSL_2(F_11) and PSL_2(F_13) (orders 660/1092 = p(p^2-1)/2), unipotent generation, point-stabilizer indices 12/14, the three cosets with pairwise intersections 5/5/5 and 6/6/6 and empty triple intersection, nonempty triple when z is replaced by the square 4, and 14+6 random proper subgroups all with index divisible by p or p+1.
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification. The alternating overlays were read before the target by the reviewer; no held prime-2/3 or selected material used.
