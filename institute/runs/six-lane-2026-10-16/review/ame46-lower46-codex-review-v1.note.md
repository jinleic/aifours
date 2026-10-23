VERDICT: ACCEPT-WITH-FIXES

- **MINOR — [S/review/SUPPORT_LOWER46.r1.md:21](ame46-lower46-parent-inputs-v1/review/SUPPORT_LOWER46.r1.md:21): verification provenance.** The worker checkers share an author and semantics; their agreement is overstated as independent validation. In r2, distinguish them and cite the parent’s addition-only RUP replay. That replay bypasses this limitation.
- **MINOR — [S/code/large_t_gen.py:241](ame46-lower46-parent-inputs-v1/code/large_t_gen.py:241): certificates discarded.** The engine records phase booleans without the obstruction vectors. P supplies the missing explicit evidence, and all 24 certificates check. Pin P’s table, checker and result in r2’s executable record.
- **MINOR — [S/code/large_t_gen.py:18](ame46-lower46-parent-inputs-v1/code/large_t_gen.py:18): stale method description.** It describes an exact SymPy LP, whereas execution uses floating candidate search followed by exact rational verification. Correct the summary and identify the obsolete routine as unused. No actual exclusion uses moduli, so this has no mathematical impact here.

## Established scope

No fatal or major mathematical defect found.

The imported Lemmas 1–11 and cases t=33–36 withstand review. Lemmas 12–16 are sound: the spin-flip proof covers arbitrary complex states; the t=32 restriction has squared norm 1/9, so multiplying by 3 normalizes it and gives unitary reshapings `2ω = 6ψ`. The t=31 contradiction and complete t/e case table are correct. Local-unitary invariance supplies the quantifier over **every product orthonormal basis**.

The finite bridge preserves every true state:

- Deficits have parts ≤6 and at most six parts. Coordinate and value normalizations are legitimate permutations.
- A true N supplies hole indicators, prefix-count counter values, and overlap auxiliaries equal to the conjunction of the corresponding entries. No auxiliary constraint forbids a realizable support.
- H preserves these conditions and realizability. A subgroup suffices; missing symmetries only increase enumeration. Exact cardinality makes each orbit clause exclude precisely one support, including all its auxiliary assignments.
- Actual T satisfies the completion CNF: it avoids hole lines and meets every other line exactly once. Thus UNSAT is a sound exclusion.

All 24 phase certificates use genuine 2×2 components. Orthogonality forces each alternating phase form to equal π modulo 2π, without assuming equal moduli. Their signed sums vanish identically while their right sides sum to an odd multiple of π. Orientation reversals merely negate a congruence, preserving the contradiction.

I also independently recovered written exclusions for all four completion representatives: the profiles with value-set sizes `(2,3,3,3)` and `(3,3,3,3)` give negative second-order counting bounds −3 and −6; `(2,4,4,4)` requires four binary length-four words at pairwise distance ≥3, which is impossible.

## Trusted imports and pending bindings

Trusted external mathematics: Tarry’s theorem, used only for t=36. Trusted computational evidence: the supplied parent verification of all 18 pinned CNFs by addition-only RUP.

**Unconditional acceptance of the computer-assisted theorem still awaits the parent’s base-CNF and orbit-block bindings.** Completion-CNF binding is also pending in that route, although the written arguments above independently cover its four exclusions. This is an evidence dependency, not a discovered mathematical counterexample.

Shared e=0 code supplies reproducibility only. Interpreter differences, obsolete moduli receipt keys and the absent CaDiCaL binary pin do not invalidate the parent’s proof-replay route.

## Exact controls run

Both support-proof hashes match the receipt; 20 non-`explore/` pins and P’s supplied hashes also match. In-memory checks passed:

- Independent capped-profile generation: **2, 1, 7** profiles for h=6,7,8.
- All **24** phase certificates, exact coverage without duplicates; three negative controls.
- **258** signed-counter projections and **340** overlap projections, exhaustively checked.
- Complex-torus controls, including a valid quarter-turn solution.

Python 3.9.6; one process; peak reported memory below 17 MiB. No solver reruns, network, delegation or file writes.

This is a model review, not peer review.