# DELTA1 middle-minus and the full uniform pair/all-odd cover - addendum v1

CANDIDATE written mathematics by hand. No review or acceptance is claimed. Drafted after `/bin/date`
2026-10-21T18:14:21-0700. This is a new argument for the middle-minus case, not a reuse of the UE-MP BAL
construction in its formerly unresolved tight cases. All permanent exposure/process history remains.

## 0. Exact scope, imports and statements

C(p,kappa) is EXACTLY the class in proof-DELTA1-UE-MP-v1.md Sec.0: p>=7 prime, length4p-2, R=p+1 rotations
in one nonzero pair, every maximal cyclic CONSTANT reflection block odd, kappa=p-1-H in[2,p-1]. Any B,
mixed/pure runs, genuine empty gaps, arbitrary reflection values and odd-block pairs. Increasing ORIGINAL
index order is required. No new hypothesis, transfer of avoidance or word-class enlargement is introduced.

THEOREM D1-MM (candidate). For every prime p>=7, every word of C(p,(p-1)/2) has an identity2p-subword.
THEOREM DELTA1-PAIR-COVER (candidate, union). For every prime p>=7 and EVERY kappa in[2,p-1], every word
of C(p,kappa) has an identity2p-subword. This is the whole operative pair/all-odd target, not ordered Olson
for arbitrary words, arbitrary high-terminal NFs, an inverse theorem, REFL or INV*.

Imports are precisely the UE-MP manuscript Secs0-2 and its own governing sources, all included literally
with whole-file SHA256/ranges in the source packet and source-bindings companion. In particular the proof
below uses only its A1-A4, Lemma GW, literal singleton/pair e5 realisations, and BAL. The baseline is used
as accepted statement-level coverage only. No raw SEG, K2P+, TOP, Fact2.1, PartII, HK1/HIGH-K-CORE, S(p),
Lev, CT, B.4 or CJ/EDGE proof step is used in this new argument. The E1 numerical band is an accepted
baseline statement; this does not re-review its transitive K2P+ proof. Direct inputs:
* UE-MP: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/delta-one-pair-cover-followon/proof-DELTA1-UE-MP-v1.md;
  SHA256 cf6444294a0bbdf3827e4458f721aef8ec96d907c1464e3eed4d7dfab5afcbda; LF11-145.
* FND: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md;
  SHA256 4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c;
  LF37-47 (S,W), LF52-64 (arcs,L2.1), LF92-108 (L3.1,BAL), through errata1-5 PartI and the foundation review Sec.C.
  The exact whole-file hashes and scopes of every overlay and own acceptance are in the packet companion.

Assume u in C(p,(p-1)/2) avoids. Apply the same order-preserving normalisation as UE-MP. Put
 e=(p+1)/2, kappa=e-1, H=e-1, k=2p-2; N_1,...,N_q, M_1,...,M_q, b_i=|M_i|, d_i=d(N_i),
 c=sum floor(b_i/2)=(k-o_M)/2.
A1-A4 give Q+: q=p+1 and every N_i singleton; Q0: q=p, one N_i has2 letters, all others singleton;
Q-: q=p-1, one N_i has3 letters, all others singleton. In Q+ d=1; in all cases d<=3.
For 2m arcs put s=p-m and Gamma(s,T)=gamma(E_+)+gamma(E_-),
 gamma(E)=min(s,E+H-s,floor(E/2)), E_+-=e+-T/2.

## 1. The exact window ranges

For p=4a+1, a>=3 (p>=7 prime), e=2a+1, H=2a:
 T=0: gamma(e)=min(s,4a+1-s,a)=a for a<=s<=3a+1, so Gamma=2a.
 |T|=2: gamma(e+1)=min(s,4a+2-s,a+1), gamma(e-1)=min(s,4a-s,a).
 For a+1<=s<=3a, these are a+1 and a, so Gamma=2a+1.
 At s=a both equal a; at s=3a+1 they are a+1 and a-1. Hence for every s in[a,3a+1] and
 T in{0,+2,-2}, both gamma>=0 and Gamma>=2a. Lemma GW therefore needs G>=2a on that larger interval,
 or G>=2a-1 when |T|=2 and s in[a+1,3a].

For p=4a+3, a>=1, e=2a+2, H=2a+1:
 T=0: gamma(e)=min(s,4a+3-s,a+1)=a+1 for a+1<=s<=3a+2, so Gamma=2a+2.
 |T|=2: gamma(e+1)=min(s,4a+4-s,a+1)=a+1 and
 gamma(e-1)=min(s,4a+2-s,a)=a on the SAME interval. Both gamma>=0; Gamma=2a+1.
 Thus G>=2a suffices for T=0 and G>=2a+1 suffices for |T|=2.
These are literal minimum calculations for the entire intervals, not sampled parameter checks.

## 2. Capacity and the cases with room for BAL

k is even, so o_M is even. Q+ permits o_M<=p+1, hence c>=(p-3)/2. Q0 and Q- permit o_M<=p-1,
hence c>=(p-1)/2. Fully pairing a reflection run means choosing floor(b_i/2) consecutive disjoint pairs;
if b_i is odd it then has exactly one FREE block, while if b_i is even it has none.

