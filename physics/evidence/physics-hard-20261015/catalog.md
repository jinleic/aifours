# Physics volume: difficult-problem screen for a 6-hour run (2026-10-15 PT)

Volume: 《10000个科学难题·物理学卷》 (Science Press 2009, ISBN 978-7-03-024269-3), 876 PDF pages, 301 articles
(inventory `research-institute/explorer/inventory/phys.json`). PDF sha256 `a4524a2f…631193f` (checked).
Selection only; nothing here is an attack result. Status words: solved / partially-solved / open / claimed
(preprints and corpora are claims). "Opened (scout)" means a read-only scout subagent opened the primary
page and reported it in this session; everything else marked opened was opened by me. [UNVERIFIED] = lead not opened.

## (a) Method, inputs, query log

1. **Whole-volume title screen (301/301).** Listed every inventory article. Marked the 10 `ai4s-owned.json` ids
   (p0333, p0348, p0350, p0464, p0526, p0541, p0601, p0688, p0798, p0814) and the cited solved-elsewhere rows of
   `ai4s-crosswalk-20261014.json` (41 physics entries). I read `physics/README.md` and `PHYSICS_RESELECTION.md`.
   Most articles are programmatic, experimental, device, astrophysics or conceptual surveys with no exact
   mathematical object. I dropped these at title level. `catalog.json` gives every id a disposition.
2. **Text screen (about 40 articles).** I scanned the text layer of every article whose title could hide an
   exact object, bound, threshold, solvable model or classification. That covers the earlier too-hard list
   plus p0073, p0095, p0101, p0352, p0354, p0364, p0381, p0422, p0457, p0489, p0491, p0568, p0578, p0580,
   p0586, p0591, p0595, p0597, p0613, p0618, p0627, p0741, p0766, p0768, p0810, p0819, p0827 and p0835.
   For each I extracted the sentences that pose a question.
3. **Page images.** The quotes for the two retained articles (p0422 at PDF 455–460, p0591 at PDF 626–627)
   were read from 150-dpi renders; copies are in `sources/`. For p0073 I used only the text layer, because
   that article was not retained.
4. **Status checks** (2026-10-15 PT).
   - Opened by me (arXiv abstract/PDF unless noted):
     - 3-SAT bounds: Vorobyev 2610.10599 (abstract and PDF); Díaz–Kirousis–Mitsche–Pérez-Giménez
       0807.3600; Hajiaghayi–Sorkin math/0310193; Achlioptas–Peres cs/0305009v2 (PDF bounds table);
       Achlioptas–Menchaca-Méndez ICALP 2012 (author PDF).
     - Depolarizing channel: Ahmed et al. 2609.39747; Krohn-Grimberghe 2608.15870.
     - Other: Leung–Smith 0810.4931; Hastings 0809.3972; Troyer–Wiese cond-mat/0408370.
     - openai/math preprint "Computing the Random 3-SAT Threshold" (local PDF).
   - Opened by two scouts and reported to me:
     - 3-SAT side: Mertens–Mézard–Zecchina cs/0309020; Ding–Sly–Sun 1411.0650v3;
       Panchenko–Talagrand 2004 (arXiv v1); Mézard–Zecchina cond-mat/0207194; Lundow–Markström 1712.04888;
       Maneva–Sinclair 0710.0805; Hugel–Boufkhad 1002.1636; ESA 2025 (LIPIcs 351:103); the Vorobyev Lean repo.
     - Depolarizing side: Fern–Whaley 0708.1597; Bausch–Leditzky 1910.00471 and 1806.08781;
       Agarwal et al. 2605.09138; Kianvash–Fanizza–Giovannetti 2008.02461; Leditzky–Datta–Smith 1701.03081;
       Fanizza–Kianvash–Giovannetti 1911.01977; Wang 1912.00931; Kondra et al. 2608.01308.
     - Effect algebras: Liu–Wu 0812.0630; the Gudder–Latrémolière preprint.
