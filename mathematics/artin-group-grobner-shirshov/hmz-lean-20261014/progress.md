# Artin question (3): HMZ, Lean and reduced-basis audit — 2026-10-14 PT

## Status, without conflating proof levels

- **Original question (3), written mathematics:** Theorem G remains a complete written construction of a generally non-reduced rational GS basis on the atoms plus Delta±1, for every finite Coxeter system with N=length(w0)>=2 and every atom order under Delta^-1<Delta<S deglex. This run and its actual HMZ reviewer found no gap in that N>=2 argument. Rank one uses the existing three-rule basis. The previously omitted literal empty system is handled below.
- **Original question (3), all-type Lean certification: NOT COMPLETE.** No theorem in this package instantiates the necessary background laws for every actual finite-type Artin monoid/group. No polynomial Composition-Diamond/GS theorem over arbitrary fields is formalized here. All 82 claim-ledger entries retain `full_goal:false`.
- **HMZ acceptance: NOT ACCEPTED.** The sole actual reviewer returned `done:false`; the terminal event is `ended how:stopped`, after the required 3600-second limit (process rc143). Kernel-checked partial progress does not change that verdict.
- **Compact reduced B4/F4 templates: NOT SUPPLIED.** Two natural shortcuts are now explicitly rejected by exact finite witnesses. This is not a proof that rational reduced templates are impossible.
- The book contains seven questions. Only (3) is addressed. None of the other six is claimed solved.

## Frozen HMZ record and post-run ownership

Frozen baseline: `e757f04c146039059a28726cbb977326f48387d9`. TASK.md and verify.py hashes remained unchanged. The sanctioned shared runner invoked scripts/hmz-run.sh with `--timeout 3600`. The pairing was codex/gpt-6.1-sol:max and claude/claude-opus-5-5:max, from the shared pairing file; installed HMZ revision `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a`, official flowverse `2c37d06df3e356807adb93b5a9fdca170a5d0be8`. Full-access permissions are not an OS sandbox.

The run started 12:21:13 PDT and stopped 13:21:13 PDT on 2026-10-14, elapsed 3600.408311 seconds. `hmz-evidence/process.json`, the copied epic/resume journals and wrapper.log retain the actual execution evidence. The reviewer independently replayed the first 57 claims and the original dropped-output negative control, confirmed their statements and permitted axioms, and returned `done:false` because the all-type Artin and GS conclusions were missing.

The second actor turn added full-word coverage and normal-form lemmas but was interrupted with two recorded elaboration errors. Its source is preserved as `attempts/timeout-Formal.lean`, its diagnostics in `attempts/p1-002.log`, and the reviewed source/ledger/logs in `attempts/review-baseline-*`. After the process stopped, the owner repaired the two errors, completed the actual-rule conditional joining/normal-form/confluence chain, and added a noncommutative mutation control. Successful incremental evidence is `attempts/owner-003.log`. **These 25 additional claims were not reviewed by the stopped HMZ reviewer.** Parent independent replay is a separate acceptance step. The process snapshot at 20:22:06 UTC found no matching surviving Artin HMZ/actor/reviewer/Lean processes.

## What Lean proves

Words are genuine `List (Letter S)`, with `Letter` containing exactly atom, Delta and inverse constructors. Simple elements occur only as state indices. `ComplementTable` stores data, not validity, normality, completeness or GS fields.

1. `ComplementTable.telescoping`: for every input word, residual e and local complement table, the ordered output product satisfies `value(e) * eval(output) = eval(input) * value(final residual)`. The local evaluation/complement balance hypotheses are explicit. `accepted_output_equality` includes the initial x/q complement and proves the actual emitted identity; `join_accepted_output_equality` connects it to u^-1(join u v), with explicit reduced-lift and prefix-length laws.
2. `output_length_balance`, `accepted_output_length`, `atom_rule_decreases`, `delta_rule_decreases`, and `gStep_finite_wellFounded` establish strict deglex decrease and termination of the actual infinite GRule family in arbitrary contexts. Delta extraction shortens length by N-1; lower-atom targets preserve length and decrease the initial atom.
3. `complement_divides_iff` derives the divisibility equivalence from a genuine universal left-lcm property and cancellation. `residual_divisibility`, `acceptance_iff_divides`, and `target_firstHit` iterate it without a word-length bound.
4. `minimal_positive_rule_coverage` proves coverage rather than assuming it. The post-run `Completeness.positiveNormal_atom`, `positive_normal_of_irreducible`, `irreducible_shape`, and `irreducible_normalForm` discharge the singleton and non-positive-pattern steps. `PositiveNormal` uses actual least representatives and Delta-freeness.
5. `Completeness.conditional_equal_iff_join`, `conditional_irreducible_iff_nf`, and `conditional_confluent` now prove end-to-end completeness of this **specific** rule family under the following explicit hypotheses: finite linearly ordered atoms; a left-cancellative positive monoid and group-valued monoid map; local evaluation and length laws; universal simple lcms and no nonidentity simple divisor of one; positive generation and homogeneity; atom injectivity; involutive Delta twist; and G5 uniqueness of Delta^k p for Delta-free p. G5 existence is not assumed: termination and coverage produce normal forms. Neither local joining nor GS completeness is an assumption. Nevertheless, the background hypotheses have **not been instantiated for every actual finite-type Artin group**, so this is a conditional bridge, not Theorem G's full Lean proof.
6. `Path`, `output_append` and `firstHitDFA_correct` formalize correlated input/output paths and the first-arrival acceptor. Finite E yields finite Option E states. They do not establish rationality of reduced output normalization.
7. `CommutingExample` proves actual four-state complement laws in Multiplicative(Nat×Nat) and the infinite loop family a^(n+1)b -> Delta a^n for every n. This is not a formal isomorphism to an Artin presentation or a simultaneous instantiation of all completeness hypotheses.
8. `EmptySystem` proves termination, reduction to the empty word, unique irreducibles and confluence for the rank-zero alphabet with the two erasing rules. `NoncommutingControl` proves a braid relation, correct concrete output and wrong-output inequality in S3; this is an order-sensitive rejection model, not an all-A2 GS theorem.

