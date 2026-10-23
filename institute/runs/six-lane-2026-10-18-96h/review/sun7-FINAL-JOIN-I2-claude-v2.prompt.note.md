# FINAL-JOIN-IMPLICATION I2 (v2): leaves K6.3, K6.2*, K7

**FATAL 0 · MAJOR 0 · MINOR 2.** Both MINORs concern how the K6.2* input contract is worded or bound to its source (C LF22, LF31). Neither moves a case boundary. I worked only from the pasted text, with no files, tools or computation.

**Keys used in LF references:**
- **C** = composition candidate; **CE1/CE2** = composition errata v1/v2.
- **RM** = README; **LED** = ledger.
- **GOV** = governing addendum, cited by its outer line numbers.
- **v14** = embedded ledger erratum v14, cited by its inner line numbers.
- **RPE** = K63-RES parent erratum v1.
- DEV, RESV, NFV, R2V, A12C, A2XV, FULLV = the accepted verdicts as pasted.

**Governing text applied:**
- GOV LF3–5: this v2 packet governs. Leaf statements are premises; global closure is a separate gate.
- v14 LF5–10 (m1–m6) govern the K62X (1,3) path.
- CE2 LF5–7 supersedes LED LF285–287 (C3). N16→N57→N58 is a retained conservative ancestry, not a dead node.
- CE1 LF5 changes only §6 prose order, so it has no effect on I2.
- A12C (LF3, LF5) is an ancestry clarification for A2X's BRIDGE list. It changes no acceptance scope and is not consumed at C LF32.
- Dated frontier/pending prose is historical; I neither used nor approved it. This covers DEV LF34–40, the last sentence of RESV LF5, R2V LF48–50, NFV LF12 "(a2) remains…" and A2XV LF39.

## Claim-wise verdicts

### V1. K6.3 (C LF18, LF30): CORRECT, exhaustive, scope-matched

- **Setting.** RM LF93 gives D={d}⊆A_3∖A_2, so 3|n_d and 2∤n_d. Hence f_d≥1 and e_d=0.
- **Split.** The three cases are:
  - f_d=1;
  - f_d≥2 and e_c≤1 for every c∈C;
  - f_d≥2 and e_c≥2 for some c∈C.
  
  They are disjoint and exhaustive by excluded middle. No auxiliary premise is used.
- **Case D matches DEV LF9.** "d carries no 3-marker" means 3∤n_d/3, i.e. f_d=1. Since e_d=0, the only marker d can carry is 5. Both "d unmarked" and "d carries only 5" are in the accepted proof (DEV LF28), and C-markers may share vertices.
- **Case E matches DEV LF10.**
  - For c∈C we have e_c≥1. Under the convention r=n/6 (NFV LF9, RPE LF5), a 2-marker at c means 2|n_c/6, which holds iff e_c≥2.
  - d cannot carry a 2-marker. So "no 2-marker in C" is exactly case E.
  - Every 5-placement is covered: h_d=0 via J2, h_d>0 via J3 (DEV LF30).
- **Case RES matches RESV LF5.**
  - "C-vertex of 2-valuation≥2" must mean v_2(n_c)≥2. RPE LF5 reads base LF25–28 as i* carrying 2^E with E≥1 in r_{i*}, i.e. v_2(n_{i*})=E+1≥2.
  - So e_{i*}=2 lies inside RES, and there is no gap between E and RES.
  - Under a v_2(r)≥2 reading the slice E=1 would fall in neither case. RPE LF5 and RESV LF5's own exhaustion sentence rule that reading out.
- **Compulsory 2-marker.** RPE LF3 confines the correction to X5 LF42–44.
  - The corrected sentence is independently true: h_d≥1 puts d in A_5∩A_3, and C⊆A_3, so RM LF48 forces h_c=0 on all of C. The 2^E at i* is untouched.
  - C LF30 defines the RES case by the presence of that marker, so no step can erase it.
  - C LF18's "changes no used weight or gcd" matches RPE LF3.
