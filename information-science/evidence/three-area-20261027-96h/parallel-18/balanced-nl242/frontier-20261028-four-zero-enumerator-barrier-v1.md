# info-6 frontier: four-zero histogram survives the projective dual-enumerator relaxation

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:20:23-0700 PDT**. **Author-owned exact finite certificate; not yet disjointly reviewed.** This is a relaxed histogram, **not a Boolean function, binary code, construction, realizability proof, or NL242 witness**. It is a barrier to one specified count-only argument, not an impossibility or novelty claim.

## The explicitly feasible count system

For a hypothetical balanced nine-variable f with f(0)=0 and |W|≤28, let A_t count the **511 nonzero frequencies** with W/4=t, −7≤t≤7. Consider only the following necessary count conditions:

- A_t are nonnegative integers; `Σ A_t=511`, `Σ t A_t=128`, `Σ t² A_t=16384`, and the odd-t counts sum to 256.
- The total number of Walsh zeros is four: because W(0)=0, this is A₀=3.
- For every j=0,…,256, `D_j=[binom(256,j)+Σ_t A_t K_j(128+t)]/512` is a nonnegative integer, where `K_j(w)=Σ_i (−1)^i binom(w,i) binom(256−w,j−i)`.
- The projective endpoint checks `D₀=1`, `D₁=D₂=D₂₅₆=0`, `D₂₅₅∈{0,1}` hold. The last endpoint reflects distinct nonzero support columns when the support XOR is nonzero.

The following vector satisfies **all** of those conditions exactly, including all 257 dual coefficients:

| t | −7 | −6 | −5 | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_t | 52 | 113 | 15 | 0 | 65 | 0 | 3 | 3 | 18 | 5 | 25 | 4 | 1 | 130 | 77 |

It also has 129 formal peak-28 counts, consistent with the previously adopted ≥92 necessary peak count, and four formal |W|=16 counts; it is **not** claimed to satisfy every other known necessary condition, particularly frequency-placement or realization constraints. Therefore these listed moments, zero count, and *all* dual integrality/positivity constraints alone cannot exclude a four-zero target. The original actual-function witness-or-unrestricted-exclusion problem remains open.

## Checks and exact boundary

The first bounded integer solve produced an integrality-and-moment model with D₂₅₅=−9, so it **failed dual nonnegativity** and was not promoted. The refined solve added the distinct-column endpoint condition. Its resulting model has D₂₅₄=69 and D₂₅₅=0; exact integer evaluation found every D_j nonnegative and their sum `2²⁴⁷`.

The generator checked all 15 compact coefficient congruences and computed all 257 original Krawtchouk numerators directly by the binomial definition. A separately written checker recomputed the entire forward transform using the three-term Krawtchouk recurrence, checked all divisibilities/nonnegativity and endpoint values, and performed the **inverse** transform to recover every one of the 257 primal coefficients. A changed count failed its mutation control. These are executed finite integer checks, not an independent human review or a proof that any code or truth table realizes the vector. The Z3 result is only a way of finding the vector: the second checker directly verifies the listed finite equalities without relying on solver correctness.

## Pinned evidence

All paths are in this directory; SHA-256 values refer to observed bytes.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-zero-four-relaxation.py` | `0a1c87451ff847cb6fed82ae4d8006d065ca638809097d170711a68a8377740f` | 89 |
| `frontier-20261028-zero-four-relaxation-result.json` | `05ca70f5350b17d74be73c6d8f6c30f39f592fedea74a8d3cf4dae3907070f04` | 306 |
| `frontier-20261028-zero-four-positive-relaxation.py` | `616fadfc7162dee4038217faee49a718adadbeda63d905c90a8f8b240bbbb8bc` | 81 |
| `frontier-20261028-zero-four-positive-relaxation-result.json` | `7651a064d75fd980ab4b127d5deb71b75ad0e3bd62921d8622e0fa22c92f62a8` | 310 |
| `frontier-20261028-zero-four-certificate-check.py` | `d0e71e1327be06983e9e6646237d9e7e50ee1b5c6302defee3cc143085294fc3` | 61 |
| `frontier-20261028-zero-four-certificate-check-result.json` | `2e67903e7a577c82a59d197b202a2b061dc35a09656a8310e5b2d03f2da98345` | 19 |

No histogram has been confused with an actual truth table, and no historical HELD result is used as a premise. **END.**
