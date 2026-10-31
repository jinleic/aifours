# RQLS10 v20 — an unrestricted sparse-partner escape inequality for the ACTUAL remaining sectors

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 07:07:07 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact orthogonality/context/graph/integer arguments only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private decimal/approximate scout or discarded-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

The original maximal1-RQLS10 remains UNKNOWN, with the parent-supported necessary intrinsic patterns{10},{4,6},{5,5}. This theorem applies to EVERY such actual distinct-ray array and ANY fixed orthonormal coordinate basis in any common sector, WITHOUT assuming all its rays are sparse. It strengthens the earlier whole-two-sparse mechanism bound into a necessary weighted density condition for genuinely mixed/dense constructions.

## 1. The exact inequality

Let a common sector have dimensiond and nd ACTUAL cells in ordern. All rays are pairwise distinct. In one fixed orthonormal sector basis, let A be the number of one-support cells (coordinate rays), M the number of genuine two-support cells, and H_k the number of cells with support sizeEXACTLYk, for3<=k<=d. Write H=sum_k H_k. Thus

    nd=A+M+H,      A<=d.

Define

    m(d,k)=floor(k/2)+2*floor((d-k)/2).

**Theorem.** Every such actual sector satisfies

    4M <= 3*sum_(k=3)^d m(d,k)*H_k.                (ESCAPE)

Equivalently

    4(nd-A) <= sum_(k=3)^d [4+3m(d,k)]*H_k.       (WEIGHTED)

This counts ACTUAL distinct high-support rays adjacent to genuine two-support rays, retaining every original row/column/transversal context. It is not a selected-support or scalar-variance relaxation asserted sufficient for a witness.

At order10 the exact original-branch consequences include:

- irreducible10 (or the whole10-space regardless of reducibility): at least13 rays have support>=3 in ANY fixed orthonormal basis;
- any4-sector: 7H_3+10H_4>=144, hence H_3+H_4>=15;
- any5-sector: 13H_3+10H_4+10H_5>=180, hence H>=14. If H=14 then H_4=H_5=0.

No assertion of sharpness or existence at the lower bound. The second statement also shows that a4-sector whose higher-support rays are all3-support requires at least21 of them. Those are necessary amplitude-independent constraints, not a finite parameter scout.

## 2. A two-support ray needs at leastFOUR distinct high-support neighbors

Take q=alpha*e_r+beta*e_s, alpha*beta!=0, and denote its unique perpendicular ray inside span(e_r,e_s) by q_perp. Maximality allows q_perp to occur in AT MOSTONE actual cell. Any pair of distinct original contexts through q's cell meets only at that cell. Thus q_perp can belong to at mostONE of q's row, column and designated-transversal bases.

Consider one of the at leastTWO other contexts. Expand the unit direction q_perp in that actual ONB. Every vector with nonzero overlap with q_perp and orthogonal to q has its two coordinates r,s proportional to q_perp, BOTH nonzero. It is not q_perp itself by the chosen context, so it has at leastONE additional nonzero coordinate. Its support is therefore>=3.

There must be at leastTWO such vectors in this context: if only one basis vector had nonzero overlap with q_perp, the basis expansion would make that vector proportional to q_perp, contradiction. Hence the context supplies at leastTWO high-support neighbors of q.

The two contexts are disjoint away from q's cell. Their at least2+2 high-support neighbors are therefore at leastFOUR DISTINCT actual cells. Additional contexts/neighbors only strengthen the count. No assumption that the high-support vectors have equal moduli, real entries, prescribed phases or a common2-dimensional sector is used.

## 3. A k-support ray has a uniform upper bound on two-support neighbors

Fix a high-support vector h, with exact coordinate support S of sizek. In ANY one ONB containing h, a genuine two-support neighbor q cannot meet S in exactlyONE coordinate: its inner product with h would have one nonzero term. Thus its support is either wholly INSIDE S or wholly OUTSIDE S.

