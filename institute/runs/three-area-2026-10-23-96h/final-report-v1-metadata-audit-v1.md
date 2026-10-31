**Verdict:** the frozen `final-report-v1.md` needs corrections before delivery: 1 MAJOR and 6 MINOR findings. Confidence about 0.8. I read only the report and the 15 allowlisted files, plus generic skill text before any run file. I opened no linked proof, owner, legacy or Atom body, and used no shell. So I did not recompute the report SHA myself; render receipt v2 records it as `ed8342c3…`, equal to the frozen hash.

## Findings

**1. MAJOR — Section 2, line 21 (new-science-stop bullet)**
- **Excerpt:** "Final-status collection was dispatched afterward ([dispatch receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-dispatch-v1.json)); owners' reported science-stop and post-cutoff clocks remain separately qualified in Section12."
- **Problem:** Section 12 (lines 347–366) has only an owner-reported prewrite clock column (11:08:01–11:14:18). Line 368 adds no qualification about when science stopped, so this pointer is false.
  - The bullet leaves out a fact the cited receipt records: InfoBalancedNL242-2-2 was the only live owner task at 11:05:41, and it was told to stop by a message sent after the receipt.
  - The status census holds only two NL242 clocks (11:14:18 and 09:49:32) and no clock about its stop. The census's limit — owner clocks are owner-reported, not independent write-time attestations — is not carried into the report.
  - NL242's stop-related clocks and the rule against backdating a stop instant appear only in v268.
- **Evidence:**
  - RUN/cutoff-science-observation-v1.json:17
  - RUN/post-cutoff-final-status-dispatch-v1.json:33-36
  - RUN/post-cutoff-final-status-cadence-and-order-dispositions-v268.json:141-142
  - RUN/report-final-status-census-v1.json:203-213, 710
- **Replacement (whole line 21):** - **New science stops (11:05:38):** observed at **2026-10-27T11:05:41-0700 PDT** ([receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/cutoff-science-observation-v1.json)). At that observation `InfoBalancedNL242-2-2` (same info-6 slot under v263) was the only live harness owner task; its stop-science direction was a message delivered after the receipt. Final-status collection was dispatched afterward ([dispatch receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-dispatch-v1.json)). Section 12 lists only owner-reported post-cutoff prewrite clocks; those and the earlier observation clocks bound in the [status census](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-final-status-census-v1.json) are owners' reported native observations, not independent write-time attestations. For NL242, [v268](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-cadence-and-order-dispositions-v268.json) records a reported last mathematical candidate preclock 10:59:43, checkpoint 105 at 11:01:15, administrative checkpoint 106 at 11:03:28 and first post-cutoff observation 11:08:00, with no post-cutoff science/proof-body opening reported; no exact science-stop instant is backdated or certified.

**2. MINOR — Section 2, lines 22–23 (deadline bullets)**
- **Excerpt:** "the assembly clock above records this report's creation before the deadline."
- **Problem:** the line 3 clock was observed "immediately before writing", so it only shows the report was written no earlier than 11:28:03. It cannot show the write finished before the deadline. The only after-the-write evidence is render receipt v2, which records the frozen SHA at 11:29:24.
  - Line 22 likewise pairs the 11:35:38 deadline with an 11:21:04 observation. The receipt itself says that observation came before the deadline, and this report was assembled at 11:28:03, also before it. Unlike line 23, line 22 never says the deadline itself was not observed.
- **Evidence:**
  - final-report-v1.md:3
  - RUN/final-report-v1-rendered-check-v2.json:3,6
  - RUN/settlement-native-final-observation-v1.json:5,7-8
- **Replacement:**
  - Append to line 22: " That observation and this report's 11:28:03 assembly both precede the 11:35:38 deadline; the deadline itself is not claimed as observed."
  - Replace line 23 with: - **Final report deadline (12:35:38):** the assembly clock above was observed immediately before writing and bounds this report's creation only from below; completion before the deadline is bound by post-write receipts (the render receipt and `final-delivery-receipt-v1.json`). The deadline itself is not claimed as observed.

