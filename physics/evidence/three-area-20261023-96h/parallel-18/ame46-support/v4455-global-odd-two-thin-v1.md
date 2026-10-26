# Candidate v1 — a three-block odd relation closes the retained whole-v4455 residual

Actual `/bin/date` before creation: **Sun Oct 25 03:57:47 PDT 2026**. Owner PhysicsAME46, physics-6. **WRITTEN CANDIDATE; exact local integer identities checked in the owner's eval kernel. Fresh independent reconstruction and parent acceptance have NOT been performed.** This is a new immutable successor, not an edit of either reviewed source.

## 1. Result, imports and unchanged numerical boundary

For every actual flagged support in the retained h12/t24/e0/support48/v4455 residual, there are THREE actual closed blocks, one from each flattening, whose signed rows have an exact relation with three coefficients in `{1,-1}` and ODD sum. In particular GLOBAL-ODD from the earlier phase packet holds over this entire residual at the imports below.

The new mechanism is local and does not enumerate officer forests:

1. In a no-Hamming1 e0 support whose thin slices are parity tetrahedra, a non-officer site carrying TWO thin coordinate values forces a six-site, three-block odd relation.
2. Every retained v4455 profile has at least seven thin values. Their four-site slices give at least28 thin incidences on24 non-officer sites, so some site has at least two thin values.
3. The exact integer relation excludes complex phase realizability, including unequal original non-officer moduli, by the earlier per-support theorem.

Thus no complex-realizable support, concrete feasible18x24 matrix, or AME tensor can be supplied INSIDE this residual if the new proof and its named imports are correct. This does NOT exclude every other support48 stratum, and is NOT a lower49 claim. The documented unrestricted interval remains **48..60**. Novelty remains UNCLEAR.

### Named imports and current SHA-256 pins

- `v4455-global-structure-v1.md`: `47150687f15b8271fa153ea04be0eacc530a7f54713422fa55f423f4e8e07d78`.
- `v4455-joint-phase-criterion-v1.md`: `985d0a41bb61decdc21d5dec74d4ae6e6ab41944e922531c012e3cdb1cd06795`.
- Run-root `wave-v18-v4455-structure-parent-v1.md`: `ae87667f606808055f386ae1233439b8ea385900a9965a40b2f8fb9e6b40a258`.
- Run-root `wave-v26-ame-joint-phase-parent-v1.md`: `381d2698b34cbce024e936d21a3f9639ddedd43c39b769653c8ccfae4498f4a0`.

The first source and its parent supply the GLOBAL no-Hamming1 theorem, every actual thin parity tetrahedron, and the complete P/Q, P/R, Q/Q, Q/R residual including both Q/Q shapes, all officer extensions/labels, exceptional c1/c4 placements and F/E possibilities. The second source and its parent supply the single globally shared phase matrix and exact odd-INTEGRAL-relation obstruction. No old finite certificate, QLS6 classification, no-AME(4,2), Smith computation, conjectured basis minimality or feasible-support hypothesis is newly imported here.

The resumption authority permits exact in-kernel integer arithmetic. No native scientific program, solver, CAS, external model CLI, background job, nested agent, git operation or file deletion was performed. The global scientific-launch HOLD and original deadline remain binding.

## 2. Explicit simultaneous hypotheses for the new local theorem

The local theorem can be stated independently of the officer-forest classification. Let N be one literal set of nonzero tensor positions. Require:

- Every officer-free pair-value line has EXACTLY two N sites, and officer lines have none.
- In each of12|34,13|24,14|23, every N component is an actual CLOSED K2,2 block with four physical positions. The same N is used in every cut.
- N has no Hamming-distance-one pair.
- Every deficit2 value has a four-site slice that is an actual parity tetrahedron: in its other three coordinates it uses two values each, with full2x2 projection onto each pair.

Every retained v4455 support satisfies these predicates at the named structural import. They are not inferred merely from deficit profiles or independently supplied rectangles.

For any actual block, orient its rows/columns and assign its signed row

    e_a - e_b - e_c + e_d

for corner array `[[a,b],[c,d]]`. An orientation reversal may negate this row. Every physical N site is one global column. The earlier phase theorem says every such row b obeys

    b theta = pi  (mod 2pi).

This is valid for arbitrary original complex moduli, before equalization.

