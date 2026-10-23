# K62-R2MIX-v2: independent hostile mathematical review (parent erratum v1 applied)

**Object.**
- Proof: `K62-R2MIX-v2.md` `b75e6dc7…0806`, lines 1–283.
- Frozen scope: `12a64d8e…e4e5`.
- Overlay: parent erratum v1 `c8528a68…badf`, items m1–m3.

**Basis.** This review is written reasoning only. I used no tools, computation, file reads, edits or delegation. I did not use the Codex review or any other review as evidence.

Not verified by me:
- any sha256, byte count or line count;
- the excerpt manifest;
- pending or verdict text outside the quoted excerpts: M3R-v2 R2N (l.121–150), MK-v2 §7(b), MK-v2 Lemma R4*/c0, LFC/INV verdict l.31.

All

six erratum Old spans match the quoted source text exactly once: proof l.4–5, 235, 237, 248–249 and 264, and scope l.8.

**Result.** 0 FATAL · 0 MAJOR · 6 MINOR.
- No gap in Lemmas 1–4 → Prop 5 → R2X, at full M3(1,1) scope: e_d ≥ 4, f_t ≥ 2, all five 5-placements, unbounded exponents and w's, arbitrary groups via R0.
- No gap in Lemma 6 → Thm 7 → R1X. R1X needs one R0 clause at the arbitrary-group scope (MINOR-2).
- No counterexample to any principal statement or step was found.
- The MINORs are labelling, provenance, ancillary sentences, and that one R0 clause.
- These are recommendations only. Labels stay CANDIDATE_UNVERIFIED until the parent verdict.

## 1. Per-claim verdicts

| Claim (lines) | Verdict |
|---|---|
| Lemma 1, light fibres (78–89) | ACCEPT |
| Lemma 2, product separation [new] (91–95) | ACCEPT |
| Lemma 3, d-system of either family (98–114) | ACCEPT |
| Lemma 4, chain at t (116–143) | ACCEPT as stated; its "Lemma C re-proved" label is MINOR-1 |
| Proposition 5 [new] (145–164) | ACCEPT |
| Theorem R2X [new] (166–190) | ACCEPT |
| Lemma 6 = M3R-v2 Lemma A (193–198) | ACCEPT |
| Theorem 7, x′_tu = 2 on O′ only (200–221) | ACCEPT; label is MINOR-1 |
| Corollary R1X (223–224) | ACCEPT for finite G; ACCEPT-WITH-FIXES at arbitrary-group scope (MINOR-2) |
| Corollary 6.1, NR (227–228) | Same as R1X |
| Corollary 6.2, M3E (229–231) | ACCEPT only as the implication "MK Theorem M3R ⇒ M3(1,1) empty" |
| Ancillary: header, §1, §7, §8, §9, package | ACCEPT-WITH-FIXES (MINOR-1, 3–6) |

## 2. New-proof derivation, re-derived independently

**D1. Directions and translation**
- For y = α, the y-configuration is Γ = (g_j, U_j). The y′-configuration is Γ* = (g_j⁻¹, g_jU_jg_j⁻¹), and Γ** = Γ by INV(a). For y = α* the roles swap.
- In any configuration (h_j, V_j), Lemma 1's W = ∩_Q h_jV_jh_j⁻¹ is the Q-intersection of the inverted configuration's subgroups.
- Hence [G:W] = lcm(n_t,n_u)·y_tu at d in y′ (Prop 5(ii)), and [G:W] = T_{y′}(V∖{t}) at t in y (Step 2).
- Lemma 2, Lemma 4 with z = y′, and Step 1 all live in Π^{y′}. So Step 1's gcd is exactly Step 2's granularity.
- Lemmas 1–3 and Prop 5 are translation-free.
- Theorem 7's g_t = 1 translation fixes the subgroups and conjugates every inverted subgroup by one common element, so q = x′ survives. ✓

