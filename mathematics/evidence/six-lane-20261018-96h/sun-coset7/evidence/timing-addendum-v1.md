# Timing addendum v1: withdrawal of three unobserved IRC time labels

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:17:10-0700.
- **Append-only:** the files below stay frozen and byte-identical; this addendum withdraws one phrase in each.

| file | sha256 | file created (host mtime) | withdrawn phrase |
|---|---|---|---|
| `K63-D-erratum-v1.md` | 75478241f060873f3911b897ad65a41cb46a3637dd8d15bfe8e09f3e7f3dae90 | 2026-10-19T01:07:41-07:00 | "(IRC at about 01:35 PDT)" |
| `K63-E-erratum-v1.md` | b5d07d06f50f44262985553ece0101268f523a0c53edf18fdaca924e52968480 | 2026-10-19T01:07:41-07:00 | "(IRC at about 01:35 PDT)" |
| `K7-35-erratum-v1.md` | b13e1cf28dd55cd0983c5cc8259520e6723206d556dbcad27389ac6aaec66e32 | 2026-10-19T01:10:27-07:00 | "(IRC at about 01:45 PDT)" |

Each withdrawn label was my unobserved estimate of the parent IRC's arrival time and is later than the file's own
creation time, hence wrong. The correct statement is only: **the parent's finding was received by IRC before the
erratum was created.** No `/bin/date` reading was taken at IRC arrival. All other timestamps in this lane's files come
from `/bin/date` reads (or, for probe records, from `/bin/date` and `ps lstart`). Mathematical content is unchanged.
