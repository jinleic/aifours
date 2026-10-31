# f124 — NEW disjoint review of the standalone ordered-four field-sequence theorem

Review id `f124-olson-standalone-ordered-four-new-scope`, file `review-v1.md`. Native `/bin/date` observed immediately before this write: **Wed Oct 28 20:20:36 PDT 2026**. Reviewer: the f124 in-harness reviewer session (Claude Code harness). Authority: manifest `manifest-v1.json`, SHA256 `81efb7408a2e72633c62211e643be44a764dbc199f001b928c17895cf0264a64` (2856 bytes, 39 LF, verified before reading).

## 0. Scope, read order, non-transfer

**Scope reviewed (exactly the manifest scope):** for every odd prime p, every length-(p+2) sequence over F_p whose consecutive entries are distinct contains indices i<j<k<l with z_i − z_j + z_k − z_l = 0. Nothing else. No actual-block, odd-run, reflection, raw-graph, floor, L_RES, lift or Olson application is reviewed, reconstructed or asserted here.

**Inputs, read in the declared order, each verified (SHA256 / bytes / LF) before reading; all four match the manifest exactly:**

| # | role | file | sha256 | bytes | LF |
|---|------|------|--------|-------|----|
| 1 | mandatory fatal correction / non-transfer | `frontier-20261028-olson-actual-block-fatal-correction-v1.json` | `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e` | 9278 | 92 |
| 2 | standalone candidate | `frontier-20261028-olson-ordered-four-standalone-v1.md` | `18dbdfaf149d7ae31563d4cb87a78f61d455fd51db57a12d5bcc95be790261a5` | 4980 | 53 |
| 3 | author checker (read as text only) | `frontier-20261028-olson-ordered-four-standalone-checker-v1.py` | `d85a76b3f6630b3c220a5347d7dd3fda0257ad6cfcc0211354a35b7782a1eeb4` | 3307 | 94 |
| 4 | author receipt | `frontier-20261028-olson-ordered-four-standalone-check-results-v1.json` | `59a9d32b3a4e004a3f00d29bcc9cad6b68dbb11371d822e1f4efcc1007ff5ce1` | 510 | 24 |

All in `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/`.

**Non-transfer, honoured:** the fatal correction (input 1) was read first. Nothing from the held f111 disposition is used as a premise. I did **not** open `frontier-20261028-olson-ordered-four-odd-boundary-v1.md`, any other file in the correction's affected-candidate inventory, any earlier review, or any earlier control output. The author checker was read as text and was neither imported nor executed; every number in §4 below comes from my own program. No author contact, web search, external model, paid API, Git, deletion, publication or infrastructure action was performed; no repository build/lint/format/test suite was run.

**Prior-exposure disclosure:** before this assignment I had no exposure to the ordered-four lemma, its earlier candidate text, its earlier review or its earlier controls. Inherited context consisted of the manifest, the four inputs above, and a harness memory summary that mentions the `three-area-2026-10-27-96h` run but contains nothing about this lemma. I learned that "the same mathematical statement appeared in the earlier source" solely from the candidate's own §0 sentence. Hence: no blind-review claim, but also no known exposure to held material.

## 1. Statement under review

Let p be an odd prime, N = p+2, and z_1,…,z_N ∈ F_p with z_i ≠ z_{i+1} for 1 ≤ i < N. Call (i,j,k,l) with i<j<k<l and z_i − z_j + z_k − z_l = 0 a *zero quadruple*. Claim: a zero quadruple exists. No full-support or pairwise-distinct hypothesis. (Candidate §1.)

## 2. Independent reconstruction of the proof

Throughout, assume for contradiction that the sequence is zero-quadruple-free ("Q-free"). All arithmetic is in F_p.

### 2.1 Full support forces an arithmetic progression (candidate §2)

Suppose additionally every element of F_p occurs. Fix i ∈ {1,…,p} and set t := z_i − z_{i+1} + z_{i+2}. By full support some position m has z_m = t. Exhaust the position of m:

* m < i: (m, i, i+1, i+2) has sum t − z_i + z_{i+1} − z_{i+2} = t − t = 0 — zero quadruple, excluded.
* m > i+2: (i, i+1, i+2, m) has sum z_i − z_{i+1} + z_{i+2} − t = 0 — excluded.
* m = i: z_i = t gives z_{i+1} = z_{i+2}, contradicting adjacency.
* m = i+2: z_{i+2} = t gives z_i = z_{i+1}, contradicting adjacency.
* Hence m = i+1 and 2z_{i+1} = z_i + z_{i+2}, i.e. z_{i+2} − z_{i+1} = z_{i+1} − z_i.

