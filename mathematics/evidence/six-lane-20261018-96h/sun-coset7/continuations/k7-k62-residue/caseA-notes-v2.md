# Case-A working notes v2 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T06:57:48-0700. Supersedes nothing (v1 stays). Unchecked
  scratch; no claim; no computation.

## Case-A row list (c = 3, E >= 2; W-multiset | e), local values via Cor 5/6 (<= 5)
- d = 1: R3 (2,2,2,4|4), R3' (1,2,2,4|4): rigid; L_f = L_t, L_z subset L_t.
- d = 2: (1,1,4,4) never (>= 6). (1,2,4,4|e): e = 1 never (o 1, fours 1/2, t 1 = 6); e in {2,4} = R5 rigid:
  L_z, L_s subset L_f1 cap L_f2. (2,2,4,4|2) = R1 rigid: L_f1 = L_f2. (2,2,4,4|4) = R2 slack (<= 4).
  (2,2,4,4|1): value 5 (y = (f 1/2, f' 1/2, t 1), (s 1/2, s' 1/2, f 1/2, t 1)); every fibre is {t}/{t,z} or contains f, f' and
  exactly one two.
- d = 3: (1,4,4,4|1) never (o 1, fours 1/3, t 1 = 6); (1,4,4,4|e), e in {2,4}: rigid (y_i = (o 1, f_i 1)):
  L_z, L_t subset L_f1 cap L_f2 cap L_f3. (2,4,4,4|1): value 5 (y = (f_i 1, t 1) and (fours 1/3, t 1)): every fibre
  without t contains f1, f2, f3 (so L_s subset of all L_fi). (2,4,4,4|e), e in {2,4}: apparently slack (< 5).
- d = 4: (4,4,4,4|1): value 5 (y = (f_i 1, t 1)): every fibre without t contains all four fours. e in {2,4}: slack?
- Same list for alpha*-rows (C^alpha*), with e* := alpha*_ut.

## Transfer use (Lemma TC): a rigid alpha-row at u with "L_j subset L_a" gives, at apex a in C^alpha, D_j cap D_u = empty.
At an apex a in W of C^alpha: mu(D_z) = 3/6 and the union is <= 5/6, so all mass of vertices whose D avoids D_z
(alpha*_av = 1, or a transfer D_z cap D_v = empty) must fit in measure <= 2/6.

## Degree bookkeeping (types (d, d*)): n12 + n13 + n31 even; n13 + n21 + n31 even; at most one alpha-1 and one
alpha*-1 per vertex; alpha-twins (alpha_uv = 1) share N_F and the t-entry.
