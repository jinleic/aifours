# Qualification package v5, bound to the narrowed supervisor v10 contract

Recorded 2026-10-19T08:14:34-0700 after reading /bin/date. Author ContinueRQLS10b. WRITTEN ONLY; no invocation is
requested, authorized or executed by this plan. The v9-bound drafts named package v5 were snapshot-cited and have been
frozen unchanged; this v10-bound package uses NEW source filenames to preserve those snapshots. No earlier file changes.

## Binding scope and prerequisites
Parent decision RUN/review/rqls10-supervisor-v10-scope-parent-decision-v1.json,
`e441d8585228c2976700cba2c3397acfa1e544bc3dfe7af919205581572af22b`: separately reviewed SINGLE-PROCESS children
only; no fork/exec/subprocess/multiprocessing; native threads permitted. The supervisor writes no human-readable
timestamps and starts no helper. All parent GO/approval/audit/release timestamps require the parent to read /bin/date.
Unlinked same-uid processes are not owned. An observed extra owned identity is a contract violation and retains the
parent block until verified ended. A fast violating fork+setsid+intermediate exit can evade sampling; source review is
the mitigation. This package removes, rather than claims to qualify, the old fork/zombie/escape/busy2 controls.

Prerequisites before ANY control: parent source acceptance of the supervisor, acceptance of this exact package, then an
exact per-invocation GO with current reservations. Global HOLD is not disposed by these files. Known source caveat
reported to the parent: v10 full_census can discard an incomplete retry before its caller applies RSS/BUSY checks. Any
source correction requires new pins and package rebinding before use. The package is not asserted executable-ready.
The real-or-effective-UID rule is fail-closed: unreadable same-real/different-effective-uid metadata can refuse
admission on this host (read-only inspection found persistent login processes of that kind). No exclusion is assumed.

## Frozen sources
- Supervisor: `code/owned_supervisor_v10.py`
  `fc6ef48a041d82d8253f158c996626f62776965f8947eb80c322a71a07620a9d`.
- Single-process test child: `code/guard_qual_child_v7.py`
  `80e61ed42145e797fbc9bacb5ba120e75af54dd87c8873a503f925e77eb1329f`.
- Metadata-only layout/config writer: `code/guard_qual_configs_v6.py`
  `518da794a2d1ed80b2154adbcfa048d6fd14134b7b84040750cf51eef0ffccdd`.
- Artifact checker: `code/guard_qual_check_v6.py`
  `1f25278064227792610f09824c2c423410c5dfb8e9147b6e61e56c34201cc88e`.
- Unchanged parent dependency references: lane `code/stability_gate_v2.py`
  `1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a`; parent observer source
  `RUN/control/resource_observer_v3.py`,
  `fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196`.
  Their execution envelopes remain parent-owned and require their existing approval to apply to the particular
  invocation. v10 does not supervise these dependencies or infer permission from their filenames. The stability gate
  reads the parent's currently pinned observer stream and writes ONE exclusive RUN/stability.json, with projected
  20971520 bytes. No separate monitor or helper is launched by the qualification child/checker.

Use the actual framework interpreter `.../Resources/Python.app/Contents/MacOS/Python`, with real path and digest pinned
by the parent, NOT the Homebrew bin/python3.14 launcher. Read-only binary inspection found that launcher calls
posix_spawn/re-execs Python.app, violating the reviewed no-exec startup assumption and changing idversion.

## Fixed confinement and preparation
QROOT = `<lane>/qual-pkg-v5-v10`. Writer v6 reaches it through retained no-follow directory descriptors under the lane,
creates it once and binds it with package-root.json. Existing scenario RUN = QROOT/SCENARIO is refused; no arbitrary
BASE_DIR is accepted. Arguments, source pins, actual interpreter and nonnegative current reservations are checked
before any creation. Writer invocation, only if the parent authorizes metadata preparation:

`PYTHON_APP -I -B code/guard_qual_configs_v6.py SCENARIO PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES`

It creates RUN/config.json, RUN/preparation.json, RUN/out/, RUN/tmp/, and mutate_pin's new RUN/pinned-scratch.txt only.
Supervisor evidence and child outputs lie in RUN/out. Parent GO, stability, authorization, stdout capture, exit evidence,
checker result, process census, late audit and release records lie in RUN OUTSIDE out/. Every write is exclusive.
The child accepts no user-selected output or mutation target: mutate_pin is exactly its own scenario fixture;
mutate_evidence is exactly its own launch.json. Target open has no create, uses O_NOFOLLOW, checks regular-file type,
link count one and bounded size; pin bytes must match the fixture. Append is exactly b'x'. No prior-run evidence changes.

