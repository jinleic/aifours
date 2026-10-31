# Ordered dihedral selector — exact two-reflection prefix potential and sharp coverage criterion

Owner **MathOlson-2-2**, original math-2 slot.
Actual native `/bin/date` before this write: **Wed Oct 28 17:10:51 PDT 2026**.
**NEW written WORD-CLASS candidate with independently replayed exact finite checks. Not a proof of the full ordered Olson conjecture or a novelty claim.**

## 1. Target and precise class

Let p be ANY odd prime and

`D_(2p)=<r,s | r^p=s^2=1, srs=r^−1>`.

Its order is2p. The original problem for this group asks for an identity product of EXACTLY2p actual occurrences, in increasing ORIGINAL order, in EVERY word of length4p−1.

Fix ANY such actual word with R rotations and F reflections, `R+F=4p−1`, in the full range

`2p−2 ≤ R ≤ 3p−2`, hence `F≥p+1`.

Choose ANY actual subset I of exactly2p−2 rotation occurrences. Write its rotation exponents x_a∈F_p and put

`S_I=∑_(a∈I) x_a`.

For each actual reflection occurrence i, write it uniquely as `r^(y_i)s`, and define its I-dependent prefix potential

`z_i^I = y_i + 2 ∑_(a∈I, a<i) x_a` in F_p.                     (1)

All sums are over ACTUAL chosen original rotation positions; unchosen rotations are ignored. Reflection indices retain their original order.

**Theorem A — exact two-reflection caller.** For i<j, the chronological product of the SAME rotation set I and these two reflection occurrences is

`r^( S_I + z_i^I − z_j^I )`.                                    (2)

Consequently that set of EXACTLY2p actual indices is an original-order identity selector IFF

`z_j^I − z_i^I = S_I`.                                         (3)

**Theorem B — two explicit sufficient word conditions.** The fixed I has such a selector whenever EITHER:

1. `S_I=0`; or
2. `S_I≠0` and the set of its reflection potentials `{z_i^I}` is ALL F_p.

The statements hold for EVERY p, every original type order, every actual exponent, repeated value and zero rotation in the stated count band. Neither condition is assumed true for every word.

This is a substantive original-object selector for a proper word class in an intermediate rotation band, not an all-word or all-group solution. It does not depend on an old held certificate or assume chronological packet flattening.

## 2. Complete proof of the actual chronological product identity

The group law in these coordinates is

`(x,e)(y,f)=(x+(-1)^e y,e+f mod2)`,

where `(x,0)=r^x` and `(y,1)=r^y s`.
With the two selected reflections i<j, let A, B, C be the sums of the selected rotation exponents BEFORE i, strictly BETWEEN i and j, and AFTER j, respectively.
The selected original product, without any reordering, is

`r^A (r^(y_i)s) r^B (r^(y_j)s) r^C`
`= r^(A+y_i−B−y_j+C)`.

The first reflection reverses the middle rotations, and the second restores the sign. Since `S_I=A+B+C`, the exponent is

`S_I+y_i−y_j−2B`.

The two actual prefix sums are `P_i=A` and `P_j=A+B`, so

`z_i^I−z_j^I=y_i−y_j−2B`.

This proves (2), and an r-power is identity exactly when its exponent is0 modulo p, giving the iff (3).
The selected positions are exactly the fixed2p−2 distinct rotation positions plus the two distinct reflection positions; no exponent is a formal proxy for an unselected occurrence. Empty before/between/after segments and arbitrary repeats are covered automatically.

## 3. Proof of the two sufficient conditions

If `S_I=0`, F≥p+1 actual reflections carry only p possible potential values. Two ordered occurrences i<j have the same z by pigeonhole. Equation (3) holds and the actual selector follows.

Suppose `S_I≠0` and every residue appears as a potential.
Consider the directed cycle `v→v+S_I` on F_p; it is a single p-cycle because p is prime and S_I nonzero.
If no increasing reflection pair i<j satisfied (3), then for EVERY v every occurrence with potential v+S_I would precede every occurrence with potential v.
Since every residue appears, these strict order relations around the entire directed cycle would force one occurrence to precede itself, impossible.
Thus some i<j satisfies (3), and (2) gives the original identity selector.
This is an orientation-sensitive argument: a mere unordered difference set is not substituted for the required order.

For the edge case R=3p−2 there are exactly p+1 reflection occurrences, still enough for the zero-sum pigeonhole. At the lower edge R=2p−2 the I-set is forced to be ALL rotations. The theorem assumes neither edges nor nonzero rotation values in general.

## 4. Sharpness of the FULL-support condition as a support-only guarantee

Fix ANY nonzero δ∈F_p and ANY nonempty PROPER set T⊊F_p.
The directed graph on T with edges `v→v+δ` is a disjoint union of directed paths: it is obtained from the directed p-cycle by removing at least one vertex.
Order the values in reverse topological order, and group arbitrarily many repetitions of each value at its position in that order.
Then there is NO earlier/later pair with difference δ, no matter how large the total number of reflection occurrences is.

