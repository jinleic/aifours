# Addendum 1: manifest v4 — polynomial audit, off-block interval, endpoints

**Native clock observed immediately before exclusive creation:** 2026-10-28T19:09:11-0700 PDT

**Binding manifest:** `manifest-v4.json`, SHA-256 `3f863ecb986c3ed4813f13a33694e6bf3304b41b265577490b98c6ab40d223e2`. This supersedes the manifest-v3 binding label in `review-v1.md`; that file is preserved as written. Its nine input SHA-256s are unchanged in v4, so its per-file findings and independent checks remain applicable to those exact bytes. `review-v1.md` SHA-256 is `430a49319301f477535624b388a94a83117e308bf4677ddb1ed5a70d60a0c377`. In both reviews, `R` means `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4`.

I verified all 16 v4 input SHA-256s, byte counts and LF counts before reading the seven new bodies completely in their manifest order, in exact raw windows. All full `sha256` pins, lengths and LF counts match. New input hashes, in order:

1. `R/frontier-20261028-74-hessian-polynomial-audit-report.md`: `6d4ce6f83845f136fa6af1b7f05a9a9ba6a6da0c680f3bb785fe31ca173900fd`.
2. `R/frontier-20261028-73-hessian-polynomial-audit.py`: `57626c72a11882440c26886b387c718eeb50dccce27a006c7a39ad36701c830e`.
3. `R/frontier-20261028-77-offblock-uniform-noise.md`: `04de53eea1187e9a890f263c954c3e05abe7c1e621817bfea24c811ca23eafb2`.
4. `R/frontier-20261028-75-offblock-constants-check.py`: `985ee8bb41dbc3bcfd7a75645200b8e697f2038dc85b64fc0c244ab2fd86e8d9`.
5. `R/frontier-20261028-76-offblock-numeric-audit.py`: `e86c18787768a2da54d18ceb4e67db139077f747b65f61da8038dbc860020832`.
6. `R/frontier-20261028-79-offblock-endpoint-report.md`: `9f4833a8059868c56cae67c6e401398e48997b50365560929a609eb607218618`.
7. `R/frontier-20261028-78-offblock-endpoint-check.py`: `74767e92a91a2f7dcd8b766a2698665177fffe235122b8dc56de2fb2712864ed`.

## Per-file verdicts

Counts are FATAL / MAJOR / MINOR, conditional on the stated imports; these are reviewer findings, not parent adoption.

| New v4 input | Verdict | Exact qualification |
|---|---|---|
| 74 Hessian polynomial audit report | **0 / 0 / 1** | Its polarization step needs the sesquilinearity/charge-covariance qualification in Finding 1. The coefficient identities themselves were independently reconstructed in `review-v1.md`. |
| 73 Hessian polynomial audit code | **INCONCLUSIVE** for the historical run and helper | Source read and loop counts checked; imported author helper 57 was not opened or executed. Independent coefficient identities do not attest the original run. |
| 77 off-block uniform-noise candidate | **0 / 0 / 0** | At the product gauge and corrected `15t/256` Hessian imported from 59, the stated physical `|1-p|<=9*10^-6` result follows from the written off-block estimates, the same-P bridge and the mirror. |
| 75 off-block exact checker | **INCONCLUSIVE** for the historical run and helper | Source read; imported author 12 helper/chain not executed or audited. Independent exact checks of the displayed bounds are recorded below. |
| 76 floating audit | **INCONCLUSIVE** for the historical run and helper | Source read; imported author 61 helper/chain and the historical floating observations were not replayed. Floating stress tests do not establish a universal theorem. |
| 79 endpoint report | **0 / 0 / 0** | Independently recomputed for the one stated input at the two endpoints, not for all inputs. |
| 78 endpoint checker | **INCONCLUSIVE** for the historical run and helper | Source read; its 66/35 helper chain was not audited. The endpoint claims were independently reproduced using separate code. |

### Finding 1 — MINOR: polarization requires more than quadratic homogeneity

