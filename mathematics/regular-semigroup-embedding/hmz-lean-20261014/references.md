# References, applicability, and source access

## Read-only mathematical baseline

* `/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/README.md`.
* `/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/proof.md`, especially §§0, 2, 3, 6, 7, 8.
* `/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/sources/book-excerpt.txt`.
* `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/CONTRACT.md` and this repository's unchanged `TASK.md`/`verify.py`.

The definitions and fixed product readings come from these files. The new formal necessity roots correspond to dossier Lemma 0; the wreath construction corresponds to Lemma 3. The orthodox reduction, the earlier positive cases, the finite portfolios and the ξ-purity discussion are mathematical context, not imported Lean conclusions or re-executed evidence.

The book cites Szendrei 2002, DOI `10.1007/s002330010100`, but her original problem wording was not recovered in this run. The book attributes its first fact to a preprint by Billhardt and **Hsieh S. C.**; the published paper with that title has Billhardt and **M. B. Szendrei**, J. Algebra 267 (2003), 559–576, DOI `10.1016/S0021-8693(03)00395-8`. The discrepancy remains recorded, with no claim that this run resolves it. The book itself does not define either product.

The fixed (P) definition is from the dossier's Szendrei survey/Auinger–Szendrei reading. The fixed (R) definition is the completely-simple specialization of Auinger–Polák's restricted product. Their claimed equality of embeddable classes remains attributed to Billhardt–Szendrei 2003 as reported by Auinger–Szendrei 2005, not to the Lean constructions here.

## Actual local openai/math inspection

| Exact path | Inspected statements/patterns | Applicability |
|---|---|---|
| `/Users/jinleic/jinleic-workspace/math/lean/OAI/Algebra/Universal/Congruence.lean` | `OAI.FiniteCongruence.Congruence.principal`, `principal_le`, `relation_map_of_updates`, `compatible_iff_translations`; read the explicit intersection construction and coordinate-update induction | Appropriate methods for a future proof of presentation/congruence or ξ-certificate soundness. They do not establish idempotent purity or faithful parallel-arrow separation for P1. This run does not import the module or claim to have proved that missing step. |
| `/Users/jinleic/jinleic-workspace/math/lean/OAI/Algebra/OddKaplansky/WreathMultiply.lean` | `topElt_mul`, `normal_repr`, `rho_injective`; inspected coordinate recovery and injectivity from represented coordinates | Transfers the method of comparing coordinates to prove a multiplication law or injectivity. The actual theorems require a field, finite group/base, primitive-root and other representation hypotheses. They are not regular-semigroup embedding theorems and are not imported. |
| `/Users/jinleic/jinleic-workspace/math/lean/OAI/Algebra/OddKaplansky/WreathActions.lean` | `top_represents`; inspected translation/action identities and reindexing via group multiplication | Useful proof pattern for verifying the orientation of a wreath shift. The represented matrix action and finite/field hypotheses do not apply to the nonunital band problem. The new shift is proved directly, without borrowing this conclusion. |
| `/Users/jinleic/jinleic-workspace/math/lean/OAI/Algebra/OrderedStates/Semigroup.lean` | `nsmul_compression_iterate`, `nsmul_compression_doubles`, `nsmul_unit_order_iff`; read the additive order arguments | Not applicable: these concern ordered additive **commutative** monoids and repeated addition. P1 concerns noncommutative multiplication and idempotent bands. No imported result from this file is used. |

No ready P1 theorem was found in these inspected files. The corpus was not copied or built. The coordinatewise wreath proof here uses only Mathlib group/Pi infrastructure, not the representation-theoretic conclusions above.

## Lean dependency closure and proof techniques

`Formal.lean` directly imports:

* `Mathlib.Algebra.Group.Hom.Basic`: Mathlib `MulHom`, `map_mul`, ordinary group/semigroup algebra and cancellation.
* `Mathlib.Algebra.Group.Pi.Basic`: coordinatewise multiplication and semigroup instances for function types.

The local definitions of `MulHom` and the Pi semigroup instance were inspected in:

* `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean/.lake/packages/mathlib/Mathlib/Algebra/Group/Hom/Defs.lean`.
* `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean/.lake/packages/mathlib/Mathlib/Algebra/Group/Pi/Basic.lean`.

`NegativeControl.lean` additionally imports `Mathlib.Algebra.Group.PUnit` and `Mathlib.Algebra.GroupWithZero.Nat`. The former's one-element group instance was read. These support the concrete wrong-conclusion mutation, and supply no P1 embedding theorem.

`Mathlib.Algebra.Group.Action.Defs` was inspected to check the available action interface. Its `MulDistribMulAction` requires a monoid base. A band in P1 can have no identity, so the file uses the small explicit nonunital `Action` and `EndAction` structures instead. All required action laws, automatic bijectivity, carrier closure, associativity and inverse equations are checked in Lean; no desired embedding is a structure field.

