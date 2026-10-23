# The whole E=2 NMH layer for p>=31: a universal implication with a finite-constant certificate

Written 2026-10-17T20:14:09-0700, task OlsonRunCount5, cycle 6.  Status: **candidate [W+F], NOT independently verified or accepted**.  The universal
implication is written below; the 315 constant rows are load-bearing finite arithmetic, not merely empirical aids.  The producing
worker's one standalone checker passes, but the independent parent/cross-vendor/third-implementation gates of
skill://finite-witness-triple-verification have NOT been performed here (this worker may not invoke model CLIs).
No full NMH/RUNS/PAR/INV/INV* or ordered-Olson claim is made.

Pinned data: c6/const-e2/315-table.json, SHA256
  cba0206dd7db29b7b840eca3aa35b77720e6591bf5ab75ca558292bb67f22b86
Strict standalone checker: c6/check_constE2.py (producer-authored, imports no other worker code).
Deterministic generator: c6/synthesizeE2const.py; it replays the finite searches and regenerates the exact pinned bytes.  All paths
are relative to mixdef-high/.  Prior written inputs remain unreviewed where stated in their headers.

## 1. Candidate conclusion and reduction to finitely many CONSTANT cases

**Theorem E2-layer [W+F, pending independent verification].**  Every NMH word with E=R-k=2 and R<=2p-3, prime p>=31, has an identity
2p-subword, for every run-length distribution and placement.

Put D=Delta0=2p-R>=3, g=kB>=1, kappa=g+B.  Then
  k=2p-D-2, kappa=p-D-1, A=p+g+1, B=p-D-1-g.
If D>=9, the quality-seed construction in E-global applies (D>=3E/2+6).  For E=2 it finishes by original C0+ case(i), with no C0WB
or A0 dependency.  If D=3, use the whole-face corollary in proof-E2smallg.md (the four tip regimes, with the balanced one using
SEED-G* under review).  We therefore need only D in {4,5,6,7,8}.

For these D, every target has weight d in [-3,3].  Ordinary aligned singleton count satisfies
  n1>=p+g-3+f_d,  f_d=(4,2,0,1,0,0,1) for d=-3..3,
and ordinary anti count is at least B-4 (proved in E2-tip/E2-balanced).  In particular a target triple deletion leaves the same
ordinary-configuration resources used below.

## 2. Two generic extremes (written, no certificate rows needed)

For g>=3 set m=(p-3)/2.  The arc calculation of E2-tip extends from D=3 to every D>=3 at fixed p,g: increasing D lowers B and kappa,
so the floor lambda cap decreases, while its other two terms do not; U's middle term decreases while its ceiling cap and first
term do not.  Thus Q of type (y,m), y=g+c with c=2 or3, and Q+t of type (y+d,m+1) are generic for all d in [-3,3], exactly as in
E2-tip Sec. 3.

**Mixed-single extreme.**  Let h=g-B<=D-6.  Then r=m-g=(D-2-h)/2>=2.  Choose c=2 or3 matching r parity and take i=(m-y)/2 ordinary
anti, j=(m+y)/2 ordinary aligned runs.  We have i,j>=0.  Aligned availability 2m=p-3<=p+g-6 follows from g>=3.  Anti availability
2i=m-y<=B-7 is equivalent to p>=2D+13-2c, which holds for p>=31,D<=8,c>=2.  The ordinary mixed-single construction therefore exists
at every target, and gives quality seeds or actual empty bounds via genericity and GS(b).

**Aligned-packing extreme.**  Let h>=18-D.  Use c=2 and pack j1=B+D-4 ordinary aligned singles and j2=(h-D+6)/2 ordinary aligned
pairs.  They are nonnegative integers (h and D have the same parity because p is odd), and have m=(p-3)/2,y=g+2.  The available
ordinary packing capacity is
  2n1-k-4>=2g+D-8.
