# PhysicsPriorGapAudit report (verbatim, read-only scout)

Recorded 2026-10-17 15:19:38 PDT. The parent directly read the Ferudun DataCite record (10.5281/zenodo.23430098) and the Nicoară arXiv abstract (math/0404301v1).

**Bottom line.** I found no earlier public claim for any of the six accepted physics results checked (4 gates plus χ8/χ12). I found two attribution gaps the ledger needs to fix, and closed one access hole:

1. **χ(G_{n,8})=4 and χ(G_{n,12})=5:** the method was already public about 10 hours before our route was proposed. An AI-assisted Zenodo preprint uses the same exact-marginal second-moment structure. Our own colour lane had saved it, but neither verdict cites it.
2. **T7 isolation:** a published 2004 theorem (Nicoară, Theorem 3.4) gives the qualitative isolation result once one finite linear-algebra condition is checked at P9. The earlier audit wrongly limited it to the Hadamard case.
3. **T7 access hole closed:** the full Rather 2023 thesis is in the qutrit-sharp lane. It presents P9's isolation only as numerical evidence and the 15/16 bound only as Conjecture 3.3.2.

No mathematical correctness is affected. I have no host clock; the arXiv API timestamps on my queries run from 2026-10-17T22:02:41Z to 22:14:19Z.

## Outcome table

