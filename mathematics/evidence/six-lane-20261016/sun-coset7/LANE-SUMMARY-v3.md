# sun-coset7 lane summary v3, FINAL (math-1, transition 44: Sun 2006 Conjecture 1.2 at k = 7). PARTIAL

- **Clock:** `/bin/date` read immediately before this file's single exclusive write: **Sun Oct 18 16:43:41 PDT 2026**. Absence of the file was checked at that moment.
- **Write discipline:**
  - This file is created once and then made read-only. It is the lane's only write since 14:58:16 PDT.
  - Its sha256 goes to the parent by message. A file cannot contain its own hash, and the parent asked for a single exclusive final write, so there is no separate record file.
- **Supersedes:** `LANE-SUMMARY-v2.md` (f4088aab905307fafdf2195cfb2a19a3bc402a08eada76916f285a5d7f6c0bf4) and `LANE-SUMMARY-v1.md` (5e754ee300cab6c1ffc6f5ec87d6d9441d7c40df5cf043a0dcfa098db3b3e5f5). Both stay frozen.
- **Content:** no new science or computation went into this summary. It reports parent verdicts and lane records only.

## Bottom line

- **Request:** transition 44 asked to settle Sun 2006 Conjecture 1.2 at k = 7 for every group, or to give an exact counterexample. Neither was achieved. **Outcome: PARTIAL.**
- **Accepted exclusions:** K5.2\* (with the D2′ case) and KII.
- **OPEN:** K7, K6.2\*, K6.3 and K5.3. K5.3 was not promoted (§4).
- **Not claimed:** no Sun(7) theorem, no counterexample, no novelty. Correctness, novelty and significance are kept separate.

## 1. Parent verdicts

All are in `institute/runs/six-lane-2026-10-16/review/`. Every hash was re-read at 16:43:33–16:43:41 PDT.

1. **Written reduction and active rules.** `sun-coset7-written-parent-verdict-v1.md`, 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35. CORRECTNESS-ACCEPTED with a mandatory overlay.
   - Accepted: the README reduction (Theorem R1(7)) to exactly six classes (K7, K6.2\*, K6.3, K5.2\*, K5.3, KII), including D2 and D2′.
   - Accepted active rules: T, K/K1/K2, P, VFC, and RPLP-k7 (Farkas only for the closed relaxation).
   - Accepted: CAP, with separate hypotheses for the 5-vertex universes.
   - FH is UNUSED. Subfamily pair tests need 2 ≤ |T| ≤ 6.
   - Under F-4, no run of K62, K63 or K7 is credited without its own frozen specification and parent permission.
   - This verdict excludes no class by itself.
2. **K5.2\* (with the D2′ case) and KII excluded.** `sun-coset7-stageB-classes-parent-verdict-v1.md`, fd14952c31852fe6c9b291114f99809f090a5f3bbb0caf07065ba50fffd3c13f. CORRECTNESS-ACCEPTED on four grounds, and computer-assisted:
   - independent checker v2 COMPLETE_VALID;
   - Codex static audit of that checker SOUND;
   - parent anchoring of the outputs;
   - parent re-execution with identical results.

   The process MAJOR F-1 is permanent.
3. **K7 structure.** `sun-coset7-k7-structure-parent-verdict-v1.md`, 2154c317e57c84c7fbdcce65296960e5227dad423325ca9b70bcd1ceeeff0059. CORRECTNESS-ACCEPTED with a mandatory overlay.
   - Accepted: K7-TRI; K7-U (the cut from 16 to 11 types is by Ppair, equivalently K1+K2); K7-TWIN; K7-Q in the X1 convention; K7-Q5 for |U| ≥ 5; K7-COV as amended by X2 and X3 (quantifier corrected in §2).
   - Overlay:
     - notation: h for the 5-valuation, δ for the triangle relaxation, d only for VFC local indices;
     - my |U| = 4 example is inadmissible and is deleted;
     - the d-relaxation covers triangle quantities only;
     - any K7 enumeration specification must use X1;
     - FH and the §7 leads are UNUSED.
4. **Twin blocks and twin pairs.** `sun-coset7-k7-blockpair-parent-verdict-v1.md`, cc214b588bce4cf26dae5e0c83879f7f943197f7191f9a9b0efa775ffec89786. CORRECTNESS-ACCEPTED with repairs.
   - Accepted: L6 as used; the L5 coset decomposition at subfamily sizes 2–5; K7-BLOCK (a)–(d); K7-PAIR (i)–(iii); P1–P3.
   - Repairs: an explicit Sun(5) import for m = 6 ⇒ k_4 = 3, and a direct proof of the single-class branch of P2.
   - Not accepted: a generic FH rule, any enumeration, and the proposed exclusion of s = 3 with |M| = 1.
