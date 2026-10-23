# Optimal CPCW eight-case bounded priority audit (read-only scout CpcwPriority, 2026-10-17 PT)

Preserved verbatim. A search miss is not novelty.

## Summary

**Correctness:** I did not re-check this. The parent check JSONs record the uncovered differences and `exact_developed_leave_matches: true` for all eight witnesses.

**Novelty:** I found no earlier construction, and no theorem that implies one, for any of the eight cases. This was a bounded search, so a miss does not prove novelty.
- The most recent source that names the eight as open is Baicheva–Topalova, Axioms 15(1):35, §3.1, p.5 (published 1 Jan 2026).
- Later work by the same group does not update that list. MEM 2026 (19 May 2026) stops at v ≤ 123 for k=5 and v ≤ 121 for k=6. Axioms 15(9):679 (11 Sep 2026) only handles lengths divisible by 4, and only says in general terms that existence "remains undecided".
- OpenAlex lists one work citing 15(1):35, and that work is 15(9):679. Nothing cites 15(9):679 yet.

**Calibration (the 2026 open list is not a novelty certificate):**
- **126:** 15(1):35 lists it as open. Its own reference [25] (Hetman–Baicheva–Topalova, JACODESMATH 13(1)) tabulates 64 cyclic (126,6,1) difference families. Hetman's arXiv:2401.08274v1 (16 Jan 2024) already listed them, with the short block {0,21,42,63,84,105} written out separately. Dropping that block leaves 4 full blocks, which form an optimal code.
- **125** (not a target): 15(1):35 marks it as new (bold). Hetman–Banakh–Ravsky, arXiv:2504.18390 (24 Apr 2025), gives 8 Steiner systems S(2,6,126) built over the cyclic group Z₁₂₅ with one fixed point. Removing the fixed point gives optimal (125,6,1) codes whose uncovered differences are {25,50,75,100}. This follows from the standard correspondence; I did not recompute their families.

**Which construction routes could apply at all:**
- Only 144 could come from a Steiner system: S(2,5,145) built over Z₁₄₄ with one fixed point. None found.
- 122, 123, 124, 144 and 162 could come from a "regular" code, where the uncovered differences form a subgroup (a relative difference family, RDF). 143, 146 and 167 have no such route.
- The RDF theorems I found all fail at these parameters. They need q prime, and for k=6 they only cover subgroup sizes h ∈ {5, 15, 25, 30, 35, 45}, never 2, 3 or 4. For 162 = 2·81, 81 is not prime. A version built on the field F₈₁ lives on Z₂ × Z₃⁴, which is not cyclic, so it is not equivalent.

**163:** the source contradicts itself. By its own Table 3 and Appendix Table A1, 163 is a tenth unresolved length. The text's list and its count of 9 leave it out. I did not add it to the frozen claim.

**Significance:** modest. These are finite instances that fill gaps named in one 2026 paper.
- 122 is the most notable. The smaller lengths of the same form 30t+2 (32, 62 and 92) are proven nonexistent.
- The k=5 witnesses took 0.02–1.30 s of tabu search, which suggests the paper's gaps came from its search method rather than real hardness [INFERENCE].

## Files

**Local evidence used (read-only):**
- `information-science/evidence/six-lane-20261016/cpcw-optimal-prep/sources/axioms-15-00035.pdf`: §1.2 known results (pp.3–4), §3.1, Tables 1–4 (p.5), Tables A1–A2 (pp.11–14).
- `information-science/evidence/six-lane-20261016/cpcw-optimal/sources/axioms-15-00679.layout.txt`:
  - §1.3 at :160-200
  - Table 1 scope at :680-684
  - §6 at :975-985
- `information-science/evidence/six-lane-20261016/cpcw-optimal/notes/table3-163/{table1,table3,table4}_crop.png`: visual crops of the tables, used for the 163 check.
- `information-science/evidence/six-lane-20261016/cpcw-optimal/README.md` §3: tabu timings, and the leave {8,44} of the paper's own (125,6,1) code.
- `institute/runs/six-lane-2026-10-16/review/cpcw{122,123,124,143,144,146,162,167}-parent-check-v1.json`: uncovered differences of each witness.
- `institute/runs/six-lane-2026-10-16/screening/info2-post-cdf-screen.md`: the earlier screen. It could not confirm 163 visually.

## How the sources connect

- 15(1):35 is the only per-parameter open list.
- 15(9):679 and MEM 2026 are the later papers by the same authors, and neither reaches the eight.
- Each optimal code corresponds to equivalent objects:
  - an optimal optical orthogonal code (the Johnson bound gives the same s here);
  - a cyclic difference packing;
  - a strictly cyclic partial 2-design;
  - a cyclic group-divisible design, when the code is regular (122, 123, 162 for these witnesses);
  - a 1-rotational Steiner system (144 only).
