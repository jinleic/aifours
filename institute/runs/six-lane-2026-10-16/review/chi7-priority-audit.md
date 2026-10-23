# Uniform random seven-regular graph colouring: bounded priority audit

Recorded 2026-10-17 06:57:00 PDT. Read-only scout `Chi7Priority`; preserved verbatim below. The sharper entropy constant is prior (AN2005; explicitly reused for loopless random lifts by Nir–Pérez-Giménez2021); the bounded audit found no corresponding statement for the uniform regular model. A miss is not novelty.

---

## Verdict (bounded search, 2026-10-17)

- **χ(G(n,7)) = 4 a.a.s. for the uniform random 7-regular graph: not found stated or proved.** The latest statements I found put it at {4,5} or {4,5,6}, or call 4-colourability unsolved.
- **The sharper constant and the improved range: found.** But they are stated for random lifts, not for the uniform model.
  - Achlioptas–Naor 2005, eq. (12), already shows the constant (k−1)³log(k−1)/(k(k−2)).
  - Nir & Pérez-Giménez (arXiv:2109.13347v1, 27 Sep 2021; arXiv has no v2, and I found no journal version) restate it as their Theorem 3.1. They apply it with c = d/2 and prove k-colourability for d < 2(k−1)³log(k−1)/(k(k−2)). This holds for random n-lifts of any fixed loopless d-regular multigraph.
  - They explicitly do not cover the uniform model. That would need the bouquet B_d, which has half-loops, and they only call this "conceivable".
- **What this means for the candidate.** The sharper-constant step is already published. What may still be unpublished is the transfer into the KPW (Kemkes–Pérez-Giménez–Wormald) uniform-model argument, or extending Nir–Pérez-Giménez to loops. A referee may treat that as a direct corollary. Do not claim priority.

## Positive findings (verbatim)

**Achlioptas–Naor, Annals 2005** (`…/chi7-parent-inputs-v1/parent-sources/an2005-annals.layout.txt`)
- Theorem 7 is stated only for c ≤ c_{k−1} (line 290): "Theorem 7. For every A ∈ S_k and c ≤ c_{k−1}, g_c(J_k) ≥ g_c(A)."
- Eq. (12), lines 756–765: "(k−1)²/k · η(s/(k(1−t))) ≥ (k−1)²/k · min{k/2, (k−1)/(k−2)·log(k−1), k/(k−1)·log k} = (k−1)³/(k(k−2)) · log(k−1) > c_{k−1}, where (12) follows from elementary calculus."
- Remark, lines 767–775: "any c for which Theorem 7 holds must satisfy c < c_{k−1} + 1."

