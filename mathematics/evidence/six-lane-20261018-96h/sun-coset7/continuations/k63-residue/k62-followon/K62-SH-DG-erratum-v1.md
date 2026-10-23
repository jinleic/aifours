# K62-SH-DG-erratum-v1: one combined overlay disposing the dual review of K62-SH and K62-DG (no statement broadened)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:37:32-0700.
- **Overlays (frozen, unchanged):** `K62-SH-v1.md` sha256 4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a;
  `K62-DG-v1.md` sha256 a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52; `K62-DG-erratum-v1.md` sha256
  e435430c6d4ff855871dfa7a9004757561435821dae8f53e7304b10e64626801 (which stays in force).
- **Responds to:** review freeze `RUN/review/sun7-K62-SH-DG-review-freeze-v1.json` (sha256
  182a817a2c100843655d8d33434935e611e835cdaf9afca421c3f2b6bbdba3a7); Codex `RUN/review/sun7-K62-SH-DG-codex-v1.prompt.stdout.txt`
  (sha256 b79975a4babf80a56945714d42626f15c02c2903040cd92bea76307ffefa578e; ACCEPT-WITH-FIXES, 0/0/3); Claude
  `RUN/review/sun7-K62-SH-DG-claude-v1.prompt.note.md` (sha256 a7af8f2db638b2d795d3c0da5bc9174c97d8e98e62daee18eb4e2389ad904009;
  ACCEPT-WITH-FIXES, SH 0/0/3, DG 0/0/5), relayed by the parent with the instruction: one combined erratum, no broader
  theorem, elementary derivations replacing the unembedded L1/V1/V3 imports, explicit Sun(5)/(6) provenance.
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Rule.** Every Old block below is an exact substring of the named frozen file and was checked, before this file was
  created, to occur there exactly once. No theorem, lemma or corollary statement is broadened; the only statement-level
  changes are scope narrowings (S5, G7) and the arithmetic/wording corrections G5, G6.

## Disposition table
| finding | item |
|---|---|
| Codex MINOR 1 (SH scope) | S5 |
| Codex MINOR 2 (DG (a) arithmetic) | G5 |
| Codex MINOR 3 (defined P_ob vs marker extension) | G7 |
| Claude SH-m1 (provenance) | S1 |
| Claude SH-m2 (SH-1 (b), SH-2 details) | S2, S3 |
| Claude SH-m3 (set inverses; fibre union) | S3, S4 |
| Claude DG-m1 (provenance) | G1 |
| Claude DG-m2 (citations; DG-3 derivation; no normality) | G1, G2, G3 |
| Claude DG-m3 (power of 2; arithmetic; "exactly 5") | G4, G5, G6 |
| Claude DG-m4 (LFC replaces (V1)/(V3); rotation) | G8 |
| Claude DG-m5 (erratum v1 was a real gap repair; scope wording) | G7 and the note below |
| Codex items 10-11 (conditionality of DG (b); P_ob proof) | note below |

## S1: SH premises: Sun instances and Sun(5)/(6) provenance
*File:* `K62-SH-v1.md`. *Disposes:* Claude SH-m1; parent request.

**Old:**
```text
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1 (1 <= alpha <= g - 1); LFC (a)-(d), INV (a)-(b)
  with E6 (verdict 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); K62-E3 Lemma 1 and the facts of its
  proof steps 1-3 (accepted verdict above): after inversion if necessary, **alpha_(d i*) = 1**; then (g_d = 1) every
  fibre F != U_d (left coset of U_d) has |S_F| <= 3, the sum of |S_F| is 11 n_d / 4, and for every c in O the set
  L_c = g_cU_cU_d is disjoint from U*_cU_d (U*_j := g_jU_jg_j^-1). Sun instances: only those inside these imports
  (Sun(4) via K62-E3 step 2). **Not used:** VFC, TG, CLIQUE, the T rule, RPLP, F7 (re-derived below by granularity),
  any computation.
```

