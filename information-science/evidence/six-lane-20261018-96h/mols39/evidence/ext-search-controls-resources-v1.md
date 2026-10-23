# Extension controls, work and storage projection v1 (2026-10-19T08:04:14-0700)

Written only. No runtime is measured here. scope-note-beta-route-search-v1.md is refined as follows (no target change):
- ext-search-spec-v2.md supersedes v1: m may be up to n-1 for planted chunks; max4096 retained solutions/chunk records;
  output16MiB; all exhaustion/retention/budget states distinguished.
- Final beta producer is ext_search_beta_v2.py, NOT v1 (v1 withdrawn unexecuted: syntax and stage1-only estimator).
  It uses recomputed supply/demand MRV, not incremental counters, and binary GF3 contrast DFS rather than the scope
  note's proposed elimination+enumeration. This is the same exact lift condition: for each triple fibre, three values
  are distinct iff every pair is unequal. No rank assumption and no scientific scope reduction.
- N12 control is a single planted partial chunk, not a full Z12 enumeration. This avoids an unbounded control job.
  N6 covers its entire normalized extension space.

## Frozen control generation (not executed)
ext_search_controls_v1.py reads pinned existing DM21 raw data, constructs files by its own stdlib code, DM-checks the
positives, and emits fixed output files plus a digest manifest. It imports/executes no Sage or third-party code.
Controls:
N6: rows0 and id over Z6, m0, one full chunk. Must finish with zero.
N12: rows0 and id over Z12, m9, split values vi=2i mod11 fori1..9. Two free columns. Must finish with zero.
Proof for both negatives: if [0,id,f] were a DM, f and id-f would be permutations. Put S=sum_Zn t=n(n-1)/2.
Then sum(id-f)=S-S=0 mod n but a permutation sums to S=n/2 !=0 mod n for even n. Contradiction.
The prefix for N12 is a valid partial near-complete mapping; the same argument rules out any completion.
P21: first5 rows of known six-row DM21. The translated deleted row f=D5-D5(0) is an extension, since each old-new
row difference is a translate of an original permutation. m18 fixes columns1..18 of that f, leaving2 free.
P57: first7 rows of a Singer-type eight-row DM57, generated from the published B=(1,6,7,9,19,38,42,49) difference set
and the GF8 OA recipe. m54 fixes columns1..54 of the normalized deleted row, leaving2 free.
The known deleted row must appear; both COMPLETE programs must return the same entire chunk solution set.
These are reconstruction/CRT/chunking controls, NOT evidence of full target feasibility.
BAD_DM: two zero rows over Z6 -> NOT_DM, direct pair failure (0,1).
BAD_PIN: valid N6 bytes with the unrelated known DM21 hash -> INPUT_PIN_MISMATCH.
Any unexpected outcome stops, no repinning. No target search is authorized by controls.

## Exact worst-case node counts (not estimates of actual search work)
Let r=n-1-m free columns. A q-ary stage-B tree has at most B=sum_(i=0)^r q^i nodes and q^r leaves.
Every B leaf may have an H tree of at most H=sum_(i=0)^r 3^i nodes, including its root (the unary transition).
Thus T_beta <= B+q^r*H. T_joint <= sum_(i=0)^r n^i because each node assigns one previously unassigned column.
Pruning, prefix inconsistency and row constraints reduce these bounds; the bounds prove small planted controls, not
that the unrestricted anchor can be finished. Output cap stops are UNKNOWN.

|case|n|k|m|r|B|H|T_beta upper|T_joint upper|
|---|---|---|---|---|---|---|---|---|
|N6|6|2|0|5|63|364|11711|9331|
|N12|12|2|9|2|21|13|229|157|
|P21|21|5|18|2|57|13|694|463|
|P57|57|7|54|2|381|13|5074|3307|
|anchor|39|6|0|38|2315311846695714396986672292572693311181523|2026277576509488133|4330582594695045868161685186254963903384827589046700898711280|2963030196370294540520774973391817366584002768926224131840841|

## Counted work per beta node (exact source-derived upper bound, no seconds claim)
Define one counted operation as a residue/index evaluation, a demand/supply counter update, or one comparison of
those counters. Exclude interpreter/object/allocation overhead, which is runtime-specific.
B node: at most k*n + 3*k*q*r + 2*k*q + r counted operations, plus bounded list scans/allocations.
H node: at most 6*k*n + 4*n counted comparisons/residue operations. Each column has2*k directed neighbours.
B-to-H setup: at most k*n bucket placements + 2*k*n neighbour additions; one direct candidate recheck adds k*n
difference computations and n CRT combinations. Every retained solution is rechecked independently by the gate.
These formulas are upper bounds on algorithmic work, NOT measured CPU rates.

## Retained-storage projection
For beta v2, D/b/a contain3*k*n scalar slots; demand and supply2*k*q; neighbours2*k*n pairs (list refs plus pair
fields budgeted as6*k*n slots); depth<=n stage frames each retaining at most q+4 scalar refs; g/h/fixed/transient
buffers budgeted12*n; retained solutions in both list and set<=2*4096*n; chunk dictionaries budgeted16*4096 slots.
Define exact projected scalar-slot budget
S=3*k*n+2*k*q+6*k*n+(q+4)*n+12*n+2*4096*n+16*4096.
This is a source-derived reference/counter capacity projection, not an exact CPython RSS statement. A 64-bit slot
accounts for8*S payload bytes; Python headers, frames, allocator arenas, big-int indices, the1MiB raw input and the
16MiB JSON serialization buffer are additional. For these fixed small raw controls/target, request a256MiB RSS cap;
conservatively reserve128MiB incremental heap for Python objects/serialization and interpreter baseline separately.
No memory measurement has occurred. No exact universal RSS bound can be inferred from Python source alone.

|case|S scalar slots|8*S payload bytes|B-node counted upper|H-node counted upper|
|---|---|---|---|---|
|N6|114912|919296|85|96|
|N12|164312|1314496|90|192|
|P21|239066|1912528|387|714|
|P57|538332|4306656|1465|2622|
|anchor|388417|3107336|9320|1560|

## Target decision boundary
Only historical fact: prior joint free0 producer v2 visited8,081,408 nodes in281.85s without exhausting (T6), so its
own total tree >8,081,408; this is NOT a bound for either new tree. Neither new node throughput nor actual total work
is known. The huge worst-case bounds above preclude a claimed guaranteed completion.
The proposed next executable item, IF separately admitted, is calibration ONLY: 256 seeded Knuth probes on each
new tree (m0,seed1,budget240s), estimator raw observations. No tolerance/absence verdict follows; parent decides whether
any subsequent deterministic chunk work has scientific/resource value. Full-range search jobs are NOT in the plan.
No seconds-per-node allocation or promise to finish is made. Underflow, incomplete probes and output stops are
reported, not converted into negatives. A real hit, even during estimation, stops and triggers candidate handling.
