# S3 lowdefect erratum 1: exact scopes, complete equality-use inventory and explicit standalone packing steps

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T09:02:34-0700. Applies to the unchanged candidate
proof-S3-lowdefect-core-v1.md 3847ade3f32e9d9edd11a7cbbd246b68b1a63c8e16beda796250d7c9d64c662a and, where stated, its review package
review-package-S3-v1.md 28cb76c9eb12022c98831544471c25d626d0d3fed364d3084f9972e6a161dcb2. Source/package/excerpt files remain unchanged.
Reviews frozen at run review/olson-S3-lowdefect-review-freeze-v1.json
955a242794aa633fde930b6f42476f22b81994312f142bf5ee15c3db515f6b35:
- Codex review/olson-S3-lowdefect-codex-v1.prompt.stdout.txt f5724e97b026f925239b4bab186fd19afa190c9d926c891f33dffd8d3ba2249b: P1/P2/P3 ACCEPT, no required repair.
- Claude review/olson-S3-lowdefect-claude-v1.prompt.note.md 55592d1d41c358e515373fcdf230e22c04ca230359005af499b8b65f57147d66: no mathematical gap; required editorial/shared
  MINORs P1-1,P1-2,P2-1,P3-1,S-1,S-2,R-1,R-2 and optional P3-2, all disposed below. Shared findings are not added to per-claim counts.
Old quotations join source line breaks by spaces. These replacements govern. No theorem is strengthened; no new external theorem
is imported; no Lev theorem or later normalization/closure candidate enters this overlay. P1/P2/P3 remain CANDIDATE_UNVERIFIED
pending the parent verdict, despite the accepted status of their L1/B2-1 dependencies.

## E-S1: historical status labels (Claude S-1)
Old (source lines4-6): 'Candidate BASE2 proof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 (L1 and B2-1) is NOT an accepted import:
its packing argument is expanded below with the changed length hypothesis checked; all consequences using L1 remain explicitly
conditional pending parent review.'
New: 'BASE2 L1 and B2-1, from proof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 through
erratum-1-BASE2-consolidated-v1.md 05749bc842c94cc628d05383d301551d62255adede75c5f1876295180afd780b, are parent-accepted in
review/olson-BASE2-cells-parent-verdict-v1.md 9df92bdafcb73cff034695ece0c5234fd3cb1bb29821ab30182b30b88fdab553, line10, ONLY in the threshold LS-counterexample
CF setting w.r.t. g0. P2 and the empty-Z0 branch of P3 use exactly that scope. P1 is proved in-file at its standalone scope;
it is not imported from restricted B2-1 or its isolated Sublemma(a), which has exact length2m+3. All labels "candidate L1",
"candidate B2-1" and "conditional on candidate L1" in this source are historical and are read with this authority. No acceptance
of the new P1/P2/P3 claims themselves is asserted.'
Old (line18): 'Candidate L1 says there is W*<=U with sum=-1(mod p), |W*|>=d+2.'
New: 'Accepted L1 (BASE2 verdict line10, threshold CF data g0 only) says there is W*<=U with sum=-1(mod p), |W*|>=d+2.'

## E-S2: d>=1 is from CF(a) (Claude S-2)
Old: 'Accepted RED, DGM-p, the threshold dichotomy and LS-II' give g=g0 a generator, M=2p-d with d:=delta0,1<=d<=h-1,'
New: 'Accepted RED, DGM-p, the threshold dichotomy and LS-II' give g=g0 a generator, M=2p-d with d:=delta0 and d<=h-1;
d>=1 is from CF(a), since (ZP_kappa) forces M<=2p-1 and d=2p-M.'

## E-P1-1: full equality-use inventory (Claude P1-1)
Old: 'This is the only place the old proof used |S|=2m+3; the lower bound is sufficient.'
New: 'The exact length entered the earlier B2-1 source at (a) (|A|>=2m+4), (b) (B>=2m+3, unused afterwards in the case split),
and (f) (existence of a fourth term outside the surviving triple; five copies of2m). Here n+1>=2m+4 and n>=2m+3>=9 supply
all of these. The J/pair/triple analysis uses only B,t and their displayed ranges, not n=2m+3; B<=4m follows from sigma>=h+1,
independently of n. No step uses an upper bound on n, other than the consequence n<=B<=4m derived in-file.'
This replaces an inaccurate inventory sentence, not a mathematical step of the new proof.

## E-P1-2: write out every standalone packing step (Claude P1-2)
Representatives (source line31), Old: 'Negate S to Q: all nonempty subset sums lie in [1,B] with B:=p-sigma<=4m,'.
New: 'Negate S termwise to Q: all nonempty subset-sum residues lie in [1,B] with B:=p-sigma<=4m; in all subsequent integer
pair/triple computations, each term of Q is identified with its least positive representative in [1,B],'.

