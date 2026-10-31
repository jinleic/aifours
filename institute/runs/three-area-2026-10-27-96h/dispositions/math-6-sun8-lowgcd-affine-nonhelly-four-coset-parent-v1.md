# Sun8: four actual low-gcd cosets with non-Helly quotient images

**Disposition: same-harness written support at the frozen f253-A scope.** For every group `G` admitting a surjection `φ:G→F₂³`, let `N` be the inverse image of the first coordinate axis. There are four pairwise-disjoint actual left cosets of index four that partition `G`, such that their first three quotient images intersect pairwise but have empty triple intersection; the fourth image is disjoint from those three. Every pair of original indices has gcd four.

The four affine lines in `F₂³`, using coordinates `(n,x,y)`, are

`{000,010}`, `{100,001}`, `{110,101}`, `{011,111}`.

They partition the eight vectors. Taking their preimages gives actual left cosets of finite-index subgroups, with no finiteness, splitting or commutativity assumption on `G`. In `G/N≅F₂²` their images are `{00,10}`, `{00,01}`, `{10,01}`, and `{11}`. The first three have pairwise intersections `{00}`, `{10}`, `{01}` and no common point. The quotient/kernel index pairs are `(2,2),(2,2),(2,2),(4,1)`.

For `G=F₂³×D`, where `D` has no proper finite-index subgroup, every finite-index subgroup contains `D` and is a preimage from `F₂³`. Hence `B₇(N)=2`, `B₇(G/N)=4` and `B₇(G)=4` in the stated packing sense. The additive rational group is an infinite choice of `D`: divisibility makes every finite quotient trivial.

This refutes the shortcut that pairwise-overlapping quotient images must have a common point merely because the original cosets are disjoint and have index gcd at most seven. **It gives four cosets, not a six- or eight-coset counterexample.** The quotient has `B₇=4`, so the example does not meet the stronger `B₇≤2` quotient hypothesis of the separately scoped six-label argument. No unrestricted Sun8, source-priority or novelty claim follows.

## Evidence and limits

- Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261029-lowgcd-affine-nonhelly-obstruction-v1.txt`, SHA-256 `d62eff5412e520a5b18e7bd85e6575424dd039643622fdd131c57e5f2fb556d4`, 156 LF. Parent displayed every line after explicitly reading the three alternating overlays and the f243 CRT correction. The parent had previously previewed candidate LF 1–30 before that fresh overlay read; this chronology is not backdated. The candidate does not import the corrected alternating conclusions or the f243 CRT argument as mathematical premises.
- Frozen manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f253-sun8-lowgcd-and-abelian-restricted-helly/manifest-v2.json`, SHA-256 `bd0f0a90d64e6b6899f2b5f5c89c927ba065b02389716a6e7d699200834a0f32`. The reviewer reports reading all six declared inputs completely in order before mathematical work; target B was not a premise for this slice.
- Review: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f253-sun8-lowgcd-and-abelian-restricted-helly/review-A-v1.md`, SHA-256 `89745705e37113a197d69813ebb6e7981b266c8065aab959fd2b58249a2b6eef`, 120 LF, **0F/0M/0m** on target A; parent displayed all review lines. Historical assertions and the earlier f243 characterization were outside that review.
- Reviewer-owned finite control exited 0 and enumerated all cosets for `F₂^d`, `d=1,2,3`, with two intended-reason negatives. Parent independently enumerated the four displayed sets, quotient intersections and index pairs at 15:32:14–15:32:25 PDT; the changed-generator negative produced an overlap. The parent did not independently enumerate every possible family in the infinite example; the upper bound is the written finite-index/preimage and packing argument.
- Same-harness only; not human, independent-model-family, formal/kernel or novelty verification. The prior candidate and review bytes remain unchanged.
