# f113 proof review v1 — candidate "at most 29 maximal coefficients in any AME(4,6)"

Reviewer: same-harness written-proof reviewer for assignment f113 (manifest `manifest-v1.json`, SHA-256 `13e3696bd685bd9ee36ed655a53591706a409dfb77e764e85cf04a1024af139b`, re-hashed at `2026-10-28T19:26:07-0700`). Clock observed immediately before this file was created is recorded in §8; clocks of each control run are copied from the `/bin/date` lines inside the control logs.

**Verdict: MINOR only — no FATAL, no MAJOR, no logical gap found.** Conditional on the named premise (the t≤30 packet, which carries the residual lemma, the incidence lemma, the classical no-OLS(6) theorem, the analytic AME(4,2) exclusion, and the n=5 XOR argument), the written candidate establishes: for **every** normalized complex AME(4,6) state, in **every** local product basis, and for **every** total support size, the number t of coefficients of modulus 1/6 satisfies **t ≤ 29**. The candidate's own contribution is exactly the exclusion of t = 30; that exclusion is purely combinatorial, and its combinatorial core was independently refuted by reviewer-authored code (exhaustive enumeration and two independent SAT solvers), without importing or executing any author check. This review does **not** establish a 29-saturated tensor, an attained bound, the global support minimum, any ≥45/≥46 support claim, novelty, priority, a formal/kernel proof, an independent-family verdict, or human review.

## 0. Inputs: hashes and read order

All seven manifest inputs were re-hashed before reading (`shasum -a 256`, `wc -c`, `wc -l`, observed `2026-10-28T19:26:07-0700`) and every SHA-256, byte count and LF count matched the manifest exactly. They were then read completely, in manifest order 1→7, before any control was written:

| # | file (under `physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/`) | SHA-256 | bytes/LF | role |
|---|---|---|---|---|
| 1 | `frontier-20261028-global-ame46-lower42-review-packet-v2.md` | `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` | 11168/107 | premise (t≤30) |
| 2 | `frontier-20261028-global-ame46-maximal-coefficients29-v1.md` | `2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c` | 7902/54 | candidate under review |
| 3 | `frontier-20261028-signed-k4-matching-bound-v1.py` | `2e54209c76a277818a702c6c51049119b221d0c666dbfbce1a5b4e7da8ef67b5` | 2286/42 | author control (read only) |
| 4 | `frontier-20261028-signed-k4-matching-bound-v1.json` | `a81641c7129f790aef937efb2c914d08f0590b31c693dadfabdde000d6dda65a` | 699/46 | author receipt (read only) |
| 5 | `frontier-20261028-n6-maximal-code-z3-v1.json` | `516cba122e2a7fbd252ccf06267e66410ab8e393089e0fe91c4d8b0f5690c083` | 5547/460 | partial P code (read only) |
| 6 | `frontier-20261028-n6-maximal-code-independent-v1.py` | `b3d3d4e1b422f038edcfc6a9b3a9cae07c962ffa623a364b9f3053860a4937ec` | 3424/71 | author checker (read only) |
| 7 | `frontier-20261028-n6-maximal-code-independent-v1.json` | `9c71a81344dc094491cb082b8ba375c626ec76a7010266fac414149f4549a421` | 2657/195 | author receipt (read only) |

Author code (inputs 3, 6) was neither imported nor executed; their receipts (4, 7) were used only as numbers to cross-compare with my own enumerations.

## 1. Exact statement reviewed, with all variables

Let ψ ∈ (ℂ⁶)^{⊗4} be any unit vector whose six two-party reduced states all equal I₃₆/36 (AME(4,6); equivalently every 2|2 flattening U = 6ψ is a 36×36 unitary). Fix any product basis and write ψ_{abcd} for the coefficients. Let P = {(a,b,c,d) : |ψ_{abcd}| = 1/6}, t = |P|, E = supp(ψ) \ P, n = 36 − t, N = |supp(ψ)| = t + |E|.

