# CUT-v3-erratum-v1 — edge-completeness corrections to CUT-v3 section 7 (metadata only; no statement, proof or order change)

- **Written:** `/bin/date` read at 2026-10-19T21:50:43-0700, immediately before this exclusive create. Owner SunM13MixedFibres (self-check while
  binding the part manifests; no review input).
- **Applies to:** `CUT-v3.md` (this directory) 79ae076357b751aaba56adcde2c53a19576d24fd721891328c66023da72efcfa, which stays
  byte-identical. Defect class: some section 7 input lists omitted a declared import that section 6 (or section 2) records.
  Every added input has a smaller id, so the order, the node count (79) and acyclicity are unchanged.

| # | location in CUT-v3 | correction | source of the declared import |
|---|---|---|---|
| X1 | LF196 (node 01) | "written proofs S56W section 2 LF34-48" reads "written proofs S56W section 2 LF34-65 (L0.1-L0.6, L1-L3 and K2, L3/K2 for pairwise disjoint cosets only per S56W erratum v1 item 1) and section 6 LF143-147 (R0, also node 03)". Node 01 thus contains every input of Prop 4.5 (node 09) and section 6 row 14-15's "01 (L0.1-L0.6, L1-L3, K2 with disjointness)" is literal. These S56W L1-L3/K2 are distinct from rules-k7 L1 (node 07) and from the R2 lemma K2. | S56W LF34, LF67 (section bounds), LF152, LF154 |
| X2 | LF209-210 (nodes 14, 15) | inputs read: 14 = 01, 02, 03, 09, 10, 12; 15 = 01, 02, 03, 09, 10, 11, 13 (01 added: classical Sun(2), L0.6) | S56W LF159-162 |
| X3 | LF244 (node 49) | inputs add 24 (K7 definition) | D/K7-D23-RICH-v1.md LF22-23 ("R0, K7 definition, L0.1 ... README sections 0, 1, 5") |
| X4 | LF246 (node 51) | inputs add 01 (E2, Sun(2)) and 24 (K7 definition); section 2's input list (CUT-v3 LF50-54) already names them | D/K7-D23P-v1.md LF25-26 |
| X5 | LF247 (node 52) | inputs add 01, 03, 04 (R0, E1, E2 through the RICH list) | D/K7-A1-STRUCT-v1.md LF17-18 |
| X6 | LF263 (node 68) and LF182 (section 6 row 68) | inputs add 04 (L0.3 = E1), 51 (D23P's type (b') z-row data, through the RICH/D23P verdict) and 63 (ZT5 S1-S5); section 6 row 68's inputs read "66, 67, 51, 59-65 (including 63), 16, 06, 17, 07, 04, 03, 01" | A/K7-A2-UNIT-3-v1.md LF18-20 |
| X7 | section 7 (convention, new sentence after LF278) | An input 17 (VFC (V2)-(V4) and count) includes VFC (V1) = node 05, an input of 17; an input 06 includes INV (a)-(b), E6 and E7; an input 01 includes Sun(2) (L0.6, the LFC-INV erratum E2 statement); an input 04 is E1 = L0.3. With X1-X6 and this convention, every import declared in section 6 (and section 2 for D23P) is a direct input of the module's section 7 row(s). | CUT-v3 LF199-201 (nodes 04-06), LF212 (node 17) |

Re-check of the remaining rows (section 6 versus section 7, read side by side): rows 10, 11, 16, 17, 33, 35-48, 53-57, 59-67
(module union), 71-78 and section 5 rows 24-34 already list every declared input (some section 7 rows list more, e.g. 42 adds
ROW-1 (20), 44 adds ROW-2 (22)). This is a bookkeeping finding for review, not a certification of completeness; the
withholding at CUT-v3 LF279-281 and LF296-299 stands. No full Sun(7), acceptance, novelty, Lean, human-review or runtime claim.
