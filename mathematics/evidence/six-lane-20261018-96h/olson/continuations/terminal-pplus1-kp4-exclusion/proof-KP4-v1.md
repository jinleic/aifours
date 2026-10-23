# KP4: terminal k=p+1, kappa^=p-4 excluded for every prime p>=11, and the pure-rotation case at p=7, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T16:27:44-0700. Status CANDIDATE_UNVERIFIED written word-level proofs.
Outcome O3 of the frozen scope KP4-EXCL-scope-v1.md (SHA256 ba13fdd35cb02b11b179c8a9087737cf35e55f9197ae4512dac62edf9cc51c4f,
frozen 2026-10-19T16:04:10-0700 before derivation, prior sketches disclosed there): KP4-EXCL is proved for every prime p>=11
and, at p=7, for avoiders whose rotation letters are all equal. KP4-EXCL at p=7 with a NON-constant rotation multiset is NOT
proved; obstruction-KP4-p7-v1.md states the exact residual. No partial statement replaces the target.
Inputs ONLY: accepted NF with its empty-run rule, GRX (if direction), RS(b), classical Cauchy-Davenport (CD). CT is not
needed. NOT premises: KP3-EXCL (candidate under review), UH-CONSTRAINTS (O3 partial), ROT-PP1/TOP, PP1-EXCL and KP2-EXCL
(accepted only at their own cells; no expansion shortcut), ASSEMBLY-P, RPdelta, REFL, RUNS/RGR-LONG, S(p), Lev, (S1), LS-family.
[RE-DERIVED] = same kind of argument as in my earlier candidates, re-proved here in full for this cell (not new progress);
[NEW] = new for this cell. No computation, enumeration by machine, model CLI, Lean, novelty/priority or human-review claim.

## 0. Statements

An avoider is a word of length 4p-2 over D_(2p) with no 2p letters in increasing original index order whose ordered product
is the identity. Full antecedent: SOME admissible normal form (accepted PM*/fusion process, existential reading of ZX overlay
2) of the avoider w has terminal k=p+1 and kappa^=p-4.

THEOREM KP4-A. Let p>=11 be prime. No avoider w has an admissible normal form with terminal k=p+1 and kappa^=p-4.
PROPOSITION KP4-7P. Let p=7. No avoider w has an admissible normal form with terminal k=8 and kappa^=3 in which all
twelve rotation letters are equal (equivalently all rotation letters of w are equal; NF preserves the rotation multiset).
LEMMA KP4-7N (necessary conditions at p=7, full antecedent): the conclusions of Sec. 7.2.
No hypothesis on o_F, reflection runs, nonempty runs or rotation pairs. H^=3 is distributed ARBITRARILY among the odd blocks.

Word form (proved directly; it implies the statements by NF): there is no avoider u of length 4p-2 with a cyclic
representation R_1 S_1 ... R_(p+1) S_(p+1), S_i=sigma_(y_i)^(l_i), all l_i odd, sum_i (l_i-1)/2=3, runs possibly empty, every
empty R_i separating DIFFERENT values y_(i-1), y_i -- for p>=11; and none with all rotation letters equal for p=7. Every
conclusion below keeps this full antecedent; no rotation multiset is excluded outside it.

## 1. Inputs, word form and the recomputed selection rule

