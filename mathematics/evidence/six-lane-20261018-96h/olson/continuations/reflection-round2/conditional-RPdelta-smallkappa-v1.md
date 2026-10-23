# CONDITIONAL ON RP-LIFT: the R = p + delta, small-kappa analogue and its neutral-even-run obstruction

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T08:31:29-0700, AFTER delivering
review-package-RPdelta-v1.md (02f1f12b...c62f6c49) and review-excerpts-RPdelta-v1.json (4e8099eb...e7bfd432).
Authorised next step: written R>p analogue, explicitly CONDITIONAL on the pending RP-LIFT proof.  No computation,
probes, tests, models or process launches.  This file is NOT an addition to either running review snapshot.

Status: CONDITIONAL_RESEARCH_CANDIDATE, NOT parent-accepted.  In particular, this is NOT a use of RP-LIFT as an accepted
fact.  The conditions are the correctness of CONNECT and LIGHT, and of the simultaneous-lift mechanism, in the frozen
proof-Rp-integer-lift-v1.md (34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69).  The bare statement of
RP-LIFT alone would not imply this note: the proof lemmas and the changed parameter checks below are essential.
Accepted imports, separate from these conditions: W, Fact2.1, Fact2.2 and P0/definitions, at the scopes of parent verdict
13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547.  No SEG-k/TRANSFER/region-B/B-prime or STAB premise.

## 1. Bounded target and notation

Prime p>=5; word length4p-2, rotations in one nonzero pair normalised to rho_1,rho_-1 and A>=B; every maximal cyclic
CONSTANT reflection block odd.  Let R=p+delta with delta>=1 and set
   M := 2p-R = p-delta,   k = M+2kappa,   1<=kappa<=floor((M-3)/2).
Thus M>=5 and R<=2p-5.  There is at least one genuine empty rotation run (as for a word in RES_<).  Runs are not required
to be pure, except when explicitly specialising to RES_<.
Success criterion for this note: identify exactly which run increments obstruct extending RP-LIFT's sign argument; do not
assert universal R>p exclusion.  In particular, a necessary structural family is not an actual avoider or a counterexample.

Use theta_i=y_(i-1)-y_i in Z_p, d_i=a_i-b_i, and e:Z_p -> C_(2p) the additive even-lift map.  Define
   alpha_i := e(theta_i)-d_i in C_(2p),
   psi(P) := -B + sum_(i in P)alpha_i = e(2u_P)-E+(P).
As before psi(P)+psi(P^c)=-R=M in C_(2p).  A ZERO increment is precisely a run for which
   d_i is even   AND   theta_i=d_i (mod p).                                                        (Z)
It cannot be empty: for an empty run d_i=0 and maximality gives theta_i!=0.
Every run with odd d_i has odd, hence nonzero, alpha_i.  No value-range rigidity of theta_i or d_i is assumed.

## 2. Fixed window and integer lift with M replacing p

The pattern range is
   L := kappa+1,   U := p-floor(R/2)=ceil(M/2).
Our kappa bound gives L<=U and 2m<k for every m in [L,U].  For every E in [0,R] and such m:
ceil(E/2)>=0>=kappa+1-m and floor(E/2)<=floor(R/2)<=p-m.  So Fact2.1 makes both endpoints floor-type, and
W kills exactly when psi(P) has a representative in [-R,0].
Detailed parity check: u_P belongs modulo p to [-floor((R-E)/2),floor(E/2)] iff some EVEN t in [-(R-E),E] reduces to 2u_P;
this iff t-E has class psi(P) and lies in [-R,0].  Conversely a representative s there gives even t=s+E with that value.
Since R<2p, the complement of these R+1 classes in C_(2p) is the interval [1,M-1].

Consequently an avoider supplies representatives N(P) in [1,M-1] for every P in each F_m, m in [L,U].  CONDITIONAL ON
CONNECT and the integer-lift argument of RP-LIFT: every index is toggled by an edge, and edge differences in
[-(M-2),M-2] determine the same integer h_i representing alpha_i modulo 2p on every edge.  Uniqueness is valid here too:
2M-3<2p.  Connectivity gives N(P)=c_m+sum_(i in P)h_i, with no identification of c_m across layers required.  Thus
   abs(sum_(i in P)h_i-sum_(i notin P)h_i)<=M-2                                                   (LIFT-M)
for all m in [L,U].  Empty runs give nonzero EVEN h_i with abs(h_i)>=2; odd d_i give nonzero ODD h_i.  Zero h_i occur
exactly at (Z).  This last possibility is the new issue absent at R=p, where every nonempty run is one letter.

