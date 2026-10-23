# RUH3: R-UH on the whole SH range 3e<=p+2 (uniform; closes residual R2 of RUH2), v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:58:14-0700. Status: CANDIDATE_UNVERIFIED written proofs. Frozen scope:
RUH3-scope-v1.md (SHA256 c6601f27ab4b1752b7d76ae769c1c1229160367b20b8da0ba4ab60a138815bbb, frozen 2026-10-19T17:30:02-0700 before
derivation; pre-freeze exposure disclosed there). Authority: RUN/control/written-slot-transition-olson-20261019-1730-v1.json
(SHA256 b95a3c222c5d95faf838ce9db98e6e94050196bc6b6f6366339922f311755455), key math2. All case work by hand; no script,
assertion, enumeration, solver, Lean or computation over scientific data. Inputs: accepted NF, GRX (if direction), RS(b),
classical Cauchy-Davenport (CD), and accepted UH-A at literal scope (only for Corollary SH). NOT imported: RUH2 (a candidate;
everything used from it is re-proved here and labelled [RE-DERIVED]; its Theorem B and its errata are not used), KP3, KP4, R7,
UH-SH, UH-MW, UH-L, UH-PH. [NEW] marks new arguments. No novelty, priority, Lean or human-review claim.

## 0. Statements

Throughout: p prime, e:=p-kappa, and the FULL antecedent: an avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing
original index order with identity product) has SOME admissible NF with terminal k=p+1 and kappa^=kappa; H^=e-1 extra
reflection pairs anywhere in the odd blocks; every empty NF run separates different reflection values. No hypothesis on o_F,
reflection runs, nonempty runs or rotation pairs; no multiset-only statement outside this antecedent. a, A, A', c, b, delta are
as in Sec. 2 (A=2kappa+c). "SH range": p>=13 and 5<=e<=(p+2)/3, i.e. 3e<=p+2.
LEMMA L [RE-DERIVED]. In the SH range there is a run h such that every nonempty set P of runs avoiding h with 1<=m(P)<=e
satisfies d(P) <= c - min(e, 2m(P)-1).
LEMMA E [NEW]. In the SH range with e<=c<=2e-1, the number E of empty runs satisfies E <= ceil(c/2)-1.
LEMMA POS [NEW]. In the SH range with 3<=c<=2e-1 (h, Q, E as in Sec. 3), if E<=e-1 and 3E<2(c+1), then some nonempty set P
avoiding h with 1<=m(P)<=e has |P n Q| > c-min(e,2m(P)-1), contradicting Lemma L (d(P)>=|P n Q|).
THEOREM R2 [NEW, uniform]. In the SH range no avoider with the full antecedent has e<=c<=2e-1. (This closes residual R2 of
RUH2, i.e. 6<=e, p>=17, and also covers e=5 uniformly.)
THEOREM A [RE-DERIVED]. In the SH range no avoider with the full antecedent has 3<=c<=e-1.
COROLLARY SH. With accepted UH-A: for every prime p>=13 and every e with 5<=e<=(p+2)/3, no avoider of length 4p-2 has an
admissible NF with terminal k=p+1 and kappa^=p-e.
NOT PROVED here: R-UH when 3e>p+2 (residual R1); see the companion residual note of this round.

## 1. Word form, selection rule, notation [RE-DERIVED]

Group law (v,eps)(v',eps')=(v+eps v',eps eps'), rho_x=(x,+1), sigma_y=(y,-1), x,y in Z_p. By NF (proof-ROT-few-E-v4.md 28-43,
overlays in Sec. 9) an admissible NF u is an avoider of length 4p-2 with the same rotation multiset, written cyclically
R_0 S_0 ... R_p S_p (N:=p+1 runs, block S_i between R_i and R_(i+1)), all blocks odd, sum (l_i-1)/2=e-1, F=p+2e-1,
R=3p-1-2e rotation letters, empty runs allowed, every empty R_i with y_(i-1)!=y_i. We exclude such u (word form).
GRX (notes-GRX-v1.md 7-20, if direction): all l_i odd give delta_GRX=N-Phi, C_max=Phi+2(e-1); every even C in [Phi,Phi+2e-2]
with 0<=2p-C<=R is admissible. Writing Phi=2m and n=2p-C=2p-2j:
  (SR) admissible j are j in [m, m+e-1] with 0<=2p-2j<=R;
