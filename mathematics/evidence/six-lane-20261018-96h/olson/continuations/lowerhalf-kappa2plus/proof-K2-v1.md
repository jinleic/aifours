# K2: the lower-half terminal cell kappa_hat=2 is excluded for every prime p>=11, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T22:59:46-0700. Status: CANDIDATE_UNVERIFIED written proof of the FULL frozen
primary target (K2-scope-v1.md SHA256 37d39e81cad02fbe13f93d299d171c4e19b18a1be4f98b91b1704d137104593f, frozen 22:46:31 before
derivation; authority RUN/control/written-olson-lowerhalf-kappa2-transition-v1.json SHA256
93f75a59338fcfbc327d3fe9ef71118dab8a5aeb30bf33415886cbf857c7136e). All case work by hand; no script, assertion, enumeration or
computation over scientific data. No novelty, priority, Lean or human-review claim; no other cell and no full ordered Olson.

## 0. Statement

THEOREM K2 [NEW]. Let p>=11 be prime. No length-(4p-2) avoider over D_(2p) (no identity 2p-subword in increasing original
index order) has an admissible normal form with terminal k=p+1 and kappa_hat=2. Full antecedent: SOME admissible NF; the
H=p-3 extra reflection pairs anywhere in the odd blocks; every empty NF run separates different reflection values; no o_F,
nonempty-run, rotation-pair or reflection-rigidity hypothesis on the original word.
Intermediate results, at kappa_hat=2 only: LEMMA N (negative letters; it gives the lift inequality 2Pi0+3+nu0>2p), LEMMA F
(a fully-full family replacing (H-ALT)), LEMMA RIG (rotation rigidity with tight lift data), and the final arc contradiction.

## 1. Accepted frame [K1 verdict: Theorem S of proof-LOWER-v1.md, read with parent erratum 087ab3ae]

Notation and results of proof-LOWER-v1.md (PL) at kappa=2; m(P) is half the number of sign transitions (m(empty set) =
m(all runs) = 0; a proper set has m equal to its number of maximal cyclic intervals). N=p+1 runs R_0..R_p (indices mod N),
R=p+3 rotations, F=3p-5 reflections. u is the NF word (an avoider), tau_i=y_i-y_(i-1), T(P)=sum_P tau_i, X^(P) as in PL Sec. 2.
(SR) [PL Sec. 2] For every P and every even n with max(0,6-2m(P)) <= n <= min(p+3,2p-2m(P)), T(P) is not a sum of n letters
 of X^(P). Windows: P empty: [6,p+3]; m=1: [4,p+3]; m=2: [2,p+3]; 3<=m<=M:=(p-3)/2: [0,p+3].
Integer frame [PL Secs. 4-6]. There is a T=0 arc P0 with complementary T=0 arc C0, chosen light: o(P0)<=2, where o(Q) counts
the letters of runs of Q with label b=1 (PL Lemma LT; swapping P0 and C0 negates all labels). After the automorphism
gamma -> 1, every letter l has an odd integer label c_l with original value c_l (mod p): c_l=b_l on C0, c_l=-b_l on P0, where
(PL Lemma IF at kappa=2, 2t<=2):
 t=0: all b_l are positive (L=p+3 of them), W=sum b_l<2p by SC0, W even (p+3 odd terms), so W<=2p-2; m1:=#{b_l=1}>=(3L-W)/2
      >=(p+11)/2 (from W-L=sum(b_l-1)>=2(L-m1)); every b_l<=W-(L-1)<=p-4.
 t=1: the labels are a_1..a_(p+1)>=1 (W=sum a_i), one further +1 (letter z+) and one -1 (letter z-): ZSTRUCT gives
      Z=g^(n+)(-s_1 g)...(-s_(n-) g) with n++n-=2, n->=1, and FB gives sum s_j=n+, so n+=n-=1, s_1=1; FB gives W+1<=2p-1;
      FB-E gives a_i<=p-2; m1:=#{a_i=1}>=(3(p+1)-W)/2>=(p+5)/2.
 In both cases at least (p+7)/2 letters have label b=1.
Put Pi0:=sum of c_l>0, nu0:=sum of |c_l| over c_l<0, B*:=Pi0+nu0=sum|c_l|>=R (each |c_l|>=1), sigma(P):=sum of c_l over the
letters of runs of P, h_i:=tau_i+X_i where X_i=sigma({i}) (mod p) is the sum of run i, H(P)=sum_P h_i.
[PL Lemma SS] the signed sums sum_(l in J) eps_l c_l of X^(P) (J any set of letters) are exactly the integers of
 [-nu(P),Pi(P)], with parity |J|.
