# K7-TC: cross-apex transfer-count coupling in (a1); Case B narrowed, Pc5' excluded, surviving obstruction Q_B'

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:04:04-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation was run; no probe is a premise.
- **Status:** CANDIDATE written mathematics, **conditional** on the candidates `K7-D23-RICH-v1.md` (sha256
  ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3) + `K7-D23-RICH-erratum-v1.md` (sha256
  8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69) and `K7-A1-STRUCT-v1.md` (sha256
  c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf; sections 1-5 used: Corollary W3, E3, Lemma B, Theorem
  CASEB). (a1) is NOT excluded; full Sun(7) remains OPEN. The patterns of section 5 are abstract, not group constructions.

## 0. Setting, imports, conventions

Setting (a1) and notation of RICH section 0 (z: 2-marker, t: 3-marker, W five unmarked vertices; T, T*). C^alpha is the
configuration, C^alpha* its inverse (INV (a); E6); C denotes either. In C, at an apex u: the **fibres** are the left
U_u-cosets, L_j^(u) := g_jU_jU_u is the union of the fibres meeting g_jU_j (LFC (b)); after normalising g_a = 1 at an apex a,
X_u^(a) := U_aU_u, D_j^(a) := U_a g_j U_j (VFC (V1)), with mu(X_u^(a)) = (alpha of C)_au/6 and mu(D_j^(a)) = (alpha* of C)_aj/6.
Imports: everything imported by RICH and A1-STRUCT at the same scopes; in particular LFC (a)-(d), INV, VFC (V1)-(V4),
Sun(2)-Sun(5) only through LFC (c)/VFC (V3), FG7 and Corollary 5/6 of RICH (for C^alpha and C^alpha*). A *row* at u is
written (W-multiset | c | e) with c = x_uz, e = x_ut for the alpha-matrix x of C; "fours/twos/ones" refer to W-entries
4/2/1, and labels/local indices of unmarked vertices are entry * w.

## 1. Lemma TC (transfer) [NEW]

**For distinct vertices u, a, j and C in {C^alpha, C^alpha*}: L_j^(u) subset L_a^(u) iff D_j^(a) subset X_u^(a)
(g_a = 1). In that case D_j^(a) cap D_u^(a) = empty.**

