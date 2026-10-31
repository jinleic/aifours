# Erratum 1 to the dyadic box-cover packet

**ERRATUM, NOT AN EDIT.** Native `/bin/date`: Thu Oct 29 04:17:15 PDT 2026. The pinned packet `frontier-20261029-cyclic15-boxcover-one-no-go-v1.md`, SHA-256 `03e8a0cc65ccae8ce13880199690e02a147a45e2faa08c365f49b01a4495937e`, remains byte-unchanged.

Its line 25 cites the replay script `frontier-20261029-cyclic15-boxcover-replay-v1.py` with an incorrectly transcribed 63-character hash ending `...edc2cf3cb`. The script's actual SHA-256, as printed by `shasum` in the replay run and recomputed now, is

`8c2ac634ddba0780a08089b58111fd7b070b81d16492d8c3fe4a31edc2cf7dcb`.

All other cited hashes in that packet match the files. The replay result `frontier-20261029-cyclic15-boxcover-replay-v1.json` SHA-256 `9f42348e94ff1590aaad932eabfb940d4ef79dd71b14a2904d8d1ab02790e70a` already recorded the correct script hash in its own `source_sha256` field. Consumers should use the corrected hash above. This affects provenance text only; no mathematical claim, certificate, replay output or scope changes.

A mechanical audit of 213 backtick-cited hashes in today's Markdown packets and 55 file/hash pairs in today's JSON records found this as the only mismatch among files present in the root.
