# info-2 pre-freeze kill check (scout report, verbatim)

Recorded 2026-10-17 13:24:13 PDT from read-only scout `Info2KillCheck`, launched after the BRD(26,130,25,5,4) target proved stale. Leads only; a miss is not novelty.

**Lane-2 target pick: weighing-matrix and related open instances, with kill checks after 2006**

## Summary
- **Freeze SW(25,16).** SW(27,16) and SW(29,16) are siblings in the same lane. Status is (b): Rosin (arXiv 2505.23881v1, 29 May 2025) lists all three as open. I found no later resolution in the scope below. That scope includes the 2026 Goldberger et al. paper that does kill SW(28,25).
- **Alternate: SkewW(30,25).** Status (b), with no later resolution found.
- **Killed:**
  - SW(28,25) is solved (it exists). Goldberger, Ben-Av, Dula and Strassler, arXiv 2603.17552v1, published as Discrete Math. 350, 115367, online Aug 2026.
  - EPA(9,8,21) does not exist, as a claim. OEIS A005677 gives R(9,1)=20 from Tolonen's classification (Mar 2026). The write-up is "in preparation" and not peer-reviewed.
  - Five of CPro1's eight DTS open instances were already resolved by Shehadeh et al. (2025). This matches the earlier screen.
- **CPro1's open lists have other gaps.** A symmetric W(23,16) was posted on Dinitz's page in Sept 2016. Szöllősi (2015) acknowledges Munemasa for a symmetric W(19,9).
- **A miss is not novelty.** "No later resolution found" covers only the sources listed. It establishes neither openness, nor priority, nor novelty. No matrix was verified computationally; this was a read-only scout.

## Ranked table

| # | Instance | Definition | Open attestation (quote, URL) | Later-literature check (result; read scope) | Blocked sources | Tractability [INFERENCE] | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | **SW(25,16)**; siblings SW(27,16), SW(29,16) | 25×25 matrix W over {0,±1} with WWᵀ=16I and W=Wᵀ | "…leaving n∈{25,27,29} as the remaining open instances for w=16." arxiv.org/abs/2505.23881 (v1, 29 May 2025) | **(b)**, none found. Goldberger 2026 solves only SW(23,16), SW(28,25), SW(30,17) and AW(28,25). The Egan–Ó Catháin–Švob census has no W(25,16), W(27,16) or W(29,16). The Dinitz page (edited 2/15/18) and Munemasa page (2017) post only non-symmetric W(25/27/29,16) plus a symmetric W(23,16). Also checked: Valtonen 2026, Topno–Saurabh 2025, the CPro1 and Goldberger repos, an arXiv sweep, and OpenAlex citers. | Rosin's NeurIPS-25 workshop paper (OpenReview bot check); the published DM version (ScienceDirect 403); Georgiou 2023 (MDPI/DOAJ 403); Ben-Av 2…
| 2 | **SkewW(30,25)** | 30×30 matrix W over {0,±1} with WWᵀ=25I and Wᵀ=−W | Table 1 (SkewW): "(18,9)? \| \| Exists" … "(30,25)? \| \| \|" arxiv.org/abs/2501.17725 (v1). CPro1 `OPEN_INSTANCES = [[18,9],[30,25]]` | **(b)**, none found. Goldberger 2026 has AW(28,25) only. The census has no real W with n=30. | Same as row 1 | **Size:** 435 free cells, zero diagonal. Equivalent to OD(30;1,25). Necessary conditions hold (25=3²+4², 25≤28). **Model:** the two-circulant skew model [[A,B],[−Bᵀ,Aᵀ]] (A skew-circulant of order 15, PAF_A+PAF_B=0, sum B=±5) is exhaustible in seconds to minutes. **Prior attempts:** CPro1's 48 h simulated-annealing (SA) runs failed (it is a default target), and Goldberger reports no AW(30,25). **Competition:** elevated; the CPro1 repo is a…
| 3 | T2(11), T2(13) | n×n array with each row a permutation; each ordered pair is adjacent in exactly one row and has one symbol between it in at most one row | `OPEN_INSTANCES = [[11],[13]]` (CPro1 tuscan-2-square problem_def.py) | **(b)**, none found. Thin scope: OEIS and arXiv/web sweeps only. | Handbook VI.62, unread | Fits SAT well. Existence is doubtful: all CPro1 development instances have even order. | Do not freeze until a dedicated kill check is done. |
| 4 | EPA (10,8,21), (11,8,21), (10,7,18), (11,7,18) | m×n array of permutations; every pair of rows differs in exactly d positions | Table 2: "(10,8): m ≥ 20", "(11,8): m ≥ 20", "(10,7): m ≥ 17", "(11,7): m ≥ 17" (2501.17725v1) | **(b)**, but Östergård–Tolonen "Classifying Equidistant Permutation Codes (in preparation)" is cited on OEIS. A013578 stops at R(9,2). | Östergård–Tolonen manuscript, not public | SA reached (12,8,21) in about 10 h; these did not fall in 48 h. Nonexistence by classification is plausible but is the competitor's active project. | Avoid (high scoop risk). |
| 5 | FR(13,13); FR(8,14), FR(8,15), FR(8,21) | r×n array of permutations; each (a,b,distance m) occurs in at most one row | Table 1: "n = 13: 13 ≥ r ≥ 12"; "n = 14: 14 ≥ r ≥ 7"; "n = 15: 15 ≥ r ≥ 7"; "n = 21: 21 ≥ r ≥ 7" | **(b)**, none found. OEIS A004079 covers n ≤ 12 only (last edited 2023). | Handbook VI.62 | OEIS shows F(n)=n only when n+1 is prime (n ≤ 12), so FR(13,13) is probably nonexistent and would need a large exhaustive proof. Randomized depth-first search failed on FR(8,·). | Avoid. |
| 6 | DTS (6,5,95), (3,8,134), (3,9,183) | (n,k) difference triangle set with scope ≤ s | `OPEN_INSTANCES = [...,[6,5,95],…,[3,8,134],[3,9,183],…]` | **(b)** for these three. Shehadeh 2502.19517v2 Table I solves the other five but has no (6,5) or n=3 entries. OEIS A010896 gives optimal (3,k) only up to k=7. | Published JCD version (Wiley 403) | A success would only improve an upper bound. The FPGA search skipped or failed (6,5). | Avoid. |
| K1 | SW(28,25) | Symmetric W(28,25) | Table 2 lists "(28,25)?" as open (2501.17725v1) | **(a) Solved (exists).** "There exist symmetric weighing matrices SW(23,16), SW(30,17), SW(28,25) and an anti-symmetric weighing matrix AW(28,25)." arxiv.org/abs/2603.17552 (v1, 18 Mar 2026). Matrix in github.com/assafg-dev/Classification-of-IW-matrices, file SW2825.txt (contains git merge markers). | ScienceDirect version | — | **Kill.** |
| K2 | EPA(9,8,21) | — | Table 2: "(9,8): m ≥ 20" | **(a), claimed nonexistence.** OEIS A005677 history: "Added the term R(9,1)=20, which was obtained by a classification of the relevant equidistant permutation arrays done by Luka Tolonen, Mar 14 2026". | Primary paper not public | — | **Kill.** |

