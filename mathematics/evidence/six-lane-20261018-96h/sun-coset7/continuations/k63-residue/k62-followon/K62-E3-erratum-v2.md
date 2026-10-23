# K62-E3-erratum-v2: consolidated disposition of the dual review (Codex 0/0/1, Claude 0/0/9) — no statement change

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T05:13:18-0700.
- **Overlays (frozen, unchanged):** `K62-E3-v1.md` sha256 70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372;
  `K62-E3-erratum-v1.md` sha256 095c31dcb9623cf3aa3887aef8d0a2d92708a0037b3bc3c7a8ad64b06ef3f797. Erratum v1 F1 and F3 are
  superseded by items Z11 and Z6 below, which contain them; erratum v1 F2 stands.
- **Responds to:** the parent's review packet `RUN/review/sun7-K62E3-review-freeze-v1.json` (sha256
  e37524b0fb004681e3bd0edf0060bb39ed748a6b04d5a6c093ae9891e0dbbfd8); Codex `RUN/review/sun7-K62E3-codex-v1.prompt.stdout.txt`
  (sha256 45adc810ef55c1388292a0d6b9508a63e0996998ef29baca6015fcaced751763; ACCEPT, 0 FATAL / 0 MAJOR / 1 MINOR); Claude
  `RUN/review/sun7-K62E3-claude-v1.prompt.note.md` (sha256 6329464530997e5204751d47596c220d831e5b3a8aabc2b86b4c4e7286fa392b;
  ACCEPT-WITH-FIXES, 0 / 0 / 9 MINOR m1-m9), relayed by the parent (IRC 05:01), which asked for exactly one
  consolidated overlay with verbatim Old/New blocks. RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Rule of this overlay.** Each item quotes an Old block that is an exact substring of `K62-E3-v1.md` (each was checked,
  before this file was created, to occur exactly once in the frozen file) and gives its New replacement. **No theorem,
  lemma or corollary statement changes**; every New block is a proof, citation or navigation repair.

## Disposition table
| finding | item(s) |
|---|---|
| Codex MINOR (Sun provenance) | Z1 |
| Claude m1 (L0.1 location; identity mu(U_iU_j) = alpha/g) | Z1, Z6 |
| Claude m2 (Lemma 1 notation; w-parts) | Z2 |
| Claude m3 (Lemma 2 orientation; F5 weight wording; optional compression) | Z3, Z4, Z5 |
| Claude m4 (Lemma 3 ordering, W*_m, gcd(6 w_e, T_m) = gcd(6, T_m), n_e prime to 5) | Z6 |
| Claude m5 (step 0 ordering of inversion and g_d = 1) | Z7 |
| Claude m6 (L_cU_d = L_c; F meets g_cU_c iff F lies in L_c) | Z8 |
| Claude m7 (C2 details; h_d = 0 no-5 argument; beta derivation; factor 3/2; e_d >= 3) | Z9, Z11 |
| Claude m8 (C1: Lemma 3 for every non-empty Q; e_d >= 3) | Z10 |
| Claude m9 (navigation labels; "LFC (c) only at |T| = 2 and |T| = 4") | Z12, Z1 |

**Two repairs implemented without the literal statement change suggested.**
1. m7 suggests promoting the h_d = 0 no-5 argument to "a stated Lemma 2 item 4". That would strengthen the statement
   of Lemma 2. To keep every statement unchanged, the argument is written out as sub-claim (a) inside the proof of C2
   (Z11), the only place where it is used. A promoted Lemma 2 would need a new versioned statement.
2. m8 suggests stating Lemma 3 for every non-empty Q contained in O. The statement of Lemma 3 is kept; the proof of C1
   (Z10) states that Lemma 3's proof applies verbatim to such Q and records the resulting identity there.

## Z1: Premises: L0.1 location, the identity mu(U_iU_j) = alpha/g, Sun provenance
*Disposes:* Claude m1, m9 (third clause); Codex MINOR.

