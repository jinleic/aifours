# Lemma U certificate package v5 — exact review disposition (2026-10-19T08:43:22-0700)

Review: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-certificate-v4-source-codex-v1.prompt.stdout.txt, SHA25640fcc2edee624615e3124f9244894d3b08b44ecf4a177d6211a2fd5eb3a50cbc, HOLD.
ONE final v5 successor package. All prior sources, staging files and reports preserved unchanged. No source executed,
compiled or syntax/AST parsed, no controls/configs/science launches. GLOBAL HOLD and exact parent per-job GO remain.
Beta-route slice remains PAUSED; no integration, estimation or search resumed.

## Frozen final source table
|role|absolute path|sha256|
|---|---|---|
|producer|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_producer.py|732ea93983058f743086208cbfbec58680b2eb545ac4853b1706460d3a76c346|
|checker I/O successor|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v3.py|ed93f236c342925eded12b299b52cfb5f6fb5b7835d30833cb8ff0b22b759dcb|
|mutants|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_mutants.py|a62622c69c5af782d09aa6f175021246f79f1764b789f93e7629dddf2670a3ed|
|expectations|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_expectations.py|ba5f502cddf1215e689d0dbda013ed18ebcebaaef95fb142d230bb30b8e9ff46|
|checker GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_entry_checker.py|811090ca44ccf35d753e96af5749b6eca924cb42f25a1de564f5895801250598|
|expectations GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_entry_expectations.py|11e40d15177b304d38da98e35ae60708395a8c208d3bc05fda2af5aa342d0737|
|generator GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_entry_mutants.py|19d2af9104a47cb52f28d38b2968fa17ea982be1f8b029f65357426304378936|
|producer GO entry|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/cert_v5_entry_producer.py|a8537ddcab7bad0b96627f57e3cf4af5241c09d6599fc88f3a9424f9bceb633d|
|checker I/O contract|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v3-io-contract-v1.md|4f11fbf058a48f0cd8cd7d5be1c690345bed9116b1efe0f996801d402128768d|
|contract overlay|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-v5-contract-overlay-v1.md|7d4d794145dbd3c9de0258e33cf1c3e6614a38f1c1e5b50fdef61a3d17d1a437|
|run plan|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-run-plan-v5.json|de1cef872d0bf97677bf40efe50fec98f850f6490a85c45aa89be6ed40efe458|

## Remaining MAJOR — every runtime file consumer is now bounded at the descriptor
Named sites repaired:
1. Expectations read_entry: os.open(name,O_RDONLY|O_NONBLOCK|O_NOFOLLOW,dir_fd=retained_job_or_audit_fd).
   Existing anchored directory walk, plain-name checks, regular fstat, nlink==1 and output-set/hash binding stay
   intact. Read requests min(65536,cap+1-total). Actual bytes consumed never exceed cap+1: at cap it requests1 byte;
   overflow is rejected before retaining that byte in joined buffers. A FIFO with no writer cannot stall at open and
   is rejected by fstat without reading. Artifact/audit failure stays Problem/deviation, never AS_EXPECTED.
2. Every cert_v5_entry_*::_load: algorithm source open O_NONBLOCK|O_NOFOLLOW, descriptor regular fstat, actual
   cap+1 read loop (1MiB cap,64KiB max block), protected read/close handling. A FIFO/path replacement cannot block
   before type validation. Read/nonregular/overflow/compile/exec failures stay ENTRY_ALGORITHM_LOAD_ERROR95;
   actual hash mismatch remains96. The EXACT returned bytes are hashed then compiled; no pathname reopen.
3. Producer and generator informational source hashes: NO __file__ open/read at all. The wrapper injects
   VERIFIED_SOURCE_SHA256 from its already-read, pin-verified source bytes before executing the module. main reads
   that value from globals; it remains informational only. No unbudgeted informational reader exists before Budget.
4. Other readers already repaired and preserved: checker read_capped_input; producer/generator read_regular_capped;
   expectation read_pinned used for plan/input/source/documentary pins and independent nc6 raw. All use descriptor
   NONBLOCK/NOFOLLOW, regular fstat and actual cap+1 consumption. Checker additionally ticks before/after reads.
