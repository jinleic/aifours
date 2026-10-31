# The 600-cell 4D core has an actual projective order-15 unitary

**EXACT-ALGEBRAIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:32:07 PDT 2026. This adds physical symmetry to the positive core in `frontier-20261029-600cell-circulant4d-core-v1.md` SHA-256 `c9370b9c56c57c0ef93ea501cccb0c8fbc34f287e6c418a1a4486bc384498ec1`. It is not a 6D complement or an order10 QLS.

For the exact 4D ray coordinates in that packet, put `phi=(1+sqrt(5))/2` and

```text
T = (1/4) [  0       -4        0         0       ]
          [  2phi     0       -2       sqrt(5)-1 ]
          [ 1-sqrt(5) 0      -2phi      -2       ]
          [  2        0      sqrt(5)-1  -2phi    ].
```

T is real orthogonal, sends each of the 30 selected rays to the ray attached to the context-edge translated by one modulo 15, and sends each of the 15 ONBs to the next. Exact multiplication gives `T^15=-I` and no smaller positive power is scalar. Thus T has projective order 15; `-T` itself has order 15. Its characteristic polynomial is

`x^4 - phi*x^3 + phi*x^2 - phi*x + 1`.

The polynomial and its sqrt(5)-conjugate multiply to the 15th cyclotomic polynomial, so all four eigenvalues of `-T` are primitive 15th roots.

The direct Q(sqrt(5)) replay `frontier-20261029-600cell-core-cyclic-unitary-v1.py` SHA-256 `2c8f32e484a4fb055970dd270362fea08cd6840c2e5ca526cf09433542071825` checks T's orthogonality, every one of the 30 original-vector ray actions, all 15 context shifts, powers through 15 and the characteristic polynomial. Result `frontier-20261029-600cell-core-cyclic-unitary-v1.json` SHA-256 `2231db9854dacd2e4d5f6e8710a4af6ff8fd28d98c3cf3cb8953610160aee990` is **PASS** at 02:32:07 PDT.

This shows the cyclic 6D ansatz is compatible with a **real, physically implemented** cyclic symmetry on the 4D half, not merely an abstract context-graph automorphism. A matching 6D action and rays remain unknown. The cyclic spectral no-gos exclude some population fields if that 6D action exists, but do not exclude symmetry-breaking 6D complements or general QLS10. Independent review and novelty clearance remain outstanding.