5. **Query log** (scouts and me, 2026-10-15). English queries:
   - "Díaz Kirousis Mitsche Pérez-Giménez 4.4898" and "random 3-SAT improved upper bound below 4.4898"
   - "random 3-SAT lower bound improved above 3.52" and "random 3-SAT satisfiable with high probability density 3.6"
   - "interpolation method random 3-SAT upper bound computer-assisted"
   - "random 4-SAT … upper bound improved below 10.23" and "random 4-SAT threshold rigorous upper bound 2026"
   - "Lelarge Oulamara replica bounds k-SAT" and "Achlioptas Menchaca-Mendez energetic interpolation 4-SAT"
   - "depolarizing channel quantum capacity threshold 2026" and "symmetric subspace Gaussian limit coherent
     information depolarizing channel"
   - "Tanaka Tasaki metallic ferromagnetism rigorous example"

   Chinese queries: "随机3-SAT 相变点 严格上界", "3-SAT 可满足性阈值 上界 4.4898",
   "随机3-SAT 阈值 4.2667 严格证明 下界 改进 2025", "退极化信道 量子容量 阈值 下界",
   "量子信道容量 相干信息 超可加性 退极化".

   Citation screens: the 40 OpenAlex citers of the Díaz–Kirousis–Mitsche–Pérez-Giménez TCS paper, and the
   10 newest arXiv "random 3-SAT threshold" abstracts. A search miss is a dated result, not proof of openness.

   Later k ≥ 4 checks (me, 02:40 PT):
   - I grepped the full texts of Díaz et al. 0807.3600, Hugel–Boufkhad 1002.1636 and Maneva–Sinclair 0710.0805.
     None gives k ≥ 4 upper-bound values.
   - A one-month web search for k = 4/5 bound improvements found only Vorobyev (k=3) and Carenini's window
     paper, arXiv:2609.26222 (opened; window sizes, no numeric bounds).
6. **openai/math.** I checked the local clone (235 `lean/docs` titles, `CONTENTS.md`, preprint names) and the
   remote `main` `CONTENTS.md` fetched on 2026-10-15.
   - SAT-related: family 235, "Limiting random SAT thresholds, sharp variance and computability". It claims a
     limiting threshold for every k ≥ 3, credits Carenini, ECCC TR26-229 [UNVERIFIED], with priority, and
     claims that the 3-SAT threshold is computable. It gives **no explicit numerical bounds**.
   - Family 221 (Mézard–Parisi formula) is for even-arity diluted models.
   - There is no depolarizing or quantum-capacity family. Family 276 concerns the classical capacity of
     generalized amplitude damping, a different question.
7. **Feasibility probes** (≤5 min each; floating point; **not certificates**). Scripts:
   - `/tmp/ai4s-hard/phys/probe_fact1rsb.py`: ran on the workspace venv before `scratch/` disappeared.
   - `/tmp/ai4s-hard/phys/probe_k_np.py`: Homebrew python3 with numpy.

   Both evaluate the single-rate energetic trial functional Φ defined under candidate #1.
8. **Runtime incident.** `/Users/jinleic/jinleic-workspace/scratch/` disappeared between 02:27 and 02:31 PT
   (confirmed absent at 02:31). I did not recreate or touch it. Nothing in this directory depends on it.

## (b) Difficult problems found (status checked 2026-10-15 PT)

Budget classes are 6h-scoped, multi-day or not-boundable. Plausibility values are [INFERENCE].

