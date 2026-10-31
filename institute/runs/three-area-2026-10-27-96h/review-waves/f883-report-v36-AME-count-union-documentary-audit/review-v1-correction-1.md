# f883 review v1 — additive correction 1

Recorded by DocF883AME36. Clock via /bin/date immediately before this write: 2026-10-31T03:27:02Z. This correction reads alongside [review-v1.md](review-v1.md), which remains unchanged.

The changes below fix citations and read-account wording only. Finding counts, classifications and verdicts are unchanged: 0 FATAL / 0 MAJOR / 4 MINOR, plus residual o1 and the reviewer process items P1/P2.

1. **m4 citation fix.** In m4, "v36 LF34 and LF40 are byte-identical to v35" means the logical lines **S4|34 and S4|40**, which are **part-02 LF39 and LF45**. The labels LF34 and LF40 were wrong: under the review's own convention those packet lines are the empty rows S4|29 and S4|35. The substance holds. The §3 `diff` shows logical lines 34 and 40 unchanged from v35. A fresh tool grep of part-02 for `[Ff]82[67]|prompt-clarity|seven direct` returns no match, so v36 says nothing about the F826/F827 ACK MINORs or the parent prompt-clarity MINOR.
2. **§2 part-02 wording fix.** The windows for S5–S8 were not all 20 LF. There were 17 windows, all ≤20 LF:
   - fifteen of 20 LF: 48-67 through 188-207, then 210-229 through 330-349;
   - one of 2 LF: 208-209;
   - one of 17 LF: 350-366.

   Total coverage and the part-02 window count of 42 are unchanged.
3. **§2 part-03 wording fix.** S9/S10 were read in ≤20 LF windows: 1-20 through 281-300 were 20 LF each, and 301-314 was 14 LF. All other part-03 windows are as stated.

Nothing else changes. All genuine held episodes AND ALL consumers remain NONINPUT.
