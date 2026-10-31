# Signed-pair selector for arbitrary reflection positions

Owner **MathOlson-2-2**, original math-2. Native `/bin/date` before this write: **Wed Oct 28 17:46:24 PDT 2026**. Scope: **WRITTEN**, with separately disclosed bounded actual-word checks. No owner other than this author has reviewed this packet.

## 1. Full actual-word theorem

Let p be an odd prime, `D_(2p)=<r,s | r^p=s^2=1, srs=r^(-1)>`, and let W be an ACTUAL word (arbitrary length and order) with R rotations and at least two reflections. Suppose `R>=3p−3`. Choose ANY two actual reflection positions `i<j`. For each rotation occurrence k with exponent x_k define its **signed value**

`v_k = x_k` if `k<i` or `k>j`, and `v_k=−x_k` if `i<k<j`, all in F_p.

Let M_ij be the largest multiplicity of a value among these R signed occurrences. If

`M_ij <= R−(p−1)`,

then the ORIGINAL word W has a `2p`-occurrence identity selector using **exactly these two specified reflections** and `2p−2` actual rotations, in their original increasing index order. No reflection adjacency, same-gap pairs, zero rotation, prescribed reflection exponent, or ability to reorder occurrences is assumed.

### Written proof

Among R signed values, a maximum number of disjoint pairs of different values is

`C = min(floor(R/2), R−M_ij)`.

The upper bound is immediate. To construct that many, repeatedly pair occurrences from two currently largest distinct-value piles; the remaining largest-pile obstruction is precisely the stated bound (equivalently, if M_ij>R/2, pair every nonmajority occurrence with a majority one; otherwise the two-largest greedy construction leaves at most one). Thus the displayed hypothesis and `R>=3p−3` yield at least `p−1` disjoint unequal signed pairs.

We need to omit `t=R−(2p−2)` rotations. Here `t>=p−1`. Choose exactly `p−1` such unequal signed pairs and omit ONE occurrence from each. Fix any further `t−(p−1)` omissions outside those pairs. Such fixed omissions exist because

`R−2(p−1) − [t−(p−1)] = p−1 >= 0`.

All remaining rotations are retained, exactly `2p−2` of them. Across the independent choice of one omitted occurrence per pair, the set of omitted signed sums is all F_p. Indeed the first choice has two distinct sums; each additional nonzero swap d replaces a nonempty support A by `A ∪ (A+d)`. If A is proper, it strictly grows: otherwise `A=A+d`, and since d generates the prime-order additive group, A would be all F_p. After `p−1` independent pairs the support has at least p elements.

Write the specified reflections as `r^(y_i)s` and `r^(y_j)s`. For a choice of omitted signed-sum U, the increasing-order product of all retained rotations and these reflections is

`r^[ (sum_k v_k) − U + y_i − y_j ]`.

Choose `U=sum_k v_k+y_i−y_j`. This is an actual attainable sum, so the selected original indices have product 1. QED.

The proof does NOT require each unequal signed pair to lie in a single reflection gap: a pair crossing either selected reflection may work because its signs are computed from the specified actual reflection positions. For R>3p−3 the extra omissions are fixed outside the pairs as above; the proof is not a shortened-word witness substitution.

## 2. A genuine necessary residual at R=3p−3

Now suppose W has the full original length `4p−1`, `R=3p−3` rotations, and hence `F=p+2` reflections. If W has NO original identity `2p`-selector, the theorem implies the following simultaneously for EVERY actual reflection pair `i<j`:

* The signed multiset has a value `a_ij` of multiplicity at least `2p−1`; it is unique, since two such disjoint value classes would have more than R occurrences.
* None of these values is zero. If one were zero then at least `2p−1` actual rotation occurrences have exponent zero. Because `F=p+2>p`, two reflection exponents coincide; choose them and any `2p−2` zero rotations to obtain an identity selector regardless of their positions.
* There is ONE fixed nonzero `a∈F_p`, determined up to sign, such that at least `2p−1` raw rotation exponents lie in `{a,−a}` and EVERY `a_ij` is either a or −a. To see this, use any one reflection pair's majority a. Its `2p−1` corresponding actual rotations have raw exponents in `{a,−a}`. Any other pair's majority class intersects the first in at least `2(2p−1)−(3p−3)=p+1` rotation occurrences; on each shared occurrence both signed values are ± its same nonzero raw exponent. Thus the other majority must be ±a.

These are necessary restrictions on a hypothetical avoiding word, NOT an assertion that such a word exists or that the restrictions themselves suffice to avoid all selectors. In particular, pairs declared ineligible by §1 may nevertheless have actual identity selectors by this or a different mechanism.