| id | zh title | authors | book (PDF) pp. | question | status (key source) | budget | plausibility |
|---|---|---|---|---|---|---|---|
| phys-p0422 · C5-k≥4-upper | 用统计物理学方法处理约束满足问题面临的五个挑战 | M. Alava, E. Aurell, 周海军 | 422–427 (455–460) | Rigorous upper bounds for random k-SAT, initially k=4,5 | No later improvement located in the dated screen; comparison entries 10.23 / 21.33 in the opened Achlioptas–Peres table. Recover each original source/model before claiming improvement; Vorobyev treats k=3 only. | 6h-scoped visit, including ≤4h attack | speculative [INFERENCE]; the general-k analytic bridge is unproved here |
| phys-p0422 · C5-3SAT-upper | same | same | same | Rigorous upper bound on the 3-SAT threshold | **claimed** 4.268 (Vorobyev 2610.10599, Lean-formalized preprint, opened). Published 4.4898 (0807.3600, opened). Headroom to cavity 4.26675 ≤ 0.0013 | 6h-scoped (tightening) | low–medium |
| phys-p0422 · C5-3SAT-lower | same | same | same | Rigorous lower bound on the 3-SAT threshold | **open**. 3.52 (Hajiaghayi–Sorkin math/0310193, opened; Kaporis–Kirousis–Lalas 2006 [UNVERIFIED body]) | multi-day / not-boundable | very low |
| phys-p0422 · existence | same | same | same | Does the k=3 limiting threshold exist? (text, not a numbered challenge) | **claimed**: Carenini ECCC TR26-229 [UNVERIFIED]; openai/math family 235 (opened) | — | — |
| phys-p0422 · C1–C4 | same | same | same | Theory of focused local search, landscape, SP failure, efficient unsatisfiability certificates | **open**; not precise (C4 is near Feige-type refutation hardness) | not-boundable | — |
| phys-p0591 · Q-threshold | 量子信道 | 周祥发, 郭光灿 | 591–592 (626–627) | Quantum capacity of noisy channels; instance: depolarizing zero-capacity threshold p* | **open**. Known 0.194868 ≤ p* ≤ 1/4 (certified explicit code, Krohn-Grimberghe 2608.15870, opened; antidegradability). **Claimed** p* ≥ 0.2029161 (Ahmed et al. 2609.39747, floating point, asymptotic). Peer-reviewed best ≈ 0.19130 (Fern–Whaley, opened by scout) | 6h-scoped | medium (explicit certified) / low (asymptotic) |
| phys-p0591 · Q-upper | same | same | same | Upper bounds on Q(N_p) for 0 < p < 1/4 | **open**. Best: Kianvash–Fanizza–Giovannetti, Quantum 6, 647 (2022) (opened by scout) | 6h-scoped | low |
| phys-p0591 · additivity | same | same | same | Is the Holevo quantity additive? | **solved** (false): Hastings 0809.3972 (opened) | — | — |
| phys-p0591 · continuity | same | same | same | Is quantum capacity continuous? | **solved** (yes): Leung–Smith 0810.4931 (opened) | — | — |
| phys-p0578 | 量子信息中的数学问题 | 杜鸿科 | 578–579 (611–614) | Uniqueness of the sequential product on E(H); extreme points of quantum operations; dual quantum computers | Sequential product: **solved** (not unique; Liu–Wu 0812.0630, opened by scout), unique under extra axioms (Gudder–Latrémolière 2008). Other items: suggested topics, not precise | ill-posed | — |
| phys-p0073 | 金属铁磁性的起源 | 田光善 | 73–80 (108–115) | Lieb's problem: rigorous metallic ferromagnetism in a "reasonable, not over-artificial" Hubbard model | **partially-solved**: Tanaka–Tasaki, PRL 98, 116402 (2007), rigorous example on a special lattice [UNVERIFIED; search snippet only] | not-boundable | — |
| phys-p0081 | 量子蒙特卡罗模拟中的负符号问题 | 张世伟, 赵汇海, 向涛 | 81–85 (116–120) | General polynomial-time removal of the QMC sign problem | **open/obstructed**: NP-hard in general (Troyer–Wiese cond-mat/0408370, opened) | not-boundable | — |
| phys-p0488 | 三维多体模型的精确解 | 孙鑫 | 488 (521) | Exact solution of 3D models (3D Ising, etc.) | **open** [INFERENCE] | not-boundable | — |
| phys-p0457 | 自旋液体是否存在？ | 寇谡鹏 | 457–458 (490–491) | Existence and model of an SU(2)- and translation-symmetric spin-liquid ground state; J1–J2 | **partially-solved**: exactly solvable SU(2)-symmetric models exist, e.g. Yao–Lee 2011 [UNVERIFIED]; J1–J2 open | not-boundable | — |
| phys-p0352 | Yangian 表示论与求解非线性模型 | 白承铭, 葛墨林 | 352–353 (385–386) | Obtain the Hubbard and Haldane–Shastry spectra from Yangian representation theory alone | Haldane–Shastry: **solved** (1992, per README). Hubbard: **open**, ill-defined deliverable | not-boundable | — |
| phys-p0354 | Navier-Stokes 方程和 Euler 方程的与自然灾害相关的环流解 | 楼森岳, 黄菲 | 354–355 (387–388) | Analytic "typhoon-like" circulation solutions of the 3D Euler/NS and baroclinic PV equations | **open** but ill-posed ("typhoon features" undefined) | multi-day / ill-posed | — |
| phys-p0810 | 声子热传导的微观机制及低维材料的热传导规律 | 赵鸿, 张勇 | 810–811 (849–850) | Derive Fourier's law; 1D anomalous exponent | **open**; numerics are not certifiable | not-boundable | — |
| phys-p0819 | 轨道扩散与太阳系稳定性 | 孙义燧, 周济林 | 819–820 (858–859) | Stability of the Solar System; Arnold diffusion | **open** | not-boundable | — |
| phys-p0163 / p0806 / p0808 | 湍流 (three articles) | 佘振苏; 张健, 何国威; 唐少强 | 163–174; 806–809 | Turbulence | **open** | not-boundable | — |
| phys-p0768 / p0766 | 量子场论的严格解 / 量子场论中的基本问题 | 王青 / 吴岳良 | 768; 766–767 | Exact solutions and foundations of QFT | **open** | not-boundable | — |
| phys-p0310 | 超弦理论的基本表叙和有限性 | 朱传界 | 310–311 | Finiteness of superstring perturbation theory | **open** [INFERENCE] | not-boundable | — |
| phys-p0533 / p0537 / p0474 | 高温超导机理 (three articles) | 封东来; 冯世平, 张酣; 李建新 | 533–538; 474–475 | High-T_c pairing mechanism | **open** | not-boundable | — |
| phys-p0597 | 量子算法和量子计算的复杂性 | 刘旭峰 | 597–598 | Power of quantum computation versus classical | **open** (BQP vs NP-type) | not-boundable | — |
| phys-p0595 | 量子相变与量子纠缠中的一些有待解决的问题 | 顾世建, 林海青, 李有泉 | 595–596 | Universal entanglement theory of QPTs; classification | not precise | ill-posed | — |
| phys-p0471 / p0489 / p0491 | 拓扑序普适性 / 量子相变和拓扑有序 / 量子混沌 | 寇谡鹏; 张广铭; 王晓光 | 471–472; 489–492 | How to characterize these phenomena | not precise | ill-posed | — |
| phys-p0246 / p0278 / p0759 | 时空四维 / 黑洞熵 / 规范等级 | various | — | Foundational high-energy questions | **open** | not-boundable | — |

