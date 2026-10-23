# RW candidate v1 (a6272c5b…): independent hostile written review

This was a no-tool review. I used only the pasted selections. Nothing was read, computed or enumerated. Every load-bearing step below was re-derived by hand from the literal accepted interfaces.

**Abbreviations:**
- RW: the candidate
- SC: the frozen scope file
- WV: the written parent verdict
- R7: `rules-k7-v1`
- AD: the addendum
- ER: `rules-k7-erratum-v1`
- S56: `S56W-v1`; S56V is its verdict; e1 and e2 are its parent errata
- FX: `FINAL-EXPOSURE`
- FBC: `FINAL-BC-repair`
- FCS: `FCS-SITES`
- CUT: `CUT-v3` §7

## Counts and bottom line

**FATAL 0 · MAJOR 0 · MINOR 8.**
- There are no correctness findings: no counterexample, no false step, no circularity and no hidden import.
- Seven MINORs are precision or completeness issues; one is a process issue.

**RW is valid at its exact restricted boundary.** Each bundle is supplied by WV LF23 plus LF34/38/40/42, the overlays at LF48–50, ER W2, and the S56 written L0.x/L3/K2.
- The bundles are T, K/K1/K2, P, VFC with the weighted count, RPLP with F7, and CAP for active quantities.
- S5W/S6W are used statement-only inside U_v, with the correct coset side and ambient indices.

**The order 01–17, 24, RW, 18–23, 25–79 is acyclic** under CUT LF193–274 plus FBC B1-OM (LF29–46). This is conditional on CUT-v3-erratum-v1, which was not supplied (m7).

**RW does not close any of these:**
- the IL5/IL6/IL10 obligations beyond RW-descendants (m5)
- CAP-ENV and IL9 (m6)
- IL7, IL12, the TS3 frame clause, IN1, IN10, KS5 and PROV
- the body census, the final graph and the final composition

Full Sun7 remains UNACCEPTED. No class-exclusion, certificate or runtime authority follows.

## Claim-wise verdicts

| # | RW claim | Checked against | Verdict |
|---|---|---|---|
| C1 | Setting, R0, P0/P1 bounds (LF6) | WV LF18, 42; S56 LF143–147; AD LF144–146 | ACCEPT |
| C2 | Authority map (LF8) | WV LF23, 34, 38, 40, 42, 48–50; ER LF5 | ACCEPT |
| C3 | T (LF13) | R7 LF19–24; WV LF23, 38; S56 L0.1 | ACCEPT |
| C4 | K/K1/K2 (LF14) | R7 LF26–28; WV LF38, 48; S56 LF54–61 + e1 item 1 | ACCEPT; m4, m8 |
| C5 | P (LF15) | R7 LF30; WV LF38; AD LF45–54; S56 L0.4/L0.5 | ACCEPT |
| C6 | VFC and count (LF16) | R7 LF40–49; WV LF34, 48 | ACCEPT |
| C7 | RPLP with F7; Farkas on the closed relaxation only (LF17) | AD LF21–110, 116–124; ER LF21–31; WV LF40, 50 | ACCEPT as rule soundness only; m1 |
| C8 | CAP, restricted (LF18) | R7 LF70–75; AD LF126–148, 155; WV LF23, 42 | ACCEPT for active quantities; m1 |
| C9 | Universality kept; no certificate or coverage (LF20) | WV LF23, 40, 56; AD LF110 | ACCEPT |
| C10 | Fibre substitution (LF22–23) | WV LF34; S56 LF17–25, 169–186; e1 item 2; e2 m1/m4/m6; S56V LF5–14 | ACCEPT; m2, m3 |
| C11 | RPLP caller is the same site; LF17–19/71 historical (LF25) | AD LF17–19, 41, 71, 120 | ACCEPT |
| C12 | τ by direct τ ≥ τ_min; no L8 M1 (LF27–28) | AD LF53, 62–66, 124; R7 LF80; FX LF51–55, 61–62 | ACCEPT; m8 |
| C13 | Exclusions (LF30) | WV LF26, 49, 60; AD LF122, 161–169; ER W1; e2 m6 | ACCEPT |
| C14 | Inputs and order (LF33) | CUT LF196–274; FBC LF29–46, 68–69 | ACCEPT under supplied edges; m2, m4, m7 |
| C15 | Census consequences (LF35) | FBC LF59–63, 80–96; FCS LF74–79 | ACCEPT only as scoped by m5 and m6 |
| C16 | Status and non-claims (LF37–38) | — | ACCEPT |

