# Referee report, Slice A2: `K7-A2-FIVE-v1.md`

**Basis.** I reviewed the embedded text (sha256 93fd95d7…8dfc). I did not re-verify any hash.

**Accepted imports used:**
- RICH (ba32d282…), with erratum-1 R-1 (8261831b…) and the consolidated erratum (55cb66ca…), which governs.
- D23P (89739dc2…) with the consolidated erratum.
- LFC/INV with errata (8621e744…).
- L0.1, L0.3, L1 and VFC (73a25ba6…).
- D23-MIX (d3453de1…).

A1-STRUCT, TC and TC-A22 were read only for the transfer's dependency-use audit. They are not accepted and not re-proved here.

## 1. Verdicts

| Claim | Verdict | FATAL/MAJOR/MINOR | Scope after repair |
|---|---|---|---|
| Lemma F (F1)–(F7), and "only z–t can be 5, in at most one orientation" | ACCEPT-WITH-FIXES | 0/0/4 (F1–F4) | (a2), both orientations, all E, A, B ≥ 1 |
| Lemma FG-a2 (a), (b) | ACCEPT | 0/0/0 | Subgroups V_j of the (a2) index tuple with β ≤ 5 |
| Corollary 5/6-a2 | ACCEPT-WITH-FIXES | 0/0/1 (C1) | u ∈ W′ if one condition of (a) holds for β = x*; u = p iff x*_zt ≠ 5 |
| Lemma D23-a2 | ACCEPT | 0/0/0 | (a2), any orientation x with x_zt ≠ 5 |
| Prop. K7-A2-ZT5 (S1)–(S5), including E ≥ 2 | ACCEPT-WITH-FIXES | 0/0/1 (Z1) | (a2-zt5), with x the orientation of the five; structural narrowing only |
| Thm. K7-A2-BRIDGE (B1)–(B7) | ACCEPT-WITH-FIXES | 0/0/6 (B1–B6) | (a2-no5), W = W′∪{p}; the explicit list in B1; FG7 is not claimed verbatim |
| Cor. K7-A2-TRANSFER | CONDITIONAL ACCEPT-WITH-FIXES, as a proof-transfer statement only | 0/0/5 (T1–T5) | Inert until A1-STRUCT c8a16f14…, TC cc48340d… and TC-A22 9ebec279… are accepted exactly; claim sections only |
| File-wide | — | 0/0/2 (G1, G2) | — |

There is no FATAL and no MAJOR finding. None of this excludes (a2), K7 or K6.2*, and no Sun(7) conclusion follows. No abstract pattern is accepted or excluded by this review.

## 2. Mandatory repairs

**File-wide**

- **G1 (§0).** Add: "All statements are for finite G. R0 (LFC verdict item 6, which preserves α and α*) lifts each of them to arbitrary G with finite-index subgroups."
- **G2 (§0 Sun bullet and delta-manifest item 4).** Replace "Sun(2), Sun(3), Sun(4), only through LFC (c)" with:
  - "Direct, in §§1–4 except the Transfer: Sun(2)–Sun(4) only, through LFC (c) and, in the bridged Lemma CC, VFC (V3).
  - The E8 standard weights are applied only to at most four neighbours with entries in {1,2,4}, where the Sun(5)/Sun(6) branches are vacuous.
  - Corollary K7-A2-TRANSFER additionally uses **Sun(5) directly**, through A1-STRUCT §0 / Corollary L, cases 44441 and 44444.
  - Transitive: the computer-assisted Sun(5) record (2cf02436…) and Sun(6) record (efe1d849…), reached through D23P (ROW-2/E8) and the LFC/INV provenance."

**Lemma F**

- **F1 (F1 proof).** After "inside F5" insert: "(the weights below vanish on t and p, the only other labels that can carry the prime 5)".
- **F2 (§0; cite in F3, F4, F6, D23-a2 and S5).** Add a clique rule:
  - "If labels have pairwise gcd 3, except possibly gcd(t,p) = 15, the allowed sets are those of size ≤ 3 and the 4-sets containing both t and p (Sun(4)).
  - No 5-set is allowed, because it contains a 4-subset missing t or p.
  - Weights ≤ 1/3 on such a clique, with weight 0 on p, are feasible on it."
  
  Cite this rule for the 17/3 vector in the last branch of (F6), whose feasibility is currently asserted without reason.
