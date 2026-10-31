# PH7 at 8/9: a directed two- or three-cycle is necessary

**Disposition: same-harness computer-assisted written support at the stated spectral scope.** No real irreducible 7×7 Metzler matrix `G` of spectral bound zero, whose characteristic polynomial is divisible by `D(y)=y[(y+1)²+8/9]²`, has a directed off-diagonal graph with no 2-cycle and no 3-cycle. Conditional on the separately supported [irreducibility and normalization result](math-1-ph7-global-irreducibility-eight-edges-parent-v1.md), every actual representation of the registered phase-type transform using at most seven states at `z=8/9` must therefore contain a directed 2- or 3-cycle. The present spectral argument alone covers exactly seven states; it does not itself exclude representations with fewer states.

Native clock observed before composing: **2026-10-28T20:47:51-0700 PDT**; not an asserted file-creation time. This is not a PH7 existence or nonexistence theorem, an exact minimum-order result, a formal/kernel proof, human or independent-model-family review, or a novelty claim.

## Mathematical reduction

Let the seven diagonal escape rates be positive `u_i` and their elementary symmetric functions be `e_i`. Irreducibility and Perron theory give strictly negative diagonal entries. In the determinant permutation expansion, absence of 2- and 3-cycles leaves, among permutations moving at most four vertices, only single directed 4-cycles. Consequently

`[y⁶]χ=e₁`, `[y⁵]χ=e₂`, `[y⁴]χ=e₃`, `[y³]χ=e₄−C₄`,

where `C₄≥0` is the sum of the weight products of all directed 4-cycles. Distinct overlapping cycles contribute separately; the excluded support-four alternative is two disjoint 2-cycles. With `χ=D(y)(y²+py+q)`, the simple Perron eigenvalue zero and strictly negative real parts of all other eigenvalues imply `q>0`. Matching coefficients gives

`E₄=e₃−4e₂+(74/9)e₁−28/3=0`,

`E₃=e₄−(70/9)e₂+(212/9)e₁−1007/27=C₄≥0`.

Choose any six positive rates with elementary functions `f₁,…,f₄`, and let the seventh rate be `x`. Set

`A=f₂−4f₁+74/9`, `B=f₃−4f₂+(74/9)f₁−28/3`,

`h₀=f₄−(70/9)f₂+(212/9)f₁−1007/27`, `h₁=f₃−(70/9)f₁+212/9`.

Then `E₄=Ax+B` and `E₃=h₁x+h₀`. Define `Qpol=81[A²−(f₁−4)B]` and `Hpol=−243[h₀A−h₁B]`. The exact six-variable Bernstein certificate below establishes both strictly positive for all six positive rates. If `A=0`, `E₄=0` forces `B=0`, contradicting `Qpol>0`. Otherwise `x=−B/A`, so `q=Qpol/(81A)` and `E₃=−Hpol/(243A)`. The positivity of `q` and `Qpol` forces `A>0`, and then `Hpol>0` forces `E₃<0`, contradicting `C₄≥0`.

## Certificate and actual verification

- Parent read the complete [candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md), 101 LF, SHA-256 `76ff376815423d69546c10e2608f7c373a80f3e7752d306c911751e8eb50f33b`, and the complete [f129 review](../review-waves/f129-ph7-girth-four-two-or-three-cycle/review-v1.md), `435401d8060097175719db4844d5d4fc590d56cd750645acbf92a5a21a907439`. The review found 0 FATAL / 0 MAJOR / 4 presentational MINORs; this disposition supplies the open-cube vertex reasoning and correct support-four alternative, and states the separate fewer-than-seven-state dependency explicitly.
- The [certificate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-ph7-girth4-critical-bernstein-certificate.json), `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8`, contains 5,332 Q and 5,334 H dyadic leaf paths. The reviewer independently derived both polynomial coefficient arrays and ran its own exact-integer engine; its [receipt](../review-waves/f129-ph7-girth-four-two-or-three-cycle/reviewer-f129-engine-result-v1.json), `1c67f113d0af7760477a4c524fa7327305511d3aae90c6f5e11d7eaa217c4c89`, records all leaves, partition coverage, nonnegative coefficients, strictly positive open-cube vertices, and mutation controls.
- Parent wrote and actually ran a separate, **nonblind** standard-library [checker](../review-waves/f129-ph7-girth-four-two-or-three-cycle/parent-f129-certificate-check-v1.py), SHA-256 `1ef15ce57a142c8cfcaf55caf1e89c195e34f13372813946dd2bf08aa486e5cd`, and its [result](../review-waves/f129-ph7-girth-four-two-or-three-cycle/parent-f129-certificate-result-v1.json), `4b2780c6e5367af77e236f8a8ecb521c91d68d99f9475a89dcbd54bd3c95fe83`. It reconstructs the literal symmetric polynomials and matches their canonical digests; checks both complete prefix-free covers, all **7,775,514** integer Bernstein coefficients and **421,110** interior vertices; and rejects altered-coefficient, missing-leaf, duplicate-leaf and prefix-collision controls for the stated reasons. Four rational substitution checks verify the displayed elimination identities at those samples. A separate exact permutation determinant checks the 4-cycle sign on a seven-cycle plus a 4-cycle; adding a 2-cycle breaks the tested coefficient identity. These sample controls do not replace the all-variable written elimination or Perron argument.
- On every leaf each coordinate is split at least once. For any open-cube point in the leaf, choose the equal endpoint when the local coordinate is at a boundary and otherwise an endpoint inside the global open cube. Its Bernstein vertex coefficient is strictly positive and its basis weight at the point is positive; all other terms are nonnegative. Thus the compactified polynomial, and hence the original polynomial on the positive orthant, is strictly positive. Computation trusts the stated Python integer/JSON/SHA and checker semantics; shared leaf data and same-harness execution are not independent-family or formal verification.
- The parent's result field `finished_native_clock` was sampled **before** its four rational samples and graph control were evaluated during result construction. The successful process output and the subsequent `20:47:51 PDT` hash/clock observation bound their completion; the field is not an exact completion time.

## Remaining problem

The 2-cycle and 3-cycle graphs remain open, including five eight-edge short-cycle shapes and higher-edge cases. The result does not construct or exclude a seven-state representation at `8/9`, determine the minimum order, establish the graph-shape classification independently of its review, or rehabilitate historical held work.