## 3. Explicit all-prime family outside the earlier fixed-I/gap/run certificates

For every odd prime `p>=5`, form the actual full word

`W_p = [ product_(j=1)^(p+2) ( r · (r^(−2j)s) ) ] · (r^2)^(2p−5)`.

The displayed product is an ordered concatenation, not a commutative product. It has length `4p−1`, `R=3p−3`, `F=p+2`, and all rotation exponents are nonzero. Every reflection run is a singleton, so neither an adjacent-reflection nor a long-reflection-run hypothesis holds. Every rotation gap is monochromatic, so the earlier disjoint unequal **same-gap** resource is zero.

Choose any two reflections, with indices in the j-labels u<v. Exactly `q=v−u` of the initial r rotations lie between them; the rest of the initial rotations are outside, as are all suffix `r^2`. The three signed values `−1,+1,+2` are distinct for `p>=5` and have multiplicities respectively `q`, `p+2−q`, and `2p−5`. Since `1<=q<=p+1`, all three are at most `2p−2`. Hence §1 supplies an actual original-order selector for **every** specified reflection pair.

An explicit one is: take the first and second reflections; take the first initial rotation, the initial rotations labeled `j=3,...,p−1`, and ANY p of the final `r^2` rotations. There are `p−2+p+2=2p` selected occurrences. No selected rotation is between the two reflections, their exponents are −2 and −4, and the ordered exponent is `(p−2)+2p + (−2−(−4)) = 3p =0 mod p`.

For the earlier fixed-I two-reflection certificate, take I to be the FIRST `2p−2` rotations. It contains all `p+2` initial r's plus `p−4` suffix `r^2`'s, so its sum is `−6 !=0`. At the j-th reflection its previously defined actual prefix potential is `(−2j)+2j=0`. Consequently NO pair of reflections paired with this particular I gives identity, despite every reflection pair succeeding with a suitable different actual rotation subset.

The quotient-type word has `2p+5` odd runs: `2(p+2)` singletons and a final odd rotation run. Thus it also cannot contain `2p−1` chronologically separated equal-type pairs. Direct reason: such pairs would cover all but one letter, so all pair intervals would have length two except possibly the single interval containing the one unused letter. Outside that exception each run is even; the exceptional letter can create at most three odd runs. This is incompatible with `2p+5`.

Thus this family is neither a counterexample to the ordered Olson theorem nor a global hard instance: it demonstrates that the new signed-pair mechanism strictly extends the named previous fixed-I, same-gap, adjacent/long-run, and saturated-separated-packet certificates.

## 4. Actual bounded checks, no novelty claim

The exact producer `frontier-20261028-dihedral-signed-pair-experiment.py`, SHA256 `d45bbf21b92b786152f453bfe8810b0e578ef6a48b72115c36b0e13f297e718c`, generated `frontier-20261028-dihedral-signed-pair-results.json`, SHA256 `74e0f7a73f8e029abc782f9aa8626e24100d92e76d38e02107aaecef4d7842e8`.
It used fixed seed2026102807 and 480 full actual words: 120 each for p=3,5,7,11, with rotation values sampled uniformly, concentrated on {0,1,−1}, or all 1. Across ALL17,400 actual reflection pairs, 13,427 met the sufficient condition and the producer generated their selectors; 3,973 pairs failed this condition and were NOT decided.

Separately written checker `frontier-20261028-dihedral-signed-pair-checker.py`, SHA256 `98acacadac20960d9320cb4c3d850e5a9f7912495a332075e896b4bab751e445`, did not import the producer. Its actual one-pass result `frontier-20261028-dihedral-signed-pair-checker-results.json`, SHA256 `61cb52a1489ec4698499a343ed7223ffee05989e4c7fd996e69fdc90e6b0d3b9`, is `PASS_INDEPENDENT_SIGNED_PAIR_REPLAY`: it replayed all480 words and all17,400 reflection pairs; independently recalculated signed multiplicity/eligibility; verified 13,427 actual selector lists, each with distinct increasing indices, by direct noncommutative multiplication; and checked four family instances p=5,7,11,13, including all240 family reflection-pair selectors and the stated earlier-certificate failures. It also rejected duplicate selector-index, reused pair-index, and false eligibility mutations for their intended reasons.

These local bounded checks are diagnostic, not a proof of the universal written argument, formal proof, human or configured-family review, novelty clearance, or resolution of the rest of the ordered Olson problem. The original R=3p−3 necessary residual in §2 and all other count bands remain open.

**END — signed-pair theorem, residual, explicit family, and actual check scope.**
