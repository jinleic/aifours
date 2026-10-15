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
