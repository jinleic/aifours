# Compact exhaustive radius-six exclusion

This concerns only the three explicit seed tables in `code/seeds.py`,
at Hamming distance at most six and followed by any linear output shift.
It does not exclude arbitrary Boolean functions. Original-origin forced
balancing distances are 6,6,14; the minimum over shifts is 2 for each.
Thus these shifted neighborhoods are non-vacuous. The seeds are pairwise
inequivalent; see `seed-and-local-proof.md`. No novelty is asserted.

The old missing radius-six LRAT proofs are not used. The present method
is an exact combinatorial enumeration with a compressed list of four-
point anchors and a separately implemented complete check.

## Complete hypergraph reduction

Let B_x contain seed Walsh indices a with |W_g(a)|=28 and
(-1)^(g(x)+a.x) opposing the sign of W_g(a). For exactly six flips S,
put k_a=|{x in S:a in B_x}|. At a saturated index, exactly

    sign(W_g(a)) W_new(a) = 28 - 12 + 4 k_a = 16 + 4 k_a.

Thus |W_new(a)|<=28 at every saturated index if and only if no four-
subset of S has a common opposing index. Call a four-set admissible if
the intersection of its B_x is empty. Every target six-set must have
all fifteen four-subsets admissible. Other seed coefficients are checked
on the final complete Walsh transform and are not silently dropped.

Enumerate all C(512,3)=22238720 sorted triples x<y<z. Allowed fourth
points u>z are exactly the complement of the union of opposing-point
sets at indices in B_x intersect B_y intersect B_z. Small lookup tables
evaluate these exact finite sets using integer bitsets. Every triple
and every allowed fourth is covered, without sampling.

Most admissible fours have XOR zero. They need not all be stored: for
a five-set T the four-subset omitting v has XOR `XOR(T) XOR v`, so at
most one four-subset has XOR zero. Every six-set therefore contains an
admissible nonzero-XOR four anchor. All such anchors are stored; the
XOR-zero fours are counted separately.

For each anchor, the producer finds every fifth point making all four-
subsets admissible. It then finds every sixth point extending each
five-set. Deduplicating gives exactly all six-sets allowed by the
saturated constraints. Every resulting full 512-input table is checked
at every Walsh index, and every survivor is tested for a Walsh zero.
A zero represents exactly the possible balancing output shifts.

## Independent check and controls

The checker imports no producer. It reads the tables from the delivered
manuscript and reconstructs every Walsh coefficient by direct character
sums. It reverses the saturated-index order and uses union tables in
blocks of ten; the producer uses intersection tables in blocks of seven.
It exhausts the complete triple range and independently reconstructs
all anchors and the XOR-zero count.

It extends anchors differently: enumerate every pair of individually
valid extra points and directly check all six four-subsets containing
both points. It computes complete direct character sums for every
resulting six-set. No sample substitutes for the full range.

A planted control relaxes the bound to 44 and uses twelve possible flip
points. It audits every triple oracle and all C(12,6)=924 six-sets,
including a known return to a balanced NL240 table. That small control
is not evidence of a headline witness. The negative control removes
one recorded legal six-set; the independent checker must reject it
after rebuilding the entire range.

## Counts and scope

| Seed | XOR-zero admissible fours | Other admissible fours | Admissible fives | Admissible sixes | Sixes preserving all bounds | Sixes with a zero |
|---|---:|---:|---:|---:|---:|---:|
| dsbf40 | 2789485 | 234135 | 23652 | 195 | 120 | 0 |
| dsbf32 | 2789485 | 230325 | 23652 | 195 | 120 | 0 |
| rsbf56 | 2789485 | 239944 | 23652 | 195 | 120 | 0 |

Combine exact distance six with the independently exhausted distances
two and four, and parity/no-zero arguments at zero and odd distances,
to obtain radius-at-most-six exclusions. Invertible affine input
substitutions and affine output additions transport the exclusions:
they preserve Hamming distance and permute or negate the Walsh spectrum.
They neither increase the radius nor give a global exclusion.
