# Referee report: "An optimal policy need not exist for the book's POMDP model"

## Verdict

**The mathematics is sound.** I re-derived every statement and formula by hand; nothing was machine-checked. I found no error in the theorem, its quantifiers, the reduction to the first commit time, the indexing, the reward timing, the existence of limits, the strict-improvement formula or the randomized-stationary formula.

The defects are all in scope and framing:
- **One Major finding:** the link from the theorem to "the book's model" rests on a paraphrase of the source that I cannot verify.
- **Several Moderate findings:** some robustness and faithfulness claims are narrower than written.

I assessed correctness and scope only, not novelty. Recommendation: accept the theorem; revise the framing.

## Verification record

| Claim | Location | Result |
|---|---|---|
| Theorem: ∃M ∀π, J(π) defined and < 1; sup = 1; ∀ε ∃ finite-memory deterministic ε-optimal π | §1 | ✓ |
| Before the first C, the history is the single all-W history (constant observation; zero rewards if observed; with or without recall of own actions), so N depends only on private randomness | §2–§3 | ✓ |
| Independence: P(N=n, X_n=B) = qⁿ·P(N=n) | §3 | ✓ Commit at time n follows transitions at times 0…n−1; n=0 gives value 0 |
| Reward timing | §2 | ✓ Pre- vs post-transition rewards shift partial sums by at most one term; the limit is unchanged |
| Limits exist; lim / liminf / limsup, with expectation inside or outside, all agree | §1, §5 | ✓ Pathwise limit is 1{H}. Independently, E r_t = P(X_t=H) is nondecreasing, so the Cesàro limit exists |
| J(π) = Σ P(N=n)(1−qⁿ); gap = P(N=∞) + Σ P(N=n)qⁿ > 0 | §3–§4 | ✓ Uses q > 0 (and q < 1 for sup = 1) |
| J_n = 1−qⁿ; least n with 2⁻ⁿ ≤ ε; (n+1)-state counter | §4 | ✓ n+1 states is also minimal for a deterministic controller with constant input |
| Shifting N to N+1 gains (1−q)·E[q^N; N<∞]; WC gives 1−q | §4 | ✓ |
| Stationary c: P(N=n) = c(1−c)ⁿ, J(c) = 1 − c/(1−q(1−c)), and for q=½, (1−c)/(1+c) | §5 | ✓ Spot check c=½: series 1 − ½·Σ4⁻ⁿ = ⅓, same as formula |
| Belief P(G) after n W actions = 1−qⁿ | §5 | ✓ |
| Full observation attains 1 | §5 | ✓ Readiness time is Geometric(1−q) on {1,2,…}, finite a.s. |
| No map selects an exact optimizer for every instance | §6 | ✓ Immediate from nonattainment |

## Findings

Severity scale:
- **Major:** a headline claim may be false as stated.
- **Moderate:** a claim is narrower than written, or an external claim is unverified.
- **Minor:** rigor or wording only; the result is unaffected.

### 1. The match with the source is unverified, and the title depends on it — Major (the theorem itself is unaffected)

**Location:**
- the title;
- §1 ¶1 ("describes policies… It gives no recurrence, mixing or optimizer-existence hypothesis");
- §6 ¶1 ("the article's unrestricted model").

**Problem.** The source text is not included in the note. Three facts place the example inside "the book's model": the policy class, the performance criterion, and the absence of standing hypotheses. All three are paraphrase.

The absence claim is the riskiest. Average-reward performance-optimization treatments often fix ergodicity or unichain assumptions once, at chapter or volume level. This example violates every such assumption:
- H and L are both absorbing.
- Every stationary randomized policy with c ∈ (0,1) reaches both, so the chain is multichain.
- The underlying MDP is not communicating.

If any such standing assumption applies, the title is false even though the theorem stands. Separately, "the book's POMDP model" could mean either the article's general formulation or a specific instance studied in it.

**Repair.**
1. Quote verbatim, in the original and in translation with page numbers, the article's policy definition, its performance formula and its question.
2. State that the enclosing chapter and volume were checked for standing assumptions.
3. Split §1 into (a) a self-contained theorem about finite POMDPs and (b) a conditional section on the relation to the source.
4. Retitle, for example: "An average-optimal policy need not exist in a four-state blind POMDP."
5. Add "existence under ergodic, unichain or communicating hypotheses" to the not-settled list in §6.

### 2. The negative answer refutes only the total reading of the request — Moderate

**Location:** §6 ¶1 ("A procedure required to return a truly optimal policy… complete negative answer").

**Problem.** Consider the total reading: for every instance M, output π with J_M(π) = sup J_M. The note is correct and complete for that reading. The request presupposes that an optimizer always exists, and that presupposition is false on part of its domain. Rejecting a false presupposition is the faithful answer. Three qualifications are missing:

