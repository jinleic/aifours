# Checkpoint 006: cadence deviation record and failed directions (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T05:05:02-0700.
- **Companion:** `checkpoint-005-v1.md` sha256 dadd6d63087648804e2624c127495a7fb5ee14e8e7dcb0d940dd5018966bca87 (written 2026-10-19T05:04:43-0700), which states the
  current target, results and next step. This file adds the deviation record and the failed directions.

## Deviation (cadence)
Checkpoint 004 was written at 2026-10-19T03:50:52-0700 and checkpoint 005 at 2026-10-19T05:04:43-0700: a gap of
73 min 51 s, against the <= 30 min rule. Cause: a long uninterrupted hand derivation (row census and triangle tables)
without an intermediate checkpoint. No computation, process or file write happened in the gap, and no claim was
frozen in it. Remedy from now on: a checkpoint at most 30 min after the previous one, even if only partial.

## Current target
K7 with the 2-marker on z and the 3-marker on t != z (the only open K7 family). Sub-family (a1): 5-marker absent,
on z or on t; accepted D23 forces both z-rows 3-type there. Sub-family (a2): 5-marker on a third vertex p.

## Proved/frozen since 03:52
Frozen: only `K7-Z23-P5-erratum-v1.md` (sha256 737e82a3...823d, 03:52) and checkpoint 005. Written but not frozen as
claims: items 1-5 of checkpoint 005 (FG at unmarked u in (a1); quantitative transfer; row facts; triangle facts;
T = W or T* = W; centre count gives sum phi_u < 5 when T = T* = W).

## Failed directions (as of this file)
1. Centre count at z needs D_t disjoint from D_u for u in T*; FG-tightness at u gives this only for rows with a
   W-three or the tight optima that put weight on z. Several FG-surviving rows with no W-three put zero weight on z
   in every optimum or are slack, and some have t isolated (phi_u = 0). So the P-kill does not extend directly.
2. Subset granularity at an unmarked u is implied by full granularity there (gcd | 6 for every subset), so it adds
   nothing at unmarked apexes; it may matter only at marked apexes (parent FYI on K62-E3).
3. LFC at t (marked, 3) has no FG strengthening (its 3-part of the full intersection index is unbounded), so no
   rigidity comes from t directly.

## Next step (bounded)
Finish the written k3 = 0 row census (c in {1,2,3}, e in {1,2,3,4}) with tightness data; combine with the
triangle facts in the two cases (T = W) and (T* = W); test the parent's suggested light-set/granularity trick at the
marked vertex z or t. Next checkpoint by 05:39 PDT at the latest.