- **Scope.**
  - Exponents are explicitly arbitrary (DEV LF9–10, RESV LF5).
  - Cofactors: none of the three statements restricts them. Each quantifies over every RM LF93 configuration, and the only cofactor condition there is P0(b) (RM LF39).
  - 5-marker: a≤1, so it sits on d, on some c, or nowhere. All three placements are covered.
- **No certificate premise.** DEV LF5 rules out LP, search and census. The weights at DEV LF24 and LF28–30 are written inequalities inside accepted proofs. The 43750-row control in RESV LF12 is declared non-premise and is unused at C LF30.
- **Conditional.** RESV LF18 records computer-assisted Sun(6) as load-bearing in the all-gcd5 six-neighbour case.
  - The written route reaches that step only through the S6W site substitution at C LF51/52 inside N39 (LED F17/F18).
  - There, S6W's equal-subgroup clause (C LF13) is load-bearing, because the subgroups U_v∩U_j may coincide.
  - This is a CLOSURE obligation, not part of I2.

### V2. K6.2* (C LF22, LF31): CORRECT as an implication; see MINOR-1 and MINOR-2

- **RM LF92 gives the FULLV LF9 matrix.**
  - C–C pairs have gcd 6 (RM LF49).
  - d∈A_2∖A_3 and a≤1 give P_dc={2}, and that gcd is 4 iff both endpoints lie in E.
  - With d∈E and C∩E={i*}, d–i* has gcd 4 and d–O has gcd 2.
- **Converse.** Seven disjoint left cosets with this matrix form an RM LF92 configuration.
  - If 3|n_d, then 3 would divide gcd(n_d,n_c).
  - Two 5-divisible indices would make some gcd in {2,4,6} divisible by 5.
  - min(e_d,e_{i*})=2 and min(e_d,e_o)=1 give d, i*∈E and e_o=1.
- **Coverage (FULLV LF9).**
  - Exponents and cofactors are unbounded.
  - The 3-marker is absent or on a C-vertex; d∉A_3, so it can be nowhere else.
  - The 5-marker is on d, on i*, on an O-vertex, or absent.
  - The 2-marker positions are fixed by the class.
- **The e_d<4 / e_d≥4 split.** E3 excludes e_d∈{2,3} (FULLV LF9; v14 LF5 "for the whole exact class"). Then min(e_d,e_{i*})=2 gives e*=2.
- **Orientation.**
  - FULLV LF9 covers the labels (1,1), (1,3) and (3,1).
  - (3,1) is reached by actual inversion and ReductionR, and f*≥2 is kept in (1,1).
  - BUD–DEEP retain α_(d i*)=1 (FULLV LF11).
  - In (1,3), t∈O, f*=1 and f_t≥2 are derived, not assumed (v14 LF7).
- **DG premise.**
  - FULLV LF21/23 use DG with G5/G6 conditionally, and M13-A DG*/C2* in (1,3). FB discharges each own-family hypothesis.
  - Per v14 LF6, DG(a)/(b) stays conditional.
  - Per v14 LF9, the own-family four-subset-depth hypothesis is retained. No D3/D4 certificate, CAP cover, M13-B/C/D or C/D replacement is reached.
  - So there is **no unconditional DG premise**.
- **Conditional.**
  - FULLV LF23 retains computer-assisted Sun(5)/(6) transitively.
  - The conservative N16→N57→N58 CAP/RC ancestry and the CI62 gate stay retained (CE2 LF5–7, v14 LF9).
  - LED LF285–287 must not be used to drop that ancestry.

### V3. K7 (C LF19–21, LF32): CORRECT, exhaustive, disjoint

