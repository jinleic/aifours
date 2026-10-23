**Priority/status audit: isolation of the qutrit 2-unitary orbit among dual and T-dual gates (T7, d = 3)**

**Answer.** I found no earlier source, in a bounded search, that proves isolation of O9 in D or T, or a strict entangling-power gap. It is also not recorded as folklore: the review authors still call the gap unestablished in June 2026. It is close to being immediate from prior results, though. The key computation was already published in Geng, arXiv:2211.15776v3 (Dec 2022, unrefereed). That paper shows that at an OLS(3) perfect tensor, every pair of the three linearized unitarity conditions has the same 33-dimensional kernel. [44] says the LU orbit is a 33-dimensional manifold. Combining the two with the standard regular-value lemma gives Theorem 1 in a few lines. Neither source draws that conclusion. Geng drew the opposite one.

PROOF.md §8 cites only [44] and does not mention Geng. That is the main fix the write-up needs.

## Sources (quotes ≤40 words, read by me in the primary text)

| # | Source, location | Quote | Stance |
|---|---|---|---|
| 1 | Review arXiv:2508.04777v3 (25 Jun 2026), p.9; layout lines 553–559 | "the other peculiarity of AME(4, 3) is that U9 seems to be isolated in the set of dual or T-dual unitaries. This is visually seen as a gap in the ep(U)−gt(U) plot" | target is open |
| 2 | same, p.9; lines 574–578 | "so that this reveals better the region of the gap, the rigorous existence of which is yet to be established." | target is open |
| 3 | same, p.21; lines 1399–1405 | "(T7). Are there dual/T-dual gates in U(9) arbitrarily close to the 2-unitary permutation matrix P9 related to the state AME(4, 3)?" | target is open |
| 4 | same, p.9; lines 568–571 | "The dual unitary Us(2π/3) is an orthogonal matrix with entangling power 15/16 = 0.9375 which is likely to be the highest possible value for dual unitaries that are not 2-unitary." | baseline |
| 5 | same, p.9; lines 593–597 (d = 4) | "There exists a continuous parameterization of dual and T-dual unitaries that limit to 2-unitaries [62] and hence there appears to be no excluded region in the vicinity of the 2−unitary gate" | d = 4 contrast |
| 6 | Review v1 (6 Aug 2025), labelled T6; v2 (30 Dec 2025), labelled T7 | Same question text, and the same "rigorous existence … yet to be established" sentence | dates the open statement |
| 7 | [44] arXiv:2212.06737v2, Theorem 1; lines 185–187 | "There is only one LU-equivalent class of AME(4, 3) states or, equivalently, one LU-equivalent class of 2-unitary gates of size 9." | uniqueness |
| 8 | [44], p.3; lines 255–265 | "The four 3 × 3 unitaries, u1,2′ and v′1,2 define a 33-dimensional manifold of 2-unitaries." (stated without derivation in the text I read) | orbit dimension |
| 9 | [44], appendix; line 931 | "it has already been shown that any enphasing of P9 is LU-equivalent to it [23]." | d = 3 is special |
| 10 | Geng arXiv:2211.15776v3, Prop. 6, p.4 | "The triple intersection of the tangent spaces T := ⋂ TΦFi⁻¹(Ui) equals to all 3 pairwise intersections TΦFi⁻¹(Ui)∩TΦFj⁻¹(Uj), ∀1 ≤ i < j ≤ 3." | **core computation already published** |
| 11 | same, Prop. 7, p.5; and p.4 | "T is a 33-dimensional real vector space." / "We compute the intersection of the tangent spaces T with Python" | core computation; exactness not stated |
| 12 | same, Thm 10 (p.5) and proof (p.6; HTML confirms the ∉) | "there is a 4-dimensional subset consisting of perfect tensors not locally equivalent to any solution corresponding to any OLS(3)" / "we conclude that e₁ ∉ TΦOrbΦ" | counter-claim, contradicted by [44] Thm 1 |
| 13 | Aravinda–Rather–Lakshminarayan arXiv:2101.04580v2 (PRR 2021), text with Fig. 9, PDF p.30 | "The third ensemble used is the dual-CUE, which can have as large as ep(U) = 1, but q = 3 is a peculiar case, where there is a gap at ep(U) = 1." | numerical gap only |
| 14 | Rather–Aravinda–Lakshminarayan arXiv:1912.12021v3 (PRL 2020), p.4 | "For the case of qutrits, the dual-CUE distribution is split and there is a peak at the largest possible value of 1/2." | numerical |
| 15 | Pandya arXiv:2610.16673v1 (12 Oct 2026), footnote 24 | "It is an upper bound on the number of parameters, modulo local unitaries, of any family of AME states through \|Φ⟩, with equality where the rank of the linearized conditions is locally constant." | the method is current practice (three cuts, d = 6) |
| 16 | Nicoară, math/0404301 (J. Operator Theory 2006) | "We prove that the commuting squares satisfying the span condition are isolated among all commuting squares (modulo isomorphisms)." | classical first-order isolation criterion (Hadamard/spin-model case) |
| 17 | Bistroń–Czartowski–Życzkowski arXiv:2312.17719v4, abstract | "resulting in multiple isolated gates" | here "isolated" means individual examples, not topological isolation |

