# RQLS10 v23 — literal40-ray complex4-space partial-sector construction with THREE actual ten-basis partitions

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW packet: **Mon Oct 26 07:33:01 PDT 2026**. AUTHOR-WRITTEN exact finite partial construction, NOT a100-ray witness or accepted finite-witness result. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty claim. The finite-witness triple-verification skill was read: its executable independent-checker/control/delegate gates have NOT been performed, are disallowed under HOLD, and are NOT called passed. This packet does not settle the original target and is offered for complete WRITTEN review only.

## 1. The positive exact object, and what it isNOT

We give forty DISTINCT complex projective rays in C4 and THREE partitions of those SAME forty rays into ten ONBs of size4. Every two bases belonging to different partitions intersect in at mostONE ray. Assigning the first partition to rows and second to columns yields forty occupied cells of a10x10 partial array, with four distinct rays per row/column. The third partition gives ten4-cell partial row-and-column transversals.

This is the positive4-dimensional geometry required of a prospective common4-sector, not an arbitrary ansatz claimed WLOG. It also shows why the earlier Witting-model obstruction is NOT a general4-sector obstruction: the present forty-ray roster and its basis incidences are different.

The literal partial Latin-symbol table is supplied below. Completing its sixty unfilled cells to a full ten-symbol Latin resolution is a SEPARATE unsolved requirement in this packet. Supplying sixty DISTINCT C6 rays there, simultaneously giving every row/column/full designated transversal a6-dimensional ONB, is ANOTHER unsolved requirement. Neither has been silently replaced by classical labels, duplicate rays or a fictitious witness. The original maximal100-ray problem remains UNKNOWN.

## 2. Canonical rays via exact Pauli projectors

Let

    I=[[1,0],[0,1]],
    X=[[0,1],[1,0]],
    Y=[[0,-i],[i,0]],
    Z=[[1,0],[0,-1]].

A two-letter label means the tensor product, e.g. XI=X tensor I. All arithmetic here is exact over Q(i) at the projector level. The ten rows of the following table define commuting triples P_0,P_1,P_2. The signs epsilon mean P_0 P_1=epsilon P_2.

| A | P_0 | P_1 | P_2 | epsilon |
|---|-----|-----|-----|---------|
| 1 | XI | IX | XX | +1 |
| 2 | XI | XY | IY | +1 |
| 3 | YI | IX | YX | +1 |
| 4 | YI | YY | IY | +1 |
| 5 | ZZ | YY | XX | -1 |
| 6 | ZZ | XY | YX | +1 |
| 7 | YZ | ZY | XX | +1 |
| 8 | XZ | YY | ZX | +1 |
| 9 | YZ | XY | ZX | -1 |
|10 | XZ | ZY | YX | -1 |

For EACH A and EACH s,t in{+1,-1}, define the ray by its rank-one projector

    Pi(A;s,t)=(I4+s P_0)(I4+t P_1)/4.

This is the COMPLETE forty-ray roster, not an unspecified solution or numerical sample. The three Pauli eigenvalues are s,t,epsilon*s*t.

Here is a direct written verification. Distinct nonidentity Hermitian two-qubit Paulis have zero trace and are trace-orthogonal. The listed P_0 and P_1 commute, square toI4, and their product is the signed THIRD distinct Pauli in that table. Therefore Pi is a Hermitian idempotent with trace1, hence a rank-one projector. For fixed A, the four projectors are mutually orthogonal and sumI4. Different A have different triples of Pauli supports. Their expansions

    Pi=(I4+sP_0+tP_1+epsilon*s*t*P_2)/4

cannot coincide by trace-orthogonality of the sixteen Pauli matrices. Thus ALL forty projective rays are distinct. No phase convention for eigenvectors is needed.

All table commutation/product signs follow from X^2=Y^2=Z^2=I, XY=iZ,YZ=iX,ZX=iY and reversed products' minus signs. These were reasoned in writing, NOT machine-checked.

## 3. ALL thirty hybrid ONBs, and their three ten-basis partitions

For a Pauli P in the table, list the A containing it in the following directed cycle. For EACH arrow A->B in the cycle define the4-ray basis

    H(P;A->B) = {Pi(A;s,t): eigenvalue(P)=+1}
                 UNION {Pi(B;s,t): eigenvalue(P)=-1}.

Each brace contains exactlyTWO of the explicitly defined projectors. The first pair is an ONB of P's positive2-eigenspace; the second is an ONB of its negative2-eigenspace. Their union is therefore an exact C4 ONB.

| partition | Pauli P | complete directed cycle | number of bases |
|-----------|---------|-------------------------|-----------------|
| rows | XI | 1->2->1 | 2 |
| rows | YI | 3->4->3 | 2 |
| rows | ZZ | 5->6->5 | 2 |
| rows | XZ | 8->10->8 | 2 |
| rows | YZ | 7->9->7 | 2 |
| columns | IX | 1->3->1 | 2 |
| columns | XY | 2->6->9->2 | 3 |
| columns | YY | 4->5->8->4 | 3 |
| columns | ZY | 7->10->7 | 2 |
| transversals | IY | 2->4->2 | 2 |
| transversals | XX | 1->5->7->1 | 3 |
| transversals | YX | 3->6->10->3 | 3 |
| transversals | ZX | 8->9->8 | 2 |

The bases in each partition are numbered1..10 by reading that partition's table rows top-to-bottom and arrows left-to-right. Thus, for example, row1=H(XI;1->2), row2=H(XI;2->1), column3=H(XY;2->6), transversal9=H(ZX;8->9). This convention fixes all later cell labels literally.

