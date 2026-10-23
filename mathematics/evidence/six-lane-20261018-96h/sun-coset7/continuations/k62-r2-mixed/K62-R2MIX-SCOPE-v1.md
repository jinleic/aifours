# K62-R2MIX-SCOPE-v1: frozen scope for the missing lemma L-R2 of M3(1,1) via a mixed-family (paired-fibre) route [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this write: 2026-10-19T12:01:42-0700. Frozen **before** any written
  derivation in this directory.
- **Owner:** SunR2MixedFibres (task worker of the math-1 sun-coset7 lane). Owned path, new files only:
  `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/`.
  Every file is created once, to a path checked to be absent immediately before, and never rewritten; corrections are new
  numbered versions. Written research only: no computation, enumeration, process, model call, import or runtime.
- **Instruction:** parent (Main) assignment: attack the missing lemma (L-R2) of `K62-M3R-v2.md` section 7 (c) with a new
  paired-fibre / product-equality argument that couples the opposite-family equality
  Phi_e(Phi_d cap Phi_(i*)) = Phi_ePhi_d (tau_y'({d, i*, e}) = 3) with actual occupied / light fibre sets, not by repeating the
  exhausted single-vertex LP / counting at t. RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62R := `.../sun-coset7/continuations/k62-regimes` (frozen definitions and evidence).

## 1. Premise discipline (fixed now)
- **Accepted imports, original scopes only:** R0, L0.1, L0.2, L0.6 = Sun(2), Sun(3), Sun(4) (old README section 0-1,
  `six-lane-20261016/sun-coset7/README.md`); Sun(5), Sun(6) computer-assisted and transitive; LFC (a)-(d) and INV (a)-(b)
  (RUN/review/sun7-lfc-inv-parent-verdict-v1.md, sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18,
  items 1-2, 6; erratum E1, E3, E6, E7); L1 (T1)-(T3) and VFC (V1)-(V4) (rules-k7-v1.md; RUN-2026-10-16 written verdict
  73a25ba6...9f35); K62-E3 at the scopes of RUN/review/sun7-K62E3-parent-verdict-v1.md (sha256
  576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f): Lemma 2 and C2 sub-claim (a); the CAP setting of
  RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md (sha256 84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0).
- **Pending, never imported as results:** `K62R/K62-M3R-v2.md` (sha256
  af2b965bf69b252e266064aff5b201b16757bcb76af152d7eee8c89ee77888b3; parent erratum RUN/review/sun7-K62-M3R-parent-erratum-v1.md,
  sha256 cb42f3e77c63c2932a17ccbf041df81c3f81f5bd4ba402a758d5119395df34c7; one Codex family returned, second family queued;
  CANDIDATE). Each of its lemmas that a proof here needs (Lemma A, Lemma C, R2N (i)-(iii), Theorem RR) is either re-proved in
  the new text or appears only as an explicitly labelled conditional premise. `K62R/K62-MK-v2.md` (sha256
  ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9, parent erratum f84defc8...) is used only as the explicit
  conditional premise of a navigation corollary. Definitions (M3(1,1), R1-/R2-instances) are repeated, not imported as
  results. M13 ((1,3)/(3,1)) is neither used nor touched. FH is not used.

## 2. Target statements (fixed now)
**Setting:** the full class M3(1,1) exactly as in K62-MK-v2 section 0 / K62-M3R-v2 section 0: K6.2*, e_d >= 4, e* = 2,
f* = 1, the 3-marker on t in O (f_t >= 2), (alpha_(d i*), alpha*_(d i*)) = (1,1), the 5-marker on d, on i*, on t, on some
p in O' := O minus {t}, or absent; all exponents and w-parts unbounded; any group with finite-index subgroups (via R0).
- **Theorem R2X (primary):** no configuration of M3(1,1) has a family y with y_tu in {1, 2} for all four u in O'.
- **Corollary R1X:** no configuration of M3(1,1) has an R1-instance — derived from R2X with Theorem RR, which is re-proved
  in the new text or else stated as CONDITIONAL ON K62-M3R-v2 Theorem RR.
- **Corollary M3E (CONDITIONAL ON K62-MK-v2 Theorem M3R, pending):** M3(1,1) is empty. Navigation only.
- **Fallback (if R2X is not achieved):** an obstruction note: (a) the exact failing step of the new route, (b) every genuinely
  new necessary consequence for an R2-instance derived in writing, (c) any restricted sub-case proved, separately named by its
  exact defining condition with the full target stated OPEN, or (d) a concrete abstract counterexample to a proposed local
  implication (never a fabricated group configuration). No other claim.

## 3. Route (pre-freeze disclosure, unwritten and unchecked)
Before this freeze I sketched, in thought only: (1) the d-fibre system of the OPPOSITE configuration y' (all six labels at
d have pairwise gcd 3, so at most three pieces per fibre) with pair granularity from y on the pairs {t, u}: the number of
d-fibres containing both t and u would be at least n_d / 2^(1 + v2 y_tu), while the sum over u in O' is at most n_d minus
the number of d-fibres shared by t and i*; (2) tau_y'({d, i*, e}) = 3 is equivalent to
(Phi'_d cap Phi'_e)(Phi'_d cap Phi'_(i*)) = Phi'_d inside the y'-subgroup of d, which would forbid e and i* from ever sharing
a d-fibre of the y'-configuration; (3) counting the d-fibres of e might then contradict. Any of this may fail; failures will
be preserved with their exact obstruction.

## 4. Deliverables
`K62-R2MIX-v1.md` (proof or obstruction note, with an interface table citing original scopes), `review-package-R2MIX-v1.md`,
`review-excerpts-R2MIX-v1.json` (entries {path, sha256, start, end}; <= 100 KB embedded), checkpoints <= 1800 s apart (target
1200 s) with `/bin/date`. Every new claim CANDIDATE_UNVERIFIED. No computation, enumeration, novelty, priority, Lean,
human-review or full-Sun(7) claim; Sun(5)/Sun(6) remain computer-assisted transitive imports.
