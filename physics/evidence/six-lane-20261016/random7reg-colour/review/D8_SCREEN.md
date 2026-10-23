# Exploratory screen: can the balanced 4-colouring second moment reach d = 8? (draft, no claims)

Status: EXPLORATORY. No target frozen, no claim. Numbers marked (N) are floating-point evidence only. Host-clock
start 06:32:25 PDT, bounded at 90 minutes by the parent. Lane-local code: `code/explore_exact_exponent.py` and
`code/explore_d8_followup.py`, both single-threaded with finite loops and no subprocess.

## 1. The exact exponent, and what KPW's Lemma 5 relaxes

Notation: k = 4, J = (1/4)·all-ones, and M a 4×4 doubly stochastic matrix with entries m_v, v = (p,q). Edges
e = {(p,q),(r,s)} join cells with p ≠ r and q ≠ s; this is the graph K_4 × K_4 (tensor product), with
adjacency A = (J_4 − I_4) ⊗ (J_4 − I_4).

**Exact count** (KPW (3.4), p.11 l.630–636, before any estimate):
|T(M)| = n! · Π_{p,q} (d m_pq n/k)!/(m_pq n/k)! · Σ_{B(M,n)} Π_{unordered e} 1/b_e!,
where B(M,n) is the set of symmetric non-negative integer arrays b with Σ_{e ∋ (p,q)} b_e = d m_pq n/k for every
cell (KPW (3.2)–(3.3)).

**Exact exponent.** Put b_e = ℓ_e n/k and apply Stirling. All n log n terms and constants cancel; the computation is
in §1.1. This gives, uniformly up to poly(n) factors,

  (1/n) log(|T(M)|/|P_{n,d}|) → Ψ_d(M) := (1 − d/2) log k + (d/2) log d + ((d−1)/k) Σ_v m_v log m_v
                                           − (1/k) min_{ℓ ∈ L(M)} Σ_e ℓ_e log ℓ_e,

