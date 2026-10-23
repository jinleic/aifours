# Reflection round 2 (Slice B), checkpoint 01

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T04:44:24-0700.  Written research only; no
computation, no model CLI.  Status: plan and frozen target; no candidate yet.

## Inputs read and pinned (sha256 re-hashed 2026-10-19 03:5x PDT, all match the controlling records)

- proof-REFL-fewodd-r5.md 4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363 (verdict cites r4 1e447754...861d).
- proof-RED-r2.md c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7.
- proof-K0star-r2.md 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1.
- proof-B0S-r3.md 95851b9c3231ec665341145d779ec9eb11da71c5a5ed772f88cb2222595de1ee.
- proof-MXG-r2.md f2235ed9964e92ca7554678bfae612b7eebb2760eb1b086e487b2e04688aae2f.
- Verdicts: refl-fewodd, K0star-RED, smallk, runs, refl-b0, cj-cjx, edge (six-lane-2026-10-16/review); KPS-SLZ, FB,
  s1sharp (six-lane-2026-10-18-96h/review).

## Frozen target (unrestricted reflection half, o_F > p)

REFL-HI(p): for prime p >= 5, every avoider w of length 4p - 2 over D_(2p) whose rotation letters lie in one set
{rho_x, rho_-x}, x != 0, and with o_F(w) >= p + 1 (odd maximal cyclic CONSTANT reflection blocks), has every maximal
cyclic reflection run constant.  With REFL-few-odd (accepted, o_F <= p) this is REFL(p).
By accepted RED (P1-P4, K0*, (I1)-(I4)) and the accepted small-k verdict, REFL-HI(p) follows from
REFL-RES-HI(p): no avoider in RES_<(p) with kappa >= 2 and k >= p + 1 (both B = 0 and 1 <= B < kappa).

## Route chosen (new; not the lift/c-function route of the previous desk)

Exact sign-pattern reformulation of the H0 windows for all-odd pure-run G-words, followed by sumset (Cauchy-Davenport)
arguments over separated arcs.  First target: the B = 0 regime IIIb (R <= 2 kappa, k >= 2p) via patterns with
m* = kappa + 1 - floor(R/2) intervals, whose windows are mass-independent.  Failed directions are recorded as found.

## Failed/limited directions already checked (written reasoning only)

- Local SPEC moves cannot lower o_F: Spec(sigma_u^a sigma_v^b), a, b odd, u != v, contains no reflection-only
  replacement except slides (SL).  Window-level fusion of two odd blocks raises H (kappa - 1) and enlarges windows.
- Theorem P parameter count for RES_< words: M = 3p - 3 - kappa + e_R/2 <= 3p - 3 = deg Q, equality iff e_R = 2 kappa;
  the boundary case reduces to a full-monomial matching coefficient, not usable without the values.
