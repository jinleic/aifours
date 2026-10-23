# Hostile review: K62-FULL v1, read with the worker erratum, provenance note and parent interface-precision erratum

I read the candidate `fabf04dd…` (lines 1–283), worker erratum F1 `4b8ae281…`, parent provenance clarification `15ce0f5d…` and parent erratum `61c1c02d…`, applied last. I also read the scope, the transition and the accepted-import excerpts. I took hashes and line ranges as supplied, because I ran no tools. The pending M13X, MK, R2MIX and M3R texts, the Codex review and all earlier reviews were not used as premises.

## Overall verdict

**ACCEPT-WITH-FIXES, editorial only: 0 FATAL / 0 MAJOR / 3 MINOR.**

I re-derived the proof independently. With the three overlays applied, Theorem K62X (`K62-FULL-v1.md:241-252`) follows from the accepted imports at their original scopes. No open MINOR finding touches a proof step.

This is a mathematical verdict only. The status stays CANDIDATE_UNVERIFIED. It gives no Sun(7), novelty, priority, Lean or human approval.

## Verdicts per claim group

| Group (lines) | Verdict | F/M/m | Basis |
|---|---|---|---|
| OR / R / FAM (70–92) | ACCEPT | 0/0/0 | Every accepted statement is used at its stated orientation scope; the family is swapped only through the actual Γ* |
| P1 (94–100) | ACCEPT | 0/0/0 | The h_d = 0 five-case is re-proved, not inherited from the Z11 heading |
| Lemmas 1, 1', 2 (103–121) | ACCEPT | 0/0/0 | Self-contained proofs |
| SG (123–141, erratum item 2) | ACCEPT-WITH-FIXES | 0/0/1 | Proof correct; MINOR-1 is in the remark only |
| R4S / DEG (144–157) | ACCEPT | 0/0/0 | Valid at every O-vertex and under every marker placement |
| CIS / EQS (160–177) | ACCEPT | 0/0/0 | Saturation and the Sun(2)/Sun(3) instances check out |
| P2–P4 / BUD / T16 / ONE / TRI (180–212, erratum item 1) | ACCEPT-WITH-FIXES | 0/0/1 | MINOR-2 is the wording of P3's initialisation |
| FB (215–234) | ACCEPT, under the item-1 context | 0/0/0 | Every case is covered, including t absent |
| DEEP / K62X / R0 (237–252) | ACCEPT | 0/0/0 | |
| Interface §1 / §10 diagnostics | ACCEPT-WITH-FIXES | 0/0/1 | MINOR-3; the diagnostics are correct after F1 and item 3 |

## Numbered findings

**MINOR-1 — `K62-FULL-v1.md:139-140`, remark after SG.**
- *Claim.* "The product-separation step is needed only when v = t."
- *Gap.* This is true only for the gcd consequence. When t ∈ O and v ≠ t, it is justified only by a chain that places t first.
  - In the written chain, t can be added at any position.
  - Without Lemma 2, an earlier step with k = 3 makes gcd(n_t, T_{r−1}) ≥ 18.
  - The multiplier at the step that adds t is then bounded only by 3^j. That leaves the absence of new primes uncontrolled, which matters at v = p.
  - The displayed form T = L·2^s needs Lemma 2 at every step, in every placement.
- *Impact.* None. The proof applies Lemma 2 at every step, and later sections use only the gcd consequence.
- *Repair.* Say: "for the gcd consequence alone: without t, k ≤ 3 suffices; with t ∈ O and v ≠ t, order t first; Lemma 2 is indispensable at v = t and for the 2^s form."

