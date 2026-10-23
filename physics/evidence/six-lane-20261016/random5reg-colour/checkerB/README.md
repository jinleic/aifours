# checkerB — independent mpmath.iv checker (phys-2 lane)

Author: sub-worker `PhysRandomColour.CheckerB`. All times are host clock (`date`, PDT, 2026-10-17).
Work started 00:13:03; central run 00:29:35–00:29:59; final outer replay 01:15:05–01:31:49;
final mutation runs 01:31:55–01:41:23 (cone00) and 01:41:27–01:50:31 (cone22). Development replays
ran 00:33–01:14 and are superseded (§5). README completed 01:51:09.

## Independence

- **Read:** lane `README.md`: §1 and §2 as of 00:12 (incl. "FROZEN: outer cell certificate scheme" and
  "central box certified by checker A"), plus the 00:44 append about the slice-concavity lemma. The
  01:14:51 and 01:36:35 entries were read only after all checker-B results were final (01:50).
  `sources/diaz2009-3col-preprint.layout.txt` lines 614–1363 (§4, §5, §5.1, Lemmas 5.1–5.6) and
  1670–1966 (§7). The format spec in the task. Inputs `outer/evidence/cone{00,01,02,10,11,12,20,21,22}.json`.
  Producer progress logs `outer/evidence/cone*.log` (tail lines) and `driverA.log` / `driverB.log`, read only
  to see when each tree was final. Directory listings (names only).
- **Not read or imported:** `code/`, `outer/code/`, `archive/`, `outer/archive/`, and checker A's outputs
  (`evidence/cert_ldc3_*`, `outer/evidence/*.check.*`, `outer/evidence/SHA256SUMS`,
  `outer/evidence/mutations/`, `outer/evidence/resources/`). Also not read: `evidence/slice_*` and
  `evidence/indep_slice_check.json`. The only checker-A numbers I saw are the margins quoted in the lane
  README text.
- **Toolchain:** lane venv `.venv/bin/python` = CPython 3.13.9, mpmath 1.3.0 (backend `python`), and the
  standard-library `fractions`. Platform macOS-27.0.1-arm64. `iv.prec = mp.prec = 128` bits. No numpy.

## Files

| file | role |
|---|---|
| `code/cb_common.py` | spectra and weights; Φ checked equal to (7.7) as a polynomial on the grid {0..5}⁴; EDGES and C_u in spec order; (7.2); exact Fraction linear algebra |
| `code/central_iv.py` | central box via (W)(Q)(C); derivations D1–D6 are in the module docstring |
| `code/cells_iv.py` | outer-tree replay: exact rational bisection, iv D-leaf bound |
| `code/mutants_iv.py` | mutation controls applied in memory (no mutated tree files are written) |

## Commands (run from `checkerB/`, one process at a time)

```
../.venv/bin/python code/central_iv.py --nc 8 --out evidence/central_iv_r0_1e-4_eps3_20_NC8.json
../.venv/bin/python code/central_iv.py --nc 4 --eps 0/1 --out evidence/central_iv_negctl_eps0_NC4.json
../.venv/bin/python code/cells_iv.py ../outer/evidence/cone{00,01,02,10,11,12,20,21,22}.json --out evidence/cells_iv_all9_final.json
../.venv/bin/python code/mutants_iv.py ../outer/evidence/cone00.json --baseline evidence/cells_iv_all9_final.json --out evidence/mutants_cone00_final.json
../.venv/bin/python code/mutants_iv.py ../outer/evidence/cone22.json --baseline evidence/cells_iv_all9_final.json --out evidence/mutants_cone22_final.json
```

Each run was wrapped in `/usr/bin/time -l`; the output is in the matching `evidence/*.time` file.

## 1. Central box: PASS

Claim: ln F(n) < L* = (5/2) ln 5 + ln(25/24) whenever 0 < max_k |n_k − 1/9| ≤ 1/10000.
Route: (W)(Q)(C) with eps = 3/20. Every object below was re-derived and computed here.

