# Beta source package successor2 — combined owner-review disposition (2026-10-19T09:35:53-0700)

ONE source successor, no search-method change. All prior artifacts and intermediate snapshots preserved unchanged.
Answers BOTH full reports:
- mathematics_algorithms_data ec551589b35908b332b9233cf4d50a06b8c619d9a7155ded2139871d51714ee8,
  RUN/review/mols39-beta-mathematics_algorithms_data-codex-v1.prompt.stdout.txt (MAJOR operationbound, MINORstorage);
- admission_gate4845407690318279d09b2ee2d5f0d288b36b910bd5280c6f92acaf89f267fd94,
  RUN/review/mols39-beta-admission_gate-codex-v1.prompt.stdout.txt (1FATAL,4MAJOR,2MINOR).
No execution/imports/compilation/AST/syntax/tests/controls/calibration/search/configs/review-CLI launch by worker.
All repairs below are SOURCE dispositions, not exercised verification. Existing mathematicaltarget status unchanged.

## Final frozen source table
|role|absolute path|sha256|
|---|---|---|
|beta algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_beta_final.py|88281d5dddfd088db19c91b7795c36320b80f9fd4b4322ffac7c80d512d33ccb|
|beta entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_beta_final.py|61c3e65f2e98f93e496f5f8c3eeb62664b9a0fd0d068cc53b433036ba7c83881|
|joint algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/ext_search_joint/ext_search_joint_io_v4.py|dad8a3a41b29b1e4f6de87bdfe964a079884f339aedb37fc2f205128b7e0dc1e|
|joint entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_joint_final.py|db4e243a9c3b89cdb025f50cbd8f66b70f983d5455fd11003c5bf6df6ddb7d9d|
|data algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_controls_final.py|19a79b56ee1a7e74e4822cedceb708fbf9d11bbae78bfded937f7cae9ed04e11|
|data entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_data_final.py|4558fdf11781f861fb9be1ae9d3f7fb73e1fb9bc6696297ea684a15d807ba4cf|
|gate algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_gate_final.py|68d6911396c032df35cd2c4b8d8644a07454631a64ee28265e0cdc604b6268c4|
|gate entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_gate_final.py|c94ef756bac7dd5f51e04ba007b4c7688833ec3bc47a601c50c6c15c28900cf2|
|complete schema/root contract|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-contract-v1.md|3fc37627e3d48ffc73f116ed0456b3caa8099e6b073d7de15d7d361e86066038|
|fully rederived resources|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-resources-v1.md|034a9dc19efd3d530314c5e8f7b9cc4a4e4da15b3bde58b80c71a2e0f112ee94|
|operative integrationv2|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-integration-v2.md|e498ec7bf0700df987b3525495fa63c446e5af1ff3a4db1558cdd3ee0ebe24e0|
|final repinnedplanv3|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v3.json|4032c6829fb42617f936fb34a52c75d3aa4462e8143456eb467129d59d704c7a|
|actual metadataverification|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-metadata-v1.json|0266f1d18479eb22d8f6d5e92657a578a09fe2322d75228b84787b53166bffbe|

Metadata verification: finalplan18unique actual64hex pins;4actual algorithm+entrypoint hashes and wrapperliteral
ALGO_PATH/ALGO_SHA256;7literal gate --plan paths ALL final ext-search-plan-v3.json, no v1/v2 operativecallsite.
New I/O guards affect all source/raw/pin actual readers, not only wrappers. All20controljob names/domains and2future
calibration parameters retained, outputroot/codeidentity changed. No automatic fulltarget work allocation.

## Admission FATAL F1 — undefined artifact cap
Gate readat(dirfd,name,cap=CAP) has an explicit local cap, default16MiB. Overflow checks and read requests use THAT
same parameter. Audit calls explicitly cap1MiB. No undefined lowercase variable remains in the reader.
This is a source repair, no actual successful read/control run has occurred.

## Admission MAJOR M1 — FIFO beforefstat
Artifact/audit leaf open is O_RDONLY|O_NONBLOCK|O_NOFOLLOW relative to retainedjob/auditfd, BEFORE fstat. It verifies
regular,nlink1,size then reads actual cap+1 bytes in<=64KiB blocks, rejects growth and rechecks linkcount. No blocking
FIFO open before typecheck. Existing dirfd/name/hash/one-link barriers retained.

