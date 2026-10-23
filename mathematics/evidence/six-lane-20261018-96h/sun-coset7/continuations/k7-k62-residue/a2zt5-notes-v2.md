# (a2-zt5) working notes v2 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:49:10-0700. Unchecked scratch; no computation.

## Lemma FG-zf (z-free / t-free granularity) - sketch
In (a2-zt5) (orientation alpha with alpha_zt = 5), for u in W and x in {alpha, alpha*}: (a) a feasible y at u with
y_z = 0 or y_t = 0 has val(y) <= 5, and if val(y) = 5 every fibre C with S_C not inside {z} (resp. {t}) has weight 1;
(b) at an apex a in W of C^alpha or C^alpha*, the union of the D_j over j != z (resp. j != t) has measure <= 5/6.
Proof idea: run the chain over V \ {u, z} (order t, p, then W') or V \ {u, t} (order z, p, then W'); every step factor
is <= 4 (resp. <= 3), the base factor alpha_tp <= 4 (resp. alpha_zp = 3), so no factor 5 or larger prime enters;
for u = p the chain has no p and 5 does not divide its index. Light fibres may hold only z (resp. t).
Consequences: Lemma EQ (union without z), SUB, IN, CELL, K3 (j, u != z), the rigid rows (their weights avoid z),
Lemma B (each kill avoids z or t) and PFG-t/Corollary L ("at least two fours") hold in (a2-zt5) in both orientations.
Lost: containments L_z subset ... (fibres with S_C = {z} may be light), the R3/TR route for alpha*-rows (fibres {t}),
and arguments using z inside a union bound.

## (zt5-B) data (sketch)
T* = {a1,a2,a3}, O* = {v1,v2}: alpha a-a 4, a-v 2, v1v2 4, t-v 4; at least two a with alpha*_ta = 4 (Cor L in
C^alpha) and alpha_ta <= 2. alpha*_va in {3,4}. If alpha*_av1 = 4 then alpha*_av2 = 4 is forced (three/four labels are
coprime: y = (v1 1, v2 1) gives 7), and then K3 at v1 in C^alpha* (masses alpha_v1v2 = 4, alpha_v1a = 2) forces a's
alpha*-row to be R2*: alpha*_aa' = alpha*_aa'' = 2, alpha*_ta = 4. If alpha*_av = 3 for both v, a's alpha*-row is
(3,3,1,1) or (3,3,2,2) (value 5 with y_z = y_t = 0); the RICH route (L*_t subset L*_z) is not available.
