# Active-count slice review: candidate global AME(4,6) support lower bound 46

Reviewer: same-harness independent reviewer (Claude, this session), slice `active-count` of manifest `manifest-v1.json`. Native clock read immediately before this write: `Wed Oct 28 19:26:06 PDT 2026` (= `2026-10-29T02:26:06Z`); this is a lower bound on the write time, not an exact completion time. **This is a same-harness written review**: it is not human review, not independent-family review, not formal/kernel verification, and not a novelty or priority audit.

## 0. Pins, read order, independence

- Manifest `manifest-v1.json`: SHA-256 `725e7c0d12bb013128ac9d11b15aba6355292578070b71b65c25f9c2c5d709a4` observed at `19:13:39 PDT`, equal to the pin given in my assignment. **Match.**
- All ten manifest inputs were hashed before reading; every SHA-256, byte count and LF count equals the manifest pin (verified in one `shasum`/`wc` pass at ~19:14 PDT). **No mismatch.** Inputs were then read completely, in manifest order, with `:raw` reads.
- The authority file `contract-addendum-2-frontier-first-owner-direction-v1.json` was read for scope.
- Author control code/receipts (`unitary-three-excess-controls-v1.py/json`, `active-count-control-v1.py/json`) were read for scope only. They were **not executed** and are **not used as evidence** below. My own controls were written from scratch (they overlap in purpose, not in code).
- Sibling-slice artifacts (`unitary-excess-review-v1.md`, `excess-*`) were present in the review directory when I listed it at ~19:21 PDT. I did **not** read them; nothing below depends on them.
- No author contact, external model, paid API, Git, deletion, publication or infrastructure action was taken. The only writes are the `active-`-prefixed files listed in §9.

## 1. Prerequisite ledger (what is assumed vs. what I re-derived)

The ≥46 candidate (`...support-lower46-v1.md`) claims: every normalized complex AME(4,6) state in every product basis has support ≥46. Its argument is: N≤44 is excluded by the ≥45 dependency; N=45 splits into t∈{27,28,29,30}; each case is excluded.

| Ingredient | Status in this review |
|---|---|
| N≤44 excluded (≥45 candidate, which itself rests on ≥44 and ≥42) | **CONDITIONAL — not re-proved here; separately under review** |
| t≤30, i.e. n≥6 (≥42 packet §1–§5: n=0 via no-OLS(6); n=1; n=2,3; n=4 AME(4,2) Pauli argument; n=5 XOR argument) | **CONDITIONAL — not re-proved here** except the n=0 (OLS) and n=1 steps, which I checked. It enters the ≥46 case split: without it t∈{31,32} (n=5, n=4) would remain open. |
| Classical no-OLS(6) (Tarry) | **External classical import, kept conditional/explicit**; it enters only through t≤30 and through the ≥44/≥45 chain, not through the n=7 argument itself. |
| Residual-unitary setup: maximal coefficients are singleton rows/columns in every 2\|2 cut; residual n×n block is unitary with no singleton line; π_ij(E) has exactly n values each with ≥2 E-extensions; N≥72−t (≥42 packet §1) | **Re-derived by me (§2 below).** |
| Incidence lemma 2r≤3(n−r) and "every fiber varies in ≥2 other coordinates" (≥42 packet §2) | **Re-derived by me (§5 below).** |
| 2n lemma (even n) and 2n+1 lemma (≥44 packet §2) — used for t=27, t=28 | **Re-derived by me (§3 below).** |
| 2n+2 classification (used by ≥46 only via "max residual row/column degree ≤3" for n=7) | **The needed part re-derived by me in two ways (§4), plus the full odd-n classification checked; exhaustive n=7 support control (B).** |
| 2n+3 classification (even n impossible) — used for t=30 | **Primary responsibility of the `unitary-excess` slice. I re-derived the author's argument step by step (§3.3) as a secondary same-harness check; I keep it conditional on that slice's verdict.** |
| n=7 fiber argument (no four-symbol residual alphabet; all alphabets size 3) | **New in ≥46; re-derived by me (§5).** |
| Active-coordinate counting 44−12=32>29 | **New in ≥46; re-derived by me (§6), with arithmetic, multiplicity and exact-cover controls (A, C).** |