**New:**
```text
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1 (1 <= alpha <= g - 1); LFC (a)-(d), INV (a)-(b)
  with E6 (verdict 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); K62-E3 Lemma 1 and the facts of its
  proof steps 1-3 (accepted verdict above): after inversion if necessary, **alpha_(d i*) = 1**; then (g_d = 1) every
  fibre F != U_d (left coset of U_d) has |S_F| <= 3, the sum of |S_F| is 11 n_d / 4, and for every c in O the set
  L_c = g_cU_cU_d is disjoint from U*_cU_d (U*_j := g_jU_jg_j^-1). **Sun instances and provenance:** LFC (c) is invoked
  only at |T| = 4 (Sun(4), through K62-E3 step 2). Sun(5) and Sun(6) are not directly invoked; the accepted LFC package's
  proof of (c) cites Sun(|T|) for |T| <= 6, so its provenance, including the accepted computer-assisted Sun(5) and
  Sun(6), remains in this file's import closure (as recorded in the LFC/INV and K62-E3 verdicts), as does the global class
  reduction; no claim is made that the import closure avoids Sun(5) or Sun(6). **Not used:** VFC, TG, CLIQUE, the T rule,
  RPLP, F7 (re-derived below by granularity), any computation.
```

## S2: SH-1 proof: disjointness for i* written out; U*_d = U_d
*File:* `K62-SH-v1.md`. *Disposes:* Claude SH-m2 (first clause).

**Old:**
```text
*Proof.* mu(L_c) = t_c / n_d = alpha_dc / g_dc = 1/2 (LFC (a)-(b)); by L0.1, mu(U*_cU_d) = [G : U*_c cap U_d]/(n_c n_d) =
alpha*_dc / g_dc = 1/2; disjointness is K62-E3 step 3 (its argument uses only w in U*_c). (b): the same disjointness
argument with i* in place of c, and mu(U*_(i*)U_d) = alpha*_(d i*)/g_(d i*) by L0.1. QED
```

**New:**
```text
*Proof.* mu(L_c) = t_c / n_d = alpha_dc / g_dc = 1/2 (LFC (a)-(b)); by L0.1, mu(U*_cU_d) = [G : U*_c cap U_d]/(n_c n_d) =
alpha*_dc / g_dc = 1/2 (g_d = 1, so the d-subgroup of the inverted family is U_d itself); disjointness is K62-E3 step 3 (its
argument uses only w in U*_c). (b) Disjointness, written out: if w u lies in L_(i*) with w in U*_(i*) and u in U_d, then
w = (w u) u^-1 lies in L_(i*)U_d = L_(i*) = g_(i*)U_(i*)U_d; writing w = g_(i*) a g_(i*)^-1 with a in U_(i*), a g_(i*)^-1 lies in
U_(i*)U_d, so g_(i*)^-1 lies in a^-1 U_(i*)U_d = U_(i*)U_d, i.e. g_(i*) lies in U_dU_(i*), i.e. g_(i*)U_(i*) meets U_d = g_dU_d,
contradicting disjointness. mu(U*_(i*)U_d) = [G : U*_(i*) cap U_d]/(n_(i*) n_d) = alpha*_(d i*)/g_(d i*) by L0.1. QED
```

## S3: SH-2 (a): gcd details; set inverses
*File:* `K62-SH-v1.md`. *Disposes:* Claude SH-m2 (second clause), SH-m3 (first clause).

**Old:**
```text
(a) mu(Z) >= lcm(n_d, J)/(n_d J) = 1/gcd(n_d, J), and gcd(n_d, J) = 2^(min(e_d, 2 + v2 a)) 5^(min(h_d, max(h*, h_c) + v5 a))
= 4 under the hypotheses (a odd; if h_d >= 1 then h* = h_c = 0 and 5 does not divide a). So mu(Z) >= 1/4 =
mu(U_dU*_(i*)); Z lies in U_dU*_(i*), so Z = U_dU*_(i*) (finite sets), and U_dU*_(i*) lies in U_dU*_c. Invert.
```

