# Independent same-harness review: dihedral type-II separated-pair theorem

Native `/bin/date` observed immediately before this exclusive-create write: **2026-10-28T19:03:32-0700 PDT**.

## Verdict and scope

**Candidate as stated for every odd prime:** FATAL **0**, MAJOR **0**, MINOR **1**. The proof of the stated existence theorem is sound under the ordered-word definition, subject to the quantifier wording correction below. In particular, I independently reconstructed the interval lemma, both branches of the selector construction, and the original-order group product. This is a same-harness written-mathematics review, not an external-family, human, formal, source-provenance, or novelty verification.

The review is **type II only**: `2p−2` occurrences of `r^a`, `p−2` of `r^(−a)`, and `p+3` reflections in any actual order, with a `2p`-term identity subsequence retaining original order. It proves nothing about type III, all-high or other bands, `L_RES`, the full ordered Olson problem, or priority.

**Odd-integer scope distinction.** The manifest says “any odd p”, while the candidate itself says **odd prime**, with nonzero `a ∈ F_p` (candidate line 7). Its proof by itself must not be cited as a proof for nonprime p or nonunit `a`: the unique missing omission sum at line 35 uses invertibility. If “any odd p” is meant literally as every odd integer `p≥3`, the independent supplementary argument below covers that wider reading too, using `Z/pZ` and nonzero `a`; it is new review reasoning, not a claim that the candidate itself states or proves the composite case. The supplement remains within the same type-II word class.

## Frozen inputs and process

Read completely in the manifest order, in exact raw windows after SHA-256 checks; both live hashes match the manifest, and `wc -cl` matched both LF and byte counts. No hash mismatch.

1. `written-releases/math-2-ordered-word-definitions-v1.md`, 16 LF, 1,275 bytes, SHA-256 `010ef028f750f718df327102ec92e1803289169b512d361bf66ed2e28145c9fc`.
2. `mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-type2-separated-proof-v1.md`, 73 LF, 7,417 bytes, SHA-256 `556fd2a1e92eb3a6b4bff4a89068949608db37f938cd44334870f9abc8b79530`.

