# A genuine high-surplus REF obstruction with an exact original selector

MathOlson-2-2. Native `/bin/date` before writing: **Wed Oct 28 22:14:07 PDT 2026**. WRITTEN all-prime family, with a finite head lemma checked by integers and independent saved-word diagnostics (§5). Pending fresh disjoint mathematical review; no novelty or full L_RES claim. Mandatory before-source: `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`.

**Caller boundary FIRST.** This family proves NONEMPTINESS only of the explicitly named count/zero-free/singleton/low-raw/REF-failure/SEL-failure base at o_π=p+4. The remaining OLD/IPGEN/GS/DS3 predicates have NOT been evaluated. Its two identity-four head blocks make historical grammar coverage a particular issue to check before any stronger membership claim. No new strict provider separation or full residual witness is asserted; it is SOLVED, never an Olson/L_RES counterexample.

## 1. Actual all-prime words

For any prime p>=7, any nonzero a,b in F_p, put Z=σ_0, T_k=σ_(ka), and L=2p−9. In the exact order shown, let

`H = Z T_(−1)^2 Z · T_1 T_2^2 T_1`,

`W = H · Z ρ_b Z^(L−1) ρ_b · T_(−1)ρ_b T_(−2)ρ_b ... T_(−(p−1))ρ_b`.

Both four-letter factors of H are identity, and every exponent denotes an ACTUAL occurrence count. The word has F=8+L+p−1=3p−2 reflections, R=2+p−1=p+1 rotations, N=4p−1. All rotations are nonzero and no cyclic reflection gap has more than one rotation. There is exactly one occupied equal-endpoint gap (inside the long Z-run); every other occupied gap has unequal endpoints.

## 2. Projection and literal raw graph

The reflection-only projection has cyclic runs

`Z, T_(−1)^2, Z, T_1, T_2^2, T_1, Z^L, T_(−1), T_(−2), ..., T_(−(p−1))`.

Adjacent labels differ for p>=7. Thus **o_π=p+4, e_π=2**, exactly the high-surplus stratum left by the current selector bands. Deleting the adjacent equal ODD-spare labels in the first two pairs (0,0) and (1,1) leaves the reverse affine AP `0,−a,−2a,...,−(p−1)a`. This realizes the affine-core alternative of the spare-cancellation reduction; that reduction never claimed its converse.

In the literal possible-switch graph, an edge occurs iff endpoint values differ or its actual gap is occupied. The missing edges inside the two squared head runs separate two paths of four vertices; the first occupied internal Z gap makes the second of those paths end at the SECOND long-run Z. The third nontrivial path has p+2 vertices, from the LAST long-run Z through all p−1 tail reflections and cyclically through the first two head reflections. Remaining 2p−12 vertices are isolates. Therefore

`η=p+7`,  `ν=2+2+floor((p+2)/2)=(p+9)/2`.

Hence ν<=p−3 exactly for primes p>=17. The actual rotation-separated block counts are **o_F=p+4,e_F=3**, not the projected e_π=2: splitting the long odd Z projection run after its first letter creates an odd block and an even block. Max reflection multiplicity is 2p−7, so the literal SEL hypothesis requiring 2p−1 equal reflections fails. No other caller equivalence is inferred.

## 3. Every reflection-only 2p selection fails

Normalize a=1 by the field automorphism (scaling reflection/rotation exponents); rotation letters are all skipped in this section. The eight head labels are

`h=(0,−1,−1,0,1,2,2,1)`.

If k head reflections are selected, their alternating exponent q has the following EXACT integer range endpoints (no modular reduction in this table):

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| min q | 0 | −1 | −3 | −2 | −2 | −1 | −1 | 0 | 0 |
| max q | 0 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 0 |

This finite eight-entry lemma can be checked by 256 subsets, or the exact recurrence `min_(i+1,k)=min(min_(i,k), min_(i,k−1)+(−1)^(k−1) h_(i+1))` and the analogous maximum recurrence; initialize min/max at k=0 to 0 and impossible other states. Both methods were independently executed (§5). In particular for every k,

`min q + ceil((9−k)/2)>=1`, `max q<=floor((9−k)/2)`.  (1)

Let z<=L zero reflections and t<=p−1 tail reflections be selected, so k+z+t=2p. Then `t>=2p−L−k=9−k>=1`. Write the selected tail indices as `1<=i_1<...<i_t<=p−1`; its labels are −i_1,...,−i_t. Since k+z has the same parity as t, the full product exponent is q+T, where

`T=(−1)^t (−i_1+i_2−i_3+...)`.

Pairing consecutive gaps gives the exact elementary bounds

`ceil(t/2)<=T<=p−1−floor(t/2)`.

For even t this is the sum of t/2 positive gaps; for odd t it is i_1 plus the remaining positive alternating gaps. Minimum gaps are 1; the endpoint range supplies the displayed upper bound. Combining with t>=9−k and (1) yields `1<=q+T<=p−1`. Thus the exponent is NONZERO mod p for EVERY original reflection-only selection of size2p. This is a complete all-prime proof of REF failure, not an inference from the finite prime diagnostics.

## 4. An actual original-index mixed identity

Select ALL EIGHT head occurrences (product1). Select the FIRST 2p−10 Z reflections of the long run, both rotations that bracket its final L−1-reflection portion, and nothing in the tail. There are `8+(2p−10)+2=2p` selected occurrences. After the first selected Z and ρ_b, there remain `2p−11` selected Z's, an ODD number. Thus this selected core product is `Zρ_b Zρ_b=1`. The whole original-order selector is identity. This is an explicit lift by actual contiguous identity head blocks with complete original cardinality, not merely a witness in a shortened word.

The family therefore refutes the easy idea that the high-surplus low-matching REF-failure BASE is empty, while explicitly solving itself. It does NOT refute L_RES or establish that all its retained caller failures hold.

## 5. Exact finite verification and limits

`frontier-20261028-olson-affine-core-surplus2-check.py`, SHA256 `a69b218901c51ee9ac90d11e27714850234a8f1ca13db8b04df6688bcfc94904`, produced `frontier-20261028-olson-affine-core-surplus2-check-results.json`, SHA256 `4960d9c627782ce004b13aa9e4f283eb26b79dd9f104cf47ce9537ff25efa92e`. At p=7,11,13,17,19,23,29 and a=b=1 it constructs the actual full words and selectors, checks counts/gaps/projection, computes the full REF 2p product support by an element DP, checks the exact raw matching by a cycle DP, and enumerates the 256 head subsets. Low matching holds only at the four primes >=17, as stated.

Separately written `frontier-20261028-olson-affine-core-surplus2-audit.py`, SHA256 `1252428b3252b27dcf142c06ad86b9c4938df0c44a284ab06f93e4e614f64f84`, imports none of that code. Its saved receipt `frontier-20261028-olson-affine-core-surplus2-audit-results.json`, SHA256 `8fff90cbf97d426c252aa2917c0922e5169a446b5228859156dc75aa8abc3094`, reconstructs the projection, re-decides REF failure by the independent run-parity/cardinality criterion, uses path components for matching, multiplies original products using affine-map composition, and checks the head table via min/max recurrence. Duplicate selection and changed selected rotation controls fail for their intended reasons. This is same-model independent implementation evidence, not an external-family/human/formal review, full residual classification or novelty clearance.

**END — high-surplus REF-failing BASE family with explicit original identity.**
