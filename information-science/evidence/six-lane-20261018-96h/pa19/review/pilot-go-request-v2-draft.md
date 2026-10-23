# PA19 pilot GO request v2 (DRAFT, not sent; final JSON follows the r5 review)

Supersedes request v1 (`review/pilot-go-request-v1.json`, fa74f887…), whose runner v3 got a parent NO-GO.

- **Items (unchanged):** b00070:00000-00024, b00005:00200-00299, b00005:00300-00350 (ms09). The coverage mapping and scientific consequence are as in v1.
- **Runner:** `code/pilot_file_drat_v12.py`, d2fa262f8ded9f9c4eedf6c52f3b0543581961a92b47fc5e0f9ddff5fb53da58.
  - Review chain: Codex r1 (v5) → r2 (v8) → r3 (v9) → r4 (v11) → r5 (v12). Every reviewer header read gpt-6.1-sol / openai / read-only / max.
- **Transport:** the CNF file is retained and SHA-pinned. kissat writes its binary DRAT to a lane FIFO, which an owned sink copies into an exclusive proof file. That file is hard-capped at 1,258,291,200 B; excess is drained and discarded, then SIGTERM. drat-trim checks the retained files.
- **UNSAT predicate:**
  - solver: self-exit rc20 with exactly `s UNSATISFIABLE`;
  - proof sink complete: connected, eof, no error, no discard, file re-hash equal, FIFO inode unchanged;
  - checker: self-exit rc0 with exactly `s VERIFIED`;
  - the header line equals the frozen CNF header;
  - `read N bytes from proof file` equals the proof bytes;
  - none of these strings: early EOF, trivial UNSAT, ERROR, MEMOUT, wrong prefix, TIMEOUT, NOT VERIFIED;
  - CNF and proof re-hash unchanged;
  - both children settled; terminal gate (registry, floor) clean;
  - commit boundary: no earlier cancel stamp and no latch.
- **Controls C1-C7** (same binaries; run first; the first deviation stops the run):
  - C1: PHP(6,5) must pass.
  - C2: a well-formed CNF with one literal removed must reach a completed checker outcome and be rejected for CNF digest.
  - C3: a trailing proof byte must give a completed `s VERIFIED` that is rejected for consumed-bytes and wrong-prefix.
  - C4: a SAT formula with a foreign proof must give a completed `s NOT VERIFIED` rc1.
  - C5: a 4096 B hard cap must give stop=proof_cap and a file of at most 4096 B, settled.
  - C6: `--time=1` must give a clean self-exit with no verdict.
  - C7: a missing input must give a clean error exit, and the sink must settle.
- **Exits:** 0 means the plan is complete; it is not a science verdict. 10 SAT candidate; 20 controls failed; 30 admission refused; 40 cancel; 50 safety (latch, unsettled or memory diagnostic); 60 exception; 70 prestart refused.
- **Resources:**
  - reservation 4,092,208,905 B (run records 1,572,864 + controls 174,067,713 + 3 × 1,305,522,776);
  - lane RSS trip 6 GiB; at most 2 busy processes;
  - stability rule and fresh statvfs before every child;
  - in-flight floor 12e9;
  - per-child cutoff reserves a 220 s settlement tail;
  - absolute end = start + 10,310 s; plus 180 s fits the 10,800 s chunk;
  - expected wall time about 20 min.
- **Evidence:**
  - list replay of the b5/b70 lists, byte-identical (45869ceb…);
  - kissat rel-4.0.4 source evidence (d4495a3f…);
  - binary imports (c822c4f0…);
  - STOP registry (ee370929…), with per-marker dispositions as in v1.