## Re-derivation of load-bearing steps

All of these are in finite G after R0, with pairwise disjoint left cosets.

**T.**
- U_a∩U_b∩U_c ≤ U_i, so n_i | T and I_xy | T.
- L = lcm(n_x,n_y)·ℓ_z, so I_xy | T ⇔ α_xy | ℓ_zτ ⇔ α_xy/gcd(α_xy,ℓ_z) | τ. Hence τ ∈ τ_min·ℤ>0.
- L0.1 gives μ(U_y(U_x∩U_z)) = T/(n_y·I_xz) = τ/(γ_y·α_xz), using L/lcm(n_x,n_z) = n_y/γ_y.
- Inclusion in U_yU_x ∩ U_yU_z gives τ ≤ τ_max.

**K.**
- Suppose g_iu_iu = g_ju_ju′.
- Then g_j⁻¹g_i ∈ U_jU_vU_i, which lies in U_jU_i under the first disjunct. Under the second disjunct, g_i⁻¹g_j ∈ U_iU_vU_j ⊆ U_iU_j. Either way this contradicts L0.2.
- Each g_iU_iU_v is right U_v-invariant. If it met U_v (with g_v = 1), it would contain 1. That forces U_v ∩ g_iU_i ≠ ∅, which is false.
- With L0.3, Σ α_iv/g_iv ≤ 1 − μ(U_v).

**K2.**
- Invert U_vU_j ⊆ U_vU_k to get U_jU_v ⊆ U_kU_v.
- This is the pair condition of K at vertex j for S = {v,k}.

**K1.**
- Use (T3) at apex i together with τ ≥ τ_min.
- Under the forcing hypothesis this gives a value ≥ μ(U_iU_v), and (T2) gives ≤ it, so equality holds.
- Then U_iU_v ⊆ U_iU_j. Inverting gives U_vU_i ⊆ U_jU_i.

**P.**
- X_j∩X_k is a union of (U_v, U_j∩U_k)-double cosets (L0.5).
- Each has measure in (1/gcd(n_v, I_jk))·ℤ (L0.4).
- For finite sets, equality with min(μX_j, μX_k) holds iff the needed containment(s) hold. If K2 bars them, the bound is strict, so it is at most hi − u when hi equals the minimum.
- Bonferroni uses U_v ⊆ ∩X_j, with upper bounds on the subtracted terms.

**Fibres (the substitution site).**
1. For y ∈ D_j there is w_j ∈ U_vy ∩ g_jU_j.
2. Then R ∩ g_jU_j = U_vw_j ∩ w_jU_j = K_jw_j, where K_j = U_v ∩ w_jU_jw_j⁻¹.
3. Since w_jU_j = g_jU_j, L0.1 gives [U_v:K_j] = |U_vw_jU_j|/|U_j| = |D_j|/|U_j| = q_jn_j/g_vj = d_j.
4. The pieces lie in the disjoint cosets g_jU_j, so they are disjoint.
5. Right-translating by y⁻¹ gives K_jc_j with c_j ∈ U_v. Inverting gives c_j⁻¹K_j.
6. The result is |T| pairwise disjoint LEFT cosets in the ambient group U_v, with the same subgroups and indices d_j. Here T ⊆ S_R ⊆ N, so |T| ≤ 6.
7. The imports are L0.6 at t = 2 (U_v is finite), Zhu at t = 3, 4 (external), and S5W/S6W at t = 5, 6. Coinciding K_j are allowed. This is a statement-only use (e2 m4, m6).

**Count.**
- Σ_j y_j|D_j| = Σ_R |R|·Σ_{j∈S_R} y_j ≤ |∪D_j| ≤ |G| − |U_v|.

**RPLP.**
- F7: (T3) and (T2) at apex v with τ ≥ τ_min force X_a = U_v(U_a∩U_b) ⊆ X_b.
- Weak duality: Σx ≥ Σx·LHS(★) = Σa·E1 + Σb·E2 + Σ(l−u)·μ(Y_j∩Y_k) ≥ Obj ≥ 1, which contradicts TOT < 1.
- Farkas applies only to the closed system P(q) (ER W2): LHS ≤ 0 on every column, Obj > 0, then rescale.

