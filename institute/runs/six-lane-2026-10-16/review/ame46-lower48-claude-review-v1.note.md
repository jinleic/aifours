VERDICT: ACCEPT-WITH-FIXES

I reviewed this by hand against the three supplied texts; nothing was executed and no file was inspected. There is no FATAL finding and one MAJOR finding, which confirms the parent's observation. The fix is a rewrite of the argument only; no search, CNF, proof stream or certificate changes. Lemmas 17 and 18, every written profile elimination and the s ≤ 47 table check out exactly.

## Findings

### FATAL
None.

### MAJOR

**M1 [proof error; fixable with no search change]: the engine-v2 completeness argument rests on a false clause-set symmetry (LF134–142, LF145–150).**

- **LF134–135 make a syntactic claim:** renaming the auxiliaries maps the clause set onto itself.
  - LF136–141 only show that each abstract constraint maps to a constraint of the same kind. That is a semantic statement.
  - With ordered prefix-counter auxiliaries the syntactic claim fails in general. Renaming auxiliaries keeps the number of clauses containing each point literal. A prefix counter makes that number depend on input position.
  - So a generator that moves an input of, for example, the |N| = 2h + e counter (LF139) to another position need not be undone by any renaming. The parent's observation is correct.
- **LF142 ("Sol is invariant under H") rests on LF134–135.**
  - A semantic substitute would need every encoding to be exact: its projection onto point variables must equal the abstract constraint.
  - The imported record states only soundness (LOWER46 r1 LF139: the true N extends).
- **LF145 needs X\* ∈ Sol**, which is LF142.
- **LF150 needs the step-4 checks to be H-invariant.** LOWER46 r1 LF142–143 only asserts this.

**Does the parent's repair work with no search change? Yes.** Starting from a true support instead of from Sol removes every use of LF134–142 and LF150. The repair uses only these five properties:

- **P1 (base soundness, imported).** The non-classical support of every normalized AME state with the given (t, e, profile) extends to base auxiliaries (LOWER46 r1 LF139).
- **P2 (lex soundness).** There is one total order ≤ on point assignments: the LF125–127 point order with a fixed bit polarity.
  - For each g ∈ Γ, every X with X ≤ g(X) satisfies g's clauses when g's chain variables are set to the prefix-equality indicators.
  - The chains are fresh for each generator and disjoint from the base auxiliaries.
  - Every generator is an involution, so the choice between g and g⁻¹ does not matter.
- **P3 (blocking).** The clause blocking a found Y is falsified by no base model other than Y. For the clause ∨_{x∈Y} ¬n_x this needs |N| = 2h + e in the base CNF.
- **P4 (composition).** The final CNF is exactly base ∧ Lex_Γ ∧ the blocking clauses of the recorded solutions (LF213–214, LF221).
- **P5 (generators).** Each lex constraint's variable permutation comes from either:
  - a value transposition inside one d-class (identity off V_i), or
  - a swap of two parties that carry the same partition.

The repair does not need exact encodings, H-invariance of the checks, or ⟨Γ⟩ being the full stabilizer of the normal form. Individual blocking may find several members of one orbit; that is harmless.

**Fix.** Replace LF134–150 (keep the generator list at LF129–132) with:

> **Completeness.** Fix (t, e) and a profile p. Let ψ be an AME(4,6) state with these parameters, normalized as in LOWER46 r1 §3 step 1, with non-classical support N ⊆ ΠV_i. Each g ∈ Γ is a permutation matrix on one party, or a swap of two parties that carry the same partition. So g·ψ is AME with the same s, t, e, V_i and d_{i,·}, and its non-classical support is g(N). Hence every member of H·N (H = ⟨Γ⟩) is the support of a normalized AME state with parameters (t, e, p).
>
> Let X\* be the ≤-least member of H·N. X\* extends to base auxiliaries by P1. Since X\* ≤ g(X\*) for every g ∈ Γ, it also extends to the fresh lex auxiliaries by P2. If X\* were not a recorded solution, it would satisfy every blocking clause (P3), and the final CNF (P4) would be satisfiable, contrary to its checked UNSAT. So X\* is a recorded solution. Being a true support, X\* satisfies every necessary condition of step 4, which contradicts its recorded exclusion.

The same argument without the lex constraints covers LOWER46 r1's full-orbit blocking (LOWER46 LF144–147, LF166–167). If the true N is blocked as h(Y), then Y = h⁻¹(N) is itself a true support. So the defect does not reach the imported cases, and LOWER46 r1 LF142–143 can be weakened in the same way.

### MINOR

