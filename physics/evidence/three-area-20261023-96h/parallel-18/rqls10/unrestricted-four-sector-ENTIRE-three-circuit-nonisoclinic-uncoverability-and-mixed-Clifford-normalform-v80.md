# RQLS10 v80 — ENTIRE three-circuit mechanism: nonisoclinic cells are uncoverable; only the mixed-chirality Clifford residual survives

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 17:34:34 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, no machine/kernel checking. All calculations below are displayed symbolic written identities, not scientific Eval/CAS/interpreter/program/solver/replay, approximate scouts or chosen physical controls/probes.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 are UNCHANGED. No automatic admission/read/adoption or verdict inheritance.

## 1. Entire residual and two elementary actual-plane facts

Use ENTIRE v76/v77 actual all-SPARSE trueE4 graph/frame facts and v79. For an original MAX1 array with EXACTLY THREE actual circuits, v79 forces the circuit-intersection graph to be the 2+2+1 triangle. Name its rank2 projection pairs P,Q,R so that the P/Q and P/R classes each contain TWO original row-pair vertices, whereas Q/R meets at the SINGLE remaining vertex w. P/Q and P/R are independently interior-isoclinic. No equality of their angles, global tensor ansatz, actual frame, original graph ordering or E6 complement is selected.

FACT A: ANY two circuit pairs meeting at an actual sparse vertex have BOTH principal-angle compression eigenvalues strictly between 0 and 1. Indeed choose the local v77 sparse form with P=span(e1,f1), Q=span(e3,f3), local plane S=span(e1,e2), and S-perp=span(e3,e4). The two local 2-by-2 unitary blocks have ALL entries nonzero and of modulus less than one; otherwise an entry of modulus one repeats an actual cell ray. On S the lines of P,Q are e1,f3, and on S-perp they are f1,e3. The two compression eigenvalues are exactly these two squared overlaps, both in (0,1). Relabeling a projection with its complement only replaces an eigenvalue by 1 minus it. This pays all endpoints using ACTUAL frames, rather than excluding them generically.

FACT B: ANY quantum transversal in an ordinary MAX100 all-SPARSE array contains at most ONE actual ray in each ORIENTED circuit plane P_C or I-P_C, across ALL intersections. At one vertex the two rays in that plane are in the SAME actual column. At distinct vertices they are two actual orthonormal bases of that SAME two-dimensional plane. If an actual ray at one vertex were orthogonal to an actual ray at another, uniqueness of the orthogonal partner in dimension two would duplicate the partner cell ray at the first vertex. MAX forbids that duplication. This fact uses actual distinct columns and ordinary maximality, not a global common rank2 sector.

## 2. The P reflection commutes with the Q/R central CS operator

Set A=2P-I, B=2Q-I, C=2R-I. Interior-isoclinicity of P/Q and P/R means

    AB+BA=2a I,    AC+CA=2b I,    -1<a,b<1.

Directly expanding gives

    A(BC+CB)=(BC+CB)A:
    ABC=2a C-2b B+BCA,
    ACB=2b B-2a C+CBA.

Thus A commutes with Z=(Q-R)^2=(2I-BC-CB)/4. B and C commute with Z as well by their two-projection identity. These written identities do not require Q/R to be isoclinic.

Suppose Q/R has UNEQUAL compression eigenvalues mu0,mu1. Its central CS planes H0,H1 are the two distinct eigenspaces of Z, each dimension two. All three P,Q,R preserve H0,H1. P has rank ONE on each plane: if A on either plane were I or -I, its anticommutator with the rank1 reflection B there would force B to be scalar a or -a, impossible for |a|<1. The Q/R CS form already gives rank1 restrictions for Q,R.

## 3. In the nonisoclinic Q/R branch, every w-cell is missing from EVERY quantum transversal