**D2. Lemma 1**
- The number of fibres is [W : W∩U*_v] = [G : W∩U*_v]/[G:W] ≥ lcm(n_v,[G:W])/[G:W].
- Avoidance: if w = g_jbg_j⁻¹ moved g_vu into g_jU_j, then g_vu ∈ g_jU_j ∩ g_vU_v, which is empty. ✓

**D3. Lemma 2**
- From p⁻¹q = ab we get pa = qb⁻¹ ∈ pU_j ∩ qU_k = g_jU_j ∩ g_kU_k, which is empty.
- Factor order is immaterial: AB = U_v ⇔ BA = U_v by inversion. The same order is used in Lemma 4(c) and Prop 5 anyway. ✓

**D4. Lemma 3**
- Labels at d are λ_c = 3^{f_c}5^{h_c}w_c and λ_{i*} = 3·5^{h*}w_*.
- Every f ≥ 1, f > 1 only at t (f* = 1), at most one h ≥ 1, and the w's are coprime. So all 15 pairwise gcds equal 3 in each 5-placement (d, i*, t, p, absent).
- Sun(4) therefore excludes every 4-subset, so |S_F| ≤ 3.
- Degrees are n_d/2 and n_d/4; the latter uses z_{d i*} = 1.
- (b) Inclusion–exclusion gives #neither = n_d − n_d/2 − n_d/2 + #both, and the Lemma 1 fibres lie among the "neither" fibres.
- The gcd equals 2^{1+v2 z′} and needs only e_d ≥ 2. Its 5-part is 1: h_d ≥ 1 forces h_c = h_{c′} = 0, and 5 ∤ z′. ✓

**D5. Lemma 4**
- t is never added to the chain, and v3 T_0 = 1.
- gcd(n_e, T_{r−1}) = 6 in every placement. If e = p, then n_d, n_{i*}, the earlier ℓ's and every k ≤ 3 are 5-free.
- k_e = 6μ(Π_eW_{r−1}) ≤ 6μ(Π_eΠ_d) = 3. Since ℓ_e is prime to 3, v3 increments iff k_e = 3.
- (b) Three nested sets have equal size, so they coincide; then a = xb⁻¹ ∈ Π_d.
- (c) [Π_d:A] = 3ℓ_e, [Π_d:B] = 3·5^{h*}w_*, and [Π_d:A∩B] = τ·3·5^{h_e+h*}w_ew_* in every placement, so the ratio is τ/3.
- Cross-check with L1 (T3) at apex e: μ(Π_eB) = (n_d/2)(τ/3)/n_d = τ/6. ✓
- (d) Γ = 2·3^{min(f_t,1)} = 6 for every f_t. ✓

**D6. Proposition 5**
- (i) S_F ⊆ {t,i*}∪O′ with |S_F| ≤ 3. Summing over the n_d/2 fibres meeting t gives ΣN_u ≤ n_d − s.
- (ii) Lemma 3(b) with z = y′ and z′ = y gives N_u ≥ n_d/4 from the R2 entries.
- (a) N_e ≤ n_d/4 − s; the argument is still valid if this bound is negative.
  - A fibre meeting e but not t also misses i*, and it is not F_d.
  - There are n_d/4 + s fibres meeting neither t nor i*, so deg_d(e) ≤ n_d/2 − 1, a contradiction.
  - Lemma 2 (contrapositive, y′-configuration) and Lemma 4(c) then give τ_{y′} ∈ {1,2}.
- (b) Let r be the number of entries equal to 1. Then n_d + r·n_d/4 ≤ ΣN_u ≤ n_d − s, so r = s = 0, every N_u = n_d/4, and equality holds fibre by fibre. ✓

**D7. Theorem R2X**
- Step 1 applies Prop 5(a) to all four e, with its hypothesis supplied by 5(b), then Lemma 4(d) with z = y′.
- Step 2 applies Lemma 1 at t in y with Q = V∖{t}, giving at least n_t/6 empty fibres.
- Step 3: the labels 2ℓ_u and 2^{e_d−1}5^{h_d}w_d have pairwise gcd exactly 2 in every placement, so only the |T| = 3 instance of LFC(c) is used.
- The weight c sums to at most 1 on each fibre and to 0 on the empty ones. The count then reads 11n_t/12 ≤ 5n_t/6, which is false. ✓

