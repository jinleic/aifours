# Addendum v2: approximate time labels in this slice are NOT host-clock reads

Supersedes addendum-timestamps-v1.md (written 2026-10-18T05:06:06-07:00, kept unchanged), whose bounds for two rows
were wrong (the "verdict read" row and the proof-EXP-v1.md rows).  This v2 was written after the host-clock read
2026-10-18T05:06:06-07:00 (no newer read before writing; the exact minute of writing is therefore not known).
No earlier file is rewritten; this addendum only qualifies their labels.

Every label of the form HH:Mx, "02:41", "02:49", or "02:37" listed below is a guess or a borrowed time, not a clock
read of this slice.  The bracket gives the nearest actual host-clock reads (command output) that bound the event.

| file / line | label | actual bounding clock reads |
|---|---|---|
| README.md "01:4x README written" | 01:4x | after 01:44:19 (directory creation), before 01:52:07 (first experiment) |
| README.md "02:3x proof-ROT-lowodd-v1.md written" | 02:3x | after 02:29:51, before 02:33:30 |
| README.md "02:37 parent IRC" | 02:37 = the parent verdict's own decision time (02:37:32), not a clock read here | IRC handled after 02:36:50, before 02:40:01 |
| README.md "verdict ... read 02:3x" | 02:3x | after 02:36:50, before 02:40:01 (v1 wrongly said after 02:35:59) |
| README.md "03:0x parent IRC ... INC error" | 03:0x | after 02:57:50, before 03:04:51 |
| README.md "03:1x proof-ROT-o4-v1.md written" | 03:1x | after 03:04:51, before 03:12:39 |
| README.md "04:1x proof-EXP-v1.md written" | 04:1x | after 04:13:12, before 04:14:11 (v1 wrongly said after 04:14:11) |
| README.md "Note (parent IRC 05:0x)" | 05:0x | after 05:01:04, before 05:02:54 |
| proof-ROT-o3-v1.md header "02:41 ... (exact minute not read)" | 02:41 | after 02:40:36, before 02:46:18 |
| proof-ROT-o3-v2.md header "after host clock 02:49" | 02:49 | after 02:48:54, before 02:57:50 |
| proof-ROT-o3-v3.md header "after host clock 03:0x" | 03:0x | after 02:57:50, before 03:04:51 |
| proof-ROT-o4-v1.md header "after host clock 03:1x" | 03:1x | after 03:04:51, before 03:12:39 |
| proof-EXP-v1.md header "after host clock 04:1x" | 04:1x | after 04:13:12, before 04:14:11 |

Labels that ARE clock reads of this slice (unchanged): notes-GRX-v1.md (after 01:52:10), proof-ROT-lowodd-v1.md (after
02:28:15), proof-SHROT-v1.md (after 04:44:39), proof-ROT-o4-v2.md (after 05:01:04), every HH:MM:SS range in README.md.
