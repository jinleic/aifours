# RQLS10 v35 — literal100-DISTINCT-ray QLS10 from two Petersen Hadamards, but TEN cells lie on NO quantum transversal

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 09:14:46 PDT 2026**. AUTHOR-WRITTEN exact finite construction/obstruction, NOT an original100-ray1-RQLS witness or accepted finite-witness result. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty claim; executable independent-checker/control/vendor/priority gates have NOT been performed underHOLD and are NOT called passed.

## 1. Literal positive object and exact negative original-model application

We construct a10x10 array of one hundred DISTINCT normalized complex rays in C10, with all ten rows and all ten columns ONBs. Unlike merely a finite partial sector, this is a COMPLETE maximal-cardinality QLS10 at the AUTHOR-WRITTEN level.

However, EACH of its ten diagonal cells is orthogonal ONLY to other cells in its OWN row or column. No quantum transversal can contain ANY diagonal cell. Therefore the array admits NO full allowed resolution of the original kind, whether covariant, cyclic or completely symmetry-breaking. It is NOT a maximal1-RQLS10 witness.

The proof also classifies ALL central complex Hadamards in the SAME Petersen-duad coordinates and excludes the ENTIRE two-central-Hadamard Schur construction for maximal1-RQLS10: same-category pairs have duplicates; cross-category pairs have100 distinct rays but the untransversalizable diagonal obstruction. Arbitrary INDEPENDENT column permutations of the two Hadamards change their coordinate pairing and are NOT covered or declared WLOG.

## 2. Complete exact matrix ingredients

Index the ten coordinates/rows/columns by duads a of{1,2,3,4,5}. Let P be disjointness adjacency(Petersen), B=J-I-P. It has3 disjoint neighbors and6 distinct intersecting neighbors per duad. Direct counting gives

    P^2=2I-P+J,     PJ=JP=3J.

Thus P is real symmetric with eigenvalue3 on the all-ones line, and1,-2 on its orthogonal complement. Their multiplicities are5 and4, from dimension and trP=0. B has corresponding eigenvalues6,-2,1.

Put

    r=(-1+i*sqrt15)/4,       |r|=1, Re(r)=-1/4,
    H=I+iP-iB,
    K=I+rP+conj(r)B.                             (HK)

These are literal10x10 matrices with unit-modulus entries, NOT unnamed catalogue objects. At the eigenvalues(3,1,-2) of P, H has eigenvalues

    1-3i,      1+3i,      1-3i,

each of squared modulus10. K has eigenvalues

    (-5-3i*sqrt15)/4,
    ( 5+3i*sqrt15)/4,
    ( 5-3i*sqrt15)/4,

again all squared modulus10. Hence HH^dagger=KK^dagger=10I. All arithmetic is exact WRITTEN reasoning, not matrix code output.

The conjugate choices r->conj(r), i->-i work identically. Define the relation exponent

    epsilon_a(s)=0 if s=a;
                 +1 if s disjoint from a;
                 -1 if s intersects a and differs.

Then K_(a s)=r^epsilon_a(s), H_(b s)=i^epsilon_b(s).

## 3. The COMPLETE one-hundred-ray roster and row/column proof

For EVERY ordered pair(a,b) of the ten duads define

    q_(a,b)(s)=r^epsilon_a(s)*i^(-epsilon_b(s))/sqrt10,
                  for EVERY coordinate s.       (QLS100)

This formula is the entire100-ray roster; there are no unspecified phases or numerical samples. All entries have squared modulus1/10. For fixed a, its ten vectors are obtained from the conjugate rows of H/sqrt10 by the same unitary coordinate diagonal diag(K_a). Hence that ROW is an ONB. For fixed b, they are obtained from the rows of K/sqrt10 by diag(conj(H_b)), so that COLUMN is an ONB. This verifies the actual row/column conditions, not just counts.

### 3.1 r is NOT a root of unity

It satisfies2r^2+r+2=0 and r+r^-1=-1/2. If it were a root of unity, r and r^-1 would both be algebraic integers, so their rational sum-1/2 would be an algebraic integer. A rational algebraic integer is an integer, contradiction. In particular r^m=i^n with integer m!=0 is impossible, since the right side is a root of unity.

### 3.2 ALL one hundred projective rays are distinct

Suppose q_(a,b)=lambda*q_(c,d). Taking ratios of two physical coordinates s,t removes lambda and gives

    r^[(epsilon_a(s)-epsilon_c(s))-(epsilon_a(t)-epsilon_c(t))]
       =i^[(epsilon_b(s)-epsilon_d(s))-(epsilon_b(t)-epsilon_d(t))].

By section3.1 the integer exponent of r must vanish. Thus epsilon_a-epsilon_c is CONSTANT across every coordinate. If a!=c, evaluating at s=a and s=c gives opposite values-h,+h, where h=epsilon_a(c)=epsilon_c(a) is+1or-1. They are not equal. Hence a=c.

Then the assumed equality says two H rows are proportional. They are orthogonal unless b=d, so b=d. Thus the cell pair is identical and ALL hundred rays are distinct up to arbitrary global phase. No machine checker, finite search or minimum-distance approximation was used.

## 4. ENTIRE no-transversal proof for EVERY diagonal cell

Let q_(a,a) be any diagonal cell. Compare it to an arbitrary q_(c,d) with c!=a and d!=a, precisely the other-cell condition required in a row-and-column transversal through(a,a). Their inner product is

    (1/10)sum_s r^Delta_s * i^(epsilon_a(s)-epsilon_d(s)),
    Delta_s=epsilon_c(s)-epsilon_a(s).            (INNER)