**D8. Lemma 6**
- γ_d = 4 gives 5 | 2^{e_d−2}5^{h_d}w_dτ.
- (T3) and (T2) at t give τ/6 ≤ ½, so τ ≤ 3 and 5 ∤ τ. Hence h_d ≥ 1. ✓

**D9. Theorem 7**
- (i) By measure, D_a = D = D_b.
- (ii) Every pairwise gcd in {a, b, j} is ≤ 2, so Sun(3) forbids a common right coset:
  - for j ∈ O′, by E3-a;
  - for j = d, because there is one 5-marker;
  - for j = i*, the only danger is a = p (or b = p) with x′_{t i*} = 5, and Lemma 6 with z = x′ excludes it.
- (iii) μ(L) ≥ 1/n_t is load-bearing: without it both cases in (iv) become non-strict.
- (iv) x′_tc = 4 fails by measure. x′_tc = 1 gives gcd(ℓ_c, n_d/2) = 1, so Sun(2) separates D_c from D_d and 1/6 ≤ μ(R) − ½ < 1/6. E3-a excludes 3 and 5. ✓

**Probes that broke nothing.**
- All w = 1 (equal indices; equal subgroups are allowed).
- Each 5-placement in Lemma 3, Lemma 4(a)/(c), Step 3 and Thm 7(ii)/(iv).
- Unbounded f_t.
- s ∈ {0, n_d/4}.
- F_d counted exactly once.
- Chain order: k_e depends on it, the conclusions do not.
- α and α* each in the role of y.

## 3. Import domains at their original scopes

| Import | Used in | Accepted domain | Check |
|---|---|---|---|
| R0 (README §1; LFC/INV item 6) | §0, R2X, R1X | Arbitrary G; preserves indices, intersections, disjointness, conjugated intersections | ✓ for R2X. R1X also needs descent of a product set (MINOR-2) |
| L0.1, L0.2, E1/L0.3 | Lemmas 1, 4; Thm 7 | Finite G; any disjoint pair | ✓ |
| LFC (a)–(c) | Lemma 3 (at d, both families); Step 3 (at t, family y) | k ≤ 7, finite G, any vertex | ✓ (c) used only at \|T\| = 3, 4 |
| INV (a)–(b), E6, E7 | §0; Lemma 1's last clause; Thm 7's q = x′ | Pairwise disjoint left cosets | ✓ |
| L1 (T1)–(T3) | Lemma 6 | General indices | ✓ γ_d = 4, γ_t = 6 |
| VFC (V1)–(V4) | Thm 7 at v = t, g_t = 1 | Normalised vertex | ✓ (V3) used only at \|T\| = 2, 3 |
| E3-a = Z11(a) | Thm 7 (ii), (iv), for x′_tu | Proof sub-claim inside accepted C2 | ✓ see the three points below |
| Sun(2); Sun(3), Sun(4) | Thm 7(iv); Step 3 and Thm 7(ii); Lemma 3(a) | Every group (L0.6; Zhu) | ✓ |
| E3 light fibres / C2(b); RC | — | Re-proved in Lemmas 1, 3 and Step 2 | Not imported ✓ |

E3-a check in detail:
- The Z11(a) proof covers x ∈ {α, α*} and every 5-placement: E3 Lemma 2 excludes 3 and also excludes 5 when h_d ≥ 1; a Sun(2) pair argument excludes 5 when h_d = 0.
- Under orientation (1,1), both Γ and Γ* satisfy C2's normalisation α_{d i*} = 1, and the K6.2* marker hypotheses hold.
- It is not used as a strengthened Lemma 2 statement.

New-proof gaps, kept separate from the imports: none at FATAL or MAJOR level. The re-proved pending arguments (Lemma 4, Lemma 6, Theorem 7) are self-contained from the imports in the table.

## 4. Findings

