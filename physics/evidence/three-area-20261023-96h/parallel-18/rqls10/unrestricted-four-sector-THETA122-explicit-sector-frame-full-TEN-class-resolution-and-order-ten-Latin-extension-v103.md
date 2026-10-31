# RQLS10 v103 — THETA(1,2,2) ALSO admits an explicit all-sparse E4 sector with a full TEN-class resolution that extends to an order-ten Latin square

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 22:31:16 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact written algebra; the Latin square was hand-checked. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Placement and operators (v98 data reused)

THETA(1,2,2) (v82/v92) has circuits X: v1->v2->v4, Y: v1->v3->v5, a: v2<->v3 and b: v4<->v5. Its columns are Xa'=X(v1->v2), Xb'=X(v2->v4), Xc'=X(v4->v1), Ya'=Y(v1->v3), Yb'=Y(v3->v5), Yc'=Y(v5->v1), a1=a(v2->v3), a2=a(v3->v2), b1=b(v4->v5) and b2=b(v5->v4). Each column carries the + plane at its tail. The constants c, s, gamma, b, beta, K, S, W and the operators R_X, R_Y, R_B, R_A, M_t1 and M_r2 are EXACTLY those of v98 §1 (with erratum E98.1). Set

    R_a = R_B,   R_b = R_A,   S_v1 = I ⊗ |3pi/4><3pi/4|,   S_v3 = S_t1 (v98),   S_v4 = S_r2 (v98),
    S_v2 = (I + R_B M2)/2,  M2 = |y+><y+| ⊗ sigma_{3pi/4} + |y-><y-| ⊗ sigma_0,
    S_v5 = (I + R_A M5)/2,  M5 = |x+><x+| ⊗ sigma_{pi/2} + |x-><x-| ⊗ sigma_{7pi/4}.

The first circuits are X at v1, v2, v4 and Y at v3, v5. Row v.1 carries the first circuit's cells inside S_v and the second circuit's inside S_v-perp; row v.2 is the reverse.

## 2. Lemma DUAL: R_B is "doubly normal"

For R = (alpha sigma_z + h sigma_x) ⊗ I + delta sigma_y ⊗ sigma_n with alpha^2 + h^2 + delta^2 = 1:
- an x-block-diagonal M (equatorial blocks mu ⊥ n) has R M commuting with R_Y iff gamma' alpha h = gamma(1 - alpha^2);
- a y-block-diagonal M has R M commuting with R_X iff gamma' alpha' h' = gamma(1 - alpha'^2), where alpha' = gamma alpha + gamma' h and h' = gamma' alpha - gamma h.

Writing gamma = cos psi, (alpha, h) = r(cos phi, sin phi) and (alpha', h') = r(cos(psi - phi), sin(psi - phi)), BOTH conditions become r^2(cos psi + cos(2phi - psi)) = 2cos psi. They are therefore equivalent.

For R_B, in the y-basis: alpha' = b; h' = b gamma' S^2 = beta K, using gamma = tan^2(pi/8); and the off-diagonal block is (y+,y-) = beta W, (y-,y+) = beta W*. Hence [R_B, M2] = 0 iff nu2 = mu2 - 3pi/4 (here 0 = 3pi/4 - 3pi/4). The block identities Q12 = Q21 = beta sigma_{mu2 - 3pi/8} and gamma'(Q11 - Q22) = 2 gamma Q12 reduce to gamma beta = gamma' b K. So S_v2 is a rank-two projection commuting with P_X and P_B, with trace one on each. The mirror J (x± <-> y±; J sigma_y J = -sigma_y, so J R_B J = R_A) gives the same for S_v5 with P_Y and P_A.

The compressions of S_v2 follow exactly as in v98 (I4): x+ ⊗ K2 -> sigma_{mu2 - pi/4} = sigma_{pi/2} and x- ⊗ K2 -> sigma_{mu2 + pi/2} = sigma_{5pi/4}. By the mirror, S_v5 compresses y+ -> sigma_{pi/4} and y- -> sigma_pi.

## 3. The forty cells (all X/Y cells product rays)

The X/Y cells are:

    v1: x±|3pi/4> (S), x±|7pi/4>, y±|3pi/4> (S), y±|7pi/4>
    v2: x+|pi/2> (S), x+|3pi/2>, x-|5pi/4> (S), x-|pi/4>
    v3: y+|pi> (S), y+|0>, y-|pi/4> (S), y-|5pi/4>
    v4: x+|pi/4> (S), x+|5pi/4>, x-|3pi/2> (S), x-|pi/2>
    v5: y+|pi/4> (S), y+|5pi/4>, y-|pi> (S), y-|0>

The a-cells are the joint eigenlines of R_B with M2 (at v2) and with M_t1 (at v3). The b-cells are those of R_A with M_r2 (at v4) and with M5 (at v5). All pairs of circuits have scalar anticommutators 2gamma, 2(sqrt2-1) or 2(1-sqrt2) (v98 I5), so different circuits share no ray.

Within X and within Y, the listed second factors are distinct. Within a: an a-cell at v2 equal to one at v3 would be a common eigenvector of M2 and M_t1. Every eigenspace intersection E±(M2) ∩ E±(M_t1) is zero, because
- E+∩E+ forces delta = 0 and then x- ⊗ |3pi/4> to be parallel to x- ⊗ |3pi/2>;
- E+(M2)∩E-(M_t1) would need (r + e^{i3pi/8})/(r + e^{-i3pi/8}) = i with r = sqrt2/K, i.e. sqrt2/K = S - K, i.e. sqrt2 = SK - K^2 = (sqrt2 - 1)/2, which is false;
- I ⊗ sigma_3 maps E± of each operator to E∓, which covers the other two intersections.

