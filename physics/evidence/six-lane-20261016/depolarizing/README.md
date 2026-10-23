# Six-lane phys-1: depolarizing-channel quantum-capacity threshold

Lane root: `physics/evidence/six-lane-20261016/depolarizing/` (owns `sources/ code/ evidence/ review/ env/`).
Contract: `institute/runs/six-lane-2026-10-16/contract.json` (lane `phys-1`). Book link: phys-p0591
(《10000个科学难题·物理学卷》 pp. 591–592, "量子信道"; catalog `physics/evidence/physics-hard-20261015/catalog.md` #2).

## 0. Frozen protocol (written 2026-10-16 ~18:45 PT, before any computation)

Channel (total-error convention): `N_p(ρ) = (1−p)ρ + (p/3)(XρX+YρY+ZρZ)`, equivalently
`D_η(ρ) = ηρ + (1−η) tr(ρ) I/2` with `η = 1 − 4p/3`. Threshold `p* = sup{p : Q(N_p) > 0}`.
Per-Pauli convention of 2608.15870 is `p_KG = p/3`.

### Primary-source status (read 2026-10-16; PDFs + text in `sources/`, SHA-256 in `sources/MANIFEST.txt`)

| Source | Claim | Evidence type |
|---|---|---|
| Krohn-Grimberghe, arXiv:2608.15870v2 | explicit 45-qubit rank-two symmetric state A, `I_c > 0` at `p = 48717/250000 = 0.194868` | exact-rational certificate + integer verifier (not peer reviewed) |
| Ahmed–Bhalerao–Lee–Leditzky–Leung–Schaeffer–Smith, arXiv:2609.39747v2 | `p* ≥ 0.2029161` via M→∞ Gaussian limit (thermal attenuator η, N_E = 1/(2η)); rank-two mod-3 Fock code, n ≤ 220, q ≈ 0.4506 | float64 `I_c ≈ 1e-12` on truncated Gaussian channel (D = 320) + asymptotic Theorem 6 (Δ_{M,K} → 0); **no finite M, no rigorous sign** |
| Agarwal et al., arXiv:2605.09138v2 | 0.19397 (n = 45, rank two, symmetric subspace) | floating point |
| Fern–Whaley 2008 | ≈ 0.19128 | Monte Carlo (peer reviewed) |
| hashing | 0.18929 | analytic |
| upper | `p* ≤ 1/4` (antidegradable) | proof |

Newer-source search (arXiv API, 2026-10-17T01:40Z): no paper after 2609.39747 improving either number
(2610.02176 Khanian–Leung–Smith concerns per-use rates of permutation-invariant inputs, not the sign/threshold;
2609.37240 concerns classical capacity). A search miss is not a novelty result.

### Exact targets (frozen)

- **T1 (certified explicit, main deliverable):** explicit M, explicit normalized input ρ on `(C²)^{⊗M}`, exact
  rational `p₀ > 0.194868`, with a *rigorous* enclosure `I_c(ρ, N_{p₀}^{⊗M}) > 0` (full channel → sector →
  truncation → entropy bridge, outward-rounded or exact arithmetic), plus semigroup monotonicity for `p ≤ p₀`
  and `Q ≥ I_c/M`. Delta reported against 0.194868 (certified) and 0.2029161 (claimed, asymptotic).
- **T2 (stretch, discovery):** a code family whose limiting (or finite-M) positivity threshold exceeds
  0.2029161, with the same rigor for the final claim (finite-M certificate preferred; a Gaussian-limit claim
  requires a rigorous Gaussian enclosure *and* an explicit, independently checked Δ_{M,K} bridge).
- Not a deliverable: re-certifying Ahmed et al.'s own state/law at slightly smaller p (labelled
  *certification of prior claim* if ever done), extra digits, or float-only margins.

### Attack protocol and gates

1. Evaluators: (a) Gaussian-limit thermal-attenuator evaluator (Fock, flag truncation by data processing);
   (b) exact finite-M Schur–Weyl sector evaluator using a loss/add (Schwinger) Horner recursion for
   `Φ_N = Σ_s π_s C_{s→N} L_{M→s}` (Ahmed et al. Thm II.9), independently validated against brute-force
   `2^M`-dimensional computation (M ≤ 10) and a separate coefficient-extraction kernel.
