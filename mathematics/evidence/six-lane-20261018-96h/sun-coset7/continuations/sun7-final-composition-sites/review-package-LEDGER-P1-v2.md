# Closed-ledger review packet P1 (v2) — nodes, final-candidate/ROOTS/ROWS-K63 rows, residuals, self-check erratum

Written: `/bin/date` read at 2026-10-20T00:47:27-0700, immediately before exclusive create. Owner SunM13MixedFibres (math-1). Supersedes the
undelivered P1-v1 (dfc8c025…) only to add the erratum; deliverable = P1-v2 + P2-v2.
Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun7-final-composition-sites/LEDGER-v1.md` SHA256 fb8699b77370efcc838be0c4474cf3ba7024ced1a5b909ae4f13511c4daac5de (LF1-177: header, keys, nodes, rows F/R/W; LF314-334: residuals, status), read
with `LEDGER-v1-erratum-v1.md` 92131060b0bfdc00b6e4fa3ea8875aedc52120430f9889092b4f318fe7a2fd57 (X1-X8: conservative forward edges and wording). Scope: `LEDGER-SCOPE-v1.md` 6f1a4fef….
TR LF68 (target) is selected. Companion packet P2-v2 holds rows H/A/K, section 3 graph and section 4 Sun sites.
Manifest: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun7-final-composition-sites/review-excerpts-LEDGER-P1-v2.json` SHA256 e9fd2ff5b6ca68102e53742f037b7d066f0db2acb3c94436c15302abe4a395dd. Repairs FR MAJOR M1 (FR LF7-27; FD LF24-26).
Module import-declaration lines cited as "declared at" in section 3 lie in the census snapshots (IDX groups) and largely in
earlier exposure manifests (X1 c28bbb3c…, X2 f900a8b5…, Y1 04ffed1e…, Y2 67016916…, B-repair 5e98e3dc…); not re-selected (size).
Report any edge you cannot check from the supplied census tables as MISSING rather than assume it.

## Exact review task
Read the supplied sources only. No computation, enumeration, edits, imports, model calls or delegation. Bookkeeping review:
1. Rows F01-F22, R01-R26, W01-W08 (with erratum X4-X6): does the "listed at" line list that interface as live (or open), are
   the statement/scope lines literal, is the correction the operative one, and does the discharge (node body in a census
   group, Zhu, or an S5W/S6W site) match the cited census verdict line?
2. Section 1: is each node's body inside the cited census coverage line, corrections in governing order? Any retained
   module missing, or any node body outside every census snapshot beyond RES-1..RES-3?
3. Completeness: is any live interface of C LF11-22, LF29, LF32, LF49-57, of CR's claim/excluded/Sun/open lists, or of CW
   LF140-149 absent from the rows, or discharged only by a status label?
4. Residuals: are RES-1..RES-6 exact; is anything silently discharged; is W08 (K7-REM not retained) correct?
Return per-row CONFIRMED / MISMATCH / MISSING with LF evidence and FATAL/MAJOR/MINOR. All judgments CANDIDATE_UNVERIFIED;
full Sun(7) UNACCEPTED; no acceptance follows from this packet.

## Size and binding
Selected source bytes: 95767. Package bytes: 3004. Package plus selected bytes: 98771 (< 100000).
Manifest fields: path, whole-file sha256, inclusive one-based start/end physical LF. Metadata-only binding; old files immutable.
