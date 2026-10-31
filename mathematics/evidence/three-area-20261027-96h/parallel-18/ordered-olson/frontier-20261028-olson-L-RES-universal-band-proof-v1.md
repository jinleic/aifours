# L_RES by an original-order two-rotation selector: complete written candidate

Owner **MathOlson-2-2**, math-2. Native `/bin/date` before this write: **Wed Oct 28 22:31:26 PDT 2026**. Status **WRITTEN candidate with bounded independently implemented local checks**, not an adopted result, disjoint scientific review, formal/kernel proof or novelty claim. A NEW full-source disjoint review is required before parent adoption.

**Before-source history:** read `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. The earlier f111 adoption and its actual-block/projection lift remain withdrawn. This proof uses NO historical o_F/e_F floor or identification, no one-endpoint maximum-matching packet lift, no old review verdict, no old GEN/IPGEN/GS/DS3 implication, and no result from the previously submitted o_π<=p or p+2 bands. Prior exposure to those candidate/control sources is disclosed, not called blind. The transport identity previously appeared in this owner's 20261023 `proof-MAXIMAL-REFLECTION-TRANSPORT-CONTROLS-v1.md`; all needed algebra is proved here, with no transfer of its verdict or its false MI2 completion.

## 1. Exact theorem and original task

**Theorem U.** Let p be any odd prime. In `D_(2p)`, every ACTUAL word containing exactly F=3p−2 reflections and at least R=p+1 rotations has an identity subsequence of exactly2p actual positions in increasing ORIGINAL order. If no reflection-only selector exists, a selector exists using exactly TWO rotations and 2p−2 reflections.

Rotation exponents may be zero. Rotations may be consecutive; no singleton-gap, matching, alphabet or caller hypothesis is imposed. For R=p+1 the word length is exactly4p−1. This is only that reflection/rotation count band, not the original all-group ordered Olson conjecture or all dihedral count bands.

The literal L_RES target in the original 20261023 `selection-lower-matching-packet-lift-v1.md:11–21,53–59` retains p>=7, F=3p−2, R=p+1, zero-free rotations, singleton gaps, raw matching<=p−3, and EVERY applicable OLD/REF/SEL/IPGEN/GS/DS3 failure. All of these are a SUBCLASS of Theorem U. Thus, if the present complete written proof survives independent review, it supplies the separately proved ACTUAL selector alternative of L_RES for the ENTIRE original residual; no certificate-family equivalence is asserted.

## 2. Algebra and actual-index transport

Write rotations `ρ_a=(a,0)`, reflections `σ_a=(a,1)` with

`(a,e)(b,f)=(a+(−1)^e b,e+f mod2)`.

Thus `σ_aσ_b=ρ_(a−b)`; conjugating σ_b by `(a,e)` gives `σ_(2a+(−1)^e b)`; conjugating ρ_b gives `ρ_((−1)^e b)`. All coordinates are in F_p.

Let S be an actual selected subset with product1, and P_i the product of its selected letters strictly before an optional occurrence h_i. Define `τ_i=P_i h_i P_i^−1`. Exact telescoping, in increasing ORIGINAL order, gives

`product(S ∪ T) = (product_(i∈T in order) τ_i) · product(S) = product_(i∈T in order) τ_i`.  (T)

This formula follows by inserting each `P_i^−1P_i` between successive actual stretches; it never commutes a raw occurrence or treats a conjugated value as an actual letter. A cyclic rotation of an identity product stays identity (`AB=1 ⇒ BA=1`). We may therefore choose convenient cyclic cuts, but final selectors are the same actual original indices.

Two consequences for reflection-only identity S:

* **Add:** two optional reflections with equal transported involutions extend S by exactly2 and preserve identity, by (T).
* **Erase:** two selected reflections with equal transported involutions can be removed while preserving identity. Indeed, write S's selected product as `A h B k C=1`; equality `A h A^−1=A h B k B^−1 h A^−1` gives `B k B^−1=h`, so the old product is `A h h B C=A B C`, exactly the product after removing h,k. Consequently any reflection identity of length L>p can be shortened by2 (there are only p transported involutions). In particular an identity of even length L>2p can be shortened to EXACTLY2p.

## 3. Maximal-identity rigidity for an adjacent-distinct cyclic reflection list

**Lemma A.** Let `1<=h<=p−1`. Any cyclic reflection list of length n=p+2h whose CYCLICALLY adjacent exponents differ has an identity subsequence of even length at least2h+2.

*Proof.* Suppose not, and choose a reflection identity S of maximum even size. Then `|S|<=2h`; if more than p reflections were outside S, two optional transported involutions would agree and the Add operation would enlarge S. Thus `|S|=2h` and exactly p reflections remain outside S. Call those occurrences the **anchors** for this lemma.

Their transported reflections, in cyclic occurrence order, are product-one-free: any nonempty identity subsequence of them would enlarge S by (T). In particular their labels are distinct (else two suffice), hence all of F_p; and they have no alternating-zero quadruple. For each consecutive triple a,b,c of anchor labels in a linear cut, `t=a−b+c` occurs among the anchors. An occurrence outside the triple gives a zero quadruple. Adjacent labels differ, so t is neither endpoint, hence t=b; therefore successive differences are a common nonzero d. The anchors form the CYCLIC AP `a,a+d,...,a+(p−1)d`. For p=3 this argument also works: every field permutation is such an AP.

For each selected reflection s∈S, let c be its transported label. There is a unique anchor r of label c. Replacing s in S by r is another identity S' of the SAME size. To see it directly, if r precedes s write `S=A B s C`; equality of transports says `r=B s B^−1`, and `A r B C=A B s C=1`. The reverse order gives the same identity by the reverse algebra. After this swap, the p complementary transported labels must again be distinct, otherwise Add enlarges S'.

Orient cyclically from r to s. If the open arc contains k anchors, they have labels `c+d,...,c+kd`, with `0<=k<=p−1`. Their new transports are conjugated by σ_c, i.e. reflected by `x↦2c−x`; all other complementary anchor transports are unchanged, and the new complementary occurrence at old s has label c. If `1<=k<=p−2`, the anchor c+d becomes c−d, DUPLICATING the unchanged anchor c−d outside the arc. Contradiction. Hence k=0 or p−1. So every selected reflection in the gap between neighboring anchors of labels a,b=a+d has transported label in `{a,b}`.

Now use the assumption that EVERY neighboring pair of raw reflection exponents in the original cyclic list differs. In a nonempty gap, the first selected transported label must be b (not a), the last must be a (not b), and successive selected transported labels must differ. Indeed for consecutive selected raw reflections x,y, their transported labels coincide iff x=y: their prefixes differ by σ_x, which fixes its own axis. The same equality criterion applies at an anchor/selected boundary. Thus the selected labels in a gap alternate `b,a,b,a,...,b,a`, and the gap contains an EVEN number 2q of selected reflections.

Cut at an anchor. The selected prefix parity is now even at every anchor, as every anchor gap has even size. In a gap with transported endpoints a,a+d and 2q selected letters, the conjugation formula in §2 gives a common raw exponent increment d between EVERY consecutive original letter, from the left anchor through those 2q letters to the right anchor. More explicitly: if the selected prefix at the left anchor is `(A,0)`, its raw label is a−2A; the following raw labels are `a−2A+d, a−2A+2d,...,a−2A+(2q+1)d`. This follows successively from the transported labels b,a,b,a and the sign flip at each selected reflection. The same formula applies at the cyclic closing gap because product(S)=1. Hence all n cyclic raw increments equal d, forcing `n d=0`.

But `n=p+2h`, d!=0 and `1<=h<=p−1`, so `n d=2h d!=0` in F_p. Contradiction. QED.

## 4. Complete REF-failure normal form, with original-index lift

**Lemma N.** A reflection list of length F=3p−2 with NO identity selector of exactly2p cyclically reduces, by neighboring equal-reflection pair deletions, to exactly p surviving actual reflections whose labels form a nonzero-step cyclic affine AP. There are exactly p−1 recorded deleted equal pairs. Each recorded pair lies wholly in ONE gap between the p surviving anchors, and the deleted reflection word in each such gap has product1.

*Proof.* Perform any cyclic adjacent-equal deletions until the surviving list v has adjacent-distinct exponents; record both ORIGINAL indices of each pair, and let k be the number deleted. These chords are noncrossing: at deletion the chosen open arc contains no surviving letter; no final anchor lies in that arc. Any chosen subset of recorded pairs forms an identity reservoir relative to an identity selection of final survivors. Prove this by reverse insertion: nested equal endpoints enclose only already-cancelling pairs, so they cancel. Across the original cut the operation may conjugate a nonidentity product, but it PRESERVES IDENTITY, which is all we use. It also preserves exact counts by adding2 per pair.

If k>=p, choose p recorded pairs, giving2p identity reflections. Otherwise k<=p−1 and `|v|=3p−2−2k>=p`. If |v|>p, write `|v|=p+2h`, where `h=p−1−k∈[1,p−1]`. Lemma A supplies an identity subsequence of even length L>=2h+2=2p−2k in v. If L>2p, Erase in §2 shortens it to2p, already a contradiction. If L<=2p, augment by p−L/2 recorded pairs, available because `L>=2p−2k`. This yields EXACTLY2p actual original reflections. Hence |v|=p and k=p−1.

If two surviving labels agree, take them and all p−1 deleted pairs; if four have alternating sum0, take those four and p−2 deleted pairs. Both give exact2p identities. Thus survivor labels are a permutation of F_p with no zero quadruple, hence an affine AP by the triple argument in §3. Each pair's empty surviving arc is contained in one anchor gap. Its gap's pairs are a complete noncrossing matching of all deleted reflections there, so that gap word has product1; omitting ANY recorded pair preserves that gap identity by the same nesting argument. QED.

This is a NECESSARY REF-failure structure only, not an inverse iff. In particular a word freely reducing to an AP can still be REF-covered by another selection.

## 5. One pair may be dropped without sacrificing the AP controls

Assume no REF selector exists and take the p anchors and p−1 pairs of Lemma N. Let S be ALL 2p−2 paired reflection occurrences; product(S)=1. In a cyclic cut at an anchor, every anchor has identity S-prefix, so its transported label is its actual AP label. For each actual rotation r of exponent b_r put

`A_r=(−1)^(number of S reflections before r) b_r`.

If two A-values sum to0, (T) with those two rotations gives an original-order identity selection of exactly2p. Henceforth suppose no such pair exists.

Fix ANY ONE recorded equal pair E and let `S_E=S∖E`, of size2p−4. Every anchor gap still has reflection product1 (§4), so all anchor transports remain the same cyclic AP when cut at an anchor. Write χ_E(r)=1 if r lies in the open interval between E's endpoints inside its anchor gap, and 0 otherwise. Removing E flips the transported rotation exponent precisely there:

`A'_r=(−1)^χ_E(r) A_r`.  (1)

