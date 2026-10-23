# K7-A1-A2-delta-erratum-v1: one combined overlay for the A1 slice (A1-STRUCT, K7-TC, K7-TC-A22) and the A2 slice (K7-A2-FIVE)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:24:09-0700.
- **Owner:** Sun7K62Successor. Written overlay; no computation (each Old text below is copied verbatim from its frozen
  file and occurs there exactly once).
- **Overlays (frozen byte-identical, not modified):** `K7-A1-STRUCT-v1.md` c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf; `K7-TC-v1.md`
  cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117; `K7-TC-A22-v1.md` 9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41; `K7-A2-FIVE-v1.md`
  93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc; manifest `delta-package-A1-TC-A22-A2FIVE-v1.md` 9fb6e385cdbc3c02be5b1f3864a75bab0bf4609dead70840533673d4e6cbfdd4.
- **Source findings (RUN/review/):** A1 Claude `sun7-K7-delta-A1-claude-v1.prompt.note.md` 509414a92b8e68dab5ccd811c02f3f93972fed4deeef22a74b4f474892adb412 (0/0/14); A1 Codex
  `sun7-K7-delta-A1-codex-v1.prompt.stdout.txt` d3f279da73c51fd6e9fb0310cb4c53f8d7a8dd38d76a7577a502758c123a5b92 (0/0, MINOR B1, T1, T2, A1); A2 Claude
  `sun7-K7-delta-A2-claude-v1.prompt.note.md` 244734c3cc2dcc05787f6961855890f6dfd98a552bda371aebda705d106c8e75 (0/0/19); A2 Codex `sun7-K7-delta-A2-codex-v1.prompt.stdout.txt`
  0514931df625d67bf8cb68daed73ff3e789934cd10f535b7492fdc9aa5493a06 (0 FATAL, 1 MAJOR scope repair, MINORs).
- **Accepted base:** RICH and D23P verdict `RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0.

## Disposition
- A1 Claude: G1 -> A1.2, A1.3, TC.1, A22.1; G2 -> A1.4, A1.10, TC.2, A22.1; G3 -> A1.4; S1 -> A1.6; S2 -> A1.7, A1.8;
  S3 -> A1.9, A1.10; S4 -> A1.11; **T1 -> TC.3, TC.4 (R1 extended to every E >= 1 only, as needed for K7-TC-A22; R3, R4,
  R5 and the ({1,4,4,4}|c|1) exclusion keep E >= 2 - the reviewer's optional R4/R5 extension is deliberately not
  adopted)**; **T2 -> TC.7 (Lemma FG-V, explicit proof), TC.8, TC.10**; T3 -> TC.2; T4 -> TC.11; **X1 -> A22.3**;
  X2 -> A22.2; X3 -> A22.4; W3 citation -> A1.5; navigation -> A1.1, A1.13, TC.13, TC.14, A22.5.
- A1 Codex: B1 -> A1.11, A1.12; T1 (occupied fibres) -> TC.5, TC.6; T2 (TC-P parenthesis) -> TC.12; A1 (R1 at E = 1)
  -> TC.4, A22.3; TC-B (ii) meaning of N -> TC.9.
- A2 Codex: MAJOR scope repair -> A2.10 (enumerated claims; no blanket FG7 with beta <= 5), A2.12 (adapted chain for
  actual families or beta <= 4); B3 -> A2.12, A2.15; B7 -> A2.16; Transfer -> A2.17; Sun accounting -> A2.2, MAN.1.
- A2 Claude: G1 -> A2.1; G2 -> A2.2, MAN.1; F1 -> A2.3; F2 -> A2.1, A2.5; F3 -> A2.4; F4 -> A2.6; C1 -> A2.7;
  Z1 -> A2.8, A2.9; B1 -> A2.10; B2 -> A2.12; B3 -> A2.15; B4, B6 -> A2.11; B5 -> A2.13, A2.14; T1-T5 -> A2.17, A2.2.

**Statement scope changes (all reviewer-requested; no theorem redesign):** TC-P is restated for its exact matrix data
(TC.11); R1 is extended to every E >= 1 with a written proof (TC.4); Theorem K7-A2-BRIDGE is narrowed to an enumerated list
(A2.10); Corollary K7-A2-TRANSFER is restricted to named claims (A2.17). Every other conclusion is unchanged.

## Replacements (verbatim Old -> New)

**Item A1.1.** `K7-A1-STRUCT-v1.md`, title. Old:

```text
and two abstract patterns that pass every written rule so far
```

New:

```text
and two abstract patterns that pass the listed local checks of section 6 only (navigation)
```

**Item A1.2.** `K7-A1-STRUCT-v1.md`, header Status. Old:

```text
- **Status:** CANDIDATE written mathematics (sections 1-5) plus a precise OBSTRUCTION record (section 6). Sections 1 and 5
  are **conditional on the candidate `K7-D23-RICH-v1.md`** (sha256 ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3)
  with its erratum (sha256 8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69), now in parent review. Nothing
  here claims that the (a1) family is excluded; full Sun(7) remains OPEN.
