# K62-HD-SCOPE-v1: frozen scope for the higher-depth alternative of Theorem DG inside G [CANDIDATE_UNVERIFIED target]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:10:11-0700 (directory created at
  that reading; this file is the first file in it). Frozen **before** any derivation of the statement below.
- **Owner:** SunK62Regimes. Owned path: `.../sun-coset7/continuations/k62-regimes/` only. Written research only; the global
  runtime HOLD is respected (no science computation, no enumeration script, no solver, no model CLI call).
- **Not worked on (pending items owned elsewhere):** M13 = (1,3)/(3,1) orientation with t in O, f* = 1
  (`k63-residue/k62-followon/review-package-M13-v2.md`); K7 family F (`k7-k62-residue/K7-family-closure-map-v2.md`).
  Nothing below uses or restates either.

## 1. Choice of regime and justification
Candidates (i) f* >= 2, (ii) 5-marker on d, (iii) higher-depth alternative for e_d >= 5. Chosen: **(iii), restricted to
the generic sub-case G** of the CAP-DT verdict (item 6).
- (i) and (ii) are sub-regimes of the remaining G-patterns whose difference from the generic f* = 1 / no-5 case is only
  that some accepted bound is lost ((RC-i*) for f* >= 2; label isolation of the i*/d pair for 5-on-d). A complete
  exclusion of either would need to close G-patterns that are open even with those bounds, so neither has a credible
  self-contained written route.
- (iii) is a self-contained statement about a single 4-subset Q of O: Theorem DG (a)/(b) needs every 4-subset to have
  capped depth <= 4, and for e_d >= 5 this hypothesis is not supplied. Lemma DG-4 (accepted, raw depths) turns a raw
  depth >= 5 into strong local conditions (4-edges, deep triples, forced apex equalities), and these collide with the
  accepted G-constraints CI', B1-B3, K62-E3 C2 and DT-C C1, which punish 4-edges and non-tight 4-pairs. A preliminary
  plausibility look (one sub-case only, not a proof) suggested the collision is strong. Hence a credible finite written
  case analysis with all exponents unbounded.

## 2. Exact setting (CAP section 0, specialised to G)
V = {d, i*} disjoint-union O, |O| = 5; n_d = 2^(e_d) 5^(h_d) w_d with **e_d >= 4** (so e* = 2); n_(i*) = 4 * 3^(f*) 5^(h*) w_*;
n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O); w's pairwise coprime and coprime to 30. **G:** no vertex of O carries a marker
(f_c = 1, h_c = 0 for all c in O); the 3-marker lies on i* (f* >= 2, any value) or is absent (f* = 1); the 5-marker lies on
d (h_d >= 1, any value), on i* (h* >= 1, any value) or is absent. Then (alpha_(d i*), alpha*_(d i*)) = (1,1) (K62-E3 Lemma 1).
Families x in {alpha, alpha*}, x' the other. For Q contained in O, the **raw depth** is v2 T_x(Q), T_x(Q) := [G : intersection
of Phi^x_c, c in Q]; the capped depth is min(e_d, v2 T_x(Q)).

## 3. Candidate statement (to be derived; CANDIDATE_UNVERIFIED)
**Theorem HD.** In G (any e_d >= 4, every admissible f*, h_d, h*, w), for both families x in {alpha, alpha*} and every
4-subset Q of O: **v2 T_x(Q) <= 4.**
**Corollary HD.** In G with e_d >= 5 no 4-subset of O has capped depth >= 5 in either family: the higher-depth alternative
of Theorem DG (b) is empty, and the four-subset hypothesis of Theorem DG (a) holds for both families for every e_d >= 4.
Consequently, in G, each family has at least two O-triples of capped depth >= 4, or exactly one, of capped depth 5
(values (4,4,4), tau = 16, e_d >= 5) - the conclusion of Theorem DG (b) at its accepted scope.
- Scope of the claim: exactly G as in section 2. **Not claimed:** any O-marked case, (1,3)/(3,1), any exclusion of G or of
  K6.2*, any pattern realisability statement, full K6.2*, K7, Sun(7).

## 4. Imports allowed (parent-accepted, at their accepted scopes only)
- CAP-DT verdict 84061c6f… items 1-6: DT-A section 1 apex table (both families, admissible only), CI/CI' (unmarked v,
  x_(d i*) = 1), DT-B (R3), (R4), B1-B5, DT-C C1 budget and consequences, all in G; RC-O at unmarked O-vertices.
- SH-DG verdict cae455c3… with both DG errata: DG-3 (G3 form), DG-4 (unmarked added vertex, raw depths, family swap by
  INV in G), Theorem DG with its orientation and four-subset hypothesis.
- K62-E3 verdict 576969dd…: Lemma 1, Lemma 2, C2 sub-claim (a), Lemma 3 proof form, C1, C2 (orientation as stated).
- LFC/INV verdict 8621e744… (LFC (a)-(d), INV (a)-(b), E6); rules-k7-v1 L0.3, L1 (T rule) via verdict 73a25ba6…
- Any further step is proved in the proof file itself. Hand case analysis only, complete in text.

## 5. Deliverable and fallback
- Success: proof file `K62-HD-v1.md`, review package and excerpt manifest (<= 100 KB embedded), all CANDIDATE_UNVERIFIED.
- Failure of any case: an obstruction note giving the explicit surviving local pattern on Q (values, tau's, tightness) and
  the smallest missing lemma; failed arguments preserved with their exact obstruction.
- Provenance to disclose: computer-assisted Sun(5)/Sun(6) remain in the import closure (LFC package, class reduction).
- No novelty, priority, Lean or human-review claim.
