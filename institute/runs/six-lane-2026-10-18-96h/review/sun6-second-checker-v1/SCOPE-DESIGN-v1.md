# Sun6 second independent checker: scope and design v1 (frozen BEFORE any checker code)

- Clock (/bin/date immediately before writing): 2026-10-19T17:10:01-0700
- Author: Sun6SecondChecker. Write scope: NEW `RUN/review/sun6-second-checker-v1/` only (RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h).
- Authority: source scope `RUN/control/sun5-sun6-second-checker-source-scope-v1.json` (6cc055bcd254dc4405b2876f67ae6d494534b844605dccb0f6c924662c49659a); fullgate ruling `RUN/control/sun7-full-result-computation-gate-ruling-v1.json` (4818f1ca96c99e012d758e165982ec0844228eae07ff3f38b95dc2b7a3a5eada); entry verdict `OLD/review/sun-coset6-parent-gate-verdict-v1.md` (efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29).
- Status: SOURCE ONLY. Nothing in this directory has been executed, compiled, tested or linted. No claim of verification, novelty or a new theorem.

## 1. What the checker is for

A second, separately written, exact standard-library verifier of the Sun(6) Core5(6) certificate set already accepted (computer-assisted) in the entry verdict. It replays the pinned untrusted engine output and decides, fail-closed, whether every T-consistent labelled pattern of every one of the 8 types lies in exactly one listed typed orbit whose witness verifies under the written rules. It closes nothing by itself: a parent source review, item GO, fresh stability gate and five-part release are required before it runs, and a completed PASS would only supply the second qualified checker the fullgate ruling asks for.

## 2. Independence boundary

- Read ONLY: the nine math sources named in the assignment, the entry verdict (for pins/format routes), run contracts/controls named above, and the pinned input DATA. Complete list with SHA256 in READLOG-v1.json.
- NOT read: `math16/sun-coset6/code/*`, `OLD/review/sun-coset6-independent-checker-v1/*`, the parent derivation `sun-coset6-parent-derivation-v1.md` (mathematical, but excluded to avoid any checker-logic contamination), parent auxiliary implementations/NumPy route, old controls, any Sun5 material.
- The engine is opaque. Its `code` field is parsed (string, 15 chars over 1-4) and never used for any decision; orbits are identified by `(type, rep)` only.
- No import of project code; standard library only (gzip, json, hashlib, itertools, fractions, math, os, sys, time, signal, re, argparse). Exact `int`/`Fraction` only; no float enters any decision.

## 3. Representation (structurally independent of the engine's E-order code strings)

