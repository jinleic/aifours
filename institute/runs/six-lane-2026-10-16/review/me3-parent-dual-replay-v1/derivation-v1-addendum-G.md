# Addendum to derivation-v1.md: G-chart enclosures in dualcheck_v2/v3

This addendum covers the G chart only. The tests of derivation-v1.md §3 (G) are unchanged; only the enclosure
arithmetic changes. Each change is a sound enclosure on its own, so the change cannot turn a false inequality into
a passing one.

* **v2: log|W|.** dualcheck_v1 computed log|W| as log(abs(W)). Python-flint returns abs(W) as the ball |mid| ± rad,
  whose lower end can be negative even when the complex ball W excludes 0, and the log of that ball is NaN.
  * Effect in v1: every such radial test failed, which is safe but very slow (run r10, aborted).
  * v2 replaces it with logabs_hull(W) = [log abs_lower(W), log abs_upper(W)].
    * abs_lower and abs_upper are Arb's rigorous bounds of |w| over the ball.
    * The hull is used only when abs_lower > 0 is certified.
  * Control C10 (r15) confirms that the hull contains log|W(x)| at 450 corner and midpoint samples (diagnostic).
* **v3: W.** On a box B, W is enclosed by the intersection of three enclosures, each valid for every x ∈ B:
  1. the Horner form zz(w₁ + zz(w₂ + zz·w₃)) in balls;
  2. the rational form q/(N₁z³) in balls (I2b);
  3. the centred form W(m) + Σ_j ∂_jW(B)·[−h_j, h_j].
  * Item 3 is applied to the real and imaginary parts separately: by the mean value theorem for each real function,
    |Re W(x) − Re W(m)| ≤ Σ_j |Re ∂_jW|_B h_j, and likewise for Im.
  * Derivatives used: ∂_sW = (q_sN₁ − qN₁′)/(N₁²z³) and ∂_ξW = (q_z z − 3q)/(N₁z⁴) (I13). Since ξ = δ − iω,
    ∂_δW = ∂_ξW and ∂_ωW = −i∂_ξW.
  * The intersection of valid enclosures is valid. If an intersection is empty (Arb raises), that candidate is
    skipped. This cannot happen for valid enclosures; it is a guard only.
* **Unchanged.** The branch certification (Im W > 0, Im W < 0 or Re W < 0 on the whole enclosure), the
  α ∈ [0, 2π) choice, the MVF of F (gradients from L and L_s, with the midpoint re-checked on the same branch),
  SMALL, TRIANGLE and the SKIP rule.
