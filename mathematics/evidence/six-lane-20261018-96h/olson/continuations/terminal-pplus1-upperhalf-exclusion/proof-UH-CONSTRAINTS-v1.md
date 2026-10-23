# Upper-half terminal k = p+1: new necessary constraints and restricted exclusions, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T13:44:36-0700. Status: CANDIDATE_UNVERIFIED written mathematics.
Frozen scope: UH-EXCL-scope-v1.md, sha256 6ff7fec519944d57c3162f45e1b19403b12a8bea19647634dc86ba20e03d15e9
(2026-10-19T13:08:38-0700; pre-freeze disclosure in that file). Outcome O3, NOT the whole-interval exclusion UH-EXCL.
This file proves necessary conditions and explicitly restricted exclusions; obstruction-UH-EXCL-v1.md records the remaining
word-level gap. No existence or non-existence outside the stated antecedents is asserted.

Accepted inputs: NF with its empty-run rule; GRX (if direction); RS(b) and classical Cauchy-Davenport (CD). CT is allowed but
not needed. No pending PP1-EXCL, KP2-EXCL, ROT-PP1/TOP, ROT-SING+, ONE-SHORT-LS or ASSEMBLY-P is a premise. No REFL, S(p), Lev,
(S1), RGR-LONG/RUNS, RPdelta or source theorem beyond the listed interfaces is used. No computation/enumeration/Lean/model CLI.
[RE-DERIVED] marks the M/P/U and ordinary-window arguments of pending proof-ROT-PP1-v2.md, re-proved here at this full range;
not new progress. [NEW] means a new candidate conclusion in this packet, not a novelty/priority claim.

## 0. Full antecedent and precise results

Throughout: p >= 7 is prime, (p-1)/2 <= kappa <= p-3, e := p-kappa (3 <= e <= (p+1)/2). A length-(4p-2) avoider means a word
with no identity product on 2p distinct letters selected in increasing original index order. Suppose an avoider w has SOME
admissible NF w^ with terminal k = p+1 and kappa^ = kappa. Write u := w^. All results below retain this FULL antecedent.
Equivalently for these arguments, u can be any avoider with a cyclic representation R_1 S_1 ... R_(p+1) S_(p+1), every block
S_i = sigma_(y_i)^(l_i) of odd length, sum_i (l_i-1)/2 = e-1, and every empty R_i between different y_(i-1), y_i. The extra
pairs may be distributed arbitrarily among the blocks. Then F = p+1+2(e-1), R = p-1+2kappa = 3p-1-2e. This word formulation
implies the NF formulation because NF preserves avoidance and the rotation multiset.

THEOREM UH-A [NEW; restricted exclusion over the WHOLE upper-half kappa interval]. There is a nonzero a such that the dominant
signed values of all non-constant run sign patterns lie in {a,-a} (Lemma U, re-proved below). Orient a so that
A := v_a(X) >= A' := v_(-a)(X), where X is the rotation multiset of u (= that of w). Then
  A >= 2kappa+3,   A <= 2p-1,   A' <= kappa,
  p-2e <= b := R-A <= p-4,   0 <= delta := R-A-A' <= p-2.
Thus NO avoider with the full antecedent has A <= 2kappa+2. This is a restriction on A, not an exclusion of any entire kappa
cell: the remaining A = 2kappa+c, 3 <= c <= 2e-1, are not eliminated here.

Other candidate necessary constraints:
- Lemma MW (Sec. 4): an explicit multi-length omitted-letter sumset test for every non-constant sign pattern.
- Proposition SH (Sec. 5): if 3e <= p+2, some run h satisfies alpha_h-beta_h >= p+1+delta; every set of runs avoiding h is low
  in the ordinary window; at least two runs are empty. This is structure, NOT an exclusion.
- Proposition L (Sec. 6): with the EXPLICIT pair premise delta = 0, low arcs have exact allowed intervals whose integer lifts
  add along a path of low arcs. No reflection-rigidity or nonempty-run premise is substituted.
