# RPdelta with at most two neutral-even increments: delta = 1,2 small-kappa exclusions (candidate v1)

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:37:37-0700.  CANDIDATE_UNVERIFIED, written only:
no computation, finite search, model call, test/build or scientific process.  This continues scope-RPdelta-two-neutral-v1.md;
all previous files and the two current review snapshots remain unchanged.  This is NOT part of the frozen RPdelta package.

## 1. Statement and exact imports

**Theorem RP-2NE (candidate).**  Let p>=5 be prime and let delta be 1 or 2.  Let w be a word of length4p-2 over D_(2p),
with exactly R=p+delta rotation letters, all in one pair {rho_x,rho_-x}, x!=0.  Suppose every maximal cyclic CONSTANT
reflection block has odd length, and with H=sum floor(l_i/2), kappa=p-1-H:
   delta+1 <= kappa <= floor((p-delta-3)/2).
Then w contains exactly 2p letters in increasing original index order whose ordered product is the identity.
Any B, no purity, no inherited hypothesis or restriction on reflection values.  In particular:
- delta=1: 2<=kappa<=(p-5)/2;
- delta=2: 3<=kappa<=(p-5)/2.
Both ranges are nonempty first at p=11.  This does NOT prove unrestricted REFL/INV*/Olson and does not assert priority.

Accepted interfaces (only these):
V5 := /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md,
SHA256 13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547, with every binding reading S1/m1-m7 and all five
source errata.  Use W (all-odd H0 window), Fact2.1 (floor-type endpoints), Fact2.2/P0 (rotation-run counts).  Source:
proof-REFLHI-arcs-v5.md, 4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c, read through erratum5
40832206bf581a685266c4f885ecf2d3008e6e362b6a791acc11fa2527d325f4 and V5.
VL := /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-parent-verdict-v1.md,
SHA256 e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652, with all seven binding readings.  Its source:
proof-Rp-integer-lift-v1.md, 34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69, including CONNECT and LIGHT.
Use only CONNECT's literal generic statement (F_m connected and every run toggled for 1<=m,2m<k) and LIGHT's literal
nonnegative-weight averaging statement (n>=2f on a cycle or disjoint union of paths).  Both are restated below; the changed
R>p lift and sign argument with zero increments are proved here.  The R=p theorem itself is NOT assumed at R>p.

No SEG-k/TRANSFER/regionB/B-prime or STAB candidate is an import.  The earlier conditional-RPdelta-smallkappa-v1.md is
superseded for the exact cases covered here; nothing from it is assumed as a theorem.

## 2. Notation, parity-sensitive fixed window and the new integer lift

Normalise x=1 and A>=B (the accepted automorphisms preserve ordered identity selections and maximal block lengths).
Let R_i precede block S_i=sigma_(y_i)^(l_i), with l_i odd; a_i,b_i count rho_1,rho_-1 in R_i, r_i=a_i+b_i, d_i=a_i-b_i;
theta_i=y_(i-1)-y_i in Z_p, u_i=theta_i/2, and k is the number of blocks.  The maximal decomposition includes empty runs,
where r_i=0 implies theta_i!=0.  Set
   M:=2p-R=p-delta,   k=M+2kappa,   L:=kappa+1,   U:=p-floor(R/2)=ceil(M/2).
The hypotheses give M>=5, L<=U and 2m<k for every L<=m<=U (2U<=M+1<k).

P is any proper nonempty subset of all k run indices, including empty runs; m(P) counts its maximal cyclic intervals.
E(P):=A_P+B_(P^c)=B+sum_(i in P)d_i is an INTEGER in [0,R], E(P^c)=R-E(P).  The accepted W criterion says that membership
of u_P in I(P)=[-gamma_m(R-E),gamma_m(E)] modulo p produces an identity2p-subword, with
   gamma_m(E)=min(p-m,E-kappa+m-1,floor(E/2)).
For L<=m<=U and EVERY E in [0,R], ceil(E/2)>=0>=kappa+1-m and floor(E/2)<=floor(R/2)<=p-m; Fact2.1 therefore gives
I(P)=[-floor((R-E)/2),floor(E/2)].

Let C=Z/(2p)Z, let e:Z_p -> C be the additive even-lift isomorphism onto the even subgroup, and define
   alpha_i:=e(theta_i)-d_i in C,   psi(P):=-B+sum_(i in P)alpha_i=e(2u_P)-E(P).
The sum theta_i is zero, so sum alpha_i=-D, D=A-B, and psi(P)+psi(P^c)=-R=M in C.
The W window kills exactly when psi(P) has an integer representative in [-R,0].  To check both directions: u_P hits I(P)
iff an EVEN t in [-(R-E),E] represents 2u_P modp; its class in C is e(2u_P), so t-E represents psi(P) in [-R,0].  Conversely
such a representative s gives t=s+E in that range, with even parity because its class is e(2u_P), and t/2 belongs to I(P).
As R<2p, the classes outside [-R,0] are exactly [1,M-1].  Thus if w avoids, for every pattern P in each F_m (L<=m<=U),
   psi(P) has a unique representative N(P) in [1,M-1].                                                       (1)
