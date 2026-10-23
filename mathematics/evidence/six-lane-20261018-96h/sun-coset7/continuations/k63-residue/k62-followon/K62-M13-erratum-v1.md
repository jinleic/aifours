# K62-M13-erratum-v1: explicit fresh row-count derivation in M13-C

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T08:58:10-0700.
- **Frozen target, unchanged:** `K62-M13-C-v1.md`, SHA256 13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12, lines 58-63.
- **Responds to:** Codex review `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13-codex-v1.prompt.stdout.txt`,
  SHA256 c8c4184bb4c71df3a34f04dcf1f03424b76df60ea9b229216eea6e89c14ef17d, ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 1 MINOR,
  finding M1 at review lines 119-136. Claude returned NO_VERDICT (capacity refusal), not a mathematical verdict.
- **Accepted prerequisite:** CAP/DT parent verdict `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-parent-verdict-v1.md`,
  SHA256 84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0, at its exact C1, RC-O and RC-i* interfaces.
- **Rule:** one exact Old/New repair. The Old block was checked to occur exactly once in the frozen C file. The numerical
  statements, centres, orientations and nonstrictness are unchanged; no new bound or pattern closure. The proof is now
  explicit rather than importing general RC beyond its accepted scope. All NEW M13 claims remain candidates; the old
  CONDITIONAL ON CAP/DT labels are discharged only for those exact imported prerequisites, not for M13's new lemmas.

## M1: replace the row-consequences paragraph by the fresh light-fibre proof and its inverted counterpart

**Old:**
```text
**Row consequences (opposite-family orientation explicit).** At every unmarked v in O, **both rows satisfy 5/6**:
- the alpha-row: Lemma RC with the alpha*-family granularity supplied by C2;
- the alpha*-row: Lemma RC with CAP (C1) for the alpha-family, whose distinguished entry alpha_(d i*) = 1 meets its
  hypothesis.
At i*, both rows satisfy 11/12 by (RC-i*), since f* = 1. These are only global, nonstrict bounds. No subset or atom grid
at an O-vertex or i* is obtained.
```

**New:**
```text
**Row consequences (opposite-family orientation explicit).** At every unmarked v in O, **both rows satisfy 5/6**:
*Fresh proof of the alpha-row bound, not an application of old (RC-O).* Normalize g_v = 1 by a common left translation;
this conjugates all U*_j by the same element and leaves their intersection indices unchanged. Put
  W' := intersection of U*_j over j != v, T := [G : W'], q := gcd(n_v, T) = 6,
where the equality q = 6 is the new C2 above, using C1w and the M13-B witness. The fibres are the n_v left cosets of U_v.
For each j != v put L_j := g_jU_jU_v, the union of the t_j = n_v alpha_vj/g_vj fibres meeting g_jU_j (LFC (a)-(b)).
The set W'U_v misses every L_j: if w u is in L_j, with w in W', u in U_v, write w = g_j a g_j^-1 with a in U_j. Then
w u in g_jU_jU_v gives a g_j^-1 in U_jU_v, hence g_j^-1 in U_jU_v, so g_j in U_vU_j and g_jU_j meets U_v = g_vU_v,
contrary to disjointness. Thus each of the fibres contained in W'U_v is empty of all the other pieces. Their number is
  M = [W' : W' cap U_v] = [G : W' cap U_v] / T >= lcm(n_v, T)/T = n_v/q = n_v/6
by Lagrange. For any y >= 0 feasible for the lambda^alpha-allowed sets at v, LFC (c) says every remaining fibre F has
allowed S_F, so sum over j in S_F of y_j <= 1. Counting incidence weights (LFC (a)-(b)) gives
  n_v sum over j != v of y_j alpha_vj/g_vj = sum_j y_j t_j
    = sum over all fibres F of (sum over j in S_F of y_j) <= n_v - M <= (5/6)n_v.
Divide by n_v. This proves the additional alpha-row bound from the new alpha*-family granularity without importing
Lemma RC outside its accepted (RC-O)/(RC-i*) interfaces.
*The alpha*-row, with inversion explicit.* Apply the same light-fibre calculation to the inverted configuration,
whose pieces are g_j^-1 U*_j, whose subgroup family is (U*_j), and whose conjugated family is (U_j) (INV (a)-(b) with E6).
Normalize its representative at v to 1; the common conjugation leaves T_alpha(V minus {v}) unchanged. Its opposite-family
gcd is q_0 := gcd(n_v, T_alpha(V minus {v})), which divides 6 by accepted CAP (C1), since alpha_(d i*) = 1 and v is
unmarked. Its corresponding empty-fibre count is at least n_v/q_0 >= n_v/6 by the same avoidance and Lagrange argument.
Summing any feasible weights for its own lambda^alpha*-allowed sets therefore gives sum_j y_j alpha*_vj/g_vj <= 5/6.
This row is also within the old (RC-O) interface; only the alpha-row above uses the newly established granularity.
At i*, both rows satisfy 11/12 by accepted (RC-i*), since f* = 1. These are only global, nonstrict bounds. No subset or atom
grid at an O-vertex or i* is obtained, and no additional universally strict slack is asserted.
```

## Boundary
Nothing else in A-D changes. Both model reviews of the corrected complete snapshot are still required before a parent
M13 verdict. Marked centres, the (1,3)/(3,1) regimes, full K6.2* and Sun(7) remain OPEN. No computation. Computer-assisted
Sun(5)/(6) provenance remains in the LFC/VFC and class-reduction import closure; no new Sun instance is introduced here.
