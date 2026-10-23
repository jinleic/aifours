# Review package: Theorem KP2-EXCL (no avoider has an admissible normal form with terminal k = p+1, kappa^ = p-2), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T13:04:45-0700. CANDIDATE_UNVERIFIED written word-level proof. Not used as premises:
the pending ROT-PP1 / ROT-PP1-TOP (context only), the pending PP1-EXCL, ROT-SING+, ROT-SING, ONE-SHORT-LS, ASSEMBLY-P, (S1), Lev,
S(p), LS+2, Lemma CT, the index-one theorem, REFL at any o_F. No computation and no model launch. The parent owns reviews and
verdicts.

## 1. Review exactly this candidate
WHOLE proof: proof-KP2-EXCL-v1.md, sha256 8be43069c0a7935db902ba2ae4dda533b661ae0c981517f62f0e2b64e518b002, lines 1-256
(24,992 bytes). Frozen scope, written BEFORE derivation (pre-freeze disclosure: generic plan only): KP2-EXCL-scope-v1.md, sha256
20ea30954e76a18bbc6d4b02f826d35e2d285e1619f306997cf18f40447d9390 (2026-10-19T12:52:47-0700).
Statements (copied from proof Sec. 0):
- THEOREM KP2-EXCL. Let p >= 7 be prime. No avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original index
  order with identity product) has an admissible normal form w^ (SOME normal form produced by the accepted process; ZX overlay 2)
  with terminal k = p+1 and kappa^ = p-2. No hypothesis on o_F(w), on the reflection runs of w, or on nonempty runs is made.
- THEOREM KP2-EXCL' (word form; implies KP2-EXCL by Sec. 2.1). No avoider u of length 4p-2 has a cyclic constant-block
  representation R_1 S_1 ... R_(p+1) S_(p+1) with one block sigma_(y_t)^3, the other p blocks single reflections, runs possibly
  empty, and every empty run separating blocks of different values.
- THEOREM EXCL-PM2 (Sec. 3). KP2-EXCL' under the extra hypothesis that all rotation letters lie in one {rho_c, rho_-c}, c != 0
  (the conclusion of the pending ROT-PP1-TOP, used only as a stated hypothesis). Input: GRX only.
Labels: [NEW]; [RE-DERIVED] = same statement/argument as the pending proof-ROT-PP1-v2.md Secs. 4-5, re-proved here (not new
progress); [EXTENDED] = that argument run without its assumption delta >= 1. Please check that the labels are accurate.

## 2. Governing source manifest and trust
Use ONLY review-excerpts-KP2-EXCL-v1.json, sha256 def71828184913ae743fac75adfbee8b1ebf7d555213958d5e9e54c70b7bbbda (3,568
bytes): JSON list of {path, sha256 of the WHOLE file, start, end}, inclusive LF line ranges, absolute paths; 15 ranges from 14
files, 70,905 selected bytes (whole proof, scope and slot transition included). Package + manifest + selected text < 100 KB.
Inputs, each at its accepted scope: the normal form with its empty-run rule (proof-ROT-few-E-v4.md 28-43, rule at 38; fewodd
addendum 1 line 12; ZX overlays 1-3 at zx-s1c verdict lines 51-53; lowodd v2 item 2 (PM*), M1, M4); GRX ("if" direction) for every
cyclic constant-block representation and every sign pattern (lowodd v2 item 1 and M2; notes-GRX-v1.md 7-20); Lemma RS(b) for an
integer K >= 0 and nonzero terms (CFXT item 4; proof-ROW-v1.md 16-27 with erratum-2 R5 at lines 36-38), resting on the classical
Cauchy-Davenport theorem (proof-ROW-v1.md lines 4-5). No input rests on a computer-assisted step.
Context only (NOT premises; for comparison of the re-derived parts): proof-ROT-PP1-v2.md (pending) with parent errata v1 and v2.

## 3. Argument map with endpoints for hostile review
A. Reduction (2.1): kappa^ = p-2 gives H^ = 1, so exactly one block of length 3; F = p+3, R = 3p-5; w^ is an avoider (NF).
B. Selection rule (2.2), recomputed: delta = p+1-Phi (all blocks odd), C_max = Phi+2, C in {Phi, Phi+2}; the long block supplies
   c_t = 3 (f_t = 1) or 2 (f_t = 0) letters for C = Phi+2; n = 2p-C in {2p-2m, 2p-2m-2}; T(z_P) = sum over P of tau_i.
C. Sec. 3 [NEW]: Lemma W2 (n = 2p-2m-2, or p-1 when m = (p+1)/2; four-case count U-L+1 >= p when both signed counts >= p-1);
   all-plus gives (A,B) in {(2p-3,p-2),(2p-2,p-3),(2p-1,p-4)}; case 1: >= 2 empty runs, tau_i = -2c, pure-c selection of
   2p-4 letters; case 2: empty runs impossible (every nonzero residue attained), then two single-letter rho_c runs give
   E_- = p-1; case 3: the set Q, partial sums in {3,4}, two empty runs with tau_i = 2c, selection (rho_-c)^(p-4) rho_c^p.
D. Sec. 4.1-4.3 [RE-DERIVED]: Lemma M (capped total, i <-> i+q pairing), Lemma P (p-1 swap pairs, filler F', RS(b) on p-1
   nonzero differences), Lemma U (unique class, pigeonhole for a != 0 with n = 2p-4).
E. Sec. 4.4: window (W) with lambda = A-2p+3 <= 2, Lambda - lambda = p-1+delta; heavy run (first passage); Step 4 [EXTENDED]
   light sets for every delta >= 0 via A' <= p-2; Step 5 [NEW] lambda >= 0 without CT; Step 6 two empty runs; Step 7 the
   three-case analysis of M = Z_p minus Sigma(B) (b = p-2, p-3, p-4), including adjacent / non-adjacent pairs and x = 1, -1/2.
Endpoints to check: delta = 0 in every step of 4.4; a = 0 (Lemma U); empty runs and tau_i != 0; the uniqueness thresholds
2p-2 > 2p-3, 2p > 2p-2, 2p+2 > 2p-1, 2(2p-3) > 3p-5; admissibility of every n used (C = Phi or Phi+2, the long block
contributing 2 or 3 letters); filler availability n-|J| <= A; p = 7 bounds (4 not in {1,2,3}, 4 != 1, 3 mod p).

## 4. Requested verdict boundary
Judge validity of Theorem KP2-EXCL (and separately Theorem EXCL-PM2 as a conditional statement) for prime p >= 7 relative to the
accepted inputs at their original scopes. Report any use of an input outside its scope separately from any gap, and say whether
the [NEW]/[RE-DERIVED]/[EXTENDED] labels are accurate. Not requested and not claimed: reflection rigidity, INV*, any o_F
statement or assembly, other (k, kappa^) (in particular 1 <= kappa^ <= p-3 at k = p+1), ordered Olson for D_(2p) or all groups,
existence or non-existence of avoiders outside this cell, p = 5, Lev, S(p), REFL, novelty or priority, Lean or human review.
Suggested split: Secs. 2-3 need only NF and GRX; Sec. 4 also needs RS(b).