`R/frontier-20261028-74-hessian-polynomial-audit-report.md:20` states that, because both sides are quadratic in the complex normal coordinates and their conjugates, values on `e_i`, `e_i+e_j`, and `e_i+i e_j` determine **all** quadratic coefficients. Quadratic homogeneity alone does not establish this: using the normal basis ordered as in `73:25,34–46`, `F(c)=Im(c_3^2)` vanishes on all 121 tested single/pair directions (and hence at all 32 sampled t values), but `F((1+i)e_3)=2`. It is a real homogeneous quadratic in coordinates and conjugates. The missing property is that the actual second-order leading-block expressions are **sesquilinear** in `c` and `conjugate(c)`, not general complex-coordinate quadratics.

This is repairable from the imported channel's excitation-number covariance: each `Lambda(|x><0|)` changes output weight by `|x|>0`; two such same-sign terms cannot return to a weight-0 or weight-1 leading block, so `c c` and conjugate-`c` conjugate-`c` coefficients vanish. Mixed `c_x conjugate(c_y)` terms vanish unless `|x|=|y|`. Once that property is stated and proved, the chosen `1/i` pair phases do determine the complex sesquilinear coefficients. `review-v1.md` gives an independent all-coefficient exact interpolation argument and thus does not rely on the unsupported general polarization claim. This finding qualifies the written inference, not the actual Hessian identities or the 77 theorem.

For `74:7,11–18`, the direction counts are arithmetically consistent: `11*32=352` basis directions; `(C(6,2)+C(4,2))*2*32=1344` same-weight directions; `(6*4+6+4)*2*32=2176` cross-weight directions; total `3872`. The six gap product has degree at most 24, and after clearing `D` or `D4` the stated difference-degree upper bound 31 is conservative, so 32 distinct exact roots would prove each fixed-direction identity **if** the imported checker did perform the asserted exact comparisons. I did not independently execute or audit that imported helper; the distinct independent proof in the original review instead establishes the same identities from 22 exact roots and degree at most 21 per coefficient.

### Process metadata — MINOR

`manifest-v4.json` supplies full matching authoritative `sha256` pins for all inputs. It corrects v3's shortened `expected` value for input 70, but the `expected` fields for inputs 73, 75, 76 and 78 are now only the correct 10-hex prefixes (`57626c72a1`, `985ee8bb41`, `e86c187877`, `74767e92a9`) while `match` is true. Full-string equality with each `expected` is false; no prefix convention is stated. This is one recurring manifest metadata inconsistency/ambiguity, **not** a mismatch of any full authoritative SHA-256. The v3 process observation remains historical.

## 77: independent off-block and constant reconstruction

For `77:11–30`, `d0-d1=2(1+t)^3>=2`; `d1-d2=2(1+t)^2(1-t)>=2` because `1+t-t^2-t^3>=1` on `[0,1/1000]`. The largest absolute reference eigenvalue is below 5. The Parseval bounds of the first review imply `||V||_F^2 <= 512t^2 <= 8/15625 < (23/1000)^2`. For the actual normalized state `v`, `W0=sum_i (r_i-z_hat)·sigma_i`, so orthogonality of one-site Pauli strings gives `||W0||_F^2=16 sum_i ||r_i-z_hat||^2 <= 256`. The off-block projection is Frobenius-contractive; each Z term is block diagonal, and the X/Y terms give `||off W0||_F^2 <=16 sum_i (r_ix^2+r_iy^2)<=64`. The remaining Pauli weights give `||W-W0||_F^2<=512t^2`; these are universal bounds, not extrapolations from examples.

At `77:30–41`, entrywise division by gaps at least 2 gives `||S1||_F<3/250`. The exact normalization remainder is bounded by `23/1000 + 17/100 = 193/1000 < 1/5`. Using the Frobenius commutator inequality and the off-block projection, independent rational arithmetic gives the upper estimates