## 3. TWO thin values force a literal six-site relation

Suppose p in N has two thin coordinate values. Permute parties to call these C=0 and D=0, with the other parties A,B. Numerical0/1 labels below are LOCAL labels for the two actual values in each coordinate; they do not assert a common alphabet between parties.

The exact-two line fixing C=D=0 contains p and a unique second point q. They must differ in BOTH A and B: equality in either would give Hamming distance1. Relabel their A/B values so that

    p=(0,0,0,0),
    q=(1,1,0,0).

### 3.1 The two actual tetrahedra determine four more positions

The thin C=0 slice contains p,q. Its two A-values and two B-values are already fixed. Its other D-value is some value different from0; label it1. The parity-tetrahedron property forces its remaining two positions to be

    r=(0,1,0,1),
    s=(1,0,0,1).

Indeed, in the three varying coordinates A,B,D, p and q have D=0 and opposite A/B bits. The unique parity tetrahedron through them places the other two A/B pairs at D=1.

Likewise the thin D=0 slice has some second C-value different from0, labeled1, and forces

    u=(0,1,1,0),
    v=(1,0,1,0).

All six positions p,q,r,s,u,v are actual distinct sites in the ONE set N. These two tetrahedra are not chosen separately from the global support.

### 3.2 Actual closure forces one shared fourth corner

In cut AC|BD:

- p,r have the SAME row AC=(0,0) and exhaust its two entries;
- p,v have the SAME column BD=(0,0) and exhaust its two entries.

The actual K2,2 component through p therefore has corner array

    K_AC = [[p,r],
            [v,w]],       w=(1,1,1,1).

Thus w is an actual N site. There is no free fourth-corner choice.

In cut AD|BC, p,u have the same row AD=(0,0), and p,s have the same column BC=(0,0). Its actual closed block is

    L_AD = [[p,u],
            [s,w]].

The fourth corner is the SAME physical position w=(1,1,1,1), not a separately assigned variable.

Finally, in cut AB|CD, r,u exhaust row AB=(0,1), and r,s exhaust column CD=(0,1). Closure gives the actual block

    M_AB = [[r,u],
            [s,v]].

The required fourth corner v is already present from the D tetrahedron. Each listed row/column has exactly its two named nonzero entries, so no extra component coefficient can alter these three four-site equations. q was needed to align the tetrahedra but is not in this local relation.

### 3.3 Exact integral cancellation, with an ODD coefficient sum

Use the global site order beginning p,r,s,u,v,w. The three block rows are

    K = e_p - e_r - e_v + e_w,
    L = e_p - e_u - e_s + e_w,
    M = e_r - e_u - e_s + e_v.

Therefore the exact INTEGER identity is

    K - L + M = 0.

The relation coefficients are `(1,-1,1)`, whose sum is1. All other columns vanish because each of these actual blocks has exactly its listed four positions. All other block coefficients are zero.

Equivalently, the visible3x6 submatrix and its certificate are

    site order: p  r  s  u  v  w
    K:          1 -1  0  0 -1  1
    L:          1  0 -1 -1  0  1
    M:          0  1 -1 -1  1  0
    z:          (1,-1,1).

For the full18x24 matrix, embed these three rows and six physical columns at their actual indices and put zero on the other15 relation coefficients. This gives B^T z=0 in ALL24 columns and odd total. This is a support-independent construction of a certificate FROM the forced positions, not a fabricated concrete18x24 matrix for a nonexistent global support.

Any orientation changes multiply the corresponding row and certificate coefficient by the same sign. The nonzero certificate still has exactly three odd entries, so its total is odd regardless of those choices. Party permutations likewise preserve the construction.

Applying the three phase equations with these coefficients gives

    0 = (1-1+1)pi = pi  (mod 2pi),

which is impossible. This proves:

> **Two-thin theorem.** Under the simultaneous support hypotheses in Section2, any site with two thin coordinate values supplies an explicit three-block odd integral relation. Consequently, in a complex-realizable such support, EVERY N site carries at most ONE thin value.

No assumption about equal original moduli, a real-sign alphabet or local-unitary equivalence was used.

## 4. Uniform incidence inequality and the ENTIRE v4455 residual

Let m be the TOTAL number of deficit2 values over all four coordinates. Every thin value has exactly four N sites. Thus the total thin-value incidence is exactly4m.

