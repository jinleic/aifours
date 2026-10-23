# PLAN-v1 (t-search-v2): the (R1) T-structure search at p = 29..43 - aid only, not a proof; frozen before any run

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T13:07:35-07:00.  To be launched ONLY after an explicit
new parent GO.

## 1. Purpose

- Test the predictions of Lemma S1 (g) v2 (proof-ROT-ZX-addendum-S1g-v2.md, cbbbfecc...b31c, unreviewed) at four
  covered (p, kappa).
- Explore whether (ZP) => (S1) can fail beyond it, in the residual range (p + delta*(p))/2 < kappa <= (2p - 2)/3.
- Representation: the (R1) structure of notes-ZX-residual-v3.md (e69a0acc...03c3).  If (S1) fails at kappa with
  3kappa <= 2p - 2, the shortest long zero-sum T is a zero-sum of even length N in [2p + 2, 4kappa] all of whose proper
  zero-sub-sums have length in [N - 2kappa, 2kappa].
- No word or full rotation sequence is enumerated.

## 2. Code

code/t_search_v2.py is t-search-v1/code/t_search_v1.py (0fa86f5c...ed0f) with four textual edits only (diff recorded in
the README):
- the docstring header;
- ITEMS;
- BUDGET_S, from 5400 to 3600;
- the role test, "RESIDUAL" replaced by ("COVERED", "BEYOND").
Everything else is byte-identical: the enumerator, (T0)/(T1), passes, extension check with cap 2e5 (over-cap gives
extends = null, i.e. UNKNOWN, never non-existence), heartbeat and budget.

## 3. Items (in this order) and expected outcomes (EXPECTED-v1.json)

- CONTROL_POS (7, 5): must find g^13 (5g)^3 (detection control).
- CONTROL_NEG (29, 15), (31, 16): kappa = (p + 1)/2, so the accepted S1 (c) forbids any T.  found_total = 0.
- COVERED (29, 18), (31, 19), (37, 22) (delta = 7) and (41, 25) (delta = 9): S1 (g) v2 predicts found_total = 0.
- BEYOND (31, 20), (37, 23), (37, 24), (41, 26), (43, 27), (43, 28) (delta = 9, 9, 11, 11, 11, 13): no prediction.

Interpretation:
- An empty item counts only if its enumeration completed.  ITEM_UNKNOWN means not checked.
- found_total > 0 in a CONTROL_NEG or COVERED item means an error in the enumerator or in the lemma: report immediately.
- A T found in a BEYOND item refutes "(ZP) => (S1)" at that (p, kappa) only if it extends to a (ZP) sequence of
  length R.  The extension check will mostly be over cap and therefore UNKNOWN.  Even then, the T itself shows that this
  representation does not exclude such sequences there.

## 4. Admission and launch (no ulimit, no tool timeout; self-budget 3600 s only)

1. Explicit new parent GO first.
2. Admission: python3 -B code/admission_v1.py R/disk-monitor-v1-20261018T0722-to-1810.jsonl 50000000.
   - The script is saved and hashed.  It checks the monitor lines (complete-line parsing, strictly increasing tz-aware
     timestamps), freshness (0 <= age <= 30 s), and the 300 s stability rule: peak-to-later drop
     <= max(300e6, (free - 13.5e9)/12) over at least 25 samples.  It also checks the floor 12.2e9 + projected, on the
     monitor and on a fresh statvfs.
   - Its JSON output goes to out/admission-run1.json.  Only "verdict": "PASS" admits.  On FAIL: report once, no launch,
     no polling.
3. Launch, in the same command after PASS: ../code/gate_v1.sh 50000000 python3 -B code/t_search_v2.py out/run1.jsonl in
   the background of that shell.  "PID $!" is echoed and recorded; gate_v1.sh execs Python, so this is the search
   process.  Then wait on that PID and echo its exit status.
4. TMPDIR = t-search-v2/tmp and PYTHONDONTWRITEBYTECODE=1.  One process; this slice's cap is 1 busy process and 2 GiB.

## 5. Disclosure

The code was produced by a scripted exact-replacement copy of the v1 script.  Before the freeze, only Python parse
checks of both scripts ran.  No enumeration and no admission check ran.
