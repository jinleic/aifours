# Balanced NL242 (3,112), L=16: s=15 excluded by the two 3-space sign spectra

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:17:07-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** Conditional on v20 and the source-separated v205 L16 chain, this excludes the whole s=15 case, not L=16 or a residue type. All-variable hand argument; no scientific program, selected numeric-state probe, independent review, formal/kernel or novelty claim.

## 1. Sign transforms on the two 3-spaces

By v20, translate so Σ=F∪G for complementary 3-spaces F,G meeting only at 0. Multiplying all signs by −1 if necessary does not change divisibility; take g(0)=+1. Let A,B be the eight Walsh values of g restricted to F,G, respectively. Over the independent dual variables,

    Ψ(ξ_F,ξ_G) = A(ξ_F)+B(ξ_G)−1.                               (1)

For any ±1 function on a 3-space with value +1 at 0, its eight Walsh values sum to 8 and their squares sum to 64. The product of the eight summands defining a Walsh value is independent of the frequency, because the sum of all points of the 3-space is 0. Consequently all eight values are either multiples of 4 or all congruent to 2 mod 4.

- In the multiple-of-4 case, Parseval leaves either a single nonzero value +8, or four values ±4 and four zero. The sum constraint makes the latter three +4 and one −4.
- In the 2-mod-4 case all eight are nonzero; Parseval gives one value ±6 and seven values ±2. If the 6 is +6, the seven 2s have four +2 and three −2. If the 6 is −6, all seven are +2.

Thus their residue multiplicities (n₀,n₁,n₂), modulo 3, are exactly one of

    I   = (7,0,1),     II  = (4,3,1),
    III = (1,3,4),     IV  = (1,0,7).                            (2)

These are derived spectral types of every sign function, not a search through chosen functions.

## 2. Zero-count bound

For vectors a,b of residue multiplicities from (2), equation (1) gives

    N₀ = a₀b₁+a₁b₀+a₂b₂.

The following symmetric table follows by direct substitution into this single identity:

| A \\ B | I | II | III | IV |
|---|---:|---:|---:|---:|
| I | 1 | 22 | 25 | 7 |
| II | 22 | 25 | 19 | 10 |
| III | 25 | 19 | 22 | 31 |
| IV | 7 | 10 | 31 | 49 |

Hence **N₀≤49 for every sign function on F∪G**. But v6's L16 budget requires N₀≥52. Contradiction. ∎

## Exact status and dependency

Conditional on the unreviewed v205 chain and `rank6-112-L16-s15-support-classification-v20.md` SHA-256 `0d3b51c59eec62cbb260478f088a7d7976b0fc6a90ff8d32df80a253377e2ba5`, 43 LF, **s=15 is excluded** at (3,112), L=16. In combination with the earlier author-only reductions and v19, s=16 is the only remaining L=16 case. No whole-L16 or whole-type exclusion, witness, unrestricted exclusion, (24,24,2) closure or novelty follows. All earlier findings, pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and every HELD/ZERO/NONINPUT cut remain binding.
