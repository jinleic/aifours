# RQLS10 v22 — full-support escape strengthens the ACTUAL4-sector density to23

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing: **Mon Oct 26 07:22:49 PDT 2026**. NEW AUTHOR-WRITTEN CANDIDATE, not parent-adopted. Exact orthogonality/support/actual-incidence/integer proof only. No interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private approximate scout/backconversion, no formal/kernel/configured-family/human/novelty/witness promotion.

## 1. Exact strengthened theorem

Take any ACTUAL common4-sector of a maximal1-RQLS10 and choose the4 sector rays of any ACTUAL row as coordinate axes. Exactly those4 actual cells are coordinate rays. Write M for genuine two-support cells, H_3 for exact three-support cells, H_4 for full-support cells. Thus

    M+H_3+H_4=36.

There are8 distinct column/transversal contexts containing one of the4 chosen axes. Let c be the number of those8 whose OTHER3 sector vectors ALL have support3. Then0<=c<=8.

**Theorem.** Every such actual sector satisfies the JOINT conditions

    H_3>=16+c,
    4H_3+10H_4>=128+2c,
    10(H_3+H_4)>=224+8c.                         (DENSITY4)

In particular AT LEAST23 actual rays in the4-sector have support>=3, in any actual-row sector basis. With the v20/v21 complete6-sector density bound>=14, an intrinsic4+6 array therefore needs at least37 high-support rays in ANY actual full-row basis. This strengthens, not withdraws, the earlier necessary bounds20 and34. The dense remaining branch is NOT excluded.

The theorem also gives a rigid limit when H_4=0:

- M=0,H_3=36,c=8; OR
- M=4,H_3=32,c=0, and the four two-support cells form ONE other all-two-support sector ROW, made of two perpendicular ray pairs on disjoint coordinate pairs. Each such cell has its column and designated-transversal axes in the complementary coordinate pair, and these are its TWO distinct missing axes.

This is a necessary dichotomy for the arbitrary complex three-or-less-support4-sector. It does NOT identify it with the particular finite Witting40-ray set, does not assume equal amplitudes/cube-root phases, and does not exclude either alternative.

## 2. The exact8 axis-context count

Each of the chosen4 axes has its column and designated-transversal context. They are8 distinct actual contexts. Each contains exactlyONE coordinate ray (the axis), since all4 coordinate rays already occur once in the chosen row and any two contexts meet at most once.

The other3 rays form an ONB of a3-dimensional coordinate complement containing NO coordinate rays. At mostONE of these3 can be genuine two-support: two orthogonal two-support vectors either have disjoint support pairs (impossible in3 coordinates), or are a perpendicular pair on the same support; their third basis vector would then be the remaining forbidden coordinate axis. Therefore each axis context has exactly one of the two patterns

    (one2-support,two3-support),
    (zero2-support,three3-support).

No4-support ray can be orthogonal to an axis. Thus the total number S of two-support incidences with these8 contexts and the total three-support incidence count T are

    S=8-c,             T=16+c.

A3-support vector is orthogonal to exactlyONE coordinate axis, and cannot share BOTH that axis's column and transversal (two cells would then be in two contexts). Hence each3-support cell contributes at mostONE of those incidences, giving H_3>=T=16+c. This proves the first inequality without a genericity assumption.

## 3. Missing a sparse partner in a NO-AXIS context costs at leastTWO FULL-support rays

**Lemma.** Let a4-dimensional ONB contain no coordinate ray, contain q=alpha*e_1+beta*e_2 with alpha*beta!=0, and NOT contain its perpendicular ray q_perp in span(e_1,e_2). Then at leastTWO of the other3 basis rays have support4.

Every vector orthogonal to q lies in the3-space

    span(q_perp,e_3,e_4).

An additional two-support ray can only be supported on {3,4}: it cannot meet {1,2} in exactlyONE coordinate, and a ray on {1,2} would be the prohibited q_perp. There is at mostONE such additional ray: two orthogonal ones would span {3,4} and force the remaining basis ray to be q_perp. If there is one, say r on {3,4}, it has both coefficients nonzero (no coordinate rays). The remaining two basis rays lie in span(q_perp,r_perp); neither can be a pure component (both prohibited sparse partners would then occur), so both mix the two disjoint two-support components and have support4.

If there is no additional two-support ray, all3 remaining rays have support>=3. A support3 one must mix q_perp with exactlyONE of e_3,e_4. Two support3 rays using DIFFERENT outside coordinates cannot be orthogonal because their q_perp components have a nonzero inner product with no other shared component. Two using the SAME outside coordinate, if orthogonal, span that2-space, forcing the third ray to be the other forbidden coordinate axis. Hence at mostONE of the3 can have support3; at leastTWO have support4. This proves the lemma in both exhaustive cases.

