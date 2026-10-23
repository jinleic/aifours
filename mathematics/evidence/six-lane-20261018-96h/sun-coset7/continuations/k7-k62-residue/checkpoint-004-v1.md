# Checkpoint 004 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T03:50:52-0700. Previous: checkpoint-003 at 2026-10-19T03:23:47-0700.
- No computation run; no process running; no old/sibling artifact edited.

## Since 003
- D23 reviews read in full (Codex 8be1767f..., Claude 86f89f3c...). Mandatory erratum frozen and sent:
  `K7-D23-NO4-erratum-v1.md` sha256 594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a.
- Parent: D23 ACCEPTED (`RUN/review/sun7-D23-parent-verdict-v1.md` sha256 d3453de10eafab4d4666eb1902e18a13140beb4aee511df3c35febf21e4f37db).
  Z23-P5: Codex ACCEPT 0/0/0, Claude running (parent-owned). Sibling K63-RES (FG lemma) read read-only; used only as an
  unaccepted CANDIDATE idea.

## Working notes (NOT claims) on the different-vertex residue (a1): 5 absent/on z/on t
1. FG transfers to every u in W in (a1): order Q as z, t, then unmarked; each step gcd(n_e,T_m)=6, k<=5. So LFC/VFC at
   u hold with val<=5 (units 1/6) in both orientations. Equality => mu(W*U_u)=1/6 and every non-W*U_u fibre is y-tight.
2. Transfer lemma (written check): at u, L_t subset L_z (every left U_u-fibre meeting g_tU_t meets g_zU_z) <=> at
   apex z (g_z=1) D_t subset X_u. Hence D_t cap D_u = empty.
3. Centre count: with alpha*-row at z 3-type (T*), if D_t cap D_u = empty for all u in T*, then
   mu(union D) >= |T*|/6 + (6-|T*|)/6 = 1, contradicting V4. (Without it: >= 1 - 2 delta/3 only.)
4. This kills the explicit obstruction P(E,A,w): every u-row of P is FG-tight (value 5) with unique symmetric optimum
   1/3 on threes and z, 0 on t; t-fibres must be {t,z,a,b}, so L_t subset L_z at all u in W = T*.
5. Hand row census at u (orientation x, z-entry c in {1,2,3} from D23, no fives anywhere in (a1) - written argument):
   rows with >= 2 W-threes survive FG only for c=3, e=x_ut=2, W in {3333,3331,3311,3322}; all tight with L_t subset L_z.
   One W-three impossible. Rows with no W-three: many survivors, some FG-slack (e.g. W=2244, z 4-type, e=4: 4+c/4),
   some tight with t isolated (W=2244/2444, c in {1,2}, e=1). So (Dis) is not available from every u.
6. Next bounded action: decide whether the global combination (T^x, T^(x*), 3-rich sets R^x subset T^x) closes (a1),
   or request a GO for a frozen stdlib row-map falsification aid (exploratory only).
