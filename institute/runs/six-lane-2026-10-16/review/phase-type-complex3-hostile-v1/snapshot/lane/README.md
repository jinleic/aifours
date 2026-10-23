# Commault–Mocanu 2003 Conjecture 1: minimal PH order, one real pole + one complex pair (math-1 successor)

Lane owner: worker `MathPhaseType3`. Lane directory created 2026-10-18 00:31 PDT (host clock) with a plain
`mkdir` (refuses an existing path). Everything outside this directory is read-only for this lane.
This README was written **before any experiment** in this lane (only source reading and three page renders of the
pinned paper into `sources/`). **No novelty, priority or "first" claim; correctness, novelty and significance are
kept separate.**

Frozen inputs (sha256 recomputed by this worker 2026-10-18 00:37 PDT):

| Input | Path (under `institute/runs/six-lane-2026-10-16/`) | sha256 |
|---|---|---|
| Frozen contract | `screening/math-1-phase-type-complex3-contract.json` | `1bb5bc6e72605a89cab72e106f881184ed99dfb8c10477b1e39eca207c7bcd13` (matches parent pin) |
| Pre-freeze screen | `screening/math-1-phase-type-complex3-screen-v1.md` | `959a2d79fc5602f87a125defcf1e1db50b498a5b431d3276438acc536e40ab22` (matches contract) |
| Untrusted candidate | `review/phase-type-complex3-candidate-v1.md` | `63ea3f3a9ff960a0918d161999657215efee8b332ebdb96f2620e60e2865ab0a` |
| Primary paper | `screening/phase-type-complex3-intake-v1/commault-mocanu-2003.pdf` | `8db1e4aa330a9d9989cb91498524d9cb0c41a95aa636906ed6e42391d5d70cfb` (matches contract) |
| Book page images | `screening/phase-type-complex3-intake-v1/images/book-560.png`, `book-561.png` | `bbff7a9a…01b4`, `b9a3ce32…a782` |
| Paper page image | `screening/phase-type-complex3-intake-v1/images/cm-13.png` | `bb971804…b360` |