- **(a) "Procedure" is misleading.** It suggests a computability result. The actual obstruction is that no admissible output exists, so no map works, computable or not.
- **(b) The partial reading is not addressed.** Under "return a maximizer whenever one exists, otherwise report none", a non-constructive selector trivially exists. The question therefore becomes purely computational: decide whether an optimizer exists, then construct it. The note does not touch this.
- **(c) A methodological reading is not addressed.** If the source's "how to choose" asks for a method, the note supplies none. It only shows that any method must restrict the instances, restrict the policy class, change the criterion, or relax to ε-optimality.

**Repair.**
- Replace the sentence with: "No map, computable or not, assigns an average-optimal policy to every finite POMDP; on the unrestricted class, 'maximum' must be read as 'supremum'."
- Add to the not-settled list: deciding whether a given finite rational POMDP admits an average-optimal policy, and constructing one when it does.

### 3. "The limit exists" covers only expectation-type criteria — Moderate

**Location:**
- §1 ¶3 ("The printed formula is informal about expectation");
- §5 "The limit exists", last sentence.

**Problem.** Suppose the printed formula is a sample-path average. That is a natural reading where ergodicity makes the average almost surely constant. In this example, η = lim T⁻¹Σr_t = 1{H reached} is a genuinely random quantity, so "maximum" requires choosing how to turn it into a number. The answers differ:

- **E η, P(η=1), or P(η≥x) for x ∈ (0,1]:** each equals J(π), so nonattainment persists.
- **Abel mean lim_{β↑1} (1−β)·E Σβᵗr_t:** this equals J(π), by the pathwise Abelian theorem and bounded convergence, so nonattainment persists. In addition, (1−β)V_β = E[β^{N+1}(1−q^N); N<∞] is maximized at a finite n*(β) that tends to infinity as β↑1. Hence no Blackwell-optimal policy exists.
- **ess inf η** (the almost-surely guaranteed average): this is 0 for every π, because P(η=0) = 1−J(π) > 0. Every policy is optimal.
- **ess sup η:** this is 1, attained by WC.

So "does not alter the result" holds for expectation and success-probability criteria. It fails for pathwise worst-case and best-case criteria.

**Repair.**
- Add these cases to §5.
- State in the theorem that the criterion is the expected average (equivalently, the success probability).
- State that the example applies to the source only if its formula is read as an expectation.

### 4. The note does not say which policy classes the conclusion holds for — Moderate

**Location:**
- the theorem's policy-class sentence;
- §5 "Unlimited memory…" and "Randomized stationary…".

**Problem.** §5 argues only that larger policy classes do not restore attainment. Because the source's policy class is only paraphrased (Finding 1), faithfulness also needs the other direction. I checked:

**No maximizer (sup = 1, never attained):**
- deterministic open-loop policies W^nC;
- deterministic belief-stationary policies (the pre-commit beliefs (qⁿ, 1−qⁿ) are all distinct, so each W^nC is belief-stationary);
- randomized memoryless policies;
- randomized finite-state controllers of any fixed size k ≥ 1;
- randomized "current observation plus last action" policies.

**Maximizer exists, trivially, in any finite class:**
- Deterministic memoryless: there are two policies, both with J = 0.
- Deterministic k-state controllers: with constant input, the first C occurs at index ≤ k−1 or never. The maximum is 1−q^{k−1}, attained by W^{k−1}C.

**Repair.**
- Add this list.
- Promote the randomized-memoryless result to a corollary of the theorem. Optimizing over parametrized randomized policies is a plausible reading of the source.

### 5. The external citation is unverified and partly ascribes intent — Moderate (does not affect correctness)

**Location:** §6 ¶2, the Chatterjee–Saona–Ziliotto sentences.

**Problem.** The cited content is not included, and I have not checked it from memory. Specific risks:
- **(a)** "Their approximation decision problem" is never defined.
- **(b)** The undecidability may be an earlier result that the paper cites rather than proves, so the attribution needs checking.
- **(c)** The cited paper's average criterion is not named. This is harmless here because all criteria coincide, but it should be said.
- **(d)** "Complements their careful use of a supremum rather than a maximum" ascribes intent and asserts a relationship that the note does not show.

**Repair.**
- Quote theorem numbers and exact statements, including the objective.
- Attribute undecidability as the cited paper does.
- End with: "The example is consistent with the cited ε-optimality result: ε-optimal finite-memory policies exist here, and ε > 0 cannot in general be replaced by 0."

### 6. The §3 reduction is informal in three places — Minor

**Location:**
- §3 ¶1 ("Realize all private randomization on a seed R…");
- §3 ¶2 ("P(H is reached | N=n)").

**Problem.**
- **(a)** "Admissible policy" is never formally defined.
- **(b)** The seed realization relies on an unstated coupling lemma: the realized process must have the same law as the canonical Ionescu–Tulcea process.
- **(c)** The expression conditions on {N=n}, which may have probability zero.

