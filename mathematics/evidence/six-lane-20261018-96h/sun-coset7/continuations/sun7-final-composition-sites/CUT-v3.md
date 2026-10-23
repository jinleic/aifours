# CUT-v3 — source-backed repair of the CUT-v2 M3 review: literal D23P/TC-P/CELL interfaces, registered reduction nodes, peripheral import closure and a reconciled 79-node order [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T21:36:17-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Frozen scopes (all before this text):** `CUT3-SCOPE-v1.md` 56162bfd35b4b5fd59859da9b08ec53d51522a0655cf8b6a95569a4ad8fb92df;
  `FINAL-SCOPE-addendum-v1.md` 8ee0d35de781767bdb51c370d0f945a121b84437ad874972550ed4fdf2ff4bd0; `FCS-SCOPE-v1.md`
  32ee3245a9a92471fc8134b291d22d5566e6cfe284f86d72deb15870a80c4b07 (this directory).
- **Reviews folded:** RUN/review/sun7-CUT2-M3-codex-v1.prompt.stdout.txt e03879a282cb26fc055db188225322a4bc484fcf0b3a8b6399ba9cc9f7e604b9 (0F/2M/1m);
  RUN/review/sun7-CUT2-M12-codex-v1.prompt.stdout.txt 258f28ababb20fbf7293ce3fd2c3f702c9a5a9b5f56fee6f86add2f33456a006 (0F/0M/0m).
- **Predecessor (immutable):** `../sun7-written-import-cutover/cut-review-repair-v1/CUT-v2.md` bd4d5946212ef3870414be51e05ef2d5e4f7900bbe40edb33594ed309969013e.
- **Roots:** S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7; D = S/continuations/k7-k62-residue;
  K62 = S/continuations/k63-residue/k62-followon; A = S/continuations/k7-a2-closure; O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7;
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h (R = RUN/review); R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.
  OV1 = D/K7-A1-A2-delta-erratum-v1.md; OV2 = D/K7-A1-A2-delta-erratum-v2.md; CE1 = D/K7-D23RICH-D23P-erratum-v1.md (consolidated
  RICH/D23P erratum); R2E = D/K7-R2-repair-erratum-v1.md; ECFF = D/K7-R2-R3-consolidated-erratum-v1.md; WV = R16/sun-coset7-written-parent-verdict-v1.md.
  All line numbers are one-based physical LF lines of the named immutable file; every range is pinned in the part manifests.
- **Rule of this file.** No accepted theorem is re-derived. Each interface below is the literal accepted statement with its
  mandatory overlays, its accepted external inputs, and every consumer binding (clause used). Where a needed hypothesis or
  conclusion were not carried by an exposed source line, the item would be marked OPEN; none was found, which is a
  CANDIDATE finding for review, not a certification.

## 0. What is carried over, and status separation
- CUT-v2 sections 2-3 (M1 E3 proof-path; M2 reachable M13-A closure) are carried over unchanged by reference; Codex M12
  returned 0F/0M/0m. They remain a CONDITIONAL dual gate until the parent's second-family/parent disposition.
- CUT-v2 sections 0-1's "S56W pending" wording is superseded, as of this writing only, by the accepted S56W verdict
  (R/sun56-S56W-parent-verdict-v1.md 63baa72b107e0f809c26a5057f10b6fd31f8ae2f09cffb527873bec11a8107ee LF5-14; errata v1 b2299b6f…, v2
  ef62c628…). Accepted cores: C5W (R/sun5-C5W-parent-verdict-v1.md cc1300d5…), C56W (R/sun6-C56W-parent-verdict-v1.md f60d546a…).
  Also accepted since CUT-v2 was frozen: A2X (R/sun7-A2X-parent-verdict-v1.md 9ad41f21…). These are recorded here as a dated
  status, not read back into any earlier text. S5W/S6W enter only as STATEMENT substitutions at the individually checked
  sites of `FCS-SITES-v1.md` (this directory); no historical internal lemma, minimal frame or old C18 is imported.
- Full Sun(7) UNACCEPTED. Completeness certification of the expanded written chain stays WITHHELD (section 7).