## 2. Setup re-derivation (used by every case)

Fix a product basis. For every pair {i,j}, 2-uniformity ρ_ij=I/36 is equivalent to the 36×36 flattening M (rows (x_i,x_j), columns (x_k,x_l)) satisfying MM†=I/36, so U=6M is unitary; every row and column of M has squared norm 1/36. Hence |ψ_x|≤1/6, and if |ψ_x|=1/6 ("maximal", x∈P) then in **every** cut x's row and column contain no other nonzero. Consequences I checked: (a) two distinct P words never agree in two coordinates; (b) no E word agrees with a P word in two coordinates; (c) in each cut, after permuting, U = (t one-dimensional unitary blocks) ⊕ (an n×n block), and a block-diagonal unitary has unitary blocks, so the residual block is unitary; (d) a singleton row/column of a unitary has modulus-1 entry, i.e. a maximal coefficient, so the residual block has every row and column degree ≥2; (e) the residual rows of the cut ij|kl are exactly π_ij(E) (n of them) and the residual row degree of (a,b) equals the number of E extensions of (a,b); (f) the 36 pairs of each ordered coordinate pair are partitioned into t P-rows (bijective with P) and n E-rows; (g) |E|≥2n hence N≥72−t. All of this holds for all six coordinate pairs because each is the row system of one cut and the column system of the complementary cut (basis-orientation point: rows and columns of a unitary satisfy identical hypotheses, and the partition in (f) is the same whichever side indexes the pair).

## 3. The four N=45 cases

N=45 and N≥72−t give t≥27; the conditional t≤30 gives t∈{27,28,29,30}, with |E|=45−t and n=36−t: (t,n,|E|) = (27,9,18), (28,8,17), (29,7,16), (30,6,15). Arithmetic checked. The list is complete given t≤30.

**Basic fact used throughout.** Two distinct rows (or columns) of a unitary whose supports intersect in exactly one position have a one-term, nonzero inner product; impossible. ("No unique overlap.")

### 3.1 t=27: |E|=2n with n=9 odd — excluded (re-proved)
All row and column degrees are ≥2 and sum to 2n, hence all equal 2. The bipartite support graph is 2-regular, a disjoint union of even cycles. In a cycle of length ≥6 two consecutive rows share exactly one column — unique overlap. So every component is a 4-cycle, i.e. a full 2×2 block, and n is even. n=9 is odd. ✓

### 3.2 t=28: |E|=2n+1 with n=8 — excluded (re-proved)
Exactly one row R has degree 3 (columns {a,b,c}); all other rows have degree 2. Every column has degree ≥2, so each of a,b,c has a neighbour row S≠R; S meets R and must meet it in ≥2 columns, so supp(S) is a 2-subset of {a,b,c}. Two such rows with different 2-subsets overlap in exactly one column — forbidden; so all neighbours of R use the same 2-subset and the third column has degree 1. Contradiction. ✓ (The argument does not use amplitudes beyond "no unique overlap"; it holds for any n.)

### 3.3 t=30: |E|=2n+3 with n=6 even — excluded conditionally (other slice primary; my step-by-step re-derivation)
I re-derived the author's argument: (i) components of the support graph of a unitary are square (rows of a component are orthonormal inside it, likewise columns); (ii) component excess r=nnz−2m≥0 is additive; excess 0 forces a full 2×2 block (§3.1); excess 1 is impossible (§3.2 applied to the component's own unitary block); so total excess 3 lives in a single connected component of size m≥3; (iii) in that component degree-2 rows have pairwise disjoint supports (equal supports would span C² on those two columns, forcing all other rows to vanish there and splitting off a 2×2 component; a one-column overlap is forbidden); hence s≤b, b≤3, m≤6; (iv) each degree-2 pair is met by ≥2 higher rows, each meeting both columns (a single higher neighbour would make the pair's two columns a 2×2 unitary with that neighbour's norm exhausted, splitting a component); (v) m=4: (s,b)=(2,2) forces higher degrees (3,4) but a higher row meets each pair in 0 or 2 columns so has even degree; (s,b)=(1,3) forces three degree-3 rows each = pair + one unpaired column, giving 3<4 incidences for the two unpaired columns; m=5: (2,3), three degree-3 rows each = one pair + the unpaired column, 3<4 pair incidences; m=6: (3,3), higher rows are unions of pairs, even degree ≠3; m=3: full 3×3. So n is odd. Every step checked; I found no gap. I nonetheless record this as **conditional on the `unitary-excess` slice**, which is the assigned primary check, and note that my re-derivation follows the author's outline rather than an independent route.

