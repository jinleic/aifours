# Lane info-2: optimal (v,6,1) CPCW codes v in {122,123,124}; optimal (v,5,1) CPCW codes v in {143,144,146,162,167}

Owner: worker `InfoCpcw`. Frozen contract: `institute/runs/six-lane-2026-10-16/screening/info-2-cpcw-optimal-contract.json`
(SHA-256 593bbfc0...6aa72, not edited). Lane opened 2026-10-17 01:18:47 PDT (host clock). Window ends
2026-10-18 18:31:43 PDT. Non-goals: v = 126 (known; used only as a positive control), any other v.

Source read by this worker (PDF text via `pdftotext -layout`, saved as `sources/axioms-15-00035.layout.txt`,
SHA-256 cd014a21...1f4c, from the prep PDF a105f220...7080): Baicheva-Topalova, Axioms 15(1) (2026) 35, Definition 1
(p.1), optimality bound floor((v-1)/(k(k-1))) (p.2), Tables 1-4 and the open-case paragraph (p.5-6), Lemmas 1-5,
Theorems 1-2, Corollary 1, Proposition 1 (p.6-10), Tables A1-A2 (p.11-14; Table A2 gives the (125,6,1) code).

## 1. Frozen representation (written 2026-10-17 01:28 PDT, BEFORE any search in this lane)

### 1.1 Object
s = floor((v-1)/(k(k-1))) k-subsets B_1..B_s of Z_v (codewords) such that the k(k-1)s ordered differences b-b'
(b != b' in the same B_i) are nonzero and pairwise distinct (source Definition 1: |C_i ∩ (C_i+t)| <= 1 for t != 0
and |C_i ∩ (C_j+t)| <= 1 for i != j; the source states these are equivalent to the difference condition, p.2).
Acceptance of any code is by `code/verify_cpcw.py` (byte copy of the prep verifier, SHA-256
85f93e8babfb45c4d6cc2924524a645da9f5df7dc582290705befebe5fce7be8, made read-only), strict format `CPCW v k`.

### 1.2 Class formulation (used by every search)
Classes [d] = {d, -d}, d = 1..floor(v/2). A k-set B is ADMISSIBLE iff its C(k,2) unordered pairs have pairwise
distinct classes and (v even) none is [v/2]. Lemma: a family of admissible k-sets is a code iff the class sets are
pairwise disjoint. Proof: the unordered pair {a,b} yields exactly the ordered differences d = b-a and -d, which are
equal iff d = v/2 (excluded by admissibility); two different pairs yield a common ordered difference iff their
classes coincide. So "all ordered differences distinct" = "no class repeats and [v/2] unused". With
H = floor((v-1)/2) coverable classes ([v/2] for even v is never coverable: source Lemma 1), a code covers
s*C(k,2) classes and leaves c = H - s*C(k,2) coverable classes uncovered (the LEAVE).

### 1.3 Symmetry (proved, used for normalization)
(a) Translation: B -> B+t preserves the difference multiset, so each codeword is a translation class.
(b) Negation per row: B and -B have the same class set, hence are interchangeable in any cover; search rows store
    one representative per {translation class of B, translation class of -B}; the output uses the stored rows.
(c) Multipliers: for m in Z_v^*, x -> mx is a group automorphism of Z_v fixing 0, so it maps distinct nonzero
    differences to distinct nonzero differences and maps codes to codes, acting on classes by [d] -> [md].
    Hence a code with leave L exists iff a code with leave mL exists, and a normalization "leave = orbit
    representative" or "anchor codeword = orbit representative" loses no code up to equivalence. Only ONE use of
    the group is made per search (leave OR anchor), plus its stabilizer only where stated.
(d) Codeword order is irrelevant (exact cover enumerates sets of rows).

