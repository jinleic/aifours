# S56W-v1 hostile mathematical review, read with parent erratum v1

**Scope of this review.** I reviewed `S56W-v1.md` (9dfa36…b894, LF1–193) as amended by parent erratum v1 (b2299b…aae02), which governs. Sources were read only as excerpted in the package. I used no tools, computation, edits or delegation. "PASS" means I have no finding.

## Bottom line

- **FATAL: none.**
- **MAJOR: none** once erratum v1 is applied.
  - Before the erratum, L3 and K2 (LF54–61) were false as standalone statements because they lacked a disjointness hypothesis.
  - Erratum item 1 closes this exactly.
- **MINOR: nine items (m1–m9).** All are wording, audit-labelling or packaging issues. None changes a mathematical step.
- **What the file establishes, if adopted.** Only two implications: **H5 ⇒ S5W** and **H5 ∧ H6 ⇒ S6W**.
  - Both hold at the full accepted scope: every group, subgroups possibly equal, no cover assumption.
  - The only external import is Zhu Theorem 1.1 (k = 3, 4).
  - It does not establish an unconditional written Sun(5) or Sun(6).

## 1. Erratum v1 check

**Item 1 (standing disjointness hypothesis at LF35): correct, necessary and sufficient.**
- L3's proof (LF56–59) applies L0.2 to pairs inside S, and also uses that g_vU_v and g_iU_i are disjoint.
- Without disjointness L3 is false: take U_v = U_i = U_j = G. The pair condition holds, but the sum is |S|.
- Every use of L3 or K2 (Prop 4.5 steps b, c, d, f, g) is inside the disjoint family g_1U_1, …, g_4U_4.
- The clause only defines notation for the family. L0.4–L0.6 are stated for arbitrary A, B, C and are unaffected; L1 and L2 are merely narrowed.

**Item 2 (identity wording): correct.**
- S5W omits two sentences from the accepted text:
  - "Infinite G is included…" is implied by "every group" together with R0.
  - "No all-k theorem…" is a non-claim.
- S6W omits only the sharpness sentence.
- The mathematical statement and scope are identical. Three sites still claim literal identity (see m1).

## 2. Claim-wise verdicts

| Claim | Lines | Verdict |
|---|---|---|
| S5W/S6W equal the accepted statements | LF16–25 | PASS under erratum item 2 (m1) |
| H5/H6 equal proof-v4 L49 / README L27 / C5W L110–112 / C56W L109–110 | LF26–31 | PASS: identical apart from the ellipsis character; none assumes distinct subgroups or a minimal frame |
| L0.1–L0.3 | LF38–42 | PASS |
| L0.4–L0.6 (granularity, double cosets, Sun(2)) | LF43–48 | PASS |
| L1 (T1–T3), L2 | LF49–53 | PASS (m8) |
| L3, K2 | LF54–61 | PASS with erratum item 1 |
| Dispositions of errata E1–E10 | LF62–65 | PASS: E6 and E9 are genuinely applied (m8) |
| Proposition 4.5, steps (a)–(g) | LF67–103 | PASS (step audit below) |
| R1 | LF106–115 | PASS |
| S5W proof | LF116–120 | PASS, conditional on H5 |
| R1(6) with C1 | LF123–137 | PASS |
| S6W proof and the C1 alternative route | LF138–141 | PASS, conditional on H5 and H6 |
| R0 | LF143–147 | PASS |
| DAG and audit | LF149–167 | PASS for nodes inside the file; m2, m3 |
| Substitution protocol | LF169–186 | PASS once restricted; m4–m7 |
| Non-claims | LF188–193 | PASS (m1 at LF190) |

**Proposition 4.5 step audit.** No determinant appears anywhere; I read that request as covering the 1/gcd granularity denominators from L0.4.

