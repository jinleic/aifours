# Two further explicit seed neighborhoods

The two Section 4 hex tables in `code/extra_seeds.py` are the last two
128-hex-digit table rows in the delivered Kavut--Yucel manuscript. Their
bit order is identical to `code/seeds.py`: index x is the integer input,
coordinate i is bit i, and each printed nibble is decoded MSB first.

| Table | Weight | W(0) | Original forced distance | Minimum over linear shifts | Absolute indicator |
|---|---:|---:|---:|---:|---:|
| perm104-ac48 | 270 | -28 | 14 | 2 | 48 |
| perm74-ac64 | 246 | 20 | 10 | 2 | 64 |

Both have nonlinearity 242 and no Walsh zero, as checked by direct sums.
Their absolute indicator values differ from each other and from the
original three values 40,32,56. The autocorrelation invariance argument
in `seed-and-local-proof.md` proves pairwise extended-affine
inequivalence of all five explicit tables.

The same pair/triple reduction and six-flip hypergraph proof applies:
their spectra also have magnitudes in {4,12,20,28}. Every pair and every
triple is independently exhausted. There are no bound-preserving pairs,
no admissible radius-four triples, and hence no legal four-flip sets.

For the weaker four-uniform hypergraph necessary at radius six, the
complete independent counts are:

| Table | XOR-zero admissible fours | Other admissible fours | Admissible fives | Admissible sixes |
|---|---:|---:|---:|---:|
| perm104-ac48 | 2789048 | 1656 | 0 | 0 |
| perm74-ac64 | 2788816 | 930 | 0 | 0 |

All C(512,3)=22238720 triples are exhausted per table to construct these
anchors. The independent checker uses direct character sums, reversed
coefficient order, different lookup chunk size, and pair extensions.
There is no sampling of the four- or six-set ranges.

Odd distances cannot yield a Walsh zero from these even-weight seeds;
distance zero already has no zero. Thus no modification within radius
six followed by any linear output addition is a balanced NL>=242 table.
Original-origin radii below 14 and 10 are vacuous; these all-shifts
claims instead have forced minimum two and are non-vacuous.

Only explicit neighborhoods are excluded, not the entire permutation-
invariant classes in which the manuscript found the tables. No novelty
is asserted.
