# BOTTOM review package: full candidate exclusion of kappa=(p-1)/2, e=(p+1)/2, p>=11, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T18:58:01-0700. CANDIDATE_UNVERIFIED FULL WRITTEN PROOF for this exact cell. Parent owns
both-family review, independent verification and verdict. No scientific computation/enumeration, script, solver, assertion,
model CLI, tests/build or Lean. No novelty/priority/first/human-review claim, no whole ordered-Olson claim.

## 1. Exact frozen proof unit
Directory: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-bottom-cell/
- proof-BOTTOM-parity-v1.md (P), SHA256 b648411f7ed7b2b17fdd9bcc4a51f2df24ca7a1540eb88cd4c7fbd2e6080a9f3, lines 1-265 (24,587 bytes).
- proof-BOTTOM-close-v1.md (C), SHA256 e9e1b55315bbe4cc24b50da7c600f6c8af09626b7a4ead6731a171b775521817, lines 1-126 (9,786 bytes).
Read TOGETHER: P was frozen as a labelled partial (E=0 + necessary odd-gap profile); C completes it by a minimal interior-g
argument. P's old residual paragraph records that earlier stage, not the final scope of the combined unit. The final result
is Theorem BOTTOM / Corollary BOTTOM in C, with no numerical/profile subcase left within the target, subject to review.
- residual-BOTTOM-v1.md (route/closeout ledger), SHA256 fd4baf232f6aa66d3c270a4b9baff65723dd9f1f5a2bc5009f6dac5f1731190e, lines 1-49: every failed route is retained, including
the real p-1-residue odd-gap obstruction; it is not silently replaced by q>=g+1 or a nonexistent path at m=e.
- BOTTOM-scope-v1.md, SHA256 ab9ee0251454d4242b2d268e73eacacf875df6172467f3a24fef6c3cbc22d99e, frozen 18:30:34 BEFORE derivation with pre-freeze exposure. Authority
RUN/control/written-olson-upperhalf-bottom-transition-v1.json, SHA256 a0deb9816a303dc65d75b7728889696e2dcc2cfb3e53d25a570eae9374be586f.

Full claim: every prime p>=11, e=(p+1)/2, kappa=(p-1)/2; an avoider of length 4p-2 has SOME admissible NF with terminal k=p+1,
kappa_hat=kappa, arbitrary H=e-1 extra reflection-pair placement, and empty runs separating different values. No such avoider
with A=p-1+c, 3<=c<=p-1 exists. UH-A forces that c-range, so the specified NF cell is excluded. No o_F/run/pair hypothesis or
multiset-only consequence outside this antecedent. No prior RUH3/RUH2/KP3/KP4/R7 candidate is used as a premise.

## 2. Manifest / import scope
review-excerpts-BOTTOM-v1.json, SHA256 e5227994692a3e52c3c1f94378215ded10f2caccaa1b14f8c92d225033fdf0b1 (4558 bytes), governs: JSON list {path,sha256,start,end}, absolute paths,
whole-file SHA256, inclusive LF ranges; 19 ranges from 18 files; raw excerpts 71285 bytes,
LF-numbered 74121. Package + manifest + numbered excerpts <100,000 bytes.
Accepted: NF (ROT-few-E-v4 28-43 with lowodd/ZX/fewodd overlays), GRX IF direction only (notes-GRX 7-20), RS(b) (ROW16-27,R5),
classical CD; UH-A at literal antecedent and UH-E (re-proved with the b<=n<=A guard). UH-L (delta=0 only) is not used; neither
are UH-SH/MW/PH, PP1/KP2 outside their cells, CT, Lev, S(p), RPdelta, ASSEMBLY-P, REFL, RUNS or LS-family. Everything reused
from prior candidate work is proved inline in P, not imported by a claim of acceptance.

## 3. Hostile-review map (all claims CANDIDATE)
A. P Secs.1-2: bottom SR is j in [m,m+e-1] intersect [1,p]; n=p-1 at j=e is always admissible for nonconstant patterns.
   P/U pairing and common nonzero class; W (low d<=c-1 / high d>=c+1+delta). MW has K_j=2j-2.
B. P Lemma C: low critical g=2r+1<=e-1, r+1<=m<=e-r. q=g leaves exactly one possible missing residue. For g>=3, every
   minority difference must translate the q-term interval by one step (+/-2a); for g=1, the two-difference argument and the
   signed -a count >=c-1 fix the step. All signed values are a,-a,3a and the missing target is EXACTLY D_z/2.
C. P Secs.3-5: empty toggles change m by <=1 but keep g, and change T by nonzero tau_i. The only small-m escape compatible
   with an empty run is e even,g=e-1,m=k0 and flat signs at empties. Cap ell=e or e-1 gives a large anchor. ME uses only
   m<=ceil((e+1)/2), unique lifts in the component of M containing B0, |defect|<p, and full subsets only at free lengths.
   Check E0's three c-ranges and its Q-block exchange/large-block count. P Secs.6-7 are consequences, not needed for C.
D. C Sec.1: minimise g over ALL INTERIOR critical patterns (r+2<=m<=e-r-1), not only m<=k0. All singleton runs are signed -a;
   a singleton can flip only out of that interval. At a sole lower endpoint they are isolated (s1<=g+2), at a sole upper
   endpoint flat (s1<=g). LEN bounds every L_i<=g. A pure signed-a run exists because w0<N, and flipping it gives g'=g-L:
   zero forbidden, even contradiction, odd a smaller interior g. Thus both endpoints coincide, e odd,g=e-2,m=(e+1)/2.
E. C Secs.2-3: even e gives cap e-1 and L_h>=p-1+delta, exceeding the positive-run maximum p-2. Odd e gives cap e-2 and
   L_h>=p-3+delta, so at least p-1+delta singleton runs; the top interior pattern has only e minority letters and every
   singleton is signed -a, contradiction. The toggle path is at m=k0=floor(e/2)+1, NEVER at m=e.
Endpoints: p=11,e=6 (even), p=13,e=7 (odd), c=e-1, c=e, c=p-1 (b=0), g=1 equality, g=e-2/e-1 and both interior endpoints.

## 4. Verdict boundary
Please judge the combined Theorem/Corollary BOTTOM, E0, critical rigidity and all load-bearing scope/range guards, not a
window-condition-only exclusion. No full UH assembly or any earlier candidate promotion is claimed; the result is confined
to this terminal NF cell. No remaining obstruction inside the exact target is asserted after C, but this is not acceptance.
