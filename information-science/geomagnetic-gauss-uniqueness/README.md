# 地磁场测量高斯分析中的唯一性问题

**Outcome:** the principal exact full-vector uniqueness question is **SOLVED-BY-PRIOR-WORK**, not a newly solved open problem. Gauss's 1839 §40 already separates internal/external fields from horizontal plus vertical observations on a sphere; Sabaka–Hulot–Olsen's 2010 review states the uniqueness explicitly. This folder supplies full classical certification proofs, including nonspherical surfaces, stability norms, local-patch continuation, finite-data obstructions, and both scalar-intensity theorems. No Lean/kernel certification or novelty claim is made.

## 1. Source

- Chinese title: **地磁场测量高斯分析中的唯一性问题**.
- Authors: **李玉和、杨建中** (assignment metadata corroborated by the supplied text layer's final attribution; names are on the following reference page, not the two question-page images).
- Book: 《10000个科学难题·信息科学卷》, Science Press,2011, book pp.880–881; PDF pp.901–902 (PDF=book+21).
- Formula-verified images: [p.880](sources/page-0901.png), [p.881](sources/page-0902.png).
- Source PDF: `/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`; assigned SHA256 `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`.
- [Primary-source ledger and read scope](sources/references.md); [complete proofs](proof.md).

## 2. Problem

### Verbatim key sentences (visually transcribed from p.881)

> 但在即使仅存在内源场情形下也必须给出整个地球表面的 U 值或垂直分量 Z 值才能唯一确定整个自由空间的磁场解。

“Even in the case where only internal sources exist, the value of U or the vertical component Z over the entire Earth's surface must be supplied to uniquely determine the magnetic-field solution throughout free space.”

> 仅已知地球表面有限个离散测点的场值，或者仅已知地球表面局部区域的场值，或者仅已知整个地球表面的总强度 F 值都不能唯一确定磁场解，即不能唯一确定全部高斯系数。

“Knowing only the field at finitely many discrete measurement points, or only in a local region of the Earth's surface, or only the total intensity F on the entire surface, cannot uniquely determine the magnetic-field solution, i.e. all Gauss coefficients.”

> 但是，在地磁场的高斯分析中，一般只能获得地表附近闭合曲面（单个边界）的地磁场强度的切向分量及其垂直分量，显然无法满足上述三种边界条件。

“In geomagnetic Gauss analysis, however, generally only the tangential and vertical field components on a closed surface near the Earth's surface (a single boundary) can be obtained; these evidently cannot meet the three boundary conditions above.”

> 如果能够从数学上找到第四类边界条件，能够证明地磁场高斯分析的唯一性，则可在丰富偏微分方程研究体系的同时巩固地球物理研究中的理论基础。

“If a fourth type of boundary condition could be found mathematically, and uniqueness of geomagnetic Gauss analysis proved, this would enrich PDE theory while strengthening the theoretical foundations of geophysical research.”

> 关于唯一性问题，至今仍然还无法从根本上作出合理、完善的解决。

“As for uniqueness, a fundamentally reasonable and complete solution has still not been obtained.”

### Formal readings and modelling choices

The book assumes a scalar potential satisfying Laplace's equation and explicitly displays both internal and external radial powers. We retain both; we do not suppress the external field to simplify the central question. Its Gauss series starts at n=1, excludes magnetic monopoles and leaves potential constants unobservable. The image uses U and external j,k; our proofs use V and standard q,s, with no change of meaning.

| Reading | Exact data and candidate class | Why this is faithful / what is fixed |
|---|---|---|
| **R1, principal** | Full vector B=−∇V on one connected closed C² surface S=∂D, strictly within a connected source-free open region. V=V_i+V_e; V_i harmonic outside a compact inner K and tends to0 at infinity; V_e harmonic on a connected open O containing closure(D). Single-valued potentials, 0∈interior(K), connected relevant exteriors/overlap. | Direct reading of “tangential and vertical” plus the displayed two families. Explicit topology/regularity and source clearance make the mathematical claim definite. “Regular at infinity” is fixed to zero; otherwise V_i has an extra constant gauge. General S need not have genus0. |
| **R1-radial** | Tangent-to-S components plus B·e_r, rather than B·n. | Both meanings of “vertical” are plausible. Strictly star-shaped surfaces give bounded algebraic conversion; general closed surfaces give a transverse patch and uniqueness. Geocentric horizontal+radial components already form the full vector. |
| **R2-vector** | Exact full-vector continuum data on a nonempty open patch Γ⊂S, in the same harmonic class. | One reading of “local region,” not the only one: the preceding book sentence discusses U or Z. Instability explicitly assumes a nonempty unobserved cap; a dense open set is not falsely included. |
| **R2-U/Z, collar** | Internal-only field; just U or just radial Z on an open patch of a sphere; harmonic in a two-sided collar. | Analyticity of the spherical trace gives uniqueness even for one component. Source clearance is an explicit hypothesis, not stated by the book's local clause. |
| **R2-U/Z, exterior-only** | Internal-only, harmonic for r>R, smooth up to r=R, decaying and no monopole, but no harmonic collar; patch leaves an unobserved open set. | Faithful rival reading when sources may reach the boundary. Smooth mean-zero boundary bumps give exact one-component non-uniqueness. |
| **R3** | Arbitrarily prescribed finite observation locations with full exact vector values; no degree cutoff. | Literal discrete-measurement clause. A fixed finite-dimensional model with a full-rank sample matrix is a different reading. |
| **R4∞** | Exact F=|B| everywhere on a sphere; internal-only harmonic potentials with a source-free collar; arbitrary convergent degree. | Matches the book's stronger assertion “even internal only.” Universal sign ambiguity is not the only obstruction: a convergent Backus series supplies non-sign ambiguity. |
| **R4finite** | Same scalar data, but both candidates have finite internal expansions. | The book separately discusses truncated models; their exact mathematical uniqueness is different from infinite expansions and practical conditioning. Uniqueness is modulo one global sign. |
| **R4mixed** | Scalar data with both internal and external sources allowed. | Returns to the displayed general series. Even finite degree1 is nonunique modulo sign. |

**Rival readings not silently settled:** incomplete/noisy measurements do not promise a uniquely recoverable true untruncated field; a missing global potential in a multiply connected region changes the model; sources/currents on S violate the source-free collar; classification of *every* scalar-data ambiguity is stronger than proving non-injectivity; recovery of physical source currents is stronger than recovery of their Gauss coefficients; all-degree continuity without specifying a coefficient norm is not a mathematical stability statement. The book's “Robin” wording actually describes mixed Dirichlet/Neumann pieces; it is not needed to invent a fourth condition, because vector observations supply ordinary Cauchy data.

## 3. Status as of 2026-10-14

| Reading | Verdict | What has been completely decided |
|---|---|---|
| R1 / R1-radial | **SOLVED-BY-PRIOR-WORK** | Yes: V modulo constant, V_i uniquely, V_e modulo constant, all degree≥1 coefficients. Green reconstruction plus Gauss separation; explicit continuity norms and continuation obstructions. |
| R2-vector | **SOLVED-BY-PRIOR-WORK** | Exact uniqueness by harmonic Cauchy continuation; unstable global recovery on a genuine restricted patch. This refutes only the full-vector interpretation of the local clause. |
| R2-U/Z, collar | **SOLVED-BY-PRIOR-WORK** | Exact one-component uniqueness on the analytic sphere, by analytic trace continuation and internal harmonic coefficients. |
| R2-U/Z, exterior-only | **SOLVED-BY-PRIOR-WORK** | Nonunique: explicit smooth boundary bumps and decaying harmonic expansions; a standard exterior boundary-value construction, not a discovery. |
| R3 | **SOLVED-BY-PRIOR-WORK** | No injectivity: dimension N(N+2)>3M gives an exact null field for any M locations. No new theorem is claimed for this elementary linear-algebra consequence. |
| R4∞ | **SOLVED-BY-PRIOR-WORK** | No injectivity even modulo sign: certified convergent Backus dipole-orthogonal series. |
| R4finite | **SOLVED-BY-PRIOR-WORK** | Yes modulo sign in the finite *internal-only* class: Backus1968, rederived in Alberto et al.2004. |
| R4mixed | **SOLVED-BY-PRIOR-WORK** | No: equal-magnitude nonparallel uniform external fields are an elementary finite-degree counterexample, not a discovery. |

Complete classification of arbitrary intensity fibers and optimal noisy inference are **not addressed / not adjudicated**, not declared mathematically open. Physical-current recovery is not an implied uniqueness result: distinct source currents can have identical exterior fields.

**Dated search log:** On 2026-10-14, searched Gauss1839 separation; Backus1968/1970 scalar results; Backus1986; BPC1996; Sabaka–Hulot–Olsen2010/2014/2015; and Holmgren uniqueness. Followed primary publisher/author/journal-archive links, read the passages listed below, and rejected search summaries as evidence. OUP/Wiley and ADS blocked original Backus articles. The 1996 book's authorized Cambridge frontmatter was read visually, identifying relevant section locations, but its theorem bodies were not obtained (Google Books preview also refused access). Those original proofs remain [UNVERIFIED], not silently claimed read. Accessible Gauss translation, the 2010 primary review, Alberto et al.'s full proof/rederivation, and Hörmander's theorem suffice for the verdict. Detailed query outcomes and access caveats are in [sources/references.md](sources/references.md).

## 4. State of the art

| Result / source | Hypotheses and precise location | Primary link | Read? |
|---|---|---|---|
| Gauss1839 internal/external separation | Horizontal+vertical observations on sphere; §40, translated printed pp.40–41; external constant undetermined | [Gauss in 2014 translation](https://hgss.copernicus.org/articles/5/11/2014/hgss-5-11-2014.pdf) | Relevant primary text and formula images read; two typeset missing factors diagnosed, corrected by its preceding equations |
| Explicit one-sphere uniqueness | Source-free shell; radial+colatitudinal components on one sphere; Sabaka–Hulot–Olsen2010 §6.1, pp.525–526, Eqs.121–127 | [Author PDF](https://www.spacecenter.dk/~nio/papers/GEM_TJS.pdf) | Yes; predates2011 book |
| Modern Gauss separation and current-carrying limits | Olsen–Glassmeier–Jia2010 §2.1, pp.136–139, Eqs.1–4; §2.2 | [Author PDF](https://www.spacecenter.dk/~nio/papers/Olsen-2010_SSR.pdf) | Yes, relevant sections |
| Scalar finite internal uniqueness ±; infinite non-sign ambiguity | Alberto–Oliveira–Pais2004 §3.1–3.2, pp.550–551, Eq.22; attributes to Backus1968/1970 | [Published primary PDF](https://repository.geologyscience.ru/server/api/core/bitstreams/af92f7a8-e5be-4ea7-a572-d0c8b542ea1a/content) | Yes; complete certification reproduced here |
| Holmgren-type uniqueness | Analytic-coefficient PDE, noncharacteristic surface; Hörmander1993 introduction pp.1223–1224; C¹ surfaces discussed | [Journal archive](https://www.numdam.org/item/10.5802/aif.1371.pdf) | Theorem statement read; Laplace proof supplied here |
| More general poloidal/toroidal separation | Backus1986, *Rev.Geophys.*24,75–109 | [DOI](https://doi.org/10.1029/RG024i001p00075) | Original403; metadata and primary2010 attribution read; **[UNVERIFIED original proof]** |
| Potential/Helmholtz foundations | BPC1996: contents locate §4.2 “Uniqueness of the Coefficients” p.123, §4.4.1 total-field non-uniqueness p.138, §5.3.4 generalization of Gauss's resolution p.189 | [Cambridge frontmatter](https://assets.cambridge.org/97805214/10069/frontmatter/9780521410069_frontmatter.pdf) | Contents visually read; theorem bodies **[UNVERIFIED]** |

Do not confuse “external field” in Backus1970's title (field outside internal sources) with an externally generated regular field V_e. The finite scalar theorem does not apply to mixed sources.

## 5. Results

| ID / strongest claim | Status | FRONTIER label | Novelty |
|---|---|---|---|
| T1–T3: general Green separation, arbitrary-surface coefficient moments, spherical (2n+1) formula | **PROVED (classical written)** | Certification / Reproduction | Known potential theory and Gauss1839; not new |
| T4: L² data → each coefficient / fixed finite vector Lipschitz; sphere weighted-ℓ² isometry; general-surface stable-side weighted bounds | **PROVED (classical written)** | Certification | Standard consequences, no novelty claimed |
| Eq.11: continuation toward sources exponentially unbounded | **PROVED (classical written)** | Certification | Known ill-posed continuation mechanism |
| T5: radial versus normal vertical measurements | **PROVED (classical written)** | Certification | Linear algebra + classical patch uniqueness, no novelty claimed |
| T6–T7: patch uniqueness and explicit Kelvin-polynomial instability | **PROVED (classical written)** | Certification | Explicit certifying example of known mechanism, not a discovery |
| Exact open-patch full-vector non-uniqueness under the R2-vector assumptions | **REFUTED** | Certification | Only that interpretation is refuted; the book's ambiguous sentence is not universally rejected |
| T7A: one-component spherical patch data with versus without a source-free collar | **PROVED (classical written)** | Certification | Standard analytic-trace and exterior-boundary-value arguments; no novelty claimed |
| T8: finite arbitrary vector samples fail in untruncated class | **PROVED (classical written)** | Certification | Rank-nullity, known obstruction |
| T9: arbitrary finite internal expansions scalar-unique modulo sign, no generic coefficient restriction | **PROVED (classical written)** | Certification / Reproduction | Backus1968 theorem; alternative proof, no novelty claim |
| T10: rational Backus recurrence, convergence on r>1/√3 and genuine non-sign ambiguity | **PROVED (classical written)** | Certification / Reproduction | Backus1970 / Alberto et al.2004 |
| Synthetic ellipsoid recovery and patch decay | **COMPUTED+VERIFIED (floating-point sanity only)** | Empirical evidence | Sanity only; cannot prove uniqueness |

### Empirical contract

The sanity script uses a synthetic mixture of all real spherical harmonics of degrees1–5, deterministic seed20261014, on an ellipsoid with semiaxes(1.1,0.9,1.0). Only B is used by the inverse: first integrate −B·dx along two surface-coordinate paths to recover f modulo a constant, set g=−B·n, then apply the general-surface moment integrals (proof Eqs.4–5). The known potential is used only for error assessment, not provided to reconstruction. Two fixed quadratures (32×64/path40 and48×96/path64) probe discretization error. A separate explicit sequence (proof Eq.13) uses N=2,4,8,16,32,64,128 and observation cap z≤−1/4. All floating-point outputs are Empirical evidence. A short rational recurrence cancellation check is separately labelled COMPUTED+VERIFIED for its finite identities only.

Executed once after implementation: [sanity.json](evidence/sanity.json), [runtime/hash receipt](evidence/sanity-receipt.json), [exact invoked commands](evidence/run-commands.json). CPU threading was capped at1; elapsed numerical runtime1.34s. All70 degree1–5 internal/external coefficients were recovered. The32×64 quadrature gave coefficient relative ℓ² error7.73×10⁻¹⁰; the48×96 quadrature gave1.38×10⁻¹⁴ (maximum absolute error4.11×10⁻¹⁵). Surface-potential recovery modulo a constant had maximum error2.33×10⁻¹⁵ at the finer resolution.

The grids count boundary quadrature nodes, **not all vector-field queries**: recovering the trace by line integration also samples B along surface paths, giving85,248 and302,592 total field evaluations respectively. `sanity.json`'s `vector_observations` field counts only the boundary quadrature nodes. [Explicit accounting](evidence/empirical-data-accounting.json). This is an approximation to a continuum-data reconstruction, not a claim to bypass R3 with finitely many observations.

For the patch sequence, sampled cap maxima at N=8,16,32,64,128 were respectively1.59×10⁻²,3.30×10⁻⁴,1.24×10⁻⁷,1.90×10⁻¹⁴,4.41×10⁻²⁸, while the exact north-pole field magnitude remained≥1/2 (0.5078125 at N=128). The reported analytic-bound evaluations are floating point; the proof's exact bound is the mathematical certificate. All32 finite rational recurrence cancellations were exactly zero using `fractions.Fraction`; this check certifies those finite identities only. No finite table is used as a substitute for the all-degree proofs.

One-command empirical replay from the repository root (write outputs to an authorized replay location):

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-geomagnetic-gauss-uniqueness/venv/bin/python -B information-science/geomagnetic-gauss-uniqueness/work/sanity.py --output /Users/jinleic/jinleic-workspace/scratch/ai4s-geomagnetic-gauss-uniqueness/replay.json --receipt /Users/jinleic/jinleic-workspace/scratch/ai4s-geomagnetic-gauss-uniqueness/replay-receipt.json
```

## 6. Independent review

The required hostile Codex review completed with `gpt-6.1-sol`, reasoning effort `max`, read-only sandbox, ephemeral session, exit0, elapsed700.20s. The actual CLI header confirms that model/effort/sandbox. [Report](evidence/codex-referee.md), [prompt](evidence/referee-prompt.txt), [command and input hashes](evidence/referee-receipt.json). The referee read all proofs and both Chinese question-page images, and found **no FATAL mathematical error in Theorems1–10**, one MAJOR unsupported status label and two MINOR formulation defects. It ran no code or numerical replay; this is independent written-proof review, not kernel verification.

| Finding | Severity | Disposition |
|---|---|---|
| 1: “Not resolved here” was incorrectly labelled OPEN | MAJOR | **Fixed:** removed the combined OPEN row; classification/noisy inference are not adjudicated, and physical-current uniqueness is not claimed. |
| 2: sample locations could lie outside an arbitrary candidate's domain | MINOR | **Fixed:** T8 now requires x_j∈Ω (surface samples in particular); the auxiliary multipole kernel can still be evaluated at all x_j≠0. |
| 3: arbitrary orthonormal basis does not give individual conventional-coefficient rescaling | MINOR | **Fixed:** explicitly select conventional real cosine/sine harmonics for that statement, and state the invertible degreewise basis transformation for any other fixed basis. |
| 4: interpretation depends on exact continuum/source-clearance assumptions | NOTE | **Retained and strengthened:** T7A separately treats the book's plausible U-only/Z-only patch reading, with and without a collar. No blanket refutation of the ambiguous local clause. |
| 5: connectedness, global potential and gauges sufficient | NOTE | Retained unchanged. |
| 6: Green signs, moments and 2n+1 separation correct | NOTE | Retained unchanged. |
| 7: continuity weights correct; monopole would add a term | NOTE | Made the no-monopole restriction explicit beside Eq.9, with the optional |δI_00|² term stated. |
| 8: radial/normal conversion and transverse patch valid | NOTE | Retained unchanged, including no unsupported global conditioning claim. |
| 9: Cauchy zero extension valid | NOTE | Retained unchanged. |
| 10: Kelvin sequence and unobserved-cap qualification valid | NOTE | Retained unchanged. |
| 11: finite scalar proof includes nongeneric coefficients | NOTE | Retained unchanged. |
| 12: Backus recurrence/convergence valid; not every prescribed smaller source ball | NOTE | Retained the explicit a>1/√3 source radius and existential non-injectivity claim. |
| 13: prior-art verdict supported; original Backus/BPC bodies unread | NOTE | Retained transparent access limits; no invented original theorem citations. |
| 14: classical proof and empirical evidence separate | NOTE | Retained; no numerical output promoted to a universal theorem. |

The first receipt pins the launch snapshot. README/source metadata and empirical results were added during that review (the report acknowledges them); its proof snapshot stayed unchanged until the findings arrived. The fixes above and added T7A were independently checked in a second focused review: [report](evidence/codex-referee-round2.md), [prompt](evidence/referee-round2-prompt.txt), [receipt](evidence/referee-round2-receipt.json). The second run used the same model/effort/read-only settings, exited0 in173.47s, and returned **“ACCEPT this revision as a classical written-proof package”**, with **no remaining FATAL, MAJOR or MINOR defects**. Its six NOTE findings confirm, respectively: fixes1–3; Eq.9's monopole term; collar trace uniqueness; bump coefficient/derivative convergence; counterexample admissibility and absence of a collar; and the conditional book interpretation. All six are retained without further mathematical changes.

The final proof is exactly the second-review proof snapshot. Subsequent README changes only record the returned review and clarify empirical field-query accounting; neither adds a theorem. No human-journal or Lean/kernel certification is claimed.

## 7. Book-level verdict

**Under the most direct exact-data reading of the book's proposed fourth-boundary-condition question, the answer is complete and classical: full tangential plus vertical field observations on one closed source-free surface determine the magnetic field and its internal/external Gauss coefficients (apart from an irrelevant potential constant). It is SOLVED-BY-PRIOR-WORK, not SOLVED-HERE.** The local clause is ambiguous: full-vector continuum data are unique; internal-only U/Z patch data are unique with a harmonic collar on the sphere but nonunique in the exterior-only smooth-boundary class. Thus we do not declare the book's local sentence universally false. Finite-point and unrestricted scalar-intensity non-uniqueness are correct; finite internal expansions instead are scalar-unique up to sign. Broad physical interpretation, source-current inversion, incomplete/noisy inference, and classification of all scalar ambiguities are not claimed solved. No new full solution of a previously open problem is counted.

## 8. Next steps

For the exact R1–R4 questions there is no remaining mathematical existence/uniqueness obligation in the stated models. A human specialist could check the classical proof package and the book interpretation. If historical attribution rather than theorem correctness is required, obtain authorized copies of Backus1986 and BPC1996 and inspect their original theorem locations; these inaccessible originals are not needed to support the present verdict. Any practical noisy-data claim needs a separately specified noise model, source-distance bounds and regularization objective, not an assertion that uniqueness implies numerical recoverability.
