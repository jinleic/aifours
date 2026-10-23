# Hostile written review: K7(a2) Unit 2

**Target:** `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-a2-closure/K7-A2-UNIT-2-v1.md` (sha256 1bef6d8c…942b, lines 1–152), together with `review-package-A2-unit2-v1.md`, its manifest, and the OV2 premise addendum.

**Basis:** I used only the embedded snapshot. I used no tools, file reads or computation. I did not check SHA256s, byte counts or timestamps. Prior reviews were treated as premise-authority records only. Every Unit 2 claim remains **CANDIDATE_UNVERIFIED**. This review does not accept any claim. Nothing here closes (a2), K7 or Sun(7).

## Result

**FATAL 0 · MAJOR 0 · MINOR 7.** I re-derived every load-bearing step and found no mathematical gap. All seven findings are about notation, wording or packet verifiability.

| Group | FATAL | MAJOR | MINOR |
|---|---|---|---|
| light/gcd map (§0–§1) | 0 | 0 | 3 |
| α no-three (§2) | 0 | 0 | 3 |
| ZT/ZTR (§3) | 0 | 0 | 0 (m6 recurs at :100, counted once) |
| B/ZS (§4) | 0 | 0 | 0 |
| ZW (§5) | 0 | 0 | 0 |
| packet/interface | 0 | 0 | 1 |

## Verdict per claim

| Claim | Lines | Verdict |
|---|---|---|
| S-data and FG-a2 interface reading | :15–22 | PASS. Matches A2-FIVE :101–105, :129–130, :157–162 literally. OV2 V2.1–V2.11 amend none of these. |
| Light lemma (LFC, opposite index T_{x*}) | :27–32 | PASS |
| VFC form (own index T_x) | :33–34 | PASS |
| FG-zf omitted-marker chain, both families, every u∈W, every p placement | :36–43 | PASS |
| L_z/L_t and V_z/V_t consequences | :44–47 | PASS |
| Full α-row bound with equality; full Γ^{α*} VFC bound | :48–49 | PASS |
| α local row test, survivors, L_t^(u)⊆L_z^(u) | :54–74 | PASS |
| Triangle (3,a,b) propagation | :76–78 | PASS (m5) |
| Centre count ⇒ α has no W-three | :78–85 | PASS |
| Spanning-tree t-bound and D_z equality witness | :88–95 | PASS |
| ZT | :97–106 | PASS |
| ZTR | :108–113 | PASS |
| B-test | :116–120 | PASS |
| ZS | :121–126 | PASS |
| ZW | :129–143 | PASS |

## Hostile checks performed

### Own versus opposite index

- **LFC in Γ^x uses the opposite family.** H=∩g_jU_jg_j⁻¹ gives [G:H]=T_{x*}(Q).
- **VFC in Γ^x uses the own family.** Φ_vW_Q ⊆ Φ_vΦ_j and V1 apply, with T_x(Q).
- **Every use matches the correct side:**
  - §2 full α-rows use T_{α*}(V∖u), via FG-a2.
  - The B-test uses T_{α*}(Q_z) and T_{α*}(Q_t).
  - ZW starred rows use T_α(Q_z).
  - ZT uses T_α(W); ZTR uses T_{α*}(W).
  - The §2 centre count uses only V4.

### Light/gcd map

- **Light lemma.** [H:H∩K]=[G:H∩K]/[G:H] ≥ n_v/gcd(n_v,[G:H]). The light set contains g_vU_v, so LFC(b) still bounds the count by 5n_v/6. This gives val≤5, and at val=5 every fibre touching Q has weight 1.
- **FG-zf.**
  - For u∈W′: T(Q_z)=6·3^A w_t·5^B w_p·x_tp·∏w_e k_e.
  - For u=p: T(Q_z)=n_t∏w_e k_e.
  - In Q_t the base is x_zp≤3, because α_zp=3 and α*_zp≤3 by S2.
  - Each entering vertex of W′ has gcd 6 with the running index, so k≤x_ej≤4.
  - Hence gcd(6w_u,T)=6, and gcd(6·5^B w_p,T)=6 because 5∤T when p∉Q.