BAL construction with a one-pair reserve. Choose G0<=c disjoint pairs, then 2m0-G0 singletons on free blocks,
where s0=a+2 and m0=p-s0. This is possible if 0<=2m0-G0 and 2m0+G0<=k, the latter equivalent to
G0<=2s0-2=2a+2. At least one free block exists since 2G0<k. Fix an M_i with one. BAL changes two parities;
the change at i adds/deletes a singleton without pair loss. The partner move deletes a singleton, adds one
on an unused block, or splits a pair, losing at most one pair. Thus G>=G0-1 and the new arc count is
2m0+Delta, Delta in{-2,0,2}; s' in[a+1,a+3]. If already |T|<=d no change is needed. Every case below has
m0-1>=1. T is even, |T|<=2, and T=0 in Q+. This uses the restricted e5 rule only for singletons/pairs.

For p=4a+1: if c>=2a+1 take G0=2a+1. Blocks fit, 2m0-G0=4a-3>=0,
G>=2a, and [a+1,a+3] is contained in[a,3a+1]. Section1 and GW close EVERY Q-type.
For p=4a+3, Q+: if c>=2a+1 take G0=2a+1; 2m0-G0=4a+1>=0. Then G>=2a and T=0.
For p=4a+3, Q0/Q-: if c>=2a+2 take G0=2a+2; 2m0-G0=4a>=0. Then G>=2a+1.
In both p=4a+3 cases [a+1,a+3] is contained in[a+1,3a+2]. Thus GW closes these cases.

All-odd tight construction. If every b_i is odd and the capacity c is one of the following values, take ALL
c pairs and again s0=a+2. Each M_i has one free block; the needed 2m0-c singletons fit as follows:
 p=4a+3, Q+, c=2a: q=4a+4 free blocks; 2m0-c=4a+2.
 p=4a+3, Q-, c=2a+1: q=4a+2 free blocks; 2m0-c=4a+1.
 p=4a+1, Q-, c=2a: q=4a free blocks; 2m0-c=4a-2.
BAL changes each parity by adding/deleting its free singleton, so NO pair is lost. The same s' intervals
apply, and the G/T requirements of Section1 are met. These cases are forced all-odd: c at its stated value
gives o_M=q. Thus every case except the tight Q0 and two tight Q+ cases below is now closed.

## 3. Direct parity choices with rigid reflection runs

Fix full pairing in every M_i, with g_i=floor(b_i/2). In each odd M_i choose x_i in{0,1}: its free block is
unused or is a singleton. Then c_i=g_i+x_i. In an even M_i put x_i=0; call it RIGID. For any z_i in{+1,-1}
satisfying z_(i+1)=(-1)^(g_i) z_i at every rigid edge, set x_i at every flexible edge so that
 z_(i+1)=(-1)^(g_i+x_i) z_i.
This defines a valid singleton/pair choice. Around the cycle the product of these relations is1, so
sum_i(g_i+x_i) is even. Therefore the arc count is 2m=c+x, x=sum x_i; the corresponding T is sum z_i d_i
up to the immaterial global sign. The choices below have m>=1 and use at most k blocks, since all pairs
are disjoint and only their free blocks are used.

Lemma DP1 (one rigid edge, Q0). For p>=7, some such z has T=0.
Proof. Let the rigid edge join N_j,N_(j+1). Choose their signs consistently with its fixed relation and let
f=z_j d_j+z_(j+1)d_(j+1). There is exactly one length-two run N_r with d_r in{-2,0,2}; all other d_i are+-1.
If r is one of j,j+1, then f is odd and |f|<=3. The remaining p-2 singleton contributions are freely+-1;
their sums are precisely the integers of parity p-2 in[-(p-2),p-2], so they can sum to -f.
If r is outside the pair, then f is even and |f|<=2. Choose z_r arbitrarily and put g=z_r d_r, even with
|g|<=2. The remaining p-3 singleton contributions are freely+-1 and can sum to -(f+g), since p-3>=4,
|f+g|<=4 and its parity is even. All unconstrained signs are free because the other edges are flexible. []

Lemma DP2 (two rigid edges, Q+). For p=4a+1>=13, some compatible z has T=0.
Proof. The two rigid edges are distinct and do not form a cycle (q=p+1>=14). Their endpoint set K has
3 or4 vertices. Assign signs satisfying both edge relations on K; this is possible on a path or on two
disjoint edges. Its contribution f has |f|<=|K|<=4 and f=|K| mod2, since all d_i are+-1.
All other q-|K| signs are free. Their contributions fill the integers of parity q-|K| in the interval
[-(q-|K|),q-|K|]. Now q is even, so this parity equals |K|, and q-|K|>=p-3>=10>=|f|.
Choose these contributions to sum to -f. []

