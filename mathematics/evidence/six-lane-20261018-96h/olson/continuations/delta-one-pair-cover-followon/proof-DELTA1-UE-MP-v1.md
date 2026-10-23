# DELTA1 top/middle-plus cover: R=p+1, kappa in {(p+1)/2, p-3, p-2, p-1}; complete residual

CANDIDATE written mathematics by hand; no parent/model gate run. Outcome category (b): a strictly larger UNIFORM
exclusion than the accepted baseline, the complete remaining residual of the ENTIRE target, and an exact first
unproved lemma. Not full DELTA1-PAIR-COVER: four small-prime middle-minus cells remain. Re-derived after the
disclosed exposure (DELTA1-exposure-acknowledgement-v1.md); no novelty, priority, independence or corroboration
claim. No scientific computation, enumeration, solver, test, model, network or nested agent was used.

## 0. Target, imports, statements

Target class C(p,kappa): p>=7 prime; u a word of length 4p-2 over D_(2p) with exactly R=p+1 rotation letters, all
in one nonzero pair {rho_c,rho_-c}; every maximal cyclic CONSTANT reflection block of odd length;
kappa:=p-1-sum_i floor(l_i/2) in [2,p-1]. Any B, mixed or pure runs, genuine empty gaps, all reflection values,
all odd-block pairs. No B<kappa, purity, inherited condition, original-o_F bound or rigidity assumption.
"Identity2p-subword" means 2p letters in increasing ORIGINAL index order with identity product; a cyclic
selection suffices by conjugation (RP-LIFT verdict binding1).

Imports (literal accepted statements at their own scopes; full bodies/overlays in the source packet):
(W),(L2.1),(L3.1),(BAL),(F2.2), the e5 realisation rule with I.6/I.7, setting (S) and normalisation: REFLHI v5
proof-REFLHI-arcs-v5.md read through errata1-5 Part I (Part II NOT used), accepted by the REFLHI v5 parent verdict;
exact scopes per foundation review Sec.C ("words in (S); 2.2 under avoidance; e5 only for singleton/pair choices").
(P0) e_R<=e_F+2kappa: proof-K0star-r2.md LF73-75, accepted by the K0*/RED verdict and carried into v5; its source
Theorem P at its own acceptance (TheoremP import-closure verdict + errata1/2). (CD) classical Cauchy-Davenport.
Baseline statements only (no proof step used): RPdelta verdict items6-7 and E1 (with its consolidated E1-E5 and
parent erratum), RP-2NE verdict, D1-END verdict (+errata v1/v2), REFLHI v5 I.14 R=p+delta bands (erratum5 I.14).
NOT used: Fact 2.1, ARC+ segments, Lemma SEG, Theorems SEG/K2P+/TOP as premises (TOP's compensation idea is
re-derived here), FP/FP-1, erratum5 Part II, HK1/HIGH-K-RES, the unaccepted HIGH-K-CORE candidate, S(p), Lev, CT,
B.4, CJ/EDGE, ASSEMBLY-LS/P, frontier v8, UPAR5.

THEOREM D1-UE (candidate). For every prime p>=7 and kappa in {p-3,p-2,p-1} with (p,kappa)!=(7,4), every word of
C(p,kappa) has an identity2p-subword.
THEOREM D1-MP (candidate). For every prime p>=7, every word of C(p,(p+1)/2) has an identity2p-subword.
COROLLARY (union with the accepted baseline, Sec.6). DELTA1-PAIR-COVER holds for every prime p>=19 and every
kappa in [2,p-1]; for p in {7,11,13,17} it holds for every kappa except kappa=(p-1)/2.

## 1. Normalisation and avoider data