```

New:

```text
- **Status:** CANDIDATE written mathematics (sections 1-5) plus an OBSTRUCTION record (section 6; navigation only, no
  existence or completeness claim). Sections 1-5 rest on the accepted RICH base (verdict
  `RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md`, sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0: RICH-v1 + erratum-1 R-1
  + consolidated erratum; FG7 in chain form (a)/(b) per RF1, Corollary 5/6 with the RF2 equality clause). Nothing here
  claims that the (a1) family is excluded; full Sun(7) remains OPEN.
```

**Item A1.3.** `K7-A1-STRUCT-v1.md`, section 0. Old:

```text
From RICH (imports, at their candidate scope):
```

New:

```text
From the accepted RICH base (header):
```

**Item A1.4.** `K7-A1-STRUCT-v1.md`, section 0, Sun sentence. Old:

```text
Sun(2)-Sun(5) are used only inside LFC (c) / VFC (V3); Sun(5) appears exactly where five pieces
with pairwise gcds <= 4 are declared not allowed (Corollary L, the two kills marked [Sun(5)]). No Sun(6) or Sun(7).
```

New:

```text
Direct Sun instances: Sun(2), Sun(3) through LFC (c) / VFC (V3) (Sun(4) never acts as the excluding instance);
Sun(5) directly exactly in the no-5-set clause of the two/four rule below, used only in Corollary L, for the
feasibility of y = 1/4 in 44444 and for the kills of 44441 and 44444 (this is the locally accepted, computer-assisted
record `six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md`, sha256
2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301). The consequence "at least two entries 4" of
Corollary L uses only the b <= 1 kills (Sun(2), Sun(3)). Transitive: through LFC/INV/E8, VFC, D23-MIX and RICH the
closure reaches the computer-assisted Sun(5) and Sun(6) records 2cf02436...5301 and efe1d849...1e29
(`sun-coset6-parent-gate-verdict-v1.md`). No Sun(7). At a W-apex and at t no W-entry, c or e is divisible by 5, and
Bz Bt = 0; hence 5^Bz and 5^Bt never enter a gcd and are suppressed in labels below.
```

**Item A1.5.** `K7-A1-STRUCT-v1.md`, section 1 proof. Old:

```text
So alpha_uw = 4, but u in W3 has no W-four (R3).
```

New:

```text
So alpha_uw = 4, but u in W3 has no W-four (RICH Corollary R3 (iii)).
```

**Item A1.6.** `K7-A1-STRUCT-v1.md`, section 2 proof. Old:

```text
give >= 4 (E8), y_z = 0, y_t = 1:
```

New:

```text
give >= 4 (E8, subset form as in RICH RF4: the W-label gcds equal the entry gcds; t's label shares no prime with any
W-label, so the allowed sets through t lie in {t, z}; with four neighbours the Sun(5)-dependent branch b >= 4 is
vacuous), y_z = 0, y_t = 1:
```

**Item A1.7.** `K7-A1-STRUCT-v1.md`, section 3 proof (i). Old:

```text
T_2 = lcm(n_u1, n_u2) x_u1u2 with x_u1u2 <= 2, and as in
FG7 each later factor satisfies
```

New:

```text
T_2 = lcm(n_u1, n_u2) x_u1u2 with x_u1u2 <= 2, and by FG7 (a) (RF1; N = Q = W, V_u = U_u of C^x, beta = x <= 5)
each later factor satisfies
```

**Item A1.8.** `K7-A1-STRUCT-v1.md`, section 3 statement (ii). Old:

```text
so S_R contains z and is allowed (VFC (V3)).
```

New:

```text
so S_R contains z and is allowed (VFC (V3)); S_R lies in W cup {z} (apex t) and S_R cap W is an allowed W-set of
y-weight 1.
```

**Item A1.9.** `K7-A1-STRUCT-v1.md`, Corollary L heading. Old:

```text
**Corollary L (allowed t-rows).**
```

New:

```text
**Corollary L (t-rows not excluded by PFG-t: a necessary condition, no realisability claim).**
```

**Item A1.10.** `K7-A1-STRUCT-v1.md`, Corollary L, value-5 list. Old:

```text
and 44444 (y = 1/4):
```

New:

```text
and 44444 (y = 1/4, feasible since no 5-set of fours is allowed [Sun(5)]):
```

**Item A1.11.** `K7-A1-STRUCT-v1.md`, section 4 proof. Old:

```text
- (1,1,1,4): W-alone 3 + 4; (1,1,2,4): 2 + V24(1,1) = 6. Both > 5.
```

New:

```text
- (1,1,1,4): y = 1 on the three ones and the four, 0 on z and t: val = 7. (1,1,2,4): y = 1 on the two ones and the
  four, 0 on the two, z and t (the three positive labels are pairwise coprime): val = 6. Both > 5.
