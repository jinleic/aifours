# Finite information-science replacement screen — 2026-10-16 PT

Source: read-only scout `FiniteInfoTargetScreen` (completed after 42m57s). Preserved verbatim below as screening evidence; parent primary-source checks are recorded separately.

I found three replacement targets. The best one: there are six cyclic (v,5,1) difference families whose existence has been open since 2004, and a 2026 journal paper still lists them as open. The other two are weaker; I'd treat them as backups.

I didn't create files, use Git, run model CLIs or run solvers. The arithmetic below is my own hand derivation and nothing has checked it yet. Search misses are not counted as evidence of openness; I quote a dated source for each target. Since the parent is now OpenAI, the cross-vendor hostile review for any of these should come from Claude Opus 5.5 max; Codex would be same-vendor.

## Ranked targets

| Rank | Target | Dated open-status source | Chance of settling in 24 h [INFERENCE] |
|---|---|---|---|
| **A** | Cyclic (v,5,1) difference families for v ∈ {321, 501, 621, 681, 801, 901}. These are the same objects as perfect (v,5,1) optical orthogonal codes. | J. Algebra Comb. Discrete Appl. 13(1), 2026, restating Discrete Appl. Math. 2004, Theorem 14 | **High** for at least v=321; **medium** for all six |
| **B** | A cyclic (211,7,1) difference family. Fallback: any Steiner system S(2,7,211). | Same 2026 paper, plus Hetman arXiv:2511.20708 v3 (28 Feb 2026) | **Low** (medium only if earlier authors never searched with a nontrivial multiplier) |
| **C** | A periodic Golay pair of length 106, written PG(106) | Lumsden–Kotsireas–Bright, arXiv v3 (16 Mar 2025); Math. Comp. 95 (2026) | **Low** |

### A. Cyclic (v,5,1) difference families, v ≤ 1001 — recommended

- **Object.** Find n = (v−1)/20 blocks of five residues mod v (n = 16, 25, 31, 34, 40, 45). Every nonzero residue mod v must appear exactly once as a difference x−y of two elements in the same block. Equivalent forms:
  - a perfect (v,5,1) optical orthogonal code (codes for optical CDMA);
  - an optimal cyclically permutable constant-weight code;
  - a cyclic Steiner system S(2,5,v).
- **Open status.**
  - Quote: *"A (20t + 1,5,1) CDF exists for 1 ≤ t ≤ 50 except possibly for t = 16, 25, 31, 34, 40, 45"* — Hetman, Baicheva, Topalova, J. Algebra Comb. Discrete Appl. 13(1) (2026) 111–119, accepted 20 Sep 2025, DOI 10.13069/jacodesmath.v13i1.389, https://jacodesmath.com/index.php/jacodesmath/article/download/389/267
  - Original source: Abel–Costa–Finizio, Discrete Appl. Math. 143 (2004), Theorem 14, which excludes exactly these six orders. I read it in the academia.edu full text. The 2004 paper also says an earlier source wrongly listed 501, 681 and 801 as known.
  - Buratti–Pasotti (DCC 2010) cover v=pq only when both primes are ≡ 11 mod 20. None of the six qualifies: 3·107, 3·167, 27·23, 3·227, 9·89, 17·53.
- **Book link (related area, labelled).** These blocks give 4-cycle-free QC-LDPC codes; the 2026 paper cites Park et al. (IEEE Trans. Commun. 2013) and Fujisawa–Sakata (ISIT 2005).
  - 高性能迭代解码问题 (邓科), book pp. 464–466 (PDF 485–487): LDPC codes and iterative decoding.
  - 光纤通信频谱效率的极限 (喻松、顾畹仪), pp. 420–422 (PDF 441–443): optical CDMA signature codes.
  - 纠错码的译码问题 (张寅), pp. 394–395 (PDF 415–416): constant-weight codes.
- **Certificate and verifier.** The certificate is n×5 integers mod v. A short verifier collects all 20n ordered differences and checks they hit each nonzero residue exactly once. Two cheap independent cross-checks:
  - expand the blocks into binary sequences and confirm every auto- and cross-correlation is at most 1;
  - develop the cyclic design and confirm every pair of points lies in exactly one block.