The b case is the J-mirror. Its intersections reduce to 2 - sqrt2 ≠ (3 - 2sqrt2)/2 and to i ≠ e^{-i pi/4}. Hence all forty rays are distinct (MAX40). The S_v have the stated commutations and traces, so the v82 §5 forward proof gives all row and column ONBs.

## 4. Ten classes (sector ONBs, distinct rows/columns)

    N1 = {x+|pi/4> v4.1 Xc', x-|pi/4> v2.2 Xa', y+|5pi/4> v5.2 Yc', y-|5pi/4> v3.2 Ya'}
    N2 = {x+|5pi/4> v4.2 Xc', x-|5pi/4> v2.1 Xa', y+|pi/4> v5.1 Yc', y-|pi/4> v3.1 Ya'}
    P1 = {x+|3pi/4> v1.1 Xa', x-|3pi/2> v4.1 Xb'} + {P_a S_v3' v3.1 a2, P_a' S_v3 v3.2 a1}   (E+(M_t1) + a-pair on E-)
    P2 = {x+|7pi/4> v1.2 Xa', x-|pi/2> v4.2 Xb'} + {P_a S_v3 v3.2 a2, P_a' S_v3' v3.1 a1}
    Q1 = {x+|pi/2> v2.1 Xb', x-|7pi/4> v1.2 Xc'} + {P_b S_v5' v5.1 b2, P_b' S_v5 v5.2 b1}  (E+(M5) + b-pair on E-)
    Q2 = {x+|3pi/2> v2.2 Xb', x-|3pi/4> v1.1 Xc'} + {P_b S_v5 v5.2 b2, P_b' S_v5' v5.1 b1}
    U1 = {y+|3pi/4> v1.2 Ya', y-|0> v5.2 Yb'} + {P_a S_v2' v2.1 a1, P_a' S_v2 v2.2 a2}   (E+(M2) + a-pair on E-)
    U2 = {y+|7pi/4> v1.1 Ya', y-|pi> v5.1 Yb'} + {P_a S_v2 v2.2 a1, P_a' S_v2' v2.1 a2}
    V1 = {y+|0> v3.2 Yb', y-|3pi/4> v1.2 Yc'} + {P_b S_v4' v4.1 b1, P_b' S_v4 v4.2 b2}   (E+(M_r2) + b-pair on E-)
    V2 = {y+|pi> v3.1 Yb', y-|7pi/4> v1.1 Yc'} + {P_b S_v4 v4.2 b1, P_b' S_v4' v4.1 b2}

N1 and N2 are ONBs by orthogonal second factors. In each P/Q/U/V class, the X- or Y-pair spans one eigenspace of the commuting reflection M, and the a- or b-pair spans the other. On that eigenspace 2S-I = ±R; R is non-scalar there because its off-diagonal block is nonzero. The author checked by hand that every cell is used once, every class has distinct rows and distinct columns, and every row and column carries four distinct classes.

## 5. Order-ten Latin extension (hand-checked; E4 entries bracketed)

           Xa'  Xb'  Xc'  Ya'  Yb'  Yc'  a1   a2   b1   b2
    v1.1  [P1]  N1  [Q2] [U2]  N2  [V2]  Q1   V1   P2   U1
    v1.2  [P2]  N2  [Q1] [U1]  N1  [V1]  V2   Q2   U2   P1
    v2.1  [N2] [Q1]  V1   V2   Q2   P1  [U1] [U2]  N1   P2
    v2.2  [N1] [Q2]  V2   V1   Q1   P2  [U2] [U1]  P1   N2
    v3.1   Q1   V1   U2  [N2] [V2]  Q2  [P2] [P1]  U1   N1
    v3.2   Q2   V2   U1  [N1] [V1]  Q1  [P1] [P2]  N2   U2
    v4.1   U1  [P1] [N1]  Q1   P2   U2   Q2   N2  [V1] [V2]
    v4.2   U2  [P2] [N2]  Q2   P1   U1   N1   Q1  [V2] [V1]
    v5.1   V2   U1   P1   P2  [U2] [N2]  V1   N1  [Q2] [Q1]
    v5.2   V1   U2   P2   P1  [U1] [N1]  N2   V2  [Q1] [Q2]

Every row and every column contains all ten symbols once, and all forty bracketed entries equal §4. All of this was checked by hand.

## 6. Consequences and scope

v92 left THETA(1,2,2) existence OPEN. If confirmed, it now has an explicit octagonal all-sparse sector with a full ten-class resolution and an order-ten Latin mate, exactly as BARBELL does (v98/v99). So the all-sparse four-sector analysis cannot close THETA(1,2,2) either.

N1 and N2 are cross XY classes whose E4 columns are exactly v1's E4 columns. By the v101 SQUEEZE argument (verbatim, with Z replaced by v1), any orthogonal-triple split of v1's six H6 planes must keep each N-class's two v1-columns (here Xb', Yb') inside one triple.

NOT an original witness: the H6 sector (sixty rays in C6 for this L) is OPEN. C5, dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN. Independent exact verification is required.

Imports: v98 data/identities/E98.1 (via v99); v82 §4-§7; v86/v92 THETA(1,2,2) structure; v101 SQUEEZE (stated, not re-proved); elementary Pauli/projection algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S103, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect, the v34 capture retry, the S98 zero-credit mental-decimal disclosure and the v46 parallel post-cell capture disclosure.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