### 3.4 t=29: |E|=2n+2 with n=7 — the slice's main case; see §4–§6. Excluded (re-proved).

## 4. Maximum residual degree ≤3 from "exactly 2n+2 nonzeros" (what the ≥46 packet needs from the 2n+2 classification)

Row degrees are ≥2 and sum to 2n+2, so the excess is 2: either one row of degree 4 or two rows of degree 3 (same for columns). So the only content needed is **no degree-4 row/column**. I re-proved it two ways.

**(a) General argument (any n≥3).** Let R have support {a,b,c,d}; all other rows have degree exactly 2. Each column has degree ≥2, so each of a,b,c,d has a non-R neighbour, which must meet R in both of its columns, i.e. is a 2-subset of {a,b,c,d}. Two occurring 2-subsets overlapping in one column give a unique overlap, so the occurring 2-subsets are pairwise disjoint and cover {a,b,c,d}: they are two disjoint pairs, say {a,b},{c,d}. If two rows S,S′ both had support {a,b}, their restrictions to (a,b) are orthonormal, span C², and R|_(a,b)≠0 is orthogonal to both (S,S′ vanish elsewhere) — impossible; so exactly one row S has support {a,b}, columns a,b are supported on rows {R,S} only, and these two orthonormal columns make the 2×2 submatrix on {R,S}×{a,b} unitary. Then |R_a|²+|R_b|²=1, contradicting R_c,R_d≠0. Transposing U gives the column statement. ✓

**(b) Simpler argument valid for n≥5 (so for n=7).** With n≥5 there is a column e∉{a,b,c,d}; a degree-2 row containing e cannot contain a column of {a,b,c,d} (that would be a unique overlap with R), so every row touching a column outside {a,b,c,d} is a 2-subset of that complement. For n=7 the complement {e,f,g} has three columns; any two distinct 2-subsets of it overlap in exactly one column, so all such rows have the same support and one of e,f,g has degree 0, contradicting column degree ≥2. (For n=5 the lone outside column cannot reach degree 2 at all. For n=6 the two outside columns {e,f} are carried by rows with support exactly {e,f}; two such rows span C², so there are exactly two and they split off a 2×2 block, leaving a 4×4 block with 10 entries — the n=4 instance of the degree-4 case, which needs argument (a). n=7 does not.) Purely combinatorial (no C² or norm step). ✓ This means the n=7 degree bound rests on strictly less than the sharp classification; see MINOR-1.

I also re-derived the full odd-n classification (two degree-3 rows R,S must share all three columns; exactly one degree-2 row inside those columns; a 3×3 block with 8 entries splits off; the rest is 2-regular, hence 2×2 blocks; n odd), confirming the packet's description "one 3×3 eight-entry block and two full 2×2 blocks" for n=7. Only "max degree ≤3" is used downstream.

**Control B (mine).** Exhaustive enumeration of 7×7 0/1 patterns with 16 ones, all row masks of popcount 2..4, row/column degrees ≥2, no unique row or column overlap, square components, rows taken in non-decreasing order: 18,585 row-filtered leaves (7,140 of them with a degree-4 row), 18,060 rejected by column degree/overlap, 210 rejected as rectangular components, **315 survivors, all of shape (3×3 with 8) ⊕ (2×2) ⊕ (2×2), maximum row/column degree 3; every degree-4-row leaf was rejected.** 315 = C(7,3)·3·3 matches the hand count for labelled columns up to row order. These are necessary-condition pattern checks, not unitary realisability.

**Orientation.** The residual block in cut ij|kl has rows π_ij(E) and columns π_kl(E); the transposed block (cut kl|ij) is also unitary with the same hypotheses, so "no pair value has more than three E extensions" holds for all six coordinate pairs, as the packet asserts.

