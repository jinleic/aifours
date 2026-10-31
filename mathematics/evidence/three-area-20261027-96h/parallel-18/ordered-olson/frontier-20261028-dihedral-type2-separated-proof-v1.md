# Two separated low pairs for the two-sign type-II subclass

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:37:01 PDT 2026**. A self-contained **WRITTEN proof candidate** with exact bounded checks in §6; no independent mathematical review, formal proof, novelty or global-adoption verdict.

## 1. Exact theorem

Let p be ANY odd prime and `a∈F_p` nonzero. Let W be an ACTUAL ordered word of length `4p−1` in `D_(2p)` whose rotations consist of exactly `2p−2` copies of `r^a` and `p−2` copies of `r^(−a)`, in arbitrary positions and order. Its other `p+3` occurrences are arbitrary reflections `r^y s`. Then W has an original-order identity subsequence of exactly2p occurrences.

Only this R=3p−4 two-sign multiplicity subclass is claimed. The type-III, all-high and other-count-band manuscripts are not mathematical inputs. No L_RES, full count-band, original Olson, novelty or formal claim is made.

For a reflection i write Q_i for the INTEGER number of `r^a` rotations before i minus the number of `r^(−a)` rotations before i. For i<j call (i,j) **low** when

`0 <= Q_j−Q_i <= p`.  (1)

## 2. Two chronologically separated low pairs always exist

**Lemma.** There are actual reflection positions `i<j<k<l` such that both (i,j) and (k,l) are low.

*Proof.* Suppose not. View each low pair as the closed interval of reflection ordinals from its first endpoint to its second. If two such intervals were disjoint, their pairs would be chronologically separated. Thus all low intervals intersect pairwise. For intervals on a line this implies a common point: the largest left endpoint is at most the smallest right endpoint. Choose their common point to be an integer reflection ordinal t. If the low-edge family is empty, choose any t.

No low pair can have both endpoints strictly before t, nor both endpoints strictly after t. Let L_left,L_right be the numbers of reflection occurrences strictly before and strictly after t. Since the total is p+3, `L_left+L_right=p+2`. The number of gaps between CONSECUTIVE reflections within these two sides is

`max(L_left−1,0)+max(L_right−1,0) >= p`.

Each such gap is NOT low. Its INTEGER prefix increment is therefore either <=−1, requiring at least one actual `r^(−a)` rotation, or >=p+1, requiring at least p+1 actual `r^a` rotations. These side-internal gaps are disjoint. There are only p−2 raw −a rotations, and at most one gap can contain p+1 raw a rotations because there are only `2p−2<2(p+1)` a rotations in the whole word. Thus there are at most `(p−2)+1=p−1` such gaps, contradicting the lower bound p. QED.

The common interval point may be a shared reflection endpoint; the proof does not incorrectly treat overlapping pairs as selectable disjoint pairs.

## 3. What no two-reflection selector forces on a low pair

Fix any actual low pair i<j and put `u=Q_j−Q_i`. The signed rotation multiset for this pair has

`2p−2−u` occurrences of +a and `p−2+u` occurrences of −a.

Both counts are at least p−2 by (1). Omitting p−2 actual rotations produces all omission sums except 0: choosing q signed −a occurrences and p−2−q signed +a occurrences for q=0,...,p−2 gives p−1 distinct residues, and the formal q=p−1 value is 0. Let T_ij be the sum of ALL signed rotation exponents. Therefore the selected `2p−2`-rotation sums are exactly `F_p\{T_ij}`.

The actual product with reflections i<j has exponent `selected signed sum + y_i−y_j`. It is identity unless the actual target `y_j−y_i` is the unique missing value T_ij.

The raw total of all rotation exponents is `(2p−2−(p−2))a = p a = 0`. Thus `T_ij = −2a(Q_j−Q_i)`. Under a hypothetical no-selector assumption, every low pair satisfies

`y_j−y_i = −2a(Q_j−Q_i)`.  (2)

Equivalently the two endpoints have the same value of `y+2aQ`. The proof does not assume all reflections have this value, nor even that the low-edge graph is connected.

## 4. Four actual reflections and a zero-sum omission

By §2 choose two separated low pairs `i<j<k<l`, with prefix increments `u_1=Q_j−Q_i`, `u_2=Q_l−Q_k`. Select those four actual reflections. For now consider ALL R=3p−4 actual rotations, with signs determined by the parity of selected reflections before each rotation. The signs are negative precisely in the disjoint intervals (i,j) and (k,l). Their signed exponent sum is

`T_0−2a(u_1+u_2) = −2a(u_1+u_2)`.

By (2), the four-reflection exponent contribution is

`y_i−y_j+y_k−y_l = 2a(u_1+u_2)`.

Hence the product of these four reflections and ALL actual rotations is identity. That oversized selection is used only as an algebraic total, NOT offered as the required witness.

Every signed rotation has value +a or −a. Since `R=3p−4>=2p−1`, one of these values occurs at least p times. OMIT any p actual rotations of that SAME signed value. Their signed sum is ±p a=0, so the actual ordered product is unchanged. The remaining rotations number `R−p=2p−4`; together with the four distinct chosen reflections they give EXACTLY2p original occurrences, with identity product. This contradicts no-selector and proves §1.

The argument does not move rotations or replace an original index set by a shortened-word witness. It uses the actual signs for the FOUR selected reflections, not two incompatible pair-specific sign conventions.

## 5. Complementary scope

The two low edges need not share a connected component; their chronological intervals must be disjoint. Equality (2) holds separately on each edge. If even one low edge's target differs from T_ij, an actual two-reflection selector already exists, so §4 is needed only in the other case. This proof does not claim every such word requires four reflections or that type-I/type-III multiplicities follow.

## 6. Actual bounded verification

`frontier-20261028-dihedral-type2-separated-experiment.py`, SHA256 `043244dc6cf63ba043943608026c547adccf62f1b3b1dd45d68a121b93d0cf72`, generated 800 actual original words at p=3,5,7,11,13. Half have arbitrary seeded reflection exponents; half deliberately use the global gauge `y_i=−2Q_i` to make every low-pair target missing and exercise the four-reflection branch. Saved `frontier-20261028-dihedral-type2-separated-results.json` has SHA256 `c3cf0b1e7fa84be13318a637e385822298ef87412e8b62b16f2b90df2051eace`.

Separately written `frontier-20261028-dihedral-type2-separated-checker.py`, SHA256 `f044341b0d9375e56484b719de6e758dd05a8a3a8c9bd9de2a9b454144cdb117`, imported no producer code and returned `PASS_INDEPENDENT_TYPE2_SEPARATED_CHECK`; result `frontier-20261028-dihedral-type2-separated-check-results.json` SHA256 `70dd39c95098c8b565d2abf14c76bbaa7846b04415b83fdcb41c4e00cfd14fbc`. It reconstructed the actual raw counts, integer low edges, separated pair positions, gauge equalities, four-reflection signed total, p actual same-signed omissions and original complement; it directly multiplied all800 distinct-index original selectors. Observed branches: 400 gauge/four-reflection, 399 random/two-reflection and one random/four-reflection. Duplicate-index, overlapping-pair and duplicate-omission mutations were rejected for their intended reasons.

These checks are not a proof of the all-prime interval lemma or a formal/cross-model review. A complete disjoint written review is requested.

**END — type-II all-prime written candidate and exact evidence.**
