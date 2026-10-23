# Independent cross-vendor verification task: LKTS(87) certificate

Read only files in this directory. Do not modify files, delegate, or access the network.

Definition. On X={0,...,86}: an STS(87) is a set of 3-subsets in which every unordered pair lies in
exactly one block. A KTS(87) is an STS(87) whose blocks are partitioned into 43 parallel classes, each
a partition of X into 29 triples. An LKTS(87) is a family of 85 KTS(87) whose block sets are pairwise
disjoint; equivalently, together they contain every one of the C(87,3)=105995 triples exactly once.
Resolutions may differ between constituents; no automorphism condition is part of the definition.

File `lkts87_g903.txt` (expected SHA-256 65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e)
claims to be an LKTS(87): one header `LKTS 87`, then `KTS i` (i=0..84 in order), `CLASS j`
(j=0..42 in order within each system), and triple lines of three integers. `#` lines are comments.

Tasks:
1. Verify the SHA-256 of the file.
2. Write and run YOUR OWN verification code in memory (for example `python3 -c`; you may not write
   files, and heredocs may be blocked by the sandbox). Check every condition directly: each class is a
   partition of all 87 points; each constituent covers every pair exactly once; exactly 85 constituents
   with 43 classes each; no repeated block; the union of all blocks is exactly the set of all 3-subsets.
   Account for every noncomment line; reject anything unrecognized.
3. Run at least three corruption controls in memory against your verifier (for example: swap one point
   between two triples of one class, duplicate a constituent, drop a class) and show they are rejected
   for the intended reason.

Report: first line exactly `RESULT: VALID`, `RESULT: INVALID`, or `RESULT: INCONCLUSIVE`; then the exact
commands with their outputs (counts), then the controls. Make no novelty or priority claim.