Excluded as owned or settled: the 10 ai4s-owned ids above, plus p0642 and p0662 (2019 SI redefinition) and the
p0591 additivity item (Hastings).

## (c) Top 3 candidates for a 6-hour run

Source folders: #1 and #3 share `sources/phys-p0422/` (PDF 455–460); #2 uses `sources/phys-p0591/`
(PDF 626–627). Each folder holds 150-dpi PNGs and an `excerpt.txt` with a header.

Runtime note: `probes/probe_k_np.py` needs only numpy. The parent reports that the research-explorer venv,
`~/.local/state/research-explorer/venv`, has numpy and mpmath.

### #1 — phys-p0422, Challenge 5: certified upper bounds on the random k-SAT threshold for k = 4, 5 (6, 7)

**Verbatim (book p. 426 = PDF 459, checked against `sources/phys-p0422/csp-459.png`):**
> 根据 Guerra 的工作，1RSB 积分方程的精确解将给出满足/不满足相变点的一个严格的变分上下限[9]。……许多分析及数学物理中的数值模拟方案通过一些技巧(如区间代数法等)都能够给出一些严格的上下限。……
> 面临的挑战 5　如果以上提到的技巧(或者其他技巧)可以有效地用于种群动力学模拟，那么这必将极大程度增进对 K-SAT 问题的满足/不满足相变点和其他相变点的上下限的严格计算。这将会成为理论计算机科学的一个非常重要的成果。

