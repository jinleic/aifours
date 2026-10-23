# review-package-GS-v1: standalone four-subset bound (FB) and emptiness of G (GE) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:55:47-0700. Author SunK62Regimes.
- **Candidate:** `K62-GS-v1.md`, sha256 020fdc7aacf105c224842990dbd434ecd49a86e39e2e70ca0f6ced41b57b4627 (213 lines).
  Scope frozen before the derivation: `K62-GS-SCOPE-v1.md`, sha256 cdd5f84a27f22661e479c5d8fc9b8713a62273afd758b2f192530eae9a6fc0d7
  (it discloses my authorship of K62-HD-v2/K62-GX-v1 and the parent's untrusted branch hint).
- **Excerpt manifest:** `review-excerpts-GS-v1.json`, sha256 51516ea01c4a8d20b160e3f3007afc6020531aac1864bd0446a0500cdea04e6a:
  32 inclusive ranges {path, whole-file sha256, start, end}; embedded text 85,385 bytes; JSON 8,067 bytes. **No range comes
  from K62-HD-v1/v2, the parent HD erratum or K62-GX-v1** (not premises). Hashes and ranges were checked against the current
  bytes (packaging metadata only, no scientific computation).
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/`.

## Claims under review (G = generic sub-case of the accepted CAP-DT verdict; all exponents unbounded)
- **Theorem FB:** for both families and every 4-subset Q of O, v2 T_x(Q) <= 4.
- **Theorem GE:** G has no configuration, for every e_d >= 4 (any group with finite-index subgroups, via R0).
- **Corollary OM:** with accepted K62-E3, every K6.2* configuration has a marker on a vertex of O.
Imports: parent-accepted only, at original scopes (file section 1). Not claimed: O-marked cases, M13, K7, Sun(7),
realisability; no promotion of the pending HD or GX v1 candidates.

## Proof map (file sections)
P1 O-values/edge-disjointness; P2 triangle table (DG-3, re-derived); P3 chain step with equality case (DG-4 written out,
prime-to-30 induction included); P4 apex identity/equality (L1 (T3), re-derived from L0.1); P5 EQ (CI both-tight; VFC + INV
+ Sun(2) one-tight); P6 BUD n_4(x) <= 8 - 2u(x) (E3-C2 for x'); P7 DEG ((R4)/DT-C C2, B1, B3); 3.1 T16; 3.2 ONE; 3.3 TRI;
4 FB (i) T16 => v2 k_e >= 1 => no 1-pair; (ii) no K4 => N != empty; (iii) each N-vertex v has R_v deep with tau 8;
(iv) ONE => N is one pair ab; (v) k_b = 2 = x_ba, equality Phi_b W = X^b_a (measure 2/6) and P4 force {a,b,c}, {a,b,q} to be
(2,4,4) with tau 8, contradicting ONE; 5 DEEP (DG with FB; T16 removes the capped-depth-5 alternative) and GE (each H_x
contains a diamond; B5's complement computation forbids both); 6 OM.

## Requested checks (hostile)
1. P3: base case, induction (gcd(n_e, T_x(S)) = 6 from the prime-to-30 claim), k = 6 mu, equality iff set equality,
   valuation additivity, and v2 k <= v2 m for a power of 2 m >= k.
2. P2/P4: T_x(R) = 6 w_a w_b w_c tau; divisibility by x-values; tau <= x1 x2; the apex identity tau / (6 x_ac).
3. EQ: VFC in the x-configuration (inverted configuration for alpha*), q = x' by INV (b); one-tight case; CI's full
   hypothesis set in the both-tight case.
4. BUD orientation (E3-C2 for x' needs x_(d i*) = 1, true in G for both x).
5. T16, ONE: counting with BUD; "E_i determines R_i".
6. FB (iii)-(iv): "the pairs of R_v with x = 2 are the N-edges avoiding v"; the |I| >= 3 contradiction.
7. FB (v): m_b = 2; k_b = 2; W_(R_b) inside Phi_a cap Phi_j; the (2,4,4) tau = 8 conclusion for j in {c, q}.
8. DEEP: DG's orientation and four-subset hypothesis supplied by FB; DG (b)'s single-triple alternative needs raw depth 5.
9. GE Step 1 (t(H_x) = 1 case: triangle + disjoint edge has no (2,4,4) triple) and Step 2 (diamond complement).
10. Scope: no use of f* = 1, (RC-i*), C2 at i*; 5-marker on d handled by (R4)'s CD13 form and CI's own scope.

## Mutation controls (thought experiments; nothing run)
Without T16: FB (i) fails. Without ONE: FB (iv)-(v) and GE Step 1 fail. CI' instead of EQ: T16/ONE unproved. Without
minimum degree: triangle (tau 8) + edge rs with x_sp = 2, tau 8 passes DEEP/ONE/BUD. Without edge-disjointness: diamonds
in both families possible.

## Provenance and labels
Direct new Sun instance: Sun(2) (EQ). Through imports: Sun(2), Sun(3), Sun(4). The LFC/VFC package and the K6.2* class
reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6) (efe1d849…1e29) in the transitive closure. All new
claims CANDIDATE_UNVERIFIED; written mathematics only; no computation, novelty, priority, Lean or human-review claim. The
parent owns all reviews, the verdict and any supersession of K62-HD-v2 / K62-GX-v1.
