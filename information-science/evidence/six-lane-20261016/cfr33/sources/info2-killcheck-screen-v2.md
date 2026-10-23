# info-2 recency-aware kill check (scout report, verbatim)

Recorded 2026-10-17 14:37:06 PDT. Parent corrections: "no claim anywhere" means only no claim found in the stated scope; EPA(9,8,21) is NOT eligible without resolving Tolonen's March2026 nonexistence claim in OEIS history, which this report missed. Parent directly read CPro1 CFR problem_def.py and Kirtchakov's August2026 CFR(5,25) note.

**Lane-2 target kill check: CPro1 / Rosin open instances, checked 2026-10-17**

**Outcome.** Two more listed instances are already resolved: CFR(5,25) was claimed on 2026-08-06, and PA(32,5,6) was shown not to exist on 2026-08-03. SkewW(30,25) has no claim anywhere, but its scoop risk is high. I recommend circular Florentine rectangles CFR(4,33) and CFR(5,27) as the lane-2 target, with the EPA (equidistant permutation array) instances as the backup.

SkewW and T2 are still open but rank lower: SkewW because agent-afk just worked the same Rosin table, T2 because it is probably out of reach before the deadline. I ran no computations. Every tractability statement is marked [INFERENCE].

## Ranked shortlist (best is rank 1)

**1. CFR(4,33) and CFR(5,27); CFR(6,21) as a stretch goal**
- **Definition (CPro1):** an r×n array whose rows are permutations of {0..n−1}. For any two distinct symbols a, b and each m in 1..n−1, at most one row puts b exactly m places to the right of a, counting circularly.
- **Open attestation:**
  - CPro1 lists `OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]` ([problem_def.py](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py), main@827f02b, 2026-06-03). Its dev instances include [5,21], [4,27] and [3,33], which are the known lower bounds.
  - Kirtchakov's note, which read the Handbook chapter directly, says CPro1 "lists the open instances (6, 21), (5, 25), (5, 27), (4, 33)" ([note.md](https://raw.githubusercontent.com/05oz/certify/HEAD/cfr-paper/note.md), draft 2026-08-06).
- **Recency check:**
  - DataCite abstracts containing "Florentine rectangle(s)", "Tuscan square(s)" or "Tuscan-2": 9 hits, of which only Kirtchakov's (5,25) is relevant.
  - OpenAlex full text "circular Florentine" since 2020: 15 hits. All are sequence-design applications; none improves F_c(21), F_c(27) or F_c(33).
  - arXiv API searches for Tuscan / Florentine / Vatican: nothing relevant.
  - Kirtchakov's repo `05oz/certify` contains only `CFR_5_25`; its last commit was 2026-08-19.
- **Scoop risk: moderate.** Kirtchakov's Claude-driven pipeline works from the same CPro1 list and has been idle for about two months.
- **Tractability [INFERENCE]:**
  - Kirtchakov found (5,25) on one laptop. He fixed one row as the identity and searched for the remaining rows as a clique of orthomorphisms that are equivariant under a multiplier group.
  - Density r/(n−1) is 0.125 for (4,33) and 0.19 for (5,27), against 0.21 for the solved (5,25), so these two look reachable. (6,21) is at 0.30.
  - He published only n=25, which may mean the other sizes failed for him.
  - There is no practical route to proving nonexistence.
  - Verifying a candidate means an exact count of r·n·(n−1) events, which takes seconds.
