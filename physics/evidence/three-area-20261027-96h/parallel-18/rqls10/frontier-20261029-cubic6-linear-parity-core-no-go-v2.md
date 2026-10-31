# The cubic-root six-dimensional master has no linear parity core of nine or more bases

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:58:57 PDT 2026**. This supplies an exact no-go for a natural 6D complement alphabet, but not for arbitrary C6 rays or unrestricted QLS10.

**v2 citation correction:** v1 SHA **0974eb0cfedeae0cea6086908ad2df7bafd491a752d6d5631bd96964e9afe659** mistyped the independent replay result hash; this successor corrects it. No mathematical claim changes.

## Theorem

Let omega be a primitive cube root of unity. Form all projective rays in C6 represented by nonzero vectors with entries in `{0,1,omega}`. No odd number M>=9 of distinct orthonormal bases chosen from these rays can have BOTH properties:

1. every ray occurs in either 0 or exactly2 selected bases;
2. any two selected bases share at most one ray.

Consequently, the 45-ray/15-basis 6D sector of a maximal 1RQLS10 balanced-quotient parity core CANNOT be contained in any common-unitary image of this alphabet. This holds for **every** 4D complement, not just the explicit Pauli 4D core. Its 15 selected row/column/transversal contexts necessarily have pairwise cell intersections at most1 and each selected ray occurs twice.

The restriction is meaningful: the same alphabet DOES contain a linear 21-ray/7-basis parity configuration with context graph K7, independently checked below. The theorem excludes odd M>=9 only.

## Finite master structure

There are exactly **665** projective input rays and **153** orthogonal 6-bases. The latter have these numbers of coordinate-singleton rays:

```text
  1 basis:  6 singleton rays  (the standard basis A)
 40 bases:  3 singleton rays
 72 bases:  1 singleton ray
 40 bases:  0 singleton rays  (type D)
```

Every type-D basis has ZERO other bases with which it shares exactly one ray. Every basis disjoint from A is type D. These are exact complete statements about the named finite alphabet, not general statements about arbitrary six-dimensional vectors.

## Proof from the census

In any selected linear 0/2-incidence configuration, every basis must share its six rays with six DISTINCT other bases, so every selected basis has six neighbors in the source single-ray-intersection graph. A type-D basis has none and cannot be selected.

If A were selected, its six rays would account for exactly six other contexts. Since M>=9, some other selected basis would be disjoint from A, hence type D, impossible. Thus A is not selected either.

Every remaining selected basis has an ODD number of singleton rays, either1 or3. An odd number M of such bases gives an odd total number of singleton incidences. But each singleton ray occurs zero or two times by hypothesis, so the total must be even. Contradiction.

## Exact checks and sharpness

`frontier-20261029-cubic6-master-structure-v1.py` SHA **d54baa393268f5b6247151256abe73c61684fd5f4a4736d85f57733f658d0719**, result SHA **54ed33497b845b6123eaa39e5f295e5d3bd9a2f4db158341b3dc614b1e1502c1**, exhausts the 3^6 source vectors modulo global phase, constructs all orthogonality edges by exact cubic-root coefficient counts, enumerates all 153 six-cliques and records every intersection degree. Independently, `frontier-20261029-cubic6-master-structure-replay-v1.py` SHA **78c5e1a16fb266517392af35ea0a91816bcced8cab28f521fc40bd5fecaf03f2**, result SHA **9c3d8ceb7ae158865473f8797c5699059a26d75d0090c1906e92a3c2f175f663**, generates phase patterns by support, uses exact `Z[omega]` arithmetic and pivoted Bron–Kerbosch, and matches all665 literal rays, all153 bases and every single-intersection degree. [Pavičić–Megill](https://pmc.ncbi.nlm.nih.gov/articles/PMC7512515/) independently identify this as a 216-ray/153-basis active master; the present generators also retain 449 rays that appear in no full basis.

`frontier-20261029-cubic6-seven-context-witness-v1.py` SHA **1c1428e55d84d46f453fe5aa32242e7537aba4b08df9d953bc591bb1f94b95fa**, result SHA **b7574d911f9c0177ed48aa1e9c61e4a9c1578398e1d11eec61635714e5345d09**, verifies 21 distinct master rays in seven 6D ONBs with each ray twice and every pair of contexts sharing one ray. Thus the M>=9 threshold is sharp for odd linear parity configurations.

The finite generation, both exact bases, linear-context caller, and 75-ray sector inference require independent full review. This result does not exclude larger alphabets, non-alphabet vectors, non-sector parity cores, or a general maximal 1RQLS10.
