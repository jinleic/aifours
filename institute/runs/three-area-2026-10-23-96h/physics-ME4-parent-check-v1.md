# ME4 maximally-entangled-reference theorem — parent written check v1

Before-creation clock observed: **2026-10-23T13:12 PT**.

## Verdict

**WRITTEN_CHECKED (in-harness level).** Theorem ME4 — `q_3(C) >= 0` for every complex rank-≤2 operator whose range or co-range contains a ray `a ⊗ η` with η maximally entangled on two ququarts — is supported by two complete independent written reconstructions with no defect found: the author manuscript (SHA `684ec10f…`) and the MathResearch96h review (0F/0M/0m, with an independent entrywise contraction table for the raw identity, independent f-basis action matrices, and hand recomputation of all eight partial traces of the separation example), plus this parent spot-check.

## Parent spot-checks actually performed (exact rational arithmetic)

- Identity block (§6): with `C=[[5/4,-1],[-1,5/4]]`, `S=[[5/4,-3/4],[-1,1/4]]`, Gram `[[16,4],[4,16]]`: `G·C=[[16,-11],[-11,16]]` and `G·S=[[16,-11],[-11,1]]`, both symmetric (confirming G-Hermiticity of the action matrices); `Form(C−S)=[[0,0],[0,15]]`, `Form(C+S)=[[32,−22],[−22,17]]` exactly as displayed; the SOS `32|α−11β/16|²+(15/8)|β|²` expands to the same matrix.
- Traceless-block SOS coefficients: `1/2+4/3=11/6` (SOS-minus z₁ coefficient) and `(29/12)(8/29)²+57/58 = 7/6` (SOS-plus z₊² coefficient) verified exactly.
- Separation example: `q₃ = 2 − ½(2/9+7/12+7/12) + ¼(4/3) = 59/36` verified exactly from the eight partial-trace norms.

## Evidence boundary

- The one admitted exact assay (r=4 PSD in both signs) agrees with but does not independently verify the written proof; the assay encoding and the written derivation are separate evidence, as labeled.
- The r=2 co-Choi failure (−6/17) kills only the general all-entangled-reference domination route, not ME4; a hand d=2 obstruction now also exists in the lane's addendum (pending its own review).
- Prior-art screen (Wu–Zou sectors, ULAM envelope, refreshed arXiv/INSPIRE/EulerSolve/openai-math): **NOVELTY_UNCLEAR**, no matched statement found; not a clearance.
- W4 unrestricted, arbitrary entangled references, other copy numbers, all-α theorem, asymptotic NPT: **NOT PROVED**. No Lean/kernel claim.
