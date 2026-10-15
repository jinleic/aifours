# Uniform rank-three continuation — 2026-10-14 (PT)

## Status and exact scope

**Complete candidate coverage was generated for height seven. Height eight remains incomplete. No independent checker was run by this worker.** The full nonsymmetrizable Gabber–Kac/Serre-ideal conjecture remains unsolved; there is no novelty claim.

The following table is an exact producer/coverage inventory, not an independent acceptance receipt. “Written reduction” excludes a **first** extra relation using a positive coordinate of `A alpha`; its use as equality requires the lower-degree prerequisites below.

| Degree, up to simultaneous index permutation | Parameter cells | Degree-stabilizer orbits | Written-reduction cells | Positive-minor candidate cells | Total candidate-covered cells | Uncovered cells |
|---|---:|---:|---:|---:|---:|---:|
| `(3,2,2)` | 144 | 78 | 16 | 128 | **144** | **0** |
| `(4,2,2)` | 256 | 136 | 48 | 163 | **211** | **45** |
| `(3,3,2)` | 324 | 171 | 68 | 167 | **235** | **89** |

The representative counts are respectively:

- `(3,2,2)`: 10 written reductions and 68 positive-minor candidates. The original campaign produced 67 positive minors; the one remaining representative was completed by the row-content method below.
- `(4,2,2)`: 26 written reductions, 86 positive-minor candidates, 24 unsuccessful representatives.
- `(3,3,2)`: 35 written reductions, 88 positive-minor candidates, 25 attempted-but-unsuccessful representatives, and **23 representatives not attempted before the degree deadline**.

The machine-readable final composition is `coverage-summary.json`. The original campaign summaries are deliberately unchanged: the supplemental height-seven certificate must be supplied to the checker explicitly.

## Prerequisites and mathematical reduction

The argument explicitly uses the existing results in `proof.md`:

1. Sections 3–4 identify the descent recurrence with `K`, the recursively generated positive Serre span with `I`, and prove `I` is lowering-stable and contained in `K`.
2. Section 7 proves equality for every rank-three degree having a zero or one coordinate, with no height bound.
3. Section 8 proves that a first extra relation must satisfy `A alpha <= 0` coordinatewise.
4. Section 9 and `evidence/symbolic-222/all-cells-independent-check.json` supply the previously accepted uniform rank-three height-six result. The new input specification records that receipt's SHA-256, and the new checker requires the same receipt.

Consequently the only new interior shape at height seven is `(3,2,2)`. The only new shapes at height eight are `(4,2,2)` and `(3,3,2)`. Missing-edge rank-three GCMs have forest diagrams and are symmetrizable, so the established symmetrizable theorem handles them in every degree. The parameter computations concern all six strictly negative off-diagonal entries.

Write `m_ij=-a_ij`, in the zero-based edge order

```text
(0,1), (0,2), (1,0), (1,2), (2,0), (2,1).
```

At a target degree `alpha`, a cell digit `m<alpha_i` fixes that magnitude to `m`; the digit `alpha_i` means `m_ij=alpha_i+x_ij`, with an independent nonnegative integer parameter. Thus the partitions have sizes

```text
322: 3^2 * 2^4 = 144
422: 4^2 * 2^4 = 256
332: 3^4 * 2^2 = 324.
```

For every degree `beta<=alpha` componentwise, a Serre generator with leading index `i` contributes exactly when its exponent `m_ij+1` fits in this box. Fixed categories specify this exponent exactly; the open category has exponent greater than `alpha_i`, so it cannot contribute anywhere in the box. The recursive ideal construction therefore gives **constant rational Serre spaces on each entire cell**. The source quotient, immediate lower quotients, and ideal projections are fixed rational spaces/maps.

Lowering is linear in the Cartan entries. Therefore the joint lowering matrix on these quotients is affine in the cell parameters. The saved minor is a maximal square minor in quotient bases, not a rank computed only at sample parameter values. The producer clears one positive common denominator, computes the determinant exactly over FLINT's integer multivariate polynomial ring, and saves its full coefficient list. A recorded orientation, strictly positive constant, and strictly positive listed coefficients imply a nonzero determinant for every nonnegative parameter tuple.