**MINOR-1: "re-proved" overstates Lemma C and Theorem RR.**
- *Lines:* 14–15, 19, 73, 116. In the package: the §Outcome bullet ("Theorem RR re-proved as Theorem 7") and five-line item 2.
- *Issue:*
  - Theorem 7 proves x′_tu = 2 for u ∈ O′ only. It does not re-prove M3R-v2 RR's x′_{t i*} = 2 (RR step 5).
  - Lemma 4 omits the converse in Lemma C(b) (τ = 3 ⇒ 9 | T) and the bound z_{e i*} ≥ 3 in C(c).
  - Line 200 ("in the form needed") is already accurate.
  - Nothing load-bearing is affected, but a downstream reader could take x′_{t i*} = 2 as available.
- *Fix:* replace "re-proved" with "re-proved in the form needed (Thm 7: O′-entries only; Lemma 4: no converse of C(b), no z_{e i*} ≥ 3)".

**MINOR-2: R0 descent of the R1 product condition.**
- *Lines:* 33–35, 223–224, 227–228.
- *Issue:*
  - An R1-instance also requires the set equality Π^x_tΠ^x_a = Π^x_tΠ^x_b.
  - Theorem 7 is a finite-G measure argument. So R1X and 6.1 at "same full scope" need this equality, and the family structure, to pass to G/N.
  - Lines 33–35 list neither. Both are true: N ⊴ G lies in every Π^x_j, so π(XY) = π(X)π(Y), and inversion commutes with π.
- *Fix:* add one clause to §0 or to the proof of R1X. R2X is unaffected because its hypothesis is α-valued.

**MINOR-3: §7 ancillary citations after the erratum.**
- *(a) l.235, erratum m1 text*
  - *Issue:* "Γ_{y′}(t) ≥ 18" uses the converse τ = 3 ⇒ v3 T ≥ 2, which R2MIX never states, and Γ_{y′}(t) is undefined in R2MIX. The fact itself holds in one line: T_{y′}({d,i*,e}) = 3·lcm(n_d, n_e, n_{i*}) has v3 = 2 and divides T_{y′}(V∖{t}), and f_t ≥ 2.
  - *Fix:* add that line and define Γ_{y′}(t) := gcd(n_t, T_{y′}(V∖{t})).
- *(b) l.238–239*
  - *Issue:* attributes the equivalence of the two product equalities to Lemma 4(b),(c), but 4(b) only derives both from k_e = 3.
  - *Fix:* add the one-line converse Π_eΠ_d = Π_e(Π_d∩Π_e)(Π_d∩Π_{i*}) = Π_e(Π_d∩Π_{i*}).
- *(c) l.234*
  - *Issue:* "single-family, t-local routes" misdescribes M3R-v2 obstruction (2), which already pairs y at t with y′-granularity, and obstruction (4), which is O-global.
  - *Fix:* reword.

**MINOR-4: mutation and necessity wording.**
- *(a) l.253–254, mutation 1*
  - *Issue:* the "no contradiction" claim fails in Prop 5(a)'s generality.
  - *Counterexample to the wording:* s = n_d/4. This is consistent with (i) and (ii); it forces N_e = 0. Then e has at most n_d/2 − 1 non-t fibres other than F_d, so deg_d(e) ≤ n_d/2 − 1 even without Lemma 2. The mutation's own bound 3n_d/4 − s − 1 shows the same.
  - For R2-rows, s = 0 by Prop 5(b), which does not use Lemma 2. So "Lemma 2 is load-bearing" stands.
  - *Fix:* add "for R2-rows, or whenever s ≤ n_d/4 − 1".
- *(b) l.269, mutation 8*
  - *Issue:* "Lemma 3 (a) fails" is literal only for the degree clause (deg_d(i*) = 3n_d/4); the three-piece cap is merely no longer derivable.
  - *Fix:* reword. The mutation correctly identifies y′_{d i*} as the orientation entry R2X uses. I draw no M13 inference from this.
- *(c) l.243–244 and l.258*
  - *Issue:* "needs both families" is true of this argument only and is not an impossibility statement; compare parent erratum M3R m4.
  - *Fix:* say "this argument uses".

