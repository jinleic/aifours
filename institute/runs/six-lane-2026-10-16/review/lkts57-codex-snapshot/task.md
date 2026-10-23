# Independent cross-vendor verification task: LKTS(57) certificate

Read only files in this directory. Do not modify files, delegate, or access the network.

Definition (book: Yanxun Chang, "Existence Problem of Large Sets of Kirkman Triple Systems").
On X={0,...,56}: an STS(57) is a set of 3-subsets in which every unordered pair lies in exactly one
block. A KTS(57) is an STS(57) whose blocks are partitioned into 28 parallel classes, each a
partition of X into 19 triples. An LKTS(57) is a family of 55 KTS(57) whose block sets are pairwise
disjoint; equivalently, together they contain every one of the C(57,3)=29260 triples exactly once.

File `lkts57_g513.txt` (expected SHA-256 09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09)
claims to be an LKTS(57): header `LKTS 57`, then `KTS i`, `CLASS j`, and triple lines.

Tasks:
1. Verify the SHA-256 of the file.
2. Write and run YOUR OWN verification code (for example `python3 -c` or a heredoc; you may not
   write files). Do not import or execute check_lkts_independent.py for this step. Check every
   condition of the definition directly, including that each class is a partition of all 57 points,
   that each constituent covers every pair exactly once, that there are exactly 55 constituents with
   28 classes each, and that the union of all blocks is exactly the set of all 3-subsets.
   Also verify the parser cannot silently skip malformed lines (count every non-comment line).
3. Separately review check_lkts_independent.py for logic gaps (a false PASS path), citing lines.

Report: first line exactly `RESULT: VALID`, `RESULT: INVALID`, or `RESULT: INCONCLUSIVE`; then the
exact commands you ran with their outputs (counts), then checker-review findings. Make no novelty or
priority claim.
