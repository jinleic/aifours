# Physics selection v1 — three-copy Werner endpoint beyond the qutrit claim

Before-creation clock observed: **2026-10-23T12:43:35-07:00**. Owner: PhysicsResearch96h. Contract: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/contract-v1.json`. This freeze authorizes written reasoning only; it is not scientific compute admission.

## Book relationship and non-substitution boundary

The source is *10000 Selected Problems in Sciences: Physics*, Science Press (2009), ISBN 978-7-03-024269-3. The relevant article is **Quantum Channel**, Zhou Xiangfa and Guo Guangcan, book pp. **591–592**, PDF pp. **626–627**. The retained unedited extraction is `physics/evidence/physics-hard-20261015/sources/phys-p0591/excerpt.txt`, with the associated page images. Book p. 592 distinguishes communication resources, entanglement, minimum-output entropy, and the difficulty of evaluating regularized quantum communication quantities. The book PDF identity is recorded in `books/README.md`.

The selected Werner problem is a modern precise question about whether three resource copies can unlock distillable quantum communication. It is **related to**, not equivalent to, the entire book article. A finite-copy Werner theorem would not determine an arbitrary channel's capacity, establish NPT bound entanglement at all copy numbers, or solve a laboratory programme. The depolarizing reserve is more directly tied to the article's minimum-output/additivity discussion; the PPT candidate concerns the strength of an undistillable communication resource.

## Three exact candidates compared

| Candidate | Exact mathematical question | Matched primary baseline and current status | Local overlap / decision |
|---|---|---|---|
| **W4: three-copy ququart Werner endpoint — PRIMARY** | For every complex operator `C` on `(C^4)^{⊗3}` of rank at most two, is `q_3(C) >= 0`, where `q_3(C) = ||C||_HS^2 - (1/2) Σ_i ||Tr_i C||_HS^2 + (1/4) Σ_{i<j} ||Tr_ij C||_HS^2 - (1/8)|Tr C|^2`? An exact negative operator is an equally decisive answer. | Wu–Zou, [arXiv:2608.02647v1](https://arxiv.org/html/2608.02647v1), 31 July 2026, explicitly calls the unrestricted three-copy endpoint unresolved. It proves normal rank-two, fully product-ray, local-overlap-at-most-two, and additional restricted sectors. Bharti–Gajjala–Haug, [2607.24479v1](https://arxiv.org/html/2607.24479v1), proves the two-copy threshold, not three copies. A **4 October 2026 unrefereed qutrit candidate** claims all complex 27×27 rank-two matrices, but expressly disclaims unrestricted higher dimensions. Therefore do not choose/re-certify the qutrit case as a new result. A present-day d=4 openness certificate is not established; status is **UNCERTIFIED-OPEN at d=4**, with a dated containing open statement and explicit competing-claim boundary. | Fresh relative to the last MOQLS8/RQLS10 round. No Werner scientific result occurs in the inspected local lane READMEs or governing v17 report. This is not a replay of held native jobs or a small-code symmetry-class search. Select because a universal inequality or exact rank-two counterexample has a direct operational consequence and written verification path. |
| **D4: four-qubit depolarizing-output majorization — RESERVE** | For every four-qubit density matrix `rho` and `0 <= p <= 4/3`, does the spectrum of `D_p^{⊗4}(rho)` lie below the pure-product output in majorization, with `D_p(X)=(1-p)X+(p/2)Tr(X)I`? | Song–Wang–Tomamichel–Fang, [2609.37240v1](https://arxiv.org/html/2609.37240v1), 29 September 2026, Eq. (2), explicitly conjectures all d,n. Approximate majorization and shifted-log-determinant order are proved, not exact order. Local `depolarizing-majorization-n4/README.md` records all-noise indices `{1,5,11,...,15}`, plus indices `{2,3,4}` at `p >= 2/3`; central indices `{6,...,10}` and low-noise `{2,3,4}` remain. Exact level-one relaxation gaps and unsuccessful level-two/Z-map routes are preserved. | Not fresh to the project and therefore reserve only. Do not recertify the three-qubit theorem or old partial indices. A restart requires an actual analytical representation different from the already-loose PPT hierarchy or Pauli-Gram proposal. |
| **P44: PPT Schmidt number at least three in 4×4 — screened, not active** | Does there exist a 16×16 density matrix `rho` with `rho >= 0`, `Tr rho=1`, `rho^{Γ_B} >= 0`, and Schmidt number at least three? Positive acceptance requires an exact PPT matrix and a proved 2-block-positive witness `W` with `Tr(W rho)<0`; a negative answer must cover every state, not one ansatz. | Krebs–Gachechiladze, [2402.12966v1](https://arxiv.org/html/2402.12966v1), 20 February 2024, explicitly asks about the smallest 4×d system. Johnston–Lovitz, [2609.11849v1](https://arxiv.org/html/2609.11849v1), 10 September 2026, reports a known 4×5 Schmidt-number-three construction and says its new asymptotic result does **not** improve those small-dimensional lower bounds. | Appeared as a reserve in the 17 October local screen, not a completed result. Strong scientific value, but detecting Schmidt number three with a complete exact witness is a larger first missing ingredient than the Werner crossed-Gram problem. Do not replace it by a grid-only exclusion or a low-rank PPT example. |

All three are scoped theoretical questions; **none is claimed to be a full-book solution**. Search misses do not establish worldwide openness or novelty.

## Frozen primary target W4

Let `H=(C^4)^{⊗3}` and use standard, unnormalized partial traces. Prove

`for every C in L(H), rank(C) <= 2 implies q_3(C) >= 0`,

or give an explicitly specified complex rational/algebraic `C` of rank at most two for which the exact value is negative. The operator is not assumed Hermitian, normal, positive, real, permutation invariant, sparse, or confined to any support class. Homogeneity permits `||C||_HS=1` during reasoning but does not change the universal statement.

For `rho_alpha^(4)=(I_16+alpha F_4)/(16+4 alpha)`, direct vectorization yields

`<vec C, ((rho_alpha^(4))^Γ)^{⊗3} vec C> = q_3(alpha,C)/(16+4 alpha)^3`.

At `alpha=-1/2` the denominator is `14^3>0`. The rank of `C` equals the Schmidt rank of its vectorization across `A1 A2 A3 : B1 B2 B3`. Thus nonnegativity is exactly three-copy undistillability of this endpoint state. A proof only at this endpoint is not, without an explicit monotonicity/LOCC bridge, a proof of every alpha. A counterexample would be a finite-copy distillation witness, not by itself an explicit optimal protocol or capacity formula.

### Missing ingredient and first bounded attack

The best written baseline closes normal operators but not general nonnormal two-planes. Its exact remaining condition is a crossed 2×2 Gram determinant for two output and two input rays. Ordinary Cauchy–Schwarz controls a differently crossed product and is insufficient.

The first attack is a **grouped-site switched-Schur representation**: study a two-plane that contains `u=a⊗eta`, where `eta` may be entangled on the other two copy slots. A fully product `eta` is already covered and earns no new result. Derive the exact two-site reference map and determine whether the one-site contraction proof extends to this biseparable reference. This is an attack lemma toward W4, **not a silent replacement of W4 by biseparable states**. If the lemma closes, exhibit operators outside every imported closed sector before claiming strict new coverage, then return to the unrestricted residual.

### Verification path

1. Reconstruct the vectorization identity and every matrix order in the switched complement in written mathematics. Parent checks the complete derivation and the exact quantifiers.
2. For a positive universal candidate: retain the full argument and its dependency map; an independent in-harness reconstruction must check the nonnormal case. Any imported primary theorem is labeled as an import, not authenticated by the act of retrieval.
3. For a negative witness: provide its exact factorization `C=XY†` with two columns, all eight exact partial-trace squared norms, and its direct negative quadratic value. An independent certificate reconstruction is required; no float residual is a certificate.
4. Numerical exploration, if separately admitted, can falsify an overstrong lemma but cannot establish W4. No program, solver, compilation, certificate replay, Lean build, test/lint/formatter suite or model CLI has been launched by this selection.
5. Formal/kernel verification is not presently performed. In-harness review is not human peer review or cross-vendor review. Novelty remains a separate primary-source gate.

### Concrete redirect conditions

- If a newer primary source proves W4 under the same quantifiers, stop calling W4 open and redirect rather than reproduce it as discovery.
- If a proposed switched-Schur extension fails, preserve an exact counterexample to the **lemma** and identify whether it also gives a rank-two Werner witness; do not conflate these conclusions.
- If the first representation reduces only to the existing fully product/local-overlap/normal sectors, it has no strict headroom. Record that obstruction and replace the representation or freeze a numbered successor before changing to D4.
- An unavailable compute/review/source gate is not mathematical exhaustion. Do not restart the old held framework or change accounts/models.

## Source and corpus screen actually exercised

Primary HTML and text extractions of `2608.02647v1`, `2607.24479v1`, `2609.37240v1`, and `2609.11849v1` are retained under `sources/`, with SHA-256 pins in `sources/capture-v1.json`. The relevant source statements were read, not merely their search snippets. The 2024 PPT primary introduction was also directly read. The anonymous qutrit candidate's [public README](https://raw.githubusercontent.com/ipitchford/three-copy-werner-undistillability/main/README.md) was directly read; its certificate and mathematical proof have **not** been replayed or accepted here. Zenodo record/API retrieval both returned HTTP 403; the GitHub statement provided the actual claim boundary.

The full fetched public `openai/math` `CONTENTS.md` is retained as `sources/openai-math-CONTENTS-20261023.md`, SHA-256 `cc7c0b8a1cdedd845a777e77cf682657308503daf8346c1349e06e9259d063c2` (638,727 bytes). Targeted searches for Werner, depolarizing, majorization, Schmidt number, bound entanglement, distillability and positive maps found no direct target entry. Family 272 concerns zero distillable secret key/PPT composition in different dimensions and is **not** a W4 or P44 theorem. The contents screen is not full-text verification of every corpus manuscript. The fetched public header says 719 manuscripts/372 families; no live clone freshness is inferred from older local counts.

ULAM.AI's directly read July 31, 2026 *Obstructions to Werner Distillation* gives separable-spectator and one-/two-copy code-envelope exclusions, plus the block recursion; these are additional baselines, not our discoveries. Its remaining-obstruction wording is not a check of the later qutrit candidate.

### Governing historical boundaries

The closed v17 report, its mandatory operative delivery erratum, and the 22 October evening continuation were read. Their old candidates, unperformed gates, UNKNOWNs and process failures retain their status. All old files remain unchanged. No parentage/soliton/M(7)/two-qutrit result is being repeated. Only the present lane root is writable.
