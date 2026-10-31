# Exact minimum band size over all CS actors for the 68-source

**Status: NEW AUTHOR WRITTEN + literal exact finite certificate; UNREVIEWED / UNADOPTED.** The previously pinned ten-element optimum applies to the **fixed actual actor q**. Here an explicit twelve-element refined CS actor permits a smaller band, and an actor-independent cone argument proves that band size is optimal. This is one finite original-class source, not a general solution to Q1.

## 1. Universal lower bound 8

The source S and its table are pinned in `frontier-20261028-quotient68-faithful-host-data-v1.json`, SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`; the quotient construction and source hypotheses are in `frontier-20261028-quotient68-sixband-host-and-obstruction-v1.md`, SHA `b24ce079030e75e6f1d5dfaa2a88696f4531eb53963f507c0876d4b0ad9f599c`.

S has eight distinct idempotents with indices

`F=[0,8,16,24,36,44,52,60]`,

and `0x=x0=0` for every x∈F. For ANY homomorphism from S into a completely simple actor D, its idempotent values satisfy `r(0)≤r(x)`. The natural order on idempotents of a CS semigroup is equality, so all eight have the same actor value. A faithful physical band-by-D embedding must therefore use **eight distinct band coefficients** for those source elements. Consequently `|B|≥8`, for every actor and every band, whether finite or infinite. This proof uses no canonical-actor transport.

## 2. An eight-element SN-band host with a twelve-element actor

The exact data file `frontier-20261028-quotient68-8band-refined-actor-data-v1.json`, SHA `72bb328439b4f24919788e7379a20ea61f01ecc58dcd74f80da3f5d8ff848c40`, contains an eight-element band table, an involutory band automorphism, a source actor map and 68 band coefficients.

The actor is `D₁₂=M[C₂;{0,1},{0,1,2};P]`, with additive C₂ and sandwich matrix

```text
0 0
0 1
0 1
```

Its canonical onto map to the original eight-actor D8 identifies columns 1 and2 and preserves the row and group coordinate; the source map into D₁₂ composes to q. The source actor map is onto and pure, and D₁₂ is a genuine twelve-element completely simple semigroup. The checker verifies this information directly from the tables; the asserted host does not rely on finding or interpreting the actual syntactic quotient of D₁₂.

The eight-band is isomorphic to the idempotent upper-cone fibre on F in the source. It satisfies seminormality and has regular local corners; the displayed involution acts on it by automorphisms. The 68 coefficient values and source actor map satisfy all 4,624 physical product equations, and the 200 distinct source pairs with the same D₁₂-actor have distinct band coefficients. Thus `S→P(B₈,D₁₂)` is faithful. The physical host has 8×12=96 elements.

`frontier-20261028-quotient68-8band-refined-actor-checker-v1.py`, SHA `13712fd7111b2c9710edd0c298aa9428d5d28a06b5bb19b8ae09992512c7f99f`, completed in the Python eval kernel before Wed Oct 28 22:11:43 PDT 2026. It directly checks the eight-source-idempotent cone, all 512 band associativity triples and 4,096 seminormal substitutions, every local corner, involution/action, all source/actor products and the 200 injectivity comparisons. It does not import a solver. The host coefficients arose from finite-domain propagation in the eval kernel; the table verifier is the evidence for their correctness, not the discovery procedure.

By §§1–2 the minimum band size over **all CS actors** is exactly **8**. The strictly larger minimum **10** for the actual actor q is separately certified by `frontier-20261028-quotient68-exact-q-band-optimum-v1.md`, SHA `d9eed1b521d76da32a096b42d34f3cf66a05dc53b007613295976e73627a6174`. Hence optimizing the actor and the band factor separately is essential: actor refinement can reduce the minimum band size. The 10-band actual-q host has 80 whole-host elements, fewer than this 96-element band-optimal host; no minimum whole-host claim is made here.

All records remain same-author WRITTEN or WRITTEN-checked finite candidates. Independent source and finite-witness review is required; no novelty, formal proof, all-source Q1 or printed-convention equivalence is asserted.
