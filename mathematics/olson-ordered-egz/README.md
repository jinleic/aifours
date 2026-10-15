# Olson's ordered Erdős–Ginzburg–Ziv conjecture

**Status on 2026-10-14 PT: no full resolution established.** General status is **uncertified-open / no resolution found**, not a claim that a current primary source certifies openness. The ordered and reorderable questions are different.

## 1. Source

*10000 Selected Problems in Sciences: Mathematics*, chapter on Davenport constants, contributor Zhiwei Sun, printed p142/PDF158. [Verbatim Chinese excerpt](source/problem.zh.txt), visually checked against the source image at `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-more-20261014/source-images/olson/page-158.png`.

Translation: Olson proved that, from every sequence of length2n-1 in any multiplicative group G of order n, n distinct indices can be chosen whose corresponding elements multiply to the identity; he conjectured that one can additionally require i_1<...<i_n.

## 2. Problem

For every finite group G, n=|G|, and every ordered sequence a_1,...,a_(2n-1), does there exist

    1 <= i_1 < ... < i_n <= 2n-1,
    a_(i_1) * ... * a_(i_n) = 1_G ?

The product follows increasing original indices. An unordered multiset, an arbitrary permutation of the chosen elements, or an identity-product sequence of another length does not meet the target. One exact finite group and one avoiding word of this precise length would refute the full conjecture.

Faithful Lean proposition, using actual group multiplication and ordered List.Sublist:

```lean
∀ (G : Type) [Group G] [Fintype G] (xs : List G),
  xs.length = 2 * Fintype.card G - 1 →
  ∃ ys : List G, ys.Sublist xs ∧
    ys.length = Fintype.card G ∧ ys.prod = 1
```

## 3. Status and novelty gate

