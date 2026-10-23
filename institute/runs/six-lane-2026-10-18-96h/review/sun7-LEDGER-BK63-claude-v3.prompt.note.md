# BK63 (N37–N39) second-family interface-closure audit

**Counts: 0 FATAL / 0 MAJOR / 4 MINOR**, plus 3 uncounted nits. All four MINORs are completeness or bookkeeping items. I found no defect in correctness, process, priority or computation.

I read the packet with LEDGER-v1, worker erratum v1, and parent errata v2–v9: the v6 explicit order, the v6 MIN-2 and v9 m1 export boundaries, and the v9 S6 note. I also read RPE, KD2 H5, KE3 J5 and KR2 X1–X2.

## Claim-wise verdicts

1. **Edges and order (LF254–256): valid. The N39 rows cell has one error (m1).**
   - N37/N38 inputs match KD LF6–11 and KE LF6–8 one-to-one:
     - R0 → N03.
     - K6.3 predicate, P0/P1 and the (I)-3 matrix (C–C 6, d–C 3; v8 m-A) → N15.
     - LFC (a), (c), (d) → N12.
     - INV (a)–(b) with E6, and α+α*≤g via E7 without VFC → N13.
     - Class analysis, standard weights and E8 at LE LF71–78 → N14.
     - The Step-1 argument → N29 (v9 m1).
     - Sun(2) (E2) and 1≤α≤g−1 (LE LF14–18, 23–24) → N02.
   - N37/N38 import no VFC, T or F7. So there is no N11/N09/N10 edge, and rows W01–W04 are right. W03 is warranted by S7/S8, which is the same rule v9 m3 applies to N29.
   - N39 inputs also match:
     - L0.1 + Lagrange (X1(i)) and the E1 range (X1(ii)) → N02.
     - R0, K6.3, P0/P1 → N03/N15.
     - LFC → N12; INV → N13.
     - VFC (V1)–(V4) and the count (X2) → N11.
   - N39 excludes the right things. TG is deleted (X1). T, F7, CLIQUE and D-ROW are excluded (KR LF18). There is no ROW-U use (X7), so no N14 edge.
   - Sun(3)/(4) applications sit inside LFC/VFC fibres and enter via N12/N11 (X1/X4), so no direct N01 edge is needed.
   - Every input precedes its consumer in the order N01–N08, N15, N09–N14, N16–N59.

2. **Actual inversion: valid.**
   - By INV(a) with E6 and v6, the inverted configuration has the same labelled index tuple. So the K6.3 predicate, the marking, the branch (f_d and any C 2-marker), v and i* are all unchanged, and D/E/RES apply verbatim to α*.
   - α+α*≤g follows from E7's double-coset argument, without VFC.
   - RES contradiction: g_vd=3, because P_vd={3} and min f≤1 by P0(c). So α_vd=α*_vd=2 violates α+α*≤3 (CW LF99).

3. **H5/J5 gcd premises (the BK63 gate): the premise is verified, but its recording is incomplete (m2, m3).**

4. **Sun sites S7–S9: scope is valid; the S9 route cell is wrong (m4).**
   - **S7 (N37/N38):** a genuine S5W instance arises only when all five members of the subset X lie in R24 with b≥4 (quarter weights).
     - The five pieces are disjoint left cosets of U_j∩U_v inside finite U_v (LFC (c) with E3; at most six pieces). Their label gcds lie in {2,4}.
     - That fits S5W: any group, equal subgroups allowed (S56V LF7–10).
     - N=4 subsets use only Sun(2)–(4).
     - An in-subset R5 class has at most 5 members, so S6's R5/S6W branch never arises inside a subset. S6's R24 branch is this same instance.
     - Any six-piece gcd-5 family elsewhere in KD/KE would still bind through S6/S4 to S6W under W03. An example is five α=5 C-neighbours plus a 5-marked d.
   - **S8 (N38):** at v=d in K63-E, N15 gives n_c=6·5^{h_c}w_c, with no C 2-marker and f_c=1 by f_d≥2 and P1(iv). With g_dc=3, the label is λ_c=2·5^{h_c}w_cα_dc, where α_dc∈{1,2} and at most one h_c>0.
     - So all pairwise gcds lie in {2,4}, matching CW LF93.
     - Five-piece subfamilies (N02 deletion) of at most six pieces in U_d give S5W.
   - **S9 (N39):** six pieces with pairwise label gcd 5 give S6W. For x=α the fibre is in U_v via LFC (c). The x=α* half is m4.
   - There is no seven-piece or frame instance, because v's own fibre is excluded (L LF47–48, E3).

