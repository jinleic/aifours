# The all-high signed-majority subclass at `R=3p−4`

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:26:54 PDT 2026**. A self-contained **WRITTEN proof candidate**, with finite checks in §8. It has not received a disjoint scientific review, formal proof, novelty clearance or global-adoption verdict.

## 1. Exact theorem and limits

Let p be ANY odd prime. Let W be an ACTUAL original-order word of length `4p−1` in `D_(2p)`, with exactly `R=3p−4` rotations and `F=p+3` reflections. For each pair of actual reflection positions i<j, sign each rotation exponent by −1 strictly between i,j and by +1 outside; let M_ij be the largest multiplicity among the resulting signed values.

**Theorem.** If `M_ij>=2p−1` for EVERY actual reflection pair i<j, W has an identity subsequence of exactly2p original occurrences, in increasing original index order.

The ALL-pairs hypothesis is essential to this proof. Its negation is not an avoiding-word witness, and this candidate does NOT settle the entire R=3p−4 band, other bands, L_RES or the original all-group problem. The earlier high-band and low-M candidates are not mathematical inputs.

Write `L=2p−1`, `n=p−3`, and use exponents in F_p. Suppose for contradiction that no such original-order identity selector exists.

## 2. Align and concentrate the high majorities

Each signed majority is unique because `2L>R`. It cannot be zero: at least L zero rotations and F>p reflections give two equal reflection exponents; these and `2p−2` actual zero rotations select identity.

Fix one pair and its nonzero signed majority h. Any other pair's L-sized majority class meets it in at least `2L−R=p+2` ACTUAL rotation occurrences. At a common occurrence both signed values are ± its raw nonzero exponent. Thus every pair's signed majority belongs to `{h,−h}`, and at least L raw rotation exponents belong to that set.

Orient h as a with m>=p raw occurrences of a; let n_- be the number of raw −a occurrences. If m>=2p, choose 2p a-rotations. If n_->=p, choose p of each sign. Both give all-rotation selectors. Therefore `p<=m<=L` and `n_-<=p−1`.

For any actual reflection pair, put `u=#(a rotations strictly between)−#(−a rotations strictly between)`. Its signed ±a multiplicities are `m−u` and `n_-+u`. One is at least L, so

`u<=m−L<=0`  OR  `u>=L−n_->=p`.  (1)

There are F−1=p+2 gaps between consecutive reflection occurrences. At most one has positive u, because it contains at least p a-rotations and m<=2p−1. At most n_-<=p−1 have negative u, because each consumes at least one distinct −a rotation. At least two gaps have u=0. In any such gap, the +a signed multiplicity must be the L-majority, so `m=L`.

Exactly n=p−3 extra rotations remain. Write their exponents b_i and `d_i=b_i−a`. For every nonempty subset S of k extras, the actual S plus `2p−k` core rotations exists and has exponent `sum_(i∈S)d_i`. Hence the d_i are zero-sum-free under the no-selector assumption. This includes p=3, where there are no extra rotations.

Let `A⊆F_p` be all subset sums of the d_i and E its complement. Each d_i is nonzero, so elementary nonzero-translation growth gives `|A|>=min(p,n+1)=p−2`; also 0∈A. Therefore

`|E|<=2` and `0∉E`.  (2)

## 3. Four adjacent-reflection boundaries are forced

Let g be the number of distinct prefix counts of the L core a-rotations at the F actual reflection positions. Let B be the number of ACTUAL adjacent-reflection boundaries in W. Exactly F−g consecutive-reflection gaps contain no core rotation; B of those are empty, and each of the other `F−g−B` consumes at least one extra rotation.

The other g−1 gaps each contain c>=1 core rotations. If k is the number of −a extras in such a gap, the signed ±a multiplicities for its bounding reflections are `L−c+k` and `n_-+c−k`. Since the signed L-majority is one of ±a,

`c<=k` OR `c>=L−n_-+k >= p+2`.  (3)

