# M13X v1: independent hostile mathematical review

**Object.** `K62-M13X-v1.md` b86bb186… (whole, X:1-332) and review package a87ccfcf…. The parent erratum f8dc60cd… is applied last; it only changes the pointers at X:313 and X:317.

**Method.** Written review only: no tools, computation, edits or delegation. Prior reviews and metadata were not used as evidence, and the hashes were not re-checked.

## Bottom line
- **0 FATAL / 0 MAJOR** in every mathematical claim group. Every claim is **ACCEPT**.
- **4 MINOR findings**, none load-bearing:
  - 2 in the §10 route diagnostics: the erratum-corrected pointers are still incomplete.
  - 2 in the interface table: bookkeeping and wording.

| Claim group (X lines) | Verdict | F/M/m |
|---|---|---|
| Lemmas 1, 1′, 2 (74-99) | ACCEPT | 0/0/0 |
| Prop. SG (101-129) | ACCEPT | 0/0/0 |
| R4S, P1, DEG (132-154) | ACCEPT | 0/0/0 |
| CIS, EQS (157-181) | ACCEPT | 0/0/0 |
| P2-P4, BUD, T16, ONE, TRI (185-231) | ACCEPT | 0/0/0 |
| FB (234-263) | ACCEPT | 0/0/0 |
| DEEP, Thm M13X, Cor M13X′ (266-294) | ACCEPT | 0/0/0 |
| §10 mutation diagnostics (311-317 + erratum); route diagnostics only, not claims | — | 0/0/2 (F1, F2) |
| Interface table (54-71); trust boundary | — | 0/0/2 (A1, A2) |
| Navigation note on (1,1) (318-321) | **Not accepted, not evaluated** | — |

## What was re-derived

**Lemmas 1, 1′, 2**
- **Lemma 1(a), light-fibre count.** The fibres in W_Q h_vΦ_v number [W_Q : W_Q∩Ψ] = [G:W_Q∩Ψ]/[G:W_Q] ≥ n_v/gcd.
- **Lemma 1(a), light fibres are empty of Q.** They miss every Q-piece, by disjointness from h_vΦ_v.
- **Lemma 1(b).** This is the LFC incidence identity. The own fibre lies inside the light set, and every other fibre is allowed.
- **Lemma 1(c).** The conjugated family of the x-configuration is the x′-family.
- **Lemma 1′.** It uses the own-family W = ∩Φ^x_j. Φ_vW ⊆ X_j and is disjoint from D_j by (V1). μ(Φ_vW) = [G:Φ_v∩W]/(n_v T_x(Q)) ≥ 1/gcd.
- **Lemma 2.** It uses the ordered product, with pa = qb⁻¹ landing in two disjoint pieces.

**SG**
- **Base step.** T₁ = lcm(n_d, n_{c₁}), because z_dc = 1.
- **gcd(n_e, L_{r−1}2^s) = 6.**
  - 2-part: min(1, ≥e_d).
  - 3-part: if e = t, the earlier vertices lie in O′ (v₃ = 1). If e ≠ t, then f_e = 1.
  - 5-part and w-part: trivial for the 5-marker on d, i*, t, some p ∈ O′, or absent. T_{r−1} has only the primes of n_d, the n_{c_j}, and 2.
- **Multiplier.** k = 6μ(Π_eW_{r−1}) ≤ 6μ(Π_eΠ_d) = 3.
- **Ruling out k = 3.**
  - Containment plus equal measure gives Π_eW_{r−1} = Π_eΠ_d.
  - Every element of Π_d is then ab with a ∈ Π_e and b ∈ W_{r−1} ⊆ Π_d∩Π_{c₁}. It follows that a ∈ Π_d.
  - So (Π_d∩Π_e)(Π_d∩Π_{c₁}) = Π_d. This is exactly Lemma 2's ordered hypothesis (v = d), with no subgroup or commutativity assumption.
  - Lemma 2 and LFC (a)-(b) act in the same z-configuration on left Π_d-cosets. Each piece meets n_d/2 fibres and misses h^z_dΠ_d, so #both = #neither ≥ 1. Contradiction.
- **Lifting to the full chain.** The 2-adic lcm step needs only 1 ≤ e_d.
- **Final gcd.** It is 6 at v = t (R = O′) and at v ≠ t.
- **Family tracking.** R4S (x-row) goes through Lemma 1(c), so it needs SG for z = x′. CIS goes through Lemma 1′, so it needs SG for z = x. Both are covered.
- **Remarks (1)-(3).** These are correct. Remark (3): v₃lcm(n_d, n_{i*}) = 1 and α*_{d i*} = 3, hence 9 | T_{α*}({d, i*}).

**R4S, P1, DEG**
- **Labels.** The labels are ℓ_u·x_vu (u ∈ O∖{v}) and n_d/2. Their odd parts are pairwise coprime for every placement, including the 5-marker on v itself, the 5-marker on i* (weight 0), and p = t.
- **Feasibility.** The positive support of any allowed set is allowed.
  - An entry-1 label is coprime to all other positive labels, so the support is a singleton.
  - Otherwise the 2-labels and d have pairwise gcd exactly 2, so the support has at most 2 elements.
