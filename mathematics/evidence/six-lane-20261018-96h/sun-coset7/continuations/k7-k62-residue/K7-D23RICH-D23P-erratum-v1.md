# K7-D23RICH-D23P-erratum-v1: consolidated MINOR repairs to K7-D23-RICH (on top of erratum-1) and K7-D23P (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:23:46-0700.
- **Owner:** Sun7K62Successor (continuation `k7-k62-residue`). Written overlay; no computation (the Old texts below were
  copied verbatim from the frozen files, and each occurs exactly once in its file).
- **Overlays (frozen byte-identical, not modified):**
  - `K7-D23-RICH-v1.md` sha256 ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3, with
    `K7-D23-RICH-erratum-v1.md` sha256 8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69 (erratum-1; its
    R-1 replacement of the last branch of NO5 (a) stays in force; its R-2 sentence is amended by RF9 below);
  - `K7-D23P-v1.md` sha256 89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880.
- **Source findings:** review freeze `RUN/review/sun7-D23RICH-D23P-review-freeze-v1.json` (sha256
  c1e127a48027dc5b3713d7fd9a4520d7d51c76112f0316de21795a4d36bb82ed).
  - Claude (opus-5-5) `RUN/review/sun7-D23RICH-D23P-claude-v1.prompt.note.md` (sha256
    1106bbb5e99ae270f7505d2c7986285370fabd7cf59e77d827d311448bf09359): ACCEPT-WITH-FIXES for both, 0 FATAL / 0 MAJOR;
    RICH MINOR RF1-RF9, D23P MINOR PF1-PF3. All twelve are applied below.
  - Codex (gpt-6.1-sol) `RUN/review/sun7-D23RICH-D23P-codex-v1.prompt.stdout.txt` (sha256
    d158f82613d7236ac1cb329618ace098faacb4896f2b9a349c5ec59e406f93ea): ACCEPT for both, 0/0/0; no repair requested (its
    remark that the R-1 replacement is essential is already met by erratum-1).
- **No statement change.** Theorem K7-D23-RICH, Theorem K7-D23P and every previously stated lemma conclusion are
  unchanged. The only restated lemma is FG7 (RF1): its previous statement is retained verbatim as a special case, and
  the added chain form (a) records what the unchanged proof establishes (and what LZ already used).
- RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

## Disposition

| finding | items | file(s) |
|---|---|---|
| RF1 (Lemma FG7: chain form for every index set (used by LZ) and the k-bound against every earlier vertex) | 1a, 1b, 1c | `K7-D23-RICH-v1.md` |
| RF2 (Corollary 5/6: weight of a fibre, equality clause, normalisation and the alpha* intersection) | 2a, 2b, 2c, 2d | `K7-D23-RICH-v1.md` |
| RF3 (Lemma NO5 for alpha*: explicit role swap) | 3 | `K7-D23-RICH-v1.md` |
| RF4 (Lemma R3: justification of the standard weights at an apex with marked neighbours) | 4 | `K7-D23-RICH-v1.md` |
| RF5 (Lemma R3: unproved optimality remark removed; survivors are local-test survivors only) | 5a, 5b | `K7-D23-RICH-v1.md` |
| RF6 (Sections 6 and 9: navigation remark and unverified remark marked as such) | 6a, 6b | `K7-D23-RICH-v1.md` |
| RF7 (Lemma TZ: citations in (i), cut argument in (iii)) | 7a, 7b, 7c | `K7-D23-RICH-v1.md` |
| RF8 (Lemma LZ: LFC (b), D23-MIX, scope of the L_j argument, FG7 (a)) | 8a, 8b, 8c | `K7-D23-RICH-v1.md` |
| RF9 (Import accounting: direct versus transitive) | 9a, 9b, 9c | `K7-D23-RICH-erratum-v1.md` (R-2), `K7-D23-RICH-v1.md` |
| PF1 (ROW-2 transfer to the marked apex z: gcd matrix, H35 not read, K2, wording as Z2 G2 / NO4 X-6) | P1 | `K7-D23P-v1.md` |
| PF2 (M1: exact triangle tables, the reason x = 5 dies, normalisation moved before the F7 step) | P2a, P2b, P2c, P2d | `K7-D23P-v1.md` |
| PF3 (Section 0: L0.3 listed; transitive Sun(5)/Sun(6) closure stated) | P3a, P3b | `K7-D23P-v1.md` |