No assertion that this flip commutes physical letters is needed; it is just the parity of the removed prefix letters in (T).

If a different cyclic cut is used (e.g. before a chosen rotation), ALL transported anchors undergo a common conjugation, hence a common affine map `x↦ε x+c`, ε∈{±1}, and ALL transported rotations undergo the same global sign ε. Thus AP and zero/nonzero sum/difference conditions are preserved; literal numerical axes need not be unchanged under a change of cut.

### 5.1 Same-anchor-gap completion

Let r,s lie in the SAME anchor gap, and suppose `A'_r+A'_s!=0`. Orient the cut so no anchor lies strictly between r and s. All p anchors follow s, with transported labels a permutation of F_p. For each t!=0, any linear ordering of F_p has two labels x before y with x−y=t: otherwise position(x−t)<position(x) for all x, impossible around the additive t-cycle. Choose `x−y=−(A'_r+A'_s)` (using the corresponding common-sign conjugated values in this cut). By (T), S_E plus the two actual rotations and these two ACTUAL anchors has optional transported product

`ρ_(A'_r)ρ_(A'_s)σ_xσ_y=1`.

It has `(2p−4)+2+2=2p` original occurrences.

### 5.2 Different-anchor-gap completion

Let r,s lie in DIFFERENT anchor gaps, and suppose `A'_r−A'_s!=0`. Cut before r. There are m anchors, 1<=m<=p−1, between r,s and p−m after s. Their transported labels are consecutive complementary arcs of one cyclic AP. The set of differences x−y with x in the first arc and y in the second is ALL F_p∖{0}: normalize to first arc `c+d,...,c+md`, second `c+(m+1)d,...,c+pd`; the positive integers `m+j−i` range over EVERY 1,...,p−1 for `1<=i<=m`, `1<=j<=p−m`.

