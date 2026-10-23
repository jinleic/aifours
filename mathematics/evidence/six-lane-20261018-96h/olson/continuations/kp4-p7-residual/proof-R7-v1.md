# R7: at p=7 no avoider has an admissible NF with terminal k=8, kappa^=3 (all non-pure cases; pure case re-proved), v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T16:59:31-0700. Status: CANDIDATE_UNVERIFIED written word-level proof. All case
work is by hand in this file; every branch is closed explicitly. No script, assertion, enumeration or computation over
scientific data was run. Scope frozen BEFORE derivation: R7-scope-v1.md, SHA256
6310d69356c0ae85662dded3b3ff2d45d9ca3f8bf2ea42b0ffb01206092e8b39 (2026-10-19T16:40:24-0700), with its pre-freeze disclosure.
Inputs: accepted NF, GRX (if direction), RS(b), classical Cauchy-Davenport (CD). INPUT CHANGE (recorded): accepted UH-A, used
exactly once (Sec. 2.4) at its literal scope. Not premises: the pending KP4 packet (its Proposition KP4-7P is re-proved here
by a different route, Sec. 5.4), KP3, other UH items, PP1/KP2 endpoints, ASSEMBLY-P, RPdelta, REFL, RUNS/RGR-LONG, S(p), Lev,
(S1), LS-family, CT. Labels: [RE-DERIVED] = kind of argument already in my pending packets, re-proved here at p=7; [NEW] =
new here. No novelty, priority, Lean or human-review claim.

## 0. Statements

An avoider is a word of length 26 over D_14 with no 14 letters in increasing original index order whose ordered product is
the identity. Full antecedent: SOME admissible normal form (accepted PM*/fusion process, existential reading of ZX overlay 2)
of the avoider w has terminal k=8 and kappa^=3.
THEOREM R7 [NEW]. No avoider w has an admissible NF with terminal k=8 and kappa^=3 whose rotation letters are not all equal.
PROPOSITION R7-PURE [RE-DERIVED]. No avoider w has such an NF whose rotation letters are all equal.
COROLLARY. No avoider of length 26 over D_14 has an admissible NF with terminal k=8 and kappa^=3. (Combining this with the
pending, separately reviewed KP4 Theorem KP4-A for p>=11 is NOT claimed here.)
No hypothesis on o_F, reflection runs, nonempty runs or rotation pairs; the three extra reflection pairs (H^=3) may sit in
the odd blocks in any way. Every conclusion below keeps the full antecedent; no rotation multiset is excluded outside it.

## 1. Word form, selection rule and cycle facts

Group law (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1), x,y in Z_7. NF (proof-ROT-few-E-v4.md 28-43, accepted
overlays in Sec. 6): an admissible NF of an avoider is an avoider with the same length and rotation multiset; with k=8,
kappa^=3 it is a cyclic word R_0 S_0 R_1 S_1 ... R_7 S_7 (S_i between R_i and R_(i+1), indices mod 8), S_i=sigma_(y_i)^(l_i),
every l_i odd, sum_i (l_i-1)/2=H^=3, F=14, R=12, runs possibly empty, and every empty R_i has y_(i-1)!=y_i. We exclude every
such avoider u (word form); the statements follow.
GRX (notes-GRX-v1.md 7-20; lowodd item 1/M2): with f_i=[z_i!=z_(i+1)], Phi=sum f_i, delta_GRX=#{i: l_i!=f_i mod 2},
C_max=F-delta_GRX, theta_i=y_(i-1)-y_i, T(z)=sum_(z_i=+1) theta_i: if an even C with Phi<=C<=C_max and 0<=14-C<=12 admits
14-C rotation occurrences of signed sum T(z) (a letter of value x in run i counts z_i x), u has an identity 14-subword. All
l_i are odd, so delta_GRX=8-Phi, C_max=Phi+6, and with Phi=2m, n=14-C:
  (SR7) n even, max(0,8-2m) <= n <= min(14-2m,12): m=0: {8,10,12}; m=1: {6,8,10,12}; m=2: {4,6,8,10}; m=3: {2,4,6,8};
        m=4: {0,2,4,6}. Write n=2nu and V_m for the set of nu: V_0={4,5,6}, V_1={3,...,6}, V_2={2,...,5}, V_3={1,...,4}.
