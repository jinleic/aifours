# review-package-GX-v1: Theorem GX (the generic sub-case G is empty) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:47:57-0700. Author SunK62Regimes.
- **Candidate:** `K62-GX-v1.md`, sha256 f3336b1f28c36a4485b6ada675dfdf7f5896c27e341b8fad2a28970207bff070 (181 lines).
  Scope frozen before the written derivation: `K62-GX-SCOPE-v1.md`, sha256
  56103d95a26e3ace6caed1a9abdf0092c1dcf6b62f2afd2343eba2719f9c16b5 (its disclosure records an unwritten route sketch that
  preceded the freeze).
- **Excerpt manifest:** `review-excerpts-GX-v1.json`, sha256 53fecc3733ed39e75e8c0ac4ae299c4b407ac6f9efb5f7fe1c79762150ff5391:
  35 inclusive ranges {path, whole-file sha256, start, end}; embedded text 82,682 bytes; JSON 8,859 bytes. Hashes and ranges
  were checked against the current bytes (packaging metadata only, no scientific computation).
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/`.

## Claim under review
In the generic sub-case G of the accepted CAP-DT verdict (K6.2*, e_d >= 4, e* = 2; no O-vertex marked; 3-marker on i*
with any f*, or absent; 5-marker on d or i* with any exponent, or absent):
- **GX (a):** no configuration has e_d = 4 — from parent-accepted imports and lemmas proved in the file, **without HD**;
- **GX (b), CONDITIONAL ON HD:** no configuration has e_d >= 5; HD (candidate `K62-HD-v2.md` 6c1858c0…, with parent erratum
  3c670e5f…) is used only to supply the four-subset hypothesis of Theorem DG (a);
- **Corollary OM:** with accepted K62-E3, every K6.2* configuration has a marker on an O-vertex (e_d >= 5 part conditional
  on HD).
Not claimed: any O-marked case, M13, K7, Sun(7), realisability, acceptance of HD.

## Proof map (all in K62-GX-v1.md)
2.1 apex equality (L1 (T3); DT-A table instances (2,4,4) tau 8 and (4,4,4) tau 16); 2.2 deep types (DG-3); 2.3 Lemma EQ
(re-proved: CI for both-tight; VFC (V1)-(V4) + INV (b) + Sun(2) for one-tight); 2.4 BUD n_4(x) <= 8 - 2u(x) (E3-C2 for
x' + edge-disjointness); 2.5 DEG (DT-C C2 / (R4), B1, B3); **2.6 T16** (no (4,4,4) tau 16: three apex equalities -> EQ -> u >= 3
-> n_4 <= 2 < 3); **2.7 ONE** (at most one (2,4,4) tau 8 per family; it costs u >= 2); **2.8 TRI** (graph lemma: <= 2
triangles, two share an edge); **2.9 DEEP** (DG (b) + T16: two tau-8 deep triples per family); **Theorem GX**: Step 1, each
H_x contains a diamond (t(H_x) <= 1 forces triangle + disjoint edge by DEG, which has no (2,4,4) cherry); Step 2, B5's
complement computation forbids diamonds in both families.

## Requested checks (hostile)
1. 2.1: (T3) at apex v in the x-configuration, gamma_v = 6; equal measure plus inclusion gives the set equality.
2. 2.3 EQ: VFC applied to the x-configuration (inverted configuration for x = alpha*), q = x' by INV (b); one-tight case
   D_b = Y, D_a inside D_b, labels w_a and 2 w_b coprime; both-tight case is exactly CI's hypothesis set.
3. 2.4 orientation: E3-C2 for x' requires x_(d i*) = 1 (true in G for both x).
4. 2.6/2.7 arithmetic and the "E_i determines R_i" step.
5. 2.8: exhaustive case split for a third triangle (degree-4 vertex or K4).
6. 2.9: DG's four-subset hypothesis automatic at e_d = 4 (verdict cae455c3… item 4); for e_d >= 5 exactly HD; the DG (b)
   alternative "only one deep triple" has capped depth 5, hence tau 16, excluded by T16.
7. Step 1: with t(H_x) = 1 and n_4(x) <= 4, minimum degree forces H_x = triangle + disjoint edge; no (2,4,4) cherry.
8. Step 2: complement of a diamond in K5 has exactly one triangle.
9. Scope: no use of f* = 1, (RC-i*), i*-rows or d-row counts beyond the cited imports; 5-marker on d handled by the CD13
   positive-support form of (R4) and by CI's own scope.

## Mutation controls (thought experiments; nothing run)
EQ replaced by CI' alone: triangle (tau 8) plus a pendant (2,4,4) tau-8 cherry with u = 1 passes the counts. Minimum degree
dropped: triangle + pendant edge rs with x_sp = 2, tau 8 passes DEEP/ONE/BUD (u = 2, n_4 = 4). Edge-disjointness dropped:
both families could carry diamonds. T16 dropped: at e_d >= 5 the single capped-depth-5 alternative of DG (b) survives.

## Provenance and labels
Direct new Sun instance: Sun(2) (Lemma EQ). Through imports: Sun(2), Sun(3), Sun(4). The LFC/VFC package and the K6.2* class
reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6) (efe1d849…1e29) in the transitive closure. All new
claims CANDIDATE_UNVERIFIED. Written mathematics only; no computation, novelty, priority, Lean or human-review claim. Parent
owns all reviews and the verdict.
