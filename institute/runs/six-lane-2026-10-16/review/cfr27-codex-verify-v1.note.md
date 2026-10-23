RESULT: VALID

All four SHA-256 hashes and byte counts match the manifest, checked before numeric parsing. Strict parsing consumed all **22 lines, 594 entries, and 1,528 bytes**, including canonical decimals, single spaces, and final LF. Each CFR contains 5×27 entries; each DM contains 6×27.

| Independent check | A | B |
|---|---:|---:|
| DM row pairs enumerating exactly residues 0–26 | 15/15 | 15/15 |
| DM differences inspected | 405 | 405 |
| CFR permutation rows | 5/5 | 5/5 |
| Ordered symbol pairs having five distinct nonzero cyclic distances | 702/702 | 702/702 |
| Distinct circular events `(d,a,b)` | 3,510/3,510 | 3,510/3,510 |
| DM→CFR entries matching exactly | 135/135 | 135/135 |

Both raw validity checks passed independently of the reconstruction.

All **14 targeted mutations**, seven per pair, were rejected by their intended invariants:

| Mutation | Verified rejection |
|---|---|
| Copy CFR row 0 into row 1 | Permutations preserved; 702 duplicate events per matrix |
| Swap positions 0 and 1 of CFR row 0 | Permutations preserved; A: 16 duplicate events; B: 18 |
| Duplicate one CFR entry | Row permutation fails; shape and range pass |
| Replace one CFR entry with 27 | Range fails |
| Drop one CFR entry | Row length becomes 26; shape fails |
| Increment DM entry `[1][0]` modulo 27 | Exactly five affected row pairs, each with one missing residue and one repeated twice |
| Copy DM row 0 into row 1 | Their difference is zero 27 times, missing residues 1–26 |

The supplied **n=4 boundary negative** passes all 12 forward nonwrap events but fails circular checking: 24 events have only 22 distinct triples. For example, `(a,b,d)=(0,3,3)` occurs in both rows: positions `0→3` and `2→1`, respectively. The latter wraps.

The supplied **n=3 positive** passes all six ordered symbol pairs and 12 distinct events. Separately rotating row index 2 left by seven positions in each pinned CFR preserved validity and all 3,510 cyclic distances. Normalization is not a validity requirement.

For reconstruction I computed, entirely modulo 27,
\[
b_j(c)=D_j[c]-D_0[c],\qquad
C_{j-1}[b_j(c)]=b_1(c),\quad j=1,\ldots,5.
\]
Each \(b_j\) is a permutation by its DM difference condition against row 0. Labels \(x=b_1(c)\) give common symbol labels. A repeated circular distance between two resulting CFR rows would repeat a difference between the corresponding DM rows at two columns, contradicting the DM condition.

Conversely, append a zero row to the CFR position maps \(P_j(x)\). Each position map is a permutation. If \(P_i(x)-P_j(x)\) repeated at distinct symbols \(x,y\), those symbols would have equal circular distances in CFR rows \(i,j\). Thus every DM row difference enumerates all residues exactly once. This uses **cyclic \(\mathbb Z_{27}\)** throughout; individual DM rows need not be permutations. No \(\mathbb F_{27}\) arithmetic is involved.

The successful in-memory `python3 -B -c` run used one process and one verifier thread, **0.044 CPU seconds**, and **21.23 MiB peak RSS**. Only the four pinned input contents were read; no files were written, and no network, solver, or delegation was used.

This certifies finite witnesses for CFR(5,27) and cyclic DM(6,27;1), establishing the lower bound of five CFR rows. It supplies no optimality or peer-review conclusion.