5. **RES correction (RPE LF5): valid.** I checked it independently here; the ledger discharge was FR-only.
   - |C∩E|≤1 (P1(iii)) makes i* the unique C 2-marker, and RPE keeps its 2^E.
   - f_d≥2 forces f_c=1 on C (P1(iv)).
   - h_d≥1 forces h_c=0 on C (P1(ii), |A₅∩A₃|≤1).
   - So z,f∈O′ are unmarked, and gcd(x_z,5)=1 for x_z∈{1,2,3,4}.
   - X5's incompatibility and all weights are unchanged. Certificates that need i*'s 2-part, such as KR LF154 ("with i* iff x_z is even"), stay consistent.

6. **Three-way split (F08, LF120): valid.**
   - The N15 K6.3 predicate puts d∈A₃∖A₂ (cf. L LF131–133), so e_d=0 and f_d≥1.
   - The three branches are disjoint and exhaustive:
     - f_d=1;
     - f_d≥2 with no c∈C having e_c≥2;
     - f_d≥2 with some such c.
   - Each branch predicate depends only on the index tuple, so it is stable under INV.
   - Exhaustiveness is N59's step (C LF18). KR LF198–202 lies outside N39's body (LF21–194). No wider class inference follows (CW LF101).

7. **Excluded premises: valid.**
   - TG is deleted (X1; CW LF129).
   - The CLIQUE/star route is withdrawn and lies outside N39's body (CW LF131).
   - Controls and certificate architecture are provenance only (CW LF132–133).
   - The old computer-assisted Sun5/6 proofs enter only as S5W/S6W statements at S7–S9 (CW LF126; S56V LF14).
   - Exploratory text (D102–103, E79–80) lies outside the bodies (CW LF127).

## Findings

**m1 — the N39 rows cell includes W05 (completeness).**
- **Step:** LF256 gives "W01-W06", which includes W05.
  - W05 is T, discharged by N09, and its only consumers are N32, N34 and N35 (LF173).
  - KR LF18 excludes "the T rule L1", and N39 has no N09 input.
  - FG's product bound comes from L0.1 + Lagrange (X1; CW LF96), not from T.
- **Consequence:** the cell claims a T interface with no edge behind it. There is no mathematical effect.
- **Repair:** set N39 rows = W01–W04, W06.

**m2 — the H5/J5 instances exceed the literal N14/N29 export boundaries (completeness and provenance; the premise itself is verified).**
- **Verified premise.** H5 (KD2 LF30–31) takes v∈C, so g=6 by P1(iii), and a chosen X⊆C∖{v} with |X|=N∈{4,5}. It requires gcd(λ_j,λ_j′)=gcd(α_vj,α_vj′) on X.
  - With α≤5 (E1), this is exactly the input the class analysis needs (L LF85–91):
    - cross-class gcd is 1, so by Sun(2) no allowed set mixes classes and R1 members are singleton-only;
    - R3 pairs have gcd 3; R5 pairs have gcd 5;
    - R24 pairs have gcd 4 iff both are fours.
  - The premise is hereditary to subsets, and LFC (d)'s weight α/6 matches.
  - It is a real premise. Unmarked neighbours satisfy it (P0(b)), but the converse fails. A counterexample: a 2-marked j with α_vj=1 and a j′ with α_vj′=2 have label gcd 2. Then {j,j′} is allowed, and the standard weights 1 and ½ are infeasible.
  - In K63-E every C-vertex has e=f=1 and at most one is 5-marked. So the unmarked C-neighbours of any v already give N≥4.
  - In K63-D, up to three C-vertices may be marked. Reaching N≥4 can then force marked members into X. Their gcd equality is an instance check in KD LF24–96 ([B:CW] CW LF92), which I did not re-verify here.
- **Gaps.**
  - (a) N=4 has no literal provider.
    - v9 m1 exports N29's argument only for five neighbours plus an isolated d (α_vd/g_vd≥1/3, label coprime to the five).
    - v6 MIN-2 limits E8 to LE LF71–78, which covers R1∪R24 only.
    - LE LF79–80, the all-class five-neighbour bound, is N29's own instance.
    - So H5's "min(N,4), stated there for K63-U0 Step 1" has no literal provider for N=4 subsets that meet R3 or R5. ME LF27–30 is not pasted and might state one.
    - The bound itself holds, from the standard weights (L LF95–101) and E8: k5≥1 gives ≥5; k3=4 gives 4; 1≤k3≤3 gives 3+min(4−k3,4)≥4; otherwise min(4,4)=4.
  - (b) H5/J5 say nothing about positive-weight vertices outside X in the same count. This corresponds to N29's "label coprime" clause and is a body obligation.
  - (c) J5 says "not through ROW-U-deg of ME F3". This conflicts with v6 MIN-2 and the v9 S6 note, which make H5/J5 subsets inherited ROW-U-deg applications. Only the six-neighbour conclusions (i)–(iii) are unused, which is what H5 says.
  - (d) W04's discharge cell (LF172) still assigns the H5/J5 subset form to N12–N14/N29.