**Old** (verbatim from `K62-E3-v1.md`):
```text
- **Premises (accepted, exact scopes):** R0; the K6.2* class definition with P0/P1 (old README sections 2, 5);
  old README section 1 **L0.1** (|XY| = |X||Y|/|X cap Y| for subgroups X, Y) with **Lagrange**;
  `K7-LFC-INV-erratum-v1.md` E1 (1 <= alpha <= g - 1 for disjoint cosets); **LFC (a)-(d)** and **INV (a)-(b)** with
  E6 (verdict `RUN/review/sun7-lfc-inv-parent-verdict-v1.md`, sha256
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18). Sun instances, all inside U_v through LFC (c):
  **Sun(2)** (Lemma 2), **Sun(4)** (four pieces with pairwise gcd 3). Sun(3), Sun(5), Sun(6) are not used.
```

**New:**
```text
- **Premises (accepted, exact scopes):** R0 (old README section 1); the K6.2* class definition with P0/P1 (old
  README sections 2, 5); old README section 0 ("Elementary facts used throughout") **L0.1**
  (|XY| = |X||Y|/|X cap Y| for subgroups X, Y), hence mu(XY) = [G : X cap Y] / ([G : X][G : Y]), with **Lagrange**;
  in particular mu(U_iU_j) = alpha_ij / g_ij whenever alpha_ij := [G : U_i cap U_j] / lcm(n_i, n_j) (the L0.3 identity
  of `K7-LFC-INV-erratum-v1.md` E1, here re-derived from L0.1); E1 also for the range 1 <= alpha <= g - 1 of disjoint
  cosets; **LFC (a)-(d)** and **INV (a)-(b)** with E6 (verdict `RUN/review/sun7-lfc-inv-parent-verdict-v1.md`, sha256
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18). Sun instances, all inside U_v through LFC (c):
  LFC (c) is invoked only for subfamilies T with |T| = 2 (**Sun(2)**: Lemma 2 and Corollary C2) and |T| = 4
  (**Sun(4)**: four pieces with pairwise gcd 3, in Lemma 1 and step 2). Sun(3), Sun(5) and Sun(6) are not directly or
  additionally invoked in this argument; the accepted LFC package's proof of (c) cites Sun(|T|) for |T| <= 6, so that
  provenance (including the accepted computer-assisted Sun(5) and Sun(6)) remains part of the imported package. No
  claim is made that the import closure of this file is free of Sun(5) or Sun(6).
```

## Z2: Lemma 1, proof: notation a := x_(d i*); trivial w-parts
*Disposes:* Claude m2.

**Old** (verbatim from `K62-E3-v1.md`):
```text
*Proof.* At d, lambda_c = n_c / 2 = 3^(f_c) 5^(h_c) w_c (c in O; odd) and lambda_(i*) = n_(i*) x / 4 =
2^(e* - 2) 3^(f*) 5^(h*) w_* x with x = x_(d i*) in {1, 2, 3}. Pairwise gcds: (c, c') gives 3^(min f) 5^(min h) = 3;
(c, i*) gives 3^(min(f_c, f* + v3 x)) * 5^(min(h_c, h* + v5 x)) = 3, except 9 when c = t and x = 3 (then f* = 1).
If all six labels have pairwise gcd 3, no fibre holds four pieces (LFC (c), Sun(4)), y = 1/3 on all six is
feasible, and LFC (d) gives 5/6 + x/12 < 1, i.e. x = 1. For alpha* apply this to the inverted configuration
(INV (a) with E6). QED
```

**New:**
```text
*Proof.* Write a := x_(d i*) in {1, 2, 3} for the entry (the letter x names the orientation only). At d,
lambda_c = n_c / 2 = 3^(f_c) 5^(h_c) w_c (c in O; odd) and lambda_(i*) = n_(i*) a / 4 = 2^(e* - 2) 3^(f*) 5^(h*) w_* a.
Pairwise gcds: (c, c') gives 3^(min f) 5^(min h) = 3; (c, i*) gives 3^(min(f_c, f* + v3 a)) * 5^(min(h_c, h* + v5 a)) = 3,
except 9 when c = t and a = 3 (then f* = 1). The 2-parts are trivial (lambda_c is odd), and the w-parts are trivial
(P0(b): the w's are pairwise coprime and coprime to 30, and a <= 3). If all six labels have pairwise gcd 3, no fibre
holds four pieces (LFC (c) with |T| = 4, Sun(4)), y = 1/3 on all six is feasible, and LFC (d) gives 5/6 + a/12 < 1,
i.e. a = 1. For alpha* apply this to the inverted configuration (INV (a) with E6). QED
```

