# PURE-A corners in columns 2 and 3 are excluded — CANDID2026-10-19T18:33:19-0700E v1

Frozen at AT under `SCOPE-FREEZE-v1.json`, SHA256 `f89e1245aea8b7955f5beab855ef1313f7b13cd6ae2a3b66855b8339d532b9bf`. This is written mathematics, not a reviewed or accepted result. No scientific scripts, assertions, enumeration, numerical checks, or nested agents were used. No prior candidate is a premise.

## 0. Exact statement and outcome

Let Q_1,...,Q_5 be five actual pairwise-orthogonal QLS(8), in the B3 normal form specified below. For every r ∈ {1,7} and c ∈ {2,3}, the entry Q_1(r,c) is not a vector entirely in V_A := span{e_1,e_2,e_3}.

Thus the PURE23 family is excluded: no pure-A corner occurs in column 2 or 3. All B3 axes and phases of squares 2..5 and all general interior vectors are retained. The proof treats c ∈ {2,3} uniformly; it never interchanges either of these columns with column 1, and it does not rely on a 2/3 symmetry.

This settles this assigned subfamily by exclusion, not by a partial assignment. It does not exclude a pure-A corner in column 1, configurations with A-free/mixed corners, the whole of B3, or order 8. It makes no Boolean/GB claim and changes no computed status.

## 1. Hypotheses, notation and elementary tensor consequences

**H1 (actual QLS and orthogonality).** Every row and column of each Q_s is an orthonormal basis of C^8. For each s != t, the 64 vectors Q_s(i,j)⊗Q_t(i,j) are an orthonormal basis of C^8⊗C^8. In particular, for distinct cells z,z',

    <Q_s(z),Q_s(z')> <Q_t(z),Q_t(z')> = 0.                 (T)

The inner product is conjugate-linear in the first variable. Phases below always have modulus one.

**H2 (standard row 0).** Q_s(0,d) = w_{s,d} e_d, for every square s and coordinate d ∈ {0,...,7}.

**H3/H4 (only axis assumptions used).** Let q_s^i := Q_s(i,0), and abbreviate q^i := q_1^i. Then

    supp(q^1) = supp(q^7) = {1,2,3},
    supp(q^6) = {2,3}.                                   (B3)

The support of q^1 is the SB2 premise, not a conclusion of the template row list. The supports of q^6,q^7 are the last two P1-B3 template rows. The other SB2 assignments and the other template rows are not needed. We do not re-prove that any more general configuration can be normalized to (B3); the theorem is conditional on exactly this stated subfamily.

