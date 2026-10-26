# math-4 selection v1 — broad regular-semigroup embedding

Observed clock immediately before this freeze: **2026-10-23T13:59:06-0700**. Author: MathSemigroup. Status: **UNCERTIFIED-OPEN; written research only**. The startup, eighteen-slot contract and its two errata are operative. This is one problem, not a new slot for each subclaim.

## Literal target and quantifiers

For **every nonempty regular semigroup S, finite or infinite**, suppose:

1. For every idempotent e and every a, if e = fa = ag for some idempotents f,g, then a is idempotent (the book's weak E-unitarity).
2. For every idempotent e, the local monoid eSe is orthodox and its idempotent band satisfies xyxzx = xyzx (the book's local r-orthodoxy).

Does there exist a band B such that every bBb is a regular band, a completely simple semigroup C, and an **injective multiplicative** map S into the specified band-by-C product?

The book pp.66–67 (PDF pp.82–83), Guo Yuqi's Question 1, is the exact statement authority. It does not define its semidirect product. I preserve the dossier's two fixed readings and do not silently use the ordinary product instead:

- **P:** C=M[G;I,Lambda;P], G acts on B by automorphisms, and
  (b,(i,g,lambda))(d,(j,h,mu))=(b * alpha_(g p_(lambda,j))(d),(i,g p_(lambda,j)h,mu)).
- **R:** the dossier's restricted action of C by endomorphisms with carrier alpha_(xx')(b)=b, x' an inverse of x, and completely-simple-specialized product (b,x)(d,y)=(b alpha_x(d),xy).

A classical reformulation or an idempotent-pure quotient is not an answer to this embedding question. No cardinality restriction, faithful-action assumption, or global orthodoxy is inserted into the target.

## Book relationship, current primary baseline and source boundary

Read literally: `mathematics/regular-semigroup-embedding/sources/book-excerpt.txt`; dossier README §§Source/Problem/Status/SOTA; proof §§0–2; the 2026-10-14 HMZ delivery; `xi-purity.md` in full, and its recorded written audit. These files are read-only baselines, not this round's discoveries.

Strongest matched accessible primary statements refreshed today:

- [Szendrei, Structure theory of regular semigroups, arXiv:1909.05280](https://ar5iv.labs.arxiv.org/html/1909.05280), §5.1: E-unitary orthodox semigroups whose **global** idempotent band is regular embed in band-by-group products. That global identity cannot be replaced without proof by local regularity. The survey explicitly gives Billhardt's nonembedding example with a left-semiregular band, but does not establish that particular band is locally regular.
- Same primary survey, §5.2, Theorem5.5: all weakly E-unitary **locally inverse** semigroups embed in Pastijn products of normal bands by completely simple semigroups. It does not state the desired locally-r-orthodox extension.
- [Author publication list](https://www.math.u-szeged.hu/tagok/bszendre/papers.html) now includes [2025 Normal extensions and full restricted semidirect products of inverse semigroups, arXiv:2409.00870v2](https://arxiv.org/html/2409.00870v2). Abstract and introduction read: its normal-extension/almost-Billhardt hypotheses and **inverse** objects do not supply the missing arbitrary locally-r-orthodox theorem.
- [Szendrei2002 publisher page](https://link.springer.com/article/10.1007/s002330010100) read today: subscription preview only. Original problem wording remains inaccessible. No primary current statement certifying that the broad target is still open has been recovered; therefore UNCERTIFIED-OPEN, not a search-miss assertion of openness.

The existing dossier proves necessity, orthodox reduction, regular-band and two-D-class cases, finite certificates, and **idempotent purity for every finite member**. Theorem X actually applies whenever a completely simple ideal exists and needs local orthodoxy, not local r-orthodoxy. No excluded finite-purity counterexample search will be retried.

## Corpus screen before attack

Read the local openai/math inventory and the existing exact applicability ledger. New targeted searches of local CONTENTS.md, overview.tex, formalization.yaml, all lean/docs and preprints for Pastijn, Billhardt, Szendrei, locally orthodox/r-orthodox, seminormal band and regular semigroup found no matched embedding claim. Generic semigroup matches in the indexes concern noise/transfer/Cuntz semigroups. The remote [current CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) was fetched and screened with the same topical strings: no matched claim; generic matches concern noise/transfer semigroups. No corpus theorem is imported or formally replayed. This is a bounded topic screen, not corpus validation or proof of novelty.

## Missing ingredient, consequential delta and first bounded attack

Missing in the orthodox reduction: construct a **faithful** derived functor into a locally regular band; its known wreath criterion cannot supply its own faithfulness. Missing in the nonorthodox case: a pure completely-simple quotient, where available, must be lifted to an actual product embedding. In the unrestricted infinite case, one must also avoid assuming a minimal/completely-simple ideal.

First bounded written attack has two connected routes within this single target:

1. Determine whether local regularity forces the actual Billhardt N1–N3 obstruction to vanish identically, not merely in old finite tests. Work algebraically with the literal premises and preserve the least-group-grade argument.
2. Build a coordinatewise ultraproduct construction for the actual P/R products. Use it to derive a genuine infinite structural barrier: directed unions of embeddable regular pieces cannot fail only through incompatible choices of band/action; extend Theorem X's pure-quotient conclusion to semigroups having a cofinal regular cover by pieces with completely simple ideals. This latter conclusion is a partial infinite-case result, not an embedding theorem. Do not silently equate a cofinal finite regular cover with ordinary local finiteness.

The desired consequential result is either an explicit faithful construction or a rigorously proved obstruction to a concrete counterexample mechanism. No scientific executable, solver, finite enumeration, compilation, new environment or Lean run is permitted without exact parent GO.

## Verification and redirect conditions

Any completed manuscript is frozen on pinned bytes and remains CANDIDATE until parent and a genuinely separate in-harness reconstruction inspect the whole proof. Written algebra is not a kernel proof; classical ultrafilter/choice/Rees imports will be named. Correctness, import trust, exact scope, novelty and significance are separate.

If accessible prior art solves the broad target, report the actual source to Main and propose a distinct replacement only after the parent's roster collision check. If Billhardt's specific nonembedding band turns out to be locally regular, verify the actual multiplication/action hypotheses before any refutation claim. A compactness criterion alone or unchanged old certificates do not meet the deliverable; the attack must produce its stated construction/proof/barrier or disclose the exact unproved step.