**MINOR-5: provenance and package.**
- *Issue:*
  - The package's v1→v2 summary omits items (4) and (5) of the proof's own list at l.7–11.
  - v1 `90d399eb…` is not in the packet, so neither list is verifiable.
  - Navigation-only references outside the packet were not checked; none is a premise. They are at l.63, 169, 188–190 and 245–247.
  - Consistency note: the c0 value of 11/2 at r = 0 in MK erratum M1 equals Step 3's 11/12.
- *Fix:* align the package with l.7–11.

**MINOR-6: editorial.**
- *Issue:*
  - l.83 locally redefines U*_v := g_vU_vg_v⁻¹. For the α*-configuration this is the original U_v, which collides with §0's U*_v (l.42).
  - l.281's arrow "Lemma 3 → Lemma 4" suggests a dependency that does not exist: Lemma 4 uses neither Lemma 1 nor Lemma 3.
- *Fix:* rename the local symbol and drop that arrow.

## 5. Ancillary audit: what passes

- **Erratum m1–m3.** All three are wording-only and correct.
  - m1's "≥ 18" holds (see MINOR-3(a)).
  - Mutation 6 after m1: 11/12 ≤ 17/18, and the bound 1 − 1/Γ only weakens as Γ grows through 18, 54, …
  - m2 removes the unsupported claim that Prop 5(a) is non-vacuous.
  - m3's metadata disclosure is consistent with the package.
- **Mutations.**
  - Mutation 3 gives ΣN_u ≤ 3n_d/2 − s and deg_d(e) ≤ n_d − 1.
  - Mutation 5 needs n_t ≥ 12, and in fact n_t ≥ 18.
  - Mutation 7 gives deg_d(e) ≤ n_d/2.
  - Mutations 2 and 4 are descriptive and consistent.
- **Scope.**
  - The R2X, R1X and conditional M3E statements match the frozen targets. The fallback is unused.
  - 6.1 is not in the target list, but it is only the definitional conjunction R1X ∧ R2X.
- **Premise hygiene.**
  - R2N is unused.
  - M3R-v2's Lemma A, Lemma C and RR are re-proved in the form needed.
  - MK's Theorem M3R appears only in 6.2.
  - M13, GS, HD, GX, FH, DT-B/C and the CAP capped profiles are unused.
- **No hidden hypotheses in R2X.** It uses no E3 import, no Z11(a) no-5 claim, no y_{t i*}, no Lemma 6 and no bound on f_t. e_d enters only as e_d ≥ 2; this is an observation, not an extended claim.

## 6. Trust boundary

- **Sun instances actually invoked.**
  - Allowed-set sizes |T| = 2 (Thm 7(iv), and inside E3-a), |T| = 3 (Step 3, Thm 7(ii)) and |T| = 4 (Lemma 3(a)).
  - No |T| ≥ 5 instance appears in any step I traced, including E3 Lemma 2 and Z11(a).
- **Computer-assisted Sun(5) `2cf02436…5301` and Sun(6) `efe1d849…1e29`.** They remain transitive imports, through two routes:
  - the accepted LFC/VFC statements, which are proved for all |T| ≤ 6;
  - the K6.2* reduction that gives M3(1,1) its hypotheses and its relevance to Sun(7): Sun(6) for three 5-vertices, and the k5-record Prop 4.5.
- The conservative wording in §9 is acceptable. This review does not change any trust label.
- No Lean check, human review, novelty assessment or priority assessment has been done.

## 7. Still open

- M3(1,1) emptiness remains conditional on the pending K62-MK-v2 Theorem M3R.
- This corrected snapshot still needs a second-family review and the parent verdict.
- M13 orientations (1,3)/(3,1) are untouched.
- M5 and the rest of K6.2* with e_d ≥ 4 outside M3(1,1) are open.
- Marked K7, including 2- and 3-markers on different vertices, and marked K6.3 are open.
- Sun(7) is open.

Nothing in this review approves full M3, K62, K7, Sun(7), Lean, human review or novelty.