- The theorems for these related objects were checked against the exact parameters below.

## Report

### A. Per-parameter applicability table
Quote IDs (S…) refer to section B.

| Case: witness leave and structure | Latest explicit open statement | Earlier construction or theorem | Exact restrictions checked, and why each fails | Access holes (beyond the global list in E) | Significance |
|---|---|---|---|---|---|
| **122, k=6, s=4**: leave {61}, a 2-regular (122,2,6,1)-RDF (cyclic 6-GDD of type 2⁶¹) | S1a, p.5. Generic only: S2a, p.16 | None found | Doubling route is dead because (61,6,1) is the one exception to the (q,6,1) family theorem (S1h). Wang–Wang–Wang needs 15 or 20 dividing v (S1g). S8 for k=6 needs h ∈ {5,15,25,30,35,45} with q prime. S11 has no integer q at e=4. No Steiner route (122 and 123 are not ≡ 1, 6 mod 15). Nonexistence: S9 Cor 4.6 is for odd k; Theorems 4.12–4.13 cover s=2,3 only; S2c needs 4 \| v | Full texts on cyclotomic RDFs over Z₂×F_q for k=6 (Momihara 2009; Buratti 1998/1999; Costa–Feng–Wang 2018) | Highest of the eight. 32, 62, 92 are proven nonexistent (S9 p.6, p.21; S1l), and S1k expected nonexistence. Still one finite instance |
| **123, k=6, s=4**: leave {41,82}, a 3-regular (123,3,6,1)-RDF (6-GDD of type 3⁴¹) | S1a. Generic: S2b | None found | Not a perfect or short-block length (123 is not ≡ 1 or 6 mod 30). 41 is not ≡ 1 mod 30. S8 has no h=3. S1g fails. No Steiner route. No nonexistence theorem applies (v odd) | Same k=6 RDF hole | Low to moderate |
| **124, k=6, s=4**: leave {19,62,105}, not regular. The regular version would be a (124,4,6,1)-RDF with leave {31,62,93} | S1a | None found | The (31,6,1) Singer difference set exists, but lifting it to Z₄ needs a (4,6,1) difference matrix over Z₄, which cannot exist [INFERENCE: Z₄ has no complete mapping]. S8 has no h=4. S1g fails. No Steiner route. Not of the form 30s+2, so no nonexistence theorem applies | Same | Low |
| **143 = 11·13, k=5, s=7**: leave {39,104}. No regular route (no divisor g of 143 has 20 \| 143−g) | S1a | None found | Every family in C needs 4, 5, 10, 12 or 20 dividing v, or v = 2q with q prime ≡ 1 mod 20. Perfect and short-block routes need v ≡ 1 or 5 mod 20. Products would need a (13,5,1) or (11,5,1) difference family, which do not exist [INFERENCE]. No Steiner route | Global only | Low (tabu found it in 0.03 s) |
| **144, k=5, s=7**: leave {30,72,114}, not regular. The regular version is a (144,4,5,1)-RDF, which is the same as a 1-rotational S(2,5,145) over Z₁₄₄ | S1a | None found | Chang–Ji (S1f) needs 144/4, 144/8 or 144/12 to be prime; these are 36, 18, 12. The k=5 1-rotational enumeration only covers v ∈ {25,65,85,101} (S7, plus the GitHub `1rot` files). No nonexistence theorem applies (144 is not 20t+2) | Handbook VI.16 1-rotational tables; Buratti's 1-rotational papers | Low |
| **146 = 2·73, k=5, s=7**: leave {11,17,73,129,135}. A 2-regular code is impossible because 20 does not divide 144 | S1a | None found | S8's (2q,5,1) needs q prime ≡ 1 mod 20, but 73 ≡ 13. A (73,5,1) difference family does not exist. Other families fail as for 143. No Steiner route | Global | Low |
| **162 = 2·3⁴, k=5, s=8**: leave {81}, a 2-regular (162,2,5,1)-RDF (5-GDD of type 2⁸¹) | S1a. Generic: S2a | None found | S8 Thm 8(1) needs q prime, and 81 is composite. The F₈₁ version is on Z₂×Z₃⁴, not cyclic, so not equivalent. Product constructions would need a factor 3 < k [INFERENCE]. S9 Cor 4.6 excludes only v ≡ 22 mod 40, and 162 ≡ 2. S1 Cor 1 needs t even, and t=8. S2c needs 4 \| v, and 162 ≡ 2 mod 4 | Galois-ring constructions over Z₈₁ not checked | Low to moderate (82 and 122 of the same 20t+2 form already exist) |
| **167, prime ≡ 7 mod 20, k=5, s=8**: leave {24,25,79,88,142,143}. No regular route | S1a | None found | (q,5,1) difference family theorems need q ≡ 1 mod 20. The families for composite lengths do not apply. No Steiner route | Global | Low |
| *Calibration:* **126, k=6** (excluded) | S1a lists it as open | **Found:** S5 (2024-01-16) and S4 (accepted 2025-09-20). Dropping {0,21,42,63,84,105} leaves an optimal code | Short-block route: 126 ≡ 6 mod 30 | — | Not new; the open list is wrong here |
| *Calibration:* **125, k=6** (not a target) | 15(1):35 Table 4 marks it bold (new) | **Found:** S6 (2025-04-24), 8 systems over Z₁₂₅ | 1-rotational route: 125 ≡ 5 mod 30 | Families not recomputed | The "new" label is wrong here |