This is a new R>p parameter check, not an enlarged statement of RP-LIFT.

**CONNECT (accepted instance, VL).**  F_m is connected by one-index toggles, including P to P^c, and every index is toggled
by an edge, whenever 1<=m,2m<k.  Its proof uses labeled boundary particles, lifted coordinates
x_1<...<x_(2m)<x_1+k and coordinate-minimum connectivity.  Read its decreasing-step sentence as keeping the preceding gap
>=1, not preserving its value; all seven VL bindings apply, including cyclic-order avoidance and adjacency of interior paths.

For an edge adding i, N(P union{i})-N(P) represents alpha_i modulo 2p and lies in [-(M-2),M-2].  This interval has
2M-3<2p integers, so there is at most one representative of alpha_i in it; every index has such an edge by CONNECT.
Call that representative h_i.  Every adding edge has increment h_i, and every removing edge -h_i, in every F_m.  Connectivity
therefore gives a constant c_m with
   N(P)=c_m+sum_(i in P)h_i.
No equality of constants across layers is needed.  Since P^c is in F_m, the constants cancel and
   abs(sum_(i in P)h_i-sum_(i notin P)h_i)<=M-2                                                           (2)
for all L<=m(P)<=U.  Also h_i=0 iff alpha_i=0.  Its parity is that of d_i (2p is even); an empty run has a nonzero EVEN
h_i, so abs(h_i)>=2; odd-length runs have odd d_i and hence odd, nonzero h_i.

## 3. At most two zero increments, and enough nonzero even ones

A zero h_i is exactly
   d_i even AND theta_i=d_i modp.                                                                         (NE)
It is not an empty run (maximality gives theta_i!=0 there), so it is a NONEMPTY EVEN rotation run.  Let z be the number of
zeros, v the number of nonempty even rotation runs, o the number of odd rotation runs, g_E the number of empty runs, and q=o+v.
(P0) with all blocks odd gives o>=k-2kappa=M.  Since R>=o+2v, v<=delta, so z<=v<=delta<=2.  Moreover R>=q+v gives
   g_E=k-q>=k-R+v=2kappa-2delta+v,
   g_E-z>=2(kappa-delta)+(v-z)>=2.                                                                         (3)
Thus the empty-run indices form a marked set Z of size e=g_E strictly GREATER than z.  They are disjoint from the zeros and
have abs(h_i)>=2; every other nonzero h_i has absolute value>=1.  In particular
   S:=sum abs(h_i)>=k+e-z>k.                                                                              (4)
This is the new source of slack even when neutral-even increments are present.

## 4. A cyclic sign lemma allowing up to two zeros (new)

**LIGHT (accepted, VL).**  On an n-cycle, n>=2f, f>=1, there is an independent f-set of weight at most f/n times the total
nonnegative weight.  Proof reminder: average all n cyclic translates of {0,2,...,2(f-1)}, whose wrapping gap is >=2;
each vertex belongs to f translates.  On a disjoint union of paths concatenate the paths into a cycle (only adding edges).
Independence on that cycle implies independence on the paths.

**SIGN-2Z.**  Let M>=5 be an integer (not assumed prime), 1<=kappa<=floor((M-3)/2), k=M+2kappa, L=kappa+1,
U=ceil(M/2).  Let h_i be integers on the k-cycle with at most z<=2 zeros.  Suppose a marked set Z of e>z indices is disjoint
from the zeros, abs(h_i)>=2 for i in Z, and abs(h_i)>=1 on every other nonzero index.  Then a sign vector s_i in {+1,-1}
with between 2L and 2U cyclic changes has
   sum_i s_i h_i > M-2.                                                                                   (5)
Proof.  Put w_i=abs(h_i), S=sum w_i>=k+e-z>k.  Start with s_i=sign(h_i) for nonzero h_i and assign either sign to every zero;
its signed sum is S.  Let the number of changes of this initial cyclic sign vector be 2m0 (m0=0 for one sign throughout).

Case A: L<=m0<=U.  S>k>=M>M-2; the initial signs work.

Case B: m0>U.  The 2m0 maximal constant-sign stretches alternate.  At most z stretches can have zero total weight (each
such stretch contains a zero index, and different stretches are disjoint); every other stretch has weight>=1, so
S>=2m0-z.  Choose the odd- or even-numbered family of m0 stretches of smaller total weight (<=S/2) and flip the
f=m0-U lightest stretches in that family.  They are nonadjacent, f<m0, and each removed boundary touches only one flipped
stretch, so the result has exactly 2m0-2f=2U changes.  Flipped weight<=f S/(2m0), and the new signed sum is >=S U/m0.
If z=0 this is >=2U>=M.  If z=1 or2, it is >=2U-z U/m0>2U-z>=M-2, since m0>U.  Thus (5) holds.

