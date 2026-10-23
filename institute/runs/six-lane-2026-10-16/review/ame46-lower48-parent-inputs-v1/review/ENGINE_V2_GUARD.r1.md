# Engine v2 for the AME(4,6) support lane: resource guard and enumeration scope (r1)

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. This file freezes the
engine before any search is run with it. No result of v2 is claimed here except the smoke receipts in §6.

## 1. Status and what stays untouched
- The frozen engine `code/large_t_gen.py` (28c0c1f9e32089d0080869689be6ea7fd3dd93ae5239cf0c7131cf4c4607bcfd) and the
  18 certificate inputs pinned in `evidence/lower46_receipt.json` are unchanged and remain the basis of
  `review/SUPPORT_LOWER46.r1.md`.
- **Resource violation.** The (26,0) run of that engine reached about 35 GiB RSS at 12:39, against an 8 GiB cap, and
  was stopped with SIGTERM. Its outcome is UNKNOWN. The guard in this file exists because of that excursion.
- v2 is the new file `code/large_t_lex.py`, SHA-256
  `cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8`. It imports, without modifying:

| file | SHA-256 | used for |
|---|---|---|
| `code/large_t_gen.py` | 28c0c1f9…bcfd | `SmallGen` and `build_gen` (N-only CNF), `component_checks`, `moduli_certificate` |
| `code/large_t_e0.py` | 67033dcf…466c | `profiles`, `PAIRS` |
| `code/phase_check.py` | 0c591d1b…f693 | exact 2×2 phase check (HNF) |
| `code/ame_e0_cnf.py` | 97e30ae4…8a26 | `CNF.at_most_k` (completion CNF) |
| `code/lratcheck` / `.c` | b4e14cd9…3470 / e9da1fa8…5159 | C LRAT checker |
| `code/lratcheck_py.py` | 7bc9cff7…7edd | independent Python LRAT checker |

## 2. What v2 changes and what it keeps

**Kept, and identical in meaning:**
- the per-profile N-only CNF (lines 0 or ≥2, hole counts d_{i,a}, |N| = 2h+e, combinatorial row and column
  orthogonality in all three reshapings);
- the per-solution checks: components including closure, moduli exclusion only by an exactly verified Stiemke
  certificate, the exact phase obstruction, and classical completion.

`completion_text` is a line-by-line in-memory transcription of `large_t_e0.completion_cnf`: the same allowed-point
set, one exactly-one constraint per non-hole line, and an empty clause when a non-hole line has no allowed point.

**Changed:**
1. **Enumeration.** No orbit is materialised. For a generating set Γ ⊆ H, v2 adds the lex-leader constraints
   X ≤_lex g(X) for every g ∈ Γ, over the point variables in the fixed order `S.points`. It then blocks each found
   solution individually.
   - H is the group the frozen engine used: value permutations inside each d-class of V_i, and coordinate
     permutations among coordinates with equal partitions.
   - Γ consists of adjacent transpositions inside each d-class, and adjacent transpositions of equal-partition
     coordinates. `profiles` lists coordinates in canonical order, so equal partitions are contiguous.
2. **I/O.**
   - CNFs are built in memory and given to CaDiCaL on stdin; exploration runs write no CNF.
   - In proof mode, CaDiCaL writes a gzip-compressed text LRAT stream (`*.lrat.gz`).
   - Both checkers read the CNF from a FIFO fed by a Python thread, and the proof from `gzip -dc` through a pipe. No
     uncompressed proof bytes are stored, and the FIFOs occupy 0 bytes.
3. **Resource guard** (§4).

## 3. Completeness of the enumeration and transfer of exclusions
**Claim.** Let Sol be the set of point-assignments X of a profile CNF that extend to a satisfying assignment. Assume
every g ∈ H maps Sol to Sol. Let F be the found solutions at the moment the solver reports UNSAT for
CNF ∧ LexΓ ∧ {¬X : X ∈ F}. Then every X ∈ Sol lies in the H-orbit of some member of F.

