# review-package-MK-v1: O-marked (1,1) part of the K6.2* residue — Theorem M5 and the M3(1,1) residual classification [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:22:27-0700. Author SunK62Regimes.
- **Candidate:** `K62-MK-v2.md`, sha256 ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9 (268 lines). It supersedes
  the undelivered draft `K62-MK-v1.md` (898ad865…; header mapping of scope items and one chain parenthetical only).
  Scope frozen before the derivation: `K62-MK-SCOPE-v1.md`, sha256 12cad4f7e9f7d29c5aa7d7520bda50534b3ecd64702cf4198ff01050ef0ef1bd.
- **Excerpt manifest:** `review-excerpts-MK-v1.json`, sha256 d7c25ea3f9111d851bdeebcb7e0e1f336f5805f5fd749bccbd069c73819cd388:
  29 inclusive ranges {path, whole-file sha256, start, end}; embedded text 89,572 bytes; JSON 7,302 bytes. No range comes from
  the pending K62-GS, K62-HD or K62-GX files (not premises). Hashes and ranges checked against current bytes (packaging metadata
  only, no scientific computation).
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/`.

## Claims under review (class K = K6.2*, e_d >= 4, e* = 2, orientation (1,1), some O-vertex marked; exponents unbounded)
- **Theorem MK:** no configuration of K satisfies NR (no R1-instance and no R2-instance; vacuous in M5).
- **Theorem M5:** M5 (5-marker on p in O, no 3-marker on O) is empty.
- **Theorem M3R:** every M3(1,1) configuration (3-marker on t in O) has an R1-instance (tight equal-X pair at t; then
  9 | T_x(V minus {t}) and some x_(e i*) >= 3) or an R2-instance (a t-row with four O-entries in {1,2}; then its i*-entry is 2,
  9 | T_x'(V minus {t}) and some x'_(e i*) >= 3).
- **Corollary M3G:** M3(1,1) is empty when 9 divides neither T_alpha(V minus {t}) nor T_alpha*(V minus {t}), e.g. when every
  i*-entry on O minus {t} lies in {1, 2} in both families.
- **Section 7:** the obstruction note required by the scope (failing steps at t; missing lemmas L-R1, L-R2 or Gt).
Not claimed: M13 ((1,3)/(3,1)), K7, Sun(7), realisability, acceptance of GS/HD/GX.

## Key new points to check (hostile)
1. ell_c = n_c / 6 odd and pairwise coprime with markers; gcds of O-labels at any O-vertex are gcds of 2-parts (EQ*'s
   one-tight case, CI* steps 2/4/5, R4*'s certificates).
2. P3 proved for adding e != t only (gcd 6), with (a) established by building S with t first; FB-M never adds t.
3. GR: chain d, i*, (t), others; gcd(n_e, T_m) = 6 at every step; (a) Gamma = 6 off t; (b) at t, Gamma = 6 iff 9 does not
   divide T; (c) y_(e i*) = 3 forces 9 | T_y(V minus {t}).
4. RC (light fibres) re-proved for any vertex; CI* re-proved at any O-vertex with Gamma_x(v) = 6 (uses the family's OWN
   granularity), RC uses the OPPOSITE family's.
5. R4*: certificates c0, c1 (z in {1,3}), c2 (z in {4,5}); z = 5 needs h_d >= 1 by L1 on {d, i*, t}; LP-free value checks;
   at v != t the 5/6 bound kills c0's 11/2.
6. T16 without NR (EQ* only at apexes != t); ONE, DEG under NR.
7. FB-M case split (iv-a)/(iv-b)/(iv-c) and steps (v)-(vii), in particular N = {ta, ab} via minimum degree of the fifth vertex.
8. DEEP via DG (any markers, orientation (1,1)); MK Steps 1-2 as in the generic case.
9. Exactness of the scope mapping: Theorem M5 complete; M3(1,1) only items (a)-(d).

## Mutation controls (thought experiments; nothing run)
Granularity 18 at t (some y_(e i*) = 3): c0's 11/2 survives RC (17/18), so R2-instances are not excluded. Using (N_t) in FB-M
fails for a (4,4,4) tau-12 triangle off t (gcd 18). Without the T rule, z = 5 with h_d = 0 at t would need another
certificate. Without E3-L2, val(c0) changes. Without edge-disjointness, diamonds in both families survive.

## Provenance and labels
Direct new Sun instances: Sun(2) (EQ*, R4*), Sun(3) (CI*, R4*). Through imports: Sun(2), Sun(4). The LFC/VFC package and the
K6.2* class reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6) (efe1d849…1e29) in the transitive
closure. All new claims CANDIDATE_UNVERIFIED; written mathematics only; no computation, novelty, priority, Lean or human-review
claim. The parent owns all reviews and the verdict.
