# K7-D23-NO4-erratum-v1: tables, role maps, citations, R0 lift and wording (no theorem change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:34:05-0700.
- **Overlays:** `K7-D23-NO4-v1.md`, sha256 a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d, frozen byte-identical.
- **Responds to (read in full):** Codex `RUN/review/sun7-D23-codex-v1.prompt.stdout.txt` (sha256 8be1767fce86eae423fcffabc12659fe4e82690d60a191d37fb5af26c9b08992; CENTER ACCEPT 0/0/0;
  MIX ACCEPT-WITH-FIXES 0/0/1) and Claude `RUN/review/sun7-D23-claude-v1.prompt.note.md` (sha256 86f89f3c9409ab2ed59cd630e0c495fba38332737255d25061c25d9c12af1265; CENTER
  ACCEPT-WITH-FIXES 0/0/5: A-1..A-5; MIX ACCEPT-WITH-FIXES 0/0/8: B-1..B-8; general MINOR G-1).
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Status:** written overlay. Claims D23-CENTER and D23-MIX keep their exact statements and scopes. No new premise,
  no new claim, no computation. Every numbered finding is disposed below; nothing else changes.

## X-1 (Claude A-1): the gcd reduction in section 1, C2

Replace "Since all r_j (j!=z) are odd and contain only disjoint 3/5 marker powers, while alpha*_zj in {1,2,4},
gcd(d_j,d_k)=gcd(alpha*_zj,alpha*_zk)" by:

**"The r_j (j != z) are odd and pairwise coprime (K7: the r_i are pairwise coprime), and alpha*_zj in {1,2,4}. Hence
no odd prime divides two of the d_j = alpha*_zj r_j, and gcd(d_j,d_k) = 2^min(v2 alpha*_zj, v2 alpha*_zk) =
gcd(alpha*_zj, alpha*_zk)."** This holds when t or a 5-marked vertex is among j, k.

## X-2 (Claude A-2): the C1 table and the x* = 5 step

Insert in section 1, C1, after the two displayed formulas (triangle {z,a,b}, a in F*, b in F, alpha-values
(alpha_za, alpha_zb, alpha_ab) = (s_a, 4, x); r_z = 2^E 5^Bz w_z with E >= 1 and 3 not dividing r_z):

| x | x/gcd(x,r_z) | tau_min | tau_max (s_a=1) | tau_max (s_a=2) | survives s_a=1 | survives s_a=2 |
|---|---|---|---|---|---|---|
| 1 | 1 | 4 | 1 | 2 | no | no |
| 2 | 1 | 4 | 2 | 4 | no | yes |
| 3 | 3 | 12 | 3 | 6 | no | no |
| 4 | 2 if E=1; 1 if E>=2 | 4 | 4 | 8 | yes | yes |
| 5 | 5 if Bz=0; 1 if Bz>=1 | 20 or 4 | 4 | 8 | only if Bz>=1 | only if Bz>=1 |

(tau_max = min(s_a x, 4 min(s_a,x), s_a min(4,x)) for apexes z, a, b.) Replace the sentence "This also rules out
x*=5." by: **"Symmetrically, x* = 5 forces x = 1 by INV (x + x* <= 6, x >= 1), and x = 1 dies in the original
table."** The inverse table (alpha*-values (4, s*_b, x*), small entry at b) is the same table with a and b exchanged,
since both compulsory terms have power-of-2 numerators over odd ell and tau_max is symmetric in a <-> b. The s_a = 1
and s*_b = 1 conclusions (x = 4, resp. x* = 4) are read AFTER the two INV exclusions of 5.

## X-3 (Claude A-3): explicit role map for the inversions in C3

Replace "If only a0 exists is the same argument in the inverse configuration (which has exactly the same indices)"
and the inversion in the last bullet by:

**"The inverted configuration has the same labelled indices and markers (INV(a), LFC-erratum E6), its alpha-matrix
is alpha*, and its own inverse is the original (alpha** = alpha). Its z-rows are alpha* and alpha, both 4-type. Its
F, F*, s, s* are our F*, F, s*, s; our a0 (s_a0 = 1) plays the role of its b0. C1 and C2 hold for it verbatim
(C1 by the a <-> b symmetric table of X-2; C2 with local indices alpha_zj r_j)."** Hence the case "only a0 exists"
is the case "only b0 exists" of the inverted configuration, and in the case "neither exists" the inverted
configuration supplies at least two a in F* with alpha*_ab = 4 for every b in F.

