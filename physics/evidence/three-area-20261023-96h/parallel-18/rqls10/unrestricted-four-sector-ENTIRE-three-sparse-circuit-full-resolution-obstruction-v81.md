# RQLS10 v81 — ENTIRE three-sparse-circuit mechanism has no original MAX1 resolution

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 17:41:39 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. All expectation/trace/product/matching/capacity identities are written below; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** Main's frozen v17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. This NEW theorem is outside those gates. No automatic review admission/read/adoption or old-verdict inheritance.

## 1. Entire actual mechanism and the remaining positive-Gram case

Use ENTIRE v76/v77 actual five-row-type E4 graph/frame classification, v79 all-pair intersection capacity, and v80's full three-circuit analysis. The theorem is NO original 100-ray maximal1-RQLS10 can have ALL local frames sparse and EXACTLY THREE actual projection circuits. We do NOT assume this mechanism is WLOG for four/five circuits, dense vertices or other placements.

By v79 the only original three-circuit intersection graph is the 2+2+1 triangle: two row-pair vertices P/Q, two P/R, one Q/R vertex w. Circuit lengths are 4,3,3. Their actual E4 cell counts, partitioned by the circuit supplying the cell's edge plane, are therefore

    N_P=16,    N_Q=12,    N_R=12.

Indeed each incident original vertex supplies exactly FOUR actual cells to a circuit: TWO rays in each of its two opposite edge planes. Distinct circuit labels here classify actual cells, not formal overlapping eigenspaces.

If Q/R is nonisoclinic, v80 makes ALL eight w-cells absent from EVERY quantum transversal, excluding a full covering resolution. The repeated P/Q and P/R pairs are already isoclinic. Thus any remaining original candidate has three pairwise interior-isoclinic rank2 projections. Put A=2P-I,B=2Q-I,C=2R-I, with scalar anticommutators 2aI,2bI,2cI and real positive-semidefinite Gram matrix

    G = [[1,a,b],[a,1,c],[b,c,1]],    a,b,c in (-1,1).

If G is singular, its rank is exactly TWO and v80's e=0 construction gives a common-first-qubit representation; its all-five-vertex distinctness/actual-column proof excludes every quantum transversal. The scalar-chirality positive-Gram branch is also excluded there, but is not needed separately below.

It therefore suffices to exclude the ENTIRE POSITIVE-DEFINITE Gram case, including ALL mixed-chirality parameters and arbitrary actual complex local frames. The argument below does not choose any Gram entries and does not need a simultaneous first-qubit representation for all three operators.

## 2. Trace balance forces every sector ONB to use EXACTLY TWO circuit pairs

Let T be ANY quantum transversal of an ordinary MAX100 array in this remaining mechanism. Its FOUR E4 rays form an ONB of H4 and have distinct original rows and columns. By v80's oriented-plane lemma, T has at most ONE actual ray in each of P,I-P,Q,I-Q,R,I-R.

Write n_P+,n_P-,n_Q+,n_Q-,n_R+,n_R- for these zero/one counts and delta_P=n_P+-n_P-, similarly delta_Q,delta_R. For any unit vector x in the epsilon eigenspace of A, scalar anticommutation gives

    2 epsilon <x,Bx> = <x,(AB+BA)x> = 2a,
    <x,Bx>=epsilon a,    <x,Cx>=epsilon b.

The corresponding formulas hold for B- and C-eigenvectors. Summing expectations of A,B,C over the FOUR-ray ONB of H4 gives their traces, all ZERO. Consequently

    delta_P + a delta_Q + b delta_R = 0,
    a delta_P + delta_Q + c delta_R = 0,
    b delta_P + c delta_Q + delta_R = 0,
    G (delta_P,delta_Q,delta_R)^T = 0.

Positive definiteness of G forces ALL three deltas to vanish. Every used circuit therefore contributes one PLUS and one MINUS ray, or neither. Since exactly FOUR rays are selected, every quantum transversal has one of EXACTLY THREE sector types: PQ,PR,QR, taking TWO opposite-plane rays from EACH named circuit. Types with circuit counts 2+1+1 are impossible in the ENTIRE positive-Gram case, without an angle resonance assumption.

## 3. A PQ-type transversal contains NO actual cell from a P/Q intersection

Fix type PQ. Use a physical isoclinic identification for THIS pair ONLY: P=p+ tensor I2,Q=q+ tensor I2, with all four first-factor rays distinct and all cross P/Q overlaps nonzero. Any selected ray in an oriented P or Q plane is its fixed first factor times some second-factor unit ray, regardless of which original vertex supplied it.

Orthogonality between EVERY selected P-ray and EVERY selected Q-ray makes the second-factor spans of the two P-rays and two Q-rays mutually orthogonal in C2. Both spans are nonzero, so both are one-dimensional. Hence, projectively, the four selected rays are

    p+ tensor u,    p- tensor u,    q+ tensor u-perp,    q- tensor u-perp.