**3. MINOR — Section 8, line 95**
- **Excerpt:** "A fourth verifier checked Sections 1–10 of the frame ([review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-v1.md)); its ten findings are applied per [v267](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-dispositions-v267.json)."
- **Problem:** the reviewed object was frame v2. This report's Sections 1–10 come from `report-final-frame-v6.md`, which line 113 says was created after the 11:12:16 snapshot.
  - Values generated later could not have been covered. For example, line 80's 170-record count comes from a carry created at 11:27:06, and that carry already lists v267 as existing — so the reviewed frame predates the count.
  - Without a version, "the frame" reads as if the final Sections 1–10 were reviewed.
- **Evidence:**
  - final-report-v1.md:80, 113
  - RUN/report-parent-deviation-carry-final-v1.json:3, 18
- **Replacement:** A fourth verifier checked Sections 1–10 of frame v2 ([review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-v1.md)); its ten findings are applied per [v267](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-dispositions-v267.json). The final frame v6 and values generated after that review (for example, the 170-record carry count) are outside those four verifiers' checks.

**4. MINOR — Section 12, line 356 (math-2 row)**
- **Excerpt:** "No new Olson result; v261 concerns privacy only. Actual-word bridge and all-finite-group target open. |"
- **Problem:** v268 classifies MathOlson-2-2's gap from 09:22:20 to 11:06:12 (1h43m52s) as a new, distinct cadence PROCESS MAJOR. The other 13 owners with such a v268 finding all carry a cadence note in Section 12; this row has none.
- **Evidence:** RUN/post-cutoff-final-status-cadence-and-order-dispositions-v268.json:58-63
- **Replacement (last cell):** No new Olson result; v261 concerns privacy only. Actual-word bridge and all-finite-group target open. New cadence interval.

