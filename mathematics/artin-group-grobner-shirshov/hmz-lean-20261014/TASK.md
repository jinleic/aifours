# Frozen Artin GS-basis task — 2026-10-14 PT

## Original goal and current baseline

The user explicitly requests HMZ + Lean + the local openai/math corpus to advance and solve the selected mathematics-volume problem. This task is ONLY question (3) of the seven-part entry: give a Gröbner–Shirshov basis of every finite-type Artin group on the atoms plus Delta and Delta inverse. Fix any total atom order and deglex Delta^-1 < Delta < S. Do not replace this with the known all-simple-element alphabet or claim the other six book questions.

Read `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/CONTRACT.md`. Read the existing target `/Users/jinleic/jinleic-workspace/ai4s/artin-group-grobner-shirshov/README.md`, `proof.md` (especially Sections 1–5 and 11–12), and `evidence/codex-uniform-review.md` before research. Those files are read-only to you.

Theorem G already has an unbounded written proof of a generally non-reduced rational GS basis, for N=length(w0)>=2. States are simple residuals e, not algebra generators. Given atom x and q<x or q=Delta, start e0=x\q, read atoms yi, set ei=yi\e(i-1), fi=e(i-1)\yi. On the first arrival at ek=1 emit:

`x y1 ... yk -> q rho(q\x) rho(f1) ... rho(fk)`.

Validity uses e(i-1)fi=yi ei, the resulting telescoping identity, and x e0=q(q\x). Lex target rules preserve atom length and decrease first letter; Delta target rules shorten X-length by N-1. Completeness follows from minimal-nonnormal-factor coverage and standard Garside divisibility. The prior proof is NOT Lean-verified. B4/F4 expressions are genuinely non-reduced; B4 has `dabda -> bdbad -> bdabd`. Compact reduced templates remain a stronger unsolved deliverable. Rank one uses the separate three-rule basis. Examine the empty Coxeter system explicitly rather than silently including it in N>=2.

## Ownership and permissions

Write ONLY this fresh Git repository `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/artin`. Do not write its frozen TASK.md or verify.py. Do not write ai4s/, math/, shared runtime, shared scripts, config, credentials, sibling directories, or outside this repository. No push, destructive Git operations, nested HMZ, additional agents/reviewer CLIs, paid runs, runtime updates, dependency downloads, or huge corpus builds. The outer process supervises the actual HMZ reviewer. Use at most two threads in any bounded solver. Preserve failed attempts and logs.

## Research and implementation priorities

1. Audit the actual Theorem G proof and its exact quantifiers. Seek a real gap and repair it, or push compact reduced B4/F4 templates rigorously. Do not simply replay the prior large certificate portfolio.
2. Produce substantive self-contained `Formal.lean` using honest List words, monoid evaluation, finite-state transitions, and the actual complement construction. At minimum prove the arbitrary-length complement-transducer telescoping bridge, accepted-output equality, and genuine word-order decrease under explicitly stated local complement/length hypotheses. Advance coverage/confluence if possible. A generic confluence theorem assuming the hard conclusion does not establish Theorem G.
3. Aim at the FULL Theorem G in Lean without baking validity, coverage, Garside facts, or confluence into a structure field that merely assumes the desired conclusion. Partial bridge lemmas are useful but explicitly partial. Never claim a theorem from its name alone.
4. Record exact local math references and applicability. Useful inspected references:
   - `math/lean/OAI/Computability/FiniteCompiler/Rewriting.lean`: `FiniteAlgebraicEnvelopes.Bootstrap.Step`, `shortlex_context`, `step_shortlex`, `steps_wellFounded`; real List words and two-sided contexts. Its `newman` assumes local joining and does not supply Artin coverage.
   - `math/lean/OAI/Topology/ArtinGroups/Coxeter/ArtinCoxeter.lean`: `HarmonicArtin.artinCoxeter_word`, `positiveLift_injective`.
   - `math/lean/OAI/Topology/ArtinGroups/Harmonic/PositiveLiftSimple.lean`: `positiveLift_simple`, `positiveLift_longest_conjugate`, `finiteArtin_positive_fraction`; correct finite Artin objects, not GS bases.
   - `math/lean/OAI/RepresentationTheory/KazhdanLusztig/Coxeter.lean`: Coxeter word products and signed inversion actions; no Artin normal-form theorem.
   - Cached Mathlib `Mathlib/Computability/RegularExpressions.lean`, `Language.lean`, `NFA.lean`: pair-labelled paths require correlated input/output concatenation, NOT independently paired projected languages.
   Inspect dependencies before importing OAI; no new large builds. Adapt short finite proofs with attribution if useful.
5. Supply meaningful Lean rejection control `NegativeControl.lean`: wrong output identity or dropped necessary local complement condition must fail for a concrete nontrivial word model. The failure must test this bridge, not an unrelated `False`.
6. Write `progress.md`, `references.md`, and `claims.json` in this repo. claims.json lists exact source filenames, every claimed theorem name, English statement, assumptions, full-goal/partial scope, mathematical novelty versus formalization, and actual printed axioms. These documents are explicitly requested deliverables.

## Lean runtime, prohibited escapes, and verification

Reuse only the already built project read-only at `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`. Installed Lean is 4.34.1. For incremental proof elaboration run from that directory:

`/Users/jinleic/.elan/bin/lake env lean /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/artin/Formal.lean`

Expected patched-dependency warnings are not errors. No lake update/build of the full corpus. Prefer narrow Mathlib imports; `import Mathlib` is cached if needed. Do not use sorry, admit, new axiom, unsafe, native_decide, Lean.ofReduceBool, implemented_by, skipKernelTC, initialize/run_cmd, custom macros/elaborators or import replacement. Permitted standard axioms are only propext, Classical.choice, Quot.sound. Each claimed theorem MUST have `#print` and `#print axioms`.

Skip broad verification mid-flight except necessary incremental Lean elaboration. After final edits execute exactly:

`python3 /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/artin/verify.py`

The checker records actual source hashes, successful Lean output, axiom audit and rejected negative control. Passing it establishes only the checked partial claims, not full mathematical completion. Do not alter it.

## Frozen acceptance and reviewer decision

Full acceptance requires a correct proof of the original all-finite-types/all-atom-orders question (3), plus a substantive Lean connection to its actual construction, a scope-exact claim ledger, and no hidden assumptions replacing the desired GS conclusion. If only conditional/partial Lean bridges are obtained, retain them and explicitly report that the full theorem has not been kernel-certified. `done:true` must not be used to pass partial progress off as a full original-goal solution; the full-goal gate includes a Lean proof of the actual GS-basis claim, not just a generic normalization theorem. Incomplete original-goal formal proof requires `done:false` even if verify.py exits zero. Reduced B4/F4 status and the other six book questions remain separately disclosed.

The only baseline commit is this frozen TASK.md plus verify.py. The parent will inspect actual HMZ journals and independently replay Lean; exit zero and timeout are not acceptance.
