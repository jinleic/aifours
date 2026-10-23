# DELTA2 arc cover v1 - every kappa>=3, and the whole-target union with LOW

Drafted after `/bin/date`2026-10-21T20:20:50-0700; exclusive immutable candidate manuscript.

CANDIDATE written mathematics by hand. No parent/model gate or acceptance is claimed. This re-derives
EVERY R-dependent window/count at R=p+2 from the literal general foundations, rather than plugging R2
into a DELTA1 lemma. Earlier same-author/reviewer-lead exposure and all process qualifications remain.

## 0. Scope, declarations and direct inputs

C2(p,kappa): p>=7 prime; a word u of length4p-2 over D_(2p) with EXACTLY R=p+2 rotations in ONE nonzero
pair{rho_c,rho_-c}; every maximal CYCLIC CONSTANT reflection block odd; kappa=p-1-sum floor(l_i/2) in[2,p-1].
Any B, mixed/pure rotation runs, genuine empty gaps, all reflection values and all odd-block pairs. Identity
means EXACTLY2p positions in increasing ORIGINAL index order. No purity/B<kappa/inherited/original-o_F/
nonempty-gap/new-rigidity/feasibility premise, and no inverse avoidance transfer.

THEOREM D2-ARC (candidate): every word of C2(p,kappa) with3<=kappa<=p-1 has an identity2p-subword.
We prove uniform MP, MM, TOP4, and END(p>=11) below, then compose ONLY the exact accepted baseline bands.
The separate proof-DELTA2-LOW-v1.md proves kappa2 for EVERY p>=7 independently of this manuscript.
Together they give the candidate full DELTA2-PAIR-COVER; no residual/unproved step remains relative to the
declared interfaces. Neither manuscript alone claims all kappa. No wider R, arbitrary-word/REFL/INV* or
full ordered-Olson statement, priority, Lean, human-review or runtime claim is made.

Own accepted inputs, all at their literal scopes (absolute path; WHOLE-file SHA256; inclusive original LF):
* FND authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md;
  13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547;1-61, with ALL bindings and errata1-5 PartI.
* FND body: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md;
  4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c;12-64(CD,S,W,L2.1),92-108(L3.1,BAL).
* Governing e5: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-2.md;
  b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820;1-21, singleton/pair choices ONLY.
* I6/I7 and all PartI: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5-erratum-5.md;
  40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4;1-164. Any applicable add/delete
  singleton move is valid; the displayed priority order is sufficient, not compulsory.
* Normalisation/P0: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md;
  6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1;12-75, with own authority and the
  current full TheoremP own proof/acceptance/both errata. No RED process or CJ/TRANSFER premise is used.
* Baseline lower band: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP2NE-parent-verdict-v1.md;
  320d817a4b24d2c39f04806ce84ab1977fd68f5869b8c7be0da5184d166d2eab;1-33, delta2 kappa[3,(p-5)/2].
* Baseline upper band: FND own authority above, LF1-61, through all bindings: delta2 kappa[(p+3)/2,p-5].
  These TWO baseline theorems are unreplayed accepted-statement interfaces, not new transitive proof claims.

Classical Cauchy-Davenport(CD): nonempty subsets A_j of Z_p have |sum A_j|>=min(p,1+sum(|A_j|-1)).
PartII is accepted but NOT USED. Raw SEG, K2P+, TOP, ARC+/SEG segments, Fact2.1 and Lemma3.2 are NOT
premises of the new proofs (the baseline I14 band is separately declared). Optional short segments are
proved directly below. No DELTA1 lemma, S(p), Lev, CT, HK1/HIGH-CORE or new model lead is assumed.
All direct foundation bodies/own authorities/mandatory overlays travel; source coverage states partial
ranges and accepted-statement boundaries without claiming every transitive body was pasted.

## 1. Actual R2 avoider data and pair capacity

Assume u in C2 avoids. Normalise c=1,A>=B by the order-preserving automorphisms; F=3p-4>=1.
Put h=(p+1)/2, Pi=(p-3)/2=h-2, H=p-1-kappa, k=3p-4-2H. Here k is ODD.
Let N_1,...,N_q be the nonempty rotation runs in cyclic order; M_i the reflection run between N_i,N_(i+1),
b_i=number of constant blocks of M_i>=1. Each internal run of M_i is genuinely empty, so adjacent block
values differ. Put x=R-q. P0 gives at least2p-R=p-2 odd nonempty runs, whence
 0<=x<=4, q=p+2-x, d=max|d(N_i)|<=x+1.                                                    (D1)