Candidate claim: t ≤ 29. Quantifiers: for all such ψ, for all product bases, with no restriction on N. The candidate proves the single statement **t ≠ 30** (candidate §§2–5) and obtains t ≤ 29 by combining with the premise **t ≤ 30** (candidate §6 last line). "In the published 60-term example the number is 12" (candidate §1) is a side remark outside the manifest inputs; it was not verified and is not load-bearing.

## 2. Exactly how the prior t≤30 / no-OLS(6) import enters

1. **Cases t ∈ {31,…,36} are excluded only by the premise**, not by the candidate: t=36 by no-OLS(6) (the only external theorem anywhere in the chain); t=35 by the singleton residual rule; t=34, 33 by the incidence lemma (r ≤ ⌊3n/5⌋ ≤ 1); t=32 (n=4) by the analytic AME(4,2) nonexistence argument (Pauli expansion and spin flip, packet §3); t=31 (n=5) by the three-fiber normal form and XOR argument (packet §§4–5).
2. **Two premise lemmas are reused as tools inside the t=30 argument**: the residual lemma (packet §1: singleton rows/columns, residual n×n unitary with ≥2 nonzeros per row/column, hence |π_ij(E)| = n with ≥2 E-extensions per projected cell, |E| ≥ 2n) and the incidence lemma (packet §2: r_i ≤ ⌊3n/5⌋, giving r_i ≤ 3 at n=6). I re-derived both in §3.1–3.2 below; they use nothing beyond 2|2 unitarity.
3. **no-OLS(6) does not enter the t=30 argument at all.**
4. **Nature of the dependency, by own control (§4, C3):** the purely combinatorial (P,E) abstraction of "n residual cells per pair" is UNSAT at n=6 and at n=5, but **SAT at n=4**. So the premise's t=32 exclusion is genuinely analytic (it needs the AME(4,2) impossibility, not just counting), while the candidate's t=30 exclusion needs no analytic input beyond unitarity-derived counting. The conditional t≤29 claim therefore inherits two non-combinatorial dependencies from the premise: Tarry's no-OLS(6) theorem and the AME(4,2) nonexistence argument.

## 3. Step-by-step reconstruction of the written argument

### 3.1 Residual lemma (premise §1, reused) — holds
In any cut ij|kl the row of U=6ψ indexed by (x_i,x_j) has unit norm; a modulus-1 entry therefore exhausts its row and column, so distinct P words never share two coordinates and π_ij is injective on P. Removing the t matched singleton rows/columns leaves an n×n block that is unitary (U is block-diagonal after permutation). A residual row with a single nonzero would have modulus 1 and lie in P, so every residual row/column has ≥2 nonzeros, all in E. Hence for each of the six pairs, |π_ij(E)| = n, every projected cell has ≥2 E-extensions, and |E| ≥ 2n. ✔

### 3.2 Incidence lemma (premise §2, reused) — holds
Fix i, r = |π_i(E)|. A fiber E_v varying in no other coordinate is a single tuple; varying in only j makes (v, x_j) determine the tuple; either way some projected cell has one extension, contradicting 3.1. So every fiber varies in ≥2 other coordinates. Σ_v(|π_j(E_v)|−1) = |π_ij(E)| − r = n − r bounds the number of fibers varying in j by n−r; so 2r ≤ 3(n−r), r ≤ ⌊3n/5⌋; at n=6, r_i ≤ 3. ✔

### 3.3 Candidate §2: alphabet profile — holds
r_i r_j ≥ |π_ij(E)| = 6 with r_i ≤ 3 leaves profiles (3,3,3,3) and (2,3,3,3). For a fixed j, π_ij is injective on P and π_ij(E) ⊂ R_i×R_j, so #P words active at i = 6r_i − 6 and #P words active at both i,j = r_i r_j − 6. Double counting gives identity (1): Σ_x [k(x) − C(k(x),2)] = Σ_i(6r_i−6) − Σ_{i<j}(r_i r_j − 6). Per-word values 0,1,1,0,−2 for k=0..4, maximum 1, so LHS ≤ |P| = 30. For (2,3,3,3): RHS = 42 − 9 = 33 > 30. ✔ (For (3,3,3,3): RHS = 48 − 18 = 30, forcing k(x) ∈ {1,2} for every P word — not used by the candidate, but it matches the Z3 code's 12/18 pattern histogram, §6.) Own control C2 confirms by solving the full 16-unknown pattern-count integer system: infeasible for all four placements of (2,3,3,3), feasible for (3,3,3,3).