**Translation:** "By Guerra's work, the exact solution of the 1RSB integral equations would give a rigorous
variational upper/lower bound on the SAT/UNSAT transition point [9 = Franz–Leone 2003]. … Many numerical
schemes in analysis and mathematical physics can give rigorous upper and lower bounds through techniques such as
interval arithmetic. … Challenge 5: if these techniques (or others) can be used effectively in population
dynamics, they will greatly advance the rigorous computation of upper and lower bounds on the SAT/UNSAT and other
transition points of K-SAT. That would be a very important result for theoretical computer science."

**Formal statement.**
- Target model. F_k(n,m) has m independent clauses, each using k uniformly chosen distinct variables
  and independent fair signs. Achlioptas–Peres initially allow repeated literals; their table cites
  other upper-bound sources. Recover the original source/model and prove each needed transfer with
  explicit losses before making a comparable-improvement claim.
- C_k(a) means: lim_{n→∞} P[F_k(n, ⌊an⌋) is satisfiable] = 0.
- Known: C_k(a) holds for a ≥ U_k, with U_4 = 10.23, U_5 = 21.33 and U_7 = 87.88. I opened no k = 6 value;
  the first-moment bound is ln 2 / (−ln(1 − 2⁻⁶)) ≈ 44.01 (computed).
- **Target:** prove C_k(a_k) for explicit rationals a_k < U_k, for k = 4 and 5 and, if time permits, 6 and 7.
- **"Solved" for this run** means three things: a written general-k energetic interpolation theorem, an exact
  rational certificate for each a_k, and an independent verifier replay. The exact threshold values stay open.
  If 1RSB is exact, the method cannot go below the cavity values 9.931, 21.117, 43.37 and 87.79.