Choose `x−y=A'_s−A'_r` (again in the common conjugated cut coordinates). (T) gives

`ρ_(A'_r)σ_xρ_(A'_s)σ_y=ρ_(A'_r+x−A'_s−y)=1`.

The same original2p cardinality holds. This uses the ACTUAL one-anchor-on-each-side order, not a reorderable set sum.

## 6. The p+1 rotations force one of these completions

Suppose for contradiction that Theorem U's selector does not exist. We already excluded REF and any pair with `A_r+A_s=0`.

If two A-values are unequal, they are not opposite (the preceding exclusion), so they are not in one opposite pair `{c,−c}`. After the sign changes (1), their new values still have both nonzero SUM and nonzero DIFFERENCE. According to whether they lie in the same or different anchor gaps, §5.1 or §5.2 finishes. Hence all rotation transports are a COMMON value c. Since at least two rotations exist and inverse pairs were excluded, c!=0.

For the fixed E:

* Two rotations in the SAME anchor gap must have DIFFERENT χ-bits; otherwise their new values are both ±c, with sum ±2c!=0, giving §5.1.
* Two rotations in DIFFERENT anchor gaps must have EQUAL χ-bits; otherwise their new values are opposite and their difference is ±2c!=0, giving §5.2.

There are p anchor gaps and at least p+1 rotations, so two rotations r,s share a gap and have different bits. A third rotation exists (p>=3). If it lies in that same gap, its bit cannot differ from BOTH r and s. If it lies in another gap, its bit cannot equal BOTH their different bits. Either way the two bullet conditions contradict one another. This proves Theorem U, as a written candidate. QED.

