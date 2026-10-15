# Prodinger-type semifilters: exact Questions 2 and 3

Date: **2026-10-14 PT**. Source: mathematics volume, book pp.61–63 / PDF pp.77–79; Questions2/3 are on book p.62.

**Outcome:** complete, independently reviewed **written structural answers to both exact questions**, an accepted bounded HMZ RLAR run, and four parent-Comparator-accepted Lean theorem roots. Formalization covers the all-word elimination identity and the complementary-series regularity/saturation criteria; the original semifilter syntax, filter classification and parity-expression expansion remain written proofs. **NOVELTY-UNCLEAR:** inaccessible relevant later sources prevent a claim of newly solving an open problem. The whole five-question chapter is not solved here.

## Exact questions and definitions

The image-checked [source excerpt](source/problem.zh.txt) and [original question page](source/page-078.png) preserve the book's statements:

* **Q2:** Find other left-divisible filters or semifilters L on a finite-alphabet free monoid X* for which R_L is exactly the regular-language class.
* **Q3:** For arbitrary two such families L₁,L₂, give a necessary and sufficient condition for R_(L₁)=R_(L₂).

A source semifilter contains X*, is closed under the **complement of symmetric difference**, and under every left quotient D_u A={v:uv∈A}. Upward/intersection closure belongs only to filters. No properness or nonempty-alphabet assumption is inserted. R_L consists of languages T for which

    u ~ v  iff  {w: uw∈T iff vw∈T} ∈ L

has finite index. Empty words are included in both the prefixes and the testing contexts.

## Answers

Let Reg denote ordinary regular languages; V={A^c:A∈L}. Write C(V) for languages with finitely many residual cosets D_u T+V, where addition is symmetric difference. The original definition gives R_L=C(V) exactly.

| Exact scope | Answer |
|---|---|
| Q2, all semifilters | **R_L=Reg iff every member of L is regular.** Reg itself is the largest qualifying semifilter. |
| Q2, all filters | **R_L=Reg iff every member of L is cofinite.** Equivalently L={A:A^c is a finite subset of U} for a unique suffix-closed U⊆X*. |
| Q3, all semifilters and filters | **R_(L₁)=R_(L₂) iff V₁⊆C(V₂) and V₂⊆C(V₁)**. The equivalent finite-expression criterion below removes the generalized-recognizability predicate from the criterion side. |

The normal-form theorem is

    C(V) = {K + Σ_(i=1..n) P_i a_i B_i :
            n≥0, K,P_i∈Reg, a_i∈X, B_i∈V}.

Here **products count factorizations modulo two**, not by existential concatenation. Precisely, `(P a B)(w)=Σ_(w=uav) P(u)B(v)` in F₂. The Q3 criterion can therefore be stated solely on the two given families:

> For both ordered pairs (j,k)=(1,2),(2,1), **every G∈L_j** admits an expression
>
>     G^c = K + Σ_(i=1..n) P_i a_i H_i^c,
>
> with finitely many terms, K,P_i regular, a_i letters and H_i∈L_k.

The finite expression can depend on G. This is a structural necessary-and-sufficient condition, not a decision algorithm for arbitrarily presented infinite families. For the empty alphabet, the sum has no terms and every language is regular. Unary alphabets and improper filters are also covered.

Concrete Q2 examples include the filter of languages containing every word of length at least n, for any n≥1, and the semifilter Reg. These examples are not claimed new.

## Proof mechanism

The complete readable derivation is [proof.md](proof.md), Theorems1–5. In brief:

1. Complementation converts the exact source axioms into a derivative-invariant F₂ subspace V; the agreement congruence becomes equality of residual cosets modulo V.
2. Every finite residual quotient gives finitely many representative series S_q and transition errors E_(q,a)∈V. Eliminating their exact recurrence over the entire word gives the regular terminal language plus the finite parity expression. All empty-word terms are retained.
3. The derivative of a marked parity product is split into cuts before/after the consumed prefix. If the tail has m residual cosets, finite sums of those cosets have at most 2^m values. This proves the required closure, without confusing parity with ordinary products or claiming that the sums vanish modulo V.
4. That closure proves C(C(V))=C(V), and hence the cross-family criterion. For filters, any infinite complementary language contains a nonregular subset by diagonalization, forcing all complements to be finite.

The [HMZ-reviewed proof snapshot](evidence/hmz/reviewed-proof.md) additionally gives a direct finite-span proof of regularity reflection and saturation. This is the route used in the substantive Lean core, not an assumption of the normal form.

## Verification and exact formal scope

[claims.json](claims.json) is the claim interface; private/helper lemmas are not counted as extra results.

