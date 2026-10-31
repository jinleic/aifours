# Level seven: thirteen small oriented primitive types for all positive parameters

Owner **MathKacMoody-2**, original math-3. Actual native `/bin/date` observed before this immutable write: **Thu Oct 29 03:52:25 PDT 2026**. **NEW WRITTEN/EXACT-COMPUTATION-SUPPORTED SCIENTIFIC CANDIDATE at explicit actual-source/classical inputs.** Alternate implementations were exercised in this harness with shared NumPy/FLINT. Independent scientific review and parent disposition PENDING.

## 1. Claim

For the ORIGINAL A(r,s)=[[2,-1,-1],[-1,2,-1],[-r,-s,2]], EVERY positive INTEGER pair r,s and EVERY allowed FULL complex Cartan realization C, let S=G_C/J be the ACTUAL Serre quotient. For each representative

    (a,b)=(1,0),(2,0),(3,0),(1,1),(2,1),(3,1),(4,1),

the ORIGINAL map D3=ad f3 is injective on the ENTIRE actual f1/f2-lowest space of S_(a,b,7). Node1/2 exchange sends A(r,s) to A(s,r) and root(a,b,7) to(b,a,7); because every positive pair is covered, the six non-diagonal transposes follow. This gives THIRTEEN oriented level7 types.

Together with earlier separate candidates for(2,2),(3,2),(2,3),(2,4),(4,2), the new(3,3) packet and the new invariant(7,7) packet, twenty of the31 oriented level7 lowest types are now covered for all parameters. The remaining eleven oriented types are(4,3),(3,4),(5,3),(3,5),(4,4),(5,4),(4,5),(5,5),(6,5),(5,6),(6,6). No B7, whole-level, all-level/book, status, novelty or priority claim is made.

## 2. Inputs and new written lemmas

