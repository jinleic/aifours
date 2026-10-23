# Parent claim-provenance corrections

Recorded 2026-10-18T05:11:29-07:00. These corrections qualify the earlier frozen records; none changes a scientific result or converts UNKNOWN into a proof.

## K0* / RED revision wording

The [parent verdict](olson-reflection-K0star-RED-parent-verdict-v1.md), section "Parent checks", says that no formula changed in r1→r2. That is false literally: r1's second FUS inclusion was false and r2 changed its left side from sigma_v to sigma_u; SING's cardinality and the non-load-bearing F3 statement were corrected too. The supported statement is: **no later use of FUS, theorem conclusion or reduction case changed**. The body lists the exact corrections and both hostile reviews accept the repaired statements. Theorem K0* is for primes p≥5 and length4p−2, with κ computed over maximal constant reflection blocks; it is not an all-integer-p claim.

## N8 EPERM attribution

The [quarantine disposition](moqls8-refine-r3-quarantine-disposition-v1.md) labels a root cause as "verified statically". Static inspection verified two executed code paths invoking setuid-root `/bin/ps`; the failed PID36858 has **no observed command, start time or UID** in the saved record. Identifying that PID as `ps` remains **[INFERENCE]**, not established causality. The failure itself is observed: proc_pidinfo returned EPERM, the supervisor failed closed, and the group stop ended with no survivors. Replacing both privileged-helper paths and passing the r4 non-native lifecycle smoke demonstrate the revised paths on that smoke; they do not retrospectively identify PID36858 or prove all native paths safe.

## Free-space cause and recurrence

The 04:09:50 and 04:53:03 floor crossings, their cooperative stops, subsequent free-space recovery and Time Machine snapshot-list changes were observed. Those observations **do not establish** that Time Machine or Syncthing caused the decline/recovery, that macOS has a thinning trigger near12e9B, or any recurrence period. Statements to workers that inferred an hourly cycle or predicted a one-to-two-hour headroom window must not be treated as measured guarantees. The fresh admission and in-flight floor checks, not those predictions, govern launches. A correction was broadcast to all active workers. No deletion, snapshot thinning, service stop or host configuration change was performed by the parent.

The broad metadata-only large-file scan found recent modification timestamps but no byte-growth baseline; it cannot attribute a disk-space delta. No personal application contents were read or copied by that scan.
