# f81: same-harness scientific review of alternating successor and P7 candidates

Native clock observed immediately before this file was written: **2026-10-28T19:01:19-0700 PDT**.

## Scope, pins and verdicts

Binding assignment: `manifest-v3.json`, SHA-256 `c9a9df1d45f0c064c8f148e01afc6dcc6169cf84e3f5a055f5f8fe7802b8b09e`. I hash-checked all eight inputs before reading them completely in the manifest's order using raw windows, and rechecked their hashes after reading. All full `sha256` fields, byte counts, and LF counts matched. The author scripts were read, **not run or treated as proof**. Pins, in manifest order:

| # | Input | Actual SHA-256 |
|---|---|---|
| 1 | successor candidate | `f6b9d6ce920f234bc89f2be0aaae709442cc16bfccf8716366df64b322fc228c` |
| 2 | A20 author control | `3d4513eedbfcd3fe6a3d695755f7a2df9cb3c688d63494a8dd69b7347223760e` |
| 3 | orbit induction candidate | `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5` |
| 4 | orbit author control | `a0a0d50ab6cae51a21c060926000c95cec5b254ad7653ba23b4ce08960bc73a1` |
| 5 | mod-8 P7 candidate | `90be5dd44ed0adecd9f9f2ab3bbd0235f309bcc02ad3840c03068c5d7eb02c19` |
| 6 | mod-8 author control | `bc62109865dac90b49fff07cbfbbaa6c3ab97bae94a027794cd985c691e749df` |
| 7 | typed P7 candidate | `b58cde595c44155c158d0d2226b721ace070322233774611d79b7c4772c57aa4` |
| 8 | typed author control | `23c0117eadd1dc9248519a0174b5be910fb294cb47af59f845684ec7cb1ccf6d` |

The counts below are **local to each candidate**, conditional on the named unproved classification import; downstream use of candidate 2 requires its correction described below.

| Candidate | FATAL | MAJOR | MINOR | Verdict |
|---|---:|---:|---:|---|
| 1. successor degree | 0 | 0 | 0 | No defect found in the transfer or stated consequences, conditional on the A_r import. |
| 2. orbit induction | 0 | 0 | 1 | Correctable strict-inequality error at the lower endpoint; the claimed bound, induction and density conclusion follow with the repair below. |
| 3. mod-8 six-step P7 | 0 | 0 | 0 | No additional defect found, conditional on the corrected candidate 2 and the A_r import. Its progression-infinitude claim additionally imports PNT in arithmetic progressions. |
| 4. typed six-step P7 | 0 | 0 | 0 | No additional defect found, conditional on the corrected candidate 2 and the A_r import. In particular, the typed collision works without a mod-8 condition. |

**Scientific MINOR, candidate 2:** `frontier-20261028-alternating-orbit-induction-v1.md:26` asserts `r+j>420` for every allowed pair. At the eligible endpoint `r=419, j=1`, the left side equals 420. This is a false intermediate inequality, not a counterexample to `d_j>7`: for `j=1`, `d_1=r+1>=420>7`; for `2<=j<=6`, `r+j>=421>420>=7 L_j`, so `d_j >= (r+j)/L_j > 7`. Candidates 3 and 4 use the latter bound (`six-step-p7-v1.md:20`, `six-step-typed-p7-v1.md:15-19`) and inherit this repair. No frozen candidate was edited.

**Process MINOR (one grouped metadata issue; no full-hash mismatch):** `manifest-v3.json:63-64,81-82` gives only the 12-hex prefixes in `expected` for inputs 6 and 8 while recording `match: true`, without specifying that `expected` is a prefix. Literal equality with the full SHA-256 values is false; both strings do match the corresponding actual prefixes, and both actual full SHA-256 values match the manifest's full `sha256` fields above. Thus this is an ambiguous/misleading comparison field, not evidence of an altered input. Interpret these two comparisons as prefix checks or record the full expected hashes.

## Named source import and its exact coverage

