# Uniform aligned singles/pairs seeds when kB >= B >= 2; the all-single-letter NMH subcase

Written 2026-10-17T19:25:03-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Controls are [F] aids only,
not hypotheses.  No NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered-Olson conclusion is asserted.

Imports: c3/proof-C-r1.md Sec. 0 (NMH setting); c6/proof-SEEDG-r2.md Lemma GS, quality seeds (QS), Theorem SEED-G and Lemma C0+.
Only the quality-seed chain is used; neither the relaxed SEED-G* theorem nor the profile/census/count-free-finisher arguments is
needed.  The packing construction (Lemma RZ2 of c6/proof-LB-r1.md) is re-proved below.  All reasoning is uniform in p; no finite
range is promoted to a theorem.

## 1. Parameters and a packing lemma

Let p>=7 be prime, g:=kB>=B>=2, kappa=g+B<=p-3, n:=p+g, k:=p+kappa, and Delta:=p-kappa>=3.  The word w has n aligned rotation
runs of length 1 and B anti rotation runs of length 1 (arbitrary positions), and all its reflection runs are odd.  Thus w is the
all-single-letter NMH subcase with R=k<=2p-3.  For a proper pattern of type (v,b):
 lam(v,b)=min(p-b+1,v+b-g,floor((v+B)/2)+1),
 U(v,b)=max(b-1,v+B-b,ceil((p-g+v)/2)-1).

**Packing lemma.**  For every run t, a configuration of j2 separated aligned pairs and j1 aligned singles (none adjacent to t) exists
if j1,j2>=0 and 3j2+2j1<=n-B-4.  It has mass y=2j2+j1 and m=j1+j2 blocks; adding t adds one block.
Proof.  Deleting t and its neighbours leaves a path with alpha>=n-3 aligned positions in r<=B+1 aligned intervals.  Within an interval
of length l, block sizes s_e in {1,2} can be packed with one intervening unused position iff sum(s_e+1)<=l+1.  First place j2 pairs:
there is capacity sum floor((l+1)/3)>=(alpha-r)/3>=j2.  The residual capacities C_l=l+1-3(pairs placed) have sum alpha+r-3j2; they
support sum floor(C_l/2)>=(alpha-3j2)/2>=j1 singles.  Distinct intervals are separated by an anti run.  All chosen blocks lie outside
t's deleted neighbourhood, proving the claim.  We also use the simpler singles bound: m isolated aligned runs are always available
when 2m<=n-3 (take every other run in each aligned interval after the same deletion).  []

## 2. The default generic type and exactly five exceptional families

Put h:=g-B>=0, q:=floor(h/2), m:=ceil(kappa/2)=B+ceil(h/2).  Define c=1 when q is odd, c=2 when q is even; set y=g+c.
Equivalently c=1 when m-g is odd and c=2 otherwise.  The candidate packing has
   j2=y-m=q+c>=1,    j1=2m-y=B+[h odd]-c>=0.
Its footprint is
   3j2+2j1=m+y,    (m+y)-(n-B-4)=c+4-Delta-q.                                      (2.1)
Since p=2B+h+Delta is odd, h+Delta is odd.  Therefore c+4-Delta-q>0 occurs exactly for
   (Delta,h)=(3,0),(3,2),(3,4),(4,1),(5,0).                                        (2.2)
Written verification of this finite case split (not a computation):
 - Delta=3: h is even.  q odd requires q>=2, so only q=1 fails; q even requires q>=3, so q=0,2 fail.  These are h=2,0,4.
 - Delta=4: h is odd.  q odd requires q>=1 (always), q even requires q>=2 (only q=0 fails), giving h=1.
 - Delta=5: h is even.  q odd requires q>=0 (always), q even requires q>=1 (only q=0 fails), giving h=0.
 - Delta>=6: q>=0 and c<=2 imply c+4-Delta-q<=0.
Thus outside (2.2) the packing lemma realises the candidate type at every target run.  Also 2m+2<=kappa+3<=p<k.

**Genericity calculation.**  For this m and either c in {1,2}, Q of type (g+c,m) and Q+t of type (g+c+d,m+1), d in {+1,-1}, are
both generic, regardless of (2.2); (2.2) concerns only availability.  To see this without a computation, put s=(p-1)/2.  We have
m<=s-1, kappa<=2m.  The second lam term for Q is m+c, at least floor((kappa+c)/2)+1; its first term p-m+1>=m+4 is larger still.
For Q+t, the second term m+c+d+1 is at least floor((kappa+c+d)/2)+1 because c+d>=floor((c+d)/2), and the first p-m>=m+3 is at least
the third term (<=m+2).  For U(Q), the ceiling term C(c)=ceil((p+c)/2)-1 is s or s+1; the first term m-1<=s-2 and the middle term
kappa+c-m<=m+c<=s-1+c=C(c) are no larger.  For U(Q+t), its first term m<=s-1 and its middle term
kappa+c+d-m-1<=s+c+d-2 are no larger than C(c+d), which is s for c+d=0,1 and s+1 for c+d=2,3.  All four arcs therefore take their
floor/ceiling values.  By Lemma GS(b), these actual configurations establish quality seeds (or an actual empty interval).

