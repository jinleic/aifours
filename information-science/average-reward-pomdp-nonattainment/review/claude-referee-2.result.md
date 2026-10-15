## Verdict: ACCEPT

I re-derived every formula and class claim in the revision by hand; nothing was machine-checked. No mathematical error or scope overclaim remains. The three items under "Optional edits" are about precision and editing, and acceptance does not depend on them.

### First-report findings

| Finding | Status | Basis |
|---|---|---|
| 1. Source match (Major) | Resolved | The theorem is self-contained. §1 makes the source relation explicitly conditional. §7 gives verbatim quotes, translations and page numbers. The assumption check is disclosed with its limit (article plus front matter and TOC). I took the source facts as parent evidence. |
| 2. Total vs partial reading | Resolved | "No map, computable or not" now appears. Decision, construction and the "no optimizer" selector are separated. The methodological reading is handled in §6–§7. |
| 3. Pathwise criteria | Resolved | The expectation criterion is fixed before the theorem. §5 covers ess inf and ess sup. §7 records that the printed formula has no E. |
| 4. Policy classes | Resolved | Each class claim is verified below. The deterministic finite-class claim now correctly requires time-homogeneity, a fixed initial memory state and no clock. |
| 5. Citation | Resolved in substance | The objective is named, the undecidability is attributed to earlier work, the intent ascription is gone, and the consistency sentence is correct. The statements are still paraphrased rather than quoted. |
| 6. §3 rigor | Resolved | Kernels are defined. The chain rule gives joint laws with no conditioning on null events. Mixtures are handled by integrating over a seed independent of plant noise. |
| 7. §4–§5 wording | Resolved | The explicit map N → N+1 gains (1−q)·E[q^N; N<∞]. The failure of upper semicontinuity is stated correctly. |

### Added claims re-derived

- **Randomized stationary (c) family.**
  - Σ c(1−c)^n q^n = c/(1−q(1−c)), which gives J = (1−c)/(1+c) at q = ½.
  - J < 1 on all of [0,1], and lim_{c↓0} J = 1 > J(0) = 0. ✓
- **Randomized k-state controllers.** They contain the randomized memoryless policies, so the class sup is 1, and no member attains it. ✓
  - The paper's "hence" is valid only because the subclass already reaches the global sup and the theorem says no admissible policy attains it. Nonattainment does not pass to a superclass in general.
- **Open-loop and belief-stationary classes.**
  - Pre-commit beliefs (q^n, 1−q^n) on {B,G} are pairwise distinct.
  - Post-commit beliefs live on {H,L}.
  - So every W^nC is implementable in both classes. ✓
- **Deterministic, time-homogeneous controllers with at most k memory states and a fixed initial state.**
  - Pre-commit input is constant, so the memory orbit is deterministic.
  - A repeated pre-commit memory state forces an all-W cycle, so N ≤ k−1 or N = ∞.
  - The maximum is 1−q^{k−1}, attained by W^{k−1}C. For k = 1 this is 0, matching the two memoryless policies. ✓
- **Pathwise criteria.**
  - η = 1_H, and Eη = P(η=1) = J.
  - ess inf η = 0 for every π, because P(η=0) = 1−J(π) > 0.
  - ess sup η = 1 is attained by WC, since P(η=1) = 1−q. ✓
- **lim, liminf and limsup, inside or outside E.** They all coincide: the pathwise limit exists, and E r_t = P(X_t=H) increases to J. ✓

### Optional edits

1. **§7 should state the policy-class condition explicitly.**
   - §1 conditions the source relation on an "unrestricted-policy reading", but §7's closing sentence names only the criterion and recurrence conditions.
   - The quote opens with 在最一般的情况下 ("in the most general case"). Add one sentence, based on the page reading, saying that the question is posed over that class and that no narrower class is introduced before it.
   - Also say that the conclusion holds whether 函数 ("function") is read as deterministic (the class contains every W^nC) or as distribution-valued (it is then the admissible class).
   - This sentence matters. By §5's own finite-class result, narrowing to deterministic current-output policies would make a maximizer exist trivially.
2. **Chatterjee–Saona–Ziliotto locators.** I cannot verify Thm 2.9, Def 3.1, Cor 3.2 or §3.1 from the embedded material. Quote them or mark them author-checked. Nothing depends on them, because all the average criteria coincide in this example.
3. **Wording nits.**
   - The §1 heading says "observation convention", but the section fixes the criterion.
   - "The parent" in §7 is workflow jargon; use a reader-facing attribution.
   - §4's "0 < ε < 1" leaves ε ≥ 1 formally untreated, although the same least-n rule gives n = 0 there.
   - "These are existence statements" should read "nonattainment statements about this instance".

### Accepted scope

**Proved and verified.** The setting:
- the blind four-state model with q ∈ (0,1), and q = ½ for rational data;
- initial state B, with or without observed rewards;
- expected long-run average reward, with any placement of lim, liminf or limsup (all are equal here);
- all history-dependent behavioral policies and their mixtures that are independent of plant noise.

In that setting:
- J(π) = Σ P(N=n)(1−q^n) < 1 for every π, and sup J = 1.
- W^nC is an (n+1)-state deterministic counter that is q^n-optimal.
- N → N+1 strictly improves every policy with P(N<∞) > 0.
- The supremum is not attained within the randomized memoryless, randomized fixed-size, deterministic open-loop and deterministic belief-stationary classes.
- Attainment is trivial within time-homogeneous deterministic k-state controllers.
- Under Eη = P(η=1) there is no optimizer. Under ess inf η every policy is optimal. Under ess sup η the maximum is attained.
- No map, computable or not, returns an expected-average-optimal policy for every finite rational POMDP. This is not a decidability statement.

**Conditional on the parent's source evidence.** The article's universal request has a false presupposition, under three conditions:
- the formula, printed without E, is read as an expectation;
- the article imposes no recurrence restriction;
- the question is posed over the quoted general policy class. The revision implies this but does not state it (see edit 1).

**Not covered:**
- models with recurrence restrictions;
- pathwise orderings other than ess inf and ess sup;
- deciding whether an optimizer exists, or constructing one;
- any methodological answer;
- the Chatterjee–Saona–Ziliotto locators;
- novelty, which is not claimed.

`★ Insight ─────────────────────────────────────`
- **Why "nonattainment within class X" holds in §5.** Each such line is valid for the same reason: X already reaches the global supremum 1, and no admissible policy attains 1. Without that, nonattainment in a subclass would say nothing about a superclass, which could contain a maximizer.
- **Why deterministic and randomized classes behave differently.** Deterministic k-state controllers form a finite set, so a maximum exists trivially. Randomizing even one state gives a compact interval of c values. J is discontinuous exactly where "commit with vanishing probability" collapses into "never commit". The obstruction lies in that discontinuity, not in memory size.
- **What happens for other ways of ranking random payoffs.** η takes only the values 0 and 1, so any criterion that ranks policies by P(η=1) also has no optimizer here, including first-order stochastic dominance. This extension is mine; the proof does not claim it. The worst-case criterion degenerates for the same reason: J(π) < 1 means P(η=0) > 0, which fixes ess inf η at 0 for every policy.
`─────────────────────────────────────────────────`