**SOTA baseline.**
- Upper bounds: [Achlioptas–Peres, JAMS 17 (2004), arXiv cs/0305009v2, table on p. 2](https://arxiv.org/pdf/cs/0305009v2),
  opened: 10.23 (k=4), 21.33 (k=5), 87.88 (k=7). The same table gives rigorous lower bounds of 7.91, 18.79 and
  84.82, used for negative controls.
- No improvement since was found: scout searches of 2013–2026; Vorobyev's paper has no k ≥ 4 remark.
- [Ding–Sly–Sun, arXiv:1411.0650](https://arxiv.org/abs/1411.0650) (opened by scout) proves the threshold only
  for k ≥ k₀, with k₀ an unspecified absolute constant.
- Franz–Leone-type interpolation makes the 1RSB value an upper bound "in principle" for even k. No certified
  numbers were found.
- Method template (k = 3 only):
  - [Vorobyev, arXiv:2610.10599](https://arxiv.org/abs/2610.10599) (opened; preprint, Lean 4) proves
    4.268 = 1067/250 with three warning rates, 1/20, 2/5 and 17/20, of weights 1/4, 1/2, 1/4. Its exact
    rational margin is Ψ₁₂₈ ≤ −10⁻⁵.
  - It builds on [Achlioptas–Menchaca-Méndez ICALP 2012](https://cgi.di.uoa.gr/~optas/papers/Energetic.pdf)
    (opened), whose energetic interpolation uses one probability p; I found no k-SAT threshold numbers in its text.

**Probe** (floating point, my derivation, not a certificate). Single-rate energetic trial:

  Φ_k(a; η, y) = E_{d₊,d₋ ~ Poi(ka/2)} log E[e^{−y·min(N₊,N₋)}] − (k−1)·a·log(1 − η^k(1 − e^{−y})),
  where N_± | d_± ~ Bin(d_±, η^{k−1}).

  Φ < 0 would imply C_k(a) if the inequality holds. Results:
  - k=3: Φ(4.4) ≈ −0.0046 and Φ(4.3) > 0. This is consistent with Vorobyev's repo, whose single-rate
    certificate files are named 4.341012 and 4.342 (per scout, [INFERENCE] from file names), and with the
    factorized estimate ≈ 4.396 quoted by Mézard–Zecchina 2002. Calibration passed.
  - k=4: Φ(10.0) ≈ +0.00016 and Φ(10.02) ≈ −0.00088, so the single-rate boundary is ≈ 10.01. The record is 10.23.
  - k=5: Φ(21.2) ≈ −0.0010, below the record of 21.33.
  - k=6: Φ(43.45) ≈ −0.00079, below the first-moment bound 44.01. No published k=6 value was opened.
  - k=7: Φ(87.85) ≈ −0.00040, below the record of 87.88. The cavity value is 87.79, so headroom is small.
  - All of these used y = 60, the optimum sat at the top of the y grid, and a single-rate trial;
    see `probes/OUTPUT.txt`.
  - **Positive control.** I evaluated Vorobyev's three-rate trial in the y → ∞ series form of this functional
    (`probes/vorobyev_control.py`, 160-digit Decimal) at a = 1067/250:
    - variable term −0.76119275, clause term +0.76118155, Ψ₁₂₈ = −1.1203×10⁻⁵. These are exactly the
      figures reported from his paper.
    - The same trial at a = 4.0 gives +0.0233, so no certificate there.

    The probe functional is therefore his Ψ at k = 3. The general-k form changes only k−1 (coin tosses),
    ka/2 (Poisson rate per sign) and (k−1)a (clause coefficient). Whether the interpolation *inequality*
    holds for general k is proof obligation P1.
  - **Multi-rate probe** (`probes/probe_multirate.py`: three rates, random search, 130-digit Decimal series,
    T = 128; not a certificate):
    - k=3: Ψ(4.268) ≈ −1.0×10⁻⁵, close to Vorobyev's −1.12×10⁻⁵.
    - **k=4: Ψ(9.96) ≈ −1.5×10⁻³ and Ψ(9.94) ≈ −3.7×10⁻⁴** (record 10.23, cavity 9.931).
    - **k=5: Ψ(21.14) ≈ −4.6×10⁻⁴ and Ψ(21.125) ≈ −3.5×10⁻⁵** (record 21.33, cavity 21.117).

    The values r₄ ≤ 9.94 and r₅ ≤ 21.13 are exploratory search targets, not certificates.
    Begin certification at comfortable margins: k=4 near 9.96 and k=5 at or above 21.14.
  - **Numerical trap.** The alternating binomial sums lose about 38 digits at T = 128. A first version that
    fed double-precision ν_i into them returned spurious values near −10⁴³. Certificates must use exact or
    high-precision ν_i, and the negative controls must catch this failure.

**Attack plan** (four-hour attack inside the six-hour visit; four threads, <1 GB RAM, <100 MB disk).
1. **First two hours, analytic go/no-go.** Establish the general-k interpolation inequality, checking
   odd-k hypotheses explicitly for k=5, finite-y or limiting control, concentration, and all model
   transfers. Cross-check the 2012 energetic paper and citing literature for already known bounds.
2. **In parallel, trial search and certificate tooling.** Start with k=4 and k=5 at comfortable
   margins. A value at or below cavity estimates 9.931 or 21.117 is a probable bug, not a breakthrough.
3. **Remaining attack time, exact evaluation and independent checks.** Use rational/interval exp-log
   bounds and explicit truncation signs. Reserve time for controls and a report; stop at four hours.

**Claim levels:** floating-point negativity is evidence only. Rigorously bounded exact/interval
negativity certifies an inequality only. A threshold theorem additionally needs every analytic bridge
accepted by the referee. Without those bridges, report the result as conditional on the fully stated
interpolation inequality. Even proved k=4,5 bounds are partial progress on Challenge 5, not exact thresholds.

**Verifier:** a second, independent evaluator (mpmath interval arithmetic, different summation order) plus a
parent replay. Lean is optional: there is no Mathlib build budget.

**Negative controls.**
- At the proven-satisfiable densities 7.91 (k=4) and 18.79 (k=5) no trial may give Φ < 0. A negative value
  there falsifies the derivation or the code.
- Mutation tests: replace (k−1) by k in the clause term, or drop the min. Each must break the controls.
- Positive control: reproduce Vorobyev's k=3 single-rate boundary (≈ 4.34) and Ψ₁₂₈(4.268) ≈ −1.12×10⁻⁵.

**Kill criteria.**
- By about two attack hours, decide whether the analytic bridge holds. Otherwise preserve only the
  conditional inequality or exploratory table, with the blocker stated explicitly.
- Do not tighten a density at the expense of a certifiable margin; raise a_k if the margin is too small.

**Risks.**
- Unfound prior art for k ≥ 4, such as values in Dubois–Boufkhad 1997, whose body I did not open, or a very
  recent preprint after Vorobyev. The parent should re-check arXiv just before launch.
- Vorobyev's proof is unreviewed. The run must prove P1 itself and not cite Vorobyev as established.
- Model-variant subtleties.

**openai/math check:** family 235 covers existence and computability with no numbers, and has no k ≥ 4
bounds. There is no conflict, and a proved bound also bounds their limiting threshold.

### #2 — phys-p0591: certified lower bound on the depolarizing channel's zero-capacity threshold

**Verbatim (book p. 592 = PDF 627, checked against `sources/phys-p0591/qch-627.png`):**
> 信道的量子容量的研究直接关系到香农第二定理的量子推广。……尽管量子信道容量在 n→∞极限下被证明与信道的相干信息等价[7~9]，但是如何有效的计算这一相干信息量是一个非常困难的问题。当 n→∞时，计算量子信道容量所涉及的变量指数增多，……对量子信道容量的求解也变得不可能。它被认为是量子信道研究中最重要的问题。

**Translation:** "The quantum capacity relates directly to the quantum generalization of Shannon's second
theorem. … Although the quantum capacity was proved equal to the regularized coherent information as n → ∞,
computing this coherent information efficiently is a very difficult problem. … Solving for the quantum capacity
becomes impossible. It is regarded as the most important problem in quantum-channel research."

**Formal statement.**
- Channel: N_p(ρ) = (1−p)ρ + (p/3)(XρX + YρY + ZρZ).
- Capacity: Q(N) = lim_n (1/n) max_ρ I_c(ρ, N^{⊗n}). Threshold: p* = sup{p : Q(N_p) > 0}.
- [ASSUMPTION] The depolarizing channel is the canonical instance of the book's general question.
- **Target:** an explicit M-qubit input state ρ with certified I_c(ρ, N_p^{⊗M}) > 0 at a rational
  p > 0.194868. Monotonicity in p (Krohn-Grimberghe's semigroup remark) then covers everything below p.
- **Stretch:** certified positivity, on the limiting Gaussian channel, of a finite-excitation state at
  η ≤ 0.7294452 (p ≥ 0.2029161), provided Ahmed et al.'s Δ_{M,K} bound is explicit.

**SOTA baseline.**
- p* ≤ 1/4: antidegradability. No proof that Q = 0 for any p < 1/4 was found.
- Certified explicit record: 0.194868 = 3·16239/250000, a 45-qubit rank-two symmetric state with an
  integer-only verifier ([arXiv:2608.15870](https://arxiv.org/abs/2608.15870), opened).
- Claimed: p* ≥ 0.2029161 ([arXiv:2609.39747](https://arxiv.org/abs/2609.39747), opened). Theorem 6 gives the
  M → ∞ limit as a thermal attenuator. The optimized rank-two mod-3 Fock state (n ≤ 220) has I_c ≈ 10⁻¹² in
  floating point. No finite M is given.
- Peer-reviewed: ≈ 0.19130 (Fern–Whaley 2008).

**Attack plan.**
1. **0–1.5 h, evaluator.** Build an exact Schur–Weyl block evaluator of I_c for permutation-symmetric rank-r
   inputs. Reproduce Krohn-Grimberghe's witness (positive control).
2. **1.5–4 h, search.** Transplant Ahmed et al.'s Gaussian-optimal mod-3 envelope into the Dicke basis at
   M = 60–200 and optimize in floating point.
3. **4–6 h, certify.** Certify the best state at a rational p with outward-rounded interval arithmetic, and
   cross-check with an independent stdlib-rational evaluator.

**Negative controls.**
- At p = 1/4 no state may certify I_c > 0.
- The n=1 hashing boundary (≈ 0.1893) must be reproduced.
- The 45-qubit witness must fail slightly above its published boundary.

**Kill criterion:** no floating-point state beyond 0.1955 at M ≤ 200 by 3 h.

**Resources: flag.** Exact-rational certificates were 17 MB at M = 45 and grow fast. Use interval
certificates to stay within 1 GB of disk and 4 GB of RAM.

**Risks.**
- The field is moving fast: three preprints in 2026, some LLM-driven. A result below 0.2029 ranks as
  "certified explicit", not as a new best claimed p*.
- Scooping.

**openai/math check:** no family (local or remote `CONTENTS.md`).

### #3 — phys-p0422, Challenge 5, k = 3: tighten the 3-SAT upper bound below 4.268

**Quote and formal statement:** as #1 with k = 3.

**Baseline:** published 4.4898 (0807.3600); claimed 4.268 (2610.10599, Lean, unreviewed). If 1RSB is exact
(cavity 4.26675), the headroom is at most 0.0013.

**Angle:** 4–8-rate trials from a population-dynamics fixed point, certified at a ≤ 4.2675 with an exact or
interval margin of about 10⁻⁶. This reuses #1's toolchain and controls.

**Plausibility and value:** low–medium plausibility, low value (third decimal). The run would also give an
independent check of an LLM-driven, unreviewed claim, though replication alone does not count. Fits the
resource limits.

The other 6h-scoped row, the Q(N_p) upper bound, ranked lower: low plausibility for an incremental gain.

## (d) Recommendation

**#1: phys-p0422, Challenge 5, k ≥ 4** (scientific value × plausibility per 6 h, FRONTIER §1).
- **Book-posed and precise.** The article explicitly asks for rigorous upper and lower bounds on K-SAT
  thresholds computed from population dynamics with rigorous numerics. The threshold problem is decades old
  and famous.
- **Open, with a named baseline.** The k = 4, 5, 7 bounds (10.23 / 21.33 / 87.88, opened) have stood since the
  late 1990s. Two independent searches found no improvement.
- **Headroom.** There is real room: 0.30 for k=4 and 0.21 for k=5 against the cavity values. A one-parameter
  floating-point probe already lands at ≈ 10.01 (k=4), below 21.2 (k=5), below 43.45 (k=6) and below 87.85
  (k=7), beating every published record that I opened. A three-rate probe reaches Ψ < 0 at 9.94 (k=4) and
  21.125 (k=5). The same code reproduces Vorobyev's k=3 certificate value exactly.
- **Checkable deliverable.** Each new bound is a rational number certified by exact arithmetic, with an
  independent verifier and falsifiable negative controls at proven-satisfiable densities.
- **Not owned.** No AI4S dossier and no openai/math family covers it.

It is a new value obtained with an existing method template, not a copied literature result. The novelty rests
on k ≥ 4, and the k=3 replication is only a control.

Alternates: #2 (higher topical prominence, lower plausibility, scooping risk) and #3 (a cheap add-on to #1,
low value).

**Decisions for the parent.**
1. Re-run an arXiv check for "k-SAT upper bound" and "4-SAT threshold" right before launch. The area moved on
   2026-10-06.
2. Accept that the general-k proof (P1) is checked by written proof plus independent review, not Lean. Building
   Mathlib is out of budget.
3. If #2 is chosen, allow interval rather than exact-rational certificates to respect the 1 GB disk limit.
