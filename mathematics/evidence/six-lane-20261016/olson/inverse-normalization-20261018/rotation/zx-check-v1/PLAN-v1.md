# PLAN-v1: finite control for Lemma ZX and Lemma S1 (aid only, not a proof), frozen before any run

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T11:47:04-07:00.
- Subject: proof-ROT-ZX-v1.md (ad2460b2...815b).
- Expected outcomes: EXPECTED-v1.json.
- Code: code/zx_check_v1.py.
- The hashes of all three are sent to the parent before launch.
- No words over D_(2p) are enumerated; this is a statement about sequences in Z_(2p).

## 1. What is checked

For each item (p, k, kappa), with R = 2p + 2kappa - k, the script considers every multiset Y of R odd residues mod 2p
satisfying (ZP): no zero-sum of size in [2kappa + 2, 2p].  Multisets are taken up to multiplication by units.
Enumerator:
- It is the enumerator of zs-check-v1/code/zs_check_v1.py (d9d0e073...6818).
- It is copied with exactly two additions: a heartbeat line every 300 s, and a self-imposed global budget of 9000 s.
  After the budget, the current item and all later items are written as ITEM_UNKNOWN.

Per multiset:
- ZP2: (ZP) re-checked from the full (size, sum) state set.
- CONC: the minimum over odd generators of cost is <= k - 1.
- S1: the longest zero-sum has length <= 2kappa.  If it does not:
  - record the multiset;
  - check that 2kappa >= p + 1;
  - search for the P, P' pair of Lemma S1 (b), if the sub-multiset count is <= 2e6.
- ZX: if S1 holds, Steps A-G of Lemma ZX, with Z a longest zero-sum and g the most frequent value of Y - Z.
  - A: Y - Z is zero-sum-free; 0 <= e = k - 1 - 2kappa + |Z| <= k - 1; g is the unique mode and a generator; MULT
    form, with weights 1 or odd d in [3, min(m, k)]; e' <= e; m >= max(2, e + 1); (A1); completeness; W' <= 2p - 1.
  - C: positive terms of Z equal g.
  - D: beta <= e - e'.
  - E: sigma = r.
  - F: W' <= 2p - 1 - r.
  - G: cost_g <= e <= k - 1, and all |b| <= k.

## 2. Scope (78 items, in this order)

- All kappa in [0, k - 1] for these (p, k): (5,1), (5,2), (5,3), (7,2), (7,3), (7,4), (7,5), (11,6), (11,7), (13,7),
  (13,8) and (13,9).  That is 57 items; these are the items of zs-check-v1 run1 with p <= 13.
- p = 17, k in {10, 11}, all kappa in [0, k - 1]: 21 items, sorted by R from 23 to 43.
- Residual items (2kappa >= p + 1): (7,5,4), (11,7,6), (13,8,7), (13,9,7), (13,9,8), (17,11,9), (17,10,9),
  (17,11,10).
- The new ZX pairs are included: (7,5,3), (11,7,5), (13,8,6), (13,9,5), (13,9,6), (17,10,8), (17,11,7), (17,11,8).

## 3. Controls

- UNIT_TESTS, which are fixed sequences:
  - the longest zero-sum of g^(2p) is 2p;
  - the longest zero-sum of g^p (-g)^p (pg)^2 is 2p + 2;
  - the type II sequence at (7,4,3) passes Steps A-G with cost = e = k - 1;
  - mutation M1 (cost <= e - 1) fails on it;
  - a planted defect, Z empty instead of a longest zero-sum, is flagged A_zsf.
- In every completed item with kappa = k - 1: type II is found, passes, and M1 fires.
- The found counts of the 57 items with p <= 13 must equal run1 (zs-check-v1/out/run1.jsonl, bb8ddafb...9b1a); all 57
  were mechanically checked against the dict in the code before the freeze.  This uses the same enumerator, so it is
  not an independent check.

## 4. Expected outcomes and interpretation

See EXPECTED-v1.json.
- Predictions with a source: in the ZX items, s1_fail = 0, zx_fail = {} and conc_fail = 0; in the residual items,
  zx_fail = {} on every multiset where S1 holds.
- No prediction: s1_fail and conc_fail in the residual items, and the p = 17 found counts.
- An ITEM_UNKNOWN is not checked.  Only the final DONE line marks a complete run; DONE_PARTIAL marks a budget stop.

## 5. Run protocol

- One process.  The lane cap is respected: this slice has at most 1 busy process and 2 GiB.
- Disk: a fresh statvfs gate via ../code/gate_v1.sh with 100000000 projected bytes.  Before launch I also check that
  the latest sample of the parent disk monitor (R/disk-monitor-v1-20261018T0722-to-1810.jsonl) is recent.
- CPU: ulimit -t 9300 as a native backstop above the 9000 s self-budget.  There is no tool timeout and no kill.
- TMPDIR = zx-check-v1/tmp and PYTHONDONTWRITEBYTECODE=1.
- Output: out/run1.jsonl, opened exclusively and flushed per line; stdout and stderr go to out/run1.stdout.txt and
  out/run1.stderr.txt.

## 6. Disclosure

Before the freeze, only the following ran: a Python parse check, a static extraction of ITEMS (78) and RUN1_FOUND, and
the mechanical comparison of RUN1_FOUND with run1 (57 entries, 0 mismatches).  No enumeration and no unit test ran.