Proper complement and x=1 (lines33-34), Old: 'Every proper nonempty subset sum x of V and its complementary sum1-x lie in
[1,B], forcing x in J:=[p+1-B,B]=[6m-B,B].'
New: 'Every proper nonempty occurrence subset of V and its actual occurrence complement are both nonempty; if the first has
residue x in[1,B], the complement has residue1-x in[1,B]. x=1 is impossible (its complement would have residue0); if x>=2,
its complementary residue is p+1-x, which lies in[1,B] exactly when x>=p+1-B. Thus x lies in J:=[p+1-B,B]=[6m-B,B].'

Lifted-pair triple lower bound (lines36-37), Old: 'a proper triple lies in [18m-1-2B,3B]'.
New: 'a proper triple contains a pair whose integer sum is p+y, y in J, and hence at least p+(6m-B)=12m-1-B; its third term
is at least6m-B, so its integer sum is at least18m-1-2B and at most3B, i.e. it lies in[18m-1-2B,3B]'.

Wrap windows at B=4m (line40), Old: 'B=4m: J=[2m,4m]; a proper pair has sum4m (both2m) or8m-1 or8m. If t>=4, a proper triple
must have sum in p+J=[8m-1,10m-1].'
New: 'B=4m: J=[2m,4m]. For an integer pair/triple sum C with4m<=C<=12m=2p+2, the residue is C if C<p; 0 if C=p or2p;
C-p if p<C<2p; and1 or2 if C=2p+1 or2p+2. Residues0,1,2 are outside J (m>=3). A proper pair has sum in[4m,8m], so residue
in J permits only C=4m (both2m) before a wrap, or C in[8m-1,8m] after one wrap. A proper triple for t>=4 has sum in
[6m,12m]=[p+1,2p+2]; it cannot have an unwrapped residue in J or a residue0,1,2 at the second wrap, so it lies in
p+J=[8m-1,10m-1].'

Surviving triple pair constraints (lines43-44), Old: 'Its total is p+1=6m (forcing (2m)^3) or2p+1=12m-1 (pair constraints
force (4m-1,4m,4m)).'
New: 'Its total is p+1=6m (all three terms are>=2m, forcing (2m)^3) or2p+1=12m-1. In the latter case each pair is
12m-1-z_k, with z_k in[2m,4m], so the pair sum lies in[8m-1,10m-1]; the proper-pair possibilities just proved restrict it
to8m-1 or8m. Thus each z_k is4m-1 or4m, and total12m-1 forces exactly (4m-1,4m,4m).'

Outside term representative (line45), Old: 'there is a term y of Q outside this triple.'
New: 'there is an actual occurrence y of Q outside this triple, identified with its least positive representative in[1,B]
(and hence in[1,4m]); every tested union of y with part of the triple uses distinct occurrences.'

## E-P2: exact P2 scope and accepted L1 (Claude P2-1)
Old heading: '## 2. P2: exclusion of d=delta0=2 (conditional on L1)'.
New heading: '## 2. P2: d=delta0=2 is impossible for a threshold BASE2 LS counterexample with CF data w.r.t. g0'.
Old conclusion: 'So d=2 is impossible at EVERY BASE2 cell, conditional on candidate L1 (not merely the m<=4 cases handled by I-small).'
New conclusion: 'For a threshold LS counterexample at a BASE2 cell (p=6m-1 prime,m>=3,kappa=4m,Y odd,|Y|=14m,(ZP_4m),a zero-sum
of length>=2p+2), with CF data w.r.t. dominant g0, d=2 is impossible, relative to accepted L1 (BASE2 verdict9df92bda line10)
and in-file P1. In this application |U|=2m+4, so the in-file P1 length extension, not the exact-length B2-1 statement, supplies
the contradiction.'
This is a configuration exclusion, not LS(p,4m). The package's I-small comparison is non-premise context (the two-cell BASE2
proof checks its literal uses); P2 does not use I-small.

