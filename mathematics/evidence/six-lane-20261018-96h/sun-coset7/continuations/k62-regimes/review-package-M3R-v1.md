# review-package-M3R-v1: M3(1,1) residual — R1 forces R2; R2 necessary conditions; obstruction note [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:39:24-0700. Author SunK62Regimes.
- **Candidate:** `K62-M3R-v2.md`, sha256 af2b965bf69b252e266064aff5b201b16757bcb76af152d7eee8c89ee77888b3 (190 lines); it
  supersedes the undelivered draft `K62-M3R-v1.md` (986bb1e3…; W-name clash and one false mutation remark only). Scope frozen
  before the derivation: `K62-M3R-SCOPE-v1.md`, sha256 421b0466fe17be97196493f695b99cd9fb75270d3b6f8a1cbdfd257aa146939a.
- **Excerpt manifest:** `review-excerpts-M3R-v1.json`, sha256 4c73f72e4a201ff8b1369d6afeddd9db16f8d2ae4cd0be473cc026e11c377843:
  20 inclusive ranges {path, whole-file sha256, start, end}; embedded text 66,261 bytes; JSON 4,845 bytes. It includes the
  R1/R2 definitions and the Theorem M3R statement of K62-MK-v2 and the parent MK erratum, only as the conditional premise of
  Corollary 6.2. Hashes and ranges checked against current bytes (packaging metadata only, no scientific computation).
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes/`.

## Outcome against the frozen scope
Theorems R1X and R2X were **not** achieved. The file is the scope's fallback: an obstruction note (section 7, items (a)-(d))
with these unconditional results (M3(1,1): 3-marker on t in O, orientation (1,1), any admissible 5-marker; exponents unbounded):
- **Lemma C:** Gamma_z(t) = gcd(n_t, T_z(V minus {t})) = 2 * 3^(min(f_t, v3 T)); 9 | T_z(V minus {t}) iff tau_z({d, i*, e}) = 3 for
  some e in O'; then Phi_e(Phi_d cap Phi_(i*)) = Phi_ePhi_d and z_(e i*) >= 3.
- **Theorem RR:** every R1-instance (x; a, b) forces x'_tu = 2 (all u in O') and x'_(t i*) = 2, so x' is an R2-instance; the
  residual of K62-MK-v2 reduces to R2 alone.
- **Proposition W6:** for an R1-instance, W = <Phi_a, Phi_b> has index 6 (index 3 dies by Sun(3) inside W), x_ab = 1,
  Phi_aPhi_b = W, and the a-, b-cosets lie in the two W-cosets outside X^t_a, which the d-coset avoids.
- **Proposition R2N:** an R2-instance y has y_(t i*) = 2; at most n_t / 12 empty fibres at t; at least n_t / 6 + 2E fibres carrying
  {u, i*, d}; 9 | T_y'(V minus {t}), hence some e in O' with tau_y'({d, i*, e}) = 3.
- **Corollary 6.1** (unconditional sub-case) and **6.2** (CONDITIONAL ON K62-MK-v2 Theorem M3R).
- **Smallest missing lemma (L-R2):** no row at t (either family) has all four O-entries in {1, 2}.

## Requested checks (hostile)
1. Lemma C: gcd 6 at each chain step after d, i* (5-part and w-part), k_e <= 3, the equality forced by k_e = 3, the apex identity
   with gamma_e = 6; the converse via T({d, i*, e}).
2. Lemma A (T rule on {d, i*, t}) and its use in RR step 2 (a 5-marked a cannot share 5 with lambda'_(i*)).
3. RR steps 3-5: the light set L meets no D_j; R has measure < 4/6; the x'_tc = 1 case via Sun(2); the odd x'_(t i*) case via
   Sun(3) and the measure sum (7 + x') / 6.
4. W6: Phi_tW = X^t_a; 3 | m from [Phi_t : Phi_t cap W] = 2m/3; t_d multiple of 3; Sun(3) inside W at m = 3; Phi_aPhi_b = W and
   disjointness argument at m = 6.
5. R2N (i) certificates c1, c2 (feasibility on positive support); (ii) the identity f_3 - f_1 = n_t / 6 + 2E and f_3 <= n_t / 3;
   (iii) the light-fibre argument with the y'-subgroups and Lagrange.
6. That nothing pending is used outside Corollary 6.2, and that M13 is not touched.

## Provenance and labels
Direct Sun instances: Sun(2), Sun(3) (inside Phi_t and inside W); through imports Sun(4) (K62-E3). The LFC/VFC package and the
K6.2* class reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6) (efe1d849…1e29) in the transitive closure.
FH is not used. All new claims CANDIDATE_UNVERIFIED; written mathematics only; no computation, novelty, priority, Lean or
human-review claim. The parent owns all reviews and the verdict.
