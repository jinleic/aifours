# FINAL-JOIN-IMPLICATION I1: hostile written review

**Slice reviewed:** N59 root (R0 and COVER) and the leaves KII, K5.2* and K5.3.

**Reading order:** I read the governing addendum and ledger erratum v14 first. Then I read candidate v1 (`cand`) with composition errata v1 and v2 (E1, E2), README (`RM`), WR, S56V, S56W with its errata v1 and v2, C5W, C56W, X1V, K52V, KIIV and the pasted ledger rows.

**Method:** I used only the pasted text. No files, tools or computation were used.

**Counts: 0 FATAL · 0 MAJOR · 1 MINOR.** I found no counterexample, logical gap, circularity or quantifier error in this slice. The one MINOR (m1) is an interface-binding gap. It leaves one COVER branch conditional.

**Treated as dated or superseded, and as neither premise nor defect:**
- WR LF5/LF56 "classes OPEN"
- C5W LF17 and C56W LF13
- K52V LF19 and KIIV LF19
- cand §6 numbered order (withdrawn by E2 item 1) and cand §7
- ledger C3 LF285–287 (superseded by E2 item 1 and v14 item 5)

## Claim-wise verdicts

### V1 · R0: ACCEPT (RM LF29; cand LF11, LF25; WR LF18)
- core_G(U_i) is the kernel of G→Sym(G/U_i). So N = ∩core_G(U_i) is normal, has finite index, and N ≤ U_i.
- Since U_iN = U_i, each g_iU_i is a union of N-cosets. It is therefore the full preimage of its image (g_iN)(U_i/N).
- Images of disjoint full preimages are disjoint.
- [G/N : U_i/N] = [G:U_i], and the same holds for U_i∩U_j ⊇ N.
- The construction applies to the given counterexample and makes no choice. LF25 forbids least-order selection, and no later I1 step reintroduces it.
- The leaves consume only indices and disjointness, so preserving intersection indices is surplus.

### V2 · P0/P1: ACCEPT (RM LF22–24, LF37–52; overlay WR LF46, 5-valuation written h_i)
I re-derived the following:
- Coprime indices give |UV| = |G|·[G:U∩V]/(n_U·n_V) ≥ |G|, using lcm | [G:U∩V]. This needs |G| finite, which R0 supplies. So UV = G, and by L0.2 the cosets meet.
- A common prime ≥7 would give gcd ≥7.
- The residual 2^α·3^β·5^γ lies in [2,6], so it is 2, 3, 4, 5 or 6 with the listed valuation triples.
- P1(i)–(iv) follow immediately.

### V3 · R1(7) and the only root Sun5/Sun6 sites: ACCEPT (RM LF61–65; cand LF38–40, LF49–50; S56W LF17–25; S56V LF5–10; F15/F16)
- **a ≥ 3.** By P1(ii), A_5 has at most one vertex in A_2 and at most one in A_3. So some x lies in A_5∖(A_2∪A_3).
  - P_xj ⊆ {5} and P_xj is nonempty, which forces A_5 = V.
  - P1(ii) then forces P_ij = {5} for every pair.
  - By deletion, six of the original cosets in the finite G have all gcds equal to 5 < 6. This contradicts S6W (any group, possibly equal subgroups). This is site S1.
- **a = 2.** A vertex outside A_5 exists, so x and y both lie in A_2∪A_3.
  - P1(ii) rules out both in A_2 and both in A_3. So x ∈ A_2∖A_3 and y ∈ A_3∖A_2, and neither lies in C.
  - Every other j meets x only through 2 and y only through 3, so j ∈ C. This is case (II), with |C| = 5.
- **a ≤ 1.** No pair has gcd 5.
  - S5W on each five-subfamily of the original cosets gives a pair with gcd 6, meaning two C-vertices. This is site S2.
  - If |V∖C| ≥ 4, some five-set would contain at most one C-vertex. Hence |C| ≥ 4.
  - A D-vertex outside A_2∪A_3 would have P_dj = ∅, as would a mixed 2-only/3-only pair. Hence the type is uniform.
- **Authority of S5W/S6W.** Both are accepted at every-group, equal-subgroup, no-frame scope (S56V LF5–10; erratum v2 m3, m6, m7).
- **Gates.** H5 and H6 are discharged by C5W LF5 and C56W LF5.
- **Sites.** In RM LF56–83 these are the only Sun5/Sun6 uses; V5 covers VFC. The tags [S6W@S1] and [S5W@S2] match.