Indeed any N_i has at most R-(q-1)=x+1 letters. Write t=floor(x/2) in{0,1,2}.
T=sum z_i d(N_i) is ODD for every labelling, since sum r(N_i)=p+2 is odd. BAL gives |T|<=d,
hence |T|<=2t+1. No parity/run-purity strengthening is assumed.

A pair is a two-consecutive-block arc inside one M_i; its two values differ. A singleton is one block.
Pair capacity c=sum floor(b_i/2)=(k-o)/2, where o=#{i:b_i odd}. Since k is odd, o is odd and o<=q.
Consequently, with u0=ceil(x/2),
 c>=p-3-H+u0.                                                                           (D2)
If q is odd(x even), o<=q gives this bound; if q is even(x odd), o<=q-1 gives it.
Full pairing in an odd M_i leaves exactly one free block; in an even M_i it leaves none.

## 2. Fresh window, direct GW2 and optional short segments

For 2m>=2 disjoint singleton/pair arcs put s=p-m and E_+-=(R+-T)/2. With kappa=p-1-H,
 gamma_m(E)=min(s,E+H-s,floor(E/2)).                                                       (W2)
If both gamma are nonnegative and Gamma(s,T):=gamma(E_+)+gamma(E_-) satisfies
 Gamma(s,T)+G>=p-1, where G is the number of pair arcs, then an identity2p-subword exists.  (GW2)
Proof. Label arcs cyclically X_1,Y_1,...,X_m,Y_m. L2.1 yields proper patterns with exactly m intervals,
E+ independent of chosen endpoints, {E+,E-}={E_+,E_-} by L3.1, and u_P=(sum y_a-sum y_b)/2.
The attained u-set contains a CD sumset of singleton sets and G two-value sets, of size>=min(p,G+1).
The W interval contains0 and has Gamma+1 integers, hence min(p,Gamma+1) residues. If either count is p,
the sets meet; otherwise their sum>=p+1 by(GW2), so they meet. W gives the required subword. []

For actual |T|=2j+1, 0<=j<=t, {E_+,E_-}={h+1+j,h-j}. Their floor-halves sum to h.
BOTH gamma equal their floor values whenever
 alpha_t:=floor((h+1+t)/2) <= s <= beta_t:=H+ceil((h-t)/2).                                (F_t)
This checks the largest E for s>=floor(E/2), and the smallest E for s<=H+ceil(E/2), hence every intermediate
j as well. Directly beta_t-alpha_t=H-t for t0/1/2, by substituting h even/odd. These are NEW R2 windows.
In particular for T1, let
 L_H:=p-H-ceil(h/2), U_H:=p-floor((h+1)/2).
Then every m in[L_H,U_H] has the same W interval of h+1 integers (both floor endpoints).

Optional short-segment lemma (fresh). Reserve a segment of L consecutive blocks, L in{3,4,5}, disjoint
from a base arc system; its internal runs are empty. It may add0,2,...,2floor(L/2) singleton arcs, without
changing T or the IN/OUT labels of any nonempty N_i. Its additional u-values, with a fixed sign, form a
set of at least L residues, so its guaranteed gain is L-1 and m rises by at most floor(L/2).
Proof. Put delta_i=y_(i+1)-y_i!=0 within the segment. Every subset J of its L-1 successive edges is a union
of at most floor(L/2) separated intervals[a,b]; choose endpoint blocks a,b+1 for each. The added u-value
is, up to one fixed sign and halving, sum_(i in J)delta_i. All subset sums of the nonzero deltas occur,
so CD applied to {0,delta_i} gives at least min(p,L)=L residues. Inserting an even number of arcs inside
one empty-run region preserves both outer gap labels. Different reserved segments contribute independently
with their fixed signs; the L2.1 telescoping formula gives the asserted additional sumset. []

Thus if a base with G pairs and reserved lengths L_a has T1, all m from m_b through m_b+sum floor(L_a/2)
lie in[L_H,U_H], and G+sum(L_a-1)>=Pi, an identity follows: the u-set has at least min(p,1+Pi) residues,
the fixed floor window h+1, and (Pi+1)+(h+1)=p+1. This is proved from W/L2.1/CD, not imported ARC+.

