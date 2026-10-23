# Parent audit v1: sun-coset5 rule set, engine, finite bridge and proof-v1 (Lemma R / S-D)

- Desk: `institute/runs/six-lane-2026-10-16/review/sun-core5-parent-rule-audit-v1/`, written 2026-10-18 between 09:41 and 10:20 PDT by the host clock.
- Lane audited (read-only): `mathematics/evidence/six-lane-20261016/sun-coset5/`.
- Scope: the frozen v1 files (README, rules-v1, engine-v1 and run1), and `proof-v1.md` as pinned by the parent. `proof-v2.md`, `rules-v1-erratum-v1.md`, `README-addendum-v2.md`, `controls_v2.py` and `core5_check_v2.py` are outside scope. They were hashed, not audited. For `core5_check_v2`, only its published counts were compared.
- This audit does not claim that k = 5 is solved. The gate still needs the parent verdict.

## Verdict: **SOUND-WITH-FIXES** — no GAP, no FATAL, no MAJOR

The audit found no rule that can eliminate a genuine configuration.

**Written mathematics.** All of it was re-derived by hand:
- R0 and R1;
- L0–L4 (T, links, K, K2, P1–P5);
- N2;
- F1–F3, H1 and H2;
- L8 (M1, M2);
- Lemma R and the S-D refutation.

Ten MINOR fixes remain: justifications, citations and wording. Each has an exact correction in §4. None changes a certificate or the survivor.

**Finite bridge.** It is verified by parent code that imports nothing from the worker. The verifier is `bridge_verifier_v1.py` (sha256 `2d7fff78…7659`) and its result is `bridge-run1/RESULT.json` (sha256 `d741396c…7278`), verdict **PASS**. The result is bound to:
- extract `review/sun-core5-certificates-run1-parent-extract.tsv`, sha256 `e9bd7c54…5bb2`;
- engine `code/core5_engine_v1.py`, sha256 `65ce5a00…2eb1`.

It supplies exactly the four runtime items required by `review/sun-core5-engine-codex-v1.note.md` (d87212a9…b3d1); see §2.

## 1. Re-derivations (hand), with the specific points requested

**R0 (README.md:27–31). ✓**
- core_G(G_i) is the kernel of the action on n_i cosets, so N = ∩core is normal of finite index and N ≤ G_i.
- Each coset a_iG_i = a_iG_iN is a full preimage. So indices, intersection indices and disjointness all pass to G/N.