Worker reading (images viewed directly): book p.544 (PDF560) states the general minimal-representation question
("对一般 PH-分布 (α,T), 如何找其最小表示是几十年来人们关注的一个公开问题"); p.545 (PDF561) holds only the references and
authors (何启明, 张汉勤). Paper p.577 (PDF13): Theorem 14 (Commault–Chemla 1996), Eq. (42)
q(s)=(1+s/c)(1+s/(a+ib))(1+s/(a−ib)), condition (43) b ≤ (a−c)/√3, Conjecture 1 and the Mocanu (1999) n_min+1
remark. Paper p.570 (PDF6, rendered `sources/cm-p6-06.png`): Theorem 4 (diagonal rescaling of a positive
irreducible realization to a PH representation) and Proposition 1. Paper p.574 (PDF10, `sources/cm-p10-10.png`):
Theorem 6 (Dmitriev–Dynkin 1945, O'Cinneide 1991): for a PH generator T of order n with eigenvalue −λ₁ of maximal
real part and any complex pair −λ₂ ± iθ, θ/(λ₂−λ₁) ≤ cot(π/n).

## 1. Exact question (contract `exact_statement`; not the book's general question)

For all real a > c > 0, b > 0, let F(s) = c(a²+b²)/[(s+c)((s+a)²+b²)]. A PH representation of order n is
(α, T): α ≥ 0 row vector with α1 = 1; T real n×n Metzler, T1 ≤ 0, Hurwitz; F(s) = α(sI−T)⁻¹(−T1).
Claim to settle: the minimum order equals n* = min{n ≥ 3 : b ≤ (a−c)cot(π/n)} (upper band endpoints included,
lower endpoints use the smaller n). Negative alternative: explicit (a,b,c) with a proof that **no** PH
representation of order n* exists, over all topologies.

## 2. Baseline and headroom

* n* = 3: Theorem 14 (Commault–Chemla 1996) — order 3 iff b ≤ (a−c)/√3 (cited; proof not read).
* Order n*+1: reported from Mocanu (1999) thesis (unread).
* Lower bound n ≥ n*: Theorem 6 plus an explicit trimming/dominant-pole argument (contract `lower_bound`).
* Headroom: the all-n sharp order n*. n = 4 alone or finite (n, β) numerics are PARTIAL, never the gate.

## 3. Specification of the deliverable

1. `proof/` — written all-n theorem: (i) lower bound with explicit handling of unreachable/unobservable states,
   cancellations and identification of the dominant eigenvalue (no assumption that unobserved eigenvalues are
   poles); (ii) construction for every n ≥ 3 and every β = b/(a−c) in the band of n, with exact derivations of:
   angle existence (IVT signs, endpoint cases), divisibility, the resolvent/cofactor formula and its orientation,
   positivity of every exit (all Taylor/jet coefficients for every n), Perron stability, diagonal PH normalization,
   and rescaling back to the original (a, b, c). Or a precise obstruction / counterexample if the candidate fails.
2. `code/` + `runs/` + `receipts/` — finite smokes only: exact symbolic identities (sympy), ball-arithmetic
   (python-flint arb) and high-precision (mpmath) checks, designed mutations. Script sha256 recorded in a receipt
   **before** each execution; outputs hashed after; params, seeds, precision, wall time, max RSS recorded.
   No in-place code edits: fixes are new versioned files; failed attempts stay.

The untrusted candidate (`review/phase-type-complex3-candidate-v1.md`) is a hypothesis to be re-derived, not an
input to trust. The cycle topology is a search/proof representation, not a target restriction.

## 4. Stop rules

* Stop the target at once if the parent relays a prior full resolution (Ph3Priority screen goes to parent).
* Hard stop 2026-10-18 18:20 PDT (contract stop-by; deadline 18:31:43 PDT).
* Any exact/symbolic failure of a proof step (wrong sign, failed divisibility, negative exit at some n in a band)
  is preserved as a versioned obstruction file; no fake fallback; a repair is a new version.
* Numerical, interval or finite-table outcomes never establish an all-n or all-real claim.
* Resource gate failure (free disk < 12.2e9 B + projected growth, safety floor 12e9 B): report once and wait; no
  resource polling.

## 5. Native caps and environment

* This lane (primary PH): ≤ 2 busy processes, ≤ 2 GiB aggregate RSS; expected ≪ 1 GiB, ≪ 10 MB new data.
* Every native run: `TMPDIR=<lane>/tmp/`, `ulimit -t` CPU cap (native limit), `/usr/bin/time -l` for max RSS,
  launched via bash async; no SIGKILL / Popen.kill / subprocess timeouts; a hit limit is UNKNOWN, not a result.
* Interpreter: existing venv `information-science/evidence/six-lane-20261016/robust-spr/code/venv/bin/python`
  (Python 3.14.3; python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0), used read-only with `-B` and
  `PYTHONDONTWRITEBYTECODE=1`. No installs, no model CLIs, no Git, no network.
* Scripts import a lane-local guard (no deletion/rename/system temp; exclusive-create writes only).

## 6. Controls (planned before any run)

* Known n = 3 regime (b ≤ (a−c)/√3) reproduced by the same construction; uniform-cycle spectral equality at
  β = cot(π/n).
* Exact polynomial/transfer identities (symbolic n = 4 family; generic symbolic cycle cofactor formula for small n;
  Taylor generating-function and Chebyshev partial-sum identities).
* n = 3..12 (interval/high precision): band interior, exact upper endpoint, near the lower endpoint; transform
  identity at test points, all exits ≥ 0, row sums ≤ 0, α stochastic, Hurwitz, original-time rescaling.
* Mutations that must FAIL: perturbed exit → transform mismatch; wrong node ordering / wrong rate orientation /
  wrong repeated angle → negative exit or spectrum mismatch; order n*−1 must violate the sector bound (checked
  against Theorem 6 arithmetic, not an optimizer failure).

## 7. Log (append-only)

| PDT | Event | Result |
|---|---|---|
| 10-18 00:31 | Lane created; paper pages 6, 7, 10 rendered with lane TMPDIR | `sources/cm-p{6,7,10}-*.png` |
| 10-18 00:37 | Input hashes recomputed; README frozen before experiments | this file |
| 10-18 00:38 | Launch gate FAILED once (free 12,055,920,640 B < 12.2e9); reported to parent; no launches | parent released gate 00:44 (17.75e9 observed) |
| 10-18 00:40–00:44 | Written proof v1 `proof/ph3-theorem-v1.md` (before any run) | re-derivation of candidate + lower-bound reductions; kept unchanged |
| 10-18 00:46 | p00 flint API probe | API as expected |
| 10-18 00:48 | e01 exact sympy identities | 32/33 PASS; E4 FAIL = simplifier miss (e02 00:53: holds by 3 methods) |
| 10-18 00:52 | b01 ball 320 bits, 98 instances | 88 OK; 10 large-n flagged only by absolute radius threshold; all 294 PH checks pass |
| 10-18 00:54 | b02 ball 640 bits, relative radius, n ≤ 64 | 112/112 OK, 336/336 PH checks |
| 10-18 00:54 | m01 mutations | core rejected 71/87: exit-scaling mutation ineffective (normalization invariance), orientation flip degenerate at n=4,f=1; reorderings 0/24 rejected (valid alternatives) |
| 10-18 00:56 | f01 mpmath 60 digits | ABORTED: lu_solve "numerically singular" (diag f01d: k=60, n*=35, ρ^(n−3)=5.8e56 pivot-threshold scaling; v2 header's "1e70" was an estimate) |
| 10-18 00:58 | Parent: priority screen NONE-FOUND-IN-SCOPE (access holes); quote Prop.1, explicit reductions, n*=3 import separate; BuTools not evidence | proof v2 written accordingly |
| 10-18 00:59 | m02 mutations v2 | normalization mutation 15/15, start-state 90/90, orientation 10/10 rejected; all 390 arrangements n=5..7 valid |
| 10-18 01:00 | s01 sector/trimming smoke; f02 mpmath 150 digits | 0 sector violations in 47,070 eigenvalues; 187/187 independent-route cases OK |
| 10-18 01:03 | **Candidate pinned**: `receipts/pin-candidate-v1.json` (sha `f125d47c…de19`), primary proof `proof/ph3-theorem-v2.md` (sha `0fa0876d…37e7`) | parent gate pending; correctness only, no novelty claim |
| 10-18 01:03 | d01 dense ball sweep (post-pin falsification) | 1,605 instances n = 3..40 (42 positions) + n = 64, 100, 128 @2048 bits; 3,210 PH checks; 0 failures |
| 10-18 01:06 | Self-review of v2 → `proof/ph3-theorem-v3.md` (sha `26071159…2ef5`): typo −a ± ib, two one-line justifications, n* = 3 two-basis wording, run list | re-pin `receipts/pin-candidate-v2.json` (sha `15144191…79cb`); pin v1 unchanged |
