# Partial row-orbit symmetry in T2(11): written lemma, complete case split, one DRAT-verified exclusion

Native `/bin/date` observed before writing: **Wed Oct 28 20:17:25 PDT 2026**. Owner InfoRecursiveMDS18-2, info-4. **WRITTEN all-variable lemma**, a mechanical case enumeration, one **DRAT-verified** UNSAT certificate, and separately labelled bounded SAT outcomes. This does not decide T2(11): it restricts where a symmetric witness could be. Unverified UNSAT and UNKNOWN are not exclusions. No novelty claim; not independently reviewed.

Motivation. A T1(11) array has no nontrivial symbol automorphism (`frontier-20261028-odd-prime-symbol-asymmetry-v1.md`, `afb26402…bf3f`) and is not isomorphic to its reversal (`frontier-20261028-odd-order-reversal-asymmetry-v1.md`, `f1f65fd9…2575`). So the only orbit-type structure a T2(11) witness can carry is *partial*: some rows form orbits of a symbol permutation, the rest are free.

## 1. Setting

A is a T1(n) array: n permutation rows of n symbols, each ordered pair of distinct symbols adjacent exactly once (linear rows); T2 adds: each ordered pair at distance 2 at most once. Each symbol starts exactly one row and ends exactly one row (its n−1 out-arcs need it to be non-last in exactly n−1 rows). Let g ≠ id be a symbol permutation of order k, ℓ_a the length of the g-cycle of a, K the symbols on cycles of length exactly k, c_k the number of such cycles, F the other symbols. Suppose A contains b ≥ 1 disjoint **blocks** {R, gR, …, g^{k−1}R} (gR is the position-wise image; these k rows are distinct since g^iR = R forces g^i = id), and f = n − bk ≥ 1 further **free** rows.

## 2. Lemma (WRITTEN)

