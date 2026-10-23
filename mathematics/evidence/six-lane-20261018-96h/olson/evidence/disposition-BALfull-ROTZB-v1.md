# Disposition: ROT-ZB v2 and BAL-full v2 after the parent verdict, v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:36:02-0700.  No frozen text is edited; this file only records how the lane
reads its own texts under the parent verdict.

- Parent verdict: run review/olson-balfull-rotzb-parent-verdict-v1.md sha256 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0
  (recorded 2026-10-19T01:34:06-0700): ROT-ZB v2 + erratum 1 and BAL-full v2 + pre-review erratum 1 are
  CORRECTNESS-ACCEPTED SCOPED PARTIALS (written).
- Reviews named there: ROT-ZB Codex 960a6033a611abe50f0afd06b5de4bb2f2de194ac07c6fd007df4a38d36af7f2, Claude
  6c1b7108365682e986eb3c6a9d60a6bae858803f44653f46a72d1b6114fc72f2; BAL-full Codex
  edfa15be1677897951754776af43091d3a6f7fba5ef975a4e13f6efb9ac8b624 (ACCEPT x4, no required MINOR), Claude
  38fad73b947e3d141bf0747652ce278659eb690af2b224fc129d35932f074dea (ACCEPT x4, 0/0/4 MINOR).
- Texts of record (unchanged): evidence/proof-ROT-ZB-v2.md 65dbedbf...f5f1 + evidence/proof-ROT-ZB-v2-erratum-1.md
  a181edbb...c0de; evidence/proof-BALfull-v2.md dffbfea8...a3e1 + evidence/proof-BALfull-v2-erratum-1.md e0f826a2...1fcf.
- The lane adopts parent overlays 1-5 verbatim in meaning: (1) the terminal residual in BAL-full erratum item 4 is
  restricted to terminal k <= p; terminal k >= p + 1 (forcing o_F >= p + 1) also remains open; a word is residual only if
  every admissible normal form lies in a residual cell (ZX overlay 2).  (2) BAL-full Remark (ii)'s example lies outside
  (S'); it only shows that 'longest' is needed.  (3) Probe consistency reads 'consistent with', not 'as predicted';
  probes are never premises.  (4) With F = o_F (mod 2) the illustrative p = 31, o_F = 30 bound is F >= 60.  (5) The
  REALIZE/ZSTRUCT extension to (S') and to every index-<1 generator is accepted through their proofs, not their original
  statements.
- Superseded lane wording: bundle v2 Sec. 4 'After BAL-full (if accepted)' now reads as accepted, with overlay 1; the
  ROT-ZB v2 cell counts remain withdrawn (erratum 1 m2).
- Accepted uniform statement (verdict wording): for every prime p >= 7, o_F <= p - 1 and F >= 2o_F - 1 imply INV* (length
  4p - 2 avoiders) and ordered Olson (length 4p - 1 words).  Not unrestricted INV*, not ordered Olson for D_2p, not the
  all-groups target.
