# Physics replacement screen (parent capture 2026-10-17 16:48:50 PDT)

Verbatim read-only scout report; hypotheses/inferences remain unverified unless separately checked.

I recommend **#1: decide M(7), the largest size of a non-classical set of quantum Latin squares of order 7.** In this run phys‑1 already proved M(7) ≤ 3, so phys‑2 would only need to show whether a non-classical set of three exists. Either answer settles a stated open case. The catch is that this is the same MOQLS family phys‑1 is working on, though not Problem 16. **If you want phys‑2 kept out of that family, take #2 instead, the PPT Schmidt-number‑3 question in 4⊗4.** It overlaps nothing, but it is less likely to finish in 20 hours.

I ran no code and wrote no files; anything marked [INFERENCE] is my own unchecked reasoning.

## Ranked candidates

| # | Exact finite target | Stated open in | Fits 20 h / 4 CPU / 8 GiB? | Significance | Kill-check | Main risk |
|---|---|---|---|---|---|---|
| **1** | Is there a non-classical set of 3 MOQLS(7)? Yes ⇒ M(7)=3; no ⇒ M(7)=2. A maximal-cardinality pandiagonal QLS(7) (MCPQLS(7)) would be a "yes" witness | Ball–Simoens 2026 (Table 2: M(7) is 2–4); Han et al. 2025 Thm 3.8; Huang–Li 2026 (MCPQLS(7)); Zhang–Cao 2026 (remaining orders) | Good: phys‑1's support‑SAT, exact phase lemmas and drat-trim pipeline can be reused | Determines one table entry exactly (narrow but clean) | No prior claim found | Same family as phys‑1; 3‑sets have weaker constraints than 4‑sets, so the SAT may be larger |
| 2 | A PPT state with Schmidt number 3 on C⁴⊗C⁴ or C³⊗C^d (equivalently a 2‑positive indecomposable map) | Krebs–Gachechiladze 2024 and 2025; Johnston–Lovitz 2026 | Uncertain: only a positive witness is realistic | Larger | No prior claim found | May not exist; the 2‑positivity certificate is the hard part |
| 3 | A maximal-cardinality 1‑resolvable QLS of order 10, or a maximal-cardinality diagonal QLS of order 6 | Zhang–Cao 2026; Huang–Li 2026 | Likely quick | Modest | Neighbouring cases were closed within weeks | Very crowded, including AI-assisted Zenodo notes |
| 4 | A graph on ≤20 vertices with χ_q < χ_q^(1) | Lalonde (EJC 2025) | Open-ended search | Modest | No claim found | The lower-bound certificate for orthogonal rank is hard |
| 5 | Codes ((9,13,3))₂ or ((11,5–7,4))₂ (gaps in the AMH Table 1) | Table gap only, no "open" sentence | Poor | Modest | — | Same family as the stalled ((7,3,3)) target. Not recommended |

## Evidence per candidate