5. **Q5 excluded.** `sun-coset7-k7-q5plus-parent-verdict-v1.md`, 38ec128d9fda84a936b4e9ffcf92e9b3b287204269b509ef4a50ea5f714b526c. CORRECTNESS-ACCEPTED: no actual K7 configuration has quotient family Q5, for any number of unmarked vertices. This holds at configuration level. The verdict also contains the controlling COV quantifier correction (§2).
6. **Unmarked lemmas.** `sun-coset7-k7-unmarked-parent-verdict-v1.md`, 463e0a45518b447207ce3416202f5cf750a07e7c147abbaf2b6ab83c87b77d85. CORRECTNESS-ACCEPTED with scope fixes:
   - narrow P2;
   - K7-HIGH;
   - K7-CLASS;
   - K7-Q23U: when M = ∅, Q23 with at least two 2-classes cannot occur;
   - the Q24 neighbour condition, which is only a necessary condition.
7. **Stage C NO-GO.** `sun-coset7-stageC-parent-no-go-v1.json`, 5cd8a2b669e9da6c3d4595b123f91ca67fdbc152a901b3be780f8ec6618fb4fd. No v4 smoke run and no K62/K63 run today.
8. **Stage A promotion held.** `sun-coset7-stageA-parent-hold-verdict-v1.md`, 10cefa4b55acebe89c16c34a93209a163f271180081d39f982b24d8d4e8e0ec1. **NOT PROMOTED: K5.3 remains OPEN** (§4).

## 2. COV quantifier correction (controlling overlay from the Q5+ verdict)

- **The error.** My erratum X2 (`K7-structure-erratum-v1.md`, f8642cb6d18877df1d4ba76c5cbe098dae6c274161f00b404abc30f76ce97138) and item 6 of the structure verdict required a pattern to "pass VFC-count at every unmarked vertex, for every admissible q". That quantifier is wrong: q ≡ 1 is already contradictory at an unmarked vertex.
- **The correct reading:**
  - a VFC **kill** requires, for **every** admissible q, a nonnegative weight vector that is feasible on every hereditary allowed subset and has objective ≥ 1;
  - a pattern **survives** iff, at each tested vertex, **some** admissible q admits no such contradiction.
- **Consequences:**
  - The abstract coverage premise is survival under this exhaustive-q kill rule.
  - Dropping Q5 from the abstract COV statement additionally requires T and Ppair on every mixed triangle {v, v′, z} with v ≠ v′ ∈ U and z not carrying marker 5.
  - Per the verdict, the correction does not alter the accepted Stage B computation, whose checker certifies every q before a VFC closure.
- **Superseded file.** `K7-M-empty-status-v1.md` (343fd617fa1f1b1758c2af1cfba86f1a7d634e7fb592bdee19162b1fdb8e40aa) is superseded by §3 below and is read under this overlay. Its q-multiset list is a hand derivation and is not accepted.

## 3. K7 structural frontier (written mathematics, per the unmarked verdict)

**Q5:** excluded for actual configurations, under any marking.

**M = ∅:**
- Q23 with at least two 2-classes: excluded.
- Q23 with one 2-class (all β = 2): reduces to the **seven-singleton all-2 pattern**, through the repaired full P2. **OPEN.**
- Q24: **OPEN**, subject to three conditions:
  - twin blocks have size ≤ 2;
  - every twin pair has at least three outsiders at α = 4;
  - every vertex has a neighbour with α ≤ 2.

**M ≠ ∅:**
- Twin blocks of size ≥ 4 are excluded.
- Size-3 blocks and the remaining marked Q23/Q24 incidences are **OPEN**.
- There is no claim that every marked configuration is feasible.

**Not accepted:**
- any exhaustive list of surviving q-vectors (the example q = (4,4,4,4,4,2) is only an illustration);
- any RPLP or Bonferroni outcome on residual patterns;
- any enumeration, count, or realizability claim.

**Required before any K7 computation:**
- a K7 enumeration specification v2 in the X1 convention. `K7-enumeration-spec-v1.md` (e5aa176b599b1fa21513bb2acaa126c8ef3863123cde2b8c7bf573fb0607795f) uses the opposite family assignment;
- a separately frozen K7 certificate format;
- parent permission (F-4).

## 4. K5.3: parent hold verdict

The verdict file is `sun-coset7-stageA-parent-hold-verdict-v1.md` (10cefa4b55acebe89c16c34a93209a163f271180081d39f982b24d8d4e8e0ec1). It reads, verbatim: "NOT PROMOTED: K5.3 remains OPEN in the accepted result ledger. X1/MSP45/CORE5 were fully verified by independent checker v1 and by a parent rerun, but the audit found a terminal-stop/publication status defect. The source repair is frozen; its required terminal controls and positive replay have NOT_STARTED because free disk is below admission. No claim that the underlying mathematics was refuted."

