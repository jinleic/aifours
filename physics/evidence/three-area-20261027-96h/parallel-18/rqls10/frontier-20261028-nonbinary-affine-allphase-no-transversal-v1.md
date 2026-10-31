# A nonbinary q18-containing affine family has no transversal at any phase

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent all-phase replay: **Wed Oct 28 20:16:58 PDT 2026**. This is a literal one-parameter nonbinary q18-containing family, NOT a BH(10,18) classification, a full four-parameter no-go, or an unrestricted QLS10 result. Unlike the all-q6 family results, it does NOT import a catalog completeness claim.

## 1. Actual continuous family

Let H be the FIFTH literal Aalto BH(10,6) representative in `frontier-20261028-aalto-bh10-6-catalog-v1.txt` SHA **3aab0ddb9d500946fbb45909fb6d5f6c46402033e2b26b797fce7a2a3547e281**. Define rectangle masks M1,...,M4 by

```text
R1={0,1,2,6,8}        C1={0,1}
R2={0,1}              C2={0,1,2,3,4}
R3={0,1,2,3,5,6,8,9} C3={0,1,6,7,9}
R4={0,1,3,5,9}        C4={0,1,2,3,4,6,7,9}
```

For any unit z set

`K(z)=H ⊙ z^[M1+M2+2M3+2M4]`.

The independent exact `frontier-20261028-nonbinary-fourmask-hadamard-v1.py`, SHA **2e4c03c5de9973db903568002b264ed557400fb504cc724244da8e5b780791a6**, checks all row-pair Laurent-coefficient sums vanish for the ENTIRE four-independent-parameter rectangle family, and that the four gauge-invariant mask signatures have rank4. Therefore this one-parameter specialization is Hadamard for every unit z.

**Claim:** the associated physical Fourier-product QLS has NO orthogonal transversal for ANY unit z, ANY physical K-row ordering, and arbitrary row/column phases and column permutations. Repeated rays are allowed. The z=zeta18 member is case0 in `frontier-20261028-q18-nonbinary-twentyfour-v1.json` SHA **776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2**: independent `frontier-20261028-q18-nonbinary-twentyfour-replay-v1.py` SHA **1ae8695da15fe9dc813539c9853f47bddcafe28cfaaff727ee69eb8088ec778b** verifies its 100 actual rays are distinct and proves it is NOT binary-gaugeable mod3. Hence this family is genuinely outside the previously excluded binary q18 lifts; it is still only one one-dimensional subfamily.

## 2. Unit-root reduction to 72 phases

For E a five-row half and c,d a pair of K columns, the necessary half-orthogonality condition is a Laurent polynomial over Q(zeta6), with exponents between -6 and6. Remove only powers of z (irrelevant on |z|=1) and denote the remaining nonzero polynomial P. Any unit-circle zero also zeros the reversed conjugate polynomial

`P*(z)=z^deg(P) conjugate(P(1/conjugate(z)))`.

The exact reciprocal-gcd program `frontier-20261028-nonbinary-affine-order72-v1.py`, SHA **9a560e85eec9a116fe37b5633b46ca10eed33587454011865067c71b98abd6c7**, checks that every nonconstant `gcd(P,P*)` among the 648 distinct projective nonzero half-polynomials divides `z^72-1`. Its raw polynomial input is pinned as `frontier-20261028-q18-nonbinary-affine-allpolys-v1.json`, SHA **3d8ba6901009f9ea717f9d435f74560c410904ea44e7f13386a27c6c9f09a2c**. There are178 nonconstant gcds; all divide the stated polynomial.

An independently written replay `frontier-20261028-nonbinary-affine-independent-v1.py`, SHA **801a8d3c2f37179d373481770f3138ec20f87fe9ed86603f006305f5d81d77bb**, reconstructs ALL `252*45=11340` literal half-polynomials directly from H and the four masks, uses rational arithmetic in the DIFFERENT field basis Q(sqrt(-3)), regenerates the648 classes and rechecks every reciprocal gcd divisibility. It also proves the graph consisting only of identically-zero half-polynomials has no perfect matching for any E. Consequently, if any transversal exists at a unit z, at least one nonidentity half-polynomial must vanish and thus `z in mu72`.

## 3. All 72 exceptional phases fail

For every `z=zeta72^s`, s=0,...,71, `frontier-20261028-nonbinary-affine-q72-scan-v1.py` SHA **17d2873a5d77b668dbc0f39ac082b749b9a7fd398bbf9f3c8f25c1630cfcf832** verifies K(z) Hadamard and checks all252 half graphs by exact Phi72 reduction; it finds NO perfect matching. Result JSON SHA **a1245c159510f72bd449f6599283629fce7796fbadf0e75ddde1abcdf6b0771c** records all72 phases.

The independent replay SHA **801a8d3c2f37179d373481770f3138ec20f87fe9ed86603f006305f5d81d77bb** instead uses `zeta72=zeta8*zeta9^8` and the 24-dimensional product basis for Q(zeta8,zeta9), reconstructs all72 matrices and **18144** half graphs, and verifies no perfect matching. Its result SHA is **939b79f252f7ff4bbadaadb562f538b16285fbe445034fb28e85784f61ac875b**. Thus no unit phase, exceptional or generic, permits a transversal.

## 4. Boundary

The proof is for the explicitly listed one-parameter specialization only, although its masks sit in a four-parameter Hadamard family. The OTHER three-dimensional slice directions and arbitrary 4-parameter tuples remain open except where separately excluded. It does not cover all BH(10,18), other phase alphabets, nonproduct arrays or the original general 1-RQLS10. Finite gcd/endpoint certificates, the reciprocal-root caller, Hadamard reconstruction and novelty require independent review; no formal proof or target 1-RQLS is claimed.