**1. M(7)**
- **Open statements (verbatim):**
  - Ball–Simoens, [arXiv:2607.12933v2](https://arxiv.org/abs/2607.12933v2), 27 Jul 2026 (still the latest version): "Problem 1. Given n ≥ 2, what is the largest value of t such that t MOQLS(n) exist?" Table 2 gives M(7) as 2–4.
  - Han et al., [arXiv:2507.20154v1](https://arxiv.org/abs/2507.20154), 27 Jul 2025, Theorem 3.8: "For v ≥ 4, there exists a non-classical 3-MOQLS(v), except possibly for v ∈ {4,5,...,15}."
  - Huang–Li, [arXiv:2606.27758v1](https://arxiv.org/abs/2606.27758), 26 Jun 2026: "Here, an MCPQLS(5) does not exist, and the existence of MCPQLS(7), MCPQLS(11), and MCPQLS(n) with gcd(n,6) ≠ 1 remains to be determined."
  - Zhang–Cao, [arXiv:2608.29201v2](https://arxiv.org/abs/2608.29201), 7 Sep 2026: "…It remains to determine the existence of maximal-cardinality 2-RQLS(v)s for the remaining orders." Order 7 is among the remaining orders.
- **Why 7 is the smallest open case:** Table 2 already gives M ≥ 3 for n = 9, 11 and 13, and M(4), M(5), M(6) ≤ 1. So 3‑sets are open only for n ∈ {7, 8, 10, 12, 14, 15}.
- **Why a finite computation can decide it:**
  - In standard form, the three squares' entries at each off-first-row cell have pairwise disjoint supports inside 6 coordinates, so every weight is at most 4 [INFERENCE].
  - Split by how many squares are classical (2, 1 or 0). Phys‑1's Theorem B already rules out 3 classical + 1 quantum.
  - Egan–Wanless (in phys‑1's lane imports) list 7 paratopism classes of 2‑MOLS(7), 5 of them maximal (cannot be extended to a third classical square).
  - A quantum square orthogonal to a maximal pair is automatically non-classical, since a classical one would extend the pair [INFERENCE]. So any exact quantum square found there gives M(7)=3 at once. Phys‑1 noted this regime was never covered (`moqls7-problem16/proof/PROOF_PARTIAL.md:119-121`).
  - A non-classical pandiagonal QLS(7) of any cardinality is enough. Constructions of the Ball–Simoens Theorem 6 type seem capped at 2 over F₇: my hand check finds only two undetermined slopes {3,4} for f(x)=x⁴ [INFERENCE].
- **Verification:**
  - Positive: an exact witness over a cyclotomic field, two independent exact checkers (rows and columns orthonormal, pairwise tensor-product orthonormal bases, more than 7 distinct rays).
  - Negative: a written reduction plus SAT proofs checked with drat-trim (not lrat-check alone), two encodings, and controls: the Corollary 7 non-classical pair and classical triples from AG(2,7).
- **Kill-check:**
  - DataCite MOQLS queries: 9 records, all arXiv, newest 2026‑09‑25.
  - DataCite Zenodo-only: no MOQLS or pandiagonal QLS(7) record. The only order‑7 quantum item is Guo, [10.5281/zenodo.22852779](https://doi.org/10.5281/zenodo.22852779) (2026‑09‑20), which covers single QLS(7) cardinalities.
  - The arXiv listing for "quantum Latin" shows no paper newer than 2610.17170 (12 Oct 2026).
  - The forward citers I read do not treat M(7); the local openai/math corpus and EulerSolve have no hits.

**2. PPT Schmidt number 3**
- **Open statements (verbatim):**
  - Krebs–Gachechiladze, [arXiv:2402.12966v1](https://arxiv.org/abs/2402.12966), PRL 132, 220203 (2024): "Our findings leave as an open problem whether there exist Schmidt number three states in 3 × d, and what the smallest local dimension is in 4 × d systems to accommodate such states."
  - [arXiv:2509.07086v1](https://arxiv.org/abs/2509.07086) (Sep 2025) calls 4×5 "the smallest system known to host such entanglement".
  - [arXiv:2609.11849v1](https://arxiv.org/abs/2609.11849) (10 Sep 2026) says its construction "does not improve the lower bounds on M_PPT(m,n) in the small-dimensional cases".
- **Why it is hard:** the easy certificate (range criterion) cannot work in 4⊗4 or 3⊗d, because a state whose range avoids Schmidt rank ≤ 2 has rank ≤ 4 (or ≤ d−2), and low-rank PPT states are separable [INFERENCE].
- **Route:** a genuine 2‑block-positive witness with an exact rational sum-of-squares certificate (roughly a 64×64 Hermitian Gram matrix), an exact PPT check, and Tr(Wρ) < 0. The 4×5 state is the positive control.
- **Kill-check:** recent work (An–Lee 2609.34255, Dinh et al. 2609.09675, Park 2602.09860, Kian 2605.26272 and 2512.05560) does not settle 4×4 or 3×d. There is no Zenodo claim.

**3. QLS exceptional orders**
- **Open statement (verbatim, Zhang–Cao v2):** "It remains to determine whether a maximal-cardinality 1-RQLS(v) exists for v ∈ {10, 14, 18, …, 94}"; the diagonal-QLS list is reduced to M₂ \ {8, 12, 20, 24, 32, 40, 48}.
- **Kill-check:** the idempotent-QLS list is already closed by [arXiv:2609.24653](https://arxiv.org/abs/2609.24653) (21 Sep 2026). I could not tell whether that paper's order‑6 example also has an anti-diagonal transversal. Order‑6 cardinalities 13–35 were closed by several 2026 notes.

**4. Lalonde graphs**
- **Open statement (verbatim):** "look for graphs on 20 vertices or less exhibiting a separation between χq and χq(1)" ([arXiv:2311.08194](https://arxiv.org/abs/2311.08194); EJC 32(1) P1.18, 2025).
- **Kill-check:** the field is active (a quantum Hedetniemi counterexample 2609.20690, a Zenodo "Database of Quantum Graphs"), but I found no claim on this question.

## Leads already resolved by others
- **Genuinely unextendible product bases:** solved by [2608.12785](https://arxiv.org/abs/2608.12785) (13 Aug 2026), which builds a 14‑element three-qutrit example.
- **Minimum UPB sizes:** claimed settled in all systems by [2609.05657](https://arxiv.org/abs/2609.05657).
- **Uniform mixing on C₉ and C₁₅:** done in [2607.28345](https://arxiv.org/abs/2607.28345) and [2607.04207](https://arxiv.org/abs/2607.04207).
- **Smallest graph with χ_q < χ:** settled by Lalonde.
- **Unextendible stabiliser bases:** [2608.10202](https://arxiv.org/abs/2608.10202) states no open problem.
- **Minimal Kochen–Specker set in d=3:** needs thousands of CPU hours.
- **Ball–Simoens Problem 17 at n=10:** too hard.
- **T7 in other dimensions:** d=4 is already known to be non-isolated.

## Recommended next step
Freeze M(7) as the contract, then run the case with two classical squares first. Test the 5 maximal 2‑MOLS(7) species and the 2 extendable classes, including the pandiagonal one, with weights ≤ 4 and exact realizability checks, in a chunk of at most 3 hours.

## Access holes and clock
- OpenAlex citer lists returned HTTP 429 twice; the Zenodo API returned 403.
- The Open Quantum Problems site returned 500 and the AME table page returned 404.
- DataCite searches metadata only, not PDF full text.
- Several sources were read only in part (Huang–Li, Han et al., Johnston–Lovitz); Semantic Scholar and Google Scholar were not checked.
- I have no shell clock. The newest DataCite record in my results was created 2026‑10‑17T22:36:21Z (15:36 PDT), so the searches ran after that; the run's last checkpoint I read was 15:57:09 PDT.

```json
{"recommendation":"C1","fallback_if_MOQLS_family_excluded":"C2",
"candidates":[
{"rank":1,"id":"C1","target":"Existence of a non-classical 3-MOQLS(7); decides M(7)=3 vs 2 given the run's accepted M(7)<=3; MCPQLS(7) is a sufficient witness","sources":["arXiv:2607.12933v2 (2026-07-27) Problem 1 + Table 2","arXiv:2507.20154v1 (2025-07-27) Thm 3.8","arXiv:2606.27758v1 (2026-06-26) MCPQLS(7)","arXiv:2608.29201v2 (2026-09-07) remaining 2-RQLS orders"],"verify":"exact cyclotomic witness + 2 checkers; or written reduction + drat-trim-checked SAT, 2 encodings, Cor7/AG(2,7) controls","kill_check":"no prior claim found (DataCite all+Zenodo, arXiv listing to 2610.17170, local openai/math, EulerSolve)","risks":["same family as phys-1","3-set SAT larger than 4-set","active QLS groups incl. AI-assisted Zenodo authors"]},
{"rank":2,"id":"C2","target":"PPT state with Schmidt number 3 on C4xC4 or C3xCd (2-positive indecomposable map)","sources":["arXiv:2402.12966v1 / PRL 132,220203","arXiv:2509.07086v1","arXiv:2609.11849v1"],"verify":"exact PPT check + exact SOS 2-block-positivity certificate + Tr(W rho)<0","kill_check":"no prior claim found","risks":["may not exist","negative direction out of reach","certificate difficulty"]},
{"rank":3,"id":"C3","target":"max-cardinality 1-RQLS(10) or max-cardinality DQLS(6)","sources":["arXiv:2608.29201v2","arXiv:2606.27758v1"],"kill_check":"idempotent list closed by arXiv:2609.24653; target orders unclaimed","risks":["heavy crowding","modest significance"]},
{"rank":4,"id":"C4","target":"graph on <=20 vertices with chi_q < chi_q^(1)","sources":["arXiv:2311.08194 / EJC 32(1) P1.18"],"kill_check":"no claim found","risks":["open-ended search","hard lower-bound certificate"]},
{"rank":5,"id":"C5","target":"((9,13,3))_2 or ((11,5..7,4))_2","sources":["arXiv:2603.19901v1 Table 1 (table gap only)"],"risks":["same family as stalled ((7,3,3))"],"recommended":false}],
"killed":["GUPB: arXiv:2608.12785","UPB minimum: arXiv:2609.05657","C9/C15 uniform mixing: arXiv:2607.28345, arXiv:2607.04207","idempotent QLS 4k+2: arXiv:2609.24653","QLS(7) cardinality spectrum: zenodo.22852779","smallest chi_q<chi: Lalonde"],
"access_holes":["OpenAlex citers HTTP 429","Zenodo API 403","OQP site 500","AME table 404","DataCite metadata-only","partial reads of Huang-Li, Han et al., Johnston-Lovitz"],
"clock":"no shell clock; newest DataCite record seen 2026-10-17T22:36:21Z; last checkpoint read 15:57:09 PDT"}
```