- **Contradiction.** val = 4/6 + 1/4 = 11/12 > 5/6.
- **P1.** Follows from Z11(a) (both families) and INV(b).
- **DEG.**
  - DEG(a) and DEG(b) follow from R4S in x and in x′.
  - DEG(c) follows from (a) and (b) at the four K4 vertices plus (a) for x′ at the fifth vertex.

**CIS, EQS**
- **Setting.** Here q = x′. The weights are d_u = ℓ_u x′_vu and d_d = n_d/2.
- **Light-set bound.** Lemma 1′ on Q = V∖{v, i*} with SG (z = x) gives a union of measure ≤ 5/6.
- **Steps 1-5.**
  1. D = G∖X_a = G∖X_b.
  2. D ∩ D_j = ∅ for every other j in Q.
  3. Saturation: the union equals D ⊔ D_d, so both remaining D_c lie in D_d.
  4. Each such x′_vc is forced to be even and ≤ 3, hence equal to 2.
  5. Sun(3) makes them disjoint, and 2/6 + 2/6 > 1/2.
- **i* never enters.** D_{i*} is not used anywhere.
- **EQS, one-tight case.** D_a ⊆ D_b, and the labels ℓ_a and 2ℓ_b are coprime (Sun(2)).

**P2-P4, BUD, T16, ONE, TRI**
- **Base facts.** lcm(n_a, n_b, n_c) = 6ℓ_aℓ_bℓ_c. P4 follows by L0.1.
- **P2.**
  - Divisibility: x_ab is a power of 2 and ℓ_c is odd.
  - τ ≤ x₁x₂: take the apex opposite the smallest pair.
- **P3.**
  - Adding t first keeps every later multiplier ≤ 4, so the prime-to-6 part of T_x(S) is ∏ℓ°.
  - Hence the gcd is 6 for e ≠ t, and equality of measures is equivalent to equality of sets.
- **BUD.** It uses C2 for x′ in both families.
  - E3-C2 for α* (α_{d i*} = 1 holds) when x = α.
  - M13-A C2* for α when x = α*.
- **T16.** EQS at two apexes already suffices. τ ≤ 15 gives v₂τ ≤ 3, with equality iff τ = 8; this stays valid even if τ has a factor 3.
- **ONE.** Apex pairs determine the triple, so two such triples give ≥ 3 non-tight pairs.
- **TRI.** The case split is exhaustive.

**FB**
- **(N).** Used only at e ≠ t.
- **(i).** Every pair of Q has a non-t endpoint.
- **(ii).** DEG(c) gives N ≠ ∅.
- **(iii).** m_v = 2, so R_v is deep with τ = 8.
- **(iv).** ONE forces |I∖{t}| ≤ 2. Shapes (a), (b) and (c) exhaust the cases.
- **Cases (a) and (b).**
  - k = 2 = m gives Φ_bW = X^b_a (respectively Φ_aW = X^a_t).
  - P4 then gives two (2,4,4) triples with τ = 8.
  - t may be c or q in (a); only b's chain step is used.
- **Case (c).**
  - If {ta, tb} ⊆ N, there are two deep (2,4,4) triples with apex q.
  - If N = {ta, ab}, then n₄ ≤ 4, so the fifth vertex (≠ t) is isolated, against DEG(a).

**DEEP, M13X, M13X′**
- **Four-subset hypothesis.** FB supplies r_Q ≤ 4 separately for each family:
  - x = α*: Thm DG, α_{d i*} = 1, with G5/G6.
  - x = α: DG*, in (1,3).
- **Lone r = 5 alternative.** Removed by T16.
- **Step 1.**
  - Deep (4,4,4) triples number ≤ #triangles ≤ 2. Deep (2,4,4) triples number ≤ 1.
  - In the one-triangle branch, H_x = triangle + c₄c₅, which contains no (2,4,4) triple.
- **Step 2.** The diamond's complement {ab, ae, be, ce, qe} contains only one triangle.
- **M13X′.**
  - R0, via LFCV item 6, preserves the conjugated intersections, so α* is preserved.
  - The actual inversion gives α(Γ*) = α*(Γ), and (Γ*)* = Γ gives α*(Γ*) = α(Γ).
  - Class and markers come from the index tuple (E6).

## Findings

**F1: MINOR (diagnostic only). X:313, as replaced by erratum item 1.**
- **Defect.** The corrected text says DEG at t is unavailable only in Step 1. FB(ii) (X:240) also depends on it.
  - FB(ii) applies DEG(c)'s no-K4 conclusion to every 4-subset Q.
  - For Q ∋ t, DEG(c)'s proof (X:153-154) uses DEG(a) (degree ≤ 3) and DEG(b) at t.
  - Both rest on R4S at t for x′, which is exactly what mutation 2 removes.