## 3. Two fresh BAL constructions

Flexible construction. Choose G0<=c disjoint pairs and2m0-G0>=0 singleton arcs on other blocks, possible
if G0+2m0<=k. Suppose k-2G0>0. Some M_i has a free block; realise the BAL change there by adding/deleting
a singleton, with NO pair loss. At its partner use the restricted e5 move: delete singleton, add singleton,
or split pair. Then G>=G0-1, arc count2m0+Delta with Delta in{-2,0,2}, and s' in{s0-1,s0,s0+1}.
If a pair IS lost, its split adds an arc; therefore Delta>=0 and s'<=s0. If every M_i has a free block
and all pair capacity is retained, both changes add/delete singletons and G is unchanged. Already balanced
T needs no move. Every use below retains at least2 arcs and consists only of singletons/pairs.

Fixed-count construction. Suppose c>=G0+1, G0+2m0<=k-1 and2m0-G0>=1.
Choose M_l with at least2 blocks; designate its initial two blocks as one singleton and one reserved UNUSED
block. Removing these two lowers capacity by exactly1; choose G0 pairs among the rest and fill the other
2m0-G0-1 singletons outside those pairs and the reserved block. The stated block inequality ensures room.
Apply BAL at l. If the partner adds an arc, delete the designated singleton; if it deletes an arc, add the
reserved singleton. Both realise the parity flip by I7. Total arc count stays2m0 and at most ONE pair is
lost(at the partner), so G>=G0-1. No unsupported parity move on a longer arc occurs. []

## 4. Fresh direct-parity filling and counting bounds

After reserving short segments and fully pairing each remaining M_i, every odd-length remainder has ONE
free block (unused or singleton). A run with even remainder has none; call its edge RIGID. Let g_i be its
number of fixed pairs. For any signs z_i satisfying z_(i+1)=(-1)^(g_i)z_i at each rigid edge, set the free
bit a_i in{0,1} at every other edge to realise that same relation with g_i+a_i. The product around the cycle
is1, so G+xi is even, G=sum g_i, xi=sum a_i. This gives a genuine base of2m_b=G+xi arcs.
A fixed complete free-bit pattern determines z up to global sign; at most ONE of these two signs has T1.
This last observation bounds bad T1 labellings by the number of bad free-bit sets, without enumerating data.

Sign-fill lemma. Let J be in{2,3,4}. Suppose r rigid edges, excess x=R-q, r+x<=J, and p+2-2J>J, r<q.
Then a compatible T1 labelling exists, in fact at least two. For J2,p>=11 there are at least C(p-2,3)
such labellings. (We use J2 at p7 only for the at-least-two conclusion.)
Proof. Rigid edges form a forest of paths. Fix signs within each nontrivial path component up to its global
orientation; include every non-singleton rotation vertex outside these paths as a separate component.
The signed contribution of a path has magnitude<=number of its vertices plus the total excess x, hence
<=r+1+x<=J+1; the same bound holds for an isolated deviant. Orient these components greedily against the
current sum to obtain total absolute value<=J+1, then flip all assigned signs if needed to make F>=0.
All remaining vertices are FREE SINGLETON rotations, n>=q-(2r+x)>=p+2-2J. Their contributions are freely+-1.
The required sum1-F has magnitude<=J<n and the parity of n, since total rotation mass is odd. It is
attainable in at least two ways. For J2,p>=11, n>=p-2>=9 and |1-F|<=2; the number of choices is at least
C(n,3)>=C(p-2,3), by the monotonicity of binomial coefficients up to the middle. []

One-rigid-edge singleton count. If x0 and exactly ONE rigid edge, the number of compatible T1 labellings
is at least C(p,(p-1)/2): in contributions w_i=z_i d(N_i), the constrained pair is either equal or opposite.
In the equal case choose both+1 and let the other p signs sum to-1; in the opposite case choose+1,-1 and
let the other p signs sum to1. Both give that binomial lower bound.
For p>=7,
 C(p,(p-1)/2)>=C(p,3)>1+C(p+1,2),                                                        (C1)
