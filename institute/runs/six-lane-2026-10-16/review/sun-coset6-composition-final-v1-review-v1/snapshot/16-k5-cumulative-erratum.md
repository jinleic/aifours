# rules-v1 erratum v3 (cumulative; supersedes erratum v1 and v2 as the single list)

The host-clock freeze record is in `evidence/proof-v4.sha256`. `rules-v1.md` (cb86c168…390f), erratum v1 (f1e51b37…bc56) and erratum v2 (df2955f2…3f) stay frozen and unchanged.

**What this erratum does not change.** No formal lemma statement used by the engine changes, and no code changes. "[NEW]" in rules-v1 means "written in this lane"; it is not a novelty claim.

| # | Where in rules-v1 | Correction | Source |
|---|---|---|---|
| E1 | L3 commentary on M-S Cor 3.11 | Take α_UV = 1 and α_UW = α_VW = b with b ∈ {2, 3}. The vertex products are b at U, b at V and b² at W, so τ_max = b. When τ = b, the K1 links are at **U and V**, not at W (the vertex shared by the two equal edges). L3 at U with S = {V, W} gives 1 + b ≤ 3, which fails for b = 3. The commentary is unused, and the formal rules and code were already correct. | Codex v1 MINOR 2; Codex delta; Claude delta m10 |
| E2 | C4 wording | Arbitrary single-label mutation need not break a witness; in run1, 94,067 of 634,470 mutants break one. C4 is restated as *selected* intended-reason demonstrations (controls-v2/v3 part A). | Codex v1 MINOR 3 |
| E3 | L3 note and README §2 on M-S Lemma 4.4 | It is not a misprint. The primary text reads α ≠ 2; "6=" is pdftotext's rendering of ≠. | Codex v1; Claude F-5 |
| E4 | Lemma R (R5) | (R5) is not derived from (R4). The k = 2 case is applied directly to the two named pieces: right-translate into U_v, invert, then apply k = 2 (proof-v4 §5). (R4) is deleted as unused. | Codex v1 MINOR 1; Claude F-1, m2 |
| E5 | L1 remark on gcd(α, r_z) | Applies only to α ∈ {2, 3}; for α = 1 the quotient α/gcd = 1 in every case. | Claude F-10 |
| E6 | L0.8 and R1 | Cite Zhu **Theorem 1.1**. M-S Lemma 4.4 applies Lemma 3.10a outside its hypotheses (a load-bearing defect). Prop 4.5 is re-proved with the patch (T = 4r_1r_2r_3τ, 3 \| r_1τ, τ ≤ 2, so 3 \| r_1), with "multiple of \|G\|/4" only (F-8) and "harmonic" fixed (F-9). See proof-v4 §2. | Claude F-2, F-7, F-8, F-9 |
| E7 | C4 status, controls, demo labels | C4 is a **shared-code witness recheck**, not independent verification. check v2 is a **lane self-report**. Controls never gate. The engine-v1-run1 demo named "K_star_1111" actually fired T; the one named "P_star_3333" actually fired K. | Codex engine audit |
| E8 | none (record only) | An exploratory, unfrozen eval cell (a vertex LP form of Lemma R) timed out at 900 s with no result. Nothing depends on it. | lane record |
| E9 | §0 and the use of L3 | Every application of L3 needs the pair condition in the form U_vU_i ⊆ U_jU_i or U_vU_j ⊆ U_iU_j. Sentences such as "U_1U_2 ⊆ U_1U_3 holds" state the inverse and must be inverted, or cited as K2 with an explicit tuple (v, j, k). proof-v4 writes every inversion out. | Claude delta m1 |
| E10 | Lemma R setting | The hypothesis "g_1U_1, …, g_5U_5 are pairwise disjoint" must be stated. Without it, (R1) and (R5′) fail. | Claude delta m3 |