**CAP.**
- gcd ∈ {2,…,6} gives H1–H3.
- Bullet 4 key step: if j carries e_j ≥ 4, the capped term is ≥ 4 − e_v. That is ≥ v₂(q_j′) + max(0, e_j′ − e_v), because v₂(q) ≤ 2 and e_j′, e_v ≤ 2.
- Bullets 1–3 and the A2 table check the same way.

**τ.**
- Every τ-dependence of RPLP is through τ ≥ τ_min, in AD F6 step 2 and F7 step 3.
- AD LF124's first two sentences therefore suffice. L8 M1 is not needed.

## Findings

**m1. Citation ranges are wider than the accepted contract (precision).**
- **Where:** RW LF17, LF18, LF25.
- **Step:**
  - R7 LF70 and LF76 cover L5 λ-gcds. WV accepts CAP only for "all active quantities" (LF23), and LF42 derives only g/γ, ℓ, gcd(n_v, I_jk) and local-index gcds. WV LF49 keeps L5 outside the active rules. RW's limiter ("gcd-capping … quantities proved in these paragraphs") still literally covers LF76.
  - AD LF157 contains CERT-FORMAT role-domain claims and audit/engine counts, which are computational content.
  - AD LF152–154 are five-vertex universes, outside RW LF6's seven-coset setting.
  - "Pattern" (AD LF139) is defined only at R7 LF80, which RW does not cite.
  - The range LF21–124 includes LF112 (certificate checking) and LF124's "upward closed" pointer. LF25's "LF21–104" omits LF106–110 and LF124.
- **Consequence:** No RW conclusion uses this text, so correctness is unaffected. A consumer could still cite RW as WV-accepted CAP for L5/FH or for A3's role domains and counts.
- **Repair:**
  - Cite R7 LF70 restricted to the L0.3/L1/K1/K2/L4/VFC quantities, plus LF71–75, and drop LF76.
  - Cite R7 LF80's first sentence only.
  - Cite AD LF128–139, LF143–148 and LF155, and exclude LF157 and LF159.
  - Restrict RPLP to LF21–110 (with W2 at LF106) plus LF124's first two sentences, and make LF25 match.

**m2. "The same applies to the actual inverted configuration" is undefined.**
- **Where:** RW LF23.
- **Step:** Neither RW nor WV defines this configuration. WV LF38's inversion is (XY)⁻¹ = YX, which is part of node 01. If the sentence means node 06 (INV, CUT LF201):
  - 06 is missing from RW's inputs (LF33)
  - its left-coset and ambient-index site check is not displayed (e2 m4, m6)
- **Consequence:** The displayed VFC/RPLP site is unaffected. Acyclicity is unaffected, because 06 precedes RW and is not an ancestor of it.
- **Repair:** Delete the sentence, or define the configuration, show its site check and add 06 to the inputs.

**m3. Both authorities are not recorded at the substituted site (process).**
- **Where:** S56 LF179–181 (protocol item 3, unmodified by e1 or e2); RW LF23 and LF38; AD LF120.
- **Step:** RW names only S5W/S6W at the t = 5, 6 site. The historical verdicts 2cf02436… and efe1d849… are not recorded there.
- **Consequence:** Provenance only.
- **Repair:** Add one line naming both: the written authority (S56V 63baa72b…) and the historical computer-assisted authorities, unchanged and distinct.

**m4. The S56 L3/K2 route has no input node.**
- **Where:** RW LF14 and LF33; CUT LF196 (node 01 covers only S56 LF34–48); FCS LF17–18.
- **Step:** S56 LF49–61 is accepted but is not a CUT node.
- **Consequence:** Bookkeeping only. The WV LF38 route needs only nodes 01 and 04, and K2 follows from K by one inversion.
- **Repair:** Fix the route to WV LF38 plus "K2 = K at vertex j, S = {v,k}", or extend node 01 to cover S56 LF34–61.

**m5. Scope of withdrawing the IL5/IL6/IL10 obligations (completeness).**
- **Where:** RW LF33 ("Optionally …") and LF35; FBC LF86.
- **Step:**
  - A positive envelope replaces a negative non-use claim only for RW-descendants.
  - With the edges left optional, no consumer actually acquires RW.
  - RW's ancestors are {01–05, 07, 09–15, 17, 24}, and these can never take RW: for example 09→14→17→RW→09 would be a cycle. Any such step there must come from their own texts: Prop 4.5 uses S56's own L3/K2 (FCS LF74), and C5W/C56W use their own fibre counts (S56 LF155–156).
  - Nodes 06, 08 and 16 precede RW in the proposed order.