because C(p,3)-C(p+1,2)=p((p-3)^2-10)/6>=p>1.
For p>=11, putting n=p-2>=9 gives
 C(p-2,3)>1+C(p+1,2).                                                                    (C2)
Indeed C(n+3,2)<=2C(n,2), since n^2-7n-6=(n-9)(n+2)+12>=0, while
C(n,3)>=(7/3)C(n,2) and C(n,2)/3>=12>1. These are symbolic counting inequalities, not enumeration.

## 5. Middle-plus: kappa=h for EVERY p>=7

Here H=h-2,k=2p-1=4h-3, and(D2) gives c>=Pi+ceil(x/2).
If c>=Pi+1 choose G0=Pi+1=h-1 and s0=alpha_t+1, except the p7,t1/t2 cases below.
For p>=11, h>=6 and beta_t-alpha_t=h-2-t>=2, so s0-1,s0,s0+1 all lie in(F_t).
The block budget is G0+2m0<=k iff2s0>=h, true by alpha_t>=h/2; and
2m0-G0=3h-1-2s0>=2h-6>=0. A free block exists(k-2G0=2h-1>0).
The flexible construction leaves G>=Pi and full floor sum h, so GW2 applies.
The same calculation works for p7,t0, where(F_0)=[2,4] and s03.

If c=Pi, (D2) forces x0 and o=q=p+2: EVERY b_i is odd. Fully pair all c pairs and use s0=alpha_0+1.
Each M_i has one free block;2m0-Pi=3h-2s0 fits among q=2h+1 free blocks since2s0>=h-1.
The flexible construction costs NO pair. (F_0) has width h-2>=2, so all three s' have full floor windows,
and G=Pi suffices. No lower capacity occurs.

p7,t1: use s04,G03,k13;2m06,3 singletons fit. The full-floor interval is[3,4]. A pair loss implies
s'<=4, hence s'3/4 and Gamma4 with G>=2. If s'5 both moves deleted arcs, so NO pair loss and G3;
at s5 both T1 and T3 have Gamma3 (respectively gamma pairs(2,1),(3,0)). In all cases Gamma+G>=6.
p7,t2: then x4,c>=4. Use fixed-count construction G03,s03,m04: G0+2m0=11<=k-1=12,
2m0-G0=5>=1. Its full-floor interval(F_2)={3}, so G>=2 and Gamma4 give6.
This proves D2-MP at its ENTIRE scope. []

## 6. Middle-minus: kappa=h-1 for EVERY p>=7

Here H=h-1,k=2p-3=4h-5, and c>=Pi-1+ceil(x/2).
For c>=Pi+1 use G0=Pi+1,s0=alpha_t+1. All three s' are in(F_t) unless p7,t2:
H-t>=2 otherwise. Block budget holds since2s0>=h+2;2m0-G0>=2h-6>=0;
k-2G0=2h-3>0. Flexible BAL gives G>=Pi and full floor sum h.
p7,t2: use s04,G03,k11. (F_2)=[3,4]. If a pair is lost s'3/4 and Gamma4 suffice with G>=2.
If s'5 no pair is lost,G3, and Gamma>=3 for every T1/3/5: the gamma pairs are(2,2),(3,1),(3,0).
All are nonnegative and GW2 applies.

For c=Pi, x<=2 and the number of even M_i is r=2-x. Fully pair every M_i; r+x=2, so the sign-fill lemma
at J2 gives at least two T1 labellings for every p>=7. There are f=q-r=p free bits. Write epsilon=h mod2.
G=Pi=h-2, xi=epsilon mod2,0<=xi<=p. The T1 floor m-window is
 [floor(h/2), U_H]. It contains m=(h-2+xi)/2 provided xi>=2-epsilon;
the upper bound is automatic(xi<=2h-epsilon). When epsilon1, parity already gives xi>=1.
When epsilon0, avoid xi0: at most one T1 labelling has that free-bit pattern, and at least two exist.
Thus G=Pi and the T1 window give an identity.

For c=Pi-1, (D2) forces x0 and all M_i odd. Since c=Pi-1>=1, some b_l>=3.
Reserve its initial3 blocks as an optional segment and fully pair all other remaining blocks.
G=c-1=Pi-2=h-4>=0, exactly one edge becomes rigid, and f=p+1=2h free bits remain.
The one-rigid-edge count(C1) exceeds1+C(p+1,2). Parity gives xi=epsilon mod2.
We need the base m_b and m_b+1 inside[floor(h/2),U_H], which is exactly
 4-epsilon<=xi<=2h-epsilon.
