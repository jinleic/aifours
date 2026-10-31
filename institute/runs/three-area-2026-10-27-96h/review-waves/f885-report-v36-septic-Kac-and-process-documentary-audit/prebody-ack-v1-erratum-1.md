# F885 prebody ACK — additive erratum 1 (DocF885SPRKM36)

Recorded after native observation `2026-10-30T20:29:46-0700` (`2026-10-31T03:29:46Z`). Read with unchanged `prebody-ack-v1.md` (2286 B), which is not edited.

The ACK file and the direct ACK message to Main said every administrative/control file was read "in 20-LF-or-smaller raw windows". That wording is inaccurate for three administrative windows: `manifest-v1.json` LF441–465 (25 LF), `freeze-receipt-v1.json` LF401–427 (27 LF) and `actual-dispatch-receipt-v1.json` LF61–83 (23 LF). Every other administrative window and all 25 control windows were ≤20 LF. Each of these windows was a few KB, far below 30000 bytes. All administrative files and controls were still read completely before any packet body. The manifest `packet_policy` limit (`raw_window_max_lf` 20) applies to the literal packet parts. Every packet-part window was ≤20 LF and <30000 B (measured; see `review-v1.md` §2).

This is a reviewer documentary/process self-report about the ACK wording. Compliance is not backdated, and the parent will classify it. It changes no packet read, comparison or finding. All held episodes AND ALL consumers remain NONINPUT.
