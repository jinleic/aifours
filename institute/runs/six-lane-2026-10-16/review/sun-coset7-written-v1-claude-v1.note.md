# Hostile audit: Sun(7) reduction, k7 rules, RPLP/CAP addendum and coverage interface

**Convention.** `Sxx:n` means SOURCExx, LF line n.

**Hashes.** I could not recompute any SHA256 (no tools), so the stated values are taken as given. The hash prefixes quoted inside the sources agree with each other:
- S02:9–12 match S00, S01, S03 and S04.
- S00:16–17 match S05 and S06.
- S05:11 matches S07 and S08.

**Premises.** No producer output, count or engine behaviour is used as a premise.

**Audited (re-derived here):**
- R0, P0, P1, R1(7), and R1a–c (modulo Prop 4.5).
- L0.3, L1, L2/L3, K1, K2, L4, L6.
- VFC (V1–V4) and its Corollary.
- D2, D2′, D3.
- CAP, together with A2 and A3.
- RPLP-k7.
- X1⇒K5.3.

**Imported, not re-audited:**
- Sun(2), re-proved anyway as L0.6.
- Zhu's Sun(3) and Sun(4).
- Sun(5) from S05 and Sun(6) from S06.
- Prop 4.5 exactly as stated at S07:67. Its single use at S00:79 matches that statement; I did not re-audit its proof.
- Cardinality facts for products and double cosets.

**Not load-bearing anywhere:** M-S Lemma 4.6, Menon Thm 4.2, FH, the minimal frame, Sun(7).

## A. Reduction to six classes: ACCEPT

**Prime incidence.**
- P0(c) lists every gcd in [2,6].
- gcd 6 is the only composite case. It is exactly P={2,3}, i.e. both vertices in C=A₂∩A₃ (S00:40, 49).

**Theorem R1(7), step by step.**
- **Step 1 (a≥3).** This forces a=7, and then every pair has P={5}. Sun(6) is correctly invoked here: gcd 5 does not contradict Sun(5) (S00:61).
- **Step 2 (a=2).** x∈C is impossible, because y would then share A₂ or A₃ with x. Hence C=V∖{x,y}.
- **Step 3 (a≤1).** Sun(5) on every 5-subset gives |V∖C|≤3.

**Small-C eliminations.**
- R1a uses Sun(4).
- R1b uses Sun(3): it would force C⊆E, which contradicts |C∩E|≤1.
- R1c:
  - The cofactors are r₁=n_i/2 (odd) and r_{t+1}=n_{d_t}/4.
  - They are pairwise coprime, including when the a=1 vertex is any of the four.
  - The tuple has exactly the shape of S07:67.

**Completeness of the case split.**

| case | outcome |
|---|---|
| \|C\|=7 | K7 |
| \|C\|=6, type 2, e_d=1 or C∩E=∅ | D2 |
| \|C\|=6, type 2, otherwise | K6.2* |
| \|C\|=6, type 3 | K6.3 |
| \|C\|=5, type 2 | R1b gives D⊆E; then C∩E=∅ is D2′, otherwise K5.2* |
| \|C\|=5, type 3 | K5.3 |
| \|C\|=4 | R1a or R1c |
| (II) | KII |

**Generality.**
- No common index factor and no Core6 template is assumed.
- Exponents and the cofactors w_i stay unbounded.
- R0 keeps arbitrary groups.

**MINOR A-1** (S00:11, 33 vs S00:34; S01:59; S02:29). The symbol g_i denotes both coset representatives and v₅(n_i), and g_ij denotes a gcd. Repair: rename the 5-adic valuation, for example h_i.

## B. D2, D2′ and partial D3: ACCEPT