## Per-invocation authority and five-part parent release transaction
No broad GO file, automatic chain, receipt-existence release or checker-only release is allowed.

1. **Allocate, prepare, authorize.** The parent serializes the allocation of 20971520 bytes and ONE CPU slot for the
   single-process child; the global lane busy ceiling remains2. The busy control uses trip threshold0, not two child
   processes; its reservation stays one slot. Hold the allocation throughout preparation, execution, live child
   aftermath and final disposition. After preparation and a fresh stability gate, the parent writes RUN/go.json
   exclusively, with its /bin/date timestamp, decision GO, exact item string from the writer, raw not_after_epoch,
   stability_receipt_sha256, and configs mapping exactly the printed config digest to the printed GO entry. For
   go_unlisted only, configs is deliberately `{}`. not_after_epoch must cover the intended launch/GO/acknowledgment
   commits; it is parent-computed, not guessed by the supervisor or extrapolated from formatted dates.
   Parent also writes RUN/parent-authorization.json exclusively and retains its digest externally. Required schema:
   kind=`v10-qualification-invocation-v1`, scenario, config_sha256, go_sha256, stability_receipt_sha256,
   preparation_sha256, sources={supervisor,child,writer,checker} each {path,sha256}, python={path,sha256}, and
   allocation={bytes:20971520,cpu_slots:1,outstanding_reservations_bytes,lane_outstanding_reservations_bytes}.
   This approval is NOT a self-authenticating receipt: its trusted digest is supplied by the parent to the checker.
2. **Invoke and join publication evidence.** Exact admitted command:
   `PYTHON_APP -I -B code/owned_supervisor_v10.py RUN/config.json`, cwd lane, tool timeout0, no subprocess/tool timeout,
   no SIGKILL/ulimit/deletion. Parent records the ACTUAL tool exit code and stores the single stdout JSON summary
   exclusively as RUN/supervisor-summary.txt. Independently re-read and hash receipt, settlement and .staged, verify
   same-inode link and capture post_publish_mono. Exit must agree with the captured summary. ACK refusal or source
   uncertainty blocks ordinary release; expected negative controls require the separate explicit parent disposition.
3. **Check artifacts.** `PYTHON_APP -I -B code/guard_qual_check_v6.py SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT` writes
   RUN/check.json exclusively. It hashes all actual sources/config/GO/stability/preparation/evidence files; reconstructs
   the scenario config; checks exact outcomes, full identity, per-root manifests, complete sample bytes/counts/digests,
   raw commit order/expiry, closed streams, all-predicate clearance and exact publication/reservation arithmetic.
   Samples use a strict sequence-of-JSON-values decoder: v10 pretty-serializes samples despite the inherited .jsonl
   filename. All bytes must be consumed; partial records, duplicate keys, overflow literals and malformed schemas fail.
4. **Verify ended owned identities.** Independent parent read-only census must establish that the exact child identity
   and EVERY recorded owned identity/contract violation is ended, using pid+uniqueid/version, not PID absence alone.
   No test process is terminated speculatively. ignore and identity may remain live until their own 60s module-entry
   lifetime deadline; before then retain the reservation and block the next GO. Any unexpected process, changed
   identity, unaccounted descendant or actual contract violation HOLDs the sequence for explicit disposition. The
   single-process source contract is a premise; no universal undetected-descendant guarantee is claimed.
5. **Late artifact audit and independent disposition.** Parent audits the entire RUN (not just out/), hashes every new
   artifact, and verifies that ignore/identity's only allowed late child-out.json names the original child/scenario,
   was born after the supervisor decision and has expected content. Earlier files must retain their frozen digests.
   Parent writes a NEW exclusive disposition binding allocation/approval, actual exit, captured summary, all verified
   digests, checker output, ended-identity census and late audit. ONLY that independently verified record authorizes
   release and a next GO. UNSETTLED receipts stay immutable; later self-exit never turns them into SETTLED or science
   success. File existence, shell rc, summary acknowledgment and checker PASS alone never advance the sequence.

## Exact proposed controls (all unrun)
Order: go_unlisted, ok, rc_nonzero, missing_output, mutate_pin, mutate_evidence, stray_file, deadline, flood, busy,
rss, ignore, identity. settle_s20, sample_s1; each is individually authorized. Child lifetime is60s from test module
entry except deadline120s; startup prior to module entry is covered by the independent supervisor deadline, not an
untrue child process-start guarantee. GO input is nonblocking with an absolute logical deadline; flood writes are
nonblocking. Source has no fork/exec/subprocess call. Nominal timings are not native-call wall-time guarantees.