**New:**
```text
(a) mu(Z) >= lcm(n_d, J)/(n_d J) = 1/gcd(n_d, J), and gcd(n_d, J) = 2^(min(e_d, 2 + v2 a)) 5^(min(h_d, max(h*, h_c) + v5 a))
= 4 under the hypotheses (a odd; if h_d >= 1 then h* = h_c = 0 and 5 does not divide a). Here v2 J = 2 + v2 a uses e* = 2 and
e_c = 1; the 3-part of the gcd is trivial because f_d = 0; the w-part is trivial because a <= 5 and the w's are pairwise
coprime and prime to 30. So mu(Z) >= 1/4 = mu(U_dU*_(i*)); Z lies in U_dU*_(i*), so Z = U_dU*_(i*) (finite sets), and
U_dU*_(i*) lies in U_dU*_c. Taking set inverses (not the configuration inversion INV): U*_(i*)U_d lies in U*_cU_d.
```

## S4: SH (i) proof: U*_(i*)U_d is a union of n_d/4 fibres
*File:* `K62-SH-v1.md`. *Disposes:* Claude SH-m3 (second clause).

**Old:**
```text
*Proof of (i).* Write B(F) := O minus S_F. Then sum_F |B(F)| = 5 n_d - 5 n_d / 2 = 5 n_d / 2, so
sum_F (|B(F)| - 2) = n_d / 2, and every term is >= 0 (|S_F| <= 3; B(U_d) = O). The n_d / 4 fibres met by g_(i*)U_(i*)
(LFC (b); U_d is not among them) have |S_F cap O| <= 2, so their terms are >= 1. By SH-1 (b) the n_d / 4 fibres
contained in U*_(i*)U_d are disjoint from L_(i*), hence distinct from those; U_d is one of them (term 3); and by SH-2 (a)
and SH-1 (a) each of them lies in G minus L_c for every c in Odd*, so |B(F)| >= |Odd*|. If |Odd*| >= 3, the sum is
>= n_d/4 + 3 + (n_d/4 - 1) = n_d/2 + 2 > n_d/2. (ii) is SH-2 (b). QED
```

**New:**
```text
*Proof of (i).* Write B(F) := O minus S_F. Then sum_F |B(F)| = 5 n_d - 5 n_d / 2 = 5 n_d / 2, so
sum_F (|B(F)| - 2) = n_d / 2, and every term is >= 0 (|S_F| <= 3; B(U_d) = O). The n_d / 4 fibres met by g_(i*)U_(i*)
(LFC (b); U_d is not among them) have |S_F cap O| <= 2, so their terms are >= 1. The set U*_(i*)U_d is right
U_d-invariant of measure alpha*_(d i*)/4 = 1/4 (SH-1 (b)), hence the union of n_d / 4 fibres; by SH-1 (b) these are
disjoint from L_(i*), hence distinct from the fibres met by g_(i*)U_(i*); U_d is one of them (term 3); and by SH-2 (a)
and SH-1 (a) each of them lies in G minus L_c for every c in Odd*, so |B(F)| >= |Odd*|. If |Odd*| >= 3, the sum is
>= n_d/4 + 3 + (n_d/4 - 1) = n_d/2 + 2 > n_d/2. (ii) is SH-2 (b). QED
```

## S5: SH section 4 scope wording
*File:* `K62-SH-v1.md`. *Disposes:* Codex MINOR 1.

**Old:**
```text
Partial necessary conditions on the i*-rows; **no sub-case of the residue is excluded by this file alone.**
```

**New:**
```text
Partial necessary conditions on the i*-rows. **No entire exponent/marker-placement regime of the residue is proved
empty by this file; the i*-row patterns violating (i), (ii) or (iii) are excluded.**
```

## G1: DG premises: L1/VFC citations withdrawn; Z10/Z11 citations; Sun provenance
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m1, DG-m2; parent request.

