# RUH3 review package: R-UH for every 5<=e<=(p-1)/2 (closes RUH2 residual R2 and most of R1) + exact residual e=(p+1)/2, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T18:17:35-0700. CANDIDATE_UNVERIFIED written proofs; outcome = R2 CLOSED, R1 PARTIAL
(closed except the boundary e=(p+1)/2), with an exact residual. The parent owns both-family reviews and verdicts. No
scientific computation, enumeration, script, assertion, solver, model CLI, test/build or Lean; all case work by hand. No
novelty/priority/"first"/human-review claim. RUH2 and its errata (including the separate erratum-2-RUH2-v1.md repair) are
NOT cited; everything used from RUH2 is re-proved in R3.

## 1. Review exactly these frozen texts (directory upperhalf-RUH-round3/)
- proof-RUH3-v1.md ("R3"), SHA256 027ac177c9b14e76ef86d1f0c881629eb1011f1dec32c9570f48be7e0b626b31, lines 1-234 (22,015 bytes): SH range.
- proof-RUH3-ext-v1.md ("R3-ext"), SHA256 0c4efe594bde2c6c3afe2916048d52beb36b9b296b6c6d0f545c4729d96feecd, lines 1-110 (9,268 bytes): e<=(p-1)/2; read with R3.
- residual-RUH3-v1.md, SHA256 38c6d830174da3e78c8b8bf4c2b2920ed057afebd9aeb6a4e63c0c9447e3b283, with erratum-1-residual-RUH3-v1.md, SHA256 79db2b2fbdefe3ff26728731dc5eecd5e7496e2c6131764e043c618c64510ed6.
- Scope RUH3-scope-v1.md, SHA256 c6601f27ab4b1752b7d76ae769c1c1229160367b20b8da0ba4ab60a138815bbb, frozen 17:30:02 BEFORE
  derivation, with pre-freeze exposure disclosed. Authority RUN/control/written-slot-transition-olson-20261019-1730-v1.json,
  SHA256 b95a3c222c5d95faf838ce9db98e6e94050196bc6b6f6366339922f311755455, key math2.
Claims (full NF antecedent: some admissible NF of a length-(4p-2) avoider has terminal k=p+1, kappa^=kappa; H^=e-1 anywhere in
the odd blocks; empty runs separate different values; no o_F/run/pair hypothesis):
- R3: Lemma L (SH), Lemma E (E<=ceil(c/2)-1 for e<=c<=2e-1), Lemma POS, Theorem R2 (SH, e<=c<=2e-1), Theorem A [re-derived]
  (SH, 3<=c<=e-1), Corollary SH with UH-A.
- R3-ext: Lemma L* (low sets, 1<=m<=k''=min(e,floor((p+2-e)/2))), Lemma H (super-heavy run from the m=floor(e/2)+1 window, for
  every e<=(p-1)/2), Lemma E* (also E+C_E<=e+eps-1; valid for e<=(p+1)/2), Lemma POS*, Theorem U (every prime p, 5<=e<=(p-1)/2,
  3<=c<=2e-1), Theorem A*, Corollary U with UH-A: cells (p+1)/2<=kappa<=p-5 empty for every prime p>=11.
- NOT proved (residual): e=(p+1)/2 (kappa=(p-1)/2), every prime p>=11, 3<=c<=p-1.

## 2. Manifest and imports
Governing review-excerpts-RUH3-v1.json, SHA256 6f6e3aa2174a56cf81a29080b31459d73f0c7f1e65c77f74c28df2bfa952b195 (5044 bytes): JSON list
{path,sha256,start,end}, whole-file SHA256, inclusive LF line ranges, absolute paths; 21 ranges from
20 files; selected raw 70665 bytes, LF-numbered 73437. Package + manifest + numbered
excerpts < 100,000 bytes. Load-bearing: NF (ROT-few-E-v4 28-43 with accepted overlays), GRX if direction (notes-GRX 7-20), RS(b)
(proof-ROW 16-27, R5), CD; accepted UH-A only for the corollaries. Not imported: RUH2, KP3, KP4, R7, UH-SH/MW/L/PH (UH-E's
content is re-proved as Lemma S). Context only: obstruction-UH-EXCL-v1.md 27-48 (R-UH), residual-RUH2-v1.md 14-24 (R1/R2).

## 3. Argument map / hostile-review focus
A. R3 Secs. 1-5 [RE-DERIVED from the candidate RUH2]: SR, Lemmas M/P/U, window (W), MW, (MWe), toggle path, h, light sets,
   counts, Lemma L, Lemma S.
B. R3 Sec. 6 Lemma E [NEW]: B0 in M; the integer interval [L,R'] (component of M containing B0); every forced interval inside
   it (|U|+|F|>=c+1); unique lifts and the defect bounds (I.5); positive/negative runs (I.6)-(I.7); Case II two-block step.
C. R3 Sec. 7 Lemma POS [NEW]: the identity 2m(P)-1=E-1+(2r_Q-o_end)+o_FF+o_in for P=Q u I; the equality case trade x->y and
   the parity of the neighbouring index; singleton Q-blocks force 3E>=2(c+1).
D. R3-ext Sec. 2 Lemma L*: Case A uses m<=floor((p+1-g)/2) (worst g=e-1 gives k''); Case B uses p>=2e+1.
E. R3-ext Sec. 3 Lemma H: low/high split at m=k with gap p+1+delta, toggle path for N>=2k+2.
F. R3-ext Sec. 4 Lemma E*: the interval-count cap M0=ceil((e+1)/2), freeness M0+e-1<=(p+1+c)/2, defect lower bounds -c and 1-2e,
   the k6 argument, C_E<=m(Y+)+m(Y-), and E+C_E<=e+eps-1.
G. R3-ext Sec. 5 POS* branch (alpha): k'' largest blocks hold <=c-e runs, the rest are singletons, m(Q)-1<=C_E+|X|, |X|<=b,
   so c+k''<=p-2+eps against c>=e+k'' and 2k''>=p+1-e.
Endpoints: p=11,e=5 (k''=4, k=3); p=13,e=5 (SH boundary 3e=p+2); c=e; c=2e-1 (Case II); e=(p-1)/2 (nu=2).

## 4. Verdict boundary
Judge Theorems R2, U, A/A*, Lemmas L, L*, H, E, E*, POS, POS* and the corollaries at the exact antecedent and ranges; confirm
the residual note does not overstate (R1b and MC1b are route statements). UH-EXCL is NOT claimed: it would still need
kappa=(p-1)/2 and the pending KP3/KP4/R7 cells (kappa=p-3, p-4 and p=7).