## Admission MAJOR M2 — full pathname/link policy for every actual consumer
Same anchored_parent/anchored_file_fd/anchored_read_bytes implementation duplicated in each algorithm/wrapper (no
cross-import into independent jointmath). Absolute normalized parents walked componentwise from'/' with
O_DIRECTORY|O_NOFOLLOW. Leaf NONBLOCK|NOFOLLOW relative to retainedparentfd, regular andnlink1,sizecap enforced on
ACTUAL descriptor, not a followed-path stat(). Cap+1 accumulated bytes, same bytes hashed/parsed.
Applies to source loader, beta/joint raw reads, DATA pinnedDM21, gate plan/pin/control inputs, artifact/audits.
Wrapper input preflight reads ZERO rawbytes: opens/type/link/cap-checks/closes only. Algorithms perform their own
single actual rawbyte read through the same parent/link policy; no secondbyte-read or preflight-only assurance.
Errors preserve entry/read/IO/deviation classes, cannot masquerade as intended NOT_DM orPIN_MISMATCH site.
Pinned source digest injected from exact bounded source bytes, no informational self-reopen. No new snapshot files.

## Admission MAJOR M3 — complete typed result and priorgate schemas
17mandatory keys, noextras, strict canonicalJSON, allhash64hex, finite nonnegative FLOAT wall (notint/bool/null),
actualinput/solutionhash, exactprogram/status/reason. Per-program/status metadata now COMPLETE:
- beta INPUT_PIN_MISMATCH occurs before n/q/k/m/lo/hi/mode publication: ALLnull, chunks/solutions empty, extraempty.
- joint INPUT_PIN_MISMATCH occurs afterargs: n/q/k null, m0,lo0,hi1 exactints,mode search; payloadempty.
- both NOT_DM: n6,q2,k2,m0,lo0,hi1 exactints,mode search; chunks/solutions/extraempty, SHA256('[]').
- COMPLETE: metadataexactactualdomain; beta extraexacttwo nonnegativeintcounters, jointextraempty; bounded sorted
  unique intvectors, normalized+fixedchunk+allrowdifference directchecks; exact chunkkeys/order/counts/nodes schema.
No arbitrary malformed earlymetadata or fabricated COMPLETEchunk can pass intended-error branch.
Prior successfulgate wall is finite nonnegativefloat, prefix/self/hash/status/qualifiedfields exacttypes. Its items
must be EXACT the current gate's independently recomputed actualprefixrecords, in sameorder, with exact
item/problemlist/artifacthashdict shapes. Nullwall/arbitraryitems counterexample nowfails.

## Admission MAJOR M4 — audit canonicalbytes/receiptpin
Auditbytes use canonical(...,AKEYS), compactsortedJSON+oneLF, not only parse(). receipt_sha256 is lowercase64hex,
auditor/at nonemptystrings, notesstring. Exact typedexit/settled/plan/item/actualoutputmap stillmandatory.
Parent independently binds receipt pin to real settled supervisor evidence and owned /bin/date. A digest's syntax
alone never establishes settlement. Missing/malformed/nonauthentic evidence blocks parent's release.

## Admission MINOR m1 — one-line preservation after algorithmentry
Before main, wrapper may emit one entry diagnostic92/93/95/96. AFTER entering main, ANY escapingBaseException or
invalidreturnstatus uses QUIET os._exit(94). No unconditional _emit after algorithmstdout, so an interrupt after a
completed line cannot append a wrapper line. Jointpublisher similarly fails quietly once stdoutstarted. Parent
still rejects missing/partial/additionalstdout and nonexpectedexit; failure is never intendedcontrolpass.

## Admission MINOR m2 — stale authority/plan descriptions
integrationv2 explicitly withdraws integrationv1 operativee441d858 description, pins governingfabe57ab. Old files
remain historical, not operational. Newgate header says finalplanv3; all7literalcalls checked finalv3. Planv1/v2
superseded/unexecuted. Mandatory owned /bin/date helper and conservativeownership/census obligations remain
SUPERVISOR duties; nonforking sciencechildren do not waive them. Qualifiedsupervisor+exactGO perjob stillrequired.