Group law (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1), x,y in Z_p. Rotation letters are actual occurrences;
X is their multiset, X_i that of R_i, v_x(.) a multiplicity; run indices are cyclic mod N:=p+1.
NF: proof-ROT-few-E-v4.md 28-43 with the accepted overlays of Sec. 9: normalisation preserves avoidance, length and rotation
multiset; all blocks odd; empty R_i implies y_(i-1)!=y_i; H^=(F-k)/2, kappa^=p-1-H^, R=2p+2kappa^-k. With k=p+1,
kappa^=p-4: H^=3, F=p+7, R=3p-9. So NF turns the full antecedent into the word form.
GRX: notes-GRX-v1.md 7-20 (lowodd item 1/M2: every word, every cyclic constant-block representation, empty runs allowed, every
pattern z). With f_i=[z_i!=z_(i+1)], Phi=sum f_i, delta_GRX=#{i: l_i!=f_i mod 2}, C_max=F-delta_GRX, theta_i=y_(i-1)-y_i,
T(z)=sum_(z_i=+1) theta_i: if some even C with Phi<=C<=C_max and 0<=2p-C<=R admits 2p-C rotation occurrences whose signed sum
(an occurrence of value x in run i counted z_i x) is T(z), the word has an identity 2p-subword. Only this direction is used.
RS(b): proof-ROW-v1.md 16-27 with erratum-2 R5: for nonzero terms over prime Z_p and an integer K>=0,
|Sigma_(<=K)(S)|>=min(p,1+sum_x min(K,v_x(S))); in particular t nonzero terms have >=min(p,t+1) subset sums (0 included).
CD: |B+C|>=min(p,|B|+|C|-1) for nonempty B,C in Z_p (classical; the import inside RS(b)).

All l_i are odd, so delta_GRX=N-Phi and C_max=Phi+6. GRX's own statement admits EVERY even C in [Phi,Phi+6], whatever the
distribution of H^=3. With Phi=2m and n:=2p-C:
  (SR4) n even, max(0,2p-6-2m) <= n <= min(2p-2m,R)  and n letters of signed sum T(z) => identity 2p-subword.
For a set P of runs, z_P:=-1 on P, +1 elsewhere; for P proper nonempty, m(P) is its number of maximal cyclic intervals,
Phi(z_P)=2m(P), 1<=m(P)<=N/2. tau_i:=y_i-y_(i-1); T(z_P)=sum_(i in P) tau_i, and tau_i!=0 on an empty R_i. Writing n=2p-2j,
(SR4) admits exactly the j in {m,m+1,m+2,m+3} with 0<=2p-2j<=R. For p>=9 all of these lie in [0,R] (2p<=3p-9).
Changing the cyclic cut conjugates the selected product, so identity and original order are preserved.

## 2. Pairing, dominant class and the ordinary window [RE-DERIVED; valid for every prime p>=7]

Lemma M. A multiset of size N' with maximal multiplicity mu has q disjoint unequal-value pairs if 2q<=N' and q<=N'-mu.
Proof. Cap every multiplicity at q; the capped total is >=2q (if mu<=q it is N'; otherwise the top value keeps q and the
others keep >=q). Choose 2q occurrences inside the caps, list equal values consecutively x_1..x_(2q), pair x_i with x_(i+q);
an equal pair would need q+1 consecutive equal occurrences, against the cap. []

Lemma P. Every non-constant z has a signed value of multiplicity >=2p-7.
Proof. Let Phi=2m, n:=max(p-1,2p-6-2m), even. It satisfies SR4: n<=2p-2m (2m<=p+1), n<=max(p-1,2p-8)<=R. If every signed
multiplicity were <=2p-8=R-(p-1), Lemma M gives p-1 disjoint unequal pairs (2(p-1)<=R=3p-9 iff p>=7). The R-2(p-1)=p-7
unpaired letters contain the n-(p-1)<=max(0,p-7) fillers needed. One letter per pair plus the fillers is an actual
n-selection; swapping pair i adds d_i!=0. RS(b) with K=p-1 gives all p residues, so some selection has sum T(z). []

Lemma U. There is a NONZERO a such that every non-constant z has its dominant value in {a,-a}; >=2p-7 rotation letters have
value in {a,-a}.
Proof. 2(2p-7)>3p-9 for p>=7, so the dominant value is unique and the classes {s,-s} of different patterns coincide. If the
class were {0}: the N=p+1 block values give y_j=y_(j') (j!=j'); the proper arc between those blocks has m=1, T=0; n=2p-8 is
admissible and 2p-8 of the >=2p-7 zero letters sum to 0. []

