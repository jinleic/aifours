RESULT: VALID

An independent verifier was written in memory before reading either permitted file. The pinned input has **4,113,669 bytes** and SHA-256:
`e38945b1204e78937527f17db3d87f147e47885dc160c04b6a4de49377da0f46`.

All requested checks passed:

- Four disjoint groups of 32 partition `0..127`.
- **80,384 distinct blocks**, each a valid 4-subset with no three points in one group.
- Block triples equal the explicitly enumerated **321,536 admissible triples**, each with multiplicity one; no group triple occurs.
- Exactly one section per point. Each contains exactly its **2,512 derived triples**, once each, partitioned into 64 nonempty classes of disjoint triples avoiding that point.
- Every point has exactly **16 hole-free classes**.
- At every point, the class-size multiset is **28 × 4, 32 × 12, 42 × 48**. The size-28 and size-32 classes are hole-free.
- Block patterns: **2+2: 20,736; 2+1+1: 53,760; 1+1+1+1: 5,888**.

Every non-comment line was consumed:
\[
5\text{ headers}+4\text{ groups}+80{,}384\text{ blocks}
+128\text{ POINT}+8{,}192\text{ CLASS}+321{,}536\text{ triples}
=410{,}249.
\]
There is one additional comment line.

Since \(127\equiv1\pmod6\), equation (1.1) gives
\[
r=\chi'(127)=64,\qquad s=64-\frac{127-31}{2}=16.
\]
Each hole point belongs to \(96/2=48\) derived triples, requiring 48 different classes. Thus at most \(64-48=16\) classes can avoid the hole. **More than 16 is impossible.**

All seven in-memory controls were rejected for the intended reason:

| Corruption | Rejection |
|---|---|
| Swap points 32 and 34 between blocks 0 and 1 | Four admissible triples missing |
| Move a triple from class 0 to class 1 at point 0 | Repeated points within class |
| Move `(16,38,110)` from class 18 to hole-free class 60 at point 0 | Only 15 hole-free classes; disjointness and triple multiset preserved |
| Drop one colouring triple | 2,511 triples instead of 2,512 |
| Duplicate a block | Repeated block |
| Set `COLOURS 63` | Incorrect colour parameter |
| Set `HOLEFREE 15` | Incorrect hole-free parameter |

The source definitions agree with the summary. PPCs require disjointness without full coverage, so size-28 classes are permitted. Any ambiguity about “there are \(s\)” meaning at least or exactly is resolved by the bound above. Colourings are required separately at each point. The certificate therefore satisfies **gcDCQS(32⁴ : 0)**.

Model verification is not peer review.