- **Consequence:** there is no correctness defect. But without an amendment, the N=4 step and the outside-vertex step read as N29 exports that N29 does not supply.
- **Repair (N37/N38 consumer cells):**
  > H5/J5 instances are owned by N37/N38. Premise: label gcds equal α-gcds on the chosen X, checked per certificate. Class analysis, standard weights and E8 come from N14 under the abstract ROW-U-deg premise; conclusions (i)–(iii) are unused. The five-neighbour bound ≥4/6 and the isolated-vertex step come from N29 when its hypotheses hold. The N=4 all-class value ≥4 follows from the check above. Every other positive-weight vertex's compatibility with X is checked in the KD/KE body.

  In W04's discharge cell, add "[B:CW] N37, N38 (CW LF92–95) for H5/J5 instances".

**m3 — N38's declaration range omits the text that carries J5's premise (completeness).**
- **Step:** LF255 lists only KE LF6–8 and KE3 J5 LF24–26. J5 states no N-range and no gcd premise of its own. It gets both only through "As in K63-D-erratum-v2.md H5", while replacing KE LF7's "under ROW-U-deg".
- **Consequence:** as currently ranged, N38's declared interface has no gcd hypothesis.
- **Repair:** add "KD2 H5 LF28–33 (hypothesis text only, via J5)" to N38's declaration cell. This is a text citation, not an N37 theorem edge; such an edge would be forward anyway.

**m4 — S9's x=α* half names the non-operative route and coset side (completeness).**
- **Step:** LF303 binds S9 only "via S4 (LFC (c))", with "U*_v (x=α*, inverted configuration)". But KR2 X2 LF22–29 makes VFC (V1)–(V4) plus the count the operative proof of §2(a), and calls the inverted-LFC proof an alternative that is "not needed".
  - So the operative Sun(6) instance lies in a right-coset fibre R=U_v y.
  - Each piece is R∩g_jU_j = H_j x_j, where H_j = U_v ∩ x_jU_jx_j⁻¹.
  - Right-translating by y⁻¹ gives H_j u_j = u_j(u_j⁻¹H_j u_j) with u_j∈U_v.
  - These are pairwise-disjoint left cosets in U_v of index d_j = n_jα*_vj/g_vj (V2 with INV(b)), and there are at most six of them (V3; CW LF130, LF136).
- **Consequence:** S6W's scope still fits, and N39 already has the N11, N12 and N13 edges, so there is no correctness or edge effect. However, under X1 this instance is carried by the N11 (VFC) edge rather than S4, and the site cell names only the unused alternative.
- **Repair:** set the S9 route cell to:
  > x=α: left fibre in U_v, LFC (c), S4. x=α*: right fibre U_v y translated into U_v, VFC (V3) via N11 (operative, KR2 X2); equivalently U*_v via S4 on the inverted configuration (X2 alternative).

## Uncounted nits

- **n1:** KR2 X1(i) cites "old README section 1, L0.1", but the pasted README §1 (LF27–29) contains only R0. The provider is N02 either way (W02, X8); only the locator needs fixing.
- **n2:** KR LF8–9 says "as used in … K63-D/E section 1". This is a scope pointer; the objects it imports come from N03/N15. If KR's body (not pasted) cites a derived statement from KD/KE §1, add conservative forward edges N37/N38→N39. Nothing in the pasted text needs them.
- **n3:** The |P*|=3 half of S8

(CW LF93) applies D-ROW to the inverted configuration, since KE imports no VFC. So that half runs at U*_d, not U_d. The v9 S4 wording ("U_v/U*_v") already covers it, but S8's ambient cell could read "U_d (U*_d via INV(a))".

## Bottom line

After m1–m4 are recorded, local BK63 closure of N37–N39 is **valid relative to the named provider boundaries**:
- the N02, N03, N11–N15 and N29 exports as fixed by errata v5–v9 (N29 per v9 m1);
- the KD, KE and KR bodies at [B:CW] CW LF92–101;
- RPE.

The H5/J5 gate closes at the interface level. The declared premise (label gcds equal α-gcds on a chosen set of N∈{4,5} C-neighbours of v∈C, with g=6) is the abstract ROW-U-deg premise, and it is sufficient and hereditary. Whether each certificate satisfies it rests on the [B:CW] body discharge, not on N14 or N29. It is automatic in K63-E but needs an instance check in K63-D, where marked members may be forced into the subset.

This approves nothing about full Sun7, the global graph or final join, runtime, novelty, human or Lean status.