The automorphism (v,eps)->(c^(-1)v,eps) of D_(2p) maps rho_(+-c) to rho_(+-1), preserves letter order, block lengths,
maximality, empty runs and identity selections; normalisation N (v->-v, K0star-r2 LF35-36) gives A>=B. So u is in
setting (S): R=p+1>=1, F=4p-2-R=3p-3>=1. Write u=R_1S_1...R_kS_k (run R_t precedes block S_t), S_t of odd length
2h_t+1, H=sum h_t=p-1-kappa, F=2H+k, hence k=p-1+2kappa. Assume u avoids.
(A1) By (P0) with e_F=0, at most 2kappa runs R_t have an even number of letters (empty runs count as even), so
o_R>=k-2kappa=p-1 runs are odd, hence nonempty.
(A2) sum_t r_t=p+1 and r_t=[R_t odd] mod2 give o_R even, so o_R in{p-1,p+1}. The excess
sum_(odd runs)(r_t-1)+sum_(even nonempty runs)r_t=p+1-o_R is 0 or 2, each odd-run term even>=0, each even-nonempty
term even>=2. Exactly one case holds: (Q+) o_R=p+1, every nonempty run has one letter, q=p+1; (Q0) one nonempty
run has 2 letters, all others one, q=p; (Q-) one run has 3 letters, all others one, q=p-1. Here q is the number of
nonempty runs N_1..N_q (cyclic order). Hence d:=max_j|d(N_j)|<=3, and d=1 in case (Q+).
(A3) M_i is the maximal reflection run between N_i and N_(i+1) (i=1..q), |M_i|>=1 blocks, sum_i|M_i|=k; consecutive
blocks of M_i are separated by EMPTY runs, which are genuine. A pair is a two-block arc of two consecutive blocks of
one M_i (nu=2); a singleton is a one-block arc (nu=1). Pair capacity c:=sum_i floor(|M_i|/2)=(k-o_M)/2 with
o_M:=#{i:|M_i| odd}<=q and o_M=k mod2. A block of M_i lying in no pair is FREE (it may be a singleton or unused).
(A4) For every arc choice (v5 Sec.3, sum c_i even, >=2), T=sum_j z_j d(N_j) is EVEN, since d(N_j)=r(N_j) mod2 and
sum_j r(N_j)=p+1. By (BAL) with I.6, for every index i there is i'!=i such that changing the parities of c_i and
c_(i') gives |T|<=d; then |T|<=2, and T=0 in case (Q+). If already |T|<=d nothing is changed.

## 2. Lemma GW (direct-window arc lemma; fresh proof)

Let u be in (S). Let an arc choice consist of 2m>=2 pairwise disjoint arcs, each a singleton or a pair, G of them
pairs, with Lemma-3.1 value T, and put E_+-=(R+-T)/2. If gamma_m(E_+)>=0, gamma_m(E_-)>=0 and
   gamma_m(E_+)+gamma_m(E_-)+G>=p-1,                                                         (GW)
gamma_m(E):=min(p-m,E-kappa+m-1,floor(E/2)) as in (W), then u has an identity2p-subword.
Proof. Number the arcs cyclically X_1,Y_1,...,X_m,Y_m; each gap contains the run right after its arc, so this is an
arc system. By (L2.1), for every a_i in X_i and b_i in Y_i, P:=union_i of the runs R_(a_i+1),...,R_(b_i) is a
proper pattern with exactly m intervals, E+(P)=E+ (the base value, independent of the choices) and
u_P=(1/2)sum_i(y_(a_i)-y_(b_i)). By (L3.1), {E+(P),E-(P)}={E_+,E_-}. The window of (W),
I=[-gamma_m(E-(P)),gamma_m(E+(P))], is an integer interval containing 0 with gamma_m(E_+)+gamma_m(E_-)+1 integers,
hence min(p,gamma_m(E_+)+gamma_m(E_-)+1) residues. The set of attained u_P contains the sumset of the sets
(1/2)V(X_i) and -(1/2)V(Y_i), V(X) the set of block values of X (|V|=1 for a singleton, 2 for a pair, since the run
inside a pair is a genuine empty run); (CD) gives at least min(p,1+G) residues. If either count is p the two sets
meet; otherwise the counts sum to >=p+1 by (GW), so they meet. Some choice has u_P congruent to an element of I, and
(W) gives an identity2p-subword (cyclic, hence in increasing original order by conjugation). []
With s:=p-m one has E-kappa+m-1=E+H-s, so gamma_m(E)=min(s,E-s+H,floor(E/2)). Put e:=(p+1)/2, so E_+-=e+-T/2, and
Gamma(s,T):=gamma(E_+)+gamma(E_-).

## 3. Theorem D1-UE (kappa=p-1-H, H in {0,1,2})

Here k=3p-3-2H. Put s0:=floor((p+1)/4), m0:=p-s0.
Step 1 (window). For T in{0,+2,-2} and every H>=0: Gamma(s0,T)>=e-1=(p-1)/2, both gamma>=0.
 p=4a+1 (a>=3), e=2a+1, s0=a. T=0: gamma(2a+1)=min(a,a+1+H,a)=a; Gamma=2a. |T|=2: gamma(2a+2)=min(a,a+2+H,a+1)=a,
 gamma(2a)=min(a,a+H,a)=a; Gamma=2a=e-1.
 p=4a+3 (a>=1), e=2a+2, s0=a+1. T=0: gamma(2a+2)=min(a+1,a+1+H,a+1)=a+1; Gamma=2a+2=e. |T|=2:
 gamma(2a+3)=min(a+1,a+2+H,a+1)=a+1, gamma(2a+1)=min(a+1,a+H,a)=a; Gamma=2a+1=e-1.
So by Lemma GW any singleton/pair choice with exactly 2m0 arcs, at least (p-1)/2 pairs and |T|<=2 gives an identity.
Step 2 (counts). c>=(k-q)/2>=(k-p-1)/2=p-2-H. G0:=(p+1)/2. Since 2s0=(p-1)/2 (p=4a+1) or (p+1)/2 (p=4a+3),
G0+2m0=2p+1 resp. 2p, and 2m0-G0=p resp. p-1, which is >=1.
Step 3 (initial choice with a designated run M_l). Exactly 2m0 arcs, exactly G0 pairs, and a run M_l carrying a
designated singleton and either (type A) a designated UNUSED block or (type B) a designated pair.
 Type A, when c>=G0+1. Choose l with |M_l|>=2 (k-q>=2p-4-2H>0). Designate the first block of M_l as the singleton and
 the second as the reserved unused block; the other |M_l|-2 consecutive blocks still hold floor(|M_l|/2)-1 disjoint
 pairs, so c-1>=G0 pairs avoid the two designated blocks; take G0 of them. The 2m0-G0-1 further singletons go on
 unused blocks other than the reserved one; this needs G0+2m0<=k-1.
 c>=G0+1 holds if p-2-H>=(p+3)/2, i.e. H<=(p-7)/2: every p>=11 (H<=2) and p=7,H=0. G0+2m0<=k-1 holds for p>=11 since
 G0+2m0<=2p+1<=3p-8<=k-1, and for p=7 (p=4a+3, G0+2m0=14) when H<=1 (k-1=17-2H).
 Type B, the only other case with H<=2 and (p,H)!=(7,2): p=7, H=1, c=4=G0. Then k=16, c=(16-o_M)/2 forces o_M=8, so
 q=8 and every |M_i| is odd; as sum|M_i|=16>8, some |M_l|>=3. In M_l designate blocks1-2 as a pair and block3 as the
 singleton, add (|M_l|-3)/2 further pairs, and floor(|M_i|/2) pairs in every other M_i: G0=4 pairs. The other 5 of the
 6=2m0-G0 singletons go on free blocks of other runs (7 available). Blocks used: G0+2m0=14<=16.
Step 4 (balancing at fixed arc count). Apply (BAL) at i=l; let i'!=l. Realise the parity change at i' by an
applicable e5/I.7 move: delete a singleton (eps'=-1), add a singleton on an unused block (eps'=+1), or split a pair
(eps'=+1, one pair lost). Realise the change at l by: eps'=+1: delete the designated singleton; eps'=-1: add a
singleton on the reserved block (type A, no loss) or split the designated pair (type B, one pair lost). Each is a
valid parity change (I.7). The arc count stays 2m0; a pair is lost at i' only when eps'=+1, and then the move at l is
a deletion; a pair is lost at l only when eps'=-1, and then the move at i' is a deletion. So at most ONE pair is
lost, G>=(p-1)/2, the result consists of singletons and pairs, and |T|<=2 by (A4).
Step 5. Lemma GW with m=m0 (Step 1) gives an identity2p-subword, contradicting avoidance. []

## 4. Theorem D1-MP (kappa=e=(p+1)/2, H=e-2, k=2p)

Step 1 (window range; gamma(E)=min(s,E-s+e-2,floor(E/2))).
 p=4a+1 (a>=3, e=2a+1, H=2a-1). T=0: gamma(2a+1)=min(s,4a-s,a)=a for a<=s<=3a; Gamma=2a. |T|=2:
 gamma(2a+2)=min(s,4a+1-s,a+1)>=a and gamma(2a)=min(s,4a-1-s,a)=a for a<=s<=3a-1; at s=3a, gamma(2a+2)=a+1 and
 gamma(2a)=a-1. So Gamma(s,T)>=2a for every s in[a,3a] and T in{0,+-2}; all gamma>=a-1>=0. (GW) needs G>=4a-2a=2a.
 p=4a+3 (a>=1, e=2a+2, H=2a). T=0: gamma(2a+2)=min(s,4a+2-s,a+1)=a+1 for a+1<=s<=3a+1; Gamma=2a+2. |T|=2:
 gamma(2a+3)=min(s,4a+3-s,a+1)=a+1 and gamma(2a+1)=min(s,4a+1-s,a)=a for a+1<=s<=3a+1; Gamma=2a+1. (GW) needs
 G>=2a if T=0 and G>=2a+1=(p-1)/2 if |T|=2.
Step 2 (initial choice). s0:=a+1 (p=4a+1) or a+2 (p=4a+3), m0:=p-s0; then s0-1,s0,s0+1 lie in the Step-1 range
(a>=1). Choose G0 pairs:
 (Q0),(Q-): o_M<=q<=p and o_M even give o_M<=p-1, c>=(p+1)/2; G0:=(p+1)/2.
 (Q+): o_M<=p+1 gives c>=(p-1)/2. If c>=(p+1)/2, G0:=(p+1)/2. If c=(p-1)/2, then o_M=p+1=q, every |M_i| is odd;
 take G0:=c, i.e. floor(|M_i|/2) pairs in every M_i, so every M_i has exactly ONE free block.
 Blocks: 2m0+G0<=k=2p iff G0<=2s0, and 2s0=(p+3)/2 resp. (p+5)/2>=(p+1)/2. Then 2m0-G0 singletons fit on the
 2p-2G0 free blocks, and 2m0-G0>=0. Since 2G0<2p, some M_i has a free block; fix such i.
Step 3 (balancing with flexible arc count). Apply (BAL) at this i; let i'!=i. Realise both parity changes by the e5
rule. At i it deletes a singleton or adds one on an unused block (M_i has a free block), never splitting; at i' it
splits a pair only if M_(i') has no free block, never in the case c=(p-1)/2 of (Q+). The arc count becomes
2m0+Delta, Delta in{-2,0,2}, so s'=s0-Delta/2 in{s0-1,s0,s0+1} lies in the Step-1 range and the new m'>=m0-1>=1;
the result consists of singletons and pairs; G>=G0-1, with G=G0 in the case c=(p-1)/2; |T|<=2 and T=0 in (Q+).
Step 4. (Q0),(Q-): G>=(p-1)/2 suffices for both residue classes. (Q+),p=4a+3: T=0 and G>=G0-1>=(p-3)/2=2a.
(Q+),p=4a+1: G>=(p-1)/2=2a (G0=(p+1)/2 with one possible loss, or G0=(p-1)/2 with none). Lemma GW at s' gives an
identity2p-subword, contradicting avoidance. []
Check p=7 (a=1): s0=3, s' in{2,3,4}; Gamma=4 (T=0) or 3 (|T|=2); (Q+) G>=2, (Q0),(Q-) G>=3; blocks 2m0+G0<=12<=14.

## 5. Why kappa=(p-1)/2 at p in{7,11,13,17} is NOT closed here (method failure, not a no-go)

At kappa=(p-1)/2: H=e-1, k=2p-2 and c=(2p-2-o_M)/2. For p=4a+1 (p=13,17), case (Q+) with every |M_i| odd gives
c=(p-3)/2=2a-1, while Gamma(s,0)<=2floor(e/2)=2a for every s, so Gamma+G<=4a-1<p-1: the pair-only route of Lemma GW
is one short. For p=4a+3 (p=7,11), case (Q0) with a pure two-letter run, o_M=p-1 and the unique even |M_j| fully
paired, c=(p-1)/2 equals the requirement for |T|=2, and the partner index of (BAL) may be that fully paired run,
losing a pair; the construction above does not close this sub-case. Longer arcs, segments (ARC+), raw SEG, B.4 or a
refined balancing might close some cells; none is claimed. No avoiding word is asserted.

## 6. Union with the accepted baseline; ENTIRE residual; diagnostics

Accepted numerical providers at delta=1 (universe kappa in[2,p-1]), by hand set algebra (cp-01):
RPdelta E1: A(p,1)=[ceil((p+5)/4),(p-5)/2] u [(p+3)/2,p-4], E(p,1)=empty; B-prime N(p,1): (p-1)/2 iff p>=19,
(p-3)/2 iff p>=17. RP-2NE: [2,(p-5)/2]. D1-END: {(p-3)/2}. New (candidate): {(p+1)/2} u {p-3,p-2,p-1}, all p>=7.
Union: p>=19: all of [2,p-1]. p in{11,13,17}: [2,p-1] minus {(p-1)/2}. p=7: {2,4,5,6}.
ENTIRE remaining residual of DELTA1-PAIR-COVER: words of C(p,(p-1)/2) for p in{7,11,13,17}, i.e. the four cells
(p,kappa)=(7,3),(11,5),(13,6),(17,8) at R=p+1, any B, with all target word data. Accepted necessary/word-dependent
conditions there (not universal bands, no feasibility): (A1)-(A4); failure of raw Theorem SEG's hypotheses (v5 with
errata4/5); at (17,8) RPdelta E5/B.4: |AB|<=N_O and x=0; the B=0 CJ/EDGE coverage recorded in the RPdelta verdict
(not read or bound here, not used). FIRST UNPROVED LEMMA D1-SMALL-MIDDLE: no word of C(p,(p-1)/2) avoids, for
p in{7,11,13,17}.

| Mandatory diagnostic, every prime p>=7 | Outcome |
|---|---|
| D1-MIDDLE-PLUS kappa=(p+1)/2 | excluded by Theorem D1-MP (new, candidate) |
| D1-UPPER-ENDS kappa in{p-3,p-2,p-1} | excluded by D1-UE, and (7,4) by D1-MP (new, candidate) |
| D1-MIDDLE-MINUS kappa=(p-1)/2 | p>=19 ALREADY covered by RPdelta B-prime (eps0), no new credit; p in{7,11,13,17} OPEN |

This is a statement about the stated uniform pair/all-odd word class only: not arbitrary high-terminal NFs, not
arbitrary original words, not full ordered Olson, not the only remaining gap; no inverse avoidance transfer and no
unrestricted REFL/INV* composition. p=5 is not included.

## 7. Exposure and process precision

TOP's fixed-arc-count compensation (v5 Sec.6 with e4/I.15) and Lemma 3.2's balanced-kill counting are the models;
every step is re-derived above from (W),(L2.1),(L3.1),(BAL),(F2.2)/(P0) and (CD). Erratum5 Part II (single-family,
NOT accepted) also evaluates gamma_m directly; it was read before this proof and is not used. Permanent process
history in the acknowledgement remains uncured. Parent alone runs reviews and verdicts.
