# One explicit continuous q18-containing Hadamard family has no transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent exception replay: **Wed Oct 28 19:49:44 PDT 2026**. This strengthens `frontier-20261028-binary-lift-transversal-rigidity-v1.md` SHA **ba643286afd36efb48a57aceac82c7762860bf3058bc3b25198e329717a0aaef** for ONE explicit family: it covers EVERY unit complex phase, including the low-degree exceptions, and does not import completeness of the q6 catalog. It remains a restricted-family result, not a general QLS10 no-go.

## 1. Exact family and claim

Let H be the FIRST literal BH(10,6) matrix in frozen Aalto supplement `frontier-20261028-aalto-bh10-6-catalog-v1.txt` SHA **3aab0ddb9d500946fbb45909fb6d5f6c46402033e2b26b797fce7a2a3547e281**. Define R={0,1}, C={0,1,2,3,4}, and

`K_(t,c)(z)=H_(t,c) * z^[t in R and c in C]`,  `|z|=1`.

Exact partial-row sums between R and its complement vanish on C; together with H's orthogonal rows this proves K(z) is a complex Hadamard for EVERY unit z. The independent checker SHA **ba5c889dcf382acabcf30c3340322c7f9443fd370c81b84ae9401d803dc4cf33** verifies these partial sums and H directly. Its q18 instance is the actual maximal QLS10 checked in `frontier-20261028-binary-lift-transversal-rigidity-v1.md`.

**Claim:** for EVERY unit z, EVERY physical K-row permutation, and arbitrary row/column phases and column permutations, the Fourier-product array

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)(z)/sqrt(10)`

has NO orthogonal transversal. This is stronger than merely no maximal array and stronger than the preceding degree>2 generic argument.

## 2. All unit-circle exceptional phases are sixth roots

For each of252 source-row halves E and45 K-column pairs c,d, the necessary half-orthogonality equation is a Laurent polynomial

`A_- z^(-1)+A_0+A_+ z=0`, `A_*, in Z[zeta6]`.

There are exactly11340 such literal half-polynomials. An independent exact scan `frontier-20261028-q18-affine-resultant-replay-v1.py`, SHA **c96217abbd24c047c9b50fc20f5366108c45056c258445b2be3ef4faeca8d0e0**, classifies them WITHOUT floating arithmetic:

```text
identity polynomials 896
nonzero reciprocal-resultant 1980
unit-root in mu6 1520
nonzero monomials proportional to z after multiplying the Laurent polynomial by z: 6944
```

The categories sum to11340. Here is the exact root test used. Put `P(z)=a z²+b z+c`, with a=A_+, b=A_0, c=A_-. A unit root must also annihilate its reciprocal conjugate `P*(z)=conjugate(c) z²+conjugate(b) z+conjugate(a)`. Let

`A=|a|²-|c|²`, `B=a conjugate(b)-b conjugate(c)`.

The resultant is `A²-|B|²`. If it is nonzero there is no unit root. If it vanishes and B!=0, the only possible unit root is `z=-A/B`; the scan checks exactly in Q(zeta6) that it is one of the SIX sixth roots and really annihilates P. When A=B=0, every nonidentity case in this literal census is `P=b z`, which has no unit-circle root. These checks prove that EVERY nonidentity half-polynomial's unit root lies in mu6.

For z not in mu6, the half graph for each E contains only identity-polynomial edges, a subgraph of its z=1 half graph. The z=1 representative has NO perfect matching for ANY E by the independent exact six-phase replay below, so no such z permits a transversal. This is an exact finite certificate, not the earlier numerical unit-root triage.

## 3. The six exceptional phases

For z=zeta6^s, `s=0,...,5`, `frontier-20261028-affine-six-exceptions-v1.py` SHA **463d2dc23fdf5d7761f97e7a99b7fea3a0101b2664acb076f8b8469f27a452aa** gives an exact certificate SHA **986f15a79db22b002167fceba63fb9f6f1f381e7e5122f79675846e40095f472**. For s=0,2,3,5 all252 half graphs lack a perfect matching. For each of s=1,4 there is one E/complement pair with a perfect matching. Coordinate-shift symmetry normalizes E to contain source row0 at physical coordinate0; the resulting `4!*5!=2880` row orders have a certificate digit naming a row with no orthogonal candidate column to normalized cell `(0,0)`.

Independent `frontier-20261028-affine-six-replay-v1.py` SHA **ba5c889dcf382acabcf30c3340322c7f9443fd370c81b84ae9401d803dc4cf33** rebuilds all six BH6 matrices and their252 half graphs, then checks all **5760** recorded row obstructions in a different exact Q(zeta3,zeta5) product basis. Physical row-shift symmetry puts the column0 cell of any putative transversal into row0. Its observed output is

```text
PASS six zeta6 phases; 4 halfgraph failures; 5760 independently checked row obstructions
PASS arbitrary-z rectangle is Hadamard by exact partial-row sums
```

The result uses only the specific literal H and exact checks, NOT the published claim that 34 classes exhaust BH(10,6). The second exact unit-root program `frontier-20261028-q18-affine-unitroots-v1.py` SHA **f3f8dc402153d57cbb84dd687b63fb45b21d7e79d99fc94af6fd77a2a56af6fc** independently classifies42 projective polynomial classes by Q(zeta6) polynomial gcd; it finds the same six unit roots, with generic half graphs lacking matching.

## 4. Limits

This is an entire continuous one-parameter K family, but only for the explicitly specified H and rectangle. It does not cover other q18 matrices, multiple independent affine parameters, arbitrary K or nonproduct QLS10. The finite scripts, reciprocal-resultant reasoning and symmetry caller need independent review before adoption. The q18 member is a 100-ray QLS but is not 1-resolvable; no unrestricted impossibility or novelty claim is made.
