# cpcw-optimal-prep (preparation only; created 2026-10-17 00:15 PDT by InfoCdf at parent request)

No target search has been run here. Contents:
- `sources/axioms-15-00035.pdf` (SHA-256 a105f220098e63aa7f0ecc012d2e6c21b44cf868b3d3829e136c57a65aa17080): Baicheva,
  Topalova, "On the Existence of Optimal (v,5,1) and (v,6,1) Binary Cyclically Permutable Constant-Weight Codes",
  Axioms 15(1) (2026) 35, DOI 10.3390/axioms15010035, from
  https://mdpi-res.com/d_attachment/axioms/axioms-15-00035/article_deploy/axioms-15-00035.pdf (the www.mdpi.com landing
  page returned "Access Denied"; kept as `archive/mdpi-landing-blocked.html`).
- `code/verify_cpcw.py` (stdlib): strict "CPCW v k" format, s = floor((v-1)/(k(k-1))) codewords; REQUIRES
  `--v`, `--k`, `--sha256` on the CLI and rejects any mismatch; checks distinct nonzero ordered differences (D), then
  binary auto/cross-correlation <= 1 (C) and at-most-once pair coverage of the cyclic development with exactly
  v|U|/2 uncovered pairs (P); reports the exact uncovered set U and that v/2 is in U for even v. C and P run only
  after D passes.
- `code/controls.py`: 12 published optimal codes transcribed (0 added to every codeword: Figure 1 v=43; Table A1
  k=5: 90, 103, 122, 126, 140, 152; Table A2 k=6: 106, 120, 125, 131, 150) -> all ACCEPT with their exact uncovered
  sets; 70 mutations on 5 of them (changed element, swapped elements, duplicated difference, v/2 pair, CLI wrong v or
  k, header wrong v, SHA mismatch, missing/extra codeword, repeated element, out of range, leading zero, CRLF) -> all
  REJECT for the intended check; 15 validity-preserving changes -> ACCEPT. 97 fixtures, 0 mismatches
  (`controls/receipt.json`, verifier SHA-256 85f93e8babfb45c4d6cc2924524a645da9f5df7dc582290705befebe5fce7be8).
- `notes/STRUCTURE.md` + `notes/structure-notes.json` (`code/structure_notes.py`): exact counting notes for the nine
  candidate lengths. Notes, not results.
