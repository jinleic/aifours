# RUH2 review-packet delta 1: erratum 2 (Codex MAJOR 1 + MINOR 1-5 repairs)

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T17:51:29-0700. CANDIDATE_UNVERIFIED; the parent owns reviews and verdicts. Written
mathematics only; no computation, script, assertion, solver or Lean. This delta ADDS to review-package-RUH2-v1.md (SHA256
086cb82461882609522180d63c30b564cc9d7cc6cdd5be8e4dfc1a10a003785f) and its manifest review-excerpts-RUH2-v1.json (SHA256
c2238172ff26829aaeb5840336c77036337a7c2c0358695880de2ab21222bb2e); nothing earlier is edited.

New pin: erratum-2-RUH2-v1.md, SHA256 4f3308b269635c9ab2b965b0d1f56854e2d2ee47902e94c396299b02c8899dcd, read after P, PE, R, RE.
Delta manifest: review-excerpts-RUH2-delta-1.json, SHA256 6b662d1cf5702da8fe35d05ef4c2958f844048b4a8488739e63cb0971a7d1929 (1486 bytes): JSON list {path,sha256,start,end}, whole-file
SHA256, inclusive LF line ranges, absolute paths; 6 ranges: erratum 2 (whole), the Codex review (whole), proof Sec. 7
(lines 115-152), erratum 1 to the proof (whole), residual lines 25-36 (F1, F2), erratum 1 to the residual (whole). Selected raw
26257 bytes, LF-numbered 27982.

Re-review focus:
- M1: the induction on |Y|<=5 for c=9 (base l=t+1<=5; step l(Y')<=10<p; an interval containing p would put 0 in M; otherwise
  it is an integer interval in [2,p-1] that must meet B0'=[1,t_max+5] because |M|<=9 and |B0'|>=6). Consequences E<=4 and the
  E=4 shape (four consecutive empty runs, all t=1) feed the unchanged P148-151 endgame.
- N1-N3: Lemma L scope 3<=m<=5 in Sec. 7; the residue convention replacing the false distinctness sentence; the c=8 adjacent
  (1,1) pair forces only [1,7].
- N4-N5: failed-route qualifications only (toggle path unavailable at N=2e; compatibility exactly when c+2delta<=2e-4).
Not claimed: any acceptance of RUH2, KP3, KP4 or R7; anything beyond the frozen RUH2 statements.
