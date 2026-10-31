# Cross-plane positivity excludes 38 more cyclic spectra over all fields

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 03:02:07 PDT 2026. This strengthens the conditional 78-class cyclic reduction `frontier-20261029-cyclic15-78-residual-spectra-v1.md` SHA-256 `d709af376455f106e4312f56a29b54b1a6d15ccf025aa85d01f76f337de692b2`. It does not rule out the remaining cyclic classes, symmetry-breaking complements, or unrestricted 1RQLS10.

## Claim and remaining scope

Of the 78 spectral classes left by the simple-spectrum, multiplicity and two-coset exclusions, **38 cannot occur** in any 45-distinct-ray C6 lift with unitary translation, for arbitrary complex amplitudes and any spectral population field. Hence at most **40** cyclic spectrum classes remain: 30 with U^5 multiplicities `(3,2,1)` and 10 with `(2,2,2)`. Their complete manifest is `frontier-20261029-cyclic15-40-residual-spectra-v1.json` SHA-256 `dd178c5ee25f214b97d843adbe5ed1fe93a0b8eccacb738fb09f1644ddc5a153`. None is claimed feasible.

## Why a 4×4 determinant must vanish

Use the explicit reduction in `frontier-20261029-cyclic15-two-plane-normal-form-v1.md` SHA-256 `b2b0ca5e4d1242c9849bc7d77b4f8183e59a6f3bdef62e8606989b617a8849e7`. In a U eigenbasis write `v5_j=sqrt(p_j)>0`, with three residue-class sums of p equal to 1/3. Its two intersection planes L,M have dimension exactly two. Let N_L,N_M be any 6×2 bases of the kernels of the respective 4×6 matrices with exponent rows

`(0,5,-2,3)` and `(0,5,-7,-2)`.

Then bases of L and M are `B_L=diag(p_j^(-1/2)) N_L` and `B_M=diag(p_j^(-1/2)) N_M`. The four cross-orthogonality equations require nonzero z,w∈C² with `z† C_e w=0` for e=`0,-7,2,-5`, where

`C_e=N_L† diag(p_j^(-1) lambda_j^e) N_M`.

Consequently the four 2×2 matrices C_e cannot span all of M2(C), so the 4×4 matrix D whose rows are their vectorizations must have determinant 0. The cofactor bases in the certificate have exact nonzero pivots, so they are valid for all positive populations.

## Positive Cauchy–Binet certificates

For a 4-element index set I, put

`R[j,(a,b)]=conjugate(N_L[j,a]) N_M[j,b]`,

`C_I=det([lambda_j^e]_(e∈{0,-7,2,-5},j∈I)) det([R_j]_(j∈I))`.

Cauchy–Binet gives

`det D = sum_(|I|=4) C_I product_(j∈I) (1/p_j)`.

For an exact nonzero reference coefficient C_ref, multiply by `conjugate(C_ref) product_j p_j`; the determinant can vanish only if

`P(p)=sum_(|I|=4) C_I conjugate(C_ref) product_(j∉I) p_j = 0`.

For each of the 38 listed spectra, the certificate chooses an overall sign and an integer L=2,3 or 4. In each term it multiplies by suitable powers of `3 sum_(j:a_j≡r mod 3) p_j=1` so every term has degree L in each residue-class group. After expansion **every nonzero coefficient is strictly positive**, while every p_j is positive. Thus the resulting polynomial, equal to either P or −P on the allowed population domain, is strictly positive. This contradicts `det D=0`. The certificate finds 30 cases with L=2, seven with L=3 and one with L=4.

## Exact certificate and verification boundary

`frontier-20261029-cyclic15-crossplane-positivity-proof-v1.py` SHA-256 `19a9bf75db1d3d3a8f92ed305294bc1053fba89b6572bb93d34017e44facc694` produces the complete spectrum-by-spectrum cofactor and expanded-polynomial data in `frontier-20261029-cyclic15-crossplane-positivity-proof-v1.json` SHA-256 `9deaf495ac24e20f3b90a5718676a046c4569dac2c83ee8c3ae43c206def5665`.

The separate same-owner replay `frontier-20261029-cyclic15-crossplane-positivity-replay-v1.py` SHA-256 `2722a226e3612b352d0fff5e183ea073c5ae2b8da175de2284ec2c6ccc83fd73` recomputes the cofactors and Cauchy–Binet coefficients in the different exact basis `1,omega,eta,omega eta` over Q(sqrt(5)), compares every stored coefficient across bases, checks all **1095** positive coefficients using rational enclosures obtained from Machin's formula and alternating cosine series, and verifies the 38 representatives belong to the 78-class manifest. Output `frontier-20261029-cyclic15-crossplane-positivity-replay-v1.json` SHA-256 `14409dea8fa68ef397a09ac446ad2f4afef9bb1e5cb96b3c19e55eae6ce32a2d` records **PASS** at 03:02:07 PDT.

The lower bound on v5 support, row-rank reduction, Cauchy–Binet caller, strict-sign enclosures, affine spectral quotient and the remaining 40-class count require independent mathematical review. This is not a formal-kernel proof, configured-family/external review or novelty clearance. It does not claim that any of the remaining spectra admit even a cyclic 6D lift.
