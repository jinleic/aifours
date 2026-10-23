# Uniform mixed-single seeds when B >= kB + 1 (all-single-letter NMH words)

Version r1, written 2026-10-17T23:35:28-0700 in c6/ (task OlsonRunCount5, cycle 6): new immutable revision after the static reviews
institute/runs/six-lane-2026-10-16/review/olson-uniform-{codex,claude}-review-v1.note.md (r0 = target T1: Codex ACCEPT; Claude ACCEPT-WITH-FIXES with
MINOR T1-m1, T1-m2; FATAL 0, MAJOR 0 in both).  The r0 file c6/proof-RZwide.md (sha256 f6aff2e2a6cf5eb8...0962a9) stays unchanged.
Changes (record and wording only; no statement, recipe, inequality, conclusion or control changed): (1) T1-m1: the import list
names Lemma H and the review status of c6/proof-SEEDG-r2.md, including that the actual-empty alternative used in Sec. 3 comes from
its r2 delta; (2) T1-m2: the no-wrap reason in Lemma R1 covers both sides of the cycle (cyclic distance min(4,k-4)>=2); (3) Sec. 3
points to the proof of Lemma GS (a) for the actual-empty alternative.  The r1 changes are not independently re-reviewed.
Original r0 provenance: written 2026-10-17T19:19:55-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof (r0 reviewed as
above; the r1 changes are not re-reviewed).  Finite controls are [F] aids only;
none is a hypothesis.  This is a uniform theorem, NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson.
Paths are relative to mixdef-high/.

Imports: Lemma H with beta = 0 (../../inverse-parity/proof-PAR-K0.md Sec. 1, with its 07:39 correction, as used in
c6/proof-SEEDG-r2.md Sec. 0; Codex ACCEPT); the all-single-letter specialisation of the NMH setting of c3/proof-C-r1.md Sec. 0;
c6/proof-SEEDG-r2.md Lemmas GS (a), (b), NW, SCW-G, SL, C0+ and Theorem SEED-G (r1 reviewed ACCEPT-WITH-FIXES by Codex and Claude;
the r2 delta, including the actual-empty alternative used in Sec. 3 (its change (4)), rated DELTA-ACCEPT-WITH-NOTES by the parent's
delta desk without independent CLI re-review).  Only these written lemmas are used.  The mixed-single
construction is re-proved below (it is Lemma RZ of c6/proof-LB-r1.md, but no finite-class result of that file is used).  In particular,
SEED-G*, its relaxed (QS*) bounds, the profile lemma, Lemma C0W and the finite class censuses are NOT used.

## 1. Setting and explicit recipe

Let p >= 7 be an odd prime, w an all-single-letter NMH word with R=k<=2p-3: n=p+g aligned runs of weight +1 and B anti runs of weight
-1, where g:=kB>=1, kappa=g+B, k=p+kappa, kappa<=p-3, and all reflection runs are odd.  Assume
   B >= g+1.
Set s:=(p-1)/2, m:=ceil(kappa/2), r:=m-g.  Since kappa>=2g+1, r>=1.  Define
   c:=1 if r is odd, and c:=2 if r is even;  y:=g+c,  i:=(m-y)/2,  j:=(m+y)/2.
Then m and y have the same parity; i,j are nonnegative integers and i+j=m.  The choice is a single fixed type (y,m) for the entire
class, independent of the positions of the anti runs and independent of the target run's sign.

**Lemma R1 (realisability).**  For every target run t there is a proper pattern Q of type (D_Q,m(Q))=(y,m) consisting of i anti singles
and j aligned singles, pairwise non-adjacent, with no member adjacent to t.  Q+t is proper and has type (y+d_t,m+1).
Proof.  r>=1, and c is the least positive integer in {1,2} of the same parity as r, so r-c>=0; hence i=(r-c)/2>=0.  If kappa=3, the
assumptions force (g,B)=(1,2), m=2,c=1,i=0.  If kappa>=4, m=ceil(kappa/2)<=kappa-2, and
   2i=m-g-c <= kappa-2-g-1 = B-3.
Further 2m<=kappa+1<=p-2<=p+g-3=n-3, and 2m+2<=kappa+3<=p<k.
Delete t and its two neighbours.  The remaining path has alpha>=n-3 aligned and beta>=B-3 anti runs.  If i=0 choose no anti run;
otherwise 2i<=beta, and selecting every other run within each anti interval gives at least beta/2>=i pairwise non-adjacent anti runs.
Remove their neighbours (at most 2i aligned runs).  At least alpha-2i aligned runs remain; selecting every other run in each remaining
aligned interval gives at least (alpha-2i)/2>=j pairwise non-adjacent aligned runs.  These are not adjacent to the chosen anti runs.
The path's ends t+2 and t-2 are at cyclic distance min(4,k-4)>=2 in the original cycle (k=p+kappa>=10),
so they are not adjacent and no wrap adjacency occurs.  Thus their union Q consists
of m isolated singles and avoids both neighbours of t.  Both Q and Q+t are proper (the neighbours of t remain omitted), and adding t
adds one block.  Since the aligned and anti weights are +1/-1, D_Q=j-i=y.  []