## 7. Exact acceptance boundary and relation to earlier candidates

The theorem's proof would close the original <=p−3 branch and L_RES as a CONSEQUENCE of a broader direct selector, not by rehabilitating L_MAX or by inferring caller failure from a profile. All original caller failures remain retained but unused. Other rotation-count bands and the original broad ordered Olson conjecture remain outside this paper. The earlier o_π bands, high-surplus family and spare-reduction records remain immutable; their open-frontier statements record what was unproved when written, not contradictions or retrospectively accepted claims.

No result or assessment from the withdrawn f111 paper is used. The source order before this manuscript includes the fatal correction; a new referee must check especially Lemma A's maximality/swap/permutation argument, Lemma N's cyclic index lift, the cut-conjugation distinction in §5, the AP cross-difference support, and the exact2p cardinality of both completions. A source-pinned review is not formal or novelty acceptance.

## 8. Bounded exact diagnostics, separate from the all-prime proof

All checks below use integers mod p, original indices and local Python, prospectively permitted by the owner direction `contract-addendum-2-frontier-first-owner-direction-v1.json`; historical disallowed runs are not reclassified. The mathematical reasoning preceded these runs; no preregistration is claimed.

* Producer `frontier-20261028-olson-universal-rotation-band-experiment-v1.py`, SHA256 `a2aed4b4c4e7af8ae291832c145caf7d7989cb98bf6bfb9260a3976e0e242025`; data `frontier-20261028-olson-universal-rotation-band-results-v1.json`, SHA256 `3cefa58fce804f2e198ce4883248699aa5b52befae68a2a51d1ab78fcea1d55d`: 3665 actual words. Includes all 729 normalized p=3 reflection lists with TWO rotation placements each (NOT all rotation placements), random and free-expanded AP reflection lists p=5,7,11,13,17, and the seven already pinned high-surplus family words (input SHA256 `4960d9c627782ce004b13aa9e4f283eb26b79dd9f104cf47ce9537ff25efa92e`). REF uses an element count/residue DP. Otherwise it cyclically erases pairs and constructs the theorem's actual selector using the FIRST recorded pair.
* Adversarial producer `frontier-20261028-olson-universal-rotation-band-adversarial-v1.py`, SHA256 `1246bcd9cd1981f7dc5ff27dab8b9af207dcb2b50f7c32274bdb3ecc8e56d3eb`; data `frontier-20261028-olson-universal-rotation-band-adversarial-results-v1.json`, SHA256 `a43ae7a92e34d2247e7592c52368a8a0a36ddc488da740fbaa52caa7cfe679a0`: 960 additional actual words p=3,5,7,11,13,17,23,31, including constant nonzero S-transport values, rotations concentrated in a gap, different-gap bit contrasts, repeated adjacent rotations and random cyclic cuts. This producer imports the first producer's constructor and is NOT a separate implementation.
* Independent audit `frontier-20261028-olson-universal-rotation-band-audit-v1.py`, SHA256 `10bbf7cfe7aec562fb23c61b2ad3607fed9bc042dcddeab756865d6ee1119562`, imports NO producer code. Result `frontier-20261028-olson-universal-rotation-band-audit-results-v1.json`, SHA256 `52fa407b40352e447c64bcfec30bb0b9e21ff55007c3f554f3d58a173450dc41`: `PASS_INDEPENDENT_UNIVERSAL_ROTATION_BAND` for all 4625 original selectors; routes REF3569, full-S404, dropped-pair/same-gap407, dropped-pair/different-gaps245. It independently re-decides REF by a bitset DP, checks the literal cyclic deletion trace/AP anchors, checks EVERY one of 12540 recorded pair-drops and the common affine anchor interface, and independently finds 1056 non-REF actual selectors using either full S or the LAST recorded pair plus four transported optional occurrences (early witness search, NOT full subset enumeration).
* That audit also checks Lemma A on ALL normalized cyclic-adjacent-distinct lists: p=3,h=1 (10), p=3,h=2 (42), p=5,h=1 (3276), p=5,h=2 (52428); and 1000 sampled lists each at (p,h)=(7,2),(11,2),(11,3),(13,4). Duplicate-selected-index, altered-selected-rotation and rotation-as-anchor controls fail for their intended reasons.

These diagnostics are finite SAME-MODEL independently implemented checks, not an external-family/disjoint mathematical review, formal proof, exhaustive all-prime verification, general original-problem closure or novelty clearance.

**END — complete written Theorem U and L_RES implication; adoption pending NEW full-source review.**
