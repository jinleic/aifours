# K62-CAP-DT-erratum-v1: consolidated overlay for the CAP/DT dual review (K62-CAP, K62-DT-A, K62-DT-B, K62-DT-C)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:40:16-0700.
- **Author:** Sun63Successor; written only. The HOLD (`RUN/review/runtime-guard-admission-HOLD-v1.json` 6c1d8440…) is in
  force; nothing was run; no enumeration and no new pattern closure.
- **Overlays (frozen, unchanged):** `K62-CAP-v1.md` sha256 19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5;
  `K62-DT-A-v1.md` sha256 cd7266d4071a8c91ac753b1f9900d690b72cf667f74046a1f90b5b449afd1a70;
  `K62-DT-B-v1.md` sha256 51960d44d60fa50901a3201143410f935750852d1ccd4c6e116f81a9c601604f;
  `K62-DT-C-v1.md` sha256 7e8bde21d6f5a162d5ecd5bd5950c90cbcd18763880bd1ee781d240b91f2186b;
  `K62-DT-C-erratum-v1.md` sha256 0f785140e10fe0e650ed683186e9e51f95abffce356e962172fcb0446a271a3b. Item CD21 carries over and supersedes
  that erratum's single item.
- **Responds to:** review freeze `RUN/review/sun7-K62-CAP-DT-review-freeze-v1.json` (sha256 6cb9a897750dfc44e3dce8e2a53b9a3fd678de7458b9560be462b315204dc2ff);
  Codex `RUN/review/sun7-K62-CAP-DT-codex-v1.prompt.stdout.txt` (sha256 93eeb14086017e92a77db4ea76f6b9208675a2e520c9624285d15af0c3f0a3ac),
  ACCEPT-WITH-FIXES; Claude `RUN/review/sun7-K62-CAP-DT-claude-v1.prompt.note.md` (sha256 03f273cfcb194043c2b560f6c9da244d9979eedcbf24e5f8f924c3ceafca77db),
  0 FATAL / 0 MAJOR / 12 MINOR (section 2); the parent's IRC questions Q1, Q2 and the parent's correction of my Q2 answer.
- **Rules.** Each Old block below was checked, before this write, to occur exactly once in the named frozen file; New
  replaces Old; nothing else in those files changes except through the reading rule GR. **No statement changes.** CD1, CD2,
  CD12-CD14 repair proofs. CD3 writes the frozen Consequences paragraph out as Lemma RC; its bounds are the frozen ones.
  CD4 states the discipline that "a predicate on U62" already required. The rest are notation, citations and labels.
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

## Disposition map
| Finding | Disposed by |
|---|---|
| Codex CAP B2; Claude m1 | CD1 |
| Codex CAP C2; Claude m2; parent Q1 | CD2 |
| Claude m3; Codex "CAP C row consequences" | CD3 |
| Claude m4; Codex "DG correction at pattern level", CAP D; parent Q2 and its correction | CD4, W1 |
| Claude m5 | CD5, CD6 |
| Codex CAP B5 remark; Claude Q2 | CD7 |
| Claude m7; Codex DT-A section 1 ("admissible") | CD8, CD9, GR |
| Codex DT-A 3a; Claude Q4 | CD10 |
| Codex DT-A 3c; Claude m6 | CD11 |
| Codex DT-B section 0; Claude m8, m10 | CD12 |
| Codex DT-B R4 (positive support); Claude m10 | CD13 |
| Codex DT-B R3; Claude m10 | CD14 |
| Codex DT-B B3, B5; Claude m9 | CD15, CD17, CD18 |
| Codex DT-B B4 remarks; Claude Q4 | CD16 |
| Claude m11; Codex DT-B section 4 (connectivity) | CD18 |
| Claude m12 | CD19, CD20, CD21 |
| Codex DT-C C3 remark (equality clause algebraic) | CD21 |
| Codex DT-C C4 | CD22 |
| Accepted by both reviews without a requested change: CAP (A1)-(A4), (B1), (B3) beyond notation, (B4), (C1); DT-A section 1 (all rows), CI, CI', (3b); DT-B (R4)/(R3) values, B1, B2, the B4 case split; DT-C C1-C3 algebra; Claude Q3 (no grid at O or i* granted or used) | no change |

## GR: reading rule for labels and row-bound citations (no text replaced)
- In `K62-DT-A-v1.md` (heading of section 3), `K62-DT-B-v1.md` (Labels bullet; headings of sections 3 and 4) and
  `K62-DT-C-v1.md` (Labels bullet; heading of C3), "CONDITIONAL ON DG" reads: "depends on Theorem DG, accepted by verdict
  `RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md` (sha256 cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda) as
  CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, with DG's orientation (the family x needs x'_(d i*) = 1) and four-subset hypothesis
  explicit". DT-A gets the same change as explicit text in CD8.
- In DT-A, DT-B and DT-C, "the 5/6 row bounds of K62-CAP (C)", "the O-row bounds of K62-CAP (C)" and "(K62-CAP (C))" used
  as a row bound read "Lemma RC (item CD3) with (C1) for the opposite family". "The 11/12 bound" reads "(RC-i*)", which
  needs f* = 1.
- CAP-62, DT-A, DT-B and DT-C remain candidates until the parent's verdict on this review round.

## W1: withdrawal of my IRC equivalence claim (parent's Q2 correction)
After the review freeze, my IRC answer to the parent's question Q2 claimed two things. First, that DG's bound
"S <= 19/16 - 2/n_d" is *equivalent*, on the 1/32 grid, to the pattern-level predicate "S < 19/16" (S <= 37/32), so that
"nothing is lost". Second, the same for "N(O)/n_d < 1/8" in place of "N(O) <= n_d/8 - 1/2". **Both claims are false and are
withdrawn**; the withdrawal was first recorded in `checkpoint-013-v1.md` (sha256 9c6102199c6327427ffe38ebbb964e07f318f7e78fb3d73d2143de6f4dc44112). The grid argument absorbs 2/n_d only when 2/n_d <= 1/32, i.e. n_d >= 64. Counterexamples to
equivalence:
- at n_d = 16, DG gives S <= 17/16, while S < 19/16 admits 18/16 (for example eight terms 1/8 and two terms 1/16);
- at n_d = 32, DG gives S <= 36/32, while the grid test admits 37/32.
The correct statement is CD4 (D3)-(D4): pattern-level predicates are safe necessary weakenings and are lossy in general.
No equivalence for n_d >= 64 is claimed here. My Q1 answer stands and is item CD2.

