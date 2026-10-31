# Independent same-harness review: depolarizing k3 chain and pointwise obstruction

**Native clock observed immediately before exclusive creation:** 2026-10-28T19:04:38-0700 PDT

**Binding manifest:** `manifest-v3.json`, SHA-256 `f98f821f037186179f9723dab2f77f5aec25f6e7ba0fca7461ae56b77c91dc1f`. All nine inputs were hashed first, then read completely in the stated order in exact raw windows. In the citations below, `R` is `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4`.

## Verdicts and process finding

Scientific verdict counts are **FATAL / MAJOR / MINOR**, at the stated imports and quantifiers; these are findings from this reviewer, not parent acceptance.

| Pinned input | Verdict | Dependency/scope |
|---|---|---|
| `R/frontier-20261028-59-uniform-high-noise-k3.md` | **0 / 0 / 0** | Full product-gauge Hessian, two-unitary remainder, far-state and same-P argument reviewed. Corrected weight-2 margin is **15t/256**. Result only for physical `|1-p| <= 10^-33`. |
| `R/frontier-20261028-65-parseval-uniform-noise.md` | **0 / 0 / 0** | Conditional on the 59 product gauge and Hessian identities, reconstructed below. The sharper block estimates and far case support only the stated physical `|1-p| <= 10^-7` interval. |
| `R/frontier-20261028-64-tighter-parseval-check.py` | **INCONCLUSIVE as to the historical author run and imported helper** | Source read; it imports the unreviewed 57 helper. This reviewer separately recomputed the universal identities and scalar constants; that does not attest the author execution. |
| `R/frontier-20261028-67-noise-endpoint-report.md` | **0 / 0 / 0** | The selected state at both endpoints is independently certified below. It is a consistency example, not a proof of the 65 universal statement. |
| `R/frontier-20261028-66-noise-endpoint-check.py` | **INCONCLUSIVE as to the historical author run and imported helper chain** | Source read; its 35 helper and the latter's dependencies were not audited. Independent original-channel and inertia checks reproduce the report. |
| `R/frontier-20261028-69-product-tube-all-parameters.md` | **0 / 0 / 0** | Conditional on the 59 Hessians, independently reconstructed below. The conclusion is the explicit product tube and its closed convex hull, not all states. |
| `R/frontier-20261028-68-product-tube-check.py` | **INCONCLUSIVE as to the historical author run and imported helper** | Source read; 57 helper not audited. The displayed radius and the universal scalar inequalities were recomputed independently. |
| `R/frontier-20261028-71-pointwise-open-region.md` | **0 / 0 / 0** | Separately verified from the direct channel; independent of 59/65/69. This is a pointwise lambda2 obstruction, **not** a k3 or majorization counterexample. |
| `R/frontier-20261028-70-pointwise-parameter-check.py` | **INCONCLUSIVE as to the historical author run and imported helper** | Source read; 12 helper and its dependencies were not audited. The displayed polynomial identities and illustrative points were independently checked. |

**PROCESS MINOR — manifest-v3.json:84–92:** The ninth input's full `sha256` field is `d88862a794dc4174205a14f0ae27b312051c943e835ba1b07cbf50f50b24b589`, and the actual full digest matches it. But its `expected` field contains only `d88862a794dc`, while `match` is `true`. Full-string equality with `expected` is false; that field is a correct 12-hex prefix, but no prefix-comparison rule is stated. This is a manifest metadata inconsistency/ambiguity, **not** a mismatch against the full binding SHA-256 and not a scientific finding. All other `expected` strings equal their full actual digests. Byte sizes and LF counts also match all nine manifest records.

The actual full SHA-256s in read order were:

