# One-row extension search specification v2 (2026-10-19T07:58:00-0700, ContinueCFR21)

Written only. Supersedes ext-search-spec-v1.md (dc4692e7f22d9a8e6786cef4df1313fbfb00cdf772188d62381f51298ea22087); scope remains option (a),
exact anchor beta-route equivalence. No computation is authorized. This version fixes bounded-output and chunk/estimate
semantics before either final search program is frozen.

## Input and problem
Read raw bytes ONCE, cap 1 MiB, hash those exact bytes. Grammar G1 (certificate-format-v2 section1): split on LF,
remove at most one final empty line, require every remaining line nonempty after bytes.split(); token has one optional
sign followed by ASCII digits; int token; reject underscores and blank rows. Infer k rows, common length n;
2<=k<=12, n<=120, n=3q, q>=2, q not divisible by3. Reduce entries mod n. Require pair differences to be permutations.
EXT(D) is the set of vectors f of length n with f[0]=0 and every D[x]-f a permutation of Z_n.

## Chunking and arguments
Flags (one occurrence each, `--flag value` only): --raw PATH --raw-sha256 HEX --m M --chunk-lo LO --chunk-hi HI
--max-solutions K --budget-s S; optional --mode search|estimate (default search); estimate requires --probes P --seed SEED.
M may be any integer 0..n-1. Split columns are1..M. Index of fixed values (v1,...,vM) is sum vi*n**(M-i).
Range is half-open 0<=LO<HI<=n**M. In M=0 there is one chunk0. Each f belongs to exactly one chunk.
K>=0; zero means no user solution limit. On the Kth solution stop IMMEDIATELY; its chunk is NOT_COMPLETE.
Finite self-budget 0<S<=10000. Shared deadline includes parsing, setup, search and final serialization/publication.
Every program uses only one process, stdlib, no threads/fork/exec/subprocess/multiprocessing/network, no date helpers.

## Tree/estimator meaning
Each implementation defines its deterministic search tree in its source. Knuth estimates must include ALL nodes of
that same tree, including beta-stage-to-lift-stage transitions. Uniformly choose among all children at each node;
node estimate=1+b0+b0*b1+..., per-probe, averaged for each chunk. Seeded random.Random, document exact seeding.
Estimates are INFORMATIONAL, never exclusions, and no acceptance tolerance is inferred.
If an estimate reaches a solution, verify and retain it, stop immediately with STOPPED_AT_SOLUTIONS; a real witness
is never suppressed as informational. No zero-result claim follows from samples.

## Retention limits and output
Maximum retained solutions4096. If another would be retained, stop INCOMPLETE_OUTPUT, exit6, chunk NOT_COMPLETE.
Maximum result.json16 MiB. If final serialized result would exceed it, emit compact INCOMPLETE_OUTPUT/exit6 with
solutions/chunks empty and reason documenting publication cap. Never label the emptied payload COMPLETE.
Only result.json is written, exclusive O_EXCL|O_NOFOLLOW, plain name in the verified working directory, last.
Same canonical JSON line printed: json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n'.
Exact keys: status,reason,program,n,q,k,m,chunk_lo,chunk_hi,mode,chunks,solutions,solutions_sha256,input_sha256,
program_sha256,extra,wall_s. Program hash informational; input hash derives from actual raw bytes. wall_s finite float.
Solutions list lexicographically sorted, unique, each length n with int entries in0..n-1, f[0]=0; every vector MUST be
directly rechecked against EXT(D) and fixed chunk before retention. solutions_sha256 hashes compact ASCII list bytes.
extra maps strings to integers only. Chunks listed in increasing index, including only started chunks:
search entries: {chunk:int,status:'COMPLETE'|'NOT_COMPLETE',nodes:int,solutions:int};
estimate-completed entries: {chunk:int,status:'ESTIMATE',nodes:int,estimate:finite float,probes:int}.
If estimate stops early, its partial chunk uses NOT_COMPLETE with nodes and solutions, never an estimate claim.
A COMPLETE global result means all requested chunks appear COMPLETE; ESTIMATE means all appear ESTIMATE.
Partial statuses may have COMPLETE earlier chunks and at most one NOT_COMPLETE last chunk. Nodes=count of visited
search nodes (implementation-specific, not comparable across implementations).

Status/exit: COMPLETE0, ESTIMATE0, STOPPED_AT_SOLUTIONS1, INCOMPLETE_BUDGET5, INCOMPLETE_OUTPUT6,
BAD_INPUT2, INPUT_PIN_MISMATCH2, IO_ERROR2, NOT_DM3, INTERNAL_ERROR4. All try to publish structured result.json.
Any late deadline overrun forbids COMPLETE or ESTIMATE, including after serialization.

## Agreement and claims
Same input/m/range and both COMPLETE => exact identical solutions lists/digests and per-chunk solution counts;
node counts need not match. Budget/output stops mean UNKNOWN, never negative evidence. Positive solutions trigger
candidate protocol irrespective of search status. Optional exact candidate checker A/B/C remains independent.
Control chunks (DM21/Singer57) that leave2 free columns are planted-recovery controls only, not from-scratch target
calibration. The full Zn6/Zn12 negative controls have a short parity proof in the control spec.

## Current artifacts
ext_search_beta_v1.py was written but NEVER run/compiled. Desk inspection found an invalid conditional-del statement
and a stage1-only estimator. It is WITHDRAWN; final beta source will be a new version with the full-tree estimator.