```

**Item A1.12.** `K7-A1-STRUCT-v1.md`, section 4 proof. Old:

```text
- E >= 2, x_ut = 1: the W-part alone has an optimal weight with y_z = 0 of value 5
```

New:

```text
- E >= 2, x_ut = 1: the W-part alone has a feasible weight with y_z = 0 of value 5
```

**Item A1.13.** `K7-A1-STRUCT-v1.md`, section 6 heading. Old:

```text
## 6. OBSTRUCTION: two abstract patterns passing every written rule used so far
```

New:

```text
## 6. OBSTRUCTION (navigation only): two abstract patterns that pass the listed checks of this section only (Pc5' is excluded by K7-TC Proposition TC-P and by K7-TC-A22)
```

**Item TC.1.** `K7-TC-v1.md`, header Status. Old:

```text
- **Status:** CANDIDATE written mathematics, **conditional** on the candidates `K7-D23-RICH-v1.md` (sha256
  ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3) + `K7-D23-RICH-erratum-v1.md` (sha256
  8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69) and `K7-A1-STRUCT-v1.md` (sha256
  c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf; sections 1-5 used: Corollary W3, E3, Lemma B, Theorem
  CASEB). (a1) is NOT excluded; full Sun(7) remains OPEN. The patterns of section 5 are abstract, not group constructions.
```

New:

```text
- **Status:** CANDIDATE written mathematics on the accepted RICH base (verdict sha256
  1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0: RICH-v1 + erratum-1 R-1 + consolidated erratum; FG7 in chain
  form (a)/(b), Corollary 5/6 with the RF2 equality clause), **conditional** on the co-packaged candidate
  `K7-A1-STRUCT-v1.md` (sha256 c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf; section 0 triangle
  evaluation, Corollary W3, E3, Lemma B, Theorem CASEB). (a1) is NOT excluded; full Sun(7) remains OPEN. Sections 5-6
  are navigation only (abstract patterns, not group constructions; no existence or completeness claim).
```

**Item TC.2.** `K7-TC-v1.md`, section 0 imports. Old:

```text
Sun(2)-Sun(5) only through LFC (c)/VFC (V3), FG7 and Corollary 5/6 of RICH (for C^alpha and C^alpha*).
```

New:

```text
direct Sun instances Sun(2), Sun(3) only (through LFC (c)/VFC (V3)); A1-STRUCT's Corollary L enters only through
CASEB's "at least two entries 4", which is Sun(5)-free; transitive closure as in A1-STRUCT section 0 (as amended),
reaching the computer-assisted Sun(5)/Sun(6) records 2cf02436...5301 and efe1d849...1e29; FG7 (b) through Lemma FG-V
(before section 3), and Corollary 5/6 of RICH with its equality clause (for C^alpha and C^alpha*). Orientation
dictionary: in C^alpha* the subgroups are U*_j = g_jU_jg_j^-1 with representatives g*_j = g_j^-1, L*_j^(u) =
g_j^-1 U*_j U*_u, the normalisation g*_a = 1 is the left translation by g_a, and at apex a mu(D*_j) = alpha_aj/6 and
mu(X*_u) = alpha*_au/6.
```

**Item TC.3.** `K7-TC-v1.md`, section 2 heading. Old:

```text
## 2. Rigid rows used (E >= 2 throughout; each value-5 weight is feasible and FG gives <= 5, so it is optimal)
```

New:

```text
## 2. Rigid rows used (R3, R4, R5 and the last item assume E >= 2; R1 holds for every E >= 1, see its last sentence; each value-5 weight is feasible and Corollary 5/6 gives <= 5, so it is optimal)
```

**Item TC.4.** `K7-TC-v1.md`, section 2, R1. Old:

```text
forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.**
```

New:

```text
forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.** *E = 1 (needed only for K7-TC-A22):* the only label gcds at u
  that change are those between z and the two fours, which drop from 4 to 2 (gcd(z, t) = 6 and gcd(z, s) = 2 are
  unchanged); this only removes allowed sets, so y_A and y_B (both vanish on z) stay feasible of value 5, and
  y_A - y_B = (1/2)([f1] - [f2]) still forces L_f1 = L_f2. Hence R1 holds for every E >= 1.
```

**Item TC.5.** `K7-TC-v1.md`, section 2, R4. Old:

```text
Every fibre not containing o contains f1, f2, f3;
```

New:

```text
Every fibre C with S_C non-empty and o not in S_C contains f1, f2, f3;
```

**Item TC.6.** `K7-TC-v1.md`, section 2, R5. Old:

```text
not containing o contains f1 and f2;
```

New:

```text
with S_C non-empty and o not in S_C contains f1 and f2;
```

**Item TC.7.** `K7-TC-v1.md`, before section 3 (insert Lemma FG-V). Old:

```text
## 3. Theorem K7-TC-B (conditional) [NEW]
```

New:

```text
**Lemma FG-V (VFC union bound) [NEW].** Let a in W and C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for
C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C. Then mu(union over j != a of D_j^(a)) <= 5/6.
*Proof.* Put Y := intersection of the U^C_j (j != a). For every j != a, U^C_a Y lies in U^C_a U^C_j = X_j^(a), which
is disjoint from D_j^(a) by (V1); so U^C_a Y avoids the union. G0 gives mu(U^C_a Y) >= 1/gcd(n_a, [G : Y]), and FG7 (b)
(N = Q = V \ {a}, V_j = U^C_j, beta = the alpha-matrix of C, <= 5 by E1, resp. INV (b) with E1) gives
gcd(n_a, [G : Y]) | 6. QED