- **Attack.** Use exact cover over the cyclic group: the columns are the (v−1)/2 difference classes, and candidate blocks are generated as needed. Run it as randomized DLX or the backtracking algorithm from the 2026 paper, CP-SAT with an all-different constraint on the 10n differences, or tabu search / simulated annealing on a collision count.
  - Symmetry I derived (not machine-checked):
    - −1 is never a multiplier, because a symmetric 5-block repeats a difference.
    - For 321, 501, 681 and 901 the only odd-order multiplier groups (orders 53, 83, 113, 13) are impossible by fixed-point counting. So these four cases are plain cyclic searches.
    - For 621 and 801 a multiplier of order 3 exists (621: m ≡ 1 mod 23, m ≡ 10 mod 27; 801: m ≡ 1 mod 89, m ≡ 4 mod 9). Requiring it cuts the search to about a third.
  - Expected number of solutions for v=321 (rough estimate): about e^109 labelled. That suggests solutions are dense, and nothing algebraic rules them out.
  - Similar cases found by computer: the 2004 authors built every other composite order up to 1001, including 3p-type orders 141, 201 and 381. The 2026 paper classified all (101,5,1) and (105,5,1) families exhaustively in 5 days on 96 processes.
- **Quick-kill checks to run first.**
  1. Check the Handbook of Combinatorial Designs (2nd ed.) difference-family chapter by Abel–Buratti and the Baicheva–Topalova data page for later constructions of these six orders.
  2. Write the verifier first. Test it on known families and on deliberately corrupted inputs.
  3. Time the solver on the known orders 141, 201, 381 and 341 before attempting 321. If 381 takes more than about 6 h, downgrade the probability.
- **Crowding.** Not an AIM problem. Grepping the full EulerSolve listing and openai/math CONTENTS.md found no difference-family, optical-code or Steiner items. CPro1 (Rosin 2025) did not include cyclic difference families in its 16 design types. Nearby active groups are Beijing Jiaotong (cyclic designs with block size 4, finished 2022; perfect difference families, 2025) and Sofia (Hetman–Baicheva–Topalova). Scoop risk is low to moderate.

### B. Cyclic (211,7,1) difference family / S(2,7,211)

- **Object.** Five 7-element blocks in Z₂₁₁ whose 210 differences are all distinct. This is a perfect (211,7,1) optical code and a cyclic S(2,7,211). Fallback certificate: any S(2,7,211), i.e. 1055 blocks, checked by pair coverage.
- **Open status.**
  - Same 2026 paper: *"a (q,7,1) CDF exists for any prime power q ≡ 1 (mod 42) except for q = 43, possibly for q = 127 (nonexistence proved in [5]), 211, 31^6, and primes q ∈ [261239791, 1.236597·10^13] …"*. The underlying theorem is Chen–Wei–Zhu, J. Combin. Des. 10 (2002).
  - Hetman, arXiv:2511.20708 v3 (28 Feb 2026), https://arxiv.org/abs/2511.20708: *"the existence of S(2,7,127) and S(2,7,211) is undecided despite 127 and 211 are prime numbers."*
  - So 211 is the smallest open prime-power case for block size 7.
- **Book link and verifier.** Same as A.
- **Attack.** The available multipliers form a cyclic group of order 210; only odd-order ones can work. Try them in order of cost:
  1. Order 7, each block an affine image of the 7th roots of unity: an instant tiling check on a 30-element quotient.
  2. Order 5, the five blocks forming one orbit (Wilson-type): need a single 7-set whose 42 differences meet each order-5 coset once. Exhaustive in minutes.
  3. Order 3, two fixed blocks c+{0, a, aω, aω², b, bω, bω²} plus one orbit of three blocks: exhaustive in hours.
  4. Unrestricted randomized exact cover on 28 cores.
  - Similar case: (169,7,1) has 4 families, 2 of them with an order-3 multiplier.
  - I showed a 1-rotational S(2,7,211) is impossible over any group of order 210, because the Sylow 7-subgroup is normal (hand-derived).
  - Rough estimate: about 10⁵ labelled solutions. The same estimate gives about 1 for v=127, where none exist, so treat it with caution.
- **Crowding.** Hetman is actively constructing S(2,7,v) systems (v = 175, 217, 259), so scoop risk is moderate to high. Chen–Wei–Zhu may already have exhausted the order-5 case; I could not see their methods.

### C. PG(106)

