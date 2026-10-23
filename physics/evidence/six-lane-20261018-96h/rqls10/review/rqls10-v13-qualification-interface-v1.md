# V13 qualification-only original-creation identity interface (REVIEW ONLY)

Recorded 2026-10-19T09:39:16-0700 after /bin/date. Source immutable:
code/owned_supervisor_v13.py `26c9e27406e467b25032e7097c5e7cf81129cdc9c164a5c6db1874f6a6b11312`.
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
Fixed QROOT=<lane>/qual-pkg-v8-v13. New child code/guard_qual_child_v10.py; writer code/guard_qual_configs_v9.py;
checker code/guard_qual_check_v9.py. Existing files frozen, NEVER edited. Writer's pure config_for must accept the
prepared creation_channel as an explicit argument and must generate `{}` for all non-mutation modes. Writer can hash
current fixed child/writer/checker paths at authorized preparation time; external parent approval provides trust.
No static circular source hash and no fabricated fallback. Child/writer artifacts are source-only, no execution.