| Control | Frozen intended outcome | Required intended evidence |
|---|---|---|
| go_unlisted | receipt NOT_LAUNCHED, child rc null, loop NOT_STARTED, no failure/trip; admission reason GO_DOES_NOT_NAME_THIS_CONFIG only; actual exit14 and unsuccessful ACK_REFUSED summary (ack revalidation also refuses the unlisted config) | published receipt/settlement digests joined to actual exit; no child/launch/sample/output; explicit parent negative-control disposition required |
| ok | SETTLED, exit0, child rc0, loop EXITED, no failure/trip/signal | child output identity; stdout exactly line1/line2/line3; complete empty-owned clearance |
| rc_nonzero | SETTLED, exit0, child rc3, loop EXITED, no failure/trip/signal | child output identity, empty stdout; process settlement is not computation success |
| missing_output | UNSETTLED, exit11, child rc0, EXITED, exactly REQUIRED_OUTPUT_MISSING | confirmed absent output, exact stdout; stop FAILURE with explicit CHILD_ALREADY_REAPED/no signal |
| mutate_pin | UNSETTLED, exit11, rc0, EXITED, exactly PIN_CHANGED_OR_UNREADABLE | fixture exactly original bytes+b'x', same single-link inode as child reports |
| mutate_evidence | UNSETTLED, exit11, rc0, EXITED, exactly EVIDENCE_MUTATED | hash launch bytes minus final b'x' equals original published digest; same inode/size reported by child |
| stray_file | UNSETTLED, exit11, rc0, EXITED, exactly UNDECLARED_ENTRIES | exact extra name and content; bytes charged to the run |
| deadline | SETTLED, exit0, child rc-15, EXITED, exactly one DEADLINE trip, no failure | trip not before mono_spawn+max_wall10; one identity-checked group SIGTERM; clear before grace |
| flood | SETTLED, exit0, child rc-15, EXITED, exactly one STREAM_CAP trip, no failure | stdout seen>cap, retained bytes=file size=1048576, matching digest and triggering sample |
| busy | SETTLED, exit0, child rc-15, EXITED, exactly one BUSY trip, no failure | ONE reported spinning child PID is in sampled/trip busy PID sets; count1 or2 > TEST threshold0; sampled global ceiling2 unchanged |
| rss | SETTLED, exit0, child rc-15, EXITED, exactly one RSS trip, no failure | reported allocating child PID, 320MiB touched, sampled RSS matching trip detail above256MiB |
| ignore | UNSETTLED, exit11, child rc null, GRACE_EXPIRED_AFTER_STOP_REQUEST; exactly GRACE_EXPIRED_AFTER_STOP_REQUEST, CHILD_NOT_REAPED, OWNED_LIVE, STREAMS_OR_THREADS_NOT_CLOSED; exactly DEADLINE trip | identity-checked SIGTERM sent but ignored; final owned identity exactly child; late output and self-exit independently audited |
| identity | as ignore plus exactly IDENTITY_UNVERIFIED, same DEADLINE trip | injected identity refusal, explicit unsent signal; does not exercise real metadata failure/PID reuse |

Every launched case needs a complete exact source/input/identity/manifest chain, nonempty fully decoded samples with
within-floor disk/output values, sampled lane_busy<=2, reconciled extrema, no hidden cancel/lost wait, exact pin results,
and the intended no-extra-process registry. Signalled SETTLED controls additionally require signal and trip to
post_publish_mono intervals<=7s. Missing or extra failures/trips, a prerequisite/resource/census anomaly, unexpected
late artifact or malformed field FAILs the individual control, not accepted as its intended effect.

## Explicitly not exercised or certified
No helper paths (N/A by decision), fork/zombie/escape workload (not an authorized single-process child), universal
sampling coverage, real UID/effective-UID transition, real identity failure/PID reuse, disappearing PID/exec races,
clearance immediately around every cutoff, native-I/O overrun, protected commit cancellation races, GO expiry/reuse,
FREE/OUTPUT/lane-ceiling boundary, insufficient publication budget, root replacement/mount/retype, source capture or
fsync/readback failure. Those remain source-review/parent-audit obligations or need separate exact GOs. Native-call
latency is unbounded by Python; fail-closed late-return detection is the source contract. No scientific target is
advanced by any of these controls; unrestricted fixed-B remains the active science route after guard qualification.
