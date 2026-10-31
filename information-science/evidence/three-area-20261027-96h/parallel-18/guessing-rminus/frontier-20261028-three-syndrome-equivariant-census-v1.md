# Equivariant three-state syndrome-color census

**Status: WRITTEN-CHECKED-IN-KERNEL; scientific review pending.** For a three-state q=8 syndrome support with no constant syndrome coordinate, translate each parity to a one-hot state indicator and partition the ten factor indices by their associated indicator. The exact finite census `frontier-20261028-three-syndrome-equivariant-color-census.py` SHA-256 `de060057fcd59fb7d15a2d8d97ddd37bb290a3fb9f9a2ccca0e9a6260b99da4e`, receipt SHA-256 `832f6da50b32eac99b0ebd71b2a9839e109556cdce52ef612e8f210e0b0cea25`, checks all `3^10=59,049` colorings. Of these, 42 meet both conditions: every vertex is incident to at least two colors, and every one of the four factor-preserving graph automorphisms sends the unordered color partition to itself, possibly permuting color labels. Up to state relabeling these form exactly seven partitions.

The first four are the orbit-constant cases in `frontier-20261028-three-syndrome-symmetric-color-census-v1.md` SHA-256 `00732f3a4277a201162503b8c04d25ed02c64647e9cd1c4c1556197e50727f84`. The remaining three are

```text
{1,2,10} {3,6,8} {4,5,7,9}
{1,5,8}  {2,6,9} {3,4,7,10}
{1,8,9}  {2,5,6} {3,4,7,10}
```

The latter two have exact conditional no-gap certificates in `frontier-20261028-three-syndrome-equivariant56-theorem-v1.md` SHA-256 `12de70c68bf009c53c9518d18416a5ddf4bb5ebf538886a989d1617e735817c3`; they import the still-unreviewed repaired two-syndrome theorem. The first listed extra partition remains open. A floating-point outer LP proposed zero gap, but no exact certificate is yet available; numerical status is not proof.

These seven are not all three-state syndrome patterns: constant factor syndromes, non-equivariant partitions, or a vertex meeting only one factor color fall outside the census. Nor are the mathematical identities formally verified or independently scientifically adopted. The first four and the last two are six restricted candidate classes, not a global three-syndrome or unrestricted guessing-number result.