**Old:**
```text
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1; LFC (a)-(d), INV (a)-(b) with E6 (verdict
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); rules-k7-v1 L1 (T rule: (T1), (T3), tau_min, tau_max)
  and VFC (V1)-(V4), accepted in `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` (sha256
  73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35), applied to the configuration or to its inverted
  configuration (INV (a): again a configuration with the same indices); K62-E3 with errata v1-v2 (accepted): Lemma 1,
  Lemma 2, Lemma 3 in the proof form for every non-empty Q (erratum v2 Z10), steps 1-3, and the C2 sub-claim (a)
  (alpha, alpha* in {1, 2, 4} on O-O pairs). Sun instances: Sun(3) via (V3) in section 5 only; others only inside the
  accepted imports. **Not used:** K62-FG, K62-R2, K62-SH, RPLP, TG, F7 as an import (containments are re-derived),
  any probe output.
```

**New:**
```text
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1; LFC (a)-(d), INV (a)-(b) with E6 (verdict
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); K62-E3 with errata v1-v2 (accepted, verdict above):
  Lemma 1, Lemma 2, Lemma 3 in the proof form for every non-empty Q contained in O (erratum v2 Z10; the chain works verbatim
  for |Q| <= 3: marked vertices first, each later unmarked step multiplies by k <= alpha*_(ej) in {1, 2, 4}), steps 1-3, and
  the C2 sub-claim (a) of erratum v2 Z11 (alpha, alpha* in {1, 2, 4} on O-O pairs). **The earlier citations of
  rules-k7-v1 L1 and VFC (V1)-(V4) are withdrawn:** the triangle identities used are derived in DG-3 from L0.1 and
  Lagrange, and the allowed-set step of section 5 is derived from LFC (c) of the original configuration (section 5
  step 2). **Sun instances and provenance:** LFC (c) is invoked only at |T| = 2 (Sun(2), through K62-E3 Lemma 2 and
  Z11 (a)), |T| = 3 (Sun(3), section 5 step 2) and |T| = 4 (Sun(4), through K62-E3 Lemma 1 and step 2). Sun(5) and
  Sun(6) are not directly invoked; the accepted LFC package's proof of (c) cites Sun(|T|) for |T| <= 6, so its provenance,
  including the accepted computer-assisted Sun(5) and Sun(6), remains in this file's import closure, as does the global
  class reduction; no claim is made that the import closure avoids them. **Not used:** K62-FG, K62-R2, K62-SH, RPLP, TG,
  F7 as an import, any probe output.
```

## G2: DG-1 proof: no normality; alpha_(d i*) = 1 not used
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m2 (last clause).

**Old:**
```text
*Proof.* For c in O, L_c := g_cU_cU_d is a union of fibres of measure alpha_dc/g_dc = 1/2 (LFC (a)-(b)); U*_cU_d has
measure [G : U*_c cap U_d]/(n_c n_d) = alpha*_dc/g_dc = 1/2 (L0.1) and is disjoint from L_c (K62-E3 step 3, whose argument
uses only w in U*_c). Hence U*_cU_d = G minus L_c, and c is in B(F) iff F lies in U*_cU_d. So N(Q) = n_d mu(Z_Q) with
Z_Q := intersection of U*_cU_d (c in Q). Z_Q is left W*_Q-invariant and right U_d-invariant, hence a union of double
cosets W*_Q x U_d, each of measure [G : W*_Q cap xU_dx^-1]/(T*_Q n_d), a multiple of 1/gcd(T*_Q, n_d) (L0.1, Lagrange).
gcd(n_d, T*_Q) = 2^(min(e_d, v2 T*_Q)) by K62-E3 Lemma 3 (proof form for Q). N(Q) >= 1 since U_d lies in Z_Q. QED
```

