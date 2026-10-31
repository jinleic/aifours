# Same-harness review: level-six (2,2,6) entire-source cone

Native clock observed immediately before creating this review: **2026-10-28T19:02:36-0700 PDT**.

## Verdict and scope

**Conditional scoped verdict: 0 FATAL / 0 MAJOR / 0 MINOR findings.** At the named, unreviewed PBW/full-Cartan/free-positive-source and ideal-transport imports described below, the candidate's `(2,2,6)` entire joint-lowest-source injectivity claim follows on precisely the cone at candidate lines 7–20. I independently reconstructed the source, lowest space, actual local lowering table and all 1,156 affine pencil entries; recomputed the leading determinant and the exact row-product bound; and independently checked the mixed determinant and stated bounded replacement search. The remaining imported source-identification/structural theorems are **not independently established by these finite calculations**. This verdict is conditional, not parent adoption.

There is **no finding of a proved full `r,s>=6` quadrant, F6 or B6, any other level-six type, arbitrary/all-level Serre, priority, or novelty**. Mixed coefficients and the bounded search do not prove a rank defect or exclude another minor/proof. This same-harness review is not a human, external-family, formal/kernel, primary-source, or novelty verification.

## Input identity and read order

The binding manifest `manifest-v1.json` has SHA-256 `93fc8f5f0cd04c60c3ca2f47bd7c5e84a91af0c061bc4420ff3e8e00b590fc6f`. All three inputs were SHA-256 checked **before** body review, and then read **completely in manifest order** in exact raw windows:

| Order | Input | Actual SHA-256 (matches manifest) | Bytes / LF |
|---:|---|---|---:|
| 1 | `written-releases/math-3-positive-freeness-pbw-transcription-addendum-v1.json` | `21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247` | 1404 / 12 |
| 2 | `frontier-20261028-level6-226-entire-source-cone-candidate-v1.md` | `e85ae127d0ea3e552dfd5785f9934371650a902cfbf3ab5ba3baf5d9ca0eb9ea` | 7023 / 70 |
| 3 | `frontier-20261028-level6-free-22-leading-cone-independent-replay-v1.json` | `046fc35bc0891f991446d3b8cd7f02967c8b03663c785220b35a68f012a1fa96` | 638 / 18 |

There were **no manifest-input hash mismatches**. I additionally hashed both written source candidates in candidate line 24 and all ten code/data artifacts pinned in candidate lines 53–62; each matched its stated full digest. In particular, my computations bind the exact pencil `b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc`, leading-cone data `83e62aba742dca5899ef6f1e086b41c054cc16ed03bc839900596d690deb0323`, mixed-polynomial data `874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8`, and replacement-search data `5c6a7888c784f5408405a1ef386bfc32d69770e46544d0b1bd5b9427f036726b`. Hashes identify inputs; they are not scientific verification.

The PBW addendum was read first. Its lines 9–11 qualify the frozen release as a **normalized mathematical transcription/paraphrase of a secondary source**, not a literal source quotation and not a newly verified primary proof. I have retained that qualification throughout; I did not treat the earlier held material as a premise.

## Reconstruction and line-specific dispositions

### Source and lowering — candidate lines 24–26

Conditional on the written source identifications, let `v=e3` and use the fixed Levi adjoint basis

`(E31, -E32, E21, E11-E33, E11-E22, -E12, -E23, -2E13)`

with horizontal increments `(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)`. The two remaining positive node-3 seeds have level `r+1` and `s+1`; for `r,s>=6` their levels are at least seven. Their positive Levi orbits and brackets with positive-level generators cannot reduce that level, so the imported ideal splitting identifies both the level-six source and level-five target with their free-Levi counterparts. This argument requires the actual quotient/ideal-transport import, not merely a character count.

My checker directly enumerates Lyndon words of every needed nonnegative horizontal multidegree, expands their standard brackets in the free associative tensor algebra, checks their triangular independence, and performs **553 exact bracket-closure checks** for all relevant smaller components. Closure plus induction establishes spanning of the generated free Lie components in this finite range; it is not just a count assumed from the author's implementation. At `(2,2,6)` there are **74** source vectors. Using independently constructed `3x3` matrix commutators for `f1,f2`, exact sparse elimination gives rank **40**; the 34 claimed coefficient vectors are independent and all lie in that complete joint kernel. Thus the whole kernel has dimension **34**. The finite-Levi Cartan weights are `2*2-2-6 = -4` and `2*2-2-6 = -4`.

Direct Jacobi gives, in that basis, `f3(m0)=-h3`, `f3(m1)=-r e1`, `f3(m2)=-s e2`, `f3(m3)=-(r+s)[e1,e2]`, `f3(m4)=-s[e1,e2]`, and zero on `m5,m6,m7`; also `[h3,m_j]=(2-r*a_j-s*b_j)m_j`. My independent tensor calculation moves every degree-zero term to the right, checks its cancellation, and uses its commutator with each later tensor letter. The resulting map is affine in `r,s`; evaluation at `(6,6),(7,6),(6,7)` therefore determines it identically. Every one of the **1,156** selected affine entries matches the pinned pencil, and every derived `(L,K,E)` entry matches the pinned leading data. The 34 selected rows are tensor-coordinate functionals on the entire target; they are not a purported lowest-only target. Extra Cartan directions are not assumed away: the local `f3` table uses `h3`, and their representation remains part of the named full-Cartan import.

### Leading determinant and row-product bound — candidate lines 32–45

With `t=(r+s)/2`, `d=(r-s)/2`, the pencil transformation is `L=A_r+A_s`, `K=A_r-A_s`, `E=A_0-6L`. My own exact rational Gaussian elimination gives