**Nir & Pérez-Giménez, "The chromatic number of random lifts of complete graphs"** (https://arxiv.org/abs/2109.13347)
- Theorem 1.2: "Let k ≥ 3, and define ℓ_k = 2(k − 1)³/(k(k − 2)) log(k − 1) > 2(k − 1) log(k − 1). Suppose d < ℓ_k, and let G be any fixed d-regular loopless multigraph. Then a.a.s. a random n-lift of G is k-colourable."
- On the uniform model: "We exclude half- and whole-loops to make some of the technical calculations in the paper simpler… It is conceivable that the result also holds for graphs with loops (of either type). In fact, such an extension would imply the main result in [18] for the uniform model G_{n,d}, by taking G = B_d." Here [18] is KPW.
- Also: "for any d-regular base graph G with more than one vertex, L_n(G) is not contiguous to the uniform model G_{n|V(G)|,d}."
- Eq. (8): "c_q = (q − 1)³/(q(q − 2)) log(q − 1)". Theorem 3.1, attributed to Achlioptas and Naor [2]: "…for any c < c_q, (1/q)h(M) + c log(q² − 2q + ρ(M)) ≤ log q + c log (q − 1)²".
- Section 5: "Note that d < ℓ_k implies d/2 < c_k, where c_k is defined in (8). Therefore, Theorem 3.1 (with q = k, c = d/2 …) yields…"
- Corollary 1.3(ii): "if d ∈ [u_{k−1}, ℓ_k) then a.a.s. χ(L_n(K_{d+1})) = k", with u_k = 2 log k/(log k − log(k−1)).
- [INFERENCE] At k = 4 this gives u_3 ≈ 5.419 and ℓ_4 ≈ 7.416, so d ∈ {6,7} and χ(L_n(K_8)) = 4 a.a.s. That is a 7-regular random-lift model, not G(n,7). The paper never writes d = 7.

## Works checked: what each says about d = 7 or the constant

**Pinned local sources**
- **Shi–Wormald, CPC 2007.** Abstract via the Sciweavers mirror: "…{3, 4} for d = 5, {4, 5} for d = 7, 8, 9, and {5, 6} for d = 10." The upper bound comes from a colouring algorithm. The pinned 2004-24 report is a scanned image with no extractable text.
- **Achlioptas–Moore, cond-mat/0407278.** Their table gives d = 7, 8, 9 → χ ∈ {4,5,6} (lines 40–46). They use the Achlioptas–Naor bound "for d < c_{k−1}" (lines 503–516).
- **KPW, arXiv:0812.2937v1** (no v2 exists).
  - Theorem 1 (lines 102–107) gives χ ∈ {k−1, k}; for d = 7 that is {4,5}.
  - The degrees they call newly determined are "χ(G_{n,10}) = 5 and χ(10^6) = 46523."
  - They use "Theorem 7 in [3]… if d < d_{k−1} := 2(k − 1) log(k − 1)" (line 1004).
- **ACG, arXiv:1812.09691v4** (Combinatorica 2022).
  - Table 1 has d_{4,smm} = 6, d_{7,smm} = 21, d_{10,smm} = 39 and d_4 = 10. It is described as "the value d_{q,smm} up to which (1.2) implies that χ(G(n,d)) ≤ q w.h.p.", where (1.2) is d < 2(q−1) log(q−1).
- **Wormald 1999 survey**, lines 1104–1121: "a.a.s. χ(G) ≥ 4 for G ∈ G_{n,d} when d ≥ 6… Non-trivial asymptotically almost sure upper bounds for small d seem to be harder to obtain."

**Theses and surveys**
- **Kemkes PhD thesis, "Properties of random graphs", UWSpace 2008** (http://hdl.handle.net/10012/4006). The colouring result is conditional. Quote: "It would also establish, for example, the previously-unknown result that a.a.s. χ(G_{n,10}) = 5." Conclusion: "The results on the chromatic number of G_{n,d} and G_{n,5} are conditional on hypotheses." Nothing on d = 7, 8, 9 or on the sharper constant.
- **Kang–McDiarmid, "Colouring random graphs"** (draft dated 13 May 2014). Says Shi–Wormald give χ(G_{n,4}) = 3, χ(G_{n,5}) ∈ {3,4} and χ(G_{n,6}) = 4, then restates KPW. Nothing on d = 7.
- **Frieze–Karoński book** (CMU PDF dated 7 Aug 2026). Only KPW's two-value range and Shi–Wormald's χ(G_{n,4}) = 3.
- **Erdős problems site (UCSD).** Restates KPW only.
- **Bykova, UChicago REU 2018.** Expository; uses the c_{k−1} constant; nothing on regular graphs.

**Papers citing Achlioptas–Naor or KPW**
- **Coja-Oghlan–Efthymiou–Hetterich, arXiv:1308.4287v1.** "several papers deal with the k-colorability of random regular graphs for k = 3, 4. This problem is not solved completely by [36] (nor by the present work)." Their main result only holds for k ≥ k₀ with k₀ not given explicitly.
- **Kunisky–Yu, arXiv:2404.17012v1** (FOCS 2024). Theorem 1.13 ("d = 7") uses only "χ(G) ≥ 4 with high probability [AM04]". Their Table 1 row reads "Min coloring | 7 | ∈{4, 5, 6} [AM04]".
- **Banks–Moore–Neeman–Netrapalli, COLT 2016.** Lemma 12 uses "δ < (q − 1) log(q − 1)", the old constant.
- **Banks–Kleinberg–Moore 2017.** χ(G_{n,d}) known "for almost all d"; no d = 7 statement.
- **Bandeira–Banks–Kunisky–Moore–Wein 2020.** No small-d colouring statement.
- **Dani–Moore–Olson 2011.** Uses the old constant and cites Achlioptas–Moore's three-value range.
- **Coja-Oghlan–Krzakala–Perkins–Zdeborová, arXiv:1611.00814.** Proves q-colourability for d < d_{q,cond} (no explicit value) for all q ≥ 3, but only in G(n,d/n): "here we confine ourselves to the Poisson case".
- **Coja-Oghlan–Kapetanopoulos–Müller, arXiv:1802.09311.** Erdős–Rényi-type model only.
- **Coja-Oghlan et al., arXiv:2007.07494.** Treats the regular-graph Potts antiferromagnet only at finite temperature, with strictly positive weights; no hard-constraint colouring result.
- **Lower relevance, nothing on d = 7:**
  - Chasing the k-colorability threshold (arXiv:1304.1063)
  - The condensation phase transition in random graph coloring (arXiv:1404.5513)
  - Spin systems on Bethe lattices (arXiv:1808.03440)
  - Bennett–Frieze, random regular hypergraphs (arXiv:2301.00085)
  - Gunderson–Nir, oriented chromatic number (arXiv:2202.12323)
  - Yu, polynomial threshold functions on random regular graphs (arXiv:2608.28539)

**Physics (not rigorous)**
- Krzakala–Pagnani–Weigt, cond-mat/0403725, Table I, regular graphs with q = 4: c = 8 COL, c = 9 COL (1RSB), c = 10 UNCOL. So physics predicts 7-regular random graphs are 4-colourable.

**Index sweeps**
- OpenAlex works citing KPW: all 26 titles screened.
- OpenAlex works citing Achlioptas–Naor with "regular" in title or abstract: 28 screened.
- OpenAlex works citing Shi–Wormald or Achlioptas–Moore: 49 screened.
- Nir–Pérez-Giménez has 0 citers in OpenAlex.
- arXiv API abstract search "random regular" plus colour terms: 19 hits screened.

## [INFERENCE] notes (hand arithmetic, not checked by code)

- For q ≤ 20, the improved range adds one new degree each at d = 7, 22, 40, 53, 60, 67, 74, 89, 112 (q = 4, 7, 10, 12, 13, 14, 15, 17, 20), compared with ACG's d_{q,smm} column. Combined with ACG's d_{q−1} values, each would give χ = q exactly. None of these degrees appears as determined in any source I read.
- The Achlioptas–Naor Remark caps their route at c < c_{k−1} + 1. For k = 4 that is d < 8.59, so this method can reach at most d = 8, never d = 9.
- KPW's extra condition k² − 2k − d + 2 > 0 holds for k = 4, d = 7 (value 3).

## Dated misses (all 2026-10-17)

Web searches returned no statement of χ(G(n,7)) = 4 or of the improved range for the uniform model. Queries tried:
- "random 7-regular" with 4-colourable or 4-colorable
- "7-regular" with "chromatic number" and a.a.s./w.h.p.
- "G(n,7)" / "G_{n,7}" with chromatic or 4-colourable
- "(k-1)^3" "k(k-2)" "log(k-1)" chromatic
- "22-regular" / "40-regular" chromatic
- MathOverflow small-degree colouring
- improved 4-colourability via second moment / small subgraph conditioning
- lecture notes on the Achlioptas–Naor constant

## Access holes

- **Citation indexes.** Semantic Scholar API (tool rejects the URL), Google Scholar (page needs JavaScript) and dblp (anti-bot wall) were unreachable. So citation coverage is OpenAlex only, which is known to be incomplete.
- **ScienceDirect (HTTP 403).** Could not read the KPW Adv. Math. 2010 journal version, the COEH JCTB 2016 version, or Shang 2026, "The fractional chromatic number of random graphs".
- **Pérez-Giménez talks and pages.**
  - UNL site failed TLS: publications page and the MIPT Dec 2020 slides.
  - PCO Sep 2020 slides are image-only, no text.
  - RS&A 2019 abstract: HTTP 503. AMS Fall 2020 abstract page did not render.
  - These talks could contain uniform-model remarks I could not see.
- **Theses not located:** JD Nir's PhD dissertation (UNL, ~2020–21) and Hetterich's PhD thesis.
- **Not read in full:**
  - Shi–Wormald CPC paper (abstract only; the pinned PDF is a scan).
  - The IEEE FOCS 2024 version of Kunisky–Yu (arXiv v1 only).
  - The CUP 2015 final of Kang–McDiarmid (2014 draft only).
