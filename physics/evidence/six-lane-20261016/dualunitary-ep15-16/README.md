# Six-lane phys-2: two-qutrit dual-unitary entangling-power optimum 15/16 outside O9

Lane: `physics/evidence/six-lane-20261016/dualunitary-ep15-16/` (owns `sources/ code/ evidence/ review/ archive/`).
Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-dualunitary-ep15-16-contract.json` (recorded 2026-10-17T02:54:44 PDT).
Prior lane `../dualunitary-t7/` and all `institute/.../review/` files are read-only inputs.

## 0. Frozen protocol (written before any search or optimisation run)

Provenance (corrected 2026-10-17 after parent note; no separate freeze receipt was captured when §0 was written).
The only host-clock evidence is the file-system mtime of this README before this provenance edit:
`2026-10-17T03:05:00-07:00`, SHA-256 `7d16a1d39b683869a98b8843c93b9ca59155124a029e0423b6392cfdf50370a7`
(stat/shasum taken just before the edit; §0 text unchanged apart from this provenance note and the fetch-time fix
below). Subsequent mtimes: `code/gates.py` 03:05:17, `evidence/controls_exact.json` 03:05:56,
`evidence/explore_dim.json` 03:07:05, first search output `evidence/search/test_mr.jsonl` 03:07:55 (all -07:00).
An earlier "03:2x" label here was a guess and is withdrawn.

### 0.1 Sources (pinned in `sources/`, SHA-256 in `evidence/SHA256SUMS.txt`)

- Survey arXiv:2508.04777v3 (read-only copy in `institute/.../review/dualunitary-primary-v1/`, SHA bc8ee8fc…5e760b):
  R `⟨ij|U^R|αβ⟩=⟨iα|U|jβ⟩` (layout l.239), Γ `⟨iβ|U^Γ|jα⟩=⟨iα|U|jβ⟩` (l.241), (10) `E(U)=1−Tr(U^RU^R†)²/d⁴`,
  `E(US)=1−Tr(U^ΓU^Γ†)²/d⁴`, `E(S)=1−1/d²`, (11a) `e_p=[E(U)+E(US)−E(S)]/E(S)`; conjecture l.568–572.
- [44] arXiv:2212.06737v2 Theorem 1 and dual normal form (14) (prior lane copy `../dualunitary-t7/sources/`).
- [62] S. A. Rather, PhD thesis IIT Madras 2023, hdl 10603/547745, `sources/rather-thesis-2023/` (file mtimes
  03:01:54–03:02:13 -07:00; fetched
  through a browser proof-of-work page; public CC BY-NC). Ch.3 §3.3.1.2 (PDF `07_chapter3.pdf` p.16–17): T-dual
  family U(θ) eq.(3.36) with `U^{Γ1}=U`, e_p formula (3.37), Schmidt-rank-6 bound 15/16, Conjecture 3.3.2.
- arXiv:1912.12021 (PRL 125, 070501), arXiv:2101.04580 (PRR 3, 043034), arXiv:2205.08842v2 (PRX Quantum 3, 040331).

### 0.2 Conventions (exact; every script re-derives them from matrix entries)

- `|ij⟩ ↔ 3i+j` (first factor most significant); S = SWAP, `S|ij⟩=|ji⟩`.
- P9 := source matrix (C7) as pinned by the prior lane: `P9|ij⟩ = |2i+j, i+j⟩ (mod 3)`.
- U(θ) := thesis (3.36) read from the rendered PDF page (c=cosθ, s=sinθ; rows listed in `code/gates.py`).
  The survey's "dual U_s(θ) with T-dual cousin SU_s(θ)" is identified as `U_s(θ) := S·U(θ)` (so `SU_s(θ)=U(θ)`, the
  thesis "self-dual" partner `U'=SU`, `U'^{R2}=U'`). Both `S·U(θ)` and `U(θ)·S` are checked.