Suppose a selected P-ray belongs to an actual P/Q vertex v. The actual sparse-frame Cartesian construction has BOTH P+ and P- rays with that SAME second factor in the SAME original row at v. Therefore the selected opposite-P ray equals an ACTUAL partner ray already in that SAME row. Global100-ray distinctness forces that selected ray to occur in exactly this actual partner cell; selecting a different occurrence would itself contradict MAX. Either way T cannot have distinct original rows.

Exactly the same argument applies if any selected Q-ray belongs to a P/Q vertex: its opposite-Q partner with the same second factor is an ACTUAL ray in the SAME original row there. Thus a PQ-type quantum transversal uses NO cell of the ENTIRE P/Q intersection class. This conclusion uses actual row placement as well as product orthogonality and MAX; plane labels alone are insufficient.

The statement is symmetric: a PR-type T uses NO P/R cell, and a QR-type T uses NO Q/R cell. Each pair identification is separate. No simultaneous global tensor ansatz or chirality choice is imposed.

## 4. The required SAME full TEN-class resolution violates actual cell capacity

Assume ONE allowed full resolution into TEN disjoint quantum transversals covering ALL100 cells. Let x,y,z be the numbers of PQ-,PR-,QR-type classes. All forty E4 cells must be covered by these SAME ten classes. The actual circuit-cell counts from section1 and section2 therefore give

    2(x+y)=16,    2(x+z)=12,    2(y+z)=12.

Equivalently x+y=8,x+z=6,y+z=6. Subtracting gives x=y; hence

    x=4,    y=4,    z=2.

Now a PQ-type class cannot use any P/Q cell by section3. Its selected Q+ and Q- cells must come from Q's OTHER intersections, which here consist of ONLY the lone Q/R vertex w. That vertex has exactly FOUR actual Q-circuit cells total: TWO Q+ and TWO Q-, in its two original rows.

Each PQ-type class consumes TWO such w Q-cells. Since the x classes are disjoint, their demand is 2x actual cells, bounded by FOUR. Thus x at most TWO. But the SAME full-resolution circuit count forced x=FOUR. This is a contradiction. Independently the PR-type classes similarly demand eight w R-cells where only four exist.

This contradiction excludes EVERY full TEN-class resolution in the ENTIRE positive-Gram pairwise-isoclinic three-circuit mechanism. It is not a chosen-resolution search or local incidence count detached from rays: section2 uses actual ONB expectations, and section3 uses actual sparse row partners/global ray distinctness. It does NOT claim that the mixed-chirality branch has no individual quantum transversals.

## 5. Exhaustive entire-three-circuit conclusion and exact original frontier

The cases are exhaustive under v79: Q/R nonisoclinic has uncoverable w-cells; pairwise-isoclinic singular-Gram cases have no quantum transversal; ALL positive-Gram cases now contradict full-resolution cell capacity. Thus the ENTIRE exactly-THREE actual sparse-circuit mechanism is excluded for original100-ray maximal1-RQLS10.

Together with v79's stronger two-circuit obstruction, an original MAX1 array in this v76 actual graph family must have at least ONE DENSE local frame OR, if ALL local frames are sparse, have at least FOUR actual vertex-simple projection circuits. Circuit-intersection H still has five edges, degrees at least two and multiplicities at most two. This is not closure of four/five-circuit mechanisms, dense geometry, other placements/minimalrank3 physical/higher-rank families, complement60 construction or the unrestricted original problem.

The full unrestricted irreducible10,4+6,5+5 branches all remain OPEN. No original witness, global no-go, all-sparse or full4+6 resolution, formal/kernel/family/vendor/human/checker/priority/current-openness/novelty promotion is delivered. The mixed-chirality normalform in v80 remains a supported historical necessary representation; its then-open original full-resolution gap is closed only PROSPECTIVELY by this NEW proof, never by rewriting or backdating v80.

Exact imports: ENTIRE v76 graph/frame placement, v77 unique sparse pairing/circuits/actual rows, v78 complete two-projection local constructions, v79 repeated-pair isoclinicity/intersection triangle, v80 strict angles/oriented-plane bound/nonisoclinic uncoverability/Gram singular reduction, and the actual primary TEN-transversal/CLASSICAL-mate interface. New ingredients are full ONB trace-balance Gdelta=0, the ACTUAL used-pair row-partner exclusion, and SAME full-resolution global count versus w-cell capacity. No NR/classifier/Butson/Gaussian/code premise or v15 global rank2 ceiling is needed.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S81, retaining ALL older individual claim nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history. Frozen Mainv17/S72/input map/proofs/live151 stay immutable; no automatic review admission/read/adoption or verdict transfer.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. No109/110/newscope/proof/coauditorreport/159/140 access/read claim, extra GO/STOP/restart or continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
