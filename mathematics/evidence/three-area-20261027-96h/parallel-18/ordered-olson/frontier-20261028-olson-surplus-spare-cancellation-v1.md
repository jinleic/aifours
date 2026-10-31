# Surplus-spare cancellation: a projection-only REF reduction

Owner MathOlson-2-2. NEW WRITTEN candidate, not independently reviewed. Native clock will be pinned separately after this source. Mandatory before-source: `frontier-20261028-olson-actual-block-fatal-correction-v1.json` (SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`). All runs here are reflection-only PROJECTION runs. No old f111 adoption, actual-block floor, packet-lift or nonzero-rotation assumption is imported.

## 1. Actual original-index reservoirs

Let an actual word have F=3p−2 reflections, p odd prime, and `o_π=p+2j`, j>=1. Rotations may be arbitrary; this source selects NONE. Choose the LAST reflection of each odd projected run as its spare, and pair the other reflections of each run consecutively from its start. This gives

`P=(F−o_π)/2=p−1−j`

actual equal-reflection pairs, disjoint from the `n=p+2j` spares in cyclic run order. Call their label sequence z. All rotations and unselected reflections are skipped. The product of any selected reflections is therefore evaluated in its actual cyclic reflection order, never in a changed word.

Perform any sequence of operations on z: delete two currently cyclically adjacent equal labels, recording their two ORIGINAL spare indices. Stop when there are no such neighbors. Let k be the number of deleted pairs and v the surviving cyclic sequence, of length n−2k. This is an index-combinatorial device, NOT a claim that a witness from a shortened word alone lifts to the target.

**Extension lemma.** Any selected subset of surviving spares whose cyclic product is IDENTITY may be augmented by ANY subset of the recorded deleted pairs and still has identity product; the selected count increases by twice the number added. Reinsert the chosen pairs in reverse deletion order. At a pair's deletion, choose the cyclic open arc between its two members that contains no then-surviving spare. At reverse insertion that arc contains no selected surviving or later-deleted spare; any chosen earlier-deleted pairs eventually inserted inside it are nested identity subproducts. The equal endpoints therefore cancel in a cyclic cut at the arc; if the pair straddles the original cut, this operation conjugates the old product rather than preserving an arbitrary nonidentity value, but identity is preserved. Alternating/interleaved chords cannot arise from these deletions. The P fixed pairs may also be inserted freely: their members are consecutive within a constant reflection run with no spare between them. Thus any chosen reservoir subset extends an IDENTITY surviving-spare selection to an identity selection on actual occurrences. Sorting back into original order only cyclically rotates an identity product.

## 2. Exact necessary alternatives under REF failure

If W has NO reflection-only identity selection of exactly2p, then for EVERY completed deletion sequence:

(A) `k<=j−2` and the surviving adjacent-distinct sequence has length at least p+4; OR

(B) `k=j` and its p surviving labels are an affine arithmetic progression listing every field value once.

There is NO k=j−1 alternative. In particular, a reduction reaching length p+2 is already a constructive REF certificate, and a reduction deleting at least j+1 pairs is also such a certificate.

**Proof.**

* k>=j+1: take j+1 deleted pairs and all P fixed pairs. They are exactly `2(j+1)+2(p−1−j)=2p` reflections with identity product by the extension lemma.
* k=j−1: the completed surviving sequence has length p+2 and adjacent-distinct labels. Section 3 proves a zero alternating quadruple exists. Select its four original spares and all `P+k=p−2` available identity pairs; the extension lemma gives exactly2p actual reflections with identity product.
* k=j: the survivors have length p. If two surviving labels agree, their two original spares plus all `P+k=p−1` identity pairs give exactly2p reflections. Hence all p labels are distinct, comprising F_p. If four surviving labels have alternating sum zero, take those four and any p−2 reservoir pairs. Thus no such quadruple exists. For every consecutive triple `a,b,c` in a linear cut, `t=a−b+c` occurs in the survivor list; an occurrence outside the triple would give a zero quadruple. Since a!=b and b!=c, t is neither a nor c, so it is b. Hence consecutive differences are a common nonzero d. The p survivor labels are an affine AP. This argument also holds for p=3, where any field permutation is an affine AP.

These cases leave exactly (A) and (B). The conclusion in (B) is NECESSARY only: even projected runs and alternative actual selections can still establish REF, and no converse is claimed.

## 3. Complete adjacent-distinct p+2 auxiliary proof

For completeness, the field-sequence lemma is re-proved here, not imported as an accepted verdict from any source. Let z be a linearly adjacent-distinct length-(p+2) list with no alternating-zero quadruple. Four equal values immediately contradict this. If a occurs three times and b twice, the interval between the b occurrences has three regions (before/inside/after); two a's in one region give disjoint or nested equal pairs, hence a zero quadruple; if one a lies in each region, the outer a's and both b's do so. Thus a triple value, if present, is the only repeated value, giving FULL support F_p. For a full-support adjacent-distinct list, each consecutive triple a,b,c has t=a−b+c somewhere. No occurrence can be outside that triple; t is neither endpoint, so t=b. The list is a nonzero-step AP and positions 1,2,3,p+2 have alternating sum −pd=0: contradiction.

Otherwise every value occurs at most twice. Let s be the number of doubled values; support p+2−s<=p gives s>=2. Any two doubled values a,b must cross in occurrence order, else disjoint/nested equal pairs give zero. Fix doubled a and any other doubled b. In the crossing order `a1<b1<a2<b2` (or its cyclic rotation) put x=2a−b. An occurrence of x before a1, between a1 and a2, or after a2 gives respectively `x,a1,b1,a2`, `a1,x,a2,b2`, or `a1,b1,a2,x`, each with alternating sum zero. The reversed crossing orientation gives the same three-region conclusion after rotating the selected quadruple. Thus every x=2a−b is absent. There are s−1 distinct such values but only s−2 missing values: contradiction. QED.

## 4. A strict equality-adjacency obstruction at j=2

Let α(z) be the number of cyclic adjacent equal pairs in a label list of length at least5. Deleting neighboring a,a, with neighbors u,v, changes α by

`α_before−α_after = 1+[u=a]+[v=a]−[u=v] >=0`.

A length-(p+2) cyclic list with no zero quadruple has α>=2: if α<=1, cut at its only equality (or anywhere if none), obtain a linearly adjacent-distinct list, and apply §3. Therefore a j=2 REF-failing spare list of length p+4 CANNOT have α=1. Indeed deleting its unique adjacent equal pair would produce a length-(p+2) list with no zero quadruple (a zero quadruple there plus that pair and P=p−3 fixed pairs would select2p). Its α would still be at most1, contradiction. Hence j=2 REF failure requires α=0 or α>=2. This does not eliminate the α=0 adjacent-distinct case.

An equal adjacency between consecutive ODD-run labels requires at least one EVEN projected run in that intervening arc; distinct arcs have disjoint even runs. Hence α<=e_π. Combining with the already stated low-raw frontier condition `o_π+e_π+g_int<=2p−6`, at p=11 the still-open j=2 cases have e_π<=1 and therefore necessarily α=0. This is not a proof that these adjacent-distinct length15 lists cannot fail REF. It isolates that missing all-variable claim; no enumeration or numerical assertion is substituted for it.

## 5. Status and genuine remaining gap

This source is a complete written reduction and constructive certificate scheme in its stated cases, not a general classification of higher surplus. The unsolved structural claim would be: for every odd prime p and j>=2, every cyclic adjacent-distinct length-(p+2j) list in F_p has a zero alternating subsequence of even length at least2j+2. It is NOT proved here. Even its proof would still need an actual rotation-assisted selector for the remaining affine-core expansion class (B); a reflection-only obstruction is not an Olson counterexample. No full L_RES/caller-failure/novelty/formal result is claimed. No new scientific computation was used in this manuscript.

**END — original-index cancellation certificates and the exact surviving obstruction.**