## JSON

```json
{
  "date": "2026-10-17",
  "caveat": "Read-only scout; no computation run. A search miss is not novelty: 'no later resolution found' covers only read_scope.",
  "ranked": [
    {
      "rank": 1,
      "instance": "SW(25,16)",
      "siblings": ["SW(27,16)", "SW(29,16)"],
      "definition": "n x n matrix W over {0,1,-1}, W W^T = 16 I, W = W^T; n = 25 (siblings 27, 29)",
      "status": "b",
      "open_attestation": {
        "quote": "This paper's results include construction of a w=16 n=22 Symmetric Weighing Matrix, resolving this open instance and leaving n∈{25,27,29} as the remaining open instances for w=16.",
        "url": "https://arxiv.org/abs/2505.23881",
        "version": "v1 (29 May 2025), latest per arXiv API"
      },
      "later_check": {
        "result": "No resolution found",
        "evidence": [
          {"src": "Goldberger, Ben-Av, Dula, Strassler, arXiv 2603.17552v1 (18 Mar 2026); Discrete Math 350:115367 (Crossref created 2026-08-04, OA)", "url": "https://arxiv.org/abs/2603.17552", "quote": "In particular we solve some open cases: Symmetric W(23,16), W(28,25) and W(30,17), and an anti-symmetric W(28,25).", "finding": "No 25/27/29; authors note symmetric W 'abundant' and urge symmetric searches"},
          {"src": "Dinitz, New Results in Part V (last edited 2/15/18)", "url": "https://site.uvm.edu/jdinitz/?page_id=404", "quote": "Weighing matrices W(n,w) for w = 16 have been found for the four values of n that were previously unknown.", "finding": "Only W(23,16) symmetric (Sept 2016); 25/27/29 general only"},
          {"src": "Munemasa, Weighing matrices of some other orders and weights (modified 2 Feb 2017)", "url": "http://www.math.is.tohoku.ac.jp/~munemasa/research/matrices/wo.htm", "finding": "W(25,16), W(27,16), W(29,16) plus symmetric W(23,16); seed W-25-16.magma readable"},
          {"src": "Egan, O Cathain, Svob, arXiv 2607.16069v1 (17 Jul 2026)", "url": "https://arxiv.org/abs/2607.16069", "finding": "Census tables (primitive rank<=5, n<=80) list no real W(25|27|29,16)"},
          {"src": "Valtonen arXiv 2608.06920v2; Topno-Saurabh NNTDM 31(3):443-447 (2025)", "finding": "No 25/27/29 claims"},
          {"src": "Adin-Epstein-Strassler math/9910164", "quote": "It turns out that the order must be an odd multiple of either 21 or 31.", "finding": "No circulant W(n,16) for n=25,27,29"}
        ],
        "read_scope": "Full text: Rosin 2501.17725v1 and 2505.23881v1; Goldberger 2603.17552v1 (HTML+PDF incl. refs); Egan 2607.16069v1 (incl. tables); Topno-Saurabh PDF. Grep: Valtonen 2608.06920v2. Pages: Dinitz, Munemasa. Repos: CPro1 designs/ (SymmW 19-9, 21-9, 22-16 only; commits to 2026-06-03), assafg-dev (AW189, AW2825, SW19_9, SW2825, SW3025). OpenAlex citers of Georgiou 2023, Topno 2025, Ben-Av 2024. arXiv newest-10 'weighing matrices'. Multiple web searches."
      },
      "blocked": ["OpenReview WlXSZiqcbH (Rosin NeurIPS-25 workshop, bot check)", "ScienceDirect S0012365X26003912 (403)", "MDPI/DOAJ/FreeLibrary Georgiou 2023 (403)", "Ben-Av et al. DM 347:113908 (closed access)", "CRC Handbook 2nd ed. Table 2.88"],
      "tractability_inference": {
        "size": "325 free ternary cells, 16 nonzeros/row; verification O(n^3)",
        "ruled_out": "circulant/back-circulant (CW classification); zero diagonal (odd n forces trace = 4(p-q) != 0, so trace in {+-4,+-12,+-20}); primitive rank<=5 automorphism group (census absence); n=29 group-developed equals circulant",
        "models": "(1) symmetric-representative test on posted seeds via Goldberger Prop 5.2 / Valtonen Alg 3 (minutes; low prior); (2) symmetric 5x5 array of Z5 circulants with symmetric IW(5,16) quotient; (3) orbit-partition models for 27 (3x9) and 29 (1+4x7); (4) SAT/ILP with symmetry breaking",
        "nonexistence_route": "none identified",
        "scoop_risk": "medium-high (Goldberger group; CPro1 active, though 25/27/29 not in its default OPEN_INSTANCES)"
      },
      "recommendation": "FREEZE as lane-2 primary; 27/29 as same-lane alternates"
    },
    {
      "rank": 2,
      "instance": "SkewW(30,25)",
      "definition": "30x30 W over {0,1,-1}, W W^T = 25 I, W^T = -W",
      "status": "b",
      "open_attestation": {"quote": "(18,9)? | | Exists | ... | (30,25)? | | |", "url": "https://arxiv.org/abs/2501.17725", "version": "v1, Table 1; CPro1 OPEN_INSTANCES = [[18,9],[30,25]]"},
      "later_check": {"result": "No resolution found", "read_scope": "As rank 1; Goldberger has AW(28,25) only; census has no real n=30 W; CPro1 designs has skew 18-9 only", "source_conflict": "CPro1 uses SkewW(28,25) as a development instance, while Goldberger calls AW(28,25) an open case; irrelevant to (30,25)"},
      "blocked": ["same as rank 1"],
      "tractability_inference": {"size": "435 free cells; equivalent to OD(30;1,25)", "conditions": "25 = 3^2+4^2, 25 <= n-2: no known obstruction", "models": "two-circulant skew [[A,B],[-B^T,A^T]], A skew-circulant order 15, PAF_A+PAF_B=0, sum(B)=+-5: exhaustive in seconds-minutes; negacyclic hybrids; AIW block quotients; antisymmetric test on known W(30,25) classes", "prior_failures": "CPro1 48 h SA (default target); no AW(30,25) from Goldberger", "scoop_risk": "elevated"},
      "recommendation": "Alternate / quick falsification lane"
    },
    {
      "rank": 3,
      "instance": "T2(11), T2(13)",
      "definition": "n x n, rows permutations of {0..n-1}; each ordered pair adjacent in exactly one row; distance-2 at most once",
      "status": "b",
      "open_attestation": {"quote": "OPEN_INSTANCES = [[11],[13]] # PARAMS for each open-problem instance.", "url": "https://github.com/Constructive-Codes/CPro1/blob/main/CPro1/design_definitions/tuscan-2-square/problem_def.py"},
      "later_check": {"result": "none found", "read_scope": "thin: OEIS A004078, arXiv/web sweeps"},
      "blocked": ["Handbook VI.62 (Chu-Golomb-Song)"],
      "tractability_inference": "SAT-friendly; existence doubtful (CPro1 dev instances all even orders)",
      "recommendation": "Needs a dedicated kill check before freezing"
    },
    {
      "rank": 4,
      "instance": "EPA (10,8,21), (11,8,21), (10,7,18), (11,7,18)",
      "definition": "m rows, permutations of {0..n-1}; every pair of rows differs in exactly d positions",
      "status": "b",
      "open_attestation": {"quote": "(10,8): m >= 20 ... (11,8): m >= 20 ... (10,7): m >= 17 ... (11,7): m >= 17", "url": "https://arxiv.org/abs/2501.17725", "version": "v1 Table 2"},
      "later_check": {"result": "none found; active competing classification (Ostergard-Tolonen, in preparation; OEIS A005677/A393633)", "read_scope": "OEIS A005677 (+history), A013578, A393633; arXiv/web sweeps"},
      "blocked": ["Ostergard-Tolonen manuscript (not public)"],
      "tractability_inference": "SA got (12,8,21) in ~10 h median but not these in 48 h; nonexistence-by-classification plausible but contested",
      "recommendation": "Avoid (high scoop risk)"
    },
    {
      "rank": 5,
      "instance": "FR(13,13); FR(8,14), FR(8,15), FR(8,21)",
      "definition": "r x n, rows permutations; each (a,b,m) at most one row",
      "status": "b",
      "open_attestation": {"quote": "n = 13: 13 >= r >= 12; n = 14: 14 >= r >= 7; n = 15: 15 >= r >= 7; n = 21: 21 >= r >= 7", "url": "https://arxiv.org/abs/2501.17725", "version": "v1 Table 1"},
      "later_check": {"result": "none found", "read_scope": "OEIS A004079 (n<=12, edited 2023); arXiv hits only quasi-Florentine DRCS papers 2505.11012, 2602.06045"},
      "blocked": ["Handbook VI.62"],
      "tractability_inference": "F(n)=n only when n+1 is prime (n<=12) suggests FR(13,13) nonexistent; proof needs large exhaustive search",
      "recommendation": "Avoid"
    },
    {
      "rank": 6,
      "instance": "DTS (6,5,95), (3,8,134), (3,9,183)",
      "definition": "(n,k)-DTS: n rulers 0=a_i0<...<a_ik<=s, all within-row differences distinct",
      "status": "b",
      "open_attestation": {"quote": "OPEN_INSTANCES = [[5,7,170],[7,5,112],[6,5,95],[5,6,118],[4,7,134],[3,8,134],[3,9,183],[6,6,145]]", "url": "https://github.com/Constructive-Codes/CPro1/blob/main/CPro1/design_definitions/difference-triangle-set/problem_def.py"},
      "later_check": {"result": "these three not addressed; other five resolved by Shehadeh et al. 2502.19517v2 (9 Jun 2025), Table I e.g. (4,7): 134 (135), (5,6): 118 (119)", "read_scope": "Shehadeh v2 PDF Table I; OEIS A010896 (3,k) optimal only to k=7"},
      "blocked": ["Wiley JCD version 10.1002/jcd.22009 (403)"],
      "tractability_inference": "upper-bound improvement only; heavy prior heuristic/FPGA search",
      "recommendation": "Avoid"
    }
  ],
  "killed": [
    {
      "instance": "SW(28,25)",
      "status": "a",
      "quote": "There exist symmetric weighing matrices SW(23,16), SW(30,17), SW(28,25) and an anti-symmetric weighing matrix AW(28,25).",
      "url": "https://arxiv.org/abs/2603.17552",
      "version": "v1, Cor. 5.3; DM 350:115367 (2026)",
      "artifact": "github assafg-dev/Classification-of-IW-matrices, SW2825.txt (merge markers present; not numerically verified here)"
    },
    {
      "instance": "EPA(9,8,21)",
      "status": "a (claimed nonexistence)",
      "quote": "Added the term R(9,1)=20, which was obtained by a classification of the relevant equidistant permutation arrays done by Luka Tolonen, Mar 14 2026",
      "url": "https://oeis.org/history?seq=A005677",
      "caveat": "primary paper in preparation; not peer reviewed"
    },
    {
      "instance": "DTS (4,7,134), (5,6,118), (5,7,170), (6,6,145), (7,5,112)",
      "status": "a",
      "url": "https://arxiv.org/abs/2502.19517",
      "version": "v2 Table I"
    }
  ],
  "calibration": [
    "CPro1 lists have gaps beyond BRD: symmetric W(23,16) posted Sept 2016 (Dinitz page); Szoellosi 2015 acknowledges Munemasa's symmetric W(19,9).",
    "Pre-register a stop rule: if structured models fail, report only the negative results for those models."
  ]
}
```

[Some lines truncated to 768 chars. Use agent://Info2KillCheck:raw:17-17 to read line 17 whole; cut lines run to line 18, each read the same way]