- **Fix.** "…DEG at t is then unavailable in FB(ii) (no K4 on a 4-subset containing t) and in the final theorem's Step 1."

**F2: MINOR (diagnostic only). X:317, as replaced by erratum item 2.**
- **Defect.** The text says "The relevant FB pointer is FB(v)". Two further uses of ONE at apex t are omitted.
  - FB(iv) (X:245-247) applies ONE to deep triples R_v = Q∖{v}. When t ∈ Q and I∖{t} = Q∖{t}, R_v contains t. If its unique x = 2 pair joins its two non-t vertices, its apex is t.
  - Thm Step 1 (X:276-277) also invokes both clauses of ONE on a deep (2,4,4) triple whose apex may be t.
- **Fix.** "Relevant pointers: FB(iv) (excluding |I∖{t}| ≥ 3 when t ∈ Q), FB(v) when t ∈ {c, q}, and Step 1; the apexes in FB(vi) (c, q) and FB(vii) (q) are not t."

**Diagnostics 1 and 3-6 are accurate as route diagnostics.**
- (1): 9 | T_{α*}(V∖{t}) and f_t ≥ 2 give gcd ≥ 18, and 17/18 > 11/12.
- (3): without the own fibre, only #both = #neither ≥ 0 follows.
- (4): accurate at t for x = α.
- (5): Step 2 needs Step 1 in both families.
- (6): C2* is consumed only by BUD for x = α*.

## Import-domain and trust-boundary audit

| Import (literal scope) | Used at | Check |
|---|---|---|
| R0 + LFCV item 6 | X:27, 289-291 | Includes conjugated intersections ✓ |
| L0.1/L0.2/Lagrange, E1 | throughout | Applied per configuration; x_dc = 1 in both families ✓ |
| LFC (a)-(c) + erratum E3 | Lemma 1, SG, R4S | General, k ≤ 7; Γ* is a disjoint family by INV(a) ✓ |
| INV (a)-(b), E6, E7 | §0, P1, CIS, M13X′ | q = x′ in the x-configuration ✓ |
| VFC (V1)-(V4) | Lemma 1′, CIS, EQS | [GEN], applied to the x-configuration ✓ |
| E3 theorem, Lemma 1 (Z2) | §0 | e_d ≥ 4, e* = 2, t ∈ O, f* = 1 ✓ |
| E3 Lemma 2 + Z11(a) | P1 | Body covers x ∈ {α, α*} ✓ (see A2) |
| E3-C2 | BUD, x = α | α_{d i*} = 1 holds ✓ |
| Thm DG (§4) + G5/G6 + SHDGE 323-327 | DEEP, x = α* | Own-family hypothesis from FB(α*); §5 unused ✓ |
| M13-A DG*, C2* | DEEP x = α; BUD x = α* | DG* hypothesis from FB(α); C2* has no hypothesis ✓ |
| Sun(2), Sun(3) | via LFC(c) and (V3) | Direct uses. Sun(4) enters only via E3 and M13-A A1. Sun(5)/(6) remain computer-assisted transitive imports ✓ |

**Pending inputs are not premises.**
- R2MIX L1/L2 are re-proved as Lemmas 1/2.
- MK 3.3/3.4/3.6/3.7/§5/§6 are re-proved. R4S uses a route free of NR and GR.
- M3R is used for comparison only.

**Unused inputs, confirmed step by step.** M13 B/C/D, CAP/DT, SH, GS/HD/GX, FH and Sun(7) do not enter. The CI attributions at X:88 and X:159 are fully re-proved.

**A1: MINOR (bookkeeping). X:66.**
- **Defect.** X:66 cites the standalone K62-DG-erratum-v1 (e435430c…). It is not in the package and only repairs DG §5, which is unused.
- **Fix.** Mark it "(not used)" or delete it.

**A2: MINOR (wording, no mathematical effect). X:64.**
- **Defect.** "Any markers/orientation" is broader than the literal home of Z11(a). That home is the C2 proof under the §5 normalisation α_{d i*} = 1 (E3-erratum-v2:279-283).
- **Why the use is still in scope.** In M13, Γ satisfies that normalisation. The body covers both families. The M13 verdict (line 5) lists Z11(a) for (1,3).
- **Fix.** Write "both families, any markers; here α_{d i*} = 1".

**Informational, no severity.**
- X:67's "(with parent erratum 99276f6d…)" is harmless; that overlay does not touch A's DG* or C2*.
- X:326 "R4S → P1" is not a real dependency; P1 rests only on Z11(a) and INV(b).
- "One 5-marker" at X:28, X:124 and package §5 means "at most one". The proofs cover the absent case too.
- The package §5 CIS row lists (V1)-(V3), but X:160 also uses (V4).

## Not given
- No parent acceptance.
- No novelty, priority, significance, Lean or human-review approval.
- No conclusion on (1,1), the rest of K6.2*, K7 or Sun(7).
- The navigation note at X:318-321 is not accepted.