`det(L) = -1454389021504438272000`.

For the 34 rows, my exact sums `R_i=sum_j |L_ij|` in order are:

```text
48, 85, 835, 230/3, 712/3, 332/3, 149, 166, 107, 100,
260/3, 182/3, 1459/9, 212/3, 2569/3, 1784/9, 1069/9,
2336/9, 748/3, 446/3, 419/3, 910/9, 173, 331/3, 806/3,
440/9, 643/3, 610, 598/3, 512/3, 185, 541/3, 24, 82.
```

Hence `min R_i=24` and

```text
product R_i =
55748513403702509807736941410682679698921203665176546923913008575293979361280000000000
/2541865828329.
```

Putting `Delta=1454389021504438272000`, exact arithmetic yields

```text
34 product(R_i) / (Delta min(R_i))
= 3206512415644869987797248672494881496686104844344108213394986160000000
  / 150094635296999121 = H;
max_i sum_j |K_ij| = 2000/9;  max_i sum_j |E_ij| = 1365.
```

The `K` maximum occurs at row 28 and the `E` maximum at row 3 (one-based). For any cofactor deleting row `j`, the Leibniz/triangle bound is `product_{h!=j} R_h`; adjugate transposition makes an inverse row sum involve the 34 possible deleted rows. Thus `||L^-1||_infinity <= 34 product(R)/(Delta min(R))=H`. Under the candidate's strict inequality, `||L^-1(dK+E)/t||_infinity<1`; since `t>0`, the geometric-series/maximum-coordinate argument makes the selected matrix invertible, hence the actual whole `D3` map injective, **conditional on the source/target imports**. For any fixed integer `r-s`, taking both parameters sufficiently large gives lattice points in this cone. I found no defect in this argument.

### Mixed determinant and bounded search — candidate line 28

I independently evaluated exact integer Bareiss determinants against the pinned bivariate coefficient list at all **630** nonnegative integer grid points with `x+y<=34`. This triangular grid is unisolvent for total degree at most 34, so it verifies the whole coefficient list, not only sample signs. It has **133 positive and 459 negative** nonzero coefficients; for example the constant is `-603138104964912067285615430860800000000000000` and the coefficient of `x^16` is `586170995820038242605190103040000000`. These signs do not imply that the determinant changes sign on the quadrant.

Using independently reconstructed tensor rows, exact adjugate row-replacement identities, and exact Newton interpolation on each axis, I also reproduced the first **400** deterministic replacements. There are 235 nonzero target tensor-coordinate candidates in the union of the three sampled actions, of which 34 are selected and 201 are alternative rows. The first 201 attempts replace slot 1 and the next 199 replace slot 2. Of the 400, **174** have zero constant, **213** have an `x`-axis coefficient of sign opposite to their constant, and the remaining **13** fail the analogous `y`-axis screen; none survives both. The search was explicitly **not exhaustive** of all one-row replacements or other proof methods. No inference of global noninjectivity or of nonexistence of another certificate is made.

## Named unverified imports and limits

1. The precise PBW import is the frozen release referenced by the qualification, SHA `b80c97dbe4b2c112164f0880ea6cbc5eda5c46421dbb2786f5ca5ede64dac8f8`. Its normalized secondary-source transcription is not a verbatim quotation or independently verified primary proof. The standard free-Lie embedding in the associative tensor algebra over characteristic zero is also used; this review does not supply a formal PBW proof.
2. The original definition packet SHA `8b811cbc88e55b5b48bebef299f356bf10c808968c967ab2ed4aca1065cc03a6`, full-Cartan/Serre/triangular structural input SHA `08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9`, and preliminary free-positive-source/ideal-transport input SHA `f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d` are **named by** the source candidates and were not independently source-proof authenticated here. In particular, the original positive/negative Serre-ideal splitting, zero Cartan intersection/nonvanishing, and actual full-Cartan presentation remain imports.
3. I read and hash-checked the complete written level-one candidate `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and free-Levi quotient candidate `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`. The finite reconstruction above checks their relevant matrix actions and the cone's consequences, but does not independently certify every premise of their all-parameter structural proofs. They remain unreviewed/unadopted inputs for purposes of this verdict.
4. The author's independent replay was read as a claim/receipt, never as proof. No held, withdrawn, or quarantined body was used as a premise. The separate `(4,4,6)` replay is outside this assignment.

## Independent local artifacts

All code and output below were exclusively created in this review directory, import no author code, and use exact standard-library `Fraction`/integers:

| Artifact | SHA-256 |
|---|---|
| `independent-exact-check-v1.py` | `21ea188314c501efd5ec580357ede8288a583ad630d922b605d1f462336f3028` |
| `independent-exact-check-v1.json` | `c51adc8ffd2f6fda1420e0d7fe7fb4e32be0578134fc54a3da8e97e7171b82e4` |
| `independent-mixed-polynomial-v1.py` | `ab8d812cd185f5b85ea3a4975484281975f5749f4d0d8d14d8cb7309c464b21a` |
| `independent-mixed-polynomial-v1.json` | `5b29312fb57a78e90807ff773d532446d353c09a5dc15eb7c41486af47c85d8c` |
| `independent-alternate-screen-v1.py` | `4aab597b6564b6bd2a6c50e8ae4e978a57d2a260f2acf64ba7579ce36c119deb` |
| `independent-alternate-screen-v1.json` | `071e853016796842b9b60a42e1915ed1118fcd9bf02367b14b9c0f0da49a11b7` |

The alternate checker reuses the reviewer-authored source/action reconstruction, not the author's programs. Each checker completed successfully; its JSON receipt records the exact measured results and input bindings.
