# R = p, small kappa: a C_(2p) fixed window and a simultaneous integer lift (candidate v1)

Owner OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:11:19-0700.  Status:
CANDIDATE_UNVERIFIED.  Written mathematics only: no computation, finite search, model call or model agreement as proof.
This is option (b) of scope-Rp-smallkappa-v1.md (69f108dcbbcc7d1f46a66a375b6e562d938f0226c121c5684a3c7a18df88f41d).
No previous file is changed.  Parent owns hostile reviews and final verdicts.

## 1. Exact statement and accepted inputs

**Theorem RP-LIFT (candidate).**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p).  Suppose its rotation
letters lie in one pair {rho_x, rho_-x}, x != 0, exactly R = p letters are rotations, and every maximal cyclic CONSTANT
reflection block has odd length.  Write H := sum_i floor(l_i/2) over these blocks and kappa := p - 1 - H.  If
   1 <= kappa <= (p - 3)/2,
then w has a subword of exactly 2p letters, in increasing original index order, whose ordered product is the identity.
No B < kappa, purity, inherited condition or hypothesis on reflection values is imposed.

In particular, this excludes the whole previously open R = p region (A),
   p >= 11,   2 <= kappa < ceil((p + 1)/4),
including its smallest cell p = 11, kappa = 2, for every B (not just B = 0).
This is not unrestricted REFL(p), INV*(p), ordered Olson or a novelty claim.

Imports (only the following three mathematical interfaces): Lemma W, Fact 2.1 and Fact 2.2 in
proof-REFLHI-arcs-v5.md, read through all five errata and the binding readings S1/m1-m7 in the parent verdict
/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md,
SHA256 13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547 (CORRECTNESS_ACCEPTED_SCOPED_PARTIAL).
The accepted source bytes were re-hashed before this candidate; all match the verdict:
- v5: 4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c;
- erratum 1: 512e1d9e9a5dcdd4ad85840ce74d6d29ab8e1b8eb72db944ddff4a5683393331;
- erratum 2: b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820;
- erratum 3: 380106c91b0bcf250a8fd98583e75b39faf3d4c7d3ecd0eba2b2472bc15e669a;
- erratum 4: 32811de59e1b5ca736a3db1a9b6592266dbcbcd8690cff27aa143b678e5907f1;
- erratum 5: 40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4.
The verdict supersedes erratum 4's narrowing, but that branch is not used here.  No separate SEG-k, TRANSFER, region-B,
B-prime, STAB or unaccepted stronger statement is a premise.

For completeness the three imported interfaces are stated at the exact instances used.  Normalise x = 1 and A >= B by
the accepted automorphisms, which preserve identity subwords and the maximal block lengths.  Write cyclically
   w = R_1 S_1 ... R_k S_k,   S_i = sigma_(y_i)^(l_i), l_i odd,
with run R_i immediately before block S_i, r_i its length, a_i,b_i its rho_1,rho_-1 counts, d_i := a_i - b_i,
A := sum a_i, B := sum b_i, D := A - B, theta_i := y_(i-1) - y_i, u_i := theta_i/2 in Z_p.  Empty runs are genuine:
r_i = 0 implies theta_i != 0.  Indices are cyclic, y_0 = y_k, sum theta_i = 0, and
   R = 2p - k + 2 kappa,   E(P) := A_P + B_(P^c) = B + sum_(i in P) d_i,   E(P^c) = R - E(P).
A proper nonempty set P of runs has m(P) maximal cyclic intervals.  Lemma W: if
   u_P := sum_(i in P) u_i belongs modulo p to
   I(P) := [-gamma_m(R - E(P)), gamma_m(E(P))],
   gamma_m(E) := min(p - m, E - kappa + m - 1, floor(E/2)),   m = m(P),
then w has an identity 2p-subword.  Fact 2.1: gamma_m(E) = floor(E/2) exactly when
   ceil(E/2) >= kappa + 1 - m   and   floor(E/2) <= p - m.
Fact 2.2: an avoider has R >= p and every rotation run has length at most 2(R - p) + 1.

Assume below, toward a contradiction, that w avoids.  At R = p Fact 2.2 forces every nonempty rotation run to consist of
one letter; hence exactly p runs are nonempty, and all others are empty.  The length identity gives
   k = p + 2 kappa,   exactly 2 kappa runs are empty,   d_i in {+1,-1} on nonempty runs and d_i = 0 on empty runs.       (1)

## 2. A fixed forbidden interval in C_(2p)