## Replacements (verbatim Old -> New)

Each item: in the named file and place, replace the Old text (exact bytes, line breaks included) by the New text.

### RF1: Lemma FG7: chain form for every index set (used by LZ) and the k-bound against every earlier vertex

**Item 1a.** `K7-D23-RICH-v1.md`, section 1, statement of Lemma FG7. Old:

```text
**Lemma FG7.** Let u in W, N := V \ {u}, and let (V_j)_(j in N) be subgroups of G with [G : V_j] = n_j and
beta_jk := [G : V_j cap V_k] / lcm(n_j, n_k) <= 5 for all j != k in N. For non-empty Q subset N put
T_Q := [G : intersection of V_j (j in Q)]. Then the prime-to-30 part of T_Q is the product of the w_j (j in Q);
hence gcd(n_u, T_Q) divides 6.
```

New:

```text
**Lemma FG7.** Let N subset V and let (V_j)_(j in N) be subgroups of G with [G : V_j] = n_j and
beta_jk := [G : V_j cap V_k] / lcm(n_j, n_k) <= 5 for all j != k in N. For non-empty Q subset N put
T_Q := [G : intersection of V_j (j in Q)]. Order Q marked-first: z (if in Q), then t (if in Q), then the unmarked
vertices of Q in any order j_1, j_2, ...; W_m is the intersection of the first m groups and T_m := [G : W_m].
(a) (Chain form.) T_1 = n_(j_1); if z and t are both in Q, T_2 = lcm(n_z, n_t) beta_zt. At every further vertex e
(it is unmarked), T_(m+1) = lcm(n_e, T_m) k with gcd(n_e, T_m) = 6 and k a positive integer such that k <= beta_(e j)
for every earlier j (so k <= 5); if e is the second vertex, k = beta_(j_1 e) exactly. Hence the prime-to-30 part of
T_Q is the product of the w_j (j in Q).
(b) If u in W \ Q, then gcd(n_u, T_Q) divides 6.
The statement used before this erratum is the case u in W, N := V \ {u}: for non-empty Q subset N the prime-to-30
part of T_Q is the product of the w_j (j in Q); hence gcd(n_u, T_Q) divides 6.
```

**Item 1b.** `K7-D23-RICH-v1.md`, section 1, proof of FG7, step. Old:

```text
and V_e W_m subset V_e V_(j_1), whose measure is beta_(e j_1)/6 <= 5/6. By induction w_e is coprime to T_m, and
6 | T_m, so gcd(n_e, T_m) = 6 and k <= 5.
```

New:

```text
and V_e W_m subset V_e V_j for every earlier j (as W_m subset V_j), whose measure is
beta_(e j)/gcd(n_e, n_j) = beta_(e j)/6 <= 5/6 (L0.1). By induction w_e is coprime to T_m, and 6 | T_m, so
gcd(n_e, T_m) = 6 and k <= beta_(e j) <= 5 for every earlier j.
```

**Item 1c.** `K7-D23-RICH-v1.md`, section 1, proof of FG7, last sentence. Old:

```text
Finally gcd(n_u, T_Q) = gcd(6 w_u, T_Q) divides 6 because w_u is coprime to every other w. QED
```

New:

```text
This proves (a). (b): gcd(n_u, T_Q) = gcd(6 w_u, T_Q) divides 6, because u is not in Q, so by (a) w_u is coprime
to T_Q (the w's are pairwise coprime). QED
```

### RF2: Corollary 5/6: weight of a fibre, equality clause, normalisation and the alpha* intersection

**Item 2a.** `K7-D23-RICH-v1.md`, section 1, statement of Corollary 5/6. Old:

```text
**Corollary 5/6.** For u in W, x in {alpha, alpha*} and every feasible y at u: **val(y) <= 5**. If val(y) = 5, then
every left fibre at u (orientation x) that meets one of the cosets carries weight exactly 1.
```

New:

```text
**Corollary 5/6.** For u in W, x in {alpha, alpha*} and every feasible y at u: **val(y) <= 5**. For a fibre C at u
in orientation x (a left coset of the subgroup of u, other than the coset of u itself, in the configuration if
x = alpha and in the inverted configuration if x = alpha*) let S_C be the set of j != u whose coset meets C, and call
sum_(j in S_C) y_j the weight of C. If val(y) = 5, then sum_(j in S_C) y_j = 1 whenever S_C is non-empty, i.e. every
left fibre at u (orientation x) that meets one of the cosets carries weight exactly 1.
```

