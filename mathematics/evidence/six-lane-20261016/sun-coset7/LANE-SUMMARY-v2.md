# sun-coset7 lane summary v2 (math-1, transition 44: Sun 2006 Conjecture 1.2 at k = 7). PARTIAL

- **Freeze record:** `evidence/lane-summary-v2.sha256`.
- **Supersedes:** `LANE-SUMMARY-v1.md` (5e754ee3…5f5). v1 stays frozen and unchanged.
- **Snapshot.** State at freeze, as known to this worker. Parent verdicts are cited by their file hashes in `institute/runs/six-lane-2026-10-16/review/`.
- **Bottom line.**
  - **Accepted exclusions:** K5.2\* (including the D2′ case) and KII, by parent verdict.
  - **OPEN:** K7, K6.2\*, K6.3 and K5.3.
  - **No Sun(7) theorem.** Nothing here is claimed novel.

## 1. Accepted by parent verdicts

**Written reduction and active rules.** Verdict `sun-coset7-written-parent-verdict-v1.md`, 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35. CORRECTNESS-ACCEPTED with a mandatory overlay for:
- the README reduction to six classes (K7, K6.2\*, K6.3, K5.2\*, K5.3, KII), including D2 and D2′;
- the active rules T, K/K1/K2, P, VFC and RPLP, and CAP;
- the 5-vertex CAP hypotheses.

FH is UNUSED. The verdict itself excludes no class.

**Classes K5.2\* (with the D2′ case) and KII.** Verdict `sun-coset7-stageB-classes-parent-verdict-v1.md`, fd14952c31852fe6c9b291114f99809f090a5f3bbb0caf07065ba50fffd3c13f. CORRECTNESS-ACCEPTED as excluded, on four grounds:
- the independent checker v2 returned COMPLETE_VALID;
- a Codex static audit of that checker found it SOUND;
- the parent anchored the outputs;
- the parent re-executed the checker.

The process MAJOR F-1 remains permanent: CERT-FORMAT (13:38:43) and the RPLP addendum (14:00:41) postdate the Stage B start (13:37:15).

**K7 structure (written).** Verdict `sun-coset7-k7-structure-parent-verdict-v1.md`, 2154c317e57c84c7fbdcce65296960e5227dad423325ca9b70bcd1ceeeff0059. CORRECTNESS-ACCEPTED, with mandatory overlay, for:
- K7-TRI, K7-U, K7-TWIN;
- K7-Q in the X1 convention;
- K7-Q5 for |U| ≥ 5 only;
- K7-COV as amended by X2/X3.

It does not exclude K7. Its overlay deletes the |U| = 4 example I gave in K7-structure-v1 §5, because that example is inadmissible. It also rejects the proposed removal of all Q5 until a frozen text exists, and requires a spec v2 in the X1 convention.

## 2. Exploratory, or pending acceptance

**K5.3.** Stage A: X1, engine v1, 0 survivors (receipt 90906aa6…657c). The X1 ⇒ K5.3 bridge is accepted at written scope. The Stage A independent checker was still running at the last report.

**K7 candidates, written and not accepted:**

| file | sha256 | review state |
|---|---|---|
| `K7-block-lemma-v1.md` | 93c3cd1f…29db3 | Codex returned: K7-BLOCK (a)–(d) ACCEPT |
| `K7-pair-lemma-v1.md` | 77ce8b1b…c3d | Codex returned: PAIR (i)–(ii) and P1 ACCEPT; PAIR (iii), P2 and P3 ACCEPT-WITH-FIXES |

The Codex note on block/pair is 35612df4…6fe8. Its findings on P2:
- **MAJOR:** P2 does not cover the one-class Q23 branch. Codex gives a repair through m = 3.
- **MINOR:** declare the Sun(5) import, with 2 ≤ |T| ≤ 5.

Claude's review of block/pair is pending, and no parent verdict exists yet.

| file | sha256 | review state |
|---|---|---|
| `K7-unmarked-lemmas-v1.md` | ca80d7e5…f242 | queued |
| `K7-M-empty-status-v1.md` | 343fd617…40aa | status summary of the M = ∅ case |
| `K7-enumeration-spec-v1.md` | e5aa176b…795f | spec only; its family convention is superseded by X1, so a v2 is needed |

**Stage C (K6.2\*, K6.3): NOT_STARTED, on parent HOLD.** No smoke run has happened either. The current candidates are frozen and have never been executed:

| file | sha256 |
|---|---|
| engine v4 | 41be7774…20b6 |
| `admission_v2` | e0b6768a…52c0 |
| `stageC_launch_v4` | a0d83698…edf4 |
| `smoke_v4_v2` | 9e862e76…78f1 |
| `terminal_probe_v1` | cbefbdc4…9fe9 |

Earlier versions are NOT_STARTED and are listed in README-addenda v2–v4.

## 3. UNKNOWNs

- No executed run is UNKNOWN. Stages A and B were COMPLETE.
- No other run exists.

## 4. Deviations, each disclosed earlier and none relabelled

1. **F-1 (late formats).** The CERT-FORMAT freeze and the RPLP addendum came after the A/B starts. This is permanent, per both parent verdicts.
2. **Wrappers.** The A/B runs used `/usr/bin/time -l … | grep` wrappers, which count as extra processes under the strict count applied later.
3. **Infrastructure revisions.** Several versions were never executed (NOT_STARTED):
   - engine v2/v3;
   - admission v1;
   - launcher v1/v2/v3 (v2 broke the process cap by design);
   - smoke v3_v1.
4. **Wording errors, since corrected:**
   - "exact frontier" became "completed-profile frontier";
   - "T and K" became "T and Ppair" for the 11-type table;
   - the K7-COV hypothesis lacked VFC (X2);
   - the "exactly one" family wording (X1);
   - the inadmissible |U| = 4 example (parent overlay).
5. **Manifest self-entry.** Line 34 of `evidence/lane-manifest-v1.sha256` is a meaningless self-entry.
6. **Draft corrections.** Mis-targeted edits in unfrozen drafts were corrected before freezing. No frozen file was ever modified.
7. **Unsubmitted draft.** A lemma draft finished just before the parent asked me to stop adding lemmas. It was archived unchanged and not submitted: `archive/qsym-lemma-v1.unsubmitted-draft.md` 268605e0…ddcd, with `archive/MANIFEST-v1.md` 9315ea68…afff.
8. **Disk dip.** The parent relayed a disk dip to 11.985e9 at 14:07:50. No lane computation was running at that time.

## 5. Where the full record is

- **Lane manifest:** `evidence/lane-manifest-v1.sha256` (06648b07…4a08), as of 14:27:50. Files frozen later each have their own `evidence/*.sha256` record, listed below.

| record | sha256 |
|---|---|
| k7-structure-v1 | 1538d8ad…23cb |
| k7-block-lemma-v1 | c0c63950…e076 |
| k7-enumeration-spec-v1 | 4f07bd15…5907 |
| k7-pair-lemma-v1 | e0193b32…440c |
| k7-structure-erratum-v1 | 5cfb8437…f0ea |
| k7-unmarked-lemmas-v1 | c93b6e25…30df |
| k7-m-empty-status-v1 | 6e96e1c5…0cb4 |
| addendum-v4 | 3cf8df9d…9357 |
| lane-summary-v1 | f6c79101…8657 |