Notice the NO-AXIS qualification: in an axis context the corresponding missing-partner pair consists of3-support rays, not4-support ones. Confusing these is exactly the gap avoided by retaining S.

## 4. Double-count only FULL-support escape edges

For a two-support actual cell q let s(q) be the number of its contexts among the8 axis-bearing contexts. Then0<=s(q)<=2 and sum_q s(q)=S. Its sparse perpendicular q_perp can occur in AT MOSTONE of its3 contexts: it is one distinct projective ray, hence at most one actual cell; two distinct contexts cannot contain both q and q_perp.

Every axis-bearing context containing q automatically lacks q_perp. Otherwise its other remaining ray would be the second coordinate axis outside q's pair, forbidden by global distinctness. Therefore at least2-s(q) of q's NO-AXIS contexts lack q_perp. By the lemma, each supplies at leastTWO4-support neighbors. Distinct contexts through q supply distinct other cells. Thus q has at least4-2s(q) DISTINCT full-support neighbors.

Conversely, any4-support cell has at mostTWO orthogonal two-support neighbors in each context. Their support pairs must be disjoint; two orthogonal rays on one pair would force that4-support vector's coordinates on the pair to vanish. Consequently its total degree toward two-support cells is at most6 over the3 original contexts. Distinct cells never share two contexts, so this degree count has no multiplicity artifact.

Double-counting the actual two-support/full-support adjacency graph gives

    4M-2S<=6H_4.

Insert M=36-H_3-H_4 and S=8-c:

    144-4H_3-4H_4-16+2c<=6H_4,
    128+2c<=4H_3+10H_4.

Finally

    10(H_3+H_4)>=128+2c+6H_3>=224+8c.

Since H_3+H_4 is integral and224>220, it is at least23. No numerical solver or rounded estimate enters the theorem.

## 5. Entire no-full-support dichotomy, not a Witting-WLOG statement

Suppose H_4=0. The lemma shows that EVERY context containing a two-support q but lacking q_perp must be an AXIS context. Since q has at leastTWO partner-missing contexts and at mostTWO axis contexts, it has EXACTLYTWO axis contexts, both lacking q_perp. The third, its ROW (not the chosen axis row), must contain q_perp.

Consider that actual ROW's4-sector basis, containing q and q_perp. The remaining2 rays lie on the complementary coordinate pair. Because there are no coordinate rays, both have genuine two-support and are perpendicular. Thus any row containing a two-support cell consists of FOUR two-support cells. Therefore M is a multiple of4.

Every such q contributes exactlyTWO axis-context incidences, so

    2M=S=8-c<=8.

Hence M is0 or4. If M=0, S=0,c=8 and H_3=36. If M=4, S=8,c=0,H_3=32; all4 two-support cells lie in one all-two-support row. Each has exactlyTWO missing coordinate axes (the complement of its support pair) and BOTH must be its actual column/transversal axes. These two axes are distinct because two actual contexts cannot share both cells.

No phase/root classification was used. This dichotomy is a NEW representation of the surviving three-support geometry: either36 genuinely3-support rays plus the4 chosen axes, or32 such rays plus one forced4-cell sparse row. It is not a finite orbit classification, no-candidate assertion, or identification with the Witting model whose independent obstruction was v18.

## 6. Import boundary, application and remaining gap

The actual common-sector trace count40/context ONBs and distinctness are the parent-supported v15/v16 model facts. Sections2–5 completely prove the new4-sector assertions, including axial incidence, refined sparse complement and no-full-support dichotomy. The whole-array37 density statement additionally imports the AUTHOR-WRITTEN complete6-sector v20/v21 weighted inequality; it needs a full union gate, not just a check of23. No arbitrary qutrit no-go is imported into rank4.

The original maximal100-ray problem is still UNKNOWN in all3 intrinsic branches{10},{4,6},{5,5}. Neither inequality nor the three-support dichotomy is known inconsistent. Irreducible10 and arbitrary proper5+5 are unaffected beyond their earlier density constraints. This theorem is progress on the actual mixed4-sector geometry, not another finite ansatz declared WLOG. Original18-owner/exclusive-root/HOLD/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/30min substantive actual-clock cadence remains binding. All prior process/math findings, including v9 and v14 withdrawals and all ZERO-credit arithmetic quarantines, remain permanent; nothing is backdated or repaired inside pinned sources.
