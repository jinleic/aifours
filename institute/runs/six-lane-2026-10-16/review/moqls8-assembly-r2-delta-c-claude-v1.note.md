**DISPOSITION: ACCEPT-WITH-FIXES** · 0 FATAL · 0 MAJOR · 10 MINOR

r2 applies all twelve r1 findings, and its narrative statuses are correct. Both new obligations are antecedents of the conditional. The defects are:
- an under-specified GB obligation;
- one table that omits a required status label;
- two wrong abbreviated pins;
- r1 guard text deleted without record.

**Basis and limits.** This is a static read of SOURCE00–05. Registry r2, r1 in full, DISP/NF2/TPL/BRIDGE/REP and the lane contract are not inlined, so DISP's quoted lines and registry-backed identities are taken as given. The brief's "per SOURCE07" has no inlined source; I checked that point against SOURCE05, the correction r2 cites at SOURCE00:347.

## 1. r1 findings → r2

| Finding | r2 at SOURCE00 | Verdict |
|---|---|---|
| m1 | :184–186, :225–236 | Applied in full. NFV pin equals SOURCE04's SHA; Claude-NF and BINDING pins equal SOURCE04:14 and :26. The six bound hashes are character-identical to r1 (SOURCE01:229–234). Statuses BOUND / PENDING / PENDING. |
| m2 | :307–316 | Applied: explicit antecedent, four templates only, superseded lines listed, the twelve keep the original contract, erratum recommended. See MINOR-4. |
| m3 | :263–296 | Applied: DISP LF40/41 verbatim; feeds bound to the S_j hash and bytes; own controls; UP-flip scope. See MINOR-3. |
| m4 | :36, :173–179, :322–327 | Applied, (a)–(d). |
| m5 | :329–342 | Applied. See MINOR-8. |
| m6 | :63–65 | Applied. |
| m7 | :101–111 | Applied; "ACCEPTED by U" withdrawn (:103). |
| m8 | :196–206 | Applied. Nit in MINOR-7. |
| m9 | :244–261 | Applied: artifact in full, field, four fingerprints, ID formula, 1765, s=1 units and s=2,3,4 tails. |
| m10 | :23–31 | Applied, (a)–(c). The set-classicality argument is correct. |
| m11 | :190–194 | Applied; matches SOURCE04:28–32. |
| Codex M1 | :9, :76–82 | Applied (wording plus three registry entries). See MINOR-6. |

## 2. Check 2 (scope and predicates): PASS, with textual defects
- The GA chain gains no new mathematical claim and no scope change.
- NF is used per C and one way (:36, :173, :325); the converse is marked load-free (:178).
- The six S_j exhaust Rep(C), and the 12+4 partition is unchanged.
- A7 is explicit and covers the four templates only (:308); the twelve stay under the original contract (:304, :315).
- The S6 predicate is quoted in full. Its S_j binding is tighter, since it adds byte count and a run-time digest.
- Weakenings are textual only (MINOR-3, MINOR-9). The new §8.2 makes unreviewed assertions (MINOR-1, MINOR-7).

## 3. Check 3 (statuses): PASS, except the D12 table rows (MINOR-2)
- BOUND (:225, :306).
- Six qualified UNSATs PENDING (:229–234). P1-B1.M2 is a non-qualifying PROOF_DIGEST_MISSING observation; P1-B3.M2 is UNKNOWN.
- The twelve direct leaves are PROOF_DIGEST_MISSING. They need fresh conforming runs or an explicit exception, and none is granted (:126, :353, :357; matches SOURCE05:7–9).
- GB has input identity only (:373, :382–389).
- Composition verdict PENDING (:236, :407).

## 4. Check 4 (gating): PASS, with content gaps
A9–A11 are antecedents (:318–320), and no conclusion is claimed (:47, :392, :409–414). With NFV LF42, no n=8 statement is licensed before both obligations are met. The gaps are in what A10 and A9 require (MINOR-1) and in the gate wording (MINOR-10).

