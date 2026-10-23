# K62-GX-SCOPE-v1: frozen scope for the G-residue after Theorem HD [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:42:15-0700. Frozen **before** the
  written derivation of the statement below.
- **Owner:** SunK62Regimes. Owned path: `.../sun-coset7/continuations/k62-regimes/` only; new files only, exclusive creates.
  Written research only; global runtime HOLD respected (no computation, no enumeration code, no solver, no model call).
- **Instruction:** parent IRC (Main) after the Codex review of HD (`RUN/review/sun7-K62-HD-codex-v1.prompt.stdout.txt`:
  Theorem HD ACCEPT, corollary ACCEPT-WITH-FIXES, 0/0/1) and the parent erratum
  `RUN/review/sun7-K62-HD-parent-erratum-v1.md` (sha256 3c670e5ff49edfcfd10d4d4ab867f9a7587bd381f5105721d6565cb30d60a2e8).
  RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`. HD remains a CANDIDATE.
- **Disclosure.** Between reading that IRC and this file I formed an unwritten sketch of one possible route: the DT-A apex
  equalities ((2,4,4) with tau = 8 at the apex opposite the 2-edge; (4,4,4) with tau = 16 at all apexes) combined with
  Lemma EQ make such triples cost non-tight 4-edges; the budget n_4 <= 8 - 2u and minimum degree >= 1 then leave diamonds
  as the only source of two deep triples; B5's edge-disjointness forbids diamonds in both families. Nothing of this was
  written or checked before this freeze; it may fail and would then be reported as failed with its exact obstruction.

## 1. Setting
Exactly G of the CAP-DT verdict (`RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md`, sha256 84061c6f…34a0, item 6), as
written in `K62-HD-v2.md` section 0: K6.2*, e_d >= 4, e* = 2; no O-vertex marked (n_c = 6 w_c); 3-marker on i* (any
f* >= 2) or absent; 5-marker on d or on i* (any exponent) or absent; both distinguished entries 1; all exponents and w-parts
unbounded. Families alpha, alpha*; graphs H_x of O-pairs with x = 4; tight/non-tight as in K62-HD-v2.

## 2. Target statements (to be derived)
- **Goal A (exclusion).** G has no configuration, in any finite group (arbitrary groups via R0).
  - **A4 (e_d = 4):** to be proved from parent-accepted imports plus lemmas proved in the new file, **without** HD.
  - **A5 (e_d >= 5):** **CONDITIONAL ON HD** (statement of Theorem HD in `K62-HD-v2.md`, sha256
    6c1858c04d7da52bde8533ba71d4dcea814fb69b30a357462e36024226b9f476, read with the parent erratum above), used only to
    supply the four-subset hypothesis of Theorem DG (a).
  - **Corollary (if A holds):** with accepted K62-E3, every K6.2* configuration has a marker on a vertex of O
    (conditional on HD for e_d >= 5). Nothing about the O-marked cases, M13 or K7 is claimed.
- **Goal B (fallback if A fails in some case).** A complete explicit description of the joint O-O structures
  (H_alpha, H_alpha*, tightness, deep-triple tau values) that survive every cited rule, with the exact missing group-level
  lemma; or one explicit necessary pattern passing every cited rule (no realisability claim).

## 3. Imports allowed (parent-accepted, at accepted scopes only)
- CAP-DT verdict 84061c6f… items 5-6: DT-A section 1 apex table (both families), CI/CI'; DT-B (R4) (positive-support form),
  B1, B3, B5's edge-disjointness argument; DT-C C2 (minimum degree), all in G.
- SH-DG verdict cae455c3… (with both DG errata): DG-3 (G3 form), Theorem DG (a)/(b) with its orientation and its
  four-subset hypothesis (automatic at e_d = 4).
- K62-E3 verdict 576969dd…: Lemma 1, Lemma 2, C2 sub-claim (a), C2 (both orientations in G).
- LFC/INV verdict 8621e744…; rules-k7-v1 L1 and VFC (V1)-(V4) via verdict 73a25ba6….
- Lemma EQ and the budget/degree facts of K62-HD-v2 are **re-proved** in the new file, not imported.
- No O-marked, M13 or K7 work; no finite enumeration code; hand analysis complete in text.

## 4. Deliverables
`K62-GX-v1.md` (proof), review package and excerpt manifest (<= 100 KB embedded), all CANDIDATE_UNVERIFIED; or an
obstruction note. Checkpoints <= 1800 s apart with `/bin/date`. Computer-assisted Sun(5)/Sun(6) remain transitive imports.
No novelty, priority, Lean or human-review claim.
