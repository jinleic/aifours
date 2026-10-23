# Lane phys-2: unrestricted `((7,3,3))_2` — attack record and switch decision

Six-lane run 2026-10-16 (contract `institute/runs/six-lane-2026-10-16/contract.json`). Lane owner: worker `PhysNonCws`.
Prior dossier (read-only): `physics/phys-quantum-code-construction/`.

**Verdict: OPEN — not solved.** No `((7,3,3))_2` projector and no nonexistence proof. The lane's new non-CWS
mechanism (operator-level Knill–Laflamme partial-trace constraints inside the Anglès Munné–Huber moment SDP) is
valid and genuinely cuts the relaxation, but does **not** exclude `K=3`. FRONTIER state: **NEEDS-NEW-REPRESENTATION**
(degree-4+ moment information). Per parent instruction the slot switches to the frozen replacement
`../matrix-weight-24-0-10/`.

## 1. Frozen target, status, baseline (before the substantive runs)

- **Claim sought.** A rank-3 orthogonal projector `P` on `(C^2)^{⊗7}` with `PEP = c_E P` for every Pauli `E` of
  weight `<= 2` (degenerate codes allowed), or a proof that none exists.
- **Primary status.** Anglès Munné–Huber, *SDP bounds on quantum codes: rational certificates*,
  arXiv:2603.19901v1, Table 1: `2 <= K_max(7,3) <= 3` (pinned `sources/rational-sdp-2603.19901.pdf`, sha256
  `6e8783…53b1`). Searches on 2026-10-16 (arXiv/web; Du–Zhang–Poon–Zeng npj QI 12:13 (2026) on KL coefficients;
  Sun–Cao–Poon–Zeng arXiv:2610.01992v1 (1 Oct 2026, pinned HTML); NumQI `qecc733` page) found **no resolution**.
  A literature miss is not proof of openness.
- **Baselines.** LP+shadow feasible at `K=3`, infeasible at `K=4`; AMH Γ-SDP does not exclude `K=3`; every CWS code
  excluded (Chuang–Cross–Smith–Smolin–Zeng 2009); VarQEC/NumQI numerics find no code.
- **Attack protocol.** (A1) derive constraints *absent* from the AMH relaxation and test them in the same reduced SDP
  with positive/negative controls; (A2) symmetry-adapted non-CWS ansätze; (A3) unrestricted numerics as guidance
  only. Acceptance: explicit exact projector with independent all-Pauli check, or a complete exact obstruction.
  Floating-point SDP/numerics are proposals only.

Exploratory note: the first LP/SDP smoke runs (§3 controls) were executed while the protocol above was being written;
no target conclusion depended on adaptive choices.

## 2. New constraint family (A1) — derivation

For `|S| <= d-1` and `T = S^c`, KL on `S` means `ρ_{RS} = (1/K) I_R ⊗ ω_S` for the purification with a reference `R`.
Schmidt symmetry `(ρ_T ⊗ 1)|Φ> = (1 ⊗ ρ_{RS})|Φ>` gives the operator identity

`(Tr_S P ⊗ 1_S) P = (1_T ⊗ Tr_T P / K) P`, i.e. `K P_T P = 2^{n-2|S|} P_S P`, with `P_U = Σ_{supp E ⊆ U} tr(PE) E`.

In AMH moment form (`Γ_ab = t_a t_b ω(a,b) t_{a+b}/K^3`, `t = tr(PE)`) this is a kernel condition `Γ λ^{(S)} = 0`,
`λ^{(S)}_b = K[supp b ⊆ T] − 2^{n−2|S|}[supp b ⊆ S]`. `|S| = 0` is exactly AMH's projector row-sum constraint;
`|S| = 1, 2` are new for `d = 3` and hold for degenerate codes. In Terwilliger-orbit variables a row `a` with
`wt(a)=i`, `|supp a ∩ S| = m` gives `Σ_{j,t,p} (K N_T − 2^{n−2s} N_S) x^{t,p}_{i,j} = 0` (`code/code_sdp.py`).

## 3. Evidence (all floating point unless stated)

