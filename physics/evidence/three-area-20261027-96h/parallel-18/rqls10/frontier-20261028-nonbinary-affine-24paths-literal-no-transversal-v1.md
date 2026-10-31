# All 24 literal nonbinary q18 affine paths have no transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at final endpoint replay: **Wed Oct 28 20:29:51 PDT 2026**. This removes the q6 classification import from `frontier-20261028-nonbinary-affine-24paths-no-transversal-v1.md` SHA **0307896e56a4c264b2901e8872902796603cf314673bc97fa5c71aa5a1cfc9f2**. It is an unconditional finite/written argument ONLY for the 24 specified literal paths, not a general BH(10,18) or QLS10 theorem.

## 1. Claim and previously checked non-endpoint region

For every case in `frontier-20261028-q18-nonbinary-twentyfour-v1.json`, SHA **776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2**, let H and four rectangle masks/coefficients be as recorded and define `K(z)=H ⊙ z^(sum_j coefficient_j M_j)`, |z|=1. Every K(z) is Hadamard by exact Laurent-coefficient checks. **Claim:** the associated actual Fourier-product QLS has NO transversal for any z, any K-row order, and arbitrary row/column phases and column permutations, even if rays repeat.

The independent squarefree reciprocal-gcd and endpoint replay `frontier-20261028-nonbinary-affine-24paths-replay-v1.py` SHA **0994d524b39be1f15764082a79cd4546c300e93bcaf50910a7e88f7b8098c53e**, result SHA **99554b306a89d16ae89b4870fbff6133e8d3243c6dd0eed9167a7906fd6c3bc3**, checks all `24*252*45=272160` half-polynomials, no identity-edge matching, and all `24*66*252=399168` half graphs at mu72 outside mu6. Every possible unit zero of a nonidentity half-polynomial is in mu72. Thus only SIX sixth-root phases per path remain. For cases0–3 and12–23, the prior all72 replay `frontier-20261028-nonbinary-affine-16paths-replay-v1.py` SHA **eaf4daab381c2eb832b1bab98cdad03baaf113c4bd480d7a98427d6c6976f996** checks all six too, with no half-graph matching.

## 2. Directly resolving the remaining 48 endpoints

For each of cases4–11 and each `s=0,...,5`, the actual endpoint `K(zeta6^s)` is reconstructed directly from the literal source. The new exact `frontier-20261028-nonbinary-eight-endpoints-v1.py` SHA **5d127a8527c57244792471ef6b8502df1ceb1a210277abf70f3dacc8e1b7d63f** checks all48 Hadamards and each endpoint's252 half graphs. Each endpoint has exactly ONE matching E/complement pair. For the normalized E containing source row0 at physical coordinate0, it records a row with no orthogonal different-column candidate to cell `(0,0)` in each of `4!*5!=2880` coordinate orders.

The 48×2880=**138240** obstruction digits are in `frontier-20261028-nonbinary-eight-endpoints-v1.json`, SHA **4de192d65346522eb77f80424f3a808645e11dd26c63e221e14044ae73ed3cd2**. Independent `frontier-20261028-nonbinary-eight-endpoints-replay-v1.py` SHA **4e0a6ba3ec919a87907a567d0105657e5d0931d6926323448d33da1cf60927a2** reconstructs EVERY endpoint and `48*252=12096` half graph, independently identifies all48 normalized matching halves, and verifies EVERY one of the138240 row digits and its nine candidate inner products in the Q(zeta3,zeta5) product basis. Its result SHA **239bee3366bdc248bccb5f8001a04ebdccd0be6cb55d9598dc51d02d67dc1052** records PASS.

The symmetry caller is the same as in the q6 packet: cyclic coordinate shifts can choose E/complement and put source row0 at physical coordinate0; a physical row shift is a common diagonal unitary and puts the column0 cell of any putative transversal at `(0,0)`. Thus the direct endpoint certificates exclude every possible T, not merely one assignment.

## 3. Limits and correction provenance

The earlier twelve-path packet conservatively left cases8–11 and20–23 unresolved because the FULL reciprocal gcd did not divide `z^72-1`. The squarefree successor showed these failures were repeated mu72 roots; the 16 already direct-halfgraph paths and the eight directly certified endpoints now cover all24 without that classification import. Earlier immutable records are unchanged.

This result does not imply no T on the other directions of the four-parameter families, for all BH(10,18), or for arbitrary 1-RQLS10. The finite programs, source bytes, reciprocal-root and normalization callers require independent review; no target witness, formal proof or novelty clearance is claimed.
