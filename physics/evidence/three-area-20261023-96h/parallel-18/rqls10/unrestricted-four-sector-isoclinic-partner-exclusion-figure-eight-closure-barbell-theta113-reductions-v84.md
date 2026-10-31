# RQLS10 v84 — Isoclinic partner exclusion: FIGURE-EIGHT closed; BARBELL forced all-isoclinic; THETA(1,1,3) exact class pattern

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 18:22:49 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written two-projection/product-ray/row-column/counting arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain

Use the ENTIRE v76 actual five-row-type trueE4 graph with ALL local frames sparse, v77 unique pairings/circuits, v79 circuit-intersection graph H, and v82's exhaustive four-circuit list. This manuscript treats the THREE four-circuit topologies WITH a repeated circuit pair: FIGURE-EIGHT, BARBELL(2,1,2) and THETA(1,1,3). By v79 every repeated pair is interior-isoclinic in any ordinary MAX100 array. Original MAX1 means ordinary MAX100 plus ONE full TEN-class resolution; each class has exactly four E4 cells forming an ONB of E4 with distinct original rows and columns (v15 count interface).

Terminology. A cell is C-labeled when its edge plane belongs to circuit C; it is C+ or C- by its oriented plane. v80 proved: every quantum transversal contains at most ONE cell of each oriented plane (C80_PLANE1). No other WLOG is used.

## 2. Three lemmas for ANY interior-isoclinic pair at ANY intersection

Let C,D be circuits whose projections satisfy P_C P_D P_C = lambda P_C with 0<lambda<1 (equivalently a scalar reflection anticommutator), meeting at an actual vertex v. By v78/v79, there is a physical identification H4 = K1 tensor K2 with P_C = c+ tensor I, P_D = d+ tensor I, all cross overlaps between {c+,c-} and {d+,d-} nonzero, and S_v = I tensor |u><u|. The eight actual cells at v are, row by row,

    row alpha:  c+ tensor u,  c- tensor u,  d+ tensor u-perp,  d- tensor u-perp,
    row beta:   c+ tensor u-perp,  c- tensor u-perp,  d+ tensor u,  d- tensor u,

up to exchanging the names of the two rows. EVERY C-labeled cell anywhere in the array has a ray c+ tensor y or c- tensor y; likewise for D.

LEMMA P (pair rule). Two cells at C/D intersections that are orthogonal and lie in distinct rows and columns belong to the SAME circuit with OPPOSITE orientations. At one vertex this is read from the displayed rows: same-column pairs are excluded, and every cross-circuit cross-row overlap is a nonzero first-factor overlap. At two different C/D intersections, v79's MAX distinctness makes the second-factor overlaps nonzero, so the first factors must be orthogonal.

LEMMA X (partner exclusion; NEW). Every C-cell at v is NON-orthogonal to EVERY D-cell at ANY other vertex. Proof: let c+ tensor s be in row rho at v (the c- case is identical). A D-cell elsewhere has ray d+- tensor y. Orthogonality means <c+|d+-><s|y>=0, so y is proportional to s-perp. But d+- tensor s-perp is ALREADY the ray of the actual D-cell in row rho at v. A second cell at another vertex with that ray contradicts ordinary 100-ray maximality. The roles of C and D are symmetric. No full resolution, multiplicity or global sector assumption is used.