## 5. The n=7 fiber argument (re-derived)

**Incidence lemma.** Fix coordinate i with r values; fibers E_v. (i) Every fiber varies (≥2 values) in at least two other coordinates: a fiber constant in all three is one point and its pair (v,x_j) has one extension; a fiber varying only in j has, for each j-value, exactly one point, so that pair has one extension — both contradict (1). (ii) For each j≠i, π_ij(E)=⊔_v {v}×π_j(E_v), so Σ_v(|π_j(E_v)|−1)=n−r and at most n−r fibers vary in j. Summing over the three j: 2r≤3(n−r). For n=7: r≤4. ✓

**No four-valued residual coordinate.** Suppose A has four values. Each fiber varies in some j; each of the ≥2 j-values forms a pair (v,w) with ≥2 extensions, all lying in E_v and disjoint across w; so |E_v|≥4. Four fibers, |E|=16, so |E_v|=4 exactly. Now fix any j≠A. If j were constant (=w) on E_v, the residual row (v,w) of the cut with rows (A,j) would have degree 4, contradicting §4. So j takes ≥2 values on each of the four fibers and |π_Aj(E)|≥8>7. Contradiction. ✓ (The §4 degree bound is genuinely load-bearing here: Control A shows the counting inequality of §6 alone does **not** reject r=(3,3,3,4), whose left side equals the bound 29.)

**All alphabets have exactly three values.** If r_i≤2 then |π_ij(E)|≤r_i·r_j≤2·3=6<7 for any j. So r_i=3 for all four coordinates. ✓

Side consequence I derived (useful consistency check, not needed): since #{x∈P: x_i=a}=6−|π_j(E_a)| is independent of j, each residual fiber has the same number of distinct values in every other coordinate; for n=7 the fiber profile per coordinate is therefore {3,2,2}, i.e. every fiber varies in all three other coordinates. Control C confirms: all surviving residual supports have both missing pairs of every projection in distinct rows **and** distinct columns of the 3×3 symbol grid (orbit slices with two missing pairs in a common row or column have zero survivors).

## 6. The counting identity (re-derived, with edge cases)

Let R_i=π_i(E), |R_i|=3. Call P word x active at i if x_i∈R_i; k(x)∈{0,…,4}.

**Per party (6r_i−n).** In the cut with rows (i,j), the 6·3=18 rows (a,b) with a∈R_i split into E-rows and P-rows. Every E-row has a∈R_i by definition of R_i, so all n=7 E-rows are among these 18; the other 11 are P-rows, in bijection with P words having x_i∈R_i. Hence exactly 11 P words are active at i, **for every choice of j** (the count is intrinsic to P, so it must be j-independent, and it is). ✓

**Per pair (r_ir_j−n).** Of the 9 pairs in R_i×R_j, all 7 of π_ij(E) lie inside (π_ij(E)⊂R_i×R_j), so exactly 2 are P-rows: exactly 2 P words are active at both i and j. ✓

**Absent-pair edge case.** An active/active pair absent from π_ij(E) is necessarily a P-row (it cannot be absent from both P and E: all 36 rows of a 36×36 unitary are nonempty, and P-rows and E-rows partition them by §2(f)). Pairs (a,b) with a∈R_i, b∉R_j are automatically P-rows; there are 9 of them per ordered (i,j), and 9+2=11 ✓. No other category exists.

**Orientation edge case.** The per-party count may be read off from the cut in which (i,j) indexes rows or from the complementary cut in which it indexes columns; both give the same P/E partition of the same 36 pairs. Ordered vs unordered pairs: per-party counts use ordered (i,j) and are j-independent; per-pair counts are symmetric in i,j. ✓

**Identity.** Σ_x k(x)=4·11=44; Σ_x C(k(x),2)=6·2=12 (a word with k active coordinates is counted in C(k,2) pairs). k−C(k,2)=0,1,1,0,−2 for k=0..4, maximum 1, so Σ_x[k−C(k,2)]≤|P|=29, but it equals 32. Contradiction. ✓ Equivalent sharper form: with m_k words of activity k, the three linear conditions force m_0+m_3+3m_4=29−32=−3<0; Control A enumerates and finds **no** nonnegative integer solution.