Only degree-preserving permutations identify fixed-degree cells. The `cover.json` files contain all 144/256/324 cells and an explicit stabilizer permutation to each representative. The checker independently requires `alpha[p[i]]=alpha[i]`. The stabilizers have order two; their fixed-cell counts are 12, 16, and 18, giving 78, 136, and 171 orbits. No height-six `S3` cover is reused without tracking the degree.

### Written first-defect exclusions

These are the exact whole-cell positive-weight reductions counted in the table:

- For `322`, `m_01=m_02=1` gives `(A alpha)_0=2`; there are 16 cells.
- For `422`, `(m_01,m_02)` equal to `(1,1)`, `(1,2)`, or `(2,1)` gives positive row-zero weight; there are 48 cells.
- For `332`, either `(m_01,m_02)=(1,1)` or `(m_10,m_12)=(1,1)` gives positive row weight. The union has `36+36-4=68` cells.

These exclusions do **not** on their own identify `K_alpha` with `I_alpha` when lower-degree equality is absent. Likewise a new minor proves local injectivity modulo the Serre ideal; it proves equality in that degree only after the immediately lower Serre and maximal quotients are identified.

The checker tracks this dependency. For height-eight cells it coarsens each magnitude category to the thresholds of the immediate lower degree, explicitly permutes that degree to `322`, and consults the corresponding lower-cell result. It reports local certificates and equality cells separately. With the supplemental height-seven certificate accepted, the 211 and 235 height-eight cells in the table become equality candidates; without it, no unconditional equality claim is made for a cell with an unsettled lower dependency.

## Completing the difficult height-seven cell

The original campaign covered 143 of the 144 cells. The sole gap was

```text
alpha = (3,2,2), cell = 332222:
m_01,m_02 >= 3;
m_10,m_12,m_20,m_21 >= 2.
```

All Serre spaces in this box vanish. The source has dimension 30 and the joint lower target dimension 34. Three 30-second Bareiss attempts timed out. A separate 600-second continuation of the first minor also timed out, after 603.661 seconds; its last completed pivot was 23, with 48,053 monomials in the largest intermediate entry. These failures and the exact saved affine minors are retained.

`work/round2_uniform_content.py` attacks the actual intermediate-expression obstruction. For a current `m`-square matrix with pivot `p`, write the Schur numerator as `C=pD-cr`. Then

```text
det(B) = det(C) / p^(m-2).
```

Extracting an exact polynomial gcd from each row of `C` removes repeated content. The producer records the resulting determinant factors, checks each local factorization identity, cancels the factors exactly, and expands the final determinant once. Thus this is an exact algebraic determinant calculation, not interpolation, random evaluation, or numerical fitting.

It produced the ordinary full polynomial certificate in **118.566 seconds**:

```text
content-322-332222/certificate.json.gz
matrix size:       30 x 30
orientation:       -1
positive constant: 512745678002234327040
monomials:         160300
negative terms:    0
SHA-256:           5f9187ee65eebad4398e99209a01a9d605bc94d99f8db79b6069f8571ec5eebf
```

This closes the producer's height-seven parameter ledger. **Acceptance still requires the parent's independent tensor reconstruction and determinant identity check.** The new checker has a separately written row-content determinant routine for this large certificate; it imports neither producer and trusts neither the producer's elimination state nor its factor ledger.

## Precisely preserved height-eight gaps

A six-digit label uses the degree-dependent category convention above. A listed representative denotes its complete degree-stabilizer orbit. All and only the complementary orbits have the candidate evidence counted in the table. Full expanded cell lists are in each original `summary.json` under `uncovered_cells`.

### Degree `(4,2,2)`

The 24 unsuccessful representatives, covering 45 cells, are:

```text
141222 142212 142222 241212 241222 242212 242221 242222
341222 342112 342122 342211 342212 342221 342222
441112 441121 441122 441212 441221 441222 442121 442122 442222
```

All 136 representatives were entered. Across all attempts at this degree, the producer recorded 86 positive minors, 63 mixed-sign determinant polynomials, and 35 timeouts. Some successful cells required a later row choice. Failed attempts remain present even when another minor succeeded.

### Degree `(3,3,2)`

The 25 attempted-but-unsuccessful representatives are:

```text
122322 123311 123321 131312 132212 132311 132312 132321 132322
133311 133312 133321 133322 222322 223312 223321 223322
232312 232322 233122 233211 233212 233221 233222 233312
```

The following 23 representatives were not attempted after the 1,200-second degree deadline:

```text
233321 233322
313111 313112 313122 313211 313212 313221 313222
313311 313312 313321 313322
323211 323212 323222 323311 323312 323321 323322
333311 333312 333322
```

Their union covers 89 cells. The attempted part recorded 88 positive minors, 65 mixed-sign determinant polynomials, and 33 timeouts. No certificate is inferred for a skipped cell.

The remaining obstruction is **this certificate search**, not a demonstrated extra relation: chosen maximal minors can have mixed coefficients, and multivariate exact elimination can grow too large for the declared time bounds. No baseline-rank defect or characteristic-zero counterexample was established. Extending the successful row-content method to these remaining height-eight cells was not part of the completed campaign, and no such output is claimed.

## Additional positivity route that failed

`work/round2_uniform_newton.py` attempted all 82 complete mixed-sign polynomials belonging to still-uncovered representatives. It changed from monomials to the exact multivariate falling-factorial basis using Stirling numbers. For integer `x>=0`, every falling factorial `x(x-1)...(x-k+1)` is nonnegative, so positive constant and nonnegative coefficients in that basis would be a sufficient integer-parameter positivity criterion.

All **82** transformed polynomials retained negative coefficients; **zero** cells were recovered. The run took 0.621 seconds, and `newton/manifest.json` binds every attempted source polynomial by SHA-256. This failed sufficient test does not refute positivity or injectivity. No unused Newton-certificate acceptance branch remains in the independent checker.

## Reproducibility, bounds, and storage

All commands are recorded exactly in `commands.txt`; producer input specifications record source hashes, parameter domains, dependency receipt hashes, and computational bounds. All mathematical runs were serial, with one process and FLINT configured for one thread.

Observed runtimes:

| Run | Seconds |
|---|---:|
| Corrected three-degree campaign, total | 2508.007 |
| Initial `322` stage | 107.801 |
| `422` stage | 1200.123 |
| `332` stage | 1200.019 |
| Longer ordinary Bareiss attempt, timed out | 603.661 |
| Successful row-content `322` supplement | 118.566 |
| Failed falling-factorial positivity pass | 0.621 |

The ordinary campaign used 30 seconds per selected minor, 1,200 seconds per degree, at most three deterministic row-order choices, and a 250,000-monomial intermediate-entry cap. Signal delivery can occur after a running FLINT operation returns, explaining small deadline overruns. The row-content supplement used a 300-second limit and the same term cap.

An initial run stopped because FLINT exponent objects were not directly JSON serializable. The fix was explicit integer conversion. `initial-failure.json` and the original partial output directory preserve that failure; the corrected campaign used `candidates/` and overwrote nothing. The partial initial gzip is not an acceptance certificate.

At the recorded storage snapshot, this evidence directory occupied **12,724 KiB**, and the entire target occupied **38,548 KiB**, comfortably below the shared storage constraints. The final small report and summary files were added after that snapshot.

## Exact parent checker command

Run from `ai4s/kac-moody-serre-relations/`:

```sh
env UV_CACHE_DIR=/tmp/kac-serre-uv-cache OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  uv run --with python-flint==0.9.0 python work/round2_uniform_check.py \
  evidence/round2-uniform/candidates \
  --extra-certificates evidence/round2-uniform/content-322-332222/certificate.json.gz \
  --output evidence/round2-uniform/parent-independent-check.json
```

The checker reconstructs Serre spaces with the independent tensor implementation, reconstructs all affine lowering entries by associative-word deletion, checks each exact polynomial identity and positivity claim, checks all stabilizer mappings and lower-degree dependencies, rejects altered determinant constants and omitted coverage cells, and binds the exercised certificates and sources by SHA-256. It refuses to overwrite an existing receipt.

**This command has not been run here.** If it accepts all supplied candidates, the intended scope flags are `uniform_height7=true` and `uniform_height8=false`; those are expected scope flags, not observed verification output. No builds, linters, formatters, or software test suites were run.