The footprint inequality m+y<=2g+D-8 is exactly h>=18-D.  Thus this configuration exists at every target and also supplies quality
seeds or actual empty bounds.  These two extremes finish directly under C0+ case(i), since E=2.

If neither extreme applies and g>=3, parity forces
  h in {D-4,D-2,...,16-D}.
Moreover B=(p-D-1-h)/2>=(p-17)/2>=7.  These are the balanced certificate rows.  The g=1,2 cases use the small-g residue rows.
The finite certificate indexes ONLY D,h,d or D,g,p mod4,d; it does not index a finite collection of primes and extrapolate it.

## 3. Balanced constant obligations and why B=7 is a universal boundary

For a balanced row (D,h,d), let g=B+h,p=2B+h+D+1.  A witness specifies S(t) (u=t) or P(t,u), type m=g+t,y=g+u.  S is ordinary aligned
singles; P uses j1=g+2t-u ordinary aligned singles and j2=u-t ordinary aligned pairs.
The written availability obligations are
  m>=1, 2m+2<=k;
  S: u=t, 2m<=p+g-6+f_d;
  P: u>=t, j1>=0, t+u<=D-8+2f_d.
Each is either independent of B or becomes weaker as B increases; checking at B=7 proves it for every B>=7.

The four arc offsets, after subtracting g, are CONSTANTS:
  L=min(-h+D+2-t,u+t,floor((u-h)/2)+1),
  U=max(t-1,u-h-t-1,ceil((u-h+D)/2)-1),
  L'=min(-h+D+1-t,u+d+t+1,floor((u+d-h)/2)+1),
  U'=max(t,u+d-h-t-2,ceil((u+d-h+D)/2)-1).
Thus a witness seed has endpoints [L'-U,U'-L], independent of B.  Two witness intervals are intersected for each target row.
For D=4..8 the certificate supplies 175 rows, exactly
  {(D,h,d): 4<=D<=8, h=D-4,D-2,...,16-D, -3<=d<=3}.
The checker verifies exact set equality, including uniqueness (not only row counts), both witness endpoints, and the intersection.
It verifies that every nonempty intersection lies in [-C,C], C=floor(D/2).

The no-wrap boundary check is also universal: lambda({t})=d+1-g.  Its quantity lambda({t})-sh+p increases by 1 with B.  In
U({t})-sl-p the three possible terms are 0-sl-p, d+B-2-sl-p, and ceil((B+D+d)/2)-1-sl-p; each decreases as B increases.  Thus both
strict no-wrap inequalities at B=7 hold for every larger B.  Canonical clipping only shrinks the stated intersection; an empty
intersection is an actual contradiction because its witness configurations are real.

Every nonempty [-C,C] range satisfies (QS*) for E=2: the smallest ceiling target among all d in [-3,3] is ceil((D+2)/2)>=C+1 for
both sides.  For (P2)/(PIN) the checker tests the common box [-C,C] for all weight pairs and m0 in {1,2} at B=7.  Their universal
extension is rigorous: every term of lambda(Q^c) increases with B, every term of p+lambda(Q)-1 increases with B, and
C-lambda({t})-(p-1) decreases with B.  Thus the boundary inequalities are their worst cases.  Lemma SCW-G* yields the full lifted
system; C0+ case(i) then excludes avoidance.  No count-free-finisher dependency enters this balanced branch.

## 4. Small-g constant obligations and why p=31/33 is a universal boundary

For a row (D,g,rho,d), g=1 or2 and rho=p mod4 in {1,3}, write p=4q+rho, a=(rho-3)/2.  A witness gives an ordinary mixed-single type
m=(p-3)/2+t=2q+a+t, with fixed mass y.  Its constants after subtracting 2q are
  L=min(rho-a-t+1,a+t+y-g,floor((y+rho-D-1-g)/2)+1),
  U=max(a+t-1,y+rho-D-2-g-a-t,ceil((rho-g-1+y)/2)-1),
  L'=min(rho-a-t,a+t+y+d+1-g,floor((y+d+rho-D-1-g)/2)+1),
  U'=max(a+t,y+d+rho-D-3-g-a-t,ceil((rho-g-1+y+d)/2)-1).
