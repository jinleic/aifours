# [INFERENCE] Exploratory lead: the χ8 route for general k, and the case (k, d) = (5, 12)

**Status.** EXPLORATORY ONLY. This is not a frozen target and nothing here is claimed; it stays [INFERENCE] until it
is proved in a frozen file and reviewed. Under contract r2's `optional_after_r1`, it is not part of any target until
the χ8 proof is accepted. Bounded: identities and constants only, no solver search.

Check: `explore/check_general_k.py` → `explore/check_general_k.json` (+ `.stdout.txt`), run 07:46:08–07:46:13 PDT.
Identities are exact (sympy, k = 3…6), constants are arb at 256 bits, and the float section is not evidence.

## 1. General-k form, checked exactly

Setting: k colours, cells [k]², allowed pairs p ≠ r and q ≠ s, and a doubly stochastic M with Σ m = k.
- **Lemma A analogue.** The same proof as PROOF_CHI8.r1 §2 gives
  V_μ = ((d−1)/k) Σ m log m + (1 − d) log k + (d/2) log d + Σ_e e^{μ_u+μ_v−1} − (d/k) Σ μ_u m_u.
  The polynomial factor now has k² cells and k²(k−1)²/2 pairs.
- **Closed form.** With μ_u = c + β log m_u and β = (d − 1)/d the entropy cancels. Optimising c gives
  U = (1 − d) log k + (d/2) log(2E_β), where E_β := Σ_{allowed} (m_u m_v)^β.
  Also U(J) = (2 − d) log k + d log(k − 1), the (EY)² exponent (sympy, symbolic in k and d).
- **Row reduction.** 2E = (Σf)² − ΣR² − ΣC² + Σf² ≤ (k − 2)ΣR² + Σf², with an exact certificate (k = 3…6). So
  E ≤ Σ_p F_k(r_p), where F_k := ((k − 2)/2)S² + Q/2.
- **Row function.** F_k = (k(k − 1)²/2)‖T_{1/(k−1)} g‖² on the uniform k-point space, with g = r^β (k = 3…6).
- **Hypercontractivity.** D–SC Theorem A.1 gives α = (1 − 2/k)/log(k − 1). With ρ = 1/(k − 1), i.e.
  t = log(k − 1), 4αt = 4 − 8/k (symbolic). The condition is d − 1 ≤ e^{4 − 8/k}.

## 2. Reach by k (floors certified in arb)

| k | 1 + e^{4−8/k} | route reaches | KPW/AN 2(k−1) log(k−1) | NPG ℓ_k |
|---|---|---|---|---|
| 3 | 4.79 | d ≤ 4 | 2.77 | 3.70 |
| 4 | 8.39 | d ≤ 8 | 6.59 | 7.42 |
| 5 | 12.02 | d ≤ 12 | 11.09 | 11.83 |
| 6 | 15.39 | d ≤ 15 | 16.09 | 16.76 |
| 7–12 | 18.4 … 29.0 | — | 21.5 … 52.8 | 22.1 … 53.2 |

The route goes beyond NPG only for k = 3, 4, 5. 1 + e^{4−8/k} stays below 1 + e⁴ ≈ 55.6, so for k ≥ 6 the route
is weaker than KPW/AN.

At k = 3 it gives d ≤ 4. That is consistent with the known χ(G_{n,4}) = 3 (Shi–Wormald), and it does not reach the
open case d = 5. This is a sanity check, not a claim.

## 3. The case (k, d) = (5, 12) [INFERENCE]

**Constants** (exact or arb). They agree with the parent's re-derivation.
- β = 11/12. F = (3/2)S² + Q/2 = 40‖T_{1/4} g‖².
- α_LS = 3/(5 ln 4) = 0.43280851…
- a = 11^{−5 ln 4/12} = 0.25030411935346394263… > 1/4 (certain).
  - This is equivalent to ln 11 < 12/5, i.e. 11⁵ = 161051 < e¹².
  - Exact: Σ_{j<22} 12^j/j! already exceeds 161051, and every term is positive.
- a² − 1/16 = 1.5215216531…·10⁻⁴ > 0.
- κ = (121/18)(a² − 1/16) = 0.0010228006668…, with ((k−1)²/2)β² = 121/18 exact.
- E_0 = E_β(J) = 200·5^{−11/6} = 10.46128388…
- C_12 = 6κ/E_0 = 5.866205397548…·10⁻⁴ > 0 (certain).

**Other parameters.**
- (H1) = 25 − 10 − 12 + 2 = 5 > 0.
- Series ratio 11/16 < 1.
- EY growth 5(4/5)⁶ = 4096/3125 > 1.
- Molloy–Reed at q = 4: 4(3/4)⁶ = 729/1024 < 1, which would give χ ≥ 5.
- KPW at d = 12 has k = 6, since 8 ln 4 < 12 < 10 ln 5, so the window is {5, 6}. Their exact clause d > 9 ln 5
  fails.
- NPG ℓ_5 = 11.8297… < 12.

**Control.** At d = 13, e^{12/5} < 12 (certain), so the condition fails.

**Float sanity, not evidence.** max (E_β(M) − E_β(J))/‖M − J‖² = −0.0644 over 3000 random 5×5 doubly stochastic
matrices plus (1 − t)J + tI. The theorem predicts ≤ −κ ≈ −0.001.

**What a frozen (5, 12) proof would still need.** None of this is checked here.
- Lemma A at k = 5: 25 cells, 200 pairs, explicit polynomial factor.
- The audit rows at (5, 12).
- Small subgraph conditioning: Σλδ² = 16 log(4/√5), ratio (4/√5)^16.
- Residues n mod 5, r = 1…4, with ℓ = 6r and multinomial(12r; 12, …, 12) uniformity.
- A second, elementary proof of the row inequality on Δ_5, if wanted. The two-value lemma generalises; the arb
  families would be (x, y, y, y, y) and (x, x, y, y, y).
- A priority check for χ(G_{n,12}) = 5.

The margin is small: a² − 1/16 ≈ 1.5·10⁻⁴, and e^{2.4} exceeds 11 by only 0.2%. So every constant must be
certified.