2. Controls (required before any certificate): hashing boundary 0.18929 (n = 1, maximally mixed); `p = 1/4`
   must never certify positive; reproduce the Ahmed threshold ≈ 0.2029 in the Gaussian evaluator (positive
   control); KG state A at M = 45 if its artifact is retrievable (positive control at 16239/250000, negative at
   203/3125 per-Pauli); same-state negative certificate slightly above each certified point (mutation/sign control).
3. Headroom gate H-A (finite M): optimize symmetric rank-two codes at M ∈ {45, 100, 200, 400, 800, …} in float64.
   If no M ≤ 4000 exceeds p = 0.1990 within ~3 h compute, downgrade T1 to the best reachable p (only if > 0.1960).
4. Headroom gate H-B (new codes): single-mode generalizations (rank 3, other moduli/residues, complex,
   unstructured) in the Gaussian limit; stop if none beats the reproduced Ahmed threshold by ≥ 1e-4 in p within
   ~6 h; then a strictly bounded two-mode structured probe.
5. Certification: midpoint–radius interval arithmetic (float64 with rigorous rounding-error bounds) or exact
   arithmetic for all sector matrices; eigenvalue enclosure via congruence + Gershgorin with component counting;
   entropy enclosure by monotonicity of `−x log x`; untreated sectors bounded by `I_c ≥ −S(ρ)`.
6. Resources: ≤ 4 CPU workers, ≤ 8 GiB RSS, checkpoints ≤ 30 min, chunks ≤ 3 h. Lane-local env `env/`
   (uv, CPython 3.13.9, numpy 2.5.4, scipy 1.18.1, mpmath 1.3.0, python-flint 0.9.0, torch 2.14.1).

## 1. Current result (status: CANDIDATE — rigorous enclosure; Codex re-review and Claude Opus 5.5 hostile review
## accept-with-fixes (fixes in v3.1/PROOFS_v5); parent independent float reproduction agrees; full same-code replay
## complete for p = 1/5 and p = 201/1000 (220/220 each, §4); parent aggregation/premise controls pending)

**v3 (provenance-bound, code_snapshot_v3, PROOFS_v4):** p = 1/5: `I_c ∈ [1.1373755593e−8, 1.1432769065e−8]` POS;
p = 201/1000: `[−7.708902770e−9, −7.649813449e−9]` NEG (same state); 17/17 discriminating controls;
`evidence/cert/v3/`. The v1 interval below is the historical first run (inside-consistent).

**T1 certificate.** Explicit M = 2000 qubit state `ρ⋆ = ½|φ0⟩⟨φ0| + ½|φ1⟩⟨φ1|`, `φ_i = Σ_k a_i[k]|D^{2000}_k⟩/‖a_i‖`,
`a_0` on `k ≡ 0 (mod 3)`, `a_1` on `k ≡ 1 (mod 3)`, `k ≤ 300`, binary64 amplitudes in
`evidence/cert/witness_g3_M2000_p1_5.json` (file SHA-256 4ced4ed9…7eca; canonical-JSON SHA-256 43117f99…d7991e2).
At `p = 1/5` exactly (`η = 11/15`):
`I_c(ρ⋆, N_{1/5}^{⊗2000}) ∈ [1.1288547919e−8, 1.1436444146e−8]` (`evidence/cert/M2000_p1_5_TOTAL.json`; 220/220
sectors with `p_N ≥ 1e−13`, rest mass ≤ 3.7e−13, max DD relative error 1.2e−26, max truncation weight 1.2e−26,
π-tail ≤ 1e−40; code snapshot `evidence/cert/code_snapshot_M2000_p1_5/`, proofs `review/PROOFS.md`).
Consequence (§0 of PROOFS): `Q(N_p) ≥ 5.64e−12 > 0` for every `0 ≤ p ≤ 1/5`.

| comparison | value | status |
|---|---|---|
| this lane | **0.2 (= 1/5)** | rigorous enclosure (DD + Arb), explicit finite state, pending review |
| 2608.15870 (KG) | 0.194868 | certified (exact rational), M = 45 |
| 2609.39747 (Ahmed et al.) | 0.2029161 | claimed; float Ic ≈ 1e−12, asymptotic M → ∞, no finite witness |