**Item 2b.** `K7-D23-RICH-v1.md`, section 1, proof of Corollary 5/6, first sentences. Old:

```text
*Proof.* x = alpha. Normalise g_u = 1 (left translation changes nothing used). Put W* := intersection of the
g_jU_jg_j^-1 (j in N).
```

New:

```text
*Proof.* Put N := V \ {u}. x = alpha. Normalise g_u = 1 (left translation by g_u^-1 changes nothing used: it
replaces each g_j by g_u^-1 g_j, hence each g_jU_jg_j^-1 by its conjugate under g_u^-1, so it conjugates W* below
without changing its index). Put W* := intersection of the g_jU_jg_j^-1 (j in N).
```

**Item 2c.** `K7-D23-RICH-v1.md`, section 1, proof of Corollary 5/6, FG7 citation. Old:

```text
By G0 and FG7 (with
V_j = g_jU_jg_j^-1, Q = N)
```

New:

```text
By G0 and FG7 (b) (with N = Q = V \ {u}, V_j = g_jU_jg_j^-1, beta = alpha*)
```

**Item 2d.** `K7-D23-RICH-v1.md`, section 1, proof of Corollary 5/6, end. Old:

```text
<= 5 n_u/6. If
val(y) = 5, all inequalities are equalities, so every fibre outside W*U_u (in particular every fibre meeting a coset)
has weight exactly 1. x = alpha*: the same for the inverted configuration (INV (a), E6). QED
```

New:

```text
<= 5 n_u/6. If val(y) = 5, all inequalities are equalities: sum_(j in S_C) y_j = 1 whenever S_C is non-empty
(moreover M = n_u/6, and every fibre outside W*U_u has S_C non-empty). x = alpha*: the same for the inverted
configuration (INV (a), E6), whose subgroups are U*_j = g_jU_jg_j^-1 with representatives g*_j = g_j^-1; its W* is the
intersection of the g*_jU*_jg*_j^-1 = U_j (j in N), conjugated by the normalising translation (index unchanged), and
FG7 (b) is applied with V_j = U_j, beta = alpha. QED
```

### RF3: Lemma NO5 for alpha*: explicit role swap

**Item 3.** `K7-D23-RICH-v1.md`, section 2, last sentence of the proof of NO5. Old:

```text
Each case contradicts Corollary 5/6 or LFC (d). The inverted configuration is in the same setting (E6). QED
```

New:

```text
Each case contradicts Corollary 5/6 or LFC (d). The inverted configuration is in the same setting (E6), and the
alpha*-statement is the alpha-statement for it, with the roles swapped as follows. In (a) the labels at u are those of
the inverted configuration, c is replaced by c* := alpha*_uz in {1,2,3} (D23-MIX for alpha*), and the contradictions
are with LFC (d) for the inverted configuration; in the last branch of (a) (erratum-1 R-1) the inverse row used is the
alpha-row at u of the original configuration (alpha** = alpha), with c = alpha_uz in {1,2,3} (D23-MIX for alpha), and
the contradiction is with LFC (d) of the original configuration. In (b) the contradictions are with Corollary 5/6 for
x = alpha* or with LFC (d) for the inverted configuration. QED
```

### RF4: Lemma R3: justification of the standard weights at an apex with marked neighbours

**Item 4.** `K7-D23-RICH-v1.md`, section 3, first sentence of the proof of R3. Old:

```text
*Proof.* Every listed weight vector is feasible by the stated reasons; "standard weights" are those of the ROW-U class
analysis on unmarked neighbours (E8: N such neighbours with entries in {1,2,4} contribute >= min(N, 4)).
```

New:

```text
*Proof.* Every listed weight vector is feasible by the stated reasons; "standard weights" are those of the ROW-U class
analysis on unmarked neighbours (E8: N such neighbours with entries in {1,2,4} contribute >= min(N, 4)). They are used
only in the two cases k3 = 1, on the set B of the three W-neighbours with entries in {1,2,4}, in the subset form
accepted in `K7-LFC-INV-erratum-v1.md` E8 (sha256 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5;
LFC verdict item 3, sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18) and in
`K63-D-erratum-v2.md` H5 (sha256 891567ee25fae8e109fca702eeac616e26243ede0e535e8c0e30c798d8da147a; accepted by
`RUN/review/sun7-K63DE-K735-parent-verdict-v1.md`, sha256 1a1c639093dd334cb404a8216ca70a839ea85454978c9fdf354cc5bc577a3919).
This is legitimate at u: among unmarked neighbours the label gcds equal the gcds of the entries (the w's never enter a
gcd); every vertex outside B carries weight 0 except the single W-three a (y_a = 1), whose label 3 w_a is coprime to
every label of B, so no allowed set contains a and an element of B (Sun(2)); and allowedness is hereditary, so an
allowed set through weight-0 elements has the weight of its positive part. With |B| = 3 the branch b >= 4 of the class
analysis (the only place where Sun(5) bounds a set of fours) is vacuous, and allowedness inside B is decided by Sun(2)
and Sun(3).
```

### RF5: Lemma R3: unproved optimality remark removed; survivors are local-test survivors only

**Item 5a.** `K7-D23-RICH-v1.md`, section 3, (2), case k3 = 2, e even, (1,1). Old:

```text
(1,1): R3' contributes at most max(3, e) and the
  ones 2; e = 4: y_t = 1, ones 1: val = 6; e = 2: survivor **S3**.
```

New:

```text
(1,1): e = 4: y_t = 1, y = 1 on both ones and y = 0 on the threes and z (R3' weighs 1; the ones are isolated):
  val = 4 + 2 = 6; e = 2: survivor **S3**.
```

**Item 5b.** `K7-D23-RICH-v1.md`, section 3, (3), heading sentence. Old:

```text
(3) **The survivors and their weights** (all with c = 3, e = 2; gcd(z,t) = 6):
```

New:

```text
(3) **The survivors and their weights** (all with c = 3, e = 2; gcd(z,t) = 6). S1-S4 are survivors of this local
test only: they are not claimed to be realisable, and the displayed weights are not claimed to be LP-optimal; only
their feasibility, their value 5 and the stated property of the sets through t are used:
```

### RF6: Sections 6 and 9: navigation remark and unverified remark marked as such

**Item 6a.** `K7-D23-RICH-v1.md`, section 6, paragraph after the proof of the theorem. Old:

```text
The abstract pattern of `K7-D23-obstruction-v1.md` (sha256 9a6d1e609c3ed95e2dc77ffcb5fada5b35b1beded4593662ce4e7396fc514863;
navigation only) has T* = W = W3 and is therefore not realisable.
```

New:

```text
Navigation only: the abstract pattern of `K7-D23-obstruction-v1.md` (sha256
9a6d1e609c3ed95e2dc77ffcb5fada5b35b1beded4593662ce4e7396fc514863; unreviewed and not embedded here) is not checked in
this file. If it has T* subset W3 or T subset W3*, it is not realised by any configuration. No other local pattern is
excluded.
```

**Item 6b.** `K7-D23-RICH-v1.md`, section 9, residue bullet. Old:

```text
Rows without a W-three (W-entries in {1,2,4}) are NOT classified here; several of them pass
  Corollary 5/6 while putting zero weight on z in every optimal y, so Lemma TR cannot be invoked for them.
```

New:

```text
Rows without a W-three (W-entries in {1,2,4}) are NOT classified here, and Lemma TR is not invoked for them.
  (Unverified, non-load-bearing remark, supported by no proof and no finite program: several of them appear to pass
  Corollary 5/6 with zero weight on z in every optimal y.)
```

### RF7: Lemma TZ: citations in (i), cut argument in (iii)

**Item 7a.** `K7-D23-RICH-v1.md`, section 7, proof of (i), definition of s and x. Old:

```text
With s := alpha_zv in
{1,2} and x := alpha_uv (<= 4 by NO5):
```

New:

```text
With s := alpha_zv in {1,2} (D23-MIX; v is not in T) and x := alpha_uv (x != 5 by NO5, so x <= 4):
```

**Item 7b.** `K7-D23-RICH-v1.md`, section 7, proof of (i), end. Old:

```text
x = 1 or 2 gives
tau_max <= 2s < 3s. So x in {3, 4}.
```

New:

```text
x = 1 or 2 gives tau_max <= 2s < 3s. So x in {3, 4}. For the alpha*-version the same triangle is used in the
inverted configuration (L1 applied to it as in `K7-Z2-erratum-v1.md` G5; same g, gamma and ell's by E6), with
s = alpha*_zv in {1,2} (D23-MIX for alpha*) and x = alpha*_uv != 5 (NO5 for alpha*).
```