**Repair.**
1. Define policies as kernels π_t(·|h_t), together with mixtures of such policies.
2. Replace the coupling with a direct computation. Write h_t^W for the all-W history of length t, and p_t := π_t(C | h_t^W); this is a fixed number because that history is the only one possible before the first C. The chain rule then gives:
   - P(N=n, X_n=B) = qⁿ·p_n·∏_{t<n}(1−p_t) = qⁿ·P(N=n);
   - P(N=∞) = ∏_t(1−p_t).
3. Mixtures follow by linearity.
4. State results as joint probabilities rather than conditional ones.
5. Note that the argument does not need the policy to recall its own actions.

### 7. Two sentences in §4–§5 claim more than they show — Minor

**Location:**
- §4 ¶4 ("There is not merely a failure at the endpoint: every policy has a strictly better policy");
- §5, final sentence ("compactness … does not imply continuity").

**Problem.**
- **(a)** "Every policy has a strictly better policy" is logically equivalent to the supremum not being attained, so it adds no new claim. What is genuinely extra is the explicit, uniform improvement map: prepend one W, which gains (1−q)·E[q^N; N<∞] and costs one memory state.
- **(b)** Compactness never implies continuity, so the sentence is malformed. The precise fact is that J is not upper semicontinuous at c=0: lim_{c↓0} J(c) = 1 > 0 = J(0).

**Repair.**
- For (a), restate the claim as the explicit improvement map.
- For (b), state that J is strictly decreasing on (0,1], because d/dc [c/(1−q+qc)] = (1−q)/(1−q+qc)² > 0, and is not upper semicontinuous at 0. Hence the Weierstrass extreme-value theorem does not apply.

## What is settled

Everything here is proved without reference to the source. Items marked † are extensions I verified; they are not in the note.

1. Under expected long-run average reward, consider the blind POMDP with 4 states, 2 actions, 1 observation, q = ½, rewards in {0,1} and a known initial state. In it:
   - every randomized history-dependent policy has a well-defined value;
   - † the set of achievable values is exactly [0,1), by mixing W^nC with never-commit;
   - the supremum 1 is not attained;
   - the deterministic (n+1)-state controller W^nC is 2⁻ⁿ-optimal;
   - every policy with P(N<∞) > 0 is strictly improved by prepending a W, and never-committing policies are improved by WC.
2. The same nonattainment holds:
   - under every lim/liminf/limsup variant;
   - † under the success-probability criterion and the Abel mean, and no Blackwell-optimal policy exists;
   - † within the randomized memoryless, randomized fixed-size, deterministic open-loop and deterministic belief-stationary classes.
3. On the class of all finite POMDPs, no map, computable or not, returns an average-optimal policy for every instance. "Maximum" must be read as "supremum" there.
4. For this instance the obstruction comes from what the agent can observe: with readiness observed, the same dynamics attain 1.

## What is not settled

1. That this instance lies inside the article's model as printed. This needs a verbatim quote and a check of standing assumptions.
2. Any methodological question the article poses. Only its presupposition that an optimizer exists is refuted.
3. Existence of optimizers under ergodic, unichain, communicating or mixing hypotheses. The example violates all of them.
4. Pathwise worst-case criteria, where every policy is optimal, and finite policy classes, where a maximum is trivially attained.
5. Computational questions:
   - deciding whether an optimal policy exists for a given finite rational POMDP, and constructing it when it does;
   - the complexity of ε-optimal synthesis and of value approximation;
   - continuous-state models.
6. **Novelty and priority.** I draw no conclusion, and the note's disclaimer is appropriate. Structurally, the belief MDP here is a countable-state stop-or-continue problem. A literature search should therefore start with countable-state average-reward MDP nonattainment examples, and with blind POMDPs and probabilistic automata.

`★ Insight ─────────────────────────────────────`
- **Why randomization and memory cannot help.** The whole problem reduces to choosing a law μ for the commit time N on {0,1,…,∞}. The value is linear in μ: J = ∫f dμ, with f(n) = 1−qⁿ and f(∞) = 0. Over all probability measures, a linear functional of this kind has supremum sup f, and it is attained only by measures concentrated where f reaches its supremum. Here f never reaches 1, so no μ attains it. That one line explains both the nonattainment and why the value set is exactly [0,1).
- **Why a finite POMDP can lack an optimizer when a finite MDP cannot.** Finite MDPs always have average-optimal stationary policies. A finite POMDP, however, induces an infinite belief MDP. Here its beliefs 1−qⁿ approach 1 without ever reaching it, and that infinite belief space is where attainment fails. Making readiness observable collapses the belief space back to finitely many states, which is why the fully observed version has an optimizer.
`─────────────────────────────────────────────────`