Orient a so that A:=v_a(X)>=A':=v_(-a)(X); b:=R-A, delta:=R-A-A' (letters outside {a,-a}), delta<=p-2.
All-plus (m=0, n=2p-6 always admissible): p-3 letters a and p-3 letters -a sum to 0, so A'<=p-4. For p>=9 also n=2p is
admissible, so A<=2p-1.
For P, alpha(P), beta(P) count letters a, -a in the runs of P; d(P):=alpha(P)-beta(P), additive. Under z_P the signed-a letters
number A-d(P) and the signed-(-a) letters A'+d(P). Lemmas P/U give for every proper nonempty P:
  (W) d(P) <= lambda:=A-2p+7  or  d(P) >= Lambda:=2p-7-A',  with gap p-5+delta>0.

## 3. Multi-length windows (p>=11) [RE-DERIVED for this cell]

Lemma MW. Let z be non-constant, Phi=2m, s in {a,-a} its dominant signed value of multiplicity phi, W the w0=R-phi other
letters with omega_u:=s_u-s!=0 (s_u the signed value of u), G_s their subset sums (0 included). Let calK be the set of
K=R-n, n admissible for m, with w0<=K<=phi; q:=|calK|. If q>=1 then w0+q<=p-1.
Proof. For K in calK and any J contained in W omit J and K-|J| letters of value s (0<=K-|J|<=phi). The n=R-K remaining letters
have sum D-Ks-sum_J omega (D the total signed sum). So D-s calK-G_s is attained. The q values Ks are distinct (calK lies in an
integer interval of length <=6<p, s!=0); RS(b) gives |G_s|>=min(p,w0+1); CD gives >=min(p,w0+q) attained residues. If w0+q>=p,
T(z) is attained. []

The admissible K for m are p-9+2m+{0,2,4,6}. Lemma P gives phi>=2p-7, w0<=p-2.
- m=2: K in {p-5,p-3,p-1,p+1}, all <=2p-7<=phi (p>=8). w0=p-2 gives q=2 and w0=p-3 gives q=3: w0+q=p, excluded. Hence
  (MW2) phi>=2p-5 (w0<=p-4).
- m=3: K in {p-3,p-1,p+1,p+3}<=phi (p>=10). w0=p-2 gives q=3, w0+q=p+1; w0<=p-3 gives q=4 and w0<=p-5. Hence phi>=2p-4.
- m=4: K in {p-1,p+1,p+3,p+5}. If phi>=p+5, q=4 and w0<=p-5. Otherwise 2p-7<=phi<=p+4 forces p=11, phi=15, q=3 (K=10,12,14),
  w0+q=12>10. Hence phi>=2p-4.
  (MW34) for m in {3,4}: phi>=2p-4.