The cached project is reused read-only at `/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`, with `leanprover/lean4:v4.34.1`. Exact reference/dependency hashes are in `attempts/provenance.json`. The only observed standard axioms are `propext` and `Quot.sound`; the latter appears in the coordinatewise/function-extensionality proofs. No OAI dependency closure, Comparator or nanoda replay is claimed.

## Lawful primary-source access, 2026-10-14

1. **Szendrei survey, arXiv:1909.05280.** The existing local PDF `/Users/jinleic/jinleic-workspace/ai4s/regular-semigroup-embedding/sources/szendrei2019_survey_arXiv1909.05280.pdf` was read through a new text extraction at `sources/szendrei2019.txt`. Section 5.1 was inspected for the regular-band theorem and the nonembeddable example's stated left-semiregular band hypothesis. It does not establish local regularity of that example. [Primary arXiv record](https://arxiv.org/abs/1909.05280).

2. **Szendrei 1993, Acta Sci. Math. 57, 601–612.** A public publisher PDF was successfully fetched into `sources/szendrei1993_acta57.pdf`, with extraction `sources/szendrei1993_acta57.txt`. Section 2, Theorem 2.2 and Corollary 2.7 describe a universal canonical homomorphism and its injectivity criterion. These support the presentation-based attack; they supply no proof that it is injective in P1's class. [Publisher PDF](https://acta.hu/download.phtml?id=2201).

3. **Hartmann, E-Unitary Covers over Group Varieties, DOI `10.1007/s00233-004-0138-9`.** The actor read the author's publicly uploaded text; its Theorem 6 restates Billhardt's necessary condition, and Theorem 8 recalls a finite graph example attributed to **Szendrei 1998**, a separate reference from Billhardt's J. Algebra paper. The integration owner preserved the exact Theorem 6 excerpt from the retained actor web output at `sources/hartmann2005-theorem6-tool-excerpt.txt` with provenance, and independently obtained the author's [2007 thesis](https://doktori.bibl.u-szeged.hu/id/eprint/1183/1/HM_dissz.pdf), Theorem 3.4, PDF p. 20, with the same formulas. The PDF is saved as `sources/hartmann2007-thesis.pdf`. [The condition audit](obstruction-condition.md) gives its exact statement, source-dependent necessity calculation and constraint mapping. No local-regularity check of the actual published counterexample's band is claimed. The original journal PDF was not downloaded; the later integration fetch met HTTP 403/browser challenge and was not bypassed. [Author-uploaded article](https://www.researchgate.net/publication/236035122_E_-Unitary_Covers_over_Group_Varieties).

4. **Billhardt's institutional publication page** was readable but provided no full-text link for the 1998 J. Algebra paper. [Author page](https://www.mathematik.uni-kassel.de/~billhard/). **Szendrei's institutional publication list** was also readable and gave bibliographic entries without linked author copies for the 1998 finite example, 2002 open-problem paper, or 2003 paper. [Author list](https://www.math.u-szeged.hu/tagok/bszendre/papers.html).

5. The first links to the Billhardt 1998 and Szendrei finite-example records returned **403 Forbidden**; the tool-resolved URLs contained a doubled `/publication/` component. Ordinary normalized record URLs were subsequently readable as metadata/abstract pages with **Request PDF**, without an accessible construction. The Billhardt record identifies DOI `10.1006/jabr.1997.7390`. No request-copy action was taken. [Billhardt record](https://www.researchgate.net/publication/215521012_On_Embeddability_into_a_Semidirect_Product_of_a_Band_by_a_Group), [Szendrei finite-example record](https://www.researchgate.net/publication/266238326_A_finite_non-embeddable_E-unitary_regular_semigroup).

No access restriction was bypassed, no account was used, and no external message or author-copy request was sent. The original Billhardt construction, Szendrei 2002 wording and BS2003 proof remain uninspected here. The existing dossier's access limitations were not converted into statements about the current status of the problem. Individual outcomes are retained in `attempts/source-access.json`.

The integration owner's additional lawful author-copy and repository work is in
`source-access.md`; the added read-only corpus inspections are in `math-applicability.md`.
The finite ξ-purity argument is now a written parent-audited result in `xi-purity.md`,
not a Lean root and not a product-embedding theorem.

## Solver and workflow provenance

The bounded searches used the existing Z3 package at `/Users/jinleic/.cache/uv/archive-v0/c7QOyiK_VoK1nOHbVXY00`, via a process-local `PYTHONPATH`, with `PYTHONDONTWRITEBYTECODE=1`, one solver thread, and a 60,000 ms solver timeout. There was no package install or cached-runtime edit. Logs and precise sizes/results are retained in `attempts/obstruction-search.log`, `attempts/obstruction-search-9-8.log`, and their JSON reports. These are unsuccessful finite searches, not theorem proofs.

The actor read the Humanize workflow and coding-discipline skills and relevant workspace policies. Its targeted search did not locate `openai-math-lean-verification`, so it followed the frozen task's explicit Lean/axiom/checker requirements. The integration owner did read that skill through `skill://openai-math-lean-verification` before launch. No missing-skill condition or optional permission flow relaxed the frozen acceptance requirements.
