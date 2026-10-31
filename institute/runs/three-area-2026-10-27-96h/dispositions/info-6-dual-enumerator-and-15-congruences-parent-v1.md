# Parent disposition — info-6-dual-enumerator-and-15-congruences-parent

Observed clock before writing: **2026-10-27T17:46:13-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Inputs actually read by Main

- [Original definition packet](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-6-full-walsh-packet-v1.md), SHA256 `a9931cf5a12f174c232e6ad50fba993e5cd01ee9d4ab13dcfe0bd35dc69d3d37`, 35 LF, raw 1–35.
- Author [projective-code equivalence](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/walsh-projective-code-equivalence-v1.md), SHA256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF, raw 1–25, 26–50.
- Author [dual enumerator](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/dual-enumerator-symbolic-v1.md), SHA256 `7a05f4b954bacaf5ba865fa3559dd0ab5ff4f130f32383d60d9245ded0c92897`, 99 LF, raw 1–35, 36–70, 71–99.
- Author [15-coefficient congruence reduction](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/dual-enumerator-congruence-reduction-v1.md), SHA256 `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad`, 70 LF, raw 1–35, 36–70.
- Reviewer [w92 (MathSun8-2)](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/review-w92-info-6-dual-enumerator-pair-v1.md), SHA256 `f95685bb6e44228e203a2240f322d3fffb52816224958b8b60df601aa8738e40`, 274 LF, raw 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–274 through ending; 0 new FATAL / 0 MAJOR / 0 MINOR at exact scope, nonblind same-harness review.
- Earlier parent-adopted [nonzero support XOR](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-support-xor-peak-multiplicity-parent-v1.md) and [at least 92 Walsh peaks](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-hyperplane-energy-and-92-peak-parent-v1.md) are used only at those stated scopes, including their mandatory count-direction correction. This disposition does not newly adopt every theorem in their source chains.
- Status-only: [unreleased owner extension STOP](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/nl242-post-enumerator-unreleased-extension-parent-stop-v1.json) and [post-pause reasoning addendum](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/nl242-post-enumerator-pause-further-reasoning-addendum-v1.json); the entire episodes and every consumer remain NONINPUT. The supplied mathematical files and w92 predate these findings; timing is not a cognitive-noninfluence certificate.

## Exact written-supported statements

1. A balanced f:F₂⁹→{0,1} with Walsh peak ≤28 exists iff a binary [256,9] code has a generator with 256 distinct nonzero columns and every nonzero word has weight in [121,135]. For the forward direction a translation placing zero outside the one-support preserves the original problem; the converse uses the actual columns as that support. Neither direction supplies such a code.
2. Let A_t count nonzero words of weight 128+t, −7≤t≤7. For any such code, the exact moment/parity/peak requirements and dual identities in the supplied candidate hold. For any nonnegative integer solution of that full stated system, 5296≤D₃≤5594, 30≤D₂₅₄≤71, 0≤D₂₅₅≤11, and (A₃−A₋₃)+5(A₅−A₋₅)+14(A₇−A₋₇)≡0 mod 8. These bounds are necessary only.
3. For ARBITRARY integers A_t (without moment, positivity or realizability assumptions), all 257 dual numerator divisibility conditions modulo 512 are equivalent to the following SINGLE coefficientwise polynomial congruence, meaning its 15 coefficients of degrees 0–14 all vanish:

   B(z)+(1−z²)⁷+256z(1−z²)⁶≡0 mod 512,  where B(z)=Σ_{t=−7}^7 A_t(1−z)^(7+t)(1+z)^(7−t).

## Parent checks and non-claims

Character orthogonality gives the full code/Boolean caller and all-j dual identity, with the zero codeword kept separate. For the third statement, the all-index generating polynomial factors as (1+z)²⁵⁶+(1−z²)¹²¹B(z); the latter factor has constant term one and is a unit over the formal-series ring modulo 512. The supplied binomial-valuation argument proves the remaining factor reduces to the degree-14 polynomial above, in both directions. No selected distribution, numerical test or scientific execution was used.

No simultaneous feasibility/infeasibility of the complete nonnegative system, code or Boolean witness, unrestricted exclusion, closure of (24,24,2), or new original-target solution is inferred. Divisibility alone does not imply dual nonnegativity or actual-code realization. Historical source/book equivalence and novelty remain UNCLEAR. Existing prior count correction and all STOP/HOLD/ZERO, L1, N4 UNKNOWN (historical child exit unestablished) and auxiliary214 STOP persist. Independent-model CLI, formal/kernel, executable and human review were not performed for these new statements.

