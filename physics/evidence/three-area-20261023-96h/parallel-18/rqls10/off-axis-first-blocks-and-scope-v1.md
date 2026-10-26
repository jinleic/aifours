# Uncovered all-rook off-axis orientation: exact first-block freeze v1

PhysicsRQLS10, same physics-5 primary. Author-written CANDIDATE. Stage clock observed before derivation:2026-10-24T04:01:18-07:00. No scientific program, arithmetic interpreter, enumeration, compilation, solver, CLI or old runtime executed.

## Literal input and unchanged goal

Keep the same literal Et-Taoui C=(J-I+sQ0)/sqrt8 on F9 labels x+3y, s=i sqrt7. Choose

    rho_off=(0,7,8,6,5,4,3,1,2),
    H={4,5}, J={3,6}, U={1,7}, V={2,8}.

The oriented representatives are4→5,3→6,1→7,2→8 in pair order(H,J,U,V). The horizontal H lies in row1, away from the missing point0. J is the column0 vertical pair; U,V are the other vertical pairs with row1 removed. All four pair edges are rook-positive.

The orientation-level target retains **EVERY** second literal C'=PCP^T and arbitrary independent complex diagonal D/E. These are necessary local equations within the same maximal1-RQLS10 problem, not a new problem or a replacement of its100 pairwise-nonparallel-ray/ONB target. The first bounded attack below treats one genuine low-rank core; that is not silently substituted for the all-P goal. The full QLS10 target remains UNKNOWN.

## Exact paired coordinates and first matrices

The even basis has fixed coordinate0 then four pair means; the odd basis has the four pair differences. Thus G_E=diag(1,2,2,2,2), G_O=2I, and

    Q0=[E0 B0; B0^T G_E/2 O0].

The pair tags give D0=I and

    A0=[0 0 0 0;
        0 0 1 1;
        0 1 0 2;
        0 1 2 0],   O0=-I+A0.

The full even5×5 block, in order(0,H,J,U,V), is

    E0=[ 0 -2  2  0  0;
        -1  1  0  0  0;
         1  0  1 -1 -1;
         0  0 -1  1  0;
         0  0 -1  0  1].

The full5×4 mixed block is

    B0=[ 0  0  2  2;
         0  2  0  0;
         0  0 -1 -1;
         2 -1  0  0;
        -2 -1  0  0].

For example the U,V fixed-row differences are2 because the first endpoint is an axis neighbour of0 and the second a diagonal non-neighbour. The H column has opposite2,-2 means at U,V; the J column has2 at H and-1 at each heavy leaf. Every column obeys h_fixed+2sum(h_pair)=0. These are actual auxiliary-character coordinates, not an assumption that the physical phases are real.

The three distinct mixed columns are independent; U and V columns coincide. Hence rank B0=3 and its kernel is span(e_U-e_V). Directly

    (B0^T G_E B0)/2=9I-O0²,

with eigenvalues8,6,6,0. The odd spectrum is-1 on H, -3 on U-V and±sqrt3 on the other triangle directions. No first-rank-one mixed-column shortcut from the old axial proof survives.

## Proof this input is outside the covered normalization orbit

The parent-supported monomial/conjugating bridge classifies all allowed independent-phase self-normalizations of this literal C: their nontrivial actions preserve or negate Q and transport rho by conjugation. Under that action the rho-even and rho-odd spaces are carried isomorphically to the transported spaces, and Q changes by at most a global sign. Therefore the rank of the even/odd mixed block of Q is invariant.

For central rho(t)=-t, Q commutes with rho and that rank is0. For the positive axial orbit it is1, and the conjugating negative-axis orbit also has rank1. The present rank3 cannot belong to any of those covered orbits. Independently, its nonzero A0 magnitudes are(2,1,1), not the axial triangle's(2,2,2). This is a genuine uncovered orientation under the proved full monomial-plus-conjugating class, not merely a different tuple in the old orbit.

The ordinary point0 group has an orbit of four such off-axis all-rook matchings (row level±1 and optional coordinate interchange), with the present matching fixed by the literal x-reflection. Its complementing orbit has four all-nonrook images. A future complete closure here would therefore add an eight-element fixed0 orbit; **that closure is not yet claimed**.

## Actual new phase system, not a frozen ansatz

For an arbitrary second Q1=P Q0 P^T define its actual E1/B1/O1 and tags D1. The exact gluing expansion remains

    M=N+sM1+s²M2,
    N=J-I-P_rho+Fix(rho),
    M1=(P_rho Q1-Q0-D1+D0 P_rho)/8,
    M2=(N-Q0 o(P_rho Q1))/8.

The leading odd coefficient is-(A0+A1)/8. Both independent mixed operator coefficients remain

    (M1)_EO=(B1-B0)/8,
    (M1)_OE=-(B1+B0)^T G_E/16.

They are not negatives of metric transposes. The first B0 is the rank3 matrix above; B1 is still unrestricted genuine second-core data. The general rank>=8 common-norm obstruction remains available for this fixed-point type, but its rank premise must be proved with these actual blocks.

The first bounded attack takes the genuine second C'=conjugate(C), which belongs to the literal family by the nonsquare R. For ANY rho of this type its paired M rows coincide, so rank M≤5; N has rank5 modulo(s), hence actual rank M=5 and the entire complex kernel has dimension4. This cannot be excluded by the rank8 lemma or by simply assuming projective K phases. The companion manuscript derives an exact full-unit-torus obstruction for this rank5 case. The other second cores remain part of the orientation-level obligation.
