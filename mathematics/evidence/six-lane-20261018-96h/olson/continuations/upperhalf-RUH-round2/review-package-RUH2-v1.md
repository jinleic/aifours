# RUH2 review package: R-UH partial (uniform c<=e-1 on 3e<=p+2; whole cell kappa=p-5 for p>=13) + exact residual, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T17:28:19-0700. CANDIDATE_UNVERIFIED written proofs; outcome = LABELLED PARTIAL of
the frozen target plus an exact residual. Parent owns both-family reviews and verdicts. No scientific computation,
enumeration, script, assertion, solver, model CLI, test/build or Lean; all case work by hand. No novelty/priority/human-review
claim.

## 1. Review exactly these frozen texts
- proof-RUH2-v1.md, SHA256 f391b08f2df02036b4a7cfc66c1f118e7f20c6dfb8d89af2a10e121ea58df4e2, lines 1-175 (16,514 bytes),
  read with erratum-1-proof-RUH2-v1.md, SHA256 a3c673137ed35b81220b51f9e19997f0c31b10a32bcb5dc7b222e641f50f3f61 (E1 closes a
  justification gap in the c=5 pair step: s=-4 is excluded by j=4; E2 states the free-length range used at c=9).
- residual-RUH2-v1.md, SHA256 267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b, read with
  erratum-1-residual-RUH2-v1.md, SHA256 52871fb8f9dc796a35fef55367764335506131856e1e24a96e3c204027ac94ac (wording of F2).
- Scope RUH2-scope-v1.md, SHA256 b1cdfaeee6db5985a2af1f8f98c4f66cd7a8e8e8fe77cbebab372f270d4c5dd0, frozen 17:07:02 BEFORE
  derivation with prior methods and the planned route disclosed. Authority: RUN/control/written-slot-transitions-olson-beta-
  prt-20261019-1708-v1.json, SHA256 32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12, key math2.

Claims (full NF antecedent: some admissible NF of a length-(4p-2) avoider has terminal k=p+1, kappa^=kappa; H^=e-1 anywhere in
the odd blocks; empty runs separate different values; no o_F/run/pair hypothesis):
- Lemma L: SH range (p>=13, 5<=e<=(p+2)/3): a run h exists with d(P)<=c-min(e,2m(P)-1) for every nonempty P avoiding h,
  1<=m(P)<=e.
- Theorem A: SH range, 3<=c<=e-1 impossible (uniform in p and e).
- Theorem B: e=5 (kappa=p-5), every prime p>=13: 3<=c<=9 impossible; Corollary B with accepted UH-A: the whole cell
  kappa=p-5 is empty for every prime p>=13.
- NOT proved (residual note): 3e>p+2 (all of p=11; p=13 with e=6,7; ...), and the SH range with e>=6, e<=c<=2e-1.

## 2. Manifest and imports
Governing review-excerpts-RUH2-v1.json, SHA256 c2238172ff26829aaeb5840336c77036337a7c2c0358695880de2ab21222bb2e (4,811 bytes):
JSON list {path,sha256,start,end}, whole-file SHA256, inclusive LF line ranges, absolute paths; 20 ranges from 19 files;
selected raw 56,636 bytes, LF-numbered 58,698. Package + manifest + numbered excerpts < 100,000 bytes.
Load-bearing: NF (ROT-few-E-v4 28-43 with accepted overlays), GRX if direction (notes-GRX 7-20), RS(b) (proof-ROW 16-27, R5),
Cauchy-Davenport; accepted UH-A only for Corollary B. UH-SH and UH-MW are NOT imported (re-derived in proof Sec. 3 because the
transition lists only UH-A/L/E as accepted UH inputs). KP3/KP4/R7 are not cited. R-UH is defined at obstruction-UH-EXCL-v1.md
lines 27-48 (with parent erratum v1: lambda=c-1).

## 3. Argument map / hostile-review focus
A. Sec. 1-2 [RE-DERIVED]: SR with j in [m,m+e-1]; Lemma P (n=max(p-1,2kappa+2-2m), p-1 pairs), Lemma U, A'<=kappa, A<=2p-1
   (2p<=R in the SH range), window (W), gap p-2e+3+delta.
B. Sec. 3 [RE-DERIVED]: Lemma MW with K_j=p-1-2e+2j; (MWe): the branch r<=e-2 forces 3e>=p+3; the toggle path from
   {0,2,...,2e-2} (N>=2e+2); super-heavy h; light sets (0>=3+2delta impossible); counts E+|Q|>=c+1, |Q|<=c-1, E>=2.
C. Sec. 4 [NEW] Lemma L: Cases A/B; check the inequalities floor((e+1+g)/2)>=g+1 and floor((e-1+g)/2)>=g for g<=e-1, the use
   of p>=3e-2 for the upper end (p+1+g)/2, and that only m<=e is claimed.
D. Sec. 5 [RE-DERIVED] Lemma S: free iff j>=e-c/2 and j<=(p+1+c)/2; (N1) at j=e-(c+1)/2.
E. Sec. 6 [NEW] Theorem A: independence number of S=E u Q forced <=(c+1)/2 by Lemma L at m=floor((c+1)/2)+1<=e; parity forces c
   odd, |S|=c+1, even components, Q empty; then t(Y)+e in M for all nonempty Y (j=e free), RS(b) with K=c+1: |M|>=c+1.
F. Sec. 7 [NEW] Theorem B: the five lists c=5..9 (read c=5 with erratum E1); the position endgames, including the c=9
   one-block-of-six case using the middle of four consecutive empty runs.
Endpoints: p=13 (residues <=10 distinct; (MWe) at 3e=15=p+2); c=e-1 boundary in Theorem A; c=9=2e-1 (two-piece M excluded);
non-wrapping of forced intervals.

## 4. Verdict boundary
Judge Lemma L, Theorem A, Theorem B and Corollary B at the exact antecedent and ranges; confirm the residual note does not
overstate (R1, R2 and the missing claims are route targets, not proven-necessary lemmas). Report import-scope issues
separately. UH-EXCL is NOT claimed; it would still need R1, R2 and the pending KP3/KP4/R7 cells.
