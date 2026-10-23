**FATAL 0 / MAJOR 0 / MINOR 6.** CI62 has four MINOR findings (m1–m4) and the ledger repair has two (m5–m6). Governing erratum v3 is applied throughout:
- the capping edge is **N16→N57** (provider→consumer);
- the conservative edge is **N57→N58**;
- no N57→N16 edge is read anywhere below.

Source keys used below:

| Key | Text |
|---|---|
| CI | CI62 lemma |
| LE2, LE3 | ledger parent errata v2, v3 |
| L, LX | LEDGER-v1 and its erratum v1 |
| RW, RWE, RWV | RW candidate, its parent erratum, its parent verdict |
| CAP | K62-CAP-v1 |
| CD | CAP-DT erratum v1 |
| V | CAP-DT erratum v2 |
| RK7, ADD | rules-k7-v1, rules-k7 addendum |
| LFC, LFE | K7-LFC-INV-v1 and its erratum |
| E3, Z | K62-E3-v1 and its erratum v2 |
| SD, SDV | SH-DG erratum, SH-DG parent verdict |
| M13, M13V | K62-M13-A-v1, M13 parent verdict |
| FP2, FULL | FULL parent erratum v2, K62-FULL-v1 |
| CAPV, P2 | CAP-DT parent verdict, P2 review |

## 1. Independent re-derivation

**Setting** (CAP LF21–26; E3 LF16–19):
- Pairwise gcds are 6 inside C, 4 on d–i*, and 2 on d–O.
- e_d ≥ 4, e* = 2, e_c = 1 and f_d = 0.
- Every C-vertex other than the 3-marker has f = 1; every vertex other than the 5-marker has h = 0.

1. **From π to ρ (CI LF13).** Each profile is read from pi1 plus fixed class values, so the claim holds:
   - ρ_d = (4, 0, ·), with the 5-coordinate recorded if m5 = d and 0 otherwise.
   - ρ_i* = (2, 2 or 1, ·), with f-coordinate 2 if m3 = i* and 1 otherwise.
   - ρ_c = (1, 2 or 1, ·), with f-coordinate 2 if c = t and 1 otherwise.

2. **RW hypotheses (CI LF15).** The claim holds:
   - g ∈ {2,4,6} gives (H1).
   - (H2) is part of the class definition.
   - (H3) holds because α ≤ g−1 (LFE E1) and α* ≤ g−α (LFC LF64).
   - The 7-vertex K62 universe is ADD LF155, which lies inside RWE LF5's admitted lines. The five-vertex universes at ADD LF152–154 are unused.

3. **B1 (CI LF17).** The claim holds, and it is exactly RK7 LF72–73 with LF70 read for L1 quantities only (RWE LF5). τ_min and τ_max then follow from RK7 LF24.
   - g and γ are class constants: γ_d ∈ {2,4}, γ_i* ∈ {6,12}, γ_c = 6.
   - The ℓ valuations are:

     | z | v2(ℓ_z) | v3(ℓ_z) | v5(ℓ_z) |
     |---|---|---|---|
     | d | e_d − v2(γ_d) ≥ 2 | 0 | h_d |
     | i* | 0 or 1 | f* − 1 | h* |
     | c ∈ O | 0 | f_c − 1 | h_c |

   - Any entry ≤5 has v_p at most (2,1,1) at p = (2,3,5).
   - So gcd(x_xy, ℓ_z) reads only min(v_p(ℓ_z), c_p), and the caps (4,2,2) preserve that quantity.

4. **B2 (CI LF19).** The claim holds.
   - Let Γ_x′ be the configuration whose α-matrix is x′. It is either Γ or its inverse.
   - By INV(a) with E6 the inverse has the same labelled indices, so it is in RW's input class.
   - The VFC q of Γ_x′ at v toward j is the α-matrix of its own inverse. This uses INV(b) and LFE E7, plus double inversion (LFC LF58) when x′ = α*.
   - So q equals x_vj, which lies in [1, g − x′_vj].
   - Its local index d_j = q_j·n_j/g_vj equals λ^x_j as an integer.
   - Hence the label gcds are exactly the RK7 LF75 VFC gcds with q ≤ 5.
   - I rechecked LF75 at all three apex types:
     - at d, no label involves e_d;
     - at i*, v2(λ_d) = e_d−2 ≥ 2, against at most 2 for the other labels (x_i*d is odd);
     - at an O-vertex, v2(λ_d) = e_d−1 ≥ 3, against at most 3 for the other labels;
     - the 3- and 5-parts work with cap 2.
   - RK7 LF76 is neither used nor needed.