**m1 [missing record; load-bearing for the M1 repair]: LF122, LF125–127, LF146–148.**
- The frozen text does not give the lex-leader clause schema, the blocking-clause form or the composition of the final CNF.
- LF122 defers to `ENGINE_V2_GUARD.r1.md`, which is not among the supplied texts, so P2–P5 cannot be checked here.
- Fix: write the clause schemas and a two-line proof of P2 into r2, or cite exact guard LF lines.
- The parent replay should regenerate the lex and blocking clauses from that schema with independent code. That is stronger than the receipt (LF213), which re-runs the worker's generator.

**m2 [proof record]: LF217–219, LF229–231.**
- L42-10 applies to 2×2 *components*, not to every rectangle with four corners in N.
- The negative controls test "not a rectangle" but not "a rectangle that is not closed". The record does not say whether `phase_cert.py` checks closure.
- For the 137 load-bearing certificates, all in (26,0) with e = 0, closure is automatic:
  - a found solution has 2h points;
  - for each pair, exactly Σ_a d_{i,a} = h lines meet it, each in at least 2 points;
  - so every hole line holds exactly two points, and every four-corner rectangle is a closed 2×2 component.
- Fix: state this argument, or check closure in the verifier and in the replay.

**m3 [trivial proof gaps in the two bridges].**
- Quantifier bridge: §2 never invokes the reduction from product orthonormal bases to the computational basis (L42 LF47–50). It arrives only through "§0 definitions" (LF11–12).
- Normalization bridge: LOWER46 r1 LF126–127 cites L42 §0 for "party permutations map AME states to AME states". L42 §0 covers only local unitaries, and the M1 repair uses party swaps.
- Fix: add one sentence for each.
  - A party permutation permutes the six two-party marginals.
  - Permutation matrices permute coefficients, so s, t and e are preserved and d_{σ(i),β_i(a)} = d_{i,a}.

**m4 [missing record]: LF90, LF161–168, LF181–183.**
- LF90 asserts that {3,2,2}⁴ is the only profile at t = 29 without giving a reason, yet it carries "t = 29 is impossible for every e".
  - Reason to add: parts are ≥ 2 (L42-8(a)), so |V_j| ≤ 3, and L46-12 bounds every part by 3.
- For most cases only profile counts are given. Fix: list the profiles, and name all 37 load-bearing final UNSATs with their stream SHA-256 values.

**m5 [provenance]: LF15–16.** The frozen file relies on wording in a "forthcoming" LOWER46 r2 that has no SHA-256.
- Fix: list the LOWER46 r1 LF numbers that are not relied on (for example LOWER46 LF21, "two independently written checkers"), or pin r2's SHA-256 once it is frozen.

**m6 [dependency record]: LF180–187, LF109, LF111.**
- LF185 imports "the cases imported from LOWER46 r1" without listing what is used.
- LF186 ("no completion proof … needed") is true only for the new cases. LOWER46 r1's own exclusions of (30,0) and (28,0) use completion UNSATs.
- With Lemmas 17/18, LOWER46 r1's load-bearing computation shrinks to:
  - 7 final UNSATs: {2,2,2}⁴ at (30,0), (30,2) and (30,3); and at (28,0) the profiles {4,2,2}{2⁴}³, {3,3,2}²{2⁴}², {3,3,2}{2⁴}³ and {2⁴}⁴;
  - 11 phase obstructions: 7 in (28,0) {4,2,2}{2⁴}³ and 4 in (28,0) {2⁴}⁴;
  - no completion UNSATs.
- Fix: state this narrowed import. It also narrows what LOWER46's pending review has to cover.

**m7 [editorial].**
- LF26: "(§5)" should be "(§4)".
- LF20–21: only six cases are computer-assisted. (29,3) and (29,4) are excluded in writing by Lemma 17; their runs are cross-checks.
- Notation clashes:
  - LF40–47: (F1)–(F4) clash with LOWER42's executable facts F1–F4 (L42 LF316–319);
  - LF147: e_k clashes with e and e_K;
  - LF149: "h ∈ H" clashes with h = 36 − t;
  - σ0–σ2 clash with σ in L42-11.
- LF60–63: |T ∩ {x_i = a}| = 6 − d_{i,a} holds by definition (L42 LF59); the line argument is redundant.
- LF68–69: only non-negativity is used, not evenness.
- LF100: e ≥ 0 comes from L42-4.
- Optional additions:
  - Closed form: f(α) = e2(v) − 6h − α(6Σv − 4h) + C(α+1,2)·t, with v = (|V_i|).
  - α ∈ {0,…,4} is exhaustive, because c(x) ∈ [0,4] makes each summand monotone in α outside [0,4].
  - {5,5}{2⁵}³ also has a two-line proof. The two officers with x₁ ∈ V₁ both have x_j equal to the single element of [6]∖V_j for j = 2, 3, 4, so they agree in three coordinates, contradicting L42-3.

## Established scope

**Checked by hand and correct:**

