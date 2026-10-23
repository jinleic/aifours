# Information-science replacement screen after the six CDF cases

Read-only scout InfoNextScreen; preserved verbatim. Its suggested proofs, arithmetic and search estimates are untrusted until parent verification.

# info-2 replacement screen: optimal cyclic (v,5,1) and (v,6,1) codes (CPCW codes / optical orthogonal codes)

## Summary
- **Eight of the nine listed cases are still open; (126,6,1) is not.** I checked every later source I could reach: the MEM 2026 paper, Axioms 15(9):679, Axioms 15(10):762, both authors' ORCID records, the OpenAlex citing works, the authors' data page, arXiv, the EulerSolve listing and the local openai/math clone. None constructs or rules out any of the eight.
- **(126,6,1) already exists in earlier work.** Hetman's arXiv:2401.08274v5 (Example 3.2) and Hetman–Baicheva–Topalova, JACODESMATH 13(1) (2026), Table 1, give 64 cyclic (126,6,1) difference families. Drop the short block {0,21,42,63,84,105} from any of them and the 4 full blocks are an optimal code.
  - I checked the first family by hand: {0,26,38,56,81,103}, {0,40,48,68,99,102}, {0,41,57,93,94,107}, {0,80,82,87,91,97}.
  - Each difference class in {1..62} except 21 and 42 occurs exactly once, so the uncovered set is {21,42,63,84,105}. This is a hand check, not a machine check.
- **121 and 125 for k=6 are not open.** For 121, [25] classifies 48 cyclic difference families. For 125, Table A2 prints an explicit code. In the text extraction, the "?" after 121 and after 125 belongs to the dropped ranges 122–124 and 126.
- **(163,5,1) may also be open.** The extracted Tables 1 and 3 drop a "?" range between 161 and 164, which can only be "162–163?". But the text list omits 163, and so does the paper's count of "9 … parameter sets". I could not confirm this visually (see access holes).
- **No known nonexistence theorem applies to any target.** For the two cases of the form k(k−1)t+2, the type equations below are satisfiable. Axioms 15(9):679 adds deeper conditions only when 4 divides v, so they do not reach 122 or 162.

## Sources quoted in the table
- **Q1** — Baicheva–Topalova, Axioms 15(1):35 (1 Jan 2026), p. 5 §3.1, https://mdpi-res.com/d_attachment/axioms/axioms-15-00035/article_deploy/axioms-15-00035.pdf: "we have not found examples of optimal (v, 5, 1) CPCW codes for v = 143, 144, 146, 162, and 167 … the question of the existence of such codes remains open."
- **Q2** — same page: "…and of optimal (v, 6, 1) CPCW codes for v = 122, 123, 124, and 126." Also p. 4: "We cannot find an optimal code for 9 of the considered parameter sets. We notice that two of these gaps are for v = k(k − 1)t + 2."
- **Q3** — Baicheva–Yoveva–Topalova, Axioms 15(9):679 (11 Sep 2026), p. 16 §6: "…research on optimal (k(k − 1)s + 2, k, 1) CPCW codes whose existence remains undecided."
- **Q4** — Topalova–Zhelezova, Axioms 15(10):762 (13 Oct 2026), p. 11 §7: "v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1) designs has not yet been determined."
- **Q5** — arXiv:2408.15611v3 abstract; Math. Comp. 95 (2026) 1517–1539: "The smallest length for which the existence of periodic Golay pairs is undecided is now 106."

