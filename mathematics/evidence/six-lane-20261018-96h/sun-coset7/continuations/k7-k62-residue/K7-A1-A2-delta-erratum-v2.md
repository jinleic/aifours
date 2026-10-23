# K7-A1-A2-delta-erratum-v2: final review-requested Old/New overlay

- Written: 2026-10-19T08:23:31-0700 (`/bin/date` immediately before this exclusive create).
- Owner: Sun7K62Successor. No original or previous overlay is overwritten.
- Primary target: `D/K7-A1-A2-delta-erratum-v1.md` `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`. The one direct-original replacement V2.2 targets `D/K7-TC-v1.md` `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`.
- Reviews: Claude `R/sun7-K7-A1-A2-repair-claude-v1.prompt.note.md` `66c93000ab9a35aaa34b004e6262e82b698dd657dd283c613366d91dd4bf8157`; Codex `R/sun7-K7-A1-A2-repair-codex-v1.prompt.stdout.txt` `1697abdf74e577e7ec9ab673bb50b3161bfce6b836816e602536a1f45af4ecde`.
- Read order: apply the literal replacements targeting v1 to that overlay first, then read its amended instructions
  against their frozen originals; apply V2.2 directly to TC as well. All unlisted v1 replacements remain in force.
  TC.11's stated matrix-data hypotheses are unchanged. Items below contain only verbatim Old/New replacements.

## V2.1 — Claude ED-1; Item A1.6 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
give >= 4 (E8, subset form as in RICH RF4: the W-label gcds equal the entry gcds; t's label shares no prime with any
W-label, so the allowed sets through t lie in {t, z}; with four neighbours the Sun(5)-dependent branch b >= 4 is
vacuous), y_z = 0, y_t = 1:
````

New:

````text
give >= 4 (E8, subset form as in RICH RF4: the W-label gcds equal the entry gcds; t's label shares no prime with any
W-label, so the allowed sets through t lie in {t, z}; with four neighbours no 5-subset of the class exists, so no Sun(5)/Sun(6) instance enters), y_z = 0, y_t = 1:
````

## V2.2 — optional R1 list tag; original TC section 2

Target: `D/K7-TC-v1.md`.

Old:

````text
twos s1, s2. Maximal allowed sets: {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
````

New:

````text
twos s1, s2. Maximal allowed sets (E >= 2): {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
````

## V2.3 — optional finite-G note; Item TC.7 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
**Lemma FG-V (VFC union bound) [NEW].** Let a in W and C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for
C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C. Then mu(union over j != a of D_j^(a)) <= 5/6.
````

New:

````text
**Lemma FG-V (VFC union bound) [NEW].** Work in finite G (R0 lifts the statement to arbitrary G). Let a in W and
C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C.
Then mu(union over j != a of D_j^(a)) <= 5/6.
````

## V2.4 — Codex M1; Item TC.9 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
N := the cosets outside both Z and K.
````

New:

````text
N := mathcalU \ (Z cup K), where mathcalU := union over j != v of D*_j (the occupied union).
````

## V2.5 — Claude AUX-1; Item A2.11 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
(Ones, twos, fours, threes keep their meaning for p.) In R3's single-three branches at an apex in W' the
  standard-weight set B (three vertices) may contain p: its label a_p 5^B w_p has the entry gcd with every label of B,
  and the single weighted three (possibly p, label 3 5^B w_p) is coprime to B, so RICH RF4 applies verbatim; at apex
  p, B lies in W'. In every L1 use ell_j = r_j and ell_p = 5^B w_p, so gcd(x, ell_p) = 1 for x <= 4, including TZ (i)
  in the inverted configuration via Z2 G5. VFC local indices r_j q_j use the actual q = x* <= 4 (INV), not arbitrary
  formal q-vectors. The entire gcd matrices, hence the hereditary allowed-set predicates (including sets through
  zero-weight vertices), are preserved.
````

New:

````text
(Ones, twos, fours, threes keep their meaning for p.) In R3's single-three branches at an apex in W' the
  standard-weight set B (three vertices) may contain p: its label a_p 5^B w_p has the entry gcd with every label of B,
  and the single weighted three (possibly p, label 3 5^B w_p) is coprime to B, so RICH RF4 applies verbatim; at apex
  p, B lies in W'. In every L1 use ell_j | r_j (so ell_p | 5^B w_p), so gcd(x, ell_p) = 1 for x <= 4, including TZ (i)
  in the inverted configuration via Z2 G5. VFC local indices r_j q_j use the actual q = x* <= 4 (INV), not arbitrary
  formal q-vectors. The entire gcd matrices, hence the hereditary allowed-set predicates (including sets through
  zero-weight vertices), are preserved.
````

## V2.6 — Codex M2; Claude AUX-2 and requested AUX-3; Item A2.12 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
The other use of FG7, the chain (a) for intersections over subsets of W (LZ), is replaced by the
  **adapted chain**, valid for the actual subgroup families of the configuration and of its inverse (pair parameters
  <= 4) and, more generally, for any family with beta_jk <= 4: for Q subset W in **any** order j_1, j_2, ...,
  T_2 = lcm(n_j1, n_j2) beta_j1j2 exactly; at each later step gcd(n_e, T_m) = 6 (for unmarked e because w_e is coprime
  to T_m and 6 | T_m; for e = p because no n_j with j != p and no beta <= 4 contains the prime 5), hence k <= beta_ej
  <= 4 for every earlier j, and T_Q = 6 5^(B [p in Q]) (product of the w_j, j in Q) beta_j1j2 (product of the k), so
  v5(T_Q) = B [p in Q]. The prime-to-30 part of T_Q is the product of the original w_j; w'_p = 5^B w_p may be used
  only in the whole-index product, never as a prime-to-30 part. RF8c's reason ("W contains no marked vertex") is false
  in (a2) and is replaced by this paragraph.
````

New:

````text
For the actual subgroup families of an (a2-no5) configuration and its inverse, all pair parameters are <= 4.
  For every non-empty Q subset V, order its members z (if present), t (if present), then the members of Q cap W in
  any order (p anywhere among them). This gives the adapted FG7 (a)/(b), reading "unmarked" as "in W": T_1 = n_j1;
  if z and t are both present, T_2 = lcm(n_z, n_t) beta_zt exactly; every other entering e is in W and has
  gcd(n_e, T_m) = 6, so T_(m+1) = lcm(n_e, T_m) k with k <= beta_ej <= 4 for every earlier j (at the second vertex,
  k = beta_j1e). The prime-to-30 part of T_Q is the product of the original w_j (j in Q), v5(T_Q) = B [p in Q], and
  if u in W \ Q then gcd(n_u, T_Q) divides 6. For Q empty set T_Q = 1; for Q = {j}, T_Q = n_j. Thus the actual-family
  chain supplies the needed FG7 conclusions for every Q without relying on an inventory of the earlier proof's uses.
  The auxiliary **adapted chain** over W is valid, more generally, for any subgroup family with [G : V_j] = n_j and
  beta_jk <= 4: for Q subset W, set T_empty = 1 and T_{j} = n_j for a singleton; the following first-pair formulas
  apply only when |Q| >= 2. In any order j_1, j_2, ..., T_2 = lcm(n_j1, n_j2) beta_j1j2 exactly. At every later step,
  gcd(n_e, T_m) = 6 (for unmarked e because w_e is coprime to T_m and 6 | T_m; for e = p because no earlier n_j
  (j != p), no beta <= 4 and no earlier k (each <= 4) contains the prime 5), hence k <= beta_ej <= 4 for every earlier
  j. For |Q| >= 2,
  T_Q = 6 5^(B [p in Q]) (product of the w_j, j in Q) beta_j1j2 (product of the k), so v5(T_Q) = B [p in Q].
  The prime-to-30 part of T_Q is the product of the original w_j; w'_p = 5^B w_p may be used only in the whole-index
  product, never as a prime-to-30 part. RF8c's reason ("W contains no marked vertex") is false in (a2) and is replaced
  by this paragraph. The old auxiliary FG7 with arbitrary beta <= 5 is not transferred.
````

## V2.7 — Claude AUX-1, TR-1, TR-2, TR-3; Item A2.17 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
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
````

New:

````text
**Corollary K7-A2-TRANSFER (conditional).** If K7-A1-STRUCT (c8a16f14...), K7-TC (cc48340d...) and K7-TC-A22
(9ebec279...) are accepted as frozen together with `K7-A1-A2-delta-erratum-v1.md` as amended by
`K7-A1-A2-delta-erratum-v2.md`, then the following named claims hold in (a2-no5) with W := W' cup {p}, with RICH
replaced by Theorem K7-A2-BRIDGE. A1-STRUCT: Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem
CASEB (with their load-bearing section-0 subroutines). K7-TC: Lemma TC, Lemma FG-V; row R1 (every E >= 1); rows R3,
R4, R5 and the exclusion of ({1,4,4,4} | c | 1) (each for E >= 2); Theorem K7-TC-B; Proposition TC-P for its stated
matrix data. K7-TC-A22: Theorem K7-TC-A22. Not transferred: A1-STRUCT sections 6-7, K7-TC sections 5-6, K7-TC-A22
section 4 (navigation and survivor checks). Any further errata to these sources require this audit to be redone.
*Proof (dependency-use audit).* (i) Triangle subroutines: entries lie in {1,2,4}, and ell_j | r_j for j in W (so
ell_p | 5^B w_p); every such ell is prime to 6 (Corollary W3 needs 3/gcd(3, ell_w) = 3). (ii) Two/four classes and ones:
p's labels and local indices 2^i 5^B w_p and 5^B w_p have the entry gcds (B2); the Sun(5) uses of Corollary L persist
when p is one of the fours (all gcds stay <= 4). (iii) FG7 (b) and Corollary 5/6 at apexes in W: (B3) and Corollary
5/6-a2. (iv) Lemma FG-V at a in W: G0 plus FG-a2 (a) (a in W') or FG-a2 (b) (a = p), applied to the actual subgroups
of C (pair parameters = the alpha-matrix of C, <= 4; the FG-a2 conditions hold since no entry is 5 and, for (b),
beta_zu <= 3 on W' by D23P for the alpha-matrix of C). (iv') For every E >= 1, at an apex in W (p included, also as
apex), a row ({2,2,4,4} | 3 | e) with e in {1,2} has the (a1) gcd matrix with Bz = Bt = 0 for the same E (B1, B2).
So y_A, y_B (TC.4, for e = 2) and y1, y2 (A22 1(c), for e = 1) are feasible with value 5, and Corollary 5/6-a2 with
its occupied-fibre clause gives L_f1 = L_f2. (v) PFG-t (i): by the adapted chain of (B3), for every spanning-tree order
(p in any position; before p every factor lies in {1,2}, so gcd(n_p, T_m) = 6), T_W = 6 5^B (product of the w_u) 2^h;
so v3(T_W) = 1 and 5^B divides T_W. The source assertion "5 does not divide T_W" is false here and is deleted; only
gcd(n_t, T_W) = gcd(6 3^A w_t, T_W) = 6 is used, which holds because t carries no 5-marker in (a2). (vi) E3: the
standard-weight set B (four W-neighbours) may contain p, handled as in (F7). (vii) Lemma B, CASEB, the rigid rows
(including o = p), TC-B, TC-P and K7-TC-A22: labels and local indices via (B2), D23-MIX replaced by D23-a2 (B4), union
bounds via (iv), V4 counts unchanged. (viii) Sun accounting: section 0. QED
````

## V2.8 — Codex M3 and Claude TR-4; replace Item TC.12 in full

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
**Item TC.12.** `K7-TC-v1.md`, section 4 proof. Old:

```text
(for K <= 2/6 the second term already gives >= 1; for K >= 2/6 the sum equals 1)
```

New:

```text
(for K <= 2/6 the first two addends K + 2(4/6 - K) = 8/6 - K already give >= 1; for K >= 2/6 the complete bound
equals 1)
```
````

New:

````text
**Item TC.12.** `K7-TC-v1.md`, section 4 proof (entire proof; Codex M3, replacing the former arithmetic parenthesis). Old:

```text
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
```

New:

```text
*Proof.* At u3 the stated alpha-row is R1, valid for every E >= 1 by TC.4, and gives
L_u2^(u3) = L_u4^(u3). Lemma TC at apex u4 in C^alpha therefore gives D_u2 cap D_u3 = empty. At that apex the stated
alpha* values give mu(D_u2) = alpha*_(u4 u2)/6 = 4/6 and mu(D_u3) = alpha*_(u4 u3)/6 = 2/6. Their disjoint union has
measure 1, but V4 says it avoids U_u4, a set of positive measure. Contradiction. QED
```
````

## V2.9 — Claude TR-4; dependency-table TC.11 row

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
| TC.11 (TC-P scope) | statement narrowed to its matrix data | transfers for the same data | transfers |
````

New:

````text
| TC.11 (TC-P scope) | generalised; every E≥1 via TC.4 | transfers for the same stated matrix data; minimal TC.12 proof uses only the u3 R1 row, two alpha* masses and V4 | transfers |
````

## V2.10 — Claude TR-4; disposition scope label

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
**Statement scope changes (all reviewer-requested; no theorem redesign):** TC-P is restated for its exact matrix data
(TC.11); R1 is extended to every E >= 1 with a written proof (TC.4); Theorem K7-A2-BRIDGE is narrowed to an enumerated list
(A2.10); Corollary K7-A2-TRANSFER is restricted to named claims (A2.17). Every other conclusion is unchanged.
````

New:

````text
**Statement scope changes (all reviewer-requested; no theorem redesign):** TC-P is generalised; every E≥1 via TC.4,
for its stated matrix data (TC.11); R1 is extended to every E >= 1 with a written proof (TC.4); Theorem K7-A2-BRIDGE is
narrowed to an enumerated list (A2.10); Corollary K7-A2-TRANSFER is restricted to named claims (A2.17). Every other
conclusion is unchanged.
````

## V2.11 — Codex M1/M3; dependency-table TC.9/TC.12 row

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
| TC.9, TC.12 (meaning of N; TC-P parenthesis) | clarification | none | unchanged |
````

New:

````text
| TC.9, TC.12 (occupied remainder N; minimal TC-P proof) | clarification and proof replacement, with the TC.11 statement unchanged | N is restricted to the occupied union; TC-P transfers by the same u3 R1 row and two alpha* masses | transfers |
````