### 3.4 Candidate §3: partner-degree invariance and perfect matchings — holds
For active a ∈ R_i and any j ≠ i, the m_i(a) P words with x_i = a have distinct x_j, and every cell (a,b) is either a P-cell or an E-cell (3.1), so d_ij(a) := #{b : (a,b) ∈ π_ij(E)} = 6 − m_i(a), independent of j. The fiber E_{i=a} is nonempty (a ∈ π_i(E)) and varies in ≥2 other coordinates (3.2), so some d_ij(a) ≥ 2, hence all are. Σ_{a∈R_i} d_ij(a) = |π_ij(E)| = 6 over three symbols forces d_ij(a) = 2 for all a, j; symmetrically for columns. Every 3×3 residual projection is 2-regular and its complement M_ij in R_i×R_j is a perfect matching. ✔ (Own P-code check C4 observes exactly m_i(a) = 4 on active and 6 on inactive symbols in the Z3 diagnostic code, as this step predicts.)

### 3.5 Candidate §4: three-cube edge bound — holds
Relabel R_B, R_C, R_D so that M_AB, M_AC, M_AD are identities (possible because each is a perfect matching). For A = a, each of B, C, D ranges over the two symbols ≠ a: an 8-vertex cube. Case split on the interleaf permutations f=M_BC, g=M_BD, h=M_CD is exhaustive: (i) if some interleaf matching fixes a, it bijects the other two symbols, forbidding two of the four allowed pairs and hence 4 cube vertices; ≤4 survive. (ii) if none fixes a, each forbids exactly one allowed pair (the unique b ≠ a with f(b) ≠ a), i.e. a cube edge parallel to the axis not in the pair; three edges parallel to three different axes are distinct; three distinct edges on only three vertices would be K₃, impossible in the bipartite cube; so ≥4 vertices are forbidden and ≤4 survive. Hence |E| ≤ 3·4 = 12, and with |E| ≥ 2n = 12 equality holds with exactly two E-extensions per projected cell. ✔ Own control C1 (all 6⁶ = 46656 matching configurations, no relabeling): max |S| = 12, max per A-fiber 4, three-cube-edge minimum cover 4.

### 3.6 Candidate §5: equality-case fiber contradiction — holds
Each A-fiber has exactly 4 tuples; within it each of B, C, D takes the two symbols ≠ a, each exactly twice (exactly two extensions of the cells (a,b), (a,c), (a,d)). For a pair jk ⊂ {B,C,D} the 2×2 contingency table with margins (2,2),(2,2) is either [[1,1],[1,1]] (full square) or [[2,0],[0,2]]/[[0,2],[2,0]] (perfect correlation) — the dichotomy is exact. Two correlated pairs in one fiber share a coordinate and make the triple a function of one binary coordinate, giving ≤2 tuples, so each fiber is correlated on ≤1 pair. The potential (j,k)-squares of fibers a ≠ a′ are (R_j\{M_Aj(a)})×(R_k\{M_Ak(a)}) and intersect in exactly one point because M_Aj, M_Ak are matchings; two full squares give ≥7 > 6 = |π_jk(E)| projected cells. So ≥2 of the 3 fibers are correlated on each of the 3 pairs: ≥6 fiber/pair correlations against ≤3 available. Contradiction. ✔ Own control C1 finds that in every one of the 1296 unrelabeled 12-configurations the maximal avoiding set already violates the ≥2-extension condition in four of the six projections, so no E can reach the start of §5 at all; the written §5 derivation is nonetheless valid as written (it derives a contradiction from the equality hypotheses).

### 3.7 All support sizes
No step assumes anything about N: |E| is an unknown bounded below by 2n (3.1) and above by 12 (3.5) under the sole hypothesis t = 30; the contradiction is reached for every conceivable E. The claim is therefore a structural all-state, all-basis, all-support statement, as asserted in candidate §1. ✔

