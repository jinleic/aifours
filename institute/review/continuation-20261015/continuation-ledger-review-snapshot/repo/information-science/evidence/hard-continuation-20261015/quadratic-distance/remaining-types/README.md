# Remaining seven residue types — partial progress and precise stopping points

**Outcome: no further residue type is excluded.** The balanced nine-variable NL242 question stays open. The seven types `(2,192), (4,160), (6,112), (6,128), (6,144), (8,120), (8,136)` remain. `(4,128)` was excluded earlier, in `../zero-geometry/`, under a model-reviewed ACCEPT.

This lane adds model-written, exactly audited **new necessary conditions**, one **sub-case exclusion**, and explicit witnesses that mark where each lever stops. Everything is conditional on the same reviewed inputs as `../zero-geometry/PROOF.md`. Nothing here is Lean-verified or peer reviewed, and novelty is unestablished. `PROOF.md` holds the proofs.

## What is proved (PROOF.md)

1. **Partition and dual correlation (lever 1).** `supp hat S ⊔ supp hat R = F_2^8`, with values ±512. Hence `|A_R| = Σp²/16 = 64 + (5d−4z−8c)/16 = 128 + AC_f(s)/4`. For every quadratic `Q` of polar rank `2τ`, the S- and R-correlations with `(−1)^Q` share one `2^{2τ}`-point budget, and each has its own congruence. Applied to `Q = D, J_g, J_h`.
2. **S–R residue coupling (lever 2).** `J1 = [|S| ∈ {12,20}]` satisfies `J1 + E ∈ RM(3,8)`. `J1` carries the same Pfaffian quartic as `E`, and the identity holds for every odd pair, even without the cap. Exact representations: `p = (−1)^E(−3+4·1_L)` on `D=1`, and `S = 4(2D−1) + 8(−1)^{J1+D}(−3+4·1_A)` everywhere.
3. **Coset energy identity (lever 3).** For `K ⊆ rad(B) ∩ D^{-1}(0)` and each K-character: `Σ_u [hat S_u² + 64·hat p_u²] = 2^18` exactly. The single-character projection threshold is `9d − 24c ≤ 2^{12−τ}`. **It can never be violated for (6,112), (6,128), (8,120) or (8,136):** the whole forced `D=1` energy fits in one Fourier slice, so the (4,128) mechanism cannot reach these four types.
4. **(6,144) sub-case.** If the zero set is invariant under `K = rad(B)`, then `c ≥ 12`. The only quadratics vanishing on `D^{-1}(0)` are `0` and `D`, which forces a single character (audited).
5. **(4,160).** `c ≤ 24`, well under the projection threshold of 50. But the K-character of `E` on `D=1` is not forced to be single: 16 of the 29 cubic-kernel words have non-constant K-derivatives, and the quadratics vanishing on `D^{-1}(0)` span 5 dimensions. Only a per-character collision inequality follows.
6. **(2,192) coset lemmas.**
   - `1_Z ∈ RM(3,6)` on `U`.
   - The four coset transforms are 2-variable fiber patterns.
   - No `D=1` restriction `E_c` is affine; at most one `X_c` is.
   - All eight coset functions share one parity pattern `π`.
   - Exact parity-weight tables, e.g. `ℓ_c=0 ⇒ 16` and `ℓ_c=1 ⇒ 42`.
   - At most one coset has `ℓ_c = 0`.
   - **All `ℓ_c, a_c ≡ z/2 (mod 2)`**, and `c ≥ 3`.

## Where the levers stop (explicit, independently checked)

- **Scalar levers**, including the refined lever 1 for `D`, `J_g` and `J_h`. For all seven types, `results/explore.json.gz` holds explicit integer count vectors over the 28 canonical pairs that satisfy every scalar constraint. They are count vectors, not Boolean functions.
- **(2,192) joint coset count relaxation.** This is the conjunction of every coset lemma: per-κ fiber patterns, Walsh–Parseval and mod-3 integrality for `E_c` and `X_c`, Λ ranges, S energy and cross identities, κ=0 bookkeeping and all scalar congruences. It is **satisfiable**. Three witnesses satisfying the full family are verified: `results/rank2-probe-*-aux.json`.
- **Solver statuses** (no claim from UNKNOWN):

  | Run | Constraint families | Status |
  |---|---|---|
  | `explore.py` (full, 600 s) | all | UNKNOWN |
  | `rank2_probe --amod4` (400 s) | base + `a ≡ 0 mod 4` | UNKNOWN |
  | `rank2_probe` base / s-energy / s-cross / both | subsets | SAT in 17–57 s; three of these witnesses also satisfy the full family |
  | `rank2_probe --tag full` (1500 s cap) | all | cancelled after full-family witnesses existed; no output written |

## Reproduce

Python 3.10+ standard library is enough for the independent audit:

```sh
python3 code/audit.py
```

These meaningful corruptions must fail on their exact assertion:

```sh
python3 code/audit.py --corrupt-witness          # 'witness size'
python3 code/audit.py --corrupt-threshold        # 'projection threshold classification'
python3 code/audit.py --corrupt-parity-table     # 'Lemma 6.4 parity-weight table'
python3 code/audit.py --corrupt-coupling         # 'Lemma 2.2 coupling on genuine pair'
python3 -O code/audit.py --corrupt-coupling      # still active under -O
```

`code/final_verify.py` runs the single final pass and writes `result.json` and `seed-bundle.json.gz`. The research producers need z3 (`code/explore.py`, `code/rank2_probe.py --tag …`), and z3 is used only to **find** positive witnesses. The audit imports neither the producers nor z3. It recomputes everything else from scratch:

- structures from truth tables;
- Pfaffian supports;
- restriction ranks in the transposed orientation;
- the thresholds;
- witness arithmetic;
- representations on all 28 pairs;
- exhaustive parity-weight tables by its own DP;
- the joint fiber-pattern identities over all 81/256 patterns;
- identity checks on six genuine cap-32 odd pairs from the pinned corpus.

The pinned input is `inputs/slice-screen.json.gz`, SHA-256 `200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d`.

## FRONTIER

**PARTIAL / NEW-MATHEMATICS-REQUIRED.** Plausible next obligations:

- **(2,192):** use the Boolean realizability of each per-coset spectrum `W_{E_c}`, `W_{X_c}`. These are genuine six-variable cubics, share the cubic part of `1_Z`, and are coupled by `E = A + a0B1 + a1B2 + a0a1C`. Count relaxations are exhausted.
- **(4,160):** force collisions of the coset characters `χ_u`.
- **(6,144):** handle zero sets that are not K-invariant.
- **(6,112), (6,128), (8,120), (8,136):** a global argument other than single-character projection.

Do not rerun the exhausted corpus searches, the DSBF heuristics or the old symmetric SAT. Longer timeouts on the count relaxations are pointless now that explicit witnesses exist.
