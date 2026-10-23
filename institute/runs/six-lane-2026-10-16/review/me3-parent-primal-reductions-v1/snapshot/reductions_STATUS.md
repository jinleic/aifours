# reductions/ — STATUS (v1)

Written 2026-10-18T03:40:41-0700 (host clock) by `MathPhaseType3.ME3Reductions` for the integration owner
`MathPhaseType3`. Scope: reduction lemmas L1–L6, controls (a)–(e) and the optional (f). **Correctness only; no
novelty, priority or "first" claim.** The D2 global bound I_2 ≥ v_cos is **not** addressed here; it is the integration
owner's part.

## 1. Claims, and what each depends on

"Proved in text" means a complete written proof in `proof/reductions-v1.md` using only the imports listed in its §0.3.
"Certified run X" means the step also uses an exact (sympy) or ball (python-flint arb) computation from run X. Runs
marked "control only" check a step but are not part of its proof.

| Item | Statement (short) | Status |
|---|---|---|
| L1 (1.1, 1.2, Thm L1(a), L1(b), Cor 1.3, Lemma 1.4, normal forms) | Densities are nonnegative e.p. of order ≤ 3 with Re < 0; a dominant real exponent exists; converse realization; SCV invariances | Proved in text. `ctl-a-v1` (a1, a4) is a control only. |
| L2 (2.1–2.4, 2.6) | Closed pointed cone with compact base; ratio form; mixture lemma; min attained on extreme rays; assembly | Proved in text. |
| L2 (2.5) | Padding/inclusion K_E ⊆ K_{E'} | Proved in text. **The outline's "faces" claim is false; counterexample in 2.5.** Only the inclusion is used (parent acknowledged). |
| L3 (3.1–3.5, Thm L3: SCV ≥ Δ3 on real exponents) | Chebyshev zero count; face rays (SCV ≥ 1/2); Hermite–Genocchi rays F_τ; classification | Proved in text. The attainment remark (SCV(F_{x1}) = Δ3) uses L4(3). `ctl-a-v1` (a3) is a control only. |
| L4(1),(2) | 1 + s = P/Q²; SOS 4(P − 5/4 Q²) = 3(τ² − 4τ + 2)² + 8τ², hence Δ3 > 1/4 | Proved in text (hand expansion), plus exact re-check in certified run `ctl-b-v1`. |
| L4(3),(4) | Δ3 = s(x1) with x1 the smallest Laguerre-L3 zero, = (x3 − x2)²/(4x2x3); minimal polynomial 32y³ − 144y² + 135y − 27; 0.2765825307809456 < Δ3 < 0.2765825307809457 | Root isolation, s(x1) < s(x3), remainder identity, resultant and Sturm bracket from **certified run `ctl-b-v1`**. The derivative identity is also proved in text. |
| L5 (5.1–5.5) | D1 cone and extreme rays; closed form; algebraic form; uniform bound 1 + SCV ≥ (1 + Δ3)/(1 + ω²); large-ω bound | Proved in text. The numeric tail constants (0.20141…, 0.33179…) are exact rationals, re-checked in `ctl-c-v2` c4. `ctl-c-v2` c5 is a control only. |
| L5 Thm 5.6 | v_cos is attained (1/4 < ω* < 4) and v_cos < U = 0.2009015635005569588013806824561593216569 | Proved in text **given certified run `ctl-c-v2`** (c3: the ball for U; c4: Δ3 > 0.2765 Sturm and the tail constants). |
| Thm 5.8 (`proof/vcos-lower-bound-v1.md`) | 0.20090156350055 ≤ v_cos < U | **Certified runs `ctl-f-main-v1`** (B&B), **`ctl-f-gradsym-v1`** (exact symbolic check of the B&B code) and `ctl-c-v2` (U); tails by written Lemmas 5.4/5.5. Mutations `ctl-f-mut-L-above-v1` and `ctl-f-mut-tail-v1` are controls. |
| L6 (6.1–6.6) | D2 extreme rays are exactly e^{−t}h_τ with feasible τ ≥ 0; feasible ⟺ φ = ωτ ∈ [0, θ1(r)]; θ1 is C¹, strictly decreasing, 2π → π; moments m_k = k!(1 − Re[cζ^{k+1}]) | Proved in text. The θ1 value table comes from certified run `ctl-e-v1`; `ctl-e-v1` e0 (exact identities), e2–e5 are controls. |
| Cor 7.1 | inf over ME(≤3) = min(v_cos, I_2) = I_2, and I_2 ≤ v_cos; the conjecture ⟺ I_2 ≥ v_cos | Proved in text from the above. Uses Δ3 > 0.2765 > U (`ctl-b-v1`, `ctl-c-v2`). |
| v_cos numerical value | 0.200901563500556958801380678959513327689390751533559694715965 at ω* = 1.03593295508585679…, φ* = 0.33703824238449376…; 1/v_cos = 4.977562058630906… | EXPLORATORY (`ctl-c-v2` c1: Newton at 80 digits, Hessian positive definite). It lies inside the certified [L, U) and inside the contract band [0.20090144, 0.20090185]. |

**Not covered (owned by the integration owner): I_2 ≥ v_cos**, i.e. a lower bound for SCV on the D2 extreme-ray
family (r, ω, φ) with r > 0, ω > 0 and 0 ≤ φ ≤ θ1(r).

## 2. Controls (contract list) — all launcher runs, receipts in `receipts/`

| Control | Run | Script (sha256) | Exit | Result |
|---|---|---|---|---|
| (a) Erlang-3 = 1/3 exact; L1 realization; HG kernels | `ctl-a-v1` | `ctl_a_erlang3_v1.py` (c17bf91f0e5631f9f893291a329a9b997956f0652965834b09f5398ee829cf90) | 0 | 26/26 checks; SCV = 1/3 exactly |
| (b) Δ3 ≥ 12 digits; exact Δ3 > 1/4 | `ctl-b-v1` | `ctl_b_delta3_v1.py` (413b3c4a744d2e2efa5be072d674c46d13f479424690e1d695362517a0c70fff) | 0 | 24/24; Δ3 = 0.276582530780945666463231609882563467003… (bracket 0.2765825307809456 < Δ3 < 0.2765825307809457); 4 mutations rejected |
| (c) v_cos ≥ 12 digits, band, certified U | `ctl-c-v1` | `ctl_c_vcos_v1.py` (0b5639b6a35df2e3a142a7702bd842dc42e4c04ce03a2eabc7137257ed6851ad) | **1** | **FAILED ATTEMPT, kept.** All math checks passed. Mutation M3 used the constant 0.5, which is below the true ω = 4 minimum (~0.547), so it was correctly not violated: a control-design error. |
| (c) same, fixed mutation | `ctl-c-v2` | `ctl_c_vcos_v2.py` (80bd5cf08ab794a8011bd799700d96cb8a070ca0328561f2e832ce5325fdb84a) | 0 | 18/18; v_cos (EXPL.) 0.2009015635005569588013807; in band; U certified; tails; 3 mutations rejected |
| (d) HSTZ eq.(4) convention | `ctl-d-v1` | `ctl_d_hstz_v1.py` (c706339d50ba579028e1568d14882fa78cc34a7f963a72ec6ccaf391db652777) | 0 | 12/12; literal cos² reading SCV = 1.57570699242661019346 (rejected); 1 − cos reading 0.200901563501977; half-frequency cos² identical |
| (e) D2 feasibility/infeasibility | `ctl-e-v1` | `ctl_e_d2feas_v1.py` (8274eb47af13655d28317f8067a7c6db88d3407c092e3aa7968681116b8567b2) | 0 | 24/24; θ1(0.3) = 4.65987805685937520611801336469…; infeasible h(0) = −0.04413 (certified < 0); feasible ray > 0 on the grid; 2 mutations rejected |
| (f) certified v_cos ≥ L | `ctl-f-main-v1` | `ctl_f_d1bnb_v1.py` (508b148870fc18e3cb32de6ada1c5245aca4271db92867b959597b4ba29341b7), argv `0.20090156350055 1/4 4 certify 3000000` | 0 | certified; 38439 boxes, depth ≤ 55, tails OK |
| (f) exact check of the B&B code | `ctl-f-gradsym-v1` | `ctl_f_gradsym_v1.py` (2417f74037567dcf6ff0a1f74c9f5f33c47cebcc64c5c3ab13b03e4dca9994ec) | 0 | grad_ball ≡ ∇F_ball and F_ball + 1 ≡ m0m2/m1² (minimizing sign), symbolic residuals 0 |
| (f) mutation: L above v_cos | `ctl-f-mut-L-above-v1` | same script, argv `0.200901563500557 1/4 4 reject 3000000` | 0 | refuted at a certified center, F = 0.2009015635005569722… < L' (rejected as intended) |
| (f) mutation: weak tail | `ctl-f-mut-tail-v1` | same script, argv `0.2009 1/2 4 reject 3000000` | 0 | tail bound 0.0212 < L (rejected as intended) |

Interpreter (all runs): the read-only venv python 3.14.3, python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0, via
`code/run_v1.sh` (sha256 0cfcb20c797c9194ab4d7ef7541d444aea23c1a38b6f1c63eb2910f9248daf40 at every launch). Every
executed script's sha256 in its pre-receipt equals the current file hash, so nothing was edited after execution.
Maximum RSS was 601 MB (`ctl-c-v2`, numpy grid); every wall time was under 2 s. New data in `reductions/` is about
0.4 MB.

## 3. Outline corrections / obstructions

* **False outline step (recorded; parent acknowledged 2026-10-18):** "lower-order densities embed as faces".
  Counterexample: E = {−1} ⊂ E' = {−1, −2, −3}; x = e^{−t} − e^{−3t} and y = e^{−t} + e^{−3t} lie in K_{E'} and
  x + y = 2e^{−t} ∈ K_E, but x, y ∉ V_E. Only the inclusion K_E ⊆ K_{E'} is true and used (reductions-v1 Lemma 2.5).
* There are no other obstructions. Every other outline step (L1–L6) was re-derived and holds in the precise form of
  reductions-v1.md.

## 4. File hashes (sha256)

| File | sha256 |
|---|---|
| `proof/reductions-v1.md` | ad6c5091da11c6f236e24d7fb0dc389b2ef99045b50141411d62dc748dd45536 |
| `proof/vcos-lower-bound-v1.md` | 01821b4ce4acbf3708fdda7acefb85e04a00773a5a9c36ab3923f9efa16a9e20 |
| `code/lane_guard.py` | 5589b0a75abf43d98c14a4b68a42ef1ea02b10829a5e67ee5fa298176c7ba484 |
| `code/ctl_a_erlang3_v1.py` | c17bf91f0e5631f9f893291a329a9b997956f0652965834b09f5398ee829cf90 |
| `code/ctl_b_delta3_v1.py` | 413b3c4a744d2e2efa5be072d674c46d13f479424690e1d695362517a0c70fff |
| `code/ctl_c_vcos_v1.py` | 0b5639b6a35df2e3a142a7702bd842dc42e4c04ce03a2eabc7137257ed6851ad |
| `code/ctl_c_vcos_v2.py` | 80bd5cf08ab794a8011bd799700d96cb8a070ca0328561f2e832ce5325fdb84a |
| `code/ctl_d_hstz_v1.py` | c706339d50ba579028e1568d14882fa78cc34a7f963a72ec6ccaf391db652777 |
| `code/ctl_e_d2feas_v1.py` | 8274eb47af13655d28317f8067a7c6db88d3407c092e3aa7968681116b8567b2 |
| `code/ctl_f_d1bnb_v1.py` | 508b148870fc18e3cb32de6ada1c5245aca4271db92867b959597b4ba29341b7 |
| `code/ctl_f_gradsym_v1.py` | 2417f74037567dcf6ff0a1f74c9f5f33c47cebcc64c5c3ab13b03e4dca9994ec |
| `runs/ctl-a-v1/ctl_a.json` | 8810114e3a907dafc5a9b7ba79b95ff04d310b0b1a4883915105e647e6a22bee |
| `runs/ctl-b-v1/ctl_b.json` | 13c745e3bd88a9d1eff5dec01b4ef332f5611d2a6e1e7a21e7f1278d67d1e7c8 |
| `runs/ctl-c-v1/ctl_c.json` (failed attempt) | 3d3a5732de8d83153619bfce5e67afa126fe23a22936ca6253c100bc90da1a33 |
| `runs/ctl-c-v2/ctl_c.json` | aaad54801256abd36e1e99254a82bc0a403672dda9c7a70f4124aaf4d4371618 |
| `runs/ctl-d-v1/ctl_d.json` | e9409bde040955882799d2319ef2ad55d9225dca487b4aec989a080ea5e2f5bb |
| `runs/ctl-e-v1/ctl_e.json` | 685ed4196c7f3b4c703607ae975e024ba5c83202276d9f7c47ed27ccf0de86d5 |
| `runs/ctl-f-main-v1/ctl_f.json` | 9a62b9f8e96a03389919e28f037ec8f2a5da53f959dce610982293655f4ea40f |
| `runs/ctl-f-gradsym-v1/ctl_f_gradsym.json` | c15beac679016f07ea8a802c371f98c0069c3cb8fd408048a85e1b7a00c3c774 |
| `runs/ctl-f-mut-L-above-v1/ctl_f.json` | 389dfc4d63b4b12b69e897e7e8dd5d8ce6108c3184c69767dbc04c48cf9f97a9 |
| `runs/ctl-f-mut-tail-v1/ctl_f.json` | 14bb6d5289dab60b8783d7d00bcc6027384b47d3b64d9bb7848def8d385affa3 |

The stdout, stderr_time and receipt hashes are in the post receipts (`receipts/<run>-post.json`). Each post receipt
also pins its pre receipt's sha256.
