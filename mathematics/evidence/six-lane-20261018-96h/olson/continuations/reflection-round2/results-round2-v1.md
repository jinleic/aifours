# Slice B (unrestricted reflection half, o_F > p): results package v1

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:29:59-0700.  Written research only: no computation,
no model CLI, no process launched.  Every result below is CANDIDATE_UNVERIFIED until the parent's verdicts; nothing here is a
claim of full REFL(p), INV*(p), ordered Olson, novelty, Lean or human review.

## 1. Frozen target

REFL-HI(p): every avoider of length 4p - 2 over D_(2p) with rotation letters in one pair {rho_x, rho_-x}, x != 0, and
o_F >= p + 1 (odd maximal cyclic CONSTANT blocks) has every maximal cyclic reflection run constant.  With the accepted
REFL-few-odd (o_F <= p) it is REFL(p).  Via the accepted RED + small-k verdicts it follows from RES-HI(p): RES_<(p) has no
avoider with kappa >= 2 and k >= p + 1.  STATUS: OPEN.

## 2. Texts (review set and separate addenda)

Delta review set (parent): proof-REFLHI-arcs-v5.md 4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c
+ erratum-1 512e1d9e9a5dcdd4ad85840ce74d6d29ab8e1b8eb72db944ddff4a5683393331
+ erratum-2 b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820 (Codex MINORs on v4)
+ erratum-3 380106c91b0bcf250a8fd98583e75b39faf3d4c7d3ecd0eba2b2472bc15e669a.
Separate addenda (not in the delta set): proof-REFLHI-arcs-v5-addendum-SEGk-v2.md
b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5; proof-REFLHI-transfer-v2.md
dc1974c8e8c8229002dd02e6bb4ef1e97cd123f7d411479bcd7d8cc9b58729fa.
History (kept unchanged): v3 2889509a...512f8f (+ erratum-1 1fba1b33...5ee3), v4 7683eb17...7f0e, K2P+ 7f5b3dc5...383f,
SEG-v2 bfa29fd5...cedce1 (+ erratum-1 53d90ba7...2868); unsent drafts tools-v1 79741c7c...7a6e, arcs-v2 667e4373...f4ed,
SEG-v1 e43f39ac...98b1, SEGk-v1 789d1ed6...8083, transfer-v1 874a3911...6e28.

## 3. Results (exact statements in the texts)

New tools: Lemma ARC (Cauchy-Davenport over a product family of patterns sharing one H0 window: arcs = runs of blocks joined by
empty runs), Lemma ARC+ (optional single-block arcs inside reflection runs keep E+ and the window), Lemma SEG (gain
>= min(2t, b' - 1) for a segment of b' blocks with at most t inserted pairs), Lemma BAL (one parity toggle pair balances the
labelling to |T| <= d), Lemma 3.2 (balanced kill).
Exclusions, for all-odd words of length 4p - 2 with rotations in one pair, ANY B (so both B = 0 and the previously untouched
1 <= B < kappa part of RES_<(p)):
* K2P+: k >= max(2p + 1, 3 kappa + 3).  (Its proof gives the word-level form: k >= 2p + 1 and max_j |a_j - b_j| <= 2H - 3.)
* SEG-k: k >= max(4 kappa + 5, p + floor(R/2) + 1); SEG-num: R = p + delta, (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2.
* R = p: kappa >= (p + 1)/4 for p >= 11 (SEG-p, MID, K2P+, TOP); p = 7 except kappa = 3; p = 5 only kappa = 4 (erratum-3).
* Corollary IIIb-X: the extreme IIIb family (B = 0, R = p, kappa = (p + 1)/2, k = 2p + 1) has no avoider for p >= 7.
* FP-1 (R = p, diversity hypothesis), Theorem ETA (B = 0, R <= 2 kappa + 1: structure, not exclusion).
Transfer to initial words (transfer-v2): along RED, D = A - B is constant and B, kappa, g = kappa - B never increase, so the
terminal lies in the box k = 2p - D_0 + 2g, R = D_0 + 2b, 1 <= g <= g_0, 0 <= b <= B_0.  REFL holds for w0 when every box cell is
excluded.  Explicit: |A - B| <= 1 and o_F >= 3 kappa + 3 (T1); o_F >= 4 kappa + 5 and A + floor((A - B)/2) <= p + 1 (T2).

## 4. What remains (precise)

Inside RES-HI(p), outside the exclusions above (and, for B = 0, outside the accepted CJ''''/EDGE/REFL-B0 coverage):
(A) kappa < (p + 1)/4 (about p^2/16 cells per prime; for B >= 1 entirely open).  Arc methods cannot reach it: every unit of
    Cauchy-Davenport gain at a fixed window needs an empty run or even run (at most 2 kappa by (P0)), while the need is
    p - ceil(R/2); the Z_(2p)/Kneser variant misses by at least one in the worst case (checkpoint-06).  Lift arguments (the
    B = 0 CJ machinery; for B >= 1 an analogue of MXG beyond k <= p) appear necessary.
(B) kappa in {(p - 3)/2, (p - 1)/2} with R > p and k <= 2p (about 2p cells).
(C) k >= 2p + 1 with k <= 3 kappa + 2 (about p^2/6 cells, kappa >= (2p - 1)/3).  There an avoider must contain a run with
    |a - b| >= 2H - 2 (word-level K2P+); the corner H <= 1 sits exactly at the Theorem P boundary (e_R = 2 kappa).
Structural facts proved for any avoider (usable by later work): Fact 2.2 (R >= p, run sizes <= 2(R - p) + 1), Theorem FP/ETA
restrictions, and the SEG disjunction (g_E <= Pi_need, or H - floor(d/2) <= Pi_need, or n_CA <= 2 m_lo + 1).

## 5. Failed directions (preserved)

Local SPEC moves cannot lower o_F; fusing odd blocks raises H and enlarges windows; Theorem P's Chevalley-Warning count is
M = 3p - 3 - kappa + e_R/2 <= deg Q (boundary e_R = 2 kappa); generalised Davenport items need k - kappa zero-mass brackets;
balanced intervals fail with giant runs; the shadow word (re-signed anti runs) gives E+(P xor Anti) = R_P but no transfer; the
Z_(2p)/Kneser arc method misses by one (count in checkpoint-06); rate-2 refinements of SEG (AB-runs in the base) give only
messy constants and were not written as theorems.

## 6. Dependencies (all at accepted scopes)

H0, (P0), (Pairs), FUS/PM0/TR bookkeeping: proof-K0star-r2.md 6681676e...96e1; Theorem RED and proof: proof-RED-r2.md
c4e7697f...d3d7; (SMALLK) verdict b71fcaf4...13b8; REFL-few-odd r5 4615dcb9...5363 (verdict binds r4 1e447754...861d); Lemma AR as
cited in K0star-r2; CJ''''/EDGE verdicts (transfer clause (f) only); Cauchy-Davenport (classical).  No rotation rigidity,
INV*, SLZ3, RED-r3, K0star-r3 or finite computation.