I directly checked the statement of Baumeister, Burness, Guralnick and Tong-Viet, [Theorem 2(i)(d)](https://arxiv.org/html/2307.13976v2#Thmtheorem2), and the relevant discussion in [Proposition 4.2](https://arxiv.org/html/2307.13976v2#S4.Thmthm2). The theorem states, for odd prime `r`, `G=T=A_r`, `r` not 11 or 23, and `r` not a prime-power repunit (with an additional exceptional `r=5` alternative that these candidates do not use), that a specified Sylow `r`-subgroup has the unique maximal overgroup `AGL_1(r) intersect A_r`. In coordinates adapted to an `r`-cycle this is its normalizer. The conclusion for an arbitrary **proper** subgroup containing that same cycle follows by placing it inside a maximal subgroup.

This import is about the **degree-r point stabilizer** only. It is not a uniqueness theorem for `A_(r+1)` or any later degree, and it does not itself assert the candidates' transfer, orbit induction, binomial divisibility, P7 exclusion, or prime density. Those are the separate derivations assessed below. The theorem's proof and dependency DAG are **not independently verified** here: the source's degree-r case invokes Burnside and the classification cited there as Guralnick [25]; the full alternating discussion refers to Liebeck–Praeger–Saxl [37]. Proposition 4.2 says `n<=24` can be handled by Magma; I did not reproduce that calculation, so the `A_19` classification used for the `A_20` example retains that explicit qualification. The `r>=419` candidates are outside this small-n branch but still depend on the unverified classification. Standard Sylow, Lagrange, orbit-stabilizer, simplicity/order of alternating groups, and elementary finite-field facts are also used.

Candidate 3's optional infinitude statement imports PNT in arithmetic progressions, not needed for its fixed-r result. I checked its statement independently against [Leiden lecture notes, Theorem 6.2.1](https://pub.math.leidenuniv.nl/~evertsejh/ant20-6.pdf), with `q=4,a=1`; I did not reprove that analytic theorem or its dependencies. Candidate 2's relative-density argument and candidate 4's infinitude do not require this extra import.

## Reconstruction of the four arguments

**Successor transfer (`successor-degree-v1.md:17-31`).** For `r+1<2r`, an r-free index implies `H` contains a Sylow r-subgroup; conjugate it to the chosen `R=<r-cycle>` fixing `x`. If intransitive, the orbit containing the r moved points has size r, so `H<=A_r` and its index is a multiple of `r+1`. If transitive, `H_x` is a proper subgroup of `A_r` containing the same `R`; otherwise orbit-stabilizer makes `H=A_(r+1)`. The source gives `H_x<=N_(A_r)(R)` of order `r(r-1)/2`. Therefore `|H|` divides `(r+1)r(r-1)/2`. The latter divides `|A_r|=r!/2`: the distinct factors `2` and `(r+1)/2` both occur in `(r-2)!` for the stated range. Hence `[A_(r+1):H]` is divisible by `r+1`, including for transitive and nonmaximal H. At most one member of a gcd-at-most-7 collection can be r-divisible; two r-free members would both share `r+1>7`, proving the three-index exclusion.

For `r=19`, I checked the repunit eligibility independently and generated, by closure of the permutations `x -> x+1` and `x -> -1/x` on the 20 projective points, a transitive 3,420-element even permutation group containing the specified 19-cycle. It is proper in `A_20`, not contained in the point stabilizer `A_19`, and shows a distinct maximal overgroup exists; the point stabilizer itself is maximal because it is transitive on the other 19 points. This does **not** replay the source's `A_19` uniqueness claim. The named preceding prime-degree family file was hash-checked as `590e8940ca35424a041798661bf8787d2c6477600440082fd5397faad48389a0`; only its lines 1-8 and 42 were consulted for the named families/example, not its full proof. The four displayed forms do not include degree 20 for a prime parameter >=11.

**Orbit induction (`orbit-induction-v1.md:21-47`).** With `n=r+j`, `L_j=lcm(1,...,j)` and `g=gcd(n,u)`, `u C(n,u)=n C(n-1,u-1)` and coprimality imply `n/g | C(n,u)`; since `u|L_j`, also `d_j=n/gcd(n,L_j)` divides that binomial. The strict lower bound needs the correction above. For an r-free proper H containing R, its orbit of R's moved points has size `r+s`. If `s<j`, H lies in that orbit's setwise stabilizer, whose index in `A_(r+j)` is `C(r+j,j-s)`; the large block contains a transposition, ensuring the alternating group has the same subset orbit as the symmetric group. Thus the index has divisor `d_j`. If `s=j`, H is transitive; a point fixed by R has proper stabilizer `H_x` containing R, and `[A_(r+j):H]=[A_(r+j-1):H_x]`. This preserves the r-free condition exactly and inducts down to the successor base. Any gcd-at-most-7 collection has at most one r-divisible index and at most one index per divisor `d_j>7`, hence at most `j+1` indices. This gives the stated no-seven result for `j<=5` and no-eight result for `j=6`.

For the density assertion: bad odd primes from `d=2` have `q=2^a`, giving `O(log x)` possibilities up to x. For `d>=3`, one has `q<=sqrt(x)` and `d<=log_2(x+1)`, so all integer bases give at most `O(sqrt(x) log x)` possibilities. For `p<=2m`, each summand of `v_p(C(2m,m))` is at most 1, so `p^v<=2m` and `C(2m,m)<=(2m)^pi(2m)`. Combining with `C(2m,m)>=4^m/(2m+1)` gives `pi(x) >> x/log x` by monotonicity. The bad proportion tends to zero; removing finitely many small primes does not change this. This is an elementary reconstruction, not a PNT import.

**Mod-8 P7 (`six-step-p7-v1.md:20-32`).** Seven pairwise-gcd-exactly-7 indices are all 7-divisible. At most one is r-divisible. The six r-free ones, if there are six, must occupy all six d-buckets with no repetition; if there are seven, repetition is immediate. For prime `r>3`, `d_3=(r+3)/2`; it is even when `r=1 mod 4`. If `r=3 mod 8`, `r+5` is a multiple of 8 while `v_2(L_5)=2`, so `d_5` is even. Both collide with even `d_1` using the common factor 7, giving gcd at least 14. The coarse `r=431` construction is correctly presented as an integer obstruction to this coarse argument, **not** as a construction of subgroup indices. Its statement that the omitted residue remains open is a limit of this particular parity argument; the separately reviewed typed candidate gives a stronger exclusion.

**Typed P7 (`six-step-typed-p7-v1.md:15-33,37`).** Along any chosen transitive descent, the index remains identical and the fixed R remains inside each proper point stabilizer. On first intransitivity at degree `r+j`, the entire `C(r+j,u)` divides the original index; if the descent reaches degree `r+1`, the base provides type 1. Choices need not be unique: choosing one valid chain per index is enough. Six r-free indices must have six distinct types, since two of type j would share `d_j>7`, so types 1, 2 and 3 necessarily occur. Type 1 is even. Both type-2 alternatives contain `r+2` because `r+2` is odd. Type-3 alternatives for u=1 and u=3 are even: the u=3 numerator contains the consecutive even factors `r+1,r+3`, hence a factor 8, while the denominator 6 removes only one power of 2. These two alternatives collide with type 1 on 14. For u=2, `C(r+3,2)=((r+3)/2)(r+2)` collides with either type-2 alternative on `r+2>7`. This is a contradiction for every eligible r, not just the three checked examples.

## Independent exact checks

Reviewer-authored `independent-exact-check-v1.py`, SHA-256 `ced48e957e30b022b04f0f9c7f06b5ea738ef5f3fd2159f8a9ec29378c66eb6a`, used only Python standard-library integer arithmetic and direct permutation closure. The recorded run `independent-exact-check-v1.txt`, SHA-256 `872f38561e02fd2a0a12e614fdf891bc88833673c959583ac1919488436def4`, exited 0 at its recorded clock. It checks all `u=1,...,j` binomial divisibilities for each `j=1,...,6`, including every binomial and remainder in the receipt. Selected results:

| r | d1,...,d6 | type 2: C(r+2,1), C(r+2,2) | type 3: C(r+3,1), C(r+3,2), C(r+3,3) |
|---:|---|---|---|
| 419 | 420, 421, 211, 141, 106, 85 | 421, 88410 | 422, 88831, 12436340 |
| 421 | 422, 423, 212, 425, 71, 427 | 423, 89253 | 424, 89676, 12614424 |
| 431 | 432, 433, 217, 145, 109, 437 | 433, 93528 | 434, 93961, 13530384 |

For each r the script checks both type-2 choices against each type-3 choice. For u3=1,2,3 respectively, the exact gcds of the relevant **7-scaled** type divisors are `(14,2947,980)`, `(14,2961,2954)`, `(14,3031,1008)` for r=419,421,431; the u3=2 value is the same for either type-2 alternative. These are checks of necessary divisors, not constructed subgroup indices. The proof above, not this finite list, covers all eligible r.

The eligibility search checks primality by trial division and exhausts all integer repunit bases and exponents using `2^d-1<=r`. The only hits `(q,d)` are: 19: `(18,2)`; 419: `(418,2)`; 421: `(420,2),(20,3)`; 431: `(430,2)`. None of those bases is a prime power. The code also checks the `r+1 | (r-2)!` transfer at these four primes and all binomial/typed arithmetic for the 4,801 odd integers from 419 through 10019; this sweep is finite, not a substitute for the written general argument.

For `r=431`, all 21 pairwise gcds of `(3017,3024,3031,1519,1015,763,3059)` are 7, the six `d_j` are pairwise coprime, and each tuple element divides `437!/2`. The sole type-3 coarse entry `1519` has remainders `(217,1519,1519)` modulo `(434,93961,13530384)`, so it satisfies none of the stronger type-3 binomial alternatives. This checks the honesty note without inferring existence or nonexistence of the listed subgroup indices.

## Limits

This is a same-harness review, not an external-family, human, formal-proof, exhaustive subgroup-enumeration, prior-art, novelty, or historical-hold clearance. It is conditional on the explicitly named source classification (and, solely for candidate 3's residue-class infinitude, the analytic theorem above). The finite A20 permutation construction is not a source Magma replay. No held, withdrawn, or quarantined body is used as a premise; no author contact or external model was used. The candidate-2 inequality and manifest comparison-field observations are reported here without modifying the frozen inputs.
