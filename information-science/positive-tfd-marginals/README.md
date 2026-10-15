# 具有明确物理含义且满足边缘条件的非负时频分布的存在性

**Bottom line:** the universal exact-IF reading is impossible, already explicitly explained by primary work in 1994. We supply a finite-energy analytic counterexample and complete written proof. We also give an explicit analytic GD counterexample, the Strassen criterion for one conditional mean, and its exact **density** version (Theorem9; a consequence of known martingale-transport results, reproved). The continuation settles the requested two-sided sufficiency question **negatively for genuine Fourier pairs**: the Schwartz signal \(s=\pi^{-1/4}e^{-t^2/2}(1+\tfrac{i}{14}(4t^4-12t^2+3))\), with \(S=s\), passes both Strassen convex orders at every strike (each one-sided problem even has a density) and the covariance identity, yet admits **no** nonnegative joint measure with both IF and GD (Theorem10, computer-assisted with exact rationals and Arb ball arithmetic). **The book's unrestricted informal “physical meaning” question is not declared solved.** Proofs are classical (one computer-assisted), not Lean/kernel-certified; novelty is not established for the new explicit certificates.

## 1. Source

- Chinese title: **具有明确物理含义且满足边缘条件的非负时频分布的存在性**.
- Authors: **张建国、殷勤业** (西安交通大学电子与信息工程学院).
- Book: 《10000个科学难题·信息科学卷》, 科学出版社, 2011, pp. **452–454**.
- PDF: pp. **473–475**; source SHA256 `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (provided source identifier).
- Images: [452](sources/pdfpage-0473.png), [453](sources/pdfpage-0474.png), [454](sources/pdfpage-0475.png). All three read; formulas checked visually. [Render receipt](evidence/render-receipt.json).

## 2. Problem

### Verbatim key sentences and translation

Book p.453:

> 最后，也是最为重要的，时频分布应该具有明确的物理含义，即能准确地反映信号频率分量随时间的变化情况，这是联合时频分析的主要目标，也是最难保证的性质。

“Finally, and most importantly, the time–frequency distribution should have clear physical meaning: it should accurately reflect how the signal's frequency components change over time. This is the main objective of joint time–frequency analysis and its hardest property to guarantee.”

> 它具有许多对信号分析来说有用的性质，如时间和频率边缘条件、瞬时频率性质与群时延性质等。

“It [the Wigner distribution] has many properties useful for signal analysis, such as time and frequency marginals, the instantaneous-frequency property, and the group-delay property.”

Book p.454:

> 实际上，非负条件是否必要也是一个非常值得探讨的问题，但目前学术界的研究重点仍然是非负时频分布的存在性。

“In fact, whether nonnegativity is necessary is itself a question well worth discussing, but the current research focus remains existence of nonnegative time–frequency distributions.”

> 综上，能反映信号时变特性（具有明确物理含义）的满足边缘条件的非负时频分布（谱）的存在性至今仍然是一个科学难题，该问题的研究不仅对信号处理意义重大，而且也是物理学研究的基本内容。

“In summary, the existence of a nonnegative time–frequency distribution (spectrum), satisfying the marginals and reflecting the signal's time-varying characteristics (having clear physical meaning), remains a scientific difficulty; its study is important both in signal processing and in physics.”

### Fixed modeling choices

Use a nonzero finite-energy complex signal and the unitary Fourier transform, normalized energy laws \(\mu=|s|^2dt/\|s\|_2^2\), \(\nu=|S|^2d\omega/\|s\|_2^2\). This is exactly the book's convention after absorbing its visible \(1/(2\pi)\) factor; see [proof §0](proof.md#0-conventions-and-exact-statements). The literal book object is a two-dimensional density. We separately label the relaxed measure model; impossibility for the latter implies impossibility for the former, but existence does not transfer automatically.

- **M:** nonnegativity plus both exact marginals. The book expressly knows this is achievable and rejects it alone as physical meaning.
- **IF:** \(\mathbb E[W\mid T]=\phi'(T)\). This is a faithful candidate extra axiom because the book explicitly names the instantaneous-frequency property; it is not asserted to be the only meaning of its informal phrase. Use \(s\in H^1\) so the conditional first-moment problem is meaningful.
- **GD:** \(\mathbb E[T\mid W]=-\psi'(W)\), explicitly named in the book. Require \(ts\in L^2\), equivalently \(S\in H^1\).
- **COV:** a universal rule must translate under time shift and frequency modulation, and transform reciprocally under positive time scaling; formulas are fixed in Theorem1. A covariance axiom is a property of a rule over a family, not of an isolated signal.
- **SUP:** weak interval support or strong support (including every internal zero-energy set), interpreted a.e. These add no restriction to nonnegative correct marginals.
- **QUAD:** universal Hermitian quadratic dependence on the unnormalized signal, matching the book's excluded bilinear class. This is distinct from allowing nonlinear signal-dependent kernels.
- **Universal** means one assignment valid for every signal in the stated class, without any gratuitous computability, continuity or quadratic requirement. Analytic means one-sided spectral support. Theorems2–3 use regular finite-energy analytic signals, not ideal pure tones; Theorem10 uses a complex Schwartz signal with two-sided spectrum.
- **Per signal** asks existence for prescribed signal data. Theorems4–6 also discuss abstract marginal/regression data; where those are not certified to arise from a Fourier pair, that limitation is explicit.

Rival readings left distinct: (i) treating “physical meaning” as positive local energy alone; (ii) exact phase-derivative conditional means; (iii) component/ridge tracking after selecting a decomposition, window or prior; (iv) a quantum/operational measurement model; (v) signed quasidistributions. The book supplies no exact error metric, decomposition rule, uniqueness requirement or operational measurement axiom that identifies these readings. None may silently replace the others.

## 3. Status as of 2026-10-14

### Verdict by reading

| Reading | Universal rule: all finite-energy signals / all analytic signals | Per-signal conclusion | Verdict |
|---|---|---|---|
| M alone, optionally COV and weak/strong SUP | Yes / yes, product density, Theorem1 | Always exists | **SOLVED-BY-PRIOR-WORK**; explicitly not the book's sought physical solution |
| M + IF, optionally GD/COV/SUP | No / no on the regular subclasses, Theorem2 | Some fail. Measure criterion \(f_\#\mu\le_{cx}\nu\) (Theorem4); exact **density** criterion: additionally \(f_\#\mu\) gives zero mass to the potential contact set (Theorem9) | **SOLVED-BY-PRIOR-WORK** for universal impossibility; per-signal measure and density criteria **SOLVED-BY-PRIOR-WORK** (Strassen; Beiglböck–Nutz–Touzi 2016 and Nutz–Wiesel 2024), reproved here |
| M + GD, optionally COV/SUP | No / no; explicit analytic counterexample Theorem3 | Exchanged criteria \(g_\#\nu\le_{cx}\mu\) plus the contact-set condition for densities (Theorem9) | **SOLVED-HERE** for the explicit analytic GD certificate (novelty unclear); one-regression criteria are prior work |
| M + IF + GD | No / no, already implied by Theorem2 | Two convex orders and covariance are necessary (Theorem5). They are **not sufficient, even for one genuine Fourier pair** (Theorem10). No exact per-signal characterization beyond the LP/duality restatement, and no analytic-signal counterexample, is established | Universal **SOLVED-BY-PRIOR-WORK**; sufficiency question **SOLVED-HERE (negative, computer-assisted; novelty not established)**; exact classification **OPEN** |
| M + QUAD | No / no, including the analytic subspace, Theorem8 | Quadraticity is not a property of one isolated signal | **SOLVED-BY-PRIOR-WORK**, reproduced proof |
| Exact marginals + IF + GD + COV, allowing signs | Wigner works on Schwartz signals, Theorem7; no claim for phase-undefined general L² signals | Explicit signed representation on that class | **SOLVED-BY-PRIOR-WORK**; shows positivity is not necessary for these algebraic identities |
| M + the book's unrestricted informal “clear physical meaning” | No unique formal statement is specified | Neither IF impossibility nor product existence settles all rival meanings | **OPEN** in this package: not a claim that every conceivable formalization is an open theorem |

“SOLVED-HERE” identifies a complete certificate in this folder, not a novelty claim. “PROVED” below means a classical written proof, not a Lean verdict.

### Dated search log (all 2026-10-14 PT)

1. Read all three book page images, distinguishing equation(5)'s product baseline from the requested local physical meaning.
2. Searched exact titles of Cohen1989, Cohen–Posch1985, and Loughlin–Pitton–Atlas1994; obtained/read the 1994 primary paper through an archived CiteSeerX scan. Its §III-D p.2700 **already states** the analytic-signal negative-IF contradiction. Therefore do not present the universal impossibility as new.
3. Read the primary Loughlin–Tacer1997 paper from a university-hosted PDF; it distinguishes phase derivative from a positive conditional average and derives the out-of-band two-tone example.
4. Read Leskelä–Vihola arXiv:1404.0999v2, definitions and Theorem1.1, verifying the precise finite-first-moment Strassen statement before applying it.
5. Attempts to read Cohen1989 via publisher and CiteSeerX encountered WAF/404. Cohen1995 and Cohen–Posch1985 full primary texts initially not obtained; these are explicitly marked [UNVERIFIED] in [references](sources/references.md), not used to support uninspected theorem/page attributions.
6. The joint-regression sufficiency proposal is disproved by an exact three-point Farkas certificate and a robust absolutely continuous extension. No claim of literature priority, or of a Fourier-realizable counterexample, is made.
7. Publisher-deposited Crossref metadata confirms Cohen–Posch DOI `10.1109/TASSP.1985.1164512` and pp.31–38; its supplied PDF endpoint also returned HTTP418. OpenAlex lists no accessible review copy. The source-access limitation remains, rather than being concealed by secondary quotations. [Machine-readable search log](evidence/literature-search.json).
8. Read Jim Pitton's official 2011 UW talk abstract, which regards adaptive positive TFDs as useful time-varying-energy representations. This is not an exact-IF existence theorem, but it confirms that physical interpretation should not be equated with IF by fiat.
9. Martingale-transport density literature: read Beiglböck–Nutz–Touzi (2016 author PDF) Definition2.2, Proposition2.3, Theorem3.2 and Lemma3.3, and Nutz–Wiesel (arXiv:2401.05209 author PDF) Remark2.2. Together they already imply the one-regression density criterion, so Theorem9 is labelled a reproduction.
10. Two-sided search for the Fourier counterexample: read Spriet–Langrenez–Brummelhuis–De Bièvre (arXiv:2511.01996), Lemma3.9, a **one-sided** state-dependent quantum no-go triggered by anomalous (out-of-range) conditional expectations. Read Cohen (Entropy26:838, 2024) abstract and introduction on local values. An ICASSP1995 abstract surfaced by search (“Instantaneous frequency and time-frequency distributions”, IEEE doc480405) was not readable and is a lead only. No two-sided counterexample on genuine Fourier data was located; this is not a novelty claim.
11. Exploratory Fourier screens and LP relaxations are preserved, including failed and inconclusive runs, in [exploration receipts](evidence/fourier-exploration-receipts.json); none of them is used as evidence.

## 4. State of the art

| Result | Hypotheses and limitation | Primary link | Read? |
|---|---|---|---|
| Positive correct-marginal Cohen–Posch family; strong support | Signal-dependent nonlinear rules; does not ensure phase IF or a unique physical interpretation | [LPA94 §II](https://doi.org/10.1109/78.324735), reproducing CP85 | Yes, LPA94; original CP85 not yet read |
| IF incompatibility with positive marginals | Analytic signal with negative phase derivative; applies beyond bilinear rules | [LPA94 §III-D p.2700](https://doi.org/10.1109/78.324735) | Yes |
| Out-of-band two-component instantaneous frequency | Unequal pure-tone strengths; pure tones themselves are not finite-energy signals | [LT97 §§II–III](https://www.math.ucdavis.edu/~saito/data/phase/loughlin-tacer-97.pdf) | Yes |
| Positive MCE construction and Gaussian chirp example | Feasible moment constraints plus a chosen prior; does not prove arbitrary added IF/GD constraints are feasible | [LPA94 §III](https://doi.org/10.1109/78.324735) | Yes |
| Convex order iff martingale coupling | Borel real probability laws with finite first moments; measures, not automatically densities | [LV14 Theorem1.1](https://arxiv.org/html/1404.0999v2#S1.Thmtheorem1), attributing Strassen1965 | Yes, exact theorem |
| Cohen desirable-property framework | Primary source requested, but full text not initially obtained; no unverified page quotations used | [Cohen1989](https://doi.org/10.1109/5.30749), [Cohen1995](https://dl.acm.org/doi/10.5555/200604) | No full text; [UNVERIFIED] |
| One-regression martingale structure: contact barriers, irreducible components, forced diagonal | Probability laws in convex order on the line | [Beiglböck–Nutz–Touzi 2016, Prop.2.3, Thm3.2](https://www.math.columbia.edu/~mnutz/docs/MOTduality.pdf) | Yes |
| Martingale coupling equivalent to product iff irreducible | Irreducible pairs; cited to BNT Lemma3.3 and proof | [Nutz–Wiesel, Remark2.2](https://www.math.columbia.edu/~mnutz/docs/martingaleSBpotentials.pdf) (arXiv:2401.05209) | Yes |
| Anomalous conditional expectation excludes a Born-compatible joint probability reproducing it | One-sided; finite spectra; range criterion | [Spriet et al., Lemma3.9](https://arxiv.org/abs/2511.01996) | Yes |

## 5. Results

Complete hypotheses and proofs are in [proof.md](proof.md). None of the finite checks substitutes for a universal proof.

| Claim | Status | FRONTIER label | Novelty status |
|---|---|---|---|
| T1: M+COV+SUP has a universal density rule | **PROVED** | Reproduction | Elementary prior art; explicitly in the book |
| T2: \(\operatorname{sinc}^2(t/8)(e^{it}-\tfrac34e^{2it})\) has positive spectral bands but IF(0)=−2 on a positive-energy negative-IF interval; no M+IF coupling | **PROVED** | Certification / Reproduction | Universal obstruction known by1994; finite-energy witness not claimed novel |
| T3: explicit one-sided-spectrum cutoff at L=129 violates the GD Jensen inequality, using rational bounds 273/32768 < 440/32768 | **PROVED** | Certification | Novelty unclear |
| T4: one-regression measure existence iff convex order | **PROVED**, relative to the stated classical Strassen theorem | Reproduction / Certification | Direct application of prior work; no novelty claim |
| T5: two convex orders and matching cross moment are necessary; the cross-moment identity is automatic for regular Fourier pairs | **PROVED** | Reproduction / Certification | Classical Fourier identity; no priority claim |
| T6: those necessary conditions are sufficient | **REFUTED** | Certification | Exact rational certificate: p23+2p31=−1/24; absolutely continuous version ≤−1/48. Novelty unclear; not Fourier-realizable data |
| T7: signed Wigner preserves the selected algebraic marginals/moments | **PROVED** | Reproduction | Classical |
| T8: positive quadratic universal exact-marginal rule | **REFUTED** | Reproduction | Classical no-go, self-contained proof |
| Ten rational LP instances \(r\in\{0,1/8,\ldots,1\}\cup\{2/3\}\), plus Farkas/GD-bound checks | **COMPUTED+VERIFIED** | Certification | Standard-library rational RREF and nonnegative-interval feasibility; no numerical solver |
| T9: one-regression **density** exists iff convex order and zero regression mass on the potential contact set | **PROVED** (self-contained, relative to Strassen) | Reproduction | Consequence of BNT2016 + NW2024 Remark2.2; no novelty claim |
| T10: \(s=\pi^{-1/4}e^{-t^2/2}(1+\tfrac{i}{14}p)\): \(S=s\); both convex orders at every strike, strict, so each one-sided problem has a density; covariance identity; **no** joint nonnegative measure with IF and GD | **PROVED** (computer-assisted) | Certification | No prior two-sided Fourier counterexample located; novelty not established |
| T10 certificates: 301-interval Arb convex-order sandwich plus Sturm-certified bound \(\sup\lvert f\rvert<3.01\) (min margin ≥0.001998); 128-coefficient rational dual with exact corner minimum \(10^{-6}\) and enclosed total \(-0.0057637\ldots\pm4.01\cdot10^{-74}\) (as printed by Arb); chirp controls and mutations | **COMPUTED+VERIFIED** | Certification | Exact rationals / Arb only; floats used for search and sanity only |
| Exact characterization of joint IF+GD existence for Fourier pairs; an analytic-signal counterexample | **OPEN** | — | Not settled here |
| Informal all-purpose physical interpretation | **OPEN** | — | Not uniquely formalized by the source |

## 6. Independent review

The required hostile **Codex gpt-6.1-sol, max** review completed with exit0 in 280seconds, finding **no fatal or major mathematical error** and two minor formulation defects. [Full review](evidence/codex-referee.md), [command/input-hash receipt](evidence/codex-referee-receipt.json).

| Finding | Disposition |
|---|---|
| R1.1: an ordinary Fourier integral does not define the transform for every L² signal | **Fixed:** proof §0 explicitly defines it on L¹∩L² and uses the unitary Plancherel extension on L² |
| R1.2: the product rule need not possess a conditional mean without first moments | **Fixed:** proof T1 now qualifies its conditional-mean statement by the respective finite-first-moment assumption |

The referee explicitly checked all bounds in the L=129 analytic GD certificate, the Strassen pullback, the Fourier covariance sign, both two-regression certificates, and source-faithfulness. No finding was declined. A **second focused review** completed with exit0 in 124seconds and **no remaining findings**: it confirmed both fixes, accepted the new analytic-subspace extension of T8, and independently eliminated the exact LP constraints to obtain feasibility precisely for \(0\le r\le2/3\). [Second review](evidence/codex-referee-2.md), [second command/input-hash receipt](evidence/codex-referee-2-receipt.json). Both runtime headers reported `gpt-6.1-sol`, effort `max`, read-only sandbox. The second review binds the round-2 proof SHA256 `1a341d70720ba10aedd7fd6e873db2314d222502ae26ea0a3c3fd9eae21158a8` (§§0–8); §§9–10 were added afterwards and reviewed in rounds3–4. Review is mathematical advice, not Lean certification or novelty clearance.

**Round3 (Theorem9, one-regression density criterion).** Codex `gpt-6.1-sol`, effort `max`, read-only (runtime header checked), exit0 in 198seconds: **no findings**. It independently verified the countable contact-barrier necessity argument, \(\nu(I)=1\) from atomlessness, the adaptive partition, the intermediate law \(\gamma\), the absolute-continuity direction of the pullback (distinguished from a merely dominating plan), and the Fourier application. [Review](evidence/codex-referee-3.md), [receipt](evidence/codex-referee-3-receipt.json), binding proof SHA256 `c1d13fbb76b3d67e6ed0d8b9537475c3d97a6deaa07af30b17dfa2145670ac52`. The later relabelling of Theorem9 as a reproduction (NW24 Remark2.2) and the §6 cross-reference edit postdate that review; the §9 proof text is unchanged.

**Round4 (Theorem10 and its checker).** Codex `gpt-6.1-sol`, effort `max`, read-only (runtime header checked), static audit, exit0 in 284seconds. Verdict: “Theorem10 is proved as stated, conditional only on correct execution of the audited checker”; **no fatal or major defect**. It re-derived by hand the Fourier invariance and eigenvalue signs, \(E=55/49\), \(f\), \(g=-f\), the covariance identity and \(\mathbb E|f(T)|\); audited `sturm_count`, root isolation, sign sampling, moment recursions, both call functions, Lemma10.1, the formula for \(\Lambda\) including tails, and the chirp formulas. [Review](evidence/codex-referee-4.md), [receipt](evidence/codex-referee-4-receipt.json) (binds proof SHA256 `8f962f85…`, checker `f505a33e…`, certificate `360d701b…`).

| Finding | Disposition |
|---|---|
| R4.1 (minor): rejecting cap \(3\) shows only \(\sup\lvert f\rvert\ge3\), not \(>3\) | **Fixed:** proof §10.1 now gives the exact witness \(f(9/5)=9450000/3143009>3\); the checker asserts it. This diagnostic is not load-bearing; the load-bearing bound \(3.01\) was accepted |
| R4.2 (minor): enclosure radius quoted as \(4\cdot10^{-74}\) but Arb printed \(4.01\cdot10^{-74}\) | **Fixed:** proof and README now quote the printed enclosure |

After round4 the only changes are these two fixes (proof §10 lines on the sup bound and \(\Lambda\), README results row, four checker lines adding the witness) and the dispositions themselves. The checker was rerun after the fix: verdict `true`, identical certificate total and margins ([receipt](evidence/fourier-obstruction-receipt.json)). No round-4 finding was declined.

### Exact computational evidence and parent replay

The requested exact LP search ran once successfully under CPython3.12.12 with no third-party packages. All ten rational instances agreed with the expected feasibility split at r=2/3; the direct linear-combination certificate gives −1/24, the continuous margin −1/48, and the GD Jensen gap is 167/32768. [Outputs](evidence/exact-checks.json), [exact command/source-hash receipt](evidence/exact-check-receipt.json).

Parent replay, without overwriting delivered evidence:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-positive-tfd-marginals/venv/bin/python -B \
  /Users/jinleic/repos/aifours/information-science/positive-tfd-marginals/work/check_exact.py
```