Strong windows: m(P)=2: d(P)<=A-2p+5 or d(P)>=2p-5-A'; m(P) in {3,4}: d(P)<=A-2p+4 or d(P)>=2p-4-A', the latter gap
p+1+delta. Complementing P swaps low and high (d(P^c)=A-A'-d(P)).

## 4. Super-heavy run, light sets, empty runs and strong bounds (p>=11) [RE-DERIVED]

Index the runs 0..N-1 (N>=12). From P0={0,2,4,6} to its complement there is a path of single-run toggles, all with m=4: add
N-1,N-2,...,8 (extending the interval of 0 backwards); remove 0; add 1, remove 2; add 3, remove 4; add 5, remove 6; add 7.
Every intermediate set has the four intervals [x,N-1]u{0} or [8,N-1] (or finally [7,N-1]) and three singletons/pairs among
1..6; 7 separates 6 from 8 until the last step, and 0,1 separate N-1 from 2. The end is {1,3,5}u[7,N-1]=P0^c.
Traverse from the low endpoint (strong m=4 split) to the high one. Some step crosses the gap p+1+delta. Removing a run i would
need -d_i>=p+1+delta, impossible as beta_i<=A'<=p-4. So a run h is added with
  (H) d_h>=p+1+delta, alpha_h>=d_h, R_h nonempty.
Light sets: every nonempty P' avoiding h is ordinary-low. Otherwise alpha(P')>=Lambda and A>=alpha_h+alpha(P')>=
3p-6+delta-A', while A=3p-9-delta-A': 0>=3+2delta, impossible.
lambda>=0: otherwise all p runs i!=h have d_i<=-1, so A'>=p. With A<=2p-1:
  A=2p-8+c, c in {1,...,7}, b=p-1-c, lambda=c-1.
Let E be the set of empty runs, Q the set of nonempty runs outside h whose letters all equal a, N_B the number of runs outside
h holding a letter !=a (N_B<=b). Then p=|E|+|Q|+N_B gives |E|+|Q|>=c+1. If Q!=empty it avoids h, so |Q|<=d(Q)<=lambda=c-1.
Hence |E|>=2.
Strong bounds: a set P avoiding h is ordinary-low (d<=c-1), below the strong high thresholds 2p-5-A'>=p-1 and 2p-4-A'>=p.
  (L2) m(P)=2, h not in P => d(P)<=c-3;   (L34) m(P) in {3,4}, h not in P => d(P)<=c-4.
For P contained in E u Q, d(P)=alpha(P n Q)>=|P n Q|.

## 5. Actual subset sums and the exact length rule (p>=11)

Let B be the b letters !=a, omega(u):=(x_u-a)/(2a)!=0 (2a a unit), G the set of subset sums (0 included), G_(>=r) the sums over
subsets with >=r elements, M:=Z_p minus G. RS(b) (K=b) gives |G|>=b+1, so |M|<=c, and 0 is not in M.
For a pattern whose negative side consists of EMPTY runs only (m intervals; m=0 is all-plus), every rotation keeps its value.
Put t:=T/(2a). A selection of n=2p-2j letters is J contained in B plus n-|J| letters a, valid iff |J|<=n and n-|J|<=A; its
sum is 2a(-j+sum_J omega) mod p. Here n>=2p-12>=b for every j<=6 used, so the only restriction is |J|>=r:=n-A=8-c-2j.
  (F) r<=0 (i.e. 2j>=8-c): t+j is in M.   (N1) r=1: t+j is not in G_(>=1), hence t+j is in M or t+j=0.
Lengths: all-plus j in {0,1,2,3} (t=0); one empty run j in {1,...,4}; two empty runs j in {1,...,4} if adjacent and {2,...,5}
if not; three empty runs forming m intervals j in {m,...,m+3}. Free j: c=1: j>=4; c=2,3: j>=3; c=4,5: j>=2; c=6,7: j>=1.
(N1) occurs at (c,j)=(1,3),(3,2),(5,1),(7,0). Residues below are written by integers; an integer interval that would
contain a multiple of p puts 0 in M and is excluded; p>=11 keeps every other integer used (<=10) distinct and nonzero.

## 6. The cases c=1,...,7 [NEW at this cell]

c=1 (|M|<=1). One empty run: j=4 free gives t+4 in M; (N1) at j=3 gives t+3 in M or 0; t+3!=t+4, so t=-3, M={1}. Two empty
runs: j=4 is admissible for m=1,2 and free: -6+4=-2 in M={1}, impossible.
c=2 (|M|<=2). All-plus j=3: 3 in M. One empty: t+3,t+4 in M, t+3!=3 (t!=0), so t+4=3, t=-1, M={2,3}. Pair, j=3: 1 in M,
impossible.
c=3 (|M|<=3). All-plus: j=3 gives 3, (N1) j=2 gives 2 (2!=0). One empty: t+3,t+4 in M and t+2 in M or t+2=0. If t+2!=0,
{t+2,t+3,t+4} contains {2,3}, so t=-1; else t=-2. Either way M={1,2,3}. A pair at free j=3 (m=1,2) needs s+3 in {1,2,3}
with s in {-2,-3,-4}: s=-2, both t=-1.
Window step: S:=E u Q has |S|>=4 and d>=0 on S. Three pairwise non-adjacent runs of S would form a set with m=3 and d>=0>c-4,
against L34. So S has independence number <=2: it is four consecutive runs v1..v4 or two separated adjacent pairs. In the
first shape {v1,v3},{v2,v4} have m=2 and L2 gives d<=0 on each; in the second S itself has m=2. So Q is empty and E has
four runs. Three of them form one interval (first shape) or two (second shape); s=-3 and free j=3 put 0 in M.
c=4 (|M|<=4). All-plus j=2,3: {2,3} in M. One empty: {t+2,t+3,t+4} in M meets {2,3}, so t in {-2,-1,1}; t=-2 puts 0 in M.
t=-1 gives {1,2,3}, t=1 gives M={2,3,4,5}; both together need 5 elements. All t=1: a pair at j=4 gives 6 in M, impossible.
All t=-1: a pair at j=2 gives 0 in M.
c=5 (|M|<=5). All-plus j=2,3 and (N1) j=1: [1,3] in M. One empty: [t+2,t+4] in M and t+1 in M or 0. If t+1!=0, the
4-interval [t+1,t+4] avoids 0 and shares >=2 elements with [1,3], so it is [2,5] (t=1, M=[1,5]); otherwise t=-1. Pairs:
adjacent needs [s+2,s+4] in M, non-adjacent [s+2,s+5] (all free). (-1,-1): 0 in M; (1,1): 6 in M=[1,5]. So |E|=2 with
t-values 1,-1. Then |Q|>=4 and |Q|<=4: four pure-a runs with one letter each. L2: d<=2; L34: d<=1. If Q has >=3 components,
one run from each of three is a set with m=3, d=3; if 2 components, P=Q has m=2, d=4; if 1 component q1q2q3q4, P={q1}u{q3,q4}
has m=2, d=3. All contradict.
c=6 (|M|<=6). All-plus j=1,2,3: [1,3]. One empty: [t+1,t+4] in M, so 1<=t<=p-5 and t<=2 (t>=3 gives 7 elements); t=2 forces
M=[1,6]. Pairs: adjacent [s+1,s+4], non-adjacent [s+2,s+5]. (1,1) non-adjacent needs 7; (1,2),(2,2) need 7 or more. So every
two empty runs are adjacent with t=1; a cycle of length >=12 has no triangle, so |E|=2. Then |Q|=5, one letter each. L2: d<=3;
L34: d<=2. >=3 components: three runs, m=3, d=3; 2 components: P=Q, d=5; one component q1..q5: {q1,q2}u{q4,q5}, m=2, d=4.
c=7 (|M|<=7). All-plus j=1,2,3: [1,3]. One empty: I_t=[t+1,t+4] in M, 1<=t<=p-5.
 Step 1: t<=3. If t>=4, M=[1,3]u[t+1,t+4] exactly (7 elements, disjoint), whose only four consecutive residues avoiding 0 are
 I_t (the gap [4,t] and 0 separate the two parts). Every empty has the same t; an adjacent pair needs [2t+1,2t+4]=I_t (t=0),
 a non-adjacent pair [2t+2,2t+5]=I_t (t=-1). Both impossible.
 Step 2: with t<=3 every empty gives M contains [1,t+4]. An adjacent pair adds [s+1,s+4] (contiguous with it), so s+4<=7,
 s<=3; a non-adjacent pair adds [s+2,s+5], so s+5<=7 (s+5=p would put 0 in M), s=2, both t=1.
 Step 3: |E|<=3, and |E|=3 means three consecutive runs with t=1. If |E|>=3, each empty is non-adjacent to another (then
 t=1) or is the middle of three consecutive empties whose ends are non-adjacent (t=1 each); that middle one then lies in a
 consecutive triple with s=2+t, [s+1,s+4] in M with [1,5] gives s<=3, t=1. So all t=1, M=[1,7]. A triple of empties with
 m=2 needs [5,8], with m=3 needs [6,9]: 8 in M, impossible. So every triple of empties is consecutive, forcing |E|=3.
 Step 4: |Q|>=8-|E|, |Q|<=6. |E|=2: |Q|=6 with one letter each; |E|=3: |Q|>=5, d(Q)>=5. L2: d<=4; L34: d<=3.
 |Q|=6: >=4 components give m=4, d>=4; 3 components P=Q, d=6; 2 components P=Q (m=2), d=6; one component q1..q6:
 {q1,q2}u{q4}u{q6}, m=3, d=4. |Q|=5 (three consecutive empties e1e2e3): >=4 components m=4, d>=4; 3 components d>=5; 2
 components (m=2) d>=5; one component q1..q5: {q1,q2}u{q4,q5}u{e2} has m=3 (e2's neighbours e1,e3 are not in it), d>=4.
Every c gives a contradiction. Theorem KP4-A is proved (word form, hence the NF statement). []

## 7. p=7

7.1 Parameters. p=7, N=8 runs, F=14, R=12. SR4: m=0: n in {8,10,12}; m=1: {6,8,10,12}; m=2: {4,6,8,10}; m=3: {2,4,6,8};
m=4: {0,2,4,6} (m=4 is exactly an alternating set of runs).
7.2 Lemma KP4-7N [RE-DERIVED at p=7]. (i) Lemmas P and U hold verbatim (pairing with q=6=R/2 pairs, n=6 for every m>=1, no
fillers): every non-constant pattern has a dominant value of multiplicity >=7 in a common class {a,-a}, a!=0. (ii) A'<=3
(n=8: four a and four -a). (iii) Window: d(P)<=A-7 or d(P)>=7-A' for every proper nonempty P. (iv) A>=7: otherwise some run
h is high (the d_i cannot all be <=-1 as their sum is A-A'>=0), a second high run would give A>=14-2A'>=8, and the other
seven runs are low with d_i<=-1, i.e. A'>=7. (v) MW: for m=2 and m=3 the dominant multiplicity is never 8 (calK={4,6,8},
q=3, w0=4: w0+q=7>6). These are necessary conditions, not an exclusion.

7.3 Proposition KP4-7P [NEW]. Suppose all twelve rotation letters equal x. By 7.2(i) x!=0 (the class is {x,-x}). Write
alpha(P) for the number of letters in the runs of P and t(P):=T(z_P)/(2x). Under z_P a selection of n=2nu letters with q of
them in P has sum 2x(nu-q); q ranges over the integers with 0<=q<=alpha, 0<=2nu-q<=12-alpha, q<=2nu, so nu-q fills the
integer interval [max(-nu,nu-alpha), min(nu,12-alpha-nu)]. Avoidance says t(P) misses all of them for nu in V_m=N_m/2.
Needed instances (each an interval of 7 consecutive integers, i.e. every residue mod 7, hence impossible):
- m=1, alpha=6: nu=3 gives [-3,3].
- m=2 or m=3, alpha=4: nu=2 gives [-2,2], nu=4 gives [0,4].  alpha=6: nu=3 gives [-3,3].  alpha=8: nu=2 gives [-2,2],
  nu=4 gives [-4,0].  (nu=2,3,4 lie in V_2={2,3,4,5} and in V_3={1,2,3,4}.)
So (R1) no arc holds exactly 6 letters; (R2) no set with m=2 holds 4, 6 or 8 letters; (R3) no set with m=3 does.
Empty runs: alpha=0, m=1: attained {3,4,5,6}, so t(e) in {1,2} (t(e)!=0). Two non-adjacent empties, m=2: attained {2,3,4,5},
so their t-sum, which lies in {2,3,4}, is attained: impossible. So |E|<=2, and |E|=2 means two adjacent empty runs.
Run sizes r_0..r_7 (sum 12), using R1-R3 (two runs at distance >=2 form an m=2 set, three pairwise non-adjacent runs an m=3
set; a run with 6 letters is an arc with 6):
- |E|=0 (all r>=1, so r<=5): profiles (5,1^7): arc of the 5-run and a neighbour has 6. (4,2,1^6): the 2-run is adjacent to the
  4-run (else 6), say runs 0 (4) and 1 (2); runs 1,3,5 are pairwise non-adjacent with 2+1+1=4. (3,3,1^6): the 3-runs are
  adjacent (else 6); a 1-run at distance 3 from the first gives 4. (3,2,2,1^5): the five runs at distance >=2 from the 3-run
  hold at most two 2-runs, so some 1-run gives 4. (2^4,1^4): two of the four 2-runs are non-adjacent: 4.
- |E|=1 (empty run 0; runs 1..7 induce a path; r<=5 since 6 is an arc): an m=2 set {0,j}, j in 2..6, forbids r_j=4.
  (2^5,1^2) and (3,2,2,2,1^3): two non-adjacent 2-runs give 4. (3,3,2,1^4): a 1-run non-adjacent to a 3-run gives 4.
  (4,2,2,1^4): the 4-run is at 1 or 7, adjacent to at most one 2-run; the other gives 6. (4,3,1^5): some 1-run is non-adjacent
  to the 3-run: 4. (5,2,1^5): a neighbouring 1-run gives an arc of 6, so the 5-run sits between run 0 and the 2-run, and the
  arc through runs 7,0,1 (or 0,1,2 after reflection) holds 1+0+5=6.
- |E|=2 (adjacent empties 0,1; runs 2..7 induce a path): every run j>=2 is non-adjacent to an empty, so r_j is not 4, 6 or 8;
  r_j=7 would leave five 1-runs, one non-adjacent to it (8). Profiles with parts in {1,2,3,5}: (2^6), (3,2^4,1): two
  non-adjacent 2-runs; (3,3,2,2,1,1): every 1-run must be adjacent to both 3-runs, possible for at most one 1-run;
  (3,3,3,1^3): two non-adjacent 3-runs; (5,2,2,1^3), (5,3,1^4): some 1-run non-adjacent to the 5-run gives 6.
Every profile is contradictory, proving Proposition KP4-7P. [] (Only arcs, m=2, m=3 sets and single/pair empty patterns
were used; no super-heavy run exists here, since every run has <=5 letters.)

## 8. Scope, re-derivation record and boundaries

- Re-derived (not new progress): SR form, Lemmas M/P/U, the ordinary window, Lemma MW, the m=4 toggle path, the super-heavy
  run, light sets, the empty-run count, the subset-sum interface (Secs. 1-5).
- New: the MW instances at m=2,3,4 for kappa^=p-4 (p>=11); the exhaustive c=1..7 analysis of Sec. 6 with exact free/(N1)
  lengths; the final run-position arguments; Lemma KP4-7N; Proposition KP4-7P with its attained-interval tables and profile
  enumeration.
- Exact restriction: KP4-EXCL is NOT proved at p=7 for non-constant rotation multisets (A<=11 after orientation);
  obstruction-KP4-p7-v1.md records the residual, route failures and the smallest missing claim.
- Not claimed: other cells, the upper or lower half, reflection rigidity, INV*, REFL, o_F assembly, ordered Olson, p=5,
  multiset-only non-existence outside the full NF antecedent, novelty/priority, Lean or human review.

## 9. Interface / scope / import table and pins

Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, LF lines, whole-file SHA256 | Accepted scope and exact use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16 lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3: avoidance and rotation multiset preserved, odd blocks, empty-run rule; terminal k=p+1, kappa^=p-4 gives H^=3 with arbitrary distribution |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | R16 lowodd item 1/M2: every representation and pattern, empty runs allowed; if direction; C in [Phi,Phi+6] |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | R18 CFXT item 4: integer K>=0, nonzero terms; K=p-1 (pairs), K=w0 (MW), K=b (Sec. 5) |
| CD | classical; proof-ROW-v1.md 4-5 | nonempty sets in prime Z_p; MW translates |
Verdicts (whole-file SHA256): R16/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only (not premises): terminal-pplus1-kp3-exclusion/proof-KP3-EXCL-v1.md
d72f277f5bdcc89526217d45c47aac973f668b26832eafe9735b8b8dfb9ff0e4. No cited input rests on a computer-assisted step.