Let C := Z/(2p)Z.  For theta in Z_p, let e(theta) be its unique EVEN lift in C (the even subgroup maps isomorphically to
Z_p).  The map e is additive.  Set
   alpha_i := e(theta_i) - d_i in C,   beta := -B in C,
   psi(P) := beta + sum_(i in P) alpha_i = e(2u_P) - E(P) in C.                                               (2)
Then sum_i alpha_i = -D in C and
   psi(P) + psi(P^c) = -2B - D = -R = p in C.                                                               (3)
For a nonempty run alpha_i is odd, so alpha_i != 0 in C.  For an empty run alpha_i = e(theta_i) is even and nonzero by
genuineness.  Thus every alpha_i is nonzero, with exactly 2 kappa of them even.

**Lemma FWIN.**  If
   kappa + 1 <= m(P) <= (p + 1)/2,
then avoidance forces psi(P) to have its unique integer representative in [1,p-1].
Proof.  For all 0 <= E <= p and m in this range, ceil(E/2) >= 0 >= kappa + 1 - m, and
floor(E/2) <= (p-1)/2 <= p-m.  Fact 2.1 makes I(P) = [-floor((p-E)/2), floor(E/2)].  Membership of u_P in this interval
modulo p is equivalent to the existence of an EVEN integer t in [-(p-E),E] with t = 2u_P modulo p: put t=2j.
An even t has class e(2u_P) in C, so such t is equivalent to psi(P) having a representative s=t-E in [-p,0].
Conversely, if psi(P) has a representative s in [-p,0], t=s+E has class e(2u_P) in C, hence is even, lies in [-(p-E),E],
and reduces to 2u_P modulo p; thus t/2 witnesses membership in I(P).  Lemma W rules this out for an avoider.
The classes of [-p,0] are p+1 consecutive classes in C and their complement is exactly the classes [1,p-1].  []

This changes the earlier arc method's variable E-window into ONE fixed interval, keeping the parity information in C.
The next step is an integer lift, not a Cauchy-Davenport cardinality estimate.

## 3. Connectivity of the pattern graph (proved here)

For 1 <= m with 2m < k, let F_m be the proper nonempty subsets of the k-cycle with exactly m cyclic intervals; join two
patterns by an edge when they differ at exactly one run index and both belong to F_m.

**Lemma CONNECT.**  The graph F_m is connected.  Every run index i is toggled by at least one edge of F_m.
Proof.  A pattern has exactly 2m boundaries between adjacent run indices, lying at distinct block sites of the k-cycle;
these boundaries alternate outside-to-inside and inside-to-outside.  Moving a boundary one site into a free adjacent site
without colliding with another boundary toggles exactly one run and leaves the interval count m unchanged.
We prove that any two such boundary configurations with the alternating labels are linked by these moves, including a
pattern and its complement.

Put n=2m.  Mark one outside-to-inside boundary as number 1; in cyclic order mark the other boundaries 2,...,n.  Choose
integer lifts of their positions satisfying
   x_1 < x_2 < ... < x_n < x_1 + k.
Labels alternate with the number.  Every pattern can be represented this way, with boundary 1 chosen at any of its
outside-to-inside boundaries.  The feasible lifted configurations form
   L = {x in Z^n : x_(i+1)-x_i >= 1 for 1<=i<n, x_1+k-x_n >= 1}.
A feasible unit change of one coordinate projects to the allowed boundary move above.  We show L is connected.

Given x,y in L, z_i := min(x_i,y_i) also lies in L.  For consecutive coordinates this follows from
min(x_(i+1),y_(i+1)) >= min(x_i+1,y_i+1) = z_i+1.  For the wrapping inequality, if z_1=x_1, then z_n<=x_n gives
z_1+k-z_n>=x_1+k-x_n>=1; the other case is the same.
If x != z, put S={i:x_i>z_i}.  A coordinate i in S can be decreased by one whenever its preceding cyclic gap is >1;
this preserves the preceding gap, and enlarges the following one.  If that preceding gap equals 1, its predecessor is
also in S: writing x_0=x_n-k and z_0=z_n-k, x_i=x_(i-1)+1 and z_i>=z_(i-1)+1 together with x_i>z_i imply
x_(i-1)>z_(i-1).  If no coordinate of S were decreasable, following predecessors would force every coordinate into S and
every gap to equal 1.  Their sum would give k=n, contrary to 2m<k.  A decreasable coordinate therefore exists; repeated
steps reduce sum_i(x_i-z_i) until x=z.  Likewise y can be decreased to z, giving a unit-move path x to y by reversing
that second path.  Thus L, and hence F_m, is connected.  For the complement of a pattern choose boundary 1 at one of its
old inside-to-outside boundaries; the same argument applies (no claim that the old labels remain at their old sites).

