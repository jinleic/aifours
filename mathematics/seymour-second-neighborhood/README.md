# Seymour's second-neighborhood conjecture — superseded intake

## Source

Book: 《10000个科学难题·数学卷》, Science Press, 2009. Problem: 西摩 (Seymour) 的二阶邻域猜想 / *Seymour's Second Neighborhood Conjecture*. Author: 李学良 (Xueliang Li). Printed pp.417–418; PDF pp.433–434. Exact extraction: [`sources/book-excerpt.txt`](sources/book-excerpt.txt).

## Problem

Every nonempty finite oriented graph (no loops or opposite arcs) has a vertex v with |N++(v)| >= |N+(v)|, where N++ consists of vertices at **exact directed distance two**, excluding v and its first out-neighbors. Sinks satisfy the inequality. No connectivity or degree restriction is part of the full conjecture.

## Status as of 2026-10-14

**Claimed solved by OpenAI/math family 173, September 23, 2026; not re-verified by Comparator in this intake.** This is not a valid still-open replacement for the five-problem selection.

The initial primary status source, Bai–Li–Park, [arXiv:2607.18047](https://arxiv.org/abs/2607.18047), July 20, 2026, explicitly says the general conjecture remains open. A more targeted current search located the later primary [OpenAI family-173 scope document](https://github.com/openai/math/blob/main/lean/docs/173.md) and accompanying *A proof of Seymour's second-neighborhood conjecture*, dated September 23, 2026. Its Theorem 1.1 asserts the full result, superseding the July source as evidence for selection.

A source snapshot from existing local openai/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` is saved under [`sources/openai-math-adc7f1241/`](sources/openai-math-adc7f1241/). [`evidence/openai-snapshot.json`](evidence/openai-snapshot.json) records 58 file hashes, including the paper, solution source modules, scope document, and Comparator challenge/configuration.

The challenge `ComparatorChallenges/SeymourSecondNeighborhood.lean` explicitly quantifies over a nonempty finite type and a loopless asymmetric relation. Its second-neighbor definition excludes the source and first neighbors and requires a two-step path. Thus **the statement scope matches the full book conjecture**, not just degree seven/eight or a dense special case. The solution root is `OAI.Combinatorics.SecondNeighborhood.Main`; the config permits only `propext`, `Quot.sound`, and `Classical.choice`. The `sorry` in the trusted challenge is its expected template body, not an inspected solution proof gap.

**No Lean build, Comparator execution, axiom audit, or fresh-kernel replay was completed here.** The claim's formal verification is not inferred from its README or the absence of textual `sorry` matches. Parent explicitly stopped this intake before those runs.

## State of the art at the superseded entry route

Opened primary sources, retained only as historical context:

- [arXiv:2412.20234](https://arxiv.org/abs/2412.20234), Huang–Peng: universal ratio 0.715538 in its abstract.
- [arXiv:2606.30588](https://arxiv.org/abs/2606.30588), Sadhukhan–Sandeep–Sen: claims minimum outdegree seven using local reductions and CP-SAT infeasibility checks.
- [arXiv:2608.11530](https://arxiv.org/abs/2608.11530), Brukhman: claims the dense case n <= 2δ+2.
- [RyanChimienti/seymour-eight](https://github.com/RyanChimienti/seymour-eight) also claims a Lean degree-eight result **conditional on degree seven**; its theorem signature was opened. It is neither the full result nor a reason to treat degree eight as untouched.

## Attack

Only source intake, exact theorem-scope comparison, and preliminary reading were performed. No degree-eight solver work was started. An isolated APFS copy of the existing Lean build was prepared at `/tmp/seymour-lean-20261014-68365`, but no verification command was run in it. The unused review prompt is retained as `evidence/openai-review.prompt.txt`; it was **not submitted to a delegate**.

## Claims

| Claim | Status | Evidence |
|---|---|---|
| Family 173's trusted statement matches the full book conjecture | PROVED | Source-level comparison of book excerpt, `Model.lean`, challenge, and scope document in pinned snapshot |
| This intake freshly kernel-verifies the full theorem | REFUTED | No such run occurred |
| July 2026 open-status wording suffices to certify October open status | REFUTED | Later September 23 primary full-proof claim |

## Independent review

No delegate review was run for this superseded intake. The parent independently identified the same local family-173 files and directed a scope-limited handoff. This is not presented as mathematical verification of the claimed proof.

## Next steps

Do not count Seymour among five still-open targets or resume obsolete degree-eight work. Parent replaced it with **非可对称化的卡茨–穆迪代数的定义关系问题**, book pp.226–227, tracked separately in `../kac-moody-serre-relations/`. Any future claim that the Seymour proof is independently verified requires its own explicit Comparator/kernel acceptance record.
