# Checkpoint 008 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T05:32:41-0700. Previous: checkpoint-007 at 2026-10-19T05:20:39-0700.
- No computation run; no process running; no old/sibling artifact edited.

## Frozen and sent since 007
- `K7-D23-RICH-erratum-v1.md` sha256 8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69 (05:26): NO5 (a) last branch
  replaced by the parent's local inverse-row argument; the direct Sun(6) instance is withdrawn.
- `K7-D23P-v1.md` sha256 89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880 (05:28): in (a2) (z, t, p distinct)
  neither z-row is 4-type (ROW-2 transferred to apex z; (a') killed by the inverse row; mixed (b')/(c') killed by
  M1/M2 with Q = {o,p} or {o1,o2}).

## New written facts (NOT yet frozen; next candidate file)
1. **(a1): W3 = W3* = empty.** If alpha_uv = 3 (u,v in W), every third w has alpha_uw = 3 or alpha_vw = 3: the only
   one-three W-triangle surviving T is (3,4,4), and rows with a W-three have no W-four (RICH R3). So W3 nonempty
   implies W3 = W, hence T* subset W3, excluded by RICH. Same for alpha*. (The '|W3| in {0,3}' note of 007 is wrong
   and withdrawn.)
2. Hence all W-W entries lie in {1,2,4} in both orientations; W-triangles avoid (1,1,2), (1,1,4), (1,2,4).
3. **Case B (T = W, T* != W) structure:** |T*| = 3, W \ T* = {v1,v2}, alpha_v1v2 = 4, alpha_vt = 4, E >= 2,
   alpha = 2 on T* x {v1,v2}, every a in T* has an alpha-four inside T*, e_a := alpha_ta in {2,4}; PFG at t (chain
   along the alpha-<=2 graph, connected here) forces >= 2 a with alpha*_ta = 4, then alpha = 4 on all of T*.
   Not yet a contradiction (PFG rigidity leaves {4,4,2,2,2} / {4,4,4,*,*} with z 4-type).
4. Case A (T = T* = W): F7 at z gives alpha_ab = 1 => X_a = X_b; pair-sum bound 2 <= sum mu(X_a cap X_b) <= 5/2;
   centre count gives sum_u phi_u < 2 + 3/alpha*_zt and >= 3 (phi_u = t-fibre fraction meeting z at u).

## Blocker / next bounded action
Case A and Case B of the (a1) residue are not closed. Next: finish Case B via rigidity at the T*-vertices (their
alpha-rows (2,2,4,4) with e = 2 are tight with forced y_z = 0, fixing fibre types) and t-triangles; then Case A.
Next checkpoint by 06:20 PDT.
