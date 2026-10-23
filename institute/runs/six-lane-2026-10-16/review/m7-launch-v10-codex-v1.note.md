**DISPOSITION: HOLD.**

All 16 SHA-256 hashes and byte counts match. This review used static snapshot reads and hashes; no reviewed code or tests were executed.

The following findings block GO:

1. **BLOCKER — monitor freshness can expire before launch.** [SOURCE02:745–764](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/m7-launch-v10-review-v1/snapshot/02-launch_B_v10.py:745) evaluates stability **before** the final census, then reuses `stab["ok"]`. A successful helper can take 45 seconds without reaching its 60-second limit. A monitor that dies immediately after evaluation can therefore be stale at spawn. The final guard checks only free ≥ 12,201,048,576 B, deadline, signals and quarantine.

   **Repair:** evaluate the bounded monitor tail after the final census and revalidate sample age at the final launch guard. Refuse stale, ended or newly disqualifying monitor evidence.

2. **MAJOR — census revalidation and unknown-identity refusal remain incomplete.** [SOURCE02:461–478](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/m7-launch-v10-review-v1/snapshot/02-launch_B_v10.py:461) sets `same = a is None or …`: absence from snapshot A counts as consistency. A process born after A can consequently pass without the claimed bracketing identity/topology validation.

   Zombies bypass resolution checks, and other-UID non-native processes need not have resolved argv. At SOURCE02:510–511, missing argv falls back to `comm`; an unresolved Python process can therefore evade the B/C411 veto. Searching untruncated **available** argv fixes truncation, but does not fix this unknown case.

   **Repair:** require the necessary A/B/C identity agreement; retry/refuse missing observations. Preserve slot/reaping identity separately from RSS eligibility, and refuse unresolved slot identity regardless of UID or zombie status.

3. **MAJOR — helper-output validation still has fail-open paths.** [SOURCE02:271–273](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/m7-launch-v10-review-v1/snapshot/02-launch_B_v10.py:271) does not capture reader-thread exceptions. SOURCE02:352–363 treats a terminated reader as finished, so a reader failure can leave partial output while helper `ok` remains true.

   Row validation also accepts malformed evidence: SOURCE02:401–417 accepts `p42\nnunknown\n` without an `fcwd` record or an absolute cwd. SOURCE02:468 then considers that cwd resolved, permitting foreign classification. The ps parser also accepts negative RSS at SOURCE02:372–379.

   **Repair:** record reader exceptions and successful EOF explicitly; require both streams to complete successfully. Validate complete cwd records and reject unresolved names and invalid numeric ranges.

4. **MAJOR — the previously requested admission serialization is still absent.** SOURCE12:9 requested serialization of cooperating admissions; [SOURCE02:43–45](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/m7-launch-v10-review-v1/snapshot/02-launch_B_v10.py:43) explicitly leaves it unimplemented. Two desks can census the same capacity and both spawn. Fresh individual scans do not prevent that race.

   **Repair:** use a shared admission lock/reservation protocol covering final census through publication of the new reservation, or enforce a single-admitter invariant. The packet supplies neither.

5. **MAJOR — requested Bcuts provenance comparisons are not independently established by this snapshot.** SOURCE06:126–139 supplies pins, and SOURCE06:315–342 implements producer-field comparisons. However, the pinned producer receipt itself is absent. The original producer composition/append implementations referenced by SOURCE07:18–22 are also absent.

   **Repair:** include the hash-pinned producer receipt and relevant producer/module sources for static comparison. The visible comparisons and assertions are useful safeguards, but do not establish that the absent receipt contains the claimed fields and values.

The following repairs/checks **are established**:

| Check | Result and source |
|---|---|
| Helper rc/stderr handling | Both ps snapshots, argv ps and lsof require helper success; rc must be zero and stderr empty. SOURCE02:361–363, 425–440. Reader/schema gaps remain above. |
| Full-argv matching | Cap and B/C411 matching precede receipt truncation. SOURCE02:487–519. |
| Preparation and final guards | Output opens before censuses; hashes/receipt body precede the final census; free/deadline/signals/quarantine are rechecked afterward. SOURCE02:727, 743–764. |
| End-by deadline | `10200 + 180 = 10,380` seconds is included in `deadline_ok()`, giving a latest nominal launch of 15:04 PDT. SOURCE02:124–163. |
| Helper bounds and isolation | Own session; TERM after 60 seconds; bounded 30-second wait followed by blocking reap; no SIGKILL. SOURCE02:132, 301–363. The visible launch/replay path puts neither ps nor lsof inside a supervised target group: SOURCE02:425, 750, 809; SOURCE06:422–425; SOURCE15:66–139, 337. |
| Tagged regen binding | Assembly refuses before writing when the selected regen hash differs from the gate binding. SOURCE03:491–497. |
| Stability arithmetic/parser | The requested last-free threshold, drop formula, bounded window, timezone awareness, strict chronology, age bounds, count and span are implemented correctly **at evaluation time**. SOURCE02:622–654. |
| Item-5 generalization | SOURCE04 changes naming, optional history, deviations and reporting; it changes no acceptance condition, feed or parser. SOURCE03:201–231 retains the acceptance calculation. |
| Bcuts construction/precheck | Visible composition uses pinned functions and asserts input, block/count and output pins. SOURCE07:109–145. Regen prerequisites and regenerated-output hash refusal are present: SOURCE02:698–707; SOURCE08:85–107, 311–318. |
| Replay predicate/transport | Exact singleton status lists after CR removal, complete measured feeds, pipe-fed CNFs and FIFO proof transport remain intact. SOURCE06:551–625, 650–707; SOURCE08:335–346. SOURCE05 leaves these bodies unchanged. |

No additional executable change outside the identified repair, selftest, assembler-generalization and Bcuts hunks was found. The supplied historical baselines do not independently establish the entire v1–v8 lineage.

SOURCE14’s `all_ok` receipt matches the reviewed launcher/library hashes and supports nominal helper behavior. Its checks do not cover the failure cases above.