**Proof.**
- Let X ∈ Sol and let X* be the lexicographically least element of its H-orbit, which lies in Sol.
- For every g ∈ H, g(X*) is in the orbit, so X* ≤_lex g(X*). In particular X* satisfies LexΓ for any subset Γ ⊆ H.
  The chain encoding of `add_lex_leader` is satisfiable by X* with e_k set to "prefixes agree up to k".
- If X* ∉ F, then X* would satisfy every blocking clause ¬X (X ∈ F, X ≠ X*), contradicting UNSAT. So X* ∈ F, and
  X = h(X*) for some h ∈ H. ∎

**Why the assumption holds.** Each generator is a symmetry of the CNF up to renaming of auxiliary variables. A value
transposition inside a d-class preserves all hole counts, and the line and overlap constraints are defined uniformly
over V_i. An equal-partition coordinate swap permutes the three reshapings and their row and column roles. This is
the same invariance the frozen engine's orbit blocking used (`review/SUPPORT_LOWER46.r1.md` §3).

**Transfer.** All per-solution checks are invariant under H, by the same section of LOWER46. So excluding every member
of F excludes Sol. F may contain several members of one orbit, and each is checked anyway. A complete enumeration
ends only in exact UNSAT. Any other solver status gives UNKNOWN.

## 4. Resource guard and preflight

**Pre-bounds**, computed before any group or CNF is generated, per profile:
- product-space size P = Π|V_i| (cap `--max-product` 1296);
- group order |H|, computed by formula without materialising (cap `--max-group` 10^15);
- estimated literal count, and from it the estimated in-memory CNF bytes (literals × 80, cap `--max-mem` 2 GiB).

A profile above any cap is UNKNOWN and is not attempted.

**RSS watchdog.**
- A thread samples `ps -o rss=` of the engine process plus its live child (solver or checker) every 1 s.
- Above `--rss-cap` (default 6 GiB, total) it trips: the child gets SIGTERM, followed by a bounded wait of 30 s.
  **Never SIGKILL.**
- After a trip, no new solver or checker call starts (`solve` and `check_stream` refuse), and any child that is
  still alive is terminated on every watchdog cycle.

**Disk accounting** (exact bytes, against the lane cap):
- At start: B0 = max(du -sk × 1024, Σ file sizes) over the whole lane, and budget = min(`--disk-budget`,
  10·2^30 − 256·2^20 − B0) bytes. At 12:48:31, B0 was du 9,334,255,616 B, which leaves 1,134,727,168 B. The default
  per-run budget is 512 MiB.
- Every completed proof stream is counted. During a solve the watchdog also adds the current size of the growing
  `.gz` stream, and trips when written + stream > budget.
- Overshoot is bounded by about 1 s of stream growth plus the SIGTERM latency. In S9 it was 4.7 MB. The 256 MiB
  headroom and the per-run budget absorb it.