**MINOR-2 — `K62-FULL-v1.md:193`, proof of P3.**
- *Wording.* "build S from t (if present)."
- *Gap.* If t ∈ O \ S, then t cannot start the chain.
- *Correct reading.* Start from t if t ∈ S, and otherwise from any vertex of S. Under that reading every added vertex e' ≠ t has f_{e'} = 1. Each step then has gcd = 6 (2-part 2, 3-part 3, and ℓ_{e'} prime to 6 and to the earlier ℓ°). Each multiplier is at most x ≤ 4, so the prime-to-6 part stays ∏ℓ°_j. The no-t initialisation is therefore sound.
- *Repair.* Write that reading explicitly.

**MINOR-3 — `K62-FULL-v1.md:67`, "Not used: CAP C1/C2/RC, …".**
- *Gap.* This is accurate only for direct use. M13 verdict `2fac7a30` (line 5) accepts its items relative to a combined import list for parts A–D, which includes CAP C1, RC-i* and the G3 form of DG-3. The excerpts do not show which of these DG*/C2* (items 1–2) rest on.
- *Consequence.* K62X's transitive closure inherits whatever those items rest on.
- *Repair.* Write "not used directly; the accepted closure of M13-A items 1–2 (verdict 2fac7a30, line 5) is inherited."

## Overlays (each checked independently)

1. **Worker F1.** Correct.
   - DEG at t enters through DEG (c), which FB (ii) and TRI use, and through DEG (a) for c4 and c5 in Step 1.
   - The isolated vertex in FB (vii) lies outside Q, and Q contains t.
   - ONE and T16 call EQS/CIS at any apex, including t. Example: in FB (v), the apexes c and q of {a,b,c} and {a,b,q}.
2. **Provenance clarification.** It contains no mathematics. Accepted.
3. **Parent erratum item 1 (normalisation context).** Necessary and sufficient.
   - T16 (200), ONE (204) and FB (215) are stated without an orientation hypothesis. Their proofs go through BUD and then FAM's (C2_{x'}), which needs α_(d i*) = 1.
   - The chain from FAM through BUD, T16, ONE and FB to DEEP is exactly the conditional chain.
   - P1, Lemmas 1/1'/2, SG, R4S, DEG, CIS, EQS, P2–P4 and TRI are orientation-free. I checked that none of them uses FAM or BUD.
   - K62X applies Reduction R first (244).
   - So no stronger standalone implication is left hidden. Unconditional forms would follow by transport through Γ* together with M13-A C2* in (3,1), but that transport is not written and is not needed.