**Item 7c.** `K7-D23-RICH-v1.md`, section 7, proof of (iii). Old:

```text
(iii) Otherwise (ii) holds for alpha and for alpha*: alpha = 4 on all pairs of
T x (W\T) and alpha* = 4 on all pairs of T* x (W\T*). No pair has alpha = alpha* = 4 (INV). The complete bipartite
graph on T, W \ T (both non-empty) is connected and spans W, so none of its edges crosses (T*, W \ T*) only if T* is
empty or W; |T*| >= 3 gives T* = W, a contradiction. QED
```

New:

```text
(iii) Suppose T != W and T* != W. Then (ii) holds for alpha and for alpha*: alpha = 4 on all pairs of T x (W\T),
and alpha* = 4 on all pairs of T* x (W\T*). No pair has alpha = alpha* = 4 (INV (b): alpha + alpha* <= 6). Hence no
edge of the complete bipartite graph K(T, W\T) crosses the cut (T*, W\T*): such an edge would have alpha = 4 (it lies
in T x (W\T)) and alpha* = 4 (it lies in T* x (W\T*)). Both T and W\T are non-empty (|T| >= 3 and T != W), so
K(T, W\T) is connected and spans W; a connected spanning graph with no edge crossing the cut forces T* = empty or
T* = W. |T*| >= 3 (D23-MIX) excludes the first and T* != W the second: a contradiction. QED
```

### RF8: Lemma LZ: LFC (b), D23-MIX, scope of the L_j argument, FG7 (a)

**Item 8a.** `K7-D23-RICH-v1.md`, section 8, first sentences of the proof. Old:

```text
*Proof.* Normalise g_z = 1 and let W* be the intersection above. As in Corollary 5/6, W*U_z is a union of left
U_z-cosets containing U_z and meeting no g_uU_uU_z (u in W); its fibres carry at most the piece of t.
```

New:

```text
*Proof.* Normalise g_z = 1 and let W* be the intersection above; s in {1,2} by D23-MIX. The L_j argument of the
proof of Corollary 5/6 is rerun here only for j in W (W* is intersected over W only): W*U_z is a union of left
U_z-cosets containing U_z and meeting no g_uU_uU_z (u in W), so its fibres carry no W-piece, but they may carry the
piece of t.
```

**Item 8b.** `K7-D23-RICH-v1.md`, section 8, the counting sentence. Old:

```text
(t_u = n_z/2 each) and t-pieces (t_t = n_z s/6, at most M - 1 of them in W*U_z, as U_z holds none):
```

New:

```text
(t_u = n_z/2 each) and t-pieces (t_t = n_z s/6, at most M - 1 of them in W*U_z, as the fibre U_z = g_zU_z holds
no piece by LFC (b)):
```

**Item 8c.** `K7-D23-RICH-v1.md`, section 8, the FG7 citation. Old:

```text
(FG7 chain with V_j = g_jU_jg_j^-1)
```

New:

```text
(FG7 (a) with N = Q = W, V_j = g_jU_jg_j^-1, beta = alpha*; W contains no marked vertex, so every order of W is
marked-first)
```

### RF9: Import accounting: direct versus transitive

**Item 9a.** `K7-D23-RICH-v1.md`, section 0, Sun accounting bullet. Old:

```text
- Sun(2), Sun(3), Sun(4) inside a subgroup only through LFC (c) / VFC (V3); Sun(5), Sun(6) only inside the imported
  ROW-U class analysis (E8). No Sun(7).
```

New:

```text
- Direct use: Sun(2), Sun(3), Sun(4) inside a subgroup only through LFC (c) / VFC (V3). Sun(5) and Sun(6) are not
  used directly: the ROW-U standard weights (E8) are applied only to three unmarked neighbours (Lemma R3, k3 = 1),
  where the Sun(5)-dependent branch b >= 4 is vacuous. No Sun(7).
```

**Item 9b.** `K7-D23-RICH-v1.md`, section 0, 'Not used' bullet. Old:

```text
- **Not used:** K63-RES / K62 FG files (FG is re-proved here in this scope), TG (its one-line inequality is re-derived as
  G0), F7, RPLP, Ppair, K, ROW-1, ROW-2, the lemmas of K7-U1 / K7-Z2 / K7-Z23-P5, any probe or census.
```

