# One-row extension search — problem and format specification v1 (2026-10-19T07:53:30-0700, ContinueCFR21)

Normative for every program of the "beta-route extension search" package (scope note
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/scope-note-beta-route-search-v1.md, sha256 95ed1ed365a1d522e7c13c1a63a7e5d59ce435a0c6d7497bd5281c04f84bd645). Written only; nothing is run under this file.

## 1. Input
A raw file in grammar G1 (lemmaU-certificate-format-v2.md section 1, sha256 a36ce58f481a6a0b4bc62a121951331a4f98276a624d79ea2b488fcd608bf64e). It is read once, at most
1,048,576 bytes; its sha256 and its parse use the same bytes. It gives k rows of n integers. Requirements:
2 <= k <= 12; n = 3q with q >= 2, q % 3 != 0 and n <= 120. Entries are reduced mod n. The rows must form a
(Z_n, k; 1)-difference matrix D: for every pair of rows x < y, c -> (D[x][c] - D[y][c]) mod n is a bijection on the
column set {0, ..., n-1}.

## 2. Problem
EXT(D) = the set of f in Z_n^n with f[0] = 0 such that, for every row x, c -> (D[x][c] - f[c]) mod n is a bijection.
(If f is an extension, so is f + t for any constant t, so the normalisation f[0] = 0 loses nothing.)
Programs enumerate EXT(D) within a chunk range (section 3). Every reported f is re-checked against this definition
before output.

## 3. Chunks (deterministic static split)
Parameter m with 0 <= m <= 3 and m <= n - 1. The split columns are 1, ..., m. Chunk index of an assignment
(v_1, ..., v_m) in Z_n^m is idx = sum over i of v_i * n^(m - i), so v_1 is the most significant digit. Chunk idx is the
set of f in EXT(D) with f[i] = v_i for i = 1..m. A job is given a half-open range [lo, hi) with
0 <= lo < hi <= n^m and treats its chunks in increasing order. For m = 0 there is one chunk, index 0.

## 4. Command line (identical for every search program; "--flag value" pairs only, each flag at most once)
--raw RAW --raw-sha256 HEX --m M --chunk-lo LO --chunk-hi HI --max-solutions K --budget-s S [--mode MODE]
[--probes P --seed SEED]
- K >= 0, where 0 means unlimited. Once K solutions have been reported, the program stops after the chunk in which
  the K-th solution was found. That chunk and all later ones are not COMPLETE.
- S is finite with 0 < S <= 10,000. The program checks its deadline cooperatively and before publication.
- MODE is "search" (default) or "estimate". In estimate mode the program runs P >= 1 seeded random root-to-leaf
  probes of its own search tree for each chunk of the range (Knuth's estimator: the estimate is the sum over levels
  of the product of branching factors). It reports per-chunk mean estimates. These are INFORMATIONAL ONLY: never
  evidence of absence, and never a gate of anything except the parent's own resource planning.

## 5. Output (only plain file names, created exclusively in the working directory, which is the verified job root)
result.json is written last. Its bytes are the printed line plus a newline, in canonical serialisation:
json.dumps(obj, sort_keys=True, separators=(",", ":")).
Keys (exactly): status, reason, program, n, q, k, m, chunk_lo, chunk_hi, mode, chunks, solutions, solutions_sha256,
input_sha256, program_sha256, extra, wall_s.
- status:
  - "COMPLETE": every chunk in the range is exhausted;
  - "STOPPED_AT_SOLUTIONS": K reached;
  - "INCOMPLETE_BUDGET";
  - "ESTIMATE";
  - "BAD_INPUT", "INPUT_PIN_MISMATCH", "NOT_DM", "IO_ERROR" or "INTERNAL_ERROR".
- program: a fixed name string.
- chunks: list, in increasing idx, of {"chunk": idx, "status": "COMPLETE" | "NOT_COMPLETE", "nodes": int,
  "solutions": int}. In estimate mode it is {"chunk": idx, "status": "ESTIMATE", "nodes": int (probe nodes
  visited), "estimate": float, "probes": P} instead.
- solutions: list of every reported f (n integers, f[0] = 0), sorted lexicographically, each re-checked.
- solutions_sha256: sha256 of json.dumps(solutions, separators=(",", ":")) encoded as ASCII.
- extra: an object with program-specific integers only (for example stage-1 counts); informational.
- program_sha256: the program's own file hash, informational only.
- wall_s: a finite non-negative float.
Exit codes: 0 for COMPLETE or ESTIMATE; 1 for STOPPED_AT_SOLUTIONS (a candidate or planted hit; it is not an
error); 5 for INCOMPLETE_BUDGET; 2 for BAD_INPUT, INPUT_PIN_MISMATCH or IO_ERROR; 3 for NOT_DM; 4 for
INTERNAL_ERROR.

## 6. Agreement rule between two independent programs (used by the expectation gate)
For the same input, m and range, both programs COMPLETE implies identical "solutions" lists (byte-identical
solutions_sha256) and, per chunk, identical solution counts. Node counts are not compared.
