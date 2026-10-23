# PA19 staged revision 10 — parent containment and audit disposition

**REJECT for resumed production use.** Read-only reviewer task `PA19StagedAudit` found four major resource/admission defects and two stream/cap-policy defects. No false mathematical UNSAT result or actual CPU/RSS excursion was demonstrated by this source-only review. Full reviewer report: `agent://PA19StagedAudit`; transcript: `history://PA19StagedAudit`.

## Findings and required disposition

| Finding | Frozen source | Required correction before resume |
|---|---|---|
| MAJOR: surviving children outlive reservations | `stream_check10.py:243–245,91–93,289–309` | Retain or quarantine CPU and big-memory capacity until every owned stage child has exited; UNKNOWN is not permission to release live capacity |
| MAJOR: runner CPU omitted from token accounting | `stream_check10.py:204–206,263–271`; `rss_watchdog.py:98–99` | Compression/decompression overlaps the native solver/checker; parent requires COUNT ≤ 2, with at most two busy processes per token and four per lane; include encoding and extension helpers |
| MAJOR: RSS guard can miss the owner | `rss_watchdog.py:63–69` | Stop new admissions before waiting; attribute RSS to runners and descendants, including CNF/extension phases; cooperatively stop the memory owner, not only a named solver; disclose sampling limits |
| MAJOR: cancellation/free-space race after token wait | `stream_check10.py:175–178`; `run_hard10.py:128–140`; `run_m2_10.py:124–135` | Recheck STOP/cancellation and the 12,000,000,000-byte free floor immediately after token acquisition and before each stage/helper launch; older disk-guard stop names do not cover rev10 |
| MINOR: consumed bytes reported as delivered bytes | `stream_check10.py:270–279` | Require successful complete writes and close; bind bytes actually delivered, and reject replay-feed/decompression/closure failures as UNKNOWN |
| MINOR: compressed flush tail can exceed cap | `stream_check10.py:217–220` | Include compressor flush output in the compressed cap check and exercise that boundary; post-chunk allocation checks are not instantaneous RSS limits |

## What the audit did establish

- The ordinary UNSAT predicate requires solver exit 20, no detected proof cap, checker self-exit 0, exactly `s VERIFIED` after carriage-return stripping, and replay equality. No LRAT-only checker is consulted. The exact delivered-stream assertion still needs the correction above.
- Solver and checker stages do not overlap within one pipeline; the Python runner can overlap either stage.
- Both consumers use the same regenerated CNF; M1 direct also requires its pass-1 CNF hash match.
- `summarize8.py` recognizes revision 10 and correctly distinguishes M1 explicit placement indices from M2 endpoint ranges. No new claim-key, FIFO collision or dispatch drop was found.
- The [saved smoke](../../../../information-science/evidence/six-lane-20261016/packing-array19/cycle2/smoke-stream10.json) shows genuine UNSAT checks, two checked SAT controls, native-limit UNKNOWN, raw-cap UNKNOWN, COUNT-1 serialization and rejection of a forged solver's empty clause. It does not exercise the six findings' boundaries.

## Containment observed by the lane, not independently inspected by this reviewer

InfoPacking19 reports COUNT 0 and stop files set at **2026-10-17 15:34:36 PDT**; all four held stages finished at boundaries by **15:35:32**, without interrupting a proof check. The fifth runner was waiting with no child/token and was stopped by SIGTERM; its reservation was retired with a manifest entry. No SIGTERM survivor or watchdog trip was reported. Sampled native-process maximum 4 and peak lane RSS 1,957,696 KB do not measure all busy runner/helper CPU or prove continuous peak compliance. The reported sampling-window count requires a separate clock-span clarification.

Revision 11 must be newly frozen, retain rev10 artifacts, pass narrow survivor/token, helper-memory, post-wait stop/free-floor, replay-write-error and compressed-flush-tail controls, and receive an explicit parent go. No resource cap is raised. No deletion, SIGKILL, publication or Git mutation is authorized by this disposition.