1. `59-uniform-high-noise-k3.md`: `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`.
2. `65-parseval-uniform-noise.md`: `5d7718e0f9e62c319512012a16f4be25fb66d893f43f2822b365876468c01e88`.
3. `64-tighter-parseval-check.py`: `4f3d72adb52a4249e52913ad8ceeda0a4ffb7a04e6b81f1b9a095cc05e0c3431`.
4. `67-noise-endpoint-report.md`: `5ec374a9644ac3db34e9a5cb345b6f8ba383bb1c7297cf4390409d6b5c6e0bb8`.
5. `66-noise-endpoint-check.py`: `0a9468089b7677c9846db198bc3b8e18abdd744aa68235b998d5302fbcb6efcc`.
6. `69-product-tube-all-parameters.md`: `37304376dc3eeeb40b8753d62198b637693f8770d9ff38b8a6ec1a36b6de575b`.
7. `68-product-tube-check.py`: `822ba8c76557048bcd595345265252acb2e9651b225fa1a086167602cf2d4a67`.
8. `71-pointwise-open-region.md`: `7fa8cb9b80e200732be8f9ca965c8a853d31733653911e1f136ba5ac0177cdb6`.
9. `70-pointwise-parameter-check.py`: `d88862a794dc4174205a14f0ae27b312051c943e835ba1b07cbf50f50b24b589`.

## Independent reconstruction of 59

For `59:19–46`, a maximizing product overlap exists; varying any one local ket in both real tangent directions makes all four weight-one coefficients vanish. Pauli covariance supplies the product gauge. The channel intertwines global excitation-phase rotations; consequently the leading-block quadratic terms contain only `c_x conjugate(c_y)` with equal input weights, so there are no cross-weight, `c c`, or conjugate-`c` conjugate-`c` terms. Ky Fan's variational principle gives `K2(sum M_h) <= sum K2(M_h)`.

I independently formed the full tensor-product channel on matrix units: on a site, a diagonal unit is sent to diagonal probabilities `a,b`, and an off-diagonal unit is multiplied by `t`. For each of all 11 normal basis indices `x,y`, all 17 leading scalar/matrix entries, and 22 exact `t=n/24` values (`n=1,...,22`), my code compares the `c_x conjugate(c_y)` coefficients in (2) against the stated weight-2, 3, 4 formulas, including cross-weight zeros: **45,254 exact comparisons**, all equal. This is more than a numerical fit: after multiplying by the three distinct relevant spectral gaps and `(1-ab)(a^2+b^2)`, each difference is a polynomial in `t` of degree at most 21. The 22 exact distinct zeros prove those coefficient identities on the nondegenerate interval. Excitation-number covariance supplies the missing monomial types. The script does not import the author's checker. This addresses `59:35–46,54–57,77–105`, including conjugations of complex weight-3 amplitudes.

For `59:54–75`, `Gamma=TT†` has trace 2, diagonal `n_i` in `[0,1]`, and `X=sum n_i^2` in `[1,2]`. Thus its centered Frobenius expression is at most `(1-t)^2(X-1)+t^2(4-X) <= 3`; `||Q-I/2||_F=1` for a rank-two projection. Hence `K2(M2) <= -ab u + (sqrt(3)/2)a u < -ab u + (7/8)a u`, and `A2+K2(M2) <= -a u/8`. For `t<=1/4`, `a(1-t^2)/8 >= 15/256`. The weight-3 and weight-4 margins are at least `45/98` and `2047/2048`, respectively, after division by `t`; both exceed `15/256`. Thus the common margin is **15t/256**, not any larger exploratory value.

For `59:107–156`, I checked the block argument rather than assuming a gap inside the four-dimensional block. Its gaps are `2(1+t)^3` and `2(1+t)^2(1-t) >= 3/2`. The Pauli-string norm sum at `t=1/4` is exactly `2145/64 < 34`; the stated `D,V,W,R` bounds follow. Dividing the off-block entries by the gaps makes the first generator anti-Hermitian; the leading blocks of the second coefficient are `16A/t` and `16M/t`. The first cubic commutator budget is at most `8,366,297,736 < 9*10^9`; the stated second is exactly `279,400,000,000 < 10^12`. The second conjugation cancels the remaining second-order off-blocks, and the leading blocks stay separated. Rank-three Weyl perturbation contributes at most three times the operator-norm remainder. Thus the scaled coefficient `-15/16`, radius `10^-15`, and original local gap `15t epsilon^2/512` follow as stated.

