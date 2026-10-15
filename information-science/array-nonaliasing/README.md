# 非均匀采样问题：任意阵列的无混叠条件

As of **2026-10-14 (America/Los_Angeles)**.

**Verdict: SOLVED-BY-PRIOR-WORK for the isotropic, noiseless, single-source reading.** The complete condition is reproduced below, including arbitrary real sensor coordinates, rank deficiency and partially commensurate alias groups. An exact terminating rational/algebraic-coordinate decision procedure is implemented. Two explicit rational arrays refute two different arbitrary-basis shortcuts in a 2022 paper. Those counterexamples are **certification, novelty unclear**, not an asserted new discovery. Arbitrary directional conformal gain functions are treated accurately at the projective-characterization level, **not counted as a general constructive solution**.

## 1. Source

* 《10000个科学难题·信息科学卷》, “非均匀采样问题 / The Problem of Non-uniform Sampling”, 穆鹏程、殷勤业, book **446–448**, PDF **467–469**.
* All three page images were opened and read: [446](sources/page-0467.png), [447](sources/page-0468.png), [448](sources/page-0469.png). The garbled PDF text layer was used only for navigation; quotations and formulas were read from images.
* The book's displayed co-array is `c(x)=sum_{(m,n) in theta(x)} w_m w_n*`, with `theta(x)={(m,n):x=x_m-x_n}`. Its discussion is about antenna-array spatial-spectrum/grating-lobe aliasing, not the recovery of arbitrary multicomponent fields from finitely many samples.

## 2. Problem

### Verbatim book statement and translation

Book 447:

> 然而，实际中的天线阵列大多不能保证是线阵，更不能保证是均匀线阵，而共形天线阵列的使用则更是在空域的非均匀采样，此时，阵列需要满足什么样的条件才能保证不出现空谱混叠就成为一个关键问题。

**Translation:** In practice, antenna arrays generally need not be linear, much less uniformly linear; using conformal antenna arrays is an even more general form of spatial nonuniform sampling. It therefore becomes a central question what conditions an array must satisfy to guarantee the absence of spatial-spectrum aliasing.

Book 447–448:

> 因此，当想要使用任意阵列进行空域非均匀采样时，该阵列需要满足什么样的条件才能保证不出现空谱混叠仍然是一个难题。

**Translation:** Thus, when an arbitrary array is used for spatial nonuniform sampling, determining what conditions the array must satisfy to guarantee the absence of spatial-spectrum aliasing remains a difficult problem.

### Formalization and quantifiers

For **every** N>=1, d>=1, finite sensor list `p_1,...,p_N in R^d`, and **every** allowed direction-coordinate set `U subset R^d`, let

```
a_j(u) = exp(i*pi*p_j dot u),       p_j measured in half wavelengths,
D_j = (p_(j+1)-p_1)^T,
G = {x : Dx in 2 Z^(N-1)}.
```

For a single narrow-band far-field emitter with unknown nonzero complex amplitude, no alias means

```
for all u != v in U and all c != 0,  a(u) != c a(v).
```

The exact answer is

```
G intersect (U-U) subset {0}.
```

It is equivalent to the absence of **full-height** matched-beamforming copies for **every strictly positive real taper on all sensors**. It does not forbid smaller sidelobes and does not apply to arbitrary nonzero weighting: a one-sensor active weight has constant magnitude everywhere.

The algorithmic full physical domains are the closed interval `[-1,1]` for the line-array direction coordinate, closed unit disk for a planar array with one-hemisphere convention, the unit circle for in-plane directions, and the unit sphere for 3D directions. Their difference sets are closed radius-two balls. Full-sphere physical directions are not identifiable by a planar isotropic geometry merely by relabelling their projection. Closed-domain nonaliasing requires **every nonzero alias difference to have norm strictly greater than 2**. Exactly half-wavelength line spacing aliases the two endfire endpoints; deleting or identifying them is a different domain convention.

## 3. Status and primary-source comparison

This is **not an unresolved isotropic geometry problem as of 2026-10-14**. No claim of a newly solved open problem is made.