### B. Quote register (each quote ≤ 40 words)

**S1. Baicheva–Topalova, Axioms 15(1):35.** https://doi.org/10.3390/axioms15010035 (PDF: https://www.mdpi.com/2075-1680/15/1/35/pdf)
- **S1a, p.5:** "In particular, we have not found examples of optimal (v, 5, 1) CPCW codes for v = 143, 144, 146, 162, and 167, and of optimal (v, 6, 1) CPCW codes for v = 122, 123, 124, and 126."
- **S1b, p.5:** "The question marks mean that we could not find optimal codes for these values of v and the question of the existence of such codes remains open."
- **S1c, p.4:** "We cannot find an optimal code for 9 of the considered parameter sets. We notice that two of these gaps are for v = k(k − 1)t + 2."
- **S1d, p.4:** "The fact that we have not succeeded to construct a code with definite parameters does not mean that such a code does not exist."
- **S1e, p.6:** "Tables A1 and A2 in Appendix A contain all the examples of new optimal (v, 5, 1) and (v, 6, 1) CPCW codes."
- **S1f, p.3:** "…an optimal (4p, 5, 1) OOC exists for prime p ≡ 1 (mod 10), and that there is an optimal (4up, 5, 1) OOC for u = 2, 3 and prime p ≡ 11 (mod 20)."
- **S1g, p.3:** "A class of optimal (gv, 6, 1) optical orthogonal codes with v a product of primes congruent to 7 modulo 12 and greater than 7 and g = 15, 20, 105, 140 is obtained in [19]."
- **S1h, p.4:** "Existence of a (q, 6, 1) cyclic difference family for any prime power q ≡ 1 (mod 30) with the exception of q = 61 is shown in [22]."
- **S1i, p.3:** "There are also several direct constructions for optimal (gv, 5, 1) OOCs where 60 ≤ g ≤ 180, g ≡ 0 (mod 20), and v is a product of primes greater than 5."
- **S1j, p.4:** "Nonexistence results for optimal (v, 5, 1) OOCs with v ≡ 22 (mod 40) and for an optimal (62, 6, 1) OOC are presented in [7]."
- **S1k, p.11:** "The results for small parameters show that nonexistence of some optimal (k(k − 1)t + c, k, 1) CPCW codes with small c can be expected."
- **S1l, p.10:** "An optimal (92, 6, 1) CPCW code does not exist."

**S2. Baicheva–Yoveva–Topalova, Axioms 15(9):679.** https://doi.org/10.3390/axioms15090679
- **S2a, p.16:** "…can be helpful in further theoretical or computer-aided research on optimal (k (k − 1)s + 2, k, 1) CPCW codes whose existence remains undecided."
- **S2b, p.3:** "A summary about (v, 5, 1) and (v, 6, 1) CPCW codes is given in [2]."
- **S2c, p.11:** "It contains only the results for values of v which are divisible by 4, namely k(k − 1)s + 2 = 4u."

**S3. MEM 55 (2026) 329–339, p.4 of the PDF (journal p.332).** https://doi.org/10.55630/mem.2026.55.329-339
- "…optimal (v, k, 1) OOCs with k = 3, 5, and 6 and 63 ≤ v ≤ 200, 90 ≤ v ≤ 123, and 106 ≤ v ≤ 121 respectively."

**S4. JACODESMATH 13(1) 111–119.** https://doi.org/10.13069/jacodesmath.v13i1.389
- p.1: "Received: 14 May 2025 … Accepted: 20 September 2025".
- p.7, Table 1 ("Number of multipliers of (v, k, 1) CDFs"): row "126 6 … 64".