**New:**
```text
*Proof.* For c in O, L_c := g_cU_cU_d is a union of fibres of measure alpha_dc/g_dc = 1/2 (LFC (a)-(b)); U*_cU_d has
measure [G : U*_c cap U_d]/(n_c n_d) = alpha*_dc/g_dc = 1/2 (L0.1) and is disjoint from L_c (K62-E3 step 3, whose argument
uses only w in U*_c). Hence U*_cU_d = G minus L_c, and c is in B(F) iff F lies in U*_cU_d. So N(Q) = n_d mu(Z_Q) with
Z_Q := intersection of U*_cU_d (c in Q). Z_Q is left W*_Q-invariant and right U_d-invariant, hence a disjoint union of
double cosets W*_Q x U_d. By L0.1, |W*_Q x U_d| = |W*_Q| |U_d| / |W*_Q cap xU_dx^-1|, so its measure is
[G : W*_Q cap xU_dx^-1]/(T*_Q n_d), and this index is divisible by T*_Q and by [G : xU_dx^-1] = n_d (Lagrange; no normality is
used): a positive multiple of 1/gcd(T*_Q, n_d). gcd(n_d, T*_Q) = 2^(min(e_d, v2 T*_Q)) by the K62-E3 Lemma 3 chain for Q
(erratum v2 Z10). N(Q) >= 1 since U_d lies in Z_Q. DG-1 does not use alpha_(d i*) = 1. QED
```

## G3: DG-3: elementary derivation replacing L1; admissible tau* listed
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m2; Codex item 7.

**Old:**
```text
(DG-3) For a 3-subset R of O with alpha*-values x1 <= x2 <= x3 on its edges: v2(T*_R) = 1 + v2(tau*_R), where tau*_R
is a multiple of lcm(x1, x2, x3) with tau*_R <= x1 x2. Hence **v2(T*_R) <= 3 unless (x1, x2, x3) is (2,4,4) or (4,4,4)**.
*Proof.* L1 for the inverted configuration: T*_R = lcm(n_a, n_b, n_c) tau*_R and v2(lcm) = 1 (e_c = 1 on O). Here g = gamma = 6
and ell_z = n_z/6 is odd, so gcd(x, ell_z) = 1 for x in {1, 2, 4} (C2 sub-claim (a)): (T1) gives x | tau* for each edge,
and tau_max = min over apexes of x_opp * min(other two) = x1 x2. A multiple of 8 is <= x1 x2 only if x1 x2 >= 8. QED
```

**New:**
```text
(DG-3) For a 3-subset R = {a, b, c} of O with alpha*-values x1 <= x2 <= x3 on its edges: v2(T*_R) = 1 + v2(tau*_R), where
tau*_R := T*_R / lcm(n_a, n_b, n_c) is a multiple of lcm(x1, x2, x3) with tau*_R <= x1 x2. Hence **v2(T*_R) <= 3 unless
(x1, x2, x3) is (2,4,4) or (4,4,4)**; the admissible tau* are {4, 8} for (2,4,4) and {4, 8, 12, 16} for (4,4,4).
*Proof (elementary; replaces the citation of L1).* Write n_j = 6 ell_j (j in O); the ell_j are odd and pairwise coprime,
markers included. T*_R is divisible by every n_j (Lagrange), hence by their lcm 6 ell_a ell_b ell_c: T*_R = 6 ell_a ell_b ell_c tau*_R.
T*_R is also divisible by [G : U*_a cap U*_b] = lcm(n_a, n_b) x_ab = 6 ell_a ell_b x_ab, so x_ab divides ell_c tau*_R; since x_ab is in
{1, 2, 4} (Z11 (a)) and ell_c is odd, x_ab divides tau*_R; likewise for the other two edges. By L0.1,
mu(U*_c(U*_a cap U*_b)) = T*_R / (n_c [G : U*_a cap U*_b]) = tau*_R / (6 x_ab) (the apex identity used again in section 5);
this set lies in U*_cU*_a and in U*_cU*_b, of measures x_ca/6 and x_cb/6 (L0.1), so tau*_R <= x_ab min(x_ca, x_cb); over the
three apexes, tau*_R <= x1 x2. Finally v2(6 ell_a ell_b ell_c) = 1. A multiple of 8 is <= x1 x2 only if x1 x2 >= 8. QED
```

## G4: DG-4 proof: m_e is a power of 2
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m3 (first clause); Codex item 8.

**Old:**
```text
*Proof.* T*_Q = lcm(n_e, T*_R) k (Lagrange) with k / gcd(n_e, T*_R) = mu(U*_e W*_R) <= alpha*_(ej)/6 (L0.1); gcd(n_e, T*_R) =
6 (w_e is prime to T*_R by K62-E3 Lemma 3's proof for R, and 6 | T*_R), so k <= m_e in {1, 2, 4}, v2(k) <= v2(m_e); and
v2(lcm(n_e, T*_R)) = v2(T*_R). QED
```