- **F3 (F4).** Mark the sub-case x_pz = 5 as "vacuous by (F3)".
- **F4 (F7).** Replace "(E8 with N = 4 …)" with:
  - "E8 subset form, justified as in RICH RF4: B = W′, four unmarked neighbours with entries in {2,4}, whose label gcds are the entry gcds.
  - The only other positive weight, y_p = 1, sits on a label coprime to all of B.
  - With |B| = 4 the branch b ≥ 4 has exactly four elements, so only Sun(2)/Sun(3) decide allowedness inside B."

**Corollary 5/6-a2 and Proposition A2-ZT5**

- **C1 (Corollary 5/6-a2 proof).** Replace "uses only gcd(n_u,[G:W*]) = 6" with: "uses, besides facts valid in every K7 configuration, only gcd(n_u,[G:W*]) = 6". The facts valid in every K7 configuration are:
  - disjointness and the L_j-avoidance of W*U_u;
  - LFC (a)–(c);
  - g_uj = 6 for all j;
  - G0;
  - the RF2 normalisation.
- **Z1 (S5).** Make three changes:
  - Replace "w_t w_p (product of the w_u)" with "w_t·w_p·∏_{u∈W′} w_u".
  - Add: "z ∉ Q, so T_2 = lcm(n_t,n_p)·x*_tp is exact for any x*_tp and no FG-a2 condition is needed. All later vertices are unmarked, with gcd(n_e,T_m) = 6."
  - Cite LFC (b) for "U_z holds no piece", and F2 for feasibility.

**Bridge**

- **B1 (statement).** Replace "every conclusion of K7-D23-RICH … holds" with an explicit list:
  - Theorem K7-D23-RICH;
  - G0;
  - Corollary 5/6 with its equality clause, at every u ∈ W, both orientations;
  - NO5;
  - R3 with S1–S4 as local-test survivors only (RF5), and Corollary R3;
  - TR;
  - CC;
  - TZ (i)–(iii);
  - LZ.
  
  Add: "FG7 is not asserted verbatim; its uses are replaced as in (B3). RICH §6 (navigation) and §9 (residue description) are not transferred."
- **B2 ((B3), second sentence).** Replace it with this W-chain paragraph:
  - "For Q ⊆ W in **any** order, T_2 = lcm(n_j1,n_j2)·β_j1j2 exactly.
  - At each later step gcd(n_e,T_m) = 6. For unmarked e this holds because w_e is coprime to T_m and 6 | T_m. For e = p it holds because no n_j (j ≠ p) and no β ≤ 4 contains the prime 5.
  - Hence k ≤ β_ej ≤ 4 for every earlier j, T_Q = 6·∏_{j∈Q} w′_j·β_j1j2·∏k, and v5(T_Q) = B·[p∈Q].
  - RF8c's reason ("W contains no marked vertex") is false in (a2) and is replaced by this paragraph."
- **B3 ((B6)).** Add:
  - "T*_W = 6·∏_{u∈W} w′_u·α*_{j1j2}·k3·k4·k5, so v5(T*_W) = B.
  - n_z = 2^{E+1}·3·w_z is prime to 5 and has v3 = 1, so g = 3·2^{min(1+E, v2 T*_W)}.
  - RICH's clause '5 does not divide T*_W' is false in (a2) and is replaced by this."
- **B4 ((B2), R3 case k3 = 1).** Add:
  - "At an apex in W′, the three-element set B may contain p. Its label a_p·5^B·w_p has the entry gcd with every label of B.
  - The single weighted three, possibly p with label 3·5^B·w_p, is coprime to B.
  - So RF4 applies verbatim. At apex p, B ⊆ W′."
- **B5.** Two changes:
  - "(B5) NO5 holds by the definition of (a2-no5)", replacing "by (B2)".
  - "(B4) D23-a2, in both orientations, replaces every RICH citation of D23-MIX: R3 (c ∈ {1,2,3}, including c = x_pz at apex p), TZ (i) (s ∈ {1,2}), TZ (iii) (|T*| ≥ 3), CC, and LZ."
- **B6 ((B2), triangles).** Add: "In every L1 use, ℓ_j = r_j and ℓ_p = 5^B·w_p, so gcd(x, ℓ_p) = 1 for x ≤ 4; this includes TZ (i) in the inverted configuration via Z2 G5."

**Transfer**