## E-P3: exact P3 scope, every Z0 choice and accepted empty case (Claude P3-1)
Old beginning: 'If delta'=1 and Z0 is empty, d=1 and P1+L1 exclude the case (candidate B2-1).'
New beginning: 'For a threshold BASE2 LS counterexample with CF data w.r.t. g0 (exact setting of E-P2), let Z0 be ANY
inclusion-maximal mod-p zero-sum occurrence sub-multiset of U, possibly empty. If delta'=d-|Z0|=1 and Z0 is empty, d=1;
accepted B2-1 (BASE2 verdict9df92bda line10, restricted threshold CF setting) excludes this. Equivalently, P1 plus accepted L1
at |U|=2m+3 supplies the contradiction.'
Old conclusion: 'Together with the empty case, delta'=1 is impossible at every BASE2 threshold, conditional on L1 only for the
empty-Z0 case.'
New conclusion: 'Thus in the exact threshold-counterexample CF setting w.r.t. g0, delta'=d-|Z0| is not1 for EVERY
inclusion-maximal choice of Z0. The nonempty-Z0 branch is independent of L1; the empty branch uses accepted B2-1 (or in-file
P1 plus accepted L1), always at that restricted setting.'

## E-P3-2: actual dependence and d=3 (optional Claude P3-2, adopted)
Old: 'For A':={0} union Sigma(U'), the first paragraph of P1 applies: |A'|>=2m+4 and A' subset {0} union T, T:=[h+1,p-1], |T|=4m.'
New: 'For A':={0} union Sigma(U'), distinct nonzero prefix sums of the zero-sum-free U' give |A'|>=|U'|+1=2m+4; (F') itself
excludes all nonempty residues in[0,h], so A' subset {0} union T, T:=[h+1,p-1], |T|=4m. No sigma'-localisation or symmetry
A'=sigma'-A' is used in this branch; the only complement needed here is the actual occurrence complement Z0-{z}.'
Old: 'If that range is empty we already have a contradiction.'
New: 'If that range is empty, which here is exactly d=3 (as d>=3), no residue zeta can occur but |Z0|=d-1=2; contradiction.'
The review package's P3 focus phrase 'complement symmetry' is read as 'the occurrence complement Z0-{z}'; P1 does use its
separate subset-complement symmetry, but P3's nonempty branch needs only the direct facts displayed here.

## E-R1: tight, disjoint necessary residual with quantified choices (Claude R-1)
Old (source78-80): 'Conditional on L1/P1, the BASE2 residual shrinks from 2<=d<=2m-3 to 3<=d<=2m-3,
2<=delta'=d-|Z0|<=d, with |Z0| either0 or>=2.'
New: 'Relative to accepted L1/B2-1 at threshold scope and in-file P1/P2/P3, every threshold BASE2 LS counterexample with CF
data w.r.t. g0 must satisfy3<=d<=2m-3. For EVERY inclusion-maximal zero-sum occurrence sub-multiset Z0, exactly one of the
following disjoint residual alternatives holds:
 (i) Z0 is empty, and delta'=d in[3,2m-3];
 (ii) 2<=|Z0|<=d-2 and delta'=d-|Z0| in[2,d-2], which requires d>=4.
These are necessary conditions only: neither existence nor nonexistence of any residual configuration is proved.'
This same replacement governs the looser residual description in review-package-S3-v1.md Sec. 2. P1/P2/P3 themselves are
still new candidates until the parent verdict; E-S1 discharges only their old L1/B2-1 status labels.

## E-R2: index-one arithmetic is orientation only (Claude R-2)
Old: 'In particular m=5 (p=29) still has the short-core value delta'=2 below the index-one threshold
|U'|+1>=floor(p/2)+2, which is equivalent to delta'>=m-2. P3 does not exclude delta'=2.'
New: 'ORIENTATION ONLY: the general index-one length inequality |U'|+1=2m+3+delta'>=floor(p/2)+2=3m+1 is equivalent to
delta'>=m-2. At m=5,p=29,delta'=2 fails it (15<16); delta'=2 can occur in the necessary residual only in branch(ii), so it
would require nonempty Z0 with d>=4. No accepted or proved interface in this file excludes the general-m configurations
with delta'>=m-2, either. The entire residual(i)/(ii), not just delta'<m-2, remains unresolved by P1/P2/P3.'
Source82-85 and the package's proposed next-lever discussion remain planning sketches, not further theorems. At m=3 and4,
LS(17,12) and LS(23,16) are already accepted by separate BASE2 verdict9df92bda; their closure is not inferred from P1/P2/P3.

## Exact conclusions and boundary
P1 remains standalone at p=6m-1 prime,m>=3,|S|>=2m+3 with nonempty occurrence sums avoiding[0,2m-2]. P2 excludes d=2 only in
the threshold LS-counterexample CF setting w.r.t. g0. P3 excludes delta'=1 there for every inclusion-maximal Z0. No universal
BASE2 LS, full LS, LS+, STAB, INV*, ordered-Olson, novelty or matched-SOTA result follows from this package. No external Lev
result is used in these three proofs or in the present dispositions. No new ZCLASS derivation was performed while reading
the reports and preparing this overlay.
