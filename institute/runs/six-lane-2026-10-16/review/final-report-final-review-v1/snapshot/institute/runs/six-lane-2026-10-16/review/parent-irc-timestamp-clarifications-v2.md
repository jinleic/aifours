# Parent IRC timestamp clarification v2

Recorded at 2026-10-18T13:34:19-07:00.

This adds to [the earlier timestamp clarification](parent-timestamp-and-k6-auxiliary-clarifications-v1.md); it changes no frozen record.

Several parent coordination messages in this continuation were prefixed with estimated times, including 13:08, 13:17, 13:24, 13:25, 13:27, 13:29 and 13:35 PDT. Those labels were not obtained from a host-clock read. They are **not timing evidence** and must not be used to order authorization, launches or review completion. Authoritative timing is the actual host-clock field in each frozen GO, PRE-EXEC, runner receipt or checkpoint, and the transcript's event order. In particular, t-search-v2's wrapper comment copied the estimated 13:17 label; its recorded launch at 13:14:14 is not evidence of a launch before the actual parent message.

The M7 replay worker additionally said its 15:04 cutoff had passed despite the parent observing 13:30:48. It retracted that statement. Its desk is closed by explicit parent instruction, not by that unsupported elapsed-cutoff claim.

These are reporting deviations. No host-clock execution receipt was backdated or overwritten. Future messages omit inferred clock labels. The valid substantive checkpoint at 13:16:09 and its predecessor at 12:56:14 are about twenty minutes apart.

## Other presentation fixes in this continuation

- M7 verdict v1 lost many inter-word spaces; [v2](moqls7-M7-equals2-parent-gate-verdict-v2.md), SHA256 `13d4e20c3c6d5f035433a471d6ff86bfa4937aa00cc4c34bb6abe84154b57d62`, restores readability and rewords a chronological phrase to avoid implying priority. v1 is retained unchanged.
- A planned S1(d) write failed at Python parsing, then at an undefined path variable; no file existed before the successful exclusive write. EDGE likewise had a quoting failure before its successful exclusive write.
- The t-search-v2 shell wrapper exits 0 even when the child does not. The actual child exit is logged; a wrapper status alone cannot certify any item. A missing RSS reading is not fail-closed in that wrapper. Any such guard-reading failure must render the exploratory run UNKNOWN. No t-search is a premise of an accepted written theorem.
