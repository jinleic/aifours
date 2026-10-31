# f313 — Routing and clock documentary audit

## Findings

**No substantive documentary finding at the assigned scope: 0 FATAL / 0 MAJOR / 0 MINOR.** No report-line replacement is warranted by the inspected evidence.

**Overall correctness:** correct at the assigned documentary scope.  
**Confidence:** 0.98.

The routing and status wording are consistent with the pinned documentary evidence. This verdict does **not** audit mathematical results or certify scientific acceptance, final closeout, owner settlement, or continuous supervision.

## Administrative sequence and coverage

Fresh `/bin/date` observations:

- **2026-10-30T14:25:58Z:** before review reads.
- **2026-10-30T14:29:04Z:** after complete packet reading and during metadata checks.
- **2026-10-30T14:30:17Z:** before delivery.

These are reviewer observations, not historical author-event clocks.

Before opening the packet body, I read the entire manifest, freeze receipt and all five designated status-only controls, checked their hashes, and submitted an administrative **PRE-BODY ACK**. The writer refused the wave-path ACK; it was not materialized. The ACK submission remains in the tool transcript. No bypass was attempted.

I then read **every frozen packet line 1–473 raw**, using individual windows of at most 20 LF, including the ending. Complete literal coverage:

| Source | Lines |
|---|---:|
| S1 | 1–52 |
| S2 | 1–160 |
| S3 | 1–29 |
| S4 | 1–89 |
| S5 | 1–37 |
| S6 | 1–30 |
| S7 | 1–28 |
| S8 | 1–27 |
| S9 | 1–19 |

No excluded link or held mathematical body was followed. Controls and ledger-row strings were used only as documentary status/metadata, not scientific premises.

## Metadata binding

Actual SHA-256 values matched the assignment and recorded pins:

| Artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| Manifest | `ff0ae1f2a72d8e55df505097e4eacdb34582d8607ed9a1928f18b0f49d3f1456` | 7,895 / 168 |
| Freeze receipt | `23a57eb944dbe800a664a92a615dfb828cf7569d755789a9081c87c511d1c6b1` | 4,930 / 138 |
| Literal packet | `4dad09ebd97d83f7bd0a89c56321b94c127430468500438b094a168934b3afb6` | 58,590 / 473 |
| Report | `7bde041747ef862756194c31f70c55d842206c1069f9ee4adeb3ff4dc203c5c0` | 13,183 / 52 |
| Routing census | `8e12551ba3a953c686367f2ce9fe5a24a997aec3a1d6af0835e5114bc7bd4ef6` | 24,657 / 160 |
| Navigation receipt | `ed6810573227e16e39c5b04811b96e4e5d5d61dd0231f85654cf799168d30804` | 1,208 / 29 |

The remaining declared input hashes and sizes/LF matched their pins.

The actual README matched census metadata: SHA-256 `6b178910fad57662787d81a1ae7ad838b68213174624ed3533c37e7ad0b42f92`, **237,422 bytes / 336 LF**. The actual contract matched SHA-256 `d4fce258f5e97729a8b5ae3fb0a120d29db6b4bac417e380fd0949da90113be7`, **18,303 bytes / 301 LF**.

README inspection was limited to hashing/counts and documentary row/path equality; contract inspection was limited to schema keys and slot/owner fields. No scientific conclusion was drawn from either.

## Per-claim dispositions

### SUPPORTED — Eighteen-slot routing and owner identity

**Report lines 17–34** match all 18 census records in **S2 lines 24–149**, both owner text and exact destination path.

Metadata comparison against the pinned README also found:

- Each census `last_raw_row` equals the actual final row for that slot.
- Its final record href resolves to the census `last_record`.
- Every census `owner_from_contract` field matches the actual contract slot/owner field.

Seventeen report owners match the contract directly. **Info-6** carries the explicitly authorized successor exception, `InfoBalancedNL242-3 (successor)`, rather than presenting it as the original `InfoBalancedNL242-2-2`.