## 2. All four arcs are generic

Put A=n=p+g, delta:=p-g.  For a proper pattern of type (v,b), Lemma H with beta=0 gives
 lam(v,b)=min(p-b+1, v+b-g, floor((v+B)/2)+1),
 U(v,b)=p-lambda(Q^c)=max(b-1, v+B-b, ceil((delta+v)/2)-1).
A pattern is generic when its lambda equals the third term of lam and its U equals the third term of U (equivalently lambda of its
complement equals the floor term).  We have kappa<=p-3=2s-2, so m<=s-1 and kappa<=2m.

**Lemma R2 (genericity).**  Q and Q+t from Lemma R1 are generic for either d_t=+1 or -1.
Proof.  For Q, v=y=g+c, b=m.  Its second lam term is m+c; the third is floor((kappa+c)/2)+1<=m+floor(c/2)+1<=m+c (c=1 or 2).
Its first term p-m+1>=m+4 is also above that third term.  For Q+t, v=y+d, b=m+1:
 - second term m+c+d+1 is >= floor((kappa+c+d)/2)+1, since kappa<=2m and
   c+d >= floor((c+d)/2) for c+d in {0,1,2,3};
 - first term p-m>=m+3 is >= that third term (which is <=m+2).
Thus both lambda values equal their floor terms.
For Q the third U term is C(c):=ceil((p+c)/2)-1, equal to s when c=1 and s+1 when c=2.  The first term m-1<=s-2 is smaller, and
   y+B-m=kappa+c-m <= m+c <= s-1+c = C(c).
For Q+t the third U term is C(c+d), equal to s for c+d=0,1 and s+1 for c+d=2,3.  The first term m<=s-1 is smaller, and
   y+d+B-(m+1)=kappa+c+d-m-1 <= m+c+d-1 <= s+c+d-2 <= C(c+d)
for all four possibilities c+d=0,1,2,3 (bounds s-2,s-1,s,s+1 respectively).  Thus both U values are their third terms.  []

## 3. Uniform exclusion

**Theorem RZ-wide.**  For every prime p>=7, every all-single-letter NMH word with g=kB>=1, B>=g+1 and kappa=g+B<=p-3 has an identity
2p-subword, for every placement of the B anti runs.
Proof.  Suppose w avoids.  For each run t use Lemma R1's actual configuration Q.  Q,Q+t are generic by Lemma R2, so Lemma GS(b) of
c6/proof-SEEDG-r2.md gives a quality seed for t (or an actually empty interval from these configurations, which immediately
contradicts avoidance: by the proof of Lemma GS (a) an avoider's x_t lies in [max(lambda({t}),s_lo), min(U({t}),s_hi)]; this is
the actual-empty alternative of Theorem SEED-G from the r2 delta).  Every aligned run has odd length 1, so n_ev,al=0 and condition (i) of Lemma C0+ holds.  Theorem SEED-G gives
a contradiction.  []
This theorem replaces the finite-class route for the entire B>kB half of the large-B all-single-letter remainder.  It also applies
outside the large-B inequality 2B+kB>=p-1; that inequality is not used.  The remaining all-single-letter large-B region (not settled
by this theorem) has B<=kB, kappa<=p-3 and 2B+kB>=p-1.  No universal conclusion for words with excess is obtained here.

## 4. Controls [F], not hypotheses

seedRZwide2.py, out/seedRZwide2.txt (native CPU/file-size bounds, peak child RSS 33,472,512 bytes):
 - Every admissible class (p,g,B), prime 7<=p<=401: 906,860 classes, 1,813,720 target signs.  RZ availability, the four generic arcs,
   the quality-seed inequalities, no wrap, P2 and PIN (when the actual seed ranges are nonempty): zero failures.
 - 66 sampled/pinned classes through p=97 in three layouts, 198 explicit words, 22,611 target configurations.  Constructed subsets
   have the exact discrepancy, block counts and isolation; independent c5 slow_lambda agrees with the four arc formulas.
   Ninety constructed intervals are actually empty (direct exclusions), not merely empty abstract quality windows.
 - Control 1: forcing c=1 instead of matching parity rejects 449,936 class recipes.  Control 2: replacing c=1 by c=3 (same parity)
   rejects 17,316 class recipes by availability or genericity.
The never-run draft seedRZwide.py had one invalid pinned sample (11,5,6); it was replaced before execution by seedRZwide2.py with
(11,2,5).  No proof or receipt relies on that draft.
