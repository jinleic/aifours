# Checkpoint 011 (Sun7K62Successor)

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T05:54:42-0700. Previous: checkpoint-010 at 2026-10-19T05:47:48-0700.
- No computation run; no process running; no old/sibling artifact edited. Decision request on (a1)-vs-(a2) priority sent
  to parent (no reply yet); continuing (a2) per the parent's last instruction.

## (a2) written results since 010 (NOT yet frozen; next candidate file K7-A2-FIVE)
Setting: z (2^E), t (3^A), p (5^B) distinct, W' four unmarked; D23P (candidate in review) gives z-rows (b').
1. **FG-a2:** at u in W', orientation x, val <= 5 if 5 !| x_zt or 3 !| x_zp or x_tp odd (chain orders (z,t,p,..),
   (z,p,t,..), (t,p,z,..)); at p, val <= 5 if x_zt != 5 (order z, t, W' with k <= x_uz <= 3).
2. **Fives:** no W'-W' five; no u-p five; no z-p five; no t-p five (all by strict LFC); x_zt = 5 forces the x-row at
   z to be (3,3,3,3 | p 3 | t 5); x_ut = 5 forces u's x-row (3,3,3 | z 3 | p 3 | t 5), x_zt = 5 and x_tp in {2,4}
   (value 17/3 > 5, FG must fail).
3. **D23-a2:** if x_zt != 5, then p behaves like an unmarked neighbour at z (no other label has a 5), ROW-1 applies to
   W' cup {p}, and the x-row at z is 3-type relative to W' cup {p}.
4. **Split:** (a2-no5): no entry 5 in either orientation; then every LFC/VFC gcd, triangle bound and FG chain coincides
   with an (a1) configuration on W := W' cup {p} (p's 5^B is invisible), so (a1)'s residue and results transfer.
   (a2-zt5): exactly one orientation has x_zt = 5, with the forced z-row above, the other row 3-type with x*_zt = 1, and
   W'-entries at t in {2,4,5}.

## Next bounded action
Freeze K7-A2-FIVE with full proofs (items 1-4), then return to the (a1) Case-B/Case-A transfer-count mechanism (which
then also covers (a2-no5)). Next checkpoint by 06:50 PDT.