| Target | Earlier match found | Source, version, date | What I read | Does it apply? | Access limits | Ledger correction |
|---|---|---|---|---|---|---|
| Maximum Hypothesis / χ(G_{n,5})=3 | None in scope | — | DataCite: "maximum hypothesis" (89 hits, all off-topic). Phrase sweep: only hit is the EulerSolve K5-lift paper. OpenAlex full text: "maximum hypothesis" with "5-regular" returns only KPW 2009; no citers of Díaz et al. since 2022. EulerSolve live index plus its 626 DataCite records. openai/math `CONTENTS.md`. Newest arXiv papers on random-regular colouring. | EulerSolve OPG-37656 is about 4-regular random lifts of K5. It does not touch Díaz's function F or d=5. | ESA 2005 and JGT 2009 bodies still paywalled; Zenodo files not opened | None. EulerSolve is already disclosed (`CLAIM-r2.md:288`, `colour-priority-audit.md:121`). |
| T7: O9 isolated in the dual (D) and T-dual (T) sets, radius 1 | **No prior answer.** A general theorem nearly implies the qualitative part. | Nicoară, arXiv:math/0404301v1 (2004-04-16), Theorem 3.4. The T7 audit cites J. Operator Theory 2006 as the journal version. | Abstract, Theorem 3.4 and its proof, Lemmas 2.6–2.8, Definition 3.2, §5 | Theorem 3.4 holds for any non-degenerate commuting square. A dual-unitary gate defines Jones's vertex-model commuting square. [INFERENCE] A commuting-square isomorphism there forces two-sided local-unitary equivalence, so the span condition at P9 implies O9 is open in D (and in T via U ↦ US). The span condition is in substance Geng 2022's numerical kernel computation and our exact rank certificate (convention mapping not checked line by line). Nobody publicly verifies it at P9. The radius-1 bound is not implied. | J. Operator Theory version, Nicoară–White JFA 2017 / PAMS 2020 bodies, Krishnan–Sunder 1996 not read | Add Nicoară 3.4 (details below). The gate stands: the target was explicitly open and is answered. Significance stays "modest". |
| T7 thesis access hole | Closed. The thesis gives evidence, not a proof. | Rather thesis (IIT Madras, 2023), all chapters in the qutrit-sharp lane | grep plus targeted reads of ch. 2, 3, 5, 7 | Ch. 2 l.278–280: "Numerics suggest that there are no dual-unitary or T-dual gates in the neighborhood of P9". Ch. 5 l.621–624: "strong numerical evidence". | Not every chapter read in full | Update `dualunitary-t7-parent-verdict.md:36` and `dualunitary-priority-audit.md:71-72` |
| Sharp 15/16 for dual / T-dual gates | None in scope | Thesis ch. 3 l.744–746 (Conjecture 3.3.2) and recommendation l.91–95 | Lakshminarayan/Rather on arXiv (latest 2609.03092, 2605.11076, nothing on 15/16). DataCite qutrit + dual-unitary (19 hits). OpenAlex full text: dual-unitary + qutrit + entangling power (18), 2-unitary + isolated (10). Tan 2601.19677v2; Rudd's Zenodo preprints (22702205, 21971117); planar-maximally-entangled and biunitary arXiv sweeps. | Tan proves AME(4,3) is unique up to local unitaries. Rudd covers product-unitary rigidity of stabilizer AME states. Neither concerns e_p or dual-gate neighbourhoods. | Full texts of Tan, Rudd and the planar-ME papers not read | None |
| Every four MOQLS(7) classical | None in scope | Ball–Simoens 2607.12933 is still v2 (updated 2026-07-27) | Newest arXiv QLS/AME papers (latest 2610.17170, 2026-10-12). OpenAlex full text "mutually orthogonal quantum Latin" since 2026-07-15 (5 hits). DataCite QLS/AME, first 100 records (back to 2026-04-20). GitHub repo search. | Guo's Zenodo 22852779 (2026-09-20) covers cardinalities of single QLS(7), not MOQLS. `carlinbfreades/moqls` is SEO spam. | GitHub code search (needs auth) not used | None |
| χ(G_{n,8})=4, χ(G_{n,12})=5 | **Exact statements: none in scope. Method precedent: not cited.** | Ferudun, "Three-Colourability of Random Lifts of K_5", EulerSolve OPG-37656, doi:10.5281/zenodo.23430098, v1.0, DataCite registered 2026-10-17T04:20:58Z. Unrefereed, AI-assisted. | DataCite record; local text `eulersolve-opg-37656-paper.txt` l.8–17, 43–45, 50–148, 400–438 | Different model (lifts of K5, k=3, d=4), so it implies neither theorem. It already has our structure (mapping below). | Its proof not checked; its source code not read | Corrections below |
| AME(4,6) support bounds 42/46/48 (still active) | No external claim | arXiv 2610.16673v1 (60 terms, lower bound 38), 2610.16882v1 (60), 2610.17170v1 (96) | Pandya repo HEAD `215fd885` (2026-10-13T11:50:15Z) README; Bruzda repo HEAD `eaa668f7` (2026-10-14T19:51:14Z) README; DataCite AME(4,6) + support (14 hits); Ramadas 2512.02749v2 | Ramadas studies q>1 Rényi decomposition entropy for d=2,3,4, not support at d=6. Freeman's Zenodo 23113708 makes no support claim. | The Siegen AME-table host did not resolve (DNS) | None; still partial |
| Five MOQLS(8) (K4/K5 still active) | None | — | Same QLS sweeps | — | — | None |
| Depolarizing capacity (scope only) | Nothing new | Krohn-Grimberghe artifact v1.4 (Zenodo 22097580, 2026-08-25): Q>0 up to per-Pauli p ≤ 0.064956 (total 0.194868) | DataCite record | Already in the verdict, as is Ahmed et al. 2609.39747 | — | None |

## χ8 / χ12: the precedent in detail

**Timeline**
- EulerSolve record registered 2026-10-17T04:20:58Z (21:20:58 PDT, Oct 16).
- [INFERENCE] Our colour lane saved the paper around 2026-10-17T06:10:37Z. This comes from the timestamp in the Cloudflare token of the saved HTML (`eulersolve-opg-37656.html:48`). The same token scheme matches the depolarizing lane's recorded fetch time of 19:30:54 PDT. The saved PDF is listed at `random5reg-colour/README.md:13`.
- The parent proposed the x^{7/8} route at about 06:50–06:55 PDT (`random7reg-colour/evidence/LOG.md:105`, `D8_PILOT.md:3-5`).
- χ8 r1 froze at 07:42:34 PDT, about 10h22m after the EulerSolve registration (`random8reg-colour/evidence/LOG.md:56`).