**Other limits.**
- At most 5000 solutions per profile (`--max-solutions`).
- CaDiCaL's native time limit, `-t` 600 s per call.
- CPU: the engine process (which waits during each call), one solver or checker child at a time, and in proof mode
  one `gzip` helper (CaDiCaL's compressor, or `gzip -dc` feeding a checker). So at most two processes are busy at
  once, the second being the light gzip. This fits the parent's current 2-CPU limit and the lane limit of 4. The
  watchdog's RSS covers the engine and the solver or checker, not the gzip helper.

**Semantics.**
- The case outcome is UNKNOWN with `excluded = false` after any trip, for any profile above a cap, and for any
  enumeration or completion solver status other than 10 (SAT) or 20 (UNSAT); that includes 0 for a time limit and
  −15 after SIGTERM. Profiles enumerated before such an event are not accepted as a partial result.
- Exploration mode (no `--proof`) reports at best `EXCLUDED-EXPLORATION (no proofs; not a certificate)`. Only
  `--proof` with both checkers verifying every final and completion stream can yield `EXCLUDED`.

**Preflight for the next candidate cases** (pre-bounds only; nothing generated). Columns: number of profiles, maximum
product space, maximum |H|, maximum estimated CNF memory.

| (t,e) | h | profiles | max P | max \|H\| | max est. memory |
|---|---|---|---|---|---|
| (26,0) | 10 | 25 | 625 | 4,976,640,000 | 115.7 MiB |
| (28,3) | 8 | 7 | 256 | 7,962,624 | 24.8 MiB |
| (27,2), (27,3) | 9 | 6 | 256 | 31,104 | 24.8 MiB |
| (28,2), (28,4) | 8 | 7 | 256 | 7,962,624 | 24.8 MiB |
| (29,3), (29,4), (29,5) | 7 | 1 | 81 | 384 | 4.4 MiB |
| (30,4), (30,5), (30,6) | 6 | 2 | 81 | 31,104 | 4.4 MiB |
| (24,0) | 12 | 158 | 1296 | 6,449,725,440,000 | 445.1 MiB |
| (26,2) | 10 | 25 | 625 | 4,976,640,000 | 115.7 MiB |

The number of solutions under partial lex-leader breaking, and the solver times, cannot be bounded in advance. They
are controlled by the solution cap, the time limit and the RSS and disk watchdogs, and a hit gives UNKNOWN.

## 5. Known limitations
- RSS is resident memory sampled by `ps` at 1 s intervals, so a faster spike between samples is not seen. The 2 GiB
  margin between the 6 GiB default cap and the 8 GiB lane cap covers growth below 2 GiB/s.
- The memory pre-bound is an estimate and not a proof. The hard stop is the watchdog.
- Lex-leader breaking with adjacent generators is complete but not minimal. Duplicates within an orbit cost time,
  not soundness.
- CNFs piped on stdin are not stored. A certificate run therefore stores the compressed proofs, and a re-check
  regenerates the CNF deterministically from the profile and the pinned code.

## 6. Smoke receipts (13:00:52–13:00:56, on the final v2 code above)
Runner `code/guard_smoke.py` (3b4d8c9b03bb2465ce6c3e05ea6176d39cabe2754e21d559d3756e85b059e308). Outputs:
`evidence/guard_smoke.json` (3c4ea4e6ad2346f358378c264994093e2dc1f58f4d288c3b927978cbf8c9db46) and
`evidence/guard_smoke.stdout.txt` (08b1060100e5322a651d8db45a0f52f0e36975ff14e70717a623d695e3628776). Case (30,0)
unless stated otherwise.

| run | setting | observed | expected |
|---|---|---|---|
| S1 | defaults, exploration | EXCLUDED-EXPLORATION, no trip | match |
| S2 | defaults, `--proof` | EXCLUDED; 3 compressed streams (2 final, 1 completion) verified by both checkers | match |
| S3 | `--rss-cap` 20 MiB | UNKNOWN; tripped "RSS 25526272 B > cap 20971520 B" | match |
| S4 | `--proof --disk-budget 1000` | UNKNOWN; tripped "disk: written 9602 B > budget 1000 B" | match |
| S5 | `--max-solutions 0` | UNKNOWN (solution cap) | match |
| S6 | `--max-product 50` | UNKNOWN (pre-bounds, not attempted) | match |
| S7 | `--max-group 1` | UNKNOWN (pre-bounds, not attempted) | match |
| S8 | live CaDiCaL on PHP(12,11), RSS cap = own RSS + 8 MiB | tripped "RSS 37076992 B > cap 29720576 B"; child exit −15 (SIGTERM) | match |
| S9 | live CaDiCaL writing a compressed stream, budget 65536 B | tripped at a 4,718,592 B stream; child exit −15 | match |

all_required_true = true.

**Consistency.** In S2, v2 found 4 solutions for profile {3,3}{2,2,2}³: 3 phase obstructions and 1 completion UNSAT.
It found 0 for {2,2,2}⁴. The frozen engine found 2 orbits for the first profile (1 phase, 1 completion) and none for
the second. Both report (30,0) excluded. These smoke streams are not certificates of this file. S4 reused the S2
output names.