The upper bound is automatic from f and parity. If epsilon0 the bad choices are xi0/2, at most
1+C(p+1,2) free-bit sets; if epsilon1 only xi1 is bad, at most p+1 such sets. Each determines at most
one T1 labelling. Therefore a good labelling exists. The base has at least2 arcs, its optional segment
has gain2 and m-rise<=1; G+2=Pi. Section2's optional-segment kill applies.
All capacities are exhausted, proving D2-MM uniformly, including p7. []

## 7. Lower-middle endpoint: kappa=h-2 for EVERY prime p>=11

Here H=h,k=2p-5=4h-7,h>=6 and c>=Pi-2+ceil(x/2).
If c>=Pi+1, take G0=Pi+1=h-1 and s0=alpha_t+2. (F_t) has width h-t>=4, so all s' stay in it.
The block budget is2s0>=h+4, true since2alpha_t>=h; and
2m0-G0=3h-1-2s0>=2h-8>=0, with k-2G0=2h-5>0. Flexible BAL gives G>=Pi and full floor sum h.

It remains c in{Pi,Pi-1,Pi-2}. Put epsilon=h mod2 and
 L=floor(h/2)-1, U=p-floor((h+1)/2).
This is the T1 floor m-window[L_H,U_H] for H=h. All short-segment bases below have m_b>=L>=2.

c=Pi. Here o=k-2c=p-2 and r=q-o=4-x rigid edges after full pairing. Thus r+x=4;
the sign-fill lemma at J4 applies(p>=11), giving T1. There are f=q-r=p-2=2h-3 free bits.
G=Pi=h-2 and xi=epsilon mod2. Every such xi gives m=(h-2+xi)/2 in[L,U]:
the lower required bound is xi>=-epsilon, automatic; the upper is xi<=2h-epsilon, also automatic.
So GW2 with G=Pi applies directly, with arbitrary deviant rotation runs retained.

c=Pi-1. Now x<=2, o=p, r=2-x and c=h-3>=3. Some M_i has b_i>=3: otherwise c=r<=2, impossible.
If an odd b_i>=3 exists, reserve its initial3 blocks. It costs1 pair, gives optional gain2 and m-rise<=1.
After full pairing the rest, G=Pi-2=h-4; that edge becomes rigid, so r'=3-x and f=q-r'=p-1=2h-2.
J3 sign-fill applies(p+2-6=p-4>3), giving at least two T1 labellings. The requirement
 m_b,m_b+1 in[L,U]
is exactly2-epsilon<=xi<=2h-epsilon. The upper bound follows from f; parity gives xi=epsilon mod2.
When epsilon1 its lower bound is automatic. When epsilon0 only xi0 is bad; at most one T1 labelling has
that fixed free-bit pattern. Choose another. The optional segment kill has G+2=Pi.

If no odd b_i>=3 exists, choose an even b_i>=4 and reserve its initial4 blocks. It costs2 pairs, gives
optional gain3 and m-rise<=2. The rigid count stays r'=2-x, f=p=2h-1, G=Pi-3=h-5.
J2 sign-fill and its strong count give at least C(p-2,3)>p compatible T1 labellings(C2).
The required range m_b,...,m_b+2 in[L,U] is
 3-epsilon<=xi<=2h-1-epsilon.
The upper bound is automatic from f and xi=h-5 modulo2. For epsilon0, only xi1 is bad(at most p patterns);
for epsilon1, only xi0 is bad. Thus a good T1 labelling exists, and G+3=Pi kills.

c=Pi-2. Necessarily x0 and every b_i odd; c=h-4>=2. If one b_i>=5, reserve its initial5 blocks.
Otherwise every b_i is1 or3 and at least two are3; reserve those two distinct3-block runs.
Either choice costs2 pairs, gives TOTAL optional gain4 and total m-rise<=2. After pairing the rest,
G=Pi-4=h-6>=0, and r' is1 or2. The free-bit count f is p+1 or p. All rotation runs are singletons.
J2 sign-fill gives at least C(p-2,3)>1+C(p+1,2) T1 labellings(C2). We need
 m_b,...,m_b+2 in[L,U], equivalently4-epsilon<=xi<=2h-epsilon.
