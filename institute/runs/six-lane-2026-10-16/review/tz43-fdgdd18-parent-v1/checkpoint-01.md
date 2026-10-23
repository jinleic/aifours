# tz43-fdgdd18-parent checkpoint 1 (2026-10-17 22:54 PDT, host clock)

Desk: Tz43FdgddParentCheck. Started 22:39:43 PDT. Free disk 13,667,172,352 B (floor 12,000,000,000 B).

Done:
- Desk dir created exclusively (inputs/, code/, controls/, runs/, tmp/).
- Pinned copies (sha256 verified, source == expected == copy):
  - inputs/fdgdd_5_18_inflated_D15.txt 3e22f502...a998 (700,931 B)
  - inputs/master_H_5_6.json 89133772...db2c (25,493 B)
  - inputs/local_RDTD_3_4_3.txt fcdb4285...3d58 (1,270 B)
- Own stdlib code written (exclusive create): code/check_fdgdd_format_d.py, code/make_controls.py,
  code/reexpand_blocks.py, code/run_matrix.py. No lane code read, imported or executed.
- In-memory dry runs (eval kernel, Python 3.14): candidate passes all 22 checks; 15 drafted controls each fail
  for the intended check; block re-expansion from master + RDTD equals the candidate block multiset.
  One dry-run output was written to tmp/reexpand-dryrun-1.json (scratch; not evidence).

Next: generate fixtures (bash), run the 2-interpreter x 2-mode matrix, re-expansion runs + comparison controls,
then result.json and report.md.