The first path is relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`; the second is relative to `/Users/jinleic/repos/aifours/`. Binding `manifest-v1.json` SHA-256 is `ee209b9d2922c34eb8da4c3d68e3bf0bc299972acf8e009c6c612681f86619ed`. All candidate line references below refer to input 2.

## Finding: MINOR 1, existential quantifier in line 37

At line 37, “the actual product … is identity unless the actual target … is the unique missing value” reads as a statement about **any particular choice** of the `2p−2` rotations. That literal statement is false; the correct statement is that **there exists** such a rotation choice giving identity if and only if `y_j−y_i ≠ T_ij`. Lines 39–43 and the subsequent proof use the correct existential contrapositive, so this does not defeat the theorem.

Concrete actual-word counterexample to the line's universal reading: take `p=3`, `a=1`, and
`W=(s, rs, s, s, s, s, r², r, r, r, r)`.
For the low pair at positions 1 and 2, `Q_2−Q_1=0`, `T_12=0`, and the target is 1, hence not missing. Yet the original-index choice `(1,2,7,8,9,10)` has product `r ≠ e`; another legitimate choice `(1,2,8,9,10,11)` has product `e`. I directly multiplied both. Change line 37 to “an original-order two-reflection identity selector exists unless …”; do not claim every choice works.

## Independent reconstruction of the prime theorem

Use `r^p=s²=e`, `sr^x=r^(−x)s`, and represent `r^e s^t` by `(e,t)`, with multiplication `(e,t)(f,u)=(e+(−1)^t f,t xor u)`. Thus all calculations below are on the **selected original indices in their original order**, not an unordered product. Definitions input lines 8–9 requires this order and exactly `|D_(2p)|=2p` indices.

1. **Separated low pairs (candidate lines 17–27).** If no two low edges are separated, their closed intervals of reflection ordinals pairwise intersect. Maximal left endpoint is at most minimal right endpoint, giving a common integer ordinal `t`, even when it is an endpoint; if there are no edges, choose any `t`. There are `p+2` reflections strictly to either side in total, so the two sides contain at least `p` within-side consecutive gaps. Each such gap has prefix increment at most `−1` or at least `p+1`. These gaps are disjoint, and the total supplies only `p−2` negative rotations and `2p−2<2(p+1)` positive rotations. At most `p−2` gaps can be negative-type and at most one can be positive-type, a contradiction. Therefore `i<j<k<l` with two low pairs exists.
2. **Low-pair missing target (lines 31–43).** For `u=Q_j−Q_i∈[0,p]`, actual signs are reversed only between `i,j`, so the total signed counts are `A=2p−2−u` and `B=p−2+u`, each at least `p−2`. Omitting `p−2` rotations using `q` negative signed values gives `(p−2−2q)a` for every `q=0,…,p−2`. Since `p` is odd and `a≠0` in `F_p`, these are `p−1` distinct residues; the excluded formal `q=p−1` gives 0. The full signed sum is `T_ij=pa−2au=−2au`, so exactly the selected-sum target `T_ij` is missing. The ordered two-reflection exponent is `selected_sum+y_i−y_j`. Thus no two-reflection selector forces `y_j−y_i=T_ij` on **every low edge**; no graph connectedness or global gauge is needed.
3. **Four-reflection completion (lines 47–59).** Under the no-selector assumption, select the two separated low pairs with increments `u_1,u_2`. Taking all actual rotations, their signs are flipped exactly in the two disjoint intervals, giving total `−2a(u_1+u_2)`; the four chosen reflections contribute its negative. The oversized product is therefore identity. Among its `3p−4≥2p−1` signed rotations, at least `p` have the same one of the two values `±a`. Removing those actual `p` rotations changes the exponent by `±pa=0`; deleting rotations does not change reflection parity at any surviving rotation. Exactly `2p−4` rotations and four reflections remain, giving `2p` distinct original indices and identity, contradiction. This also covers the boundary `p=3`.

## Independent supplement for the literal “every odd p” reading

This section proves a separate extension, rather than silently treating a nonprime `p` as a field. Let `p≥3` be odd, exponents lie in `Z/pZ`, and `a≠0`.

* If `gcd(a,p)=1`, the reconstruction above works verbatim: `2a` is a unit, so the `p−1` omission sums are distinct. No field operations beyond invertibility are used.
* If `d=gcd(a,p)>1`, write `m=p/d`; both `d,m` are odd, `m≥3`, and `m≤p/3`. The subgroup generated by `a` is the set of residues divisible by `d`, of order `m`. Among `p+3=dm+3` reflections, at least `m+1≥4` have exponents in one residue class modulo `d`. Choose four of them in their original order; their three intervening gaps are disjoint. Write `u=Q_j−Q_i` for any adjacent chosen pair and call the gap good when `m−p+1 ≤ u ≤ 2p−m−1`. A nongood low gap has `u≤m−p` and consumes at least `p−m` raw negative rotations; at most one such disjoint gap exists since `p−2<2(p−m)`. A nongood high gap has `u≥2p−m` and consumes at least `2p−m` raw positive rotations; at most one exists since `2p−2<2(2p−m)`. Hence one of the three gaps is good.
* For that actual same-class pair, signed rotation counts `A=2p−2−u` and `B=p−2+u` are both at least `m−1`. Omitting `k=p−2` actual rotations permits `q` negative signed rotations in the integer interval `[max(0,k−A), min(k,B)]`. This interval has at least `m` values: if both `A,B≥k`, it has `k+1≥m`; if one is below `k`, the other exceeds `k` because `A+B=3p−4`, and it has respectively `A+1` or `B+1` values. As `m` is odd, `(k−2q)a` for `m` consecutive `q` covers the whole subgroup generated by `a`. Consequently the sums of the remaining `2p−2` signed rotations cover that subgroup as well. The reflection difference lies in the subgroup by the same residue class, so one actual two-reflection original-order selector is identity. This establishes the nonunit branch without using the prime-only missing-residue assertion.

This extension does not change the source candidate's own stated scope and is not a formal proof or independent-family review. As additional finite diagnostics only, the separate supplement checked 16 seeded nonunit words at `p=9` and 48 at `p=15`, explicitly constructing and directly multiplying a two-reflection selector for each; these examples are not a proof of the unbounded statement.

## Independent exact computation and receipts

`independent-exact-check-v1.py` is my own standard-library implementation, not an author script. For `p=3`, it enumerates all `C(11,6)·5=2,310` actual reflection/rotation position patterns, both `a=1,2`, and all `3^6=729` reflection-exponent vectors per pattern and `a`: **3,367,980 actual qualifying words**, with no omissions modulo a normalization. For each pattern it independently evaluates every actual six-index choice; an exact bitset encodes the label vectors making its original-order product identity. Every word is enumerated and checked against these selectors. This is a batched exact selector enumeration, not a claim of 3,367,980 separate runs of the group-product DP.

* **3,353,790** words have a two-reflection identity selector; the remaining **14,190** have no two-reflection selector and all have an explicitly constructed legal four-reflection selector. No word failed.
* The implementation checked 32,340 low pairs across the 2,310 patterns for each of the two `a` values, including the missing-target identity and the separated-pair construction for every applicable reflection-label assignment. It also performed **18,480** separate direct original-order group-product DP comparisons of exact two-/four-reflection existence, against the batch encoding.
* For `p=5` and `p=7`, seed **2010243745**, it generated **160 iid random words per p** (uniform nonzero `a`, shuffled multiset positions, independent uniform reflection labels) and another **160 gauge-stress words per p** with random positions and `y=−2aQ`. An independent DP over original positions and dihedral group products found and directly multiplied a `2p`-index identity for every word. All 160 iid examples at each p had a two-reflection witness; all 160 gauge examples at each p had no two-reflection witness and were verified by an explicit four-reflection construction. It checked 8,204 low edges at p=5 and 12,823 at p=7. The gauge words are deliberately structured stress tests, not iid uniform label samples.
* Example iid `p=5`, `a=2`: the full 19-element word is stored as sample index 0 in the receipt, and an independently checked two-reflection witness is the 1-based index sequence `(1,3,4,5,6,7,9,10,13,15)`. Example iid `p=7`, `a=5`: the full 27-element word is sample index 0 for that p, and a checked two-reflection witness is `(1,2,3,4,5,7,8,10,11,13,14,15,18,19)`. Each word is encoded `[exponent,reflection_bit]`, where the bit 1 means `r^exponent s`.

All artifacts below are in this review directory; commands actually run were `python3 independent-exact-check-v1.py` and `python3 composite-supplement-v1.py`:

* `independent-exact-check-v1.py`: SHA-256 `fb257f19198607fd7b14e19c950c469efd12b9d7615727887fa953e7a6d1ff92`.
* `exact-check-results-v1.json`: SHA-256 `f4e1fbdd8aa24d0fe5ff1cc75bab68ab8c4868b3d7c713fa738e3a573835dba7`; contains all 640 sampled words and their actual witness indices and the exhaustive counts.
* `composite-supplement-v1.py`: SHA-256 `8dc0d568210a9db8c45fd3da0ead087acb892c817567d1b52e97182e5fa526a8`.
* `composite-supplement-results-v1.json`: SHA-256 `fff9b6b28c194a06023af18a9f685eaf200ceffe173057ad867216c9e579e2e3`.

## Named unverified imports and limits

The definitions input quotes `/Users/jinleic/repos/aifours/mathematics/olson-ordered-egz/source/problem.zh.txt` and cites a book-page transcription; neither that underlying file nor the PDF/page image was independently read or re-hashed in this review. The review uses the ordered definition literally as supplied, and makes no source-transcription or source-priority finding.

Candidate lines 67–69 name `frontier-20261028-dihedral-type2-separated-experiment.py`, `frontier-20261028-dihedral-type2-separated-results.json`, `frontier-20261028-dihedral-type2-separated-checker.py`, and `frontier-20261028-dihedral-type2-separated-check-results.json`. Their bodies, claimed hashes, claimed 800 examples, and mutation results were **not** independently read, checked, or used as proof. The listed independent computations above are separate. No author contact, external model, or held/withdrawn/quarantined material was used.