## Z3: Lemma 2, proof: orientation of items 1-2 stated before item 3
*Disposes:* Claude m3 (first clause).

**Old** (verbatim from `K62-E3-v1.md`):
```text
*Proof* (orientation alpha; for alpha* use the inverted configuration).
```

**New:**
```text
*Proof* (orientation alpha; for alpha* use the inverted configuration, which is again a K6.2* configuration with
the same indices and markers, INV (a) with E6). Items 1 and 2 use only LFC at v, so they hold for every
configuration of the class and hence in both orientations before item 3 is proved; item 3 (iii) uses item 2 in
the other orientation only.
```

## Z4: Lemma 2, item 3 (i): feasibility reason
*Disposes:* Claude m3 (second clause).

**Old** (verbatim from `K62-E3-v1.md`):
```text
(sets of fives have
  sum <= 1 since |F5| <= 4)
```

**New:**
```text
(the total weight on F5
  is 1, and u' never shares a fibre with a five, by Sun(2))
```

## Z5: Lemma 2: optional compression of (ii)-(iii), as a remark
*Disposes:* Claude m3 (optional clause).

**Old** (verbatim from `K62-E3-v1.md`):
```text
Each case contradicts val < 6. QED
```

**New:**
```text
Each case contradicts val < 6. QED
(Remark, not needed: by INV (b), x_vu = 5 forces x*_vu = 1, so item 2 in the other orientation gives |F5| <= 2 < 4;
hence case (i) applies whenever F5 is non-empty. Cases (ii) and (iii) are kept; erratum v1 F2 stands.)
```

## Z6: Lemma 3, proof: ordering, W*_m, gcd(6 w_e, T_m) = gcd(6, T_m), n_e prime to 5, the identity
*Disposes:* Claude m4, m1 (second clause); supersedes erratum v1 F3 (contained here).

**Old** (verbatim from `K62-E3-v1.md`):
```text
*Proof.* beta_jk := [G : U*_j cap U*_k] / lcm(n_j, n_k) = alpha*_jk (INV), and 1 <= alpha* <= g - 1. Order O as: t,
then p (if p exists and p != t), then the remaining vertices, which have n_e = 6 w_e. With T_m the index of the
intersection of the first m groups: T_1 = n_(c_1); if two marked vertices start the order, T_2 = lcm(n_t, n_p)
alpha*_(tp). For each later e: T_(m+1) = lcm(n_e, T_m) k with k a positive integer (Lagrange), and by L0.1
k / gcd(n_e, T_m) = mu(U*_e W*_m) <= mu(U*_e U*_j) = alpha*_ej / 6 for any earlier j. By induction the prime-to-30
part of T_m is the product of the earlier w's, so gcd(n_e, T_m) = gcd(6 w_e, T_m) divides 6 and k <= alpha*_ej <= 5;
no prime > 5 enters. If h_d >= 1, no O-vertex is 5-marked and Lemma 2 gives alpha*_cc' in {1, 2, 4} on O, so the pair
factor alpha*_(c_1 c_2) and every k <= alpha*_ej <= 4 are prime to 5. Finally n_d = 2^(e_d) 5^(h_d) w_d has no 3, w_d is
prime to every w_c, and the 5-part of the gcd is trivial (h_d = 0, or 5 does not divide T*_O). QED
```

