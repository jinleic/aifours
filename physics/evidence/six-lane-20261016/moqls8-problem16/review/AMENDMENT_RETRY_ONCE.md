# Amendment RETRY-ONCE (K4 and K5 splits) — frozen before first use; parent approval 18:3x PDT 2026-10-17

1. Scope: the K5 cover (README §8–§8.2) and the K4 cover (README §9–§9.1, orbit plan r2), at every depth that is
   authorised by the parent. Nothing else changes: same base CNFs (K5 6ecb77a7…469b, K4 7bb806fc…01f7), same encoders,
   same declared split lists, same leaf CNF bytes (base header with C + |path units|, base body, one unit per path
   literal; SHA-256 recomputed from the base), same strict predicate, same ledgers and validators.
2. Trigger: a leaf whose strict attempt ends UNKNOWN at the native 900 s solver limit (strict receipt without
   "s UNSATISFIABLE"), or a K5 root whose old worker record is a 900 s timeout, is QUEUED.
   Excluded: K4 orbit non-representatives (c032, c064, c033, c065, c080, c096, c081, c097, c044, c076), which are
   settled only by orbit transfer from their representatives.
3. Retry: at the end of the current pass, each queued leaf is re-run ONCE in the same strict streamed pipeline —
   certify() of code/k5_resplit_r2.py (identical to code/k5_resplit.py 4aed8e43…7069 except that the drat-trim
   native limit is an explicit argument): CaDiCaL 3.0.1 `-q -t 1800` (default seed), binary DRAT streamed (not
   stored; SHA-256 and byte count recorded) into the pinned drat-trim `-i -t 3600`; aggregate RSS guard 6 GiB
   (engine + solver + checker, SIGTERM, bounded wait); disk floor 12e9 and lane ≤ 9.5 GiB before each leaf.
   A guard trip, a solver timeout or a checker timeout/failure means UNKNOWN. Runner: code/leaf_retry.py `run`.
4. Ledger: code/leaf_retry.py `ingest` writes a new ledger version: the leaf's evidence becomes the attempt-2 strict
   receipt (state CERTIFIED iff the strict conjunction holds), "attempt": 2 is set and the attempt-1 evidence is kept
   in "prior_attempts" (attempt-1 receipts remain unchanged in their files). The validators are unchanged
   (K5: code/k5_cover.py; K4: code/k4_cover.py + code/k4_orbit_r3.py).
5. Only a leaf whose attempt-2 receipt is UNKNOWN may be refined (full 128-assignment product of the next declared
   list), and only at depths the parent has authorised. No leaf gets a third attempt.
6. Smoke controls before first production use (recorded): PHP(6,5) UNSAT → verified; PHP(5,5) SAT → not verified;
   a checker-limit control (proof whose check exceeds a 1 s checker limit) → not verified.
