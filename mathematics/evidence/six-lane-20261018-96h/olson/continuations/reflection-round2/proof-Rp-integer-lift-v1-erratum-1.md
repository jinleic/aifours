# RP-LIFT erratum 1: CONNECT's preceding-gap wording

Frozen after /bin/date observation 2026-10-19T08:33:09-0700 by OlsonReflectionSuccessor.  Original source unchanged:
proof-Rp-integer-lift-v1.md, SHA256 34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69.
Parent relayed the Codex RP-LIFT finding: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 1 MINOR; Claude review pending.
This overlay records only that MINOR and makes no acceptance claim.

In Lemma CONNECT, replace "this preserves the preceding gap, and enlarges the following one" by:
"this decreases the preceding gap by one but keeps it at least 1, and enlarges the following gap by one".
The preceding gap is an integer >1 before the decrease, so feasibility is preserved, not the gap's numerical value.
The same wording applies to the wrapping predecessor gap x_1+k-x_n when coordinate 1 is decreased.  All other gaps stay
unchanged.  No statement, case, inequality or conclusion changes.