- **Setting.** RM LF91 gives C=V, so n_j=6r_j and 6·gcd(r_j,r_k)=6. The r_j are pairwise coprime, so each prime divides at most one r_j, and |Z|,|T|,|P|≤1.
- **NF step.** NFV LF9–11 gives Z={z} and T={t} with z≠t. Coprimality then gives 3∤r_z, 2∤r_t, and 2,3∤r_w for every w∉{z,t}.
- **Case (a1).** If P is empty, {z} or {t}, then:
  - r_z=2^E 5^{B_z} w_z and r_t=3^A 5^{B_t} w_t, with B_z·B_t=0;
  - the five other vertices are unmarked;
  - the w-parts are pairwise coprime and prime to 30.
  
  This is exactly R2V LF9.
- **Case (a2).** If P={p} with p∉{z,t}, then r_z=2^E w_z, r_t=3^A w_t, r_p=5^B w_p, and the other four r_j=w_j. This is exactly A2XV LF9.
- **Disjoint and exhaustive**, because |P|≤1. This is the partition parent-checked in NFV LF18.
- **No circular edge.** Item 6 consumes K7-NF, not K7-REM (which itself uses (a1), NFV LF12). So no (a1)→NF edge enters.
- **Scopes.** NFV LF11 and A2XV LF9 state unbounded exponents and cofactors explicitly. R2V LF9 imposes only the lower bounds E,A≥1 and B≥0.
- **Inversion.**
  - Actual inversion preserves every n_j, hence every r_j and the sets Z, T, P. So the case assignment does not depend on orientation.
  - Mirrors are handled inside the leaves (R2V LF17; A2XV LF15).
  - A2XV LF9's "no relabelling removes the p-marker" is respected, because item 6 never relabels.
- **Statement-level acyclicity.**
  - NF draws on M0/M1/K7-35/Z2/U1/Z23-P5 (NFV LF18), with no A2X (LF5) and no (a1) (C LF19).
  - R2V LF46 lists neither NF nor (a2), and LF50 adds no (a2) transfer.
  - A2XV LF37 excludes any K62 result and Sun7.
- **Conditional.**
  - NFV LF22, R2V LF5/46 and A2XV LF37 retain computer-assisted Sun(5)/(6). A2XV LF37 requires the written cutover to have "its own accepted composition", which is the CLOSURE gate.
  - C LF20's provenance ("R2's CASEA/CELL chain") is narrower than R2V LF17/46. Those lines also rest on TZ(iii), TC-A22, CASEB/TC-B, A1/A2 via OV v1/v2 with A12C, RICH/D23P, LFC/INV and INV E6.
  - Only R2V LF5/9 is consumed here. The other N48 ancestors belong to CLOSURE.

### V4. These are exactly the remaining COVER leaves: CONFIRMED, taking COVER as a premise

Using C LF41 with RM LF56–65 and LF82:
- |C|=7 is K7.
- |C|=6 type 3 is K6.3.
- |C|=6 type 2 with uniform gcd 2 is removed by D2. Otherwise some i has gcd 4, so d, i∈E, and RM LF49 forces C∩E={i}. That is RM LF92.
- a=2 and |C|≤5 belong to I1.

Items 4–6 use RM LF91–93 verbatim (C LF14).

### V5. Quantifiers: CONFIRMED

| Statement | Groups | Cosets | Equal subgroups |
|---|---|---|---|
| DEV LF9–10 | all (LF13) | left (RM LF33) | universal (RM LF11) |
| RESV LF5 | arbitrary | left (RM) | universal |
| NFV LF9–11 | any | left | universal |
| R2V LF5, LF9 | any (R0) | "disjoint-coset" | universal |
| A2XV LF9 | none admits | left | explicit |
| FULLV LF9 | none admits | left | universal |

- R2V's missing "left" is immaterial: x↦x^{-1} maps disjoint right cosets U_jg_j to disjoint left cosets g_j^{-1}U_j of the same U_j.
- Equal subgroups are a live sub-case only among unmarked index-6 vertices (r=1). Every statement covers that sub-case literally; whether each proof body handles it is for the body census.
- Only finite instances are consumed (C LF25).

### V6. Excluded premises at the implication layer: CONFIRMED

