**VERDICT: ACCEPT-WITH-FIXES**

The four finite existence claims are correct. Every fix below concerns calibration or receipt binding; none affects validity.

**Disclosure:** I am Claude Opus 5.5, the same model that wrote `cdf-claude-verifier-v1/checker.py`. My audit of that file is therefore not independent of its authorship. The hand check in §1 uses no code.

## 1. What I verified

**Bridge argument: correct.**
- **Pair coverage.** Take x ≠ y. The unique triple (i, a, b) with a−b = x−y gives the translation t = x−a = y−b.
  - Suppose {x, y} ⊆ B_j+s. Then (x−s, y−s) is an ordered pair in B_j with the same difference, so (j, s) = (i, t).
  - It follows that translates are pairwise distinct, since two equal translates would share a pair. That gives v(v−1)/20 blocks covering v(v−1)/2 pairs, each exactly once.
- **Stabilisers.** If B+t = B, then B is a union of ⟨t⟩-cosets. So |⟨t⟩| divides both 5 and v, and gcd(5, v) = 1 forces t = 0.
  - Equivalently, a nonzero t would occur 5 times as a difference.
  - Divisibility of v by 3 or 27 is irrelevant here, because a short orbit needs a subgroup of order 5.
- **Correlation.** If |B_i ∩ (B_j+s)| ≥ 2, then (x, y) and (x−s, y−s) are two ordered pairs with equal difference. They are distinct whenever i ≠ j or s ≠ 0.
- **Negation and translation.** Both preserve a block's difference list, because each block's ordered difference list is closed under negation.

**Checkers: no acceptance gap in `check_cdf_independent.py` or `checker.py`.**
- **Parsing.** Both split on `\n` only, so CR, TAB, VT, FF and stray spaces all fail the canonical-integer regexes. Both reject out-of-range and repeated elements and require exactly (v−1)/20 blocks.
- **Binding v and k=5.** The parent `main` rejects on `v != expected_v or k != 5`. `checker.py` compares the header string against the canonical `EXPECTED_V` and requires `toks[2] == str(K)`.
- **Hashing.** Each checker hashes and parses the same single read, and the SHA comparison is exact.
- **Failure handling.** Decode errors fail closed. `sys.exit` raises SystemExit, which `except Exception` does not catch.
- **Arithmetic.** Residues come from Python `%`, so they lie in [0, v). Differences are taken over ordered pairs of distinct positions, and each of 1..v−1 must occur exactly once.
- **Lenient lines.** Both accept comment and blank lines, which is harmless under SHA binding.
- **Provenance.**
  - The checker hashes recorded in every receipt match the audited files.
  - The parent controls (22:42:47) predate the first certificate (22:59:50).

**Hand verification (no code).**
- For each of the four displayed main certificates, I computed all 10 within-block differences of every block and reduced each to its class {d, v−d}.
- Every class 1 ≤ d ≤ (v−1)/2 occurs exactly once: 160, 250, 310 and 340 classes respectively.
- This includes the class of v/3 (107, 167, 207, 227) and, for 621, the multiples of 23 and of 27.
- Because v is odd, d ≠ −d, so this is equivalent to the ordered-difference condition.
- Headers, block counts, ranges and distinctness are all correct.

**Scope.**
- **Uncovered orders.** Using only the ACF 2004 excerpt:
  - There are 31 composite v ≡ 1 (mod 20) with v ≤ 1001.
  - 25 of them are covered by v = 21, §3 Types 1–3, or Theorem 13.
  - The remaining six are exactly {321, 501, 621, 681, 801, 901}.
  - This confirms reading the OCR's "∈" in Theorem 14 as "∉".
- **Index mapping.** The t↔v mapping (t = 16, 25, 31, 34) is correct.
- **Definitions.** The DF definitions in ACF §3 and in BT 2026 p.2 match the checked object.
- **What is open.** Only cyclicity: an S(2,5,v) exists for every v ≡ 1, 5 (mod 20) (Hanani). Downstream text must never drop "cyclic" or "strictly cyclic".

