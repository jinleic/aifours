# Erratum v2: only two complete phase words are excluded

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:48:29 PDT 2026**. This additively corrects `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`, and `checkpoint-069-second-odd-tail-proof-correction-v1.json`, SHA-256 `d8992077044b3099f5ab875fe72fc45f45e1e646a052f491ea45db60bc4e7520`. Frozen bytes remain untouched.

The previous erratum correctly identifies the upper-envelope proof gap for a final node in the second odd band, but its count of **three** entirely excluded phase words is too strong. In the word \((2,1,3,5,4)\), the third node is class 3, with even sign positive and odd sign negative. It may lie **inside the second odd band** \((c,d)\), before that selected member's second odd root. The available four-circuit proof only handles its third node at or below \(c\); the class label alone does not guarantee this. The remaining part of that word is therefore **OPEN**. No counterexample is asserted.

The available complete-word exclusions are only
\[
(2,1,2,5,4),\qquad(2,1,3,2,5).
\]
For the first, the class-2 third node has negative even sign and hence lies strictly before the second odd band; its final selected positive nodes in classes 5/4 lie after \(d\). For the second, the strict class-3-to-class-2 backward even crossing puts both possible third nodes in the second even-root band inside \((b,c)\), while the final class-5 node is after \(d\). The named gap-case and corrected early-third arguments apply.

Two further words are only partially excluded: \((2,1,3,2,4)\) remains open when the final selected node lies in \((c,d)\), and \((2,1,3,5,4)\) remains open when its selected third node lies in \((c,d)\). The other eight conservative words are open. Thus **ten of twelve words remain open in whole or in part**. These are weak odd-canceling-certificate classifications, not direct strict-negative-coordinate classifications or an unrestricted SPR7 verdict.

The exact actual-box failure of the old common vertex in one of the open subcases is `frontier-20261029-second-odd-band-fixed-vertex-failure-v1.md`, SHA-256 `acdb9f5b33f4308507929481321adfcc50e3c1eac03450f83e1fd918b5b95755`; it is not a no-go certificate. No independent review, formal verification, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
