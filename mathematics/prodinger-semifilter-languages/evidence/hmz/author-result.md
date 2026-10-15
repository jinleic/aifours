# Exact semifilter Questions 2 and 3: result

Date: 2026-10-14 PT. Baseline: `9852932`.

Author completion status: **done:true**, through the written-resolution route
with a substantive checked Lean component. The Lean formalization is explicitly
partial relative to the original questions. Final verification is recorded below. This is an artifact-author assessment, not a parent Comparator or
independent-review verdict. Questions 4/5 and discovery priority are outside the
completion claim.

## Written full-goal status

[candidate-proof.md](candidate-proof.md) proves both exact questions for every finite
alphabet, including empty and unary alphabets, with no properness assumption.

- **Q2, semifilters:** `R_L = Reg` iff every member of `L` is ordinarily regular.
- **Q2, filters:** equivalently every member is cofinite; uniquely
  `L=L_U={A : A^c is a finite subset of U}` for a suffix-closed `U`.
- **Q3, both families:** equality holds iff each complementary generator from
  either family has a finite expression `K + sum_i A_i a_i B_i` using regular
  `K,A_i`, letters `a_i`, and error tails from the other complementary family.
  The finite number of terms may vary without a uniform bound. All products
  count factorizations modulo two. Criterion (12) has no generalized finite-index
  predicate on its criterion side.

The proof derives the original agreement-congruence translation, proves the
marked parity derivative identity by disjoint cuts, eliminates the finite-state
recurrence by simultaneous-state word-length induction, and proves both parity
product regularity and regular-left closure using the finite span of residual
cosets. It then proves saturation and the cross-family criterion. Filter ideal
duality, an arbitrary-infinite-complement diagonal argument, all source axioms of
`L_U`, and the improper-filter cases are included. No substantive written proof
obligation is intentionally deferred.

## Exact Lean coverage

[Formal.lean](Formal.lean) defines finite orbit using `Set.Finite (Set.range ...)`
over **all words**. Saturation is finite orbit in the quotient module; the file
proves that this equals finiteness of the actual residual-coset range. It does not
define recognition by normal form. Every addition used in the linear proof is
addition of `ZMod 2` series; Mathlib's ordinary union/product notation for
`Language` is not substituted for parity operations.

The load-bearing proof constructs finitely many state lifts and their transition
errors, taking the empty word at the initial state. The span of the state lifts
and all the finite error orbits is finite over the finite coefficient ring and
is preserved by every letter map. This proves the lifting theorem without a
normal-form or idempotence assumption. Applied to the successive quotients it
proves saturation directly. Characteristic functions and their supports connect
these results to Mathlib's `Language.leftQuotient`, its Myhill-Nerode theorem,
and `Language.IsRegular`.

The only claimed roots, each with `#print` and `#print axioms`, are:

| Root | Exact coverage |
| --- | --- |
| `Semifilter.series_regular_criterion` | The complete Q2 criterion in complementary-series finite-coset form, quantified over ordinary languages and ordinary regularity. |
| `Semifilter.series_saturation` | `C(C(V))=C(V)` for actual series residual cosets. |
| `Semifilter.series_q3` | `C(V)=C(W)` iff `V` is contained in `C(W)` and conversely. |

All roots quantify over an arbitrary finite alphabet with **no nonemptiness
hypothesis**. [claims.json](claims.json) states their exact assumptions, scope and
novelty status. Helpers are not counted as additional theorem roots.

**Written-only bridges:** the construction of the complementary submodule from
all original semifilter axioms; equivalence between the original agreement-set
finite index and the quotient range; the parity derivative/normal-form proof and
its finite-expression Q3 expansion; and the entire filter classification.
Consequently this submission is a written resolution with a checked substantive
formal component, not full Lean certification of original-syntax Q2/Q3.

## Audit findings and dispositions

- The candidate's principal formulas survive the audit. Its terse recurrence
  elimination was strengthened to an induction over every starting state, with
  the zero-length case and the initial representative explicitly fixed.
- The marked cut proof now handles both boundary positions. The added unmarked
  product proof uses a strict prefix cut, avoiding a duplicated boundary cut.
- Sums of residual cosets of a tail in `C(V)` are confined to their finite span;
  they are not asserted to lie in `V`. Error tails are not presumed regular.
- Upward closure is used only for filters. The infinite-complement argument and
  complete suffix-closed parametrization are explicit, including empty/unary
  alphabets and improper filters.
- Prodinger pp.36-37 and 43-44 were image-checked. His Section 5 imposes filter
  hypotheses before the Boolean-algebra argument. The broader 2010 Theorem 2.4
  is not used for arbitrary semifilters. All seven survey pages were inspected;
  equation-dependent comparisons use page images, not OCR alone.
- The book scan itself is not present; its exact question/axiom specification is
  the immutable supplied TASK.md. No claim of rechecking that absent scan is made.

## Prior art and novelty

The [1980 author copy](sources/prodinger1980.pdf) supplies the definitions and
filter-qualified Boolean result. The [2010 publisher full text](sources/guo-wang-shum2010.pdf)
records the existing cofinite result (Theorem 2.7) and suffix-generated special
family results (Theorems 3.3/3.4). Those special cases and their examples are not
claimed new. Its other sections concern further special families; the closing
comment about difficulty with general semifilters is not evidence of novelty.

Primary full texts for DOI `10.1142/S1793557117500450` (2017) and
`10.1007/978-981-99-9171-6_3` (2024) have not been compared here. The assigning
agent's separate investigation and comparison with other later literature remain
necessary before any priority statement. **Novelty is unresolved; no discovery
or prior-art-clearance claim is made.**

## Verification and boundaries

The completed artifacts received one final `python3 verify.py` pass, which
**exited 0**. The [receipt](verification/receipt-20261015T044226077836Z.json)
records the exact commands and SHA-256 hashes:

- [Formal.lean compiler log](verification/20261015T044220285231Z/Formal.lean.log):
  exit 0. Three style warnings; no errors. Every root's printed assumptions are
  exactly `[propext, Classical.choice, Quot.sound]`; no additional trusted
  assumption or proof placeholder appears.
- [Negative-control log](verification/20261015T044226077191Z/NegativeControl.lean.log):
  exit 1 because `decide` proved that `0 = 1` is false. The rejection is not an
  instance-synthesis or import failure.

The source and claims hashes still match the receipt after this report update.
The default Lean kernel check and immutable false-proposition control are distinct
from the parent's fresh Comparator verification, which was not run here.

The frozen task, acceptance file, checker, negative control, existing sources,
shared cache, and `math/` files are unchanged. No installs, builds, dependency
updates, outside writes, deletion, commits, external contacts, extra HMZ run, or
reviewer process were performed. Intermediate proof attempts and logs are retained
in [research/](research/), with [JOURNAL.md](research/JOURNAL.md) recording failures
and their dispositions.
