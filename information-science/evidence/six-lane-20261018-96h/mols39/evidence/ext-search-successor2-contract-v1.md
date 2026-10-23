# Beta extension successor2 — complete runtime/output contract (2026-10-19T09:32:48-0700)

Written only. Addresses both owner reviews, math ec551589... and admission48454076....
No source imported/executed/compiled/AST-parsed/tested, no controls/probes/search/configs. One successor package,
old evidence intact. Mathematical enumeration blocks unchanged; operation/storage document supersedes old bounds.

## Scientific/interface scope unchanged
ext-search-spec-v2.md solution/chunk/estimate semantics remain, with this stronger publication/schema contract.
20controls/data/gate jobs and2SEPARATE informational calibrations only; no deterministic target search allocation.
Normalized f[0]=0, correctedR1 existence equivalence only, no widerbeta family. COMPLETE peer sets compared exactly.
Qualified finalG-CONTROLS means controls only, target_claim always UNEVALUATED. Any actualtargethit stops/pins and
requires independent A/B/C+parent checks. Caps/budget/errors/estimates never negative evidence.

## All runtime file consumers: anchored parents, nonblocking regular one-link descriptors
Source loaders, raw-data readers, control/pin/plan readers and artifact/audit readers all walk ABSOLUTE NORMALIZED
parent components from retained '/' fd using O_DIRECTORY|O_NOFOLLOW, never string-resolve a symlinked ancestor.
The leaf opens O_RDONLY|O_NONBLOCK|O_NOFOLLOW relative to that retained parent fd, then fstat must show regular,
nlink==1 and size within cap BEFORE reading. The SAME descriptor is read in<=64KiB blocks, actual total<=cap+1,
rejecting overflow (including growth). Check nlink again before returning. FIFO cannot block before fstat.
Algorithm-source cap1MiB; raw cap1MiB; plan/source-pin/artifact cap16MiB (wrapper plan preflight4MiB); audit cap1MiB.
Gate readat(dir_fd,name,cap=CAP) has an EXPLICIT cap parameter, eliminating the undefined-name blocker.
Entrypoint input preflight opens/checks/closes descriptor WITHOUT reading raw bytes. Algorithms themselves make the
single actual raw read and hash/parse identical bytes. Preflight is NOT substituted for actual-consumer guarantees.
Source bytes are hashed then compiled in-process; wrapper injects verified source digest, no source reread.
Parent path/link/read errors retain IO/entry-error/deviation taxonomy, never intended NOT_DM orPIN_MISMATCH sites.
No snapshot files, process/helper launches or new child output names.

## Complete search result schemas (canonical, exact17keys)
status,reason,program,n,q,k,m,chunk_lo,chunk_hi,mode,chunks,solutions,solutions_sha256,input_sha256,
program_sha256,extra,wall_s. All keys mandatory; no extras. Strict JSON rejects duplicates/nonfinite values.
Typed equality distinguishes bool/int/float. Every hash lowercase64hex; input hash binds actualraw; solution hash binds
actualcompact solutions bytes. Source selfhash informational only. wall_s finite NONNEGATIVE FLOAT, notnull/int.
Planned intended outcomes only COMPLETE/NOT_DM/INPUT_PIN_MISMATCH. Any other status blocks controls qualification.
Per-status metadata:
- COMPLETE (both): n,q,k,m,lo,hi exact integers derived from actualraw+independently derived chunk; mode='search'.
  beta reason=null and extra EXACT {stage_b_leaves:int>=0,stage_h_nodes:int>=0}; joint reason='all requested chunks
  exhausted' and extra EXACT{}. solutions<=4096 sortedunique vectors ofn exactints0..n-1 withf0=0; gate directly
  verifies each EXT(D) and fixedchunk. chunks<=4096 exactly requested range in increasingorder, each exactkeys
  {chunk,status,nodes,solutions}, statusCOMPLETE, nonnegativeintnodes, exact perchunk solutioncount.