- D = {U ∈ U(9): U^R unitary}, T = {U^Γ unitary}, O9 = {(v1⊗v2)P9(v3⊗v4)}.
- Objective identity used everywhere (to be verified exactly as a control): for U ∈ D,
  `1 − e_p(U) = ‖U^Γ U^Γ† − I‖_F² / 72`. Hence the conjecture ⟺ `‖U^ΓU^Γ†−I‖_F² ≥ 9/2` on D∖O9
  ⟺ `Tr ρ_14² ≥ 1/6` for the four-party state `ψ(a,b,c,d)=U[(c,d),(a,b)]/3` with `ρ_12=ρ_13=I/9`.
- T-dual counterpart: `U ↦ US` maps D onto T (survey/PRR eq. 26d identity `(US)^R = U^Γ S`, checked exactly) and
  preserves e_p (`e_p(U)=e_p(US)`, from `(US)S=U`, checked exactly); it maps O9 onto O9 iff `P9 S ∈ O9` (checked).

### 0.3 Plan and representation (frozen)

1. Exact controls (sympy, algebraic numbers in Q(√3)): P9 → e_p=1; S → 0; identity → 0 (T-dual side); U(θ)
   symbolic → (3.37); U_s(2π/3) → 15/16, dual, not T-dual, not in O9 (rank U^Γ = 6 ≠ 9). Mutations: one entry of
   U_s altered (breaks duality, flagged), objective with E(S) replaced by 1 (normalisation flagged).
2. Local structure (numerical, then exact where feasible): real Jacobian rank of the dual system at random dual
   points and at U_s(2π/3); dimension of D modulo LU; Riemannian gradient/Hessian of e_p on D at U_s(2π/3).
3. Search (floats = candidates only): maximise e_p on D by (a) penalty continuation on the unit sphere of ψ ∈ C^81,
   objective `P14 + μ(P12+P13−2/9)`, μ → large, then (b) Gauss–Newton projection onto D to residual ≤1e−12 and
   projected-gradient polishing on D. Runs converging to O9 (distance-to-O9 proxy: P14 → 1/9) are recorded, not
   counted. Seeds: Haar random, perturbations of U_s(2π/3), of P9-orbit points (radius ≥1), of dual permutations.
4. Proof route (scoped): structural reductions only if each step is a theorem for ALL of D∖O9. Any ansatz-only
   bound is labelled partial. No polynomial inequality over all of D (false on O9).

### 0.4 Stop / claim rules (frozen)

- A float candidate counts only if constraint residual ≤1e−12 and e_p ≥ 15/16 + 1e−6; then attempt exact
  algebraic reconstruction or an interval Newton–Kantorovich existence proof on a verified constant-rank chart,
  plus certified e_p > 15/16. Otherwise it is "numerical evidence", never a counterexample.
- No search miss is evidence of the conjecture beyond "numerical evidence". UNKNOWN ≠ proof.
- Resources: ≤4 CPU processes, ≤8 GiB, checkpoint ≤30 min, chunks ≤3 h. Python: `../depolarizing/env` read-only with
  `-B` (numpy 2.5.4, scipy 1.18.1, sympy 1.14, python-flint 0.9.0); research venv as fallback.

## 1. Status

**CANDIDATE PROOF, NOT PROMOTED (chunk 2, 2026-10-17 PT).** Current frozen text: `review/LEMMA_R_PROOF.r4.md`
(SHA-256 afd392daa38b9b8bccfded8d855bd72c1f1b824ab844a5f4c32c7db28d6659ed, mtime 2026-10-17T05:56:23-0700). It is the
final revision requested by the parent and is never to be edited. r4 applies the 12 editorial findings (E1–E12) of
the complete Claude CLI claude-opus-5-5 review of r3: ACCEPT-WITH-FIXES, with no missing case and no fatal or major
issue. The substantive case analysis is unchanged from r3, and the §W tables are byte-identical to r3's.

What r4 proves: every dual unitary that is not 2-unitary has rank U^Γ ≤ 6, hence e_p ≤ 15/16. For T-dual,
non-2-unitary V = US the corresponding statement is rank V^R ≤ 6 and e_p(V) ≤ 15/16. As a corollary, if correct,
this gives thesis Conjecture 3.3.2, which r3 and r4 quote alongside the survey sentence.

