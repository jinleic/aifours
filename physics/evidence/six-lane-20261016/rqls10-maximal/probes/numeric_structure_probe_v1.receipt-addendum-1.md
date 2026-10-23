# Addendum 1 to numeric_structure_probe_v1.receipt.md

Recorded after a parent instruction at about 14:22 PDT, 2026-10-18.

## Withdrawn wording

The receipt says: "The lane wrote about 50 KB in total, so this probe was not the writer."

**The clause "so this probe was not the writer" is withdrawn.** A small recorded output does not prove the process
could not contribute to shared-volume consumption, for example through process-induced swap.

## Correct wording

- The probe's recorded output was small.
- The in-run guard observed a floor breach: free = 11,999,363,072 < 12e9 at about elapsed 251 s. A df at 14:20:05 PDT
  read 11,771,092,992.
- The causal writer is unidentified.

No system services or snapshots were diagnosed or modified.

## Status reminders, unchanged from the receipt

- **Overall: UNKNOWN.** This was a cooperative DISK_FLOOR stop, not a completion. No candidate and no exclusion
  follow from it.
- **G10 was truncated.** It used about 161 of its 170 s slice, over 7 starts.
- **G8 control was weak.** maxdev reached 8.5e-6, which misses the 1e-9 threshold. It is not a successful sensitivity
  control.
- **No further probes.** The one-run GO is used up. No further numerical or native probe is authorised.
