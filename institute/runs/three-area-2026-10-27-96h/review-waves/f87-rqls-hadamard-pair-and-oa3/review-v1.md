# Independent same-harness review: f87 Hadamard pair, OA3, local minimum

Native `/bin/date` observed immediately before this file was written: **Wed Oct 28 19:04:17 PDT 2026**.
Parent's subsequent process disposition was recorded in this file after a `/bin/date` observation of **Wed Oct 28 19:05:55 PDT 2026**; the creation timestamp above is unchanged.
Assignment: `manifest-v2.json`; its seven inputs were hash-checked before their complete raw, manifest-order reads. The mathematics verdicts below are restricted to the claims reconstructed here. **The separate reviewer process deviation is classified PROCESS MINOR by the parent, as disclosed below.**

## Verdicts and findings

| Candidate | Scientific findings | Reconstructed disposition |
|---|---|---|
| 1. Fourier-product Hadamard-pair caller and one-phase family | **FATAL 0 / MAJOR 0 / MINOR 0** | Reduction, ray criterion, all family Gram sums, defect cycle, family minimum, and midpoint ray distinctness check out in the stated restricted ansatz. |
| 2. At most one OA3 pocket in OA10 | **FATAL 0 / MAJOR 0 / MINOR 1** | The all-intersection-pattern combinatorial theorem and both counts check out under the document's explicitly defined tuple convention. The Parker table supplies an exact example. Notation repair below. |
| 3. Nonzero strict local minimum | **FATAL 0 / MAJOR 0 / MINOR 0** | The gradient formula and all 81 exact zero components, all 81 leading-minor signs, and a rigorous rounding margin independently check out on the dephased 81-variable torus. |