Put h=epsilon_a(d)=epsilon_d(a), which is+1or-1. For all s EXCEPTa,d the exponent epsilon_a(s)-epsilon_d(s) is even(0,+2,-2), so the corresponding i-factor is REAL, +1or-1. At s=a the factor is i^-h=-h*i; at s=d it is i^h=h*i. Thus INNER times10 has the exact field decomposition

    R(r)+h*i*[r^Delta_d-r^Delta_a],
    R(r) in F=Q(r)=Q(sqrt(-15)).                  (FIELD)

Crucial: this is a decomposition in the quadratic field extension F(i)=F directsum iF, NOT an ordinary real/imaginary-part split. Since F and Q(i) are distinct quadratic fields, i is NOT in F and the two F-components are linearly independent. Therefore vanishing would force

    r^Delta_d=r^Delta_a,
    Delta_d=Delta_a,

where the second conclusion uses r not being a root of unity.

But Delta_a=epsilon_c(a) is ODD, either+1or-1. If d=c, then Delta_d=-epsilon_a(c)=-Delta_a, unequal. If d!=c, then d differs from BOTH a,c and Delta_d is the difference of two signs, hence EVEN(0,+2,-2), again unequal to Delta_a. These are ALL possibilities because d!=a was required.

Consequently q_(a,a) is NOT orthogonal to ANY cell outside its own row and column. Since its row and column are ONBs, its orthogonality neighbors are exactly the other18 rook cells in those contexts. A quantum transversal through(a,a) would require its other nine rays to be outside that row AND column and orthogonal to q_(a,a), impossible.

This holds for EACH of the ten diagonals. No full resolution can cover all cells. The failure is stronger than lack of an A5-covariant resolution(v34): NO symmetry-breaking or other allowed full resolution exists for this actual100-ray array.

## 5. COMPLETE central-Hadamard classification and whole two-matrix family

Any A5-invariant entrywise-unit matrix in these SAME coordinates is, after one common phase normalization,

    M=I+xP+yB,       |x|=|y|=1.

These are exactly the matrices constant on the three ordered-pair duad orbits; no global row/column equivalence is assumed. For it to be Hadamard, its eigenvalues at P=1,-2 must have squared modulus10:

    |1+x-2y|^2=10,
    |1-2x+y|^2=10.

Write u=Re(x),v=Re(y),w=Re(x*conj(y)). Expanding gives

    u-2v-2w=2,
    -2u+v-2w=2.

Hence u=v and u+2w=-2. Unit complex numbers of equal real part satisfy y=x or y=conj(x). The first gives u=-4, impossible. The second gives w=2u^2-1 and therefore4u^2+u=0. Thus the ONLY possibilities are

    x=+i,y=-i;    x=-i,y=+i;
    x=r,y=conj(r); x=conj(r),y=r.

The all-ones eigenvalue also has squared modulus10, either directly as in section2 or by traceMM^dagger=100 and the printed other multiplicities5,4. Thus these are ALL central Hadamards in the literal coordinate system.

For a pair K,H in the Schur construction q_(a,b)=K_a*conj(H_b)/sqrt10:

- If the two matrices are in the SAME two-element category(conference or r), they are equal or conjugate. Equality makes ALL ten diagonal rays the same uniform ray. Conjugacy makes q_(a,b)=q_(b,a), repeating offdiagonal rays. Neither is maximal.
- If they are in DIFFERENT categories, the case K=r-type,H=conference is exactly sections2–4, including BOTH sign choices. The opposite category order is obtained by array transposition plus complex conjugation, preserving row/column/resolution conditions and ray distinctness. It therefore has the same nonresolvability.

This exhausts the ENTIRE two-central-Hadamard family at the stated common coordinate pairing. Independent row phases/permutations, common column permutations, arbitrary column phases on either matrix(which act as a common coordinate diagonal on the array), and any common unitary applied to the resulting ray array preserve the conclusion. Arbitrary RELATIVE column permutations of K and H are a DIFFERENT unclassified pairing and have NOT been excluded.

## 6. Original gap, review contract and assurance

The positive claim is a full literal100-distinct-ray QLS10, NOT a1-RQLS10. The negative claim excludes ALL allowed full resolutions for the cross-category arrays and ALL maximal1-RQLS candidates from the entire SAME-coordinate central-Hadamard pair family. Both require an ENTIRE review: exact matrix/eigenvalue/unitarity ingredients; ALL100-ray distinctness; field-independence/non-root-of-unity argument; ALL diagonal/offcell cases; complete central matrix classification and equal/conjugate/cross-category application. A row/column norm check or chosen-transversal test is not the result.

No unprovided quantum-Latin/Hadamard/finite-geometry classifier is an operative premise. Only the exact Petersen adjacency identity, elementary simultaneous spectral decomposition and elementary quadratic-field/algebraic-integer facts printed here are used. The finite-witness skill's executable independent-checker/control/vendor/priority gates remain NOT PERFORMED underHOLD. No scientific execution or private approximate scout. No accepted witness/novelty/current-openness/formal/kernel/family/human promotion.

The original maximal100-ray1-RQLS10 remains UNKNOWN. The full TypeIV biunitary master outside this pair construction, mixed TypeI/TypeII/III and arbitrary noncovariant intrinsic10/4+6/5+5 possibilities remain OPEN. The next scientific step must replace the closed pair construction (for example a genuinely different relative pairing or full master seed), not test another resolution on these already-untransversalizable cells. All prior process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early pending-review park.
