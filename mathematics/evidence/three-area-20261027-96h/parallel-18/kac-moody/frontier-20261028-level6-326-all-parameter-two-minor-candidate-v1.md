# Level-six types (3,2,6) and (2,3,6): injective for EVERY r,s>=6 — a two-minor resultant candidate

**MathKacMoody-2 / math-3.** Native `/bin/date` observed immediately before this additive write: **Wed Oct 28 21:10:32 PDT 2026** (precreation observation). New exact-computation-assisted written argument, **UNREVIEWED**: not parent adoption, formal/kernel, human, independent-model, priority or novelty acceptance.

## 1. Exact claim

For every pair of integers `r,s>=6`, every allowed FULL complex Cartan realization C of A(r,s), the original Serre quotient `S=G_C/J`, and `P_(3,2,6)=ker f1 ∩ ker f2`, at the same named UNREVIEWED full-Cartan/free-Levi/PBW source-identification inputs used for the level-six (2,2,6) candidates (they identify `P_(3,2,6)` with the 54-dimensional free-Levi joint horizontal kernel and the actual target `S_(3,2,5)` with the 400 affine target rows of the pencil):

> **Candidate theorem.** The ENTIRE original map `D3: P_(3,2,6) -> S_(3,2,5)` is injective for all integers `r,s>=6`. By the node exchange `A(r,s)<->A(s,r)` (simultaneously exchanging nodes 1,2 and the first two degree coordinates) the same holds for `P_(2,3,6)`.

Effective and complete on the quadrant for these two primitive types; no Faltings/Siegel/HIT import, no density or residue restriction. Not claimed: the other five level-six types ((3,3),(4,3)/(3,4),(4,4),(5,5),(6,6)), the regime `min(r,s)<=5`, F6/B6, arbitrary-GCM/all-level Serre, a non-Serre witness, novelty or priority.

## 2. Argument

Put `x=r-6,y=s-6`; every matrix entry is affine in x,y (the pencil `frontier-20261028-level6-free-32-pencil-v1.json`, built from the actual lowering at (6,6),(7,6),(6,7)). Two actual maximal 54×54 minors were computed exactly by total-degree interpolation and factored:

- `P1` (baseline selected rows) `= -(2097152/81)(y+4)(y+5)^8(x+4)(x+5)^6 F5 G33`;
- `P2` (slot 0 replaced by target word `01412`) `= (4194304/81)(y+4)(y+5)^8(x+4)^2(x+5)^6 F5 K32`.

Here F5 (total degree 5, 21 terms) has **all coefficients positive**, as do the linear factors, so they are strictly positive on the closed quadrant `x,y>=0`. G33 (degree 33, 594 terms) and K32 (degree 32, 560 terms) are the only factors that can vanish there; both have constant leading coefficient in x (degrees 33 and 32 in x).

Let `H(y)=Res_x(G33,K32)`. Constant x-leading coefficients make `H(y0)=Res(G33(·,y0),K32(·,y0))` exact for every y0, so `H(y0)!=0` means no common complex root on the fibre. Exactly, `deg H=1055` (bound 1056); its repeated part has degree 158 and consists only of the linear factors
`(2y+23)^2(2y+11)^4(2y+15)^4(y+4)^10(y+5)^10(y+6)^19(5y+28)^36(14y+69)^81`
(multiplicities in H). The squarefree part (degree 897) is certified by Cauchy bound + Hensel uniqueness at p=1019 (21 simple roots mod p; every symmetric lift outside the bound unless an exact root) to have integer roots exactly `-7,-6,-5,-4,-3`. Hence H has **no integer root y0>=0**; for every integer point of the quadrant, G33 or K32 is nonzero; so P1 or P2 is nonzero; the full 400×54 matrix has rank 54; and D3 is injective on `P_(3,2,6)`. This proves the candidate theorem at the stated inputs.

## 3. Exact evidence

- General producer `frontier-20261028-level6-two-minor-general.py`, 270LF SHA `c22754a615becd06aed9aec9ab286a68069db1c977ecec265de4c487878821c6` (run `--a 3 --b 2 --slot 0 --word 01412`): full rows, both interpolated minors, exact factorization with product check, positivity labels, exact resultant from 1065 exact univariate resultants with interpolation on 1057 points and 8 extra checks, gcd/squarefree decomposition, Hensel/Cauchy integer roots, fibre and rank fallbacks (none needed). Output `frontier-20261028-level6-326-two-minor-certificate-v1.json`, 7428LF SHA `c91b2f973180211296a0c92af8e1b3d6977e923af6b6190e634622b304533180`, status `ALL_INTEGER_QUADRANT_POINTS_FULL_RANK` at **Wed Oct 28 21:07:57 PDT 2026**. The pencil SHA recorded inside is that of the pinned input file.
- Separately authored general replay `frontier-20261028-level6-two-minor-general-replay.py`, 268LF SHA `78340a98b974ef2104a6118f3acc96e1028cc588e439530cc93ff05a606764e5`, imports no producer code: rebuilds all 400 target rows with the separate tree-Jacobi engine; rebuilds both minors from the claimed factorizations by own rational convolution and matches them at 1540 own fraction-free determinants each on a SHIFTED unisolvent grid; rechecks positivity labels; matches H modulo two 60-bit primes at 1056 points each (2112 own Sylvester eliminations) and by 3 exact integer Sylvester determinants; divides out the linear factors; re-derives the integer roots at the different Hensel prime 5003. Output `frontier-20261028-level6-326-two-minor-independent-replay-v1.json`, SHA `790403ca661e1eb5802607cde3e36bcfe4f2c450af7d0ca44690ea0a05d9550a`, `PASS_INDEPENDENT_GENERAL_TWO_MINOR_REPLAY` at **Wed Oct 28 21:10:04 PDT 2026**.

Same owner, shared pencil data; exact computation, not independent-model, human or formal verification.

## 4. Gates

Full scientific review of the source-identification inputs, the two-minor reduction, the resultant specialization and the Hensel argument, plus a source/code audit of both programs and the pinned pencil, are required before adoption. All earlier ZERO/STOP/HOLD/process findings, the incidental older cone-status exposure and the pending F5 audit are unchanged; no held guide is a premise.

**END — (3,2,6)/(2,3,6) all-parameter candidate at named source inputs; independent review pending.**