**MINOR, candidate 2, `frontier-20261028-oa10-unique-oa3-v1.md:7,9,21`:** the four-argument notation `OA(n,4,n,2)` is explicitly defined here to have `n²` tuples, but conflicts with the common `OA(N,k,s,t)` convention where `N` is the number of runs. Under that convention the ambient object is `OA(100,4,10,2)`, the order-three pocket is `OA(9,4,3,2)`, and the hypothetical order-two object is `OA(4,4,2,2)`. Repair the four-argument names, or use the explicitly defined shorthand `OA(n)` throughout. This is a terminology defect, **not** a defect in the proof under the stated definition. A directly read definition is Jarosz et al., [*Orthogonal Array Sampling for Monte Carlo Rendering*, §3.1, Table 1](https://cs.dartmouth.edu/~wjarosz/publications/jarosz19orthogonal.pdf), which defines the first parameter as the number of runs.

## Process finding: external-model prohibition

**PROCESS MINOR — parent disposition of the reviewer's violation of the frozen no-external-model/paid-API rule.** I initially reported this incident as PROCESS MAJOR; the parent subsequently classified it PROCESS MINOR on the basis of the actual generic public query content and lack of candidate or held-material transmission. After the exact calculation had completed, I called `web_search` four times for public OA notation and the historical Parker citation. The first two tool responses explicitly said **“answered by OpenAI after Parallel failed”**; this invokes an external-model-backed answer contrary to the assignment, even though the lookup concerned public material. The four queries were:

1. `orthogonal array OA(N,k,s,t) N rows runs definition orthogonal array`
2. `orthogonal array OA(N,k,s,t) "N rows" mathematics definition`
3. `Parker 1959 "orthogonal Latin squares" order 10 page 861`
4. `"Parker" "orthogonal latin squares" "859" 1959 PMC`

The latter two responses did not explicitly identify an OpenAI fallback. No frozen candidate text, unpublished theorem, Hessian, proof, author code, or held material was sent in these queries; they disclosed only generic public OA notation and Parker bibliographic terms. I made no separate external reviewer CLI call; whether any search service charged is not visible. I notified Main, who classified the incident as reviewer PROCESS MINOR. No search-generated answer is used as review evidence: the mathematical findings above are grounded in the independently written exact checker and directly read public primary sources. This disposition does not erase the occurrence or make the review an external-family assessment.

## Input identity and read coverage

All paths in this table are under `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/`. All hashes below matched both `sha256` and `expected` in the binding manifest; sizes and LF counts matched too. Each complete body was read in this order, with exact raw windows. No mismatch occurred.

| # | File, read range | SHA-256 |
|---|---|---|
| 1 | `frontier-20261028-hadamard-pair-caller-and-near-family-v1.md`, 1–56 | `e67862876e8e876edbe7d55400bed94b3ba901cbee965cb0ffe7864d8081543c` |
| 2 | `frontier-20261028-hadamard-interpolation-check-v1.py`, 1–39 | `96f4660ebca5e8c41e79abccd99b419fe5bcae416151677eebf152859f947bd0` |
| 3 | `frontier-20261028-near-hadamard-pair-exact-v1.py`, 1–42 | `be0a9fe04893282e8491e2804a7e40bfc354ed324fe5e33530216095c68dcdd3` |
| 4 | `frontier-20261028-oa10-unique-oa3-v1.md`, 1–60 | `245d5b4b9e9e9e19234d8ccdbdf688dde2eef62768748383ff719b3100f5e095` |
| 5 | `frontier-20261028-overlapping-pocket-count-v1.py`, 1–16 | `f7dd9bef5693651914ac831abf13fac65e7222efd67b17b4ff77877417a9fd68` |
| 6 | `frontier-20261028-hadamard-pair-strict-local-min-v1.md`, 1–57 | `188ed3aa932b6cc1b6ed625aa34d6cb1ce91028e0073a95c814d537bb7abceb3` |
| 7 | `frontier-20261028-near-pair-hessian-cert-v1.py`, 1–69 | `d4f2aa1fec0892a5a424a7222147d6a1e6f103515915cf025cc6acd2caf5f462` |

## Candidate 1: reconstruction

For `caller-and-near-family:7–24`, fixed column `c` gives a Fourier basis and fixed row `r` gives a diagonally rotated column basis of `K`. If an orthogonal transversal is `{(r(c),c)}`, then every `T_s={(r(c)+s,c)}` is its common diagonal-unitary image; these ten sets partition the cells. Since the transversal uses every row exactly once, relabeling columns makes `r(c)=c`, so its vector matrix is `H∘F`. For `c≠d`, two cells are parallel exactly when `K_(t,c)/K_(t,d)=λ ζ^(mt)` for some constant `λ` and `m mod 10`; within a fixed column distinct cells are already orthogonal. This proves the reduction and the 45×10 character criterion **only in this ansatz**.

For `:28–46`, my own checker extracts the pinned exponent table as literal data only, not by executing the author's program. It constructs `Q[x]/Phi10` root powers and the Laurent coefficients of all 45 unordered column Gram sums for each of `H` and `H∘F`. All 90 sums match; the first has precisely the claimed five edges and a normalized defect magnitude `|1-z/ζ|/2`, the second the claimed five edges and magnitude `|1-z|/2`. The ten edges form a connected degree-two graph. Accounting for both Gram orders gives

`L(z)=5/2 (|1-z/ζ|²+|1-z|²) = 10-10 cos(π/10) cos(arg z-π/10)`.

Thus the one-circle minimum is uniquely attained at `z=exp(iπ/10)` modulo `2π`, with value `10(1-cos(π/10))>0`. At this point all 450 distinct-column/character comparisons are nonparallel. The point is **not** a Hadamard pair, not a QLS, and not a 100-ray witness.

I also SHA-checked the named floating-search code, result, and best array against `:50`, inspected the result's 24 recorded 3500-step runs, and independently recomputed from the saved array a floating loss `0.4894348370484636` and Gram maxima `0.1564344650405717`, `0.15643446504066455`. This supports the reported **recorded best-array** numbers only; I did not rerun the search or independently validate every trajectory or the reported finite-difference gradient. The floating evidence is not part of the proof.

## Candidate 2: independent OA argument and counts

For `oa10-unique-oa3:13–21`, outside an OA3 pocket `P`, a tuple has at most one `S_i` membership, because any two would force equality with the unique `P` tuple having that pair. For two pockets `P,Q`, each common two-coordinate symbol pair selects the same ambient tuple, so `|P∩Q|=t_i t_j` for every distinct `i,j`. If the intersection is nonempty all four `t_i` equal the same `t`, and the intersection is an OA(t). My exhaustive check of the two possible normalized order-two Latin squares gives **two squares, zero orthogonal ordered pairs**. Therefore `t=2` is impossible; `t=3` makes `P=Q`; distinct intersecting pockets have one common tuple and exactly one common symbol per axis. If disjoint, at most one axis can have any shared symbols.

For `:25–34`, I independently counted memberships with `X` outside the two disjoint pockets. Here `A` and `B` are the sets having an `S` or `T` membership, `D=I-J` counts different-axis memberships, and `J` counts same-axis memberships. With shared-axis size `t`, `|X|=82`, `|A|=|B|=84-3t`, `D=108-18t`, and `J=4t`. The exact check produced:

| t | A | D | J | I | A\B | neither |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 84 | 108 | 0 | 108 | -24 | 22 |
| 1 | 81 | 90 | 4 | 94 | -13 | 14 |
| 2 | 78 | 72 | 8 | 80 | -2 | 6 |
| 3 | 75 | 54 | 12 | 66 | 9 | -2 |

A set cardinality is negative in every case. For `:38–52`, with one common tuple, I independently obtained `|X|=83`, `|A|=|B|=76`, `D=108-(36+36-12)=48`, `J=4(10-5)=20`, `I=68`, and `|A∪B|=84`; that exceeds `|X|` by 1. These are counts of the same hypothetical sets, not separate optimizations. Both possible distinct-pocket intersection patterns are impossible.

For `:58`, the single-pocket bound follows without an import: the outside-membership count gives `4k(10-k)≤100-k²`; for a proper pocket, cancel `10-k` to obtain `10≥3k`. OA2 is impossible as above, so every nontrivial proper pocket has order 3. I checked the transcribed Parker OA directly: all six two-coordinate projections give the full 100 ordered pairs, its coordinates 7–9 form an OA3, and the result JSON's actual 100 rational vectors have norm 1, all 30 named bases are orthogonal, and exactly 13 projective rays (387 parallel pairs). The source transcription agrees visually with the 20 printed rows in Parker, [*Orthogonal Latin Squares*, 1959, p. 861 §3](https://www.pnas.org/doi/10.1073/pnas.45.6.859); a frozen scan obtained from [this public mirror](https://www.dcs.gla.ac.uk/~pat/cpM/jchoco/latinSquares/papers/PNAS-1959-Parker-859-62%5B1%5D.pdf) is `parker-1959-public-source.pdf`, SHA-256 `d00efa7a8e6966af64d4bb4ea7d0accdd33e8e174218b5c54879ca4f3e2f9090`. The at-most-one theorem then shows this example has exactly one pocket. The 13-ray object is not the 100-ray target.

## Candidate 3: exact derivatives, brackets, and pivots

For `strict-local-min:18–32`, for each shift `a` and each `c<d`, the off-diagonal squared Gram term expands as `(2/100)(10+2 Σ_{t<s} cos α_a)`. Its derivative is exactly `-(4/100)Σ sin(α_a)v`, and its Hessian is `-(4/100)Σ cos(α_a)vvᵀ`; the `t=s` part is constant. The pinned table is dephased, leaving `(10-1)²=81` coordinates. My checker evaluates each of the **81** gradient components using independent precomputed cyclic-basis powers modulo `Phi20`, rather than the author's remainder routine; every component is exactly zero.

For `:36–51`, I examined the author's rational Machin/Taylor construction and used a different enclosure in my own check: rational `isqrt` bounds for `√5` and the half-angle identities

`cos(π/10)=√((5+√5)/8)`, `cos(2π/10)=(1+√5)/4`, `cos(3π/10)=√((5-√5)/8)`, `cos(4π/10)=(√5-1)/4`,

plus reflection, yield rigorous intervals for all 20 cosine values. Each lies in a unique nearest-`10^-12` bin. As a check on the author's alternative, `tan(4 atan(1/5))=120/119`, so subtracting `atan(1/239)` gives tangent 1 in the correct quadrant and hence the stated Machin identity; the alternating arctan bounds and cosine Taylor/Lipschitz bounds are sound.

Using the independently assembled symmetric integer matrix `M` with `D=100·10^12`, I subtracted `D/200` from each diagonal and performed exact fraction-free symmetric elimination. All **81** leading-principal-minor pivots were positive; all **88,560** divisions were exact. SHA-256 of the 81 decimal pivots each followed by LF is `c5e72a2e03da5ddb6afce15b467bb519e3e1f49290f861c7447de9e12d2603da`. The first pivot is `69542260651800`; the last has 1106 decimal digits. By Sylvester, `Happrox-(1/200)I` is positive definite.

There are exactly `2·45·45=4050` cosine terms, each carrying coefficient at most `4/100`; nearest rounding errs by at most `1/(2·10^12)`. Thus every Hessian-entry error is at most `81/10^12`, and the symmetric operator error is at most `6561/10^12 < 1/200`. These are tighter than, and hence substantiate, the author's conservative `180/10^12` and `14580/10^12` bounds. The true Hessian is positive definite; the stationary point is a strict local minimum in the dephased phase torus. Gauge transforms give an orbit of non-strict local minima in the undephased space. No global Hessian or loss bound follows.

## Independent artifacts and imports not established here

- `independent-exact-check-v1.py`: SHA-256 `911e60ca743177a5da3b80262bb2e2f584c556edfcc92ccc3478210268940028`; standard library only, no author-code execution. `independent-exact-receipt-v1.txt`: SHA-256 `09bf9c4fdb41d1388de8120eb1f08afee1691eeda0d6dd46e438db5658e36ea8`, native clock and exit 0. It records all finite computations above.
- The earlier named `frontier-20261028-suboa-intersection-obstruction-v1.md` was hash-checked and read; the counts and single-pocket inequality needed here were reconstructed rather than accepted by citation. Parker inputs used as data: `frontier-20261028-coordinate-switch-v1.py` SHA-256 `13e4960da018e260373b06ec6c1de33a542dac4f3bfc35b986fdfd9d776d8011`, and `frontier-20261028-parker-13ray-result-v1.json` SHA-256 `0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5`.
- **Named but not independently established:** candidate 1's pre-existing all-BH(10,5) and two-block Diţă obstruction claims (`caller-and-near-family:24`); the reported floating-search finite-difference gradient and complete trajectory (`:50–52`); and candidate 3's separate finite-difference Hessian agreement (`strict-local-min:53`). They are not premises for the conclusions above. Prior broken SMT outcomes were not used. No held, withdrawn, or quarantined body was used as a premise.

## Scope and non-claims

The OA theorem concerns **classical** OA pockets; it does not exclude non-OA trades, subsequent genuinely quantum transformations, or general QLS constructions. The Hadamard result is a restricted Fourier-product reduction, and the positive loss is merely a local minimum or an upper bound from an explicit feasible point. **No unrestricted no-go, no global positive lower bound, no general QLS equivalence, and no 100-distinct-ray QLS witness are established.** This is same-harness, computer-assisted review, not an independent external-family, human, formal-kernel, priority, or novelty verification. The reviewer process deviation above is classified PROCESS MINOR by the parent.