This potential word can be realized by actual D_(2p) occurrences: choose2p−2 actual rotations with total exponent δ, retain any fixed placement I, and set each reflection exponent to `y_i=z_i−2P_i` using the actual selected-rotation prefix P_i.
Additional unselected rotations can have arbitrary exponents. Thus a proper potential support, even of size p−1 and with F≥p+1, does NOT by itself force condition (3) when S_I=δ≠0.

This proves only the sharpness of **support-only sufficiency for this fixed-I/two-reflection construction**. It does NOT show that such a word lacks another I, another reflection count, or an original2p-selector. No avoiding word or global no-go follows.

The exact criterion remains (3): full support is sufficient, not necessary. For a particular potential sequence, an ordered pair can exist with a proper support; conversely an unordered pair difference without the correct orientation need not suffice.

## 5. An all-prime alternating family outside the separated-packet class

For EVERY odd prime p construct an actual word with

- `F=2p` reflections and `R=2p−1` rotations;
- strictly alternating quotient types, beginning and ending with a reflection;
- every rotation equal to r (exponent1).

Index reflections by j=0,…,2p−1 and choose I as the FIRST2p−2 actual rotations. The number of selected rotations before reflection j is

`min(j,2p−2)`.

Set its ACTUAL reflection exponent to

`y_j = j − 2 min(j,2p−2) mod p`.

Then `z_j^I=j mod p`, so the reflection potentials cover ALL F_p, while

`S_I=2p−2≡−2 mod p ≠0`.

Taking i=0 and j=p−2 gives `z_j−z_i=p−2≡−2=S_I`; their actual two reflections together with I therefore form an original-order identity selection of EXACTLY2p occurrences by (2).

The quotient pattern has4p−1 singleton runs, so it is outside the previously proved saturated separated-pair word class. This is an explicit family on which the new potential criterion applies beyond that specific certificate; it does NOT demonstrate that every alternating word, or every word in the count band, is solved.
The construction is an all-prime proof, not an assertion of novelty or a selected numerical proof of the general theorem.

## 6. Reproducible bounded actual-word experiment

The following NEW scripts use only standard-library exact integer modular arithmetic; the checker imports NO producer code:

| Artifact | SHA256 | Purpose |
|---|---|---|
| `frontier-20261028-dihedral-two-reflections-experiment.py` | `1fca69346c5780109270c263b5a74a6a26f48755119a76e739c9a3f268127bc8` | Produce bounded actual original D_(2p) words and selected indices |
| `frontier-20261028-dihedral-two-reflections-checker.py` | `8915b015ae97e9f3435bd23d4cdbcffa95a5a0d8f9f50b7089d77478df93e19f` | Independent seed replay, all-pair direct group multiplication and mutation controls |
| `frontier-20261028-dihedral-two-reflections-results.json` | `877ac388279b361d0250e3b53b130bd57befbb34d6a2a6e105b9e78f8b5e6e67` | Saved actual examples, deterministic seed and counts |

The bounded run used p=3,5,7 and EVERY R in the theorem's stated range, with80 seed-reproducible random actual words for each (p,R): **1,440** random full original words in total, seed2026102802.
The producer reported **700** words satisfying Theorem B's sufficient condition and finding actual selectors. It also found a working two-reflection pair in **718** further sampled words outside that sufficient condition; this illustrates that the criterion is not necessary. The remaining sampled words are not called avoiding words.

The separate checker replayed all1,440 words from the recorded seed and **directly checked all60,480 reflection-pair original-order products**, not only the displayed selected pairs. For EVERY such pair it compared direct group multiplication against formula (2). It also validated all18 saved domain representatives and the p=3,5,7 instances of the alternating family.
Its output was `PASS_BOUNDED_REPLAY_AND_DIRECT_PRODUCTS`; duplicate selected indices, a false saved product and a wrong word hash were all rejected for their intended reasons.

One saved p=5 alternating word has SHA256 `6bb5e74ef93cd5b72b81ab2f3fe7bd336b3101ef99531f448926e6a05c6238c3`. In zero-based original indexing the checker verified the actual selection

`0,1,3,5,6,7,9,11,13,15`,

of size10, with direct product `(0,0)` (identity). The full19-occurrence word and every claimed exponent/position are in the pinned results. This checked instance does not replace the symbolic all-p proof.

## 7. Scope, prior and remaining gap

The theorem's assumptions are sufficient conditions on an ACTUAL fixed rotation subset, not an assertion that every word admits one. With an insufficient potential support or no appropriate directed difference, this construction makes no claim.
The all-finite-group original question, the general odd-prime dihedral residual and all remaining count bands are not solved here. No actual avoiding word is claimed.
The original ordered-group source, parent-adopted valid transport and public prior distinctions remain as separately documented; no historical HELD outcome is treated as verified by this new work.

The standalone finite program/checker runs establish only the reported finite replay and mutation results. No formal/kernel/human/cross-family review, priority/novelty clearance or stronger finite-witness certification is inferred.
The latest owner direction permits these bounded local scientific checks; no external model/paid API, secret, Git push, deletion, publication or infrastructure mutation was used.

**END — exact actual two-reflection selector and sharp potential-support boundary.**