- **Consequence:** A global withdrawal would overstate. A residual pre-RW obligation remains. It is low-risk but must be recorded.
- **Repair:**
  - Make RW→v required for every v in 18–23 and 25–79 whose body census is not closed (conservatively all), and for 79.
  - Forbid RW citations from its ancestors.
  - Note that 06, 08 and 16 are covered only if RW is moved before them.

**m6. IL9 / CAP-ENV is not closed by RW (completeness).**
- **Where:** RW LF35; FBC LF59–63 and LF85; FX LF46–48, LF51–55, LF61–66; SC LF11.
- **Step:**
  - CAP-62 uses "its capping argument" via min(·, 2), "as in" Lemma CAP. RW admits only the quantities at R7 LF71–75 and A2, and does not show CAP-62's quantities are among them. They may instead rest on CAPV.
  - Non-use of LF80 / L8 M1 through n75–n79 is established only at search level (SC LF11).
  - n75's declared imports require edges 03, 07, 17, 24 and RW into 75.
- **Consequence:** B2(4) and IL9 stay CONDITIONAL even if RW passes.
- **Repair:** List items (a)–(c) above as open in LF35.

**m7. Acyclicity relies on edges that were not supplied (completeness).**
- **Where:** RW LF33 ("all existing correction edges"); FBC LF68–69.
- **Step:** The reorder is valid iff no edge runs from 18–23 into 24 and all of RW's ancestors lie in the prefix.
  - Both hold for the supplied edges: In(24) = {01} (CUT LF219), and B1-OM touches only nodes 42–78.
  - CUT-v3-erratum-v1 was not supplied.
- **Consequence:** The acyclicity claim holds only under the supplied edges.
- **Repair:** Cite the erratum's changes, if any, to In(01–17) and In(24).

**m8. K1's T-dependency is omitted, and the τ_min forms are not stated (wording).**
- **Where:** RW LF14 and LF28; R7 LF27; WV LF49.
- **Step:**
  - K1 uses (T2)/(T3) and τ ≥ τ_min. This is internal to RW and has no DAG effect.
  - RW keeps T/K/P only at actual parameters. That is narrower than WV LF49, which treats them as pattern predicates.
  - Yet the T-kill (τ_min > τ_max), the K1 τ_min test and the P/F6 τ_min lower bound all hold for every admissible τ by RW's own direct argument, without L8 M1.
- **Consequence:** None for correctness. A consumer may wrongly think these forms need L8 M1.
- **Repair:** Add one clause to LF14 and one sentence to LF28.

## Acyclicity under supplied edges

- In the original order, every input id is smaller than its node id (CUT LF193; FBC LF42).
- Only node 24 moves earlier. Its inputs are {01}. The inputs of nodes 18–23 are {04, 06, 16, 18, 20, 22}, which excludes 24.
- RW's ancestors are {01, 02, 03, 04, 05, 07, 09, 10, 11, 12, 13, 14, 15, 17, 24}, all inside the prefix. No node numbered 18 or higher is an ancestor of RW.
- Therefore the order is topological, and any optional edge RW→v with v in 18–23 or 25–79 preserves acyclicity.

## Remains OPEN

- The body census for proof-level use of anything RW excludes: L5/FH seven-piece, the frame, C18, L8 M1, StageA/B and solver outputs.
- IL7, IL12 and TS3.
- CAP-ENV (m6).
- IN1, IN10, KS5 and PROV.
- N2c and N2d, and the B2 CONDITIONAL items (1)–(3).
- The final graph and composition (node 79).
- WV F-1, unchanged.

## Classification and non-claims

**Errata applied:** ER W1/W2; WV overlay items 1, 3, 4 and 5 (items 6–9 are unused); AD A5 E2/E6; S56 e1 items 1–2 and e2 m1/m4/m5/m6/m8; FBC B1-OM.

**Classification:**

| Type | Findings |
|---|---|
| Correctness | none |
| Completeness / precision | m1, m2, m4–m8 |
| Process | m3 |
| Priority | no claim made or inferred |
| Computation | none introduced; AD LF157 and StageA/B are excluded (m1) |

No novelty, first, Lean or human-referee claim is made. This is not an approval of full Sun7, of any class exclusion, of any certificate, or of runtime.