**Entire partition proof.** Each A contains EXACTLYONE Pauli from each table partition (the three columns P_0,P_1,P_2). A ray from A appears in exactlyONE hybrid basis for each of these Paulis: for positive eigenvalue, use the outgoing arrow at A; for negative eigenvalue, use the incoming arrow. It appears nowhere else because its unique A is fixed. Therefore each table partition covers EACH of the forty rays EXACTLYONCE, in ten exact ONBs.

**Entire intersection proof.** For the SAME P, different arrows use different positive/negative pairs. Even when their node sets overlap, the shared A supplies opposite-sign disjoint ray pairs. Such bases have no ray in common. For DIFFERENT P,Q, two hybrid bases can share at mostONE node A: two distinct commuting triples in our literal table cannot both contain two different Paulis P,Q, because their third Pauli is then forced by the product. If they share one node A, simultaneous prescribed P and Q eigenvalues select exactlyONE of its four rays. Different A never share a ray. Thus ANY TWO DISTINCT hybrid bases intersect in at mostONE ray. This proves the cross-partition condition as well as same-partition disjointness without a classification of all stabilizer bases.

## 4. Literal partial10x10 ray/Latin-symbol table

For each A, the following four cell-symbol entries are in the order(s,t)=(+,+),(+,-),(-,+),(-,-). The ray in that entry is exactly Pi(A;s,t), not merely the displayed transversal symbol.

| A | (+,+) | (+,-) | (-,+) | (-,-) |
|---|-------|-------|-------|-------|
| 1 | (1,1):3 | (1,2):5 | (2,1):5 | (2,2):3 |
| 2 | (2,3):1 | (2,5):2 | (1,3):2 | (1,5):1 |
| 3 | (3,2):6 | (3,1):8 | (4,2):8 | (4,1):6 |
| 4 | (4,6):2 | (4,8):1 | (3,6):1 | (3,8):2 |
| 5 | (5,7):3 | (5,6):4 | (6,7):4 | (6,6):3 |
| 6 | (6,4):7 | (6,3):6 | (5,4):6 | (5,3):7 |
| 7 | (9,9):5 | (9,10):4 | (10,9):4 | (10,10):5 |
| 8 | (7,8):9 | (7,7):10 | (8,8):10 | (8,7):9 |
| 9 | (10,5):9 | (10,4):10 | (9,5):10 | (9,4):9 |
|10 | (8,10):7 | (8,9):8 | (7,10):8 | (7,9):7 |

This table is obtained directly from the preceding literal incoming/outgoing rules and the epsilon sign table. Those algebraic rules are the primary definition; the displayed expansion is included so a reviewer can check EVERY cell and any transcription defect independently. None has been computationally checked.

Each row and column has FOUR occupied cells with four orthogonal projectors. Every symbol occurs FOUR times, at different rows and columns, and those four rays are its exact hybrid ONB. The no-double-cell/no-repeat-symbol facts are consequences of the full intersection proof, not counts asserted instead of incidence verification.

The ten A blocks are2x2 intercalates in this partial Latin table. This is NOT a claim that every such partial Latin square completes. No cyclic i-j resolution or other selected resolution was assumed WLOG.

## 5. A tempting4+6 exterior-power continuation FAILS maximality

One natural attempt is to take, for each row's4-space basis B, its six wedge products as the basis of Lambda^2(C4), dimension6. This does NOT produce the remaining sixty DISTINCT rays here.

Indeed row1 and row2 are H(XI;1->2) and H(XI;2->1). Their positive-XI pairs are two different ONBs of the SAME2-space E_+(XI), and their negative-XI pairs likewise span E_-(XI). The wedge of the two positive-pair vectors is the unique projective line Lambda^2 E_+(XI), independent of the chosen ONB; the negative-pair wedge similarly repeats Lambda^2 E_-(XI). Thus the two proposed6-sector ROW bases already share TWO projective rays. Distinct rows need distinct actual cells, so maximal100-ray cardinality is impossible for this direct exterior-square continuation.

This is an exact rejection of THAT natural continuation only. Row-dependent new unitaries could change this premise but would require solving all column/transversal conditions again; they are neither dismissed WLOG nor declared a fix. No arbitrary6-sector impossibility is inferred.

## 6. Full residual and review contract

The positive partial geometry in sections2–4 is complete at its stated scope: a literal forty-ray C4 roster, thirty exact ONBs, three partitions, cross-basis intersection<=1 and the expanded40-entry partial Latin table. It needs an ENTIRE mathematical review of the projector/sign/cycle/partition/intersection/cell claims and an ENTIRE application review preserving the following open requirements:

1. Complete the actual40 prescribed symbols to a full order10 Latin resolution, or prove the partial pattern cannot complete and replace it rather than declaring a witness.
2. On the sixty empty cells, construct sixty DISTINCT C6 rays, orthonormal in each six-cell row/column/completed-transversal sector context, with the SAME full resolution.
3. Parent acceptance under its written-wave protocol; no executable finite-witness gate has occurred. Any later100-ray candidate needs its own full definition-first independent verification and priority screen, which this packet does not anticipate as passed.

No prior-art classification, unprovided table of all60 stabilizer rays, or algorithmic catalogue is an operative premise. The background Pauli-label idea motivated a new literal derivation; only the finite tables printed here and ordinary exact tensor-product linear algebra are used. No novelty claim is made.

This is a NEW positive representation, not a repair inserted into frozen v18, a rank4-WLOG assumption, or a fake100-ray deliverable. All original intrinsic branches remain OPEN; the irreducible10 and5+5 branches remain available. The complete earlier density candidates v20–v22 remain separately unreviewed and were NOT used as a substitute for verifying this construction. All process/math findings and ZERO-credit quarantines, including v9/v14 withdrawals, persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 remain binding. Primary continues the exact remaining completion/construction problem without an early pending-review park.