**Their abstract (DataCite):** "The main ingredient is an exact-marginal edge entropy inequality for pairs of fibrewise balanced three-colourings. A sharp three-coordinate fractional-power inequality yields the edge bound through a spectral absolute-value estimate. This gives the unique global maximum in the degree-four second-moment calculation."

**How their steps map to ours**

| EulerSolve | χ8/χ12 |
|---|---|
| Prop. 3.2: H(B) ≤ (3/4)(H(A)+H(C)) + log Z, with Q ∝ A^{3/4}C^{3/4} | Lemma A: weak duality with multipliers (d−1)/d · log m |
| Lemma 3.1: spectral absolute value plus Cauchy–Schwarz, reducing to row brackets Σx^{3/2} + (Σx^{3/4})² | Lemma 3.1: row function F(r) = S² + Q/2 |
| Lemma 2.1: per-row bound via boundary exclusion and a two-value Lagrange reduction | Proof 2 of Lemma 3.2 (`PROOF_CHI8.r3.md:425ff`) |

[INFERENCE] A unique global maximum plus a non-degenerate Hessian already gives global quadratic decay with some constant. The only load-bearing step that is really distinct is the hypercontractive row inequality at k=4 and k=5, applied in KPW's uniform-model S₂ estimate. Even that step has an elementary interval-arithmetic alternative in our own proofs.

**Small-k applicability check.** None of these covers (k,d) = (4,8) or (5,12) in the uniform model:

| Source | Why not |
|---|---|
| COEH | needs k ≥ k₀; ε_k never given |
| CKPZ 1611.00814, CKM 1802.09311 | all q ≥ 3, but only for the Poisson G(n,p) model |
| Perkins, Bull. AMS 2025 | its condensation results are for G(n,p) |
| Nir–Pérez-Giménez | random lifts; ℓ₄ = 7.42 < 8, ℓ₅ = 11.83 < 12 |
| Bapst–Coja-Oghlan | soft constraints; d₀ not specified |
| EulerSolve | k=3, lifts of K5 |

## Required ledger corrections

**χ8 / χ12**
- `review/chi8-parent-verdict.md:45-47,51` and `review/chi12-parent-verdict.md:9,54,56`:
  - Cite EulerSolve OPG-37656 as the method precedent.
  - Replace "no source proving a constrained global decay step" and "The new step is Theorem C…" with: the distinct step is the hypercontractive quadratic-decay row inequality at (4,8) and (5,12) in the uniform model.
  - The gate can rest only on the new-theorem half of the "materially new theorem/method" clause. That is the parent's call to re-decide.
- `review/chi8-priority-audit.md:19,182-183`: three statements are now wrong — "global-decay step was not found anywhere", "No colouring paper I found exploits the constrained gap", and "no stronger source … for any small k".
- `outcomes.md:9,40,65`: add the precedent and restate the basis for the gate.

**T7**
- `dualunitary-t7-parent-verdict.md:36,38`: the thesis hole is closed (isolation is numerical only). Add Nicoară Theorem 3.4: the qualitative result is a corollary of it once the span condition is checked exactly. What is ours: the exact check, the radius 1, the T-dual case, and the e_p-gap corollary via [44].
- `dualunitary-priority-audit.md:26,67,71-72`: the label "(Hadamard/spin-model case)" is wrong; Theorem 3.4 is for general commuting squares.
- `outcomes.md:55`: add Nicoară to the imports listed for the T7 corollary.

