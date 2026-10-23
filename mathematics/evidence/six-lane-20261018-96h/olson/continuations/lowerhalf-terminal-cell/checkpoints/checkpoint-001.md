# LOWER checkpoint 001: range/coverage verified; general tools located; derivation under way

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T21:30:21-0700. Scope LOWER-scope-v1.md SHA256
2e9784c14a8c467d52eb43e2787d22a0d947a2bee255dd731ccc5a65b1007959 frozen 21:17:19 before derivation. Written only; no computation.
Parent IRC (KP3-EXCL accepted at its own cell, verdict bb9d8a27...) noted; lower-half work unchanged; KP3 is another cell.

Actual results so far (notes, CANDIDATE, unfrozen):
- NF range at k=p+1 from pins: GRX all-plus kappa_hat>=0, H>=0 kappa_hat<=p-1 (DAV gives only <=p); target 1..(p-3)/2 inside.
- Coverage: no accepted whole-cell exclusion in the lower half; accepted B0S-CJ''' (cj-cjx verdict lines 8-15) covers ONLY the
  all-rotations-equal sub-case (Delta=-kappa<=0, R=p-1+2kappa>=4kappa-4, 2kappa<=p-1). ROT-FB/LS/ZX need k<=p; not usable.
- Accepted Theorem P (Chevalley-Warning; listed as accepted import in the K0*-RED verdict line 7) applies to general rotations:
  in every lower-half NF, F+sum floor(r_i/2)<=3p-2 gives sum_i floor(r_i/2)<=2kappa-1, so at most 2kappa runs have even length
  (empty included) and the runs are mostly singletons. (Will be recorded via a scope addendum before use, as Theorem P was not
  listed in the frozen input list.)
- RS(a) at n=2kappa: every nonconstant sign pattern has a signed rotation value of multiplicity >=2kappa+1; for 1<=m<=kappa the
  excess sum_x max(0,v_x-(2kappa+2-2m))>=2m-1.
- Exact zero-sum reformulation of GRX at k=p+1 (any rotations): identity iff some zero-sum subsequence S of the 2p+2kappa odd/even
  elements {(1,x) for letters} u {(r_i mod 2, -(tau_i+X_i)) for runs} of Z_2p has n(S)+2m(S) in [2kappa+2,2p] (n, m invariant under
  complement). Davenport (2p) gives many zero-sums; the obstruction is controlling n+2m (n is not additive).
Blocker: no uniform mechanism yet; kappa=1 looks closable by a finite written case analysis (Theorem P forces E<=2, nearly all
runs singletons; T=0 arc + Savchev-Chen structure). Next bounded action (<=30 min): decide route (kappa=1 cell vs uniform
rotation structure) and freeze the first lemmas (range/coverage, run structure, dominance) as a partial.
