# K62-FG-erratum-v1: clean statement of Lemma OO's five case; attribution of the product bound; one softened remark

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:48:49-0700.
- **Overlays:** `K62-FG-v1.md`, sha256 d47e3747ce16ffc21aa818229e79a2028923ec8722aaaae14031e079b4cad083 (frozen, unchanged), and
  `SETTING-v1.md` (sha256 3bff4e6618cb6591683f7adcc1fbd52fbd3dd16e306b024be6181c332f42bb8d).
- **Sources:** my own re-read (Q1, Q3); the parent's relay of the K63-RES Codex MINOR on attribution (Q2).

## Q1: Lemma OO, item "No 5" — replacement text (the frozen text contains unfinished phrases)
"*No 5.* (Threes are already excluded.) If h_d = 0, a five u (x_vu = 5) has an odd label without common 5 with
lambda_d, so y_u = y_d = 1 gives val = 8. If h_d >= 1, no C-vertex is 5-marked, so 5 divides lambda_u iff x_vu = 5; let
F5 be the set of fives at v.
(i) If some u' in O minus {v} is not a five, then x_vu' is 1, 2 or 4 and u' is incompatible with every five f: no
common 2 (lambda_f is odd), no common 5, and a common 3 would need f_u' >= 2 and f_f >= 2 (two 3-markers) or
3 | x_vu'. Then y = 1/|F5| on F5 and y_u' = 1 (all else 0) is feasible and val >= 5 + 1.
(ii) If all four are fives and 5 does not divide x_(v i*): lambda_(i*) and a five share no 2 and no 5, and share a 3
only if the five is t and x_(v i*) = 3. So i* meets at most one five. With y = 1/4 on F5 and y_(i*) = 1 if i* meets no
five (val >= 5 + 1), or y_(i*) = 3/4 if it meets t (then x_(v i*) = 3 and val = 5 + 9/4), every allowed set has sum
<= 1 and val >= 6.
(iii) If all four are fives and x_(v i*) = 5: INV (b) gives x*_vu = 1 for the four fives, i.e. four 1-entries in the
other orientation, excluded by the item 'At most two 1s' applied to that orientation."
Lemma OO's statement is unchanged.

## Q2: attribution of the measure bound (same correction as the K63-RES Codex MINOR)
In `SETTING-v1.md` (import boundary) and in `K62-FG-v1.md` section 3 ("the final gcd and the measure bound are as in
K63-RES section 1") the bound mu(HW) >= 1/gcd([G:H], [G:W]) for subgroups H, W of a finite group is to be attributed
directly to the L0.3 formula mu(HW) = [G : H cap W] / ([G:H][G:W]) together with lcm([G:H], [G:W]) dividing
[G : H cap W] (Lagrange). The accepted TG verdict (three subgroups) is not broadened.

## Q3: section 6, second bullet — softened
Replace "(FG-62 can fail there only through a T-factor 7 in the step that adds t or i*)" by "(FG-62 is not
established for the family whose d-i* entry is 3; no claim is made about how it could fail)".

Nothing else changes.
