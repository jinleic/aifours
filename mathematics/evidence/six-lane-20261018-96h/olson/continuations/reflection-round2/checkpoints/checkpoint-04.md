# Reflection round 2 (Slice B), checkpoint 04

Written after host clock 2026-10-19T06:00:29-0700 (file created ~06:1x).  Written research only.  Parent runtime-guard HOLD
(RUN/review/runtime-guard-admission-HOLD-v1.json 6c1d8440...) acknowledged: this slice owns no process and launched none.

## Sent candidates since checkpoint 03

| file | sha256 |
|---|---|
| proof-REFLHI-arcs-v4-addendum-SEG-v2.md | bfa29fd5352343fc26f79e57f6cc8fe4fb462c23f11f3818d4ae7a1153cedce1 |
| proof-REFLHI-arcs-v4-addendum-SEG-v2-erratum-1.md | 53d90ba77bf8333a358ec4511f78e80e7d76b0ae0421fd7e1e86d230c7d92868 |
Unsent and superseded: proof-REFLHI-arcs-v4-addendum-SEG-v1.md (e43f39ac971802b27d8eecdf9376664cd890f45c44a8a982e7c3bb5fd34998b1).

## State (all CANDIDATE_UNVERIFIED)

Excluded for all-odd words with rotations in one pair, any B: k >= max(2p + 1, 3 kappa + 3) (K2P+); R = p with
(p + 1)/4 <= kappa <= (p - 3)/2 (SEG-p) or (p + 1)/2 <= kappa <= p - 3 (K2P+); R = p + delta with
(p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2 (SEG-num).  REFL-HI / RES-HI remain OPEN.

## New exact observation (not yet written as a lemma), and a failed direction

At R = p, B = 0, in the floor regime of both windows, put psi(P) := (E+(P) mod 2, u_P - D_P/2) in Z_2 x Z_p = Z_(2p); psi is
additive over runs, and P kills iff psi(P) lies in K = {0} x [-(p-1)/2, 0] u {1} x [0, (p-1)/2], |K| = p + 1.  Every
Z_2- or Z_p-periodic set meets K, so Kneser's theorem kills as soon as a product family of patterns has sum of (|A_i| - 1)
>= p - 1, and now block boundaries across NONEMPTY runs also give gain.  Failed as a route below the arc limit: keeping every
configuration in the floor regime forces about 4 kappa - 2 rotation letters outside all varying parts, and the doubled
requirement p - 1 then exceeds the available boundaries unless kappa <= 1.  Recorded; not pursued further.

## Next

Consolidated self-contained candidate v5 (ARC, ARC+, SEG, BAL, FP/FP-1, K2P+, SEG-p, SEG-num, ETA, IIIb-X, remaining map)
to reduce reviewer load; then the R = p cells kappa = (p - 1)/2 and the large-delta band.