This checks finite rational identities and LPs, not the analytic proofs or source-faithfulness; those remain written/referee evidence.

**Continuation evidence (Theorem10).** The decisive checker is `work/verify_fourier_obstruction.py` (exact rationals, FLINT `fmpq_poly`/Sturm/root isolation, Arb balls at 256 bits; python-flint0.9.0 pinned in `work/requirements.txt`). It ran once with verdict `true`: exact Fourier-invariance and phase-derivative identities, exact normalization and moment identities, the all-strike convex-order certificate, the full-plane dual certificate, chirp feasibility controls with \(\Lambda>0\), and three rejected mutations. [Output](evidence/fourier-obstruction-verification.json), [command/hash receipt](evidence/fourier-obstruction-receipt.json), [certificate](evidence/fourier-certificate.json). An independent floating-point rebuild from SciPy Hermite functions is sanity only: [output](evidence/fourier-sanity.json), [receipt](evidence/fourier-sanity-receipt.json).

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-positive-tfd-marginals/venv/bin/python -B \
  /Users/jinleic/repos/aifours/information-science/positive-tfd-marginals/work/verify_fourier_obstruction.py \
  --certificate /Users/jinleic/repos/aifours/information-science/positive-tfd-marginals/evidence/fourier-certificate.json \
  --entry 0 --output /tmp/positive-tfd-fourier-replay.json