The upper bound is automatic from f and parity xi=epsilon mod2. For epsilon0, bad xi0/2 account for at
most1+C(p+1,2) free-bit sets; for epsilon1, bad xi1 accounts for at most p+1. Each gives at most one T1
labelling, so a good one exists. The optional segment kill has G+4=Pi.
All capacities are exhausted; this proves D2-END at every p>=11. []
For p7 its nominal endpoint kappa2 is NOT asserted by this arc argument; the separate LOW proof handles it.

## 8. All FOUR top ends: H in{0,1,2,3}, EVERY prime p>=7

This is kappa in{p-1,p-2,p-3,p-4}, with overlaps handled as one word class. For p7,H2 andH3 are respectively
MP(kappa4) andMM(kappa3), already proved. We now prove H0/H1 for all p and H2/H3 for p>=11.
Write u0=ceil(x/2),t=floor(x/2),alpha_t=floor((h+1+t)/2). The following table gives a fixed-count choice;
Gamma_min holds for EVERY actual odd T with |T|<=2t+1, and both gamma are nonnegative.

| H | t | s0 | G0 | Gamma_min |
|---|---|---|---|---|
| 0 | 0 | alpha_0 | h-1 | h |
| 0 | 1 | alpha_1 | h | h-1 |
| 0 | 2 | alpha_0 | h+1 | h-2 |
| 1 | 0 or1 | alpha_t | h-1 | h |
| 1 | 2 | alpha_2 | h | h-1 |
| 2 or3 (p>=11) | 0,1,2 | alpha_t | h-1 | h |

Window calculation in full. For H>=2, s0=alpha_t lies in(F_t), since H>=t; both gamma are full floors.
For H1,t<=1 the same reasoning applies. To check ALL other minima, write actual |T|=2j+1.
If h=2a+1(p=4a+1, hence a>=3), then alpha_0=alpha_1=a+1,alpha_2=a+2.
At H0,s=alpha_0, the gamma pairs(Emax,Emin) for j0,1,2 are
 (a+1,a), (a+1,a-1), (a+1,a-2), respectively; their sums are h,h-1,h-2.
At H1,s=alpha_2 they are (a+1,a),(a+1,a-1),(a+2,a-2), summing h,h-1,h-1.
If h=2a+2(p=4a+3,a>=1), then alpha_0=a+1,alpha_1=alpha_2=a+2.
At H0,s=alpha_0 the pairs are (a+1,a+1),(a+1,a),(a+1,a-1), summing h,h-1,h-2.
At H0,s=alpha_1, for j0/1 the pairs are (a+1,a),(a+2,a-1), both summing h-1.
At H1,s=alpha_2 the pairs are (a+1,a+1),(a+2,a),(a+2,a-1), summing h,h,h-1.
These follow by literal substitution in(W2); all entries are>=0 even at p7(a1 in the second case).
They prove every row, including smaller j than the displayed worst t, without a sample-prime substitute.

We check the fixed-count construction's hypotheses, not merely its gain.
(D2) says c>=2h-4-H+u0. For H0,t0 this is>=h=G0+1(h>=4); for t1,u0>=1 it is>=h+1;
for t2,u0=2 it is>=h+2. For H1,t2 it is>=2h-3>=h+1=G0+1.
For H1,t<=1 it is>=h unless p7,x0; for H2/H3,p>=11 it is>=h unless p11,H3,x0.
Except for those two minima, c>=G0+1. In the exceptional parameters, if the actual c is any larger the
same fixed-count construction applies; only their minimum capacities need the separate cases below.

The block budget G0+2m0<=k-1 is equivalent, row by row, to the following lower requirements on2s0:
 5-h;6-h;7-h;7-h;8-h;2H-h+5, respectively.
They hold since2alpha_t>=h,h>=4, and in the final row h>=6,H<=3.
Also2m0-G0=4h-2-2s0-G0>=2h-6>=2, since2s0<=h+3 andG0<=h+1.
Thus a designated singleton exists, pair capacity after reserving two blocks is enough, and the full fixed-
count construction is valid. It leaves G>=G0-1. Every row satisfies
 Gamma_min+(G0-1)=p-1,
