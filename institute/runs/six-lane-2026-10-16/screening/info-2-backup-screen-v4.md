# info-2 backup-target screen v4 — parent disposition (2026-10-17 PT)

Read-only scout `InfoTargetScreen4` (first report then a blocker follow-up; transcript `history://InfoTargetScreen4`). Nothing was frozen; CFR(5,27) remains the active info-2 target.

## Candidates

1. **CGMN conjecture, q = 18** (a Latin square L of order 18 with M(x,y) = L(y, L(x,y)) also Latin; equivalently a full 2-recursive [4,2,3]₁₈ MDS code). Klimov arXiv:2604.01105v2 §6 names q = 14 and 18 as the remaining cases. **q = 14 is already claimed** (Nithil R., Zenodo doi:10.5281/zenodo.21499738, registered 2026-07-22T21:32:06Z, with a Lean certificate), which also publicly names 18 as the sole remaining case.
   - Scout-proved bridge (unreviewed): any design whose blocks are cyclic orders of size ≥ 4 with every ordered pair 1-, 2- and 3-apart exactly once yields an idempotent recursively differentiable quasigroup; size ≥ 4 is necessary.
   - **DERIVABILITY-UNRESOLVED:** Bennett–Zwicker–Chang (Discrete Math. 309, 2009), Bennett–Xu (2009) and Xiang–Xu–Bennett (2010) could contain a 3-fold perfect mixed-block design of order 18 that would imply q = 18 through that bridge; their theorem statements were unreadable by legitimate routes. An (18,k,1)-PMD with k ∈ {6, 9, 17} would also imply it; (18,6,1) is listed open, (18,9,1) and (18,17,1) have unknown status (a Z₁₈-cyclic (18,17,1) design is impossible by a sum-of-differences argument).
   - Cleared: Sage has no Mendelsohn objects (its MOLS(18)/OA(7,18) are not equivalent; an optional cheap conjugate test is not run), Hsu–Zhou does not apply, Z₁₈-affine constructions and regular-group (complete-mapping) constructions fail.
   - **Disposition: do not freeze.** Freezing requires reading the unread theorem statements or obtaining equivalent primary evidence; high scoop risk.
2. **Perfect Mendelsohn designs (9,6,1), (10,6,1), (12,6,1)** from CPro1 `OPEN_INSTANCES` (main@827f02b). For (9,6,1) the underlying 6-sets are forced to be the complements of the 12 lines of AG(2,3) (proof modulo STS(9) uniqueness), leaving a small exact cover. Staleness unresolved: Zhu 1989, Miao–Zhu 1995, Abel–Bennett–Zhang 2000 and Handbook Table 35.29 were not read; the table may already record (9,6,1) as nonexistent. Low significance, comparable to the accepted BTD decisions.

## Disposition

No backup freeze now. If CFR(5,27) reaches a concrete obstruction, the next step is a targeted read of the PMD primary tables (or the three Bennett-group papers) before any freeze; an equivalence/staleness hit would kill the candidate exactly as in CFR(4,33).
