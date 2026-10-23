# Physics volume

Source volume: 《10000个科学难题·物理学卷》 (10000 Selected Problems in Sciences: Physics,
Science Press, 2009, ISBN 978-7-03-024269-3). Local copy: [`books/`](../books/README.md), not
tracked by Git; 876 PDF pages; the table of contents is on PDF pages 9–18; PDF page = book page + 33
for book pages 183–579 and + 35 for 580–704.

Each target directory owns its own status, sources, evidence and claims. This index only routes.
Physics round evidence—intake runs and parent replays, the reselection packages and the
SOTA/significance audit—lives in [`evidence/`](evidence/). [Repository overview](../README.md).

## Current reselection (2026-10-14)

The user subsequently chose **“Re-select with explicit open statements.”** Five replacement
packages now contain complete classical arguments, source/SOTA screens, independent reviews and
passing parent replays; their exact outcomes are indexed in
[PHYSICS_RESELECTION.md](PHYSICS_RESELECTION.md). All are **Certification** results with
**uncertified novelty/priority**, not five priority-certified discoveries or full book-chapter
solutions. Three targets come from one Tevet paper, and the supersoliton result addresses only
the selected generic criterion. The five earlier proof packages below remain preserved but do
not count toward the replacement five; the already-solved SO(5) candidate is also excluded.

## Earlier narrowed intake (selection gate not passed)

The opening table of contents and about 40 candidate sections were screened. Five workers first
investigated cone packing, bilinear integrability, fractional parentage, optical invariance and
quantum codes. That first pass did **not** establish five easy, literature-open chapter problems.
The user then explicitly chose **“Choose precise open subproblems”** rather than keeping the
chapter-scale questions or restarting the full-volume screen.

The five focused proof obligations below come from **three book chapters**. Two distinct parity
branches concern the same integrability chapter; two different state families concern fractional
parentage. None was proved in the first-pass package. In the prior-art screen run on 2026-10-14,
none of the primary sources we could access settled the exact scoped statements. However, some
key primary texts could not be accessed (for example, the full Peng et al. (2008) paper), so their
openness and novelty remain **uncertified**. “Accessible” means that each target reduces to a finite
symbolic computation or a specific proof identity. It does not guarantee that the theorem is easy,
novel or previously unknown. Each directory records its own verdict and independent review.

**Still-unsolved selection gate: NOT PASSED (blocked on inaccessible primary sources).** All five
proofs are complete, independently reviewed and replayed, but none of the five statements is
certified as historically unsolved. Each was **previously unproved in this project**; no checked
primary source explicitly declares the exact statement open. Final comparisons are recorded in each
target's STATUS.md under “Openness gate (final, 2026-10-14)”. Inaccessible sources are listed there
and are not treated as negative evidence.