## 4. Independent controls (reviewer-authored code only; author code neither imported nor executed)

| id | artifact(s) | what it tests | result | clock(s) |
|---|---|---|---|---|
| C1 | `proof-control-matching-exhaustive-v1.py` → `…-v1.json` | all 6⁶=46656 six-matching configurations on {0,1,2}⁴ with no relabeling: (a) max avoiding set, max per A-fiber; (b) whether any avoiding set satisfies condition (1) (monotone, so suffices); (c) 3-cube edge lemma; (d) author's relabeled numbers | (a) 12 and 4; (b) **0 of 46656**; (c) 4; (d) histogram {0:1,4:18,6:98,7:18,8:36,10:39,12:6}, max 12, drop-CD 15 — all agree with author receipt input 4 | run `2026-10-28T19:34:26-0700`→`19:34:27-0700`, 0.99 s |
| C2 | `proof-control-profile-count-v1.py` → `…-v1.json` | exact feasibility of the full 16-unknown active-pattern count system for every profile in {1,2,3}⁴ with all pair products ≥6; identity (1) RHS | (2,3,3,3) and its 3 permutations **infeasible** (RHS 33); (3,3,3,3) feasible (RHS 30; witness 12 one-active + 18 two-active words) | 0.18 s; ran between `19:37:30` and `19:39:12` (−0700), no in-log clock |
| C3a | `proof-control-t30-sat-v1.py eonly` → `proof-control-t30-eonly-v1.cnf`, `…-kissat-v1.log`, `…-model-v1.json` | E only (81 vars): is condition (1) with six 6-cell projections satisfiable by some E ⊂ {0,1,2}⁴ without P? | **SAT**: |E| = 20, profile (3,3,2,3), projections not 2-regular — shows candidate §§2–3 (P-side counting) are load-bearing | kissat 0.19 s; first run `19:36:12`→`19:36:13` (−0700); the saved log is an identical re-run between `19:36:24` and `19:37:26`, no in-log clock |
| C3b | `proof-control-t30-sat-v1.py full` → `proof-control-t30-full-v1.cnf` (3105 vars, 150936 clauses); logs `…-full-kissat-v1.log`, `…-full-cadical-v1.log` | complete combinatorial abstraction of t=30: P ⊂ [6]⁴, E ⊂ {0,1,2}⁴ (WLOG from r_i ≤ 3, re-derived in §3.2); every cell of every pair is a P-cell (exactly one P word, no E) or an E-cell (no P, ≥2 E); exactly 6 E-cells per pair; cardinality by exact sequential counter | **UNSAT** (kissat 4.0.4, 46.76 s wall) and **UNSAT** (cadical 3.0.1, 129.59 s wall) — two independent solvers | kissat `19:36:24`→`19:37:11`; cadical `19:37:26`→`19:39:35` (−0700) |
| C3c | `proof-control-tn5-full-v1.cnf`, `…-kissat-v1.log` | same abstraction at n=5 (t=31) | UNSAT, 0.68 s (consistent with premise §§4–5; premise not re-verified here) | `19:39:12`→`19:39:13` |
| C3d | `proof-control-tn4-full-v1.cnf`, `…-kissat-v1.log`, `…-model-v1.json` | same abstraction at n=4 (t=32) — positive control for the encoding and characterization of the premise's analytic step | **SAT**, 0.13 s; model (32 P words, 16 E words, profile (2,2,2,2)) validated directly against the abstraction by `proof-control-decode-model-v1.py` (`abstraction_check.valid = true`), so the encoding is not over-constrained | `19:39:13` |
| C3e | `proof-control-t30-unres-v1.cnf` (4320 vars, 165354 clauses), `…-unres-kissat-v1.log` | n=6 with E ⊂ [6]⁴ (no r_i ≤ 3 import at all) | **UNKNOWN** at the 3000 s cap — INCONCLUSIVE; not needed because r_i ≤ 3 is re-derived in §3.2 | `19:37:30`→`20:27:31` |
| C4 | `proof-control-pcode-check-v1.py` → `…-v1.json` | own verification of the Z3 30-word P code (input 5, SHA-256 re-hashed `516cba12…`) | 30 distinct words, pair-injective in all six pairs; missing cells are identity perfect matchings inside {0,1,2}²; m_i(a) = 4 (active) / 6 (inactive); pattern histogram {1:12, 2:18}; **0 compatible E tuples**; no amplitude/phase/E keys present | ran between `19:37:30` and `19:39:12` (−0700), after C2, no in-log clock |

