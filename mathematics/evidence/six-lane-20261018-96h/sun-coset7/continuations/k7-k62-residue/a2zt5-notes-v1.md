# (a2-zt5) working notes v1 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:42:48-0700. Unchecked scratch; no computation.

## Available tools in (a2-zt5) (orientation alpha carries alpha_zt = 5; W := W' cup {p})
- FG (Corollary 5/6-a2) for alpha-rows at every u in W; for alpha*-rows only at W' and only if alpha_tp = 1 (the factor
  5 of [G : U_z cap U_t] makes FG for alpha*-rows at p genuinely unavailable).
- FG-V in C^alpha* (masses = alpha-rows) at every W-apex; in C^alpha only V4 (so K3 needs mass sum >= 6/6).
- Lemma EQ, SUB, IN, CELL (K7-CELL) need only FG-V at the EQ apex (C^alpha*), LFC and Sun(3).

## Structure (sketch)
- RICH-type step: R3 for alpha-rows (FG ok, c = 3, no fives) + TR + CC at z in C^alpha (V4 only; alpha*_zt = 1) give
  W3 = empty for alpha (Corollary W3 argument with ell_p = 5^B w_p). So alpha on W lies in {1,2,4}; alpha-rows are
  Case-A rows; Lemma B holds for them.
- TZ (i) for alpha* (no FG needed): u in T*, v in O* := W \ T* give alpha*_uv in {3,4}, so alpha_uv in {1,2}.
  Lemma B at v in O* (>= 3 entries <= 2): single alpha-four inside O* and alpha_vt = 4. Hence O* is empty or
  O* = {v1, v2} with alpha_v1v2 = 4, |T*| = 3; triangles {v1, v2, a} force alpha_va = 2: v-rows are R3.
- (zt5-A) T* = W; (zt5-B) |T*| = 3, O* = {v1, v2}.
- (zt5-B): EQ at v1 in C^alpha* (masses v2 4, t 4, a's 2, z 3) gives D*_v2 = D*_t; SUB needs alpha*_v1v2 = 2 and
  alpha*_tv2 = 2 (both <= 2 by INV) to produce K = U*_v1U*_v2 = U*_v2U*_t of index 3.
- Missing for a CELL kill: a second index-3 subgroup (from an apex a in T* whose alpha-row has W cup t-part 4,4,2,2,2 and
  alpha* = 2 on the relevant pairs) and the alpha*-side data, which lacks FG.