**Universality of the packet's inequality (1).** Σ_i(6r_i−n)−Σ_{i<j}(r_ir_j−n)≤36−n holds whenever: all six |π_ij(E)|=n, every P word is pair-injective (true, §2(a)), and the P/E partition of §2(f) holds. The packet states only the first hypothesis explicitly; see MINOR-2. Control A: over all size-nondecreasing r∈{1..4}⁴ with every r_ir_j≥7, the inequality rejects exactly r=(3,3,3,3) (lhs 32); (3,3,3,4) gives 29 (tight, not rejected); the packet's "nearby n=6, (3,3,3,3)" value is 30 = bound, not rejected — consistent with the packet's own statement.

**Control C (mine).** Enumerating residual supports E⊂{0,1,2}⁴ with |E|=16 whose (01|23) flattening has the shape of §4 (198,450 labelled patterns per choice of the two missing row pairs and two missing column pairs, the latter taken up to S₃×S₃ as same-row / same-column / diagonal): **40 distinct E** satisfy all six projections having exactly 7 values with 2–3 extensions each (all in the diagonal|diagonal slice). For every one of them, all four residual alphabets have size 3, the recomputed P-row counts are 11 for all 12 ordered party pairs and 2 for all 6 unordered pairs (0 failures), and an exact-cover depth-first search for 29 pairwise pair-distinct words covering all 29 non-E pair values per projection returns **infeasible** (complete search, 3,304 nodes, 513 candidate words, for each of three distinct E). A positive control of the identical DFS on complements of three random 29-word partial orthogonal arrays **found** verified covers (1,073–7,704 nodes), so the infeasible verdicts are not an artefact. This shows the n=7 residual geometry is combinatorially realisable at the E level and that the contradiction is produced exactly at the P-completion stage, as the packet's argument asserts; it is a bounded check on specific E, not the universal proof.

## 7. Findings

No FATAL and no MAJOR defect found in the ≥46-specific reasoning (§2 case split, §3 residual alphabets, §4 counting of the candidate).

