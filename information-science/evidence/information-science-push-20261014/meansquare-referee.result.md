`★ Insight ─────────────────────────────────────`
- Theorem 1 rests on four kernel identities (K1, K2, M0, M1). Once they hold, the Itô drift of V cancels term by term, so the completion of squares is pure algebra. It also survives the (b−h,b] tail, because K(t,b) ≡ 0 on [b−h,b] when P(b)=0.
- For a scalar plant with multiplicative noise, preview gives γ_opt² = 2(1+e^{−2h}). This value sits strictly between the h=0 adapted value (4) and the deterministic-disturbance value (2). That gap is exactly why F2 (W-correlated disturbances) carries the necessity proof.
`─────────────────────────────────────────────────`

```json
{
  "verdict": "correct-with-fixes",
  "theorem_verdicts": {
    "Theorem 1": "correct-with-fixes (minor). I re-derived the following without finding an error: K1, K2, M0, M1; the Lemma 2 grouping, including t in (b-h,b]; adaptedness of u* and w*; Lemmas 3, 5, 7 and 8 (the Lemma 8 adjoint was verified explicitly); and the blow-up alternative. The one real gap is in Lemma 6, which uses the hypothesis at w=0 although Theorem 1(1) and F5 quantify only over w≠0. The gap closes under F2 plus strong well-posedness (R-01, R-02).",
    "Theorem 2": "correct-with-fixes, conditional on cited standard facts. I checked Steps 0-7 and Lemma 9. A closed-form stochastic example with h>0 matches the theorem exactly, including an independent lower bound (R-09). (A3) is a genuine restriction and must be stated for the transformed data (R-04). The theorem is not fully proved: the renewal, Krein-Rutman, SFDE continuous-dependence and Datko-type facts are cited, not proved (R-05)."
  },
  "findings": [
    {
      "id": "R-01",
      "severity": "minor",
      "location": "Sec. 0 (||T||<γ ⇔ J≤−ε||w||² for all w∈𝒲); Sec. 3.4 hypothesis; Lemma 6 ('For w ≡ 0 the hypothesis gives E∫|z|² ≤ 0')",
      "problem": "Theorem 1(1) and F5 take the sup over w≠0 only. So the fact that the w≡0 loop has z̄≡0 is not given, yet both Lemma 6 and the Sec. 0 equivalence use it.",
      "counterexample_or_check": "Take K_bad = u* on [a,b−h], and on (b−h,b] add e1·1{∫_a^{b−h}|w|²=0} (a measurable, nonanticipative rule). For every deterministic w≠0, K_bad equals u*, so its gain is <γ. At w=0, however, z̄≠0. So the step fails for a deterministic-only disturbance class. Under F2 the step is true. Take A∈F_{a+δ} with 0<P(A) small and w=ε1_A on [a+δ,b−h]. On Aᶜ the loop coincides with the w≡0 loop, so E[1_{Aᶜ}∫|z̄|²] ≤ γ1²ε²P(A)(b−h−a−δ). Let ε→0, then P(A)→0; this gives z̄≡0. Equivalently, K_bad has infinite gain under F2.",
      "suggested_fix": "Insert this localization lemma before Lemma 6. It needs b−h>a, non-atomic F_{a+δ}, and pathwise locality of the closed loop. Alternatively, define feasibility as E∫|z|² ≤ γ1²||w||² for all w∈𝒲 including 0, and prove the equivalence."
    },
    {
      "id": "R-02",
      "severity": "minor",
      "location": "F4; Lemma 6 ('on [a,t] the trajectory equals the w≡0 trajectory'); F2 randomisation remark",
      "problem": "'Closed loop well posed' is never specified. Lemma 6 and R-01 need four things: strong (pathwise) existence and uniqueness for every w∈𝒲 on the given filtered space; u∈L²_F for every w; nonanticipative path functionals; and locality (inputs equal on an F_s-event imply trajectories equal on that event). Weak well-posedness does not identify trajectories.",
      "counterexample_or_check": "Under strong well-posedness, Lemmas 6-8 go through. Enlarged filtrations are also fine: in Lemma 8 the martingale part q dW = P(A0x+B0u)dW is explicit, so no representation theorem is needed. Lemmas 6-8 take the inf over all F-adapted u, so necessity even covers controllers that observe W.",
      "suggested_fix": "Define admissibility as strong well-posedness for every w∈𝒲 with u∈L²_F. Then state the robustness remark (necessity covers controllers that observe W)."
    },
    {
      "id": "R-03",
      "severity": "major (scope/fidelity; not a proof error, and the manuscript already disclaims it)",
      "location": "F2; necessity in Theorems 1 and 2; any summary calling (𝒫)/(𝒜) N&S for 'the book problem'",
      "problem": "Necessity needs disturbances correlated with W (a feedback worst case). If the disturbance class is restricted to deterministic or W-independent signals, the condition remains sufficient but is strictly not necessary.",
      "counterexample_or_check": "Plant: n=1, A=−1, B=0, C=1, A0=1, B0=0, D0=(1,0)ᵀ, D1=(0,1)ᵀ. F6 and A1-A3 hold. For w deterministic or independent of W, E∫x² = ∫∫e^{−|r−s|}w(s)w(r)dsdr ≤ 2||w||², so u=0 has gain ≤√2 for every horizon and every h. For adapted w with h=0, (𝒫) reads −Ṗ = γ^{−2}P² − P + 1, which is >0 for γ<2. At γ=1.9 it escapes after backward time ∫_0^∞dP/(0.277P²−P+1) ≈ 17.2. So for γ=1.9 and b−a≥18, the deterministic-w problem is solvable while (𝒫) has no solution on [a,b]. For h>0 the adapted threshold is γ²=2(1+e^{−2h})>2 (R-09), so the separation is strict for every finite h.",
      "suggested_fix": "Put the disturbance class into every theorem statement ('all F-progressive w, including feedback disturbances'). State that the deterministic and W-independent variants are not characterized, and that the condition is only sufficient for them."
    },
    {
      "id": "R-04",
      "severity": "minor",
      "location": "Sec. 5, (A1)-(A3)",
      "problem": "The 'WLOG' substitution in (A1) replaces (A, A0, D0). Detectability is not invariant under this substitution, so (A3) must be imposed on (D̃0; A−BΣ, A0−B0Σ). (A2)-(A3) are restrictions (R) but are missing from the F1-F7 list. (A3) cannot be dropped: it is used in ⇐ step 1 and in ⇒ steps 6(iv) and 7(b).",
      "counterexample_or_check": "Add a state x2' = x2+u2 that is absent from D0 and not driven by w. Then lim P_T(0) vanishes on that block, A_P has eigenvalue +1, and T1 fails at the limit. Yet the IS problem is solvable via u2=−2x2, and another root (p2=2) is stabilizing. In this example (A3) fails.",
      "suggested_fix": "Label A2 and A3 as (R) formalization items, and state A3 for the transformed data."
    },
    {
      "id": "R-05",
      "severity": "minor",
      "location": "Lemma 9 steps 2-4; Theorem 2 steps 1, 3, 6(ii); Sec. 6",
      "problem": "Theorem 2 is proved only modulo cited facts. Lemma 9 step 2's 'iff' consistency claim is only sketched. (T2) is well defined only under (T1).",
      "counterexample_or_check": "I re-derived the parts that are actually used. Under u*, the drift of (x;p) is H0(P)[x;p]+[Cv;0], with p-drift −Ãᵀp−Q̃x. After the first window the conditional means lie in E·graph(P) and evolve by A_P; this also holds with v_0 forcing, using g0=∫[P,−I]e^{−H0r}[C;0]v_0(r)dr. The dW-part is [I;P]σ with σ=Γσ(x;p). The renewal equation and the Perron argument are correct.",
      "suggested_fix": "Keep the 'modulo cited facts' qualifier in every claim. Write T2 as 'T1 and ρ(𝒯_P)<1'. Replace the 'iff' in step 2 with the forward inclusion that is actually used."
    },
    {
      "id": "R-06",
      "severity": "nit",
      "location": "Sec. 4 (deterministic case); Remark (iii)",
      "problem": "The identity H_eff = e^{−H0h}H_γe^{H0h} holds only for t≤b−h; on (b−h,b], H_eff=H0. With P(b)=0, k is continuous at b−h because K(t,b)≡0 on [b−h,b]. With a terminal penalty P_b≠0, k jumps there. The jump is harmless for Carathéodory solutions, but it is unstated.",
      "counterexample_or_check": "∂_tK(t,b) = −A_cᵀK(t,b) on (b−h,b] with K(b,b)=P(b)C(b).",
      "suggested_fix": "Add both qualifiers."
    },
    {
      "id": "R-07",
      "severity": "info",
      "location": "Header; F1(b); Secs. 6-7",
      "problem": "Several claims cannot be checked from this manuscript: the book text, the 2014 criterion, literal_continuation.md, the Codex referee rounds, and the numerics (1.72152). None of them is evidence of correctness.",
      "counterexample_or_check": "n/a",
      "suggested_fix": "Cite them as provenance only."
    },
    {
      "id": "R-08",
      "severity": "check-passed",
      "location": "Lemmas 1-2, 4, 8; Sec. 1 feedback laws",
      "problem": "none",
      "counterexample_or_check": "(K2): the difference is (Ṗ+ÃᵀP+PÃ+Q̃−PBR̂⁻¹BᵀP)Φ11C = −γ^{−2}kkᵀΦ11C. (M0): follows from ΦJΦᵀ=J and Φ11(t,s)=Φ22(s,t)ᵀ. (M1): follows from ∂tΦ22(s,t)=Φ21BR̂⁻¹Bᵀ+Φ22Ãᵀ. Lemma 2 grouping: the v(t)-terms cancel; the x-g terms cancel since A−A_c=BR̂⁻¹L; the x-μ, g-g and μ-μ terms cancel; the x-x block is (𝒫). On (b−h,b] there is no incoming term, and k=0, μ=0, so the identity holds with ∫_a^{b−h}|w−w*|². u* and w* use x(t) and w|[t−h,t] only, with no instantaneous w(t) term. They are therefore F_t-measurable and progressive, and w=w*+η is a Volterra equation (Lemma 4 is fine). Lemma 8: drift minus target equals Lᵀ(u°+R̂⁻¹(Lx+Bᵀg))=0, and stationarity is Lx+Bᵀg+R̂u°=0.",
      "suggested_fix": "none"
    },
    {
      "id": "R-09",
      "severity": "check-passed",
      "location": "Lemma 7; Theorem 2 (𝒜), T1-T2; Sec. 4 reductions",
      "problem": "none",
      "counterexample_or_check": "Lemma 7: with ρ=ε/γ², (1+ρ)(γ²−ε)−γ² = −ε²/γ². For the R-03 plant with h>0: k = P cosh h − sinh h, and (𝒜) becomes 0 = −P+1+γ^{−2}(P cosh h − sinh h)². The discriminant is 1−4γ^{−2}e^{−h}cosh h, so (𝒜) is solvable iff γ² ≥ 2(1+e^{−2h}). The smaller root P>0 satisfies T1-T2: A_P = −1+γ^{−2}e^h k, and T2 ⇔ A_P < −1/(1+e^{2h}). At the threshold A_P = −1/(1+e^{2h}), so ρ(𝒯_P)=1 exactly. Independent lower bound: let the adversary play w=θζ with ζ(t)=E[x(t+h)|F_t]. Then E∫x² = 2E∫ζw. The renewal kernel is ψ(τ)=e^{−τ} for τ≤h and e^{(θ−1)τ−θh} for τ>h. ∫ψ²=1 ⇔ θ=1/(1+e^{−2h}), which gives gain² ≥ 2(1+e^{−2h}). This matches exactly: 4 at h=0, and 2 as h→∞. The h=0 reduction holds (k=PC). Deterministic check (A0=0): the threshold γ≥|C/A| is independent of h, as it must be.",
      "suggested_fix": "Optionally add this example as a regression test."
    }
  ],
  "load_bearing_external_facts": [
    "Strong existence/uniqueness and E sup|x|² bounds for linear SDEs/SFDEs with bounded coefficients and L² (Volterra-type) inputs (Lemmas 2, 4, 8; Theorem 2).",
    "Burkholder-Davis-Gundy inequality (true-martingale property in Lemma 2 and in the Lemma 8 duality).",
    "Carathéodory existence, uniqueness, continuation and parameter-continuous dependence for retarded FDEs in reversed time (Lemma 5; openness in γ).",
    "Non-atomicity of the Brownian σ-field F_{a+δ}, plus pathwise locality of strong solutions (needed for the R-01 fix).",
    "Renewal theory for matrix-valued positive convolution equations: if the kernel decays exponentially and ρ(∫𝒦)<1, solutions decay exponentially (Lemma 9).",
    "Krein-Rutman/Perron-Frobenius for positive maps on the PSD cone (Lemma 9 converse).",
    "For LTI SDEs, L²-stability for all x0 ⇔ exponential mean-square stability; an MS-stable system driven by L² inputs has an L² state (Theorem 2 steps 1, 6(iv), 7(b)).",
    "Continuous dependence of linear SFDE solutions on uniformly convergent coefficients on compact intervals (Theorem 2 step 6(ii)).",
    "For the h=0 remark only: (A,A0) is MS stable ⇔ A is Hurwitz and ρ(Γ∫e^{Aτ}(·)e^{Aᵀτ}dτ Γᵀ)<1.",
    "Fidelity only, not used in any proof: the book text (pp. 674-676), the Wang-Zhang-Chen-Yu 2014 criterion, and the Hinrichsen-Pritchard 1998 stochastic bounded real lemma. None verified here."
  ],
  "permissible_claim_wording": "Setting: the mean-square formalization F1-F6, meaning expected-energy norms; disturbances ranging over all F-progressive L² processes, including feedback disturbances correlated with the plant noise; x(a)=0 with zero pre-window; and D1ᵀD1 ⪰ r0I uniformly. Admissible controllers are strongly well-posed, nonanticipative, possibly nonlinear full-information rules. Finite horizon: a controller with sup_{w≠0}||z||/||w|| < γ exists iff the advanced generalized Riccati functional differential equation (𝒫) has a solution on [a,b]. In that case P ⪰ 0, and the explicit preview law u*, which uses only x(t) and w on [t−h,t], achieves the bound. Moreover, J(u,w) = E∫_a^b|R̂^{1/2}(u−u*)|² − γ²E∫_a^{b−h}|w−w*|² for all admissible u and all w. Infinite horizon: assume constant data, (A1)-(A3) with A3 imposed on the transformed data, and internal mean-square stability. Then solvability is equivalent to the existence of a solution P ⪰ 0 of (𝒜) with A_P Hurwitz and ρ(𝒯_P)<1. That solution is unique and equals lim P_T(0). This infinite-horizon statement is proved modulo cited standard facts (SFDE well-posedness and continuous dependence, positive renewal theory, Krein-Rutman). Not claimed: anything about the printed L¹(Ω;L²) ratio; necessity when disturbances are restricted to deterministic or W-independent signals (there the condition is sufficient but provably not necessary); attainment at γ_opt."
}
```