- **Object.** Two ±1 sequences A, B of length 106 whose periodic autocorrelations sum to 0 at shifts 1–53. The only possible sums are (±14, ±4), since 212 = 14² + 4² is the only way to write it as two squares. Equivalently, a supplementary difference set 2-{106; 46, 51; 44}.
- **Open status.** *"The smallest length for which the existence of periodic Golay pairs is undecided is now 106."* arXiv:2408.15611v3 (16 Mar 2025), https://arxiv.org/abs/2408.15611; Math. Comp. 95 (2026) 1517–1539, DOI 10.1090/mcom/4096.
- **Book link (related area).** 无线通信系统中信道容量的定义和度量 (邓科、穆鹏程), pp. 455–457 (PDF 476–478): complementary sequences are used for channel sounding. Alternative: 水声通信 (卞红雨、杨德森), pp. 483–484 (PDF 504–505).
- **Verifier.** Integer autocorrelation sums. As a cross-check, build the 212×212 Hadamard matrix with two circulant cores and confirm HHᵀ = 212·I.
- **Attack.**
  - Compress by 2. This gives a ternary periodic complementary pair of length 53 with total weight 53. The compression by 53 is unique (Theorem 4 of the paper).
  - Lift back using matching on power spectra. Symmetry is poor:
    - an order-13 multiplier is size-incompatible;
    - only an order-4 multiplier on A and A↦reverse(A) symmetry on B fit.
  - The paper's multi-level compression doesn't help because 106 = 2·53. Earlier 2p lengths (34, 58, 74, 82) do exist.
- **Crowding.** Bright and Kotsireas are active. 2026 sweeps of similar Hadamard-type sequence tables (Lebedev, Sep 2026) suggest moderate scoop risk.

## Rejected candidates

| Candidate | Reason |
|---|---|
| Circulant weighing matrices CW(n,k), n ≤ 200, k ≤ 100 | Closed: Tan, arXiv:2608.18468v2 (1 Sep 2026), proves all 8 remaining open entries in the La Jolla circulant weighing matrix repository (v1.3) impossible. |
| Circulant weighing matrices CW(n,k), n < 1000 (Gordon, J. Algebraic Combin. 2026) | Crowded (Gordon and Tan are active); most open entries are expected not to exist. |
| Optimal (v,4,1) optical orthogonal codes | Solved for all v ≠ 25 (Zhao–Chang–Feng, IEEE TIT 70(12), 2024). |
| Perfect difference families with block size 4; cyclic (v,4,1) designs | Solved (JCTA 2026; DCC 2022). |
| Quaternary Legendre pairs | Crowded: Lebedev (4 Sep 2026) settled 7 of the 14 open lengths ≤ 100. |
| Binary Legendre pairs | Kotsireas group active; Hadamard-adjacent with a weak information-science link; LP(333) is equivalent to Hadamard order 668 (excluded). |
| Signed difference sets | Diffuse (tens of thousands of open cases) and active (He–Wu, Aug 2026). |
| Gordon's four possible cyclic relative-difference-set lifts with k ≤ 256 | Expected not to exist, so a witness is unlikely. |
| Visual cryptography thresholds (k,n), n ≥ 6 | No 2024–2026 source names an open entry; the repo already covers n ≤ 5. |
| Minimum-weight correlation-immune functions / simple orthogonal arrays | Latest open-entry sources found are 2020–2022. |
| Small symmetric/skew weighing matrices; Florentine rectangles | Being swept by LLM-driven search (CPro1, 2025); Florentine rectangles also need upper-bound proofs. |
| Constant-weight code bounds A(n,d,w) | Active in 2026; lower-bound improvements don't settle exact values. |
| Linear code tables (codetables.de, Maruta tables) | Diffuse and competitive; single-entry progress, not a named smallest open case. |
| QC-LDPC girth tables | Questions are asymptotic, or exact values need nonexistence proofs. |
| Equiangular tight frame table | Latest version is 2016. |
| S(2,7,127) | Cyclic version proved impossible; prime order defeats the usual symmetric constructions. |
| Resilient-function and APN small cases | Too hard or already excluded. |
| Six-participant secret sharing / index coding | Adjacent to the excluded Khazaei line; no dated finite list. |

## What I could not access

- The Handbook of Combinatorial Designs (2nd ed.) difference-family table.
- The full texts of Chen–Wei–Zhu 2002 (which searches they ran at q=211), Buratti–Pasotti 2010 (abstract only) and Zhao–Chang–Feng 2024 (abstract via OpenAlex only).
- ScienceDirect and ACM pages (HTTP 403).
- The Baicheva–Topalova data page.
- I took chapter titles and page numbers from `info.json` and did not re-read those book pages.

## Local files used

- `/Users/jinleic/jinleic-workspace/research-institute/explorer/inventory/info.json`: the five chapter entries at lines 1221 (纠错码), 1357 (光纤通信), 1541 (无线通信), 1581 (迭代解码) and 1690 (水声通信).
- `/Users/jinleic/repos/aifours/information-science/README.md` and `visual-cryptography-optimality/README.md`: existing dossiers; visual cryptography is certified only for n ≤ 5.
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/{transitions.json,screening/fresh-information-screen-final.md}`: slot history and the earlier exclusions.
