# Follow-up referee decision: **ACCEPT**

All eight findings from `review/claude-review.md` have been honestly addressed. None of the pinned sources is misstated in what it assumes or what it concludes:
- YSS21 is not extended past its badly-approximable (BA) hypothesis.
- Akiyama is used only for the optional BA boundary.
- Bacher's unproved claims are marked as unproved.
- The Tevet extracts are verbatim, and the publication metadata matches.

The new topology, continued-fraction and window clarifications contain no mathematical error. Three wording fixes are left, none blocking.

## Disposition check

| # | Finding | Verdict | What the pinned text shows |
|---|---|---|---|
| 1 | Bacher Rem. 1.2 | Addressed, softened (see R3) | Journal p. 5: (1) rational angles degenerate to rank one; (2) `lim vol V(n) = π` for irrational θ, with no proof. I read all 26 PDF pages and found no proof anywhere: p. 12 calls it "the fact," and p. 23 repeats it. "Unproved" (`STATUS.md:46`, `:59`) is accurate. |
| 2 | YSS21 | Resolved | arXiv v1 p. 2: Theorem 1 and Corollary 2 both begin "Suppose that θ/2π is badly approximable." With exponent ½ the limit area is π, and the arXiv abstract carries the same qualifier. `STATUS.md:55` handles the paper's α (exponent) / θ (angle) notation correctly. |
| 3 | Prop. 6.1 unproved | Fixed | Bacher p. 13: "We leave the proof to the reader." Akiyama states Theorem 2 (four equivalent conditions) on p. 3 and proves it in §2 (pp. 5–7) and §3 (p. 7). |
| 4 | Earlier work not credited | Fixed | Tevet: p. 2 (rational case, "easy to show"), Prop. 4 and Cor. 5 (p. 3), index shift (p. 11). Bacher p. 8: the bounds √(1/4+4π²) and √(2π/√3). |
| 5 | p. 12 antecedent | Fixed | Both extracts are verbatim and consecutive on Tevet p. 12, each under 40 words. |
| 6 | Containment vs. attainability | Fixed | `RESULTS.md:25`, `STATUS.md:23` |
| 7 | Implicit standard facts | Correctly stated | See "New clarifications" below. |
| 8 | Excluded files (finite controls, book excerpt) | Honestly disclosed | `RESULTS.md:270`; I did not audit them either. |

The publisher page says "Vol. 14, No. 3-4, 2025," pp. 239–249, accepted 10 Sep 2025, published 24 Oct 2025. That matches `STATUS.md:27`; the `citation_issue` meta tag just shortens the issue to "3."

## Remaining issues (wording only, non-blocking)

**R1. `RESULTS.md:216`** says Akiyama's Theorem 2 "excludes empty BA limits." Akiyama never mentions Chabauty limits. Ruling out empty limits is your own one-line relative-density argument (§6, and Tevet's Prop. 4). Suggested wording: *"…proves BA ⇔ relative density; with the transfer argument of §6, this excludes empty BA limits."*

**R2. `RESULTS.md:212`** says "The standard continued-fraction equivalence is recalled in Akiyama, pp. 2–3: [best-approximation argument]."
- What Akiyama pp. 2–3 actually recalls is a different equivalence: a uniform bound on q·|qα − p| holds iff the partial quotients are bounded. Akiyama cites Khinchin Thm 23 and Bugeaud Thm 1.9 for it.
- The best-approximation argument and Tevet's convergent-based definition do not appear on those pages.
- Your mathematics is correct; only the citation pointer is loose. Present the bridge as your own standard argument.

**R3. `RESULTS.md:25` / `STATUS.md:46`.** The predecessor's clause "which Bacher asserted in Voronoi-area form" was replaced by "fully acknowledged in STATUS.md."
- Your caveat about "arbitrary Fell convergence" is true, but it addresses a weaker inference than the predecessor's.
- Bacher's Theorem 1.1 defines closeness through a one-to-one matching of points (p. 5). Read with that theorem, Remark 1.2(2) would already assert the affirmative covolume answer.
- Nothing is hidden: `STATUS.md:49–51` concedes the stronger point. Still, "fully acknowledged" deserves one explicit sentence saying so.

A trivial one: at `RESULTS.md:159`, the bound M appears in the sentence just after Bacher's Corollary 3.2, not in the corollary itself.

## New clarifications checked — no error found
- **§1 (`:13`):** the equivalence with Tevet's metric holds in both directions. Tevet's distance uses radius 1/ε and the ε-neighbourhood of the *full* other set.
- **§5 (`:147–151`):** δ_j = ±1/(q_jβ + q_{j−1}) with β > a_{j+1} gives |δ_j| < 1/q_{j+1}.
- **§6 (`:169`):** "the negation of Tevet's BA condition" is exact, because Tevet p. 1 defines BA as `liminf q_j|q_jα − p_j| > 0`.
- **§7 (`:200–202`):** h_j = ⌊√n_j⌋ tends to infinity and is o(n_j). The ε-net length does not depend on the starting phase, so the first minimizer's error is at most ε once h_j is large enough. No equidistribution rate is used.
- **§8 (`:212`):** the best-approximation bound (0 < q < q_{j+1} implies ‖qα‖ ≥ |δ_j|) holds for all j ≥ 0.

## What the texts prove vs. my own inference

**Stated explicitly in the pinned texts:**
- YSS21 proves Voronoi-area convergence only for BA angles.
- Akiyama proves the four-way equivalence for irrational α.
- Bacher's Remark 1.2(2) and Prop. 6.1 are asserted without proof.
- Tevet's reference list omits Bacher.

**My inference (not stated in any pinned text):**
- Chabauty–Fell convergence alone does not imply Voronoi-area convergence. For example, Λ ∪ (Λ + e/j) → Λ, but the cell areas halve. So the manuscript's caution is right.
- For this spiral, Bacher's one-to-one matching (or Lemma 2.2 plus a positive shortest vector) rules out merging points at lattice limits. So Remark 1.2(2) would imply covolume π there.
- The three sources' definitions of BA agree for irrational numbers.
- Tevet cites YSS21 only for the BA case and then poses the non-BA question. That weakly supports, but does not prove, that the journal version of YSS21 is also BA-only.

## Scope
**Read:**
- `STATUS.md`, `README.md`, all of `RESULTS.md` (focusing on §§1, 3, 5–8, 10), `review/claude-review.md` and `manifest.json`.
- Source pages: YSS21 pp. 1–3; Akiyama pp. 1–8; Tevet pp. 1–4 and 9–13; all of Bacher; the publisher page's metadata and milestones.

**Not done:**
- No re-audit of the proofs of Theorems 1–2.
- No code, finite controls or book excerpt.
- No hash recomputation (I ran no commands).
- No check of claims about unpinned web pages: the published YSS21 abstract, the arXiv version histories, the publisher-PDF access denial and the OpenAlex/Semantic Scholar screen.

This is a model-written review, not a machine-checked certificate.

`★ Insight ─────────────────────────────────────`
- Bacher's "ε-close" requires a **one-to-one matching** of points, which is stronger than Chabauty–Fell closeness (Fell allows two points to merge into one limit point). That explains both sides of R3: Fell convergence alone can't carry Voronoi areas, but Bacher's own framework would carry his remark to covolume π.
- The sources define "badly approximable" three ways: Tevet by a liminf over convergents, Akiyama by q‖qα‖ ≥ C for all q, YSS by bounded partial quotients. They agree for irrational α, so "YSS21 assumes BA" restricts exactly the same class of angles that Tevet's non-BA question excludes.
`─────────────────────────────────────────────────`