with L(M) := {ℓ ≥ 0 on edges : Σ_{e ∋ v} ℓ_e = d m_v for all 16 cells v} (KPW's L(M), (3.16), p.17 l.1035–1040).
For the upper bound this is rigorous for every M, since the sum over B(M,n) has O(n^{k⁴}) terms. It matches KPW
(3.9)–(3.11) at J: Ψ_d(J) = (2 − d) log k + d log(k − 1) = 2(log k + (d/2) log(1 − 1/k)), the exponent of (EY)².

**What Lemma 5 relaxes** (KPW p.13 l.713–723; proof pp.17–19 l.1035–1138).
- KPW maximise ψ(L) = Π_v m_v^{d m_v}/Π_e ℓ_e^{ℓ_e} over L(M). On L(M), ψ coincides with
  ψ̂(L) = Π_e (m_u m_v/ℓ_e)^{ℓ_e}.
- They then maximise ψ̂ over the larger polytope L̂ ⊃ L(M), which keeps only the single summed constraint
  Σ_e ℓ_e = dk/2 ((3.18)) and drops the 16 per-cell constraints (3.16).
- The relaxed maximiser is ℓ_e ∝ m_u m_v. This gives exactly ln k + φ_d(M), KPW (3.8)–(3.9).
- It lies in L(M) iff m_v(k − 2 + m_v) ∝ m_v on the support, i.e. iff all non-zero entries of M are equal. This
  holds at J and at scaled permutation matrices, but not at M_t = (1−t)J + tI for 0 < |t| < 1.
- So Ψ_d ≤ ln k + φ_d, with equality at J. The gap is what can rescue d = 8.

**Dual form (used for computation and certification).** The inner problem is an entropy problem with linear
constraints, so its optimiser is ℓ_e = x_u x_v. Strong duality gives
  min_{L(M)} Σ ℓ log ℓ = max_λ [Σ_v c_v λ_v − Σ_{e=uv} e^{λ_u+λ_v}] + Σ_v c_v/2,   c_v := d m_v,
hence
  Ψ_d(M) = min_λ U_λ(M),   U_λ(M) := C_d + ((d−1)/4) Σ m log m − (d/4) Σ_v m_v λ_v + (1/4) Σ_{e=uv} e^{λ_u+λ_v},
with C_d = (1 − d/2) log 4 + (d/2) log d − d/2.
- **Weak duality:** Ψ_d(M) ≤ U_λ(M) for every λ ∈ R^16 and every M. U_λ is convex in M and closed-form.
- Envelope gradient: ∂Ψ/∂m_v = ((d−1)/4)(log m_v + 1) − (d/4)λ*_v(M).
- At J the local exponent is Ψ_d(J) − ((k²−2k−d+2)/(2(k²−2k+2)))·‖M − J‖², i.e. coefficient −(10 − d)/20 at
  k = 4. This is KPW (3.11) with Lemma 7(c). The Hessian is negative definite for d ≤ 9 and degenerate at d = 10.
  The second-moment ratio stays finite for d ≤ 9 ((d−1)/9 < 1).

### 1.1 Stirling bookkeeping

- log n! = n log n − n + O(log n).
- Σ_v log[(c_v n/k)!/(m_v n/k)!] = n[d log d + (d−1) log(n/k) − (d−1)] + (n(d−1)/k) Σ m log m + O(log n), using Σ_v m_v = k.
- log Σ_B Π 1/b_e! = −(n/k) min Σ ℓ log ℓ − (dn/2) log(n/k) + dn/2 + O(log n), using Σ_e ℓ_e = dk/2.
- log |P_{n,d}| = (dn/2) log(dn) − dn/2 + O(log n).

Summing: the n log n terms cancel (1 + (d−1) − d/2 − d/2 = 0), the linear terms cancel, and what is left is Ψ_d.

## 2. Numerics: exact exponent versus KPW's relaxed φ (N, floats; `evidence/explore_exact_exponent.json`)

**Checks.**
- Ψ_d(J) matches the closed form, with error ≤ 1e−15.
- The numerical Hessian coefficient at J is −0.15000, −0.10000 and −0.05000 for d = 7, 8, 9, which is exactly
  KPW's local coefficient −(10 − d)/20.
- Ψ_d ≤ ln 4 + φ_d at 900 random points.

**At M = (J + I)/2:**

| d | Ψ_d(M) − Ψ_d(J) (exact) | ln4 + φ_d(M) − Ψ_d(J) (relaxed) |
|---|---|---|
| 7 | −0.0644 | −0.0326 |
| 8 | −0.0290 | +0.0074 (the r1 control) |
| 9 | +0.0065 | +0.0474 |

**One-parameter families (1 − t)J + tP.** The table gives the minimum normalised margin
(Ψ(J) − Ψ(M))/‖M − J‖²; negative means the centre loses.

| P | d = 7 | d = 8 | d = 9 | d = 10 |
|---|---|---|---|---|
| I (M_t) | 0.0821 | **0.0350** | −0.0121 (max excess +0.0186 at t ≈ 0.755) | −0.0592 |
| 1 ⊕ J_3/3 | 0.1255 | 0.0776 | 0.0295 | −0.0187 |
| I_2 ⊕ J_2/2 | 0.1113 | 0.0637 | 0.0161 | −0.0316 |
| J_2/2 ⊕ J_2/2 | 0.1500 | 0.1000 | 0.0500 | 0.0000 |

**Multistart over B_4** (SLSQP with analytic envelope gradient, 160 starts per d; mixed Sinkhorn-random,
near-vertex, and Birkhoff-mixture starts):
- d = 8: all 160 runs end at J, so no non-centre local maximum was found.
- d = 9: 125 of 160 runs end at a non-centre maximum with Ψ_9 − Ψ_9(J) = +0.01864. Its shape is diagonal 0.8156
  and off-diagonal 0.0615, up to permutation, i.e. on M_t.

**Global normalised margin at d = 8** (`evidence/explore_d8_followup.json`, F1). The minimum over B_4 of
(Ψ_8(J) − Ψ_8(M))/‖M − J‖² is 0.035008, attained at M_{2/3}: rows (3/4, 1/12, 1/12, 1/12) on a permutation, which
is the same configuration as the equality case of the k = 4 AN row inequality. The absolute margin there is 0.0467.

**Rigorous point enclosures** (`code/d9_failure_enclosure.py` → `evidence/d9_failure_enclosure.json`; arb plus an
exact rational primal-feasible ℓ for the lower bound and a rational dual for the upper bound):
- Ψ_9(M_{3/4}) − Ψ_9(J) ∈ 0.0186292384986560592641 ± 1e−20, which is **> 0**. So the plain balanced second moment
  cannot reach d = 9: |T(M)| near M_{3/4} is exponentially larger than (EY)².
- Ψ_8(M_{3/4}) − Ψ_8(J) = −0.0609659 and Ψ_8(M_{2/3}) − Ψ_8(J) = −0.0466773 (both < 0, rigorous at these points).

## 3. Closed-form dual bounds: removing the inner optimisation (N)

Weak duality with λ_v = α + g(m_v), with α optimised in closed form, gives for every function g and every M:
  Ψ_d(M) ≤ B_g(M) := C_d − (d/2) ln(4d) + d/2 + Σ_v [((d−1)/4) m_v ln m_v − (d/4) m_v g(m_v)] + (d/2) ln(YᵀAY),
where Y_v = e^{g(m_v)}. Moreover B_g(J) = Ψ_d(J), and g = ln m recovers KPW's relaxation.
(`code/explore_d8_dualfamilies.py`, `explore_d8_tune.py`, `explore_d8_rowrelax.py`, `explore_d8_separable.py`.)

- g = β ln m, β ∈ [0, 1]: fails at d = 8 for every β. β = 1 gives worst +0.0081, which is KPW.
- g = β ln m + γ m with (β, γ) ≈ (1.3263, −1.4526), Nelder–Mead tuned: B_g ≤ B_g(J) on B_4 with minimum normalised
  margin **0.035008**, the same as Ψ_8 itself, binding at M_{2/3}. The Hessian coefficient of B_g at J is −0.082.
- Row-only Cauchy–Schwarz relaxation. Use YᵀAY ≤ (3/4)(ΣY)² − Σ_p S_p² + ΣY², where S_p are the row sums of Y;
  this keeps the rows exact and relaxes the columns. It gives R_g ≥ B_g, which depends on each row only through
  (a(r), s(r), t(r)) and the aggregates.
  - With (β, γ) ≈ (1.2441, −1.1825), R_g ≤ R_g(J) on **all row-stochastic matrices**, i.e. on the product of four
    simplices, with minimum normalised margin **0.03501** over 96 multistarts. It binds where every row is a
    permutation of (≈0.749, 0.083, 0.083, 0.083).
  - A 60-grid scan of the "three uniform rows + one free row" family gives 0.0365.
- Full Cauchy–Schwarz (columns relaxed too, a symmetric function of the entries) fails: −0.035.
- Fully separable relaxations fail badly: AM–QM on the cross term gives −0.228, and adding a tangent line of ln
  gives −0.285 per row. So the coupling through S = Σ_p s_p must be kept.

## 4. Certification plan for d = 8 (if a target is frozen) and cost estimate

**What carries over unchanged from r1's KPW audit:**
- (H1) k² − 2k − d + 2 = 2 > 0.
- The small subgraph conditioning step: (d−1)/(k−1)² = 7/9 < 1, Σλ_mδ_m² = 9 ln(3/√2), and the ratio tends to
  (3/√2)⁹.
- The n ≡ 2 (mod 4) extension: k′ = 4, r = 2, ℓ = 8, with the induced-matching remark from the Codex review.
- The lower bound χ ≥ 4: sup Φ_8 < 0 is already certified (evidence/verify_rigorous.json, C."d=8").

**New ingredients:**
1. Replace Lemma 5 by the exact inner maximisation: |T(M)|/|P_{n,8}| ≤ poly(n)·e^{nΨ_8(M)} for all M. This is the
   same argument as (3.7), without enlarging L(M) to L̂. It is routine.
2. Prove the global decay Ψ_8(M) ≤ Ψ_8(J) − c‖M − J‖² on B_4, i.e. (H2) for the exact exponent. By §3 it suffices
   to prove it for one explicit closed-form bound (B_g, or R_g on (Δ_4)⁴), with rational (β, γ).

**Route (b1), preferred: AN-style aggregate reduction of R_g on (Δ_4)⁴.**
- R_g = K + Σ_p a(r_p) + (d/2) ln((3/4)(Σ_p s_p)² − Σ_p s_p² + Σ_p t_p).
- At a maximiser, each row maximises a(r) + μ_1 s(r) + μ_2 s(r)² + μ_3 t(r), with common multipliers.
- Needed lemma: such per-row maximisers take at most two values. This would follow by a strict-concavity /
  two-solution argument like Lemma 2.1(b), applied to the per-coordinate first-order condition; it is to be proved.
- That reduces everything to rows of type (x, y, y, y) or (x, x, y, y), with how many rows of each type, plus the
  multipliers: a 4–8 parameter verification with arb, and a local Hessian argument at J.
- Cost: CPU minutes to an hour, plus analytic work.
- Risk: **medium–high, after a quick probe** (`code/probe_row_two_value.py` → `evidence/probe_row_two_value.json`).
  - For the tuned g, the per-coordinate first-order function F(r) = h′(r) + Y′(r)(κ + 2μ₃Y(r)) has up to 3
    interior turning points for multipliers in the sampled range (κ ∈ [3.26, 4.57], μ₃ ∈ [1.60, 3.53]). For
    example, at κ ≈ 3.52, μ₃ ≈ 2.71 the turning points are at r ≈ 0.14, 0.29, 0.44, with very shallow wiggles of
    ~0.01 in F.
  - So the plain two-value lemma does NOT hold as stated. (b1) would need either another dual family g that makes
    F unimodal while keeping the margin, or AN-style second-order restrictions (at most one coordinate in a convex
    region).
  - The binding configuration (all rows permutations of the same vector) is still consistent with a structured
    maximiser.

**Route (b2), fallback: direct 9-D branch-and-bound on the explicit B_g over B_4.** Inputs:
- B_4 occupies 1.05·10⁻³ of the 9-parameter cube (Monte Carlo, 4·10⁵ samples).
- Symmetry group order 1152.
- Minimum normalised margin 0.035; coefficient 0.08–0.10 near J.

Estimates:
- First-order bounds (one dual per box; U_λ is convex, so the maximum is at the 512 corners) have slack ~10²·h²,
  so they need h ≲ 0.02·dist(M, J). That is ≥ 10¹² boxes: **infeasible**.
- Second-order Taylor models (slack ~K₃h³, K₃ ~ 10² assumed) need h ≈ 0.04 at distance 0.5 and 0.015 at distance
  0.1. That is roughly 10⁶ boxes away from J plus ~4·10⁷ in the shell 0.1 ≤ ρ ≤ 0.2, with an analytic Hessian
  ball for ρ ≤ r₀ ~ 0.1. At ~0.1–1 ms per box, this is **3–30 CPU hours** (1–8 h on 4 workers) plus
  implementation.
- K₃ is not measured; the estimate is order-of-magnitude only.

## 5. Go / no-go

- **d = 9: NO-GO** for the balanced 4-colouring second moment. The exact exponent exceeds the centre at M_{3/4},
  enclosed rigorously as +0.018629… > 0. Any proof for d = 9 needs a different method.
- **d = 8: conditional GO.**
  - Numerically the exact exponent has J as its strict global maximiser (160 of 160 multistarts, five families,
    minimum normalised margin 0.035 at M_{2/3}, Hessian coefficient −0.1).
  - A closed-form dual bound preserves that margin, even after relaxing to the product of simplices (R_g).
  - Recommended next step, if the parent wants to pursue d = 8: a ≤ 2 h pilot of route (b1). First search for a
    dual family g that keeps the 0.035 margin and makes F unimodal on the relevant multiplier range; then prove
    the two-value lemma. Freeze a target "χ(G_{n,8}) = 4" only if the pilot succeeds. Otherwise fall back to (b2),
    and only if ~1 day of 4-worker compute and a Taylor-model implementation are acceptable.
  - Nothing here is a claim. Every number in §§2–3 except the point enclosures is floating-point evidence.