Every one of the 82 theorem declarations has an actual printed statement and transitive axiom list in `lean.log` and `claims.json`. The axiom union is exactly `{propext, Classical.choice, Quot.sound}`. No sorry/admit/new axioms/native_decide/custom metaprogram escapes are used. Exact source hashes, imports, statements, assumptions and source lines are in the ledger. No Comparator, external kernel or sandbox acceptance is claimed.

## Empty-system boundary correction

If “every finite Coxeter system” includes S empty, then W={1}, N=0 and Delta=1. On the formal letters Delta^-1<Delta the reduced basis is `{Delta -> epsilon, Delta^-1 -> epsilon}`. Every nonempty word contains a leading letter and reduces to epsilon; both rules decrease length. This closes the written boundary omission without applying the N>=2 transducer outside its scope. Rank-one A1 remains the separate existing three-rule basis. Neither trivial case is used to claim the N>=2 problem solved in Lean.

## Two meaningful Lean rejection controls

`NegativeControl.lean` deliberately contains two false theorems:

- **Lost output:** on the accepted commuting path starting at b and reading a,b, deleting every emitted block asserts aab=Delta instead of aab=Delta a. Multiplicative(Nat×Nat) distinguishes (2,1) from (1,1). Three preceding true controls establish balance, acceptance and correct output.
- **Reversed blocks:** the A2 path with residuals `ab,b,ba,ba,a,1` and emissions `epsilon,ab,b,epsilon,epsilon`, after initial output `aba`, gives `baaaba -> abaabb`. Reversing the two nonempty blocks yields `ababab`. The transpositions (01),(12) in S3 satisfy aba=bab, validate the correct output, and reject the reversed one. This detects order corruption invisible to a generic commutative length check. The source proves two true quotient controls before the deliberate failure.

The final negative run must fail at exactly these two wrong conclusions, with no setup/import error or sorryAx in the five true-control axiom prints. Historical failed setup controls remain preserved in scratch attempts and are not counted as acceptance.

## Reduced B4/F4 audit

Use a<b<c<d corresponding to [s1,s3,s4,s2]. `reduced_filter_control.py` independently enumerates complete homogeneous braid classes of four short words and reads all outputs for those inputs from the existing paired graphs; it imports neither the transducer compiler nor the Garside oracle.

| type | minimal nonnormal input | sole current output | smaller equivalent output |
|---|---|---|---|
| B4 | dabda | bdbad | bdabd |
| F4 | dbcdbc | bdbdcb | bdbcdb |

Both maximal proper factors are lex-minimal in their complete braid classes and shorter than Delta (N=16/24), hence normal by the existing Lemma 2. Removing rules whose right sides are nonnormal deletes the only rule for these minimal nonnormal inputs. Lemma 1 therefore rules out this pruning shortcut as a GS basis.

Commutations alone also do not suffice: B4 admits `daabbdabd -> adaadbdaa`, whose right side has no commuting move but has the decreasing braid move `adaadbdaa -> adaabdbaa`; F4 admits `dabdabdb -> bdbdadbd`, with no commuting move but `bdbdadbd -> bdbadabd`. The certificate retains whole positive braid classes, proper-factor classes, source hashes and exact emitted outputs. These finite obstructions do not supply compact reduced bases or prove their nonexistence.

## Reproduction and exact remaining work

Run the integrated `reproduce.py`; it invokes the byte-identical frozen checker from this directory, then the finite reduced-strategy controls, and audits that the negative errors are exactly the two expected rejected theorems. It uses the existing read-only cached Lean project, never a corpus rebuild. Lean runtime: 4.34.1, arm64-apple-darwin24.6.0, commit 5045d0056413266e57c625dcd7c365b10e377c52. Expected patched-dependency warnings are retained.

The next exact missing full-goal step is an actual all-finite-type Artin instantiation of the now-formal conditional completeness theorem, especially weak-order joins as positive lcms and G5 uniqueness. The local OAI sources contain relevant cancellation, generation, grading, positive-lift and spherical-lcm theorems but were read as references, not imported/replayed. A separate polynomial Composition-Diamond bridge remains. Compact reduced B4/F4 descriptions are still a stronger independent problem. `references.md` records applicability and non-applicability; no corpus title is being substituted for these missing proofs.
