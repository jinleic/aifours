# RQLS10 v39 — GROUP-FREE extension: ALL conference/golden PHASE-ALPHABET Hadamard pairs are unresolvable, not just four central matrices

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 09:47:26 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact Hadamard/field/polynomial/Gaussian/Fourier/integer proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/accepted finite-witness claim.

## 1. Entire new phase-family theorem, with NO A5/Petersen/centrality premise

Fix r=(-1+i*sqrt15)/4. Define two classes of unit-entry COMPLEX HADAMARD matrices of order10:

    C: H_aa=1, H_ab in{+i,-i} for a!=b;
    G: H_aa=1, H_ab in{r,r^-1} for a!=b.

Every member satisfies HH^dagger=10I by definition. The classes are nonempty by v35's explicit central examples, but matrices here need NOT be central, graph-symmetric, regular, covariant or from any supplied finite list. In particular nonsymmetric G matrices are ALLOWED.

Take ANY H,K in C union G, and form the literal Hadamard-pair QLS

    q_(a,b)(s)=K_(a,s)*conj(H_(b,s))/sqrt10.       (PAIR)

Allow arbitrary INDEPENDENT row/column permutations/phases on H and K and arbitrary common unitary changes to the resulting array.

**Theorem.** No such array admits a full allowed quantum-transversal resolution. More precisely:

- GG pairs have NO quantum transversal AT ALL;
- CC pairs have ten matched real cells lying on NO quantum transversal;
- CG/GC mixed pairs have100 DISTINCT rays, but ten matched cells lying on NO quantum transversal.

This is a GROUP-FREE universal phase-pattern theorem, not merely the already closed four central matrices or their finite monomial orbits. It is still NOT arbitrary complex Hadamards, not the full TypeIV master, not an arbitrary original-array WLOG and not an unrestricted maximal1-RQLS10 no-go.

Independent row phases/permutations only rephase/relabel array cells. Independent column phases give one common coordinate diagonal. For independent column permutations, first make H canonical, then relabel K rows to align its unique exceptional1 positions with physical coordinates. This replaces K by a simultaneous row/column permutation of an otherwise arbitrary class member, still in C or G. Thus it is enough to analyze canonical PAIR with BOTH exceptional positions at a=a. No relative pairing was dropped; class membership is preserved by arbitrary simultaneous permutation, without a group-normalizer requirement.

## 2. Elementary alphabet facts and the positive mixed100-ray claim

The number r is not a root of unity because r+r^-1=-1/2 cannot be a rational algebraic integer if r were one. Its primitive irreducible polynomial is2x^2+x+2; F=Q(r)=Q(sqrt(-15)) does not contain i.

A G member can be written K_(a,s)=r^epsilon_a(s), with UNIQUE epsilon_a(a)=0 and every other epsilon in{+1,-1}. No symmetry epsilon_a(c)=epsilon_c(a) is presumed. A C member is H=I+iC0, with C0 REAL zero-diagonal signs.

For a mixed pair, all100 rays are projectively distinct. A hypothetical collision between golden row a/conference row b and golden row c/conference row d, after taking two coordinate ratios, equates a power of r to a fourth root of unity. The r exponent difference must beZERO, so epsilon_a-epsilon_c is constant across ALL coordinates. That would make the two golden Hadamard rows proportional; their orthogonality forces a=c. Then the two conference rows must likewise be proportional, forcing b=d. This argument DOES NOT incorrectly assume opposite signs at the two exceptional coordinates of a nonsymmetric G matrix.

Thus the positive mixed100-ray QLS construction really extends to the entire group-free phase class, but not to a resolvable witness.

## 3. GG: the mod3/permutation proof needs ONLY a unique zero exponent

For two distinct-row/distinct-column cells(a,b),(c,d), the unscaled inner product is a sum of ten powers r^Delta_s with Delta_s in[-4,4]. Multiplying by r^4 gives an integer polynomial P with P(1)=10. If the inner product vanishes, Gauss's lemma gives divisibility by2x^2+x+2 in Z[x]; hence P(-1) is divisible by3.

The exponent is odd exactly on the symmetric difference of{a,c} and{b,d}, because each epsilon row has its UNIQUE zero at its own label and is odd everywhere else. Therefore N_odd is0,2or4, and P(-1)=10-2N_odd is10,6or2. It must be6, forcing

    |{a,c} intersect {b,d}|=1.

A candidate transversal b=T(a) would require this for EVERY pair of distinct rows. If T has two fixed points, their pair has intersection2. Otherwise there are at leastnine nonfixed points; choose a nonfixed a and another point c outside its predecessor/successor, which exists. The corresponding pair has intersection0. Contradiction.

No symmetry/row weight/central graph was used. This is the COMPLETE proof for all GG members and all pairings, including conjugate sign choices absorbed in epsilon.

## 4. C matrices automatically are symmetric real conferences

If H=I+iC0 in C, expand

    HH^dagger=I+C0 C0^T+i(C0-C0^T)=10I.

Real/imaginary equality forces C0=C0^T and C0^2=9I. Thus symmetry is DERIVED from the Hadamard axiom, not imposed as a new convention.

