# Beta successor3 — work/storage accounting v3 (2026-10-19T10:13:54-0700)

Successor3 revision (ContinueCFR21c), written only. Supersedes ext-search-successor2-resources-v1.md
(034a9dc19efd3d530314c5e8f7b9cc4a4e4da15b3bde58b80c71a2e0f112ee94) ONLY by correcting its line-41 guard-clock
sentence per math MINOR m2 (4b112b556ce98fab3f046aaf6ed2202e77d7df4b8350ba5289fa77141036049b). All other v1 text
(v1 lines 3-40 and 42-end) is carried verbatim; successor3 changes no Engine/search block (beta 233bd15e..., joint
020100ee...), so no logical-unit total, node bound, frame bound or storage-inventory term changes. Unpinned
intermediate ext-search-successor3-resources-v2.md (09e151d089fe128e7944522ff782880fbc3dc121486dd0a5dc327210b36f4e80)
differs only by a line break inside the required phrase; it is superseded here and is not an operative reference.

Written only, no search/test/import/clock benchmark. Addresses math-owner MAJOR M1 and MINOR m1
(ec551589b35908b332b9233cf4d50a06b8c619d9a7155ded2139871d51714ee8).
Withdraw earlier B_node formulas in controls-resources-v1, package-overlay-v1 and final-resources-v1.
Withdraw the earlier scalar-slot S as an established upper bound and its 'depth<=n stage frames' premise.
Those immutable files remain historical, NOT the operative resource authority. No method change is used to fix a
miscount: both mathematical search blocks are byte-preserved in successor2 (package map gives exact hashes).

## Counted units, explicit exclusions
Each named logical operation counts1: I=one COMPLETE item-index/residue expression (e.g. x*q+(b[x][c]-v)%q),
U=one demand/supply fill/update or explicit state/counter-cell update, C=one named algorithmic scalar comparison/
truth test, A=one explicit left/opts append. I and U are DIFFERENT units: an assigned-column expression and its
counter decrement each count. This matches and extends the earlier declared logical-operation convention.
These are NOT machine instructions; implicit comprehension append/list allocation, Python loop/dispatch/lookup,
object headers/bigint internals, and clock calls are separate runtime costs, not silently equated to these units.

Let u be the number of unassigned columns at a B node, s=n-u, with u<=r=n-1-m. In b_pick:
- Demand initialization: kq U. Each of s assigned columns and k rows incurs ks I AND ks U (not merely ks total).
- Scan n sign tests, at mostu explicit left appends. min(demand) plus its branch <=kq C.
- Leaf any(demand) <=kq C; or non-leaf supply init kq U and final supply-demand comparisons <=kq C.
  Counting BOTH (although mutually exclusive) is conservative:3kq C and2kq U total scans/fills.
- At mostqu candidate values: k item expressions I, up tok positive-demand tests C, one result condition C,
  at most1 opts append A and k supply increments U each. Thus candidate work kqu I+kqu U+(k+1)qu C+qu A.
- Empty opts and MRV selection <=3u C. Remaining caller tests, node counters, unary-leaf counter and incoming
  assign/undo are conservatively covered by5 U and15 C constants; loop mechanics remain excluded as above.
Hence uniform per SEARCH B-node bounds, substituting s<=n andu<=r:
  I_B <= kn+kqr
  U_B <= kn+kqr+2kq+5
  C_B <= n+3kq+(k+1)qr+3r+15
  A_B <= r(q+1)
  TOTAL_B <= 2kn+(3k+2)qr+5kq+n+4r+20.
The stage2 setup is separate: kn fibre placements and2kn directed neighbour additions, not a hidden B-node unit.

For h_pick there are at most2k neighbours per column. Across up ton variables and3 trial values, <=6kn neighbour
predicates are evaluated. Each predicate costs at most1 residue expression I and2 comparisons C. Type/empty/MRV/
trial selection adds <=7n+14 C, state and node updates <=6 U (assign/undo charged to the incoming child):
  I_H <=6kn, U_H<=6, C_H<=12kn+7n+14, A_H=0,
  TOTAL_H <=18kn+7n+20.
Leaf CRT+direct witness checks, solution hashing/retention and final serialization are separate source-bounded work;
they are not charged to every nonleaf. Guard-clock overhead is separate and per visit:
B-core guard calls <= u+1 <= r+1, plus <= k calls for each adjacency construction (once per feasible B leaf,
before the H-root call); H calls exactly 1 per visit. E.g. review corner P57 m56 r0: 1+7=8 calls precede the
H-root call. Per-chunk, raw-read, input-validation and publication clock reads are further separate, non-per-node
costs. Clock work is outside I/U/C/A as before.
The formulas bound their EXACT specified logical units, not universal seconds or all Python primitive operations.