Use a P/Q isoclinic identification H4=C2_first tensor C2_second so P=p+ tensor I, Q=q+ tensor I. Since the central planes commute with P,Q, choose its second basis e0,e1 so H_s=C2 tensor e_s. On each H_s, R is a rank1 qubit projection with rays r_s+,r_s-. Fact A and P/R isoclinicity make EVERY overlap of r_s+/- with p+/- and q+/- nonzero. The q and p bases also have all cross-overlaps nonzero.

At the lone Q/R vertex w, the unequal CS eigenvalues and the actual local commuting rank2 projection force the eight local rays to be EXACTLY

    q+/- tensor e_s,    r_s+/- tensor e_s,    s=0,1.

This is the local unequal-angle construction, not a common projector on all actual rays. At each P/Q vertex, the eight rays are {p+/-,q+/-} tensor {u,u-perp}. Both coordinates of EACH such second ray in e0,e1 are nonzero: a canonical e_s would duplicate the actual q+ tensor e_s ray already at w.

Consequently NO ray from either P/Q vertex is orthogonal to ANY w-ray of type r_s+/- tensor e_s: its first overlap is nonzero by Fact A and its second coordinate is nonzero. A P/Q ray orthogonal to the w-ray q_t tensor e_s must instead have first factor q_-t, hence belong to the OPPOSITE Q oriented plane.

Repeat the SAME argument in a P/R isoclinic identification. Its central planes are again H0,H1 because Z commutes with P,R. Its second bases at the P/R vertices have both central coordinates nonzero, since a canonical coordinate would duplicate a w-ray of R. Fact A now implies that NO ray at either P/R vertex is orthogonal to ANY w-ray belonging to an oriented Q plane. This is a separate pair identification, NOT a simultaneous global product assumption.

Consider a quantum transversal containing one w-ray in a Q plane. It has NO E4 ray from the P/R class. All its E4 rays from the P/Q class must lie in the same opposite Q oriented plane, so there is at most ONE of them by Fact B. The w vertex has only TWO original rows and therefore supplies at most TWO selected E4 cells in total. This bounds its E4 contribution by at most THREE, whereas a full quantum transversal must supply FOUR E4 rays. Contradiction.

Interchanging Q,R gives the same contradiction for a w-ray in an R plane. EVERY one of the eight actual w cells is therefore absent from EVERY quantum transversal in this branch. In particular no full TEN-class resolution can cover them. This excludes the ENTIRE unequal-angle Q/R branch for original MAX1, all complex frames and all mu0,mu1 in (0,1), without asserting that transversals avoiding w do not exist.

## 4. All THREE pairs must therefore be interior-isoclinic; exact Gram/Clifford reduction

For original MAX1 with three actual sparse circuits we now require

    AB+BA=2a I,    AC+CA=2b I,    BC+CB=2c I,
    a,b,c in (-1,1).

The REAL symmetric Gram matrix G with diagonal 1 and off-diagonal a,b,c is positive semidefinite: for all real x,y,z, the Hermitian square (xA+yB+zC)^2 equals ((x,y,z)G(x,y,z)^T)I. Its rank is at least two since |a|<1.

Put s=sqrt(1-a^2)>0 and B0=(B-aA)/s. Then B0 is a Hermitian reflection anticommuting with A. The two are unitarily sigma_z tensor I2 and sigma_x tensor I2: split A's two eigenspaces; B0's off-diagonal unitary identifies them. This is a DERIVED simultaneous representation for TWO anticommuting reflections, not a selected Pauli control.

Define d=(c-ab)/s and X=C-bA-dB0. The pair anticommutators give {X,A}={X,B0}=0 and

    X^2=(1-b^2-d^2)I = e^2 I,    e^2>=0.

If e=0, Hermiticity and X^2=0 imply X=0, and ALL three reflections act on the same first qubit tensored with I2. If e>0, D=X/e is a Hermitian reflection anticommuting with A,B0. In the displayed coordinates it MUST have form sigma_y tensor T: anticommutation with sigma_z forces off-diagonal blocks; anticommutation with sigma_x makes the off-diagonal block skew-Hermitian; D*=D and D^2=I make T a Hermitian unitary on C2. These are all possibilities, including degenerate scalar T.

