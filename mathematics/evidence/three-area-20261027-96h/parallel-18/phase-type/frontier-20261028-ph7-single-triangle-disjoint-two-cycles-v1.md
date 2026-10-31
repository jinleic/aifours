# A critical single triangle cannot be disjoint from all 2-cycles when there is no 4-cycle

**NEW ALL-TOPOLOGY WRITTEN APPLICATION, conditional on the named exact one-triangle spectral certificate and separately reviewed Perron facts. Independent peer review/novelty clearance pending.** MathResearch96h-2. This extends the exact `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md`, SHA256 `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc`, beyond graphs with no 2-cycles. It is not an unrestricted PH7 impossibility theorem.

## Theorem

At z=8/9, an irreducible seven-state Metzler matrix of spectral bound0, whose actual characteristic polynomial contains `D(y)=y[(y+1)^2+8/9]^2`, cannot simultaneously have

1. exactly one directed 3-cycle C;
2. no directed 4-cycle; and
3. no vertex of C incident to a directed 2-cycle.

There may be arbitrarily many 2-cycles among the other four vertices and arbitrarily many longer directed cycles/edges. Hence a critical PH7 candidate with exactly one triangle and no 4-cycle must have at least one bidirectional edge INCIDENT to that triangle. This is conditional structural progress, not a 7-state exclusion.

## 1. A block-diagonal symmetric comparison

Normalize G to an irreducible row generator by positive Perron similarity. Its three triangle diagonal escape rates u1,u2,u3 remain positive, and its triangle edge product w is unchanged. Let `S_ii=G_ii` and `S_ij=sqrt(G_ij G_ji)`. Because no triangle vertex is incident to a 2-cycle, S is block diagonal:

    S=diag(-u1,-u2,-u3) direct-sum S4.

The mandatory-triangle proof gives `S<=0`. In fact `S4<0`: pick k sufficiently large that `A=kI+G` is irreducible nonnegative with Perron root k. Its proper principal 4-by4 block A4 has spectral radius <k. By Cauchy–Schwarz and positive Perron comparison, the geometric-mean symmetrization of A4 has spectral radius <=rho(A4); if A4 is reducible, apply the same argument to A4+epsilon*11^T and let epsilon↓0. Therefore every eigenvalue of S4 is strictly negative. Write its four positive eigenrates as `v1,...,v4`.

S has no triangle: an S triangle would make both directed orientations positive in G, producing at least TWO directed 3-cycles, contradicting uniqueness. It has no 4-cycle because every S edge is bidirectional in G. All 2-cycle products in characteristic coefficients agree exactly between G and S.

## 2. Reproduce the exact one-triangle coefficient system

Let w be the product of the actual sole directed triangle in G. Its three row fractions multiply to `theta=w/(u1u2u3)` in(0,1]. The G and S coefficients of y6,y5 agree. At y4, S has no triangle and G has exactly the one, so

    [y^4]det(yI-G)=[y^4]det(yI-S)-w.

At y3, 2-cycle/diagonal terms and disjoint 2+2 terms agree, while both graphs have no 4-cycle. The triangle term is `-w` times the sum of diagonal escape rates outside C, so

    [y^3]det(yI-G)=[y^3]det(yI-S)-w sum_(i outside C)(-G_ii).

The final sum is `trace(-S4)=v1+...+v4`. Thus these four characteristic coefficients are EXACTLY those of a diagonal product with seven positive rates `u1,u2,u3,v1,...,v4`, with the same unique-triangle corrections used in the named full one-triangle source.

Choose any two of v1,...,v4 as the auxiliary fourth/fifth rates and treat the other two by their real sum/product. The named exact 5D Bernstein certificate proves its discriminant numerator strictly positive for every positive five-rate choice and every `theta in[0,1]`; hence the required real sum/product cannot exist. It applies unchanged, including a zero determinant of the outer linear coefficient system. Contradiction. □

This coefficient transfer is an application of the existing 2311-leaf certificate, not a new execution or stronger certificate. A reviewer must independently check S4 strict stability, all 2/2+2 terms, the unique-triangle outside trace, and the certificate's graph-independent coefficient interface.

## Limits

The theorem does not cover a 4-cycle, multiple triangles, or a bidirectional edge touching the triangle. Those are exactly the remaining graph directions in this local structural branch. It does not establish a critical PH7 exclusion, minimum8, novelty, formal/Lean/kernel proof or independent-review acceptance. Held records remain nonpremises and historic process findings remain.

END — with one triangle and no 4-cycle, a critical PH7 candidate must have a 2-cycle touching that triangle.