|case|n|k|m|r|B_I|B_U|B_C|B_A|Btotal|Htotal|B live frames|max H live frames|rows+D+b+a reference entries|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|N6|6|2|0|5|32|45|78|15|170|278|6|6|48|
|N12|12|2|9|2|40|61|81|10|192|536|3|3|96|
|P21|21|5|18|2|175|250|231|16|672|2057|3|3|420|
|P57|57|7|54|2|665|936|781|40|2422|7601|3|3|1596|
|anchor calibration|39|6|0|38|3198|3359|3860|532|10949|4505|39|39|936|
|review P57 m56 corner|57|7|56|0|399|670|471|0|1540|7601|1|1|1596|

## Review counterexample explicitly covered
For known P57 withm56,r0,k7,q19,n57, the assigned index/update charge is2kn=798, not399.
Even initialization+assigned work+minimum costs at least2kn+2kq-1=1063. New uniform bound1540 exceeds that lower
bound and additionally covers any(demand)/column scans/caller constants. This arithmetic is source analysis only.

## Simultaneous live storage: explicit inventory, no portable RSS claim
At an H path the ENTIRE B recursion remains suspended: up to(r+1) B frames PLUS(r+1) H frames simultaneously.
For anchor r38 this is39+39=78 stage frames, not<=39. The P21 full-domain corner would have21+21 frames, too.
The table lists the actual planned r values; planted r2 controls need at most3+3 stage frames.
main retains parsed rows AFTER constructing reduced D, and Engine retains b/a: FOUR matrix arrays rows,D,b,a,
4kn reference entries, four outer row-lists and4k row-lists, not3kn. Parsed rows may own large original integer
objects (G1 digit limit/raw cap); D,b,a are reduced values. Do not assume every original integer is7bits.
raw remains live in main during search (<=1MiB), alongside argument metadata and engine/output references.

A transparent Python-layout-dependent bound template for live DATA (not processRSS):
  H_fixed + R + 4L(k) + 4k L(n) + kn[J_input+3J_7] + 4L(n) + Dict(m+1)
  + Adj(n,k) + max(Temp_B,Temp_H,Temp_adj)
  + (r+1)[Frame_B+L(q)+B_locals] + (r+1)[Frame_H+L(3)+H_locals]
  + 2L(C) + C L(n) + Set(C) + C Tuple(n) + Chunk_list/dictionaries(C)
  + publication/digest buffers + Python allocator/interpreter/stack baseline.
Here C=4096, R<=1MiB, L/Dict/Set/Tuple/Frame/J are explicit runtime object-layout terms; J_input bounds original
parsed integers by their actual allowed token bit lengths. Adj=one outer n-list+n neighbour lists of length2k+
2kn two-field tuples. Temp_B includes TWO kq counter lists, unassigned-column listn, current+best option lists<=q,
and last item listk. Only ONE b_pick call is active while its caller's recursion frames wait. Temp_H covers h_pick
lists<=3 and predicate/iterator temporaries; Temp_adj includes q fibre bucket lists containingn column indices.
Both suspended frame families are included even when temporaries only belong to one currently running helper.
Retained f lists and tuple-set entries share some integers but are overcounted safely as separate container terms.
Serialization may create Unicode and byte buffers plus encoder state; do not count only one16MiB string or ignore
parsed rows. The source caps4096 solutions/chunks and result16MiB, and overrun is UNKNOWN. No universal numeric
RSS upper bound follows from Python language semantics. Earlier scalar S is only a RETIRED sizing sketch, not a proof.

The independent JOINT packed-buffer counts/node work bounds from README/math review are unchanged and accepted
IN SOURCE: their packed element formula is not portableRSS either. Full parent-walk readers add transient byte
blocks+joined input<=2*cap and retained parent/leaf descriptors (closed after reading), not new retained files.
Source caps remain256MiB RSS/16MiB output/100MB reservation per future individually admitted job, not measured memory.
All work/node bounds are analytical; no runtime throughput or guaranteed wall fit is inferred.

## Unchanged accepted combinatorial bounds and controls
B=sum_(i=0)^r q^i,H=sum_(i=0)^r3^i: T_beta<=B+q^r H; T_joint<=sum_(d=0)^r r!/(r-d)!.
Control betaN6<=11711,N12<=229,P21<=694,P57<=5074; jointN6<=326, other planted<=5.
These do not assert a small full target tree. Future256-probe path bounds joint<=9984,beta<=19968 forr38 remain
INFORMATIONAL ONLY, no exclusion and no deterministic search GO. Controls20/separate calibrations2 unchanged.