- Corollary PH (Sec. 6): the restricted pure-rotation subcase A'=delta=0 with some run holding >= p rotations is impossible.
  No conclusion for the pure case with all run sizes < p is claimed.
- Lemma E (Sec. 7): exact subset-family exclusions for empty-negative-side patterns, with both occurrence bounds retained.
All statements are CANDIDATE_UNVERIFIED. Full UH-EXCL remains unproved; lower 1 <= kappa < (p-1)/2 is untouched.

## 1. Accepted interfaces, notation and recomputed selection range

(v,epsilon)(v',epsilon') = (v+epsilon v', epsilon epsilon'); rho_x=(x,+1), sigma_y=(y,-1), x,y in Z_p.
Multisets are of actual occurrences. v_x is multiplicity; Sigma_(<=K)(S) denotes sums of at most K terms (0 included).
(NF) proof-ROT-few-E-v4.md 28-43, with accepted overlays in Sec. 9: u avoids, same length/rotation multiset; all l_i odd;
     every empty run R_i has y_(i-1) != y_i; H^=(F-k)/2, kappa^=p-1-H^, R=2p+2kappa^-k. Indices are mod p+1.
(GRX) notes-GRX-v1.md 7-20, lowodd verdict item 1/M2: for every such cyclic representation (empty runs allowed) and z,
     f_i=[z_i != z_(i+1)], Phi=sum f_i (even), delta_GRX=#{i:l_i != f_i mod2}, C_max=F-delta_GRX,
     theta_i=y_(i-1)-y_i, T(z)=sum_(z_i=+1) theta_i. If Phi <= C <= C_max is even, 0 <= 2p-C <= R, and 2p-C actual rotations
     have signed value sum T(z), the word has an identity 2p-subword. Only this implication is used.
(RS(b)) proof-ROW-v1.md 16-27, with erratum R5: nonzero terms over Z_p, integer K>=0 imply
     |Sigma_(<=K)(S)| >= min(p,1+sum_x min(K,v_x(S))). In particular all subset sums of t nonzero terms have >=min(p,t+1) values.
(CD) Classical |B+C| >= min(p,|B|+|C|-1) for nonempty B,C in Z_p; this is also the classical import inside RS(b).

Since every l_i is odd, delta_GRX = p+1-Phi and C_max = Phi+2H = Phi+2e-2. Selecting f_i letters at a singleton minimum and
then adding pairs within the blocks realises EVERY even C from Phi through Phi+2e-2: each block contributes an independent
integer interval in steps 2. Neither the distribution of H nor nonemptiness of any run is used. Thus for Phi=2m:
  (SR) n even, max(0,2kappa+2-2m) <= n <= min(2p-2m,R).
Whenever n actual rotation letters have signed sum T(z), SR and GRX give an identity 2p-subword. Changing the cyclic cut
conjugates the selected product, preserving identity and the existence of a selection in original linear order.
For a set P of runs, z_P=-1 on P, +1 elsewhere; P is non-constant iff neither empty nor all runs. If non-constant, m(P) is
its number of maximal cyclic intervals and Phi=2m(P), 1<=m(P)<=(p+1)/2. Put tau_i=y_i-y_(i-1); then
  T(z_P)=sum_(i in P) tau_i,  and tau_i!=0 for an empty R_i.
Single arcs have m=1; two distinct empty runs have m=1 if adjacent, otherwise m=2. The all-plus pattern has m=0, T=0 and
forbids rotation zero-sums at all even lengths in [2kappa+2,min(2p,R)]. This is (ZP_kappa) for Y(x)=(1,x) in C_2 x C_p.
The symbol delta below counts deviant rotations, NEVER delta_GRX.

## 2. Pairing and the ordinary window [RE-DERIVED]

Lemma M. A multiset of size N, maximum multiplicity mu, has q disjoint unequal-value pairs if 2q<=N and q<=N-mu.
Proof. The total after capping every multiplicity at q is >=2q: if mu<=q it is N; otherwise the top value keeps q and the
others keep at least q (one of them keeps q, or their uncapped total N-mu>=q is kept). Choose 2q occurrences within these
caps and list equal values consecutively as x_1,...,x_(2q). Pair x_i with x_(i+q). Equal values in such a pair would occupy
q+1 consecutive positions, against the cap. []