- **Lemma 17.**
  - σ1: σ1 = 6Σ|V_i| − 4h, since t_{i,a} = 6 − d_{i,a} by definition.
  - σ2: the h hole lines of {i, j} all lie in V_i × V_j (by F3 and L46-12), and every other cell there holds exactly one officer (F2). So σ2 = e2(v) − 6h.
  - The expansion of f(α) and its non-negativity for integer α are correct.
  - α = 1 is the Bonferroni inequality: t ≥ |∪ᵢ{x_i ∈ V_i}| ≥ σ1 − σ2.
- **Lemma 18.** The four officers with x₁ ∈ V₁ are words over four 2-letter alphabets. Pairwise distance ≥ 3 needs a distance sum of at least 18, but at most 4·4 = 16 is possible. Correct.
- **Recomputed values, all matching the text:**

| t | profile | v | σ1 | σ2 | f(0..4) |
|---|---|---|---|---|---|
| 29 | {3,2,2}⁴ | 3333 | 44 | 12 | 12, −3, 11, 54, 126 |
| 30 | {3,3}{2,2,2}³ | 2333 | 42 | 9 | 9, −3, 15, 63, 141 |
| 28 | {3,3,2}⁴ | 3333 | 40 | 6 | 6, −6, 10, 54, 126 |
| 28 | {3,3,2}³{2⁴} | 3334 | 46 | 15 | 15, −3, 7, 45, 111 |
| 27 | {3,3,3}⁴ / ³{3,2,2,2} / ²{3,2,2,2}² | 3333 / 3334 / 3344 | 36 / 42 / 48 | 0 / 9 / 19 | f(1) = −9 / −6 / −2 |
| 26 | {5,5}{2⁵}³ | 2555 | 62 | 45 | 45, 9, −1, 15, 57 |

- **Every other profile at t = 26–30 has f(0..4) ≥ 0.** So the written list is exactly what Lemma 17 excludes, plus Lemma 18 for {4,4}{2⁴}³, where f(1) = 0.
- **Profile enumeration.** Parts ≥ 2, summing to h, with largest part ≤ min_{j≠i}|V_j|. This gives 25 / 6 / 7 / 1 / 2 profiles for t = 26 / 27 / 28 / 29 / 30, matching LF161–168. Hence 51 − 14 written exclusions = 37 load-bearing final UNSATs.
- **The s ≤ 47 table is complete.** The new pairs are all 23 (t, e) with s ∈ {46, 47}: e = t − 26 for t = 26..36 and e = t − 25 for t = 25..36. Each row's reason is valid. L46-12, L46-13, L46-15, L46-16 and the L42 corollary are sound as used, and none depends on e.
- **Internal arithmetic.**
  - 137 = 51 + 29 + 10 + 16 + 16 + 15.
  - 1695 = 1619 + 76.
  - 28 = 20 + 4 + 4.
  - 131 = 51 + 80.
  - 37 = 24 + 3 + 4 + 4 + 1 + 1.
- **Consistency cross-check (not load-bearing).** Every completion UNSAT (76 + 4) lies in a profile that Lemmas 17/18 forbid.
- **By-products, written and valid for every AME(4,6) state:** t = 29 is impossible, and every profile listed at LF90–96 is impossible for every e.

**Conditional result.** After the M1 fix, every AME(4,6) state has at least 48 non-zero coefficients in every product orthonormal basis, subject to the open gates below.
- This is a lower bound only. It is not the minimum and does not settle the minimum-support question.
- Nothing about 59 versus 60 is established, and there is no novelty claim.

## Imports / pending evidence

**Imported and conditioned on (not re-checked here):**
- LOWER42 r2, which cites Tarry's theorem for t = 36.
- LOWER46 r1: its Theorem and §3 steps 1, 2 and 4. Its evidence rests on the parent checks you listed (18 CNFs RUP-verified, 14 bindings replayed, 24 phase obstructions machine-checked, 4 completion CNFs regenerated).
- LOWER46's Codex review has no FATAL or MAJOR finding. **Its Claude review is still pending, so LOWER48 inherits that gate.**

**LOWER48 gates still open:**
1. Parent replay of the 37 final UNSATs against independently regenerated CNFs, including binding P2–P5 and checking that auxiliaries are fresh. CNFs are not stored (LF233–234), so regeneration must reproduce the receipt's CNF SHA-256 values.
2. Parent replay of the 137 phase certificates, including the closure check from m2.
3. Confirmation from the eight reports that no guard, solution cap or time limit tripped (LF152–153, LF212).
4. One load-bearing stream passes only in skip mode (LF225–227); the RUP replay must cover it.
5. Both LRAT checkers were written by the worker (LF24–25), so their agreement shows reproducibility, not independent validation.
6. LOWER46 r2 wording (m5).

This review does not close any of these gates. It is a model review, not peer review.