## X-4 (Claude A-4): acceptance citations for L1, VFC and F7, including the inverted configuration

In section 0 replace the acceptance reference for the general rules by: **L1 (T1)-(T3) with tau_min/tau_max, VFC
(V1)-(V4) and F7 (addendum A1, the forced-containment condition of RPLP) are accepted as sound necessary rules by the
written verdict `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` sha256
73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 (its "Active triangle T ... VFC and RPLP rules are
sound" item and its RPLP paragraph on the forced condition). `RUN/review/sun7-Z2-parent-verdict-v1.md` sha256
0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c confirms their use in K7. Application of L1 and F7
to the inverted configuration is cited from `K7-Z2-erratum-v1.md` G5 (sha256
3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9)**: the inverted configuration is itself a family of
pairwise disjoint left cosets with the same indices, so every general rule applies to it.

## X-5 (Claude A-5, B-8): R0 lift for both claims, with alpha* preserved

Replace "R0 gives arbitrary groups." (end of section 1) by, and append after "This proves D23-MIX." (end of section 3):

**"By R0 the claim holds for arbitrary groups with finite-index subgroups: N = intersection of the cores of the U_i is
normal of finite index, so it lies in every U_i and in every conjugate g_iU_ig_i^-1. The quotient G/N preserves the
indices n_i, the indices of U_i cap U_j and of g_iU_ig_i^-1 cap g_jU_jg_j^-1, and pairwise disjointness. Hence
alpha, alpha*, the markers and both row types are the same in G/N (`RUN/review/sun7-lfc-inv-parent-verdict-v1.md`
sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18, item 6)."**

## X-6 (Claude B-1): exact ROW-1 transfer used at apex z in section 2

Replace "This is exactly the ROW-1-degree transfer accepted in Z2 erratum G2" by:

**"ROW-1-deg at z holds: g_zj = 6 for all six neighbours; each W-label is w_u alpha_zu with the w_u pairwise coprime
and prime to 30; the t-label is m_t w_t alpha_zt with m_t = 3^A 5^Bt odd and {3,5}-smooth and w_t prime to 30 and to
every w_u; LFC(d) holds at z, and z's own index never enters these labels. The apex-independence of ROW-1's proof is
`K7-Z2-erratum-v1.md` G2 (accepted instance m = 5^h). The 3-sensitive step, the last case of ROW-1(b), is covered by
`K7-M1-erratum-v1.md` F2/F5 (sha256 4094b53783244e8b824dd64409d28380d0a635e76d74035e361f5ca22a26c510): since 3 | m_t,
gcd(lambda_t, three-label) is exactly 3, and the listed sets {t}, {t,x}, {t,3,3} still contain every allowed set
through t, so the weights (1/3 on threes, 1 on ones, 1/2 on twos, 1/3 on t) give 5 + alpha_zt/3 >= 6 when
alpha_zt >= 3."** The composition of G2 and F2/F5 is therefore within accepted scope.

## X-7 (Claude B-2): the precise ROW-1(c) output

Replace "If no W-entry is 3, its five entries are {1,2,4}; ROW-1(c) gives a 4-type full row" by:

**"If no W-entry is 3, then (k5 = k3 = 0) its five W-entries lie in {1,2,4}. By ROW-1(c) with `K7-M1-erratum-v1.md`
F3, gcd(w_u alpha_zu, m_t w_t alpha_zt) = gcd(alpha_zu, alpha_zt) for every alpha_zt <= 5, so ROW-U-deg holds on all
fifteen label pairs and ROW-U's proof gives the full six-entry row: all entries, including alpha_zt, lie in {1,2,4},
at most one equals 1, and at least three equal 4."**

## X-8 (Claude B-3): the alpha*-dichotomy

Append to section 2: **"The alpha*-version of the k5 = 5 kill uses LFC(d) of the original configuration, since
alpha** = alpha. The inverted configuration has the same labelled indices, hence W is unmarked there too (LFC-erratum
E6), and section 2 applies to it verbatim."**

## X-9 (Claude B-4): notation

In section 3 rename **P = W \ T = {p1, p2}** to **Q = W \ T = {u1, u2}**, and read every "p in P", "s_p", "D*_p",
"d*_p", "X*_p", "Y*_p" there as "u in Q", "s_u", "D*_u", "d*_u", "X*_u", "Y*_u". The letter p is reserved for the
5-marked third vertex of section 0, which cannot occur under D23-MIX; the vertices of Q are unmarked.

## X-10 (Codex MINOR, Claude B-5): order of the q_a = 1 conclusion in M1

In section 3, M1, replace "gives x* in {2,4,5}, with x*=4 when q_a=1" by: **"gives x* in {2,4} or x* = 5 (the latter
only if Bz >= 1) when q_a = 2, and x* in {4,5} (5 only if Bz >= 1) when q_a = 1."** The following sentences of M1
remove x* = 5 and x = 5 by INV; only then does x* = 2 follow (x >= 3 and x + x* <= 6), and the inverse table at x* = 2
forces q_a = 2. Conclusion unchanged.