Tight Q0: c=(p-1)/2 implies o_M=p-1 and q=p, so exactly ONE b_i is even. Use DP1 and full pairing.
For p=4a+1, c=2a is even; x is even and 0<=x<=p-1=4a. Thus a<=m<=3a,
so a+1<=s<=3a+1. T=0, Gamma=2a, G=c=2a, and GW holds.
For p=4a+3, c=2a+1 is odd; x is odd and 1<=x<=p-2=4a+1. Thus a+1<=m<=3a+1,
so a+2<=s<=3a+2. T=0, Gamma=2a+2, G=c=2a+1, and GW holds.
No BAL partner can consume a pair, since BAL is NOT used in these two tight Q0 cases.

Tight Q+, p=4a+1, c=2a: then o_M=4a=p-1 and q=p+1, so exactly TWO b_i are even. Use DP2 and full pairing.
x is even and 0<=x<=p-1=4a; hence a<=m<=3a and a+1<=s<=3a+1.
T=0, Gamma=2a, G=2a, and GW holds.

## 4. The all-flexible one-short Q+ case

It remains p=4a+1, c=2a-1. Here o_M=4a+2=q=p+1, so every b_i is odd. Fully pair every M_i.
All edges are flexible and every sign vector z can be realised by Section3. Since every d_i is+-1,
choose contributions w_i=z_i d_i with exactly2a+2 of them+1 and2a of them-1. Then T=2.
Let F be the edge set where z changes sign, and P0={i:g_i odd}. The free-singleton set is
D=F symmetric-difference P0; x=|D|. Since c=2a-1 is odd and total arc count is even, x is odd,
so 1<=x<=q-1=4a+1. If x>=3 retain this vector.
If x=1, pick a vertex with w=+1. Among the2a>=6 vertices with w=-1, at most2 are its cyclic neighbours;
choose one that is NOT adjacent. Flip z at these two vertices. The +1 becomes-1 and the -1 becomes+1,
so T remains2. Their four incident edges are distinct, and F changes on exactly those four edges.
Consequently the new D has size3 (if its old single edge was among those four) or5 (otherwise).
Thus a realisation with 3<=x<=4a+1 exists; the upper bound also follows from x odd and q even.
Now 2m=c+x gives a+1<=m<=3a, hence a+1<=s<=3a. Section1 gives Gamma=2a+1 at |T|=2.
G=c=2a-1, so Gamma+G=4a=p-1. Lemma GW gives an identity2p-subword, contradiction.
This resolves the one-short T=0 obstruction by changing the actual target value T, not by inventing capacity.

## 5. Exhaustion and the full union

Every avoider has one of Q+,Q0,Q-. For p=4a+1 the capacity ranges are:
 Q+: c>=2a+1 (Section2), c=2a (DP2), or c=2a-1 (Section4).
 Q0: c>=2a+1 (Section2) or c=2a (DP1).
 Q-: c>=2a+1 (Section2) or c=2a (all-odd Section2).
For p=4a+3 they are:
 Q+: c>=2a+1 (Section2) or c=2a (all-odd Section2).
 Q0: c>=2a+2 (Section2) or c=2a+1 (DP1).
 Q-: c>=2a+2 (Section2) or c=2a+1 (all-odd Section2).
All cases contradict avoidance, proving D1-MM at EVERY prime p>=7. The prime split includes p=7 (a=1)
and p=11 (a=2) in the second class and p=13 (a=3), p=17 (a=4) in the other. No finite substitute is used.
In particular (p,kappa)=(7,3),(11,5),(13,6),(17,8) are closed by this genuinely new direct-parity argument.
For p>=19 the same theorem duplicates the accepted B-prime middle-minus coverage; NO additional cell
credit is assigned there and no independent corroboration is claimed.

For the whole target retain the baseline of UE-MP Sec6 at its own accepted scope. For p>=11, the consecutive
bands/singletons [2,(p-5)/2], {(p-3)/2}, {(p-1)/2}, {(p+1)/2}, [(p+3)/2,p-4], {p-3,p-2,p-1}
partition[2,p-1] (an interval with its lower endpoint above its upper is empty). Providers are respectively
accepted RP-2NE, accepted D1-END, new D1-MM, new D1-MP, accepted RPdelta E1, new D1-UE.
For p=7, kappa2 is D1-END, kappa3 is D1-MM, kappa4 is D1-MP (the UE exception), and kappa5,6 are D1-UE.
Thus the full operative DELTA1-PAIR-COVER is proved IN THIS CANDIDATE UNION. No residual or unproved
step remains relative to the declared accepted statements. Parent hand check and both-family complete-source
gates are still required. This is neither an unconditional statement beyond those imports nor any claim about
p=5, arbitrary words/NFs, other rotation counts, REFL, INV*, full ordered Olson or a priority/novelty result.

## 6. Proof boundary and process

UE-MP Sec5 correctly records failure of that particular BAL construction. It is not a no-go theorem. This
addendum supplies direct parity choices that the old construction lacked. UE-MP Sec6's FOUR-cell residual
and its D1-SMALL-MIDDLE status are superseded ONLY as candidate conclusions by the new proof above.
The original file remains unchanged. No computational scientific step or model review was used. New reasoning
followed the already-published exposure acknowledgement, not a second freeze. The checkpoint/source ledger
records the continued cadence, draft creation and exact used/not-used sources. All old process departures
remain permanent and uncured. Parent alone runs reviews and makes acceptance/frontier decisions.
