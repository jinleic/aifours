# Balanced NL242 (3,112): the final s=16 branch at L=16, and the resulting author-only L≥18 floor

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:25:16-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** Conditional on the entire source-separated v205 chain and its errata, this excludes L=16 at (3,112) and claims L≥18 there. It excludes no residue type and does not settle the original witness-or-unrestricted-exclusion question. No independent review, formal/kernel check, scientific program, selected-state probe or novelty claim.

## 1. Excluding the remaining s=16 branch

By v23, s=16 at L=16 is reduced to τ=0 and Γ=+1. In that branch v22 gives N₀=54, m=10, four |Ψ|=12 values, and signed plane sum A₄=40. Let W be the unsigned Walsh transform of 1_Σ. Write t for the number of nonzero frequencies with |W|=8. The unsigned moment calculation in v22 gives

    p=20+2t,    # {ω≠0: |W(ω)|=4}=48−4t,
    # {ω: W(ω)=0}=15+3t,

where p is the number of Σ-planes. Since p≥A₄=40, t≥10, so W has at least 45 zeros.

Fix any frequency ζ* with |Ψ(ζ*)|=12 and let ε be its sign. Of the sixteen signs g(x)χ_{ζ*}(x), exactly two disagree with ε; call their distinct positions y,z and put d=y+z≠0. For every η,

    Ψ(ζ*+η)=ε[W(η)−2χ_η(y)−2χ_η(z)].                            (1)

The half χ_η(d)=+1 contains 32 frequencies. Since W has at least 45 zeros, at least 13 of its zeros lie in this half. At each such zero, χ_η(y)=χ_η(z), so (1) gives |Ψ(ζ*+η)|=4. These are 13 distinct non-3-divisible Ψ-values, contradicting m=10 (and already contradicting m≤12). Therefore the final s=16 branch is impossible. ∎

## 2. Consequence at this exact author scope

The prior source-separated author chain reports:

- L≥16 and even L at (3,112): v5 and its cited parity/base chain;
- at L=16, s=0,…,11,13,14 excluded by v6–v8 and their errata;
- s=12 excluded by the d=4/6 reductions and v11/v12/v17/v18/v19 at d=5;
- s=15 excluded by v20/v21;
- s=16 excluded by v22/v23 and §1 above.

Thus, **conditional on every unreviewed premise and proof in that entire chain, the author candidate is L≥18 at (3,112)**. The remaining (3,112) window is even L in 18,…,28. The earlier (3,144) L≥12 floor remains separately author-only. These are necessary frontiers, not a witness, a whole-type or unrestricted exclusion, (24,24,2) closure, cross-vendor/human/kernel verification, or novelty.

## Exact dependencies and process

- `rank6-112-L16-s16-tau0-positive-spectral-v22.md`, SHA-256 `b710c08be56a4e3f8dabf524f706fa82f477f4c31925d4d204a7ba9cadd20284`, 54 LF.
- `rank6-112-L16-s16-tau-nonzero-and-negative-exclusion-v23.md`, SHA-256 `95d0ac2a74367702e0aad3d0baad63639e93bf6daf82d5705d7e7a9b3f918a96`, 40 LF.
- The exact upstream v205 chain, source cuts and mandatory errata identified in those files, and v6–v21 as listed above; no historical HELD candidate is an input.

All findings and pre-pin corrections, the v263 pre-cutoff early-stop deviation, HOLD v2, N4 UNKNOWN historical child exit unestablished, aux214 STOP, and every HELD/ZERO/NONINPUT cut remain binding. Novelty is UNCLEARED; no continuous-work or method-clean assurance is made.
