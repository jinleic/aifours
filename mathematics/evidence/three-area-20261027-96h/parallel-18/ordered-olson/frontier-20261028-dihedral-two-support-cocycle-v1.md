# Two-support reflection cocycle in the `R=3p−4` band

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 18:09:12 PDT 2026**. Scope: written exact results, plus the finite checks §5. The earlier high-band candidate is not an input; no independent peer review, all-band closure or novelty is claimed.

## 1. Exact original-word two-support calculation

Let p be any odd prime. Let W be an actual ordered `D_(2p)` word with `R=3p−4` rotation occurrences and at least two reflections. Fix actual reflections i<j with exponents y_i,y_j. For each actual rotation exponent t, write its signed value −t if it occurs strictly between i,j and +t otherwise. Assume this signed multiset has EXACTLY the two distinct values x,z, with multiplicities m,n satisfying

`m+n=3p−4`,  `m,n>=p−2`.

Equivalently, its maximum multiplicity is at most `2p−2`. Let `T_ij=mx+nz` be the total signed sum.

Among ALL choices of exactly `2p−2` of these actual rotations, the obtainable signed sums are **exactly**

`F_p \ { μ_ij }`, where  `μ_ij = T_ij+x+z = (m+1)x+(n+1)z`.  (1)

Consequently the specified two reflections can be extended to an original-order identity `2p` selector if and only if

`y_j−y_i != μ_ij`.  (2)

Proof. Omit `p−2` rotations. Since each value occurs at least p−2 times, for every q=0,...,p−2 we may omit q occurrences of z and p−2−q of x. The omitted sums form p−1 distinct residues

`(p−2)x + q(z−x)`.

Their only missing residue is the formal q=p−1 value `−x−z`. Subtracting from T_ij gives (1). The exact original selected product is `r^[signed rotation sum + y_i−y_j]`, giving (2). Distinctness and original order are retained: q is realized by actual occurrences. QED.

This calculation applies at p=3 as well, but the bounded examples below start at p=5. It does not say a word with target μ_ij has no OTHER selector; it only characterizes selectors using this specified pair and `2p−2` rotations.

## 2. Coupling three actual reflection gaps

Let i<j<k be actual reflection positions. Assume each of the three pairs (i,j), (j,k), (i,k) satisfies the EXACT two-value/multiplicity hypothesis of §1. For pair u<v denote the two distinct signed values by `x_uv,z_uv`, total signed sum by `T_uv`, and unique missing value by

`μ_uv = T_uv+x_uv+z_uv`.

Let `T_0` be the total of the original raw rotation exponents. The intervals (i,j) and (j,k) are disjoint and their union is (i,k), since j itself is a reflection. Therefore

`T_ij+T_jk−T_ik = T_0`.  (3)

If the actual word has no `2p` identity selector, (2) forces `y_j−y_i=μ_ij`, `y_k−y_j=μ_jk` and `y_k−y_i=μ_ik`. These differences must add. Hence the following computable raw-word scalar must vanish:

`Ω = μ_ij+μ_jk−μ_ik`

`  = T_0+(x_ij+z_ij)+(x_jk+z_jk)−(x_ik+z_ik)`.  (4)

**Theorem.** If Ω is nonzero, an actual original-order `2p` identity selector exists, using two of these three specified reflections. This conclusion is independent of the reflection exponents: at least one of their three actual directed differences must differ from its unique unavailable rotation sum. Then (2) constructs an actual selector for that pair.

More generally, create a graph on actual reflection occurrences and retain only pairs satisfying §1. Put the uniquely missing μ on each edge in increasing-index orientation and its negative in reverse orientation. No-selector requires every oriented graph-cycle sum to vanish, since each edge difference must equal the corresponding difference of the SAME actual reflection exponents. A nonzero cycle is therefore an identity-selector certificate. Vanishing cycle sums alone are NOT a sufficient condition for an avoiding word or for nonexistence of other selectors.

## 3. Opposite-sign specialization

If all raw rotations are `r^a` or `r^(−a)`, a!=0, then every qualifying signed pair's two values are a and −a, so `x_uv+z_uv=0`. Under the three §1 hypotheses, Ω in (4) is simply `T_0`. Thus, whenever `T_0!=0`, the actual word has an original-order selector regardless of the values of the three chosen reflection exponents.

This is a conditional, value-dependent COUPLING of three actual gaps. It is not a claim that every word has three qualifying pairs, and it is not a bilinear-expression cancellation or L_RES proof.

## 4. Explicit all-prime actual family

For every prime p>=5, let a=1 and take the following original occurrences, where each `s_y` denotes `r^y s` and y_1,y_2,y_3 are ARBITRARY in F_p:

`[2p−5 copies r] · [p−3 copies r^(-1)] · s_(y_1) · r · r^(-1) · s_(y_2) · r · r^(-1) · s_(y_3) · [p copies s]`.

There are `2p−3` raw +1 rotations, `p−1` raw −1 rotations, total R=3p−4, and F=p+3 reflections. Each of the first three reflection pairs crosses zero, one or two balanced `(r,r^(-1))` gaps, so its signed multiset STILL has `2p−3` +1 values and `p−1` −1 values. Its maximum is below `2p−2`, it has exactly two values, and its missing value is `μ=T_0=−2 !=0`. Thus Ω=−2 and §2 constructs a selector for EVERY triple `(y_1,y_2,y_3)`.

These pairs are outside the earlier diverse-three-signed-value sufficient condition because each support has only two values. This is a solvable illustration, not an avoiding family or a claim that all earlier methods fail.

## 5. Exact finite checks, not a universal audit

`frontier-20261028-dihedral-two-support-cocycle-checker.py`, SHA256 `85cf8559f0296e9ac6c94a0e0921e5d4fdb7e71035797b7c7680a075b4688163`, actually returned `PASS_TWO_SUPPORT_COCYCLE_EXACT`; the saved result `frontier-20261028-dihedral-two-support-cocycle-check-results.json` has SHA256 `06990663297f88c469b7edcabfbfc5370eaa07a93810639f95c996b9ff4ee785`.

For p=5,7,11,13 respectively it checked all x!=z and all multiplicity pairs in §1: 120,336,1320,2184 exact missing-support formulas. It also constructed every p³ choice of the three reflection exponents in the specific §4 full-word family and directly multiplied an actual original-index identity selector: 125,343,1331,2197 words, respectively. The script rejected a deliberately shifted missing-residue formula because the shifted value was actually attainable.

These finite calculations do not exhaust the original R=3p−4 class, establish any global no-go, or independently review this proof. The unrestricted count band, original Olson conjecture, L_RES and novelty remain open here.

**END — two-support exact formula, gap cocycle and bounded scope.**