Call a gap LARGE if `c>=p+2`. At most one is LARGE, since `2(p+2)>L`. Each non-LARGE positive-core gap consumes at least one −a extra by (3). Thus if g>=2,

`p−3 >= (F−g−B)+(g−2) = p+1−B`,

and if g=1, `p−3>=F−1−B=p+2−B`. Consequently **B>=4** (and B>=5 when g=1). The counts concern disjoint actual reflection gaps; other rotation values are never silently identified with −a.

## 4. Three disjoint adjacent pairs cannot coexist with no-selector

For ANY pair of actual reflections with no rotation between them, let b be the second reflection exponent minus the first. For any subset of extras, select it with `2p−2−|S|` core rotations; all have positive sign. The actual product with that pair is identity exactly when `sum_(i∈S)d_i=2a+b`. Thus no-selector forces

`s=2a+b ∈ E`.  (4)

Now choose two DISJOINT actual adjacent reflection pairs, with their associated s_1,s_2. Select their four reflections and, for any subset S of extras, select `2p−4−|S|` core rotations. No rotation lies inside either selected adjacent pair, so all selected rotations have positive sign. Their product is identity exactly when `sum_(i∈S)d_i=s_1+s_2`; hence `s_1+s_2∈E`.

Because E contains at most two nonzero residues, this forces `s_1=s_2=s` and `E={s,2s}`: if s_1!=s_2, their sum cannot equal either without one being zero; if equal, 2s is a distinct second element.

If THREE disjoint adjacent reflection pairs existed, applying the preceding observation to every two gives the same s for all three. Select their six reflections plus `2p−6−|S|` core rotations and any subset S of extras. All rotation signs remain positive, and identity would occur at `sum d_i=3s`. But `3s` is neither s nor 2s for odd p and s!=0, so it lies in A, giving an actual length2p selector. At p=3, the chosen rotation count is zero and A={0}; the same argument applies. Thus no-selector allows at most TWO disjoint adjacent pairs.

Combining this with B>=4: a reflection run of length ℓ has ℓ−1 adjacent boundaries and floor(ℓ/2) disjoint adjacent pairs, with `ℓ−1<=2 floor(ℓ/2)`, equality only for odd ℓ. Therefore B=4, the maximum disjoint-pair count is exactly2, and the ONLY possible non-singleton run patterns are

* one actual run of length5; or
* two separate actual runs of length3.

In particular g>=2, since g=1 would require B>=5.

## 5. The forced runs are constant

In the run5 case, let b_1,...,b_4 be consecutive directed reflection differences. Pairs (1,2) and (3,4), pairs (1,2) and (4,5), and pairs (2,3) and (4,5) are disjoint. The two-pair observation above forces all four values `2a+b_i` to equal one s.

In the two-run3 case, ANY adjacent pair from the first run is disjoint from ANY adjacent pair from the second, so again all four adjacent directed differences equal one b and `E={s,2s}`, `s=2a+b`.

In either pattern, take the first and third reflections of one run. They are not adjacent, but there is **no rotation between them**: skip the middle reflection. Their directed difference is 2b, so by (4) `2a+2b∈{s,2s}`. Equality to s gives b=0; equality to 2s gives 2a=0, impossible because p is odd and a!=0. Thus b=0, every non-singleton run is constant, and

`E={2a,4a}`.  (5)

No claim about the number of reflections required by OTHER selectors is made.

## 6. Saturate the gap count, then use the endpoints

With B=4 and g>=2, the lower bound in §3 is exactly p−3, the total number of extras. Hence there is EXACTLY one LARGE gap (otherwise g−1 positive-core gaps would force p−2 extras); every counted non-LARGE/no-adjacency gap uses exactly one extra; the LARGE gap contains none; and no extra rotation lies before the first or after the last reflection. Its ≥p+2 core rotations lie strictly between the endpoint reflections.