- Vertices 0..5. Internal pattern = symmetric 6x6 integer matrix `A`.
- Universe keys are 15-character strings over '1'..'4' in LEXICOGRAPHIC pair order (0,1),(0,2),(0,3),(0,4),(0,5),(1,2),...,(4,5) ("lex key"). The format's edge order E (pairs sorted by (j,i)) is used only to parse `rep` and to recompute the published `leafcodes_sha256` cross-check.
- Enumeration is vertex-incremental in DESCENDING vertex order 5,4,3,2,1,0: when vertex k is added, its edges to already-placed vertices are assigned one at a time and every triangle {k,m,m'} with both other vertices placed is tested as soon as its three edges exist. A node is pruned only when a completed triangle fails T (a T-inconsistent triangle is contained in every completion). Leaves = complete labellings with all 20 triangles tested.
- T predicate per triangle from the format/rules table (L1, CERT-FORMAT section 2): tau_min = lcm over the three edges of alpha_e/gcd(alpha_e, r_opp), tau_max = min over the three vertices of the product of the two alphas there; consistent iff tau_min <= tau_max. gcd(alpha, r_z) read from E2-class/E3 status of z only (exact for every admissible cofactor, see MATH-BRIDGE).
- Every representative is T-checked directly on all 20 triangles (a code path separate from the enumerator's incremental tables).

## 4. Universe and orbit coverage (exact set equality)

- Types: exactly the 8 tuples (None,0,None) (None,0,0) (0,1,None) (0,1,0) (0,1,1) (0,2,None) (0,2,0) (0,2,1).
- Stabiliser of a type recomputed as all permutations p of 0..5 with p(e2)=e2 (if present) and p(e3)=e3 (if present); sizes asserted 720/120/24 (S6, S5, S4).
- Action: (p.A)[p(i)][p(j)] = A[i][j]; precomputed per p as a lex-position map.
- For each type: leaf set L (lex keys). For each line of the type: rep must be T-consistent and in L; its full stabiliser orbit is expanded; every image must be in L and unowned by another line (else DUPLICATE_ORBIT). After all lines: owned set must EQUAL L (missing count reported). No count or hash replaces this.
- Fail-closed cross-checks against run.json (untrusted summary): per type leaves_labelled, orbits (== number of lines of that type), orbit_rule_counts, leafcodes_sha256 (sha256 of sorted E-order codes joined by \n plus final \n); total_orbits; total_survivors; orbits_jsonl_sha256_uncompressed; rlp_dual_entries. pruned_nodes and seconds are informational (C20) and ignored except for strict type.
- Placement reduction: all 91 placements of (E2 none or vertex x class 1/2) x (E3 none or vertex) are mapped by an explicit S6 search; each must reach exactly one of the 8 types.

## 5. Per-rule verification (every used rule; predicates derived in MATH-BRIDGE-v1.md)

- K [v,S]: S duplicate-free subset of N=0..5 minus v; sum alpha_iv >= 5; every pair {i,j} in S has tau_min(i,v,j) == alpha_iv*alpha_vj.
- RLP [v]: for EVERY q in prod_j {1..5-alpha_vj} (itertools.product order): key "q1,...,q5|d1f1;...;d5f5" recomputed from q and neighbour statuses; dual must exist; y_x >= 0; sum_(x in S) y_x <= 1 for EVERY hereditary-allowed S among all 31 non-empty subsets (singletons always allowed; |S|>=2 allowed iff every T subset of S with |T|>=2 has a pair with maxgcd >= |T|); sum (q_x/5) y_x >= 1. maxgcd = 2^min(e2) 3^min(e3), e2 = v2(q)+{0,1,SAT} by class digit, e3 = v3(q)+{SAT if E3}, SAT = 64. Results memoised by (q tuple, status tuple) only.
- Ppair [v,[j,k]] and PB [v,S]: x_j = alpha_vj/5; u = 1/(5 gcd(r_v, alpha_jk)) from the status table at z=v; lo = u*ceil(max(tau_min(v,j,k)/(5 alpha_jk), x_j+x_k-1, 0)/u); hi = u*floor(min(x_j,x_k)/u), lowered by u iff hi == min(x_j,x_k) and the containment is barred by K2 (x_j<x_k: barred unless alpha_vj+alpha_kj<=4; x_k<x_j: unless alpha_vk+alpha_jk<=4; equal: unless both). C21 strengthening NOT used. Ppair: lo > hi. PB: lo <= hi for every pair of N and sum_S(1-x_j) - sum_pairs_S(1-x_j-x_k+hi_jk) >= 1.
- FH5 [[a,b],V,counts]: a != b; alpha_ab == 1; V recomputed = {v not in {a,b} : alpha_va == alpha_vb} must equal the witnessed set (duplicate-free) and be non-empty; counts = 7 non-negative ints (informational only). For EACH of the 7 placements e5 in (None,0,...,5): exhaustive search over the full domain (a fixed to coset 0; b and inside V-vertices all 5 singletons; forced V-vertices all C(5,c) subsets; every other vertex all 31 non-empty subsets with t=|M|). Reject iff (F3) some t_i=1 vertex has alpha_il > t_l, or (L9a hereditary F2) some coset has a member subset T, |T|>=2, without a pair of fgcd >= |T|; fgcd = 2^min 3^min 5^min with exponents v_p(t) + SAT for the E2(class2)/E3/E5 vertex and +1 for E2 class 1, SAT = 64. Safe monotone pruning: both rejection conditions are preserved under extending a partial assignment, so a rejected partial assignment rejects every completion; every complete assignment is either reached or below a rejected node. Exact accounting: (reached complete assignments) + sum over rejected nodes of (product of remaining domain sizes) must equal the full domain product, per placement. Any surviving complete assignment => FAIL (FH5_SURVIVING_ASSIGNMENT).
- N26 [v]: v != E2; alpha_vj == 2 for all j != v; alpha_jk in {2,4} for all pairs of neighbours; if v == E3 then tau_max < 3*tau_min on every neighbour triple (C11 corrected test).
- RPLP [v,certs]: len(certs) == prod(5-alpha_vj) in itertools.product order. ["R",key]: key equals the key recomputed for that q and the RLP dual check passes. ["P",vec]: 30 exact rationals (a_j N-ascending, b_j, u_p pairs lexicographic, l_p); u,l >= 0; forced ORDERED pairs (w,j): tau_min(v,w,j) >= alpha_vw*alpha_wj (product at w); columns = all (A,S) with A non-empty subset of N, no forced (w,j) with j in A and w not in A, S subset of A empty/singleton/hereditary-allowed (maxgcd for this q); every column coefficient sum_S a + sum_A b - sum_(p in A) u + sum_(p in A) l <= 1; objective sum a q/5 + sum b (5-alpha_vj)/5 - sum u*yhi + sum l*ylo >= 1, yhi/ylo = 1-(alpha_vj+alpha_vk)/5+hi/lo.
- SURVIVE (or any non-empty survivors.json) => FAIL. Ppair is supported though absent from the data.

## 6. Strict parsing (every record accounted)

- Each input file: size and SHA256 checked against hard-coded pins BEFORE parsing; orbits.jsonl.gz additionally decompressed-length and decompressed-SHA pinned. ASCII only; no CR; final newline required; no empty lines.
- JSON: duplicate keys rejected (object_pairs_hook), floats rejected (parse_float), NaN/Infinity rejected (parse_constant); `bool` never accepted as int. Unknown or missing fields rejected. run.json floats allowed only at the informational `seconds` paths (wrapped and type-checked).
- Rational strings: regex ^-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?$ , length <= 64, parsed with Fraction from integers (no float path).
- rlp_duals.json: every key matches ^[1-4](,[1-4]){4}\|[0-2][01](;[0-2][01]){4}$ ; value exactly {"value","y"}; y length 5. Every entry is parsed; entries are USED (verified on demand) or UNUSED (counted, no proof weight).
- Line accounting: each line ends in exactly one of VERIFIED / FAILED(reason) / INCOMPLETE(reason); verified+failed+incomplete == total lines is asserted.

## 7. Fail-closed lifecycle and publication interface (no scheduler/guardian reimplemented)

- Guard: absolute wall-clock deadline (required CLI integer epoch seconds), optional cancel file, SIGTERM handler that only sets a flag. Checked between all work units and every 2048 FH5/enumeration nodes. Trigger => remaining units INCOMPLETE; verdict INCOMPLETE; exit 2; never PASS.
- Verdict gate recomputed from counters, not flags: PASS iff pins+parse ok, all 8 coverage equalities true, 91/91 placement reduction, all run.json cross-checks true, verified == total lines, failed == 0, incomplete == 0, survivors == 0, no SURVIVE line, guard never triggered and not late at gate. Any failure => FAIL (exit 1); input rejection => exit 3.
- Publication: out-dir created exclusively (must not exist); REPORT.json written with O_EXCL, fsync, read back and hash-verified; then guard re-checked; then REPORT.seal.json (O_EXCL) binding report sha256, verdict and sealed time. Exit 0 ONLY if verdict PASS and seal written and verified. Any OSError => exit 4, no seal. A PASS claim requires all of: exit 0, seal present, seal hash == sha256(REPORT.json), seal verdict PASS.
- Output bounded: failure detail list capped (first 400 entries + total count). Single process, no children, no threads.

## 8. Controls (frozen before execution; see CONTROLS-PLAN-v1.json)

Hand-derived intended-reason unit/record/coverage/pipeline/lifecycle controls, each naming the clause it targets and why a defective checker would pass it. Real-data positive control = the main replay itself (expected PASS per the accepted verdict; not hand-derived). Controls are executed only after parent review + item GO by a separate harness (`code/sun6_second_checker_controls_v1.py`) that imports only the new checker module.

## 9. Dependencies stated literally (not removed)

- Sun(5) in every group: imported from the accepted Sun(5) verdict 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 (sun-coset5 proof-v4 + cumulative erratum v3), used in R1(6) (p=2 branch) and in every hereditary test with |T| = 5 (FH5 cosets, RLP/RPLP supports). That accepted result is itself computer-assisted (including its S-D handling); this checker does NOT re-verify or remove the Sun5 computation, which is a separate gate.
- Zhu Theorem 1.1 (|T| = 3,4), L0.6 (|T| = 2).
- Sun(6) in proper subgroups: ONLY in FH5 cosets with |T| = 6, valid only inside the least-order counterexample frame (H = U_aU_b has index 5, so H < G). The checker's conclusion is therefore the C18 form: no least-order Sun(6) counterexample carries a Core5(6) configuration; R1(6) + R0 then give Sun(6).
- Written rules/proofs (rules-k6-v1/v2/v3, proof-k6-lemmas-v1, erratum-v3 C1-C22, README R0/R1(6)) are inputs, not re-proved by code.

## 10. Resources (estimates are [INFERENCE], nothing measured)

One CPython 3 process, stdlib only, no children, single thread. Inputs ~0.52 MB compressed / 6.3 MB decompressed. Expected peak RSS <= 2 GiB, output <= 2 MiB, wall time <= 20 min; self-deadline proposal 2700 s. Exact plan in RESOURCE-LIFECYCLE-PLAN-v1.json.
