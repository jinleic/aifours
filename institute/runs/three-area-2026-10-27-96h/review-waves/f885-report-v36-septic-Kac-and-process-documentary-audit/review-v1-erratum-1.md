# F885 review — additive erratum 1 (DocF885SPRKM36)

Recorded after native observation `2026-10-30T20:37:03-0700` (`2026-10-31T03:37:03Z`). Read with unchanged `review-v1.md` (28369 B / 281 LF, sha256 `cb8d03fe74e13471e9937acf3b584dda85b7ee5cbfc89569b51cc34f47d4bb31`), which is not edited. The reviewer's own proofread found the six corrections below. None changes a finding, a classification or the reviewer count **0 FATAL / 0 MAJOR / 9 MINOR**.

1. **§1, the sentence "All of these equal the manifest pins for S1–S22", over-generalizes.**
   - The pins in the listed ranges that refer to sources S1–S22 equal the manifest pins.
   - Five pins in S8|84–147 and S9|33–84 refer to dispositions outside the packet, so they have no manifest counterpart. Their S8 and S9 copies are identical strings:
     - AME t23/t24 `4c201b80…` (S8|91 = S9|70);
     - t28 `44a750bb…` (S8|97 = S9|58);
     - t26 `67e216de…` (S8|103 = S9|64);
     - PPT exterior `5236f99e…` (S8|109 = S9|76);
     - high-defect `3a312a20…` (S8|115 = S9|82).
   - The receipt pins at S9|87–112 and the candidate pins at S9|120–169 have no counterpart in the packet and were not compared.

2. **§2.3, the timing of the clipping checks.** The tail checks did not all run right after their windows.
   - For part 01 LF1–20 and LF21–37 (lines LF8, 10, 12, 14, 21, 23, 30, 34 and 36) and for part 02 LF12, the check ran later, after part 02 LF83–95 had been displayed. Every other check ran in the same or the next tool turn.
   - That late check therefore re-displayed tails of already-read part 01 lines (at most 50 characters each) while part 02 reading was in progress. It was used only to verify there was no clipping, and it showed no new body text.
   - This is added to **P3** as a sequencing qualification. It resembles the F721 backward-part-read item recorded at S3|40 and S4|40. The parent classifies it, and compliance is not backdated.

3. **§4.3, observation 3, quotes v35 non-literally.** The literal v35 text at S3|19 is "for every integer s>=4 and every FULL complex Cartan realization". The observation stands: the v36 heading "full-Cartan" states less, not more.

4. **§4.4 lists the wrong events as new since v35.**
   - Only the F854 report-window MINOR (S5|40) is new since v35.
   - The F832 capture MINOR was recorded before v35 (S19, observed `02:31:34.384Z`) and omitted from v35 (S2|5). It is now stated in S4|19.
   - The F832 v1 pre-run design MAJOR and the F807 chronology correction were already stated in v35 (S3|32). They are carried into S4|19.
   - m6–m8 are unchanged.

5. **m4, an incomplete list of S11 links.** S11 is linked from S12|3, S12|6 and S13|3, not only S12|3 and S13|3. The conclusion is unchanged: v36 has no direct or enumerated S11 link (S4|12, S4|32), and neither does S8's `new_sources`.

6. **§6, the phrase "all outside this scope", is too broad.**
   - The v33/v34 DC-zero and F815 items lie outside this scope, as do F855's other overlaps (S1|9).
   - The v33/v34 stale-footer issue and the F807 chronology item lie inside the footer and math-3 process scope. They are prior recorded findings, which v36 correctly marks "not recounted" (S4|3), and this review does not recount them either.

The P1–P4 process items stand, with P3 extended by item 2. All genuine held episodes AND ALL consumers remain NONINPUT.
