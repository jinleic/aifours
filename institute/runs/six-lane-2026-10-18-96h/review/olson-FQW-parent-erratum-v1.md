# Olson FQW — parent erratum v1 (Codex m1/m2 and parent-check wording)

Recorded 2026-10-20T07:27:07-0700 (`/bin/date`). Governs proof-FQW-v1.md (9b4561780b37874c47a188fc788ae34fc223f1252f7e4bf9a1be9a6dffd09dc5) after worker erratum1 (9cf740b22a6b5f20d1562c38be4ebeedfd5b95e003542a57f71e85072f965fd5). Codex review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FQW-codex-v1.prompt.stdout.txt (7d4e54569970f6fc99a58f89379e5b827b10b889829dacb6bf99520b1142c1ca):0F/0M/2m. No main statement, used case or conclusion changes.

1. **m1 — auxiliary Lemma8(b) scope (LF158).** Add "v is EVEN". Since all labels are odd, the assumed |J0|≤2 then means |J0|∈{0,2}, exactly the cases proved. The omitted odd-v case (e.g. v1 with all positive labels) is not claimed; Lemma9(c), its only consumer, already assumes v even (LF181). This is an explicit narrowing of unused auxiliary generality, not of FQW's full target.
2. **m2 — rounding, cell(5,13) LF402.** Read m1≥(41−5t)/2≥21/2, hence m1≥11 by integrality (t≤4). The earlier chain ≥11 was false at t4, though its final integer bound was correct.
3. **Parent written-check typo.** In olson-FQW-parent-written-check-v1.md (76ee5b7f2cbe332dcf939e98f14ffd3d2727bb95035d5370b9ec0bb3b694647a), read "m1≥(5kappa−4)/2>10", not "m1>(5kappa−4)/2>10". Only m1>10 is needed for the negative-label surplus; the paper states the non-strict first inequality correctly.

No mathematical execution, no new theorem scope and no full ordered-Olson/runtime claim.