New:

```text
- **Not used directly:** K63-RES / K62 FG files (FG is re-proved here in this scope), TG (its one-line inequality is
  re-derived as G0), F7, RPLP, Ppair, K, ROW-1, ROW-2, the lemmas of K7-U1 / K7-Z2 / K7-Z23-P5, any probe or census.
- **Transitive closure.** "Not used" and the Sun accounting above refer to direct use only. The imported D23-MIX
  conclusion rests on ROW-1 (`K7-M1-v1.md` with `K7-M1-erratum-v1.md`, verdict sha256
  7121ceeedc1f1b0de8d9642c8f5c2aed052d9f2e83140afee33ffcd2f71ced84), the ROW-1-deg transfer (`K7-Z2-erratum-v1.md`
  G2), D23-CENTER, L1 / F7 / VFC and LFC / INV. The closure of these accepted packages (and of ROW-U / E8 and LFC)
  contains Zhu's Sun(3), Sun(4) and the locally accepted, computer-assisted, model-reviewed Sun(5) record
  `six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md` (sha256
  2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301) and Sun(6) record
  `six-lane-2026-10-16/review/sun-coset6-parent-gate-verdict-v1.md` (sha256
  efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29).
```

**Item 9c.** `K7-D23-RICH-erratum-v1.md` (R-2), R-2, first sentence. Old:

```text
After R-1 the new arguments of the file use Sun(2), Sun(3) and Sun(4) only (through LFC (c) and VFC (V3)); Sun(5) and
Sun(6) enter only inside the imported ROW-U class analysis (E8 standard weights), exactly as section 0 states.
```

New:

```text
After R-1 the new arguments of the file use Sun(2), Sun(3) and Sun(4) only (through LFC (c) and VFC (V3)). Sun(5)
and Sun(6) are not used directly (the E8 standard weights are applied to at most three neighbours, where the
Sun(5)-dependent branch is vacuous); they enter only transitively, through the accepted imports, as section 0 states
after item RF9 of the consolidated erratum `K7-D23RICH-D23P-erratum-v1.md`.
```

### PF1: ROW-2 transfer to the marked apex z: gcd matrix, H35 not read, K2, wording as Z2 G2 / NO4 X-6

**Item P1.** `K7-D23P-v1.md`, section 1, first paragraph. Old:

```text
At z the LFC labels are lambda_u = w_u alpha_zu (u in W'), lambda_t = 3^A w_t alpha_zt, lambda_p = 5^B w_p alpha_zp, all with
g_zj = 6. **ROW-2-deg at z:** four neighbour labels have the form w_u alpha with the w_u pairwise coprime and prime to 30;
one label is 3^A w_t alpha, one is 5^B w_p alpha, with w_t, w_p prime to 30 and to every other w; and LFC (d) holds at z.
These are the only facts the proof of ROW-2 reads (it argues with the six neighbour labels and the bound val < 6; the
apex's own index enters only through 1 - 1/n_z). Hence, exactly as `K7-Z2-erratum-v1.md` G2 transfers ROW-1, ROW-2's
conclusions hold for the alpha-row at z, with k5, k3 the numbers of W'-entries equal to 5, resp. 3:
```

New:

```text
At z the LFC labels are lambda_u = w_u a_u (u in W', a_u := alpha_zu), lambda_t = 3^A w_t a_t and
lambda_p = 5^B w_p a_p (a_t := alpha_zt, a_p := alpha_zp), all with g_zj = 6. **ROW-2-deg at z holds:** g_zj = 6 for
all six neighbours; each W'-label is w_u a_u with the w_u pairwise coprime and prime to 30; the t-label is 3^A w_t a_t
and the p-label is 5^B w_p a_p, with w_t, w_p prime to 30 and to every other w; LFC (d) holds at z; and z's own index
(in particular its 2-part 2^E) never enters these labels. As every entry is <= 5, the six-label gcd matrix is

    gcd(lambda_u, lambda_v) = gcd(a_u, a_v),
    gcd(lambda_t, lambda_u) = gcd(3^A a_t, a_u) = 2^min(v2 a_t, v2 a_u) * 3^[3 | a_u] * 5^[5 | a_t and 5 | a_u],
    gcd(lambda_p, lambda_u) = gcd(5^B a_p, a_u) = 2^min(v2 a_p, v2 a_u) * 3^[3 | a_p and 3 | a_u] * 5^[5 | a_u],
    gcd(lambda_t, lambda_p) = gcd(3^A a_t, 5^B a_p) = 2^min(v2 a_t, v2 a_p) * 3^[3 | a_p] * 5^[5 | a_t],

which is exactly the matrix that ROW-2 uses at its unmarked apex w (`K7-35-v1.md` section 2, first sentence of the
proof, with alpha_wj replaced by alpha_zj). The proof of ROW-2, with `K7-35-erratum-v2.md` K2, reads only this matrix,
the ROW-U-deg / E8 standard weights on the unmarked classes and LFC (d) (val < 6; the apex's own index enters only
through 1 - 1/n_z). Hypothesis H35 of K7-35 (no vertex with 2-exponent >= 2) is not read by that local proof: in both
settings the neighbour labels carry no 2-part beyond their entries (r_t = 3^A w_t, r_p = 5^B w_p and the w_u are odd),
and the apex's own 2-part never enters a neighbour label. This is the apex-independence used for ROW-1 in
`K7-Z2-erratum-v1.md` G2 and `K7-D23-NO4-erratum-v1.md` X-6. Hence ROW-2's conclusions hold for the alpha-row at z,
with k5, k3 the numbers of W'-entries equal to 5, resp. 3:
```

### PF2: M1: exact triangle tables, the reason x = 5 dies, normalisation moved before the F7 step

**Item P2a.** `K7-D23P-v1.md`, section 2, M1, alpha-triangle bullet, last two sentences. Old:

```text
For x = 5: x/gcd(5, r_z) = 5, tau_min >= 15 > 3 min(s_b, 5). Hence **x in {3, 4}**.
```

New:

```text
For x = 5: x/gcd(5, r_z) = 5, because r_z = 2^E w_z has no factor 5 in (a2) (contrast `K7-D23-NO4-erratum-v1.md`
  X-11, where z may carry the 5-marker and x = 5 survives when Bz >= 1); so tau_min >= 15 > 3 min(s_b, 5) >= tau_max.
  Hence **x in {3, 4}**. Exact table (tau_min / tau_max; the L1 test excludes the triangle iff tau_min > tau_max):

  | x | s_b = 1 | s_b = 2 |
  |---|---|---|
  | 1 | 3 / 1: dies | 6 / 2: dies |
  | 2 | 3 / 2: dies | 6 / 4: dies |
  | 3 | 3 / 3: survives | 6 / 6: survives |
  | 4 | 6 / 3 if E = 1: dies; 3 / 3 if E >= 2: survives | 6 / 6: survives |
  | 5 | 15 / 3: dies | 30 / 6: dies |

  Here x/gcd(x, r_z) = 1, 1, 3, (2 if E = 1, 1 if E >= 2), 5 for x = 1, ..., 5. The proof uses only x in {3, 4}; the
  extra restriction (x = 4 dies when s_b = 1 and E = 1) is not used.
```

**Item P2b.** `K7-D23P-v1.md`, section 2, M1, alpha*-triangle bullet, last two sentences. Old:

```text
x* = 4: tau*_min = 4 <= 4 q_a. Hence x* in {2, 4}, and x* = 2 forces q_a = 2.
```

New:

```text
x* = 4: tau*_min = 4 <= 4 q_a. Hence x* in {2, 4}, and x* = 2 forces q_a = 2. Exact table
  (tau*_min / tau*_max):

  | x* | q_a = 1 | q_a = 2 |
  |---|---|---|
  | 1 | 4 / 1: dies | 4 / 2: dies |
  | 2 | 4 / 2: dies | 4 / 4: survives |
  | 3 | 12 / 3: dies | 12 / 6: dies |
  | 4 | 4 / 4: survives | 4 / 8: survives |
  | 5 | 20 / 4: dies | 20 / 8: dies |

  Here x*/gcd(x*, r_z) = 1, 1, 3, (2 if E = 1, 1 if E >= 2), 5 for x* = 1, ..., 5, so tau*_min = 4, 4, 12, 4, 20.
```

**Item P2c.** `K7-D23P-v1.md`, section 2, M1, F7 bullet, opening. Old:

```text
- F7 in the inverted configuration at apex z for the ordered pair (a, b):
```

New:

```text
- Normalise g_z = 1; then g*_z = g_z^-1 = 1 and U*_z = g_zU_zg_z^-1 = U_z, so the inverted configuration is
  normalised at z simultaneously; put X*_j := U_zU*_j. F7 in the inverted configuration at apex z for the ordered
  pair (a, b):
```

**Item P2d.** `K7-D23P-v1.md`, section 2, M2, first sentence. Old:

```text
**M2 (inverted VFC at z).** Normalise g_z = 1; then the inverted configuration is normalised at z as well
(g*_z = g_z^-1 = 1, U*_z = U_z). With X*_j := U_zU*_j (measure alpha*_zj/6, L0.3), Y*_j := G \ X*_j and
```

New:

```text
**M2 (inverted VFC at z).** The normalisation g_z = g*_z = 1, U*_z = U_z and X*_j = U_zU*_j are fixed in M1
before the F7 step; X*_j has measure alpha*_zj/6 (L0.3). With Y*_j := G \ X*_j and
```

### PF3: Section 0: L0.3 listed; transitive Sun(5)/Sun(6) closure stated

**Item P3a.** `K7-D23P-v1.md`, section 0, rules-k7 import bullet, first line. Old:

```text
- L1 (T1)-(T3) with tau_min / tau_max, VFC (V1)-(V4) and F7: `six-lane-20261016/sun-coset7/rules-k7-v1.md` sha256
```

New:

```text
- L0.3 (mu(U_iU_j) = alpha_ij/g_ij; used in M2 for mu(X*_j) in the inverted configuration; listed for LFC in
  `K7-LFC-INV-erratum-v1.md` E1), L1 (T1)-(T3) with tau_min / tau_max, VFC (V1)-(V4) and F7:
  `six-lane-20261016/sun-coset7/rules-k7-v1.md` sha256
```

**Item P3b.** `K7-D23P-v1.md`, section 0, Sun accounting bullet. Old:

```text
- New set prohibitions here use Sun(2) only (through LFC (c) / VFC (V3)); larger Sun instances enter only inside the
  imported ROW-2 / D23-CENTER proofs. **Not used:** ROW-1, FG, TG, RPLP, Ppair, K, any computation.
```

New:

```text
- New set prohibitions here use Sun(2) only (through LFC (c) / VFC (V3)); larger Sun instances enter only inside the
  imported ROW-2 / D23-CENTER proofs. **Not used directly:** ROW-1, FG, TG, RPLP, Ppair, K, any computation.
  **Transitive closure:** ROW-2 rests on the ROW-U / ROW-U-deg class analysis with the E8 standard weights (whose R24
  branch b >= 4 uses Sun(5) and whose R5 class uses Sun(6)); D23-CENTER rests on the accepted imports of
  `K7-D23-NO4-v1.md` (ROW-1 with `K7-M1-erratum-v1.md` and the transfer `K7-Z2-erratum-v1.md` G2, L1 / F7 / VFC,
  LFC / INV). The closure of these accepted packages contains Zhu's Sun(3), Sun(4) and the locally accepted,
  computer-assisted, model-reviewed Sun(5) record `six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md`
  (sha256 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301) and Sun(6) record
  `six-lane-2026-10-16/review/sun-coset6-parent-gate-verdict-v1.md` (sha256
  efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29). "Sun(2) only" and "Not used" refer to direct
  use. No Sun(7).
```

## Unchanged

- K7-D23-RICH: G0; FG7 (previous statement retained as the special case u in W, N = V \ {u}); Corollary 5/6 (val <= 5
  and the equality clause, now with the weight defined explicitly); NO5 (with erratum-1 R-1); Lemma R3, its survivors
  S1-S4 and Corollary R3; Lemma TR; Lemma CC; Theorem K7-D23-RICH; Lemma TZ (i)-(iii); Lemma LZ; the residue
  description of section 9 (with the RF6 qualification of its unverified remark).
- K7-D23P: the row trichotomy, the (a') exclusion, the position count, M1 (x in {3,4}, x* = 2, q_a = 2, X*_a subset
  X*_b), M2 and Theorem K7-D23P.
- Scope: RICH excludes exactly the (a1) configurations with T* subset W3 or T subset W3*; D23P excludes exactly the (a2)
  configurations with a 4-type z-row in either orientation. Still OPEN: the (a1) residue, (a2) with both z-rows of type
  (b'), K6.2* and full Sun(7). No novelty, Lean or human-review claim.