Two gates attain 15/16, and r3 prints both matrices explicitly:
- U_s(2π/3), over Q(√3);
- the Codex normal-form gate H, over Q(√6).
Both are certified by `code/witnesses_exact.py`. Its `--check-doc` mode re-certified the tables printed in r3, and
a mutated copy of r3 was rejected. The r4 tables are byte-identical to r3's (textual comparison).

Fixes applied:
- r2 applied the parent's fixes F1 (Fact K; primary sources `sources/quant-ph-0101003v2.pdf` and
  `sources/quant-ph-9911079v1.pdf`) and F2 (9ρ_14 = MM† = (U^Γ†U^Γ)^T).
- r3 adds the Codex minors: R2 (precise T-dual transfer), R3 (explicit pivot / Rank Lemma) and R4 (explicit
  witnesses).
- r4 adds the editorial fixes E1–E12 of the Claude r3 review.

Version history:
- v1 263f9df9…a6a8 is preserved byte-exact as `review/LEMMA_R_PROOF.v1.md`, together with
  `LEMMA_R_NORMAL_FORM.v1.md` (37fb…) and `REDUCTION.v1.md` (8190…). These are copies of the parent pin
  `…/review/dualunitary-rank-bound-parent-inputs-v1/`.
- `review/LEMMA_R_PROOF.md` holds the interim revision a05e563b…2f7c (parent pin `…-inputs-v2`), left unchanged.
- `review/LEMMA_R_PROOF.r2.md` is r2, c8e62cba…4284, left unchanged.
- `review/LEMMA_R_PROOF.r3.md` is r3, ae42fcbb…90ea, left unchanged.

The parent reports: the Codex review of the interim text was ACCEPT-WITH-FIXES with no fatal or major defect; its
replay of the four exact scripts was byte-identical; the bounded priority audit found no prior proof. No novelty
claim.

Cycle-1 record: `review/REDUCTION.md` (its "fixed index permutation" marginal claim is wrong in general; see r4
§7), `review/LOCAL_THEOREM.md`, `evidence/LOG.md`.

- Controls (exact, `evidence/controls_exact.json`): P9 e_p = 1 (dual, T-dual); SWAP e_p = 0; identity e_p = 0;
  `U_s(2π/3) = S·U(2π/3)` real orthogonal, dual, not T-dual, self-dual, e_p = 15/16, spec(U^ΓU^Γ†) = {3/2^6, 0^3};
  symbolic e_p of U(θ) = thesis (3.37); `(XS)^R = X^Γ S`; P9·S ∈ O9 by local permutations; mutations
  (entry change, non-local rotation, E(S) → 1) detected.
- Rigorous: Theorem A (rank U^Γ ≤ 6 ⇒ e_p ≤ 15/16, equality iff six equal singular values); Corollary A1 (all
  LU-images of self-dual gates); T-dual transfer U ↦ US; Theorem L (near U_s every dual unitary is LU-equivalent
  to a self-dual one, so U_s is a local maximiser of e_p on D; exact certificates `evidence/local_theorem_exact.json`);
  Proposition P (every enphased non-2-unitary dual permutation has e_p ≤ 9/10; `evidence/enphased_perms_exact.json`).
- Lemma R — every U ∈ D∖O9 has rank U^Γ ≤ 6 — was the missing all-gate reduction in cycle 1. The candidate proof
  is now in `review/LEMMA_R_PROOF.r2.md`: max-overlap normal form, qubit Kraus-span Lemma N1, the 2×2×2×2 tensor
  Lemma T, and the case tree S / G / A\* / B\*. The stronger "LU-self-dual" statement fails on a rank-4 stratum
  and is not needed.
- Theorem L replay: `../depolarizing/env/bin/python -B code/replay_theorem_L.py` (pinned manifest
  `evidence/theorem_L_manifest.json`; "local maximiser" defined precisely in `review/LOCAL_THEOREM.md`).
- Numerical evidence (`evidence/search_summary.json`): ≈1,300 projected dual points from diverse seeds; no non-O9
  point with rank U^Γ ≥ 7 (three apparent rank-8 points are unresolved-precision artefacts next to rank-4 dual
  points, e_p ≤ 0.77); ascent maxima exactly 15/16 (main stratum), 5/6 (rank-4), 1 only on O9.