Lemma P. Every non-constant z has a signed value of multiplicity >=2kappa+1.
Proof. Let Phi=2m and n=max(p-1,2kappa+2-2m). Both alternatives are even. Since 2kappa>=p-1 and m>=1, n<=2kappa; since
2m<=p+1 and kappa<=p-1, n<=2p-2m; also n<=R and n meets SR. If the maximum signed multiplicity were <=2kappa=R-(p-1),
Lemma M gives p-1 disjoint unequal-signed-value pairs (2(p-1)<=R is exactly kappa>=(p-1)/2). Their complement has
R-2(p-1)=2kappa-p+1 letters, enough to fix n-(p-1) fillers, since 0<=n-p+1<=2kappa-p+1. Choose one letter per pair and
these disjoint fillers. Swapping the i-th pair adds a nonzero difference d_i; RS(b), K=p-1, says its p-1 differences have
all p subset-sum residues. One actual selection of n letters therefore has sum T(z): contradiction. []

Lemma U. All non-constant z have their dominant value in a common class {a,-a}, with a!=0; at least 2kappa+1 rotation
letters have value in this class, so delta<=p-2.
Proof. 2(2kappa+1)>R, since 2kappa>p-3. The dominant value is unique; the class {s(z),-s(z)} contains all >=2kappa+1 letters
of that signed value. Different classes are disjoint and cannot both have this many letters. If the common class were {0},
pigeonhole on the p+1 block values in Z_p gives y_j=y_(j') with j!=j'. The proper arc between these blocks has m=1,T=0;
n=2kappa is admissible, and 2kappa of the >=2kappa+1 zero-valued rotations give an identity: contradiction. []

Orient a so A>=A', and set b=R-A=A'+delta. The all-plus pattern gives A'<=kappa: otherwise kappa+1 letters each of a,-a
are a length-(2kappa+2) zero-sum. Also A<=2p-1: if 2p letters a existed, their zero-sum is admissible; if R<2p this is
already a count bound. Consequently A>=kappa+1 and b>=R-(2p-1)=p-2e.
For a set P define alpha(P), beta(P) as its counts of a,-a and d(P)=alpha(P)-beta(P); use alpha_i,beta_i,d_i for one run.
Signed counts under z_P are phi_a=A-d(P), phi_(-a)=A'+d(P). Lemmas P/U give for EVERY non-constant P:
  (W) d(P)<=lambda:=A-2kappa-1=p-2-b  OR  d(P)>=Lambda:=2kappa+1-A'.
Here d(all runs)=A-A'=lambda+Lambda,
  g:=Lambda-lambda=4kappa+2-A-A'=p-2e+3+delta>=2+delta,  and lambda<=2e-2.

Lemma H (tracked sufficient condition). If b+delta>=2e-4, a run h is high: d_h>=Lambda; alpha_h>=Lambda>=kappa+1.
Proof. This condition is exactly g>lambda. If all single runs were low, prefixes P_t={1,...,t} have d(P_1)<=lambda and
 d(P_p)=A-A'-d_(p+1)>=Lambda. At the first crossing from <=lambda to >=Lambda, a single increment d_t>=g>lambda would be
high, contradiction. Prefixes and singletons are proper nonempty sets, so every W invocation is valid. []

Lemma D (tracked bound on two high sets). If P_1,P_2 are disjoint high sets, then
  A>=2Lambda, equivalently A'>=p-2e+3+delta = 2kappa+3-p+delta.
Proof. alpha(P_j)>=d(P_j)>=Lambda; add and substitute A=p-1+2kappa-delta-A'. []
Thus delta>=e-2 excludes two high sets (as A'<=kappa=p-e). More exactly A<2Lambda excludes them. If h is high and no high
set avoids h, every nonempty set of runs avoiding h is low. Then lambda>=0: otherwise all p other single runs require
beta_i>=1 and A'>=p>kappa. Let P+={i!=h:d_i>=1}. Its cardinality <=d(P+)<=lambda when nonempty. Every nonempty run besides h
either uses a non-a letter (at most b such runs) or is in P+. So there are at most b+lambda=p-2 nonempty runs besides h:
AT LEAST TWO RUNS ARE EMPTY. These are conditional conclusions, not an unconditional heavy/light hypothesis.

## 3. Theorem UH-A: exclusion of A <= 2kappa+2 [NEW]

Suppose b>=p-3, equivalently A<=2kappa+2. Since 2e<=p+1, b+delta>=p-3>2e-5; Lemma H gives a high run h.
If b>=p-1, then A<=2kappa<2Lambda (Lambda>=kappa+1); no high set avoids h. But lambda=p-2-b<=-1, contradicting the light-set
conclusion of Sec. 2. Hence b<=p-2.
If b=p-2, A=2kappa+1<2Lambda, so light sets hold and at least two runs are empty.
If b=p-3, A=2kappa+2: if light sets hold there are again two empty runs. Otherwise take a high P_2 avoiding h. Equality is
forced in A>=alpha_h+alpha(P_2)>=2Lambda>=2kappa+2=A: A'=kappa, alpha_h=alpha(P_2)=kappa+1, beta_h=beta(P_2)=0, no a-letter
lies outside {h} union P_2, and delta=b-A'=e-3.
All -a letters lie outside {h} union P_2. For any set S of those outside runs, {h} union S is proper (it misses nonempty P_2),
and has d=kappa+1-beta(S). W with lambda=1,Lambda=kappa+1 forces beta(S)=0 or beta(S)>=kappa. Since A'=kappa, all -a letters
are in ONE outside run. Let Q be the set of a-containing runs; it is proper since that -a run is outside Q. For each subset
Q' of Q, d(Q')=alpha(Q') (there are no -a letters in Q), so any nonempty Q' has alpha(Q')<=1 or >=kappa+1. Each positive alpha_i
is therefore 1 or >=kappa+1; at most one can be 1 (two give sum 2<=kappa), and at most two can be >=kappa+1. Two large runs
already exhaust A, leaving no small one; thus at most TWO runs contain a. Nonempty runs number at most 2+1+delta=e, giving
at least p+1-e=kappa+1>=2 empty runs. This settles the two-high-set branch without assuming it absent.

It remains to rule out two empty runs for b=p-2,p-3. Let B be the b non-a letters and omega(u)=x_u-a!=0. Let G be all subset
sums of these weights, G_nonempty the nonempty subset sums, M=Z_p minus G. RS(b), K=b, gives |G|>=min(p,b+1), so
|M|<=p-1-b and 0 is not in M. For all-plus and for negative sides consisting solely of empty runs, EVERY rotation keeps its
value. Selecting J contained in B and n-|J| letters a gives sum na+sum_J omega, provided |J|<=n and n-|J|<=A. In particular
if b<=n<=A, every J is allowed, and avoidance forces T-na in M. All lengths below satisfy |J|<=b<=p-2<=2kappa.
- b=p-2, A=2kappa+1, |M|<=1. An empty run i, with n=2kappa free, forces tau_i+2ea in M. With n=2kappa+2=A+1 admissible for
  m=1 (e>=3), every NONEMPTY J is allowed, so tau_i+(2e-2)a is not in G_nonempty. It differs by 2a from the unique element
  tau_i+2ea of M, hence belongs to G but not G_nonempty; it must be 0. Thus tau_i=-(2e-2)a and M={2a} for every empty run.
  For two empty runs i,l, T=-(4e-4)a. The length n=2kappa is admissible for m=1 and m=2, free, and forces
  T-na=(4-2e)a in M={2a}. This says 2(e-1)=0 mod p, impossible as 4<=2e-2<=p-1.
- b=p-3, A=2kappa+2, |M|<=2. All-plus with free n=2kappa+2 forces v:=(2e-2)a in M. An empty run i with the free lengths
  n=2kappa and 2kappa+2 forces tau_i+2ea and tau_i+v in M. They differ by 2a and tau_i+v!=v (empty-run rule). With only two
  elements available, tau_i+2ea=v, so tau_i=-2a and M={v,(2e-4)a}. For two empty runs, T=-4a. Use free n=2kappa+2:
  it is admissible for m=1, and also m=2 since 2kappa+2<=2p-4 (e>=3). Then T-na=(2e-6)a must be v or (2e-4)a, forcing
  4a=0 or 2a=0. Impossible.
Every b>=p-3 is excluded, proving A>=2kappa+3 and b<=p-4 under the FULL antecedent of Sec. 0. []

## 4. Lemma MW: multi-length omission window [NEW]

Fix a non-constant z with Phi=2m and any NONZERO signed value s. Let phi=v_s(S_z), w0=R-phi the number of other letters;
for those letters put omega=x_signed-s!=0, and let G_s be their subset-sum set. Set
  K_min=max(0,p-1-2e+2m), K_max=p-3+2m,
  calK={even K:max(w0,K_min)<=K<=min(phi,K_max)}, q=|calK|.
If q>=1, avoidance forces
  (MW) w0+q<=p-1.
Proof. SR is equivalent to K=R-n even in [K_min,K_max]. For every K in calK and every subset J of the w0 other letters, omit
J and K-|J| letters of signed value s; 0<=K-|J|<=phi holds because w0<=K<=phi. All occurrences are distinct. If D is the sum
of all signed values, the selected sum is D-Ks-sum_J omega. So the attained set contains D-s calK-G_s. RS(b), K=w0 (or G_s={0}
if w0=0), gives |G_s|>=min(p,w0+1). calK has at most e<p elements and its images under multiplication by nonzero s are
distinct (step 2s); CD gives at least min(p,w0+q) attained residues. If w0+q>=p, T(z) is attained: contradiction. []
The restrictions q>=1 and s!=0 are essential; no inequality is inferred from an empty calK. This lemma does not discard the
selection upper bound |J|<=n: that bound is exactly the omitted-majority inequality K-|J|<=phi applied to the COMPLEMENT
minority subset when translating to the selected-letter picture.

Useful specialisation: m=e and 3e<=p+2. Take the dominant s of Lemma P, so phi>=2kappa+1, w0<=p-2. K_min=p-1,
K_max=p+2e-3 and q>=1. If w0<=2kappa+2-2e then phi>=K_max and q=e, forcing w0<=p-1-e=kappa-1.
If w0>=2kappa+3-2e then q=kappa+1-ceil(w0/2), and MW forces floor(w0/2)<=e-2, i.e. w0<=2e-3. But
2kappa+3-2e=2p-4e+3>2e-3 when 3e<=p+2. Thus the latter branch is impossible:
  (MW-e) m=e, 3e<=p+2 => phi_dominant>=R-(kappa-1)=p+kappa.

## 5. Proposition SH: a super-heavy run when 3e <= p+2 [NEW]

Assume 3e<=p+2. For all P with m(P)=e, MW-e gives a low/high split with stronger thresholds
  d(P)<=L:=A-(p+kappa)=kappa-1-b  OR  d(P)>=U:=p+kappa-A',  gap U-L=p+1+delta.
Complementing P swaps the two types. A path of SINGLE-RUN toggles, each still with m=e, joins some P to its complement:
index the n=p+1 runs by 0,...,n-1. Start P0={0,2,...,2e-2}. Add n-1,n-2,...,2e in that order (extending the 0 interval
backwards); remove 0; for j=1,...,e-1 add 2j-1 then remove 2j; finally add 2e-1. The end is the complement of P0. At every
step there are e intervals: the long interval [2e,n-1] stays nonempty, since n>=2e+2, and the toggles slide the e-1 isolated
runs one step. This inequality follows from 3e<=p+2 and p>=7. All sets stay proper and nonempty.
Traverse in the direction from a low endpoint to a high endpoint. Some step goes low to high across a gap p+1+delta.
Deleting i would require -d_i>=p+1+delta, impossible since beta_i<=A'<=kappa<p+1+delta. So that step adds a run h with
  d_h>=p+1+delta, and alpha_h>=d_h.
If any high ordinary-window set P' avoided h, alpha(P')>=Lambda and
A>=alpha_h+alpha(P')>=p+1+delta+2kappa+1-A'; substituting A=p-1+2kappa-delta-A' gives 0>=3+2delta, impossible. Therefore
every nonempty set avoiding h is ordinary-low. Sec. 2 then gives lambda>=0 and at least two empty runs. No claim that these
two empty runs alone are contradictory in this parameter range is made. []

## 6. Proposition L: additive lifts of pair-valued low arcs [NEW, EXPLICIT delta = 0 premise]

Assume delta=0, so A+A'=R (this is a hypothesis, NOT an imported rigidity result). For a proper arc P low in W put
  epsilon(P):=A'+d(P) in [0,p-2], U(P):=min(p-1,floor((R-epsilon(P))/2)).
The rotation sums attainable at m=1, divided by 2a, are EXACTLY the integer interval
  [kappa-epsilon(P), U(P)] reduced mod p.
Proof. For n=2nu with kappa<=nu<=min(p-1,R/2), selecting q letters of signed value -a gives x=nu-q and
max(0,2nu-(R-epsilon))<=q<=epsilon (epsilon<=p-2<2kappa<=2nu). Thus x runs from nu-epsilon to
min(nu,R-epsilon-nu). These intervals overlap or touch for successive nu (each is nonempty), have minimum kappa-epsilon,
and maximum min(p-1,floor((R-epsilon)/2)); floor((R-epsilon)/2)>=kappa because the majority has >=2kappa+1 letters. []
Its size is between 1 and p-1: if U=p-1, epsilon<=2kappa-p+1<=kappa-2; otherwise the size is
floor((p+1+epsilon)/2)<=p-1. Therefore avoidance defines a UNIQUE integer lift X(P) congruent to T(z_P)/(2a) mod p with
  (L) U(P)+1-p <= X(P) <= kappa-epsilon(P)-1.
If a path of at most p runs has EVERY nonempty consecutive subarc low, the lifts ADD: X(P)=sum_(i in P) X({i}). In particular
X({i})!=0 on an empty run, by tau_i!=0.
Proof of additivity. Append a run Q to an arc P, P'=P union Q; all three are low. Write eps1,eps2,eps for their epsilons,
U1,U2,U for their U's. Then eps1+eps2=eps+A'. The difference D=X(P)+X(Q)-X(P') is divisible by p. By L,
  D<=p+2kappa-eps-A'-3-U < p,
because if U=p-1, 2kappa-A'<=p (from A<=2p-1); otherwise U=kappa+floor((p-1-eps)/2) and
kappa-A'-eps-3<=e-eps-3<floor((p-1-eps)/2), using A'>=2kappa-p and 2e<=p+1. Also
  D>=U1+U2-2p-kappa+eps+3 > -p:
if one U_j=p-1 use the other U_j>=kappa; otherwise
U1+U2>=2kappa+p-2-(eps+A')/2 > p+kappa-eps-3, since A'<=kappa. Thus -p<D<p and D=0. Induct on arc length. []

Corollary PH (restricted pure-heavy exclusion). Under the full Sec. 0 antecedent, if all rotations are equal and some run
holds >=p of them, there is a contradiction.
Proof. Lemma U makes that value a!=0. Here A'=delta=0, A=R; A<=2p-1 and kappa>=(p-1)/2 force kappa=(p-1)/2, R=2p-2.
Let alpha_h>=p. Every arc of the p runs outside h has alpha(P)<=2p-2-alpha_h<=p-2, hence is low. Proposition L gives
 -ceil(alpha(P)/2)<=X(P)<= (p-3)/2-alpha(P).
Put D(P)=X(P)+alpha(P)/2, additive on these arcs; D(P)>=-1/2 and
D(all p runs)<= (alpha_h-p-1)/2. Every empty run has X_i>=1, since its allowed interval starts at 0 and tau_i!=0.
Let E be the number of empty runs outside h. Cutting the path at these E runs leaves at most E+1 nonempty arc pieces, each
with D>=-1/2 (empty pieces contribute 0). Hence D(all)>=E-(E+1)/2=(E-1)/2, so E<=alpha_h-p. But only
2p-2-alpha_h rotation letters lie outside h, so at least p-(2p-2-alpha_h)=alpha_h-p+2 runs there are empty: contradiction.
This does NOT settle the pure case with every run <p; no such claim from the earlier sketch is retained. []

## 7. Lemma E: exact empty-negative-side exclusions [NEW statement of the retained constraints]

For B the b letters of value !=a, omega(u)=x_u-a, let G=Sigma(omega(B)), M=Z_p minus G. Then |M|<=max(0,p-1-b), 0 not in M.
For every pattern whose negative runs are all empty, and every even n allowed by SR:
  (E) T(z)-na is NOT in {sum_J omega: J contained in B, |J|<=n, n-|J|<=A}.
In particular b<=n<=A forces T(z)-na in M. These assertions follow from selecting the actual J letters and n-|J| distinct
a-letters, with their order realised by GRX. If b>n or n>A, only the displayed restricted family is excluded, not all of G.
This distinction is essential at the lower half-range endpoint, where two non-adjacent empty runs may permit n=2kappa-2<p-2.
The all-plus case T=0, one-empty-run case T=tau_i!=0, and empty-pair cases T=tau_i+tau_j (m=1 or 2) are included.

## 8. Scope and re-derivation record

Theorem UH-A is a new NECESSARY MULTIPLICITY bound at the full upper-half interval; it does not prove UH-EXCL. Proposition SH is
an extra structural condition at 3e<=p+2, not an exclusion band. Proposition L requires delta=0 and a low-arc path; PH requires
all rotations equal AND one run with >=p letters. Lemma MW and E are word-level necessary constraints, not word constructions.
The M/P/U and ordinary W, heavy-run and two-high-set bounds are re-derived from the pending ROT-PP1 route, not accepted as
premises. All new exclusions retain k=p+1, kappa^=kappa and the full avoider/NF antecedent. No statement excludes a rotation
multiset irrespective of order/word class or outside these cells. No REFL, reflection rigidity, INV*, o_F assembly, ordered
Olson, lower kappa range, p=5, novelty/priority, Lean or human-referee claim is made. The parent owns both-family review/verdicts.

## 9. Interface / scope / import table and pins

Paths: A=/Users/jinleic/repos/aifours; ROT=A/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=A/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2;
R16=A/institute/runs/six-lane-2026-10-16/review; R18=A/institute/runs/six-lane-2026-10-18-96h/review.
| Interface | Source, LF lines, whole-file sha256 | Acceptance and scope | Instance |
|---|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16/fewodd addendum 1 line12; ZX overlays1-3; lowodd item2/M1/M4. Avoider preserved, same rotations, empty-run rule | k=p+1,H=e-1 with arbitrary odd l_i |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | lowodd item1/M2: every cyclic constant-block representation and pattern, empty runs allowed | if direction; SR derived for all m; no rearrangement of occurrences |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | R18/CFXT verdict item4: integer K>=0, nonzero terms | K=p-1 on swap differences; K=number of minority weights for full subset sums (empty sequence handled as {0}) |
| CD | classical; proof-ROW-v1.md 4-5 | same CFXT classical import; nonempty sets over prime Z_p | Lemma MW: translates by distinct multiples of 2s |

Full verdict filenames and SHA256: R16/olson-rotation-lowodd-parent-verdict-v2.md
0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only: assembly-p/proof-ROT-PP1-v2.md 99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca, read with
R18/olson-ROT-PP1-parent-erratum-v1.md 7f192a89e50ab349a37999669d0e1d411034f626730fac6118c0a546b886e479 and
R18/olson-ROT-PP1-parent-erratum-v2.md 49c3e4917ed59647d52eb204c73b6157a4aa08de7fb596345ca67c9f2c086646; not premises.