| Item | Result | File |
|---|---|---|
| GST06 block formulas (q=4) vs brute force n=1,2,3 | generalized spectra match exactly | `code/test_terwilliger.py` |
| New constraints on explicit codes | satisfied to `<=2e-13` by Steane, five-qubit⊗|00> (impure), [[6,4,2]]-subcode⊗|0> (K=3,d=2, only s<=1), random K=3 subcode of [[8,3,3]] (s<=2); violated (`0.8–2.4`) by random subspace and perturbed Steane; families `s>=d` violated as expected | `evidence/validate_constraints.json` |
| Independent KL checker | `kl_check.py` (tensor-contraction, no WHT): Steane/[[8,3,3]] distance confirmed; negative controls fail | same |
| Reduced-SDP controls | feasible: ((7,2,3)), ((8,8,3)), ((8,3,3)), impure ((6,2,3)); infeasible: ((7,4,3)) τ*=−4.0e-4, ((8,9,3)) τ*=−3.5e-5 (AMH exclusion reproduced), pure ((6,2,3)) τ*=−4.7e-4 (AMH note (e) reproduced) | `evidence/sdp_suite.json` |
| **Target ((7,3,3))** | AMH: τ*≈−9e-10; AMH+LP+new s=1,2: τ*≈−2.6e-9; pure: τ*≈−3.8e-9 — **feasible within solver tolerance** | same |
| Cut strength | new constraints shrink the region (A4 max 59.9→52.2, A5 min 129.7→149.1, A6 max 163.7→154.4) but not to empty | `evidence/sdp_suite.json`, session logs |
| Pure-code structure | pure region: `S_0 ∈ [−8e-9, 2.7e-8]`, `A_5 = 162`; exact pure-LP algebra gives `A_5 = 315−6A_3−3A_4`, `S_0 = (2A_3+A_4−51)/16`, so `A_5=162 ⇔ S_0 = tr(P Y^{⊗7} P^T Y^{⊗7}) = 0`, i.e. a pure code would be orthogonal to its spin flip. Numerical, **not certified** | same |
| PSL(2,7) (Fano) ansatz | 3-dim irreps have multiplicity **0** in `(C^2)^{⊗7}` (exact character projection: 1:10, 6:12, 7:2, 8:4 copies); invariant codes must lie in the 10-dim trivial component | `evidence/psl27_multiplicities.json` |
| PSL(2,7)-invariant search | 3-dim subspaces of the 10-dim invariant space; see `evidence/psl27_invariant_search.json` (K=2 control must reach ~0: Steane is invariant) | `code/sym_invariant_search.py` |
| Unrestricted numerics | Stiefel BB search finds ((5,2,3)), ((7,2,3)) to `1e-29`; ((7,3,3)): 36 restarts × 5000 iterations (seeds 21–23) best loss `1.0978172060830` reached independently by two seeds, quantiles 1.10/1.24/1.34 — bounded away from 0 (evidence only, no universality) | `evidence/logs/kl_search_733_seed2*.json` |

## 4. Exact obstruction and why the slot switches

Every relaxation built here is convex in moments of degree `<= 3` in `P` and invariant under `S_7`, local Cliffords and
`U(3)` on the logical space; such relaxations reduce to AMH-type orbit data, which the new partial-trace family
tightens but does not empty. Rank-three information enters first at degree 4 (`P^{⊗4} A_4 = 0`, antisymmetrizer on four
copies), and an `n=7` symmetry-reduced degree-4 relaxation needs orbit algebras of Pauli quadruples (~10^5 orbits) —
a new large implementation with no evidence it decides the case. The PSL(2,7) irreducible ansatz is empty and the
remaining symmetric/unrestricted numerics give no candidate. No concrete next mechanism with credible decision value
remains, so per the parent's 2026-10-16 instruction the lane switches to `../matrix-weight-24-0-10/`.

## 5. Reproduction

```sh
cd code && ../env/venv/bin/python test_terwilliger.py && ../env/venv/bin/python validate_constraints.py --with8 \
  && ../env/venv/bin/python run_sdp_suite.py && ../env/venv/bin/python sym_ansatz.py
```

Environment: lane-local `env/venv` (Python 3.13.9, numpy 2.5.4, scipy 1.18.1, cvxpy 1.9.3, clarabel 0.11.1,
sympy 1.14.0). File hashes: `evidence/manifest.json`.

## 6. Claim boundary

No discovery, no novelty claim. The partial-trace identity is an elementary consequence of KL + Schmidt
decomposition; its use as an AMH-SDP constraint was not found in AMH (§3, Remarks 2–5) but priority is **not**
established. All SDP statements are floating-point and uncertified.
