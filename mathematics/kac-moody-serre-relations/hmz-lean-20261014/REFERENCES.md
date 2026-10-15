# Audited local references and dependency evidence

Date: 2026-10-14. All listed corpus and dossier files were read-only.
No theorem in the local OAI corpus was imported or counted as an accepted
result merely because a file or topic name looked relevant.

## Hash-bound ledger

[source-evidence.json](source-evidence.json) records the exact absolute paths
and SHA-256 hashes of the audited inputs, direct Mathlib source files,
corresponding compiled objects, and the new structural arithmetic artifacts.
Its SHA-256 is

`52cab6bf3d8372255004d2b54f6006c968e59c96c0f4c709c4d8f140e0faf5d2`.

The full written structural argument, STRUCTURAL.md, has SHA-256
`94b8b1fe14dea85f06ed27dc3f7aff07dbb9b5d8d2296f8302d143223e659694`.

All frozen/read-only input hashes were rechecked without changes. The
important corpus and dossier source hashes are:

| Input, relative to /Users/jinleic/jinleic-workspace | SHA-256 |
|---|---|
| ai4s/kac-moody-serre-relations/README.md | f2caf3fb8fbc6d0d03b6a77d13fff87dcc40e8a91e2362bd0660a1a5be9bd3da |
| ai4s/kac-moody-serre-relations/proof.md | 87434c71647ca06737fdd6b9bfefa924f42d7499f87f8e5c2868b34e01493dd9 |
| ai4s/kac-moody-serre-relations/evidence/round2-coefficient-two.md | 82630f6bc98b8b9d1bfcc3d8882cafee8e62264a0a4defa6aaf174185e180473 |
| ai4s/kac-moody-serre-relations/evidence/round2-uniform/report.md | ba45df2b217fc9d8a83c70851b8db9eb237aba0b739824be0ba11d7770032a02 |
| ai4s/kac-moody-serre-relations/evidence/round2-uniform/parent-independent-check.json | 7275abb3ecfc9b8c0efc4c437274229cec6be4245ae5674d69ef79df7b48c44d |
| math/lean/docs/008.md | 45829bd7e8ea32a33fe881d5168307b2cd03dd50f4a5b34f0659f1211a6622e0 |
| math/lean/ComparatorChallenges/DeligneDrinfeld.lean | b2fc1de28eb29eb1e8934f52978a64a1cd9fc13f3b4379e84171d4f8a106e3cd |
| math/lean/OAI/Algebra/Drinfeld/Foundations.lean | cf89211f03a17d8a9d990d4a3797e06ef3ae5a78c67bf2e9ad3906abb1c6d8d2 |
| math/lean/OAI/RingTheory/Multiplicity/ExactSequenceTransport.lean | 004990e86aec075b478278998751ca9c50ded94e8b5b040d585673dfe6f7ed9e |
| math/lean/OAI/Combinatorics/StripMass/SchurIdentity.lean | ad9fe9954180ea01f46b4c0f7a841a3f1f17706ae414ea6c985479f2e0c83ef8 |

Frozen scratch files retain:

- TASK.md: `ad36b51623ceda838d94de5fc05a26ab3114664ca478cd85948698cc351cad60`.
- verify.py: `8ac9cef6a5be5e3547e745a625888b80d0a0ea06df7ea3a58521a761a3fddf46`.

The frozen final receipt separately hashes Formal.lean, NegativeControl.lean,
claims.json, REPORT.md and this file. The explicit hash of the source ledger
above binds its additional references and arithmetic results into this
receipt's documentary chain. This is evidence binding, not a proof that the
universal mathematics has been accepted.

## The actual applicability of family 008

Exact paths:

- `/Users/jinleic/jinleic-workspace/math/lean/docs/008.md`.
- `/Users/jinleic/jinleic-workspace/math/lean/ComparatorChallenges/DeligneDrinfeld.lean`.

The topic is the Deligne–Drinfeld conjecture for the rational
Grothendieck–Teichmüller solution Lie algebra with the Ihara bracket, freely
generated in odd weights and completed by weight. It is **not** the
Gabber–Kac conjecture. The document states its own scope; those statements
were not independently accepted here.

Audited symbols in `OAI.DeligneDrinfeld`:

- `L := FreeLieAlgebra ℚ Bool`, `eval := FreeLieAlgebra.lift`.
- `braidIdeal := LieSubmodule.lieSpan ℚ BraidFree braidRelations`.
- `T4 := BraidFree ⧸ braidIdeal` is an actual Lie quotient, with
  `LieSubmodule.Quotient.mk` for its generators.
- `WeightedWord` has genuine generator and bracket constructors;
  `weightPiece` is the Submodule.span of those words.
