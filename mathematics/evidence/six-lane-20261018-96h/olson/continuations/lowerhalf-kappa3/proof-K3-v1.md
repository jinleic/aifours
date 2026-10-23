# K3: lower-half terminal cell kappa_hat=3 - excluded for every prime p>=13; p=11 excluded outside an explicit residual, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T23:50:09-0700. Status: CANDIDATE_UNVERIFIED written proofs; LABELLED PARTIAL of the
frozen target (K3-scope-v1.md SHA256 5b04e5ac805c225f25820d52447752ebc6a8d6278dde9e459a24ca38c7c12676, frozen 23:29:01 before
derivation; authority RUN/control/written-olson-lowerhalf-kappa3-transition-v1.json SHA256
d7530d176e16a5b2a4555335487f1462bf5091068f7c005d43419de2acb22311): the cell is closed for every prime p>=13; the prime p=11 is
isolated explicitly (Theorem K3-11 and Sec. 7). All case work by hand; no script, assertion, enumeration or computation over
scientific data. No novelty, priority, Lean or human-review claim; no other cell; no full ordered Olson.

## 0. Statements

Full antecedent throughout: a length-(4p-2) avoider w over D_(2p) (no identity 2p-subword in increasing original index order)
has SOME admissible NF u with terminal k=p+1 and kappa_hat=3; the H=p-4 extra reflection pairs lie anywhere in the odd blocks;
every empty NF run separates different reflection values; no o_F, nonempty-run, rotation-pair or reflection-rigidity
hypothesis on w.
THEOREM K3 [NEW]. For every prime p>=13, no such avoider exists.
THEOREM K3-11 [NEW, partial]. For p=11, no such avoider exists whose NF u, in the integer frame of Sec. 1, satisfies (H11):
some run contains a letter with c>0 and a letter with c<0, OR at most three runs contain no letter with c>0.
NOT PROVED (exact residual, Sec. 7): p=11 with (H11) failing.
Intermediate results (kappa_hat=3 only): LEMMA N3 (negative letters; lift inequality), LEMMA FULL (fullness of m=4 patterns),
LEMMA F3 (lift framework on all m=4 patterns), LEMMA RIG3 (rigidity with tight data), and the final cases (Sec. 6).

## 1. Accepted frame at kappa=3 [K1 verdict: Theorem S of PL = proof-LOWER-v1.md, with parent erratum 087ab3ae]

Notation of PL Secs. 2-7 with kappa=3; m(P) is half the number of sign transitions (a proper nonempty P has m(P) equal to its
number of maximal cyclic intervals). N=p+1 runs R_0..R_p (indices mod N), R=p+5 rotation letters, F=3p-7 reflections.
tau_i=y_i-y_(i-1), T(P)=sum_P tau_i, X^(P) = the letter values with the letters of runs of P negated.
(SR) [PL Sec. 2] For every proper nonempty P and every even n with max(0,8-2m(P)) <= n <= min(p+5,2p-2m(P)), T(P) is not a
 sum of n letters of X^(P); for P empty the window is [8,p+5] with target 0. Windows: m=1: [6,p+5]; m=2: [4,p+5];
 m=3: [2,p+5] (p>=11); m=4: [0,min(p+5,2p-8)], which is [0,R] iff p>=13 and [0,14] at p=11 (R=16).