## 3. Theorem K7-TC-B (conditional) [NEW]
```

**Item TC.8.** `K7-TC-v1.md`, section 3 (i), last sentence. Old:

```text
while FG7 for
C^alpha* at a gives mu(union) <= 5/6.
```

New:

```text
while Lemma FG-V for C^alpha* at a gives mu(union) <= 5/6.
```

**Item TC.9.** `K7-TC-v1.md`, section 3 (ii). Old:

```text
N := the rest outside Z.
```

New:

```text
N := the cosets outside both Z and K.
```

**Item TC.10.** `K7-TC-v1.md`, section 3 (ii), last sentence. Old:

```text
contradicting FG7 for C^alpha* at v.
```

New:

```text
contradicting Lemma FG-V for C^alpha* at v.
```

**Item TC.11.** `K7-TC-v1.md`, section 4 statement. Old:

```text
**The abstract pattern Pc5' of `K7-A1-STRUCT-v1.md` section 6 violates Lemma TC with V4; no configuration has its data.**
```

New:

```text
**No (a1) configuration has alpha-rows ({2,2,4,4} | 3 | 2) at u3 and u5 with fours {u2, u4}, resp. {u4, u1},
together with alpha*_(u4 u1) = alpha*_(u4 u2) = 4 and alpha*_(u4 u3) = alpha*_(u4 u5) = 2; in particular the abstract
pattern Pc5' of `K7-A1-STRUCT-v1.md` section 6 is not realised (also subsumed by K7-TC-A22).**
```

**Item TC.12.** `K7-TC-v1.md`, section 4 proof. Old:

```text
(for K <= 2/6 the second term already gives >= 1; for K >= 2/6 the sum equals 1)
```

New:

```text
(for K <= 2/6 the first two addends K + 2(4/6 - K) = 8/6 - K already give >= 1; for K >= 2/6 the complete bound
equals 1)
```

**Item TC.13.** `K7-TC-v1.md`, section 5 heading. Old:

```text
## 5. Surviving obstruction Q_B' (abstract pattern; not a group construction)
```

New:

```text
## 5. Navigation only: obstruction Q_B' (abstract pattern; not a group construction; no existence or completeness claim)
```

**Item TC.14.** `K7-TC-v1.md`, section 5 counts. Old:

```text
**Counts are satisfiable** (explicit right-coset distributions, measures; every listed S-set is allowed):
```

New:

```text
**Counts (unverified navigation, not premises; no realisability claim)** (explicit right-coset distributions, measures):
```

**Item A22.1.** `K7-TC-A22-v1.md`, header Status. Old:

```text
- **Status:** CANDIDATE, **conditional** on `K7-D23-RICH-v1.md` (ba32d282...f2bb3) + erratum (8261831b...0ba69),
  `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf, sections 1-3: Corollary W3, E3, PFG-t with Corollary L) and `K7-TC-v1.md`
  (cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117: Lemma TC, row R1). It generalises Proposition TC-P of
  K7-TC (the pattern Pc5'). (a1) is NOT excluded; full Sun(7) remains OPEN.
```

New:

```text
- **Status:** CANDIDATE on the accepted RICH base (verdict sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0;
  NO5, FG7, Corollary 5/6 with the RF2 equality clause), **conditional** on the co-packaged candidates
  `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf: section 0 triangle rule, Corollary W3, E3, PFG-t with Corollary L) and
  `K7-TC-v1.md` (cc48340d...e117: Lemma TC, row R1 for every E >= 1 as amended by item TC.4 of
  `K7-A1-A2-delta-erratum-v1.md`). It generalises Proposition TC-P of K7-TC (the pattern Pc5'). (a1) is NOT excluded;
  full Sun(7) remains OPEN. Direct Sun instances: Sun(2), Sun(3) only; Corollary L enters only through "at least two
  entries 4" (Sun(5)-free); transitive closure as in A1-STRUCT section 0 (as amended).
```

**Item A22.2.** `K7-TC-A22-v1.md`, section 1 (b). Old:

```text
The same for alpha* on F.
```

New:

```text
The same argument with alpha*, F* in place of alpha, F shows alpha* != 1 on W.
```

**Item A22.3.** `K7-TC-A22-v1.md`, section 1 (c). Old:

```text
for e = 2 this is R1 of K7-TC;
```

New:

```text
for e = 2 this is R1 of K7-TC, valid for every E >= 1 (K7-TC section 2 as amended; Case A does not force E >= 2 here);
```

**Item A22.4.** `K7-TC-A22-v1.md`, section 1 (d). Old:

```text
Gamma^alpha = F* -complement... precisely {uv : alpha_uv <= 2} = the complement of F, a
5-cycle, is connected
```

New:

```text
Gamma^alpha = {uv : alpha_uv <= 2} is the complement of F among the pairs of W, i.e. the 5-cycle F*, hence connected
```

**Item A22.5.** `K7-TC-A22-v1.md`, section 4 heading. Old:

```text
## 4. Remaining Case A
```

New:

```text
## 4. Remaining Case A (navigation only, not a claim)
```

**Item A2.1.** `K7-A2-FIVE-v1.md`, section 0, label facts. Old:

```text
x_vj in {2, 4}; the w's never enter a gcd (entries <= 5).
```

New:

```text
x_vj in {2, 4}; the w's never enter a gcd (entries <= 5). All statements are for finite G; R0 (LFC verdict item 6,
which preserves alpha and alpha*) lifts each of them to arbitrary G with finite-index subgroups.
**Clique rule.** If labels have pairwise gcd 3, except possibly gcd(t, p) = 15, the allowed sets among them are those of
size <= 3 and the 4-sets containing both t and p (Sun(4)); no 5-set is allowed, since it contains a 4-subset missing t
or p. Weights <= 1/3 on such a clique, with weight 0 on p, are feasible on it.
```

**Item A2.2.** `K7-A2-FIVE-v1.md`, section 0, Sun bullet. Old:

```text
- Direct Sun instances: Sun(2), Sun(3), Sun(4), only through LFC (c). Transitive closure as recorded in the RICH/D23P
  verdict (it reaches the computer-assisted Sun(5)/Sun(6) records). No Sun(7), no computation.
