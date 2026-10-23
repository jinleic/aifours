# V14 qualification-only original-creation identity interface (REVIEW ONLY)

Recorded 2026-10-19T09:58:14-0700 after /bin/date. Source immutable:
code/owned_supervisor_v14.py `b42d646dad157d3c08dcf755931ff2a5b064ebb123ae09bdcf1381a0e3c9adeb`.
Binding correction fabe57ab retained; parent explicitly approved this small protocol design for review, NOT runtime.
Read source validate/authorization_io/creation_manifest/launch_and_go for the exact fixed schema.

## Ordinary/science/certificate consumers
New required config field `creation_channel` is `{}`. The GO config entry binds it alongside output_roots, argv,
max_wall_s,cpu_slots and three reservation fields. Bytes delivered are EXACTLY `GO\n` then EOF, no default extra line.
No science solver/numerical implementation is changed or admitted by this protocol.

## Only mutate_pin and mutate_evidence negatives
Config creation_channel exact keys:
- kind=`qualification-creation-v1`
- scenario=`mutate_pin` OR `mutate_evidence`
- preparation_path=RUN/preparation.json
- preparation_sha256=the exact preparation bytes
- target_path=RUN/pinned-scratch.txt for pin, or cfg.launch_record for evidence.
Purpose must be guard-qualification, one output root. No arbitrary target/command accepted.
GO additionally requires exact qualification_negative object:
`{"scenario":SCENARIO,"kind":"mutation","creation_channel":true}`.

Preparation top-level exact keys:
`kind,scenario,run,output_root,fixture,source_pins,python,allocation,negative_control`.
- kind=`qualification-creation-preparation-v1`; scenario exact; negative_control=true for these mutations.
- run={path:RUN,inode:[dev,ino]}; output_root={path:RUN/out,inode:[dev,ino]}.
- fixture=null for launch mutation. For pin: {path:RUN/pinned-scratch.txt,inode:[dev,ino],sha256:original,
  bytes:original,nlink:1} captured by fstat ON THE CREATED descriptor BEFORE its close, not a later pathname stat.
- source_pins exactly supervisor/child/writer/checker, each {path,sha256}; python={path,sha256} actual Python.app.
- allocation={bytes,cpu_slots,outstanding_reservations_bytes,lane_outstanding_reservations_bytes} exactly config.
Source validates pins' bounded metadata schema and actual supervisor pin, current allocation, interpreter path,
run/out anchor identity, original target identity/content/link count. Parent external approval must pin all actual
preparation/source/config bytes and semantically validate the whole preparation, not merely hash self-assertions.

Avoid config/preparation digest circularity: preparation contains creation facts/pins/allocation, NOT config_sha256 or
GO digest. Create it after fresh run/out/pin creation, then build config with its exact SHA. Parent approval joins both.

## Actual supervisor-to-child bytes
Only the declared mutation receives `GO\n` followed by ONE canonical compact JSON line <=4096 bytes, then EOF:
{kind:`qualification-creation-manifest-v1`,scenario,preparation_sha256,run,output_root,target}.
Run/out copied from verified preparation. Target={path,inode:[dev,ino],sha256,bytes,nlink:1}.
- Pin target matches approved CREATED fixture descriptor identity and original content BEFORE mutation.
- Launch target uses the supervisor's ORIGINAL publish-returned inode and digest, not later arbitrary pathname facts.
Source re-hashes target and refuses before GO on replacement. Child independently opens through retained no-follow
run/out descriptors and checks expected original inode+digest+size+one-link BEFORE appending. A renamed older
same-content file must be refused before mutation. Return exact received manifest SHA/inodes in child output.

Source retains rec.go_creation_manifest plus SHA256 of the exact JSON line INCLUDING newline. Preparation binding is
re-read in protected authorization_io after preparation I/O; both token+extra line+close share GO deadline/cancel/
expiry/age/remaining-runtime completion checks. No new wait, helper, command, implicit protocol or unbounded payload.
All evidence comparisons are written-only until the source/package reviews and individual itemGOs permit execution.

## Rebound package filenames / ownership for delegated authoring
Fixed QROOT=<lane>/qual-pkg-v8-v14. New child code/guard_qual_child_v10.py; writer code/guard_qual_configs_v9.py;
checker code/guard_qual_check_v9.py. Existing files frozen, NEVER edited. Writer's pure config_for must accept the
prepared creation_channel as an explicit argument and must generate `{}` for all non-mutation modes. Writer can hash
current fixed child/writer/checker paths at authorized preparation time; external parent approval provides trust.
No static circular source hash and no fabricated fallback. Child/writer artifacts are source-only, no execution.

## V14 minimal accounting and cap/cleanup additions
Mutation negative GO requires EXACT three keys and `creation_channel is True`; numeric 1 is refused.
Original-creation wire/preparation schema above is otherwise unchanged. Ordinary/science/certificate wire remains exact.

Both positive ACK and ACK_REFUSED summaries expose actual `publication_resources` (b), `ack_resources` (end), and
`publication_payload_bytes`. Missing actual records stay null; no fresh value or precheck a is substituted.
Current reconciliation additionally exposes those fields, `last_accounting_observation={resources,mono_observed}`,
`maxima` and `min_free`. Resources are exactly {charged_bytes,lane_bytes,free}; mono is raw monotonic telemetry,
not a human timestamp or peak claim. Positive ACK continues to bind actual publication readbacks, directory fsync,
post_publish_mono and actual exit. Refusal and missing/incomplete post-ACK stderr evidence never release reservations.

A completed resource measurement now includes full `identity_after` from the successful RAW final bracket. The
composite and partial counters are retained/enforced before fallible history charging. A cap halts scanning and
adds one bounded `completed_measurement` to the overflow witness; no overflow is a qualified success. Validated
initial main identity/group is installed before retention can request cleanup. Helper TERM updates its signal
record and preserves `identity_observed`, `mono_identity_observed`, and mono_sent where sent. Once an ACK attempt
begins, reporting failures cannot produce another stdout summary or change actual14 into13.

Existing22 controls are required but do NOT cover the extra finite review matrix. Packagev8 must separately enumerate
new cap/final-bracket, cap/initial-main, cap/helper-TERM, and post-ACK stderr-write/flush cases, with separately reviewed
bounded fixtures and exact individual negative GOs before any execution. No fixture or matrix case has been run.