Directory O_DIRECTORY walks and stat metadata are not data readers. GO pipe has separately bounded3byte+probe policy.
No filesystem snapshot copies, new child outputs, dependencies, subprocesses or helper processes are introduced.
Error taxonomy and parent audit requirements unchanged. Slow regular-file I/O still needs supervisor wall enforcement.

## Remaining MINOR — final stdout completion included in self-budget
All four final roles now check deadline AFTER print(line,flush=True) has completed:
- Producer/generator/expectations: budget.tick after flush, late => return5 (also when an earlier failure status was
  emitted). No expected success/control exit is returned after an observed overrun.
- Checker finish: shared deadline after flush, late => ERROR2 even if emitted scientific verdict was INVALID1.
Already emitted file/stdout bytes are IMMUTABLE: no rewriting, no second line, no forged updated wall_s. A late
retained/report line may still look OK/VALID/INVALID with a pre-flush wall_s. That line alone NEVER qualifies the job;
parent independently audits exact final exit/completion telemetry and rejects5/ERROR2 or any other nonexpected exit.
This preserves the one-line protocol and intended-control/error distinction. A failed stdout operation already
returns non-success; late normal completion is now checked explicitly.
Pre/post retained-file and individual mutant/manifest publication checks fromv4 remain unchanged.

## Previously fixed findings remain fixed
- nc6 is still reconstructed independently from actual pinned raw, all fibres and coefficient points. Selection is
  first eligible source failure then smallest passing fibre, compared only afterward to manifest. No helper import.
- Literal exact-anchor claim includes raw anchor hash, actual cert artifact hash, dimension/rank and two signs;
  final qualification/exit0 requires true, and earlier phases say UNEVALUATED.
- Complete audited prefix includes prior EXP results and every actual artifact. Strict typed schemas and canonical
  producer/mutant bytes; immutable source pins verified. No manifest paths trusted.
- Each21 job needs its own exact GO and intervening parent audit. CHK-anchor admission must cite completed
  AUDITED_PASS EXP-D audit by path+sha. Nothing autochains or polls.
- Real output roots retain no-follow walk, ownership/mode checks, fchdir and exclusive fixed plain outputs.
- G1 grammar and nc0..10 intended rejections unchanged. nc9 raw/provenance bytes still embedded inplanv5; direct
  columns0 and18 duplicate difference38 for rows0,1, independently visible from bytes.

## Mathematical independence and exact source preservation
Original independent checker e7e84962... -> I/O-only v5 checker ed93f236c342925eded12b299b52cfb5f6fb5b7835d30833cb8ff0b22b759dcb.
Scientific block FORMAT_TAG through compute_facts EXACT17,671 bytes,
SHA256b2b8719207d7375189b982feacf0b8409220db14dab39d2da575f036009d9e56 in both. Source-byte comparison only, not a
checker run. No rank/basis/rainbow/coverage/parser/rejection-string modification and no producer import.

## Runtime inventory / supervisor authority
Planv5 inventories19 paths/digests. All source/entrypoint pins now name finalv5, checker I/O document is updated,
formatv2+newv5overlay+nestednc9provenance+originalspec/erratum/format remain pinned. Added governing correction
/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-supervisor-v10-scope-parent-correction-v1.json, SHA256fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2.
All entries are actually hashed by expectations; missing mandatory source/format/provenance pins fail closed.
Review-only disposition map is not claimed runtime-consumed, and plan self-hash is checked by invocation.
The old e441d858 decision grants NO authority. Governing fabe57ab correction retains owned bounded /bin/date helper
and conservative known ownership/unresolved-census obligations. Nonforking science children DO NOT waive those.
Supervisor still unqualified; total startup/load/GO + compute + file/stdout completion must fit independent wall
admission. Child120s GO allowance +240s algorithm is NOT asserted to be300s whole job.

## Scope and state
Certificate route UNEXECUTED/UNQUALIFIED, no launch permission. LemmaU existing computer-assisted exact-anchor scoped
acceptance unchanged. Corrected R1 accepted as equivalence, both extension problems UNKNOWN. SixMOLS39/CFR6,39 OPEN.
No candidate, no novelty/priority/non-anchor claim. Beta remains paused, all old evidence preserved.
