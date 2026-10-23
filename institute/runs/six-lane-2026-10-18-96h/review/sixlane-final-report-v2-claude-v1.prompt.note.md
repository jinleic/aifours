# Second-family consistency review: continuation report v2

**Basis.** I used only the pasted text, with no tools.

Abbreviations:
- R = report v2
- F2 = frontier v2; E1 and E2 = frontier errata v1 and v2
- D = disposition JSON
- O6 = outcomes-v6
- S7 = Sun7 verdict
- U = UFC verdict
- C2 = FC1023 v2 confirmation
- G1–G3 = cadence-gap records v1–v3
- PR = priority refresh JSON
- Q15 = queue v15

**Errata applied.** E2 governs E1, which governs F2. C2 governs FC1023 v1.

**Not applied (cited but not pasted):** UFC erratum v1, the FC717 errata, and the FQW, K0T, BOTTOM and PP1-EXCL verdicts.

**Method.** Arithmetic is limited to evaluating the records' own scope formulas. There is no proof re-derivation and no enumeration.

## Counts: FATAL 0 · MAJOR 2 · MINOR 6

No report-level status statement is false. Both MAJORs are about support or scope, not correctness. No computation is relied on: U LF22 says none was used, and S7 LF22 says no computed-coverage premise is operative. Priority issues are limited to min-5.

## MAJOR

**MAJ-1. A binding misapplication survives in the cited p=23 union, and the repair records certify it as correct.**
- **Type:** citation/bookkeeping; items (a), (b), (g).
- **Defect.** F2 LF15–17 (p=23) reads:
  - `5 | FCW (p=4·5−1)`, which evaluates to 19;
  - `6 | TCW (p=4·6−5)`, which evaluates to 19;
  - `7 | SCW (p=4·7−3)`, which evaluates to 25.

  None equals 23. SCW and FQW always give p≡1 (mod 4), so neither can apply at 23≡3. Under R LF21, using E2 LF12–13's convention that each family covers the cell kappa_hat=κ, FCW at p=23 is κ=6 and TCW is κ=7.
- **The governing chain certifies these rows:**
  - E1 LF5 keeps them ("No other row changes").
  - E2 LF19 says "Bindings elsewhere in frontier v2 … are confirmed correct".
  - D LF25 says "frontier labels confirmed correct".
  - R LF37 cites exactly this chain for the p=23 union.
- **The same defect existed at p=29.** F2 LF31–32 had `4·8−1` and `4·9−5`, both equal to 31. E2 LF12–13 replaced these silently, and the "Corrections made" list (E2 LF19) does not mention it.
- **Consequence.** Three cells of a headline closed row are cited to verdicts whose literal scope excludes them. The closure itself still holds from R's own scopes:
  - (5,23) is in USK, since floor(22/4)=5.
  - (6,23) is FCW, since 4·6−1=23.
  - (7,23) is TCW, since 4·7−5=23.

  The open set does not change. This is the first-family M2 defect class, repaired in R but not in the frontier.
- **Minimal repair:**
  1. Issue frontier erratum v3 with p=23 rows "3–5 USK; 6 FCW; 7 TCW", and record the p=29 rows 8–9 re-attribution.
  2. Withdraw the E2 LF19 sentence "elsewhere … confirmed correct" and amend D's M2 line.
  3. Add to R LF21: "each family excludes the single cell kappa_hat=κ".
  4. Cite erratum v3 in R LF37.

**MAJ-2. An unresolved qualifier sits on a component of every closed row.**
- **Type:** scope/missing premise; item (e).
- **Defect.** R LF25 reads `K0T | kappa_hat=0, every odd p (relative to Theorem P)`.
  - Theorem P is not identified, linked or given a status anywhere in R or the pasted records.
  - It is not in the LF7 permitted-import list, which names only Zhu Sun(3)/Sun(4).
  - K0T is the only scope covering kappa_hat=0 (R LF25–30), so every closed row uses it.
  - Yet R LF19, LF32, LF33, LF35 and LF37 state the closures without qualification, and F2 LF13 and E2 LF9 also drop it.
- **Consequence.** A consumer cannot tell whether the six closures are unconditional (at the NF antecedent) or relative to an unaccepted premise. Under the governing rule, the six-row closures remain conditional on Theorem P.
- **Minimal repair.** Add one line at LF25 naming Theorem P's record and acceptance basis, or add it to LF7 as an import. Otherwise, qualify all six closures as relative to Theorem P. This finding downgrades to MINOR if Theorem P is an accepted local theorem and R says so.

## MINOR