- **(a)** gcd(2r_1, 4r_i) = 2. Hence α(1,i) = 1 and I_1i = 4r_1r_i. PASS.
- **(b)**
  - T_123 is divisible by lcm(2r_1, 8r_2r_3) = 8r_1r_2r_3.
  - The apex-1 lower bound is ≥ 1/2, so L2 applies.
  - The inverted inclusion U_2U_1 ⊆ U_3U_1 is L3's first alternative at v = 2 for (i, j) = (1, 3).
  - The L3 sum is 1/2 + 2/4 = 1, a contradiction. PASS.
- **(c)**
  - Write T = 4r_1r_2r_3τ. Since 12r_2r_3 divides T, 3 divides r_1τ.
  - At apex 2 over edge 13, τ/4 ≤ size(U_2U_1) = 1/2. So τ ≤ 2 and therefore 3 | r_1.
  - Granularity: 1/gcd(4r_2, 4r_1r_3) = 1/4.
  - The size 1/2 is excluded: the inverse U_1U_2 ⊆ U_3U_2 is the first alternative at v = 1 for (2, 3), giving 1/2 + 1/2. PASS.
- **(d)**
  - At apex 2, τ/4 ≤ 1/4, so τ = 1. Here any apex works, because all three α equal 1.
  - The lower bounds at apex 1 in triangles {1,2,4} and {1,3,4} hold.
  - At v = 4 with S = {1,2,3}, every pair satisfies the first alternative, and 1/2 + 1/4 + 1/4 = 1. PASS (m8).
- **(e)** The apex choice matters here.
  - At apex 2 (or 3), the bound is τ ≤ α(2,4)α(3,4) = 1.
  - At apex 4 the bound would only be τ/12 ≤ 1/4, i.e. τ ≤ 3, which is useless.
  - LF91's identification of proof-v4's bound as the apex-2 bound is therefore correct.
  - 12r_2r_3 dividing 4r_2r_3r_4 forces 3 | r_4, contradicting 3 | r_1. PASS.
- **(f)**
  - 3 | τ because 3 does not divide r_4.
  - At apex 3, τ/12 ≥ 1/4, so L2 applies.
  - U_4U_3 ⊆ U_2U_3 is the second alternative at v = 4 for (2, 3), giving 3/4 + 1/4. PASS.
- **(g)**
  - Granularity: 1/gcd(4r_2, 12r_3r_4) = 1/4, since 3 does not divide r_2.
  - The size 3/4 is excluded by K2 with (2, 3, 4), i.e. L3 at vertex 3 with S = {2, 4} using U_3U_2 ⊆ U_4U_2.
  - The final count is 1/2 − 1/4 − 1/4 = 0, yet 1 ∈ U_2, which lies in A∩B∩C.
  - Applying (c) to the pair (2, 4) uses the legitimate 3↔4 relabelling (m8). PASS.

**R1, R1(6), R0 and scope.**
- **R1.**
  - No gcd equals 1 (L0.6 with L0.2).
  - If some index is odd, 3 divides all five indices and every gcd is 3.
  - If all indices are even, the odd parts are pairwise coprime, min(e_i, e_j) ≤ 2, and at most one e_i ≥ 3.
  - The split by number of indices with e = 1 (at least two, exactly one, none) is exhaustive, with pairwise-coprime r's in each branch.
- **R1(6).**
  - Each pair of indices shares exactly one prime from {2, 3, 5}.
  - Σ C(|A_p|, 2) = 15, with |A_p ∩ A_q| ≤ 1.
  - The value 10 would need two binomials summing to 5, which is impossible. Without 10, the only multiset is 6 + 6 + 3, and two 4-sets meeting in at most one point need at least 7 points. So some |A_p| = 6.
  - Case p = 3: all fifteen gcds equal 3 (C1 applied at LF133–134).
  - Case p = 2: reduces to R1 step (3).
  - Case p = 5: indices are 5r_i with pairwise-coprime r_i, possibly with 5 dividing one r_i, which H6's literal statement covers.
  - The C1 override "Core(5) input is H5" is stated explicitly (LF124). The alternative route uses S5W, which is upstream, so it is not circular.
- **R0.**
  - N lies in every U_i, so each coset is a full preimage. Indices, intersection indices and disjointness all pass to G/N.
  - Prop 4.5's "By R0" is a forward reference, not circular.
