# info-6: an odd-divisor obstruction for every constant-magnitude affine Walsh flat

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:11:56-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a universally quantified local/global arithmetic obstruction, not a selected magnitude/flat, original witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program or selected-state/boundary probe was used.

## Claim

Let f:F₂⁹→{0,1} be any Boolean function, balanced or not. Suppose an affine frequency d-flat E=a₀+H, with 0≤d≤8, has |W_f(a)|=M>0 at every a∈E. Write M=2^t m with m odd. Then

    2m ≤ 2^{9−d},     and at most 2^{2t−2}                        (1)

of the coherently oriented local Walsh coefficients on the source cosets of H^⊥ are nonzero. For t=2 their nonzero pattern is exactly **one coefficient of magnitude 4m**, or **four coefficients of magnitude 2m**; in the four-case their labels form an affine 2-flat and their sign product is −1. The one-case is an affine character sign pattern on E. These are necessary statements for every such E; neither pattern nor any f is asserted to exist.

For the original balanced peak≤28 target, W is divisible by 4 and its possible nonzero magnitudes all fall under (1). In particular any fully peak flat with M=28 has d≤5; the same dimension bound holds for M=20, while M=12 or 24 gives d≤6. These are universal **layer constraints**, not selected numerical tests and not an original-target no-go.

## Proof

Put U=H^⊥ and choose a linear section y↦x_y of V/U. Write W(a₀+h)=Mε(h) with ε(h)=±1. For every source coset define the coherently oriented local Walsh sum

    C(y)=χ_{a₀}(x_y) Σ_{x∈x_y+U}(-1)^{f(x)}χ_{a₀}(x).

The affine restriction identity gives

    2^d C(y)=M Σ_{h∈H} ε(h)χ_h(x_y).                             (2)

Since d≤8, every source coset has even size, so C(y) is even. Because m is odd and divides M, (2) and gcd(m,2^d)=1 imply m|C(y). Any nonzero C(y) therefore has |C(y)|≥2m. The transform on the right of (2) is nonzero somewhere; since each local sum has at most 2^{9−d} terms, the dimension inequality in (1) follows.

Parseval on H and (2) give the exact common-object energy

    Σ_y C(y)²=M².                                                 (3)

Thus the number of nonzero local coefficients is at most M²/(2m)²=2^{2t−2}. If t=2, divide each nonzero C by 2m. The resulting nonzero integers have squares summing to 4, so either one has magnitude 2 or four have magnitude 1. In the one-case the inverse H-transform makes ε an affine character. In the four-case inversion makes ε half the sum of four signed characters; because ε=±1 everywhere, their sign product is −1 at every point. The four labels therefore XOR to 0 and form an affine 2-flat, with transform-sign product −1. Changing the linear section multiplies these signs by a character, whose product over that 2-flat is +1. ∎

## Scope and remaining gap

The theorem does not require balance until the final target-specific list of possible Walsh magnitudes; it does not decide whether any constant-magnitude flat exists. For M=28 it supplies an independent written route to the basic dimension obstruction in `walsh-saturated-flat-rigidity-v1.md`, not an independent review of that paper or an adoption. It does not reproduce its extra mod-4 bilinear-radical claim.

Inputs are the S1 supplied definitions and the unreviewed all-affine restriction identity in `walsh-affine-restriction-coupling-v1.md` SHA-256 `1c03c02f37f10c5b74e5f81b5c69e56fcf1f02ef02684367e3869856ea84c457`, 43 LF, with elementary integer divisibility/character Parseval. No old Gate-I/candidate/HELD body, stopped half-split/canonical or global truth-degree/ANF method, or source-selection guide is an input. The original balanced peak-28 witness-or-unrestricted-no-go, all original rank/weight alternatives and `(24,24,2)` remain open. Main-notified written support for earlier premises does not adopt this theorem; independent full-scope review, human, formal/kernel, executable and novelty remain unperformed. Prior exposure, metadata-poll MINOR, S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