**Exact objects.**
- B is the Hadamard basis (row, column and product contrasts), with BᵀB = 4I.
- W2 = Σ w_s s sᵀ has eigenvalue 5625 on **1** and 825, 825, 1145 on B.
- X0 = diag(152/55, 152/55, 1768/1145).
- Xmin = diag(1520/607, 1520/607, 17680/12113).
- R(0) = B X0⁻¹ Bᵀ. Row 0 is (46065/33592, −1145/1768, −1145/1768, −2555/33592), and every row sums to 0.
- Y = −(45/4) G⁻¹ Σ_u C_uᵀ**1** a_uᵀ has entries in {0, ±75582/17915}.
- The c-box half-widths are γ = (113373/44787500, 113373/44787500, 340119/89575000).

**Exact identities checked.**
- Ū(0) = L*: both sides have coefficients (−3, −1, 9/2) on (ln 2, ln 3, ln 5).
- Σ_u a_u = 0 and Σ_u l_u = 0.
- R̄ = R(0) + eps(I − J/4) = B Xmin⁻¹ Bᵀ.

**(Q): 512 c-sub-boxes, 0 failed.**
- Method: parametric Krawczyk in φ = log μ coordinates (radii ≤ 1.6e-4, 1.6e-4, 3.0e-4; contraction ≤ 0.0222).
  Then the Loewner sandwich N ⪯ Σ_s q_s^hi s sᵀ and m̂ ≥ m̂_lo, followed by Gershgorin.
- Margin: min rigorous lower bound of λ_min(X − Xmin) is **0.070803368**. Min leading minor: 0.004401106.

**(C): exact rational Sylvester test at the 16 vertices of B0.**
- Hess Ū ⪯ −δI on B0, with **δ = 1176209/10⁶**. Numerically, max λ_max = −1.17621098.
- Hess Ū(0) has eigenvalues −10.877, −3.626, −3.626, −1.2085.

**Conclusion.** ln F(n) ≤ L* − (δ/2)|η|₂² < L* on B0 \ {n*}, where η = n − n*.

**Resources.** Runtime 24.1 s (Q part 24.0 s); peak RSS 29.5 MiB.

**Negative control.** eps = 0 with NC = 4: (Q) fails in 64 of 64 sub-boxes, so the result is FAIL
(exit 1), as it should be.

**Checker A (README text only).** A reports a (Q) margin ≥ 0.02922 and a (C) margin ≥ 1.1651. B gets 0.0708 and
1.176209 using a different basis and a different enclosure method.

## 2. Outer trees: 9/9 PASS, all 9 facets covered

Source: `evidence/cells_iv_all9_final.json`. The margin column is the rigorous lower bound of
L* − max_v U_y(v) over all D leaves, rounded down.

| tree | sha256 | result | nodes | S | D | C | failed | min margin | s |
|---|---|---|---|---|---|---|---|---|---|
| cone00 | `5b194f11…f7412a` | PASS | 67079 | 33539 | 33032 | 508 | 0 | 1.727268e-11 | 113.1 |
| cone01 | `f563df24…1742b0` | PASS | 67079 | 33539 | 33032 | 508 | 0 | 1.727195e-11 | 113.7 |
| cone02 | `56630444…026ce7` | PASS | 64863 | 32431 | 31946 | 486 | 0 | 1.727402e-11 | 110.1 |
| cone10 | `4d5a4de9…7f34a8` | PASS | 67075 | 33537 | 33030 | 508 | 0 | 1.727073e-11 | 113.4 |
| cone11 | `1c3e5152…025f68` | PASS | 67079 | 33539 | 33032 | 508 | 0 | 1.727218e-11 | 113.7 |
| cone12 | `6254f54c…185f3c4a` | PASS | 64867 | 32433 | 31948 | 486 | 0 | 1.727407e-11 | 109.6 |
| cone20 | `9341ce75…dd0cb0cf2` | PASS | 64863 | 32431 | 31946 | 486 | 0 | 1.727271e-11 | 110.0 |
| cone21 | `0fcb54bc…c4b9ee` | PASS | 64867 | 32433 | 31948 | 486 | 0 | 1.727289e-11 | 109.8 |
| cone22 | `d4ffe5b6…e3d9e` | PASS | 64555 | 32277 | 31638 | 640 | 0 | 6.221281e-11 | 108.9 |

