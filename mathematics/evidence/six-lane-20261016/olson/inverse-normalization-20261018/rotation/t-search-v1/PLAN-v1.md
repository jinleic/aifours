# PLAN-v1: targeted search for the (R1) structure in the residual range (aid only, not a proof), frozen before any run

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:33:37-07:00.
- Subject: notes-ZX-residual-v1.md (fdb5ad4a...ee98), Sec. 4 (R1).
- Code: code/t_search_v1.py.  Expected outcomes: EXPECTED-v1.json.  Hashes of all three are sent before launch.
- This is the new representation from (R1), not a census of full rotation sequences.  If (S1) fails at kappa with
  3kappa <= 2p - 2, the shortest long zero-sum T must be a zero-sum of even length N in [2p + 2, 4kappa] whose nonempty
  proper zero-sub-sums all have length in [N - 2kappa, 2kappa].
- So "no such T at (p, kappa)" implies "(ZP) => (S1) at (p, kappa)" for every sequence.  As a finite statement this
  rests on the enumerator and needs an independent replay before any acceptance.

## 1. Search

For each (p, kappa) and each even N in [2p + 2, 4kappa], the script enumerates all multisets T of N odd residues mod 2p,
up to units, with:
- (T0) sum 0;
- (T1) no zero-sum sub-multiset of even length l with 2 <= l <= N - 2 and l outside [N - 2kappa, 2kappa].

Enumerator:
- It is the multiplicity-vector DFS of zs-check-v1/code/zs_check_v1.py (d9d0e073...6818), with bitmask (length, sum)
  reachability.
- Changes: the forbidden set is (T1), and the target size is N with total sum 0.
- Passes: "1-max" (residue 1 has a largest multiplicity, ties allowed) and "(1,0)-max" ((1,0) strictly largest).

For each T found (at most 6 recorded per item), the script records:
- its zero-sum lengths;
- for residual items, for each k with kappa + 1 <= k and 3k <= 2p + 1 (R = 2p + 2kappa - k): whether some W of R - N
  odd residues makes T W satisfy (ZP) at kappa.  The check is exhaustive over W when there are at most 200000
  completions; otherwise it is EXT_UNCHECKED.  Up to 3 such Y are recorded, each with its minimum generator cost.

## 2. Items (in this order)

- CONTROL_POS (7, 5): the parent's negative control g^13 (5g)^3 (R/olson-zx-s1c-parent-verdict-v1.md) has N = 16 and
  zero-sum lengths 6, 10, 16.  It must be found (control_target_found = true).  Here 3kappa > 2p - 2, outside (R1)'s
  range; it serves only as a detection control.
- CONTROL_NEG (13, 7) and (17, 9): kappa = (p + 1)/2.  Such a T satisfies (ZP) and violates (S1), so Lemma S1 (c)
  (parent-accepted) forbids it.  Expected found_total = 0.
- RESIDUAL (13, 8), (17, 10), (19, 11), (19, 12), (23, 13), (23, 14): all have (p + 3)/2 <= kappa <= (2p - 2)/3.
  No prediction.

## 3. Interpretation

- RESIDUAL found_total = 0: within the enumeration, (ZP) => (S1) at that (p, kappa).  This is an aid, not a premise.
- RESIDUAL T found:
  - if some extension Y of length R exists, it is a (ZP) sequence violating (S1) at (p, k, kappa), and refutes
    "(ZP) => (S1)" there, not ROT.  Its min_cost tells whether the Lemma ZS cost conclusion still holds;
  - if no extension exists (exhaustively), T is irrelevant at those R.
- Items not completed within the budget are ITEM_UNKNOWN.

## 4. Run protocol
- One process, within this slice's cap of 1 busy process and 2 GiB.  zx-check-v1 run1 is still running, so this
  search is launched only after that run ends, or earlier only with the parent's explicit approval for a temporary
  second process.  The shared math2 lane stays at <= 4 processes and 8 GiB.
- Disk: fresh statvfs gate via ../code/gate_v1.sh with 50000000 projected bytes, and the parent disk monitor's latest
  sample checked before launch.
- No ulimit and no timeout: the only bound is the self-budget of 5400 s (wall clock, checked every 4096 nodes), with a
  heartbeat line every 300 s.
- TMPDIR = t-search-v1/tmp and PYTHONDONTWRITEBYTECODE=1.  Output: out/run1.jsonl, opened exclusively and flushed.

## 5. Disclosure

The draft code was edited in place before this freeze: the positive control is now checked over all found T, and the
extension check is capped.  Only Python parse checks ran.  No enumeration ran.