**Fibre construction.**
- **Pieces.** For w_j∈g_jU_j∩R, the piece is A_jw_j with A_j=U_v∩w_jU_jw_j⁻¹ and [U_v:A_j]=|D_j|/|U_j|=d_j (S07:186–188).
- **Translation.** Fix one w∈R for all pieces. Then c_j=w_jw⁻¹ lies in U_v.
- **Inversion.** Right translation by w⁻¹ followed by inversion gives disjoint left cosets c_j⁻¹A_j in U_v.
- **Imports.** Sun(|T|) is needed only for |T|≤6, and it holds unconditionally in every group. So neither a properness premise nor Sun(7) is needed.
- **Cardinalities.** |D_j| is a multiple of |G|/g_vj, and q_j≤g_vj−α_vj. The Corollary is strict because ∪D_j⊆G∖U_v.

**D2.**
- Σq/g=3, while VFC-count requires <3.
- Every set of size ≥4 has all pairwise gcds equal to 3, so only Sun(4) is used.

**D2′.**
- **q∈{1,2}:** gcd(d′,d_i)=1, so D_{d₂} is disjoint from every C-fibre, and 1/4+5/6>1.
- **q=3:** every pairwise gcd is 3, and 13/4>3.
- The 5-parts never meet, because a≤1.

**D3.**
- Four α=2 force |Q|≤2.
- The maximal allowed y-sum is exactly 1.
- Σ=|Q|/6+(6−|Q|)/6=1, while VFC-count requires <1.
- The hypothesis is load-bearing: if |Q|=3, the set {o}∪Q is allowed and has y-sum 5/4.
- D3 removes nothing in S00:98–103.

**MINOR B-1** (S00:81). "§R" should read §3; this is erratum E1 at S02:173.

**MINOR B-2** (S01:46). The multi-piece proof of (V3) and the proof of (V4) are only cited: (V3) to a k6 file, and S07 §5 does not state (V4). Repair: inline the argument above.

## C. Rule formulas: AWF

**Verified.**
- **T rule.**
  - T1 follows from L=lcm(n_x,n_y)·ℓ_z.
  - T3 gives τ/(γ_y·α_xz).
  - τ_min pairs each edge with the opposite vertex's ℓ, and S04:60, 65 use the same orientation.
- **L3, re-proved.**
  - Under the pair condition, the sets g_iU_iU_v are pairwise disjoint and miss g_vU_v.
  - From U_vU_j⊆U_iU_j we get U_iU_vU_j⊆U_iU_j, which does not contain g_i⁻¹g_j.
  - The other alternative follows by inversion.
- **K1.** Both link disjuncts in S04:68 are oriented correctly (apex i, respectively apex j).
- **K2.** This is L3 at j with S={v,k}, using the inverted inclusion U_jU_v⊆U_kU_v.
- **L4.**
  - The grid is 1/gcd(n_v,I_jk), from (U_v, U_j∩U_k)-double cosets.
  - When the two measures are equal, the bar applies if either containment is barred (S04:85).
  - PB is Bonferroni using hi.
- **L6** is correct.
- **Allowed sets** are defined hereditarily over all subsets, and the same definition is used in VFC, in (R) and in the columns.
- **Partial pruning** is sound by deletion:
  - T is applied only to completed triangles.
  - Kp is applied only when every triangle {v,x,y} is complete.
  - VFC over N′ is applied for every q∈Π[1,g−α].

**MINOR C-1** (S01:80; S03:15). These lines say every rule is a pattern predicate that "kills every CE". That includes L5, which needs (m, t, fibre) data, and whose 7-piece case holds only in a least-order CE. Repair: restrict the claim to T, K/K1, K2, P, VFC and RPLP.

**MINOR C-2** (S01:26). L3 is only cited; inline the proof above.

**MINOR C-3** (S01:32). Add the condition |T|≥2.

**FH is NOT accepted; no FH exclusion is credited.** Minimum conditions before any future use:
1. **The L6 hypothesis.** U_vU_a=U_vU_b must follow from pattern data. The condition at S02:166 is sound: (F7) for (a,b) together with α_va/g_va=α_vb/g_vb.
2. **Every admissible m must be refuted.** Admissible means: m≥2, m|g_ab, mα_ab≤g_ab, t_v=mα_va/g_va∈ℤ, and every λ_l∈ℤ. Because m=6 is never attempted (S03:27), FH is void on any edge that admits m=6.
3. **Fibre domains.**
   - t_a=t_b=1, and t_l∈[1,m] for every other l.
   - Every t_l-subset of W-cosets must be allowed.
   - F3 must hold at a and b.
   - No balance or cover assumption may be added.
   - Only one coset label may be fixed.