a sign pattern z avoids only if, for every admissible j, no n=2p-2j rotation letters have signed sum equal to its target T(z).
For a set P of runs, z_P:=-1 on P (+1 elsewhere); m(P):=number of maximal cyclic intervals of P (m(empty set)=0, all-plus
pattern); T(z_P)=sum_(i in P) tau_i, tau_i:=y_i-y_(i-1), tau_i!=0 for empty R_i. Cyclic cuts conjugate products, so order
and identity are preserved. In the SH range 2e<=p-3, so every j in [m,m+e-1] with 0<=m<=e has 0<=2p-2j<=R.

## 2. Pairing, dominant class, window [RE-DERIVED]

Lemma M. A multiset of size N' and maximal multiplicity mu' has q disjoint unequal pairs if 2q<=N' and q<=N'-mu' (cap
multiplicities at q, pair x_i with x_(i+q) in a value-sorted list of 2q capped occurrences).
Lemma P. Every non-constant z has a signed value of multiplicity >=2kappa+1. Proof: n:=max(p-1,2kappa+2-2m) is admissible
and p-1<=n<=2kappa (m>=1). If all multiplicities were <=2kappa=R-(p-1), Lemma M gives p-1 unequal pairs (2(p-1)<=R as
e<=(p+1)/2); the R-2(p-1)=2kappa-p+1 unpaired letters contain n-p+1 fillers; choosing one letter of each pair plus the
fillers, RS(b) with K=p-1 on the nonzero swap differences attains every residue, in particular T(z). []
Lemma U. All non-constant z have their dominant value in one class {a,-a}, a!=0. Proof: two classes of total multiplicity
>=2kappa+1 each would need R>=4kappa+2, but 2(2kappa+1)-R=p-2e+3>0. If the class were {0}: two of the p+1 block values
coincide, y_i=y_k; the proper arc P of runs strictly after S_i up to R_k has m=1 and T(z_P)=y_k-y_i=0; j=e (n=2kappa) is
admissible, and 2kappa letters 0 attain T. []
Orient A:=v_a>=A':=v_(-a); delta:=R-A-A'. d(P):=alpha(P)-beta(P) (letters a minus letters -a in the runs of P), additive.
All-plus (m=0, T=0): A'<=kappa (n=2kappa+2, j=e-1: kappa+1 letters each of a,-a), and in the SH range A<=2p-1 (n=2p, j=0,
admissible as R-2p=p-1-2e>=2). Write A=2kappa+c (so c<=2e-1), b:=R-A=p-1-c, lambda:=c-1, Lambda:=2kappa+1-A'. Under z_P the
signed value a has multiplicity A-d(P) and -a has A'+d(P); Lemmas P/U give for every proper nonempty P:
  (W) d(P)<=lambda or d(P)>=Lambda; Lambda-lambda=p-2e+3+delta>0.

## 3. Omission windows and the super-heavy run [RE-DERIVED]