Let c be the total number of core a-rotations strictly between the first and last reflections. ALL n_- raw −a extras are inside those endpoints. The endpoint signed +a count is `L−c+n_-`, and its signed −a count is c. Because `c>=p+2` and `n_-<=p−3`, the +a count is at most `2p−6<L`. The endpoint has an L-majority in `{±a}`; it must therefore be −a, forcing c>=L. Hence **all L core rotations and all extras lie strictly between the endpoints**.

The run5, or the two run3s, supplies two disjoint adjacent reflection pairs that avoid BOTH endpoint occurrences. For run5, an endpoint lying in the run must be at its end; the other four consecutive reflections give two pairs. For two run3s, each run contains at most one endpoint, and the remaining two reflections provide a pair. The two runs are disjoint. By §5 both pairs have equal exponents within each pair, so inserting either pair between the selected endpoints does not change the endpoint reflection contribution or any selected rotation's signs.

Let δ be the last endpoint exponent minus the first. For k=0,1,2, select the two endpoints plus k of those equal adjacent pairs, and select an arbitrary subset S of extras together with `2p−2−2k−|S|` actual core rotations. This is possible for every S: `|S|<=p−3<=2p−6` even at k=2. There are exactly2p selected occurrences. As all rotations are between the endpoints, the signed core value is −a and each extra's signed deviation from it is −d_i. Their actual product is identity exactly when

`sum_(i∈S)d_i = 2(k+1)a−δ`.  (6)

The three targets for k=0,1,2 are distinct for every odd prime p, because 2a is nonzero. But A misses at most two residues. Thus one target in (6) is realized by an actual extra subset, yielding an original-order identity selector—a contradiction. This proves §1.

## 7. Dependencies and assurance

The proof above derives every structural assertion in its own scope from the displayed signed-count and subset-sum arguments. Earlier same-owner low-M, two-support and other-count-band packets are not imported; no held or quarantined guidance is used as a premise. The gap-count lower bound and the endpoint insertion are written mathematical arguments, not an inference from the limited checks below.

## 8. Actual bounded checks

`frontier-20261028-dihedral-all-high-normal-checker.py`, SHA256 `957eededdc53f4dca5f9be47785c3068a57b461ac7ec7ca2b739f2485525ccbf`, actually returned `PASS_ALL_HIGH_NORMAL_LAYOUTS`; saved output `frontier-20261028-dihedral-all-high-normal-check-results.json`, SHA256 `8792f8814847d22e14a02fff5b2cc3d85f34579c5fc6d261e06d85d52b24c2ef`. It constructed and directly multiplied 240 actual original selectors for both structural layout families at p=5,7,11,13; observed branches were one-five k0/k1/k2=97/10/13 and two-threes=95/14/11. It verified all actual reflection pairs were high, actual run patterns, and endpoint-pair insertion. The same checker was exercised separately on 60 p=3 empty-extra instances using `frontier-20261028-dihedral-all-high-normal-p3.py`, SHA256 `cbfe7a845410336b41917e9851f4b3386295a33706d041029af0862587613860`; result `899b5a8c08d7adaab512f7098135029363717e5722d6506747c9639193d6191e`.

A separately written finite combinatorial audit `frontier-20261028-dihedral-all-high-structure-audit.py`, SHA256 `188d9b8e73743d7498b925bc751022aa86a0a19dd8671e6f0b2f0f2761f2ad95`, returned `PASS_ALL_HIGH_FINITE_STRUCTURAL_AUDIT` in result `3625a310334a35f325c877877005194ff2be4b0a4c41390479b14b607e347cdb`. It checked all adjacency patterns with exactly four boundaries for p=3,5,7,11,13; every maximum-two-pair case had a 5-run or two 3-runs and supplied two disjoint pairs avoiding endpoints. It also checked the missing-set pairing lemma in those finite fields and exhaustively checked nonzero extra tuples at p=3,5,7.

These do not independently establish the all-word signed-majority and gap-count deductions, and the scripts do not constitute a formal proof or external-family review. A disjoint full-source scientific review is requested.

**END — all-high actual-word proof candidate and bounded scope.**