Moreover ALL row products of the nine offdiagonal signs of C0 are the SAME. Symmetrically switch its first row to all+1 by a diagonal sign matrix. Orthogonality with that first row forces each other row's remaining eight signs to sumZERO, so exactlyFOUR are negative. Every switched row has offdiagonal product+1. Switching by signs s_a changes EACH original row product by the SAME factor product_a s_a, since there are nine offdiagonal factors and s_a^8=1. Hence the unswitched row products are also constant, +1or-1.

These facts hold for EVERY class C matrix, not just a permutation of the Petersen example. They supply exactly the conference hypotheses needed for the universal matched-cell Hadamard obstruction below.

## 5. Mixed pairs: the only possible matched-cell transversal would make G Hermitian, which is impossible

Put a golden K and conference H in canonical form. Fix matched cell(a,a) and compare it to a crosscell(c,d), with c!=a,d!=a. In the exact F directsum iF inner-product decomposition, only coordinates a,d have nonreal conference factors. If d!=c, the golden exponent difference at a is ODD(+1or-1), while at d it is EVEN(0,+2,-2). Thus the iF component cannot vanish: r is not a root of unity. Consequently a crosscell orthogonal to q_(a,a) MUST have d=c, i.e. itself be MATCHED.

Therefore ANY quantum transversal through ANY matched cell would have to be the ENTIRE ten-cell matched set{(c,c)}. It is not enough to test a selected relative pairing: this is forced by the exact crosscell field separation.

If that matched set were an ONB, compare matched a,c for EVERY a!=c. Conference symmetry(section4) makes their two exceptional i-factors OPPOSITE. Vanishing in F directsum iF then forces the two golden exceptional exponents to be equal:

    epsilon_c(a)=-epsilon_a(c).

Thus K_(c,a)=conj(K_(a,c)) for every offdiagonal pair, while the diagonal is1: the golden matrix K would be HERMITIAN. But then its Hadamard identity gives K^2=10I, so its eigenvalues are+-sqrt10. Its trace is10 from its diagonal. No integer difference of multiplicities times irrational sqrt10 can equal the nonzero rational10. Contradiction.

Hence the full matched set is not an ONB, and NO quantum transversal passes through ANY matched cell. Exchanging category orders by transposition/complex conjugation preserves the result. This repairs a genuine scope hazard: for a NONSYMMETRIC G member, different matched cells can have the SAME exceptional exponent, so the simpler central-v35 opposite-odd argument must NOT be copied. The Hermitian-trace argument is what closes the larger family.

## 6. CC: the full conference matched-cell obstruction uses NO central graph

For arbitrary two C members, section4 gives symmetric real conferences with constant row-sign products. Their ten matched q_(a,a) are REAL+-1 vectors with the SAME entry product, so two cannot be orthogonal in length10 (orthogonality would require exactlyFIVE sign disagreements, reversing their products).

A transversal through one matched cell has exactlyONE matched cell. After real-only dephasing its hypothetical fourth-root Hadamard is

    T=[[1,1^T],[1,A+iB]],

with9x9 integer A,B, disjoint supports, B imaginary support I+P_f for a nine-point derangement. The COMPLETEv37 Gaussian-prime argument forces f to be ONE9-cycle: dividingA-J+iB by1+i reduces to I+P_f overF2; cycle countc yields determinant valuation>=9+c while NormdetT=10^10 gives10.

The COMPLETEv38 rigidity argument then applies verbatim and uses NO Petersen fact: row/column sums force B=+-(I-R); both Hadamard real equations make A normal with AA^T=A^TA=10I-J-(2I-R-R^-1); row sums make it commute with cycle adjacency. Its zero diagonal and the odd9-cycle Fourier decomposition force A circulant. The imaginary equation gives

    (I-R)(A^T+R^-1 A)=0.

The integer matrix in parentheses has constant columns with column sum-2, forcing every entry-2/9, impossible. Thus no matched-cell transversal exists.

All Gaussian-entry reduction, rank/divisibility, sign, Fourier and integrality steps are part of the ENTIREv37/v38 dependency and must be reconstructed for this extension. Their hypotheses have now been proved for EVERY C member, not asserted from membership in an unprovided finite classification.

## 7. Whole new boundary and remaining original problem

No full resolution can avoid ten matched cells. Sections3,5,6 therefore prove the group-free theorem for ALL pairs in C union G and all independent monomial changes. The four central Petersen examples ofv35 are merely nonempty subclasses. No classification of G matrices, row-weight regularity, symmetry of G, group covariance, graph normalizer or finite enumeration was required.

This result does NOT exclude arbitrary complex-Hadamard pairs with other phase alphabets or without a unique exceptional phase per row/column, nor the complete TypeIV biunitary master or arbitrary original irreducible10/4+6/5+5 arrays. All those original branches remain OPEN. A new construction must leave this CLOSED two-alphabet class rather than change a relative permutation or try another resolution inside it.

An ENTIRE gate needs ALLseven sections/endings plus operative fullv37/v38 and v35's non-root/quadratic facts as used: especially the nonsymmetric-G mixed exception and Hermitian trace, and the proof that arbitrary C is symmetric/constant-row-product. A central-family spotcheck is not the new theorem. Exact WRITTEN only; no independent finite-witness/checker/control/vendor/priority gate performed or passed. No100-ray1-RQLS witness/unrestrictedno-go/formal/kernel/family/human/current-openness/novelty promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early pending-review park.
