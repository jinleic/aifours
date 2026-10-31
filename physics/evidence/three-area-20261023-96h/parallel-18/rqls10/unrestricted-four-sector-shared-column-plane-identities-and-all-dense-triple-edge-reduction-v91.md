# RQLS10 v91 — Shared-column plane identities; in the all-dense case a triple column forces ONE graph and pins four cell placements

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 19:33:51 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written projection-sum/graph/counting arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Lemma SC: sum identities for vertices sharing columns

At EVERY vertex u of the v76 graph the four incident column planes sum to 2I, because the two row ONBs each sum to I. Across every column e={u,y}, P_(y,e) = I - P_(u,e). Let u,y share exactly k columns.

* k=3: if u's fourth plane is B_u and y's fourth plane is B_y, then B_y = I - B_u. Indeed B_y = 2I - sum over the three shared columns of (I - P_(u,e)) = -I + (2I - B_u).
* k=2: the two non-shared planes at u and the two at y together sum to 2I.

These identities hold for sparse and dense vertices alike and use only v76 column complements.

## 2. Theorem T5: the all-dense case with a triple column

Let d=5, so every vertex is dense. G is a connected loopless 4-regular multigraph on five vertices; a quadruple column would disconnect two vertices, so multiplicities are at most three. Suppose V and Y share a triple column. Let V's fourth column go to W and Y's fourth column go to Z.

(a) W=Z is IMPOSSIBLE. By SC, B_Y = I - B_V. At W the column V-W has plane I-B_V and the column Y-W has plane I-B_Y = B_V. These two incident planes at dense W are complementary, contradicting v77's strict dense traces.

(b) Hence W is not Z. The degree count on the remaining vertices W,Z,X then forces

    G = { V=Y triple, V-W, Y-Z, W-Z, W=X double, Z=X double }.

Indeed W,Z need three more column ends each and X needs four, and the integer solution is unique. In this G:

    P_(W,VW) = I - B_V = B_Y = P_(Y,YZ),     P_(Z,YZ) = I - B_Y = B_V = P_(V,VW).

So two column planes at DIFFERENT dense vertices coincide twice.

(c) PINNED PLACEMENTS (full resolution). By v87 Theorem DX, a cell at one vertex lying in a column plane of another dense vertex is non-orthogonal to ALL cells there. Each dense vertex is missed by exactly two classes. Therefore:

* the two W-cells of column V-W lie in the two Y-missing classes;
* the two Y-cells of column Y-Z lie in the two W-missing classes;
* the two Z-cells of column Y-Z lie in the two V-missing classes;
* the two V-cells of column V-W lie in the two Z-missing classes.

The two cells of one column at one vertex share a column, so they lie in distinct classes; this makes each placement a bijection.

(d) A trace constraint follows. In a Y-missing class T containing the W-cell w of column V-W, T's V-cell lies in some triple column with plane A_e, since column V-W is w's. T's Z-cell cannot lie in column Y-Z, whose plane is B_V, because DX at V would forbid it next to T's V-cell. The trace identity at V (v88) for the plane B_V then gives

    <z,B_V z> + <x,B_V x> = 2 - lambda^V_(e,4),

for T's Z-cell z and X-cell x. Since z lies in a Z-column plane f other than Y-Z, <z,B_V z> = lambda^Z_(f,YZ) by Lemma TD at Z, using B_V = P_(Z,YZ). Hence

    lambda^V_(e,4) + lambda^Z_(f,YZ) >= 1.

This is one exact necessary inequality per Y-missing class; symmetric inequalities hold for the W-, V- and Z-missing classes.

(e) Chirality locks (v90 L3): Pi^Y = I - Pi^V. The double columns W=X and Z=X force each of (Pi^W,Pi^X) and (Pi^Z,Pi^X) to be equal-up-to-complement or interior-isoclinic (v89).

## 3. Scope and frontier

New paid results: Lemma SC; the impossibility of an all-dense array whose triple column endpoints share their fourth neighbour; the unique graph and double plane coincidence otherwise; four pinned placements; and the per-class inequality. d=5 without triple columns (including K5 and graphs with only double columns), the remaining case-(b) gluing, d in {2,3,4}, all-sparse residuals, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain OPEN. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v76 graph/column complements, v77 DENSE strict traces, v85 D1, v87 DX, v88 Lemma TD and trace identity, v89/v90 chirality theorems, and the actual primary TEN-transversal/CLASSICAL-mate interface for (c)-(d). No NR/classifier/Butson/Gaussian/code premise, chosen frame or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S91, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor, the v30 dangling-reference defect and the v34 capture retry. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