## CD1: CAP (B1)/(B2) proof: the 3-part exception 9 at d
*File:* `K62-CAP-v1.md`. *Disposes:* Codex CAP B2 (MINOR); Claude m1.
*Why:* The frozen bound "every other label in a gcd with it has 3-part <= 3" fails at v = d when x_(d i*) = 3: there lambda_(i*) has 3-part 9. The conclusion (determinacy through min(f, 2)) is unchanged; proof only.

**Old:**
```text
3- and 5-parts: only m3 (resp. m5)
has exponent >= 2 (resp. >= 1); every other label in a gcd with it has 3-part (resp. 5-part) <= 3 (resp. 5), so the gcd
depends on f_(m3) (resp. h_(m5)) only through min(., 2), as in rules-k7-v1 Lemma CAP.
```

**New:**
```text
3- and 5-parts: only m3 (resp. m5)
has vertex exponent f >= 2 (resp. h >= 1). A label lambda = n_j x_vj / g_vj not belonging to m5 has 5-part <= 5 (at most
one factor 5, from an entry x = 5), so a 5-part of a label gcd reads h_(m5) at most through min(h_(m5), 1). A label not
belonging to m3 has 3-part <= 3, with **one exception, at v = d:** if x_(d i*) = 3 (then t lies in O and f* = 1, K62-E3
Lemma 1), lambda_(i*) = n_(i*) * 3 / 4 has 3-part 9, and gcd(lambda_t, lambda_(i*)) = 3^(min(f_t, 2)) = 9. (At an O-vertex
and at i*, every C-label is n_j x / 6, which removes one factor 3, so a non-m3 C-label has 3-part 3^(v3 x) <= 3, and the
d-label has 3-part 3^(v3 x_(dv)) <= 3; at d, the O-labels n_c / 2 have 3-part 3^(f_c) = 3 for c != t, and lambda_(i*) has
3-part 3^(f*) = 3 when x_(d i*) = 1 and i* is not m3.) Hence the gcd depends on f_(m3) (resp. h_(m5)) only through
min(., 2), as in rules-k7-v1 Lemma CAP; the cap 2 on f is exactly what the exception at d needs.
```

## CD2: CAP (C2) proof: exact first O-step (gcd 2, k = 1) when t is absent
*File:* `K62-CAP-v1.md`. *Disposes:* Codex CAP C2 (MINOR); Claude m2; parent question Q1.
*Why:* The frozen proof added p (or an unmarked vertex) with gcd 6 even when t is absent; then the first O-vertex after d has gcd 2 with n_d and k = 1 exactly. The statement of (C2) is unchanged; proof only.

**Old:**
```text
(C2) order d, t, p, unmarked rest. Adding t: gcd(n_t, n_d) = 2, k <= 2 * (1/2) = 1. Adding p != t: gcd(n_p, lcm(n_d, n_t)) = 6,
k <= 3. Unmarked: gcd 6, k <= 3. Then gcd(n_(i*), T): 2-part min(2, v2 T) = 2 (v2 T >= e_d); 3-part 3^(min(f*, v3 T)) = 3
(f* = 1, v3 T >= 1); 5-part 1 (if h* >= 1, neither d nor an O-vertex is 5-marked and all k <= 3). QED
```

**New:**
```text
(C2) Order d, then a first O-vertex u (u := t if t exists; otherwise u := p if p lies in O; otherwise any O-vertex), then
the other marked O-vertex p != u if there is one, then the unmarked rest. *First O-step (exact, in every case, including t
absent):* T_1 = n_d and gcd(n_u, n_d) = 2 (n_d has no factor 3, h_d h_u = 0, the w's are coprime), so
k = 2 mu(Phi_uPhi_d) = 2 (x_ud / 2) = x_ud = 1 exactly (A2); thus T_2 = lcm(n_d, n_u), which contains 3^(f_u) with f_u >= 1.
*Later O-steps:* every later O-vertex e has gcd(n_e, T_m) = 6 and k <= 6 mu(Phi_ePhi_d) = 3. Indeed the 2-part is 2
(v2 n_e = 1); the 3-part is 3 (f_e = 1, because t, if it exists, is u; and 3 divides T_m); the 5-part is 1 (if e = p, then
m5 = p, so h_d = h* = 0, the earlier O-vertices are not 5-marked, and every earlier k is an integer <= 3; if e is
unmarked, h_e = 0); the w-part is 1 (no k so far has a prime > 5, so the prime-to-30 part of T_m is the product of the w's
already included). Then gcd(n_(i*), T): 2-part min(2, v2 T) = 2 (v2 T >= e_d); 3-part 3^(min(f*, v3 T)) = 3 (f* = 1,
v3 T >= 1); 5-part 1 (if h* >= 1, neither d nor an O-vertex is 5-marked and every k is an integer <= 3); w-part 1 (w_* is
not included). So gcd(n_(i*), T) = 12. QED
```

