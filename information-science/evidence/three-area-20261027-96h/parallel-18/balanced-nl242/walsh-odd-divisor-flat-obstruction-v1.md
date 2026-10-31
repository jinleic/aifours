# info-6: an odd-divisor obstruction for whole affine Walsh restrictions

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:25:09-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is an all-magnitudes, all-affine-flats necessary condition, not a selected layer/flat, witness, unrestricted no-go, rank/type exclusion, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program, selected-state/boundary probe or source enumeration was used.

## Claim

Let f:F₂⁹→{0,1} be arbitrary, and let m≥1 be any odd integer. For every affine frequency d-flat E=a₀+H with 0≤d≤8, if every W_f value on E is divisible by m, then either all those values are zero or

    2m ≤ 2^{9−d}.                                                (1)

If d=9 and m>1, the entire Walsh spectrum cannot be divisible by m. These statements require neither balance nor a fixed original rank; they quantify over every f, m and E.

For the original balanced peak≤28 target, W is divisible by 4. Thus, for example as a fully quantified corollary, every affine frequency flat of dimension at least 6 containing a |W|=28 coefficient must also contain a coefficient not divisible by 7, hence a **nonzero nonpeak** coefficient. Zeros are explicitly allowed in the flat; the claim is stronger than excluding a flat whose coefficients are all peaks. No specific magnitude layer, flat or coefficient is selected.

## Proof

Put U=H^⊥ and, for each source coset y∈V/U, define the coherently oriented local Walsh sum C(y) as in the all-affine restriction identity. Then

    2^d C(y)=Σ_{a∈E} W_f(a)χ_a(x_y).                              (2)

The right side is divisible by m. Since m is odd, gcd(m,2^d)=1, so m divides every integer C(y). For d≤8 each source coset has even size, so C(y) is even. Thus any nonzero C(y) has magnitude at least 2m. Fourier inversion on H says the C-array vanishes identically exactly when the W-values on E all vanish. If some W-value on E is nonzero, some C(y) is nonzero, and its magnitude is at most the source-coset size 2^{9−d}; this proves (1).

For d=9 each source coset is a singleton and C(y)=±1. If every W-value is divisible by an odd m>1, (2) would force m|±1, impossible. Equivalently the full Fourier inverse forbids a common nontrivial odd divisor. ∎

## Exact scope and residual

This obstruction does not decide whether any particular flat or any original witness exists, and it does not prove a no-go. The full original balanced peak-28 witness-or-unrestricted-exclusion question and `(24,24,2)` remain open. The parent-notified earlier results are not upgraded by this unreviewed theorem.

Inputs are the S1 definitions and the all-affine restriction identity in `walsh-affine-restriction-coupling-v1.md` SHA-256 `1c03c02f37f10c5b74e5f81b5c69e56fcf1f02ef02684367e3869856ea84c457`, 43 LF; its relation to the preceding constant-magnitude author theorem `walsh-constant-magnitude-odd-divisor-v1.md` SHA-256 `d0c351677d8bdad6a93c5d6eb93b515e9f92a5bc651934ac60b05b2d45e4abe3`, 37 LF, with edge clarification `walsh-constant-magnitude-odd-divisor-addendum-v1.md` SHA-256 `ce0ab2816882784f76a9c46ff3ff15099de309d6366fac97ca398c3b5e57c09e`, 7 LF, is generalization only, not independent review. All three were live-pinned before this candidate write. No old Gate-I/candidate/HELD body, stopped half-split/canonical or global truth-degree/ANF method, or selection guide is an input. Book-source equivalence is only at the separate internal bridge; independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed. Prior exposure, metadata-poll and delayed-pin documentary MINORs, all S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