5. **Exceptional gcd 9 (CI LF23; CD LF80–88).** The claim holds.
   - If x_di* = 3, then t ∈ O and f* = 1 (E3 LF26).
   - Then v3(λ_i*) = 2 and v3(λ_t) = f_t ≥ 2, so the gcd reads min(f_t,2) = 2.
   - In LF75's terms this is the case v3(q) = 1, where the second term meets the cap exactly and LF75's inequality holds with equality.
   - So the cap-2 argument is valid exactly where CAP's original "≤3" claim failed.

6. **B3/A3 (CI LF29).** The claim holds.
   - τ is stored in pi3.
   - (T1)–(T3) (RK7 LF20–24) apply to Γ and to its inverse.
   - The apex measure is τ/(γ_b·x_ac) and the pair measure is x_ab/g_ab.
   - Neither τ = τ_min nor τ-monotonicity is used.

7. **A4/B4 (CI LF30–31).** The claim holds, independently of RW's cap 4 and of Z11(a).
   - In either family, [G : Φ^x_j ∩ Φ^x_k] = lcm(n_j, n_k)·x_jk and μ(Φ^x_jΦ^x_k) = x_jk/g_jk.
   - E3 Lemma 2 holds in both orientations.
   - So the marked-first chain (Z LF155–170, extended to every nonempty Q by Z LF255–260 and SD LF159–160) behaves as follows:
     - it starts with v2 = 1, or ≤3 for a marked pair;
     - each unmarked step multiplies by an integer k ≤ 5 with v2(k) ≤ 2 and no prime above 5.
   - Hence v2 T_x(Q) ≤ 2|Q|−1 ≤ 9.
   - Also gcd(n_d, T_x(Q)) = 2^min(e_d, v2 T). When h_d ≥ 1 this is 5-free by Lemma 2.
   - The raw depths are 1, 1+v2(x_ab), 1+v2(τ_x(R)) and δ_x(Q) for |Q| = 1, 2, 3, ≥4.
   - min(e_d, v) = min(ê_d, v) for every v ≤ 9.

8. **B5 (CI LF32).** The claim holds: only the LFC(a) ratio t_j/n_v = x_vj/g_vj is determined (CD LF246–247).

9. **C1/C2/RC/D and CD4–CD7 (now live under RES-1).** No defect found.
   - **C1** (CAP LF73–76): T_2 = lcm(n_d, n_i*), and every later multiplier is k ≤ 3.
   - **C2** (CD LF104–114): the first O-step has k = x_ud = 1 exactly, later steps have k ≤ 3, and the gcd is 12.
   - **RC** (CD LF140–154): W′U_v misses every L_j, and M ≥ n_v/gcd(n_v, T). RC-O and RC-i* are its specialisations.
   - **D** (CD LF175–198 with V5, V6, V8): a valid conditional transfer with no cover supplied.
   - **Arithmetic checks:**
     - W1/V3 counterexamples: at n_d = 16, 17/16 versus 18/16; at n_d = 32, 36/32 versus 37/32.
     - The N(O) equivalence holds by integrality, since 8 | n_d.
     - The D4 lattice is valid: capped triple depth is ≤5 because τ ≤ x1·x2 ≤ 16 (SD LF211–220).
     - CD6: h_m5 is read only through min(·,1).

10. **Dependencies (LE2 LF6).** CI's providers are N02, N09, N11, N12, N13, N15, N16 and N53. All are already inputs of N57 (L LF274), so there is no new edge and no cycle.

## 2. Claim-wise verdicts

| Claim | Source | Verdict |
|---|---|---|
| π determines ρ and both families | CI LF6–8, LF13 | correct |
| K6.2* satisfies RW (H1)–(H3) in the 7-vertex universe | CI LF15; ADD LF143–148, LF155 | correct; m1 |
| B1 lies within RK7 LF72–73 | CI LF17 | correct |
| B2 lies within RK7 LF75 via INV; LF76 unused | CI LF19–21 | correct; m1, m2 |
| Exceptional gcd 9 | CI LF23; CD LF80–88 | correct |
| A3/B3 from stored τ plus L1 | CI LF29 | correct; m1 |
| A4/B4: cap 10, independent of cap 4, all Q, both families | CI LF30–31 | correct |
| B5 normalized only | CI LF32 | correct |
| C1/C2/RC/D kept separate; conditional, no cover | CI LF37–39 | correct by reference; m3 |
| Whole capping step is B1/B2; exclusions listed | CI LF42 | correct; m4 |
| Erratum v3 arrow fix | LE3 LF5 | correct, notation only |
| LE2 item 1 (M1) | LE2 LF5 | correct; m6(ii) |
| LE2 item 2 (M2) | LE2 LF6 with LE3 | correct in substance; m6(i),(iii) |
| LE2 item 3 (m1) | LE2 LF7 | partial; m5 |
| LE2 item 4 (residuals) | LE2 LF8 | correct |

