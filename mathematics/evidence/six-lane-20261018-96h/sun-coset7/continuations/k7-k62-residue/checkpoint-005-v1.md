# Checkpoint 005 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T05:04:43-0700. Previous: checkpoint-004 at 2026-10-19T03:50:52-0700.
- No computation run; no process running; no old/sibling artifact edited. Deviation recorded: the Z23-P5 erratum
  header clock (03:51:55) preceded its exclusive create (03:52:17) by 22 s (two eval cells); parent noted it.

## Since 004 (actual results)
- `K7-Z23-P5-erratum-v1.md` sha256 737e82a331929432422f6a9dec535e7af8a5f697c86ae78870af7d7296ec823d frozen and sent; parent
  verdict `RUN/review/sun7-Z23P5-parent-verdict-v1.md` sha256 7179e5645df3b840a1e4a9735e554ae7be4114d2e34f2b418face51e017c6f8d: Z23-P5 ACCEPTED.
  Accepted K7 frontier now: 2- and 3-markers on DIFFERENT vertices only (5 absent/on z/on t = (a1); 5 on third p = (a2)),
  with D23 restrictions.
- Written derivations (NOT yet frozen as claims; to go into one candidate file):
  1. FG-K7 at an unmarked u in (a1): order z, t, then unmarked; each step gcd(n_e,T_m) | 6, k <= 5; so LFC and VFC at u
     hold with val <= 5 (units 1/6) in both orientations. (a2) needs one base pair with a compatible beta.
  2. Quantitative transfer: at apex z (g_z=1), mu(D_t cap X_u)/mu(D_t) = fraction of t-fibres at apex u meeting z.
     Hence D_t cap D_u = empty iff every t-fibre at u meets z.
  3. Rows at u (FG): no W-W five and alpha_ut != 5 (both orientations); every row with a W-three has c=alpha_uz=3, e=2,
     W-part (3333),(3331),(3311),(3322), all FG-tight with L_t subset L_z; rows with c in {1,2} have no W-three.
  4. Triangles {z,u,v}: u in T, v not in T force alpha_uv in {3,4}; hence T != W implies W3 = empty and
     alpha_uv = 4 on all T x (W \ T). Both T != W and T* != W together are impossible (INV + connectivity), so
     T = W or T* = W.
  5. In T = T* = W, the centre count at z gives sum_u phi_u < 5 (phi_u = fraction of t-fibres at u meeting z), and
     sum_u phi_u >= 3 always; the obstruction P has all phi_u = 1 and dies.
- **Blocker / next bounded action:** k3=0 rows (W-part in {1,2,4}) survive FG in many shapes, some with t isolated
  (phi_u = 0), so the centre count alone does not close (a1). Next: finish the written census of k3=0 rows with
  tightness data and attempt the global (T=W or T*=W) closure; otherwise freeze an exact residual pattern list.