## Findings

**FATAL:** none.

**MAJOR:** none. MINOR-5 escalates to MAJOR if registry r2 disagrees with r1 for either file.

### MINOR

**MINOR-1 — GB obligation under-specified** (SOURCE00:318–319, :349, :362, :367, :371, :382–389).
- (a) A9 and §8.1 cover "all 18" GA replays, so GB runs carry no digest obligation.
- (b) "DRAT checked by the parent checker" (:384) is a summary predicate. A summary (NFV LF37–40 against DISP LF40) is what produced PROOF_DIGEST_MISSING (SOURCE05:5).
- (c) "Every GB counterpart" (22, :384) conflicts with "every exhaustive step" (18, :362).
- (d) The bridge text omits two requirements: the §4 moves must preserve U's normal form (row-0 standard form, the (1,0) pattern, the Q1 witness) and the 42 template bits; and genuine M_s must be exactly what the GB tail means.
- (e) "Carries the same semantic 42 units and … tails" (:371) is a claim of the UNREVIEWED note (:367), stated as fact.
- (f) Independence of GB from GA is never listed as something to establish.

*Repair.* Restate A10 in three parts:
- (i) Parent acceptance of the GB note, including GB-name semantics and independence from GA.
- (ii) Either an accepted written GB bridge with the content in (d), or direct GB refutation of the four P1 templates.
- (iii) For each counted GB input, a parent replay that meets DISP LF40 verbatim:
  - feeds equal the GBBINDING hash and bytes;
  - proof-stream SHA256 and byte count recorded at run time;
  - raw logs hash-bound;
  - own controls.

Also extend A9/§8.1 to "every counted replay, GA and GB". Make the choice of exhaustive steps a parent determination. Mark the T16 orbit check (:113) and the NF finite check (:187) as supporting only.

**MINOR-2 — D12 rows lack the required label** (SOURCE00:130–143). SOURCE05:9 requires undigested results to "retain `PROOF_DIGEST_MISSING` in any final reconciliation". The Status column says only "accepted exact UNSAT".
*Repair:* change Status to "parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING". Add a "Qualified (fresh, digested)" column set to PENDING, as at :227.

**MINOR-3 — Fail-closed list shortened; SOURCE05:11 not carried** (SOURCE00:283, :285–296, :357).
- r1 also failed closed on "incomplete feed, failed control or missing parent acceptance" (SOURCE01:236), and DISP LF41 adds "unstarted". r2 drops these and never names checker rejection or a missing or mismatched digest.
- §8.1 omits SOURCE05:11's bars: weaker formula or checker, skipped cases, lost guard handling, relaxed disk/memory.
- Own controls are prescribed only for the six S_j, not for the twelve re-runs on the new relay.

*Repair:*
- Restore and extend the list.
- Import SOURCE05:11 for every counted run.
- Pin the checker to parent drat-trim `a46c0c71…8e37` or a reviewed, pinned successor.
- Apply the §6 control classes to every run on the new relay.

**MINOR-4 — When A7 counts as satisfied** (SOURCE00:44, :307–316, :406).
- The erratum is "recommended … not performed", yet it is listed as missing and pending.
- A7's reach beyond NFV LF36's literal "item 3" is the assembly's own reading.
- "Supersedes DISP LF41 / REP LF108–110" invites dropping their control clauses.

*Repair:* "A7 holds only once the parent confirms this reach, by erratum or by an explicit A11 finding. Only the 16/16-direct quantifier is superseded; the regeneration, negative-control, fail-closed, retention and floor/cap clauses bind the six S_j."

**MINOR-5 — Two wrong abbreviated pins** (SOURCE00:68, :89).
- `094dab60…3ff3c`: the full r1 hash ends `…e224ff3c` (SOURCE01:82), so the suffix is `ff3c`.
- `65311ab0…80b0`: the full hash ends `…480928b0` (SOURCE01:86), so the suffix is `28b0`.
- Abbreviation lengths are also non-uniform: `…bab` (:124), `…6e21798` (:5).