*Proof.* Both statements are invariant under a common left translation; take g_a = 1, so L_a^(u) = U_aU_u. If
g_jU_jU_u subset U_aU_u then g_jU_j subset U_aU_u, so U_a g_j U_j subset U_aU_aU_u = U_aU_u. Conversely, if
U_a g_j U_j subset U_aU_u then g_jU_jU_u subset U_a g_j U_j U_u subset U_aU_u. Finally D_u^(a) cap X_u^(a) = empty (V1). QED
(RICH's Lemma TR is the case (j, a) = (t, z).)

**Rigidity source (RICH Corollary 5/6, equality clause).** At u in W, if feasible weights y_1, ..., y_m (for C's labels at u)
all have value 5, then every fibre meeting a coset has an allowed S-set S with y_i(S) = 1 for every i. Hence: if every
allowed S with y_i(S) = 1 (all i) and j in S contains a, then L_j^(u) subset L_a^(u).

## 2. Rigid rows used (E >= 2 throughout; each value-5 weight is feasible and FG gives <= 5, so it is optimal)

- **R1 = ({2,2,4,4} | 3 | 2)**, fours f1, f2, twos s1, s2. Maximal allowed sets: {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
  (z-t gcd 6). y_A = (f1 1/2, f2 0, s 1/2, 1/2, t 1/2, z 0) and y_B (f1 0, f2 1/2, rest equal) have value 5. y_A(S) = y_B(S)
  forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.**
- **R3 = ({2,2,2,4} | 3 | 4)**, four f, twos s1, s2, s3. Maximal allowed sets {f,z,t,s_i}, {s_i,s_j} (z-t gcd 12).
  y_A = (s 1/2 each, f 1/2, t 0, z 0), y_B = (s 1/2 each, f 0, t 1/2, z 0) have value 5. Weight-1 sets for both have
  [f in S] = [t in S]; a weight-1 set containing z lies in some {f,z,t,s_i} and must contain f (y_A) hence t.
  **L_f = L_t and L_z subset L_t.**
- **R4 = ({1,4,4,4} | c | 2)**, c in {1,2}, one o, fours f1, f2, f3. y_i = (o 1, f_i 1, else 0) have value 5 (o's label is coprime
  to all). Every fibre not containing o contains f1, f2, f3; z (label c 2^E w_z) and t (label 2 3^A w_t) are coprime to o.
  **L_z, L_t subset L_f_i (i = 1, 2, 3).**
- **R5 = ({1,2,4,4} | 3 | e)**, e in {2,4}, one o, two s, fours f1, f2. y_i = (o 1, f_i 1, else 0) have value 5. Every fibre
  not containing o contains f1 and f2; z (3 2^E w_z) and s (2 w_s) are coprime to o. **L_z, L_s subset L_f1 cap L_f2.**
- ({1,4,4,4} | c | 1) with c in {1,2} has value >= 6 (y = (o 1, fours 1/3, t 1); t's label 3^A w_t is coprime to all), so it
  does not occur.

## 3. Theorem K7-TC-B (conditional) [NEW]

**In Case B of Theorem CASEB (T = W, T* = {a1,a2,a3} != W, W \ T* = {v1,v2}): alpha*_v1v2 = 2 and alpha*_aa' = 2 for all
a != a' in T*.**

*Proof.* By CASEB, alpha*_aa', alpha*_v1v2 lie in {1,2}, alpha*_av = 4, alpha_av = 2, alpha_aa' = 4, alpha_v1v2 = 4,
alpha_vt = 4, alpha_at in {2,4}, alpha_za = alpha_zv = 3, alpha*_za = 3, E >= 2. The alpha*-values on the triangle T* avoid
(1,1,2) (triangle rule, A1-STRUCT section 0); (1,1,1) gives an alpha*-row W-part {1,1,4,4} of value >= 2 + 4 = 6 > 5. So
the pattern is (2,2,2) or (1,2,2). For a in T*, alpha*_ta lies in {2,4}: 3 and 5 are excluded (E3, NO5) and 1 by the
t-triangle {t, a, v}, whose alpha*-entries (1, alpha*_tv, 4) are forbidden for alpha*_tv in {1,2}.

(i) **alpha*_v1v2 = 1 is impossible.** Each v has alpha*-row ({1,4,4,4} | alpha*_zv | alpha*_tv) with the one at v'; by the
last item of section 2, alpha*_tv = 2, so it is R4: L*_z subset L*_a for every a in T* (in C^alpha*, apex v). Lemma TC in
C^alpha*: at apex a, D*_z cap D*_v1 = D*_z cap D*_v2 = empty. At a (C^alpha*, VFC; masses alpha_aj/6 by INV (b) with
alpha** = alpha): a', a'' 4/6, v1, v2 2/6, z 3/6, t alpha_at/6; local indices 4w (a', a''), 2w (v's), 3 2^E w_z (z),
alpha_at 3^A w_t (t, even). A right coset with both v's has S-set exactly {v1, v2} (a third element has gcd 2 with both
v's and with each other's labels, Sun(3); z is excluded). Let Z be the union of the cosets in D*_z (measure 3/6), V2 that of
the cosets with S = {v1,v2}, R the rest of the union. a' has mass 4/6 and lies in Z cup R, so mu(R) >= 1/6; the v-mass 4/6
gives 4/6 <= 2 mu(V2) + mu(R). Hence mu(union) >= 3/6 + (4/6 - mu(R))/2 + mu(R) >= 5/6 + 1/12 = 11/12, while FG7 for
C^alpha* at a gives mu(union) <= 5/6. Contradiction.

(ii) **Pattern (1,2,2) is impossible** (now alpha*_v1v2 = 2). Let alpha*_a1a2 = 1, alpha*_a1a3 = alpha*_a2a3 = 2. The alpha*-rows
of a1 and a2 are ({1,2,4,4} | 3 | alpha*_ta) with alpha*_ta in {2,4}, i.e. R5 with o = the other end of the 1-edge, s = a3,
fours v1, v2: L*_z, L*_a3 subset L*_v1 cap L*_v2 (C^alpha*, apexes a1 and a2). Lemma TC: at apex v (either v), in C^alpha*,
D*_z cap D*_ai = D*_a3 cap D*_ai = empty (i = 1, 2). At v (C^alpha*, VFC; masses alpha_vj/6): a's 2/6 each, v' 4/6, z 3/6,
t 4/6; local indices 2w (a's), 4w (v'), 3 2^E w_z (z), 4 3^A w_t (t); allowed sets are the subsets of the 4-sets
{v', z, t, a_i} and the pairs {a_i, a_j} (a triple with two a's has all gcds 2; a 5-set would contain {z, a_i, a_j}).
Let Z := cosets in D*_z (measure 3/6; they contain no a1, a2), K := cosets with S = {a1, a2} (the only cosets with two a's,
since a3 meets neither a1 nor a2), N := the rest outside Z. v' has mass 4/6 with at most 3/6 inside Z, so mu(N) >= 1/6;
each N-coset holds at most one a, so mu(N) >= (2/6 - mu(K)) * 2 + mass(a3 outside Z) >= 4/6 - 2 mu(K). Thus
mu(union) >= 3/6 + mu(K) + max(1/6, 4/6 - 2 mu(K)) >= 11/12 > 5/6 (minimum at mu(K) = 1/4), contradicting FG7 for C^alpha* at v.
QED

## 4. Proposition TC-P [NEW]

**The abstract pattern Pc5' of `K7-A1-STRUCT-v1.md` section 6 violates Lemma TC with V4; no configuration has its data.**

*Proof.* In Pc5' the alpha-rows at u3 and u5 are R1, with fours {u2, u4} at u3 and {u4, u1} at u5. Hence (C^alpha)
L_u2^(u3) = L_u4^(u3) and L_u1^(u5) = L_u4^(u5), and Lemma TC at apex u4 gives D_u2 cap D_u3 = empty and D_u1 cap D_u5 =
empty. At u4 (C^alpha, VFC; masses alpha*_(u4 j)/6): u1, u2: 4/6; u3, u5: 2/6; z: 3/6; t: 4/6 (alpha*_t,u4 = 4); local
indices 4w (u1, u2), 2w (u3, u5), 12 w_z (z), 4 3^A w_t (t). A coset containing u1 and u2 contains neither u3 nor u5; one
containing u1 but not u2 contains at most u3 among the twos; one containing u2 but not u1 at most u5; a coset with neither
holds at most two twos (no allowed triple of z or t with two twos). With K := mu(cosets containing u1 and u2), the
u1-only and u2-only cosets each have measure 4/6 - K and absorb at most min(4/6 - K, 2/6) of the two-mass each; the
remaining two-mass sits in cosets with neither, at most two per coset. So mu(union) >= K + 2(4/6 - K) +
max(0, 2K - 4/6)/2 >= 1 (for K <= 2/6 the second term already gives >= 1; for K >= 2/6 the sum equals 1). But the union
avoids U_u4 (V4). Contradiction. QED

## 5. Surviving obstruction Q_B' (abstract pattern; not a group construction)

**Q_B'** is the pattern Q_B of A1-STRUCT section 6 with **alpha*_v1v2 = 2** (instead of 1). Explicitly: E = 2, A = 1,
Bz = Bt = 0; alpha: z-W 3, z-t 1, a-a 4, a-v 2, v1v2 4, t-a 2, t-v 4; alpha*: z-a 3, z-v 1, z-t 1, a-a 2, a-v 4, v1v2 2,
t-a 4, t-v 2. It satisfies Theorem K7-TC-B's conclusion.

**Checks beyond A1-STRUCT section 6** (all other items there hold verbatim): INV on v1v2: 4 + 2 = 6. Triangles changed:
alpha* {a, v1, v2} = (2,4,4), {t, v1, v2} = (2,2,2), {z, v1, v2} = (1,1,2) with tau_min = lcm(1, 1, 2/gcd(2, 4 w_z)) = 1 =
tau_max. The alpha*-row at v is ({2,4,4,4} | 1 | 2): value <= 9/2 < 5 (cover: weight 3/2 on {f,f,f,v'}, 3/2 on {f,f,f,t},
1 on {f,f,f,z}, 1/2 on {v', t}).
**Rigid rows of Q_B':** alpha-rows R1 at each a (fours: the other two a's) and R3 at each v (four v', twos the a's). All
alpha*-rows are slack (R2 at a: <= 4; ({2,4,4,4}|1|2) at v: <= 9/2), so C^alpha* yields no transfer.
**All transfers (C^alpha):** from R1 at a_i: at apex a_k, D_aj cap D_ai = empty ({i,j,k} = {1,2,3}); from R3 at v: at apex
t, D_v' cap D_v = D_z cap D_v = empty; at apex v', D_t cap D_v = D_z cap D_v = empty.
**Counts are satisfiable** (explicit right-coset distributions, measures; every listed S-set is allowed):
- apex a (masses a', a'' 2/6; v1, v2 4/6; z 3/6; t 4/6; a' and a'' disjoint): {v1,v2,z,t,a'} 2/6, {v1,v2,z,t,a''} 1/6,
  {v1,v2,t,a''} 1/6: union 4/6 <= 5/6.
- apex v (masses a's 4/6 each; v' 2/6; z 1/6; t 2/6; z and t disjoint from v'): {a1,a2,a3,v'} 2/6, {a1,a2,a3,t} 2/6,
  {z} 1/6: union 5/6 (FG allows equality).
- apex t (masses a's 4/6; v's 2/6; z 1/6; v1, v2, z pairwise disjoint): {a1,a2,a3,v1} 2/6, {a1,a2,a3,v2} 2/6, {z} 1/6:
  union 5/6 < 1, W-union 4/6 <= 5/6 (PFG-t).
- apex z: no transfer ends at z (no rigid row puts z in a forced position); LFC at z holds (A1-STRUCT check 3).
The fibre-type counts at the rigid rows have integral solutions in units n_u/6 (e.g. at v: one fibre-unit {a1,a2}, and
{a_i, v', t, z} / {a3, v', t} units filling the rest), consistent with the 1/6-granularity of the FG blocks.

## 6. Exact residue and missing lemma

- **(a1) residue after this file (conditional):** Case A (T = T* = W) beyond Pc5' is not analysed here; Case B is reduced
  to alpha*_v1v2 = 2, alpha* = 2 on T*, which contains Q_B'. **Missing lemma:** a constraint that uses R1/R3 fibre types
  beyond single containments (their unions), or a count at z or t with these transfers, excluding Q_B'.
- **Not covered:** (a2) (see checkpoint 011 for the written five-entry reductions, not frozen yet); K6.2*; full Sun(7).
- Requested checks: the value-5 weights of R1, R3, R4, R5 and the forced equalities; the two counts in section 3 and the
  count in section 4; the transfer orientations (C^alpha* in section 3, C^alpha in section 4). No novelty, Lean or
  human-review claim.