**min-1 (c). The U0/UFC statement is still not self-contained.** Type: completeness/wording.
- R LF34 gives the domain only as "the middle range". U LF7 defines it: T is prime p≥17 with floor((p+7)/4)<kappa≤(p−3)/2.
- R LF34 omits U0's premise "with accepted UMR's identity" (U LF7, LF22).
- "E0/ENV valid on the whole range" drops "at their stated scopes" (U LF8).
- U1 "lands in R_U" should read "induces data in R_U" (U LF9).
- R LF39 says "no … necessity claimed", which reads against LF34's "U1 … necessary only". U LF14 has the same tension, and its governing erratum v1 is not pasted.
- R LF21's antecedent omits "original-index identity-2p-subword" (U LF7). That ordering constraint is what §2's "in some order" contrast depends on.
- Correctly stated: the T0 bounds, kappa_hat=kappa, and the named cells (U LF10).
- **Consequence:** the domain must be inferred, U0's dependence on UMR is hidden, and LF34 and LF39 appear to contradict each other.
- **Repair:** transcribe U LF7–10 and reword LF39.

**min-2 (d). The deviation list is not "complete" as LF49 claims.** Type: process only.

The cadence durations, endpoints and stale checkpoints 107/116 are exact (G1 LF5, LF7; G2 LF3; G3 LF3, LF5). The list omits:
- the F2 p=29 misstatement (LF33–38), its propagation (E1 LF5; O6 LF10, LF17) and its E2 repair. This is the same class as items LF56–57. The MAJ-1 repair should also be recorded once made.
- the "original 217.8KB final packet" NO_VERDICT run from LF15. Item 3 (LF53) names only P1/P1A, so either add it or say which of those it was.
- U LF22's qualification "worker authored UMR/FC717/FC19". FC717 is also missing from LF54's inheritance list with no explanation.

It also has two inconsistencies:
- Item 9 (LF59) declines to enumerate earlier deviations, but O6 LF31 says "the final report must enumerate them".
- LF52 says finished outputs waited only during gap v2. They also waited during v1 (FC19 at 10:39:08 and CK62 at 10:51:47; G1 LF7) and v3 (UFC Claude at 22:52:48; G3 LF3).

**Repair:** add the missing items, reconcile LF59 with O6 LF31, and annotate all three gaps or none.

**min-3 (e). Inherited components are not given a trust basis.** Type: trust/provenance.
- LF7 scopes the trust model to new acceptances only. R does not mark which §1.2 and §1.3 components are pre-window, or what their acceptance basis and provenance flags are. The same applies to the Sun7 inputs R0, WR COVER/D2/D2′ and written Prop4.5 (S7 LF11).
- Q15 carries unlaunched Claude prompts for olson-RUH2 (LF96–101), D1END (LF144–149) and ROT-PP1 (LF150–155). R nowhere states that BOTTOM or PP1-EXCL (LF30) are independent of these.
- S7 LF27 ("RES-1..6 … discharged or explicitly permitted") and S7 LF22 ("no computed-coverage premise is operative") are missing from LF17. As a result, "permitted" is never bound to LF7's import list.
- **Consequence:** if any cited verdict depends on an unlaunched review, the dependent closures become conditional, and this finding would escalate to MAJOR.
- **Repair:** add a one-line inherited-basis statement per lane and "no cited verdict depends on a READY_FROZEN prompt", and carry S7 LF22 and LF27 into LF17.

**min-4 (f). Some status language goes beyond the snapshot.** Type: wording.
- LF17 says "runtime HOLD continues to the deadline", which is a forward claim. It should read "observed through the snapshot; re-verified at freeze".
- LF19 says "proved". Per LF7's convention it should say "accepted (written)".

**min-5 (g). Citation defects.** Type: citation/priority.
- **Queue path.** LF58 links `…/review/second-family-review-queue-one-third-v15.json`. The pasted record is at `…/control/…`, and Q15 LF5's own lineage is in control/. No review/ copy is evidenced.
- **Queue count.** "14 … cross-domain reviews" matches the 14 entries in Q15 LF77–162. However, entry LF78–83 (sun7-CUT2-M12-claude-v1) is a Sun7 prompt superseded by the compact Claude review (S7 LF17; Q15 LF60–63 lists CUT2_M12 as completed). The accurate description is 13 outstanding plus 1 superseded, as of 2026-10-20T20:18:24.
- **Primary sources (LF47).** There is no link to the record. PR contains neither "feed updated 2026-10-21T03:50:41Z" nor "Conjecture 5.1 still open in source"; PR LF30 only retains a notev7 reading.
- **PA19 (LF43).** "current_counts_parent" is unlinked; O6 LF20 binds it to pa19-parent-frontier-v11.json.
- **Consequence:** D LF25's "queue/primary citations pointed at literal records" is not yet true.
- **Repair:** fix the path, restate the count, link PR (or notev7) and link pa19-parent-frontier-v11.json.