- **Totals:** 592327 nodes; 291552 D leaves; 4616 C leaves; 0 invalid; 0 structure errors.
- **Overall minimum margin:** ≥ 1.727073e-11, in cone10.
- **Resources:** 1004 s total; peak RSS 552 MiB.
- **Trusted radius:** every tree has `r0` = 1/10000, which matches the trusted constant exactly.
- **Max over S:** the 8 candidate spectra are verified in code to be exactly the vertex set of conv(S).
  Each of the 36 spectra has an exact convex-combination certificate in the candidates, and each
  candidate has an exposing integer functional. Both are listed in the output JSON.

## 3. Mutation controls (in memory)

All runs use the final `cells_iv.py`. Every mutation was rejected; none was harmless.

| mutation (in memory) | cone00 (`mutants_cone00_final.json`) | cone22 (`mutants_cone22_final.json`) |
|---|---|---|
| `y_min`: at the min-margin D leaf, largest \|y_e\| ×1.1 | REJECTED: 1 leaf fails, margin −1.386e-5 | REJECTED: 1 leaf fails, margin −2.772e-5 |
| `y_first`: at the first D leaf, largest \|y_e\| ×1.1 | REJECTED: margin −2.444e-3 | REJECTED: margin −2.444e-3 |
| `mu_far`: mu0^u of the class with largest min-vertex n^u (u = 2) → (2¹⁰, 2⁻¹⁰, 2⁻¹⁰, 2¹⁰) | REJECTED: margin −11.49 | REJECTED: margin −11.49 |
| `lstar`: L* → L* − 1/50 | REJECTED: 32888 of 33032 D leaves fail | REJECTED: 31494 of 31638 D leaves fail |
| `del`: delete a 3-node subtree (cone00 nodes 33535–33537; cone22 32280–32282) | REJECTED: structure error "tree truncated", plus 16517 failing leaves | REJECTED: "tree truncated", plus 15814 failing leaves |
| `r0`: tree `r0` changed to `1/20000` | REJECTED: differs from the trusted constant 1/10000 | REJECTED: same |

Why each control behaves as it does:
- **y perturbations:** weak duality holds for every y, so a perturbed leaf that still passed would remain a valid
  certificate. Here the producer's multipliers are close to optimal for their cells, so a 10% change breaks
  the leaf bound.
- **mu_far:** a_u is still a valid upper bound for any mu0 > 0, but it is very loose at a far supergradient point.
- **lstar:** the 144 surviving leaves in each tree are cells with margin > 0.02.
- **del:** deleting a subtree desynchronises the preorder, so later cells are mis-assigned
  (for example, a C leaf lands outside the box) and the node list runs out.
- **r0:** a smaller r0 would still be sound, because the C cells would sit inside the certified box. It is
  rejected anyway because the parent required exact equality with the trusted constant (message received
  about 01:14, before the final runs).

## 4. Not re-proved here (inputs to both checkers)

- **Concavity of ψ on conv(S).** This is the README §2 slice-concavity lemma, in its weak form on the closed slice.
  - Central box (D4): it identifies the interior stationary point as the maximiser. The local strictness
    (X ⪰ Xmin ≻ 0) is verified here.
  - Outer cells: it is used in frozen rule 1.
- **Cover of Δ by the 9 root cones.** The argument is in the `cells_iv.py` docstring (n* is interior;
  Birkhoff–von Neumann). The checker verifies exactly that each root simplex has its 4 facet points on
  n^{u0} = 0 and is non-degenerate. It also verifies that the 9 trees cover the 9 distinct facets.
- **Not in scope:** the bridge from H1.1 to Lemmas 5.6–5.10 and §6 of the paper.

## 5. sha256

