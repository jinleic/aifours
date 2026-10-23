# README addendum v4: record closure for k = 5

The host-clock freeze record is in `evidence/proof-v4.sha256`. Earlier README files stay frozen.

1. **Text of record.** It is now `proof-v4.md`.
   - proof-v4 restores the full derivations that proof-v3 had abbreviated: Lemma R (R1)–(R3), the repaired (R5′), the step from certificates to impossibility (M1, M2), the closure of the theorem, and the S-D derivations.
   - It writes out every inversion used in Lemma K.
   - It contains no new mathematics.
   - The cumulative erratum is `rules-v1-erratum-v3.md`.
2. **Wording.**
   - The result is a **locally written candidate proof of a previously claimed case**.
   - This run has published nothing.
   - **[NEW]** means "written in this lane", not novelty.
3. **Priority.**
   - Z.-W. Sun reports that **Z. Gong** confirmed k = 5 for general groups. The reports are MathOverflow Q316709 (2018) and slides Cover-Z+G.pdf (2024), which give the years 2009/2010.
   - No public proof was located. That is a search miss. It is neither a novelty claim nor evidence that the thesis was never refereed.
   - README-addendum-v3 wrote "Zhu Gong". Read that as "Z. Gong", to avoid confusion with W.-J. Zhu (2008).
4. **Verification status.**
   - The parent bridge replay passed: verifier 2d7fff78…7659, RESULT d741396c…7278.
   - The lane's `core5_check_v2.py` is a self-report. Its 60 RSD kills are the 60 labelled S-D triples. The parent bridge lists the same 60 as SURVIVE, because it has no Lemma R rule. Both then rely on proof-v4 §6.
   - Hostile reviews:
     - Codex and Claude reviewed v1 and both returned ACCEPT-WITH-FIXES.
     - Codex and Claude reviewed the v1→v3 delta and both returned ACCEPT-WITH-FIXES.
     - No review found a FATAL or MAJOR issue.
   - No Lean check. The gate is not claimed. The parent issues the correctness verdict.