## 2. Fatal findings

None.

## 3. Major finding

**M1. The gate is claimed before the cross-vendor review existed, and which frozen target it satisfies is not shown.**

Locations: the final **FRONTIER** line of `00-cdf-k5-parent-verdict.md`, and the Status cell of the info-2 row in `01-outcomes.md` ("meeting the contract's finite-target gate").

- **Review substituted by a checker.** The ledger defines the gate as requiring a cross-vendor *review*. FRONTIER substitutes "independent verification with a cross-vendor checker", and no review existed in this snapshot.
- **Set vs. per-order target.** The info-2 Target column freezes the six-order set. "Complete solution" therefore holds per order, not for the frozen slot target.
- **Freeze timing unshown.** Neither the contract clause nor the CDF freeze time (`transitions.json`) is in the snapshot, so I cannot confirm the target was frozen before the 22:59:50 discovery.

**Fix:**
- Write: "meets the finite-target gate per order (each order is separately named as a possible exception in ACF 2004, HBT and BT 2026); cross-vendor hostile review: ‹this review›, ACCEPT-WITH-FIXES."
- Cite the contract clause that permits per-order targets, and the freeze timestamp.
- If the frozen target is in fact the set, write "4 of 6 frozen target orders complete" instead.

## 4. Minor findings

**m1. Incorrect count.**
- **Where:** `01-outcomes.md`, Next actions item 6, says "Construct the six remaining…".
- **Fix:** "the two remaining orders, 801 and 901".

**m2. Parent-checker runs are not bound to the pinned files in receipts 08–10.**
- **Where:** receipts `08`, `09` and `10` record the parent checker only as `parent_rc`/`parent_status`.
  - They give no certificate path, no expected-SHA argument and no output JSON.
  - Receipt `07` does carry `certificate_sha256`.
  - Only the Claude checker's stdout binds the bytes.
- **Missing artifact:** `cdf501-alt-parent-verification-v1.json` is cited but not included.
- **Untested branches:** the parent controls never exercise `main`'s rejections for SHA, v or k≠5. The `wrong_v` control actually hits the block-count check. These branches are correct by inspection.
- **Fix:** add the parent output JSON paths and hashes to each receipt, pin the 501-alt JSON, and add `main`-level controls.

**m3. Worker-verifier claims are unbound.**
- **Code:**
  - `verify_cdf.py:main` takes no expected v, k or SHA.
  - `parse()` accepts any k; for example, a trivial (321,2,1) family would be ACCEPTed.
  - This is the only genuine binding gap I found, and it is confined to the third implementation.
- **Receipts:** no worker report is in the snapshot.
- **Claims:**
  - The verdict says "ACCEPT for all four orders" and "All three read the same pinned bytes", but the receipts list worker-tree source paths.
  - The ledger says "accept every pinned witness".
- **Fix:** pin the worker JSON reports showing sha256, v and k=5 for each witness. Otherwise narrow the wording to "two parent-executed checkers accept every pinned witness; the worker verifier reported ACCEPT on the four main certificates (not parent-replayed)".

**m4. Correlation attribution and hard-coded constants.**
- **Attribution:** the verdict's 321/621/681 rows credit "correlation 1" to both checkers, but `checker.py` checks only differences and pair coverage.
- **Constants:** `check_cdf_independent.py:77-78` returns `differences_once: v-1` and `max_correlation: 1` as constants once the threshold checks pass. Both values are true by construction, but neither is measured.
- **Fix:** attribute each statistic to the checker that computes it, and rename the field to `correlation_le_1: true` or compute the actual maximum.

**m5. Reproduction gap.**
- **Where:** the ledger's Reproduction block has no CDF commands.
- **Fix:** add both parent-executed commands for each pinned witness, noting that the parent checker refuses to overwrite an existing output path.