For `59:160–171`, the common-projector far estimate can be reconstructed without an imported theorem. The first-weight Pauli term is bounded by the top-three sum of `sum_i r_i n_i·sigma_i`, namely `L=r1+r2+3r3+3r4`. For a pure input, Parseval gives higher-weight squared Pauli norm `15-S`; for rank-three `P` it is at most `48-9=39`. Their Cauchy–Schwarz contribution is at most `t^2 sqrt(39(15-S))`. Also `16R3=3+8t+6t^2-t^4 >= 3+8t+5t^2`. This gives (15), with `sqrt(39(15-S))-5 < 20` because `585 < 625`. The commuting local-projector union bound gives `1-m <= (8-L)/2`; the same actual `P` is used when averaging pure decompositions. The spin-flip/transposition mirror correctly covers the physical negative-shrink side. None of this assumes pointwise domination of individual eigenvalues.

## 65 Parseval and block constants

At `65:17–36`, both normal-direction matrices have squared Frobenius norm 2. Pauli Parseval and the absence of weight-zero/one coefficients in the first yield `||V||_F^2 <= 512t^2`; at `t=1/100` this is `32/625 < 1/16`. Likewise `||W||_F^2 <= 512 < 23^2`. Entrywise division over the block gaps gives `||S1||_F < 1/6`. The exact displayed bound is

`23 + 2(1/4)(1/6) + 12(1/6)^2 = 281/12 < 24`,

and `||S2||_F < 16`. The two independent rational remainder recomputations for `65:38–64` give `4799/108 < 45` and `1909/25 < 77`. At `epsilon=1/500`, the Hessian-to-remainder slack is exactly `15/32 - 231/500 = 27/4000 > 0`; the displayed local gap follows. Both block approximations remain below half the reference gap. In the far case, `8-L > 2/250001 > 1/250000 > 20*10^-7`; one fixed `P` and the mirror complete the stated result. The conditional dependence on 59 is not replaced by the finite checker 64.

## 67 endpoint check

For each signed shrinkage `q=±1/10000000`, my independent Gaussian-rational code constructed the output both from local tensor matrix units and from all 256 Pauli Kraus strings; all 256 matrix entries agree. It certifies output inertia `(16,0,0)`, inertia `(16,0,0)` of `u1 I-sigma`, and inertia `(15,1,0)` of `u2 I-sigma`, where

- `u1 = 390625156249/6250000000000`,
- `u2 = 3125000624997/50000000000000`.

Thus `K3(sigma) < 4687501249993/25000000000000`, while the product reference is `30000008000000599999999999999/160000000000000000000000000000`; the exact difference of reference and certified upper bound is `45399999999999999/160000000000000000000000000000 > 0`. The positive-side projector on indices `{0,1,2}` and its spin-flipped-transpose `{15,14,13}` have the reported exact trace `7500031999996150000066666670861111/40000160000000000000000000000000000`. These are exact independent certifications of `67:5–35`, not an all-input inference.

## 69 product-tube radius and dependencies

For `69:7–56`, the actual Hessian margin over `t in [delta,1-delta]` is at least `delta/16` after division by `t`: weights 2 and 3 give the displayed bounds; for weight 4, `a^2+b^2 >= t >= t^5`, so `1-t^6/(a^2+b^2) >= 1-t >= delta`, stronger than the displayed `delta/2`. The rescaled coefficient is therefore at most `-delta`. The Frobenius-to-operator factor is 4 in dimension 16, justifying `s1=1020/delta` and `s2=2q0/delta`. The `e0` minima bound both exponentials, the perturbation from `D`, and the block-diagonal approximation; `3C2 epsilon <= delta/2` gives the original gap `t delta epsilon^2/32`. A fixed actual projector extends the conclusion to the closed convex hull only as claimed.

At the exact illustrative `delta=1/10`, independent Fraction arithmetic gives:

- `s1=10200`, `q0=3339684510`, `s2=66793690200`;
- `e0=1/267174760800`, `C1=45490470409020`, `C2=182821637144730`;
- `epsilon_delta=1/10969298228683800`.