```

New:

```text
- Direct Sun instances in sections 1-4 except Corollary K7-A2-TRANSFER: Sun(2)-Sun(4) only, through LFC (c) and, in
  the bridged Lemma CC, VFC (V3); the E8 standard weights are applied only to at most four neighbours with entries in
  {1,2,4}, where the Sun(5)/Sun(6) branches are vacuous. Corollary K7-A2-TRANSFER additionally uses **Sun(5)
  directly** (A1-STRUCT section 0 / Corollary L: the feasibility of y = 1/4 in 44444 and the kills of 44441 and 44444;
  p may be one of the fours, and its local index 4 5^B w_p keeps every gcd <= 4). Transitive: the computer-assisted
  Sun(5) record (2cf02436...5301) and Sun(6) record (efe1d849...1e29), reached through D23P (ROW-2/E8, D23-CENTER) and
  the LFC/INV provenance. No Sun(7), no computation.
```

**Item A2.3.** `K7-A2-FIVE-v1.md`, (F1) proof. Old:

```text
so an allowed set meeting F5 has its other
positive-weight elements inside F5.
```

New:

```text
so an allowed set meeting F5 has its other positive-weight elements inside F5 (the weights below vanish on t and
p, the only other labels that can carry the prime 5).
```

**Item A2.4.** `K7-A2-FIVE-v1.md`, (F4) proof. Old:

```text
If x_pz = 5: z shares only 5 with t:
```

New:

```text
If x_pz = 5 (vacuous by (F3); kept for completeness): z shares only 5 with t:
```

**Item A2.5.** `K7-A2-FIVE-v1.md`, (F6) last branch. Old:

```text
y = 1/3 on the threes, z and t, y_p = 0 is feasible with val = 17/3 < 6,
```

New:

```text
y = 1/3 on the threes, z and t, y_p = 0 is feasible by the clique rule (section 0) with val = 17/3 < 6,
```

**Item A2.6.** `K7-A2-FIVE-v1.md`, (F7) proof. Old:

```text
standard weights (E8 with N = 4; with four elements only Sun(2)-Sun(4) decide allowedness) have value >= 4;
```

New:

```text
standard weights have value >= 4 (E8 subset form, justified as in RICH RF4: B = W', four unmarked neighbours with
entries in {2,4}, whose label gcds are the entry gcds; the only other positive weight, y_p = 1, sits on a label coprime
to all of B; with |B| = 4 only Sun(2)/Sun(3) decide allowedness inside B);
```

**Item A2.7.** `K7-A2-FIVE-v1.md`, Corollary 5/6-a2 proof. Old:

```text
The proof of RICH Corollary 5/6 (consolidated-erratum form) uses only gcd(n_u, [G : W*]) = 6,
```

New:

```text
The proof of RICH Corollary 5/6 (consolidated-erratum form) uses, besides facts valid in every K7 configuration
(disjointness and the L_j-avoidance of W*U_u, LFC (a)-(c), g_uj = 6 for all j, G0, the RF2 normalisation), only
gcd(n_u, [G : W*]) = 6,
```

**Item A2.8.** `K7-A2-FIVE-v1.md`, (S5) proof. Old:

```text
W*U_z is a union of M left U_z-cosets that contains U_z and meets no g_jU_jU_z
```

New:

```text
W*U_z is a union of M left U_z-cosets that contains U_z (which holds no piece, LFC (b)) and meets no g_jU_jU_z
```

**Item A2.9.** `K7-A2-FIVE-v1.md`, (S5) proof. Old:

```text
Ordering t, p first
and then W' (as in section 2: T_2 = lcm(n_t, n_p) x*_tp, every later k <= 5), the prime-to-30 part of [G : W*] is
w_t w_p (product of the w_u), coprime to w_z,
```

New:

```text
Ordering t, p first and then W' (z is not in the intersection, so T_2 = lcm(n_t, n_p) x*_tp is exact for any x*_tp
and no FG-a2 condition is needed; every later vertex is unmarked, with gcd(n_e, T_m) = 6 and k <= 5), the
prime-to-30 part of [G : W*] is w_t w_p (product of the w_u over u in W'), coprime to w_z (the factor 5^B of
[G : W*] is harmless, n_z being prime to 5),
```

**Item A2.10.** `K7-A2-FIVE-v1.md`, Theorem K7-A2-BRIDGE statement. Old:

```text
**Theorem K7-A2-BRIDGE [NEW].** In (a2-no5) put W := W' cup {p}, T := {j in W : alpha_zj = 3}, T* := {j in W :
alpha*_zj = 3}, and W3, W3* as in RICH with this W. Then every conclusion of K7-D23-RICH (with erratum-1 and the
consolidated erratum) holds: **no (a2-no5) configuration has T* subset W3 or T subset W3***, and G0, Corollary 5/6 at
every u in W (both orientations), NO5, R3 with Corollary R3, TR, CC, TZ (i)-(iii) and LZ hold with this W.
```

New:

```text
**Theorem K7-A2-BRIDGE [NEW].** In (a2-no5) put W := W' cup {p}, T := {j in W : alpha_zj = 3}, T* := {j in W :
alpha*_zj = 3}, and W3, W3* as in RICH with this W. Then the following named RICH claims hold with this W, and only
these: Theorem K7-D23-RICH (**no (a2-no5) configuration has T* subset W3 or T subset W3***); G0; Corollary 5/6 with
its equality clause at every u in W, both orientations; NO5; R3 with S1-S4 as local-test survivors only (RF5) and
Corollary R3; TR; CC (under its separation hypothesis); TZ (i)-(iii); LZ. FG7 is **not** asserted verbatim: its uses
are replaced as in (B3), and the original auxiliary FG7 with arbitrary beta <= 5 is not transferred (for an auxiliary
pair with beta_zt = 5 one gets gcd(n_p, T_{z,t}) = 6 5^min(B, v5 beta_zt) = 30). RICH section 6 (navigation) and
section 9 (residue description) are not transferred.
```

**Item A2.11.** `K7-A2-FIVE-v1.md`, (B2). Old:

```text
(Ones, twos, fours, threes keep their meaning for p.)
```

New:

```text
(Ones, twos, fours, threes keep their meaning for p.) In R3's single-three branches at an apex in W' the
  standard-weight set B (three vertices) may contain p: its label a_p 5^B w_p has the entry gcd with every label of B,
  and the single weighted three (possibly p, label 3 5^B w_p) is coprime to B, so RICH RF4 applies verbatim; at apex
  p, B lies in W'. In every L1 use ell_j = r_j and ell_p = 5^B w_p, so gcd(x, ell_p) = 1 for x <= 4, including TZ (i)
  in the inverted configuration via Z2 G5. VFC local indices r_j q_j use the actual q = x* <= 4 (INV), not arbitrary
  formal q-vectors. The entire gcd matrices, hence the hereditary allowed-set predicates (including sets through
  zero-weight vertices), are preserved.
