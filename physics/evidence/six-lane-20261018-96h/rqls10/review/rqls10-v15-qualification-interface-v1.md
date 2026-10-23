# V15 qualification-only original-creation identity interface (REVIEW ONLY)

Recorded 2026-10-19T10:06:43-0700 after /bin/date. Source immutable:
code/owned_supervisor_v15.py `0a22bbc56a929bf674a579314ef0eeefd7f8e71ed5b3e39cb44db7921f5f34f9`.
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

## V15 terminal and accounting contract
V14's fixed creation, resource/cap/cleanup and publication interfaces are unchanged. Mutation negative GO
requires EXACT three keys and literal boolean true; numeric1 is refused. The sole v15 behavioral repair is after
main() has returned14 from its existing bounded cleanup/publication/diagnostic attempts: os._exit(14) prevents
CPython shutdown from re-flushing failed buffered standard streams and overriding actual14 with120. Other statuses
use normal sys.exit. This does not skip earlier cleanup or diagnostic attempts, prove missing evidence complete,
broaden allowed exit codes, or authorize parent reservation release.

Both positive ACK and ACK_REFUSED summaries expose actual publication_resources=b, ack_resources=end, and
publication_payload_bytes. Current reconciliation additionally exposes these fields, last_accounting_observation
={resources,mono_observed}, maxima and min_free. Each resources record is exactly {charged_bytes,lane_bytes,free};
mono_observed is raw monotonic telemetry, not a human timestamp or in-flight peak. Unreached stages retain nulls.
Precheck a and fresh values MUST NOT substitute for b/end. Positive ACK still requires exact readbacks/directory
fsync/post_publish_mono and separately captured actual exit. Incomplete post-ACK stdout/stderr or actual14 holds.

Completed resource measurements include raw successful identity_after. The complete composite/partial totals are
retained/enforced before fallible history charging, with a bounded completed_measurement in the overflow witness;
no resumed scan or cap acceptance. Validated initial main identity/group precedes retention. Helper signal records
preserve identity_observed/mono_identity_observed and, if sent, mono_sent.

Packagev8 uses fresh root <lane>/qual-pkg-v8-v15; its independent final manifest pins each actual child/writer/checker
source and this supervisor. Pure metadata preparation hashes those fixed final sources at its individually authorized
time; external exact parent approval is the trust root, not static circular source hashes.

The existing22 controls remain required but do NOT cover the extra finite matrix. In addition to all v13 obligations,
separately reviewed bounded fixtures must cover final-bracket/initial-main/helper-TERM cap paths and post-ACK stderr
write AND flush failures persisting through interpreter shutdown, with actualexit captured. Accounting fixtures must
observe all four stages: pre-payload; payload established but b not successfully returned; b returned but end not
successfully returned; end returned. Compare actual observations/artifacts, honest nulls, late-vs-completed records.
No host-clock mutation, synthetic value labelled actual /bin/date, execution or source/runtime acceptance occurs here.