[PL Sec. 7] P is FULL if every even v in [-nu(P),Pi(P)] is such a sum with |J| in the (SR) window of P. Lemma U: if P is full,
 B*<=2p-2 and H(P) has a unique representative U(P) in [Pi0+1,2p-1-nu0] with U(P)=sigma(P) (mod 2); U'(P):=U(P)-2p lies in
 [Pi0+1-2p,-1-nu0]. Lemma A: P1,P2 disjoint, P1,P2,P1uP2 full and 2Pi0+3+nu0>2p imply U'(P1uP2)=U'(P1)+U'(P2). Lemma C:
 P and its complement full imply U'(P)+U'(P^c)=Pi0-nu0-2p.
[CJ''', R16 cj-cjx verdict lines 8-15, as applied in PL Sec. 1] if all rotation letters of u are equal (non-identity), u has
 an identity 2p-subword (k=p+1, kappa=2: Delta=-2<=0, R=p+3>=4, 2kappa=4<=p-1, genuine empty runs, odd maximal blocks).

## 2. Lemma N: the negative letters [NEW]

LEMMA N. Let A- be the set of letters with c_l<0. Every l in A- has c_l in {-1,-3}, and |A-|+nu0<=4. Hence
A- is one of {}, {-1}, {-1,-1}, {-3}, nu0<=3, and 2Pi0+3+nu0=2B*+3-nu0>=2(p+3)+3-3=2p+6>2p.
Proof. A letter with c=+1 is a C0 letter with b=1 or z- lying in P0; so u+:=#{c_l=+1}>=#{b=1}-o(P0)>=(p+7)/2-2=(p+3)/2.
A letter with c_l<0 is a P0 letter with b_l>0, or z- lying in C0 (c=-1). An integer zero-sum of X (P empty) of even size n in
[6,p+3] is forbidden by (SR) (target T(empty set)=0).
(a) Suppose c_l=-B with B>=5 (B odd). Then l is a P0 letter with label B, not z+-. Count labels: if t=1, sum(a_i-1)=W-(p+1)
<=p-3; l contributes B-1, so at most (p-2-B)/2 other a_i exceed 1, and at least (p+1)-1-(p-2-B)/2=(p+2+B)/2 of the a_i equal
1; with z+, #{b=1}>=(p+4+B)/2. If t=0, sum(b-1)=W-(p+3)<=p-5, at most (p-4-B)/2 other labels exceed 1, so #{b=1}>=
(p+3)-1-(p-4-B)/2=(p+8+B)/2. In both cases u+>=#{b=1}-2>=(p+B)/2>=B (B<=p-2). The letter l with B letters of value +1 is an
integer zero-sum of X of size B+1, which is even and lies in [6,p-1]: forbidden. So every negative letter has |c| in {1,3}.
(b) Suppose |A-|+nu0>=6. List A- in any order; x_j := j + (weight of the first j letters) is even and increases by 2 or 4 per
letter, from x_0=0. Let x_j be the first value >=6; then x_j in {6,8}, and the weight w_j<=x_j-1<=7<=(p+3)/2<=u+ (p>=11).
The first j letters with w_j letters of value +1 form an integer zero-sum of X of size x_j in [6,8]: forbidden. So
|A-|+nu0<=4. Each |c|>=1 is odd, which leaves the four listed sets. The last inequality uses B*>=R=p+3 and nu0<=3. []

## 3. Lemma F: a family of full patterns and additive lifts [NEW at kappa=2]

Let F be the family of sets Q of runs with 3<=m(Q)<=M=(p-3)/2 (M>=4 as p>=11). Write S_ev={0,2,...,p-1}, S_od={1,3,...,p}
(N even; each is a set of (p+1)/2>=6 pairwise non-adjacent runs, and S_od is the complement of S_ev).
(F1) Every Q in F is full: its (SR) window is all even n in [0,p+3], and every v in [-nu(Q),Pi(Q)] is a signed sum by PL
 Lemma SS. Hence B*<=2p-2 (Lemma U), and Lemmas A and C apply inside F (the inequality of Lemma A is Lemma N).
(F2) Increments. If Q and Q u {i} (i not in Q) are full, d:=U'(Q u {i})-U'(Q) satisfies d=h_i (mod p), d=sigma({i}) (mod 2)
 and |d|<=(-1-nu0)-(Pi0+1-2p)=2p-2-B*<=p-5. Two such differences d,d' (from different Q) satisfy d-d'=0 (mod 2p) and
 |d-d'|<=2p-10, so d=d'. For every run i such a pair exists in F: Q={i+2,i+4,i+6} has m(Q)=3 and m(Q u {i})=4<=M (N>=12,
 so i+6 and i are not adjacent). Define theta_i as this common value; then theta_i=h_i (mod p), theta_i=sigma({i}) (mod 2).
(F3) Connectivity. Call Q,Q' in F neighbours if they differ in one run. F is connected:
 (a) if Q in F has an interval [x,y] with x!=y, then Q\{y} has the same number of intervals; repeating, Q is joined to an
     independent set (pairwise non-adjacent runs) of m(Q) runs;
 (b) removing one run from an independent set of >=4 runs leaves an independent set with m>=3; repeating gives a triple;
 (c) for an independent triple a,b,c in cyclic order let g_a,g_b,g_c>=1 be the numbers of runs strictly between a and b,
     b and c, c and a (sum N-3>=9). If g_a>=2, the set {a,a+1,b,c} has the three intervals {a,a+1},{b},{c} (b>=a+3), and
     {a+1,b,c} is an independent triple: "advancing" a moves one unit from g_a to g_c through F; symmetrically "retreating"
     a moves one unit from g_c to g_a when g_c>=2. Transferring units from a gap above its target value to one below it
     (the donor is >=2), any triple reaches the gap vector (3,3,N-9); with all gaps >=2, advancing c, then b, then a (each
     time the gap ahead is >=2) shifts the triple by one position and restores its gaps. So all independent triples are
     joined, and F is connected.
(F4) Additivity of theta. Put f(Q):=U'(Q)-sum_(i in Q) theta_i on F. By (F2), f(Q u {i})=f(Q) for neighbours, so f is a
 constant f0 by (F3). For P1={0,2,4} and P2={1,6,8} (both independent triples, N>=12), P1 u P2 has the intervals
 {0,1,2},{4},{6},{8}, so m=4<=M; Lemma A gives U'(P1 u P2)=U'(P1)+U'(P2), hence f0=2f0 and f0=0:
   U'(Q)=sum_(i in Q) theta_i for every Q in F.
(F5) Total. Q0={0,2,4} and its complement both have m=3, so Lemma C and (F4) give
   sum over all runs of theta_i = U'(Q0)+U'(Q0^c) = Pi0-nu0-2p = B*-2nu0-2p.                                        []

## 4. Lemma RIG: rotation rigidity with tight data [NEW at kappa=2]

LEMMA RIG. B*=R=p+3: every |c_l|=1, so all rotation letters lie in {rho_1,rho_-1}; nu0=|A-| is in {0,1,2}; and in each of
S_ev, S_od the theta-values are: theta_(1)+theta_(2)=-nu0 and theta_(j)=-1 for every j>=3 (decreasing order).
Proof. Fix S in {S_ev,S_od} and order its theta-values decreasingly. Its top three runs are pairwise non-adjacent, so they form
a set J* in F with m(J*)=3, and theta_(1)+theta_(2)+theta_(3)=U'(J*)<=-1-nu0 by (F4) and Lemma U. Thus theta_(3)<0, so
theta_(3)<=-1 and theta_(j)<=-1 for all j>=3, and
  sum_S theta <= (-1-nu0) - (|S|-3).
Adding the bounds for S_ev and S_od ((p+1)/2 runs each) and using (F5):
  B*-2nu0-2p <= -2-2nu0-(p+1-6) = -p+3-2nu0,   i.e.   B* <= p+3 = R.
As B*>=R, equality holds everywhere: every |c_l|=1; in each S the top-three sum is -1-nu0 and theta_(j)=-1 for j>=4; since
theta_(4)=-1<=theta_(3)<=-1, theta_(3)=-1 and theta_(1)+theta_(2)=-nu0. With |c|=1, Lemma N gives A-={} or {-1} or {-1,-1}. []

## 5. Proof of Theorem K2 [NEW]

Assume an avoider as in Sec. 0 and use its NF word u in the frame of Sec. 1. By Lemma RIG every letter has value +1 or -1
(after gamma -> 1) and exactly nu0 letters have value -1. For every run i: tau_i = theta_i - sigma({i}) (mod p) (as
theta_i=h_i=tau_i+X_i and X_i=sigma({i})), theta_i = sigma({i}) = r_i (mod 2), and for a single run, T({i})=tau_i, m({i})=1,
window [4,p+3]. X^({i}) is X with the letters of run i negated.
Case nu0=0. All rotation letters equal rho_gamma, gamma!=0: excluded by CJ''' (Sec. 1).
Case nu0=2. In each alternating set theta_(1)+theta_(2)=-2 with theta_(2)>=theta_(3)=-1, so theta_(1)=theta_(2)=-1: every
 theta_i=-1. Then every r_i is odd, and sum(r_i-1)=R-N=2 forces one run of length 3 and p runs of length 1. At most two of
 these singletons hold a -1, so some singleton run i holds a +1: sigma({i})=1 and tau_i=-1-1=-2. In X^({i}) the flipped
 letter and the two original -1 letters (outside i) have value -1, and p letters have value +1. Three -1's and one +1 form
 n=4 letters with sum -2=T({i}), and n=4 lies in the arc window: an identity 2p-subword, contradiction.
Case nu0=1. In each alternating set theta_(1)+theta_(2)=-1 with theta_(2)>=-1, so theta_(1)=0, theta_(2)=-1: exactly one run
 of S_ev and one run of S_od have theta=0, all other runs theta=-1. A run e with theta_e=0 has r_e even (parity), and it is
 not empty: an empty run has X_e=0 and tau_e!=0 (empty-run rule), so theta_e=h_e=tau_e!=0 (mod p). The two theta=0 runs
 are different (one in each alternating set) and only one letter has value -1, so one of them, e, has all its r_e>=2
 letters equal to +1: sigma({e})=r_e and tau_e=0-r_e=-r_e (mod p). In X^({e}) the r_e flipped letters and the original -1
 (outside e) give r_e+1 letters of value -1, and p+2-r_e>=1 letters have value +1 (r_e<=p+1: r_e is even and the -1 letter
 is outside e, so r_e<=R-1=p+2). Take all r_e+1 letters of value -1 and one +1: n=r_e+2 is even, 4<=n<=p+3, and the sum is
 -r_e=T({e}) (mod p): an identity 2p-subword, contradiction.
All cases are impossible; since u is an avoider by NF, so is the hypothesis. This proves Theorem K2. []
Remark (failed route kept). Theorem P is not used. The K1 route of PL Sec. 8 (additivity over single runs) fails at kappa=2:
a single run is an arc with window [4,p+3], and e.g. when nu0=0 and run i is one letter of value c>0, the even value v=1-c is
a signed sum of X^({i}) only with |J|=2 (three positive odd letters sum to at least 3), so {i} need not be full. Lemma F
replaces single runs by the family 3<=m<=(p-3)/2, which is full for every word at kappa=2, and Lemma N supplies the lift
inequality; this replaces (H-ALT) and the third antecedent of PL Lemma CR at kappa=2 only.

## 6. Scope, boundary and interface table

- Claimed: Theorem K2 (cell kappa_hat=2, every prime p>=11, full existential-NF/word antecedent). Lemmas N, F, RIG are proved
  only at kappa_hat=2 in this frame. NOT claimed: any other lower-half cell 3<=kappa_hat<=(p-3)/2 (still open), kappa_hat=0,
  p<11, (H-ALT) or the lift inequality for kappa>=3, reflection rigidity, INV*, o_F assembly, full ordered Olson, any
  multiset-only statement outside the antecedent. Route remark only (no claim): the argument uses kappa=2 in the window
  arithmetic of (F1) (3<=m<=(p-3)/2 needs p>=9), in Lemma N (forbidden sizes from 6), and in the tight case analysis of Sec. 5.
- [NEW]: Lemma N, Lemma F (F1-F5), Lemma RIG, Sec. 5. [CITED, accepted]: PL Theorem S (SR, Lemma IF, SS/D, LT, U, A, C) per
  the K1 verdict and parent erratum; CJ''' (all-equal sub-case only). Not used: Theorem P, RS, CD, LS-family, UH results,
  unreviewed candidates (BOTTOM/RUH3 concern other cells; their acceptance is not used).
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review; R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md.
| Input | Text, whole-file SHA256 | Scope; use |
|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | Theorem S accepted relative to its inputs; CR conditional only (not used) |
| parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | m(P) convention; theta only via full pairs (F2) |
| PL | PL Secs. 1-7 (lines 26-129); 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | SR, IF, D, SS, LT, U, A, C at kappa=2 |
| PL inputs | NF, GRX (if), S1(a), SC0, ZSTRUCT/FB/FB-E/Setting fact in (S') as pinned in PL Sec. 10 and LOWER-scope-addendum-1.md (0a68bf4204623d9cff7950175bda235fffefe120a3a203e478fc333fadd60442) | through Lemma IF only |
| CJ''' | R16/olson-cj-cjx-parent-verdict-v1.md lines 8-15; 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d | case nu0=0 only |