4. **Scope.** Fibres with at most 6 pieces are unconditional. A 7-piece fibre needs the theorem closure restated as "no least-order CE" (S02:169; S00:111).
5. **λ-gcds** must come from CAP bullet 5.
6. **Freezing.** The rule must be frozen before any counted use.

## D. RPLP-k7: ACCEPT (as a written lemma)

**F1–F5.**
- X_j, Y_j and D_j are left U_v-invariant, so every right coset R has a well-defined type (A_R, S_R).
- S_R⊆A_R, and S_R is allowed for d_j=q_jn_j/g_vj.
- ∪Y_j⊆G∖U_v, so (TOT) is strict.

**F6.**
- The lower bound τ_min/(γ_v·α_jk) comes from T3 at apex v, with γ_v=lcm(g_vj,g_vk).
- The K2 bar applies only when hi equals the minimum.

**F7.**
- The test τ_min·g_va≥γ_v·α_ab·α_va gives μ(U_v(U_a∩U_b))≥μ(X_a).
- With inclusion and finiteness, U_v(U_a∩U_b)=X_a⊆X_b. This is T3/T2 at apex v, not the older attribution.
- The test is ordered, and the column rule "b∈A⇒a∈A" encodes Y_b⊆Y_a (S04:96–97).

**Weak duality.**
- (★)≤1 holds on the support 𝒞(q*).
- a and b are free because they multiply the equalities E1 and E2.
- u,l≥0 and μ(Y_j∩Y_k)∈[ylo,yhi], so −u·μ≥−u·yhi and l·μ≥l·ylo.
- Hence Σx≥Obj≥1, which contradicts Σx<1. A non-strict Obj≥1 is enough.

**Farkas scaling.** Dividing by Obj keeps u,l≥0 and gives (★)≤0≤1.

**Quantifiers.**
- (R) is checked against every allowed T.
- The columns are every nonempty A paired with S=∅ or every allowed S⊆A.
- All q∈Q_v must be refuted.
- τ enters only through τ≥τ_min.
- Dropping valid constraints only weakens the LP, so it cannot create a false kill.

**MINOR D-1** (S02:106). The Farkas paragraph covers only infeasibility of {x≥0, E1, E2, B}. When that system is feasible, a (P) certificate exists iff min Σx≥1, which is LP duality. This affects completeness only, not soundness.

**MINOR D-2** (S02:19). The correspondence between this text and the engine code is not established. Checkers must be built from S02 §A1 and S04 §3 alone.

No Stage A/B RPLP kill is accepted by this verdict.

## E. CAP: ACCEPT

Under (H1)–(H3) (S02:144–146), every quantity used is exact.

**Exactness, per quantity.**
- **g and γ.** The pairwise minima are ≤2 and ≤1, below the caps 4 and 2.
- **τ_min.** v₂(γ)≤2 and v₂(α)≤2, so a truncated vertex keeps capped v₂(ℓ)≥2. The same argument works for p=3 and 5.
- **u.**
  - If v carries the unique large valuation, the other argument is ≤4 for p=2 and ≤2 for p=3, 5.
  - If j carries it, v's small valuation is the minimum either way.
- **VFC gcds.**
  - If j is truncated: second term ≤ 2+max(0, e_j′−e_v) ≤ 4−e_v ≤ capped first term.
  - If v is truncated: v₂(d_j)=v₂(q_j), which does not involve e_v.
- **Cofactors.** The prime-to-30 parts w never contribute.
- **Derived quantities.** Forced pairs, links, K2, lo/hi and the column sets are all functions of the quantities above.