**R1 (README.md:36–46). ✓ mathematically.**
- No pair is coprime (L0.6), so each gcd is in {2, 3, 4}.
- If some n_i is odd, every gcd with it equals 3, so 3 divides all five indices. The gcds are then all 3 and the cofactors are pairwise coprime. Any four contradict Sun k = 4.
- Otherwise all indices are even and n_i = 2^{e_i}m_i, with the m_i pairwise coprime, min(e_i, e_j) ∈ {1, 2}, and at most one e_i ≥ 3.
  - Two indices with e = 1 plus any third index give (2r, 2r′, 2r″) with r″ = 2^{e−1}m, pairwise coprime: excluded by Prop 4.2.
  - Exactly one index with e = 1 gives (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd: excluded by Prop 4.5.
  - Otherwise the configuration is Core(5).
- The proof of M-S Prop 4.5 (arXiv v1 pp. 9–10) was re-checked line by line. Two lines need justification patches, F-2 and F-8 below.
- Both direction labels are swapped (F-5).
- Independent support: the parent C1 replay (`indep-run1/summary.json` D_C1_shapes) kills every orbit of (2,2,2) [5], (3,3,3,3) [111] and (2,4,4,4) with r_1 odd [119]. It uses only the lane lemmas L1–L4, at 5 explicit r-instances. So Props 4.2, 4.3 and 4.5 are also re-derived from audited lane lemmas.

**T (rules-v1.md:70–98). ✓**
- Statement: L | T, and I_xy | Lτ (T1).
- (T3): |U_y(U_x∩U_z)| = |G|·T/(n_y·I_xz).
- (T2) is containment in U_yU_x ∩ U_yU_z, both used purely as sets.
- Core(5) forms:
  - (T1) ⟺ α_xy | r_zτ, so τ_min = lcm_e α_e/γ_e;
  - (T3) = τ|G|/(4α_xz);
  - τ_max = the minimum product of two α's.
- Engine `tau_min`/`tau_max`/`T3` (core5_engine_v1.py:64–85) implement the general-index form exactly. The floor in tau_max is correct.

**Links / K / K2 (rules-v1.md:100–132). ✓, orientation checked.**
- If |U_y(U_x∩U_z)| = |U_yU_x|, then U_yU_x = U_y(U_x∩U_z) ⊆ U_yU_z. Inverting gives U_xU_y ⊆ U_zU_y.
- K step 1: g_iu_iu = g_ju_ju′ gives g_j⁻¹g_i ∈ U_jU_vU_i. The containment U_vU_i ⊆ U_jU_i makes this ⊆ U_jU_i, which contradicts L0.2 for the left cosets g_jU_j, g_iU_i. The second alternative works through the inverse.
- K step 2: g_iU_iU_v is right-U_v-invariant, so meeting g_vU_v would force g_iU_i ∩ g_vU_v ≠ ∅.
- The bound Σ|U_iU_v| ≤ |G| − |U_v| is strict.
- K1 links have the Core(5) condition τ = α_viα_vj (the product at v).
- K2 is L3 at vertex j with S = {v,k}, after inverting U_vU_j ⊆ U_vU_k.
- Engine `link` (:87–90) is evaluated at τ_min. This is sound (M1): a link at τ_min attains a (T2) bound, so τ = τ_min is forced.
- Parent check: every link used by the 637 K certificates lies in a triangle with τ_min = τ_max (0 exceptions; `indep-run1` B_M1).

**P (rules-v1.md:142–165). ✓**
- X_j ∩ X_k is left-U_v and right-(U_j∩U_k) invariant (L0.5). Its double cosets are multiples of |G|/gcd(n_v, I_jk) = |G|/(4·gcd(r_v, α_jk)) (L0.4).
- Lower bound: max(T3 at τ_min, |X_j| + |X_k| − |G|), rounded up to a multiple of the unit u.
- Upper bound: min(|X_j|, |X_k|), lowered by one unit u when the forced containment violates K2. The smaller side is tested; for equal sizes, both directions are tested.
- Bonferroni: ∪Y_j ⊆ G∖U_v. The left side decreases in each |X_j∩X_k|, so substituting the upper bound hi is conservative. "≥ 1" correctly refutes the strict inequality.
- The PB value does not depend on τ at all.
- Engine `p_bounds` and `rule_P` (:117–151) match.
- In all 20 PB orbits it is Bonferroni that fires, not P-pair (P-pair fires in 0 of them; `labelled-run1` §4).

**N2 (rules-v1.md:167–185). ✓ for all 5 marker orbits.**
- τ is even and τ ≤ 4. τ = 4 gives links and then 2 + 2 ≤ 3, so τ = 2.
- At a vertex v with r_v odd, X_j∩X_k = Z_jk with |Z_jk| = |G|/4, using K2 and u = |G|/4.
- Q is divisible by lcm(8r_vr_jr_k, 8r_vr_jr_l, 8r_vr_kr_l) = 8r_vr_jr_kr_l (pairwise coprime, cofactors 1 allowed). So the three Z's of each triple coincide, and all six coincide.
- Then |∪X_j| = 5|G|/4.

**F / H1 / H2 (rules-v1.md:187–219). ✓**
- (F1): g_lU_lH is t_l left H-cosets. t_l = 1 ⟺ U_l ⊆ H.
- (F2): the trace in C = yH is y(U_l∩H). Translating by z⁻¹ gives pairwise disjoint left cosets in H of index λ_l. Sun(s) applies in H.
- (F3): U_iU_l ⊆ HU_l, and |HU_l| = t_l|G|/m.
- H1 (M-S 3.7): UV = UW, VU = VW and WU = WV give UV = VU, so UV is a subgroup, proved rather than assumed.
- H2:
  - τ = 2.
  - U_vU_a = U_v(U_a∩U_b) = U_vU_b = X.
  - X is right-invariant under W = ⟨U_a, U_b⟩, so X = U_vW.
  - [G:W] divides 4, and W ≠ G.
  - Index 4: W = U_aU_b by cardinality, and t_v = 2.
  - Index 2: U_v ⊆ W.
- Engine `fibre_search` and `rule_FH2` (:161–248):
  - all t, all met-coset sets;
  - one valid label symmetry (:182);
  - F3 at every t = 1 vertex (:192);
  - F2 per coset (:203);
  - **both** H2 alternatives for the **same** (a,b) (:245–247).
  - No coverage or balance constraint is imposed.
- **Minimal counterexample inside proper H.** F2 with s = 5 uses Sun(5) in the proper subgroup H. This is legitimate, because §0 (rules-v1.md:30) minimises over the full target, so proper subgroups satisfy full Sun k = 5. It is not circular.
  - Parent finding: under the engine's (non-hereditary) F2, all 22 FH2 certificates (900 labelled patterns) **need** this s = 5 clause; without it, 0 of 22 are refuted.
  - With hereditary F2, all 22 are refuted without minimality (22 of 22, at saturated and at e = f = 1 exponents). Hereditary F2 applies L0.6 or Zhu to every sub-family of a coset's traces; sub-families of pairwise disjoint cosets stay disjoint.
  - So the minimality frame is valid but avoidable (optional O-1).

**L8 (rules-v1.md:221–241). ✓**
- M1 is covered above.
- M2:
  - T, K and P read r only through gcd(r, α) for α ∈ {1, 2, 3}.
  - In F, λ_l = (4/m)r_lt_l. No prime ≥ 5 is common to two λ's.
  - min v₂ is capped by the other endpoint at 2. min v₃ is capped at 1.
  - Hence 16 = 2⁴ and 81 = 3⁴ saturate every pairwise gcd (v₂(r_E2) ≥ 2 and v₃(r_E3) ≥ 1 already suffice). Kills are monotone in the gcds.
- Runtime check: rule-by-rule agreement of the parent's symbolic flags-only form with a parent numeric general-index form at 5 r-instances. The instances are primes 5–17 and 19–37 with ×2/×3, ×4/×9 and ×16/×81; primes 41–59 with ×128/×243; and all cofactors 1 with ×2/×3. Result: 528,980 rule evaluations and **0 mismatches**. FH at the smallest exponents gives identical kills (`indep-run1` C_L8).

**Lemma R and the S-D refutation (proof-v1.md:31–89). ✓ after F-1.**
- (R1): g_j ∉ U_vU_j, so D_j and U_vU_j are distinct double cosets.
- (R2) follows from L0.4.
- (R3):
  - U_vy = U_vg_ju ∋ g_ju.
  - wU_j ∩ U_vw = (U_v ∩ wU_jw⁻¹)w.
  - The index is |U_vwU_j|/|U_j| = d_j, since w ∈ D_j.
  - Left/right orientation and the conjugate were both checked.
- (R4): c_j = w_jw₀⁻¹ ∈ U_v. Right-translating and then inverting gives disjoint left cosets in U_v, with s ≤ 4.
- (R5) needs F-1.
- Core(5) form: |D_j| = s_j|G|/4, with s_j ≤ 4 − α_vj and d_j = s_jr_j.
- S-D steps:
  - Step 1: D_j = Y_j and d_j = r_j for j = 1, 3, 4.
  - Step 2: Y_1, Y_3, Y_4 are disjoint, by R5′ and coprimality.
  - Step 3:
    - τ₀₁₂ = 1 (T2), and τ₀₂₃ = τ₀₂₄ = 2 (T1 with r₂ odd, and T2).
    - The apex-2 sets have size |G|/4 = |X₀|, so X₀ ⊆ X₁∩X₃∩X₄.
  - Step 4: G∖X₀ = Y₁⊔Y₃⊔Y₄.
  - Step 5: D₀ ⊆ G∖X₀.
    - Meeting Y₃ or Y₄ is impossible, since gcd(s₀, r_j) = 1 for r_j coprime to 6.
    - So D₀ ⊆ Y₁, which forces s₀ = 1; meeting Y₁ would need s₀ = 2. Contradiction.
- The parent symbolic replay of these numbers is in `indep-run1` F_SD_replay.
- **Lemma R on genuine data:** R1–R5 and the Core(5) form hold on every vertex of every realisable control (§3), with 0 violations.

**Other requested points.**
- **Quantifiers:** K needs every pair of S; F2 needs some pair; T2 is checked at all apexes. All correct.
- **Products are never assumed to be subgroups.** Exceptions are H1 and H2, where it is proved.
- **Divisibility:** L | T; τ_min by lcm; Q in N2; u in P2.
- **Containment directions:** L2, K1, K2 and P4.
- **Double-coset increments:** u ∈ {|G|/4, |G|/8, |G|/12}; |X_j| is always a multiple of u.

## 2. Finite bridge: Codex engine-note runtime items 1–4 (parent code, no worker imports)

**(1) Independent canonical keys.**
- All 3¹⁰·6² = **2,125,764** raw triples were canonicalised: lex-min α over S5, then the min marker pair over the stabiliser, with none sorting after the vertices. This gives **21,150** codes over **792** α-orbits.
- Result: exact **set equality** with the 21,150 extract records, with no missing and no extra keys.
- Labelled coverage, summing orbit sizes by record rule: T 2,091,281; K 33,091; PB 396; N2 36; FH2 900; SURVIVE 60. The total is 2,125,764.
- These equal the worker's `core5_check_v2` counts (`evidence/check-v2-run1/summary.json` 81db2c11…ff34; read as data only).
- Cross-checks: Burnside gives 792 / 21,150. A direct labelled classification of all 2,125,764 triples (`labelled-run1`) gives identical counts, and its 60 unkilled triples are exactly the S-D orbit.

**(2) Every serialized witness is checked against its own decoded pattern**, with no first-firing assumption:
- **T (20,465):** the recorded τ_min and τ_max must equal the recomputed values, and τ_min > τ_max.
- **K (637):** every pair in S is K1-linked; the recorded total equals Σα_iv/4; and the total is ≥ 1.
- **PB (20):** the recorded value equals the recomputed Bonferroni value, and the value is ≥ 1.
- **N2 (5):** the witness is exactly `[]`, and all ten α equal 2.
- **FH2 (22):**
  - α_ab = 1;
  - the recorded V2 equals the recomputed V2 = [2,3,4];
  - case (i) and case (ii) are both refuted by the parent's own full enumeration (3,456 and 32 assignments, with no symmetry reduction);
  - the recorded counts 864 / 16 equal the exhaustive space with one inside vertex pinned (3,456/4 and 32/2).
- **SURVIVE (1):** exactly `1122333333/10`, which is the S-D pattern of proof-v1.md:25–28.

**Own decision of every orbit**, independent of the records: hit-set histogram over the 21,150 orbits:

| Hit set | Orbits |
|---|---:|
| K+PB+Ppair+T | 19,972 |
| K+PB+Ppair | 559 |
| K+Ppair+T | 380 |
| Ppair+T | 109 |
| K | 78 |
| FH2 | 22 |
| PB | 20 |
| N2 | 5 |
| PB+Ppair+T | 4 |
| NONE | 1 (S-D) |

- **No orbit other than S-D is left unkilled by the parent's own rules.**
- Every record's rule is contained in the parent's hit set for that orbit.
- No FH2 certificate pair refutes only one case. Among the 23 orbits that reach the FH stage, 0 pairs refute only one case.

**(3) Strict rejection**, demonstrated by **46 mutation fixtures**. All 46 are rejected, each for its expected reason, and the pristine input has 0 errors. The fixtures cover:
- malformed lines: 2 or 4 fields, CR, an empty line, no final newline;
- bad codes and markers, and an unknown rule;
- duplicate, missing and extra keys, including a non-canonical equivalent key;
- invalid vertices: 5, 7, a repeated vertex, and v ∈ S;
- wrong witness shapes and types (string or bool bounds), non-canonical JSON, and an N2 witness with payload;
- altered T bounds, and a T witness on an unkilled triangle;
- an altered K total, and a K witness with an unlinked pair;
- an altered PB value, and a PB witness at a non-failing vertex or set;
- an FH2 record with shortened V2, an altered count, or α_ab ≠ 1;
- **a one-case-only FH2 forgery** (`1111122221/01`, pair [1,2], in which only case (ii) is refuted);
- a killable pattern labelled SURVIVE, and S-D forged as T or as N2;
- inconsistent run.json: counts, engine sha or certificate sha;
- inconsistent survivors.json: markers, n_representative, or emptied;
- altered engine bytes, a gzip/extract provenance mismatch, and record order.

**(4) Hashed verifier and result:**
- `bridge_verifier_v1.py`, sha256 `2d7fff78cf042d8a09d16199c69c5151d893b340e6717b998714fdbe166f7659`;
- `bridge-run1/RESULT.json`, sha256 `d741396cd8c4428f404db16b47845e4b301224c6a35a415c9f67d0324bdd7278`.

RESULT.json records the hash of every input and checks the following bindings:
- extract e9bd7c54…5bb2;
- engine 65ce5a00…2eb1;
- run.json 7910d9f8…a89;
- survivors.json fe87e4ea…ef35;
- certificates.tsv.gz 1c7e8008…be85, which decompresses byte-identical to the extract;
- run.json engine_sha256 and certificates sha.

## 3. Controls (parent permutation code; sanity only, not gate evidence)

- **Menon configurations**, built from the printed generators and representatives of arXiv:2608.15873v1 Thm 3.1 and §5, with left cosets g∘U:
  - A5 (6,6,6,10,15) and its five 4-subconfigurations;
  - C2×S4 (4,6,6,6,6) and its five 4-subconfigurations;
  - C2×S4 (6,6,6,6,16).
- **Other configurations:**
  - Z5 with five cosets;
  - Core-shaped realisable 4-configurations: Z4, Z2³ four lines (all α = 2), Z2³ three lines plus a point (E2; K at its Σ = 3 boundary), S4 four point stabilisers (all α = 3), and S4 three stabilisers plus a C2 (E3; τ_min = τ_max = 2 links).
- **Results:**
  - All 19 configurations are disjoint.
  - No general-index rule fires, and no Core-form rule fires on the Core-shaped ones.
  - **0 lemma-predicate violations on actual data**, covering L0.3, T1–T3, L2, L3, K2, P2–P5, the PB upper bound, H1/F1–F3, and Lemma R1–R5 with its Core form.

## 4. Findings and exact corrections (all MINOR; none affects a certificate or the survivor)

- **F-1 (load-bearing justification).** proof-v1.md:40 and :53 (R5), used at :64 and :82.
  - Problem: "Apply (R4) with s ≥ 2" yields only *some* pair of S_C.
  - Correction (R5′): by (R3), C meets g_jU_j and g_kU_k in disjoint pieces of indices d_j and d_k in U_v. Translate by w₀⁻¹ and invert to obtain two disjoint left cosets in U_v. L0.6 then gives gcd(d_j, d_k) ≥ 2.
  - The Claude F-1 and Codex reviews agree.
- **F-2 (imported justification, load-bearing for R1).** M-S arXiv v1 p.10, Lemma 4.4 second bullet: "Lemma 3.10a) implies that 3 divides r1". It is used by Prop 4.5 and hence README.md:45.
  - Problem: 3.10 is applied outside its hypotheses, because there is no common a with coprime cofactors.
  - Patch:
    - T = [G:U₁∩U₂∩U₃] = 4r₁r₂r₃τ.
    - 12r₂r₃ | T gives 3 | r₁τ.
    - |U₂(U₁∩U₃)| = τ|G|/4 ≤ |U₂U₁| = |G|/2 gives τ ≤ 2.
    - Hence 3 | r₁.
  - The C1 replay gives an independent lane-lemma derivation of Prop 4.5.
- **F-3 (wording).** proof-v1.md:18 and rules-v1.md:30. Add: "R1's case analysis applies to the configuration inside the minimal G, so that configuration is Core(5)-shaped."
- **F-4 (citation).** README.md:50 and rules-v1.md:140. The claimed misprint in M-S Lemma 4.4 does not exist.
  - Evidence: rendering the lane's own PDF p.9 shows "α(U₂,U₃) ≠ 2"; pdftotext prints ≠ as "6=" (`tmp/ms-p-09.png`).
  - Correction: delete the claim.
- **F-5 (labels).** README.md:38–39: swap (⇐) and (⇒). The "(⇒)" block proves the load-bearing direction, Core(5) ⇒ Sun.
- **F-6 (unused commentary).** rules-v1.md:139. With α_UV = 1 and α_UW = α_VW = b, the forced links are at U and V (τ = b = α_UV·α_UW), not at W (whose product is b²). Name U or V instead.
- **F-7 (citation).** README.md:42 and :44, proof-v1.md:17. Zhu Thms 2.2 and 3.1 are Sun k = 3 and k = 4, which imply Props 4.2 and 4.3. Thm 3.1 as printed in arXiv:0807.2207v1 omits "pairwise disjoint" (a source typo; its proof uses it). Cite Zhu Thm 1.1 instead.
- **F-8 (imported).** M-S p.10, Prop 4.5 proof: "multiple of |G|α/4" should read "multiple of |G|/4", since gcd(4r₂, 12r₃r₄) = 4. Only the latter is used.
- **F-9 (control description).** proof-v1.md:110 and rules-v1.md:266. C4 is a shared-code recheck, not independent verification. Two of its three demos target the wrong rule, as already acknowledged at README-addendum-v1.md:12–16. Replace it with the parent bridge (§2).
- **F-10 (cosmetic).**
  - rules-v1.md:98: "gcd(α, r_z) = α exactly when…" is false for α = 1, but harmless.
  - proof-v1.md:55: the symbol s_j clashes with s = |S_C|.

**Optional hardening (not required):**
- **O-1.** Use hereditary F2, so that minimality is not needed by any certificate (22 of 22 FH2 orbits still refuted).
- **O-2.** In H2 case (ii), U_vU_a = W gives g_aW = g_bW ≠ g_vW for v ∈ V2. This is an extra valid restriction. It is unused, and the engine's case (ii) search correctly does not force a and b into distinct cosets.
- **O-3.** Sun(3) follows from L0.6 + Prop 4.2, and Sun(4) from L0.6 + Props 4.2 and 4.3, by gcd-type analysis. So the C1 lane-lemma certificates could replace the Zhu and M-S imports.

## 5. Correctness boundary

- **Classical, computer-assisted, not Lean-checked.**
- Parent code: `indep_check_v1.py` (dee4861c…3b23), `indep_labelled_v1.py` (e6a22ca5…3b9c) and `bridge_verifier_v1.py` (2d7fff78…7659). All are standard library only and ran on CPython 3.14.3, the same interpreter family as the worker, with independently written source.
- Imports remaining on the essential path:
  - Zhu Thm 1.1 (statement);
  - M-S Prop 4.5 (audited, with the F-2 patch; alternatively the C1 replay);
  - standard group facts.
- Hand re-derivations are this desk's own. They agree with the Claude (dc4f90c5…e576) and Codex (84b3dadd…2002) written-math reviews. F-1 to F-8 were reached here before those reviews were read. F-9 (C4 is not independent) follows the Codex engine note, and F-10 follows the Claude note.
- Not done here: any review of proof-v2 or the erratum.

## 6. Hashes (sha256)

**Lane, frozen v1:**

| File | sha256 |
|---|---|
| README.md | 6bff400c970958dd2c1077d76fb284a6869351702aeff286f48471d23945a75e |
| rules-v1.md | cb86c16836d929a21256c34f0a87a5fc71788b970a6e1052751a69d637d1390f |
| proof-v1.md | e35bfa0ecb946f604d3162ea8259f4c61b7abae7bece91c03b2c21296995c698 |
| README-addendum-v1.md | af4a051fe829483f2ab0b04a3c450cb8ec189f0dafc93e4099a06d7e8bd10474 |
| code/core5_engine_v1.py | 65ce5a00cdd513ef55533b3507a8e8a37dcc88e9d389a541978a0f23cb952eb1 |
| engine-v1-run1/certificates.tsv.gz | 1c7e8008a35ac1bd5dbc6be2b3ec886a36b62765a62ef2a15a5ff8f0f541be85 (uncompressed e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2) |
| survivors.json | fe87e4eac3a97b1a0442032cc23ca11b8d470f766c04c54d1515b2e8a16bef35 |
| controls.json | d6478d0c237b361586c757efd3f8ec49cb85e0058276ebb848ea1ab2744671b8 |
| run.json | 7910d9f8e93388544373651f557d8e2d737a75eec4d5824a288a8cb6b0ce5a89 |
| freeze-v1.sha256 | bac763413e774d729cc75b221b6ed13ed3e15f75b6173057fad8b9b5c4071fa3 |
| proof-v1.sha256 | 0dfdb4e80f4d11fce9b776621bb6dc1b32a16e9fcac671e4d1e2e0d6942cbd0c |

**Sources** (all match README §5):

| File | sha256 |
|---|---|
| arxiv-1803.03569v1.pdf | 3c3341ba5c642fb4174430ffab4bbe92a10255111017de146f4a73c69a7e3ffe |
| arxiv-0807.2207v1.pdf | 5f5b9a7172ec55ef7ffb629bf123de9538fcc821d24f499ee9a91c0e2e205c62 |
| arxiv-math0501451v4.pdf | 9e62667f0c4ae77051a4b3da162428f91853dd7e995f0e18fbb8713ea03318e2 |
| arxiv-2608.15873v1.pdf | 2717059bdf6a7d38e92226bb35a887a8502a499a6808e4024961b87bd14f3296 |
| arxiv-2607.24655v1.pdf | 33bffe0628027510d69a51ce5f39ab72541e5562f4fcd29dd1fe2903e8728b08 |

**Campaign files:**

| File | sha256 |
|---|---|
| screening contract | 8c61ff0049d603fabca7235a5eb556f7d81b50c7eceef24a3b3aabc559ed1367 |
| screen v1 | e01d8a44e6ca3a2defce32bb839d5c904c0f740852ab6c1c440e5c4394a2ff09 |
| certificates extract | e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2 |
| Claude note | dc4f90c5e5dd1e4b5ec63f51ce693c9a5bc8c355a6e8f6b9c1dc9c961765e576 |
| Codex note | 84b3daddf7866c94301e3653c69661233287060772a6d8d33f9f201ad4a02002 |
| Codex engine note | d87212a9fb4d53951769f3bd1a03b8ee660d77b72709f344fecfe6f1f533b3d1 |

**Seen but out of scope** (not audited):

| File | sha256 |
|---|---|
| proof-v2.md | 8eeb7976abb3a41bb5471029de441f477223ed13147bbcd2c46046c8e877c5ab |
| rules-v1-erratum-v1.md | f1e51b37e3d390346c2c2218054bbcabf2fc492d106137ffda4f9f488611bc56 |
| README-addendum-v2.md | 5a14260e1337ba25b3463d76551dd4a7059121a6dc0b28e6964564cf147b886f |
| code/core5_check_v2.py | 9e4aac2a5dadec244fb27bffa90bff95ee8bbb859063acef190531d8d0848ae2 |
| code/controls_v2.py | 52372b7388eaa5bb6d323bd4196c6d211a9d36a524aa7c94fb11dd2008505667 |
| check-v2-run1/summary.json | 81db2c1113eab81600297babca6291c2ecb55478c7885a217f0978731467ff34 |

**Desk outputs:**

| File | sha256 |
|---|---|
| indep_check_v1.py | dee4861c6293106571e9f0e61db03d551a02546d8ade563c3a9ad15ffc7b23b3 |
| indep-run1/summary.json | 6e477e704ae92f2aee19125639ee3e6cbe52f1b25b98c169679bedbe1c610fd1 |
| indep_labelled_v1.py | e6a22ca543bef528cefd315bdbeac703ad3d5ee7e4a663053605656c7e723b9c |
| labelled-run1/summary.json | e367dfc43be52b54d09f0cb53f4671bc761437e1d4f8fb0343a0578ba81d3ecf |
| bridge_verifier_v1.py | 2d7fff78cf042d8a09d16199c69c5151d893b340e6717b998714fdbe166f7659 |
| bridge-run1/RESULT.json | d741396cd8c4428f404db16b47845e4b301224c6a35a415c9f67d0324bdd7278 |