- NOT_DM (both): exactn6,q2,k2,m0,lo0,hi1,mode='search'; chunks=[],solutions=[],extra={}, digest SHA256('[]').
  beta reason='rows 0, 1'; joint reason='a pair difference is not a permutation'. ActualBAD_DMraw duplicatedzeros
  and status comes aftershape/args publication, before any chunk/engine allocation.
- INPUT_PIN_MISMATCH beta: n,q,k,m,lo,hi,mode allnull (site precedes metadata publication).
- INPUT_PIN_MISMATCH joint: n,q,k null, m0,lo0,hi1 integers, mode='search' (argument metadata precedes rawpin).
  Both: chunks=[],solutions=[],extra={}, emptylistdigest; beta reason='raw hash', joint reason='raw sha256 does not
  match pin'. No arbitrary malformed metadata or falseCOMPLETE chunk survives an early-error return.

## Prior gate result schema
Exact keys status,reason,self,plan_sha256,prefix,all_as_expected,qualified,target_claim,items,wall_s.
Successful priorgate hasOK,nullreason, exactself/planhash and exact orderedprefix; booleans true/false as appropriate,
UNEVALUATED targetclaim and finite nonnegative FLOATwall. items MUST equal the current gate's independently
recomputed actual audited-prefix records, in order, each exact {item,problems,artifacts}. Successful records have
emptyproblems and exact actual declared filename->hash map. A nullwall/arbitraryitems cannot qualify.

## Parent audit schema and chronology
AUDITBYTES must be canonical compact sortedJSON plus one LF, not merely parseable JSON. Exactkeys
format,item,plan_sha256,verdict,settled,exit_code,declared_output_sha256,receipt_sha256,auditor,at,notes.
formatext-search-job-audit-v1; AUDITED_PASS; settled=trueBOOLEAN; exactplannedexitINTEGER; exact declared names and
actual outputhashes. receipt_sha256 MUST be lowercase64hex; auditor/at nonempty strings, notes string. Parent
SEPARATELY binds that digest to the actual settled supervisor receipt and /bin/date provenance; syntax is not proof.
No child writes audit files. Each20job needs new exactGO and post-exitparentaudit before nextGO, all previousgates
included. Parent audits G-CONTROLS before considering either separate calibration. No autochain/poll/retry.

## Publication clocks and one-line evidence
Pre/post serialization, filecreate/write/close and stdoutwrite/flush checkpoints. Shared algorithmbudget starts
beforevalidation/setup. A late final completion returns5 regardless of earlier expected status. Serialized success
may already exist on disk/stdout: preserve it IMMUTABLY and reject by nonexpectedexit/parentendpoint audit; do not
rewrite or append another line. Earlyunpublished errors may publish one structured error record, never an absence.
Wrapper may emit diagnostic92/93/95/96 BEFORE entering algorithm. AFTERmainentry escaping exception or invalidstatus
fails QUIETLY94: no wrapper secondline, because it cannot know if algorithm stdout partially/finally published.
Joint publication also fails quietly after stdout started; pre-stdout errors may emit one non-success record while
retaining any file alreadycreated (mismatch blocks audit). Separate supervisor deadline still handles blocking IO.

## Authority
The operative authority is parentcorrection fabe57ab. e441d858 is HISTORICAL AND WITHDRAWN, supplies NO launch
permission. The old integrationv1 description is superseded by integrationv2 and this contract; oldplanv1/v2 are
historical unexecuted records, not operativeinvocations. All7gate --plan literal arguments name finalplanv3.
Mandatory owned bounded /bin/date helper, complete conservativeownership/census, protected admission/deadline/
resource/stream/settlement and exactpublication charging remain SUPERVISOR duties. Singleprocessscience children do
not waive them. Source20controls and2calibrations stillneed independent source/runtimequalification and exactGO.
No scientific status changes: LemmaU scopedaccepted exactanchor, both extension questions UNKNOWN, sixMOLS39 OPEN.