## Publication requirement across every role
Pre/post serialization and each file/stdout completion checks. IndividualDATA outputfiles/manifest similarly
bracketed. Sharedbudget starts before input validation/setup. Late finalflush returns5; immutable emittedline/file
is never rewritten or supplemented. If deadlineexpires after a retainedwrite, source may emit one non-success
stdoutreport while preserving thatfile; parent audit rejects mismatch/nonexpectedexit, not status-onlyacceptance.
Independent supervisor wall guards blockingregularIO and fullstartup/loading/GO/compute/publication accounting.
120s GO allowance +240s selfbudget is NOT claimed tofit300s automatically. No new helpers/processes.

## Math MAJOR M1 — assigned item index AND update fully charged
Old B-nodeaggregate/tables WITHDRAWN as upperbounds. New resource proof counts I,U,C,A separately; each assigned
(column,row) charged an item-index/residue expression I AND demanddecrement U. It also charges demand/supply
initialization/min/any/final scans, candidateindices/checks/updates, explicitappends andcaller/state constants.
  I_B<=kn+kqr; U_B<=kn+kqr+2kq+5;
  C_B<=n+3kq+(k+1)qr+3r+15; A_B<=r(q+1).
  TOTAL_B<=2kn+(3k+2)qr+5kq+n+4r+20.
H work similarly separates up to6kn residueexpressions and12kn predicatecomparisons, variable/value/MRV tests and
state/callconstants: TOTAL_H<=18kn+7n+20. Both are exact declared logical-unit bounds, not CPUcycle/instruction or
seconds guarantees. Budget/interpreter/object/loop overhead separated explicitly. Perinputtable re-evaluated.
ReviewcornerP57,m56,r0: newB1540 exceeds source lowerbound1063 (oldformulafalse); no search/test run.
Accepted node bounds unchanged (betaN611711,N12229,P21694,P575074; jointN6326, planted5). No target runtimepromise.

## Math MINOR m1 — simultaneous stacks/parsedrows explicit
Old scalarS established-upper-bound claim RETIRED to a historical sizingsketch; false depth<=n premise withdrawn.
StageH runs inside fullBstack, so liveframes <=(r+1)B+(r+1)H, anchor39+39=78. Also mainretains parsedrows separately
from D/b/a: FOUR matrices,4kn referenceentries plus originalintegerobject sizes, row/outerlists andraw1MiB.
Resource document gives a transparent layout-dependent template with BOTH framefamilies, B/H/adjacency temporaries,
retained f-list/set/tuples/chunkrecords andserialization buffers, originalbigintvalues (not assumed7bits), allocator/
interpreter baseline. It makes NO exactportableRSS upperclaim. Joint packedbuffer source formula/nodework accepted
unchanged;256MiB/16MiB/100MB are admissioncaps, not measuredRSS/time. Everycase evaluated; no brute computation.

## Exact independence/source preservation
Beta Engine block exact 4887bytes SHA233bd15e3472b010c4f85078927202fc0fdfcc238c0b5fc909215f1b9b315b59 unchanged from reviewed7231f46d... source.
Independent joint search block exact 11171bytes SHA020100eebbd493a417e798354e5547e2777eaafd9dc6409d07841de39f7c60b7 unchanged from revieweda7734f4a.../originalauthor.
These are sourcebyte comparisons only. No pruning/chunk/CRT/estimate/controlmath edits. Integration owner changed
IO/schema/publication boundaries; independentjoint still imports no producer/helpercode.

## Scope/state
Source successor only, requires BOTH owner source re-reviews and independently qualified supervisor before runtime
controls. No20job launches, no2futurecalibrations, no deterministictargetallocation. No imports/tests/search/configs.
Existing exactanchor LemmaU computer-assisted scopedacceptance intact; correctedR1 equivalence accepted. Both
extension questions UNKNOWN andsixMOLS39/CFR6,39 OPEN. No new witness/nonexistence/novelty/priority/science result.