- **T1 (statement).** Replace with:
  - "If A1-STRUCT (c8a16f14…), K7-TC (cc48340d…) and K7-TC-A22 (9ebec279…) are accepted exactly as frozen, then the following hold in (a2-no5) with W = W′∪{p}, with RICH replaced by K7-A2-BRIDGE:
    - A1-STRUCT: Cor W3, E3, PFG-t with Cor L, Lemma B, CASEB;
    - TC: Lemma TC, R1/R3/R4/R5, the exclusion of ({1,4,4,4}|c|1), TC-B, TC-P;
    - TC-A22: Theorem K7-TC-A22.
  - Not transferred: A1-STRUCT §§6–7, TC §§5–6, TC-A22 §4.
  - Any errata to these sources require this audit to be redone."
- **T2.** State the direct Sun(5) use (as in G2). Note that p may be one of the fours: its local index is 4·5^B·w_p and all gcds remain ≤ 4.
- **T3.** Replace "(every ell … is odd)" with: "every ℓ of a vertex in W is prime to 6, including ℓ_p; Cor W3 needs the 3-part, 3/gcd(3, ℓ_w) = 3".
- **T4.** Add: "The bounds μ(∪D) ≤ 5/6 at W-apexes in TC-B (i)/(ii) are G0 + FG-a2 for the subgroups of the configuration carrying the VFC (pairwise β = α* in C^{α*}). The condition holds in (a2-no5)."
- **T5.** Add the following:
  - **PFG-t ordering.** In PFG-t (i), p may occupy any position. Before p, T_m is prime to 5 (its factors lie in {1,2}), so gcd(n_p, T_m) = 6.
  - **3-part.** v3(T_W) = 1.
  - **5-part.** 5^B | T_W, so the text's "T_W prime to 5" is false here. Only gcd(n_t, T_W) = 6 is used.
  - **E3.** In E3, B may contain p; |B| = 4, handled as in F4.

## 3. Justification

### 3.1 Lemma F

**Conventions.** At apex v of C^x, the label of j is r_j·x_vj. Every g equals 6, and LFC (d) reads val < 6.

**Prime incidence of labels:**
- 5 divides the label iff j = p or the entry is 5;
- 3 divides it iff j = t or the entry is 3;
- 2 divides it iff j = z or the entry is in {2,4}.

I checked every weight vector:

- **(F1).** c ∈ {1,2,3} by D23P.
  - The labels 5w_v (v ∈ F5) are coprime to z and to every non-five W′-label. They meet only t, p and F5, and t, p carry weight 0.
  - If |F5| ≤ 2, val is at least 5 + x_ub ≥ 6. A suitable b exists because |W′∖{u}| = 3.
  - If |F5| = 3, val = 5 + c ≥ 6.
- **(F2).** The label 5^{B+1}·w_p is coprime to z (c ≤ 3) and to W′ (entries ≤ 4 by F1). So val = 5 + c ≥ 6.
- **(F3).** At z, D23P gives W′-entries in {1,2,3} and k3 ≥ 2.
  - Case x_zt ≠ 5, x_zp = 5: p is isolated, and val = 8.
  - Case x_zt = 5: t's label 5·3^A·w_t meets threes in 3, p in 5 or 15, and ones or twos in 1.
    - k3 = 2: val = 7. Twos are also coprime to p = 3·5^B·w_p.
    - k3 = 3: val = 5 + o ≥ 6.
    - k3 = 4 with x_zp ≠ 3: the only sets through p are {p} and {p,t}, so val = 4 + 5/3 + 2x_zp/3 ≥ 19/3.
  - So the only surviving z-row is (3,3,3,3 | 3 | 5), and x_zp ≠ 5 in every case.
- **(F4).** At p:
  - a W′- or z-entry in {1,2,4} gives val ≥ 6;
  - all threes with x_pz = 3 give val = 20/3;
  - the sub-case x_pz = 5 is vacuous by F3.
