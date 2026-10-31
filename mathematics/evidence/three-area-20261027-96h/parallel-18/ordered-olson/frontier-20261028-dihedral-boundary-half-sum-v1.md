# Exact boundary-majority support and half-total gap coupling

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:11:12 PDT 2026**. Written proof candidate plus bounded exact checks, no independent mathematical review, formal proof, novelty or full-band closure.

## 1. An exact fixed-pair classification

Let p be any odd prime. In an ACTUAL ordered dihedral word with `R=3p−4` rotation occurrences, fix two actual reflection positions i<j. Sign each rotation exponent by −1 if it is strictly between i,j, +1 otherwise; let T be the sum of all R signed values. Suppose the largest signed-value multiplicity is EXACTLY `2p−2`, occurring at x. It is unique, and exactly `p−2` outlier occurrences remain; write their values `x+d_1,...,x+d_(p−2)`, where each d_i!=0.

Let Σ be the set of signed sums of ALL actual choices of exactly `2p−2` rotations. Then:

* If all d_i belong to `{d,−d}` for one nonzero d, `Σ = F_p \ {T/2}`.
* If not, `Σ = F_p`.

Accordingly, the specified pair's actual `2p` identity selector exists if and only if the actual directed reflection difference lies in Σ. In particular, whether or not Σ is full, a target DIFFERENT from `T/2` always has an actual selector. Division by 2 is valid because p is odd. The p=3 case is included: there is just one outlier and the first branch applies.

## 2. Written proof without a joint-affinity assumption

Choose ANY subset S of the p−2 actual outlier occurrences and fill the remaining slots with actual x occurrences, of which there are exactly2p−2. The resulting signed sum is

`(2p−2)x + sum_(i∈S)d_i = −2x+sum_(i∈S)d_i`.  (1)

Conversely every `2p−2`-rotation selection is of this form, because the only non-x rotations are these outliers. By nonzero translation growth, the subset sums in (1) have at least p−1 values.

Complementary subsets S and S^c have selected signed sums adding to

`−4x+sum_i d_i = (3p−4)x+sum_i d_i = T` in F_p.

Thus Σ is invariant under the ACTUAL involution `v↦T−v`. If it misses exactly one residue, that residue must be its unique fixed point T/2. This proves the at-most-one-missing and half-total assertion without pretending independent actual reflection gaps have no mixed term.

For p>=5, the inverse subset-sum lemma proved in `frontier-20261028-dihedral-three-value-swaps-v1.md`, SHA256 `dc24d3f6e6bbc0c25a2682c5ab2a5a0115b9aa3e114cba70d2de23d055d6bccf`, states that p−2 nonzero d_i have a p−1-element subset support ONLY when they are all ± one nonzero d. It does not assume zero-sum-freeness. Conversely, if u of the d_i equal d and v equal −d, u+v=p−2, their subset sums are the p−1 distinct values `q d`, `−v<=q<=u`; hence the support is exactly p−1 and its missing value is T/2 as above. For p=3 the single nonzero d_i is trivially of this form and gives p−1=2 values. QED.

The imported inverse lemma's proof and exact bounded check are in the named source; it is an author-owned named input, not an independent-review verdict. The half-total at-most-one-missing statement itself needs only the elementary growth/complement argument just displayed.

## 3. Three-gap coupling at the boundary

Let i<j<k be ACTUAL reflections in the same original word. Suppose the largest signed multiplicity for EACH of these three pairs is `2p−2`. Write their signed totals T_ij,T_jk,T_ik, and let T_0 be the total raw rotation exponent. Exact interval bookkeeping gives

`T_ij+T_jk−T_ik = T_0`.  (2)

For each pair, either its support is full and it already yields an actual selector, or no-selector forces its actual directed reflection difference to equal T_uv/2. The three directed reflection differences add, so no-selector implies

`T_0/2 = (T_ij+T_jk−T_ik)/2 = 0`.

**Boundary cocycle theorem:** if `T_0!=0`, the original word has an identity selector of exactly2p occurrences using two of i,j,k, irrespective of their reflection exponents. This theorem does not require the three pair supports to contain only two values; symmetric three-value boundary supports are explicitly included. Nor does it presume that reflection-gap choices commute or that a selector exists in a shortened word.

For a graph of such boundary pairs, no-selector forces each oriented edge label to be `T_uv/2`, hence every oriented cycle sum must be zero. A zero cycle alone does NOT prove avoidance.

## 4. Relation to the full local low-M classification

For p>=5, combine this paper with the preceding two named author-owned stages:

* If `M<=2p−3` and signed support has at least three values, the diverse-swap proof in `frontier-20261028-dihedral-three-value-swaps-v1.md` gives FULL support.
* If signed support is exactly two values x,z, each of multiplicity at least p−2, `frontier-20261028-dihedral-two-support-cocycle-v1.md`, SHA256 `8fbfd99636eade69410dd700836995b62ec95575b9f33a3a612633fc3ede03e4`, gives exact support `F_p\{T+x+z}`.
* At `M=2p−2`, §1 gives the exact full-versus-half-total classification even for three-value symmetric support.

These cases classify the selected-rotation sum support for each specified pair with `M<=2p−2`. They leave `M>=2p−1` and global compatibility/other-selector questions open; they do not establish that any word attains the no-selector residual. No pending R=3p−3 theorem or f63 historical separation assertion is an input.

## 5. Explicit interleaved family and exact checks

For p>=5 choose arbitrary y_1,y_2,y_3 and concatenate actual occurrences

`[2p−2 copies of 1] · s_(y_1) · r · s_(y_2) · r^(-1) · s_(y_3) · [p−4 copies of r] · [p copies of s]`.

There are R=3p−4 rotations and F=p+3 reflections. For all three specified pairs, the `2p−2` zero-exponent rotations remain unchanged and the p−2 nonzero signed outliers all lie in `{+1,−1}`. Hence M=2p−2 and each rotation support is exactly `F_p\{T_uv/2}`. The raw total is `T_0=−4 !=0`, so the boundary cocycle forces an actual selector for EVERY triple of the reflection exponents. At least two of the three pairs have three signed values, so this is not confined to the two-support calculation. It is a solvable example, not an avoiding word or a claim of priority.

`frontier-20261028-dihedral-boundary-half-sum-checker.py`, SHA256 `7969f6dbe049788d5b78c61e7e9382d877690a6650a5d9ec4a47643a5e35a163`, actually returned `PASS_BOUNDARY_HALF_SUM_CLASSIFICATION`; saved `frontier-20261028-dihedral-boundary-half-sum-check-results.json`, SHA256 `0b54fbc72723cbd42a4d4623e3b6fd9bc6aa87f5e5c269649e36add8e22ffecc`. For p=3,5,7 it exhausted respectively 2,64,7776 nonzero outlier tuples relative to zero majority and found full/one-missing counts 0/2, 48/16, 7680/96, exactly as stated. For the explicit interleaved family it checked p=5,7,11,13 and ALL p³ triples of y values, directly multiplying respectively 125,343,1331,2197 original-order selector lists. These are finite checks, not a proof for arbitrary words or a substituted global counterexample.

**END — exact boundary classification and three-gap coupling.**
