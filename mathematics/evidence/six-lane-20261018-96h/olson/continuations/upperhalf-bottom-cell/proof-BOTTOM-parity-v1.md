# BOTTOM: empty-run exclusion and an odd-gap row-critical bottleneck, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:47:44-0700. CANDIDATE_UNVERIFIED, LABELLED PARTIAL / NECESSARY PROFILE, not a
bottom-cell solution. Scope BOTTOM-scope-v1.md SHA256 ab9ee0251454d4242b2d268e73eacacf875df6172467f3a24fef6c3cbc22d99e was frozen
2026-10-19T18:30:34-0700 before derivation. Authority RUN/control/written-olson-upperhalf-bottom-transition-v1.json SHA256
a0deb9816a303dc65d75b7728889696e2dcc2cfb3e53d25a570eae9374be586f. Written by hand; no scientific computation/enumeration,
script, assertion, solver, Lean, model CLI or nested agent. No novelty, priority, human-review or whole-target claim.
Every used ingredient of unreviewed RUH3/RUH2 is re-proved here [RE-DERIVED]; those candidates are not premises.

## 0. Statements and scope

FULL antecedent throughout: p>=11 prime, e=(p+1)/2, kappa=(p-1)/2; an avoider w of length 4p-2 over D_(2p) has SOME admissible
NF with terminal k=p+1 and kappa_hat=kappa, H=e-1 extra reflection pairs anywhere in the odd blocks; empty runs separate
DIFFERENT reflection values. An avoider means no identity product from 2p letters in increasing original index order.
No hypothesis on o_F, rotation pairs, nonempty runs or reflection rigidity. Let a!=0 be the common unsigned dominant class,
orient A>=A', and A=p-1+c, 3<=c<=p-1 (UH-A at literal scope). Put delta:=2p-2-A-A', b:=p-1-c, k0:=floor(e/2)+1. For a run i:
L_i is its rotation length, alpha_i and beta_i its counts of a and -a, d_i:=alpha_i-beta_i, delta_i its count outside {a,-a},
X_i its rotation exponent sum in Z_p, tau_i:=y_i-y_(i-1), H_i:=tau_i+X_i in Z_p. For a set P of runs, d(P):=sum_P d_i,
m(P) its number of maximal cyclic intervals, t(P):=sum_P tau_i/(2a); sign z_P is - on P, + elsewhere. All counts/inequalities
in d,g,L are in ordinary integers; sums in tau,X,H,t are in Z_p unless an integer lift is explicitly named.

THEOREM E0 [NEW]. Every putative avoider in this cell has NO empty run: L_i>=1 for all p+1 runs.
THEOREM BOTTLE [NEW]. Such an avoider necessarily has a proper nonempty set P with
  3<=m(P)<=k0,   g:=c-d(P) odd,   3<=g<=min(e-1,2m(P)-2).                         (ESC)
For EVERY set satisfying (ESC) (indeed every low critical pattern in Lemma C below):
  (i) all rotation letters outside {a,-a} have signed value 3a under z_P;
  (ii) 2T(z_P)=D_z, the total signed rotation sum, equivalently
       2 sum_(i in P) H_i = D0, where D0:=sum_i X_i;
  (iii) no run contains both 3a and -3a, every original -3a run lies in P and every original +3a run lies outside P.
In particular EVERY rotation lies in {a,-a,3a,-3a}; if a non-{a,-a} letter outside {3a,-3a} exists, or one run contains both
3a and -3a, there is no avoider with the full antecedent. These are restricted exclusions, not a bottom-cell closure.
The remaining precise parity/word regime and failed routes are in residual-BOTTOM-v1.md. No avoider is constructed.

## 1. SR, dominant class and the ordinary window [RE-DERIVED]

Write (v,eps)(v',eps')=(v+eps v',eps eps'), rho_x=(x,+1), sigma_y=(y,-1). Accepted NF (interface Sec. 9) yields a cyclic word
R_0 S_0 ... R_p S_p, N=p+1=2e runs, block S_i between R_i and R_(i+1), all S_i constant and odd, sum_i (|S_i|-1)/2=e-1.
Thus F=p+2e-1=2p reflections and R=3p-1-2e=2p-2 rotations; tau_i!=0 for an empty R_i. Cyclic cuts conjugate products.
GRX (if direction) gives, for sign pattern z_P with 2m changes, every even C in [2m,2m+2e-2] reflections. Consequently
  (SR) j in [m,m+e-1] intersect [1,p], n=2p-2j: no actual n-letter signed rotation sum can equal T(z_P)=sum_P tau_i.