1. **Endpoints.** If ℓ_a < k, then a is neither first nor last in a block row: if a starts g^iR, then g^{i+ℓ_a}R ≠ g^iR also starts with g^{ℓ_a}a = a. Hence every block row starts with a K-symbol, the k rows of a block start with all symbols of one k-cycle, different blocks use different k-cycles, and **b ≤ c_k** (no block exists when no cycle has length k).
2. **Orbit arcs.** If (x, y) occurs at distance 1 in a block row, then lcm(ℓ_x, ℓ_y) = k: with m = lcm(ℓ_x, ℓ_y) < k the pair would occur at the same positions of the distinct rows g^iR and g^{i+m}R. For **T2** arrays the same holds at distance 2, because distance-2 pairs occur at most once.
3. **One free row is impossible.** If f = 1, the block arcs form a g-invariant set, so the free row's arc set (the complement) is g-invariant. A Hamiltonian path is determined by its arc set, so g fixes the free row position-wise, i.e. g = id.
4. **Strict cycle count.** If F ≠ ∅ and lcm(ℓ_a, ℓ_{a'}) < k for all a, a' ∈ F, then **b ≤ c_k − 1.** For a ∈ F, each block row contains an arc (x, a) (part 1). By part 2, lcm(ℓ_x, ℓ_a) = k, so x ∉ F by the hypothesis, i.e. x ∈ K. These bk arcs are distinct, so bk ≤ |K| = k·c_k. If b = c_k, all arcs between a and K (both directions) lie in block rows for every a ∈ F, so no free row contains an F–K adjacency; but a free row visits both F and K. Contradiction.
5. **Placement (T2).** In a block row, F-symbols occupy positions 1..n−2 (part 1), and two symbols with lcm < k are at distance ≥ 3 (part 2 at distances 1 and 2). For n = 11 at most 3 pairwise such symbols fit into positions 1..9.

## 3. Complete case split for n = 11

`frontier-20261028-row-orbit-classification-v1.py` (SHA-256 `127e0df66cd6d50a2e76af72f2255f2894b7413fb98ce10a4e6be22a526b5888`) enumerates every cycle type of g with 2 ≤ k ≤ 10 and every b ≥ 1 with f ≥ 1 and applies parts 1, 3, 4, 5 in that order (output `…classification-v1.json`, `0b703e5e6ad44dbfd855463696108c262ed5e724843707e5a595788101b756f5`). Of the **70** (type, b) cases, part 1 excludes 28, part 3 excludes 3, part 4 excludes 22 and part 5 excludes 4. An independent hand enumeration gave the same list. **Thirteen cases remain:**

(6,3,2) b=1; (5,5,1) b=1; (4,4,2,1) b=1; (4,4,1³) b=1; (3³,1²) b∈{1,2}; (2⁵,1) b∈{1,2,3,4}; (2⁴,1³) b∈{1,2,3}.

(6,3,2) is the only remaining type whose short-cycle symbols include a pair with lcm = k.

## 4. DRAT-verified exclusion of (6,3,2), b = 1

The v1 encoder `frontier-20261028-partial-symmetry-sat-v1.py` (`e93b0c63b00c4e22019ed8afe7b0a720a1da308aeef3a09faa3649448fe29ef5`) encodes exactly this structure for T2(11): X/S/T channelling, D1 exactly once, D2 at most once, unique starts and ends, canonical g on consecutive symbols, and rows jk+i = g^i(row jk). Its CNF `frontier-20261028-partial-sym-6-3-2-b1.cnf` (`6bbd7e0295d7ffea5cdac698b04a88fd6981005f7e8228f6b4ed3f44d7285eb0`, header 13,673 variables / 92,576 clauses) is **UNSAT, DRAT-VERIFIED**:

- runner `frontier-20261028-fifo-drat-check-v2.py` (`f74c320ddfe6ede4418d4bd6ebb2d517b7999944b4f3643cbe813053aca364a7`) streamed Kissat's binary proof through an owned FIFO into drat-trim's stdin (`-i`);
- 208,863,195 proof bytes read; Kissat rc 20 `s UNSATISFIABLE` in 66.1 s; drat-trim rc 0 `s VERIFIED`; parsed counts equal the header;
- CNF, Kissat (`05d6f3e9…a848`) and drat-trim (`e6799e1d…fc35`) hashes unchanged;
- receipt `frontier-20261028-partial-sym-6-3-2-b1-drat.json` (`ad806d276e2792959092e351089c6e05d419eafcc530b2eaa8d26053de048bc8`).

Controls: PHP(6,5) UNSAT verified with 1,520 proof bytes (`…control-php65-drat-v2.json`, `10679579…b118`); PHP(5,5) SAT not verified (`…control-php55-drat-v2.json`, `27c530f5…1ed3`); a PHP(6,5) proof checked against the PHP(5,5) formula is rejected (`…control-wrongcnf-drat.txt`, `e9579260…8fdc`).

The mathematical conclusion "no T2(11) contains a (6,3,2) row orbit" also depends on the encoder being correct. I checked it line by line, but it has not been independently reviewed.

**Tooling erratum.** Runner v1 (`…fifo-drat-check-v1.py`, `e960d50c…fc96`) failed its UNSAT control (`…control-php65-drat.json`, `3cdab514…6b80`). drat-trim closes and reopens a named proof file (drat-trim.c lines 1457–1459), so a FIFO path loses the stream. Runner v1 produced no scientific verdict.

## 5. Bounded SAT outcomes (unverified; v1 encoder, no symmetry breaking)

The cases that the lemma excludes were also observed UNSAT by Kissat as consistency checks. Reported elapsed times:

| Type | b | elapsed |
|---|---|---|
| (9,1,1) | 1 | 212 ms |
| (3³,1²) | 3 | 202 ms |
| (8,2,1) | 1 | 191 ms |
| (4,4,1³) | 2 | 379 ms |
| (4,4,2,1) | 2 | 217 ms |
| (2⁴,1³) | 4 | 212 ms |
| (4,2³,1) | 2 | 166 ms |
| (7,1⁴) | 1 | 169 ms |
| (6,2,2,1) | 1 | 155 ms |
| (3,2⁴) | 1 | 16 ms |
| (3,3,2,2,1) | 1 | 15 ms |

Four cases were UNKNOWN at 240 s: (2⁵,1) b=4 (`…partial-sym-2-2-2-2-2-1-b4.json`, `e30b4a23…02d4`), (2⁵,1) b=3 (`…-b3.json`, `30768991…5f5c`), (3³,1²) b=2 (`…partial-sym-3-3-3-1-1-b2.json`, `4b49cc8d…a182`) and (5,5,1) b=1 (`…partial-sym-5-5-1-b1.json`, `35620110…17c7`).

The v2 encoder `frontier-20261028-partial-symmetry-sat-v2.py` (`570dde55dd27a58a5022bccb7d87795eb8c98be69b3a8151444bd1c6b318ea9c`) adds only constraints justified by part 1, part 2 and the centraliser of g:

- block j uses the j-th k-cycle, and its base row starts with that cycle's least symbol;
- the free rows start with the remaining symbols in increasing order;
- short-cycle symbols are never endpoints of block rows;
- no D1 or D2 pair with lcm < k occurs in a block row.

Bounded v2 runs on the 12 open cases are in progress. A SAT model in any case would be an actual T2(11) square, and it would be independently rechecked before any claim.

## 6. Other target-side observation

A 3,400 s simulated-annealing run on unrestricted 11-row arrays (`frontier-20261028-anneal-n11-run-01.json`, `75ed7a7bfc9228fbd617e4b794ad3351cf6cda8cc17fa514666adba5858a70bf`) ended with D1 excess 5 (105 of 110 events distinct) and D2 excess 2 (97 of 99 events distinct). I independently recounted this from the rows. For comparison, the best exact-T1 repair walk has D1 excess 0 and D2 excess 8. Neither is a witness.

## Limits

These results apply only to T2(11) arrays that contain a block in the sense of §1. Arrays with no partial row-orbit symmetry are untouched. The original existence/no-go question remains **OPEN**.
