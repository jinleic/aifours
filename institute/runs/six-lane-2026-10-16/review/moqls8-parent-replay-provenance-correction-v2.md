# MOQLS(8) proof-digest provenance correction v2

Recorded at 2026-10-18T06:31:58-07:00. This supersedes the compliance interpretation in `moqls8-parent-replay-predicate-addendum-v1.md` (SHA256 `38451b0a0143b9b493df7a4ce79d8922e6b50ae94b50fb61bc21d22d18282d37`), which is preserved unchanged.

The earlier addendum correctly observes that the parent pipelines delivered their solver proof directly to drat-trim and did not record a proof-stream SHA256. Its assertion that this was merely a clarification, not a protocol deviation, is withdrawn. The normal-form verdict explicitly retained F4, whose recorded evidence includes proof SHA256 and byte count. A post-result interpretation does not supply that missing evidence.

The twelve direct-input receipts and P1-B1.M2 remain observations of native verification against their measured, bound CNFs. They are not counterexamples or failed mathematical refutations. Their proof-digest provenance is incomplete. No digest can be recovered from the discarded streams. No final n=8 protocol-complete gate may rely on an assertion that these receipts contain proof digests.

Action: the strengthened replay desk has been told to hold new admissions at the next safe boundary, preserve any already-running attempt, and freeze a new hashing/counting relay for source review and controls before use. Old receipts stay immutable. Native results without proof digests must retain `PROOF_DIGEST_MISSING` in any final reconciliation; qualification requires fresh conforming evidence or a separately explicit authorized protocol exception, not the withdrawn interpretation.

This correction concerns evidence provenance. It does not authorize a weaker formula, a weaker checker, skipped cases, lost guard handling, or a relaxed disk/memory limit. The separate second-encoding obligation also remains open.
