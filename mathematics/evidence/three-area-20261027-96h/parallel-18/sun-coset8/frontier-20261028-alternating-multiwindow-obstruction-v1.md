# A saturated t=41 multiwindow arithmetic obstruction

**Status: WRITTEN arithmetic-relaxation candidate, with one exact finite control; not a P7 counterexample, subgroup construction, independent verification or novelty claim.** There are infinitely many eligible primes r above any prescribed bound for which one can write seven positive integers satisfying all of the following simultaneously:

- pairwise gcd exactly 7, each dividing |A_(r+41)| and at least r+41;
- exactly one is divisible by r, the other six are r-free;
- each r-free integer is an exact product of disjoint binomial windows with formal quotient factors c=1, consumes exactly one of the six seven-cells, and has a final lower window of length at least 2;
- whenever a displayed two-window chain descends, at least one position is left between its windows, consistent with—but not proving—the required transitive projected-subgroup step.

These are **necessary arithmetic features only**. The construction does not produce the actual transitive projections, subgroups or disjoint cosets. In particular the original t=41 direct-P7 problem remains open for this route. This packet strengthens the earlier 7-local model, which did not control non-7 gcds, and shows that the exact index factorization, seven-cell packing, whole group-order divisibility and elementary minimum-index bound alone cannot certify closure.

## 1. Nonblind/source boundary

The actual subgroup quotient c|u!, seven-cell necessity and saturation are the unreviewed written arguments in `frontier-20261028-alternating-seven-cell-p7-v1.md` SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f` and `frontier-20261028-alternating-saturated-seven-frontier-v1.md` SHA `82cb25f5f1ab52d928f3fc3ee6fba73ac2147b7aa0c00833aee1b1618dc91fee`. The relevant A_r source is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2. These sources remain unreviewed; this packet does not adopt them or use Sun7.

**Mandatory pre-source arithmetic correction:** before either listed source or this successor, read `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`. Its corrected shared-cell estimate is (r+h)/gcd(r+h,t!) ≥ (r+1)/t! > 7. No frozen source is edited. The writer was nonblind; the incidental cross-topic display is recorded at `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such content is used and no historical hold is changed.

## 2. A finite exact template

For r=431, set N0=7r and define the six r-free integers by these ordered window products, where an interval [a,b] contributes C(r+b,b−a+1):

| label | ordered windows | N_i |
|---|---|---:|
| 1 | [2,3] | 93961 |
| 2 | [10,10], [7,8] | 42398181 |
| 3 | [12,17] | 10857619219552 |
| 4 | [21,24] | 1762351955 |
| 5 | [30,32] | 16435111 |
| 6 | [38,38], [35,36] | 51032359 |

All displayed quotient factors are 1. The windows are pairwise disjoint, each r-free label consumes exactly one of the six seven-cells 3,10,17,24,31,38, and the final window of every chain has length at least 2. In the two-window chains, endpoints 10→8 and 38→36 leave a full transitive-descending gap. Direct integer arithmetic gives gcd(N_i,N_j)=7 for every pair including N0=3017, r∤N_i for i≥1, and every N_i divides 472!/2 and is at least 472. The source's much larger size bound r+1>7·41! is **not** met by this selected example.

## 3. Infinitely many large arithmetic templates

Let
\[M=8\cdot9\cdot25\cdot49\cdot11\cdot13\cdot17\cdot19\cdot23\cdot29\cdot31
 =84235405854600.\]
For any prime r≡431 mod M, use the same six window products and N0=7r. All numerator offsets are distinct and lie between 2 and 38, so a non-7 prime common to products from two labels must divide a nonzero offset difference at most 36. Thus it is among 2,3,5,11,13,17,19,23,29,31. Divisibility by 2,3,5 of any displayed binomial is determined by r mod 8,9,25, respectively, because the window lengths are at most 6; divisibility by the remaining listed primes is determined by r modulo that prime, since none divides a denominator ≤6!. These flags therefore match the r=431 template, where no pair has a common non-7 prime.

The six seven-cells remain 3,10,17,24,31,38. Modulo 49 only the cell 10 can have valuation at least 2; the other five have valuation exactly 1. All displayed window lengths are ≤6, so no denominator contains 7 and each r-free product has its cell's 7-valuation. Their pairwise 7-adic gcd is exactly 7. Also no numerator r+h is divisible by r, so every product is r-free and has gcd exactly 7 with N0=7r.

Each r-free product divides |A_(r+41)|: its numerator uses distinct factorial factors r+h, its binomial denominators are integers, and the factorial quotient contains a separate factor 2. Multiplication by r+41 is not asserted; the products themselves are already at least r+41 for r≥431. Similarly 7r divides the group order. Their disjoint windows and valid formal quotient factors c=1 satisfy the listed relaxation, but **do not** prove any corresponding actual subgroup or projected-transitivity chain exists.

The standard prime number theorem in arithmetic progressions is an additional named import for infinitude: since gcd(431,M)=1, π(x;M,431)∼x/(φ(M)log x), see https://en.wikipedia.org/wiki/Prime_number_theorem#Prime_number_theorem_for_arithmetic_progressions. The earlier elementary O(√x log x) bound on excluded repunit primes therefore leaves infinitely many eligible primes in this progression, beyond the finite threshold r+1>7·41!. This establishes an unbounded **integer-model** obstruction only, not a t=41 group counterexample.

## 4. Actual finite control and remaining gap

`frontier-20261028-alternating-multiwindow-obstruction-check.py`, SHA-256 `7582beb2ac507c596b778e2e528144fca66af3737aae9335c39d5c6618dfc660`, 37 LF / 1422 bytes, ran at 19:50:47 PDT on 2026-10-28. It checked all 21 pairwise gcds of the seven integers, r-freeness of the six products, disjoint cells and descent gaps, the per-chain last-window lengths, and actual 472!/2 divisibility/minimum-index arithmetic at r=431; it also checked the integer gcd pattern at one translate r+M, without claiming that translate is prime. The finite run does not construct any subgroup or coset and does not prove the all-prime progression argument.

**Genuine remaining obligation:** show that at least one formal product cannot arise from the required chain of actual proper transitive projections, or find a different exact obstruction or real construction. In particular, a group-order divisor, minimum-index bound, and formally valid c|u! factors are not a subgroup-realizability certificate. No P7 verdict, independent review, Lean proof, publication-priority claim or historical-hold change is implied.
