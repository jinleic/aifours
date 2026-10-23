# KP3-EXCL: exclusion of terminal k=p+1, kappa^=p-3 for every prime p>=7, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T14:01:31-0700. Status CANDIDATE_UNVERIFIED, written word-level proof.
Scope frozen before derivation: KP3-EXCL-scope-v1.md, SHA256
58ca7d6281f5532b85536efb1cb7c0fb6e30dcabbca3bac3e0fea7b8c678c169 (2026-10-19T13:54:42-0700). Its disclosure records Main's
UNVERIFIED guided hypotheses. None of those hypotheses, the pending UH packet, or accepted PP1/KP2 endpoints is a premise.
This proof re-derives the needed pairing, m=3 window and super-heavy/light-set arguments; it then proves the small missing-set
classification and the final run-position contradiction. No inverse critical-sumset theorem is imported.
Inputs ONLY: accepted NF with its empty-run rule, GRX if direction, RS(b), classical Cauchy-Davenport. CT is not needed.
No scientific computation/enumeration, solver, test/build, model CLI or Lean. No novelty/priority, human review or formal claim.

## 0. Exact theorem and antecedent discipline

THEOREM KP3-EXCL. Let p>=7 be prime. No avoider w of length4p-2 over D_(2p) (no 2p distinct letters in increasing original
index order with identity product) has SOME admissible normal form u with terminal k=p+1 and kappa^=p-3.
No o_F, nonempty-run, reflection-rigidity or rotation-pair hypothesis. H^=2 is arbitrarily distributed among odd reflection
blocks: either one block of length5 or two blocks of length3, all others singletons. No entire upper-half exclusion is claimed.

We prove the stronger word-form assertion: there is no avoider u of length4p-2 with a cyclic constant-block representation
R_1 S_1 ... R_(p+1) S_(p+1), S_i=sigma_(y_i)^(l_i), all l_i odd, sum_i(l_i-1)/2=2, and every empty R_i separating DIFFERENT
values y_(i-1),y_i. An admissible NF u of the hypothesised w is such an avoider by NF. All multiset/position conclusions below
remain under THIS full word/NF antecedent; no rotation multiset is excluded in other word classes or cells.

## 1. Inputs, notation and recomputed reflection capacity

Group law (v,epsilon)(v',epsilon')=(v+epsilon v',epsilon epsilon'); rho_x=(x,+1),sigma_y=(y,-1), x,y in Z_p. Rotation letters
are actual occurrences; X is their multiset, X_i that of R_i, v_x multiplicity. Indices cyclic mod p+1.
NF: proof-ROT-few-E-v4.md28-43 with accepted lowodd/fewodd/ZX overlays (Sec.10): normalisation preserves avoidance, length and
rotation multiset; all l_i odd; empty R_i implies y_(i-1)!=y_i; H=(F-k)/2, kappa^=p-1-H, R=2p+2kappa^-k.
GRX: notes-GRX-v1.md7-20, accepted for every cyclic constant-block representation, empty runs and every pattern z:
f_i=[z_i!=z_(i+1)], Phi=sum f_i (even), delta_GRX=#{i:l_i!=f_i mod2}, C_max=F-delta_GRX,
theta_i=y_(i-1)-y_i, T(z)=sum_(z_i=+1)theta_i. If C even, Phi<=C<=C_max, 0<=2p-C<=R, and some 2p-C rotation occurrences
have signed sum T(z) (a letter x in run i counts z_i x), the word has an identity2p-subword. Only this implication is used.
RS(b): for nonzero terms S over prime Z_p and integer K>=0,
 |Sigma_(<=K)(S)|>=min(p,1+sum_x min(K,v_x(S))). In particular t nonzero terms have >=min(p,t+1) subset sums including0.
CD: classical |B+C|>=min(p,|B|+|C|-1) for nonempty B,C in Z_p. Exact source/verdict pins are in Sec.10.