## 3. Sign argument when there are no zero increments (conditional exclusion)

Here is the changed signed-sum calculation, stated separately to expose every change from RP-LIFT.
Suppose all h_i are nonzero, and some marked index (a genuine empty run) has abs(h_i)>=2.  Let E be ANY nonempty set of such
marked indices, e=|E|>=1; no assumption e=2kappa is needed.  Let S=sum abs(h_i)>=k+e.  Start from the signs of h_i, with
2m0 cyclic changes.
* L<=m0<=U: the signed sum is S>M-2.
* m0>U: as in RP-LIFT, flip the m0-U lightest stretches from the lighter parity class of the 2m0 alternating stretches.
  There remain exactly 2U changes and the signed sum is >=S U/m0>=2U>=M>M-2.
* 1<=m0<L: f=L-m0; interior set J (indices whose two neighbours share their sign) has n>=k-4m0 and
  n-2f>=M-2-2m0>=M-2-2kappa>=1.  CONDITIONAL ON LIGHT, choose independent F inside J of size f and weight <=f/n times W_J.
  Flipping F adds exactly 2f changes, giving exactly 2L.  With e_J=|E intersect J|,
  W_J>=n+e_J and W_(J^c)>=k-n+(e-e_J), and 1-2f/n>=0.  Thus the signed sum is >=
      k+e-2f-(2f/n)e_J >= k-2f = M-2+2m0 > M-2.
* m0=0: LIGHT on the full k-cycle with f=L gives signed sum >=S(1-2L/k)=S(M-2)/k>M-2 because S>=k+e>k.
So some pattern in the required range violates (LIFT-M).

**Conditional conclusion NER (no-neutral-even-run exclusion).**  Under the conditions at the top of this note, an avoider
must have an index satisfying (Z).  In particular, if every nonempty rotation run has ODD length, then no avoider exists:
on an odd-length run d_i has odd parity, so alpha_i is nonzero; every empty run also has nonzero alpha_i; Section3 then
contradicts (LIFT-M).  This is a word-structure exclusion, NOT universal coverage of an R=p+delta parameter cell.

The only conditions beyond accepted W/Fact2.1/P0 are the still-pending RP-LIFT CONNECT/LIGHT/simultaneous-lift lemmas and
the unreviewed M-version parameter/sign checks in this note.  No acceptance, finite proof or review is claimed.

## 4. The remaining family is small in run count, but not empty by assumption

For an avoider, P0 gives o_R>=k-2kappa=M.  If e_+ denotes the number of nonempty EVEN rotation runs, then
   R>=o_R+2e_+>=M+2e_+,  hence e_+<=(R-M)/2=delta.
The neutral-even indices (Z) are among these e_+ indices.  Thus NER would force at least one and at most delta such runs.
In a RES_< terminal word every run is pure or empty, so (Z) means a nonempty pure EVEN run, with
   theta_i=+r_i (mod p) for rho_1-runs, or theta_i=-r_i (mod p) for rho_-1-runs.
The selection of one reflection from each bounding block and ALL letters of the intervening run then has ordered
product sigma_(y_(i-1)) rho_(d_i) sigma_(y_i)=rho_(theta_i-d_i)=1, and has EVEN length r_i+2.  It is a SHORT identity
subword, not automatically the required length2p; no padding or avoidance-preserving replacement is assumed.

For delta=1 the conditional remaining shape is especially exact.  One nonempty even run must exist.  Since
R=p+1=M+2, that run has length2, there are exactly M=p-1 odd nonempty runs (all single letters), no other positive even run,
q=p, and g_E=k-q=2kappa-1.  If the word is in RES_<, the exceptional run is rho_1^2 or rho_-1^2 and its endpoints satisfy
   y_(i-1)-y_i=+2 or -2 (mod p), respectively.
This gives a four-letter identity selection across that run.  The cell is still OPEN: the four-letter identity is not a
length2p witness and is not a counterexample to REFL.

## 5. What remains and review boundary

This note isolates the neutral-even-run obstruction, at most delta positions, conditional on RP-LIFT's proof lemmas.
To exclude the remaining family one needs a justified move or a second family of patterns that uses the short identity
selections without losing the exact target length or the original order.  Replacing such a four-letter identity by four
equal reflections is NOT licensed by SPEC: it introduces size2 identity selections that need not exist before replacement.
No such move is claimed here.  No conclusion for kappa>floor((p-delta-3)/2), zero empty runs, or arbitrary R is drawn.
RP-LIFT remains in its separate dual review and is not promoted by this conditional note.  Full REFL/INV*/Olson remain open.
