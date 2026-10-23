# FCS checkpoint 001 — scope frozen; site enumeration in progress

- Written: `/bin/date` read at 2026-10-19T21:24:52-0700, immediately before this exclusive create. Slice start 2026-10-19T21:14:02-0700;
  scope frozen 2026-10-19T21:19:15-0700 (FCS-SCOPE-v1.md, sha256 32ee3245a9a92471fc8134b291d22d5566e6cfe284f86d72deb15870a80c4b07).
- Eval kernel was lost once (21:18) before any file existed; helpers re-created; no partial write.

## Actual result so far (search ledger, read-only grep + context reads; no derivation)
- Universe searched: O16 README/rules-k7-v1/addendum/erratum; written verdict 73a25ba6; LFC/INV v1+erratum and verdict;
  M1, Z2, K7-35, K63-D, K63-E (+errata); all k7-k62-residue texts; K63-RES (+errata, verdict); K62 E3/DG/SH-DG/CAP/CAP-DT/
  M13-A/SETTING; K62-FULL (+errata); A2X units/scope (+parent errata); K7-NF (+parent errata); SUN7-COMP-v1 (+errata,
  COMP-U0 erratum); C5W, C56W, K52-W, KII-W, X1 candidate/clarification; old Sun(5)/Sun(6)/StageB verdict scopes.
- Theorem-statement sites found: README R1(7) step 1 (LF61, Sun(6)) and step 3 (LF63, Sun(5)); README import list LF13-17;
  README deletion LF25; rules-k7-v1 LF13 and VFC (V3) LF43/46 with verdict LF34; LFC (c) LF42-43 with imports LF12-14.
- |T|=5/6 instance sites (route through LFC (c)/VFC (V3)): ROW-U R5/R24 (LFC LF89-101, E8); K63-U0 step 2 (not in final
  K6.3 partition); K63-E D-ROW (LF25-31); K63-RES case (1c) x_*=5 (LF140-143; erratum v2 X8: the load-bearing Sun(6));
  A1-STRUCT two/four 'no 5-set' (LF28-29, LF89-90; OV1 A1.4/A1.10). RICH-v1 LF96-97 direct Sun(6) was withdrawn by its
  mandatory erratum-1 R-1.
- Internal-lemma sites: README L0 proofs (LF21) -> S56W section 2; Prop 4.5 (README LF19/LF79) -> S56W section 3;
  [GEN] VFC (V2)/(V4)/(V3) proofs (rules-k7-v1 LF46 cite old proof-v4 section 5 and proof-k6-lemmas) -> written verdict
  73a25ba6 LF34 with mandatory overlay item 3; L4/L5/CAP/RPLP (old k6 rule citations) are outside the final proof-use
  closure (DROP).
- K5.2*/KII sites: SUN7-COMP-v1 LF53, LF91, LF112 and status lines; README LF94/LF96 class definitions vs K52W verdict LF9
  and KIIW verdict LF5 (scope match to be written); D2' stays the written COVER removal (COMP LF44).
- Written branches C5W/C56W/K52W/KIIW/X1 confirmed free of Sun(5)/Sun(6) by their own boundary lines.
- No genuine gap found yet; none certified.

## Next
Write FCS-SITES-v1.md (site table with ambient group / inversion / deletion / cofactor conditions / needed lemma / status,
replacement map, gap list, Appendix A ledger), then the excerpt manifest and review package (<= 100 KB), final checkpoint,
IRC to Main, park.
