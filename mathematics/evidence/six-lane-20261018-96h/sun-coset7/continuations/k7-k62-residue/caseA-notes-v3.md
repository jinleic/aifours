# Case-A working notes v3 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:05:51-0700. Unchecked scratch; no computation.

## Lemma T-TIGHT (sketch)
C^alpha, Gamma^alpha connected, t's alpha*-row on W = 44222 or 44122 (fours f1, f2). PFG-t equality: every W-coset at t
is {f1,f2,s}, {s,s'} or {o}; {s,s'}-mass = 1/6 (44222) resp. 0 (44122). A single-four alpha-vertex u0 (R3/R3', four f)
with alpha*_tu0 = 2 has D_u0 cap D_f = empty at t (Lemma TC from L_f = L_t at u0). If f in {f1,f2}, all u0-mass (2/6)
sits in {s,s'}-cosets: contradiction. So such f is not in P*.

## Degree types (no d = 3, d* = 3): (n12, n21, n22) in {(2,0,3), (0,2,3), (2,2,1), (4,0,1), (0,4,1)}.

## Structure S1 = (2,0,3): F = path u0-a-b-c-u1, F* = complementary pentagram, N = {u0u1}. DEAD (sketch):
- Twin rule kills every W-entry 1 (twins would share N_F / N_F*): all W-entries of alpha, alpha* in {2,4}, alpha = alpha* = 2 on u0u1.
- u0, u1: alpha-row R3 (fours a, c), so alpha_tu0 = alpha_tu1 = 4; t-triangles give alpha_t in {2,4} on a, b, c.
- Cor L both ways: t's alpha-row is 44222 or 44422, |P*| >= 2 inside {a,b,c} \ P.
- alpha*-triangle {t,u0,a} (alpha*_u0a = 2): alpha*_tu0 = 1 forbids alpha*_ta = 4 (and symmetric for u1, c).
- |P*| = 2 (tight row): in every placement some single-four vertex (u0 with a in P*, or u1 with c in P*) is forced to be
  an alpha*-two of t: T-TIGHT kills it. (Covers t's alpha-rows 44222 with |P*| = 2 and all 44422 cases.)
- |P*| = 3 (P* = {a,b,c}, t's alpha-row 44222): a, b, c have alpha-rows R1 (e = 2); at apex b (C^alpha) the transfers
  D_u0 cap D_a = D_u1 cap D_c = empty (from R1 at a and at c) give the K7-TC-A22 count: union >= 1, contradicting V4.
- Hence also (0,2,3) dead by inversion.

## Remaining structure list to check
(2,2,1), (4,0,1)/(0,4,1), and the structures with a (1,3) or (3,1) vertex (including F = K_{2,3}).
