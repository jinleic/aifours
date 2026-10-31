# A harder κ=1/e_F=2 candidate: exact DS3 split and qualified IPGEN scans

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 19:45:47 PDT 2026**. This is a frozen evidence dossier and written partial analysis, NOT an accepted finite residual witness, an ordered-Olson counterexample, or a proof of L_RES.

## 1. Frozen words and essential before-source overlays

For every prime p>=11 and a!=0 define `b=−a/2`, Z=σ_0, A=σ_a, B=σ_(−a), T_j=σ_(ja), ρ_b=r^b, and the actual word

`W_b = Z^(2p−7) ρ_b A A Z B B Z ρ_b T_1 ρ_b T_2 ρ_b ... T_(p−1) ρ_b`.

Actual named occurrence repetitions and chronological order are intended. It has F=3p−2, R=p+1, length4p−1, nonzero rotations, singleton cyclic reflection gaps, odd-run count p+2/e_F=2/κ=1 and raw matching `(p+5)/2<=p−3`. Its reflection-only projection is IDENTICAL to the REF-failing family proved in `frontier-20261028-olson-kappa1-e2-ref-fail-family-v1.md`, SHA256 `e9d49c28052f4821568eaec81085c793c1110413416b3c0f322caeec7bd2cdce`. Before reading that source, reviewers must first read BOTH its mandatory SEL overlay `frontier-20261028-olson-kappa1-e2-sel-overlay-v1.md`, SHA256 `278edd81bb512c1a4ff0c3e54c76eec57f38d953422c2e64007e190f4cbcc6ce`, AND its mandatory GEN overlay `frontier-20261028-olson-kappa1-e2-gen-overlay-v1.md`, SHA256 `74d5e17495cf62ad6e09a2284a22ada29eb36e3630d7f404ff956aff938dc1b4`.

The old source uses rotation a, whereas THIS word uses b=−a/2. REF-failure and the raw graph depend only on the unchanged reflection projection and which gaps are occupied, so their direct proofs apply. Its SEL multiplicity failure is likewise unchanged. The old family's specific GEN certificate does **NOT** automatically apply: each old tail block is now locally BAD, as calculated in §2. Its old GEN exclusion is not carried over by name.

This word is explicitly SOLVED: select all `2p−7` initial Z reflections, the first ρ_b, both A reflections, the first singleton Z, both B reflections, skip the second singleton Z, and select the next ρ_b. Exactly2p actual indices give

`Z ρ_b A² Z B² ρ_b = Z ρ_b Z ρ_b = 1`.

Thus even a fully verified membership in the retained residual would be a solved residual example, never a counterexample to Olson or L_RES.

The normalized p=11 and p=13 actual input bytes are `frontier-20261028-olson-kappa1-hard-candidate-words-v1.json`, SHA256 `6c355021602ffb682072023678f8ba2b0ecd60c67d200fcde1cfff1083c4b16d`; a=1 and b=(p−1)/2. The author first explored grammar parses BEFORE this freeze; the freeze is not represented as preregistration.

## 2. Exact literal local grammar difference

For each original tail block `T_(2j−1) ρ_b T_(2j) ρ_b`, the literal GEN GOOD4 parameters are

`A_rot=2b=−a`, `B_ref=−a`, `C=−a`.

Thus `A_rot=B_ref` but `C!=2 A_rot`, so the old family's original `p−1`/2 GOOD4 tail certificate is invalid for W_b. This does NOT prove failure of GEN or IPGEN: a different cut, omission, parse tree or inverse insertion may still work.

The literal historical GEN bases and operations used in the scans are scoped to same-type two-letter bases, actual balanced GOOD4 bases, actual SIX bases, consecutive concatenation and rotation wrapping; IPGEN additionally permits inserting an ACTUALLY adjacent inverse pair at an arbitrary gap of a certified block. SIX cannot appear in ANY deletion subsequence of W_b because all its rotations are the same nonzero b, while the SIX base requires a,a,c,c with `c∉{a,−a}`. Two adjacent rotations in W_b cannot be inverses because `2b=−a!=0`; inverse reflection pairs have equal exponents.

The named historical definitions were read only at `proof-EXTENDED-UNITS-AND-SIX-BLOCK-OBSTRUCTION-v1.md:65–127,181–205` and `proof-LOWER-BAND-SELECTOR-AND-INVERSE-INSERTION-v1.md:169–180`, at the exact hashes in the e9-family GEN overlay. Their entire source DAG, all OLD callers and old theorem acceptance were not independently reconstructed here.

## 3. p=11 is actually DS3-covered

For the p=11 frozen input, `frontier-20261028-olson-kappa1-ds3-witness-p11-results.json`, SHA256 `cc6df5d6abe6278923063c1ddc26e90f7d11d38984feea6d46122f2f1c111296`, gives this ACTUAL DS3 packet system at the original cut. All indices below are ZERO-BASED full-word indices:

* `K={22,30}`, C=20 reflection packets;
* singleton packets 3,4,5,6,7,8,9,10,11,12,13 and 17;
* binary packets `(14,16),(18,19),(20,21),(23,25),(27,29),(31,33),(35,37),(39,41)` in that actual order.

Each packet span precedes the next. The chosen endpoints and complete actual selector are recorded in the pinned JSON. For the literal selected-K gauge `z_j=y_j+2 sum_(K before j)x_r`, the eight signed increments are

`[10,1,1,10,1,10,1,10]` in F_11,