```

**Item A2.12.** `K7-A2-FIVE-v1.md`, (B3), second sentence. Old:

```text
The other use of FG7, the chain (a) for
  intersections over W in LZ, has every step factor k <= 4 (no fives); when p enters after earlier W'-vertices,
  gcd(n_p, T_m) = 6 because 5 does not divide T_m.
```

New:

```text
The other use of FG7, the chain (a) for intersections over subsets of W (LZ), is replaced by the
  **adapted chain**, valid for the actual subgroup families of the configuration and of its inverse (pair parameters
  <= 4) and, more generally, for any family with beta_jk <= 4: for Q subset W in **any** order j_1, j_2, ...,
  T_2 = lcm(n_j1, n_j2) beta_j1j2 exactly; at each later step gcd(n_e, T_m) = 6 (for unmarked e because w_e is coprime
  to T_m and 6 | T_m; for e = p because no n_j with j != p and no beta <= 4 contains the prime 5), hence k <= beta_ej
  <= 4 for every earlier j, and T_Q = 6 5^(B [p in Q]) (product of the w_j, j in Q) beta_j1j2 (product of the k), so
  v5(T_Q) = B [p in Q]. The prime-to-30 part of T_Q is the product of the original w_j; w'_p = 5^B w_p may be used
  only in the whole-index product, never as a prime-to-30 part. RF8c's reason ("W contains no marked vertex") is false
  in (a2) and is replaced by this paragraph.
```

**Item A2.13.** `K7-A2-FIVE-v1.md`, (B4). Old:

```text
- **(B4)** The D23-MIX conclusion used by RICH (alpha_zu, alpha*_zu in {1,2,3} on W; |T|, |T*| >= 3;
  alpha_zt, alpha*_zt in {1,2}) is Lemma D23-a2 for both orientations.
```

New:

```text
- **(B4)** Lemma D23-a2, in both orientations, replaces every RICH citation of D23-MIX: R3 (c in {1,2,3}, including
  c = x_pz at apex p), TZ (i) (s in {1,2}), TZ (iii) (|T*| >= 3), CC and LZ (alpha_zu, alpha*_zu in {1,2,3} on W;
  |T|, |T*| >= 3; alpha_zt, alpha*_zt in {1,2}).
