# k63-residue falsification aid: frozen plan v1 (GO REQUEST; nothing has been run)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:27:14-0700.
- **Owner:** Sun63Successor. **Item:** mechanical falsification aid for the case tables of the Row Lemma in
  `K63-RES-v1.md` (sha256 1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515) with
  `K63-RES-erratum-v1.md` (sha256 e70a5518a74ee4230d442a1b81d562d65b683ab6fcb904ff306792ea0ac3b49b).
- **Status of the output, whatever it is:** EXPLORATORY, never a premise. It cannot prove anything about groups.
  It can only falsify the written case tables (a row with x_vd = 1 whose exact LFC optimum is <= 5 would show a gap in
  section 3). It does not touch Lemma FG or Corollary 5/6.

## Source (frozen)
- `falsification-aid-rowlemma-v2.py` sha256 0879577c64689e93e4ebe7f211c86d1b6e111a82f1a99f4554c060b8b0b4cfbe (stdlib only).
- `falsification-aid-rowlemma-v1.py` sha256 382960be4970e7117340aa14d331c24403a6b2f4cb1537f2aee559f1c2bb8ac6 is
  WITHDRAWN and will never be run (no caching, uncertified optimum; superseded by v2).

## What it computes
For every row at an unmarked odd C-vertex v with x_vd = 1 (x = alpha or alpha*; the label formula is the same):
O'-entries in 1..5 (ordered, 625), x_* in 1..5, E in {1, 2}, 5-marker in {none, d, i*, u0, u1, u2, u3}:
43,750 rows. Types as in section 3 of the candidate. It maximises val(y) over lambda-feasible y exactly (Fractions,
Bland simplex over the maximal allowed sets) and certifies each optimum (primal feasible y and dual u >= 0 with
u^T A >= a and sum u = optimum, all exact). Main check: every optimum > 5. Controls: all-3 row (x_* = 3, no marker)
must give 17/3; row (4,4,4,4), x_* = 3, x_d = 2, E = 2 must give 5 (a survivor, so the checker is not vacuous);
count of x_d = 2 rows with optimum <= 5 must be > 0; count of x_d = 1 rows with optimum < 6 must be > 0 (the
5/6-bound is load-bearing).

*Universe reduction (why these caps are exact for the gcds):* the other side of every gcd has 2-part <= 4,
3-part <= 3 and 5-part <= 5 (entries <= 5, unmarked), so only min(E + v2(x_*), 2), min(F, 1) and min(h, 1) enter;
hence E in {1, 2}, F = 1 and marker exponent 1 represent all exponents. The w-parts never enter (pairwise coprime,
coprime to 30 and to entries <= 5).

## Launch parameters (to be recorded in an exclusive launch record only after an item GO)
- Command: `/usr/bin/env python3 -B falsification-aid-rowlemma-v2.py <OUT>` with OUT =
  `evidence-fa-v2-r1/result.json` (new directory, exclusive create), cwd = this continuation directory,
  PYTHONDONTWRITEBYTECODE=1.
- Self budget 250 s wall (checked in the loop; status STOPPED_BUDGET if hit). Expected seconds: well under 60.
- Output <= 1 MiB (enforced in the source); retained-byte reservation 2 MiB including stdout/stderr captures.
- RSS expected < 200 MB. No network, no reads of other files, no native code.
- Start gate: fresh disk/RSS check; record PID/PGID, start time, absolute child end = launch + 250 s; settlement by
  observing the direct-child exit; owned SIGTERM only on budget overrun; no SIGKILL; no tool timeout kill.

## Request
Parent item GO (or NO-GO) for exactly this source hash and these parameters. Without GO nothing is run.
