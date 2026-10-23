# v = 163 (k = 5) in Baicheva-Topalova, Axioms 15(1) (2026) 35: primary evidence only (no search run)

Written 2026-10-17 02:01 PDT by InfoCpcw at parent request. Source PDF: prep copy
`cpcw-optimal-prep/sources/axioms-15-00035.pdf` (SHA-256 a105f220...7080). Evidence files in this directory:
`p5r300-05.png` (page 5 rendered at 300 dpi with `pdftoppm -f 5 -l 5 -r 300`), crops `table1_crop.png`,
`table3_crop.png`, `table4_crop.png`, word boxes `axioms35-p5-bbox.html` (`pdftotext -bbox-layout`).

## What the page shows
- Caption semantics (p.5, text above Table 1 and the table footers): "A question mark means that nothing is known
  about the existence of optimal codes with this length"; Tables 3-4: "The question marks mean that we could not
  find optimal codes for these values of v and the question of the existence of such codes remains open."
- Table 1 (k=5, before the study), row 4, left to right: `145 | ? | 161 | ? | 164 | 165 | ? | 181 | 182 (struck) | ? | 185`.
- Table 3 (k=5, after the study), row 4: `145 | ? | 147-160 (bold) | 161 | ? | 164 | 165 | 166 (bold) | ? | 168-180 (bold) | 181`.
  Row 3 ends `... 141 | 142 (struck) | ?`.
- Every other "?" cell of Tables 1 and 3 stands for the maximal run of consecutive lengths not listed in another
  cell (Table 1 row 4: 146-160, 162-163, 166-180, 183-184; Table 3 rows 3-4: 143-144, 146, then the cell in
  question, 167). Normal-font (theoretical) lengths are listed as single cells (e.g. `164 | 165`, `88 | 89`).
- The length 163 appears in no cell of Table 1 or Table 3, and Table A1 (all new (v,5,1) codes of the paper,
  p.11-13) lists lengths 90-100, 103-104, 106-120, 122-123, 126-131, 133-134, 136-140, 147-160, 166, 168-180: no 163.
- The text (p.5-6) names the k=5 open lengths as "v = 143, 144, 146, 162, and 167"; 163 is not named.
- The bulleted known results (p.3-4) contain no theorem giving v = 163 (163 is prime, 163 = 20*8+3, not 1 mod 20,
  not of the forms 15p, 4p, 4up, 3^s 5 v, 5p, pq listed there).
- The later paper (Axioms 15(9) 679, `sources/axioms-15-00679.pdf`) has no statement about v = 163 (its "163"
  table row is k = 163).

## Reading
Table 3's single "?" between 161 and 164 can only cover {162, 163}: 163 is not listed elsewhere, was "?" before the
study (Table 1, same cell), and received no code in Table A1. So by the tables, (163,5,1) is open after the paper,
while the text's list omits it. This is a table/text discrepancy in the primary source; the tables, the cell
convention and Appendix A all point to 163 being an additional undecided length (s = 8, H = 81, one uncovered class,
the same "small c" pattern 20t+c, c = 3, as 143). [INFERENCE] the omission in the text is a typo/oversight; only the
authors can confirm. No search for 163 has been run in this lane (parent instruction).