**Notation.**
- **s** is the optimal number of codewords, ⌊(v−1)/(k(k−1))⌋.
- The **leave** is the set of nonzero differences no codeword covers. For even v, v/2 is always in the leave (Lemma 1).
- **Type of a codeword** is min(#even, #odd) of its elements. a_i counts codewords of type i.
- **Later sources** is the same for every row: MEM 2026 covers only k=5 with v ≤ 123 and k=6 with v ≤ 120. Axioms 15(9):679 has necessary conditions only, its Table 1 has no k=5 rows, and for k=6 it lists only odd s. Axioms 15(10):762 is on a different topic. OpenAlex shows one citing work (15(9):679).
- **Certificate** for every row: s lines of k residues. A checker verifies that all s·k(k−1) ordered differences are distinct and nonzero and prints the leave. Cross-checks: binary auto/cross-correlations are at most 1, and the cyclic development is a packing.
- **Solution estimates** are my crude random-difference model, marked [INFERENCE] throughout.
  - It matched (82,5,1) and (122,5,1), which exist.
  - It matched (62,6,1), which does not exist.
  - It predicted 75 solutions for (65,6,1), which does not exist, and 13.9 for (92,6,1), which is ruled out by a 2-adic argument.
  - So k=6 values of roughly 10² or less are unreliable.

## Ranked table

| # | Target | Exact object (s; leave) | Quote | Nonexistence theorems | Search size [INFERENCE] | Risks |
|---|---|---|---|---|---|---|
| 1 | (162,5,1) | s=8; leave exactly {81}. Equivalent to an RDF in Z₁₆₂ relative to {0,81} (Buratti–Stinson §5.2, "2-regular OOC"). Equivalent to an (81,5,2) difference family in Z₈₁ plus Z₂ labels solving 40 GF(2) equations | Q1, Q2-p4, Q3 | Buratti–Stinson Thm 4.3: S={40}, representable. Published Thm 4.6 excludes only v≡22 (mod 40); 162≡2. 15(1):35 Thm 1 gives (a0,a1,a2) ∈ {(0,4,4),(1,1,6)}. 15(9):679 Thm 2 needs 4∣v, so n/a | about 2.6e6 candidate blocks; 80 columns × 8 rows; model ≈10¹⁵ labelled solutions (≈10¹⁴ after parity) | Nonexistence risk low. No nontrivial multiplier is possible (my derivation), so plain search or the Z₂-lift. Scoop risk: the Sofia group |
| 2 | (122,6,1) | s=4; leave exactly {61}. Equivalent to an RDF in Z₁₂₂ relative to {0,61}. Equivalent to a (61,6,2) difference family in Z₆₁ plus Z₂ labels solving 30 GF(2) equations in about 20 unknowns | Q2, Q2-p4, Q3 | Thm 4.3: S={30}=5+8+8+9, the only representation. Thm 1 gives the unique solution (a0..a3)=(0,1,2,1). Published Thms 4.12 and 4.13 cover only s=2,3 | about 3.9e6 candidate blocks; 60 columns × 4 rows; model ≈5e2 after parity, which is in the unreliable zone | **Highest nonexistence risk**: 32, 62 and 92 (the earlier k=6 cases of this form) all fail. No multiplier of order 2, 3 or 5 is possible (my derivation). Exhaustive search through the (61,6,2) families looks feasible but is untimed |
| 3 | (143,5,1) | s=7; leave {±d}, any d | Q1 | None (odd v). My subgroup counts mod 11 and 13 are feasible | about 1.7e6 blocks; 70 of 71 classes; ≈10¹⁴ | Low. Multipliers not analysed |
| 4 | (144,5,1) | s=7; leave {72,±d}, with d forced even by Thm 4.3; (a0,a1,a2) ∈ {(1,0,6),(0,3,4)} | Q1 | Thm 4.3: S={36,35}; 36 is representable | about 1.5e6 blocks; ≈10¹³ | Low. The multi-level 2-adic check of 15(9):679 has not been extended to this leave |
| 5 | (146,5,1) | s=7; leave {73,±d1,±d2}, with an even number of the pairs odd | Q1 | Thm 4.3: S={36,35,34}; satisfiable | about 1.6e6 blocks; ≈10¹⁵ | Low |
| 6 | (167,5,1) | s=8; leave {±d1,±d2,±d3}. v is prime and no multiplier is possible | Q1 | None | about 3.5e6 blocks; ≈10²⁰ | Low |
| 7 | (124,6,1) | s=4; leave {62,±d}. Parity types {5,8,8,9} if d is odd, {5,8,9,9} if d is even. Natural structure: d=31 gives an RDF over the order-4 subgroup, i.e. a (31,6,4) family in Z₃₁ (e.g. multiplier images of the Singer set) plus Z₄ labels | Q2 | Thm 4.3: S={31,30}; satisfiable. My mod-4 count is also feasible | about 4.3e6 blocks; ≈10⁴–10⁵ | Low to moderate |
| 8 | (123,6,1) | s=4; leave {±d}. Natural structure: d=41 gives Z₃×Z₄₁, a (41,6,3) family plus Z₃ labels | Q2 | None (odd v) | about 5.3e6 blocks; ≈2e5 | Low to moderate |
| 9 | (163,5,1) | s=8; leave {±d}. Prime, no multipliers | Tables 1/3 only, inferred from the extraction; not in the text | None | about 3.1e6 blocks; ≈10¹⁷ | Open status ambiguous: either the text omitted it or the table has a typo |
| — | (126,6,1) | **Not a target: already exists** (see Summary). The leave in Hetman's family is {21,42,63,84,105} | Q2, but superseded | — | 0 | Record only; no novelty |

**Why the two headline cases reduce to labelling problems.** v/2 is odd in both, so Z_v ≅ Z₂×Z_{v/2}.
- Reducing the blocks mod v/2 must give a (v/2,k,2) difference family.
- Choosing which half each element lifts to is a GF(2) linear system. For each class y, the two occurrences of y must lift to different halves.
- Calibration controls:
  - Positive: the published (122,5,1) code in Table A1 (same form, t=6). I checked its types by hand; they give (0,3,3), which matches Thm 1.
  - Positive: (82,5,1).
  - Negative: (62,6,1), which Buratti–Stinson proved does not exist. Any exhaustive mode must return nothing for it.

## Recommended set for the next 2 hours
1. **First 15 minutes:** write an OOC verifier straight from the definition. Positive controls: the Table A1 (122,5,1) code, the Table A2 (125,6,1) code, and Hetman's 4 full (126,6,1) blocks. Add the usual negative mutations.
2. **Headline runs, 2 CPU, about 75 minutes:** (162,5,1) and (122,6,1), using both the Z₂-lift and direct randomized exact cover. Only if randomized search misses for 122 should exhaustive enumeration of (61,6,2) families start, and only after the (62,6,1) negative control passes.
3. **Sweep, 2 CPU, 10–15 minutes each:** 143, 144, 146 and 167 for k=5; 123 and 124 for k=6. Add 163 only after someone looks at Table 3 in the PDF, and label it "table-only".
4. **Exclude:** 126 (earlier work), and 121 and 125 (not open).
5. **Before any novelty wording:** a priority audit covering the access holes below.

## Alternatives (two, ranked)
- **A. Cyclically resolvable 2-(88,4,1) design.** Q4 calls it open as of 13 Oct 2026, but my short argument says none exists, so this is a proof-and-review task, not a search. [INFERENCE: my derivation, not reviewed.]
  1. Suppose a parallel class contains m short blocks with 1 ≤ m ≤ 21. Its stabilizer H acts freely on its 22−m full blocks, its orbit length 88/|H| is at most 29, and that orbit holds 88m/|H| ≤ 22 short blocks. Checking |H| = 4, 8, 11, 22, 44 gives no solution. So the short orbit is a single class (type T1), which agrees with the paper.
  2. Every other class has |H| dividing 22 and orbit length at most 28, so H is 8Z₈₈ or 4Z₈₈. Each class is a union of H-orbits whose representatives form a transversal of Z₈₈/H, so no block in it has a difference in 8Z₈₈.
  3. The short blocks give only the differences 22, 44 and 66.
  4. So the pair {0,8} lies in no block, which contradicts the design property.
  - Next step: hostile review plus a prior-art check of Genma–Mishima–Jimbo 1997, Lam–Miao 1999 and Mishima–Jimbo 2000. The certificate would be about a one-page proof.
- **B. Periodic Golay pair of length 106 (Q5).** The object is two ±1 sequences of length 106 whose periodic autocorrelations sum to 0. The certificate is the two sequences; as a cross-check, build the Hadamard matrix of order 212 with two circulant cores. The odds in 2 hours are low: 106 = 2·53 compresses poorly, and the paper's exhaustive searches reached only v ≤ 72 using under 10 CPU-years. Bright and Kotsireas are active on it, and it is Hadamard-adjacent. Not recommended for this cycle.

## Access holes
1. **Visual check of Tables 1–4 of Axioms 15(1):35.** The PDF text extraction drops every range marked "?", so the reading of 163 is inferred. The MDPI HTML returned 403 and a reader proxy returned 401.
2. **CDF archive members.** I could list `CDF31-126_6_1.rar` (it contains `6-126.txt`, 8.3 KB) but could not extract members from the URL. I used Hetman's Example 3.2 instead.
3. **Constructions not read** (the main priority risk, especially for 122 = 2·61 via cyclotomic relative difference families):
   - the Handbook of Combinatorial Designs, 2nd ed. (difference family and packing tables);
   - Momihara, FFA 2010/11;
   - Fuji-Hara–Miao 2000;
   - Yin 1998;
   - Chang–Miao 2003;
   - Wang–Wang–Wang 2015.
4. **Unopened supplements and closed indexes.** I did not open the 15(9):679 supplement (C++ source and solutions). Crossref's cited-by service needs membership and I did not use Google Scholar.
5. **Theorem numbering.** I read Buratti–Stinson arXiv v1, where published Thms 4.6 and 4.13 appear as Thms 4.5 and 4.10. I took the published statements from 15(9):679 §1.3.

## Files read
- Local: `institute/runs/six-lane-2026-10-16/transitions.json`, `screening/finite-info-target-screen.md`, `screening/fresh-information-screen-final.md`, `information-science/evidence/six-lane-20261016/cdf-k5/README.md`.
- Remote, read in full: the three Axioms PDFs, the MEM PDF, the JACODESMATH PDF, Hetman arXiv:2401.08274v5, Buratti–Stinson arXiv:2007.01908v1 (Sections 1–5).
- Remote, metadata: the tsonka data pages, both ORCID works APIs, OpenAlex, the EulerSolve listing.
