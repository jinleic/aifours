# info-6 frontier: exact mod-8 residue census in the four-zero rank-six branch

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T20:57:59-0700 PDT**. **UNREVIEWED COMPUTER-ASSISTED AUTHOR CANDIDATE**: the two exact finite implementations agree, but the numerical census and written caller require a disjoint review. This is not a witness, unrestricted exclusion, formal/kernel proof or novelty claim.

## Conditional necessary count

Assume an actual balanced peak≤28 target has exactly four Walsh zeros. The preceding written reduction `frontier-20261028-four-zero-rank6-only-v1.md` (SHA-256 `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37`, 43 LF) forces the even-half polar to have rank six and its radical to be exactly the zero plane. Let `z=#{a∈K:q(a)=0}`, and let A_t count nonzero frequencies with W/4=t. The exact finite relaxation below gives the following further necessary restrictions:

| z | Allowed values of `A₋₂+A₆` |
|---:|---|
| 144 | 28, 52, 56, 60, 84 |
| 112 | 36, 44, 52, 60, 68, 72, 76, 84, 92, 100, 108 |

For |k|≤7, `A₋₂+A₆` is exactly the number of even-half frequencies with `(k/2)≡3 (mod4)`. The counts are necessary only. The census is exhaustive for a **mod-8 polynomial relaxation**; it does not assert that its solutions come from Boolean functions, or that other Walsh constraints are satisfied.

## Complete finite model

On K choose a basis whose last two coordinates span R=rad(B); write a=(x,r), x∈F₂⁶, r∈F₂². Since the zero plane equals R, q vanishes on R and descends to a nondegenerate six-variable quadratic. Up to invertible linear coordinates there are two cases, represented by the following **integer** polynomials before reducing modulo two:

    g₀⁺(a)=a₀a₁+a₂a₃+a₄a₅,
    g₀⁻(a)=g₀⁺(a)+a₀+a₁.                                                    (1)

Their q-zero sets have 144 and 112 points, respectively. Both include the four radical points. The standard symplectic normal form plus the two Arf classes justifies that this covers all actual cases; all coordinates and the radical are allowed to transform together.

For any actual f, let M be its one-support and n_a the number of x∈M with a·x=1. On K, every n_a is even and `k(a)≡n_a (mod8)`. Expanding parity as an integer modulo eight, then dividing by two modulo four, gives in any K-basis

    k(a)/2 ≡ Σ_i α_i a_i + Σ_{i<j} β_ij a_i a_j
              + 2Σ_{i<j<ℓ} γ_ijℓ a_i a_j a_ℓ                    (mod 4).      (2)

Here the α_i,β_ij are arbitrary residues modulo four and γ_ijℓ are arbitrary residues modulo two; their reductions modulo two reproduce q. Consequently every actual possibility is included in

    k(a)/2 ≡ g₀±(a)+2h(a) (mod 4),

where h is an arbitrary Boolean polynomial of degree≤3 on eight variables. We make **no** claim that every such h has an actual Boolean preimage.

For q(a)=0, an even target coefficient with |k|≤7 is 0 or ±4. The condition that the four zeros are exactly R is equivalent to

    h(a) = (g₀±(a)/2 mod 2) + 1_{a∉R}       (mod 2),      q(a)=0.          (3)

Take the 93 monomials of degree≤3 as columns, evaluate them at every q-zero point, and use (3) as the exact F₂ right-hand side. The result is an affine linear system. For q=1, evaluate `(g₀±+2h) mod4` and count the value 3. The complete computed census is:

| q-zero count | Matrix rank | Nullity | Number of h | Histogram of residue-3 counts: multiplicity |
|---:|---:|---:|---:|---|
| 144 | 84 | 9 | 512 | 28:8; 52:56; 56:384; 60:56; 84:8 |
| 112 | 76 | 17 | 131,072 | 36:40; 44:792; 52:2,160; 60:4,752; 68:8,640; 72:98,304; 76:8,640; 84:4,752; 92:2,160; 100:792; 108:40 |

The Python implementation uses high-pivot elimination; the independent C++ implementation uses low-pivot full RREF. Both enumerate every affine nullspace vector in Gray order and give the identical full multiplicity tables. Each includes an inconsistency mutation control. The scripts and result receipts are pinned below.

## Remaining gap

The finite restrictions do **not** finish even the four-zero branch. A formal count model survives the listed moment, dual, rank, phase, quartic-count and new residue filters: z=112, `A₋₂+A₆=108`, 168 peak-28 counts, and odd peak/unit count 208. All 257 dual coefficients are integral and nonnegative and were independently checked forward and backward. This is only a histogram; no common frequency assignment, code, Boolean inverse, or original witness has been produced. Other unlisted constraints may exclude it.

## Pinned evidence

All files are in this directory. The independent executable is pinned alongside both source files and exact receipts.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-rank6-mod8-census.py` | `0c639d87b3855eff83cf5737d937c1e4634a736cf0d10ebe086e685e8bb67761` | 77 |
| `frontier-20261028-rank6-mod8-census-result.json` | `b852dd70f60defd9098cf2707af2f9ffed3600b46fa218f7805a057ae8c550a2` | 47 |
| `frontier-20261028-rank6-mod8-census-independent.cpp` | `ffc04d6dd6e364bd8212a1f1ce818a364a6a4188e0d96e03f8f9a9fb3d3cb105` | 63 |
| `frontier-20261028-rank6-mod8-census-independent` executable | `e6d8a83366b71257fcbf3f78fe608f32bed00df7a6c5917ac75a1f707ff587bc` | — |
| `frontier-20261028-rank6-mod8-census-independent-result.json` | `9a59ce9e3f736c8a74a54a5d3d11dff5112f7ce46dbb7a90e07efed16260255c` | 7 |
| `frontier-20261028-four-zero-mod8-counts.py` | `1794458212bbacb314887e2b7354b9f5502e74c9be79a112f89ba3bf8e0f4543` | 54 |
| `frontier-20261028-four-zero-mod8-counts-result.json` | `4f2c667037511d35ae9aada921f3361c3812274fa06639e9024a10ebcc20b1ea` | 288 |
| `frontier-20261028-four-zero-mod8-counts-check.json` | `e74c5bfe89b8414e2644854198e4c6f124b6ec586847540961ccb2f9cb411ac8` | 19 |
| `frontier-20261028-four-zero-rank6-only-v1.md` | `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37` | 43 |

The original witness-or-unrestricted-exclusion target remains unresolved by this result. **END.**