- **(F5).** Holds as written.
- **(F6).**
  - c ∈ {1,2}: val = 5 + c ≥ 6.
  - c = 3 with some W′-entry in {1,2,4}: val ≥ 6.
  - All W′-entries 3 and x_up ∈ {1,2,4}: {a1,a2,a3,z,t} is a gcd-3 clique; {p,z,t} is allowed (gcd(t,p) = 5 ≥ 3) and weighs 1; any set containing p and a three is excluded by Sun(2). So val = 19/3, resp. ≥ 19/3.
  - **Last branch (x_up = 3):**
    - The vector y = 1/3 off p gives val = 17/3 ∈ (5, 6), so LFC (d) does not decide.
    - INV gives x*_ut = 1.
    - If x*_zt = 5, then (F5) for x* (LFC at t in C^{x*}) contradicts x*_tu = 1.
    - Otherwise 5 ∤ x*_zt. FG-a2 (a) with order (z,t,p) applies, and Cor 5/6-a2 gives val ≤ 5 < 17/3.
  - There is no circularity: FG-a2 reads nothing from Lemma F, Cor 5/6-a2 reads only D23P, and (F5) reads only LFC.
- **(F7).** (F5) and (F6) give x_tu ∈ {2,4}. If x_tp = 3, then p (label 3·5^B·w_p) meets only z (label 5·2^E·w_z). The E8 value 4 on W′ plus 3 gives val = 7.
- **Exhaustiveness.**
  - Pairs covered: W′W′ by F1, W′p by F2, W′z by D23P, W′t by F6, zp by F3, tp by F4.
  - Since x_zt + x*_zt ≤ 6, at most one orientation has a five on z–t.
  - Hence the split into (a2-zt5) and (a2-no5) is exhaustive, exclusive and stable under inversion.

### 3.2 FG-a2 and Corollary 5/6-a2

**Step bound.** μ(V_e·W_m) = k / gcd(n_e, T_m) ≤ β_ej / 6 for every earlier j. This uses L0.1 and the fact that every pairwise gcd is 6.

The indices are n_z = 2^{E+1}·3·w_z, n_t = 2·3^{A+1}·w_t and n_p = 6·5^B·w_p. The third-marked-vertex gcds are:

| Order | Valuations of T_2 | gcd with third index |
|---|---|---|
| (z,t,p) | v2, v3 ≥ 2; v5 = v5(β_zt) | 6·5^{min(B, v5 β_zt)} |
| (z,p,t) | v3 = 1 + v3(β_zp) | 6·3^{min(A, v3 β_zp)} |
| (t,p,z) | v2 = 1 + v2(β_tp) | 6·2^{min(E, v2 β_tp)} |

- All three agree with the text.
- **The condition is genuinely needed.** If the third gcd were 30, the bound would only give k ≤ 25, which may contain a prime dividing w_u.
- **(b) keeps 5 out.** It uses k ≤ β_ez ≤ 3. The comparator must be z, not t, because D23P bounds the z-row and nothing bounds β_et.
- **Corollary 5/6-a2.** The RF2 proof of RICH reads only the facts listed in C1. W* has pairwise β = x* in C^x. For x = α*, W* is a conjugate of ∩U_j, so its index is unchanged.

### 3.3 D23-a2

I recomputed every value:

- **(i), x_zp = 4.** Here p = 4·5^B·w_p meets only W′-twos and t.
  - k3 = 4: val = 8.
  - k3 = 3, o = 1: val = 8.
  - k3 = 3, o = 2: val = 6. The parenthetical about {o,p,t} is not load-bearing, since y_t = 0.
- **(ii), x_zt = 3.**
  - k3 = 4: val = 6, or 5 + x_zp.
  - k3 = 3, o = 1: val = 6, 6, 7.
  - k3 = 3, o = 2: val = 7, 7, 6.
  - k3 = 2: val = 6.

All values are ≥ 6. The conclusion is exactly the D23-MIX conclusion that RICH reads, now with W = W′∪{p}.

### 3.4 A2-ZT5

**(S1)–(S4).** These follow from:
- F3;
- INV plus D23-a2 for x* (x*_zt = 1);
- F7;
- Lemma F.

**(S5), E ≥ 2.**
- Normalise g_z = 1. W*·U_z contains U_z and carries no piece, by the general L_j argument and LFC (b).
- y = 1/3 on W′∪{t} with y_p = 0 is feasible by the clique rule, with val = 17/3.
- The count gives (n_z/6)·(17/3) ≤ n_z − M, so M ≤ n_z/18.
- G0 then gives gcd(n_z, [G:W*]) ≥ 18.
- The chain (t, p, W′) has prime-to-30 part w_t·w_p·∏w_u, which is coprime to w_z.
- 5^B divides [G:W*] but is harmless, because n_z is prime to 5.
- So the gcd equals 3·2^{min(E+1, v2)} ≥ 18, which forces E + 1 ≥ 3, i.e. E ≥ 2.