**New:**
```text
*Proof.* [G : U*_j] = n_j, and beta_jk := [G : U*_j cap U*_k] / lcm(n_j, n_k) = alpha*_jk by the definition of alpha*
(INV), with 1 <= alpha*_jk <= g_jk - alpha_jk <= g_jk - 1 (INV (b)); by L0.1, mu(U*_jU*_k) = [G : U*_j cap U*_k] /
(n_j n_k) = alpha*_jk / g_jk. Order O as follows: first the marked vertices of O, namely t (if t exists) and then p (if
p exists and p != t), so that there is one initial marked vertex if exactly one of t, p lies in O or if t = p, two if
t != p both lie in O, and none if no vertex of O is marked; then the unmarked vertices of O (n_e = 6 w_e), in any
order. Write c_1, ..., c_5 for this order, W*_m := U*_(c_1) cap ... cap U*_(c_m) and T_m := [G : W*_m], so that
T_5 = T*_O. Induction claim: the prime-to-30 part of T_m is w_(c_1) ... w_(c_m). Base: T_1 = n_(c_1); if two marked
vertices start the order, T_2 = lcm(n_t, n_p) alpha*_(tp) with alpha*_(tp) <= 5. Step, for an unmarked e = c_(m+1):
T_(m+1) = lcm(n_e, T_m) k with k a positive integer (Lagrange: n_e and T_m divide T_(m+1)), and by L0.1
k / gcd(n_e, T_m) = T_(m+1) / (n_e T_m) = mu(U*_e W*_m) <= mu(U*_e U*_j) = alpha*_ej / 6 for any earlier j (W*_m lies
in U*_j). By the induction claim w_e is coprime to T_m, so gcd(n_e, T_m) = gcd(6 w_e, T_m) = gcd(6, T_m) divides 6, and
k <= alpha*_ej <= 5; no prime > 5 enters, which proves the claim for m + 1. If h_d >= 1: no O-vertex is 5-marked, so p
does not exist and the order starts with t (if t exists) or with an unmarked vertex; T_1 = n_(c_1) has no factor 5,
every n_e (e in O) is prime to 5 (h_e = 0), and every later k satisfies k <= alpha*_ej <= 4, because alpha*_ej lies in
{1, 2, 4} on O by Lemma 2 with x = alpha*; hence 5 divides no T_m. Finally n_d = 2^(e_d) 5^(h_d) w_d has no 3, w_d is
prime to every w_c, and the 5-part of the gcd is trivial (h_d = 0, or 5 does not divide T*_O). QED
```

## Z7: Theorem, step 0: inversion first, then g_d = 1; what inversion preserves
*Disposes:* Claude m5.

**Old** (verbatim from `K62-E3-v1.md`):
```text
By Lemma 1 and INV (a) with E6 (the inverted configuration is again K6.2* with the same indices and markers, and its
alpha is our alpha*), we may assume **alpha_(d i*) = 1**. Normalise g_d = 1. Fibres are the n_d left cosets of U_d;
for a fibre F let S_F be the set of j != d with g_jU_j cap F non-empty.
```

**New:**
```text
By Lemma 1, alpha_(d i*) = 1 or alpha*_(d i*) = 1. In the second case replace the configuration by its inverted
configuration (INV (a) with E6): its cosets g_j^-1 U*_j = (g_jU_j)^-1 are pairwise disjoint and have the same labelled
index tuple, so it is again of class K6.2* with the same distinguished vertices d and i*, the same O, the same marked
vertices t, p and the same exponents (all of these are read off the labelled index tuple); its alpha-matrix is our
alpha* by definition, and since inverting twice returns the original configuration, its alpha*-matrix is our alpha.
The conclusion (e_d >= 4) depends only on the index tuple. So we may assume **alpha_(d i*) = 1**. Only after this
possible inversion, left-translate every coset by g_d^-1, so that g_d = 1 (indices, intersection indices and
disjointness are unchanged; all U*_j are conjugated by the same element g_d^-1, so [G : W*_O] is unchanged). Fibres
are the n_d left cosets of U_d; for a fibre F let S_F be the set of j != d with g_jU_j cap F non-empty.
```

## Z8: Theorem, step 3: L_cU_d = L_c; F meets g_cU_c iff F lies in L_c
*Disposes:* Claude m6.

