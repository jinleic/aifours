# Checkpoint 007 (Slice A, OlsonSTABSuccessor)

Written after /bin/date 2026-10-19T06:46:13-0700.  Written work only; no computation, model call, launch or edit of an existing file.
Process deviation: checkpoint-006 was at 06:08:22, so this one is about 38 minutes later (more than 1800 s).  The gap includes the
interval after my final report (report-sliceA-v1.md, 06:14:51) until the parent's next instruction re-woke this worker.
- NEW proof-LSplus-red-v1-addendum-2.md f2984d80340f80569a1e9f91cde61db2edb8d3f35582b6334d8cae722f96d2b7 [W, unreviewed]: case a = -1/2 of LS+-RED is impossible for e >= 3 and
  prime p >= 10e - 13 (equivalently p >= 10e - 16).  Method: involutions as units (Lemma 0), Z0 splits into positive/negative terms,
  first-crossing bounds P_(Z0+) <= max(A, 0) and Omega_(Z0-) <= delta0 - 1, then the t-form of (L) fails for every W.  Even
  involution deletion is recorded as Remark 4 (excludes the sub-case E'' <= delta' for every p >= 9e - 13); not needed for the theorem.
  Retained: a = -1/2 with E'' >= delta' + 1 for primes 9e - 13 <= p <= 10e - 17 ((23,4), (41,6), (43,6), (53,7), (59,8), (61,8), ...).
- NEW proof-LSplus-lin-v1.md 1372a691022cfef9a75c0fceec73054563e2b3d411e12c739ef27970587667cf [W, assembly]: LS+(p, kappa) for e = 2 and for e >= 3 with p >= 10e - 13 (sharp),
  conditional on CT/CTgen/LS+2 (delta review pending) and on the unreviewed LS+-RED + addenda 1, 2.  Exceptional cells listed
  exactly: 3 <= e <= floor((p-1)/3) with p < 10e - 13, minus BASE1 cells; for p <= 31: (11,8), (13,10), (17,12-13), (19,14-15),
  (23,16-19), (29,20-24), (31,22-26).  No new LS cell (all inside LS-lin's range).  STAB not covered.
- Next justified lever (same STAB target, not started): STAB-lin, i.e. the same CT/CF machinery at length 3kappa + 1 (CT with
  n = kappa - 1), where the two-heavy case must yield exactly E2 and the one-heavy case a in {1, -1, -1/2, -1/3} must yield exactly E3
  (a = -1/3) or a contradiction.