- **Why it fits information science:** F_c(N) is the family size of optimal perfect polyphase sequence sets ([Zhang–Vinterbo, arXiv 2308.04837](https://arxiv.org/abs/2308.04837)) and of OC-FHS sets.

**2. EPA(11,8,21) and EPA(9,8,21); also EPA(10,8,21), EPA(10,7,18), EPA(11,7,18)**
- **Definition:** m rows, each a permutation of {0..n−1}, with every pair of rows differing in exactly d positions. Adding a constant column turns EPA(n,d,m) into EPA(n+1,d,m), so (9,8,21) implies (10,8,21) and (11,8,21).
- **Open attestation:**
  - CPro1 lists `[[10, 7, 18], [11, 7, 18], [9, 8, 21], [10, 8, 21], [11, 8, 21], [12, 8, 21]]`, and its `designs/` folder contains only `result-12-8-21`.
  - Rosin's Jan 2025 Table 2 gives "(9,8): m ≥ 20 … (12,8): m ≥ 20" with no progress from the literature ([arXiv 2501.17725v1](https://arxiv.org/abs/2501.17725)).
- **Recency check:** the DataCite phrase "equidistant permutation" returns only Rosin. OpenAlex since 2023 returns 5 hits, none about these instances.
- **Scoop risk: low to moderate.**
- **Tractability [INFERENCE]:** SAT with symmetry breaking, or a prescribed Z₇ or Z₃ action on the 21 rows. (11,8,21) is the weakest instance and so the easiest to construct; (9,8,21) settles three instances at once.

**3. BTD(12,15;6,2,10;8,6), BTD(14,18;7,1,9;7,4), BTD(12,20;4,3,10;6,4); also (14,28;8,3,14;7,6), which appears only in Rosin's table**
- **Definition:** V×B incidence matrix N with entries 0/1/2, satisfying N·Nᵀ = (ρ₁+4ρ₂−L)I + LJ.
- **Open attestation:**
  - CPro1 `OPEN_INSTANCES` lists the three main instances.
  - Rosin's Jan 2025 Table 1 marks "(14,18;7,1,9;7,4)? (12,15;6,2,10;8,6)? (12,20;4,3,10;6,4)? … (14,28;8,3,14;7,6)?", citing Greig 2002.
- **Recency check:** DataCite returns only Rosin. OpenAlex since 2023 returns 8 hits, none relevant. The 2026 Research Square preprint on balanced n-ary designs does not mention these parameters (grep, no hit).
- **Scoop risk: low.**
- **Tractability [INFERENCE]:** the matrices are tiny, so exhaustive SAT/ILP search should decide existence either way. This is the best pick if you want a nonexistence-type result. Weaknesses: a looser information-science fit, and pre-2025 literature that I could not fully check.

**4. FR(8,14), FR(8,15), FR(8,21)**
- **Definition:** the non-circular version of CFR above.
- **Open attestation:** CPro1 lists `[[8,14],[8,15],[7,20],[8,21],[7,24],…]`; CPro1 solved only the r=7 cases. The Handbook's F(n) table, as quoted in arXiv 2308.04837v1 (2023), gives "14 | 7,…,14; 15 | 7,…,15; 21 | 7,…,21".
- **Recency check:** the same searches as rank 1 found nothing.
- **Scoop risk: moderate** (same Handbook chapter Kirtchakov mined).
- **Tractability:** unclear [INFERENCE].

**5. SkewW(30,25)**
- **Definition:** a 30×30 matrix with entries in {0,±1}, Wᵀ = −W, W·Wᵀ = 25I.
- **Open attestation:** CPro1 `OPEN_INSTANCES = [[18,9],[30,25]]`, with only (18,9) solved. [Goldberger et al., arXiv 2603.17552v1](https://arxiv.org/abs/2603.17552) (2026-03-18) solves "an anti-symmetric W(28,25)" but not order 30. Their repo has `AW189`, `AW2825` and `SW3025` files, but no antisymmetric W(30,25).
- **Recency check:** DataCite "skew weighing" returns 2 hits (Rosin; Ghaderpour 2016). Searches for W(30,25) and skew-symmetric weighing return only noise. OpenAlex since 2024 returns only Rosin. Recent arXiv weighing-matrix papers (2507–2608) contain none. Long and Macías-Quintero have no skew records.
- **Scoop risk: high.** agent-afk took SW(25/27/29,16) from the same Rosin tables on 2026-10-15; Goldberger's group is active; Macías-Quintero posts weighing matrices weekly.
- **Tractability [INFERENCE]:** a two-circulant search is cheap: skew-circulant A and circulant B of order 15 with A·Aᵀ + B·Bᵀ = 25I and rowsum(B) = ±5. If that fails, use SAT with a prescribed signed automorphism. There is no nonexistence route. Treat this as a probe of an hour or so at most.

**6. PMD(9,6,12); also (10,6,15), (12,6,22), (15,6,35), (16,6,40), (18,6,51), (14,7,26), (15,7,30)**
- **Open attestation:** only CPro1 `OPEN_INSTANCES`. The older papers that might settle these could not be fetched (ScienceDirect and ResearchGate returned 403): Miao–Zhu 1995, Abel–Bennett–Zhang 2000.
- **Recency check:** DataCite and OpenAlex since 2023 show nothing.
- **Scoop risk: low.**
- **Tractability [INFERENCE]:** v=9 is an exact-cover problem with about 10⁴ candidate blocks and 180 items, likely decided in minutes. Because the BRD-2011 precedent shows CPro1 lists can be stale, check Handbook Table 35.29 before investing.

**7. T2(11), T2(13)**
- **Definition:** an n×n array of permutation rows in which each ordered pair (a,b) is adjacent exactly once and at distance 2 at most once.
- **Open attestation:**
  - CPro1 `OPEN_INSTANCES = [[11],[13]]`.
  - Dinitz's Handbook-updates page (last edited 2019-10-18): "Page 656, Table 62.26. An exhaustive search has shown that there is no 9 x 9 Tuscan-2 square. Daniele Bartoli … 1/12" ([page](https://site.uvm.edu/jdinitz/?page_id=413)).
  - Rosin's Table 3 shows no Tuscan-2 instance solved.
- **Recency check:** DataCite and arXiv return nothing. OpenAlex "Tuscan squares" returns 29 hits; the newest on-topic one is Golomb–Hess 2016 (unread). None of the 23 works citing Etzion–Golomb–Taylor 1989 resolves T2.
- **Scoop risk: low to moderate.** Kirtchakov's record carries the subject tag "Tuscan square".
- **Tractability [INFERENCE]:**
  - No cyclic construction exists for odd n, because Z_n has no sequencing when n is odd.
  - Nonexistence is believable (n = 3, 5, 9 are known not to exist), but an exhaustive proof at n=11 is likely far beyond the deadline, and n=13 more so.

## Instances claimed in 2025–2026 records
| Instance | Claim | Record / date |
|---|---|---|
| SW(25,16), SW(27,16), SW(29,16) | exist | Long (agent-afk), doi:10.5281/zenodo.23404962 (concept DOI …961), 2026-10-15 |
| CFR(5,25) | exists | Kirtchakov, doi:10.5281/zenodo.21831896, 2026-08-06 |
| PA(32,5,6) | does not exist: pa(5;6) = pa(6;6) = 31 | Sadhu, arXiv:2608.01606 v1 2026-08-03 (v2 08-08) |
| UNSQS(44,946), UNSQS(50,1225) | exist [INFERENCE: these are the "completely uniform" cases] | Lu, arXiv:2509.06663 v1 2025-09-08: "completely uniform nested SQS(v) for all v ≤ 50" |
| DC(16,2,·) | 209 (EinsteinArena), 215 (Weindel–Heckel arXiv:2504.00613 v2, Jun 2026), 216 | Gippini Requeijo (Team Banzai), doi:10.5281/zenodo.23029076, 2026-09-29 |
| Antisymmetric W(28,25) (a CPro1 dev instance); symmetric W(23,16), W(28,25), W(30,17) | exist | Goldberger et al., arXiv:2603.17552, 2026-03-18 |
| SW(22,16) | duplicate of CPro1's result | Topno–Saurabh, NNTDM 31(3), 2025, cited in 2603.17552 |
| DTS scopes (several) | improved | Shehadeh et al., arXiv:2502.19517, 2025-02-26 (individual instances not extracted) |
| Rosin's own results (Jan and May 2025) | SymmW (19,9), (21,9), (22,16); SkewW(18,9); EPA(12,8,21); 7 BTDs; FR(7,{20,24–27}); 3 BRDs; PA maxima; UNSQS(14,91); covering sequences, Johnson clique covers, deletion codes | arXiv:2501.17725 (2025-01-29), arXiv:2505.23881 (2025-05-29) |
| BRD(26,130,25,5,4) | stale; claimed in 2011 | already known to you |

Non-overlapping 2026 activity also seen: Costas order-32 partial nonexistence (Zenodo 22865915), covering numbers C(18,11,3) and C(20,12,3) (Team Banzai), circulant weighing matrix nonexistence (arXiv 2608.18468), and Hetman's S(2,7,505/589) (arXiv 2604.04975). None of these resolves a remaining CPro1 instance.

## Remaining CPro1 instances after removing the claims
- **CFR:** (6,21), (5,27), (4,33)
- **FR:** (8,14), (8,15), (8,21)
- **EPA:** (10,7,18), (11,7,18), (9,8,21), (10,8,21), (11,8,21)
- **SkewW:** (30,25)
- **T2:** 11, 13
- **PMD:** all 8 listed instances
- **BTD:** 3, plus one from Rosin's table
- **UNSQS:** (22,154), (26,260), (34,374), (46,690), (46,759), not checked against Lu's paper
- **Not individually rechecked:** BIBD (40,52,13,10,3), S(2,6,51), (39,57,19,13,6), (40,60,21,14,7); supersimple designs ×8; OA ×8; Costas 32 and 33; cap set (7,237)
- **None left:** SymmW, PA, BRD (stale)

**Blocked sources:** Zenodo record pages and API (403); OpenReview, which hosts the Dec 2025 workshop version (browser challenge); ScienceDirect for Song 2000, Etzion 1991 and the PMD papers (403); ResearchGate and CORE (403); Google Books and its API (429); the Semantic Scholar API; GitHub code search (401). I did not read any Handbook tables directly.

**Before depositing any result,** rerun the DataCite Florentine/Kirtchakov or EPA queries the same day. Stay out of the PA family, since memory says PA(19,8,6) is already a six-lane lane (I did not verify this in the repo).

```json
{"checked":"2026-10-17","recommendation":{"primary":["CFR(4,33)","CFR(5,27)"],"stretch":["CFR(6,21)"],"backup":["EPA(11,8,21)","EPA(9,8,21)"],"probe_only":["SkewW(30,25) two-circulant, about 1h"]},
"shortlist":[
{"rank":1,"family":"circular Florentine rectangle","instances":[[4,33],[5,27],[6,21]],"attestation":[{"quote":"OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]","url":"https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py","date":"main@827f02b 2026-06-03"},{"quote":"which lists the open instances (6, 21), (5, 25), (5, 27), (4, 33)","url":"https://raw.githubusercontent.com/05oz/certify/HEAD/cfr-paper/note.md","date":"2026-08-06"}],"recency":"DataCite Florentine/Tuscan abstracts 9 hits (only CFR(5,25)); OpenAlex circular Florentine since 2020: 15, none relevant; arXiv none; certify repo only CFR_5_25, last commit 2026-08-19","scoop_risk":"moderate","tractability":"[INFERENCE] equivar…
{"rank":2,"family":"equidistant permutation array","instances":[[11,8,21],[9,8,21],[10,8,21],[10,7,18],[11,7,18]],"attestation":[{"quote":"OPEN_INSTANCES = [[10, 7, 18], [11, 7, 18], [9, 8, 21], [10, 8, 21], [11, 8, 21], [12, 8, 21]]","url":"https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/equidistant-permutation-array/problem_def.py","date":"2026-06-03"}],"recency":"DataCite: only Rosin; OpenAlex since 2023: 5 hits, none relevant","scoop_risk":"low-moderate","tractability":"[INFERENCE] SAT with symmetry or Z7/Z3 row action; (9,8,21) implies (10,8,21) and (11,8,21)"},
{"rank":3,"family":"balanced ternary design","instances":["(12,15;6,2,10;8,6)","(14,18;7,1,9;7,4)","(12,20;4,3,10;6,4)","(14,28;8,3,14;7,6)"],"attestation":[{"quote":"Open instances [Greig, 2002] ... (14,18;7,1,9;7,4)? (12,15;6,2,10;8,6)?","url":"https://arxiv.org/abs/2501.17725","date":"v1 2025-01-29"}],"recency":"DataCite only Rosin; OpenAlex since 2023: 8 hits, none relevant","scoop_risk":"low","tractability":"[INFERENCE] exhaustive SAT/ILP decides either way; nonexistence-type"},
{"rank":4,"family":"Florentine rectangle","instances":[[8,14],[8,15],[8,21]],"attestation":[{"quote":"14 | 7, ..., 14 ... 15 | 7, ..., 15 ... 21 | 7, ..., 21","url":"https://arxiv.org/abs/2308.04837","date":"v1 2023-08-09"}],"recency":"same searches as rank 1, nothing","scoop_risk":"moderate","tractability":"[INFERENCE] unclear"},
{"rank":5,"family":"skew weighing matrix","instances":[[30,25]],"attestation":[{"quote":"OPEN_INSTANCES = [[18,9],[30,25]]","url":"https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/skew-weighing-matrix/problem_def.py","date":"2026-06-03"},{"quote":"we solve some open cases: Symmetric W(23,16), W(28,25) and W(30,17), and an anti-symmetric W(28,25)","url":"https://arxiv.org/abs/2603.17552","date":"v1 2026-03-18"}],"recency":"DataCite skew weighing 2 hits (old); OpenAlex since 2024 only Rosin; arXiv none; Goldberger repo has no AW 30/25; Long and Macias-Quintero none","scoop_risk":"high","tractability":"[INFERENCE] two-circulant search takes minutes; then signed-automorphism SAT; no nonexistence route"},
{"rank":6,"family":"perfect Mendelsohn design","instances":[[9,6,12],[10,6,15],[12,6,22],[15,6,35],[16,6,40],[18,6,51],[14,7,26],[15,7,30]],"attestation":[{"quote":"OPEN_INSTANCES = [[9,6,12],[10,6,15],[12,6,22],[15,6,35],[16,6,40],[18,6,51],[14,7,26],[15,7,30]]","url":"https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/perfect-mendelsohn-design/problem_def.py","date":"2026-06-03"}],"recency":"DataCite and OpenAlex since 2023: none; 1995/2000 papers blocked","scoop_risk":"low","tractability":"[INFERENCE] exact cover for v=9 decided in minutes; check Handbook VI.35 before investing"},
{"rank":7,"family":"Tuscan-2 square","instances":[[11],[13]],"attestation":[{"quote":"OPEN_INSTANCES = [[11],[13]]","url":"https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/tuscan-2-square/problem_def.py","date":"2026-06-03"},{"quote":"An exhaustive search has shown that there is no 9 x 9 Tuscan-2 square. Daniele Bartoli","url":"https://site.uvm.edu/jdinitz/?page_id=413","date":"edited 2019-10-18"}],"recency":"DataCite and arXiv none; OpenAlex 29 hits plus 23 citers, none resolve","scoop_risk":"low-moderate","tractability":"[INFERENCE] no cyclic construction for odd n; exhaustive proof at n=11 likely beyond deadline"}],
"claimed_2025_2026":[{"instance":"SW(25,16),SW(27,16),SW(29,16)","doi":"10.5281/zenodo.23404962","date":"2026-10-15"},{"instance":"CFR(5,25)","doi":"10.5281/zenodo.21831896","date":"2026-08-06"},{"instance":"PA(32,5,6) nonexistence","doi":"10.48550/arXiv.2608.01606","date":"2026-08-03"},{"instance":"UNSQS(44,946),UNSQS(50,1225) [INFERENCE]","doi":"10.48550/arXiv.2509.06663","date":"2025-09-08"},{"instance":"DC(16,2,216)","doi":"10.5281/zenodo.23029076","date":"2026-09-29"},{"instance":"antisymmetric W(28,25); SW(23,16),SW(28,25),SW(30,17)","doi":"10.48550/arXiv.2603.17552","date":"2026-03-18"},{"instance":"DTS scopes","doi":"10.48550/arXiv.2502.19517","date":"2025-02-26"},{"instance":"Rosin CPro1 set","doi":"10.48550/arXiv.2501.17725; 10.48550/arXiv.2505.238…
"blocked":["zenodo.org pages/API 403","openreview challenge","sciencedirect 403","researchgate 403","core.ac.uk 403","google books 429","semantic scholar API","github code search 401"]}
```

[Some lines truncated to 768 chars. Use agent://Info2KillCheck2:raw:113-113 to read line 113 whole; cut lines run to line 120, each read the same way]