**Old** (verbatim from `K62-E3-v1.md`):
```text
3. *Light fibres.* The set W*_O U_d is a union of left U_d-cosets, contains U_d, and meets no
   L_c := g_cU_cU_d (c in O): if w u lies in L_c with w in W*_O, u in U_d, then w = g_c a g_c^-1 (a in U_c) lies in
   g_cU_cU_d, so a g_c^-1 lies in U_cU_d, so g_c^-1 lies in U_cU_d, i.e. g_c lies in U_dU_c, i.e. g_cU_c meets
   U_d = g_dU_d, contradicting disjointness. Hence every fibre F inside W*_O U_d has S_F contained in {i*}, and
   S_(U_d) is empty. Let M be the number of fibres inside W*_O U_d (M >= 1). Then
   11 n_d / 4 <= 3 (n_d - M) + (M - 1), i.e. **M < n_d / 8**.
```

**New:**
```text
3. *Light fibres.* For c in O let L_c := g_cU_cU_d; it is the union of the fibres that meet g_cU_c, so L_cU_d = L_c,
   and a fibre F meets g_cU_c if and only if F is contained in L_c. The set W*_O U_d is a union of left U_d-cosets,
   contains U_d, and meets no L_c: if w u lies in L_c with w in W*_O, u in U_d, then w = (w u) u^-1 lies in
   L_cU_d = L_c = g_cU_cU_d; writing w = g_c a g_c^-1 (a in U_c), a g_c^-1 lies in U_cU_d, so g_c^-1 lies in
   a^-1 U_cU_d = U_cU_d, i.e. g_c lies in U_dU_c, i.e. g_cU_c meets U_d = g_dU_d, contradicting disjointness. Hence a
   fibre F contained in W*_O U_d is contained in no L_c, so it meets no g_cU_c (c in O): S_F is contained in {i*}; and
   S_(U_d) is empty (LFC (b)). Let M be the number of fibres contained in W*_O U_d (M >= 1, since U_d is one of them).
   Then 11 n_d / 4 <= 3 (n_d - M) + (M - 1), i.e. M <= n_d / 8 - 1/2, so **M < n_d / 8**.
```

## Z9: Section 5 preamble: derivations of the two beta relations written out
*Disposes:* Claude m7 (second clause).

**Old** (verbatim from `K62-E3-v1.md`):
```text
For a fibre F let B(F) := O minus S_F. Then sum_F |B(F)| = 5 n_d / 2, |B(F)| >= 2 + [i* in S_F], and B(F) contains Q
whenever F lies in W*_Q U_d (W*_Q = intersection of U*_c, c in Q; step 3 for Q in place of O). Writing
beta_k n_d for the number of fibres with |B(F)| = k (k = 2, ..., 5): beta_3 + 2 beta_4 + 3 beta_5 = 1/2 and
beta_4 + 2 beta_5 <= 1/4 - 1/n_d (the n_d/4 fibres met by g_(i*)U_(i*) have |B| >= 3, and U_d is another fibre
with |B| = 5).
```

**New:**
```text
For a fibre F let B(F) := O minus S_F. Then sum_F |B(F)| = 5 n_d - sum_F |S_F cap O| = 5 n_d - 5 n_d / 2 = 5 n_d / 2
(step 1); |B(F)| >= 2 + [i* in S_F] for F != U_d (step 2: |S_F| <= 3), and |B(U_d)| = 5; and B(F) contains Q whenever F
is contained in W*_Q U_d (W*_Q = intersection of U*_c, c in Q; the argument of step 3 with Q in place of O). Write
beta_k n_d for the number of fibres with |B(F)| = k (k = 2, ..., 5), so that beta_2 + beta_3 + beta_4 + beta_5 = 1.
Subtracting 2 n_d from sum_F |B(F)| gives **beta_3 + 2 beta_4 + 3 beta_5 = 1/2**. The n_d / 4 fibres met by
g_(i*)U_(i*) (LFC (b)) have |B| >= 3, and U_d is a further fibre (not met by g_(i*)U_(i*), LFC (b)) with |B| = 5, so
beta_3 + beta_4 + beta_5 >= 1/4 + 1/n_d; subtracting, **beta_4 + 2 beta_5 <= 1/4 - 1/n_d**.
```

## Z10: Corollary C1: Lemma 3's proof for every non-empty Q; dependence on e_d >= 3
*Disposes:* Claude m8.

