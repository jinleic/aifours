# CFR(6,21) pre-freeze priority and viability screen

Parent capture: 2026-10-17T18:58:24-07:00. The read-only scout Cfr21Screen report below is preserved verbatim, followed by its coordinate-change correction. Verdict: OPEN-IN-SCOPE, not a proof of openness or novelty.

## Parent scope and source spot checks

- Parent directly read CPro1's CFR definition and OPEN_INSTANCES at commit 827f02b4048fc96a6b79f0970c87ca5a54f31f40; [6,21] is listed. The exact upstream source is already pinned in ../review/cfr27-cpro1-predicate-v1/upstream/problem_def.py (sha256 44f4d4ff86757bd221a4875a8e84d3d5195deb483dcde1119154bfc901bf70aa).
- Parent directly read Miller–Abel–Valkov–Fraser, *Implementing the MOLS Table for n Up to 500*, Symmetry 16 (2024), 1678, [accepted PDF](https://eprints.gla.ac.uk/343648/1/343648.pdf), Table 4: the n-list starts 6,10,15,20,21,22 and the corresponding lower bounds are 1,2,4,4,5,3. Its reference 67 is Nazarok, *Five pairwise orthogonal Latin squares of order 21* (1991). This is a published lower bound, not an upper bound or a direct reading of Nazarok.
- Parent directly read [Sage MOLS_handbook_data.py](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/combinat/designs/MOLS_handbook_data.py): index 21 is 5. It is a handbook table implementation, not a comprehensive recency guarantee.
- Parent directly read Evans, [A class of orthogonal latin square graphs](https://ajc.maths.uq.edu.au/pdf/57/ajc_v57_p189.pdf), AJC 57 (2013), Lemma 2 and Table 2: a clique of r normalized orthomorphisms gives r+1 MOLS; the Z_21 row gives 275,148,653,115 normalized orthomorphisms and omega(Z_21) >= 4.
- The parent independently checked the count bridge: a 7-row DM, after subtracting row0 and relabelling columns by row1, has rows 0,id,theta1,...,theta5. The arrays d_i(x)+y (i=1,...,6) are six MOLS, since d_i-d_j is bijective for every pair. Five theta maps also give five MODCLS. Under (i,j)=(y,x+y), the old x-coordinate becomes the sixth Latin square j-i; the old Cayley square becomes the column coordinate j. The scout corrected this in the addendum below.
- The scout's L2–L4 structural lemmas and its random-clique heuristic are **unreviewed leads only**. They are not used as a general nonexistence argument, and must not prune the unrestricted target or certify a symmetry family. In particular its broad row-cycle-type exclusions need their multiplier hypotheses checked separately.
- Priority limits remain: Nazarok 1991, the relevant Handbook bodies, Evans 2018 Ch.13, Wanless 2004 and Song 2000 were not read; no claim of priority or of an optimal N(21) bound. If a witness appears, repeat the post-result screen.

## Original scout report (verbatim)

**VERDICT: OPEN-IN-SCOPE.** I found no construction, and no nonexistence or upper-bound result, for CFR(6,21). In equivalent terms: no 7-row difference matrix over cyclic Z₂₁, no 5 mutually orthogonal orthomorphisms of Z₂₁ (ω(Z₂₁) ≥ 5), and no 5 MODCLS(21). The best published values are ω(Z₂₁) ≥ 4, F_c(21) ≥ 5 and N(21) ≥ 5, all coming from Nazarok (1991). Several sources could not be read; they are listed at the end and could still hold prior art. A search miss is not novelty.

## Count bridges, re-checked after your correction (my elementary proofs, unreviewed)
- **CFR ⇔ DM.** CPro1's definition: "at most one row in which b appears in the position which is m steps to the right of a". Write g_i(a) for the position of symbol a in row i. A violation means g_i(b)−g_i(a) = g_k(b)−g_k(a), so the CFR condition is that every g_i − g_k is a bijection. Adding a zero row then gives a 7-row DM over Z₂₁. Hence CFR(6,21) ⇔ 7-row DM, and in general F_c(n) = ω(Z_n) + 1.
- **DM ⇔ 5 orthomorphisms.** Make row 0 zero. Relabel columns so row 1 is the identity, i.e. θ_i = d_i∘d₁⁻¹. The other five rows are then orthomorphisms, and they are pairwise orthogonal because θ_i − θ_j = (d_i − d_j)∘d₁⁻¹ is a bijection.
- **5 orthomorphisms ⇔ 5 MODCLS, not 6.** Every diagonally cyclic Latin square has the form L(i,j) = i + θ(j−i). It is Latin exactly when θ is an orthomorphism, and two such squares are orthogonal exactly when θ−φ is a bijection. The identity map gives L(i,j) = j, which is not Latin.
- **The DM gives 6 MOLS.** Set L_i(x,y) = d_i(x) + y for i = 1..6; this is an OA(8,21). After the relabelling these six squares are the Cayley table x+y plus θ₁(x)+y, …, θ₅(x)+y. Under the cell map (i,j) = (y, x+y), the five θ-squares become the MODCLS. The Cayley table becomes j−i, which is Latin but not diagonally cyclic. That is why the count is 5 MODCLS but 6 MOLS.
- **Consistency check.** CPro1's dev list has [2,9] and [4,15] and no open instance at 9 or 15. That matches Evans's exact values ω(Z₉) = 1 and ω(Z₁₅) = 3.

## Evidence (all fetched 2026-10-17 PDT)
| # | Source | Quote (≤40 words) | Bearing |
|---|---|---|---|
| 1 | [CPro1 problem_def.py @827f02b4](https://raw.githubusercontent.com/Constructive-Codes/CPro1/827f02b4048fc96a6b79f0970c87ca5a54f31f40/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py) | "OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]"; DEV includes "[3,21],[4,21],[5,21]" | Target is listed open |
| 2 | [Sage develop database.py](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/combinat/designs/database.py), lines 3217–3250 and 4063; last commit to the file 1fd3a298 (2025-09-02) | "Return a `(21,6,1)`-difference matrix. As explained in the Handbook III.3.50"; "return AdditiveCyclic(21), Mb"; "(21 ,1) : (6 ,DM_21_6_1)," | Group Z₂₁, 6 rows. A zero column plus four base columns shifted cyclically over five coordinates (a ℤ₅ symmetry). No 7-row entry for 21 |
| 3 | [Sage MOLS_handbook_data.py](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/combinat/designs/MOLS_handbook_data.py) | "corresponding to Table 3.87 in the Handbook of Combinatorial Designs, 2nd edition"; row `4,5,3,22,…  # 20` | Index 21 = 5, so N(21) ≥ 5 in 2007 |
| 4 | [Dinitz, New Results in Part III](https://site.uvm.edu/jdinitz/index.php?rest_route=/wp/v2/pages/389) | "Last edited 9/17/2019" … "Page 176 Table 3.87. N(60) ≥ 5." | Updates are 14, 18, 60 and 7968; none for 21 |
| 5 | [Janiszczak–Staszewski, arXiv 1812.06886v3](https://arxiv.org/pdf/1812.06886v3) (5 Mar 2019; J. Combin. Des. 27, 2019) | "For n ∈ {20, 21, 56} there are separable (n, m)-PA … corresponding to 4, 5 and 7 MOLS"; for n = 21, "a conversion from a result of A.V. Nazarok" | Their search covered 10 ≤ n ≤ 100 and found improvements only for 35, 48, 63 and 96. Not exhaustive |
| 6 | [Abel–Janiszczak–Staszewski, arXiv 2412.00480v1](https://arxiv.org/abs/2412.00480) (30 Nov 2024; Des. Codes Cryptogr. 2025) | "we obtain improvements for N(n) when n ∈ {54, 96, 108}" | Not 21 |
| 7 | [Miller–Abel–Valkov–Fraser, Symmetry 16:1678](https://eprints.gla.ac.uk/343648/1/343648.pdf) (2024-12-18; accepted version, MDPI copy returned 403) | "In Table 4, we provide a source for the most up to date largest lower bound for N(n), for n ≤ 500"; row "…20, 21, 22… / …4, 5, 3…"; reference 67 is Nazarok | **N(21) ≥ 5 as of Dec 2024** |
| 8 | [Keita–Shapiro, arXiv 2601.22205v1](https://arxiv.org/pdf/2601.22205v1) (29 Jan 2026) | Table 2 row "21 \| 5 \| 21 \| [37]", where [37] is Nazarok | Only "representative examples": the same table still lists 18→3 and 35→5, so it is not a bounds table |
| 9 | [Evans, Australas. J. Combin. 57](https://ajc.maths.uq.edu.au/pdf/57/ajc_v57_p189.pdf) (revised 21 May 2013), Table 2 | "Z₂₁ \| 21 \| 275,148,653,115 \| ≥ 4"; "Z₁₅ \| 15 \| 2,424,195 \| 3"; "Lazebnik and Thomason [45] computed ω(G) for all abelian groups of order at most 16" | ω(Z₂₁) has only a lower bound; exact values are computed only up to order 16 |
| 10 | Same paper, Theorem 4 | "If p is the smallest prime divisor of \|G\| and the Sylow p-subgroup of G is cyclic, then any (p − 2)–clique of P(G) is a maximal set of orthomorphisms of G." | Basis of lemma L2 below |
| 11 | [Evans 2018, Ch. 13 "Groups of Small Order"](https://link.springer.com/chapter/10.1007/978-3-319-94430-2_13) | "We will summarize known values and bounds for \|Orth(G)\| and ω(G) when \|G\|≤ 23." | Body paywalled. Its reference list has Nazarok 1991 and nothing newer specific to 21, so the bound is probably still ≥ 4 [INFERENCE] |
| 12 | [Khalifa, MUN MSc thesis 2025](https://memorial.scholaris.ca/bitstreams/bbe845c9-5fc5-4712-8b50-692fb1e924f6/download) | "advance the lower bounds from v(n) ≥ 5 to v(n) ≥ 6" for n = 21, 33, 35, 39; v(n) is defined by "a Room d-cube of side n" | Name collision only: these are Room cubes, not MOLS |
| 13 | [Lampio–Östergård–Szöllősi, arXiv 1707.02287](https://arxiv.org/abs/1707.02287) | "There are exactly 72 … [BH(21,3)] matrices" | The mod-3 image needed by a 7-row DM exists (lemma L3) |
| 14 | DataCite `"circular florentine"` ([query](https://api.datacite.org/dois?query=%22circular+florentine%22&page%5Bsize%5D=100&sort=-created&fields%5Bdois%5D=titles,created,creators,url)) | 3 records in total; newest "Certify v0.5.0: an explicit 5x25 circular Florentine rectangle establishing F_c(25) >= 5" (created 2026-08-07T03:58:59Z) | No CFR(6,21) |

## Answers to the five questions
1. **Best lower bound on N(21).** It is **5**, from Nazarok 1991 (rows 3, 5, 7, 8). N(21) ≥ 6 does **not** appear in any source read, including the Dec 2024 table co-authored by Abel. A verified CFR(6,21) would therefore give 6 MOLS(21) and improve that table entry.
2. **Computational or exhaustive bounds on ω(Z₂₁).** None found. Evans 2013 gives ω(Z₂₁) ≥ 4. Known exact values are ω(Z₁₅) = 3 and ω(Z₉) = 1, which make F_c(15) = 4 and F_c(9) = 2 exact. The JS2019 search for 10 ≤ n ≤ 100 found nothing new at 21. The algebraic routes give only ω(Z₂₁) ≥ 3: Evans's Theorem 33 for 3m, and Jungnickel's Theorem 34, ω(Z_{q²+q+1}) ≥ N(q+1) − 1 with q = 4. Bryant–Buchanan–Wanless 2009 is about spectra of quasigroups with cyclic automorphisms, not counts of orthogonal squares (read at abstract level only). No nonexistence result was found.
3. **Sage.** `DM_21_6_1` is over `IntegerModRing(21)`, the cyclic group Z₂₁, with 6 rows (row 2 of the table).
4. **Recency checks (DataCite / arXiv / OpenAlex).**
   - Every hit was read at title level.
     - DataCite topic queries:
       - "circular florentine": 3 records
       - florentine + rectangle/array: 17
       - MOLS + 21: 57
       - difference matrix + 21/cyclic: 28
       - diagonally cyclic / MODCLS / orthogonal orthomorphisms / orthomorphism graph (the corrected 5-MODCLS query): 9
       - orthomorphism / complete mapping: 800 in total, newest 100 scanned
     - arXiv:
       - abstracts containing "orthogonal latin squares": newest 40, feed timestamp 2026-10-18T01:37:34Z
       - Florentine queries: 7 results
     - OpenAlex full text:
       - "circular florentine": 17
       - "orthogonal latin squares of order 21" since 2015: one hit, the Miller et al. paper in row 7
   - None of these claims CFR(6,21), a 7-row Z₂₁ DM, 5 MODCLS(21) or N(21) ≥ 6.
   - Author families, all with no hits on CFR, DM or MOLS:
     - Kirtchakov: 22 records, newest 2026-08-14T10:50:44Z. The only CFR item is CFR(5,25). His repository head 3159a74 (2026-08-19) contains only `CFR_5_25.json`.
     - Griffin Long: 2 records, 2026-10-15T20:42:34Z, both on SW(25/27/29,16).
     - Vos (2026, topic-filtered): 11 records, CPCW only.
     - Raval: 27 records, covering problems.
     - Ferudun: 26 topic-matched records, newest 2026-10-17T16:01:32Z.
     - Gippini: all 52 records, newest 2026-10-17T22:26:15Z.
     - Sadhu: 2 records.
5. **Viability.** See below.

## Significance of N(21)
A verified CFR(6,21) gives an OA(8,21), i.e. 6 MOLS(21), so N(21) ≥ 6, one more than the published 5. It would also give ω(Z₂₁) ≥ 5, F_c(21) ≥ 6 and 5 MODCLS(21). The upper bound stays trivial (20).

In the sources read, the n = 21 entry has been 5, credited to Nazarok 1991, in every table from the Handbook (2007) through Miller et al. (2024). Since 2007, only eight orders up to 100 have improved: 14, 18, 35, 48, 54, 60, 63 and 96. Significance is "potentially substantive specialist" [INFERENCE]. Correctness and novelty would still need separate checks.

## Viability [INFERENCE; my proofs, unreviewed]
**Density.** r/(n−1) = 6/20 = 0.30. That is higher than the exact maximum known for Z₁₅ (4/14 ≈ 0.29).

**Random-clique heuristic.** I estimated the expected number of k-cliques in the orthomorphism graph as C(T,k)·q^C(k,2). Here T is the published count of normalized orthomorphisms and q = n!/n^(n−1) is roughly the chance that two random ones are orthogonal.

| Group | Expected 3-cliques | Expected 4-cliques | Expected 5-cliques | Known value |
|---|---|---|---|---|
| Z₁₅ | ≈ 2×10⁵ | ≈ 0.01 | — | ω = 3 exactly (matches) |
| Z₂₁ | — | ≈ 9×10³ | **≈ 6×10⁻¹³** | ω ≥ 4 (Nazarok's 4-clique exists) |

The heuristic fails for Z₉ (it predicts about 200 orthogonal pairs; there are none) and for prime orders. So generic SAT or local search for CFR(6,21) is predicted to be futile. Any witness would have to be highly structured.

This is a different situation from CFR(5,25) and CFR(5,27). Those are 4-cliques with expected counts around e²¹ and e²⁸, which is why search found them.

**Structural lemmas.** None of them obstructs the target.
- **L2 (mod 3).** If three rows of a 4-or-more-row DM over Z₂₁ summed to a constant mod 3 in every column, a further row would need a function on AG(2,3) with all twelve line sums equal to 7. That forces the value 7/3 at every point, which is impossible. So no three rows sum to a constant mod 3. In particular, none of the five orthomorphisms can be linear (x ↦ ax).
- **L3 (projections).** The images mod 3 and mod 7 are a (Z₃,7;7)-DM (any 7 rows of a BH(21,3)) and a (Z₇,7;3)-DM (three copies of the GF(7) table). Both exist, so projection gives no obstruction.
- **L4 (row-permutation symmetries of a 7-row DM).**
  - The permutation can fix at most one row.
  - Cycle types 6+1, 4+3 and 3+2+2 are impossible. A column with a nontrivial stabilizer repeats a row-pair agreement, and 21 cannot be split as at most one fixed column plus free orbits of size 6 or 12.
  - So Nazarok's ℤ₅ symmetry pattern cannot be extended to 7 rows.
  - Types 7, 5+2, 4+2+1, 3+3+1 and 2+2+2+1 pass the counting test.

**Cheap decisive experiments to run first.**
- **Z₇ ⋊ Z₃ acting on rows**, i ↦ 2i with entries multiplied by 4, and the columns forming one regular orbit. This reduces to a single vector v ∈ Z₂₁⁷ with v₀ = 0. The condition is that {v_{j+1}−v_j} ∪ {4(v_{j+4}−v_j)} ∪ {16(v_{j+2}−v_j)} equals all of Z₂₁. That is 21⁶ ≈ 8.6×10⁷ candidates, which takes seconds. Heuristic: about 16 hits, roughly 0.75 orbits. A necessary condition: the residues of v mod 3 have class sizes {4,2,1}.
- **A 7-cycle on the rows** with 3 base columns. Estimated about 2 solutions and about 10¹¹ backtracking nodes.
- **Caveat.** JS2019 may already have covered some symmetric families without success; they do not list which groups they tried.

## UNKNOWN / access holes
- Handbook VI.62, Table 62.27 entry for n = 21 (I infer 5 from CPro1's dev/open split), and the body of Example III.3.50.
- Nazarok 1991 itself (not online).
- Body of Evans 2018 Ch. 13.
- Wanless 2004 (EJC): author PDF returned 503, ScienceDirect 403.
- Song 2000: not retried (the earlier scout got 403).
- Lampio's 2011 JSPI paper: 403.
- Zenodo full texts (I searched DataCite metadata only); MathSciNet and Russian-language follow-ups not searched.

## Deviations
- **Your correction.** My task prompt said "6 MODCLS". Per your message, the correct count is 5 MODCLS and 6 MOLS; I checked both bridges above and used the 5-MODCLS query.
- **No hashes or host clock.** I had no shell, so there are no sha256 values. I recorded URLs, commit SHAs and server timestamps instead. Those timestamps place the screen at about 18:20–18:45 PDT on 2026-10-17.
- **No computations run.** The heuristic figures are hand calculations from published counts.
- **Weaker reads.** The Miller et al. table row was read from a flattened PDF extraction of the accepted version. The Semantic Scholar API call failed.

**Files created:** none. Earlier run context I consulted, under REVIEW: `cfr27-priority-scout-v1.md`, `cfr27-status-screen-v1.md`, `cfr33-prior-art-parent-verdict.md` and `cfr27-priority-parent-spot-v1/summary.json`.

## Scout coordinate-change correction (verbatim)

You are right, and my report had this wrong. The incorrect sentence was "The Cayley table becomes j−i, which is Latin but not diagonally cyclic." It is the old x-coordinate that becomes j−i, not the Cayley square. The rest of the report, including the evidence table, is unchanged.

**Corrected coordinate change.**
- After normalizing the 7-row difference matrix to rows 0, id, θ₁…θ₅, the OA(8,21) has eight coordinates, indexed by column x and group element y:
  - x (the column index)
  - y (the zero row)
  - x+y (the identity row)
  - θ_k(x)+y for k = 1…5
- In the (x,y) frame the six MOLS are x+y and the five θ_k(x)+y. That part of my report was correct.
- Under (i,j) = (y, x+y), so x = j−i and y = i:
  - The old Cayley square x+y becomes the column coordinate j itself. It is no longer one of the squares.
  - The old coordinate x becomes the extra Latin square L(i,j) = j−i. It satisfies L(i+1,j+1) = L(i,j), so it is not diagonally cyclic.
  - Each θ_k(x)+y becomes i + θ_k(j−i). These are the five MODCLS.
- So in the (i,j) frame the six MOLS are {j−i} together with the five squares i + θ_k(j−i). The old Cayley square is swapped out for the old x-coordinate as an OA column.

**Checks (my own elementary proof, not independently reviewed).**
- j−i is Latin: for fixed i, j ↦ j−i is a bijection, and for fixed j, i ↦ j−i is a bijection.
- j−i is orthogonal to i + θ(j−i): with t = j−i, the pair (t, i+θ(t)) determines both t and i.
- i + θ(j−i) is orthogonal to i + φ(j−i) exactly when θ−φ is a bijection, which holds for any two of the five orthomorphisms.

**Conclusions unchanged.**
- A 7-row DM over Z₂₁ gives an OA(8,21), so 6 MOLS(21) and N(21) ≥ 6.
- The largest set of mutually orthogonal diagonally cyclic Latin squares (MODCLS) of order 21 has size ω(Z₂₁), so CFR(6,21) is equivalent to 5 MODCLS(21).
- My line "the identity map gives L(i,j) = j, which is not Latin" still holds. It agrees with the correction: i + id(j−i) = j is exactly the coordinate that becomes the column index.

I created no files and sent no other messages for this addendum.