**S5. Hetman, arXiv:2401.08274v1, p.2.** https://arxiv.org/abs/2401.08274v1
- "Example 3.2. List of 8 difference families (126, 6, 1). … yielding 64 non-isomorphic difference families. Last block {0, 21, 42, 63, 84, 105} is omitted."

**S6. Hetman–Banakh–Ravsky, arXiv:2504.18390v1, p.2.** https://arxiv.org/abs/2504.18390
- Table row: "SmallGroup(125,1) | Z₁₂₅ | 8".
- Example 2.1: "[[0, 1, 3, 15, 47, 74], [0, 4, 9, 20, 65, 103], [0, 6, 40, 88, 95, 112], [0, 8, 18, 41, 76, 104], [0, 25, 50, 75, 100, ∞]]".

**S7. arXiv:2505.00469v1, p.4.** https://arxiv.org/abs/2505.00469
- "In this section we enumerate 1-rotational designs S(2, k, v) with k = 5 and v ∈ {25, 85, 101}, generated by actions of groups of order 24, 84 and 100."

**S8. Chang–Costa–Feng–Wang, Discrete Math. 343 (2020) 111776.** https://arxiv.org/abs/1901.06837
- p.12, Thm 8(1): "There exist an optimal (2q, 5, 1)-OOC and an optimal (12q, 5, 1)-OOC for any prime q ≡ 1 (mod 20)."
- p.13, Thm 8(2)–(3): "(g, k) ∈ {(10, 5), (5, 6), (15, 6), (21, 7)} for any prime q ≡ 1 (mod 12)" and "{(25, 6), (30, 6), (35, 6), (45, 6), (35, 7), (49, 7)} for any prime q ≡ 1 (mod 6)".

**S9. Buratti–Stinson, arXiv:2007.01908v2.** https://arxiv.org/abs/2007.01908
- p.6, Table 1: "32 ≤ v ≤ 34 | 6 | does not exist".
- p.21: "an optimal (v, 5, 1)-OOC does not exist if v ≡ 22 mod 40"; "…we conclude that an optimal (62, 6, 1)-OOC does not exist."
- p.27: "When G = Z_v and the order of the subgroup H is equal to w, a (G, H, k, 1)-RDF is clearly a (v, k, 1)-OOC whose leave is the subgroup of Z_v of order w."

**S10. Ma–Chang, JCD 13 (2005).** zbMATH summary, https://zbmath.org/1056.05027
- "optimal (gv, 5, 1) optical orthogonal codes (OOCs) where 60 ≤ g ≤ 180 satisfying g ≡ 0 (mod 20) and v is a product of primes greater than 5."

**S11. Momihara, FFA 17 (2011).** zbMATH summary, https://zbmath.org/1222.05012
- "an optimal ((q²−1)/e, ⌈(q−(e−1)√q)/e⌉, 1)-OOC with e codewords; … ((q²+q+1)/e, ⌈(q+1−(e−1)√q)/e⌉, 1)-OOC with e codewords".

**S12. Buratti, Art Discrete Appl. Math. 1 (2018).** zbMATH summary, https://zbmath.org/1422.94049
- "the literature almost completely lacks optimal (v, k, 1)-OOCs with k > 3 which are not regular … (3p, 4, 1)-, (5p, 5, 1)-, and (2p, 4, 1)-OOCs".

**S13. Chang–Costa–Feng–Wang, JCD 28 (2020), p.15.** https://arxiv.org/abs/1911.07189
- "a (5v, 5, 1)-OOC with J(5v, 5, 1) = ⌊(v − 1)/4⌋ codewords whenever gcd(v, 10) = 1."

**S14. Chee, arXiv:2610.10973 (7 Oct 2026), abstract.** https://arxiv.org/abs/2610.10973
- "the Johnson bound is asymptotically attained at all lengths by optical orthogonal codes … with w ≥ λ+2". This is an asymptotic result and settles no finite length.

### C. Theorem families checked against all eight