There is at least one allowed boundary move because n<k leaves a free site adjacent to some boundary.  It toggles some
index t.  Rotate the whole configuration by i-t to obtain an edge toggling any prescribed i.  []

## 4. Simultaneous integer lifts of all run increments

Let L0 := kappa+1 and U0 := (p+1)/2.  The assumed bound kappa <= (p-3)/2 gives L0<=U0.  For every m in this range,
2m<=p+1<k=p+2kappa, so Lemma CONNECT applies.
For every P in F_m let N(P) in [1,p-1] be the representative given by Lemma FWIN.

**Lemma ILIFT.**  There are nonzero integers h_1,...,h_k with |h_i|<=p-2 such that:
- h_i represents alpha_i modulo 2p; it is odd for each nonempty run and even for each empty run;
- for each m in [L0,U0] a constant c_m in Z satisfies
      N(P) = c_m + sum_(i in P) h_i   for every P in F_m;                                                     (4)
- for every such P,
      abs(sum_(i in P) h_i - sum_(i notin P) h_i) <= p-2.                                                     (5)
Proof.  Pick an edge of F_(L0) adding index i (orient an edge the other way if needed), which exists for every i by
CONNECT.  Its integer difference N(P u {i})-N(P) represents alpha_i and lies in [-(p-2),p-2].  This interval has fewer than
2p integers, so at most one integer in it represents alpha_i; call it h_i.  Every edge in every F_m adding i has the
same congruence and the same bounds, so has difference h_i (and a removing edge has difference -h_i).  Since alpha_i is
nonzero, h_i is nonzero; since 2p is even, h_i has the same parity as alpha_i.  By connectivity the quantity
N(P)-sum_(i in P)h_i is constant on F_m, giving (4).  No equality of c_m across different m is needed or asserted.
P^c also belongs to F_m.  Thus (4) cancels c_m, and N(P)-N(P^c) lies in [-(p-2),p-2], proving (5).
In fact (3) also gives N(P)+N(P^c)=p (their sum lies in [2,2p-2] and is p modulo 2p), consistently with
2c_m+sum_i h_i=p; this last identity is not needed for (5).  []

By (1) and ILIFT, each of the p nonempty-run h_i has abs(h_i)>=1 and each of the 2kappa empty-run h_i has abs(h_i)>=2.
We next prove that such integers cannot obey (5) for all m in [L0,U0].

## 5. A cyclic signed-sum lemma

**Lemma LIGHT.**  Let n nonnegative weights be arranged on a cycle, with n>=2f, f>=1.  There is an independent set of f
vertices (no two cyclically adjacent) of weight at most f/n times the total weight.  The same conclusion holds for a
disjoint union of paths with n vertices (use the vertices in their path order).
Proof.  The set {0,2,...,2(f-1)} is independent on the n-cycle: its wrapping gap is n-2(f-1)>=2.  Its n cyclic translates
all have f vertices and each vertex belongs to exactly f translates.  Their average weight is f/n times the total, so
one is no heavier than that.  For a disjoint union of paths, list the paths consecutively and add edges to turn this list
into one cycle; independence in the augmented cycle implies independence in the original paths.  []

**Lemma SIGN.**  Let p>=5 be odd, 1<=kappa<=(p-3)/2, and k=p+2kappa.  Let h_1,...,h_k be nonzero integers on the k-cycle,
with a marked set E of exactly 2kappa indices whose abs(h_i)>=2 (all other abs(h_i)>=1).  Then there is a sign vector
s_i in {+1,-1} with between 2(kappa+1) and p+1 cyclic sign changes such that
      sum_i s_i h_i > p-2.                                                                                (6)
Thus its positive set is some P in F_m with L0<=m<=U0.
Proof.  Put w_i=abs(h_i), S=sum_i w_i>=k+2kappa, and start from s_i=sign(h_i), which gives sum_i s_i h_i=S.  Let the number
of its sign changes be 2m0 (m0=0 means every h_i has the same sign).

Case 1: L0<=m0<=U0.  The initial vector works, since S>=k+2kappa>p-2.