Inside S, two such two-support neighbors cannot overlap in exactlyONE coordinate (again their mutual inner product would have one term). They cannot be two independent orthogonal rays on the SAME pair either, because both being orthogonal to h would force h's two nonzero coordinates on that pair to vanish. Therefore their coordinate pairs are disjoint, with at most floor(k/2) rays.

Outside S, the same support-pair argument partitions the used coordinates into disjoint two-coordinate blocks; each supports at mostTWO mutually orthogonal rays. At most2*floor((d-k)/2) such neighbors fit. One-support neighbors are not counted in M and cannot increase this bound.

Thus h has at most m(d,k) genuine two-support neighbors in EACH actual context. Its three contexts intersect only at h's cell, so h has at most3m(d,k) distinct two-support neighboring cells in total.

Build the actual bipartite adjacency graph between the M two-support cells and the H high-support cells, with an edge when they share an original context. Such an edge is not counted twice because two distinct cells cannot share two contexts. Section2 gives degree at least4 on the two-support side; Section3 gives degree at most3m(d,k) for a k-support vertex. Double-counting proves ESCAPE and hence WEIGHTED.

## 4. Complete order10 specializations

For d=4 the exact m values are m(4,3)=1 and m(4,4)=2. Since A<=4, WEIGHTED gives

    7H_3+10H_4>=4(40-4)=144.

Therefore H>=15. With H_4=0 one gets H_3>=21. This is a density condition inside the FULL arbitrary4-sector, not a Witting-only or coordinate-root alphabet assumption.

For d=5, m(5,3)=3 and m(5,4)=m(5,5)=2. Since A<=5,

    13H_3+10H_4+10H_5>=4(50-5)=180.

Hence H>=14. If H=14, the left side is182-3(H_4+H_5), forcing H_4=H_5=0. This retains support-size distinctions instead of freeing all high-support cells as a single weight.

For d=10, the largest m(10,k) for3<=k<=10 is8 (at k4). Therefore WEIGHTED and A<=10 give

    28H>=4(100-10)=360,
    H>=13.

These are integer products/ceilings, not decimal bounds. The theorem applies in ANY chosen orthonormal coordinate basis; choosing an ACTUAL row basis is particularly natural. In that case the ten coordinate axes occur already in that row and cannot occur again by distinctness. Moreover EVERY other cell is orthogonal to TWO distinct coordinate axes: the first-row cell in its column and the first-row cell in its designated transversal. They are distinct because a transversal cannot repeat a column. Hence every non-first-row vector has support at most8 in those coordinates. This support upper bound coexists with the lower density above and must not be confused with an all-two-sparse hypothesis.

For a PROPER sector basis extracted from that row, those two excluded full-space coordinates may lie in the OTHER sector. Thus the support<=8 full-space statement cannot be copied as an artificial small-sector zero pattern. ESCAPE itself remains valid without that extra specialization.

## 5. Exact scientific gap and assurance

The earlier whole-two-sparse cardinality bound(v19) excludes that full mechanism even when duplicate rays are allowed. Here maximality is used differently to force high-support escape and count actual neighbor multiplicities, so the theorem addresses the genuinely mixed surviving arrays. It does NOT show the new inequalities are inconsistent, that every dense partial array exists, or that dimensions4/5 are impossible. Witting's40-ray3-support model required its independent full spread obstruction(v18), not a false rank3-to-rank4 transfer.

The original remaining task stays an actual100-ray row/column/permitted-resolution ONB construction or exclusion of ALL irreducible10/proper4+6/proper5+5 branches. No numerical benchmark/current-openness/novelty or formal/kernel/human/configured-family/executable claim is promoted. All frozenbytes/earlier findings, v9 and v14 mathematical withdrawals and ZERO-credit quarantines remain permanent. Same original18/exclusive root/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence. Primary continues the actual remaining geometry rather than ending on a pending-gate park.
