# P11R: the K3 p=11 residual - structure, near-rigidity of rotations (B* in {16,18}), and the exact obstruction, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-20T00:13:30-0700. Status: CANDIDATE_UNVERIFIED written proofs; outcome = LABELLED PARTIAL
plus EXACT OBSTRUCTION of the frozen target (P11R-scope-v1.md SHA256 14701fd9860d6b4288c4373f683cca6883273c7cd433322a5af81f0b61c9e00c,
frozen 23:55:39 before derivation; authority RUN/control/written-olson-kappa3-p11-residual-transition-v1.json SHA256
2aff97fc4770e0898df336669a50e58f1aa45c306a7f55e61b9ce45bdf252ed4). The residual branch is NOT shown empty. All case work by hand;
no script, assertion, enumeration or computation over scientific data. The K3 candidate (proof-K3-v1.md) is NOT a premise:
every step used from it is re-derived below. No novelty, priority, Lean or human-review claim; no other prime or kappa.

## 0. Setting and statements

p=11, terminal k=12, kappa_hat=3, words of length 42 over D_22. Full antecedent: an avoider w (no identity 22-subword in
increasing original index order) has SOME admissible NF u with terminal k=12 and kappa_hat=3; the H=7 extra reflection pairs lie
anywhere in the odd blocks; every empty NF run separates different reflection values; no o_F, nonempty-run, rotation-pair or
reflection-rigidity hypothesis. RESIDUAL: in the integer frame of Sec. 1, (H11) fails, i.e. (i) no run holds letters of both
label signs and (ii) at least four runs hold no letter with c>0.
THEOREM P11R [NEW]. Every avoider in the residual satisfies, in its frame:
 (a) [frame] Sec. 1 data; (b) [light arc] the T=0 arc P0 carries at most five letters, C0 at least eleven, and the light side is
 unique; (c) [runs] at least three runs with positive letters, at most three purely negative runs, between one and six empty runs;
 (d) [fullness] a pattern Q with m(Q) in {3,4} is full iff X^(Q) has letters of both signs;
 (e) [near-rigidity] B*:=sum|c_l| is 16 or 18. If B*=16, every rotation letter is rho_gamma or rho_-gamma, and the number nu0 of
 letters rho_-gamma is 1, 2 or 3. If B*=18, exactly one letter is rho_3gamma, every other letter is rho_gamma or rho_-gamma, and at
 most one letter is rho_-gamma.
 (f) [sorting failure] for every alternating set S and every ordering of S, if the first three and the first four runs both give
 single-signed patterns, then the configuration is (alpha) or (beta) of Sec. 7.
EXACT OBSTRUCTION (not proved): the residual configurations satisfying (a)-(e); the missing claim is stated in Sec. 8.

## 1. The frame at p=11 [re-derived from the accepted interfaces of PL = proof-LOWER-v1.md, K1 verdict + LOWER parent erratum]

