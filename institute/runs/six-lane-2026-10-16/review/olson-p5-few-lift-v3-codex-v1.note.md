**ACCEPT**, conditional only on the supplied parent-accepted statements at their accepted scopes. **0 FATAL / 0 MAJOR / 0 MINOR. No repairs required.**

All 16 snapshot SHA256 hashes and byte counts match the supplied pins. The audited conclusions are precisely the length-18 INV* statement and length-19 ordered identity10-subword statement with \(o_F\le4\).

1. **The p=5 substitution is sufficient and noncircular.**  
   For a length-18 avoider, \(o_F=0\) is impossible; \(o_F=1,2\) supplies the nonzero rotation pair by ROT-o2; \(o_F=3\) uses ROT-o3; \(o_F=4\) uses C5. These accepted statements concern maximal **constant reflection blocks** and require no reflection-run constancy (SOURCE10:9; SOURCE11:7; SOURCE06:6–8). Thus C5 supplies exactly the missing input identified in SOURCE01:30–36.

   REFL-few-odd then applies to the same word: length \(18=4p-2\), avoidance, rotations in a common nonzero ±pair, and \(o_F\le4\le5=p\). Its accepted statement holds for every prime \(p\ge5\), without an additional RGR or block-count hypothesis (SOURCE03:21–28; SOURCE09:6). This establishes SOURCE00:165–173.

2. **Case 1, \(R\le2\): pair counting and cyclic order are valid.**  
   Here \(F\ge17\), and
   \[
   \sum_S\lfloor |S|/2\rfloor=(F-o_F)/2\ge7,
   \]
   since \(F-o_F\) is even and at least 13. Five disjoint equal-reflection pairs therefore suffice.

   With a rotation present, start the frame at a rotation; with no rotations and nonconstant reflections, cut at a value change. No constant block wraps across either cut. The remaining all-equal reflection case supplies ten identical reflections directly (SOURCE02:31–34).

   Restoring the original index order is legitimate: if the selected products on the two sides of the cut are \(u,v\), the products \(uv\) and \(vu=u^{-1}(uv)u\) are conjugate. Identity is preserved. This checks SOURCE02:35–36 and SOURCE12:49,59 without assuming commutativity.

3. **Case 2: the odd-block deletion lowers \(o_F\) exactly by one.**  
   Deleting one letter from an odd block of length at least three leaves that block nonempty, of even length at least two. No separator disappears, no other blocks fuse, and no block splits—even when the block crosses the displayed linear boundary. Hence
   \[
   o_F(w')=o_F(w)-1\le3.
   \]
   The length-18 deletion remains an avoider, so the previously accepted INV*-FEW(a) suffices. Reinserting the same reflection inside its surviving constant block preserves the rotations and reflection-run constancy (SOURCE00:181–183,204–205; SOURCE02:37–39; SOURCE07:6). A resulting \(o_F=0\) branch closes by the accepted impossibility statement.

4. **Case 3: each separate rotation deletion stays within \(o_F\le4\).**  
   If the deleted rotation’s run survives, the constant-block decomposition is unchanged. If its run becomes empty, another rotation run survives: the deleted run was a singleton and \(R\ge3\). Its two bordering reflection runs are therefore distinct cyclic runs.

   Unequal bordering block values remain distinct. Equal values fuse once: odd+odd lowers \(o_F\) by two; odd+even and even+even preserve it. The fused block’s outer neighbours already have different values or remain separated by rotations, so no cascade occurs. Consequently,
   \[
   o_F(w_i)\in\{o_F(w),\,o_F(w)-2\}\subseteq[0,4].
   \]
   This verifies SOURCE00:184–194, including the cyclic boundary. The two words are separate single-letter deletions, each of length 18 (SOURCE02:41–43).

   A third rotation survives in both words. Its value \(t\ne0\) belongs to both resulting ±pairs, forcing both pairs to equal \(\{t,-t\}\). Every original rotation survives in at least one deletion. Any cyclically adjacent unequal reflections in the original word also remain adjacent after deleting a rotation, contradicting the deletion’s constant reflection runs. Thus reconstruction proves the original word is RGR (SOURCE02:43–46; SOURCE00:206–208).

5. **The complete call inventory has no scope overrun.**

   | Application | Word and bound | Accepted input |
   |---|---|---|
   | L-INV | Length 18, \(o_F\le4\) | ROT-o2 / ROT-o3 / C5, then REFL-few-odd |
   | Case 2 INV* | Length 18, \(o_F=o-1\le3\) | Existing INV*-FEW(a), SOURCE07:6 |
   | Case 3 INV*, twice | Each length 18, \(o_F=o\) or \(o-2\le4\) | L-INV established above |
   | Final long-word step | Original length 19 word, now RGR | RGR-LONG(5), SOURCE12:7 |

   All deletion words avoid because their ordered subwords are also ordered subwords of the original word. Insertions reconstruct the conclusion; they precede no INV*, ROT or REFL call. RGR-LONG’s accepted final statement requires precisely the nonzero rotation pair and constant maximal cyclic reflection runs. Its intermediate inherited hypotheses do not become additional caller obligations (SOURCE00:210–225; SOURCE12:7–16).

6. **The terminal RED bound is adequate.**  
   The supplied reflection proof preserves \(o_F\) under normalization and never increases it through P1–P4: even-block fusion/appending preserves parity except for a possible two-odd-block loss; P3 changes no blocks; P4 inserts its equal pair into a block **of the same value**, preserving parity, with only a possible further fusion loss. Insertion into another-valued block could split it, but that is explicitly excluded (SOURCE04:79–112).

   The terminal maximal decomposition has all blocks odd, hence \(k=o_F(\mathrm{terminal})\le o_F(\mathrm{input})\le4\le5\). The accepted small-k residual exclusion applies (SOURCE04:82–87; SOURCE14:3,7–13; SOURCE15:3,11). No bound on the original total number of blocks is silently assumed.

7. **Previous M1 is discharged for these restricted consequences.**  
   SOURCE05:97–110 withheld the lift because the dependency texts and deletion-call justification were absent; it did not reject C5 (SOURCE05:3–6). This packet supplies the pinned accepted inputs, parent-accepted C5, and the valid call inventory above. The old exclusion expressly arose from ROT-o4’s \(p\ge7\) scope (SOURCE07:9; SOURCE11:8–11). C5 replaces that input; every remaining invoked statement admits p=5.

**Audited versus imported:** I independently checked the implications, parity changes, cyclic-order arguments and application scopes above. The parent-accepted theorem statements—including C5—are imports; their unseen originals, computational output bytes and historical runtime are not independently verified here. SOURCE00’s search tables are supporting metadata, not premises. Part (b), SHgen-E and the historical D10 census enter neither proof. Acceptance makes no novelty claim and establishes neither unrestricted INV*(5) nor complete ordered Olson for D10 (SOURCE00:224–251; SOURCE06:25–27).