## 1. MINOR m3 — corrected TRANSFER list (replaces CUT-v2 LF148 and LF176 readings)
CUT-v2 LF148 and LF176 wrote the excluded TC row as "1114 | c | 1". The accepted text is "the exclusion of ({1,4,4,4} | c | 1)
(each for E >= 2)" (OV2 LF187-189, the V2.7 New field), i.e. the row **1444 | c | 1** with c in {1,2}: TC-v1 LF50 ("({1,4,4,4} | c | 1)
with c in {1,2} has value >= 6 (y = (o 1, fours 1/3, t 1); t's label 3^A w_t is coprime to all)"), kept at E >= 2 by OV1 LF17-18.
**Complete TRANSFER list (OV2 LF183-190), corrected transcription:** in (a2-no5) with W := W' cup {p}, with RICH replaced by
the BRIDGE list: A1-STRUCT Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem CASEB (with their
load-bearing section-0 subroutines); K7-TC Lemma TC, Lemma FG-V, row R1 (every E >= 1), rows R3, R4, R5 and the exclusion of
1444 | c | 1 (each for E >= 2), Theorem K7-TC-B, Proposition TC-P for its stated matrix data (section 3 below); K7-TC-A22 Theorem
K7-TC-A22. Not transferred: A1-STRUCT sections 6-7, K7-TC sections 5-6, K7-TC-A22 section 4. All other CUT-v2 section 6
restrictions stand.

## 2. MAJOR1(a) — D23P: exact accepted interface, branch structure and consumer bindings
**Accepted statement (D/K7-D23P-v1.md LF20-22, unchanged by CE1 LF585-586; accepted by R/sun7-K7-D23RICH-D23P-parent-verdict-v1.md
LF12-13):** "In (a2) neither z-row is 4-type. More precisely, for x in {alpha, alpha*}, with T_x := {u in W' : x_zu = 3}:
|T_x| >= 2, x_zu in {1,2} for u in W' \ T_x, x_zt != 4, and if |T_x| = 2 then x_zp = 3 and the two entries on W' \ T_x are
equal. (Arbitrary groups with finite-index subgroups by R0.)" Setting (D23P LF10-18): distinct z, t, p, r_z = 2^E w_z,
r_t = 3^A w_t, r_p = 5^B w_p, E, A, B >= 1 actual and unbounded; W' the four unmarked vertices; alpha, alpha* the actual
families. **Hence, for BOTH actual families x and every u in W': x_zu in {1,2,3}.**
**Accepted external inputs (D23P LF24-46 with CE1 P3a LF550-554 and P3b LF565-576):** R0 and the K7 definition (README); LFC (a),
(c), (d), INV (a), (b), E1, E2, E6, E7 (LFC/INV package, verdict 8621e744); Lemma ROW-2 (a')-(c') of K7-35 with its two errata
(verdict 1a1c6390), used at the marked apex z only through CE1 P1 (LF441-459: the exact six-label gcd matrix, H35 not read);
D23-CENTER (D23 verdict R/sun7-D23-parent-verdict-v1.md LF6: both z-rows 4-type is impossible, **5-marker anywhere**); L0.3,
L1 (T1)-(T3), VFC (V1)-(V4), F7 (rules-k7-v1, addendum A1; WV), applied also to the inverted configuration (Z2 erratum G5).
**D23-MIX is not an input of D23P** (its scope needs W unmarked; D23 verdict LF7); this answers the review's MIX remark.
**Branch structure (exposed, not re-derived):** (i) D23P LF48-61 with CE1 P1: at z each x-row is of type (a') [k5 >= 1 =>
k5 = 4 and x_zt = 5], (b') [k3 >= 1 => k3 >= 2, no W'-entry 4 or 5, x_zt != 4; k3 = 2 => x_zp = 3 and the two other W'-entries
equal in {1,2}] or (c') [all W'-entries in {1,2,4} => 4-type]; the three cases are exhaustive (LF60). (ii) LF63-67: (a') is
impossible for alpha (inverse row of ones, LFC (d) of the inverted configuration) and for alpha* (alpha** = alpha). (iii) LF73:
(c')/(c') is excluded by D23-CENTER; by INV it suffices to exclude alpha (b')/alpha* (c'). (iv) LF76-84 position count (|T| = 4
impossible; |T| = 3: Q = {o, p}; |T| = 2: Q = {o1, o2}); LF86-97 M1 with CE1 P2a-P2c (LF464-524: exact tau tables; x in {3,4},
x* = 2, q_a = 2, X*_a subset X*_b after the joint normalisation g_z = g*_z = 1); LF99-108 M2 with CE1 P2d (LF526-538: D*_b lies in
Y*_a \ D*_a, of measure 1/6, against the 2/6 mass of the two D*_b). (v) LF110-112: both rows are of type (b'), which is the
statement. Every step uses actual exponents; no capping.
**Consumer bindings (clause of the statement used):**
| consumer | source line | clause used |
|---|---|---|
| A2-FIVE section 0 import | D/K7-A2-FIVE-v1.md LF23-27 | all clauses, both x |
| Lemma F (F1) | A2-FIVE LF53 | c = x_uz in {1,2,3} (u in W') |
| Lemma F (F3) | A2-FIVE LF61, LF65 | x_zu in {1,2,3}; k3 >= 2; k3 = 2 => x_zp = 3, other two equal in {1,2} |
| D23-a2 | A2-FIVE LF132 | x_zu in {1,2,3}; k3 >= 2; x_zt != 4 |
| FG-a2 (b) / Cor 5/6-a2 at u = p (marked apex) | A2-FIVE LF105, LF120-122 | beta_zu <= 3 on W' for beta = x*, an ACTUAL family: x*_zu in {1,2,3} |
| BRIDGE (B3) | A2-FIVE LF185-188 | beta_zu <= 3 on W' (no beta = 5 in (a2-no5)) |
| TRANSFER V2.7 (iv), FG-V at a = p | OV2 LF195-197 | beta_zu <= 3 on W' "by D23P for the alpha-matrix of C", C in {C^alpha, C^alpha*}: both families covered |
| BRIDGE (B3) adapted chain (V2.6) | OV2 LF130-147 | uses only pair parameters <= 4 of actual families; D23P not needed beyond (B3) |
| A2X Unit 2 S-data / FG-a2 interface | A/K7-A2-UNIT-2-v1.md LF15-22 | alpha*_zu in {1,2,3} (via accepted D23-a2/ZT5 S2, which use D23P) and FG-a2(b) for beta = alpha* |
| A2X Unit 3, (a2-no5) | A/K7-A2-UNIT-3-v1.md LF57-59 | FG-a2(b) at p for own and opposite actual families (beta_zt != 5, beta_zu <= 3 on W') |
**Disposition:** N1a proposed RESOLVED at the exposed-interface level (CANDIDATE_UNVERIFIED). The marked-apex gate
beta_zu <= 3 (u in W') is carried literally by "x_zu in {1,2} for u in W' \ T_x" together with the definition of T_x, for both
actual families; no auxiliary family and no beta = 5 is involved.

## 3. MAJOR1(b) — TC-P: literal TC.11 matrix hypothesis and consumers
**Accepted statement (OV1 Item TC.11 New, LF366-369; transferred by OV2 LF188 "for its stated matrix data"):** "No (a1)
configuration has alpha-rows ({2,2,4,4} | 3 | 2) at u3 and u5 with fours {u2, u4}, resp. {u4, u1}, together with
alpha*_(u4 u1) = alpha*_(u4 u2) = 4 and alpha*_(u4 u3) = alpha*_(u4 u5) = 2; in particular the abstract pattern Pc5' of
K7-A1-STRUCT-v1.md section 6 is not realised (also subsumed by K7-TC-A22)." Row notation (TC-v1 LF18-20): (W-multiset | c | e),
c = x_uz, e = x_ut. Pc5' data for reference only: A1-STRUCT LF138, LF142-143.
**Proof as accepted (OV2 V2.8 New, LF250-255):** R1 at u3 (every E >= 1, OV1 TC.4 LF272-275) gives L_u2^(u3) = L_u4^(u3);
Lemma TC at apex u4 in C^alpha gives D_u2 cap D_u3 empty; mu(D_u2) = 4/6, mu(D_u3) = 2/6 from the stated alpha* values; V4
contradiction. Scope labels: OV2 V2.9 (LF270-271), V2.10 (LF288-292), V2.11 (LF307-308).
**Consumers in the final chain: none.** The (a1) closure (R/sun7-K7-R2-parent-verdict-v1.md LF17) uses TC-A22 for Case A all-(2,2),
CASEA-K23 + CELL-A for the other Case A types, CASEB/TC-B/CASEB-T + CELL-B for Case B. TC-A22 mentions TC-P only as the
special case it generalises (D/K7-TC-A22-v1.md LF7-8). A2X Unit 3 (no5) uses Unit 1's own H_A theorem for Case A
(A/K7-A2-UNIT-3-v1.md LF64-69) and CASEB/TC-B + Unit 1 R1/K3/M_B for Case B (LF71-80); a search of Units 1-3, CASEA-K23, CELL,
R2E, ECFF, the R2 and A2X verdicts finds no TC-P application. **Disposition:** N1b proposed RESOLVED: the hypothesis is
displayed; TC-P is a retained TRANSFER-list item with no load-bearing consumer.

## 4. MAJOR1(c) — CELL: exact restated lemma, hypotheses, conclusions and consumers
**Accepted scope (R2 verdict LF15, LF31):** vertex-wise CELL at LK = G; CELL(i) needs no distinct-coset assumption; CELL(ii)/(iii)
retain their literal piece-index and disjoint-coset hypotheses. Reading order: CELLE C.1-C.4 (D/K7-CELL-erratum-v1.md LF10-58;
C.1 amended by ECFF R2.4 LF99-113, C.2 by R2E E2 LF75-93), ECFF R2.3 (LF83-97: IN for i != j), then R2E's CELL items (E15-E24).
**Literal Lemma CELL = R2E E18 New (LF428-457), summarised clause by clause without change:** K, L subgroups of index 3 with
**LK = G** (holds if some x has U_x subset L and m^K_x = 3; index 9 comes from LK = G, not from K != L).
- (i) [G : K cap L] = 9; c -> (cK, cL) is a bijection from the nine left (K cap L)-cosets ("cells") onto the pairs; the cell of
  (gK, hL) is gK cap hL. **Vertex-wise:** if U_v subset K and m^L_v = 3, then g_vU_v meets each of the three cells in g_vK, each
  piece g_vU_v cap c being a left coset of U_v cap L of index **n_v/3** in K cap L; symmetrically for U_x subset L, m^K_x = 3
  (index n_x/3). No assumption on which cosets such vertices occupy; the old three-distinct-coset form is a special case.
- (ii) For ANY vertex z, a nonempty piece g_zU_z cap c is a left coset of U_z cap K cap L, of index **N_z = [G : U_z cap K cap L]/9**
  in K cap L, with N_z = n_z [U_z : U_z cap K][U_z cap K : U_z cap K cap L]/9, both brackets integers <= 3; so every prime factor
  of N_z lies in {2, 3} or divides r_z.
- (iii) Three nonempty pieces of three DISTINCT vertices in one cell are, after left translation of the cell onto K cap L,
  **pairwise disjoint left cosets of subgroups of K cap L** (because the g_iU_i are pairwise disjoint); if their indices in
  K cap L have pairwise gcds <= 2 this contradicts Sun(3) (Zhu) inside K cap L. In particular, if in a cell the pieces of v and x
  and a possible piece of z have pairwise index gcds <= 2, then g_zU_z does not meet that cell.
**Index facts used with (ii) in (a1) (CELL-v1 LF74-75):** n_v/3 = 2 r_v with r_v = w_v for v in W and r_t = 3^A 5^Bt w_t; the
w's are coprime to 30 and Bz Bt = 0; hence for v, x in W and any third z: gcd(2 w_v, 2 w_x) = 2 and gcd(2 w_v, N_z),
gcd(2 w_x, N_z) divide 2.
**Consumer bindings:**
| consumer | source lines | CELL clauses and hypotheses used |
|---|---|---|
| CELL-A t-placement | CELL-v1 LF100-102 with C.2 New as amended by R2E E2 (LF89-92) | vertex-wise (i) (U_t subset K, m^L_t = 3; LK = G by E20) and (iii) with pieces v1/v2, t, u of indices 2w, 2 3^A 5^Bt w_t, 2w (pairwise gcd 2) |
| CELL-A cells and z | CELL-v1 LF102-105, E20 (LF493-494), E19 (LF474-477) | LK = G (U_x subset L, m^K_x = 3); (i) pieces of K- and L-vertices; (ii) for z's pieces + LF74-75 gcd facts; (iii) => z meets no cell of the v1/v2 K-cosets; then U_z subset K and the measure contradiction 1/3 < 1/2 |
| CELL-B | CELL-v1 LF126-131 with C.4 (LF56-57), E21 (LF510-511), E22 (LF527), E23 (LF543-545) | (i) with K := K', L := H and HK' = G; (iii) for t; (ii)/(iii) for z in v-columns; z in the t-column: N_z = [K' cap H : U*_z cap H] = n_z m^H_z/9 integral => m^H_z = 3, N_z = 2^(E+1) 5^Bz w_z; pairwise gcd 2 => (iii) contradiction |
| (a1) closure | R2 verdict LF17 | Theorems CELL-A, CELL-B at their stated hypotheses |
| A2X Unit 1 | A/K7-A2-UNIT-3-v1.md LF37-40 (Unit 1 export) | Unit 1 RE-PROVES its own CELL at the (a2) index arithmetic (LK = G, n_v/3 pieces, N_z = n_z ab/9 with a, b <= 3, Sun(3)); it imports no R2 CELL statement (A2X verdict LF13, LF17) |
**Disposition:** N1c proposed RESOLVED at the exposed-interface level: every hypothesis (index 3, LK = G, U_v subset K with
m^L_v = 3, distinct vertices, pairwise disjoint pieces) and conclusion (index 9, n_v/3, N_z formula and prime support, the
Sun(3) contradiction) used by a consumer is carried by E18 New and the consumer lines above.

## 5. MAJOR2(a)/(b) — registered reduction nodes (formerly unexposed inside CUT-v2 nodes 66-67)
| node | literal statement (source) | external inputs (node ids of section 7) | acceptance |
|---|---|---|---|
| P0/P1 (24) | README LF37-52 (proofs inline) and LF67 (gcd matrices) | 01 (L0.2, L0.6) | WV LF18-20 |
| R1(7) (25) | README LF56-65: a in {0,1,2}; (I) a <= 1, \|C\| >= 4, D uniformly type 2 or 3; (II) a = 2 | 01, 24, 15 (step 1: any six of seven cosets, all gcd 5), 14 (step 3: every 5-subset) | WV LF20, LF32 |
| R1a (26) | README LF71 | 02 (Sun(4)), 24 | WV LF21, LF32 |
| R1b (27) | README LF73 | 02 (Sun(3)), 24 | WV LF21, LF32 |
| R1c (28) | README LF75-79 (tuple (2r_1,4r_2,4r_3,4r_4), r's pairwise coprime, r_1 odd) | 01 (deletion), 09 (Prop 4.5 written, S56W section 3), 24, 27 | WV LF21, LF32 (statement); Prop 4.5 now from S56W (FCS site) |
| D2 (29) | rules-k7-v1 LF55-56: (I) type 2, \|C\| = 6, D = {d}, gcd(n_d, n_i) = 2 for all i in C => no CE. Proof: VFC at d, q_i = 1, d_i = n_i/2, local gcds 3, allowed sets <= 3 (Sun(4)), sum 3 contradicts VFC-count | 02 (Sun(4)), 05, 17, 24 | WV LF21, LF36; overlay item 2 (WV LF47: cite rules section 3) |
| D2' (30) | rules-k7-v1 LF58-61: (I) type 2, \|C\| = 5, D = {d1, d2} (D subset E by R1b), C cap E empty => no CE. Proof: VFC at d1; q in {1,2}: d' coprime to all C-indices (Sun(2): S_R = {d2}), C-pieces <= 3 (Sun(4)), union >= 1/4 + 5/6 > 1 vs (V4); q = 3: all six local gcds 3, 13/4 > 3 vs VFC-count | 01 (Sun(2)), 02 (Sun(4)), 05, 17, 24, 27 | WV LF21, LF36; overlay item 2 |
| COVER (31) | README LF85-103 class table and removals; COMP section 1 LF30-48 re-check | 25-30 | WV LF20-21 |
| BRIDGE-X1 (32) | addendum LF159: in a K5.3 CE take both D-vertices (r = n/3, odd since e = 0) and any three C-vertices (r = n/6); gcds 3/3/6 give pairwise coprime r's; by deletion they form an X1 configuration in the same group; no minimal frame | 01 (deletion, README LF25), 24 (K5.3 row README LF95; gcd matrix LF67) | WV LF24; X1 verdict LF5 |
| K53-EXCL (34) | X1 verdict LF5 statement applied to the BRIDGE output | 31, 32, 33 | X1 verdict LF5, LF26-29 |
**D2' stays necessary beside K52W:** K52W's literal scope is the exact README LF94 K5.2* matrix (R/sun7-K52W-parent-verdict-v1.md
LF9: "The larger D2-prime universe and KII are not certified here"); COVER removes the D2' case (C cap E empty) BEFORE the
K5.2* leaf (C cap E = {i*}). StageB's over-covering of D2' (R16 StageB verdict LF20) is historical only.

## 6. MAJOR2(c) — peripheral class-module closure from each module's own import declaration
Each row quotes the module's import declaration (with overlays) and maps every declared input to a node of section 7.
"Re-proved inside" means the module proves that input itself and imports no accepted package for it.
| node | module | own import declaration (file LF; overlays) | declared inputs -> nodes | status |
|---|---|---|---|---|
| 10 | C5W | S/continuations/core5-written-bridge/C5W-v1.md LF20-32 | Core(5) def; Lagrange/product/coset criterion (01); Sun(2) re-proved (01); Zhu Sun(3) (02); FC/INV re-proved | closed |
| 11 | C56W | S/continuations/core6-written-bridge/C56W-v1.md LF17-31 | definitions; 01; Sun(2) re-proved; Zhu Sun(3)/(4) (02); FC/INV re-proved | closed |
| 14-15 | S5W/S6W | S56W-v1 LF149-167 (with errata v1 item 1, v2 m2/m3/m6) | 01 (L0.1-L0.6, L1-L3, K2 with disjointness), 02, 03, 09, 10, 11, 12, 13 | closed |
| 16 | LFC | K7-LFC-INV-v1.md LF12-16 with E2/E3 | 01, 02, 03, 14, 15 (statement sites, FCS), 05 (INV only) | closed |
| 17 | VFC | rules-k7-v1 LF40-49; proofs WV LF34 + overlay item 3 (WV LF48) | 01, 02, 04, 05, 14, 15 | closed (old proof-v4/proof-k6-lemma citations NOT used) |
| 33 | X1 | R/x1-written-parent-candidate-v1.md LF12-18; clarification LF5-7; X1 verdict overlays LF19-20 | 01, 03, 04, 06, 07; pairwise fibre bound proved in the clarification (Sun(2) only) | closed |
| 35 | K52W | S/continuations/k52-written/K52-W-v1.md LF45-56 | 24 (README LF94 definition), 03, 01, 04, 02 (Sun(4)); FC24/INV re-proved | closed |
| 36 | KIIW | S/continuations/kii-written/KII-W-v1.md LF24-35 | 24 (README LF33-35, LF96), 03, 01, 02 (Sun(3)); FC23/INV re-proved | closed |
| 37 | K63-D | S/K63-D-v1.md LF6-11; erratum v2 H5 (LF28-33) | 03, 24 (K6.3 def), 16, 06, 01 (Sun(2)), 19 (K63-U0 Step 1 subset form), 18 (E8), 04 | closed |
| 38 | K63-E | S/K63-E-v1.md LF6-8; erratum v3 J5 (LF24-26) | as K63-D: 03, 24, 16, 06, 01, 19, 18, 04 | closed |
| 39 | K63-RES | S/continuations/k63-residue/K63-RES-v1.md LF7-19; erratum v2 items RESX1 (LF11-15: TG REMOVED, L0.1 + Lagrange instead) and RESX8 (LF61-73) | 03, 24, 01, 04, 16, 06, 17 | closed (TG is not an input) |
| 41 | K7-M0 | K7-LFC-INV-v1.md LF111-121 | 18, 06, 03 | closed |
| 42 | K7-M1 | S/K7-M1-v1.md LF7-11; erratum F1 (LF10-15) | 16, 06, 18, 04, 03 | closed |
| 43 | K7-Z2 | S/K7-Z2-v1.md LF7-16; erratum G1 (LF10-16), G5 (LF43-47), G6 (LF49-53) | 16, 06, 18, 20/21 (ROW-1, G2 transfer), 04, 07, 17, 08, 03, 01 | closed |
| 44 | K7-35 | S/K7-35-v1.md LF5-9; erratum v2 K4 (LF21-23) | 03, 16, 06, 01, 18, 20, 21, 04 | closed |
| 45 | K7-U1 | D/K7-U1-v1.md LF10-26 | 03, 24, 16, 06, 04, 18, 07, 17, 08 | closed |
| 46 | Z23-P5 | D/K7-Z23-P5-v1.md LF22-42 | 03, 24, 16, 06, 04, 18, 20, 21, 07, 17, 08 | closed |
| 47 | K7-NF | S/continuations/k7-complement-f/K7-NF-v1.md LF43-57 (internal SHAPE LF22-26, MK LF35-37, PART LF59-81) | 03, 24, 41-46 | closed; NF's "MK" is internal (not the pending K62-MK packet named in LF56) |
| 48 | D23-CENTER/MIX | D/K7-D23-NO4-v1.md LF30-52 with its erratum | 03, 16, 06, 18, 20, 21, 07, 17, 08 | closed |
| 49-50 | RICH | D/K7-D23-RICH-v1.md LF21-42 with erratum-1 R-1 and CE1 RF1-RF9 | 03, 24, 01, 16, 06, 04, 18, 07, 17, 48 (D23-MIX) | closed |
| 51 | D23P | D23P LF24-46 with CE1 P3a/P3b | section 2 | closed |
| 52 | A1-STRUCT | D/K7-A1-STRUCT-v1.md LF10-19 with OV1 A1.2-A1.4, A1.6 (+OV2 V2.1) | 49, 50, 03, 16, 06, 04, 18, 07, 17, 48 | closed |
| 53 | TC | D/K7-TC-v1.md LF11-20 with OV1 TC.1-TC.2 | 49, 50, 52, 16, 06, 17 | closed |
| 54 | TC-A22 | D/K7-TC-A22-v1.md LF5-16 with OV1 A22.1 | 49, 50, 52, 53 | closed |
| 55 | CASEA-K23 | D/K7-CASEA-K23-v1.md LF5-14 with K23E, ECFF R2.1-R2.2, R2E K23 items | 49, 50, 48, 16, 06, 17, 07, 03, 52, 53, 54 | closed |
| 56 | CELL | D/K7-CELL-v1.md LF5-13 with R2E E15 (adds L0.2, INV E6) | 52, 53, 54, 55, 49, 50, 16, 06, 17, 01, 04, 03, 02 (Sun(3), also in K cap L) | closed |
| 57 | (a1) closure | R2 verdict LF9-17, LF42-46 | 50 (TZ(iii)), 53, 54, 55, 56, 06, 03 | closed |
| 59-65 | A2-FIVE: FG-a2, F, D23-a2, ZT5, BRIDGE, TRANSFER | D/K7-A2-FIVE-v1.md LF22-36 with OV1 A2.1-A2.17 and OV2 V2.5-V2.7 | 51, 49, 50, 16, 06, 04, 01, 18, 07, 17 (and 52-54 for TRANSFER) | closed |
| 66 | A2X Unit 1 | A/K7-A2-UNIT-1-v1.md LF24-32 (+ unit1 parent erratum) | 03, 01, 04, 16, 06, 17, 07, 02 | closed |
| 67 | A2X Unit 2 | A/K7-A2-UNIT-2-v1.md LF7-24 (+ unit2 parent errata v1/v2) | 03, 01, 04, 16, 06, 17, 07, 59-63 | closed |
| 68 | A2X Unit 3 | A/K7-A2-UNIT-3-v1.md LF16-45 (+ unit3 parent erratum) | 66, 67, 59-65, 16, 06, 17, 07, 03; R2 verdict read for scope only | closed |
| 71 | E3 | K62/K62-E3-v1.md LF6-13 with erratum v2 Z1 (LF53-64) | 03, 24, 01, 04, 16, 06 | closed |
| 72-73 | DG | K62/K62-SH-DG-erratum-v1.md G1 (LF157-169; L1/VFC citations withdrawn) | 01, 04, 16, 06, 71 | closed |
| 74 | SH-1 disjointness (S2) | K62/K62-SH-DG-erratum-v1.md LF74-79 | 01, 06, 71 | closed |
| 75-76 | CAP-C1/C2, RC | K62/K62-CAP-v1.md LF9-18; CAP-DT erratum v1 CD2 (LF104-114), CD3 (LF131-154); erratum v2 V4-V7 (LF115-162) | 01, 04, 06, 16 (LFC (a)-(c)), 71 | closed at restricted interfaces |
| 77 | M13-A items 1-2 | K62/K62-M13-A-v1.md LF7-16; M13 verdict LF5; parent erratum status tags | 03, 01, 04, 16, 06, 71, 72, 73, 74; inherited envelope 07, 17, 75, 76 | closed (envelope retained) |
| 78 | K62X | S/continuations/k62-full-closure/K62-FULL-v1.md LF49-67 with parent erratum v2 item 3 (R/sun7-K62-FULL-parent-erratum-v2.md LF7) | 03, 24, 01, 04, 16, 06, 17, 71, 73, 77 | closed |
No declared input outside the node list was found. Names that collide are kept apart: NF's internal Lemma MK vs. the
pending K62-MK packet; K63-RES erratum items RESX1-RESX8 vs. the X1 tuple; S56W's elementary R1/K2 vs. R1(7) and the R2 lemma K2;
gate ids G5/G6 vs. DG corrections G5/G6.

## 7. MAJOR2(d) — reconciled topological order (79 nodes; every listed input has a smaller id)
| id | node | inputs |
|---|---|---|
| 01 | ELEM: Lagrange; L0.1 product formula; L0.2 coset criterion; L0.4/L0.5 granularity; L0.6 Sun(2); deletion; finite cores (README LF21-25 statements; written proofs S56W section 2 LF34-48, accepted; NOT the old sun-coset5 rules-v1 L0 citation) | — |
| 02 | ZHU Sun(3), Sun(4), every group (external) | — |
| 03 | R0 (README LF27-29; S56W LF143-147) | 01 |
| 04 | E1 (LFC-INV erratum LF12-19) | 01 |
| 05 | VFC (V1) (rules-k7-v1 LF41, LF46 first part) | 01, 04 |
| 06 | INV/E6/E7 | 01, 03, 04, 05 |
| 07 | L1 T1-T3 (rules-k7-v1 LF19-24) | 01, 04 |
| 08 | F7 only (addendum LF56-67) | 04, 07 |
| 09 | Prop 4.5 (S56W LF67-103) | 01, 03 |
| 10 | H5 = C5W | 01, 02, 03 |
| 11 | H6 = C56W | 01, 02, 03 |
| 12 | R1(5) (S56W LF106-115) | 01 |
| 13 | R1(6) (S56W LF126-137) | 01 |
| 14 | S5W | 02, 03, 09, 10, 12 |
| 15 | S6W | 02, 03, 09, 10, 11, 13 |
| 16 | LFC (a)-(d) | 01, 02, 03, 04, 14, 15 |
| 17 | VFC (V2)-(V4), count | 01, 02, 04, 05, 14, 15 |
| 18 | ROW-U/E8 (+ROW-U-deg, M1 erratum F3) | 04, 16 |
| 19 | K63-U0 (Step 1 subset form) | 06, 16, 18 |
| 20 | ROW-1 | 04, 16, 18 |
| 21 | ROW-1-deg (Z2 G2) | 16, 20 |
| 22 | ROW-2 | 16, 18 |
| 23 | ROW-2 marked-apex transfer (CE1 P1) | 16, 22 |
| 24 | P0/P1 and class definitions (README LF31-52, LF67, LF85-96) | 01 |
| 25 | R1(7) | 01, 14, 15, 24 |
| 26 | R1a | 02, 24 |
| 27 | R1b | 02, 24 |
| 28 | R1c | 01, 09, 24, 27 |
| 29 | D2 | 02, 05, 17, 24 |
| 30 | D2' | 01, 02, 05, 17, 24, 27 |
| 31 | COVER | 25, 26, 27, 28, 29, 30 |
| 32 | BRIDGE-X1 | 01, 24 |
| 33 | X1 | 01, 03, 04, 06, 07 |
| 34 | K53-EXCL | 31, 32, 33 |
| 35 | K52W | 01, 02, 03, 04, 24 |
| 36 | KIIW | 01, 02, 03, 24 |
| 37 | K63-D | 01, 03, 04, 06, 16, 18, 19, 24 |
| 38 | K63-E | 01, 03, 04, 06, 16, 18, 19, 24 |
| 39 | K63-RES | 01, 03, 04, 06, 16, 17, 24 |
| 40 | K63-EXCL (3-way split) | 37, 38, 39 |
| 41 | K7-M0 | 03, 06, 18 |
| 42 | K7-M1 | 03, 04, 06, 16, 18, 20 |
| 43 | K7-Z2 | 01, 03, 04, 06, 07, 08, 16, 17, 18, 20, 21 |
| 44 | K7-35 | 01, 03, 04, 06, 16, 18, 20, 21, 22 |
| 45 | K7-U1 | 03, 04, 06, 07, 08, 16, 17, 18, 24 |
| 46 | Z23-P5 | 03, 04, 06, 07, 08, 16, 17, 18, 20, 21, 24 |
| 47 | K7-NF (internal SHAPE/MK/PART) | 03, 24, 41, 42, 43, 44, 45, 46 |
| 48 | D23-CENTER/MIX | 03, 06, 07, 08, 16, 17, 18, 20, 21 |
| 49 | RICH G0/FG7/Cor 5/6 | 01, 03, 04, 06, 16 |
| 50 | RICH NO5/R3/TR/CC/theorem/TZ/LZ | 06, 07, 16, 17, 18, 48, 49 |
| 51 | D23P | 03, 04, 06, 07, 08, 16, 17, 23, 48 |
| 52 | A1-STRUCT sections 0-5 | 06, 07, 16, 17, 18, 48, 49, 50 |
| 53 | TC (TC, FG-V, R1-R5, TC-B, TC-P) | 06, 07, 16, 17, 49, 50, 52 |
| 54 | TC-A22 | 16, 17, 49, 50, 52, 53 |
| 55 | CASEA-K23 / CASEB-T | 03, 06, 07, 16, 17, 48, 49, 50, 52, 53, 54 |
| 56 | CELL, CELL-A, CELL-B | 01, 02, 03, 04, 06, 16, 17, 49, 50, 52, 53, 54, 55 |
| 57 | (a1) closure | 03, 06, 50, 53, 54, 55, 56 |
| 58 | K7-REM | 47, 57 |
| 59 | FG-a2, Cor 5/6-a2 | 01, 04, 06, 16, 49, 51 |
| 60 | Lemma F (F1)-(F5) | 06, 16, 18, 51 |
| 61 | Lemma F (F6)-(F7) | 06, 16, 18, 59, 60 |
| 62 | D23-a2 | 06, 16, 51, 60 |
| 63 | ZT5 (S1)-(S5) | 01, 06, 16, 49, 60, 61, 62 |
| 64 | BRIDGE A2.10 (exact list) | 06, 07, 16, 17, 49, 50, 59, 62 |
| 65 | TRANSFER V2.7 (exact list, section 1) | 51, 52, 53, 54, 59, 64 |
| 66 | A2X Unit 1 | 01, 02, 03, 04, 06, 07, 16, 17 |
| 67 | A2X Unit 2 | 01, 03, 04, 06, 07, 16, 17, 59, 60, 61, 62, 63 |
| 68 | A2X Unit 3 | 01, 03, 06, 07, 16, 17, 59, 60, 61, 62, 64, 65, 66, 67 |
| 69 | A2X (accepted join) | 66, 67, 68 |
| 70 | K7-EXCL (K7-SPLIT + K7-REM + A2X) | 24, 58, 69 |
| 71 | E3 | 01, 03, 04, 06, 16, 24 |
| 72 | DG-1..DG-4 | 01, 04, 06, 16, 71 |
| 73 | Theorem DG (G5/G6) | 71, 72 |
| 74 | SH-1 disjointness argument (SH-DG erratum S2) | 01, 06, 71 |
| 75 | CAP-C1/C2 (own entry 1 / f* = 1) | 01, 04, 06, 71 |
| 76 | RC-O / RC-i* (nonstrict) | 01, 04, 06, 16, 75 |
| 77 | M13-A items 1-2 (envelope 07, 17, 75, 76 retained) | 01, 03, 04, 06, 07, 16, 17, 71, 72, 73, 74, 75, 76 |
| 78 | K62X | 01, 03, 04, 06, 16, 17, 24, 71, 73, 77 |
| 79 | SUN7-COND (final composition join) | 03, 31, 34, 35, 36, 40, 70, 78 |
**Reconciliation with CUT-v2 (68 nodes):** CUT-v2 nodes 01-07 -> 01-04, 06-08 (VFC (V1) split out as 05); 08 -> 09; 09-14 -> 10-15;
15-16 -> 16-17; 17-23 -> 18, 20-23 with K63-U0 (19) added; CUT-v2 node 66 (six-class reduction) is now split into 24-31 (P0/P1,
R1(7), R1a, R1b, R1c, D2, D2', COVER); CUT-v2 node 67 is now 32 (BRIDGE-X1) + 33 (X1) + 34 (K53-EXCL); the SH-1 argument (74) and
K7-EXCL (70) are explicit; CUT-v2 68 -> 79. Net: 68 -> 79. Every input in every row of section 6 occurs as a node id here.
**Acyclicity** at this registered boundary holds by inspection of the table (each row's inputs are smaller ids). Whether
any import of an accepted module is still missing from its own declaration is exactly what the parent/second-family review of
Part B must check; this file does not certify completeness.

## 8. Dispositions, gates and non-claims
| key | proposed disposition (CANDIDATE_UNVERIFIED) |
|---|---|
| m3 | resolved (section 1) |
| N1a D23P | resolved at exposed interface (section 2) |
| N1b TC-P | resolved: hypothesis displayed; no final-chain consumer (section 3) |
| N1c CELL | resolved at exposed interface (section 4) |
| N2a D2/D2' | registered (section 5) |
| N2b deletion bridge | registered (section 5) |
| N2c peripheral closure | closed at declared-import level (section 6); no undeclared input found |
| N2d graph | 79-node order (section 7) |
| C1 S56W status | accepted statements used only via FCS sites |
| C2 M12 | Codex 0F/0M/0m; conditional dual gate |
Still required before any completeness certification: parent/second-family review of this file's parts A/B, the second-family
disposition of M12, the COMP-U0 metadata overlay (SUN7-COMP-erratum-v3.md) and the final composition review. Not claimed:
full Sun(7); acceptance of CUT-v3 or of any candidate; that historical Sun(5)/Sun(6)/StageB records are computation-free;
novelty, Lean, human review or runtime authority. Old records unchanged.