- **MINOR-1 (dependency weight, not an error).** The packet derives "max residual degree ≤3" from the sharp 2n+2 classification. For n≥5 (hence n=7) the bound follows from the combinatorial no-unique-overlap rule plus column degree ≥2 alone (§4(b)); the full classification, the C² span step and the 2×2 norm step are not needed for ≥46. Stating this would shrink the ≥46 dependency surface to: ≥45 chain, 2n, 2n+1, 2n+3 lemmas.
- **MINOR-2 (statement hygiene).** The reusable inequality (1) is stated under the hypothesis "all pair projections have size n" only; it also needs pair-injectivity of P and the P/E partition of every 36-pair system (both true in the residual framework) and is specific to four parties (k≤4). As written it could be misapplied outside this framework.
- **MINOR-3 (presentation).** In §3 of the packet the step "If j were constant in an A-fiber, that single pair would have all four fiber entries as extensions" silently uses that the four fiber entries all share x_A=v and x_j=w, i.e. lie in one residual row; correct, but worth one clause. The alternative sum-of-fiber-values route (each fiber's j-value count ∈{1,2}, total 7 forces exactly one constant fiber per j) does not by itself contradict and the degree bound is required — the packet chose the right tool.
- **Clock note.** The packet's native clock `19:10:09 PDT` is consistent with the earlier dependencies' clocks (18:47:22, 18:49:24, 18:57:25, 19:04:26, 19:09:02) and with the manifest's `19:12:50`. No timestamp inconsistency observed. Receipts carry no clocks.
- **My own artefact errata.** `active-count-controls-v1.py/json` double-counted column-pair splits in control C (each pattern and each surviving E generated twice; "80" survivors = 40 distinct; DFS samples 2 and 3 identical); conclusions unaffected. Fixed in v2, which is the version cited above. `active-count-dfs-positive-control-v1.py` had a bracket typo and never ran; v2 is the version cited. Nothing was deleted.

## 8. Verdict

**Slice verdict: NO FATAL / NO MAJOR; MINOR only. The t=29 (n=7, |E|=16) exclusion is correct as written, given its stated inputs, and I have re-derived every step it uses.**

**Verdict on the ≥46 candidate as a whole — CONDITIONALLY CORRECT**, i.e. "every normalized complex AME(4,6) state in every product basis has support ≥46" holds **if and only if the following prerequisites hold**, none of which is adopted by this review:

1. The ≥45 candidate (exclusion of N≤44), itself resting on the ≥44 and ≥42 candidates — **separately under review, not re-proved here.**
2. From the ≥42 packet, t≤30 (the n=4 AME(4,2) Pauli argument and the n=5 XOR argument) — **not re-proved here**; needed for the N=45 case split to be exhaustive (otherwise t∈{31,32} would need separate treatment).
3. The classical no-OLS(6) theorem — **explicit external import**, entering through items 1–2, not through the n=7 argument.
4. The 2n+3 lemma for even n (t=30 case) — **primary responsibility of the `unitary-excess` slice**; my secondary step-by-step re-derivation (§3.3) found no gap but is not an independent route.

Independently re-derived in this review and **not** left conditional: the residual-unitary setup and pair partition; the incidence lemma; the 2n and 2n+1 lemmas (cases t=27, t=28); the "no degree-4 line" bound for 2n+2 (two proofs, plus exhaustive n=7 pattern control); the n=7 fiber argument forcing all four residual alphabets to size 3; the counting identity 44−12=32>29 (hand derivation, multiplicity infeasibility, per-party j-independence, absent-pair and orientation edge cases, bounded exact-cover controls).

Not claimed: any exact global minimum (the gap 46…60 to the published 60-term witness remains open as far as this review goes), any 46-term witness, novelty or priority over [Pandya arXiv:2610.16673v1 §VI]'s reported 38, formal/kernel verification, human or independent-family review. If prerequisites 1–4 are later rejected, this slice verdict does not rescue ≥46; if they are accepted at their own review gates, this slice supplies the remaining t=29 step and verifies the t=27/t=28 steps.

## 9. Reviewer artefacts (all in this review directory, `active-` prefix; SHA-256 observed at 19:26:06 PDT)

- `active-count-controls-v1.py` `847aea7505d8d5785a041da2cd9906ce4bc26dc2d23c38c280369528b2278468` (12,824 B; superseded, double count in control C)
- `active-count-controls-v1.json` `bff89fce94532ecbc76903eba0521bf45fe2e9611ac5ec330adbc02447f249a9` (6,726 B; run 19:22:00–19:22:35 PDT)
- `active-count-controls-v2.py` `41502b301d5135635a759231b9e41f0fe463427ba0938e05d46f89c2eeef8c2f` (13,190 B; cited version)
- `active-count-controls-v2.json` `ec7c8c0c38459f438dc782778f9f40d19c39226694c08c2f6fddb1e3fea23d0f` (6,756 B; run 19:23:22–19:23:47 PDT; A: 32>29, no multiplicity solution, only (3,3,3,3) rejected; B: 315 survivors, max degree 3, single shape; C: 40 distinct E, 0 count failures, 3/3 DFS infeasible)
- `active-count-dfs-positive-control-v1.py` `1cad76466ea0a54d736155b0a0b614b8e3aa781fa180a1f0f78f67d863255008` (4,209 B; syntax error, never ran)
- `active-count-dfs-positive-control-v2.py` `7c663ce85e632eb51944b2ff6a581c9502f0e319df9feb1e3505905d89bed76d` (4,258 B)
- `active-count-dfs-positive-control-v2.json` `7f6317b75d46b1c915934b25dc6c8efdbbbb0aa36f4dbb4ae607862157c4e383` (623 B; run 19:24:41–19:24:51 PDT; 3/3 covers found and verified)
- This file `active-count-review-v1.md` (hash to be recorded by the parent after creation).

Reproduce: `python3 -B active-count-controls-v2.py <new.json>` (~26 s) and `python3 -B active-count-dfs-positive-control-v2.py <new.json>` (~10 s); both refuse to overwrite an existing output path. Python 3.14.3 was used.