**Old** (verbatim from `K62-E3-v1.md`):
```text
- **(C1)** For every 4-subset Q of O: v2([G : W*_Q]) >= 3 (fibres in W*_Q U_d number at most
  (beta_4 + beta_5) n_d < n_d / 4; granularity as in step 4; the chain of Lemma 3 applies to Q).
```

**New:**
```text
- **(C1)** For every 4-subset Q of O: v2([G : W*_Q]) >= 3. (Every fibre contained in W*_Q U_d has Q contained in
  B(F), so |B(F)| >= 4; these fibres therefore number at most (beta_4 + beta_5) n_d <= (beta_4 + 2 beta_5) n_d
  <= n_d / 4 - 1 < n_d / 4. By L0.1 and Lagrange their number is n_d mu(U_d W*_Q) >= n_d / gcd(n_d, [G : W*_Q]). The
  proof of Lemma 3 applies verbatim to every non-empty Q contained in O in place of O (marked vertices of Q first, then
  its unmarked vertices), giving gcd(n_d, [G : W*_Q]) = 2^(min(e_d, v2([G : W*_Q]))). Hence
  min(e_d, v2([G : W*_Q])) >= 3; since e_d >= 4 by the Theorem (e_d >= 3 suffices here), v2([G : W*_Q]) >= 3.)
```

## Z11: Corollary C2: full proof written out (no-5 sub-claim, pair granularity, double count, e_d >= 3)
*Disposes:* Claude m7 (first, third, fourth clauses); supersedes erratum v1 F1 (contained here).

**Old** (verbatim from `K62-E3-v1.md`):
```text
- **(C2)** The number of pairs {c, c'} of O with alpha*_cc' = k, written n_k, satisfies **n_4 >= 2 n_1 + 2**.
  *Proof.* The fibres containing (U*_c cap U*_c')U_d number at least n_d / 2^(1 + v2(alpha*_cc')) (granularity:
  [G : U*_c cap U*_c'] = lcm(n_c, n_c') alpha*_cc', alpha* in {1, 2, 4} by Lemma 2 and the no-5 argument of its first
  item when h_d = 0 (a five u and d would be isolated: val = 5 + 3), e_d >= 4). Summing over the ten pairs:
  sum_k C(k, 2) beta_k = 2 + beta_4 + 3 beta_5 <= 19/8 - 3/(2 n_d) < 19/8, so 4 n_1 + 2 n_2 + n_4 <= 18 with
  n_1 + n_2 + n_4 = 10.
```

**New:**
```text
- **(C2)** The number of pairs {c, c'} of O with alpha*_cc' = k, written n_k, satisfies **n_4 >= 2 n_1 + 2**.
  *Proof.* (a) *Every O-O entry of alpha* lies in {1, 2, 4}.* Lemma 2 excludes 3, and excludes 5 when h_d >= 1. If
  h_d = 0 and x_vu = 5 for some v, u in O and x in {alpha, alpha*}, then lambda_u = 3^(f_u - 1) 5^(h_u + 1) w_u is odd and
  coprime to lambda_d = 2^(e_d - 1) w_d, so u and d never share a fibre (LFC (c) with |T| = 2, Sun(2)); y_u = y_d = 1
  (all else 0) is feasible and val = 5 + 3 = 8, contradicting LFC (d) at v. (This sub-claim is proved and used here
  only; the statement of Lemma 2 is unchanged.)
  (b) *Pair granularity.* For c != c' in O put H := U*_c cap U*_c', so [G : H] = lcm(n_c, n_c') alpha*_cc'. The fibres
  contained in HU_d (a union of left U_d-cosets) number n_d mu(U_dH) >= n_d / gcd(n_d, [G : H]) (L0.1, Lagrange), and
  each of them has {c, c'} contained in B(F) (the argument of step 3 with Q = {c, c'}). Here
  gcd(n_d, [G : H]) = 2^(min(e_d, 1 + v2(alpha*_cc'))) = 2^(1 + v2(alpha*_cc')), because e_d >= 3 (true by the Theorem)
  and v2(alpha*_cc') <= 2 by (a); the 3-part is trivial (n_d has no 3), the 5-part is trivial (if h_d >= 1 then
  h_c = h_c' = 0 and alpha*_cc' has no factor 5 by (a)), and the w-part is trivial (P0(b)). So these fibres number at
  least n_d / 2, n_d / 4, n_d / 8 for alpha*_cc' = 1, 2, 4 respectively.
  (c) *Double count.* Counting pairs ({c, c'}, F) with {c, c'} contained in B(F):
  n_d (n_1 / 2 + n_2 / 4 + n_4 / 8) <= sum_F C(|B(F)|, 2) = n_d sum_k C(k, 2) beta_k = n_d (1 + 2 beta_3 + 5 beta_4 + 9 beta_5)
  = n_d (2 + beta_4 + 3 beta_5), using beta_2 = 1 - beta_3 - beta_4 - beta_5 and beta_3 + 2 beta_4 + 3 beta_5 = 1/2. Since
  beta_4 >= 0, beta_4 + 3 beta_5 <= (3/2)(beta_4 + 2 beta_5) <= 3/8 - 3/(2 n_d). Hence n_1 / 2 + n_2 / 4 + n_4 / 8 < 19/8,
  i.e. 4 n_1 + 2 n_2 + n_4 < 19, so 4 n_1 + 2 n_2 + n_4 <= 18 (integers). With n_1 + n_2 + n_4 = 10 (by (a)),
  substituting n_2 = 10 - n_1 - n_4 gives 2 n_1 - n_4 <= -2, i.e. n_4 >= 2 n_1 + 2.
```

