# Mixed imbalance branches exclude three more cyclic spectra

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:28:37 PDT 2026. This continues the all-field cyclic reduction of `frontier-20261029-cyclic15-imbalance-16-no-go-v1.md` SHA-256 `ffb91f78c106751d67a6322bf568a9fc624356872ee1d6acf1beb4adaa7917d1`; it does not rule out arbitrary G6 or QLS10.

## Claim and complete branch table

The three spectrum representatives below cannot occur in a cyclic-equivariant 45-distinct-ray C6 lift, for any spectral population field or complex phases. Each low-index tuple lists, in residue-class order, the **zero-based positions in the displayed spectrum** of the low v5 population in each short ±3 pair. The row-imbalance theorem makes these branch choices exhaustive.

| Spectrum | Low-index tuple | Exact obstruction |
|---|---|---|
| `(0,1,2,3,5,10)` | `(0,2)` | v2 self-plane, theta `25pi/15` |
| same | `(0,4)` | positive cross-plane determinant |
| same | `(3,2)` | two high rows collide modulo 5 |
| same | `(3,4)` | v7 self-plane, theta `13pi/15` |
| `(0,1,2,4,9,11)` | `(1)` | v2 self-plane, theta `23pi/15` |
| same | `(3)` | v7 self-plane, theta `29pi/15` |
| `(0,1,3,5,8,10)` | `(0,3)` | two high rows collide modulo 5 |
| same | `(0,4)` | v2 self-plane, theta `24pi/15` |
| same | `(2,3)` | v7 self-plane, theta `14pi/15` |
| same | `(2,4)` | two high rows collide modulo 5 |

The conditional cyclic search therefore has **10 spectral classes** left: seven with U^5 multiplicities `(3,2,1)` and three with `(2,2,2)`. Their exact manifest `frontier-20261029-cyclic15-10-residual-spectra-v1.json` has SHA-256 `d107780a8cc21d27ed7c1129b3f331e31fbb50882d567d069286351b87cd612b`. This is a list of unsolved cases, not a claim that any are realizable.

## Why each branch fails

For every short pair, the exact row-imbalance theorem forces one v5 population below `7/240` and its partner above `73/240`, as derived in the preceding 16-class packet. Write the two populations as

`p_low=(7/240)x_low`, `p_high=(73/240)x_low+(1/3)x_high`,

with positive x variables summing to 1. In any other U^5 group write `p_j=x_j/3` with positive x summing to 1. These substitutions are made independently for all short groups in a branch.

- **Collision:** two selected high rows have exponents congruent mod 5 but different U^5 classes. For their exponent difference 5 or 10, all three row coefficients for d=2,5,7 have magnitude 1. Since both v5 populations exceed 1/4, the triangle/Cauchy inequality of `frontier-20261029-cyclic15-short-two-coset-no-go-v1.md` SHA-256 `29aa9aa0930a2ca393ed34ad823388bc0a72cf562cd7616795a02468293cc3bb` is impossible. This argument applies to the two high rows alone and does not require the whole spectrum to be two cosets.
- **Cross determinant:** the determinant numerator P of `frontier-20261029-cyclic15-crossplane-38-no-go-v1.md` SHA-256 `0a4bd44d9dca934397153be9547e029b6e171677f0690c9862e6262293d06bd8` has a strict positive-coefficient expansion on the specified branch after multiplication by group identities `sum x=1`. It cannot vanish as cross-orthogonality requires.
- **Self plane:** with the indicated d and theta, the 2×2 Hermitian self-plane compression from `frontier-20261029-cyclic15-selfplane-3-no-go-v1.md` SHA-256 `f4f22317a1d497473b7767ef84924da11fcd018e47fad8be084618cb21f37479` has trace and determinant with strict positive-coefficient expansions on the branch. It is positive definite, so `<v_d,U^(-d)v_d>` cannot be zero.

All polynomial substitutions use only the strict rational relaxation of the exact imbalance and cover the full irrational boundary allowed by that condition.

## Exact evidence and limits

`frontier-20261029-cyclic15-mixed-branch-proof-v1.py` SHA-256 `43933740bcc04aea381125cbec83cd7dad64dace829b7927f13286274c4491b6` records all 10 branches, cofactor bases, collision indices and exact positive coefficients in `frontier-20261029-cyclic15-mixed-branch-proof-v1.json` SHA-256 `72c51e1e752a0fbb7a1ce48fb93a4f59d0c7a0fcfb69330457a4ba8973e447ab`.

The separate same-owner replay `frontier-20261029-cyclic15-mixed-branch-replay-v1.py` SHA-256 `43e6554061b5557ecbacb76690bf6c8cdd6677babf622749038f61ec21543092` reconstructs the determinant and self-plane polynomials in an independent cyclotomic basis, verifies branch coverage and collisions, and checks **667** strict coefficient signs using rational intervals. Result `frontier-20261029-cyclic15-mixed-branch-replay-v1.json` SHA-256 `3ea48db95dccc9ee6a7807900fbbe35d5185ee14e3c61a3e983068901e0a708f` is **PASS** at 03:28:37 PDT.

The imported rank-4/full-support proof, affine quotient, row imbalance, positive-definiteness and all exact callers require independent mathematical review. The remaining 10 cyclic cases, all symmetry-breaking 6D complements and the 25 omitted QLS cells remain open; no formal-kernel or novelty claim is made.