so GW2 kills. There is no hidden double pair loss or shift outside a zero-width window.

Exception p7,H1,x0,c3. Here q9,k15,all b_i odd. Fully pair all3 pairs and choose s03,m04, with5 singletons
on its9 free blocks. Flexible BAL loses NO pair. For T1, s'2/3 has Gamma4 and s'4 has gamma pair(2,1),
Gamma3. Thus Gamma+G>=3+3=6. (If c>=4 the table's fixed-count construction already works.)
Exception p11,H3,x0,c5. Here q13,k23,all b_i odd. Fully pair all5 pairs and choose s04,m07, with9 singletons
on its13 free blocks. Flexible BAL loses NO pair. Its s'3/4/5 lie in(F_0)=[3,6]; Gamma6 and G5 suffice.
(If c>=6 the table's fixed-count construction works.)
This proves the FULL uniform TOP4 statement, and in particular the mandatory three upper ends. []

## 9. Entire arc class and full DELTA2 union; exact credit boundary

For every p>=11 the pieces
 [3,(p-5)/2], {(p-3)/2}, {(p-1)/2}, {(p+1)/2}, [(p+3)/2,p-5], {p-4,p-3,p-2,p-1}
cover EVERY integer3<=kappa<=p-1. Providers: accepted RP-2NE, new END, new MM, new MP, accepted I14,
new TOP4. Empty intervals are interpreted literally. At p7, kappa3 isMM,kappa4 isMP,kappa5/6 areTOP4.
Hence D2-ARC covers its ENTIRE stated class, not just the diagnostics. Its remaining whole-target class is
EXACTLY kappa2; the separately complete LOW manuscript covers that class at every p>=7.
Combining these two independent-in-logic manuscripts proves the full candidate DELTA2-PAIR-COVER for
EVERY p>=7 and EVERY kappa in[2,p-1]. No residual/unproved lemma remains relative to the declared imports.
Both-family COMPLETE-source gates and parent hand check are still pending; this is NOT acceptance.

The actual Step0 U2 baseline remains as recorded in DELTA2-baseline-audit-v1.md. Bprime ALREADY supplies
MM and END for p>=19. Their uniform new proofs are UNCREDITED duplicates there, not independent
corroboration. Additional AnyB middle cells are MM at p7/11/13/17 and END at p11/13/17; p7 END=kappa2
is the LOW theorem. The B0 CJ subcases of LOW/(7,3)/(11,4) were already known, but do not cover AnyB words.
TOP4/MP/MM overlaps at p7 are counted once. No comparison with an unverified literature/SOTA claim.

Mandatory uniform diagnostics now have candidate proofs: LOW kappa2(allp), MIDDLES MM/MP(allp, with old
Bprime credit retained), UPPER three ends(allp) within the stronger TOP4 theorem. The additional p-4 and
small-prime lower-middle obligations were NOT dropped. Every original word variable and genuine-gap rule
remains; no representative, fixed prime list or auxiliary filter replaces an entire target family.

## 10. Process and source boundary

All mathematics was derived by hand after the published DELTA2 acknowledgement and mandatory Step0
report. Prior DELTA1 mechanisms are disclosed exposure, not theorem imports or independent corroboration.
There is one pre-creation in-memory sign-fill-domain wording clarification(J explicitly2/3/4) and one
pre-creation broadening of a source citation to its complete own authority LF1-61; no frozen file is edited.
Source/metadata checks do not certify proof-creation chronology. The1674s checkpoint gap is a474s target
miss below1800; the intervening clock was NOT a checkpoint and never resets/cures the record.

No scientific code/computation/enumeration/assertion/solver/test/Lean/native/modelCLI/network/nested
agent/old-file overwrite or deletion. Classical binomial/CD counting proves existence, not a finite search.
The final packet must supply BOTH full manuscripts, scope/ack/checkpoints, every direct foundation with
own authority/mandatory overlays, generic CONNECT/LIGHT for LOW, current TheoremP own chain, and the
baseline own statements at their explicit unreplayed trust boundary. Read-only exposure sources are
named as such, not silently promoted to used premises or claimed fully pasted. Any omitted load-bearing
body requires BOTH families on a complete new input before promotion. Parent alone reviews and decides.