## Z12: Scope: navigation labels
*Disposes:* Claude m9 (first, second clauses).

**Old** (verbatim from `K62-E3-v1.md`):
```text
- **Excluded:** every K6.2* configuration with e_d = 2 or e_d = 3, any position of the 3- and 5-markers, arbitrary
  exponents. This contains the accepted K62-A (e_d = 2 with the 3-marker absent or on i*) and the candidates
  `K62-FG-v1.md` Theorem R2-11 and `K62-R2-v1.md` (R2: e_d = 2 with the 3-marker in O), which it supersedes; those
  files remain frozen and are not needed.
- **Remaining K6.2*:** e_d >= 4, e* = 2 (3-marker on i*, on a vertex of O, or absent; any 5-marker). See
  `K62-STATUS-v2.md` (to be frozen) for the exact obstruction there.
```

**New:**
```text
- **Excluded:** every K6.2* configuration with e_d = 2 or e_d = 3, any position of the 3- and 5-markers, arbitrary
  exponents. (Navigation only, not used in any proof: as a set inclusion this class contains the accepted K62-A
  (e_d = 2 with the 3-marker absent or on i*) and the candidates `K62-FG-v1.md` Theorem R2-11 and `K62-R2-v1.md`
  (R2: e_d = 2 with the 3-marker in O); no statement of those files is used here, and they remain frozen.)
- **Remaining K6.2*:** e_d >= 4, e* = 2 (3-marker on i*, on a vertex of O, or absent; any 5-marker). (Navigation only:
  `K62-STATUS-v2.md`, frozen after this file, sha256 696a627f14453655578d9444bdbf0bb20ce59ec1da09bff08d11fb0f695da7fd,
  describes the state there; it is not part of this file's claims.)
```

## Unchanged
The statement of Theorem K62-E3; the statements of Lemmas 1, 2 and 3 and of Corollaries C1 and C2; steps 1, 2 and 4
of the proof; the verification-boundary list and the mutation controls of section 6; erratum v1 F2. No new claim is
made. Full K6.2* (e_d >= 4, e* = 2), K7 and full Sun(7) remain OPEN.

## Out-of-scope note (reported to the parent; not repaired here)
The same README citation slip occurs in `../K63-RES-erratum-v2.md` X1 (an accepted file) and in `K62-FG-erratum-v2.md`
Y1: both cite L0.1 as "old README section 1", but L0.1 is in old README section 0 ("Elementary facts used throughout");
section 1 is R0. It is a citation slip with no mathematical effect; its disposition is the parent's.

No novelty, priority, Lean or human-review claim.