**Separate universe hypotheses.**
- X1: min e≤1, min f=1, min g=0.
- MSP45: min e≤2.
- CORE5: min e=2.
- In all three, w_i divides r_i and every g≤6.
- The role domains at S04:13–22 contain every capped profile.

**High-valuation search: no counterexample, and the caps are tight.**
- **u-grid.** Take KII with v=i* (e≥5), the pair {x,y}, e_x=2 and α_xy=4. Both the true and the capped value are 4; a cap of 3 would give 3.
- **τ_min.** In the triangle {x,y,i*} with α_xy=4 and γ=12, capped v₂(ℓ)=2=v₂(4). A cap of 3 would overstate τ_min, which is unsound.
- **VFC.** At v=y with x (g=5, α=1, q=4) and i*, both minima are 4.
- **u-grid for p=3.** In a C–C pair with α=3, viewed from a vertex with f≥3, the minimum is 2. A cap of 1 fails.

The stated profile counts (S02:157) match my own static Burnside recount from these domains: 660/115, 567/135 and 1331/71. That checks the domains only and carries no coverage weight.

## F. X1⇒K5.3 and the coverage interface: AWF (the bridge itself is ACCEPT)

**The bridge.**
- Take n/3 for both D-vertices. These are odd because e=0.
- Take n/6 for any three C-vertices.
- The cofactors are pairwise coprime:
  - D–D: gcd 3 forces coprime cofactors.
  - D–C: 3·gcd(r_d, 2r_c)=3 forces coprime cofactors.
  - C–C: gcd 6 forces coprime cofactors.
- By deletion, these five cosets form an X1 configuration in the same group, for every finite group.
- No minimal frame is used, and neither Menon nor M-S 4.6 is needed.
- This is only conditional on an independently verified X1 exclusion.

**The interface.** All rules are equivariant under vertex permutations. So profile orbits obtained by sorting within role runs, and leaf canonicalisation under the profile stabiliser, are both valid.

**What a fail-closed checker must recompute:**
- its own admissible-tuple enumeration, stabilisers and canonical codes;
- every signature and every LP key, from (entries, q);
- every used vfc_killed signature, for every q;
- at every leaf: the forced pairs, all columns, and (★)/Obj for every q.

It must then re-walk the entire tree. Stored code and key strings are only values to match; they cannot serve as proof identities.

**MAJOR F-1 (process; S02:174–178, S04:3–5, S03:26, 31).**
- The certificate format (13:38:43) postdates Stage A (13:35:02–05) and the start of Stage B (13:37:15).
- The RPLP addendum (14:00:41) postdates both stages.
- S03:26 was false when frozen.
- So no Stage A/B output carries proof weight or counts as preregistered. The only repair is a full independent replay built from the frozen texts.

**MINOR F-2** (S04:120). "Equivalent" should read "sufficient". The checker should search every N′⊆N(v) with |N′|≥3 and re-verify each hit. S04:116 then needs one of two definitions:
- the checker's uncovered leaves form a subset of SURVIVE; or
- the checker mirrors the engine's pruning exactly.

**MINOR F-3** (S03:29, 33 vs S02:179–181). No node certificates are stored. This is acceptable only through the full re-walk.

**MINOR F-4** (S04:28–34 vs S02:155). No K53, K62, K63 or K7 universe is defined. Any such run needs a new frozen format.

## Process boundary

A sound written bridge exists, conditional on the prescribed full finite checks:
- **Requirement.** An independent checker, built only from S01, S02 and S04, re-walks the complete X1, K52 or KII universe. It verifies every closure and every per-q certificate.
- **Consequence.** That class (K5.3, K5.2* or KII) then has no counterexample in any finite group, and by R0 in any group.
- **Imports used.** These kills use only Sun(t≤6) and no minimal frame.

**Classes with no frozen universe.** K6.2*, K6.3 and K7 have none, and FH is unusable.

**Status.**
- All six classes remain OPEN.
- The independent checker results were not provided and are not inferred.
- No Sun(7) claim is made.
