# Three further cyclic spectra fail a self-orthogonality test

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:12:52 PDT 2026. This is an all-field, all-phase exclusion conditional on the cyclic 6D graph and the preceding simple-spectrum/full-support reduction; it is not a general G6 or 1RQLS10 no-go.

## Claim

Among the 32 cyclic classes remaining after `frontier-20261029-cyclic15-semicircle-8-no-go-v1.md` SHA-256 `2850d6b2f80e5fa83ae93001e59d9dc6383bb4111be2eeab7f12b3f41e617007`, the following three cannot occur:

| Spectrum representative | Missing self-orthogonality | Separating angle |
|---|---:|---:|
| `(0,1,2,3,5,11)` | `<v7,U^(-7)v7>=0` | `5pi/3` |
| `(0,1,2,4,10,11)` | `<v2,U^(-2)v2>=0` | `4pi/3` |
| `(0,1,3,5,7,10)` | `<v2,U^(-2)v2>=0` | `5pi/3` |

This leaves **29** conditional cyclic spectrum classes: 23 with U^5 multiplicities `(3,2,1)` and six with `(2,2,2)`. Their manifest `frontier-20261029-cyclic15-29-residual-spectra-v1.json` has SHA-256 `59962a77982e79225d8104079c682e2f67be1401d991f1d2f818af4f259ca9bb`. No surviving class is claimed feasible.

## Positive-compression argument

Use the two-plane normal form `frontier-20261029-cyclic15-two-plane-normal-form-v1.md` SHA-256 `b2b0ca5e4d1242c9849bc7d77b4f8183e59a6f3bdef62e8606989b617a8849e7`. For d=2 or 7 let N be a 6×2 exact cofactor basis for the kernel of the exponent matrix with rows `(0,5,-d,5-d)`, and let `B=diag(p_j^(-1/2))N` be a basis of the corresponding 2D plane. Here all p_j are positive and their sum in each exponent residue class modulo 3 is 1/3.

For the separating angle theta in the table, define

`H = Re(e^(-i theta) B† U^(-d) B) = N† diag(h_j/p_j) N`,

where `h_j=cos(theta+2 pi d a_j/15)`. If H is positive definite, then `Re(e^(-i theta)<x,U^(-d)x>)>0` for every nonzero x in the plane, so the relevant paired self-orthogonality is impossible. For a 2×2 Hermitian matrix, positivity of both trace and determinant is sufficient.

Cauchy–Binet gives exact homogeneous numerators

`(product_l p_l) tr(H) = sum_j h_j ||N[j,:]||² product_(l≠j) p_l`,

`(product_l p_l) det(H) = sum_(j<k) h_j h_k |det N[{j,k},:]|² product_(l notin {j,k}) p_l`.

For each of the three spectra, multiplying individual terms by suitable powers of the identities `3 sum_(j:a_j≡r mod 3)p_j=1` makes each expression multihomogeneous. The exact expanded trace and determinant numerators have **strictly positive nonzero coefficients**. Hence both are strictly positive for every allowed positive p, so H is positive definite and no paired ray exists. The trace degree per residue is 3 in all three cases; the determinant degrees are 3, 3 and 4 respectively.

## Exact evidence and limits

`frontier-20261029-cyclic15-selfplane-positivity-proof-v1.py` SHA-256 `e5c77c6b24b28424090cf8dfea0090467b8cda3d52a9f779df0cd260e4953ad4` produces the complete cofactor bases and positive expanded coefficients in `frontier-20261029-cyclic15-selfplane-positivity-proof-v1.json` SHA-256 `f150d1f050f2e55051ccc239e8c64c2ae2b1eb89ce766991303b8808eb3689ad`.

The separate same-owner replay `frontier-20261029-cyclic15-selfplane-positivity-replay-v1.py` SHA-256 `4d0c92ec738d72c4b6468ad76afb0a5cfa996cb196acec3ee30df423940fca71` reconstructs the field elements in `1,omega,eta,omega eta` over Q(sqrt(5)), checks all cofactors and polynomial coefficients, and certifies **185** strict signs by rational trigonometric enclosures. Its output `frontier-20261029-cyclic15-selfplane-positivity-replay-v1.json` SHA-256 `1debfdbf3c60401bed0acc9012c864386e86567b4f5485fa7ecd6c5d06265c81` is **PASS** at 03:12:51 PDT.

The spectral quotient, field-basis caller, Hermitian positive-definiteness argument and sign enclosures require independent mathematical review. The remaining 29 cyclic classes, symmetry-breaking G6 representations, and the 25 omitted QLS cells are not settled; no formal-kernel or novelty claim is made.