As i ranges over 1,…,p every consecutive difference equals d := z_2 − z_1 ≠ 0, so z_n = z_1 + (n−1)d. Then (1,2,3,p+2) has sum z_1 − (z_1+d) + (z_1+2d) − (z_1+(p+1)d) = −pd = 0, and 1<2<3<p+2 since p ≥ 3. Contradiction. **Checked, correct.** (Only one occurrence of t is needed; the candidate's "all its occurrences" is harmless.)

### 2.2 Multiplicities (candidate §3)

(a) A value occurring ≥ 4 times gives (a,a,a,a) with sum 0. (b) If a occurs ≥ 3 times and b ≠ a occurs ≥ 2 times, take b_1<b_2 and three occurrences of a. The three regions "before b_1 / between / after b_2" receive three a's: either two share a region — orders a,a,b,b or b,a,a,b or b,b,a,a, each summing to 0 — or one lies in each region, order a,b,a,b,a, and (a_first, b_1, b_2, a_last) sums to a−b+b−a = 0. Either way excluded. (c) So if some value occurs 3 times, it occurs exactly 3 times and every other value once; the number of distinct values is N−2 = p, i.e. full support, contradicting 2.1. (d) Hence every multiplicity is ≤ 2. With s doubled values the support has size p+2−s ≤ p, so s ≥ 2. (e) For doubled a ≠ b the occurrence intervals cannot be disjoint (a,a,b,b) or nested (a,b,b,a or b,a,a,b), all summing to 0; so they cross: a_1<b_1<a_2<b_2 or b_1<a_1<b_2<a_2. **Checked, correct.**

### 2.3 The absent value x = 2a − b (candidate §4)

Fix doubled a ≠ b and put x := 2a − b. x = a ⇔ a = b; x = b ⇔ 2(a−b) = 0 ⇔ a = b because 2 is invertible for odd p. So x ∉ {a,b}, and any position m with z_m = x is distinct from a_1,a_2,b_1,b_2. I verified all six cases, including index order:

| order | position of m | quadruple | sum |
|---|---|---|---|
| a_1<b_1<a_2<b_2 | m < a_1 | (m, a_1, b_1, a_2) | x − a + b − a = (2a−b) − 2a + b = 0 |
| a_1<b_1<a_2<b_2 | a_1 < m < a_2 | (a_1, m, a_2, b_2) | a − x + a − b = 2a − (2a−b) − b = 0 |
| a_1<b_1<a_2<b_2 | m > a_2 | (a_1, b_1, a_2, m) | a − b + a − x = 0 |
| b_1<a_1<b_2<a_2 | m < a_1 | (m, a_1, b_2, a_2) | x − a + b − a = 0 |
| b_1<a_1<b_2<a_2 | a_1 < m < a_2 | (b_1, a_1, m, a_2) | b − a + x − a = 0 |
| b_1<a_1<b_2<a_2 | m > a_2 | (a_1, b_2, a_2, m) | a − b + a − x = 0 |

In the middle cases the position of m relative to the b that is skipped (b_1 in the first order, b_2 in the second) is irrelevant because that b is not used; the quadruple's third/fourth entries are increasing by the assumed crossing order. The regions m<a_1, a_1<m<a_2, m>a_2 exhaust m ≠ a_1,a_2. Hence x is absent. **Checked, correct.**

### 2.4 Counting (candidate §4, end)

For fixed a the map b ↦ 2a−b is injective, so the s−1 other doubled values give s−1 distinct absent elements. But the support has size p+2−s, so exactly p−(p+2−s) = s−2 elements are absent. s−1 > s−2 is the contradiction; the theorem follows. **Checked, correct.** (When s = 2 this already contradicts without 2.1; 2.1 is needed only for the tripled case in 2.2(c).)

### 2.5 Hypothesis audit (where each hypothesis is actually used)

* **Adjacent-distinct:** used only in 2.1 (excluding m = i and m = i+2). Load-bearing for the *statement*: without it, Q-free sequences of length p+2 exist — [0,0,0,1,2] over F_3 is one (§4 G).
* **Length p+2:** used in 2.1's final quadruple and in the counts of 2.2(c),(d) and 2.4. Sharp: Q-free adjacent-distinct sequences of length p+1 exist for every tested p, e.g. 0,1,…,p−1,0 (§4 C).
* **p odd:** used only for x ≠ b in 2.3. At p = 2, x = b for both ordered pairs (§4 E).
* **p prime:** not used beyond oddness. The written argument, read literally, proves the same statement over Z/n for every odd n ≥ 3; this is consistent with the Z/9, Z/15, Z/21 exhaustive probes (§4 H). Recorded as an observation about the proof's dependencies only, not as an adopted result.
* Full support / pairwise distinctness are correctly *not* assumed.

**Conclusion of §2:** the written argument is complete and correct for every odd prime p at the level of a rigorous elementary combinatorial proof. I found no gap, no unproved sub-claim and no miscount.

## 3. Author checker and receipt (read as text; not run)

* `find(values,p)`: for k = 2,…,L−2 the dictionary accumulates differences z_i − z_j over all pairs i<j<k (pairs (i,k−1) are inserted at step k), and for each l > k tests whether z_l − z_k is among them; a hit gives z_i − z_j + z_k − z_l = 0 with i<j<k<l. Every zero quadruple (i,j,k,l) is reachable at its own k, so the search is complete; the index/sum self-check before `return` is sound. Error order BAD_LENGTH → VALUE_RANGE → ADJACENT_EQUAL matches the three control inputs and their expected labels.
* `exact(p)`: z_1 = 0 with steps in 1..p−1, i.e. (p−1)^{p+1} sequences: 2^4 = 16 (p=3), 4^6 = 4096 (p=5). Translation normalization is valid (z ↦ z+c preserves adjacency and alternating sums). Matches receipt and candidate §5.
* `crossing(p)`: 10·p·(p−1) cases: 60/200/420 at p = 3/5/7. Matches receipt. Minor: it tests that *some* 4-subset of the five positions sums to zero, not the specific quadruple the text names; §4 E below tests the exact named quadruple.
* Sampling: 2000 per p ∈ {7,11,13}, seed 2026102823; receipt keys and values are the ones the code emits.
* I did not execute the author's code, so I do not independently confirm the author's run; my own run below is the evidence used for this verdict. No defect found in the author checker text.

## 4. Independent control: `reviewer-control-v1.py` — one receipted run

Written by me without importing or executing the author checker. Files, both in this directory:

* `reviewer-control-v1.py` — SHA256 `deb561307835e782a6230d05fc790b7d27d5396574ed3563180dfb4c70d929b3`, 22947 bytes, 504 LF.
* `reviewer-control-results-v1.json` — SHA256 `a092d8c2761c4683d16369d7efc9925ddd7aa91820115f40d25bc76529a75859`, 23930 bytes, 1131 LF; created with exclusive `open(...,'x')`.

Receipted run: `/bin/date` before launch `Wed Oct 28 20:13:52 PDT 2026`; receipt `bin_date_at_start` `Wed Oct 28 20:13:52 PDT 2026`, `bin_date_at_end` `Wed Oct 28 20:19:56 PDT 2026`; shell `/bin/date` after exit `Wed Oct 28 20:19:56 PDT 2026`; exit 0; `elapsed_s` 363.59; Python 3.14.3, macOS-27.0.1-arm64. Seed 12420261028 (mine, not the author's). Argv recorded in the receipt: `--primes 3,5,7,11,13,17 --affine-primes 7,11,13,17 --odd-composites 9,15,21 --evens 4,6,8,10 --no-adjacency-primes 3,5,7 --sample-primes 17,19,23,29,31 --samples 3000 --detector-trials 20000`. The receipt binds the manifest, the four inputs and the script itself by sha256/bytes/LF (all equal to the values in §0 and above). Disclosure: two earlier *gauge* runs of the same script with smaller/other parameter sets and no `--output` were made to size the DFS (0.2 s and 358 s wall); they wrote no files and are not the evidence.

**Result: `PASS_F124_REVIEWER_STANDALONE_ORDERED_FOUR_FINITE_CONTROL`; all 12 required checks true.**

| sect. | what was run | outcome |
|---|---|---|
| A | 20 000 random sequences (n ∈ {3,5,7,11,13}, random lengths 4..n+2, adjacency *not* enforced): O(L⁴) brute force vs my independent O(L²) prefix-difference bitmask detector | 20 000/20 000 agree; a deliberately wrong oracle disagreed with brute force 3 809 times, so the comparison discriminates |
| B | unnormalized full enumeration of every adjacent-distinct sequence of every length 1..p+2, p = 3, 5 | Q-free counts at length p+2: 0/48 (p=3), 0/20 480 (p=5); per-length counts equal p × the DFS counts in C |
| C | exhaustive pruned DFS over Q-free adjacent-distinct sequences with z_1 = 0, p ∈ {3,5,7,11,13,17}, to length p+2 (pruning is lossless because prefixes of Q-free sequences are Q-free) | Q-free sequences of length p+2: **0 for every p**. DFS nodes 11 / 121 / 1 057 / 44 821 / 242 713 / 5 603 169. Every node checked against the §2–§4 internal claims M4, M3, CROSS, ABSENT, AP: **0 violations**. Max Q-free length is p+1 for every p (exactly p−1 sequences, first example 0,1,…,p−1,0), so p+2 is sharp. Full-support Q-free sequences occur only at lengths p and p+1 and are all arithmetic progressions |
| D | same DFS with affine normalization z_1=0, z_2=1, p ∈ {7,11,13,17} | 0 Q-free at length p+2; 0 violations; counts equal C's counts divided by p−1 at every length ≥ 2 |
| E | §4 positional check: odd primes ≤ 31, all a≠b, both crossing orders, all five insertion slots of x=2a−b, the exact quadruple named in the text | 31 960 cases, 0 failures: every named quadruple is strictly increasing with sum 0; inserted 5-sequences adjacent-distinct; x ∉ {a,b}; b ↦ 2a−b injective. p = 2 boundary: x = b for both pairs (oddness is load-bearing) |
| F | §2 final step: every nonconstant AP 0,d,…,(p+1)d, 25 odd primes ≤ 101 | 1 134 progressions; (1,2,3,p+2) sums to −pd = 0 in all; brute force finds a zero quadruple in all |
| G | adjacency hypothesis dropped, p = 3,5,7, DFS to length p+2 | Q-free length-(p+2) sequences exist: 10 / 28 / 54 (z_1=0), e.g. [0,0,0,1,2]; only the AP claim is violated there (16/48/96), M4/M3/CROSS/ABSENT still hold — exactly where the proof uses adjacency |
| H | modulus probes, adjacency kept: Z/9, Z/15, Z/21 (odd composite) and Z/4, Z/6, Z/8, Z/10 (even), DFS to length n+2 | odd composite: 0 Q-free at n+2 (nodes 7 055 / 1 106 179 / 92 547 047), 0 internal-claim violations, max length n+1 — consistent with the proof using only oddness; even: also 0 at n+2 (observational only; the written proof does not cover even n) |
| I | 3 000 random adjacent-distinct sequences of length p+2 for p ∈ {17,19,23,29,31} | 3 000/3 000 contain a zero quadruple at every p; 0 of their length-(p+1) prefixes were Q-free |

The finite control is a consistency check with exhaustive coverage of p ≤ 17 (far beyond the author's exhaustive p ≤ 5); it is not the all-prime proof. The all-prime claim rests on §2 of this review.

## 5. Findings

* **Fatal: 0. Major: 0.**
* Minor / presentational (no effect on correctness):
  * m1. Candidate §5 says "normalized" without saying how; the checker normalizes z_1 = 0 (valid by translation invariance). Suggest stating it.
  * m2. The author's `crossing` control verifies a weaker property than §4 states (some zero 4-subset, not the named quadruple). Covered by my §4 E; suggest the author's text say "some" or check the named quadruple.
  * m3. §2 says "all its occurrences lie inside the triple"; one occurrence suffices. Harmless.
  * m4. Observation: primality is used only through oddness; the argument as written proves the Z/n statement for odd n. No change required for the stated theorem.

## 6. Verdict (this new standalone scope only)

**PASS.** The standalone theorem — for every odd prime p, every length-(p+2) adjacent-distinct F_p sequence has i<j<k<l with z_i − z_j + z_k − z_l = 0 — is correctly stated and the written proof in `frontier-20261028-olson-ordered-four-standalone-v1.md` (SHA256 `18dbdfaf…261a5`) is complete and correct as an elementary combinatorial argument; the reviewer's independent finite control passes with exhaustive coverage p ∈ {3,5,7,11,13,17} and all internal-claim, boundary and mutation checks. Dependencies of this verdict: the four frozen inputs listed in §0, this reviewer's reconstruction in §2, and the single receipted run in §4; nothing else.

## 7. Non-claims

Not a human review; not an independent model-family review (same harness family as the author lane; the reviewer is an in-harness session); not a formal/kernel proof; no novelty, priority or literature claim; no original Olson target, actual-block, reflection lift, odd-run, raw-graph, floor, L_RES or p7/p11 profile claim of any kind; no transfer of this verdict to, or salvage of, the held f111 disposition or any file in the correction's affected inventory. Any application of this standalone theorem to actual-block structure requires its own separately stated source correspondence and its own review.

**END — review-v1.md, f124 standalone scope only.**