- The [2006 Mohar listing](https://www.sfu.ca/~mohar/Problems/P0604_OlsonConjecture.html), [2007 Open Problem Garden](https://openproblemgarden.org/op/olsons_conjecture), and [2015 Halasz primary problem-session abstract](https://canadam.org/archives/2015f/program/abs/op/) state the exact ordered conjecture. The2015 abstract says it remains open apart from special cases.
- The dated search on2026-10-14 found no general resolution. This is not proof of present openness or of novelty. [Search and access record](evidence/source-observations.json).
- Original Olson1976 bibliographic metadata was recovered, but not its body: publisher routes returned403, API alternatives returned400/406 or metadata only, and a separate browser attempt stopped at a CAPTCHA. The exact original wording was therefore corroborated through primary later research/problem statements, not directly read from the1976 paper.
- The odd-dihedral lower bound reproduced here was already claimed in Agarwal–Lou2016's primary abstract. Their full proof and construction were not exposed. **No new mathematical discovery is claimed.**

## 4. State of the art

The key recovered baseline is [Dimitrov2004](sources/dimitrov-2004.pdf), Theorem2, visually checked on p131: **the ordered conjecture holds for all finite p-groups**. For noncyclic p-groups of order n, the paper improves the threshold to (1+(2p-1)/p^2)n-1. Its soluble-group corollary is explicitly unordered. Thus small Q8/order-eight dihedral checks do not add new group coverage.

[Zhao–Wang2026, arXiv2603.21052](https://arxiv.org/abs/2603.21052) defines its constant using products “in some order”; it does not settle this question. The2026 revision of [Godara–Joshi–Mazumdar](https://arxiv.org/html/2408.13558v2) separately studies ordered Davenport constants (arbitrary nonempty lengths) and unordered Gao constants (length|G|). These cannot be combined without a new argument.

[References and math/ transfer audit](sources/references.md) record exact source boundaries. No covering local or remote openai/math entry was found. The finite-certificate example in `math/lean/ComparatorChallenges/SnakyCertificate` informed statement binding, not the mathematics of Olson's problem.

## 5. Attack and obtained results

See [proof.md](proof.md) for the actual arguments.

1. **All-parameter known lower bound.** For every nonzero odd m, in the actual dihedral group of order2m the word r^(2m-1)s^(2m-1) has length4m-2 and no ordered2m-term identity product. Lean proves the group order, word length and universal ordered-sublist condition. This is **one term too short**, not a counterexample.
2. **Universal structured-construction barrier.** For every finite G and every a,b,c, the particular word a^(|G|-1)c b^(|G|-1) DOES contain an ordered |G|-term identity product. This was proved and Lean-checked without cyclic-factor assumptions. It covers only that word family, not arbitrary words. The finite pigeonhole proof either finds c among a^(-k)b^(k+1) or obtains a collision giving an identity subword that skips c.
3. **Mixed-prime exact searches.** Full-word SMT searches on A4 and C3 semidirect C4 (both order12), each bounded to180 solver seconds, returned UNKNOWN/timeouts. No counterexample or all-word exclusion was obtained.
4. **Structured finite exclusions.** Every length23 word with at most three constant runs in those two order12 groups was checked:95,832 nontrivial parameterizations per group, with each identity witness multiplied again as actual letters. This says nothing about four-or-more-run words.
5. **Model audit.** The parent's ordered-DP transition, state merging and final-horizon low-layer pruning are mathematically sound for its genuine group tables. Its D5/order10 BFS timed out at900 seconds without a result; that remains UNKNOWN and was not rerun here. A disjoint-contiguous-interval shortcut already fails as a sufficient proof route on a simple C2 word, although Olson's conclusion holds there.

## 6. Claims table

| Claim | Status | Exact scope |
|---|---|---|
| Full ordered Olson conjecture | OPEN IN THIS WORK | Every finite group and every length2|G|-1 word remain required |
| Odd-dihedral one-short word | PROVED / known-bound reproduction | Every odd m; length2|G|-2 only |
| Boundary singleton insertion | PROVED / no novelty claimed | Every finite group, only a^(n-1)c b^(n-1) |
| A4 and C3 semidirect C4 unrestricted search | UNKNOWN | Two180-second SMT timeouts, no inference of infeasibility |
| Three-run words in those groups | COMPUTED+WITNESS-CHECKED | Two fixed order12 groups and at most three constant runs |
| Reorderable2026 bounds imply ordered claim | NOT ESTABLISHED | Missing preservation of increasing indices |

Machine-readable statements, assumptions and theorem roots: [claims.json](claims.json).

## 7. Verification and independent review

- [DihedralLowerBound.lean](work/DihedralLowerBound.lean): accepted by `lake env lean`; theorem root `OlsonPartial.odd_dihedral_sharp_lower_bound`.
- [BoundaryInsertion.lean](work/BoundaryInsertion.lean): accepted after correcting one sublist-unfolding elaboration error; failed source/log preserved under `evidence/attempts/`. Root `OlsonBoundary.boundary_word_ordered_egz`.
- Both roots print only propext,Classical.choice,Quot.sound as axioms. These are worker Lean checks, **not a claimed parent Comparator replay**.
- [NegativeControl.lean](work/NegativeControl.lean) fails because `decide` proves its finite ordered-sublist proposition false, not because an instance is missing. The added identity permits r^3 s^2 1 in D6.
- [Semidirect SMT receipt](evidence/c3rtc4-smt.json): its length22 positive-avoidance control raw-enumerated all646,646 twelve-subsets and agreed with set-DP; its fixed length23 identity-extension control was UNSAT. These controls are not full-conjecture counterexamples.
- [Independent Codex snapshot review](evidence/review/result.json), actual gpt-6.1-sol/max, read-only, returned `correct-partial` with no findings. [Pinned snapshot and command](evidence/review/receipt.json). It reviewed the lower-bound theorem, original complementary-cyclic insertion argument, DP/SMT semantics, false control and source limits. A [second independent snapshot review](evidence/review-boundary/result.json), also gpt-6.1-sol/max and read-only, audited the stronger unconditional boundary theorem, its Lean statement/proof, and the later three-run coverage assay. It also returned `correct-partial` with no findings; [second snapshot receipt](evidence/review-boundary/receipt.json).

### HMZ terminal state and retained actor results

The sole sanctioned3600-second HMZ round **was not accepted**: native journals ended `how:"stopped"`, `ok:false`, after three completed negative reviews and an interrupted fourth review. Frozen TASK.md, ACCEPTANCE.md and verify.py were unchanged. [Terminal audit and reviewer notes](evidence/hmz-terminal.json).

The tool capped the outer deadline at3600 seconds too, so the runner's final receipt-copy step was interrupted. The genuine native journals nevertheless contain their terminal records and were separately recovered and hashed; the original incomplete process.json was preserved, not fabricated. [Exact outer/native distinction and no-process check](evidence/hmz-outer-timeout.json). No second round was launched.

Runtime3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a; official flowverse2c37d06df3e356807adb93b5a9fdca170a5d0be8. Actor: codex/gpt-6.1-sol,max; reviewer: claude/claude-opus-5-5,max. Both retained ALL local/user/system/online permission; this was **not an OS sandbox**. The local flow does not explicitly set a web-search mode, and an effective CLI mode was not independently recorded. Frozen baseline80d3ee85e46b071b2c95c6466524d392f2b211e4; [original provenance receipt](evidence/hmz-process.json).

The [retained actor snapshot](hmz-round-20261014/proof.md) is hash-pinned by [its manifest](evidence/hmz-artifact-manifest.json). It contains no full proof, counterexample, or full-goal Lean file. Its closest saved D14 word still has **three** ordered14-term identity subsets, out of20,058,300 raw subsets. Saved Dic12 and A4 words have33 and3,066 identity subsets respectively; both raw audits cover1,352,078 subsets. These are explicitly failed counterexample candidates, not counterexamples.

HMZ also completed restricted-family exclusions in D14 and Dic12: rotations must all be the single fixed generator r, and reflection-coset letters must form at most five constant blocks with arbitrary r-gaps. Its five-block stage recorded17,307,764,565 and2,530,653,840 parameter tuples respectively, most pruned by proved filters or symmetry; these are **not counts of distinct words or of raw subset enumerations**. The final independent HMZ reviewer checked the pruning mathematics and replayed selected compiled assays, while keeping `done:false`. Exact families, counts, controls and limitations are in the retained actor proof/claims/logs; the worker did not rerun those large assays. General words—even in either fixed group—remain outside this result.

The fresh actor repository and heavy/raw runtime output remain under `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-more-20261014/olson` and `olson-hmz-evidence`. The full-goal verifier's recorded result is exit1, `NOT ACCEPTED: Exact full goal not claimed solved`.

## 8. Reproduction and exact next action

Run artifact checks on a copied dossier if receipts must remain immutable. From the shared read-only Mathlib project:

```sh
PATH="$HOME/.elan/bin:$PATH" lake env lean /ABS/PATH/work/DihedralLowerBound.lean
PATH="$HOME/.elan/bin:$PATH" lake env lean /ABS/PATH/work/BoundaryInsertion.lean
# Expected failure, explicitly false proposition:
PATH="$HOME/.elan/bin:$PATH" lake env lean /ABS/PATH/work/NegativeControl.lean
```

From a copied dossier, `python3 work/block_search.py` replays the complete three-run family and writes its receipt. `ordered_smt.py` records UNKNOWN faithfully and never turns timeout into UNSAT.

A resolution still needs either an all-groups proof preserving the order of arbitrary interleaved terms, or one exact finite group and a length2|G|-1 word with every increasing-index |G|-subset excluded. The boundary-insertion theorem rules out a simple proposed construction but does not bridge that quantifier. For the searched order12 groups, any further construction must have at least four constant runs; no larger brute force is justified by these timeouts alone.