Delta vs matched certified prior art: +0.005132 in p (first certified point ≥ 0.2). Not a new best *claimed*
threshold: it is 0.0029 below 2609.39747's asymptotic float claim.
Cross-checks: independent float64 evaluator `code/finite.py` gives 1.1412e−8 at M = 2000 (inside); brute force
M ≤ 7 (15/15 inside, `evidence/test_cert_small*.log`); KG's published state R reproduced inside both KG certified
intervals (`evidence/controls/kg_state_R_rigorous.json`). Same-state float scan: p = 0.2005 → +1.87e−9,
p = 0.201 → −7.67e−9 (negative certificate at 201/1000 running).
Protocol deviations: KG state A unavailable (Zenodo 403) → used KG's other certified state R; precision upgraded
from float64 interval to double-double with proved error bounds (same certification design).

## 2. Log

(see `evidence/LOG.md` for dated checkpoints)

## 3. Corrections and protocol deviations (appended 2026-10-16 23:4x PDT; frozen §0 text above left as written)

- **§0 table, row 2609.39747 (README line 18):** "float Ic ≈ 1e−12" should read "numerical Ic ≈ 1e−12, precision
  unspecified (no stated precision, error bound or interval artifact located; amplitudes unpublished)". Theorem 6
  of 2609.39747 has an explicit convergence proof (parent audit `review/depolarizing-asymptotic-priority-audit.md`
  in the run directory); the lack of a finite M does not invalidate that convergence-existence argument.
- **Protocol deviation (§0 Controls, "reproduce the Ahmed threshold ≈ 0.2029 in the Gaussian evaluator"):** NOT
  completed. Their amplitudes are not public, and our optimizer did not reproduce positivity at η ≈ 0.7294 (best
  grid/warm-start values ≤ 0 at the float noise floor; `evidence/gauss/assay_lane*.jsonl`). Recorded as an
  unavailable prerequisite / failed positive control, NOT a pass. The finite certificate's own positive controls
  (brute force M ≤ 7, KG state R inside KG's certified intervals, parent independent reproduction) are unaffected.
- **Scope of the T1 claim:** p = 1/5 is an explicit finite realization with a rigorous sign, an upgrade over the
  certified 0.194868; it is neither a new threshold beyond the claimed 0.2029161 nor a new ansatz.
- **Headroom beyond 0.2029161 (float, Gaussian limit):** none found for mod-2/3/4/5/6 rank-2, rank-3 mod-3 and a
  warm-started K = 450 mod-3 code at p = 0.20295 (optimizer-limited negative; multi-mode variants untested).

## 4. Lane state at closeout (2026-10-17 00:4x PDT, host clock)

- **T1 (p = 1/5, M = 2000): CANDIDATE, gates closed on the lane side.** Certified code v3 (`evidence/cert/code_snapshot_v3/`,
  cert.py 81d50d97…, dd.py cbfb39f4…) byte-identical; tooling v3.1 (`code_snapshot_v3_1/`); proofs `review/PROOFS_v5.md`.
  Full same-code replays: p = 1/5 `evidence/cert/v3/p1_5_full_replay_SUMMARY.json` (220/220 equal);
  p = 201/1000 `evidence/cert/v3_1/p201_1000_full_replay_RECEIPT.json` (220/220 equal; exit codes not captured,
  completion inferred from logs; one pre-validation module version not byte-retained — see receipt). Same-code
  replay is not an independent implementation. Promotion is the parent's decision after its own aggregation and
  premise/upper-bound controls.
- **Beyond 0.2029161: NEEDS-NEW-REPRESENTATION (scoped; not a no-go).** Single-mode Gaussian-limit rank-2/3 modular
  codes at η = 0.7294 under the recorded budgets showed no positive signal (`evidence/gauss/assay_lane{A,B}.jsonl`).
  Multi-mode, non-symmetric, concatenated/degenerate constructions and larger budgets are untested.
- No new target self-selected (parent scout is selecting the next physics-1 target).
