# S3 continuation: two low-defect core statements, frozen before written derivations, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T08:02:45-0700.  Parent authorized S3 while the BASE2 reviews run.  Status:
SCOPE ONLY; all uses of proof-LS-BASE2-cells-v2.md (fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306) remain CONDITIONAL (not parent-accepted).
No computation.  Same ordered-Olson slot, same BASE2 family, no new target.

## Setting
p=6m-1 prime,m>=3,kappa=4m,e=2m-1,threshold odd Y with |Y|=14m,(ZP_kappa),a long zero-sum.  Accepted RED/DGM-p/LS-II'/CF(a) give case(I),
g=g0,1<=delta0<=2m-3,r=|U|=2m+2+delta0 and (F*): rho(W)<=h:=2m-2 => |W|+2rho(W)<=delta0-1.  Z0 maximal mod-p zero-sum in U,
|Z0|<=delta0-1,U'=U-Z0 zero-sum-free,delta'=delta0-|Z0|>=1,|U'|=2m+2+delta'; (F') with delta'.  L1 is the candidate statement giving
W*<=U of sum -1 and size>=delta0+2.  It will be treated explicitly CONDITIONAL unless its parent verdict arrives.

## Exact next statements under test (not granted)
P1 (packing reformulation of B2-1).  Let S be a sequence of nonzero residues mod p with |S|>=2m+3 such that every nonempty subset
sum avoids [0,2m-2].  Then S has no occurrence sub-multiset W with sum -1 (mod p) and |W|>=3.  This is the candidate B2-1 proof with
its |U|=2m+3 equality replaced by a lower bound; every use of that equality must be checked, not assumed.
P2 (delta0=2).  No threshold BASE2 LS counterexample in case(I) has delta0=2 (use P1 and L1 after checking F* implies the hypothesis).
P3 (delta'=1).  No threshold BASE2 LS counterexample in case(I) has delta'=1, even for delta0>=3 (when Z0 is nonempty).  Planned
lever: complement symmetry gives |A'|>=2m+4 and A' subset {0} union [h+1,p-1]; Z0-{z} forbids the full interval z+[1,h] for A'.  Medium
and negative z values should be excluded by cardinality and the empty subset, leaving only small positive residues; a first-crossing
argument must then exclude a nonempty Z0.  The empty Z0 case depends on candidate B2-1/P1 and L1.
If any statement fails, preserve the exact obstruction rather than import a short-core inverse theorem.  No full BASE2, LS+ or
STAB conclusion is implied by P1-P3; the next unsolved core values would be delta'>=2 with delta0>=3.