```

**Parent verification completed.** The parent replayed this exact Arb checker into a separate
[output](../evidence/information-science-more-20261014/positive-tfd-fourier-worker-checker-replay.json)
and wrote an independent verifier importing no worker code and using no FLINT/Arb:
[source](../evidence/information-science-more-20261014/parent_verify_fourier_obstruction.py),
[result](../evidence/information-science-more-20261014/positive-tfd-fourier-parent-independent.json),
[receipt and hand-check scope](../evidence/information-science-more-20261014/positive-tfd-fourier-parent-receipt.json).
Its exact Fraction corner/Sturm/identity checks and 60-digit mpmath Gaussian integration
reproduce the certificate total, all 301 convex-order interval margins, positive chirp controls
and rejected mutations. The independent integrals are high-precision reproductions, **not**
interval-certified bounds; the separately replayed Arb checker supplies those bounds.

## 7. Book-level verdict

**Not fully solved under the book's unrestricted wording.** A particularly faithful precise reading—nonnegative exact-marginal distributions must also have the explicitly named instantaneous-frequency property for every analytic finite-energy signal—is fully answered **no**, already by prior literature, with a complete finite-energy certificate here. The GD-only universal reading is also answered no by the explicit analytic construction. Marginals plus covariance/support alone are answered yes but were already known and rejected by the book as inadequate. For one conditional mean, per-signal existence is settled exactly for both measures (Strassen) and densities (Theorem9, known martingale-transport results). For both named conditional means together, the natural per-signal test—both convex orders plus the covariance identity—is proved **insufficient even for a genuine Fourier pair** (Theorem10, computer-assisted). That answers the exact sufficiency question negatively; it does not classify which signals admit both, does not give an analytic-signal example, and does not settle the informal physical-meaning question. It would be misleading to count the broad 2011 book entry as a newly solved scientific problem.

## 8. Next steps

1. Construct an **analytic** (one-sided-spectrum) counterexample. Modulation preserves everything but does not create analyticity; a smooth spectral cutoff keeps the dual certificate robust (it is continuous in \(H^1\) with weights), but the far-tail convex-order comparison of exponentially small quantities must then be controlled.
2. Seek checkable **sufficient** conditions for two-sided existence on Fourier pairs (for example Gaussian chirps, where the Wigner function works), or a structural reason for failure. A duality/LP restatement alone does not count as a classification.
3. Obtain primary Cohen1989/Cohen1995/Cohen–Posch1985 texts for precise historical attribution and a fuller desirable-properties comparison. This does not block the already-read1994 no-go argument.
4. To address a different physical reading, first fix an operational measurement model or component-tracking target and admissible error criterion. Without that choice, “physical meaning” cannot be certified by a theorem about a different axiom set.