- **Equal subgroups.**
  - No step assumes the subgroups are distinct.
  - Two subgroups can coincide only where their indices agree:
    - among U_2–U_4 with r = 1 in Prop 4.5;
    - with r_i = r_j = 1 in H5/H6;
    - at index 3 in the Zhu k = 4 branch.
  - Coincidence is impossible in the Zhu k = 3 branch.
- **No minimal frame anywhere.** The notes at LF120 and LF141 are true.

## 3. MINOR findings and exact repairs

The original file is immutable, so these would go in a parent erratum v2.

**m1. Literal-identity claims left uncovered by erratum item 2.**
- LF16: "(identical wording for later import substitution)" → "(identical mathematical statements, notation normalized, for later import substitution)".
- LF190: "quotations match their sources exactly" → "are mathematically identical to their sources (notation normalized; trailing remarks omitted)".
- Package LF37: "Verbatim equality" → "Identical mathematical statement and scope (erratum v1 item 2)".

**m2. The audit states unaudited facts about H5/H6, and one literal claim is false.** LF166–167 says "No proof in this DAG invokes Sun(5)", but the optional route at LF140–141 invokes S5W.
- LF155, last column → "claimed by C5W: no Sun(5)/S5W/bridge/minimal frame; discharge condition (C5W gate)".
- LF156, last column → "claimed by C56W: no Sun(6)/S6W, no Sun(6) inside subgroups, no minimal frame; discharge condition (C56W gate)".
- LF162–163: "(their own proofs import only Sun(2) and Zhu k = 3, 4)" → "(claimed to import only Sun(2) and Zhu k = 3, 4; not audited here)".
- LF165–167, from "**Circularity check:**" to the end of the sentence → "**Circularity check:** no proof here uses the accepted Sun(5)/Sun(6); the only Sun(5)-statement use is S5W in the optional route at LF140–141, which is upstream of S6W. Non-circularity of H5/H6 is a discharge condition of their own gates."
- Package LF12–13 and LF42 need the same qualification.

**m3. The consumed scope of H5/H6 is never stated.** Insert after LF32 (wording in §4 below).

**m4. Section 8 item 1 reads as unconditional and pre-clears citation sites.**
- LF173: "both theorems hold in every group" → "both theorems, conditionally on H5 (S5W), resp. H5 and H6 (S6W), until item 2 is met, hold in every group".
- LF172, after "may cite instead", add: "only where the imported item is literally the Sun(5)/Sun(6) statement (items 4–5); the listed sites are examples to be checked individually, not pre-cleared".

**m5. LF184 implies Prop 4.5, R1 and R1(6) are already accepted.** Replace "(e.g. Prop 4.5, R1, R1(6)), as here." with "(Prop 4.5, R1, R1(6) qualify only through their written re-proofs here, once this composition is accepted)."

**m6. LF186 is ambiguous about the ambient group and the minimal frames.**
- After "(sub-families by deletion);" insert: "indices are taken in the group where the statement is applied (e.g. in U_v); right cosets are first inverted (same subgroups);".
- Replace "no use of the minimal frames." with "no import of the Sun(5)/Sun(6) minimal-order frames or of results proved only inside them (e.g. C18's frame-restricted Core5(6))."

**m7 (optional). LF175 is conservative but imprecise.** Replace "Until the parent accepts H5 (C5W), H6 (C56W) and this composition" with "Until the parent accepts this composition and C5W (for S5W), resp. C5W and C56W (for S6W)".

**m8. Notation.**
- LF35: "G is finite until section 6." → "G is finite in section 2 and in R1/R1(6); all-group statements reduce to this by R0 (section 6)."
- LF49: append "Put tau = T/L."
- LF84: "T is a" → "T_124 = [G : U_1 cap U_2 cap U_4] is a".
- LF85: "T/(2r_1" → "T_124/(2r_1".
- LF86: "likewise U_4U_1" → "likewise (triangle {1,3,4}) U_4U_1".
- LF96: "By (c) for the pairs (2,3) and (2,4)," → "By (c), and (c) with 3 and 4 interchanged,".
- LF63: "'harmonic' defined" → "'harmonic' unused (disjointness stated directly)".
- LF112 and LF135: "two indices" → "at least two indices".