## 5. Every common-first-qubit branch has NO quantum transversal

If e=0 OR T=I OR T=-I, all three circuit projections have a common representation as qubit rank1 projections tensor I2. At each of the five actual vertices, its local commuting projection is I2 tensor |u_v><u_v| and its eight rays are its two incident qubit bases times {u_v,u_v-perp}, by the same actual-frame argument as v78/v79.

ANY two vertices among the three pair classes share a circuit. A coincidence between their second-factor rays would therefore repeat an actual product ray by fixing that shared circuit's plus first factor. Thus ALL TEN second-factor rays at the five vertices are distinct and all cross-vertex second overlaps are nonzero. This uses the actual THREE-circuit incidence, not an assumption for an arbitrary larger circuit family.

Exactly as in v79's partial-transversal lemma, first-factor spans of distinct selected vertex groups must then be pairwise orthogonal in C2. At most two groups occur. Three selected cells would force two with the SAME first factor at one vertex, which belong to the SAME incident column; a single vertex has only two actual rows. Thus there is not even an orthogonal distinct-row/column subset of size THREE in the entire forty-cell E4 sector. In particular there is NO quantum transversal, which requires FOUR sector rays.

This closes ALL rankG=two and ALL scalar-chirality representations, not just a special angle/phase choice. No actual frame parameter or control has been selected.

## 6. ENTIRE three-circuit residual is necessarily positive-Gram MIXED chirality

The only Hermitian-unitary T on C2 not already excluded has eigenvalues +1,-1. A unitary on the second factor diagonalizes it to sigma_z. Thus EVERY surviving original three-circuit candidate admits the EXACT necessary operator normalform

    A = sigma_z tensor I2,
    B = (a sigma_z+s sigma_x) tensor I2,
    C = (b sigma_z+d sigma_x) tensor I2 + e sigma_y tensor sigma_z,
    s=sqrt(1-a^2),  d=(c-ab)/s,  e=sqrt(1-b^2-d^2)>0.

Here a,b,c are ALL variables, in (-1,1), and G is positive definite. The projections are P=(I+A)/2,Q=(I+B)/2,R=(I+C)/2. The mixed chirality is DERIVED as a necessary surviving representation; neither a chosen model nor proof that its actual local ray frames/full Latin resolution exist. Arbitrary complex local frames in the separate pair commutants remain to be glued across the five row-pair vertices. In particular no simultaneous common-first-qubit interpretation is available in this residual.

## 7. Claim boundary and exact imports

Imports: v76 complete actual five-row-type graph/frame placement, v77 complete sparse frames/unique pairing/circuits, v78 complete two-projection local CS construction, v79 repeated-pair isoclinicity/2+2+1 triangle, and the actual primary TEN-transversal/CLASSICAL-mate interface. New arguments here pay strict principal-angle endpoints from actual frames, the oriented-plane one-cell bound, central commutation, ALL nonisoclinic-w uncoverability, and the complete Gram/Clifford/chirality reduction. No classifier/NR/Butson/Gaussian/code premise or v15 global rank2 ceiling is needed.

These are author-WRITTEN necessary geometry and actual mechanism exclusions only. Remaining: the FULL mixed-chirality three-circuit actual frame/column gluing and SAME TEN-class resolution; four/five actual circuits; dense vertices; other placements/minimalrank3 physical and higher-rank families; complement60 and actual100 distinct rays. Unrestricted irreducible10,4+6,5+5 all remain OPEN. No original witness/global no-go/formal/kernel/family/vendor/human/checker/priority/current-openness/novelty promotion.

Only a NEW complete SEPARATE-FUTURE union may incorporate S80, preserving ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history. Frozen Mainv17/S72/index/proofs/live151 remain immutable; older then-open statements are qualified prospectively, never edited/backdated.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. No109/110/newscope/proof/coauditorreport/159/140 access/read claim, extra GO/STOP/restart or continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