| Primary source opened | Matched result | Important limits |
|---|---|---|
| Godara–Cantoni, *JASA* **70(2), 467–475 (August 1981)**, [DOI 10.1121/1.386790](https://doi.org/10.1121/1.386790); [author institutional record](https://research-repository.uwa.edu.au/en/publications/uniqueness-and-linear-independence-of-steering-vectors-in-array-s/) | Original steering-uniqueness conditions for linear, planar and general arrays; the 2022 article explicitly credits its Theorem 6 with an N&S integer-wrapping/linear-algebra test | Primary abstract/metadata opened; original full text and verified publisher PDF returned HTTP 403. Exact original constants, gains hypotheses and boundary wording were **not** independently read. Multi-source linear independence is a different question. |
| Tucker–Zhao–Ahmad–Potter, *IEEE SPL* **29, 2457–2461 (2022-11-28)**, [DOI 10.1109/LSP.2022.3224834](https://doi.org/10.1109/LSP.2022.3224834), [complete primary author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC9757818/) | Proposition 3: arbitrary-direction-set translate disjointness. Corollary 4: shortest nonzero alias norm strictly greater than 2 | Isotropic, single-source model; full-column-rank geometry; a full-rank solution lattice is assumed for the basis section. **Corollary 5 and equation (11) are separately refuted below.** No separately obtained publisher PDF is claimed. |
| Kastinen–Kero, *AMT* **13, 6813–6835 (2020-12-16)**, [DOI/full primary 10.5194/amt-13-6813-2020](https://amt.copernicus.org/articles/13/6813/2020/) | Section 2.1, equations (1)–(6): arbitrary complex receiver gains; perfect ambiguity iff absolute normalized inner product is one | Nonzero response vectors; numerical gradient searches/simulation do not certify global absence of aliases. Zero responses require a separate blind-direction case. |

[Source comparison and dated search log](sources/source-comparison.json) contains access outcomes and scope. Local HTML/XML/metadata snapshots are retained and hash-bound in the check and review receipts. No search miss is used to prove openness, absence of an erratum, or novelty.

## 4. Attack and complete result

The full derivation is [proof.md](proof.md).

1. **Exact isotropic theorem:** divide sensor phases by a reference sensor to obtain `D(u-v) in 2Z`. Equality in the positive weighted triangle inequality connects projective ambiguity to full-height copies.
2. **All real geometries:** `G=ker(D) direct-sum L`, where L is discrete and may have rank anywhere from 0 to rank(D). For example, rows `(1,0),(sqrt(2),0),(0,1)` give `G={0} x 2Z`, not a full-rank 2D lattice.
3. **Finite rational/algebraic algorithm:** rank deficiency yields a small nonzero kernel witness. Otherwise select d independent rows B of D and enumerate exactly
   `|k_i| <= floor(||B_i||)`; test `x=2 B^-1 k`, `0<||x||<=2`, and **all** rows `Dx/2 in Z`. The bound is complete by Cauchy–Schwarz. This is an executable reproduction of the classical wrapping test, not an unbounded reformulation.
4. **Algebraic exactness:** inputs use a real primitive element given by an irreducible polynomial and rational isolating interval; coordinates are rational polynomials in it. Residue-field arithmetic, exact root counts and shrinking rational intervals decide equality, integer membership and sign without floating tolerances. Every finite real-algebraic tuple has this encoding.
5. **2D repair:** an explicitly verified Gauss-reduced basis has its first vector shortest; the proof is included. Thus both shortcuts become correct after that certified 2D reduction. **No unproved 3D reduction claim:** use bounded enumeration `|z_i|<=floor(2||row_i(V^-1)||)` instead.

### Two different published shortcuts, two certificates

Columns of V are lattice basis vectors. Set `D=2V^-1`, append the origin as reference sensor, and the entire alias group is exactly `V Z^2`.

| | Example E: equation (11) | Example C: Corollary 5 as well |
|---|---|---|
| V | `[[3,29/10],[0,3/10]]` | `[[3,30],[0,3/10]]` |
| Nonzero sensor rows D | `(2/3,-58/9),(0,20/3)` | `(2/3,-200/3),(0,20/3)` |
| Short difference x | `v2-v1=(-1/10,3/10)` | `10v1-v2=(0,-3/10)` |
| Squared norm | `1/10` | `9/100` |
| Binary vertex test | passes: squared norms `9,17/2,349/10` | passes |
| **All pairwise** vertex test | fails; this example alone does not refute Corollary 5 | passes; minimum squared pair distance `9` |
| Physical disk directions | `u=x/2`, `v=-x/2` | `u=x/2`, `v=-x/2` |
| Original-data steering vectors | both `(1,-1,-1)` | both `(1,1,-1)` |

The binary test omits difference coefficients. Even checking every pair of vertices misses the integer coefficient `(10,-1)` in C. An arbitrary skew fundamental cell need not contain a nearest lattice point in its origin-adjacent translates. These refutations leave Proposition 3 and Corollary 4 intact. A 3D orthogonal extension is also checked.

### Directional conformal gains: precise coverage limit

With `b_j(u)=g_j(u)exp(i*pi*p_j dot u)`, two **nonzero** responses alias iff all 2-by-2 minors of `[b(u),b(v)]` vanish, or equivalently the absolute normalized inner product equals one. Supports must agree. Two blind directions are indistinguishable; a blind and visible direction are not projectively equal under a nonzero-source assumption. Identifiability including a zero measurement requires injectivity on visible projective responses and at most one blind direction; guaranteed detectability requires no blind directions.

For `g_j(u)=c_j h(u)` with fixed nonzero `c_j` and nowhere-zero `h`, the isotropic theorem applies after invertible diagonal calibration. For arbitrary gain functions, the pairwise equations are a **characterization only**, not a finite constructive global decision or synthesis procedure. The book does not specify such a gain-function representation, so that broader reading is not declared fully resolved.

## 5. Claims and verification

| Claim | Status | Evidence type |
|---|---|---|
| Exact arbitrary-real isotropic condition, including projective phase and positive matched tapers | PROVED in classical written mathematics; SOLVED-BY-PRIOR-WORK | Reproduction; [Theorem 1](proof.md) |
| Full-domain finite rational/algebraic decision with complete wrapping bound | PROVED in classical written mathematics; implementation exercised | Reproduction/certification; Theorem 3 |
| Equation (11) for any basis | REFUTED | Exact E certificate and original-sensor phases |
| Corollary 5 for any basis | REFUTED | Exact C certificate and original-sensor phases |
| Both tests after certified Gauss reduction in 2D | PROVED in classical written mathematics | Lemma 4; unimodular reduction checked |
| General arbitrary directional-gain constructive solution | NOT ESTABLISHED | Existing projective criterion only |
| Novelty of shortcut counterexamples | NOVELTY-UNCLEAR | No primary correction established by the logged searches |
| Lean/kernel proof or human journal certification | NOT CLAIMED | Written proof and machine arithmetic are distinct |

The decisive exact run completed successfully: **2 counterexamples, 19 general decision cases, 22 controls**, including **13 rejected tamper/false-claim/invalid-input controls**. [Raw structured receipt](evidence/check-exact.json) records rational and algebraic decisions, complete candidate-box counts, original phase equalities, separate shortcut results, Gauss transforms and input/code/proof SHA-256 hashes. The general search returns the first valid alias, not necessarily the shortest; shortest norms in the examples are independently certified by reduction. No incomplete search is labelled alias-free.

Reproduce from the repository root using the existing SymPy 1.14.0 environment, with an isolated output path:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-ddp-static-output-feedback/venv/bin/python \
  information-science/array-nonaliasing/work/check_exact.py \
  --max-candidates 100000 \
  --output /Users/jinleic/jinleic-workspace/scratch/ai4s-array-nonaliasing/parent-check.json
```

For a new array, place its exact JSON under the permitted scratch directory and use `--input PATH --output PATH`. Example rational input: `{"positions":[["0","0"],["1/2","0"],["0","1/2"]],"domain":"ball"}`. Example algebraic input: `{"field":{"minimal_polynomial":[1,0,-2],"isolating_interval":[1,2]},"positions":[["0"],["1"],[["0","1"]]]}`. Polynomial coefficients are **ascending** for coordinates and **descending** for `minimal_polynomial`. The optional candidate cap raises an explicit error before an oversized search; omitting the cap implements the finite mathematical algorithm without a fixed search limit. The executed suite is single-threaded and uses no new environment or solver installation.

## 6. Independent review

The complete proof was frozen as [reviewed-proof.txt](evidence/reviewed-proof.txt) and sent to the configured other-vendor Claude CLI, tool-free, with `--safe-mode --no-chrome --tools '' --permission-mode dontAsk --no-session-persistence --output-format json` and `stdin=DEVNULL`. The prompt embeds the complete proof, the challenged source statements and primary-source hashes; source images and HTML/XML were inspected by the authoring worker, not independently opened by the tool-free referee. The runner reads model/effort from `docs/knowledge-system/DELEGATE_MODELS.json`.

The first invocation timed out after 1800 seconds and yielded **no verdict** ([failure record](evidence/review-attempt-1.json)). A bounded retry completed in 600.19 seconds with actual reported model **claude-opus-5-5**, effort **max**, a parsed successful final event, and verdict **REVISE for minor exposition issues; no load-bearing mathematical defect found**. Its [complete receipt](evidence/claude-review-retry.json) independently re-derives both counterexamples and endorses the isotropic prior-work classification. All five findings are accounted for in [referee dispositions](evidence/referee-dispositions.json):

* F1: replace an imprecise successive-minima parenthetical with a complete finite-index proof that the discrete alias component is a lattice.
* F2: remove the misleading “circular” description; a genuinely certified Minkowski-reduced basis does validate both tests through its shortest-vector property. The actual 3D implementation remains complete bounded enumeration.
* F3: verify Tucker equation (3) directly: its matrix uses sensor differences, exactly `P=pi D`; add that explicit source convention.
* F4: reject the suggested bibliographic conflation: image filenames are **book PDF pages**, not the 1981 JASA article; identify them explicitly.
* F5: add a directional-gain disambiguation witness, state what common-pattern zeros do, and spell out the 3D sensor/direction example.

The referee reviewed the preserved pre-revision proof, not the checker code. No second-round ACCEPT, human certification or kernel verification is claimed. `check-exact.json` binds the same pre-revision proof preserved as `reviewed-proof.txt`; the checker and its input cases were unchanged by these exposition/source-clarification revisions. [Final artifact manifest](evidence/final-artifact-manifest.json) binds the delivered files separately. Parent replay can produce a fresh receipt for the final prose snapshot without overwriting this evidence.

## 7. Disposition and limits

The isotropic reading should be removed from an unresolved-problem shortlist, not promoted as a new full solution. The reproducible shortcut counterexamples can be retained as a correction candidate with novelty unresolved. Original 1981 full-text access remains a bibliographic limitation, not a mathematical blocker to the independently proved criterion. No external author contact or submission was made. General directional-conformal constructive conditions require a specified gain-function class and are not silently replaced by the isotropic special model. Parent replay and any future human review are separate from the executed checks reported here.