Case 2: m0>U0.  There are 2m0 maximal constant-sign stretches around the cycle.  Their odd-numbered stretches form one
nonadjacent family of m0 stretches, and their even-numbered stretches form another.  Choose the family of smaller total
weight (<=S/2) and within it the f=m0-U0 lightest stretches.  Since 1<=f<m0, flipping their signs removes exactly 2f
boundaries (the chosen stretches are pairwise nonadjacent and at least one member of the chosen family stays unflipped),
so the resulting vector has 2U0=p+1 sign changes.  The total flipped weight is <= f S/(2m0).  Its signed sum is therefore
>=S(1-f/m0)=S U0/m0>=2U0=p+1>p-2, since S>=2m0 (each stretch is nonempty).

Case 3: m0<L0.  Write f=L0-m0>=1.  First suppose m0>=1.  Let J be the set of indices strictly internal to their original
constant-sign stretches: i is in J iff both neighbours of i have the same original sign as i.  Each of the 2m0 stretches
has at most two noninternal indices, so n:=|J|>=k-4m0, and
   n-2f >= p-2-2m0 >= p-2-2kappa >=1.
J is a disjoint union of paths (interior portions of stretches).  LIGHT supplies an independent F subset J of size f with
weight <= f/n times W_J:=sum_(i in J) w_i.  Flip these f signs.  Both neighbours of a flipped index had its old sign and
are unflipped; no two flipped indices are adjacent.  Each flip therefore adds exactly two sign changes, for a total of
2m0+2f=2L0.  The new signed sum is >=W_(J^c)+(1-2f/n)W_J.  Let e_J:=|E n J|; by the marked-weight assumption,
W_J>=n+e_J and W_(J^c)>=k-n+(2kappa-e_J).  As 1-2f/n>=0, the sum is >=
   k+2kappa-2f-(2f/n)e_J >= k+2kappa-2f-2kappa = k-2f = p-2+2m0 > p-2.

If m0=0, all indices have the same sign.  Apply LIGHT directly to the full cycle with n=k and f=L0=kappa+1 (k>=2f as
p>=5).  Flipping the resulting independent set produces 2L0 sign changes and a signed sum >=
   S(1-2L0/k)=S(p-2)/k >= (k+2kappa)(p-2)/k > p-2,
since kappa>=1.  This finishes all cases.  []

## 6. Proof of RP-LIFT and precise delta

Assume an avoider w under RP-LIFT's hypotheses.  Sections 1-4 produce the integers h_i satisfying (5) for EVERY pattern
P with L0<=m(P)<=U0.  The empty-run indices form a marked set E of size 2kappa and abs(h_i)>=2 there; all h_i are nonzero.
Lemma SIGN gives signs s_i and their positive set P in one of those F_m for which
   sum_i s_i h_i = sum_(i in P) h_i - sum_(i notin P) h_i > p-2,
contradicting (5).  Hence w has an increasing-index identity 2p-subword.  []

Exact new coverage against parent verdict 13ee1ba8...a547: for every p>=11 the whole open R=p band
2<=kappa<ceil((p+1)/4) is excluded, for EVERY B.  The smallest cell p=11,kappa=2 (in particular B=1) is included without a
finite calculation.  Combining this candidate with the accepted R=p bands of I.14 would exclude every residual cell
R=p, kappa>=2 for p>=11.  The candidate itself proves only 1<=kappa<=(p-3)/2: it does NOT newly cover (p,kappa)=(5,2),
(5,3),(7,3).  It leaves R>p and unrestricted REFL-HI/RES-HI open.

The new step is the fixed half-cycle in C_(2p) followed by CONNECT and ILIFT.  It is not a stronger assumed rotation
rigidity or an unreviewed lift theorem.  The earlier arc-family cardinality obstruction remains valid for that method;
RP-LIFT does not use it, a sumset size estimate, or an import from STAB.

## 7. Review checklist / possible failure points

All of the following are proved above and should be checked independently by the parent's two CLI families:
1. FWIN's parity-sensitive equivalence (2u even-lift, subtraction of E), including E=0 and E=p.
2. CONNECT for the label-aware cyclic boundary graph, especially P to P^c and existence of an edge for each run index.
3. Uniqueness of integer increments in [-(p-2),p-2] modulo 2p; constants c_m may differ across layers and need not match.
4. LIGHT on the union of interior paths and the nonnegative coefficient 1-2f/n in SIGN, Case 3.
5. Flipping whole nonadjacent stretches in Case 2 removes exactly the intended boundaries; flipping interior independent
   vertices in Case 3 adds exactly the intended boundaries.
No computational probe or test was run; universal claims rest on this written argument, not on finite evidence.
