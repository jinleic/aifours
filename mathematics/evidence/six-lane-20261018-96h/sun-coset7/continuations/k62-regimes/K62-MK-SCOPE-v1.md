# K62-MK-SCOPE-v1: frozen scope for the O-marked (1,1) part of the K6.2* residue [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:04:40-0700. Frozen **before** the
  written derivation.
- **Owner:** SunK62Regimes; owned path `.../sun-coset7/continuations/k62-regimes/` only; new files only (exclusive
  creates); every older file immutable. Written research only; no compute GO; no model call; no enumeration code.
- **Instruction:** parent IRC (Main) after the GS dual-review freeze `RUN/review/sun7-K62-GS-review-freeze-v1.json`
  (0ef99649…4638): new written obligation on K6.2*, e_d >= 4, e* = 2, (alpha_(d i*), alpha*_(d i*)) = (1,1), with an
  O-marker; M13 orientations (1,3)/(3,1) and K7 family F excluded. RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Premise discipline:** K62-GS-v1, K62-HD-v1/v2 and K62-GX-v1 are NOT imported (pending candidates). Every step needed
  from them is re-proved in the new file, adapted to markers, or the result is stated as explicitly conditional.
- **Disclosure (pre-freeze feasibility look, unwritten):** at an O-vertex v the LFC/VFC labels of the other O-vertices are
  ell_u x_vu with ell_u := n_u / 6 odd and pairwise coprime, markers included, so the coprimality used in EQ's one-tight
  case survives every marker; at the 5-only-marked vertex p, gcd(n_p, .) of every chain is 6, which suggests that the
  granularity bound (C1), CI, RC, (R4)/B1-B3 and the chain step all transfer to p; at the 3-marked vertex t, gcd(n_t, .)
  can contain 9 (a (4,4,4) triangle with tau = 12 off t, or chain multipliers 3 at d/i*), so the chain step that adds t,
  CI at t and the row bound at t are expected to be the breaking points.

## 1. Classes (exact)
Common setting: K6.2* (accepted class definition, setting of the CAP-DT verdict section "Accepted scopes"), e_d >= 4,
e* = 2, all exponents and w-parts unbounded.
- **M5** := the 5-marker lies on a vertex p of O (h_p >= 1) and no 3-marker lies on O (the 3-marker is on i* or absent).
  By K62-E3 Lemma 1 the orientation is then automatically (1,1). Here h_d = h* = 0.
- **M3(1,1)** := the 3-marker lies on a vertex t of O (f_t >= 2, so f* = 1) and (alpha_(d i*), alpha*_(d i*)) = (1,1); the
  5-marker anywhere admissible (d, i*, t itself, another O-vertex p, or absent).
- The O-marked (1,1) class is exactly M5 disjoint-union M3(1,1).

## 2. Targets (statements fixed now)
- **Theorem M5 (complete-proof target):** M5 has no configuration (any group with finite-index subgroups, via R0).
- **Part M3 (attempt):** Theorem M3: M3(1,1) has no configuration. If this is not achieved, the deliverable for M3(1,1)
  is an **obstruction note** containing exactly: (a) each step of the M5 proof that fails or is unproved at t, with the
  precise reason; (b) the smallest missing lemma(s), stated as exact hypotheses on configurations; (c) any statement
  proved for M3(1,1) under those hypotheses, labelled CONDITIONAL with the hypotheses written out; (d) any sub-case of
  M3(1,1) proved unconditionally, with its exact defining condition. No other claim about M3(1,1).
- Nothing is claimed about M13 ((1,3)/(3,1)), K7, Sun(7), realisability of patterns, or acceptance of GS/HD/GX.

## 3. Imports allowed (parent-accepted, original scopes)
- CAP-DT verdict 84061c6f… items 1-6 (C1 at unmarked O-vertex with x_(d i*) = 1; RC-O; CI/CI' at unmarked v; DT-A apex
  table; DT-B/DT-C only in G, hence re-proved where used outside G).
- SH-DG verdict cae455c3… (both DG errata): DG-3, DG-4 (unmarked added vertex), Theorem DG with orientation and four-subset
  hypothesis (any markers).
- K62-E3 verdict 576969dd…: Lemma 1, Lemma 2, C2 sub-claim (a), Lemma 3 proof form, C1, C2 (any markers).
- LFC/INV verdict 8621e744…; rules-k7-v1 L1, VFC via verdict 73a25ba6…; R0 and L0.1 (old README).
- Everything else is proved in the new file(s).

## 4. Deliverables and process
`K62-MK-v1.md` (proof of Theorem M5 and the M3(1,1) part or its obstruction note), review package and excerpt manifest
(<= 100 KB embedded), all CANDIDATE_UNVERIFIED; checkpoints <= 1800 s apart with `/bin/date`; paths and SHA256 to the
parent. Computer-assisted Sun(5)/Sun(6) remain transitive imports. No novelty, priority, Lean or human-review claim.