## 3. Findings (all MINOR)

**m1 — The inverted-configuration hand-off is left implicit (completeness; CI LF10, LF15, LF17, LF19, LF29).**
- **Missing premise.** RWE LF6 removed RW's own sentence about the inverted configuration. It requires an inverted consumer to establish RW's hypotheses through its own literal INV interface. CI cites "INV" generically and never states:
  - that the inverse is a seven-disjoint-left-coset configuration with the same labelled indices (LFC LF56–58; LFE LF49–51);
  - that, for x = α, the q of the α*-configuration is α (INV(b) on the inverse plus double inversion);
  - that the α*-family's τ_min, τ_max and apex identity come from L1 applied to the inverse (V LF223–225 does this for DT-A);
  - that "E1" for α* entries means E1 on the inverse, or α* ≤ g−α.
- **Consequence.** None for correctness: B1 is integer arithmetic valid for any entry ≤5, and (T1)–(T3) are subgroup identities. Only the literal hand-off required by RWE m2 is missing.
- **Minimal repair.** Add one sentence citing INV(a) with E6, double inversion, and INV(b)/E7 for both directions and for L1.

**m2 — The L5 contrast is drawn on the wrong thing (justification wording only; CI LF21, repeated in LE2 LF6).**
- **Step.** CI says LFC labels differ from L5 "trace indices n_l t_l/m". But LFC Remark (1) (LFC LF47) says LFC *is* L5 with H = U_v, so the labels are the same numbers.
- **Correct contrast.** The difference is the argument. The gcd comes from LF75's VFC arithmetic with multiplier x_vj ≤ 5, which INV makes a literal VFC instance. It does not come from LF76, nor under LF76's proviso t ≤ m ≤ 6 (RK7 LF70).
- **Consequence.** None; "LF76 unused" is true.
- **Minimal repair.** State the contrast in terms of the argument, not the object.

**m3 — RC scope and the role of erratum v2 are understated (completeness; CI LF37, LF39).**
- **(i)** RC-O's hypotheses are not written out: v ∈ O unmarked, the **opposite** entry x′_di* = 1, and the x-row bound obtained from C1 for x′ (CD LF138; CAPV LF25).
- **(ii)** CI LF39 describes erratum v2 as "notation and normalized-count/marker precision". In fact it changes the rule discipline:
  - V4/V5 (V LF117–120, LF133) restrict rule use of RC to RC-O and RC-i*, because the general RC slack is not a pattern quantity;
  - V6 (V LF146) adds intersection indices T to the non-pattern slacks.
- **(iii)** "Strict necessary weakenings are lossy" repeats CD4 wording that V8 (V LF175–176) superseded. It is false for the N(O) replacement, which is equivalent by integrality and was withdrawn only as unneeded (V LF91–95).
- **Consequence.** None for the inclusion itself. A consumer reading only CI could import general RC as a rule, or treat every strict replacement as strictly weaker.
- **Minimal repair.** State the RC-O and RC-i* hypotheses and cite V4–V6 and V8.

**m4 — The non-use claim is scoped to the lemma, not to CAP (completeness; CI LF42).**
- **Missing statement.** RWE LF10 says RW alone does not show that CAP-62 has no LF80/M1 dependency. P2 LF53 asks this to be established from the operative CAP text. CI's non-use sentence covers only "this inclusion lemma".
- **The CAP-level fact is true:**
  - CAP imports only "section 4 Lemma CAP (its capping argument)" (CAP LF13), i.e. RK7 LF70–76, not LF80;
  - π stores actual τ and actual depths;
  - CD4's transfer evaluates proved rules at π(Γ) of the actual configuration (CD LF194–198), so neither τ-monotonicity nor LF80's "every instance" clause is used.
- **Consequence.** The second clause of RWE m6 is discharged only implicitly.
- **Minimal repair.** Add that CAP-level sentence.