| Family | Exact restriction | Targets it reaches |
|---|---|---|
| Perfect or short-block cyclic difference families (Chen–Zhu, Abel et al., Buratti–Pasotti pq, Hanani 5p, S4, S5) | v ≡ 1 or k (mod k(k−1)) | None (k=5 targets ≡ 3, 4, 6, 2, 7 mod 20; k=6 targets ≡ 2, 3, 4 mod 30) |
| Chang–Ji (S1f) | v = 4p with p prime ≡ 1 mod 10; or 8p, 12p with p prime ≡ 11 mod 20 | None |
| Tang–Yin; Ma–Chang 3ˢ·5·v; Buratti 2018 (S12); S13 | 5 divides v | None |
| Ma–Chang 2005 (S10, S1i) | 20 divides v | None |
| Wang–Wang–Wang 2015 (S1g) | 15 or 20 divides v | None |
| Chang et al. 2020 (S8) | Listed hq forms, q prime | None (81 composite; 73 ≢ 1 mod 20; h ∉ {2,3,4}) |
| Momihara 2011 (S11) | (q²−1)/e or (q²+q+1)/e | None (no integer q at e = 4, 7, 8) |
| Yin–Yang–Li 2011 | v = 20p | None |
| 1-rotational over Z_v (S6, S7) | v ≡ k−1 (mod k(k−1)) | 144 only; no example found |
| Nonexistence results (S9, S1 Cor 1 and Prop 1, S2) | v ≡ 22 mod 40; s = 2, 3; t even; 4 \| v | None of the eight is excluded |
| Asymptotic (S14) | (1−o(1)) of the bound | No finite implication |

**Not equivalent, so not counted:**
- non-cyclic packings;
- Z₂×F₈₁ RDFs;
- (v,6,2,1)-OOCs, i.e. auto-correlation 2 allowed (Baicheva–Topalova 2023, not read);
- constant-weight codes A(n,d,w) (arXiv:2603.00174, 2608.13906; lengths n ≤ 35-ish);
- integer Golomb-ruler packings (arXiv:2608.13739).

### D. Is 163 a real extra case?

- **Table 3 (p.5).** Read visually from `table3_crop.png`, row 4 is `145 | ? | 147–160 | 161 | ? | 164 | 165 | 166 | ? | 168–180 | 181`. Table 1 shows the same `161 | ? | 164`. Every integer from 41 to 181 appears in some cell, so that "?" cell covers both 162 and 163.
- **Other "?" cells agree with the text.** They are 143–144, 146, 167, and for k=6 (from `table4_crop.png`) 122–124 and 126.
- **Appendix.** Table A1 jumps from 160 to 166, so no 163 code is printed, even though S1e says the appendix contains all new codes.
- **Text.** The list in S1a omits 163, and S1c says "9" sets.
- **Verdict.** This is an internal inconsistency in the source, not an extension of our claim.
  - By the paper's own Table 3 and Table A1, 163 is a tenth unresolved length.
  - The text list and count are the more likely error. The other reading would need two separate omissions: a missing bold cell and a missing appendix row.
  - No later source resolves it: MEM 2026 stops at k=5, v ≤ 123, and 15(9):679 has no k=5 rows.
  - I found no theorem covering 163 (prime ≡ 3 mod 20, s=8, uncovered differences {±d}).
  - The frozen eight are unchanged, and I did not evaluate any 163 witness.

### E. Global access holes and what was actually checked

**Not read in full (only abstracts or zbMATH/Springer summaries):** Momihara DCC 51 (2009); Buratti JCD 6 (1998) and JCD 7 (1999); Buratti–Gionfriddo (2008); Buratti–Pasotti FFA (2009) and DCC (2010); Yin DM 185 (1998) and JCTA 97 (2002); Chang–Miao DM 261 (2003); Chu–Golomb (2003); Fuji-Hara–Miao (2000); Bitan–Etzion (1995); Moreno et al. (1995); Costa–Feng–Wang FFA (2018). The Wang–Wang–Wang 2015 statement is taken second-hand from S1g.

**Not accessed at all:** the Handbook of Combinatorial Designs, 2nd ed. (VI.16 and the packing/OOC chapters).

**Citation and other searches:**
- OpenAlex was queried.
- Google Scholar and Crossref cited-by were not used, and the Semantic Scholar lookup failed with a tool error.
- Chinese-language journals and theses were not searched.

**Author archives:**
- The MEM archives `(v,5,1)OOC.rar` (37.6 MB) and `(v,6,1)OOC.rar` (49.3 MB) could not be listed, because members exceed the tool's 64 MB limit. I relied on the length ranges stated in S3.
- The 15(9):679 supplement was not opened (it only covers lengths divisible by 4).
- The authors' OOC page lists only λ = 2, 3 codes and (v,4,1) codes; it has no (v,5,1) or (v,6,1) data. Their CDF page covers difference families only.

**Hetman's 13 arXiv papers were screened.** None reaches the eight, apart from the 125 and 126 calibration items:
- For k=6, S(2,6,v) needs v ≡ 1 or 6 mod 15, which rules out 122–124 in either the plain or the 1-rotational form.
- arXiv:2511.20708 is about block size k ≥ 7.

**Nothing was changed:** no files were written, no tests or computations were run, and no further delegation was made.