### 3.5 Bridge: RICH checked item by item

| RICH item | What changes with 5-marked p ∈ W | Status |
|---|---|---|
| G0, TR, VFC, INV | Nothing (pure group facts) | Holds |
| FG7 (a)/(b) | Marked-first order and "w prime to 30" fail for p | Replaced: FG-a2 (a) at W′ (condition 1), FG-a2 (b) at p, W-chain of B2 |
| Cor 5/6 and equality clause, both orientations | Needs gcd(n_u,[G:W*]) = 6 | Holds via Cor 5/6-a2 (x*_zt ≠ 5, x*_zu ≤ 3) |
| NO5 (R-1, RF3) | — | Holds by hypothesis; R-1 unused |
| R3, S1–S4, Cor R3 | The gcd table needs 5^B to meet no 5 | Identical (no entry 5; z, t prime to 5). At apex p the labels are exactly the (a1) labels; c = x_pz ∈ {1,2,3}; E8 on B ∋ p per B4 |
| CC | d_p = α*_zp·5^B·w_p | Same gcd table; \|W\| = 5, so (\|T*\| + \|O*\| + 1)/6 = 1 |
| Theorem | Inversion | (a2-no5) is inversion-stable |
| TZ (i)–(iii) | ℓ_p = 5^B·w_p | 3/gcd(3, ℓ_p) = 3 and s/gcd(s, ℓ_p) = s; D23-a2 |
| LZ | p-label 3·5^B·w_p; "5 ∤ T*_W" | Count unchanged (all gcds 3, Sun(4)); g as in B3; Γ*_1 argument via B2 |

The W-chain is valid for any order, including p first or second, and for unmarked vertices after p. No zero-weight or subset-size step changes, because heredity and the gcd tables are identical.

### 3.6 Transfer: dependency-use audit

| Step in source | (a1)-specific fact it reads | Replacement in (a2-no5) |
|---|---|---|
| A1 §0 triangles | ℓ odd | ℓ_p = 5^B·w_p is odd |
| A1 §0 two/four classes and ones | gcd equals entry gcd | p-labels 2^i·5^B·w_p and 5^B·w_p (B2); **Sun(5) direct** (T2) |
| A1 §1 Cor W3 | ℓ prime to 3 | ℓ_p is prime to 3 (T3); RICH replaced by BRIDGE |
| A1 §2 E3 | E8 on four W-neighbours; Bz·Bt = 0 | E8 with p ∈ B (T5); Bz = Bt = 0 |
| A1 §3 PFG-t | 5 ∤ T_W | Only gcd(n_t, T_W) = 6 is needed; it holds (T5) |
| A1 §4–5 (Lemma B, CASEB) | Labels; TZ; D23-MIX | (B2); BRIDGE; D23-a2 |
| TC rigid rows | z–t gcd 6 or 12; "o coprime to all" | Both hold, including o = p; Cor 5/6-a2 |
| TC-B | μ(∪D*) ≤ 5/6 | G0 + FG-a2 with β = α* (T4) |
| TC-P, TC-A22 | V4 counts; "t-label 3^A·w_t meets only z" | Both hold with p ∈ W |

No (a1)-only fact outside (B1)–(B7) and T3–T5 was found. The acceptance is a proof-transfer only. It is conditional on exact acceptance of the three sources. It adds a direct Sun(5) dependence.

### 3.7 Import accounting

- **Direct, §§1–4 without the Transfer:** Sun(2), Sun(3) (inside E8 at F7, and the bridged R3/CC), and Sun(4) (the cliques and LZ).
- **Direct, Transfer:** additionally Sun(5).
- **Transitive:**
  - D23P (ROW-2/E8 with b ≥ 4 using Sun(5), and R5 using Sun(6); D23-CENTER);
  - LFC provenance;
  - the computer-assisted Sun(5)/Sun(6) records.
- D23-MIX is not used in (a2). Sun(7) is not used anywhere.

### 3.8 Still open

The following remain open:
- (a2-zt5) beyond (S1)–(S5).
- The (a2-no5) residue: some u ∈ T* whose α-row has no W-three, and some u′ ∈ T whose α*-row has no W-three.
- The Transfer's content, which stays inert until its sources are accepted.
- The (a1) residue.
- K6.2*.
- Full K7.
- Sun(7).

No novelty claim is made.