Again witness intervals [L'-U,U'-L] have no unbounded variable.  The certificate supplies exactly 140 rows for D=4..8,g=1,2,
rho=1,3,d=-3..3.  It verifies both endpoints and their intersection after the constant lower clipping lambda({t})=d+1-g, and
checks that the result is quality (QS) or actually empty.

The ordinary-run availability obligations are m-y even, 0<=y<=m, 2m+2<=k,
  m-y<=B-7,    2m<=p+g-6+f_d.
For rho=3 their smallest p>=31 is 31; for rho=1 the algebraic smallest is 33 (primality is not needed for these scalar inequalities).
The checker uses those boundary values.  When q increases, m grows by2, p grows by4, B grows by4.  Consequently m-y<=B-7 becomes
weaker, y<=m becomes weaker, properness becomes weaker, and the aligned-count inequality cancels q and stays fixed.  Parity is
fixed.  Thus the configurations are available at every larger p of that residue class.

No wrap also extends: lambda({t}) is constant and p increases; U's middle term minus p is constant, its ceiling term minus p
decreases, and its zero term minus p decreases.  The two strict inequalities at the boundary therefore hold uniformly.  Actual
canonical upper clipping can only shrink the quality/empty intersection certified by the data.  Lemma GS and Theorem SEED-G with
C0+ case(i) finish this branch, with no weak seed or new count-finisher dependency.

## 5. Putting the cases together

Assuming the pinned finite certificate satisfies the explicitly listed obligations (as the worker checker reports), the two
extremes, the balanced branch and the small-g branch exhaust D=4..8.  D=3 is the previously written whole-face corollary; D>=9 is
E-global under E=2.  Hence the candidate theorem covers every NMH word of excess TWO for every prime p>=31.  This is not a proof
for E>=4 or a full RUNS/inverse/ordered-Olson result.  The certificate and all imported unreviewed links still need independent
parent acceptance; no promotion is asserted here.

## 6. Byte pinning, worker receipts and controls

* check_constE2.py (producer's one standalone implementation) returns VALID for the expected hash and full 175/140 index universes,
  630 witnesses, under both normal Python and -O: out/constE2_normal.txt and out/constE2_optimized.txt.  No worker module is imported;
  expected SHA is a required CLI argument; duplicate JSON keys/extra fields/unrecognised indexes are rejected.
* Intended-reason controls (out/constE2_controls.json), normal and -O separately: dropping a balanced row -> COVERAGE; changing an
  endpoint -> ALGEBRA; setting an impossible type -> AVAILABILITY; wrong expected SHA -> HASH.  All eight invocations reject with the
  intended reason.  Mutation fixtures and hashes are retained in const-e2/.  These controls belong to this checker only.
* synthesizeE2const.py regenerates const-e2/315-regenerated.json byte-exactly (same SHA above); the strict checker accepts the
  regenerated copy (out/constE2_regenerated_check.txt).  The generator is deterministic finite-constant search, NOT the checker.
* Constructive smoke (replayE2layer.py/out/replayE2layer.txt): 80 selected parameter jobs, 160 actual words across all four
  constructions.  Balanced:10,176 configurations, small g:10,208, mixed-single extreme:5,312, aligned-packing extreme:5,352.
  Every actual mass, block count, isolation and interval agrees with independent c5 slow_lambda; zero failures.  No residue-vector
  avoider or raw group-product claim is made.  Peak child RSS34,308,096 bytes; native CPU/file-size limits.
* This is still only producer verification.  Per the finite-witness verification skill, independent parent and model-written
  implementations, their own controls, pinned input manifests and action/priority audit remain unperformed in this worker.
