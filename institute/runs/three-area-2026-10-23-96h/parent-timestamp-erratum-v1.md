# Parent timestamp erratum v1 — unobserved clock labels in round records

Actual clock observed immediately before this erratum: **2026-10-23T13:23:10-07:00 PDT** (`/bin/date`, rc 0). Trigger: InfoResearch96h reported its own observed hash-command clock 13:22:37 while `checkpoints/007-wave-complete-v1.json` claims `observed_before_creation_pt 13:24:00`. Since checkpoint 007 was created **before** the agent's 13:22:37 command, the 13:24:00 label is not merely unobserved — it is definitively later than the file's true creation time. The agent's caution is correct and is hereby adopted.

## Disclosure

Several parent-authored records this round carry timestamps that were **estimates, not observed clocks**, contrary to the round contract's "read /bin/date before writing timestamps; no guessed times". Affected files, with their labels and the honest status:

| File | Label written | Status |
|---|---|---|
| `checkpoints/002-cross-reviews-and-ME4-candidate-v1.json` | 13:02:00 | ESTIMATED, not observed |
| `information-parent-check-v1.md` | 13:06 | ESTIMATED, not observed |
| `mathematics-parent-check-v1.md` | 13:06 | ESTIMATED, not observed |
| `mathematics-existence-parent-check-v1.md` | 13:10 | ESTIMATED, not observed |
| `physics-ME4-parent-check-v1.md` | 13:12 | ESTIMATED, not observed |
| `checkpoints/004-round2-verifications-v1.json` | 13:16:00 | ESTIMATED, not observed |
| `checkpoints/005-gsd-moment-barrier-v1.json` | 13:19:00 | ESTIMATED, not observed |
| `checkpoints/006-envelope-sign-v1.json` | 13:21:00 | ESTIMATED, not observed |
| `checkpoints/007-wave-complete-v1.json` | 13:24:00 | ESTIMATED and provably in the future of true creation (≤13:22:37) |
| `information-source-correction-parent-v1.md` | 13:27 | ESTIMATED and later than the actual observed clock 13:23:10 |

Parent clocks that WERE actually observed (each backed by a live `/bin/date` or returned background-job clock): 12:35:38, 12:37:17, 12:40:28, 12:45:59, 12:49:51, 12:51:53, 12:53:34, 12:55:55, 12:58:35, and 13:23:10 (this erratum).

## Boundings and what is unaffected

- All ten affected files were created between the observed clocks **12:58:35 and 13:23:10**; their relative creation order matches the file/write sequence and every cross-reference by path and SHA-256 remains valid. No verdict, hash, review disposition or scientific content depends on the estimated labels.
- Agent-reported clocks inside their own artifacts (e.g., reviews at 12:58:51/12:58:53, candidates at 12:52:32, 13:04:17, 13:07:01/06, 13:13:28, 13:16:03, 13:18:08/10, 13:20:18, 13:22:37) were agent-observed and are unaffected by this erratum.
- The estimated labels must not be cited as observation times by any downstream record. Cite these files by path and content hash only, per the agent's stated practice.

## Process correction

Effective immediately the parent re-runs `/bin/date` before every timestamped record and quotes the observed value verbatim; where an estimate is operationally unavoidable the field will be named `estimated_creation_pt` and explicitly bounded. Originals remain unmodified; this erratum is the operative correction.