For the word form F=p+5,R=3p-7 and H=2. Every l_i is odd, so delta_GRX=p+1-Phi and C_max=Phi+4. Write l_i=1+2h_i, sum h_i=2.
At a fixed parity f_i the selected count in S_i is f_i+2j_i with 0<=j_i<=h_i. Thus C=Phi, Phi+2, Phi+4 are ALL realised,
whether the two pairs lie in one block or in different blocks. Their signed contribution depends only on f_i, not j_i.
Writing Phi=2m, n=2p-C, GRX therefore gives the following sufficient rule (all even n throughout):
 (SR3) max(0,2p-4-2m)<=n<=min(2p-2m,R), signed rotation sum=T(z) => identity2p-subword.
For a set P of runs let z_P=-1 on P,+1 elsewhere. For nonempty proper P, m(P) is its number of maximal cyclic intervals;
Phi=2m(P), 1<=m(P)<=(p+1)/2. Put tau_i=y_i-y_(i-1). Then T(z_P)=sum_(i in P)tau_i and tau_i!=0 on an empty R_i.
Explicit lengths used:
 m=0 (all-plus,T=0): n=2p,2p-2,2p-4;
 m=1: n=2p-2,2p-4,2p-6;
 m=2: n=2p-4,2p-6,2p-8;
 m=3: n=2p-6,2p-8,2p-10.
All listed lengths are nonnegative and <=R for p>=7. Cyclically moving a cut conjugates the selected product, so identity is
unchanged and GRX gives a selection in original linear order; no rearrangement of rotation occurrences is assumed.

## 2. Dominant signed class [RE-DERIVED, not a pending premise]

Lemma M. A multiset of size N and maximum multiplicity mu has q disjoint unequal-value pairs if 2q<=N and q<=N-mu.
Proof. Cap each multiplicity at q; the capped total is >=2q. If mu<=q it is N; otherwise the top value retains q and the
others retain >=q (one retains q, or all their N-mu>=q occurrences are retained). Choose 2q occurrences within these caps,
list equal values consecutively x_1,...,x_(2q), and pair x_i with x_(i+q). An equal pair would force q+1 consecutive equal
occurrences, violating the cap. []

Lemma P. For every non-constant z the signed rotation multiset S_z has a value of multiplicity >=2p-5.
Proof. Let Phi=2m and n=max(p-1,2p-4-2m), even. It satisfies SR3: n<=2p-6 (m>=1,p>=5), n<=2p-2m (2m<=p+1), and n<=R.
If the maximum signed multiplicity were <=2p-6=R-(p-1), Lemma M gives p-1 disjoint unequal-signed-value pairs (2(p-1)<=R).
There are R-2(p-1)=p-5 unpaired letters, enough to fix n-(p-1) fillers since 0<=n-p+1<=p-5. Choose one occurrence per pair
and those disjoint fillers. Swapping the i-th pair adds d_i!=0 to the signed sum. RS(b), K=p-1, gives every residue among
the subset sums of the p-1 differences; some actual n-letter selection has sum T(z), contradicting SR3/avoidance. []