Put A := {1,2,3}, W := {4,5,6,7}, D := {0}∪W, P_A := orthogonal projection onto V_A. For a chosen r ∈ {1,7}, let r' be the other member. Column-0 orthonormality implies that q^1,q^6,q^7 form an orthonormal basis of V_A. Therefore

    P_r := V_A ∩ (q^r)^⊥ = span{q^6,q^{r'}}.              (1)

We use the following consequences, each proved directly.

**C1 (column zero coordinate).** At an interior cell (i,j), every square has zero coordinate j, by its column's orthogonality to Q_s(0,j) = w e_j.

**C2 (common-coordinate exclusivity).** At an interior cell z=(i,j), for every coordinate d, at most one square has a nonzero coefficient on e_d. For d=j this follows from C1. For d!=j, apply (T) to z and (0,d). The phases w are nonzero, so two nonzero coefficients in different squares would contradict (T). This includes d=0 by using (0,0).

**C3 (own-index exclusivity).** For any interior z=(i,j) and any k != i, at most one square has <q_s^k,Q_s(z)> != 0. Apply (T) to (k,0) and z. This shares the index k across the squares; it never identifies their physical vectors q_s^k.

**C4 (axes of the other squares).** For s>=2,

    q_s^1,q_s^7 ∈ span{e_d : d∈W},
    q_s^6 ∈ span{e_1,e_4,e_5,e_6,e_7}.                   (2)

Proof: apply C2 at (r,0), equivalently (T) to (r,0) and (0,d), for each d in supp(q^r). Square 1's nonzero coefficients force the other squares' coefficients there to vanish. Also q_s^i⊥q_s^0∝e_0 when i!=0. Thus (B3) gives (2).

In fact, for r∈{1,7}, the four vectors q_s^r, s=2,...,5, have nonempty disjoint supports in the four-set W, again by (T) at (r,0),(0,d). Hence

    q_s^r = phase · e_{p_s},   q_s^{r'} = phase · e_{t_s}, (3)

where (p_s)_{s=2}^5 and (t_s)_{s=2}^5 are each bijections onto W. For every s, p_s!=t_s by column-0 orthonormality. Nothing below fixes either bijection or an axis phase.

Finally, at most one square among s=2,...,5 has q_s^6 proportional to e_1: two such squares would contradict (T) at (6,0),(0,1). More generally, at most one has any nonzero e_1 coefficient.                 (4)

## 2. Corner-line calculation (re-proved)

Write q^r = Σ_{d∈A} a_d e_d, where every a_d!=0. At (r,c), c∈A, C1 and row orthogonality give

    P_A Q_1(r,c) ∈ V_A ∩ {e_c,q^r}^⊥ = span{ell_c},
    ell_c := conjugate(a) × e_c.                         (5)

Explicitly, in coordinates (e_1,e_2,e_3),

    ell_1 = (0, conjugate(a_3), -conjugate(a_2)),
    ell_2 = (-conjugate(a_3), 0, conjugate(a_1)),
    ell_3 = (conjugate(a_2), -conjugate(a_1), 0).

Each is nonzero, orthogonal to q^r and e_c, and has support exactly A\{c}. The intersection in (5) is one-dimensional because q^r is not parallel to e_c. Direct multiplication gives, for b!=c,

    <ell_c,ell_b> = -a_b conjugate(a_c) != 0.             (6)

Let u be a unit vector on ell_c, and let m be a unit vector in the two-dimensional plane P_r orthogonal to u. Then supp(m)=A. Indeed, if m had a zero coordinate b, (5) applied to that coordinate would make m parallel to ell_b. If b=c it would be parallel to u, impossible. If b!=c it would not be orthogonal to u by (6), also impossible.

For c∈{2,3}, both u and m have nonzero coefficients on both q^6 and q^{r'} in (1). For u:
- u cannot be proportional to q^6, since u has nonzero coordinate 1 whereas q^6 does not;
- u cannot be proportional to q^{r'}, since u has zero coordinate c whereas q^{r'} has nonzero coordinate c.
In a two-dimensional orthonormal basis, the orthogonal complement of a vector with two nonzero coefficients also has two nonzero coefficients. Thus the assertion holds for m as well.                             (7)

This is the place where column 1 differs: u is proportional to q^6 for c=1, and (7) would be false. No column-1 result is inferred here.

## 3. A pure corner forces a second pure-A entry in its row

Suppose, toward a contradiction, that y=(r,c), with c∈{2,3}, is pure-A. Up to its phase Q_1(y)=u.

Every other interior row-r entry has its A-part in span{m}: it is orthogonal to q^r and to u. In the other two corner columns b∈A\{c}, this A-part also lies on ell_b, so is zero by (6). Hence any additional nonzero A-parts occur at columns in W and are multiples of the full-support vector m.

Row-r orthonormality gives the projected resolution

    Σ_{j=1}^7 P_A |Q_1(r,j)><Q_1(r,j)| P_A
      = P_A - |q^r><q^r| = |u><u| + |m><m|.             (8)

Thus the other entries carry m-mass exactly one. Let k>=1 be their number. A support-incidence count forces k=1:
- Interior row r has 18 available A-slots: two at each column 1,2,3 and three at each column in W, by C1.
- By C4, q_s^r⊥V_A for s>=2. Their row resolutions therefore give mass one on each of e_1,e_2,e_3. Each of these twelve (square,coordinate) demands uses at least one A-slot.
- Square 1 uses two A-slots at y and three at each of the k other A-carrying entries, because supp(m)=A.
- C2 makes all these slots disjoint across squares. Consequently

      2 + 3k + 12 <= 18,  hence k=1.                    (9)

Call the unique other cell x=(r,j), j∈W. Equation (8) gives |<m,Q_1(x)>|^2=1. Since Q_1(x) is unit, it is a phase times m, with no orthogonal remainder. Both x and y are pure-A. By (7), square 1 has nonzero own coefficients 6 and r' at both cells. Therefore C3 gives, for all s>=2,

    Q_s(x), Q_s(y) ⊥ q_s^6, q_s^{r'}.                   (10)

This is derived from the genuine tensor equations, not from a support-only relaxation.

## 4. Saturation at x and the three-versus-one contradiction at y

Square 1 occupies all A-coordinates at x. The four other squares there have no A-coordinate by C2, and no coordinate j by C1. They are unit vectors with nonempty disjoint supports in the four-set D\{j}. Hence

    Q_s(x) = phase · e_{d_s},
    {d_s : s=2,...,5} = D\{j},                          (11)

with all d_s distinct. Exactly three of the d_s belong to W; let I be those three squares.

Fix any s∈I. From (3), row-r orthogonality, and (10),

    d_s != p_s,   d_s != t_s,   <q_s^6,e_{d_s}> = 0.     (12)

The three elements p_s,t_s,d_s of W are therefore distinct. Let h_s be the unique remaining element of W. By C4, q_s^6 has no coordinates 0,2,3. Column-0 orthogonality makes it orthogonal to q_s^r∝e_{p_s} and q_s^{r'}∝e_{t_s}. Equation (12) removes coordinate d_s. Thus

    q_s^6 = alpha_s e_1 + beta_s e_{h_s}.                (13)

At y, square 1 occupies A\{c} and C1 excludes coordinate c. Thus Q_s(y) has no A-coordinate. Row orthogonality removes e_{p_s} (against q_s^r) and e_{d_s} (against Q_s(x)); (10) removes e_{t_s}. It follows that

    Q_s(y) ∈ span{e_0,e_{h_s}}.                         (14)

By (10) and (13), if beta_s!=0 then the e_{h_s} coefficient of Q_s(y) is zero. As Q_s(y) is unit,

    beta_s!=0  implies  Q_s(y)=phase · e_0.              (15)

If beta_s=0, the unit vector (13) is proportional to e_1. By (4), this happens for at most one square in I. There are three squares in I. Thus at least two have beta_s!=0, and (15) forces both of their vectors at y onto e_0. This contradicts C2 at y (coordinate 0), equivalently (T) at y,(0,0).

The contradiction excludes every possible choice of r∈{1,7}, c∈{2,3}, j∈W, both bijections (p_s),(t_s), all phases and all remaining axes and vectors. QED.

## 5. Complete tensor-pair ledger and scope boundary

Every tensor use in the proof has the following form. The relevant cells are distinct and have different rows and columns; entries in square s are never replaced by square 1's physical vectors.

| Use | Cell pair | Consequence |
|---|---|---|
| C2 at an interior z=(i,j) | z,(0,d), d!=j | common-coordinate exclusivity, including d=0 |
| C3 at z=(i,j) | z,(k,0), k!=i | own-index exclusivity |
| C4 at rows r,r' | (r,0),(0,d) or (r',0),(0,d), d∈A | other-square axes avoid A |
| C4 at row 6 | (6,0),(0,d), d=2,3 | other-square q_s^6 avoids e_2,e_3 |
| Singleton axes in (3) | (r,0),(0,d) and (r',0),(0,d), d∈W | four disjoint supports in W |
| At-most-one in (4) | (6,0),(0,1) | at most one other q_s^6 contains e_1 |
| Equation (10) at x | x,(6,0) and x,(r',0) | Q_s(x)⊥q_s^6,q_s^{r'} |
| Equation (10) at y | y,(6,0) and y,(r',0) | Q_s(y)⊥q_s^6,q_s^{r'} |
| Support saturation at x | x,(0,d), d∈A or d∈D\{j} | no A and four distinct singleton D\{j} supports |
| No A at y | y,(0,d), d∈A\{c} | other squares avoid A\{c}; coordinate c excluded by column orthogonality |
| Final contradiction | y,(0,0) | two other squares cannot both be proportional to e_0 |

Only row/column orthonormality is used for the remaining steps. Neither a candidate no-all-mixed theorem nor any classification, absorption claim, Latin completion, finite enumeration, numeric control or native result is imported.

**Remaining full-grid problem.** This proof excludes only PURE23. It does not decide column-1 pure corners, A-free/mixed corner patterns, or full B3 compatibility. The previous column-1 partial assignment is not used, extended, accepted or relabelled here. A pure-A entry in column 1 lacks the two-own-index property (7), so the argument would fail exactly at (10) and (13); we do not fill that gap by symmetry.

No actual partial assignment of rows 0,1,7 and column 0 is claimed. Such an assignment satisfying all the hypotheses and the equations used above would already contradict the proof if it contained a PURE23 corner. The alternative deliverable route is therefore not needed.

## 6. Source and import table

- [PRIM] defines QLS and mutually orthogonal QLS: physical LF195–225. Imported definition only.
- [J] pins the P1-B3 template rows q^6,q^7. Imported support assumptions only, not the Boolean formula or its status.
- [NF] records the attribution of q^1's support to SB2 at physical LF109. Imported support assumption only, not its model-transformation proof.
- [SC] and [TR] freeze the assigned subfamily and written-only authority.

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [NF] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md`, SHA256 `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure23-corner/SCOPE-FREEZE-v1.json`, SHA256 `f89e1245aea8b7955f5beab855ef1313f7b13cd6ae2a3b66855b8339d532b9bf`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-B3-pure23-corner-transition-v1.json`, SHA256 `1fd51059a88098c559981271dcba098de599d507d2c139723d4797f7051c46dc`.