### V4 · |C| = 4 eliminations: ACCEPT, with R1c conditional on m1 (RM LF71–79; cand LF43)
- **R1a.** Type 3 with D = {d_1,d_2,d_3} and i ∈ C gives four original cosets with all gcds 3 < 4. This contradicts Zhu Sun(4).
- **R1b.** Type 2 with d ≠ d′ and e_d = 1.
  - The triple {d,d′,i} has gcds 2 and 2, so Zhu Sun(3) forces gcd(n_{d′},n_i) = 4.
  - That puts every C-vertex in E, which contradicts |C∩E| ≤ 1.
  - Hence D ⊆ E, and D–D gcds are 4.
- **R1c.** Pick i ∈ C with e_i = 1.
  - r_1 = n_i/2 is the odd part of n_i.
  - gcd(n_i, n_{d_t}) = 2 makes the odd parts coprime, so gcd(r_1, n_{d_t}/4) = 1.
  - gcd(n_{d_s}, n_{d_t}) = 4 with min e = 2 gives coprime quarters.
  - So the four cosets realise (2r_1, 4r_2, 4r_3, 4r_4) with the r_i pairwise coprime and r_1 odd. This is exactly the tuple at RM LF19 and cand LF43.
- **What this instance requires of the authority:**
  - 3 | r_1 is forced, because i ∈ C.
  - At most one of r_2..r_4 is even.
  - A 5-factor may occur.
  - r = 1 may occur.
  - U_{d_s} = U_{d_t} is possible a priori, at index 4.

### V5 · D2/D2′: ACCEPT, with no Sun5/Sun6 load (RM LF81–83; WR LF34, LF36, LF47–48; cand LF52)

**Fibre facts from WR LF34, re-derived.** Normalise g_v = 1.
- D_j = U_v·g_j·U_j is disjoint from X_j = U_v·U_j ⊇ U_v. Otherwise g_j ∈ U_vU_j, and U_v would meet g_jU_j.
- μ(D_j) = q_j/g_vj and μ(X_j) = α_vj/g_vj, where q_j and α_vj are integers with 1 ≤ q_j ≤ g_vj − α_vj. This uses lcm | [G : U_v ∩ xU_jx⁻¹].
- Each right fibre U_v·y ⊆ D_j meets g_jU_j in the set (U_v ∩ w_jU_jw_j⁻¹)·w_j.
- Translating on the right by y⁻¹ and then inverting turns the simultaneous pieces into pairwise disjoint LEFT cosets in U_v of index d_j = q_j·n_j/g_vj.
- ∪D_j ⊆ G∖U_v.
- If every fibre holds at most M pieces, then Σμ(D_j) ≤ M·μ(∪D_j) < M.

**D2 (apex d, six C-neighbours with g = 2).**
- Each q_j = 1, so each mass is 1/2 and d_j = n_j/2.
- gcd(n_j/2, n_k/2) = 3. Four pieces in one fibre would violate Sun(4), so M = 3.
- The total mass is 3, which would have to be < 3.

**D2′ (apex d_1).** R1b gives g = 4 for the pair d_1, d_2. C∩E = ∅ gives g = 2 to C and makes each n_c/2 odd.
- The C-pieces have mass 1/2 and local gcd 3, so μ(∪_C D_c) ≥ 5/6.
- For d_2, q ∈ {1,2,3} and gcd(q·n_{d_2}/4, n_c/2) = gcd(q, n_c/2).
- If q = 1 or 2, the local gcd is 1. By Sun(2) in U_v, D_{d_2} shares no fibre with any D_c, so the total is ≥ 1/4 + 5/6 > 1.
- If q = 3, every local gcd is 3, so M = 3. The total mass is 13/4, giving μ(∪) ≥ 13/12 > 1.

**Consequences.**
- Every local gcd is ≤ 3, so any fibre with four or more pieces already contains a 4-set violating Sun(4).
- The VFC Sun(5)/Sun(6) clauses (F18 [S5W/S6W@S5]) are formally present but are not load-bearing here.
- Each fibre holds at most 6 pieces, because the apex's own fibre is exclusive.
- No minimal-order assumption is used (WR LF36, LF49, LF60).

### V6 · Exhaustive six-class split: ACCEPT, with the R1c branch conditional on m1 (RM LF85–96; cand LF14, LF36–43; WR LF21; F04)
- a ≥ 3: contradiction via S6W.
- a = 2: KII.
- a ≤ 1: |C| ∈ {4,5,6,7}.
  - |C| = 7: K7.
  - |C| = 6, type 3: K6.3.
  - |C| = 6, type 2: the d–i gcd is 4 exactly when both d and i lie in E. Either all six gcds are 2, which D2 excludes, or d ∈ E and C∩E = {i*}, which is K6.2*.
  - |C| = 5, type 3: K5.3.
  - |C| = 5, type 2: R1b gives D ⊆ E. If C∩E = ∅, D2′ applies. If C∩E = {i*}, the class is K5.2*, with d_1–d_2 gcd 4, d_t–i* gcd 4 and d_t–(C∖i*) gcd 2.
  - |C| = 4: R1a, or R1b with R1c.