For a set P of runs, z_P:=-1 on P, +1 elsewhere; for P proper and nonempty m(P) is its number of maximal cyclic intervals and
Phi(z_P)=2m(P). tau_i:=y_i-y_(i-1); T(z_P)=sum_(i in P) tau_i (T=0 for P empty), and tau_i!=0 when R_i is empty. Changing
the cyclic cut conjugates the product, so original order and identity are preserved.
Cycle facts (C_8, vertices = runs): each run has exactly two neighbours; three runs always contain a non-adjacent pair; any five
runs contain three pairwise non-adjacent runs (their maximal blocks have sizes summing to 5, and the sum of the halves rounded
up is >=3); two distinct runs never have the same two neighbours (C_8 has no 4-cycle).

## 2. Dominant class, normalization and the window [RE-DERIVED at p=7]

2.1 Lemma M. A multiset of size N' with maximal multiplicity mu has q disjoint unequal-value pairs if 2q<=N' and q<=N'-mu.
Proof. Cap every multiplicity at q; the capped total is >=2q (if mu<=q it is N'; else the top value keeps q and the others
keep >=q). Choose 2q occurrences within the caps, list equal values consecutively x_1..x_(2q), pair x_i with x_(i+q); an
equal pair would need q+1 consecutive equal occurrences, against the cap. []
2.2 Lemma P7. Every non-constant z has a signed rotation value of multiplicity >=7.
Proof. n=6 is admissible for m=1,2,3,4 (SR7). If all signed multiplicities were <=6, Lemma M (N'=12, q=6) gives six
disjoint unequal pairs using all letters; one letter from each pair is a 6-selection, swapping in pair i adds d_i!=0, and
RS(b) with K=6 gives all 7 residues among the subset sums of the d_i, so some selection has sum T(z). []
2.3 Lemma U7. There is a NONZERO a such that every non-constant z has its dominant value in {a,-a}.
Proof. 2*7>12, so the dominant value of z is unique, and two different classes {s,-s} cannot both hold 7 letters. If the
class were {0}: two of the 8 block values agree, y_j=y_(j'); the proper arc between those blocks has m=1, T=0; n=6 is
admissible and six letters of value 0 sum to 0. []
Normalization. phi(v,e)=(v/a,e) is an automorphism of D_14 (phi((v,e)(v',e'))=((v+ev')/a,ee')=phi(v,e)phi(v',e')); applied
letterwise it preserves identity subwords, block constancy and parities, and the empty-run rule. Choose the sign of a so that
A:=#{rotation letters of value a}>=A':=#{value -a}, and assume a=1. delta:=12-A-A' counts the other letters.
For a set P of runs: alpha(P), beta(P) count the letters of value 1, resp. -1, in the runs of P; d(P):=alpha(P)-beta(P),
additive; d_i:=d({i}). Under z_P exactly A-d(P) letters have signed value 1 and A'+d(P) have signed value -1. Hence:
  (W7) every proper nonempty set P of runs has d(P) <= A-7 or d(P) >= 7-A', i.e. d(P) avoids the band [A-6, 6-A'].
All-plus with n=8: four 1's and four -1's sum to 0=T, so A'<=3.
2.4 Input change: UH-A. Main accepted UH-A (RUN/review/olson-UH-CONSTRAINTS-parent-verdict-v1.md, SHA256
7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3; mandatory errata v1-v3). Its antecedent is literally ours
(prime p=7, kappa=3 in [(p-1)/2, p-3]=[3,4], some admissible NF with terminal k=p+1, any distribution of H=e-1=3, empty-run
rule) and its dominant class and orientation are those of 2.3. It gives A>=2kappa+3=9. So b:=12-A is 0,1,2 or 3; b=0 is the
pure case (Sec. 5.4), and A'<=b.

## 3. Positive selections, the letters !=1 and the empty runs

Let B be the b letters of value !=1, with values beta_u; omega_u:=(beta_u-1)/2 in Z_7 (1/2=4), omega_u!=0; G is the set of
sums of omega over subsets J of B (0 included), G_(>=r) the sums over |J|>=r, M:=Z_7 minus G, omega_B:=sum over B. Inverting,
beta_u=1+2 omega_u: omega=1,4,5,6 give beta=3,2,4,-1.
Lemma S (empty negative side). Let P be a set of EMPTY runs (P=empty allowed, m=m(P), m=0 if P is empty), t:=T(z_P)/2. If
t-nu=sum_J omega for some nu in V_m and J in B with max(0,2nu-A)<=|J|<=2nu, then u has an identity 14-subword.
Proof. No letter lies in P, so every letter's signed value is its value. J plus 2nu-|J| letters of value 1 (possible since
0<=2nu-|J|<=A) has sum (2nu-|J|)+sum_J beta=2(nu+sum_J omega)=2t=T. SR7 and GRX. []
Here 2nu-A<=0 for nu<=4, 2*5-A=b-2, 2*6-A=b; and |J|<=2nu binds only for nu<=1.
3.1 Lemma B (all-plus: P empty, t=0, V_0={4,5,6}): 3 is in M; 2 is not in G_(>=b-2); omega_B!=1.
Classification [NEW]. b=1: G={0,omega}; omega not in {0,1,2,3}; so omega in {4,5,6}: B={2},{4} or {-1}.
b=2: omega_1,omega_2 not in {0,2,3} and omega_1+omega_2 not in {1,2,3}. Pairs from {1,4,5,6}: (1,1) sum 2, (4,4) 1, (4,5) 2,
(4,6) 3, (5,5) 3 are excluded; (1,4),(1,5),(1,6),(5,6),(6,6) remain: B={3,2},{3,4},{3,-1},{4,-1},{-1,-1}.
b=3: singles avoid {0,2,3}; pairs avoid {2,3} (3 not in G, 2 not in G_(>=1)); the total avoids {1,2,3}. Allowed pairs from
{1,4,5,6}: (1,4),(1,5),(1,6),(4,4),(5,6),(6,6) (excluded (1,1),(4,5),(4,6),(5,5)). Triples: with a 4 the others lie in {1,4}
and (1,1) is excluded: {4,4,4} (total 5) or {4,4,1} (total 2, excluded); without 4, at most one 1 and one 5: {1,5,6} (5),
{1,6,6} (6), {5,6,6} (3, excluded), {6,6,6} (4). So B={2,2,2},{3,4,-1},{3,-1,-1},{-1,-1,-1}.
Twelve non-pure configurations: C1 {-1}; C2 {2}; C3 {4}; C4 {3,2}; C5 {3,4}; C6 {3,-1}; C7 {4,-1}; C8 {-1,-1}; C9 {2,2,2};
C10 {3,4,-1}; C11 {3,-1,-1}; C12 {-1,-1,-1}. (A=12-b, A'=number of -1's, delta=b-A'.)
3.2 Lemma E (empty runs) [NEW]. Let E be the number of empty runs. One empty run e (m=1) has t_e:=tau_e/2!=0 and
  (E1) t_e-3 and t_e-4 are not in G, t_e-5 is not in G_(>=b-2), t_e-6!=omega_B.
Two empty runs with s:=t_e+t_e': if adjacent (m=1) the four conditions (E1) hold for s; if not adjacent (m=2):
  (E2) s-2, s-3, s-4 are not in G and s-5 is not in G_(>=b-2).
Three empty runs (m in {1,2,3}, nu=4 in V_m): their sum minus 4 is not in G. Per configuration:
- b=1, G={0,omega}, G_(>=-1)=G, omega_B=omega. (E1) excludes t in {3,4,5}u{omega+3,...,omega+6}u{0}.
  C2 (omega=4): t=6=-1 only; two empties have s=5, excluded by (E1) (5 in {3,4,5}) and by (E2) (s-2,...,s-5 = 3,2,1,0 and
  0 in G). So E<=1. C3 (omega=5): t=-1 only; s=5 is excluded the same way. E<=1.
  C1 (omega=6=-1): t in {1,-1}; s in {2,0,5}: adjacent pairs need s not in {2,3,4,5}, non-adjacent s not in {1,...,5}; so
  s=0, the two t-values are opposite, and three empties are impossible. E<=2.
- b=2, G_(>=0)=G, omega_B=omega_1+omega_2. (E1) needs three consecutive residues t-5,t-4,t-3 in M.
  C4: G={0,1,4,5}, M={2,3,6}: no three consecutive; E=0. C5: G={0,1,5,6}, M={2,3,4}: t-5=2 gives t=0; E=0.
  C6: G={0,1,6}, M={2,3,4,5}: t-5 in {2,3} gives t in {0,1}, so t=1 (t-6=2!=0=omega_B). Two empties, s=2: adjacent needs
  s-3=6 in M (no); non-adjacent needs s-2=0 not in G (no). E<=1.
  C7: G={0,4,5,6}, M={1,2,3}: t=6=-1 (t-6=0!=4). s=5: s-5=0 is in G in both cases. E<=1.
  C8: G={0,5,6}, M={1,2,3,4}: t in {6,0}, so t=-1 (t-6=0!=5). s=5: s-5=0 in G. E<=1.
- b=3, G_(>=b-2)=G_(>=1), omega_B: (E1) needs t-4, t-3 in M (consecutive), t-5 not in G_(>=1).
  C9: G={0,1,4,5} (sums of 4,4,4), M={2,3,6}: t=6, but t-5=1 lies in G_(>=1)={1,4,5}. E=0.
  C10: G=G_(>=1)u{0}={0,1,4,5,6} (sums of 1,5,6: 1,5,6,6,0,4,5), M={2,3}: t=6, t-5=1 in G_(>=1). E=0.
  C11: G={0,1,5,6} (sums of 1,6,6: 1,6,6,0,0,5,6), M={2,3,4}: t in {6,0}, t=6, t-5=1 in G_(>=1)={0,1,5,6}. E=0.
  C12: G={0,4,5,6} (sums of 6,6,6), G_(>=1)={4,5,6}, M={1,2,3}, omega_B=4: t in {5,6}={-2,-1} (t=5: t-5=0 not in G_(>=1),
  t-6=6!=4; t=6: t-5=1, t-6=0!=4). Pairs s in {3,4,5}: s=3,4 put 0 among s-3,s-4; s=5 passes (adjacent: 2,1, s-5=0 not in
  G_(>=1), s-6=6!=4; non-adjacent: 3,2,1 and 0). So any two empties have t=-1 each; three empties give sum 4 and 4-4=0 in G.
  E<=2.

## 4. Pair-case attained intervals (delta=0) [RE-DERIVED]

If every rotation letter is 1 or -1 (C1, C8, C12 and the pure case), let eps(P):=A'+d(P) be the number of letters of signed
value -1 under z_P. A selection of n=2nu letters with q of signed value -1 has sum 2(nu-q), and q takes every integer with
max(0,2nu-(12-eps))<=q<=min(2nu,eps); so nu-q fills the integer interval [max(-nu,nu-eps), min(nu,12-eps-nu)]. With
t(P):=T(z_P)/2, avoidance says t(P) is outside the union over nu in V_(m(P)). Needed instances:
- (FORB) m(P) in {2,3} and eps(P)=4: nu=2 gives [-2,2], nu=4 gives [0,4]; eps(P)=8: nu=2 gives [-2,2], nu=4 gives [-4,0].
  Each union is seven consecutive integers, i.e. every residue: impossible. (nu=2,4 lie in V_2 and in V_3.)
- Allow_1(3)={-2,-1}: for m=1, eps=3 the intervals are [0,3],[1,4],[2,4],[3,3] (nu=3,...,6), union [0,4].
- Allow_1(5)={-3}: eps=5, m=1: [-2,3],[-1,3],[0,2],[1,1], union [-2,3].
- Allow_2(5)={-3}: eps=5, m=2: [-2,2],[-2,3],[-1,3],[0,2] (nu=2,...,5), union [-2,3].
- Allow_2(7)={3}: eps=7, m=2: [-2,2],[-3,2],[-3,1],[-2,0], union [-3,2].

## 5. Elimination of every configuration

Zero-weight runs: a run with d_i=0 is empty, or holds as many -1's as 1's (at least one of each: "balanced"), or holds
letters !=+-1 only. P+ denotes the multiset of positive weights d_i>0; "a subset sum of P+" always comes from a proper
nonempty set of runs here (the zero and negative runs, or other positive runs, lie outside it), so (W7) applies to it.
Lists "k parts of n" below are complete lists of partitions; checking them is part of the proof.

5.1 Heavy run (C4, C5, C9, C10, C11) [RE-DERIVED]. Put lambda:=A-7, Lambda:=7-A'. In these cases
(A,A')=(10,0),(10,0),(9,0),(9,1),(9,2), so Lambda-lambda=14-A-A'>lambda and A<2 Lambda.
(a) Some single run h has d_h>=Lambda: otherwise every single run has d_i<=lambda (W7); the prefixes {0},...,{0,...,6} start
low and end with d=d(all)-d_7>=A-A'-lambda=Lambda; at the first high prefix the added run has d_t>=Lambda-lambda>lambda,
so it is not low, hence high: contradiction.
(b) Every nonempty set P' avoiding h has d(P')<=lambda: otherwise alpha(P')>=d(P')>=Lambda and alpha_h>=Lambda give A>=2Lambda.
(c) The nonempty runs outside h holding only 1's form a set Q with |Q|<=d(Q)<=lambda (if Q is nonempty); at most b runs hold
a letter !=1. So at least 7-b-lambda runs are empty: 7-2-3=2 (C4, C5) and 7-3-2=2 (C9, C10, C11). But E=0 there (3.2).

5.2 Band subset sums (C2, C3, C6, C7, C8) [NEW].
C2, C3 (A=11, A'=0, band [5,6], letters !=1: one deviant u). d_i=alpha_i. Zero runs: at most one empty run (E<=1) and the
run of u if it holds u only. So P+ has >=6 parts, total 11, and no subset sum in {5,6}. A part >=7 would leave >=5 parts
summing to <=4. So all parts are <=4 (5, 6 excluded). 6 parts of 11 with parts <=4: (4,3,1,1,1,1) 4+1; (4,2,2,1,1,1) 4+1;
(3,3,2,1,1,1) 3+2; (3,2,2,2,1,1) 3+2; (2,2,2,2,2,1) 2+2+1. 7 parts: (4,2,1^5) 4+1; (3,3,1^5) 3+1+1; (3,2,2,1^4) 3+2;
(2,2,2,2,1,1,1) 2+2+1. 8 parts: (4,1^7) 4+1; (3,2,1^6) 3+2; (2,2,2,1^5) 2+2+1. Each has a subset sum 5 or 6: contradiction.
C6, C7 (A=10, A'=1, band [4,5], one -1 letter in run g1, one deviant u; E<=1). d_(g1)=alpha_(g1)-1.
 (i) d_(g1)=-1: zero runs are at most the empty run and {u}; P+ has >=5 parts, total 10, and its subset sums avoid {4,5}
 and (adding g1) {5,6}, so avoid {4,5,6}. A part >=7 leaves >=4 parts summing to <=3; so parts <=3. 5 parts of 10 with
 parts <=3: (3,3,2,1,1) 3+1; (3,2,2,2,1) 2+2; (2,2,2,2,2) 2+2. 6 parts: (3,3,1^4) 3+1; (3,2,2,1,1,1) 3+1; (2,2,2,2,1,1) 2+2.
 7: (3,2,1^5) 3+1; (2,2,2,1^4) 2+2. 8: (3,1^7) 3+1; (2,2,1^6) 2+2. Contradiction.
 (ii) d_(g1)=0 (g1 holds the -1 and one 1): zero runs are g1, at most one empty run, {u}: P+ has >=5 parts, total 9, subset
 sums avoid {4,5}. A part >=6 leaves >=4 parts summing to <=3; so parts <=3. 5 parts of 9: (3,3,1,1,1) 3+1; (3,2,2,1,1) 3+1;
 (2,2,2,2,1) 2+2. 6: (3,2,1^4) 3+1; (2,2,2,1,1,1) 2+2. 7: (3,1^6) 3+1; (2,2,1^5) 2+2. 8: (2,1^7) 2+1+1. 9: (1^9) 1+1+1+1.
 (iii) d_(g1)>=1: zero runs are at most the empty run and {u}; P+ has >=6 parts, total 9, avoiding {4,5}: the 6- to 9-part
 lists of (ii) all fail. Contradiction in all cases.
C8 (A=10, A'=2, band {4}, two -1 letters; E<=1). Zero runs: <=1 empty run and balanced runs (each uses a -1).
 No negative run: zero runs <=3, P+ has >=5 parts, total 8, no subset sum 4; a part >=5 leaves >=4 parts summing to <=3, and
 4 is excluded, so parts <=3: 5 parts of 8: (3,2,1,1,1) 3+1; (2,2,2,1,1) 2+2. 6: (3,1^5) 3+1; (2,2,1^4) 2+2. 7: (2,1^6)
 2+1+1. 8: (1^8). All contain 4.
 One run with d=-1: balanced runs <=1, zero runs <=2, P+ has >=5 parts, total 9, avoiding {4,5}: the lists of C6 (ii) fail.
 One run with d=-2 (it holds both -1's and no 1): zero runs <=1, P+ has >=6 parts, total 10, avoiding {4,6}: a part >=5
 leaves >=5 parts summing to <=5, so (5,1^5), which has 1+1+1+1; otherwise parts <=3: (3,3,1^4) 3+1; (3,2,2,1,1,1) 3+1;
 (2,2,2,2,1,1) 2+2; 7 parts (3,2,1^5) 3+1, (2,2,2,1^4) 2+2; 8 parts (3,1^7) 3+1, (2,2,1^6) 2+2. Fail.
 Two runs with d=-1 (each the single letter -1): zero runs <=1, P+ has >=5 parts, total 10, avoiding {4,5,6}: the lists of
 C6 (i) fail. Every case is contradictory.

5.3 Pair cases C1 and C12 [NEW]. Here Sec. 4 applies.
C1 (A=11, A'=1, band {5}, one -1 letter in run g; E<=2 with opposite t-values).
 (i) d_g=-1 (g holds only the -1): zero runs are the empty runs; P+ has >=5 parts, total 11, avoiding {5} and (with g) {6}.
 A part >=8 leaves >=4 parts summing to <=3: impossible; a part 7 leaves >=4 parts summing to 4: (7,1,1,1,1), whose subset
 sums 0-4, 7-11 avoid 5,6. Otherwise parts <=4: 5 parts of 11: (4,4,1,1,1) 4+1; (4,3,2,1,1) 4+1; (4,2,2,2,1) 4+2;
 (3,3,3,1,1) 3+3; (3,3,2,2,1) 3+2; (3,2,2,2,2) 3+2; 6, 7, 8 parts: the lists of C2 fail. So P+=(7,1,1,1,1) and E=2.
 Let h7 be the 7-run. A non-adjacent empty run e would give the m=2 set {h7,e} with eps=1+7=8 (FORB); so the two empty runs are
 the two neighbours of h7. g and the four 1-runs fill the other five places; some 1-run x is not adjacent to g; then h7, g, x
 are pairwise non-adjacent, an m=3 set with d=7-1+1=7, eps=8 (FORB). Contradiction.
 (ii) d_g=0 (g holds the -1 and one 1): zero runs are g and the empty runs; P+ has >=5 parts, total 10, avoiding {5}. A part
 >=7 leaves >=4 parts summing to <=3; a part 6 leaves four 1's: (6,1,1,1,1) (sums 0-4, 6-10). Otherwise parts <=4: 5 parts
 of 10: (4,3,1,1,1) 4+1; (4,2,2,1,1) 4+1; (3,3,2,1,1) 3+2; (3,2,2,2,1) 3+2; (2,2,2,2,2) (all subset sums even: allowed);
 6 parts: (4,2,1^4) 4+1; (3,3,1^4) 3+1+1; (3,2,2,1,1,1) 3+2; (2,2,2,2,1,1) 2+2+1; 7: (4,1^6) 4+1; (3,2,1^5) 3+2;
 (2,2,2,1^4) 2+2+1; 8: (3,1^7) 3+1+1; (2,2,1^6) 2+2+1. So P+ is (6,1,1,1,1) or (2,2,2,2,2), and E=2.
 (6,1,1,1,1): a 1-run x not adjacent to the 6-run h6 exists (four 1-runs, two neighbours); {h6,x} has m=2, eps=1+7=8 (FORB).
 (2,2,2,2,2): each 2-run (m=1, eps=3) has t in Allow_1(3)={-2,-1}; two non-adjacent 2-runs (m=2, eps=5) have t-sum in
 Allow_2(5)={-3}, so their t-values are -1 and -2. Five runs contain three pairwise non-adjacent ones, whose t-values would be
 pairwise different elements of {-2,-1}: impossible.
 (iii) d_g>=1: zero runs are the empty runs; P+ has >=6 parts, total 10, avoiding {5}: a part >=6 leaves >=5 parts summing to
 <=4; the 6-, 7-, 8-part lists of (ii) fail. Contradiction.
C12 (A=9, A'=3, band {3}, three -1 letters; E<=2; total d=6). Let s_- be the sum of the negative weights (s_- in [-3,0]).
 (a) s_-=0: P+ has total 6 and no subset sum 3; zero runs = empty runs (<=2) + balanced runs (<=3), so |P+|>=3. 3 parts of
 6: (4,1,1), (3,2,1) [3], (2,2,2); >=4 parts: (3,1,1,1) [3], (2,2,1,1) [2+1], (2,1,1,1,1) [2+1], (1^6) [1+1+1]. So P+ is
 (4,1,1) or (2,2,2) with exactly 5 zero runs: E=2 and three balanced runs, each with exactly one -1 and one 1; the positive
 runs hold only 1's. (4,1,1): a 1-run x and a zero run z not adjacent to it (five zero runs, two neighbours): m=2, eps=3+1=4
 (FORB). (2,2,2): each 2-run has eps=5, t=-3 (Allow_1(5)); two non-adjacent 2-runs (three runs contain such a pair) have
 eps=3+4=7 and t-sum -6=1, not in Allow_2(7)={3}. Contradiction.
 (b) s_-=-1 (one run with d=-1): P+ has total 7 and its subset sums avoid {3,4}. Zero runs <=2+2 (balanced runs need the
 remaining -1's), so |P+|>=3. 3 parts of 7: (5,1,1) allowed; (4,2,1) [4]; (3,3,1) [3]; (3,2,2) [3]; >=4 parts: (4,1,1,1) [4];
 (3,2,1,1) [3]; (2,2,2,1) [2+2]; (3,1^4) [3]; (2,2,1,1,1) [2+1]; (2,1^5) [2+1]; (1^7) [1+1+1]. So P+=(5,1,1) with 4 zero runs:
 E=2, two balanced runs, and the negative run is the single letter -1. A 1-run x and a zero run not adjacent to it give an
 m=2 set with eps=4 (FORB).
 (c1) one run with d=-2 (it holds >=2 -1's): zero runs <=2+1, |P+|>=4, total 8, subset sums avoid {3,5}. 4 parts of 8:
 (5,1,1,1) [5]; (4,2,1,1) [4+1]; (4,3,1,0)-type excluded; (3,3,1,1) [3]; (3,2,2,1) [3]; (2,2,2,2) allowed; (4,4) etc. have <4
 parts; >=5 parts: (4,1^4) [4+1]; (3,2,1,1,1) [3]; (2,2,2,1,1) [2+1]; (3,1^5) [3]; (2,2,1^4) [2+1]; (2,1^6) [2+1]; (1^8)
 [1+1+1]. So P+=(2,2,2,2): E=2, one balanced run, and the negative run is {-1,-1}. Two non-adjacent 2-runs (four runs contain
 such a pair) have t=-3 each and eps=7: t-sum 1 is not in Allow_2(7). Contradiction.
 (c2) two runs with d=-1: zero runs <=2+1, |P+|>=3, total 8, subset sums avoid {3,4,5}. 3 parts of 8: (6,1,1) allowed;
 (5,2,1) [5]; (4,3,1) [4]; (4,2,2) [4]; (3,3,2) [3]; >=4 parts all contain 3, 4 or 5 [(5,1,1,1) 5; (4,2,1,1) 4; (3,3,1,1) 3;
 (3,2,2,1) 3; (2,2,2,2) 2+2; (4,1^4) 4; (3,2,1,1,1) 3; (2,2,2,1,1) 2+2; (3,1^5) 3; (2,2,1^4) 2+2; (2,1^6) 2+1; (1^8) 1+1+1].
 So P+=(6,1,1): E=2, one balanced run, the negative runs are two single -1's. Zero runs: three; each 1-run must be adjacent to
 all three (else an m=2 set with eps=4): impossible with two neighbours.
 (d1) one run with d=-3 (all three -1's, no 1): no balanced run, zero runs = empty runs <=2, |P+|>=5, total 9, subset sums
 avoid {3,6}: with >=5 parts there is a 1; a 2 would give 2+1, three 1's give 3; so parts are in {1,4,5,7,8,9} with <=2 ones,
 hence >=3 parts >=4 and total >=14: impossible.
 (d2) runs with d=-2 and d=-1: no balanced run, |P+|>=4, total 9, subset sums avoid {3,4,5,6}: a part >=7 leaves >=3 parts
 summing to <=2; otherwise parts are 1 or 2, and 1+2, 2+2, 1+1+1 are forbidden, so all parts equal 2 (total 9 is odd) or
 there are at most two 1's and no 2 (total <=2): impossible.
 (d3) three runs with d=-1 (each the single letter -1): |P+|>=3, total 9, subset sums avoid {3,4,5,6}: as in (d2) a part >=7
 leaves parts summing to <=2, so P+=(7,1,1); otherwise impossible. E=2. Each 1-run x must be adjacent to both empty runs
 (else {x,e} is an m=2 set with eps=4); two distinct runs cannot share the same two neighbours. Contradiction.
 This exhausts s_- in {0,-1,-2,-3}.

5.4 The pure case (b=0, A=12, A'=0, band {6}) [RE-DERIVED by a shorter route]. G={0}, so (E1) gives t_e in {1,2} for an empty
run; two non-adjacent empty runs have s in {2,3,4}, excluded by (E2) (s-2,...,s-5 must avoid 0); so E<=2. Zero runs are the
empty runs, P+ has >=6 parts, total 12, no subset sum 6. A part >=8 leaves >=5 parts summing to <=4; a part 7 leaves five 1's:
(7,1,1,1,1,1). Otherwise parts <=5: 6 parts of 12: (5,3,1^4) 5+1; (5,2,2,1,1,1) 5+1; (4,4,1^4) 4+1+1; (4,3,2,1,1,1) 4+2;
(4,2,2,2,1,1) 4+2; (3,3,3,1,1,1) 3+3; (3,3,2,2,1,1) 3+3; (3,2,2,2,2,1) 3+2+1; (2^6) 2+2+2. 7 parts: (5,2,1^5) 5+1;
(4,3,1^5) 4+1+1; (4,2,2,1^4) 4+2; (3,3,2,1^4) 3+3; (3,2,2,2,1,1,1) 3+2+1; (2,2,2,2,2,1,1) 2+2+2. 8 parts: (5,1^7) 5+1;
(4,2,1^6) 4+2; (3,3,1^6) 3+3; (3,2,2,1^5) 3+2+1; (2,2,2,2,1^4) 2+2+2. So P+=(7,1^5) and E=2; the 7-run and a 1-run not
adjacent to it form an m=2 set with eps=alpha=8 (FORB). Contradiction.

Every configuration is impossible: Theorem R7, Proposition R7-PURE and the Corollary are proved. []

## 6. Scope, labels and interface table

- [RE-DERIVED]: SR7, Lemmas M, P7, U7 and the window (W7); the pair-case interval formula; the heavy-run argument 5.1; the
  pure case (by a new shorter route than the pending KP4 Sec. 7.3). [NEW]: the B-classification, Lemma E per configuration,
  the band subset-sum eliminations 5.2, the pair-case profiles 5.3.
- Exactly one accepted input beyond NF/GRX/RS(b)/CD: UH-A (A>=9), recorded in 2.4. Without it the cases A in {7,8} would remain.
- Not claimed: anything outside this p=7 cell (KP4 for p>=11 is the separate pending packet); reflection rigidity, INV*, REFL,
  o_F assembly, ordered Olson for D_14 or other groups; multiset-only non-existence outside the full NF antecedent.
Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, LF lines, whole-file SHA256 | Accepted scope; use here |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16 lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3; avoidance and rotation multiset preserved, odd blocks, empty-run rule |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | R16 lowodd item 1/M2; if direction; C in [Phi,Phi+6] |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | R18 CFXT item 4; K=6 in Lemma P7 |
| CD | classical; proof-ROW-v1.md 4-5 | only inside RS(b) |
| UH-A | R18/olson-UH-CONSTRAINTS-parent-verdict-v1.md line 15; 7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3; errata v1 8f1ea491eb2ab8ab4d4f1006896cb9aad63d6c51e270acb190de7bdaf4074ee3, v2 ac2a7f26ef941366e70e939545bae07a5baea6564005af29e5c9185560aaaa50, v3 0dc678867d10f28abc2f1681b21805658318fa9fc3a4c379062152cc1aef813f | shared antecedent at verdict line 9; A>=2kappa+3=9 at p=7, kappa=3 |
Verdicts (whole-file SHA256): R16/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only (not premises): terminal-pplus1-kp4-exclusion/proof-KP4-v1.md a6308ea8e265869795028fcddbdfaaa5a01f0ec514b587da0a6c227af1efaacf
and obstruction-KP4-p7-v1.md cdac29f484dfd5de4587b2ada214c27c0018052ce8bf8a01df929c3c85ff0462. No cited input rests on a
computer-assisted step.