LEMMA W (pair exclusion). Let T contain d+ tensor s and d- tensor s' with s not proportional to s', as happens for two distinct-row cells at one C/D vertex (s'=s-perp) or at two different C/D vertices (v79 distinctness). Then T contains NO C-cell anywhere: c+- tensor y orthogonal to both forces y orthogonal to two independent vectors of C2.

## 3. Theorem 1: a length-two partner circuit forces len(D) at most three

Suppose C has LENGTH TWO and both of its vertices are C/D intersections (thus m_CD=2 and C/D is isoclinic). Every C-cell lies at these two vertices. In ANY full TEN-class resolution:

* There are exactly four C+ cells, so exactly FOUR classes contain a C+ cell; likewise four contain a C- cell.
* A class containing a C-cell contains NO D-cell: D-cells at the two C/D vertices are excluded by Lemma P, and D-cells elsewhere by Lemma X.
* D has length len(D), hence 2 len(D) D+ cells in 2 len(D) distinct classes, none of them a C+ class.

Therefore 2 len(D) <= 10-4, i.e. len(D) <= 3. If len(D)=3, the four C- classes avoid the six D+ classes and so COINCIDE with the four C+ classes. Each contains a C+/C- pair, and each of the other SIX classes contains one D+ and one D- cell.

## 4. Corollary: the ENTIRE FIGURE-EIGHT topology has no original MAX1 resolution

In FIGURE-EIGHT, H is a three-cycle X-A-B-X glued at X to a doubled edge X=C. The circuit C has length two with both vertices on X, while X has degree four in H, i.e. length FOUR. Theorem 1 requires length at most three. Hence NO original MAX1 array has the all-sparse FIGURE-EIGHT mechanism, for ALL cyclic orders, orientations, row labels, complex frames and angles. This does not choose a resolution or test candidates.

## 5. BARBELL(2,1,2): forced isoclinic bridge and an exact residual normal form

BARBELL has doubled edges X=A and Y=B joined by ONE bridge X-Y at a single row-pair vertex z. A and B have length two; X and Y have length three. Apply Theorem 1 to (A,X) and (B,Y), both with equality. Hence:

* four PA classes contain an A-pair and no X-cell; the other six contain X+ and X-;
* four PB classes contain a B-pair and no Y-cell; the other six contain Y+ and Y-.

Let q be the number of classes in BOTH PA and PB. At least 10-(8-q)=2+q classes are in NEITHER, and each such class consists of EXACTLY ONE cell each of X+,X-,Y+,Y-.

For such a class put U = span of its X+ and X- rays. U is P_X-invariant, and its orthogonal complement, spanned by the Y+ and Y- rays, is P_Y-invariant. So the projection Pi_U commutes with BOTH P_X and P_Y.

If the single bridge pair X/Y has UNEQUAL compression eigenvalues (both interior by v80), v78's commutant argument gives Pi_U = S_z or I-S_z. Then the class's X+ and X- rays are P_X S_z and (I-P_X)S_z, or both from I-S_z: they are the two z cells of ONE original row. Global distinctness identifies them with those actual cells, contradicting distinct rows. So the bridge pair X/Y MUST be interior-isoclinic.

In the isoclinic case use the (X,Y) identification: S_z = I tensor |omega><omega| and Pi_U = I tensor |w><w|. Then the class's X-rays are x+ tensor w,x- tensor w and its Y-rays are y+ tensor w-perp,y- tensor w-perp. If any of them were a z cell, w would be omega or omega-perp and its same-sign partner would be the z cell of the SAME row. Hence every NEITHER class is an X-pair from the X/A intersections plus a Y-pair from the Y/B intersections, sharing the (X,Y)-second factor w. The four z X-cells lie ONLY in B-pair classes, and the four z Y-cells ONLY in A-pair classes. Counting X+ cells also gives q <= 2.

EXACT RESIDUAL NORMAL FORM. With all three pairs X/A, X/Y and Y/B interior-isoclinic, write R_C=2P_C-I. In (X,Y) coordinates R_X = sigma_z tensor I and R_Y = (gamma sigma_z + sqrt(1-gamma^2) sigma_x) tensor I. Then

    R_A = alpha R_X + sqrt(1-alpha^2) N_A,
    N_A = |0><1| tensor V_A + |1><0| tensor V_A*,
    R_B = beta R_Y + sqrt(1-beta^2) N_B,
    N_B = |y+><y-| tensor V_B + |y-><y+| tensor V_B*,

with alpha,beta,gamma in (-1,1) and V_A,V_B in U(2). This is DERIVED: (R_A-alpha R_X)^2=(1-alpha^2)I and anticommutation with sigma_z tensor I force the displayed off-diagonal unitary form. Every X/A vertex has S_v = |0><0| tensor Pi + |1><1| tensor V_A* Pi V_A for a rank-one Pi, and S_z = I tensor |omega><omega|. Thus the WHOLE BARBELL residual is parameterized by alpha,beta,gamma,V_A,V_B,omega and four rank-one vertex projections, plus ALL discrete data. Existence of an actual full resolution in this family remains UNSOLVED.

## 6. THETA(1,1,3): exact forced class pattern

THETA(1,1,3) has a doubled edge X=Y at row-pair vertices v1,v2, and a path X-a-b-Y with vertices w1 (X/a), w2 (a/b), w3 (b/Y). X and Y have length three, a and b length two. X/Y is interior-isoclinic (v79). The X+ cells number six: four at v1,v2 and two at w1; likewise X-, Y+-. Theorem 1 does not apply because no length-two circuit is doubled.

Classify a full-resolution class by its v1/v2 part: PX (X-pair), PY (Y-pair), SX or SY (one cell), N (none); Lemma P makes this exhaustive. Lemma W gives PX classes no Y-cells and PY no X-cells. Lemma X says an SX class has no w3 Y-cell, so it has at most ONE foreign X/Y cell (the opposite X plane at w1); likewise SY. N classes have at most four foreign X/Y cells. From the cell counts,

    2(p_X+p_Y)+r = 16,   p_X+p_Y+r+n = 10   =>   p_X+p_Y = 6+n,  r = 4-2n.

The eight foreign X/Y cells at w1,w3 need 8 <= r+4n = 4+2n. Hence n=2, r=0 and p_X+p_Y=8. Six classes contain X+ and PY classes contain none, so p_Y <= 4; similarly p_X <= 4. Therefore

    EXACTLY 4 PX classes, 4 PY classes and 2 N classes.

Each N class is {X+,X- at w1; Y+,Y- at w3}. Orthogonality in the X/Y identification forces the rays x+ tensor z, x- tensor z, y+ tensor z-perp, y- tensor z-perp. Consequently

    S_w1 = span(x+ tensor z1, x- tensor z1-perp),  2S_w1-I = R_X tensor tau,
    S_w3 = span(y+ tensor t1, y- tensor t1-perp),  t1 in {z1,z1-perp},

with tau=|z1><z1|-|z1-perp><z1-perp|. Thus both S operators are the product reflections R_X tensor tau and +-R_Y tensor tau, with the SAME tau. Every a-cell at w1 lies in S_w1 or its complement and has both x+ and x- components. It lies in no PX class: membership would force the PX pair's second factors to be z1-perp,z1, which contradicts global distinctness from the w1 X-cells. Likewise every b-cell at w3 lies only in PX classes. The sixteen a/b cells fill exactly the PX/PY slots: four w1 a-cells in PY, four w3 b-cells in PX, and the eight w2 cells split four/four. Existence or exclusion of this exact pattern remains OPEN.

## 7. Exact frontier and imports

New paid results: Lemma X; Theorem 1; ENTIRE FIGURE-EIGHT excluded for original MAX1; BARBELL forces an isoclinic bridge, a finite-parameter all-isoclinic normal form and an exact class pattern; THETA(1,1,3) forces a 4/4/2 class pattern with product-reflection S operators and a/b placement rules. The remaining all-sparse frontier is: BARBELL normal-form gluing; THETA(1,1,3) a/b gluing; exceptional coupled loci of THETA(1,2,2)/C5 (v83); dense local frames; other sector placements; minimal rank3 physical and higher-rank families; complementH6; SAME TEN-class resolution. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: the ENTIRE v76/v77 actual graph/sparse frames, v78 complete local two-projection constructions, v79 repeated-pair isoclinicity/distinctness, v80 strict angles/oriented-plane bound, v82 topology list/ribbon interface, and the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure-theoretic genericity, global tensor WLOG, or v15 global ceiling. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S84, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