- **FG-a2 at β=α*.**
  - Condition (a) holds because α*_zt=1.
  - Condition (b) holds because α*_zt=1 and α*_zu≤3.
  - The proof correctly does not assert FG-a2 for β=α (there α_zt=5, α_zp=3, and α_tp may be even).

### α no-three (§2)

- **Feasible vectors.** I re-derived every vector:
  - k=1 gives ≥6.
  - k=2 leaves only remainders 11 and 22; k=3 leaves remainder 1 or 2.
  - e=1 gives 16/3, 16/3, 16/3, 17/3, 16/3.
  - e=4 gives 6, 11/2, 16/3, 16/3, 16/3.
  - e=2 with k=3 and remainder 2 gives 16/3.
- **Zero-weight sets.** I checked the allowed sets through zero-weight vertices. For example, {t,z,3,3′} is allowed via gcd(z,t)=6 or 12, and its weight is still ≤1.
- **Survivors 3333, 3331, 3311, 3322.** Each survivor vector has value exactly 5 and is feasible. Every weight-1 set through t contains z, so g_tU_tU_u ⊆ U_zU_u.
- **Triangle.** T1 gives 3·max(a,b) | τ. T3 at apex w gives τ ≤ 3min(a,b), so a=b. T3 at apex v then gives a=b=4.
- **Centre count.** D_t ⊆ U_zU_u is disjoint from D_u by V1. The weighted mass is (|T*|+|O*|+1)/6=1, against V4. The Sun(2), Sun(3) and Sun(4) instances are correct.

### ZT/ZTR

- **Tree chain.** T_x(W)=6∏ρ·2^h, and no factor of 5 enters before p.
- **Equality witness.** At equality the W-union is exactly 5/6 and the light product is exactly 1/6 and contains Φ_t. D_z meets the W-union in a right coset R whose W-part has weight 1, and S_R is allowed by V3 heredity.
- **ZT.** d_z=2^E w_z. I checked k=0 through k=5 exhaustively.
- **ZTR.**
  - d_z=5·2^E w_z and μ(D_z)=5/6.
  - In the zero-fours case, the forbidden triple is {z,2,2′}, which forces D_z∩Q⊆D_p.
  - This gives 4/6 > 2/6, a contradiction.
  - The z–p gcd (5 or 10) is retained.

### B/ZS

- **B-test.** The case list is exhaustive:
  - no four;
  - 1114, value 7;
  - 1124, value 6;
  - 1224/2224 with E=1 (13/2), e=1 (6), e=2 (6).
- **ZS starred triangle.** T1 and T3 force α*_av∈{3,4}, hence α_av∈{1,2}.
- **ZS branches.** |outside|=1 (the |T*|=4 case) is killed by the B-test. When |outside|=2, triangle(4,s1,s2) forces s1=s2=2. Every placement of p is covered.

### ZW

- **Starred rows.** All starred-row vectors use y_z=0 (L_z). For 3311/3322 the vector has value 4+e*/3 and is feasible for every e*, so e*≤3.
- **Θ* structure.**
  - Each Θ* edge dominates the other vertices.
  - Every vertex has degree ≥2, and degree 4 contradicts the B-test.
  - Nonadjacency is transitive, so Θ*=K_{3,2}.
- **Contradiction.** The A×B entries have α=2, which proves Γ_α connected before ZT is invoked. ZT then requires two starred t-fours, and there is room for none.

### Unbounded exponents

- E only matters through min(E,2), and E=1 is handled explicitly in the B-test.
- A only affects gcds through a single factor 3.
- 5^B never meets a 5 except through d_z at apex t of Γ^{α*}, and ZTR retains that collision.

## MINOR findings

**m1 (light/gcd)** `K7-A2-UNIT-2-v1.md:12, :32, :91, :93`
x′ is used but never defined. It must mean x* (by INV(b), the VFC q in Γ^x is x*).
*Repair:* add "x′ := x*, the other family" to §0.