No other branch exists. The six classes are pairwise disjoint because a, |C| and type separate them. The list is identical to RM LF89–96 and to cand LF36–43.

### V7 · KII leaf: ACCEPT (cand LF17, LF27; RM LF96; KIIV LF5, LF9, LF11; F07)
- KII is the set of all CEs with a = 2.
- KIIV LF5's literal scope is: any group, seven disjoint left cosets, all gcds ≤ 6, exactly two 5-divisible indices. That is this class, with no extra restriction.
- The LF9 normal form is internal to KIIW and agrees with case (II).
- Imports: elementary facts, a re-proved Sun(2), and Zhu Sun(3). There is no Sun4/5/6/7, VFC, StageB, K52W or least-order input.

### V8 · K5.2* leaf after COVER/D2′: ACCEPT (cand LF16, LF28, LF42; RM LF94; K52V LF5, LF9; F06)
- COVER's output is RM LF94's matrix with s = i* and O4 = C∖{i*}. This is exactly K52V LF9's scope.
- The "equivalently" normal form is implied by the matrix and does not narrow it:
  - 4 | n_d and 12 | n_s.
  - gcd(n_d, n_o) = 2 together with 4 | n_d forces r_o odd.
  - gcd(4q, 12q_s) = 4 gives gcd(q, 3q_s) = 1, hence 3 ∤ q_1q_2.
  - gcd(4q, 6r_o) = 2 gives gcd(2q, 3r_o) = 1.
  - gcd(12q_s, 6r_o) = 6 gives gcd(2q_s, r_o) = 1.
  - The remaining pairs give coprimality directly.
- a ≤ 1 holds automatically, since no matrix entry is divisible by 5.
- K52W is applied only after D2′ has removed C∩E = ∅ (K52V LF9; cand LF28).
- Imports: elementary facts and Zhu Sun(4).

### V9 · K5.3 → X1 bridge: ACCEPT (cand LF15, LF29; RM LF57, LF67, LF95; WR LF24; X1V LF5, LF19–20; F05/F13)
- Each n_{d_t} is odd, every pair meeting D has gcd 3, and C–C pairs have gcd 6.
- Set r_d = n_d/3 (odd) and r_c = n_c/6.
  - gcd(3r_1, 3r_2) = 3 gives gcd(r_1, r_2) = 1.
  - gcd(3r_d, 6r_c) = 3·gcd(r_d, 2r_c) = 3 gives gcd(r_d, r_c) = 1.
  - gcd(6r_c, 6r_{c′}) = 6 gives gcd(r_c, r_{c′}) = 1.
- By deletion, the two d-cosets and any three C-cosets are disjoint left cosets of indices (3r_1, 3r_2, 6r_3, 6r_4, 6r_5), with r_1 and r_2 odd and all five pairwise coprime.
- This is literally the statement at X1V LF5. It includes r = 1, 3 | r_d when f_d ≥ 2, one even r_c, and a 5-factor anywhere.
- X1 imports only its proved pairwise left-fibre bound (LF19). Menon and M-S appear only as attribution (X1V LF7; WR LF24).

### V10 · Quantifiers: ACCEPT

| Input | Group | Equal subgroups | Side | Frame |
|---|---|---|---|---|
| Target (cand LF6) | every group | allowed | left | none |
| R0 (RM LF29) | every group → finite G/N | preserved | left | no selection |
| S5W/S6W (S56W LF17–25) | every group | explicit | left | none (m3, m6) |
| Zhu Sun3/4 (cand LF12) | every group | not restated (see O1) | left | none |
| Prop4.5 (S56W) | **not pasted (m1)** | not pasted | not pasted | m6 forbids frames |
| VFC (WR LF34) | U_v | may coincide | right fibres → left cosets | ≤ 6 pieces |
| X1 / K52W / KIIW | no group / arbitrary group / arbitrary group | no distinctness hypothesis | left | none |

### V11 · Excluded premises: none operative in this slice (cand LF55, LF57; F21, F22)

The load-bearing set is:
- elementary facts and R0
- Sun(2)
- Zhu Sun(3) and Sun(4)
- S6W at S1 and S5W at S2
- the written Prop4.5 (subject to m1)
- WR's VFC
- X1, K52W and KIIW