If there were no site with two thin values, each N site would contribute at most1, giving

    4m <= |N| = 2h.

Hence every complex-realizable no-Hamming1 e0 support with thin tetrahedra satisfies the stronger necessary inequality

    2m <= h.

For the present h12/N24 stratum this is m<=6. The retained profiles have:

| Four-axis pair | Five-axis pair | Thin-value count m | Thin incidences4m |
|---|---|---:|---:|
| P/Q | F/F | 0+1+3+3=7 | 28 |
| P/R | F/F | 0+2+3+3=8 | 32 |
| Q/Q, either forest shape | F/F | 1+1+3+3=8 | 32 |
| Q/R | F/F | 1+2+3+3=9 | 36 |
| P/Q | E/F, either five-axis order | 0+1+4+3=8 | 32 |
| Q/Q, either forest shape | E/F, either order | 1+1+4+3=9 | 36 |

Here P=(3,3,3,3), Q=(4,3,3,2), R=(4,4,2,2), F=(3,3,2,2,2), E=(4,2,2,2,2). P/R and Q/R have no E branch at the structural import; the allowed c1/c4 restrictions are unchanged.

Every row violates m<=6. For EVERY actual retained support, pigeonhole therefore supplies a point with two thin values, and Section3 constructs its odd relation. No choice of forest labels, exterior officer extension, thin tetrahedron, exception placement or complex phase evades this argument. It does not require that any residual combinatorial support actually exists.

> **Whole-residual conclusion (WRITTEN candidate).** GLOBAL-ODD holds for every actual C1/C2 support in the retained v4455 residual, at the named structural imports. Every such support has a certificate with exactly THREE coefficients in `{1,-1}`. The entire h12/t24/e0/support48/(4,4,5,5) AME stratum is excluded.

This is stronger than an isolated special odd-support class: the existing global structure forces the local odd class somewhere in EVERY residual support.

## 5. Exact in-kernel checks: exercised scope, not formal proof

The owner used exact integers in its own eval kernel for these finite checks only:

1. The six displayed positions, each of the three cut-specific corner arrays, and the resulting signed3x6 matrix were constructed literally. All row/column labels in each2x2 array were checked.
2. The multiplication by z=(1,-1,1) yielded exactly six zeros, with sum(z)=1. Padding the selected rows by18 zero columns yielded24 exact zeros.
3. A known-true single-square checkerboard row was checked to have sum0. A one-coefficient mutation of K changed the image to `[-2,0,0,0,0,0]`; the cancellation check rejected it.
4. The two displayed four-site slices were checked to have all four pairs in each of their three pair projections. Their literal seven-site union with w has no Hamming-distance-one pair.
5. The six profile rows above were checked using integer lists: every axis deficit sum is12, m is7,8,8,9,8,9 and4m is28,32,32,36,32,36 respectively.

The coordinate forcing, universal quantification and import applicability remain WRITTEN arguments. These arithmetic checks are not proof-assistant/kernel verification, a native certificate consumer, exhaustive support enumeration, rank/Smith computation, independent code, cross-vendor review or human review. No18x24 feasible B or all-six-marginal tensor was computed.

## 6. Constructive branch and lower49 boundary

The requested concrete complex-realizable48-site support cannot lie in the retained residual if this theorem is correct: it would give BOTH an odd integral relation and a complex phase solution. Consequently no fake modulus-equalized tensor or marginal claim is offered here. The earlier roots-of-unity construction remains valid on other admissible supports that have no odd relation; it is simply not attainable in this residual.

This is a lower49 ATTEMPT, not a lower49 theorem. For support48, e=t-24. The present result treats only t24/e0 with active sizes(4,4,5,5), using the parent-supported no-Hamming1/thin structure. The parity theorem must not be applied blindly to positive-excess supports, where lines can have more than two entries and actual components need not be closed2x2 blocks. Nor does this proof supply a complete inventory/exclusion of other t24/e0 active-size patterns.

The park record will retain the exact missing unrestricted bridge. Fresh reconstruction should first check Section3's forced corner arrays, that the SAME w occurs in both cuts, and the support-complete cancellation K-L+M=0; then verify Section4 against the parent-supported residual list. No old reviewed packet is changed and no review verdict is transferred to this new hash.