**m2 (light/gcd)** `K7-A2-UNIT-2-v1.md:40`, `:146`
- At :40, "Φ_eW" reuses W (the vertex set) for the running intersection.
- At :146, the exports name "G_z/G_t", but §1 defines only FG-zf, (L_z)/(L_t) and (V_z)/(V_t).

*Repair:* rename the running intersection to H_m, and define G_z/G_t at :36–37 as the two gcd equalities.

**m3 (light/gcd)** `K7-A2-UNIT-2-v1.md:50–51`
This remark is imprecise, though nothing depends on it:
- "z/t odd label parts share 3" fails in α*-rows where α*_uz∈{1,2}.
- A 5-share between z and p occurs only at apex t, never at a W-apex.

*Repair:* localise the remark to "W-apices of Γ^α (c=3)" and "apex t, where the z coefficient is α_tz=5".

**m4 (α no-three)** `K7-A2-UNIT-2-v1.md:74, :78`
L_j^(u) is used as a set but never defined. It also collides with the bound names (L_z)/(L_t) at :45. The identity L_z^(u)=U_zU_u at :78 needs the definition L_j^(u):=g_jU_jU_u together with g_z=1.
*Repair:* define L_j^(u) as "the union of left U_u-fibres met by g_jU_j, i.e. g_jU_jU_u" before :74.

**m5 (α no-three)** `K7-A2-UNIT-2-v1.md:77`
"at most a·min(3,a)" mislabels the T3 bound. The apex bounds are b·min(3,a) at apex u and a·min(3,b) at apex v. The stated form is correct only after a=b has been derived.
*Repair:* "at most a·min(3,b) (apex v); with a=b this gives 3a ≤ a·min(3,a)".

**m6 (α no-three, recurs at ZT `:100`)** `K7-A2-UNIT-2-v1.md:60`
The pair-value for 24 is stated as 3, but the true maximum is 4 (weight 1 on the four). This is harmless: every use is a lower bound, and 3 already kills (3+3>5 in §2; 3>2 in ZT).
*Repair:* write "are at least (2,3,5,2,3,4), with equality for 11 and 22".

**m7 (packet)** `review-package-A2-unit2-v1.md:9–10` and the manifest
OV1 is supplied only as excerpts (:488–492, :505–511, :575–577, :589, :603–606). The snapshot therefore cannot show that no other OV1 item amends the literal statements of Lemma F (:40–49), FG-a2 (:101–105), D23-a2 (:129–130) or S1–S5 (:157–162). The D23P statement is also absent. The used content is corroborated by OV2 V2.7(iv), which invokes FG-a2(a)/(b) with the same hypotheses.
*Repair:* add an OV1 item index to the manifest, giving the item IDs and line ranges that target those A2-FIVE ranges, or an explicit "none".

## Join notes (not findings)

- **J1. Normalisation and R0 are left to the join.** Unit 2 works only in finite G with α_zt=5 normalised. The α*_zt=5 component (actual inversion: INV(a) and E6 swap α and α* while keeping indices and markers) and the R0 lift are scope obligations (b) and (d) for the joining unit. Unit 2 correctly restricts its exports at :146.
- **J2. Conditional exports are exactly as stated.** ZT requires Γ_α connected, ZTR requires Γ_{α*} connected, and ZW requires T*=W. ZS leaves two open terminal branches. Nothing in Unit 2 touches (a2-no5) or proves (a2) empty.
- **J3. The B-test proves more than it states.** The proof shows the W-part is in {1224, 2224}, but Unit 3 may use only the stated form unless it re-cites the proof.
- **J4. Sun accounting.**
  - **Direct:** only Sun(2)–Sun(4) are used. No vector's feasibility needs Sun(5) or Sun(6); zero-weight 5-sets such as {z,4,4,4,4} carry weight ≤1 regardless.
  - **Transitive:** Sun(5)/Sun(6) enter only through the S-data and D23P provenance and through LFC/INV. They remain computer-assisted imports, and Unit 2 discloses this at :14.
- **J5. The dependency order is acyclic as declared.** ZT does not need §2; ZS and ZW invoke the B-test only after §2 has supplied entries in {1,2,4}.

No (a2), K7 or Sun(7) closure follows from this packet. No novelty, Lean or human-review claim is made.