## X-11 (Claude B-6): the M1 alpha-triangle table

Insert in section 3, M1, after the tau_max formula (alpha-values (alpha_za, alpha_zu, alpha_au) = (3, s_u, x) with
a in T, u in Q, ell_a = w_a, ell_u = w_u):

| x | tau_min / tau_max (s_u = 1) | tau_min / tau_max (s_u = 2) |
|---|---|---|
| 1 | 3 / 1: dies | 6 / 2: dies |
| 2 | 3 / 2: dies | 6 / 4: dies |
| 3 | 3 / 3: survives | 6 / 6: survives |
| 4 | 6 if E=1 (dies), 3 if E>=2 (survives) / 3 | 6 / 6: survives |
| 5 | 15 if Bz=0 (dies), 3 if Bz>=1 (survives) / 3 | 30 if Bz=0 (dies), 6 if Bz>=1 (survives) / 6 |

(tau_min = lcm(3, s_u, x/gcd(x, r_z)); tau_max = min(s_u x, s_u min(3,x), 3 min(s_u,x)).) The proof uses only
the necessary restriction x in {3,4,5}; the exact survivor list is a subset of it.

## X-12 (Claude B-7): the inverse VFC facts used in M2

Replace the first sentence of M2 by: **"The original is normalised by g_z = 1; then g*_z = g_z^-1 = 1 and
U*_z = g_zU_zg_z^-1 = U_z, so the inverted configuration is normalised at z simultaneously. Put X*_j = U_zU*_j,
Y*_j = G \ X*_j, D*_j = U_z g*_j U*_j. VFC(V1) for the inverted configuration gives D*_j subset Y*_j; INV(b) for the
inverted configuration together with alpha** = alpha gives mu(D*_j) = alpha_zj/6, and L0.3 gives
mu(X*_j) = alpha*_zj/6."** The displayed measures of M2 follow.

## X-13 (Claude G-1): the reference to the obstruction note in section 4

Replace "The abstract family in `K7-D23-obstruction-v1.md` is a precise obstruction to closing this residue by
LFC+INV+T/F7 alone; it is not an actual coset construction." by: **"(Navigation only, not a claim of this file: the
separate unreviewed note `K7-D23-obstruction-v1.md`, sha256 9a6d1e609c3ed95e2dc77ffcb5fada5b35b1beded4593662ce4e7396fc514863,
records an abstract double-3 pattern; nothing in this file depends on it.)"**

## Non-defect remarks recorded (no change)

Claude: E >= 1 is never load-bearing in C1 (for x in {2,4}, x/gcd(x,r_z) divides 4 for every r_z); "at most one 1"
is not used in CENTER; MIX's restriction to unmarked W is load-bearing only in section 2. M1-M2 avoid t correctly
(3/gcd(3,ell_t) = 1 and gcd(d*_t, d*_a) = 3), so |Q| = 2 is exactly what is needed. Codex: the full C1/M1 tables,
F7 orientations, C2 gcds, C3 four types, ROW-1 transfer and R0 lift were checked with no further finding.

## Unchanged

Claims D23-CENTER (5-marker anywhere; both z-rows 4-type excluded) and D23-MIX (5-marker absent, on z or on t;
either z-row 4-type excluded) keep exactly their statements. Double-3 z-rows, the third-vertex-5 mixed rows of the
different-vertex family, and every other open K7/K6.2*/K6.3 family remain OPEN. No novelty, Lean or human-review
claim.