- `||Q||_F < 500781/31250 < 17`;
- `||off Q||_F < 250781/31250 < 81/10`;
- `||S2||_F < 41/10`.

For `77:43–56`, the two exponential factors are below 2. The first and second cubic matrix-remainder budgets are, respectively, `15875567/15625000 < 11/10` and `4767/625 < 8`. At `epsilon<=1/100`, the actual and approximate perturbations from `D` are bounded by `9651/5000000` and `193/100000`, both below `1/500=0.002`; hence their leading `1+4` blocks stay separated. The predecessor's rescaled second coefficient is at most `-15/16`, and the Weyl remainder has slack `15/32-3*8/100 = 183/800 > 0`. Scaling back yields the claimed local gap `15t epsilon^2/512`.

For the far case `77:58–62`, `epsilon>1/100` gives `8-L>2/10001`. At the stated endpoint, the exact slack is `2/10001 - 20*(9/1000000) = 9991/500050000 > 0`. The proof of the same-projector far bound, product-overlap union bound, physical negative-shrink mirror, and averaging with one actual P is in `review-v1.md`. Thus 77 depends on those 59 ingredients and does not solve the unrestricted all-p/all-k problem.

I also independently built the actual scaled matrices by tensor matrix units, local Bloch coefficients, and exact Gaussian-rational divided-gap/commutator algebra for two complex normal directions at each of `t=1/1000` and `9/1000000`: all four cases satisfy the `V,W0,off W0,W-W0,S1,Q,off Q,S2` bounds. These checks supplement, but do not replace, the universal argument above.

## 79: two exact endpoint certificates

For `79:5–21`, independent Gaussian-rational construction using all 256 Pauli Kraus strings agrees entrywise with the tensor matrix-unit channel at both signed shrinkages `q=±9/1000000`. In each case, output inertia is `(16,0,0)`; for the two displayed thresholds, the shifted inertias are `(16,0,0)` and `(15,1,0)`. Thus the top-three output sum is below `2343806250043/12500000000000`; the product reference is `3000072000485999999993439/16000000000000000000000000`, and their exact positive difference is `430959999993439/16000000000000000000000000`. The diagonal rank-three projectors on `{0,1,2}` and `{15,14,13}` have the reported common trace `750021000085500053998683749271/4000016000000000000000000000000`. The construction is one near-product input at two endpoints, not a proof of the universal interval by itself.

## Independent evidence and scope

- `review-v4-check.py`, SHA-256 `d00fdad7869759ae83aaed11d6187c251367097f07e2aaadd6647fb6541ff707`, executed with `/opt/homebrew/opt/python@3.14/bin/python3.14 -B`, exit 0; `review-v4-check-receipt.json` SHA-256 `67b661a273901188a7239a327fa614912a9142ad6549b2887f8d9e2385f8db3a`. It loads definitions from the previous independent reviewer script, never author code.
- `review-v4-polarization-check-v2.py`, SHA-256 `aedd2af0e8a8653b2f705cd074d0682366c1446b26644dd7a52f7c49170b3f84`, executed with the same interpreter and `-B`, exit 0; `review-v4-polarization-receipt-v2.json` SHA-256 `8f254b5338d5856c9d0ba46b48c3ed1751d5afd7f67de3af4e3810d801e87b81`. The first, retained `review-v4-polarization-check.py` (SHA-256 `c8e82fd3b2d611a9c3393bf4e6644968c7071249b3d0ba7d2f94f9e663e9b977`) ran the assertions but exited 1 when JSON could not serialize a `Fraction`; v2 only converts that output value to string. No earlier run is represented as a successful receipt.

Unverified imports remain those listed in `review-v1.md`, plus the author 73→57, 75→12, 76→61 and 78→66→35 helper chains; the named helper bytes, original run histories, and any claims not independently reconstructed were not audited. No held, withdrawn, or quarantined body was a premise. This review is same-harness only, not external-family, human, formal, novelty, or parent acceptance.
