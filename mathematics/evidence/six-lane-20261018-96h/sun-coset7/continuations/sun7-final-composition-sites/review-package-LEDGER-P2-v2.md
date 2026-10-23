# Closed-ledger review packet P2 (v2) — RICH-A1/R2-A2/K62 rows, explicit closed module graph, Sun(5)/Sun(6) sites, residuals

Written: `/bin/date` read at 2026-10-20T00:47:27-0700, immediately before exclusive create. Owner SunM13MixedFibres (math-1). Supersedes the
undelivered P2-v1 (03f482be…) only to add the erratum; deliverable = P1-v2 + P2-v2.
Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun7-final-composition-sites/LEDGER-v1.md` SHA256 fb8699b77370efcc838be0c4474cf3ba7024ced1a5b909ae4f13511c4daac5de (LF1-106: header, keys, nodes; LF178-334: rows H/A/K, section 3 graph, section 4
Sun sites, section 5 residuals, section 6 status), read with `LEDGER-v1-erratum-v1.md` 92131060b0bfdc00b6e4fa3ea8875aedc52120430f9889092b4f318fe7a2fd57 (X1 Sun-edge convention; X2-X3
conservative forward edges; X7-X8 wording). Companion P1-v2 carries C, FR, CR, CW and rows F/R/W.
Manifest: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/sun7-final-composition-sites/review-excerpts-LEDGER-P2-v2.json` SHA256 fe6f98372479161e66bc9f19342752c2802c4af049b8c2552692456bb01bd0b7. Section 3 replaces the numbered order asserted at C LF62 (in P1).
Its "declared at" lines lie in the census snapshots and largely in earlier exposure manifests (X1 c28bbb3c…, X2 f900a8b5…,
Y1 04ffed1e…, Y2 67016916…, B-repair 5e98e3dc…); not re-selected (size). Report any edge you cannot check as MISSING.

## Exact review task
Read the supplied sources only. No computation, enumeration, edits, imports, model calls or delegation. Bookkeeping review:
1. Rows H01-H08 (CH LF96-110), A01-A08 (CA LF94-103), K01-K06 (CK LF105-112): literal scope, operative correction, and
   discharge consistent with the cited census lines?
2. Section 3 with erratum X1-X3: does each node's input list match what the census tables report the module imports? Is
   every input number smaller than its node (acyclicity)? Are C1-C4 right, in particular C3 (N16 RW and N57 CAP62 have no
   operative consumer) and C4 (as amended by X8)?
3. Section 4 (with X7): is every live Sun(5)/Sun(6) site bound with ambient subgroup, coset side/inversion and piece count?
   Compare CH LF59-71, CA LF51-59, CK LF77-81 here and CR LF85-94, CW LF109-136, FR LF45-55 in P1. Missing or misbound sites?
4. Section 5: are the residuals exact and nothing silently discharged?
Return per-item CONFIRMED / MISMATCH / MISSING with LF evidence and FATAL/MAJOR/MINOR. All judgments CANDIDATE_UNVERIFIED;
full Sun(7) UNACCEPTED; no acceptance follows from this packet.

## Size and binding
Selected source bytes: 95789. Package bytes: 2869. Package plus selected bytes: 98658 (< 100000).
Manifest fields: path, whole-file sha256, inclusive one-based start/end physical LF. Metadata-only binding; old files immutable.