Case C: 1<=m0<L.  Put f=L-m0.  Let J contain indices whose two neighbours have the same initial sign as the index; it is
the union of interiors of the 2m0 stretches.  Each stretch has at most two noninterior indices, so n=|J|>=k-4m0 and
   n-2f>=M-2-2m0>=M-2-2kappa>=1.
The interiors are disjoint paths.  Apply LIGHT to choose an independent Phi subset J of f indices with weight
<=f/n times W_J=sum_(i in J)w_i.  Interior-path independence implies original-cycle independence because stretch endpoints
are excluded (VL binding5).  Flipping Phi adds exactly 2f boundaries (both neighbours of a flipped index share its old sign
and are unflipped), giving 2L changes.  Put gamma=2f/n<1, e_J=|Z intersect J| and z_J=number of zero indices in J.
The new signed sum is >= W_(J^c)+(1-gamma)W_J.  The pointwise baseline
   w_i>=1+1_(i in Z)-1_(h_i=0)
gives W_J>=n+e_J-z_J and W_(J^c)>=k-n+(e-e_J)-(z-z_J).  Since 1-gamma>0, the sum is >=
   k+e-z-2f-gamma e_J+gamma z_J
   >=k-2f-z+(1-gamma)e
   =M-2+2m0-z+(1-gamma)e > M-2,
because 2m0-z>=0, e>=1 and 1-gamma>0.  The strict coefficient is why the written kappa upper bound is retained.

Case D: m0=0.  Apply LIGHT on the full cycle with f=L (k>=2L as M>=5).  Flipping that independent set yields 2L changes
and signed sum >=S(1-2L/k)=S(M-2)/k>M-2 by S>k and M-2>0.  This proves the lemma in all cases.  []

## 5. Proof, exact coverage delta, and boundaries

If w under RP-2NE avoided, Sections2-3 would produce integers h_i satisfying (2) and SIGN-2Z's hypotheses: z<=delta<=2 and
marked empty-run set Z of size e=g_E>z.  Lemma SIGN-2Z gives signs s_i with 2m changes for some L<=m<=U and a signed sum
>M-2.  Its positive set P is a proper nonempty pattern in F_m; its signed sum is
sum_(i in P)h_i-sum_(i notin P)h_i, contradicting (2).  Therefore w is solvable.  Cyclic rotation gives an increasing-original-
index identity selection by conjugation, exactly as in VL binding1.  []

The universal new cells, relative to accepted V5 I.14 numerical bands (not relative to every accepted structural or B=0
criterion), are precisely the following set differences.  Put
   A(p,delta)=[ceil((p+3delta+2)/4),floor((p-delta-4)/2)]_Z
              union [ceil((p+delta+1)/2),p-delta-3]_Z.
For delta=1, the new candidate range is [2,(p-5)/2]_Z; its new part is
   [2,min((p-5)/2,ceil((p+5)/4)-1)]_Z.
For delta=2, the new range is [3,(p-5)/2]_Z; its new part is
   [3,min((p-5)/2,ceil((p+8)/4)-1)]_Z union {(p-5)/2}, for p>=11.
The second isolated endpoint is above SEG-num's upper endpoint (p-7)/2; the K2P+ band is above both candidate ranges.
Examples of newly excluded numerical cells (arithmetic of statements only, no search):
   p=11,delta=1,kappa in {2,3}; p=11,delta=2,kappa=3;
   p=13,delta=1,kappa in {2,3,4}; p=13,delta=2,kappa in {3,4}.
Every claim is any-B; RES_< consequences of course retain B<kappa and pure/empty runs.

At delta=1 this removes the neutral length2-run obstruction identified in the earlier conditional note: zeros are now
allowed in the sign argument.  No local replacement, fusion, padding or new avoidance-preserving move is used.
At delta=2,kappa=2 the proof does NOT claim a contradiction: (3) gives e>=z rather than e>z, and the all-one-sign Case D can
meet its bound with equality.  This is a failure of this sufficient sign estimate, not an actual avoider of the cell.
For delta>=3 Case C can have 2m0-z<0 and Case B's lower estimate need not exceed M-2; those cases remain open here.
No claim outside kappa>=delta+1, 2kappa<=p-delta-3 is made, and unrestricted REFL/INV*/Olson stay open.

Review focus: (a) new fixed C_(2p) window with R=p+delta and M=p-delta; (b) zero-increment criterion and the counts
z<=v<=delta, e-z>=2(kappa-delta); (c) nonnegative pointwise baseline for zero vertices in SIGN-2Z, especially Case C's strict
n-2f>=1 and Case B's S>=2m0-z; (d) complement cancellation needs no equality of c_m across layers; (e) no RP-LIFT theorem is
used outside R=p, only CONNECT/LIGHT within their literal general ranges.  Parent owns dual reviews and final verdict.