**m9. Package hygiene.**
- Package LF15: "138-143" → "138-141".
- Remove the stray "## 6. R0 (complete)" (package LF28) from inside the code fence.

**Notes (no defect).**
- **N1, Zhu import.** It is imported at the scope stated in rules-v1 L0.7 ("in every group"); I cannot inspect arXiv:0807.2207.
  - The equal-subgroup case is not load-bearing anyway. Suppose U_1 = U_2 = U in the k = 4 branch, so U has index 3. The other two cosets lie in the third coset hU. Then U_3, U_4 ≤ U, and h⁻¹g_3U_3, h⁻¹g_4U_4 are disjoint cosets in U with coprime indices n_3/3 and n_4/3. That contradicts L0.6 in U.
  - This sentence can be added after LF120 if wanted.
  - Zhu's freedom from computation is not re-verified here; the gate ruling's gap list does not name it.
- **N2, Prop 4.5 in the Sun(5) DAG.** SCOPE LF16 and the authority's DAG shape omit Prop 4.5 for Sun(5). LF159 and LF161 correctly include it. This deviation is correct and should be disclosed.
- **N3, H5/H6 proof blocks (context only, not a gate verdict).**
  - The visible "inverse" step is consistent with an elementary lemma. The inverted family consists of left cosets of the conjugates g_iU_ig_i⁻¹, in the same G and with the same indices.
  - The double coset U_i(g_i⁻¹g_j)U_j is disjoint from U_iU_j, which gives α* ≤ g − α.
  - Nothing visible imports Sun(5) or Sun(6). Lemmas PR, AR, P6 and A6 are not in the package.

## 4. H5/H6: no hidden stronger scope, but discharge conditions apply

The composition consumes H5 only at R1's fourth branch and at R1(6)'s p = 2 branch with no index having e = 1. It consumes H6 only at R1(6)'s p = 5 branch. In both cases the configuration sits in a finite quotient and the hypothesis is used at its literal statement.

That literal scope is unrestricted, which is stronger than anything the old records certified directly: proof-v4 F-3 worked in a minimal-order frame, and k6 erratum C18 certified Core5(6) only "in a minimal-order Sun(6) counterexample". Repair m3 therefore inserts after LF32:

> **Discharge conditions.** H5/H6 are used at their literal statements: every finite group (no minimal-order restriction); subgroups possibly equal (possible only when r_i = r_j = 1); every cofactor, including E2 with any 2-power and E3. C5W must not use Sun(5), S5W, Sun(6) or S6W, including inside subgroups. C56W must not use Sun(6) or S6W. Any use of Sun(5)/S5W by C56W is non-circular but must be added to the DAG, contradicting LF156 as written. If a gate accepts only a minimal-order-restricted form, S5W/S6W still follow by an explicit minimal-counterexample frame: R1 and R1(6) hold group by group, proper subgroups satisfy Sun(k) by minimality, and S6W uses the C1 route for p = 2, 3. In that case the "no minimal-order frame" notes at LF120 and LF141 must be withdrawn.

## 5. Conditional composition versus accepted result

- **Supported here:** the two implications H5 ⇒ S5W and H5 ∧ H6 ⇒ S6W, given Zhu.
- **Not supported here:**
  - H5 and H6 themselves; the C5W and C56W gates remain open.
  - Unconditional written versions of S5W and S6W.
  - Acceptance of S56W itself.
  - Closure of the full-result computation gate for its Sun5/Sun6 components, which stay UNMET. The Sun6 component also needs C5W.
- **Substitution protocol.** It permits only the identical theorem statement (items 1 and 4) and expressly excludes old internal lemmas, certificates, N2/FH2 and RPLP duals (item 4). Historical records stay computer-assisted and unchanged (item 3). With m4–m6 applied it is sound and not overstated.
