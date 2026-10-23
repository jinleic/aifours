# README addendum v1

Written 2026-10-18, starting 09:44 PDT by the host clock. It does not change any frozen file.

1. **Time correction.** The frozen `README.md` says it was created "about 09:40 PDT", and the frozen `rules-v1.md` says "about 09:35 PDT". Both were estimates written before the clock was read. The actual freeze time, by the host clock, is **09:33:21 PDT**, as recorded in the first line of `evidence/freeze-v1.sha256`. Read the host-clock record; the times in the file text are wrong.
2. **Frozen run (09:37 PDT).** `code/core5_engine_v1.py` (65ce5a00…2eb1) wrote `evidence/engine-v1-run1/`.
   - All 21,150 patterns are killed except one.
   - The survivor is S-D: code `1122333333/10`, with E2 = 1 and E3 = 0.
3. **Candidate proof.** `proof-v1.md` (e35bfa0e…c698), frozen at 09:43:21 PDT.
   - It refutes S-D with the new Lemma R (right-coset fibres over a vertex subgroup).
   - Status is CANDIDATE: unreviewed, computer-assisted, not Lean-checked.
4. **Control C4: targeted demos.** Two of the three targeted demos were badly designed. In each, the demo pattern was killed first by a rule other than the one being demonstrated:
   - the star-1111 pattern by T;
   - the star-3333 pattern by K.

   So those two demos do not test the intended mutation. The general C4 check is unaffected: all 21,149 witnesses re-verify, and 634,470 single-label mutants were tested. Corrected targeted demos go in a separate control script, v2.