## CD3: CAP (C) Consequences written out as Lemma RC (nonstrict row count, opposite-family granularity, light-fibre proof)
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m3; Codex "CAP C row consequences" (keep orientation and f* = 1); parent mandatory item.
*Why:* The frozen paragraph stated the 5/6 and 11/12 row bounds with a pointer to K62-E3 step 3. Lemma RC now states them with a full proof: nonstrict, no slack in n_v, with the orientation explicit (the x-row uses (C1)/(C2) for x'). (RC-O) and (RC-i*) are exactly the frozen bounds; (RC) is the inequality the pointer's argument proves.

**Old:**
```text
*Consequences (used by rules R1).* With the light-set argument of K62-E3 step 3 (and its VFC analogue: U_vW is
contained in every U_vU_j, hence disjoint from every D_j by (V1)): at an unmarked v in O, the alpha-row count holds with
bound 5/6 when alpha*_(d i*) = 1 (granularity of Phi^alpha*), and the alpha*-row count holds with bound 5/6 when
alpha_(d i*) = 1 (granularity of Phi^alpha); at i*, if f* = 1, both counts hold with bound 11/12.
```

**New:**
```text
**Lemma RC (row count with light fibres).** Let v be a vertex, x in {alpha, alpha*} a family and x' the other family.
Every y >= 0 on V minus {v} that is feasible for the lambda^x-allowed sets at v (sum over j in T of y_j <= 1 for every
lambda^x-allowed T, where lambda^x_j = n_j x_vj / g_vj are the LFC labels of the configuration whose alpha-matrix is x)
satisfies
  (RC)  sum over j != v of y_j x_vj / g_vj  <=  1 - 1/gcd(n_v, T_x'(V minus {v})).
In particular (nonstrict bounds, no slack depending on n_v; **the x-row bound uses the granularity of the opposite family
x'**):
- (RC-O) if v in O is unmarked and **x'_(d i*) = 1**, (C1) applied to x' gives the bound 5/6;
- (RC-i*) if v = i* and f* = 1, (C2) applied to x' gives the bound 11/12.
*Proof (light fibres).* Case x = alpha. Left-translate so that g_v = 1 (the translated representatives keep the names
g_j); this conjugates every U*_j = g_jU_jg_j^-1 by one common element, so T_alpha*(.) is unchanged, and U*_v = U_v. The
fibres at v are the n_v left cosets of U_v. For j != v, L_j := g_jU_jU_v is the union of the t_j = n_v alpha_vj / g_vj
fibres that meet g_jU_j (LFC (a)-(b)). Put W' := intersection of the U*_j (j != v), of index T := T_alpha*(V minus {v}).
*W'U_v misses every L_j* (the argument of accepted K62-E3 step 3, with v in place of d): if w u lies in L_j with w in W' and
u in U_v, write w = g_j a g_j^-1 (a in U_j); then g_j a g_j^-1 u lies in g_jU_jU_v, so g_j^-1 lies in U_jU_v, so g_j lies in
U_vU_j, and g_jU_j meets U_v = g_vU_v, contradicting disjointness. W'U_v is the union of the M := [W' : W' cap U_v] fibres
wU_v (w in W'), the *light fibres*: they include U_v, each has S_F empty, and M = [G : W' cap U_v] / T >= lcm(n_v, T) / T
= n_v / gcd(n_v, T) (Lagrange). Every other fibre F has S_F lambda^alpha-allowed (LFC (c)), so its sum over j in S_F of
y_j is <= 1. Hence n_v sum_j y_j alpha_vj / g_vj = sum_j y_j t_j = sum over fibres F of (sum over j in S_F of y_j)
<= n_v - M, which is (RC). Case x = alpha*: apply the case x = alpha to the inverted configuration (g_j^-1 U*_j) (INV (a)
with E6): it has the same indices, its alpha-matrix is alpha* (INV (b)), its LFC labels are the lambda^alpha*_j, and its
conjugated family is (g_j^-1 U*_j g_j) = (U_j) = Phi^alpha, so T becomes T_alpha(V minus {v}). Particular cases: under the
stated hypotheses gcd(n_v, T_x'(V minus {v})) divides 6 by (C1) (resp. 12 by (C2)), and 1 - 1/g <= 5/6 (resp. 11/12) for
every divisor g of 6 (resp. 12). QED
*VFC form (used in K62-DT-A Lemma CI).* In the Phi^x-configuration at v, Phi_vW (W := intersection of the Phi^x_j, j != v)
lies in every X^v_j = Phi_vPhi_j, hence misses every D'_j (V1), and mu(Phi_vW) >= 1/gcd(n_v, T_x(V minus {v})) (L0.1,
Lagrange): there the union of the D'_j, which carries the x'-row, is bounded by the granularity of x. Neither form gives a
grid of proper subsets at v (section 3).
```

## CD4: CAP (D): rule discipline; strict weakenings are lossy; quantifiers
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m4; Codex "DG correction at pattern level" and CAP D quantifiers; parent's correction of my Q2 IRC claim (with W1).
*Why:* Makes explicit which predicates count as rules: side conditions decidable from pi; only slack-free normalized inequalities or strict necessary weakenings; rounding only onto lattices determined by pi. Records that strict weakenings are lossy, not equivalences. The transfer implication is unchanged.

**Old:**
```text
**(D) Transfer.** Call a *rule* a statement, proved from accepted imports, of the form "every configuration Gamma of
the residue satisfies P(pi(Gamma))" with P a predicate on U62 built from the quantities in (B) and the bounds in (C).
If every element of U62 violates some rule, the residue has no configuration in any finite group, hence (R0) in any
group. QED
```

**New:**
```text
**(D) Transfer.** Call a *rule* a statement, proved from accepted imports, of the form "every configuration Gamma of
the residue satisfies P(pi(Gamma))", where P is a predicate on U62 obeying this discipline:
- (D1) its side conditions (sub-case, orientation, and the hypotheses of every imported lemma, for example the orientation
  and the four-subset hypothesis of Theorem DG, or the hypotheses of Lemma RC) are decidable from pi;
- (D2) it reads only pi and the quantities of (B), together with the bounds of (C) and Lemma RC;
- (D3) every imported inequality enters either in a slack-free normalized form (for example Lemma RC: <= 5/6 and <= 11/12,
  nonstrict; K62-E3 C2: n_4 >= 2 n_1 + 2, an integer statement about the matrix) or as a **strict necessary weakening**:
  an inequality X <= c - epsilon(Gamma) with epsilon(Gamma) > 0 depending on n_v, n_d, the w's or absolute counts yields
  only X < c (for example LFC (d) yields sum y x/g < 1; a rule importing DG-2 (N(O) <= n_d/8 - 1/2) gets only
  N(O)/n_d < 1/8; a rule importing Theorem DG (a) gets only S_x < 19/16, where S_x is the sum over the O-triples R of
  2^(-min(e_d, v2 T_x(R))));
- (D4) rounding is allowed only onto a lattice that pi determines (for example 32 S_x is an integer because every capped
  triple depth is <= 5, so S_x < 19/16 gives S_x <= 37/32; when e^_d = 4, 16 S_x is an integer and S_x <= 9/8; DG-1 gives
  N(Q)/n_d in 2^(-r_Q) Z_(>0) with r_Q = min(e^_d, v2 T_x(Q)), which fixes the grid but not the value).
**Strict weakenings are lossy; they are not equivalent to their sources.** For example Theorem DG (a) gives S_x <= 17/16
at n_d = 16 and S_x <= 36/32 at n_d = 32, while the pattern-level predicate admits S_x = 18/16 and S_x = 37/32 there. A
rule that needs an exact n_d-dependent form would need a pattern carrying an n_d-class, which CAP-62 does not define. Not
functions of pi: n_v and n_d (through 5^(h_d) w_d, and e_d once e_d > 10), the absolute counts t_j, M and N(Q), and the
slacks 1/n_v, 2/n_d and 3/(2 n_d).
*Transfer.* For every configuration Gamma of the residue in a finite group, pi(Gamma) lies in U62 by (A) and every rule
holds at pi(Gamma). So if for every pi in U62 some rule fails at pi, the residue has no configuration in any finite group,
hence (R0) in any group. Surjectivity of pi onto U62 is not needed, but every stored triangle choice, orientation and
marker case must be covered. U62 is finite, but no element-wise check exists; (D) proves nothing about the residue until
such a check is carried out and itself reviewed. QED
```

## CD5: CAP (B3): vertex letters distinct from the family letter
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m5 (first clause).
*Why:* The letter x named both a vertex and a family. Notation only.

**Old:**
```text
- (B3) tau_min, tau_max, every apex measure mu(Phi_y(Phi_x cap Phi_z)) = tau_x(xyz) / (gamma_y x_xz) (L1 (T3)) and every pair
  measure mu(Phi_xPhi_y) = x_xy / g_xy (L0.1);
```

**New:**
```text
- (B3) tau_min, tau_max, every apex measure mu(Phi^x_b(Phi^x_a cap Phi^x_c)) = tau_x(abc) / (gamma_b x_ac) (L1 (T3)) and every
  pair measure mu(Phi^x_aPhi^x_b) = x_ab / g_ab (L0.1), for vertices a, b, c and the family x;
```

## CD6: CAP (pi1): remark on constant capped exponents
*File:* `K62-CAP-v1.md`. *Disposes:* Claude m5 (second clause).
*Why:* Remark only; the definition of pi and of U62 is unchanged.

**Old:**
```text
- (pi1) Marker data: m3 in {i*} cup O cup {none}, m5 in {d, i*} cup O cup {none}, with capped exponents
  min(f_(m3), 2), min(h_(m5), 2), and **e^_d := min(e_d, 10)**.
```

**New:**
```text
- (pi1) Marker data: m3 in {i*} cup O cup {none}, m5 in {d, i*} cup O cup {none}, with capped exponents
  min(f_(m3), 2), min(h_(m5), 2), and **e^_d := min(e_d, 10)**. (Remark, definition unchanged: m3 has f >= 2 and m5 has
  h >= 1 by definition, so min(f_(m3), 2) = 2 is constant, and min(h_(m5), 2) could be min(h_(m5), 1), since no gcd or
  bound reads more than h_(m5) >= 1; an enumeration of U62 as defined contains harmless duplicate patterns.)
```

## CD7: CAP (B5): normalized counts only
*File:* `K62-CAP-v1.md`. *Disposes:* Codex CAP B5 remark; Claude Q2.
*Why:* (B5) determines t_j / n_v, not t_j. Wording only; the identity is unchanged.

**Old:**
```text
- (B5) the fibre counts at every vertex v: t_j / n_v = x_vj / g_vj (LFC (a)).
```

**New:**
```text
- (B5) the normalized fibre counts at every vertex v: t_j / n_v = x_vj / g_vj (LFC (a)); the absolute counts t_j (and M,
  N(Q)) are not functions of pi (see (D)).
```

## CD8: DT-A status labels: DG dependency discharged at the verdict's scope
*File:* `K62-DT-A-v1.md`. *Disposes:* Claude m7 (first clause).
*Why:* The DG dependency of section 3 is discharged at the scope of verdict cae455c3…; the remaining candidate premise CAP (C1) is named.

**Old:**
```text
- **Status labels.** Sections 1-2 are unconditional (given the imports below). Section 3 is **CONDITIONAL ON DG**
  (`K62-DG-v1.md` sha256 a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 + erratum e435430c…, under dual
  review). Section 2 uses the global bound (C1) of the candidate `K62-CAP-v1.md` (sha256
  19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5), re-stated below with its one-line source.
```

**New:**
```text
- **Status labels.** Sections 1-2 are unconditional (given the imports below and the candidate bound (C1) of K62-CAP).
  Section 3 depends on Theorem DG (`K62-DG-v1.md` sha256 a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52
  with `K62-DG-erratum-v1.md` e435430c… and `K62-SH-DG-erratum-v1.md` 755edc21…), which the parent verdict
  `RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md` (sha256 cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda)
  accepts as CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, with DG's orientation and four-subset hypothesis explicit; the former
  label CONDITIONAL ON DG is discharged at exactly that scope. Section 2 uses the global bound (C1) of the candidate
  `K62-CAP-v1.md` (sha256 19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5), re-stated below with its one-line source.
```

## CD9: DT-A section 1: citation of the tau bound (DG-3 in its G3 form); "admissible"
*File:* `K62-DT-A-v1.md`. *Disposes:* Claude m7 (second and third clauses); Codex DT-A section 1 remark.
*Why:* Cites the tau bound in its accepted G3 form. The apex identity stays cited as L1 (T3) of rules-k7-v1 earlier in section 1, one of the two citations Claude m7 allows.

**Old:**
```text
With tau a multiple of lcm(x's) and tau <= (product of the two smallest values) (K62-DG Lemma DG-3, whose proof is L1):
```

**New:**
```text
With tau a multiple of lcm(x's) and tau <= (product of the two smallest values) (Lemma DG-3 in its form of
K62-SH-DG-erratum-v1 G3, accepted; its elementary proof (L0.1, Lagrange, Z11 (a)) applies verbatim to either family;
"admissible" below means allowed by these two constraints and makes no realizability claim):
```

## CD10: DT-A (3a): raw versus capped depth
*File:* `K62-DT-A-v1.md`. *Disposes:* Codex DT-A 3a; Claude Q4.
*Why:* Distinguishes raw depth from capped depth. The types T1-T3 are unchanged.

**Old:**
```text
- (3a) **Deep triples.** In Theorem DG (b) the triples R with min(e_d, depth) >= 4 have x-values (2,4,4) with tau = 8
  (type T1) or (4,4,4) with tau in {8, 16} (types T2: tau = 8, depth 4, no forcing; T3: tau = 16, depth 5). By CI', a
```

**New:**
```text
- (3a) **Deep triples.** For S in O with |S| in {3, 4} write v2 T_x(S) for its *raw depth* (for a triple,
  1 + v2 tau_x(S) <= 5 by DG-3) and r_S := min(e_d, v2 T_x(S)) for its *capped depth*, the quantity read by Theorem DG; in
  this section "depth" alone means capped depth. In Theorem DG (b) the triples R with r_R >= 4 (equivalently raw depth
  >= 4, as e_d >= 4) have x-values (2,4,4) with tau = 8 (type T1: raw and capped depth 4) or (4,4,4) with tau in {8, 16}
  (types T2: tau = 8, raw and capped depth 4, no forcing; T3: tau = 16, raw depth 5, capped depth min(e_d, 5), which is 4
  when e_d = 4). By CI', a
```

## CD11: DT-A (3c): capped-depth counts, unambiguous names, "implies" (necessary weakening of DG (a))
*File:* `K62-DT-A-v1.md`. *Disposes:* Codex DT-A 3c (MINOR); Claude m6; count-name clash (a, b, c, e were also vertex names).
*Why:* The inequality is unchanged up to renaming (a, b, c, e -> theta_4, theta_5, theta_2, theta_1, counted by capped depth). It is now derived explicitly as a strict necessary weakening of DG (a), not as an equivalent reading.

**Old:**
```text
- (3c) **Weights.** Writing a, b, c, e for the numbers of triples of depth 4, depth 5, depth 2 and depth 1, DG (a)
  (all 4-subsets of depth <= 4) reads 2a + 3b >= 3 + 4c + 12e (sum over triples of 2^(-depth) at most 37/32).
```

**New:**
```text
- (3c) **Weights.** For r = 1, ..., 5 let theta_r(x) be the number of O-triples R with capped depth r_R = r, and let
  S_x := sum over the ten O-triples of 2^(-r_R), so 32 S_x = 40 + 12 theta_1 + 4 theta_2 - 2 theta_4 - 3 theta_5. Under the
  hypothesis of DG (a) (every 4-subset Q of O has capped depth r_Q <= 4), DG (a) gives S_x <= 19/16 - 2/n_d, hence
  S_x < 19/16 (a strict necessary weakening; 2/n_d is not a pattern quantity), hence S_x <= 37/32 (32 S_x is an integer).
  So DG (a) **implies** 2 theta_4 + 3 theta_5 >= 3 + 4 theta_2 + 12 theta_1; this consequence is not equivalent to DG (a),
  since it drops the term 2/n_d. When e_d = 4, theta_5 = 0 and the raw-depth-5 triples (type T3) are counted in theta_4,
  with weight 1/16.
```

## CD12: DT-B section 0: the d-label and the i*-label can share 5; positive-support feasibility; z for the i*-entry
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B section 0 (MINOR); Claude m8; Claude m10 (letter x).
*Why:* The frozen claim that the d-label shares no odd prime with the i*-label fails when the 5-marker is on d and z = 5 (gcd 10). It is not load-bearing: certificates are checked on their positive-weight support. The row bound is now cited as Lemma RC.

**Old:**
```text
O-vertex is unmarked, and at every v in O the alpha-row and the alpha*-row satisfy the 5/6 bound (K62-CAP (C)): every
feasible y has val(y) := sum over O-neighbours u of y_u x_vu + y_(i*) x_(v i*) + 3 y_d <= 5 (units of 1/6). In G the label
of an O-neighbour u at v has {2,3,5}-type x_vu exactly; the label of i* has 2-part 2^(1 + v2 x_(v i*)) and shares no odd
prime with an O-label; the label of d has 2-part >= 8 and shares no odd prime with an O-label or with the i*-label. So an
entry 1 is isolated, entries 2 and 4 have 2-adic valuations 1 and 2, and d has valuation >= 3.
```

**New:**
```text
O-vertex is unmarked, and at every v in O the alpha-row and the alpha*-row satisfy the 5/6 bound (Lemma RC of
`K62-CAP-DT-erratum-v1.md` item CD3, case (RC-O): the alpha-row uses (C1) for alpha*, the alpha*-row uses (C1) for alpha;
both distinguished entries are 1 in G): every feasible y has val(y) := sum over O-neighbours u of y_u x_vu + y_(i*) z
+ 3 y_d <= 5 (units of 1/6), where z := x_(v i*) denotes the i*-entry of the row. In G the label of an O-neighbour u at v
is w_u x_vu (odd part w_u, 2-part x_vu); the label of i* is 2 * 3^(f* - 1) 5^(h*) w_* z, of 2-part 2^(1 + v2 z), and shares
no odd prime with an O-label; the label of d is 2^(e_d - 1) 5^(h_d) w_d, of 2-part >= 8, and shares no odd prime with an
O-label. **The d-label and the i*-label can share the prime 5:** gcd(lambda_d, lambda_(i*)) = 2^(1 + v2 z), times 5
exactly when the 5-marker is on d (h_d >= 1) and z = 5 (then the gcd is 10). So an entry 1 is isolated (its label w_u is
coprime to every other label; Sun(2)), entries 2 and 4 have 2-adic valuations 1 and 2, and d has valuation >= 3. Allowed
sets are hereditary, so a certificate y is feasible as soon as the positive-weight part {j in T : y_j > 0} of every
allowed set T has weight <= 1; no certificate below gives positive weight to both d and i*.
```

## CD13: DT-B (R4): feasibility on the positive-weight support
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B R4 remark; Claude m10 (R4 sentence).
*Why:* The frozen blanket sentence fails when h_d >= 1 and z = 5. The certificate is feasible on its positive-weight support; the values are unchanged.

**Old:**
```text
Certificate: y = 1 on entries 1, 1/2 on entries 2, y_d = 1/2, all else 0. Feasible: entries 1 are isolated; an allowed
  set with >= 3 elements contains at most one element of 2-adic valuation 1 (otherwise all its pairwise gcds through
  those two elements are 2 and, with d, no pair reaches 3: Sun(3)), so positive-weight sets are singletons, pairs
  (sum <= 1) and nothing larger.
```

**New:**
```text
Certificate: y = 1 on entries 1, 1/2 on entries 2, y_d = 1/2, all else 0 (so y_(i*) = 0). Feasible: entries 1 are
  isolated; the other positive-weight labels are the O-2-labels 2 w_u and the d-label, and any two of them have gcd
  exactly 2 (odd parts coprime; 2-parts 2, 2 and >= 8), so no allowed set contains three of them (Sun(3)); by heredity the
  positive-weight part of an allowed set is a single entry 1 or at most two half-weights (sum <= 1). (The frozen claim
  that an allowed set with >= 3 elements contains at most one element of 2-adic valuation 1 is withdrawn: when h_d >= 1
  and z = 5, {two, i*, d} is allowed with gcds 2, 2, 10; its positive-weight part {two, d} has weight 1.)
```

## CD14: DT-B (R3): blanket allowed-set sentence narrowed to the positive-weight support
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B R3 (MINOR); Claude m10.
*Why:* The frozen claim fails for {two, i*, d} when h_d >= 1 and z = 5. Feasibility uses only the positive-weight labels; the values are unchanged (z is the i*-entry).

**Old:**
```text
Certificate: y = 1 on entries 1, 1/2 on entries 2, on the 4 and on i*, y_d = 0. The i*-label then has
  2-adic valuation 1, so the elements of valuation 1 are the 2-entries and i*; an allowed set with >= 3 elements
  contains at most one of them, so positive-weight allowed sets have sum <= 1 ({two, 4, d} and {i*, 4, d} sum to 1).
  Values: (2,2,2,4): 3 + 2 + x/2; (2,2,1,4): 1 + 2 + 2 + x/2; (2,1,1,4): 2 + 1 + 2 + x/2; all >= 11/2 > 5 (x >= 1).
```

**New:**
```text
Certificate: y = 1 on entries 1, 1/2 on entries 2, on the 4 and on i*, y_d = 0. Since z = x_(v i*) is odd, the
  i*-label has 2-adic valuation 1. Besides the isolated entries 1, the positive-weight labels are the O-2-labels 2 w_u, the
  single O-4-label (2-part 4) and the i*-label; any two of them have gcd exactly 2 (at most one has 2-part 4, the others
  have 2-part 2, and the odd part of an O-label is coprime to every other label), so no allowed set contains three of them
  (Sun(3)), and by heredity the positive-weight part of every allowed set has weight <= 1. (The zero-weight d-label does
  not matter: {two, 4, d} and {i*, 4, d} are allowed with weight 1, and so is {two, i*, d}, with gcds 2, 2, 10, when
  h_d >= 1 and z = 5. The frozen blanket claim that an allowed set with >= 3 elements contains at most one element of
  valuation 1 is withdrawn; it fails in that last case.)
  Values: (2,2,2,4): 3 + 2 + z/2; (2,2,1,4): 1 + 2 + 2 + z/2; (2,1,1,4): 2 + 1 + 2 + z/2; all >= 11/2 > 5 (z >= 1).
```

## CD15: DT-B B3 proof: K4 vertex renamed q
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B B3 (MINOR); Claude m9.
*Why:* The K4 vertex named d clashed with the distinguished vertex d.

**Old:**
```text
*Proof.* A K4 on
  {a,b,c,d} gives each of its vertices degree 3 (B1), so by B2 x' = 4 on all four pairs from the fifth vertex e to the
  K4, and e has H_(x')-degree 4, contradicting B1 for x'.
```

**New:**
```text
*Proof.* A K4 on
  {a, b, c, q} gives each of its vertices degree 3 (B1), so by B2 x' = 4 on all four pairs from the fifth vertex e to the
  K4, and e has H_(x')-degree 4, contradicting B1 for x'.
```

## CD16: DT-B B4 proof: capped hypothesis of DG (a), raw depths in DG-4, renamed counts
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B B4 remarks; Claude Q4; renamed counts of CD11.
*Why:* Capped versus raw depth is now explicit, and 2a becomes 2 theta_4. The case split and the conclusion are unchanged.

**Old:**
```text
Hence the triples of depth >= 4 are exactly the 4-triangles with tau = 8 (depth 4), and no triple has
  depth 5. If all 4-subsets have depth <= 4, DG (a) gives 2a >= 3 (Part A (3c)), so H_x has two triangles, which share an
  edge by B3 (two triangles in a 5-set share a vertex): a diamond. Otherwise some 4-subset Q has depth >= 5; by DG-4 every
  e in Q has depth(Q minus e) + v2(m_e) >= 5 with depth <= 4, i.e. either Q minus e is a 4-triangle (tau = 8) and m_e >= 2, or
  m_e = 4.
```

**New:**
```text
Hence the triples of raw depth >= 4 (equivalently capped depth >= 4) are exactly the 4-triangles with tau = 8 (raw
  and capped depth 4), and no triple has raw depth 5, so theta_5(x) = 0. If all 4-subsets have capped depth <= 4 (the
  hypothesis of DG (a)), Part A (3c) gives 2 theta_4(x) >= 3, so H_x has two triangles, which share an edge by B3 (two
  triangles in a 5-set share a vertex): a diamond. Otherwise some 4-subset Q has capped depth >= 5, hence raw depth
  v2 T_x(Q) >= 5; by DG-4 (raw depths; for the family x, via the inverted configuration when x = alpha; every e in Q is
  unmarked in G) every e in Q has v2 T_x(Q minus e) + v2(m_e) >= 5 with v2 T_x(Q minus e) <= 4, i.e. either Q minus e is a
  4-triangle (tau = 8) and m_e >= 2, or
  m_e = 4.
```

## CD17: DT-B B5: diamond vertex renamed q; oriented parity statement
*File:* `K62-DT-B-v1.md`. *Disposes:* Codex DT-B B5 (MINOR); Claude m9.
*Why:* Read literally, the frozen "x'_(d i*) even" concerned the distinguished d, where x'_(d i*) = 1 in G. Rename and orient.

**Old:**
```text
- **B5 (at most one free family).** If H_x contains a diamond on {a, b, c, d} (missing the pair ab), then H_(x') lies in
  {ab, ea, eb, ec, ed} (e the fifth O-vertex), which contains a single triangle, so H_(x') contains no diamond. Hence at
  least one family y has a non-tight y-4-pair, i.e. u(y) >= 1, and by accepted K62-E3 C2 for y':
  **n_4(y') >= 2 n_1(y') + 2 >= 2 u(y) + 2 >= 4.** Moreover, if H_x contains the diamond, B2 at c and d (H_x-degree 3)
  gives x'_ce = x'_de = 4 and x'_(c i*), x'_(d i*) even.
```

**New:**
```text
- **B5 (at most one free family).** If H_x contains a diamond on {a, b, c, q} (missing the pair ab; q an O-vertex), then
  H_(x') lies in {ab, ea, eb, ec, eq} (e the fifth O-vertex), which contains a single triangle, so H_(x') contains no
  diamond. Hence at least one family y has a non-tight y-4-pair, i.e. u(y) >= 1, and by accepted K62-E3 C2 for y':
  **n_4(y') >= 2 n_1(y') + 2 >= 2 u(y) + 2 >= 4.** Moreover, if H_x contains the diamond, B2 at c and q (each of
  H_x-degree 3) gives x'_ce = x'_qe = 4, and the O-i* entries x'_(c i*), x'_(q i*) of the x'-rows at c and q are even (a
  statement about these two O-vertices only; the distinguished entry x'_(d i*) equals 1 in G).
```

## CD18: DT-B section 4: residual restated precisely; connectivity explicit
*File:* `K62-DT-B-v1.md`. *Disposes:* Claude m11; Codex DT-B section 4 (exhaustive qualitative division; connectivity); Claude m9 (rename).
*Why:* Restates what remains as a description, not an enumeration or characterization. Notes that no connectivity is assumed and that, in the (1,3)/(3,1) orientations, DG and CI' apply to different families.

**Old:**
```text
Inside G: patterns in which (i) one family x has a diamond in H_x with x'_ce = x'_de = 4 as in B5, the other family y
satisfies DG through deep triples or 4-subsets whose forced apexes (CI') use non-tight y-4-pairs, and C2 holds in both
families; or (ii) neither family has a diamond and both satisfy DG through non-tight pairs. Not yet treated: these
residual patterns; the sub-cases with a marker in O (including (alpha_(d i*), alpha*_(d i*)) = (1,3), where DG applies to
one family only and CI' needs x_(d i*) = 1); and e_d-dependent weight details (a depth-5 triple counts 1/16 when e_d = 4).
```

**New:**
```text
Inside G, the patterns not excluded by Parts A-B are the G-patterns in U62 that satisfy, in both families, (R3), (R4),
B1-B5 and the accepted K62-E3 (Lemma 2, C2), K62-SH/DG (DG with its explicit orientation and four-subset hypothesis) and
L1 constraints; Part C adds C1-C3. This describes what remains; it is not a characterization of realizable patterns and
not an enumeration of joint matrices, triangle parameters or depths. Qualitatively (an exhaustive case division): (i)
exactly one family x has a diamond in H_x, on {a, b, c, q} missing ab, with x'_ce = x'_qe = 4 as in B5, and the other
family x' has no diamond, hence (B4) a non-tight x'-4-pair; or (ii) neither family has a diamond, and then (B4) each family
has a non-tight 4-pair. Both families cannot have a diamond (B5). No connectivity of H_alpha or H_alpha* is assumed. Not
yet treated: these residual patterns; the sub-cases with a marker in O (including (alpha_(d i*), alpha*_(d i*)) in
{(1,3), (3,1)}, where Theorem DG for a family x needs x'_(d i*) = 1 while CI' for x needs x_(d i*) = 1, so they apply to
different families); and e_d-dependent weight details (a raw-depth-5 triple has capped depth 4 and weight 1/16 when
e_d = 4).
```

## CD19: DT-C C1: count names N41 ... N22
*File:* `K62-DT-C-v1.md`. *Disposes:* Claude m12.
*Why:* The names A-H clashed with the vertex set C, the vertex d, E and the sub-case G. Renaming only; the algebra is unchanged.

**Old:**
```text
The ten O-pairs carry joint values (alpha, alpha*) in J_O (K62-E3 Lemma 2, C2 sub-claim (a)). Write
A, B, C, D, E, F, G, H for the numbers of pairs with joint value (4,1), (4,2), (1,4), (2,4), (1,1), (1,2), (2,1), (2,2).
**Then 2A + 2C + 5E + 3F + 3G + H <= 6.**
*Proof.* K62-E3 C2 for alpha* (orientation alpha_(d i*) = 1) and for alpha (alpha*_(d i*) = 1): n_4(alpha) >= 2 n_1(alpha) + 2 and
n_4(alpha*) >= 2 n_1(alpha*) + 2, i.e. A + B >= 2(C + E + F) + 2 and C + D >= 2(A + E + G) + 2. Adding:
B + D >= A + C + 4E + 2F + 2G + 4; insert B + D = 10 - (A + C + E + F + G + H). QED
Consequences: E <= 1; if E = 1 then A = C = F = G = 0 and H <= 1; F + G <= 2.
```

**New:**
```text
The ten O-pairs carry joint values (alpha, alpha*) in J_O (K62-E3 Lemma 2, C2 sub-claim (a)). Write
N41, N42, N14, N24, N11, N12, N21, N22 for the numbers of pairs with joint value (4,1), (4,2), (1,4), (2,4), (1,1), (1,2),
(2,1), (2,2) (Nab counts the pairs with (alpha, alpha*) = (a, b)).
**Then 2 N41 + 2 N14 + 5 N11 + 3 N12 + 3 N21 + N22 <= 6.**
*Proof.* K62-E3 C2 for alpha* (orientation alpha_(d i*) = 1) and for alpha (alpha*_(d i*) = 1): n_4(alpha) >= 2 n_1(alpha) + 2 and
n_4(alpha*) >= 2 n_1(alpha*) + 2, i.e. N41 + N42 >= 2(N14 + N11 + N12) + 2 and N14 + N24 >= 2(N41 + N11 + N21) + 2. Adding:
N42 + N24 >= N41 + N14 + 4 N11 + 2 N12 + 2 N21 + 4; insert N42 + N24 = 10 - (N41 + N14 + N11 + N12 + N21 + N22). QED
Consequences: N11 <= 1; if N11 = 1 then N41 = N14 = N12 = N21 = 0 and N22 <= 1; N12 + N21 <= 2.
```

## CD20: DT-C C2: count names
*File:* `K62-DT-C-v1.md`. *Disposes:* Claude m12.
*Why:* Renaming only.

**Old:**
```text
With B1 (degree <= 3): A + B <= 7, C + D <= 7, A + B >= 3, C + D >= 3.
```

**New:**
```text
With B1 (degree <= 3): 3 <= N41 + N42 <= 7 and 3 <= N14 + N24 <= 7 (these sums are |H_alpha| and |H_alpha*|).
```

## CD21: DT-C C3: count names; supersedes the single item of K62-DT-C-erratum-v1
*File:* `K62-DT-C-v1.md`. *Disposes:* Claude m12; carries over K62-DT-C-erratum-v1 (B + D >= 5).
*Why:* Renaming, plus the correction of K62-DT-C-erratum-v1 carried over unchanged, with the algebraic equality clause labelled as such (Codex DT-C C3 remark). This item supersedes the only item of that erratum; read C3 from this item.

**Old:**
```text
Some family has a non-tight 4-pair, so **A + C >= 1**, and C1 leaves exactly:
- A + C = 1: E = 0, F + G <= 1, H <= 4 - 3(F + G);
- A + C = 2: E = F = G = 0, H <= 2;
- A + C = 3: E = F = G = H = 0 (so B + D = 7).
In every case at least 6 of the 10 O-pairs are tight 4-pairs ((4,2) or (2,4)), entries 1 occur on at most three
O-pairs, and (E = 0) no O-pair has alpha = alpha* = 1.
```

**New:**
```text
Some family has a non-tight 4-pair, so **N41 + N14 >= 1**, and C1 leaves exactly:
- N41 + N14 = 1: N11 = 0, N12 + N21 <= 1, N22 <= 4 - 3(N12 + N21);
- N41 + N14 = 2: N11 = N12 = N21 = 0, N22 <= 2;
- N41 + N14 = 3: N11 = N12 = N21 = N22 = 0 (so N42 + N24 = 7).
In every case at least 5 of the 10 O-pairs are tight 4-pairs ((4,2) or (2,4)): N42 + N24 >= 5 when N41 + N14 = 1
(equality only for N12 = N21 = 0, N22 = 4; an algebraic statement, not a claim that such a tuple survives the other
constraints), N42 + N24 >= 6 when N41 + N14 = 2, N42 + N24 = 7 when N41 + N14 = 3; entries 1 occur on at most three
O-pairs (N41 + N14 + N11 + N12 + N21 <= 3), and (N11 = 0) no O-pair has alpha = alpha* = 1.
```

## CD22: DT-C C4: parity statements in their orientation
*File:* `K62-DT-C-v1.md`. *Disposes:* Codex DT-C C4 (MINOR).
*Why:* The frozen phrase "B2 and (R3) force even entries at every vertex of 4-degree 1 or 3" did not say which family's i*-entry is even.

**Old:**
```text
Not yet derived: a contradiction for them (candidates for the next step: the i*-rows, where B2 and (R3) force even
entries at every vertex of 4-degree 1 or 3, together with K62-SH and the 11/12 bound when f* = 1; and the exact weights
of Theorem DG for the forced deep triples).
```

**New:**
```text
Not yet derived: a contradiction for them (candidates for the next step: the i*-entries, with the parity facts in
their orientation: a vertex v of H_x-degree 1 has x_(v i*) even ((R3) on the x-row at v); a vertex v of H_x-degree 3 has
H_(x')-degree 1 and x'_(v i*) even (B2), which says nothing about the parity of x_(v i*); when both entries at v are known
to be even, (x_(v i*), x'_(v i*)) is (2,2), (2,4) or (4,2) (E1, INV (b)); together with K62-SH and the 11/12 bound (RC-i*)
when f* = 1; and the weights of Theorem DG for the forced deep triples, used at pattern level only in the weakened forms
of K62-CAP (D)).
```

## Provenance (unchanged by this overlay)
**Sun instances applied directly** in CAP-62, DT-A, DT-B, DT-C and this overlay:
- Sun(2): isolation of entries 1; CI step 4.
- Sun(3): CI steps 2 and 5; the (R3)/(R4) certificates.
Both enter through LFC (c) or (V3). Lemma RC is LFC (a)-(d) plus index arithmetic. Its allowed-set notion is LFC (c),
which is proved via Sun(|T|) for |T| <= 6. Sun(4) enters only through accepted K62-E3 (Lemma 1, step 2).

**Sun(5) and Sun(6)** are never invoked directly. They remain in the import closure in two ways:
- through the accepted LFC/VFC package;
- through the README reduction that defines K6.2*.
These are the named computer-assisted imports; the Codex review lists their hashes as 2cf02436…5301 and efe1d849…1e29.
No closure here is free of them.

## Scope after this overlay
- **Corrections only**, as stated under Rules. Theorem DG is discharged at the scope of verdict cae455c3… (GR). Everything
  else in CAP-62, DT-A, DT-B and DT-C stays a candidate pending the parent's verdict.
- **Remarks from both reviews, recorded here** (already consistent with the texts):
  - G allows the 3-marker on i*, and its f* >= 2 branch has no (RC-i*).
  - The 5-marker on d is allowed in G; this is why CD12 matters.
  - CI/CI' for a family x need x_(d i*) = 1, and Theorem DG for x needs x'_(d i*) = 1. In a (1,3) or (3,1) orientation they
    apply to different families.
- **Still OPEN (both reviews):**
  - every marked sub-case (a marker in O), including the (1,3)/(3,1) orientations;
  - the remaining G-patterns;
  - full K6.2* with e_d >= 4, e* = 2;
  - K7 and full Sun(7).
- U62 is finite, but nothing has been enumerated, and the rule architecture is not a proof of the residue.
- No computation. No novelty, Lean or human-review claim.