NF word u: 12 runs R_0..R_11 (indices mod 12), 16 rotation letters, 26 reflections in odd blocks S_i; tau_i=y_i-y_(i-1),
T(P)=sum_P tau_i; m(P) = half the number of sign transitions of the pattern z_P (= number of maximal cyclic intervals for proper
nonempty P); X^(P) = letter values with the letters of runs of P negated.
(SR) [PL Sec. 2] For proper nonempty P, T(P) is not a sum of n letters of X^(P) for even n in [max(0,8-2m),min(16,22-2m)]; for
P empty the target is 0 and n ranges over [8,16]. Windows: m=1: [6,16]; m=2: [4,16]; m=3: [2,16]; m=4: [0,14]; m=5: [0,12];
m=6: [0,10].
T=0 arcs: the 12 block values lie in Z_11, so y_c=y_c' for some c!=c'; the arc P0 of runs c+1,...,c' and its complementary arc C0
have T=0.
[PL Lemma IF] The sequence Y of elements (1,x) of C_22 over the letters x of X^(P0) has no zero-sum of length in [6,16]
((SR) at P0, m=1), hence none in [6,22] (|Y|=16); accepted S1(a) at kappa'=2 bounds its zero-sums by 4: a longest zero-sum has
length 2t, t in {0,1,2}. SC0 on the zero-sum-free rest (length L=16-2t>=12) gives g=(1,gamma), gamma!=0, odd labels
a_1..a_L>=1, W=sum a_i<22. For t>=1 the setting (S') holds with (k',kappa')=(10,2) (|Y|=22+4-10=16), and ZSTRUCT/FB give the
extra labels with balance sum s_j=n+ and W+n+<=21; n-=0 would force n+=0, and n-<=n+:
 t=0: 16 a-labels, W even <=20, #(a=1)>=(48-20)/2=14, every a<=20-15=5.
 t=1: 14 a-labels and extra labels +1,-1; W even <=20; #(a=1)>=11; every a<=7.
 t=2: 12 a-labels and extra labels +1,+1,-1,-1 or +1,+1,+1,-3; W even <=18; #(a=1)>=9; every a<=7.
 (Counting: W-L=sum(a_i-1)>=2(L-#(a=1)); a_max<=W-(L-1).) Hence #1 := #(labels b=+1) >= 11 and every |b|<=7.
[PL Lemma LT] min(o(P0),o(C0))<=3, o(Q) := #(letters of runs of Q with b=1). Since o(P0)+o(C0)=#1>=11, exactly one side is
light; call it P0 (swapping the arcs keeps b and negates gamma). After gamma -> 1: c_l=b_l on C0, c_l=-b_l on P0, original value
c_l (mod 11). u+ := #(c=+1) >= #1-o(P0) >= 8 (C0-letters with b=1). A- := {l : c_l<0}; nu0 := sum_(A-)|c|; Pi0 := sum of c>0;
B* := Pi0+nu0 >= 16 (16 odd labels, so B* is even); sigma(P) := sum of c over the letters of runs of P.
[PL Lemmas SS, U, A, C] as in PL Secs. 5 and 7 (signed sums of X^(P) fill [-nu(P),Pi(P)] with the parity of the number of
letters; a full P forces B*<=20 and U'(P) in [Pi0+1-22,-1-nu0] with U'(P)=sigma(P) (mod 2); Lemma A needs 2Pi0+3+nu0>22;
Lemma C for complements).
[CJ''', R16 cj-cjx verdict lines 8-15] all rotation letters equal to one non-identity rotation gives an identity 22-subword
(k=12, kappa=3, Delta=-3<=0, R=16>=8, 2kappa=6<=10, odd maximal blocks, genuine empty runs).

## 2. Negative letters at p=11 [re-derived; the K3 Lemma N3 specialised]

LEMMA N11. A- is one of {}, {-1}, {-1,-1}, {-1,-1,-1}, {-3}, {-3,-1}, {-5} (as label multisets); nu0<=5; and
2Pi0+3+nu0=2B*+3-nu0>=30>22.
Proof. An integer zero-sum of X (a set of letters whose labels sum to 0) of even size in [8,16] is forbidden by (SR) at P empty.
A letter with c=-B, B>=5, is a P0-letter with an a-label B (the extra labels are +1,-1,-3, and C0-letters have c=b).
(a) c=-7: then t in {1,2} and W-L<=6 forces every other a-label to be 1, so #1>=13 and u+>=10; the letter with seven letters
 c=+1 is a forbidden zero-sum of size 8. So negative labels are -1, -3, -5.
(b) Weights x(l)=1+|c_l| in {2,4,6}; a subset S of A- with x(S) in [8,16] and w(S)=sum_S|c|<=u+ gives the forbidden zero-sum S
 plus w(S) letters c=+1. If x(A-)>=8: a sub-multiset of weight sum 8 has w<=7<=u+; otherwise (no sub-sum 8) the weights contain a
 6, no 2 and at most one 4: {-5,-3} gives x=10, w=8<=u+; two -5's would be two a-labels 5 in P0 with W-L>=8>6: impossible.
 Hence x(A-)<=6, which leaves the listed multisets; nu0<=5 and B*>=16 give the inequality. []

## 3. Lemma ARC: the light arc carries at most five letters [NEW]

LEMMA ARC. Every letter of P0 with b>0 has c=-b<0, so it lies in A-; at most |A-|<=3 such letters exist. The letters with b<0
are the ZSTRUCT extra labels -1 or -3: none (t=0), one (t=1), at most two (t=2). Hence letters(P0) has at most 5 elements and
C0 at least 11; o(C0)>=8. The frame is determined by the choice of the T=0 arc (the light side is unique). []

## 4. Run classes in the residual [NEW]

Call a run positive (P-run) if it holds a letter with c>0, negative (N-run) if it is nonempty and all its letters have c<0, empty
otherwise; by (H11)(i) failing, a P-run holds only letters c>0. Let P, Nr, E be these sets, k_P=|P|, E=|E|.
(c1) |Nr|<=|A-|<=3. (c2) |Nr|+E>=4 (by (H11)(ii) failing), so E>=1. (c3) k_P>=3: all >=16-3=13 positive letters lie in P-runs,
and accepted Theorem S (S1) (PL Sec. 3, via accepted Theorem P) gives sum_i floor(r_i/2)<=5, so 13<=sum_P r_i<=k_P+2*5.
(c4) E<=6: sum over nonempty runs of (r_i-1) = 16-(12-E) = 4+E, and r-1<=2floor(r/2), so 4+E<=10.

## 5. Fullness at p=11 [NEW; specialises and completes the K3 Lemma FULL]

LEMMA FULL11. Let m(Q) in {3,4}.
(a) Q is full iff X^(Q) has letters of both signs ("two-signed").
(b) X^(Q) is single-signed iff letters(Q)=A- or letters(Q^c)=A- (letters(Q) := the set of letters in runs of Q).
(c) In the residual: Q is two-signed whenever Q and Q^c both contain a P-run ("P-split"); and, when nu0>=1, whenever all runs
 of Q are empty.
Proof. Every |c|<=7 (Sec. 1 and Lemma N11) and u+>=8.
Two-signed implies a nonempty integer zero-sum in X^(Q): the >=8 letters with c=+1 have values +-1 in X^(Q); if both signs
occur they give a pair +1,-1; otherwise all are, say, +1 and any negative value -c (c<=7) plus c of them sums to 0 (symmetric).
m=3, window [2,16]=[2,R]: by Lemma SS every even v in [-nu(Q),Pi(Q)] has a representation; v!=0 forces >=2 letters (odd labels,
even count); v=0 needs a NONEMPTY zero-sum. So Q is full iff X^(Q) has a nonempty integer zero-sum, iff (by the above, and since
a single-signed multiset has none) X^(Q) is two-signed.
m=4, window [0,14]: if X^(Q) is two-signed, take for an even v a representation J of minimal size; J contains no nonempty
zero-sum. If |J|>=15, J contains >=7 letters with c=+1, all of one sign in X^(Q) (else a pair +1,-1); any opposite value -c (c<=7)
with c of them would be a zero-sum; so all letters of J have one sign, |J| is even and >=15, hence |J|=16 and X^(Q) is
single-signed: contradiction. So |J|<=14 and Q is full. If X^(Q) is single-signed, say all positive, v=Pi(Q)=B* is even and its
only representation uses all 16 letters, beyond 14: Q is not full (symmetric for all negative).
(b) X^(Q) is all positive iff every letter in runs of Q has c<0 and every other letter has c>0, i.e. letters(Q)=A-; all
negative iff letters(Q^c)=A-.
(c) A P-run in Q gives a negative value and one in Q^c a positive value. If all runs of Q are empty, X^(Q)=X contains a
negative letter (nu0>=1) and positive ones. []

## 6. Lemma PAIR and near-rigidity [NEW]

LEMMA PAIR. In the residual there are disjoint sets P1, P2 of runs with m(P1)=m(P2)=m(P1 u P2)=3, all three P-split.
Proof. Take distinct P-runs a, b, c (c3) and index the runs so that c=0; let a', b' in {1,...,11} be the indices of a, b. Choose
g1<g2 in {1,...,11} with g1>=3, g2-g1>=3, g2<=9 and g1, g2 not in {a',b'}: if 3 is not in {a',b'} take g1=3 and g2 in
{6,7,8,9}\{a',b'}; if 3 is in {a',b'} but 4 is not, take g1=4 and g2 in {7,8,9}\{a',b'}; if {a',b'}={3,4}, take g1=5, g2=8.
The blocks B1=[1,g1-1], B2=[g1+1,g2-1], B3=[g2+1,11] have length >=2 and are pairwise non-adjacent (separated by g1, g2 and
by run 0), and they contain a and b. Split every block into two nonempty consecutive parts: between a and b if both lie in it;
otherwise anywhere. Let P1 consist of the part containing a (from a's block) and one part of each other block, chosen so that
b's part goes to P2; P2 is the rest of B1 u B2 u B3. Each of P1, P2 has one interval in each block, so m=3; P1 u P2 = B1 u B2 u
B3 has m=3; P1 contains a, P2 contains b, and c lies outside all three. []
THEOREM NR (near-rigidity). B* is 16 or 18. If B*=16: every |c_l|=1 and nu0=|A-| is 1, 2 or 3. If B*=18: exactly one letter
has |c|=3, it has c=+3, and nu0<=1 (A- is {} or {-1}).
Proof. P1, P2, P1 u P2 are full (Lemma FULL11). Lemma U: B*<=20 and every full P has Pi0+1-22 <= U'(P) <= -1-nu0, i.e.
U'(P) in [B*-nu0-21, -1-nu0]. If B*=20 this interval is the single value -1-nu0, and Lemma A (its inequality is Lemma N11)
gives U'(P1 u P2)=U'(P1)+U'(P2), i.e. -1-nu0=-2-2nu0: impossible. B* is even and >=16, so B* is 16 or 18.
If B*=18: Lemma A gives -3-nu0 <= U'(P1 u P2) = U'(P1)+U'(P2) <= -2-2nu0, so nu0<=1; then A- is {} or {-1}, and the single label
of absolute value 3 (B*-16=2 means exactly one |c|=3, all other |c|=1) is positive.
If B*=16: every |c|=1, so A- consists of nu0 letters -1 and nu0<=3 (Lemma N11). If nu0=0, all letters equal rho_gamma, excluded
by CJ''' (Sec. 1). []
Remark. For B*=16 the rotation half of rigidity holds in the residual (all rotation letters in one pair {rho_gamma,rho_-gamma}).

## 7. Where the K3 sorting can fail [NEW, combinatorial]

LEMMA BOTH. Let S be an alternating set ({0,2,...,10} or {1,3,...,11}) and s_1, ..., s_6 any ordering of S. Put J3={s_1,s_2,s_3},
J4=J3 u {s_4}. If X^(J3) and X^(J4) are both single-signed, then one of:
(alpha) letters(J3)=A- (J3 contains every N-run, no P-run) and s_4 is empty; if nu0=0 this says that s_1,...,s_4 are empty runs;
(beta) k_P=3, the three P-runs are s_1, s_2, s_3 (pairwise non-adjacent), s_4 is empty, B*=16, nu0=3, A- = three singleton runs -1,
 the P-runs have odd lengths summing to 13 (all letters +1), and the remaining six runs are empty.
Proof. By Lemma FULL11(b) each of J3, J4 has letter set A- (type A) or complement letter set A- (type B).
Type A for both: J4 has no P-run and letters(J4)=A-=letters(J3), so s_4 has no letters: empty.
Type B for both: J3 contains every P-run (so k_P=3 and P=J3) and no N-run; J4 contains no N-run either and s_4 is not a P-run, so
s_4 is empty. All >=13 positive letters lie in three runs; (S1) gives 5 >= sum_(P) floor(r/2) >= (13-3)/2, so the three lengths are
odd with sum exactly 13, every other run has length <=1, |A-|=16-13=3, hence A- = {-1,-1,-1} (Lemma N11), nu0=3 and B*=16 (Theorem
NR); the nine other runs carry three letters: three singleton -1 runs and six empty runs.
Mixed types: type A for J3 and type B for J4 would put all P-runs in {s_4} (k_P<=1); type B for J3 and type A for J4 would need J3
to contain P-runs while J4 contains none. Both impossible. []

## 8. Exact obstruction (not proved) and failed routes

Residual after this note. p=11, (H11) failing, and the near-rigid alternative of Theorem NR: either B*=16 with nu0 in {1,2,3}
(all rotation letters in {rho_gamma, rho_-gamma}), or B*=18 with exactly one letter rho_3gamma and at most one letter rho_-gamma;
plus Lemmas ARC and BOTH and the run structure of Sec. 4. No avoider in this regime is constructed or claimed.
Missing claim (route target, not shown necessary). A family M of full patterns with m in {3,4}, connected under single-run
toggles inside M, containing: a pair Q, Q u {i} for every run i; the sets P1, P2, P1 u P2 of Lemma PAIR; a set together with its
complement; and, for each alternating set S, the first three or the first four runs of S in decreasing theta-order. Given M, the
increments theta_i (unique by the bound |d|<=20-B*<=4<11), the additivity f=0 on M (Lemma A on PAIR), the total
sum theta = B*-2nu0-22 (Lemma C) and the K3 sorting give B*<=16 (or B*<=14 if a first-three set lies in M), and the final cases of
K3 Sec. 6 then apply at p=11 (their counts p-9+nu0>=3 unit runs, etc., hold at p=11). By Lemma FULL11(c) every P-split pattern is
full; connectivity of the P-split patterns (plausible by moving runs around two P-run anchors, k_P>=3) is NOT proved here, and by
Lemma BOTH the sorting can lose its first-three and first-four sets only in the configurations (alpha), (beta).
Failed routes, kept. (F1) Single empty runs: (SR) with window [6,16] only restricts tau_e to a few residues (e.g. all labels 1,
nu0=0 leaves tau_e in {2,4,7,9}); no contradiction. (F2) Window-only additivity: a chain decomposition into four full triples
(when it exists, e.g. the residue classes mod 4 if each is P-split) gives sum U' = B*-2nu0-22 <= -4-4nu0, i.e. B*<=18-2nu0, which
leaves (B*,nu0) in {(16,1),(18,0)}; no contradiction. (F3) Alternative frames: the light side is unique (Lemma ARC), so a word
with a single coincidence of block values has a single frame. (F4) The K3 Lemma F3 used ALL m=4 patterns; in the residual some
m=4 patterns are single-signed (e.g. letters(Q)=A-) and these are not full (Lemma FULL11(a)). (F5) Theorem P beyond (S1):
F+sum floor(r_i/2) <= 26+5 = 31 < 32.

## 9. Interface table

Accepted inputs (literal scopes): K1 verdict RUN/review/olson-LOWER-K1-parent-verdict-v1.md 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83
with parent erratum RUN/review/olson-LOWER-parent-erratum-v1.md 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377:
PL (proof-LOWER-v1.md 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d) Secs. 2-7 - SR, (S1) via accepted Theorem P,
IF (through NF, GRX if direction, S1(a), SC0, ZSTRUCT/FB/FB-E in (S')), D, SS, LT, U, A, C; CJ''' (R16/olson-cj-cjx-parent-verdict-v1.md
lines 8-15, 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d) for nu0=0 with B*=16 only.
Not premises: proof-K3-v1.md (35ea47b03ad4a2c57c5b1430dfd642d524a935ae0c152ad220d5bb388da4ab30) and its review freeze
(93b25a2fac58b7fdeb3bc037fad38de709f924861db8ab9c0e5a33ce67877edc); the K2 verdict (kappa_hat=2 only). RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h,
R16=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.