Lemma MW. Let z be non-constant with Phi=2m, s a nonzero signed value of multiplicity phi, W the w0=R-phi other letters,
omega_u:=s_u-s!=0 (signed values), G_s their subset sums. For admissible j put K_j:=R-(2p-2j)=p-1-2e+2j; let q be the number
of admissible j with w0<=K_j<=phi. If q>=1 then w0+q<=p-1.
Proof. For such j and any J in W, omit J and K_j-|J| letters of value s (0<=K_j-|J|<=phi); the 2p-2j selected letters have
sum D-K_j s-sum_J omega (D the total signed sum). The q values K_j s are distinct (the j's differ by <e<p, s!=0); RS(b) gives
|G_s|>=min(p,w0+1) and CD gives >=min(p,w0+q) attained residues. If w0+q>=p, T(z) is attained. []
(MWe) m=e in the SH range: every P with m(P)=e has a dominant multiplicity >=p+kappa.
Proof. The K_j (j in [e,2e-1]) are p-1,p+1,...,p+2e-3, all >=w0 (w0<=R-2kappa-1=p-2 by Lemma P). Write phi=p-1+2r+eps (eps in
{0,1}, r>=0; phi>=2kappa+1>=p). If r<=e-2, q=r+1 and w0=2p-2e-2r-eps, so MW needs r>=p-2e+2-eps, whence e-2>=p-2e+2-eps and
3e>=p+4-eps>=p+3: impossible. So r>=e-1, q=e, w0<=p-1-e=kappa-1, phi>=R-kappa+1=p+kappa. []
Hence for m(P)=e: d(P)<=c-e or d(P)>=p+kappa-A', a split with gap p+1+delta; complements swap the two types
(d(P^c)=A-A'-d(P), m(P^c)=m(P)).
Path. With runs 0..N-1 (N=p+1>=3e-1>=2e+2), single-run toggles keep m=e from P0={0,2,...,2e-2} to its complement: add N-1,
N-2,...,2e (extending the interval of 0); remove 0; for i=1..e-1 add 2i-1 and remove 2i; add 2e-1. (The block [2e,N-1] stays
nonempty; 2e-1 separates 2e-2 from 2e until the last step; 0 and 1 separate N-1 from 2.)
Super-heavy run. Orient the path from its low end to its high end; some step goes from the low to the high type across the gap
p+1+delta. Removing a run would need beta_i-alpha_i>=p+1+delta>kappa>=A'. So a run h is added with d_h>=p+1+delta
(alpha_h>=d_h).
Light sets. If a nonempty P' avoiding h were high in (W), alpha(P')>=Lambda and A>=alpha_h+alpha(P')>=3p-2e+2+delta-A', while
A=3p-1-2e-delta-A': impossible (0>=3+2delta). So every nonempty set avoiding h has d<=c-1.
Counts. E:=number of empty runs (all differ from h); Q:=set of nonempty runs other than h holding only letters a; at most b
runs other than h hold a letter !=a. So E+|Q|>=p-b=c+1, and |Q|<=d(Q)<=c-1 when Q is nonempty; hence E>=2. Every set P of
runs inside E u Q has d(P)>=|P n Q| (a run of Q has d>=1, an empty run d=0).

## 4. Lemma L [RE-DERIVED]

Let P be nonempty, h not in P, 1<=m:=m(P)<=e, d:=d(P), g:=c-d>=1 (light sets). Under z_P the signed value a has multiplicity
phi=A-d, w0=R-phi=b+d=p-1-g. For admissible j: K_j>=w0 iff j>=e-g/2; K_j<=phi iff j<=(p+1+g)/2. Suppose g<=e-1 and g<=2m-2;
we show q>=g+1, contradicting MW (q>=g+1>=1 forces w0+q<=p-1, i.e. q<=g). Note (p+1+g)/2>=(3e-1+g)/2 as p>=3e-2.
 Case A, m>=e-floor(g/2): j runs over [m, min(m+e-1, floor((3e-1+g)/2))] at least; since m<=e this has >=min(e,
 floor((e+1+g)/2)) elements, and floor((e+1+g)/2)>=g+1 because g<=e-1.
 Case B, m<e-floor(g/2): j runs over [e-floor(g/2), min(m+e-1, floor((3e-1+g)/2))]. If the minimum is m+e-1 the count is
 m+floor(g/2)>=g+1 because g<=2m-2; otherwise it is floor((e-1+g)/2)+floor(g/2)+1>=g+1 because floor((e-1+g)/2)>=g.
Hence g>=min(e,2m-1), i.e. d(P)<=c-min(e,2m(P)-1). (Selected runs may be empty; nothing is claimed for m>e.) []

## 5. Positive selections and the missing set [RE-DERIVED; this is the content of accepted UH-E]

B: the b letters !=a; omega_u:=(x_u-a)/(2a)!=0; G: their subset sums (0 included); G_(>=r): sums over >=r elements;
M:=Z_p minus G; |M|<=p-1-b=c (RS(b), K=b) and 0 is not in M.
Lemma S. Let Y be a set of EMPTY runs (Y empty allowed; m=m(Y)), t(Y):=T(z_Y)/(2a). For an admissible j put n=2p-2j. If
t(Y)+j=sum_J omega for some J in B with max(0,n-A)<=|J|<=min(n,b), u has an identity 2p-subword. In particular, if n<=A and
n>=b (j>=e-c/2 and j<=(p+1+c)/2: "free"), then t(Y)+j is in M; if n=A+1 (j=e-(c+1)/2, c odd: "(N1)"), then t(Y)+j is not in
G_(>=1), so t(Y)+j is in M or t(Y)+j=0.
Proof. Every letter keeps its value (no letter lies in Y). J plus n-|J| letters a sum to 2a(n/2+sum_J omega)=2a(-j+sum_J
omega) (mod p); equality with T(z_Y)=2a t(Y) is the stated condition; SR. []
For an empty run i write t_i:=t({i})=tau_i/(2a)!=0; then t(Y)=sum_(i in Y) t_i (mod p).

## 6. Proof of Lemma E [NEW]

Let e<=c<=2e-1, mu:=floor(c/2), eps:=c-2mu, so ceil(c/2)=mu+eps. For a nonempty set Y of empty runs with m:=m(Y)<=e put
J(Y):=[max(m,e-mu), m+e-1]. Every j in J(Y) is admissible (m<=j<=m+e-1) and free (j>=e-mu>=e-c/2; j<=2e-1<=(p+1+c)/2 as
p>=3e-2 and c>=e), so Lemma S gives
  F(Y):=t(Y)+J(Y) is contained in M, a set of |J(Y)|=min(m+mu,e)>=mu+1 cyclically consecutive residues (mu<=e-1).

Case I: c<=2e-2. Then mu+eps<=e-1 (eps=1 forces c<=2e-3) and e<=c=2mu+eps.
(I.1) B0:=[e-mu-eps, e-1] lies in M: for the all-plus pattern (Y empty, m=0, t=0) the lengths j in [e-mu,e-1] are admissible
 and free, and for eps=1 the (N1) length j=e-mu-1 in [1,e-1] gives j in M (j is not 0 mod p).
(I.2) Let [L,R'] be the largest integer interval containing B0 all of whose integers have residues in M. As 0 is not in M:
 1<=L<=e-mu-eps and e-1<=R'<=p-1; the residues of [L,R'] are distinct, so R'-L+1<=|M|<=c; by maximality the residues of L-1
 and R'+1 are not in M. Write U for the residue set of [L,R'].
(I.3) Every F(Y) is contained in U: if F(Y) missed U then |M|>=|U|+|F(Y)|>=(mu+eps)+(mu+1)=c+1; so F(Y) meets U, and a
 cyclically consecutive subset of M that meets U and leaves it would contain the residue of L-1 or of R'+1.
(I.4) Hence there is a unique integer theta(Y) congruent to t(Y) mod p with theta(Y)+J(Y) contained in [L,R'] (start from the
 element of [L,R'] congruent to t(Y)+min J(Y); the following integers stay in [L,R'] because the residue of R'+1 is not in M;
 uniqueness as R'-L<p), and
  (K) L-max(m,e-mu) <= theta(Y) <= R'-m-e+1.
(I.5) Additivity. Let Y1, Y2 be disjoint and nonempty, with m1:=m(Y1), m2:=m(Y2) and m:=m(Y1 u Y2) all <=e, and put
 D:=theta(Y1)+theta(Y2)-theta(Y1 u Y2), a multiple of p. By (K), R'<=L+c-1 and L<=e-mu-eps:
  D <= 2R'-L-m1-m2-2e+2+max(m,e-mu) <= 2c-mu-eps-e-(m1+m2)+max(m,e-mu),
 which is <=3mu+eps-e<=2e-2 if the maximum is m (m<=m1+m2), and <=c-2 if it is e-mu (m1+m2>=2); and
  D >= 2L-R'-e+m-1 >= L-c-e+m >= 2-c-e >= 4-3e >= 2-p.
 So |D|<p and D=0. Adding the runs of Y one at a time, interval by interval, keeps every partial set at <=m(Y) intervals;
 hence theta(Y)=sum_(i in Y) theta_i with theta_i:=theta({i})!=0 (t_i!=0), for every nonempty Y with m(Y)<=e.
(I.6) Positive runs. Let Y+:={i: theta_i>0}, if nonempty. If m(Y+)>e, the union Y' of e intervals of Y+ has
 e<=theta(Y')<=R'-2e+1<=L+c-2e<=mu-e<0: impossible. So m(Y+)<=e and |Y+|<=theta(Y+)<=R'-e.
(I.7) Negative runs. Let Y-:={i: theta_i<0}, if nonempty. If m(Y-)>=e-mu, the union Y' of exactly e-mu intervals of Y- has
 -(e-mu)>=-|Y'|>=theta(Y')>=L-(e-mu)>=1-(e-mu): impossible. So m(Y-)<=e-mu-1 and |Y-|<=-theta(Y-)<=e-mu-L.
(I.8) E=|Y+|+|Y-|. If R'>=e: E<=(R'-e)+(e-mu-L)=R'-L-mu<=c-1-mu=mu+eps-1. If R'=e-1, Y+ is empty by (I.6) and
 E<=e-mu-L<=e-mu-1<=mu+eps-1 (e<=2mu+eps). So E<=ceil(c/2)-1.

Case II: c=2e-1 (mu=e-1, eps=1, ceil(c/2)-1=e-1). Here J(Y)=[m,m+e-1] and |J(Y)|=e.
(II.1) All-plus: every j in [1,e-1] is free (2j>=2e-c=1), so B0:=[1,e-1] lies in M. A single empty run i has F({i})=t_i+[1,e];
 as 0 is not in M, t_i is not in {-e,...,-1}, so t_i has a lift in [1,p-e-1].
(II.2) No t_i>=e. If t_i>=e, then [t_i+1,t_i+e] and [1,e-1] are disjoint subsets of [1,p-1] whose residues lie in M, with
 e+(e-1)=c>=|M| elements, so M is exactly their union. The residues 0, e, t_i and t_i+e+1 are not in M, so M consists of two
 maximal blocks of cyclically consecutive residues, of sizes e-1 and e, and every set of e cyclically consecutive residues
 inside M equals F({i}). Every other empty run k (E>=2) then has F({k})=F({i}), so t_k=t_i=:t. A pair Y of empty runs
 (m(Y) in {1,2}) gives F(Y)=2t+[m,m+e-1]=t+[1,e], so t=1-m in {0,-1} mod p, contradicting t in [e,p-e-1].
(II.3) So every t_i lies in [1,e-1] and M contains [1,t_i+e]. Let [1,R'] be the largest integer interval starting at 1 whose
 residues lie in M: e+1<=R'<=|M|<=2e-1<=p-1. Every F(Y) (Y nonempty, m(Y)<=e) has e residues and meets the residues of [1,R']
 (else |M|>=2e+1), hence lies in them as in (I.3). Lifts theta(Y) with theta(Y)+[m,m+e-1] inside [1,R'] satisfy
 1-m<=theta(Y)<=R'-m-e+1<=e-m; the defect of (I.5) satisfies D<=(e-m1)+(e-m2)-(1-m)<=2e-1<p and
 D>=(1-m1)+(1-m2)-(e-m)>=3-3e>=1-p, so D=0; and theta({i})=t_i. Hence sum_(i in Y) t_i<=e-m(Y), i.e. |Y|+m(Y)<=e, for every
 nonempty Y with m(Y)<=e. For Y = all empty runs, a union of e intervals would give |Y'|<=0; so m(Y)<=e and E<=e-1. []

## 7. Proof of Lemma POS [NEW]

Remove h from the cycle of runs: the other p runs form a path, and for P avoiding h, m(P) is the number of maximal intervals
of P on this path. Q is nonempty, since |Q|>=c+1-E and 3E<2(c+1). Call a maximal set of consecutive empty runs a cluster, a
maximal set of consecutive runs of (empty runs) u Q an S-block, and a maximal set of consecutive runs of Q a Q-block. A cluster
is of type FF if it is a whole S-block (no neighbour in Q), "end" if exactly one neighbour is in Q (it is the first or last
cluster of an S-block containing Q-runs), and "inner" if both neighbours are in Q. With r_Q the number of S-blocks containing
Q-runs and n_in the number of inner clusters, m(Q)=r_Q+n_in, and there are at most 2r_Q end clusters.
Choice of I. In a cluster c_1,...,c_l (path order) call a run available if neither neighbour is in Q: all runs (FF);
c_1..c_(l-1) for an end cluster whose Q-neighbour follows c_l (c_2..c_l in the mirror case); c_2..c_(l-1) (inner). I takes
the 1st, 3rd, 5th, ... available run of every cluster: ceil(l/2), floor(l/2), floor((l-1)/2) runs respectively. Runs of I are
pairwise non-adjacent and have no neighbour in Q.
P:=Q u I. Each Q-block is a maximal interval of P and each run of I is a singleton interval, so m(P)=r_Q+n_in+|I|; as
2ceil(l/2)=l+[l odd], 2floor(l/2)=l-[l odd] and 2floor((l-1)/2)+2=l+[l odd],
  2m(P)-1 = E-1+(2r_Q-o_end)+o_FF+o_in >= E-1,
where o_X is the number of clusters of type X and odd length (o_end<=2r_Q).
(i) m(P)>e. If m(Q)>=e, the union P1 of e Q-blocks has m(P1)=e and |P1 n Q|>=e>c-e (c<=2e-1). Otherwise delete runs of I
 from P until m=e: P1 contains Q, m(P1)=e and |Q|>=c+1-E>=c+2-e>c-e. Either way Lemma L (min(e,2e-1)=e) fails.
(ii) m(P)<=e and 2m(P)-1>=E: Lemma L gives |Q|<=d(P)<=c-min(e,E)=c-E<|Q| (E<=e-1).
(iii) Otherwise 2m(P)-1=E-1. Then o_end=2r_Q and o_FF=o_in=0: every S-block containing Q-runs begins and ends with a cluster
 of odd length, and every inner cluster has even length (>=2). Lemma L gives |Q|<=c-E+1, so |Q|=c+1-E. Every Q-block is
 immediately preceded by an empty run (the last run of an end or inner cluster).
 (iii-a) Some Q-block has >=2 runs: let x be its first run and y the empty run just before x. Then y is not in I, and the run
 before y is not in P: it lies outside (empty runs) u Q when y's cluster is an end cluster of length 1; otherwise it is
 c_(l-1) of y's cluster, which has an even index in an odd end cluster and an odd index in an even inner cluster, so it was
 not taken into I. P':=(P minus {x}) u {y} has m(P')=m(P)+1 (x's block keeps a run; y is a new singleton interval),
 2m(P')-1=E+1<=e and |P' n Q|=|Q|-1; Lemma L gives |Q|-1<=c-E-1: contradiction.
 (iii-b) Every Q-block is a single run: |Q|=m(Q)=r_Q+n_in, while E>=2r_Q+2n_in=2|Q| (two odd end clusters per S-block
 containing Q-runs; inner clusters of even length >=2). So c+1=|Q|+E<=3E/2, contrary to 3E<2(c+1). []

## 8. Proofs of Theorem R2, Theorem A and Corollary SH

Theorem R2 [NEW]. Let e<=c<=2e-1 in the SH range. Lemma E gives E<=ceil(c/2)-1, which is <=e-1 and <=(c-1)/2, so
3E<=3(c-1)/2<2(c+1). With the counts of Sec. 3 (E+|Q|>=c+1) and c>=e>=5, Lemma POS produces a set violating Lemma L. []
Theorem A [RE-DERIVED]. Let 3<=c<=e-1 (SH range); h, Q, E as in Sec. 3; S:=(empty runs) u Q. Every P inside S has
d(P)>=|P n Q|>=0.
(1) No P inside S has m(P)=k0:=floor((c+1)/2)+1 (k0<=e): Lemma L would give d(P)<=c-min(e,2k0-1)<0, since 2k0-1>=c+1 and
e>c. A set inside S with more intervals contains a subset with exactly k0 of them. So the independence number of S (S misses
h, so its components are paths) is <=floor((c+1)/2).
(2) The components of S are paths of lengths L_i with sum |S|>=c+1 and independence number sum ceil(L_i/2)>=|S|/2>=(c+1)/2.
With (1): c is odd, |S|=c+1 and every L_i is even. Every run of S lies in a maximum independent set (each even path has two
alternating ones); such a set P has m(P)=(c+1)/2<=e and Lemma L gives d(P)<=c-min(e,c)=0, so P holds no run of Q. Hence Q
is empty and E=c+1.
(3) For every nonempty set Y of empty runs, m(Y)<=c+1<=e, so j=e is admissible and free (2p-2e=2kappa<=A; 2kappa>=b as
2e<=p+1+c); Lemma S gives t(Y)+e in M. RS(b) with K=c+1 on the c+1 nonzero values t_i gives at least min(p,c+2)=c+2
subset sums, hence at least c+1 nonempty ones, all in M-e. So |M|>=c+1>c: contradiction. []
Corollary SH. For 5<=e<=(p+2)/3, kappa=p-e satisfies (p-1)/2<=(2p-2)/3<=kappa<=p-5<=p-3, so UH-A's literal antecedent holds
(prime p>=7; some admissible NF with terminal k=p+1 and kappa^=kappa; every H=e-1 distribution; empty-run rule), and Lemma U
supplies the nonzero common class with orientation A>=A'. UH-A gives 2kappa+3<=A<=2p-1, i.e. 3<=c<=2e-1. Theorem A excludes
3<=c<=e-1 and Theorem R2 excludes e<=c<=2e-1. []

## 9. Scope and interface table

- [RE-DERIVED] (from the candidate RUH2, re-proved here): Secs. 1-5 (SR, pairing, Lemmas P/U, window, MW, the m=e window,
  toggle path, super-heavy run, light sets, counts, Lemma L, Lemma S) and Theorem A. [NEW]: Lemma E, Lemma POS, Theorem R2.
  RUH2's Theorem B (e=5) is not used; Theorems A and R2 re-prove the e=5 cell uniformly.
- Accepted inputs: NF, GRX (if), RS(b), CD; UH-A only for Corollary SH. Not used as premises: RUH2 and its errata, KP3, KP4, R7,
  PP1/KP2, UH-SH/MW/L/PH (UH-E is re-proved as Lemma S), ASSEMBLY-P, RPdelta, REFL, RUNS, S(p), Lev, (S1), LS-family, CT.
Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, LF lines, whole-file SHA256 | Accepted scope; use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16 lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3 |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | R16 lowodd item 1/M2; if direction; C in [Phi,Phi+2e-2] |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | R18 CFXT item 4; K=p-1, w0, b, c+1 |
| CD | classical; proof-ROW-v1.md 4-5 | MW translates |
| UH-A | R18/olson-UH-CONSTRAINTS-parent-verdict-v1.md lines 9,15; 7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3; errata v1 8f1ea491eb2ab8ab4d4f1006896cb9aad63d6c51e270acb190de7bdaf4074ee3, v2 ac2a7f26ef941366e70e939545bae07a5baea6564005af29e5c9185560aaaa50, v3 0dc678867d10f28abc2f1681b21805658318fa9fc3a4c379062152cc1aef813f | Corollary SH only (2kappa+3<=A<=2p-1) |
Verdicts (whole-file SHA256): R16/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only (not premises): terminal-pplus1-upperhalf-exclusion/obstruction-UH-EXCL-v1.md
f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d (R-UH definition, lines 27-48) and its parent errata;
upperhalf-RUH-round2/residual-RUH2-v1.md 267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b (definitions of R1/R2).