These agree with `69:60` and are not optimal-radius claims. Neither 69 nor the checks extend the result to all inputs outside the explicitly specified convex hull.

## 71 exact obstruction and two points

For `71:8–43,49–60`, my code independently constructs the original channel entry polynomials. Ten displayed entry identities and six parity-zero identities agree at five distinct exact `q` values; each entry has degree at most four, establishing those identities in `q`. The `w` numerator is separately checked as a polynomial in `z` at nine exact `q` values; its `q` degree is at most six. It is exactly `2abq(2q^2+q-2) z^2`, with all other coefficients zero. The `u` gap is the displayed `q[a^3-b(3a^2+ab+b^2)z^2]/(1+3z^2)`. Since `2q^2+q-2>0` precisely for `q>(sqrt(17)-1)/4` in the physical range, both orthogonal compression diagonals are positive under (1); the cross term vanishes. Min–max therefore gives lambda2 strictly above `a^3b`. The actual rank-three extension is `|u><u|+|w><w|/||w||^2+|1000><1000|`.

Two independent exact evaluations of (3) are:

| `(q,z)` | upper bound on `z^2` | `lambda*=a^3 b` | `u` gap | normalized `w` gap |
|---|---:|---:|---:|---:|
| `(4/5,1/10)` | `729/253` | `729/10000` | `72647/128750` | `6/108665` |
| `(9/10,1/3)` | `6859/1103` | `6859/160000` | `45471/80000` | `741/472000` |

Both chosen `z^2` are strictly below their bounds and both gaps are positive. For each of the four 1:3 bipartitions I independently found a minor `z`; for each of the three representative 2:2 bipartitions I found a minor `z^2`, and a zero row or column gives rank at most 3. Thus their stated Schmidt ranks 2 and 3, respectively, hold for every real `z != 0`, without relying on 54. At `(4/5,1/10)` I additionally certify `lambda1<81/125` and `lambda2,lambda3<73/1000` by exact shifted inertias `(16,0,0)` and `(15,1,0)`, so `K3<397/500 < 8019/10000=R3`, with gap lower bound `79/10000`. This independently supports the illustrative comparison in `71:64` only; it makes no assertion of k3 behavior at the other point or throughout the open region.

## Replay evidence, unverified imports, and limits

Independent reviewer scripts and receipts, all exclusive-created in this directory:

- `review-check.py`, SHA-256 `79311a55a8041c0907ab5b709d7a457a33579019bb2583ceecb1a524687d2975`; `/opt/homebrew/opt/python@3.14/bin/python3.14 -B review-check.py` returned 0. `review-check-receipt.json` SHA-256 `d76d3083ff02cc63b17fe03314fc291ab3a4bb625e53def209dda4ee0433cb5a`.
- `review-point-k3-check.py`, SHA-256 `4cf95620261d3eea8de1ea9c48413e82fafe47dc88ec24937e91c736cbe963a9`; the same interpreter with `-B` returned 0. `review-point-k3-receipt.json` SHA-256 `673b31d111a51e2b8055f708b9585c2b27364c0d13949898e887533c98ade07e`. This second script loads only definitions from the independent first script, not author code.

Named but **unread/unverified as source or historical execution**: `frontier-20261028-57-product-hessian-exact.py` (and its helpers), `frontier-20261028-58-uniform-noise-exact-check.py`, `frontier-20261028-61-perturbation-block-audit.py`, `frontier-20261028-35-entangled-frame-saturation.py` and its helper chain, `frontier-20261028-12-bloch-gap-check.py` and its helper chain, `frontier-20261028-54-original-pointwise-family.md`, and `frontier-20261028-52-original-pointwise-obstruction.md`. Their cited mathematical content was independently reconstructed where used above; their original bytes, runs, provenance, and any other claims were not audited. No held, withdrawn, or quarantined body is a premise.

This is one same-harness scientific review. It is not an independent model-family, external, human, formal-proof, priority, or novelty verification; it does not itself adopt any result or establish unrestricted four-qubit majorization.