**Report lines 3 and 13** explicitly distinguish historical owner identity/ledger routing from current activity and unconditional theorem status. No stale-path or owner-routing defect was found.

### SUPPORTED — Local navigation at the receipt’s stated scope

The **S3 receipt lines 10–25** binds the exact report hash and asserts **47 rendered local hrefs**, zero directory targets and no missing targets, using `Bun.markdown.html`.

An independent documentary rendering of the frozen report with that renderer reproduced **47 hrefs**. Filesystem checks found **all 47 target occurrences present**, with **zero directory targets**. Target files were not opened through those links.

**Fragment correctness remains INCONCLUSIVE/not audited.** S3 line 25 expressly excludes fragment validation, so existence of `README.md` is not promoted to proof of the `written-result-ledger` fragment. Neither this review nor the receipt verifies target scientific content, external publication, owner activity, or navigation inside linked documents.

### SUPPORTED — Clock labels and non-final/deadline boundaries

**Report line 3** records an as-of native observation of **2026-10-30T07:21:26-0700 PDT**:

- **S3 line 3:** the same observed-before-creation clock.
- **S4 line 3:** later checkpoint observation, **07:22:38-0700 PDT**.
- **S2 line 3:** later census observation, **07:25:11-0700 PDT**.

These observations are **not completion, write, or dispatch timestamps**. The later checkpoint/census cannot prove that their events were complete at the report’s earlier as-of observation.

Consequently, precise completion/dispatch times at **07:21:26** remain **INCONCLUSIVE on this packet alone**; no contrary event timestamp establishes a false report sentence. **Report lines 1, 3, 42 and 52** expressly avoid final-report, science-stop and later-settlement claims.

The deadline in **report line 3** remains **2026-10-31T21:23:27Z**, consistent with **S4 line 4** and the owner-direction control. No backdated-completion or finality correction is justified.

### SUPPORTED — Provider failures and duty/owner distinctions

**Report line 40** preserves failed f299 as **429/NO_VERDICT** and failed owner wakes as **no answer**, rather than successful deliveries. This matches **S5 lines 15–32**; **S4 line 86** likewise disclaims successful original-owner acknowledgments.

**Report lines 38–40** distinguish prospective written **AUTHOR CANDIDATE** duties from independently reviewed results. **S4 lines 39–71** records the separate development agents and their author-duty ceiling. These do not establish that the historical owners in the table were active.

**S5 line 34** gives a vendor reset string without a verified timezone. The report makes no reset-timezone or retry-schedule inference; none is added here.

Actual provider/account/configuration operations were not independently audited. This disposition concerns documentary fidelity, not an operational absence certificate.

### SUPPORTED — Diagnostic and supervision disclosures

**Report line 46** preserves both permanent parent supervision gaps—**6h10m42s** and **2h32m26s**—matching **S6 lines 11–17** and **S5 lines 10–13**. It explicitly denies that later observations repair continuity.

**Report lines 47–48** preserve the selected-review holds, narrow author execution/reporting rulings, and both later parent private-diagnostic quarantines. This is consistent with the status-only controls and **S7–S9**: whole-episode/consumer exclusion is not converted into a theorem-falsity finding, clean-fragment salvage, or verification credit.

The two parent quarantine controls preserve prior frozen inputs only at their existing scopes and disclaim clean-cognition certification. **Report line 48** retains that distinction.

## Assurance and delivery boundary

No source theorem or scientific result was imported or independently reconstructed. Scientific correctness, originality, author cognition, historical runtime continuity, exact dispatch/completion times, and full owner-slot settlement are outside this verdict.

Documentary execution was restricted to hashes, byte/LF counts, renderer href extraction, file existence, and text/path/owner comparisons. No scientific execution, selected mathematical probe, CAS/solver, external-model CLI, account/configuration change, test/build/lint/formatter, deletion, commit, or push was performed.

Frozen report and source bytes were preserved. **The writer refused both ordinary filesystem-path writes, including `review-v1.md`. This full review is returned for parent materialization under the manifest’s refusal fallback; no write bypass was attempted.**