**New:**
```text
*Proof.* T*_Q = lcm(n_e, T*_R) k (Lagrange) with k / gcd(n_e, T*_R) = mu(U*_e W*_R) <= alpha*_(ej)/6 (L0.1); gcd(n_e, T*_R) =
6 (w_e is prime to T*_R by the K62-E3 Lemma 3 chain for R, and 6 | T*_R), so k <= m_e in {1, 2, 4}, and v2(k) <= v2(m_e)
because m_e is a power of 2 (no divisibility k | m_e is assumed); and v2(lcm(n_e, T*_R)) = v2(T*_R). QED
```

## G5: Theorem DG (a): arithmetic N(O) >= n_d/8 + 1/3
*File:* `K62-DG-v1.md`. *Disposes:* Codex MINOR 2; Claude DG-m3.

**Old:**
```text
so N(Q) >= n_d/8, and DG-2 (iii) gives 5 n_d/8 <= n_d/4 - 1 + 3 N(O), i.e. N(O) > n_d/8 - 1/2, contradicting
DG-2.
```

**New:**
```text
so N(Q) >= n_d/8, and DG-2 (iii) gives 5 n_d/8 <= n_d/4 - 1 + 3 N(O), i.e. N(O) >= n_d/8 + 1/3 > n_d/8 - 1/2, contradicting
DG-2 (n_d/16 is an integer because e_d >= 4).
```

## G6: Theorem DG (b): "exactly 5"
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m3 (last clause).

**Old:**
```text
and if only one does, it has min(e_d, v2 T*_R) >= 5 (values (4,4,4),
tau*_R = 16, e_d >= 5).
```

**New:**
```text
and if only one does, it has min(e_d, v2 T*_R) = 5 (values (4,4,4),
tau*_R = 16, e_d >= 5; v2 T*_R <= 5 by DG-3).
```

## G7: Corollary header: defined P_ob versus its matrix pattern with markers
*File:* `K62-DG-v1.md`. *Disposes:* Codex MINOR 3; Claude DG-m5 (second clause).

**Old:**
```text
## 5. Corollary: the pattern P_ob of `K62-STATUS-v2.md` is excluded (any markers, any e_d >= 4)
```

**New:**
```text
## 5. Corollary: the defined pattern P_ob of `K62-STATUS-v2.md` (no markers) is excluded; the same proof excludes its (alpha, alpha*) matrix pattern with any class-admissible marker placement, for every e_d >= 4
```

## G8: Corollary step 2: LFC of the original configuration replaces (V1)/(V3); rotation justified
*File:* `K62-DG-v1.md`. *Disposes:* Claude DG-m4.

**Old:**
```text
2. *tau* != 8.* Suppose tau* = 8 on R = {c_1, c_2, c_4} (other i by rotation). In the inverted configuration at apex c_4
   (L1 (T3), gamma = 6): mu(U*_4(U*_1 cap U*_2)) = 8/(6 alpha*_12) = 2/3 = alpha*_41/6 = alpha*_42/6, so (finite sets, inclusion)
   X*_1 = X*_2 where X*_j := U*_4U*_j. From the consecutive triples {c_2,c_3,c_4} and {c_4,c_5,c_1} (tau* = 4):
   mu(U*_4(U*_2 cap U*_3)) = 4/(6 * 2) = 1/3 = alpha*_43/6 gives X*_3 contained in X*_2, and likewise X*_5 contained in X*_1.
   Every edge c_4c_j (j in O) is tight (alpha + alpha* = 6 = g), so the VFC sets of the inverted configuration at c_4
   satisfy D~_j = G minus X*_j (V1, INV (b)). Hence D~_1 = D~_2 is contained in D~_3; it is non-empty (measure
   alpha_41/6 = 1/3), and every right coset R in it has S_R containing {c_1, c_2, c_3}, with local indices
   n_j alpha_4j/6 (j = 1, 2, 3; alpha_41 = alpha_42 = 2, alpha_43 = 4), whose pairwise gcds are 2 (the w's and marker parts are
   pairwise coprime). Three pieces with pairwise gcds < 3 violate (V3) (Sun(3)). So tau* = 4 on all ten triples.
```