Integer frame [PL Lemma IF (accepted for general kappa), PL Lemma LT]. A T=0 arc P0 and its complementary T=0 arc C0 exist;
the sequence Y of elements (1,x) over the letters x of X^(P0) has no zero-sum of length in [6,2p] ((SR) at P0, m=1, R<2p), so
accepted S1(a) at kappa'=2 bounds its zero-sums by 4: a longest zero-sum Z has |Z|=2t, t in {0,1,2}; Y'=Y-Z is zero-sum free of
length L=p+5-2t>=p+1; SC0 gives a generator g=(1,gamma), gamma!=0, and odd labels a_1..a_L>=1 with W=sum a_i<2p. For t>=1, Y is
in setting (S') with (k',kappa')=(p-1,2) (|Y|=2p+2kappa'-k'=p+5), and ZSTRUCT/FB give Z=g^(n+)(-s_1 g)...(-s_(n-) g) with odd
s_j>=1, n+ + n- = 2t, balance sum s_j = n+, and W + n+ <= 2p-1. Since s_j>=1, n- <= n+, and n-=0 would force n+=0:
 t=1: n+=n-=1, s_1=1 (extra labels +1, -1);  t=2: (n+,n-)=(2,2), s=(1,1) (extra +1,+1,-1,-1) or (3,1), s_1=3 (extra +1,+1,+1,-3).
W is even (L odd terms, L = p+5-2t even), so W<=2p-2 (t=0,1) and W<=2p-1-n+, i.e. W<=2p-4 (t=2).
Counting [W-L=sum(a_i-1)>=2(L-m1), m1:=#{a_i=1}]: t=0: m1>=(p+17)/2; t=1: m1>=(p+11)/2; t=2: m1>=(p+7)/2. Hence the number #1 of
letters with label b=+1 (a-labels 1 and the n+ extra +1's) satisfies #1>=(p+11)/2 in all cases. Every a_i<=W-(L-1)<=p-4, so
every label has |b|<=p-4 (the extra labels are +-1, -3).
Light side: PL Lemma LT gives min(o(P0),o(C0))<=3 (o(Q) = #letters of runs of Q with b=1); swapping P0 and C0 keeps the labels
b and negates gamma; choose P0 with o(P0)<=3. After the automorphism gamma -> 1 every letter l has the odd integer label
c_l = b_l (l in C0), c_l = -b_l (l in P0), and original value c_l (mod p). Put u+:=#{l : c_l=+1} >= #1 - o(P0) >= (p+5)/2
(l in C0 with b_l=1 has c_l=+1). A- := {l : c_l<0}; Pi0, nu0 := sums of |c_l| over c_l>0, c_l<0; B*:=Pi0+nu0>=R;
sigma(P) := sum of c_l over the letters of runs of P; h_i := tau_i + X_i with X_i = sigma({i}) (mod p).
[PL Lemma SS] the signed sums sum_(l in J) eps_l c_l of X^(P) (J any set of letters) are exactly the integers of [-nu(P),Pi(P)],
 and such a sum has the parity of |J|.
[PL Sec. 7] FULL, Lemma U (a full P forces B*<=2p-2 and gives U(P) in [Pi0+1,2p-1-nu0], U(P)=sigma(P) (mod 2), U'=U-2p in
 [Pi0+1-2p,-1-nu0]), Lemma A (needs 2Pi0+3+nu0>2p), Lemma C (complements).
[CJ''', R16 cj-cjx verdict lines 8-15] if all rotation letters of u equal one non-identity rotation, u has an identity
 2p-subword: here k=p+1, kappa=3, Delta=k-p-kappa-1=-3<=0, R=p+5>=4kappa-4=8, 2kappa=6<=p-1, odd maximal blocks (each S_i is a
 maximal constant block by the empty-run rule), genuine empty runs.

## 2. Lemma N3: negative letters [NEW]

LEMMA N3. Every l in A- has c_l in {-1,-3,-5}, and x(A-) := |A-| + nu0 <= 6. Hence A- is one of {}, {-1}, {-1,-1},
{-1,-1,-1}, {-3}, {-3,-1}, {-5}; |A-|<=3; nu0<=5; and 2Pi0+3+nu0 = 2B*+3-nu0 >= 2(p+5)+3-5 = 2p+8 > 2p.
Proof. An integer zero-sum of X (P empty: a set of letters whose labels sum to 0) of even size in [8,p+5] is forbidden by
(SR). A letter with c=-B, B>=5, is a letter of P0 with an a-label B (the extra labels are +1, -1, -3; letters of C0 have c=b).
(a) Let c_l=-B, B>=7. Count the a-labels equal to 1 when one a-label is B: the other a-labels exceed 1 at most
 (W-L-(B-1))/2 times, with W-L<=p-7 (t=0), p-5 (t=1, t=2); this gives #1 >= (p+14+B)/2, (p+10+B)/2, (p+8+B)/2 for t=0,1,2
 (adding the n+ extra +1's), so u+ >= (p+2+B)/2 >= B (B<=p-4). Then l and B letters with c=+1 form an integer zero-sum of even
 size B+1 in [8,p-3]: forbidden. So every negative label is -1, -3 or -5.
(b) Give each l in A- the weight x(l)=1+|c_l| in {2,4,6}; a subset S of A- with x(S) in [8,p+5] and w(S):=sum_S |c_l| <= u+
 yields the integer zero-sum S plus w(S) letters c=+1, of size x(S): forbidden. Suppose x(A-)>=8. If some S has x(S)=8, then
 w(S)=8-|S|<=7<=u+ (u+>=(p+5)/2>=8): forbidden. Otherwise the weight multiset has no sub-multiset of sum 8: it contains no
 two 4's, no 2 together with a 6, no 4 with two 2's, no four 2's, so (as x(A-)>=8) it contains a 6 and no 2, and at most one 4.
 If it contains a 6 and a 4: S={-5,-3}, x(S)=10, w(S)=8<=u+: forbidden. Otherwise it contains two 6's: S={-5,-5}, both
 a-labels 5 in P0; the count of (a) with two a-labels 5 gives #1 >= (p+21)/2, (p+17)/2, (p+15)/2 (t=0,1,2), so
 u+ >= (p+9)/2 >= 10 = w(S), and x(S)=12<=p+5: forbidden. Hence x(A-)<=6, which leaves the seven listed sets. []

## 3. Lemma FULL: fullness of m=4 patterns [NEW]

LEMMA FULL. (a) If p>=13, every set Q of runs with m(Q)=4 is full.
(b) If p=11 and Q has m(Q)=4 and X^(Q) contains letters of both signs, Q is full.
(c) X^(Q) has letters of only one sign iff letters(Q)=A- or letters(Q^c)=A- (letters(Q) := the set of letters in runs of Q).
(d) If p=11 and (H11) holds, every Q with m(Q)=4 is full.
Proof. (a) The window is [0,R]; by Lemma SS every even v in [-nu(Q),Pi(Q)] is a signed sum with |J| even and 0<=|J|<=R.
(b) Here R=16, the window is [0,14], u+>=8, and every |c_l|<=7 (|b|<=p-4=7; negative labels by Lemma N3). Let v be even in
 [-nu(Q),Pi(Q)] and J a representation (Lemma SS) with |J| minimal. No nonempty sub-multiset of J has sum 0 (removing it would
 give a smaller representation). If |J|>=15, J misses at most one letter, so J contains at least 7 letters with c=+1, whose
 values in X^(Q) are +-1; they have one common sign, say +1 (else a pair +1,-1). A letter of J of value -c (c<=7) together
 with c of these would sum to 0; so every letter of J is positive in X^(Q). As |J| is even (v even) and >=15, |J|=16: all
 letters are positive in X^(Q), contrary to the hypothesis (the case of common sign -1 is symmetric). So |J|<=14.
(c) X^(Q) is all positive iff every letter in runs of Q has c<0 and every other letter has c>0, i.e. letters(Q)=A-; all
 negative iff letters(Q^c)=A-.
(d) letters(Q)=A- forces every run of Q to contain no letter with c>0 and every run with a letter c<0 to lie in Q. Under
 (H11), a run with letters of both signs would have to lie in Q and outside Q; and Q has at least 4 runs, all without
 positive letters, which needs at least four such runs. The same holds for Q^c (m(Q^c)=4). By (c) and (b) Q is full. []

## 4. Lemma F3: the lift framework on all m=4 patterns [NEW at kappa=3]

Assume (ALL4): every set Q of runs with m(Q)=4 is full. By Lemma FULL, (ALL4) holds for every p>=13, and for p=11 under (H11).
Let F4 be the family of sets Q with m(Q)=4. N=p+1>=12.
(F1) Every member is full, so B*<=2p-2 (Lemma U), Lemma C applies to a member whose complement is a member, and Lemma A applies
 to two disjoint members with member union (its inequality is Lemma N3).
(F2) Increments. If Q and Q u {i} (i not in Q) are in F4, d:=U'(Q u {i})-U'(Q) satisfies d=h_i (mod p), d=sigma({i}) (mod 2)
 and |d|<=(-1-nu0)-(Pi0+1-2p)=2p-2-B*<=p-7. Two such increments for the same i are congruent mod 2p and differ by at most
 2p-14, hence are equal. For every run i such a pair exists: Q_i={i+1,i+3,i+5,i+7} has pairwise cyclic distances >=2
 (N>=12), and Q_i u {i} has the intervals {i,i+1},{i+3},{i+5},{i+7} (i+7 and i are at cyclic distance >=5), so both have m=4.
 Define theta_i as this common value; theta_i=h_i (mod p) and theta_i=sigma({i}) (mod 2).
(F3) Connectivity: any two members of F4 are joined by a chain of members, consecutive ones differing in one run.
 (a) If Q has an interval [x,y] with x!=y, then Q\{y} still has m=4; repeating, Q is joined to an independent set
     (pairwise non-adjacent runs) with m=4, i.e. an independent quadruple.
 (b) For an independent quadruple v1,v2,v3,v4 in cyclic order let g_1,..,g_4>=1 be the numbers of runs strictly between
     v1,v2; v2,v3; v3,v4; v4,v1 (sum N-4>=8). If g_1>=2, the set {v1,v1+1,v2,v3,v4} has the intervals {v1,v1+1},{v2},{v3},{v4}
     (m=4) and {v1+1,v2,v3,v4} is an independent quadruple: "advancing v1" moves one unit from g_1 to g_4; "retreating v1"
     (needs g_4>=2) moves one unit back; likewise for v2,v3,v4. So a unit moves between cyclically adjacent gaps whenever the
     donor gap is >=2. If the gap vector differs from the target (2,2,2,N-10), some gap exceeds its target (hence is >=3);
     moving one unit from it along the cycle to a gap below its target (each intermediate gap is >=2 after receiving)
     decreases sum|g-target| by 2; so every independent quadruple is joined to one with gap vector (2,2,2,N-10) (N-10>=2).
     From such a quadruple, advancing v4, v3, v2, v1 in this order (each time the gap ahead is >=2) shifts all four runs by
     one position and restores the gap vector; repeating gives all rotations. Hence all independent quadruples are joined.
(F4) Put f(Q):=U'(Q)-sum_(i in Q) theta_i on F4. By (F2) f is unchanged along a chain step, so f is a constant f0 by (F3). The
 independent quadruples P1={0,3,6,9}, P2={1,4,7,10} are disjoint and P1 u P2 has the intervals {0,1},{3,4},{6,7},{9,10} (10 and
 0 are at cyclic distance N-10>=2), so m=4. Lemma A gives U'(P1 u P2)=U'(P1)+U'(P2), so f0=2f0, f0=0:
   U'(Q) = sum_(i in Q) theta_i for every Q in F4.
(F5) Q0={0,2,4,6} and its complement (intervals {1},{3},{5},{7,...,N-1}) both have m=4; Lemma C and (F4) give
   sum over all runs of theta_i = Pi0-nu0-2p = B*-2nu0-2p.                                                            []

## 5. Lemma RIG3: rigidity with tight data [NEW at kappa=3]

LEMMA RIG3. Under (ALL4): B*=R=p+5, so every |c_l|=1 and all rotation letters lie in {rho_1,rho_-1}; nu0=|A-| in {0,1,2,3};
every theta_i>=-1; and in each of the alternating sets S_ev={0,2,...,p-1}, S_od={1,3,...,p}:
   sum_(i in S) (theta_i+1) = 3-nu0.
Proof. Fix S (|S|=(p+1)/2>=6, its runs pairwise non-adjacent) and order its theta-values decreasingly. The top four form an
independent quadruple J* in F4, so theta_(1)+...+theta_(4)=U'(J*)<=-1-nu0 (Lemma U). Hence theta_(4)<0, so theta_(j)<=-1 for all
j>=4, and sum_S theta <= -1-nu0-(|S|-4). Adding over S_ev and S_od and using (F5):
   B*-2nu0-2p <= -2-2nu0-(p+1-8),   i.e.   B* <= p+5 = R.
As B*>=R, equality holds: every |c_l|=1; in each S, theta_(1)+...+theta_(4)=-1-nu0 and theta_(j)=-1 for j>=5; since
theta_(4)>=theta_(5)=-1 (|S|>=5), theta_(4)=-1, so theta_(1)+theta_(2)+theta_(3)=-nu0 and every theta in S is >=-1. Summing,
sum_S(theta+1) = (3-nu0)+0 = 3-nu0 >= 0, so nu0<=3; with |c|=1, Lemma N3 gives A- = nu0 letters -1. []

## 6. Proof of Theorem K3 and of Theorem K3-11 [NEW]

Assume (ALL4) (always for p>=13; under (H11) for p=11) and use Lemma RIG3. Every letter has value +1 or -1 (gamma=1), exactly
nu0 of them -1. For a run i let s_i:=sigma({i}) (number of +1 minus number of -1 letters of run i). Then theta_i=s_i=r_i (mod 2),
tau_i = theta_i - s_i (mod p) (as theta_i=h_i=tau_i+X_i and X_i=s_i), and for every proper P: T(P) = sum_P (theta_i - s_i) (mod p),
while X^(P) has exactly nu0 + sum_P s_i letters of value -1.
Case nu0=0. All rotation letters equal rho_gamma, gamma!=0: excluded by CJ''' (Sec. 1).
Now let nu0>=1.
(A) No run is empty: an empty run e has theta_e=0 (mod 2), theta_e>=-1 and theta_e+1<=3-nu0<=2, so theta_e=0; then
 h_e=tau_e=0 (mod p) (X_e=0), contradicting the empty-run rule (tau_e != 0).
(B) sum_i (r_i-1) = R-N = 4, so at least N-4 = p-3 runs are singletons; at most nu0 of them hold a -1; at most 2(3-nu0) runs have
 theta != -1. Call a singleton run whose letter is +1 and whose theta is -1 a "unit run"; there are at least
 (p-3-nu0)-(6-2nu0) = p-9+nu0 unit runs. For a unit run i: s_i=1, tau_i=-2 (mod p). Any three runs of the cycle contain two
 non-adjacent ones (N>=4).
Case nu0 in {2,3}. There are at least p-7>=4 unit runs; take two non-adjacent ones i,j. P={i,j} has m=2, window [4,p+5],
 T(P)=-4 (mod p), and X^(P) has nu0+2>=4 letters -1: four of them have sum -4 with n=4: an identity 2p-subword, contradiction.
Case nu0=1. In each alternating set the excess 3-nu0=2 is carried either by one run with theta=1 or by two runs with theta=0.
 (i) Some run e has theta_e=1 (r_e odd).
   - If e is not the singleton {-1}: e holds at most one -1, so s_e>=1 (s_e=r_e if e has no -1; r_e>=3 and s_e=r_e-2 if it has
     the -1). There are at least p-8>=3 unit runs, at most two of them adjacent to e; take a unit run i non-adjacent to e.
     P={e,i}: m=2, window [4,p+5], T(P)=(1-s_e)+(-2)=-1-s_e (mod p); X^(P) has 1+s_e+1=s_e+2 letters -1 and
     p+3-s_e>=1 letters +1 (s_e<=r_e<=5). All s_e+2 letters -1 and one +1 give the sum -1-s_e with n=s_e+3 in [4,8]:
     contradiction.
   - If e={-1}: s_e=-1, tau_e=2. The alternating set of e has no other run with theta!=-1, so at most 3 runs have theta!=-1,
     and there are at least (p-4)-2=p-6 unit runs, at least p-8>=3 of them non-adjacent to e; take two of these, i,j,
     non-adjacent to each other. P={e,i,j}: m=3, window [2,p+5], T(P)=2-2-2=-2 (mod p); X^(P) has exactly two letters -1 (the
     letters of i,j; the letter of e becomes +1); these two give sum -2 with n=2: contradiction.
 (ii) Otherwise each alternating set has two runs with theta=0 and all other runs have theta=-1. A theta=0 run has even length
     >=2 (by (A)); four of them and sum(r_i-1)=4 force each to have length 2 and all other runs to be singletons. The single
     -1 lies in at most one of them; let e be a theta=0 run with both letters +1: s_e=2, tau_e=-2. All other runs are
     singletons with theta=-1, so there are at least p-4 unit runs; take one, i, non-adjacent to e. P={e,i}: m=2,
     T(P)=-4 (mod p), X^(P) has 1+2+1=4 letters -1: n=4, sum -4: contradiction.
In every case u has an identity 2p-subword, contradicting that u is an avoider. Hence (ALL4) is impossible for an avoider:
for p>=13 this proves Theorem K3, and for p=11 it proves Theorem K3-11. []

## 7. Exact residual at p=11 and failed routes (not claimed)

Residual. p=11 (kappa_hat=3, R=16, N=12): avoiders whose NF u, in the frame of Sec. 1, has no run containing letters of both
signs and at least four runs containing no letter with c>0 (empty or purely negative runs; at most three runs are purely
negative, so at least one run is empty). Proved there: the frame of Sec. 1, Lemma N3, Lemma FULL(b),(c) (an m=4 pattern Q with two-signed X^(Q) is full,
and X^(Q) is single-signed exactly when letters(Q) or letters(Q^c) equals A-; conversely a single-signed X^(Q) is not full: if
every letter is positive in X^(Q), the even value v=B* needs all R=16 letters, beyond 14), and the final analysis of Sec. 6 once
the tight data of Lemma RIG3 are available. Missing claim (route target only):
the lift framework (theta for every run, additivity on a connected family of full patterns, a complement pair) together with
fullness of the top four runs of each alternating set, in the presence of the single-signed m=4 patterns of Lemma FULL(c).
Failed routes, kept. (R1) The K2 family "full (SR) window" is 4<=m<=(p-5)/2 here: empty at p=11, only m=4 at p=13; F3 uses
m=4 alone, which has the full window exactly for p>=13. (R2) At p=11 the m=4 window [0,14] misses the size R=16 needed for the
extreme values +-B* of a single-signed X^(Q); m=5,6 windows ([0,12],[0,10]) are worse. (R3) Route remark (not used): at p=11, m=3
patterns have window [2,16]; such a pattern is full iff X^(Q) has a nonempty integer zero-sum, which (u+>=8, |c|<=7) holds iff
X^(Q) is two-signed; sorting the top THREE of each alternating set would give B*<=p+3<R directly, but this needs the same
framework in the residual regime. (R4) Single-run
additivity (the K1 route) fails: a single run has window [6,p+5].

## 8. Scope and interface table

Claimed: Theorem K3 (every prime p>=13) and Theorem K3-11 (p=11 under (H11)), both at the full existential-NF/word antecedent.
Lemmas N3, FULL, F3, RIG3 are proved only at kappa_hat=3 in this frame. NOT claimed: p=11 without (H11); any other cell; reflection
rigidity; INV*; o_F assembly; full ordered Olson; any multiset-only statement outside the antecedent. The K2 lemmas are not used
as premises (their methods are re-proved at kappa=3).
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review; R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md.
| Input | Text, whole-file SHA256 | Scope; use |
|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | PL Theorem S accepted relative to its inputs |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | m(P) convention; theta only via full pairs (F2) |
| PL | PL Secs. 2-7 (lines 40-129); 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | SR, IF, D, SS, LT, U, A, C at kappa=3 |
| PL inputs | NF, GRX (if), S1(a), SC0, ZSTRUCT/FB/FB-E/Setting fact in (S'), pinned in PL Sec. 10 and LOWER-scope-addendum-1.md (0a68bf4204623d9cff7950175bda235fffefe120a3a203e478fc333fadd60442) | through Lemma IF |
| K2 verdict | R18/olson-K2-parent-verdict-v1.md; 5ca98c9a81b2e1607cf5f562bc276ad29ed81feb774857f1428e657293db04c7 (errata 081ca8a1..., 444ae57b...) | context/method only |
| CJ''' | R16/olson-cj-cjx-parent-verdict-v1.md lines 8-15; 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d | case nu0=0 only |
