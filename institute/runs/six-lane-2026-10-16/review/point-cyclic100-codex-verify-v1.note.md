Both files’ SHA-256 hashes match the supplied pins. I read only those two files and used independent Python code entirely in memory.

All direct certificate checks passed:

- 825 distinct blocks, each containing four distinct points of \(\mathbb Z_{100}\).
- All 4,950 unordered pairs occur exactly once.
- 33 classes of 25 blocks, each partitioning \(\mathbb Z_{100}\); every block belongs to exactly one class.
- \(s(x)=x+1\bmod100\) preserves the block collection and maps every class onto a listed class.
- **Class-orbit lengths:** \(25,4,4\).
- **Block-orbit lengths:** eight orbits of length 100 and one of length 25.
- The point action is one cycle of length 100.

Independent seed expansion produced exactly the certificate’s 33 classes as sets of blocks. The 96 directed differences from the six X-blocks and two Y-blocks cover exactly \(\mathbb Z_{100}\setminus\{0,25,50,75\}\), each once.

All seven in-memory corruption controls were rejected by substantive checks, independently of hashes:

| Corruption | Detected reason |
|---|---|
| Swap points between blocks within one class | Six missing and six repeated pairs; class partition survives |
| Swap points between blocks in different classes | Pair coverage and class partitions fail |
| Replace one block by its \(+1\) translate | Duplicate block and incorrect pair coverage |
| Move one block to another class | Class sizes become 24/26; partitions fail |
| Duplicate a block | Only 824 distinct blocks; membership and pair coverage fail |
| Change header’s 100 to 101 | Header mismatch |
| Globally interchange point labels 0 and 1 | Design and resolution conditions survive, but the specified \(s\) fails both automorphism checks |

No substantive ambiguity under the supplied definitions. “Point-cyclic” concerns the point action, so shorter class orbits are consistent. The difference check uses ordered differences \(b-a\bmod100\).

RESULT: VALID