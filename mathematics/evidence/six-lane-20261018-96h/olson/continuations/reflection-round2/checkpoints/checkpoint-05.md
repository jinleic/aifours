# Reflection round 2 (Slice B), checkpoint 05

Written after host clock 2026-10-19T06:15:24-0700.  Written research only; no process owned or launched (parent HOLD
RUN/review/runtime-guard-admission-HOLD-v1.json acknowledged).
Correction to checkpoint-04 (7f668f8a...559b): its "(file created ~06:1x)" label was an estimate and is withdrawn; the host
clock read immediately after its creation was 2026-10-19T06:04:06-0700.

## Review set (parent instruction 06:1x IRC)

Delta review set (parent freezes after Claude's v4 review): proof-REFLHI-arcs-v5.md (4e463746...cff1c) + erratum-1
(512e1d9e...3331) + erratum-2 (b4451461...8820; applies Codex MINOR 1 and 2 on v4).
Separate, NOT in the delta set: proof-REFLHI-arcs-v5-addendum-SEGk-v2.md (b6d52682...70d5); its unsent v1 (789d1ed6...8083)
is superseded.  Known nit for SEG-k v2: the (H2) parenthetical on kappa >= 0 should cite (Pairs) of K0star-r2.

## Coverage after v5 + SEG-k (CANDIDATE), all-odd words, rotations in one pair, any B

Excluded: k >= max(2p + 1, 3 kappa + 3); k >= max(4 kappa + 5, p + floor(R/2) + 1); R = p with kappa >= (p + 1)/4 (p >= 11).
Remaining in RES-HI(p):
(A) kappa < (p + 1)/4: arc-method limit (gain <= g_E < Pi_need).  For B = 0 the accepted CJ''''/REFL-B0 cover only
    kappa <= min((R + 4)/4, (5R - 4p + 10)/6) (or Delta <= 1); for B >= 1 nothing.  This is the bulk (about p^2/16 cells per B).
(B) (p - 5)/2 < kappa < (p + 1)/2, R > p, k <= 2p (about 3p cells).
(C) k >= 2p + 1 with k <= 3 kappa + 2 (thin).
Transfer to initial words: for B_0 = 0 the RED terminal keeps R and has kappa_T in [2, kappa_0]; our exclusions plus CJ''''
leave a kappa-gap between min((R + 4)/4, (5R - 4p + 10)/6) and about (3R/2 - p)/2 for large p, so no new unconditional
REFL-B0 range follows; the results are exclusions inside RES-HI (and direct statements for initial all-odd words).

## Failed directions recorded since checkpoint 04

- Z_(2p) / Kneser with m in [kappa + 1, p - ceil(R/2)] (all windows floor-type for every E+ when kappa is small): the
  m-range has length p - ceil(R/2) - kappa, while the doubled gain 2p - R - 1 needs about p - R/2 units at rate 2; short by
  about kappa.  Base arcs crossing nonempty runs can be two-valued in Z_(2p), so they do not help in the worst case.
- Shadow word (anti runs re-signed): E+(P xor Anti) = R_P exactly, but m and u change; no avoidance transfer found.

## Next

(B) via rate-2 accounting (AB-runs in the base, rate-2 segment units); then a read of B0SPP-r5/CJ-r2/CJx-r4 to judge a B >= 1
analogue for (A).
