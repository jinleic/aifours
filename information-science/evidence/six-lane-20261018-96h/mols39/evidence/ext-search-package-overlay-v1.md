# Extension package final spec/resource overlay v1 (2026-10-19T09:00:30-0700)

Written only. This overlay plus ext-search-spec-v2.md governs final source integration. Sources remain unexecuted,
uncompiled, unparsed. Corrected R1 accepted as an existence equivalence; no target answer is obtained here.

## Normative interface clarifications
- Retain at most4096 started chunk records as well as4096 solutions; another chunk/solution =>INCOMPLETE_OUTPUT6.
- Search-mode partial result: earlier COMPLETE chunks, at most one NOT_COMPLETE final chunk. Estimate-mode partial:
  earlier ESTIMATE chunks, at most one NOT_COMPLETE final chunk, with no partial estimate claimed.
- Optional probe/seed flags in search mode: independent joint source validates then ignores them; beta source rejects
  them. The plan supplies NO such flags in search jobs, so all planned scientific domains coincide. Seed reset policies
  are explicitly per-program and not compared: beta seed*1000003+chunk, joint seed per chunk.
- Success reason differs by program: beta COMPLETE reason null; joint COMPLETE reason 'all requested chunks exhausted'.
  Gate checks the exact frozen value per job, not an arbitrary nonempty reason or missing field.
- BAD_DM exact reasons: beta 'rows 0, 1', joint 'a pair difference is not a permutation'. BAD_PIN exact reasons:
  beta 'raw hash', joint 'raw sha256 does not match pin'. Those are source-derived control sites, not arbitrary error2/3.
- Every EOF, late publication or status/exit mismatch blocks parent audit. Post-stdout deadline checks return5;
  final emitted one-line/file evidence is immutable, no second line or overwritten artifact. Some wrappers may
  emit a more explicit failure line before returning; audit requires exact expected exit and actual publication.

## Projection corrections (no runtime measurement)
The earlier beta resource note's B-node count omitted reset/min/final-supply scans if those are counted too.
Use the following conservative exact source-derived COUNTED-OPERATION upper bound instead:
B_node <= k*n + 3*k*q*r + 4*k*q + 2*n + r.
Counted operation means one logical item-index/residue computation, demand/supply reset/update, or demand/supply/MRV
comparison. It excludes interpreter/loop/object bookkeeping (separately runtime-dependent). Explanation:
- at most kn assigned demand updates; scan up ton columns;
- three kq scans/resets (demand init, minimum demand, supply init) plus finalkq supply-demand comparisons;
- at most q*r value options, each at mostk index computations,k demand checks,k supply updates;
- at mostr MRV choices plus at mostn list/assignment scans (the2n term conservatively covers column scans).
For each H node there are at most6kn neighbour-PREDICATE evaluations,3n trial-value tests andn MRV comparisons:
H_node <=6kn+4n predicate/test units. Predicates may perform several Python index/modulo operations, so H and B units
are NOT CPU cycles and do not assert equal instruction cost. Adjacency setup/direct witness recheck separately bounded.
Combinatorial B/H/joint node bounds in the resource notes are unchanged. The sharper joint bound
sum_(d=0)^r r!/(r-d)! gives N6<=326, and N12/P21/P57 planted chunks<=5 joint nodes.

## Exact joint packed payload (independent author's source-derived formula)
C=4096,I=kn,M=n(n-1), h=array('H').itemsize,d=array('d').itemsize,
b=max(1,ceil(bit_length(T(r))/8)) for search, T(r)=sum falling-factorial nodes; for P probes useP(r+1).
B=[h(k+1)+1]M+(h+2)I+(C+1)n+C(b+h+d+1).
With intended h=2,d=8, n39k6,m0,b19: B=305829bytes. Additional fixed JSON buffer16777216bytes=>17083045 payload bytes.
n21k5,m0,b8: B169741bytes, +JSON16946957bytes. This is EXACT packed-element payload, not totalRSS.
Joint non-solution-node packed-cell work <= W=2I+2(n-1)+n+2k(n-1)+4k+2U(3k+2)+2,
U=min(M,n+k(n-2)). Direct leaf check/copy uniform upper W_all=W+2I+4n.
Anchor W11505,W_all12129; n21k5 W4437,W_all4731. README details allocation/header/frames/bigints separately.
Initial raw-reader integration adds <=2MiB transient byte buffers (same-fd capped blocks plus join), released before
packed/JSON publication as source permits. Source file is not reread: wrapper injects verified source digest.

## Beta/reference storage vs RSS
The beta note's scalar-slot/reference formula is a projected capacity with Python object/layout terms separate,
not an exact allocator/RSS bound. Final package explicitly distinguishes these (the language does not specify an
exact process-RSS value). Both source families request256MiB RSS and100MB retained-output reservation per job as
ADMISSION CAPS; hitting a cap is UNKNOWN/deviation, not a proof. No measurement or guaranteed seconds fit is claimed.
Per-job outputs16MiB cap; data-maker small raw+manifest files (<1MiB expected) declared exactly.

## Authority and claims
Historical e441d858 weakened scope is withdrawn. Governingfabe57ab correction requires owned bounded /bin/date and
complete conservativeownership/census settlement for the SUPERVISOR. Science children still single-process with no
helper launches; those restrictions do NOT waive supervisor obligations. Qualified guard source/control decision and
one exact parent GO per job are prerequisites, including controls/gates/calibration. No autochain/poll/retry.
Control-positive inputs are engine-independent but derived from shared pinned datasets/construction recipe; their
role is reconstruction, not independently proving a new DM. DATA gate directly verifies actual full DM premises and
derives chunks. Full target has no executable search allocation. Seeded calibration raw estimates only, never absence.
