# review-package-HD-v1: Theorem HD (G: every 4-subset of O has raw depth <= 4) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:20:50-0700. Author SunK62Regimes.
- **Candidate:** `K62-HD-v2.md`, sha256 6c1858c04d7da52bde8533ba71d4dcea814fb69b30a357462e36024226b9f476 (this directory).
  Scope frozen before derivation: `K62-HD-SCOPE-v1.md`, sha256 c0cbb507adc8d23fb5894e02744d1176ba27f613b904c0ddb40739feb0702f82.
  Superseded draft, not for review: `K62-HD-v1.md` 52611b80… (hash suffix, L0.1 location, one wording; no math change).
- **Excerpt manifest:** `review-excerpts-HD-v1.json`, sha256 a634044497b019c05e5a6d01d57bfe9227bfa358ca287134ccc7fe632ee56008:
  30 inclusive ranges {path, whole-file sha256, start, end}; embedded text 84,589 bytes; JSON 7,584 bytes. All hashes and
  ranges were checked against the current bytes (packaging metadata only, no scientific computation).
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/`.

## Claim under review
In the generic sub-case G of the accepted CAP-DT verdict (no O-marker; 3-marker on i* with any f*, or absent; 5-marker on
d or i* with any exponent, or absent; every e_d >= 4, e* = 2), for both families x in {alpha, alpha*} and every 4-subset Q
of O: v2 [G : intersection of Phi^x_c, c in Q] <= 4. Corollary: for e_d >= 5 no 4-subset has capped depth >= 5 (the
higher-depth alternative of Theorem DG (b) is empty in G), so Theorem DG (a)/(b) apply in G to both families with no
remaining hypothesis. Nothing else is claimed: no exclusion of G, of K6.2*, K7 or Sun(7); no O-marked case; no M13 or K7
material is used.

## Reading order (manifest order)
1. Candidate and scope (ranges 1-2).
2. Authorities: CAP-DT verdict (whole); SH-DG verdict items 1-5 and boundary; K62-E3 verdict setting/derivation and
   provenance; LFC/INV verdict items 1-6; written RUN-2026-10-16 verdict lines 20-26 (L1, VFC soundness).
3. Imported texts at their scopes: rules-k7-v1 §0-L1 and §2 VFC; INV (K7-LFC-INV §2, erratum E1, E6); DT-A §0-§2 (apex
   table, CI, CI'); DT-B §0-§2 ((R3), (R4), B1-B3); DT-C C1-C2; CAP-DT erratum-v1 CD3 (Lemma RC), CD9, CD13 ((R4) positive
   support); erratum-v2 V4 (RC rule scope), V11 (L1 + INV citation); K62-E3 Lemmas 1-3 and §5 C1/C2 with erratum-v2 Z6
   (Lemma 3 chain), Z10, Z11 (C2 sub-claim (a), C2 proof); K62-DG §3-§4 with SH-DG erratum G3-G6 and Notes.

## Requested checks (hostile)
1. **P3:** gcd(n_e, T_x(S)) = 6 for unmarked e (w_e coprime to T_x(S) by the Lemma 3 chain, for x = alpha via inversion);
   k = 6 mu(Phi_e W_S) <= x_ej with equality iff Phi_e W_S = Phi_ePhi_j; v2 additivity.
2. **P2:** the admissible tau table and "delta >= 4 iff (2,4,4) tau 8 or (4,4,4) tau 8/16".
3. **Lemma EQ, one-tight case:** D'_b = Y by tightness; D'_a inside Y; lambda'_a = w_a, lambda'_b = 2 w_b coprime; (V3) at
   |T| = 2. Both-tight case is exactly CI's hypothesis set.
4. **Case B enumeration:** only one edge, two adjacent, two disjoint, or a triangle of x = 2 edges survive "at most one
   N-edge avoids each N-vertex".
5. **B1/B2 apex arguments (P4):** tau({a,b,c}) >= 8 from Phi_b W_{a,c,q} = X^b_a; the (2,2,4) contradiction 1/6 < 2/6.
6. **P5 orientation:** E3-C2 applied to x' needs x_(d i*) = 1, true in G for both families; edge-disjointness of H_x, H_x'.
7. **P6 from (R4)** in G (RC-O with x'_(d i*) = 1), including h_d >= 1 with z = 5 (CD13 positive-support form).
8. **Scope:** every import holds for f* >= 2 and for the 5-marker on d or i* (none of them uses (RC-i*) or C2 at i*).
9. **Corollary HD** matches Theorem DG's accepted statement (capped depths; orientation; (b) "exactly one ... = 5").

## Mutation controls (thought experiments; nothing run)
Drop B3: a 4-clique with all tau = 16 passes (N_e). Drop P3's equality case: B2 (tau = 8) and B4 lose their
contradictions. Drop E3-C2: B1, B3 and Case A lose the budget contradiction. Put a marker in Q: gcd 6 in P3 and the
coprimality in Lemma EQ fail; the proof is not claimed there.

## Provenance and labels
Direct new Sun instance: Sun(2) (Lemma EQ). Through imports: Sun(2), Sun(3), Sun(4). The LFC/VFC package and the K6.2*
class reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6) (efe1d849…1e29) in the transitive closure.
All new claims CANDIDATE_UNVERIFIED. Written mathematics only; no computation, novelty, priority, Lean or human-review claim.
Parent owns all reviews and the verdict.
