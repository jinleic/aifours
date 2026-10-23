# Tz43TriplingAudit — corrections: two time labels and one wording note

Written after `receipt-v2.json`, SHA-256 `8ecd6f41…17a4`. The files below are left unchanged, because the receipt
hashes them; this note supersedes only their time labels.

Two time labels in the desk's markdown were estimates, not host-clock readings. The actual host-clock file times
come from `stat` (birth and mtime, PT):

| File | Label written | Host-clock times |
|---|---|---|
| `verdict-v1.md` | "Recorded … at about 01:08 PT (host clock)" — a guessed, slightly future time | created 2026-10-18T01:05:05, last modified 2026-10-18T01:07:00 |
| `dispositions-v1.md` | "Recorded … at about 01:05 PT (host clock)" | created and last modified 2026-10-18T01:04:11 |

All other time stamps in desk JSON files come from `datetime.now(ZoneInfo('America/Los_Angeles'))`. Those in
`checkpoint-01.md` come from `date`. Nothing else in those two files is affected.

**One wording inaccuracy in `lemma-v2.md`.** Line 15 reads "§4 also cites the v2 generator and runner". In fact §4
cites only the v2 generator, `code/build_tripled_fdgdd_v2.py`. The v2 runner `code/run_checker_matrix_v2.py` is
cited in `dispositions-v1.md` and `verdict-v1.md`. Nothing mathematical is affected.