For every proper nonempty P, 1<=m<=e, so j=e (n=p-1) is always admissible. For all-plus, m=0, T=0, j=1,...,e-1.

Pairing lemma. A multiset of size N' and maximal multiplicity mu has q disjoint unequal pairs when 2q<=N' and q<=N'-mu.
Proof: sum_x min(q,v_x)>=2q (if some v_x>=q, the other terms cap to at least q; otherwise the sum is N'); take 2q capped
occurrences in value order and pair the r-th with the (r+q)-th. Each constant segment has length <=q. []
Lemma P. Every nonconstant sign pattern has a value of multiplicity >=p. Otherwise the pairing lemma gives p-1 unequal pairs
in its 2p-2 signed values. Choose one letter of every pair; RS(b) with integer K=p-1 on the p-1 nonzero swap differences
attains every residue in sums of p-1 letters, contradicting SR at j=e. []
Lemma U. All such dominant values lie in ONE original unsigned class {a,-a}: each class that can dominate has total size >=p,
and two disjoint classes would need >=2p>R. If a=0, two of the p+1 block values y_i coincide; the intervening proper arc has
m=1, T=0, and p-1 zero rotations attain its target at j=e. So a!=0. Orient A=v_a>=A'=v_(-a). All-plus gives A'<=kappa (j=e-1,
n=p+1: choose (p+1)/2 of a and of -a). Accepted UH-A, at this full antecedent, gives A>=p+2 and A<=2p-1; R=2p-2 in fact gives
A<=2p-2. Thus 3<=c<=p-1 and A'=p-1-c-delta>=0, b=A'+delta=p-1-c.
Under z_P the multiplicities of a and -a are A-d(P) and A'+d(P). Hence for every proper nonempty P:
  (W) d(P)<=c-1 ("low") OR d(P)>=p-A'=c+1+delta=:Lambda ("high").
Their gap is 2+delta; d(all)=A-A'=2c+delta, so complementation swaps low and high and preserves m.

## 2. Omission windows, central parity and the equality case [RE-DERIVED + NEW rigidity]

MW. Let s!=0 be a signed value with multiplicity phi and W_s the w0=R-phi other letters, with differences omega_u=s_u-s!=0.
For an admissible j put K_j=R-(2p-2j)=2j-2. Count q indices with w0<=K_j<=phi. For each such j and each subset J of W_s,
omit J plus K_j-|J| letters of value s; every choice is valid and the selected sum is D_z-K_j s-sum_J omega. The q values K_j s
are distinct, RS(b) with K=w0 gives at least min(p,w0+1) subset sums, and CD gives at least min(p,w0+q) attained residues.
Avoidance therefore requires q>=1 => w0+q<=p-1. []
For a low P put g:=c-d(P)>=1. Take s=a, phi=A-d=p-1+g, w0=p-1-g. The counted indices are precisely
  [m,m+e-1] intersect [1,p] intersect [e-g/2,e+g/2].                              (CW)
If g=2r is even and r+1<=m<=e-r, the whole integer window [e-r,e+r] counts: q=g+1 and w0+q=p, impossible.
If g=2r+1<=e-1 is odd and r+1<=m<=e-r, the whole window [e-r,e+r] counts: q=g and w0+q=p-1. Call this a LOW CRITICAL pattern.
For 1<=m<=k0 a violation of d(P)<=c-min(e,2m-1) entails g<=min(e-1,2m-2); the even case is impossible by (CW), so it is
an odd critical pattern (r<=m-2; m+r<=e as m<=k0 and g<=e-1). Call such a violation an escape, allowing g=1 for now.

Lemma C (critical row rigidity) [NEW]. Every low critical pattern has (i) all signed values in {a,-a,3a}, and (ii) 2T=D_z.
Proof. For g>=3 let I be the q=g values K_j a (a consecutive progression of step 2a), and G_s=sum_{u in W_s}{0,omega_u}.
Avoidance says |I+G_s|<=p-1; g+w0=p-1. Put any one difference omega first. If |I+{0,omega}|>=g+2, each of the remaining
w0-1 additions grows by at least one until p (CD), giving p attained residues. Therefore |I union (I+omega)|=g+1. For an
interval of q residues of step 1, its growth under a translate v in {1,...,p-1} is min(q,p-q,v,p-v) (split the shifted interval
at p and count the overlap). Here 2<=g<=e-1<=p-2, so growth one forces omega/(2a)=+1 or -1. Thus every minority signed value
is -a or 3a.
For g=1, w0=p-2 and q=1. If two differences u,v were not equal up to sign, {0,u,v,u+v} has four elements; the remaining
w0-2 additions would give at least 4+(w0-2)=p residues. So every difference is +/-u for one u. The number of signed -a
letters is beta=A'+d=p-2-delta>=c-1>=2 (delta<=b=p-1-c), so one difference is -2a and u=+/-2a. Again the only signed values
are a,-a,3a.
Write beta for the signed -a count; all delta other letters are signed 3a, so beta=p-1-g-delta and
D_z=2a(p-1-beta+delta). After division by 2a, the attained residues from the counted lengths are the integer interval
  [p-(e+r)-beta, p-(e-r)+delta],
whose length is w0+q=p-1. Its unique missing residue is p-(e+r)-beta-1. If t=T/(2a) is that residue, then
2t=g+2delta (mod p), while D_z/(2a)=p-1-beta+delta=g+2delta. Thus T=D_z/2. Finally D_z=D0-2sum_P X_i and T=sum_P tau_i,
so 2sum_P H_i=D0. This proves Lemma C. []

Local transport [NEW]. If toggling one run i takes one low critical pattern to another, then delta_i=0 and H_i=0: both
patterns must give every non-{a,-a} letter the signed value 3a, impossible if any such letter is flipped; subtract 2T=D_z
between the patterns to obtain 2(tau_i+X_i)=0. In particular an empty run (tau_i!=0, X_i=0) can never be so toggled.

## 3. What an empty run forces at an escape [NEW]

Let an escape have g=2r+1, 1<=g<=min(e-1,2m-2), 1<=m<=k0. Thus r<=m-2 and m-1>=r+1. Toggling an empty run changes m by at
most one and leaves g unchanged. If m+r<=e-1, the new m lies in [r+1,e-r], so both patterns are low critical, contrary to
local transport. For e odd, m+r<=e-1 always: writing e=2h+1, m<=h+1 and r<=h-1. For e even (e=2h), equality m+r=e is possible
only at m=h+1=k0, r=h-1, g=e-1. In this case local transport forbids a toggle with m'=m or m-1, hence every empty run must
have m'=m+1 when toggled, which means its own sign and both neighbours' signs are ALL THE SAME.
Consequently, if E>0, every low set with 1<=m<=k0 satisfies
  d(P)<=c-min(ell,2m-1),  ell:=e for e odd, ell:=e-1 for e even.                 (LB)
For e even, the sole possible violation of the original cap-e bound is m=k0, g=e-1, with flat signs at every empty run.

## 4. Anchoring and missing sets [RE-DERIVED at the bottom cell]

Anchor lemma. Suppose all low sets with m<=k0 obey (LB), with ell=e or e-1. At m=k0, 2k0-1>=e, so low sets have d<=c-ell
and high sets, by complementation, have d>=Lambda+ell-1; gap 2ell+delta. There IS a single-run-toggle path at m=k0 (not m=e):
N=2e>=2k0+2; from {0,2,...,2k0-2}, add N-1,...,2k0; remove 0; for j=1,...,k0-1 add 2j-1 then remove 2j; add 2k0-1. At every
step m=k0 (one interval grows/shrinks; the gaps 0,1 and 2k0-1 keep the neighbouring intervals apart until the relevant step),
and the endpoints are complements. Orient low to high. A removal crossing the gap would need beta_i-alpha_i>=2ell+delta,
impossible as A'<=e-1<2ell; thus an added run h has d_h>=2ell+delta>=p-1+delta. If a high set P avoids h, A>=alpha_h+alpha(P)
>=2ell+delta+Lambda>A (difference 2ell-2e+3+2delta>=1+2delta). So every nonempty set avoiding h is low.
Let Q be the nonempty runs other than h made entirely of a; X the runs other than h holding a letter !=a, |X|<=b. The p runs
other than h partition into Q, X and empty runs; hence
  E+|Q|>=p-b=c+1; |Q|<=d(Q)<=c-1 when Q is nonempty; therefore E>=2.
For P contained in (empty runs) union Q, d(P)>=|P intersect Q|. []

Missing sets. Let B be the b rotations !=a; omega_u=(x_u-a)/(2a)!=0 and G their subset sums, including 0; M=Z_p minus G.
RS(b), K=b, gives |M|<=p-1-b=c, and 0 is not in M. If Y consists of empty runs, no rotation value is changed by z_Y. For
j admissible and n=2p-2j, picking a subset J of B and n-|J| letters a attains T(z_Y) iff
  t(Y)+j=sum_J omega, with max(0,n-A)<=|J|<=min(n,b).
Thus if b<=n<=A ("free": j>=e-c/2 and j<=(p+1+c)/2=e+c/2), t(Y)+j lies in M. If n=A+1 (c odd, j=e-(c+1)/2), then t(Y)+j is
in M or is 0 (all nonempty subset sums are excluded). This is also the literal scope of accepted UH-E; here re-derived. []

Lemma ME [RE-DERIVED with restricted interval counts]. If e<=c<=p-1=2e-2, then
  E<=ceil(c/2)-1<=e-2,   E+C_E<=e+eps-1,                                       (ME)
where C_E is the number of empty clusters and eps=c-2floor(c/2). E=0 is trivial, so assume E>0. Put mu=floor(c/2),
M0=ceil((e+1)/2), h0=e-mu<=M0. For every nonempty Y of empty runs with m=m(Y)<=M0, all j in
J(Y)=[max(m,h0),m+e-1] are admissible and free: 1<=j<=M0+e-1<=3e/2<=(p+1+c)/2, j>=e-mu>=e-c/2.
The all-plus free lengths [e-mu,e-1], plus j=e-mu-1>=1 when eps=1 (the A+1 rule and j!=0), give
B0=[e-mu-eps,e-1] contained in M. Let [L,U] be the maximal integer interval containing B0 whose residues lie in M.
As 0 is not in M, 1<=L<=e-mu-eps, e-1<=U<=p-1, U-L+1<=c; residues L-1,U+1 are outside M. Every
F(Y)=t(Y)+J(Y) (at least mu+1 cyclically consecutive residues in M) meets [L,U], since disjointness would give at least
(mu+eps)+(mu+1)=c+1 residues in M, and therefore lies in its residues (cannot cross a missing boundary). There is a unique
integer theta(Y) congruent to t(Y) with theta(Y)+J(Y) inside [L,U], so
  L-max(m,h0)<=theta(Y)<=U-m-e+1.                                             (K)
For disjoint nonempty Y1,Y2 with m1,m2,m(Y1 union Y2)<=M0, the lift defect D=theta(Y1)+theta(Y2)-theta(Y1 union Y2) is a
multiple of p. Put m=m(Y1 union Y2)<=m1+m2. From (K), U<=L+c-1 and L<=e-mu-eps,
  D<=2c-mu-eps-e-m1-m2+max(m,h0)<=max(3mu+eps-e,c-2)<=2e-2<p;
  D>=2L-U-2M0+m+e-1>=L-c-1>=-c>-p.
So D=0, and adding runs interval by interval (prefixes have <=m(Y) intervals) gives theta(Y)=sum_Y theta_i for m(Y)<=M0,
where theta_i=theta({i})!=0. Let Y+ and Y- be the empty runs with positive and negative theta_i.
If m(Y+)>=k6:=floor(mu/2)+1, the union of k6 of its intervals has theta>=k6 but theta<=U-k6-e+1<=mu-k6, impossible.
Hence m(Y+)<=floor(mu/2), and |Y+|+m(Y+)<=U-e+1 (when nonempty). If m(Y-)>=h0, a union of h0 of its intervals has
theta<=-h0 but theta>=L-h0>=1-h0: impossible. Hence m(Y-)<=h0-1 and |Y-|<=h0-L. All these uses have m<=M0.
If U>=e, E<=(U-e)+(e-mu-L)<=mu+eps-1; if U=e-1, Y+ is empty and E<=e-mu-L<=e-mu-1<=mu+eps-1 (c>=e). Every empty cluster
contains an interval of Y+ or Y-, so C_E<=m(Y+)+m(Y-). If both signs occur,
E+C_E<=(U-e+1)+(e-mu-L)+(e-mu-1)=U-L+e-2mu<=e+eps-1;
if only negative signs occur, E+C_E<=2e-2mu-2<=e+eps-2; if only positive, E+C_E<=U-e+1<=mu<=e-1. This proves (ME). []

## 5. Proof of Theorem E0 [NEW]

Assume E>0. By Sec. 3, (LB) holds with ell=e (e odd) or ell=e-1 (e even). The anchor lemma gives h, all its avoiding sets
low, and E+|Q|>=c+1, E>=2. Thus (LB) applies to every nonempty P avoiding h with m(P)<=k0.

Case A: c<=ell-1. Put S=(empty runs) union Q. Every P inside S has d(P)>=|P intersect Q|>=0. No such P has
m(P)=floor((c+1)/2)+1<=k0: (LB) would give d(P)<=c-min(ell,2m-1)<0. In particular its independence number is at most
floor((c+1)/2). As S misses h it is a disjoint union of paths of lengths l_j, with sum |S|>=c+1 and independence number
sum ceil(l_j/2)>=|S|/2>=(c+1)/2. Therefore c is odd, |S|=c+1, all l_j are even. Every run of an even path belongs to an
alternating maximum independent set; such a set has m=(c+1)/2 and (LB) gives d<=c-min(ell,c)=0. So Q is empty and E=c+1.
For any nonempty subset Y of these runs, m(Y)<=c+1<=ell<=e, and j=e is admissible and free (n=p-1, b<=p-1<=A). Thus
t(Y)+e is in M. RS(b) on the c+1 nonzero values tau_i/(2a), with integer K=c+1, gives at least c+2 distinct subset sums
(c+2<=e+1<=p), at least c+1 from nonempty subsets. Hence |M|>=c+1>c: contradiction.

Case B: e even and c=e-1=ell. Suppose S has an independent set P of k0=e/2+1 runs. It has m=k0 and (LB) gives d(P)<=0, so
all its runs are empty. It is an escape with g=c=e-1; Sec. 3 says every empty run has the same sign as BOTH neighbours. But
an empty run selected in this independent set has both neighbours outside P: contradiction. Thus the independence number
of S is <=e/2. Since |S|>=e it equals e/2, |S|=e, and all components are even paths. As in Case A, each run lies in a maximum
independent set, now with m=e/2 and (LB) gives d<=c-(e-1)=0. So Q is empty and E=e. The last RS(b) argument of Case A, with
e nonzero values, K=e, j=e for all nonempty subsets, gives |M|>=e>c=e-1: contradiction.

Case C: c>=e. By (ME), E<=ceil(c/2)-1<=e-2, E+C_E<=e+eps-1 and 3E<2(c+1). Q is nonempty (|Q|>=c+1-E).
Remove h from the cycle to form a path; for sets avoiding h, m is the path interval count. A cluster is a maximal set of
consecutive empty runs. An S-block is a maximal set of consecutive runs of S=(empty runs) union Q, and a Q-block a maximal
set of consecutive Q-runs. A cluster is FF if it is an entire S-block, "end" if exactly one neighbour is in Q, and "inner"
if both neighbours are in Q. Let r_Q be the number of S-blocks containing Q and n_in the number of inner clusters. Then
m(Q)=r_Q+n_in and there are at most 2r_Q end clusters.
In each cluster take alternating AVAILABLE runs, where available means not adjacent to Q: all l runs in an FF cluster,
the l-1 runs away from Q in an end cluster, the middle l-2 in an inner cluster. Choose the 1st,3rd,5th,... available runs;
call their union I. Counts: ceil(l/2), floor(l/2), floor((l-1)/2), respectively. Each run of I is isolated from I and Q.
P=Q union I therefore has
  2m(P)-1 = E-1+(2r_Q-o_end)+o_FF+o_in >= E-1,                                 (POS)
where o_X counts the odd-length clusters of type X (o_end<=2r_Q).
 (alpha) m(Q)>=k0. The union P1 of the k0 largest Q-blocks has m=k0 and (LB) gives
 k0<=|P1 intersect Q|<=d(P1)<=c-ell<=c-e+1<=e-1<2k0.
 So the k0-th largest block and every block outside P1 are single runs, |Q|<=c-ell+m(Q)-k0. Consecutive Q-blocks are
 separated by non-Q segments containing a whole empty cluster or a run of X, distinct segments distinct ones. Thus
 m(Q)-1<=C_E+|X|<=(e+eps-1-E)+(p-1-c).
 Combining with |Q|>=c+1-E and ell>=e-1 gives c+k0<=p-1+eps. But k0<=c-ell gives
 c+k0>=ell+2k0>=2e=p+1>p-1+eps: contradiction.
 (beta) m(Q)<k0<m(P). Delete runs of I until m=k0. The resulting P1 contains Q, and (LB) gives
 |Q|<=d(P1)<=c-ell<=c-e+1, against |Q|>=c+1-E>=c+3-e.
 (gamma) m(P)<=k0. If 2m(P)-1>=E, then (LB) and ell>=e-1>E give |Q|<=c-E<|Q|. Otherwise (POS) is equality:
 2m(P)-1=E-1, o_end=2r_Q and o_FF=o_in=0. Every Q-containing S-block starts and ends with an odd cluster; each inner
 cluster has even length >=2. Also (LB) gives |Q|<=c-E+1, hence |Q|=c+1-E. If a Q-block has at least two runs, let x be its
 first run and y the empty run immediately before it. In the alternating construction y is not in I and neither is the
 run before y: for an odd end cluster its preceding index l-1 is even (or lies outside S if l=1); for an even inner cluster
 l-1 is odd while I uses even indices. Replace x by y. The Q-block retains a run, and y becomes a new singleton interval:
 m(P')=m(P)+1, |P' intersect Q|=|Q|-1, and 2m(P')-1=E+1<=e-1<=ell, m(P')<=e/2<=k0. Thus (LB) gives
 |Q|-1<=c-E-1, contradicting |Q|=c+1-E. If instead all Q-blocks are single runs, |Q|=r_Q+n_in but the two odd end clusters
 per Q-containing S-block and the even inner clusters give E>=2r_Q+2n_in=2|Q|, hence 3E>=2(c+1), again impossible.
All possible c are in A, B or C. Therefore E=0. []

## 6. Proof of Theorem BOTTLE [NEW]

If no escape with 1<=m<=k0 and g>=1 exists, Sec. 2 gives the low-set bound (LB) with ell=e (even g is already excluded).
The anchor lemma then gives E>=2, contrary to Theorem E0. So an escape exists.
We exclude g=1. With E=0 all N=p+1 runs have positive lengths and R=2p-2=2N-4. If s1 counts the singleton rotation runs,
  s1 = 4 + sum_(L_i>=3)(L_i-2) >= 4.                                         (LEN)
For a g=1 escape, 2<=m<=k0 and Lemma C says every signed letter is a,-a or 3a. Consider a singleton rotation run:
 - Signed a: flipping its run changes g to 0, i.e. d to c, forbidden by (W).
 - Signed 3a: its d_i=0, so flipping keeps g=1; the new m is between m-1 and m+1, hence in [1,k0+1] subset [1,e]. Every such
   pattern is low critical for g=1, but its flipped letter is -3a, contradicting Lemma C (p>=11).
 - Signed -a: flipping changes g to 2. If the new m is in [2,e-1], the even case of (CW) is impossible. Since
   m'<=k0+1<=e-1 (e>=6), it must be m'=1, hence m=2 and the singleton is an isolated vertex of P or of its complement.
Thus all singleton rotation runs are isolated sign vertices in a two-interval pattern. It has four maximal sign intervals;
as N>=12>4 at least one has more than one vertex, so at most three are singleton intervals. This contradicts (LEN).
Hence every escape has g>=3 (and m>=3), proving (ESC). Lemma C gives (i),(ii). For (iii), each non-{a,-a} letter must be
originally 3a outside P or -3a inside P, so a run cannot hold both. This proves Theorem BOTTLE. []

## 7. Exact parity/run constraints supplied by the proof [NEW; necessary only]

For a putative remaining avoider:
- All L_i>=1, and (LEN) holds; in particular at least four runs are singleton rotations.
- All rotation exponents lie in {a,-a,3a,-3a}, and every run contains at most one of the signs 3a,-3a.
- At least one (indeed every escape) satisfies (ESC), signed other letters 3a and 2sum_P H_i=D0. Its integer parity is
  d(P) congruent c-1 (mod 2), with 3<=g odd<=min(e-1,2m-2), 3<=m<=floor(e/2)+1.
- More generally for EVERY low critical pattern (g=2r+1<=e-1, r+1<=m<=e-r), Lemma C and local transport hold.
  This is an explicit local test: put w_i=z_i d_i (z_i=-1 on P), so toggling i gives g'=g-w_i and m'=m+Delta_i,
  Delta_i in {-1,0,1}. If g'>=2 is even and g'/2+1<=m'<=e-g'/2, no such pattern is possible by MW. If g' is odd in [1,e-1]
  and (g'+1)/2<=m'<=e-(g'-1)/2, then delta_i=0 and H_i=0. These are necessary transition constraints, not a finite search
  or a construction. A flip can leave these windows, and no assertion about those flips is supplied.
No sufficiency is asserted for any numerical/run profile in this list; the original word and all SR targets must still be
realised. In particular a restricted multiset statement does not replace the full NF antecedent.

## 8. What remains open

Theorem E0 is a uniform run-regime exclusion, NOT exclusion of the whole cell. Theorem BOTTLE reduces the exact remaining
cell to the empty-free, four-value, odd-gap regime of Sec. 7. The obstruction is mathematical: critical omission windows can
attain exactly p-1 residues, and their one omitted residue is precisely the target D_z/2. Another low critical pattern need
not be reachable by a particular flip (m or g can leave the displayed window), so local transport does not force all H_i=0.
No contradiction or counterexample for this regime is claimed. See residual-BOTTOM-v1.md for the failed branches.

## 9. Scope and interface table

[RE-DERIVED]: SR, pairing, P/U, W, MW, the positive-selection/missing-set rule, the restricted-interval lift proof, the anchor
and independent-set/position counting arguments. [NEW]: critical row rigidity and half-total target, local transport,
Theorem E0, the necessary escape and exclusion of g=1. RUH3/RUH2/KP3/KP4/R7 are not cited as premises. UH-L (delta=0 only),
UH-SH/MW/PH, PP1/KP2, CT, Lev, S(p), RPdelta, ASSEMBLY-P, REFL, RUNS and LS-family are not used.
Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, inclusive LF lines, whole-file SHA256 | Scope/use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | Some admissible NF; lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3 |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | If direction; SR for every admissible j |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | Accepted CFXT item 4; integer K=p-1,w0,b,c+1,e |
| CD | classical; proof-ROW-v1.md 4-5 | Interval/subset sum growth and MW translates |
| UH-A | R18/olson-UH-CONSTRAINTS-parent-verdict-v1.md 9,15; 7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3; errata v1 8f1ea491eb2ab8ab4d4f1006896cb9aad63d6c51e270acb190de7bdaf4074ee3, v2 ac2a7f26ef941366e70e939545bae07a5baea6564005af29e5c9185560aaaa50, v3 0dc678867d10f28abc2f1681b21805658318fa9fc3a4c379062152cc1aef813f | Full existential NF antecedent; 3<=c and multiplicity bounds; no empty-run hypothesis added |
| UH-E | Same verdict line 20 with errata | Re-proved in Sec. 4; full subset sums only when b<=n<=A |
Verdict hashes: R16/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
