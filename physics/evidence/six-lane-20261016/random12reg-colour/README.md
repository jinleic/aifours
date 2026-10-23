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
- 09:29:10–09:29:32 float exploration `explore/explore_k5.py` (not evidence):
  - the minimum row ratio (F(u*) − F)/|r − u*|² is 0.0644, at (0.804, 0.049 × 4);
  - the local coefficient at u* is 0.2497;
  - KPW's relaxed φ_12 appears to be maximised at J over 5×5 doubly stochastic matrices (320 SLSQP starts). No claim
    follows.
- 09:37:06–09:37:34 `code/verify_chi12.py` first full run: all_required_true = true (sections A–G; S is floats).
  The proof r1 is being written next.
- 09:39:10–09:39:37 verifier rerun after adding arb point values of the supplementary slack: all_required_true =
  true. SHAs: `code/verify_chi12.py` aa326a1f…baa1, `evidence/verify_chi12.json` 595b7389…0118.
- 09:44:53 (mtime) **FROZEN r1** `review/PROOF_CHI12.r1.md`, SHA-256
  0b608b0790887d8ade912b6cf5700ab57df3b2ff57ad7936430eafdb7b35d85e, 634 lines. Candidate proof, not yet reviewed.
  Never to be edited; corrections go to r2. The working draft was moved, byte-identical, to `archive/`.
  - Claim: χ(G_{n,12}) = 5 a.a.s. Route: the χ8 route at (5, 12) (Lemma A at k = 5; Theorem C with
    C_12 = 5.8662e−4 from the analytic row inequality, with 11⁵ < e¹² proved exactly; KPW audit at (5, 12);
    small subgraph conditioning; residues r = 1..4; Molloy–Reed 729/1024).
  - Caveat (in r1 §2.1 and §9): in floats, KPW's relaxed φ_12 appears to be maximised at J over 5×5 doubly
    stochastic matrices, so the per-cell constraints are not shown to be needed at (5, 12).
  - Reported to Main. No processes running.
- 09:58–10:05 Parent review results on r1:
  - Codex hostile review `chi12-codex-hostile-review-v1.note.md`: ACCEPT-WITH-FIXES, no fatal or major finding.
    Minor: W99 Theorem 4.1's first conclusion, P(Y > 0) = exp(−Σλ) + o(1), is overstrong under its hypotheses
    (counterexample Y + 1); the colouring application is unaffected.
  - Parent replay of the verifier: byte-identical output, all_required_true = true.
  - The Claude complete review is still running (its output is empty at 10:04:57).
- 10:05 r2 draft prepared at `review/drafts/PROOF_CHI12.r2.DRAFT.md`, NOT frozen. Following the parent's instruction,
  it uses only W99's contiguity conclusion G^{(Y)} ≈ Ĝ in §1 (I3), §5.2, §5.3, §4 A4, §9 and §10; §11 lists the
  changes. No arithmetic changed and the verifier is unchanged. A single r2 will be frozen after the Claude review
  is folded in. No processes running.
- 10:06 Claude complete review `chi12-claude-complete-review-v1.note.md`: ACCEPT-WITH-FIXES, no fatal or major
  finding; minors m1–m6. The parent instructed: freeze ONE r2 = the SSC draft + m1–m5 (m6: no change).
- 10:15:59–10:16:13 new exact verifier `code/verify_chi12_r2.py` (0eca7bc5…6086): all_required_true = true. Sections:
  M1 (Lemma 8's two ε-conditions: 9/50, 2400/17, ε² < 51/40000, d-free); L67 (Lemmas 6 and 7 at k = 5); M4 (the EX_i
  formula against exhaustive enumeration); M3 (finite marked-space statements). `code/verify_chi12.py` is unchanged.
- 10:19:27 (mtime) **FROZEN r2** `review/PROOF_CHI12.r2.md`, SHA-256
  5fee0295e1ec3716b26924920f015d4a2116e63516ac12f6431724ef1d6e1a00, 781 lines. It is r1 plus exactly the changes
  of its §11: the Codex SSC fix (contiguity conclusion only) and Claude m1–m5. Diff `evidence/r1-to-r2.diff`
  (c1f8e1ea…ba56). The draft was moved, byte-identical, to `archive/`. r2 itself has not been reviewed. No processes
  running.
- 10:33:10 (mtime) **FROZEN r3** `review/PROOF_CHI12.r3.md`, SHA-256
  04f5f370f13f84ebf2e0f08ac9421209a07309fc040bd74b05d05e4cfa2c1f39, 801 lines. It is r2 plus exactly the two fixes
  from the Codex delta review of r2 (`chi12-r2-delta-codex-review-v1.note.md`: ACCEPT-WITH-FIXES, no fatal or major
  finding), plus title, status and §11 items 7–8:
  - (I4): the EX_i explanation now counts oriented descriptions and divides by 2i, valid for every i ≥ 1;
  - §5.3, step 1: the claims are qualified by m > 4ℓ.
  Diff `evidence/r2-to-r3.diff` (dd32557b…07b8). No verifier changed. The draft was moved, byte-identical, to
  `archive/`.