## How the pieces connect

- **[44] uniqueness** says D ∩ T = O9. So O9 is trivially isolated inside the set of 2-unitaries, but this says nothing about the larger sets D or T.
- **Theorem 1** says D ∩ N_ε(O9) = O9, and likewise for T. This is strictly stronger and is not implied by [44].
- **Corollary 2** needs both facts: compactness of D \ O9 (from Theorem 1) and "e_p = 1 ⇒ in O9" (from [44]).
- **Geng's flattenings** F1, F2, F3 correspond to the cuts 12|34, 13|24 and 14|23 used in PROOF.md §1.4. His pairwise kernels are therefore exactly ker dF_D and ker dF_T.
- Geng works at an OLS(3) tensor rather than P9 itself. All 2-unitary permutations of order 9 are LU-equivalent (PRX Quantum 3, 040331, Prop. 2), and kernel dimension is LU-invariant, so the result transfers to P9.

## Exact delta

- **Theorem 1 itself is not located anywhere.** Its ingredients were already public:
  - kernel 33: Geng 2022, computed numerically;
  - orbit dimension 33: asserted in [44].
- **What the candidate adds:**
  - the identification ker = T_{P9}O9, which corrects Geng;
  - the regular-value, LU-covariance and compactness argument;
  - a hand proof through the perfect tetracode and S3 orbits, which explains Geng's 12 rank-6 + 9 rank-1 basis;
  - exact rank certificates.
- **Corollary 2 (qualitative gap) is not located; the review explicitly calls it open.** No gap value is given, and the 15/16 conjecture is untouched.
- **Literal T7 is trivially yes**, through LU images of P9. Only the non-trivial reading is answered, and only for d = 3. The other-dimensions half of T7 is untouched.
- **Geng's Theorem 10 is false**, as [44] Theorem 1 already shows. My hand check [INFERENCE, not machine-verified]:
  - His Prop. 7 basis fits a relabelled tensor C′ = {1123, 1232, 1311, 2131, 2213, 2322, 3112, 3221, 3333}, not his printed Example 4 tensor.
  - Relative to C′, his e₁ is exactly the LU generator E21 − E12 on party 2, so it does lie in the orbit tangent.
  - Relative to the printed Φ, e₁ fails the cut-12 condition (the points 1132 and 2123 should pair).
  - His paper has no later version and its one OpenAlex citer is unrelated; neither [44] nor the review cites it.
- **Note for the d = 5/7 continuation** [INFERENCE]:
  - Geng's Prop. 15 gives T = 145 at d = 5, against my count of about 97 for the LU tangent, so the same linear test cannot certify isolation there.
  - [44] Theorem 2 (enphasing gives infinitely many LU classes for d ≥ 4, d ≠ 6) suggests the permutation orbit is not isolated even among 2-unitaries.
  - The d = 4 control is consistent with Geng's Prop. 14, which says the pairwise/triple equality fails at d = 4.

