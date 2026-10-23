# Olson reflection lane: REFL-HI arc-system exclusions (v5 with errata 1–5)

Recorded at 2026-10-19T07:50:36-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** These are written structural exclusions inside the reflection half of the inverse problem for D_(2p). REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and ordered Olson for D_(2p) all remain **OPEN**. No computation, Lean, novelty or priority claim is made.

## Text of record

- [v5](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md) `4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c`, read through errata [1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-1.md) `512e1d9e9a5dcdd4ad85840ce74d6d29ab8e1b8eb72db944ddff4a5683393331`, [2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-2.md) `b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820`, [3](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-3.md) `380106c91b0bcf250a8fd98583e75b39faf3d4c7d3ecd0eba2b2472bc15e669a`, [4](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-4.md) `32811de59e1b5ca736a3db1a9b6592266dbcbcd8690cff27aa143b678e5907f1` and [5](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-5.md) `40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4`.
- **Erratum 5 Part II is ACCEPTED**, so the printed Theorem SEG holds for every R:
  - Π_need ≥ 1: the I.12 loop.
  - Π_need = 0: I.12.
  - Π_need < 0 (R ≥ 2p+1): Part II, which uses (H1) and (H2) only.
- **Erratum 4's narrowing is superseded.** It remains true as a weaker statement, and its finding was correct for the v5 text alone.
- **Binding readings from the second-family slice reviews.** All are wording or scope fixes; no statement is strengthened.
  - **S1/m1:** in e5, read "is a special case" as "toggles c_j ∈ {0,1} by deleting or adding the unique base arc of M_j; e5's moves are not used". This applies to both SEG and MID.
  - **m2:** N_O ≤ p is stated at the choice of O₀.
  - **m3:** the Sec. 8 "Remaining" bullet for R=p is superseded by I.14.
  - **m4:** under its diversity hypothesis, FP-1 excludes words in every non-excluded R=p cell except (5,3). This is a conditional statement only, not universal coverage.
  - **m5:** TOP holds for p ≥ 7 and also for (p,κ)=(5,4).
  - **m6:** the I.14 R=p+δ clause "or the FP-1 diversity conditions" is deleted.
  - **m7:** after Part II, the R ≥ 2p+1 reading uses the printed Theorem SEG hypotheses.
  - **Cosmetics:** C1 (max(0,·) steps), C2, C3 (rename a*, b*, c*; cite H≥0; γ_m(E±)≥1) and C4/C5 are recorded and change no statement.

## Accepted claims

All claims hold in setting (S): p ≥ 5 prime; a cyclic word of length 4p−2 over D_(2p); rotation letters in one pair {ρ_x, ρ_−x}, x≠0, normalised to x=1 and A≥B; every maximal cyclic constant reflection block odd; F, R ≥ 1; maximal decomposition with genuine empty runs; no purity assumption, no B<κ assumption, no value restriction.

- **Foundations** (per-claim scopes as in the Claude foundation review §C, with I.10/I.11): Lemma W, Facts 2.1–2.2, Lemma 2.1, ARC/ARC+, Lemma SEG (e1+I.3), Lemmas 3.1/3.2, BAL, the realisation rule (e5 as read above), Theorem FP and Corollary FP-1 (R=p, conditional on diversity), K2P+, IIIb-X, ETA, and Lemma 1.1 (RES-HI(p) ⇒ REFL(p)).
- **Theorem SEG** as printed, for every R, together with Corollaries SEG-p, SEG-num (I.13: m_lo ≥ 2, the maximum inactive), MID (R=p, κ=(p−1)/2, p≥11) and TOP (R=p, κ∈{p−2,p−1}, p≥7, plus (5,4)).
- **Exact universal coverage (I.14) for R=p**, among residual cells κ≥2:

| Prime | Excluded κ | Not excluded |
|---|---|---|
| p=5 | 4 | 2 (excluded only under the FP-1 diversity hypothesis), 3 |
| p=7 | 2, 4, 5, 6 | 3 (excluded only under FP-1 diversity) |
| p=11 | 3–10 | 2 |
| p≥11 | ⌈(p+1)/4⌉ … p−1 | 2 ≤ κ < ⌈(p+1)/4⌉ |

- **R=p+δ, δ≥1:** the integer bands ⌈(p+3δ+2)/4⌉ ≤ κ ≤ ⌊(p−δ−4)/2⌋ (SEG-num) and ⌈(p+δ+1)/2⌉ ≤ κ ≤ p−δ−3 (K2P+) are excluded. Words meeting the printed hypotheses of Theorem SEG are also excluded.

## Reviews (observed identities; read-only/no tools)

| Review | Family | sha256 | Covers | Outcome |
|---|---|---|---|---|
| [Codex v4](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-arcs-v4-codex-v1.prompt.stdout.txt) | gpt-6.1-sol, max | `fb7bd1acf3a464bb3280532b8bc72a8e42a05a96b94f614160d2998259f7a396` | Foundations, FP/FP-1, K2P+, IIIb-X, ETA, RES-HI⇒REFL | 0/0/2 MINOR |
| [Claude foundations v5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-foundation-claude-v1.prompt.note.md) | claude-opus-5-5, max | `300bebdaafb9864b7d4bddecc04d514799934f40af1f2d60d5319e9b3db26224` | All v5 foundations | 0/0/11 MINOR, disposed by Part I |
| [Codex v5 corollaries](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-corollaries-codex-v1.prompt.stdout.txt) | gpt-6.1-sol, max | `7cf9cc103bb753dabc6e88c40c50d511e5ab4db742f7695477b172b949bb0880` | ARC+, SEG, SEG-p, SEG-num, MID, TOP, coverage | 1 MAJOR (R>2p) with the repair argument (§3), 1 MINOR; disposed by I.12 and Part II |
| [Claude slice A](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-erratum5-seg-negative-budget-claude-v1.prompt.note.md) | claude-opus-5-5, max | `cc36faf027b05432ab65c1346e1c539de4d90dfad792c271831d3dfcfd09bcd6` | SEG after I.12, Part II, SEG-p, SEG-num | 0/0/1; Part II ACCEPT |
| [Claude slice B](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-erratum5-mid-top-coverage-claude-v1.prompt.note.md) | claude-opus-5-5, max | `25e3312fb6483b6b03b93eb9af6f72b7bd9338105ab69c88eb3471a03827d0f9` | MID, TOP, I.14 | 0/0/7 |

Part II's argument was first given by Codex as a reviewer repair, re-derived by the worker, and accepted by Claude. Both families have therefore examined it.

## Not accepted / open

- **Separate unreviewed files are not part of this verdict:** SEG-k v2 (+ erratum `7030b758…`), TRANSFER v2, region-B v2 (+ errata) and addendum B′ (+ erratum).
- **Open cells:**
  - R=p: (5,2), (5,3), (7,3), and 2 ≤ κ < ⌈(p+1)/4⌉ for p≥11. The diversity-conditional FP-1 exclusions there do not count as coverage.
  - R=p+δ: everything outside the stated bands.
- **Deviations:** the Claude reviews of v4 and of the v5 corollaries each reached their 2700 s budget with no verdict (rc 143). They were rescoped into disjoint slices, and nothing from them is used.
- **Calibration:** these are modest written partial exclusions. They are not a matched SOTA improvement.