Generator reproducibility: after adding the residual-size parameter, `proof-control-t30-sat-v1.py full` regenerated the n=6 CNF and `.map` byte-identically (`cmp` clean) to the files solved in C3b.

## 5. Findings

No FATAL. No MAJOR. No gap in the written argument.

- **MINOR-1 (wording, candidate §1).** "Equivalently it cannot have 30 saturated entries" is an equivalence only together with the premise t ≤ 30; the candidate's own proof excludes exactly t = 30. The last line of §5/§6 states the combination correctly; §1 should say "given the dependency's t ≤ 30".
- **MINOR-2 (informational, candidate §5).** The equality case is already dead one step earlier than the written derivation uses: control C1 shows every 12-tuple avoiding set has a single-extension cell in four projections, so "every pair projection value has exactly two E extensions" (end of §4) is never attainable. The written §5 argument is valid as written; this only notes that it could be shortened. No change required.
- **MINOR-3 (unverified side remark, candidate §1).** "In the published 60-term example the number is 12" is outside the manifest inputs and was not checked; nothing depends on it.
- **MINOR-4 (presentation, candidate §4).** "If that matching fixes a" is stated for one interleaf matching while the second bullet is "if none … fixes a"; the case split is exhaustive as intended (some vs. none) but the first bullet could say "if some interleaf matching fixes a".

## 6. Partial P-code versus AME witness

Input 5 is a 30-word classical code satisfying pair-injectivity and the active-pattern counts; it carries no amplitudes, no phases and no E support (own check C4: record keys are `direct_integer_pair_verification, records, scope, solver, status, timeout_ms`). Its six residual matchings are all identities, so no 4-tuple of [6]⁴ projects into all six residual cell sets (C4: 0 compatible E tuples); this particular code cannot be extended to any AME(4,6) state. More strongly, C3b shows **no** 30-word P code admits any compatible E meeting the residual condition. Nothing in the manifest is, or is claimed to be, an AME(4,6) tensor with 30 (or 29) maximal coefficients; the candidate correctly makes no sharpness or attainment claim.

## 7. Consequence observed, not claimed by the candidate and not adopted here

The premise's inequality (2), N ≥ 72 − t, combined with t ≤ 29 would give N ≥ 43 for every AME(4,6) state in every product basis. The candidate does not state this; I record it only so the parent can see that accepting the candidate moves the support frontier by exactly one from the premise's 42, no further. It is not a ≥45/≥46 claim and no such claim is supported by anything reviewed here.

## 8. Artifacts written by this review (all new, `proof-` prefixed, under the review directory)

SHA-256 (`shasum -a 256`, observed `2026-10-28T20:27:40-0700`):

