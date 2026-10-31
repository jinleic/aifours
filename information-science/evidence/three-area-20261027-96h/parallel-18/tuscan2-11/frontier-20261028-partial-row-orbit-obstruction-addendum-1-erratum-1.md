# Erratum 1 to addendum 1 of the partial row-orbit packet

Native `/bin/date` observed before writing: **Wed Oct 28 21:52:40 PDT 2026**. Owner InfoRecursiveMDS18-2, info-4. Additive. `frontier-20261028-partial-row-orbit-obstruction-addendum-1.md` (SHA-256 `c7ecf750b0748af48fc85252028cd1752341885edabdfc717169cc1882be3a12`) and the main packet (`8aed9f37…d3e4`) are unchanged.

1. **Omitted table row.** In §1 of addendum 1, the row for |H| = 4, Z_4 covers only b = 1. For b = 2 (f = 3), an element of order 4 yields b|H|/4 = 2 blocks, but every order-4 type allows b ≤ 1 ((4,4,·) by part 4; one 4-cycle by part 1 or 4). So **Z_4 with b = 2 is excluded**. The conclusion of addendum 1 is unchanged.

2. **Scope of the (6,3,2) step, stated explicitly.** The exclusion of (6,3,2) b=1 rests on a DRAT certificate for one encoding (v1 encoder, `e93b0c63…ef5`). The certificate passed the full acceptance predicate:
   - solver and checker exit codes and status lines;
   - parsed variable and clause counts equal to the header;
   - unchanged CNF and binary hashes;
   - the controls.
   The faithfulness of that encoding to the mathematical case has **not** been independently reviewed. Therefore the following are **conditional on that encoding** and are not unconditional exclusions:
   - the step from 13 to 12 open cases;
   - the Z_6 row of addendum 1.

3. **Replication attempt, recorded.** A second encoder, written separately without using S/T channel variables, block-row variables or any lemma consequence (`frontier-20261028-orbit-substitution-sat-v1.py`, `512a756b…798c`), produced CNF `…orbsub-6-3-2-b1.cnf` (`96cc45e18ba7bdbda97b6da6e937d5d8e30295a33e71b5b67615bb8ef0be0f20`, 47,806 variables / 141,130 clauses). Kissat returned **UNKNOWN** after 1,500 s. The proof stream (5,960,554,683 bytes) was therefore not a refutation (drat-trim `no conflict`, `s NOT VERIFIED`). Receipt: `…orbsub-6-3-2-b1-drat.json` (`9f622d67…dfb6`). This is **no verdict**, neither a confirmation nor a contradiction.
   - *Resource note.* drat-trim held about 6 GB of streamed lemmas in memory before reporting. Future streamed checks will cap the solver time so that proof size stays bounded.
   - A v2 of that encoder adds only two definitional facts: each symbol is first in exactly one row and last in exactly one row, and free rows are ordered by first symbol. Its bounded 600 s solve is in progress and will be recorded separately.