Actual-source inputs: `frontier-20261028-fixed-levi-level1-independent-v1.md`, SHAa001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a, and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md`, SHAe5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f, Sections0–4, with PBW qualification21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247. Classical inputs are finite sl3 complete reducibility/classification/duality, Witt/Lyndon free-Lie facts and finite-A2 Weyl extraction. These are substantive candidate inputs, not adoptions.

The rank arguments use the new written lemmas `frontier-20261029-quotient-stable-contraction-descent-v1.md` (SHAd42a3664cfda9ee1729007368c993667a739209bab6295b3edbb0ecc44827717), `frontier-20261029-whole-seed-ideal-lowest-projection-v1.md` (SHAa78deb93b99908efe166f7dfeabde3dda9f80cdb92fe5c5651243cb01c887488), and Sections3–4 of `frontier-20261029-level7-33-all-parameters-candidate-v1.md` (SHAd0c1b60356e18fa8b7db22da459823fbcdf942ac4ae42aa86c49889d03837624): each one-seed ideal is the positive part of an honest Lie ideal because theta=(ad e3)^(p+1)e_i is killed by every f_k, and invertibility on P/N1 descends to P/N whenever N1 is contained in the stable actual kernel N. All require independent mathematical review.

## 3. Complete free sources and free-region positivity

For each representative, `frontier-20261029-level7-canonical-small-type.py` solves the WHOLE free f1/f2 nullspace in the complete Lyndon basis of root(a,b,7), checks every primitive vector horizontal and independent, and matches the exact Witt/Weyl multiplicity. It then constructs the complete canonical contraction pencil Omega(r,s)=A+(r-7)B+(s-7)C in that basis, with all three full coordinate-matrix products checked. `frontier-20261029-level7-canonical-determinant.py` interpolates the complete determinant from the full triangular grid.

All seven determinants have only positive coefficients at x=r-7,y=s-7. The existing independent replay `frontier-20261029-level7-canonical-independent-replay.py` imports no producer, rebuilds the entire source with separate string-Lyndon/tree-Jacobi algebra and literal theta-negative words, recomputes all3 matrices and checks the whole polynomial on a DIFFERENT shifted unisolvent triangle.

| Type | free lowest dim | polynomial terms | shifted replay determinants | least uniform positive bound b0 |
|---|---:|---:|---:|---:|
| (1,0,7) | 1 | 2 | 3 | 7 |
| (2,0,7) | 2 | 3 | 6 | 3 |
| (3,0,7) | 2 | 3 | 6 | 3 |
| (1,1,7) | 6 | 28 | 28 | 3 |
| (2,1,7) | 17 | 165 | 171 | 3 |
| (3,1,7) | 24 | 297 | 325 | 3 |
| (4,1,7) | 12 | 81 | 91 | 3 |

At r,s>=b0, the translated free determinant has a nonzero constant and only positive coefficients; free-source contraction descent proves actual injectivity there, whatever the actual Serre ideal.

## 4. Every lower row and corner on the actual quotient

`frontier-20261029-level7-type-actual-quotients.py` expands the complete normalized free source into all tensor words, forms the entire compact finite-Levi Gram by arbitrary-integer arithmetic, and for each node and small parameter p<b0 includes EVERY ordered root-matching nested M-letter descendant of the literal lowest seed. Projected coordinates H^(-1)b give the ENTIRE one-seed lowest ideal. The canonical one-seed quotient is an affine pencil in t=other_parameter-b0; its univariate determinant is interpolated, and the least base where all translated coefficients are nonnegative with positive constant is recorded. Any row points below that base are added to the explicit corner set. Every corner uses the ENTIRE two-seed ideal sum, retains overlaps, and computes the induced contraction on the actual quotient. Every needed ideal is checked contraction-stable.

Results: all rows certify from other parameter b0, except (1,1): p=1 from5 and p=2 from4, and (2,1): node2 p=2 from4. All explicit actual corner contractions are nonsingular. The actual lowest source vanishes at every listed corner except (2,1,7) at(r,s)=(3,2), where it has dimension1 with nonzero induced determinant. In the(1,0,7) case the source is the r=6 Serre seed descendant; its free determinant has the single root r=6, where the actual source is zero; this agrees with the classical sl2 identity [f3,(ad e3)^7e1]=-7(6-r)(ad e3)^6e1.

`frontier-20261029-level7-type-actual-quotients-replay.py` imports no producer. It rebuilds the normalized source with the older separate Lyndon implementation, reconstructs the whole Gram by Hadamard diagonalization, recomputes all seven free-bound tests by stdlib integer binomial translation, regenerates seeds by repeated tuple brackets with sparse G on descendants, uses transpose evaluation RREF and explicit annihilator quotients, checks each row polynomial at all shifted exact matrix determinants, and recomputes every corner determinant. Totals: (descendants, shifted row matrix determinants, corners)=(6,18,36),(9,8,4),(16,8,4),(18,10,10),(66,24,5),(129,40,4),(146,24,4) for the seven representatives in the order of Section1.

## 5. Coverage and assurance

For each representative the disjoint regions r,s>=b0; one parameter<b0 with the other at or above its certified row base; and all explicit corners exhaust EVERY positive integer pair. The quoted actual dimensions are not claimed outside the computed rows/corners. `frontier-20261029-level7-thirteen-small-types-manifest-v1.json` binds the sources, pencils, polynomials, free replays, actual certificates and replays.

All results remain same-owner exact/WRITTEN candidates with shared NumPy2.4.3/FLINT0.9.0. Independent disjoint source/mathematics/code review and parent disposition remain pending. No formal/kernel, configured-family/human, native-library, B7, status, novelty or priority acceptance is claimed. Historical immutable held/ZERO/STOP/HOLD/process records and original deadline2026-10-31T21:23:27Z remain unchanged.

**END — thirteen small oriented level7 primitive types, all positive parameters, named inputs; eleven oriented types remain.**