```

**Item A2.14.** `K7-A2-FIVE-v1.md`, (B5). Old:

```text
- **(B5)** NO5 holds trivially by (B2).
```

New:

```text
- **(B5)** NO5 holds by the definition of (a2-no5); its original five-containing branches (including erratum-1 R-1) are not needed.
```

**Item A2.15.** `K7-A2-FIVE-v1.md`, (B6). Old:

```text
- **(B6)** Where LZ states that 5 does not divide T*_W, this is used only to evaluate g = gcd(n_z, T*_W); in (a2) n_z is
  prime to 5, so g = 3 2^min(1+E, v2(T*_W)) holds although 5^B divides T*_W.
```

New:

```text
- **(B6)** In LZ the adapted chain of (B3) gives T*_W = 6 5^B (product of the w_u, u in W) alpha*_(j1 j2) k_3 k_4
  k_5, so v5(T*_W) = B; RICH's clause "5 does not divide T*_W" is false in (a2) and is withdrawn here. It was used only
  to evaluate g = gcd(n_z, T*_W); n_z = 2^(E+1) 3 w_z is prime to 5 and has v3 = 1, so g = 3 2^min(1+E, v2(T*_W))
  holds. If Gamma*_1 were connected, the spanning-tree order gives T*_W = 6 5^B (product of the w_u), of 2-valuation
  1, as LZ requires.
```

**Item A2.16.** `K7-A2-FIVE-v1.md`, (B7). Old:

```text
- **(B7)** All remaining ingredients (LFC, INV, VFC, L1, G0, Lemma TR, and the VFC count of Lemma CC with local indices
  alpha*_zj r_j) hold for every K7 configuration.
```

New:

```text
- **(B7)** LFC, INV, general VFC counting, L1, G0 and Lemma TR hold for every K7 configuration. In the present
  setting CC's particular weight is feasible by (B1), (B2) and (B4) together with CC's hypothesis D_t cap D_u = empty
  for u in T*: at z the local indices are d_j = alpha*_zj r_j; inside T* their pairwise gcds remain 3, between T* and
  W \ T* they remain 1, the classes of value 1 and 2 keep the gcd-1/gcd-2 constraints CC uses, and there are still
  five W-vertices and one t-vertex, so the weighted mass is 1. CC is not asserted for unrestricted K7 data.
