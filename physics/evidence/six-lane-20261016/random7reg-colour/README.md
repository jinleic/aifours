# Six-lane phys-2 (second target): chromatic number of the random 7-regular graph

Lane: `physics/evidence/six-lane-20261016/random7reg-colour/` (owns `sources/ code/ evidence/ review/ archive/`).
Contract (frozen, read-only): `institute/runs/six-lane-2026-10-16/screening/phys-2-random7reg-colour-contract.json`
(recorded 2026-10-17T06:02:00-07:00). Lane assigned by parent IRC; first captured host time 06:04:34 PDT.

## 0. Frozen protocol

Written before any computation in this lane. Host time when written: the README mtime; the last captured `date`
before writing was 06:14:04 PDT. Only the source reading and the priority searches in §0.5 preceded it.

### 0.1 Target and claim rules
- Target: decide χ(G_{n,7}) for the uniformly random 7-regular graph (n even, n → ∞). Either prove χ = 4 a.a.s.,
  or isolate the exact failing dependency of the route below.
- A proof counts only as a written, self-contained argument. It must state every imported theorem with its exact
  hypotheses and verify them at (k,d) = (4,7). Every numeric inequality must carry exact rational bounds or
  rigorous ball arithmetic (python-flint `arb`, outward-rounded). Floating-point checks are sanity checks only.
- Numerical multistart, a restatement of KPW, or importing KPW (3.15) without proving it at d = 7 is insufficient
  (contract).
- No novelty or priority claim. A search miss is not novelty. Correctness, novelty and significance are kept
  separate.

### 0.2 Route (frozen; from the contract's untrusted lead, every step to be re-proved here)
1. Upper bound χ ≤ 4: KPW (arXiv:0812.2937v1) at k = 4 colours and d = 7.
   - Second moment of the number Y of balanced 4-colourings of the pairing model P_{n,7} (Proposition 2).
   - Small subgraph conditioning: (1.1)–(1.3).
   - The n ≢ 0 (mod 4) extension: §4, Theorem 10.
   - KPW assume d < 2(k−1) log(k−1), which fails at (4,7) since 6 ln 3 ≈ 6.59 < 7. Every use of that hypothesis
     in §§2–4 is to be audited with page and line quotes from the pinned layout text.
   - Planned replacement for KPW (3.15): the sharpened Achlioptas–Naor inequality at k = 4, stated as a per-row
     inequality D(p‖U_4) ≥ (3/2)·ln 3·(Σp_i² − 1/4) for all p ∈ Δ_4. Summed over rows it gives
     φ_d(M) ≤ φ_d(J/4) − ((3/8) ln 3 − d/18)·Σ(m_pq − 1/4)², with a positive constant at d = 7.
2. Lower bound χ ≥ 4: first moment for proper 3-colourings of P_{n,7}, maximised over all class-size vectors.
   The pairing-model statement transfers to simple graphs because P(simple) is bounded away from 0.
3. Cross-check of step 1's inequality through AN's own proof: the hypotheses of Theorem 9 for h = −x log x, then
   eqs. (9)–(12) and the three critical values of η at k = 4.

### 0.3 Representation and reductions (frozen)
- KPW's function (3.8) at k = 4: φ_d(M) = −(1/4)Σ m ln m + (d/2)·ln(1/2 + Σ m²/16) on 4×4 doubly stochastic M,
  natural logarithms. AN's g_c with c = d/2 is the same function.
- Per-row reduction: probability vectors only. The sign of each derivative is settled by exact inequalities on
  ln 3. Two-valued vectors are reduced to by Lagrange multipliers; the boundary is excluded by a descent argument.
- First moment: the exact count of pairings with no monochromatic pair, for each class-size vector.
  - Stirling bounds give a separable exponent Σ_k w(x_k) on {x ∈ Δ_3, x_k ≤ 1/2}.
  - Its maximisers are reduced by KKT to two one-parameter curves.
  - Rigorous one-dimensional ball-arithmetic subdivision is done on those curves only.

### 0.4 Controls and stop rules (frozen)
- Controls:
  - KPW's original threshold arithmetic: at k = 4 they need d < 6 ln 3 = 6.59..., so d = 6 is covered and d = 7
    is not.
  - The sharpened argument must fail at d = 8. Exhibit a doubly stochastic M with φ_8(M) > φ_8(J/4), rigorously
    enclosed; the relaxation threshold (27/4) ln 3 = 7.41... < 8 is also reported.
  - Reproduce χ(G_{n,6}) = 4 (KPW/Shi–Wormald arithmetic) and the first-moment non-3-colourability for d ≥ 6.
  - The same first-moment test must come out positive (inconclusive) at d = 5.
  - Mutation controls on the verifier.
- Stop rule: if a cited step has a hypothesis that genuinely fails at (4,7), or the needed global bound fails at
  an exactly enclosed point, report the refutation of the route. That only stops the route; it does not answer χ.