- `D` and `ihara` use the tangent lift, not Chevalley lowering.
- `MainStatement` concerns that graded/completed Ihara algebra.
  The challenge `main` has an unfinished body. It is not an accepted result
  and supplies no theorem for Serre equality.

Transferred: the distinction between a genuine free Lie presentation,
an actual generated ideal/quotient, and explicit weighted spans. No symbol
or challenge theorem from this file is a dependency of Formal.lean.

## Free-Lie universal properties and bracket induction

Exact path:

`/Users/jinleic/jinleic-workspace/math/lean/OAI/Algebra/Drinfeld/Foundations.lean`.

The audit read the relevant definitions and proof bodies, including the
following exact symbols and ranges:

- `OAI.DeligneDrinfeld.freeLie_induction` at the start: for a commutative
  scalar ring, a predicate closed under zero, generators, addition,
  scalar multiplication and bracket is made a LieSubalgebra. A map from
  the free Lie algebra into that subalgebra is constructed with `lift`;
  `hom_ext` and the inclusion identify its composition with the identity.
- `OAI.DeligneDrinfeld.braidIdeal`: an actual LieSubmodule.lieSpan ideal,
  rather than an imposed dimension equality.
- `OAI.DeligneDrinfeld.BraidModel.ideal_le_ker`, lines 756–768 in the
  requested 746–780 region: generator relations are killed by the actual
  Lie homomorphism preMap, and `LieSubmodule.lieSpan_le` propagates this to
  the generated ideal. This proves containment, not injectivity of a
  general quotient or triviality of its maximal ideal.
- `OAI.DeligneDrinfeld.BraidModel.map`, lines 770–776: `liftQ` needs
  ideal_le_ker; its Lie-homomorphism field is checked by quotient induction
  on representatives. A quotient map does not itself identify the kernel.
- `OAI.DeligneDrinfeld.IntegralWords.kill_lie`, lines 2307–2319:
  `LieSubalgebra.lieSpan_induction` checks generators, zero, sums, scalars
  and brackets to show that the named associative deletion map preserves
  rationalLie. This deletion map is not the contragredient lowering D_i.

Transferred: closure-by-bracket induction, generated-ideal minimality,
and the need to verify a map kills generators before descending it. The
formal implementation uses the corresponding **Mathlib** APIs directly.
It proves the Jacobi stability step and an inductive generator closure;
it imports neither this file nor its large closure. The requested portions
were not compiled or axiom-audited here, and their main result is not
assumed to solve the frozen problem.

## Exact sequences and base change

Exact path:

`/Users/jinleic/jinleic-workspace/math/lean/OAI/RingTheory/Multiplicity/ExactSequenceTransport.lean`.

Audited symbols:

- `OAI.Lech.ModuleSequence.transport` requires A a commutative ring,
  the relevant additive groups and A-module structures, linear equivalences
  on all three terms, two commuting squares, injective f, exact f,g and
  surjective g. It transports these **given** properties to f',g'.
- `OAI.Lech.ModuleSequence.baseChange` requires a commutative A-algebra B,
  **`Module.Flat A P` on the quotient/end term P**, injective f,
  exact f,g and surjective g. It invokes the matching tensor exactness
  and flatness lemmas to preserve a given sequence.

Transferred: exactness and injectivity must be premises of a transport;
flatness hypotheses cannot be omitted. Over the field Q scalar extension
to C preserves the finite rational calculations with the appropriate
algebraic interpretation. Neither result proves the missing injectivity
in all degrees. No code from this file is imported or asserted to have been
kernel-checked in this run.

## Pfaffian/Schur identities and explicit nonvanishing premises

Exact path:

`/Users/jinleic/jinleic-workspace/math/lean/OAI/Combinatorics/StripMass/SchurIdentity.lean`.

Audited symbols in `OAI.StripPfaffian`:

- `pfaffian_schur_even` assumes Even n, x : Fin n -> C,
  every x_i+x_j nonzero, and Function.Injective x. Its induction explicitly
  transports these hypotheses to the smaller matrices and new coordinates.
- `pfaffian_schur_odd_snoc` additionally requires every x_i+a nonzero;
  it performs its elimination using the named Schur-complement identities,
  a nonzero unit pivot and the stated denominator hypotheses.
- `pfaffian_schur_odd` transports those premises on splitting the last
  coordinate, rather than silently asserting them.

Transferred: elimination must carry its nonzero-denominator premises and
the exact matrix identity. Not transferred: any positivity or injectivity
statement for the Serre lowering matrix. This is a different complex
matrix family. Its import of InverseIntegrability and all later strip-mass
results are outside this task and were not imported into Formal.lean.

## Existing Kac–Moody premises and producer/checker distinction

