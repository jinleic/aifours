# Pending items for the ONE next supervisor version after owned_supervisor_v7 (written note; no code yet)

Recorded 2026-10-19T07:08:30-0700 (from /bin/date). Author ContinueRQLS10b. code/owned_supervisor_v7.py (a45f8538...d2fa)
is unchanged and under the parent's independent source review; per the parent (07:07) a successor is written only
together with the findings of that review, as ONE version with a cumulative diff and a disposition. Until then the
assay v7 / checker v5 review is on hold (their supervisor API is not final); no science, no Q1.

## P1 (parent, 07:07): monotonic publication evidence and parent commit
v7 sets receipt mono_end before publish(receipt) and publish_linked(settlement); the settlement record's file birth time
is wall clock. Successor contract: after BOTH publications, their re-reads and the directory fsync, the supervisor
reads time.monotonic() once more and prints ONE stdout summary line carrying post_publish_mono, the verified receipt
sha256 and the verified settlement-record sha256 (plus settlement, exit code meaning, trips, first failures). The parent
captures and verifies that line and writes its own exclusive commit record; only that commit is authoritative and only
it releases reservations. The successor checker (after fixedb_q1_check_v5) must take the latency bound from the
parent-captured post_publish_mono (signal mono_sent -> post_publish_mono <= 7 s; trip mono -> post_publish_mono <= 7 s)
and must drop the wall-clock birth-time criterion; Q1 latency is not qualified by v7/v5.

## P2 (self-review): lane roots must be real directory chains
Lane membership compares kernel-canonical cwd paths with the configured lane_roots by string prefix. A lane root path
with a symlink component would never match (fail-open for lane RSS/busy accounting). Admission must require
real_dir_chain for every lane root (v7 checks lane and lane_disk_root only).

## P3 (self-review): anchored lane walk
walk_bytes re-opens subdirectories by path; a directory replaced by a symlink between listing and descent is followed
(counts may be wrong in either direction). Walk through O_DIRECTORY|O_NOFOLLOW descriptors (scandir on fds, openat
descent) and treat a symlink or a vanished directory consistently.

## Not changed by these items
Outcome set, failure latch, lineage census, identity tuple, single reaper, bounded reads, grace rules, one-use GO
admission and the qualification scenarios (plan v4) stay as in v7 unless the parent's review requires otherwise; the
qualification plan/checker are re-versioned only if the summary or receipt fields they read change.
