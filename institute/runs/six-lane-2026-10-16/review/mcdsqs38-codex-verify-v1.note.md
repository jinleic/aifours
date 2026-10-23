Independent in-memory Python verification passed; no claimant-lane files or checkers were accessed.

- **SHA-256:** matches `973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c`.
- **SQS:** 2109 distinct valid 4-subsets; all 8436 possible 3-subsets occur exactly once.
- **Derived colourings:** at every point, all 222 derived triples appear exactly once across 19 classes. Every triple avoids the derived point, and every class consists of pairwise disjoint triples. Each derived design also passed independent pair coverage: 666 pairs, each once.
- **Class-size multiset:** identical at **every point 0–37**: eighteen classes of size 12 and one of size 6.

For any STS(37), the number of triples is \(37·36/6=222\). A partial parallel class contains at most \(\lfloor37/3\rfloor=12\) triples, so every colouring needs at least \(\lceil222/12\rceil=19\) colours. The supplied colourings attain this bound. This agrees with [Tan–Zhou’s formula and definitions](/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt:110): \(\chi'(37)=19\). Consequently, every derived design is an mcSTS(37), and the block design is an mcDSQS(38).

Both \(g_1\) and \(g_2\) preserve the block set. Enumerating their permutation-group closure gives **order 342**. For each point \(x\), all nine group elements mapping \(0\) to \(x\) transport the colouring at 0 to the listed colouring at \(x\), treating classes as unordered.

Nine in-memory corruptions were rendered, reparsed, and rejected by structural checks independently of the checksum:

| Corruption | Rejection reason |
|---|---|
| Swap points between two blocks | Four uncovered and four repeated 3-subsets |
| Move a triple between classes | Destination class repeats points |
| Merge two classes | Only 18 classes at that point |
| Drop one coloured triple | Derived partition misses one triple |
| Set `COLOURS 18` | Minimum-colouring certificate requires 19 |
| Set `COLOURS 20` | Minimum-colouring certificate requires 19 |
| Replace a block with a duplicate | Repeated block |
| Insert the derived point into a triple | Triple fails to avoid that point |
| Substitute a disjoint, non-derived triple | Triple absent from derived design |

No definitional mismatch was found. Partial parallel classes need not cover all points, and class labels are immaterial. The source’s \(\chi'(37)\) is a minimum across designs; it does not assert that every STS(37) admits 19 colours. Symmetry is additional information.

RESULT: VALID