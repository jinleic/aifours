# K62-GS-SCOPE-v1: frozen scope for a standalone successor of K62-HD/K62-GX (four-subset bound and emptiness of G, no HD premise) [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:50:16-0700. Frozen **before** the
  written derivation.
- **Owner:** SunK62Regimes; owned path `.../sun-coset7/continuations/k62-regimes/` only; new files only, exclusive creates;
  all older files (K62-HD-v1/v2, K62-GX-v1, their scopes, packages, manifests, checkpoints) stay immutable.
  Written research only; no computation (no compute GO); no model call.
- **Instruction:** parent IRC (Main) after receiving the GX v1 packet: "optional next written obligation AUTHORIZED";
  standalone successor proving every 4-subset raw depth <= 4 in G and then G empty for all e_d >= 4, without importing HD
  or GX v1 as premises.
- **Disclosure of prior knowledge.** I authored K62-HD-v2 (Cases A, B1-B4) and K62-GX-v1 (EQ, BUD, DEG, T16, ONE, TRI,
  DEEP); checkpoint-003 noted that T16 and ONE should shorten HD's Cases A/B1/B3. The parent's IRC contains an explicitly
  UNTRUSTED branch hint (T16 removes tau-16 branches; Case A immediate; one 2-edge -> two (2,4,4) tau-8 triples vs ONE;
  two adjacent 2-edges -> measure 1/6 vs 2/6; disjoint 2-edges -> several tau-8 triples; triangle of 2-edges -> k = 4,
  equal X-sets, EQ/BUD or E3 Lemma 2). Every step will be derived in the new file; nothing in the hint or in the old files
  is assumed true.

## 1. Setting
Exactly G of the CAP-DT verdict (`RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md`, sha256 84061c6f…34a0, item 6):
K6.2*, e_d >= 4, e* = 2; n_c = 6 w_c for every c in O; 3-marker on i* (any f* >= 2) or absent; 5-marker on d or i* (any
exponent) or absent; both distinguished entries 1; all exponents and w-parts unbounded. RUN :=
`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

## 2. Target statements (to be derived in ONE coherent file, `K62-GS-v1.md`)
- **Theorem FB (four-subset bound).** In G, for both families x and every 4-subset Q of O: v2 T_x(Q) <= 4.
- **Theorem GE (G empty).** G has no configuration, for every e_d >= 4, in any finite group (arbitrary groups via R0).
- **Corollary OM.** With accepted K62-E3, every K6.2* configuration has a marker on a vertex of O.
- Inside the same file, with full proofs: the chain step with its equality case (the accepted DG-4 chain, written out),
  the apex identity/equalities, Lemma EQ, the budget n_4(x) <= 8 - 2u(x), the degree facts, T16, ONE, the graph lemma,
  and the two-deep-triples lemma.

## 3. Imports allowed (parent-accepted only, at their original scopes)
- CAP-DT verdict 84061c6f… items 5-6: DT-A section 1 apex table (both families, admissible only) and CI; DT-B (R4) in its
  CD13 positive-support form, B1, B3, B5's edge-disjointness computation; DT-C C2 (minimum degree); in G only.
- SH-DG verdict cae455c3… with both mandatory DG errata: DG-3 (G3 form), DG-4 (unmarked added vertex, raw depths),
  Theorem DG (a)/(b) with its orientation and four-subset hypothesis.
- K62-E3 verdict 576969dd…: Lemma 1, Lemma 2, C2 sub-claim (a), Lemma 3 proof form for every non-empty Q in O, C2.
- LFC/INV verdict 8621e744…; rules-k7-v1 L1 and VFC (V1)-(V4) via verdict 73a25ba6….
- **Not imported:** K62-HD-v1/v2 (Theorem HD, its lemmas), the parent HD erratum, K62-GX-v1 (any lemma or theorem).

## 4. Fallback
If some branch of Theorem FB cannot be closed by written argument, the deliverable is an obstruction note giving the exact
surviving local data on Q (values, tau's, tightness, chain multipliers) and the smallest missing lemma; K62-GX-v1
(conditional on HD) remains the reviewable conditional proof.

## 5. Deliverables and process
`K62-GS-v1.md`, a review package and an excerpt manifest (<= 100 KB embedded), all CANDIDATE_UNVERIFIED; checkpoints
<= 1800 s apart with `/bin/date`; paths and SHA256 sent to the parent. Computer-assisted Sun(5)/Sun(6) remain transitive
imports. No M13, O-marked or K7 work. No novelty, priority, Lean or human-review claim.