```
d772c30b2c0c6ffee7045ea54dc2895f191a355459eed47cdb74fd28a2332bd7  proof-control-matching-exhaustive-v1.py
82d05f89f8c3c0fae1f1693779d7549fd6d6eb043beb25c52f4e637bb6efc03a  proof-control-matching-exhaustive-v1.json
f9f48315208de69a5ae5679e37dfba021055d6aa1ab6345b13b57753594c0adc  proof-control-profile-count-v1.py
c8c690b26f8c4dddffc057be32c9db8c6d3f56d2d2b92ab68ea481978fa6fa79  proof-control-profile-count-v1.json
df1ce654e9ab072e164a8ab8f35fb4cbe26de656a81b89a83b5e96ebe685aa5c  proof-control-t30-sat-v1.py
20a2b416f796e2cea288bbfa322398fdddd93e773379c4a227f3d59171d28356  proof-control-decode-model-v1.py
515765c64d42c5712757a53aa6f1a2ea74791e7552b844c1bba059ffb83190df  proof-control-t30-eonly-v1.cnf
26f8ae950c1b580dae5e6007d83571a78871090b0b7ba2d9be0bf6ba09994d9b  proof-control-t30-eonly-v1.cnf.map
c8487cf2d61b0438817c04e023dda3b602d7495faa42e0f3e460855a66145040  proof-control-t30-eonly-kissat-v1.log
bdb210a6345e8852e6f5bfeabb110ea9e6fa24bbe499590dcb50f93012c9db05  proof-control-t30-eonly-model-v1.json
7cd15d42f8f44696015b33eddc7a524f7bb007563370588e216b90b3a3273b31  proof-control-t30-full-v1.cnf
ed7e1c4d6aaa9267fda50e23b56f71123500174184c8e1d3f0cd845e500fd6ca  proof-control-t30-full-v1.cnf.map
1f587f735f6a2f7e97a05b966ab3638b341cd82d352da498b03a412d5dba4197  proof-control-t30-full-kissat-v1.log
7058a5ba9f9eb66cc7b412e9b490b4e4254347ad95f13528df75e1d72bfacf35  proof-control-t30-full-cadical-v1.log
6ae5c5a41e5c04967ba3cd8dd79db1839edae876391180b0694fce8199da7f40  proof-control-t30-unres-v1.cnf
bf563e3ca9a11ddac5aab63d814a8bd912cb5a45a5c0a737a76356328d3e6275  proof-control-t30-unres-v1.cnf.map
66b90cc71881c8122b1d04224638dea693a19706de2dd9c87b1f48e28b93097e  proof-control-t30-unres-kissat-v1.log
26dd08dc2af7613ba370eb0a5a2038691616024cb6faadddf6317273333f30c7  proof-control-tn5-full-v1.cnf
ed7e1c4d6aaa9267fda50e23b56f71123500174184c8e1d3f0cd845e500fd6ca  proof-control-tn5-full-v1.cnf.map
a31be38811d3a09827b3f2431ca58448dccf256d02a43aa651e254ce1f8551cd  proof-control-tn5-full-kissat-v1.log
3ed7ff4c4a798afa1b7e1528da15b883e557b8eb96da7ab2171a03f3cc5be78d  proof-control-tn4-full-v1.cnf
7eae39f261b509f9b625437ed4922d48b039a4aa3a4fe9ae6900ab4544be3cdd  proof-control-tn4-full-v1.cnf.map
540ef78ab627f9317f0c16701a7d95a3100edb1c67d4f6a071e76d114dc53fb5  proof-control-tn4-full-kissat-v1.log
ffc2e04a079a2874f6290828546e7f93df2c213c85ec5ed6a4b8d2cca9b52a68  proof-control-tn4-full-model-v1.json
d53e112f006d8f85cc3341f508ee04be57b52fb48a41de9bced6df905482bd11  proof-control-pcode-check-v1.py
2b8257d0c1dc7d1bcc8fbb4022ccfff18a1c54888f8b11847ea99daccc2f71bc  proof-control-pcode-check-v1.json
```

Process notes: one in-progress bug in my own `proof-control-profile-count-v1.py` (inconsistent recursion return) crashed before writing its receipt; it was fixed in place and the receipt above is from the fixed run. The sibling `finite-*` and parent `parent-*` files present in the directory were not read, used, or touched. No manifest input was modified (hashes re-checked in §0). Solvers: kissat 4.0.4 and cadical 3.0.1 from the local Homebrew install; no DRAT/LRAT checker was available, which is why two solvers were cross-run instead of certificate-checking. Clock immediately before creating this file: `2026-10-28T20:30:32-0700`.

## 9. Limits of this review

Same-harness review by the same model family that produced the candidate: it is not human review, not an independent-family verdict, not a formal/kernel proof, and not a novelty or priority audit. The premise's own t≤30 chain was not re-verified beyond the two lemmas actually reused (§3.1–3.2); its n=4 and n=5 steps are taken as named premise, and C3c/C3d only characterize which of them are combinatorial. No external source, model, paid API, author contact, Git, deletion, publication or infrastructure action was used.