## 3. Written seed table for the exceptional families

For (Delta,h) in {(3,0),(3,2),(4,1),(5,0)}, take m=y=g isolated aligned singles.  They are always available: kappa<=p-3 implies
g<=p-B-3<=p-5, hence 2g<=n-3.  For (Delta,h)=(3,4), take j2=1,j1=g-2, i.e. m=g-1,y=g.  Here g=B+4>=6 and p=2g-1, and
3j2+2j1=2g-1=n-B-4, so the packing lemma applies at equality.
Direct substitution into the displayed lam/U formulas gives the following values.  Every arc entry is its value MINUS g; plus/minus
refer to adding a target run of sign +1/-1.  This table is arithmetic in the free integer B>=2, not a finite-B verification.

| Delta,h | m,y | lam(Q)-g | U(Q)-g | lam(Q+t+)-g | U(Q+t+)-g | lam(Q+t-)-g | U(Q+t-)-g | seed + | seed - |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 3,0 | g,g | 0 | 1 | 1 | 1 | 0 | 0 | [0,1] | [-1,0] |
| 3,2 | g,g | 0 | 0 | 0 | 0 | -1 | 0 | [0,0] | [-1,0] |
| 3,4 | g-1,g | -1 | -1 | -1 | -1 | -2 | -1 | [0,0] | [-1,0] |
| 4,1 | g,g | 0 | 1 | 1 | 1 | 0 | 0 | [0,1] | [-1,0] |
| 5,0 | g,g | 0 | 2 | 1 | 2 | 0 | 1 | [-1,2] | [-2,1] |

For transparency on each substitution: p=2g-h+Delta, B=g-h; insert these and m,y from the second column into
min(p-m+1,y+m-g,floor((y+B)/2)+1) and max(m-1,y+B-m,ceil((p-g+y)/2)-1), then repeat at (y+1,m+1) and (y-1,m+1).
For example, in (Delta,h)=(3,4), (p,B)=(2g-1,g-4), m=g-1,y=g.  The three lam terms are g+1,g-1,g-1 and the three U terms are
g-2,g-3,g-1.  At (y+1,m+1) the minima/maxima are g-1,g-1; at (y-1,m+1) they are g-2,g-1.  This gives [0,0] and [-1,0].
In all five rows the seed intervals satisfy (QS): a_d>=(d-Delta)/2+1 and b_d<=(d+Delta)/2-1.  Lemma NW prevents wrap; Lemma GS(a)
intersects these bounds with the canonical singleton range, producing quality seeds (or an actual empty interval).

## 4. Uniform conclusion and the all-single-letter subcase

**Theorem S2-wide.**  For every prime p>=7, every all-single-letter NMH word with g=kB>=B>=2 and kappa=g+B<=p-3 has an identity
2p-subword, for every anti-run placement.
Proof.  Outside (2.2), use the packed generic configuration in Sec. 2.  Inside (2.2), use the actual configurations and seed table
in Sec. 3.  Every run obtains a quality seed or an actual empty interval.  All aligned runs have odd length 1, so n_ev,al=0.
Theorem SEED-G (C0+ case (i)) gives a contradiction to avoidance.  []

**Corollary (all-single-letter NMH subcase).**  Every all-single-letter NMH word with R=k<=2p-3, every prime p>=5, has an identity
2p-subword.
Proof.  In the NMH setting B>=1 and g=kB>=1.  If B=1, this is W(p,g), 1<=g<=p-4, covered by Theorem W-ALL (c3/proof-WALL.md,
3g<=p+4) or Theorem SEED (c6/c5-fixes/proof-SEED-r3.md, 3g>=p+5).  At p=5,7 all its g lie in W-ALL's range; Theorem SEED is used
only for p>=11 as stated there.  If B>=2, kappa=g+B>=3 implies p>=7: apply Theorem RZ-wide (c6/proof-RZwide.md) when B>=g+1, or
Theorem S2-wide when g>=B.  []
This corollary closes ONLY the all-single-letter NMH subcase.  Words with excess, parity/inverse reductions, and the full ordered
Olson problem are not settled by it.

## 5. Controls [F], not hypotheses

seedS2wide.py / out/seedS2wide.txt: every admissible (p,g,B) with prime p<=401, g>=B>=2, kappa<=p-3: 899,911 classes; 899,535 use the
default recipe and 376 use the five exceptional families (76/75/75/75/75).  Availability, genericity or the exact seed table,
quality, no wrap, P2 and PIN all pass.  Omitting the exception split violates the packing capacity in all 376 exceptional class
recipes.  Constructive smoke: 66 sampled/pinned classes in 3 layouts (198 words), 22,095 actual target configurations, all with
correct block counts/isolation and independent c5 slow_lambda arcs; no empty actual seed in this sample.  Peak child RSS 33,587,200
bytes; native CPU/file-size limits used.  Lemma RZ2's separator-deletion mutation controls are separately recorded in
c6/out/replayLB.txt (132 rejected constructions); no cross-checker's controls are being attributed to this recipe script.