Items 4–6 use none of the C LF57 premises, and no certificate existence or direct Sun5/Sun6 call. C LF25 explicitly declines a least-order frame, and all six leaf statements are universal. Whether these premises are absent inside the leaf bodies (LED F22) is a CLOSURE question; I did not verify it here.

### V7. Bookkeeping: consistent

The N59 inputs at LED LF276 (N36–N39, N48, N52, N58) match rows F08–F12 and F14 (LED LF120–126). F08's RPE note is correct.

## Findings

**MINOR-1: K62X class bound by reference (FULLV LF9 vs C LF31 and C LF86). Axis: completeness/binding.**
- **Step.**
  - C LF31 says K62X's hypotheses are "the class definition and P0/P1".
  - FULLV LF9 instead defines its class "at proof lines 17-24 … with the stated prime-incidence/marker/cofactor conditions". FULL LF17–24 is not pasted, even though C LF86 requires the exact statement text.
  - V2 proves RM LF92 is equivalent to the paraphrased matrix. Beyond that, it relies on FULLV LF9's scope sentence.
- **Consequence.**
  - None, if those lines list only RM LF92 plus P0/P1 consequences.
  - If they contain any extra restriction (for example on distinctness, cofactors or 5-placement), item 5 leaves an unexcluded K6.2* residue.
- **Minimal repair.** Quote FULL LF17–24 in the closure packet or a parent note, and derive each listed condition from RM LF92 and P0/P1.

**MINOR-2: K62X contract wording (C LF22 vs FULLV LF9/21 and v14 LF6/9). Axis: wording.**
- **Step.**
  - C LF22 speaks of "both actual orientations" and "the other orientation". The accepted coverage is three labels, (1,1), (1,3) and (3,1), with f*≥2 kept in (1,1).
  - "Two-deep-triple" has no binding in any pasted accepted text. The accepted conditional is the DG/DG* own-family four-subset-depth hypothesis.
- **Consequence.**
  - None for C LF31, which consumes only "the entire class is empty".
  - A later consumer could read "both" as two cases, or attach the conditional to the wrong DG statement.
- **Minimal repair.** Reword to: "all labels (1,1), (1,3), (3,1) of FULLV LF9, with (3,1) via inversion/ReductionR and f*≥2 kept in (1,1); the conditional DG(a)/(b) and DG*/C2* own-family antecedents are discharged by FB in each family."

## Axes

- **Correctness:** no flaw in C §3 items 4–6 as implications from the literal accepted statements.
- **Completeness:** MINOR-1. COVER/root (I1) and global closure are outside this packet.
- **Process:**
  - The early v1 freeze is recorded (GOV LF3).
  - A2XV LF25–31 records that, after a NO_VERDICT, the second family reviewed Unit3 only through narrowed passes. Unit3 LF15–46 and LF149–157 were read by the parent only.
  - I did not re-adjudicate this.
- **Computation:**
  - I2 uses no computation.
  - RESV LF12 and FULLV LF23 "GS" are non-premises.
  - Transitive computer-assisted Sun(5)/(6) remains in every leaf verdict until the CLOSURE site substitution is accepted.
- **Priority/novelty:** none claimed or assessed.

## Status

C LF30–32 close K6.3, K6.2* and K7 correctly and exhaustively from DEV LF9–10, RESV LF5 with RPE, FULLV LF9, NFV LF11, R2V LF5/9 and A2XV LF9. This holds subject to MINOR-1's literal binding.

These leaf implications remain **CONDITIONAL** on three things:
- **I1:** COVER/root and the other three leaves.
- **FINAL-JOIN-CLOSURE:**
  - the S5W/S6W site substitutions inside N36–N39, N48, N52 and N58;
  - the CAP/RC/CI62 ancestry of N58;
  - the F22 excluded-premise check inside the leaf bodies.
- **The parent verdict.**

N59 and full Sun(7) remain **UNACCEPTED**. This review grants no runtime authority and makes no novelty, Lean or human-review claim.
