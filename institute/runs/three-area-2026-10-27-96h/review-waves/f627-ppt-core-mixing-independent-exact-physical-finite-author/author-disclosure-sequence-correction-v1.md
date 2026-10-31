# f627 additive correction: disclosure event sequence

The previously written `author-report-documentary-edit-disclosure-v1.md` incorrectly places Main's decision before the post-edit report metadata observation. Its before/after line texts, its record of the in-place edit, and its report/source metadata remain unchanged; this correction withdraws only that ordering. The prior disclosure is retained without editing or deletion. Its observed SHA256 is `3f699fc0ef13c059b71d7e4d115ead72964857fd25d469e57320131390dabdd3` (4,296 bytes, 25 LF).

The actual order was:

1. Create the checker source; observe its hash/size/line count; then observe clock `2026-10-30T14:51:10-0700 PDT`.
2. Create the report; no initial report hash was observed.
3. Make the one disclosed in-place line 11 edit to that unreturned report.
4. Send Main the direct disclosure and request its process decision.
5. Observe the post-edit report SHA256 `9cb4a0057ebdec56dc93622b1239f18ca64ff0fe8cf3fb81d90cef1e1d441024`, 14,124 bytes and 126 LF.
6. Receive Main's decision: documentary/process deviation, no automatic scientific invalidation or full-episode hold on the reported facts, retain the report unchanged, and create an additive disclosure.
7. Observe native clock `2026-10-30T14:54:19-0700 PDT` and create the first additive disclosure.
8. Observe that disclosure's hash, size and LF count as above, then obtain native clock `2026-10-30T14:55:38-0700 PDT` before creating this correction.

The individual creation/edit/message event times were not recorded. Clock reads bound only the observations described and do not backdate them. The checker has not been scientifically executed; the source and report have not been edited again. No initial report hash is asserted.