Exact source root:

`/Users/jinleic/jinleic-workspace/ai4s/kac-moody-serre-relations`.

README.md supplied the exact full-realization target and the accepted scope
ledger. proof.md §§2–4 supplied the row-correct lowering formula, radical
recurrence and positive Serre ideal generated-span recurrence. §§7–8 supplied
coefficient-one equality and the primitive-weight condition. §§10–11 supplied
the coefficient-band lemma, the actual A(r,s) slice presentation and omitted
lowering criterion; §14 preserves the unbounded gap. The later finite
sections were read without repeating their computations.

round2-coefficient-two.md was read in full. Its sl3 module, exterior-square
decomposition and original D3 formulas are premises of the new written
structural consequence and controls for the new local map computation.
Its warnings about the changed omitted row, two occurrences of f_i,
and the nonzero Levi-lowest z vector were retained.

round2-uniform/report.md was read in full. It is a producer inventory and
explicitly says its worker did not run an independent checker. The separate
existing `evidence/round2-uniform/parent-independent-check.json` was then
read and hash-bound. Its actual flags are uniform_height7=true,
uniform_height8=false, and its scope is conditional on the written
reductions and previously accepted height-six premise. Neither checker nor
certificate campaign was replayed here. A producer success is not promoted
to independent acceptance.

The new producer level4_invariant_check.py uses rational matrix models and
recursive brackets. The separately written check_level4_invariant.py reads
no producer code and uses associative word deletion. It independently
supplies a bracket expression from the saved tensor and verifies every
affine image coefficient. These tools concern one level-four map, with
no assertion about all primitive summands or the universal equality.

## Actual imports and compiled dependency usage

The cache is exactly

`/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`.

The toolchain file specifies `leanprover/lean4:v4.34.1`. Every elaboration
uses `/Users/jinleic/.elan/bin/lake env lean` with that cwd and an absolute
scratch-source path; no lake update or full build was run.

Direct Formal.lean imports:

- Mathlib.Algebra.Lie.Ideal: actual Lie ideals and Lie-module span infrastructure.
- Mathlib.Algebra.Module.Torsion.Free: scalar-zero cancellation at a nonzero vector.
- Mathlib.Tactic.Ring: kernel-producing coefficient identities.
- Mathlib.Data.Nat.Find: least vanishing-string index infrastructure.
- Mathlib.Data.Nat.Order.Lemmas: the last-nonzero/first-zero string lemma.

The last module also imports Nat.Find; the explicit Nat.Find import is
redundant but points to the same prebuilt module. Lean's built-in omega
tactic handles the strict predecessor inequalities in strong induction.

Direct NegativeControl.lean imports:

- Mathlib.Algebra.Lie.Matrix.
- Mathlib.LinearAlgebra.Matrix.Notation.
- Mathlib.Tactic.NormNum.
- Mathlib.Tactic.FinCases.

The direct source paths are under the cache's
`.lake/packages/mathlib/Mathlib/...`; their corresponding compiled objects
are under `.lake/packages/mathlib/.lake/build/lib/lean/Mathlib/...`.
source-evidence.json gives the exact paths and both source and object
SHA-256 hashes for each of these nine consumer/import entries.
Formal.dependencies.log is the actual output of `lake env lean -j 2 --deps`
for Formal.lean, with the direct compiled paths and expected patched-package
warnings. It is not claimed to be a kernel verification of every transitive
library theorem. The successful root axiom prints independently describe
which logical axioms the claimed results actually use.

No OAI, ComparatorChallenges, local copied module, replacement import,
custom metaprogram or proof escape is present in the checked source. The
only logical axioms appearing in claimed roots are propext, Classical.choice
and Quot.sound, with each root's exact list in claims.json and the Lean logs.
The initial missing-import error and the mathematical negative control's
original failed output remain in their incremental logs. Comparator and
nanoda were not run. All arithmetic scripts use Python's standard library.


## Complete level-four continuation and diagonal lemma

The separately written level4_cells_producer.py and level4_cells_check.py
use the previously bound recursive and independent tensor helpers,
respectively. The checker imports no producer. Its receipt binds both new
scripts, their exact certificate and both helper sources. It independently
rebuilds all Lie and primitive spaces and all four positive determinant
polynomials. The source ledger includes all four new artifact hashes.
The degree-four theorem retains the already audited earlier-level premises.
The diagonal-specialization lemma uses the existing symmetrizable theorem,
the explicit symmetrizer (t,t,1), and the exact radical recurrence. It applies
only while omitted-node Serre exponents exceed the level, and supplies no
all-level assertion for a fixed matrix. No new corpus file was imported,
modified, downloaded or assumed to settle the universal target.