and base B=7. Their actual packet support is `{0,3,4,5,6,7,8,9,10}` and contains0. The selected 22 original occurrences multiply to identity. Thus this p=11 word has a POSITIVE actual DS3 packet certificate and is outside full L_RES's DS3-failure condition; do not call it a residual realization.

Separately written `frontier-20261028-olson-kappa1-ds3-witness-checker.py`, SHA256 `838bdc0217fd12c9f0c06457713a33cad59595f8e995b020e6dd1cf173cce436`, independently recomputed the actual K/gauge, all20 ordered packets, all eight nonzero increments, complete packet support and original group product. It returned `PASS_INDEPENDENT_ACTUAL_DS3_WITNESS` in result SHA256 `281a1ebe6b2b6ae8af42d695578190e632f9d16b7e293096de2e2bca8143636f`; duplicate endpoint, duplicate selected index and falsified gauge metadata were rejected for their intended reasons. It imports no witness producer code.

## 4. DS3 failure for p>=13 at the literal packet scope

For p>=13, `ν_M=(p+5)/2<=p−4`. Fix ANY actual even K and ANY cyclic cut. For two adjacent reflections, a nonzero difference of their selected-K gauge labels implies either their raw reflection exponents differ or their actual intervening gap contains a rotation; in both cases the corresponding CYCLIC raw edge exists.

If a pair of reflection endpoints has different selected-K gauge values, at least one adjacent reflection-to-reflection gauge difference in its actual span is nonzero. In a DS3 packet system the binary packet spans are pairwise ordered and disjoint, so choosing one such adjacent edge from each span produces a raw matching of the same cardinality. A system with p−3 nonzero binary packets would therefore require `ν_M>=p−3`, contradiction.

Thus for this family p>=13, the literal **p−3 nonzero-switch DS3 packet class fails for every K/cut/system**. This is an elementary written implication of the actual graph, not a claim that every possible OTHER selector, GS predicate, or OLD caller fails. In particular it does not conflict with the direct two-rotation selector in §1.

## 5. What the finite IPGEN scans do and do not establish

All cuts and one-letter omissions of the two frozen normalized words were scanned by THREE separately written local implementations:

1. Author depth-first reverse-insertion search `frontier-20261028-olson-kappa1-ip-fullscan.py`, SHA256 `f9a73a6b037e38d964d4ac709ee58aade45168f2fb220fc518b649836a039708`, using GEN parser `frontier-20261028-olson-kappa1-gen-parser.py`, SHA256 `fc7958ed6ea9e99384ef22f8b29ebed411c5149666d3dc34203cfe290775aaf5`. Before the candidate freeze it reported no tree, after 1,134/1,550 unique cut-and-omission words and 37,846/65,244 reduced sequences for p=11/13.
2. Separately written breadth-first inverse-removal audit `frontier-20261028-olson-kappa1-independent-ip-audit.py`, SHA256 `fb16dbfdb092196f3c773498ae4f183340f1865e6a391b794821a19104f0f2c3`, read the frozen word bytes and returned `PASS_INDEPENDENT_BFS_IP_AUDIT` in result SHA256 `eec6c850cf5c1b35409bf19bc6b4b442d55e6a04d4d6bcc2428c99c7a0bf4557`. It found the SAME initial and closure counts, no reachable GEN tree, and exercised rotation-value, known-GEN, IP-insertion-only and odd-length controls.
3. A further separately written erasable-gap chart `frontier-20261028-olson-kappa1-ip-chart-audit.py`, SHA256 `2fceefcbb02447157ec02294d1b90d8682bcd95a18d77ed2bf122ea1162830b5`, independently scanned all unique cut/omission words using stack free-reduction tables plus a same-type/GOOD4/concatenation/rotation-wrap chart. It reported no certificate for p=11 and p=13 in output hashes `30b1f2f95f9f502631fd01127f256c33bd7fd534073f8c29e2aec5bc815d9331` and `a360f07f777c2615e23eb2e655a5c5a4b6be427060e566b6a78898ff42faf03a` respectively, with IP-insertion and odd-length controls.

These are **three local implementations in the same harness/model context**, not three independent human or cross-model-family reviews. Their fixed input and outputs do not by themselves prove the grammar normalization, checker completeness or an all-prime IPGEN-failure theorem. For the intended normalization, a reviewer must establish both directions: any IP insertion inside a child can be postponed to an equivalent insertion at the corresponding gap of the whole concatenated/wrapped root, so all such insertions may be reversed as actual adjacent inverse removals to a GEN skeleton; conversely each reverse step may be reinserted into the root by the literal IP rule. The chart's erasable-gap semantics also need a soundness/completeness review. No result here is promoted merely by matching state counts.

Even if the p=13 IPGEN-failure result is ultimately verified, other OLD/GS and all retained caller conditions remain unchecked. It is NOT yet a certified full L_RES member. The p=11 case is already DS3-covered by §3.

## 6. Assurance and task frontier

No human, formal/kernel or cross-family validation and no novelty clearance has occurred. The exact required `L_RES` universal implication for all retained failures remains unproved. No genuine 2p-avoiding word is claimed; W_b has the explicit original selector in §1. The next scientifically consequential actions are disjoint review of the actual IP grammar/three implementations and independent checking of the remaining original caller conditions for p>=13—not re-running the scans or treating the successful selector as a counterexample.

**END — exact p11 DS3 exclusion and qualified p13 finite lead.**
