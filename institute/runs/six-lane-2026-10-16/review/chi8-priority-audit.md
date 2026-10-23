# Random 8-regular (and exploratory 12-regular) colouring: bounded priority and method audit

Recorded 2026-10-17 08:22:54 PDT. Read-only scout `Chi8Priority`; a search miss is not novelty. Raw scout report follows.

---

# χ(G_{n,8}) = 4 and χ(G_{n,12}) = 5: bounded priority and SOTA audit (2026-10-17)

## Summary

- **Explicit prior (slice 1).** The bounded screen found no source that states or implies χ(G_{n,8}) = 4 or χ(G_{n,12}) = 5 for the uniform simple model. This is a search miss, not novelty.
  - The latest rigorous status I found:
    - KPW: {4,5} at d = 8 and {5,6} at d = 12.
    - ACG v4 Table 1: the rigorous bounds leave q = 4 open at d ∈ {7,8,9} and q = 5 open at d ∈ {12,13,14}.
    - COEH: "k = 3, 4 … not solved completely".
  - The 1RSB physics predicts that both graphs are colourable (KPW04 Table I: q = 4, c = 8 COL; q = 5, c = 12 COL).
  - The Pérez-Giménez slides (Utrecht 2012, now read; plus MIPT 2020 and the RS&A 2019 abstract) say nothing about d = 8 or d = 12. The 2012 deck lists "Close the gap" as an open issue.
  - Forward citations (OpenAlex) of KPW (26 citers), ACG (5), COEH-JCTB (28) and AN 2021–2026 (30): nothing relevant.
- **Equivalent method (slice 2).** Lemma A's closed form is a known reformulation; the global-decay step was not found anywhere.
  - [INFERENCE: my identification] The candidate's closed form U(M) = (1−d)log k + (d/2)log(2E_β) equals Φ₁ for the paired interaction B⊗B, evaluated at R = M^{(d−1)/d}. Φ₁ is the ℓ_{Δ/(Δ−1)} reformulation of Galanis–Štefankovič–Vigoda (GSV) and Galanis–Štefankovič–Vigoda–Yang (GSVY).
  - The published uses drop the marginal constraints and rely on Bennett's tensor multiplicativity. That is valid for bipartite graphs (GSV) and for ferromagnetic models on non-bipartite graphs (GSVY; Coja-Oghlan et al. 2022). GSVY's Remark 2 says it fails for antiferromagnetic colourings.
  - The colouring literature instead bounds the regular-graph second moment by the Erdős–Rényi function: AM04 §6, KPW Lemma 5, COEH §5. Coja-Oghlan–Loick–Mezei–Sorkin (CLMS) call this "the trick" and say it fails in their antiferromagnetic Ising setting.
  - I found no source that keeps the doubly-stochastic constraint and proves global decay at J via the complete-graph log-Sobolev inequality / hypercontractivity. OpenAlex finds no work citing both Diaconis–Saloff-Coste (D–SC) and any of KPW, COEH or GSV.
- **Counterpoint for the correctness reviewers.** AM04 §6 says its relaxation is "in fact tight". [INFERENCE: my algebra] It is tight only for overlaps that are constant on their support. The χ8 mechanism needs that claim to be false; this is consistent with the χ7 package's control C2.
- **COEH (slice 3).**
  - ε_k is never made explicit, and the paper assumes k ≥ k₀ throughout.
  - Its separability scale κ = ln⁵⁰⁰k/k is about 10^70 at k = 4 [INFERENCE: arithmetic].
  - So COEH implies nothing at (4,8) or (5,12).
- **Significance, if correct:** potentially substantive specialist; major not established. The d = 12 lead uses the same mechanism, so it carries the same priority risk: treat χ8 and χ12 as one contribution. The χ8 route also covers d = 7 [INFERENCE: ln 6 < 2].

## Files

- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/chi7-priority-audit.md`: the earlier audit (AN eq. 12, NPG Theorem 1.2 and its "conceivable" quote, sweeps, holes). I built on it rather than repeating it.
- `…/review/chi8-parent-inputs-v1/PROOF_CHI8.r1.md:1-79` (status, theorem, context, §0 notation) and `:485-514` (§9 priority statement).
- `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random8reg-colour/explore/GENERAL_K_LEAD.md:10-66`: the general-k closed form U = (1−d)log k + (d/2)log(2E_β), the reach table, and the (5,12) constants.
- `…/random8reg-colour/evidence/LOG.md:32-36`: the 2012 slides were surfaced but not read.
- `…/review/colour7-parent-source-screen-v2/acg1812.09691v4.layout.txt:105-135`: ACG Theorem 1.1, the tightness conjecture, Table 1.
- `…/review/colour7-parent-source-screen-v1/kpw0812.2937v1.layout.txt`:
  - 105–107: Theorem 1;
  - 645: "(3.4) is the expression used in [2]";
  - 709–716: Lemma 5;
  - 1035–1060: proof of Lemma 5, which is an inequality only;
  - 1536: Theorem 10.
- `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random7reg-colour/sources/achlioptas-moore-cond-mat-0407278v1.layout.txt`:
  - 338–345: constraint (8);
  - 397–480: §6 "A tight relaxation";
  - 530–537: §7.
- `…/review/chi8-parent-inputs-v1/diaconis-saloffcoste-1996-lsi.layout.txt:2727-2739`: D–SC Theorem A.1.

## Architecture

KPW's framework is the pairing model plus small subgraph conditioning on balanced colourings. Its second-moment estimate S₂ uses Lemma 5, which is the AM04 relaxation of the regular-graph exponent to the Erdős–Rényi / AN function, plus AN's maximisation over doubly stochastic matrices.

The candidate replaces Lemma 5 + AN with two steps:
- **Lemma A:** weak duality at fixed overlap. The multiplier β log m with β = (d−1)/d cancels the entropy. This is the same R ↔ α map as GSV/GSVY's Φ.
- **Theorem C:** row reduction to F_k, then D–SC's log-Sobolev constant and Gross's hypercontractivity give the condition d < 1 + e^{4−8/k}.

Where the neighbouring work sits:
- AN eq. (12) and NPG: the sharper constant, for G(n,m) and random lifts.
- COEH: large k, "good" colourings.
- GSV/GSVY: matrix norms, bipartite or ferromagnetic only.
- CLMS: says the Erdős–Rényi bound is lossy, and switches to spatial mixing.
- ACG and KPW04: the lower bound and the physics prediction.

## Report

### 1. Theorem applicability

Reference values: the candidate's route needs d < 1 + e^{4−8/k}, i.e. d < 8.389 at k = 4 and d < 12.023 at k = 5. Arithmetic is mine unless quoted.

| Source (version) | Model / variable | At (k,d) = (4,8) | At (5,12) | Implies target? |
|---|---|---|---|---|
| KPW Thm 1 (0812.2937v1) | uniform simple; balanced; Lemma 5 + AN | χ ∈ {4,5} (k = 5; 7 log 4 = 9.70 > 8) | χ ∈ {5,6} (k = 6; 9 log 5 = 14.48 > 12) | No |
| AM04 (cond-mat/0407278v1) | configuration model; Erdős–Rényi relaxation | {4,5,6} | {5,6,7} | No |
| Shi–Wormald CPC 2007 (abstract only) | uniform; algorithmic | {4,5} | d ≤ 10 only | No |
| AN Thm 7 + eq. (12) | G(n,m); balanced | needs c = 4 < 3.708: fails | needs c = 6 < 5.915: fails; AN's cap c < c₄ + 1 = 6.545 does not rule out this route | No (wrong model and range) |
| NPG Thm 1.2 (2109.13347v1) | random lifts of loopless graphs; strongly equitable colourings | ℓ₄ = 7.416 < 8 | ℓ₅ = 11.83 < 12 | No |
| COEH Thm 1.1 (1308.4287v1) | uniform; good/separable colourings; k ≥ k₀ | 6 ln 4 − ε₄ = 8.318 − ε₄, ε₄ not given | 9 ln 5 − 2 ln 2 − ε₅ = 13.10 − ε₅, ε₅ not given | No |
| ACG Thm 1.1 + Table 1 (v4) | uniform; interpolation (lower bounds) | χ > 4 only for d ≥ 10; ≤ 4 only for d ≤ 6 | χ > 5 only for d ≥ 15; ≤ 5 only for d ≤ 11 | No |
| CKPZ (1611.00814) | Poisson G(n,d/n) only | — | — | No |
| Bapst–Coja-Oghlan, *Harnessing the Bethe free energy*, Ex. 3.4 | regular graphs; soft-constraint Potts; d₀(k) not given | — | — | No |
| GSV Thm 1.4 / GSVY Thms 6–7 | bipartite graphs, or ferromagnetic models | — | — | No |
| Molloy–Reed | uniform; first moment | χ ≥ 4 (16/27 < 1) | χ ≥ 5 (729/1024 < 1) | Lower bound only |
| KPW04 physics, Table I | regular graphs; 1RSB, non-rigorous | COL (η not reported) | COL (η not reported) | Predicts both are true |

### 2. Findings (quotes of at most 40 words; scope = what I actually read)

**F1. COEH Theorem 1.1** (counter to any small-k implication). https://arxiv.org/abs/1308.4287, v1 of 2013-08-20; DataCite lists only v1; JCTB 116 (2016) not read. Scope: §1, §2 opening, Definitions 3.1–3.3, §5 opening (extracted text).
> "There is a sequence (ε_k)_{k≥3} with lim_{k→∞} ε_k = 0 such that the following is true. 1. If d ≤ (2k − 1) ln k − 2 ln 2 − ε_k, then G(n,d) is k-colorable w.h.p."

**F2. COEH has no explicit constants** (counter). Same source.
> "(We have not attempted to explicitly extract or even optimize the explicit error term ε_k.)" … "we are going to assume implicitly throughout that k ≥ k₀ for a sufficiently large constant k₀ > 0."

**F3. COEH on small k** (supports openness at k = 3, 4 as of 2013). Same source; [36] is KPW.
> "several papers deal with the k-colorability of random regular graphs for k = 3, 4. This problem is not solved completely by [36] (nor by the present work)."

**F4. COEH's variable and method** (nuance). Same source.
> "The second moment argument for the number Z_{ρ,bal} of balanced k-colorings of G(n,d) carried out in [36] does not work for the (entire) range of d" … "κ = ln⁵⁰⁰ k/k = o_k(1)"

Far-from-J overlaps are handled with AN's G(n,m) function f(ρ) = H(ρ/k) + E(ρ).
[INFERENCE: arithmetic] κ ≈ 2·10^70 at k = 4 and ≈ 4·10^102 at k = 5. κ < 1 needs k ≳ e^{4170}.

**F5. Hetterich, RS&A 2015 abstract** (supports F1–F2). https://www.math.cmu.edu/rsa2015/pdf/41_SamuelHetterich.pdf, read in full.
> "This implies that for every integer k exceeding a certain constant k₀ we identify a number d_{k,col}"

**F6. Pérez-Giménez, Utrecht slides, Sept 2012** (openness in 2012; no d = 8 or 12 claim). https://web.archive.org/web/20250120113200/https://www.math.unl.edu/~xperezgimenez2/talks/chromatic_xperez.pdf, read in full. The OCR dropped "χ"; I restored it.
> "Open Issues: Case d = 5. Are there kangaroos on the moon? Close the gap for χ(G_{n,d}) for general constant d. Can we extend the idea of rainbow balanced colourings?"

The deck's Shi–Wormald table stops at d = 10.

**F7. Pérez-Giménez, MIPT slides, Dec 2020** (nuance). https://web.archive.org/web/20250120132105/https://www.math.unl.edu/~xperezgimenez2/talks/chromatic_lifts.pdf, read in full. It still uses the old threshold, k_d = min{k : d < 2k log k}.
> "Thm (Kemkes, P-G, Wormald 2010): Analogous result holds for uniform d-regular graphs. (Improved by Coja-Oghlan, Efthymiou, Hetterich 2016.)" … "Note: Upper bound on χ(L) is still valid for any d-regular G."

**F8. Pérez-Giménez, RS&A 2019 abstract** (nuance). https://web.archive.org/web/20221102021009/https://ethz.ch/content/dam/ethz/special-interest/math/mathematical-research/fim-dam/Conferences/2019/19th%20Int%20Conf%20on%20Random%20Structures%20and%20Algorithms/Abstracts/Perez-Gimenez_Xavier.pdf, read in full.
> "for fixed d ≥ 3 the chromatic number of a random lift of K_d is (asymptotically almost surely) either k or k + 1, where k is the smallest integer satisfying d < 2k log k."

**F9. Nir, UNL PhD 2020** (nuance: lifts only). https://digitalcommons.unl.edu/dissertations/AAI27956779. I read the abstract only; the full text is campus-restricted.
> "I obtain an upper bound for the chromatic number of random lifts of a general d-regular graph. … This result complements results on the chromatic number of regular graphs chosen uniformly with the configuration model."

**F10. GSV** (method precursor; bipartite). https://arxiv.org/abs/1305.2902, v3 of 4 Nov 2014 (J. ACM 62(6), 2015). Scope: abstract, §§1.3, 2, 3.
> "Let p = ∆/(∆ − 1). For non-negative r, c, define Φ(r, c) by: exp(Φ(r, c)/∆) = r⊺Bc/(‖r‖_p‖c‖_p)." … "Lemma 3.1. max Ψ₁(α, β) = max Φ(r, c)."

The equality is only between global maxima, plus agreement at critical points. A pointwise bound at fixed overlap is not stated in what I read.

**F11. GSV drops the constraints** (method precursor). Same source.
> "Ignoring the four constraints in (13) can only increase the value of (12)" … "for induced norms ‖·‖_{p→q} with p ≤ q it holds … ‖B ⊗ B‖_{p→q} = ‖B‖_{p→q}‖B‖_{p→q}."

**F12. GSVY** (method on non-bipartite random regular graphs, ferromagnetic only). https://arxiv.org/abs/1311.4839, v3 of 13 Sep 2016 (SIAM J. Comput.). Scope: abstract, §§1.2, 3.1, 5.1, Remark 2, §11.3.
> "Φ₁(R) = (∆/2) ln Σ B_ij R_i R_j − (∆ − 1) ln Σ R_i^{∆/(∆−1)}" … "We note that Φ₁ is not a reparameterization of Ψ₁, however they do agree at the critical points."

Its map (20), α_i ∝ R_i^{∆/(∆−1)}, is the candidate's multiplier choice.

**F13. GSVY Remark 2** (counter: the norm route fails for antiferromagnetic colourings). Same source.
> "We will illustrate the necessity of the ferromagnetism assumption in Theorem 6 by giving an example of an antiferromagnetic model for which the second moment method fails … Consider proper 3-colorings of random 10-regular graphs."

**F14. Coja-Oghlan, Galanis, Goldberg, Ravelomanana, Štefankovič, Vigoda, "Metastability of the Potts ferromagnet on random regular graphs"** (nuance: ferromagnetic only). https://arxiv.org/abs/2202.05777 (CMP 2023). I grepped §2 only; version not recorded.
> "these constraints can be relaxed, permitting an elegant translation of the problem to operator theory. In effect, the second moment computation can be reduced to a study of matrix norms."

**F15. CLMS, "The Ising antiferromagnet and max cut on random regular graphs"** (supports: the standard trick is lossy). https://arxiv.org/abs/2009.10483, v2 of 12 Nov 2020 (SIDMA 2022). Scope: §§1.2, 2.1. Their [1] is AM04.
> "A common approach to problems of this type would be the trick of bounding the second moment of random regular graphs by that of the Erdős-Rényi as applied in [1, 13]. Since this approach fails in our case"

and
> "A similar trick has been applied with some success to various random regular graph problems, notably graph colouring [1]."

**F16. AM04 §6** (counterpoint: asserts the relaxation is tight). https://arxiv.org/abs/cond-mat/0407278v1, 11 Jul 2004; pinned layout lines 397–480.
> "relax the constraints, in a manner such that the maximum value remains unchanged" … "Clearly, such βijkℓ also satisfy the original constraints (12), and therefore the upper bound we obtain from this relaxation is in fact tight."

[INFERENCE: my algebra] Take α balanced (rows and columns sum to 1/k). The relaxed maximiser β = (d/p)α_ijα_kℓ, with p = 1 − 2/k + Σα², has row sums (d/p)α_ij(1 − 2/k + α_ij). Constraint (12) therefore holds iff α_ij = Σα² on the support of α, i.e. iff α is constant on its support (J, or permutation-type overlaps). Elsewhere the unique, strictly concave relaxed maximiser is infeasible, so the relaxation is strictly lossy. This agrees with KPW stating Lemma 5 only as an inequality (pinned l.709–716, 1035–1060).

**F17. AM04 §7** (counterpoint / framing). Same file, lines 530–534.
> "Our proof establishes that if X, Y are the numbers of balanced k-colorings of Gn,d and G(n, m = dn/2), respectively, then E[X]²/E[X²] = Θ(E[Y]²/E[Y²])."

**F18. ACG** (rigorous status). https://arxiv.org/abs/1812.09691v4, 19 Oct 2021; pinned lines 105–135.
> "Theorem 1.1. If q ≥ 3 and d ≥ d_q then χ(G(n, d)) > q w.h.p." … "Thus, Theorem 1.1 verifies the lower bound from (1.7), which [44] conjectures to be tight for all q ≥ 3."

Table 1: d_{4,smm} = 6, d₄ = 10; d_{5,smm} = 11, d₅ = 15.

**F19. Krzakala–Pagnani–Weigt physics** (supports that both targets are true; non-rigorous). https://arxiv.org/abs/cond-mat/0403725, v2 of 28 Jul 2004. Table I.
> "q = 4, c = 8 COL | q = 4, c = 9 COL 1RSB | q = 4, c = 10 UNCOL 1RSB | q = 5, c = 12 COL | q = 5, c = 14 COL 1RSB | q = 5, c = 15 UNCOL 1RSB"

[INFERENCE] The route's reach (d ≤ 8 for q = 4, d ≤ 12 for q = 5) matches the last rows of Table I labelled plain "COL" rather than "COL 1RSB" (η and Σ blank in those rows; the paper says the solution is trivial below clustering). This is not evidence.

**F20. Bapst–Coja-Oghlan, "Harnessing the Bethe free energy"** (counter to a hidden small-k corollary). https://arxiv.org/abs/1504.03975 (latest v3, Oct 2015). I grepped only.
> "In this example (3.6) holds with asymptotic equality if either d ≤ d0(k) or d > d0(k) and β ≤ β0(d, k) for certain critical values" … "Definition 3.1 does not accommodate the graph coloring problem"

**F21. Coja-Oghlan et al., "Charting the replica symmetric phase"** (nuance: small-q colouring results exist only for the Poisson model). https://arxiv.org/abs/1704.01043. I grepped only.
> "the condensation threshold in a few special cases such as the random graph q-coloring problem [17], albeit only for q exceeding some (astronomical) constant q0"

**F22. D–SC Theorem A.1** (the component is standard). Pinned layout lines 2727–2739.
> "In particular, for π ≡ 1/|X|, α = (1 − 2/|X|)/log(|X| − 1)."

**F23. Wolff 2007** (context: no ready-made sharper constant). https://eudml.org/doc/284523, abstract only.
> "The optimal hypercontractivity constant for a natural operator semigroup acting on a discrete finite probability space is established up to a universal factor."

**F24. Chang–Kolhe–Sohn 2023** (context: small k is a recognised gap in random CSPs; this is hypergraph NAE-SAT, not graph colouring). https://arxiv.org/abs/2308.02075v1, abstract.
> "Establishing the same for small values of k ≥ 3 remains an important open problem in the study of random CSPs."

### 3. Equivalent-method verdict (slice 2)

1. **The closed form is not new technique.** [INFERENCE] Put R_u = m_u^{(d−1)/d}. Then Σ_u R_u^{d/(d−1)} = Σ m = k, and GSVY's Φ₁ for interaction B⊗B (B = J_k − I_k, i.e. the allowed-pair graph K_k × K_k) equals (d/2)log(2E_β) − (d−1)log k. That is exactly U from GENERAL_K_LEAD §1. What the candidate adds is the pointwise weak-duality inequality at fixed doubly-stochastic overlap (standard Lagrangian duality). GSV/GSVY state only equality of the maxima and agreement at critical points.
2. **The published second-moment uses drop the marginals.** That works in the bipartite case (F11) and for ferromagnetic non-bipartite models (F12, F14). It fails for antiferromagnetic colourings (F13).
3. **Colouring papers use the Erdős–Rényi relaxation** (F15–F17; KPW Lemma 5; COEH f(ρ)). It is strictly lossy away from overlaps that are constant on their support (F16, my inference). No colouring paper I found exploits the constrained gap.
4. **No stronger source was located** for global decay of the exact constrained colouring exponent, for any small k. Co-citation checks: AN ∩ D–SC = 2 unrelated works; D–SC ∩ {KPW, COEH, GSV} = 0.
5. **Distinctions:**
   - Colouring variables:
     - candidate: plain balanced colourings, as in KPW;
     - COEH: good/separable colourings (meaningless at k = 4, 5 by F4);
     - NPG: strongly equitable colourings of lifts;
     - Díaz et al. 2009 (k = 3, d = 5): locally rainbow balanced colourings, conditional on numerics;
     - Heckel's "tame" colourings (2306.07253) concern dense G(n, 1/2) and are irrelevant here.
   - Models:
     - uniform simple G_{n,d} (target): KPW, COEH, ACG, AM04 via the configuration model;
     - random lifts of loopless base graphs: NPG (the bouquet B_d is excluded);
     - G(n,m) or G(n,d/n): AN, CKPZ, Coja-Oghlan–Vilenchik, Rassmann, Bapst–Coja-Oghlan–Efthymiou;
     - bipartite random regular graphs: GSV, Chen et al. 2021, Li et al. 2026.

### 4. COEH small-k check (slice 3)

- ε_k is not given, and the paper assumes k ≥ k₀ throughout (F1, F2). The separability scale κ is astronomically large at k = 4, 5 (F4).
- [INFERENCE] With small ε_k, part 2 of Theorem 1.1 would assert non-4-colourability at d = 9 (8.704 + ε₄). Consistency with the physics prediction "4-COL at d = 9" (F19) needs ε₄ > 0.296. Part 1 reaches d = 8 only if ε₄ ≤ 0.318. The paper gives no such window.
- Conclusion: COEH implies neither (4,8) nor (5,12).

### 5. Significance

"Major" here means a broad new method, a prominent long-standing problem settled, or a SOTA gain under matched assumptions.

- **χ8, if correct:** potentially substantive specialist. It fixes χ exactly at a degree left at {4,5} by Shi–Wormald (2007) and KPW (arXiv 2008), and it is consistent with the physics.
  - The novelty can only sit in Theorem C and in exploiting the regular-model marginal constraint.
  - Lemma A's form is GSV/GSVY-equivalent; D–SC and Gross are standard.
  - The reach is small-k only: 1 + e^{4−8/k} < 1 + e⁴, so for k ≥ 6 the route is weaker than KPW (GENERAL_K_LEAD §2).
- **χ12 lead:** exploratory; it still needs a frozen proof. It shares the mechanism, so present it as one contribution with χ8. The margin is razor-thin (ln 11 = 2.398 < 2.4).
- **Accepted χ7** (AN(12) transfer): a modest extension. The χ8 route would also cover d = 7.
- **Together,** the three would settle 3 of the 6 rigorously open degrees implied by ACG Table 1. d = 9 (q = 4) and d = 13, 14 (q = 5) would remain.
- **Major: not established.**

### 6. Counterpoints and next checks, ranked

1. Have the correctness reviewers confirm that the exact constrained exponent is strictly below the relaxed one at the χ7 C2 witness. That refutes AM04 §6 explicitly and pre-empts the obvious referee objection. If the relaxation were tight, Theorem C at d = 8 would contradict C2.
2. In any write-up, cite GSV (J. ACM 2015) and GSVY (SICOMP 2016) for Φ, CLMS for the "trick", and D–SC/Gross. Never write "first".
3. If budget allows: Semantic Scholar / Google Scholar forward citations of GSV and GSVY filtered for colouring and non-bipartite; the COEH JCTB final text; the Hetterich and Ayre theses; Wormald's publication list.

### 7. Queries completed (2026-10-17; arXiv feed stamps 15:06:19Z, 15:12:46Z, 15:18:24Z)

- **Web searches (17):**
  - Pérez-Giménez slides (×3);
  - Nir thesis (×3);
  - Hetterich thesis (×2);
  - Ayre thesis;
  - "random 12-regular" 5-colourable;
  - "8-regular" "4-colorable";
  - recent small-degree results (past year);
  - Harnessing Bethe;
  - regular occupation problems;
  - hypercontractivity + balanced colouring second moment;
  - induced matrix norm + antiferromagnetic non-bipartite;
  - "G_{n,12}";
  - exact constrained versus relaxed second moment (AM04/KPW);
  - Wormald publication list;
  - Wolff 2007.
- **OpenAlex:**
  - IDs: KPW W2089189975, ACG W2905876360, AN W1978113428 and W2164437357, COEH W2951145705 and W2101851522, D–SC W2077810240, GSV W1986631610 and W2952513650.
  - Citer lists: KPW (26), ACG (5), COEH-JCTB (28), AN 2021+ (30).
  - Intersections: AN ∩ D–SC (2), AN-STOC ∩ D–SC (0), AN with "hypercontractivity" (2), GSV ∩ (KPW ∪ AN) (5), D–SC ∩ (KPW ∪ COEH ∪ GSV) (0), D–SC with "coloring random regular second moment" (3).
  - Sweeps: "chromatic number random regular" since 2019 (26 hits); dissertation search; Pérez-Giménez works since 2019 (8, none on colouring); NPG title search (v1 only; no journal version); Shang 2025 (no abstract).
- **arXiv API:**
  - hypercontractivity AND colouring (1 irrelevant hit, 1312.2915);
  - abs:"random regular" AND colour/chromatic (22 hits, all screened by title);
  - NPG id_list (v1 only);
  - COEH v2 (404).
- **Pages read:** the URLs under F1–F24; Greenhill's publication list (colour/chromatic grep finds only ACG and hypergraph papers); Kemkes's 2009 Georgia Tech abstract (KPW only); Kunisky–Yu (no d = 8 or 12 rows); the KPW authors' preprint via Wayback (grep finds no remark about the relaxation being tight or improvable).

### 8. Access holes

- The UNL site fails TLS ("unable to verify the first certificate"). I used Wayback copies.
- The ETH abstract returns 503 live; I used the Wayback copy.
- Nir's thesis full text is campus-only.
- Wormald's `papers.pdf` returns 503.
- Hetterich's and Ayre's theses were not located.
- Not opened: ScienceDirect versions (KPW Adv. Math., COEH JCTB, Shang 2025); the Springer "Landscape of 21st Century Mathematics" chapters citing AN (title only); O'Donnell's *Analysis of Boolean Functions* and a 2026 spectral-independence paper (both co-cite AN and D–SC; title-screened only).
- Semantic Scholar, Google Scholar and dblp were not used, so citation coverage is OpenAlex only. OpenAlex is on its keyless shared daily budget.

### 9. New relative to PROOF_CHI8.r1 §9

- GSV/GSVY as published equivalents of the closed form.
- AM04 §6's tightness assertion, a counterpoint the proof should address.
- CLMS's statement that the standard Erdős–Rényi bound is lossy.
- COEH's ε_k/k₀/κ details.
- The 2012, 2019 and 2020 Pérez-Giménez talks, now read: no d = 8 or 12 claims.
- Nir's thesis located (abstract only).
- The physics prediction of colourability at q = 5, c = 12.
- ACG's q = 5 gap {12, 13, 14}.