*Repair:* print both pins in full and confirm that registry r2 holds r1's values. Otherwise an accepted binding record changed after acceptance; that is MAJOR and needs re-review.

**MINOR-6 — "Pinned inline" claim vs abbreviated-only identities** (SOURCE00:9). Many new identities appear only as 8…4 abbreviations, which are not pins:
- layout.txt (:23), bind_v1.py (:225), the desk RESULT and receipts (:238–240);
- check_local_boolean_v1.py (:249), the predicate addendum (:347);
- the GB package and members (:364–369);
- GBBINDING, the manifest, the own-hash receipt and the base body (:373–378).

The audit file paths were also dropped (:145 vs SOURCE01:188).
*Repair:* print the full SHA256 of every identity not in registry r2, or register it, and say which applies. Restore the paths.

**MINOR-7 — Labels that go beyond their authority.**
- §9 lists GB input identity under "Accepted" (:399), on a PASS binding record with no parent verdict. Relabel it "BOUND (identity only)".
- "No G1 family exists" (:197) should read "none is defined in the cited sources".
- "As previously exercised by parent desks" (:289) cannot cover the digest-agreement control (:294; SOURCE05:5). Mark that control as new.

**MINOR-8 — Trust boundary incomplete** (SOURCE00:329–342).
- It omits the PRIM rules #1–#3 (LF287–302) that A1 imports (:301).
- It drops r1's "certification predicates" (SOURCE01:244). The feed-hashing relay, the raw-log parser, bind_v1.py and check_local_boolean_v1.py are all trusted tooling.
- It is silent on GB and its unreviewed bridge.

*Repair:* add all three.

**MINOR-9 — r1 guard text deleted without record.** None of these deletions was driven by a finding, and none appears in Appendix A:
- SOURCE01:8 — later receipts need a new version.
- SOURCE01:86 — the binding's scope; worker code `61eda…d400` and its receipts "do not substitute".
- SOURCE01:92 — T16 assumes no P4 on the other four squares.
- SOURCE01:100 — these are not the historical producer candidates.
- SOURCE01:225 — the rejected generator r1 is not evidence; no CNF or solve was produced.
- SOURCE01:236 — the producer lane has no S6 native role.
- SOURCE01:246 — producer counts are never relabelled as parent proofs.

*Repair:* restore each, or record it as a deliberate deletion with its reason.

**MINOR-10 — Gate wording** (SOURCE00:300, :322–327). The derivation uses only A1–A8. A9–A11 are protocol gates, and A9 is already embedded in A4/A8 via DISP LF40.
*Repair:* change "holds only if" to "may be asserted only if". Add: "No n=8 statement, including forms qualified 'modulo provenance' or 'pending GB', may be made until A1–A11 all hold (NFV LF42)."

## Verified statically
- Every abbreviated pin that has a full value in SOURCE01–05 matches it, except the two in MINOR-5.
- Deletion spacing is 1569.
- GA clause counts: 5740226 / 5740268 / 5740394.
- GB clause counts: 17025578 + 42 = 17025620, and 17025620 + 126 = 17025746.
- The SB2 cross-check decodes to 1765.
- S_j byte counts are internally consistent:
  - Same-source pairs are equal in size, because every s = 2, 3, 4 tail ID is four digits (1625–5090).
  - Across templates, the size gaps of 2, 2 and 1 bytes equal the gaps in Q1 column-0 one-counts m = 12, 14, 16, 17 (SOURCE02:211), through the negative-unit count.
  - Assuming 56 six-digit literals per deleted ALO line, the absolute sizes reconcile exactly with the 137664569 B original.

Not audited: registry contents, NF/T16/U internals, and receipt bytes.