**min-6. Supporting records still contradict the corrected state.** Type: record hygiene.
- O6 LF10 and LF17 still read "p29 kappa_hat13,14 open", citing E1.
- F2 LF42 calls the FC717/FC19 cells "j≤2v−2". E2 LF23 subtracts them from the outside-T0 set "for p≥23".
- By U LF7, (7,17) satisfies 7≤56/8, and (7,19) and (8,19) satisfy ≤64/8, so all three lie inside T0. Both primes are also below 23. The complementary strip is therefore empty at p=17 and p=19, and those cells are covered twice.
- **Consequence:** the open set does not change, but navigation readers get a contradictory p=29 status and a wrong picture of where the strip lies.
- **Repair:** issue outcomes-v7 or a supersession note, and fold the LF23 wording fix into erratum v3.

## Claim-wise verdicts

| Claim (R LF) | Verdict |
|---|---|
| Sun7 statement (LF11) | Consistent with S7 LF7. |
| Sun7 chain and counts (LF15) | Consistent with S7 LF11 and LF16–19. "All inside this window" cannot be verified from the paste. LF15 says "K62" where S7 says "K62X". |
| Sun7 non-claims (LF17) | Consistent but incomplete (min-3, min-4). |
| Bindings (LF21) | Consistent with E2 LF12–13 and LF19. The κ minima are consistent with the p=11 and p=13 rows. The cell convention is not stated (MAJ-1). |
| p=29 open at exactly 12,13; 14 in BOTTOM (LF39) | Consistent with E2 LF9–17. (11,29) is covered by the uniform U0 statement even though U LF10 does not name it. |
| p=7, 11, 13 closed (LF37) | Consistent from R's scopes. At p=11, FCW (κ=3) and TCW (κ=4) cover the cells, so H11 is not needed. FQW LF9 is not pasted. Conditional on Theorem P (MAJ-2). |
| p=17, 19 closed (LF32–33) | Consistent; these cells are also inside U's T0. Conditional (MAJ-2). |
| p=23 closed (LF35, LF37) | Correct from scopes, but the cited union misattributes rows 5–7 (MAJ-1). FC1023 is genuinely needed, since 10>9.5 puts (10,23) outside T0. Conditional (MAJ-2). |
| UFC row (LF34) and HIGH-COVER (LF39) | Bounds, U1 and named cells are consistent with U LF7–10 and LF14. Wording is incomplete (min-1). |
| Trust model (LF7) | Holds for the in-window acceptances shown (U LF18–20; E1 LF3 with C2 LF3; S7 LF15–19). Scoping gaps: MAJ-2, min-3. |
| Other lanes (LF43) | Consistent with O6 LF18–21, including 70+58=128. Unlinked (min-5). |
| Primary sources (LF47) | Versions and quotes are consistent with PR LF13–49. Unlinked, with two unsupported details (min-5). |
| Deviations (LF51–59) | Cadence entries exact; list incomplete (min-2). |
| Snapshot language (LF3, LF63) | Consistent; residual issues at LF17 and LF19 (min-4). |

## Repair-map check against D LF25

| Disposition item | Status |
|---|---|
| M1 (p=29 row) | Repaired. |
| M2 (bindings) | Repaired in R. The "frontier labels confirmed correct" certification is false (MAJ-1). |
| U0 statement completed | Partial. |
| Parent-hint exposures added | Done. |
| M1-repaired history recorded | Done. |
| Cadence endpoints corrected | Done. |
| Trust model scoped | Partial. |
| Snapshot language qualified | Partial. |
| Kernel-loss count cited | Cited; the records are not pasted. |
| Queue/primary citations pointed at records | Not done. |

## Notes (not counted)

- LF3 says "no external contact", while §2 relies on public Atom-API and search reads (PR LF9, LF42–47). LF3 should say these were read-only queries.
- The v2 gap interval contains parent writes at 20:51:53 (PR LF2) and 20:57:44 (G2 LF3). R matches G2's checkpoint-to-clock measurement, which is a different measure from the no-action intervals in G1 and G3.

## Freeze verdict

**Not freeze-ready as frozen.** There is no FATAL finding, and no report-level status is false: p∈{7,11,13,17,19,23} closed and p=29 open at exactly kappa_hat 12,13 agree with the literal scopes, subject to MAJ-2.

Required before freeze:
1. MAJ-1: erratum v3, the D amendment, and the LF21/LF37 edits.
2. MAJ-2: a Theorem P status line, or qualified closures.

The minors are wording, citation and record hygiene. No new mathematics is needed, and a delta check of the repaired lines is sufficient.

This review approves only report consistency at the cited scopes. It approves no research target or runtime, and makes no Lean, human-review, novelty or priority claim.