**New:**
```text
2. *tau* != 8.* Suppose tau* = 8 on R = {c_1, c_2, c_4} (other i by rotation; see the end of this step). Left-translate
   so that g_(c_4) = 1; this conjugates every U*_j by one common element, so indices and the apex identities are unchanged,
   and U*_4 = U_4. By the apex identity of DG-3 at c_4: mu(U*_4(U*_1 cap U*_2)) = 8/(6 alpha*_12) = 2/3 = alpha*_41/6 =
   alpha*_42/6, so (finite sets, inclusion) X*_1 = X*_2, where X*_j := U*_4U*_j. From the consecutive triples {c_2,c_3,c_4} and
   {c_4,c_5,c_1} (tau* = 4): mu(U*_4(U*_2 cap U*_3)) = 4/(6 * 2) = 1/3 = alpha*_43/6 gives X*_3 contained in X*_2, and likewise
   X*_5 contained in X*_1. *LFC of the original configuration replaces (V1)/(V3):* for j in O minus {c_4} let
   L_j := g_jU_jU_4, the union of the fibres at c_4 (left U_4-cosets) that meet g_jU_j, of measure alpha_4j/6 (LFC (a)-(b)).
   The set (X*_j)^-1 = U*_jU_4 has measure alpha*_4j/6 (L0.1) and is disjoint from L_j (the argument of K62-E3 step 3 with
   c_4 in place of d: if w u lies in L_j with w in U*_j and u in U_4, then g_j lies in U_4U_j, so g_jU_j meets U_4 =
   g_(c_4)U_(c_4)). Every edge c_4c_j (j in O) is tight (alpha + alpha* = 6), so L_j = G minus (X*_j)^-1. Hence L_1 = L_2 is
   contained in L_3; it has measure alpha_41/6 = 1/3, so it contains a fibre F, and F meets g_1U_1, g_2U_2 and g_3U_3. Their
   LFC labels at c_4 are n_j alpha_4j/6 = 2 ell_1, 2 ell_2, 4 ell_3 (alpha_41 = alpha_42 = 2 on chords, alpha_43 = 4 on a cycle edge;
   ell_j = n_j/6 odd and pairwise coprime, markers included), with pairwise gcds 2: this violates LFC (c) at |T| = 3 (Sun(3)).
   *Rotation:* the step uses only the O-O entries of P_ob and n_c = 6 ell_c, never the i*-row, d or the markers, so it applies
   to every rotation c_j -> c_(j+i). So tau* = 4 on all ten triples.
```

## Notes (no text replaced)
- **K62-DG-erratum-v1 was a real gap repair (Claude DG-m5).** The frozen section 5 step 3 chose the end c_(i+3) of the
  4-path as the added vertex without justification; both ends can be marked (for example t = c_1, p = c_4). Erratum v1
  supplies the needed choice (every vertex of the 4-path has a cycle-neighbour in it, and at least two of its vertices are
  unmarked). It stays mandatory.
- **Conditionality of Theorem DG (b) (Codex item 10).** (b) holds under the hypothesis of (a) (every 4-subset of capped
  depth <= 4). For e_d = 4 that hypothesis is automatic, so at least two triples of capped depth >= 4 are forced; for
  e_d >= 5 the alternative "some 4-subset of capped depth >= 5" remains available.
- **Orientation (both reviews).** Theorem DG concerns the alpha*-family after the choice alpha_(d i*) = 1; it applies to the
  alpha-family when alpha*_(d i*) = 1; both apply when (alpha_(d i*), alpha*_(d i*)) = (1, 1).
- **Unchanged:** all other text of K62-SH-v1 and K62-DG-v1. K6.2* (e_d >= 4, e* = 2) and full Sun(7) remain OPEN. No
  novelty claim.