| # | Scoped proof target | Book chapter; book pages (PDF pages) | Openness gate | Directory |
|---|---|---|---|---|
| 1 | Spin-2 low-total-spin CFPs (L ≤ 5), all seniorities: 24 squared-coefficient formulas and two block weights | 母配分系数递推关系的破解 (鲍诚光); 348–349 (381–382) | No settling source among those checked; Kishimoto–Tamura 1971, Arima–Iachello 1976, Talmi 1993 pp. 763–771 and others inaccessible | [`phys-fractional-parentage-coefficients/`](phys-fractional-parentage-coefficients/) |
| 2 | General-spin near-stretched CFPs at deficit five: f ≥ 3, L = fv − 5, v → v−1 | Same chapter; 348–349 (381–382) | No settling source among those checked; Sun et al. 1989, Bayman–Lande 1966 tables, Kishimoto–Tamura 1971 and Talmi 1993 inaccessible | [`phys-parentage-deficit-five/`](phys-parentage-deficit-five/) |
| 3 | Odd-cubic two-function bilinear system: arbitrary-amplitude Pfaffian tau formula for all N | 关于得到高维可积模型的一个新猜想 (楼森岳, 李金花); 350–351 (383–384) | Partial overlap: equation and three-soliton structure in Hietarinta (1987/1997); Peng et al. 2008 reports Wronskian N-solitons (full text inaccessible) | [`phys-bilinear-higher-dim-integrability/`](phys-bilinear-higher-dim-integrability/) |
| 4 | Mixed-parity bilinear system (c₂ ≠ 0): all-N tau formula for arbitrary F/G seed patterns | Same chapter; 350–351 (383–384) | Partial overlap on both branches: c₃ ≠ 0 is gauge-equivalent to the odd-cubic pair; c₃ = 0 is Li–Lou model (ii); same inaccessible sources | [`phys-bilinear-mixed-parity/`](phys-bilinear-mixed-parity/) |
| 5 | Fresnel polarization-degree invariance for sector-diagonal sources in LG modes n = 0, 1, orders ±m | 光传播中的光谱不变性和偏振不变性 (赵道木); 333–334 (366–367) | No settling source among 24 checked; Li 2015, Zhao–Wolf 2008, Gori 2008 and others inaccessible | [`phys-spectral-polarization-invariance/`](phys-spectral-polarization-invariance/) |

## Screened out

Retained but rejected as active “not-too-hard” selections:

- [Cone/Fibonacci packing](phys-fibonacci-cone-spirals/): the fixed-golden-angle ansatz has a
  certified counterexample, but this does not settle every Fibonacci-contact configuration or the
  experimental elastic-energy problem. Its sharp number-theoretic packing-density law also has
  [2024 prior art](https://arxiv.org/html/2106.12333v8); it is not a fresh open target.
- [Small quantum codes](phys-quantum-code-construction/): the unrestricted rank-three/rank-five
  existence questions remain open in the checked tables, while the tested CWS classes were
  already excluded in stronger prior work. Reproductions are preserved but not counted as
  solutions or as evidence that the unrestricted problems are easy.

Already settled (some before, others after the book was published):

- 一维量子自旋链系统在任意边界磁场中的严格解: off-diagonal Bethe ansatz, Cao, Yang, Shi, Wang,
  Nucl. Phys. B 877, 152 (2013) (arXiv:1307.2023).
- 梯度方法能否用于求解 Dirac 方程?: yes; the inverse Hamiltonian method avoids variational collapse
  (e.g. Ren et al., Phys. Rev. C 95, 024313 (2017), Dirac equation on a 3D lattice).
- 五夸克态是否存在?: LHCb, Phys. Rev. Lett. 115, 072001 (2015).
- 介观环中的持续电流的实验观测值与理论值有较大差距的疑难: Bleszynski-Jayich et al., Science 326, 272
  (2009), measured currents agree with theory.
- 量子信道, additivity of the classical capacity: false, Hastings, Nature Phys. 5, 255 (2009).
- 用"瓦特天平"法实现量子质量基准 and 用基本物理常数建立国际单位制 SI 的基本单位: the 2019 SI
  redefinition fixed h, e, k and N_A.
- Yangian 表示论与求解非线性模型, Haldane–Shastry part: Haldane, Ha, Talstra, Bernard, Pasquier,
  Phys. Rev. Lett. 69, 2021 (1992).
- 能否利用随机共振机制提高弱信号接收的信噪比: largely settled for weak signals by Fisher-information
  bounds (Duan, Chapeau-Blondeau, Abbott, PLoS ONE 7, e34282 (2012)).

Too hard for a bounded attempt: exact solutions of 3D many-body models; the QMC sign problem; the
high-T_c pairing mechanism; a rigorous Fourier law and the 1D anomalous heat-conduction exponent;
turbulence; quantum capacities of general channels; exact solutions of quantum field theories; a
Yangian-only solution of the Hubbard spectrum; spin-liquid ground states of J1–J2 models.

Not precisely posed: most astrophysics, acoustics, nuclear-structure, materials and device items,
and conceptual questions such as 为什么严格的多体波函数计算不能给出超导态 (answered by off-diagonal
long-range order, Yang, Rev. Mod. Phys. 34, 694 (1962)).

## Difficult-problem visit (2026-10-15)

The owner requested one difficult physics-volume problem with a six-hour total ceiling, alongside
mathematics and information science. The [hard-problem catalog](evidence/physics-hard-20261015/catalog.md)
records candidates, status sources, budget classes, probes and parent-review restrictions.

Selected `phys-p0422`, **用统计物理学方法处理约束满足问题面临的五个挑战** (M. Alava, E. Aurell,
周海军, book pp. 422–427; PDF pp. 455–460), Challenge 5: rigorous random-k-SAT threshold bounds,
initially k=4 and k=5. A certified negative trial-functional value is not a threshold theorem without
the general-k interpolation, limiting/concentration argument and model transfers. Improved bounds
would address only part of the chapter, not determine exact thresholds.

The [institute run](../institute/runs/hard-2026-10-15/README.md) first timed out during 10-minute
identification. With owner approval it restarted at 12:02 PT with a fresh six-hour allocation and a
30-minute selected-question identification stage. Authority for those engine visits:
[`record.json`](../institute/runs/hard-2026-10-15/problems/phys-p0422/record.json).
Its batch 03 continuation closed **unverified** (accept-with-fixes) at 14:49 PT. That snapshot's
written proof and rational enclosures gave random 4-SAT/5-SAT whp unsatisfiability at 9.96/21.14.
It had no formal verification or established novelty. The
[batch ledger](../institute/review/hard-2026-10-15-outcomes.md) records that historical outcome.

### Authorized continuation (2026-10-16)

The [new certificate package](evidence/hard-continuation-20261015/README.md) improves the
explicit densities and adds a 3-SAT refinement:

| Arity | Written proof + rigorous numerical certificate | Separate Lean-kernel endpoint |
|---|---|---|
| 3-SAT | **4.26679** | **4.26718** |
| 4-SAT | **9.9325** | **9.934** |
| 5-SAT | **21.1175** | **21.123** |

All use iid legal signed clauses, with replacement across clauses. The
[Lean development](evidence/hard-continuation-20261015/formal/README.md) proves a general-arity
criterion and convergence to zero, not the written proof's exponential rate or explicit finite-n
constants. The new 3-SAT closure passed fresh kernel replay within 4 GiB per process; earlier
k=4/5 kernel checks required about 12 GB, a corrected resource limitation. The strongest numerical
rows are not kernel theorems.

The 3-SAT value is 0.00121 below Vorobyev's explicit 4.268 endpoint, within his established method.
Prior work already states near-cavity variational upper bounds, and earlier general-k Lean material
exists. These are reproducible numerical/formal instantiations, not a new principle, exact thresholds,
human peer review or an established global record. See the
[continuation ledger](../institute/review/continuation-20261015/outcomes.md) for controls and priority holes.

## Six concurrent research lanes (2026-10-16–18)

An explicit rank-two input on 2000 qubits has a computer-assisted coherent-information enclosure
of `[1.1373755593e-8, 1.1432769066e-8]` bits at **total-error p=1/5** (outward-rounded), implying
positive depolarizing-channel quantum capacity for every `0 ≤ p ≤ 1/5`. Its exact witness premises,
sector replay, numerical controls, independent float cross-check and hostile reviews are documented
in the [parent verdict](../institute/runs/six-lane-2026-10-16/review/depolarizing-parent-verdict.md).
The trust base includes binary64 arithmetic assumptions and FLINT/Arb; this is not a Lean theorem.
The point improves the certified finite-witness threshold 0.194868 but not the claimed asymptotic
0.2029161 threshold. Significance and priority remain separate from certification.

Other scoped results are AMH Open Problem 1 moment feasibility (not code existence), three-qubit
depolarizing-output majorization for all physical replacement parameters, and partial four-qubit
indices.

**The Díaz et al. Maximum Hypothesis for random 5-regular 3-colouring now has a computer-assisted
proof.** It rests on an exact slice-concavity lemma, nine facet cones each checked by three
independently written outer checkers, and a central-box certificate checked by two hardened central
checkers. With Theorem 1.1 of the pinned 2009 preprint, **χ(G_{n,5}) = 3 asymptotically almost
surely**. The corollary imports the preprint's analytic arguments, and the published version was not
compared ([parent verdict](../institute/runs/six-lane-2026-10-16/review/colour-maximum-parent-verdict.md)).

The two-qutrit 2-unitary orbit is also isolated among dual and among T-dual gates: every other such
gate is at Frobenius distance at least 1. This answers the non-trivial reading of T7 at d = 3. Geng
(2022) had already computed the 33-dimensional linear kernel, so novelty is unclear
([parent verdict](../institute/runs/six-lane-2026-10-16/review/dualunitary-t7-parent-verdict.md)).
**Every set of four mutually orthogonal quantum Latin squares of order 7 is classical, so
2 ≤ M(7) ≤ 3.** This answers the n = 7 instance of Ball–Simoens Problem 16 (arXiv:2607.12933v2),
the smallest open case of their Table 2. The proof is computer-assisted: a written reduction to three
support-pattern classes, two independently written encodings per class, and six UNSAT certificates
that the parent regenerated byte-for-byte and verified with drat-trim. It imports the Egan–Wanless
MOLS(7) classification; whether M(7) is 2 or 3, and every n ≥ 8, stay open. NOVELTY-UNCLEAR after a
bounded audit ([parent verdict](../institute/runs/six-lane-2026-10-16/review/moqls7-parent-verdict.md)).
At n = 8, the classes with exactly one or two non-classical squares are excluded: the written
K1 argument and the 39-net K2 reduction passed Codex and Claude reviews, with all wording fixes applied in r2;
the parent independently rebuilt all 78 CNFs, verified all 78 DRAT proofs, and checked the
catalogue's 39 distinct net isomorphism classes and relaxed positive controls.
The class with exactly three non-classical squares is excluded as well: 2165 net representatives, each with a parent-regenerated CNF
and a parent-verified DRAT proof. This is partial progress only; K4 and K5 remain open
([K1/K2 record](../institute/runs/six-lane-2026-10-16/review/moqls8-k1k2-parent-verdict.md),
[K3 record](../institute/runs/six-lane-2026-10-16/review/moqls8-k3-parent-verdict.md)).
**The maximum entangling power of a two-qutrit dual unitary that is not 2-unitary is exactly 15/16**,
and the same holds for T-dual gates. Every non-2-unitary dual gate has rank U^Γ ≤ 6 (for T-dual gates,
realignment rank ≤ 6), which proves Rather's 2023 Conjecture 3.3.2 and the optimum described as likely in
arXiv:2508.04777v3. It is a reviewed written proof with exact algebra and two exact attaining gates, not a
Lean formalization; NOVELTY-UNCLEAR after a bounded audit
([parent verdict](../institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md)).
**Theorem K1 at n = 7 (2026-10-17):** no set of three mutually orthogonal quantum Latin squares of order 7 has exactly one
non-classical square. Hence every 2-resolvable and every pandiagonal QLS(7) has cardinality 7, so neither an MCPQLS(7)
(Huang–Li 2026) nor a maximal-cardinality 2-RQLS(7) (Zhang–Cao 2026) exists. It is a computer-assisted proof with five
independent parent routes, including a full re-enumeration of the reduced Latin squares of order 7, and Codex/Claude reviews
returned ACCEPT-WITH-FIXES with the fixes delta-checked. NOVELTY-UNCLEAR, not Lean
([parent verdict](../institute/runs/six-lane-2026-10-16/review/moqls7-k1-parent-verdict.md)). **Theorem K2 (2026-10-18,
partial):** no such triple has exactly two non-classical squares. It is a computer-assisted proof: the parent replayed all
294 UNSAT certificates and checked main-class coverage, and four hostile reviews returned ACCEPT-WITH-FIXES. It carries a
stated provenance caveat ([parent verdict](../institute/runs/six-lane-2026-10-16/review/moqls7-k2-parent-verdict.md)).
**Final update: M(7) = 2**, computer-assisted and internally correctness-accepted: every triple is
classical, and a non-classical pair exists. The [final parent verdict v2](../institute/runs/six-lane-2026-10-16/review/moqls7-M7-equals2-parent-gate-verdict-v2.md)
supersedes the earlier K3-pending status. Its provenance caveats remain: 35 K2 classes lack
script-hash-observed parent replay, and the streamed M7 proofs were not retained or digested.
No fresh upper-bound replay, Lean proof, human review or priority claim is supplied by this update.
The later Problem16 n=8 and maximal 1-RQLS(10) targets remain unresolved at the
[96-hour closeout](../institute/runs/six-lane-2026-10-18-96h/report/continuation-report-2026-10-22-final-v17.md).
See the [six-lane ledger](../institute/runs/six-lane-2026-10-16/outcomes.md) for exact scope.


**Random regular colouring continuation (2026-10-17).** χ(G_{n,7}) = 4 a.a.s. for the uniform simple
random 7-regular graph is CORRECTNESS-ACCEPTED after Codex and Claude reviews and parent delta review
([verdict](../institute/runs/six-lane-2026-10-16/review/chi7-parent-verdict.md)). It is DERIVED-OPEN:
its key sharper constant already appears in Achlioptas–Naor and in Nir–Pérez-Giménez for random lifts,
so it is not counted as an explicitly named gate. **χ(G_{n,8}) = 4 and χ(G_{n,12}) = 5 a.a.s.** are now
CORRECTNESS-ACCEPTED on final r3 proofs after Codex hostile, Claude complete and Codex delta reviews, byte-identical
parent verifier replays and independent parent rational arithmetic
([χ8](../institute/runs/six-lane-2026-10-16/review/chi8-parent-verdict.md),
[χ12](../institute/runs/six-lane-2026-10-16/review/chi12-parent-verdict.md)).
They close KPW's {4,5} and {5,6} windows at degrees8 and12 beyond the previous constants7.4156 and11.8297, through
one shared hypercontractive global-decay mechanism. DERIVED-OPEN, priority unresolved; recorded under the contract's
new-theorem half of that clause only (the method has an earlier random-lift precedent;
[attribution addendum](../institute/runs/six-lane-2026-10-16/review/physics-priority-addendum-v1.md)), not as two separate results. The older χ7/χ8 generic SSC formulation is
clarified by a parent [conditional-contiguity addendum](../institute/runs/six-lane-2026-10-16/review/colouring-ssc-formulation-addendum-v1.md).
At that stage, the continuation was **AME(4,6) minimum support**, with exact witness≤59 or complete lower bound60 required
([contract](../institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json)). A partial result is accepted:
**every AME(4,6) state has at least 48 nonzero coefficients** in every product orthonormal basis (published bound 38).
The bound 42 is a written proof importing only Tarry's theorem. The steps to 46 and 48 add computer-assisted enumerations;
their 55 load-bearing UNSAT certificates, orbit/schema bindings and 161 phase certificates were independently rechecked by
the parent, with Codex and Claude reviews ([s ≥ 42](../institute/runs/six-lane-2026-10-16/review/ame46-lower42-parent-verdict.md),
[s ≥ 46](../institute/runs/six-lane-2026-10-16/review/ame46-lower46-parent-verdict.md),
[s ≥ 48](../institute/runs/six-lane-2026-10-16/review/ame46-lower48-parent-verdict.md)).