**Lane side:**
- Stage A ran exploratorily with engine v1.
- X1: COMPLETE, 0 survivors.
- Controls: MSP45 and CORE5 have 0 survivors; the realisable controls all survive.
- Receipt: `evidence/stageA-RECEIPT.md`, 90906aa60ac3026317af164069d2c0e22f825fc776cf789d4507d1445db4657c.
- The bridge X1 ⇒ K5.3 is accepted at written scope by the written verdict.

**Parent side, as relayed at parent clock 16:39:56:**
- The mathematical replay is complete.
- The terminal-stop fix is untested at runtime and held for resources; free space was 4,384,600,064 B.
- No further Stage A launch is authorised below the admission threshold.
- The hold verdict states the restart obligation: a fresh resource gate, the frozen terminal controls, one positive v2 replay, a parent audit, and then a NEW disposition through the accepted X1 ⇒ K5.3 bridge. None of this is scheduled or authorised.

## 5. Executed runs, UNKNOWNs, NOT_STARTED

**Executed.** Both stages used engine v1, e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d. All runs ended COMPLETE.

| stage | universes | time (PDT) |
|---|---|---|
| A | X1, MSP45, CORE5, CONTROLS | 13:35:02–13:35:05 |
| B | K52, KII | 13:37:15–13:45:02 |

Stage B receipt: `evidence/stageB-RECEIPT.md`, e044a4eba6decd3c34222e577628993f762a51b67cc63e61853f97db7ca9e074.

**UNKNOWN:** none. No other lane process ran.

**NOT_STARTED.** These files are frozen and were never executed. They are not scientific results.

Current candidates for a future session:

| file | sha256 |
|---|---|
| engine v4 | 41be7774aeb058ee02858a86a7c35799bee0ebdb8a465e90dd814feed18020b6 |
| admission_v2 | e0b6768aec643d160d4fb392b5598f6ada8ed47e22ab9ae2e469d1e4af0b52c0 |
| stageC_launch_v4 | a0d8369889213dc3f5cfc9fe3a798bf5d20cf0d8de3f0df7c50731be3adaedf4 |
| smoke_v4_v2 | 9e862e76d2d03639bbab0d0e85c5690f44cb9193424006db3f7da91f1ee578f1 |
| terminal_probe_v1 | cbefbdc42e448c9b4ab81fa54239b62ea710060b41f27d556998286d97449fe9 |
| CERT-FORMAT-k7-addendum-v1 (pre-launch overlay) | e2b097be5a4f1eed35d8cdff93ea49b5b3a4f238fd674c80d2a27386f031a677 |

Superseded:

| file | sha256 |
|---|---|
| engine v2 | 7ebb0bab09fdfe99bf016dbf0340c08148a5a61c3aa0444fc6f6e10c90f640c0 |
| engine v3 | a26e6c686c78ee25b47635c9bea84bae170ee8d74fe57d48c2c955138f8b23a7 |
| admission_v1 | f58861d8e0d90435fd2e71b92ace3561076dfb5c247525ad94a7ee0122ab2cbc |
| stageC_launch v1 | 158c074df266573451feccc20cbcb678829da531276da1349fca3ca999772db1 |
| stageC_launch v2 (three processes; non-compliant by design) | 9955a8e05265a78ba834067006356c5fee56b06c388f566464ac89d0a7d2bb4f |
| stageC_launch v3 | 4f00be287110b8155387cf8d7b2e2d0488be0a57a142c96cb62cb1dc8e03d8dc |
| smoke_v3_v1 | 36ae890fad41f1d0ee38753f649f3e757dbd2982fd5541dbd231cfcdbecfa386 |

## 6. Deviations (all disclosed earlier; none relabelled)

1. **F-1 (permanent).** CERT-FORMAT-k7-v1 (frozen 13:38:43) and the RPLP addendum (14:00:41) postdate the Stage A run and the Stage B start. These are late specifications, never retroactive preregistration.
2. **RPLP not written down.** RPLP was absent from rules-k7-v1 when Stages A and B ran. FINITE-COVERAGE §2.5 called it "transcribed", which was false at freeze.
3. **No per-node certificates.** Engine v1 stores none, contrary to the FINITE-COVERAGE §3 plan, so checkers re-walk the tree.
4. **Wrappers.** Stages A and B ran under `/usr/bin/time -l … | grep` wrappers. These are extra processes under the strict count applied later.
5. **Infrastructure.** Launch infrastructure went through several versions that were never executed (§5). Launcher v2 broke the 2-process cap by design.
6. **Wording errors, corrected by overlays or verdicts:**
   - README line 81 cited "§R" for §3;
   - L5 lacked 2 ≤ |T|, and the Farkas system was underspecified (both fixed in `rules-k7-erratum-v1.md`, 75a61776871748a53191d4d3b6fe3d4435c6b8216929a9c60067b9f28d705560);
   - "T and K" should read "T and Ppair";
   - the "exactly one family" wording (fixed by X1);
   - the VFC premise of COV (X2), and then its quantifier (§2);
   - the inadmissible |U| = 4 example;
   - "exact frontier" should read "completed-profile frontier";
   - the PAIR/P3 import range (Sun(5)) and the P2 single-class gap.