| file | sha256 |
|---|---|
| `code/cb_common.py` | `9d3ad5abb52c3ac9ad1bc1027ae9618040d01b3f7e6266f48651ca91ba183726` |
| `code/central_iv.py` | `cca710e9efeeb98358ae4407457505856927b10210d7d884a9a350f1bc99f9e0` |
| `code/cells_iv.py` (final) | `ea8aca331111d764441d505ced5132b01173e251348f69dca4b42fa5364c7c3b` |
| `code/mutants_iv.py` (final) | `9859b3d522476cdcbfd48c9b0033c2a1ce8e81f19a90a1bcb25c957fa1c8144b` |
| `evidence/central_iv_r0_1e-4_eps3_20_NC8.json` | `ef0de716e6e8700734d08c76433c6c0b3b84ece4f9b7a957a092287b8a57d598` |
| `evidence/central_iv_negctl_eps0_NC4.json` | `3c87321580bc771f57659d66950ba32c9de08bfc40e682ca58675835efa8ecc8` |
| `evidence/cells_iv_all9_final.json` | `ec4f8fe99a015b4fa15b0955e2c5a516d054cb28184b0ba66b0e6714a137449b` |
| `evidence/mutants_cone00_final.json` | `9a23b6c1f9d32f570f227712d8466a0544ca12ca4f572793f873f32c11e22dec` |
| `evidence/mutants_cone22_final.json` | `5cf72175b54c149ff162a7dd72ef3dc318039924edd7ebffc6feb24846a1a5d5` |
| input `README.md` (lane; 00:57 version, after the 00:44 append) | `ba56618ac2e9831ec2a047360cb9c7b00bc5c1be13b53246be6ec220b1df39df` |
| input `README.md` (lane; 01:50:35 version, frozen sections unchanged) | `30d3738d0a3020fac8bec808beae9a1a68e7fa8bdf142d59c03f4a12f4daf20c` |
| input `sources/diaz2009-3col-preprint.layout.txt` | `da12c0eecb7773b6b148861512e1cbb1507d72e074ca6e409d18502e0c7639ea` |
| input `outer/evidence/cone00.json` | `5b194f11353b8a8bb5cf424569240822ae60658a35349278b8a023933ef7412a` |
| input `outer/evidence/cone01.json` | `f563df242403c0c070c554d279800fd296b5261f4b8b26d45ea3489ac41742b0` |
| input `outer/evidence/cone02.json` | `56630444b20f26c9959115942519d2af7af0663555ae6418282734704c026ce7` |
| input `outer/evidence/cone10.json` | `4d5a4de90ec05c031d38190cd03e84df85ddf91f1fe80ab351d10173a37f34a8` |
| input `outer/evidence/cone11.json` | `1c3e515254d7f07c9c53cf0aa585f61f1ea717bce8b5610bc7ad508c59025f68` |
| input `outer/evidence/cone12.json` | `6254f54cda9ab535c527077c975e3883e48a4657a9bfe93274329c86185f3c4a` |
| input `outer/evidence/cone20.json` | `9341ce75bc7de9a8704b3eeaf0d5e1df794642acaa3a1fe5bd7e003dd0cb0cf2` |
| input `outer/evidence/cone21.json` | `0fcb54bccc04849f4c30339ab993fa03ccb746ed00e2a08366738d5fbdc4b9ee` |
| input `outer/evidence/cone22.json` | `d4ffe5b672625e453f2777d27d2ae453ffcf66b4234f6831f7cc9b72697e3d9e` |

**Superseded development outputs (kept, not deleted).** These came from earlier `cells_iv.py` versions;
the D-leaf code was identical and the margins match the final run:
- `evidence/cells_iv_cone00.json` (`cells_iv.py` 7dea1750…, before the memory-bounding change).
- `evidence/cells_iv_batch1.json` and `evidence/cells_iv_batch2.json` (017cb559…, which accepted tree r0 ≤ 1/10000).
- `evidence/mutants_cone00.json` and `evidence/mutants_cone22.json` (017cb559…).