## Not read
- Zenodo record files (only DataCite metadata was used).
- Semantic Scholar and Google Scholar.
- GitHub code search.
- Bodies of: ESA 2005, JGT 2009, Krishnan–Sunder 1996, Nicoară's J. Operator Theory version, Nicoară–White.
- The Siegen AME table (DNS failure).
- Anything on arXiv after 22:14Z.

## Files
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/outcomes.md:9,39-40,55,64-65`
- `.../review/{chi8,chi12,colour-maximum,dualunitary-t7,qutrit-sharp,moqls7,depolarizing}-parent-verdict.md`
- `.../review/{chi8,colour,dualunitary,qutrit-sharp,moqls7}-priority-audit.md`
- `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour/{README.md:13, sources/eulersolve-opg-37656-*}`
- `.../random7reg-colour/{evidence/LOG.md:105-158, review/D8_PILOT.md}`
- `.../random8reg-colour/{evidence/LOG.md:53-56, review/PROOF_CHI8.r3.md:24-28,310-324,754-767}`
- `.../dualunitary-ep15-16/sources/rather-thesis-2023/*.layout.txt`

```json
{"scout_clock":"no host clock; arXiv API stamps 2026-10-17T22:02:41Z-22:14:19Z","writes":"none","results":[
{"target":"Maximum Hypothesis / chi(G_n,5)=3","outcome":"NONE-FOUND-IN-SCOPE","correction":"none"},
{"target":"T7 isolation of O9 in D and T","outcome":"NO-PRIOR-RESOLUTION; GENERAL-THEOREM-NEAR-IMPLICATION","source":"Nicoara arXiv:math/0404301v1 (2004-04-16) Thm 3.4","applicability":"[INFERENCE] vertex-model commuting square of a dual-unitary gate; isomorphism => two-sided LU; span condition at P9 = kernel/tangent check (Geng 2022 numerical; ours exact); radius 1 not implied","correction":"cite Nicoara 3.4; fix audit row 16 scope; gate and significance unchanged"},
{"target":"T7 thesis hole","outcome":"ACCESS-HOLE-CLOSED","source":"Rather thesis 2023, local lane copy, ch2 l.278-280, ch5 l.621-624, ch3 l.744-746","finding":"isolation numerical only; 15/16 conjectural"},
{"target":"sharp 15/16","outcome":"NONE-FOUND-IN-SCOPE","correction":"none"},
{"target":"MOQLS(7) Problem 16 n=7","outcome":"NONE-FOUND-IN-SCOPE","notes":"Ball-Simoens still v2; Guo Zenodo 22852779 is single-QLS cardinalities","correction":"none"},
{"target":"chi(G_n,8)=4, chi(G_n,12)=5","outcome":"NONE-FOUND for exact statements; METHOD-PRECEDENT-OMITTED","source":"Ferudun EulerSolve OPG-37656, doi:10.5281/zenodo.23430098 v1.0, DataCite registered 2026-10-17T04:20:58Z","timing":"~9.5h before parent route (~06:50 PDT); ~10h22m before chi8 r1 (07:42:34 PDT); saved by colour lane (README:13)","applicability":"different model (K5 lifts, k=3, d=4); same exact-marginal weak duality + row reduction + per-row sharp inequality","correction":"cite it; narrow novelty to the hypercontractive decay at (4,8)/(5,12); fix chi8-priority-audit:19,182-183; parent to re-decide gate clause"},
{"target":"AME(4,6) support 42/46/48 (active)","outcome":"NO-EXTERNAL-CLAIM","correction":"none"},
{"target":"five MOQLS(8) (active)","outcome":"NONE-FOUND"},
{"target":"depolarizing (scope only)","outcome":"NO-NEW-CLAIM"}],
"not_read":["Zenodo files","Semantic/Google Scholar","GitHub code search","ESA 2005, JGT 2009, Krishnan-Sunder 1996, Nicoara JOT 2006 and Nicoara-White bodies","Siegen AME table (DNS)","arXiv after 22:14Z"]}
```