7. **Manifest self-entry.** Line 34 of `evidence/lane-manifest-v1.sha256` (06648b07baa77f4a934e1c2f6f7b7af80df956d011638464d3e25d3cbae54a08) is a meaningless self-entry.
8. **Draft corrections.** Mis-targeted edits in unfrozen drafts were corrected before freezing. No frozen file was ever modified.
9. **Unsubmitted draft.** It was archived unchanged as `archive/qsym-lemma-v1.unsubmitted-draft.md` (268605e0f1443e298b250f06d117678af95f03a94b291388dce2ce28affbddcd), with manifest `archive/MANIFEST-v1.md` (9315ea681dce334f419d4ac01246e697921f97fd3a5eb66cca207ec793dafbff). It is not a premise of anything.
10. **Disk.** The parent relayed a dip to 11.985e9 B at 14:07:50, when no lane computation was running, and 4,384,600,064 B free at parent clock 16:39:56, under the resource HOLD.

## 7. Principal lane texts (sha256)

| file | sha256 | status |
|---|---|---|
| README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | reduction accepted (written verdict) |
| rules-k7-v1.md | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | accepted with overlay |
| rules-k7-addendum-v1.md | fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066 | accepted (RPLP-k7, CAP extension) |
| rules-k7-erratum-v1.md | 75a61776871748a53191d4d3b6fe3d4435c6b8216929a9c60067b9f28d705560 | overlay |
| FINITE-COVERAGE-k7-v1.md | cbad6fdd85d27181a235231f4219df059e7f41c653e0405b152a3b0b1843e0dc | contract proposal |
| CERT-FORMAT-k7-v1.md | 2c0e483011a0ea3aace670da4b9a200ae333e676682e0e10fb47d2e584401545 | late (F-1) |
| K7-structure-v1.md | f4534c07c556557c9113c6db6106f081486316e326c6d92db3f069d5fc539fc1 | accepted with overlay |
| K7-structure-erratum-v1.md | f8642cb6d18877df1d4ba76c5cbe098dae6c274161f00b404abc30f76ce97138 | X1–X3 dispositioned; X2's quantifier corrected (§2) |
| K7-block-lemma-v1.md | 93c3cd1f2d0d41b332dc460aab33a6945e77b68202eb9e27f48b58dbd3129db3 | accepted with repairs |
| K7-pair-lemma-v1.md | 77ce8b1bd0ad2803fd3d13d09aac03456b60f887b4dd2801e7e0bfcb85b88c3d | accepted with repairs |
| K7-unmarked-lemmas-v1.md | ca80d7e5884de3831e35c1fcd69214abaef0c74d18bdd4108937094f41a3f242 | accepted with scope fixes |
| K7-Q5-strengthening-v1.md | 71705ab36d850435182c4017cec4f004a39a431de49acbb7bfa42234f1e12791 | accepted (configuration level) |
| K7-M-empty-status-v1.md | 343fd617fa1f1b1758c2af1cfba86f1a7d634e7fb592bdee19162b1fdb8e40aa | superseded by §3 |
| K7-enumeration-spec-v1.md | e5aa176b599b1fa21513bb2acaa126c8ef3863123cde2b8c7bf573fb0607795f | spec only; convention superseded |
| README-addendum-v1.md | 76056d8639f89b662f2014d5e199fe7c660bad4f3b305cb95ace3b5d1ae3193d | engine freeze; Prop 4.5 citation |
| README-addendum-v2.md | f7cd210f2c23f2c6207f39f5eb06e08a418f48bde46a4f34623520292c8f51f3 | Stage C infrastructure (NOT_STARTED) |
| README-addendum-v3.md | 8657c0d17d040a7403b19d7e4c367f5c91d18d42be77a7c576903b1ea319cfbc | sequential launcher (NOT_STARTED) |
| README-addendum-v4.md | 1ca4306caa770f4665168ec035440fab64d6fe2faecb04a9faf3f2bfff459ea3 | terminal coercion (NOT_STARTED) |

**Verification boundary:**
- The exclusion of K5.2\* and KII is computer-assisted: the lane engine, an independent checker, and a parent re-execution.
- Everything else is written mathematics, checked by the Codex and Claude reviews and by parent derivations.
- There is no Lean, no human review, and no novelty determination.
