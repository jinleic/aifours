# Sun8: Helly–Ramsey normal-extension bridge (conditional on quotient Helly)

**Disposition: same-harness written support at the frozen f243 scope; conditional, not an unrestricted Sun8 result.** With B_T as in the sparse-quotient disposition (every r+1 pairwise-disjoint actual LEFT cosets of finite-index subgroups contain an index pair with gcd>T):

1. **General bridge.** For any group G, normal N and quotient Q=G/N whose finite-index left-coset families have the finite-clique Helly property, B_T(N)<=r and B_T(Q)<=s imply B_T(G)<=R(r+1,s+1)-1 (finite Ramsey on the label overlap graph; cliques give common-fibre kernel cosets via (g_iU_i∩Nt)t^{-1}=(x_it^{-1})(tK_it^{-1}), independent sets give disjoint quotient cosets).
2. **Theorem A.** If B_7(N)<=2, B_7(Q)<=2 and Q's finite-index left-coset triples are 3-Helly, then B_7(G)<=5 (R(3,3)=6), hence Sun8(G). Without Helly, any six-label bad family under the two factor bounds must contain a projected intersecting triple with empty total intersection (a necessary obstruction, not an existence statement).
3. **Cyclic quotients are Helly** for finite families (pairwise-compatible congruences have a common solution; finite case by choosing an integer solution and reducing mod M). Reviewer MINOR: the source's sentence about a residue mod L being "well-defined modulo M" is wrong as a unique lift (M=6, L=2 gives three residues); the corrected choice-of-lift argument preserves the claim.
4. **Example.** For all primes p,q>7, N=D_{2p}, Q=C_{2q}: each factor has exact bad-family maximum 2, so 4<=B_7(D_{2p}×C_{2q})<=5; mu(G)=2, outside every adopted f151 mu>=8 criterion.
5. **Failed shortcuts** (adopted as stated): C_7×C_7 shows factor-Sun8 neither forces disjoint projections nor bounds fibre multiplicity; F_5^2 affine lines show arbitrary quotients need not be 3-Helly (indices 25, not a low-gcd pattern); the eight-cycle shows graph-only constraints from B_7<=7 factors are insufficient.

Native clock observed before composing: **2026-10-29T14:52:42-0700 PDT**; not a file-creation time.

## Not adopted

- Any unrestricted Sun8 statement; sharpness of the bound 5; existence of a six-label obstruction; f184/f188; the conditional assembly; the sparse-quotient bridge (separately dispositioned at f242).
- Author provenance/history assertions (INCONCLUSIVE); novelty; source/book equivalence.

## Evidence and limits

- Source: /Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261029-helly-ramsey-normal-bridge-v1.txt, SHA-256 ba5dae355377f7e63a5426a76177d9bf2a50e9220f5be8a95aea6e28f35cb3e1, 190 LF; dispatched manifest-v2 3ffcfe6f57f8a43fed08931d3cbaaca6a4fae153d18cc8b487cd84f5368c4f8c (f151 disposition scope-only, three mandatory alternating overlays, target; v1 never dispatched). Parent relies on the reviewer receipt for the complete source and overlay displays (raw windows listed in the review).
- Review: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f243-sun8-helly-ramsey-normal-bridge/review-v1.md, SHA-256 bb636e4026157bf2cf23c5db715667aa579bd67aa419a3598314e71cceabc3e4, 108 LF, **0F/0M/1m** plus one provenance INCONCLUSIVE row; parent displayed every review line (raw windows 1-54, 55-108).
- Reviewer-owned exact controls (exit 0, <=120 s, native clocks 14:44:21-14:44:22 PDT): D_6×C_2 fibre identity over 1,872 fibres with a MISSING_CONJUGATION negative; all 5/6-vertex colourings (12 triangle-free on K5, none on K6); 45,777 cyclic congruence families with PAIR_CONFLICT and NO_UNIQUE_LIFT negatives; D_22, C_22 and D_22×C_22 enumerations; C_7×C_7 and C_5×F_5^2 constructions with targeted mutations.
- Parent exact control (retained Python kernel, 2026-10-29T14:52:15-0700 PDT): every 2-colouring of K6 has a monochromatic triangle and exactly 12 colourings of K5 do not; the three F_5^2 lines meet pairwise in one point with empty triple intersection; the seven C_7×C_7 cosets are disjoint and each projects onto the quotient.
- Assurance boundary: same-harness; not human, independent-model-family, formal/kernel or novelty verification. No held prime-2/3, selected or f161/f162 material used.
