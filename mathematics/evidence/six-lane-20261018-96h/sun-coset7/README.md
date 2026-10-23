# math-1 sun-coset7, 96-hour continuation: Sun 2006 Conjecture 1.2 at k = 7, every group

- **Created:** `/bin/date` 2026-10-18T23:20:19-0700. This README is written once; later changes go into numbered addenda.
- **Run contract:** `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/contract-v1.json`
  (sha256 55baff0c...cffaa). Deadline 2026-10-22T22:56:33-07:00; native launches stop 2026-10-22T20:56:33-07:00.
- **Old lane (read-only):** `mathematics/evidence/six-lane-20261016/sun-coset7`, final summary LANE-SUMMARY-v3.md
  (02796f8a...f578f1? see pin: 02796f8a9567c8df24459d4aec1147b90c56fce75bf44716aea9250c4888f907).
- **Owner:** worker ContinueSun7. Parent owns run metadata, reviews, and every class disposition (K5.3 in particular).

## Target (unchanged, no quantifier reduction)

G arbitrary; seven finite-index subgroups (possibly equal); seven pairwise disjoint LEFT cosets; no cover assumption;
conclusion gcd([G:U_i],[G:U_j]) >= 7 for some i < j. Sharp at seven cosets of an index-7 subgroup.

## Inherited frontier

See `evidence/inherited-stop-registry-v1.md`. Open: K7, K6.2*, K6.3; K5.3 pending parent's NEW disposition after the
parent-run StageA v2 qualification. Excluded (accepted, computer-assisted, F-1 permanent): K5.2* (with D2') and KII.

## Frozen initial scientific plan (v1)

1. **New written route [started].** Lemma LFC (L5 with H = U_v: left-fibre count with alpha in place of q) and Lemma INV
   (q = alpha* of the inverted configuration; alpha + alpha* <= g). Candidate consequences in `K7-LFC-INV-v1.md`:
   K7 with M empty excluded (parity of a 3-regular graph on 7 vertices); fully unmarked K6.3 excluded.
2. **Marked cases next:** K7 with 1 <= |M| <= 3, K6.3 with markers, K6.2* (inherently marked). Method: per-vertex LFC and
   INV-LFC (= VFC) row analysis with marker-modified labels lambda = r alpha, joint (alpha, alpha*) constraints, then
   global counting. Exploration may use frozen standard-library probes of <= 300 s and <= 16 MiB output, each with a
   fresh resource check, frozen source hash, recorded command and output. Probes are exploratory and never premises.
3. **Proof standard.** Prefer hand-checkable written certificates (explicit feasible y per killed row type). If a
   finite case analysis becomes load-bearing computation: frozen certificate format first, two independently written
   exact checkers, parent item-specific GO, parent replay; F-4 discipline.
4. **K5.3:** parent-owned. A separate written LFC route for X1 may be attempted later only as an independent
   candidate; it never promotes K5.3 automatically.
5. **No** Stage C engine restart, no old driver restart, no StageA duplication (parent ran it), no native solver.

## Files

| file | role |
|---|---|
| `evidence/inherited-stop-registry-v1.md` | inherited stops, holds, NOT_STARTED items, class ledger |
| `K7-LFC-INV-v1.md` | candidate lemmas LFC, INV, ROW-U; candidate theorems K7-M0, K63-U0 |
| `checkpoints/` | substantive checkpoints (<= 30 min apart while active) |