Nothing else is load-bearing:
- No seven-piece fibre occurs.
- No least-order frame is used.
- No StageA or StageB output is used.
- No Menon result or M-S Lemma 4.6 is used.
- No historical computer-assisted Sun5/Sun6 is used. Per S56V LF14, C5W LF13 and C56W LF11, S5W, S6W, C5W and C56W import neither.
- RW and CAP reach N59 only through N58 (K6.2*, which is I2's scope).
- The k5 engine control C1 (RM LF19) is not used.

### V12 · Remaining leaves: CONFIRMED, not adjudicated (cand LF18–22, LF30–32)
After KII, K5.2* and K5.3, the COVER output is exactly K7, K6.2* and K6.3. Steps 4–6 address exactly these. Their exclusions belong to I2.

### V13 · Ledger cells: consistent for this slice (LF105, LF113–134, LF276)
F01–F07, F13, F15, F16, F19, F21 and F22 describe the same interfaces as above. The following are remarks, not findings:
- LF276 lists N24 alongside N25, which is redundant but harmless.
- The pasted rows do not show which node numbers carry R1a–c, D2 and D2′, or their Zhu and Prop4.5 edges. That check belongs to the closure gate.

## Finding m1: MINOR (completeness and interface binding; not a correctness defect)

**Source:** cand LF43 and LF53; RM LF19 and LF75–79; S56V LF10 and LF14; S56W erratum v2 m4, m5, m8 and the LF15 note; ledger F19.

**Missing premise text.** After m5, the operative authority at R1c is the written Prop4.5 in S56W. Its literal statement is not in the packet. S56V LF14 and m4 require a site-specific scope check against that statement. Only RM LF19's old wording and the tuple at cand LF43 are available to check against.

**Scope the statement must cover:**
- every finite group
- four disjoint left cosets of indices (2r_1, 4r_2, 4r_3, 4r_4)
- r_i positive and pairwise coprime, with r_1 odd
- no restriction on where 3 or 5 divide (3 | r_1 is forced here)
- no restriction on an even r_i, on r = 1, or on coincident subgroups
- no minimal-order assumption

**Consumer-visible consequence.** If the S56W statement is narrower than this, the type-2 |C| = 4 branch becomes an uncovered seventh COVER leaf. N59 would then not follow. Nothing else in I1 is affected.

**Expected outcome.** This should be a pure binding fix with no new mathematics. RM LF19 has no such restriction. S5W's no-frame, every-finite-group acceptance also needs Prop4.5 at a correspondingly general scope, since Prop4.5 is in its DAG (note at LF15).

**Minimal repair.** Paste the exact S56W Prop4.5 statement with the overlays from errata v1 and v2. Then record the one-line check: "R1c instance at cand LF43 ⊆ S56W Prop4.5 scope". No proof step changes.

## Observations (not counted)

**O1 · Zhu with coincident subgroups (cand LF12; F02).** The text omits "subgroups may coincide", although the R1a and D2 sites can meet coincident subgroups. Under ordinary reading the wording already covers them. The case also reduces to Sun(2):
- Suppose U_1 = U_2 = U.
- If U has index 2, there is no room for a third coset.
- If the index is ≥ 3, Sun(3) holds outright; if it is ≥ 4, Sun(4) holds outright.
- For Sun(4) at index exactly 3, the other two cosets lie in the third U-coset, so U_3 and U_4 lie inside U.
- Sun(2) inside U then gives gcd(n_3/3, n_4/3) ≥ 2, hence a gcd ≥ 6.

**O2 · Reading of "3-only" (cand LF29).** It means "in A_3∖A_2", not "a power of 3". The bridge uses only that n_d is odd.

**O3 · Governing errata for K52 and KII (F06/F07).** Items 1–5 of each parent erratum are not pasted. V7 and V8 rely only on the verdict-level scopes at K52V LF9 and KIIV LF5. If the closure gate finds an item that alters those statements, V7 and V8 need re-checking.

**O4 · Process.** The original freeze at 19:38:36 predates the CUT2-M12 disposition at 20:15:39. The addendum records this, and I reviewed the corrected v2 reading. CUT2-M12 concerns N56 and N58, which are outside I1. F-1 and the computer-assisted provenance records remain.

## Axes
- **Correctness:** no flaw.
- **Completeness:** m1. Component proof bodies were taken at their accepted statements, apart from the re-derivations above.
- **Process:** O4; nothing new.
- **Computation:** nothing computational is load-bearing.
- **Priority/novelty:** none claimed.

## Boundary
**I1 verdict.** R0, COVER and the KII, K5.2* and K5.3 leaves compose correctly from the literal accepted statements. The type-2 |C| = 4 branch is conditional on m1.

**What remains open.** This is not a Sun7 verdict. Still required:
- I2 (K6.3, K6.2*, K7)
- FINAL-JOIN-CLOSURE
- N59 and global closure
- the parent verdict

Sun7 remains UNACCEPTED. I make no runtime, novelty, first-result, publication, Lean or human-review claim.