**5. MINOR — Section 12, line 358 (math-4 row: the record set is addendum + mandatory base, but only the addendum's hash and line count are shown)**
- **Excerpt:** "| `162e25262ace` | 27 | 2026-10-27T11:09:57-0700 |"
- **Problem:** the hash and LF cells cover only the 27-line addendum. The census and the complete-read receipt both bind the base (`cbf864316dcb…`, 141 LF, base prewrite 11:08:10), and v268 says the two files must travel together.
- **Evidence:**
  - RUN/report-final-status-census-v1.json:361-362, 376-379
  - RUN/report-final-status-main-complete-read-receipt-v1.json:4, 176-179
  - v268:152
- **Replacement (cells):** | `162e25262ace` + base `cbf864316dcb` | 27 + base 141 | 2026-10-27T11:09:57-0700 (base 11:08:10) |

**6. MINOR — Section 12, line 365 (physics-5 row)**
- **Excerpt:** "One later status file identified only by metadata; metadata-derived cadence interval qualified."
- **Problem:** v268 classifies this as PRESERVE_OWNER_REPORTED_CADENCE_MAJOR_WITH_METADATA_DURATION_QUALIFICATION.
  - The MAJOR is kept; only its 09:26:05 filesystem-birth start is qualified as metadata, and v268 calls the later file an unread checkpoint.
  - As written, the row reads the same as the math-5 and math-6 rows, where no new interval is asserted.
- **Evidence:** v268:124-136
- **Replacement:** One later checkpoint identified only by metadata; the owner-reported new cadence MAJOR is preserved, with its 09:26:05 filesystem-birth start qualified as metadata, not a native observed clock.

**7. MINOR — line 82 (Section 6) and line 354 (info-6 row)**
- **Excerpt (line 82):** "The later final-wake cadence, memory-order qualification, Semigroup correction and NL242 administrative read-order finding are disposed in [v268](…)."
- **Problem:** v268 also keeps a separate NL242 disclosure: its fresh continuation opened park-v17 and checkpoint082 before the no-old-checkpoint direction. Their exact protected status is not established, and v268 says not to reopen them.
  - Line 82 and the info-6 row both omit it, so line 76's exposure list is missing one item from v268.
- **Evidence:** v268:142-143
- **Replacement (line 82):** The later final-wake cadence, memory-order qualification, Semigroup correction, NL242 administrative read-order finding and NL242's disclosed earlier opening of park-v17 and checkpoint082 (exact protected status not established; not reopened) are disposed in [v268](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-cadence-and-order-dispositions-v268.json). No held proof or selected value was recovered for those decisions.
- **Optional, line 354:** insert "earlier park-v17/checkpoint082 opening disclosed, protected status not established;" before "no whole-type or witness result."

## UNVERIFIABLE (the allowlist cannot settle these)
- **Line 7:** that fifteen owners were actually launched, the October 23 replacement dates, whether roster v3 is current, and whether info-1 and info-4 were authorized to write under `privacy-diamond-mse` and `tuscan2-11` instead of their contract-v2 `write_root`s `sof24` and `recursive-mds18` (contract-v2:55, 58).
- **Lines 86–90:**
  - What the source maps say: the 18 mapped records, the scouts having no clock, the null fields, and whether the 46 IDs are the complete mapped set.
  - That non-arXiv sources are "unrefreshed as recorded".
  - That the Atom XML bytes match the pin; I did not open the XML.
- **Line 95:** the contents of v264, v266 and v267, and the count of "ten findings".
- **Line 104:** that no Git commit, push or similar action is recorded in the parent ledger; the README ledger is not on the allowlist.
- **Line 110:** that later README changes are only "header-pointer" changes.
- **Line 113:**
  - Whether the list of post-snapshot files is complete.
  - When queue v1 and frame v6 were created.
  - Whether the arXiv pin (same 11:12:16 clock as the ledger census) was written after the snapshot.
- **Lines 23 and 114:** `final-delivery-receipt-v1.json` is not yet available. It should bind render receipt v2, not the erroneous v1.
- **Line 67:** what gates each owner's final record carries, and the pre-cutoff queue.
- **Line 119:** that Section 11's bytes equal v4 from its Information science heading onward. The SHA matches the erratum's pin at erratum:6-7, but v4 itself is not on the allowlist.
- **Lines 349–366:** row text beyond what v268 and the census show (for example SOURCE-MATCH-U1, RM-S015, v199–v216/W44DB, v261, J49/J50, "No new file").
- **Section 6:** record-specific claims other than the carry count and the v268 paragraph.

## Checked, no finding
- **Section 2:** the contract cutoffs and window match contract-v2:6-7, 48-52. The receipt clocks are at or after their cutoffs (10:35:40, 11:05:41), and the settlement observation (11:21:03–04) falls between the science cutoff and the owned-compute deadline. The argv/cwd matches are empty, N4 is absent, no owned tasks were live, no signal was sent, and the wording stays bounded (line 24).
- **Section 5:**
  - 102 review entries, all "blocked".
  - One separate operational item, "in_progress", not conflated with the reviews.
  - The per-slot keyword counts sum to 103, consistent with the stated overlap.
- **Section 7:** 46 IDs requested, 46 returned, 46 unique; none lacks a versioned ID or an updated date. The 11:11:08/11:11:09 bracket matches, and the response hash is bound.
- **Section 10:**
  - Ledger census: 86 rows (85 slot rows plus UNBOUND row 82) and 205 hashed files.
  - Parent-record census: 450 files, class counts sum correctly, all hashed.
  - Deviation carry: 170 = 162 + 8.
- **Section 12:**
  - All 18 paths, SHA prefixes, line counts and prewrite clocks match the census and the complete-read receipt, and every mtime falls after its clock.
  - The Tuscan pre-cutoff final appears as an associated, non-cutoff record.
  - v268 cadence and memory notes match the other 15 rows.
- **Render receipt v2** matches your stated qualification:
  - 198 hrefs = 197 files plus 1 directory, the line-108 checkpoints directory — the only extensionless href.
  - Nothing missing, nothing non-absolute.
  - Both 19-row tables (4 and 7 columns) preserved.
  - Not a single-path exception.
- **Header erratum:** the hash at line 119 matches the erratum's source pin, and the report uses v4 content starting at line 121, excluding the copied header.
- **Assurance wording:** I found no claim of historical child exit, hidden cognition, continuous work or global navigation.
