# Written facts v8 (worker InfoCFR27Lift; written 2026-10-17 17:24 PDT) -- twisted actions of order-6 groups

Twisted element s_t = (mu, pi, t): (s_t c)_i = mu c_{pi^-1(i)} + t_i, t modulo the diagonal. Conjugating the DM by a row
translation u replaces t by t + (L - 1)u, L(t)_i = mu t_{pi^-1(i)}; classes = first cohomology. Computed by brute force
over Z_27^5 (../code/twist_classes_v1.py, ../code/twist_classes_s3_v1.py; outputs in
../cfr27/dmorbit-v1/twist/runs-v1/ and ../cfr27/dmorbit-v1/calib-xc2/runs-v1/twist-S3*.out):
* T6, T4odd, T10, S3a: only the trivial class (every twist is removable).
* T8 = <(1, (0 1 2 3 4 5))>: two nontrivial classes, representatives t = (0,1,0,0,0,0) and (0,2,0,0,0,0) (images of
  each other under the global multiplier -1).
* S3b: two nontrivial classes, sigma twist (0,0,2,1,1,0) or (0,0,4,2,2,0), tau = (26, (1 2)(4 5)) untwisted.
* A twisted group with a G-fixed column c is conjugate to the untwisted group (translate by -c, as in facts-v7 F5),
  so for a nontrivial class only "no G-fixed column" (nozero mode) is new.

## T1 (twisted T8 is impossible) [written proof; matches dmorbit_xc_v2: root item without options]
s = (1, pi6, t), t = e_1 (class representative; the other class is its negative). s^3 = (1, pi6^3, t3) with
t3 = t + Lt + L^2 t = (0,1,1,1,0,0) and pi6^3 = (0 3)(1 4)(2 5). On the row pair (0,3):
(s^3 c)_0 - (s^3 c)_3 = (c_3 + 0) - (c_0 + 1) = -(c_0 - c_3) - 1, an involution d -> -1 - d of Z_27 with the single fixed
point d = 13. The column D with c_0 - c_3 = 13 is unique, and s^3 D also has difference 13, so s^3 D = D + g 1. From
rows 0 and 3: c_3 = c_0 + g and c_0 + 1 = c_3 + g, so 2g = 1, g = 14. Row 2 then gives c_5 + 1 = c_2 + 14, i.e.
c_5 - c_2 = 13. But (s D)_0 - (s D)_3 = (c_5 + t_0) - (c_2 + t_3) = c_5 - c_2 = 13 as well, and s D != D (else s fixes D
and then the untwisted conjugate argument applies: a twisted class with a fixed column is trivial). Two different
columns with difference 13 on the pair (0,3): contradiction. Hence no (Z_27,6;1)-DM is invariant under a twisted T8.
dmorbit_xc_v2 agrees: 768,960 valid orbits, all of size 6, none covers the item (pair (0,3), value 13).