```

**Item A2.17.** `K7-A2-FIVE-v1.md`, Corollary K7-A2-TRANSFER. Old:

```text
**Corollary K7-A2-TRANSFER (conditional on the acceptance of K7-A1-STRUCT sections 1-5, K7-TC and K7-TC-A22).** Their
conclusions hold in (a2-no5) with W := W' cup {p}. *Proof.* They read the same facts (B1)-(B7): the two/four classes and
ones of A1-STRUCT section 0 via (B2) (p's labels are 2^i 5^B w_p or 5^B w_p), its triangle evaluation via (B2) (every ell
of a vertex in W, including ell_p = 5^B w_p, is odd), Corollary 5/6 and FG7 at apexes in W via (B3), and PFG-t (i), whose
statement "5 does not divide T_W" is used only to get gcd(n_t, T_W) = 6, which holds because n_t = 6 3^A w_t is prime to
5 and v3(T_W) = 1 (as in (B6)). QED
```

New:

```text
**Corollary K7-A2-TRANSFER (conditional).** If K7-A1-STRUCT (c8a16f14...), K7-TC (cc48340d...) and K7-TC-A22
(9ebec279...) are accepted as frozen together with the overlay `K7-A1-A2-delta-erratum-v1.md`, then the following
named claims hold in (a2-no5) with W := W' cup {p}, with RICH replaced by Theorem K7-A2-BRIDGE. A1-STRUCT: Corollary
W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem CASEB (with their load-bearing section-0 subroutines).
K7-TC: Lemma TC, Lemma FG-V, rows R1 (every E >= 1), R3, R4, R5 (E >= 2), the exclusion of ({1,4,4,4} | c | 1),
Theorem K7-TC-B, Proposition TC-P for its stated matrix data. K7-TC-A22: Theorem K7-TC-A22. Not transferred:
A1-STRUCT sections 6-7, K7-TC sections 5-6, K7-TC-A22 section 4 (navigation and survivor checks). Any further errata to
these sources require this audit to be redone.
*Proof (dependency-use audit).* (i) Triangle subroutines: entries lie in {1,2,4} and every ell of a vertex in W,
including ell_p = 5^B w_p, is prime to 6 (Corollary W3 needs 3/gcd(3, ell_w) = 3). (ii) Two/four classes and ones:
p's labels and local indices 2^i 5^B w_p and 5^B w_p have the entry gcds (B2); the Sun(5) uses of Corollary L persist
when p is one of the fours (all gcds stay <= 4). (iii) FG7 (b) and Corollary 5/6 at apexes in W: (B3) and Corollary
5/6-a2. (iv) Lemma FG-V at a in W: G0 plus FG-a2 (a) (a in W') or FG-a2 (b) (a = p), applied to the actual subgroups of
C (pair parameters = the alpha-matrix of C, <= 4; the FG-a2 conditions hold since no entry is 5). (v) PFG-t (i): by the
adapted chain of (B3), for every spanning-tree order (p in any position; before p every factor lies in {1,2}, so
gcd(n_p, T_m) = 6), T_W = 6 5^B (product of the w_u) 2^h; so v3(T_W) = 1 and 5^B divides T_W. The source assertion
"5 does not divide T_W" is false here and is deleted; only gcd(n_t, T_W) = gcd(6 3^A w_t, T_W) = 6 is used, which
holds because t carries no 5-marker in (a2). (vi) E3: the standard-weight set B (four W-neighbours) may contain p,
handled as in (F7). (vii) Lemma B, CASEB, the rigid rows (including o = p), TC-B, TC-P and K7-TC-A22: labels and local
indices via (B2), D23-MIX replaced by D23-a2 (B4), union bounds via (iv), V4 counts unchanged. (viii) Sun accounting:
section 0. QED
```

**Item MAN.1.** `delta-package-A1-TC-A22-A2FIVE-v1.md`, item 4. Old:

```text
- **Conditional part:** Corollary K7-A2-TRANSFER only, on items 1-3 of this package.
- **Direct Sun instances:** Sun(2)-Sun(4).
```

New:

```text
- **Conditional part:** Corollary K7-A2-TRANSFER only, on items 1-3 of this package.
- **Direct Sun instances:** Sun(2)-Sun(4) in sections 1-4 (through LFC (c) and VFC (V3)); Corollary K7-A2-TRANSFER
  additionally uses Sun(5) directly (A1-STRUCT Corollary L); the transitive closure reaches the computer-assisted
  Sun(5)/Sun(6) records.
```

## Dependency-transfer re-audit after all items (A1-side changes and Corollary K7-A2-TRANSFER)

| A1-side item | nature of the change | effect on the (a2-no5) transfer (A2.17) | status |
|---|---|---|---|
| A1.4, A1.10 (Sun accounting; 44444 feasibility) | accounting only | direct Sun(5) of Corollary L recorded in A2.2; p may be one of the fours | content unchanged |
| A1.6 (E3 subset form) | justification added | the four-neighbour set B may contain p (A2.17 (vi), as in F7) | transfers |
| A1.7 (PFG-t cites FG7 (a)) | citation | replaced in (a2-no5) by the adapted chain (A2.12); T_W carries 5^B (A2.17 (v)) | transfers with that change |
| A1.8, A1.9 (PFG-t (ii) location; Corollary L necessity wording) | wording | none | unchanged |
| A1.11, A1.12 (Lemma B certificates) | explicit certificates, same values | labels via (B2) | transfers |
| TC.4 (R1 for E = 1) | **materially new proof step** (necessary-test matrix comparison) | marker-independent: only gcd(z, four) changes; p's labels via (B2) | transfers; **conditional pending re-review** |
| TC.5, TC.6 (occupied-fibre qualifier, R4/R5) | logically required restriction; no conclusion changes | none | transfers |
| TC.7, TC.8, TC.10 (Lemma FG-V and its use in TC-B) | **materially new lemma** (explicit union-bound proof) | in (a2-no5): G0 + FG-a2 (a)/(b) for the actual subgroup families (A2.17 (iv)); never the auxiliary FG7 with beta <= 5 | transfers; **conditional pending re-review** |
| TC.9, TC.12 (meaning of N; TC-P parenthesis) | clarification | none | unchanged |
| TC.11 (TC-P scope) | statement narrowed to its matrix data | transfers for the same data | transfers |
| A22.3 (A22 uses R1 at E = 1) | uses TC.4 | as TC.4 | **conditional pending re-review** |
| A1.1-A1.3, A1.5, A1.13, TC.1-TC.3, TC.13, TC.14, A22.1, A22.2, A22.4, A22.5 | status, citation, navigation labels | none (navigation is never transferred) | unchanged |

**Materially changed items.** TC.4 (R1 at E = 1) and TC.7 (Lemma FG-V), together with their uses in TC.8, TC.10 and
A22.3, are new proof steps. Until they are re-reviewed, Theorem K7-TC-B, Theorem K7-TC-A22 and the corresponding parts of
Corollary K7-A2-TRANSFER remain conditional on them. On the A2 side, A2.10 and A2.12 change the scope of
Theorem K7-A2-BRIDGE (enumerated claims; adapted chain for actual families or beta <= 4) and A2.17 restricts the
transfer; the proofs of Lemma F, FG-a2, Corollary 5/6-a2, D23-a2 and Proposition K7-A2-ZT5 are unchanged apart from the
added citations (A2.1, A2.3-A2.9).

## Unchanged
All other text of the four candidates and of the manifest. Navigation sections (A1-STRUCT sections 6-7, K7-TC sections
5-6, K7-TC-A22 section 4) carry no claim. (a1), (a2), K6.2*, full K7 and Sun(7) remain OPEN. No novelty, Lean or
human-review claim.