**m6. Prior claim omitted from the ledger row.**
- **Where:** the info-2 row says no earlier "construction or nonexistence claim" was found.
- **What's missing:** it omits the only prior claim that touches the claimed orders. The 1996 Handbook listed 501 and 681 as known, and ACF 2004 (same first author) called that listing incorrect.
- **Fix:** add one clause; the verdict already states this.

**m7. Gate terminology is inconsistent.**
- **Where:** the headline says only Mathematics met "the contract's breakthrough gate", while the info-2 row claims "the finite-target gate".
- **Fix:** define the gate once. After M1, either add one calibrated headline sentence for info-2 ("modest specialist finite cases") or state why info-2 does not count.

**m8. HBT sourcing.**
- **Locator:** the verdict cites HBT "§1"; the priority audit quotes "p.114".
- **Provenance:** the verdict says "read by the parent", but only the *Axioms* excerpt is pinned.
- **Journal title:** I believe it is *J. Algebra Comb. Discrete Struct. Appl.*
- **Fix:** pin a parent-read HBT excerpt with page number and quotation.

## 5. What I could not verify

- **Hashes of the displayed text.** I cannot confirm that the displayed certificate text hashes to the pinned SHA-256 values; my hand check binds only to the displayed blocks.
- **Alternate witnesses.** The 501 seed-2 and 321 seed-2/3 witnesses are not displayed.
- **Worker-lane evidence.** The worker verifier's runs, its 24/117 control suites, the byte-exact 321 replay, and the discovery times.
- **Receipt authenticity.** I also cannot see the prompt receipt behind "from the definition alone".
- **Missing project files.** `contract.json`, `transitions.json`, and the multiplier-audit JSONs. The multiplier audits are correctly marked as not load-bearing.
- **Unread literature.** The HBT text, Handbook 1996 Remark 4.10.18, Handbook 2007 §VI.16, and the paywalled sources.
- **Robust SPR.** The Robust SPR portion of the info-2 row; it makes no positive claim, and the snapshot contains no evidence for it.

## 6. Minimal defensible theorem

**Theorem.** For each v ∈ {321, 501, 621, 681}, the (v−1)/20 base blocks in the pinned file listed below form a cyclic (v,5,1) difference family in Z_v:

| v | SHA-256 of pinned file |
|---|---|
| 321 | `0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b` |
| 501 | `517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74` |
| 621 | `257d85f25cd85afc06f6762f1a8f7d4f72e37cbfde806927838f1ac6b7ae05f5` |
| 681 | `16af75391a6b01bd6fc7ee8ec45bd3b53396bd72403e667297af89c1dc09f7b7` |

Hence, for each such v, the following also exist:
- a perfect (v,5,1) optical orthogonal code, with (v−1)/20 codewords and all periodic correlations ≤ 1;
- a strictly cyclic S(2,5,v).

**Corollary.** This is conditional on ACF 2004 Theorem 14 and the prime case it cites. For v ≡ 1 (mod 20) with v ≤ 1001, existence of a cyclic (v,5,1) DF is undecided at most for v ∈ {801, 901}.

**Not claimed:** priority, "first", a new method, any infinite family, or completion of the spectrum up to 1001.

## 7. Promotion verdict

- **Correctness: ACCEPT.** The support is two audited checkers plus a code-free hand check of the displayed certificates.
- **Bounded novelty: NOVELTY-UNCLEAR.** The correct wording is "no earlier construction located in a bounded search".
- **Significance:** modest, specialist finite results that close four of the six named possible exceptions. Novelty and significance are stated separately and not conflated; I found no "first" claim and no method overclaim.
- **Gate:**
  - **Now:** promote to "certified finite cases; cross-vendor hostile review ACCEPT-WITH-FIXES".
  - **Next step:** promote to "finite-target gate met (per order)" once M1 and m1 are applied.
  - **Non-blocking:** m2–m8.
