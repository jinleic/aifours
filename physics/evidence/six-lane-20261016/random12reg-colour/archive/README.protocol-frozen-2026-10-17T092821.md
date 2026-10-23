# Six-lane phys-2 (fourth target): chromatic number of the random 12-regular graph

## 0. Frozen protocol

Frozen before any computation for this target. Host clock at lane creation: 2026-10-17 09:27:55 PDT; this README
was written immediately afterwards, and its first mtime is recorded in `evidence/LOG.md`.

### 0.1 Authority and lane separation
- **Contract:** `institute/runs/six-lane-2026-10-16/screening/phys-2-random12reg-colour-contract.json`, SHA-256
  9b33f97f42179c6b15a50cdd3ae3ec907821cf4e9330663a7dadf43a406f15bb, recorded 09:22:28 PDT.
- **Target:** prove that the uniformly random 12-regular graph G_{n,12} has χ = 5 a.a.s., or isolate the exact
  failing dependency of the proposed route.
- **Writable:** only this lane, `physics/evidence/six-lane-20261016/random12reg-colour/`.
- **Read-only prior inputs:**
  - `random8reg-colour/`: the accepted χ8 proof r3 (SHA e7c506d0…187e2d); the GSV, GSVY and CLMS sources;
    `explore/GENERAL_K_LEAD.md`, an untrusted [INFERENCE] lead.
  - `random7reg-colour/sources/`: D–SC 1996, W99, NPG, AM04.
  - Parent-pinned KPW, AN and ACG layouts under `institute/runs/six-lane-2026-10-16/review/`.

### 0.2 Route (fixed before computation)
The χ8 route, re-run concretely at (k, d) = (5, 12).

1. **Framework.** KPW's balanced-colouring second moment plus small subgraph conditioning at (k, d) = (5, 12). Only
   the S_2 estimate changes.
2. **Lemma A at k = 5.** The exact count (3.4) over 25 cells and 200 unordered allowed pairs (K_5 × K_5), bounded at
   finite n by pointwise weak duality, with:
   - an explicit polynomial factor P_12(n) = e^{26}(12n + 1)^{25/2}(6n + 1)^{401/2};
   - empty cells handled.
3. **Proposition B.** Multipliers μ_u = c_0 + (11/12) log m_u, exponent e^{μ_u+μ_v−1}. This gives
   U(M) = −11 log 5 + 6 log(2E(M)), where E(M) = Σ_{allowed} (m_u m_v)^{11/12}, and U(J) = 24 log 2 − 10 log 5.
4. **Theorem C at k = 5.**
   - Row reduction E(f) ≤ Σ_p ((3/2)R_p² + Q_p/2) for every non-negative 5×5 array, proved at k = 5.
   - F_5 = (3/2)S² + Q/2 = 40‖T_{1/4} g‖² on the uniform 5-point space.
   - Hypercontractivity of the resampling chain: D–SC Theorem A.1 gives α = 3/(5 log 4); Theorem 3.5(ii) is used
     with q = 12, plus L² duality.
   - ρ = 1/4 ≤ a = 11^{−5 log 4/12} ⟺ 11⁵ < e¹², proved by exact rationals.
   - κ = (121/18)(a² − 1/16) and C_12 = 6κ/E(J).
5. **KPW audit at (5, 12).** It must cover (H1) = 5, Lemma 9 (2(k−1)² = 32 > 25), the Lemma 6 eigenvalues, the
   Lemma 8 constants, and the S_1 Hessian (exact eigenvalues and determinant).
6. **Small subgraph conditioning.** Series ratio 11/16 and Σλδ² = 8 log(16/5).
7. **Residues.** r = 1, …, 4 with ℓ = 6r and exact multinomial(12r; 12, …, 12)-to-one conditional uniformity; the
   colour-3 step must be checked at k = 5.
8. **Lower bound.** Molloy–Reed, 4(3/4)⁶ = 729/1024 < 1, plus a self-contained weak-duality first moment.

### 0.3 Representation and symmetry
- k = 5 colours. Cells u = (p, q) ∈ [5]² carry the entries of a doubly stochastic overlap matrix M, so Σ m = 5.
- J = (1/5)J_5. The allowed pairs (p ≠ r, q ≠ s) form K_5 × K_5: 400 ordered pairs, 200 unordered.
- The only symmetry used is coordinate-permutation invariance of the row function on Δ_5. It is used only in the
  optional supplementary interval check, through two-value families (x, y, y, y, y) and (x, x, y, y, y).

### 0.4 Acceptance (contract items (1)–(7), verbatim in the contract)
1. Imported theorems with exact hypotheses verified at (5, 12).
2. Lemma A at k = 5 and finite n, with every factorial bound, P(n) and empty cells.
3. The k = 5 row reduction and the analytic row inequality on Δ_5, with log 11 < 12/5 and a > 1/4 proved by exact
   rationals, and all constants exact or arb.
4. The KPW audit at (5, 12).
5. Small subgraph conditioning at (5, 12).
6. Residues r = 1, …, 4 with exact uniformity.
7. χ > 4 a.a.s.

### 0.5 Controls
- General-k code that reproduces the k = 4 constants of the accepted χ8 proof.
- At d = 13 the route's condition fails (e^{12/5} < 12); nothing is claimed at d = 13.
- Float sanity is not evidence.

### 0.6 Stop rules
- A rigorous counterexample to Lemma A, the k = 5 row reduction, the row inequality or Theorem C, or a KPW dependency
  that genuinely needs Lemma 5 outside S_2, means stop and report a refutation of the route only.
- If any required verifier item is not certain, do not freeze.
- The proof is frozen once (r1); corrections go to r2.

### 0.7 Evidence, priority and safety
- Exact rationals, big integers, sympy and python-flint arb only; floats are not evidence.
- Priority and significance are shared with χ8 (same mechanism). No separate novelty claim; a search miss is not
  novelty.
- ≤ 4 CPU processes, ≤ 8 GiB, chunks ≤ 3 h. No /tmp or other out-of-repo writes, no deletion, no external contact.
  Cooperative stopping only: never SIGKILL or `subprocess.run(timeout=...)`.
- Host-clock checkpoints in §1 at most every 30 minutes.

## 1. Status

- 09:27:55 PDT: lane created; protocol frozen. No computation yet.