| Artifact / theorem roots | Exercised verification | What it establishes |
|---|---|---|
| [Written proof snapshot](evidence/reviewed-proof-snapshot.md) | Independent no-tools Opus/max referee: **correct-with-minor-fixes**, 42 checked claims, no fatal/major findings | Full written Q2/Q3 structural answers, conditional only on the source transcription; parent and worker separately checked that transcription against images. [Dispositions](evidence/review-resolution.json) record the fixes. |
| [Elimination.lean](work/Elimination.lean): `SemifilterElimination.residual_elimination` | Worker Lean check; parent fresh-module Comparator **accepted**, 82.69s | Exact all-word coefficient elimination, not a standalone proof of Q2/Q3. Observed axiom: propext. [Receipt](evidence/comparator-elimination/receipt.json). |
| [Formal.lean](work/Formal.lean): `Semifilter.series_regular_criterion`, `Semifilter.series_saturation`, `Semifilter.series_q3` | HMZ actor and independent HMZ reviewer compile passed; parent fresh-module Comparator **accepted**, 82.27s | Complete regularity/saturation/mutual-inclusion criteria for actual finite residual-coset ranges in F₂ series, bridged to Mathlib `Language.IsRegular`. Only propext, Classical.choice, Quot.sound. [Receipt](evidence/comparator-q2q3/receipt.json). |
| [Negative control](work/NegativeControl.lean) | Lean rejects `0=1` because the proposition is false | Rejection is mathematical, not missing synthesis/imports. [Actual log](evidence/hmz/NegativeControl.lean.log). |
| [Independent parity assay](work/check_parity_identities.py) | 28,800 derivative-split and 260,096 normal-form coefficient cases passed; four semantic mutations detected | Bounded corroboration only, not an infinite-language proof or novelty evidence. [Receipt](evidence/parity-assay.json). |

**Written-only bridges:** construction of the complementary submodule from original semifilter axioms; equality between the original congruence index and the residual-coset range; normal-form parity-product expansion; and the cofinite/suffix-closed-U filter classification. Consequently the whole original-syntax answer is **not fully Lean-certified**, despite the substantive semantic roots.

Comparator checked never-built solution modules, statement/definition agreement, permitted axioms and fresh Lean-kernel acceptance. The macOS `fake-landrun` wrapper is not an OS sandbox, and no external kernel was configured. It does not certify novelty or mathematical statement faithfulness by itself.

### Accepted HMZ round

One wrapper-owned run, maximum 3600s, finished after **1639.44s** with actual reviewer **done:true**, native epic **how:done**, resume **ok:true**, and runner exit0. Frozen TASK/ACCEPTANCE/verify files stayed unchanged. See the [terminal audit](evidence/hmz/terminal-audit.json), [actual reviewer verdict](evidence/hmz/reviewer-verdict.json) and [integration scope/dispositions](evidence/hmz/integration.json).

* Baseline: `9852932c8aef2151eb3dfd3bad195310c327559c`.
* Runtime: `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a`; official flowverse: `2c37d06df3e356807adb93b5a9fdca170a5d0be8`.
* Live pairing: Codex `gpt-6.1-sol:max` actor, Claude `claude-opus-5-5:max` reviewer. Both retained the configured full-access permissions; no sandbox claim.
* Failed Lean attempts remain preserved in `/Users/jinleic/jinleic-workspace/scratch/ai4s-math-more-20261014/semifilter/research/`. The exact scoped process check found no owned process remaining.

The no-tools-reviewed snapshot SHA is `6af974f5622aaab0e28f5c2aadeb262060fba7f93ef3e536ad3af160937b8774`; its minor fixes are applied to the integrated proof. The separately HMZ-reviewed snapshot SHA is `e6c94919d699a073400042e0389b8838f11124219338c63d0e24ca548e6a462d`. These are distinct reviews of distinct preserved artifacts, not one review retroactively covering edited bytes.

## Prior art and the remaining blocker

The [source comparison](sources/references.md) and [access log](evidence/source-access.json) document lawful recovery of **Prodinger1980** and the complete **Guo–Wang–Shum2010 survey**. The latter already gives special suffix-filter answers (Theorems3.3/3.4) and records the known cofinite theorem (Theorem2.7). Those results are not discoveries here.

The exact general statements still require full-text comparison with:

* [Guo–Wang–Shum2017](https://doi.org/10.1142/S1793557117500450), whose abstract says it answers a Prodinger question but does not identify the application theorem;
* [Wang2021](https://zbmath.org/1513.68033), *On languages defined by generalized principal right congruences*, a direct-scope paper on suffix-closed-language semifilters;
* [Guo–Liu–Wang2024, chapter3](https://link.springer.com/chapter/10.1007/978-981-99-9171-6_3), especially §§3.4–3.5. The free front matter was recovered, not the chapter.

Public routes failed through HTTP403, TLS/access challenges or subscription redirects, as individually recorded. The 2011 PS-regular-language original is another uncompleted comparison. A search miss is not proof of openness. **The deliverable is a reviewed answer with substantive formal evidence; no newly solved open-problem priority is asserted.**

## Reproduction

The portable bounded assay, writing no files unless requested:

```sh
python3 -B mathematics/prodinger-semifilter-languages/work/check_parity_identities.py
```

Lean compilation uses the existing read-only Mathlib verification project; supply an absolute file path and do not build or write in the cache directory:

```sh
# cwd: /Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify
PATH="$HOME/.elan/bin:$PATH" lake env lean -j 4 \
  /Users/jinleic/repos/aifours/mathematics/prodinger-semifilter-languages/work/Formal.lean
```

The parent-owned fresh Comparator packages are retained byte-for-byte under `evidence/comparator-{elimination,q2q3}/`. Full HMZ scratch state and failed proof-attempt history are preserved rather than replaced by the integrated dossier.