## Latest explicit open attestation

- arXiv:2508.04777v3 (25 Jun 2026), p.9 and p.21. The same text appears in v1 (6 Aug 2025, as T6) and v2 (30 Dec 2025, as T7).
- The journal version, Rep. Prog. Phys. 89, 057601 (2026), e-published 19 May 2026, was not read. Its Crossref reference list keeps the thesis entry (key ropae672abib62) and the universal-entangler reference, which is indirect evidence that the passage survived [INFERENCE].
- No later restatement or resolution was found among the 17 Semantic Scholar citers through 12 Oct 2026; I spot-checked six of them.

## Earlier equivalent

None found in the bounded search. The closest partial results are Geng 2022 (Props. 6–7), the [44] 33-dimension remark, and the numerical observations from 2020, 2021 and 2025–26. The first-order isolation method itself is classical: Tadej–Życzkowski's defect, Nicoară's span condition, and now Pandya 2026.

## Access holes

- **Rather thesis [62] was not read.** The Shodhganga metadata was readable: 246 + xxi pages, completed 2023, 13 PDF files. The three PDFs I tried (03_content, 04_abstract, 12_chapter7) all returned an Anubis proof-of-work bot challenge. I did not bypass it and found no other copy. The IITM defense notice (3 Feb 2022) does not mention a gap.
  - [INFERENCE] The thesis probably contains no proof, because its advisor co-signed the 2026 "yet to be established" sentence. Seeing the thesis text would settle this.
- **Other sources not read:**
  - IOP published review: blocked by a captcha.
  - Krishnan–Sunder 1996, Trans. AMS (biunitary permutation matrices of index 9): HTTP 403.
  - White 2013 UT thesis: abstract only.
  - Published versions of PRA, PRX Quantum, PRR and PRL papers: I used the arXiv versions.
  - Geng's code: not checked, so whether his computation was exact is unknown.
- **Search limits:** no full-text search engine was used; the arXiv API searches abstracts only, and citer lists may be incomplete.
- **Hash:** the PROOF.md SHA-256 f44ab953…43ce comes from the lane's `evidence/SHA256SUMS.txt`. I had no hashing tool, so I did not compute it myself. The copy I read is the post-erratum version (§1.4 shows M₁₄ = (U^Γ)^T S9).

## Calibrated significance

Not major: there is no new method, no quantitative gain, no explicit gap, and it covers d = 3 only. This is a **modest extension, close to corollary level**. It is a short, rigorous answer to the non-trivial reading of an explicitly posed 2025–26 review question (T7 at d = 3), plus a proof of the qualitative gap that has been seen numerically since 2020–21. The main limitation is that its core computation was already in Geng 2022 (numerical, unrefereed, misinterpreted), and the remaining steps are textbook.

Suggested edit to PROOF.md §8: cite Geng 2022 Props. 6–7 and 14–15 as the prior kernel computation, note that its Theorem 10 conflicts with [44], cite PRR 2021 and PRL 2020 for the numerical gap, and use the history wording "no earlier equivalent located in the bounded screen".

## Read scope

- **Lane, read in full:** `README.md`, `review/PROOF.md` (191 lines), `evidence/LOG.md`, `evidence/SHA256SUMS.txt`, and the contract JSON.
- **Lane, ranges:**
  - `sources/2508.04777v3.layout.txt` lines 195–219, 354–473, 519–603, 1300–1423, 2404–2433;
  - `sources/2212.06737v2.layout.txt` lines 1–78, 174–303, 395–423, 920–935;
  - `screening/phys1-post-capacity-screen.md` lines 30–72.
- **External:** the arXiv texts and greps listed in the Sources table, plus arXiv API, OpenAlex, Semantic Scholar, Crossref and EPMC metadata.