- Resources: ≤4 CPU processes, ≤8 GiB, host-clock checkpoints ≤30 min, chunks ≤3 h. No /tmp or other out-of-repo
  writes. Python: `../depolarizing/env/bin/python -B` (python-flint 0.9.0, sympy 1.14), read-only.

### 0.5 Sources
- Parent-pinned and read in place, not copied: `institute/runs/six-lane-2026-10-16/review/colour7-parent-source-screen-v1/`
  - KPW arXiv:0812.2937v1: pdf bf56a321…657f, layout c75d6c7d…2afd;
  - AN Annals 162 (2005): pdf b5cc85ac…def7, layout b22f7ba1…0430;
  - Gandolfo–Ruiz–Wouts arXiv:0811.2735v1;
  - and `…-v2/` ACG arXiv:1812.09691v4.
- Lane-fetched for the priority check (SHA-256 in `evidence/SHA256SUMS.txt`): Achlioptas–Moore
  cond-mat/0407278v1, and the Shi–Wormald Waterloo report 2004-24, which is image-only (no text extracted).

## 1. Status

**CANDIDATE PROOF, frozen r2 (r2 itself not yet reviewed).** File: `review/PROOF_CHI7.r2.md`, SHA-256
f157337d864cb122247d5c9ec3c73e2d12efb5786c837404efbeafa1b6afb6a5, mtime 2026-10-17T07:12:31-0700. It is never to be
edited. It supersedes r1 (`review/PROOF_CHI7.r1.md`, SHA-256
8a79ba3c9858137fa698c5f962ac6fe4e1fba38f2b61ce919772893d74ea906c, mtime 2026-10-17T06:25:30-0700), which is kept
unchanged.

Reviews of r1 (parent-held, under `institute/runs/six-lane-2026-10-16/review/`):
- Codex hostile review: ACCEPT-WITH-FIXES, with one minor (induced matching, triangle exclusion, C(14,7)
  uniformity).
- Claude complete review: ACCEPT-WITH-FIXES, no fatal or major finding, minors m1–m7. The parent's addendum shows m1
  was a prompt-numbering artefact.
- Parent priority audit: Achlioptas–Naor display (12) and Nir–Pérez-Giménez arXiv:2109.13347v1 (Theorems 1.2 and
  3.1, random lifts of loopless regular multigraphs) are prior work on the constant. No uniform-model statement was
  found.
r2 applies every fix; its §9 lists them.

Claim: χ(G_{n,7}) = 4 a.a.s.
- Upper bound: KPW's second moment and small subgraph conditioning at k = 4.
  - The audit shows KPW's hypothesis d < 2(k−1) log(k−1) enters §§2–4 only through (H1) k² − 2k − d + 2 > 0 (here
    3) and (H2) the global bound (3.15).
  - (H2) is proved at d = 7 with C_7 = (3/8) ln 3 − 7/18 ∈ (0.023, 0.024), from the per-row inequality
    D(p‖U_4) ≥ (3/2) ln 3·(Σp² − 1/4). That inequality is the k = 4 case of AN's display (12), which is prior work;
    r2 gives an elementary hand proof of it.
  - All n ≡ 2 (mod 4) are covered by KPW Theorem 10, via the induced-matching reduction with exact conditional
    uniformity.
- Lower bound: the published Molloy–Reed criterion is primary. The rigorous first-moment maximisation over all
  3-colour class sizes is a cross-check.

Numerics: `code/verify_rigorous.py` → `evidence/verify_rigorous.json`, using exact rationals and python-flint arb;
all_required_true = true. Not rerun for r2, which changes no computation.

Independent second routes (not needed by r1 or r2): `code/crosscheck.py` → `evidence/crosscheck.json`,
all_ok = true. These are:
- a rigorous arb proof of the family-1 inequality via Taylor neighbourhoods plus subdivision;
- family 2 by convexity;
- brute-force validation of the pairing count;
- exact E Z_3 exponents for n ≤ 320.

Controls: KPW threshold arithmetic; failure at d = 8 (13³² > 2⁵⁶·3³²·5⁵ exactly, at M = (J + I)/2); χ(G_{n,6}) = 4;
first-moment non-3-colourability for d = 6, 7, 8; d = 5 inconclusive; mutation controls.

Priority: two bounded audits found no uniform-model statement. The sharp constant is prior work (AN (12); NPG for
random lifts). No novelty claim; a search miss is not novelty.

Separate exploratory d = 8 work (no claim, no frozen target):
- `review/D8_SCREEN.md`;
- `review/D8_PILOT.md`, with `code/verify_d8_pilot.py` → `evidence/verify_d8_pilot.json` (all_ok = true). The
  pilot recommends GO for a frozen target χ(G_{n,8}) = 4, pending the parent's decision. It also corrects
  D8_SCREEN §3.
