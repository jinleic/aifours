# K62-M13X-SCOPE-v1: frozen scope for a mixed-family route to the full M13 orientations (1,3)/(3,1) of K6.2* [target; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this write: 2026-10-19T12:32:06-0700. Frozen **before** any written derivation in this
  directory (the directory was created empty at 2026-10-19T12:31:26-0700).
- **Owner:** SunM13MixedFibres (task worker, math-1 sun-coset7 slot of the six-lane 96h round). Owned path, new files only:
  `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-m13-mixed/`.
  Every file is created once with exclusive-create mode `x` and never rewritten; corrections are new numbered versions or
  errata. Written mathematics only: no computation, enumeration, solver, Lean, source import, test, build, model call,
  nested agent, /tmp use, commit or push. Hash/byte/range metadata only.
- **Authority:** parent transition `RUN/control/mathematics-slot-transitions-20261019-1230-v1.json`, sha256
  7317001625115b2be565642a3130e3072c5771ca4a585b700512ebfa5ffbb89f (slot math1: "mixed-family route for full
  M13orientation(1,3)/(3,1), notnewthirdproblem"). RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
  This is not extra target or runtime authority.

## 1. Target (fixed now)
**Setting M13.** Class K6.2* of the old README section 5 (sha256 2a6d6d6e…3fd1): V = {d, i*} disjoint-union O, |O| = 5,
n_d = 2^(e_d) 5^(h_d) w_d, n_(i*) = 2^(e*) 3^(f*) 5^(h*) w_*, n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O), w's pairwise coprime and
coprime to 30, gcds 6 inside {i*} cup O, 4 on d-i*, 2 on d-O; with the joint d-i* entry
(alpha_(d i*), alpha*_(d i*)) in {(1,3), (3,1)}. By accepted K62-E3 (verdict 576969dd…0fb0f) every K6.2* configuration
has e_d >= 4, e* = 2, and an entry 3 at d-i* forces the 3-marker t in O (f_t >= 2) and f* = 1. The 5-marker may be on d,
i*, t, some p in O' := O minus {t}, or absent. All exponents and w-parts unbounded; arbitrary groups with finite-index
subgroups via R0.
- **Primary target, Theorem M13X:** no configuration of M13 exists. The orientation (3,1) is to be handled by applying the
  (1,3) argument to the ACTUAL inverted configuration (INV (a)-(b) with E6: its alpha-matrix is alpha*, its index tuple
  and markers are unchanged), not by a symmetry assertion.
- **Fallback (if M13X is not achieved):** (a) the exact failing step of the attempted route with its arithmetic retained;
  (b) every genuinely new necessary constraint for M13 derived in writing; (c) any restricted subclass proved, separately
  NAMED by its exact defining condition, with the full M13 target stated OPEN; (d) a local-incidence countermodel to a
  proposed implication (an abstract incidence pattern, clearly NOT a group configuration), with the exact smallest missing
  bridge. Never call a conditional or restricted statement "full M13". Sun7 and full K7 are outside this scope.

## 2. Premise discipline (fixed now)
- **Accepted imports, at their original verdict scopes only:** R0, L0.1, L0.2, L0.6 = Sun(2), Zhu Sun(3), Sun(4) (old
  README section 0-1; RUN-2026-10-16 written verdict 73a25ba6…9f35); accepted Sun(5), Sun(6) (computer-assisted,
  transitive, verdicts 2cf02436…5301, efe1d849…1e29) only through LFC(c)/VFC(V3) and the class reduction; E1 (L0.3);
  LFC (a)-(d), INV (a)-(b), E3/E6/E7 and the R0 lift (RUN/review/sun7-lfc-inv-parent-verdict-v1.md, sha256
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18, with K7-LFC-INV-erratum-v1 7af9acf0…); rules-k7-v1 L1
  (T1)-(T3) and VFC (V1)-(V4) (written verdict 73a25ba6); K62-E3 Lemmas 1-3, step 3 and C1/C2 at the scopes of
  RUN/review/sun7-K62E3-parent-verdict-v1.md (sha256 576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f) with
  errata v1-v2; the CAP setting and C1/C2/RC-O/RC-i* interfaces of RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md (sha256
  84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0) with its mandatory overlays (CAP-DT errata v1-v2); SH/DG
  at the scopes of RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md (cae455c3…) if used.
- **Pending, never imported as results:** M13 package `k63-residue/k62-followon/review-package-M13-v2.md` (d6a07082…) with
  K62-M13-A/B/C/D-v1 and K62-M13-erratum-v1 (Codex c8c4184b returned 0F/0M/1m; Claude running; no verdict); K62-R2MIX-v2
  (b75e6dc7…0806, package a4cab369…, manifest 9500f7b9…; no verdict). Any of their statements needed here is either
  re-proved in the new text (attributed) or appears only as an explicitly labelled CONDITIONAL premise. MK, M3R, GS, HD at
  other orientations are not premises. FH, Sun(7), any engine/probe output: not used.

## 3. Route (pre-freeze disclosure; thought only, unwritten and unchecked)
Before this freeze I only read the inputs. While reading I restated, without new derivation, the label gcds at d in both
configurations of (1,3): in the alpha-configuration all six d-labels have pairwise gcd 3 (so at most three pieces per
d-fibre); in the inverted configuration gcd(lambda*_t, lambda*_(i*)) = 9 and all other pairs 3 (so four-piece d-fibres
must contain t and i*; M13-A (e) says at least n_d/4 + 3 of them). Planned attack, any part of which may fail:
(1) re-prove, for M13, the general light-fibre and product-separation lemmas (R2MIX Lemmas 1-2) and the M13-A fibre facts
needed; (2) couple the four-piece d-fibres of the inverted configuration (each containing t and i*) with the
opposite-family (alpha) structure at the marked vertex t or at i* — e.g. product equalities / tau values of triples
containing t, i*, d — so that a forced fibre sharing contradicts a separation; (3) keep track of the t/i* odd-label gcd 9,
the four-piece cap and the i*-degree 3n_d/4, where the (1,1) argument of R2MIX fails verbatim. No bound on f_t, h, w or e_d
may be imposed silently.

## 4. Deliverables
`K62-M13X-v1.md` (complete written proof, or obstruction note per the fallback, with a scope/import table citing original
scopes), `review-package-M13X-v1.md`, `review-excerpts-M13X-v1.json` (entries {path, sha256, start, end}; <= 100 KB
embedded), checkpoints `checkpoint-NNN-v1.md` at most 1800 s apart (target 1200 s, waits included), each with `/bin/date`.
Every new claim CANDIDATE_UNVERIFIED. No novelty/priority/"first", human, Lean or full-target claim; Sun(5)/Sun(6) remain
computer-assisted transitive imports. Parent owns model reviews and verdicts. Park after the deliverable.