**m5 — Residue of P2 m1: the Theorem DG proof argument is not exported separately (completeness; LE2 LF7).**
- **Step.** M13 LF14 imports "the proof of Theorem DG with G5/G6" as an argument. M13 re-runs it for DG* in orientation (1,3), where α*_di* = 3 for the α-family (M13V LF9, LF13). There the conditional statement's orientation premise fails (SDV LF19, LF23).
- **What LE2 lists.** LE2 exports "TheoremDG read through G5/G6 with the correct distinguished orientation", which is the statement, not the argument.
- **What is correct.** DG-1 is listed orientation-free (SDV LF17; SD LF194). DG-3/G3 and DG-4 (unmarked added vertex) are also listed correctly and kept distinct.
- **Consequence.** N56/K05's actual import is unlisted. A reader could think M13 applies conditional Theorem DG in (1,3), which would be invalid.
- **Minimal repair.** Under N55/K04, add "Theorem DG proof argument (G5/G6 arithmetic)" as an argument export, like N54's SH-1. It is re-instantiated by M13-A with its own DG-1*/DG-2* and each family's own four-subset hypothesis, and is distinct from the conditional statement used by FULL (FULL LF63).

**m6 — Ledger rows not updated (process and bookkeeping).**
- **(i) R16 range text.** R16 (L LF154) still names "RK7 LF70-76; ADD LF126-159". LE2 replaces only the discharge and adds a reading instruction; P2 LF53 asked for the range text itself to be replaced. N57's exact use is:
  - used: RK7 LF70 (only its L1 γ/gcd(α,ℓ) and VFC gcd(d,d′) clauses), LF71–73, LF75; ADD LF143–148 and LF155;
  - unused by N57: RK7 LF74 and ADD LF128–139;
  - excluded: RK7 LF76, LF80's second sentence; ADD LF152–154, LF157, LF159.
- **(ii) New conservative edge not recorded.** The K06 consumer cell (L LF210) and N58's rows cell (L LF275) do not show the new conservative consumer and edge.
- **(iii) CI62 not listed as governing text.** CI62 is new governing text for N57 that lies outside every census snapshot. Neither the N57 body (L LF103) nor C2's "RES-1 to RES-3" list (L LF283–284) names it.
- **Consequence.** None for the graph, the order or reachability.
- **Minimal repair.** Literal amendments to those rows.

## 4. Status of the original P2 findings

- **P2 M1 — RESOLVED at the graph level.**
  - The edge N57→N58 is forward (57 < 58), and N56 keeps its exact operative inputs (L LF273; LX X2).
  - I re-traced the closure backwards from N59. Before LE2, exactly N16 and N57 were unreached, as L LF285 says. Now N57 is reached via N58 and N16 via N57, so all 59 nodes are reachable.
  - All edges are forward and the graph is acyclic, so the revised C3 statement is accurate.
  - The edge matches FP2 LF7. Through N57 it also brings N09 (L1, which M13V LF5 names in its envelope) into N58's conservative closure.
  - Residual: m6(ii).
  - **Consumer-visible consequence:** the conservative closure of N58 and N59 now contains N16 and CI62. Any statement that the closure is complete is therefore conditional on CI62's gates, even though M13's envelope needs only C1 and RC-i*, which use no capping. Splitting N57 would narrow this; doing so is optional.

- **P2 M2 — RESOLVED IN SUBSTANCE, but conditional.**
  - Every capping assertion CAP uses fits inside RWE-restricted RW: B1 under RK7 LF72–73, and B2 under RK7 LF75 via INV.
  - The only other cap, ê_d = min(e_d, 10), is proved independently from E3/Z10 and CAP A4.
  - No excluded range is needed.
  - It remains a candidate until the parent verdict. Residuals: m1–m4 and m6(i),(iii).

- **P2 m1 — PARTIALLY RESOLVED.**
  - Done: DG-1 (orientation-free), DG-3/G3, DG-4 and conditional Theorem DG are listed separately, and LE2 states that conditional Theorem DG alone does not supply DG-1.
  - Still open: the import of the G5/G6 proof argument (m5).

## 5. Boundary

- **Correctness:** no FATAL or MAJOR defect in CI62, in CD4–CD7, or in the repaired graph.
- **Other findings:** all six are completeness, wording or process issues. There are no computation or priority issues, and no computation was used.
- **Unaffected:** FULL's operative argument and N59's modular implication.
- **Still CANDIDATE_UNVERIFIED pending the parent verdict:** CI62, LE2/LE3, N57's capping interface and RES-1.
- **Not concluded:** no CAP cover, no K6.2*, no full Sun(7) result, no runtime acceptance, and no novelty, Lean or human-referee claim.