Lemma U. There is a NONZERO a such that the signed dominant value of every non-constant z is in {a,-a}; at least2p-5
rotation occurrences have value in this class.
Proof. 2(2p-5)>3p-7, so the dominant value for each z is unique. All its >=2p-5 letters have unsigned value in {s(z),-s(z)}.
Different classes are disjoint and cannot each contain this many letters; hence the class is common. If it were {0}, the
p+1 block values in Z_p give y_j=y_(j') for distinct blocks. The proper arc between them has m=1,T=0; n=2p-6 is admissible,
and 2p-6 of the >=2p-5 zero-valued rotations have signed sum0, an identity. Thus a!=0. []

Orient a so A=v_a(X)>=A'=v_(-a)(X). Put b=R-A (number of non-a letters), delta=R-A-A' (number outside {a,-a}); delta<=p-2.
All-plus forces A<=2p-1 (2p letters a would sum0), and A'<=p-3 (otherwise p-2 each of a,-a sum0 with length2p-4).
For P put alpha(P),beta(P) its counts of a,-a, d(P)=alpha(P)-beta(P), additive on disjoint runs. Signed counts are
 phi_a(z_P)=A-d(P), phi_(-a)(z_P)=A'+d(P).
Lemmas P/U give for every proper nonempty P:
 (W) d(P)<=lambda:=A-2p+5=p-2-b OR d(P)>=Lambda:=2p-5-A'.
The gap Lambda-lambda=p-3+delta>0. No high-run/light-set conclusion is assumed from this window alone.

## 3. The three-length m=3 window [RE-DERIVED in this cell]

Lemma MW3. For every P with m(P)=3, its dominant signed multiplicity is >=2p-3, not merely2p-5.
Proof. Let s be its dominant signed value, phi=v_s(S_z)>=2p-5, w0=R-phi<=p-2. By Lemma U s is a or -a, so s!=0.
Let W be the w0 other signed letters, weights omega=x_signed-s!=0, and G_s their subset-sum set. For K in {p-1,p+1,p+3}
with K<=phi, every subset J of W can be omitted together with K-|J| dominant letters: w0<=p-2<K<=phi, so all counts fit.
The remaining n=R-K is respectively2p-6,2p-8,2p-10, each admissible at m=3. If D is the total signed sum, the attained sums
contain D-Ks-G_s. RS(b) gives |G_s|>=min(p,w0+1) (G_s={0} when w0=0); CD with the distinct translates spaced2s gives at least
min(p,w0+q) attained residues for q such K. Avoidance requires w0+q<=p-1.
Now phi>=2p-5>=p+2. If phi>=p+3, all three K work: q=3, w0<=p-4 and phi=R-w0>=2p-3.
The only other possibility is phi=p+2. Then q=2 and w0+q=(3p-7-(p+2))+2=2p-7>=p, contradiction (including equality p=7).
This proves the claim with every omitted subset and dominant filler explicitly available. []

Thus for m(P)=3 there is the stronger split
 (W3) d(P)<=A-2p+3 OR d(P)>=2p-3-A',
whose gap is 4p-6-A-A'=p+1+delta. Complementing P swaps these two types.

## 4. A super-heavy run, light sets, and two empty runs [RE-DERIVED in full]

Index runs 0,...,N-1 with N=p+1>=8. There is a single-run-toggle path, all m=3, from P0={0,2,4} to its complement:
add N-1,N-2,...,6 in order (extending the 0 interval backwards); remove0; add1/remove2; add3/remove4; add5.
At each step there are three intervals. The long interval [6,N-1] has at least two runs and remains nonempty when0 is
removed; the other two intervals slide from2,4 to1,3. The final set is {1,3} union [5,N-1], exactly P0's complement.
Traverse in the direction from a W3-low endpoint to its W3-high complement. At some step the value crosses a gap p+1+delta.
Deleting a run i would require -d_i>=p+1+delta, impossible since beta_i<=A'<=p-3. So some step adds a run h with
 (H) d_h>=p+1+delta, and alpha_h>=d_h; R_h is nonempty.

Every nonempty set P' avoiding h is ordinary-W-low. Otherwise alpha(P')>=Lambda=2p-5-A', and
 A>=alpha_h+alpha(P')>=p+1+delta+2p-5-A'=3p-4+delta-A';
but A=3p-7-delta-A', giving 0>=3+2delta, impossible. In particular lambda>=0: if lambda<=-1 all p runs outside h would need
beta_i>=1, so A'>=p>p-3. Combining lambda>=0 with A<=2p-1 gives
 A=2p-6+c, c in {1,2,3,4,5}; b=p-1-c; lambda=c-1.
This reduction does NOT import UH-A: the cases c=1,2 will also be excluded below.
Let Q+={i!=h:d_i>=1}. If nonempty, |Q+|<=d(Q+)<=lambda. Every nonempty run outside h either contains a non-a letter
(at most b such runs) or lies in Q+. At most b+lambda=p-2 of the p runs outside h are nonempty: there are AT LEAST TWO
EMPTY RUNS. Moreover every P avoiding h with m=3 is W3-low (the W3-high threshold exceeds the ordinary high threshold), so
 (L3) m(P)=3, h not in P => d(P)<=A-2p+3=c-3.

## 5. Actual subset sums and exact filler bounds

Let B be the b non-a rotation occurrences; for u in B set omega(u)=(x_u-a)/(2a)!=0 in Z_p (2a is a unit). Let G be all subset
sums of omega(B), including0, M=Z_p minus G. RS(b), K=b, gives |M|<=p-1-b=c and 0 not in M.
For a pattern whose negative runs are EMPTY, every rotation keeps its signed value equal to its value. Put t=T(z)/(2a).
A choice of J contained in B and n-|J| a-letters has sum divided by2a equal to n/2+sum_J omega. It is valid exactly when
 |J|<=n and n-|J|<=A.
Consequently if b<=n<=A, avoidance forces t-n/2 in M. If n=A+1 (and n>=b), every NONEMPTY J is allowed; avoidance forces
 t-n/2 not in G_nonempty, hence t-n/2 is in M or is0 (only the empty subset can give a G-value outside G_nonempty).
Here G_nonempty is the set of nonempty subset sums, not asserted disjoint from {0}.

Write n=2p-2j, so t-n/2=t+j modp. All-plus permits j=0,1,2 with t=0; one empty run i permits j=1,2,3 with
t_i=tau_i/(2a)!=0; two empty runs permit j=1,2,3 if adjacent, j=2,3,4 otherwise, with t=t_i+t_l. Every one of these n
satisfies n>=b: the smallest is2p-8>=p-2>=b for p>=7. Thus only the upper filler bound n<=A needs a separate check below.
These patterns use actual disjoint rotation occurrences and the reflections supplied by SR3. M is an actual subset-sum
complement, not an arbitrary feasible residue/count model.

## 6. Cases c=1,2,3,4 [NEW at the changed cell, with full filler accounting]

c=1: A=2p-5,b=p-2,|M|<=1. For an empty run t, j=3 is free (n=A-1), so t+3 in M. j=2 has n=A+1 and permits every nonempty
minority subset, so t+2 is in M or0. It differs from the unique M-element t+3, forcing t+2=0. Thus every empty t=-2 and
M={1}. For two empties j=3 is admissible whether adjacent or not, free with n=2p-6<A; it requires -2-2+3=-1 in M={1}.
Impossible for p>=7.

c=2: A=2p-4,b=p-3,|M|<=2. All-plus j=2 free gives2 in M. An empty run has j=2,3 both free, so t+2,t+3 in M. They differ
by1, and t+2!=2 since t!=0; hence t+3=2, t=-1 and M={1,2}. Two empties at free j=2 require0 in M, impossible. This j is
admissible both for adjacent and non-adjacent pairs.

c=3: A=2p-3,b=p-4,|M|<=3. All-plus j=2 free gives2 in M; all-plus j=1 has n=A+1, so1 not in G_nonempty; since1!=0,
1 in M. For an empty run, j=2,3 are free and j=1 has n=A+1, so t+2,t+3 in M and t+1 in M or0.
If t+1!=0, all three consecutive residues t+1,t+2,t+3 lie in M, avoid0, and t!=0. Represent t canonically by 0,...,p-1.
A length3 interval avoiding0 cannot wrap across0, so 1<=t<=p-4. If t=1 the union with {1,2} has four residues {1,2,3,4};
if t>=2 it has five. Either contradicts |M|<=3. Hence t=-1 for every empty run. A pair at free j=2 requires0 in M, impossible.

c=4: A=2p-2,b=p-5,|M|<=4. All-plus j=1,2 free give {1,2} in M. All three single-empty lengths are free, giving
I_t:=t+[1,3] contained in M. As above 1<=t<=p-4. For t>=2 the union {1,2} union I_t has five residues, impossible. So every
t=1 and M={1,2,3,4}. A pair of empty runs at free j=3 (admissible in either adjacency case) requires5 in M, impossible.

All these contradictions use the existence of two empty runs from Sec.4. Thus only c=5 remains, without assuming an unproved
reduction or importing the pending UH-A result.

## 7. Case c=5: complete elementary missing-set / empty-position classification [NEW]

Here A=2p-1,b=p-6,|M|<=5. All-plus j=1,2 are free, so {1,2} contained in M. All single-empty j=1,2,3 are free, so
 I_t=t+[1,3] contained in M, t!=0.
Since 0 not in M, every empty t has a canonical representative 1<=t<=p-4. There are at least two empty runs.

(a) No empty t>=3. If one existed, I_t and {1,2} are disjoint, so M={1,2,t+1,t+2,t+3} exactly. Its ONLY cyclic interval of
three consecutive residues avoiding0 is I_t: the component {1,2} has length2, the other has length3, separated on both sides
by at least one omitted residue (including0 on the wrap side). Thus another empty s, whose I_s must fit, satisfies s=t.
If these two empty runs are adjacent, their pair forces 2t+[1,3] contained in M; this length3 interval must equal I_t,
forcing 2t=t and t=0. If not adjacent, their pair forces 2t+[2,4]=I_t, so 2t+2=t+1 and t=-1. Both contradict 3<=t<=p-4.
Equality of the starting residues follows because a proper cyclic interval of length3<p-1 has a unique start.

(b) No empty t=2. By (a) all empty values are1 or2. If t=2 existed, M={1,2,3,4,5}. Pair it with another empty s in{1,2}.
The sum t+s is3 or4. For adjacent runs, (t+s)+[1,3] includes6; for non-adjacent runs, (t+s)+[2,4] includes6. Every required
length is free (n<=A), so6 would be in M, impossible for p>=7. Thus ALL empty t=1.

(c) Exactly two adjacent empty runs. A single empty now forces {1,2,3,4} contained in M. A non-adjacent pair with sum2
requires {4,5,6} contained in M, giving SIX distinct residues in M. Hence every pair of empty runs is adjacent. A cycle of
length p+1>=8 has no triangle: a pairwise-adjacent set has at most two vertices. Since at least two empties exist, there are
EXACTLY TWO, adjacent. Their adjacent-pair constraint adds5, so M={1,2,3,4,5} exactly, and each has tau=2a.
This classification used only forced intervals and occurrence-valid lengths, not a critical-sumset theorem or its conjecture.

## 8. Four pure-a singleton runs and the final m=3 contradiction [NEW]

The super-heavy run h is nonempty. Of the p runs outside h, exactly two are empty, so p-2 are nonempty. At most b=p-6 of
these nonempty runs contain a non-a letter. Let Q be the nonempty PURE-a runs outside h; there are at least4. The whole set
Q avoids h, so ordinary light sets give d(Q)<=lambda=4. Each contributes its positive number of a-letters, hence Q has
EXACTLY FOUR runs, each containing EXACTLY ONE a-letter. Let E be the two adjacent empty runs. Q and E are disjoint and avoid h.

Cycle lemma. In a cycle of length N>=8, four marked vertices Q and a disjoint adjacent pair E admit P contained in Q union E
with m(P)=3 and at least three vertices of Q.
Proof. If Q contains three pairwise non-adjacent vertices, those three alone form P. Otherwise the induced subgraph on Q is
one path of length4 vertices or two paths each of length2 vertices. Indeed its path-component sizes sum4 and independence
number is the sum of their ceiling half-sizes; no independent triple means all components have even size.
- One path of four: at least one vertex v of E is not adjacent to any Q vertex. Otherwise the two outside neighbors of the
  adjacent E pair are the two endpoints of the Q path, which would make the whole cycle have only6 vertices. Pick three Q
  vertices making two components (the first two and the last); adding v gives three components.
- Two adjacent Q pairs: if some v in E has no Q neighbor, use all four Q plus v, giving three components. Otherwise E occupies
  precisely a gap of length2 between the Q pairs. Delete from Q the endpoint adjacent to one chosen v in E; the remaining
  three Q vertices still form two components. Add that v but not the other E vertex; v is now isolated from the retained Q,
  giving the third component. The other gap is nonempty (N>=8), so no additional merger occurs.
Each constructed set is proper, and the number of cyclic components is m(P). []

Apply the lemma to the actual run cycle. The resulting P avoids h, has m=3, and d(P)=|P intersect Q|>=3 because Q consists of
pure-a singletons and E is empty. But the strong light bound L3 at c=5 says d(P)<=c-3=2. Contradiction.

Every c=1,...,5 is impossible. This proves the word-form assertion, and hence KP3-EXCL by NF. []

## 9. Preserved route notes, source boundaries and scope

- Re-derived, not new progress: unequal pairs M, all-pattern dominant class P/U, the m=3 multi-length omission argument and
  super-heavy/light-set path are rebuilt from the previous pending route; no pending statement is a premise.
- New closing steps: exhaustive c=1..5 reduction without assuming UH-A; elementary M/empty classification c=3,4,5; exact four
  pure-a singleton count; cycle lemma combining them with the adjacent empty pair. The guided parent sketch's classification
  and exhaustive reduction were unproved at freeze; both have now been proved above, not assumed.
- The ordinary c=5 light bound d(P)<=4 ALLOWS four pure-a singletons, so it is not itself a contradiction. The separate m=3
  bound d(P)<=2 and the cycle lemma close this failed single-window route. Likewise |M|<=5 alone allows a length3 missing
  interval: coupling every second empty run via both adjacency patterns was essential.
- All non-free lengths used (c=1,c=3) have n=A+1 and explicitly require nonempty minority subsets. No assumption that every
  G-residue has a nonempty representation, and no all-runs-nonempty shortcut. No formula lambda=c-2 is used: lambda=c-1.
- No complete classification of B's weights is needed, only the exact missing set M at the constrained word. No count model
  or rotation sequence is called a word or a counterexample. The full NF antecedent is retained on every consequence.
- No use of PP1/KP2 endpoint conclusions via expansion: deleting reflection pairs and inserting rotations has no supplied
  avoidance-preserving interface. No REFL extension, reflection rigidity, INV*, o_F assembly, upper-half exclusion, other
  kappa cell, p=5, full ordered Olson, novelty/priority, human review or Lean verification is claimed.

## 10. Interface / scope / import table and pins

Let Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2;
R16=Aroot/institute/runs/six-lane-2026-10-16/review; R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, LF lines, whole-file SHA256 | Accepted scope and exact use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | lowodd item2/M1/M4, fewodd addendum1 line12, ZX overlays1-3: avoidance/rotations preserved, empty-run rule. SOME terminal k=p+1,kappa^=p-3 implies H2, arbitrary odd-block distribution |
| GRX | ROT/notes-GRX-v1.md7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | lowodd item1/M2: every representation and pattern, empty runs allowed, same group law. If direction; capacities Phi..Phi+4; actual occurrences throughout |
| RS(b) | SR2/proof-ROW-v1.md16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | CFXT item4: integer K>=0, nonzero terms. K=p-1 on swap differences; K=w0 on signed-minority weights; K=b on B weights (empty sequence handled as {0}) |
| CD | classical, proof-ROW-v1.md4-5 | nonempty sets over prime Z_p; MW3 uses q=2 or3 distinct translates spaced2s, s!=0 |

Verdict files (whole-file SHA256): R16/olson-rotation-lowodd-parent-verdict-v2.md
0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only, NOT premises: upper-half/proof-UH-CONSTRAINTS-v1.md
56327b678bf9f7fe62d6f518499ab692f00897a3ecff2c62ddecac4a42a5115c and parent erratum8f1ea491; no mathematical step is omitted
by referring to them. Source labels and comparison context are not acceptance or a claim of independent model review.
