# t-search-v1 run1: admission audit receipt, v1

Written after host clock 2026-10-18T12:40:19-07:00 by OlsonRotationRigidity, at the parent's urgent audit (IRC received
after 12:40:07).

## Facts

- Launch: bash job bg_2294 at 12:39:02 (host clock printed at launch).  Command:
  ../code/gate_v1.sh 50000000 python3 -B code/t_search_v1.py out/run1.jsonl, with stdout and stderr to out/.
  TMPDIR = t-search-v1/tmp, PYTHONDONTWRITEBYTECODE=1, no ulimit, no tool timeout.
- The PID of the Python process was not recorded: gate_v1.sh execs the command.  This is disclosed as a receipt gap.
- End: the job reported exit=0 at 12:39:16.  The script wrote DONE (elapsed 13.4 s).
- The run had already ended when the audit message arrived.  At 12:40:19, pgrep -f t_search_v1.py found no process.
  So no SIGTERM was sent: there was no process to stop.
- Outputs, preserved unchanged:
  - out/run1.jsonl e79de63132ab3d23b510b1c45f788da96a97e36b13287494193b02bd870d2780 (11 lines);
  - out/run1.stdout.txt 0b75a4c0c3baa9d1723f550bee82d017d15b07cbf18eeeb6fba8daabfcc2cdff (contains the gate line);
  - out/run1.stderr.txt e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty).

## Admission checks actually performed

1. Disk gate: code/gate_v1.sh (sha256 0292511a24268e69a37c6de7d3d93bbfd7305e9895b7bdd2da7dc65d22634e5a).
   - It requires statvfs free >= 12.2e9 + projected bytes, here 12,250,000,000.
   - Printed: GATE-OK free=41787121664 need=12250000000 12:39:02.
2. Monitor check at 12:38:44.  This was an inline Python heredoc, not saved as a file; its text is in the session
   record.  It read R/disk-monitor-v1-20261018T0722-to-1810.jsonl and checked:
   - last sample age <= 30 s: 12:38:36, age 9 s;
   - strictly increasing timestamps;
   - at least 300 samples in the last 60 min: 360;
   - minimum free in the last 60 min >= 12.25e9: 42,945,286,144.
   Reported as "PASS".

## Deviation

The second check is NOT the frozen 300 s stability rule.  The parent states that rule as: over the last 300 s window,
the largest drop from a peak to a later sample must not exceed max(300e6, (latest free - 13.5e9)/12).  Recomputed after
the fact from the same monitor file:
- Window ending 12:38:36 (the sample my check read): 31 samples.  Free 49,265,217,536 -> 42,946,519,040.  Largest
  drop 6,319,931,392 B; allowed 2,453,876,586 B.  FAIL.
- Window ending 12:38:56 (the parent's window, 12:33:56-12:38:56): 31 samples.  Free 49,262,522,368 ->
  42,769,801,216.  Largest drop 6,493,204,480 B; allowed 2,439,150,101 B.  FAIL.
So the launch was admitted under the wrong rule.  The correct rule would have refused it.

## Status

- Per the parent, the scientific attempt is UNKNOWN.  The controls and outputs above are preserved, and no claim
  rests on them.
- There will be no relaunch until a correctly evaluated, fresh 300 s window passes and the parent gives a new GO.
- Future admissions in this slice evaluate exactly that 300 s rule, from a saved script with a recorded hash, and
  record the PID.