4. **Item 2.** W_r := ∩_{S_r} Π_j is exactly what the proof uses (W_{r−1} ⊆ Π_d ∩ Π_{c1}).
5. **Item 3.** Verified, diagnostic only.
   - If x'_(d i*) = 3, then 9 | T_{x'}({d,i*}), which divides T_{x'}(V∖{t}).
   - If x'_(e i*) = 3 for some e ∈ O∖{t}, then 9 | 3·lcm(n_e, n_{i*}).
   - The pair (t, i*) does not lie in V∖{t}.
   - Then gcd(n_t, ·) ≥ 18 gives the bound 17/18 > 11/12, so the R4S contradiction is lost.

## Re-derivation record (the requested hostile checks)

**OR and Reduction R.**
- E1 with g = 4 gives x_(d i*) ∈ {1,2,3}.
- E3-L1 (Z2) is stated for both families. At d the labels are n_c/2 (odd) and n_{i*}·a/4. All pairwise gcds are 3, except gcd 9 at (t, i*) when a = 3, in which case f* = 1.
- Uniform weight 1/3 then gives 5/6 + a/12 < 1. So a = 2 never occurs, and a = 3 requires t ∈ O.
- INV (b) gives α + α* ≤ 4, which excludes (3,3). Uniqueness of the 3-marker gives f* = 1.
- For R: (Γ*)* = Γ, so the pair of Γ* is (α*_(d i*), 3) = (1,3). The labelled tuple is the same, so the class and markers are the same (E6). The case α* = 1 keeps f* ≥ 2 and every 5-placement.

**FAM.**
- *x = α\*.* E3-C2 and DG (b) with G6 need only α_(d i*) = 1. So they apply in both (1,1) and (1,3). The depths v2 T*_Q are invariant under conjugation and equal δ_{α*}.
- *x = α with α\* = 1.* The accepted statements are applied verbatim to the actual configuration Γ*.
  - Γ* has α_(d i*)(Γ*) = 1.
  - Its conjugated family is g_j⁻¹U*_j g_j = U_j.
  - This yields C2_α and DG_α with depths δ_α. No scope is widened, f* ≥ 2 is allowed, and every 5-placement is allowed.
- *x = α with α\* = 3.* FAM uses M13-A C2*, which has no four-subset hypothesis, and DG* (b) under its own hypothesis. Both lie inside verdict 2fac7a30's setting.
- The DG_x alternative in FAM matches the accepted text: capped depth 5, type (4,4,4), τ = 16.
- DG_x is invoked only in DEEP, after FB has supplied each family's four-subset hypothesis. No M13X theorem is imported.

**P1.**
- E3-L2 is orientation-free (verdict item 2).
- For h_d = 0 and x_vu = 5:
  - λ_u = 5ℓ_u is odd and λ_d = 2^{e_d−1}w_d.
  - These are coprime, also when u = t or u = p.
  - So {u, d} is not allowed, and the bound gives 5/6 + 1/2 > 1, a contradiction.
- INV (b) in the x-configuration gives x + x' ≤ 6.

**Lemmas 1, 1', 2.**
- Lemma 1 (a): [W_Q : W_Q∩Ψ] ≥ lcm/[G:W_Q] = n_v/gcd. Avoidance follows from h_j⁻¹h_v u ∈ Φ_j.
- Lemma 1 (b): because y vanishes off Q, the light fibres contribute nothing.
- Lemma 1 (c): W_Q = ∩Φ^{x'}_j, which is the opposite family.
- Lemma 1': Φ_vW ⊆ X_j, which is disjoint from D_j. Its measure is [G : Φ_v∩W]/(n_v·T_x) ≥ 1/gcd, using the own family x.
- Lemma 2: p⁻¹q = ab gives pa = qb⁻¹, which lies in both pieces, a contradiction.

**SG.**
- *gcd at each step, for e = c_r.* The gcd is 6 in every case.
  - 2-part: 2.
  - 3-part: v3 L_{r−1} = max f over earlier vertices ≥ 1, and it equals 1 when e = t, so t can be at any position.
  - 5-part: there is at most one 5-vertex in {d} ∪ O, including d; there is none if the 5-marker is on i* or absent.
  - w-part: 1.
- *Multiplier bound.* k ≤ 6·μ(Π_eΠ_d) = 3.
- *k = 3 is impossible.*
  - Π_eW_{r−1} = Π_eΠ_d (containment, both of measure 1/2), so Π_d = (Π_d∩Π_e)(Π_d∩Π_{c1}), in Lemma 2's order.
  - At d, the support of the e-piece and the support of the c1-piece are n_d/2 fibres each, and both miss d's own coset h^z_dΠ_d.
  - So #(fibres meeting both) = #(fibres meeting neither) ≥ 1, which contradicts Lemma 2.
- *lcm step.* The 2-adic lcm step is correct.
- *Final gcd.* At v = t every vertex of R has f = 1; at v ≠ t, f_v = 1.
- *Independence from i\*.* i* never enters the chain. So f*, h*, e* and the i* entries are all free, and no f* = 1 is assumed silently.

**R4S and DEG.**
- The odd parts of {ℓ_u}_{u≠v} and of 5^{h_d}w_d are pairwise coprime under every placement: t, p, t = p, 5-marker on d, 5-marker on i*, or no 5-marker. The vertex v itself carries no label.
- Feasibility:
  - an entry-1 label is coprime to every other positive label, so an allowed set containing it is a singleton (Sun(2));
  - the entry-2 labels and d have pairwise gcd exactly 2, so an allowed set among them has at most 2 elements (Sun(3));
  - y_(i*) = 0.
- The value is 11/12, which exceeds the bound 5/6 from Lemma 1 (b)–(c) with SG for z = x'.
- DEG then follows from R4S.

**CIS and EQS.**
- Saturation: the union of the D_j over V∖{v, i*} has measure ≤ 5/6, by Lemma 1' with SG for z = x.
- D = G∖X_a = G∖X_b.
- Step 2 is a Sun(3) instance. Step 3 saturation gives D_c ⊆ D_d.
- Step 4 is a Sun(2) instance, together with μ(D_c) ≤ 1/2, giving x'_vc = 2.
- Step 5 is a Sun(3) instance and gives 4/6 ≤ 1/2, which is false.
- D_{i*} never enters. The argument is valid with v, a, b, c ∈ {t, p}.
- The one-tight case of EQS is a Sun(2) instance.

**P2–P4, BUD, T16, ONE and TRI.**
- P4: the measure is τ/(6x_ac), and the equality case is containment in X∩X of measure 4/6.
- P2: x_ab | ℓ_c·τ gives x_ab | τ, and τ ≤ x1·x2.
- BUD: n_4(x) ≤ 10 − n_4(x') ≤ 8 − 2u(x).
- T16: EQS at all three apexes gives u ≥ 3, hence n_4 ≤ 2 < 3, a contradiction. Then τ ≤ 15, and v2 τ = 3 exactly when τ = 8.
- ONE: two distinct triples have distinct pairs of apex edges, which gives at least 3 non-tight pairs, a contradiction.
- TRI: the case analysis is correct.

**FB.**
- Relation (N) is used only at e ≠ t.
- Steps (i)–(iv) are correct, including the endpoint-count argument.
- Case (a) is "t ∉ I", which covers both t absent and t ∈ Q∖I.
- Case (c) lists exactly the four admissible sets N.
- (v) and (vi): k = 2 = x = m, so P3's equality case applies, and P4 gives τ ≥ 8. Together with P2's cap of 8, this yields two (2,4,4) triples with τ = 8, contradicting ONE.
- (vii): either ONE is contradicted directly, or n_4 ≤ 4 and the fifth vertex is isolated. That vertex is not t, so DEG (a) gives the contradiction.

**DEEP, K62X and R0.**
- DEEP: the τ = 16 alternative is excluded by T16.
- Step 1 is correct in each case: zero triangles, one triangle, and two triangles.
- Step 2: the complement {ab, ae, be, ce, qe} contains only the triangle {a, b, e}, which contradicts Step 1 for α*.
- R0: N = ∩core(U_i) lies in every U_i and in every U*_i, so it preserves both families, disjointness and the index tuple. No normality is assumed for the U_i.
- No marker case and no exponent case is omitted.

**Diagnostics.** No granularity stronger than what SG proves is claimed. Lines 265–268 describe ledger coverage, with the mechanism attributed to the pending M13X. That is consistent with lines 281–282 and makes no unsupported claim of method novelty.

## Import-scope assessment

- **General lemmas** (E1/L0.3, L0.1, L0.2, Lagrange, LFC (a)–(d) with k ≤ 7, INV (a)–(b) with E6/E7, VFC (V1)–(V4)) are applied only to actual disjoint coset families, Γ and Γ*. In scope.
- **E3 statements.** E3-T, E3-L1 and E3-L2 hold for the whole class, in both families. E3-C2 and DG are used only where their distinguished entry is 1. DG's four-subset hypothesis is discharged per family by FB, and the e_d ≥ 5 alternative is closed rather than assumed away.
- **M13-A.** C2* and DG* are used only for α in (1,3).
- **Sun results.** Sun(2) and Sun(3) are used directly, through instances with |T| ≤ 3. Sun(4) enters through E3, DG and M13-A. Sun(5) and Sun(6) are computer-assisted and enter transitively only. Sun(7) is not used.
- **GS and pending texts.** No proof line cites GS; it serves as a cross-check, and K62X restricted to G agrees with GE. No pending text is cited as a premise; every borrowed lemma has a proof inside the file.

## Trust-boundary assessment

- **Hashes.** Hashes and line ranges are unverified. I treated the excerpts as the content of the cited files.
- **Imports trusted, not re-proved.** E3 steps 1–4 and Lemma 3, DG-1 to DG-3, and M13-A A1 and DG-2* rest on their parent verdicts. Spot checks of E3-L1 (Z2) and E3-L2 agreed.
- **M13-A erratum not visible.** Verdict 2fac7a30 is to be read "with the parent erratum below", 99276f6d, whose text is not in the package. The α-branch of FAM in (1,3) assumes items 1–2 survive that erratum as excerpted. This is the one import whose final text I could not see in full. See also MINOR-3.
- **Overlays.** The overlays are confirmed correct, and none of them alters a proof step.