### 1.4 Exact per-v leave structure (re-derived from scratch; `code/structure.py` -> `notes/structure.json`)
| v | k | s | H | leave c (besides v/2) | leave orbits under Z_v^* | parity system (even v) |
|---|---|---|---|---|---|---|
| 122 | 6 | 4 | 60 | 0 (only [61] uncovered) | 1 | unique (a0,a1,a2,a3) = (0,1,2,1) |
| 123 | 6 | 4 | 61 | 1 | 3: [1], [3], [41] (gcd 1, 3, 41) | - |
| 124 | 6 | 4 | 61 | 1 | 4: [1], [2], [4], [31] | u odd: (0,1,2,1); u even: (0,1,1,2) |
| 143 | 5 | 7 | 71 | 1 | 3: [1], [11], [13] | - |
| 144 | 5 | 7 | 71 | 1, must be EVEN | 13 total, 10 even | u even only: (a0,a1,a2) = (0,3,4) or (1,0,6) |
| 146 | 5 | 7 | 72 | 2, same parity | 72 total, 36 admissible | both even: (0,3,4),(1,0,6); both odd: (0,4,3),(1,1,5) |
| 162 | 5 | 8 | 80 | 0 (only [81]) | 1 | (0,4,4) or (1,1,6) |
| 167 | 5 | 8 | 83 | 3 | 1107 | - |
Parity system (even v): type i = min(#odd, #even) elements of a codeword (an odd translation swaps parities); type
i has i(k-i) cross-parity pairs (odd classes) and C(i,2)+C(k-i,2) same-parity pairs (even classes); the counts must
equal the odd/even coverable classes minus the uncovered ones. Calibration: 82 (k=5) gives (0,2,2) = source
Example 3; 92 (k=6) gives (0,1,0,2) = source eq. (15); 62 (k=6) has no solution (known nonexistence).
Source Theorem 1 re-checked for 122 and 162: (3) sum a_i = t, (5) sum i(k-i)a_i = (v-2)/4 = 30 resp. 40; same
solutions. Corollary 1 (20t+2 needs t even): 162 = 20*8+2, t = 8 even, not excluded.
Every code for 122, 124 (and 126) has EXACTLY ONE type-1 codeword (a1 = 1 in every solution); used as an anchor.

### 1.5 RDF and the half-length projection (proved)
For 122 and 162 the leave is empty, so the 30s (resp. 20s) ordered differences are exactly Z_v \ {0, v/2}: a cyclic
(v,2,k,1) relative difference family over H = {0, v/2}. Projection pi: Z_v -> Z_{v/2} (kernel H): each nonzero
y in Z_{v/2} has two preimages in Z_v \ H, each covered once, so the projected blocks form a (v/2,k,2) difference
family in Z_{v/2}, and each projected block is a k-SET (two elements differing by v/2 would cover v/2).
Conversely a (v/2,k,2)-DF lifts iff a GF(2) linear system in the labels eps (B = {p + eps_p v/2}) is solvable:
for the two occurrences of each class, eps_1+eps_1'+eps_2+eps_2' = 1 + sigma_1 + sigma_2 (mod 2) with sigma the
integer wrap bits; for v/2 odd (61, 81) the CRT form Z_2 x Z_{v/2} gives right-hand side 1. [Status: derivation
only; used as a search representation for 162, not as a proof device.]

### 1.6 Search representations (frozen before running)
- R1 (all v, constructive): prescribe a leave (random parity-admissible, or an orbit representative), place p
  random admissible rows with disjoint classes avoiding the leave, enumerate ALL admissible rows (1.3b) inside the
  remaining classes, Algorithm X on bitmasks (min-candidate column, random row order), node limit. Each attempt is
  complete for its (leave, prefix) when the node limit is not hit. Deterministic per seed (splitmix64).
- R2 (122, 124; complete classification): anchor = the unique type-1 codeword, translated so its lone-parity
  element is 0: B1 = {0} u O, O a 5-set of odd residues (unique translate with this property); multiplier
  normalization: O ranges over orbit representatives of Z_v^* (all units are odd, so they preserve parity and fix
  0). The remaining s-1 codewords (types forced by 1.4) exactly cover the remaining classes (124: minus one leave
  class u, all u tried). All solutions are recorded; equivalence classes are counted afterwards by canonical form.
  A second, independently written implementation with a different anchor (the unique type-3 codeword for 122) is
  required before any zero is reported.
- R3 (162): projection form 1.5 and/or direct R1 in Z_162 with the parity types of 1.4.
- Any further representation is appended (with time) to the log BEFORE it is run.

### 1.7 Claim discipline
FOUND = strict-format file + SHA-256 + prep-verifier ACCEPT output saved + exact replay (source hash, binary hash,
command, seed). PROVED-NONEXISTENT only with two independent complete classifications (stated symmetry, proofs above)
plus positive controls (k=6: 121, 125, 126 rediscovered by the same code) and mutation controls. Timeouts,
exhausted heuristics or one unaudited exhaustive run are UNKNOWN. No novelty or priority claim is made here.

## 2. Per-v status
(updated in the log below; final table at the end)

## 3. Log (append-only, host clock)
- 2026-10-17 01:18:47 PDT lane created; 01:28 verifier copied (SHA above), structure.json computed (no search).
- 01:30-01:40 R1 (`code/cpcw_xc.c`) smoke + calibration, k=6, p=1 random prefix codeword + exact cover of the
  remaining 45-47 classes (complete per attempt, node limit never hit), seed 1 (300 attempts each) and seed 11
  (runs/r1-k6, launched 01:33:50, stopped by SIGINT 01:40:34, ~400 s each): 121 >= 2000 attempts, 123 >= 2000,
  125 >= 2800, 126 >= 3000 attempts, NO completion for any v (positive controls 121/125/126 not rediscovered).
  Scope: random (leave, first codeword) pairs only; says nothing about existence. R1 is too weak for k=6
  (~1e-3 completions/attempt or less); k=6 moves to complete classification R2.
- 01:34 later source found by web search and saved: Baicheva-Yoveva-Topalova, Axioms 15(9) (2026) 679
  (`sources/axioms-15-00679.pdf`, SHA-256 750fe8f7...85c1, published 11 Sep 2026): new necessary conditions for
  optimal (k(k-1)s+2,k,1) codes only when 4 | v; 122 and 162 are 2 mod 4, so not covered; it lists Buratti-Stinson
  Thm 4.6 exclusions (k=8u+5 needs s odd to be excluded; 162 has s=8) - neither target is excluded there.
- 01:38 `code/k6cls_a.c` (implementation A of R2; SHA-256 59d92df4...5e30, bin 1eacdbe5...7008) row count
  v=125: 7,111,700 admissible 6-sets up to translation+negation; targeted control `given:0,1,3,19,31,54` (first
  codeword of the Axioms Table A2 (125,6,1) code) returns exactly 1 completion, leave {8,44}, = the published
  code up to negating/translating codewords (e.g. -{0,4,67,80,105,119}+4 = {0,4,10,24,49,62}).
- 01:39 v=122: 5,277,452 rows; anchor1 orbit representatives O: 30,462 (Z_122^* acting on type-1 codewords).
- 01:40:44 full 122 run started: `bin/k6cls_a 122 anchor1 0 j 4 a122_j<j>` for j=0..3 (runs/a122).
- 01:43 v2 of implementation A (`code/k6cls_a.c` = frozen copy `code/k6cls_a_v2.c`, SHA-256 57d35efd...13d3,
  bin `bin/k6cls_a_v2` 5937cc06...79b8): adds mode `minrank` (anchor = Z_v^*-orbit representative of least orbit
  key among the 4 codewords; other codewords restricted to orbit key >= anchor key; leave free). Proof of
  completeness: the orbit key is invariant under the group, so applying the multiplier that maps the least-key
  codeword onto its orbit representative gives an equivalent code of the searched form. 121 sample: 5,804,986 rows,
  105,546 orbits.
- **01:43-01:44 FOUND v=122**: the running 122 job 0 reported anchor 3980 (B1 = {0,1,3,21,59,111}) with one
  completion; extracted with `bin/k6cls_a_v2 122 given:0,1,3,21,59,111 0 0 1 g122_a3980` (certs/v122/, 6.4 s,
  deterministic: no randomness in k6cls_a). Certificate `certs/v122/cpcw_122_6.txt`:
  {0,1,3,21,59,111} {0,4,10,27,40,75} {0,5,34,42,67,83} {0,7,22,31,50,76}, SHA-256
  872912e960a63621da68d2ebe49ba11181c6ff0eb1b3f9dbe03bfd88f00551bc; prep verifier ACCEPT (saved
  `certs/v122/verify_prep_cpcw_122_6.json`): uncovered = [61] only, 61 uncovered pairs. Parity types
  (1,2,3,2) = (a0,a1,a2,a3) = (0,1,2,1) as predicted by Theorem 1. Parent messaged 01:44.
- 01:45:44 implementation-A full 122 run finished (`runs/a122/`, 4 jobs x ~296 s): all 30,462 type-1 anchors,
  11 mask-level completions in total (one per listed anchor, `a122_j*.sols`). Single unaudited implementation:
  NOT promoted as a classification count.
- 01:45:35 `code/k6cls_a_v1.c` = byte-exact reconstruction of the source of `bin/k6cls_a` (SHA-256 59d92df4...5e30
  matches the hash recorded at 01:40:44); a clean rebuild gives a different binary hash (2a4ae749...), so replays use
  the preserved read-only binaries. 01:45:57 v2 given-anchor replay: `certs/v122/replay/` (.sols byte-identical).
- 01:46:40 started implementation A on 124 (`anchor1`, 2 jobs, runs/a124) and 123 (`minrank`, 2 jobs, runs/a123);
  01:47:36 a123_j1 paused (SIGSTOP) to give the parent a CPU slot for its 122 replay (parent replay complete).
- REPRESENTATION R4 (added 01:48; this entry is written after its first runs at 01:49 -- procedural deviation from
  1.6, recorded honestly): tabu local search `code/cpcw_ls.c` (frozen copy `code/cpcw_ls_v1.c`, SHA-256
  dbece67b...0acc; bin `bin/cpcw_ls` 0486d138...37e5): s codewords with element 0 fixed, cost = sum over classes
  of max(0, count - capacity) with capacity 0 for [v/2]; cost 0 <=> optimal code. No structure imposed.
  Calibration 01:49:18: (147,5,1) and (166,5,1) (Table A1 lengths) found in 0.00 s / 0.02 s, seed 1.
- **01:49:26 FOUND k=5, all five targets**, `bin/cpcw_ls V 5 1 120 ls_V_s1` (seed 1, runs/ls-targets), each
  certificate copied to `certs/vV/cpcw_V_5.txt` (read-only), prep verifier ACCEPT saved as
  `certs/vV/verify_prep_cpcw_V_5.json`, seed replay byte-identical (`certs/vV/replay/`):
  | v | found after | SHA-256 | uncovered differences |
  |---|---|---|---|
  | 143 | 1284 it, 0.03 s | eeeada3d4e3cf0ed70b038ba04d3b38b22200a6e1183dc693881bcc408bf06e8 | 39, 104 |
  | 144 | 3838 it, 0.09 s | b55797c7636eb5c378e6f4562d0cc8e2f03415e6ab7cc195f10be4fc7d96da2c | 30, 72, 114 (class 30 even, as forced) |
  | 146 | 708 it, 0.02 s | 52d69e01d9fd6147072c1854d460d0859a3ce17b717e361b2397a0e03a09a830 | 11, 17, 73, 129, 135 (both classes odd) |
  | 162 | 42249 it, 1.30 s | 7e26a43ec41d21aa24955e575dd23d0afc9fe9781b54c2dce4a4bc57dd5e638a | 81 only (RDF) |
  | 167 | 1569 it, 0.04 s | 4a46416eb88cdd6fddca538e97562bc176d610c019597cb61c8a3be2050f2bda | 24, 25, 79, 88, 142, 143 |
  Parent messaged 01:50.
- 01:50 R4 on k=6 (runs/ls-k6, 60 s each, seed 1): positive controls 125 FOUND 7.07 s, 126 FOUND 5.17 s.
- 01:53:33 R4 on k=6, seed 1, 60 s: 123, 124, 121 TIMEOUT with best cost 1 (runs/ls-k6).
- **01:54 FOUND v=124 and v=123** (implementation A v2, deterministic, no RNG). The running classification jobs
  printed completions; extracted (with a124_j1 briefly SIGSTOPped to stay within the CPU budget):
  124: discovery `runs/a124`: `../../bin/k6cls_a_v2 124 anchor1 0 0 2 a124_j0` -> "anchor 4782 sols=1 B1=0 1 3 27
  33 43"; extraction (cwd certs/v124) `../../bin/k6cls_a_v2 124 given:0,1,3,27,33,43 0 0 1 g124_a4782` (7.2 s).
  Certificate `certs/v124/cpcw_124_6.txt` = {0,1,3,27,33,43} {0,4,25,63,70,78} {0,5,18,52,93,107} {0,9,29,73,85,96},
  SHA-256 5fefb1f5cfab87f256eb9b84cd9bedf5a3da31102c0b8ae8c43c8df0cef2e225, uncovered 19, 62, 105, types (0,1,2,1).
  123: discovery `runs/a123`: `../../bin/k6cls_a_v2 123 minrank 0 0 2 a123_j0` -> "anchor 3150 sols=1"; extraction
  (cwd certs/v123) `../../bin/k6cls_a_v2 123 minrank 0 3150 1000000000 m123_a3150` (16.0 s; job index = anchor
  index selects that single anchor). Certificate `certs/v123/cpcw_123_6.txt` = {0,1,3,7,84,99} {0,5,19,56,74,94}
  {0,8,21,30,53,65} {0,10,26,62,73,90}, SHA-256 d499ac51efb27249b22c807ff15db8e0cc55f84dc2aae79e6d99ebed48855a83,
  uncovered 41, 82. Prep verifier ACCEPT for both (saved JSON); 01:55 extraction replays byte-identical
  (`certs/v12x/replay/`). Parent messaged 01:54; parent replays complete (parent receipts, not in this lane).
- 01:56:46-01:57:14 classification jobs stopped at their 600 s checkpoints by SIGTERM at parent request (target is
  existence). Partial outputs kept as written (`runs/a124/`, `runs/a123/`): .sols flushed at the checkpoint; any
  completion printed after it is in the .log only. Scope: a124 j0/j1 to anchor index ~7200 of 30,210 (job
  residues mod 2), a123 j0 to ~5700 of 162,453, a123 j1 to ~370. NOT a classification; no counts are claimed.
- 01:57:37 mutation controls `code/mutation_controls.py` -> `controls/mutation-receipt.json`: 8 certificates ACCEPT,
  157 fixtures (32 validity-preserving: translate/negate/reorder/multiply -> ACCEPT; 125 faults -> REJECT for the
  intended check D or F), 165 checks, 0 mismatches, verifier 85f93e8b...e7be8.
- 01:59 positive controls copied to `controls/positive/` with prep verifier ACCEPT: R4 seed 1 125 (e9e9cde7...)
  and 126 (4e7737fa...); calibration 147 (d3d7fb62...) and 166 (2b2497bb...). 121 not rediscovered by R4 (seed 1
  60 s; seeds 2-6 x 120 s running). Parity types of the even witnesses match 1.4: 122 (0,1,2,1), 124 (0,1,2,1),
  144 (1,0,6), 146 (0,4,3), 162 (1,1,6).
- 02:01 `notes/table3-163/NOTE.md` (parent request, primary evidence only, no search): page 5 rendered
  (`pdftoppm -r 300`), Tables 1/3/4 cropped, word boxes saved. Table 3's "?" between 161 and 164 covers {162,163};
  163 is listed nowhere and has no Table A1 code, but the text names only 143, 144, 146, 162, 167 -> table/text
  discrepancy; by the tables (163,5,1) is also undecided.
- 02:05 `RESULTS.md` written (frozen witness package; explicit non-claims) and `code/make_manifest.py` added
  (manifest generated after the 121 control runs end).
- Disclosure: at 01:18, before the lane existed, one scratch file was written outside the lane:
  `/tmp/cpcw-src/axioms.txt` (pdftotext of the source PDF; byte-identical to `sources/axioms-15-00035.layout.txt`,
  SHA-256 cd014a21...1f4c). Not deleted (lane rule); to retire it: `mv /tmp/cpcw-src ~/.Trash/`.
- 02:07:57 121 positive-control attempts ended: R4 `bin/cpcw_ls 121 6 SEED T ls_121_sSEED`, seed 1 (60 s) and
  seeds 2-6 (120 s each): all TIMEOUT with best cost 1 (runs/ls-k6). (121,6,1) NOT rediscovered; scope = these 6
  tabu runs only. CPU now idle (no lane process running).
- 02:08:07 frozen (read-only): `RESULTS.md` SHA-256 0b32f04fc5ae6c03346185e3ab23262c5066cfac371c06855228bc316dca0413,
  `RESULTS-manifest.json` SHA-256 e00e6e2561d78df1b2b04b97671e9f2278137c5bec1e9ec67a92a47d2ec2c5ca (313 files incl.
  this README as of 02:08:07).

## 2'. Final per-v status (2026-10-17 02:08 PDT; appended, supersedes the placeholder in section 2)
| v | k | status | certificate (SHA-256) |
|---|---|---|---|
| 122 | 6 | FOUND (prep ACCEPT; parent check + rebuild/replay reported PASS) | certs/v122/cpcw_122_6.txt 872912e9...51bc |
| 123 | 6 | FOUND (same) | certs/v123/cpcw_123_6.txt d499ac51...5a83 |
| 124 | 6 | FOUND (same) | certs/v124/cpcw_124_6.txt 5fefb1f5...e225 |
| 143 | 5 | FOUND (same) | certs/v143/cpcw_143_5.txt eeeada3d...06e8 |
| 144 | 5 | FOUND (same) | certs/v144/cpcw_144_5.txt b55797c7...da2c |
| 146 | 5 | FOUND (same) | certs/v146/cpcw_146_5.txt 52d69e01...a830 |
| 162 | 5 | FOUND (same) | certs/v162/cpcw_162_5.txt 7e26a43e...638a |
| 167 | 5 | FOUND (same) | certs/v167/cpcw_167_5.txt 4a46416e...2bda |
No classification, nonexistence, novelty or priority claim. Third parent checker and priority audit are parent gates.

## 4. Addendum (163,5,1) -- label TABLE-ATTESTED OPEN (log, append-only, host clock)
- 2026-10-17 02:23:05 PDT addendum contract read: `institute/runs/six-lane-2026-10-16/screening/info-2-cpcw163-addendum-contract.json`
  (SHA-256 cf56021e5473c65d083c6050cc8751c2edb156d57ebb3e84ffe3ea428a5d495b, recorded 02:22:24 PDT; not edited).
  Status basis: source Tables 1/3 + Table A1 (`notes/table3-163/NOTE.md`); the source TEXT omits 163.
  Pre-registered run (BEFORE any 163 search; new files only, under `runs/ls-163/` and `certs/v163/`):
  unchanged frozen binary `bin/cpcw_ls` (0486d138...37e5, source `code/cpcw_ls_v1.c` dbece67b...0acc), command
  `../../bin/cpcw_ls 163 5 SEED 120 ls_163_sSEED` (cwd `runs/ls-163`), seeds 1, 2, 3, 4, 5, 6 in this order,
  ONE process at a time (<= 1 CPU), stop at the first FOUND; hard stop after seed 6 or 15 min wall from launch.
  If FOUND: `certs/v163/cpcw_163_5.txt` = byte copy of the .sol, prep verifier JSON
  `certs/v163/verify_prep_cpcw_163_5.json`, exact replay of the same command in `certs/v163/replay/` with cmp.
  A miss is UNKNOWN (no nonexistence claim). Existence only; no novelty/priority claim.
- 02:23:13 PDT launched as pre-registered (`runs/ls-163/launch.txt`); **seed 1 FOUND** at 02:23:13 (13166 iterations,
  0.37 s), loop stopped (seeds 2-6 not run). `certs/v163/cpcw_163_5.txt` (read-only, 131 B):
  {0,12,17,75,107} {0,11,85,135,139} {0,3,9,19,34} {0,82,84,125,143} {0,21,65,117,118} {0,13,40,70,112}
  {0,23,49,71,126} {0,29,62,76,156}, SHA-256 27acd32017f71a009b1c99cdd541fe965978c7f65aa0f38fbc458bb500c8e0bc,
  uncovered differences 8, 155 (one +-class, as forced). Prep verifier ACCEPT (D, C, P pass;
  `certs/v163/verify_prep_cpcw_163_5.json`); inline definition check PASS (`certs/v163/direct_check.txt`);
  02:23 replay of the same command in `certs/v163/replay/`: .sol byte-identical to the certificate, .ckpt identical.
  Parent messaged 02:23:50. Lane idle afterwards. RESULTS.md / manifest (frozen 02:08) intentionally not modified;
  this section is the record for 163. Existence only; label TABLE-ATTESTED OPEN; no novelty/priority claim.
